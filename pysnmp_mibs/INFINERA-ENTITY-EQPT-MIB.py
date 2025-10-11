# SNMP MIB module (INFINERA-ENTITY-EQPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-EQPT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:37 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(commonEquipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonEquipment")

(FloatArbitraryPrecision,
 FloatHundredths,
 FloatTenths,
 InfnAdminState,
 InfnArc,
 InfnAvailabilityState,
 InfnCircuitPackType,
 InfnCorrelatedRedunStatus,
 InfnEqptType,
 InfnLastRebootReason,
 InfnOperationalState,
 InfnOpsQualifierList) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "FloatTenths",
    "InfnAdminState",
    "InfnArc",
    "InfnAvailabilityState",
    "InfnCircuitPackType",
    "InfnCorrelatedRedunStatus",
    "InfnEqptType",
    "InfnLastRebootReason",
    "InfnOperationalState",
    "InfnOpsQualifierList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eqptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqptTable_Object = MibTable
eqptTable = _EqptTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    eqptTable.setStatus("current")
_EqptEntry_Object = MibTableRow
eqptEntry = _EqptEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1)
)
eqptEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    eqptEntry.setStatus("current")
_EqptMoId_Type = DisplayString
_EqptMoId_Object = MibTableColumn
eqptMoId = _EqptMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 1),
    _EqptMoId_Type()
)
eqptMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptMoId.setStatus("current")
_EqptLabel_Type = DisplayString
_EqptLabel_Object = MibTableColumn
eqptLabel = _EqptLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 2),
    _EqptLabel_Type()
)
eqptLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptLabel.setStatus("current")


class _EqptAdministrativeState_Type(InfnAdminState):
    """Custom type eqptAdministrativeState based on InfnAdminState"""
    defaultValue = 3


_EqptAdministrativeState_Type.__name__ = "InfnAdminState"
_EqptAdministrativeState_Object = MibTableColumn
eqptAdministrativeState = _EqptAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 3),
    _EqptAdministrativeState_Type()
)
eqptAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptAdministrativeState.setStatus("current")
_EqptOperationalState_Type = InfnOperationalState
_EqptOperationalState_Object = MibTableColumn
eqptOperationalState = _EqptOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 4),
    _EqptOperationalState_Type()
)
eqptOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptOperationalState.setStatus("current")
_EqptAvailabilityState_Type = InfnAvailabilityState
_EqptAvailabilityState_Object = MibTableColumn
eqptAvailabilityState = _EqptAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 5),
    _EqptAvailabilityState_Type()
)
eqptAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAvailabilityState.setStatus("current")


class _EqptAlarmReportControl_Type(InfnArc):
    """Custom type eqptAlarmReportControl based on InfnArc"""
    defaultValue = 1


_EqptAlarmReportControl_Type.__name__ = "InfnArc"
_EqptAlarmReportControl_Object = MibTableColumn
eqptAlarmReportControl = _EqptAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 6),
    _EqptAlarmReportControl_Type()
)
eqptAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptAlarmReportControl.setStatus("current")
_EqptOpStateQualifierList_Type = InfnOpsQualifierList
_EqptOpStateQualifierList_Object = MibTableColumn
eqptOpStateQualifierList = _EqptOpStateQualifierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 7),
    _EqptOpStateQualifierList_Type()
)
eqptOpStateQualifierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptOpStateQualifierList.setStatus("current")
_EqptAlarmInhibitState_Type = InfnArc
_EqptAlarmInhibitState_Object = MibTableColumn
eqptAlarmInhibitState = _EqptAlarmInhibitState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 8),
    _EqptAlarmInhibitState_Type()
)
eqptAlarmInhibitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInhibitState.setStatus("current")
_EqptProvEqptType_Type = InfnEqptType
_EqptProvEqptType_Object = MibTableColumn
eqptProvEqptType = _EqptProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 9),
    _EqptProvEqptType_Type()
)
eqptProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptProvEqptType.setStatus("current")
_EqptInstalledEqptType_Type = InfnEqptType
_EqptInstalledEqptType_Object = MibTableColumn
eqptInstalledEqptType = _EqptInstalledEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 10),
    _EqptInstalledEqptType_Type()
)
eqptInstalledEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptInstalledEqptType.setStatus("current")
_EqptBaseCircuitPackType_Type = InfnCircuitPackType
_EqptBaseCircuitPackType_Object = MibTableColumn
eqptBaseCircuitPackType = _EqptBaseCircuitPackType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 11),
    _EqptBaseCircuitPackType_Type()
)
eqptBaseCircuitPackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptBaseCircuitPackType.setStatus("current")
_EqptCLEI_Type = DisplayString
_EqptCLEI_Object = MibTableColumn
eqptCLEI = _EqptCLEI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 12),
    _EqptCLEI_Type()
)
eqptCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptCLEI.setStatus("current")


