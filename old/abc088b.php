<?php
$num = intval(trim(fgets(STDIN)));
$cardVal = explode(" ", trim(fgets(STDIN)));
rsort($cardVal);
$ans = 0;
for ($i=0; $i<$num; $i++){
    if ($i %2 == 0) {
        $ans += $cardVal[$i];
    } else {
        $ans -= $cardVal[$i];
    }
}
echo $ans;
?>