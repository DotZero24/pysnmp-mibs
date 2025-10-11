# SNMP MIB module (FS-AC-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-AC-DOT11-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:41 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsAcDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65)
)
if mibBuilder.loadTexts:
    fsAcDot11MIB.setRevisions(
        ("2009-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsAcDot11MIBObjects_ObjectIdentity = ObjectIdentity
fsAcDot11MIBObjects = _FsAcDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1)
)
_FsAcDot11LinkTestStaTable_Object = MibTable
fsAcDot11LinkTestStaTable = _FsAcDot11LinkTestStaTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 1)
)
if mibBuilder.loadTexts:
    fsAcDot11LinkTestStaTable.setStatus("current")
_FsAcDot11LinkTestStaEntry_Object = MibTableRow
fsAcDot11LinkTestStaEntry = _FsAcDot11LinkTestStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 1, 1)
)
fsAcDot11LinkTestStaEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsAcDot11LinkMac"),
)
if mibBuilder.loadTexts:
    fsAcDot11LinkTestStaEntry.setStatus("current")
_FsAcDot11LinkMac_Type = MacAddress
_FsAcDot11LinkMac_Object = MibTableColumn
fsAcDot11LinkMac = _FsAcDot11LinkMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 1, 1, 1),
    _FsAcDot11LinkMac_Type()
)
fsAcDot11LinkMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAcDot11LinkMac.setStatus("current")


class _FsAcDot11Link_Type(DisplayString):
    """Custom type fsAcDot11Link based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAcDot11Link_Type.__name__ = "DisplayString"
_FsAcDot11Link_Object = MibTableColumn
fsAcDot11Link = _FsAcDot11Link_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 1, 1, 2),
    _FsAcDot11Link_Type()
)
fsAcDot11Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcDot11Link.setStatus("current")
_FsAcDot11ShowClientTable_Object = MibTable
fsAcDot11ShowClientTable = _FsAcDot11ShowClientTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 2)
)
if mibBuilder.loadTexts:
    fsAcDot11ShowClientTable.setStatus("current")
_FsAcDot11ShowClientEntry_Object = MibTableRow
fsAcDot11ShowClientEntry = _FsAcDot11ShowClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 2, 1)
)
fsAcDot11ShowClientEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsAcDot11ClientMac"),
)
if mibBuilder.loadTexts:
    fsAcDot11ShowClientEntry.setStatus("current")
_FsAcDot11ClientMac_Type = MacAddress
_FsAcDot11ClientMac_Object = MibTableColumn
fsAcDot11ClientMac = _FsAcDot11ClientMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 2, 1, 1),
    _FsAcDot11ClientMac_Type()
)
fsAcDot11ClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAcDot11ClientMac.setStatus("current")


class _FsAcDot11Client_Type(DisplayString):
    """Custom type fsAcDot11Client based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAcDot11Client_Type.__name__ = "DisplayString"
_FsAcDot11Client_Object = MibTableColumn
fsAcDot11Client = _FsAcDot11Client_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 2, 1, 2),
    _FsAcDot11Client_Type()
)
fsAcDot11Client.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcDot11Client.setStatus("current")
_FsAcDot11AuthTimeout_Type = Integer32
_FsAcDot11AuthTimeout_Object = MibScalar
fsAcDot11AuthTimeout = _FsAcDot11AuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 3),
    _FsAcDot11AuthTimeout_Type()
)
fsAcDot11AuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAcDot11AuthTimeout.setStatus("current")
_FsAcDot11CountryTable_Object = MibTable
fsAcDot11CountryTable = _FsAcDot11CountryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 4)
)
if mibBuilder.loadTexts:
    fsAcDot11CountryTable.setStatus("current")
_FsAcDot11CountryEntry_Object = MibTableRow
fsAcDot11CountryEntry = _FsAcDot11CountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 4, 1)
)
fsAcDot11CountryEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsAcDot11CountryNum"),
)
if mibBuilder.loadTexts:
    fsAcDot11CountryEntry.setStatus("current")
_FsAcDot11CountryNum_Type = Integer32
_FsAcDot11CountryNum_Object = MibTableColumn
fsAcDot11CountryNum = _FsAcDot11CountryNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 4, 1, 1),
    _FsAcDot11CountryNum_Type()
)
fsAcDot11CountryNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAcDot11CountryNum.setStatus("current")


