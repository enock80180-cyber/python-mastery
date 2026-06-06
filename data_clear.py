# 1.Temporary list of the scanned IP addresses 
Temp_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]
print("Before cleanup:", Temp_ips)

# 2. Use clear() machine tool to wipe the memory 
Temp_ips.clear()

# 3. Print the list again to verify it is completely empty
print("After cleanup:", Temp_ips)
