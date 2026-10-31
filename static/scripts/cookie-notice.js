// static/cookie_notice.js
document.addEventListener('DOMContentLoaded', function() {
    var cookieNotice = document.getElementById('cookie-notice');
    var acceptButton = document.getElementById('accept-cookies');

    if (!localStorage.getItem('cookiesAccepted')) {
        cookieNotice.style.display = 'block';
    }

    acceptButton.addEventListener('click', function() {
        localStorage.setItem('cookiesAccepted', 'true');
        cookieNotice.style.display = 'none';
    });
});
