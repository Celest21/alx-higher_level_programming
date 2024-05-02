// Wait for the document to be fully loaded
// Send a GET request to the specified URL to fetch the translation
// Update the content of the div#hello element with the fetched translation
$(document).ready(function(){
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('div#hello').text(data.hello);
    });
});
