<?php
fscanf(STDIN, "%d %d", $n, $q);

for($i=0; $i<$n-1; $i++) {
    fscanf(STDIN, "%d %d", $a, $b);
    $node[$b] = $a;
}
$count = array_fill(1,$n,0);
while ($q--) {
    fscanf(STDIN, "%d %d", $p, $x);
    $count[$p] += $x;
}
$t = [$count[1]];
for ($i = 2; $i <= $n; $i++) {
	$t[] = $count[$i] += $count[$node[$i]];
}
echo implode(' ', $t);