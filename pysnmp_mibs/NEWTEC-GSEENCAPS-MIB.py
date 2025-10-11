# SNMP MIB module (NEWTEC-GSEENCAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-GSEENCAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:54 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcGseEncaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100)
)
if mibBuilder.loadTexts:
    ntcGseEncaps.setRevisions(
        ("2015-09-25 11:00",
         "2015-04-13 07:00",
         "2015-01-30 08:00",
         "2014-12-03 07:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-07-05 06:00",
         "2013-05-22 06:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcGseEncObjects_ObjectIdentity = ObjectIdentity
ntcGseEncObjects = _NtcGseEncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1)
)
if mibBuilder.loadTexts:
    ntcGseEncObjects.setStatus("current")
_NtcGseEncCarrier_ObjectIdentity = ObjectIdentity
ntcGseEncCarrier = _NtcGseEncCarrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1)
)
if mibBuilder.loadTexts:
    ntcGseEncCarrier.setStatus("current")


class _NtcGseEncModStandard_Type(Integer32):
    """Custom type ntcGseEncModStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dvbs2", 1),
          ("s2ext", 3),
          ("dvbs2x", 7))
    )


_NtcGseEncModStandard_Type.__name__ = "Integer32"
_NtcGseEncModStandard_Object = MibScalar
ntcGseEncModStandard = _NtcGseEncModStandard_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 1),
    _NtcGseEncModStandard_Type()
)
ntcGseEncModStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncModStandard.setStatus("current")


class _NtcGseEncPilots_Type(NtcEnable):
    """Custom type ntcGseEncPilots based on NtcEnable"""
    defaultValue = 1


_NtcGseEncPilots_Type.__name__ = "NtcEnable"
_NtcGseEncPilots_Object = MibScalar
ntcGseEncPilots = _NtcGseEncPilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 2),
    _NtcGseEncPilots_Type()
)
ntcGseEncPilots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncPilots.setStatus("current")


class _NtcGseEncSymbolRate_Type(Unsigned32):
    """Custom type ntcGseEncSymbolRate based on Unsigned32"""
    defaultValue = 5000000


_NtcGseEncSymbolRate_Type.__name__ = "Unsigned32"
_NtcGseEncSymbolRate_Object = MibScalar
ntcGseEncSymbolRate = _NtcGseEncSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 3),
    _NtcGseEncSymbolRate_Type()
)
ntcGseEncSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseEncSymbolRate.setUnits("baud")
_NtcGseEncCarLinkOpt_ObjectIdentity = ObjectIdentity
ntcGseEncCarLinkOpt = _NtcGseEncCarLinkOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ntcGseEncCarLinkOpt.setStatus("current")


class _NtcGseEncTransMode_Type(Integer32):
    """Custom type ntcGseEncTransMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("multiple", 2),
          ("singlelin", 3))
    )


_NtcGseEncTransMode_Type.__name__ = "Integer32"
_NtcGseEncTransMode_Object = MibScalar
ntcGseEncTransMode = _NtcGseEncTransMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 4, 1),
    _NtcGseEncTransMode_Type()
)
ntcGseEncTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncTransMode.setStatus("current")


class _NtcGseEncEquaEnable_Type(NtcEnable):
    """Custom type ntcGseEncEquaEnable based on NtcEnable"""
    defaultValue = 0


_NtcGseEncEquaEnable_Type.__name__ = "NtcEnable"
_NtcGseEncEquaEnable_Object = MibScalar
ntcGseEncEquaEnable = _NtcGseEncEquaEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 4, 2),
    _NtcGseEncEquaEnable_Type()
)
ntcGseEncEquaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncEquaEnable.setStatus("current")


class _NtcGseEncStreamMode_Type(Integer32):
    """Custom type ntcGseEncStreamMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multistream", 1),
          ("singlestream", 2))
    )


_NtcGseEncStreamMode_Type.__name__ = "Integer32"
_NtcGseEncStreamMode_Object = MibScalar
ntcGseEncStreamMode = _NtcGseEncStreamMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 5),
    _NtcGseEncStreamMode_Type()
)
ntcGseEncStreamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncStreamMode.setStatus("current")


class _NtcGseEncS2Modcod_Type(Integer32):
    """Custom type ntcGseEncS2Modcod based on Integer32"""
    defaultValue = 7

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
              80)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk1345", 29),
          ("qpsk920", 30),
          ("qpsk1120", 31),
          ("e8apsk59l", 32),
          ("e8apsk2645l", 33),
          ("e8psk2336", 34),
          ("e8psk2536", 35),
          ("e8psk1318", 36),
          ("e16apsk12l", 37),
          ("e16apsk815l", 38),
          ("e16apsk59l", 39),
          ("e16apsk2645", 40),
          ("e16apsk35", 41),
          ("e16apsk35l", 42),
          ("e16apsk2845", 43),
          ("e16apsk2336", 44),
          ("e16apsk23l", 45),
          ("e16apsk2536", 46),
          ("e16apsk1318", 47),
          ("e16apsk79", 48),
          ("e16apsk7790", 49),
          ("e32apsk23l", 50),
          ("e32apsk3245", 51),
          ("e32apsk1115", 52),
          ("e32apsk79", 53),
          ("e64apsk3245l", 54),
          ("e64apsk1115", 55),
          ("e64apsk79", 56),
          ("e64apsk45", 57),
          ("e64apsk56", 58),
          ("e128apsk34", 59),
          ("e128apsk79", 60),
          ("e256apsk2945l", 61),
          ("e256apsk23l", 62),
          ("e256apsk3145l", 63),
          ("e256apsk3245", 64),
          ("e256apsk1115l", 65),
          ("e256apsk34", 66),
          ("qpsk1145", 67),
          ("qpsk415", 68),
          ("qpsk1445", 69),
          ("qpsk715", 70),
          ("qpsk815", 71),
          ("qpsk3245", 72),
          ("e8psk715", 73),
          ("e8psk815", 74),
          ("e8psk2645", 75),
          ("e8psk3245", 76),
          ("e16apsk715", 77),
          ("e16apsk815", 78),
          ("e16apsk3245", 79),
          ("e32apsk23", 80))
    )


_NtcGseEncS2Modcod_Type.__name__ = "Integer32"
_NtcGseEncS2Modcod_Object = MibScalar
ntcGseEncS2Modcod = _NtcGseEncS2Modcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 6),
    _NtcGseEncS2Modcod_Type()
)
ntcGseEncS2Modcod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncS2Modcod.setStatus("current")


class _NtcGseEncFrameType_Type(Integer32):
    """Custom type ntcGseEncFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcGseEncFrameType_Type.__name__ = "Integer32"
