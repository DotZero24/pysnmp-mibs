# SNMP MIB module (NEWTEC-MULTIACMCLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MULTIACMCLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:53 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcMultiAcmClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700)
)
if mibBuilder.loadTexts:
    ntcMultiAcmClient.setRevisions(
        ("2018-02-02 09:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-07-05 06:00",
         "2013-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcMltAcmClntObjects_ObjectIdentity = ObjectIdentity
ntcMltAcmClntObjects = _NtcMltAcmClntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntObjects.setStatus("current")
_NtcMltAcmClntCfgTable_Object = MibTable
ntcMltAcmClntCfgTable = _NtcMltAcmClntCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgTable.setStatus("current")
_NtcMltAcmClntCfgEntry_Object = MibTableRow
ntcMltAcmClntCfgEntry = _NtcMltAcmClntCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1)
)
ntcMltAcmClntCfgEntry.setIndexNames(
    (0, "NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntCfgDemodId"),
)
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgEntry.setStatus("current")


class _NtcMltAcmClntCfgDemodId_Type(Integer32):
    """Custom type ntcMltAcmClntCfgDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMltAcmClntCfgDemodId_Type.__name__ = "Integer32"
_NtcMltAcmClntCfgDemodId_Object = MibTableColumn
ntcMltAcmClntCfgDemodId = _NtcMltAcmClntCfgDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1, 1),
    _NtcMltAcmClntCfgDemodId_Type()
)
ntcMltAcmClntCfgDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgDemodId.setStatus("current")


class _NtcMltAcmClntCfgModCodAlgor_Type(Integer32):
    """Custom type ntcMltAcmClntCfgModCodAlgor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("headerEsno", 1),
          ("linkMargin", 2),
          ("linearCarrier", 3),
          ("nonLinearCarrier", 4),
          ("coND", 5))
    )


_NtcMltAcmClntCfgModCodAlgor_Type.__name__ = "Integer32"
_NtcMltAcmClntCfgModCodAlgor_Object = MibTableColumn
ntcMltAcmClntCfgModCodAlgor = _NtcMltAcmClntCfgModCodAlgor_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1, 2),
    _NtcMltAcmClntCfgModCodAlgor_Type()
)
ntcMltAcmClntCfgModCodAlgor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgModCodAlgor.setStatus("current")


class _NtcMltAcmClntCfgMDeltaMargin_Type(Integer32):
    """Custom type ntcMltAcmClntCfgMDeltaMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntCfgMDeltaMargin_Type.__name__ = "Integer32"
_NtcMltAcmClntCfgMDeltaMargin_Object = MibTableColumn
ntcMltAcmClntCfgMDeltaMargin = _NtcMltAcmClntCfgMDeltaMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1, 3),
    _NtcMltAcmClntCfgMDeltaMargin_Type()
)
ntcMltAcmClntCfgMDeltaMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgMDeltaMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgMDeltaMargin.setUnits("dB")


class _NtcMltAcmClntCfgRemoteTermId_Type(Unsigned32):
    """Custom type ntcMltAcmClntCfgRemoteTermId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65277),
    )


_NtcMltAcmClntCfgRemoteTermId_Type.__name__ = "Unsigned32"
_NtcMltAcmClntCfgRemoteTermId_Object = MibTableColumn
ntcMltAcmClntCfgRemoteTermId = _NtcMltAcmClntCfgRemoteTermId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1, 4),
    _NtcMltAcmClntCfgRemoteTermId_Type()
)
ntcMltAcmClntCfgRemoteTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgRemoteTermId.setStatus("current")


class _NtcMltAcmClntCfgMarginLogging_Type(Integer32):
    """Custom type ntcMltAcmClntCfgMarginLogging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcMltAcmClntCfgMarginLogging_Type.__name__ = "Integer32"
_NtcMltAcmClntCfgMarginLogging_Object = MibTableColumn
ntcMltAcmClntCfgMarginLogging = _NtcMltAcmClntCfgMarginLogging_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 1, 1, 5),
    _NtcMltAcmClntCfgMarginLogging_Type()
)
ntcMltAcmClntCfgMarginLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMltAcmClntCfgMarginLogging.setStatus("current")
_NtcMltAcmClntMonTable_Object = MibTable
ntcMltAcmClntMonTable = _NtcMltAcmClntMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntMonTable.setStatus("current")
_NtcMltAcmClntMonEntry_Object = MibTableRow
ntcMltAcmClntMonEntry = _NtcMltAcmClntMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1)
)
ntcMltAcmClntMonEntry.setIndexNames(
    (0, "NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonDemodId"),
)
if mibBuilder.loadTexts:
    ntcMltAcmClntMonEntry.setStatus("current")


class _NtcMltAcmClntMonDemodId_Type(Integer32):
    """Custom type ntcMltAcmClntMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMltAcmClntMonDemodId_Type.__name__ = "Integer32"
