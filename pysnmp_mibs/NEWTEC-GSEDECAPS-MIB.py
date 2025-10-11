# SNMP MIB module (NEWTEC-GSEDECAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-GSEDECAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:03 2025
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

ntcGseDecaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200)
)
if mibBuilder.loadTexts:
    ntcGseDecaps.setRevisions(
        ("2018-02-02 09:00",
         "2015-09-25 11:00",
         "2015-04-13 07:00",
         "2015-01-30 08:00",
         "2014-10-07 08:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-07-05 06:00",
         "2013-05-22 06:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcGseDecObjects_ObjectIdentity = ObjectIdentity
ntcGseDecObjects = _NtcGseDecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1)
)
if mibBuilder.loadTexts:
    ntcGseDecObjects.setStatus("current")


class _NtcGseDecEnable_Type(NtcEnable):
    """Custom type ntcGseDecEnable based on NtcEnable"""
    defaultValue = 0


_NtcGseDecEnable_Type.__name__ = "NtcEnable"
_NtcGseDecEnable_Object = MibScalar
ntcGseDecEnable = _NtcGseDecEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 1),
    _NtcGseDecEnable_Type()
)
ntcGseDecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecEnable.setStatus("current")


class _NtcGseDecOutputSelection_Type(Integer32):
    """Custom type ntcGseDecOutputSelection based on Integer32"""
    defaultValue = 1

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
        *(("none", 0),
          ("data1", 1),
          ("data2", 2),
          ("data", 3))
    )


_NtcGseDecOutputSelection_Type.__name__ = "Integer32"
_NtcGseDecOutputSelection_Object = MibScalar
ntcGseDecOutputSelection = _NtcGseDecOutputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 2),
    _NtcGseDecOutputSelection_Type()
)
ntcGseDecOutputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecOutputSelection.setStatus("current")


class _NtcGseDecIsiFilter_Type(NtcEnable):
    """Custom type ntcGseDecIsiFilter based on NtcEnable"""
    defaultValue = 1


_NtcGseDecIsiFilter_Type.__name__ = "NtcEnable"
_NtcGseDecIsiFilter_Object = MibScalar
ntcGseDecIsiFilter = _NtcGseDecIsiFilter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 3),
    _NtcGseDecIsiFilter_Type()
)
ntcGseDecIsiFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecIsiFilter.setStatus("current")
_NtcGseDecMonitor_ObjectIdentity = ObjectIdentity
ntcGseDecMonitor = _NtcGseDecMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4)
)
if mibBuilder.loadTexts:
    ntcGseDecMonitor.setStatus("current")