_NtcGseEncFrameType_Object = MibScalar
ntcGseEncFrameType = _NtcGseEncFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 1, 7),
    _NtcGseEncFrameType_Type()
)
ntcGseEncFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncFrameType.setStatus("current")
_NtcGseEncMonitor_ObjectIdentity = ObjectIdentity
ntcGseEncMonitor = _NtcGseEncMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2)
)
if mibBuilder.loadTexts:
    ntcGseEncMonitor.setStatus("current")
_NtcGseEncMonChannelTable_Object = MibTable
ntcGseEncMonChannelTable = _NtcGseEncMonChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntcGseEncMonChannelTable.setStatus("current")
_NtcGseEncMonChannelEntry_Object = MibTableRow
ntcGseEncMonChannelEntry = _NtcGseEncMonChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1)
)
ntcGseEncMonChannelEntry.setIndexNames(
    (0, "NEWTEC-GSEENCAPS-MIB", "ntcGseEncMonChannelInx"),
)
if mibBuilder.loadTexts:
    ntcGseEncMonChannelEntry.setStatus("current")
_NtcGseEncMonChannelInx_Type = Unsigned32
_NtcGseEncMonChannelInx_Object = MibTableColumn
ntcGseEncMonChannelInx = _NtcGseEncMonChannelInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 1),
    _NtcGseEncMonChannelInx_Type()
)
ntcGseEncMonChannelInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseEncMonChannelInx.setStatus("current")


