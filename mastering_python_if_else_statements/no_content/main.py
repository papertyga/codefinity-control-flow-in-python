password = "user123"
correct_password = "p@ssword123"
login_message = "Login successful!"
login_message = "Incorrect password, try again."

login_message if password == correct_password else not login_message
    

# Testing
print("Login Status:", login_message)