import random

greetings = []
intros = []
links = []
expectations = []

greetings.append("Hello. ")
greetings.append("Yo, what's up. ")

intros.append("My name is Yujian Tang. ")
intros.append("It's ya boi Ra. ")

links.append("You may know me from Super Simple Python. ")
links.append("I'm the owner of the Social Techies Discord server. ")
links.append("You may have seen my articles on Medium. ")

expectations.append("I'm going to teach you how to become a software engineer.")
expectations.append("I create the best software content in the world.")
expectations.append("I will show you how to actually learn engineering skills.")
expectations.append("If you want to truly learn Python in a useable manner, you should follow me.")

full_greeting = random.choice(greetings) + random.choice(intros) + random.choice(links) + random.choice(expectations)

print(full_greeting)