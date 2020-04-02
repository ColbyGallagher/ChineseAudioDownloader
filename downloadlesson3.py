import requests

for i in range(12,21):
    url = "https://polyglot.sps.edu/audio/chinese/IntChineseLevel1Part1_3e/Lesson_03/2-{}.mp3".format(i)
    r = requests.get(url, allow_redirects=True)
    open("Lesson_03-2-{}.mp3".format(i),"wb").write(r.content)

for i in range(29,32):
    url = "https://polyglot.sps.edu/audio/chinese/IntChineseLevel1Part1_3e/Lesson_03/4-{}.mp3".format(i)
    r = requests.get(url, allow_redirects=True)
    open("Lesson_03-4-{}.mp3".format(i),"wb").write(r.content)