# SNMP MIB module (QTECH-AC-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AC-DOT11-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:09 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechAcDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65)
)
if mibBuilder.loadTexts:
    qtechAcDot11MIB.setRevisions(
        ("2009-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAcDot11MIBObjects_ObjectIdentity = ObjectIdentity
qtechAcDot11MIBObjects = _QtechAcDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1)
)
_QtechAcDot11LinkTestStaTable_Object = MibTable
qtechAcDot11LinkTestStaTable = _QtechAcDot11LinkTestStaTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 1)
)
if mibBuilder.loadTexts:
    qtechAcDot11LinkTestStaTable.setStatus("current")
_QtechAcDot11LinkTestStaEntry_Object = MibTableRow
qtechAcDot11LinkTestStaEntry = _QtechAcDot11LinkTestStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 1, 1)
)
qtechAcDot11LinkTestStaEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechAcDot11LinkMac"),
)
if mibBuilder.loadTexts:
    qtechAcDot11LinkTestStaEntry.setStatus("current")
_QtechAcDot11LinkMac_Type = MacAddress
_QtechAcDot11LinkMac_Object = MibTableColumn
qtechAcDot11LinkMac = _QtechAcDot11LinkMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 1, 1, 1),
    _QtechAcDot11LinkMac_Type()
)
qtechAcDot11LinkMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAcDot11LinkMac.setStatus("current")


class _QtechAcDot11Link_Type(DisplayString):
    """Custom type qtechAcDot11Link based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAcDot11Link_Type.__name__ = "DisplayString"
_QtechAcDot11Link_Object = MibTableColumn
qtechAcDot11Link = _QtechAcDot11Link_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 1, 1, 2),
    _QtechAcDot11Link_Type()
)
qtechAcDot11Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcDot11Link.setStatus("current")
_QtechAcDot11ShowClientTable_Object = MibTable
qtechAcDot11ShowClientTable = _QtechAcDot11ShowClientTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 2)
)
if mibBuilder.loadTexts:
    qtechAcDot11ShowClientTable.setStatus("current")
_QtechAcDot11ShowClientEntry_Object = MibTableRow
qtechAcDot11ShowClientEntry = _QtechAcDot11ShowClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 2, 1)
)
qtechAcDot11ShowClientEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechAcDot11ClientMac"),
)
if mibBuilder.loadTexts:
    qtechAcDot11ShowClientEntry.setStatus("current")
_QtechAcDot11ClientMac_Type = MacAddress
_QtechAcDot11ClientMac_Object = MibTableColumn
qtechAcDot11ClientMac = _QtechAcDot11ClientMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 2, 1, 1),
    _QtechAcDot11ClientMac_Type()
)
qtechAcDot11ClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAcDot11ClientMac.setStatus("current")


class _QtechAcDot11Client_Type(DisplayString):
    """Custom type qtechAcDot11Client based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechAcDot11Client_Type.__name__ = "DisplayString"
_QtechAcDot11Client_Object = MibTableColumn
qtechAcDot11Client = _QtechAcDot11Client_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 2, 1, 2),
    _QtechAcDot11Client_Type()
)
qtechAcDot11Client.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAcDot11Client.setStatus("current")
_QtechAcDot11AuthTimeout_Type = Integer32
_QtechAcDot11AuthTimeout_Object = MibScalar
qtechAcDot11AuthTimeout = _QtechAcDot11AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 3),
    _QtechAcDot11AuthTimeout_Type()
)
qtechAcDot11AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcDot11AuthTimeout.setStatus("current")
_QtechAcDot11CountryTable_Object = MibTable
qtechAcDot11CountryTable = _QtechAcDot11CountryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 4)
)
if mibBuilder.loadTexts:
    qtechAcDot11CountryTable.setStatus("current")
_QtechAcDot11CountryEntry_Object = MibTableRow
qtechAcDot11CountryEntry = _QtechAcDot11CountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 4, 1)
)
qtechAcDot11CountryEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechAcDot11CountryNum"),
)
if mibBuilder.loadTexts:
    qtechAcDot11CountryEntry.setStatus("current")
_QtechAcDot11CountryNum_Type = Integer32
_QtechAcDot11CountryNum_Object = MibTableColumn
qtechAcDot11CountryNum = _QtechAcDot11CountryNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 4, 1, 1),
    _QtechAcDot11CountryNum_Type()
)
qtechAcDot11CountryNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAcDot11CountryNum.setStatus("current")


