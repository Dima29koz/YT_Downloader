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
-- Table structure for table `artist_album`
--

DROP TABLE IF EXISTS `artist_album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_album` (
  `artist_album` int NOT NULL AUTO_INCREMENT,
  `id_artist` varchar(40) NOT NULL,
  `id_album` varchar(40) NOT NULL,
  PRIMARY KEY (`artist_album`),
  KEY `id_artist_idx` (`id_artist`),
  KEY `id_album_idx` (`id_album`),
  CONSTRAINT `id_album_art` FOREIGN KEY (`id_album`) REFERENCES `album` (`id_album`),
  CONSTRAINT `id_artist_alb` FOREIGN KEY (`id_artist`) REFERENCES `artists` (`id_artist`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_album`
--

LOCK TABLES `artist_album` WRITE;
/*!40000 ALTER TABLE `artist_album` DISABLE KEYS */;
INSERT INTO `artist_album` VALUES (79,'UC02e0Ntqqe7JSRkXTfy1R8g','MPREb_bLo81dYH6Na'),(80,'UC5Lsr6bVLulAFbSRwCKt3tg','MPREb_sW9YUpBLOGw'),(81,'UC_tC_1RE-4nxKXoyjPjiRbQ','MPREb_sW9YUpBLOGw'),(82,'UCJif7WIflX_1Jg5RypJjqnw','MPREb_v7Ub5XgdI8k'),(83,'UCJif7WIflX_1Jg5RypJjqnw','MPREb_v7Ub5XgdI8k'),(84,'UCzYd1EYoMbG8tFWQ69Odi4Q','MPREb_WuipnfO4lQw'),(85,'UCcucrfDVx-WyEtb8mQIKj0A','MPREb_KRpzc1wcZNm'),(86,'UCcMcUoDPCQhtONMyuKJs-dg','MPREb_c6QjKoWibkc'),(87,'UC_o4Fz0kJt1pY-45KT10BEA','MPREb_WqATcp72Irc'),(88,'UC8w5xrdhxbzOWm21eBBYqSA','MPREb_IWUeCDFDP4I'),(89,'UCJif7WIflX_1Jg5RypJjqnw','MPREb_v7Ub5XgdI8k'),(90,'UCzYd1EYoMbG8tFWQ69Odi4Q','MPREb_gbtBjQn8JXf'),(91,'UC0OKzXpwi1XsYlld_XzYx7w','MPREb_OO063RUCmxw'),(92,'UCE9L8h3LgZRSudpWLahhGuQ','MPREb_vn8w6DKmlHQ'),(93,'UCcMcUoDPCQhtONMyuKJs-dg','MPREb_keJO6XJy5nO'),(94,'UCFaZ4xC5bMx6tlazsuA4wdg','MPREb_cGg2ooQRuwQ'),(95,'UCzYd1EYoMbG8tFWQ69Odi4Q','MPREb_ZvM9V7DBuyy'),(96,'UCedvOgsKFzcK3hA5taf3KoQ','MPREb_UUFKiZYr3uO'),(97,'UCJif7WIflX_1Jg5RypJjqnw','MPREb_v7Ub5XgdI8k'),(98,'UCDssrdgCuRtfpjfMc_hsYRw','MPREb_g6GwtcGLCJk'),(99,'UC0OestVal7P0ltKyVvbwxyw','MPREb_zioMNYHmNn9'),(100,'UCUHYrf3BF5yI9QdRw09__BA','MPREb_U6SwkJdwCvX'),(101,'UCJif7WIflX_1Jg5RypJjqnw','MPREb_v7Ub5XgdI8k');
/*!40000 ALTER TABLE `artist_album` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-28 16:30:20
