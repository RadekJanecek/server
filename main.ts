let start = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    start
    basic.showIcon(IconNames.Yes)
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    console.log(String.fromCharCode(receivedNumber))
})
