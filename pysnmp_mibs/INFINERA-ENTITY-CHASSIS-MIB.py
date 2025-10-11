# SNMP MIB module (INFINERA-ENTITY-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:08 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatArbitraryPrecision,
 FloatHundredths,
 FloatTenths,
 FloatThousandths,
 InfnChassisSwitchingMode,
 InfnChassisType,
 InfnEnableDisable,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths",
    "FloatTenths",
    "FloatThousandths",
    "InfnChassisSwitchingMode",
    "InfnChassisType",
    "InfnEnableDisable",
    "InfnPmHistStatsControl")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

chassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")
_ChassisMoId_Type = DisplayString
_ChassisMoId_Object = MibTableColumn
chassisMoId = _ChassisMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 1),
    _ChassisMoId_Type()
)
chassisMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisMoId.setStatus("current")
_ChassisProvChassisType_Type = InfnChassisType
_ChassisProvChassisType_Object = MibTableColumn
chassisProvChassisType = _ChassisProvChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 2),
    _ChassisProvChassisType_Type()
)
chassisProvChassisType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisProvChassisType.setStatus("current")
_ChassisInstalledChassisType_Type = InfnChassisType
_ChassisInstalledChassisType_Object = MibTableColumn
chassisInstalledChassisType = _ChassisInstalledChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 3),
    _ChassisInstalledChassisType_Type()
)
chassisInstalledChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisInstalledChassisType.setStatus("current")
_ChassisProvSerialNumber_Type = DisplayString
_ChassisProvSerialNumber_Object = MibTableColumn
chassisProvSerialNumber = _ChassisProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 4),
    _ChassisProvSerialNumber_Type()
)
chassisProvSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisProvSerialNumber.setStatus("current")
_ChassisInstalledSerialNumber_Type = DisplayString
_ChassisInstalledSerialNumber_Object = MibTableColumn
chassisInstalledSerialNumber = _ChassisInstalledSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 5),
    _ChassisInstalledSerialNumber_Type()
)
chassisInstalledSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisInstalledSerialNumber.setStatus("current")
_ChassisRackName_Type = DisplayString
_ChassisRackName_Object = MibTableColumn
chassisRackName = _ChassisRackName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 6),
    _ChassisRackName_Type()
)
chassisRackName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisRackName.setStatus("current")
_ChassisRUlocationInRack_Type = Unsigned32
_ChassisRUlocationInRack_Object = MibTableColumn
chassisRUlocationInRack = _ChassisRUlocationInRack_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 7),
    _ChassisRUlocationInRack_Type()
)
chassisRUlocationInRack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisRUlocationInRack.setStatus("current")


class _ChassisSwitchCapabilityMode_Type(Integer32):
    """Custom type chassisSwitchCapabilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ring", 1),
          ("mesh", 2))
    )


_ChassisSwitchCapabilityMode_Type.__name__ = "Integer32"
_ChassisSwitchCapabilityMode_Object = MibTableColumn
chassisSwitchCapabilityMode = _ChassisSwitchCapabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 8),
    _ChassisSwitchCapabilityMode_Type()
)
chassisSwitchCapabilityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisSwitchCapabilityMode.setStatus("current")
_ChassisInletTemperature_Type = FloatArbitraryPrecision
_ChassisInletTemperature_Object = MibTableColumn
chassisInletTemperature = _ChassisInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 9),
    _ChassisInletTemperature_Type()
)
chassisInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisInletTemperature.setStatus("current")


class _ChassisAcoState_Type(Integer32):
    """Custom type chassisAcoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChassisAcoState_Type.__name__ = "Integer32"
_ChassisAcoState_Object = MibTableColumn
chassisAcoState = _ChassisAcoState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 10),
    _ChassisAcoState_Type()
)
chassisAcoState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisAcoState.setStatus("current")