class _QtechAcDot11Country_Type(DisplayString):
    """Custom type qtechAcDot11Country based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_QtechAcDot11Country_Type.__name__ = "DisplayString"
_QtechAcDot11Country_Object = MibTableColumn
qtechAcDot11Country = _QtechAcDot11Country_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 4, 1, 2),
    _QtechAcDot11Country_Type()
)
qtechAcDot11Country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcDot11Country.setStatus("current")
_QtechAcDot11CountryEnable_Type = TruthValue
_QtechAcDot11CountryEnable_Object = MibTableColumn
qtechAcDot11CountryEnable = _QtechAcDot11CountryEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 4, 1, 3),
    _QtechAcDot11CountryEnable_Type()
)
qtechAcDot11CountryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAcDot11CountryEnable.setStatus("current")


class _QtechNetDot11AEnable_Type(TruthValue):
    """Custom type qtechNetDot11AEnable based on TruthValue"""
    defaultValue = 1


_QtechNetDot11AEnable_Type.__name__ = "TruthValue"
_QtechNetDot11AEnable_Object = MibScalar
qtechNetDot11AEnable = _QtechNetDot11AEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 5),
    _QtechNetDot11AEnable_Type()
)
qtechNetDot11AEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AEnable.setStatus("current")
_QtechNetDot11AMCS0_Type = TruthValue
_QtechNetDot11AMCS0_Object = MibScalar
qtechNetDot11AMCS0 = _QtechNetDot11AMCS0_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 6),
    _QtechNetDot11AMCS0_Type()
)
qtechNetDot11AMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS0.setStatus("current")
_QtechNetDot11AMCS1_Type = TruthValue
_QtechNetDot11AMCS1_Object = MibScalar
qtechNetDot11AMCS1 = _QtechNetDot11AMCS1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 7),
    _QtechNetDot11AMCS1_Type()
)
qtechNetDot11AMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS1.setStatus("current")
_QtechNetDot11AMCS2_Type = TruthValue
_QtechNetDot11AMCS2_Object = MibScalar
qtechNetDot11AMCS2 = _QtechNetDot11AMCS2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 8),
    _QtechNetDot11AMCS2_Type()
)
qtechNetDot11AMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS2.setStatus("current")
_QtechNetDot11AMCS3_Type = TruthValue
_QtechNetDot11AMCS3_Object = MibScalar
qtechNetDot11AMCS3 = _QtechNetDot11AMCS3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 9),
    _QtechNetDot11AMCS3_Type()
)
qtechNetDot11AMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS3.setStatus("current")
_QtechNetDot11AMCS4_Type = TruthValue
_QtechNetDot11AMCS4_Object = MibScalar
qtechNetDot11AMCS4 = _QtechNetDot11AMCS4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 10),
    _QtechNetDot11AMCS4_Type()
)
qtechNetDot11AMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS4.setStatus("current")
_QtechNetDot11AMCS5_Type = TruthValue
_QtechNetDot11AMCS5_Object = MibScalar
qtechNetDot11AMCS5 = _QtechNetDot11AMCS5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 11),
    _QtechNetDot11AMCS5_Type()
)
qtechNetDot11AMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS5.setStatus("current")
_QtechNetDot11AMCS6_Type = TruthValue
_QtechNetDot11AMCS6_Object = MibScalar
qtechNetDot11AMCS6 = _QtechNetDot11AMCS6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 12),
    _QtechNetDot11AMCS6_Type()
)
qtechNetDot11AMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS6.setStatus("current")
_QtechNetDot11AMCS7_Type = TruthValue
_QtechNetDot11AMCS7_Object = MibScalar
qtechNetDot11AMCS7 = _QtechNetDot11AMCS7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 13),
    _QtechNetDot11AMCS7_Type()
)
qtechNetDot11AMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS7.setStatus("current")
_QtechNetDot11AMCS8_Type = TruthValue
_QtechNetDot11AMCS8_Object = MibScalar
qtechNetDot11AMCS8 = _QtechNetDot11AMCS8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 14),
    _QtechNetDot11AMCS8_Type()
)
qtechNetDot11AMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS8.setStatus("current")
_QtechNetDot11AMCS9_Type = TruthValue
_QtechNetDot11AMCS9_Object = MibScalar
qtechNetDot11AMCS9 = _QtechNetDot11AMCS9_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 15),
    _QtechNetDot11AMCS9_Type()
)
qtechNetDot11AMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS9.setStatus("current")
_QtechNetDot11AMCS10_Type = TruthValue
_QtechNetDot11AMCS10_Object = MibScalar
qtechNetDot11AMCS10 = _QtechNetDot11AMCS10_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 16),
    _QtechNetDot11AMCS10_Type()
)
qtechNetDot11AMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS10.setStatus("current")
_QtechNetDot11AMCS11_Type = TruthValue
_QtechNetDot11AMCS11_Object = MibScalar
qtechNetDot11AMCS11 = _QtechNetDot11AMCS11_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 17),
    _QtechNetDot11AMCS11_Type()
)
qtechNetDot11AMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS11.setStatus("current")
_QtechNetDot11AMCS12_Type = TruthValue
_QtechNetDot11AMCS12_Object = MibScalar
qtechNetDot11AMCS12 = _QtechNetDot11AMCS12_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 18),
    _QtechNetDot11AMCS12_Type()
)
qtechNetDot11AMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS12.setStatus("current")
_QtechNetDot11AMCS13_Type = TruthValue
_QtechNetDot11AMCS13_Object = MibScalar
qtechNetDot11AMCS13 = _QtechNetDot11AMCS13_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 19),
    _QtechNetDot11AMCS13_Type()
)
qtechNetDot11AMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS13.setStatus("current")
_QtechNetDot11AMCS14_Type = TruthValue
_QtechNetDot11AMCS14_Object = MibScalar
qtechNetDot11AMCS14 = _QtechNetDot11AMCS14_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 20),
    _QtechNetDot11AMCS14_Type()
)
qtechNetDot11AMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS14.setStatus("current")
_QtechNetDot11AMCS15_Type = TruthValue
_QtechNetDot11AMCS15_Object = MibScalar
qtechNetDot11AMCS15 = _QtechNetDot11AMCS15_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 21),
    _QtechNetDot11AMCS15_Type()
)
qtechNetDot11AMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AMCS15.setStatus("current")


class _QtechNetDot11AAMPDU_Type(Integer32):
    """Custom type qtechNetDot11AAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechNetDot11AAMPDU_Type.__name__ = "Integer32"
