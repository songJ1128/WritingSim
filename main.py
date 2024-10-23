import pyautogui
import random
import time

delay_char = [0.04, 0.05, 0.06,0.07,0.08,0.09, 0.1,0.12,0.14,0.16,0.19, 0.2,0.24,0.26, 0.3]
delay_sentence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
delay_paragraph = [10, 20, 30, 60, 120, 180, 240]

def get_incorrect_word(correct_word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    incorrect_length = random.randint(1, min(4, len(correct_word))) 
    incorrect_word = ''.join(random.choice(alphabet) for i in range(incorrect_length))
    return incorrect_word


def simulate_typing(text):
    time.sleep(30)  
    for word in text.split(): 
        for char in word + ' ':
            if char == '.':
                time.sleep(random.choice(delay_sentence)) 
            if char == '\n':
                time.sleep(random.choice(delay_paragraph))   
            if random.random() < 0.1: 
                incorrect_word = get_incorrect_word(word)  
                pyautogui.typewrite(incorrect_word) 
                time.sleep(random.choice(delay_char)) 
                for _ in range(len(incorrect_word)):
                    pyautogui.press('backspace')
                time.sleep(random.choice(delay_char))
            pyautogui.typewrite(word + ' ') 
            time.sleep(random.choice(delay_char))

if __name__ == "__main__":
    file_path = input("Enter file path ")
    
    try:
        with open(file_path, 'r') as file:
            text_to_type = file.read()
    except FileNotFoundError:
        print("no file")
        exit()
    
    print("Switch to the window where you want the text to be written within 30 secs and click where you want it to be written")
    simulate_typing(text_to_type)

    