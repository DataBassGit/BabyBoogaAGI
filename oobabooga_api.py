import requests

# Server address
server = "127.0.0.1"

def generate_text(prompt, params):
    response = requests.post(f"http://{server}:7860/run/textgen", json={
        "data": [
            prompt,
            params['max_new_tokens'],
            params['do_sample'],
            params['temperature'],
            params['top_p'],
            params['typical_p'],
            params['repetition_penalty'],
            params['encoder_repetition_penalty'],
            params['top_k'],
            params['min_length'],
            params['no_repeat_ngram_size'],
            params['num_beams'],
            params['penalty_alpha'],
            params['length_penalty'],
            params['early_stopping'],
            params['seed']
        ]
    }).json()

    reply = response["data"][0]
    return reply
