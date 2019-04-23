use sakila;

select * from actor;

#1a
SELECT first_name AS "First Name", last_name AS "Last Name" 
FROM actor;

#1b
SELECT concat(first_name, " ", last_name) AS "Actor Name"
FROM actor;

#2a
SELECT actor_id AS "Actor ID", first_name AS "First Name", last_name AS "Last Name"
FROM actor
WHERE first_name = "JOE";

#2b
SELECT actor_id AS "Actor ID", first_name AS "First Name", last_name AS "Last Name"
FROM actor
WHERE last_name like "%GEN%";

#2c 
SELECT actor_id AS "Actor ID", last_name AS "Last Name", first_name AS "First Name"
FROM actor
WHERE last_name like "%LI%";

#2d
SELECT country_id AS "Country ID", country AS "Country"
FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

#3a
ALTER TABLE actor add column description blob;
select * from actor;

#3b
ALTER TABLE actor DROP COLUMN description;
SELECT * FROM actor;

#4a
SELECT distinct last_name AS "Distinct Last names", count(last_name) AS "Last Name Count"
FROM actor
group by last_name;

#4b
SELECT distinct last_name AS "Distinct Last names", count(last_name) AS "Last Name Count"
FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;

#4c
UPDATE actor
SET first_name = "HARPO"
WHERE actor.actor_id = (
	SELECT actor_id 
    FROM (SELECT actor_id 
		FROM actor
		WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS"
) AS temp);

#4d
UPDATE actor
SET first_name = "GROUCHO"
WHERE actor.actor_id = (
	SELECT actor_id 
    FROM (SELECT actor_id 
		FROM actor
		WHERE first_name = "HARPO" AND last_name = "WILLIAMS"
) AS temp);
use sakila;
select * from address;
#5d
use sakila;
CREATE TABLE address (
	address_id INT PRIMARY KEY AUTO_INCREMENT,
    address varchar(30) NOT NULL,
    address2 varchar(30),
    district varchar (20),
    city_id int NOT NULL,
    postal_code INT,
    phone INT,
    location BLOB,
    last_update DATETIME
);

#6a
SELECT concat(staff.first_name, " ", staff.last_name) "Staff Name", address.address "Address"
FROM staff
INNER JOIN address on address.address_id = staff.address_id;

#6b
SELECT concat(staff.first_name, " ", staff.last_name) "Staff Name", SUM(amount) "Amount Rung \n August 2005"
FROM staff
INNER JOIN payment ON payment.staff_id = staff.staff_id
WHERE payment.payment_date LIKE "2005-08%" GROUP BY payment.staff_id;

#6c
SELECT title AS "Movie Title", COUNT(actor_id) AS "Number of Actors in the Movie"	
FROM film_actor
INNER JOIN film ON film.film_id = film_actor.film_id
GROUP BY film_actor.film_id;

#6d
SELECT count(film_id) FROM inventory
WHERE film_id in (Select film.film_id from film where film.title = "Hunchback Impossible")
GROUP BY film_id;

