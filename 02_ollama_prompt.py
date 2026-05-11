import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

model_name = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

llm = ChatOllama(model=model_name, temperature=0)

print("💬 Chatbot IA prêt ! Tape 'exit' pour quitter\n")

# mémoire de la conversation
history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("Toi : ")

    if user_input.lower() == "exit":
        print("Bye 👋")
        break

    # ajouter message utilisateur
    history.append({"role": "user", "content": user_input})

    # appel IA
    response = llm.invoke(history)

    reply = response.content
    print("IA :", reply)

    # ajouter réponse IA à la mémoire
    history.append({"role": "assistant", "content": reply})