🔐 Password Complexity Checker

This is a simple Python tool that checks the strength of a user's password based on specific security criteria. It provides real-time feedback to help users create stronger passwords.

---

✅ Features

- Checks if the password:
  - Has at least 10 characters
  - Contains uppercase letters
  - Contains lowercase letters
  - Includes at least one number
  - Includes at least one special character
- Gives helpful feedback if the password is weak
- Type 'exit' to quit the program

---

📌 How It Works

The program evaluates a password by assigning points for each of the following:
- Length ≥ 10 characters
- Contains uppercase letters (A–Z)
- Contains lowercase letters (a–z)
- Contains numbers (0–9)
- Contains special characters (!@#$%^&*(), etc.)

If the password scores 5 out of 5, it is considered strong.

---

▶ How to Run

1. Make sure Python is installed.
2. Open the file in VS Code or any code editor.
3. Run the script:



4. Enter passwords to test. Type exit to stop.

---

🧠 Example


hello123

 🔴 Weak password. Password should contain at least one uppercase letter. Password should contain at least one special  character.

Hello@1234

 ✅ Strong password! Keep it safe.


