import smtplib
from dotenv import load_dotenv
import os


load_dotenv('pass.env')
my_name = 'Алексей'
friend_name = 'Василий'
website = 'https://dvmn.org/referrals/2ZZypO6FEbdN693QUfJpA28yctjg6XIwnLdMYNzg/'

email_from = 'episodeboli@yandex.ru'
email_to= 'frojiteira@yandex.ru'
subject = 'Приглашение!'


letter = '''From: {email_from}
To: {email_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(email_from=email_from,email_to=email_to,subject=subject)
login = os.environ['LOGIN']
password = os.environ['PASSWORD']
letter = letter.replace('%website%', website)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%my_name%', my_name)
encoded_letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, encoded_letter)
server.quit()

