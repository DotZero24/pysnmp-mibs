# SNMP MIB module (ENTERASYS-APPLICATION-SIGNATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-APPLICATION-SIGNATURE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:17 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

etsysApplicationSignatureMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107)
)
if mibBuilder.loadTexts:
    etsysApplicationSignatureMIB.setRevisions(
        ("2016-05-11 12:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysApplicationSignatureMIBObjects_ObjectIdentity = ObjectIdentity
etsysApplicationSignatureMIBObjects = _EtsysApplicationSignatureMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1)
)
_EtsysAppSignGroupTable_Object = MibTable
etsysAppSignGroupTable = _EtsysAppSignGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 1)
)
if mibBuilder.loadTexts:
    etsysAppSignGroupTable.setStatus("current")
_EtsysAppSignGroupEntry_Object = MibTableRow
etsysAppSignGroupEntry = _EtsysAppSignGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 1, 1)
)
etsysAppSignGroupEntry.setIndexNames(
    (0, "ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignGroupId"),
)
if mibBuilder.loadTexts:
    etsysAppSignGroupEntry.setStatus("current")


class _EtsysAppSignGroupId_Type(Unsigned32):
    """Custom type etsysAppSignGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysAppSignGroupId_Type.__name__ = "Unsigned32"
_EtsysAppSignGroupId_Object = MibTableColumn
etsysAppSignGroupId = _EtsysAppSignGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 1, 1, 1),
    _EtsysAppSignGroupId_Type()
)
etsysAppSignGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAppSignGroupId.setStatus("current")
_EtsysAppSignGroupName_Type = SnmpAdminString
_EtsysAppSignGroupName_Object = MibTableColumn
etsysAppSignGroupName = _EtsysAppSignGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 1, 1, 2),
    _EtsysAppSignGroupName_Type()
)
etsysAppSignGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAppSignGroupName.setStatus("current")
_EtsysAppSignDisplayNameTable_Object = MibTable
etsysAppSignDisplayNameTable = _EtsysAppSignDisplayNameTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 2)
)
if mibBuilder.loadTexts:
    etsysAppSignDisplayNameTable.setStatus("current")
_EtsysAppSignDisplayNameEntry_Object = MibTableRow
etsysAppSignDisplayNameEntry = _EtsysAppSignDisplayNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 2, 1)
)
etsysAppSignDisplayNameEntry.setIndexNames(
    (0, "ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignDisplayId"),
)
if mibBuilder.loadTexts:
    etsysAppSignDisplayNameEntry.setStatus("current")


class _EtsysAppSignDisplayId_Type(Unsigned32):
    """Custom type etsysAppSignDisplayId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5999),
    )


_EtsysAppSignDisplayId_Type.__name__ = "Unsigned32"
_EtsysAppSignDisplayId_Object = MibTableColumn
etsysAppSignDisplayId = _EtsysAppSignDisplayId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 2, 1, 1),
    _EtsysAppSignDisplayId_Type()
)
etsysAppSignDisplayId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAppSignDisplayId.setStatus("current")


class _EtsysAppSignDisplayName_Type(SnmpAdminString):
    """Custom type etsysAppSignDisplayName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysAppSignDisplayName_Type.__name__ = "SnmpAdminString"
_EtsysAppSignDisplayName_Object = MibTableColumn
etsysAppSignDisplayName = _EtsysAppSignDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 2, 1, 2),
    _EtsysAppSignDisplayName_Type()
)
etsysAppSignDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysAppSignDisplayName.setStatus("current")
_EtsysAppSignDisplayNameRowStatus_Type = RowStatus
_EtsysAppSignDisplayNameRowStatus_Object = MibTableColumn
etsysAppSignDisplayNameRowStatus = _EtsysAppSignDisplayNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 2, 1, 3),
    _EtsysAppSignDisplayNameRowStatus_Type()
)
etsysAppSignDisplayNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysAppSignDisplayNameRowStatus.setStatus("current")
_EtsysAppSignPatternTable_Object = MibTable
etsysAppSignPatternTable = _EtsysAppSignPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 3)
)
if mibBuilder.loadTexts:
    etsysAppSignPatternTable.setStatus("current")
_EtsysAppSignPatternEntry_Object = MibTableRow
etsysAppSignPatternEntry = _EtsysAppSignPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 3, 1)
)
etsysAppSignPatternEntry.setIndexNames(
    (0, "ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignGroupId"),
    (0, "ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignDisplayId"),
    (0, "ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignPatternIndex"),
)
if mibBuilder.loadTexts:
    etsysAppSignPatternEntry.setStatus("current")


class _EtsysAppSignPatternIndex_Type(Unsigned32):
    """Custom type etsysAppSignPatternIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 2000000),
    )


