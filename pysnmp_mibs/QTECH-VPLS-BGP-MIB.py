# SNMP MIB module (QTECH-VPLS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VPLS-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:31 2025
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

(qtechvplsConfigIndex,
 qtechvplsPwBindIndex) = mibBuilder.importSymbols(
    "QTECH-VPLS-GENERIC-MIB",
    "qtechvplsConfigIndex",
    "qtechvplsPwBindIndex")

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


# MODULE-IDENTITY

qtechvplsBgpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79)
)
if mibBuilder.loadTexts:
    qtechvplsBgpDraft01MIB.setRevisions(
        ("2010-04-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class QtechVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_QtechvplsBgpObjects_ObjectIdentity = ObjectIdentity
qtechvplsBgpObjects = _QtechvplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1)
)
_QtechvplsBgpVETable_Object = MibTable
qtechvplsBgpVETable = _QtechvplsBgpVETable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1)
)
if mibBuilder.loadTexts:
    qtechvplsBgpVETable.setStatus("current")
_QtechvplsBgpVEEntry_Object = MibTableRow
qtechvplsBgpVEEntry = _QtechvplsBgpVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1)
)
qtechvplsBgpVEEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEindex"),
)
if mibBuilder.loadTexts:
    qtechvplsBgpVEEntry.setStatus("current")


class _QtechvplsBgpVEindex_Type(Unsigned32):
    """Custom type qtechvplsBgpVEindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechvplsBgpVEindex_Type.__name__ = "Unsigned32"
_QtechvplsBgpVEindex_Object = MibTableColumn
qtechvplsBgpVEindex = _QtechvplsBgpVEindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 1),
    _QtechvplsBgpVEindex_Type()
)
qtechvplsBgpVEindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechvplsBgpVEindex.setStatus("current")


class _QtechvplsBgpVEId_Type(Unsigned32):
    """Custom type qtechvplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QtechvplsBgpVEId_Type.__name__ = "Unsigned32"
_QtechvplsBgpVEId_Object = MibTableColumn
qtechvplsBgpVEId = _QtechvplsBgpVEId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 2),
    _QtechvplsBgpVEId_Type()
)
qtechvplsBgpVEId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpVEId.setStatus("current")


class _QtechvplsBgpRangeSize_Type(Unsigned32):
    """Custom type qtechvplsBgpRangeSize based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QtechvplsBgpRangeSize_Type.__name__ = "Unsigned32"
_QtechvplsBgpRangeSize_Object = MibTableColumn
qtechvplsBgpRangeSize = _QtechvplsBgpRangeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 3),
    _QtechvplsBgpRangeSize_Type()
)
qtechvplsBgpRangeSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpRangeSize.setStatus("current")


class _QtechvplsBgpVEPreference_Type(Unsigned32):
    """Custom type qtechvplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_QtechvplsBgpVEPreference_Type.__name__ = "Unsigned32"
_QtechvplsBgpVEPreference_Object = MibTableColumn
qtechvplsBgpVEPreference = _QtechvplsBgpVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 4),
    _QtechvplsBgpVEPreference_Type()
)
qtechvplsBgpVEPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsBgpVEPreference.setStatus("current")
_QtechvplsBgpVERowStatus_Type = RowStatus
_QtechvplsBgpVERowStatus_Object = MibTableColumn
qtechvplsBgpVERowStatus = _QtechvplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 1, 1, 5),
    _QtechvplsBgpVERowStatus_Type()
)
qtechvplsBgpVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpVERowStatus.setStatus("current")
_QtechvplsBgpPwBindTable_Object = MibTable
qtechvplsBgpPwBindTable = _QtechvplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2)
)
if mibBuilder.loadTexts:
    qtechvplsBgpPwBindTable.setStatus("current")
_QtechvplsBgpPwBindEntry_Object = MibTableRow
qtechvplsBgpPwBindEntry = _QtechvplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1)
)
qtechvplsBgpPwBindEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsBgpPwBindEntry.setStatus("current")


