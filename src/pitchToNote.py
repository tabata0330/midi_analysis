import pretty_midi as pm

title = 'jupiter_4'

midi_data = pm.PrettyMIDI(title+'.mid')

for inst in midi_data.instruments:
    print(str(pm.program_to_instrument_name(inst.program)))