class _ChassisBayLevelSummaryAlarmReporting_Type(Integer32):
    """Custom type chassisBayLevelSummaryAlarmReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChassisBayLevelSummaryAlarmReporting_Type.__name__ = "Integer32"
_ChassisBayLevelSummaryAlarmReporting_Object = MibTableColumn
chassisBayLevelSummaryAlarmReporting = _ChassisBayLevelSummaryAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 11),
    _ChassisBayLevelSummaryAlarmReporting_Type()
)
chassisBayLevelSummaryAlarmReporting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisBayLevelSummaryAlarmReporting.setStatus("current")
_ChassisConfiguredMaxPowerDraw_Type = FloatThousandths
_ChassisConfiguredMaxPowerDraw_Object = MibTableColumn
chassisConfiguredMaxPowerDraw = _ChassisConfiguredMaxPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 12),
    _ChassisConfiguredMaxPowerDraw_Type()
)
chassisConfiguredMaxPowerDraw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisConfiguredMaxPowerDraw.setStatus("current")
_ChassisCurrentEstimatedPowerDraw_Type = FloatThousandths
_ChassisCurrentEstimatedPowerDraw_Object = MibTableColumn
chassisCurrentEstimatedPowerDraw = _ChassisCurrentEstimatedPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 13),
    _ChassisCurrentEstimatedPowerDraw_Type()
)
chassisCurrentEstimatedPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCurrentEstimatedPowerDraw.setStatus("current")
_ChassisEqptMaxPowerDraw_Type = FloatHundredths
_ChassisEqptMaxPowerDraw_Object = MibTableColumn
chassisEqptMaxPowerDraw = _ChassisEqptMaxPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 14),
    _ChassisEqptMaxPowerDraw_Type()
)
chassisEqptMaxPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisEqptMaxPowerDraw.setStatus("current")
_ChassisScmMigrationAllowed_Type = TruthValue
_ChassisScmMigrationAllowed_Object = MibTableColumn
chassisScmMigrationAllowed = _ChassisScmMigrationAllowed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 15),
    _ChassisScmMigrationAllowed_Type()
)
chassisScmMigrationAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisScmMigrationAllowed.setStatus("current")
_ChassisScmMigrationInProgress_Type = TruthValue
_ChassisScmMigrationInProgress_Object = MibTableColumn
chassisScmMigrationInProgress = _ChassisScmMigrationInProgress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 16),
    _ChassisScmMigrationInProgress_Type()
)
chassisScmMigrationInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisScmMigrationInProgress.setStatus("current")


class _ChassisPowerControl_Type(Integer32):
    """Custom type chassisPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChassisPowerControl_Type.__name__ = "Integer32"
