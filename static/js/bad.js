// // dropdownอุปกรณืที่1
// var subjectObject = {
//     "115KV": {
//         "สายดิน": ["ขาด", "หย่อน", "เป็นสนิม", "จุดสนิม"],
//         "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
//         "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
//         "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
//         "อุปกรณ์ตัดตอน": ["บิน", "แตก", "มีรอยอาร์ค"],

//     },
//     "33KV": {
//         "สายดิน": ["ขาด", "หย่อน", "เป็นสนิม", "จุดต่อหลวม"],
//         "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
//         "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
//         "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
//         "ล่อฟ้า": ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"],
//         "คาปาซิเตอร์": ["บิ่น/แตก", "มีรอยอาร์ค", "ผิวสกปรก"],


//     },
//     "เสา": {
//         "เสาคอนกรีต": ["สภาพปกติ", "บิ่นแตก", "บิดงอ,เสียรูป"],
//         "ลูกถ้วย": ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก'],
//         "สายไฟ": ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"],
//         "จุดต่อ": ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"],
//         "ล่อฟ้า": ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"],
//         "คาปาซิเตอร์": ["บิ่น/แตก", "มีรอยอาร์ค", "ผิวสกปรก"],
//     },



// }
// window.onload = function() {
//     var subjectSel = document.getElementById("subject");
//     var topicSel = document.getElementById("topic");
//     var chapterSel = document.getElementById("chapter");
//     for (var x in subjectObject) {
//         subjectSel.options[subjectSel.options.length] = new Option(x, x);
//     }
//     subjectSel.onchange = function() {    //empty Chapters- and Topics- dropdowns
//            
//         chapterSel.length = 1;   
//         topicSel.length = 1;
//         //display correct values
//         for (var y in subjectObject[this.value]) {
//             topicSel.options[topicSel.options.length] = new Option(y, y);
//         }
//     }
//     topicSel.onchange = function() {    //empty Chapters dropdown
//            
//         chapterSel.length = 1;
//         //display correct values
//         var z = subjectObject[subjectSel.value][this.value];
//         for (var i = 0; i < z.length; i++) {
//             chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
//         }
//     }
// }

// function Reg() {
//     var alice = document.getElementById("alice");
//     console = log(alice.value);
//     var bob = document.getElementById("bob");
//     console = log(bob.value);
//     var carol = document.getElementById("carol");
//     console = log(carol.value);
// }




var typeData = ["115KV", "33KV", "22KV"];

var type115_topic = [
    "สายดิน",
    "ลูกถ้วย",
    "สายไฟ",
    "จุดต่อ",
    "อุปกรณ์ตัดตอน"
]

