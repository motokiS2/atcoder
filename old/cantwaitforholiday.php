<?php
$s = trim(fgets(STDIN));
if($s === "SUN") {
    $nextSun = 7;
} elseif($s === "MON") {
    $nextSun = 6;
} elseif($s === "TUE") {
    $nextSun = 5;
} elseif($s === "WED") {
    $nextSun = 4;
} elseif($s === "THU") {
    $nextSun = 3;
} elseif($s === "FRI") {
    $nextSun = 2;
} elseif($s === "SAT") {
    $nextSun = 1;
}
echo $nextSun . PHP_EOL;