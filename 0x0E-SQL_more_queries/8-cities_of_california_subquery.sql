-- lists all the cities of California that can be found in the database.
-- WHERE -  relational database management system.
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name ="California"
);
