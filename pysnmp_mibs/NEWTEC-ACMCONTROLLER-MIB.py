# SNMP MIB module (NEWTEC-ACMCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ACMCONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:16 2025
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

ntcAcmController = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800)
)
if mibBuilder.loadTexts:
    ntcAcmController.setRevisions(
        ("2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-07-05 06:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAcmCtrlObjects_ObjectIdentity = ObjectIdentity
ntcAcmCtrlObjects = _NtcAcmCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlObjects.setStatus("current")


class _NtcAcmCtrlEnable_Type(Integer32):
    """Custom type ntcAcmCtrlEnable based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("monitoringOnly", 2))
    )


_NtcAcmCtrlEnable_Type.__name__ = "Integer32"
_NtcAcmCtrlEnable_Object = MibScalar
ntcAcmCtrlEnable = _NtcAcmCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 1),
    _NtcAcmCtrlEnable_Type()
)
ntcAcmCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlEnable.setStatus("current")


class _NtcAcmCtrlMode_Type(Integer32):
    """Custom type ntcAcmCtrlMode based on Integer32"""
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


_NtcAcmCtrlMode_Type.__name__ = "Integer32"
_NtcAcmCtrlMode_Object = MibScalar
ntcAcmCtrlMode = _NtcAcmCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 2),
    _NtcAcmCtrlMode_Type()
)
ntcAcmCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlMode.setStatus("current")


class _NtcAcmCtrlModCodAlgor_Type(Integer32):
    """Custom type ntcAcmCtrlModCodAlgor based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("headerEsno", 1),
          ("linkMargin", 2),
          ("linearCarrier", 3),
          ("nonLinearCarrier", 4),
          ("auto", 5))
    )


_NtcAcmCtrlModCodAlgor_Type.__name__ = "Integer32"
_NtcAcmCtrlModCodAlgor_Object = MibScalar
ntcAcmCtrlModCodAlgor = _NtcAcmCtrlModCodAlgor_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 3),
    _NtcAcmCtrlModCodAlgor_Type()
)
ntcAcmCtrlModCodAlgor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlModCodAlgor.setStatus("current")
_NtcAcmCtrlDvbS2_ObjectIdentity = ObjectIdentity
ntcAcmCtrlDvbS2 = _NtcAcmCtrlDvbS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlDvbS2.setStatus("current")


class _NtcAcmCtrlS2MinModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2MinModCod based on Integer32"""
    defaultValue = 0

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
        *(("unused", 0),
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


_NtcAcmCtrlS2MinModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2MinModCod_Object = MibScalar
ntcAcmCtrlS2MinModCod = _NtcAcmCtrlS2MinModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 1),
    _NtcAcmCtrlS2MinModCod_Type()
)
ntcAcmCtrlS2MinModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2MinModCod.setStatus("current")


class _NtcAcmCtrlS2MaxModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2MaxModCod based on Integer32"""
    defaultValue = 0

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
        *(("unused", 0),
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


_NtcAcmCtrlS2MaxModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2MaxModCod_Object = MibScalar
ntcAcmCtrlS2MaxModCod = _NtcAcmCtrlS2MaxModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 2),
    _NtcAcmCtrlS2MaxModCod_Type()
)
ntcAcmCtrlS2MaxModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2MaxModCod.setStatus("current")
_NtcAcmCtrlS2ModCodsTable_Object = MibTable
ntcAcmCtrlS2ModCodsTable = _NtcAcmCtrlS2ModCodsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ModCodsTable.setStatus("current")
_NtcAcmCtrlS2ModCodsEntry_Object = MibTableRow
ntcAcmCtrlS2ModCodsEntry = _NtcAcmCtrlS2ModCodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1)
)
ntcAcmCtrlS2ModCodsEntry.setIndexNames(
    (0, "NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ModCod"),
)
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ModCodsEntry.setStatus("current")


