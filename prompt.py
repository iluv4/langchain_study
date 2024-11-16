from langchain import PromptTemplate

prompt = PromptTemplate(
    template="{product}는 어디 회사에서 개발한 제품인가요?",

    input_variables = [
        "product"
    ]
)

print(prompt.format(product=('hi')))

print(prompt.format(product=('li')))
