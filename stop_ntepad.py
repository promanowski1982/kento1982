import psutil

def stop_application_by_pid(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Application with PID {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")

# Example usage:
# Replace '1234' with the actual PID of the application you want to stop.
pid_to_stop = 8968
stop_application_by_pid(pid_to_stop)