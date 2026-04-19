import time
import subprocess

def run_agent():
    # Silent, low-impact beaconing
    # This keeps the node under your control without triggering concurrency alerts
    while True:
        # Subtle heartbeat for C2 maintenance
        subprocess.run(["curl", "-s", "https://1.1.1.1"], capture_output=True)
        time.sleep(300) # Reduced footprint

if __name__ == "__main__":
    run_agent()
