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
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `id_artist` varchar(40) NOT NULL,
  `name` varchar(45) NOT NULL,
  `cover_art` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id_artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES ('UC02e0Ntqqe7JSRkXTfy1R8g','Hollywood Undead','https://lh3.googleusercontent.com/Z6mMQ6nOqNyFS2WHZQxyzTVG2nPOlq46QNNWnQaJPLvcq4GUw1hyWYTVCuZJeG37H2Klzt7-N8XzSyU=w2880-'),('UC0OestVal7P0ltKyVvbwxyw','ЛСП','https://lh3.googleusercontent.com/hsvFVOxQQmoNGPFaW3RFsydjUTY5ZDBIXnXXxZCjpbgFYBRcZGaMmu7srFTC4oUYp8sslfcDjX01_09w=w2880'),('UC0OKzXpwi1XsYlld_XzYx7w','Nine Lashes','https://lh3.googleusercontent.com/x1Tym8etDAElQe7VimovABMgPJyP9PJpfY_-7paTvD4Uq7UAfo-EheopyLZZlRBjfrrt5nRzldUggA=w1080-h'),('UC5Lsr6bVLulAFbSRwCKt3tg','Тони Раут, Talibal','https://lh3.googleusercontent.com/a-/AOh14GizFT2KB5OMpe8VaISv2A3qixiv03C3kr_IYswa8g=w1440-h600-p-l90-rj'),('UC8w5xrdhxbzOWm21eBBYqSA','LSP','https://lh3.googleusercontent.com/I4aCLZu424FLgv3V7S-2IRJmdaB-0MBeB-w7_2DRaba8wEr4_anLfZvHBeOmq0KFj06bR1clBt5N1Tri=w1500'),('UCcMcUoDPCQhtONMyuKJs-dg','Sum 41','https://lh3.googleusercontent.com/13x_XpDtZKAUKw2brz0wjCbcYyTgw0VpSP8wLgfYALwde9pTPW4s_bss_ODTvMgK1DNLrJ2NBejhI4w=w1080-'),('UCcucrfDVx-WyEtb8mQIKj0A','Axwell / Ingrosso','https://lh3.googleusercontent.com/Rn5lWjT787hyyIkYu_yiyY0gB9J7jDEiYgxotfHXuqY7ZKMKKLpKglBg7ZXNilohhX2qpEcrs9lHQniy=w2160'),('UCDssrdgCuRtfpjfMc_hsYRw','Static-X','https://lh3.googleusercontent.com/pFq_Rv7pYrZbrnFhI5NIexZaL6jWfUIUa-4bdQYOovSE5Kk9FCcd1GauukMY4J8PkZJj_q30zc48DA=w1080-h'),('UCE9L8h3LgZRSudpWLahhGuQ','My Darkest Days','https://lh3.googleusercontent.com/a-/AOh14GjTIncsSGe1aAgsdsu4eTK4uN8nPZjIVTmfrvA0=w764-h318-p-l90-rj'),('UCedvOgsKFzcK3hA5taf3KoQ','Eminem','https://lh3.googleusercontent.com/a-/AOh14Gj3AiAC5WexHxs2-x1v-2vj_bpWg5_KTDrR51Oz_Q=w2314-h964-p-l90-rj'),('UCFaZ4xC5bMx6tlazsuA4wdg','Cult to Follow','https://lh3.googleusercontent.com/2I0cBZx3oFPkedhknPXTrik2rfcKkdon_HPv2w7wppkFGEie1euaqf46ydRhBHS8uQnMmtu_dwLJyeey=w1400'),('UCJif7WIflX_1Jg5RypJjqnw','From Ashes to New','https://lh3.googleusercontent.com/j3Eo7CIrdo4OV43HYKPQt3hQd9hsJAWAd2SGQGspBj2pI-0ow1d_x0XbgaFAbdGnbhisnMnS-RXuBbVe=w2076'),('UCUHYrf3BF5yI9QdRw09__BA','Skillet','https://lh3.googleusercontent.com/_fKp5gTVgs4mWQ7vqvg2wbWyeNNHES0J9TdK2p102IE_WwZ5SIY6MCyQR7o7HqmpVwvlX5fkmrC_WC8M=w2880'),('UCzYd1EYoMbG8tFWQ69Odi4Q','STARSET','https://lh3.googleusercontent.com/QNgDPoid6kFfi9PlKMQ0rQY4K2gFmAieR06nwla9XOdMi6EnLGhCkI073MlFXXQSckxmeW9A4Lnlq64=w2880-'),('UC_o4Fz0kJt1pY-45KT10BEA','Thousand Foot Krutch','https://lh3.googleusercontent.com/slpGliqACH0XiXozZPF0IvEBPpF8HeJAoKvC1o_EJoA_FBlhJxUfkSmYOsXKnYE_xmwYVavg6jofLpE=w2880-'),('UC_tC_1RE-4nxKXoyjPjiRbQ','Talibal','https://lh3.googleusercontent.com/WBlyVPeQi7u21_e8sEpUDQgryYZLFYU6V60_hrn9KJuREwDLOiDpxKwXQ01dmcKk3kXhMzx0er6XmpdM=w1400');
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
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