class _FsAcDot11Country_Type(DisplayString):
    """Custom type fsAcDot11Country based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_FsAcDot11Country_Type.__name__ = "DisplayString"
_FsAcDot11Country_Object = MibTableColumn
fsAcDot11Country = _FsAcDot11Country_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 4, 1, 2),
    _FsAcDot11Country_Type()
)
fsAcDot11Country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAcDot11Country.setStatus("current")
_FsAcDot11CountryEnable_Type = TruthValue
_FsAcDot11CountryEnable_Object = MibTableColumn
fsAcDot11CountryEnable = _FsAcDot11CountryEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 4, 1, 3),
    _FsAcDot11CountryEnable_Type()
)
fsAcDot11CountryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAcDot11CountryEnable.setStatus("current")


class _FsNetDot11AEnable_Type(TruthValue):
    """Custom type fsNetDot11AEnable based on TruthValue"""
    defaultValue = 1


_FsNetDot11AEnable_Type.__name__ = "TruthValue"
_FsNetDot11AEnable_Object = MibScalar
fsNetDot11AEnable = _FsNetDot11AEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 5),
    _FsNetDot11AEnable_Type()
)
fsNetDot11AEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AEnable.setStatus("current")
_FsNetDot11AMCS0_Type = TruthValue
_FsNetDot11AMCS0_Object = MibScalar
fsNetDot11AMCS0 = _FsNetDot11AMCS0_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 6),
    _FsNetDot11AMCS0_Type()
)
fsNetDot11AMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS0.setStatus("current")
_FsNetDot11AMCS1_Type = TruthValue
_FsNetDot11AMCS1_Object = MibScalar
fsNetDot11AMCS1 = _FsNetDot11AMCS1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 7),
    _FsNetDot11AMCS1_Type()
)
fsNetDot11AMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS1.setStatus("current")
_FsNetDot11AMCS2_Type = TruthValue
_FsNetDot11AMCS2_Object = MibScalar
fsNetDot11AMCS2 = _FsNetDot11AMCS2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 8),
    _FsNetDot11AMCS2_Type()
)
fsNetDot11AMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS2.setStatus("current")
_FsNetDot11AMCS3_Type = TruthValue
_FsNetDot11AMCS3_Object = MibScalar
fsNetDot11AMCS3 = _FsNetDot11AMCS3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 9),
    _FsNetDot11AMCS3_Type()
)
fsNetDot11AMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS3.setStatus("current")
_FsNetDot11AMCS4_Type = TruthValue
_FsNetDot11AMCS4_Object = MibScalar
fsNetDot11AMCS4 = _FsNetDot11AMCS4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 10),
    _FsNetDot11AMCS4_Type()
)
fsNetDot11AMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS4.setStatus("current")
_FsNetDot11AMCS5_Type = TruthValue
_FsNetDot11AMCS5_Object = MibScalar
fsNetDot11AMCS5 = _FsNetDot11AMCS5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 11),
    _FsNetDot11AMCS5_Type()
)
fsNetDot11AMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS5.setStatus("current")
_FsNetDot11AMCS6_Type = TruthValue
_FsNetDot11AMCS6_Object = MibScalar
fsNetDot11AMCS6 = _FsNetDot11AMCS6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 12),
    _FsNetDot11AMCS6_Type()
)
fsNetDot11AMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS6.setStatus("current")
_FsNetDot11AMCS7_Type = TruthValue
_FsNetDot11AMCS7_Object = MibScalar
fsNetDot11AMCS7 = _FsNetDot11AMCS7_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 13),
    _FsNetDot11AMCS7_Type()
)
fsNetDot11AMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS7.setStatus("current")
_FsNetDot11AMCS8_Type = TruthValue
_FsNetDot11AMCS8_Object = MibScalar
fsNetDot11AMCS8 = _FsNetDot11AMCS8_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 14),
    _FsNetDot11AMCS8_Type()
)
fsNetDot11AMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS8.setStatus("current")
_FsNetDot11AMCS9_Type = TruthValue
_FsNetDot11AMCS9_Object = MibScalar
fsNetDot11AMCS9 = _FsNetDot11AMCS9_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 15),
    _FsNetDot11AMCS9_Type()
)
fsNetDot11AMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS9.setStatus("current")
_FsNetDot11AMCS10_Type = TruthValue
_FsNetDot11AMCS10_Object = MibScalar
fsNetDot11AMCS10 = _FsNetDot11AMCS10_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 16),
    _FsNetDot11AMCS10_Type()
)
fsNetDot11AMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS10.setStatus("current")
_FsNetDot11AMCS11_Type = TruthValue
_FsNetDot11AMCS11_Object = MibScalar
fsNetDot11AMCS11 = _FsNetDot11AMCS11_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 17),
    _FsNetDot11AMCS11_Type()
)
fsNetDot11AMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS11.setStatus("current")
_FsNetDot11AMCS12_Type = TruthValue
_FsNetDot11AMCS12_Object = MibScalar
fsNetDot11AMCS12 = _FsNetDot11AMCS12_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 18),
    _FsNetDot11AMCS12_Type()
)
fsNetDot11AMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS12.setStatus("current")
_FsNetDot11AMCS13_Type = TruthValue
_FsNetDot11AMCS13_Object = MibScalar
fsNetDot11AMCS13 = _FsNetDot11AMCS13_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 19),
    _FsNetDot11AMCS13_Type()
)
fsNetDot11AMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS13.setStatus("current")
_FsNetDot11AMCS14_Type = TruthValue
_FsNetDot11AMCS14_Object = MibScalar
fsNetDot11AMCS14 = _FsNetDot11AMCS14_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 20),
    _FsNetDot11AMCS14_Type()
)
fsNetDot11AMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS14.setStatus("current")
_FsNetDot11AMCS15_Type = TruthValue
_FsNetDot11AMCS15_Object = MibScalar
fsNetDot11AMCS15 = _FsNetDot11AMCS15_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 21),
    _FsNetDot11AMCS15_Type()
)
fsNetDot11AMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AMCS15.setStatus("current")


class _FsNetDot11AAMPDU_Type(Integer32):
    """Custom type fsNetDot11AAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsNetDot11AAMPDU_Type.__name__ = "Integer32"
