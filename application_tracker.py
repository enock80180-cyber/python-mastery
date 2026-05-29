# Note 1: A list of companies you applied to
my_applications = ["company A", "Calco", "Company B"]

print("scanning my application statuses......")

# Note 2: The loop + If-statement Combo Machine
for company in my_applications:
     if company == "Calco":
        print("MATCH FOUND:" + company + " invited me for an interview! Time to celebrate! 🎉")
     else:
         print(company + " status: Still waiting for a response ")