class _NtcGseDecMonReset_Type(Integer32):
    """Custom type ntcGseDecMonReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcGseDecMonReset_Type.__name__ = "Integer32"
_NtcGseDecMonReset_Object = MibScalar
ntcGseDecMonReset = _NtcGseDecMonReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 1),
    _NtcGseDecMonReset_Type()
)
ntcGseDecMonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecMonReset.setStatus("current")
_NtcGseDecMonOutBitRate_Type = Counter64
_NtcGseDecMonOutBitRate_Object = MibScalar
ntcGseDecMonOutBitRate = _NtcGseDecMonOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 2),
    _NtcGseDecMonOutBitRate_Type()
)
ntcGseDecMonOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonOutBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonOutBitRate.setUnits("bps")
_NtcGseDecMonOutByteCnt_Type = Counter64
_NtcGseDecMonOutByteCnt_Object = MibScalar
ntcGseDecMonOutByteCnt = _NtcGseDecMonOutByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 3),
    _NtcGseDecMonOutByteCnt_Type()
)
ntcGseDecMonOutByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonOutByteCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonOutByteCnt.setUnits("bytes")
_NtcGseDecMonOutPktCnt_Type = Counter64
_NtcGseDecMonOutPktCnt_Object = MibScalar
ntcGseDecMonOutPktCnt = _NtcGseDecMonOutPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 4),
    _NtcGseDecMonOutPktCnt_Type()
)
ntcGseDecMonOutPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonOutPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonOutPktCnt.setUnits("packets")
_NtcGseDecMonDropByteCnt_Type = Counter64
_NtcGseDecMonDropByteCnt_Object = MibScalar
ntcGseDecMonDropByteCnt = _NtcGseDecMonDropByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 5),
    _NtcGseDecMonDropByteCnt_Type()
)
ntcGseDecMonDropByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonDropByteCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonDropByteCnt.setUnits("bytes")
_NtcGseDecMonDropPktCnt_Type = Counter64
_NtcGseDecMonDropPktCnt_Object = MibScalar
ntcGseDecMonDropPktCnt = _NtcGseDecMonDropPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 6),
    _NtcGseDecMonDropPktCnt_Type()
)
ntcGseDecMonDropPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonDropPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonDropPktCnt.setUnits("packets")
_NtcGseDecMonChanTable_Object = MibTable
ntcGseDecMonChanTable = _NtcGseDecMonChanTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ntcGseDecMonChanTable.setStatus("current")
_NtcGseDecMonChanEntry_Object = MibTableRow
ntcGseDecMonChanEntry = _NtcGseDecMonChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1)
)
ntcGseDecMonChanEntry.setIndexNames(
    (0, "NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanCounterInx"),
)
if mibBuilder.loadTexts:
    ntcGseDecMonChanEntry.setStatus("current")
_NtcGseDecMonChanCounterInx_Type = Unsigned32
_NtcGseDecMonChanCounterInx_Object = MibTableColumn
ntcGseDecMonChanCounterInx = _NtcGseDecMonChanCounterInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 1),
    _NtcGseDecMonChanCounterInx_Type()
)
ntcGseDecMonChanCounterInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseDecMonChanCounterInx.setStatus("current")


class _NtcGseDecMonChanName_Type(DisplayString):
    """Custom type ntcGseDecMonChanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcGseDecMonChanName_Type.__name__ = "DisplayString"
_NtcGseDecMonChanName_Object = MibTableColumn
ntcGseDecMonChanName = _NtcGseDecMonChanName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 2),
    _NtcGseDecMonChanName_Type()
)
ntcGseDecMonChanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanName.setStatus("current")
_NtcGseDecMonChanByteCnt_Type = Counter64
_NtcGseDecMonChanByteCnt_Object = MibTableColumn
ntcGseDecMonChanByteCnt = _NtcGseDecMonChanByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 3),
    _NtcGseDecMonChanByteCnt_Type()
)
ntcGseDecMonChanByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanByteCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonChanByteCnt.setUnits("bytes")
_NtcGseDecMonChanPktCnt_Type = Counter64
_NtcGseDecMonChanPktCnt_Object = MibTableColumn
ntcGseDecMonChanPktCnt = _NtcGseDecMonChanPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 4),
    _NtcGseDecMonChanPktCnt_Type()
)
ntcGseDecMonChanPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonChanPktCnt.setUnits("packets")
_NtcGseDecMonChanByteDropCount_Type = Counter64
_NtcGseDecMonChanByteDropCount_Object = MibTableColumn
ntcGseDecMonChanByteDropCount = _NtcGseDecMonChanByteDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 5),
    _NtcGseDecMonChanByteDropCount_Type()
)
ntcGseDecMonChanByteDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanByteDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonChanByteDropCount.setUnits("bytes")
_NtcGseDecMonChanDropPktCnt_Type = Counter64
_NtcGseDecMonChanDropPktCnt_Object = MibTableColumn
ntcGseDecMonChanDropPktCnt = _NtcGseDecMonChanDropPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 6),
    _NtcGseDecMonChanDropPktCnt_Type()
)
ntcGseDecMonChanDropPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanDropPktCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcGseDecMonChanDropPktCnt.setUnits("packets")


class _NtcGseDecMonChanModCod_Type(Integer32):
    """Custom type ntcGseDecMonChanModCod based on Integer32"""
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


