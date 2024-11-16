import telebot
import time
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import win32clipboard
from io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

# Инициализация bot для работы с telegram api
token = '7855556970:AAH_ZswZdR0qYwp2f8-TERJDp-HugVzKHMQ'
bot=telebot.TeleBot(token)

# Инициализация driver для работы с браузером
options = webdriver.ChromeOptions()

# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://playerok.com")

# Переменные
userData = {}
description = "👾Для приобритения вам понадобится прислать мне ваш ник / либо же отправить мне запрос в Fortnite  (второе предпочтительней) (МОЙ НИК: kxrtik06, kxrtik07,  kxrtik08) \n👾После добавления в друзья нужно будет подождать 2 дня (дефолтный трейд бан)👾 \n👾В-баксы не поступают на баланс аккаунта, не выдаются кодом, не начисляются на аккаунт, дарится предмет/скин/эмоция/ что-либо из магазина предметов на ту сумму, которую вы купили (это очень важно)👾 \n👾Возврат по причине случайная покупка/отказ от покупки/ не знал, что это подарком/ любая другая причина - возврат не производится👾"
comment = "Привет, спасибо за покупку🤗. Кинь запрос в друзья на эти аккаунты: kxrtik06, kxrtik07, kxrtik08 (обязательно на все)👾."

# Классы
class Advertisement:
  def __init__(self, photo_path, title, description, price, sale, comment):
      self.photo_path = photo_path
      self.title = title
      self.description = description
      self.price = price
      self.sale = sale
      self.comment = comment

# Обьекты
advertisement_500 = Advertisement("images/vb500.png", "👾500 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 250, 231, comment)
advertisement_800 = Advertisement("images/vb800.png", "👾800 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 450, 370, comment)
advertisement_1200 = Advertisement("images/vb1200.png", "👾1200 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 650, 555, comment)
advertisement_1500 = Advertisement("images/vb1500.png", "👾1500 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 750, 693, comment)
advertisement_2000 = Advertisement("images/vb2000.png", "👾2000 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 1000, 924, comment)
advertisement_3000 = Advertisement("images/vb3000.png", "👾3000 VB ПОДАРКОМ👾 Быстро и Надёжно👾", description, 1500, 1386, comment)

# Функции
def copy_image_to_clipboard(advertisment):
  image = Image.open(advertisment.photo_path)
  output = BytesIO()
  image.convert('RGB').save(output, 'BMP')
  data = output.getvalue()[14:]
  output.close()

  win32clipboard.OpenClipboard()
  win32clipboard.EmptyClipboard()
  win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
  win32clipboard.CloseClipboard()

def next_step(message):
  try:
    element_next_button = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "button.MuiBox-root.mui-style-16ty3xs"))
    )
    element_next_button.click()
  except:
    bot.send_message(message.chat.id, 'Не удалось перейти к следующему этапу 🚫')

def post_advertisment(message, number_count_vb_btn, advertisment):
  driver.get("https://playerok.com/sell")
  time.sleep(3)
  if driver.current_url == "https://playerok.com/sell":
    # Выбор игры
    try:
      element_fortnite_button = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MuiBox-root.mui-style-16442oc"))
      )
      element_fortnite_button[3].click()
    except:
      bot.send_message(message.chat.id, 'Не удалось выбрать игру 🚫')
    # Выбор категории товара
    try:
      element_gifts_button = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MuiBox-root.mui-style-14n99w1"))
      )
      element_gifts_button[3].click()
    except:
      bot.send_message(message.chat.id, 'Не удалось выбрать категорию 🚫')
    # Выбор кол-ства товара
    try:
      element_count_vb_button = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MuiBox-root.mui-style-1p30snl"))
      )
      element_count_vb_button[number_count_vb_btn].click()
    except:
      bot.send_message(message.chat.id, 'Не удалось выбрать кол-ство товара 🚫')
    # Переход на следуйщий этап
    next_step(message)
    # Вставка изоображения
    try:
      copy_image_to_clipboard(advertisment)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, 'Не удалось вставить изображение🚫')
    # Переход на следуйщий этап
    next_step(message)
    # Вставка заголовка обьявления
    try:
      pyperclip.copy(advertisment.title)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, "Не удалось вставить заголовок 🚫")
    # Переход на следуйщий этап
    next_step(message)
    # Вставка описания
    try:
      pyperclip.copy(advertisment.description)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, "Не удалось вставить описание 🚫")
    # Переход на следуйщий этап
    next_step(message)
    # Вставка цены
    try:
      pyperclip.copy(advertisment.price)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, "Не удалось указать цену 🚫")
    # Переход на следуйщий этап
    next_step(message)
    # Вставка комментария
    try:
      element_text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
      )
      element_text_area.click()
      pyperclip.copy(advertisment.comment)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, "Не удалось вставить комментарий 🚫")
    # Переход на следуйщий этап
    try:
      element_next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.MuiBox-root.mui-style-o1d96g"))
      )
      element_next_button.click()
    except:
      bot.send_message(message.chat.id, 'Не удалось перейти к следующему этапу 🚫')
    # Открытие редакитирование обьявления
    try:
      element_edit_ad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.MuiBox-root.mui-style-4g6ai3"))
      )
      element_edit_ad.click()
    except:
      bot.send_message(message.chat.id, 'Не удалось открыть обьявление 🚫')
    # Вставка скидочной цены
    try:
      element_sale_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.MuiBox-root.mui-style-awfqns"))
      )
      element_sale_price.click()
      pyperclip.copy(advertisment.sale)
      actions = ActionChains(driver)
      actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    except:
      bot.send_message(message.chat.id, 'Не удалось установить скидочную цену 🚫')
    # Переход на следуйщий этап
    next_step(message)
    # Публикация обьявления
    try:
      element_publish_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.MuiBox-root.mui-style-o1d96g'))
      )
      element_publish_btn.click()
      bot.send_message(message.chat.id, 'Обьявление опубликовано ✅')
    except:
      bot.send_message(message.chat.id, 'Не удалось опубликовать обьявление 🚫')
  else:
    bot.send_message(message.chat.id, "Не удалось перейти на страницу: https://playerok.com/sell 🚫")

