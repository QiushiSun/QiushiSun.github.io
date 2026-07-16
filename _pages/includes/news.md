# 🔥 News

<style>
    /* News list (Plan A): date pill in our Paper-blue + slim scrollbar. */
    .scrollable-area {
        max-height: 210px;
        overflow-y: auto;
        margin: 0.5em 0 0.75em;
        padding: 0.2em 0.5em 0.2em 0;
        border-bottom: 1px solid #eef0f3;
        scrollbar-width: thin;
        scrollbar-color: #cfd8dc transparent;
    }
    .scrollable-area::-webkit-scrollbar { width: 6px; }
    .scrollable-area::-webkit-scrollbar-track { background: transparent; }
    .scrollable-area::-webkit-scrollbar-thumb {
        background: #cfd8dc;
        border-radius: 3px;
    }
    .scrollable-area::-webkit-scrollbar-thumb:hover { background: #90a4ae; }

    .scrollable-area ul { list-style: none; padding: 0; margin: 0; }

    .news-item {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        padding: 0 4px 0 6px;
    }
    .news-date {
        flex: 0 0 auto;
        min-width: 58px;
        text-align: center;
        font-family: ui-monospace, "SF Mono", Menlo, monospace;
        font-size: 0.78em;
        font-weight: 600;
        color: #1A73E8;
        background: #E8F0FE;
        border-radius: 4px;
        padding: 2px 6px;
        letter-spacing: 0.02em;
        margin-top: 0.18em;
    }
    .news-body { flex: 1; line-height: 1.3; }

    .pdf { text-decoration: none; color: #122c8b; }
    .code { text-decoration: none; color: #122c8b; }
    .title { color: #374798; }
</style>
<div class="scrollable-area">
    <ul>
        <li class="news-item"><span class="news-date">2026.06</span><span class="news-body">🐳 Attending ACL 2026 in San Diego 🎙️ 2 oral talks: <a href="https://arxiv.org/abs/2510.24411">OS-Sentinel</a> and <a href="https://arxiv.org/abs/2507.22080">CodeEvo</a>!</span></li>
        <li class="news-item"><span class="news-date">2026.04</span><span class="news-body">🌟 Excited to be joining <a href="https://research.google/"><em class="entity-mention" style="--entity-color: #4285F4"><img src="./images/logos/Google.png" class="entity-icon" alt="">Google Research</em></a> as a Student Researcher Intern!</span></li>
        <li class="news-item"><span class="news-date">2026.04</span><span class="news-body">🏆 <a href="https://arxiv.org/abs/2510.24411">OS-Sentinel</a> received the <span style="color:#ac530f">Best Paper Award</span> at AIWILD @ ICLR 2026!</span></li>
        <li class="news-item"><span class="news-date">2026.04</span><span class="news-body">🎈 Four papers are accepted by ACL 2026! See you in San Diego 🇺🇸!</span></li>
        <li class="news-item"><span class="news-date">2026.03</span><span class="news-body">🐧☁️ Excited to receive the Tencent Qingyun Scholarship (Student Travel Grant).</span></li>
        <li class="news-item"><span class="news-date">2026.02</span><span class="news-body">🚀🔬 Introducing <a href="https://huggingface.co/internlm/Intern-S1-Pro"><em class="entity-mention" style="--entity-color: #2E6DB4"><img src="./images/logos/internlm.webp" class="entity-icon" alt="">Intern-S1-Pro</em></a>, a trillion-scale scientific multimodal foundation model!</span></li>
        <li class="news-item"><span class="news-date">2026.01</span><span class="news-body">🎉 <a href="https://huggingface.co/collections/internlm/januscoder/">JanusCoder</a>, <a href="https://qiushisun.github.io/ScienceBoard-Home/">ScienceBoard</a>, and <a href="https://github.com/OpenGVLab/ScaleCUA">ScaleCUA (Oral)</a> are accepted by ICLR'26! See you in Rio 🇧🇷!</span></li>
        <li class="news-item"><span class="news-date">2025.11</span><span class="news-body">⛱️ Attending EMNLP 2025 in Suzhou 🇨🇳</span></li>
        <li class="news-item"><span class="news-date">2025.10</span><span class="news-body">🛡️🤖 We launch <a href="https://arxiv.org/abs/2510.24411">OS-Sentinel</a> and <a href="https://huggingface.co/datasets/OS-Copilot/MobileRisk">MobileRisk</a> to advance the safety research of mobile agents.</span></li>
        <li class="news-item"><span class="news-date">2025.10</span><span class="news-body">⚙️🤗 Introducing <a href="https://huggingface.co/collections/internlm/januscoder/">JanusCoder-7B/14B</a> and <a href="https://huggingface.co/collections/internlm/januscoder">JanusCoderV-7B/8B</a>, new foundation models for multimodal code intelligence.</span></li>
        <li class="news-item"><span class="news-date">2025.08</span><span class="news-body">📑🖊️ Start serving as an Area Chair for ACL Rolling Review.</span></li>
        <li class="news-item"><span class="news-date">2025.06</span><span class="news-body">🎙️🌏 <a href="https://qiushisun.github.io/ScienceBoard-Home/">ScienceBoard</a> will be presented as an oral paper at ICML 2025 Workshop on Computer Use Agents 🇨🇦!</span></li>
        <li class="news-item"><span class="news-date">2025.05</span><span class="news-body">🔬🧪 We release <a href="https://qiushisun.github.io/ScienceBoard-Home/">ScienceBoard</a> to advance computer-using agents in scientific workflows!</span></li>
        <li class="news-item"><span class="news-date">2025.05</span><span class="news-body">🎈 Six papers are accepted by ACL 2025! Bis bald in Wien 🇦🇹!</span></li>
        <li class="news-item"><span class="news-date">2025.03</span><span class="news-body">🏖️ Will attend ICLR 2025! See you at Singapore 🇸🇬!</span></li>
        <li class="news-item"><span class="news-date">2024.12</span><span class="news-body">🤖 We release <a href="https://qiushisun.github.io/OS-Genesis-Home/">OS-Genesis</a> (ACL'25), <a href="https://osatlas.github.io/">OS-Atlas</a> (ICLR'25) and <a href="https://chengyou-jia.github.io/AgentStore-Home/">AgentStore</a> (ACL'25) to advance GUI agents!</span></li>
        <li class="news-item"><span class="news-date">2024.08</span><span class="news-body">⭐️ (Physically) started my PhD at <a href="https://www.hku.hk/"><em class="entity-mention" style="--entity-color: #2E7D5A"><img src="./images/logos/hku_logo.png" class="entity-icon" alt="">The University of Hong Kong</em></a> 🇭🇰!</span></li>
        <li class="news-item"><span class="news-date">2024.07</span><span class="news-body">🎉 One paper get accepted by COLM 2024! See you at Upenn 🇺🇸!</span></li>
        <li class="news-item"><span class="news-date">2024.05</span><span class="news-body">🥂 Four papers are accepted by ACL 2024! See you in Bangkok 🇹🇭!</span></li>
        <li class="news-item"><span class="news-date">2024.03</span><span class="news-body">📑 Check out our <a href="https://arxiv.org/abs/2403.14734">Code Intelligence Survey Paper</a> 🔥</span></li>
        <li class="news-item"><span class="news-date">2024.02</span><span class="news-body">🎓 Graduated from <a href="https://www.nus.edu.sg/"><em class="entity-mention" style="--entity-color: #EF7C00"><img src="./images/nus.svg-1.png" class="entity-icon" alt="">National University of Singapore</em></a>.</span></li>
        <li class="news-item"><span class="news-date">2023.12</span><span class="news-body">⛱️ Attending EMNLP 2023 in SG 🇸🇬</span></li>
        <li class="news-item"><span class="news-date">2023.07</span><span class="news-body">✨ Started my research intern at NLP Group, <a href="https://www.shlab.org.cn/"><em class="entity-mention" style="--entity-color: #2E6DB4"><img src="./images/svgs/shailab-logo.svg" class="entity-icon" alt="">Shanghai AI Lab</em></a></span></li>
        <li class="news-item"><span class="news-date">2023.05</span><span class="news-body">🚀 HugNLP Framework (CIKM'23 Best Demo Paper) is ready for use! Please check our <a href="https://arxiv.org/abs/2302.14286">Paper</a>, <a href="https://github.com/HugAILab/HugNLP">Repo</a> and <a href="https://zhuanlan.zhihu.com/p/628106578">Blogs</a></span></li>
        <li class="news-item"><span class="news-date">2023.05</span><span class="news-body">👏 We release <a href="https://arxiv.org/abs/2305.18153">SelfAware</a> for benchmarking LLMs' self-knowledge</span></li>
        <li class="news-item"><span class="news-date">2023.01</span><span class="news-body">🌟 Started my research intern at <a href="https://www.a-star.edu.sg/i2r"><em class="entity-mention" style="--entity-color: #1A3F8C"><img src="./images/svgs/astar-i2r.svg" class="entity-icon" alt="">I<sup>2</sup>R, A*STAR</em></a>, Singapore</span></li>
        <li class="news-item"><span class="news-date">2022.12</span><span class="news-body">🎉 Our team won second prize (100k RMB) in the <a href="https://iacc.pazhoulab-huangpu.com/">International Algorithm Case Competition</a>: PLM Tuning Track.</span></li>
        <li class="news-item"><span class="news-date">2022.08</span><span class="news-body">📚 Started my master's studies at National University of Singapore. 🇸🇬</span></li>
        <li class="news-item"><span class="news-date">2022.07</span><span class="news-body">🎓 Graduated from <a href="https://www.dase.ecnu.edu.cn/"><em class="entity-mention" style="--entity-color: #7B3F98"><img src="./images/svgs/DaSE.svg" class="entity-icon" alt="">School of Data Science and Engineering</em></a> of <a href="https://english.ecnu.edu.cn/"><em class="entity-mention" style="--entity-color: #A82235"><img src="./images/svgs/ECNU-logo.svg.png" class="entity-icon" alt="">ECNU</em></a>!</span></li>
        <li class="news-item"><span class="news-date">2022.07</span><span class="news-body">🥇 Awarded outstanding UG thesis and <span style="color:#ac530f">Shanghai Outstanding Graduate</span>.</span></li>
        <li class="news-item"><span class="news-date">2021.09</span><span class="news-body">📚 Started serving as a TA for Deep Learning for Computer Vision course this semester.</span></li>
        <li class="news-item"><span class="news-date">2021.05</span><span class="news-body">🏆 Led my team to win the Finalist Award in the Mathematical and Interdisciplinary Contest in Modeling!</span></li>
        <li class="news-item"><span class="news-date">2021.02</span><span class="news-body">❄️ Attending Data Science Winter School at Imperial College London 🇬🇧.</span></li>
    </ul>
</div>
