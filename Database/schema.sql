DROP DATABASE LilBuddy;

CREATE DATABASE IF NOT EXISTS LilBuddy DEFAULT CHARACTER SET = 'utf8mb4';

USE LilBuddy;

CREATE TABLE IF NOT EXISTS `Servers` (
	`discord_id` BIGINT UNSIGNED NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`discord_id`)
);

CREATE TABLE IF NOT EXISTS `Users` (
	`discord_id` BIGINT UNSIGNED NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`discord_id`)
);

CREATE TABLE IF NOT EXISTS `WatchingStatus` (
	`user_id` BIGINT UNSIGNED NOT NULL,
	`status_channel` BIGINT UNSIGNED NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`user_id`),
	CONSTRAINT `WatchingStatus_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`discord_id`)
); 

CREATE TABLE IF NOT EXISTS `Statuses` (
	`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`user_id` BIGINT UNSIGNED NOT NULL,
	`status` VARCHAR(129),
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`id`),
	CONSTRAINT `Statuses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`discord_id`)
);
