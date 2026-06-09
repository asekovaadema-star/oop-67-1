class Contact:
    def __init__(self, name, phone):
        self.name = name 
        self.phone = phone 
    
    @classmethod
    def validate_phone_number(cls, phone):
        if len(phone) == 10:
            return True
        return False

class ContactList:
    all_contacts = []

    @classmethod
    def add_contacts(cls, name, phone):
        if Contact.validate_phone_number(phone):
            new_contact = Contact(name, phone)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError('Номер телефона должен содержать ровно 10 цифр')

        
print(ContactList.all_contacts)

ContactList.add_contacts("Анджелина Джоли", "0707691467")
ContactList.add_contacts("Kale Henituse", "0999505050")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)
ContactList.add_contacts("Miku", "666666")