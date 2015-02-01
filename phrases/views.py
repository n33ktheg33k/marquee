from django.shortcuts import render_to_response
from django.http import HttpResponse
from phrases.services import ScrollrDisplay
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from phrases.models import Phrase

def RunScrollr(request):
	ScrollrDisplay()
	return render_to_response('scrollr.html')

def GenImage(request):
	text = ""
	for phrase in Phrase.objects.all():
		text += phrase.phrase_text + "    "	

	

	font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)

	width, ignore = font.getsize(text)

	im = Image.new("RGB", (width + 30, 16), "black")
	draw = ImageDraw.Draw(im)

	x = 0;
	for phrase in Phrase.objects.all():
		t = phrase.phrase_text + "    "
		c = (phrase.color.red, phrase.color.green, phrase.color.blue)
		draw.text((x, 0), t, c, font=font)
		x = x + font.getsize(t)[0]

	im.save("/home/pi/display16x32/rpi-rgb-led-matrix/test.ppm")
	return render_to_response('scrollr.html')