_FsNetDot11AAMPDU_Object = MibScalar
fsNetDot11AAMPDU = _FsNetDot11AAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 22),
    _FsNetDot11AAMPDU_Type()
)
fsNetDot11AAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AAMPDU.setStatus("current")


class _FsNetDot11BEnable_Type(TruthValue):
    """Custom type fsNetDot11BEnable based on TruthValue"""
    defaultValue = 1


_FsNetDot11BEnable_Type.__name__ = "TruthValue"
_FsNetDot11BEnable_Object = MibScalar
fsNetDot11BEnable = _FsNetDot11BEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 23),
    _FsNetDot11BEnable_Type()
)
fsNetDot11BEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BEnable.setStatus("current")


class _FsNetDot11BMCS0_Type(Integer32):
    """Custom type fsNetDot11BMCS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS0_Type.__name__ = "Integer32"
_FsNetDot11BMCS0_Object = MibScalar
fsNetDot11BMCS0 = _FsNetDot11BMCS0_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 24),
    _FsNetDot11BMCS0_Type()
)
fsNetDot11BMCS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS0.setStatus("current")


class _FsNetDot11BMCS1_Type(Integer32):
    """Custom type fsNetDot11BMCS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS1_Type.__name__ = "Integer32"
_FsNetDot11BMCS1_Object = MibScalar
fsNetDot11BMCS1 = _FsNetDot11BMCS1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 25),
    _FsNetDot11BMCS1_Type()
)
fsNetDot11BMCS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS1.setStatus("current")


class _FsNetDot11BMCS2_Type(Integer32):
    """Custom type fsNetDot11BMCS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS2_Type.__name__ = "Integer32"
_FsNetDot11BMCS2_Object = MibScalar
fsNetDot11BMCS2 = _FsNetDot11BMCS2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 26),
    _FsNetDot11BMCS2_Type()
)
fsNetDot11BMCS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS2.setStatus("current")


class _FsNetDot11BMCS3_Type(Integer32):
    """Custom type fsNetDot11BMCS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS3_Type.__name__ = "Integer32"
_FsNetDot11BMCS3_Object = MibScalar
fsNetDot11BMCS3 = _FsNetDot11BMCS3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 27),
    _FsNetDot11BMCS3_Type()
)
fsNetDot11BMCS3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS3.setStatus("current")


class _FsNetDot11BMCS4_Type(Integer32):
    """Custom type fsNetDot11BMCS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS4_Type.__name__ = "Integer32"
_FsNetDot11BMCS4_Object = MibScalar
fsNetDot11BMCS4 = _FsNetDot11BMCS4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 28),
    _FsNetDot11BMCS4_Type()
)
fsNetDot11BMCS4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS4.setStatus("current")


class _FsNetDot11BMCS5_Type(Integer32):
    """Custom type fsNetDot11BMCS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS5_Type.__name__ = "Integer32"
_FsNetDot11BMCS5_Object = MibScalar
fsNetDot11BMCS5 = _FsNetDot11BMCS5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 29),
    _FsNetDot11BMCS5_Type()
)
fsNetDot11BMCS5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS5.setStatus("current")


