<?php
$s = trim(fgets(STDIN));
$len = strlen($s);
$error = 0;
for($i=0; $i<$len/2; $i++) {
    if($s[$i*2] === "L") {
        $error = 1;
    } elseif ($s[$i*2+1] === "R") {
        $error = 1;
    }
}
if($error === 0) {
    echo "Yes";
} else {
    echo "No";
}