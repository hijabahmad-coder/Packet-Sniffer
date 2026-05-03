```markdown
# 📡 Packet Sniffer - Network Traffic Monitor

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A real-time network traffic monitoring web application built with **Flask** and **Python**. Capture, analyze, and visualize network packets through an intuitive web dashboard.

---

## ✨ Features

- 🔍 **Real-time Packet Capture** - Monitor network traffic live
- 📊 **Traffic Analytics** - View statistics and patterns
- 📁 **CSV Data Support** - Export/Import traffic data
- 🎨 **Interactive Dashboard** - User-friendly web interface
- ⚡ **Lightweight** - Minimal resource usage
- 🔒 **Safe Monitoring** - Passive packet analysis

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Backend logic |
| Flask | Web framework |
| Pandas | Data processing |
| Scapy | Packet capture |
| HTML/CSS | Frontend interface |

---

## 📁 Project Structure

```
Packet-Sniffer/
└── network_monitor/
    ├── assets/          # CSS, JS, images
    ├── templates/       # HTML files
    │   └── index.html   # Main dashboard
    ├── data.csv         # Traffic data storage
    ├── app.py           # Main application
    └── README.md        # Documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Administrator/root privileges (for packet capture)

### Step 1: Clone the Repository
```bash
git clone https://github.com/hijabahmad-coder/Packet-Sniffer.git
cd Packet-Sniffer/network_monitor
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install flask pandas scapy
```

Or if you have requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
Navigate to: `http://127.0.0.1:5000`

---

## 📖 Usage Guide

1. **Start the server** - Run `python app.py`
2. **Open dashboard** - Go to `http://localhost:5000`
3. **Start capture** - Click "Start Monitoring" button
4. **View statistics** - See live packet data
5. **Export data** - Save traffic logs to CSV

---

## 📊 CSV Data Format

The `data.csv` file stores captured traffic with following columns:

| Column | Description |
|--------|-------------|
| timestamp | Time of capture |
| src_ip | Source IP address |
| dst_ip | Destination IP address |
| protocol | Protocol (TCP/UDP/ICMP) |
| length | Packet size in bytes |
| info | Additional information |

---

## 🔧 Configuration

You can modify these settings in `app.py`:

```python
# Change network interface
interface = "eth0"  # Windows: "Wi-Fi" or "Ethernet"

# Change port
app.run(debug=True, port=5000)

# Update CSV path
CSV_FILE = "data.csv"
```

---

## ⚠️ Important Notes

- 🔐 **Administrator privileges** required for packet capture
- 🌐 Only monitors traffic on your local network interface
- 📡 Does not capture encrypted packet payloads
- 🛡️ For educational purposes only

---

## 🐛 Troubleshooting

### Error: "No module named 'flask'"
```bash
pip install flask
```

### Error: "Permission denied" (Linux/Mac)
```bash
sudo python app.py
```

### Error: "Network interface not found"
- Check your network adapter name
- Update `interface` variable in `app.py`

### Port 5000 already in use
```bash
# Change port in app.py
app.run(port=5001)
```

---

## 📝 To-Do / Future Improvements

- [ ] Add real-time graphs
- [ ] Email alerts for suspicious traffic
- [ ] Mobile-responsive design
- [ ] Dark mode support
- [ ] Export to PCAP format
- [ ] Multi-interface support

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

This project is licensed under the **MIT License** - see below:

```
MIT License

Copyright (c) 2026 hijabahmad-coder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 👨‍💻 Author

**Hijab Ahmad**  
- GitHub: [@hijabahmad-coder](https://github.com/hijabahmad-coder)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Python Network Programming](https://realpython.com/python-networking/)

---

**Happy Monitoring! 📡**
