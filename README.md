# 📚 Xbato Manga Downloader

[English](#english) | [Русский](#russian)

---

<a name="english"></a>
## 🇬🇧 English

### Description

A Python script to download manga from Xbato.co.uk (and its mirrors). Features an interactive interface with language selection and easy domain configuration.

### ✨ Features

- 🌐 **Multi-language interface** (English/Russian)
- 🔄 **Easy domain switching** - change domain in one line if site moves
- 💬 **Interactive mode** - user-friendly prompts for beginners
- ⚡ **Command-line mode** - quick downloads for advanced users
- 📁 **Custom save location** - choose where to save your manga
- 🎯 **Auto-detection** - automatically finds all chapters
- 📊 **Progress tracking** - see download progress in real-time
- ⏸️ **Resume support** - skips already downloaded images

### 🚀 Quick Start

#### Installation

1. **Clone the repository:**
```bash
https://github.com/FILyaKIRya/Xbato-manga-downloader.git
cd xbato-downloader
```

2. **Install dependencies:**
```bash
pip3 install -r requirements.txt
```

Or manually:
```bash
pip3 install requests beautifulsoup4
```

#### Usage

**Interactive Mode (Recommended for beginners):**
```bash
python3 xbato_downloader_interactive.py
```

The program will ask you:
1. Select language (English/Russian)
2. Enter manga chapter URL
3. Choose save location

**Command-line Mode (For advanced users):**
```bash
python3 xbato_downloader_interactive.py "CHAPTER_URL" [OUTPUT_FOLDER]
```

**Examples:**
```bash
# Download to current directory
python3 xbato_downloader_interactive.py "https://xbato.co.uk/read/too-many-losing-heroines/chapter-1"

# Download to specific folder
python3 xbato_downloader_interactive.py "https://xbato.co.uk/read/too-many-losing-heroines/chapter-1" "/path/to/manga"
```

### ⚙️ Configuration

#### Changing Domain

If the site moves to a new domain, open `xbato_downloader_interactive.py` and change:

```python
BASE_DOMAIN = "https://xbato.co.uk"  # Change to new domain
```

For example, if site moves to `xbato.net`:
```python
BASE_DOMAIN = "https://xbato.net"
```

#### Adjusting Download Speed

In the same file, find and modify:

```python
DELAY_BETWEEN_CHAPTERS = 2.0  # Delay between chapters (seconds)
DELAY_BETWEEN_IMAGES = 0.5    # Delay between images (seconds)
```

⚠️ **Not recommended** to set very low values to avoid overloading the server.

### 📋 Requirements

- Python 3.6 or higher
- Libraries:
  - `requests`
  - `beautifulsoup4`

### 📁 Output Structure

```
Manga_Title/
├── Chapter 1/
│   ├── 001.webp
│   ├── 002.webp
│   └── ...
├── Chapter 2/
│   ├── 001.webp
│   ├── 002.webp
│   └── ...
└── ...
```

### ❓ FAQ

**Q: Files are in wrong order?**  
A: Files are named correctly (001, 002, 003...). If your file manager shows them incorrectly, sort by name.

**Q: Site moved to new domain?**  
A: See "Changing Domain" section above.

**Q: Script doesn't work / shows error?**  
A: 
1. Make sure all dependencies are installed
2. Check that URL is correct (must contain `/read/`)
3. Check internet connection
4. Site structure may have changed - please report

**Q: Can I download only one chapter?**  
A: No, the script downloads all chapters. But you can stop it (Ctrl+C) after the desired chapter.

**Q: How to stop download?**  
A: Press Ctrl+C

### 📝 License

This script is provided "as is" for personal use.

### ⚠️ Disclaimer

This script is intended for personal use only. Make sure you comply with copyright laws and the site's terms of service.

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 📧 Support

If you encounter any issues, please [open an issue](https://github.com/yourusername/xbato-downloader/issues).

---

<a name="russian"></a>
## 🇷🇺 Русский

### Описание

Python-скрипт для скачивания манги с сайта Xbato.co.uk (и его зеркал). Имеет интерактивный интерфейс с выбором языка и простой настройкой домена.

### ✨ Возможности

- 🌐 **Многоязычный интерфейс** (Английский/Русский)
- 🔄 **Легкая смена домена** - измените домен в одной строке, если сайт переехал
- 💬 **Интерактивный режим** - удобные подсказки для новичков
- ⚡ **Режим командной строки** - быстрая загрузка для опытных пользователей
- 📁 **Выбор папки сохранения** - выберите, куда сохранить мангу
- 🎯 **Автоопределение** - автоматически находит все главы
- 📊 **Отслеживание прогресса** - видите прогресс загрузки в реальном времени
- ⏸️ **Поддержка возобновления** - пропускает уже скачанные изображения

### 🚀 Быстрый старт

#### Установка

1. **Клонируйте репозиторий:**
```bash
https://github.com/FILyaKIRya/Xbato-manga-downloader.git
cd xbato-downloader
```

2. **Установите зависимости:**
```bash
pip3 install -r requirements.txt
```

Или вручную:
```bash
pip3 install requests beautifulsoup4
```

#### Использование

**Интерактивный режим (Рекомендуется для новичков):**
```bash
python3 xbato_downloader_interactive.py
```

Программа спросит:
1. Выберите язык (Английский/Русский)
2. Введите URL главы манги
3. Выберите место сохранения

**Режим командной строки (Для опытных пользователей):**
```bash
python3 xbato_downloader_interactive.py "URL_ГЛАВЫ" [ПАПКА_СОХРАНЕНИЯ]
```

**Примеры:**
```bash
# Скачать в текущую папку
python3 xbato_downloader_interactive.py "https://xbato.co.uk/read/too-many-losing-heroines/chapter-1"

# Скачать в указанную папку
python3 xbato_downloader_interactive.py "https://xbato.co.uk/read/too-many-losing-heroines/chapter-1" "/путь/к/манге"
```

### ⚙️ Настройка

#### Изменение домена

Если сайт переехал на новый домен, откройте `xbato_downloader_interactive.py` и измените:

```python
BASE_DOMAIN = "https://xbato.co.uk"  # Измените на новый домен
```

Например, если сайт переехал на `xbato.net`:
```python
BASE_DOMAIN = "https://xbato.net"
```

#### Настройка скорости загрузки

В том же файле найдите и измените:

```python
DELAY_BETWEEN_CHAPTERS = 2.0  # Пауза между главами (секунды)
DELAY_BETWEEN_IMAGES = 0.5    # Пауза между изображениями (секунды)
```

⚠️ **Не рекомендуется** ставить слишком маленькие значения, чтобы не перегружать сервер.

### 📋 Требования

- Python 3.6 или выше
- Библиотеки:
  - `requests`
  - `beautifulsoup4`

### 📁 Структура файлов

```
Название_Манги/
├── Chapter 1/
│   ├── 001.webp
│   ├── 002.webp
│   └── ...
├── Chapter 2/
│   ├── 001.webp
│   ├── 002.webp
│   └── ...
└── ...
```

### ❓ Частые вопросы

**В: Файлы в неправильном порядке?**  
О: Файлы названы правильно (001, 002, 003...). Если файловый менеджер показывает их неправильно, отсортируйте по имени.

**В: Сайт переехал на новый домен?**  
О: См. раздел "Изменение домена" выше.

**В: Скрипт не работает / выдает ошибку?**  
О: 
1. Убедитесь, что установлены все зависимости
2. Проверьте, что URL правильный (должен содержать `/read/`)
3. Проверьте подключение к интернету
4. Возможно, сайт изменил структуру - сообщите об этом

**В: Можно ли скачать только одну главу?**  
О: Нет, скрипт скачивает все главы. Но вы можете остановить его (Ctrl+C) после нужной главы.

**В: Как остановить загрузку?**  
О: Нажмите Ctrl+C

### 📝 Лицензия

Скрипт предоставляется "как есть" для личного использования.

### ⚠️ Дисклеймер

Этот скрипт предназначен только для личного использования. Убедитесь, что вы соблюдаете авторские права и условия использования сайта.

### 🤝 Участие в разработке

Приветствуются любые вклады! Не стесняйтесь отправлять Pull Request.

### 📧 Поддержка

Если вы столкнулись с проблемами, пожалуйста [создайте issue](https://github.com/yourusername/xbato-downloader/issues).

---

## 📸 Screenshots / Скриншоты

```
======================================================================
  📚 XBATO MANGA DOWNLOADER 📚
======================================================================
  Current domain: https://xbato.co.uk
======================================================================

🌐 Select language / Выберите язык:
   1. English
   2. Русский

   Choice / Выбор (1 or 2): 
```

---

## 🛠️ Development / Разработка

### Project Structure / Структура проекта

```
xbato-downloader/
├── xbato_downloader_interactive.py  # Main script with UI
├── xbato_downloader.py              # Legacy version
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── ИНСТРУКЦИЯ.txt                   # Russian quick guide
└── XBATO_README.md                  # Detailed documentation
```

### Code Structure / Структура кода

- `get_page_content()` - Loads HTML page
- `get_manga_title_from_page()` - Extracts manga title
- `get_all_chapters_from_page()` - Gets list of all chapters
- `get_chapter_images()` - Extracts image URLs from chapter
- `download_file()` - Downloads file
- `download_manga()` - Main download function

---

Made with ❤️ for manga lovers

Сделано с ❤️ для любителей манги

