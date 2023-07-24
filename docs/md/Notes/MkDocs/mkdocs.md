# MkDocs
!!! quote "参考"
    [:material-link: MkDocs官方文档](https://www.mkdocs.org/)
## MkDocs安装

```shell
pip install mkdocs
```
## 常用指令

=== "创建工作区"

    ```
    mkdocs new <work-space-name>
    ```
=== "启动服务"

    ```
    mkdocs serve
    ```
=== "构建静态文件"

    ```
    mkdocs build
    ```
=== "部署到github"

    ```
    mkdocs gh-deploy
    ```
=== "查看帮助"

    ```
    mkdocs -h
    ```

## 目录结构
    
```text
    <work-space-name>
    ├── mkdocs.yml
    ├── site
    │   ├── ...
    │   └── ...
    ├── docs
    │   ├── ...
    │   │   ├── ...
    │   │   └── ...
    │   └── index.md
    └── README.md
```
## 配置文件

```yaml title='mkdocs.yml'
site_name: <site-name>  # 网站名称
site_url: <site-url>    # 网站地址
site_description: <site-description>    # 网站描述
site_author: <site-author>  # 网站作者

repo_url: <repo-url>    # 仓库地址(1)
edit_uri: <edit-uri>    # 编辑地址(2)

theme: <theme-name> # 主题名称
markdown_extensions: # 扩展语法
    - ...
    - ...
extra_css: # 额外的css
    - ...
    - ...
extra_javascript: # 额外的js
    - ...
    - ...
plugins: # 插件
    - ...
    - ...
nav:    # 导航栏
    - <nav-name>: <nav-link>
    - <nav-name>: <nav-link>
    - <nav-name>: <nav-link>
```

1. 用于部署到 :material-github:github
2. 用于编辑页面的 :material-file-edit-outline:编辑按钮
