<?php

fscanf(STDIN, "%s", $s);

$rs = strrev($s);
$count = 0;
for($i = 0; $i < strlen($s); $i++) {
    if($s[$i] !== $rs[$i]) {
        $count++;
    }
}

echo $count / 2;