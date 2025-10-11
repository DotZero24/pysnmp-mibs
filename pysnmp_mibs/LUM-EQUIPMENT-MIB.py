# SNMP MIB module (LUM-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-EQUIPMENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:45 2025
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

(AlarmPerceivedSeverity,) = mibBuilder.importSymbols(
    "LUM-ALARM-MIB",
    "AlarmPerceivedSeverity")

(lumEquipmentMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumEquipmentMIB",
    "lumModules")

(AdminStatus,
 BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 SlotNumber,
 SubrackNumber,
 TruthValueWithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatus",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "SlotNumber",
    "SubrackNumber",
    "TruthValueWithNA")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumEquipmentMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 12)
)
if mibBuilder.loadTexts:
    lumEquipmentMIBModule.setRevisions(
        ("2018-12-21 00:00",
         "2018-07-01 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2017-02-25 00:00",
         "2016-11-30 00:00",
         "2016-07-15 00:00",
         "2015-09-30 00:00",
         "2015-09-15 00:00",
         "2015-01-13 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-01 00:00",
         "2012-12-20 00:00",
         "2011-12-20 00:00",
         "2011-06-21 11:00",
         "2011-04-27 11:00",
         "2007-01-31 11:00",
         "2006-01-27 00:00",
         "2005-09-26 00:00",
         "2005-09-14 00:00",
         "2003-02-17 00:00",
         "2002-11-20 00:00",
         "2002-09-16 00:00",
         "2002-05-31 00:00",
         "2002-03-05 00:00",
         "2002-02-21 00:00",
         "2002-02-20 00:00",
         "2001-12-03 00:00",
         "2001-11-22 00:00",
         "2001-11-09 00:00",
         "2001-10-30 00:00",
         "2001-10-25 00:00",
         "2001-10-23 00:00",
         "2001-10-10 00:00",
         "2001-08-14 00:00",
         "2001-08-09 00:00",
         "2001-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EquipmentSubrackType(TextualConvention, Integer32):
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
              9002,
              9006,
              9011,
              9013)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tm300", 1),
          ("tm3000", 2),
          ("tm301", 3),
          ("tm101", 4),
          ("tm101p", 5),
          ("aux", 6),
          ("tm102", 7),
          ("mba1", 8),
          ("mba2", 9),
          ("mba2E", 10),
          ("tm102pas", 11),
          ("tm102pas3", 12),
          ("tm3000ii", 13),
          ("tm2000", 14),
          ("tm301ii", 15),
          ("tmFha1UDc1", 16),
          ("tmRfuAc1", 17),
          ("tmEmxp1UDc", 18),
          ("tmHdea1600Dc", 19),
          ("tm3000iie", 20),
          ("ts1100Subrack2Slots", 9002),
          ("tm206Subrack6Slots", 9006),
          ("ts1100Subrack8Slots", 9011),
          ("ts1100Subrack12Slots", 9013))
    )



class EquipmentBoardType(TextualConvention, Integer32):
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
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
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
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              1001,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1014,
              1015,
              1016,
              1040,
              1041,
              1042,
              1043,
              1044,
              1050,
              1051,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1070,
              1080,
              1081,
              1082,
              1083,
              1084,
              1085,
              2012,
              2014,
              10000,
              10001,
              10002,
              10003,
              10004,
              10005,
              20000,
              20001,
              20002,
              20003,
              20004,
              220401,
              250101,
              250201,
              260401,
              261001,
              270001,
              540001,
              540002,
              540003,
              550000,
              580000,
              581000,
              590000,
              600100,
              600300,
              740001,
              750000,
              760000,
              770000,
              772000,
              790000,
              791000,
              802001,
              803000,
              803100,
              803200,
              803300,
              812001,
              813001,
              813101,
              813200,
              813300,
              813400,
              814001,
              814101,
              823000,
              850100,
              870101,
              870102,
              883001,
              883101,
              900000,
              904800,
              912200,
              914800,
              922000,
              5800002,
              5800003,
              5800004,
              5810002,
              5810003,
              5900002,
              7910002,
              9200201,
              9221001,
              9221002,
              9500101,
              9510101,
              9510201,
              9510301,
              9510401,
              9510501,
              9600201,
              9600202,
              9780001,
              9813001,
              9813101,
              9814001,
              9814101,
              9823001,
              9823002,
              9870101)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("cu", 1),
          ("tpMr2500", 2),
          ("oxc8", 3),
          ("oxc16", 4),
          ("ocu2", 5),
          ("mxp028", 6),
          ("ad1AB", 7),
          ("ad1BA", 8),
          ("ad2AB", 9),
          ("ad2BA", 10),
          ("ad4AB", 11),
          ("ad4BA", 12),
          ("tpDGbE", 13),
          ("oa", 14),
          ("mdu8Ext", 15),
          ("mdu8Term", 16),
          ("ocu4", 17),
          ("mxp004", 18),
          ("ad2oaAB", 19),
          ("ad2oaBA", 20),
          ("oa2", 21),
          ("adcwdm", 22),
          ("ad1spr", 23),
          ("tp10G", 24),
          ("tpLMr2500", 25),
          ("cu1osc", 26),
          ("cu2osc", 27),
          ("obu", 28),
          ("sync2Mhz", 29),
          ("mxp8", 30),
          ("mxp16", 31),
          ("tpDGbED", 32),
          ("tpDGbEC", 33),
          ("tpDFcD", 34),
          ("tpDFcC", 35),
          ("tpFcGbED", 36),
          ("tpFcGbEC", 37),
          ("tpTFcD", 38),
          ("tpQMr", 39),
          ("mdu4TermAB", 40),
          ("mdu4TermBA", 41),
          ("ad1cwdm", 42),
          ("ad2cwdm", 43),
          ("tp10GLAN", 44),
          ("tp10GRC", 45),
          ("escon8", 46),
          ("oa1x15dBm", 47),
          ("oa2x15dBm", 48),
          ("gxp2500", 49),
          ("gxp2500Sfp", 50),
          ("gxp10G", 51),
          ("tpDGbEDv2", 52),
          ("tpDGbESfp", 53),
          ("tpDFcDv2", 54),
          ("tpDFcSfp", 55),
          ("ad2x1cwdm", 56),
          ("ad2x2cwdm", 57),
          ("mdu8Term2", 58),
          ("tpDDGbE", 59),
          ("fpuOas2824", 60),
          ("mu2F8C", 61),
          ("du2F8C", 62),
          ("tpD10GL", 63),
          ("tpDDGbER", 64),
          ("tp10GBu", 65),
          ("tp10GLANBu", 66),
          ("tp10GClBu", 67),
          ("tp10GLANClBu", 68),
          ("mdu8EvenExt", 69),
          ("mdu8EvenTerm", 70),
          ("oapre1x17dBm", 71),
          ("oa2x17dBm", 72),
          ("oiuc100200", 73),
          ("oapow1x17dBm", 74),
          ("oa1x17dBm", 75),
          ("gbe9Mxp10G", 76),
          ("ad1dwdm2F", 77),
          ("ad1cwdm2F", 78),
          ("mdu4Ext2F", 79),
          ("mdu4Term2F", 80),
          ("voa8ch", 81),
          ("oa1x20dBm", 82),
          ("oa2x20dBm", 83),
          ("fpuYm235", 84),
          ("ad4dwdm2F", 85),
          ("tpQMri", 86),
          ("oar450c", 87),
          ("cuSfp", 88),
          ("tpMr25v2", 89),
          ("tpD10GbE", 90),
          ("tpD10GbER", 91),
          ("mdu4ExtAB", 92),
          ("mdu4ExtBA", 93),
          ("oiuc50100", 94),
          ("mROADM1P800", 95),
          ("edu6pGbE", 96),
          ("tp10GClTc", 97),
          ("mxp4x2G5", 98),
          ("oa1xLG20dBm", 99),
          ("oa2xLG20dBm", 100),
          ("oa1xFG10dBm", 101),
          ("oa2xFG10dBm", 102),
          ("tp10GOtnTc", 103),
          ("mdu40Even", 104),
          ("mdu40Odd", 105),
          ("mdu8Ee", 106),
          ("mdu8Eo", 107),
          ("ocm2p", 108),
          ("msMxp", 109),
          ("voa8chii", 110),
          ("msMxpR", 111),
          ("msMxpDQgbe", 112),
          ("tp10GTcEr", 113),
          ("gbe10Emxp10G", 114),
          ("edu12pGbE", 115),
          ("gbeMxp10GFEC", 116),
          ("roadm1x4G100", 117),
          ("dQgbeMxpR", 118),
          ("tpQMS", 119),
          ("tpQMSR", 120),
          ("gbe22Emxp10G", 121),
          ("oa1x26dBm", 122),
          ("pcu2p", 123),
          ("mxp4x2G5Oc", 124),
          ("voa2ch", 125),
          ("msMxp10GTCEr", 126),
          ("msMxp10G", 127),
          ("msMxpQMS2G5", 128),
          ("gbe22Emxp10Gii", 129),
          ("bsu1x5Even", 130),
          ("bsu1x5Odd", 131),
          ("gbe10Emxp10Gii", 132),
          ("mba1", 133),
          ("mba1SonetDeprecated", 134),
          ("mba2", 135),
          ("mba2SonetDeprecated", 136),
          ("mxpmbh1Sdh", 137),
          ("mxpmbh1Sonet", 138),
          ("roadm1x8G50", 139),
          ("ad4Even50", 140),
          ("ad4Odd50", 141),
          ("emxp80Gii", 142),
          ("msMxpQMS2G5R", 143),
          ("mxp8iiSdh", 144),
          ("mxp8iiSonet", 145),
          ("mba2E", 146),
          ("mba2ptpSdh", 147),
          ("mba2ptpSonet", 148),
          ("mba2EptpSdh", 149),
          ("mba2EptpSonet", 150),
          ("mdu40EvenL", 151),
          ("mdu40OddL", 152),
          ("oa1x20dBmVg", 153),
          ("oa2x20dBmVg", 154),
          ("roadm1x2G100", 155),
          ("roadm1x2G50", 156),
          ("tpq10Gfec", 157),
          ("cuSfpii", 158),
          ("coD40ev", 159),
          ("coD40eve", 160),
          ("coD40od", 161),
          ("coD40ode", 162),
          ("dcDk652km20", 163),
          ("dcDk652km40", 164),
          ("dcDk652km60", 165),
          ("dcDk652km80", 166),
          ("dcP652km40", 167),
          ("dcP652km60", 168),
          ("dcP652km80", 169),
          ("dcP652km100", 170),
          ("dcP652km120", 171),
          ("emxp40Gii", 172),
          ("tpqmp", 173),
          ("tpq10GfecReg", 174),
          ("mdu16cl50g", 175),
          ("voa8chsfp", 176),
          ("msTp40G", 177),
          ("msMxp40G", 178),
          ("mxp10gotn", 179),
          ("emxp62iie", 180),
          ("emxp120iie", 181),
          ("ocudq", 182),
          ("tm4700", 183),
          ("tm4011", 184),
          ("tm100mxp", 185),
          ("tm100tp", 186),
          ("tm100reg", 187),
          ("ocuseed2p", 188),
          ("oa2x21seed", 189),
          ("oypatchcord", 190),
          ("tpq10gfeci", 191),
          ("tpq10gfecregi", 192),
          ("tphex10gotn", 193),
          ("emxp48iie", 194),
          ("tp100gotn", 195),
          ("emxp220iie", 196),
          ("tpmrHL16G", 197),
          ("fhmxp10g", 198),
          ("mxp100gotn", 199),
          ("cuSfpiii", 200),
          ("emxp240iie", 201),
          ("tpmrHL16GUni", 202),
          ("fpu1", 203),
          ("oaraed21hghyb", 204),
          ("oaraed21hgind", 205),
          ("emxp3", 206),
          ("dcDk652km100", 207),
          ("dcDk652km120", 208),
          ("dcP652km20", 209),
          ("fhau1", 210),
          ("fha1u1", 211),
          ("oa1x20dBmVg2", 212),
          ("oa2x20dBmVg2", 213),
          ("ptio10g", 214),
          ("fxp400gotn", 215),
          ("compo24", 216),
          ("rfu1", 217),
          ("coD919926", 218),
          ("coD927934", 219),
          ("coD935942", 220),
          ("coD943950", 221),
          ("oD951958", 222),
          ("coD919926e", 223),
          ("coD927934e", 224),
          ("coD935942e", 225),
          ("coD943950e", 226),
          ("coD951958e", 227),
          ("co4", 228),
          ("co5", 229),
          ("codsf20eva", 230),
          ("codsf20evb", 231),
          ("codsf4919", 232),
          ("codsf4926", 233),
          ("codsf4927", 234),
          ("codsf4934", 235),
          ("codsf4935", 236),
          ("codsf4942", 237),
          ("codsf4943", 238),
          ("codsf4950", 239),
          ("codsf4951", 240),
          ("codsf4958", 241),
          ("codsf2919", 242),
          ("codsf2922", 243),
          ("codsf2923", 244),
          ("codsf2926", 245),
          ("codsf2927", 246),
          ("codsf2930", 247),
          ("codsf2931", 248),
          ("codsf2934", 249),
          ("codsf2935", 250),
          ("codsf2938", 251),
          ("codsf2939", 252),
          ("codsf2942", 253),
          ("codsf2943", 254),
          ("codsf2946", 255),
          ("codsf2947", 256),
          ("codsf2950", 257),
          ("codsf2951", 258),
          ("codsf2954", 259),
          ("codsf2955", 260),
          ("codsf2958", 261),
          ("tp100gotnii", 262),
          ("roadm1x4f", 263),
          ("ptio100g", 264),
          ("oadm2ch", 265),
          ("emxp1u", 266),
          ("emxp1us", 267),
          ("mxp200gotn", 268),
          ("emxp440", 269),
          ("oaraed20lghyb", 270),
          ("roadm1x9f", 271),
          ("ocm8p", 272),
          ("ad1c2fotdr", 273),
          ("hdea1600", 274),
          ("oa1xLG20dBmb", 275),
          ("oa2xLG20dBmb", 276),
          ("oa1x20dBmVgb", 277),
          ("oa2x20dBmVgb", 278),
          ("codsf24mpo10104", 279),
          ("otdr8p", 280),
          ("coD48ev", 281),
          ("coD48od", 282),
          ("tgCo4", 1001),
          ("tgCo5", 1005),
          ("tgCo6", 1006),
          ("tgCo7", 1007),
          ("tgCo8", 1008),
          ("tgCo9", 1009),
          ("tgCo10", 1010),
          ("tgCo11", 1011),
          ("tgCo12", 1012),
          ("tgCo14", 1014),
          ("tgCo15", 1015),
          ("tgCo16", 1016),
          ("tgCoDxxxyyy", 1040),
          ("tgCoD40ev", 1041),
          ("tgCoD40eve", 1042),
          ("tgCoD40od", 1043),
          ("tgCoD40ode", 1044),
          ("tgCoBSU1x5ev", 1050),
          ("tgCoBSU1x5od", 1051),
          ("tgCad86XX04", 1055),
          ("tgCad86XX02", 1056),
          ("tgCoDSF2ch9XXAB", 1057),
          ("tgCoDSF4ch9XXAB", 1058),
          ("tgCoDSF2ch9XXBA", 1059),
          ("tgCoDSF4ch9XXBA", 1060),
          ("tgTcosf2x1b", 1061),
          ("tgTcosf2x1d", 1062),
          ("tgCoD4XXX", 1070),
          ("tgCoDSF20", 1080),
          ("tgCoDSF20evA", 1081),
          ("tgCoDSF20evB", 1082),
          ("tgCoDSF20odA", 1083),
          ("tgCoDSF20odB", 1084),
          ("tgCoSFBSU1x5ev", 1085),
          ("tgTco12", 2012),
          ("tgTco14", 2014),
          ("acd2pGbE", 10000),
          ("acd5pGbE", 10001),
          ("acd10G", 10002),
          ("edu5GT", 10003),
          ("edu10GLT", 10004),
          ("edu10GLTS", 10005),
          ("nidGE", 20000),
          ("nidSfp155", 20001),
          ("nidSfp622", 20002),
          ("nidSfpVc12", 20003),
          ("nidSfp2488", 20004),
          ("ts1100EthMux4p", 220401),
          ("ts1100OPU", 250101),
          ("ts1100OPUDouble", 250201),
          ("ts1100PreAmpDouble", 260401),
          ("ts1100PreAmp", 261001),
          ("ts1100AttenuatorDouble", 270001),
          ("ts1100UnivAggDGbE", 540001),
          ("ts1100UnivAggDFC", 540002),
          ("ts1100UnivAggDGbE2", 540003),
          ("ts1100UnivAgg", 550000),
          ("ts1100UnivAgg4xGbE", 580000),
          ("ts1100UnivAgg2xGbE2xSTM", 581000),
          ("ts1100Muxponder10G", 590000),
          ("ts1100Nmb", 600100),
          ("ts1100Nmb6003", 600300),
          ("ts1100Tp2x4GFC", 740001),
          ("ts1100Conv1250Cwdm", 750000),
          ("ts1100Conv2500Cwdm", 760000),
          ("ts1100Tp2500Cwdm1", 770000),
          ("ts1100Tp2x2500Cwdm1", 772000),
          ("ts1100Tp10G", 790000),
          ("ts1100Tp10G7910", 791000),
          ("ts1100DuplexerDouble", 802001),
          ("ts1100MuxDemux4chPizza", 803000),
          ("ts1100MuxDemux4chExtPizza", 803100),
          ("ts1100MuxDemux8chPizza", 803200),
          ("ts1100MuxDemux8chExtPizza", 803300),
          ("ts1100Duplexer", 812001),
          ("ts1100MuxDemux4ch1t4", 813001),
          ("ts1100MuxDemux4p1ch1t4", 813101),
          ("ts1100MuxDemux8ch", 813200),
          ("ts1100MuxDemux8p1ch", 813300),
          ("ts1100MuxDemux8ch2", 813400),
          ("ts1100MuxDemux4ch5t8", 814001),
          ("ts1100MuxDemux4p1ch5t8", 814101),
          ("ts1100MuxDemux4chBidir", 823000),
          ("ts1100AddDropDouble", 850100),
          ("ts1100AddDrop", 870101),
          ("ts1100AddDropSingle", 870102),
          ("ts1100DWDMMuxDemuxExt", 883001),
          ("ts1100DWDMMuxDemux", 883101),
          ("ts1100Power9000Supply", 900000),
          ("ts1100Power9048Supply", 904800),
          ("ts1100Power9122Supply", 912200),
          ("ts1100Power9148Supply", 914800),
          ("ts1100Power9220Supply", 922000),
          ("ts1100UnivAgg2xDGbE", 5800002),
          ("ts1100UnivAgg3xGbERep", 5800003),
          ("ts1100UnivAgg3x25GRep", 5800004),
          ("ts1100UnivAgg4xGbE2", 5810002),
          ("ts1100UnivAgg3xGbERep2", 5810003),
          ("ts1100Muxponder10G2", 5900002),
          ("ts1100Tp10G7910Rep", 7910002),
          ("tm206Fan", 9200201),
          ("tm206OSC1", 9221001),
          ("tm206OSC2", 9221002),
          ("tm206TAM4xesc", 9500101),
          ("tm206TAMln4xesc", 9510101),
          ("tm206TAMln4xetr", 9510201),
          ("tm206TAMlnFlex", 9510301),
          ("tm206TAMln2xfc", 9510401),
          ("tm206TAMlnp2xfc", 9510501),
          ("tm206Cu", 9600201),
          ("tm206Cu2", 9600202),
          ("tm206tp2x4gfc", 9780001),
          ("tm206MuxDemux4ch1t4", 9813001),
          ("tm206MuxDemux4p1ch1t4", 9813101),
          ("tm206MuxDemux4ch5t8", 9814001),
          ("tm206MuxDemux4p1ch5t8", 9814101),
          ("tm206MuxDemux4chBidir1", 9823001),
          ("tm206MuxDemux4chBidir2", 9823002),
          ("tm206AddDrop", 9870101))
    )



class FirstPbSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              13)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("slot3", 3),
          ("slot4", 4),
          ("slot13", 13))
    )



# MIB Managed Objects in the order of their OIDs

_LumEquipmentConfs_ObjectIdentity = ObjectIdentity
lumEquipmentConfs = _LumEquipmentConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1)
)
_LumEquipmentGroups_ObjectIdentity = ObjectIdentity
lumEquipmentGroups = _LumEquipmentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1)
)
_LumEquipmentCompl_ObjectIdentity = ObjectIdentity
lumEquipmentCompl = _LumEquipmentCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2)
)
_LumEquipmentMinimalGroups_ObjectIdentity = ObjectIdentity
lumEquipmentMinimalGroups = _LumEquipmentMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 3)
)
_LumEquipmentMinimalCompl_ObjectIdentity = ObjectIdentity
lumEquipmentMinimalCompl = _LumEquipmentMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4)
)
_LumEquipmentMIBObjects_ObjectIdentity = ObjectIdentity
lumEquipmentMIBObjects = _LumEquipmentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2)
)
_EquipmentGeneral_ObjectIdentity = ObjectIdentity
equipmentGeneral = _EquipmentGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1)
)
_EquipmentGeneralTestAndIncr_Type = TestAndIncr
_EquipmentGeneralTestAndIncr_Object = MibScalar
equipmentGeneralTestAndIncr = _EquipmentGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 1),
    _EquipmentGeneralTestAndIncr_Type()
)
equipmentGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentGeneralTestAndIncr.setStatus("current")


class _EquipmentGeneralMibSpecVersion_Type(DisplayString):
    """Custom type equipmentGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_EquipmentGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_EquipmentGeneralMibSpecVersion_Object = MibScalar
equipmentGeneralMibSpecVersion = _EquipmentGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 2),
    _EquipmentGeneralMibSpecVersion_Type()
)
equipmentGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentGeneralMibSpecVersion.setStatus("current")


class _EquipmentGeneralMibImplVersion_Type(DisplayString):
    """Custom type equipmentGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_EquipmentGeneralMibImplVersion_Type.__name__ = "DisplayString"
_EquipmentGeneralMibImplVersion_Object = MibScalar
equipmentGeneralMibImplVersion = _EquipmentGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 3),
    _EquipmentGeneralMibImplVersion_Type()
)
equipmentGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentGeneralMibImplVersion.setStatus("current")
_EquipmentGeneralLastChangeTime_Type = DateAndTime
_EquipmentGeneralLastChangeTime_Object = MibScalar
equipmentGeneralLastChangeTime = _EquipmentGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 4),
    _EquipmentGeneralLastChangeTime_Type()
)
equipmentGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralLastChangeTime.setStatus("current")
_EquipmentGeneralStateLastChangeTime_Type = DateAndTime
_EquipmentGeneralStateLastChangeTime_Object = MibScalar
equipmentGeneralStateLastChangeTime = _EquipmentGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 5),
    _EquipmentGeneralStateLastChangeTime_Type()
)
equipmentGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralStateLastChangeTime.setStatus("current")
_EquipmentGeneralEquipmentSubrackTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentSubrackTableSize_Object = MibScalar
equipmentGeneralEquipmentSubrackTableSize = _EquipmentGeneralEquipmentSubrackTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 6),
    _EquipmentGeneralEquipmentSubrackTableSize_Type()
)
equipmentGeneralEquipmentSubrackTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentSubrackTableSize.setStatus("current")
_EquipmentGeneralEquipmentBoardTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentBoardTableSize_Object = MibScalar
equipmentGeneralEquipmentBoardTableSize = _EquipmentGeneralEquipmentBoardTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 7),
    _EquipmentGeneralEquipmentBoardTableSize_Type()
)
equipmentGeneralEquipmentBoardTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentBoardTableSize.setStatus("current")
_EquipmentGeneralEquipmentPowerTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentPowerTableSize_Object = MibScalar
equipmentGeneralEquipmentPowerTableSize = _EquipmentGeneralEquipmentPowerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 8),
    _EquipmentGeneralEquipmentPowerTableSize_Type()
)
equipmentGeneralEquipmentPowerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentPowerTableSize.setStatus("current")
_EquipmentGeneralEquipmentFanTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentFanTableSize_Object = MibScalar
equipmentGeneralEquipmentFanTableSize = _EquipmentGeneralEquipmentFanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 9),
    _EquipmentGeneralEquipmentFanTableSize_Type()
)
equipmentGeneralEquipmentFanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentFanTableSize.setStatus("current")
_EquipmentGeneralEquipmentSlotTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentSlotTableSize_Object = MibScalar
equipmentGeneralEquipmentSlotTableSize = _EquipmentGeneralEquipmentSlotTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 10),
    _EquipmentGeneralEquipmentSlotTableSize_Type()
)
equipmentGeneralEquipmentSlotTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentSlotTableSize.setStatus("current")
_EquipmentGeneralEquipmentOpticalModuleTableSize_Type = Unsigned32
_EquipmentGeneralEquipmentOpticalModuleTableSize_Object = MibScalar
equipmentGeneralEquipmentOpticalModuleTableSize = _EquipmentGeneralEquipmentOpticalModuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 1, 11),
    _EquipmentGeneralEquipmentOpticalModuleTableSize_Type()
)
equipmentGeneralEquipmentOpticalModuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentGeneralEquipmentOpticalModuleTableSize.setStatus("current")
_EquipmentSubrackList_ObjectIdentity = ObjectIdentity
equipmentSubrackList = _EquipmentSubrackList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2)
)
_EquipmentSubrackTable_Object = MibTable
equipmentSubrackTable = _EquipmentSubrackTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    equipmentSubrackTable.setStatus("current")
_EquipmentSubrackEntry_Object = MibTableRow
equipmentSubrackEntry = _EquipmentSubrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1)
)
equipmentSubrackEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
)
if mibBuilder.loadTexts:
    equipmentSubrackEntry.setStatus("current")


class _EquipmentSubrackIndex_Type(Unsigned32):
    """Custom type equipmentSubrackIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentSubrackIndex_Type.__name__ = "Unsigned32"
_EquipmentSubrackIndex_Object = MibTableColumn
equipmentSubrackIndex = _EquipmentSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 1),
    _EquipmentSubrackIndex_Type()
)
equipmentSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackIndex.setStatus("current")
_EquipmentSubrackName_Type = MgmtNameString
_EquipmentSubrackName_Object = MibTableColumn
equipmentSubrackName = _EquipmentSubrackName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 2),
    _EquipmentSubrackName_Type()
)
equipmentSubrackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackName.setStatus("current")
_EquipmentSubrackSubrack_Type = SubrackNumber
_EquipmentSubrackSubrack_Object = MibTableColumn
equipmentSubrackSubrack = _EquipmentSubrackSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 3),
    _EquipmentSubrackSubrack_Type()
)
equipmentSubrackSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentSubrackSubrack.setStatus("current")


class _EquipmentSubrackDescr_Type(DisplayString):
    """Custom type equipmentSubrackDescr based on DisplayString"""
    defaultValue = OctetString("")


_EquipmentSubrackDescr_Type.__name__ = "DisplayString"
_EquipmentSubrackDescr_Object = MibTableColumn
equipmentSubrackDescr = _EquipmentSubrackDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 4),
    _EquipmentSubrackDescr_Type()
)
equipmentSubrackDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackDescr.setStatus("current")


class _EquipmentSubrackInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type equipmentSubrackInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentSubrackInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_EquipmentSubrackInvPhysIndexOrZero_Object = MibTableColumn
equipmentSubrackInvPhysIndexOrZero = _EquipmentSubrackInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 5),
    _EquipmentSubrackInvPhysIndexOrZero_Type()
)
equipmentSubrackInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackInvPhysIndexOrZero.setStatus("current")
_EquipmentSubrackAllFanUnitsFailed_Type = FaultStatus
_EquipmentSubrackAllFanUnitsFailed_Object = MibTableColumn
equipmentSubrackAllFanUnitsFailed = _EquipmentSubrackAllFanUnitsFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 6),
    _EquipmentSubrackAllFanUnitsFailed_Type()
)
equipmentSubrackAllFanUnitsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackAllFanUnitsFailed.setStatus("current")
_EquipmentSubrackRowStatus_Type = RowStatus
_EquipmentSubrackRowStatus_Object = MibTableColumn
equipmentSubrackRowStatus = _EquipmentSubrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 7),
    _EquipmentSubrackRowStatus_Type()
)
equipmentSubrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentSubrackRowStatus.setStatus("current")


class _EquipmentSubrackExpectedType_Type(EquipmentSubrackType):
    """Custom type equipmentSubrackExpectedType based on EquipmentSubrackType"""
    defaultValue = 0


_EquipmentSubrackExpectedType_Type.__name__ = "EquipmentSubrackType"
_EquipmentSubrackExpectedType_Object = MibTableColumn
equipmentSubrackExpectedType = _EquipmentSubrackExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 8),
    _EquipmentSubrackExpectedType_Type()
)
equipmentSubrackExpectedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackExpectedType.setStatus("current")
_EquipmentSubrackActualType_Type = EquipmentSubrackType
_EquipmentSubrackActualType_Object = MibTableColumn
equipmentSubrackActualType = _EquipmentSubrackActualType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 9),
    _EquipmentSubrackActualType_Type()
)
equipmentSubrackActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackActualType.setStatus("current")
_EquipmentSubrackUnexpectedType_Type = FaultStatus
_EquipmentSubrackUnexpectedType_Object = MibTableColumn
equipmentSubrackUnexpectedType = _EquipmentSubrackUnexpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 10),
    _EquipmentSubrackUnexpectedType_Type()
)
equipmentSubrackUnexpectedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackUnexpectedType.setStatus("current")


class _EquipmentSubrackTemp_Type(Integer32):
    """Custom type equipmentSubrackTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_EquipmentSubrackTemp_Type.__name__ = "Integer32"
_EquipmentSubrackTemp_Object = MibTableColumn
equipmentSubrackTemp = _EquipmentSubrackTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 11),
    _EquipmentSubrackTemp_Type()
)
equipmentSubrackTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackTemp.setStatus("current")
_EquipmentSubrackTempHighExceeded_Type = FaultStatus
_EquipmentSubrackTempHighExceeded_Object = MibTableColumn
equipmentSubrackTempHighExceeded = _EquipmentSubrackTempHighExceeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 12),
    _EquipmentSubrackTempHighExceeded_Type()
)
equipmentSubrackTempHighExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackTempHighExceeded.setStatus("current")


class _EquipmentSubrackTempThreshold_Type(Integer32):
    """Custom type equipmentSubrackTempThreshold based on Integer32"""
    defaultValue = 550

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 800),
    )


_EquipmentSubrackTempThreshold_Type.__name__ = "Integer32"
_EquipmentSubrackTempThreshold_Object = MibTableColumn
equipmentSubrackTempThreshold = _EquipmentSubrackTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 13),
    _EquipmentSubrackTempThreshold_Type()
)
equipmentSubrackTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackTempThreshold.setStatus("current")
_EquipmentSubrackDataChanged_Type = FaultStatus
_EquipmentSubrackDataChanged_Object = MibTableColumn
equipmentSubrackDataChanged = _EquipmentSubrackDataChanged_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 14),
    _EquipmentSubrackDataChanged_Type()
)
equipmentSubrackDataChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackDataChanged.setStatus("current")
_EquipmentSubrackSystemModeSet_Type = FaultStatus
_EquipmentSubrackSystemModeSet_Object = MibTableColumn
equipmentSubrackSystemModeSet = _EquipmentSubrackSystemModeSet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 15),
    _EquipmentSubrackSystemModeSet_Type()
)
equipmentSubrackSystemModeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackSystemModeSet.setStatus("current")


