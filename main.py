#!/usr/bin/env python3
#Author: Shammah Matasva
#Reverse of the change calculator program
#Calculates total money amount from coins proved as input

class Account:
	def __init__(self):
		#initialise variables 
		self.totalCents=0
		self.totalDollar=0.00
		self.penny=0
		self.nickel=0
		self.dime=0
		self.quater=0

	def getInput(self):
		#input the number of coins for each type
		self.penny=int(input("Enter number of pennies: "))
		self.nickel=int(input("Enter number of nickels: "))
		self.dime=int(input("Enter number of dimes: "))
		self.quater=int(input("Enter number of quaters: "))

	def getTotalCents(self):
		#Calculate the value amount for the coins in cents
		self.totalCents=self.penny+(self.nickel*5)+(self.dime*10)+(self.quater*25)

	def getTotalDollar(self):
		#Calculate the value in dollars
		self.totalDollar=self.totalCents/100.0

	def printOut(self):
		#print out program details
		print("Thank you for using coin stack")
		print("You entered:")
		print("Pennies: %2d ,Nickels: %2d ,Dime: %2d ,Quaters: %2d " %(self.penny,self.nickel,self.dime,self.quater))
		print("You have %2d cents" %(self.totalCents))
		print("Dollar total: $ %.2f" %(self.totalDollar))

	def run(self):
		self.getInput()
		self.getTotalCents()
		self.getTotalDollar()
		self.printOut()

account=Account()
account.run()
