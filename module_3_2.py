def send_email(message, recipient, sender = "university.help@gmail.com"):
    symbol = '@'
    end_email = ('.com', '.net', '.ru')
    if recipient == sender:
        print('Нельзя отправить письмо самому себе')
        return
    if recipient.endswith(end_email) and sender.endswith(end_email) and symbol in recipient and symbol in sender:
        if sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        if sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



send_email("привет", 'university.@gmail.com')