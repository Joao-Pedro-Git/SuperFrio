# obter_elementos.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def pegar_elementos(driver):
    """
    Função para pegar elementos de uma página usando XPath.
    Aqui você pode modificar os XPaths de acordo com os elementos da página que deseja pegar.
    """
    try:
        # Exemplo de como pegar o primeiro link da página
        primeiro_link = driver.find_element(By.XPATH, "(//a)[1]")
        print("Primeiro Link:", primeiro_link.text)
        
        # Exemplo de pegar um campo de busca
        search_box = driver.find_element(By.XPATH, "//input[@name='q']")
        print("Campo de Busca Encontrado:", search_box)

        # Exemplo de pegar todos os links
        links = driver.find_elements(By.XPATH, "//a")
        print(f"Total de Links encontrados: {len(links)}")

        # Interagir com algum elemento (exemplo: clicar no primeiro link)
        primeiro_link.click()
        time.sleep(2)

    except Exception as e:
        print("Erro ao pegar os elementos:", e)