_QtechNetDot11AAMPDU_Object = MibScalar
qtechNetDot11AAMPDU = _QtechNetDot11AAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 22),
    _QtechNetDot11AAMPDU_Type()
)
qtechNetDot11AAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AAMPDU.setStatus("current")


class _QtechNetDot11BEnable_Type(TruthValue):
    """Custom type qtechNetDot11BEnable based on TruthValue"""
    defaultValue = 1


_QtechNetDot11BEnable_Type.__name__ = "TruthValue"
_QtechNetDot11BEnable_Object = MibScalar
qtechNetDot11BEnable = _QtechNetDot11BEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 23),
    _QtechNetDot11BEnable_Type()
)
qtechNetDot11BEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BEnable.setStatus("current")


class _QtechNetDot11BMCS0_Type(Integer32):
    """Custom type qtechNetDot11BMCS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS0_Type.__name__ = "Integer32"
_QtechNetDot11BMCS0_Object = MibScalar
qtechNetDot11BMCS0 = _QtechNetDot11BMCS0_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 24),
    _QtechNetDot11BMCS0_Type()
)
qtechNetDot11BMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS0.setStatus("current")


class _QtechNetDot11BMCS1_Type(Integer32):
    """Custom type qtechNetDot11BMCS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS1_Type.__name__ = "Integer32"
_QtechNetDot11BMCS1_Object = MibScalar
qtechNetDot11BMCS1 = _QtechNetDot11BMCS1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 25),
    _QtechNetDot11BMCS1_Type()
)
qtechNetDot11BMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS1.setStatus("current")


class _QtechNetDot11BMCS2_Type(Integer32):
    """Custom type qtechNetDot11BMCS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS2_Type.__name__ = "Integer32"
_QtechNetDot11BMCS2_Object = MibScalar
qtechNetDot11BMCS2 = _QtechNetDot11BMCS2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 26),
    _QtechNetDot11BMCS2_Type()
)
qtechNetDot11BMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS2.setStatus("current")


class _QtechNetDot11BMCS3_Type(Integer32):
    """Custom type qtechNetDot11BMCS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS3_Type.__name__ = "Integer32"
_QtechNetDot11BMCS3_Object = MibScalar
qtechNetDot11BMCS3 = _QtechNetDot11BMCS3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 27),
    _QtechNetDot11BMCS3_Type()
)
qtechNetDot11BMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS3.setStatus("current")


class _QtechNetDot11BMCS4_Type(Integer32):
    """Custom type qtechNetDot11BMCS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS4_Type.__name__ = "Integer32"
_QtechNetDot11BMCS4_Object = MibScalar
qtechNetDot11BMCS4 = _QtechNetDot11BMCS4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 28),
    _QtechNetDot11BMCS4_Type()
)
qtechNetDot11BMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS4.setStatus("current")


class _QtechNetDot11BMCS5_Type(Integer32):
    """Custom type qtechNetDot11BMCS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS5_Type.__name__ = "Integer32"
_QtechNetDot11BMCS5_Object = MibScalar
qtechNetDot11BMCS5 = _QtechNetDot11BMCS5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 29),
    _QtechNetDot11BMCS5_Type()
)
qtechNetDot11BMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS5.setStatus("current")


