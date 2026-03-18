from langchain_openai import ChatOpenAI
import openai
import os
# 调用非对话模型
# llm = OpenAI(...)
print(os.environ["OPENAI_BASE_URL"])
print(os.environ["OPENAI_API_KEY"])
# 调用对话模型
chat_model = ChatOpenAI(
    #必须要设置的3个参数
    model_name="gpt-4o-mini", #默认使用的是gpt-3.5-turbo模型
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

#调用模型
response = chat_model.invoke("什么是langchain")

#查看响应的文本
print(response.content)