<?php
fscanf(STDIN, "%d %d", $n, $m);
$a = array_map('intval', explode(' ', trim(fgets(STDIN))));
$queue = new SplPriorityQueue();
for($i=0; $i<$n; $i++) {
    // $queue->insert(a,b); $queueにaの値を優先度bで挿入
    $queue->insert($a[$i], $a[$i]);
}
while($m) {
    // $queue->extract(); $queueの最も優先度の高いキューを取り出す(取り出した後はキューから値が消える)
    $max = $queue->extract();
    $max = intval($max/2);
    $queue->insert($max, $max);
    $m--;
}
// $queue->count(); $queueの中のキュー数を数える。
$count = $queue->count();
$ans = 0;
for($i=0; $i<$count; $i++) {
    $ans += $queue->extract();
}
echo $ans;
