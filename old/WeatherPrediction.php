<?php
$s = trim(fgets(STDIN));
if($s === "Sunny") {
    echo "Cloudy";
} elseif ( $s === "Cloudy") {
    echo "Rainy";
} elseif ( $s === "Rainy") {
    echo "Sunny";
}
