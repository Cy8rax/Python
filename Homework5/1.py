# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = 'фыыфвфыфрваамвб  абв оывпаып ылыабввра ывр  ыввлораывьтлмьбиры лыарпюблрыпв лрвывбла ыа неаы сы ыгнпмокуу ив сыовлоир'

lst_text = text.split()

for i in reversed(range(len(lst_text))):
    if ("а" in lst_text[i]) and ("б" in lst_text[i]) and ("в" in lst_text[i]):
        del lst_text[i]

print(' '.join(lst_text))