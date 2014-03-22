function delBtnName(pageURL) {
     var btnNames = ["1d", "1w", "1m", "3m", "6m", "1y", "5y", "10y"]

     for (i = 0; i<btnNames.length; i++) {
         if (pageURL.search(btnNames[i])!=-1) {
             pageURL = pageURL.replace(btnNames[i],"");
             pageURL = pageURL.replace("//", "/");
         }
     }
     return pageURL;
}

function init() {
     var pageURL = window.location.pathname;
     var button1Day = document.getElementById("1d_button");
     var button1Week = document.getElementById("1w_button");
     var button1Month = document.getElementById("1m_button");
     var button3Month = document.getElementById("3m_button");
     var button6Month = document.getElementById("6m_button");
     var button1Year = document.getElementById("1y_button");
     var button5Year = document.getElementById("5y_button");
     var button10Year = document.getElementById("10y_button");

     pageURL = delBtnName(pageURL);

     button1Day.href = pageURL + "1d/";
     button1Week.href = pageURL + "1w/";
     button1Month.href = pageURL + "1m/";
     button3Month.href = pageURL + "3m/";
     button6Month.href = pageURL + "6m/";
     button1Year.href = pageURL + "1y/";
     button5Year.href = pageURL + "5y/";
     button10Year.href =pageURL + "10y/";
}

window.onload = init;