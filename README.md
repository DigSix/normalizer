<h1 align="center">Normalizer</h1>

<p align="center">
  <img alt="Project Status" src="https://img.shields.io/badge/status-in%20development-yellow">
  <img alt="Made with Python" src="https://img.shields.io/badge/made%20with-Python-blue">
  <img alt="Maintained by DigSix" src="https://img.shields.io/badge/maintained%20by-DigSix-56BEB8">
</p>
<br>

## 🎯 About ##

**Normalizer** is a **Python** project developed to automate the process of **downloading, decompressing, and cleaning files** received via **SFTP**.  
It organizes and normalizes text files (`.gz` and `.txt`), keeping only the processed and cleaned data in a folder ready for integration with other systems.
This tool was created to **automate a manual task** I had to perform daily at work, saving time and reducing the risk of human error.

---

## ✨ Features ##

Connection to SFTP server via `.env`;  
Automatic download of files from the last 24 hours;  
Automatic decompression of `.gz` files;  
Cleaning and standardization of text lines;  
Daily automated execution via internal loop or Docker;  
Simple HTTP server to expose normalized files.

---

## 🚀 Technologies ##

The following tools were used in this project:

- [Python 3.x](https://www.python.org/)
- [Paramiko](https://www.paramiko.org/) — SFTP connection  
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` configuration  
- [gzip / shutil / os] — File manipulation and decompression  
- [Docker](https://www.docker.com/) — Automated and isolated execution  

---

## ✅ Requirements ##

Before starting, make sure you have installed:

- [Git](https://git-scm.com)  
- [Python 3.x](https://www.python.org/)  
- (Optional) [Docker](https://www.docker.com/)

---

## 🏁 Getting Started ##

```bash
# Clone this repository
$ git clone https://github.com/DigSix/normalizer

# Access the project folder
$ cd normalizer

# Create the virtual environment
$ python -m venv venv
$ source venv/bin/activate  # (or venv\Scripts\activate on Windows)

# Install dependencies
$ pip install -r requirements.txt

# Configure the .env file
SFTP_HOST=your.server.com
SFTP_PORT=22
SFTP_USER=username
SFTP_PASS=password

# Run the main script
$ python main.py

# Run the server
$ python server.py
```

The process automatically runs every day at **08:00**, downloading and cleaning the latest files.

---

## 🐳 Running with Docker ##

```bash
# Build the image
$ docker build -t normalizer .

# Run in background with memory limit
$ docker run -d -m 512m --name normalizer normalizer
```

---

## 📝 License ##

This project is under the **MIT** license.  
See the [LICENSE](LICENSE.md) file for more details.

---

Made with :coffee: and :snake: by <a href="https://github.com/DigSix" target="_blank">YOUR_NAME</a>

&#xa0;

<a href="#top">Back to top</a>