class _QtechNetDot11BMCS6_Type(Integer32):
    """Custom type qtechNetDot11BMCS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS6_Type.__name__ = "Integer32"
_QtechNetDot11BMCS6_Object = MibScalar
qtechNetDot11BMCS6 = _QtechNetDot11BMCS6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 30),
    _QtechNetDot11BMCS6_Type()
)
qtechNetDot11BMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS6.setStatus("current")


class _QtechNetDot11BMCS7_Type(Integer32):
    """Custom type qtechNetDot11BMCS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS7_Type.__name__ = "Integer32"
_QtechNetDot11BMCS7_Object = MibScalar
qtechNetDot11BMCS7 = _QtechNetDot11BMCS7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 31),
    _QtechNetDot11BMCS7_Type()
)
qtechNetDot11BMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS7.setStatus("current")


class _QtechNetDot11BMCS8_Type(Integer32):
    """Custom type qtechNetDot11BMCS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS8_Type.__name__ = "Integer32"
_QtechNetDot11BMCS8_Object = MibScalar
qtechNetDot11BMCS8 = _QtechNetDot11BMCS8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 32),
    _QtechNetDot11BMCS8_Type()
)
qtechNetDot11BMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS8.setStatus("current")


class _QtechNetDot11BMCS9_Type(Integer32):
    """Custom type qtechNetDot11BMCS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS9_Type.__name__ = "Integer32"
_QtechNetDot11BMCS9_Object = MibScalar
qtechNetDot11BMCS9 = _QtechNetDot11BMCS9_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 33),
    _QtechNetDot11BMCS9_Type()
)
qtechNetDot11BMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS9.setStatus("current")


class _QtechNetDot11BMCS10_Type(Integer32):
    """Custom type qtechNetDot11BMCS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS10_Type.__name__ = "Integer32"
_QtechNetDot11BMCS10_Object = MibScalar
qtechNetDot11BMCS10 = _QtechNetDot11BMCS10_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 34),
    _QtechNetDot11BMCS10_Type()
)
qtechNetDot11BMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS10.setStatus("current")


class _QtechNetDot11BMCS11_Type(Integer32):
    """Custom type qtechNetDot11BMCS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS11_Type.__name__ = "Integer32"
_QtechNetDot11BMCS11_Object = MibScalar
qtechNetDot11BMCS11 = _QtechNetDot11BMCS11_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 35),
    _QtechNetDot11BMCS11_Type()
)
qtechNetDot11BMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS11.setStatus("current")


class _QtechNetDot11BMCS12_Type(Integer32):
    """Custom type qtechNetDot11BMCS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS12_Type.__name__ = "Integer32"
_QtechNetDot11BMCS12_Object = MibScalar
qtechNetDot11BMCS12 = _QtechNetDot11BMCS12_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 36),
    _QtechNetDot11BMCS12_Type()
)
qtechNetDot11BMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS12.setStatus("current")


class _QtechNetDot11BMCS13_Type(Integer32):
    """Custom type qtechNetDot11BMCS13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS13_Type.__name__ = "Integer32"
_QtechNetDot11BMCS13_Object = MibScalar
qtechNetDot11BMCS13 = _QtechNetDot11BMCS13_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 37),
    _QtechNetDot11BMCS13_Type()
)
qtechNetDot11BMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS13.setStatus("current")


class _QtechNetDot11BMCS14_Type(Integer32):
    """Custom type qtechNetDot11BMCS14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS14_Type.__name__ = "Integer32"
_QtechNetDot11BMCS14_Object = MibScalar
qtechNetDot11BMCS14 = _QtechNetDot11BMCS14_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 38),
    _QtechNetDot11BMCS14_Type()
)
qtechNetDot11BMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS14.setStatus("current")


class _QtechNetDot11BMCS15_Type(Integer32):
    """Custom type qtechNetDot11BMCS15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechNetDot11BMCS15_Type.__name__ = "Integer32"
_QtechNetDot11BMCS15_Object = MibScalar
qtechNetDot11BMCS15 = _QtechNetDot11BMCS15_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 39),
    _QtechNetDot11BMCS15_Type()
)
qtechNetDot11BMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BMCS15.setStatus("current")


