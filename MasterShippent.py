# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import tkinter as tk
from tkinter import simpledialog, messagebox
from ElementsJDA import pegar_elementos  

def obter_mastershippent():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    while True:
        try:
            mastershippent = simpledialog.askstring("Solicite a MS", "Digite a MS aqui:")
            if mastershippent is None:
                return None  # Caso o usuário cancele o input

            if len(mastershippent) == 10 and mastershippent.isdigit():
                return mastershippent
            else:
                raise ValueError("O valor deve ser numérico e ter exatamente 10 dígitos.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

def abrir_navegador(mastershippent):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    sleep(2)
    
    # Encontrar o campo de pesquisa do Google
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(mastershippent)  # Digita o valor da MS no campo de busca
    search_box.submit()  # Submete o formulário de pesquisa
    
    sleep(3)  # Aguarda alguns segundos para visualizar a pesquisa
    
    # Agora que a página foi carregada, podemos chamar a função do outro arquivo
    pegar_elementos(driver)  # Função que interage com a página e pega os elementos

    sleep(3)  # Aguarda para visualizar interações
    
    driver.quit()

def main():
    mastershippent = obter_mastershippent()
    if mastershippent is None:
        print("Operação cancelada pelo usuário.")
    else:
        print("Valor de Mastershippent:", mastershippent)
        abrir_navegador(mastershippent)

if __name__ == "__main__":
    main()
