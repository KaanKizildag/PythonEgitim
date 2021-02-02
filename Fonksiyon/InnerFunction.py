def usAlma(power):

    def inner(number):
        return power ** number

    return inner

metot = usAlma(3) # şu kuvvetini al
print(metot(4)) # şunun kuvvetini al