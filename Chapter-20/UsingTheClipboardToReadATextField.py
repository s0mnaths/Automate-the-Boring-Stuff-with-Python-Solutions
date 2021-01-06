import pyautogui,pyperclip

window=pyautogui.getWindowsWithTitle('Visual Studio Code')
left=int(window.left)+100
top=int(window.top)+100
window.activate()
pyautogui.click(left+top)

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

text=pyperclip.paste()
print(text)