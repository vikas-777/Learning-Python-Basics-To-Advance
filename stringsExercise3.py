greetings = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

Name = input("Enter the name: ")
Date = input("enter date in dd/mm/yyyy format")
New_greetings = greetings.replace("<|Name|>", Name).replace("<|Date|>", Date)
print(greetings)
print(New_greetings)
print(f"Name\t {Name} \nDate\t {Date}")
