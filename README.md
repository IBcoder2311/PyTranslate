# PyTranslate
Приложение-переводчик на Kivy. Позволяет выбрать язык перевода и перевести введённый текст. Интерфейс оформлен в темной гамме и поддерживает кнопки, поля ввода и выпадающие списки.

## Technologies
- Python
- Kivy (GUI)
- Translator module (wrapper around translation)

## Features
- Dark window theme
- Multiple target languages: Russian, English, French, Spanish, German, Estonian, Finnish, Turkish
- Text input and output fields
- "Translate" button to perform translation
- Basic error handling during translation

## Project structure
- main.py (example code shown above)
  - MyApp — main application class, inherits from App
  - build() — assembles and returns the root layout
  - on_spinner_select() — language selection handler
  - on_btn_press() — performs translation and updates the result
- Kivy components used:
  - App, BoxLayout, Image, Button, TextInput, Spinner, Label
  - Window to change background color
- Translation module:
  - Translator (from the external translate module)

## How it works
- The user selects the target translation language from the Spinner (e.g., Russian, English, etc.).
- Based on the chosen language, a language code is set (ru, en, fr, es, de, et, fi, tr) and a Translator(to_lang=...) instance is created.
- Pressing the “Translate” button translates the text from the input field and shows the result in the output field.

## Installation
1.Install Python 3.x
2.Install dependencies (environment dependent):
```

pip install kivy

```

```

pip install translate (or the equivalent translation library you use)

```
3.Run the app:
```

python main.py

```

## Usage example

- Open the app.
- Select a target language (e.g., English).
- Enter text in the “Enter text” field.
- Press `Translate`.
- The result appears in the output field.
