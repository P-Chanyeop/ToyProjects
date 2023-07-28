import librosa
import librosa.display
import scipy as sp
import IPython.display as ipd

import numpy as np
import matplotlib.pyplot as plt

# librosa 라이브러리 사용 예제
# audio_path = './A_dim_1-0.wav'
# y, sr = librosa.load(audio_path, sr=16000)
# librosa.display.waveshow(y, sr=sr)
# plt.show()

# scipy 라이브러리 사용 예제
import scipy.io.wavfile
from IPython.display import Audio, display

t = np.linspace(0, 1, 100)

# 위상 : 반복되는 파형의 한 주기에서 첫 시작점의 각도 혹은 어느 한 순간의 위치를 말한다.
# 진폭 : 주기적으로 진동하는 파의 진동 폭을 의미한다.
# 주파수 : 진동하는 물체가 단위 시간 동안 진동하는 횟수를 의미한다. 단위로는 Hz(헤르츠)를 사용한다. 1Hz는 1초 동안 물체가 1회 진동할 때를 의미한다.

# 진폭(amplitude) 𝐴
# 위 아래로 움직이는 폭. 소리의 크기로 인식된다.

# 주파수(frequency) 𝜔 또는 𝑓
# 진동 속도. 주파수가 높으면 빠르게 진동한다. 소리의 높낮이로 인식된다.

# 위상(phase) 𝜙
# 사인 함수의 시작 시점. 위상 만큼 출발이 늦어진다. 위상의 차이는 소리의 시간차로 인식된다.

plt.plot(t, 1 * np.sin(2 * np.pi * t + 0), ls="-", label=r"$\sin\left(2\pi{t}\right)$ frequency 1Hz. Amplitude 1, Phase 0")
plt.plot(t, 2 * np.sin(2 * np.pi * t + 0), ls="--", label=r"$2\sin\left(2\pi{t}\right)$ when Amplitude increase at 2 ")  # 진폭이 2로 증가할 경우
plt.plot(t, 1 * np.sin(3 * np.pi * t + 0), ls=":", label=r"$\sin\left(3\pi{t}\right)$ when frequency increase at 1.5Hz")    # 주파수가 1.5Hz로 커질경우
plt.plot(t, 1 * np.sin(2 * np.pi * t - 0.3), ls="-.", label=r"$\sin\left(2\pi{t} - 0.3\right)$ when Phase is lower")   # 위상이 늦춰질 경우
plt.ylim(-2.2, 3)
plt.xticks(np.linspace(0, 1, 5))
plt.xlabel('0 ~ 1 linspace values')
plt.ylabel('Amplitude')
plt.legend()
plt.title(r"$A\sin\left(\omega{t}+\phi\right)$")
plt.show()

# 싱글톤 멜로디
def single_tone(frequecy, sampling_rate=44100, duration=1):
    # frequency: 주파수
    # sampling_rate: 초당 샘플링 데이터 수. 디폴트 44100
    # duration: 지속 시간. 단위 초. 디폴트 1초
    t = np.linspace(0, duration, int(sampling_rate))
    y = np.sin(2 * np.pi * frequecy * t)
    return y

y = single_tone(400)

plt.plot(y[:400])
plt.show()

# 멜로디 배열
notes = 'C,C#,D,D#,E,F,F#,G,G#,A,A#,B,C'.split(',')
freqs = 261.62 * 2**(np.arange(0, len(notes)) / 12.)
notes = list(zip(notes, freqs))
print(notes)

octave = np.hstack([single_tone(f) for f in freqs])
display(Audio(octave, rate=44100))

# harmony 화음 
tone_C = single_tone(261.62)
tone_E = single_tone(329.62)
tone_G = single_tone(392)
harmony = tone_C + tone_E + tone_G

plt.plot(harmony[:10000])
plt.show()

# 초당 샘플링 데이터 수 
sampling_rate = 44100
sp.io.wavfile.write("octave.wav", sampling_rate, octave)

sr, y_read = sp.io.wavfile.read("octave.wav")
# sr == sampling_rate

plt.plot(y_read[40000:50000])
plt.show()

# # sr = 16000이 의미하는 것은 1초당 16000개의 데이터를 샘플링 한다는 것입니다. sampling rate=16000
# y, sr = librosa.load(audio_path, sr=16000)

# print('sr:', sr, ', audio shape:', y.shape)
# print('length:', y.shape[0]/float(sr), 'secs')

# # Fourier -> Spectrum

# fft = np.fft.fft(y)

# magnitude = np.abs(fft) 
# frequency = np.linspace(0,sr,len(magnitude))

# left_spectrum = magnitude[:int(len(magnitude) / 2)]
# left_frequency = frequency[:int(len(frequency) / 2)]

# plt.figure(figsize = (10,5))
# plt.plot(left_frequency, left_spectrum)
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.title("Power spectrum")

# n_fft = 2048 
# hop_length = 512 

# stft = librosa.stft(y, n_fft = n_fft, hop_length = hop_length)
# spectrogram = np.abs(stft)
# print("Spectogram :\n", spectrogram)

# plt.figure(figsize = (10,5))
# librosa.display.specshow(spectrogram, sr=sr, hop_length=hop_length)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.plasma()
# plt.show()

# log_spectrogram = librosa.amplitude_to_db(spectrogram)

# plt.figure(figsize = (10,5))
# librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar(format="%+2.0f dB")
# plt.title("Spectrogram (dB)")

# mfcc = librosa.feature.mfcc(y, sr=16000, n_mfcc=20, n_fft=n_fft, hop_length=hop_length)
# plt.figure(figsize = (10,5))
# librosa.display.specshow(mfcc, sr=16000, hop_length=hop_length, x_axis='time')
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar(format='%+2.0f dB')
# plt.show()

