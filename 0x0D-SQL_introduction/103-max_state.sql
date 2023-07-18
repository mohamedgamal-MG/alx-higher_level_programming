-- script display the max temp.
SELECT `state`, MAX(`value`) AS `max_temp`
GROUP BY `state`
ORDER BY `max_temp` DESC;