class _QtechNetDot11BAMPDU_Type(Integer32):
    """Custom type qtechNetDot11BAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechNetDot11BAMPDU_Type.__name__ = "Integer32"
_QtechNetDot11BAMPDU_Object = MibScalar
qtechNetDot11BAMPDU = _QtechNetDot11BAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 40),
    _QtechNetDot11BAMPDU_Type()
)
qtechNetDot11BAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BAMPDU.setStatus("current")


class _QtechNetDot11AGEnable_Type(TruthValue):
    """Custom type qtechNetDot11AGEnable based on TruthValue"""
    defaultValue = 1


_QtechNetDot11AGEnable_Type.__name__ = "TruthValue"
_QtechNetDot11AGEnable_Object = MibScalar
qtechNetDot11AGEnable = _QtechNetDot11AGEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 41),
    _QtechNetDot11AGEnable_Type()
)
qtechNetDot11AGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11AGEnable.setStatus("current")


class _QtechNetDot11BGEnable_Type(TruthValue):
    """Custom type qtechNetDot11BGEnable based on TruthValue"""
    defaultValue = 1


_QtechNetDot11BGEnable_Type.__name__ = "TruthValue"
_QtechNetDot11BGEnable_Object = MibScalar
qtechNetDot11BGEnable = _QtechNetDot11BGEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 1, 42),
    _QtechNetDot11BGEnable_Type()
)
qtechNetDot11BGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNetDot11BGEnable.setStatus("current")
_QtechApDot11MIBObjects_ObjectIdentity = ObjectIdentity
qtechApDot11MIBObjects = _QtechApDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2)
)
_QtechApDot11PoeTable_Object = MibTable
qtechApDot11PoeTable = _QtechApDot11PoeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 1)
)
if mibBuilder.loadTexts:
    qtechApDot11PoeTable.setStatus("current")
_QtechApDot11PoeEntry_Object = MibTableRow
qtechApDot11PoeEntry = _QtechApDot11PoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 1, 1)
)
qtechApDot11PoeEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechApDot11PoeAPID"),
)
if mibBuilder.loadTexts:
    qtechApDot11PoeEntry.setStatus("current")
_QtechApDot11PoeAPID_Type = TruthValue
_QtechApDot11PoeAPID_Object = MibTableColumn
qtechApDot11PoeAPID = _QtechApDot11PoeAPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 1, 1, 1),
    _QtechApDot11PoeAPID_Type()
)
qtechApDot11PoeAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApDot11PoeAPID.setStatus("current")
_QtechApDot11PoeEnable_Type = TruthValue
_QtechApDot11PoeEnable_Object = MibTableColumn
qtechApDot11PoeEnable = _QtechApDot11PoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 1, 1, 2),
    _QtechApDot11PoeEnable_Type()
)
qtechApDot11PoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11PoeEnable.setStatus("current")
_QtechApDot11ChannelTable_Object = MibTable
qtechApDot11ChannelTable = _QtechApDot11ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 2)
)
if mibBuilder.loadTexts:
    qtechApDot11ChannelTable.setStatus("current")
_QtechApDot11ChannelEntry_Object = MibTableRow
qtechApDot11ChannelEntry = _QtechApDot11ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 2, 1)
)
qtechApDot11ChannelEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechApDot11ChannelAPID"),
)
if mibBuilder.loadTexts:
    qtechApDot11ChannelEntry.setStatus("current")
_QtechApDot11ChannelAPID_Type = Integer32
_QtechApDot11ChannelAPID_Object = MibTableColumn
qtechApDot11ChannelAPID = _QtechApDot11ChannelAPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 2, 1, 1),
    _QtechApDot11ChannelAPID_Type()
)
qtechApDot11ChannelAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApDot11ChannelAPID.setStatus("current")


class _QtechApDot11ChannelWidthA_Type(Integer32):
    """Custom type qtechApDot11ChannelWidthA based on Integer32"""
    defaultValue = 20


_QtechApDot11ChannelWidthA_Type.__name__ = "Integer32"
_QtechApDot11ChannelWidthA_Object = MibTableColumn
qtechApDot11ChannelWidthA = _QtechApDot11ChannelWidthA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 2, 1, 2),
    _QtechApDot11ChannelWidthA_Type()
)
qtechApDot11ChannelWidthA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11ChannelWidthA.setStatus("current")


class _QtechApDot11ChannelWidthB_Type(Integer32):
    """Custom type qtechApDot11ChannelWidthB based on Integer32"""
    defaultValue = 20


_QtechApDot11ChannelWidthB_Type.__name__ = "Integer32"
_QtechApDot11ChannelWidthB_Object = MibTableColumn
qtechApDot11ChannelWidthB = _QtechApDot11ChannelWidthB_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 2, 1, 3),
    _QtechApDot11ChannelWidthB_Type()
)
qtechApDot11ChannelWidthB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11ChannelWidthB.setStatus("current")
_QtechApDot11AntenneTable_Object = MibTable
qtechApDot11AntenneTable = _QtechApDot11AntenneTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3)
)
if mibBuilder.loadTexts:
    qtechApDot11AntenneTable.setStatus("current")
_QtechApDot11AntenneEntry_Object = MibTableRow
qtechApDot11AntenneEntry = _QtechApDot11AntenneEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1)
)
qtechApDot11AntenneEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechApDot11AntenneAPID"),
)
if mibBuilder.loadTexts:
    qtechApDot11AntenneEntry.setStatus("current")
_QtechApDot11AntenneAPID_Type = Integer32
_QtechApDot11AntenneAPID_Object = MibTableColumn
qtechApDot11AntenneAPID = _QtechApDot11AntenneAPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1, 1),
    _QtechApDot11AntenneAPID_Type()
)
qtechApDot11AntenneAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApDot11AntenneAPID.setStatus("current")


class _QtechApDot11AntenneRxA_Type(Integer32):
    """Custom type qtechApDot11AntenneRxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechApDot11AntenneRxA_Type.__name__ = "Integer32"
