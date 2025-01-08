import requests  # A Python library used for making HTTP requests to fetch data from an API
import tkinter as tk  # A standard Python library for building graphical user interfaces (GUIs).

def get_movie_info(movie_name):
    api_key = "9efff641"  # unique key used to authenticate requests to OMDb.
    base_url = "http://www.omdbapi.com/"  # Base URL used to access the OMDb API.

    # Construct the complete URL with the movie name and API key
    complete_url = f"{base_url}?t={movie_name}&apikey={api_key}"

    print(f"Requesting URL: {complete_url}")  # Debug: print the URL we're calling

    try:
        response = requests.get(complete_url)
        print(f"HTTP Status Code: {response.status_code}")  # Debug: print status code
        print(f"Response Text: {response.text}")  # Debug: print response text

        if response.status_code == 200:  # meaning the request was successful
            data = response.json()  # Converts the response from JSON format (JavaScript) into a Python dictionary for easier data manipulation.
            if data.get('Response') == "False":  # Check if the movie wasn't found
                return "Movie not found, please try again."

            # Extracts the movie data from the JSON response.
            movie_title = data['Title']
            description = data['Plot']

            return f"Movie: {movie_title}\nDescription: {description}"
        else:
            return f"Error fetching data, HTTP status code: {response.status_code}"  # for debug

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Function to handle user input and display movie info
def send():
    user_input = entry.get()  # Get user input
    movie_info = get_movie_info(user_input)  # Fetch movie info

    # Display the result in the chat box
    chat_box.insert(tk.END, f"You: {user_input}\n")
    chat_box.insert(tk.END, f"Bot: {movie_info}\n")

    # Scroll to the bottom of the chat box - to show the most recent messages
    chat_box.yview(tk.END)


# Function to start the conversation
def start_conversation():
    # Initial message asking for the movie
    chat_box.insert(tk.END, "Bot: Hello! Tell me the name of a movie, \n"
                            "and I will provide you with information about it!\n")
    chat_box.yview(tk.END)


# Create the main window
root = tk.Tk()
root.title("Movie Info Chatbot")
root.geometry("400x400")

# Create the chat box
chat_box = tk.Text(root, height=15, width=50)
chat_box.pack(pady=20)

# Create the input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create the send button
send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

# Start the conversation
start_conversation()

# Run the application
root.mainloop()
