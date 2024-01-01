import os
import wolframalpha
import wikipedia
print("Welcome! 😁\n")

while True:
    text = input("Whats your question?\n")
    if text == "Stop":
        break
    else:
        try:

            answer = wikipedia.summary(text)
            print(answer)

        except:
            app_id = "LYPJEW-JH4W8XAQGY"
            client = wolframalpha.Client(app_id)
            res = client.query(text)

            try:
                answer = next(res.results).text
            except StopIteration:
                answer = "I'm sorry, but I did not understand your question...."

            print(answer)









        
