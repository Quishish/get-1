import r2r_adc as r2r
import adc_plot as plt
import mcp3921_driver as i2c
from time import time

if __name__ == "__main__":
    dynamic_range = 3.117
    bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
    comp_gpio = 21

    adc = r2r.R2R_ADC(dynamic_range)
    adc2 = i2c.MCP3021(5.1)

    voltages = []
    times = []
    durations = 5.0

    try:
        time0 = time()
        current_time = time()
        while(time0 < current_time < time0 + durations):
            #value = adc.get_sc_voltage()
            #value = adc.get_sar_voltage()
            value = adc2.get_voltage()
            time1 = time()
            times.append(time1-time0)
            voltages.append(value)
            current_time = time()
        if len(times) == 0:
            times = [0]
            voltages = [0]
        plt.plot_voltage_vs_time(times, voltages, dynamic_range)
        #plt.plot_sampling_period_hist(times)
    finally:
        adc.deinit()

