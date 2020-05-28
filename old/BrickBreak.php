<?php
$n = intval(trim(fgets(STDIN)));
$a = array_map('intval', explode(' ', trim(fgets(STDIN))));
$check = 1;
$break = 0;
for($i = 0; $i < $n; $i++) {
    if($a[$i] === $check) {
        $check++;
    } else {
        $break++;
    }
}
if($break === $n) {
    echo -1;
} else {
    echo $break;
}