class _QtechvplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type qtechvplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QtechvplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_QtechvplsBgpPwBindLocalVEId_Object = MibTableColumn
qtechvplsBgpPwBindLocalVEId = _QtechvplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1, 1),
    _QtechvplsBgpPwBindLocalVEId_Type()
)
qtechvplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsBgpPwBindLocalVEId.setStatus("current")


class _QtechvplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type qtechvplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QtechvplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_QtechvplsBgpPwBindRemoteVEId_Object = MibTableColumn
qtechvplsBgpPwBindRemoteVEId = _QtechvplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 1, 2, 1, 2),
    _QtechvplsBgpPwBindRemoteVEId_Type()
)
qtechvplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsBgpPwBindRemoteVEId.setStatus("current")
_QtechvplsBgpConformance_ObjectIdentity = ObjectIdentity
qtechvplsBgpConformance = _QtechvplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2)
)
_QtechvplsBgpCompliances_ObjectIdentity = ObjectIdentity
qtechvplsBgpCompliances = _QtechvplsBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1)
)
_QtechvplsBgpGroups_ObjectIdentity = ObjectIdentity
qtechvplsBgpGroups = _QtechvplsBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2)
)

# Managed Objects groups

qtechvplsBgpVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2, 2)
)
qtechvplsBgpVEGroup.setObjects(
    ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEPreference")
)
if mibBuilder.loadTexts:
    qtechvplsBgpVEGroup.setStatus("current")

qtechvplsBgpPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 2, 3)
)
qtechvplsBgpPwBindGroup.setObjects(
      *(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindLocalVEId"),
        ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    qtechvplsBgpPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechvplsBgpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1, 1)
)
qtechvplsBgpModuleFullCompliance.setObjects(
      *(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpConfigGroup"),
        ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEGroup"),
        ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsBgpModuleFullCompliance.setStatus(
        "current"
    )

qtechvplsBgpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 79, 2, 1, 2)
)
qtechvplsBgpModuleReadOnlyCompliance.setObjects(
      *(("QTECH-VPLS-BGP-MIB", "qtechvplsBgpConfigGroup"),
        ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpVEGroup"),
        ("QTECH-VPLS-BGP-MIB", "qtechvplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsBgpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VPLS-BGP-MIB",
    **{"QtechVplsBgpRouteDistinguisher": QtechVplsBgpRouteDistinguisher,
       "QtechVplsBgpRouteTarget": QtechVplsBgpRouteTarget,
       "qtechvplsBgpDraft01MIB": qtechvplsBgpDraft01MIB,
       "qtechvplsBgpObjects": qtechvplsBgpObjects,
       "qtechvplsBgpVETable": qtechvplsBgpVETable,
       "qtechvplsBgpVEEntry": qtechvplsBgpVEEntry,
       "qtechvplsBgpVEindex": qtechvplsBgpVEindex,
       "qtechvplsBgpVEId": qtechvplsBgpVEId,
       "qtechvplsBgpRangeSize": qtechvplsBgpRangeSize,
       "qtechvplsBgpVEPreference": qtechvplsBgpVEPreference,
       "qtechvplsBgpVERowStatus": qtechvplsBgpVERowStatus,
       "qtechvplsBgpPwBindTable": qtechvplsBgpPwBindTable,
       "qtechvplsBgpPwBindEntry": qtechvplsBgpPwBindEntry,
       "qtechvplsBgpPwBindLocalVEId": qtechvplsBgpPwBindLocalVEId,
       "qtechvplsBgpPwBindRemoteVEId": qtechvplsBgpPwBindRemoteVEId,
       "qtechvplsBgpConformance": qtechvplsBgpConformance,
       "qtechvplsBgpCompliances": qtechvplsBgpCompliances,
       "qtechvplsBgpModuleFullCompliance": qtechvplsBgpModuleFullCompliance,
       "qtechvplsBgpModuleReadOnlyCompliance": qtechvplsBgpModuleReadOnlyCompliance,
       "qtechvplsBgpGroups": qtechvplsBgpGroups,
       "qtechvplsBgpVEGroup": qtechvplsBgpVEGroup,
       "qtechvplsBgpPwBindGroup": qtechvplsBgpPwBindGroup}
)
