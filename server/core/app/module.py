import os 
import sys

def make_module(module_name: str):
    
    module_name = module_name.lower()
    module_name = os.path.join(os.getcwd(), module_name)
    if os.path.exists(module_name):
        print("Module already exists")
        return
        
    os.mkdir(module_name)
    
    with open(f"{module_name}/__init__.py", "w") as f:
        f.write("")
        
    print(f"Module {module_name} created")
    


if __name__ == "__main__":
    module_name = sys.argv[1]
    make_module(module_name)
    
    