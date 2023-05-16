import openai

openai.api_key="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"




class bookReview :

    title = ""
    author = ""
    region = ""

    def __init__(self,title,author,region):
        self.title = title
        self.author = author
        self.region = region


    
    def review(self):
        message = self.region + "의 작가" + self.author + "의 책" + self.title + "의 감상문을 작성해줘"

        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        return completion.choices[0].message.content

    
    def quote(self):
        message = self.region + "의 작가" + self.author + "의 책" + self.title +  "에서 주요 문장 하나를 인용하고 인용한 이유를 알려줘"

        completion = openai.ChatCompletion.create(

        model ="gpt-3.5-turbo",
        messages=[
            {"role" : "user", "content" : message}
        ]
        )
        return completion.choices[0].message.content

    def summary(self):
        message = self.region+ "의 책 " + self.title + "의 작가는"+ self.author + "이고 이 책의 내용을 요약해줘"

        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages=[
                {"role" : "user", "content" : message}
                ]
            )
        return completion.choices[0].message.content
        


print("책 제목을 입력해주세요")
title = input()

print("작가를 입력해주세요")
author = input()

print("국가를 입력해주세요")
region = input()

print("시작")

BC = bookReview(title,author,region)


print(BC.review())
print(BC.quote())
print(BC.summary())

