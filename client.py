from keyboard._keyboard_event import KEY_DOWN, KEY_UP
import keyboard
import websocket
from keyRecConf import HOST, PORT

# -- Keyboard Listener -- #
def on_action(event, webSocket):
   
    if event.event_type == KEY_DOWN:
        on_press(event.name, webSocket)

    # elif event.event_type == KEY_UP:
    #     on_release(event.name, webSocket)

def on_press(key, webSocket):
    print(f"Pressed:  {key}")
    webSocket.send(key)

def on_release(key, webSocket):
    print(f"Released: {key}")
    webSocket.send(key)

# -- WebSocket Client -- #
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    keyboard.hook(lambda e: on_action(e, ws))


if __name__ == "__main__":
    ws = websocket.WebSocketApp(f"ws://{HOST}:{PORT}/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    
    

    ws.run_forever()
