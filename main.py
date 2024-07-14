import numpy as np
import matplotlib.pyplot as plt

def read_signal_data(file_path):
    data = np.loadtxt(file_path)
    frequencies = data[:, 0]
    amplitudes = data[:, 1]
    return frequencies, amplitudes

def find_extreme_sections(frequencies, amplitudes, section_length):
    num_points = len(frequencies)
    max_sum = -np.inf
    min_sum = np.inf
    max_section = (0, section_length)
    min_section = (0, section_length)

    for i in range(num_points - section_length + 1):
        current_section_sum = np.sum(amplitudes[i:i + section_length])

        if current_section_sum > max_sum:
            max_sum = current_section_sum
            max_section = (i, i + section_length)

        if current_section_sum < min_sum:
            min_sum = current_section_sum
            min_section = (i, i + section_length)

    return max_section, min_section

def plot_signal(frequencies, amplitudes, max_section=None, min_section=None):
    plt.figure(figsize=(10, 6))
    plt.plot(frequencies, amplitudes, label='Амплитудная панорама сигнала')

    if max_section and min_section:
        max_freqs = frequencies[max_section[0]:max_section[1]]
        max_amps = amplitudes[max_section[0]:max_section[1]]
        plt.plot(max_freqs, max_amps, color='red', label='Участок с максимумами')

        min_freqs = frequencies[min_section[0]:min_section[1]]
        min_amps = amplitudes[min_section[0]:min_section[1]]
        plt.plot(min_freqs, min_amps, color='green', label='Участок с минимумами')

    plt.xlabel('Частота')
    plt.ylabel('Амплитуда')
    plt.title('Амплитудная панорама сигнала')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    file_path = 'signal2.txt'
    frequencies, amplitudes = read_signal_data(file_path)

    section_length = 3
    max_section, min_section = find_extreme_sections(frequencies, amplitudes, section_length)

    plot_signal(frequencies, amplitudes)
    plot_signal(frequencies, amplitudes, max_section, min_section)

    print("Участок с максимальными значениями:")
    print(f"Частоты: {frequencies[max_section[0]]} - {frequencies[max_section[1] - 1]}")
    print(f"Амплитуды: {amplitudes[max_section[0]:max_section[1]]}")

    print("Участок с минимальными значениями:")
    print(f"Частоты: {frequencies[min_section[0]]} - {frequencies[min_section[1] - 1]}")
    print(f"Амплитуды: {amplitudes[min_section[0]:min_section[1]]}")

if __name__ == '__main__':
    main()

