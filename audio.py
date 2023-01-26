import os
from narakeet_api import AudioAPI

api_key = os.environ['NARAKEET_API_KEY']
format = "wav"
voice = "victoria"
script = "Hello there from the long content API. This is Victoria speaking!"

def show_progress(progress_data):
    # change this to do something smarter with percent, message and thumbnail
    print(progress_data)

api = AudioAPI(api_key)

# start a build task using the text sample and voice
# and wait for it to finish
task = api.request_audio_task(format, script, voice)
task_result = api.poll_until_finished(task['statusUrl'], show_progress)

# grab the result file
if task_result['succeeded']:
    filename = f'output.{format}'
    api.download_to_file(task_result['result'], filename)
    print(f'downloaded to {filename}')
else:
    raise Exception(task_result['message'])
