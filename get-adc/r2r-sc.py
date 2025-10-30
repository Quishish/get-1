import r2r_adc as r2r
import adc_plot as plt
from time import time

if __name__ == "__main__":
    dynamic_range = 3.117
    bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
    comp_gpio = 21

    adc = r2r.R2R_ADC(dynamic_range)

    voltages = []
    times = []
    durations = 3.0

    try:
        time0 = time()

        while(time0 < time() < time0 + durations):
            value = adc.get_sc_voltage()
            time1 = time()
            times.append(time1-time0)
            voltages.append(value)
        if len(times) == 0:
            times = [0]
            voltages = [0]
        plt.plot_voltage_vs_time(times, voltages, dynamic_range)
        plt.plot_sampling_period_hist(times)
    finally:
        adc.deinit()

