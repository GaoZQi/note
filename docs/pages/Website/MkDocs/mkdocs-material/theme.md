# Material for MkDocs的主题配置

??? tip "本站配置"
    !!! warning "配置报错问题"
        部分拓展需要额外下载，拓展配置细节推荐查看相关插件在GitHub或PyPi上的文档。

        有关主题的配置，请参考[**Material for MkDocs的主题配置**](https://squidfunk.github.io/mkdocs-material/customization/#theme)。

    ```yaml title="mkdocs.yml"
    site_name: GaoZQi's Note # 网站名称
    site_url: https://GaoZQi.github.io/note # 网站地址
    site_description: 个人文档 # 网站描述
    site_author: GaoZQi # 网站作者

    repo_name: GaoZQi/note # 仓库名称
    repo_url: https://github.com/GaoZQi/note # 仓库地址
    edit_uri: tree/main/docs # 编辑链接

    theme:
    name: "material" # 主题名称
    language: "zh" # 网站语言
    favicon: images/star.png # 网站图标
    icon: # 网站图标
        logo: material/arrow-bottom-right-thick

    custom_dir: "docs/resources" # 自定义目录

    features: # 特性
        - content.code.annotate # 代码注释
        - navigation.tracking # 导航栏跟踪
        - navigation.tabs # 导航栏标签
        - navigation.indexes # 导航栏索引
        - navigation.top # 导航栏顶部
        - content.code.copy # 代码复制
        - content.code.annotate # 代码注释
        - navigation.footer # 导航栏底部
        - content.action.edit # 编辑
        - content.action.view # 查看
        # - header.autohide
        - navigation.sections
        # - navigation.tabs.sticky  #粘滞选项卡
        # - toc.integrate
        - navigation.expand #目录展开
        - navigation.path
        - toc.follow
    palette:
        accent: deep orange



        # # Palette toggle for automatic mode
        # - media: "(prefers-color-scheme)"
        #   toggle:
        #     icon: material/brightness-auto
        #     name: Switch to light mode

        # # Palette toggle for light mode
        # - media: "(prefers-color-scheme: light)"
        #   scheme: default

        #     accent: blue
        #   toggle:
        #     icon: material/brightness-7
        #     name: Switch to dark mode

        # # Palette toggle for dark mode
        # - media: "(prefers-color-scheme: dark)"
        #   scheme: slate
        #   palette:
        #     primary: black
        #     accent: blue
        #   toggle:
        #     icon: material/brightness-4
        #     name: Switch to system preference

    extra_css:
    # - https://gcore.jsdelivr.net/npm/katex@0.15.1/dist/katex.min.css
    # - https://gcore.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.1.0/style.css
    # - https://gcore.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css
    # - https://cdn.tonycrane.cc/utils/katex.min.css
    # - https://cdn.tonycrane.cc/jbmono/jetbrainsmono.css
    # - https://cdn.tonycrane.cc/lxgw/lxgwscreen.css
    # - css/tasklist.css
    - css/fonts.css
    - css/custom.css
    # - css/img.css
    - css/admonition_old.css
    - css/flink.css

    extra_javascript:
    - js/mathjax.js
    # - js/img.js
    - https://polyfill.io/v3/polyfill.min.js?features=es6
    - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

    plugins:
    - search: {}
    - mkdocs-code-runner
    - git-revision-date-localized:
        type: iso_datetime
        custom_format: "%d. %B %Y"
        timezone: Asia/Shanghai
        locale: zh
        fallback_to_build_date: false
        enable_creation_date: true
        exclude:
            - index.md
            - pages/Home/map.md
            - pages/Website/MkDocs/mkdocs-material/theme.md
            - pages/CTF/index.md
            - pages/Notes/index.md
            - pages/Archive/index.md
            - pages/Other/index.md
            - pages/CTF/PWN/index.md
    - statistics:
        codelines_per_minute: 10
        # page_check_metadata: data
    # - changelog:
    #     changelog: docs\pages\Home\changelog.yml
    - encryptcontent:
        title_prefix: "🫥 "
        remember_password: True
        summary: '⚠️ 文章已加密'
        placeholder: '输入口令'
        # placeholder_user: User
        password_button_text: '校验'
        decryption_failure_message: '口令错误或没有权限！'
        encryption_info_message: '输入口令以查看该页面。'
        password_button: True

        encrypted_something:
            mkdocs-encrypted-toc: [div, id]
        # encrypted_something:
        # mkdocs-encrypted-toc: [nav, class]
            # myToc: [div, id]
            # myTocButton: [div, id]
        # password_file: 'passwords.yml'



    markdown_extensions:
    - abbr # 缩写
    - pymdownx.snippets # 代码块
    - pymdownx.highlight: # 代码高亮
        anchor_linenums: true # 代码行号
    - pymdownx.inlinehilite # 行内代码高亮
    - pymdownx.superfences # 内置标题栏
    - attr_list # 属性列表

    - toc: # 目录
        permalink: "☍" # 目录链接
        toc_depth: 4 # 目录深度
    - meta # 元数据
    - def_list # 定义列表
    - attr_list # 属性列表
    - md_in_html # HTML中的Markdown
    - sane_lists # 列表
    - admonition # 警告

    - pymdownx.keys # 键盘
    - pymdownx.mark # 标记
        # 格式化处理
    - pymdownx.caret # 上标
    - pymdownx.keys # 键盘
    - pymdownx.mark # 标记
    - pymdownx.tilde # 删除线
    - pymdownx.critic # 评论

    - pymdownx.details # 详情
    - pymdownx.magiclink # 链接
    - tables # 表格

    - meta

    - pymdownx.tabbed: # 标签
        alternate_style: true # 标签样式
    - pymdownx.tasklist: # 任务列表
        custom_checkbox: true # 自定义复选框
    - pymdownx.arithmatex: # 数学公式
        generic: true # 通用
    - pymdownx.emoji: # emoji
        emoji_index: !!python/name:materialx.emoji.twemoji # emoji索引
        emoji_generator: !!python/name:materialx.emoji.to_svg
            # emoji生成器

    # 导航栏
    nav:
    # - 404.md
    - 导航:
        - 主页: index.md
        # - 网站地图: pages/Home/map.md

    - CTF:
        - pages/CTF/index.md
        - PWN:
            - pages/CTF/PWN/index.md
            - PWN环境配置记录: pages/CTF/PWN/env.md
            - PWN题目部署: pages/CTF/PWN/other/build-pwn.md
            - pwntools: pages/CTF/PWN/pwntools/notes.md
        - Docker:
            - pages/CTF/Docker/index.md
            # - Dockerfile: pages/CTF/Docker/Dockerfile.md
            - Docker的使用:
            - Docker简介: pages/CTF/Docker/overview.md
            - Docker容器的使用: pages/CTF/Docker/containers.md
            - Docker镜像的使用: pages/CTF/Docker/images.md
            - Docker常用命令: pages/CTF/Docker/command.md

    - WriteUp:
        - pages/WriteUp/index.md
        - 第十六届全国大学生信息安全竞赛——创新实践能力赛: pages/WriteUp/第十六届全国大学生信息安全竞赛——创新实践能力赛/writeup.md
        - 2023年第三届陕西省大学生网络安全技能大赛--本科高校组: pages/WriteUp/2023年第三届陕西省大学生网络安全技能大赛--本科高校组/writeup.md
        - 2023年网络空间安全实验技能竞赛: pages/WriteUp/2023年网络空间安全实验技能竞赛/writeup.md
        - NSCTF四校联合CTF邀请赛: pages/WriteUp/NSCTF四校联合CTF邀请赛/writeup.md



    - Website:
        - pages/Website/index.md
        - MkDocs搭建:
            - MkDocs: pages/Website/MkDocs/mkdocs.md
            - Material for MkDocs:
                - pages/Website/MkDocs/mkdocs-material/index.md
                - Material for MkDocs的安装: pages/Website/MkDocs/mkdocs-material/config.md
                - Material for MkDocs的主题配置: pages/Website/MkDocs/mkdocs-material/theme.md
                - Material for MkDocs的拓展语法: pages/Website/MkDocs/mkdocs-material/mdextra.md

    # - Python:
    #     - index.md
    # - ROS:
    #     - index.md

    - 笔记:
        - pages/Notes/index.md

    - 存档:
        - pages/Archive/index.md
        - Python: pages/Notes/Python/Python.md
        - pages\Other\python\data_model.md
        - pages\Other\python\index.md
        - ROS: pages/Notes/ROS/ROS.md
        - Matlab: pages/Other/Matlab.md

    - 项目:
        - pages/Project/index.md
        # - 大创: pages/Project/creation/index.md

    - 课程:
        - 课程: pages/Course/index.md

    - 其他:
        - pages/Other/index.md
        - 测试: pages/Home/test.md
        - 代办: pages/Home/list.md
        - CCBC:
            - pages/Other/CCBC/index.md
            - 小行星带:
            - pages\Other\CCBC\CCBC2023\planets\index.md
            - pages\Other\CCBC\CCBC2023\planets\11.md
            - pages\Other\CCBC\CCBC2023\planets\22.md
            - pages\Other\CCBC\CCBC2023\planets\33.md
            - pages\Other\CCBC\CCBC2023\planets\44.md
            - pages\Other\CCBC\CCBC2023\planets\55.md
            - pages\Other\CCBC\CCBC2023\planets\66.md
            - pages\Other\CCBC\CCBC2023\planets\77.md
            - pages\Other\CCBC\CCBC2023\planets\88.md
            - CCBC-13: pages\Other\CCBC\CCBC2023\CCBC13\index.md
            - CCBC-14: pages\Other\CCBC\CCBC2023\CCBC14\index.md
    ```

!!! warning
    正在学习中……〒▽〒

<link rel="stylesheet" href="../../../../../css/index_styles.css">
<div class="center-container">

  <state>U•ェ•*U</state>
  <text>waiting</text>
  <text class="line">.....</text>
</div>

---

[:material-arrow-u-left-top: 回到上一级](./index.md)