class _EquipmentSubrackEffectiveSystemMode_Type(Unsigned32):
    """Custom type equipmentSubrackEffectiveSystemMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentSubrackEffectiveSystemMode_Type.__name__ = "Unsigned32"
_EquipmentSubrackEffectiveSystemMode_Object = MibTableColumn
equipmentSubrackEffectiveSystemMode = _EquipmentSubrackEffectiveSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 16),
    _EquipmentSubrackEffectiveSystemMode_Type()
)
equipmentSubrackEffectiveSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackEffectiveSystemMode.setStatus("current")


class _EquipmentSubrackCurrentSystemMode_Type(Unsigned32):
    """Custom type equipmentSubrackCurrentSystemMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentSubrackCurrentSystemMode_Type.__name__ = "Unsigned32"
_EquipmentSubrackCurrentSystemMode_Object = MibTableColumn
equipmentSubrackCurrentSystemMode = _EquipmentSubrackCurrentSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 17),
    _EquipmentSubrackCurrentSystemMode_Type()
)
equipmentSubrackCurrentSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackCurrentSystemMode.setStatus("current")


class _EquipmentSubrackAdminStatus_Type(Integer32):
    """Custom type equipmentSubrackAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_EquipmentSubrackAdminStatus_Type.__name__ = "Integer32"
_EquipmentSubrackAdminStatus_Object = MibTableColumn
equipmentSubrackAdminStatus = _EquipmentSubrackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 18),
    _EquipmentSubrackAdminStatus_Type()
)
equipmentSubrackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackAdminStatus.setStatus("current")


class _EquipmentSubrackOperStatus_Type(Integer32):
    """Custom type equipmentSubrackOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_EquipmentSubrackOperStatus_Type.__name__ = "Integer32"
_EquipmentSubrackOperStatus_Object = MibTableColumn
equipmentSubrackOperStatus = _EquipmentSubrackOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 19),
    _EquipmentSubrackOperStatus_Type()
)
equipmentSubrackOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackOperStatus.setStatus("current")
_EquipmentSubrackObjectProperty_Type = ObjectProperty
_EquipmentSubrackObjectProperty_Object = MibTableColumn
equipmentSubrackObjectProperty = _EquipmentSubrackObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 20),
    _EquipmentSubrackObjectProperty_Type()
)
equipmentSubrackObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackObjectProperty.setStatus("current")


class _EquipmentSubrackShelfLength_Type(Unsigned32):
    """Custom type equipmentSubrackShelfLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EquipmentSubrackShelfLength_Type.__name__ = "Unsigned32"
_EquipmentSubrackShelfLength_Object = MibTableColumn
equipmentSubrackShelfLength = _EquipmentSubrackShelfLength_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 21),
    _EquipmentSubrackShelfLength_Type()
)
equipmentSubrackShelfLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackShelfLength.setStatus("current")
_EquipmentSubrackLANModuleMissing_Type = FaultStatus
_EquipmentSubrackLANModuleMissing_Object = MibTableColumn
equipmentSubrackLANModuleMissing = _EquipmentSubrackLANModuleMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 22),
    _EquipmentSubrackLANModuleMissing_Type()
)
equipmentSubrackLANModuleMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackLANModuleMissing.setStatus("current")


class _EquipmentSubrackExpectedFirstPbSlot_Type(FirstPbSlot):
    """Custom type equipmentSubrackExpectedFirstPbSlot based on FirstPbSlot"""
    defaultValue = 0


_EquipmentSubrackExpectedFirstPbSlot_Type.__name__ = "FirstPbSlot"
_EquipmentSubrackExpectedFirstPbSlot_Object = MibTableColumn
equipmentSubrackExpectedFirstPbSlot = _EquipmentSubrackExpectedFirstPbSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 23),
    _EquipmentSubrackExpectedFirstPbSlot_Type()
)
equipmentSubrackExpectedFirstPbSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSubrackExpectedFirstPbSlot.setStatus("current")


class _EquipmentSubrackActualFirstPbSlot_Type(FirstPbSlot):
    """Custom type equipmentSubrackActualFirstPbSlot based on FirstPbSlot"""
    defaultValue = 0


_EquipmentSubrackActualFirstPbSlot_Type.__name__ = "FirstPbSlot"
_EquipmentSubrackActualFirstPbSlot_Object = MibTableColumn
equipmentSubrackActualFirstPbSlot = _EquipmentSubrackActualFirstPbSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 24),
    _EquipmentSubrackActualFirstPbSlot_Type()
)
equipmentSubrackActualFirstPbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackActualFirstPbSlot.setStatus("current")
_EquipmentSubrackFirstPbSlotMismatch_Type = FaultStatus
_EquipmentSubrackFirstPbSlotMismatch_Object = MibTableColumn
equipmentSubrackFirstPbSlotMismatch = _EquipmentSubrackFirstPbSlotMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 25),
    _EquipmentSubrackFirstPbSlotMismatch_Type()
)
equipmentSubrackFirstPbSlotMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackFirstPbSlotMismatch.setStatus("current")
_EquipmentSubrackAid_Type = DisplayString
_EquipmentSubrackAid_Object = MibTableColumn
equipmentSubrackAid = _EquipmentSubrackAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 26),
    _EquipmentSubrackAid_Type()
)
equipmentSubrackAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackAid.setStatus("current")
_EquipmentSubrackPhysicalLocation_Type = DisplayString
_EquipmentSubrackPhysicalLocation_Object = MibTableColumn
equipmentSubrackPhysicalLocation = _EquipmentSubrackPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 27),
    _EquipmentSubrackPhysicalLocation_Type()
)
equipmentSubrackPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackPhysicalLocation.setStatus("current")
_EquipmentSubrackChangeExpectedType_Type = CommandString
_EquipmentSubrackChangeExpectedType_Object = MibTableColumn
equipmentSubrackChangeExpectedType = _EquipmentSubrackChangeExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 2, 1, 1, 28),
    _EquipmentSubrackChangeExpectedType_Type()
)
equipmentSubrackChangeExpectedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSubrackChangeExpectedType.setStatus("current")
_EquipmentBoardList_ObjectIdentity = ObjectIdentity
equipmentBoardList = _EquipmentBoardList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3)
)
_EquipmentBoardTable_Object = MibTable
equipmentBoardTable = _EquipmentBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    equipmentBoardTable.setStatus("current")
_EquipmentBoardEntry_Object = MibTableRow
equipmentBoardEntry = _EquipmentBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1)
)
equipmentBoardEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
)
if mibBuilder.loadTexts:
    equipmentBoardEntry.setStatus("current")


class _EquipmentBoardIndex_Type(Unsigned32):
    """Custom type equipmentBoardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentBoardIndex_Type.__name__ = "Unsigned32"
_EquipmentBoardIndex_Object = MibTableColumn
equipmentBoardIndex = _EquipmentBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 1),
    _EquipmentBoardIndex_Type()
)
equipmentBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardIndex.setStatus("current")
_EquipmentBoardName_Type = MgmtNameString
_EquipmentBoardName_Object = MibTableColumn
equipmentBoardName = _EquipmentBoardName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 2),
    _EquipmentBoardName_Type()
)
equipmentBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardName.setStatus("current")


class _EquipmentBoardExpectedType_Type(EquipmentBoardType):
    """Custom type equipmentBoardExpectedType based on EquipmentBoardType"""
    defaultValue = 0


_EquipmentBoardExpectedType_Type.__name__ = "EquipmentBoardType"
_EquipmentBoardExpectedType_Object = MibTableColumn
equipmentBoardExpectedType = _EquipmentBoardExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 3),
    _EquipmentBoardExpectedType_Type()
)
equipmentBoardExpectedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentBoardExpectedType.setStatus("current")
_EquipmentBoardActualType_Type = EquipmentBoardType
_EquipmentBoardActualType_Object = MibTableColumn
equipmentBoardActualType = _EquipmentBoardActualType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 4),
    _EquipmentBoardActualType_Type()
)
equipmentBoardActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardActualType.setStatus("current")


class _EquipmentBoardDescr_Type(DisplayString):
    """Custom type equipmentBoardDescr based on DisplayString"""
    defaultValue = OctetString("")


_EquipmentBoardDescr_Type.__name__ = "DisplayString"
_EquipmentBoardDescr_Object = MibTableColumn
equipmentBoardDescr = _EquipmentBoardDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 5),
    _EquipmentBoardDescr_Type()
)
equipmentBoardDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardDescr.setStatus("current")


class _EquipmentBoardSubrack_Type(SubrackNumber):
    """Custom type equipmentBoardSubrack based on SubrackNumber"""
    defaultValue = 0


_EquipmentBoardSubrack_Type.__name__ = "SubrackNumber"
_EquipmentBoardSubrack_Object = MibTableColumn
equipmentBoardSubrack = _EquipmentBoardSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 6),
    _EquipmentBoardSubrack_Type()
)
equipmentBoardSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentBoardSubrack.setStatus("current")


class _EquipmentBoardSlot_Type(SlotNumber):
    """Custom type equipmentBoardSlot based on SlotNumber"""
    defaultValue = 0


_EquipmentBoardSlot_Type.__name__ = "SlotNumber"
_EquipmentBoardSlot_Object = MibTableColumn
equipmentBoardSlot = _EquipmentBoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 7),
    _EquipmentBoardSlot_Type()
)
equipmentBoardSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentBoardSlot.setStatus("current")


class _EquipmentBoardTemp_Type(Integer32):
    """Custom type equipmentBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_EquipmentBoardTemp_Type.__name__ = "Integer32"
_EquipmentBoardTemp_Object = MibTableColumn
equipmentBoardTemp = _EquipmentBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 8),
    _EquipmentBoardTemp_Type()
)
equipmentBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardTemp.setStatus("current")


class _EquipmentBoardInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type equipmentBoardInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentBoardInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_EquipmentBoardInvPhysIndexOrZero_Object = MibTableColumn
equipmentBoardInvPhysIndexOrZero = _EquipmentBoardInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 9),
    _EquipmentBoardInvPhysIndexOrZero_Type()
)
equipmentBoardInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardInvPhysIndexOrZero.setStatus("current")


class _EquipmentBoardLedTest_Type(Integer32):
    """Custom type equipmentBoardLedTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EquipmentBoardLedTest_Type.__name__ = "Integer32"
_EquipmentBoardLedTest_Object = MibTableColumn
equipmentBoardLedTest = _EquipmentBoardLedTest_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 10),
    _EquipmentBoardLedTest_Type()
)
equipmentBoardLedTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardLedTest.setStatus("current")


class _EquipmentBoardAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type equipmentBoardAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_EquipmentBoardAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_EquipmentBoardAdminStatus_Object = MibTableColumn
equipmentBoardAdminStatus = _EquipmentBoardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 11),
    _EquipmentBoardAdminStatus_Type()
)
equipmentBoardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardAdminStatus.setStatus("current")


class _EquipmentBoardOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type equipmentBoardOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_EquipmentBoardOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_EquipmentBoardOperStatus_Object = MibTableColumn
equipmentBoardOperStatus = _EquipmentBoardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 12),
    _EquipmentBoardOperStatus_Type()
)
equipmentBoardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardOperStatus.setStatus("current")
_EquipmentBoardLastChangeTime_Type = DateAndTime
_EquipmentBoardLastChangeTime_Object = MibTableColumn
equipmentBoardLastChangeTime = _EquipmentBoardLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 13),
    _EquipmentBoardLastChangeTime_Type()
)
equipmentBoardLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardLastChangeTime.setStatus("current")
_EquipmentBoardRowStatus_Type = RowStatus
_EquipmentBoardRowStatus_Object = MibTableColumn
equipmentBoardRowStatus = _EquipmentBoardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 14),
    _EquipmentBoardRowStatus_Type()
)
equipmentBoardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentBoardRowStatus.setStatus("current")
_EquipmentBoardMissing_Type = FaultStatus
_EquipmentBoardMissing_Object = MibTableColumn
equipmentBoardMissing = _EquipmentBoardMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 15),
    _EquipmentBoardMissing_Type()
)
equipmentBoardMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardMissing.setStatus("current")
_EquipmentBoardUnexpectedType_Type = FaultStatus
_EquipmentBoardUnexpectedType_Object = MibTableColumn
equipmentBoardUnexpectedType = _EquipmentBoardUnexpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 16),
    _EquipmentBoardUnexpectedType_Type()
)
equipmentBoardUnexpectedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardUnexpectedType.setStatus("current")
_EquipmentBoardTempHighExceeded_Type = FaultStatus
_EquipmentBoardTempHighExceeded_Object = MibTableColumn
equipmentBoardTempHighExceeded = _EquipmentBoardTempHighExceeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 17),
    _EquipmentBoardTempHighExceeded_Type()
)
equipmentBoardTempHighExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardTempHighExceeded.setStatus("current")
_EquipmentBoardCommunicationFailure_Type = FaultStatus
_EquipmentBoardCommunicationFailure_Object = MibTableColumn
equipmentBoardCommunicationFailure = _EquipmentBoardCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 18),
    _EquipmentBoardCommunicationFailure_Type()
)
equipmentBoardCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardCommunicationFailure.setStatus("current")
_EquipmentBoardInterworkFailed_Type = FaultStatus
_EquipmentBoardInterworkFailed_Object = MibTableColumn
equipmentBoardInterworkFailed = _EquipmentBoardInterworkFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 19),
    _EquipmentBoardInterworkFailed_Type()
)
equipmentBoardInterworkFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardInterworkFailed.setStatus("current")
_EquipmentBoardSecondaryPowerFailed_Type = FaultStatus
_EquipmentBoardSecondaryPowerFailed_Object = MibTableColumn
equipmentBoardSecondaryPowerFailed = _EquipmentBoardSecondaryPowerFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 20),
    _EquipmentBoardSecondaryPowerFailed_Type()
)
equipmentBoardSecondaryPowerFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardSecondaryPowerFailed.setStatus("current")
_EquipmentBoardVitalDataMissing_Type = FaultStatus
_EquipmentBoardVitalDataMissing_Object = MibTableColumn
equipmentBoardVitalDataMissing = _EquipmentBoardVitalDataMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 21),
    _EquipmentBoardVitalDataMissing_Type()
)
equipmentBoardVitalDataMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardVitalDataMissing.setStatus("current")
_EquipmentBoardNonVitalDataMissing_Type = FaultStatus
_EquipmentBoardNonVitalDataMissing_Object = MibTableColumn
equipmentBoardNonVitalDataMissing = _EquipmentBoardNonVitalDataMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 22),
    _EquipmentBoardNonVitalDataMissing_Type()
)
equipmentBoardNonVitalDataMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardNonVitalDataMissing.setStatus("current")
_EquipmentBoardUnderMaintenance_Type = FaultStatus
_EquipmentBoardUnderMaintenance_Object = MibTableColumn
equipmentBoardUnderMaintenance = _EquipmentBoardUnderMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 23),
    _EquipmentBoardUnderMaintenance_Type()
)
equipmentBoardUnderMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardUnderMaintenance.setStatus("current")