class _FsNetDot11BMCS6_Type(Integer32):
    """Custom type fsNetDot11BMCS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS6_Type.__name__ = "Integer32"
_FsNetDot11BMCS6_Object = MibScalar
fsNetDot11BMCS6 = _FsNetDot11BMCS6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 30),
    _FsNetDot11BMCS6_Type()
)
fsNetDot11BMCS6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS6.setStatus("current")


class _FsNetDot11BMCS7_Type(Integer32):
    """Custom type fsNetDot11BMCS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS7_Type.__name__ = "Integer32"
_FsNetDot11BMCS7_Object = MibScalar
fsNetDot11BMCS7 = _FsNetDot11BMCS7_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 31),
    _FsNetDot11BMCS7_Type()
)
fsNetDot11BMCS7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS7.setStatus("current")


class _FsNetDot11BMCS8_Type(Integer32):
    """Custom type fsNetDot11BMCS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS8_Type.__name__ = "Integer32"
_FsNetDot11BMCS8_Object = MibScalar
fsNetDot11BMCS8 = _FsNetDot11BMCS8_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 32),
    _FsNetDot11BMCS8_Type()
)
fsNetDot11BMCS8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS8.setStatus("current")


class _FsNetDot11BMCS9_Type(Integer32):
    """Custom type fsNetDot11BMCS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS9_Type.__name__ = "Integer32"
_FsNetDot11BMCS9_Object = MibScalar
fsNetDot11BMCS9 = _FsNetDot11BMCS9_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 33),
    _FsNetDot11BMCS9_Type()
)
fsNetDot11BMCS9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS9.setStatus("current")


class _FsNetDot11BMCS10_Type(Integer32):
    """Custom type fsNetDot11BMCS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS10_Type.__name__ = "Integer32"
_FsNetDot11BMCS10_Object = MibScalar
fsNetDot11BMCS10 = _FsNetDot11BMCS10_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 34),
    _FsNetDot11BMCS10_Type()
)
fsNetDot11BMCS10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS10.setStatus("current")


class _FsNetDot11BMCS11_Type(Integer32):
    """Custom type fsNetDot11BMCS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS11_Type.__name__ = "Integer32"
_FsNetDot11BMCS11_Object = MibScalar
fsNetDot11BMCS11 = _FsNetDot11BMCS11_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 35),
    _FsNetDot11BMCS11_Type()
)
fsNetDot11BMCS11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS11.setStatus("current")


class _FsNetDot11BMCS12_Type(Integer32):
    """Custom type fsNetDot11BMCS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS12_Type.__name__ = "Integer32"
_FsNetDot11BMCS12_Object = MibScalar
fsNetDot11BMCS12 = _FsNetDot11BMCS12_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 36),
    _FsNetDot11BMCS12_Type()
)
fsNetDot11BMCS12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS12.setStatus("current")


class _FsNetDot11BMCS13_Type(Integer32):
    """Custom type fsNetDot11BMCS13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS13_Type.__name__ = "Integer32"
_FsNetDot11BMCS13_Object = MibScalar
fsNetDot11BMCS13 = _FsNetDot11BMCS13_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 37),
    _FsNetDot11BMCS13_Type()
)
fsNetDot11BMCS13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS13.setStatus("current")


class _FsNetDot11BMCS14_Type(Integer32):
    """Custom type fsNetDot11BMCS14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS14_Type.__name__ = "Integer32"
_FsNetDot11BMCS14_Object = MibScalar
fsNetDot11BMCS14 = _FsNetDot11BMCS14_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 38),
    _FsNetDot11BMCS14_Type()
)
fsNetDot11BMCS14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS14.setStatus("current")


class _FsNetDot11BMCS15_Type(Integer32):
    """Custom type fsNetDot11BMCS15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsNetDot11BMCS15_Type.__name__ = "Integer32"
_FsNetDot11BMCS15_Object = MibScalar
fsNetDot11BMCS15 = _FsNetDot11BMCS15_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 39),
    _FsNetDot11BMCS15_Type()
)
fsNetDot11BMCS15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BMCS15.setStatus("current")


