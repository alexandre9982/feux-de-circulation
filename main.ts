function wait_line () {
    pins.digitalWritePin(DigitalPin.P8, 1)
}
function green () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
function white () {
    pins.digitalWritePin(DigitalPin.P16, 1)
}
input.onButtonPressed(Button.A, function () {
    passage = 1
})
function yello () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
function red () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
}
let passage = 0
passage = 0
let wait_light = 1
basic.forever(function () {
    if (passage == 1) {
        wait_light = 0
        if (pins.analogReadPin(AnalogPin.P0) == 1) {
            yello()
            basic.pause(100)
            red()
        } else {
            red()
        }
        white()
        basic.showNumber(5)
        basic.pause(1000)
        basic.showNumber(4)
        basic.pause(1000)
        basic.showNumber(3)
        basic.pause(1000)
        basic.showNumber(2)
        basic.pause(1000)
        basic.showNumber(1)
        basic.pause(1000)
        basic.showNumber(0)
        basic.clearScreen()
        passage = 0
        wait_light = 1
    } else {
        basic.pause(2000)
        green()
        basic.pause(2000)
        yello()
        basic.pause(1000)
        red()
    }
})
basic.forever(function () {
    if (wait_light == 1) {
        pins.digitalWritePin(DigitalPin.P8, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
})
basic.forever(function () {
    if (passage == 0) {
        pins.digitalWritePin(DigitalPin.P16, 0)
    }
})
