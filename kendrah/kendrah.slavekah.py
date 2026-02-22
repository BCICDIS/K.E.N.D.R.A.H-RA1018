import os
# from requests import Client as requestsClient
import time
from typing import Optional
from datetime import datetime

class ChatInterface:
    def __init__(self):
        self.messages: dict[str, list] = {}
        self.control_windows: dict[str, list[int]] = {}
        self.current_sender: Optional[str] = None
        self.error_handler: None = None

    def add_user(self, sender_name: str) -> None:
        """Add a new user to the chat interface."""
        current_sender = self.current_sender
        if current_sender is not None and current_sender.name != sender_name:
            raise ValueError("Cannot have multiple users with the same name.")

        self.messages[sender_name] = []
        self.control_windows[sender_name] = 0

    def send_message_to_user(self, user_name: str, message: str) -> None:
        """Send new text to a specific user."""
        self.messages[user_name].append({"message": message, "sender": user_name})

        # Update UI display for the current sender
        if self.current_sender is not None and self.current_sender.name != user_name:
            self.display_message(user_name)

        # Show the messages in their respective windows
        for name, cont in self.control_windows.items():
            cont.append({"message": message, "sender": name})

    def display_message(self, message: str) -> None:
        """Display a message to the user in the appropriate control window."""
        sender_name = [cont["sender"] for cont in self.control_windows.values() if cont["sender"] ==
        message.name][0]
        print(f"{sender_name}: {message['message']}")

    def wait_for_answer(self) -> None:
        """Wait for AI response to be received from the user and display it."""
        while True:
            try:
                response = self._get_ai_response()
                if response is not None:
                    self.display_message(response)
                    return
                else:
                    print("AI response was invalid or could not be retrieved.")
            except requests.exceptions.RequestException as e:
                # Catch any request errors and handle accordingly
                print(f"Request failed: {str(e)}")
            except Exception as e:
                # Catch other unexpected exceptions
                print(f"Unexpected error occurred: {str(e)}")

    def _get_ai_response(self) -> Optional[str]:
        """Retrieve AI response from the Ollama server."""
        if self.error_handler is None:
            raise ValueError("Error handling. Need to configure error handler first.")

        ollama_url = "http://127.0.0.1:11434"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.error_handler, self.error_token}'
        }

        try:
            with open(os.path.join(os.getcwd(), "routes.go"), "r") as f:
                import json
                response = requestsClient(
                    headers=headers,
                    data=f.read().decode()
                )
                result = response.json()

                if isinstance(result, dict) and 'response' in result:
                    return result['response']
                else:
                    raise Exception(f"JSON parsing failed: {result}")
        except (requests.exceptions.RequestException, Exception) as e:
            print(f"Request failed: {str(e)}")
            raise

    def add_user(self, sender_name: str):
        """Add a user to the chat interface."""
        self.add_user(sender_name)

    def _handle_additional_features(self, message: dict) -> None:
        """Handle additional features like keyboard shortcuts or background processing."""
        pass  # Placeholder for actual feature handling

# Initialize the AI assistant
ai = ChatInterface()
ai.error_handler = "Ollama Error Handler"
ai.current_sender = "AI Assistant"
ai.control_windows = {}
ai.messages = {}

try:
    ai.add_user("User 1")
    ai.add_user("User 2")

    while True:
        user_input = input("\n\nEnter your message (e.g., 'help' to see commands'):").strip()
        if not user_input:
            print("No valid message entered.")
            continue

        for sender in ["AI Assistant", "System Logs"]:
            try:
                ai.send_message_to_user(sender, user_input)

                if user_input.lower() == "help":
                    print("\nAvailable chat operations:")
                    print("1. Enter a command or message to start a new conversation.")
                    break
            except requests.exceptions.RequestException as e:
                print(f"Invalid input: {user_input}")
        else:
            # Handle other errors in helpful mode
            try:
                ai.display_message(user_input)
                continue
            except Exception as e:
                print(f"Unexpected error occurred: {e}")

except KeyboardInterrupt:
    print("\nOperation interrupted gracefully.")
    pass