class _EquipmentBoardTempThreshold_Type(Integer32):
    """Custom type equipmentBoardTempThreshold based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800),
    )


_EquipmentBoardTempThreshold_Type.__name__ = "Integer32"
_EquipmentBoardTempThreshold_Object = MibTableColumn
equipmentBoardTempThreshold = _EquipmentBoardTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 24),
    _EquipmentBoardTempThreshold_Type()
)
equipmentBoardTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardTempThreshold.setStatus("current")
_EquipmentBoardSwVersionMismatch_Type = FaultStatus
_EquipmentBoardSwVersionMismatch_Object = MibTableColumn
equipmentBoardSwVersionMismatch = _EquipmentBoardSwVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 25),
    _EquipmentBoardSwVersionMismatch_Type()
)
equipmentBoardSwVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardSwVersionMismatch.setStatus("current")
_EquipmentBoardObjectProperty_Type = ObjectProperty
_EquipmentBoardObjectProperty_Object = MibTableColumn
equipmentBoardObjectProperty = _EquipmentBoardObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 26),
    _EquipmentBoardObjectProperty_Type()
)
equipmentBoardObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardObjectProperty.setStatus("current")
_EquipmentBoardTempLow_Type = FaultStatus
_EquipmentBoardTempLow_Object = MibTableColumn
equipmentBoardTempLow = _EquipmentBoardTempLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 27),
    _EquipmentBoardTempLow_Type()
)
equipmentBoardTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardTempLow.setStatus("current")
_EquipmentBoardTempVeryHigh_Type = FaultStatus
_EquipmentBoardTempVeryHigh_Object = MibTableColumn
equipmentBoardTempVeryHigh = _EquipmentBoardTempVeryHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 28),
    _EquipmentBoardTempVeryHigh_Type()
)
equipmentBoardTempVeryHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardTempVeryHigh.setStatus("current")
_EquipmentBoardReconfigure_Type = CommandString
_EquipmentBoardReconfigure_Object = MibTableColumn
equipmentBoardReconfigure = _EquipmentBoardReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 29),
    _EquipmentBoardReconfigure_Type()
)
equipmentBoardReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardReconfigure.setStatus("current")


class _EquipmentBoardLedStatus_Type(Integer32):
    """Custom type equipmentBoardLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("minor", 2),
          ("major", 3))
    )


_EquipmentBoardLedStatus_Type.__name__ = "Integer32"
_EquipmentBoardLedStatus_Object = MibTableColumn
equipmentBoardLedStatus = _EquipmentBoardLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 30),
    _EquipmentBoardLedStatus_Type()
)
equipmentBoardLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardLedStatus.setStatus("current")
_EquipmentBoardModuleInfo_Type = DisplayString
_EquipmentBoardModuleInfo_Object = MibTableColumn
equipmentBoardModuleInfo = _EquipmentBoardModuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 31),
    _EquipmentBoardModuleInfo_Type()
)
equipmentBoardModuleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardModuleInfo.setStatus("current")
_EquipmentBoardNewSwActivatedButNotRestarted_Type = FaultStatus
_EquipmentBoardNewSwActivatedButNotRestarted_Object = MibTableColumn
equipmentBoardNewSwActivatedButNotRestarted = _EquipmentBoardNewSwActivatedButNotRestarted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 32),
    _EquipmentBoardNewSwActivatedButNotRestarted_Type()
)
equipmentBoardNewSwActivatedButNotRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardNewSwActivatedButNotRestarted.setStatus("current")
_EquipmentBoardLowTemperature_Type = FaultStatus
_EquipmentBoardLowTemperature_Object = MibTableColumn
equipmentBoardLowTemperature = _EquipmentBoardLowTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 33),
    _EquipmentBoardLowTemperature_Type()
)
equipmentBoardLowTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardLowTemperature.setStatus("current")


class _EquipmentBoardTempLowThreshold_Type(Integer32):
    """Custom type equipmentBoardTempLowThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 400),
    )


_EquipmentBoardTempLowThreshold_Type.__name__ = "Integer32"
_EquipmentBoardTempLowThreshold_Object = MibTableColumn
equipmentBoardTempLowThreshold = _EquipmentBoardTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 34),
    _EquipmentBoardTempLowThreshold_Type()
)
equipmentBoardTempLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardTempLowThreshold.setStatus("current")


class _EquipmentBoardAdditionalInfo_Type(DisplayString):
    """Custom type equipmentBoardAdditionalInfo based on DisplayString"""
    defaultValue = OctetString("")


_EquipmentBoardAdditionalInfo_Type.__name__ = "DisplayString"
_EquipmentBoardAdditionalInfo_Object = MibTableColumn
equipmentBoardAdditionalInfo = _EquipmentBoardAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 35),
    _EquipmentBoardAdditionalInfo_Type()
)
equipmentBoardAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardAdditionalInfo.setStatus("current")
_EquipmentBoardBootError_Type = FaultStatus
_EquipmentBoardBootError_Object = MibTableColumn
equipmentBoardBootError = _EquipmentBoardBootError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 36),
    _EquipmentBoardBootError_Type()
)
equipmentBoardBootError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardBootError.setStatus("current")
_EquipmentBoardHardwareError_Type = FaultStatus
_EquipmentBoardHardwareError_Object = MibTableColumn
equipmentBoardHardwareError = _EquipmentBoardHardwareError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 37),
    _EquipmentBoardHardwareError_Type()
)
equipmentBoardHardwareError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardHardwareError.setStatus("current")
_EquipmentBoardLowDiskSpace_Type = FaultStatus
_EquipmentBoardLowDiskSpace_Object = MibTableColumn
equipmentBoardLowDiskSpace = _EquipmentBoardLowDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 38),
    _EquipmentBoardLowDiskSpace_Type()
)
equipmentBoardLowDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardLowDiskSpace.setStatus("current")
_EquipmentBoardClockDrift_Type = FaultStatus
_EquipmentBoardClockDrift_Object = MibTableColumn
equipmentBoardClockDrift = _EquipmentBoardClockDrift_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 39),
    _EquipmentBoardClockDrift_Type()
)
equipmentBoardClockDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardClockDrift.setStatus("current")


class _EquipmentBoardPostponeFwUpgrade_Type(Integer32):
    """Custom type equipmentBoardPostponeFwUpgrade based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentBoardPostponeFwUpgrade_Type.__name__ = "Integer32"
_EquipmentBoardPostponeFwUpgrade_Object = MibTableColumn
equipmentBoardPostponeFwUpgrade = _EquipmentBoardPostponeFwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 40),
    _EquipmentBoardPostponeFwUpgrade_Type()
)
equipmentBoardPostponeFwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardPostponeFwUpgrade.setStatus("current")
_EquipmentBoardActivatePendingFwCommand_Type = CommandString
_EquipmentBoardActivatePendingFwCommand_Object = MibTableColumn
equipmentBoardActivatePendingFwCommand = _EquipmentBoardActivatePendingFwCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 41),
    _EquipmentBoardActivatePendingFwCommand_Type()
)
equipmentBoardActivatePendingFwCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardActivatePendingFwCommand.setStatus("current")
_EquipmentBoardFwActivationPending_Type = FaultStatus
_EquipmentBoardFwActivationPending_Object = MibTableColumn
equipmentBoardFwActivationPending = _EquipmentBoardFwActivationPending_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 42),
    _EquipmentBoardFwActivationPending_Type()
)
equipmentBoardFwActivationPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardFwActivationPending.setStatus("current")
_EquipmentBoardFeatureNotSupported_Type = FaultStatus
_EquipmentBoardFeatureNotSupported_Object = MibTableColumn
equipmentBoardFeatureNotSupported = _EquipmentBoardFeatureNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 43),
    _EquipmentBoardFeatureNotSupported_Type()
)
equipmentBoardFeatureNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardFeatureNotSupported.setStatus("current")
_EquipmentBoardFwReloadNeeded_Type = FaultStatus
_EquipmentBoardFwReloadNeeded_Object = MibTableColumn
equipmentBoardFwReloadNeeded = _EquipmentBoardFwReloadNeeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 44),
    _EquipmentBoardFwReloadNeeded_Type()
)
equipmentBoardFwReloadNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardFwReloadNeeded.setStatus("current")
_EquipmentBoardFwContextUnknown_Type = FaultStatus
_EquipmentBoardFwContextUnknown_Object = MibTableColumn
equipmentBoardFwContextUnknown = _EquipmentBoardFwContextUnknown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 45),
    _EquipmentBoardFwContextUnknown_Type()
)
equipmentBoardFwContextUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardFwContextUnknown.setStatus("current")


class _EquipmentBoardBoardVariant_Type(Integer32):
    """Custom type equipmentBoardBoardVariant based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("dualMuxponderProt", 1),
          ("hexTransponder", 2),
          ("tripleMuxponderProt", 3),
          ("quadTransponderProt", 4),
          ("notApplicable", 2147483647))
    )


_EquipmentBoardBoardVariant_Type.__name__ = "Integer32"
_EquipmentBoardBoardVariant_Object = MibTableColumn
equipmentBoardBoardVariant = _EquipmentBoardBoardVariant_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 46),
    _EquipmentBoardBoardVariant_Type()
)
equipmentBoardBoardVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardBoardVariant.setStatus("current")


class _EquipmentBoardCabinetConnectivity_Type(Integer32):
    """Custom type equipmentBoardCabinetConnectivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentBoardCabinetConnectivity_Type.__name__ = "Integer32"
_EquipmentBoardCabinetConnectivity_Object = MibTableColumn
equipmentBoardCabinetConnectivity = _EquipmentBoardCabinetConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 47),
    _EquipmentBoardCabinetConnectivity_Type()
)
equipmentBoardCabinetConnectivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentBoardCabinetConnectivity.setStatus("current")
_EquipmentBoardCabinetConnectionFailure_Type = FaultStatus
_EquipmentBoardCabinetConnectionFailure_Object = MibTableColumn
equipmentBoardCabinetConnectionFailure = _EquipmentBoardCabinetConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 48),
    _EquipmentBoardCabinetConnectionFailure_Type()
)
equipmentBoardCabinetConnectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardCabinetConnectionFailure.setStatus("current")


class _EquipmentBoardOperationalVariant_Type(Integer32):
    """Custom type equipmentBoardOperationalVariant based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("openFlowControlled", 2))
    )


_EquipmentBoardOperationalVariant_Type.__name__ = "Integer32"
_EquipmentBoardOperationalVariant_Object = MibTableColumn
equipmentBoardOperationalVariant = _EquipmentBoardOperationalVariant_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 49),
    _EquipmentBoardOperationalVariant_Type()
)
equipmentBoardOperationalVariant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    equipmentBoardOperationalVariant.setStatus("current")
_EquipmentBoardAid_Type = DisplayString
_EquipmentBoardAid_Object = MibTableColumn
equipmentBoardAid = _EquipmentBoardAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 50),
    _EquipmentBoardAid_Type()
)
equipmentBoardAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardAid.setStatus("current")
_EquipmentBoardPhysicalLocation_Type = DisplayString
_EquipmentBoardPhysicalLocation_Object = MibTableColumn
equipmentBoardPhysicalLocation = _EquipmentBoardPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 3, 1, 1, 51),
    _EquipmentBoardPhysicalLocation_Type()
)
equipmentBoardPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentBoardPhysicalLocation.setStatus("current")
_EquipmentPowerList_ObjectIdentity = ObjectIdentity
equipmentPowerList = _EquipmentPowerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4)
)
_EquipmentPowerTable_Object = MibTable
equipmentPowerTable = _EquipmentPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1)
)
if mibBuilder.loadTexts:
    equipmentPowerTable.setStatus("current")
_EquipmentPowerEntry_Object = MibTableRow
equipmentPowerEntry = _EquipmentPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1)
)
equipmentPowerEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentPowerIndex"),
)
if mibBuilder.loadTexts:
    equipmentPowerEntry.setStatus("current")


class _EquipmentPowerIndex_Type(Unsigned32):
    """Custom type equipmentPowerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentPowerIndex_Type.__name__ = "Unsigned32"
_EquipmentPowerIndex_Object = MibTableColumn
equipmentPowerIndex = _EquipmentPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 1),
    _EquipmentPowerIndex_Type()
)
equipmentPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerIndex.setStatus("current")


class _EquipmentPowerName_Type(DisplayString):
    """Custom type equipmentPowerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EquipmentPowerName_Type.__name__ = "DisplayString"
_EquipmentPowerName_Object = MibTableColumn
equipmentPowerName = _EquipmentPowerName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 2),
    _EquipmentPowerName_Type()
)
equipmentPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerName.setStatus("current")
_EquipmentPowerSubrack_Type = SubrackNumber
_EquipmentPowerSubrack_Object = MibTableColumn
equipmentPowerSubrack = _EquipmentPowerSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 3),
    _EquipmentPowerSubrack_Type()
)
equipmentPowerSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerSubrack.setStatus("current")


class _EquipmentPowerSlot_Type(Unsigned32):
    """Custom type equipmentPowerSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EquipmentPowerSlot_Type.__name__ = "Unsigned32"
_EquipmentPowerSlot_Object = MibTableColumn
equipmentPowerSlot = _EquipmentPowerSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 4),
    _EquipmentPowerSlot_Type()
)
equipmentPowerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerSlot.setStatus("current")


class _EquipmentPowerType_Type(Integer32):
    """Custom type equipmentPowerType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ac", 1),
          ("dc", 2))
    )


_EquipmentPowerType_Type.__name__ = "Integer32"
_EquipmentPowerType_Object = MibTableColumn
equipmentPowerType = _EquipmentPowerType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 5),
    _EquipmentPowerType_Type()
)
equipmentPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerType.setStatus("current")


class _EquipmentPowerInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type equipmentPowerInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentPowerInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_EquipmentPowerInvPhysIndexOrZero_Object = MibTableColumn
equipmentPowerInvPhysIndexOrZero = _EquipmentPowerInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 9),
    _EquipmentPowerInvPhysIndexOrZero_Type()
)
equipmentPowerInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerInvPhysIndexOrZero.setStatus("current")


class _EquipmentPowerAdminStatus_Type(Integer32):
    """Custom type equipmentPowerAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_EquipmentPowerAdminStatus_Type.__name__ = "Integer32"
_EquipmentPowerAdminStatus_Object = MibTableColumn
equipmentPowerAdminStatus = _EquipmentPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 10),
    _EquipmentPowerAdminStatus_Type()
)
equipmentPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentPowerAdminStatus.setStatus("current")