# Декораторы
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️")

@bot.message_handler(commands=['login'])
def login(message):
  bot.send_message(message.chat.id, "Укажите свою почту")
  try:
    driver.get("https://playerok.com/profile/auth")
  except:
    bot.send_message(message.chat.id, 'Не удалось открыть страницу входа 🚫')
  bot.register_next_step_handler(message, set_login)
  
def set_login(message):
  userData['email'] = message.text
  bot.send_message(message.chat.id, f"Ваша почта: {userData['email']}")
  try:
    element_email_input = driver.find_element(By.NAME, 'email')
    element_email_input.send_keys(userData['email'])
    element_email_input.submit()
  except:
    bot.send_message(message.chat.id, 'Не удалось вписать email 🚫')
  bot.send_message(message.chat.id, 'Введите полученый код')
  bot.register_next_step_handler(message, set_verification_code)

def set_verification_code(message):
  try:
    element_code_input = driver.find_element(By.CSS_SELECTOR, "div.react-code-input input")
    element_code_input.send_keys(message.text)

    bot.send_message(message.chat.id, f'Проверка 🔄')
    time.sleep(5)
    if driver.current_url == "https://playerok.com/profile/auth":
        bot.send_message(message.chat.id, 'Неверный код 🚫')
        bot.register_next_step_handler(message, login)
    else:
      bot.send_message(message.chat.id, f'Вход выполнен успешно ✅')
  except:
    bot.send_message(message.chat.id, 'Не удалось вписать код 🚫')
  
@bot.message_handler(commands=['500'])
def start(message):
  post_advertisment(message, 1, advertisement_500)

@bot.message_handler(commands=['800'])
def start(message):
  post_advertisment(message, 1, advertisement_800)

@bot.message_handler(commands=['1200'])
def start(message):
  post_advertisment(message, 2, advertisement_1200)

@bot.message_handler(commands=['1500'])
def start(message):
  post_advertisment(message, 3, advertisement_1500)

@bot.message_handler(commands=['2000'])
def start(message):
  post_advertisment(message, 4, advertisement_2000)

@bot.message_handler(commands=['3000'])
def start(message):
  post_advertisment(message, 5, advertisement_3000)

bot.polling()