class _NtcAcmCtrlS2ModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2ModCod based on Integer32"""
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
        *(("unused", 0),
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


_NtcAcmCtrlS2ModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ModCod_Object = MibTableColumn
ntcAcmCtrlS2ModCod = _NtcAcmCtrlS2ModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1, 1),
    _NtcAcmCtrlS2ModCod_Type()
)
ntcAcmCtrlS2ModCod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ModCod.setStatus("current")


class _NtcAcmCtrlS2McEnable_Type(Integer32):
    """Custom type ntcAcmCtrlS2McEnable based on Integer32"""
    defaultValue = 1

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


_NtcAcmCtrlS2McEnable_Type.__name__ = "Integer32"
_NtcAcmCtrlS2McEnable_Object = MibTableColumn
ntcAcmCtrlS2McEnable = _NtcAcmCtrlS2McEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1, 2),
    _NtcAcmCtrlS2McEnable_Type()
)
ntcAcmCtrlS2McEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McEnable.setStatus("current")


class _NtcAcmCtrlS2McMinMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2McMinMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlS2McMinMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2McMinMargin_Object = MibTableColumn
ntcAcmCtrlS2McMinMargin = _NtcAcmCtrlS2McMinMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1, 3),
    _NtcAcmCtrlS2McMinMargin_Type()
)
ntcAcmCtrlS2McMinMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McMinMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McMinMargin.setUnits("dB")


class _NtcAcmCtrlS2McTargMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2McTargMargin based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlS2McTargMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2McTargMargin_Object = MibTableColumn
ntcAcmCtrlS2McTargMargin = _NtcAcmCtrlS2McTargMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1, 4),
    _NtcAcmCtrlS2McTargMargin_Type()
)
ntcAcmCtrlS2McTargMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McTargMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McTargMargin.setUnits("dB")


class _NtcAcmCtrlS2McDistMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2McDistMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_NtcAcmCtrlS2McDistMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2McDistMargin_Object = MibTableColumn
ntcAcmCtrlS2McDistMargin = _NtcAcmCtrlS2McDistMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 4, 3, 1, 5),
    _NtcAcmCtrlS2McDistMargin_Type()
)
ntcAcmCtrlS2McDistMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McDistMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2McDistMargin.setUnits("dB")
_NtcAcmCtrlS2Ext_ObjectIdentity = ObjectIdentity
ntcAcmCtrlS2Ext = _NtcAcmCtrlS2Ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlS2Ext.setStatus("current")


class _NtcAcmCtrlS2ExtMinModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMinModCod based on Integer32"""
    defaultValue = 0

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
              87)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("qpsk45180", 1),
          ("qpsk60180", 2),
          ("qpsk72180", 3),
          ("qpsk80180", 4),
          ("qpsk90180", 5),
          ("qpsk100180", 6),
          ("qpsk108180", 7),
          ("qpsk114180", 8),
          ("qpsk120180", 9),
          ("qpsk126180", 10),
          ("qpsk135180", 11),
          ("qpsk144180", 12),
          ("qpsk150180", 13),
          ("qpsk160180", 14),
          ("qpsk162180", 15),
          ("e8psk80180", 16),
          ("e8psk90180", 17),
          ("e8psk100180", 18),
          ("e8psk108180", 19),
          ("e8psk114180", 20),
          ("e8psk120180", 21),
          ("e8psk126180", 22),
          ("e8psk135180", 23),
          ("e8psk144180", 24),
          ("e8psk150180", 25),
          ("e16apsk80180", 26),
          ("e16apsk90180", 27),
          ("e16apsk100180", 28),
          ("e16apsk108180", 29),
          ("e16apsk114180", 30),
          ("e16apsk120180", 31),
          ("e16apsk126180", 32),
          ("e16apsk135180", 33),
          ("e16apsk144180", 34),
          ("e16apsk150180", 35),
          ("e16apsk160180", 36),
          ("e16apsk162180", 37),
          ("e32apsk100180", 38),
          ("e32apsk108180", 39),
          ("e32apsk114180", 40),
          ("e32apsk120180", 41),
          ("e32apsk126180", 42),
          ("e32apsk135180", 43),
          ("e32apsk144180", 44),
          ("e32apsk150180", 45),
          ("e32apsk160180", 46),
          ("e32apsk162180", 47),
          ("e64apsk90180", 48),
          ("e64apsk100180", 49),
          ("e64apsk108180", 50),
          ("e64apsk114180", 51),
          ("e64apsk120180", 52),
          ("e64apsk126180", 53),
          ("e64apsk135180", 54),
          ("e64apsk144180", 55),
          ("e64apsk150180", 56),
          ("e64apsk160180", 57),
          ("e64apsk162180", 58),
          ("e8pskl80180", 59),
          ("e8pskl90180", 60),
          ("e8pskl100180", 61),
          ("e8pskl108180", 62),
          ("e8pskl114180", 63),
          ("e8pskl120180", 64),
          ("e16apskl80180", 65),
          ("e16apskl90180", 66),
          ("e16apskl100180", 67),
          ("e16apskl108180", 68),
          ("e16apskl114180", 69),
          ("e16apskl120180", 70),
          ("e16apskl126180", 71),
          ("e16apskl135180", 72),
          ("e16apskl144180", 73),
          ("e16apskl150180", 74),
          ("e16apskl160180", 75),
          ("e16apskl162180", 76),
          ("e64apskl90180", 77),
          ("e64apskl100180", 78),
          ("e64apskl108180", 79),
          ("e64apskl114180", 80),
          ("e64apskl120180", 81),
          ("e64apskl126180", 82),
          ("e64apskl135180", 83),
          ("e64apskl144180", 84),
          ("e64apskl150180", 85),
          ("e64apskl160180", 86),
          ("e64apskl162180", 87))
    )


