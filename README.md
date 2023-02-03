# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Hongyu Zhao

## Lab Question Answers

Answer for Question 1: 
The reliability of UDP dropped drastically when the 50% loss was added. The numbers would sometimes not be received after transmission. This occured because UDP just sends the information and does not verify that it was received. Thus, in an enviornment where there is 50% loss, with UDP, 50% of the transmissions are lost and never received.

Answer for Question 2:
The reliability of TCP remained the same even in a 50% loss environment. This is because TCP waits to verify if information was received, and if not, then it will be sent again. Thus, all information sent will be received.

Answer for Question 3:
The speed of the TCP response slowed down a lot. This may happen because if a transmission is not verified, then the server waits until it gets all the missed information. Thus, TCP has to wait a lot for the information in a 50% loss environment which slows down transmission.

Answer about tcp_server.c

1. The arguments argc and *argv[] allows for arguments to be given in the command line with the program is run through the command line. argc stores the number of arguments that the code is ran with, including itself. *argv[] stores the actual arguments in an array, each argument having its own index.

2. A file descriptor is a unique non-negative integer given to any file or process running in the OS. This number can them be used to refer to and interact with the file. A file descriptor table is the table that stores all of these numbers for the current files that are opened.

3. A struct is a blueprint for which a new datatype can be defined. A struct will usually hold fields of values that can be assigned to this new datatype created by struct. The structure of sockaddr_in contains a short variable called sin_family, a unisgned short variable called sin_port, another structure of in_addr called sin_addr, and a char array called sin_zero. As a whole, the structure sockaddr_in contains and handles internet addresses.

4. The input parameters of socket() are the address domain, the type of socket, and the protocol. The function returns a file descriptor which the socket can be refered to by.

5. The input parameters of bind() are the socket file descriptor, the address that its bound to, and the size of the address its bound to. The input paramteres to listen() are the socket file descriptor and the backlog queue size.

6. Using while(1) allows for multiple messages to be received and written, not just one. If there are multiple connections, each user will have to wait for the previous user to finish sending and receiving a message before they can connect and send their message.

7. The fork() command creates a new process that runs the same code that comes after. Thus, it can have multiple instances of receiving and sending messages which would help accomodate multiple connections.

8. A system call is a request for the kernel of the OS to provide some service.
...