class _FsNetDot11BAMPDU_Type(Integer32):
    """Custom type fsNetDot11BAMPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsNetDot11BAMPDU_Type.__name__ = "Integer32"
_FsNetDot11BAMPDU_Object = MibScalar
fsNetDot11BAMPDU = _FsNetDot11BAMPDU_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 40),
    _FsNetDot11BAMPDU_Type()
)
fsNetDot11BAMPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BAMPDU.setStatus("current")


class _FsNetDot11AGEnable_Type(TruthValue):
    """Custom type fsNetDot11AGEnable based on TruthValue"""
    defaultValue = 1


_FsNetDot11AGEnable_Type.__name__ = "TruthValue"
_FsNetDot11AGEnable_Object = MibScalar
fsNetDot11AGEnable = _FsNetDot11AGEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 41),
    _FsNetDot11AGEnable_Type()
)
fsNetDot11AGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11AGEnable.setStatus("current")


class _FsNetDot11BGEnable_Type(TruthValue):
    """Custom type fsNetDot11BGEnable based on TruthValue"""
    defaultValue = 1


_FsNetDot11BGEnable_Type.__name__ = "TruthValue"
_FsNetDot11BGEnable_Object = MibScalar
fsNetDot11BGEnable = _FsNetDot11BGEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 1, 42),
    _FsNetDot11BGEnable_Type()
)
fsNetDot11BGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNetDot11BGEnable.setStatus("current")
_FsApDot11MIBObjects_ObjectIdentity = ObjectIdentity
fsApDot11MIBObjects = _FsApDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2)
)
_FsApDot11PoeTable_Object = MibTable
fsApDot11PoeTable = _FsApDot11PoeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 1)
)
if mibBuilder.loadTexts:
    fsApDot11PoeTable.setStatus("current")
_FsApDot11PoeEntry_Object = MibTableRow
fsApDot11PoeEntry = _FsApDot11PoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 1, 1)
)
fsApDot11PoeEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsApDot11PoeAPID"),
)
if mibBuilder.loadTexts:
    fsApDot11PoeEntry.setStatus("current")
_FsApDot11PoeAPID_Type = TruthValue
_FsApDot11PoeAPID_Object = MibTableColumn
fsApDot11PoeAPID = _FsApDot11PoeAPID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 1, 1, 1),
    _FsApDot11PoeAPID_Type()
)
fsApDot11PoeAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsApDot11PoeAPID.setStatus("current")
_FsApDot11PoeEnable_Type = TruthValue
_FsApDot11PoeEnable_Object = MibTableColumn
fsApDot11PoeEnable = _FsApDot11PoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 1, 1, 2),
    _FsApDot11PoeEnable_Type()
)
fsApDot11PoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11PoeEnable.setStatus("current")
_FsApDot11ChannelTable_Object = MibTable
fsApDot11ChannelTable = _FsApDot11ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 2)
)
if mibBuilder.loadTexts:
    fsApDot11ChannelTable.setStatus("current")
_FsApDot11ChannelEntry_Object = MibTableRow
fsApDot11ChannelEntry = _FsApDot11ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 2, 1)
)
fsApDot11ChannelEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsApDot11ChannelAPID"),
)
if mibBuilder.loadTexts:
    fsApDot11ChannelEntry.setStatus("current")
_FsApDot11ChannelAPID_Type = Integer32
_FsApDot11ChannelAPID_Object = MibTableColumn
fsApDot11ChannelAPID = _FsApDot11ChannelAPID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 2, 1, 1),
    _FsApDot11ChannelAPID_Type()
)
fsApDot11ChannelAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsApDot11ChannelAPID.setStatus("current")


class _FsApDot11ChannelWidthA_Type(Integer32):
    """Custom type fsApDot11ChannelWidthA based on Integer32"""
    defaultValue = 20


_FsApDot11ChannelWidthA_Type.__name__ = "Integer32"
_FsApDot11ChannelWidthA_Object = MibTableColumn
fsApDot11ChannelWidthA = _FsApDot11ChannelWidthA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 2, 1, 2),
    _FsApDot11ChannelWidthA_Type()
)
fsApDot11ChannelWidthA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11ChannelWidthA.setStatus("current")


class _FsApDot11ChannelWidthB_Type(Integer32):
    """Custom type fsApDot11ChannelWidthB based on Integer32"""
    defaultValue = 20


_FsApDot11ChannelWidthB_Type.__name__ = "Integer32"
_FsApDot11ChannelWidthB_Object = MibTableColumn
fsApDot11ChannelWidthB = _FsApDot11ChannelWidthB_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 2, 1, 3),
    _FsApDot11ChannelWidthB_Type()
)
fsApDot11ChannelWidthB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11ChannelWidthB.setStatus("current")
_FsApDot11AntenneTable_Object = MibTable
fsApDot11AntenneTable = _FsApDot11AntenneTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3)
)
if mibBuilder.loadTexts:
    fsApDot11AntenneTable.setStatus("current")
_FsApDot11AntenneEntry_Object = MibTableRow
fsApDot11AntenneEntry = _FsApDot11AntenneEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1)
)
fsApDot11AntenneEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsApDot11AntenneAPID"),
)
if mibBuilder.loadTexts:
    fsApDot11AntenneEntry.setStatus("current")
_FsApDot11AntenneAPID_Type = Integer32
_FsApDot11AntenneAPID_Object = MibTableColumn
fsApDot11AntenneAPID = _FsApDot11AntenneAPID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1, 1),
    _FsApDot11AntenneAPID_Type()
)
fsApDot11AntenneAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsApDot11AntenneAPID.setStatus("current")


class _FsApDot11AntenneRxA_Type(Integer32):
    """Custom type fsApDot11AntenneRxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsApDot11AntenneRxA_Type.__name__ = "Integer32"
