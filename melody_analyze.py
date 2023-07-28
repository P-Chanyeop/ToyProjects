import librosa
import IPython.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.signal import find_peaks

# 계이름별 주파수 만들기
hertz2keys = {440: 'A_4'}
keys = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


# 440hz 이상 계산
octave = 4
pitch_num = 1
    
while True:
    if keys[pitch_num % 12] == 'C':
        octave += 1

    if octave > 8:
        break

    # calculate hz
    hz = round(440 * 2 ** (pitch_num / 12), 2) # 0을 대입하면 440hz 출력

    hertz2keys[hz] = keys[pitch_num % 12] + f'_{octave}'

    pitch_num += 1


# 440hz 이하 계산
octave = 4
pitch_num = -1
    
while True:
    if keys[pitch_num % 12] == 'B':
        octave -= 1

    if octave < 0:
        break
    # calculate hz
    hz = round(440 * 2 ** (pitch_num / 12), 2) # 0을 대입하면 440hz 출력

    hertz2keys[hz] = keys[pitch_num % 12] + f'_{octave}'

    pitch_num -= 1


path = './caono.wav'

# 음원 길이 설정(초)
duration = 22
data, sample_rate = librosa.load(path, sr=44100, mono=True, duration=duration)

# 1초 단위로 데이터 슬라이싱
sec = 1
trim_sec = int(1 / sec)
n_rows = data.shape[0] // sample_rate * trim_sec # 지정한 주기로 슬라이싱
dataset = data.reshape(n_rows, -1)

result = [] # detection 결과 수집
for sample in dataset:
    if sample.mean() == 0: # 구간 내 소리가 없는 경우 0 입력
        result.append(0) # No Signal
        continue
    
    autocorrelation = sm.tsa.acf(sample, nlags=200)
    peaks = find_peaks(autocorrelation)[0] # peak로 간주되는 지점 탐색
    
    if peaks.shape[0] == 0: # peak가 없는 경우 0 입력
        result.append(0) # No Peak
        continue
    
    lag = peaks[0]
    pitch = int(sample_rate / lag) # Transform lag into frequency
    
    result.append(pitch)

def herts_to_closed_key(hertz):
    """음원이 계이름과 정확하게 일치하는 hertz를 출력하지 않을 경우 근사하는 주파수의 계이름을 출력"""
    
    if hertz == 0: # 소리가 없는 경우 No Signal을 출력
        return 'NS'
    
    herts_array = np.array(list(hertz2keys.keys())) # 딕셔너리 key값을 리스트로 변경
    closed_index = np.argmin(abs(herts_array - hertz)) # 확인 대상과 가장 가까운 계이름 hertz 찾기
    key = hertz2keys[herts_array[closed_index]] # 출력
    
    return key

print(f"Length: {len(result)}")
print(result)
print([herts_to_closed_key(x) for x in result])

# Length: 22
# [0, 918, 588, 531, 918, 816, 588, 787, 864, 668, 604, 864, 787, 668, 711, 595, 558, 450, 580, 588, 572, 580]
# ['NS', 'Bb_5', 'D_5', 'C_5', 'Bb_5', 'G#_5', 'D_5', 'G_5', 'A_5', 'E_5', 'D_5', 'A_5', 'G_5', 'E_5', 'F_5', 'D_5', 'C#_5', 'A_4', 'D_5', 'D_5', 'D_5', 'D_5']