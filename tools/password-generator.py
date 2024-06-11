import random

class Password: 
    
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    symbol = "~!@#$%^&*()_-?<>{[]}"
    
    def __init__(self, amount = 5) -> None:
        random.shuffle(list(self.lowercase))
        random.shuffle(list(self.uppercase))
        random.shuffle(list(self.symbol))
        
        for i in range(amount):
            result = self.GetRandomChar()
            random.shuffle(result)
            print("".join(result))
    
    def GetRandomChar(self):
        result = []
        
        for i in range(5):
            result.append(random.choice(self.lowercase))
        
        for i in range(4):
            result.append(random.choice(self.uppercase))
            
        for i in range(3):
            result.append(random.choice(self.symbol))
        
        return result
    
password = Password()
    