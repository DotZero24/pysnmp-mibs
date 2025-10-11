# SNMP MIB module (ARICENT-VPLS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-VPLS-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:35 2025
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

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

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
 enterprises,
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(vplsConfigIndex,) = mibBuilder.importSymbols(
    "VPLS-GENERIC-MIB",
    "vplsConfigIndex")


# MODULE-IDENTITY

fsVplsBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86)
)
if mibBuilder.loadTexts:
    fsVplsBgpMIB.setRevisions(
        ("2013-02-22 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VplsBgpObjects_ObjectIdentity = ObjectIdentity
vplsBgpObjects = _VplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1)
)
_VplsBgpConfigTable_Object = MibTable
vplsBgpConfigTable = _VplsBgpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 1)
)
if mibBuilder.loadTexts:
    vplsBgpConfigTable.setStatus("current")
_VplsBgpConfigEntry_Object = MibTableRow
vplsBgpConfigEntry = _VplsBgpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 1, 1)
)
vplsBgpConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpConfigEntry.setStatus("current")


class _VplsBgpConfigVERangeSize_Type(Unsigned32):
    """Custom type vplsBgpConfigVERangeSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VplsBgpConfigVERangeSize_Type.__name__ = "Unsigned32"
_VplsBgpConfigVERangeSize_Object = MibTableColumn
vplsBgpConfigVERangeSize = _VplsBgpConfigVERangeSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 1, 1, 1),
    _VplsBgpConfigVERangeSize_Type()
)
vplsBgpConfigVERangeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsBgpConfigVERangeSize.setStatus("current")
_VplsBgpVETable_Object = MibTable
vplsBgpVETable = _VplsBgpVETable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2)
)
if mibBuilder.loadTexts:
    vplsBgpVETable.setStatus("current")
_VplsBgpVEEntry_Object = MibTableRow
vplsBgpVEEntry = _VplsBgpVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1)
)
vplsBgpVEEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "ARICENT-VPLS-BGP-MIB", "vplsBgpVEId"),
)
if mibBuilder.loadTexts:
    vplsBgpVEEntry.setStatus("current")


class _VplsBgpVEId_Type(Unsigned32):
    """Custom type vplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpVEId_Type.__name__ = "Unsigned32"
_VplsBgpVEId_Object = MibTableColumn
vplsBgpVEId = _VplsBgpVEId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1, 1),
    _VplsBgpVEId_Type()
)
vplsBgpVEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsBgpVEId.setStatus("current")


class _VplsBgpVEName_Type(SnmpAdminString):
    """Custom type vplsBgpVEName based on SnmpAdminString"""
    defaultValue = OctetString("")


_VplsBgpVEName_Type.__name__ = "SnmpAdminString"
_VplsBgpVEName_Object = MibTableColumn
vplsBgpVEName = _VplsBgpVEName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1, 2),
    _VplsBgpVEName_Type()
)
vplsBgpVEName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEName.setStatus("current")


