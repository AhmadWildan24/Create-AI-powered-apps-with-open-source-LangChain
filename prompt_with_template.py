import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_community.llms import HuggingFaceEndpoint

huggingFace_API_Key = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingFace_API_Key
# Mendefinisikan model AI

llm = HuggingFaceEndpoint(
    repo_id="google/flan-ul2",
    HUGGINGFACEHUB_API_TOKEN = huggingFace_API_Key 
)
# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["posisi", "perusahaan", "keterampilan"],
    template="Yang terhormat HRD Manajer {perusahaan},\n\nDengan surat ini, saya [NAMA KAMU], ingin melamar untuk posisi {posisi} di {perusahaan}. Saya memiliki pengalaman di bidang {keterampilan}. Terima kasih telah mempertimbangkan lamaran saya.\n\nHormat saya,\n[NAMA KAMU]",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm.invoke(formatted_prompt)
    return response
# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan")
]
# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")
# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860, share=True)