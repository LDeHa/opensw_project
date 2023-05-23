import openai

openai.api_key = "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"




class bookGPT :

    def __init__(self) -> None:
        pass


    
    def review(self,title,author):
        message = "작가 " + author + "의 책 " + title + "의 감상문을 작성해줘"

        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        return completion.choices[0].message.content

    
    def quote(self,title,author):
        message = "작가 " + author + "의 책 " + title +  "에서 주요 문장 하나를 인용하고 인용한 이유를 알려줘"


        completion = openai.ChatCompletion.create(

        model ="gpt-3.5-turbo",
        messages=[
            {"role" : "user", "content" : message}
        ]
        )
        return completion.choices[0].message.content

    def summary(self,title,author):
        message = "책 " + title + "의 작가는 "+ author + "이고 이 책의 내용을 요약해줘"

        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        return completion.choices[0].message.content
    
    def debate(self,title,author):
        message = "책 " + title + "의 작가는 "+ author + " 이고 이 책에서 구절 하나를 인용해서 토론 주제를 정하고, 그 주제에 대해서 너의 의견을 말해줘"

        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        return completion.choices[0].message.content
        