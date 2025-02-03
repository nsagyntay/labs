#Write a function that computes the
#volume of a sphere given its radius.
def volume_of_sphere(radius):
    volume = (4/3) * 3.14 * radius**3
    return volume
radius = float(input("radius: "))
print(volume_of_sphere(radius))
    