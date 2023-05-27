from dbControl import *

#gui대신 임시로 사용하는 테스트용 실행 클래스


class Executer :


    BookList = []

    def __init__(self) -> None:
        pass
    


    def Show(self) :
        count = 1

        for title, author in self.BookList :
            print("%d : %s   %s" %(count, title, author))
            count = count +1

   

    def Start(self) :

        key = "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"

        openai.api_key = key
        #gpt 인증키

        DB = dbControl()

        while(1):
            print("수행할 작업을 선택하시오 : \n")
            print("1. DB에서 불러오기 2. 작가 검색 3. 제목 검색 \n")
            print("4. 책 목록 출력 5. GPT 생성")
 
            number = int(input())

            if number == 1:
                self.BookList = DB.makeListAll()
            elif number == 2:
                author_name = input("작가 이름을 입력하세요: ")
                self.BookList = DB.SearchAuthor(author_name)
            elif number == 3:
                title_name = input("책 제목을 입력하세요: ")
                self.BookList = DB.SearchTitle(title_name)
            elif number == 4:
                self.Show()

            elif number == 5:
                self.GPT()

            else :
                print("정의되지 않은 동작\n")


    def GPT(self) :
        print("몇번 책을 고르시겠습니까")
        n = int(input())

        if n < len(self.BookList):
            Book = self.BookList[n]

        print("감상평 : %s\n" % Book.Review())
        
        print("\n")

        print("주요 문장 인용 : %s\n" % Book.Quote())
        
        print("\n")

        print("줄거리 요약 : %s\n" % Book.Summary())
        
        print("\n")

        print("토론 주제 및 답변 : %s\n" % Book.Debate())
        
        print("\n")

        
      
Ex = Executer()
Ex.Start()








        

        