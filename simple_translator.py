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
            # определяю язык
            detected = translator.detect(text)

            if detected.lang == 'ru':
                # русс то енг
                result = translator.translate(text, dest='en')
                print(f" английский: {result.text}")
            else:
                # с любвого на русс
                result = translator.translate(text, dest='ru')
                print(f" русский: {result.text}")

                # еще раз показываем
                print(f" исзодный изык: {detected.lang}")

        except Exception as e:
            print(f"❌ ерор: {e}")

if __name__ == "__main__":
    main()

