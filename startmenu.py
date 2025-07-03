import pygame
import sys
import constants
import subprocess
import threading
import re
from client import client
from server import server

class GameMenu:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Multiplayer Game Menu")
        self.clock = pygame.time.Clock()
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (150, 150, 150)
        self.BLACK = (0, 0, 0)
        self.ACTIVE_COLOR = (0, 100, 255)
        self.INACTIVE_COLOR = (100, 100, 100)
        self.PLACEHOLDER_COLOR = (120, 120, 120)
        # Additional colors for better UI
        self.LIGHT_GRAY = (200, 200, 200)
        self.GREEN = (0, 150, 0)
        self.RED = (200, 100, 100)
        
        # Font
        self.font = pygame.font.SysFont(None, 50)
        
        # Button dimensions
        self.button_width, self.button_height = 200, 80
        
        # Initialize UI elements
        self._setup_input_boxes()
        self._setup_buttons()
    
    def _setup_input_boxes(self):
        """Initialize input boxes for settings menu."""
        center_x = constants.SCREEN_WIDTH // 2
        
        # IP Address input with 4 separate boxes
        self.ip_boxes = []
        for i in range(4):
            self.ip_boxes.append({
                "rect": pygame.Rect(center_x - 200 + i * 90, 150, 80, 50),
                "color": self.INACTIVE_COLOR,
                "text": "",
                "active": False,
                "placeholder": "000"
            })
        
        # Name input box
        self.name_box = {
            "rect": pygame.Rect(center_x - 200, 250, 300, 50),
            "color": self.INACTIVE_COLOR,
            "text": "",
            "active": False,
            "placeholder": "Enter Your Name"
        }

        # Port input box
        self.port_box = {
            "rect": pygame.Rect(center_x - 200, 350, 300, 50),
            "color": self.INACTIVE_COLOR,
            "text": "",
            "active": False,
            "placeholder": "Enter Port"
        }

        # Connect button
        self.connect_button = pygame.Rect(center_x - 100, 450, 200, 60)
        
        # Back button
        self.back_button = pygame.Rect(50, 50, 100, 50)
    
    def _setup_buttons(self):
        """Initialize button rectangles."""
        center_x = constants.SCREEN_WIDTH // 2
        center_y = constants.SCREEN_HEIGHT // 2
        
        # Main menu buttons
        self.button_rect_start = pygame.Rect(
            center_x - self.button_width // 2,
            center_y - 140,
            self.button_width,
            self.button_height
        )
        self.button_rect_exit = pygame.Rect(
            center_x - self.button_width // 2,
            center_y - 40,
            self.button_width,
            self.button_height
        )
        self.button_rect_setting = pygame.Rect(
            center_x - self.button_width // 2,
            center_y + 60,
            self.button_width,
            self.button_height
        )
        
        # Difficulty buttons (same positions as main menu)
        self.button_rect_easy = pygame.Rect(
            center_x - self.button_width // 2,
            center_y - 140,
            self.button_width,
            self.button_height
        )
        self.button_rect_normal = pygame.Rect(
            center_x - self.button_width // 2,
            center_y - 40,
            self.button_width,
            self.button_height
        )
        self.button_rect_hard = pygame.Rect(
            center_x - self.button_width // 2,
            center_y + 60,
            self.button_width,
            self.button_height
        )
    
    def is_port_listening(self, port):
        """Check if a port is currently listening."""
        try:
            result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
            pattern = f':{port}.*LISTEN'
            return bool(re.search(pattern, result.stdout))
        except Exception:
            return False
    
    def draw_button(self, rect, text_str):
        """Draw a button with text."""
        pygame.draw.rect(self.screen, self.BLACK, rect)
        text = self.font.render(text_str, True, self.WHITE)
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)
    
    def draw_menu(self):
        """Draw the main menu."""
        self.screen.fill(self.GRAY)
        self.draw_button(self.button_rect_start, "Start Game")
        self.draw_button(self.button_rect_exit, "Exit Game")
        self.draw_button(self.button_rect_setting, "Settings")
        pygame.display.flip()
    
    def draw_difficulty_menu(self):
        """Draw the difficulty selection menu."""
        self.screen.fill(self.GRAY)
        self.draw_button(self.button_rect_easy, "Easy")
        self.draw_button(self.button_rect_normal, "Normal")
        self.draw_button(self.button_rect_hard, "Hard")
        pygame.display.flip()
    
    def draw_input_box(self, box, is_ip=False):
        """Draw a single input box."""
        # Draw background
        pygame.draw.rect(self.screen, self.WHITE, box["rect"])
        # Draw border
        pygame.draw.rect(self.screen, box["color"], box["rect"], 3)
        
        text_to_show = box["text"] if box["text"] else box["placeholder"]
        color = self.BLACK if box["text"] else self.PLACEHOLDER_COLOR
        
        # Center text in IP boxes, left-align in other boxes
        if is_ip:
            text_surface = self.font.render(text_to_show, True, color)
            text_rect = text_surface.get_rect(center=box["rect"].center)
            self.screen.blit(text_surface, text_rect)
        else:
            text_surface = self.font.render(text_to_show, True, color)
            self.screen.blit(text_surface, (box["rect"].x + 10, box["rect"].y + 10))
    
    def draw_settings_labels(self):
        """Draw labels for settings inputs."""
        # Title
        title_font = pygame.font.SysFont(None, 70)
        title_text = title_font.render("Settings", True, self.BLACK)
        title_rect = title_text.get_rect(center=(constants.SCREEN_WIDTH // 2, 80))
        self.screen.blit(title_text, title_rect)
        
        # IP Address label
        ip_label = self.font.render("IP Address:", True, self.BLACK)
        self.screen.blit(ip_label, (constants.SCREEN_WIDTH // 2 - 200, 110))
        
        # Draw dots between IP boxes
        for i in range(3):
            dot_x = constants.SCREEN_WIDTH // 2 - 200 + (i + 1) * 90 - 5
            dot_y = 175
            pygame.draw.circle(self.screen, self.BLACK, (dot_x, dot_y), 5)
        
        # Name label
        name_label = self.font.render("Player Name:", True, self.BLACK)
        self.screen.blit(name_label, (constants.SCREEN_WIDTH // 2 - 200, 210))

        # Port label
        port_label = self.font.render("Port Number:", True, self.BLACK)
        self.screen.blit(port_label, (constants.SCREEN_WIDTH // 2 - 200, 310))
    
    def handle_ip_input(self, event, box_index):
        """Handle input for IP address boxes."""
        box = self.ip_boxes[box_index]
        
        if event.key == pygame.K_BACKSPACE:
            if box["text"]:
                box["text"] = box["text"][:-1]
            elif box_index > 0:
                # Move to previous box if current is empty
                self.ip_boxes[box_index]["active"] = False
                self.ip_boxes[box_index]["color"] = self.INACTIVE_COLOR
                self.ip_boxes[box_index - 1]["active"] = True
                self.ip_boxes[box_index - 1]["color"] = self.ACTIVE_COLOR
        elif event.unicode.isdigit():
            # Only allow digits and max 3 characters
            if len(box["text"]) < 3:
                new_text = box["text"] + event.unicode
                # Check if valid IP octet (0-255)
                if int(new_text) <= 255:
                    box["text"] = new_text
                    # Auto-move to next box if 3 digits entered
                    if len(box["text"]) == 3 and box_index < 3:
                        box["active"] = False
                        box["color"] = self.INACTIVE_COLOR
                        self.ip_boxes[box_index + 1]["active"] = True
                        self.ip_boxes[box_index + 1]["color"] = self.ACTIVE_COLOR
        elif event.key == pygame.K_PERIOD or event.key == pygame.K_RIGHT:
            # Move to next box
            if box_index < 3:
                box["active"] = False
                box["color"] = self.INACTIVE_COLOR
                self.ip_boxes[box_index + 1]["active"] = True
                self.ip_boxes[box_index + 1]["color"] = self.ACTIVE_COLOR
        elif event.key == pygame.K_LEFT:
            # Move to previous box
            if box_index > 0:
                box["active"] = False
                box["color"] = self.INACTIVE_COLOR
                self.ip_boxes[box_index - 1]["active"] = True
                self.ip_boxes[box_index - 1]["color"] = self.ACTIVE_COLOR
    
    def handle_name_input(self, event):
        """Handle input for name box."""
        if event.key == pygame.K_BACKSPACE:
            self.name_box["text"] = self.name_box["text"][:-1]
        elif len(self.name_box["text"]) < 20:  # Max 20 characters
            # Allow letters, numbers, spaces, and common symbols
            if (event.unicode.isalnum() or 
                event.unicode in [" ", "-", "_", "."]):
                self.name_box["text"] += event.unicode

    def handle_port_input(self, event):
        """Handle input for port box."""
        if event.key == pygame.K_BACKSPACE:
            self.port_box["text"] = self.port_box["text"][:-1]
        elif len(self.port_box["text"]) < 5:  # Max 5 characters for port
            # Allow only digits for port
            if event.unicode.isdigit():
                new_text = self.port_box["text"] + event.unicode
                # Check if valid port number (1-65535)
                if int(new_text) <= 65535:
                    self.port_box["text"] = new_text

    def handle_settings_click(self, event_pos):
        """Handle mouse clicks in settings menu."""
        # Deactivate all boxes first
        for ip_box in self.ip_boxes:
            ip_box["active"] = False
            ip_box["color"] = self.INACTIVE_COLOR
        self.name_box["active"] = False
        self.name_box["color"] = self.INACTIVE_COLOR
        self.port_box["active"] = False
        self.port_box["color"] = self.INACTIVE_COLOR
        
        # Check IP boxes
        for i, box in enumerate(self.ip_boxes):
            if box["rect"].collidepoint(event_pos):
                box["active"] = True
                box["color"] = self.ACTIVE_COLOR
                return
        
        # Check name box
        if self.name_box["rect"].collidepoint(event_pos):
            self.name_box["active"] = True
            self.name_box["color"] = self.ACTIVE_COLOR
            return
        
        # Check port box
        if self.port_box["rect"].collidepoint(event_pos):
            self.port_box["active"] = True
            self.port_box["color"] = self.ACTIVE_COLOR
            return
        
        # Check connect button
        if self.connect_button.collidepoint(event_pos):
            ip_address = ".".join([box["text"] for box in self.ip_boxes if box["text"]])
            name = self.name_box["text"]
            port = self.port_box["text"]
            
            if ip_address and name and port:
                print(f"Connecting to {ip_address}:{port} as {name}")
                # Save connection settings to file
                try:
                    with open("connection.txt", "w") as f:
                        f.write(f"IP:{ip_address}\n")
                        f.write(f"player_name:{name}\n")
                        f.write(f"port:{port}")
                    print("Connection settings saved!")
                except Exception as e:
                    print(f"Error saving settings: {e}")
            else:
                print("Please fill all fields before connecting!")
            return "back"
        
        # Check back button
        if self.back_button.collidepoint(event_pos):
            return "back"
    
    def handle_settings_keydown(self, event):
        """Handle keyboard input in settings menu."""
        # Handle IP input
        for i, box in enumerate(self.ip_boxes):
            if box["active"]:
                self.handle_ip_input(event, i)
                return
        
        # Handle name input
        if self.name_box["active"]:
            self.handle_name_input(event)
            return
        
        # Handle port input
        if self.port_box["active"]:
            self.handle_port_input(event)
            return
    
    def get_ip_address(self):
        """Get the complete IP address from all boxes."""
        ip_parts = [box["text"] for box in self.ip_boxes if box["text"]]
        return ".".join(ip_parts) if len(ip_parts) == 4 else ""
    
    def is_valid_input_character(self, char):
        """Check if character is valid for input."""
        return (char.isdigit() or 
                char.isalpha() or 
                char in [".", "-", "_", " "])
    
    def settings_menu_loop(self):
        """Handle the settings menu loop."""
        while True:
            # Background
            self.screen.fill(self.GRAY)
            
            # Draw labels and UI elements
            self.draw_settings_labels()
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.handle_settings_click(event.pos)
                    if result == "back":
                        return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    self.handle_settings_keydown(event)
            
            # Draw IP address input boxes
            for box in self.ip_boxes:
                self.draw_input_box(box, is_ip=True)
            
            # Draw name input box
            self.draw_input_box(self.name_box, is_ip=False)
            
            # Draw port input box
            self.draw_input_box(self.port_box, is_ip=False)
            
            # Draw connect button
            all_filled = (self.get_ip_address() and 
                         self.name_box["text"] and 
                         self.port_box["text"])
            connect_color = self.GREEN if all_filled else (100, 100, 100)
            pygame.draw.rect(self.screen, connect_color, self.connect_button)
            pygame.draw.rect(self.screen, self.BLACK, self.connect_button, 3)
            connect_text = self.font.render("Connect", True, self.WHITE)
            connect_rect = connect_text.get_rect(center=self.connect_button.center)
            self.screen.blit(connect_text, connect_rect)
            
            # Draw back button
            pygame.draw.rect(self.screen, self.RED, self.back_button)
            pygame.draw.rect(self.screen, self.BLACK, self.back_button, 3)
            back_text = pygame.font.SysFont(None, 40).render("Back", True, self.WHITE)
            back_rect = back_text.get_rect(center=self.back_button.center)
            self.screen.blit(back_text, back_rect)
            
            # Draw current connection info preview
            current_ip = self.get_ip_address()
            if current_ip:
                preview_font = pygame.font.SysFont(None, 35)
                ip_preview = preview_font.render(f"IP: {current_ip}", True, self.BLACK)
                self.screen.blit(ip_preview, (constants.SCREEN_WIDTH // 2 - 200, 560))
            
            if self.port_box["text"]:
                preview_font = pygame.font.SysFont(None, 35)
                port_preview = preview_font.render(f"Port: {self.port_box['text']}", True, self.BLACK)
                self.screen.blit(port_preview, (constants.SCREEN_WIDTH // 2 - 200, 530))
            
            pygame.display.flip()
            self.clock.tick(60)
    
    def set_difficulty(self, difficulty):
        """Set game difficulty by modifying ball speed."""
        if difficulty == "Easy":
            constants.BALL_SPEED = [1, 1]
        elif difficulty == "Normal":
            constants.BALL_SPEED = [6, 6]
        elif difficulty == "Hard":
            constants.BALL_SPEED = [10, 10]
    
    def run_game(self, difficulty):
        """Start the game with specified difficulty."""
        if not self.is_port_listening(5557):
            print(f"Starting game with difficulty: {difficulty}")
            if difficulty:  # Only set difficulty if it's not empty
                self.set_difficulty(difficulty)
            threading.Thread(target=server, daemon=True).start()
        client()
    
    def difficulty_menu_loop(self):
        """Handle the difficulty selection menu loop."""
        while True:
            self.draw_difficulty_menu()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect_easy.collidepoint(event.pos):
                        self.run_game("Easy")
                        return
                    elif self.button_rect_normal.collidepoint(event.pos):
                        self.run_game("Normal")
                        return
                    elif self.button_rect_hard.collidepoint(event.pos):
                        self.run_game("Hard")
                        return
    
    def quit_game(self):
        """Quit the game properly."""
        pygame.quit()
        sys.exit()
    
    def main(self):
        """Main game loop."""
        while True:
            self.draw_menu()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect_start.collidepoint(event.pos):
                        if not self.is_port_listening(5557):
                            self.difficulty_menu_loop()
                        else:
                            self.run_game("")
                    elif self.button_rect_setting.collidepoint(event.pos):
                        self.settings_menu_loop()
                    elif self.button_rect_exit.collidepoint(event.pos):
                        self.quit_game()


def main():
    """Entry point for the game."""
    game_menu = GameMenu()
    game_menu.main()


if __name__ == "__main__":
    main()