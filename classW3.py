has_acc=True
email_verified=False
email="zai@gmail"
can_login=has_acc and email_verified
is_email_valid="@" in email
user_age=17
is_age_valid=user_age>=18
can_login_final=has_acc and email_verified and is_email_valid and is_age_valid
print("You can't login because E-mail is not verified",can_login)
print("Is email valid:",is_email_valid)
print("Is age valid:",is_age_valid)
print("Final login status:",can_login_final)
if has_acc is True:
    print("You have an account.")
