class Solution:
    def isValid(self, s: str) -> bool:
        container = []
        brackets = { 
            ')':'(', 
            '}':'{',
            ']':'['
        }
        
        for char in s:
          if char in brackets.values():
            container.append(char)
          elif container and container[-1] == brackets[char]:
             container.pop()
          else:
            return False
        return True if not container else False
         

          

        
