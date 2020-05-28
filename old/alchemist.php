<?php
fscanf(STDIN, "%d", $n);
$v = explode(" ",fgets(STDIN));
for($i=0; $i<$n; $i++) {
    $v[$i] = intval($v[$i]);
}
sort($v);
for($i=0; $i<$n-1; $i++) {
    $v[$i+1] = ($v[$i]+$v[$i+1])/2;
}
echo $v[$n-1];
?>