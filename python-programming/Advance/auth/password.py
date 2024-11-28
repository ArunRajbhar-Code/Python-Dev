from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()
password='mypassword'
hashed_pass=bcrypt.generate_password_hash(password)

print(hashed_pass)

real_pass=bcrypt.check_password_hash(hashed_pass,'mypassword')
print(real_pass)