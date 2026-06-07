# 1. Current queue of pending server tasks
task_queue = ["backup_data", "clean_logs", "update_apps"]
print("Original Queue:", task_queue)

# 2. Use .insert() to force "SEC-PATCH" into the index 1
# syntax: list.insert(index_position, item_to_add)
task_queue.insert(1,"SEC-PATH")

# 3. Print the new queue to see the precision injection
print("priority Queue:", task_queue)
