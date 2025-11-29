from sys import exit

#    _   __                   _ _   
#   | | / /                  | | |  
#   | |/ /  _____      ____ _| | |_ 
#   |    \ / _ \ \ /\ / / _` | | __|
#   | |\  \ (_) \ V  V / (_| | | |_ 
#   \_| \_/\___/ \_/\_/ \__,_|_|\__|
#                                    

class Debugger:
    def __init__(self, prefix="[Kowalt]>> "):
        self.prefix = prefix

    def info(self, msg):
        print(self.prefix + str(msg))
    
    def warn(self, msg):
        print("[WARN]" + self.prefix + str(msg))
    
    def error(self, msg):
        print("[ERROR]" + self.prefix + str(msg))
        exit(1)

class Value:
    def __init__(self, name="Value", data=0, debugger=None):
        self.debugger = debugger or Debugger()
        if not isinstance(data, (int, float)):
            self.debugger.error("Value can only be Int or Float")
        
        self.name = name
        self.data = data
    
    def add(self, amount):
        self._require_number(amount)
        self.data += amount
        self.debugger.info(f"{self.name} += {amount} → {self.data}")

    def set(self, amount):
        self._require_number(amount)
        self.data = amount
        self.debugger.info(f"{self.name} = {amount}")

    def delete(self, amount):
        self._require_number(amount)
        self.data -= amount
        self.debugger.info(f"{self.name} -= {amount} → {self.data}")

    def _require_number(self, v):
        if not isinstance(v, (int, float)):
            self.debugger.error("argument must be Int or Float")
