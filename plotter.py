import matplotlib.pyplot as plt
import math

cwnd_values = []
ssthresh = []
start_ssthresh = -1
seconds = []
with open('cwnd_log.txt') as cwnd_log:
    for log in cwnd_log:
        if 'time:' not in log:
            continue

        seconds.append(int(log[5:log.index(" ")]))
        
        if " " in log:
            cwnd_values.append((int(log[log.index("cwnd:") + 5: log[log.index("cwnd:"):].index(" ") + log.index("cwnd:")])))
        else:
            cwnd_values.append((int(log[log.index("cwnd:") + 5:])))

        if ' ssthresh:' not in log:
            start_ssthresh = len(cwnd_values)
            continue

        ssthresh_index = log.index("ssthresh")
        if " " in log[ssthresh_index:]:
            ssthresh.append((int(log[ssthresh_index + 9: log[ssthresh_index:].index(" ") + ssthresh_index])))
        else:
            ssthresh.append((int(log[ssthresh_index + 9:])))

seconds = [x - seconds[0] for x in seconds]

# time_intervals = range(len(cwnd_values))
# ss_intervals = range(start_ssthresh, len(cwnd_values))

time_intervals = seconds
ss_intervals = seconds[start_ssthresh:]

#Plot
plt.figure(figsize=(20, 6))
plt.plot(time_intervals, cwnd_values, linestyle="-", linewidth=1, label="cwnd")
plt.plot(ss_intervals, ssthresh, linestyle="-", linewidth=1, label="ssthresh")
plt.title("Congestion Window Over Time")
plt.xlabel("Time (ms)")
plt.ylabel("Congestion Window Size")
plt.grid(True)
plt.legend()
plt.savefig("cwnd_plot.png", format='png', dpi=300)