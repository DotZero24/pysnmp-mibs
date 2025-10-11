# SNMP MIB module (ENTERASYS-HIGH-AVAILABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-HIGH-AVAILABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:54 2025
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

etsysHighAvailabilityUpgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84)
)
if mibBuilder.loadTexts:
    etsysHighAvailabilityUpgradeMIB.setRevisions(
        ("2011-12-12 15:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysHauSystemStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hauDisabled", 1),
          ("hauPending", 2),
          ("hauRunning", 3),
          ("hauHalted", 4),
          ("hauSuccess", 5),
          ("hauError", 6),
          ("hauForceComplete", 7))
    )



class EtsysHauMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hauNever", 1),
          ("hauIfPossible", 2),
          ("hauAlways", 3))
    )



class HauSlotList(TextualConvention, OctetString):
    status = "current"


class HauSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysHauObjects_ObjectIdentity = ObjectIdentity
etsysHauObjects = _EtsysHauObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1)
)
_EtsysHauStats_ObjectIdentity = ObjectIdentity
etsysHauStats = _EtsysHauStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1)
)
_EtsysHauStatsStatus_Type = EtsysHauSystemStatus
_EtsysHauStatsStatus_Object = MibScalar
etsysHauStatsStatus = _EtsysHauStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 1),
    _EtsysHauStatsStatus_Type()
)
etsysHauStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsStatus.setStatus("current")
_EtsysHauStatsOriginalImage_Type = SnmpAdminString
_EtsysHauStatsOriginalImage_Object = MibScalar
etsysHauStatsOriginalImage = _EtsysHauStatsOriginalImage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 2),
    _EtsysHauStatsOriginalImage_Type()
)
etsysHauStatsOriginalImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsOriginalImage.setStatus("current")
_EtsysHauStatsTargetImage_Type = SnmpAdminString
_EtsysHauStatsTargetImage_Object = MibScalar
etsysHauStatsTargetImage = _EtsysHauStatsTargetImage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 3),
    _EtsysHauStatsTargetImage_Type()
)
etsysHauStatsTargetImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsTargetImage.setStatus("current")
_EtsysHauStatsPendingSlotList_Type = HauSlotList
_EtsysHauStatsPendingSlotList_Object = MibScalar
etsysHauStatsPendingSlotList = _EtsysHauStatsPendingSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 4),
    _EtsysHauStatsPendingSlotList_Type()
)
etsysHauStatsPendingSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsPendingSlotList.setStatus("current")
_EtsysHauStatsInProgressSlotList_Type = HauSlotList
_EtsysHauStatsInProgressSlotList_Object = MibScalar
etsysHauStatsInProgressSlotList = _EtsysHauStatsInProgressSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 5),
    _EtsysHauStatsInProgressSlotList_Type()
)
etsysHauStatsInProgressSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsInProgressSlotList.setStatus("current")
_EtsysHauStatsUpgradedSlotList_Type = HauSlotList
_EtsysHauStatsUpgradedSlotList_Object = MibScalar
etsysHauStatsUpgradedSlotList = _EtsysHauStatsUpgradedSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 6),
    _EtsysHauStatsUpgradedSlotList_Type()
)
etsysHauStatsUpgradedSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsUpgradedSlotList.setStatus("current")
_EtsysHauStatsErrorSlotList_Type = HauSlotList
_EtsysHauStatsErrorSlotList_Object = MibScalar
etsysHauStatsErrorSlotList = _EtsysHauStatsErrorSlotList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 7),
    _EtsysHauStatsErrorSlotList_Type()
)
etsysHauStatsErrorSlotList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsErrorSlotList.setStatus("current")
_EtsysHauStatsStartTime_Type = DateAndTime
_EtsysHauStatsStartTime_Object = MibScalar
etsysHauStatsStartTime = _EtsysHauStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 8),
    _EtsysHauStatsStartTime_Type()
)
etsysHauStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsStartTime.setStatus("current")
_EtsysHauStatsDuration_Type = TimeInterval
_EtsysHauStatsDuration_Object = MibScalar
etsysHauStatsDuration = _EtsysHauStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 1, 9),
    _EtsysHauStatsDuration_Type()
)
etsysHauStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauStatsDuration.setStatus("current")
_EtsysHauSystem_ObjectIdentity = ObjectIdentity
etsysHauSystem = _EtsysHauSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2)
)


class _EtsysHauSystemInterGroupDelay_Type(Unsigned32):
    """Custom type etsysHauSystemInterGroupDelay based on Unsigned32"""
    defaultValue = 15


