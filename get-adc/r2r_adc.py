import RPi.GPIO as GPIO
import time as time
import r2r_dac as r2r

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        ##print('1')
        out = [int(element) for element in bin(number)[2:].zfill(8)]
        for i in range(len(self.bits_gpio)):
            ##print('4')
            ##print(out)
            GPIO.output(self.bits_gpio[i], out[i])

    def sequentiial_counting_adc(self):
        ##print('2')
        n = -1
        while (GPIO.input(self.comp_gpio) == 0 and n <= 255):
            time.sleep(self.compare_time)
            n+=1
            print(GPIO.input(self.comp_gpio) )
            self.number_to_dac(n)
        return n
    
    def get_sc_voltage(self):
        ##print('3')
        number = self.sequentiial_counting_adc()
        return (number/255 * self.dynamic_range)
    
if __name__ == "__main__":
    dynamic_range = 3.117
    adc = R2R_ADC(3.117, 0.1)
    try:
        while True:
            print(adc.get_sc_voltage())
    finally:
        adc.deinit()