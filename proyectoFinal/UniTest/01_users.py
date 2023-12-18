
class Usuarios:

    def __init__(self, username, email="indefinido"):
        self.username = username
        self.email = email

    def getusername(self):
        return self.username

    def getemail(self):
        return self.email


user = Usuarios("Steffany", "steff@s.com")
email = user.getemail()
print(email)

if '@' in "steff@s.com":
    print("Prueba exitosa")
else:
    print("Prueba fallida")


user = Usuarios("XXXXXXXXXXX")
email =user.getemail()
if email == "indefinido":
    print("Prueba exitosa")
else:
    print("Prueba fallida")


user = Usuarios("Steffany")
nombre = user.getusername()
if nombre == "Steffany":
    print("Prueba exitosa")
else:
    print("Prueba fallida")




