# -*- coding: utf-8 -*-

class transCookie:
	def __init__(self, cookie):
	    self.cookie = cookie

	def stringToDict(self):
	    '''
	    将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
	    :return:
	    '''
	    itemDict = {}
	    items = self.cookie.split(';')
	    for item in items:
	        key = item.split('=')[0].replace(' ', '')
	        value = item.split('=')[1]
	        itemDict[key] = value
	    return itemDict

if __name__ == "__main__":
	cookie = "_T_WM=9488922b79b3a5c3466d62922c80f1b7; SCF=Ar6mKqdSjw_f79qLBBjBLs6S6S6SDlWx9ze7ChlzRfJvpiaTjPwrypZTJTk2bgxV0pNfhoFQE9rmvYf49eOjRuI.; MLOGIN=1; SUB=_2A252MkZTDeRhGeVO6VcS9C_Fwj2IHXVV3WobrDV6PUJbkdANLWH4kW1NTT97o0S9jV9VDJZyn8Cpt-19JCDGJSnI; SUHB=0D-FxxuvyDw4t1; SSOLoginState=1530279427; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D20000174%26lfid%3Dhotword"
	trans = transCookie(cookie)
	print(trans.stringToDict())
