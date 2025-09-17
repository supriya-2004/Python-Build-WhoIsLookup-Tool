# Python-build-Whoislookup-tool

This is a simple command-line tool built in Python for performing WHOIS lookups on a list of domains. It can take domain names as space-separated arguments or read a list of domains from a file.

The tool provides a clean output, showing only the domain and its corresponding registrar, which is useful for quick audits or data collection.

---

## 🧩 Features
- **Command-line input**: Look up one or more domains by passing them as arguments.  
- **File input**: Read a list of domains from a text file.  
- **Graceful error handling**: The script will continue to run even if a lookup for a specific domain fails.  

---

## 🛠️ Prerequisites
- Python **3.x**  
- The `python-whois` library  
```bash
pip install python-whois
```

---

## Usage
1. **Lookup with Command-Line Arguments**
To perform a lookup for one or more domains, provide them as space-separated arguments directly to the script:
```bash
python whois_lookup.py google.com wikipedia.org
```

2. Lookup with a File
You can also provide a list of domains in a text file, with one domain per line.

Create a file (e.g., `input.txt`):
```bash
domain1.com
domain2.net
domain3.org
```
Then, run the script with the `--file` flag:
```bash
python whois_lookup.py --file input.txt
```

---

## ✅ Learning Outcomes
By building this tool, I have gained experience with:

- **Command-line Interface (CLI) development**: Using `argparse` to create a robust and user-friendly CLI.

- **External Libraries**: Integrating and using a third-party Python library (`python-whois`) to add powerful functionality.

- **File I/O**: Reading and processing data from text files.

- **Error Handling**: Implementing `try-except` blocks to handle potential issues gracefully.

- **Code Structure**: Organizing a script into functions (`get_registrar`, `main`) for better readability and maintainability.

---

## 🔚 Conclusion
This project serves as an excellent foundation for building more complex command-line applications. You can expand its capabilities by adding features such as parallel lookups, rate limiting, and support for additional data outputs from the WHOIS records. This tool demonstrates the power of combining a simple script with a powerful library to automate practical tasks.



