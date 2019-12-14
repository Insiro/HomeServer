var hostname = 'insiro.me.epic'

function go_table() {
    if (arguments.length < 1) {
        location.href = "Tables?table=" + "None";
    } else {
        location.href = "Tables?table=" + arguments[0];
    }
}

function go_detail() {
    //argu[0]:id, argu[1]:table
    if (arguments.length < 1) {
        location.href = "detail?id=" + "None";
    } else {
        location.href = "detail?id=" + arguments[0] + "&table=" + arguments[1];
    }
}

function login() {
    var form = document.getElementByID('loginform').value;
    window.open(form + 'id :' + form.id)
}

function nullDialog() {
    var name = document.getElementById("dialogName")
    var detailBtn = document.getElementById("detailBtn")
    var content = document.getElementById("dialogContents")
    content.innerHTML = "None"
    name.innerText = "None"
    detailBtn.addEventListener("click", function () { location.href = "detail?id=None"; })
}

function viewDialog() {
    //arg0=id
    if (arguments.length < 1) nullDialog()
    else {
        var name = document.getElementById("dialogName")
        var detailBtn = document.getElementById("detailBtn")
        var content = document.getElementById("dialogContents")
        var req = new XMLHttpRequest()
        var id = arguments[1]
        var table = arguments[0]
        req.open("GET", "info?table=" + table + "&id=" + id);
        req.addEventListener("load", function () {
            if (req.status != 200) {
                nullDialog()
                return
            }
            // detailBtn.addEventListener("click", function () {
            //     go_detail(id, table)
            //     //location.href = "detail?id=\"" + id + "\"&table=\"" + table + "\"";
            // })
            content.innerHTML = "<table id='diatable'></table>"
            var data = JSON.parse(req.responseText);
            name.innerText = data.name;
            content.innerHTML += "<h6>Writer : " + data.writer + "</h6>"
            if (data.link != null)
                content.innerHTML += "<a href = '" + data.link + "'>link</a>"
            if (data.contents != null)
                content.innerHTML += "<p>" + data.contents.split("\n").join("<br>") + "</p>"
            else if (data.memo != null)
                content.innerHTML += "<p>" + data.memo.split("\n").join("<br>") + "</p>"

        });
        req.send(null);
    }
    $('#modalDialog').modal('show')

}



function getGameList(theGame, length) {
    var req = new XMLHttpRequest()
    req.open("GET", hostname + "list/" + theGame + "/" + length);
    req.addEventListener("load", function () {
        if (req.status === 200) {
            var json = JSON.parse(req.responseText);
            var data = json.data;
            writeList(theGame, data);
        } else {
            writeList();
            console.error("NONE");
        }
    });
    req.send(null);
}

function get_detail(table, id) {
    var req = new XMLHttpRequest()
    req.open("GET", hostname + "info/" + table + "/" + id);
    req.addEventListener("load", function () {
        if (req.status === 200) {
            var json = JSON.parse(req.responseText);
            var data = json.data;
            writedata(data);
        } else {
            writedata();
            console.error("NONE");
        }
    });
    req.send(null);
}

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    return null;
}

function includeHTML() {
    var z, i, elmnt, file, xhttp;
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        elmnt = z[i];
        file = elmnt.getAttribute("include-html");
        if (file) {
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    elmnt.innerHTML = this.responseText;
                    elmnt.removeAttribute("include-html");
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            return;
        }
    }
}

function addFooter() {
    var footerdiv = document.getElementById("footer")
    var footerstr = "<div class=\"copyright text - center my - auto \"> <span > Copyright© Your Website 2019 </span> </div > "
    footerstr += ""
    footerdiv.innerHTML = footerstr
}



function reloadLoginState(loginBox) {
    loginXhttpRequest = new XMLHttpRequest();
    if (loginBox) {
        $('#Login').modal('hide');
    }

    loginXhttpRequest.open("GET", "php/isLoggedin.php");
    loginXhttpRequest.addEventListener("load", function () {
        var log_in_item = document.getElementById('logged_nav').style;
        var un_log_in_tem = document.getElementById('unlogged_nav').style;
        json = JSON.parse(loginXhttpRequest.responseText);
        if (json.login) {
            log_in_item.display = 'none';
            un_log_in_tem.display = '';
        } else {
            log_in_item.display = '';
            un_log_in_tem.display = 'none';
        }
    });

    loginXhttpRequest.send(null);
}



function loginRequest() {
    var id = document.getElementById('login_id').value;
    var pw = document.getElementById('login_pwd').value;

    var xhttp = new XMLHttpRequest();

    // Testing Code Only
    xhttp.open("POST", "php/makelogin.php");

    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=utf-8");
    xhttp.addEventListener("load", function () {
        parsedJson = JSON.parse(xhttp.responseText);

        if (parsedJson.success) {
            reloadLoginState(true);
        } else {
            console.error('login error');
        }
    });

    xhttp.send("id=" + id + "&pwd=" + pw);
}

function logout() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "php/logout.php");

    xhttp.addEventListener("load", function () {
        reloadLoginState(false);
    });

    xhttp.send(null);

}

function signUp(data) {
    if (data.pwd.value != data.check.value) {
        return false;
    }
    return true;
}