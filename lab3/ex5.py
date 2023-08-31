import random

otp = ""

otp += str(random.choice([8, 9]))
otp += str(random.choice([6, 7]))
otp += str(random.choice([4, 5]))
otp += str(random.choice([2, 3]))
otp += str(random.choice([0, 1]))

print("Your OTP is %s. This password will be expired within 5 minutes." % otp)