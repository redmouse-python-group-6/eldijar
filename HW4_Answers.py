# -- coding: utf-8 --
import random

while True:
	answers=["Ну конечно","Вероятно","Если сегодня пятница то Да",
		"Да, а хотя Нет!","98% вероятность или .98%",
		"Да это невозможно","НЕЕТ!!","Если Да то что?","Да, хороший вопрос"]

	quest=input("Ваш вопрос, только те вопросы где нужны ответы Да или Нет,\n оставьте пустым чтобы выйти:\n")

	if quest=="":
		break
	print(quest,"-",random.choice(answers))