class _EqptSAFpgaUpgradePending_Type(Integer32):
    """Custom type eqptSAFpgaUpgradePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sa", 2))
    )


_EqptSAFpgaUpgradePending_Type.__name__ = "Integer32"
_EqptSAFpgaUpgradePending_Object = MibTableColumn
eqptSAFpgaUpgradePending = _EqptSAFpgaUpgradePending_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 13),
    _EqptSAFpgaUpgradePending_Type()
)
eqptSAFpgaUpgradePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptSAFpgaUpgradePending.setStatus("current")


class _EqptSAFpgaUpgradeFlag_Type(Integer32):
    """Custom type eqptSAFpgaUpgradeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upgradeOnNextColdBoot", 1),
          ("doNotUpgrade", 2),
          ("upgradeOnNextWarmBoot", 3))
    )


_EqptSAFpgaUpgradeFlag_Type.__name__ = "Integer32"
_EqptSAFpgaUpgradeFlag_Object = MibTableColumn
eqptSAFpgaUpgradeFlag = _EqptSAFpgaUpgradeFlag_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 14),
    _EqptSAFpgaUpgradeFlag_Type()
)
eqptSAFpgaUpgradeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptSAFpgaUpgradeFlag.setStatus("current")
_EqptEqptMaxPowerDraw_Type = FloatHundredths
_EqptEqptMaxPowerDraw_Object = MibTableColumn
eqptEqptMaxPowerDraw = _EqptEqptMaxPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 15),
    _EqptEqptMaxPowerDraw_Type()
)
eqptEqptMaxPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptEqptMaxPowerDraw.setStatus("current")
_EqptLastRebootTime_Type = DisplayString
_EqptLastRebootTime_Object = MibTableColumn
eqptLastRebootTime = _EqptLastRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 16),
    _EqptLastRebootTime_Type()
)
eqptLastRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptLastRebootTime.setStatus("current")
_EqptLastRebootReason_Type = InfnLastRebootReason
_EqptLastRebootReason_Object = MibTableColumn
eqptLastRebootReason = _EqptLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 17),
    _EqptLastRebootReason_Type()
)
eqptLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptLastRebootReason.setStatus("current")
_EqptInletTemp_Type = FloatArbitraryPrecision
_EqptInletTemp_Object = MibTableColumn
eqptInletTemp = _EqptInletTemp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 18),
    _EqptInletTemp_Type()
)
eqptInletTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptInletTemp.setStatus("current")
if mibBuilder.loadTexts:
    eqptInletTemp.setUnits("degrees Celcius")
_EqptOutletTemp_Type = FloatArbitraryPrecision
_EqptOutletTemp_Object = MibTableColumn
eqptOutletTemp = _EqptOutletTemp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 19),
    _EqptOutletTemp_Type()
)
eqptOutletTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptOutletTemp.setStatus("current")
if mibBuilder.loadTexts:
    eqptOutletTemp.setUnits("degrees Celcius")
_EqptPartNumber_Type = DisplayString
_EqptPartNumber_Object = MibTableColumn
eqptPartNumber = _EqptPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 20),
    _EqptPartNumber_Type()
)
eqptPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptPartNumber.setStatus("current")
_EqptSerialNumber_Type = DisplayString
_EqptSerialNumber_Object = MibTableColumn
eqptSerialNumber = _EqptSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 21),
    _EqptSerialNumber_Type()
)
eqptSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptSerialNumber.setStatus("current")
_EqptManufacturedDate_Type = DisplayString
_EqptManufacturedDate_Object = MibTableColumn
eqptManufacturedDate = _EqptManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 22),
    _EqptManufacturedDate_Type()
)
eqptManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptManufacturedDate.setStatus("current")
_EqptVendorId_Type = DisplayString
_EqptVendorId_Object = MibTableColumn
eqptVendorId = _EqptVendorId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 23),
    _EqptVendorId_Type()
)
eqptVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptVendorId.setStatus("current")
_EqptHardwareVersion_Type = DisplayString
_EqptHardwareVersion_Object = MibTableColumn
eqptHardwareVersion = _EqptHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 24),
    _EqptHardwareVersion_Type()
)
eqptHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptHardwareVersion.setStatus("current")
_EqptFirmwareVersion_Type = DisplayString
_EqptFirmwareVersion_Object = MibTableColumn
eqptFirmwareVersion = _EqptFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 25),
    _EqptFirmwareVersion_Type()
)
eqptFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptFirmwareVersion.setStatus("current")
_EqptPON_Type = DisplayString
_EqptPON_Object = MibTableColumn
eqptPON = _EqptPON_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 26),
    _EqptPON_Type()
)
eqptPON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptPON.setStatus("current")
_EqptUniversalSlotUsage_Type = Integer32
_EqptUniversalSlotUsage_Object = MibTableColumn
eqptUniversalSlotUsage = _EqptUniversalSlotUsage_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 27),
    _EqptUniversalSlotUsage_Type()
)
eqptUniversalSlotUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptUniversalSlotUsage.setStatus("current")
_EqptFruInsertionDate_Type = DisplayString
_EqptFruInsertionDate_Object = MibTableColumn
eqptFruInsertionDate = _EqptFruInsertionDate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 28),
    _EqptFruInsertionDate_Type()
)
eqptFruInsertionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptFruInsertionDate.setStatus("current")
_EqptRedundancyStatus_Type = InfnCorrelatedRedunStatus
_EqptRedundancyStatus_Object = MibTableColumn
eqptRedundancyStatus = _EqptRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 1, 1, 29),
    _EqptRedundancyStatus_Type()
)
eqptRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptRedundancyStatus.setStatus("current")
_EqptConformance_ObjectIdentity = ObjectIdentity
eqptConformance = _EqptConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 3)
)
_EqptCompliances_ObjectIdentity = ObjectIdentity
eqptCompliances = _EqptCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 3, 1)
)
_EqptGroups_ObjectIdentity = ObjectIdentity
eqptGroups = _EqptGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 3, 2)
)

