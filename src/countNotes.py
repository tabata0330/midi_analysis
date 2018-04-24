import pretty_midi
import matplotlib.pyplot as plt

title = 'evans'

midi_data = pretty_midi.PrettyMIDI(title+'.mid')

instrument_name = 'Distortion Guitar'

instruments = midi_data.instruments

dg = pretty_midi.PrettyMIDI()

for instrument in instruments:
    if pretty_midi.program_to_instrument_name(instrument.program).__eq__(instrument_name):
        dg.instruments.append(instrument)

print(dg.instruments[0].notes)

dg_pitch_list = []

for note in dg.instruments[0].notes:
    dg_pitch_list.append(note.pitch)

print(dg_pitch_list)


def pitchToNote(pitch):
    picth_mod = (pitch + 4) % 12
    pitch_div = (pitch + 4) // 12
    notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note = notes_list[picth_mod] + str(pitch_div - 1)
    return note


note_list = list(map(lambda x: pitchToNote(x), dg_pitch_list))
print(note_list)

plt.hist(note_list)
plt.show()
