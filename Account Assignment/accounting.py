import doctest
import os
import tempfile
import pickle
import http.cookiejar


#Dekai Rohlsen
#U50753261

class Transaction(object):

	def __init__(self,amt,date,currency,conv,descript):
		self.__amt = amt
		self.__date = date
		self.__currency = currency
		self.__conv = conv
		self.__descript = descript


	def get_amt(self):
		#print("Getting attribute amount...")
		""" Return amount
		>>> t.get_amt()
		Getting attribute amount...
		100
		"""
		print("Getting attribute amount...")
		return self.__amt

	def get_date(self):
		#print("Getting attribute date...")
		""" Return date
		>>> t.get_date()
		Getting attribute date...
		'Today'
		"""
		print("Getting attribute date...")
		return self.__date
		
	def get_currency(self):
	#	print("Getting attribute currency type...")
		""" Return currency
		>>> t.get_currency()
		Getting attribute currency type...
		'USD'
		>>>
		"""
		print("Getting attribute currency type...")
		return self.__currency	
		
	def get_conv(self):
		#print("Getting attribute conversion...")
		"""Return Conv type
		>>> t.get_conv()
		Getting attribute conversion...
		1
		"""
		print("Getting attribute conversion...")
		return self.__conv

	def get_descript(self):
		#print("Getting attribute Description...")
		"""Return Description
		>>> t.get_descript()
		Getting attribute Description...
		'Deposit'
		"""
		print("Getting attribute Description...")
		return self.__descript
	
	def get_usd(self):
		#print("Getting attribute usd...")
		"""Return USD value
		>>> t.get_usd()
		Getting attribute usd...
		100
		"""
		print("Getting attribute usd...")
		usd_val = self.__amt * self.__conv
		return usd_val

	amt = property(get_amt)
	date = property(get_date)
	currency = property(get_currency)
	conv = property(get_conv)
	descript = property(get_descript)
	usd = property(get_usd)


class Account(Transaction):
	
	def __init__(self):
		self.__acct_name = None
		self.__acct_num = 1111111
		self.transactions = []
		

	def get_acct_num(self):
		"""
		>>> a.get_acct_num()
		1111111
		"""	
		return self.__acct_num

	def get_acct_name(self):
		"""
		>>> a.get_acct_name()
		
		"""
		return self.__acct_name

	def set_acct_name(self, name):
		"""
		>>> a.set_acct_name("Bob")
		Attempting to set account name [ Bob ]... 
		Error: name is too short!!
		<BLANKLINE>
		>>> a.set_acct_name("Brian")
		Attempting to set account name [ Brian ]... 
		Name change is successful!
		<BLANKLINE>
		"""
		print("Attempting to set account name [ %s ]... " % name)
		if(len(name) > 4):
			print("Name change is successful!\n")
			self.__acct_name = name

		else:
			print("Error: name is too short!!\n")	
	def all_usd(self):

		for i in range(0,len(self.transactions)):
			if self.transactions[i][2][2] != "USD":
				return False
		return True

	def get_balance(self):
		
		total = 0
		check = self.all_usd()	
		if check:
			print("All transactions are in USD")
			for i in range(0,len(self.transactions)):
				print(self.transactions[i][2])
				total = total + self.transactions[i][2][0]	
		else:
			print("All transactions are not in USD. Converting...")
			for i in range(0,len(self.transactions)):
				print(self.transactions[i][2])
				total = float(total) + self.transactions[i][2][0]*self.transactions[i][2][3]

		print("\nCurrent balance is: %.2f\n" % total)


	def apply_(self,trans):
		
		self.transactions = sum([self.transactions, trans],[])
		print("%d transactions were conducted" % len(self.transactions))

	def save(self):

		acct_num = self.__acct_num
		account_name = self.__acct_name + ".acc"
		name = os.path.join(tempfile.gettempdir(),account_name)
		
		print("saving data to: %s" % name)
		fh = None
		try:
			data = [self.__acct_name,acct_num,self.transactions]
			fh = open(name,'wb')
			pickle.dump(data,fh,pickle.HIGHEST_PROTOCOL)
		except (EnvironmentError, pickle.PicklingError) as err:
			raise SaveError(str(err))
		finally:
			if fh is not None:
				print("Save Sucessful!!\n")
				fh.close()

	def load(self):
		account_name = self.__acct_name + ".acc"
		name = os.path.join(tempfile.gettempdir(),account_name)
		

		print("Attempting to open file: %s" % name)
		fh = None
		try:
			fh = open(name,'rb')
			data = pickle.load(fh)
			
		except (EnvironmentError,pickle.UnpicklingError) as err:
			raise IOError(str(err))
		finally:
			if fh is not None:
				print("Load Successful!!\n")
				for i in range(0,len(data)):
					if self.__acct_num != data[1]:
						print(data[1])
						print("Discrepency in account numbers!")
						print("your acct numbers:%s | %s" % (self.__acct_num,data[1] ))
						return -1
				fh.close()
				print("Loaded Data: \n Acct name: %s \n Acct number: %d \n Transactions: " % (data[0],data[1]))
				for i in range(0,len(data[2])):
					print(data[2][i][2])
	acct_num = property(get_acct_num)
	acct_name = property(get_acct_name,set_acct_name)
	balance = property(get_balance)
	usd = property(all_usd)



if __name__ == "__main__":

	doctest.testmod(extraglobs={'t': Transaction(100,"Today","USD",1,"Deposit"), 'a': Account()})
	my_trans = Transaction(555,"June 22nd 2017","USD",1,"Payroll")
	print("\n Testing Defaults for Transaction() \n")
	print("Amount for transaction: %d \n" % my_trans.amt)
	print("Date of transaction: %s \n" % my_trans.date)
	print("Type of currency: %s \n" % my_trans.currency)
	print("Conversion rate to USD: %d \n" % my_trans.conv)
	print("Description of transaction: %s \n" % my_trans.descript)
	print("Result of conversion: %d \n" % my_trans.usd)
	
	my_acct = Account()
	my_acct.set_acct_name("Tom")
	my_acct.set_acct_name("Banks")
	translist1 = [[1111111,"Banks", [10,"nov 22nd","USD",1,"birthday gift"]],
		[1111111,"Banks", [20,"nov 22nd","USD",1,"birthday gift"]],
		[1111111,"Banks", [50,"nov 22nd","USD",1,"birthday gift"]]]


	
	print("\nAccount information: \n")
	print("Account Name: %s" % my_acct.acct_name)
	print("Account Number: %s" % my_acct.acct_num)
	my_acct.apply_(translist1)
	my_acct.get_balance()
	my_acct.save()
	my_acct.load()

	



	translist2 = [[1111111,"Banks", [10,"nov 22nd","USD",1,"birthday gift"]],
                [1111111,"Banks", [20,"nov 22nd","FRE",.8,"birthday gift"]],
                [1111111,"Banks", [51,"nov 22nd","BRI",.3,"birthday gift"]]]
	
	print("\nAccount information: \n")
	print("Account Name: %s" % my_acct.acct_name)
	print("Account Number: %s" % my_acct.acct_num)
	my_acct.apply_(translist2)
	my_acct.get_balance()
	my_acct.save()
	my_acct.load() 