_NtcAcmCtrlS2ExtMinModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMinModCod_Object = MibScalar
ntcAcmCtrlS2ExtMinModCod = _NtcAcmCtrlS2ExtMinModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 1),
    _NtcAcmCtrlS2ExtMinModCod_Type()
)
ntcAcmCtrlS2ExtMinModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMinModCod.setStatus("current")


class _NtcAcmCtrlS2ExtMaxModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMaxModCod based on Integer32"""
    defaultValue = 0

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
              87)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("qpsk45180", 1),
          ("qpsk60180", 2),
          ("qpsk72180", 3),
          ("qpsk80180", 4),
          ("qpsk90180", 5),
          ("qpsk100180", 6),
          ("qpsk108180", 7),
          ("qpsk114180", 8),
          ("qpsk120180", 9),
          ("qpsk126180", 10),
          ("qpsk135180", 11),
          ("qpsk144180", 12),
          ("qpsk150180", 13),
          ("qpsk160180", 14),
          ("qpsk162180", 15),
          ("e8psk80180", 16),
          ("e8psk90180", 17),
          ("e8psk100180", 18),
          ("e8psk108180", 19),
          ("e8psk114180", 20),
          ("e8psk120180", 21),
          ("e8psk126180", 22),
          ("e8psk135180", 23),
          ("e8psk144180", 24),
          ("e8psk150180", 25),
          ("e16apsk80180", 26),
          ("e16apsk90180", 27),
          ("e16apsk100180", 28),
          ("e16apsk108180", 29),
          ("e16apsk114180", 30),
          ("e16apsk120180", 31),
          ("e16apsk126180", 32),
          ("e16apsk135180", 33),
          ("e16apsk144180", 34),
          ("e16apsk150180", 35),
          ("e16apsk160180", 36),
          ("e16apsk162180", 37),
          ("e32apsk100180", 38),
          ("e32apsk108180", 39),
          ("e32apsk114180", 40),
          ("e32apsk120180", 41),
          ("e32apsk126180", 42),
          ("e32apsk135180", 43),
          ("e32apsk144180", 44),
          ("e32apsk150180", 45),
          ("e32apsk160180", 46),
          ("e32apsk162180", 47),
          ("e64apsk90180", 48),
          ("e64apsk100180", 49),
          ("e64apsk108180", 50),
          ("e64apsk114180", 51),
          ("e64apsk120180", 52),
          ("e64apsk126180", 53),
          ("e64apsk135180", 54),
          ("e64apsk144180", 55),
          ("e64apsk150180", 56),
          ("e64apsk160180", 57),
          ("e64apsk162180", 58),
          ("e8pskl80180", 59),
          ("e8pskl90180", 60),
          ("e8pskl100180", 61),
          ("e8pskl108180", 62),
          ("e8pskl114180", 63),
          ("e8pskl120180", 64),
          ("e16apskl80180", 65),
          ("e16apskl90180", 66),
          ("e16apskl100180", 67),
          ("e16apskl108180", 68),
          ("e16apskl114180", 69),
          ("e16apskl120180", 70),
          ("e16apskl126180", 71),
          ("e16apskl135180", 72),
          ("e16apskl144180", 73),
          ("e16apskl150180", 74),
          ("e16apskl160180", 75),
          ("e16apskl162180", 76),
          ("e64apskl90180", 77),
          ("e64apskl100180", 78),
          ("e64apskl108180", 79),
          ("e64apskl114180", 80),
          ("e64apskl120180", 81),
          ("e64apskl126180", 82),
          ("e64apskl135180", 83),
          ("e64apskl144180", 84),
          ("e64apskl150180", 85),
          ("e64apskl160180", 86),
          ("e64apskl162180", 87))
    )


_NtcAcmCtrlS2ExtMaxModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMaxModCod_Object = MibScalar
ntcAcmCtrlS2ExtMaxModCod = _NtcAcmCtrlS2ExtMaxModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 2),
    _NtcAcmCtrlS2ExtMaxModCod_Type()
)
ntcAcmCtrlS2ExtMaxModCod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMaxModCod.setStatus("current")
_NtcAcmCtrlS2ExtModCodsTable_Object = MibTable
ntcAcmCtrlS2ExtModCodsTable = _NtcAcmCtrlS2ExtModCodsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtModCodsTable.setStatus("current")
_NtcAcmCtrlS2ExtModCodsEntry_Object = MibTableRow
ntcAcmCtrlS2ExtModCodsEntry = _NtcAcmCtrlS2ExtModCodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1)
)
ntcAcmCtrlS2ExtModCodsEntry.setIndexNames(
    (0, "NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtModCod"),
)
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtModCodsEntry.setStatus("current")


class _NtcAcmCtrlS2ExtModCod_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtModCod based on Integer32"""
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
              87)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("qpsk45180", 1),
          ("qpsk60180", 2),
          ("qpsk72180", 3),
          ("qpsk80180", 4),
          ("qpsk90180", 5),
          ("qpsk100180", 6),
          ("qpsk108180", 7),
          ("qpsk114180", 8),
          ("qpsk120180", 9),
          ("qpsk126180", 10),
          ("qpsk135180", 11),
          ("qpsk144180", 12),
          ("qpsk150180", 13),
          ("qpsk160180", 14),
          ("qpsk162180", 15),
          ("e8psk80180", 16),
          ("e8psk90180", 17),
          ("e8psk100180", 18),
          ("e8psk108180", 19),
          ("e8psk114180", 20),
          ("e8psk120180", 21),
          ("e8psk126180", 22),
          ("e8psk135180", 23),
          ("e8psk144180", 24),
          ("e8psk150180", 25),
          ("e16apsk80180", 26),
          ("e16apsk90180", 27),
          ("e16apsk100180", 28),
          ("e16apsk108180", 29),
          ("e16apsk114180", 30),
          ("e16apsk120180", 31),
          ("e16apsk126180", 32),
          ("e16apsk135180", 33),
          ("e16apsk144180", 34),
          ("e16apsk150180", 35),
          ("e16apsk160180", 36),
          ("e16apsk162180", 37),
          ("e32apsk100180", 38),
          ("e32apsk108180", 39),
          ("e32apsk114180", 40),
          ("e32apsk120180", 41),
          ("e32apsk126180", 42),
          ("e32apsk135180", 43),
          ("e32apsk144180", 44),
          ("e32apsk150180", 45),
          ("e32apsk160180", 46),
          ("e32apsk162180", 47),
          ("e64apsk90180", 48),
          ("e64apsk100180", 49),
          ("e64apsk108180", 50),
          ("e64apsk114180", 51),
          ("e64apsk120180", 52),
          ("e64apsk126180", 53),
          ("e64apsk135180", 54),
          ("e64apsk144180", 55),
          ("e64apsk150180", 56),
          ("e64apsk160180", 57),
          ("e64apsk162180", 58),
          ("e8pskl80180", 59),
          ("e8pskl90180", 60),
          ("e8pskl100180", 61),
          ("e8pskl108180", 62),
          ("e8pskl114180", 63),
          ("e8pskl120180", 64),
          ("e16apskl80180", 65),
          ("e16apskl90180", 66),
          ("e16apskl100180", 67),
          ("e16apskl108180", 68),
          ("e16apskl114180", 69),
          ("e16apskl120180", 70),
          ("e16apskl126180", 71),
          ("e16apskl135180", 72),
          ("e16apskl144180", 73),
          ("e16apskl150180", 74),
          ("e16apskl160180", 75),
          ("e16apskl162180", 76),
          ("e64apskl90180", 77),
          ("e64apskl100180", 78),
          ("e64apskl108180", 79),
          ("e64apskl114180", 80),
          ("e64apskl120180", 81),
          ("e64apskl126180", 82),
          ("e64apskl135180", 83),
          ("e64apskl144180", 84),
          ("e64apskl150180", 85),
          ("e64apskl160180", 86),
          ("e64apskl162180", 87))
    )


