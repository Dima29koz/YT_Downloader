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
-- Table structure for table `video_song`
--

DROP TABLE IF EXISTS `video_song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `video_song` (
  `id_Video` varchar(40) NOT NULL,
  `id_song` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_Video`),
  KEY `id_song_idx` (`id_song`),
  CONSTRAINT `id_song` FOREIGN KEY (`id_song`) REFERENCES `track` (`id_track`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video_song`
--

LOCK TABLES `video_song` WRITE;
/*!40000 ALTER TABLE `video_song` DISABLE KEYS */;
INSERT INTO `video_song` VALUES ('-grPV-Fae6I','-grPV-Fae6I'),('-_Vb3qAjKM0','-_Vb3qAjKM0'),('0hcOeACHbVc','0hcOeACHbVc'),('0m7puo2uBzA','0m7puo2uBzA'),('5gF2F51GAj0','5gF2F51GAj0'),('8onXlXfbOXs','8onXlXfbOXs'),('dPqixofTN98','dPqixofTN98'),('h2cd5JyPR5o','h2cd5JyPR5o'),('I11KN8kWo2M','I11KN8kWo2M'),('Mph84UBO1as','Mph84UBO1as'),('MYK040Jd3d8','MYK040Jd3d8'),('nSDYRXbAxC4','nSDYRXbAxC4'),('Q9BHJQZAP2o','Q9BHJQZAP2o'),('qJRqbAL6LTI','qJRqbAL6LTI'),('QpFOTXYs438','QpFOTXYs438'),('s6tmab1hPpk','SDnECdi4tMc'),('SkOAP2TwjSg','SkOAP2TwjSg'),('TYrDI-Aad1s','TYrDI-Aad1s'),('USR0g4_J4_4','USR0g4_J4_4'),('xsXgXf0ygTA','xsXgXf0ygTA'),('yN66LdJx-pE','yN66LdJx-pE'),('yW1jU3Fv528','yW1jU3Fv528');
/*!40000 ALTER TABLE `video_song` ENABLE KEYS */;
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
