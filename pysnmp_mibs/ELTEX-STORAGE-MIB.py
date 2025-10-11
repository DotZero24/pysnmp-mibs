# SNMP MIB module (ELTEX-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-STORAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:56 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(EltexPercent,
 EltexThresholdRelation) = mibBuilder.importSymbols(
    "ELTEX-TC",
    "EltexPercent",
    "EltexThresholdRelation")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogSeverity")


# MODULE-IDENTITY

eltexStorageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39)
)
if mibBuilder.loadTexts:
    eltexStorageMIB.setRevisions(
        ("2017-05-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexStorageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ramfs", 1),
          ("spi", 2),
          ("raw-nand", 3),
          ("sata", 4),
          ("sd-card", 5),
          ("usb", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EltexStorageMIBObjects_ObjectIdentity = ObjectIdentity
eltexStorageMIBObjects = _EltexStorageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1)
)
_EltexStorageDevice_ObjectIdentity = ObjectIdentity
eltexStorageDevice = _EltexStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1)
)
_EltexStorageDeviceTable_Object = MibTable
eltexStorageDeviceTable = _EltexStorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexStorageDeviceTable.setStatus("current")
_EltexStorageDeviceEntry_Object = MibTableRow
eltexStorageDeviceEntry = _EltexStorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1)
)
eltexStorageDeviceEntry.setIndexNames(
    (0, "ELTEX-STORAGE-MIB", "eltexStorageDeviceIndex"),
)
if mibBuilder.loadTexts:
    eltexStorageDeviceEntry.setStatus("current")
_EltexStorageDeviceIndex_Type = Unsigned32
_EltexStorageDeviceIndex_Object = MibTableColumn
eltexStorageDeviceIndex = _EltexStorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 1),
    _EltexStorageDeviceIndex_Type()
)
eltexStorageDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexStorageDeviceIndex.setStatus("current")
_EltexStorageDevicePhysicalIndex_Type = PhysicalIndex
_EltexStorageDevicePhysicalIndex_Object = MibTableColumn
eltexStorageDevicePhysicalIndex = _EltexStorageDevicePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 2),
    _EltexStorageDevicePhysicalIndex_Type()
)
eltexStorageDevicePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDevicePhysicalIndex.setStatus("current")
_EltexStorageDeviceType_Type = EltexStorageType
_EltexStorageDeviceType_Object = MibTableColumn
eltexStorageDeviceType = _EltexStorageDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 3),
    _EltexStorageDeviceType_Type()
)
eltexStorageDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDeviceType.setStatus("current")
_EltexStorageDeviceSize_Type = Gauge32
_EltexStorageDeviceSize_Object = MibTableColumn
eltexStorageDeviceSize = _EltexStorageDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 4),
    _EltexStorageDeviceSize_Type()
)
eltexStorageDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDeviceSize.setStatus("current")
if mibBuilder.loadTexts:
    eltexStorageDeviceSize.setUnits("bytes")
_EltexStorageDeviceSizeOverflow_Type = Gauge32
_EltexStorageDeviceSizeOverflow_Object = MibTableColumn
eltexStorageDeviceSizeOverflow = _EltexStorageDeviceSizeOverflow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 5),
    _EltexStorageDeviceSizeOverflow_Type()
)
eltexStorageDeviceSizeOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDeviceSizeOverflow.setStatus("current")
if mibBuilder.loadTexts:
    eltexStorageDeviceSizeOverflow.setUnits("bytes")
_EltexStorageDeviceHCSize_Type = Counter64
_EltexStorageDeviceHCSize_Object = MibTableColumn
eltexStorageDeviceHCSize = _EltexStorageDeviceHCSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 6),
    _EltexStorageDeviceHCSize_Type()
)
eltexStorageDeviceHCSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDeviceHCSize.setStatus("current")
if mibBuilder.loadTexts:
    eltexStorageDeviceHCSize.setUnits("bytes")
_EltexStorageDeviceRemovable_Type = TruthValue
_EltexStorageDeviceRemovable_Object = MibTableColumn
eltexStorageDeviceRemovable = _EltexStorageDeviceRemovable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 1, 1, 7),
    _EltexStorageDeviceRemovable_Type()
)
eltexStorageDeviceRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageDeviceRemovable.setStatus("current")
_EltexStoragePartitionTable_Object = MibTable
eltexStoragePartitionTable = _EltexStoragePartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltexStoragePartitionTable.setStatus("current")
_EltexStoragePartitionEntry_Object = MibTableRow
eltexStoragePartitionEntry = _EltexStoragePartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1)
)
eltexStoragePartitionEntry.setIndexNames(
    (0, "ELTEX-STORAGE-MIB", "eltexStorageDeviceIndex"),
    (0, "ELTEX-STORAGE-MIB", "eltexStoragePartitionIndex"),
)
if mibBuilder.loadTexts:
    eltexStoragePartitionEntry.setStatus("current")
