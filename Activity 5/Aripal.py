import os
if not os.path.exists('thinkdsp.py'):
    !wgetimport matplotlib.pyplot as plt
import matplotlib.pyplot as plt

from thinkdsp import decorate    

if not os.path.exists('263868__kevcio__amen-break-a-160-bpm.wav'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/92002__jcveliz__violin-origional.wav\
from thinkdsp import read_wave

wave = read_wave('263868__kevcio__amen-break-a-160-bpm.wav')

wave.make_audio()
