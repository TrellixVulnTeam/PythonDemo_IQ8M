

CREATE DATABASE IF NOT EXISTS books default charset utf8;
USE books;

DROP TABLE IF EXISTS `t_book`;
CREATE TABLE `t_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL COMMENT '图书名称',
  `pub_date` date NOT NULL COMMENT '发布日期',
  `read` int(11) NOT NULL DEFAULT '0' COMMENT '阅读量',
  `comment` int(11) NOT NULL DEFAULT '0' COMMENT '评论量',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='图书表';

INSERT INTO `t_book` VALUES ('1', '射雕英雄传', '1980-05-01', '12', '34', '0');
INSERT INTO `t_book` VALUES ('2', '天龙八部', '1986-07-24', '36', '40', '0');
INSERT INTO `t_book` VALUES ('3', '笑傲江湖', '1995-12-24', '20', '80', '0');

DROP TABLE IF EXISTS `t_hero`;
CREATE TABLE `t_hero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '姓名',
  `gender` smallint(6) NOT NULL COMMENT '性别',
  `description` varchar(200) DEFAULT NULL COMMENT '描述',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `book_id` int(11) NOT NULL COMMENT '所属图书ID',
  PRIMARY KEY (`id`),
  KEY `t_hero_book_id` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='英雄人物表';

INSERT INTO `t_hero` VALUES ('1', '郭靖', '1', '降龙十八掌', '0', '1');
INSERT INTO `t_hero` VALUES ('2', '黄蓉', '0', '打狗棍法', '0', '1');
INSERT INTO `t_hero` VALUES ('3', '乔峰', '1', '降龙十八掌', '0', '2');
INSERT INTO `t_hero` VALUES ('4', '令狐冲', '1', '独孤九剑', '0', '3');
INSERT INTO `t_hero` VALUES ('5', '任盈盈', '0', '弹琴', '0', '3');

