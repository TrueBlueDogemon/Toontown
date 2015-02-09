CREATE TABLE `Accounts` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rawPassword` tinyint(4) NOT NULL,
  `email` varchar(255) NOT NULL,
  `accountid` int(11) NOT NULL,
  `accesslevel` int(11) NOT NULL,
  `canPlay` int(10) DEFAULT '1',
  `banReason` varchar(255) NOT NULL,
  `banRelease` varchar(30) NOT NULL,
  `isMod` tinyint(10) NOT NULL,
  `status` text NOT NULL,
  `name` varchar(25) NOT NULL,
  `newsname` varchar(25) NOT NULL,
  `registrationdate` varchar(40) NOT NULL,
  `allowemails` tinyint(10) NOT NULL DEFAULT '1',
  `registrationip` varchar(50) NOT NULL,
  `lastloggedinip` varchar(50) NOT NULL,
  `rpwkey` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `NameApprovals` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `avid` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `status` varchar(10) NOT NULL,
  `reviewedby` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;
