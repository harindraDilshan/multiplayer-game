import subprocess
import threading
import time
import re

def is_port_listening(port):
    try:
        result = subprocess.run(['netstat', '-an'], 
                              capture_output=True, text=True)
        pattern = f':{port}.*LISTEN'
        return bool(re.search(pattern, result.stdout))
    except:
        return False

def run_server():
    print("Starting server...")
    subprocess.run(["uv", "run", "server.py"])

def run_client():
    print("Starting client...")
    time.sleep(2)
    subprocess.run(["uv", "run", "client.py"])

if __name__ == "__main__":
    if not is_port_listening(5557):
        threading.Thread(target=run_server).start()
    run_client()