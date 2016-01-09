-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u2
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Sam 09 Janvier 2016 à 20:29
-- Version du serveur: 5.5.46
-- Version de PHP: 5.4.45-0+deb7u2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `elitedangerous`
--

-- --------------------------------------------------------

--
-- Structure de la table `commodity`
--

CREATE TABLE IF NOT EXISTS `commodity` (
  `commodity_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`commodity_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=107 ;

-- --------------------------------------------------------

--
-- Structure de la table `market`
--

CREATE TABLE IF NOT EXISTS `market` (
  `station_id` int(11) NOT NULL,
  `commodity_id` int(11) NOT NULL,
  `buyPrice` int(11) NOT NULL,
  `sellPrice` int(11) NOT NULL,
  `demand` int(11) NOT NULL,
  `supply` int(11) NOT NULL,
  `last_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`station_id`,`commodity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `route`
--

CREATE TABLE IF NOT EXISTS `route` (
  `route_id` int(11) NOT NULL AUTO_INCREMENT,
  `source_id` int(11) NOT NULL,
  `destination_id` int(11) NOT NULL,
  `commodity_id` int(11) NOT NULL,
  `buyPrice` float NOT NULL,
  `sellPrice` float NOT NULL,
  `profit` int(11) NOT NULL,
  `distance` int(11) NOT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `station`
--

CREATE TABLE IF NOT EXISTS `station` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `system_id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `imported_id` int(11) DEFAULT NULL,
  `dist_from_star` float DEFAULT NULL,
  PRIMARY KEY (`station_id`),
  KEY `imported_id` (`imported_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3792 ;

-- --------------------------------------------------------

--
-- Structure de la table `system`
--

CREATE TABLE IF NOT EXISTS `system` (
  `system_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `x` float DEFAULT NULL,
  `y` float DEFAULT NULL,
  `z` float DEFAULT NULL,
  `imported_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`system_id`),
  KEY `imported_id` (`imported_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=8938 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
