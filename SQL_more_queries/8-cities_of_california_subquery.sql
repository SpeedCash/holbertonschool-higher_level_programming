-- Lists all cities of California in the hbtn_0d_usa database without using JOIN
SELECT cities.id, cities.name 
FROM cities, states 
WHERE cities.state_id = states.id AND states.name = 'California' 
ORDER BY cities.id ASC;
