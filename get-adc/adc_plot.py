from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("voltage vs time")
    plt.xlabel("Time, sec")
    plt.ylabel("Voltage, V")
    plt.xlim(min(time), max(time))
    plt.ylim(0, max(voltage)*1,2)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):

    sampling_periods = []

    for i in range(1, len(time)):
        sampling_periods.append(time[i]-time[i-1])

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title("Sampling period histogram")
    plt.xlabel("Period")
    plt.ylabel("Number of measurements")
    #plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()

    