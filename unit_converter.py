def in_to_ft(_in):
    return _in/12

def ft_to_in(_ft):
    return _ft*12

def mi_to_km(_mi):
    return _mi*1.609

def km_to_mi(_km):
    return _km/1.609

def c_to_f(_c):
    return 9*_c/5 + 32

def f_to_c(_f):
    return (_f-32)*5/9

_dict = {
    "inches to feet": in_to_ft,
    "feet to inches": ft_to_in,
    "miles to kilometers": mi_to_km,
    "kilometers to miles": km_to_mi,
    "celsius to fahrenheit": c_to_f,
    "fahrenheit to celsius": f_to_c     
}

print("Available conversions (to and from): inches to feet, miles to kilometers, celsius to fahrenheit")
convert = input("Which conversion do you want to do? ")
num = float(input("What is the value in the base unit? "))

op = _dict[convert]
print(op(num))
