#sa salvam imagini cu caini intr-un pdf

import image_functions as image_func
import pdf_functions as pdf

MENU = """
1. SAVE RANDOM IMAGE
2. SHOW ALL IMAGES
3. SAVE IMAGES TO PDF
4. DELETE ALL IMAGES
"""


if __name__ == '__main__':
    config = image_func.read_config()

    while True:
        user_pick = input(MENU)

        match user_pick:
            case "1":
                random_image_dict = image_func.get_dog_image(config['url_dog_images'])
                content = image_func.download_dog_image(random_image_dict['message'])
                image_func.save_dog_image(content)
            case "2":
                image_func.show_all_images()
            case "3":
                pdf.create_pdf("test.pdf")
            case "4":
                pass



