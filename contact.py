class contact:
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno

    def __str__(self):
        return 'Contact : [ Name : {}, Email : {}, Phoneno : {}]'.format(self.name, self.email, self.phoneno)