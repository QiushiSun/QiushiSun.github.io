---
permalink: /research/
title: "Research"
excerpt: ""
author_profile: true
---

<span class='anchor' id='research'></span>

<style>
    /* ---- Research page (scoped styles) ---- */
    .research-lead { margin: 0.5em 0 1.25em; }

    /* Widen this page so the timelines fit without scrolling.
       The avatar column is hidden at every width: the timelines and the
       publication list need the horizontal space, and the profile is already
       on the homepage. */
    #main .sidebar { display: none; }
    #main .page {
        float: none;
        width: 100%;
        margin: 0 auto;
        padding-left: 0;
        padding-right: 0;
    }

    @media (min-width: 1600px) {
        #main { max-width: 1600px; }
    }

    .research-theme {
        border-left: 3px solid #2d3748;
        padding: 0.1em 0 0.1em 1em;
        margin: 0 0 1.5em;
    }
    .research-theme > p { margin: 0.35em 0; }
    .research-theme .theme-name { font-weight: 700; }
    .t-stop.bl-hidden { display: none; }
    #bl-merged { cursor: pointer; }
    .bl-expand { color: #7B3F98; }
    .bl-paper .t-topic { cursor: pointer; }
    .bl-paper .t-topic::after { content: " ▾"; color: #9B7BC8; }
    @keyframes bl-hint {
        0%, 100% { background: transparent; }
        50% { background: #F3EDFB; }
    }
    .bl-paper.bl-revealed .t-topic {
        border-radius: 4px;
        animation: bl-hint 1.1s ease 2;
    }
    .t-stop.t-soon { opacity: 0.55; }
    .t-stop.t-soon .t-dot { background: #B9CDEA; }

    /* ---- CUA timeline ---- */
    .cua-timeline-wrap {
        overflow-x: auto;
        padding: 0.9em 0 0.3em;
        scrollbar-width: thin;
        scrollbar-color: #dfe5ec transparent;
    }
    .cua-timeline-wrap::-webkit-scrollbar { height: 5px; }
    .cua-timeline-wrap::-webkit-scrollbar-track { background: transparent; }
    .cua-timeline-wrap::-webkit-scrollbar-thumb { background: #dfe5ec; border-radius: 3px; }
    .cua-timeline {
        position: relative;
        display: flex;
        justify-content: space-between;
        min-width: 1150px;
        padding: 0 26px 0 6px;
    }
    /* arrow shaft */
    .cua-timeline::before {
        content: "";
        position: absolute;
        left: 0; right: 12px;
        top: 45px;
        height: 4px;
        border-radius: 2px;
        background: linear-gradient(90deg, #C5D9F5, #7FA8E0);
    }
    /* arrowhead */
    .cua-timeline::after {
        content: "";
        position: absolute;
        right: 0;
        top: 40px;
        border-left: 13px solid #7FA8E0;
        border-top: 7px solid transparent;
        border-bottom: 7px solid transparent;
    }
    .t-stop {
        position: relative;
        z-index: 1;
        flex: 1;
        min-width: 104px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .t-topic {
        height: 20px;
        font-size: 12.5px;
        font-weight: 700;
        color: #5f6b7a;
        letter-spacing: 0.02em;
        white-space: nowrap;
    }
    .t-date {
        height: 20px;
        font-family: ui-monospace, "SF Mono", Menlo, monospace;
        font-size: 12px;
        font-weight: 600;
        color: #1A73E8;
    }
    .t-dot {
        width: 14px; height: 14px;
        border-radius: 50%;
        background: #1A73E8;
        border: 3px solid #fff;
        box-shadow: 0 0 0 1.5px #7FA8E0;
    }
    .t-name { margin-top: 0.5em; font-size: 13.5px; font-weight: 600; line-height: 1.25; }
    .t-name a { color: #122c8b; text-decoration: none; }
    .t-name a:hover { text-decoration: underline; }
    .t-venue { font-size: 11.5px; color: #8a94a3; }
    /* Month tags on minor stops: temporarily hidden to reduce crowding
       (data kept in the HTML) — delete this rule to show them again. */
    .t-mdate { display: none; }

    /* Secondary works hang below the axis, linked by a light connector */
    .t-stop.t-minor { min-width: 84px; flex: 0.7; }
    .t-minor .t-dot {
        width: 10px; height: 10px;
        background: #B9CDEA;
        border: 2px solid #fff;
        box-shadow: 0 0 0 1px #B9CDEA;
    }
    .t-connector {
        width: 0;
        height: 24px;
        border-left: 2px dashed #C5D9F5;
        margin-top: 2px;
    }
    .t-arrowhead {
        width: 0; height: 0;
        border-top: 6px solid #C5D9F5;
        border-left: 4.5px solid transparent;
        border-right: 4.5px solid transparent;
        margin-bottom: 4px;
    }
    .t-minor .t-name { margin-top: 0; font-size: 12.5px; }
    .t-minor .t-name a { color: #4a6ea8; }
    .t-minor .t-venue { font-size: 11px; }

    /* Code axis: same geometry as the CUA axis, purple palette */
    .code-axis::before { background: linear-gradient(90deg, #DFD3F0, #9B7BC8); }
    .code-axis::after { border-left-color: #9B7BC8; }
    .code-axis .t-date { color: #7B3F98; }
    .code-axis .t-dot { background: #7B3F98; box-shadow: 0 0 0 1.5px #B79CD6; }
    .code-axis .t-soon .t-dot { background: #DFD3F0; }

    /* ---- Publication list with tabs ---- */
    .rp-note { font-size: 0.85em; color: #6b7684; margin: 0.25em 0 0.75em; }
    .rp-tabs {
        display: flex;
        gap: 1.5em;
        border-bottom: 1px solid #e5e8ec;
        margin-bottom: 0.5em;
    }
    .rp-tab {
        appearance: none;
        background: none;
        border: none;
        padding: 0.4em 0.1em;
        margin-bottom: -1px;
        font-size: 0.9em;
        color: #8a94a3;
        cursor: pointer;
        border-bottom: 2px solid transparent;
    }
    .rp-tab:hover { color: #374798; }
    .rp-tab.active {
        color: #1a1f2b;
        font-weight: 700;
        border-bottom-color: #1A73E8;
    }
    .rp-list { list-style: none; padding: 0; margin: 0; }
    .rp-item {
        display: flex;
        gap: 18px;
        align-items: flex-start;
        padding: 1em 0;
        border-bottom: 1px solid #f0f2f5;
    }
    .rp-thumb {
        flex: 0 0 274px;
        display: flex;
        justify-content: center;
        position: relative;
        transform-origin: left center;
        transition: transform 0.3s ease;
    }
    .rp-thumb:hover {
        z-index: 1000;
        transform: scale(2.8);
    }
    .rp-thumb:hover img {
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
    }
    .rp-thumb img {
        max-width: 274px;
        max-height: 152px;
        object-fit: contain;
        border: 1px solid #e5e8ec;
        border-radius: 4px;
        background: #fff;
    }
    .rp-badge {
        position: absolute;
        top: 6px;
        left: -4px;
        z-index: 2;
        padding: 1px 8px;
        color: #fff;
        background-color: #00369f;
        font-size: 0.62em;
        font-weight: 600;
        letter-spacing: 0.02em;
    }
    /* Counter-scale the badge so it grows less than the zoomed thumbnail */
    .rp-thumb .rp-badge { transform-origin: left top; transition: transform 0.3s ease; }
    .rp-thumb:hover .rp-badge { transform: scale(0.5); }
    .rp-main { flex: 1; min-width: 0; }
    .rp-title {
        display: inline-block;
        font-weight: 700;
        color: #1a1f2b;
        text-decoration: none;
        line-height: 1.3;
        margin-bottom: 0.15em;
    }
    .rp-title:hover { color: #374798; }
    .rp-authors { font-size: 0.85em; color: #4a5568; line-height: 1.35; }
    .rp-meta { margin: 0.3em 0 0.15em; }
    .rp-links { margin: 0.15em 0 0.3em; }
    .rp-links .btn-link { font-size: 0.78em; }
    .rp-venue {
        display: inline-block;
        font-family: ui-monospace, "SF Mono", Menlo, monospace;
        font-size: 0.72em;
        font-weight: 600;
        color: #1A73E8;
        background: #E8F0FE;
        border-radius: 4px;
        padding: 2px 7px;
        letter-spacing: 0.02em;
    }
    .rp-desc { font-size: 0.82em; font-style: italic; color: #8a94a3; }

    @media (max-width: 600px) {
        .rp-item { flex-direction: column; gap: 8px; }
        .rp-thumb { flex-basis: auto; }
    }
</style>

<h1 id="-research-overview">🔭 Research Overview</h1>

<p class="research-lead">My research aims at building agentic methods that operate real-world software, along two threads:</p>

<div class="research-theme">
  <p><span class="theme-name">Computer-Using Agents</span> — agents that operate computers, phones, and browsers the way people do, toward digital automation. My work spans GUI grounding (<a href="https://arxiv.org/abs/2401.10935">SeeClick</a>, <a href="https://osatlas.github.io/">OS-Atlas</a>), trajectory synthesis (<a href="https://qiushisun.github.io/OS-Genesis-Home/">OS-Genesis</a>, <a href="https://njucckevin.github.io/openmobile/">OpenMobile</a>), application in advanced workflows (<a href="https://qiushisun.github.io/ScienceBoard-Home/">ScienceBoard</a>), safety (<a href="https://qiushisun.github.io/OS-Sentinel-Home/">OS-Sentinel</a>), reward modeling (<a href="https://os-copilot.github.io/OSReward-Home/">OSReward &amp; OS-Shepherd</a>) and more.</p>
  <div class="cua-timeline-wrap">
    <div class="cua-timeline">
      <div class="t-stop">
        <div class="t-topic">Grounding</div>
        <div class="t-date">2024.01</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2401.10935">SeeClick / ScreenSpot</a></div>
        <div class="t-venue">ACL'24</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Action Model</div>
        <div class="t-date">2024.10</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://osatlas.github.io/">OS-Atlas</a></div>
        <div class="t-venue">ICLR'25</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Data Synthesis</div>
        <div class="t-date">2024.12</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://qiushisun.github.io/OS-Genesis-Home/">OS-Genesis</a></div>
        <div class="t-venue">ACL'25</div>
      </div>
      <div class="t-stop t-minor">
        <div class="t-topic"></div>
        <div class="t-date"></div>
        <div class="t-dot"></div>
        <div class="t-connector"></div>
        <div class="t-arrowhead"></div>
        <div class="t-name"><a href="https://chengyou-jia.github.io/AgentStore-Home/">AgentStore</a></div>
        <div class="t-venue"><span class="t-mdate">2024.10 · </span>ACL'25</div>
      </div>
      <div class="t-stop t-minor">
        <div class="t-topic"></div>
        <div class="t-date"></div>
        <div class="t-dot"></div>
        <div class="t-connector"></div>
        <div class="t-arrowhead"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2504.10127">GUIMid</a></div>
        <div class="t-venue"><span class="t-mdate">2025.04 · </span>COLM'25</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Advanced CUA Applications</div>
        <div class="t-date">2025.05</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://qiushisun.github.io/ScienceBoard-Home/">ScienceBoard</a></div>
        <div class="t-venue">ICLR'26</div>
      </div>
      <div class="t-stop t-minor">
        <div class="t-topic"></div>
        <div class="t-date"></div>
        <div class="t-dot"></div>
        <div class="t-connector"></div>
        <div class="t-arrowhead"></div>
        <div class="t-name"><a href="https://github.com/OpenGVLab/ScaleCUA">ScaleCUA</a></div>
        <div class="t-venue"><span class="t-mdate">2025.09 · </span>ICLR'26 Oral</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">CUA Safety</div>
        <div class="t-date">2025.10</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://qiushisun.github.io/OS-Sentinel-Home/">OS-Sentinel</a></div>
        <div class="t-venue">ACL'26 Oral &amp; Best Paper, AIWILD @ ICLR'26</div>
      </div>
      <div class="t-stop t-minor">
        <div class="t-topic"></div>
        <div class="t-date"></div>
        <div class="t-dot"></div>
        <div class="t-connector"></div>
        <div class="t-arrowhead"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2601.07779">OS-Symphony</a></div>
        <div class="t-venue"><span class="t-mdate">2026.01 · </span>ACL'26</div>
      </div>
      <div class="t-stop t-minor">
        <div class="t-topic"></div>
        <div class="t-date"></div>
        <div class="t-dot"></div>
        <div class="t-connector"></div>
        <div class="t-arrowhead"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2604.15093">OpenMobile</a></div>
        <div class="t-venue"><span class="t-mdate">2026.04 · </span>COLM'26</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Reward Modeling</div>
        <div class="t-date">2026.07</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://os-copilot.github.io/OSReward-Home/">OSReward &amp; OS-Shepherd</a></div>
      </div>
      <div class="t-stop t-soon">
        <div class="t-topic">General CUA Eval</div>
        <div class="t-date">2026</div>
        <div class="t-dot"></div>
        <div class="t-name">OS-Omni</div>
        <div class="t-venue">NeurIPS'26</div>
      </div>
    </div>
  </div>
</div>

<div class="research-theme">
  <p><span class="theme-name">Code Intelligence</span> — language models that understand and generate code, and code as an interface for agents. My work charts the field (<a href="https://qiushisun.github.io/NCI-Survey-Homapage/">NCI Survey</a>), synthesizes code-centric data via agent interaction (<a href="https://arxiv.org/abs/2507.22080">CodeEvo</a>), and builds multimodal code models (<a href="https://github.com/InternLM/JanusCoder">JanusCoder</a>) for generative UI and beyond.</p>
  <div class="cua-timeline-wrap" id="code-timeline">
    <div class="cua-timeline code-axis">
      <div class="t-stop" id="bl-merged" title="Click to expand">
        <div class="t-topic">Before LLMs</div>
        <div class="t-date">2022–23</div>
        <div class="t-dot"></div>
        <div class="t-name"><span class="bl-expand">2 papers ▸</span></div>
        <div class="t-venue">EMNLP'22 · COLING'24</div>
      </div>
      <div class="t-stop bl-paper bl-hidden">
        <div class="t-topic" title="Click to collapse">Before LLMs</div>
        <div class="t-date">2022.10</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2210.04633">CAT-Probing</a></div>
        <div class="t-venue">EMNLP'22</div>
      </div>
      <div class="t-stop bl-paper bl-hidden">
        <div class="t-topic" title="Click to collapse">Before LLMs</div>
        <div class="t-date">2023.06</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2306.07285">TransCoder</a></div>
        <div class="t-venue">COLING'24</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Charting the Field</div>
        <div class="t-date">2024.03</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2403.14734">Code Intelligence Survey</a></div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Data Synthesis</div>
        <div class="t-date">2025.07</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2507.22080">CodeEvo</a></div>
        <div class="t-venue">ACL'26 Oral</div>
      </div>
      <div class="t-stop">
        <div class="t-topic">Multimodal Code Intelligence</div>
        <div class="t-date">2025.10</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://arxiv.org/abs/2510.23538">JanusCoder</a></div>
        <div class="t-venue">ICLR'26</div>
      </div>
      <div class="t-stop t-soon">
        <div class="t-topic">Coming Soon</div>
        <div class="t-date">2026</div>
        <div class="t-dot"></div>
        <div class="t-name"><a href="https://qiushisun.github.io/PrismaCoder-Home/">PrismaCoder</a></div>
        <div class="t-venue">Stay tuned</div>
      </div>
    </div>
  </div>
</div>

<h1 id="-publication-threads">🧵 Publication Threads</h1>

<p class="rp-note"><sup>*</sup> equal contribution &nbsp;·&nbsp; <sup>†</sup> project co-lead</p>

<div class="rp-tabs">
  <button class="rp-tab active" data-cat="all">All</button>
  <button class="rp-tab" data-cat="agents">Computer-Using Agents</button>
  <button class="rp-tab" data-cat="code">Code Intelligence</button>
  <button class="rp-tab" data-cat="reasoning">Reasoning and Planning</button>
</div>

<ul class="rp-list">
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">Preprint</span><img src="/images/paper_thumbnails/osreward.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2607.28609">OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models</a>
      <div class="rp-authors"><strong>Qiushi Sun<sup>†</sup></strong>, Kanzhi Cheng<sup>†</sup>, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2607.28609" class="btn-link btn-paper">Paper</a> <a href="https://os-copilot.github.io/OSReward-Home/" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/datasets/OS-Copilot/OSReward" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">OSReward</a> <a href="https://huggingface.co/collections/OS-Copilot/osreward-and-os-shepherd" class="btn-link btn-hf"><img src="/images/logos/os-shepherd.png" style="margin-right: 7px;" alt="">OS-Shepherd-9B/35B</a> <a href="https://huggingface.co/datasets/OS-Copilot/OS-Shepherd-100K" class="btn-link btn-data">Data</a> <a href="https://github.com/OS-Copilot/OSReward" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2026osreward">BIB</a></div>
      <div class="rp-desc">A standardized benchmark for computer-use reward models, with OS-Shepherd judges trained on 100K trajectory judgments.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ICLR'26</span><img src="/images/paper_thumbnails/scienceboard-short.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2505.19897">ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows</a>
      <div class="rp-authors"><strong>Qiushi Sun</strong>, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, Jianing Wang, Qintong Li, Xiangru Tang, Tianbao Xie, Xiachong Feng, Xiang Li, Ben Kao, Wenhai Wang, Biqing Qi, Lingpeng Kong, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2505.19897" class="btn-link btn-paper">Paper</a> <a href="/files/ScienceBoard_slides.pdf" class="btn-link btn-slide">Slide</a> <a href="https://qiushisun.github.io/ScienceBoard-Home/" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/collections/OS-Copilot/os-genesis-6768d4b6fffc431dbf624c2d" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">HF</a> <a href="https://huggingface.co/OS-Copilot/ScienceBoard-Env" class="btn-link btn-env">Env</a> <a href="https://github.com/OS-Copilot/ScienceBoard" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2026scienceboard">BIB</a> <a href="https://x.com/qiushi_sun/status/1927720338072486387" class="btn-link btn-tw"><img src="/images/Logo_of_Twitter.svg.png" alt=""></a></div>
      <div class="rp-desc">A realistic environment and benchmark for evaluating computer-using agents in scientific workflows.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="code">
    <div class="rp-thumb"><span class="rp-badge">ICLR'26</span><img src="/images/paper_thumbnails/januscoder-short.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2510.23538">JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence</a>
      <div class="rp-authors"><strong>Qiushi Sun<sup>*</sup></strong>, Jingyang Gong<sup>*</sup>, Yang Liu<sup>*</sup>, Qiaosheng Chen<sup>*</sup>, Lei Li, Kai Chen, Qipeng Guo, Ben Kao, Fei Yuan</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2510.23538" class="btn-link btn-paper">Paper</a> <a href="/files/JanusCoder-ICLR_260331.pdf" class="btn-link btn-slide">Slide</a> <a href="https://github.com/InternLM/JanusCoder" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/collections/internlm/januscoder" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">HF</a> <a href="https://huggingface.co/datasets/QiushiSun/JanusCode-800K" class="btn-link btn-data">Data</a> <a href="https://github.com/InternLM/JanusCoder" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2026januscoder">BIB</a></div>
      <div class="rp-desc">Foundation models that establish a unified visual-programmatic interface for code intelligence.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ACL'26 Oral</span><img src="/images/paper_thumbnails/os-sentinel.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2510.24411">OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows</a>
      <div class="rp-authors"><strong>Qiushi Sun<sup>*</sup></strong>, Mukai Li<sup>*</sup>, Zhoumianze Liu<sup>*</sup>, Zhihui Xie<sup>*</sup>, Fangzhi Xu, Zhangyue Yin, Kanzhi Cheng, Zehao Li, Zichen Ding, Qi Liu, Zhiyong Wu, Zhuosheng Zhang, Ben Kao, Lingpeng Kong</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2510.24411" class="btn-link btn-paper">Paper</a> <a href="/files/OS-Sentinel_AIWILD@ICLR_260426.pdf" class="btn-link btn-slide">Slide</a> <a href="https://qiushisun.github.io/OS-Sentinel-Home/" class="btn-link btn-project">Project</a> <a href="https://github.com/OS-Copilot/OS-Sentinel" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2026sentinel">BIB</a> <a href="https://x.com/qiushi_sun/status/1927720338072486387" class="btn-link btn-tw"><img src="/images/Logo_of_Twitter.svg.png" alt=""></a></div>
      <div class="rp-award">🏆 <span style="color: #C62828; font-weight: 700;">AIWILD @ ICLR 2026 Best Paper Award</span></div>
      <div class="rp-desc">A hybrid safety detection framework for mobile GUI agents, pairing formal verification with contextual judgment.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="code">
    <div class="rp-thumb"><span class="rp-badge">ACL'26 Oral</span><img src="/images/paper_thumbnails/codeevo.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2507.22080">CodeEvo: Interaction-Driven Synthesis of Code-centric Data through Hybrid and Iterative Feedback</a>
      <div class="rp-authors"><strong>Qiushi Sun</strong>, Jingyang Gong, Lei Li, Qipeng Guo, Fei Yuan</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2507.22080" class="btn-link btn-paper">Paper</a> <a href="/files/CodeEvo_ACL2026_Oral.pdf" class="btn-link btn-slide">Slide</a> <a href="https://github.com/QiushiSun/CodeEvo" class="btn-link btn-code">Code</a> <a href="https://huggingface.co/datasets/QiushiSun/CodeEvo-100K" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">Data</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2026codeevo">BIB</a></div>
      <div class="rp-desc">Synthesizes code-centric training data through coder–reviewer agent interaction with hybrid feedback.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ACL'25</span><img src="/images/paper_thumbnails/os-genesis-short.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2412.19723">OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis</a>
      <div class="rp-authors"><strong>Qiushi Sun<sup>*</sup></strong>, Kanzhi Cheng<sup>*</sup>, Zichen Ding<sup>*</sup>, Chuanyang Jin<sup>*</sup>, Yian Wang, Fangzhi Xu, Zhenyu Wu, Chengyou Jia, Liheng Chen, Zhoumianze Liu, Ben Kao, Guohao Li, Junxian He, Yu Qiao, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2412.19723" class="btn-link btn-paper">Paper</a> <a href="/files/ACL25_OS_Genesis.pdf" class="btn-link btn-slide">Slide</a> <a href="https://qiushisun.github.io/OS-Genesis-Home/" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/collections/OS-Copilot/os-genesis-6768d4b6fffc431dbf624c2d" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">HF</a> <a href="https://huggingface.co/collections/OS-Copilot/os-genesis-6768d4b6fffc431dbf624c2d" class="btn-link btn-data">Data</a> <a href="https://github.com/OS-Copilot/OS-Genesis" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2025osgenesis">BIB</a> <a href="https://x.com/qiushi_sun/status/1874807124515344599" class="btn-link btn-tw"><img src="/images/Logo_of_Twitter.svg.png" alt=""></a></div>
      <div class="rp-desc">Constructs high-quality GUI agent trajectories without human supervision via reverse task synthesis.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">COLM'26</span><img src="/images/paper_thumbnails/openmobile_synth.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2604.15093">OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis</a>
      <div class="rp-authors">Kanzhi Cheng, Zehao Li, Zheng Ma, Nuo Chen, Jialin Cao, <strong>Qiushi Sun</strong>, Zichen Ding, Fangzhi Xu, Hang Yan, Jiajun Chen, Anh Tuan Luu, Jianbing Zhang, Lewei Lu, Dahua Lin</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2604.15093" class="btn-link btn-paper">Paper</a> <a href="https://njucckevin.github.io/openmobile/" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/datasets/cckevinn/OpenMobile-Data" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">Data</a> <a href="https://github.com/njucckevin/OpenMobile-Code" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">An open recipe for mobile agents that synthesizes tasks from environment memory and rolls out trajectories with policy switching.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ACL'26</span><img src="/images/paper_thumbnails/os-symphony-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://aclanthology.org/2026.acl-long.1021">OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agents</a>
      <div class="rp-authors">Bowen Yang, Kaiming Jin, Zhenyu Wu, Zhaoyang Liu, <strong>Qiushi Sun</strong>, Zehao Li, Jingjing Xie, Zhoumianze Liu, Fangzhi Xu, Kanzhi Cheng, Qingyun Li, Yian Wang, Yu Qiao, Zun Wang, Zichen Ding</div>
      <div class="rp-links"><a href="https://aclanthology.org/2026.acl-long.1021" class="btn-link btn-paper">Paper</a> <a href="https://os-copilot.github.io/OS-Symphony/" class="btn-link btn-project">Project</a> <a href="https://github.com/OS-Copilot/OS-Symphony" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">Orchestrates tool, grounding, and reflection-memory agents for robust computer use across operating systems.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ICLR'26 Oral</span><img src="/images/paper_thumbnails/scalecua-overview.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2509.15221">ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data</a>
      <div class="rp-authors">Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, <strong>Qiushi Sun</strong>, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2509.15221" class="btn-link btn-paper">Paper</a> <a href="https://huggingface.co/collections/OpenGVLab/scalecua" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">HF</a> <a href="https://huggingface.co/datasets/OpenGVLab/ScaleCUA-Data" class="btn-link btn-data">Data</a> <a href="https://github.com/OpenGVLab/ScaleCUA" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">Scales open computer-use agents with a cross-platform corpus spanning six operating systems.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ACL'25</span><img src="/images/paper_thumbnails/agentstore-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2410.18603">AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant</a>
      <div class="rp-authors">Chengyou Jia, Minnan Luo, Zhuohang Dang, <strong>Qiushi Sun</strong>, Fangzhi Xu, Junlin Hu, Tianbao Xie, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2410.18603" class="btn-link btn-paper">Paper</a> <a href="https://chengyou-jia.github.io/AgentStore-Home/" class="btn-link btn-project">Project</a> <a href="https://github.com/chengyou-jia/AgentStore" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">Dynamically integrates heterogeneous agents, App-store style, into a generalist computer assistant.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">COLM'25</span><img src="/images/paper_thumbnails/guimid-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://openreview.net/forum?id=QDtORaZt8K">Breaking the Data Barrier – Building GUI Agents Through Task Generalization</a>
      <div class="rp-authors">Junlei Zhang, Zichen Ding, Chang Ma, Zijie Chen, <strong>Qiushi Sun</strong>, Zhenzhong Lan, Junxian He</div>
      <div class="rp-links"><a href="https://openreview.net/forum?id=QDtORaZt8K" class="btn-link btn-paper">Paper</a> <a href="https://huggingface.co/datasets/hkust-nlp/GUIMid" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">Data</a> <a href="https://github.com/hkust-nlp/GUIMid" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">Mid-training on reasoning-rich non-GUI tasks transfers to GUI planning, easing the trajectory-data bottleneck.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ICLR'25 Spotlight</span><img src="/images/paper_thumbnails/os-atlas-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2410.23218">OS-ATLAS: A Foundation Action Model for Generalist GUI Agents</a>
      <div class="rp-authors">Zhiyong Wu, Zhenyu Wu, Fangzhi Xu, Yian Wang, <strong>Qiushi Sun</strong>, Chengyou Jia, Kanzhi Cheng, Zichen Ding, Liheng Chen, Paul Pu Liang, Yu Qiao</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2410.23218" class="btn-link btn-paper">Paper</a> <a href="https://osatlas.github.io/" class="btn-link btn-project">Project</a> <a href="https://huggingface.co/collections/OS-Copilot/os-atlas" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">HF</a> <a href="https://huggingface.co/datasets/OS-Copilot/OS-Atlas-data" class="btn-link btn-data">Data</a> <a href="https://huggingface.co/datasets/OS-Copilot/ScreenSpot-v2" class="btn-link btn-data">ScreenSpot-v2</a></div>
      <div class="rp-desc">A foundation action model unifying GUI grounding, action, and agent modes across platforms.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="agents">
    <div class="rp-thumb"><span class="rp-badge">ACL'24</span><img src="/images/paper_thumbnails/seeclick-screenspot.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2401.10935">SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents</a>
      <div class="rp-authors">Kanzhi Cheng, <strong>Qiushi Sun</strong>, Yougang Chu, Fangzhi Xu, Yantao Li, Jianbing Zhang, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2401.10935" class="btn-link btn-paper">Paper</a> <a href="https://huggingface.co/cckevinn/SeeClick" class="btn-link btn-hf"><img src="/images/svgs/huggingface_logo.svg" alt="">Model</a> <a href="https://github.com/njucckevin/SeeClick" class="btn-link btn-code">Code</a></div>
      <div class="rp-desc">Pioneers screenshot-only GUI agents via grounding pre-training and introduces the ScreenSpot benchmark.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">COLM'24</span><img src="/images/paper_thumbnails/corex-short.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2310.00280">Corex: Pushing the Boundaries of Complex Reasoning through Multi-Model Collaboration</a>
      <div class="rp-authors"><strong>Qiushi Sun</strong>, Zhangyue Yin, Xiang Li, Zhiyong Wu, Xipeng Qiu, Lingpeng Kong</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2310.00280" class="btn-link btn-paper">Paper</a> <a href="/files/COLM24_Corex_Presentation.pdf" class="btn-link btn-slide">Slide</a> <a href="https://github.com/QiushiSun/Corex" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2024corex">BIB</a></div>
      <div class="rp-desc">Multi-model collaboration that pushes complex reasoning beyond single-model prompting.</div>
    </div>
  </li>
    <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">Preprint</span><img src="/images/paper_thumbnails/odysseyarena-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2602.05843">OdysseyArena: Benchmarking Large Language Models For Long-Horizon, Active and Inductive Interactions</a>
      <div class="rp-authors">Hang Yan<sup>*</sup>, Fangzhi Xu<sup>*</sup>, <strong>Qiushi Sun<sup>*</sup></strong>, Jinyang Wu, Zixian Huang, Muye Huang, Jingyang Gong, Zichen Ding, Kanzhi Cheng, Yian Wang, Xinyu Che, Zeyi Sun, Jian Zhang, Zhangyue Yin, Haoran Luo, Ben Kao, Qika Lin</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2602.05843" class="btn-link btn-paper">Paper</a> <a href="https://yayayacc.github.io/Odyssey-Home/" class="btn-link btn-project">Project</a></div>
      <div class="rp-desc">Benchmarks LLMs on long-horizon, active, and inductive interaction in live environments.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">ACL'25</span><img src="/images/paper_thumbnails/gp-prm.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://aclanthology.org/2025.acl-long.212/">Dynamic and Generalizable Process Reward Modeling</a>
      <div class="rp-authors">Zhangyue Yin, <strong>Qiushi Sun</strong>, Zhiyuan Zeng, Qinyuan Cheng, Xipeng Qiu, Xuanjing Huang</div>
      <div class="rp-links"><a href="https://aclanthology.org/2025.acl-long.212/" class="btn-link btn-paper">Paper</a></div>
      <div class="rp-desc">Automatically designs process rewards and allocates them dynamically via reward trees and Pareto-optimal selection.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">ACL'25</span><img src="/images/paper_thumbnails/ENVISIONS-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2406.11736">Interactive Evolution: A Neural-Symbolic Self-Training Framework for Large Language Models</a>
      <div class="rp-authors">Fangzhi Xu, <strong>Qiushi Sun</strong>, Kanzhi Cheng, Jun Liu, Yu Qiao, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2406.11736" class="btn-link btn-paper">Paper</a></div>
      <div class="rp-desc">A neural-symbolic self-training loop that improves LLMs from environment feedback without human annotation.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">ACL'24</span><img src="/images/paper_thumbnails/cok-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2306.06427">Boosting Language Models Reasoning with Chain-of-Knowledge Prompting</a>
      <div class="rp-authors">Jianing Wang<sup>*</sup>, <strong>Qiushi Sun<sup>*</sup></strong>, Xiang Li, Ming Gao</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2306.06427" class="btn-link btn-paper">Paper</a> <a href="/files/ACL24_CoK_Presentation.pdf" class="btn-link btn-slide">Slide</a></div>
      <div class="rp-desc">Prompts models with structured knowledge triples to ground multi-step reasoning and curb hallucination.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="reasoning">
    <div class="rp-thumb"><span class="rp-badge">COLING'24</span><img src="/images/paper_thumbnails/bbt-rgb-cover.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2305.08088">Make Prompt-based Black-Box Tuning Colorful: Boosting Model Generalization from Three Orthogonal Perspectives</a>
      <div class="rp-authors"><strong>Qiushi Sun</strong>, Chengcheng Han, Nuo Chen, Renyu Zhu, Jingyang Gong, Xiang Li, Ming Gao</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2305.08088" class="btn-link btn-paper">Paper</a></div>
      <div class="rp-desc">Boosts gradient-free prompt tuning with two-stage optimizers, multi-verbalizers, and better initialization.</div>
    </div>
  </li>
  <li class="rp-item" data-cat="code">
    <div class="rp-thumb"><span class="rp-badge">Survey</span><img src="/images/paper_thumbnails/nci-survey.png" alt=""></div>
    <div class="rp-main">
      <a class="rp-title" href="https://arxiv.org/abs/2403.14734">A Survey of Neural Code Intelligence: Paradigms, Advances and Beyond</a>
      <div class="rp-authors"><strong>Qiushi Sun</strong>, Zhirui Chen, Fangzhi Xu, Chang Ma, Kanzhi Cheng, Zhangyue Yin, Jianing Wang, Chengcheng Han, Renyu Zhu, Shuai Yuan, Pengcheng Yin, Qipeng Guo, Xipeng Qiu, Xiaoli Li, Fei Yuan, Lingpeng Kong, Xiang Li, Zhiyong Wu</div>
      <div class="rp-links"><a href="https://arxiv.org/abs/2403.14734" class="btn-link btn-paper">Paper</a> <a href="/files/NCI_Survey_Slides_V1.pdf" class="btn-link btn-slide">Slide</a> <a href="https://qiushisun.github.io/NCI-Survey-Homapage/" class="btn-link btn-project">Project</a> <a href="https://github.com/QiushiSun/Awesome-Code-Intelligence" class="btn-link btn-code">Code</a> <a href="#" class="btn-link btn-bib" data-bib-key="sun2024survey">BIB</a> <a href="https://twitter.com/qiushi_sun/status/1773252567637639185" class="btn-link btn-tw"><img src="/images/Logo_of_Twitter.svg.png" alt=""></a></div>
      <div class="rp-desc">Traces the development of code intelligence, from pretrained models to LLM-based agents.</div>
    </div>
  </li>
</ul>

<script>
  var blMerged = document.getElementById('bl-merged');
  if (blMerged) {
    blMerged.addEventListener('click', function () {
      blMerged.classList.add('bl-hidden');
      document.querySelectorAll('.bl-paper').forEach(function (el) { el.classList.remove('bl-hidden'); el.classList.add('bl-revealed'); });
    });
    document.querySelectorAll('.bl-paper .t-topic').forEach(function (el) {
      el.addEventListener('click', function () {
        blMerged.classList.remove('bl-hidden');
        document.querySelectorAll('.bl-paper').forEach(function (p) { p.classList.add('bl-hidden'); p.classList.remove('bl-revealed'); });
      });
    });
  }

  document.querySelectorAll('.rp-tab').forEach(function (tab) {
    tab.addEventListener('click', function () {
      document.querySelectorAll('.rp-tab').forEach(function (t) { t.classList.remove('active'); });
      tab.classList.add('active');
      var cat = tab.dataset.cat;
      document.querySelectorAll('.rp-item').forEach(function (item) {
        item.style.display = (cat === 'all' || item.dataset.cat === cat) ? '' : 'none';
      });
    });
  });
</script>
