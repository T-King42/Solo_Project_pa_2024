-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: yugibase_schema
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `card_name` varchar(255) DEFAULT NULL,
  `atk` int DEFAULT NULL,
  `def` int DEFAULT NULL,
  `effect` varchar(2000) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,'Blue-Eyes White Dragon',3000,2500,'This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.','card_images/Blue-Eyes_White_Dragon.jpg','2024-03-17 01:36:22','2024-03-18 04:03:55'),(2,'Dark Magician',2500,2100,'\'\'The ultimate wizard in terms of attack and defense.\'\'','card_images/Dark_Magician.jpg','2024-03-17 01:37:14','2024-03-18 04:03:55'),(3,'Exodia the Forbidden One',1000,1000,'If you have \"Right Leg of the Forbidden One\", \"Left Leg of the Forbidden One\", \"Right Arm of the Forbidden One\" and \"Left Arm of the Forbidden One\" in addition to this card in your hand, you win the Duel.','card_images/Exodia_the_Forbidden_One.jpg','2024-03-17 02:00:26','2024-03-18 04:03:55'),(4,'Dark Hole',NULL,NULL,'Destroy all monsters on the field.','card_images/Dark_Hole.jpg','2024-03-17 22:54:45','2024-03-18 04:03:55'),(5,'Decode Talker',2300,NULL,'2+ Effect Monsters\r\nGains 500 ATK for each monster it points to. When your opponent activates a card or effect that targets a card(s) you control (Quick Effect): You can Tribute 1 monster this card points to; negate the activation, and if you do, destroy that card.','card_images/Decode_Talker.jpg','2024-03-17 22:55:32','2024-03-18 04:03:55'),(6,'Raigeki',NULL,NULL,'Destroy all monsters your opponent controls.','card_images/Raigeki.jpg','2024-03-17 23:28:46','2024-03-18 04:03:55'),(7,'Trap Hole',NULL,NULL,'When your opponent Normal or Flip Summons 1 monster with 1000 or more ATK: Target that monster; destroy that target.','card_images/Trap_Hole.jpg','2024-03-18 04:28:07','2024-03-18 04:39:42'),(8,'Qliphort Scout',1000,2800,'[ Pendulum Effect ] \nYou cannot Special Summon monsters, except \"Qli\" monsters. This effect cannot be negated. Once per turn: You can pay 800 LP; add 1 \"Qli\" card from your Deck to your hand, except \"Qliphort Scout\".\n[ Monster Effect ] \n\'\'Booting in Replica Mode...\r\nAn error has occurred while executing C:\\sophia\\zefra.exe\r\nUnknown publisher.\r\nAllow C:\\tierra\\qliphort.exe ? ...[Y]\r\nBooting in Autonomy Mode...\'\'','card_images/Qliphort_Scout.jpg','2024-03-18 04:40:18','2024-03-18 04:40:18'),(9,'Ultimate Conductor Tyranno',3500,3200,'Cannot be Normal Summoned/Set. Must first be Special Summoned (from your hand) by banishing 2 Dinosaur-Type monsters from your Graveyard. Once per turn, during either player\'s Main Phase: You can destroy 1 monster in your hand or field, and if you do, change all face-up monsters your opponent controls to face-down Defense Position. This card can attack all monsters your opponent controls, once each. At the start of the Damage Step, if this card attacks a Defense Position monster: You can inflict 1000 damage to your opponent, and if you do, send that Defense Position monster to the Graveyard.','card_images/Ultimate_Conductor_Tyranno.jpg','2024-03-18 17:20:50','2024-03-18 17:20:50'),(10,'Dark Magician Girl',2000,1700,'Gains 300 ATK for every \"Dark Magician\" or \"Magician of Black Chaos\" in the GY.','card_images/Dark_Magician_Girl.jpg','2024-03-18 18:53:39','2024-03-18 18:53:39'),(11,'Kuriboh',300,200,'During damage calculation, if your opponent\'s monster attacks (Quick Effect): You can discard this card; you take no battle damage from that battle.','card_images/Kuriboh.jpg','2024-03-18 20:03:51','2024-03-18 20:03:51');
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-18 21:07:43
