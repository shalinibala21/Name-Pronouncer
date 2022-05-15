# import packages
import shutil
import gradio as gr


def record(emp_id, audio):
    """
    Function to customise name pronounciaton
    :param emp_id:
    :param audio:
    :return: success message
    """
    src = audio
    dst = emp_id + ".wav"
    shutil.copy(src, dst)
    return 'Saved successfully!'


iface = gr.Interface(fn=record,
                     inputs=["text", gr.inputs.Audio(source="microphone", type='filepath')],
                     outputs='text',
                     title='Customize Pronounce',
                     description='Records and save your name',
                     article=
                     '''<div>
                         <p>After recording your customized name pronunciation, You can hear the playback in Get Your Name Right Section</p>
                     </div>''',
                     allow_flagging='never'
                     )
# launch UI
iface.launch(server_port=7870)
