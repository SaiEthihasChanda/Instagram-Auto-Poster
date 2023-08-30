from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap
import time
import shutil

from instabot import Bot





while True:
    folder_path = "config"

    try:
        shutil.rmtree(folder_path)
        print(f"{folder_path} has been deleted.")
    except FileNotFoundError:
        print(f"{folder_path} does not exist.")
    bot = Bot()

    with open('qoutes.txt', 'r') as file:
        quotes = file.readlines()
    quotes = [quote.strip() for quote in quotes]
    random_quote = random.choice(quotes)
    # Get the current working directory

    line_to_delete = random_quote

    # Read the content of the file and store the lines to keep
    lines_to_keep = []
    with open('qoutes.txt', 'r') as file:
        for line in file:
            if line.strip() != line_to_delete:
                lines_to_keep.append(line)

    # Rewrite the file with the lines you want to keep
    with open('qoutes.txt', 'w') as file:
        file.writelines(lines_to_keep)

    current_directory = os.getcwd()

    image_extensions = ['.jpg', '.jpeg']
    image_files = [file for file in os.listdir(current_directory) if any(file.lower().endswith(ext) for ext in image_extensions)]

    if image_files:
        random_image_filename = random.choice(image_files)
        random_image_path = os.path.join(current_directory, random_image_filename)
        print("Selected random image:", random_image_path)
    else:
        print("No image files found in the directory.")

    imgObject = Image.open(random_image_path)


    img_width, img_height = imgObject.size
    center_x = img_width // 2
    center_y = img_height // 2


    max_font_size = min(img_width, img_height) // 10

    font_size = max_font_size
    font = ImageFont.truetype("KaushanScript-Regular.ttf", font_size)


    while font.getsize_multiline(random_quote, spacing=10)[0] > img_width or font.getsize_multiline(random_quote, spacing=10)[1] > img_height:
        font_size -= 1
        font = ImageFont.truetype("KaushanScript-Regular.ttf", font_size)

        random_quote = textwrap.fill(random_quote, width=20)

    drawing_object = ImageDraw.Draw(imgObject)


    text_width, text_height = drawing_object.textsize(random_quote, font=font)
    text_x = center_x - text_width // 2
    text_y = center_y - text_height // 2

    drawing_object.multiline_text((text_x, text_y), random_quote, font=font, fill=(0, 0, 0), spacing=10)

    output_image_path = 'today.jpg'
    imgObject.save(output_image_path)
    print("Image saved as:", output_image_path)

    img_path = 'today.jpg'
    img = Image.open(img_path)

    # Calculate new dimensions for 4:5 aspect ratio
    img_width, img_height = img.size
    target_aspect_ratio = 4 / 5
    new_height = int(img_width * target_aspect_ratio)


    resized_img = img.resize((img_width, new_height), Image.LANCZOS)


    resized_img.save('today.jpg')

    bot.login(username="spamacct3007", password="5193703@NTS3007")
    bot.upload_photo("today.jpg", caption="Happy Programming!")

    file_path = 'today.jpg'

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    else:
        print(f"File '{file_path}' not found.")
    time.sleep(300)



