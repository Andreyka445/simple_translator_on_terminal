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
            # Автоматически определяем язык
            detected = translator.detect(text)
            src_lang = detected.lang
            src_lang_name = LANGUAGES.get(src_lang, src_lang)
            
            print(f"🔍 Определен язык: {src_lang_name}")
            
            # Предлагаем варианты перевода
            if src_lang == 'ru':
                print("🌍 на какой язык переводим??")
                print("1. англ (en)")
                print("2. испанский (es)")
                print("3. французкий (fr)")
                print("4. нужен другой пример? (пиши код языка например 'en')")
            else:
                print("🌍 куда переводим??")
                print("1. русский (ru) - автоматически")
                print("2. англ (en)")
                print("3. другой язык (напиши код языка код)")
            
            choice = input("Твой выбор (1/2/3/4 или код языка): ").strip().lower()
            
            if choice == '1':
                dest_lang = 'en' if src_lang == 'ru' else 'ru'
            elif choice == '2':
                dest_lang = 'es' if src_lang == 'ru' else 'en'
            elif choice == '3' and src_lang == 'ru':
                dest_lang = 'fr'
            elif choice == '3' and src_lang != 'ru':
                dest_lang = input("введи код языка (например: de, it, ja): ").strip().lower()
            elif choice == '4' and src_lang == 'ru':
                dest_lang = input("введи код языка (например: de, it, ja): ").strip().lower()
            elif len(choice) == 2:
                dest_lang = choice
            else:
                dest_lang = 'en' if src_lang == 'ru' else 'ru'
                print(f"⚠️ Использую {dest_lang} по умолчанию")
            
            result = translator.translate(text, dest=dest_lang)
            dest_lang_name = LANGUAGES.get(dest_lang, dest_lang)
            print(f"🎯 перевод на {dest_lang_name}: {result.text}")
                
        except Exception as e:
            print(f"❌ еррор: {e}")

if __name__ == "__main__":
    main()

