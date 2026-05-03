# Computer_Networks
```markdown
# Network Traffic Monitor

A lightweight network traffic monitoring and analysis tool with web-based interface. Supports both CSV data analysis and live packet capture.

## 📋 Requirements Fulfilled

| Requirement | Status |
|-------------|--------|
| Start/Stop Monitoring | ✅ |
| Display Table for Network Data | ✅ |
| Log/Record Display Section | ✅ |
| Basic Statistics Section | ✅ |
| Filter (Protocol, Source IP, Destination IP) | ✅ |
| Reset/Clear Filter Button | ✅ |
| Service Column (Port Mapping) | ✅ |
| CSV Dataset Support | ✅ |
| Live Packet Sniffing | ✅ (Bonus) |

## 🚀 Features

- 📁 **CSV Mode** - Load and analyze pre-recorded packet data
- 🔴 **Live Capture Mode** - Real-time packet sniffing using Scapy
- 🎛️ **Packet Filtering** - By Protocol (TCP/UDP/ICMP), Source IP, Destination IP
- 📊 **Statistics** - Total packets, protocol breakdown, average packet size
- 🔌 **Port-to-Service Mapping** - HTTP(80), HTTPS(443), DNS(53), SSH(22), MySQL(3306), and more
- 🎮 **Start/Stop Control** - Toggle monitoring on/off
- 🌐 **Web Interface** - Clean, responsive HTML/CSS dashboard

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python + Flask |
| Packet Capture | Scapy |
| Frontend | HTML5, CSS3 |
| Templating | Jinja2 |
| Data Format | CSV |

## 📋 Prerequisites

- Python 3.7 or higher
- pip package manager
- Administrator/root privileges (for Live Capture Mode only)

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/hijabahmad-coder/network-traffic-monitor.git
cd network-traffic-monitor

# Install dependencies
pip install flask scapy
```

## 💻 Usage

### Start the Application

```bash
python app.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

### CSV Mode (No admin rights needed)

1. Click **"CSV Mode"** button
2. Click **"START"** button
3. View packets from `data.csv` file
4. Apply filters or view statistics

### Live Capture Mode (Requires Administrator)

**Windows:** Run Command Prompt as Administrator
**Linux/Mac:** Run with `sudo`

```bash
# Windows (Admin CMD)
python app.py

# Linux/Mac
sudo python app.py
```

Then:
1. Click **"Live Capture Mode"** button
2. Click **"START"** button
3. Generate network traffic (e.g., `ping google.com -t`)
4. Watch packets appear in real-time
5. Click **"STOP"** to end capture

## 📊 Dataset Format (data.csv)

| Field | Type | Description |
|-------|------|-------------|
| Time | String | Timestamp (HH:MM:SS) |
| Source IP | String | Sender IPv4 address |
| Destination IP | String | Receiver IPv4 address |
| Protocol | String | TCP, UDP, or ICMP |
| Packet Size | Integer | Bytes |
| Source Port | Integer | Ephemeral port |
| Destination Port | Integer | Well-known port |

### Sample Record

```csv
Time,Source IP,Destination IP,Protocol,Packet Size,Source Port,Destination Port
10:35:21,192.168.1.5,8.8.8.8,TCP,512,52341,80
```

## 🗺️ Port-to-Service Mapping

| Port | Service | Port | Service |
|------|---------|------|---------|
| 80 | HTTP | 443 | HTTPS |
| 53 | DNS | 22 | SSH |
| 25 | SMTP | 21 | FTP |
| 3306 | MySQL | 5432 | PostgreSQL |
| 8080 | HTTP-Alt | 110 | POP3 |
| 143 | IMAP | - | - |

## 📁 Project Structure

```
network-traffic-monitor/
│
├── app.py              # Flask backend + packet processing
├── data.csv            # Pre-recorded packet dataset
├── templates/
│   └── index.html      # Web interface template
└── README.md           # This file
```

## 🧪 Testing Live Capture

1. Run application as Administrator
2. Select **Live Capture Mode**
3. Click **START**
4. Open Command Prompt and run: `ping google.com -t`
5. Switch back to browser - ICMP packets will appear
6. Press `Ctrl+C` in CMD to stop ping
7. Click **STOP** in browser

## ⚠️ Important Notes

- **Live Capture Mode** requires administrator/root privileges
- CSV Mode works without any special permissions
- Live capture stores last 100 packets for performance
- Filter works on captured packets (stop capture, then filter)

## 📸 Screenshots

| Mode | Description |
|------|-------------|
| CSV Mode | Static data from data.csv file |
| Live Mode | Real-time packets from network interface |
| Filter | Filter by protocol, source/destination IP |
| Statistics | Total packets, protocol breakdown, avg size |

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 Author

**Hijab Ahmad**

- GitHub: [@hijabahmad-coder](https://github.com/hijabahmad-coder)
## 📄 License

This project is for educational purposes as part of Computer Networks course.

---

⭐ Star this repository if you found it useful!
```


Ab aapka GitHub repo professional lagega! 🚀

**Koi aur change chahiye?** Batao!
