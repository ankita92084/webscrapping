    from bs4 import BeautifulSoup
    from task1 import adventure_movie
    # list3=scrape_top_list()
    import requests
    import json
    import os.path
    import time

    def scrape_movie_details(movie_url):
        movie_id=''
        for id in movie_url[27]:
            if '/' not in id:
                movie_id+=id
                # print(movie_id)
            else:
                break
        file_name=movie_id+'.json'
        text=None
        if os.path.exists('data/movie details/'+file_name):
            f=open('data/movie details/'+file_name)
            text=f.read()
            # print(text)
            return text
        # if text is None:
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")
        title_div=soup.find("ul",class_="content-meta info")
        sub_title_div=title_div.find_all("li",class_="meta-row clearfix")
        movie_dic={}
        name=soup.find("h1",class_="scoreboard__tittle")
        # print(name)
        movie_dic.update({"Movie Name":name})
        for i in sub_title_div:
            key=i.find("div",class_="meta-label subtle").get_text()
            # print(key)
            value=(i.find("div",class_="meta-value").text.replace(" "," ").replace("\n","").strip())
            movie_dic.update({key:value})
            print(movie_dic)
        # with open("task8.json","w")as file:
        with open('detail_of_one.json','w')as file:
                json.dump(movie_dic,file,indent=2)
    scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")

