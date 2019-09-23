#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiml
import os
import argparse
import sys
from playsound import playsound

reload(sys)
sys.setdefaultencoding('utf8')

def speak(sexta_responde):
	os.system("espeak -s 145 -v pt+f4 '{}'".format(sexta_responde))

kernel = aiml.Kernel()
#kernel.verbose(False)

kernel.setBotPredicate("name", "Sexta")

#if os.path.isfile("bot_brain.brn"):
#    kernel.bootstrap(brainFile = "bot_brain.brn")
#else:
#    kernel.bootstrap(learnFiles = os.path.abspath("std-startup.xml"), commands = "load aiml b")
#    kernel.saveBrain("bot_brain.brn")

kernel.bootstrap(learnFiles = os.path.abspath("/etc/sexta/std-startup.xml"), commands = "load aiml b")

# kernel now ready for use
while True:
    playsound('/etc/sexta/wav/voice_start.wav')
    message = raw_input(">> ")
    if message == "sair":
        exit()
    elif message == "salvar":
        kernel.saveBrain("bot_brain.brn")
    else:
        jarvis_responde = kernel.respond(message)
        print "> ", jarvis_responde
	playsound('/etc/sexta/wav/voice_stop.wav')
	speak(jarvis_responde)