class _EquipmentPowerOperStatus_Type(Integer32):
    """Custom type equipmentPowerOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_EquipmentPowerOperStatus_Type.__name__ = "Integer32"
_EquipmentPowerOperStatus_Object = MibTableColumn
equipmentPowerOperStatus = _EquipmentPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 11),
    _EquipmentPowerOperStatus_Type()
)
equipmentPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerOperStatus.setStatus("current")
_EquipmentPowerRowStatus_Type = RowStatus
_EquipmentPowerRowStatus_Object = MibTableColumn
equipmentPowerRowStatus = _EquipmentPowerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 12),
    _EquipmentPowerRowStatus_Type()
)
equipmentPowerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentPowerRowStatus.setStatus("current")
_EquipmentPowerACPowerFailed_Type = FaultStatus
_EquipmentPowerACPowerFailed_Object = MibTableColumn
equipmentPowerACPowerFailed = _EquipmentPowerACPowerFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 13),
    _EquipmentPowerACPowerFailed_Type()
)
equipmentPowerACPowerFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerACPowerFailed.setStatus("current")
_EquipmentPowerDCPowerFailed_Type = FaultStatus
_EquipmentPowerDCPowerFailed_Object = MibTableColumn
equipmentPowerDCPowerFailed = _EquipmentPowerDCPowerFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 14),
    _EquipmentPowerDCPowerFailed_Type()
)
equipmentPowerDCPowerFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerDCPowerFailed.setStatus("current")
_EquipmentPowerTemperatureHigh_Type = FaultStatus
_EquipmentPowerTemperatureHigh_Object = MibTableColumn
equipmentPowerTemperatureHigh = _EquipmentPowerTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 15),
    _EquipmentPowerTemperatureHigh_Type()
)
equipmentPowerTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerTemperatureHigh.setStatus("current")
_EquipmentPowerModuleMissing_Type = FaultStatus
_EquipmentPowerModuleMissing_Object = MibTableColumn
equipmentPowerModuleMissing = _EquipmentPowerModuleMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 16),
    _EquipmentPowerModuleMissing_Type()
)
equipmentPowerModuleMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerModuleMissing.setStatus("current")
_EquipmentPowerObjectProperty_Type = ObjectProperty
_EquipmentPowerObjectProperty_Object = MibTableColumn
equipmentPowerObjectProperty = _EquipmentPowerObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 17),
    _EquipmentPowerObjectProperty_Type()
)
equipmentPowerObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerObjectProperty.setStatus("current")


class _EquipmentPowerDCPowerFailedSeverity_Type(AlarmPerceivedSeverity):
    """Custom type equipmentPowerDCPowerFailedSeverity based on AlarmPerceivedSeverity"""
    defaultValue = 4


_EquipmentPowerDCPowerFailedSeverity_Type.__name__ = "AlarmPerceivedSeverity"
_EquipmentPowerDCPowerFailedSeverity_Object = MibTableColumn
equipmentPowerDCPowerFailedSeverity = _EquipmentPowerDCPowerFailedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 18),
    _EquipmentPowerDCPowerFailedSeverity_Type()
)
equipmentPowerDCPowerFailedSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentPowerDCPowerFailedSeverity.setStatus("current")
_EquipmentPowerAid_Type = DisplayString
_EquipmentPowerAid_Object = MibTableColumn
equipmentPowerAid = _EquipmentPowerAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 19),
    _EquipmentPowerAid_Type()
)
equipmentPowerAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerAid.setStatus("current")
_EquipmentPowerPhysicalLocation_Type = DisplayString
_EquipmentPowerPhysicalLocation_Object = MibTableColumn
equipmentPowerPhysicalLocation = _EquipmentPowerPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 4, 1, 1, 20),
    _EquipmentPowerPhysicalLocation_Type()
)
equipmentPowerPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentPowerPhysicalLocation.setStatus("current")
_EquipmentFanList_ObjectIdentity = ObjectIdentity
equipmentFanList = _EquipmentFanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5)
)
_EquipmentFanTable_Object = MibTable
equipmentFanTable = _EquipmentFanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1)
)
if mibBuilder.loadTexts:
    equipmentFanTable.setStatus("current")
_EquipmentFanEntry_Object = MibTableRow
equipmentFanEntry = _EquipmentFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1)
)
equipmentFanEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
)
if mibBuilder.loadTexts:
    equipmentFanEntry.setStatus("current")


class _EquipmentFanIndex_Type(Unsigned32):
    """Custom type equipmentFanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentFanIndex_Type.__name__ = "Unsigned32"
_EquipmentFanIndex_Object = MibTableColumn
equipmentFanIndex = _EquipmentFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 1),
    _EquipmentFanIndex_Type()
)
equipmentFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanIndex.setStatus("current")


class _EquipmentFanName_Type(DisplayString):
    """Custom type equipmentFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EquipmentFanName_Type.__name__ = "DisplayString"
_EquipmentFanName_Object = MibTableColumn
equipmentFanName = _EquipmentFanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 2),
    _EquipmentFanName_Type()
)
equipmentFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanName.setStatus("current")
_EquipmentFanSubrack_Type = SubrackNumber
_EquipmentFanSubrack_Object = MibTableColumn
equipmentFanSubrack = _EquipmentFanSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 3),
    _EquipmentFanSubrack_Type()
)
equipmentFanSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanSubrack.setStatus("current")


class _EquipmentFanSlot_Type(Unsigned32):
    """Custom type equipmentFanSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EquipmentFanSlot_Type.__name__ = "Unsigned32"
_EquipmentFanSlot_Object = MibTableColumn
equipmentFanSlot = _EquipmentFanSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 4),
    _EquipmentFanSlot_Type()
)
equipmentFanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanSlot.setStatus("current")


class _EquipmentFanInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type equipmentFanInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EquipmentFanInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_EquipmentFanInvPhysIndexOrZero_Object = MibTableColumn
equipmentFanInvPhysIndexOrZero = _EquipmentFanInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 5),
    _EquipmentFanInvPhysIndexOrZero_Type()
)
equipmentFanInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanInvPhysIndexOrZero.setStatus("current")


class _EquipmentFanAdminStatus_Type(Integer32):
    """Custom type equipmentFanAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_EquipmentFanAdminStatus_Type.__name__ = "Integer32"
_EquipmentFanAdminStatus_Object = MibTableColumn
equipmentFanAdminStatus = _EquipmentFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 6),
    _EquipmentFanAdminStatus_Type()
)
equipmentFanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentFanAdminStatus.setStatus("current")


class _EquipmentFanOperStatus_Type(Integer32):
    """Custom type equipmentFanOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_EquipmentFanOperStatus_Type.__name__ = "Integer32"
_EquipmentFanOperStatus_Object = MibTableColumn
equipmentFanOperStatus = _EquipmentFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 7),
    _EquipmentFanOperStatus_Type()
)
equipmentFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanOperStatus.setStatus("current")
_EquipmentFanRowStatus_Type = RowStatus
_EquipmentFanRowStatus_Object = MibTableColumn
equipmentFanRowStatus = _EquipmentFanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 8),
    _EquipmentFanRowStatus_Type()
)
equipmentFanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentFanRowStatus.setStatus("current")
_EquipmentFanUnitFailed_Type = FaultStatus
_EquipmentFanUnitFailed_Object = MibTableColumn
equipmentFanUnitFailed = _EquipmentFanUnitFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 9),
    _EquipmentFanUnitFailed_Type()
)
equipmentFanUnitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanUnitFailed.setStatus("current")
_EquipmentFanMainUnitFailed_Type = FaultStatus
_EquipmentFanMainUnitFailed_Object = MibTableColumn
equipmentFanMainUnitFailed = _EquipmentFanMainUnitFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 10),
    _EquipmentFanMainUnitFailed_Type()
)
equipmentFanMainUnitFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanMainUnitFailed.setStatus("current")
_EquipmentFanObjectProperty_Type = ObjectProperty
_EquipmentFanObjectProperty_Object = MibTableColumn
equipmentFanObjectProperty = _EquipmentFanObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 11),
    _EquipmentFanObjectProperty_Type()
)
equipmentFanObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanObjectProperty.setStatus("current")
_EquipmentFanFanFault_Type = FaultStatus
_EquipmentFanFanFault_Object = MibTableColumn
equipmentFanFanFault = _EquipmentFanFanFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 12),
    _EquipmentFanFanFault_Type()
)
equipmentFanFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanFanFault.setStatus("current")
_EquipmentFanAid_Type = DisplayString
_EquipmentFanAid_Object = MibTableColumn
equipmentFanAid = _EquipmentFanAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 13),
    _EquipmentFanAid_Type()
)
equipmentFanAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanAid.setStatus("current")
_EquipmentFanPhysicalLocation_Type = DisplayString
_EquipmentFanPhysicalLocation_Object = MibTableColumn
equipmentFanPhysicalLocation = _EquipmentFanPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 5, 1, 1, 14),
    _EquipmentFanPhysicalLocation_Type()
)
equipmentFanPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentFanPhysicalLocation.setStatus("current")
_LumentisEquipmentNotifications_ObjectIdentity = ObjectIdentity
lumentisEquipmentNotifications = _LumentisEquipmentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6)
)
_EquipmentNotifyPrefix_ObjectIdentity = ObjectIdentity
equipmentNotifyPrefix = _EquipmentNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0)
)
_EquipmentNode_ObjectIdentity = ObjectIdentity
equipmentNode = _EquipmentNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7)
)


class _EquipmentNodeLedTest_Type(Integer32):
    """Custom type equipmentNodeLedTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EquipmentNodeLedTest_Type.__name__ = "Integer32"
_EquipmentNodeLedTest_Object = MibScalar
equipmentNodeLedTest = _EquipmentNodeLedTest_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 1),
    _EquipmentNodeLedTest_Type()
)
equipmentNodeLedTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeLedTest.setStatus("current")


class _EquipmentNodeIcnRedundancyMode_Type(Integer32):
    """Custom type equipmentNodeIcnRedundancyMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("ring", 3))
    )


_EquipmentNodeIcnRedundancyMode_Type.__name__ = "Integer32"
_EquipmentNodeIcnRedundancyMode_Object = MibScalar
equipmentNodeIcnRedundancyMode = _EquipmentNodeIcnRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 2),
    _EquipmentNodeIcnRedundancyMode_Type()
)
equipmentNodeIcnRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeIcnRedundancyMode.setStatus("current")


class _EquipmentNodeMemoryProfile_Type(Integer32):
    """Custom type equipmentNodeMemoryProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentNodeMemoryProfile_Type.__name__ = "Integer32"
_EquipmentNodeMemoryProfile_Object = MibScalar
equipmentNodeMemoryProfile = _EquipmentNodeMemoryProfile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 3),
    _EquipmentNodeMemoryProfile_Type()
)
equipmentNodeMemoryProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentNodeMemoryProfile.setStatus("current")


class _EquipmentAllowDummyPassiveSlots_Type(Integer32):
    """Custom type equipmentAllowDummyPassiveSlots based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentAllowDummyPassiveSlots_Type.__name__ = "Integer32"
_EquipmentAllowDummyPassiveSlots_Object = MibScalar
equipmentAllowDummyPassiveSlots = _EquipmentAllowDummyPassiveSlots_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 4),
    _EquipmentAllowDummyPassiveSlots_Type()
)
equipmentAllowDummyPassiveSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentAllowDummyPassiveSlots.setStatus("current")


class _EquipmentNodeManagementVlan_Type(Integer32):
    """Custom type equipmentNodeManagementVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("bridge2dcn", 2),
          ("on", 3))
    )


_EquipmentNodeManagementVlan_Type.__name__ = "Integer32"
_EquipmentNodeManagementVlan_Object = MibScalar
equipmentNodeManagementVlan = _EquipmentNodeManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 5),
    _EquipmentNodeManagementVlan_Type()
)
equipmentNodeManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeManagementVlan.setStatus("current")


class _EquipmentNodeMgmtVlanPrivacy_Type(Integer32):
    """Custom type equipmentNodeMgmtVlanPrivacy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 1),
          ("community", 2))
    )


_EquipmentNodeMgmtVlanPrivacy_Type.__name__ = "Integer32"
_EquipmentNodeMgmtVlanPrivacy_Object = MibScalar
equipmentNodeMgmtVlanPrivacy = _EquipmentNodeMgmtVlanPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 6),
    _EquipmentNodeMgmtVlanPrivacy_Type()
)
equipmentNodeMgmtVlanPrivacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeMgmtVlanPrivacy.setStatus("current")


class _EquipmentNodeDcnRedundancyMode_Type(Integer32):
    """Custom type equipmentNodeDcnRedundancyMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentNodeDcnRedundancyMode_Type.__name__ = "Integer32"
_EquipmentNodeDcnRedundancyMode_Object = MibScalar
equipmentNodeDcnRedundancyMode = _EquipmentNodeDcnRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 7),
    _EquipmentNodeDcnRedundancyMode_Type()
)
equipmentNodeDcnRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeDcnRedundancyMode.setStatus("current")


class _EquipmentNodeProxyArp_Type(Integer32):
    """Custom type equipmentNodeProxyArp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EquipmentNodeProxyArp_Type.__name__ = "Integer32"
_EquipmentNodeProxyArp_Object = MibScalar
equipmentNodeProxyArp = _EquipmentNodeProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 7, 8),
    _EquipmentNodeProxyArp_Type()
)
equipmentNodeProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentNodeProxyArp.setStatus("current")
_EquipmentResource_ObjectIdentity = ObjectIdentity
equipmentResource = _EquipmentResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 8)
)
_EquipmentResourceNumberOfBoards_Type = Unsigned32
_EquipmentResourceNumberOfBoards_Object = MibScalar
equipmentResourceNumberOfBoards = _EquipmentResourceNumberOfBoards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 8, 1),
    _EquipmentResourceNumberOfBoards_Type()
)
equipmentResourceNumberOfBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentResourceNumberOfBoards.setStatus("current")
_EquipmentResourceMaxNumberOfBoards_Type = Unsigned32
_EquipmentResourceMaxNumberOfBoards_Object = MibScalar
equipmentResourceMaxNumberOfBoards = _EquipmentResourceMaxNumberOfBoards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 8, 2),
    _EquipmentResourceMaxNumberOfBoards_Type()
)
equipmentResourceMaxNumberOfBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentResourceMaxNumberOfBoards.setStatus("current")
_EquipmentResourceNumberOfActiveBoards_Type = Unsigned32
_EquipmentResourceNumberOfActiveBoards_Object = MibScalar
equipmentResourceNumberOfActiveBoards = _EquipmentResourceNumberOfActiveBoards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 8, 3),
    _EquipmentResourceNumberOfActiveBoards_Type()
)
equipmentResourceNumberOfActiveBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentResourceNumberOfActiveBoards.setStatus("current")
_EquipmentResourceMaxNumberOfActiveBoards_Type = Unsigned32
_EquipmentResourceMaxNumberOfActiveBoards_Object = MibScalar
equipmentResourceMaxNumberOfActiveBoards = _EquipmentResourceMaxNumberOfActiveBoards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 8, 4),
    _EquipmentResourceMaxNumberOfActiveBoards_Type()
)
equipmentResourceMaxNumberOfActiveBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentResourceMaxNumberOfActiveBoards.setStatus("current")
_EquipmentSlot_ObjectIdentity = ObjectIdentity
equipmentSlot = _EquipmentSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9)
)
_EquipmentSlotTable_Object = MibTable
equipmentSlotTable = _EquipmentSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1)
)
if mibBuilder.loadTexts:
    equipmentSlotTable.setStatus("current")
_EquipmentSlotEntry_Object = MibTableRow
equipmentSlotEntry = _EquipmentSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1)
)
equipmentSlotEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentSlotIndex"),
)
if mibBuilder.loadTexts:
    equipmentSlotEntry.setStatus("current")


class _EquipmentSlotIndex_Type(Unsigned32):
    """Custom type equipmentSlotIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentSlotIndex_Type.__name__ = "Unsigned32"
_EquipmentSlotIndex_Object = MibTableColumn
equipmentSlotIndex = _EquipmentSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 1),
    _EquipmentSlotIndex_Type()
)
equipmentSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotIndex.setStatus("current")
_EquipmentSlotName_Type = MgmtNameString
_EquipmentSlotName_Object = MibTableColumn
equipmentSlotName = _EquipmentSlotName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 2),
    _EquipmentSlotName_Type()
)
equipmentSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotName.setStatus("current")
_EquipmentSlotSubrack_Type = SubrackNumber
_EquipmentSlotSubrack_Object = MibTableColumn
equipmentSlotSubrack = _EquipmentSlotSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 3),
    _EquipmentSlotSubrack_Type()
)
equipmentSlotSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotSubrack.setStatus("current")
_EquipmentSlotSlot_Type = SlotNumber
_EquipmentSlotSlot_Object = MibTableColumn
equipmentSlotSlot = _EquipmentSlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 4),
    _EquipmentSlotSlot_Type()
)
equipmentSlotSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotSlot.setStatus("current")
_EquipmentSlotAdminStatus_Type = AdminStatus
_EquipmentSlotAdminStatus_Object = MibTableColumn
equipmentSlotAdminStatus = _EquipmentSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 5),
    _EquipmentSlotAdminStatus_Type()
)
equipmentSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equipmentSlotAdminStatus.setStatus("current")


class _EquipmentSlotUsageState_Type(Integer32):
    """Custom type equipmentSlotUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("used", 2))
    )


