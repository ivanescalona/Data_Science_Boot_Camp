USE sakila;

SELECT * FROM actOR;

#1a
SELECT first_name AS "First Name", last_name AS "Last Name" 
FROM actOR;

#1b
SELECT concat(first_name, " ", last_name) AS "ActOR Name"
FROM actOR;

#2a
SELECT actOR_id AS "ActOR ID", first_name AS "First Name", last_name AS "Last Name"
FROM actOR
WHERE first_name = "JOE";

#2b
SELECT actOR_id AS "ActOR ID", first_name AS "First Name", last_name AS "Last Name"
FROM actOR
WHERE last_name LIKE "%GEN%";

#2c 
SELECT actOR_id AS "ActOR ID", last_name AS "Last Name", first_name AS "First Name"
FROM actOR
WHERE last_name LIKE "%LI%";

#2d
SELECT COUNTry_id AS "COUNTry ID", COUNTry AS "COUNTry"
FROM COUNTry
WHERE COUNTry IN ("Afghanistan", "Bangladesh", "China");

#3a
ALTER TABLE actOR ADD COLUMN DESCRIPTION BLOB;
SELECT * FROM actOR;

#3b
ALTER TABLE actOR DROP COLUMN DESCRIPTION;
SELECT * FROM actOR;

#4a
SELECT DISTINCT last_name AS "Distinct Last names", COUNT(last_name) AS "Last Name COUNT"
FROM actOR
GROUP BY last_name;

#4b
SELECT DISTINCT last_name AS "DISTINCT Last names", COUNT(last_name) AS "Last Name COUNT"
FROM actOR
GROUP BY last_name
HAVING COUNT(last_name) > 1;

#4c
UPDATE actOR
SET first_name = "HARPO"
WHERE actOR.actOR_id = (
	SELECT actOR_id 
    FROM (SELECT actOR_id 
		FROM actOR
		WHERE first_name = "GROUCHO" AND last_name = "WILLIAMS"
) AS temp);

#4d
UPDATE actOR
SET first_name = "GROUCHO"
WHERE actOR.actOR_id = (
	SELECT actOR_id 
    FROM (SELECT actOR_id 
		FROM actOR
		WHERE first_name = "HARPO" AND last_name = "WILLIAMS"
) AS temp);
USE sakila;
SELECT * FROM address;
#5d
USE sakila;
CREATE TABLE address (
	address_id INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(30) NOT NULL,
    address2 VARCHAR(30),
    district VARCHAR (20),
    city_id INT NOT NULL,
    postal_code INT,
    phone INT,
    location BLOB,
    last_update DATETIME
);

#6a
SELECT concat(staff.first_name, " ", staff.last_name) "Staff Name", address.address "Address"
FROM staff
INNER JOIN address ON address.address_id = staff.address_id;

#6b
SELECT concat(staff.first_name, " ", staff.last_name) "Staff Name", SUM(amount) "Amount Rung \n August 2005"
FROM staff
INNER JOIN payment ON payment.staff_id = staff.staff_id
WHERE payment.payment_date LIKE "2005-08%" GROUP BY payment.staff_id;

#6c
SELECT title AS "Movie Title", COUNT(actOR_id) AS "Number of ActORs in the Movie"	
FROM film_actOR
INNER JOIN film ON film.film_id = film_actOR.film_id
GROUP BY film_actOR.film_id;

#6d
SELECT COUNT(film_id) FROM inventORy
WHERE film_id in (SELECT film.film_id FROM film WHERE film.title = "Hunchback Impossible")
GROUP BY film_id;

#6e
SELECT concat(customer.first_name, " ", customer.last_name) "Customer Name", SUM(amount) "Total Amount Paid \n By Customer"
FROM customer
INNER JOIN payment ON payment.customer_id = customer.customer_id
GROUP BY payment.customer_id;

#7a
SELECT film.title "Movie title" FROM film
WHERE (title LIKE "k%" OR title LIKE "q%") AND film.language_id IN (
	SELECT language_id FROM language 
    WHERE language.name = "English");

#7b
SELECT concat(a.first_name, " ", a.last_name) "ActORs in the film \n \"Alone Trip\"" FROM actOR a
WHERE a.actOR_id IN (SELECT fa.actOR_id FROM film_actOR fa WHERE fa.film_id = (
	SELECT film_id FROM film
    WHERE film.title = "Alone Trip"));
    
#7c
SELECT concat(c.first_name, " ", c.last_name) "Canada Customers \n Full Name", c.email "Email Address" 
FROM customer c, address a, COUNTry con
WHERE con.COUNTry = "Canada";

#7d
SELECT f.title "Family Movies" 
FROM film f, film_categORy fc, categORy c
WHERE c.name = "Family" AND f.film_id = fc.film_id;

#7e
SELECT f.title "Movie Title", COUNT(f.title) "Frequency of movie rental"
FROM film f, rental r, inventORy i
WHERE r.inventORy_id = i.inventORy_id AND i.film_id = f.film_id
GROUP BY f.title
ORDER BY COUNT(f.title) DESC;

#7f
SELECT s.stORe_id "StORe number", SUM(p.amount) "Total revenue"
FROM payment p, rental r, customer c, stORe s
WHERE p.customer_id = c.customer_id AND c.stORe_id = s.stORe_id AND r.customer_id = c.customer_id
GROUP BY s.stORe_id;

#7g
SELECT s.stORe_id "StORe Number", ci.city "City", co.COUNTry "COUNTry"
FROM stORe s, city ci, address a, COUNTry co
WHERE s.address_id = a.address_id AND a.city_id = ci.city_id AND ci.COUNTry_id = co.COUNTry_id;

#7h
SELECT c.name "Genre", SUM(p.amount) "Total Revenue" 
FROM categORy c, payment p, film_categORy fc, inventORy i, rental r
WHERE r.inventORy_id = i.inventORy_id AND i.film_id = fc.film_id AND fc.categORy_id = c.categORy_id
AND r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY COUNT(p.amount) DESC
LIMIT 5;

#8a
CREATE VIEW top5_genres AS SELECT c.name "Genre", SUM(p.amount) "Total Revenue" 
FROM categORy c, payment p, film_categORy fc, inventORy i, rental r
WHERE r.inventORy_id = i.inventORy_id AND i.film_id = fc.film_id AND fc.categORy_id = c.categORy_id
AND r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY COUNT(p.amount) DESC
LIMIT 5;

#8b
SELECT * FROM top5_genres;

#8c
DROP VIEW IF EXISTS top5_genres;
