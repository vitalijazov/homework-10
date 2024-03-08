from readline import append_history_file
from unittest import result


phone_book={}
path='phones.txt'
SEPARATOR=';'

def open_phone_book():
    global phone_book
    with open(path,'r' encoding='UTF-8') as file:
    data=file.readlines()
    for u_id, contact in enumerate(data,1):
     phone_book[u_id]=contact.strip().split(SEPARATOR)

     def save_phone_book():
        global phone_book
        data=[]
        for contact in phone_book.values():
           data.append(SEPARATOR.join(contact))
           data='\n'.join(data)
           with open(path, 'w', encoding='UTF-8') as file:
              file.write(data)


     def _next_id():
        global phone_book
        if phone_book:
           return max(phone_book + 1) if phone_book else 1
       
     
     def add_new_contact(new_contact:list[str]):
        global phone_book
        phone_book[_next_id()]=new_contact


def find_contact(search_word):
   global phone_book
   for u_id, contact in phone_book .items():
     if search_word.lower() in ' '.join(contact).lower():
        result[u_id]=contact
        return result
     

     def edit_contact(u_id: int,edited_contact: list[str]):
        global phone_book
        current_contact=phone_book[u_id]
        for i in range(len(current_contact)):
           current_contact[i]=edited_contact[i] if edit_contact[i] else current_contact[i]
           phone_book[u_id] = current_contact
           return current_contact[0]
     
def delete_contact(u_id):
   global phone_book
   return phone_book.pop(u_id)[0]















     