_NtcGseDecMonChanModCod_Type.__name__ = "Integer32"
_NtcGseDecMonChanModCod_Object = MibTableColumn
ntcGseDecMonChanModCod = _NtcGseDecMonChanModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 7),
    _NtcGseDecMonChanModCod_Type()
)
ntcGseDecMonChanModCod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanModCod.setStatus("current")


class _NtcGseDecMonChanLinkMargin_Type(DisplayString):
    """Custom type ntcGseDecMonChanLinkMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcGseDecMonChanLinkMargin_Type.__name__ = "DisplayString"
_NtcGseDecMonChanLinkMargin_Object = MibTableColumn
ntcGseDecMonChanLinkMargin = _NtcGseDecMonChanLinkMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 7, 1, 8),
    _NtcGseDecMonChanLinkMargin_Type()
)
ntcGseDecMonChanLinkMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonChanLinkMargin.setStatus("current")


class _NtcGseDecMonMonCod_Type(Integer32):
    """Custom type ntcGseDecMonMonCod based on Integer32"""
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


_NtcGseDecMonMonCod_Type.__name__ = "Integer32"
_NtcGseDecMonMonCod_Object = MibScalar
ntcGseDecMonMonCod = _NtcGseDecMonMonCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 8),
    _NtcGseDecMonMonCod_Type()
)
ntcGseDecMonMonCod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonMonCod.setStatus("current")


class _NtcGseDecMonLinkMargin_Type(DisplayString):
    """Custom type ntcGseDecMonLinkMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcGseDecMonLinkMargin_Type.__name__ = "DisplayString"
_NtcGseDecMonLinkMargin_Object = MibScalar
ntcGseDecMonLinkMargin = _NtcGseDecMonLinkMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 4, 9),
    _NtcGseDecMonLinkMargin_Type()
)
ntcGseDecMonLinkMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcGseDecMonLinkMargin.setStatus("current")
_NtcGseDecChannelsTable_Object = MibTable
ntcGseDecChannelsTable = _NtcGseDecChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5)
)
if mibBuilder.loadTexts:
    ntcGseDecChannelsTable.setStatus("current")
_NtcGseDecChannelsEntry_Object = MibTableRow
ntcGseDecChannelsEntry = _NtcGseDecChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1)
)
ntcGseDecChannelsEntry.setIndexNames(
    (0, "NEWTEC-GSEDECAPS-MIB", "ntcGseDecChannelsName"),
)
if mibBuilder.loadTexts:
    ntcGseDecChannelsEntry.setStatus("current")


class _NtcGseDecChannelsName_Type(DisplayString):
    """Custom type ntcGseDecChannelsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseDecChannelsName_Type.__name__ = "DisplayString"
_NtcGseDecChannelsName_Object = MibTableColumn
ntcGseDecChannelsName = _NtcGseDecChannelsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 1),
    _NtcGseDecChannelsName_Type()
)
ntcGseDecChannelsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseDecChannelsName.setStatus("current")
_NtcGseDecChannelsRowStatus_Type = RowStatus
_NtcGseDecChannelsRowStatus_Object = MibTableColumn
ntcGseDecChannelsRowStatus = _NtcGseDecChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 2),
    _NtcGseDecChannelsRowStatus_Type()
)
ntcGseDecChannelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChannelsRowStatus.setStatus("current")
_NtcGseDecChanEnable_Type = NtcEnable
_NtcGseDecChanEnable_Object = MibTableColumn
ntcGseDecChanEnable = _NtcGseDecChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 3),
    _NtcGseDecChanEnable_Type()
)
ntcGseDecChanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChanEnable.setStatus("current")
_NtcGseDecChanDemodId_Type = Unsigned32
_NtcGseDecChanDemodId_Object = MibTableColumn
ntcGseDecChanDemodId = _NtcGseDecChanDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 4),
    _NtcGseDecChanDemodId_Type()
)
ntcGseDecChanDemodId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChanDemodId.setStatus("current")
_NtcGseDecChanIsi_Type = Unsigned32
_NtcGseDecChanIsi_Object = MibTableColumn
ntcGseDecChanIsi = _NtcGseDecChanIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 5),
    _NtcGseDecChanIsi_Type()
)
ntcGseDecChanIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChanIsi.setStatus("current")


class _NtcGseDecChanLabel_Type(DisplayString):
    """Custom type ntcGseDecChanLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcGseDecChanLabel_Type.__name__ = "DisplayString"
