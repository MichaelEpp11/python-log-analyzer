failed_attempts = {}

with open("log.txt", "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from ")[1].split()[0]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("\nSuspicious Login Attempts:\n")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempts")

print("\nPotential Attackers (3+ attempts):\n")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"ALERT: {ip} may be brute-forcing ({count} attempts)")
