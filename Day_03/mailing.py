# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:47:33 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      We need to copy both the new and old list in your solution .py file
      
"""

old_list = ["janusfury@aol.com",
"ajlitt@me.com",
"dburrows@me.com",
"robles@yahoo.com",
"jshirley@gmail.com",
"saridder@live.com",
"dmiller@mac.com",
"agapow@yahoo.ca",
"hamilton@sbcglobal.net",
"madler@att.net",
"grady@gmail.com",
"iami@gmail.com",
"heroine@gmail.com",
"loxy@att.net",
"violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]


new_list = ["violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]

list1=[]
for i in old_list:
    if i not in new_list:
        list1.append(i)
    else:
        pass
    
print(list1)

