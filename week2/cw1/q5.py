def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds %= 60
    return f"{hours}:{minutes}:{seconds}"

print(convert_seconds(3690))