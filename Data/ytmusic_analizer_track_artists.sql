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
-- Table structure for table `track_artists`
--

DROP TABLE IF EXISTS `track_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `track_artists` (
  `track_artists` int NOT NULL AUTO_INCREMENT,
  `id_track` varchar(40) NOT NULL,
  `id_artist` varchar(40) NOT NULL,
  PRIMARY KEY (`track_artists`),
  KEY `id_track_idx` (`id_track`),
  KEY `id artist_idx` (`id_artist`),
  CONSTRAINT `id_artist_tr` FOREIGN KEY (`id_artist`) REFERENCES `artists` (`id_artist`),
  CONSTRAINT `id_track_art` FOREIGN KEY (`id_track`) REFERENCES `track` (`id_track`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `track_artists`
--

LOCK TABLES `track_artists` WRITE;
/*!40000 ALTER TABLE `track_artists` DISABLE KEYS */;
INSERT INTO `track_artists` VALUES (83,'I11KN8kWo2M','UC02e0Ntqqe7JSRkXTfy1R8g'),(84,'SDnECdi4tMc','UC5Lsr6bVLulAFbSRwCKt3tg'),(85,'SDnECdi4tMc','UC_tC_1RE-4nxKXoyjPjiRbQ'),(86,'yN66LdJx-pE','UCJif7WIflX_1Jg5RypJjqnw'),(87,'MYK040Jd3d8','UCJif7WIflX_1Jg5RypJjqnw'),(88,'Mph84UBO1as','UCzYd1EYoMbG8tFWQ69Odi4Q'),(89,'USR0g4_J4_4','UCcucrfDVx-WyEtb8mQIKj0A'),(90,'QpFOTXYs438','UCcMcUoDPCQhtONMyuKJs-dg'),(91,'8onXlXfbOXs','UC_o4Fz0kJt1pY-45KT10BEA'),(92,'nSDYRXbAxC4','UC8w5xrdhxbzOWm21eBBYqSA'),(93,'0hcOeACHbVc','UCJif7WIflX_1Jg5RypJjqnw'),(94,'TYrDI-Aad1s','UCzYd1EYoMbG8tFWQ69Odi4Q'),(95,'-_Vb3qAjKM0','UC0OKzXpwi1XsYlld_XzYx7w'),(96,'5gF2F51GAj0','UCE9L8h3LgZRSudpWLahhGuQ'),(97,'Q9BHJQZAP2o','UCcMcUoDPCQhtONMyuKJs-dg'),(98,'SkOAP2TwjSg','UCFaZ4xC5bMx6tlazsuA4wdg'),(99,'dPqixofTN98','UCzYd1EYoMbG8tFWQ69Odi4Q'),(100,'-grPV-Fae6I','UCedvOgsKFzcK3hA5taf3KoQ'),(101,'yW1jU3Fv528','UCJif7WIflX_1Jg5RypJjqnw'),(102,'h2cd5JyPR5o','UCDssrdgCuRtfpjfMc_hsYRw'),(103,'qJRqbAL6LTI','UC0OestVal7P0ltKyVvbwxyw'),(104,'0m7puo2uBzA','UCUHYrf3BF5yI9QdRw09__BA'),(105,'xsXgXf0ygTA','UCJif7WIflX_1Jg5RypJjqnw');
/*!40000 ALTER TABLE `track_artists` ENABLE KEYS */;
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
