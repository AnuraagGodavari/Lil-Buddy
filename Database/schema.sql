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

CREATE TABLE IF NOT EXISTS `WatchStatuses` (
	`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`user_id` BIGINT UNSIGNED NOT NULL,
	`status` VARCHAR(129),
	`status_channel` BIGINT UNSIGNED NOT NULL,
	`created` timestamp NOT NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`id`)
); 
