def wait_line():
    pins.digital_write_pin(DigitalPin.P8, 1)
def green():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
def white():
    pins.digital_write_pin(DigitalPin.P16, 1)

def on_button_pressed_a():
    global passage
    passage = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def yello():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
def red():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
passage = 0
passage = 0
wait_light = 1

def on_forever():
    global wait_light, passage
    if passage == 1:
        wait_light = 0
        if pins.analog_read_pin(AnalogPin.P0) == 1:
            yello()
            basic.pause(100)
            red()
        else:
            red()
        white()
        basic.show_number(5)
        basic.pause(1000)
        basic.show_number(4)
        basic.pause(1000)
        basic.show_number(3)
        basic.pause(1000)
        basic.show_number(2)
        basic.pause(1000)
        basic.show_number(1)
        basic.pause(1000)
        basic.show_number(0)
        basic.clear_screen()
        passage = 0
        wait_light = 1
    else:
        basic.pause(2000)
        green()
        basic.pause(2000)
        yello()
        basic.pause(1000)
        red()
basic.forever(on_forever)

def on_forever2():
    if wait_light == 1:
        pins.digital_write_pin(DigitalPin.P8, 1)
    else:
        pins.digital_write_pin(DigitalPin.P8, 0)
basic.forever(on_forever2)

def on_forever3():
    if passage == 0:
        pins.digital_write_pin(DigitalPin.P16, 0)
basic.forever(on_forever3)