_NtcMltAcmClntMonDemodId_Object = MibTableColumn
ntcMltAcmClntMonDemodId = _NtcMltAcmClntMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 1),
    _NtcMltAcmClntMonDemodId_Type()
)
ntcMltAcmClntMonDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonDemodId.setStatus("current")


class _NtcMltAcmClntMonFadEstMg_Type(Integer32):
    """Custom type ntcMltAcmClntMonFadEstMg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntMonFadEstMg_Type.__name__ = "Integer32"
_NtcMltAcmClntMonFadEstMg_Object = MibTableColumn
ntcMltAcmClntMonFadEstMg = _NtcMltAcmClntMonFadEstMg_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 2),
    _NtcMltAcmClntMonFadEstMg_Type()
)
ntcMltAcmClntMonFadEstMg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonFadEstMg.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonFadEstMg.setUnits("dB")


class _NtcMltAcmClntMonShrtRefEsno_Type(Integer32):
    """Custom type ntcMltAcmClntMonShrtRefEsno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntMonShrtRefEsno_Type.__name__ = "Integer32"
_NtcMltAcmClntMonShrtRefEsno_Object = MibTableColumn
ntcMltAcmClntMonShrtRefEsno = _NtcMltAcmClntMonShrtRefEsno_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 3),
    _NtcMltAcmClntMonShrtRefEsno_Type()
)
ntcMltAcmClntMonShrtRefEsno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonShrtRefEsno.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonShrtRefEsno.setUnits("dB")


class _NtcMltAcmClntMonShrtReqModcod_Type(Integer32):
    """Custom type ntcMltAcmClntMonShrtReqModcod based on Integer32"""
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
        *(("noRequest", 0),
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


_NtcMltAcmClntMonShrtReqModcod_Type.__name__ = "Integer32"
_NtcMltAcmClntMonShrtReqModcod_Object = MibTableColumn
ntcMltAcmClntMonShrtReqModcod = _NtcMltAcmClntMonShrtReqModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 4),
    _NtcMltAcmClntMonShrtReqModcod_Type()
)
ntcMltAcmClntMonShrtReqModcod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonShrtReqModcod.setStatus("current")


class _NtcMltAcmClntMonShrtReqEsno_Type(Integer32):
    """Custom type ntcMltAcmClntMonShrtReqEsno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntMonShrtReqEsno_Type.__name__ = "Integer32"
_NtcMltAcmClntMonShrtReqEsno_Object = MibTableColumn
ntcMltAcmClntMonShrtReqEsno = _NtcMltAcmClntMonShrtReqEsno_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 5),
    _NtcMltAcmClntMonShrtReqEsno_Type()
)
ntcMltAcmClntMonShrtReqEsno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonShrtReqEsno.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonShrtReqEsno.setUnits("dB")


class _NtcMltAcmClntMonNrmlRefEsno_Type(Integer32):
    """Custom type ntcMltAcmClntMonNrmlRefEsno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntMonNrmlRefEsno_Type.__name__ = "Integer32"
_NtcMltAcmClntMonNrmlRefEsno_Object = MibTableColumn
ntcMltAcmClntMonNrmlRefEsno = _NtcMltAcmClntMonNrmlRefEsno_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 6),
    _NtcMltAcmClntMonNrmlRefEsno_Type()
)
ntcMltAcmClntMonNrmlRefEsno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonNrmlRefEsno.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonNrmlRefEsno.setUnits("dB")


class _NtcMltAcmClntMonNrmlReqModcod_Type(Integer32):
    """Custom type ntcMltAcmClntMonNrmlReqModcod based on Integer32"""
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
        *(("noRequest", 0),
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


_NtcMltAcmClntMonNrmlReqModcod_Type.__name__ = "Integer32"
_NtcMltAcmClntMonNrmlReqModcod_Object = MibTableColumn
ntcMltAcmClntMonNrmlReqModcod = _NtcMltAcmClntMonNrmlReqModcod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 7),
    _NtcMltAcmClntMonNrmlReqModcod_Type()
)
ntcMltAcmClntMonNrmlReqModcod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonNrmlReqModcod.setStatus("current")


