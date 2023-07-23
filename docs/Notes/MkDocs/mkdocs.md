# MkDocs搭建

## MkDocs安装

1. 安装 ```pip install mkdocs```
2. 常用指令
   + `mkdocs new <work-space-name> #创建工作区`
   + `mkdocs serve #启动服务`
   + `mkdocs build #构建静态文件`
   + `mkdocs gh-deploy #部署到github`
   + `mkdocs -h    #查看帮助`

## MkDocs

## mkdocs-material主题安装

1. 安装 `pip install mkdocs-material`
2. 配置 `mkdocs.yml`

   ```yml
   site_name: mkdocs-material
   theme: material
   ```

3. 配置 `mkdocs.yml` 侧边栏

   ```yml
   nav:
       - 主页: index.md
       - 文档:
           - mkdocs: mkdocs.md
           - mkdocs-material: mkdocs-material.md
       - 关于: about.md
   ```

4. 配置 `mkdocs.yml` 顶部导航栏

   ```yml
   nav:
       - 主页: index.md
       - 文档:
           - mkdocs: mkdocs.md
           - mkdocs-material: mkdocs-material.md
       - 关于: about.md
   ```