_EquipmentSlotUsageState_Type.__name__ = "Integer32"
_EquipmentSlotUsageState_Object = MibTableColumn
equipmentSlotUsageState = _EquipmentSlotUsageState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 6),
    _EquipmentSlotUsageState_Type()
)
equipmentSlotUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotUsageState.setStatus("current")
_EquipmentSlotEmptySlot_Type = FaultStatus
_EquipmentSlotEmptySlot_Object = MibTableColumn
equipmentSlotEmptySlot = _EquipmentSlotEmptySlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 7),
    _EquipmentSlotEmptySlot_Type()
)
equipmentSlotEmptySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotEmptySlot.setStatus("current")
_EquipmentSlotEquipped_Type = TruthValueWithNA
_EquipmentSlotEquipped_Object = MibTableColumn
equipmentSlotEquipped = _EquipmentSlotEquipped_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 8),
    _EquipmentSlotEquipped_Type()
)
equipmentSlotEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotEquipped.setStatus("current")


class _EquipmentSlotAid_Type(DisplayString):
    """Custom type equipmentSlotAid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EquipmentSlotAid_Type.__name__ = "DisplayString"
_EquipmentSlotAid_Object = MibTableColumn
equipmentSlotAid = _EquipmentSlotAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 9),
    _EquipmentSlotAid_Type()
)
equipmentSlotAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotAid.setStatus("current")


class _EquipmentSlotPhysicalLocation_Type(DisplayString):
    """Custom type equipmentSlotPhysicalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EquipmentSlotPhysicalLocation_Type.__name__ = "DisplayString"
_EquipmentSlotPhysicalLocation_Object = MibTableColumn
equipmentSlotPhysicalLocation = _EquipmentSlotPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 9, 1, 1, 10),
    _EquipmentSlotPhysicalLocation_Type()
)
equipmentSlotPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentSlotPhysicalLocation.setStatus("current")
_EquipmentOpticalModuleList_ObjectIdentity = ObjectIdentity
equipmentOpticalModuleList = _EquipmentOpticalModuleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10)
)
_EquipmentOpticalModuleTable_Object = MibTable
equipmentOpticalModuleTable = _EquipmentOpticalModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1)
)
if mibBuilder.loadTexts:
    equipmentOpticalModuleTable.setStatus("current")
_EquipmentOpticalModuleEntry_Object = MibTableRow
equipmentOpticalModuleEntry = _EquipmentOpticalModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1)
)
equipmentOpticalModuleEntry.setIndexNames(
    (0, "LUM-EQUIPMENT-MIB", "equipmentOpticalModuleIndex"),
)
if mibBuilder.loadTexts:
    equipmentOpticalModuleEntry.setStatus("current")


