print("Hooman Amiri     4005193006     computer science")

contacts = []

def add_contact():
    first_name = input("نام: ")
    last_name = input("نام خانوادگی: ")
    mobile_number = input("شماره موبایل: ")
    home_number = input("شماره تلفن محل سکونت: ")
    address = input("آدرس محل سکونت: ")
    national_code = input("کد ملی: ")
    email = input("آدرس ایمیل: ")

    contact = {
        'نام': first_name,              
        'نام خانوادگی': last_name,              
        'شماره موبایل': mobile_number,              
        'شماره تلفن محل سکونت': home_number,              
        'آدرس محل سکونت': address,              
        'کد ملی':  national_code,              
        'آدرس ایمیل':  email               
              }

    contacts.append(contact)
    print("مخاطب با موفقیت اضافه شد!")

def search_contact():
    search_option = input("قابلیت جستجو را انتخاب کنید:\n1. براساس نام خانوادگی\n2. براساس شماره تلفن\nانتخاب خود را وارد کنید: ")

    if search_option == '1':
        last_name = input("نام خانوادگی مخاطب را وارد کنید: ")
        
        found_contacts = []
        for contact in contacts:
            if contact['نام خانوادگی'] == last_name:
                found_contacts.append(contact)

        if found_contacts:
            print("مخاطبان یافت شده:")
            for contact in found_contacts:
                print_contact(contact)
        else:
            print("هیچ مخاطبی با این نام خانوادگی یافت نشد.")

    elif search_option == '2':
        phone_number = input("شماره تلفن مخاطب را وارد کنید: ")
        
        found_contacts = []
        for contact in contacts:
            if contact['شماره تلفن محل سکونت'] == phone_number:
                found_contacts.append(contact)

        if found_contacts:
            print("مخاطبان یافت شده:")
            for contact in found_contacts:
                print_contact(contact)
        else:
            print("هیچ مخاطبی با این شماره تلفن یافت نشد.")

    else:
        print("انتخاب نامعتبر!")

def delete_contact():
    last_name = input("نام خانوادگی مخاطب را وارد کنید: ")
    
    deleted_contacts = []
    for contact in contacts:
        if contact['نام خانوادگی'] == last_name:
            contacts.remove(contact)
            deleted_contacts.append(contact)

    if deleted_contacts:
        print("مخاطبان حذف شده:")
        for contact in deleted_contacts:
            print_contact(contact)
    else:
        print("هیچ مخاطبی با این نام خانوادگی یافت نشد.")

def edit_contact():
    last_name = input("نام خانوادگی مخاطب را وارد کنید: ")
    
    edited_contacts = []
    for contact in contacts:
        if contact['نام خانوادگی'] == last_name:
            print("اطلاعات قبلی:")
            print_contact(contact)

            first_name = input("نام جدید: ")
            mobile_number = input("شماره موبایل جدید: ")
            home_number = input("شماره تلفن محل سکونت جدید: ")
            address = input("آدرس محل سکونت جدید: ")
            national_code = input("کد ملی جدید: ")
            email = input("آدرس ایمیل جدید: ")

            contact['نام'] = first_name
            contact['شماره موبایل'] = mobile_number
            contact['شماره تلفن محل سکونت'] = home_number
            contact['آدرس محل سکونت'] = address
            contact['کد ملی'] = national_code
            contact['آدرس ایمیل'] = email

            edited_contacts.append(contact)

    if edited_contacts:
        print("مخاطبان ویرایش شده:")
        for contact in edited_contacts:
            print_contact(contact)
    else:
        print("هیچ مخاطبی با این نام خانوادگی یافت نشد.")

def report_phone_numbers():
    print("شماره مخاطبان:")

    for contact in contacts:
        print(contact['نام'])
        print(contact['شماره موبایل'])
        print("\n")
def report_addresses():
    
    print("آدرس مخاطبان:")

    for contact in contacts:
        print(contact['نام'])
        print(contact['آدرس محل سکونت'])
        print("\n")

def report_emails():
    print("آدرس ایمیل مخاطبان:")

    for contact in contacts:
        print(contact['نام'])
        print(contact['آدرس ایمیل'])
        print("\n")

def print_contact(contact):
    print("نام: " + contact['نام'])
    print("نام خانوادگی: " + contact['نام خانوادگی'])
    print("شماره موبایل: " + contact['شماره موبایل'])
    print("شماره تلفن محل سکونت: " + contact['شماره تلفن محل سکونت'])
    print("آدرس محل سکونت: " + contact['آدرس محل سکونت'])
    print("کد ملی: " + contact['کد ملی'])
    print("آدرس ایمیل: " + contact['آدرس ایمیل'])


def main():
    while True:
        print("منوی انتخاب:")
        print("1. اضافه کردن مخاطب")
        print("2. جستجوی مخاطب بر اساس نام خانوادگی یا شماره تلفن")
        print("3. حذف مخاطب بر اساس نام خانوادگی")
        print("4. ویرایش مخاطب بر اساس نام خانوادگی")
        print("5. گزارش شماره مخاطبان")
        print("6. گزارش آدرس مخاطبان")
        print("7. گزارش آدرس ایمیل مخاطبان")
        print("8. خروج از برنامه")

        choice = input("\nانتخاب خود را وارد کنید: \n")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            report_phone_numbers()
        elif choice == '6':
            report_addresses()
        elif choice == '7':
            report_emails()
        elif choice == '8':
            break
        else:
            print("Error!")

if __name__ == '__main__':
    main()