var type115_problem = new Map([
    ["สายดิน", ["ขาด", "หย่อน", "เป็นสนิม", "จุดสนิม"]],
    ["ลูกถ้วย", ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก']],
    ["สายไฟ", ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"]],
    ["จุดต่อ", ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"]],
    ["อุปกรณ์ตัดตอน", ["บิน", "แตก", "มีรอยอาร์ค"]],
]);

var type33_topic = [
    "สายดิน",
    "ลูกถ้วย",
    "สายไฟ",
    "จุดต่อ",
    "ล่อฟ้า",
    "คาปาซิเตอร์",
]
var type33_problem = new Map([
    ["สายดิน", ["ขาด", "หย่อน", "เป็นสนิม", "จุดสนิม"]],
    ["ลูกถ้วย", ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก']],
    ["สายไฟ", ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"]],
    ["จุดต่อ", ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"]],
    ["ล่อฟ้า", ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"]],
    ["อุปกรณ์ตัดตอน", ["บิน", "แตก", "มีรอยอาร์ค"]],
]);

var type22_topic = [
    "สายดิน",
    "ลูกถ้วย",
    "สายไฟ",
    "จุดต่อ",
    "ล่อฟ้า",
    "คาปาซิเตอร์",
]
var type22_problem = new Map([
    ["สายดิน", ["ขาด", "หย่อน", "เป็นสนิม", "จุดสนิม"]],
    ["ลูกถ้วย", ["แตก/บิ่น", "แฟลช", 'แตกลาย', 'เปลี่ยนสี', 'คราปสกปรก']],
    ["สายไฟ", ["สายแตก", "คลายตัว", "อุปกรณ์จับสายชำรุด"]],
    ["จุดต่อ", ["เปลี่ยนสี/เป็นสนิม", "มีรอยอาร์ด", "บิดงอเสียรูป"]],
    ["ล่อฟ้า", ["บิ่นแตก/แตก/ฉีก", "มีรอยอาร์ค", "ผิวสกปรก", "เปลี่ยนสี"]],
    ["อุปกรณ์ตัดตอน", ["บิน", "แตก", "มีรอยอาร์ค"]],
]);
$('document').ready(function() {
    setting();
    $('#chapter').multipleSelect({
        showClear: true
    })
});

function setting() {

    addData();
    $("#subject").on("change", function() {
        $("#topic").html('<option value=" " selected="selected">ชนิดอุปกรณ์</option>');
        $("li").removeClass("selected");
        $(".ms-choice span").text("");
        if ($("#subject").val() == "115KV") {
            for (var i = 0; i < type115_topic.length; i++) {
                $("#topic").prepend(
                    `<option value="` + type115_topic[i] + `">` + type115_topic[i] + `</option>`
                );
            }
            $("#topic").on("change", function() {
                var topic = $("#topic").val();
                type115_problem.get(topic);
                $("#chapter").html("");
                console.log(type115_problem.get(topic))
                for (var k = 0; k < type115_problem.get(topic).length; k++) {
                    $("#chapter").append(
                        ` <option value="` + type115_problem.get(topic)[k] + `" >` + type115_problem.get(topic)[k] + `</option>`
                    ).multipleSelect('refresh');
                }
            });





        } else if ($("#subject").val() == "33KV") {
            for (var i = 0; i < type33_topic.length; i++) {
                $("#topic").prepend(
                    `<option value="` + type33_topic[i] + `">` + type33_topic[i] + `</option>`
                );
            }
            $("#topic").on("change", function() {
                var topic = $("#topic").val();
                type33_problem.get(topic);
                $("#chapter").html("");
                console.log(type33_problem.get(topic))
                for (var k = 0; k < type33_problem.get(topic).length; k++) {
                    $("#chapter").append(
                        ` <option value="` + type33_problem.get(topic)[k] + `" >` + type33_problem.get(topic)[k] + `</option>`
                    ).multipleSelect('refresh');
                }
            });

        } else if ($("#subject").val() == "22KV") {
            for (var i = 0; i < type22_topic.length; i++) {
                $("#topic").prepend(
                    `<option value="` + type22_topic[i] + `">` + type22_topic[i] + `</option>`
                );
            }
            $("#topic").on("change", function() {
                var topic = $("#topic").val();
                type22_problem.get(topic);
                $("#chapter").html("");
                console.log(type22_problem.get(topic))
                for (var k = 0; k < type22_problem.get(topic).length; k++) {
                    $("#chapter").append(
                        ` <option value="` + type22_problem.get(topic)[k] + `" >` + type22_problem.get(topic)[k] + `</option>`
                    ).multipleSelect('refresh');
                }
            });

        }

    });

}


function addData() {
    $("#subject").append(
        ` <option value=" " selected="selected">ประเภทอุปกรณ์</option>`
    );
    $("#topic").append(
        `<option value=" " selected="selected">ชนิดอุปกรณ์</option>`
    );
    $("#chapter").append(
        `<option value=" " selected="selected">สาเหตุการชำรุด</option>`
    );
    for (var i = 0; i < typeData.length; i++) {
        $("#subject").append(
            `<option value="` + typeData[i] + `" >` + typeData[i] + `</option>`
        )
    }

}