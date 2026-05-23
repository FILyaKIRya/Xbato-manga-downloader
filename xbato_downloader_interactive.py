#!/usr/bin/env python3
"""
Xbato Manga Downloader - Interactive Version with Multi-language Support
Downloads manga from Xbato (or its mirrors)
"""

import requests
import os
import re
import sys
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# ============================================================================
# SETTINGS - Change domain here if site moves
# ============================================================================
BASE_DOMAIN = "https://xbato.co.uk"  # Change to new domain if needed

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': BASE_DOMAIN + '/'
}

DELAY_BETWEEN_CHAPTERS = 2.0  # Delay between chapters (seconds)
DELAY_BETWEEN_IMAGES = 0.5    # Delay between images (seconds)

# ============================================================================
# TRANSLATIONS
# ============================================================================
TRANSLATIONS = {
    'en': {
        'banner_title': 'XBATO MANGA DOWNLOADER',
        'current_domain': 'Current domain',
        'select_language': 'Select language',
        'choice': 'Choice',
        'enter_data': 'Enter data for downloading manga:',
        'enter_url': 'Enter link to any manga chapter:',
        'example': 'Example',
        'url': 'URL',
        'empty_url': 'URL cannot be empty!',
        'invalid_url': 'Invalid URL format. Make sure it\'s a chapter link (contains \'/read/\').',
        'save_location': 'Where to save manga?',
        'current_folder': 'Current folder (subfolder with manga name will be created)',
        'custom_path': 'Specify custom path',
        'select_option': 'Select (1 or 2)',
        'enter_path': 'Enter full path to folder',
        'folder_not_exist': 'Folder \'{}\' does not exist. Create?',
        'create_failed': 'Failed to create folder',
        'path_empty': 'Path cannot be empty!',
        'invalid_choice': 'Invalid choice. Enter 1 or 2.',
        'starting': 'Starting processing',
        'getting_info': 'Getting manga information...',
        'manga': 'Manga',
        'chapters_found': 'Chapters found',
        'save_folder': 'Save folder',
        'confirm_download': 'Will download {} chapters. Continue? (y/n)',
        'cancelled': 'Download cancelled by user.',
        'starting_download': 'STARTING DOWNLOAD',
        'loading_chapter': 'Loading',
        'pages_found': 'Pages found',
        'failed_load': 'Failed to load chapter page. Skipping.',
        'no_pages': 'No pages in this chapter. Skipping.',
        'downloaded': 'Downloaded',
        'completed': 'Download of \'{}\' completed!',
        'files_saved': 'Files saved to',
        'success': 'Program completed successfully!',
        'error': 'Program completed with errors.',
        'interrupted': 'Download interrupted by user (Ctrl+C)',
        'critical_error': 'Critical error',
        'failed_detect': 'Failed to detect manga from link. Make sure the link is correct.',
        'no_chapters': 'No chapters found.',
    },
    'ru': {
        'banner_title': 'XBATO MANGA DOWNLOADER',
        'current_domain': 'Текущий домен',
        'select_language': 'Выберите язык',
        'choice': 'Выбор',
        'enter_data': 'Введите данные для скачивания манги:',
        'enter_url': 'Введите ссылку на любую главу манги:',
        'example': 'Пример',
        'url': 'URL',
        'empty_url': 'URL не может быть пустым!',
        'invalid_url': 'Неверный формат URL. Убедитесь, что это ссылка на главу (содержит \'/read/\').',
        'save_location': 'Куда сохранить мангу?',
        'current_folder': 'В текущую папку (будет создана подпапка с названием манги)',
        'custom_path': 'Указать свой путь',
        'select_option': 'Выберите (1 или 2)',
        'enter_path': 'Введите полный путь к папке',
        'folder_not_exist': 'Папка \'{}\' не существует. Создать?',
        'create_failed': 'Не удалось создать папку',
        'path_empty': 'Путь не может быть пустым!',
        'invalid_choice': 'Неверный выбор. Введите 1 или 2.',
        'starting': 'Начинаем обработку',
        'getting_info': 'Получаю информацию о манге...',
        'manga': 'Манга',
        'chapters_found': 'Найдено глав',
        'save_folder': 'Папка для сохранения',
        'confirm_download': 'Будет скачано {} глав. Продолжить? (y/n)',
        'cancelled': 'Загрузка отменена пользователем.',
        'starting_download': 'НАЧИНАЕМ ЗАГРУЗКУ',
        'loading_chapter': 'Загрузка',
        'pages_found': 'Найдено страниц',
        'failed_load': 'Не удалось загрузить страницу главы. Пропускаю.',
        'no_pages': 'В этой главе нет страниц. Пропускаю.',
        'downloaded': 'Скачано',
        'completed': 'Загрузка \'{}\' полностью завершена!',
        'files_saved': 'Файлы сохранены в',
        'success': 'Программа завершена успешно!',
        'error': 'Программа завершена с ошибками.',
        'interrupted': 'Загрузка прервана пользователем (Ctrl+C)',
        'critical_error': 'Критическая ошибка',
        'failed_detect': 'Не удалось определить мангу по ссылке. Убедитесь, что ссылка правильная.',
        'no_chapters': 'Не найдено ни одной главы.',
    }
}

