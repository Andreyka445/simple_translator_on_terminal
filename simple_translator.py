from googletrans import Translator

def main():
    print("🐍 самый простой переводчик")
    print("чтобы выйти напиши 'exit'")
    
    translator = Translator()

    while True:
        text = input("\nсюда текст, который хочешь перевести: ").strip()
        
        if text.lower() in ['exit', 'выход', 'quit']:
            print("пака! 👋")
            break
            
        if not text:
            continue
            
        try:
            result = translator.translate(text, dest='ru')
            print(f"📝 перевод: {result.text}")
            
        except Exception as e:
            print(f"❌ еррор: {e}")

if __name__ == "__main__":
    main()
