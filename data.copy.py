# 1. The original master list of employee salaries
master_salaries = [45000, 52000, 61000, 48000]

# 2. Create a completey independtly clone using .copy()
experimental_salaries = master_salaries.copy()

# 3. Change the first item in our experimental list only 
experimental_salaries[0] = 99999

# 4. Print both to prove the original master list stayed safe!
print("Original Master (Safe):",master_salaries)
print("Experimental Clone (Modified):", experimental_salaries)
