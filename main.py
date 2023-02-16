import openai
import os
from flask import Flask, request, jsonify

openai.api_key = os.getenv("OPENAI_API_KEY")

class Bot:
    def __init__(self, prompt) -> None:
        self.model_engine = "text-davinci-002"
        self.prompt = prompt

    def result(self):
        
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=self.prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.9
        )
        return completion.choices[0].text

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/output", methods=["POST"])
def output():
    prompt = request.form.get('prompt')
    output = Bot(prompt=prompt).result()
    result = {"result" : output}
    return jsonify(result)

def main():
    print("Server has started")
    app.run(debug=True, port=3000)

if __name__ == "__main__":
    main()