_EtsysAppSignPatternIndex_Type.__name__ = "Unsigned32"
_EtsysAppSignPatternIndex_Object = MibTableColumn
etsysAppSignPatternIndex = _EtsysAppSignPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 3, 1, 1),
    _EtsysAppSignPatternIndex_Type()
)
etsysAppSignPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysAppSignPatternIndex.setStatus("current")


class _EtsysAppSignPattern_Type(DisplayString):
    """Custom type etsysAppSignPattern based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysAppSignPattern_Type.__name__ = "DisplayString"
_EtsysAppSignPattern_Object = MibTableColumn
etsysAppSignPattern = _EtsysAppSignPattern_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 3, 1, 2),
    _EtsysAppSignPattern_Type()
)
etsysAppSignPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysAppSignPattern.setStatus("current")
_EtsysAppSignPatternRowStatus_Type = RowStatus
_EtsysAppSignPatternRowStatus_Object = MibTableColumn
etsysAppSignPatternRowStatus = _EtsysAppSignPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 1, 3, 1, 3),
    _EtsysAppSignPatternRowStatus_Type()
)
etsysAppSignPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysAppSignPatternRowStatus.setStatus("current")
_EtsysApplicationSignatureConformance_ObjectIdentity = ObjectIdentity
etsysApplicationSignatureConformance = _EtsysApplicationSignatureConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2)
)
_EtsysAppSignGroups_ObjectIdentity = ObjectIdentity
etsysAppSignGroups = _EtsysAppSignGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 1)
)
_EtsysAppSignCompliances_ObjectIdentity = ObjectIdentity
etsysAppSignCompliances = _EtsysAppSignCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 2)
)

# Managed Objects groups

etsysAppSignGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 1, 1)
)
etsysAppSignGroup.setObjects(
    ("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignGroupName")
)
if mibBuilder.loadTexts:
    etsysAppSignGroup.setStatus("current")

etsysAppSignDisplayNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 1, 2)
)
etsysAppSignDisplayNameGroup.setObjects(
      *(("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignDisplayName"),
        ("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignDisplayNameRowStatus"))
)
if mibBuilder.loadTexts:
    etsysAppSignDisplayNameGroup.setStatus("current")

etsysAppSignPatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 1, 3)
)
etsysAppSignPatternGroup.setObjects(
      *(("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignPattern"),
        ("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignPatternRowStatus"))
)
if mibBuilder.loadTexts:
    etsysAppSignPatternGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysAppSignCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 107, 2, 2, 1)
)
etsysAppSignCompliance.setObjects(
      *(("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignGroup"),
        ("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignDisplayNameGroup"),
        ("ENTERASYS-APPLICATION-SIGNATURE-MIB", "etsysAppSignPatternGroup"))
)
if mibBuilder.loadTexts:
    etsysAppSignCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-APPLICATION-SIGNATURE-MIB",
    **{"etsysApplicationSignatureMIB": etsysApplicationSignatureMIB,
       "etsysApplicationSignatureMIBObjects": etsysApplicationSignatureMIBObjects,
       "etsysAppSignGroupTable": etsysAppSignGroupTable,
       "etsysAppSignGroupEntry": etsysAppSignGroupEntry,
       "etsysAppSignGroupId": etsysAppSignGroupId,
       "etsysAppSignGroupName": etsysAppSignGroupName,
       "etsysAppSignDisplayNameTable": etsysAppSignDisplayNameTable,
       "etsysAppSignDisplayNameEntry": etsysAppSignDisplayNameEntry,
       "etsysAppSignDisplayId": etsysAppSignDisplayId,
       "etsysAppSignDisplayName": etsysAppSignDisplayName,
       "etsysAppSignDisplayNameRowStatus": etsysAppSignDisplayNameRowStatus,
       "etsysAppSignPatternTable": etsysAppSignPatternTable,
       "etsysAppSignPatternEntry": etsysAppSignPatternEntry,
       "etsysAppSignPatternIndex": etsysAppSignPatternIndex,
       "etsysAppSignPattern": etsysAppSignPattern,
       "etsysAppSignPatternRowStatus": etsysAppSignPatternRowStatus,
       "etsysApplicationSignatureConformance": etsysApplicationSignatureConformance,
       "etsysAppSignGroups": etsysAppSignGroups,
       "etsysAppSignGroup": etsysAppSignGroup,
       "etsysAppSignDisplayNameGroup": etsysAppSignDisplayNameGroup,
       "etsysAppSignPatternGroup": etsysAppSignPatternGroup,
       "etsysAppSignCompliances": etsysAppSignCompliances,
       "etsysAppSignCompliance": etsysAppSignCompliance}
)
