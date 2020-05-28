<?php
fscanf(STDIN, "%d %d", $a, $b);
$loop = 1;
$multi = 1;
$greater = max($a,$b);
$less = min($a,$b);
while($loop === 1) {
    if(($greater * $multi) % $less === 0) {
    $loop = 0;
    break;
    } else {
        $multi++;
    }
}
echo $greater * $multi;