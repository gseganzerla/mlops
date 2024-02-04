from datetime import datetime

CURRENT_DATE = datetime.now().strftime('%Y-%m-%d')


def write_log(request_data, response_data):
    with open(f"var/logs/{CURRENT_DATE}.log", '+a') as file:
        log = f"""request_data: {request_data}, response_data: {response_data}, date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"""

        file.write(log)