_ChassisPowerControl_Object = MibTableColumn
chassisPowerControl = _ChassisPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 17),
    _ChassisPowerControl_Type()
)
chassisPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerControl.setStatus("current")
_ChassiscurrentInstalledPowerDraw_Type = FloatThousandths
_ChassiscurrentInstalledPowerDraw_Object = MibTableColumn
chassiscurrentInstalledPowerDraw = _ChassiscurrentInstalledPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 18),
    _ChassiscurrentInstalledPowerDraw_Type()
)
chassiscurrentInstalledPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassiscurrentInstalledPowerDraw.setStatus("current")
_ChassisConfiguredPemRating_Type = Unsigned32
_ChassisConfiguredPemRating_Object = MibTableColumn
chassisConfiguredPemRating = _ChassisConfiguredPemRating_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 19),
    _ChassisConfiguredPemRating_Type()
)
chassisConfiguredPemRating.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisConfiguredPemRating.setStatus("current")
_ChassisRowStatus_Type = RowStatus
_ChassisRowStatus_Object = MibTableColumn
chassisRowStatus = _ChassisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 20),
    _ChassisRowStatus_Type()
)
chassisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisRowStatus.setStatus("current")
_ChassisIsNCChassis_Type = TruthValue
_ChassisIsNCChassis_Object = MibTableColumn
chassisIsNCChassis = _ChassisIsNCChassis_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 21),
    _ChassisIsNCChassis_Type()
)
chassisIsNCChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIsNCChassis.setStatus("current")
_ChassisSwitchingMode_Type = InfnChassisSwitchingMode
_ChassisSwitchingMode_Object = MibTableColumn
chassisSwitchingMode = _ChassisSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 22),
    _ChassisSwitchingMode_Type()
)
chassisSwitchingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSwitchingMode.setStatus("current")
_ChassisMaxAvailablePower_Type = FloatThousandths
_ChassisMaxAvailablePower_Object = MibTableColumn
chassisMaxAvailablePower = _ChassisMaxAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 23),
    _ChassisMaxAvailablePower_Type()
)
chassisMaxAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMaxAvailablePower.setStatus("current")
_ChassisActvTimingSource_Type = DisplayString
_ChassisActvTimingSource_Object = MibTableColumn
chassisActvTimingSource = _ChassisActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 24),
    _ChassisActvTimingSource_Type()
)
chassisActvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisActvTimingSource.setStatus("current")
_ChassisOperatingTemperatureThreshold_Type = Integer32
_ChassisOperatingTemperatureThreshold_Object = MibTableColumn
chassisOperatingTemperatureThreshold = _ChassisOperatingTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 25),
    _ChassisOperatingTemperatureThreshold_Type()
)
chassisOperatingTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisOperatingTemperatureThreshold.setStatus("current")
_ChassisConfiguredAmbientTemp_Type = Unsigned32
_ChassisConfiguredAmbientTemp_Object = MibTableColumn
chassisConfiguredAmbientTemp = _ChassisConfiguredAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 26),
    _ChassisConfiguredAmbientTemp_Type()
)
chassisConfiguredAmbientTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisConfiguredAmbientTemp.setStatus("current")


class _ChassisSkewBudget_Type(Integer32):
    """Custom type chassisSkewBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("low", 2),
          ("high", 3))
    )


_ChassisSkewBudget_Type.__name__ = "Integer32"
_ChassisSkewBudget_Object = MibTableColumn
chassisSkewBudget = _ChassisSkewBudget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 27),
    _ChassisSkewBudget_Type()
)
chassisSkewBudget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chassisSkewBudget.setStatus("current")
_ChassisPduCktBreakerRating_Type = FloatArbitraryPrecision
_ChassisPduCktBreakerRating_Object = MibTableColumn
chassisPduCktBreakerRating = _ChassisPduCktBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 28),
    _ChassisPduCktBreakerRating_Type()
)
chassisPduCktBreakerRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisPduCktBreakerRating.setStatus("current")
_ChassisRebootTime_Type = Integer32
_ChassisRebootTime_Object = MibTableColumn
chassisRebootTime = _ChassisRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 29),
    _ChassisRebootTime_Type()
)
chassisRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisRebootTime.setStatus("current")
_ChassisCLEI_Type = DisplayString
_ChassisCLEI_Object = MibTableColumn
chassisCLEI = _ChassisCLEI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 30),
    _ChassisCLEI_Type()
)
chassisCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCLEI.setStatus("current")
_ChassisHardwareVersion_Type = DisplayString
_ChassisHardwareVersion_Object = MibTableColumn
chassisHardwareVersion = _ChassisHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 31),
    _ChassisHardwareVersion_Type()
)
chassisHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHardwareVersion.setStatus("current")
_ChassisManufacturedDate_Type = DisplayString
_ChassisManufacturedDate_Object = MibTableColumn
chassisManufacturedDate = _ChassisManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 32),
    _ChassisManufacturedDate_Type()
)
chassisManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisManufacturedDate.setStatus("current")
_ChassisPartNumber_Type = DisplayString
_ChassisPartNumber_Object = MibTableColumn
chassisPartNumber = _ChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 33),
    _ChassisPartNumber_Type()
)
chassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPartNumber.setStatus("current")
_ChassisPON_Type = DisplayString
_ChassisPON_Object = MibTableColumn
chassisPON = _ChassisPON_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 34),
    _ChassisPON_Type()
)
chassisPON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPON.setStatus("current")


class _ChassisHolderType_Type(Integer32):
    """Custom type chassisHolderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("self", 2),
          ("slot", 3),
          ("subSlot", 4),
          ("unknown", 5))
    )


