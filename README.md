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
| <img src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg" width="40" alt="霸王别姬"> | [霸王别姬](https://ssr1.scrape.center/detail/1) | Farewell My Concubine | 剧情, 爱情 | 中国内地、中国香港 | 171 分钟 | 1993-07-26 | **9.5** |
| <img src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg" width="40" alt="这个杀手不太冷"> | [这个杀手不太冷](https://ssr1.scrape.center/detail/2) | Léon | 剧情, 动作, 犯罪 | 法国 | 110 分钟 | 1994-09-14 | **9.5** |
| <img src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg" width="40" alt="肖申克的救赎"> | [肖申克的救赎](https://ssr1.scrape.center/detail/3) | The Shawshank Redemption | 剧情, 犯罪 | 美国 | 142 分钟 | 1994-09-10 | **9.5** |
| <img src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg" width="40" alt="泰坦尼克号"> | [泰坦尼克号](https://ssr1.scrape.center/detail/4) | Titanic | 剧情, 爱情, 灾难 | 美国 | 194 分钟 | 1998-04-03 | **9.5** |
| <img src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg" width="40" alt="罗马假日"> | [罗马假日](https://ssr1.scrape.center/detail/5) | Roman Holiday | 剧情, 喜剧, 爱情 | 美国 | 118 分钟 | 1953-08-20 | **9.5** |
| <img src="https://p0.meituan.net/movie/da64660f82b98cdc1b8a3804e69609e041108.jpg" width="40" alt="唐伯虎点秋香"> | [唐伯虎点秋香](https://ssr1.scrape.center/detail/6) | Flirting Scholar | 喜剧, 爱情, 古装 | 中国香港 | 102 分钟 | 1993-07-01 | **9.5** |
| <img src="https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg" width="40" alt="乱世佳人"> | [乱世佳人](https://ssr1.scrape.center/detail/7) | Gone with the Wind | 剧情, 爱情, 历史, 战争 | 美国 | 238 分钟 | 1939-12-15 | **9.5** |
| <img src="https://p0.meituan.net/movie/1f0d671f6a37f9d7b015e4682b8b113e174332.jpg" width="40" alt="喜剧之王"> | [喜剧之王](https://ssr1.scrape.center/detail/8) | The King of Comedy | 剧情, 喜剧, 爱情 | 中国香港 | 85 分钟 | 1999-02-13 | **9.5** |
| <img src="https://p0.meituan.net/movie/8959888ee0c399b0fe53a714bc8a5a17460048.jpg" width="40" alt="楚门的世界"> | [楚门的世界](https://ssr1.scrape.center/detail/9) | The Truman Show | 剧情, 科幻 | 美国 | 103 分钟 | N/A | **9.0** |
| <img src="https://p0.meituan.net/movie/27b76fe6cf3903f3d74963f70786001e1438406.jpg" width="40" alt="狮子王"> | [狮子王](https://ssr1.scrape.center/detail/10) | The Lion King | 动画, 歌舞, 冒险 | 美国 | 89 分钟 | 1995-07-15 | **9.0** |
| <img src="https://p1.meituan.net/movie/06ec3c1c647942b1e40bca84036014e9490863.jpg" width="40" alt="V字仇杀队"> | [V字仇杀队](https://ssr1.scrape.center/detail/11) | V for Vendetta | 剧情, 动作, 科幻, 惊悚 | 美国、英国、德国 | 132 分钟 | 2005-12-11 | **8.9** |
| <img src="https://p0.meituan.net/movie/34998e31c6d07475f1add6b8b16fd21d192579.jpg" width="40" alt="少年派的奇幻漂流"> | [少年派的奇幻漂流](https://ssr1.scrape.center/detail/12) | Life of Pi | 剧情, 奇幻, 冒险 | 美国、中国台湾、英国、加拿大 | 127 分钟 | 2012-11-22 | **8.9** |
| <img src="https://p0.meituan.net/movie/7b7d1f8aa36d7a15463ce6942708a1a7265296.jpg" width="40" alt="美丽心灵"> | [美丽心灵](https://ssr1.scrape.center/detail/13) | A Beautiful Mind | 剧情, 传记 | 美国 | 135 分钟 | 2001-12-13 | **8.8** |
| <img src="https://p1.meituan.net/movie/05bc2f0ccf97aacfa64fcac4f237cf8082385.jpg" width="40" alt="初恋这件小事"> | [初恋这件小事](https://ssr1.scrape.center/detail/14) | สิ่งเล็กเล็กที่เรียกว่า...รัก | 喜剧, 爱情 | 泰国 | 118 分钟 | 2012-06-05 | **8.9** |
| <img src="https://p1.meituan.net/movie/640cc32445df972b066c9a04b194da141104515.jpg" width="40" alt="借东西的小人阿莉埃蒂"> | [借东西的小人阿莉埃蒂](https://ssr1.scrape.center/detail/15) | 借りぐらしのアリエッティ | 动画, 奇幻, 冒险 | 日本 | 94 分钟 | 2010-07-17 | **8.8** |
| <img src="https://p0.meituan.net/movie/6cb23356f9d8e0b506349561c633310d102189.jpg" width="40" alt="一一"> | [一一](https://ssr1.scrape.center/detail/16) | Yi yi: A One and a Two | 剧情, 爱情, 家庭 | 中国台湾、日本 | 173 分钟 | 2000-05-15 | **8.8** |
| <img src="https://p1.meituan.net/movie/580d81a2c78bf204f45323ddb4244b6c6821175.jpg" width="40" alt="美丽人生"> | [美丽人生](https://ssr1.scrape.center/detail/17) | La vita è bella | 战争, 剧情, 爱情 | 意大利 | 116 分钟 | 2020-01-03 | **9.1** |
| <img src="https://p0.meituan.net/movie/609e45bd40346eb8b927381be8fb27a61760914.jpg" width="40" alt="海上钢琴师"> | [海上钢琴师](https://ssr1.scrape.center/detail/18) | La leggenda del pianista sull'oceano | 剧情, 爱情, 音乐 | 意大利 | 126 分钟 | 2019-11-15 | **9.1** |
| <img src="https://p0.meituan.net/movie/30b20139e68c46d02e0893277d633b701292458.jpg" width="40" alt="千与千寻"> | [千与千寻](https://ssr1.scrape.center/detail/19) | 千と千尋の神隠し | 动画, 冒险, 奇幻, 家庭 | 日本 | 125 分钟 | 2019-06-21 | **9.1** |
| <img src="https://p1.meituan.net/movie/a1634f4e49c8517ae0a3e4adcac6b0dc43994.jpg" width="40" alt="迁徙的鸟"> | [迁徙的鸟](https://ssr1.scrape.center/detail/20) | The Travelling Birds | 纪录片 | 法国、德国、意大利、西班牙、瑞士 | 98 分钟 | 2001-12-12 | **9.1** |
| <img src="https://p0.meituan.net/movie/cd18ed2c5cda9e71e17e5e6ef61ced172912303.jpg" width="40" alt="黄金三镖客"> | [黄金三镖客](https://ssr1.scrape.center/detail/21) | Il buono, il brutto, il cattivo. | 西部, 冒险 | 意大利、西班牙、西德 | 161 分钟 | 1966-12-23 | **9.1** |
| <img src="https://p1.meituan.net/movie/a19a7f64a10e133b68de87d2f3bc46f3111417.jpg" width="40" alt="海洋"> | [海洋](https://ssr1.scrape.center/detail/22) | Océans | 纪录片 | 法国、瑞士、西班牙、美国、阿联酋 | 104 分钟 | 2011-08-12 | **9.1** |
| <img src="https://p1.meituan.net/movie/ed50b58bf636d207c56989872a91f4cf305138.jpg" width="40" alt="我爱你"> | [我爱你](https://ssr1.scrape.center/detail/23) | 그대를 사랑합니다 | 剧情, 爱情 | 韩国 | 118 分钟 | 2011-02-17 | **9.1** |
| <img src="https://p0.meituan.net/movie/85215b28d568ea8e2c97766edd95f890210522.jpg" width="40" alt="阿飞正传"> | [阿飞正传](https://ssr1.scrape.center/detail/24) | Days of Being Wild | 剧情, 爱情, 犯罪 | 中国香港 | 94 分钟 | 2018-06-25 | **9.1** |
| <img src="https://p1.meituan.net/movie/a53a0200eba15ba483c905c872db9bf4331099.jpg" width="40" alt="7号房的礼物"> | [7号房的礼物](https://ssr1.scrape.center/detail/36) | 7번방의 선물 | 剧情, 喜剧, 家庭 | 韩国 | 127 分钟 | 2013-01-23 | **8.8** |
| <img src="https://p0.meituan.net/movie/de1142a5dceb901eb939eb0bcfc2f88470909.jpg" width="40" alt="爱·回家"> | [爱·回家](https://ssr1.scrape.center/detail/25) | 집으로... | 剧情, 家庭 | 韩国 | 80 分钟 | 2002-04-05 | **9.1** |
| <img src="https://p0.meituan.net/movie/c304c687e287c7c2f9e22cf78257872d277201.jpg" width="40" alt="龙猫"> | [龙猫](https://ssr1.scrape.center/detail/26) | となりのトトロ | 动画, 冒险, 奇幻, 家庭 | 日本 | 86 分钟 | 2018-12-14 | **9.1** |
| <img src="https://p1.meituan.net/movie/4ffca83fd972f71e291f8ea8d78a4b58594878.jpg" width="40" alt="七武士"> | [七武士](https://ssr1.scrape.center/detail/27) | 七人の侍 | 剧情, 动作, 冒险 | 日本 | 207 分钟 | 1954-04-26 | **8.8** |
| <img src="https://p1.meituan.net/movie/92198a6fc8c3f5d13aa1bdf203572c0f99438.jpg" width="40" alt="美国往事"> | [美国往事](https://ssr1.scrape.center/detail/28) | Once Upon a Time in America | 剧情, 犯罪 | 意大利、美国 | 229 分钟 | 2015-04-23 | **8.8** |
| <img src="https://p1.meituan.net/movie/30310858fdab34c7a17cfd7ec8ad8bfc112201.jpg" width="40" alt="完美的世界"> | [完美的世界](https://ssr1.scrape.center/detail/29) | A Perfect World | 剧情, 犯罪 | 美国 | 138 分钟 | 1993-11-24 | **8.8** |
| <img src="https://p1.meituan.net/movie/b553d13f30100db731ab6cf45668e52d94703.jpg" width="40" alt="上帝之城"> | [上帝之城](https://ssr1.scrape.center/detail/30) | Cidade de Deus | 剧情, 犯罪 | 巴西、法国 | 130 分钟 | N/A | **8.8** |
| <img src="https://p0.meituan.net/movie/1433d81b10d116239dbbf02a06ac3c19265682.jpg" width="40" alt="辩护人"> | [辩护人](https://ssr1.scrape.center/detail/31) | 변호인 | 剧情 | 韩国 | 127 分钟 | 2013-12-18 | **8.8** |
| <img src="https://p0.meituan.net/movie/2d42e00d7ee59ff5bd574f93b8558aa726665.jpg" width="40" alt="忠犬八公物语"> | [忠犬八公物语](https://ssr1.scrape.center/detail/32) | ハチ公物語 | 剧情 | 日本 | 107 分钟 | 1987-08-01 | **8.8** |
| <img src="https://p0.meituan.net/movie/eb2ea56996f21e7fb47b1a0736c7f177258901.jpg" width="40" alt="海豚湾"> | [海豚湾](https://ssr1.scrape.center/detail/33) | The Cove | 纪录片 | 美国 | 92 分钟 | 2009-07-31 | **8.8** |
| <img src="https://p0.meituan.net/movie/3e5f5f3aa4b7e5576521e26c2c7c894d253975.jpg" width="40" alt="英雄本色"> | [英雄本色](https://ssr1.scrape.center/detail/34) | A Better Tomorrow | 剧情, 动作, 犯罪 | 中国香港 | 95 分钟 | 2017-11-17 | **8.8** |
| <img src="https://p0.meituan.net/movie/1da0af2570fe697d38c4a37fdfded19b254936.jpg" width="40" alt="恐怖直播"> | [恐怖直播](https://ssr1.scrape.center/detail/35) | 더 테러 라이브 | 剧情, 悬疑, 犯罪 | 韩国 | 97 分钟 | 2013-07-31 | **8.8** |
| <img src="https://p0.meituan.net/movie/3985eaf3858bea0f2a3d966bf7ee2103178217.jpg" width="40" alt="窃听风暴"> | [窃听风暴](https://ssr1.scrape.center/detail/37) | Das Leben der Anderen | 剧情, 悬疑 | 德国 | 137 分钟 | 2006-03-23 | **8.8** |
| <img src="https://p0.meituan.net/movie/6d8491386d07cda91967a6fbbd0d0788294693.jpg" width="40" alt="时空恋旅人"> | [时空恋旅人](https://ssr1.scrape.center/detail/38) | About Time | 喜剧, 爱情, 奇幻 | 英国 | 123 分钟 | 2013-09-04 | **8.8** |
| <img src="https://p1.meituan.net/movie/d5970e36c8868a4b746c80f3b3f8a404174615.jpg" width="40" alt="穿条纹睡衣的男孩"> | [穿条纹睡衣的男孩](https://ssr1.scrape.center/detail/39) | The Boy in the Striped Pajamas | 剧情, 战争 | 英国、美国 | 94 分钟 | 2008-08-28 | **8.8** |
| <img src="https://p0.meituan.net/movie/1199dc6273680f175fd9b06c9c36d08a219658.jpg" width="40" alt="教父"> | [教父](https://ssr1.scrape.center/detail/40) | The Godfather | 剧情, 犯罪 | 美国 | 175 分钟 | 2015-04-18 | **8.8** |
| <img src="https://p1.meituan.net/movie/4c55f3bf5fa9660db3cb7014651a0950267034.jpg" width="40" alt="萤火之森"> | [萤火之森](https://ssr1.scrape.center/detail/41) | 蛍火の杜へ | 剧情, 爱情, 动画, 奇幻 | 日本 | 45 分钟 | 2011-09-17 | **8.8** |
| <img src="https://p0.meituan.net/movie/19653e8af59cf473cd40f9ccc0658d93692304.jpg" width="40" alt="素媛"> | [素媛](https://ssr1.scrape.center/detail/42) | 소원 | 剧情 | 韩国 | 123 分钟 | 2013-10-02 | **8.8** |
| <img src="https://p1.meituan.net/movie/135c612860fae899df2220149664d97a173555.jpg" width="40" alt="小鞋子"> | [小鞋子](https://ssr1.scrape.center/detail/43) | بچههای آسمان | 剧情, 家庭 | 伊朗 | 89 分钟 | N/A | **8.8** |
| <img src="https://p1.meituan.net/movie/2a0783b4fd95566568f24adfad2181bb5392280.jpg" width="40" alt="熔炉"> | [熔炉](https://ssr1.scrape.center/detail/44) | 도가니 | 剧情 | 韩国 | 125 分钟 | 2011-09-22 | **8.8** |
| <img src="https://p1.meituan.net/moviemachine/508056769092059fe43a611b949f27d14863831.jpg" width="40" alt="大话西游之大圣娶亲"> | [大话西游之大圣娶亲](https://ssr1.scrape.center/detail/45) | A Chinese Odyssey Part Two - Cinderella | 喜剧, 爱情, 奇幻 | 中国香港、中国大陆 | 110 分钟 | 2014-10-24 | **8.9** |
| <img src="https://p1.meituan.net/movie/7833126c8c21a11571bb52fbdece0acb811449.jpg" width="40" alt="新龙门客栈"> | [新龙门客栈](https://ssr1.scrape.center/detail/46) | New Dragon Gate Inn | 动作, 爱情, 武侠, 古装 | 中国香港、中国大陆 | 88 分钟 | 2012-02-24 | **8.9** |
| <img src="https://p1.meituan.net/movie/1e700e53e4fe29dd5942381bb353c8532239179.jpg" width="40" alt="触不可及"> | [触不可及](https://ssr1.scrape.center/detail/47) | Intouchables | 剧情, 喜剧 | 法国 | 112 分钟 | 2011-11-02 | **8.9** |
| <img src="https://p0.meituan.net/movie/bcbe59fc51580317adf94537a61a1a26142090.jpg" width="40" alt="钢琴家"> | [钢琴家](https://ssr1.scrape.center/detail/48) | The Pianist | 剧情, 音乐, 传记, 历史, 战争 | 法国、德国、英国、波兰 | 150 分钟 | 2002-05-24 | **8.9** |
| <img src="https://p0.meituan.net/movie/2526f77c650bf7cf3d5ee2dccdeac332244951.jpg" width="40" alt="本杰明·巴顿奇事"> | [本杰明·巴顿奇事](https://ssr1.scrape.center/detail/49) | The Curious Case of Benjamin Button | 剧情, 爱情, 奇幻 | 美国 | 166 分钟 | 2008-12-25 | **8.9** |
| <img src="https://p1.meituan.net/movie/96d98200d2afb4b87ff189f9c15b6545568339.jpg" width="40" alt="倩女幽魂"> | [倩女幽魂](https://ssr1.scrape.center/detail/50) | A Chinese Ghost Story | 爱情, 奇幻, 武侠, 古装 | 中国香港 | 98 分钟 | 2011-04-30 | **8.9** |
| <img src="https://p1.meituan.net/movie/bb0eca029cd25329776a4549b3fbe262924727.jpg" width="40" alt="哈利·波特与死亡圣器（下）"> | [哈利·波特与死亡圣器（下）](https://ssr1.scrape.center/detail/51) | Harry Potter and the Deathly Hallows: Part 2 | 剧情, 悬疑, 奇幻, 冒险 | 英国、美国 | 130 分钟 | 2011-08-04 | **8.9** |
| <img src="https://p1.meituan.net/movie/0b0d45b58946078dd24d4945dd6be3b51329411.jpg" width="40" alt="甜蜜蜜"> | [甜蜜蜜](https://ssr1.scrape.center/detail/52) | Comrades: Almost a Love Story | 剧情, 爱情 | 中国香港 | 118 分钟 | 2015-02-13 | **8.9** |
| <img src="https://p0.meituan.net/movie/f7f4b4099773268f8290ed033f49dc01377512.jpg" width="40" alt="蝙蝠侠：黑暗骑士崛起"> | [蝙蝠侠：黑暗骑士崛起](https://ssr1.scrape.center/detail/53) | The Dark Knight Rises | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国、英国 | 165 分钟 | 2012-08-27 | **8.9** |
| <img src="https://p0.meituan.net/movie/34f9202c5e823f490ffec4c69d5d0028137395.jpg" width="40" alt="鬼子来了"> | [鬼子来了](https://ssr1.scrape.center/detail/54) | Devils on the Doorstep | 剧情, 战争 | 中国大陆 | 139 分钟 | 2000-05-13 | **8.8** |
| <img src="https://p1.meituan.net/movie/70a574550c4bb928dcc6a40641294785150838.jpg" width="40" alt="无敌破坏王"> | [无敌破坏王](https://ssr1.scrape.center/detail/55) | Wreck-It Ralph | 喜剧, 动画, 奇幻, 冒险 | 美国 | 101 分钟 | 2012-11-06 | **8.8** |
| <img src="https://p0.meituan.net/movie/83df1c541e6e0696e67ce7da81cb1e1a251258.jpg" width="40" alt="致命魔术"> | [致命魔术](https://ssr1.scrape.center/detail/56) | The Prestige | 剧情, 悬疑, 惊悚 | 美国、英国 | 130 分钟 | 2006-10-17 | **8.8** |
| <img src="https://p0.meituan.net/movie/85c2bfba6025bfbfb53291ae5924c215308805.jpg" width="40" alt="神偷奶爸"> | [神偷奶爸](https://ssr1.scrape.center/detail/57) | Despicable Me | 喜剧, 动画, 冒险 | 美国、法国 | 95 分钟 | 2010-06-20 | **8.8** |
| <img src="https://p0.meituan.net/movie/e71affe126eeb4f8bfcc738cbddeebc8288766.jpg" width="40" alt="断背山"> | [断背山](https://ssr1.scrape.center/detail/58) | Brokeback Mountain | 剧情, 爱情, 家庭 | 美国、加拿大 | 134 分钟 | 2005-09-02 | **8.8** |
| <img src="https://p0.meituan.net/movie/15f1ac49b6d1ff7b71207672993ed6901536456.jpg" width="40" alt="怦然心动"> | [怦然心动](https://ssr1.scrape.center/detail/59) | Flipped | 剧情, 喜剧, 爱情 | 美国 | 90 分钟 | 2010-07-26 | **8.8** |
| <img src="https://p0.meituan.net/movie/b0d97e4158b47d653d7a81d66f7dd3092146907.jpg" width="40" alt="驯龙高手"> | [驯龙高手](https://ssr1.scrape.center/detail/60) | How to Train Your Dragon | 喜剧, 动画, 奇幻, 冒险 | 美国 | 98 分钟 | 2010-05-14 | **8.8** |
| <img src="https://p0.meituan.net/movie/f9356a376358f1576da3263d998eca7a94624.jpg" width="40" alt="飞屋环游记"> | [飞屋环游记](https://ssr1.scrape.center/detail/61) | Up | 剧情, 喜剧, 动画, 冒险 | 美国 | 96 分钟 | 2009-08-04 | **8.8** |
| <img src="https://p0.meituan.net/movie/2e383b5f5f306f10f9f26d9f1c28cf1d825537.jpg" width="40" alt="黑客帝国3：矩阵革命"> | [黑客帝国3：矩阵革命](https://ssr1.scrape.center/detail/62) | The Matrix Revolutions | 动作, 科幻 | 美国、澳大利亚 | 129 分钟 | 2003-11-05 | **8.8** |
| <img src="https://p0.meituan.net/movie/845ce32778a1b3f258de089f91a3979b5766154.jpg" width="40" alt="速度与激情5"> | [速度与激情5](https://ssr1.scrape.center/detail/63) | Fast Five | 动作, 犯罪 | 美国 | 130 分钟 | 2011-05-12 | **8.9** |
| <img src="https://p1.meituan.net/movie/f8e9d5a90224746d15dfdbd53d4fae3d209420.jpg" width="40" alt="勇敢的心"> | [勇敢的心](https://ssr1.scrape.center/detail/64) | Braveheart | 剧情, 动作, 传记, 历史, 战争 | 美国 | 177 分钟 | 1995-05-18 | **8.9** |
| <img src="https://p1.meituan.net/movie/ca4a128a5a54d5b5e35ceba622636c831810197.jpg" width="40" alt="三傻大闹宝莱坞"> | [三傻大闹宝莱坞](https://ssr1.scrape.center/detail/65) | 3 Idiots | 剧情, 喜剧, 爱情, 歌舞 | 印度 | 171 分钟 | 2011-12-08 | **8.9** |
| <img src="https://p1.meituan.net/movie/8d7b0b902afd4ec1a3dd7a9c6149463c187734.jpg" width="40" alt="闻香识女人"> | [闻香识女人](https://ssr1.scrape.center/detail/66) | Scent of a Woman | 剧情 | 美国 | 157 分钟 | 1992-12-23 | **8.9** |
| <img src="https://p1.meituan.net/movie/21b9211eb1094af360842472018db634286646.jpg" width="40" alt="末代皇帝"> | [末代皇帝](https://ssr1.scrape.center/detail/67) | The Last Emperor | 剧情, 传记, 历史 | 英国、意大利、中国大陆、法国、美国 | 163 分钟 | 1987-10-23 | **8.9** |
| <img src="https://p0.meituan.net/movie/4f9638ba234c3fb673f23a09968db875371576.jpg" width="40" alt="风之谷"> | [风之谷](https://ssr1.scrape.center/detail/68) | 風の谷のナウシカ | 动画, 奇幻, 冒险 | 日本 | 117 分钟 | N/A | **8.9** |
| <img src="https://p0.meituan.net/movie/396266d8b711958841b3536a3fa7b868211445.jpg" width="40" alt="大话西游之月光宝盒"> | [大话西游之月光宝盒](https://ssr1.scrape.center/detail/69) | A Chinese Odyssey | 喜剧, 爱情, 奇幻, 古装 | 中国香港、中国大陆 | 87 分钟 | 2014-10-24 | **8.9** |
| <img src="https://p0.meituan.net/movie/70de97ebb6b5251ecb7c3f6d7a782a7f189340.jpg" width="40" alt="放牛班的春天"> | [放牛班的春天](https://ssr1.scrape.center/detail/70) | Les choristes | 剧情, 音乐 | 法国、德国、瑞士 | 97 分钟 | 2004-10-16 | **8.9** |
| <img src="https://p1.meituan.net/movie/7d1d85610651dbe1c8687781a87d1008184950.jpg" width="40" alt="当幸福来敲门"> | [当幸福来敲门](https://ssr1.scrape.center/detail/71) | The Pursuit of Happyness | 剧情, 家庭, 传记 | 美国 | 117 分钟 | 2008-01-17 | **8.9** |
| <img src="https://p0.meituan.net/movie/a08f65e6cb50fab32df5da69ff116f593095363.jpg" width="40" alt="幽灵公主"> | [幽灵公主](https://ssr1.scrape.center/detail/72) | もののけ姫 | 动画, 奇幻, 冒险 | 日本 | 134 分钟 | 1998-05-01 | **8.9** |
| <img src="https://p0.meituan.net/movie/df15efd261060d3094a73ef679888d4f238149.jpg" width="40" alt="十二怒汉"> | [十二怒汉](https://ssr1.scrape.center/detail/73) | 12 Angry Men | 剧情 | 美国 | 96 分钟 | 1957-04-13 | **8.9** |
| <img src="https://p0.meituan.net/movie/b3defc07dfaa1b6f5b74852ce38a3f8f242792.jpg" width="40" alt="搏击俱乐部"> | [搏击俱乐部](https://ssr1.scrape.center/detail/74) | Fight Club | 剧情, 动作, 悬疑, 惊悚 | 美国、德国 | 139 分钟 | 1999-09-10 | **8.9** |
| <img src="https://p1.meituan.net/movie/bc022b86345c643ca21d759166f77a553679589.jpg" width="40" alt="疯狂原始人"> | [疯狂原始人](https://ssr1.scrape.center/detail/75) | The Croods | 喜剧, 动画, 冒险 | 美国 | 98 分钟 | 2013-04-20 | **8.9** |
| <img src="https://p1.meituan.net/movie/e540384dc6c9f63bdb27cc554588a77f44305.jpg" width="40" alt="阿凡达"> | [阿凡达](https://ssr1.scrape.center/detail/76) | Avatar | 动作, 科幻, 冒险 | 美国、英国 | 162 分钟 | 2010-01-04 | **8.9** |
| <img src="https://p0.meituan.net/movie/0127b451d5b8f0679c6f81c8ed414bb2432442.jpg" width="40" alt="哈尔的移动城堡"> | [哈尔的移动城堡](https://ssr1.scrape.center/detail/77) | ハウルの動く城 | 动画, 奇幻, 冒险 | 日本 | 119 分钟 | 2004-09-05 | **8.9** |
| <img src="https://p1.meituan.net/movie/d40efe1183f29d5900f5c60be3c8a89d339225.jpg" width="40" alt="盗梦空间"> | [盗梦空间](https://ssr1.scrape.center/detail/78) | Inception | 剧情, 科幻, 悬疑, 冒险 | 美国、英国 | 148 分钟 | 2010-09-01 | **8.9** |
| <img src="https://p0.meituan.net/movie/5f0a709378d6b567807aa9685610f818282136.jpg" width="40" alt="忠犬八公的故事"> | [忠犬八公的故事](https://ssr1.scrape.center/detail/79) | Hachi: A Dog's Tale | 剧情 | 美国、英国 | 93 分钟 | 2009-06-13 | **8.9** |
| <img src="https://p1.meituan.net/movie/a2a287c77415dc1f85b04d288f7d63ab1089754.jpg" width="40" alt="拯救大兵瑞恩"> | [拯救大兵瑞恩](https://ssr1.scrape.center/detail/80) | Saving Private Ryan | 剧情, 历史, 战争 | 美国 | 169 分钟 | 1998-11-13 | **8.9** |
| <img src="https://p0.meituan.net/movie/4c41068ef7608c1d4fbfbe6016e589f7204391.jpg" width="40" alt="活着"> | [活着](https://ssr1.scrape.center/detail/81) | To Live | 剧情, 家庭, 历史 | 中国大陆、中国香港 | 132 分钟 | 1994-05-17 | **9.0** |
| <img src="https://p0.meituan.net/movie/267dd2483f0fb57081474c00fbea38451415571.jpg" width="40" alt="机器人总动员"> | [机器人总动员](https://ssr1.scrape.center/detail/82) | WALL·E | 喜剧, 科幻, 动画 | 美国 | 98 分钟 | 2008-06-27 | **9.0** |
| <img src="https://p0.meituan.net/movie/76fc92cfa6c8f2959431b8aa604ef7ae126414.jpg" width="40" alt="天堂电影院"> | [天堂电影院](https://ssr1.scrape.center/detail/83) | Nuovo Cinema Paradiso | 剧情, 爱情 | 意大利、法国 | 155 分钟 | 1988-11-17 | **9.0** |
| <img src="https://p0.meituan.net/movie/02bb9fd161c05bad6089133098efcdb5546589.jpg" width="40" alt="指环王2：双塔奇兵"> | [指环王2：双塔奇兵](https://ssr1.scrape.center/detail/84) | The Lord of the Rings: The Two Towers | 剧情, 动作, 奇幻, 冒险 | 美国、新西兰 | 179 分钟 | 2003-04-25 | **9.0** |
| <img src="https://p1.meituan.net/movie/dd08154878aac7c8c649fe3eeb8ccd0a2498277.jpg" width="40" alt="指环王1：护戒使者"> | [指环王1：护戒使者](https://ssr1.scrape.center/detail/85) | The Lord of the Rings: The Fellowship of the Ring | 剧情, 动作, 奇幻, 冒险 | 新西兰、美国 | 178 分钟 | 2002-04-04 | **9.0** |
| <img src="https://p0.meituan.net/movie/86c5190ba1d1236093c13f2fe9ed8dd4150050.jpg" width="40" alt="射雕英雄传之东成西就"> | [射雕英雄传之东成西就](https://ssr1.scrape.center/detail/86) | The Eagle Shooting Heroes | 喜剧, 奇幻, 武侠, 古装 | 中国香港 | 113 分钟 | 1993-02-05 | **9.0** |
| <img src="https://p0.meituan.net/movie/09658109acfea0e248a63932337d8e6a4268980.jpg" width="40" alt="蝙蝠侠：黑暗骑士"> | [蝙蝠侠：黑暗骑士](https://ssr1.scrape.center/detail/87) | The Dark Knight | 剧情, 动作, 科幻, 惊悚, 犯罪 | 美国、英国 | 152 分钟 | 2008-07-14 | **9.0** |
| <img src="https://p0.meituan.net/movie/606de8f394d40dbcbb9b87943fec71a2130408.jpg" width="40" alt="无间道"> | [无间道](https://ssr1.scrape.center/detail/88) | Infernal Affairs | 剧情, 悬疑, 犯罪 | 中国香港 | 101 分钟 | 2003-09-05 | **9.0** |
| <img src="https://p0.meituan.net/movie/bb1dee5e0b25889a2410211c1d5010ae190824.jpg" width="40" alt="教父2"> | [教父2](https://ssr1.scrape.center/detail/89) | The Godfather: Part Ⅱ | 剧情, 犯罪 | 美国 | 202 分钟 | 1974-12-12 | **9.0** |
| <img src="https://p0.meituan.net/movie/b05b94b28eca53f325ae8d807fcd4ce01798036.jpg" width="40" alt="加勒比海盗"> | [加勒比海盗](https://ssr1.scrape.center/detail/90) | Pirates of the Caribbean: The Curse of the Black Pearl | 动作, 奇幻, 冒险 | 美国 | 143 分钟 | 2003-11-21 | **9.0** |
| <img src="https://p0.meituan.net/movie/d66b56b77b55aa3da5987b68948444c9106742.jpg" width="40" alt="哈利·波特与魔法石"> | [哈利·波特与魔法石](https://ssr1.scrape.center/detail/91) | Harry Potter and the Sorcerer's Stone | 奇幻, 冒险 | 美国、英国 | 152 分钟 | 2002-01-26 | **9.0** |
| <img src="https://p0.meituan.net/movie/932bdfbef5be3543e6b136246aeb99b8123736.jpg" width="40" alt="指环王3：王者无敌"> | [指环王3：王者无敌](https://ssr1.scrape.center/detail/92) | The Lord of the Rings: The Return of the King | 剧情, 动作, 奇幻, 冒险 | 美国、新西兰 | 201 分钟 | 2004-03-15 | **9.0** |
| <img src="https://p1.meituan.net/movie/ad974d3527879f00be2eec29135118163728582.jpg" width="40" alt="黑客帝国"> | [黑客帝国](https://ssr1.scrape.center/detail/93) | The Matrix | 动作, 科幻 | 美国、澳大利亚 | 136 分钟 | 2000-01-14 | **9.0** |
| <img src="https://p1.meituan.net/movie/6a964e9cee699267053bd6a4bf6f2671195394.jpg" width="40" alt="剪刀手爱德华"> | [剪刀手爱德华](https://ssr1.scrape.center/detail/94) | Edward Scissorhands | 剧情, 爱情, 奇幻 | 美国 | 105 分钟 | 1990-12-06 | **9.0** |
| <img src="https://p0.meituan.net/movie/ae7245920d95c03765fe1615f3a1fe3865785.jpg" width="40" alt="春光乍泄"> | [春光乍泄](https://ssr1.scrape.center/detail/95) | Happy Together | 剧情, 爱情 | 中国香港、日本、韩国 | 96 分钟 | 1997-05-17 | **9.0** |
| <img src="https://p1.meituan.net/movie/14a7b337e8063e3ce05a5993ed80176b74208.jpg" width="40" alt="大闹天宫"> | [大闹天宫](https://ssr1.scrape.center/detail/96) | The Monkey King | 动画, 奇幻 | 中国大陆 | 114 分钟 | 1965-12-31 | **9.0** |
| <img src="https://p1.meituan.net/movie/ba1ed511668402605ed369350ab779d6319397.jpg" width="40" alt="天空之城"> | [天空之城](https://ssr1.scrape.center/detail/97) | 天空の城ラピュタ | 动画, 奇幻, 冒险 | 日本 | 125 分钟 | 1992-05-01 | **9.0** |
| <img src="https://p0.meituan.net/movie/ef6d7e040278f3d727306745e8df1af5246411.jpg" width="40" alt="音乐之声"> | [音乐之声](https://ssr1.scrape.center/detail/98) | The Sound of Music | 剧情, 爱情, 歌舞, 传记 | 美国 | 174 分钟 | 1965-03-02 | **9.0** |
| <img src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg" width="40" alt="辛德勒的名单"> | [辛德勒的名单](https://ssr1.scrape.center/detail/99) | Schindler's List | 剧情, 历史, 战争 | 美国 | 195 分钟 | 1993-11-30 | **9.5** |
| <img src="https://p0.meituan.net/movie/58782fa5439c25d764713f711ebecd1e201941.jpg" width="40" alt="魂断蓝桥"> | [魂断蓝桥](https://ssr1.scrape.center/detail/100) | Waterloo Bridge | 剧情, 爱情, 战争 | 美国 | 108 分钟 | 1940-05-17 | **9.5** |
