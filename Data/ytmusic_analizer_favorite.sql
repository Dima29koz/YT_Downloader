-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: ytmusic_analizer
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorite`
--

DROP TABLE IF EXISTS `favorite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorite` (
  `favorite_user` int NOT NULL AUTO_INCREMENT,
  `user_email` varchar(255) NOT NULL,
  `id_track` varchar(40) NOT NULL,
  `downloaded` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`favorite_user`),
  KEY `user_email_idx` (`user_email`),
  KEY `id_track_idx` (`id_track`),
  CONSTRAINT `id_track_fav` FOREIGN KEY (`id_track`) REFERENCES `track` (`id_track`),
  CONSTRAINT `user_email` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorite`
--

LOCK TABLES `favorite` WRITE;
/*!40000 ALTER TABLE `favorite` DISABLE KEYS */;
INSERT INTO `favorite` VALUES (157,'Dima29koz@yandex.ru','I11KN8kWo2M',0),(158,'Dima29koz@yandex.ru','SDnECdi4tMc',0),(159,'Dima29koz@yandex.ru','yN66LdJx-pE',0),(160,'Dima29koz@yandex.ru','MYK040Jd3d8',0),(161,'Dima29koz@yandex.ru','Mph84UBO1as',0),(162,'Dima29koz@yandex.ru','USR0g4_J4_4',0),(163,'Dima29koz@yandex.ru','QpFOTXYs438',0),(164,'Dima29koz@yandex.ru','8onXlXfbOXs',0),(165,'Dima29koz@yandex.ru','nSDYRXbAxC4',0),(166,'Dima29koz@yandex.ru','0hcOeACHbVc',0),(167,'Dima29koz@yandex.ru','TYrDI-Aad1s',0),(168,'Dima29koz@yandex.ru','-_Vb3qAjKM0',0),(169,'Dima29koz@yandex.ru','5gF2F51GAj0',0),(170,'Dima29koz@yandex.ru','Q9BHJQZAP2o',0),(171,'Dima29koz@yandex.ru','SkOAP2TwjSg',0),(172,'Dima29koz@yandex.ru','dPqixofTN98',0),(173,'Dima29koz@yandex.ru','-grPV-Fae6I',0),(174,'Dima29koz@yandex.ru','yW1jU3Fv528',0),(175,'Dima29koz@yandex.ru','h2cd5JyPR5o',0),(176,'Dima29koz@yandex.ru','qJRqbAL6LTI',0),(177,'Dima29koz@yandex.ru','0m7puo2uBzA',0),(178,'Dima29koz@yandex.ru','xsXgXf0ygTA',0);
/*!40000 ALTER TABLE `favorite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-28 16:30:21
