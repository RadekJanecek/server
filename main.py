start = False
def on_button_pressed_a():
    start
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_number(receivedNumber):
    print(String.from_char_code(receivedNumber))
radio.on_received_number(on_received_number)