import re
import xml.etree.ElementTree as ET

newFile = open("mdb.csv", "w", encoding="UTF-8")
newFile.write("mid,title,diff1,diff1lvl,diff2,diff2lvl,diff3,diff3lvl,diff4,diff4lvl,diff5,diff5lvl\n")

with open('O:\\rhythmGames\sdvx5eg\contents\data\others\music_db.xml','r') as mdb:
    root = ET.fromstring(mdb.read())
    i = 0
    for child in root:
        mid = root[i].get('id')
        title = root[i][0][1].text
        difficulty = root[i][1]

        diff1 = difficulty[0].tag
        diff1lvl = difficulty[0][0].text
        diff2 = difficulty[1].tag
        diff2lvl = difficulty[1][0].text
        diff3 = difficulty[2].tag
        diff3lvl = difficulty[2][0].text
        diff4 = difficulty[3].tag
        diff4lvl = difficulty[3][0].text
        try:
            difficulty[4]
        except:
            diff5 = 0
            diff5lvl = 0
        else:
            diff5 = difficulty[4].tag
            diff5lvl = difficulty[4][0].text
            

        newFile.write(f'{mid},"{title}",{diff1},{diff1lvl},{diff2},{diff2lvl},{diff3},{diff3lvl},{diff4},{diff4lvl},{diff5},{diff5lvl}\n')
        i = i + 1


#<mdb>
#   <music id="n">[n-1]
#       <info> [0]
#           <title_name> [1]
#       <difficulty> [1]  
#           <novice> [0]
#               <difnum __type="u8"> [0]    [i][1][0][0]
#           <advanced> [1]
#               <difnum __type="u8"> [0]    [i][1][1][0]
#           <exhaust> [2]
#               <difnum __type="u8"> [0]    [i][1][2][0]
#           <infinite> [3]
#               <difnum __type="u8"> [0]    [i][1][3][0]
