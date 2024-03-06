# Menggunakan Hugging FaceHub
import os
import gradio as gr
from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "token API Hugging Face"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def chatbot(prompt):
    return llm.invoke(prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)