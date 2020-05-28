<?php
fscanf(STDIN, "%d %d", $n, $m);
$p = array();
for($i = 0; $i < $m; $i++) {
    $p[] = explode(" ",trim(fgets(STDIN)));
}
