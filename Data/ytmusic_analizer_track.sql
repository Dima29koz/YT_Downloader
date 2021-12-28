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
-- Table structure for table `track`
--

DROP TABLE IF EXISTS `track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `track` (
  `id_track` varchar(40) NOT NULL,
  `title` varchar(45) NOT NULL,
  `year` int DEFAULT NULL,
  `track_number` int DEFAULT NULL,
  `disk_number` int DEFAULT '1',
  `tr_genre_id` int DEFAULT NULL,
  `lyrics` text,
  `duration` int DEFAULT NULL,
  PRIMARY KEY (`id_track`),
  KEY `genre_id_idx` (`tr_genre_id`),
  CONSTRAINT `tr_genre_id` FOREIGN KEY (`tr_genre_id`) REFERENCES `genres` (`id_genre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `track`
--

LOCK TABLES `track` WRITE;
/*!40000 ALTER TABLE `track` DISABLE KEYS */;
INSERT INTO `track` VALUES ('-grPV-Fae6I','Not Afraid',NULL,7,1,NULL,NULL,248),('-_Vb3qAjKM0','Anthem Of The Lonely',NULL,1,1,NULL,NULL,241),('0hcOeACHbVc','Scars that I\'m Hiding',NULL,1,1,NULL,NULL,176),('0m7puo2uBzA','Feel Invincible',NULL,1,1,NULL,NULL,230),('5gF2F51GAj0','Come Undone',NULL,8,1,NULL,NULL,248),('8onXlXfbOXs','War of Change',NULL,10,1,NULL,NULL,231),('dPqixofTN98','Monster',NULL,13,1,NULL,NULL,256),('h2cd5JyPR5o','The Only',NULL,7,1,NULL,NULL,172),('I11KN8kWo2M','Heart Of A Champion (feat. Ice Nine Kills & P',NULL,10,1,NULL,NULL,211),('Mph84UBO1as','It Has Begun',NULL,6,1,NULL,NULL,316),('MYK040Jd3d8','Bulletproof',NULL,8,1,NULL,NULL,208),('nSDYRXbAxC4','Koktejl',NULL,2,1,NULL,NULL,183),('Q9BHJQZAP2o','Still Waiting',NULL,4,1,NULL,NULL,158),('qJRqbAL6LTI','Тело',NULL,4,1,NULL,NULL,225),('QpFOTXYs438','Pieces',NULL,11,1,NULL,NULL,183),('SDnECdi4tMc','Танцуй на костях',NULL,7,1,NULL,NULL,182),('SkOAP2TwjSg','Leave It All Behind',NULL,1,1,NULL,NULL,225),('TYrDI-Aad1s','Halo',NULL,3,1,NULL,NULL,225),('USR0g4_J4_4','More Than You Know',NULL,1,1,NULL,NULL,202),('xsXgXf0ygTA','Blind',NULL,4,1,NULL,NULL,166),('yN66LdJx-pE','Brick',NULL,2,1,NULL,NULL,204),('yW1jU3Fv528','Death Of Me',NULL,10,1,NULL,NULL,181);
/*!40000 ALTER TABLE `track` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-28 16:30:22