_NtcGseDecChanLabel_Object = MibTableColumn
ntcGseDecChanLabel = _NtcGseDecChanLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 6),
    _NtcGseDecChanLabel_Type()
)
ntcGseDecChanLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChanLabel.setStatus("current")


class _NtcGseDecChanLabelFilter_Type(Integer32):
    """Custom type ntcGseDecChanLabelFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofilter", 0),
          ("use36bytes", 1))
    )


_NtcGseDecChanLabelFilter_Type.__name__ = "Integer32"
_NtcGseDecChanLabelFilter_Object = MibTableColumn
ntcGseDecChanLabelFilter = _NtcGseDecChanLabelFilter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 5, 1, 7),
    _NtcGseDecChanLabelFilter_Type()
)
ntcGseDecChanLabelFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecChanLabelFilter.setStatus("current")
_NtcGseDecBbfChannelsTable_Object = MibTable
ntcGseDecBbfChannelsTable = _NtcGseDecBbfChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6)
)
if mibBuilder.loadTexts:
    ntcGseDecBbfChannelsTable.setStatus("current")
_NtcGseDecBbfChannelsEntry_Object = MibTableRow
ntcGseDecBbfChannelsEntry = _NtcGseDecBbfChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1)
)
ntcGseDecBbfChannelsEntry.setIndexNames(
    (0, "NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChannelsName"),
)
if mibBuilder.loadTexts:
    ntcGseDecBbfChannelsEntry.setStatus("current")


class _NtcGseDecBbfChannelsName_Type(DisplayString):
    """Custom type ntcGseDecBbfChannelsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseDecBbfChannelsName_Type.__name__ = "DisplayString"
_NtcGseDecBbfChannelsName_Object = MibTableColumn
ntcGseDecBbfChannelsName = _NtcGseDecBbfChannelsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 1),
    _NtcGseDecBbfChannelsName_Type()
)
ntcGseDecBbfChannelsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseDecBbfChannelsName.setStatus("current")
_NtcGseDecBbfChannelsRowStatus_Type = RowStatus
_NtcGseDecBbfChannelsRowStatus_Object = MibTableColumn
ntcGseDecBbfChannelsRowStatus = _NtcGseDecBbfChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 2),
    _NtcGseDecBbfChannelsRowStatus_Type()
)
ntcGseDecBbfChannelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChannelsRowStatus.setStatus("current")
_NtcGseDecBbfChanEnable_Type = NtcEnable
_NtcGseDecBbfChanEnable_Object = MibTableColumn
ntcGseDecBbfChanEnable = _NtcGseDecBbfChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 3),
    _NtcGseDecBbfChanEnable_Type()
)
ntcGseDecBbfChanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanEnable.setStatus("current")


class _NtcGseDecBbfChanInputTypeName_Type(OctetString):
    """Custom type ntcGseDecBbfChanInputTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseDecBbfChanInputTypeName_Type.__name__ = "OctetString"
_NtcGseDecBbfChanInputTypeName_Object = MibTableColumn
ntcGseDecBbfChanInputTypeName = _NtcGseDecBbfChanInputTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 4),
    _NtcGseDecBbfChanInputTypeName_Type()
)
ntcGseDecBbfChanInputTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanInputTypeName.setStatus("current")


class _NtcGseDecBbfChanInputInstName_Type(OctetString):
    """Custom type ntcGseDecBbfChanInputInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseDecBbfChanInputInstName_Type.__name__ = "OctetString"
_NtcGseDecBbfChanInputInstName_Object = MibTableColumn
ntcGseDecBbfChanInputInstName = _NtcGseDecBbfChanInputInstName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 5),
    _NtcGseDecBbfChanInputInstName_Type()
)
ntcGseDecBbfChanInputInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanInputInstName.setStatus("current")


