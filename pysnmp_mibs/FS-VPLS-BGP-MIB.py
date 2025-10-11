# SNMP MIB module (FS-VPLS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VPLS-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:28 2025
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

(fsvplsConfigIndex,
 fsvplsPwBindIndex) = mibBuilder.importSymbols(
    "FS-VPLS-GENERIC-MIB",
    "fsvplsConfigIndex",
    "fsvplsPwBindIndex")

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

fsvplsBgpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79)
)
if mibBuilder.loadTexts:
    fsvplsBgpDraft01MIB.setRevisions(
        ("2010-04-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class FSVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_FsvplsBgpObjects_ObjectIdentity = ObjectIdentity
fsvplsBgpObjects = _FsvplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1)
)
_FsvplsBgpVETable_Object = MibTable
fsvplsBgpVETable = _FsvplsBgpVETable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1)
)
if mibBuilder.loadTexts:
    fsvplsBgpVETable.setStatus("current")
_FsvplsBgpVEEntry_Object = MibTableRow
fsvplsBgpVEEntry = _FsvplsBgpVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1)
)
fsvplsBgpVEEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-BGP-MIB", "fsvplsBgpVEindex"),
)
if mibBuilder.loadTexts:
    fsvplsBgpVEEntry.setStatus("current")


class _FsvplsBgpVEindex_Type(Unsigned32):
    """Custom type fsvplsBgpVEindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsvplsBgpVEindex_Type.__name__ = "Unsigned32"
_FsvplsBgpVEindex_Object = MibTableColumn
fsvplsBgpVEindex = _FsvplsBgpVEindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 1),
    _FsvplsBgpVEindex_Type()
)
fsvplsBgpVEindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsvplsBgpVEindex.setStatus("current")


class _FsvplsBgpVEId_Type(Unsigned32):
    """Custom type fsvplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsvplsBgpVEId_Type.__name__ = "Unsigned32"
_FsvplsBgpVEId_Object = MibTableColumn
fsvplsBgpVEId = _FsvplsBgpVEId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 2),
    _FsvplsBgpVEId_Type()
)
fsvplsBgpVEId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpVEId.setStatus("current")


class _FsvplsBgpRangeSize_Type(Unsigned32):
    """Custom type fsvplsBgpRangeSize based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsvplsBgpRangeSize_Type.__name__ = "Unsigned32"
_FsvplsBgpRangeSize_Object = MibTableColumn
fsvplsBgpRangeSize = _FsvplsBgpRangeSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 3),
    _FsvplsBgpRangeSize_Type()
)
fsvplsBgpRangeSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpRangeSize.setStatus("current")


class _FsvplsBgpVEPreference_Type(Unsigned32):
    """Custom type fsvplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_FsvplsBgpVEPreference_Type.__name__ = "Unsigned32"
_FsvplsBgpVEPreference_Object = MibTableColumn
fsvplsBgpVEPreference = _FsvplsBgpVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 4),
    _FsvplsBgpVEPreference_Type()
)
fsvplsBgpVEPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsBgpVEPreference.setStatus("current")
_FsvplsBgpVERowStatus_Type = RowStatus
_FsvplsBgpVERowStatus_Object = MibTableColumn
fsvplsBgpVERowStatus = _FsvplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 1, 1, 5),
    _FsvplsBgpVERowStatus_Type()
)
fsvplsBgpVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpVERowStatus.setStatus("current")
_FsvplsBgpPwBindTable_Object = MibTable
fsvplsBgpPwBindTable = _FsvplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2)
)
if mibBuilder.loadTexts:
    fsvplsBgpPwBindTable.setStatus("current")
_FsvplsBgpPwBindEntry_Object = MibTableRow
fsvplsBgpPwBindEntry = _FsvplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1)
)
fsvplsBgpPwBindEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    fsvplsBgpPwBindEntry.setStatus("current")


