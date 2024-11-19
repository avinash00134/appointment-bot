import os
import warnings
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import re
# Suppress warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Initialize LangChain
def setup_langchain():
    """
    Sets up LangChain with OpenAI API using the API key from environment variables.
    """
    # Fetch the OpenAI API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
    else:
        print("OpenAI API Key is available!")

    return ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo", openai_api_key=api_key)

# Build the conversation chain with memory
def build_conversation_chain(llm, memory):
    """
    Creates a LangChain-based conversation chain with memory for appointment booking.
    """
    system_message = (
        "You are a friendly AI assistant for a dental clinic. "
        "Assist patients in booking appointments. Ask for the date and time if not provided, "
        "and confirm the booking once the details are received. If the user asks for help or has a question, "
        "respond appropriately. Always confirm when an appointment is booked successfully."
    )
    system_template = SystemMessagePromptTemplate.from_template(system_message)
    human_template = HumanMessagePromptTemplate.from_template("{query}")
    chat_prompt = ChatPromptTemplate.from_messages([system_template, human_template])

    # Adding the memory to the conversation chain
    return LLMChain(llm=llm, prompt=chat_prompt, memory=memory)

# Appointment management logic
appointments = {}

def process_conversation(user_input, llm_chain):
    """
    Processes the user's input and dynamically manages the conversation.
    """
    try:
        ai_response = llm_chain.run(query=user_input)
    except Exception as e:
        return f"Error: Failed to process your request. Details: {str(e)}"
    
    # Extract appointment details using regular expressions
    date_time_pattern = r"(\d{1,2}\s*(?:\w+\s*\w*)?\s*(?:\d{4})?)\s*(\d{1,2}(:\d{2})?\s*(?:AM|PM|am|pm))"
    match = re.search(date_time_pattern, user_input)
    
    if match:
        date = match.group(1)
        time = match.group(2)
        
        # Normalize date and time formatting if necessary
        if date and time:
            if date in appointments:
                return f"Sorry, there is already an appointment on {date} at {appointments[date]}. Please choose another time."
            appointments[date] = time
            return f"Booking your appointment for {date} at {time}... Done! Your appointment is confirmed."
    
    # Return the AI response for generic queries
    return ai_response

def start_conversation(llm_chain):
    """
    Starts the dynamic conversation loop for appointment booking.
    """
    print("Welcome to the Dental Clinic Assistant! Type 'exit' to end the conversation.\n")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Agent: Thank you! Have a great day!")
                break
            response = process_conversation(user_input, llm_chain)
            print(f"Agent: {response}")
        except KeyboardInterrupt:
            print("\nAgent: Goodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

# Main script
if __name__ == "__main__":
    try:
        llm = setup_langchain()
        
        # Initialize memory buffer with a window size of 5 (can be adjusted)
        memory = ConversationBufferMemory(memory_key="conversation_history", return_messages=True)
        
        # Build the conversation chain with memory
        llm_chain = build_conversation_chain(llm, memory)
        
        print("Starting the AI Assistant for booking appointments...\n")
        start_conversation(llm_chain)
        
        # Final Appointments after exit
        if appointments:
            print("\nFinal Appointments:")
            for date, time in appointments.items():
                print(f"Appointment on {date} at {time}")
        else:
            print("\nNo appointments booked.")
    
    except Exception as e:
        print(f"Critical Error: {str(e)}")
