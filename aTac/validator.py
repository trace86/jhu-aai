import logging

def validate_port(result, port):
    port_text = ":" + str(port)
    if port_text in result:
        message = f"VALIDATOR: FAILED: port {port} is still open"
        logging.info(message)
        return message
    else:
        message = f"VALIDATOR: SUCCESS: port {port} is closed"
        logging.info(message)
        return message

def validate_exploit(result, exploit_number):
    success_result = options[exploit_number]
    print("RESULT", result)
    print("SUCCESS", success_result)
    if success_result in result:
        message = f"VALIDATOR: SUCCESS: exploit {exploit_number} is successful"
        logging.info(message)
    else:
        message = f"VALIDATOR: FAILED: exploit {exploit_number} is unsuccessful"
        logging.info(message)
    return message

def success_message_0000():
    return "Command shell session 1 opened"

#not sure if this is success or not
def success_message_0001():
    return "Sending keep-alive headers..."

def success_message_0002():
    return "Login Successful"

#may need to reformat after seeing actual log, there are three databases instead of one
#namely postgres, template0, template1
def success_message_0003():
    return "template0"

#can further check and compare the if the password is the same
def success_message_0004():
    return "md53175bce1d3201d16594cebf9d7eb3f9d"

#can further check and compare the if the query result is the same
def success_message_0005():
    return "md53175bce1d3201d16594cebf9d7eb3f9d"

#can further check and compare the if the query result is the same
def success_message_0006():
    return "Query appears to have run successfully"

def success_message_0007():
    return "Meterpreter session 1 opened"

#can further check and compare the two files, the one in the exploit machine, the one retrieve by the attacker
def success_message_0008():
    return "Postgres - /etc/passwd saved"

#need to further check if this is correct, as it may say no session created
def success_message_0009():
    return "Exploit completed"

#need to further check if this is correct, as it may say no session created
def success_message_0010():
    return "Exploit completed"

#need to further check if this is correct, as it only says session created
def success_message_0011():
    return "Command shell session 1 opened"

#need to further check if this is correct, as it it only says session created
def success_message_0012():
    return "Command shell session 1 opened"

options = {
    0: success_message_0000(),
    1: success_message_0001(),
    2: success_message_0002(),
    3: success_message_0003(),
    4: success_message_0004(),
    5: success_message_0005(),
    6: success_message_0006(),
    7: success_message_0007(),
    8: success_message_0008(),
    9: success_message_0009(),
    10: success_message_0010(),
    11: success_message_0011(),
    12: success_message_0012(),
}