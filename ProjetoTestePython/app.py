import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores')
#//h2[@class="MuiTypography-root jss350 jss351 MuiTypography-h6"]
titulos= driver.find_elements(By.XPATH,"//a[@class='nome-produto']")
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")
workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
shet_produtos = workbook['produtos']
shet_produtos['A1'].value = 'Produto'
shet_produtos['b1'].value = 'Preço'

for titulos,precos in zip (titulos, precos):
    shet_produtos.append([titulos.text,precos.text])
    

workbook.save('produtos.xlsx')
