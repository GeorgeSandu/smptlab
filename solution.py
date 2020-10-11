from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
	msg = "\r\n Message SMPT LAB"
	endmsg = "\r\n.\r\n"

	# Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
	#Fill in start
	mail_server = mailserver

	mail_port = port
	#Fill in end
	
	# Create socket called clientSocket and establish a TCP connection with mailserver and port
	# Fill in start
	Client_SMPT_Socket = socket(AF_INET,SOCK_STREAM)
	Client_SMPT_Socket.connect((mail_server, mail_port))
	# Fill in end

	recv = clientSocket.recv(1024).decode()
	print("Msg after reqst: "+ str(recv))
	if recv[:3] != '220':
		print('220 reply not received from server.')

	# Send HELO command and print server response.
	heloCommand = 'HELO George\r\n'
	clientSocket.send(heloCommand.encode())
	recv1 = clientSocket.recv(1024).decode()
	print(recv1)
	if recv1[:3] != '250':
		print('250 reply not received from server.')

	# Send MAIL FROM command and print server response.
	# Fill in start
	mailfromCommand ='georgesandutest@gm.com\r\n'
	Client_SMPT_Socket.send(mailfromCommand.encode())
	recv1 = clientSocket.recv(1024)
	print(recv1)
	if recv1[:3]! = '250':
		print('250 reply not received from server.')
	# Fill in end

	# Send RCPT TO command and print server response.
	# Fill in start
	rcpttoCommand = '<gsandutest2@gm.com>\r\n'
	Client_SMPT_Socket.send(rcpttoCommand.encode())
	recv1 = clientSocket.recv(1024)
	print(recv1)
	if recv1[:3] != '250':
		print('250 reply not received from server.')
	# Fill in end

	# Send DATA command and print server response.
	# Fill in start
	dataCommand = 'Data'
	print dataCommand
	Client_SMPT_Socket.send(dataCommand.encode())
	recv1 = clientSocket.recv(1024)
	print recv1
	if recv1[:3] != '250':
		print('250 reply not received from server.')
	# Fill in end

	# Send message data.
	# Fill in start
	message = raw_input('Enter Message Here: ')
	# Fill in end

	# Message ends with a single period.
	# Fill in start
	Client_SMPT_Socket.send(message+ mailMessageEnd)
	print recv1
	if recv1[:3] != '250':
		print('250 reply not received from server.')
	# Fill in end

	# Send QUIT command and get server response.
	# Fill in start
	quitCommand = 'Quit\r\n'
	print quitCommand
	Client_SMPT_Socket.send(quitCommand)
	recv1 = clientSocket.recv(1024)
	print recv1
	if recv1[:3] != '250'.:
	print('250 reply not received from server.')
	pass
	# Fill in end


if __name__ == '__main__':
	smtp_client(1025, '127.0.0.1')
