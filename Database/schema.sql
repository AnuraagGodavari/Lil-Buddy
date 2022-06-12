DROP DATABASE LilBuddy;

CREATE DATABASE IF NOT EXISTS LilBuddy DEFAULT CHARACTER SET = 'utf8mb4';

USE LilBuddy;

CREATE TABLE IF NOT EXISTS `Servers` (
	`discord_id` int(24) NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`discord_id`)
);

CREATE TABLE IF NOT EXISTS `Users` (
	`discord_id` int(24) NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`discord_id`)
);

CREATE TABLE IF NOT EXISTS `WatchStatuses` (
	`id` int(10) NOT NULL,
	`user_id` int(24) NOT NULL,
	`status` VARCHAR(129),
	`status_channel` int(24) NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`user_id`),
	CONSTRAINT `WatchStatuses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`discord_id`)
);