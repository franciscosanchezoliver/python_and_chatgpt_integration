from src.chatgtp.chatgpt import ChatGPT

if __name__ == "__main__":
    chatgtp = ChatGPT(api_key="")
    while True:
        question = input("say something:")
        response = chatgtp.ask(question=question)
        print("🤖: " + response)
