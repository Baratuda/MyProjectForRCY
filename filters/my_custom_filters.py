def dificult_length_calculator(dict):
    result = 0
    result_dict = {}
    if  isinstance(dict, type({}.values())):
       for j in dict:
           result= result+len(j.values())
    else:
        result = 0 
        for j in dict.values():
            if isinstance(j, type({})):
                result_dict = j
                while True:
                    if type(next(iter(result_dict))) is list:
                        for i in result_dict:
                            result+=len(i)
                        break
                    result_dict = j.values() 
            if type(j) is list:
                result+=len(j)  
            
                 
    return result 


def sort_firedepartments(list_firedepartments, main_firedepartments):
    main_firedepartment = {}
    for i,j in list_firedepartments.items():
        if i in main_firedepartments: 
            main_firedepartment = {i:j}
            del list_firedepartments[i]
            break
    return dict(list(main_firedepartment.items()) + list(list_firedepartments.items()))    

romanNumber = {0:'I',1:'II', 2:'III', 3:'IV', 4:'V', 5:'VI', 6:'VII', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
def sort_number_of_firetrukset(list_firedepartments):
    if list_firedepartments.get('Резерв'):    
        res = list_firedepartments.get('Резерв')
        del list_firedepartments['Резерв']
        list_firedepartments['Резерв'] = res
    if list_firedepartments.get('Ремонт'):
        rep = list_firedepartments.get('Ремонт')
        del list_firedepartments['Ремонт']
        list_firedepartments['Ремонт'] = rep
    return list_firedepartments


def noCombatTruksmarker(truks,notСombatVehicles):
    for i in truks:
        if i.licensePlate in notСombatVehicles:
            return notСombatVehicles[i.licensePlate][0]
    return 'green'