class _NtcGseEncMonChannelName_Type(DisplayString):
    """Custom type ntcGseEncMonChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcGseEncMonChannelName_Type.__name__ = "DisplayString"
_NtcGseEncMonChannelName_Object = MibTableColumn
ntcGseEncMonChannelName = _NtcGseEncMonChannelName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 2),
    _NtcGseEncMonChannelName_Type()
)
ntcGseEncMonChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseEncMonChannelName.setStatus("current")


class _NtcGseEncMonChannelNominalModcod_Type(Integer32):
    """Custom type ntcGseEncMonChannelNominalModcod based on Integer32"""
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
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215),
          ("qpsk1345", 256),
          ("qpsk920", 257),
          ("qpsk1120", 258),
          ("e8apsk59l", 259),
          ("e8apsk2645l", 260),
          ("e8psk2336", 261),
          ("e8psk2536", 262),
          ("e8psk1318", 263),
          ("e16apsk12l", 264),
          ("e16apsk815l", 265),
          ("e16apsk59l", 266),
          ("e16apsk2645", 267),
          ("e16apsk35", 268),
          ("e16apsk35l", 269),
          ("e16apsk2845", 270),
          ("e16apsk2336", 271),
          ("e16apsk23l", 272),
          ("e16apsk2536", 273),
          ("e16apsk1318", 274),
          ("e16apsk79", 275),
          ("e16apsk7790", 276),
          ("e32apsk23l", 277),
          ("e32apsk3245", 278),
          ("e32apsk1115", 279),
          ("e32apsk79", 280),
          ("e64apsk3245l", 281),
          ("e64apsk1115", 282),
          ("e64apsk79", 283),
          ("e64apsk45", 284),
          ("e64apsk56", 285),
          ("e128apsk34", 286),
          ("e128apsk79", 287),
          ("e256apsk2945l", 288),
          ("e256apsk23l", 289),
          ("e256apsk3145l", 290),
          ("e256apsk3245", 291),
          ("e256apsk1115l", 292),
          ("e256apsk34", 293),
          ("qpsk1145", 294),
          ("qpsk415", 295),
          ("qpsk1445", 296),
          ("qpsk715", 297),
          ("qpsk815", 298),
          ("qpsk3245", 299),
          ("e8psk715", 300),
          ("e8psk815", 301),
          ("e8psk2645", 302),
          ("e8psk3245", 303),
          ("e16apsk715", 304),
          ("e16apsk815", 305),
          ("e16apsk3245", 306),
          ("e32apsk23", 307))
    )


_NtcGseEncMonChannelNominalModcod_Type.__name__ = "Integer32"
_NtcGseEncMonChannelNominalModcod_Object = MibTableColumn
ntcGseEncMonChannelNominalModcod = _NtcGseEncMonChannelNominalModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 3),
    _NtcGseEncMonChannelNominalModcod_Type()
)
ntcGseEncMonChannelNominalModcod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseEncMonChannelNominalModcod.setStatus("current")


class _NtcGseEncMonChannelModcod_Type(Integer32):
    """Custom type ntcGseEncMonChannelModcod based on Integer32"""
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
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215),
          ("qpsk1345", 256),
          ("qpsk920", 257),
          ("qpsk1120", 258),
          ("e8apsk59l", 259),
          ("e8apsk2645l", 260),
          ("e8psk2336", 261),
          ("e8psk2536", 262),
          ("e8psk1318", 263),
          ("e16apsk12l", 264),
          ("e16apsk815l", 265),
          ("e16apsk59l", 266),
          ("e16apsk2645", 267),
          ("e16apsk35", 268),
          ("e16apsk35l", 269),
          ("e16apsk2845", 270),
          ("e16apsk2336", 271),
          ("e16apsk23l", 272),
          ("e16apsk2536", 273),
          ("e16apsk1318", 274),
          ("e16apsk79", 275),
          ("e16apsk7790", 276),
          ("e32apsk23l", 277),
          ("e32apsk3245", 278),
          ("e32apsk1115", 279),
          ("e32apsk79", 280),
          ("e64apsk3245l", 281),
          ("e64apsk1115", 282),
          ("e64apsk79", 283),
          ("e64apsk45", 284),
          ("e64apsk56", 285),
          ("e128apsk34", 286),
          ("e128apsk79", 287),
          ("e256apsk2945l", 288),
          ("e256apsk23l", 289),
          ("e256apsk3145l", 290),
          ("e256apsk3245", 291),
          ("e256apsk1115l", 292),
          ("e256apsk34", 293),
          ("qpsk1145", 294),
          ("qpsk415", 295),
          ("qpsk1445", 296),
          ("qpsk715", 297),
          ("qpsk815", 298),
          ("qpsk3245", 299),
          ("e8psk715", 300),
          ("e8psk815", 301),
          ("e8psk2645", 302),
          ("e8psk3245", 303),
          ("e16apsk715", 304),
          ("e16apsk815", 305),
          ("e16apsk3245", 306),
          ("e32apsk23", 307))
    )


_NtcGseEncMonChannelModcod_Type.__name__ = "Integer32"
_NtcGseEncMonChannelModcod_Object = MibTableColumn
ntcGseEncMonChannelModcod = _NtcGseEncMonChannelModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 4),
    _NtcGseEncMonChannelModcod_Type()
)
ntcGseEncMonChannelModcod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseEncMonChannelModcod.setStatus("current")
_NtcGseEncMonChannelModcodChanges_Type = Counter64
_NtcGseEncMonChannelModcodChanges_Object = MibTableColumn
ntcGseEncMonChannelModcodChanges = _NtcGseEncMonChannelModcodChanges_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 5),
    _NtcGseEncMonChannelModcodChanges_Type()
)
ntcGseEncMonChannelModcodChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseEncMonChannelModcodChanges.setStatus("current")


class _NtcGseEncProtocol_Type(Integer32):
    """Custom type ntcGseEncProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gse", 0),
          ("xpe", 1),
          ("mpe", 2),
          ("ule", 3))
    )


_NtcGseEncProtocol_Type.__name__ = "Integer32"
_NtcGseEncProtocol_Object = MibTableColumn
ntcGseEncProtocol = _NtcGseEncProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 2, 1, 1, 6),
    _NtcGseEncProtocol_Type()
)
ntcGseEncProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseEncProtocol.setStatus("current")
_NtcGseEncapsTable_Object = MibTable
ntcGseEncapsTable = _NtcGseEncapsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3)
)
if mibBuilder.loadTexts:
    ntcGseEncapsTable.setStatus("current")
_NtcGseEncapsEntry_Object = MibTableRow
ntcGseEncapsEntry = _NtcGseEncapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3, 1)
)
ntcGseEncapsEntry.setIndexNames(
    (0, "NEWTEC-GSEENCAPS-MIB", "ntcGseEncapsIsi"),
)
if mibBuilder.loadTexts:
    ntcGseEncapsEntry.setStatus("current")
_NtcGseEncapsIsi_Type = Unsigned32
_NtcGseEncapsIsi_Object = MibTableColumn
ntcGseEncapsIsi = _NtcGseEncapsIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3, 1, 1),
    _NtcGseEncapsIsi_Type()
)
ntcGseEncapsIsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseEncapsIsi.setStatus("current")
_NtcGseEncapsRowStatus_Type = RowStatus
_NtcGseEncapsRowStatus_Object = MibTableColumn
ntcGseEncapsRowStatus = _NtcGseEncapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3, 1, 2),
    _NtcGseEncapsRowStatus_Type()
)
ntcGseEncapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncapsRowStatus.setStatus("current")
_NtcGseEncapsEnable_Type = NtcEnable
_NtcGseEncapsEnable_Object = MibTableColumn
ntcGseEncapsEnable = _NtcGseEncapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3, 1, 3),
    _NtcGseEncapsEnable_Type()
)
ntcGseEncapsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncapsEnable.setStatus("current")


