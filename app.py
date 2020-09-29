from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


image = ImageCaptcha(width = 280, height = 90)
data = image.generate('1234')
image.write('1234', 'out.png')



audio = AudioCaptcha()
data = audio.generate('1234')
audio.write('1234', 'out.wav')
