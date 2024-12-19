---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<!-- Currently, I am working with the NLP group of [Shanghai AI Lab](https://www.shlab.org.cn/) under the supervision of [Dr. Zhiyong Wu](https://lividwo.github.io/zywu.github.io/), focusing on topics related to LLM Agents. -->

<!-- Welcome to my homepage! I am a Ph.D. student at [HKU CS](https://www.cs.hku.hk/), advised by Prof. [C.M. Kao](https://www.cs.hku.hk/index.php/people/academic-staff/kao). I also work with the NLP group of [Shanghai AI Lab](https://www.shlab.org.cn/) and [HKUNLP](https://hkunlp.github.io/), focusing on topics related to LLM Agents. Previously, I was a master’s student at NUS, advised by [Dr. Xiaoli Li](https://www.a-star.edu.sg/i2r/about-i2r/i2r-management/li-xiaoli) at the Institute for Infocomm Research ([I<sup>2</sup>R](https://www.a-star.edu.sg/i2r)), A*STAR. Before that, I completed my B.Eng with distinction in the School of Data Science and Engineering ([DaSE](http://dase.ecnu.edu.cn/)) at [East China Normal University](https://en.wikipedia.org/wiki/East_China_Normal_University), where I was privileged to be instructed by [Prof. Weining Qian](http://dase.ecnu.edu.cn/dase-module-gateway/dase/teacher/single_teacher.html?teacherId=27), [Prof. Xuesong Lu](http://dase.ecnu.edu.cn/dase-module-gateway/dase/teacher/single_teacher.html?teacherId=40), and [Prof. Xiang Li](https://lixiang3776.github.io/) for research and engineering projects.
My research interests include neural code intelligence, LLM-based agents, and broad deep learning topics in general. -->

Welcome to my homepage! I am a Ph.D. student at [HKU CS](https://www.cs.hku.hk/), advised by Prof. [C.M. Kao](https://www.cs.hku.hk/index.php/people/academic-staff/kao). I also work with the NLP group of [Shanghai AI Lab](https://www.shlab.org.cn/) and [HKUNLP](https://hkunlp.github.io/), focusing on topics related to LLM Agents. Previously, I was a master’s student at NUS, advised by [Dr. Xiaoli Li](https://www.a-star.edu.sg/i2r/about-i2r/i2r-management/li-xiaoli) at [I<sup>2</sup>R](https://www.a-star.edu.sg/i2r), A*STAR. Before that, I completed my B.Eng with distinction in the School of Data Science and Engineering at [East China Normal University](https://en.wikipedia.org/wiki/East_China_Normal_University), where I was privileged to be instructed by [Prof. Weining Qian](https://scholar.google.com/citations?user=KqqoR6gAAAAJ), [Prof. Xuesong Lu](https://scholar.google.com/citations?user=Xh484PAAAAAJ), and [Prof. Xiang Li](https://lixiang3776.github.io/) for research and engineering projects.
My research interests include neural code intelligence, LLM-based agents, and broad deep learning topics in general.

🍀 **Office hours**: I am holding office hours (1~2 hours per week) dedicated to offering consultation for [COMP7607](https://nlp.cs.hku.hk/comp7607-fall2024/) students and mentorship programs. If you want to have a chat (whether or not it's about research), please book me through [this link](https://qiushi.youcanbook.me/)!

<!-- I will start my Ph.D. in Computer Science at [HKU CS](https://www.cs.hku.hk/) in 2024 Fall 🐱 -->

<!-- Download my [Resumé](./files/Qiushi_Academic_CV_June_2023.pdf)📄 in PDF. -->
 <!-- I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->
 
<div  align="right">
<img src='./images/qiushi-seal.jpg' style='width: 2.75em;'>  
</div>
# 🔥 News
<!-- - *2024.05*: &nbsp;🥂🥂 Four papers are accepted by ACL 2024! See you in Bangkok!
- *2024.03*: &nbsp;📑📑 Check out our Code Intelligence Survey Paper 🔥
- *2023.12*: &nbsp;⛱️⛱️ Attending EMNLP 2023 in SG 🇸🇬
- *2023.05*: &nbsp;🚀🚀 *HugNLP* Framework is ready for use! Please check our [Paper](https://arxiv.org/abs/2302.14286), [Repo](https://github.com/HugAILab/HugNLP) and [Blogs](https://zhuanlan.zhihu.com/p/628106578)!
- *2023.05*: &nbsp;👏👏 We release [*SelfAware* (ACL 2023 Findings)](https://arxiv.org/abs/2305.18153) for benchmarking LLMs' self-knowledge [Slides](./files/ACL23_LLMSA-Presentation.pdf).
- *2022.12*: &nbsp;🎉🎉 Our team won second prize (100k RMB) in the [International Algorithm Case Competition](https://iacc.pazhoulab-huangpu.com/): PLM Tuning Track.  -->
<style>  
    .scrollable-area {  
        max-height: 180px;  
        overflow-y: auto;  
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);  
        padding: 10px;  
    }
    .pdf {
        text-decoration: none;
        color: #122c8b;
    }
    .code {
        text-decoration: none;
        color: #122c8b;
    }
    .title{
        color: #374798;
    }
</style>  
<div class="scrollable-area">  
    <ul>
        <li><em>2024.08</em>: 🤖🤖 We release <a href="https://qiushisun.github.io/OS-Genesis.github.io/">OS-Genesis</a> and <a href="https://osatlas.github.io/">OS-Atlas</a> for the advancement of generalist GUI Agents!</li>
        <li><em>2024.08</em>: ⭐️⭐️ (Physically) started my PhD at The University of Hong Kong 🇭🇰!</li>
        <li><em>2024.07</em>: 🎉🎉 One paper get accepted by COLM 2024! See you at Upenn!</li>
        <li><em>2024.05</em>: 🥂🥂 Four papers are accepted by ACL 2024! See you in Bangkok!</li>
        <li><em>2024.03</em>: 📑📑 Check out our <a href="https://arxiv.org/abs/2403.14734">Code Intelligence Survey Paper</a>🔥</li>  
        <li><em>2024.02</em>: 🎓🎓 Graduated from National University of Singapore. </li>
        <li><em>2023.12</em>: ⛱️⛱️ Attending EMNLP 2023 in SG 🇸🇬</li>  
        <li><em>2023.07</em>: ✨✨ Started my research intern at NLP Group, Shanghai AI Lab</li>
        <li><em>2023.05</em>: 🚀🚀 HugNLP Framework (CIKM'23 Best Demo Paper) is ready for use! Please check our <a href="https://arxiv.org/abs/2302.14286">Paper</a>, <a href="https://github.com/HugAILab/HugNLP">Repo</a> and <a href="https://zhuanlan.zhihu.com/p/628106578">Blogs</a></li>  
        <li><em>2023.05</em>: 👏👏 We release <a href="https://arxiv.org/abs/2305.18153">SelfAware</a> for benchmarking LLMs' self-knowledge </li>  
        <li><em>2023.01</em>: 🌟🌟 Started my research intern at <a href="https://www.a-star.edu.sg/i2r">I<sup>2</sup>R, A*STAR</a>, Singapore </li>
        <li><em>2022.12</em>: 🎉🎉 Our team won second prize (100k RMB) in the <a href="https://iacc.pazhoulab-huangpu.com/">International Algorithm Case Competition</a>: PLM Tuning Track. </li> 
        <li><em>2022.08</em>: 📚📚 Started my master's studies at National University of Singapore. 🇸🇬</li>
        <li><em>2022.07</em>: 🎓🎓 Awarded outstanding UG thesis and graduated from ECNU as a Shanghai Outstanding Graduate. </li>
        <li><em>2021.09</em>: 📚📚 Started serving as a TA for Deep Learning for Computer Vision course this semester.</li>
        <li><em>2021.05</em>: 🏆🏆 Led my team to win the Finalist Award in the Mathematical and Interdisciplinary Contest in Modeling!</li>
        <li><em>2021.02</em>: ❄️❄️ Attending Data Science Winter School at Imperial College London.</li>
    </ul>  
</div>  

{% include_relative includes/pub.md %}

{% include_relative includes/interns.md %}

{% include_relative includes/honors.md %}

{% include_relative includes/ta.md %}

{% include_relative includes/edu.md %}

{% include_relative includes/services.md %}

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

> "What's past is prologue." -- William Shakespeare (The Tempest)  
> 
<!-- > <a href='https://scholar.google.com/citations?user=QgMkYFAAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> -->

<!-- # 📅 My Calendar

<iframe src="https://calendar.google.com/calendar/u/0?cid=dG9tbXlzdW4xMDE5QGdtYWlsLmNvbQ" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe> -->