class _NtcGseEncapsFrmTp_Type(Integer32):
    """Custom type ntcGseEncapsFrmTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcGseEncapsFrmTp_Type.__name__ = "Integer32"
_NtcGseEncapsFrmTp_Object = MibTableColumn
ntcGseEncapsFrmTp = _NtcGseEncapsFrmTp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 3, 1, 4),
    _NtcGseEncapsFrmTp_Type()
)
ntcGseEncapsFrmTp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncapsFrmTp.setStatus("current")
_NtcGseEncChannelsTable_Object = MibTable
ntcGseEncChannelsTable = _NtcGseEncChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4)
)
if mibBuilder.loadTexts:
    ntcGseEncChannelsTable.setStatus("current")
_NtcGseEncChannelsEntry_Object = MibTableRow
ntcGseEncChannelsEntry = _NtcGseEncChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1)
)
ntcGseEncChannelsEntry.setIndexNames(
    (0, "NEWTEC-GSEENCAPS-MIB", "ntcGseEncChannelsName"),
)
if mibBuilder.loadTexts:
    ntcGseEncChannelsEntry.setStatus("current")


class _NtcGseEncChannelsName_Type(DisplayString):
    """Custom type ntcGseEncChannelsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseEncChannelsName_Type.__name__ = "DisplayString"
_NtcGseEncChannelsName_Object = MibTableColumn
ntcGseEncChannelsName = _NtcGseEncChannelsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 1),
    _NtcGseEncChannelsName_Type()
)
ntcGseEncChannelsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseEncChannelsName.setStatus("current")
_NtcGseEncChannelsRowStatus_Type = RowStatus
_NtcGseEncChannelsRowStatus_Object = MibTableColumn
ntcGseEncChannelsRowStatus = _NtcGseEncChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 2),
    _NtcGseEncChannelsRowStatus_Type()
)
ntcGseEncChannelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChannelsRowStatus.setStatus("current")
_NtcGseEncChanEnable_Type = NtcEnable
_NtcGseEncChanEnable_Object = MibTableColumn
ntcGseEncChanEnable = _NtcGseEncChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 3),
    _NtcGseEncChanEnable_Type()
)
ntcGseEncChanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanEnable.setStatus("current")
_NtcGseEncChanIsi_Type = Unsigned32
_NtcGseEncChanIsi_Object = MibTableColumn
ntcGseEncChanIsi = _NtcGseEncChanIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 4),
    _NtcGseEncChanIsi_Type()
)
ntcGseEncChanIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanIsi.setStatus("current")


class _NtcGseEncChanLabel_Type(DisplayString):
    """Custom type ntcGseEncChanLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcGseEncChanLabel_Type.__name__ = "DisplayString"
_NtcGseEncChanLabel_Object = MibTableColumn
ntcGseEncChanLabel = _NtcGseEncChanLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 5),
    _NtcGseEncChanLabel_Type()
)
ntcGseEncChanLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanLabel.setStatus("current")


class _NtcGseEncChanNomS2Modcod_Type(Integer32):
    """Custom type ntcGseEncChanNomS2Modcod based on Integer32"""
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
              80)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk1345", 29),
          ("qpsk920", 30),
          ("qpsk1120", 31),
          ("e8apsk59l", 32),
          ("e8apsk2645l", 33),
          ("e8psk2336", 34),
          ("e8psk2536", 35),
          ("e8psk1318", 36),
          ("e16apsk12l", 37),
          ("e16apsk815l", 38),
          ("e16apsk59l", 39),
          ("e16apsk2645", 40),
          ("e16apsk35", 41),
          ("e16apsk35l", 42),
          ("e16apsk2845", 43),
          ("e16apsk2336", 44),
          ("e16apsk23l", 45),
          ("e16apsk2536", 46),
          ("e16apsk1318", 47),
          ("e16apsk79", 48),
          ("e16apsk7790", 49),
          ("e32apsk23l", 50),
          ("e32apsk3245", 51),
          ("e32apsk1115", 52),
          ("e32apsk79", 53),
          ("e64apsk3245l", 54),
          ("e64apsk1115", 55),
          ("e64apsk79", 56),
          ("e64apsk45", 57),
          ("e64apsk56", 58),
          ("e128apsk34", 59),
          ("e128apsk79", 60),
          ("e256apsk2945l", 61),
          ("e256apsk23l", 62),
          ("e256apsk3145l", 63),
          ("e256apsk3245", 64),
          ("e256apsk1115l", 65),
          ("e256apsk34", 66),
          ("qpsk1145", 67),
          ("qpsk415", 68),
          ("qpsk1445", 69),
          ("qpsk715", 70),
          ("qpsk815", 71),
          ("qpsk3245", 72),
          ("e8psk715", 73),
          ("e8psk815", 74),
          ("e8psk2645", 75),
          ("e8psk3245", 76),
          ("e16apsk715", 77),
          ("e16apsk815", 78),
          ("e16apsk3245", 79),
          ("e32apsk23", 80))
    )


_NtcGseEncChanNomS2Modcod_Type.__name__ = "Integer32"
_NtcGseEncChanNomS2Modcod_Object = MibTableColumn
ntcGseEncChanNomS2Modcod = _NtcGseEncChanNomS2Modcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 6),
    _NtcGseEncChanNomS2Modcod_Type()
)
ntcGseEncChanNomS2Modcod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanNomS2Modcod.setStatus("current")


class _NtcGseEncChanNomS2ExtModcod_Type(Integer32):
    """Custom type ntcGseEncChanNomS2ExtModcod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              215)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215))
    )