_QtechApDot11AntenneRxA_Object = MibTableColumn
qtechApDot11AntenneRxA = _QtechApDot11AntenneRxA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1, 2),
    _QtechApDot11AntenneRxA_Type()
)
qtechApDot11AntenneRxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11AntenneRxA.setStatus("current")


class _QtechApDot11AntenneTxA_Type(Integer32):
    """Custom type qtechApDot11AntenneTxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechApDot11AntenneTxA_Type.__name__ = "Integer32"
_QtechApDot11AntenneTxA_Object = MibTableColumn
qtechApDot11AntenneTxA = _QtechApDot11AntenneTxA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1, 3),
    _QtechApDot11AntenneTxA_Type()
)
qtechApDot11AntenneTxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11AntenneTxA.setStatus("current")


class _QtechApDot11AntenneRxB_Type(Integer32):
    """Custom type qtechApDot11AntenneRxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechApDot11AntenneRxB_Type.__name__ = "Integer32"
_QtechApDot11AntenneRxB_Object = MibTableColumn
qtechApDot11AntenneRxB = _QtechApDot11AntenneRxB_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1, 4),
    _QtechApDot11AntenneRxB_Type()
)
qtechApDot11AntenneRxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11AntenneRxB.setStatus("current")


class _QtechApDot11AntenneTxB_Type(Integer32):
    """Custom type qtechApDot11AntenneTxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechApDot11AntenneTxB_Type.__name__ = "Integer32"
_QtechApDot11AntenneTxB_Object = MibTableColumn
qtechApDot11AntenneTxB = _QtechApDot11AntenneTxB_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 2, 3, 1, 5),
    _QtechApDot11AntenneTxB_Type()
)
qtechApDot11AntenneTxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApDot11AntenneTxB.setStatus("current")
_QtechWlanDot11MIBObjects_ObjectIdentity = ObjectIdentity
qtechWlanDot11MIBObjects = _QtechWlanDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3)
)
_QtechWlanDot11LoadTable_Object = MibTable
qtechWlanDot11LoadTable = _QtechWlanDot11LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1)
)
if mibBuilder.loadTexts:
    qtechWlanDot11LoadTable.setStatus("current")
_QtechWlanDot11LoadTEntry_Object = MibTableRow
qtechWlanDot11LoadTEntry = _QtechWlanDot11LoadTEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1, 1)
)
qtechWlanDot11LoadTEntry.setIndexNames(
    (0, "QTECH-AC-DOT11-MIB", "qtechWlanDot11WlanId"),
)
if mibBuilder.loadTexts:
    qtechWlanDot11LoadTEntry.setStatus("current")
_QtechWlanDot11WlanId_Type = Integer32
_QtechWlanDot11WlanId_Object = MibTableColumn
qtechWlanDot11WlanId = _QtechWlanDot11WlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1, 1, 1),
    _QtechWlanDot11WlanId_Type()
)
qtechWlanDot11WlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechWlanDot11WlanId.setStatus("current")


class _QtechWlanDot11Enable_Type(TruthValue):
    """Custom type qtechWlanDot11Enable based on TruthValue"""
    defaultValue = 2


_QtechWlanDot11Enable_Type.__name__ = "TruthValue"
_QtechWlanDot11Enable_Object = MibTableColumn
qtechWlanDot11Enable = _QtechWlanDot11Enable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1, 1, 2),
    _QtechWlanDot11Enable_Type()
)
qtechWlanDot11Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanDot11Enable.setStatus("current")


class _QtechWlanDot11Window_Type(Integer32):
    """Custom type qtechWlanDot11Window based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_QtechWlanDot11Window_Type.__name__ = "Integer32"
_QtechWlanDot11Window_Object = MibTableColumn
qtechWlanDot11Window = _QtechWlanDot11Window_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1, 1, 3),
    _QtechWlanDot11Window_Type()
)
qtechWlanDot11Window.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanDot11Window.setStatus("current")