_NtcAcmCtrlS2ExtModCod_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtModCod_Object = MibTableColumn
ntcAcmCtrlS2ExtModCod = _NtcAcmCtrlS2ExtModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1, 1),
    _NtcAcmCtrlS2ExtModCod_Type()
)
ntcAcmCtrlS2ExtModCod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtModCod.setStatus("current")


class _NtcAcmCtrlS2ExtMcEnable_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMcEnable based on Integer32"""
    defaultValue = 1

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


_NtcAcmCtrlS2ExtMcEnable_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMcEnable_Object = MibTableColumn
ntcAcmCtrlS2ExtMcEnable = _NtcAcmCtrlS2ExtMcEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1, 2),
    _NtcAcmCtrlS2ExtMcEnable_Type()
)
ntcAcmCtrlS2ExtMcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcEnable.setStatus("current")


class _NtcAcmCtrlS2ExtMcMinMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMcMinMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlS2ExtMcMinMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMcMinMargin_Object = MibTableColumn
ntcAcmCtrlS2ExtMcMinMargin = _NtcAcmCtrlS2ExtMcMinMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1, 3),
    _NtcAcmCtrlS2ExtMcMinMargin_Type()
)
ntcAcmCtrlS2ExtMcMinMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcMinMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcMinMargin.setUnits("dB")


class _NtcAcmCtrlS2ExtMcTargMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMcTargMargin based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlS2ExtMcTargMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMcTargMargin_Object = MibTableColumn
ntcAcmCtrlS2ExtMcTargMargin = _NtcAcmCtrlS2ExtMcTargMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1, 4),
    _NtcAcmCtrlS2ExtMcTargMargin_Type()
)
ntcAcmCtrlS2ExtMcTargMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcTargMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcTargMargin.setUnits("dB")


class _NtcAcmCtrlS2ExtMcDistMargin_Type(Integer32):
    """Custom type ntcAcmCtrlS2ExtMcDistMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_NtcAcmCtrlS2ExtMcDistMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlS2ExtMcDistMargin_Object = MibTableColumn
