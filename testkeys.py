##Pygame Zero Test Keys

WIDTH = 800
HEIGHT = 600

last_key_type = 0
last_key_press = ""

def draw():
    screen.clear()
    screen.draw.text("Last key press: "+last_key_press+" key: "+str(last_key_type), (20, 100))

def on_key_down(key, mod, unicode):
    global last_key_press, last_key_type
    # Double press q to quit
    if (last_key_type == keys.Q and key == keys.Q):
        quit()
    last_key_type = key
    last_key_press = unicode# Write your code here :-)
