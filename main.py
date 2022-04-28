start = False
def on_button_pressed_a():
    start
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

