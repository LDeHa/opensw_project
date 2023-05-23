from dbControl import *


class Executer :

    BookList : typeBook = []

    def __init__(self) -> None:
        pass
    


    def Show(self) :
        for title, author in self.BookList :
            print("%s   %s" %title %author)

   

    def Start(self) :
        DB = dbControl()

        while(1):
            print("수행할 작업을 선택하시오 : \n")
            print("1. DB에서 불러오기 2. 작가 검색 3. 제목 검색 \n")
            print("4. 책 목록 출력 5. GPT 생성")
 
            number = int(input())

            if number == 1:
                self.BookList = DB.makeListAll()
            elif number == 2:
                self.BookList = DB.SearchAuthor()
            elif number == 3:
                self.BookList = DB.SearchTitle()
            elif number == 4:
                self.Show()
            else :
                print("정의되지 않은 동작")


    def GPT(self) :
        print("몇번 책을 고르시겠습니까")
        n = input()

        Book : typeBook = self.BookList[n]

        print("감상평 : \n")
        Book.Review()
        print("\n")

        print("주요 문장 인용 : \n")
        Book.Quote()
        print("\n")

        print("줄거리 요약 : \n")
        Book.Summary()
        print("\n")

        print("토론 주제 및 답변 : \n")
        Book.Debate()
        print("\n")

        
      
Ex = Executer()
Ex.Start()








        

        