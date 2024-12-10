import datetime

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"output_{current_time}.txt"
    with open(filename, "w") as f:
        # Write some data to the file
        f.write("This is a sample file generated at {}\n".format(current_time))
    print(f"Created file: {filename}")
    # Adjust the sleep time as needed
    time.sleep(60)  # Create a new file every 1 minute
