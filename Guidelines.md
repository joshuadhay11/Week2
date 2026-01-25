Throughout the course you will be required to submit GitHub Repositories with your code in D2L.

Although it may not be called out in the assignment specifically, please consider these base requirements when submitting:

### 1) Include a header at the very top of your script

Include your name, date, and course name and course number

---

### 2) File Structure must be consistent with Python best practices.

Most assignments will already have the structure built for you, please make use of it for your projects.

It must be easy for anyone to find your script and any documents.

- Your scripts will be in either the `scripts/` or `src/` folder.  
- Your screenshots, output, or project reflections should go in your `docs/` folder.  
- Assets used will go in `assets/` or `images/` or something appropriately labeled like `dumps/`

Do not simply drop your adjustments at the root of your project. Keep it clean and organized.

---

### 3) When using 3rd Party Modules add `requirements.txt` at your root

Check out: [https://pip.pypa.io/en/stable/reference/requirements-file-format/](https://pip.pypa.io/en/stable/reference/requirements-file-format/) for details

---

### 4) Include and edit the ReadMe if needed

When running your script is not as simple as running a python file, make sure you include instructions.

---

### 5) Follow Python best practices when coding

Assignments may not specifically call out for you to use Python best practices but the following is expected in a higher level Python course. 

As a rule of thumb and at a minimum:

- Do not use absolute paths  
- Catch exceptions elegantly  
- Stop the script if an exception breaks it and provide reasonable feedback  
- Script should not crash at bad inputs  

Account for multiple test cases including, at a minimum:

- Data being too large to process  
- Data being too small to process  
- Data not existing  
- Data being misformatted  
- Data not being in right case (Capital vs Lower)  
- Data not always being consistently formatted  
- Data being formatted in more than one reasonable way  

For example, locations may be formatted like:  
- Tucson  
- Tucson, Arizona  
- Tucson, AZ  
- Tucson, Arizona USA  

Either call out a specific format that input must come in or account for reasonable cases.  

When it comes to testing number input think about how to handle:  
- Negative Numbers  
- Very Small Numbers  
- Huge Numbers  
- Zero  
- Non Digits or Symbols  
- Decimals, Integers, Floats - e or pi even  

Sanitize input reasonably  
- Remove trailing spaces  
- Remove unsupported/script breaking characters  

Never commit credentials or API Keys. Always use environment variables or secrets.

**Note:** Your scripts will be evaluated using both the provided test data and additional edge-case data to assess how well your code handles unexpected or extreme inputs.

The above are required as a minimum.

Please Note: There are many more Python best practices like:

- Testing  
- Using Type Hints  
- Creating example .env files  
- Using the logging module  

Feel free to implement them as you feel appropriate.

---

### 6) Use Comments

Add Comments when it is unclear what a snippet of code is doing or to explain your thought process and decisions.

---

### 7) Every Assignment Should Have Some Output Submitted

There must be evidence that your script ran appropriately attached to every assignment submission. This may be a screenshot, video recording, and/or csv. Sometimes it will be explicitly called out in the assignment. If it is not, include the best evidence at your discretion.

---

### 8) Never commit secrets to GitHub

As part of a secure best practice, you do not submit API Keys, Passwords, or any detail that you do not want the whole world to see. Secrets committed to GitHub will result in a steep penalty. Always use environment variables or other secrets management methods. Even prompting for a secret is better than having it in your code.

---

### 9) Always include the link to your GitHub Repo in your D2L Submission.

If you cannot access GitHub Classroom, create a new repository and invite your instructor to it for grading.

---

### 10) Call out AI Usage and/or any Copy Pasted Scripts/Code

With the exception of code already provided for you, you must include a source for any code that is copy-pasted or generated for you. Include comments with these citations in each line. If you do not call this out, it will be assumed all work submitted is your own. 

If you used a package or import something not discussed in the course or the examples, provide a detailed explanation as to why.
