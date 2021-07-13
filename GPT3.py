import os
from glob import glob

import openai

from components import *

openai.api_key = ""


class GPT3:
    def __init__(self):
        self.start_sequence = "\nA:"
        self.restart_sequence = "\nQ:"
        self.engine = "curie-instruct-beta"
        self.engine_qss = "curie-instruct-beta"
        self.temperature = 0
        self.temperature_qss = 0.2
        self.max_tokens = 250
        self.shots = ''
        self.style = ''

    def select_shots(self, content):
        self.shots = ''
        files = glob(f'shots/{content}*')
        for file in files:
            f = open(file, 'r')
            self.shots += f.read()

    def generate_ui(self, input_):
        print(f"{self.shots} \nQ: {input_} \nA:",)
        response = openai.Completion.create(
            engine=self.engine,
            prompt=f"{self.shots} \nQ: {input_} \nA:",
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0.2,
            stop=["#end", "Q:"]
        )
        g = open('ui.py', 'w')
        g.write(PYQT_HEADER)
        response = response["choices"][0]["text"].split('\n')
        for line in response:
            g.write(f'        {line}\n')
        g.write(PYQT_FOOTER(self.style))
        g.close()


        os.system('python ui.py')

    def generate_style(self, input_):
        response = openai.Completion.create(
            engine=self.engine_qss,
            prompt=f"{self.shots} \nQ: {input_} \nA:",
            temperature=self.temperature_qss,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0.15,
            presence_penalty=0.3,
            stop=["Q:"]
        )
        self.style = response["choices"][0]["text"]
        print(response['choices'][0]["finish_reason"])


    def generate_placeholder(self):
        g = open('ui.py', 'w')
        g.write(PYQT_HEADER)
        g.write(PLACEHOLDER)
        g.write(PYQT_FOOTER(self.style))
        g.close()
        os.system('python ui.py')

# gpt3 = GPT3()
# gpt3.select_shots()
# gpt3.generate_ui('formular de inscriere la o scoala cu checkbox pentru acord parental')
