def sent_email(messages, recipient, sender = "university.help@gmail.com" ):
   if "@" not in recipient or "@"not in sender \
           or not recipient.endswith((".com",".ru",".net"))or not sender.endswith ((".com",".ru",".net")):
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
   elif recipient == sender :
       print("Нельзя отправить письмо самому себе")
   elif sender !="university.help@gmail.com":
       print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на aдрес {recipient}.")
   else:
       print("Письмо успешно отправлено с адреса sender на адрес recipient.")



