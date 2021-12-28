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
-- Table structure for table `album_track`
--

DROP TABLE IF EXISTS `album_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_track` (
  `album_track` int NOT NULL AUTO_INCREMENT,
  `id_track` varchar(40) NOT NULL,
  `id_album` varchar(40) NOT NULL,
  PRIMARY KEY (`album_track`),
  KEY `id_track_idx` (`id_track`),
  KEY `id_album_idx` (`id_album`),
  CONSTRAINT `id_album_tr` FOREIGN KEY (`id_album`) REFERENCES `album` (`id_album`),
  CONSTRAINT `id_track_alb` FOREIGN KEY (`id_track`) REFERENCES `track` (`id_track`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_track`
--

LOCK TABLES `album_track` WRITE;
/*!40000 ALTER TABLE `album_track` DISABLE KEYS */;
INSERT INTO `album_track` VALUES (77,'I11KN8kWo2M','MPREb_bLo81dYH6Na'),(78,'SDnECdi4tMc','MPREb_sW9YUpBLOGw'),(79,'yN66LdJx-pE','MPREb_v7Ub5XgdI8k'),(80,'MYK040Jd3d8','MPREb_v7Ub5XgdI8k'),(81,'Mph84UBO1as','MPREb_WuipnfO4lQw'),(82,'USR0g4_J4_4','MPREb_KRpzc1wcZNm'),(83,'QpFOTXYs438','MPREb_c6QjKoWibkc'),(84,'8onXlXfbOXs','MPREb_WqATcp72Irc'),(85,'nSDYRXbAxC4','MPREb_IWUeCDFDP4I'),(86,'0hcOeACHbVc','MPREb_v7Ub5XgdI8k'),(87,'TYrDI-Aad1s','MPREb_gbtBjQn8JXf'),(88,'-_Vb3qAjKM0','MPREb_OO063RUCmxw'),(89,'5gF2F51GAj0','MPREb_vn8w6DKmlHQ'),(90,'Q9BHJQZAP2o','MPREb_keJO6XJy5nO'),(91,'SkOAP2TwjSg','MPREb_cGg2ooQRuwQ'),(92,'dPqixofTN98','MPREb_ZvM9V7DBuyy'),(93,'-grPV-Fae6I','MPREb_UUFKiZYr3uO'),(94,'yW1jU3Fv528','MPREb_v7Ub5XgdI8k'),(95,'h2cd5JyPR5o','MPREb_g6GwtcGLCJk'),(96,'qJRqbAL6LTI','MPREb_zioMNYHmNn9'),(97,'0m7puo2uBzA','MPREb_U6SwkJdwCvX'),(98,'xsXgXf0ygTA','MPREb_v7Ub5XgdI8k');
/*!40000 ALTER TABLE `album_track` ENABLE KEYS */;
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