_NtcGseEncChanNomS2ExtModcod_Type.__name__ = "Integer32"
_NtcGseEncChanNomS2ExtModcod_Object = MibTableColumn
ntcGseEncChanNomS2ExtModcod = _NtcGseEncChanNomS2ExtModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 7),
    _NtcGseEncChanNomS2ExtModcod_Type()
)
ntcGseEncChanNomS2ExtModcod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanNomS2ExtModcod.setStatus("current")
_NtcGseEncChanAcmEnable_Type = NtcEnable
_NtcGseEncChanAcmEnable_Object = MibTableColumn
ntcGseEncChanAcmEnable = _NtcGseEncChanAcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 8),
    _NtcGseEncChanAcmEnable_Type()
)
ntcGseEncChanAcmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanAcmEnable.setStatus("current")


class _NtcGseEncChanTermName_Type(DisplayString):
    """Custom type ntcGseEncChanTermName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcGseEncChanTermName_Type.__name__ = "DisplayString"
_NtcGseEncChanTermName_Object = MibTableColumn
ntcGseEncChanTermName = _NtcGseEncChanTermName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 4, 1, 9),
    _NtcGseEncChanTermName_Type()
)
ntcGseEncChanTermName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncChanTermName.setStatus("current")
_NtcGseEncIsisTable_Object = MibTable
ntcGseEncIsisTable = _NtcGseEncIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5)
)
if mibBuilder.loadTexts:
    ntcGseEncIsisTable.setStatus("current")
_NtcGseEncIsisEntry_Object = MibTableRow
ntcGseEncIsisEntry = _NtcGseEncIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1)
)
ntcGseEncIsisEntry.setIndexNames(
    (0, "NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsisName"),
)
if mibBuilder.loadTexts:
    ntcGseEncIsisEntry.setStatus("current")


class _NtcGseEncIsisName_Type(DisplayString):
    """Custom type ntcGseEncIsisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseEncIsisName_Type.__name__ = "DisplayString"
_NtcGseEncIsisName_Object = MibTableColumn
ntcGseEncIsisName = _NtcGseEncIsisName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 1),
    _NtcGseEncIsisName_Type()
)
ntcGseEncIsisName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseEncIsisName.setStatus("current")
_NtcGseEncIsisRowStatus_Type = RowStatus
_NtcGseEncIsisRowStatus_Object = MibTableColumn
ntcGseEncIsisRowStatus = _NtcGseEncIsisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 2),
    _NtcGseEncIsisRowStatus_Type()
)
ntcGseEncIsisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncIsisRowStatus.setStatus("current")
_NtcGseEncIsiEnable_Type = NtcEnable
_NtcGseEncIsiEnable_Object = MibTableColumn
ntcGseEncIsiEnable = _NtcGseEncIsiEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 3),
    _NtcGseEncIsiEnable_Type()
)
ntcGseEncIsiEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncIsiEnable.setStatus("current")
_NtcGseEncIsiIsi_Type = Unsigned32
_NtcGseEncIsiIsi_Object = MibTableColumn
ntcGseEncIsiIsi = _NtcGseEncIsiIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 4),
    _NtcGseEncIsiIsi_Type()
)
ntcGseEncIsiIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncIsiIsi.setStatus("current")


class _NtcGseEncIsiFrmTp_Type(Integer32):
    """Custom type ntcGseEncIsiFrmTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcGseEncIsiFrmTp_Type.__name__ = "Integer32"
_NtcGseEncIsiFrmTp_Object = MibTableColumn
ntcGseEncIsiFrmTp = _NtcGseEncIsiFrmTp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 5),
    _NtcGseEncIsiFrmTp_Type()
)
ntcGseEncIsiFrmTp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncIsiFrmTp.setStatus("current")


class _NtcGseEncIsiProtocol_Type(Integer32):
    """Custom type ntcGseEncIsiProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("gse", 1),
          ("xpe", 2))
    )


_NtcGseEncIsiProtocol_Type.__name__ = "Integer32"
_NtcGseEncIsiProtocol_Object = MibTableColumn
ntcGseEncIsiProtocol = _NtcGseEncIsiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 5, 1, 6),
    _NtcGseEncIsiProtocol_Type()
)
ntcGseEncIsiProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncIsiProtocol.setStatus("current")
_NtcGseEncBbfChannelsTable_Object = MibTable
ntcGseEncBbfChannelsTable = _NtcGseEncBbfChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6)
)
if mibBuilder.loadTexts:
    ntcGseEncBbfChannelsTable.setStatus("current")
