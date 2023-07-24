// 检测用户的系统偏好设置是否为深色模式
function isDarkModePreferred() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return true;
    }
    return false;
}

// 切换深色模式
function toggleDarkMode() {
    const body = document.querySelector('body');
    body.classList.toggle('dark-mode');
}

// 初始化：根据用户的系统偏好设置切换深色模式
if (isDarkModePreferred()) {
    toggleDarkMode();
}