class _NtcGseDecBbfChanLabel_Type(DisplayString):
    """Custom type ntcGseDecBbfChanLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcGseDecBbfChanLabel_Type.__name__ = "DisplayString"
_NtcGseDecBbfChanLabel_Object = MibTableColumn
ntcGseDecBbfChanLabel = _NtcGseDecBbfChanLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 6),
    _NtcGseDecBbfChanLabel_Type()
)
ntcGseDecBbfChanLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanLabel.setStatus("current")


class _NtcGseDecBbfChanLabelFilter_Type(Integer32):
    """Custom type ntcGseDecBbfChanLabelFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofilter", 0),
          ("use36bytes", 1))
    )


_NtcGseDecBbfChanLabelFilter_Type.__name__ = "Integer32"
_NtcGseDecBbfChanLabelFilter_Object = MibTableColumn
ntcGseDecBbfChanLabelFilter = _NtcGseDecBbfChanLabelFilter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 7),
    _NtcGseDecBbfChanLabelFilter_Type()
)
ntcGseDecBbfChanLabelFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanLabelFilter.setStatus("current")


class _NtcGseDecBbfChanVirtualNetwork_Type(OctetString):
    """Custom type ntcGseDecBbfChanVirtualNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseDecBbfChanVirtualNetwork_Type.__name__ = "OctetString"
_NtcGseDecBbfChanVirtualNetwork_Object = MibTableColumn
ntcGseDecBbfChanVirtualNetwork = _NtcGseDecBbfChanVirtualNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 8),
    _NtcGseDecBbfChanVirtualNetwork_Type()
)
ntcGseDecBbfChanVirtualNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanVirtualNetwork.setStatus("current")


class _NtcGseDecBbfChanAccessVlan_Type(Unsigned32):
    """Custom type ntcGseDecBbfChanAccessVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NtcGseDecBbfChanAccessVlan_Type.__name__ = "Unsigned32"
_NtcGseDecBbfChanAccessVlan_Object = MibTableColumn
ntcGseDecBbfChanAccessVlan = _NtcGseDecBbfChanAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 6, 1, 9),
    _NtcGseDecBbfChanAccessVlan_Type()
)
ntcGseDecBbfChanAccessVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecBbfChanAccessVlan.setStatus("current")
_NtcGseDecIsisTable_Object = MibTable
ntcGseDecIsisTable = _NtcGseDecIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7)
)
if mibBuilder.loadTexts:
    ntcGseDecIsisTable.setStatus("current")
_NtcGseDecIsisEntry_Object = MibTableRow
ntcGseDecIsisEntry = _NtcGseDecIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1)
)
ntcGseDecIsisEntry.setIndexNames(
    (0, "NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsisName"),
)
if mibBuilder.loadTexts:
    ntcGseDecIsisEntry.setStatus("current")


