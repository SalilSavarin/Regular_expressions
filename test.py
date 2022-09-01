import re
import csv
from pprint import pprint



pattern_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone = r'+7(\2)\3\4\5 \6 \7'

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def update_list(contacts_list:list) ->list:
    new_list = list()
    for user_inf in contacts_list:
        full_name = ' '.join(user_inf[:3]).split(' ')
        user_list = [full_name[0], full_name[1], full_name[2], user_inf[3], user_inf[4],
                  re.sub(pattern_phone, sub_phone, user_inf[5]),user_inf[6]]
        new_list.append(user_list)
    return new_list

new_contact = update_list(contacts_list)
        
def removes_repetitions(users_inf_list:list) -> list:
    final_list = list()
    for user_inf in users_inf_list:
        firstname = user_inf[0]
        lastname = user_inf[1]
        for new_contact in users_inf_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if firstname == new_first_name and lastname == new_last_name:
                if user_inf[2] == "": 
                    user_inf[2] = new_contact[2]
                if user_inf[3] == "": 
                    user_inf[3] = new_contact[3]
                if user_inf[4] == "": 
                    user_inf[4] = new_contact[4]
                if user_inf[5] == "": 
                    user_inf[5] = new_contact[5]
                if user_inf[6] == "": 
                    user_inf[6] = new_contact[6]
    for x in users_inf_list:
        if x not in final_list:
            final_list.append(x)
    return final_list

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(removes_repetitions(update_list(contacts_list)))
