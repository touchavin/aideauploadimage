var subjectObject = {
    "115KV": {
        "สายดิน": ["ปกติ"],
        "ลูกถ้วย": ["ปกติ"],
        "สายไฟ": ["ปกติ"],
        "จุดต่อ": ["ปกติ"],
        "อุปกรณ์ตัดตอน": ["ปกติ"],

    },
    "33KV": {
        "สายดิน": ["ปกติ"],
        "ลูกถ้วย": ["ปกติ"],
        "สายไฟ": ["ปกติ"],
        "จุดต่อ": ["ปกติ"],
        "ล่อฟ้า": ["ปกติ"],
        "คาปาซิเตอร์": ["ปกติ"],
        "อุปกรณ์ตัดตอน": ["ปกติ"],

    },
    "22KV": {
        "สายดิน": ["ปกติ"],
        "ลูกถ้วย": ["ปกติ"],
        "สายไฟ": ["ปกติ"],
        "จุดต่อ": ["ปกติ"],
        "ล่อฟ้า": ["ปกติ"],
        "คาปาซิเตอร์": ["ปกติ"],
        "อุปกรณ์ตัดตอน": ["ปกติ"],
    },





}

window.onload = function() {
    var subjectSel = document.getElementById("subject");
    var topicSel = document.getElementById("topic");

    for (var x in subjectObject) {
        subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }
    subjectSel.onchange = function() { //empty Chapters- and Topics- dropdowns


        topicSel.length = 1;
        //display correct values
        for (var y in subjectObject[this.value]) {
            topicSel.options[topicSel.options.length] = new Option(y, y);
        }
    }

}