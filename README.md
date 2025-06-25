
# 🖨️ 3D Printer Web Controller

A web application for **remote control of a 3D printer** via serial port.  
Upload your G-code files and start printing right from your browser! 🚀

---

## ✨ Features

- 🖥️ Easy-to-use Flask web interface for file uploads  
- 🧵 Asynchronous printing using threads — keeps the server responsive  
- 🔌 Sending commands and reading responses from the printer via `pyserial`  
- 🎨 Colorful terminal logs using `colorama` for easy debugging  

---

## 🚀 Quick Start

1. Clone this repo and navigate to the project folder  
```bash
git clone https://github.com/Zitrul/3dprinter-web.git
cd 3dprinter-web
```
2. Run the server  
```bash
python app.py
```
3. Open in your browser 👉 [http://localhost:2000](http://localhost:2000) and upload your G-code file to print 🎉

---

## ⚙️ Configuration

- Define your 3D printers in `config.py`:  
```python
PRINTERS = [
    {
        "name": "ANYCUBIC I3 MEGA",
        "baud": 250000,
        "port": "COM4",
        "status": "w"
    }
]
```
- Set the upload path in `UPLOAD_FOLDER`

---

## 🔍 How It Works

- Upload a G-code file through the web form  
- The server saves the file and starts a separate print thread  
- Commands are sent to the printer line-by-line  
- Printer replies "ok" — then the next command is sent  
- Printer status changes to prevent conflicting print jobs

---

## 🧰 Requirements

- Python 3.x  
- Flask  
- pyserial  
- colorama  
- werkzeug  

---

## 🤝 Contributing

Want to help improve the project?  
Pull requests and ideas are welcome! 💡

- Fork this repo  
- Add your feature  
- Open a PR  

Or just open an issue if you have questions or suggestions.

---

## 📄 License

MIT License — use freely for any projects!  
Appreciate attribution but it’s not required 😉

---

## 📬 Contact

Feel free to reach out if you have questions or want to chat: ardutex@gmail.com  
Happy printing! 🖨️✨