class _EquipmentOpticalModuleIndex_Type(Unsigned32):
    """Custom type equipmentOpticalModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EquipmentOpticalModuleIndex_Type.__name__ = "Unsigned32"
_EquipmentOpticalModuleIndex_Object = MibTableColumn
equipmentOpticalModuleIndex = _EquipmentOpticalModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 1),
    _EquipmentOpticalModuleIndex_Type()
)
equipmentOpticalModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleIndex.setStatus("current")
_EquipmentOpticalModuleHostBoardType_Type = EquipmentBoardType
_EquipmentOpticalModuleHostBoardType_Object = MibTableColumn
equipmentOpticalModuleHostBoardType = _EquipmentOpticalModuleHostBoardType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 2),
    _EquipmentOpticalModuleHostBoardType_Type()
)
equipmentOpticalModuleHostBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleHostBoardType.setStatus("current")
_EquipmentOpticalModuleType_Type = MgmtNameString
_EquipmentOpticalModuleType_Object = MibTableColumn
equipmentOpticalModuleType = _EquipmentOpticalModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 3),
    _EquipmentOpticalModuleType_Type()
)
equipmentOpticalModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleType.setStatus("current")
_EquipmentOpticalModuleName_Type = MgmtNameString
_EquipmentOpticalModuleName_Object = MibTableColumn
equipmentOpticalModuleName = _EquipmentOpticalModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 4),
    _EquipmentOpticalModuleName_Type()
)
equipmentOpticalModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleName.setStatus("current")
_EquipmentOpticalModuleSubrack_Type = SubrackNumber
_EquipmentOpticalModuleSubrack_Object = MibTableColumn
equipmentOpticalModuleSubrack = _EquipmentOpticalModuleSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 5),
    _EquipmentOpticalModuleSubrack_Type()
)
equipmentOpticalModuleSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleSubrack.setStatus("current")
_EquipmentOpticalModuleSlot_Type = SlotNumber
_EquipmentOpticalModuleSlot_Object = MibTableColumn
equipmentOpticalModuleSlot = _EquipmentOpticalModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 6),
    _EquipmentOpticalModuleSlot_Type()
)
equipmentOpticalModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleSlot.setStatus("current")
_EquipmentOpticalModuleFirmwareVersion_Type = DisplayString
_EquipmentOpticalModuleFirmwareVersion_Object = MibTableColumn
equipmentOpticalModuleFirmwareVersion = _EquipmentOpticalModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 7),
    _EquipmentOpticalModuleFirmwareVersion_Type()
)
equipmentOpticalModuleFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleFirmwareVersion.setStatus("current")
_EquipmentOpticalModuleSerialNumber_Type = DisplayString
_EquipmentOpticalModuleSerialNumber_Object = MibTableColumn
equipmentOpticalModuleSerialNumber = _EquipmentOpticalModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 8),
    _EquipmentOpticalModuleSerialNumber_Type()
)
equipmentOpticalModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleSerialNumber.setStatus("current")
_EquipmentOpticalModuleWarmingUpState_Type = TruthValueWithNA
_EquipmentOpticalModuleWarmingUpState_Object = MibTableColumn
equipmentOpticalModuleWarmingUpState = _EquipmentOpticalModuleWarmingUpState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 9),
    _EquipmentOpticalModuleWarmingUpState_Type()
)
equipmentOpticalModuleWarmingUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleWarmingUpState.setStatus("current")
_EquipmentOpticalModuleFailure_Type = FaultStatus
_EquipmentOpticalModuleFailure_Object = MibTableColumn
equipmentOpticalModuleFailure = _EquipmentOpticalModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 10, 1, 1, 10),
    _EquipmentOpticalModuleFailure_Type()
)
equipmentOpticalModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equipmentOpticalModuleFailure.setStatus("current")

# Managed Objects groups

equipmentGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 1)
)
equipmentGeneralGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralTestAndIncr"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralMibSpecVersion"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralMibImplVersion"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentGeneralGroup.setStatus("current")

equipmentSubrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 2)
)
equipmentSubrackGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroup.setStatus("deprecated")

equipmentBoardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 3)
)
equipmentBoardGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroup.setStatus("deprecated")

equipmentPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 4)
)
equipmentPowerGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentPowerIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerName"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerType"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerACPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerTemperatureHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerModuleMissing"))
)
if mibBuilder.loadTexts:
    equipmentPowerGroup.setStatus("deprecated")

equipmentFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 5)
)
equipmentFanGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanName"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanUnitFailed"))
)
if mibBuilder.loadTexts:
    equipmentFanGroup.setStatus("deprecated")

equipmentGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 6)
)
equipmentGeneralGroupV2.setObjects(
    ("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    equipmentGeneralGroupV2.setStatus("deprecated")

equipmentSubrackGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 8)
)
equipmentSubrackGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV2.setStatus("deprecated")

equipmentSubrackGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 9)
)
equipmentSubrackGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV3.setStatus("deprecated")

equipmentBoardGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 10)
)
equipmentBoardGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV2.setStatus("deprecated")

equipmentNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 11)
)
equipmentNodeGroup.setObjects(
    ("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest")
)
if mibBuilder.loadTexts:
    equipmentNodeGroup.setStatus("deprecated")

equipmentGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 12)
)
equipmentGeneralGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentGeneralGroupV3.setStatus("deprecated")

equipmentNodeGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 13)
)
equipmentNodeGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV2.setStatus("deprecated")

equipmentNodeGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 14)
)
equipmentNodeGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV3.setStatus("deprecated")

equipmentSubrackGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 15)
)
equipmentSubrackGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV4.setStatus("deprecated")

equipmentBoardGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 16)
)
equipmentBoardGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV3.setStatus("deprecated")

equipmentSubrackGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 18)
)
equipmentSubrackGroupV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV5.setStatus("deprecated")

equipmentFanGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 19)
)
equipmentFanGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanName"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanMainUnitFailed"))
)
if mibBuilder.loadTexts:
    equipmentFanGroupV2.setStatus("deprecated")

equipmentGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 20)
)
equipmentGeneralGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralStateLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentSubrackTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentBoardTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentPowerTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentFanTableSize"))
)
if mibBuilder.loadTexts:
    equipmentGeneralGroupV4.setStatus("deprecated")

equipmentSubrackGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 21)
)
equipmentSubrackGroupV6.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackObjectProperty"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV6.setStatus("deprecated")

equipmentBoardGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 22)
)
equipmentBoardGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV4.setStatus("deprecated")

equipmentPowerGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 23)
)
equipmentPowerGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentPowerIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerName"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerType"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerACPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerTemperatureHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerObjectProperty"))
)
if mibBuilder.loadTexts:
    equipmentPowerGroupV2.setStatus("deprecated")

equipmentFanGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 24)
)
equipmentFanGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanName"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanMainUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanObjectProperty"))
)
if mibBuilder.loadTexts:
    equipmentFanGroupV3.setStatus("deprecated")

equipmentNodeGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 25)
)
equipmentNodeGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"),
        ("LUM-EQUIPMENT-MIB", "equipmentAllowDummyPassiveSlots"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV4.setStatus("deprecated")

equipmentBoardGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 26)
)
equipmentBoardGroupV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV5.setStatus("deprecated")

equipmentBoardGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 27)
)
equipmentBoardGroupV6.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV6.setStatus("deprecated")

equipmentBoardGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 28)
)
equipmentBoardGroupV7.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV7.setStatus("deprecated")

equipmentNodeGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 29)
)
equipmentNodeGroupV8.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"),
        ("LUM-EQUIPMENT-MIB", "equipmentAllowDummyPassiveSlots"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeManagementVlan"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV8.setStatus("deprecated")

equipmentBoardGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 30)
)
equipmentBoardGroupV8.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV8.setStatus("deprecated")

equipmentNodeGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 31)
)
equipmentNodeGroupV9.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"),
        ("LUM-EQUIPMENT-MIB", "equipmentAllowDummyPassiveSlots"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeManagementVlan"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMgmtVlanPrivacy"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV9.setStatus("deprecated")

equipmentResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 32)
)
equipmentResourceGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentResourceNumberOfBoards"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceMaxNumberOfBoards"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceNumberOfActiveBoards"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceMaxNumberOfActiveBoards"))
)
if mibBuilder.loadTexts:
    equipmentResourceGroup.setStatus("current")

equipmentSubrackGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 33)
)
equipmentSubrackGroupV7.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackShelfLength"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV7.setStatus("deprecated")

equipmentSubrackGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 34)
)
equipmentSubrackGroupV8.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackShelfLength"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackLANModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackFirstPbSlotMismatch"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV8.setStatus("deprecated")

equipmentBoardGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 35)
)
equipmentBoardGroupV9.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV9.setStatus("deprecated")

equipmentBoardGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 37)
)
equipmentBoardGroupV10.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdditionalInfo"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV10.setStatus("deprecated")

equipmentNodeGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 38)
)
equipmentNodeGroupV10.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"),
        ("LUM-EQUIPMENT-MIB", "equipmentAllowDummyPassiveSlots"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeManagementVlan"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMgmtVlanPrivacy"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeDcnRedundancyMode"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV10.setStatus("deprecated")

equipmentBoardGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 40)
)
equipmentBoardGroupV11.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdditionalInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBootError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardHardwareError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowDiskSpace"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardClockDrift"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV11.setStatus("deprecated")

equipmentFanGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 41)
)
equipmentFanGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanName"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanMainUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanFanFault"))
)
if mibBuilder.loadTexts:
    equipmentFanGroupV4.setStatus("deprecated")

equipmentSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 42)
)
equipmentSlotGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSlotIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotUsageState"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotEmptySlot"))
)
if mibBuilder.loadTexts:
    equipmentSlotGroup.setStatus("deprecated")

equipmentBoardGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 43)
)
equipmentBoardGroupV12.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdditionalInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBootError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardHardwareError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowDiskSpace"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardClockDrift"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardPostponeFwUpgrade"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActivatePendingFwCommand"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwActivationPending"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFeatureNotSupported"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV12.setStatus("deprecated")

equipmentNodeGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 44)
)
equipmentNodeGroupV11.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentNodeLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeIcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMemoryProfile"),
        ("LUM-EQUIPMENT-MIB", "equipmentAllowDummyPassiveSlots"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeManagementVlan"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeMgmtVlanPrivacy"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeDcnRedundancyMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeProxyArp"))
)
if mibBuilder.loadTexts:
    equipmentNodeGroupV11.setStatus("current")

equipmentBoardGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 45)
)
equipmentBoardGroupV13.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdditionalInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBootError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardHardwareError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowDiskSpace"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardClockDrift"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardPostponeFwUpgrade"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActivatePendingFwCommand"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwActivationPending"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFeatureNotSupported"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwReloadNeeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwContextUnknown"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBoardVariant"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCabinetConnectivity"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCabinetConnectionFailure"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV13.setStatus("deprecated")

equipmentPowerGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 46)
)
equipmentPowerGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentPowerIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerName"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerType"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerACPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerTemperatureHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailedSeverity"))
)
if mibBuilder.loadTexts:
    equipmentPowerGroupV3.setStatus("deprecated")

equipmentBoardGroupV14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 47)
)
equipmentBoardGroupV14.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedTest"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCommunicationFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInterworkFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSecondaryPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNonVitalDataMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardUnderMaintenance"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSwVersionMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardReconfigure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLedStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardModuleInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardNewSwActivatedButNotRestarted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowTemperature"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLowThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdditionalInfo"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBootError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardHardwareError"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLowDiskSpace"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardClockDrift"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardPostponeFwUpgrade"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActivatePendingFwCommand"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwActivationPending"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFeatureNotSupported"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwReloadNeeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardFwContextUnknown"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardBoardVariant"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCabinetConnectivity"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardCabinetConnectionFailure"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperationalVariant"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardPhysicalLocation"))
)
if mibBuilder.loadTexts:
    equipmentBoardGroupV14.setStatus("current")

equipmentSlotGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 48)
)
equipmentSlotGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSlotIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotUsageState"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotEmptySlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotEquipped"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotPhysicalLocation"))
)
if mibBuilder.loadTexts:
    equipmentSlotGroupV2.setStatus("current")

equipmentSubrackGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 49)
)
equipmentSubrackGroupV9.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackShelfLength"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackLANModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackFirstPbSlotMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackPhysicalLocation"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV9.setStatus("deprecated")

equipmentPowerGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 50)
)
equipmentPowerGroupV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentPowerIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerName"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerType"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerACPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerTemperatureHigh"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerDCPowerFailedSeverity"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerPhysicalLocation"))
)
if mibBuilder.loadTexts:
    equipmentPowerGroupV4.setStatus("current")

equipmentFanGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 51)
)
equipmentFanGroupV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentFanIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanName"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanMainUnitFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanFanFault"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanPhysicalLocation"))
)
if mibBuilder.loadTexts:
    equipmentFanGroupV5.setStatus("current")

equipmentGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 52)
)
equipmentGeneralGroupV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralStateLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentSubrackTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentBoardTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentPowerTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentFanTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentSlotTableSize"))
)
if mibBuilder.loadTexts:
    equipmentGeneralGroupV5.setStatus("deprecated")

equipmentSubrackGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 53)
)
equipmentSubrackGroupV10.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentSubrackIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackName"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAllFanUnitsFailed"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackUnexpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempHighExceeded"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackTempThreshold"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackDataChanged"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackSystemModeSet"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackEffectiveSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackCurrentSystemMode"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackObjectProperty"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackShelfLength"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackLANModuleMissing"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackExpectedFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackActualFirstPbSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackFirstPbSlotMismatch"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackAid"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackPhysicalLocation"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackChangeExpectedType"))
)
if mibBuilder.loadTexts:
    equipmentSubrackGroupV10.setStatus("current")

equipmentGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 54)
)
equipmentGeneralGroupV6.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralStateLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentSubrackTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentBoardTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentPowerTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentFanTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentSlotTableSize"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentOpticalModuleTableSize"))
)
if mibBuilder.loadTexts:
    equipmentGeneralGroupV6.setStatus("current")

equipmentOpticalModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 55)
)
equipmentOpticalModuleGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleHostBoardType"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleType"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleName"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleFirmwareVersion"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleSerialNumber"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleWarmingUpState"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleFailure"))
)
if mibBuilder.loadTexts:
    equipmentOpticalModuleGroup.setStatus("current")

equipmentGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 3, 1)
)
equipmentGeneralMinimalGroupV1.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralStateLastChangeTime"),
        ("LUM-EQUIPMENT-MIB", "equipmentGeneralEquipmentBoardTableSize"))
)
if mibBuilder.loadTexts:
    equipmentGeneralMinimalGroupV1.setStatus("current")

equipmentBoardMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 3, 2)
)
equipmentBoardMinimalGroupV1.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"))
)
if mibBuilder.loadTexts:
    equipmentBoardMinimalGroupV1.setStatus("deprecated")

equipmentBoardMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 3, 3)
)
equipmentBoardMinimalGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSubrack"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardSlot"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardInvPhysIndexOrZero"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardExpectedType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardActualType"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardDescr"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTemp"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardAdminStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardOperStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatus"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempLow"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardTempVeryHigh"))
)
if mibBuilder.loadTexts:
    equipmentBoardMinimalGroupV2.setStatus("current")


# Notification objects

equipmentBoardRowStatusActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0, 1)
)
equipmentBoardRowStatusActive.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentBoardRowStatusActive.setStatus(
        "current"
    )

equipmentBoardRowStatusDestroy = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0, 2)
)
equipmentBoardRowStatusDestroy.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentBoardRowStatusDestroy.setStatus(
        "deprecated"
    )

equipmentBoardRowStatusInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0, 3)
)
equipmentBoardRowStatusInserted.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentBoardRowStatusInserted.setStatus(
        "current"
    )

equipmentBoardRowStatusRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0, 4)
)
equipmentBoardRowStatusRemoved.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentBoardRowStatusRemoved.setStatus(
        "current"
    )

equipmentBoardRowStatusDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 2, 6, 0, 5)
)
equipmentBoardRowStatusDeleted.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardIndex"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardName"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentBoardRowStatusDeleted.setStatus(
        "current"
    )


# Notifications groups

equipmentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 7)
)
equipmentNotificationGroup.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusActive"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusDestroy"))
)
if mibBuilder.loadTexts:
    equipmentNotificationGroup.setStatus(
        "deprecated"
    )

equipmentNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 17)
)
equipmentNotificationGroupV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusActive"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusDestroy"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusInserted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusRemoved"))
)
if mibBuilder.loadTexts:
    equipmentNotificationGroupV2.setStatus(
        "deprecated"
    )

equipmentNotificationGroupV3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 1, 36)
)
equipmentNotificationGroupV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusActive"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusInserted"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusRemoved"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardRowStatusDeleted"))
)
if mibBuilder.loadTexts:
    equipmentNotificationGroupV3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumEquipmentBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 1)
)
lumEquipmentBasicComplV1.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV1.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 2)
)
lumEquipmentBasicComplV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV2.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 3)
)
lumEquipmentBasicComplV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV3.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 4)
)
lumEquipmentBasicComplV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV4.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 5)
)
lumEquipmentBasicComplV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV5.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 6)
)
lumEquipmentBasicComplV6.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV6.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 7)
)
lumEquipmentBasicComplV7.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV7.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 8)
)
lumEquipmentBasicComplV8.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV8.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 9)
)
lumEquipmentBasicComplV9.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV9.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 10)
)
lumEquipmentBasicComplV10.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV10.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 11)
)
lumEquipmentBasicComplV11.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV11.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 12)
)
lumEquipmentBasicComplV12.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV12.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 13)
)
lumEquipmentBasicComplV13.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV13.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 14)
)
lumEquipmentBasicComplV14.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV14.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 15)
)
lumEquipmentBasicComplV15.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV15.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 16)
)
lumEquipmentBasicComplV16.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV16.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 17)
)
lumEquipmentBasicComplV17.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV17.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 18)
)
lumEquipmentBasicComplV18.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV3"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV18.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 19)
)
lumEquipmentBasicComplV19.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV4"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV19.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 20)
)
lumEquipmentBasicComplV20.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV4"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV20.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 21)
)
lumEquipmentBasicComplV21.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV7"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV4"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV21.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 22)
)
lumEquipmentBasicComplV22.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV7"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV4"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV22.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 23)
)
lumEquipmentBasicComplV23.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV7"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV8"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV23.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 24)
)
lumEquipmentBasicComplV24.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV8"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV24.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV25 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 25)
)
lumEquipmentBasicComplV25.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV9"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV25.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 26)
)
lumEquipmentBasicComplV26.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV26.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 27)
)
lumEquipmentBasicComplV27.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV7"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV27.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 28)
)
lumEquipmentBasicComplV28.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV28.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV29 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 29)
)
lumEquipmentBasicComplV29.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV29.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 30)
)
lumEquipmentBasicComplV30.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV30.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV31 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 31)
)
lumEquipmentBasicComplV31.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV31.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV32 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 32)
)
lumEquipmentBasicComplV32.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV12"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV32.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV33 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 33)
)
lumEquipmentBasicComplV33.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV13"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV33.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV34 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 34)
)
lumEquipmentBasicComplV34.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV9"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV14"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV34.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV35 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 35)
)
lumEquipmentBasicComplV35.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV14"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV35.setStatus(
        "deprecated"
    )

lumEquipmentBasicComplV36 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 2, 36)
)
lumEquipmentBasicComplV36.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV10"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardGroupV14"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV4"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV5"),
        ("LUM-EQUIPMENT-MIB", "equipmentNotificationGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentNodeGroupV11"),
        ("LUM-EQUIPMENT-MIB", "equipmentResourceGroup"),
        ("LUM-EQUIPMENT-MIB", "equipmentSlotGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentOpticalModuleGroup"))
)
if mibBuilder.loadTexts:
    lumEquipmentBasicComplV36.setStatus(
        "current"
    )

lumEquipmentMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 1)
)
lumEquipmentMinimalComplV1.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV1.setStatus(
        "deprecated"
    )

lumEquipmentMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 2)
)
lumEquipmentMinimalComplV2.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV2.setStatus(
        "deprecated"
    )

lumEquipmentMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 3)
)
lumEquipmentMinimalComplV3.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV6"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV3.setStatus(
        "deprecated"
    )

lumEquipmentMinimalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 4)
)
lumEquipmentMinimalComplV4.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV7"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV4.setStatus(
        "current"
    )

lumEquipmentMinimalComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 5)
)
lumEquipmentMinimalComplV5.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV5.setStatus(
        "deprecated"
    )

lumEquipmentMinimalComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 11, 1, 4, 6)
)
lumEquipmentMinimalComplV6.setObjects(
      *(("LUM-EQUIPMENT-MIB", "equipmentGeneralMinimalGroupV1"),
        ("LUM-EQUIPMENT-MIB", "equipmentBoardMinimalGroupV2"),
        ("LUM-EQUIPMENT-MIB", "equipmentSubrackGroupV8"),
        ("LUM-EQUIPMENT-MIB", "equipmentPowerGroupV3"),
        ("LUM-EQUIPMENT-MIB", "equipmentFanGroupV2"))
)
if mibBuilder.loadTexts:
    lumEquipmentMinimalComplV6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-EQUIPMENT-MIB",
    **{"EquipmentSubrackType": EquipmentSubrackType,
       "EquipmentBoardType": EquipmentBoardType,
       "FirstPbSlot": FirstPbSlot,
       "lumEquipmentMIBModule": lumEquipmentMIBModule,
       "lumEquipmentConfs": lumEquipmentConfs,
       "lumEquipmentGroups": lumEquipmentGroups,
       "equipmentGeneralGroup": equipmentGeneralGroup,
       "equipmentSubrackGroup": equipmentSubrackGroup,
       "equipmentBoardGroup": equipmentBoardGroup,
       "equipmentPowerGroup": equipmentPowerGroup,
       "equipmentFanGroup": equipmentFanGroup,
       "equipmentGeneralGroupV2": equipmentGeneralGroupV2,
       "equipmentNotificationGroup": equipmentNotificationGroup,
       "equipmentSubrackGroupV2": equipmentSubrackGroupV2,
       "equipmentSubrackGroupV3": equipmentSubrackGroupV3,
       "equipmentBoardGroupV2": equipmentBoardGroupV2,
       "equipmentNodeGroup": equipmentNodeGroup,
       "equipmentGeneralGroupV3": equipmentGeneralGroupV3,
       "equipmentNodeGroupV2": equipmentNodeGroupV2,
       "equipmentNodeGroupV3": equipmentNodeGroupV3,
       "equipmentSubrackGroupV4": equipmentSubrackGroupV4,
       "equipmentBoardGroupV3": equipmentBoardGroupV3,
       "equipmentNotificationGroupV2": equipmentNotificationGroupV2,
       "equipmentSubrackGroupV5": equipmentSubrackGroupV5,
       "equipmentFanGroupV2": equipmentFanGroupV2,
       "equipmentGeneralGroupV4": equipmentGeneralGroupV4,
       "equipmentSubrackGroupV6": equipmentSubrackGroupV6,
       "equipmentBoardGroupV4": equipmentBoardGroupV4,
       "equipmentPowerGroupV2": equipmentPowerGroupV2,
       "equipmentFanGroupV3": equipmentFanGroupV3,
       "equipmentNodeGroupV4": equipmentNodeGroupV4,
       "equipmentBoardGroupV5": equipmentBoardGroupV5,
       "equipmentBoardGroupV6": equipmentBoardGroupV6,
       "equipmentBoardGroupV7": equipmentBoardGroupV7,
       "equipmentNodeGroupV8": equipmentNodeGroupV8,
       "equipmentBoardGroupV8": equipmentBoardGroupV8,
       "equipmentNodeGroupV9": equipmentNodeGroupV9,
       "equipmentResourceGroup": equipmentResourceGroup,
       "equipmentSubrackGroupV7": equipmentSubrackGroupV7,
       "equipmentSubrackGroupV8": equipmentSubrackGroupV8,
       "equipmentBoardGroupV9": equipmentBoardGroupV9,
       "equipmentNotificationGroupV3": equipmentNotificationGroupV3,
       "equipmentBoardGroupV10": equipmentBoardGroupV10,
       "equipmentNodeGroupV10": equipmentNodeGroupV10,
       "equipmentBoardGroupV11": equipmentBoardGroupV11,
       "equipmentFanGroupV4": equipmentFanGroupV4,
       "equipmentSlotGroup": equipmentSlotGroup,
       "equipmentBoardGroupV12": equipmentBoardGroupV12,
       "equipmentNodeGroupV11": equipmentNodeGroupV11,
       "equipmentBoardGroupV13": equipmentBoardGroupV13,
       "equipmentPowerGroupV3": equipmentPowerGroupV3,
       "equipmentBoardGroupV14": equipmentBoardGroupV14,
       "equipmentSlotGroupV2": equipmentSlotGroupV2,
       "equipmentSubrackGroupV9": equipmentSubrackGroupV9,
       "equipmentPowerGroupV4": equipmentPowerGroupV4,
       "equipmentFanGroupV5": equipmentFanGroupV5,
       "equipmentGeneralGroupV5": equipmentGeneralGroupV5,
       "equipmentSubrackGroupV10": equipmentSubrackGroupV10,
       "equipmentGeneralGroupV6": equipmentGeneralGroupV6,
       "equipmentOpticalModuleGroup": equipmentOpticalModuleGroup,
       "lumEquipmentCompl": lumEquipmentCompl,
       "lumEquipmentBasicComplV1": lumEquipmentBasicComplV1,
       "lumEquipmentBasicComplV2": lumEquipmentBasicComplV2,
       "lumEquipmentBasicComplV3": lumEquipmentBasicComplV3,
       "lumEquipmentBasicComplV4": lumEquipmentBasicComplV4,
       "lumEquipmentBasicComplV5": lumEquipmentBasicComplV5,
       "lumEquipmentBasicComplV6": lumEquipmentBasicComplV6,
       "lumEquipmentBasicComplV7": lumEquipmentBasicComplV7,
       "lumEquipmentBasicComplV8": lumEquipmentBasicComplV8,
       "lumEquipmentBasicComplV9": lumEquipmentBasicComplV9,
       "lumEquipmentBasicComplV10": lumEquipmentBasicComplV10,
       "lumEquipmentBasicComplV11": lumEquipmentBasicComplV11,
       "lumEquipmentBasicComplV12": lumEquipmentBasicComplV12,
       "lumEquipmentBasicComplV13": lumEquipmentBasicComplV13,
       "lumEquipmentBasicComplV14": lumEquipmentBasicComplV14,
       "lumEquipmentBasicComplV15": lumEquipmentBasicComplV15,
       "lumEquipmentBasicComplV16": lumEquipmentBasicComplV16,
       "lumEquipmentBasicComplV17": lumEquipmentBasicComplV17,
       "lumEquipmentBasicComplV18": lumEquipmentBasicComplV18,
       "lumEquipmentBasicComplV19": lumEquipmentBasicComplV19,
       "lumEquipmentBasicComplV20": lumEquipmentBasicComplV20,
       "lumEquipmentBasicComplV21": lumEquipmentBasicComplV21,
       "lumEquipmentBasicComplV22": lumEquipmentBasicComplV22,
       "lumEquipmentBasicComplV23": lumEquipmentBasicComplV23,
       "lumEquipmentBasicComplV24": lumEquipmentBasicComplV24,
       "lumEquipmentBasicComplV25": lumEquipmentBasicComplV25,
       "lumEquipmentBasicComplV26": lumEquipmentBasicComplV26,
       "lumEquipmentBasicComplV27": lumEquipmentBasicComplV27,
       "lumEquipmentBasicComplV28": lumEquipmentBasicComplV28,
       "lumEquipmentBasicComplV29": lumEquipmentBasicComplV29,
       "lumEquipmentBasicComplV30": lumEquipmentBasicComplV30,
       "lumEquipmentBasicComplV31": lumEquipmentBasicComplV31,
       "lumEquipmentBasicComplV32": lumEquipmentBasicComplV32,
       "lumEquipmentBasicComplV33": lumEquipmentBasicComplV33,
       "lumEquipmentBasicComplV34": lumEquipmentBasicComplV34,
       "lumEquipmentBasicComplV35": lumEquipmentBasicComplV35,
       "lumEquipmentBasicComplV36": lumEquipmentBasicComplV36,
       "lumEquipmentMinimalGroups": lumEquipmentMinimalGroups,
       "equipmentGeneralMinimalGroupV1": equipmentGeneralMinimalGroupV1,
       "equipmentBoardMinimalGroupV1": equipmentBoardMinimalGroupV1,
       "equipmentBoardMinimalGroupV2": equipmentBoardMinimalGroupV2,
       "lumEquipmentMinimalCompl": lumEquipmentMinimalCompl,
       "lumEquipmentMinimalComplV1": lumEquipmentMinimalComplV1,
       "lumEquipmentMinimalComplV2": lumEquipmentMinimalComplV2,
       "lumEquipmentMinimalComplV3": lumEquipmentMinimalComplV3,
       "lumEquipmentMinimalComplV4": lumEquipmentMinimalComplV4,
       "lumEquipmentMinimalComplV5": lumEquipmentMinimalComplV5,
       "lumEquipmentMinimalComplV6": lumEquipmentMinimalComplV6,
       "lumEquipmentMIBObjects": lumEquipmentMIBObjects,
       "equipmentGeneral": equipmentGeneral,
       "equipmentGeneralTestAndIncr": equipmentGeneralTestAndIncr,
       "equipmentGeneralMibSpecVersion": equipmentGeneralMibSpecVersion,
       "equipmentGeneralMibImplVersion": equipmentGeneralMibImplVersion,
       "equipmentGeneralLastChangeTime": equipmentGeneralLastChangeTime,
       "equipmentGeneralStateLastChangeTime": equipmentGeneralStateLastChangeTime,
       "equipmentGeneralEquipmentSubrackTableSize": equipmentGeneralEquipmentSubrackTableSize,
       "equipmentGeneralEquipmentBoardTableSize": equipmentGeneralEquipmentBoardTableSize,
       "equipmentGeneralEquipmentPowerTableSize": equipmentGeneralEquipmentPowerTableSize,
       "equipmentGeneralEquipmentFanTableSize": equipmentGeneralEquipmentFanTableSize,
       "equipmentGeneralEquipmentSlotTableSize": equipmentGeneralEquipmentSlotTableSize,
       "equipmentGeneralEquipmentOpticalModuleTableSize": equipmentGeneralEquipmentOpticalModuleTableSize,
       "equipmentSubrackList": equipmentSubrackList,
       "equipmentSubrackTable": equipmentSubrackTable,
       "equipmentSubrackEntry": equipmentSubrackEntry,
       "equipmentSubrackIndex": equipmentSubrackIndex,
       "equipmentSubrackName": equipmentSubrackName,
       "equipmentSubrackSubrack": equipmentSubrackSubrack,
       "equipmentSubrackDescr": equipmentSubrackDescr,
       "equipmentSubrackInvPhysIndexOrZero": equipmentSubrackInvPhysIndexOrZero,
       "equipmentSubrackAllFanUnitsFailed": equipmentSubrackAllFanUnitsFailed,
       "equipmentSubrackRowStatus": equipmentSubrackRowStatus,
       "equipmentSubrackExpectedType": equipmentSubrackExpectedType,
       "equipmentSubrackActualType": equipmentSubrackActualType,
       "equipmentSubrackUnexpectedType": equipmentSubrackUnexpectedType,
       "equipmentSubrackTemp": equipmentSubrackTemp,
       "equipmentSubrackTempHighExceeded": equipmentSubrackTempHighExceeded,
       "equipmentSubrackTempThreshold": equipmentSubrackTempThreshold,
       "equipmentSubrackDataChanged": equipmentSubrackDataChanged,
       "equipmentSubrackSystemModeSet": equipmentSubrackSystemModeSet,
       "equipmentSubrackEffectiveSystemMode": equipmentSubrackEffectiveSystemMode,
       "equipmentSubrackCurrentSystemMode": equipmentSubrackCurrentSystemMode,
       "equipmentSubrackAdminStatus": equipmentSubrackAdminStatus,
       "equipmentSubrackOperStatus": equipmentSubrackOperStatus,
       "equipmentSubrackObjectProperty": equipmentSubrackObjectProperty,
       "equipmentSubrackShelfLength": equipmentSubrackShelfLength,
       "equipmentSubrackLANModuleMissing": equipmentSubrackLANModuleMissing,
       "equipmentSubrackExpectedFirstPbSlot": equipmentSubrackExpectedFirstPbSlot,
       "equipmentSubrackActualFirstPbSlot": equipmentSubrackActualFirstPbSlot,
       "equipmentSubrackFirstPbSlotMismatch": equipmentSubrackFirstPbSlotMismatch,
       "equipmentSubrackAid": equipmentSubrackAid,
       "equipmentSubrackPhysicalLocation": equipmentSubrackPhysicalLocation,
       "equipmentSubrackChangeExpectedType": equipmentSubrackChangeExpectedType,
       "equipmentBoardList": equipmentBoardList,
       "equipmentBoardTable": equipmentBoardTable,
       "equipmentBoardEntry": equipmentBoardEntry,
       "equipmentBoardIndex": equipmentBoardIndex,
       "equipmentBoardName": equipmentBoardName,
       "equipmentBoardExpectedType": equipmentBoardExpectedType,
       "equipmentBoardActualType": equipmentBoardActualType,
       "equipmentBoardDescr": equipmentBoardDescr,
       "equipmentBoardSubrack": equipmentBoardSubrack,
       "equipmentBoardSlot": equipmentBoardSlot,
       "equipmentBoardTemp": equipmentBoardTemp,
       "equipmentBoardInvPhysIndexOrZero": equipmentBoardInvPhysIndexOrZero,
       "equipmentBoardLedTest": equipmentBoardLedTest,
       "equipmentBoardAdminStatus": equipmentBoardAdminStatus,
       "equipmentBoardOperStatus": equipmentBoardOperStatus,
       "equipmentBoardLastChangeTime": equipmentBoardLastChangeTime,
       "equipmentBoardRowStatus": equipmentBoardRowStatus,
       "equipmentBoardMissing": equipmentBoardMissing,
       "equipmentBoardUnexpectedType": equipmentBoardUnexpectedType,
       "equipmentBoardTempHighExceeded": equipmentBoardTempHighExceeded,
       "equipmentBoardCommunicationFailure": equipmentBoardCommunicationFailure,
       "equipmentBoardInterworkFailed": equipmentBoardInterworkFailed,
       "equipmentBoardSecondaryPowerFailed": equipmentBoardSecondaryPowerFailed,
       "equipmentBoardVitalDataMissing": equipmentBoardVitalDataMissing,
       "equipmentBoardNonVitalDataMissing": equipmentBoardNonVitalDataMissing,
       "equipmentBoardUnderMaintenance": equipmentBoardUnderMaintenance,
       "equipmentBoardTempThreshold": equipmentBoardTempThreshold,
       "equipmentBoardSwVersionMismatch": equipmentBoardSwVersionMismatch,
       "equipmentBoardObjectProperty": equipmentBoardObjectProperty,
       "equipmentBoardTempLow": equipmentBoardTempLow,
       "equipmentBoardTempVeryHigh": equipmentBoardTempVeryHigh,
       "equipmentBoardReconfigure": equipmentBoardReconfigure,
       "equipmentBoardLedStatus": equipmentBoardLedStatus,
       "equipmentBoardModuleInfo": equipmentBoardModuleInfo,
       "equipmentBoardNewSwActivatedButNotRestarted": equipmentBoardNewSwActivatedButNotRestarted,
       "equipmentBoardLowTemperature": equipmentBoardLowTemperature,
       "equipmentBoardTempLowThreshold": equipmentBoardTempLowThreshold,
       "equipmentBoardAdditionalInfo": equipmentBoardAdditionalInfo,
       "equipmentBoardBootError": equipmentBoardBootError,
       "equipmentBoardHardwareError": equipmentBoardHardwareError,
       "equipmentBoardLowDiskSpace": equipmentBoardLowDiskSpace,
       "equipmentBoardClockDrift": equipmentBoardClockDrift,
       "equipmentBoardPostponeFwUpgrade": equipmentBoardPostponeFwUpgrade,
       "equipmentBoardActivatePendingFwCommand": equipmentBoardActivatePendingFwCommand,
       "equipmentBoardFwActivationPending": equipmentBoardFwActivationPending,
       "equipmentBoardFeatureNotSupported": equipmentBoardFeatureNotSupported,
       "equipmentBoardFwReloadNeeded": equipmentBoardFwReloadNeeded,
       "equipmentBoardFwContextUnknown": equipmentBoardFwContextUnknown,
       "equipmentBoardBoardVariant": equipmentBoardBoardVariant,
       "equipmentBoardCabinetConnectivity": equipmentBoardCabinetConnectivity,
       "equipmentBoardCabinetConnectionFailure": equipmentBoardCabinetConnectionFailure,
       "equipmentBoardOperationalVariant": equipmentBoardOperationalVariant,
       "equipmentBoardAid": equipmentBoardAid,
       "equipmentBoardPhysicalLocation": equipmentBoardPhysicalLocation,
       "equipmentPowerList": equipmentPowerList,
       "equipmentPowerTable": equipmentPowerTable,
       "equipmentPowerEntry": equipmentPowerEntry,
       "equipmentPowerIndex": equipmentPowerIndex,
       "equipmentPowerName": equipmentPowerName,
       "equipmentPowerSubrack": equipmentPowerSubrack,
       "equipmentPowerSlot": equipmentPowerSlot,
       "equipmentPowerType": equipmentPowerType,
       "equipmentPowerInvPhysIndexOrZero": equipmentPowerInvPhysIndexOrZero,
       "equipmentPowerAdminStatus": equipmentPowerAdminStatus,
       "equipmentPowerOperStatus": equipmentPowerOperStatus,
       "equipmentPowerRowStatus": equipmentPowerRowStatus,
       "equipmentPowerACPowerFailed": equipmentPowerACPowerFailed,
       "equipmentPowerDCPowerFailed": equipmentPowerDCPowerFailed,
       "equipmentPowerTemperatureHigh": equipmentPowerTemperatureHigh,
       "equipmentPowerModuleMissing": equipmentPowerModuleMissing,
       "equipmentPowerObjectProperty": equipmentPowerObjectProperty,
       "equipmentPowerDCPowerFailedSeverity": equipmentPowerDCPowerFailedSeverity,
       "equipmentPowerAid": equipmentPowerAid,
       "equipmentPowerPhysicalLocation": equipmentPowerPhysicalLocation,
       "equipmentFanList": equipmentFanList,
       "equipmentFanTable": equipmentFanTable,
       "equipmentFanEntry": equipmentFanEntry,
       "equipmentFanIndex": equipmentFanIndex,
       "equipmentFanName": equipmentFanName,
       "equipmentFanSubrack": equipmentFanSubrack,
       "equipmentFanSlot": equipmentFanSlot,
       "equipmentFanInvPhysIndexOrZero": equipmentFanInvPhysIndexOrZero,
       "equipmentFanAdminStatus": equipmentFanAdminStatus,
       "equipmentFanOperStatus": equipmentFanOperStatus,
       "equipmentFanRowStatus": equipmentFanRowStatus,
       "equipmentFanUnitFailed": equipmentFanUnitFailed,
       "equipmentFanMainUnitFailed": equipmentFanMainUnitFailed,
       "equipmentFanObjectProperty": equipmentFanObjectProperty,
       "equipmentFanFanFault": equipmentFanFanFault,
       "equipmentFanAid": equipmentFanAid,
       "equipmentFanPhysicalLocation": equipmentFanPhysicalLocation,
       "lumentisEquipmentNotifications": lumentisEquipmentNotifications,
       "equipmentNotifyPrefix": equipmentNotifyPrefix,
       "equipmentBoardRowStatusActive": equipmentBoardRowStatusActive,
       "equipmentBoardRowStatusDestroy": equipmentBoardRowStatusDestroy,
       "equipmentBoardRowStatusInserted": equipmentBoardRowStatusInserted,
       "equipmentBoardRowStatusRemoved": equipmentBoardRowStatusRemoved,
       "equipmentBoardRowStatusDeleted": equipmentBoardRowStatusDeleted,
       "equipmentNode": equipmentNode,
       "equipmentNodeLedTest": equipmentNodeLedTest,
       "equipmentNodeIcnRedundancyMode": equipmentNodeIcnRedundancyMode,
       "equipmentNodeMemoryProfile": equipmentNodeMemoryProfile,
       "equipmentAllowDummyPassiveSlots": equipmentAllowDummyPassiveSlots,
       "equipmentNodeManagementVlan": equipmentNodeManagementVlan,
       "equipmentNodeMgmtVlanPrivacy": equipmentNodeMgmtVlanPrivacy,
       "equipmentNodeDcnRedundancyMode": equipmentNodeDcnRedundancyMode,
       "equipmentNodeProxyArp": equipmentNodeProxyArp,
       "equipmentResource": equipmentResource,
       "equipmentResourceNumberOfBoards": equipmentResourceNumberOfBoards,
       "equipmentResourceMaxNumberOfBoards": equipmentResourceMaxNumberOfBoards,
       "equipmentResourceNumberOfActiveBoards": equipmentResourceNumberOfActiveBoards,
       "equipmentResourceMaxNumberOfActiveBoards": equipmentResourceMaxNumberOfActiveBoards,
       "equipmentSlot": equipmentSlot,
       "equipmentSlotTable": equipmentSlotTable,
       "equipmentSlotEntry": equipmentSlotEntry,
       "equipmentSlotIndex": equipmentSlotIndex,
       "equipmentSlotName": equipmentSlotName,
       "equipmentSlotSubrack": equipmentSlotSubrack,
       "equipmentSlotSlot": equipmentSlotSlot,
       "equipmentSlotAdminStatus": equipmentSlotAdminStatus,
       "equipmentSlotUsageState": equipmentSlotUsageState,
       "equipmentSlotEmptySlot": equipmentSlotEmptySlot,
       "equipmentSlotEquipped": equipmentSlotEquipped,
       "equipmentSlotAid": equipmentSlotAid,
       "equipmentSlotPhysicalLocation": equipmentSlotPhysicalLocation,
       "equipmentOpticalModuleList": equipmentOpticalModuleList,
       "equipmentOpticalModuleTable": equipmentOpticalModuleTable,
       "equipmentOpticalModuleEntry": equipmentOpticalModuleEntry,
       "equipmentOpticalModuleIndex": equipmentOpticalModuleIndex,
       "equipmentOpticalModuleHostBoardType": equipmentOpticalModuleHostBoardType,
       "equipmentOpticalModuleType": equipmentOpticalModuleType,
       "equipmentOpticalModuleName": equipmentOpticalModuleName,
       "equipmentOpticalModuleSubrack": equipmentOpticalModuleSubrack,
       "equipmentOpticalModuleSlot": equipmentOpticalModuleSlot,
       "equipmentOpticalModuleFirmwareVersion": equipmentOpticalModuleFirmwareVersion,
       "equipmentOpticalModuleSerialNumber": equipmentOpticalModuleSerialNumber,
       "equipmentOpticalModuleWarmingUpState": equipmentOpticalModuleWarmingUpState,
       "equipmentOpticalModuleFailure": equipmentOpticalModuleFailure}
)
