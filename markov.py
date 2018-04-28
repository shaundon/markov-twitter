import json
import markovify

def get_tweet():
    config = json.load(open('config.json'))
    inputFile = config['inputFile']

    # Get raw text as string.
    with open(inputFile) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print three randomly-generated sentences of no more than 140 characters
    return text_model.make_short_sentence(140)