_EltexStoragePartitionIndex_Type = Gauge32
_EltexStoragePartitionIndex_Object = MibTableColumn
eltexStoragePartitionIndex = _EltexStoragePartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 1),
    _EltexStoragePartitionIndex_Type()
)
eltexStoragePartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexStoragePartitionIndex.setStatus("current")
_EltexStoragePartitionTotal_Type = Gauge32
_EltexStoragePartitionTotal_Object = MibTableColumn
eltexStoragePartitionTotal = _EltexStoragePartitionTotal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 2),
    _EltexStoragePartitionTotal_Type()
)
eltexStoragePartitionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionTotal.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionTotal.setUnits("bytes")
_EltexStoragePartitionTotalOverflow_Type = Gauge32
_EltexStoragePartitionTotalOverflow_Object = MibTableColumn
eltexStoragePartitionTotalOverflow = _EltexStoragePartitionTotalOverflow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 3),
    _EltexStoragePartitionTotalOverflow_Type()
)
eltexStoragePartitionTotalOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionTotalOverflow.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionTotalOverflow.setUnits("bytes")
_EltexStoragePartitionHCTotal_Type = Counter64
_EltexStoragePartitionHCTotal_Object = MibTableColumn
eltexStoragePartitionHCTotal = _EltexStoragePartitionHCTotal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 4),
    _EltexStoragePartitionHCTotal_Type()
)
eltexStoragePartitionHCTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionHCTotal.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionHCTotal.setUnits("bytes")
_EltexStoragePartitionFreePercent_Type = EltexPercent
_EltexStoragePartitionFreePercent_Object = MibTableColumn
eltexStoragePartitionFreePercent = _EltexStoragePartitionFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 5),
    _EltexStoragePartitionFreePercent_Type()
)
eltexStoragePartitionFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionFreePercent.setStatus("current")
_EltexStoragePartitionFree_Type = Gauge32
_EltexStoragePartitionFree_Object = MibTableColumn
eltexStoragePartitionFree = _EltexStoragePartitionFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 6),
    _EltexStoragePartitionFree_Type()
)
eltexStoragePartitionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionFree.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionFree.setUnits("bytes")
_EltexStoragePartitionFreeOverflow_Type = Gauge32
_EltexStoragePartitionFreeOverflow_Object = MibTableColumn
eltexStoragePartitionFreeOverflow = _EltexStoragePartitionFreeOverflow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 7),
    _EltexStoragePartitionFreeOverflow_Type()
)
eltexStoragePartitionFreeOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionFreeOverflow.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionFreeOverflow.setUnits("bytes")
_EltexStoragePartitionHCFree_Type = Counter64
_EltexStoragePartitionHCFree_Object = MibTableColumn
eltexStoragePartitionHCFree = _EltexStoragePartitionHCFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 8),
    _EltexStoragePartitionHCFree_Type()
)
eltexStoragePartitionHCFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionHCFree.setStatus("current")
if mibBuilder.loadTexts:
    eltexStoragePartitionHCFree.setUnits("bytes")
_EltexStoragePartitionThresholdFreeIndex_Type = Unsigned32
_EltexStoragePartitionThresholdFreeIndex_Object = MibTableColumn
eltexStoragePartitionThresholdFreeIndex = _EltexStoragePartitionThresholdFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 1, 2, 1, 9),
    _EltexStoragePartitionThresholdFreeIndex_Type()
)
eltexStoragePartitionThresholdFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStoragePartitionThresholdFreeIndex.setStatus("current")
_EltexStorageThreshold_ObjectIdentity = ObjectIdentity
eltexStorageThreshold = _EltexStorageThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2)
)


class _EltexStorageThresholdNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexStorageThresholdNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexStorageThresholdNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexStorageThresholdNotificationGlobalEnable_Object = MibScalar
eltexStorageThresholdNotificationGlobalEnable = _EltexStorageThresholdNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 1),
    _EltexStorageThresholdNotificationGlobalEnable_Type()
)
eltexStorageThresholdNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexStorageThresholdNotificationGlobalEnable.setStatus("current")


