# Write a function password_validator(correct_password) that returns a function.
# The returned function checks if the password matches.

def password_validator(password):
    def check(confirm_password):
        return password == confirm_password
    return check

check = password_validator('pass@123')
print(check('pass@1234'))
print(check('pass@123'))
print(check.__closure__)