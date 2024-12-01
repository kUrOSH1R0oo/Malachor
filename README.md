## Malachor: ForkBomb | Denial of Service Malware

Malachor is a highly destructive Python-based malware designed to cause system instability and unwanted behaviors. It performs various malicious actions such as overloading system resources, spawning unnecessary programs, opening browsers with URLs, and persisting itself in the system registry.

# Disclaimer: 
This malware is for educational purposes only. It is illegal to use this script on systems you do not own or have explicit permission to test. Misuse of this tool can result in legal consequences. Use responsibly and ethically.

# Features:
1. **Fork Bomb**: Overloads the system by continuously creating processes, consuming CPU resources.
2. **Browser Spawning**: Opens specified URLs in available browsers (Chrome, Firefox, Edge, etc.) on the system.
3. **Program Spawning**: Continuously opens unnecessary programs like command prompt, PowerShell, calculator, and Task Manager.
4. **Persistence**: Adds itself to the Windows registry to ensure it runs on startup, even after a reboot.

# Installation and Deployment
1. Clone the repository:
    ```bash
    git clone https://github.com/Kuraiyume/Malachor
    ```
2. Install PyInstaller:
    ```bash
    pip3 install PyInstaller
    ```
3. You can run Malachor in a raw script (.py) or run it as an executable (.exe):
    - Raw
    ```bash
    python3 malachor.py
    ```
    - Executable (For Executable, you need to configure the .spec file based on your preference before you build it into a standalone executable.):
    ```bash
    pyinstaller malachor.spec
    ```

# Caution
Malachor is destructive and can cause the system to become unstable, slow down, or crash due to excessive resource consumption. Do not run this on systems you do not own or have explicit permission to test.

# Legal Warning
Using this script in unauthorized environments is illegal. It is strictly intended for educational purposes, and you should only run it on systems you own or have explicit permission to test.

# License
This project is licensed under the MIT License.

# Author
Kuroshiro (A1SBERG)