_ChassisHolderType_Type.__name__ = "Integer32"
_ChassisHolderType_Object = MibTableColumn
chassisHolderType = _ChassisHolderType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 35),
    _ChassisHolderType_Type()
)
chassisHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHolderType.setStatus("current")


class _ChassisHolderState_Type(Integer32):
    """Custom type chassisHolderState based on Integer32"""
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
        *(("empty", 1),
          ("plugIn", 2),
          ("installed", 3),
          ("installedAndExpected", 4),
          ("mismatchOfInstalledAndExpected", 5),
          ("unknown", 6))
    )


_ChassisHolderState_Type.__name__ = "Integer32"
_ChassisHolderState_Object = MibTableColumn
chassisHolderState = _ChassisHolderState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 36),
    _ChassisHolderState_Type()
)
chassisHolderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHolderState.setStatus("current")
_ChassisAcceptableEquipmentTypeList_Type = DisplayString
_ChassisAcceptableEquipmentTypeList_Object = MibTableColumn
chassisAcceptableEquipmentTypeList = _ChassisAcceptableEquipmentTypeList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 37),
    _ChassisAcceptableEquipmentTypeList_Type()
)
chassisAcceptableEquipmentTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisAcceptableEquipmentTypeList.setStatus("current")
_ChassisUnreachableFromManagement_Type = TruthValue
_ChassisUnreachableFromManagement_Object = MibTableColumn
chassisUnreachableFromManagement = _ChassisUnreachableFromManagement_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 38),
    _ChassisUnreachableFromManagement_Type()
)
chassisUnreachableFromManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisUnreachableFromManagement.setStatus("current")
_ChassisSerialPortCLIAccess_Type = InfnEnableDisable
_ChassisSerialPortCLIAccess_Object = MibTableColumn
chassisSerialPortCLIAccess = _ChassisSerialPortCLIAccess_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 39),
    _ChassisSerialPortCLIAccess_Type()
)
chassisSerialPortCLIAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSerialPortCLIAccess.setStatus("current")
_ChassisAcliSessionAdminState_Type = InfnEnableDisable
_ChassisAcliSessionAdminState_Object = MibTableColumn
chassisAcliSessionAdminState = _ChassisAcliSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 40),
    _ChassisAcliSessionAdminState_Type()
)
chassisAcliSessionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAcliSessionAdminState.setStatus("current")
_ChassisFruInsertionDate_Type = DisplayString
_ChassisFruInsertionDate_Object = MibTableColumn
chassisFruInsertionDate = _ChassisFruInsertionDate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 41),
    _ChassisFruInsertionDate_Type()
)
chassisFruInsertionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFruInsertionDate.setStatus("current")


class _ChassisPowerSupplyType_Type(Integer32):
    """Custom type chassisPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("native", 1),
          ("unmanaged3rdparty", 2))
    )


_ChassisPowerSupplyType_Type.__name__ = "Integer32"
_ChassisPowerSupplyType_Object = MibTableColumn
chassisPowerSupplyType = _ChassisPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 42),
    _ChassisPowerSupplyType_Type()
)
chassisPowerSupplyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisPowerSupplyType.setStatus("current")


class _ChassisBaffleType_Type(Integer32):
    """Custom type chassisBaffleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mtc9AirBaffle", 2),
          ("mtc9AirBaffle2", 3))
    )


