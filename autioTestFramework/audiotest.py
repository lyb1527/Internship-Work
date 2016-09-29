import subprocess 
import os
import xml.dom.minidom as dom
import re


xmldoc = dom.parse('audio.xml')
hooks = xmldoc.getElementsByTagName('hook')
for hook in hooks: 
	executable = hook.getElementsByTagName('executable')
	hk = hook.getElementsByTagName('command')[0].childNodes[0].data
	hk = str(hk)
	
	if hk == 'audio_probe.sh':
		os.system("./" + hk + ">" "probe.log")

	if hk == 'audio_fetch.sh':
		os.system("./" + hk + ">" "fetch.log")
	

	result = subprocess.check_output('./' + 'audio_adjust.sh', shell=True)	
	global device
	device = result.split('=')[1]


testdoc= dom.parse('audio_test.xml')
morehooks = testdoc.getElementsByTagName('hook')
for hook in morehooks: 
	executable = hook.getElementsByTagName('executable')
	hk=hook.getElementsByTagName('command')[0].childNodes[0].data
	if hk == "audio.stf":
		os.system('./' + hk + " " + device + '>' 'result.log')

subprocess.Popen(['sh', 'audio_clean.sh'])       