ntcAcmCtrlS2ExtMcDistMargin = _NtcAcmCtrlS2ExtMcDistMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 5, 3, 1, 5),
    _NtcAcmCtrlS2ExtMcDistMargin_Type()
)
ntcAcmCtrlS2ExtMcDistMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcDistMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlS2ExtMcDistMargin.setUnits("dB")
_NtcAcmCtrlMon_ObjectIdentity = ObjectIdentity
ntcAcmCtrlMon = _NtcAcmCtrlMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 6)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlMon.setStatus("current")
_NtcAcmCtrlMonConfMsgCounter_Type = Unsigned32
_NtcAcmCtrlMonConfMsgCounter_Object = MibScalar
ntcAcmCtrlMonConfMsgCounter = _NtcAcmCtrlMonConfMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 6, 1),
    _NtcAcmCtrlMonConfMsgCounter_Type()
)
ntcAcmCtrlMonConfMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAcmCtrlMonConfMsgCounter.setStatus("current")
_NtcAcmCtrlFbAcceptedCounter_Type = Unsigned32
_NtcAcmCtrlFbAcceptedCounter_Object = MibScalar
ntcAcmCtrlFbAcceptedCounter = _NtcAcmCtrlFbAcceptedCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 6, 2),
    _NtcAcmCtrlFbAcceptedCounter_Type()
)
ntcAcmCtrlFbAcceptedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAcmCtrlFbAcceptedCounter.setStatus("current")
_NtcAcmCtrlFbDiscardedCounter_Type = Unsigned32
_NtcAcmCtrlFbDiscardedCounter_Object = MibScalar
ntcAcmCtrlFbDiscardedCounter = _NtcAcmCtrlFbDiscardedCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 6, 3),
    _NtcAcmCtrlFbDiscardedCounter_Type()
)
ntcAcmCtrlFbDiscardedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAcmCtrlFbDiscardedCounter.setStatus("current")


