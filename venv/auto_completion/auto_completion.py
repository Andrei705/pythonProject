from pyperclip import paste
from openpyxl import load_workbook
from re import split


text = paste()

text = split(r'[\b\t]', text)

wb = load_workbook('1.xlsx')
ws = wb.active
ws.tile = 'Проверка'
ws['C10'] = text[5]
ws['C11'] = text[0]
ws['C12'] = text[1]
ws['C13'] = text[2]
ws['C14'] = text[4]
ws['C15'] = text[6]
ws['C17'] = text[11]
ws['C18'] = text[15]
ws['C19'] = text[17]
ws['D23'] = text[21]
ws['E23'] = "Да"
ws['E25'] = "Да"
ws['E26'] = "Да"
ws['E27'] = "Да"
ws['E34'] = "Да"
ws['E35'] = "Да"
ws['E36'] = "Да"
ws['E37'] = "Да"
ws['E38'] = "Да"
ws['E39'] = "Да"
wb = wb.save('{}.xlsx'.format(text[5]))

