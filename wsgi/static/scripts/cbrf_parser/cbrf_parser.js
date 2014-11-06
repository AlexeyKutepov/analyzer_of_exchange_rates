/**
 * Created by Alexey Kutepov on 06.11.14.
 */

/**
 * Берёт настройки со страницы и запускает парсер
 */
function parse() {
    $.ajax({
        type: "POST",
        url: "/cbrf_parser_settings/",
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            days: $("#input_days").val()
        },
        success: function(data) {
            alert("Парсер курсов валют с сайта ЦБ РФ запущен! ");
        },
        error: function(xhr, textStatus, errorThrown) {
            alert("Error: "+errorThrown+xhr.status+xhr.responseText);
        }
    });
}