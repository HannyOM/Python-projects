email = input("Input your email address: ").strip()
x = email.index("@")
username = email[:x]
domain_name = email[x+1:]
print ("Username: " + username)
print ("Domain_name: " + domain_name)
