def filter_and_save_names():

    input_names = input("Enter names : ")

    names = [name.strip() for name in input_names.split(",")]

    filtered_names = sorted([
        name for name in names
        if name.lower().startswith('a') and len(name) > 3
    ])

    try:

        with open("names.txt", "w", encoding="utf-8") as file:
            for name in filtered_names:
                file.write(name)
            file.write(f"names saved: {len(filtered_names)}")


        print(f"File saved successfully with {len(filtered_names)} names.")

    except Exception as e:
        print("Error saving file:", e)



filter_and_save_names()