class _VplsBgpVEPreference_Type(Unsigned32):
    """Custom type vplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VplsBgpVEPreference_Type.__name__ = "Unsigned32"
_VplsBgpVEPreference_Object = MibTableColumn
vplsBgpVEPreference = _VplsBgpVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1, 3),
    _VplsBgpVEPreference_Type()
)
vplsBgpVEPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEPreference.setStatus("current")
_VplsBgpVERowStatus_Type = RowStatus
_VplsBgpVERowStatus_Object = MibTableColumn
vplsBgpVERowStatus = _VplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1, 5),
    _VplsBgpVERowStatus_Type()
)
vplsBgpVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVERowStatus.setStatus("current")


class _VplsBgpVEStorageType_Type(StorageType):
    """Custom type vplsBgpVEStorageType based on StorageType"""
    defaultValue = 2


_VplsBgpVEStorageType_Type.__name__ = "StorageType"
_VplsBgpVEStorageType_Object = MibTableColumn
vplsBgpVEStorageType = _VplsBgpVEStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 2, 1, 6),
    _VplsBgpVEStorageType_Type()
)
vplsBgpVEStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpVEStorageType.setStatus("current")
_VplsBgpPwBindTable_Object = MibTable
vplsBgpPwBindTable = _VplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 3)
)
if mibBuilder.loadTexts:
    vplsBgpPwBindTable.setStatus("current")
_VplsBgpPwBindEntry_Object = MibTableRow
vplsBgpPwBindEntry = _VplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 3, 1)
)
vplsBgpPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpPwBindEntry.setStatus("current")


class _VplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type vplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_VplsBgpPwBindLocalVEId_Object = MibTableColumn
vplsBgpPwBindLocalVEId = _VplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 3, 1, 1),
    _VplsBgpPwBindLocalVEId_Type()
)
vplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsBgpPwBindLocalVEId.setStatus("current")


class _VplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type vplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_VplsBgpPwBindRemoteVEId_Object = MibTableColumn
vplsBgpPwBindRemoteVEId = _VplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 1, 3, 1, 2),
    _VplsBgpPwBindRemoteVEId_Type()
)
vplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsBgpPwBindRemoteVEId.setStatus("current")
_VplsBgpConformance_ObjectIdentity = ObjectIdentity
vplsBgpConformance = _VplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2)
)
_VplsBgpCompliances_ObjectIdentity = ObjectIdentity
vplsBgpCompliances = _VplsBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 1)
)
_VplsBgpGroups_ObjectIdentity = ObjectIdentity
vplsBgpGroups = _VplsBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 2)
)

# Managed Objects groups

vplsBgpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 2, 1)
)
vplsBgpConfigGroup.setObjects(
    ("ARICENT-VPLS-BGP-MIB", "vplsBgpConfigVERangeSize")
)
if mibBuilder.loadTexts:
    vplsBgpConfigGroup.setStatus("current")

vplsBgpVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 2, 2)
)
vplsBgpVEGroup.setObjects(
      *(("ARICENT-VPLS-BGP-MIB", "vplsBgpVEName"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpVEPreference"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpVERowStatus"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpVEStorageType"))
)
if mibBuilder.loadTexts:
    vplsBgpVEGroup.setStatus("current")

vplsBgpPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 2, 3)
)
vplsBgpPwBindGroup.setObjects(
      *(("ARICENT-VPLS-BGP-MIB", "vplsBgpPwBindLocalVEId"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    vplsBgpPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vplsBgpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 1, 1)
)
vplsBgpModuleFullCompliance.setObjects(
      *(("ARICENT-VPLS-BGP-MIB", "vplsBgpConfigGroup"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpVEGroup"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    vplsBgpModuleFullCompliance.setStatus(
        "current"
    )

vplsBgpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 29601, 2, 86, 2, 1, 2)
)
vplsBgpModuleReadOnlyCompliance.setObjects(
      *(("ARICENT-VPLS-BGP-MIB", "vplsBgpConfigGroup"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpVEGroup"),
        ("ARICENT-VPLS-BGP-MIB", "vplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    vplsBgpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-VPLS-BGP-MIB",
    **{"fsVplsBgpMIB": fsVplsBgpMIB,
       "vplsBgpObjects": vplsBgpObjects,
       "vplsBgpConfigTable": vplsBgpConfigTable,
       "vplsBgpConfigEntry": vplsBgpConfigEntry,
       "vplsBgpConfigVERangeSize": vplsBgpConfigVERangeSize,
       "vplsBgpVETable": vplsBgpVETable,
       "vplsBgpVEEntry": vplsBgpVEEntry,
       "vplsBgpVEId": vplsBgpVEId,
       "vplsBgpVEName": vplsBgpVEName,
       "vplsBgpVEPreference": vplsBgpVEPreference,
       "vplsBgpVERowStatus": vplsBgpVERowStatus,
       "vplsBgpVEStorageType": vplsBgpVEStorageType,
       "vplsBgpPwBindTable": vplsBgpPwBindTable,
       "vplsBgpPwBindEntry": vplsBgpPwBindEntry,
       "vplsBgpPwBindLocalVEId": vplsBgpPwBindLocalVEId,
       "vplsBgpPwBindRemoteVEId": vplsBgpPwBindRemoteVEId,
       "vplsBgpConformance": vplsBgpConformance,
       "vplsBgpCompliances": vplsBgpCompliances,
       "vplsBgpModuleFullCompliance": vplsBgpModuleFullCompliance,
       "vplsBgpModuleReadOnlyCompliance": vplsBgpModuleReadOnlyCompliance,
       "vplsBgpGroups": vplsBgpGroups,
       "vplsBgpConfigGroup": vplsBgpConfigGroup,
       "vplsBgpVEGroup": vplsBgpVEGroup,
       "vplsBgpPwBindGroup": vplsBgpPwBindGroup}
)
