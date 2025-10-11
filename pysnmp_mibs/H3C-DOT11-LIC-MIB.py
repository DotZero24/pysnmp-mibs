# SNMP MIB module (H3C-DOT11-LIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DOT11-LIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:11 2025
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

(h3cDot11,) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "h3cDot11")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDot11LIC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14)
)
if mibBuilder.loadTexts:
    h3cDot11LIC.setRevisions(
        ("2012-04-25 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDot11LICConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11LICConfigGroup = _H3cDot11LICConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 1)
)


class _H3cDot11LICSerialNumber_Type(OctetString):
    """Custom type h3cDot11LICSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11LICSerialNumber_Type.__name__ = "OctetString"
_H3cDot11LICSerialNumber_Object = MibScalar
h3cDot11LICSerialNumber = _H3cDot11LICSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 1, 1),
    _H3cDot11LICSerialNumber_Type()
)
h3cDot11LICSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICSerialNumber.setStatus("current")


class _H3cDot11LicApNumGroupSupport_Type(TruthValue):
    """Custom type h3cDot11LicApNumGroupSupport based on TruthValue"""
    defaultValue = 2


_H3cDot11LicApNumGroupSupport_Type.__name__ = "TruthValue"
_H3cDot11LicApNumGroupSupport_Object = MibScalar
h3cDot11LicApNumGroupSupport = _H3cDot11LicApNumGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 1, 2),
    _H3cDot11LicApNumGroupSupport_Type()
)
h3cDot11LicApNumGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LicApNumGroupSupport.setStatus("current")
_H3cDot11LICApNumGroup_ObjectIdentity = ObjectIdentity
h3cDot11LICApNumGroup = _H3cDot11LICApNumGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2)
)
_H3cDot11LICApNumAttrTable_ObjectIdentity = ObjectIdentity
h3cDot11LICApNumAttrTable = _H3cDot11LICApNumAttrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 1)
)
_H3cDot11LICDefautAPNumPermit_Type = Integer32
_H3cDot11LICDefautAPNumPermit_Object = MibScalar
h3cDot11LICDefautAPNumPermit = _H3cDot11LICDefautAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 1, 1),
    _H3cDot11LICDefautAPNumPermit_Type()
)
h3cDot11LICDefautAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICDefautAPNumPermit.setStatus("current")
_H3cDot11LICCurrentAPNumPermit_Type = Integer32
_H3cDot11LICCurrentAPNumPermit_Object = MibScalar
h3cDot11LICCurrentAPNumPermit = _H3cDot11LICCurrentAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 1, 2),
    _H3cDot11LICCurrentAPNumPermit_Type()
)
h3cDot11LICCurrentAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICCurrentAPNumPermit.setStatus("current")
_H3cDot11LICMaxAPNumPermit_Type = Integer32
_H3cDot11LICMaxAPNumPermit_Object = MibScalar
h3cDot11LICMaxAPNumPermit = _H3cDot11LICMaxAPNumPermit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 1, 3),
    _H3cDot11LICMaxAPNumPermit_Type()
)
h3cDot11LICMaxAPNumPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICMaxAPNumPermit.setStatus("current")
_H3cDot11LICApNumLicTable_Object = MibTable
h3cDot11LICApNumLicTable = _H3cDot11LICApNumLicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11LICApNumLicTable.setStatus("current")
_H3cDot11LICApNumLicEntry_Object = MibTableRow
h3cDot11LICApNumLicEntry = _H3cDot11LICApNumLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2, 1)
)
h3cDot11LICApNumLicEntry.setIndexNames(
    (0, "H3C-DOT11-LIC-MIB", "h3cDot11LICLicenseKeyIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11LICApNumLicEntry.setStatus("current")


class _H3cDot11LICLicenseKeyIndex_Type(Integer32):
    """Custom type h3cDot11LICLicenseKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11LICLicenseKeyIndex_Type.__name__ = "Integer32"
_H3cDot11LICLicenseKeyIndex_Object = MibTableColumn
h3cDot11LICLicenseKeyIndex = _H3cDot11LICLicenseKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2, 1, 1),
    _H3cDot11LICLicenseKeyIndex_Type()
)
h3cDot11LICLicenseKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICLicenseKeyIndex.setStatus("current")
_H3cDot11LICLicenseKey_Type = OctetString
_H3cDot11LICLicenseKey_Object = MibTableColumn
h3cDot11LICLicenseKey = _H3cDot11LICLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2, 1, 2),
    _H3cDot11LICLicenseKey_Type()
)
h3cDot11LICLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICLicenseKey.setStatus("current")
_H3cDot11LICActivationKey_Type = OctetString
_H3cDot11LICActivationKey_Object = MibTableColumn
h3cDot11LICActivationKey = _H3cDot11LICActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2, 1, 3),
    _H3cDot11LICActivationKey_Type()
)
h3cDot11LICActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICActivationKey.setStatus("current")
_H3cDot11LICApNum_Type = Integer32
_H3cDot11LICApNum_Object = MibTableColumn
h3cDot11LICApNum = _H3cDot11LICApNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 2, 2, 1, 4),
    _H3cDot11LICApNum_Type()
)
h3cDot11LICApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICApNum.setStatus("current")
_H3cDot11LICFeatureGroup_ObjectIdentity = ObjectIdentity
h3cDot11LICFeatureGroup = _H3cDot11LICFeatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3)
)
_H3cDot11LICFeatureAttrTable_Object = MibTable
h3cDot11LICFeatureAttrTable = _H3cDot11LICFeatureAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1)
)
if mibBuilder.loadTexts:
    h3cDot11LICFeatureAttrTable.setStatus("current")
