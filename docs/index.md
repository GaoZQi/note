---
title: 主页
# description: Nullam urna elit, malesuada eget finibus ut, ac tortor. 

hide:
    - navigation
    - toc
    - title
    - statistics

statistics: True
---
<!-- # 主页 -->

<link rel="stylesheet" href="css/index.css">
<div class="center-container">
  <span class="note-text">GaoZQi's Note</span>
</div>

---
<!-- <span id="web-time"></span> -->
<b>文章数</b>：{{pages}}篇  | <b>总字数</b>：{{words}}字 | <b>代码行数</b>：{{codes}}行

[:fontawesome-brands-bilibili: 糕芝奇](https://space.bilibili.com/229571662)　·　
[:fontawesome-brands-github: GaoZQi](https://github.com/GaoZQi)　·　
[:simple-notion: GGCTF](https://gaozqi.notion.site/d89d2c01587a4e87bd173ad8c8fd52f7?v=1a424dd567664341957429ba3a4b8ac4&pvs=4)

[:fontawesome-regular-clock: 近期文章：](.\pages\Home\list.md)[其他 > CCBC](.\pages\Other\CCBC\index.md)
<!-- 
<script>
function updateTime() {
    var date = new Date();
    var now = date.getTime();
    // var startDate = new Date("");
    var start = startDate.getTime();
    var diff = now - start;
    var y, d, h, m;
    y = Math.floor(diff / (365 *24* 3600 *1000));
    diff -= y* 365 *24* 3600 *1000;
    d = Math.floor(diff / (24* 3600 *1000));
    h = Math.floor(diff / (3600* 1000) % 24);
    m = Math.floor(diff / (60 *1000) % 60);
    if (y == 0) {
        document.getElementById("web-time").innerHTML = d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    } else {
        document.getElementById("web-time").innerHTML = y + "<span class=\"heti-spacing\"> </span>年<span class=\"heti-spacing\"> </span>" + d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    }
    setTimeout(updateTime, 1000* 60);
}
updateTime();
function toggle_statistics() {
    var statistics = document.getElementById("statistics");
    if (statistics.style.opacity == 0) {
        statistics.style.opacity = 1;
    } else {
        statistics.style.opacity = 0;
    }
}
</script> -->
