import requests


# For local streaming, the websockets are hosted without ssl - http://
HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'


def generate_text(prompt, params):

    request = {
        'prompt': prompt,
        'max_new_tokens': params['max_new_tokens'],

        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'None',
        'do_sample': params['do_sample'],
        'temperature': params['temperature'],
        'top_p': params['top_p'],
        'typical_p': params['typical_p'],
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': params['repetition_penalty'],
        'encoder_repetition_penalty': params['encoder_repetition_penalty'],
        'top_k': params['top_k'],
        'min_length': params['min_length'],
        'no_repeat_ngram_size': params['no_repeat_ngram_size'],
        'num_beams': params['num_beams'],
        'penalty_alpha': params['penalty_alpha'],
        'length_penalty': params['length_penalty'],
        'early_stopping': params['early_stopping'],
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,

        'seed': params['seed'],
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    response = requests.post(URI, json=request)

    # debug
    # print(response)

    reply = response.json()["results"][0]["text"]
    return reply
