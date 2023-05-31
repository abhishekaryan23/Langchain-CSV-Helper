# Chat with CSV Readme

This is a simple Streamlit application that allows users to upload a CSV file and ask questions related to the document. The application uses the `streamlit` library for the user interface and the `get_answer_csv` function from the `src.utils` module to process the uploaded file and provide answers to the user's questions.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`

2. Copy the code provided into a Python file, for example, `app.py`.

3. Run the application using the command `streamlit run app.py`.

4. Once the application is running, you can access it in your web browser at `http://localhost:8501`.

5. Upload a CSV file by clicking on the "Upload a csv file" button and selecting a file from your local machine.

6. Type your question in the text area provided and click the "Submit" button to get an answer related to the document.

7. The answer will be displayed below the question.

8. The uploaded file is saved temporarily as `temp.csv` for processing. After getting the answer, the temporary file is removed.

Note: Make sure you have the necessary permissions to write files in the directory where the application is running.

## Requirements

- Python 3.9+
- Streamlit
- Other dependencies specified in the `requirements.txt` file, if any

## Credits

The `get_answer_csv` function used in this application is defined in the `src.utils` module. Make sure to check and modify the implementation of this function according to your requirements.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as needed.
