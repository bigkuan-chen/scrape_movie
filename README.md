# Movie Scraping Project & AI Assistant

An elegant, fully-featured movie catalog web application that crawls pages, exports structured data, and embeds an interactive AI chat assistant.

🚀 **Live Demo**: [https://scrape-movie.vercel.app/](https://scrape-movie.vercel.app/)

## Key Features
- 🕷️ **Crawl All Movies**: Overwrites the basic page 1 scraper to traverse all 10 pages of [Scrape Center (SSR1)](https://ssr1.scrape.center/) and fetch all 100 classic movies.
- 🖼️ **High-Resolution Media**: Automatically strips CDN compression parameters to download high-resolution posters and downsamples crisp local thumbnails.
- 📊 **Excel Integration**: Generates a custom-formatted `movies_with_posters.xlsx` spreadsheet containing the full metadata and compact poster thumbnails embedded directly in cell rows.
- ⚡ **FastAPI Backend**: Serves API data routes, direct Excel download paths, and host routes in Python.
- 🎨 **Premium UI**: Single Page Application styled with responsive vanilla CSS, featuring glassmorphism, fluid scaling, rating badges, search/filter panels, and light/dark theme toggles.
- 🤖 **Gemini 2.5 Flash AI Assistant**: Interactive floating chat widget allowing natural language conversation about the movie database, with graceful offline rules fallback.
- ☁️ **Vercel Serverless Ready**: Packaged configuration files for seamless Python ASGI deployment.

## Project Structure
- `scrape.py`: Crawls all pages and saves the combined HTML into `page1.html`.
- `parse_movies.py`: Parses the HTML and generates `movies.csv` and `movies.md`.
- `create_excel.py`: Downloads posters, generates thumbnails, and builds `movies_with_posters.xlsx`.
- `main.py`: FastAPI server handling endpoints, static mounts, and Gemini API chatbot logic.
- `vercel.json` & `requirements.txt`: Vercel serverless deployment specifications.
- `README.md`: This file, detailing the project and showing the compiled movie database.

## Getting Started Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Scrape & Parse Data**:
   ```bash
   python scrape.py
   python create_excel.py
   python parse_movies.py
   ```
3. **Configure API Key (Optional)**:
   Create a `.env` file in the root folder and add your Gemini key:
   ```env
   GEMINI_API_KEY=your-api-key-here
   ```
4. **Launch Server**:
   ```bash
   python -m uvicorn main:app --reload
   ```

## Scraped Movie List (Page 1-10)

| Poster | Chinese Title | English / Original Title | Categories | Regions / Countries | Duration | Release Date | Score |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| <img src="posters/resized/movie_1.jpg" width="40" alt="霸王别姬"> | [霸王别姬](https://ssr1.scrape.center/detail/1) | Farewell My Concubine | 剧情, 爱情 | 中国内地、中国香港 | 171 分钟 | 1993-07-26 | **9.5** |
| <img src="posters/resized/movie_2.jpg" width="40" alt="这个杀手不太冷"> | [这个杀手不太冷](https://ssr1.scrape.center/detail/2) | Léon | 剧情, 动作, 犯罪 | 法国 | 110 分钟 | 1994-09-14 | **9.5** |
| <img src="posters/resized/movie_3.jpg" width="40" alt="肖申克的救赎"> | [肖申克的救赎](https://ssr1.scrape.center/detail/3) | The Shawshank Redemption | 剧情, 犯罪 | 美国 | 142 分钟 | 1994-09-10 | **9.5** |
| <img src="posters/resized/movie_4.jpg" width="40" alt="泰坦尼克号"> | [泰坦尼克号](https://ssr1.scrape.center/detail/4) | Titanic | 剧情, 爱情, 灾难 | 美国 | 194 分钟 | 1998-04-03 | **9.5** |
| <img src="posters/resized/movie_5.jpg" width="40" alt="罗马假日"> | [罗马假日](https://ssr1.scrape.center/detail/5) | Roman Holiday | 剧情, 喜剧, 爱情 | 美国 | 118 分钟 | 1953-08-20 | **9.5** |
| <img src="posters/resized/movie_6.jpg" width="40" alt="唐伯虎点秋香"> | [唐伯虎点秋香](https://ssr1.scrape.center/detail/6) | Flirting Scholar | 喜剧, 爱情, 古装 | 中国香港 | 102 分钟 | 1993-07-01 | **9.5** |
| <img src="posters/resized/movie_7.jpg" width="40" alt="乱世佳人"> | [乱世佳人](https://ssr1.scrape.center/detail/7) | Gone with the Wind | 剧情, 爱情, 历史, 战争 | 美国 | 238 分钟 | 1939-12-15 | **9.5** |
| <img src="posters/resized/movie_8.jpg" width="40" alt="喜剧之王"> | [喜剧之王](https://ssr1.scrape.center/detail/8) | The King of Comedy | 剧情, 喜剧, 爱情 | 中国香港 | 85 分钟 | 1999-02-13 | **9.5** |
| <img src="posters/resized/movie_9.jpg" width="40" alt="楚门的世界"> | [楚门的世界](https://ssr1.scrape.center/detail/9) | The Truman Show | 剧情, 科幻 | 美国 | 103 分钟 | N/A | **9.0** |
| <img src="posters/resized/movie_10.jpg" width="40" alt="狮子王"> | [狮子王](https://ssr1.scrape.center/detail/10) | The Lion King | 动画, 歌舞, 冒险 | 美国 | 89 分钟 | 1995-07-15 | **9.0** |
| <img src="posters/resized/movie_11.jpg" width="40" alt="V字仇杀队"> | [V字仇杀队](https://ssr1.scrape.center/detail/11) | V for Vendetta | 剧情, 动作, 科幻, 惊悚 | 美国、英国、德国 | 132 分钟 | 2005-12-11 | **8.9** |
| <img src="posters/resized/movie_12.jpg" width="40" alt="少年派的奇幻漂流"> | [少年派的奇幻漂流](https://ssr1.scrape.center/detail/12) | Life of Pi | 剧情, 奇幻, 冒险 | 美国、中国台湾、英国、加拿大 | 127 分钟 | 2012-11-22 | **8.9** |
| <img src="posters/resized/movie_13.jpg" width="40" alt="美丽心灵"> | [美丽心灵](https://ssr1.scrape.center/detail/13) | A Beautiful Mind | 剧情, 传记 | 美国 | 135 分钟 | 2001-12-13 | **8.8** |
| <img src="posters/resized/movie_14.jpg" width="40" alt="初恋这件小事"> | [初恋这件小事](https://ssr1.scrape.center/detail/14) | สิ่งเล็กเล็กที่เรียกว่า...รัก | 喜剧, 爱情 | 泰国 | 118 分钟 | 2012-06-05 | **8.9** |
| <img src="posters/resized/movie_15.jpg" width="40" alt="借东西的小人阿莉埃蒂"> | [借东西的小人阿莉埃蒂](https://ssr1.scrape.center/detail/15) | 借りぐらしのアリエッティ | 动画, 奇幻, 冒险 | 日本 | 94 分钟 | 2010-07-17 | **8.8** |
| <img src="posters/resized/movie_16.jpg" width="40" alt="一一"> | [一一](https://ssr1.scrape.center/detail/16) | Yi yi: A One and a Two | 剧情, 爱情, 家庭 | 中国台湾、日本 | 173 分钟 | 2000-05-15 | **8.8** |
| <img src="posters/resized/movie_17.jpg" width="40" alt="美丽人生"> | [美丽人生](https://ssr1.scrape.center/detail/17) | La vita è bella | 战争, 剧情, 爱情 | 意大利 | 116 分钟 | 2020-01-03 | **9.1** |
| <img src="posters/resized/movie_18.jpg" width="40" alt="海上钢琴师"> | [海上钢琴师](https://ssr1.scrape.center/detail/18) | La leggenda del pianista sull'oceano | 剧情, 爱情, 音乐 | 意大利 | 126 分钟 | 2019-11-15 | **9.1** |
| <img src="posters/resized/movie_19.jpg" width="40" alt="千与千寻"> | [千与千寻](https://ssr1.scrape.center/detail/19) | 千と千尋の神隠し | 动画, 冒险, 奇幻, 家庭 | 日本 | 125 分钟 | 2019-06-21 | **9.1** |
| <img src="posters/resized/movie_20.jpg" width="40" alt="迁徙的鸟"> | [迁徙的鸟](https://ssr1.scrape.center/detail/20) | The Travelling Birds | 纪录片 | 法国、德国、意大利、西班牙、瑞士 | 98 分钟 | 2001-12-12 | **9.1** |
| <img src="posters/resized/movie_21.jpg" width="40" alt="黄金三镖客"> | [黄金三镖客](https://ssr1.scrape.center/detail/21) | Il buono, il brutto, il cattivo. | 西部, 冒险 | 意大利、西班牙、西德 | 161 分钟 | 1966-12-23 | **9.1** |
| <img src="posters/resized/movie_22.jpg" width="40" alt="海洋"> | [海洋](https://ssr1.scrape.center/detail/22) | Océans | 纪录片 | 法国、瑞士、西班牙、美国、阿联酋 | 104 分钟 | 2011-08-12 | **9.1** |
| <img src="posters/resized/movie_23.jpg" width="40" alt="我爱你"> | [我爱你](https://ssr1.scrape.center/detail/23) | 그대를 사랑합니다 | 剧情, 爱情 | 韩国 | 118 分钟 | 2011-02-17 | **9.1** |
| <img src="posters/resized/movie_24.jpg" width="40" alt="阿飞正传"> | [阿飞正传](https://ssr1.scrape.center/detail/24) | Days of Being Wild | 剧情, 爱情, 犯罪 | 中国香港 | 94 分钟 | 2018-06-25 | **9.1** |
| <img src="posters/resized/movie_25.jpg" width="40" alt="7号房的礼物"> | [7号房的礼物](https://ssr1.scrape.center/detail/36) | 7번방의 선물 | 剧情, 喜剧, 家庭 | 韩国 | 127 分钟 | 2013-01-23 | **8.8** |
| <img src="posters/resized/movie_26.jpg" width="40" alt="爱·回家"> | [爱·回家](https://ssr1.scrape.center/detail/25) | 집으로... | 剧情, 家庭 | 韩国 | 80 分钟 | 2002-04-05 | **9.1** |
| <img src="posters/resized/movie_27.jpg" width="40" alt="龙猫"> | [龙猫](https://ssr1.scrape.center/detail/26) | となりのトトロ | 动画, 冒险, 奇幻, 家庭 | 日本 | 86 分钟 | 2018-12-14 | **9.1** |
| <img src="posters/resized/movie_28.jpg" width="40" alt="七武士"> | [七武士](https://ssr1.scrape.center/detail/27) | 七人の侍 | 剧情, 动作, 冒险 | 日本 | 207 分钟 | 1954-04-26 | **8.8** |
| <img src="posters/resized/movie_29.jpg" width="40" alt="美国往事"> | [美国往事](https://ssr1.scrape.center/detail/28) | Once Upon a Time in America | 剧情, 犯罪 | 意大利、美国 | 229 分钟 | 2015-04-23 | **8.8** |
| <img src="posters/resized/movie_30.jpg" width="40" alt="完美的世界"> | [完美的世界](https://ssr1.scrape.center/detail/29) | A Perfect World | 剧情, 犯罪 | 美国 | 138 分钟 | 1993-11-24 | **8.8** |
| <img src="posters/resized/movie_31.jpg" width="40" alt="上帝之城"> | [上帝之城](https://ssr1.scrape.center/detail/30) | Cidade de Deus | 剧情, 犯罪 | 巴西、法国 | 130 分钟 | N/A | **8.8** |
| <img src="posters/resized/movie_32.jpg" width="40" alt="辩护人"> | [辩护人](https://ssr1.scrape.center/detail/31) | 변호인 | 剧情 | 韩国 | 127 分钟 | 2013-12-18 | **8.8** |
| <img src="posters/resized/movie_33.jpg" width="40" alt="忠犬八公物语"> | [忠犬八公物语](https://ssr1.scrape.center/detail/32) | ハチ公物語 | 剧情 | 日本 | 107 分钟 | 1987-08-01 | **8.8** |
| <img src="posters/resized/movie_34.jpg" width="40" alt="海豚湾"> | [海豚湾](https://ssr1.scrape.center/detail/33) | The Cove | 纪录片 | 美国 | 92 分钟 | 2009-07-31 | **8.8** |
| <img src="posters/resized/movie_35.jpg" width="40" alt="英雄本色"> | [英雄本色](https://ssr1.scrape.center/detail/34) | A Better Tomorrow | 剧情, 动作, 犯罪 | 中国香港 | 95 分钟 | 2017-11-17 | **8.8** |
| <img src="posters/resized/movie_36.jpg" width="40" alt="恐怖直播"> | [恐怖直播](https://ssr1.scrape.center/detail/35) | 더 테러 라이브 | 剧情, 悬疑, 犯罪 | 韩国 | 97 分钟 | 2013-07-31 | **8.8** |
| <img src="posters/resized/movie_37.jpg" width="40" alt="窃听风暴"> | [窃听风暴](https://ssr1.scrape.center/detail/37) | Das Leben der Anderen | 剧情, 悬疑 | 德国 | 137 分钟 | 2006-03-23 | **8.8** |
| <img src="posters/resized/movie_38.jpg" width="40" alt="时空恋旅人"> | [时空恋旅人](https://ssr1.scrape.center/detail/38) | About Time | 喜剧, 爱情, 奇幻 | 英国 | 123 分钟 | 2013-09-04 | **8.8** |
| <img src="posters/resized/movie_39.jpg" width="40" alt="穿条纹睡衣的男孩"> | [穿条纹睡衣的男孩](https://ssr1.scrape.center/detail/39) | The Boy in the Striped Pajamas | 剧情, 战争 | 英国、美国 | 94 分钟 | 2008-08-28 | **8.8** |
| <img src="posters/resized/movie_40.jpg" width="40" alt="教父"> | [教父](https://ssr1.scrape.center/detail/40) | The Godfather | 剧情, 犯罪 | 美国 | 175 分钟 | 2015-04-18 | **8.8** |
| <img src="posters/resized/movie_41.jpg" width="40" alt="萤火之森"> | [萤火之森](https://ssr1.scrape.center/detail/41) | 蛍火の杜へ | 剧情, 爱情, 动画, 奇幻 | 日本 | 45 分钟 | 2011-09-17 | **8.8** |
| <img src="posters/resized/movie_42.jpg" width="40" alt="素媛"> | [素媛](https://ssr1.scrape.center/detail/42) | 소원 | 剧情 | 韩国 | 123 分钟 | 2013-10-02 | **8.8** |
| <img src="posters/resized/movie_43.jpg" width="40" alt="小鞋子"> | [小鞋子](https://ssr1.scrape.center/detail/43) | بچههای آسمان | 剧情, 家庭 | 伊朗 | 89 分钟 | N/A | **8.8** |
| <img src="posters/resized/movie_44.jpg" width="40" alt="熔炉"> | [熔炉](https://ssr1.scrape.center/detail/44) | 도가니 | 剧情 | 韩国 | 125 分钟 | 2011-09-22 | **8.8** |
| <img src="posters/resized/movie_45.jpg" width="40" alt="大话西游之大圣娶亲"> | [大话西游之大圣娶亲](https://ssr1.scrape.center/detail/45) | A Chinese Odyssey Part Two - Cinderella | 喜剧, 爱情, 奇幻 | 中国香港、中国大陆 | 110 分钟 | 2014-10-24 | **8.9** |
| <img src="posters/resized/movie_46.jpg" width="40" alt="新龙门客栈"> | [新龙门客栈](https://ssr1.scrape.center/detail/46) | New Dragon Gate Inn | 动作, 爱情, 武侠, 古装 | 中国香港、中国大陆 | 88 分钟 | 2012-02-24 | **8.9** |
| <img src="posters/resized/movie_47.jpg" width="40" alt="触不可及"> | [触不可及](https://ssr1.scrape.center/detail/47) | Intouchables | 剧情, 喜剧 | 法国 | 112 分钟 | 2011-11-02 | **8.9** |
| <img src="posters/resized/movie_48.jpg" width="40" alt="钢琴家"> | [钢琴家](https://ssr1.scrape.center/detail/48) | The Pianist | 剧情, 音乐, 传记, 历史, 战争 | 法国、德国、英国、波兰 | 150 分钟 | 2002-05-24 | **8.9** |
| <img src="posters/resized/movie_49.jpg" width="40" alt="本杰明·巴顿奇事"> | [本杰明·巴顿奇事](https://ssr1.scrape.center/detail/49) | The Curious Case of Benjamin Button | 剧情, 爱情, 奇幻 | 美国 | 166 分钟 | 2008-12-25 | **8.9** |
| <img src="posters/resized/movie_50.jpg" width="40" alt="倩女幽魂"> | [倩女幽魂](https://ssr1.scrape.center/detail/50) | A Chinese Ghost Story | 爱情, 奇幻, 武侠, 古装 | 中国香港 | 98 分钟 | 2011-04-30 | **8.9** |
| <img src="posters/resized/movie_51.jpg" width="40" alt="哈利·波特与死亡圣器（下）"> | [哈利·波特与死亡圣器（下）](https://ssr1.scrape.center/detail/51) | Harry Potter and the Deathly Hallows: Part 2 | 剧情, 悬疑, 奇幻, 冒险 | 英国、美国 | 130 分钟 | 2011-08-04 | **8.9** |
| <img src="posters/resized/movie_52.jpg" width="40" alt="甜蜜蜜"> | [甜蜜蜜](https://ssr1.scrape.center/detail/52) | Comrades: Almost a Love Story | 剧情, 爱情 | 中国香港 | 118 分钟 | 2015-02-13 | **8.9** |
| <img src="posters/resized/movie_53.jpg" width="40" alt="蝙蝠侠：黑暗骑士崛起"> | [蝙蝠侠：黑暗骑士崛起](https://ssr1.scrape.center/detail/53) | The Dark Knight Rises | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国、英国 | 165 分钟 | 2012-08-27 | **8.9** |
| <img src="posters/resized/movie_54.jpg" width="40" alt="鬼子来了"> | [鬼子来了](https://ssr1.scrape.center/detail/54) | Devils on the Doorstep | 剧情, 战争 | 中国大陆 | 139 分钟 | 2000-05-13 | **8.8** |
| <img src="posters/resized/movie_55.jpg" width="40" alt="无敌破坏王"> | [无敌破坏王](https://ssr1.scrape.center/detail/55) | Wreck-It Ralph | 喜剧, 动画, 奇幻, 冒险 | 美国 | 101 分钟 | 2012-11-06 | **8.8** |
| <img src="posters/resized/movie_56.jpg" width="40" alt="致命魔术"> | [致命魔术](https://ssr1.scrape.center/detail/56) | The Prestige | 剧情, 悬疑, 惊悚 | 美国、英国 | 130 分钟 | 2006-10-17 | **8.8** |
| <img src="posters/resized/movie_57.jpg" width="40" alt="神偷奶爸"> | [神偷奶爸](https://ssr1.scrape.center/detail/57) | Despicable Me | 喜剧, 动画, 冒险 | 美国、法国 | 95 分钟 | 2010-06-20 | **8.8** |
| <img src="posters/resized/movie_58.jpg" width="40" alt="断背山"> | [断背山](https://ssr1.scrape.center/detail/58) | Brokeback Mountain | 剧情, 爱情, 家庭 | 美国、加拿大 | 134 分钟 | 2005-09-02 | **8.8** |
| <img src="posters/resized/movie_59.jpg" width="40" alt="怦然心动"> | [怦然心动](https://ssr1.scrape.center/detail/59) | Flipped | 剧情, 喜剧, 爱情 | 美国 | 90 分钟 | 2010-07-26 | **8.8** |
| <img src="posters/resized/movie_60.jpg" width="40" alt="驯龙高手"> | [驯龙高手](https://ssr1.scrape.center/detail/60) | How to Train Your Dragon | 喜剧, 动画, 奇幻, 冒险 | 美国 | 98 分钟 | 2010-05-14 | **8.8** |
| <img src="posters/resized/movie_61.jpg" width="40" alt="飞屋环游记"> | [飞屋环游记](https://ssr1.scrape.center/detail/61) | Up | 剧情, 喜剧, 动画, 冒险 | 美国 | 96 分钟 | 2009-08-04 | **8.8** |
| <img src="posters/resized/movie_62.jpg" width="40" alt="黑客帝国3：矩阵革命"> | [黑客帝国3：矩阵革命](https://ssr1.scrape.center/detail/62) | The Matrix Revolutions | 动作, 科幻 | 美国、澳大利亚 | 129 分钟 | 2003-11-05 | **8.8** |
| <img src="posters/resized/movie_63.jpg" width="40" alt="速度与激情5"> | [速度与激情5](https://ssr1.scrape.center/detail/63) | Fast Five | 动作, 犯罪 | 美国 | 130 分钟 | 2011-05-12 | **8.9** |
| <img src="posters/resized/movie_64.jpg" width="40" alt="勇敢的心"> | [勇敢的心](https://ssr1.scrape.center/detail/64) | Braveheart | 剧情, 动作, 传记, 历史, 战争 | 美国 | 177 分钟 | 1995-05-18 | **8.9** |
| <img src="posters/resized/movie_65.jpg" width="40" alt="三傻大闹宝莱坞"> | [三傻大闹宝莱坞](https://ssr1.scrape.center/detail/65) | 3 Idiots | 剧情, 喜剧, 爱情, 歌舞 | 印度 | 171 分钟 | 2011-12-08 | **8.9** |
| <img src="posters/resized/movie_66.jpg" width="40" alt="闻香识女人"> | [闻香识女人](https://ssr1.scrape.center/detail/66) | Scent of a Woman | 剧情 | 美国 | 157 分钟 | 1992-12-23 | **8.9** |
| <img src="posters/resized/movie_67.jpg" width="40" alt="末代皇帝"> | [末代皇帝](https://ssr1.scrape.center/detail/67) | The Last Emperor | 剧情, 传记, 历史 | 英国、意大利、中国大陆、法国、美国 | 163 分钟 | 1987-10-23 | **8.9** |
| <img src="posters/resized/movie_68.jpg" width="40" alt="风之谷"> | [风之谷](https://ssr1.scrape.center/detail/68) | 風の谷のナウシカ | 动画, 奇幻, 冒险 | 日本 | 117 分钟 | N/A | **8.9** |
| <img src="posters/resized/movie_69.jpg" width="40" alt="大话西游之月光宝盒"> | [大话西游之月光宝盒](https://ssr1.scrape.center/detail/69) | A Chinese Odyssey | 喜剧, 爱情, 奇幻, 古装 | 中国香港、中国大陆 | 87 分钟 | 2014-10-24 | **8.9** |
| <img src="posters/resized/movie_70.jpg" width="40" alt="放牛班的春天"> | [放牛班的春天](https://ssr1.scrape.center/detail/70) | Les choristes | 剧情, 音乐 | 法国、德国、瑞士 | 97 分钟 | 2004-10-16 | **8.9** |
| <img src="posters/resized/movie_71.jpg" width="40" alt="当幸福来敲门"> | [当幸福来敲门](https://ssr1.scrape.center/detail/71) | The Pursuit of Happyness | 剧情, 家庭, 传记 | 美国 | 117 分钟 | 2008-01-17 | **8.9** |
| <img src="posters/resized/movie_72.jpg" width="40" alt="幽灵公主"> | [幽灵公主](https://ssr1.scrape.center/detail/72) | もののけ姫 | 动画, 奇幻, 冒险 | 日本 | 134 分钟 | 1998-05-01 | **8.9** |
| <img src="posters/resized/movie_73.jpg" width="40" alt="十二怒汉"> | [十二怒汉](https://ssr1.scrape.center/detail/73) | 12 Angry Men | 剧情 | 美国 | 96 分钟 | 1957-04-13 | **8.9** |
| <img src="posters/resized/movie_74.jpg" width="40" alt="搏击俱乐部"> | [搏击俱乐部](https://ssr1.scrape.center/detail/74) | Fight Club | 剧情, 动作, 悬疑, 惊悚 | 美国、德国 | 139 分钟 | 1999-09-10 | **8.9** |
| <img src="posters/resized/movie_75.jpg" width="40" alt="疯狂原始人"> | [疯狂原始人](https://ssr1.scrape.center/detail/75) | The Croods | 喜剧, 动画, 冒险 | 美国 | 98 分钟 | 2013-04-20 | **8.9** |
| <img src="posters/resized/movie_76.jpg" width="40" alt="阿凡达"> | [阿凡达](https://ssr1.scrape.center/detail/76) | Avatar | 动作, 科幻, 冒险 | 美国、英国 | 162 分钟 | 2010-01-04 | **8.9** |
| <img src="posters/resized/movie_77.jpg" width="40" alt="哈尔的移动城堡"> | [哈尔的移动城堡](https://ssr1.scrape.center/detail/77) | ハウルの動く城 | 动画, 奇幻, 冒险 | 日本 | 119 分钟 | 2004-09-05 | **8.9** |
| <img src="posters/resized/movie_78.jpg" width="40" alt="盗梦空间"> | [盗梦空间](https://ssr1.scrape.center/detail/78) | Inception | 剧情, 科幻, 悬疑, 冒险 | 美国、英国 | 148 分钟 | 2010-09-01 | **8.9** |
| <img src="posters/resized/movie_79.jpg" width="40" alt="忠犬八公的故事"> | [忠犬八公的故事](https://ssr1.scrape.center/detail/79) | Hachi: A Dog's Tale | 剧情 | 美国、英国 | 93 分钟 | 2009-06-13 | **8.9** |
| <img src="posters/resized/movie_80.jpg" width="40" alt="拯救大兵瑞恩"> | [拯救大兵瑞恩](https://ssr1.scrape.center/detail/80) | Saving Private Ryan | 剧情, 历史, 战争 | 美国 | 169 分钟 | 1998-11-13 | **8.9** |
| <img src="posters/resized/movie_81.jpg" width="40" alt="活着"> | [活着](https://ssr1.scrape.center/detail/81) | To Live | 剧情, 家庭, 历史 | 中国大陆、中国香港 | 132 分钟 | 1994-05-17 | **9.0** |
| <img src="posters/resized/movie_82.jpg" width="40" alt="机器人总动员"> | [机器人总动员](https://ssr1.scrape.center/detail/82) | WALL·E | 喜剧, 科幻, 动画 | 美国 | 98 分钟 | 2008-06-27 | **9.0** |
| <img src="posters/resized/movie_83.jpg" width="40" alt="天堂电影院"> | [天堂电影院](https://ssr1.scrape.center/detail/83) | Nuovo Cinema Paradiso | 剧情, 爱情 | 意大利、法国 | 155 分钟 | 1988-11-17 | **9.0** |
| <img src="posters/resized/movie_84.jpg" width="40" alt="指环王2：双塔奇兵"> | [指环王2：双塔奇兵](https://ssr1.scrape.center/detail/84) | The Lord of the Rings: The Two Towers | 剧情, 动作, 奇幻, 冒险 | 美国、新西兰 | 179 分钟 | 2003-04-25 | **9.0** |
| <img src="posters/resized/movie_85.jpg" width="40" alt="指环王1：护戒使者"> | [指环王1：护戒使者](https://ssr1.scrape.center/detail/85) | The Lord of the Rings: The Fellowship of the Ring | 剧情, 动作, 奇幻, 冒险 | 新西兰、美国 | 178 分钟 | 2002-04-04 | **9.0** |
| <img src="posters/resized/movie_86.jpg" width="40" alt="射雕英雄传之东成西就"> | [射雕英雄传之东成西就](https://ssr1.scrape.center/detail/86) | The Eagle Shooting Heroes | 喜剧, 奇幻, 武侠, 古装 | 中国香港 | 113 分钟 | 1993-02-05 | **9.0** |
| <img src="posters/resized/movie_87.jpg" width="40" alt="蝙蝠侠：黑暗骑士"> | [蝙蝠侠：黑暗骑士](https://ssr1.scrape.center/detail/87) | The Dark Knight | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国、英国 | 152 分钟 | 2008-07-14 | **9.0** |
| <img src="posters/resized/movie_88.jpg" width="40" alt="无间道"> | [无间道](https://ssr1.scrape.center/detail/88) | Infernal Affairs | 剧情, 悬疑, 犯罪 | 中国香港 | 101 分钟 | 2003-09-05 | **9.0** |
| <img src="posters/resized/movie_89.jpg" width="40" alt="教父2"> | [教父2](https://ssr1.scrape.center/detail/89) | The Godfather: Part Ⅱ | 剧情, 犯罪 | 美国 | 202 分钟 | 1974-12-12 | **9.0** |
| <img src="posters/resized/movie_90.jpg" width="40" alt="加勒比海盗"> | [加勒比海盗](https://ssr1.scrape.center/detail/90) | Pirates of the Caribbean: The Curse of the Black Pearl | 动作, 奇幻, 冒险 | 美国 | 143 分钟 | 2003-11-21 | **9.0** |
| <img src="posters/resized/movie_91.jpg" width="40" alt="哈利·波特与魔法石"> | [哈利·波特与魔法石](https://ssr1.scrape.center/detail/91) | Harry Potter and the Sorcerer's Stone | 奇幻, 冒险 | 美国、英国 | 152 分钟 | 2002-01-26 | **9.0** |
| <img src="posters/resized/movie_92.jpg" width="40" alt="指环王3：王者无敌"> | [指环王3：王者无敌](https://ssr1.scrape.center/detail/92) | The Lord of the Rings: The Return of the King | 剧情, 动作, 奇幻, 冒险 | 美国、新西兰 | 201 分钟 | 2004-03-15 | **9.0** |
| <img src="posters/resized/movie_93.jpg" width="40" alt="黑客帝国"> | [黑客帝国](https://ssr1.scrape.center/detail/93) | The Matrix | 动作, 科幻 | 美国、澳大利亚 | 136 分钟 | 2000-01-14 | **9.0** |
| <img src="posters/resized/movie_94.jpg" width="40" alt="剪刀手爱德华"> | [剪刀手爱德华](https://ssr1.scrape.center/detail/94) | Edward Scissorhands | 剧情, 爱情, 奇幻 | 美国 | 105 分钟 | 1990-12-06 | **9.0** |
| <img src="posters/resized/movie_95.jpg" width="40" alt="春光乍泄"> | [春光乍泄](https://ssr1.scrape.center/detail/95) | Happy Together | 剧情, 爱情 | 中国香港、日本、韩国 | 96 分钟 | 1997-05-17 | **9.0** |
| <img src="posters/resized/movie_96.jpg" width="40" alt="大闹天宫"> | [大闹天宫](https://ssr1.scrape.center/detail/96) | The Monkey King | 动画, 奇幻 | 中国大陆 | 114 分钟 | 1965-12-31 | **9.0** |
| <img src="posters/resized/movie_97.jpg" width="40" alt="天空之城"> | [天空之城](https://ssr1.scrape.center/detail/97) | 天空の城ラピュタ | 动画, 奇幻, 冒险 | 日本 | 125 分钟 | 1992-05-01 | **9.0** |
| <img src="posters/resized/movie_98.jpg" width="40" alt="音乐之声"> | [音乐之声](https://ssr1.scrape.center/detail/98) | The Sound of Music | 剧情, 爱情, 歌舞, 传记 | 美国 | 174 分钟 | 1965-03-02 | **9.0** |
| <img src="posters/resized/movie_99.jpg" width="40" alt="辛德勒的名单"> | [辛德勒的名单](https://ssr1.scrape.center/detail/99) | Schindler's List | 剧情, 历史, 战争 | 美国 | 195 分钟 | 1993-11-30 | **9.5** |
| <img src="posters/resized/movie_100.jpg" width="40" alt="魂断蓝桥"> | [魂断蓝桥](https://ssr1.scrape.center/detail/100) | Waterloo Bridge | 剧情, 爱情, 战争 | 美国 | 108 分钟 | 1940-05-17 | **9.5** |
