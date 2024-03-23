# Google Form Auto Submitter

This Python script automates the process of submitting a Google Form multiple times. It utilizes Selenium for web scraping and threading for concurrent submissions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/username/google-form-auto-submitter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd google-form-auto-submitter
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up a Google Form to be submitted.

2. Modify the `form_url` variable in the `submit_form.py` file to point to your Google Form URL.

3. Run the script:

   ```bash
   python submit_form.py
   ```

4. Follow the prompts to configure the script and start submitting forms.

## Features

- **Automated Form Submission:** The script automates the process of filling out and submitting a Google Form multiple times.
- **Concurrency:** Utilizes threading to submit multiple forms concurrently, speeding up the submission process.
- **Question Identification:** Identifies the nature of each question in the form (e.g., multiple-choice, short answer, paragraph) before starting submissions.
- **Headless Browsing:** Uses headless Chrome to perform form submissions without displaying the browser window.

## Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

Please make sure to follow the code of conduct and maintain a clean commit history.
