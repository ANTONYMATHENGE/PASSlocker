import unittest
from main import User,Credentials
users=[]
credentials=[]

class TestMain(unittest.TestCase):
    def setUp(self):
        self.user=User('Antony','2021')
        self.cred=Credentials('facebook','Antony','1996')
    def test_user(self):
        self.assertEqual(self.user.username,'Antony')
        self.assertEqual(self.user.password,'2021')

    def test_credentials(self):
        self.assertEqual(self.cred.site,'facebook')
        self.assertEqual(self.cred.username,'Antony')
        self.assertEqual(self.cred.password,'1996')

    def test_register(self):
        user=User('Antony','2021')
        users.append(user)
        self.assertEqual(len(users),1)
   
       

if __name__=='__main__':
    unittest.main()
