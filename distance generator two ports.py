import requests
import bs4

def get_url(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
               'referer': 'http://ports.com/sea-route/',
               'Pragma': 'no-cache',
               'Host': 'ports.com',
               'X-Requested-With': 'XMLHttpRequest'}

    res = requests.get(url, headers=headers)
    
    return res


def get_num(city):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    url='http://ports.com/aj/findport/?q='+city
    print(url)
    res = requests.get(url, headers=headers)
    print(res.text)
    print(type(res.text))
    res=res.text

    res=res.splitlines()
    print(res)
    i=0
    while i < len(res):
        if res[i].find('Port of '+city)!= -1:
            res=res[i].split(sep='|',maxsplit=2)
        i+=1
   
    print(res)
    '''
    if res.find(city)!= -1:
        num=res[res.find('Singapore'):33]
        '''
    num=res[1]
    print(num)

    return num

def cal(city1,city2):
    

def main():
    port=['Piraeus','Barcelona','Bremerhaven','Gothenburg','Zeebrugge','Southampton',
          'Halifax','New York','Baltimore','Charleston','Brunswick','Miami','Manzanillo','Port Hueneme',
          'Yokohama','Kobe','Shanghai','Guangzhou','Laem Chabang','Singapore',
          'Auckland','Brisbane','Port Kembla','Melbourne','Fremantle']
    port=set(port)
    print(port)
    for city1 in port:
        for city2 in port:
            cal(city1,city2)
    city1 = 'Piraeus'
    #country2 = 'China'
    '''
    city2 ='Singapore'
    #country2 ='Singapore'
    '''
    city2 ='Barcelona'
    #country1 ='Singapore'
    
    num1 = get_num(city1)
    num2 = get_num(city2)
    host = 'http://ports.com/aj/sea-route/?'
    a= 'a=' + num1 + '&amp;'
    b= 'b=' + num2 + '&amp;'
    c= 'c=Port%20of%20' + city1 + ',%20' + '&amp;'
    d= 'd=Port%20of%20' + city2 + '&amp;'
    url = host+a+b+c+d
    #url = 'http://ports.com/aj/sea-route/?a=4595&amp;b=857&amp;c=Port%20of%20Shanghai,%20China&amp;d=Port%20of%20Singapore,%20Singapore'
    #'http://ports.com/aj/sea-route/?a=4595&amp;b=857&amp;c=Port%20of%20Shanghai,%20China&amp;d=Port%20of%20Singapore,%20Singapore'
    #'http://ports.com/aj/sea-route/?a=0&amp;b=0&amp;c=Port%20of%20New%20York&amp;d=Port%20of%20Shanghai'
    #input("请输入链接地址：")
    res = get_url(url)
    
    #print(res.text)
    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(res.text)
    
    t=res.json()
    #print(type(t))
    distance = t['cost']['nauticalmiles']
    twoport = t['title']
    print('Distance from '+ twoport + ' is ' + distance + ' nauticalmiles')
    result=[]
    for eacha in port:
        for eachb in port:
        result.extend(twoport + ' ' + distance + ' nauticalmiles')

    with open("distance.txt", "w", encoding="utf-8") as file:
        for each in result:
            file.write(each)
    
if __name__ == "__main__":
    main()