class _QtechWlanDot11Flow_Type(Integer32):
    """Custom type qtechWlanDot11Flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 130),
    )


_QtechWlanDot11Flow_Type.__name__ = "Integer32"
_QtechWlanDot11Flow_Object = MibTableColumn
qtechWlanDot11Flow = _QtechWlanDot11Flow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 3, 1, 1, 4),
    _QtechWlanDot11Flow_Type()
)
qtechWlanDot11Flow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlanDot11Flow.setStatus("current")
_QtechAcDot11MIBConformance_ObjectIdentity = ObjectIdentity
qtechAcDot11MIBConformance = _QtechAcDot11MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 5)
)
_QtechAcDot11MIBCompliances_ObjectIdentity = ObjectIdentity
qtechAcDot11MIBCompliances = _QtechAcDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 5, 1)
)
_QtechAcDot11MIBGroups_ObjectIdentity = ObjectIdentity
qtechAcDot11MIBGroups = _QtechAcDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 5, 2)
)

# Managed Objects groups

qtechAcDot11MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 5, 2, 1)
)
qtechAcDot11MIBGroup.setObjects(
      *(("QTECH-AC-DOT11-MIB", "qtechAcDot11Link"),
        ("QTECH-AC-DOT11-MIB", "qtechAcDot11Client"),
        ("QTECH-AC-DOT11-MIB", "qtechAcDot11AuthTimeout"),
        ("QTECH-AC-DOT11-MIB", "qtechAcDot11Country"),
        ("QTECH-AC-DOT11-MIB", "qtechAcDot11CountryEnable"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11PoeEnable"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11ChannelWidthA"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11ChannelWidthB"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11AntenneRxA"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11AntenneTxA"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11AntenneRxB"),
        ("QTECH-AC-DOT11-MIB", "qtechApDot11AntenneTxB"),
        ("QTECH-AC-DOT11-MIB", "qtechWlanDot11Enable"),
        ("QTECH-AC-DOT11-MIB", "qtechWlanDot11Window"),
        ("QTECH-AC-DOT11-MIB", "qtechWlanDot11Flow"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AEnable"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS0"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS1"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS2"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS3"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS4"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS5"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS6"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS7"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS8"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS9"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS10"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS11"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS12"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS13"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS14"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AMCS15"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AAMPDU"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BEnable"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS0"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS1"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS2"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS3"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS4"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS5"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS6"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS7"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS8"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS9"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS10"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS11"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS12"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS13"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS14"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BMCS15"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BAMPDU"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11AGEnable"),
        ("QTECH-AC-DOT11-MIB", "qtechNetDot11BGEnable"))
)
if mibBuilder.loadTexts:
    qtechAcDot11MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechAcDot11MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 65, 5, 1, 1)
)
qtechAcDot11MIBCompliance.setObjects(
    ("QTECH-AC-DOT11-MIB", "qtechAcDot11MIBGroup")
)
if mibBuilder.loadTexts:
    qtechAcDot11MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AC-DOT11-MIB",
    **{"qtechAcDot11MIB": qtechAcDot11MIB,
       "qtechAcDot11MIBObjects": qtechAcDot11MIBObjects,
       "qtechAcDot11LinkTestStaTable": qtechAcDot11LinkTestStaTable,
       "qtechAcDot11LinkTestStaEntry": qtechAcDot11LinkTestStaEntry,
       "qtechAcDot11LinkMac": qtechAcDot11LinkMac,
       "qtechAcDot11Link": qtechAcDot11Link,
       "qtechAcDot11ShowClientTable": qtechAcDot11ShowClientTable,
       "qtechAcDot11ShowClientEntry": qtechAcDot11ShowClientEntry,
       "qtechAcDot11ClientMac": qtechAcDot11ClientMac,
       "qtechAcDot11Client": qtechAcDot11Client,
       "qtechAcDot11AuthTimeout": qtechAcDot11AuthTimeout,
       "qtechAcDot11CountryTable": qtechAcDot11CountryTable,
       "qtechAcDot11CountryEntry": qtechAcDot11CountryEntry,
       "qtechAcDot11CountryNum": qtechAcDot11CountryNum,
       "qtechAcDot11Country": qtechAcDot11Country,
       "qtechAcDot11CountryEnable": qtechAcDot11CountryEnable,
       "qtechNetDot11AEnable": qtechNetDot11AEnable,
       "qtechNetDot11AMCS0": qtechNetDot11AMCS0,
       "qtechNetDot11AMCS1": qtechNetDot11AMCS1,
       "qtechNetDot11AMCS2": qtechNetDot11AMCS2,
       "qtechNetDot11AMCS3": qtechNetDot11AMCS3,
       "qtechNetDot11AMCS4": qtechNetDot11AMCS4,
       "qtechNetDot11AMCS5": qtechNetDot11AMCS5,
       "qtechNetDot11AMCS6": qtechNetDot11AMCS6,
       "qtechNetDot11AMCS7": qtechNetDot11AMCS7,
       "qtechNetDot11AMCS8": qtechNetDot11AMCS8,
       "qtechNetDot11AMCS9": qtechNetDot11AMCS9,
       "qtechNetDot11AMCS10": qtechNetDot11AMCS10,
       "qtechNetDot11AMCS11": qtechNetDot11AMCS11,
       "qtechNetDot11AMCS12": qtechNetDot11AMCS12,
       "qtechNetDot11AMCS13": qtechNetDot11AMCS13,
       "qtechNetDot11AMCS14": qtechNetDot11AMCS14,
       "qtechNetDot11AMCS15": qtechNetDot11AMCS15,
       "qtechNetDot11AAMPDU": qtechNetDot11AAMPDU,
       "qtechNetDot11BEnable": qtechNetDot11BEnable,
       "qtechNetDot11BMCS0": qtechNetDot11BMCS0,
       "qtechNetDot11BMCS1": qtechNetDot11BMCS1,
       "qtechNetDot11BMCS2": qtechNetDot11BMCS2,
       "qtechNetDot11BMCS3": qtechNetDot11BMCS3,
       "qtechNetDot11BMCS4": qtechNetDot11BMCS4,
       "qtechNetDot11BMCS5": qtechNetDot11BMCS5,
       "qtechNetDot11BMCS6": qtechNetDot11BMCS6,
       "qtechNetDot11BMCS7": qtechNetDot11BMCS7,
       "qtechNetDot11BMCS8": qtechNetDot11BMCS8,
       "qtechNetDot11BMCS9": qtechNetDot11BMCS9,
       "qtechNetDot11BMCS10": qtechNetDot11BMCS10,
       "qtechNetDot11BMCS11": qtechNetDot11BMCS11,
       "qtechNetDot11BMCS12": qtechNetDot11BMCS12,
       "qtechNetDot11BMCS13": qtechNetDot11BMCS13,
       "qtechNetDot11BMCS14": qtechNetDot11BMCS14,
       "qtechNetDot11BMCS15": qtechNetDot11BMCS15,
       "qtechNetDot11BAMPDU": qtechNetDot11BAMPDU,
       "qtechNetDot11AGEnable": qtechNetDot11AGEnable,
       "qtechNetDot11BGEnable": qtechNetDot11BGEnable,
       "qtechApDot11MIBObjects": qtechApDot11MIBObjects,
       "qtechApDot11PoeTable": qtechApDot11PoeTable,
       "qtechApDot11PoeEntry": qtechApDot11PoeEntry,
       "qtechApDot11PoeAPID": qtechApDot11PoeAPID,
       "qtechApDot11PoeEnable": qtechApDot11PoeEnable,
       "qtechApDot11ChannelTable": qtechApDot11ChannelTable,
       "qtechApDot11ChannelEntry": qtechApDot11ChannelEntry,
       "qtechApDot11ChannelAPID": qtechApDot11ChannelAPID,
       "qtechApDot11ChannelWidthA": qtechApDot11ChannelWidthA,
       "qtechApDot11ChannelWidthB": qtechApDot11ChannelWidthB,
       "qtechApDot11AntenneTable": qtechApDot11AntenneTable,
       "qtechApDot11AntenneEntry": qtechApDot11AntenneEntry,
       "qtechApDot11AntenneAPID": qtechApDot11AntenneAPID,
       "qtechApDot11AntenneRxA": qtechApDot11AntenneRxA,
       "qtechApDot11AntenneTxA": qtechApDot11AntenneTxA,
       "qtechApDot11AntenneRxB": qtechApDot11AntenneRxB,
       "qtechApDot11AntenneTxB": qtechApDot11AntenneTxB,
       "qtechWlanDot11MIBObjects": qtechWlanDot11MIBObjects,
       "qtechWlanDot11LoadTable": qtechWlanDot11LoadTable,
       "qtechWlanDot11LoadTEntry": qtechWlanDot11LoadTEntry,
       "qtechWlanDot11WlanId": qtechWlanDot11WlanId,
       "qtechWlanDot11Enable": qtechWlanDot11Enable,
       "qtechWlanDot11Window": qtechWlanDot11Window,
       "qtechWlanDot11Flow": qtechWlanDot11Flow,
       "qtechAcDot11MIBConformance": qtechAcDot11MIBConformance,
       "qtechAcDot11MIBCompliances": qtechAcDot11MIBCompliances,
       "qtechAcDot11MIBCompliance": qtechAcDot11MIBCompliance,
       "qtechAcDot11MIBGroups": qtechAcDot11MIBGroups,
       "qtechAcDot11MIBGroup": qtechAcDot11MIBGroup}
)
