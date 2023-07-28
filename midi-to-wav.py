import wave
import os
import numpy as np
from midiutil.MidiFile import MIDIFile
import matplotlib.pyplot as plt
from scipy.fft import fft
import math
import pyaudio

CHUNK_SIZE = 8192
OVERLAP = 4800
TRACK_AMOUNT = 8

fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

audio = wave.open(f"{os.getcwd()}/caono.wav", 'rb')
frame_rate = audio.getframerate()
num_frames = audio.getnframes()
duration = num_frames/frame_rate

# Read all frames
frames = audio.readframes(num_frames)
audio.close()

audio_signal = np.frombuffer(frames, dtype=np.int16)

x = CHUNK_SIZE*2
sound = []

while x<num_frames:
    yfft = fft(audio_signal[x-CHUNK_SIZE:x])[:int(CHUNK_SIZE*0.75)]
    frequencies = np.argsort(yfft)[len(yfft)-TRACK_AMOUNT:]
    volumes = np.sort(yfft)[len(yfft)-TRACK_AMOUNT:]
    sound.append([frequencies, volumes])
    x+=OVERLAP

sound = np.array(sound)
max_volumes = []

for i in range(0, TRACK_AMOUNT):
    max_volumes.append(np.amax(sound[:,1,i]))

max_volume = math.sqrt(max(max_volumes))

for i in range(0, len(sound)):
    for j in range(0, TRACK_AMOUNT):
        sound[i][1][j] = math.sqrt(sound[i][1][j])/max_volume*100

ax1.plot(sound[:,0,0])
ax2.plot(sound[:,1,0])

mf = MIDIFile(TRACK_AMOUNT)     # only 1 track
time = 0    

for i in range(0, TRACK_AMOUNT):
    mf.addTrackName(i, time, f"Track {i}")
    mf.addTempo(i, time, int(frame_rate/OVERLAP)*60)

# add some notes
channel = 0
note_length = duration/len(sound)
for value in sound:
    for i in range(0, TRACK_AMOUNT):
        if(value[0][i] != 0):
            volume = abs(value[1][i])
            pitch = 12*math.log2(value[0][i]*frame_rate/CHUNK_SIZE/220.0)+57
            mf.addNote(i, channel, int(pitch), int(time), 1, int(volume))
    time += 1

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)

plt.show()