class _NtcMltAcmClntMonNrmlReqEsno_Type(Integer32):
    """Custom type ntcMltAcmClntMonNrmlReqEsno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMltAcmClntMonNrmlReqEsno_Type.__name__ = "Integer32"
_NtcMltAcmClntMonNrmlReqEsno_Object = MibTableColumn
ntcMltAcmClntMonNrmlReqEsno = _NtcMltAcmClntMonNrmlReqEsno_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 2, 1, 8),
    _NtcMltAcmClntMonNrmlReqEsno_Type()
)
ntcMltAcmClntMonNrmlReqEsno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonNrmlReqEsno.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonNrmlReqEsno.setUnits("dB")
_NtcMltAcmClntMonErrStatsTable_Object = MibTable
ntcMltAcmClntMonErrStatsTable = _NtcMltAcmClntMonErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsTable.setStatus("current")
_NtcMltAcmClntMonErrStatsEntry_Object = MibTableRow
ntcMltAcmClntMonErrStatsEntry = _NtcMltAcmClntMonErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1)
)
ntcMltAcmClntMonErrStatsEntry.setIndexNames(
    (0, "NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonErrStatsStatCtr"),
)
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsEntry.setStatus("current")
_NtcMltAcmClntMonErrStatsStatCtr_Type = Unsigned32
_NtcMltAcmClntMonErrStatsStatCtr_Object = MibTableColumn
ntcMltAcmClntMonErrStatsStatCtr = _NtcMltAcmClntMonErrStatsStatCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1, 1),
    _NtcMltAcmClntMonErrStatsStatCtr_Type()
)
ntcMltAcmClntMonErrStatsStatCtr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsStatCtr.setStatus("current")


class _NtcMltAcmClntMonErrStatsDemodId_Type(Integer32):
    """Custom type ntcMltAcmClntMonErrStatsDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMltAcmClntMonErrStatsDemodId_Type.__name__ = "Integer32"
_NtcMltAcmClntMonErrStatsDemodId_Object = MibTableColumn
ntcMltAcmClntMonErrStatsDemodId = _NtcMltAcmClntMonErrStatsDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1, 2),
    _NtcMltAcmClntMonErrStatsDemodId_Type()
)
ntcMltAcmClntMonErrStatsDemodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsDemodId.setStatus("current")


