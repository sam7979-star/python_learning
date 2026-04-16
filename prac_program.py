def replaceMonth(inList):
    monthMap = {
        1:"Jan", 2:"Feb",3:"Mar",4:"Apr",
        5:"May",6:"June", 7:"Jul", 8:"Aug",
        9:"Sep",10:"Oct",11:"Nov",12:"Dec"
    }

    for i in range(len(inList)):
        parts = inList[i].split("-")
        inList[i] = parts[0] + "-" + monthMap[int(parts[1])] + "-"+parts[2]
    return inList

lst_dates = ['01-01-2024','21-03-2024','11-08-2024','12-12-2024']
print(replaceMonth(lst_dates))