class _FsvplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type fsvplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsvplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_FsvplsBgpPwBindLocalVEId_Object = MibTableColumn
fsvplsBgpPwBindLocalVEId = _FsvplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1, 1),
    _FsvplsBgpPwBindLocalVEId_Type()
)
fsvplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsBgpPwBindLocalVEId.setStatus("current")


class _FsvplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type fsvplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FsvplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_FsvplsBgpPwBindRemoteVEId_Object = MibTableColumn
fsvplsBgpPwBindRemoteVEId = _FsvplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 1, 2, 1, 2),
    _FsvplsBgpPwBindRemoteVEId_Type()
)
fsvplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsBgpPwBindRemoteVEId.setStatus("current")
_FsvplsBgpConformance_ObjectIdentity = ObjectIdentity
fsvplsBgpConformance = _FsvplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2)
)
_FsvplsBgpCompliances_ObjectIdentity = ObjectIdentity
fsvplsBgpCompliances = _FsvplsBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1)
)
_FsvplsBgpGroups_ObjectIdentity = ObjectIdentity
fsvplsBgpGroups = _FsvplsBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2)
)

# Managed Objects groups

fsvplsBgpVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2, 2)
)
fsvplsBgpVEGroup.setObjects(
    ("FS-VPLS-BGP-MIB", "fsvplsBgpVEPreference")
)
if mibBuilder.loadTexts:
    fsvplsBgpVEGroup.setStatus("current")

fsvplsBgpPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 2, 3)
)
fsvplsBgpPwBindGroup.setObjects(
      *(("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindLocalVEId"),
        ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    fsvplsBgpPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsvplsBgpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1, 1)
)
fsvplsBgpModuleFullCompliance.setObjects(
      *(("FS-VPLS-BGP-MIB", "fsvplsBgpVEGroup"),
        ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    fsvplsBgpModuleFullCompliance.setStatus(
        "current"
    )

fsvplsBgpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 79, 2, 1, 2)
)
fsvplsBgpModuleReadOnlyCompliance.setObjects(
      *(("FS-VPLS-BGP-MIB", "fsvplsBgpVEGroup"),
        ("FS-VPLS-BGP-MIB", "fsvplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    fsvplsBgpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VPLS-BGP-MIB",
    **{"FSVplsBgpRouteDistinguisher": FSVplsBgpRouteDistinguisher,
       "FSVplsBgpRouteTarget": FSVplsBgpRouteTarget,
       "fsvplsBgpDraft01MIB": fsvplsBgpDraft01MIB,
       "fsvplsBgpObjects": fsvplsBgpObjects,
       "fsvplsBgpVETable": fsvplsBgpVETable,
       "fsvplsBgpVEEntry": fsvplsBgpVEEntry,
       "fsvplsBgpVEindex": fsvplsBgpVEindex,
       "fsvplsBgpVEId": fsvplsBgpVEId,
       "fsvplsBgpRangeSize": fsvplsBgpRangeSize,
       "fsvplsBgpVEPreference": fsvplsBgpVEPreference,
       "fsvplsBgpVERowStatus": fsvplsBgpVERowStatus,
       "fsvplsBgpPwBindTable": fsvplsBgpPwBindTable,
       "fsvplsBgpPwBindEntry": fsvplsBgpPwBindEntry,
       "fsvplsBgpPwBindLocalVEId": fsvplsBgpPwBindLocalVEId,
       "fsvplsBgpPwBindRemoteVEId": fsvplsBgpPwBindRemoteVEId,
       "fsvplsBgpConformance": fsvplsBgpConformance,
       "fsvplsBgpCompliances": fsvplsBgpCompliances,
       "fsvplsBgpModuleFullCompliance": fsvplsBgpModuleFullCompliance,
       "fsvplsBgpModuleReadOnlyCompliance": fsvplsBgpModuleReadOnlyCompliance,
       "fsvplsBgpGroups": fsvplsBgpGroups,
       "fsvplsBgpVEGroup": fsvplsBgpVEGroup,
       "fsvplsBgpPwBindGroup": fsvplsBgpPwBindGroup}
)