class _NtcGseDecIsisName_Type(DisplayString):
    """Custom type ntcGseDecIsisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcGseDecIsisName_Type.__name__ = "DisplayString"
_NtcGseDecIsisName_Object = MibTableColumn
ntcGseDecIsisName = _NtcGseDecIsisName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 1),
    _NtcGseDecIsisName_Type()
)
ntcGseDecIsisName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcGseDecIsisName.setStatus("current")
_NtcGseDecIsisRowStatus_Type = RowStatus
_NtcGseDecIsisRowStatus_Object = MibTableColumn
ntcGseDecIsisRowStatus = _NtcGseDecIsisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 2),
    _NtcGseDecIsisRowStatus_Type()
)
ntcGseDecIsisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsisRowStatus.setStatus("current")
_NtcGseDecIsiEnable_Type = NtcEnable
_NtcGseDecIsiEnable_Object = MibTableColumn
ntcGseDecIsiEnable = _NtcGseDecIsiEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 3),
    _NtcGseDecIsiEnable_Type()
)
ntcGseDecIsiEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsiEnable.setStatus("current")
_NtcGseDecIsiIsi_Type = Unsigned32
_NtcGseDecIsiIsi_Object = MibTableColumn
ntcGseDecIsiIsi = _NtcGseDecIsiIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 4),
    _NtcGseDecIsiIsi_Type()
)
ntcGseDecIsiIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsiIsi.setStatus("current")


class _NtcGseDecIsiProtocol_Type(Integer32):
    """Custom type ntcGseDecIsiProtocol based on Integer32"""
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


_NtcGseDecIsiProtocol_Type.__name__ = "Integer32"
_NtcGseDecIsiProtocol_Object = MibTableColumn
ntcGseDecIsiProtocol = _NtcGseDecIsiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 5),
    _NtcGseDecIsiProtocol_Type()
)
ntcGseDecIsiProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsiProtocol.setStatus("current")


class _NtcGseDecIsiInputTypeName_Type(OctetString):
    """Custom type ntcGseDecIsiInputTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseDecIsiInputTypeName_Type.__name__ = "OctetString"
_NtcGseDecIsiInputTypeName_Object = MibTableColumn
ntcGseDecIsiInputTypeName = _NtcGseDecIsiInputTypeName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 6),
    _NtcGseDecIsiInputTypeName_Type()
)
ntcGseDecIsiInputTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsiInputTypeName.setStatus("current")


class _NtcGseDecIsiInputInstanceName_Type(OctetString):
    """Custom type ntcGseDecIsiInputInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcGseDecIsiInputInstanceName_Type.__name__ = "OctetString"
_NtcGseDecIsiInputInstanceName_Object = MibTableColumn
ntcGseDecIsiInputInstanceName = _NtcGseDecIsiInputInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 7, 1, 7),
    _NtcGseDecIsiInputInstanceName_Type()
)
ntcGseDecIsiInputInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcGseDecIsiInputInstanceName.setStatus("current")


class _NtcGseDecDefDecProt_Type(Integer32):
    """Custom type ntcGseDecDefDecProt based on Integer32"""
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


_NtcGseDecDefDecProt_Type.__name__ = "Integer32"
_NtcGseDecDefDecProt_Object = MibScalar
ntcGseDecDefDecProt = _NtcGseDecDefDecProt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 8),
    _NtcGseDecDefDecProt_Type()
)
ntcGseDecDefDecProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecDefDecProt.setStatus("current")


class _NtcGseDecXpeChecksum_Type(Integer32):
    """Custom type ntcGseDecXpeChecksum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("crc32", 0),
          ("off", 1))
    )


_NtcGseDecXpeChecksum_Type.__name__ = "Integer32"
_NtcGseDecXpeChecksum_Object = MibScalar
ntcGseDecXpeChecksum = _NtcGseDecXpeChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 9),
    _NtcGseDecXpeChecksum_Type()
)
ntcGseDecXpeChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecXpeChecksum.setStatus("current")


class _NtcGseDecDestMacEnable_Type(NtcEnable):
    """Custom type ntcGseDecDestMacEnable based on NtcEnable"""
    defaultValue = 0


_NtcGseDecDestMacEnable_Type.__name__ = "NtcEnable"
_NtcGseDecDestMacEnable_Object = MibScalar
ntcGseDecDestMacEnable = _NtcGseDecDestMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 10),
    _NtcGseDecDestMacEnable_Type()
)
ntcGseDecDestMacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecDestMacEnable.setStatus("current")


class _NtcGseDecDestMac_Type(DisplayString):
    """Custom type ntcGseDecDestMac based on DisplayString"""
    defaultValue = OctetString("00:00:00:00:00:00")


_NtcGseDecDestMac_Type.__name__ = "DisplayString"
_NtcGseDecDestMac_Object = MibScalar
ntcGseDecDestMac = _NtcGseDecDestMac_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 11),
    _NtcGseDecDestMac_Type()
)
ntcGseDecDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecDestMac.setStatus("current")


