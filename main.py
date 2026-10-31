def check_password_strength(password):
  score = 0
  feedback = []

  # 1. Length Check
  if len(password) >= 8:
    score += 1
  else:
    feedback.append("❌ Password must be at least 8 characters long.")

  # 2. Number Check
  has_number = any(char.isdigit() for char in password)
  if has_number:
    score += 1
  else:
    feedback.append("❌ Must contain at least one number (0-9).")

  # 3. Uppercase Check
  has_upper = any(char.isupper() for char in password)
  if has_upper:
    score += 1
  else:
    feedback.append("❌ Must contain at least one uppercase letter (A-Z).")

  # 4. Special Character Check
  special_chars = "!@#$%^&*(),.?\":{}|<>"
  has_special = any(char in special_chars for char in password)
  if has_special:
    score += 1
  else:
    feedback.append("❌ Must contain at least one special character (!@#$%^&*).")

  # Final Result Based on Score
  print("\n--- Analysis Result ---")
  if score == 4:
    return (
        "🟢 Strong: Perfect! Your password is secure and highly secure."
    )
  elif score == 3:
    return (
        "🟡 Medium: Good password, but you can make it stronger by fixing the"
        f" following:\n"
        + "\n".join(feedback)
    )
  else:
    return (
        "🔴 Weak: Your password is weak. Please fix these issues:\n"
        + "\n".join(feedback)
    )


# Program execution loop
print("*** Welcome to Smart Password Strength Checker ***")
while True:
  user_password = input(
      "\nEnter your password to check (or type 'exit' to quit): "
  )
  if user_password.lower() == "exit":
    print("Exiting... Goodbye!")
    break

  result = check_password_strength(user_password)
  print(result)