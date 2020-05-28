<?php
fscanf(STDIN, "%d %d", $a, $b);
function gcd($x,$y){
    if($y === 0) {
        return $x;
    } else {
        return gcd($y, $x%$y);
    }
}
$gcd = gcd($a, $b);

$init = 2;
$comPrime = array();
while($init <= floor(sqrt($gcd))){
    if($gcd % $init === 0) {
        $gcd /= $init;
        $comPrime[] = $init;
    } else {
        $init++;
    }
}
if($gcd > 1){
    $comPrime[] = $gcd;
}
$uniquePrime = array_unique($comPrime);
echo count($uniquePrime) + 1;