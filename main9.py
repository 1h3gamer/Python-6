class Shepherd:
    species = "dog"
    def __init__(self,breed,colour):
        self.breed = breed
        self.colour = colour

blu = Shepherd("German","red")
woo = Shepherd("Australian","green")

print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

print("Blu is a {} {} and is {} ".format(blu.breed,blu.species,blu.colour))
print("Woo is an {} {} is {} ".format(woo.breed,woo.species,woo.colour))