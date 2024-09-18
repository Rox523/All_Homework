def send_email(message, recipient, *, sender="university.help@gmail.com"):
  def is_valid_email(email):
      return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

  if not is_valid_email(sender) or not is_valid_email(recipient):
      print("Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
      return
  if sender == recipient:
      print('Нельзя отправить сообщение самому себе')
      return
  if sender == 'university.help@gmail.com':
      print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
  else:
      print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




