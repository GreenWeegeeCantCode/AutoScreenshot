# AutoScreenshot
Simple screenshotting tool that uses ShareX to make PFA nolags easily!

# How to use
First, make sure you have Share installed.
In ShareX set the capture entire screen hotkey to Shift + Alt + S.
Then, open PFA, load the midi you wanna nolag, pause and make sure the right key is set to move by 1/60th of a second.
After that, open the .py file in something like VS Code, here you can configure it a bit such as changing the delay and the screenshot key.
When you run it, open PFA and wait for it to finish.

I recommend setting the file naming in ShareX to "%i{5}" so you can turn the frames into a video using FFmpeg.

# Configuring delay
To change the delay, change the number in time.sleep(1) to whatever you want, you can make it something like 0.5, 0.2, 2, ect.
