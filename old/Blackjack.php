<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);

$sum = $a + $b + $c;

if($sum >= 22) {
    echo 'bust';
} else {
    echo 'win';
}

?>