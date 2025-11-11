import serial

port = '/dev/ttyACM0'
baudrate = 115200
serial_connection = serial.Serial(port, baudrate, timeout=1)

while True:
    user_input = input("Press Enter to read, or type 'q' + Enter to quit: ")
    if user_input.lower() == 'q':
        break
    if user_input != '':
        continue

    # Clear any old readings in the buffer
    serial_connection.reset_input_buffer()

    # Wait for a fresh line to arrive
    data = serial_connection.readline().decode('utf-8').rstrip()
    print(data)

serial_connection.close()
