<?php
fscanf(STDIN, "%d", $n);
$s = fgets(STDIN);
if($n % 2 === 1) {
    echo "No";
} else if($n % 2 === 0) {
    $error = 0;
    for($i = 0; $i < $n/2; $i++) {
        if($s[$i] !== $s[$i + $n/2]) {
            $error = 1;
        }
    }
}
if($error === 1) {
    echo "No";
} else if($error === 0) {
    echo "Yes";
}