_H3cDot11LICFeatureAttrEntry_Object = MibTableRow
h3cDot11LICFeatureAttrEntry = _H3cDot11LICFeatureAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1, 1)
)
h3cDot11LICFeatureAttrEntry.setIndexNames(
    (0, "H3C-DOT11-LIC-MIB", "h3cDot11LICAttrIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11LICFeatureAttrEntry.setStatus("current")


class _H3cDot11LICAttrIndex_Type(Integer32):
    """Custom type h3cDot11LICAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11LICAttrIndex_Type.__name__ = "Integer32"
_H3cDot11LICAttrIndex_Object = MibTableColumn
h3cDot11LICAttrIndex = _H3cDot11LICAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1, 1, 1),
    _H3cDot11LICAttrIndex_Type()
)
h3cDot11LICAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICAttrIndex.setStatus("current")
_H3cDot11LICAttrTypeName_Type = OctetString
_H3cDot11LICAttrTypeName_Object = MibTableColumn
h3cDot11LICAttrTypeName = _H3cDot11LICAttrTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1, 1, 2),
    _H3cDot11LICAttrTypeName_Type()
)
h3cDot11LICAttrTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICAttrTypeName.setStatus("current")
_H3cDot11LICAttrDefVal_Type = Integer32
_H3cDot11LICAttrDefVal_Object = MibTableColumn
h3cDot11LICAttrDefVal = _H3cDot11LICAttrDefVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1, 1, 3),
    _H3cDot11LICAttrDefVal_Type()
)
h3cDot11LICAttrDefVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICAttrDefVal.setStatus("current")
_H3cDot11LICAttrMaxVal_Type = Integer32
_H3cDot11LICAttrMaxVal_Object = MibTableColumn
h3cDot11LICAttrMaxVal = _H3cDot11LICAttrMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 1, 1, 4),
    _H3cDot11LICAttrMaxVal_Type()
)
h3cDot11LICAttrMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICAttrMaxVal.setStatus("current")
_H3cDot11LICFeatureLicTable_Object = MibTable
h3cDot11LICFeatureLicTable = _H3cDot11LICFeatureLicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2)
)
if mibBuilder.loadTexts:
    h3cDot11LICFeatureLicTable.setStatus("current")
_H3cDot11LICFeatureLicEntry_Object = MibTableRow
h3cDot11LICFeatureLicEntry = _H3cDot11LICFeatureLicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1)
)
h3cDot11LICFeatureLicEntry.setIndexNames(
    (0, "H3C-DOT11-LIC-MIB", "h3cDot11LICKeyIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11LICFeatureLicEntry.setStatus("current")


class _H3cDot11LICKeyIndex_Type(Integer32):
    """Custom type h3cDot11LICKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11LICKeyIndex_Type.__name__ = "Integer32"
_H3cDot11LICKeyIndex_Object = MibTableColumn
h3cDot11LICKeyIndex = _H3cDot11LICKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1, 1),
    _H3cDot11LICKeyIndex_Type()
)
h3cDot11LICKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICKeyIndex.setStatus("current")
_H3cDot11LICTypeName_Type = OctetString
_H3cDot11LICTypeName_Object = MibTableColumn
h3cDot11LICTypeName = _H3cDot11LICTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1, 2),
    _H3cDot11LICTypeName_Type()
)
h3cDot11LICTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICTypeName.setStatus("current")
_H3cDot11LICKey_Type = OctetString
_H3cDot11LICKey_Object = MibTableColumn
h3cDot11LICKey = _H3cDot11LICKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1, 3),
    _H3cDot11LICKey_Type()
)
h3cDot11LICKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICKey.setStatus("current")
_H3cDot11LICTimeLimit_Type = Integer32
_H3cDot11LICTimeLimit_Object = MibTableColumn
h3cDot11LICTimeLimit = _H3cDot11LICTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1, 4),
    _H3cDot11LICTimeLimit_Type()
)
h3cDot11LICTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICTimeLimit.setStatus("current")
_H3cDot11LICValue_Type = Integer32
_H3cDot11LICValue_Object = MibTableColumn
h3cDot11LICValue = _H3cDot11LICValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 14, 3, 2, 1, 5),
    _H3cDot11LICValue_Type()
)
h3cDot11LICValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11LICValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-LIC-MIB",
    **{"h3cDot11LIC": h3cDot11LIC,
       "h3cDot11LICConfigGroup": h3cDot11LICConfigGroup,
       "h3cDot11LICSerialNumber": h3cDot11LICSerialNumber,
       "h3cDot11LicApNumGroupSupport": h3cDot11LicApNumGroupSupport,
       "h3cDot11LICApNumGroup": h3cDot11LICApNumGroup,
       "h3cDot11LICApNumAttrTable": h3cDot11LICApNumAttrTable,
       "h3cDot11LICDefautAPNumPermit": h3cDot11LICDefautAPNumPermit,
       "h3cDot11LICCurrentAPNumPermit": h3cDot11LICCurrentAPNumPermit,
       "h3cDot11LICMaxAPNumPermit": h3cDot11LICMaxAPNumPermit,
       "h3cDot11LICApNumLicTable": h3cDot11LICApNumLicTable,
       "h3cDot11LICApNumLicEntry": h3cDot11LICApNumLicEntry,
       "h3cDot11LICLicenseKeyIndex": h3cDot11LICLicenseKeyIndex,
       "h3cDot11LICLicenseKey": h3cDot11LICLicenseKey,
       "h3cDot11LICActivationKey": h3cDot11LICActivationKey,
       "h3cDot11LICApNum": h3cDot11LICApNum,
       "h3cDot11LICFeatureGroup": h3cDot11LICFeatureGroup,
       "h3cDot11LICFeatureAttrTable": h3cDot11LICFeatureAttrTable,
       "h3cDot11LICFeatureAttrEntry": h3cDot11LICFeatureAttrEntry,
       "h3cDot11LICAttrIndex": h3cDot11LICAttrIndex,
       "h3cDot11LICAttrTypeName": h3cDot11LICAttrTypeName,
       "h3cDot11LICAttrDefVal": h3cDot11LICAttrDefVal,
       "h3cDot11LICAttrMaxVal": h3cDot11LICAttrMaxVal,
       "h3cDot11LICFeatureLicTable": h3cDot11LICFeatureLicTable,
       "h3cDot11LICFeatureLicEntry": h3cDot11LICFeatureLicEntry,
       "h3cDot11LICKeyIndex": h3cDot11LICKeyIndex,
       "h3cDot11LICTypeName": h3cDot11LICTypeName,
       "h3cDot11LICKey": h3cDot11LICKey,
       "h3cDot11LICTimeLimit": h3cDot11LICTimeLimit,
       "h3cDot11LICValue": h3cDot11LICValue}
)
