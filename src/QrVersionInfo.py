from dataclasses import dataclass
from src.Enums.ErrorCorrection import ErrorCorrectionMode


@dataclass(frozen=True, slots=True)
class VersionInfo:
    data_codewords: int
    ec_codewords_per_block: int
    blocks_group1: int
    data_codewords_group1: int
    blocks_group2: int
    data_codewords_group2: int


QR_VERSION_INFO = {
    1: {
        ErrorCorrectionMode.LOW: VersionInfo(19, 7, 1, 19, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(16, 10, 1, 16, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(13, 13, 1, 13, 0, 0),
        ErrorCorrectionMode.HIGH: VersionInfo(9, 17, 1, 9, 0, 0),
    },

    2: {
        ErrorCorrectionMode.LOW: VersionInfo(34, 10, 1, 34, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(28, 16, 1, 28, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(22, 22, 1, 22, 0, 0),
        ErrorCorrectionMode.HIGH: VersionInfo(16, 28, 1, 16, 0, 0),
    },

    3: {
        ErrorCorrectionMode.LOW: VersionInfo(55, 15, 1, 55, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(44, 26, 1, 44, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(34, 18, 2, 17, 0, 0),
        ErrorCorrectionMode.HIGH: VersionInfo(26, 22, 2, 13, 0, 0),
    },

    4: {
        ErrorCorrectionMode.LOW: VersionInfo(80, 20, 1, 80, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(64, 18, 2, 32, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(48, 26, 2, 24, 0, 0),
        ErrorCorrectionMode.HIGH: VersionInfo(36, 16, 4, 9, 0, 0),
    },

    5: {
        ErrorCorrectionMode.LOW: VersionInfo(108, 26, 1, 108, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(86, 24, 2, 43, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(62, 18, 2, 15, 2, 16),
        ErrorCorrectionMode.HIGH: VersionInfo(46, 22, 2, 11, 2, 12),
    },

    6: {
        ErrorCorrectionMode.LOW: VersionInfo(136, 18, 2, 68, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(108, 16, 4, 27, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(76, 24, 4, 19, 0, 0),
        ErrorCorrectionMode.HIGH: VersionInfo(60, 28, 4, 15, 0, 0),
    },

    7: {
        ErrorCorrectionMode.LOW: VersionInfo(156, 20, 2, 78, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(124, 18, 4, 31, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(88, 18, 2, 14, 4, 15),
        ErrorCorrectionMode.HIGH: VersionInfo(66, 26, 4, 13, 1, 14),
    },

    8: {
        ErrorCorrectionMode.LOW: VersionInfo(194, 24, 2, 97, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(154, 22, 2, 38, 2, 39),
        ErrorCorrectionMode.QUARTILE: VersionInfo(110, 22, 4, 18, 2, 19),
        ErrorCorrectionMode.HIGH: VersionInfo(86, 26, 4, 14, 2, 15),
    },

    9: {
        ErrorCorrectionMode.LOW: VersionInfo(232, 30, 2, 116, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(182, 22, 3, 36, 2, 37),
        ErrorCorrectionMode.QUARTILE: VersionInfo(132, 20, 4, 16, 4, 17),
        ErrorCorrectionMode.HIGH: VersionInfo(100, 24, 4, 12, 4, 13),
    },

    10: {
        ErrorCorrectionMode.LOW: VersionInfo(274, 18, 2, 68, 2, 69),
        ErrorCorrectionMode.MEDIUM: VersionInfo(216, 26, 4, 43, 1, 44),
        ErrorCorrectionMode.QUARTILE: VersionInfo(154, 24, 6, 19, 2, 20),
        ErrorCorrectionMode.HIGH: VersionInfo(122, 28, 6, 15, 2, 16),
    },

        11: {
        ErrorCorrectionMode.LOW: VersionInfo(324, 20, 4, 81, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(254, 30, 1, 50, 4, 51),
        ErrorCorrectionMode.QUARTILE: VersionInfo(180, 28, 4, 22, 4, 23),
        ErrorCorrectionMode.HIGH: VersionInfo(140, 24, 3, 12, 8, 13),
    },

    12: {
        ErrorCorrectionMode.LOW: VersionInfo(370, 24, 2, 92, 2, 93),
        ErrorCorrectionMode.MEDIUM: VersionInfo(290, 22, 6, 36, 2, 37),
        ErrorCorrectionMode.QUARTILE: VersionInfo(206, 26, 4, 20, 6, 21),
        ErrorCorrectionMode.HIGH: VersionInfo(158, 28, 7, 14, 4, 15),
    },

    13: {
        ErrorCorrectionMode.LOW: VersionInfo(428, 26, 4, 107, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(334, 22, 8, 37, 1, 38),
        ErrorCorrectionMode.QUARTILE: VersionInfo(244, 24, 8, 20, 4, 21),
        ErrorCorrectionMode.HIGH: VersionInfo(180, 22, 12, 11, 4, 12),
    },

    14: {
        ErrorCorrectionMode.LOW: VersionInfo(461, 30, 3, 115, 1, 116),
        ErrorCorrectionMode.MEDIUM: VersionInfo(365, 24, 4, 40, 5, 41),
        ErrorCorrectionMode.QUARTILE: VersionInfo(261, 20, 11, 16, 5, 17),
        ErrorCorrectionMode.HIGH: VersionInfo(197, 24, 11, 12, 5, 13),
    },

    15: {
        ErrorCorrectionMode.LOW: VersionInfo(523, 22, 5, 87, 1, 88),
        ErrorCorrectionMode.MEDIUM: VersionInfo(415, 24, 5, 41, 5, 42),
        ErrorCorrectionMode.QUARTILE: VersionInfo(295, 30, 5, 24, 7, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(223, 24, 11, 12, 7, 13),
    },

    16: {
        ErrorCorrectionMode.LOW: VersionInfo(589, 24, 5, 98, 1, 99),
        ErrorCorrectionMode.MEDIUM: VersionInfo(453, 28, 7, 45, 3, 46),
        ErrorCorrectionMode.QUARTILE: VersionInfo(325, 24, 15, 19, 2, 20),
        ErrorCorrectionMode.HIGH: VersionInfo(253, 30, 3, 15, 13, 16),
    },

    17: {
        ErrorCorrectionMode.LOW: VersionInfo(647, 28, 1, 107, 5, 108),
        ErrorCorrectionMode.MEDIUM: VersionInfo(507, 28, 10, 46, 1, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(367, 28, 1, 22, 15, 23),
        ErrorCorrectionMode.HIGH: VersionInfo(283, 28, 2, 14, 17, 15),
    },

    18: {
        ErrorCorrectionMode.LOW: VersionInfo(721, 30, 5, 120, 1, 121),
        ErrorCorrectionMode.MEDIUM: VersionInfo(563, 26, 9, 43, 4, 44),
        ErrorCorrectionMode.QUARTILE: VersionInfo(397, 28, 17, 22, 1, 23),
        ErrorCorrectionMode.HIGH: VersionInfo(313, 28, 2, 14, 19, 15),
    },

    19: {
        ErrorCorrectionMode.LOW: VersionInfo(795, 28, 3, 113, 4, 114),
        ErrorCorrectionMode.MEDIUM: VersionInfo(627, 26, 3, 44, 11, 45),
        ErrorCorrectionMode.QUARTILE: VersionInfo(445, 26, 17, 21, 4, 22),
        ErrorCorrectionMode.HIGH: VersionInfo(341, 26, 9, 13, 16, 14),
    },

    20: {
        ErrorCorrectionMode.LOW: VersionInfo(861, 28, 3, 107, 5, 108),
        ErrorCorrectionMode.MEDIUM: VersionInfo(669, 26, 3, 41, 13, 42),
        ErrorCorrectionMode.QUARTILE: VersionInfo(485, 30, 15, 24, 5, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(385, 28, 15, 15, 10, 16),
    },

    21: {
        ErrorCorrectionMode.LOW: VersionInfo(932, 28, 4, 116, 4, 117),
        ErrorCorrectionMode.MEDIUM: VersionInfo(714, 26, 17, 42, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(512, 28, 17, 22, 6, 23),
        ErrorCorrectionMode.HIGH: VersionInfo(406, 30, 19, 16, 6, 17),
    },

    22: {
        ErrorCorrectionMode.LOW: VersionInfo(1006, 28, 2, 111, 7, 112),
        ErrorCorrectionMode.MEDIUM: VersionInfo(782, 28, 17, 46, 0, 0),
        ErrorCorrectionMode.QUARTILE: VersionInfo(568, 30, 7, 24, 16, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(442, 24, 34, 13, 0, 0),
    },

    23: {
        ErrorCorrectionMode.LOW: VersionInfo(1094, 30, 4, 121, 5, 122),
        ErrorCorrectionMode.MEDIUM: VersionInfo(860, 28, 4, 47, 14, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(614, 30, 11, 24, 14, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(464, 30, 16, 15, 14, 16),
    },

    24: {
        ErrorCorrectionMode.LOW: VersionInfo(1174, 30, 6, 117, 4, 118),
        ErrorCorrectionMode.MEDIUM: VersionInfo(914, 28, 6, 45, 14, 46),
        ErrorCorrectionMode.QUARTILE: VersionInfo(664, 30, 11, 24, 16, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(514, 30, 30, 16, 2, 17),
    },

    25: {
        ErrorCorrectionMode.LOW: VersionInfo(1276, 26, 8, 106, 4, 107),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1000, 28, 8, 47, 13, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(718, 30, 7, 24, 22, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(538, 30, 22, 15, 13, 16),
    },

    26: {
        ErrorCorrectionMode.LOW: VersionInfo(1370, 28, 10, 114, 2, 115),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1062, 28, 19, 46, 4, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(754, 28, 28, 22, 6, 23),
        ErrorCorrectionMode.HIGH: VersionInfo(596, 30, 33, 16, 4, 17),
    },

    27: {
        ErrorCorrectionMode.LOW: VersionInfo(1468, 30, 8, 122, 4, 123),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1128, 28, 22, 45, 3, 46),
        ErrorCorrectionMode.QUARTILE: VersionInfo(808, 30, 8, 23, 26, 24),
        ErrorCorrectionMode.HIGH: VersionInfo(628, 30, 12, 15, 28, 16),
    },

    28: {
        ErrorCorrectionMode.LOW: VersionInfo(1531, 30, 3, 117, 10, 118),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1193, 28, 3, 45, 23, 46),
        ErrorCorrectionMode.QUARTILE: VersionInfo(871, 30, 4, 24, 31, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(661, 30, 11, 15, 31, 16),
    },

    29: {
        ErrorCorrectionMode.LOW: VersionInfo(1631, 30, 7, 116, 7, 117),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1267, 28, 21, 45, 7, 46),
        ErrorCorrectionMode.QUARTILE: VersionInfo(911, 30, 1, 23, 37, 24),
        ErrorCorrectionMode.HIGH: VersionInfo(701, 30, 19, 15, 26, 16),
    },

    30: {
        ErrorCorrectionMode.LOW: VersionInfo(1735, 30, 5, 115, 10, 116),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1373, 28, 19, 47, 10, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(985, 30, 15, 24, 25, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(745, 30, 23, 15, 25, 16),
    },

    31: {
        ErrorCorrectionMode.LOW: VersionInfo(1843, 30, 13, 115, 3, 116),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1455, 28, 2, 46, 29, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1033, 30, 42, 24, 1, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(793, 30, 23, 15, 28, 16),
    },

    32: {
        ErrorCorrectionMode.LOW: VersionInfo(1955, 30, 17, 115, 0, 0),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1541, 28, 10, 46, 23, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1115, 30, 10, 24, 35, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(845, 30, 19, 15, 35, 16),
    },

    33: {
        ErrorCorrectionMode.LOW: VersionInfo(2071, 30, 17, 115, 1, 116),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1631, 28, 14, 46, 21, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1171, 30, 29, 24, 19, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(901, 30, 11, 15, 46, 16),
    },

    34: {
        ErrorCorrectionMode.LOW: VersionInfo(2191, 30, 13, 115, 6, 116),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1725, 28, 14, 46, 23, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1231, 30, 44, 24, 7, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(961, 30, 59, 16, 1, 17),
    },

    35: {
        ErrorCorrectionMode.LOW: VersionInfo(2306, 30, 12, 121, 7, 122),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1812, 28, 12, 47, 26, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1286, 30, 39, 24, 14, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(986, 30, 22, 15, 41, 16),
    },

    36: {
        ErrorCorrectionMode.LOW: VersionInfo(2434, 30, 6, 121, 14, 122),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1914, 28, 6, 47, 34, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1354, 30, 46, 24, 10, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(1054, 30, 2, 15, 64, 16),
    },

    37: {
        ErrorCorrectionMode.LOW: VersionInfo(2566, 30, 17, 122, 4, 123),
        ErrorCorrectionMode.MEDIUM: VersionInfo(1992, 28, 29, 46, 14, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1426, 30, 49, 24, 10, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(1096, 30, 24, 15, 46, 16),
    },

    38: {
        ErrorCorrectionMode.LOW: VersionInfo(2702, 30, 4, 122, 18, 123),
        ErrorCorrectionMode.MEDIUM: VersionInfo(2102, 28, 13, 46, 32, 47),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1502, 30, 48, 24, 14, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(1142, 30, 42, 15, 32, 16),
    },

    39: {
        ErrorCorrectionMode.LOW: VersionInfo(2812, 30, 20, 117, 4, 118),
        ErrorCorrectionMode.MEDIUM: VersionInfo(2216, 28, 40, 47, 7, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1582, 30, 43, 24, 22, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(1222, 30, 10, 15, 67, 16),
    },

    40: {
        ErrorCorrectionMode.LOW: VersionInfo(2956, 30, 19, 118, 6, 119),
        ErrorCorrectionMode.MEDIUM: VersionInfo(2334, 28, 18, 47, 31, 48),
        ErrorCorrectionMode.QUARTILE: VersionInfo(1666, 30, 34, 24, 34, 25),
        ErrorCorrectionMode.HIGH: VersionInfo(1276, 30, 20, 15, 61, 16),
    },
}