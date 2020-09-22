# Hospital-Appointment-Management-System

Computer Networks Project

Team Size:3

Members: 
         Karthik.N (PES1201700692)
         V.Nayana (PES1201701580)
         Swathi.S.V (PES1201802467)

We have implemented a hospital appointment management system. The topology contains 3 client systems connected to a server through switches using client-server architecture. Here the server takes information provided by the user and processes it to get an output. The system first displays a user interface which asks the user to login with password. The user next has to choose two diseases they are suffering from, after which they are suggested with the best doctor and asked to book a slot from 1-20. The user cancel an appointment if he wishes to.
We have used tkinter module to create GUI. 

FUNCTIONS USED:
We have used 3 functions to implement this system
1)Book
2)Cancel 
3)Exit

Book: This function is used to book a slot from the available slots.
After the user has logged in, he/she is asked to mention the diseases they are suffering from. Based on the user’s input the best doctor available is suggested and appointment with that doctor is booked by choosing the available slot from 1-20.

Cancel: If the user wishes to cancel an appointment, he/she can cancel it by clicking on the Cancel button. They can cancel either all appoinments by entering 0 or one by one by entering 1 and then mentioning the doctor’s ID.

Exit: Once the appointments are booked or cancelled, the user can exit the booking interface by clicking on EXIT button.