# Global language setting
LANG = 'en'

def t(key):
    """Get translation for current language."""
    return TRANSLATIONS[LANG].get(key, key)

# ============================================================================
# FUNCTIONS
# ============================================================================

def select_language():
    """Let user select interface language."""
    global LANG
    print("=" * 70)
    print("  📚 XBATO MANGA DOWNLOADER 📚")
    print("=" * 70)
    print(f"  Current domain / Текущий домен: {BASE_DOMAIN}")
    print("=" * 70)
    print()
    print("🌐 Select language / Выберите язык:")
    print("   1. English")
    print("   2. Русский")
    print()

    while True:
        choice = input("   Choice / Выбор (1 or 2): ").strip()
        if choice == '1':
            LANG = 'en'
            break
        elif choice == '2':
            LANG = 'ru'
            break
        else:
            print("   ❌ Invalid choice / Неверный выбор. Enter / Введите 1 or 2.\n")

    print()

def print_banner():
    """Print welcome banner."""
    print("=" * 70)
    print(f"  📚 {t('banner_title')} 📚")
    print("=" * 70)
    print(f"  {t('current_domain')}: {BASE_DOMAIN}")
    print("=" * 70)
    print()

def sanitize_filename(name: str) -> str:
    """Clean string from characters not allowed in folder names."""
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

def get_series_slug_from_url(chapter_url: str) -> str:
    """
    Extract manga slug from URL.
    Example: from '.../read/too-many-losing-heroines/chapter-1' get 'too-many-losing-heroines'
    """
    parts = chapter_url.rstrip('/').split('/')
    if 'read' in parts:
        read_index = parts.index('read')
        if len(parts) > read_index + 1:
            return parts[read_index + 1]
    return None

def get_page_content(url: str) -> BeautifulSoup:
    """Get HTML content of page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"❌ Error loading page {url}: {e}")
        return None

def get_manga_title_from_page(soup: BeautifulSoup) -> str:
    """Extract manga title from HTML."""
    # Look in breadcrumb
    breadcrumb = soup.find('script', type='application/ld+json')
    if breadcrumb:
        try:
            import json
            data = json.loads(breadcrumb.string)
            if 'itemListElement' in data and len(data['itemListElement']) > 1:
                return data['itemListElement'][1]['name']
        except:
            pass

    # Alternative - from chapter title
    title_elem = soup.find('h1', class_='chapter-title')
    if title_elem:
        title_text = title_elem.text.strip()
        match = re.match(r'(.+?):\s*CHAPTER', title_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Unknown Manga"

def get_all_chapters_from_page(soup: BeautifulSoup, base_url: str) -> list:
    """Extract list of all chapters from dropdown menu."""
    chapters = []
    select = soup.find('select', id='chapter-dropdown')

    if not select:
        return chapters

    for option in select.find_all('option'):
        chapter_url = option.get('value', '').strip()
        chapter_name = option.text.strip()

        if chapter_url and chapter_url.startswith('http') and chapter_name != '-- Select Chapter --':
            chapters.append({
                'url': chapter_url,
                'name': chapter_name
            })

    # Reverse list so chapters go in order (1, 2, 3...)
    return list(reversed(chapters))

def get_chapter_images(soup: BeautifulSoup) -> list:
    """Extract URLs of all chapter images from HTML."""
    images = []

    # Find container with images
    container = soup.find('div', class_='chapter-images-container')
    if not container:
        return images

    # Find all img tags with data-src or src
    for img in container.find_all('img'):
        # Skip ad images
        if 'notice-img' in img.get('class', []):
            continue

        # Get image URL
        img_url = img.get('data-src') or img.get('src')

        if img_url and img_url.startswith('http'):
            images.append(img_url)

    return images

def download_file(url, filepath):
    """Download file and save to disk."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"   └─ ❌ Failed to download {os.path.basename(filepath)}: {e}")
        return False

def get_user_input():
    """Get data from user in interactive mode."""
    print(f"📝 {t('enter_data')}\n")

    # Get URL
    while True:
        chapter_url = input(f"🔗 {t('enter_url')}\n   {t('example')}: https://xbato.co.uk/read/too-many-losing-heroines/chapter-1\n   {t('url')}: ").strip()

        if not chapter_url:
            print(f"❌ {t('empty_url')}\n")
            continue

        if 'read/' not in chapter_url:
            print(f"❌ {t('invalid_url')}\n")
            continue

        break

    print()

    # Get save folder
    print(f"📁 {t('save_location')}")
    print(f"   1. {t('current_folder')}")
    print(f"   2. {t('custom_path')}")

    while True:
        choice = input(f"\n   {t('select_option')}: ").strip()

        if choice == '1':
            output_dir = None
            break
        elif choice == '2':
            output_dir = input(f"\n   {t('enter_path')}: ").strip()
            if output_dir:
                # Check if path exists
                if not os.path.exists(output_dir):
                    create = input(f"\n   ⚠️  {t('folder_not_exist').format(output_dir)} (y/n): ").strip().lower()
                    if create == 'y':
                        try:
                            os.makedirs(output_dir, exist_ok=True)
                            break
                        except Exception as e:
                            print(f"   ❌ {t('create_failed')}: {e}\n")
                            continue
                    else:
                        continue
                else:
                    break
            else:
                print(f"   ❌ {t('path_empty')}\n")
        else:
            print(f"   ❌ {t('invalid_choice')}\n")

    print()
    return chapter_url, output_dir

