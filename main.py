

#HELLO ITP - THIS IS MY FINAL TEST.

#ABEL AGUNDIZ RAMIREZ - FULL STACK DEVELOPER PYTHON/FLUTTER.


# Define the Contact and Lead classes
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Function to update or add new registrants
def add_or_update_contacts(contacts, leads, registrants):
    for reg in registrants:
        reg_name = reg["name"]
        reg_email = reg["email"]
        reg_phone = reg["phone"]
        
        # 1) Try to match registrant's email to contacts
        matched = False
        for contact in contacts:
            if reg_email and contact.email == reg_email:
                if contact.phone is None:
                    contact.phone = reg_phone
                if contact.name is None:
                    contact.name = reg_name
                matched = True
                break
        
        # 2) If not matched, try to match registrant's phone to contacts
        if not matched:
            for contact in contacts:
                if reg_phone and contact.phone == reg_phone:
                    if contact.email is None:
                        contact.email = reg_email
                    if contact.name is None:
                        contact.name = reg_name
                    matched = True
                    break
        
        # 3 & 4) If not matched, try to match email or phone in leads
        if not matched:
            for lead in leads:
                if reg_email and lead.email == reg_email:
                    contacts.append(Contact(reg_name if reg_name else lead.name, reg_email, reg_phone))
                    leads.remove(lead)
                    matched = True
                    break
            if not matched:
                for lead in leads:
                    if reg_phone and lead.phone == reg_phone:
                        contacts.append(Contact(reg_name if reg_name else lead.name, reg_email, reg_phone))
                        leads.remove(lead)
                        matched = True
                        break
        
        # 5) If not matched, add to contacts
        if not matched:
            contacts.append(Contact(reg_name, reg_email, reg_phone))

# Initial Contacts and Leads
contacts = [
    Contact("Alice Brown", None, "1231112223"),
    Contact("Bob Crown", "bob@crowns.com", None),
    Contact("Carlos Drew", "carl@drewess.com", "3453334445"),
    Contact("Doug Emerty", None, "4564445556"),
    Contact("Egan Fair", "eg@fairness.com", "5675556667")
]

leads = [
    Lead(None, "kevin@keith.com", None),
    Lead("Lucy", "lucy@liu.com", "3210001112"),
    Lead("Mary Middle", "mary@middle.com", "3331112223"),
    Lead(None, None, "4442223334"),
    Lead(None, "ole@olson.com", None)
]

# Registrants
registrants = [
    {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": None},
    {"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"},
    {"name": "Uma Thurman", "email": "uma@thurs.com", "phone": None}
]

# Process registrants
add_or_update_contacts(contacts, leads, registrants)

# Print final contacts
print("Final Contacts:")
for contact in contacts:
    print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

# Print remaining leads
print("\nRemaining Leads:")
for lead in leads:
    print(f"Name: {lead.name}, Email: {lead.email}, Phone: {lead.phone}")
