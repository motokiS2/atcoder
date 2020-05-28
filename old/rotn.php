<?php
fscanf(STDIN, "%d", $n);
$s = trim(fgets(STDIN));
$list = range("A", "Z");
$length = strlen($s);
for($i = 0; $i < $length; $i++) {
    $skey = array_search($s[$i], $list);
    $moveKey = ($skey + $n) % 26;
    echo $list[$moveKey];
}
