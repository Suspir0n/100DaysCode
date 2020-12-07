def verifyPasswordRule(password):
    if len(password) == 6:
        message = 'Valid password, save with success'
        return message is True
    elif len(password) > 6:
        message = 'Invalid password, this with more digits. The Correct is 6 digits'
        return message is False
    else:
        message = 'Invalid password, this with fewer digits. The Correct is 6 digits'
        return message is False