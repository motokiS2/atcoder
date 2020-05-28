<?php
fscanf(STDIN, "%d", $n);
$kuku = array();
$judge = 0;
for($i = 1; $i < 10; $i++) {
    for($j = 1; $j < 10; $j++) {
        $kuku[$i][$j] = $i * $j;
    }
}
for($i = 1; $i < 10; $i++) {
    for($j = 1; $j < 10; $j++) {
        if($n === $kuku[$i][$j]) {
            $judge = 1;
        }
    }
}
if($judge === 1) {
    echo "Yes";
} else {
    echo "No";
}