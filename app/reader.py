# imports
from gtts import gTTS
import gradio as gr
import os
import eng_to_ipa as p
import json

# load country and language config
with open('../config.json') as json_file:
    data = json.load(json_file)


def generate_name(emp_name, emp_id, language_selected, country_selected, speed):
    """
     Function to generate name from google text to speech or customised pronunciation
    """
    #   retrieve county and language codes
    language_code = data['language_list'][language_selected]
    country_code = data['country_list'][country_selected]

    phonetic_word = p.convert(emp_name)
    if os.path.exists(emp_id + ".wav"):
        audio = emp_id + ".wav"
        return audio, phonetic_word
    else:
        audio_object = gTTS(text=emp_name, lang=language_code, slow=speed, tld=country_code)
        audio_object.save("test.wav")
        return 'test.wav', phonetic_word


iface = gr.Interface(fn=generate_name,

                     inputs=["text", "text",
                             gr.inputs.Dropdown(list(data['language_list'].keys()),
                                                type="value", default="English", label="Language", optional=False),
                             gr.inputs.Dropdown(list(data['country_list'].keys()),
                                                type="value", default="India", label="Country", optional=False)
                         , gr.inputs.Checkbox(label="slow")],

                     outputs=[gr.outputs.Audio(type="auto", label="Audio"),
                              gr.outputs.Textbox(type="auto", label="Phonetics")],
                     title='Get Your Name Right',
                     description='Pronounces your name',
                     article=
                     '''<div>
                            <p>Check your Name Pronounciation</p>
                        </div>''',
                     allow_flagging='never',
                     )

# launch UI
iface.launch(server_port=7869)
