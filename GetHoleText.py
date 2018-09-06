#抓取树洞中的帖子和回复内容
#爬太久会遇到问题，单个ip单次可以爬9页左右……
import functools
import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
filename = 'hole.txt'

@functools.lru_cache(maxsize=None)
def GetComment (pid):
    print("Processing "+ str(pid))
    headers = {'Host': 'www.pkuhelper.com'} # MUST add this!
    ans = requests.get("http://162.105.205.61/services/pkuhole/api.php?action=getcomment&pid=" + str(pid), headers=headers)
    try:
        ans = ans.json()
    except:
        print("Error!")
        return None
    return ans

def GetPost(startp,endp = None):
    print("Getting posts....")
    if (endp is None):
        endp = startp
    res = {}
    headers = {'Host': 'www.pkuhelper.com'} # MUST add this!
    for p in range(startp,endp+1):
        print("Processing page "+str(p))
        ans = requests.get("http://162.105.205.61/services/pkuhole/api.php?action=getlist&p=" + str(p), headers=headers)
        try:
            ans = ans.json()#不然会返回一个response类
        except:
            return res
        #print (ans)
        for answer in ans["data"]:
            tempdic = {}
            tempdic["post"] = answer["text"]
            comment = GetComment(answer["pid"])
            if(comment is None):
                continue
            temparray = []
            for reply in comment["data"]:
                temparray.append(reply["text"])
            tempdic["comment"] = temparray
            res[answer["pid"]] = tempdic
    return res

if __name__ == "__main__":
    res = GetPost(1,10)
    with open(filename,"w",encoding='UTF-8') as f:
        for key in res:
            f.write(res[key]["post"]+"\n")
            for reply in res[key]["comment"]:
                f.write(reply+"\n")

    f.close()
