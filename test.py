# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


import os
#import rich
import requests
#import youtube_transcript_api as yta

import youtube_transcript_api as yta 

def main():
    print("Hello from yttst!")
    j  = yta.YouTubeTranscriptApi()
    video_id = "WXsD0ZgxjRw"
    ss = j.list(video_id)
    kk = j.fetch(video_id) #, languages=["hi"])
    km = j.fetch(video_id)
    jm = j.fetch(video_id).to_raw_data()

    print(km)
    print(ss)#.list())
   # o = j.list()
    i = 0
    jj=iter(kk)
#    print(type(i in km))
    while i <15:
        print(next(jj))
        i+=1

    print(jm)
    print(type(jm))
    print(str(type(jm)))
    oo = []
    """
    for i in jm:
        
        oo.append(jm["text"])
    """
    print(jm[1]['text'])
    
    with open("1.txt","w+", encoding="utf-8") as f:
      #  f.write(str(jm['text'][:15]))
        f.write(oo)
        f.close()

    os.system("notepad.exe 1.txt")

 #   for i in 
 #   print(type(str(ss)))
#
"""
    with open('h.txt', 'w') as f:
        f.write(ss)
        f.close()
    
    os.system("notepad.exe h.txt")
"""
    

"""
approach fpr youtube api based library, nd also do something for the ip blovkinh...:
fucntiosn to be defined to get the anscript only, nd that too in the desired language, obiv after searcing for it otherwise using gemni api for keys and all. chapter based approach wud be part of the AI fine tunning and programming..


"""

if __name__ == "__main__":
    main()
