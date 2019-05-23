'''
This code was written in the second semester of my second year of Computer Applications in DCU.
The task was to demostrate threading using the well known barbershop problem as an example.
'''

#
# Please use python 3 to execute this code
#


import time
import os
import random
import queue
from threading import Thread


custs = ["Adriana", "Andreas", "Ange", "Anna", "Arya", "Bean",
		 "Betty", "Brian", "Carmela", "Caro", "Celine", "Clemence",
		 "Cormac", "Corrado", "Danny", "Dermot", "Elsa", "Eminem",
		 "Evelina", "Florence", "Frank", "Garwood", "Gary", "Gaspard",
		 "Hugh", "Hugo", "Ingrid", "Jane", "Janice", "Jonathan",
		 "Kamel", "Kevin", "Livia", "Louis", "Lynell", "Margery",
		 "Mark", "Mary", "Meadow", "Medhi", "Michele", "Nakia",
		 "Patricia", "Paul", "Pierre", "Raychel", "Ricky", "Riona",
		 "Simone", "Steffi", "Stu", "Theo", "Thomas", "Tiffany",
		 "Timmy", "Tony", "Trudy", "Vito", "Wendy", "Yoan"]

barbs = ["Bobbi", "Casey", "Chris", "Drew", "Eddie", "Frankie", "Georgie",
		 "Jesse", "Jo", "Jules", "Nicky", "Remy", "River", "Riley", "Val"]


# HERE ARE THE VARIABLES THAT YOU CAN CHANGE TO EASILY ALTER THE PROGRAM:

barbers_on_duty = 3 # you can have as many barbers as you like here -- as long as you have enough names in barbs!
seats_in_waiting_room = 15 # put the number of seats you'd like to have in the waiting room

close_time = 100 # end thread after {} seconds

waiting_custs = []
on_duty = []



class Barber(Thread):

	def __init__(self, barb_name, max_chairs):
		super(Barber, self).__init__()
		self.barb_name = barb_name
		self.max_chairs = max_chairs # a queue (number) of chairs in the waiting room
		self.is_shop_open = True # Flag to end the main thread
		self.sleeping = True # Flag to have the barber start at sleep until a customer arrives
		self.waiting_count = 0
		self.number_haircuts = 0
		self.tips = 0 
		self.days_profit = 0


	def run(self):
		# make sure is_shop_open is true and check for customers.
		# don't let barber leave if customers are present.

		while self.is_shop_open or not self.max_chairs.empty(): # continue until shop is closed or queue is empty
			
			if not self.max_chairs.empty():
				self.sleeping = False # if customers awake 
				customer = self.max_chairs.get()
				customer.in_barber_chair = True
				print("~~ SNIP SNIP ~~  Barber {} will now cut {}'s hair.".format(self.barb_name, customer.name))
				waiting_custs.remove(customer.name)
				print('\n'"   --- {} customer(s) in the waiting room ---"'\n'.format(len(waiting_custs)))
				print("{} has {} hair, this should take {}0 minutes.".format(customer.name, customer.hair_type, customer.cut_time))
				time.sleep(cut_time)
				customer_time_waster = random.choice(["yes", "no"])
				
				if customer_time_waster == "yes":			# another time simulation
					print("""
		Oh no! {} is not yet happy with their cut!
		Barber {} will have to spend more time than expected!
				~~ SNIP SNIP ~~
					""".format(customer.name, self.barb_name)) 
					stagger = random.choice([2, 3, 4]) # time spent with time waster customer
					time.sleep(stagger)
				print("Barber {} is done cutting {}'s {} hair."'\n'.format(self.barb_name, customer.name, customer.hair_type))
				self.number_haircuts += 1
				self.tips += random.choice(range(6))
				self.days_profit += cut_time * 15
			
			elif not self.sleeping: # elif no customers in line and not already sleeping, grab 40 winks
				self.sleeping = True 
				print("""
				ZZZZZZZZZZZzzzzzzzzzZZZZZZZZZZzzzzzzzzzz
				No one in the waiting room,
				Barber {} is going to nap in the chair.
				ZZZZZZZZZZZzzzzzzzzzZZZZZZZZZZzzzzzzzzzz
				""".format(self.barb_name))
		
		if number_rejected > 0:
			time.sleep(8) # this is in order to make sure all barbers are done
								# for the day before we release the statement
			print("""
		Look at the time! We have to close up the shop!
		The barbers:
		""", end = "")
			[print(name, end = " ") for name in on_duty]
			print("""
		gave {} haircuts altogether!
		We made a total of ${}.
		We were so busy we had to reject {} customer(s)!
		We must do better tomorrow.
			   	""".format(self.number_haircuts,sum([self.tips, self.days_profit]), number_rejected))
			os._exit(0)

		else:
			time.sleep(8)  # this is in order to make sure all barbers are done
								# for the day before we release the statement
			print("""
		Look at the time! We have to close up the shop!
		The barbers:
		""", end = "")
			[print(name, end = " ") for name in on_duty]
			print("""
		gave {} haircuts altogether!
		We made a total of ${}.
	  	Although we were busy, we rejected {} customers!
	   	I'm so proud of you!
			""".format(self.number_haircuts,sum([self.tips, self.days_profit]), number_rejected))
			os._exit(0)


class Customer(Thread):

	def __init__(self, name, hair_type, cut_time):
		super(Customer, self).__init__()
		self.name = name
		self.hair_type = hair_type
		self.cut_time = cut_time
		self.in_barber_chair = False

	def run(self):
		while not self.in_barber_chair:
			pass
		time.sleep(cut_time)


if __name__ == '__main__':
	
	print("""
		---------------------------
		 Time to open up the shop!
		---------------------------
		""")

	number_rejected = 0
	hair_types = ['short', 'medium length', 'long'] # haircut length also simulates time
	waiting_room = queue.Queue(seats_in_waiting_room) # max number of chairs in waiting room {} chairs
	
	i = 0
	while i < barbers_on_duty:
		on_duty.append(random.choice(barbs))
		barber = Barber(on_duty[i], waiting_room)
		barber.start()
		print('\n'" - - {} is going to start their day at work! - - ".format(barbs[i]))
		i += 1

	is_shop_open = time.time()
	current_time = is_shop_open
	while (current_time - is_shop_open) < close_time: # check if barber thread has been running longer than open time
		please_cut_my_hair = random.choice(custs) # pick a random name
		if not waiting_room.full(): # if the Queue isn't full grab a seat
			waiting_custs.append(please_cut_my_hair)
			length = random.choice(hair_types)
			cut_time = 4 if length == 'short' else 6 if length == 'medium' else 8
			customer = Customer(please_cut_my_hair, length, cut_time)
			waiting_room.put(customer)
			print('\n'"{} sat down in the waiting room""\n".format(please_cut_my_hair))
			customer.start()
		else: # else leave shop
			print("""
		Sorry, {}! We're too full, try coming back when it's not so busy!
			""".format(please_cut_my_hair))
			number_rejected += 1
		stagger = random.choice([1, 2]) # stagger time each customer thread is created
		time.sleep(stagger)
		current_time = time.time()

	j = 0
	while j < barbers_on_duty:
		barber.is_shop_open = False # close shop/barber will finish off remaining threads in queue.
		j += 1
