import websocket

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}: {close_msg}")

def on_open(ws):
    print("WebSocket connection opened")
    ws.send("Hello, WebSocket!")

websocket_url = "wss://example.com/socket"

# Create a WebSocket instance and set the event handlers
ws = websocket.WebSocketApp(websocket_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open

# Start the WebSocket connection
ws.run_forever()
