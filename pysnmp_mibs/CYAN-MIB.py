# SNMP MIB module (CYAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cyan/CYAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:18 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cyanAlarmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20)
)
if mibBuilder.loadTexts:
    cyanAlarmMibModule.setRevisions(
        ("2014-12-07 06:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CyanProbablecauseTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              11,
              31,
              32,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              201,
              202,
              203,
              204,
              205,
              301,
              302,
              401,
              402)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("unequipped", 1),
          ("eqptRestart", 2),
          ("eqptFail", 3),
          ("eqptDgrade", 4),
          ("eqptMismtch", 5),
          ("eqptUnexpected", 6),
          ("eqptWarning", 7),
          ("notConfig", 8),
          ("autoUpgrade", 11),
          ("batFail", 31),
          ("batDgrade", 32),
          ("tpLol", 49),
          ("preAmp", 50),
          ("tpLos", 51),
          ("tpLoc", 52),
          ("tpLof", 53),
          ("tpAis", 54),
          ("tpLom", 55),
          ("tpSf", 56),
          ("tpBdi", 57),
          ("tpFdi", 58),
          ("tpPmi", 59),
          ("tpSd", 60),
          ("tpRdi", 61),
          ("tpTim", 62),
          ("tpIae", 63),
          ("tpBiae", 64),
          ("tpOci", 65),
          ("tpLck", 66),
          ("tpLoflom", 67),
          ("tpSsf", 68),
          ("tpOorangeAlm", 69),
          ("tpOorangeWrn", 70),
          ("tpFaclpbk", 71),
          ("tpHighLoss", 72),
          ("tpLowLoss", 73),
          ("tpFiber", 74),
          ("tpPlm", 75),
          ("tpLtc", 76),
          ("tpMsim", 77),
          ("protFail", 78),
          ("ccm", 79),
          ("tpLfd", 80),
          ("tpLink", 81),
          ("tpGfp", 82),
          ("tpTpt", 83),
          ("gtp", 84),
          ("tpSqm", 85),
          ("tpLoa", 86),
          ("tpLti", 87),
          ("ltm", 88),
          ("aps", 89),
          ("tpLop", 90),
          ("tpUneq", 91),
          ("csf", 92),
          ("exmism", 93),
          ("upm", 94),
          ("protCmd", 95),
          ("farendCmd", 96),
          ("protocolErr", 97),
          ("loopback", 98),
          ("lmm", 99),
          ("dmm", 100),
          ("commFail", 101),
          ("commDgrade", 102),
          ("packetLpbk", 103),
          ("xcspktsloss", 104),
          ("xcspktserr", 105),
          ("srcaddrmis", 106),
          ("arp", 107),
          ("tsa", 108),
          ("erpPort", 109),
          ("tpLoomfi", 110),
          ("syncFail", 201),
          ("syncDgrade", 202),
          ("holdover", 203),
          ("xcsholdover", 204),
          ("syncExcmdActive", 205),
          ("envAlm", 301),
          ("envWrn", 302),
          ("incmpld", 401),
          ("admin", 402))
    )



class CyanAlarmstateTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asCleared", 0),
          ("asSet", 1))
    )



class CyanTypeTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              96,
              97,
              98,
              99,
              100,
              101,
              106,
              107,
              108,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              143,
              144,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              201,
              202,
              204,
              207,
              299,
              300,
              301,
              303,
              304,
              305,
              306,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              442,
              443,
              444,
              445,
              446,
              447,
              448,
              449,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              464,
              465,
              466,
              467,
              468,
              469,
              470,
              471,
              472,
              473,
              474,
              475,
              476,
              477,
              478,
              479,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              487,
              488,
              489,
              490,
              491,
              492,
              493,
              494,
              495,
              496,
              497,
              498,
              499,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              552,
              553,
              554,
              555,
              556,
              557,
              558,
              559,
              560,
              561,
              562,
              563,
              564,
              565,
              566,
              567,
              568,
              569,
              570,
              571,
              572,
              573,
              574,
              575,
              576,
              577,
              578,
              580,
              601,
              602,
              603,
              604,
              605,
              702,
              703,
              704,
              705,
              706,
              707,
              708,
              709,
              710,
              711,
              712,
              713,
              714,
              715,
              716,
              717,
              718,
              719,
              720,
              721,
              722,
              723,
              724,
              725,
              726,
              727,
              728,
              729,
              730,
              731,
              732,
              733,
              734,
              735,
              736,
              737,
              738,
              800,
              801,
              802)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unequipped", 1),
          ("unavailable", 2),
          ("cyanMs", 3),
          ("cyanNetwork", 4),
          ("cyanTopologicalline", 5),
          ("cyanTopologicallink", 6),
          ("cyanZ77", 7),
          ("cyanShelf16slot", 8),
          ("cyanShelf16", 9),
          ("cyanShelf8", 10),
          ("cyanXfpslot", 11),
          ("cyanSfpslot", 12),
          ("cyanAmcslot", 13),
          ("cyanLampcoreeqpt", 14),
          ("cyanLampshelf", 15),
          ("cyanLamp", 16),
          ("cyanShelfslot", 17),
          ("cyanZ33", 18),
          ("cyanLgx3shelf", 19),
          ("cyanOfx4", 20),
          ("cyanPemslot", 21),
          ("cyanBtmslot", 22),
          ("cyanRtmslot", 23),
          ("cyanOpticalfabricslot", 24),
          ("cyanPacketfabricslot", 25),
          ("cyanAwg40", 26),
          ("cyanAwg40shelf", 27),
          ("cyanShelf16v2", 28),
          ("cyanShelf4", 29),
          ("cyanCemslot", 30),
          ("cyanBossslot", 31),
          ("cyanFimslot", 32),
          ("cyanFanslot", 33),
          ("cyanOppanelslot", 34),
          ("cyanZ77fanslot", 35),
          ("cyanZ22", 36),
          ("cyanSfppslot", 37),
          ("cyanCfpslot", 38),
          ("cyanSfppdslot", 39),
          ("cyanAwg96shelf", 40),
          ("cyanAwg96", 41),
          ("cyanOfx8", 42),
          ("cyanLad2g", 96),
          ("cyanZ22fan", 97),
          ("cyanZ77fan", 98),
          ("cyanLad2p", 99),
          ("cyanZ33fan", 100),
          ("cyanBoss", 101),
          ("cyanFan", 106),
          ("cyanOperationpanel", 107),
          ("cyanCem", 108),
          ("cyanMinifan", 111),
          ("cyanLad4", 112),
          ("cyanLad4a", 113),
          ("cyanMse1482", 114),
          ("cyanPsx280", 115),
          ("cyanPsw20", 116),
          ("cyanLad2pLgx", 117),
          ("cyanPme412", 118),
          ("cyanSmx28", 119),
          ("cyanSmx416", 120),
          ("cyanLme4", 121),
          ("cyanLad8", 122),
          ("cyanLad8a", 123),
          ("cyanLad8e", 124),
          ("cyanDtm8g", 126),
          ("cyanLad2gLgx", 127),
          ("cyanDtm8", 128),
          ("cyanSft8", 129),
          ("cyanLac8", 130),
          ("cyanLedpanel", 131),
          ("cyanWss402", 132),
          ("cyanWss404", 133),
          ("cyanPme216", 135),
          ("cyanWmx", 136),
          ("cyanCemi", 137),
          ("cyanLad8i", 138),
          ("cyanLad40", 139),
          ("cyanLad40e", 140),
          ("cyanLme10g10", 141),
          ("cyanXc2800", 143),
          ("cyanTsw10", 144),
          ("cyanBoss2", 146),
          ("cyanDtm4", 147),
          ("cyanLad8x", 148),
          ("cyanSft10g16", 149),
          ("cyanFlx216", 150),
          ("cyanDtm100g", 151),
          ("cyanPsw10", 152),
          ("cyanPsw618", 153),
          ("cyanPsw100g", 154),
          ("cyanMsw10g12", 155),
          ("cyanDtm100g2", 156),
          ("cyanLad96", 157),
          ("cyanPsw10g20", 159),
          ("cyanWssF2", 160),
          ("cyanWssF4", 161),
          ("cyanWssF8", 162),
          ("cyanOla200", 163),
          ("cyanOla201", 164),
          ("cyanOla220", 165),
          ("cyanOla010", 166),
          ("cyanOla221", 167),
          ("cyanXfpxcvr", 201),
          ("cyanCfpxcvr", 202),
          ("cyanSfpxcvr", 204),
          ("cyanAmc", 207),
          ("cyanPem2", 299),
          ("cyanLampbtm", 300),
          ("cyanBtm", 301),
          ("cyanPxc280", 303),
          ("cyanPem", 304),
          ("cyanR1g8sfp", 305),
          ("cyanRtm2x", 306),
          ("cyanRcm", 308),
          ("cyanMidstageptp", 309),
          ("cyanEqptClockTtp", 310),
          ("cyanStm1msTtp", 311),
          ("cyanStm4msTtp", 312),
          ("cyanStm16msTtp", 313),
          ("cyanStm64msTtp", 314),
          ("cyanSaug1Ttp", 315),
          ("cyanAug1Ttp", 316),
          ("cyanAug4Ttp", 317),
          ("cyanAug16Ttp", 318),
          ("cyanAug64Ttp", 319),
          ("cyanSaug4Ttp", 320),
          ("cyanStm1rsTtp", 321),
          ("cyanStm4rsTtp", 322),
          ("cyanStm16rsTtp", 323),
          ("cyanStm64rsTtp", 324),
          ("cyanMuxadddropfiberptp", 325),
          ("cyanOcgptp", 326),
          ("cyanTxextsdTtp", 327),
          ("cyanTxsdTtp", 328),
          ("cyanRxsdTtp", 329),
          ("cyanAdddropcwdmfiberptp", 330),
          ("cyanLinetimingttp", 331),
          ("cyan3rfiberptp", 332),
          ("cyan10gafiberptp", 333),
          ("cyanLadoscTtp", 334),
          ("cyanLadaomsTtp", 335),
          ("cyanLadomsTtp", 336),
          ("cyanAdddropfiberptp", 337),
          ("cyanS1fiberptp", 338),
          ("cyanS4fiberptp", 339),
          ("cyanS16fiberptp", 340),
          ("cyanS16mrfiberptp", 341),
          ("cyanS64fiberptp", 342),
          ("cyanOtu2fiberptp", 343),
          ("cyanLadeotmPtp", 344),
          ("cyanSdhlinkftp", 345),
          ("cyanExtcc2mhzrxttp", 346),
          ("cyanExtcc2mhzptp", 347),
          ("cyanPflinkttp", 348),
          ("cyanLinkftp", 349),
          ("cyan10gemfiberptp", 350),
          ("cyanElectricalctp", 351),
          ("cyanOtmPtp", 352),
          ("cyanFiberptp", 353),
          ("cyanFiberttp", 354),
          ("cyan10gfiberptp", 355),
          ("cyan10gefiberptp", 356),
          ("cyanDerivedtimingreference", 357),
          ("cyanTimingrefftp", 358),
          ("cyanTss", 359),
          ("cyanExttimingreference", 360),
          ("cyanTimingreference", 361),
          ("cyanExttimingptp", 362),
          ("cyanExttimingtxttp", 363),
          ("cyanExttimingrxttp", 364),
          ("cyanOc48Ttp", 365),
          ("cyanStm16Ttp", 366),
          ("cyanOc192Ttp", 367),
          ("cyanStm64Ttp", 368),
          ("ituOtu1gcc0tp", 369),
          ("ituOtu2gcc0tp", 370),
          ("ituOdu1gcc12tp", 371),
          ("ituOdu2gcc12tp", 372),
          ("cyanOdu1nim", 373),
          ("cyanOdu2nim", 374),
          ("cyanOdu1ctp", 375),
          ("cyanOdu2ctp", 376),
          ("cyanOdu1tcmTtp", 377),
          ("cyanOdu2tcmTtp", 378),
          ("cyanClientftp", 379),
          ("cyanOdu1ttp", 380),
          ("cyanOdu2ttp", 381),
          ("cyanOtukctp", 382),
          ("cyanOtu1ttp", 383),
          ("cyanOtu2ttp", 384),
          ("cyanFiberotu2ttp", 385),
          ("cyanOcgttp", 386),
          ("cyanOccnimctp", 387),
          ("cyanOccttp", 388),
          ("cyanOchttp", 389),
          ("cyanOscttp", 390),
          ("cyanOmsTtp", 391),
          ("cyanOtsTtp", 392),
          ("cyanLag", 393),
          ("cyanLampotmPtp", 394),
          ("cyanLadotmPtp", 395),
          ("cyanLadaotmPtp", 396),
          ("cyanLadotsTtp", 397),
          ("cyanTetyTtp", 398),
          ("cyanMauTtp", 399),
          ("cyanMautTtp", 400),
          ("cyanGfpTtp", 401),
          ("cyanEttyTtp", 402),
          ("cyanEty31Ptp", 403),
          ("cyanEty32Ptp", 404),
          ("cyanGigeptp", 405),
          ("cyanEthernetttp", 406),
          ("cyanEtyTtp", 407),
          ("cyanDcnptp", 408),
          ("pbbEspTesi", 409),
          ("pbbFlowpointpool", 410),
          ("cyanEthflowpointpool", 411),
          ("cyanEthuni", 412),
          ("cyanEthnni", 413),
          ("cyanOccctp", 414),
          ("cyanEthlagfpp", 415),
          ("cyanGfecotu2ttp", 416),
          ("cyanTety10gTtp", 417),
          ("cyanEtty10gTtp", 418),
          ("cyanLadeotsTtp", 419),
          ("cyanLadeomsTtp", 420),
          ("cyanEthflowpoint", 421),
          ("pbbFlowpoint", 422),
          ("cyanEosApi", 423),
          ("cyanOtu2ettp", 424),
          ("dot1agmip", 425),
          ("cyanEthlagflowpoint", 426),
          ("cyanOdu2ettp", 427),
          ("cyanUfecotu2ttp", 428),
          ("cyan10geofiberptp", 429),
          ("cyanWmxotmPtp", 430),
          ("dot3ahmep", 431),
          ("cyanEoamApi", 432),
          ("cyanEthflowdomain", 433),
          ("cyanEthbridge", 434),
          ("dot1agmd", 435),
          ("dot1agma", 436),
          ("dot1agmep", 437),
          ("cyanFtp", 438),
          ("cyanVcg", 439),
          ("pbbGtp", 440),
          ("cyanEthbwprofile", 441),
          ("cyanEthcosprofile", 442),
          ("cyanEthqueueprofile", 443),
          ("cyanUserethqueueprofile", 444),
          ("cyanUserethbwprofile", 445),
          ("cyanEthlinkoamprofile", 446),
          ("cyanUserethlinkoamprofile", 447),
          ("cyanEthkbwprofile", 448),
          ("cyanUserethkbwprofile", 449),
          ("cyanSdhsonetApi", 450),
          ("cyanXgewanTtp", 451),
          ("cyanAdddropwwdmfiberptp", 452),
          ("cyanMultifibertp", 453),
          ("cyanOcgettp", 454),
          ("cyanSethTtp", 455),
          ("cyanLadocgptp", 456),
          ("cyanmd", 457),
          ("cyanEty32bPtp", 458),
          ("cyanGigeptpnopmstats", 459),
          ("cyanEthernetttpwpmstats", 460),
          ("cyanGigeptpnopmstatsroute", 461),
          ("cyan10gaofiberptp", 462),
          ("cyanOdu0ttp", 463),
          ("cyanOduflexttp", 464),
          ("cyanOdu2muxttp", 465),
          ("cyanOdu1muxttp", 466),
          ("cyanErppGtp", 467),
          ("erpFlowpointpool", 468),
          ("erpFlowpoint", 469),
          ("cyanSethTxttp", 470),
          ("cyanLad40eotmPtp", 471),
          ("cyan3r10gmrfiberptp", 472),
          ("cyanLad8xotmPtp", 473),
          ("cyan10geopfiberptp", 474),
          ("cyanNetty10gTtp", 475),
          ("cyanErpv2Profile", 476),
          ("cyanUsererpv2Profile", 477),
          ("cyanPathpg", 478),
          ("cyanEthoamprofile", 479),
          ("cyanUserethoamprofile", 480),
          ("eprotectiongroupT", 481),
          ("cyanPg", 482),
          ("cyanOpticalpg", 483),
          ("cyanMsprPg", 484),
          ("cyanTesiexpressApi", 485),
          ("cyanErp", 486),
          ("cyanS0Ctp", 487),
          ("cyanS1Ctp", 488),
          ("cyanS4Ctp", 489),
          ("cyanS16Ctp", 490),
          ("cyanS0Ttp", 491),
          ("cyanS1Ttp", 492),
          ("cyanS4Ttp", 493),
          ("cyanS16Ttp", 494),
          ("cyanS64Ttp", 495),
          ("cyanTimingrefprofile", 496),
          ("cyanTimingrefprofileline", 497),
          ("cyanErpProfile", 498),
          ("cyanUsererpProfile", 499),
          ("cyanEthscheduleprofile", 500),
          ("cimOspfservice", 501),
          ("cimIpprotocolendpoint", 502),
          ("cimIpinterface", 503),
          ("cimOspfprotocolendpoint", 504),
          ("cimOspfinterface", 505),
          ("cimOspfarea", 506),
          ("cyanOspflsdb", 507),
          ("cyanOspfneighbor", 508),
          ("cimDcnipTtp", 509),
          ("cimDcnospfTtp", 510),
          ("cyanUserethscheduleprofile", 511),
          ("cyanAfecotu2ttp", 512),
          ("cyanMrflxptp", 513),
          ("cyan100gemfiberptp", 514),
          ("cyanTety100gTtp", 515),
          ("cyanOtu4ttp", 516),
          ("cyanGfecotu4ttp", 517),
          ("cyanOdu4ttp", 518),
          ("cyanOtm04Ptp", 519),
          ("cyanOccrctp", 520),
          ("cyanSection155mTtp", 521),
          ("cyanSection622mTtp", 522),
          ("cyanSection2488mTtp", 523),
          ("cyanOcgwssptp", 524),
          ("cyanEtyLbTtp", 525),
          ("cyan10gepfiberptp", 526),
          ("cyanEtyFpgaTtp", 527),
          ("cyanElectricalgtp", 528),
          ("cyanElectricalFlowpointpool", 529),
          ("cyanElectricalFlowpoint", 530),
          ("cyanEthflowdomainfrmnt", 531),
          ("cyanIngressoffp", 532),
          ("cyanEthflowdomainintfrmnt", 533),
          ("cyanOcgwssfptp", 534),
          ("cyanSfecotu2ttp", 535),
          ("cyanElectricalPbbflowpoint", 536),
          ("cyanElectricalErpflowpoint", 537),
          ("cyanElectricalLagflowpoint", 538),
          ("cyanElectricalUniflowpoint", 539),
          ("cyanOdukCtp", 540),
          ("cyanSbconEsconTtp", 541),
          ("cyanFc100FiconTtp", 542),
          ("cyanFc200FiconxTtp", 543),
          ("cyanFc400Ttp", 544),
          ("cyanFc800Ttp", 545),
          ("cyanFc1200Ttp", 546),
          ("cyan10ggfiberptp", 547),
          ("cyanOtu4fiberptp", 548),
          ("cyanRodu2ttp", 549),
          ("cyanLogicalinterface", 550),
          ("cyanMplstpNode", 551),
          ("cyanMplstpInterface", 552),
          ("cyanMplstpTunnel", 553),
          ("cyanMplstpLsp", 554),
          ("cyanPwFlowpoint", 555),
          ("cyanPwFlowpointpool", 556),
          ("cyanPwFlowdomain", 557),
          ("cyanMplstpMd", 558),
          ("cyanMplstpMa", 559),
          ("cyanMplstpMep", 560),
          ("cyanMplstpMip", 561),
          ("cyanMplstpLabelrange", 562),
          ("cyanMplstpOamApi", 563),
          ("cyanElectricalOfflowpoint", 564),
          ("cyanEtty100gTtp", 565),
          ("cyanWssfotmPtp", 566),
          ("cyanMultifiber7tp", 567),
          ("cyanMplsexp2cospidprofile", 568),
          ("cyanUsermplsexp2cospidprofile", 569),
          ("cyanInternalOdu2ttp", 570),
          ("cyanInternalOtu2ttp", 571),
          ("cyanOlaotmPtp", 572),
          ("cyanOlaocmotmPtp", 573),
          ("cyanMplstpLspFrgmnt", 574),
          ("cyanMplstpMepFrgmnt", 575),
          ("cyanMsaotu4ttp", 576),
          ("cyanCfpnetworklanePtp", 577),
          ("cyanNetworklaneTtp", 578),
          ("cyanWssfxXconApi", 580),
          ("cyanCrossconnect", 601),
          ("cyanSubnetworkconnection", 602),
          ("cyanSta", 603),
          ("cyanPcapfile", 604),
          ("cyanSvcApi", 605),
          ("cyanMiniroot", 702),
          ("asapT", 703),
          ("tcaparameterprofileT", 704),
          ("pmpT", 705),
          ("cyanOpticaltcaparameterprofile", 706),
          ("usertcaparameterprofileT", 707),
          ("cyanUseropticaltcaparamprofile", 708),
          ("cyanLagp", 709),
          ("userAsapT", 710),
          ("cyanBurstydegthresholdprofile", 711),
          ("cyanSonetsdhmsprofile", 712),
          ("cyanShelfprofile", 713),
          ("cyanEthpcp2cospidprofile", 714),
          ("cyanSonetsdhvcprofile", 715),
          ("cyanAugnprofile", 716),
          ("cyanInternalclockgen", 717),
          ("cyanStationclockgen", 718),
          ("cyanUsersonetsdhvcprofile", 719),
          ("cyanUsersonetsdhmsprofile", 720),
          ("cyanUserethpcp2cospidprofile", 721),
          ("cyanUserburstydegthresholdprofile", 722),
          ("cyanUserpgprofile", 723),
          ("cyanUsermsprProfile", 724),
          ("cyanUserlagp", 725),
          ("cyanDscp2cospidprofile", 726),
          ("cyanUserdscp2cospidprofile", 727),
          ("tcaparameterprofile", 728),
          ("usertcaparameterprofile", 729),
          ("mepTcaparameterprofile", 730),
          ("usermepTcaparameterprofile", 731),
          ("cyanOchtcaparameterprofile", 732),
          ("cyanUserochtcaparamprofile", 733),
          ("cyanMaclimitprofile", 734),
          ("cyanEdprofile", 735),
          ("cyanPcp2colorprofile", 736),
          ("cyanEqptprofile", 737),
          ("cyanUsereqptprofile", 738),
          ("cyanUser", 800),
          ("cyanRole", 801),
          ("cyanSshkeys", 802))
    )



class CyanProbablecausequalifierTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("comm1", 1),
          ("comm2", 2),
          ("unassigned", 3),
          ("hiRxpwr", 4),
          ("lowRxpwr", 5),
          ("hiTxpwr", 6),
          ("lowTxpwr", 7),
          ("hiVoltage", 8),
          ("lowVoltage", 9),
          ("hiCurrent", 10),
          ("lowCurrent", 11),
          ("hiTempRise", 12),
          ("memAccess", 13),
          ("pwrAOverVltg", 14),
          ("pwrAUnderVltg", 15),
          ("eidInvalid", 16),
          ("memFull", 17),
          ("memLow", 18),
          ("warmUp", 19),
          ("midStage", 20),
          ("fuse1Fail", 21),
          ("fuse2Fail", 22),
          ("fuse3Fail", 23),
          ("fuse4Fail", 24),
          ("pwrFeed1Loss", 25),
          ("pwrFeed2Loss", 26),
          ("pwrFeed3Loss", 27),
          ("pwrFeed4Loss", 28),
          ("pwrA", 29),
          ("pwrB", 30),
          ("och", 31),
          ("overhead", 32),
          ("payload", 33),
          ("provMism", 34),
          ("noResp", 35),
          ("farEnd", 36),
          ("hiRxpwrOh", 37),
          ("lowRxpwrOh", 38),
          ("hiTxpwrOh", 39),
          ("lowTxpwrOh", 40),
          ("txFreq", 41),
          ("rxFreq", 42),
          ("allPwrFeeds", 43),
          ("unitA", 44),
          ("unitB", 45),
          ("tx", 46),
          ("rx", 47),
          ("xover", 48),
          ("txPayload", 49),
          ("tec", 50),
          ("xcon", 51),
          ("error", 52),
          ("rmep", 53),
          ("macStat", 54),
          ("rdi", 55),
          ("unitC", 56),
          ("unitD", 57),
          ("i2cErr", 58),
          ("rtDiagNotsupp", 59),
          ("uncertified", 60),
          ("dupIpaddr", 61),
          ("dupNodename", 62),
          ("sntpHost", 63),
          ("ssf", 64),
          ("dyingGasp", 65),
          ("critical", 66),
          ("pwrFeedLoss", 67),
          ("maxTca", 68),
          ("packet", 69),
          ("mismerge", 70),
          ("unexmel", 71),
          ("unexmep", 72),
          ("unexperiod", 73),
          ("lacp", 74),
          ("cfgNotsupp", 75),
          ("lowPostamprxpwr", 80),
          ("lowRxspanloss", 81),
          ("hiRxspanloss", 82),
          ("diskLow", 83),
          ("cpuHi", 84),
          ("mfgmode", 85),
          ("ipc", 86),
          ("lbus", 87),
          ("ddrPktCrc", 88),
          ("eccFail", 89),
          ("farendSfP", 90),
          ("protocol", 91),
          ("nodeIdMism", 92),
          ("farendSfW", 93),
          ("apsByteFail", 94),
          ("dfltKbytes", 95),
          ("apsModeMism", 96),
          ("lockout", 97),
          ("manual", 98),
          ("forced", 99),
          ("esmc", 100),
          ("oscPrtcl", 101),
          ("dccFail", 102),
          ("gcc0Fail", 103),
          ("gcc12Fail", 104),
          ("apsChMism", 105),
          ("apsincmpld", 106),
          ("ccm", 107),
          ("path", 108),
          ("blocked", 109),
          ("dsbld", 110),
          ("fail", 111),
          ("csf", 112),
          ("lfd", 113),
          ("exmism", 114),
          ("ssm", 115),
          ("ip", 116),
          ("upm", 117),
          ("maint", 118),
          ("swMism", 201),
          ("swBad", 202),
          ("dbMism", 203),
          ("dbBad", 204),
          ("swUpgradeFail", 205),
          ("swUpgradeDsbld", 206),
          ("swIncompatible", 207),
          ("hiTemp", 301),
          ("lowTemp", 302),
          ("hiTempIn", 303),
          ("lowTempIn", 304),
          ("hiTempOut", 305),
          ("lowTempOut", 306),
          ("cooling", 307),
          ("rxLaserHiTemp", 311),
          ("rxLaserLowTemp", 312),
          ("rxLaserHiCurrent", 313),
          ("rxLaserLowCurrent", 314),
          ("rxLaserHiTxpwr", 315),
          ("rxLaserLowTxpwr", 316),
          ("rxTec", 317),
          ("wlenUnlocked", 318),
          ("apdPwrSupply", 319),
          ("rxFifoErr", 320),
          ("hwInterLock", 321),
          ("fanFilterDirty", 380),
          ("device", 381),
          ("pwrBOverVltg", 382),
          ("pwrBUnderVltg", 383),
          ("deviceGpio", 384),
          ("pwrFeedOverVltg", 385),
          ("pwrFeedUnderVltg", 386),
          ("compressorFail", 401),
          ("airConditioningFail", 402),
          ("airDryerFail", 403),
          ("batteryDischarge", 404),
          ("batteryFail", 405),
          ("coolFanFail", 406),
          ("engineFail", 407),
          ("engineOperating", 408),
          ("explosiveGas", 409),
          ("fireDetectorFail", 410),
          ("fire", 411),
          ("flood", 412),
          ("fuseFail", 413),
          ("generatorFail", 414),
          ("hiAirflow", 415),
          ("hiHumidity", 416),
          ("hiWater", 417),
          ("intrusion", 418),
          ("lowBatteryVoltage", 419),
          ("lowFuel", 420),
          ("lowHumidity", 421),
          ("lowCablePress", 422),
          ("lowWater", 423),
          ("userDefinedAlm1", 424),
          ("openDoor", 425),
          ("commPowerFail", 426),
          ("pumpFail", 427),
          ("powerSupplyFail", 428),
          ("rectifierFail", 429),
          ("rectifierHiVoltage", 430),
          ("rectifierLowVoltage", 431),
          ("smoke", 432),
          ("toxicGas", 433),
          ("ventilationFail", 434),
          ("userDefinedAlm2", 435),
          ("userDefinedAlm3", 436),
          ("userDefinedAlm4", 437),
          ("userDefinedAlm5", 438),
          ("remoteAco", 439),
          ("heatExchangerFail", 440),
          ("rectifierFailMjr", 441))
    )



class AssignedseverityTTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("nonalarmed", 1),
          ("freeChoice", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )



class EventtypeTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              61,
              62,
              63,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              91)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("objectcreation", 1),
          ("objectdeletion", 2),
          ("attributevaluechange", 3),
          ("statechange", 4),
          ("routechange", 5),
          ("alarm", 6),
          ("tca", 7),
          ("pmBeginunavailtime", 8),
          ("pmEndunavailtime", 9),
          ("pmContses", 10),
          ("pmStatechange", 11),
          ("pmStatechangetca", 12),
          ("filetransferstatusip", 21),
          ("filetransferstatusdone", 22),
          ("filetransferstatusfail", 23),
          ("backupstatusip", 24),
          ("backupstatusdone", 25),
          ("backupstatusfail", 26),
          ("dbRestoreip", 27),
          ("dbRestoredone", 28),
          ("dbRestorefail", 29),
          ("swdwnldip", 31),
          ("swdwnlddone", 32),
          ("swdwnldfail", 33),
          ("swupgradeip", 34),
          ("swupgradedone", 35),
          ("autoupgradeip", 36),
          ("autoupgradedone", 37),
          ("swrevertdone", 38),
          ("swautorevertip", 39),
          ("swmanrevertip", 40),
          ("equipped", 51),
          ("unequipped", 52),
          ("coldrestart", 53),
          ("warmrestart", 54),
          ("swmismatch", 55),
          ("autoprovisioning", 56),
          ("parityerror", 57),
          ("loginfail", 61),
          ("loginsucceed", 62),
          ("loginend", 63),
          ("pll", 71),
          ("go2freerun", 72),
          ("locked", 73),
          ("aps", 74),
          ("lockout", 75),
          ("manual", 76),
          ("forced", 77),
          ("ssm", 78),
          ("clear", 79),
          ("revertive", 80),
          ("eqptprotectionswitch", 81),
          ("protectionswitch", 82),
          ("heartbeat", 83),
          ("physicaltopochange", 91))
    )



# MIB Managed Objects in the order of their OIDs

_Cyan_ObjectIdentity = ObjectIdentity
cyan = _Cyan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533)
)
if mibBuilder.loadTexts:
    cyan.setStatus("current")
_CyanProducts_ObjectIdentity = ObjectIdentity
cyanProducts = _CyanProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1)
)
if mibBuilder.loadTexts:
    cyanProducts.setStatus("current")
_CyanZ77_ObjectIdentity = ObjectIdentity
cyanZ77 = _CyanZ77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 1)
)
_CyanLAMP_ObjectIdentity = ObjectIdentity
cyanLAMP = _CyanLAMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 2)
)
_CyanZ33_ObjectIdentity = ObjectIdentity
cyanZ33 = _CyanZ33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 3)
)
_CyanZ22_ObjectIdentity = ObjectIdentity
cyanZ22 = _CyanZ22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 1, 5)
)
_CyanMibModules_ObjectIdentity = ObjectIdentity
cyanMibModules = _CyanMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5)
)
if mibBuilder.loadTexts:
    cyanMibModules.setStatus("current")
_CyanAlarmObjectTypes_ObjectIdentity = ObjectIdentity
cyanAlarmObjectTypes = _CyanAlarmObjectTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20)
)
if mibBuilder.loadTexts:
    cyanAlarmObjectTypes.setStatus("current")
