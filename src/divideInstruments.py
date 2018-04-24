import pretty_midi
import os
# import matplotlib.pyplot as plt

title = 'vn_concerto_tch'

midi_data = pretty_midi.PrettyMIDI(title+'.mid')

if not os.path.isdir('output'):
    os.mkdir('output')

if not os.path.isdir('output/' + str(title)):
    os.mkdir('output/' + str(title))


for i in range(0, len(midi_data.instruments)):

    instrument = midi_data.instruments[i]
    program_num = instrument.program

    rev_en_chord = pretty_midi.PrettyMIDI()

    rev_en_chord.instruments.append(instrument)

    rev_en_chord.write('output/' + str(title) + '/' + str(title) + '_ins_' + str(pretty_midi.program_to_instrument_name(program_num).replace(' ', '_') + '_') + str(i) + '.mid')