class _NtcAcmCtrlMonCounterReset_Type(Integer32):
    """Custom type ntcAcmCtrlMonCounterReset based on Integer32"""
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


_NtcAcmCtrlMonCounterReset_Type.__name__ = "Integer32"
_NtcAcmCtrlMonCounterReset_Object = MibScalar
ntcAcmCtrlMonCounterReset = _NtcAcmCtrlMonCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 6, 4),
    _NtcAcmCtrlMonCounterReset_Type()
)
ntcAcmCtrlMonCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlMonCounterReset.setStatus("current")


class _NtcAcmCtrlModcodTuning_Type(Integer32):
    """Custom type ntcAcmCtrlModcodTuning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_NtcAcmCtrlModcodTuning_Type.__name__ = "Integer32"
_NtcAcmCtrlModcodTuning_Object = MibScalar
ntcAcmCtrlModcodTuning = _NtcAcmCtrlModcodTuning_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 7),
    _NtcAcmCtrlModcodTuning_Type()
)
ntcAcmCtrlModcodTuning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlModcodTuning.setStatus("current")


class _NtcAcmCtrlMinMargin_Type(Integer32):
    """Custom type ntcAcmCtrlMinMargin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlMinMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlMinMargin_Object = MibScalar
ntcAcmCtrlMinMargin = _NtcAcmCtrlMinMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 8),
    _NtcAcmCtrlMinMargin_Type()
)
ntcAcmCtrlMinMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlMinMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlMinMargin.setUnits("dB")