_ChassisBaffleType_Type.__name__ = "Integer32"
_ChassisBaffleType_Object = MibTableColumn
chassisBaffleType = _ChassisBaffleType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 43),
    _ChassisBaffleType_Type()
)
chassisBaffleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisBaffleType.setStatus("current")
_ChassisPmHistStatsEnable_Type = InfnPmHistStatsControl
_ChassisPmHistStatsEnable_Object = MibTableColumn
chassisPmHistStatsEnable = _ChassisPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 44),
    _ChassisPmHistStatsEnable_Type()
)
chassisPmHistStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmHistStatsEnable.setStatus("current")
_ChassisInletTemperatureOffset_Type = FloatTenths
_ChassisInletTemperatureOffset_Object = MibTableColumn
chassisInletTemperatureOffset = _ChassisInletTemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 45),
    _ChassisInletTemperatureOffset_Type()
)
chassisInletTemperatureOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisInletTemperatureOffset.setStatus("current")
_ChassisHasPluggableEeprom_Type = TruthValue
_ChassisHasPluggableEeprom_Object = MibTableColumn
chassisHasPluggableEeprom = _ChassisHasPluggableEeprom_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 46),
    _ChassisHasPluggableEeprom_Type()
)
chassisHasPluggableEeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHasPluggableEeprom.setStatus("current")
_ChassisPluggablePromSerialNumber_Type = DisplayString
_ChassisPluggablePromSerialNumber_Object = MibTableColumn
chassisPluggablePromSerialNumber = _ChassisPluggablePromSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 47),
    _ChassisPluggablePromSerialNumber_Type()
)
chassisPluggablePromSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPluggablePromSerialNumber.setStatus("current")
_ChassisOutletTemperature_Type = FloatArbitraryPrecision
_ChassisOutletTemperature_Object = MibTableColumn
chassisOutletTemperature = _ChassisOutletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 48),
    _ChassisOutletTemperature_Type()
)
chassisOutletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisOutletTemperature.setStatus("current")
_ChassisTTLMax_Type = Integer32
_ChassisTTLMax_Object = MibTableColumn
chassisTTLMax = _ChassisTTLMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 49),
    _ChassisTTLMax_Type()
)
chassisTTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTTLMax.setStatus("current")
_ChassisTTLCurrentDays_Type = Integer32
_ChassisTTLCurrentDays_Object = MibTableColumn
chassisTTLCurrentDays = _ChassisTTLCurrentDays_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 1, 1, 50),
    _ChassisTTLCurrentDays_Type()
)
chassisTTLCurrentDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTTLCurrentDays.setStatus("current")
_ChassisConformance_ObjectIdentity = ObjectIdentity
chassisConformance = _ChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 3)
)
_ChassisCompliances_ObjectIdentity = ObjectIdentity
chassisCompliances = _ChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 3, 1)
)
_ChassisGroups_ObjectIdentity = ObjectIdentity
chassisGroups = _ChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 3, 2)
)

# Managed Objects groups

chassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 3, 2, 1)
)
chassisGroup.setObjects(
      *(("INFINERA-ENTITY-CHASSIS-MIB", "chassisMoId"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisProvChassisType"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisInstalledChassisType"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisProvSerialNumber"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisInstalledSerialNumber"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisRackName"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisRUlocationInRack"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisSwitchCapabilityMode"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisInletTemperature"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisAcoState"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisBayLevelSummaryAlarmReporting"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisConfiguredMaxPowerDraw"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisCurrentEstimatedPowerDraw"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisEqptMaxPowerDraw"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisScmMigrationAllowed"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisScmMigrationInProgress"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPowerControl"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassiscurrentInstalledPowerDraw"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisConfiguredPemRating"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisRowStatus"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisIsNCChassis"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisSwitchingMode"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisMaxAvailablePower"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisActvTimingSource"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisOperatingTemperatureThreshold"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisConfiguredAmbientTemp"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisSkewBudget"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPduCktBreakerRating"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisRebootTime"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisCLEI"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisHardwareVersion"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisManufacturedDate"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPartNumber"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPON"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisHolderType"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisHolderState"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisAcceptableEquipmentTypeList"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisUnreachableFromManagement"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisSerialPortCLIAccess"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisAcliSessionAdminState"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisFruInsertionDate"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPowerSupplyType"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisBaffleType"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPmHistStatsEnable"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisInletTemperatureOffset"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisHasPluggableEeprom"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisPluggablePromSerialNumber"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisOutletTemperature"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisTTLMax"),
        ("INFINERA-ENTITY-CHASSIS-MIB", "chassisTTLCurrentDays"))
)
if mibBuilder.loadTexts:
    chassisGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

chassisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 13, 3, 1, 1)
)
chassisCompliance.setObjects(
    ("INFINERA-ENTITY-CHASSIS-MIB", "chassisGroup")
)
if mibBuilder.loadTexts:
    chassisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-CHASSIS-MIB",
    **{"chassisMIB": chassisMIB,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisMoId": chassisMoId,
       "chassisProvChassisType": chassisProvChassisType,
       "chassisInstalledChassisType": chassisInstalledChassisType,
       "chassisProvSerialNumber": chassisProvSerialNumber,
       "chassisInstalledSerialNumber": chassisInstalledSerialNumber,
       "chassisRackName": chassisRackName,
       "chassisRUlocationInRack": chassisRUlocationInRack,
       "chassisSwitchCapabilityMode": chassisSwitchCapabilityMode,
       "chassisInletTemperature": chassisInletTemperature,
       "chassisAcoState": chassisAcoState,
       "chassisBayLevelSummaryAlarmReporting": chassisBayLevelSummaryAlarmReporting,
       "chassisConfiguredMaxPowerDraw": chassisConfiguredMaxPowerDraw,
       "chassisCurrentEstimatedPowerDraw": chassisCurrentEstimatedPowerDraw,
       "chassisEqptMaxPowerDraw": chassisEqptMaxPowerDraw,
       "chassisScmMigrationAllowed": chassisScmMigrationAllowed,
       "chassisScmMigrationInProgress": chassisScmMigrationInProgress,
       "chassisPowerControl": chassisPowerControl,
       "chassiscurrentInstalledPowerDraw": chassiscurrentInstalledPowerDraw,
       "chassisConfiguredPemRating": chassisConfiguredPemRating,
       "chassisRowStatus": chassisRowStatus,
       "chassisIsNCChassis": chassisIsNCChassis,
       "chassisSwitchingMode": chassisSwitchingMode,
       "chassisMaxAvailablePower": chassisMaxAvailablePower,
       "chassisActvTimingSource": chassisActvTimingSource,
       "chassisOperatingTemperatureThreshold": chassisOperatingTemperatureThreshold,
       "chassisConfiguredAmbientTemp": chassisConfiguredAmbientTemp,
       "chassisSkewBudget": chassisSkewBudget,
       "chassisPduCktBreakerRating": chassisPduCktBreakerRating,
       "chassisRebootTime": chassisRebootTime,
       "chassisCLEI": chassisCLEI,
       "chassisHardwareVersion": chassisHardwareVersion,
       "chassisManufacturedDate": chassisManufacturedDate,
       "chassisPartNumber": chassisPartNumber,
       "chassisPON": chassisPON,
       "chassisHolderType": chassisHolderType,
       "chassisHolderState": chassisHolderState,
       "chassisAcceptableEquipmentTypeList": chassisAcceptableEquipmentTypeList,
       "chassisUnreachableFromManagement": chassisUnreachableFromManagement,
       "chassisSerialPortCLIAccess": chassisSerialPortCLIAccess,
       "chassisAcliSessionAdminState": chassisAcliSessionAdminState,
       "chassisFruInsertionDate": chassisFruInsertionDate,
       "chassisPowerSupplyType": chassisPowerSupplyType,
       "chassisBaffleType": chassisBaffleType,
       "chassisPmHistStatsEnable": chassisPmHistStatsEnable,
       "chassisInletTemperatureOffset": chassisInletTemperatureOffset,
       "chassisHasPluggableEeprom": chassisHasPluggableEeprom,
       "chassisPluggablePromSerialNumber": chassisPluggablePromSerialNumber,
       "chassisOutletTemperature": chassisOutletTemperature,
       "chassisTTLMax": chassisTTLMax,
       "chassisTTLCurrentDays": chassisTTLCurrentDays,
       "chassisConformance": chassisConformance,
       "chassisCompliances": chassisCompliances,
       "chassisCompliance": chassisCompliance,
       "chassisGroups": chassisGroups,
       "chassisGroup": chassisGroup}
)
