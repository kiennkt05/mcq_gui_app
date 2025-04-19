# MCQ GUI Application

This project is a graphical user interface (GUI) application for displaying multiple-choice questions (MCQs). Users can interact with the application by clicking on their answers instead of using the terminal.

## Project Structure

```
mcq_gui_app
├── src
│   ├── main.py          # Entry point of the application
│   ├── mcq_reader.py    # Functions for reading MCQs from a file
│   └── assets
│       └── input.txt    # Input file containing MCQs
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:

   ```
   git clone <repository-url>
   cd mcq_gui_app
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required libraries using:

   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to start the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Upon running the application, users will see a window displaying a multiple-choice question.
- Click on the answer options (A, B, C, or D) to select your answer.
- The application will provide feedback on whether the selected answer is correct or not.
- After answering all questions, the application will display the total score.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
