# K.E.N.D.R.A-RA1018 – Version 1.0.0
# Main interface for Kendrah Assistant AI

# from kendrah_backend_run import KendrahBackend
# from AppData.core.mode.host.offline_mode import OfflineMode
# from AppData.core.mode.host.online_mode import OnlineMode

class KendrahAssistant:
    def __init__(self):
        self.offline_mode = OfflineMode()
        self.online_mode = OnlineMode()
        self.current_mode = None
        
    def check_internet(self):
        try:
            import socket
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False

    def initialize_mode(self):
        if self.check_internet():
            self.current_mode = "online"
            return self.online_mode.initialize_service("deepseek")
        else:
            self.current_mode = "offline"
            return self.offline_mode.check_local_llm_status()

def main():
    # Clean interface without backend noise
    print("\n╔════════════════════════════════════╗")
    print("║      K.E.N.D.R.A-RA1018 v1.0.0    ║")
    print("╚════════════════════════════════════╝\n")
    
    # Initialize assistant and check mode
    assistant = KendrahAssistant()
    mode_status = assistant.initialize_mode()
    
    # Initialize backend silently
    backend = KendrahBackend(show_startup_messages=False)
    
    print(f"[System] Ready in {assistant.current_mode} mode")
    print("[System] How can I help you today?\n")
    
    # Main interaction loop
    while True:
        try:
            should_exit = backend.listen_and_process()
            if should_exit:
                print("\n[System] Goodbye! Have a great day! 👋\n")
                break
        except KeyboardInterrupt:
            print("\n\n[System] Interrupted by user. Shutting down...")
            break
        except Exception as e:
            print(f"\n[System] Encountered an error but I'm still here! Let's continue...")
            continue

if __name__ == "__main__":
    main()