def download_manga(chapter_url: str, output_dir: str = None):
    """Main function for downloading entire manga."""
    print(f"\n🚀 {t('starting')}: {chapter_url}\n")

    series_slug = get_series_slug_from_url(chapter_url)

    if not series_slug:
        print(f"❌ {t('failed_detect')}")
        return False

    # 1. Load chapter page to get information
    print(f"🔍 {t('getting_info')}")
    soup = get_page_content(chapter_url)
    if not soup:
        return False

    # 2. Get manga title
    series_title = get_manga_title_from_page(soup)
    safe_title = sanitize_filename(series_title)
    print(f"✅ {t('manga')}: {series_title}")

    # 3. Get list of all chapters
    chapters = get_all_chapters_from_page(soup, BASE_DOMAIN)
    if not chapters:
        print(f"❌ {t('no_chapters')}")
        return False

    total_chapters = len(chapters)
    print(f"📚 {t('chapters_found')}: {total_chapters}\n")

    # Create root folder for manga
    if output_dir is None:
        output_dir = safe_title
    else:
        output_dir = os.path.join(output_dir, safe_title)

    os.makedirs(output_dir, exist_ok=True)
    print(f"💾 {t('save_folder')}: {os.path.abspath(output_dir)}\n")

    # Confirmation before starting download
    confirm = input(f"⚠️  {t('confirm_download').format(total_chapters)} ").strip().lower()
    if confirm != 'y':
        print(f"\n❌ {t('cancelled')}")
        return False

    print("\n" + "=" * 70)
    print(f"  🚀 {t('starting_download')}")
    print("=" * 70 + "\n")

    # 4. Download each chapter
    for idx, chapter in enumerate(chapters, 1):
        chapter_name = chapter['name']
        chapter_url = chapter['url']

        # Create safe folder name for chapter
        chapter_folder_name = sanitize_filename(chapter_name)
        chapter_folder = os.path.join(output_dir, chapter_folder_name)
        os.makedirs(chapter_folder, exist_ok=True)

        print(f"📖 [{idx}/{total_chapters}] {t('loading_chapter')} {chapter_name}...")

        # Load chapter page
        chapter_soup = get_page_content(chapter_url)
        if not chapter_soup:
            print(f"   └─ ⚠️ {t('failed_load')}\n")
            continue

        # Get image links
        image_urls = get_chapter_images(chapter_soup)

        if not image_urls:
            print(f"   └─ ⚠️ {t('no_pages')}\n")
            continue

        print(f"   └─ 🖼️  {t('pages_found')}: {len(image_urls)}")

        # Download all chapter images
        downloaded = 0
        for page_num, img_url in enumerate(image_urls, 1):
            # Determine file extension
            ext = os.path.splitext(urlparse(img_url).path)[1]
            if not ext or ext.lower() not in ['.jpg', '.jpeg', '.png', '.webp']:
                ext = '.webp'

            filename = f"{page_num:03d}{ext}"
            filepath = os.path.join(chapter_folder, filename)

            if os.path.exists(filepath):
                downloaded += 1
                continue

            success = download_file(img_url, filepath)
            if success:
                downloaded += 1
            time.sleep(DELAY_BETWEEN_IMAGES)

        print(f"   └─ ✅ {t('downloaded')}: {downloaded}/{len(image_urls)}\n")

        # Pause between chapters
        time.sleep(DELAY_BETWEEN_CHAPTERS)

    print("=" * 70)
    print(f"🎉 {t('completed').format(safe_title)}")
    print(f"📁 {t('files_saved')}: {os.path.abspath(output_dir)}")
    print("=" * 70)
    return True

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main program function."""
    # Check command line arguments
    if len(sys.argv) >= 2:
        # Command line mode - use English by default
        global LANG
        LANG = 'en'
        print_banner()
        chapter_url = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        # Interactive mode - select language first
        select_language()
        print_banner()
        chapter_url, output_dir = get_user_input()

    # Start download
    success = download_manga(chapter_url, output_dir)

    if success:
        print(f"\n✅ {t('success')}")
        sys.exit(0)
    else:
        print(f"\n❌ {t('error')}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n⚠️  {t('interrupted')}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ {t('critical_error')}: {e}")
        sys.exit(1)
