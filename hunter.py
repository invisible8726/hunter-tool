import socket
import requests
import hashlib
import os
import pyfiglet

# ---------------------- Banner ----------------------
def show_banner():
    banner = pyfiglet.figlet_format("HUNTER")
    developer = "Developed by INVISIBLE"
    print(banner)
    print(developer)
    print("=" * 50)  # Line separator

# ---------------------- Port Scanner ----------------------
def port_scanner(target, ports=[21, 22, 80, 443, 8080]):
    print(f"\n[+] Scanning {target} for open ports...")
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"  Port {port}: OPEN 🟢")
            else:
                print(f"  Port {port}: CLOSED 🔴")
            sock.close()
    except Exception as e:
        print(f"Error: {e}")

# ---------------------- Password Checker ----------------------
def password_strength(password):
    strength = 0
    if len(password) >= 8: strength +=1
    if any(c.isupper() for c in password): strength +=1
    if any(c.isdigit() for c in password): strength +=1
    if not password.isalnum(): strength +=1
    
    feedback = {
        0: "Very Weak (Chotu, aur complex banao!) 😭",
        1: "Weak (Thoda aur try karo) 🥺",
        2: "Medium (Aur characters add karo) 😐",
        3: "Strong (Chalega!) 👍",
        4: "Very Strong (Waah, hacker banega tu!) 🔥"
    }
    return feedback.get(strength, "Invalid")

# ---------------------- Website Security Checker ----------------------
def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        missing = []
        
        security_headers = [
            'Content-Security-Policy',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'Strict-Transport-Security'
        ]
        
        print(f"\n[+] Checking security headers for {url}:")
        for header in security_headers:
            if header in headers:
                print(f"  ✅ {header}: Present")
            else:
                print(f"  ❌ {header}: Missing")
                missing.append(header)
        
        if missing:
            print("\nWarning: Website is missing critical security headers! 🚨")
        
    except Exception as e:
        print(f"Error: {e}")

# ---------------------- File Hasher ----------------------
def file_hasher(file_path, algorithm='md5'):
    try:
        hasher = hashlib.md5() if algorithm == 'md5' else hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        print(f"\n[{algorithm.upper()}] Hash for {os.path.basename(file_path)}:")
        print(hasher.hexdigest())
    except Exception as e:
        print(f"Error: {e}")

# ---------------------- Main Menu ----------------------
def main_menu():
    print("\n🔒 CYBER SECURITY TOOLKIT 🔒")
    print("1. Port Scanner")
    print("2. Password Strength Checker")
    print("3. Website Security Checker")
    print("4. File Hasher")
    print("5. Exit")
    
    choice = input("\nChoose option (1-5): ")
    return choice

# ---------------------- Run Program ----------------------
if __name__ == "__main__":
    show_banner()  # Banner Show Karega

    while True:
        choice = main_menu()
        
        if choice == '1':
            target = input("Enter target IP/domain: ")
            port_scanner(target)
            
        elif choice == '2':
            password = input("Enter password to check: ")
            print(password_strength(password))
            
        elif choice == '3':
            url = input("Enter website URL (e.g., https://example.com): ")
            check_security_headers(url)
            
        elif choice == '4':
            file_path = input("Enter file path: ")
            algo = input("Hash type (md5/sha256): ").lower()
            file_hasher(file_path, algo)
            
        elif choice == '5':
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice! Try again.")

