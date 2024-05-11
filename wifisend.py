import socket
ESP32_IP = "192.168.236.69"
ESP32_PORT = 80

def send_command(command):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ESP32_IP, ESP32_PORT))
        s.sendall(command.encode())
        s.close()
    except Exception as e:
        print("Error:", e)
send_command("abc")
