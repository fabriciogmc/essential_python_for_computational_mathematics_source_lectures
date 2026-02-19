# Basic match-case example

personal_data = {"name": "Fabricio", "age": 46 , 
                 "profession": "scientist"}

match personal_data:
    case {"name": "Fabricio", "age": 46 }:
        print("Found 2 values!")

    case {"name": name, "age": age }:
        print("Found 2 keys! Name: %s , Age: %s" %(name,age))
        
    case {"name": "Fabrício", "age": 46 }:
        print("Found!")

    case _ :
        print("Not found!")
