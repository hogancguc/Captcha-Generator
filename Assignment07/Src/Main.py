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

from Src.Assignment07 import generate_captcha

def main():
    num_chars = 6
    filename = "captcha_image.png"

    captcha_image, captcha_string = generate_captcha(num_chars, filename)

    print("Captcha String: >", captcha_string, "<")

    captcha_image.show()

if __name__ == "__main__":
    main()