_EtsysHauSystemInterGroupDelay_Type.__name__ = "Unsigned32"
_EtsysHauSystemInterGroupDelay_Object = MibScalar
etsysHauSystemInterGroupDelay = _EtsysHauSystemInterGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2, 1),
    _EtsysHauSystemInterGroupDelay_Type()
)
etsysHauSystemInterGroupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysHauSystemInterGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysHauSystemInterGroupDelay.setUnits("seconds")
_EtsysHauSystemHauMode_Type = EtsysHauMode
_EtsysHauSystemHauMode_Object = MibScalar
etsysHauSystemHauMode = _EtsysHauSystemHauMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 2, 2),
    _EtsysHauSystemHauMode_Type()
)
etsysHauSystemHauMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysHauSystemHauMode.setStatus("current")
_EtsysHauModule_ObjectIdentity = ObjectIdentity
etsysHauModule = _EtsysHauModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3)
)
_EtsysHauModuleTable_Object = MibTable
etsysHauModuleTable = _EtsysHauModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysHauModuleTable.setStatus("current")
_EtsysHauModuleEntry_Object = MibTableRow
etsysHauModuleEntry = _EtsysHauModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1)
)
etsysHauModuleEntry.setIndexNames(
    (0, "ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleSlot"),
)
if mibBuilder.loadTexts:
    etsysHauModuleEntry.setStatus("current")
_EtsysHauModuleSlot_Type = HauSlot
_EtsysHauModuleSlot_Object = MibTableColumn
etsysHauModuleSlot = _EtsysHauModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 1),
    _EtsysHauModuleSlot_Type()
)
etsysHauModuleSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysHauModuleSlot.setStatus("current")
_EtsysHauModuleEntRef_Type = PhysicalIndex
_EtsysHauModuleEntRef_Object = MibTableColumn
etsysHauModuleEntRef = _EtsysHauModuleEntRef_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 2),
    _EtsysHauModuleEntRef_Type()
)
etsysHauModuleEntRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysHauModuleEntRef.setStatus("current")


class _EtsysHauModuleGroupId_Type(Unsigned32):
    """Custom type etsysHauModuleGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EtsysHauModuleGroupId_Type.__name__ = "Unsigned32"
_EtsysHauModuleGroupId_Object = MibTableColumn
etsysHauModuleGroupId = _EtsysHauModuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 1, 3, 1, 1, 3),
    _EtsysHauModuleGroupId_Type()
)
etsysHauModuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysHauModuleGroupId.setStatus("current")
_EtsysHauConformance_ObjectIdentity = ObjectIdentity
etsysHauConformance = _EtsysHauConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2)
)
_EtsysHauGroups_ObjectIdentity = ObjectIdentity
etsysHauGroups = _EtsysHauGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1)
)
_EtsysHauCompliances_ObjectIdentity = ObjectIdentity
etsysHauCompliances = _EtsysHauCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 2)
)

# Managed Objects groups

etsysHauSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1, 1)
)
etsysHauSystemGroup.setObjects(
      *(("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemInterGroupDelay"),
        ("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemHauMode"))
)
if mibBuilder.loadTexts:
    etsysHauSystemGroup.setStatus("current")

etsysHauModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 1, 2)
)
etsysHauModuleGroup.setObjects(
    ("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleGroupId")
)
if mibBuilder.loadTexts:
    etsysHauModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysHauCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 84, 2, 2, 1)
)
etsysHauCompliance.setObjects(
      *(("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauSystemGroup"),
        ("ENTERASYS-HIGH-AVAILABILITY-MIB", "etsysHauModuleGroup"))
)
if mibBuilder.loadTexts:
    etsysHauCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-HIGH-AVAILABILITY-MIB",
    **{"EtsysHauSystemStatus": EtsysHauSystemStatus,
       "EtsysHauMode": EtsysHauMode,
       "HauSlotList": HauSlotList,
       "HauSlot": HauSlot,
       "etsysHighAvailabilityUpgradeMIB": etsysHighAvailabilityUpgradeMIB,
       "etsysHauObjects": etsysHauObjects,
       "etsysHauStats": etsysHauStats,
       "etsysHauStatsStatus": etsysHauStatsStatus,
       "etsysHauStatsOriginalImage": etsysHauStatsOriginalImage,
       "etsysHauStatsTargetImage": etsysHauStatsTargetImage,
       "etsysHauStatsPendingSlotList": etsysHauStatsPendingSlotList,
       "etsysHauStatsInProgressSlotList": etsysHauStatsInProgressSlotList,
       "etsysHauStatsUpgradedSlotList": etsysHauStatsUpgradedSlotList,
       "etsysHauStatsErrorSlotList": etsysHauStatsErrorSlotList,
       "etsysHauStatsStartTime": etsysHauStatsStartTime,
       "etsysHauStatsDuration": etsysHauStatsDuration,
       "etsysHauSystem": etsysHauSystem,
       "etsysHauSystemInterGroupDelay": etsysHauSystemInterGroupDelay,
       "etsysHauSystemHauMode": etsysHauSystemHauMode,
       "etsysHauModule": etsysHauModule,
       "etsysHauModuleTable": etsysHauModuleTable,
       "etsysHauModuleEntry": etsysHauModuleEntry,
       "etsysHauModuleSlot": etsysHauModuleSlot,
       "etsysHauModuleEntRef": etsysHauModuleEntRef,
       "etsysHauModuleGroupId": etsysHauModuleGroupId,
       "etsysHauConformance": etsysHauConformance,
       "etsysHauGroups": etsysHauGroups,
       "etsysHauSystemGroup": etsysHauSystemGroup,
       "etsysHauModuleGroup": etsysHauModuleGroup,
       "etsysHauCompliances": etsysHauCompliances,
       "etsysHauCompliance": etsysHauCompliance}
)