_NtcGseEncBbfChannelsEntry_Object = MibTableRow
ntcGseEncBbfChannelsEntry = _NtcGseEncBbfChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1)
)
ntcGseEncBbfChannelsEntry.setIndexNames(
    (0, "NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChannelsName"),
)
if mibBuilder.loadTexts:
    ntcGseEncBbfChannelsEntry.setStatus("current")


class _NtcGseEncBbfChannelsName_Type(DisplayString):
    """Custom type ntcGseEncBbfChannelsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseEncBbfChannelsName_Type.__name__ = "DisplayString"
_NtcGseEncBbfChannelsName_Object = MibTableColumn
ntcGseEncBbfChannelsName = _NtcGseEncBbfChannelsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 1),
    _NtcGseEncBbfChannelsName_Type()
)
ntcGseEncBbfChannelsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseEncBbfChannelsName.setStatus("current")
_NtcGseEncBbfChannelsRowStatus_Type = RowStatus
_NtcGseEncBbfChannelsRowStatus_Object = MibTableColumn
ntcGseEncBbfChannelsRowStatus = _NtcGseEncBbfChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 2),
    _NtcGseEncBbfChannelsRowStatus_Type()
)
ntcGseEncBbfChannelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChannelsRowStatus.setStatus("current")
_NtcGseEncBbfChanEnable_Type = NtcEnable
_NtcGseEncBbfChanEnable_Object = MibTableColumn
ntcGseEncBbfChanEnable = _NtcGseEncBbfChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 3),
    _NtcGseEncBbfChanEnable_Type()
)
ntcGseEncBbfChanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanEnable.setStatus("current")


class _NtcGseEncBbfChanOutTypeName_Type(OctetString):
    """Custom type ntcGseEncBbfChanOutTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseEncBbfChanOutTypeName_Type.__name__ = "OctetString"
_NtcGseEncBbfChanOutTypeName_Object = MibTableColumn
ntcGseEncBbfChanOutTypeName = _NtcGseEncBbfChanOutTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 4),
    _NtcGseEncBbfChanOutTypeName_Type()
)
ntcGseEncBbfChanOutTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanOutTypeName.setStatus("current")


class _NtcGseEncBbfChanOutInstanceName_Type(OctetString):
    """Custom type ntcGseEncBbfChanOutInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseEncBbfChanOutInstanceName_Type.__name__ = "OctetString"
_NtcGseEncBbfChanOutInstanceName_Object = MibTableColumn
ntcGseEncBbfChanOutInstanceName = _NtcGseEncBbfChanOutInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 5),
    _NtcGseEncBbfChanOutInstanceName_Type()
)
ntcGseEncBbfChanOutInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanOutInstanceName.setStatus("current")


class _NtcGseEncBbfChanLabel_Type(DisplayString):
    """Custom type ntcGseEncBbfChanLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcGseEncBbfChanLabel_Type.__name__ = "DisplayString"
_NtcGseEncBbfChanLabel_Object = MibTableColumn
ntcGseEncBbfChanLabel = _NtcGseEncBbfChanLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 6),
    _NtcGseEncBbfChanLabel_Type()
)
ntcGseEncBbfChanLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanLabel.setStatus("current")


class _NtcGseEncBbfChanNomS2Modcod_Type(Integer32):
    """Custom type ntcGseEncBbfChanNomS2Modcod based on Integer32"""
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
              80)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk1345", 29),
          ("qpsk920", 30),
          ("qpsk1120", 31),
          ("e8apsk59l", 32),
          ("e8apsk2645l", 33),
          ("e8psk2336", 34),
          ("e8psk2536", 35),
          ("e8psk1318", 36),
          ("e16apsk12l", 37),
          ("e16apsk815l", 38),
          ("e16apsk59l", 39),
          ("e16apsk2645", 40),
          ("e16apsk35", 41),
          ("e16apsk35l", 42),
          ("e16apsk2845", 43),
          ("e16apsk2336", 44),
          ("e16apsk23l", 45),
          ("e16apsk2536", 46),
          ("e16apsk1318", 47),
          ("e16apsk79", 48),
          ("e16apsk7790", 49),
          ("e32apsk23l", 50),
          ("e32apsk3245", 51),
          ("e32apsk1115", 52),
          ("e32apsk79", 53),
          ("e64apsk3245l", 54),
          ("e64apsk1115", 55),
          ("e64apsk79", 56),
          ("e64apsk45", 57),
          ("e64apsk56", 58),
          ("e128apsk34", 59),
          ("e128apsk79", 60),
          ("e256apsk2945l", 61),
          ("e256apsk23l", 62),
          ("e256apsk3145l", 63),
          ("e256apsk3245", 64),
          ("e256apsk1115l", 65),
          ("e256apsk34", 66),
          ("qpsk1145", 67),
          ("qpsk415", 68),
          ("qpsk1445", 69),
          ("qpsk715", 70),
          ("qpsk815", 71),
          ("qpsk3245", 72),
          ("e8psk715", 73),
          ("e8psk815", 74),
          ("e8psk2645", 75),
          ("e8psk3245", 76),
          ("e16apsk715", 77),
          ("e16apsk815", 78),
          ("e16apsk3245", 79),
          ("e32apsk23", 80))
    )


