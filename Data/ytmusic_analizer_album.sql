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
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `id_album` varchar(40) NOT NULL,
  `album_title` varchar(45) NOT NULL,
  `year` int DEFAULT NULL,
  `disks_amount` int DEFAULT '1',
  `track_amount` int DEFAULT NULL,
  `alb_genre_id` int DEFAULT NULL,
  `cover_art` varchar(200) DEFAULT NULL,
  `type_id` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_album`),
  KEY `type_id_idx` (`type_id`),
  KEY `genre_id_idx` (`alb_genre_id`),
  CONSTRAINT `alb_genre_id` FOREIGN KEY (`alb_genre_id`) REFERENCES `genres` (`id_genre`),
  CONSTRAINT `type_id` FOREIGN KEY (`type_id`) REFERENCES `album_type` (`id_album_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES ('MPREb_bLo81dYH6Na','New Empire, Vol. 2',2020,1,12,NULL,'https://lh3.googleusercontent.com/YCs74hyPvhXFquE8ZhrOpWg3zyxUdsHSfMHkZbCezNtUlQG9oaeYc-F1IburaKkGal5jFvBARVV6RD3GDw=w544-h544-l90-rj',1),('MPREb_c6QjKoWibkc','Chuck',2004,1,14,NULL,'https://lh3.googleusercontent.com/ZhHFDrMl4GjwHA4lCN3DwRqlc959T8e5WLPMI0dmiFtZdF2jaXbyiVQ_t9hj-Oa6kcPiuG92EFr8cIUl=w544-h544-l90-rj',1),('MPREb_cGg2ooQRuwQ','Leave It All Behind',2011,1,1,NULL,'https://lh3.googleusercontent.com/iRuje6yrGP7aJU9ziHlSmUFyYlceeBwirZyCXeHETN-F3SA9dSRT4InsG30nd8Ogy_6Yosi5IZgo_FI=w544-h544-l90-rj',0),('MPREb_g6GwtcGLCJk','Shadow Zone (U.S. Version)',2003,1,13,NULL,'https://lh3.googleusercontent.com/A7cpkCYPiiuvefrVz8QZIQp7M1SulZaEzLRIU661YKECHGovOYPjzdDIRECTmk_8y9d2-ouK2s22ka-p=w544-h544-s-l90-rj',1),('MPREb_gbtBjQn8JXf','Transmissions',2014,1,13,NULL,'https://lh3.googleusercontent.com/2E0keG7IMF9WN934gzhBCqqRhax_rAZlBf_buN81PD8lKopjdRCms-h0TRgv4KDd0ewQCkowXyp-a8c=w544-h544-l90-rj',1),('MPREb_IWUeCDFDP4I','YoP',2014,1,9,NULL,'https://lh3.googleusercontent.com/jAK-C4ySbH6KmUrODOHu8ApmXFMN84XCqb8rT3kwjgBSEN1rSfTqFQ5TiYrFO_0IoAQoDl04XJkb-doF=w544-h544-l90-rj',1),('MPREb_keJO6XJy5nO','Does This Look Infected?',2002,1,12,NULL,'https://lh3.googleusercontent.com/YKO8v0Sy3H6qKS0u8Vb_cajD5c9RErhNnOsWh4Z018dlTont_YVTlJu1WZrCyM7a9yV7IjhuLNY57pQ0Og=w544-h544-s-l90-rj',1),('MPREb_KRpzc1wcZNm','More Than You Know',2017,1,4,NULL,'https://lh3.googleusercontent.com/mbq-tS0t3I9rS1LrTrQ33nzum9ayxP_KpyH3J24qpKwuYqVe66RtwKA_yfrqku7qkkbmPvCe1VHMvwat=w544-h544-l90-rj',2),('MPREb_OO063RUCmxw','World We View',2012,1,11,NULL,'https://lh3.googleusercontent.com/pda88op5qxjeFgaiRxm8NAMXFbKHSBj8OlSHvyquk3PeixnqEsOKNXCMQ0NSL0jgoaNCs0RDDDHY_oFN=w544-h544-l90-rj',1),('MPREb_sW9YUpBLOGw','Bad Pazific',2017,1,11,NULL,'https://lh3.googleusercontent.com/unge3TGxXRgOiMSNsXCvkOjOpTVSaFdZqXm2mNqA9v5KHx_2Ip9gWdsz8McjEmW8REfF2cYCEqeaqBnr=w544-h544-l90-rj',1),('MPREb_U6SwkJdwCvX','Unleashed',2016,1,12,NULL,'https://lh3.googleusercontent.com/5k7bYwUzRgZM9blivKiKhim7VmDs3n87CcziXgzHCRIXXkDCJMQRgwX-_Teg1OH46qNfjcQoZqQw1b5s=w544-h544-l90-rj',1),('MPREb_UUFKiZYr3uO','Recovery',2010,1,17,NULL,'https://lh3.googleusercontent.com/IUuZFSUqFLMQlejTtsnLM_cB16A0T1g-savL7DYbWz5NFh2-DOw5-v9_PREJt9keX48NSan-8yUQCPM=w544-h544-l90-rj',1),('MPREb_v7Ub5XgdI8k','Panic',2020,1,11,NULL,'https://lh3.googleusercontent.com/6eVozMd3Ebqj4UKQfBT99LUzJafeDSgoP5g0VL8vZGc-q7-7VCJpD5WEOADvdt0lQvfdySxJ1g0cG0T3=w544-h544-l90-rj',1),('MPREb_vn8w6DKmlHQ','My Darkest Days',2010,1,11,NULL,'https://lh3.googleusercontent.com/gQ3tQgpZrL3jbu7Cjkz4wfa23-LLcgXwOZ-fQi1ZC8NQgoT80lwafaLr88wOlb9DGdNSA_5mLA0u3gSccA=w544-h544-l90-rj',1),('MPREb_WqATcp72Irc','The End Is Where We Begin',2012,1,15,NULL,'https://lh3.googleusercontent.com/6M3wYtyNcB9ckYYGXSmcD41Fi2lHGR8hczuw34zXhEOORXfpb832-i_surd2dGJInWkLqxS1iv7XDFZH=w544-h544-l90-rj',1),('MPREb_WuipnfO4lQw','Transmissions (Deluxe Version)',2014,1,20,NULL,'https://lh3.googleusercontent.com/SFEjDOf3uo8Aw43QFj0RN6TpBvtR2_L4NHJ1bRgBYmslC9O3h6uwuUgjlvpmkAsmwOeZ8MFlBs90Op_U=w544-h544-l90-rj',1),('MPREb_zioMNYHmNn9','Tragic City',2017,1,13,NULL,'https://lh3.googleusercontent.com/jGzUjV9irr8Lyi_PoU7vWaMV3PJtxZGmhRpf1_KQSYM2TaANhItCyawvYIOlY-BiIbcX5aWbRKwyIQ=w544-h544-l90-rj',1),('MPREb_ZvM9V7DBuyy','Vessels',2017,1,15,NULL,'https://lh3.googleusercontent.com/eKdkM8SO3aX-u9lKKim-1sg4Lq_pks-KWJCKhiJnxJEs1TWKiZPnokrFPJ0RHV90ot8anBMKwQCSyU7I=w544-h544-l90-rj',1);
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
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