_FsApDot11AntenneRxA_Object = MibTableColumn
fsApDot11AntenneRxA = _FsApDot11AntenneRxA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1, 2),
    _FsApDot11AntenneRxA_Type()
)
fsApDot11AntenneRxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11AntenneRxA.setStatus("current")


class _FsApDot11AntenneTxA_Type(Integer32):
    """Custom type fsApDot11AntenneTxA based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsApDot11AntenneTxA_Type.__name__ = "Integer32"
_FsApDot11AntenneTxA_Object = MibTableColumn
fsApDot11AntenneTxA = _FsApDot11AntenneTxA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1, 3),
    _FsApDot11AntenneTxA_Type()
)
fsApDot11AntenneTxA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11AntenneTxA.setStatus("current")


class _FsApDot11AntenneRxB_Type(Integer32):
    """Custom type fsApDot11AntenneRxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsApDot11AntenneRxB_Type.__name__ = "Integer32"
_FsApDot11AntenneRxB_Object = MibTableColumn
fsApDot11AntenneRxB = _FsApDot11AntenneRxB_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1, 4),
    _FsApDot11AntenneRxB_Type()
)
fsApDot11AntenneRxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11AntenneRxB.setStatus("current")


class _FsApDot11AntenneTxB_Type(Integer32):
    """Custom type fsApDot11AntenneTxB based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsApDot11AntenneTxB_Type.__name__ = "Integer32"
_FsApDot11AntenneTxB_Object = MibTableColumn
fsApDot11AntenneTxB = _FsApDot11AntenneTxB_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 2, 3, 1, 5),
    _FsApDot11AntenneTxB_Type()
)
fsApDot11AntenneTxB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApDot11AntenneTxB.setStatus("current")
_FsWlanDot11MIBObjects_ObjectIdentity = ObjectIdentity
fsWlanDot11MIBObjects = _FsWlanDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3)
)
_FsWlanDot11LoadTable_Object = MibTable
fsWlanDot11LoadTable = _FsWlanDot11LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1)
)
if mibBuilder.loadTexts:
    fsWlanDot11LoadTable.setStatus("current")
_FsWlanDot11LoadTEntry_Object = MibTableRow
fsWlanDot11LoadTEntry = _FsWlanDot11LoadTEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1, 1)
)
fsWlanDot11LoadTEntry.setIndexNames(
    (0, "FS-AC-DOT11-MIB", "fsWlanDot11WlanId"),
)
if mibBuilder.loadTexts:
    fsWlanDot11LoadTEntry.setStatus("current")
_FsWlanDot11WlanId_Type = Integer32
_FsWlanDot11WlanId_Object = MibTableColumn
fsWlanDot11WlanId = _FsWlanDot11WlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1, 1, 1),
    _FsWlanDot11WlanId_Type()
)
fsWlanDot11WlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWlanDot11WlanId.setStatus("current")


class _FsWlanDot11Enable_Type(TruthValue):
    """Custom type fsWlanDot11Enable based on TruthValue"""
    defaultValue = 2


_FsWlanDot11Enable_Type.__name__ = "TruthValue"
_FsWlanDot11Enable_Object = MibTableColumn
fsWlanDot11Enable = _FsWlanDot11Enable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1, 1, 2),
    _FsWlanDot11Enable_Type()
)
fsWlanDot11Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWlanDot11Enable.setStatus("current")


class _FsWlanDot11Window_Type(Integer32):
    """Custom type fsWlanDot11Window based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FsWlanDot11Window_Type.__name__ = "Integer32"
_FsWlanDot11Window_Object = MibTableColumn
fsWlanDot11Window = _FsWlanDot11Window_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1, 1, 3),
    _FsWlanDot11Window_Type()
)
fsWlanDot11Window.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWlanDot11Window.setStatus("current")


