// Paste here the data from a specific network
const data = [21,  35,  66,  67,  83,  90,  91, 106, 119, 123, 124, 134,
    137, 158, 167, 175, 200, 204, 212, 213, 234, 235, 251, 259,
    260, 261, 274, 280, 295, 300, 306, 313, 320, 327, 337, 350,
    356, 383, 397, 398, 398, 409, 413, 417, 434, 457, 458, 460,
    463, 466, 470, 482, 483, 487, 492, 502, 511, 515, 519, 528,
    536, 547, 548, 562, 571, 574, 576, 577, 583, 586, 588, 617,
    620, 620, 622, 624, 624, 625, 628, 661, 664, 671, 679, 689,
    694, 699, 700, 706, 711, 712, 750, 773, 782, 794, 805, 809,
    816, 881, 902, 945
];

const resolution = 10;
const percentile = data[data.length - 1] / resolution;
let limit = percentile;
let y = 0;
let sparkline = '0 0 ';
let sparkspikes = '';

for (let i = 1; i < (resolution + 1); i++) {
    let limit = percentile * i;
    let y = data.filter(d => d <= limit && d > percentile * (i - 1)).length;
    sparkline += `${i / resolution} ${y / data.length} `
    sparkspikes += `\\sparkspike ${i / resolution} ${y / data.length} `
}
console.log(sparkline);
console.log(sparkspikes);