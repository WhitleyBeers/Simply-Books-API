CREATE TABLE `Authors` (
        `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `email` TEXT NOT NULL,
        `first_name`    TEXT NOT NULL,
        `last_name`    TEXT NOT NULL,
        `image`    TEXT NOT NULL,
        `favorite`  BOOLEAN FALSE
);

CREATE TABLE `Books` (
        `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `title` TEXT NOT NULL,
        `image` TEXT NOT NULL,
        `price` FLOAT NOT NULL,
        `sale`  BOOLEAN FALSE,
        `description`   TEXT NOT NULL,
        `author_id` INTEGER NOT NULL,
        FOREIGN KEY(`author_id`) REFERENCES `Authors`(`id`)
);

INSERT INTO `Authors` VALUES (null, "molly@doyle.com", "Molly", "Doyle", "url placeholder", True)
INSERT INTO `Books` VALUES (null, "Bloodshed", "url placeholder", 16.00, True, "A full-length novel focused on the favorite Masked Men. We like to believe monsters don't exist, even in the moonlit streets of a place like Salem, Massachusetts. But they're very real... and very human.", 1)

INSERT INTO `Authors` VALUES (null, "lemony@snicket.com", "Lemony", "Snicket", "url placeholder", False);
INSERT INTO `Authors` VALUES (null, "stephenie@meyer.com", "Stephenie", "Meyer", "url placeholder", False);
INSERT INTO `Books` VALUES (null, "The Grim Grotto", "url placeholder", 12.99, False, "The Grim Grotto is the eleventh novel in the children's book series A Series of Unfortunate Events by Lemony Snicket.", 2);
