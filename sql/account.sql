create database mqtt;
use mqtt;


SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account_backup
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
                                   `user_name` varchar(255) NOT NULL,
                                   `email` varchar(255) NOT NULL,
                                   `password` varchar(512) NOT NULL,
                                   `date` date NOT NULL,
                                   PRIMARY KEY (`user_name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;