_CyanAlarmProbCause_Type = CyanProbablecauseTc
_CyanAlarmProbCause_Object = MibScalar
cyanAlarmProbCause = _CyanAlarmProbCause_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 1),
    _CyanAlarmProbCause_Type()
)
cyanAlarmProbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmProbCause.setStatus("current")
_CyanAlarmProbCauseQualifier_Type = CyanProbablecausequalifierTc
_CyanAlarmProbCauseQualifier_Object = MibScalar
cyanAlarmProbCauseQualifier = _CyanAlarmProbCauseQualifier_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 2),
    _CyanAlarmProbCauseQualifier_Type()
)
cyanAlarmProbCauseQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmProbCauseQualifier.setStatus("current")
_CyanAlarmSourceType_Type = CyanTypeTc
_CyanAlarmSourceType_Object = MibScalar
cyanAlarmSourceType = _CyanAlarmSourceType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 3),
    _CyanAlarmSourceType_Type()
)
cyanAlarmSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceType.setStatus("current")
_CyanAlarmSourceAddress_Type = DisplayString
_CyanAlarmSourceAddress_Object = MibScalar
cyanAlarmSourceAddress = _CyanAlarmSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 4),
    _CyanAlarmSourceAddress_Type()
)
cyanAlarmSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceAddress.setStatus("current")
_CyanAlarmState_Type = CyanAlarmstateTc
_CyanAlarmState_Object = MibScalar
cyanAlarmState = _CyanAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 5),
    _CyanAlarmState_Type()
)
cyanAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmState.setStatus("current")
_CyanAlarmSeverity_Type = AssignedseverityTTc
_CyanAlarmSeverity_Object = MibScalar
cyanAlarmSeverity = _CyanAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 6),
    _CyanAlarmSeverity_Type()
)
cyanAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSeverity.setStatus("current")
_CyanAlarmReportingTimeStamp_Type = Integer32
_CyanAlarmReportingTimeStamp_Object = MibScalar
cyanAlarmReportingTimeStamp = _CyanAlarmReportingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 7),
    _CyanAlarmReportingTimeStamp_Type()
)
cyanAlarmReportingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmReportingTimeStamp.setStatus("current")
_CyanAlarmAdditionalText_Type = DisplayString
_CyanAlarmAdditionalText_Object = MibScalar
cyanAlarmAdditionalText = _CyanAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 8),
    _CyanAlarmAdditionalText_Type()
)
cyanAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmAdditionalText.setStatus("current")
_CyanEventType_Type = EventtypeTc
_CyanEventType_Object = MibScalar
cyanEventType = _CyanEventType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 9),
    _CyanEventType_Type()
)
cyanEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventType.setStatus("current")
_CyanEventName_Type = DisplayString
_CyanEventName_Object = MibScalar
cyanEventName = _CyanEventName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 10),
    _CyanEventName_Type()
)
cyanEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventName.setStatus("current")
_CyanEventSourceType_Type = CyanTypeTc
_CyanEventSourceType_Object = MibScalar
cyanEventSourceType = _CyanEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 11),
    _CyanEventSourceType_Type()
)
cyanEventSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceType.setStatus("current")
_CyanEventSourceAddress_Type = DisplayString
_CyanEventSourceAddress_Object = MibScalar
cyanEventSourceAddress = _CyanEventSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 12),
    _CyanEventSourceAddress_Type()
)
cyanEventSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceAddress.setStatus("current")
_CyanEventReportingTimeStamp_Type = Integer32
_CyanEventReportingTimeStamp_Object = MibScalar
cyanEventReportingTimeStamp = _CyanEventReportingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 13),
    _CyanEventReportingTimeStamp_Type()
)
cyanEventReportingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventReportingTimeStamp.setStatus("current")
_CyanEventAdditionalText_Type = DisplayString
_CyanEventAdditionalText_Object = MibScalar
cyanEventAdditionalText = _CyanEventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 14),
    _CyanEventAdditionalText_Type()
)
cyanEventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventAdditionalText.setStatus("current")
_CyanEventNodeName_Type = DisplayString
_CyanEventNodeName_Object = MibScalar
cyanEventNodeName = _CyanEventNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 15),
    _CyanEventNodeName_Type()
)
cyanEventNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventNodeName.setStatus("current")
_CyanAlarmNodeName_Type = DisplayString
_CyanAlarmNodeName_Object = MibScalar
cyanAlarmNodeName = _CyanAlarmNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 16),
    _CyanAlarmNodeName_Type()
)
cyanAlarmNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmNodeName.setStatus("current")
_CyanAlarmSourceDescription_Type = DisplayString
_CyanAlarmSourceDescription_Object = MibScalar
cyanAlarmSourceDescription = _CyanAlarmSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 17),
    _CyanAlarmSourceDescription_Type()
)
cyanAlarmSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceDescription.setStatus("current")
_CyanAlarmSourceOSSLabel_Type = DisplayString
_CyanAlarmSourceOSSLabel_Object = MibScalar
cyanAlarmSourceOSSLabel = _CyanAlarmSourceOSSLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 18),
    _CyanAlarmSourceOSSLabel_Type()
)
cyanAlarmSourceOSSLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanAlarmSourceOSSLabel.setStatus("current")
_CyanEventSourceDescription_Type = DisplayString
_CyanEventSourceDescription_Object = MibScalar
cyanEventSourceDescription = _CyanEventSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 19),
    _CyanEventSourceDescription_Type()
)
cyanEventSourceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceDescription.setStatus("current")
_CyanEventSourceOSSLabel_Type = DisplayString
_CyanEventSourceOSSLabel_Object = MibScalar
cyanEventSourceOSSLabel = _CyanEventSourceOSSLabel_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 20, 20),
    _CyanEventSourceOSSLabel_Type()
)
cyanEventSourceOSSLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEventSourceOSSLabel.setStatus("current")
_CyanAlarmObjectGroups_ObjectIdentity = ObjectIdentity
cyanAlarmObjectGroups = _CyanAlarmObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21)
)
if mibBuilder.loadTexts:
    cyanAlarmObjectGroups.setStatus("current")
_CyanAlarms_ObjectIdentity = ObjectIdentity
cyanAlarms = _CyanAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30)
)
if mibBuilder.loadTexts:
    cyanAlarms.setStatus("current")
_CyanEntityModules_ObjectIdentity = ObjectIdentity
cyanEntityModules = _CyanEntityModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30)
)
if mibBuilder.loadTexts:
    cyanEntityModules.setStatus("current")

# Managed Objects groups

cyanAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21, 1)
)
cyanAlarmObjectGroup.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmObjectGroup.setStatus("current")

cyanEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 21, 2)
)
cyanEventObjectGroup.setObjects(
      *(("CYAN-MIB", "cyanEventType"),
        ("CYAN-MIB", "cyanEventName"),
        ("CYAN-MIB", "cyanEventSourceType"),
        ("CYAN-MIB", "cyanEventSourceAddress"),
        ("CYAN-MIB", "cyanEventReportingTimeStamp"),
        ("CYAN-MIB", "cyanEventAdditionalText"),
        ("CYAN-MIB", "cyanEventNodeName"),
        ("CYAN-MIB", "cyanEventSourceDescription"),
        ("CYAN-MIB", "cyanEventSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanEventObjectGroup.setStatus("current")


# Notification objects

cyanAlarmNa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 1)
)
cyanAlarmNa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmNa.setStatus(
        "current"
    )

cyanAlarmUnequipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 2)
)
cyanAlarmUnequipped.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmUnequipped.setStatus(
        "current"
    )

cyanAlarmEqptRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 3)
)
cyanAlarmEqptRestart.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptRestart.setStatus(
        "current"
    )

cyanAlarmEqptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 4)
)
cyanAlarmEqptFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptFail.setStatus(
        "current"
    )

cyanAlarmEqptDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 5)
)
cyanAlarmEqptDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptDgrade.setStatus(
        "current"
    )

cyanAlarmEqptMismtch = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 6)
)
cyanAlarmEqptMismtch.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptMismtch.setStatus(
        "current"
    )

cyanAlarmEqptUnexpected = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 7)
)
cyanAlarmEqptUnexpected.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptUnexpected.setStatus(
        "current"
    )

cyanAlarmEqptWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 8)
)
cyanAlarmEqptWarning.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEqptWarning.setStatus(
        "current"
    )

cyanAlarmNotConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 9)
)
cyanAlarmNotConfig.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmNotConfig.setStatus(
        "current"
    )

cyanAlarmAutoUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 12)
)
cyanAlarmAutoUpgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAutoUpgrade.setStatus(
        "current"
    )

cyanAlarmBatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 32)
)
cyanAlarmBatFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmBatFail.setStatus(
        "current"
    )

cyanAlarmBatDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 33)
)
cyanAlarmBatDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmBatDgrade.setStatus(
        "current"
    )

cyanAlarmTpLol = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 50)
)
cyanAlarmTpLol.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLol.setStatus(
        "current"
    )

cyanAlarmPreAmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 51)
)
cyanAlarmPreAmp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmPreAmp.setStatus(
        "current"
    )

cyanAlarmTpLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 52)
)
cyanAlarmTpLos.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLos.setStatus(
        "current"
    )

cyanAlarmTpLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 53)
)
cyanAlarmTpLoc.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoc.setStatus(
        "current"
    )

cyanAlarmTpLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 54)
)
cyanAlarmTpLof.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLof.setStatus(
        "current"
    )

cyanAlarmTpAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 55)
)
cyanAlarmTpAis.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpAis.setStatus(
        "current"
    )

cyanAlarmTpLom = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 56)
)
cyanAlarmTpLom.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLom.setStatus(
        "current"
    )

cyanAlarmTpSf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 57)
)
cyanAlarmTpSf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSf.setStatus(
        "current"
    )

cyanAlarmTpBdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 58)
)
cyanAlarmTpBdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpBdi.setStatus(
        "current"
    )

cyanAlarmTpFdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 59)
)
cyanAlarmTpFdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFdi.setStatus(
        "current"
    )

cyanAlarmTpPmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 60)
)
cyanAlarmTpPmi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpPmi.setStatus(
        "current"
    )

cyanAlarmTpSd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 61)
)
cyanAlarmTpSd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSd.setStatus(
        "current"
    )

cyanAlarmTpRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 62)
)
cyanAlarmTpRdi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpRdi.setStatus(
        "current"
    )

cyanAlarmTpTim = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 63)
)
cyanAlarmTpTim.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpTim.setStatus(
        "current"
    )

cyanAlarmTpIae = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 64)
)
cyanAlarmTpIae.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpIae.setStatus(
        "current"
    )

cyanAlarmTpBiae = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 65)
)
cyanAlarmTpBiae.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpBiae.setStatus(
        "current"
    )

cyanAlarmTpOci = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 66)
)
cyanAlarmTpOci.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOci.setStatus(
        "current"
    )

cyanAlarmTpLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 67)
)
cyanAlarmTpLck.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLck.setStatus(
        "current"
    )

cyanAlarmTpLoflom = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 68)
)
cyanAlarmTpLoflom.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoflom.setStatus(
        "current"
    )

cyanAlarmTpSsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 69)
)
cyanAlarmTpSsf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSsf.setStatus(
        "current"
    )

cyanAlarmTpOorangeAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 70)
)
cyanAlarmTpOorangeAlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOorangeAlm.setStatus(
        "current"
    )

cyanAlarmTpOorangeWrn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 71)
)
cyanAlarmTpOorangeWrn.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpOorangeWrn.setStatus(
        "current"
    )

cyanAlarmTpFaclpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 72)
)
cyanAlarmTpFaclpbk.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFaclpbk.setStatus(
        "current"
    )

cyanAlarmTpHighLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 73)
)
cyanAlarmTpHighLoss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpHighLoss.setStatus(
        "current"
    )

cyanAlarmTpLowLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 74)
)
cyanAlarmTpLowLoss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLowLoss.setStatus(
        "current"
    )

cyanAlarmTpFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 75)
)
cyanAlarmTpFiber.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpFiber.setStatus(
        "current"
    )

cyanAlarmTpPlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 76)
)
cyanAlarmTpPlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpPlm.setStatus(
        "current"
    )

cyanAlarmTpLtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 77)
)
cyanAlarmTpLtc.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLtc.setStatus(
        "current"
    )

cyanAlarmTpMsim = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 78)
)
cyanAlarmTpMsim.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpMsim.setStatus(
        "current"
    )

cyanAlarmProtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 79)
)
cyanAlarmProtFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtFail.setStatus(
        "current"
    )

cyanAlarmCcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 80)
)
cyanAlarmCcm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCcm.setStatus(
        "current"
    )

cyanAlarmTpLfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 81)
)
cyanAlarmTpLfd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLfd.setStatus(
        "current"
    )

cyanAlarmTpLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 82)
)
cyanAlarmTpLink.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLink.setStatus(
        "current"
    )

cyanAlarmTpGfp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 83)
)
cyanAlarmTpGfp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpGfp.setStatus(
        "current"
    )

cyanAlarmTpTpt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 84)
)
cyanAlarmTpTpt.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpTpt.setStatus(
        "current"
    )

cyanAlarmGtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 85)
)
cyanAlarmGtp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmGtp.setStatus(
        "current"
    )

cyanAlarmTpSqm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 86)
)
cyanAlarmTpSqm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpSqm.setStatus(
        "current"
    )

cyanAlarmTpLoa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 87)
)
cyanAlarmTpLoa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoa.setStatus(
        "current"
    )

cyanAlarmTpLti = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 88)
)
cyanAlarmTpLti.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLti.setStatus(
        "current"
    )

cyanAlarmLtm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 89)
)
cyanAlarmLtm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLtm.setStatus(
        "current"
    )

cyanAlarmAps = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 90)
)
cyanAlarmAps.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAps.setStatus(
        "current"
    )

cyanAlarmTpLop = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 91)
)
cyanAlarmTpLop.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLop.setStatus(
        "current"
    )

cyanAlarmTpUneq = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 92)
)
cyanAlarmTpUneq.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpUneq.setStatus(
        "current"
    )

cyanAlarmCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 93)
)
cyanAlarmCsf.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCsf.setStatus(
        "current"
    )

cyanAlarmExmism = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 94)
)
cyanAlarmExmism.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmExmism.setStatus(
        "current"
    )

cyanAlarmUpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 95)
)
cyanAlarmUpm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmUpm.setStatus(
        "current"
    )

cyanAlarmProtCmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 96)
)
cyanAlarmProtCmd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtCmd.setStatus(
        "current"
    )

cyanAlarmFarendCmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 97)
)
cyanAlarmFarendCmd.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmFarendCmd.setStatus(
        "current"
    )

cyanAlarmProtocolErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 98)
)
cyanAlarmProtocolErr.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmProtocolErr.setStatus(
        "current"
    )

cyanAlarmLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 99)
)
cyanAlarmLoopback.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLoopback.setStatus(
        "current"
    )

cyanAlarmLmm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 100)
)
cyanAlarmLmm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmLmm.setStatus(
        "current"
    )

cyanAlarmDmm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 101)
)
cyanAlarmDmm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmDmm.setStatus(
        "current"
    )

cyanAlarmCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 102)
)
cyanAlarmCommFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCommFail.setStatus(
        "current"
    )

cyanAlarmCommDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 103)
)
cyanAlarmCommDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmCommDgrade.setStatus(
        "current"
    )

cyanAlarmPacketLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 104)
)
cyanAlarmPacketLpbk.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmPacketLpbk.setStatus(
        "current"
    )

cyanAlarmXcspktsloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 105)
)
cyanAlarmXcspktsloss.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcspktsloss.setStatus(
        "current"
    )

cyanAlarmXcspktserr = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 106)
)
cyanAlarmXcspktserr.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcspktserr.setStatus(
        "current"
    )

cyanAlarmSrcaddrmis = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 107)
)
cyanAlarmSrcaddrmis.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSrcaddrmis.setStatus(
        "current"
    )

cyanAlarmArp = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 108)
)
cyanAlarmArp.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmArp.setStatus(
        "current"
    )

cyanAlarmTsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 109)
)
cyanAlarmTsa.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTsa.setStatus(
        "current"
    )

cyanAlarmErpPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 110)
)
cyanAlarmErpPort.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmErpPort.setStatus(
        "current"
    )

cyanAlarmTpLoomfi = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 111)
)
cyanAlarmTpLoomfi.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmTpLoomfi.setStatus(
        "current"
    )

cyanAlarmSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 202)
)
cyanAlarmSyncFail.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncFail.setStatus(
        "current"
    )

cyanAlarmSyncDgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 203)
)
cyanAlarmSyncDgrade.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncDgrade.setStatus(
        "current"
    )

cyanAlarmHoldover = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 204)
)
cyanAlarmHoldover.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmHoldover.setStatus(
        "current"
    )

cyanAlarmXcsholdover = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 205)
)
cyanAlarmXcsholdover.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmXcsholdover.setStatus(
        "current"
    )

cyanAlarmSyncExcmdActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 206)
)
cyanAlarmSyncExcmdActive.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmSyncExcmdActive.setStatus(
        "current"
    )

cyanAlarmEnvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 302)
)
cyanAlarmEnvAlm.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEnvAlm.setStatus(
        "current"
    )

cyanAlarmEnvWrn = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 303)
)
cyanAlarmEnvWrn.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmEnvWrn.setStatus(
        "current"
    )

