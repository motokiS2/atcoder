<?php
$n = intval(trim(fgets(STDIN)));

for($i = 0; $i < $n; $i++) {
    $a[] = intval(trim(fgets(STDIN)));
    for($j = 0; $j < $a[$i]; $j++) {
        $xy[$i][] = array_map('intval', explode(' ', trim(fgets(STDIN))));
    }
}
$honest = array();
$honest[0] = 1;

if ($honest[0] === 1) {
    $honest[$xy[0]]
}

?>