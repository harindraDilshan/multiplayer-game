# Constants
SPEED = 5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BALL_SPEED = [3, 3]
PLAYER_ONE_MARKS = 0
PLAYER_TWO_MARKS = 0

def load_settings():
    ip = "" # Server IP  # default fallback
    port = 5557       # default fallback
    player_name = "Jhone"
    try:
        with open("connection.txt", "r") as f:
            for line in f:
                if line.startswith("IP:"):
                    ip = line.strip().split(":")[1]
                if line.startswith("player_name:"):
                    player_name = line.strip().split(":")
                elif line.startswith("PORT:"):
                    port = int(line.strip().split(":")[1])
    except FileNotFoundError:
        print("settings.txt not found. Using default IP and PORT.")
    return ip, port, player_name
