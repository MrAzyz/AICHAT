from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()
 
template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)


repo_id = "google/flan-t5-xxl" 


llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.6}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

def generate_response(question):
    return llm_chain.invoke(question).get('text')
#answer = response.split('.')[1].split(':')[1].strip()