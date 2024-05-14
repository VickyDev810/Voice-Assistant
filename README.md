## Voice Assistant

Voice Assistant is a simple yet powerful voice recognition application designed to assist you with various tasks using voice commands. With Voice Assistant, you can effortlessly open applications, perform Google searches, play commands, and much more, all through intuitive voice input.

## Features

- **Interactive UI**: Voice Assistant comes with a user-friendly tkinter-based graphical user interface (GUI).
- **Voice Recognition**: Recognizes voice commands using the Google Speech Recognition API.
- **Application Opener**: Opens applications installed on the system.
- **Google Search**: Performs Google searches based on voice commands.
- **Play Command**: Executes commands to play media or perform specific tasks.
- **Command Playback**: Control media playback or perform specific actions by simply speaking your command.

## User Interface
Voice Assistant comes with a user-friendly tkinter-based graphical user interface (GUI) that provides a seamless experience for interacting with the assistant. The UI presents easy-to-use buttons and input fields, making it convenient for users to input voice commands and receive responses from the 
assistant.

## Getting Started

1. Users must have python installed in there PC: [Download Python](https://www.python.org/downloads/)

2. **Clone the repositry**
```sh
git clone https://github.com/VickyDev810/Voice-Assistant.git  
cd Voice-Assistant
```

3. **Create a virtual environment** (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. Install required packages:
```sh
pip install -r requirements.txt
```

5. Run the application:
```sh
python -u main.py
```

## Usage

1. ### Using the Mic Button
 On clicking on the mic button, you will be prompted to say something on terminal then you can speak any query:

i. **Searching Query**
The Voice Assistant will search for anything you say. For example, if you say "hello," it will be searched online.

ii. **Open Application**
This feature works only for a few apps that are defined in your OS path. Some example commands are:
 ```sh
 open calc
 open notepad
 open explorer
 open spotify works when you have spotify installed from microsoft store
 open cmd ( This command may cause errors as it will open the cmd in vs code terminal itself)
 ```
#### Note: May not work on MAC

iii. **Play Command**
You can use these commands to play videos on YouTube or search for them:
```sh
play 'Video Name'
```

Opens up a video defined by user when prompted you can change it inside play_command.py
```sh
play song or play a song or play something
```

2. ### Using the Search Box 
You can also simply type the query in the textbox and click the search button to perform a Google search or execute a command.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Glimpse of UI

![image](https://github.com/VickyDev810/Voice-Assistant/assets/142140937/9af4515b-17f5-4620-a4e8-be00f355b328)

