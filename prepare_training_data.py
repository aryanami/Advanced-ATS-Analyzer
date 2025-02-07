import json
import openai

def prepare_training_data(examples):
    training_data = []
    for example in examples:
        training_data.append({
            "messages": [
                {"role": "user", "content": example["prompt"]},
                {"role": "assistant", "content": example["completion"]}
            ]
        })
    return training_data

def prepare_fine_tuning_data(examples_file):
    with open(examples_file, 'r') as f:
        examples = json.load(f)
    
    training_data = prepare_training_data(examples)
    
    # Save training data in JSONL format
    with open('training_data.jsonl', 'w') as f:
        for example in training_data:
            f.write(json.dumps(example) + '\n')
    
    # Upload training file to OpenAI
    upload_response = openai.File.create(
        file=open('training_data.jsonl', 'rb'),
        purpose='fine-tune'
    )
    
    return upload_response.id 