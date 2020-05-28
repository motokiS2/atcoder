<?php
fscanf(STDIN, "%d %d %d", $a, $b, $k);
if($k > $a) {
    echo 0 . " " . max(($a + $b - $k), 0);
} elseif($k <= $a) {
    echo $a - $k . " " . $b;
}