class _NtcAcmCtrlTargetMargin_Type(Integer32):
    """Custom type ntcAcmCtrlTargetMargin based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcAcmCtrlTargetMargin_Type.__name__ = "Integer32"
_NtcAcmCtrlTargetMargin_Object = MibScalar
ntcAcmCtrlTargetMargin = _NtcAcmCtrlTargetMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 1, 9),
    _NtcAcmCtrlTargetMargin_Type()
)
ntcAcmCtrlTargetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAcmCtrlTargetMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcAcmCtrlTargetMargin.setUnits("dB")
_NtcAcmCtrlConformance_ObjectIdentity = ObjectIdentity
ntcAcmCtrlConformance = _NtcAcmCtrlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 2)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlConformance.setStatus("current")
_NtcAcmCtrlConfCompliance_ObjectIdentity = ObjectIdentity
ntcAcmCtrlConfCompliance = _NtcAcmCtrlConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlConfCompliance.setStatus("current")
_NtcAcmCtrlConfGroup_ObjectIdentity = ObjectIdentity
ntcAcmCtrlConfGroup = _NtcAcmCtrlConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAcmCtrlConfGroup.setStatus("current")

# Managed Objects groups

ntcAcmCtrlConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 2, 2, 1)
)
ntcAcmCtrlConfGrpV1Standard.setObjects(
      *(("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlEnable"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlMode"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlModCodAlgor"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2MinModCod"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2MaxModCod"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2McEnable"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2McMinMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2McTargMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2McDistMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMinModCod"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMaxModCod"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMcEnable"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMcMinMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMcTargMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlS2ExtMcDistMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlMonConfMsgCounter"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlFbAcceptedCounter"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlFbDiscardedCounter"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlMonCounterReset"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlModcodTuning"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlMinMargin"),
        ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlTargetMargin"))
)
if mibBuilder.loadTexts:
    ntcAcmCtrlConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAcmCtrlConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2800, 2, 1, 1)
)
ntcAcmCtrlConfCompV1Standard.setObjects(
    ("NEWTEC-ACMCONTROLLER-MIB", "ntcAcmCtrlConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAcmCtrlConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ACMCONTROLLER-MIB",
    **{"ntcAcmController": ntcAcmController,
       "ntcAcmCtrlObjects": ntcAcmCtrlObjects,
       "ntcAcmCtrlEnable": ntcAcmCtrlEnable,
       "ntcAcmCtrlMode": ntcAcmCtrlMode,
       "ntcAcmCtrlModCodAlgor": ntcAcmCtrlModCodAlgor,
       "ntcAcmCtrlDvbS2": ntcAcmCtrlDvbS2,
       "ntcAcmCtrlS2MinModCod": ntcAcmCtrlS2MinModCod,
       "ntcAcmCtrlS2MaxModCod": ntcAcmCtrlS2MaxModCod,
       "ntcAcmCtrlS2ModCodsTable": ntcAcmCtrlS2ModCodsTable,
       "ntcAcmCtrlS2ModCodsEntry": ntcAcmCtrlS2ModCodsEntry,
       "ntcAcmCtrlS2ModCod": ntcAcmCtrlS2ModCod,
       "ntcAcmCtrlS2McEnable": ntcAcmCtrlS2McEnable,
       "ntcAcmCtrlS2McMinMargin": ntcAcmCtrlS2McMinMargin,
       "ntcAcmCtrlS2McTargMargin": ntcAcmCtrlS2McTargMargin,
       "ntcAcmCtrlS2McDistMargin": ntcAcmCtrlS2McDistMargin,
       "ntcAcmCtrlS2Ext": ntcAcmCtrlS2Ext,
       "ntcAcmCtrlS2ExtMinModCod": ntcAcmCtrlS2ExtMinModCod,
       "ntcAcmCtrlS2ExtMaxModCod": ntcAcmCtrlS2ExtMaxModCod,
       "ntcAcmCtrlS2ExtModCodsTable": ntcAcmCtrlS2ExtModCodsTable,
       "ntcAcmCtrlS2ExtModCodsEntry": ntcAcmCtrlS2ExtModCodsEntry,
       "ntcAcmCtrlS2ExtModCod": ntcAcmCtrlS2ExtModCod,
       "ntcAcmCtrlS2ExtMcEnable": ntcAcmCtrlS2ExtMcEnable,
       "ntcAcmCtrlS2ExtMcMinMargin": ntcAcmCtrlS2ExtMcMinMargin,
       "ntcAcmCtrlS2ExtMcTargMargin": ntcAcmCtrlS2ExtMcTargMargin,
       "ntcAcmCtrlS2ExtMcDistMargin": ntcAcmCtrlS2ExtMcDistMargin,
       "ntcAcmCtrlMon": ntcAcmCtrlMon,
       "ntcAcmCtrlMonConfMsgCounter": ntcAcmCtrlMonConfMsgCounter,
       "ntcAcmCtrlFbAcceptedCounter": ntcAcmCtrlFbAcceptedCounter,
       "ntcAcmCtrlFbDiscardedCounter": ntcAcmCtrlFbDiscardedCounter,
       "ntcAcmCtrlMonCounterReset": ntcAcmCtrlMonCounterReset,
       "ntcAcmCtrlModcodTuning": ntcAcmCtrlModcodTuning,
       "ntcAcmCtrlMinMargin": ntcAcmCtrlMinMargin,
       "ntcAcmCtrlTargetMargin": ntcAcmCtrlTargetMargin,
       "ntcAcmCtrlConformance": ntcAcmCtrlConformance,
       "ntcAcmCtrlConfCompliance": ntcAcmCtrlConfCompliance,
       "ntcAcmCtrlConfCompV1Standard": ntcAcmCtrlConfCompV1Standard,
       "ntcAcmCtrlConfGroup": ntcAcmCtrlConfGroup,
       "ntcAcmCtrlConfGrpV1Standard": ntcAcmCtrlConfGrpV1Standard}
)