class _NtcMltAcmClntMonErrStatsInterval_Type(Integer32):
    """Custom type ntcMltAcmClntMonErrStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("today", 0),
          ("e1dayago", 1),
          ("e2daysago", 2),
          ("e3daysago", 3),
          ("e4daysago", 4),
          ("e5daysago", 5))
    )


_NtcMltAcmClntMonErrStatsInterval_Type.__name__ = "Integer32"
_NtcMltAcmClntMonErrStatsInterval_Object = MibTableColumn
ntcMltAcmClntMonErrStatsInterval = _NtcMltAcmClntMonErrStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1, 3),
    _NtcMltAcmClntMonErrStatsInterval_Type()
)
ntcMltAcmClntMonErrStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsInterval.setStatus("current")
_NtcMltAcmClntMonErrStatsSec_Type = Counter32
_NtcMltAcmClntMonErrStatsSec_Object = MibTableColumn
ntcMltAcmClntMonErrStatsSec = _NtcMltAcmClntMonErrStatsSec_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1, 4),
    _NtcMltAcmClntMonErrStatsSec_Type()
)
ntcMltAcmClntMonErrStatsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsSec.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsSec.setUnits("s")
_NtcMltAcmClntMonErrStatsMtbe_Type = Counter32
_NtcMltAcmClntMonErrStatsMtbe_Object = MibTableColumn
ntcMltAcmClntMonErrStatsMtbe = _NtcMltAcmClntMonErrStatsMtbe_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 1, 3, 1, 5),
    _NtcMltAcmClntMonErrStatsMtbe_Type()
)
ntcMltAcmClntMonErrStatsMtbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsMtbe.setStatus("current")
if mibBuilder.loadTexts:
    ntcMltAcmClntMonErrStatsMtbe.setUnits("s")
_NtcMltAcmClntConformance_ObjectIdentity = ObjectIdentity
ntcMltAcmClntConformance = _NtcMltAcmClntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 2)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntConformance.setStatus("current")
_NtcMltAcmClntConfCompliance_ObjectIdentity = ObjectIdentity
ntcMltAcmClntConfCompliance = _NtcMltAcmClntConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 2, 1)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntConfCompliance.setStatus("current")
_NtcMltAcmClntConfGroup_ObjectIdentity = ObjectIdentity
ntcMltAcmClntConfGroup = _NtcMltAcmClntConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 2, 2)
)
if mibBuilder.loadTexts:
    ntcMltAcmClntConfGroup.setStatus("current")

# Managed Objects groups

ntcMltAcmClntConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 2, 2, 1)
)
ntcMltAcmClntConfGrpV1Standard.setObjects(
      *(("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntCfgModCodAlgor"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntCfgMDeltaMargin"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntCfgRemoteTermId"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntCfgMarginLogging"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonFadEstMg"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonShrtRefEsno"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonShrtReqModcod"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonShrtReqEsno"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonNrmlRefEsno"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonNrmlReqModcod"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonNrmlReqEsno"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonErrStatsDemodId"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonErrStatsInterval"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonErrStatsSec"),
        ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntMonErrStatsMtbe"))
)
if mibBuilder.loadTexts:
    ntcMltAcmClntConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcMltAcmClntConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4700, 2, 1, 1)
)
ntcMltAcmClntConfCompV1Standard.setObjects(
    ("NEWTEC-MULTIACMCLIENT-MIB", "ntcMltAcmClntConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcMltAcmClntConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MULTIACMCLIENT-MIB",
    **{"ntcMultiAcmClient": ntcMultiAcmClient,
       "ntcMltAcmClntObjects": ntcMltAcmClntObjects,
       "ntcMltAcmClntCfgTable": ntcMltAcmClntCfgTable,
       "ntcMltAcmClntCfgEntry": ntcMltAcmClntCfgEntry,
       "ntcMltAcmClntCfgDemodId": ntcMltAcmClntCfgDemodId,
       "ntcMltAcmClntCfgModCodAlgor": ntcMltAcmClntCfgModCodAlgor,
       "ntcMltAcmClntCfgMDeltaMargin": ntcMltAcmClntCfgMDeltaMargin,
       "ntcMltAcmClntCfgRemoteTermId": ntcMltAcmClntCfgRemoteTermId,
       "ntcMltAcmClntCfgMarginLogging": ntcMltAcmClntCfgMarginLogging,
       "ntcMltAcmClntMonTable": ntcMltAcmClntMonTable,
       "ntcMltAcmClntMonEntry": ntcMltAcmClntMonEntry,
       "ntcMltAcmClntMonDemodId": ntcMltAcmClntMonDemodId,
       "ntcMltAcmClntMonFadEstMg": ntcMltAcmClntMonFadEstMg,
       "ntcMltAcmClntMonShrtRefEsno": ntcMltAcmClntMonShrtRefEsno,
       "ntcMltAcmClntMonShrtReqModcod": ntcMltAcmClntMonShrtReqModcod,
       "ntcMltAcmClntMonShrtReqEsno": ntcMltAcmClntMonShrtReqEsno,
       "ntcMltAcmClntMonNrmlRefEsno": ntcMltAcmClntMonNrmlRefEsno,
       "ntcMltAcmClntMonNrmlReqModcod": ntcMltAcmClntMonNrmlReqModcod,
       "ntcMltAcmClntMonNrmlReqEsno": ntcMltAcmClntMonNrmlReqEsno,
       "ntcMltAcmClntMonErrStatsTable": ntcMltAcmClntMonErrStatsTable,
       "ntcMltAcmClntMonErrStatsEntry": ntcMltAcmClntMonErrStatsEntry,
       "ntcMltAcmClntMonErrStatsStatCtr": ntcMltAcmClntMonErrStatsStatCtr,
       "ntcMltAcmClntMonErrStatsDemodId": ntcMltAcmClntMonErrStatsDemodId,
       "ntcMltAcmClntMonErrStatsInterval": ntcMltAcmClntMonErrStatsInterval,
       "ntcMltAcmClntMonErrStatsSec": ntcMltAcmClntMonErrStatsSec,
       "ntcMltAcmClntMonErrStatsMtbe": ntcMltAcmClntMonErrStatsMtbe,
       "ntcMltAcmClntConformance": ntcMltAcmClntConformance,
       "ntcMltAcmClntConfCompliance": ntcMltAcmClntConfCompliance,
       "ntcMltAcmClntConfCompV1Standard": ntcMltAcmClntConfCompV1Standard,
       "ntcMltAcmClntConfGroup": ntcMltAcmClntConfGroup,
       "ntcMltAcmClntConfGrpV1Standard": ntcMltAcmClntConfGrpV1Standard}
)
