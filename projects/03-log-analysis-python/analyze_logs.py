"""Count failed SSH logins per IP address in an auth log."""
import re
import sys
from collections import Counter

PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
)


def analyze(path, threshold=3):
    ips = Counter()
    users = Counter()
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = PATTERN.search(line)
            if match:
                users[match.group(1)] += 1
                ips[match.group(2)] += 1

    print(f"Total failed logins: {sum(ips.values())}")
    print(f"\nIPs with {threshold}+ failures:")
    for ip, count in ips.most_common():
        if count >= threshold:
            print(f"  {ip}: {count}")
    print("\nMost targeted usernames:")
    for user, count in users.most_common(5):
        print(f"  {user}: {count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_logs.py <logfile> [threshold]")
        sys.exit(1)
    analyze(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3)
