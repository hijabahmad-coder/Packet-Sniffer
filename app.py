from flask import Flask, render_template, request
import csv
import threading
import time
from datetime import datetime
import os
import sys

app = Flask(__name__)

# Global variables
monitoring = False
live_mode = False
all_packets = []
captured_packets = []
sniffer_thread = None
stop_sniffing = False

# Service mapping function
def get_service(port):
    services = {
        80: 'HTTP',
        443: 'HTTPS',
        53: 'DNS',
        22: 'SSH',
        25: 'SMTP',
        21: 'FTP',
        3306: 'MySQL',
        5432: 'PostgreSQL',
        8080: 'HTTP-Alt',
        110: 'POP3',
        143: 'IMAP'
    }
    return services.get(port, 'Other')

# Load data from CSV file
def load_csv_data():
    data = []
    try:
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dest_port = int(row.get('Destination Port', 0))
                service = get_service(dest_port)
                row['Service'] = service
                data.append(row)
        print(f"Loaded {len(data)} packets from data.csv")
    except FileNotFoundError:
        print("data.csv not found, starting with empty dataset")
        # Create sample data if file doesn't exist
        create_sample_csv()
        return load_csv_data()
    except Exception as e:
        print(f"Error loading CSV: {e}")
    return data

def create_sample_csv():
    """Create a sample CSV file if it doesn't exist"""
    sample_data = [
        ['Time', 'Source IP', 'Destination IP', 'Protocol', 'Packet Size', 'Source Port', 'Destination Port'],
        ['10:35:21', '192.168.1.5', '8.8.8.8', 'TCP', '512', '52341', '80'],
        ['10:35:22', '192.168.1.6', '1.1.1.1', 'UDP', '128', '54321', '53'],
        ['10:35:23', '192.168.1.7', '192.168.1.1', 'ICMP', '64', '0', '0'],
        ['10:35:24', '192.168.1.5', '203.0.113.5', 'TCP', '1024', '52342', '443'],
        ['10:35:25', '192.168.1.8', '8.8.4.4', 'UDP', '256', '54322', '53'],
    ]
    
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print("Created sample data.csv file")

# Function to process a single packet (for live capture)
def process_packet(packet):
    global captured_packets
    
    if not monitoring or stop_sniffing:
        return
    
    try:
        # Check if packet has IP layer
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            protocol_num = packet['IP'].proto
            
            # Map protocol number to name
            proto_map = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}
            proto_name = proto_map.get(protocol_num, 'Other')
            
            # Get packet size
            packet_size = len(packet)
            
            # Get timestamp
            timestamp = datetime.now().strftime('%H:%M:%S')
            
            # Get port information for TCP/UDP
            src_port = 0
            dst_port = 0
            service = 'Other'
            
            if proto_name == 'TCP' and packet.haslayer('TCP'):
                src_port = packet['TCP'].sport
                dst_port = packet['TCP'].dport
                service = get_service(dst_port)
            elif proto_name == 'UDP' and packet.haslayer('UDP'):
                src_port = packet['UDP'].sport
                dst_port = packet['UDP'].dport
                service = get_service(dst_port)
            elif proto_name == 'ICMP':
                service = 'ICMP'
            
            # Create packet record
            packet_record = {
                'Time': timestamp,
                'Source IP': src_ip,
                'Destination IP': dst_ip,
                'Protocol': proto_name,
                'Packet Size': packet_size,
                'Source Port': src_port,
                'Destination Port': dst_port,
                'Service': service
            }
            
            # Add to captured packets (keep last 100 for performance)
            captured_packets.insert(0, packet_record)
            if len(captured_packets) > 100:
                captured_packets.pop()
                
            print(f"Captured: {src_ip} -> {dst_ip} [{proto_name}]")  # Debug output
            
    except Exception as e:
        print(f"Error processing packet: {e}")

# Sniffing function to run in background thread
def start_live_sniffing():
    global stop_sniffing, captured_packets
    from scapy.all import sniff
    
    print("Live sniffing started...")
    stop_sniffing = False
    captured_packets = []
    
    # Start sniffing (will run until stop_sniffing becomes True)
    try:
        sniff(prn=process_packet, stop_filter=lambda x: stop_sniffing, store=False)
    except Exception as e:
        print(f"Sniffing error: {e}")
    print("Live sniffing stopped...")

# Load initial CSV data
all_packets = load_csv_data()

@app.route('/', methods=['GET', 'POST'])
def home():
    global monitoring, live_mode, sniffer_thread, stop_sniffing, captured_packets
    
    # Determine which packets to display
    if live_mode and monitoring:
        display_packets = captured_packets.copy()
    else:
        display_packets = all_packets.copy()
    
    filtered_packets = display_packets.copy()
    
    if request.method == 'POST':
        # Start button
        if 'start' in request.form:
            monitoring = True
            # If in live mode but no sniffing thread, start it
            if live_mode and (sniffer_thread is None or not sniffer_thread.is_alive()):
                stop_sniffing = False
                sniffer_thread = threading.Thread(target=start_live_sniffing, daemon=True)
                sniffer_thread.start()
        
        # Stop button
        elif 'stop' in request.form:
            monitoring = False
            if live_mode:
                stop_sniffing = True
                time.sleep(0.5)
        
        # Switch to CSV mode
        elif 'csv_mode' in request.form:
            live_mode = False
            monitoring = False
            stop_sniffing = True
            if sniffer_thread:
                time.sleep(0.5)
        
        # Switch to Live mode
        elif 'live_mode' in request.form:
            live_mode = True
            monitoring = False
            captured_packets = []
        
        # Clear captured packets
        elif 'clear_logs' in request.form:
            if live_mode:
                captured_packets = []
        
        # Filter form submitted
        elif 'filter' in request.form:
            protocol = request.form.get('protocol')
            src_ip = request.form.get('src_ip')
            dst_ip = request.form.get('dst_ip')
            
            if protocol and protocol != 'All':
                filtered_packets = [p for p in filtered_packets if p['Protocol'] == protocol]
            if src_ip:
                filtered_packets = [p for p in filtered_packets if src_ip in p['Source IP']]
            if dst_ip:
                filtered_packets = [p for p in filtered_packets if dst_ip in p['Destination IP']]
        
        elif 'reset' in request.form:
            filtered_packets = display_packets.copy()
    
    # If monitoring is stopped, show empty list
    if not monitoring:
        filtered_packets = []
    
    # Calculate statistics
    total = len(filtered_packets)
    tcp = sum(1 for p in filtered_packets if p['Protocol'] == 'TCP')
    udp = sum(1 for p in filtered_packets if p['Protocol'] == 'UDP')
    icmp = sum(1 for p in filtered_packets if p['Protocol'] == 'ICMP')
    
    total_size = 0
    for p in filtered_packets:
        try:
            total_size += int(p['Packet Size'])
        except:
            total_size += 0
            
    avg_size = total_size / total if total > 0 else 0
    
    stats = {
        'total': total,
        'tcp': tcp,
        'udp': udp,
        'icmp': icmp,
        'avg_size': round(avg_size, 2)
    }
    
    return render_template('index.html', 
                         packets=filtered_packets, 
                         stats=stats, 
                         monitoring=monitoring,
                         live_mode=live_mode)

if __name__ == '__main__':
    print("=" * 50)
    print("Network Traffic Monitor Starting...")
    print(f"CSV Mode: {len(all_packets)} packets loaded")
    print("Open browser at: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, threaded=True, host='127.0.0.1', port=5000)