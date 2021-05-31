from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        self.mensagem = " Bom dia, tenha uma otima semana "
        self.grupos = ["grupoLoja"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def EnviarMensagens(self):
        # <span dir="auto" title="grupoLoja" class="_35k-1 _1adfa _3-8er">grupoLoja</span>
        # <div tabindex="-1" class="_1JAUF _2x4bz">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(25)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath("//span[@title='grupoLoja']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_2x4bz')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()

bot = whatsappBot()
bot.EnviarMensagens()