class _EltexStorageThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexStorageThresholdRecoveryNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexStorageThresholdRecoveryNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexStorageThresholdRecoveryNotificationGlobalEnable_Object = MibScalar
eltexStorageThresholdRecoveryNotificationGlobalEnable = _EltexStorageThresholdRecoveryNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 2),
    _EltexStorageThresholdRecoveryNotificationGlobalEnable_Type()
)
eltexStorageThresholdRecoveryNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexStorageThresholdRecoveryNotificationGlobalEnable.setStatus("current")
_EltexStorageThresholdTable_Object = MibTable
eltexStorageThresholdTable = _EltexStorageThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltexStorageThresholdTable.setStatus("current")
_EltexStorageThresholdEntry_Object = MibTableRow
eltexStorageThresholdEntry = _EltexStorageThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1)
)
eltexStorageThresholdEntry.setIndexNames(
    (0, "ELTEX-STORAGE-MIB", "eltexStorageDeviceIndex"),
    (0, "ELTEX-STORAGE-MIB", "eltexStoragePartitionIndex"),
    (0, "ELTEX-STORAGE-MIB", "eltexStorageThresholdIndex"),
)
if mibBuilder.loadTexts:
    eltexStorageThresholdEntry.setStatus("current")
_EltexStorageThresholdIndex_Type = Unsigned32
_EltexStorageThresholdIndex_Object = MibTableColumn
eltexStorageThresholdIndex = _EltexStorageThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 1),
    _EltexStorageThresholdIndex_Type()
)
eltexStorageThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexStorageThresholdIndex.setStatus("current")
_EltexStorageThresholdRowStatus_Type = RowStatus
_EltexStorageThresholdRowStatus_Object = MibTableColumn
eltexStorageThresholdRowStatus = _EltexStorageThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 2),
    _EltexStorageThresholdRowStatus_Type()
)
eltexStorageThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdRowStatus.setStatus("current")
_EltexStorageThresholdValue_Type = EltexPercent
_EltexStorageThresholdValue_Object = MibTableColumn
eltexStorageThresholdValue = _EltexStorageThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 3),
    _EltexStorageThresholdValue_Type()
)
eltexStorageThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdValue.setStatus("current")


class _EltexStorageThresholdFlappingInterval_Type(EltexPercent):
    """Custom type eltexStorageThresholdFlappingInterval based on EltexPercent"""
    defaultValue = 0


_EltexStorageThresholdFlappingInterval_Type.__name__ = "EltexPercent"
_EltexStorageThresholdFlappingInterval_Object = MibTableColumn
eltexStorageThresholdFlappingInterval = _EltexStorageThresholdFlappingInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 4),
    _EltexStorageThresholdFlappingInterval_Type()
)
eltexStorageThresholdFlappingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdFlappingInterval.setStatus("current")


class _EltexStorageThresholdSeverity_Type(SyslogSeverity):
    """Custom type eltexStorageThresholdSeverity based on SyslogSeverity"""
    defaultValue = 1


_EltexStorageThresholdSeverity_Type.__name__ = "SyslogSeverity"
_EltexStorageThresholdSeverity_Object = MibTableColumn
eltexStorageThresholdSeverity = _EltexStorageThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 5),
    _EltexStorageThresholdSeverity_Type()
)
eltexStorageThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdSeverity.setStatus("current")
_EltexStorageThresholdRelation_Type = EltexThresholdRelation
_EltexStorageThresholdRelation_Object = MibTableColumn
eltexStorageThresholdRelation = _EltexStorageThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 6),
    _EltexStorageThresholdRelation_Type()
)
eltexStorageThresholdRelation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdRelation.setStatus("current")


class _EltexStorageThresholdNotificationEnable_Type(TruthValue):
    """Custom type eltexStorageThresholdNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexStorageThresholdNotificationEnable_Type.__name__ = "TruthValue"
_EltexStorageThresholdNotificationEnable_Object = MibTableColumn
eltexStorageThresholdNotificationEnable = _EltexStorageThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 7),
    _EltexStorageThresholdNotificationEnable_Type()
)
eltexStorageThresholdNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdNotificationEnable.setStatus("current")


class _EltexStorageThresholdRecoveryNotificationEnable_Type(TruthValue):
    """Custom type eltexStorageThresholdRecoveryNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexStorageThresholdRecoveryNotificationEnable_Type.__name__ = "TruthValue"
