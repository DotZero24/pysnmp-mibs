# SNMP MIB module (RAD-SSFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-SSFP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:26 2025
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

(PhysicalIndexOrZero,
 entPhysicalAlias) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero",
    "entPhysicalAlias")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(radSpecificDevices,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radSpecificDevices")

(SlotType,) = mibBuilder.importSymbols(
    "RAD-TC",
    "SlotType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

smartSFP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 40, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SmartSfpModuleType(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("miRIC-E1", 2),
          ("miRIC-T1", 3),
          ("miRIC-E3", 4),
          ("miRIC-T3", 5),
          ("miRICi-E1", 6),
          ("miRICi-T1", 7),
          ("miRICi-E3", 8),
          ("miRICi-T3", 9),
          ("miRICi-155", 10),
          ("miRICi-622", 11),
          ("miTOP-E1", 12),
          ("miTOP-E3", 13),
          ("miTOP-T1", 14),
          ("miTOP-T3", 15),
          ("sfp-VDSL-2W", 16))
    )



# MIB Managed Objects in the order of their OIDs

_SmartSfpEvents_ObjectIdentity = ObjectIdentity
smartSfpEvents = _SmartSfpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 0)
)
if mibBuilder.loadTexts:
    smartSfpEvents.setStatus("current")
_SmartSfpTable_Object = MibTable
smartSfpTable = _SmartSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1)
)
if mibBuilder.loadTexts:
    smartSfpTable.setStatus("current")
_SmartSfpEntry_Object = MibTableRow
smartSfpEntry = _SmartSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1)
)
smartSfpEntry.setIndexNames(
    (0, "RAD-SSFP-MIB", "smartSfpSlotIdx"),
    (0, "RAD-SSFP-MIB", "smartSfpPortIdx"),
)
if mibBuilder.loadTexts:
    smartSfpEntry.setStatus("current")
_SmartSfpSlotIdx_Type = SlotType
_SmartSfpSlotIdx_Object = MibTableColumn
smartSfpSlotIdx = _SmartSfpSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 1),
    _SmartSfpSlotIdx_Type()
)
smartSfpSlotIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smartSfpSlotIdx.setStatus("current")
_SmartSfpPortIdx_Type = Integer32
_SmartSfpPortIdx_Object = MibTableColumn
smartSfpPortIdx = _SmartSfpPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 2),
    _SmartSfpPortIdx_Type()
)
smartSfpPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smartSfpPortIdx.setStatus("current")
_SmartSfpRowStatus_Type = RowStatus
_SmartSfpRowStatus_Object = MibTableColumn
smartSfpRowStatus = _SmartSfpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 3),
    _SmartSfpRowStatus_Type()
)
smartSfpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smartSfpRowStatus.setStatus("current")


class _SmartSfpType_Type(SmartSfpModuleType):
    """Custom type smartSfpType based on SmartSfpModuleType"""
    defaultValue = 1


_SmartSfpType_Type.__name__ = "SmartSfpModuleType"
_SmartSfpType_Object = MibTableColumn
smartSfpType = _SmartSfpType_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 4),
    _SmartSfpType_Type()
)
smartSfpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smartSfpType.setStatus("current")


class _SmartSfpAdminStatus_Type(Integer32):
    """Custom type smartSfpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SmartSfpAdminStatus_Type.__name__ = "Integer32"
_SmartSfpAdminStatus_Object = MibTableColumn
smartSfpAdminStatus = _SmartSfpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 5),
    _SmartSfpAdminStatus_Type()
)
smartSfpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smartSfpAdminStatus.setStatus("deprecated")


class _SmartSfpOperState_Type(Integer32):
    """Custom type smartSfpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 1),
          ("offLine", 2),
          ("notInstalled", 3),
          ("mismatch", 4))
    )


_SmartSfpOperState_Type.__name__ = "Integer32"
_SmartSfpOperState_Object = MibTableColumn
smartSfpOperState = _SmartSfpOperState_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 6),
    _SmartSfpOperState_Type()
)
smartSfpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartSfpOperState.setStatus("current")


class _SmartSfpResetCmd_Type(Integer32):
    """Custom type smartSfpResetCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SmartSfpResetCmd_Type.__name__ = "Integer32"
_SmartSfpResetCmd_Object = MibTableColumn
smartSfpResetCmd = _SmartSfpResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 7),
    _SmartSfpResetCmd_Type()
)
smartSfpResetCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smartSfpResetCmd.setStatus("current")
_SmartSfpInstall_Type = SmartSfpModuleType
_SmartSfpInstall_Object = MibTableColumn
smartSfpInstall = _SmartSfpInstall_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 8),
    _SmartSfpInstall_Type()
)
smartSfpInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartSfpInstall.setStatus("current")
_SmartSfpPhysicalIndex_Type = PhysicalIndexOrZero
_SmartSfpPhysicalIndex_Object = MibTableColumn
smartSfpPhysicalIndex = _SmartSfpPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 1, 1, 9),
    _SmartSfpPhysicalIndex_Type()
)
smartSfpPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartSfpPhysicalIndex.setStatus("current")

# Managed Objects groups


# Notification objects

smartSfpMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 40, 2, 0, 1)
)
smartSfpMismatch.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("ENTITY-MIB", "entPhysicalAlias"),
        ("RAD-SSFP-MIB", "smartSfpType"),
        ("RAD-SSFP-MIB", "smartSfpInstall"))
)
if mibBuilder.loadTexts:
    smartSfpMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-SSFP-MIB",
    **{"SmartSfpModuleType": SmartSfpModuleType,
       "smartSFP": smartSFP,
       "smartSfpEvents": smartSfpEvents,
       "smartSfpMismatch": smartSfpMismatch,
       "smartSfpTable": smartSfpTable,
       "smartSfpEntry": smartSfpEntry,
       "smartSfpSlotIdx": smartSfpSlotIdx,
       "smartSfpPortIdx": smartSfpPortIdx,
       "smartSfpRowStatus": smartSfpRowStatus,
       "smartSfpType": smartSfpType,
       "smartSfpAdminStatus": smartSfpAdminStatus,
       "smartSfpOperState": smartSfpOperState,
       "smartSfpResetCmd": smartSfpResetCmd,
       "smartSfpInstall": smartSfpInstall,
       "smartSfpPhysicalIndex": smartSfpPhysicalIndex}
)