cyanAlarmIncmpld = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 402)
)
cyanAlarmIncmpld.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmIncmpld.setStatus(
        "current"
    )

cyanAlarmAdmin = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 403)
)
cyanAlarmAdmin.setObjects(
      *(("CYAN-MIB", "cyanAlarmProbCause"),
        ("CYAN-MIB", "cyanAlarmProbCauseQualifier"),
        ("CYAN-MIB", "cyanAlarmSourceType"),
        ("CYAN-MIB", "cyanAlarmSourceAddress"),
        ("CYAN-MIB", "cyanAlarmState"),
        ("CYAN-MIB", "cyanAlarmSeverity"),
        ("CYAN-MIB", "cyanAlarmReportingTimeStamp"),
        ("CYAN-MIB", "cyanAlarmAdditionalText"),
        ("CYAN-MIB", "cyanAlarmNodeName"),
        ("CYAN-MIB", "cyanAlarmSourceDescription"),
        ("CYAN-MIB", "cyanAlarmSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanAlarmAdmin.setStatus(
        "current"
    )

cyanEventTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 30, 10008)
)
cyanEventTca.setObjects(
      *(("CYAN-MIB", "cyanEventType"),
        ("CYAN-MIB", "cyanEventName"),
        ("CYAN-MIB", "cyanEventSourceType"),
        ("CYAN-MIB", "cyanEventSourceAddress"),
        ("CYAN-MIB", "cyanEventReportingTimeStamp"),
        ("CYAN-MIB", "cyanEventAdditionalText"),
        ("CYAN-MIB", "cyanEventNodeName"),
        ("CYAN-MIB", "cyanEventSourceDescription"),
        ("CYAN-MIB", "cyanEventSourceOSSLabel"))
)
if mibBuilder.loadTexts:
    cyanEventTca.setStatus(
        "current"
    )


# Notifications groups

cyanAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 50)
)
cyanAlarmGroup.setObjects(
      *(("CYAN-MIB", "cyanAlarmNa"),
        ("CYAN-MIB", "cyanAlarmUnequipped"),
        ("CYAN-MIB", "cyanAlarmEqptRestart"),
        ("CYAN-MIB", "cyanAlarmEqptFail"),
        ("CYAN-MIB", "cyanAlarmEqptDgrade"),
        ("CYAN-MIB", "cyanAlarmEqptMismtch"),
        ("CYAN-MIB", "cyanAlarmEqptUnexpected"),
        ("CYAN-MIB", "cyanAlarmEqptWarning"),
        ("CYAN-MIB", "cyanAlarmNotConfig"),
        ("CYAN-MIB", "cyanAlarmAutoUpgrade"),
        ("CYAN-MIB", "cyanAlarmBatFail"),
        ("CYAN-MIB", "cyanAlarmBatDgrade"),
        ("CYAN-MIB", "cyanAlarmTpLol"),
        ("CYAN-MIB", "cyanAlarmPreAmp"),
        ("CYAN-MIB", "cyanAlarmTpLos"),
        ("CYAN-MIB", "cyanAlarmTpLoc"),
        ("CYAN-MIB", "cyanAlarmTpLof"),
        ("CYAN-MIB", "cyanAlarmTpAis"),
        ("CYAN-MIB", "cyanAlarmTpLom"),
        ("CYAN-MIB", "cyanAlarmTpSf"),
        ("CYAN-MIB", "cyanAlarmTpBdi"),
        ("CYAN-MIB", "cyanAlarmTpFdi"),
        ("CYAN-MIB", "cyanAlarmTpPmi"),
        ("CYAN-MIB", "cyanAlarmTpSd"),
        ("CYAN-MIB", "cyanAlarmTpRdi"),
        ("CYAN-MIB", "cyanAlarmTpTim"),
        ("CYAN-MIB", "cyanAlarmTpIae"),
        ("CYAN-MIB", "cyanAlarmTpBiae"),
        ("CYAN-MIB", "cyanAlarmTpOci"),
        ("CYAN-MIB", "cyanAlarmTpLck"),
        ("CYAN-MIB", "cyanAlarmTpLoflom"),
        ("CYAN-MIB", "cyanAlarmTpSsf"),
        ("CYAN-MIB", "cyanAlarmTpOorangeAlm"),
        ("CYAN-MIB", "cyanAlarmTpOorangeWrn"),
        ("CYAN-MIB", "cyanAlarmTpFaclpbk"),
        ("CYAN-MIB", "cyanAlarmTpHighLoss"),
        ("CYAN-MIB", "cyanAlarmTpLowLoss"),
        ("CYAN-MIB", "cyanAlarmTpFiber"),
        ("CYAN-MIB", "cyanAlarmTpPlm"),
        ("CYAN-MIB", "cyanAlarmTpLtc"),
        ("CYAN-MIB", "cyanAlarmTpMsim"),
        ("CYAN-MIB", "cyanAlarmProtFail"),
        ("CYAN-MIB", "cyanAlarmCcm"),
        ("CYAN-MIB", "cyanAlarmTpLfd"),
        ("CYAN-MIB", "cyanAlarmTpLink"),
        ("CYAN-MIB", "cyanAlarmTpGfp"),
        ("CYAN-MIB", "cyanAlarmTpTpt"),
        ("CYAN-MIB", "cyanAlarmGtp"),
        ("CYAN-MIB", "cyanAlarmTpSqm"),
        ("CYAN-MIB", "cyanAlarmTpLoa"),
        ("CYAN-MIB", "cyanAlarmTpLti"),
        ("CYAN-MIB", "cyanAlarmLtm"),
        ("CYAN-MIB", "cyanAlarmAps"),
        ("CYAN-MIB", "cyanAlarmTpLop"),
        ("CYAN-MIB", "cyanAlarmTpUneq"),
        ("CYAN-MIB", "cyanAlarmCsf"),
        ("CYAN-MIB", "cyanAlarmExmism"),
        ("CYAN-MIB", "cyanAlarmUpm"),
        ("CYAN-MIB", "cyanAlarmProtCmd"),
        ("CYAN-MIB", "cyanAlarmFarendCmd"),
        ("CYAN-MIB", "cyanAlarmProtocolErr"),
        ("CYAN-MIB", "cyanAlarmLoopback"),
        ("CYAN-MIB", "cyanAlarmLmm"),
        ("CYAN-MIB", "cyanAlarmDmm"),
        ("CYAN-MIB", "cyanAlarmCommFail"),
        ("CYAN-MIB", "cyanAlarmCommDgrade"),
        ("CYAN-MIB", "cyanAlarmPacketLpbk"),
        ("CYAN-MIB", "cyanAlarmXcspktsloss"),
        ("CYAN-MIB", "cyanAlarmXcspktserr"),
        ("CYAN-MIB", "cyanAlarmSrcaddrmis"),
        ("CYAN-MIB", "cyanAlarmArp"),
        ("CYAN-MIB", "cyanAlarmTsa"),
        ("CYAN-MIB", "cyanAlarmErpPort"),
        ("CYAN-MIB", "cyanAlarmTpLoomfi"),
        ("CYAN-MIB", "cyanAlarmSyncFail"),
        ("CYAN-MIB", "cyanAlarmSyncDgrade"),
        ("CYAN-MIB", "cyanAlarmHoldover"),
        ("CYAN-MIB", "cyanAlarmXcsholdover"),
        ("CYAN-MIB", "cyanAlarmSyncExcmdActive"),
        ("CYAN-MIB", "cyanAlarmEnvAlm"),
        ("CYAN-MIB", "cyanAlarmEnvWrn"),
        ("CYAN-MIB", "cyanAlarmIncmpld"),
        ("CYAN-MIB", "cyanAlarmAdmin"),
        ("CYAN-MIB", "cyanEventTca"))
)
if mibBuilder.loadTexts:
    cyanAlarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cyanAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 20, 60)
)
cyanAlarmCompliance.setObjects(
      *(("CYAN-MIB", "cyanAlarmGroup"),
        ("CYAN-MIB", "cyanAlarmObjectGroup"),
        ("CYAN-MIB", "cyanEventObjectGroup"))
)
if mibBuilder.loadTexts:
    cyanAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-MIB",
    **{"CyanProbablecauseTc": CyanProbablecauseTc,
       "CyanAlarmstateTc": CyanAlarmstateTc,
       "CyanTypeTc": CyanTypeTc,
       "CyanProbablecausequalifierTc": CyanProbablecausequalifierTc,
       "AssignedseverityTTc": AssignedseverityTTc,
       "EventtypeTc": EventtypeTc,
       "cyan": cyan,
       "cyanProducts": cyanProducts,
       "cyanZ77": cyanZ77,
       "cyanLAMP": cyanLAMP,
       "cyanZ33": cyanZ33,
       "cyanZ22": cyanZ22,
       "cyanMibModules": cyanMibModules,
       "cyanAlarmMibModule": cyanAlarmMibModule,
       "cyanAlarmObjectTypes": cyanAlarmObjectTypes,
       "cyanAlarmProbCause": cyanAlarmProbCause,
       "cyanAlarmProbCauseQualifier": cyanAlarmProbCauseQualifier,
       "cyanAlarmSourceType": cyanAlarmSourceType,
       "cyanAlarmSourceAddress": cyanAlarmSourceAddress,
       "cyanAlarmState": cyanAlarmState,
       "cyanAlarmSeverity": cyanAlarmSeverity,
       "cyanAlarmReportingTimeStamp": cyanAlarmReportingTimeStamp,
       "cyanAlarmAdditionalText": cyanAlarmAdditionalText,
       "cyanEventType": cyanEventType,
       "cyanEventName": cyanEventName,
       "cyanEventSourceType": cyanEventSourceType,
       "cyanEventSourceAddress": cyanEventSourceAddress,
       "cyanEventReportingTimeStamp": cyanEventReportingTimeStamp,
       "cyanEventAdditionalText": cyanEventAdditionalText,
       "cyanEventNodeName": cyanEventNodeName,
       "cyanAlarmNodeName": cyanAlarmNodeName,
       "cyanAlarmSourceDescription": cyanAlarmSourceDescription,
       "cyanAlarmSourceOSSLabel": cyanAlarmSourceOSSLabel,
       "cyanEventSourceDescription": cyanEventSourceDescription,
       "cyanEventSourceOSSLabel": cyanEventSourceOSSLabel,
       "cyanAlarmObjectGroups": cyanAlarmObjectGroups,
       "cyanAlarmObjectGroup": cyanAlarmObjectGroup,
       "cyanEventObjectGroup": cyanEventObjectGroup,
       "cyanAlarms": cyanAlarms,
       "cyanAlarmNa": cyanAlarmNa,
       "cyanAlarmUnequipped": cyanAlarmUnequipped,
       "cyanAlarmEqptRestart": cyanAlarmEqptRestart,
       "cyanAlarmEqptFail": cyanAlarmEqptFail,
       "cyanAlarmEqptDgrade": cyanAlarmEqptDgrade,
       "cyanAlarmEqptMismtch": cyanAlarmEqptMismtch,
       "cyanAlarmEqptUnexpected": cyanAlarmEqptUnexpected,
       "cyanAlarmEqptWarning": cyanAlarmEqptWarning,
       "cyanAlarmNotConfig": cyanAlarmNotConfig,
       "cyanAlarmAutoUpgrade": cyanAlarmAutoUpgrade,
       "cyanAlarmBatFail": cyanAlarmBatFail,
       "cyanAlarmBatDgrade": cyanAlarmBatDgrade,
       "cyanAlarmTpLol": cyanAlarmTpLol,
       "cyanAlarmPreAmp": cyanAlarmPreAmp,
       "cyanAlarmTpLos": cyanAlarmTpLos,
       "cyanAlarmTpLoc": cyanAlarmTpLoc,
       "cyanAlarmTpLof": cyanAlarmTpLof,
       "cyanAlarmTpAis": cyanAlarmTpAis,
       "cyanAlarmTpLom": cyanAlarmTpLom,
       "cyanAlarmTpSf": cyanAlarmTpSf,
       "cyanAlarmTpBdi": cyanAlarmTpBdi,
       "cyanAlarmTpFdi": cyanAlarmTpFdi,
       "cyanAlarmTpPmi": cyanAlarmTpPmi,
       "cyanAlarmTpSd": cyanAlarmTpSd,
       "cyanAlarmTpRdi": cyanAlarmTpRdi,
       "cyanAlarmTpTim": cyanAlarmTpTim,
       "cyanAlarmTpIae": cyanAlarmTpIae,
       "cyanAlarmTpBiae": cyanAlarmTpBiae,
       "cyanAlarmTpOci": cyanAlarmTpOci,
       "cyanAlarmTpLck": cyanAlarmTpLck,
       "cyanAlarmTpLoflom": cyanAlarmTpLoflom,
       "cyanAlarmTpSsf": cyanAlarmTpSsf,
       "cyanAlarmTpOorangeAlm": cyanAlarmTpOorangeAlm,
       "cyanAlarmTpOorangeWrn": cyanAlarmTpOorangeWrn,
       "cyanAlarmTpFaclpbk": cyanAlarmTpFaclpbk,
       "cyanAlarmTpHighLoss": cyanAlarmTpHighLoss,
       "cyanAlarmTpLowLoss": cyanAlarmTpLowLoss,
       "cyanAlarmTpFiber": cyanAlarmTpFiber,
       "cyanAlarmTpPlm": cyanAlarmTpPlm,
       "cyanAlarmTpLtc": cyanAlarmTpLtc,
       "cyanAlarmTpMsim": cyanAlarmTpMsim,
       "cyanAlarmProtFail": cyanAlarmProtFail,
       "cyanAlarmCcm": cyanAlarmCcm,
       "cyanAlarmTpLfd": cyanAlarmTpLfd,
       "cyanAlarmTpLink": cyanAlarmTpLink,
       "cyanAlarmTpGfp": cyanAlarmTpGfp,
       "cyanAlarmTpTpt": cyanAlarmTpTpt,
       "cyanAlarmGtp": cyanAlarmGtp,
       "cyanAlarmTpSqm": cyanAlarmTpSqm,
       "cyanAlarmTpLoa": cyanAlarmTpLoa,
       "cyanAlarmTpLti": cyanAlarmTpLti,
       "cyanAlarmLtm": cyanAlarmLtm,
       "cyanAlarmAps": cyanAlarmAps,
       "cyanAlarmTpLop": cyanAlarmTpLop,
       "cyanAlarmTpUneq": cyanAlarmTpUneq,
       "cyanAlarmCsf": cyanAlarmCsf,
       "cyanAlarmExmism": cyanAlarmExmism,
       "cyanAlarmUpm": cyanAlarmUpm,
       "cyanAlarmProtCmd": cyanAlarmProtCmd,
       "cyanAlarmFarendCmd": cyanAlarmFarendCmd,
       "cyanAlarmProtocolErr": cyanAlarmProtocolErr,
       "cyanAlarmLoopback": cyanAlarmLoopback,
       "cyanAlarmLmm": cyanAlarmLmm,
       "cyanAlarmDmm": cyanAlarmDmm,
       "cyanAlarmCommFail": cyanAlarmCommFail,
       "cyanAlarmCommDgrade": cyanAlarmCommDgrade,
       "cyanAlarmPacketLpbk": cyanAlarmPacketLpbk,
       "cyanAlarmXcspktsloss": cyanAlarmXcspktsloss,
       "cyanAlarmXcspktserr": cyanAlarmXcspktserr,
       "cyanAlarmSrcaddrmis": cyanAlarmSrcaddrmis,
       "cyanAlarmArp": cyanAlarmArp,
       "cyanAlarmTsa": cyanAlarmTsa,
       "cyanAlarmErpPort": cyanAlarmErpPort,
       "cyanAlarmTpLoomfi": cyanAlarmTpLoomfi,
       "cyanAlarmSyncFail": cyanAlarmSyncFail,
       "cyanAlarmSyncDgrade": cyanAlarmSyncDgrade,
       "cyanAlarmHoldover": cyanAlarmHoldover,
       "cyanAlarmXcsholdover": cyanAlarmXcsholdover,
       "cyanAlarmSyncExcmdActive": cyanAlarmSyncExcmdActive,
       "cyanAlarmEnvAlm": cyanAlarmEnvAlm,
       "cyanAlarmEnvWrn": cyanAlarmEnvWrn,
       "cyanAlarmIncmpld": cyanAlarmIncmpld,
       "cyanAlarmAdmin": cyanAlarmAdmin,
       "cyanEventTca": cyanEventTca,
       "cyanAlarmGroup": cyanAlarmGroup,
       "cyanAlarmCompliance": cyanAlarmCompliance,
       "cyanEntityModules": cyanEntityModules}
)
