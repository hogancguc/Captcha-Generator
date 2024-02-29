# Name: Cameron Hogan
# email: hogancg@mail.uc.edu
# Assignment Number: Assignment 07
# Due Date: 2/29/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Adding parameters to customize captcha generator.
# Brief Description of what this module does: Contains functions for generating random strings of numbers and letters, drawing random shapes, and saving the captcha image to a file.
# Citations:
# Anything else that's relevant:
'''
Created on Feb 26, 2020

@author: nicomp
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    """
    Generate a random string of numbers and letters.
    
    Args:
        length (int): Length of the random string.
    
    Returns:
        str: Random string of numbers and letters.
    """
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    """
    Draw a random ellipse on the image.
    
    Args:
        draw (PIL.ImageDraw.Draw): Drawing context.
    """
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha(num_chars, filename):
    """
    Generate a captcha image with a random string of numbers and letters.
    
    Args:
        num_chars (int): Number of characters in the captcha string.
        filename (str): Filename where the captcha should be stored.
    
    Returns:
        tuple: A tuple containing the captcha image and the captcha string.
    """
    if not 6 <= num_chars <= 10:
        raise ValueError("Number of characters should be between 6 and 10.")

    captcha_string = generate_random_string(num_chars)
    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)

    fontStyle = ImageFont.truetype("Aaargh.ttf", 48)

    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    for letter in captcha_string:
        draw.text((x, y), letter, (0,0,0),font=fontStyle)
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    
    captcha_image.save(filename)

    return (captcha_image, captcha_string)