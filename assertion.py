def KelvinToFahrenheit(Temperature):
    try:
        assert(Temperature>=0),Temperature
        return((Temperature-273)*1.8)+32
    except AssertionError:
        print("colder than absolute zero",Temperature)
print(KelvinToFahrenheit(273),"deg far")
print(int(KelvinToFahrenheit(505.78)),"deg far")
print(KelvinToFahrenheit(-5),"deg far")
