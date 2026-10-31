document.addEventListener('DOMContentLoaded', () => { 
    const rows = document.querySelectorAll('.clickable-row'); 
    rows.forEach(row => { 
        row.addEventListener('click', () => { 
            window.location.href = row.dataset.href; 
        });
     });
 }); 
 

 function goBack() {
    window.history.back();
}
function goForward() {
    window.history.forward();
}


document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.newest-items-table .clickable-row');
    rows.forEach(function(row) {
        row.addEventListener('click', function() {
            window.location = this.querySelector('a.table-link').href;
        });
    });
});