# Managed Objects groups

eqptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 3, 2, 1)
)
eqptGroup.setObjects(
      *(("INFINERA-ENTITY-EQPT-MIB", "eqptMoId"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptLabel"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptAdministrativeState"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptOperationalState"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptAvailabilityState"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptAlarmReportControl"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptOpStateQualifierList"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptAlarmInhibitState"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptProvEqptType"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptInstalledEqptType"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptBaseCircuitPackType"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptCLEI"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptSAFpgaUpgradePending"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptSAFpgaUpgradeFlag"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptEqptMaxPowerDraw"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptLastRebootTime"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptLastRebootReason"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptInletTemp"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptOutletTemp"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptPartNumber"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptSerialNumber"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptManufacturedDate"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptVendorId"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptHardwareVersion"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptFirmwareVersion"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptPON"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptUniversalSlotUsage"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptFruInsertionDate"),
        ("INFINERA-ENTITY-EQPT-MIB", "eqptRedundancyStatus"))
)
if mibBuilder.loadTexts:
    eqptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

eqptCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 1, 3, 1, 1)
)
eqptCompliance.setObjects(
    ("INFINERA-ENTITY-EQPT-MIB", "eqptGroup")
)
if mibBuilder.loadTexts:
    eqptCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-EQPT-MIB",
    **{"eqptMIB": eqptMIB,
       "eqptTable": eqptTable,
       "eqptEntry": eqptEntry,
       "eqptMoId": eqptMoId,
       "eqptLabel": eqptLabel,
       "eqptAdministrativeState": eqptAdministrativeState,
       "eqptOperationalState": eqptOperationalState,
       "eqptAvailabilityState": eqptAvailabilityState,
       "eqptAlarmReportControl": eqptAlarmReportControl,
       "eqptOpStateQualifierList": eqptOpStateQualifierList,
       "eqptAlarmInhibitState": eqptAlarmInhibitState,
       "eqptProvEqptType": eqptProvEqptType,
       "eqptInstalledEqptType": eqptInstalledEqptType,
       "eqptBaseCircuitPackType": eqptBaseCircuitPackType,
       "eqptCLEI": eqptCLEI,
       "eqptSAFpgaUpgradePending": eqptSAFpgaUpgradePending,
       "eqptSAFpgaUpgradeFlag": eqptSAFpgaUpgradeFlag,
       "eqptEqptMaxPowerDraw": eqptEqptMaxPowerDraw,
       "eqptLastRebootTime": eqptLastRebootTime,
       "eqptLastRebootReason": eqptLastRebootReason,
       "eqptInletTemp": eqptInletTemp,
       "eqptOutletTemp": eqptOutletTemp,
       "eqptPartNumber": eqptPartNumber,
       "eqptSerialNumber": eqptSerialNumber,
       "eqptManufacturedDate": eqptManufacturedDate,
       "eqptVendorId": eqptVendorId,
       "eqptHardwareVersion": eqptHardwareVersion,
       "eqptFirmwareVersion": eqptFirmwareVersion,
       "eqptPON": eqptPON,
       "eqptUniversalSlotUsage": eqptUniversalSlotUsage,
       "eqptFruInsertionDate": eqptFruInsertionDate,
       "eqptRedundancyStatus": eqptRedundancyStatus,
       "eqptConformance": eqptConformance,
       "eqptCompliances": eqptCompliances,
       "eqptCompliance": eqptCompliance,
       "eqptGroups": eqptGroups,
       "eqptGroup": eqptGroup}
)
