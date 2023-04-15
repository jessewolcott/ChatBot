import openai
import gradio
import keys

openai.api_key = keys.apptoken

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gradio.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gradio.outputs.Textbox(label="Reply")

gradio.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Bot",
             description="Ask anything you want",
             theme="compact").launch(share=True)