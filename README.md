Appointment Bot - Dental Clinic Assistant
This project is a conversational AI assistant designed to help patients book appointments at a dental clinic. It uses LangChain and OpenAI's GPT-3.5 to facilitate dynamic conversations, handle appointment bookings, and ensure users can get confirmations for their appointments.

Features
AI-Powered Appointment Booking: The bot can assist patients in booking dental appointments by interacting with them conversationally.
Date and Time Detection: Automatically detects date and time from user input using regular expressions.
Conversation Memory: The bot retains the context of the conversation to provide a seamless experience, remembering user inputs and past queries.
Real-Time Appointment Confirmation: Once a user provides an appointment request, the bot confirms the booking and checks for any conflicts.
Final Appointment Summary: At the end of the conversation, the bot displays a summary of all booked appointments.
Prerequisites
Before running the bot, ensure you have the following prerequisites installed:

Python 3.7+
pip (Python package manager)
Required Libraries
langchain
langchain-community
openai
python-dotenv
re (built-in Python library for regex operations)
You can install the necessary dependencies by running:

bash
Copy code
pip install langchain langchain-community openai python-dotenv
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/avinash00134/appointment-bot.git
cd appointment-bot
Create a .env file in the root directory of the project and add your OpenAI API key:
makefile
Copy code
OPENAI_API_KEY=your-openai-api-key-here
Make sure to replace your-openai-api-key-here with your actual API key from OpenAI.

Usage
Starting the Bot
Once everything is set up, you can start the bot by running the following command:

bash
Copy code
python appointment_bot.py
The bot will greet you and start a conversation. You can interact with it by providing appointment dates and times. Here's how the conversation might go:

vbnet
Copy code
Welcome to the Dental Clinic Assistant! Type 'exit' to end the conversation.

You: hi there what can do for me
Agent: Hello! I can help you book an appointment at our dental clinic. When would you like to schedule your visit?

You: i would like to book an appointment    
Agent: That's great! I can help you with that. When would you like to book the appointment for?

You: 5 august 5pm
Agent: Booking your appointment for 5 August at 5 PM... Done! Your appointment is confirmed.

You: exit
Agent: Thank you! Have a great day!

Final Appointments:
Appointment on 5 August at 5 PM
How It Works
Conversation Setup: The bot prompts the user to provide an appointment date and time.
Date and Time Parsing: It extracts the date and time from the user input using regex.
Conflict Check: It checks if the user’s preferred date is already booked. If not, it confirms the booking.
Final Appointment Display: When the user types exit, the bot displays all booked appointments.
