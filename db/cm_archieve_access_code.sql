CREATE DATABASE  IF NOT EXISTS `cm_archieve` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cm_archieve`;
-- MySQL dump 10.13  Distrib 5.6.14, for Win32 (x86)
--
-- Host: 125.211.221.215    Database: cm_archieve
-- ------------------------------------------------------
-- Server version	5.5.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `access_code`
--

DROP TABLE IF EXISTS `access_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `access_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `archieve_id` varchar(20) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_code`
--

LOCK TABLES `access_code` WRITE;
/*!40000 ALTER TABLE `access_code` DISABLE KEYS */;
INSERT INTO `access_code` VALUES (1,'230102198101201037','1123','2014-01-06'),(4,'230102198101201037','8947','2014-01-17'),(5,'230102198101201037','1596','2014-01-17'),(6,'230102198101201037','3706','2014-01-17'),(7,'230102198101201037','7438','2014-01-20'),(8,'230184197001306317','4610','2014-01-20'),(9,'230102198101201037','1123','2014-01-20'),(10,'230102198101201037','9249','2014-01-22'),(11,'230102198101201037','5009','2014-01-22'),(12,'230102198101201037','1773','2014-01-22'),(13,'230102198101201037','3669','2014-01-22'),(14,'230102198101201037','2806','2014-01-25'),(15,'230102198101201037','6638','2014-01-27'),(16,'230102198101201037','1925','2014-01-27'),(17,'230102198101201037','6806','2014-03-11'),(18,'230102198101201037','4032','2014-03-19'),(19,'230102198101201037','4079','2014-04-09'),(20,'230102198101201037','4762','2014-04-20');
/*!40000 ALTER TABLE `access_code` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-23 23:06:52