_EltexStorageThresholdRecoveryNotificationEnable_Object = MibTableColumn
eltexStorageThresholdRecoveryNotificationEnable = _EltexStorageThresholdRecoveryNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 8),
    _EltexStorageThresholdRecoveryNotificationEnable_Type()
)
eltexStorageThresholdRecoveryNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexStorageThresholdRecoveryNotificationEnable.setStatus("current")
_EltexStorageThresholdEvaluation_Type = TruthValue
_EltexStorageThresholdEvaluation_Object = MibTableColumn
eltexStorageThresholdEvaluation = _EltexStorageThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 39, 1, 2, 3, 1, 9),
    _EltexStorageThresholdEvaluation_Type()
)
eltexStorageThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexStorageThresholdEvaluation.setStatus("current")
_EltexStorageMIBNotification_ObjectIdentity = ObjectIdentity
eltexStorageMIBNotification = _EltexStorageMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39, 2)
)
_EltexStorageMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
eltexStorageMIBNotificationPrefix = _EltexStorageMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 39, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexStorageFreeMemoryThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 39, 2, 0, 1)
)
eltexStorageFreeMemoryThresholdNotification.setObjects(
      *(("ELTEX-STORAGE-MIB", "eltexStoragePartitionFreePercent"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdSeverity"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdRelation"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdValue"))
)
if mibBuilder.loadTexts:
    eltexStorageFreeMemoryThresholdNotification.setStatus(
        "current"
    )

eltexStorageFreeMemoryThresholdRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 39, 2, 0, 2)
)
eltexStorageFreeMemoryThresholdRecoveryNotification.setObjects(
      *(("ELTEX-STORAGE-MIB", "eltexStoragePartitionFreePercent"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdSeverity"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdRelation"),
        ("ELTEX-STORAGE-MIB", "eltexStorageThresholdValue"))
)
if mibBuilder.loadTexts:
    eltexStorageFreeMemoryThresholdRecoveryNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-STORAGE-MIB",
    **{"EltexStorageType": EltexStorageType,
       "eltexStorageMIB": eltexStorageMIB,
       "eltexStorageMIBObjects": eltexStorageMIBObjects,
       "eltexStorageDevice": eltexStorageDevice,
       "eltexStorageDeviceTable": eltexStorageDeviceTable,
       "eltexStorageDeviceEntry": eltexStorageDeviceEntry,
       "eltexStorageDeviceIndex": eltexStorageDeviceIndex,
       "eltexStorageDevicePhysicalIndex": eltexStorageDevicePhysicalIndex,
       "eltexStorageDeviceType": eltexStorageDeviceType,
       "eltexStorageDeviceSize": eltexStorageDeviceSize,
       "eltexStorageDeviceSizeOverflow": eltexStorageDeviceSizeOverflow,
       "eltexStorageDeviceHCSize": eltexStorageDeviceHCSize,
       "eltexStorageDeviceRemovable": eltexStorageDeviceRemovable,
       "eltexStoragePartitionTable": eltexStoragePartitionTable,
       "eltexStoragePartitionEntry": eltexStoragePartitionEntry,
       "eltexStoragePartitionIndex": eltexStoragePartitionIndex,
       "eltexStoragePartitionTotal": eltexStoragePartitionTotal,
       "eltexStoragePartitionTotalOverflow": eltexStoragePartitionTotalOverflow,
       "eltexStoragePartitionHCTotal": eltexStoragePartitionHCTotal,
       "eltexStoragePartitionFreePercent": eltexStoragePartitionFreePercent,
       "eltexStoragePartitionFree": eltexStoragePartitionFree,
       "eltexStoragePartitionFreeOverflow": eltexStoragePartitionFreeOverflow,
       "eltexStoragePartitionHCFree": eltexStoragePartitionHCFree,
       "eltexStoragePartitionThresholdFreeIndex": eltexStoragePartitionThresholdFreeIndex,
       "eltexStorageThreshold": eltexStorageThreshold,
       "eltexStorageThresholdNotificationGlobalEnable": eltexStorageThresholdNotificationGlobalEnable,
       "eltexStorageThresholdRecoveryNotificationGlobalEnable": eltexStorageThresholdRecoveryNotificationGlobalEnable,
       "eltexStorageThresholdTable": eltexStorageThresholdTable,
       "eltexStorageThresholdEntry": eltexStorageThresholdEntry,
       "eltexStorageThresholdIndex": eltexStorageThresholdIndex,
       "eltexStorageThresholdRowStatus": eltexStorageThresholdRowStatus,
       "eltexStorageThresholdValue": eltexStorageThresholdValue,
       "eltexStorageThresholdFlappingInterval": eltexStorageThresholdFlappingInterval,
       "eltexStorageThresholdSeverity": eltexStorageThresholdSeverity,
       "eltexStorageThresholdRelation": eltexStorageThresholdRelation,
       "eltexStorageThresholdNotificationEnable": eltexStorageThresholdNotificationEnable,
       "eltexStorageThresholdRecoveryNotificationEnable": eltexStorageThresholdRecoveryNotificationEnable,
       "eltexStorageThresholdEvaluation": eltexStorageThresholdEvaluation,
       "eltexStorageMIBNotification": eltexStorageMIBNotification,
       "eltexStorageMIBNotificationPrefix": eltexStorageMIBNotificationPrefix,
       "eltexStorageFreeMemoryThresholdNotification": eltexStorageFreeMemoryThresholdNotification,
       "eltexStorageFreeMemoryThresholdRecoveryNotification": eltexStorageFreeMemoryThresholdRecoveryNotification}
)
