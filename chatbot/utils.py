import os
from io import BytesIO
import requests
import json
import re
from typing import Any, Dict, List

from django.conf import settings

from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType, ZeroShotAgent, ConversationalChatAgent, AgentExecutor, create_pandas_dataframe_agent
from langchain import LLMMathChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import SerpAPIWrapper
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma, FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.document_loaders import DataFrameLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import PDFMinerLoader
#from langchain.document_loaders import PyPDFium2Loader
from langchain.document_loaders import PyMuPDFLoader
#from langchain.document_loaders import PDFPlumberLoader

from pypdf import PdfReader
from langchain.chains import RetrievalQAWithSourcesChain

openai_api_key = settings.OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = openai_api_key

def parse_pdf(file: BytesIO) -> List[str]:
    pdf = PdfReader(file)
    output = []
    for page in pdf.pages:
        text = page.extract_text()
        # Merge hyphenated words
        text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
        # Fix newlines in the middle of sentences
        text = re.sub(r"(?<!\n\s)\n(?!\s\n)", " ", text.strip())
        # Remove multiple newlines
        text = re.sub(r"\n\s*\n", "\n\n", text)
        output.append(text)
    #return output
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    pages = text_splitter.create_documents(output)
    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    #texts = text_splitter.create_documents(pages)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(pages, embeddings)
    index_file_path = os.path.join(settings.BASE_DIR, 'data',)
    vectorstore.save_local(index_file_path)
	#vectorstore.save_local("pdf_data")
    result = 'Done!, Data successfully embedded'
    return [result, output]

def generate_answers(message):

	prompt_template = """Use the following pieces of context to answer the question at the end.
	If you don't know the answer, just say that you don't know, don't try to make up an answer.

	{context}

	Question: {question}
	"""
	PROMPT = PromptTemplate(

    	template=prompt_template, input_variables=["context", "question"]
    )

	chain_type_kwargs = {"prompt": PROMPT}

	llm = OpenAI(temperature=0)
	embeddings = OpenAIEmbeddings()
	index_file_path = os.path.join(settings.BASE_DIR, 'data',)
	vectorstore = FAISS.load_local(index_file_path, embeddings)
	qa = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="map_reduce", retriever=vectorstore.as_retriever(), chain_type_kwargs=chain_type_kwargs)
	query = message
	#chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0, max_tokens=1500, model_name='text-davinci-003'), vectorstore=store)
	#result = chain({"question": args.question})
	result = qa({"question": query})

	return result['answer']
