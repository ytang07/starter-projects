def compound_interest(principle, rate, freq, years):
    return principle*(((1+rate/freq)**(freq*years)-1)*years/rate)

print(compound_interest(800, 0.40, 12, 10))