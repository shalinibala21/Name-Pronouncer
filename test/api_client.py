import requests
import gradio as gr

r = requests.post(url='http://127.0.0.1:7860/api/predict/',
                  json={"data":
                            ["Shalini Ramasami",
                             "815124",
                             "English",
                             "Australia",
                             1
                             ]})
response = r.json()
encoding = response['data'][0]

gr.processing_utils.decode_base64_to_file(encoding, encryption_key=None, file_path="api.wav")
