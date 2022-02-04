##First you need to install either Qjoypad for linux - see game design document or install Antimicro for pc
##Then you need to run either Qjoypad or Antimicro and configure your controller scheme for the controller you are using
##Then you can run this script to check that each of the controller bindings are working with this script before moving on to
##testing with a simple PygameZero Project


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
