from langchain.chat_models import init_chat_model

llm = init_chat_model("openai:gpt-4.1", temperature=0.7)



print(llm.invoke("give me a step 1 question about biochemistry"))




