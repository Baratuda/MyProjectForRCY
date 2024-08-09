romanNumbers = {0:'I',1:'II', 2:'III', 3:'IV', 4:'V', 5:'VI', 6:'VII', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
rictangles = {
    '45':[1,30,5,3,29,36,21,14,15],
    '67':[5,15,36,29],
    '34':[21,14,30,5],
}   


# Нужно переписать с учетом данных из журнала ЦОУ
def getNotСombatVehicles():
    return { 
                '7643 АС-7':['#76d43e','Дежурство'],	
                '9945 АС-7':['#fdf401','Другие загорания'],	
                '3463 АК-7':['#ff7601','Занятия'],	
                '4567АВ-7': ['#ffffff','Заправка'], 	
                '3890 АН-7':['#bf51c4','Ликвидация жалоносных'],		
                '8904 ВК-7':['#07f583','Ложный'],	
                '2456 АН-7':['#8bfe47','Платные услуги'], 
                '6733 РН-7':['#fe2400','Пожар'],	
                '4564АВ-7':['#fdf401' , 'Другие загорания'],	
                '6575 ПН-7':['#01ffe7','Помощь населению'],
                '1249 АС-7':['#fe2400','Пожар'],}

def test(list1, list2=None):
    truks = {}
    if list2:
        result = { i:{} for i in list2}   
    else:    
        result = { i.fireDepartment_id:{} for i in list1}
    for i in list1:
        if i.main_truk_id:
            if truks.get(i.main_truk_id):
                truks[i.main_truk_id].append(i)
                continue
            else:
                truks[i.main_truk_id] = [i]
                continue
        if not truks.get(i.licensePlate):
            truks[i.licensePlate] = [i]
            continue   
        else:
            truks[i.licensePlate].append(i)
            continue  
    for i in list1:
        x = 0
        if result[i.fireDepartment_id].get('Ремонт') and result[i.fireDepartment_id].get('Резерв'): x=2
        elif result[i.fireDepartment_id].get('Ремонт'): x=1
        elif result[i.fireDepartment_id].get('Резерв'): x=1
        number = len(result[i.fireDepartment_id])-x 
        if truks.get(i.licensePlate):
            if truks[i.licensePlate][0].status == 'COM':
                result[i.fireDepartment_id][romanNumbers[number]] = truks[i.licensePlate]
                continue
            elif truks[i.licensePlate][0].status == 'REP':
                result[i.fireDepartment_id]['Ремонт'] = truks[i.licensePlate] 
                continue
            else:
                result[i.fireDepartment_id]['Резерв'] = truks[i.licensePlate]
                continue 

    return result
           


def get_firetruks(list, list2=None):
    result = {}
    if list2: 
        truks = test(list2)
        for fireTruk, district in list:
            if result.get(district.districtDepartmentName):
                result[district.districtDepartmentName][fireTruk.fireDepartment_id] = truks[fireTruk.fireDepartment_id]
            else:
                result[district.districtDepartmentName]={fireTruk.fireDepartment_id : truks[fireTruk.fireDepartment_id]}    
    else:  
        for fireTruk, district in list:
            if result.get(district.districtDepartmentName):
                result[district.districtDepartmentName][fireTruk.fireDepartment_id] = [fireTruk,]
            else:
                result[district.districtDepartmentName]={fireTruk.fireDepartment_id : [fireTruk,]}                
    return result 