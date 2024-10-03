import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Инициализация драйвера
driver = webdriver.Firefox()

def search_on_wikipedia(query):
    # Поиск в Википедии
    driver.get('https://www.wikipedia.org/')
    search_box = driver.find_element(By.NAME, 'search')
    search_box.send_keys(query + Keys.RETURN)
    time.sleep(2) # небольшая задержка для загрузки страницы

def list_paragraphs():
    # Получение параграфов статьи
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    for i, paragraph in enumerate(paragraphs):
        print(f'--- Параграф {i+1} ---')
        print(paragraph.text)
        print()
    input("Нажмите Enter, чтобы продолжить...")

def get_related_links():
    # Получение связанных ссылок из статьи
    links = driver.find_elements(By.CSS_SELECTOR, 'p a[href]')
    return links

def related_links_action(links):
    while True:
        print("\nСвязанные страницы:")
        for i, link in enumerate(links):
            print(f"{i + 1}: {link.text}")
        print("0: Вернуться к предыдущему меню")

        choice = input("Выберите номер страницы (или 0 для выхода): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(links):
                links[choice - 1].click()
                time.sleep(2)  # небольшая задержка для загрузки страницы
                manage_article()
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

def manage_article():
    while True:
        print("\nЧто вы хотите сделать?")
        print("1: Листать параграфы статьи")
        print("2: Перейти на одну из связанных страниц")
        print("0: Выйти")

        choice = input("Введите номер действия: ")
        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            links = get_related_links()
            related_links_action(links)
        elif choice == '0':
            print("Выход из программы.")
            driver.quit()
            exit()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

def main():
    initial_query = input("Введите запрос для поиска на Википедии: ")
    search_on_wikipedia(initial_query)
    manage_article()

if __name__ == "__main__":
    main()



