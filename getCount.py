import urllib2
import time
import pyglet
import sys


def find_between(s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return "Error"

while(1):
	req = urllib2.Request('https://www.facebook.com/CATReloaded')
	response = urllib2.urlopen(req)
	the_page = response.read()

	num = find_between(the_page,'<span class="_52id _50f5 _50f7">','<span')

	if(num >= '2000'):
		print "Yes"
		import pyglet
		foo=pyglet.media.load("beep.wav")
		foo.play()
		def exiter(dt):
			pyglet.app.exit()
		pyglet.clock.schedule_once(exiter, foo.duration)
		pyglet.app.run()
		break
		exit()
	else:
		time.sleep(60)
		