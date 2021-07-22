// dropdownอุปกรณืที่1
var subjectObject = {
    "115KV": {
        "สายดิน": ["ขาด", "หย่อน", "เป็นสนิม", "จุดสนิม"],
        "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
        "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
        "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
        "อุปกรณ์ตัดตอน": ["บิน", "แตก", "มีรอยอาร์ค"],

    },
    "33KV": {
        "สายดิน": ["ขาด", "หย่อน", "เป็นสนิม", "จุดต่อหลวม"],
        "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
        "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
        "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
        "ล่อฟ้า": ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"],
        "คาปาซิเตอร์": ["บิ่น/แตก", "มีรอยอาร์ค", "ผิวสกปรก"],


    },
    "เสา": {
        "เสาคอนกรีด": ["สภาพปกติ", "บิ่น,แตก (คอนกรีต),เป็นสนิม (โครงเหล็ก)", "บิดงอ,เสียรูป"],
        "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
        "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
        "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
        "ล่อฟ้า": ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"],
        "คาปาซิเตอร์": ["บิ่น/แตก", "มีรอยอาร์ค", "ผิวสกปรก"],
    },



}
window.onload = function() {
    var subjectSel = document.getElementById("subject");
    var topicSel = document.getElementById("topic");
    var chapterSel = document.getElementById("chapter");
    for (var x in subjectObject) {
        subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }
    subjectSel.onchange = function() {    //empty Chapters- and Topics- dropdowns
           
        chapterSel.length = 1;   
        topicSel.length = 1;
        //display correct values
        for (var y in subjectObject[this.value]) {
            topicSel.options[topicSel.options.length] = new Option(y, y);
        }
    }
    topicSel.onchange = function() {    //empty Chapters dropdown
           
        chapterSel.length = 1;
        //display correct values
        var z = subjectObject[subjectSel.value][this.value];
        for (var i = 0; i < z.length; i++) {
            chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
        }
    }
}

// function Reg() {
//     var alice = document.getElementById("alice");
//     console = log(alice.value);
//     var bob = document.getElementById("bob");
//     console = log(bob.value);
//     var carol = document.getElementById("carol");
//     console = log(carol.value);
// }