_NtcGseEncBbfChanNomS2Modcod_Type.__name__ = "Integer32"
_NtcGseEncBbfChanNomS2Modcod_Object = MibTableColumn
ntcGseEncBbfChanNomS2Modcod = _NtcGseEncBbfChanNomS2Modcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 7),
    _NtcGseEncBbfChanNomS2Modcod_Type()
)
ntcGseEncBbfChanNomS2Modcod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanNomS2Modcod.setStatus("current")


class _NtcGseEncBbfChanNomS2ExtModcod_Type(Integer32):
    """Custom type ntcGseEncBbfChanNomS2ExtModcod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              215)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215))
    )


_NtcGseEncBbfChanNomS2ExtModcod_Type.__name__ = "Integer32"
_NtcGseEncBbfChanNomS2ExtModcod_Object = MibTableColumn
ntcGseEncBbfChanNomS2ExtModcod = _NtcGseEncBbfChanNomS2ExtModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 8),
    _NtcGseEncBbfChanNomS2ExtModcod_Type()
)
ntcGseEncBbfChanNomS2ExtModcod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanNomS2ExtModcod.setStatus("current")
_NtcGseEncBbfChanAcmEnable_Type = NtcEnable
_NtcGseEncBbfChanAcmEnable_Object = MibTableColumn
ntcGseEncBbfChanAcmEnable = _NtcGseEncBbfChanAcmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 9),
    _NtcGseEncBbfChanAcmEnable_Type()
)
ntcGseEncBbfChanAcmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanAcmEnable.setStatus("current")


class _NtcGseEncBbfChanTermName_Type(DisplayString):
    """Custom type ntcGseEncBbfChanTermName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcGseEncBbfChanTermName_Type.__name__ = "DisplayString"
_NtcGseEncBbfChanTermName_Object = MibTableColumn
ntcGseEncBbfChanTermName = _NtcGseEncBbfChanTermName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 10),
    _NtcGseEncBbfChanTermName_Type()
)
ntcGseEncBbfChanTermName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanTermName.setStatus("current")


class _NtcGseEncBbfChanAccessVlan_Type(Unsigned32):
    """Custom type ntcGseEncBbfChanAccessVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NtcGseEncBbfChanAccessVlan_Type.__name__ = "Unsigned32"
_NtcGseEncBbfChanAccessVlan_Object = MibTableColumn
ntcGseEncBbfChanAccessVlan = _NtcGseEncBbfChanAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 6, 1, 11),
    _NtcGseEncBbfChanAccessVlan_Type()
)
ntcGseEncBbfChanAccessVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseEncBbfChanAccessVlan.setStatus("current")


class _NtcGseEncDefEncProt_Type(Integer32):
    """Custom type ntcGseEncDefEncProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gse", 0),
          ("xpe", 1))
    )


_NtcGseEncDefEncProt_Type.__name__ = "Integer32"
_NtcGseEncDefEncProt_Object = MibScalar
ntcGseEncDefEncProt = _NtcGseEncDefEncProt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 1, 7),
    _NtcGseEncDefEncProt_Type()
)
ntcGseEncDefEncProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseEncDefEncProt.setStatus("current")
_NtcGseEncConformance_ObjectIdentity = ObjectIdentity
ntcGseEncConformance = _NtcGseEncConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 2)
)
if mibBuilder.loadTexts:
    ntcGseEncConformance.setStatus("current")
_NtcGseEncConfCompliance_ObjectIdentity = ObjectIdentity
ntcGseEncConfCompliance = _NtcGseEncConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 2, 1)
)
if mibBuilder.loadTexts:
    ntcGseEncConfCompliance.setStatus("current")
_NtcGseEncConfGroup_ObjectIdentity = ObjectIdentity
ntcGseEncConfGroup = _NtcGseEncConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 2, 2)
)
if mibBuilder.loadTexts:
    ntcGseEncConfGroup.setStatus("current")

# Managed Objects groups

ntcGseEncConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 2, 2, 1)
)
ntcGseEncConfGrpV1Standard.setObjects(
      *(("NEWTEC-GSEENCAPS-MIB", "ntcGseEncModStandard"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncPilots"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncSymbolRate"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncTransMode"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncEquaEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncStreamMode"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncS2Modcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncFrameType"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncMonChannelName"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncMonChannelNominalModcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncMonChannelModcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncMonChannelModcodChanges"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncProtocol"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncapsRowStatus"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncapsEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncapsFrmTp"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChannelsRowStatus"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanIsi"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanLabel"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanNomS2Modcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanNomS2ExtModcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanAcmEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncChanTermName"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsisRowStatus"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsiEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsiIsi"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsiFrmTp"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncIsiProtocol"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChannelsRowStatus"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanOutTypeName"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanOutInstanceName"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanLabel"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanNomS2Modcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanNomS2ExtModcod"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanAcmEnable"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanTermName"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncBbfChanAccessVlan"),
        ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncDefEncProt"))
)
if mibBuilder.loadTexts:
    ntcGseEncConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcGseEncConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2100, 2, 1, 1)
)
ntcGseEncConfCompV1Standard.setObjects(
    ("NEWTEC-GSEENCAPS-MIB", "ntcGseEncConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcGseEncConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-GSEENCAPS-MIB",
    **{"ntcGseEncaps": ntcGseEncaps,
       "ntcGseEncObjects": ntcGseEncObjects,
       "ntcGseEncCarrier": ntcGseEncCarrier,
       "ntcGseEncModStandard": ntcGseEncModStandard,
       "ntcGseEncPilots": ntcGseEncPilots,
       "ntcGseEncSymbolRate": ntcGseEncSymbolRate,
       "ntcGseEncCarLinkOpt": ntcGseEncCarLinkOpt,
       "ntcGseEncTransMode": ntcGseEncTransMode,
       "ntcGseEncEquaEnable": ntcGseEncEquaEnable,
       "ntcGseEncStreamMode": ntcGseEncStreamMode,
       "ntcGseEncS2Modcod": ntcGseEncS2Modcod,
       "ntcGseEncFrameType": ntcGseEncFrameType,
       "ntcGseEncMonitor": ntcGseEncMonitor,
       "ntcGseEncMonChannelTable": ntcGseEncMonChannelTable,
       "ntcGseEncMonChannelEntry": ntcGseEncMonChannelEntry,
       "ntcGseEncMonChannelInx": ntcGseEncMonChannelInx,
       "ntcGseEncMonChannelName": ntcGseEncMonChannelName,
       "ntcGseEncMonChannelNominalModcod": ntcGseEncMonChannelNominalModcod,
       "ntcGseEncMonChannelModcod": ntcGseEncMonChannelModcod,
       "ntcGseEncMonChannelModcodChanges": ntcGseEncMonChannelModcodChanges,
       "ntcGseEncProtocol": ntcGseEncProtocol,
       "ntcGseEncapsTable": ntcGseEncapsTable,
       "ntcGseEncapsEntry": ntcGseEncapsEntry,
       "ntcGseEncapsIsi": ntcGseEncapsIsi,
       "ntcGseEncapsRowStatus": ntcGseEncapsRowStatus,
       "ntcGseEncapsEnable": ntcGseEncapsEnable,
       "ntcGseEncapsFrmTp": ntcGseEncapsFrmTp,
       "ntcGseEncChannelsTable": ntcGseEncChannelsTable,
       "ntcGseEncChannelsEntry": ntcGseEncChannelsEntry,
       "ntcGseEncChannelsName": ntcGseEncChannelsName,
       "ntcGseEncChannelsRowStatus": ntcGseEncChannelsRowStatus,
       "ntcGseEncChanEnable": ntcGseEncChanEnable,
       "ntcGseEncChanIsi": ntcGseEncChanIsi,
       "ntcGseEncChanLabel": ntcGseEncChanLabel,
       "ntcGseEncChanNomS2Modcod": ntcGseEncChanNomS2Modcod,
       "ntcGseEncChanNomS2ExtModcod": ntcGseEncChanNomS2ExtModcod,
       "ntcGseEncChanAcmEnable": ntcGseEncChanAcmEnable,
       "ntcGseEncChanTermName": ntcGseEncChanTermName,
       "ntcGseEncIsisTable": ntcGseEncIsisTable,
       "ntcGseEncIsisEntry": ntcGseEncIsisEntry,
       "ntcGseEncIsisName": ntcGseEncIsisName,
       "ntcGseEncIsisRowStatus": ntcGseEncIsisRowStatus,
       "ntcGseEncIsiEnable": ntcGseEncIsiEnable,
       "ntcGseEncIsiIsi": ntcGseEncIsiIsi,
       "ntcGseEncIsiFrmTp": ntcGseEncIsiFrmTp,
       "ntcGseEncIsiProtocol": ntcGseEncIsiProtocol,
       "ntcGseEncBbfChannelsTable": ntcGseEncBbfChannelsTable,
       "ntcGseEncBbfChannelsEntry": ntcGseEncBbfChannelsEntry,
       "ntcGseEncBbfChannelsName": ntcGseEncBbfChannelsName,
       "ntcGseEncBbfChannelsRowStatus": ntcGseEncBbfChannelsRowStatus,
       "ntcGseEncBbfChanEnable": ntcGseEncBbfChanEnable,
       "ntcGseEncBbfChanOutTypeName": ntcGseEncBbfChanOutTypeName,
       "ntcGseEncBbfChanOutInstanceName": ntcGseEncBbfChanOutInstanceName,
       "ntcGseEncBbfChanLabel": ntcGseEncBbfChanLabel,
       "ntcGseEncBbfChanNomS2Modcod": ntcGseEncBbfChanNomS2Modcod,
       "ntcGseEncBbfChanNomS2ExtModcod": ntcGseEncBbfChanNomS2ExtModcod,
       "ntcGseEncBbfChanAcmEnable": ntcGseEncBbfChanAcmEnable,
       "ntcGseEncBbfChanTermName": ntcGseEncBbfChanTermName,
       "ntcGseEncBbfChanAccessVlan": ntcGseEncBbfChanAccessVlan,
       "ntcGseEncDefEncProt": ntcGseEncDefEncProt,
       "ntcGseEncConformance": ntcGseEncConformance,
       "ntcGseEncConfCompliance": ntcGseEncConfCompliance,
       "ntcGseEncConfCompV1Standard": ntcGseEncConfCompV1Standard,
       "ntcGseEncConfGroup": ntcGseEncConfGroup,
       "ntcGseEncConfGrpV1Standard": ntcGseEncConfGrpV1Standard}
)