class _NtcGseDecPidFilter_Type(NtcEnable):
    """Custom type ntcGseDecPidFilter based on NtcEnable"""
    defaultValue = 1


_NtcGseDecPidFilter_Type.__name__ = "NtcEnable"
_NtcGseDecPidFilter_Object = MibScalar
ntcGseDecPidFilter = _NtcGseDecPidFilter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 1, 12),
    _NtcGseDecPidFilter_Type()
)
ntcGseDecPidFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcGseDecPidFilter.setStatus("current")
_NtcGseDecConformance_ObjectIdentity = ObjectIdentity
ntcGseDecConformance = _NtcGseDecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 2)
)
if mibBuilder.loadTexts:
    ntcGseDecConformance.setStatus("current")
_NtcGseDecConfCompliance_ObjectIdentity = ObjectIdentity
ntcGseDecConfCompliance = _NtcGseDecConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 2, 1)
)
if mibBuilder.loadTexts:
    ntcGseDecConfCompliance.setStatus("current")
_NtcGseDecConfGroup_ObjectIdentity = ObjectIdentity
ntcGseDecConfGroup = _NtcGseDecConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 2, 2)
)
if mibBuilder.loadTexts:
    ntcGseDecConfGroup.setStatus("current")

# Managed Objects groups

ntcGseDecConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 2, 2, 1)
)
ntcGseDecConfGrpV1Standard.setObjects(
      *(("NEWTEC-GSEDECAPS-MIB", "ntcGseDecEnable"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecOutputSelection"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiFilter"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonReset"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonOutBitRate"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonOutByteCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonOutPktCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonDropByteCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonDropPktCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanName"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanByteCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanPktCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanByteDropCount"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanDropPktCnt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanModCod"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonChanLinkMargin"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonMonCod"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecMonLinkMargin"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChannelsRowStatus"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChanEnable"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChanDemodId"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChanIsi"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChanLabel"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecChanLabelFilter"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChannelsRowStatus"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanEnable"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanInputTypeName"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanInputInstName"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanLabel"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanLabelFilter"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanVirtualNetwork"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecBbfChanAccessVlan"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsisRowStatus"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiEnable"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiIsi"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiProtocol"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiInputTypeName"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecIsiInputInstanceName"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecDefDecProt"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecXpeChecksum"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecDestMacEnable"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecDestMac"),
        ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecPidFilter"))
)
if mibBuilder.loadTexts:
    ntcGseDecConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcGseDecConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2200, 2, 1, 1)
)
ntcGseDecConfCompV1Standard.setObjects(
    ("NEWTEC-GSEDECAPS-MIB", "ntcGseDecConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcGseDecConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-GSEDECAPS-MIB",
    **{"ntcGseDecaps": ntcGseDecaps,
       "ntcGseDecObjects": ntcGseDecObjects,
       "ntcGseDecEnable": ntcGseDecEnable,
       "ntcGseDecOutputSelection": ntcGseDecOutputSelection,
       "ntcGseDecIsiFilter": ntcGseDecIsiFilter,
       "ntcGseDecMonitor": ntcGseDecMonitor,
       "ntcGseDecMonReset": ntcGseDecMonReset,
       "ntcGseDecMonOutBitRate": ntcGseDecMonOutBitRate,
       "ntcGseDecMonOutByteCnt": ntcGseDecMonOutByteCnt,
       "ntcGseDecMonOutPktCnt": ntcGseDecMonOutPktCnt,
       "ntcGseDecMonDropByteCnt": ntcGseDecMonDropByteCnt,
       "ntcGseDecMonDropPktCnt": ntcGseDecMonDropPktCnt,
       "ntcGseDecMonChanTable": ntcGseDecMonChanTable,
       "ntcGseDecMonChanEntry": ntcGseDecMonChanEntry,
       "ntcGseDecMonChanCounterInx": ntcGseDecMonChanCounterInx,
       "ntcGseDecMonChanName": ntcGseDecMonChanName,
       "ntcGseDecMonChanByteCnt": ntcGseDecMonChanByteCnt,
       "ntcGseDecMonChanPktCnt": ntcGseDecMonChanPktCnt,
       "ntcGseDecMonChanByteDropCount": ntcGseDecMonChanByteDropCount,
       "ntcGseDecMonChanDropPktCnt": ntcGseDecMonChanDropPktCnt,
       "ntcGseDecMonChanModCod": ntcGseDecMonChanModCod,
       "ntcGseDecMonChanLinkMargin": ntcGseDecMonChanLinkMargin,
       "ntcGseDecMonMonCod": ntcGseDecMonMonCod,
       "ntcGseDecMonLinkMargin": ntcGseDecMonLinkMargin,
       "ntcGseDecChannelsTable": ntcGseDecChannelsTable,
       "ntcGseDecChannelsEntry": ntcGseDecChannelsEntry,
       "ntcGseDecChannelsName": ntcGseDecChannelsName,
       "ntcGseDecChannelsRowStatus": ntcGseDecChannelsRowStatus,
       "ntcGseDecChanEnable": ntcGseDecChanEnable,
       "ntcGseDecChanDemodId": ntcGseDecChanDemodId,
       "ntcGseDecChanIsi": ntcGseDecChanIsi,
       "ntcGseDecChanLabel": ntcGseDecChanLabel,
       "ntcGseDecChanLabelFilter": ntcGseDecChanLabelFilter,
       "ntcGseDecBbfChannelsTable": ntcGseDecBbfChannelsTable,
       "ntcGseDecBbfChannelsEntry": ntcGseDecBbfChannelsEntry,
       "ntcGseDecBbfChannelsName": ntcGseDecBbfChannelsName,
       "ntcGseDecBbfChannelsRowStatus": ntcGseDecBbfChannelsRowStatus,
       "ntcGseDecBbfChanEnable": ntcGseDecBbfChanEnable,
       "ntcGseDecBbfChanInputTypeName": ntcGseDecBbfChanInputTypeName,
       "ntcGseDecBbfChanInputInstName": ntcGseDecBbfChanInputInstName,
       "ntcGseDecBbfChanLabel": ntcGseDecBbfChanLabel,
       "ntcGseDecBbfChanLabelFilter": ntcGseDecBbfChanLabelFilter,
       "ntcGseDecBbfChanVirtualNetwork": ntcGseDecBbfChanVirtualNetwork,
       "ntcGseDecBbfChanAccessVlan": ntcGseDecBbfChanAccessVlan,
       "ntcGseDecIsisTable": ntcGseDecIsisTable,
       "ntcGseDecIsisEntry": ntcGseDecIsisEntry,
       "ntcGseDecIsisName": ntcGseDecIsisName,
       "ntcGseDecIsisRowStatus": ntcGseDecIsisRowStatus,
       "ntcGseDecIsiEnable": ntcGseDecIsiEnable,
       "ntcGseDecIsiIsi": ntcGseDecIsiIsi,
       "ntcGseDecIsiProtocol": ntcGseDecIsiProtocol,
       "ntcGseDecIsiInputTypeName": ntcGseDecIsiInputTypeName,
       "ntcGseDecIsiInputInstanceName": ntcGseDecIsiInputInstanceName,
       "ntcGseDecDefDecProt": ntcGseDecDefDecProt,
       "ntcGseDecXpeChecksum": ntcGseDecXpeChecksum,
       "ntcGseDecDestMacEnable": ntcGseDecDestMacEnable,
       "ntcGseDecDestMac": ntcGseDecDestMac,
       "ntcGseDecPidFilter": ntcGseDecPidFilter,
       "ntcGseDecConformance": ntcGseDecConformance,
       "ntcGseDecConfCompliance": ntcGseDecConfCompliance,
       "ntcGseDecConfCompV1Standard": ntcGseDecConfCompV1Standard,
       "ntcGseDecConfGroup": ntcGseDecConfGroup,
       "ntcGseDecConfGrpV1Standard": ntcGseDecConfGrpV1Standard}
)
