<?php
fscanf(STDIN, "%d", $n);
$a = explode(" ",(trim(fgets(STDIN))));
asort($a);
foreach($a as $key => $value) {
    echo ($key+1) . " ";
}