class _FsWlanDot11Flow_Type(Integer32):
    """Custom type fsWlanDot11Flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 130),
    )


_FsWlanDot11Flow_Type.__name__ = "Integer32"
_FsWlanDot11Flow_Object = MibTableColumn
fsWlanDot11Flow = _FsWlanDot11Flow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 3, 1, 1, 4),
    _FsWlanDot11Flow_Type()
)
fsWlanDot11Flow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWlanDot11Flow.setStatus("current")
_FsAcDot11MIBConformance_ObjectIdentity = ObjectIdentity
fsAcDot11MIBConformance = _FsAcDot11MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 5)
)
_FsAcDot11MIBCompliances_ObjectIdentity = ObjectIdentity
fsAcDot11MIBCompliances = _FsAcDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 5, 1)
)
_FsAcDot11MIBGroups_ObjectIdentity = ObjectIdentity
fsAcDot11MIBGroups = _FsAcDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 5, 2)
)

# Managed Objects groups

fsAcDot11MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 5, 2, 1)
)
fsAcDot11MIBGroup.setObjects(
      *(("FS-AC-DOT11-MIB", "fsAcDot11Link"),
        ("FS-AC-DOT11-MIB", "fsAcDot11Client"),
        ("FS-AC-DOT11-MIB", "fsAcDot11AuthTimeout"),
        ("FS-AC-DOT11-MIB", "fsAcDot11Country"),
        ("FS-AC-DOT11-MIB", "fsAcDot11CountryEnable"),
        ("FS-AC-DOT11-MIB", "fsApDot11PoeEnable"),
        ("FS-AC-DOT11-MIB", "fsApDot11ChannelWidthA"),
        ("FS-AC-DOT11-MIB", "fsApDot11ChannelWidthB"),
        ("FS-AC-DOT11-MIB", "fsApDot11AntenneRxA"),
        ("FS-AC-DOT11-MIB", "fsApDot11AntenneTxA"),
        ("FS-AC-DOT11-MIB", "fsApDot11AntenneRxB"),
        ("FS-AC-DOT11-MIB", "fsApDot11AntenneTxB"),
        ("FS-AC-DOT11-MIB", "fsWlanDot11Enable"),
        ("FS-AC-DOT11-MIB", "fsWlanDot11Window"),
        ("FS-AC-DOT11-MIB", "fsWlanDot11Flow"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AEnable"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS0"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS1"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS2"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS3"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS4"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS5"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS6"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS7"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS8"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS9"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS10"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS11"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS12"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS13"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS14"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AMCS15"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AAMPDU"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BEnable"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS0"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS1"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS2"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS3"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS4"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS5"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS6"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS7"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS8"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS9"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS10"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS11"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS12"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS13"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS14"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BMCS15"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BAMPDU"),
        ("FS-AC-DOT11-MIB", "fsNetDot11AGEnable"),
        ("FS-AC-DOT11-MIB", "fsNetDot11BGEnable"))
)
if mibBuilder.loadTexts:
    fsAcDot11MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsAcDot11MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 65, 5, 1, 1)
)
fsAcDot11MIBCompliance.setObjects(
    ("FS-AC-DOT11-MIB", "fsAcDot11MIBGroup")
)
if mibBuilder.loadTexts:
    fsAcDot11MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-AC-DOT11-MIB",
    **{"fsAcDot11MIB": fsAcDot11MIB,
       "fsAcDot11MIBObjects": fsAcDot11MIBObjects,
       "fsAcDot11LinkTestStaTable": fsAcDot11LinkTestStaTable,
       "fsAcDot11LinkTestStaEntry": fsAcDot11LinkTestStaEntry,
       "fsAcDot11LinkMac": fsAcDot11LinkMac,
       "fsAcDot11Link": fsAcDot11Link,
       "fsAcDot11ShowClientTable": fsAcDot11ShowClientTable,
       "fsAcDot11ShowClientEntry": fsAcDot11ShowClientEntry,
       "fsAcDot11ClientMac": fsAcDot11ClientMac,
       "fsAcDot11Client": fsAcDot11Client,
       "fsAcDot11AuthTimeout": fsAcDot11AuthTimeout,
       "fsAcDot11CountryTable": fsAcDot11CountryTable,
       "fsAcDot11CountryEntry": fsAcDot11CountryEntry,
       "fsAcDot11CountryNum": fsAcDot11CountryNum,
       "fsAcDot11Country": fsAcDot11Country,
       "fsAcDot11CountryEnable": fsAcDot11CountryEnable,
       "fsNetDot11AEnable": fsNetDot11AEnable,
       "fsNetDot11AMCS0": fsNetDot11AMCS0,
       "fsNetDot11AMCS1": fsNetDot11AMCS1,
       "fsNetDot11AMCS2": fsNetDot11AMCS2,
       "fsNetDot11AMCS3": fsNetDot11AMCS3,
       "fsNetDot11AMCS4": fsNetDot11AMCS4,
       "fsNetDot11AMCS5": fsNetDot11AMCS5,
       "fsNetDot11AMCS6": fsNetDot11AMCS6,
       "fsNetDot11AMCS7": fsNetDot11AMCS7,
       "fsNetDot11AMCS8": fsNetDot11AMCS8,
       "fsNetDot11AMCS9": fsNetDot11AMCS9,
       "fsNetDot11AMCS10": fsNetDot11AMCS10,
       "fsNetDot11AMCS11": fsNetDot11AMCS11,
       "fsNetDot11AMCS12": fsNetDot11AMCS12,
       "fsNetDot11AMCS13": fsNetDot11AMCS13,
       "fsNetDot11AMCS14": fsNetDot11AMCS14,
       "fsNetDot11AMCS15": fsNetDot11AMCS15,
       "fsNetDot11AAMPDU": fsNetDot11AAMPDU,
       "fsNetDot11BEnable": fsNetDot11BEnable,
       "fsNetDot11BMCS0": fsNetDot11BMCS0,
       "fsNetDot11BMCS1": fsNetDot11BMCS1,
       "fsNetDot11BMCS2": fsNetDot11BMCS2,
       "fsNetDot11BMCS3": fsNetDot11BMCS3,
       "fsNetDot11BMCS4": fsNetDot11BMCS4,
       "fsNetDot11BMCS5": fsNetDot11BMCS5,
       "fsNetDot11BMCS6": fsNetDot11BMCS6,
       "fsNetDot11BMCS7": fsNetDot11BMCS7,
       "fsNetDot11BMCS8": fsNetDot11BMCS8,
       "fsNetDot11BMCS9": fsNetDot11BMCS9,
       "fsNetDot11BMCS10": fsNetDot11BMCS10,
       "fsNetDot11BMCS11": fsNetDot11BMCS11,
       "fsNetDot11BMCS12": fsNetDot11BMCS12,
       "fsNetDot11BMCS13": fsNetDot11BMCS13,
       "fsNetDot11BMCS14": fsNetDot11BMCS14,
       "fsNetDot11BMCS15": fsNetDot11BMCS15,
       "fsNetDot11BAMPDU": fsNetDot11BAMPDU,
       "fsNetDot11AGEnable": fsNetDot11AGEnable,
       "fsNetDot11BGEnable": fsNetDot11BGEnable,
       "fsApDot11MIBObjects": fsApDot11MIBObjects,
       "fsApDot11PoeTable": fsApDot11PoeTable,
       "fsApDot11PoeEntry": fsApDot11PoeEntry,
       "fsApDot11PoeAPID": fsApDot11PoeAPID,
       "fsApDot11PoeEnable": fsApDot11PoeEnable,
       "fsApDot11ChannelTable": fsApDot11ChannelTable,
       "fsApDot11ChannelEntry": fsApDot11ChannelEntry,
       "fsApDot11ChannelAPID": fsApDot11ChannelAPID,
       "fsApDot11ChannelWidthA": fsApDot11ChannelWidthA,
       "fsApDot11ChannelWidthB": fsApDot11ChannelWidthB,
       "fsApDot11AntenneTable": fsApDot11AntenneTable,
       "fsApDot11AntenneEntry": fsApDot11AntenneEntry,
       "fsApDot11AntenneAPID": fsApDot11AntenneAPID,
       "fsApDot11AntenneRxA": fsApDot11AntenneRxA,
       "fsApDot11AntenneTxA": fsApDot11AntenneTxA,
       "fsApDot11AntenneRxB": fsApDot11AntenneRxB,
       "fsApDot11AntenneTxB": fsApDot11AntenneTxB,
       "fsWlanDot11MIBObjects": fsWlanDot11MIBObjects,
       "fsWlanDot11LoadTable": fsWlanDot11LoadTable,
       "fsWlanDot11LoadTEntry": fsWlanDot11LoadTEntry,
       "fsWlanDot11WlanId": fsWlanDot11WlanId,
       "fsWlanDot11Enable": fsWlanDot11Enable,
       "fsWlanDot11Window": fsWlanDot11Window,
       "fsWlanDot11Flow": fsWlanDot11Flow,
       "fsAcDot11MIBConformance": fsAcDot11MIBConformance,
       "fsAcDot11MIBCompliances": fsAcDot11MIBCompliances,
       "fsAcDot11MIBCompliance": fsAcDot11MIBCompliance,
       "fsAcDot11MIBGroups": fsAcDot11MIBGroups,
       "fsAcDot11MIBGroup": fsAcDot11MIBGroup}
)
