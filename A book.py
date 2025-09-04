class Accounts:
	def __init__(self, phone_email, username, password):
		self.phone_email = phone_email
		self.username = username
		self.password = password
	
	def show(self):
		print(f"{self.phone_email} : {self.username} : {self.password}")
		
facebook = Accounts("07148254493@gmail",  "Terer Somtdili",  "656956")

google = Accounts("08165852258", "Zojdnesko", "Ebastijo1@ificat")

istagram = Accounts ("82288458888", "Zanaskbd", "lgdgadon")

google3 = Accounts("123598898", "paisefsko", "stifichhkffation")

yahoo = Accounts("125888788", "fjkfjvhesko", "967284vn rosoft")

yahoo.show()
