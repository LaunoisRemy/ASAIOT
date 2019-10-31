import time
import utils.grovepi

def readValue() :
    # Connect the Grove Rotary Angle Sensor to analog port A1
    # SIG,NC,VCC,GND
    potentiometer = 1

    grovepi.pinMode(potentiometer,"INPUT")
    time.sleep(1)

    # Reference voltage of ADC is 5v
    adc_ref = 5

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)

    # Calculate voltage
    voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

    # Calculate rotation in degrees (0 to 300)
    degrees = round((voltage * full_angle) / grove_vcc, 2)

    val1 = degrees//37.5

    return val1

def readValue() :
    # Connect the Grove Rotary Angle Sensor to analog port A1
    # SIG,NC,VCC,GND
    potentiometer = 1

    grovepi.pinMode(potentiometer,"INPUT")
    time.sleep(1)

    # Reference voltage of ADC is 5v
    adc_ref = 5

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)

    # Calculate voltage
    voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

    # Calculate rotation in degrees (0 to 300)
    degrees = round((voltage * full_angle) / grove_vcc, 2)

    val1 = degrees//150

    return val1
