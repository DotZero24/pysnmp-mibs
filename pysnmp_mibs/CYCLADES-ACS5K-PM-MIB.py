# SNMP MIB module (CYCLADES-ACS5K-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vertiv/CYCLADES-ACS5K-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:46 2025
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

(cyACS5KMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS5K-MIB",
    "cyACS5KMgmt")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cyACS5KPM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5)
)
if mibBuilder.loadTexts:
    cyACS5KPM.setRevisions(
        ("2010-07-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyNumberOfPM_Type = Integer32
_CyNumberOfPM_Object = MibScalar
cyNumberOfPM = _CyNumberOfPM_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 1),
    _CyNumberOfPM_Type()
)
cyNumberOfPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyNumberOfPM.setStatus("current")
_CyPMTable_Object = MibTable
cyPMTable = _CyPMTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2)
)
if mibBuilder.loadTexts:
    cyPMTable.setStatus("current")
_CyPMEntry_Object = MibTableRow
cyPMEntry = _CyPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1)
)
cyPMEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMSerialPortNumber"),
)
if mibBuilder.loadTexts:
    cyPMEntry.setStatus("current")
_CyPMSerialPortNumber_Type = InterfaceIndex
_CyPMSerialPortNumber_Object = MibTableColumn
cyPMSerialPortNumber = _CyPMSerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 1),
    _CyPMSerialPortNumber_Type()
)
cyPMSerialPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMSerialPortNumber.setStatus("current")
_CyPMNumberOutlets_Type = Integer32
_CyPMNumberOutlets_Object = MibTableColumn
cyPMNumberOutlets = _CyPMNumberOutlets_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 2),
    _CyPMNumberOutlets_Type()
)
cyPMNumberOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMNumberOutlets.setStatus("current")
_CyPMNumberUnits_Type = Integer32
_CyPMNumberUnits_Object = MibTableColumn
cyPMNumberUnits = _CyPMNumberUnits_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 3),
    _CyPMNumberUnits_Type()
)
cyPMNumberUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMNumberUnits.setStatus("current")
_CyPMCurrent_Type = DisplayString
_CyPMCurrent_Object = MibTableColumn
cyPMCurrent = _CyPMCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 4),
    _CyPMCurrent_Type()
)
cyPMCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMCurrent.setStatus("current")
_CyPMVersion_Type = DisplayString
_CyPMVersion_Object = MibTableColumn
cyPMVersion = _CyPMVersion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 5),
    _CyPMVersion_Type()
)
cyPMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMVersion.setStatus("current")


class _CyPMCommand_Type(DisplayString):
    """Custom type cyPMCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CyPMCommand_Type.__name__ = "DisplayString"
_CyPMCommand_Object = MibTableColumn
cyPMCommand = _CyPMCommand_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 2, 1, 7),
    _CyPMCommand_Type()
)
cyPMCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMCommand.setStatus("current")
_CyPMUnitTable_Object = MibTable
cyPMUnitTable = _CyPMUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3)
)
if mibBuilder.loadTexts:
    cyPMUnitTable.setStatus("current")
_CyPMUnitEntry_Object = MibTableRow
cyPMUnitEntry = _CyPMUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1)
)
cyPMUnitEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMSerialPortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMUnitNumber"),
)
if mibBuilder.loadTexts:
    cyPMUnitEntry.setStatus("current")
_CyPMUnitNumber_Type = InterfaceIndex
_CyPMUnitNumber_Object = MibTableColumn
cyPMUnitNumber = _CyPMUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 1),
    _CyPMUnitNumber_Type()
)
cyPMUnitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyPMUnitNumber.setStatus("current")
_CyPMUnitVersion_Type = DisplayString
_CyPMUnitVersion_Object = MibTableColumn
cyPMUnitVersion = _CyPMUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 2),
    _CyPMUnitVersion_Type()
)
cyPMUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitVersion.setStatus("current")
_CyPMUnitOutlets_Type = Integer32
_CyPMUnitOutlets_Object = MibTableColumn
cyPMUnitOutlets = _CyPMUnitOutlets_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 3),
    _CyPMUnitOutlets_Type()
)
cyPMUnitOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitOutlets.setStatus("current")
_CyPMUnitFirstOutlet_Type = Integer32
_CyPMUnitFirstOutlet_Object = MibTableColumn
cyPMUnitFirstOutlet = _CyPMUnitFirstOutlet_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 4),
    _CyPMUnitFirstOutlet_Type()
)
cyPMUnitFirstOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitFirstOutlet.setStatus("current")
_CyPMUnitCurrent_Type = Integer32
_CyPMUnitCurrent_Object = MibTableColumn
cyPMUnitCurrent = _CyPMUnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 5),
    _CyPMUnitCurrent_Type()
)
cyPMUnitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitCurrent.setStatus("current")
_CyPMUnitMaxCurrent_Type = Integer32
_CyPMUnitMaxCurrent_Object = MibTableColumn
cyPMUnitMaxCurrent = _CyPMUnitMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 6),
    _CyPMUnitMaxCurrent_Type()
)
cyPMUnitMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitMaxCurrent.setStatus("current")
_CyPMUnitSequenceInterval_Type = Integer32
_CyPMUnitSequenceInterval_Object = MibTableColumn
cyPMUnitSequenceInterval = _CyPMUnitSequenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 9),
    _CyPMUnitSequenceInterval_Type()
)
cyPMUnitSequenceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitSequenceInterval.setStatus("current")
_CyPMUnitCycleInterval_Type = Integer32
_CyPMUnitCycleInterval_Object = MibTableColumn
cyPMUnitCycleInterval = _CyPMUnitCycleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 10),
    _CyPMUnitCycleInterval_Type()
)
cyPMUnitCycleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitCycleInterval.setStatus("current")
_CyPMUnitID_Type = DisplayString
_CyPMUnitID_Object = MibTableColumn
cyPMUnitID = _CyPMUnitID_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 11),
    _CyPMUnitID_Type()
)
cyPMUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitID.setStatus("current")


class _CyPMUnitPhases_Type(Integer32):
    """Custom type cyPMUnitPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single-phase", 0),
          ("three-phase", 3))
    )


_CyPMUnitPhases_Type.__name__ = "Integer32"
_CyPMUnitPhases_Object = MibTableColumn
cyPMUnitPhases = _CyPMUnitPhases_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 12),
    _CyPMUnitPhases_Type()
)
cyPMUnitPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitPhases.setStatus("current")
_CyPMUnitBanks_Type = Integer32
_CyPMUnitBanks_Object = MibTableColumn
cyPMUnitBanks = _CyPMUnitBanks_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 13),
    _CyPMUnitBanks_Type()
)
cyPMUnitBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitBanks.setStatus("current")
_CyPMUnitNominalVoltage_Type = Integer32
_CyPMUnitNominalVoltage_Object = MibTableColumn
cyPMUnitNominalVoltage = _CyPMUnitNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 14),
    _CyPMUnitNominalVoltage_Type()
)
cyPMUnitNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitNominalVoltage.setStatus("current")
_CyPMUnitPower_Type = Integer32
_CyPMUnitPower_Object = MibTableColumn
cyPMUnitPower = _CyPMUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 3, 1, 15),
    _CyPMUnitPower_Type()
)
cyPMUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMUnitPower.setStatus("current")
_CyOutletTable_Object = MibTable
cyOutletTable = _CyOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4)
)
if mibBuilder.loadTexts:
    cyOutletTable.setStatus("current")
_CyOutletEntry_Object = MibTableRow
cyOutletEntry = _CyOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1)
)
cyOutletEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMSerialPortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyOutletNumber"),
)
if mibBuilder.loadTexts:
    cyOutletEntry.setStatus("current")
_CyOutletNumber_Type = InterfaceIndexOrZero
_CyOutletNumber_Object = MibTableColumn
cyOutletNumber = _CyOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 1),
    _CyOutletNumber_Type()
)
cyOutletNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyOutletNumber.setStatus("current")


class _CyOutletName_Type(DisplayString):
    """Custom type cyOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CyOutletName_Type.__name__ = "DisplayString"
_CyOutletName_Object = MibTableColumn
cyOutletName = _CyOutletName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 2),
    _CyOutletName_Type()
)
cyOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletName.setStatus("current")
_CyOutletServer_Type = DisplayString
_CyOutletServer_Object = MibTableColumn
cyOutletServer = _CyOutletServer_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 3),
    _CyOutletServer_Type()
)
cyOutletServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletServer.setStatus("current")


class _CyOutletPower_Type(Integer32):
    """Custom type cyOutletPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("cycle", 2),
          ("unknow", 3))
    )


_CyOutletPower_Type.__name__ = "Integer32"
_CyOutletPower_Object = MibTableColumn
cyOutletPower = _CyOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 4),
    _CyOutletPower_Type()
)
cyOutletPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletPower.setStatus("current")


class _CyOutletLock_Type(Integer32):
    """Custom type cyOutletLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("unknow", 2))
    )


_CyOutletLock_Type.__name__ = "Integer32"
_CyOutletLock_Object = MibTableColumn
cyOutletLock = _CyOutletLock_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 5),
    _CyOutletLock_Type()
)
cyOutletLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletLock.setStatus("current")
_CyOutletPUInterval_Type = Integer32
_CyOutletPUInterval_Object = MibTableColumn
cyOutletPUInterval = _CyOutletPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 6),
    _CyOutletPUInterval_Type()
)
cyOutletPUInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyOutletPUInterval.setStatus("current")
_CyOutletMinimumOnInterval_Type = Integer32
_CyOutletMinimumOnInterval_Object = MibTableColumn
cyOutletMinimumOnInterval = _CyOutletMinimumOnInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 7),
    _CyOutletMinimumOnInterval_Type()
)
cyOutletMinimumOnInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletMinimumOnInterval.setStatus("current")
_CyOutletMinimumOffInterval_Type = Integer32
_CyOutletMinimumOffInterval_Object = MibTableColumn
cyOutletMinimumOffInterval = _CyOutletMinimumOffInterval_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 8),
    _CyOutletMinimumOffInterval_Type()
)
cyOutletMinimumOffInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletMinimumOffInterval.setStatus("current")
_CyOutletWakeupState_Type = Integer32
_CyOutletWakeupState_Object = MibTableColumn
cyOutletWakeupState = _CyOutletWakeupState_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 9),
    _CyOutletWakeupState_Type()
)
cyOutletWakeupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletWakeupState.setStatus("current")
_CyOutletPduID_Type = DisplayString
_CyOutletPduID_Object = MibTableColumn
cyOutletPduID = _CyOutletPduID_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 10),
    _CyOutletPduID_Type()
)
cyOutletPduID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyOutletPduID.setStatus("current")
_CyOutletPduNumber_Type = Integer32
_CyOutletPduNumber_Object = MibTableColumn
cyOutletPduNumber = _CyOutletPduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 4, 1, 11),
    _CyOutletPduNumber_Type()
)
cyOutletPduNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyOutletPduNumber.setStatus("current")
_CyPMElecPduTable_Object = MibTable
cyPMElecPduTable = _CyPMElecPduTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5)
)
if mibBuilder.loadTexts:
    cyPMElecPduTable.setStatus("current")
_CyPMElecPduTableEntry_Object = MibTableRow
cyPMElecPduTableEntry = _CyPMElecPduTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1)
)
cyPMElecPduTableEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecPduTablePortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecPduTablePduNumber"),
)
if mibBuilder.loadTexts:
    cyPMElecPduTableEntry.setStatus("current")
_CyPMElecPduTablePortNumber_Type = InterfaceIndex
_CyPMElecPduTablePortNumber_Object = MibTableColumn
cyPMElecPduTablePortNumber = _CyPMElecPduTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 1),
    _CyPMElecPduTablePortNumber_Type()
)
cyPMElecPduTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePortNumber.setStatus("current")
_CyPMElecPduTablePduNumber_Type = InterfaceIndex
_CyPMElecPduTablePduNumber_Object = MibTableColumn
cyPMElecPduTablePduNumber = _CyPMElecPduTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 2),
    _CyPMElecPduTablePduNumber_Type()
)
cyPMElecPduTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePduNumber.setStatus("current")
_CyPMElecPduTableCurrentValue_Type = Integer32
_CyPMElecPduTableCurrentValue_Object = MibTableColumn
cyPMElecPduTableCurrentValue = _CyPMElecPduTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 3),
    _CyPMElecPduTableCurrentValue_Type()
)
cyPMElecPduTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTableCurrentValue.setStatus("current")
_CyPMElecPduTableCurrentMax_Type = Integer32
_CyPMElecPduTableCurrentMax_Object = MibTableColumn
cyPMElecPduTableCurrentMax = _CyPMElecPduTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 4),
    _CyPMElecPduTableCurrentMax_Type()
)
cyPMElecPduTableCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPduTableCurrentMax.setStatus("current")
_CyPMElecPduTablePowerValue_Type = Integer32
_CyPMElecPduTablePowerValue_Object = MibTableColumn
cyPMElecPduTablePowerValue = _CyPMElecPduTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 5),
    _CyPMElecPduTablePowerValue_Type()
)
cyPMElecPduTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerValue.setStatus("current")
_CyPMElecPduTablePowerMax_Type = Integer32
_CyPMElecPduTablePowerMax_Object = MibTableColumn
cyPMElecPduTablePowerMax = _CyPMElecPduTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 6),
    _CyPMElecPduTablePowerMax_Type()
)
cyPMElecPduTablePowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerMax.setStatus("current")
_CyPMElecPduTableVoltageValue_Type = Integer32
_CyPMElecPduTableVoltageValue_Object = MibTableColumn
cyPMElecPduTableVoltageValue = _CyPMElecPduTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 7),
    _CyPMElecPduTableVoltageValue_Type()
)
cyPMElecPduTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTableVoltageValue.setStatus("current")
_CyPMElecPduTableVoltageMax_Type = Integer32
_CyPMElecPduTableVoltageMax_Object = MibTableColumn
cyPMElecPduTableVoltageMax = _CyPMElecPduTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 8),
    _CyPMElecPduTableVoltageMax_Type()
)
cyPMElecPduTableVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPduTableVoltageMax.setStatus("current")
_CyPMElecPduTablePowerFactorValue_Type = Integer32
_CyPMElecPduTablePowerFactorValue_Object = MibTableColumn
cyPMElecPduTablePowerFactorValue = _CyPMElecPduTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 9),
    _CyPMElecPduTablePowerFactorValue_Type()
)
cyPMElecPduTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerFactorValue.setStatus("current")
_CyPMElecPduTablePowerFactorMax_Type = Integer32
_CyPMElecPduTablePowerFactorMax_Object = MibTableColumn
cyPMElecPduTablePowerFactorMax = _CyPMElecPduTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 10),
    _CyPMElecPduTablePowerFactorMax_Type()
)
cyPMElecPduTablePowerFactorMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerFactorMax.setStatus("current")


class _CyPMElecPduTablePowerType_Type(Integer32):
    """Custom type cyPMElecPduTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPduTablePowerType_Type.__name__ = "Integer32"
_CyPMElecPduTablePowerType_Object = MibTableColumn
cyPMElecPduTablePowerType = _CyPMElecPduTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 11),
    _CyPMElecPduTablePowerType_Type()
)
cyPMElecPduTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerType.setStatus("current")


class _CyPMElecPduTableVoltageType_Type(Integer32):
    """Custom type cyPMElecPduTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPduTableVoltageType_Type.__name__ = "Integer32"
_CyPMElecPduTableVoltageType_Object = MibTableColumn
cyPMElecPduTableVoltageType = _CyPMElecPduTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 12),
    _CyPMElecPduTableVoltageType_Type()
)
cyPMElecPduTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTableVoltageType.setStatus("current")


class _CyPMElecPduTablePowerFactorType_Type(Integer32):
    """Custom type cyPMElecPduTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPduTablePowerFactorType_Type.__name__ = "Integer32"
_CyPMElecPduTablePowerFactorType_Object = MibTableColumn
cyPMElecPduTablePowerFactorType = _CyPMElecPduTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 5, 1, 13),
    _CyPMElecPduTablePowerFactorType_Type()
)
cyPMElecPduTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPduTablePowerFactorType.setStatus("current")
_CyPMElecPhaseTable_Object = MibTable
cyPMElecPhaseTable = _CyPMElecPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6)
)
if mibBuilder.loadTexts:
    cyPMElecPhaseTable.setStatus("current")
_CyPMElecPhaseTableEntry_Object = MibTableRow
cyPMElecPhaseTableEntry = _CyPMElecPhaseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1)
)
cyPMElecPhaseTableEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecPhaseTablePortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecPhaseTablePduNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecPhaseTableIndex"),
)
if mibBuilder.loadTexts:
    cyPMElecPhaseTableEntry.setStatus("current")
_CyPMElecPhaseTablePortNumber_Type = InterfaceIndex
_CyPMElecPhaseTablePortNumber_Object = MibTableColumn
cyPMElecPhaseTablePortNumber = _CyPMElecPhaseTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 1),
    _CyPMElecPhaseTablePortNumber_Type()
)
cyPMElecPhaseTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePortNumber.setStatus("current")
_CyPMElecPhaseTablePduNumber_Type = InterfaceIndex
_CyPMElecPhaseTablePduNumber_Object = MibTableColumn
cyPMElecPhaseTablePduNumber = _CyPMElecPhaseTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 2),
    _CyPMElecPhaseTablePduNumber_Type()
)
cyPMElecPhaseTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePduNumber.setStatus("current")
_CyPMElecPhaseTableIndex_Type = InterfaceIndex
_CyPMElecPhaseTableIndex_Object = MibTableColumn
cyPMElecPhaseTableIndex = _CyPMElecPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 3),
    _CyPMElecPhaseTableIndex_Type()
)
cyPMElecPhaseTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableIndex.setStatus("current")
_CyPMElecPhaseTableName_Type = DisplayString
_CyPMElecPhaseTableName_Object = MibTableColumn
cyPMElecPhaseTableName = _CyPMElecPhaseTableName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 4),
    _CyPMElecPhaseTableName_Type()
)
cyPMElecPhaseTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableName.setStatus("current")
_CyPMElecPhaseTableCurrentValue_Type = Integer32
_CyPMElecPhaseTableCurrentValue_Object = MibTableColumn
cyPMElecPhaseTableCurrentValue = _CyPMElecPhaseTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 5),
    _CyPMElecPhaseTableCurrentValue_Type()
)
cyPMElecPhaseTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableCurrentValue.setStatus("current")
_CyPMElecPhaseTableCurrentMax_Type = Integer32
_CyPMElecPhaseTableCurrentMax_Object = MibTableColumn
cyPMElecPhaseTableCurrentMax = _CyPMElecPhaseTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 6),
    _CyPMElecPhaseTableCurrentMax_Type()
)
cyPMElecPhaseTableCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableCurrentMax.setStatus("current")
_CyPMElecPhaseTablePowerValue_Type = Integer32
_CyPMElecPhaseTablePowerValue_Object = MibTableColumn
cyPMElecPhaseTablePowerValue = _CyPMElecPhaseTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 7),
    _CyPMElecPhaseTablePowerValue_Type()
)
cyPMElecPhaseTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerValue.setStatus("current")
_CyPMElecPhaseTablePowerMax_Type = Integer32
_CyPMElecPhaseTablePowerMax_Object = MibTableColumn
cyPMElecPhaseTablePowerMax = _CyPMElecPhaseTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 8),
    _CyPMElecPhaseTablePowerMax_Type()
)
cyPMElecPhaseTablePowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerMax.setStatus("current")
_CyPMElecPhaseTableVoltageValue_Type = Integer32
_CyPMElecPhaseTableVoltageValue_Object = MibTableColumn
cyPMElecPhaseTableVoltageValue = _CyPMElecPhaseTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 9),
    _CyPMElecPhaseTableVoltageValue_Type()
)
cyPMElecPhaseTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableVoltageValue.setStatus("current")
_CyPMElecPhaseTableVoltageMax_Type = Integer32
_CyPMElecPhaseTableVoltageMax_Object = MibTableColumn
cyPMElecPhaseTableVoltageMax = _CyPMElecPhaseTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 10),
    _CyPMElecPhaseTableVoltageMax_Type()
)
cyPMElecPhaseTableVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableVoltageMax.setStatus("current")
_CyPMElecPhaseTablePowerFactorValue_Type = Integer32
_CyPMElecPhaseTablePowerFactorValue_Object = MibTableColumn
cyPMElecPhaseTablePowerFactorValue = _CyPMElecPhaseTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 11),
    _CyPMElecPhaseTablePowerFactorValue_Type()
)
cyPMElecPhaseTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerFactorValue.setStatus("current")
_CyPMElecPhaseTablePowerFactorMax_Type = Integer32
_CyPMElecPhaseTablePowerFactorMax_Object = MibTableColumn
cyPMElecPhaseTablePowerFactorMax = _CyPMElecPhaseTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 12),
    _CyPMElecPhaseTablePowerFactorMax_Type()
)
cyPMElecPhaseTablePowerFactorMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerFactorMax.setStatus("current")


class _CyPMElecPhaseTablePowerType_Type(Integer32):
    """Custom type cyPMElecPhaseTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPhaseTablePowerType_Type.__name__ = "Integer32"
_CyPMElecPhaseTablePowerType_Object = MibTableColumn
cyPMElecPhaseTablePowerType = _CyPMElecPhaseTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 13),
    _CyPMElecPhaseTablePowerType_Type()
)
cyPMElecPhaseTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerType.setStatus("current")


class _CyPMElecPhaseTableVoltageType_Type(Integer32):
    """Custom type cyPMElecPhaseTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPhaseTableVoltageType_Type.__name__ = "Integer32"
_CyPMElecPhaseTableVoltageType_Object = MibTableColumn
cyPMElecPhaseTableVoltageType = _CyPMElecPhaseTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 14),
    _CyPMElecPhaseTableVoltageType_Type()
)
cyPMElecPhaseTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTableVoltageType.setStatus("current")


class _CyPMElecPhaseTablePowerFactorType_Type(Integer32):
    """Custom type cyPMElecPhaseTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecPhaseTablePowerFactorType_Type.__name__ = "Integer32"
_CyPMElecPhaseTablePowerFactorType_Object = MibTableColumn
cyPMElecPhaseTablePowerFactorType = _CyPMElecPhaseTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 6, 1, 15),
    _CyPMElecPhaseTablePowerFactorType_Type()
)
cyPMElecPhaseTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecPhaseTablePowerFactorType.setStatus("current")
_CyPMElecBankTable_Object = MibTable
cyPMElecBankTable = _CyPMElecBankTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7)
)
if mibBuilder.loadTexts:
    cyPMElecBankTable.setStatus("current")
_CyPMElecBankTableEntry_Object = MibTableRow
cyPMElecBankTableEntry = _CyPMElecBankTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1)
)
cyPMElecBankTableEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecBankTablePortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecBankTablePduNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecBankTableIndex"),
)
if mibBuilder.loadTexts:
    cyPMElecBankTableEntry.setStatus("current")
_CyPMElecBankTablePortNumber_Type = InterfaceIndex
_CyPMElecBankTablePortNumber_Object = MibTableColumn
cyPMElecBankTablePortNumber = _CyPMElecBankTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 1),
    _CyPMElecBankTablePortNumber_Type()
)
cyPMElecBankTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePortNumber.setStatus("current")
_CyPMElecBankTablePduNumber_Type = InterfaceIndex
_CyPMElecBankTablePduNumber_Object = MibTableColumn
cyPMElecBankTablePduNumber = _CyPMElecBankTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 2),
    _CyPMElecBankTablePduNumber_Type()
)
cyPMElecBankTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePduNumber.setStatus("current")
_CyPMElecBankTableIndex_Type = InterfaceIndex
_CyPMElecBankTableIndex_Object = MibTableColumn
cyPMElecBankTableIndex = _CyPMElecBankTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 3),
    _CyPMElecBankTableIndex_Type()
)
cyPMElecBankTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTableIndex.setStatus("current")
_CyPMElecBankTableName_Type = DisplayString
_CyPMElecBankTableName_Object = MibTableColumn
cyPMElecBankTableName = _CyPMElecBankTableName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 4),
    _CyPMElecBankTableName_Type()
)
cyPMElecBankTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTableName.setStatus("current")
_CyPMElecBankTableCurrentValue_Type = Integer32
_CyPMElecBankTableCurrentValue_Object = MibTableColumn
cyPMElecBankTableCurrentValue = _CyPMElecBankTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 5),
    _CyPMElecBankTableCurrentValue_Type()
)
cyPMElecBankTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTableCurrentValue.setStatus("current")
_CyPMElecBankTableCurrentMax_Type = Integer32
_CyPMElecBankTableCurrentMax_Object = MibTableColumn
cyPMElecBankTableCurrentMax = _CyPMElecBankTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 6),
    _CyPMElecBankTableCurrentMax_Type()
)
cyPMElecBankTableCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecBankTableCurrentMax.setStatus("current")
_CyPMElecBankTablePowerValue_Type = Integer32
_CyPMElecBankTablePowerValue_Object = MibTableColumn
cyPMElecBankTablePowerValue = _CyPMElecBankTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 7),
    _CyPMElecBankTablePowerValue_Type()
)
cyPMElecBankTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerValue.setStatus("current")
_CyPMElecBankTablePowerMax_Type = Integer32
_CyPMElecBankTablePowerMax_Object = MibTableColumn
cyPMElecBankTablePowerMax = _CyPMElecBankTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 8),
    _CyPMElecBankTablePowerMax_Type()
)
cyPMElecBankTablePowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerMax.setStatus("current")
_CyPMElecBankTableVoltageValue_Type = Integer32
_CyPMElecBankTableVoltageValue_Object = MibTableColumn
cyPMElecBankTableVoltageValue = _CyPMElecBankTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 9),
    _CyPMElecBankTableVoltageValue_Type()
)
cyPMElecBankTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTableVoltageValue.setStatus("current")
_CyPMElecBankTableVoltageMax_Type = Integer32
_CyPMElecBankTableVoltageMax_Object = MibTableColumn
cyPMElecBankTableVoltageMax = _CyPMElecBankTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 10),
    _CyPMElecBankTableVoltageMax_Type()
)
cyPMElecBankTableVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecBankTableVoltageMax.setStatus("current")
_CyPMElecBankTablePowerFactorValue_Type = Integer32
_CyPMElecBankTablePowerFactorValue_Object = MibTableColumn
cyPMElecBankTablePowerFactorValue = _CyPMElecBankTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 11),
    _CyPMElecBankTablePowerFactorValue_Type()
)
cyPMElecBankTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerFactorValue.setStatus("current")
_CyPMElecBankTablePowerFactorMax_Type = Integer32
_CyPMElecBankTablePowerFactorMax_Object = MibTableColumn
cyPMElecBankTablePowerFactorMax = _CyPMElecBankTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 12),
    _CyPMElecBankTablePowerFactorMax_Type()
)
cyPMElecBankTablePowerFactorMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerFactorMax.setStatus("current")


class _CyPMElecBankTablePowerType_Type(Integer32):
    """Custom type cyPMElecBankTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecBankTablePowerType_Type.__name__ = "Integer32"
_CyPMElecBankTablePowerType_Object = MibTableColumn
cyPMElecBankTablePowerType = _CyPMElecBankTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 13),
    _CyPMElecBankTablePowerType_Type()
)
cyPMElecBankTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerType.setStatus("current")


class _CyPMElecBankTableVoltageType_Type(Integer32):
    """Custom type cyPMElecBankTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecBankTableVoltageType_Type.__name__ = "Integer32"
_CyPMElecBankTableVoltageType_Object = MibTableColumn
cyPMElecBankTableVoltageType = _CyPMElecBankTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 14),
    _CyPMElecBankTableVoltageType_Type()
)
cyPMElecBankTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTableVoltageType.setStatus("current")


class _CyPMElecBankTablePowerFactorType_Type(Integer32):
    """Custom type cyPMElecBankTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecBankTablePowerFactorType_Type.__name__ = "Integer32"
_CyPMElecBankTablePowerFactorType_Object = MibTableColumn
cyPMElecBankTablePowerFactorType = _CyPMElecBankTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 7, 1, 15),
    _CyPMElecBankTablePowerFactorType_Type()
)
cyPMElecBankTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecBankTablePowerFactorType.setStatus("current")
_CyPMElecOutletTable_Object = MibTable
cyPMElecOutletTable = _CyPMElecOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8)
)
if mibBuilder.loadTexts:
    cyPMElecOutletTable.setStatus("current")
_CyPMElecOutletTableEntry_Object = MibTableRow
cyPMElecOutletTableEntry = _CyPMElecOutletTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1)
)
cyPMElecOutletTableEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecOutletTablePortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecOutletTablePduNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMElecOutletTableNumber"),
)
if mibBuilder.loadTexts:
    cyPMElecOutletTableEntry.setStatus("current")
_CyPMElecOutletTablePortNumber_Type = InterfaceIndex
_CyPMElecOutletTablePortNumber_Object = MibTableColumn
cyPMElecOutletTablePortNumber = _CyPMElecOutletTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 1),
    _CyPMElecOutletTablePortNumber_Type()
)
cyPMElecOutletTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePortNumber.setStatus("current")
_CyPMElecOutletTablePduNumber_Type = InterfaceIndex
_CyPMElecOutletTablePduNumber_Object = MibTableColumn
cyPMElecOutletTablePduNumber = _CyPMElecOutletTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 2),
    _CyPMElecOutletTablePduNumber_Type()
)
cyPMElecOutletTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePduNumber.setStatus("current")
_CyPMElecOutletTableNumber_Type = InterfaceIndex
_CyPMElecOutletTableNumber_Object = MibTableColumn
cyPMElecOutletTableNumber = _CyPMElecOutletTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 3),
    _CyPMElecOutletTableNumber_Type()
)
cyPMElecOutletTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTableNumber.setStatus("current")
_CyPMElecOutletTableName_Type = DisplayString
_CyPMElecOutletTableName_Object = MibTableColumn
cyPMElecOutletTableName = _CyPMElecOutletTableName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 4),
    _CyPMElecOutletTableName_Type()
)
cyPMElecOutletTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTableName.setStatus("current")
_CyPMElecOutletTableCurrentValue_Type = Integer32
_CyPMElecOutletTableCurrentValue_Object = MibTableColumn
cyPMElecOutletTableCurrentValue = _CyPMElecOutletTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 5),
    _CyPMElecOutletTableCurrentValue_Type()
)
cyPMElecOutletTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTableCurrentValue.setStatus("current")
_CyPMElecOutletTableCurrentMax_Type = Integer32
_CyPMElecOutletTableCurrentMax_Object = MibTableColumn
cyPMElecOutletTableCurrentMax = _CyPMElecOutletTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 6),
    _CyPMElecOutletTableCurrentMax_Type()
)
cyPMElecOutletTableCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecOutletTableCurrentMax.setStatus("current")
_CyPMElecOutletTablePowerValue_Type = Integer32
_CyPMElecOutletTablePowerValue_Object = MibTableColumn
cyPMElecOutletTablePowerValue = _CyPMElecOutletTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 7),
    _CyPMElecOutletTablePowerValue_Type()
)
cyPMElecOutletTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerValue.setStatus("current")
_CyPMElecOutletTablePowerMax_Type = Integer32
_CyPMElecOutletTablePowerMax_Object = MibTableColumn
cyPMElecOutletTablePowerMax = _CyPMElecOutletTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 8),
    _CyPMElecOutletTablePowerMax_Type()
)
cyPMElecOutletTablePowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerMax.setStatus("current")
_CyPMElecOutletTableVoltageValue_Type = Integer32
_CyPMElecOutletTableVoltageValue_Object = MibTableColumn
cyPMElecOutletTableVoltageValue = _CyPMElecOutletTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 9),
    _CyPMElecOutletTableVoltageValue_Type()
)
cyPMElecOutletTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTableVoltageValue.setStatus("current")
_CyPMElecOutletTableVoltageMax_Type = Integer32
_CyPMElecOutletTableVoltageMax_Object = MibTableColumn
cyPMElecOutletTableVoltageMax = _CyPMElecOutletTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 10),
    _CyPMElecOutletTableVoltageMax_Type()
)
cyPMElecOutletTableVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecOutletTableVoltageMax.setStatus("current")
_CyPMElecOutletTablePowerFactorValue_Type = Integer32
_CyPMElecOutletTablePowerFactorValue_Object = MibTableColumn
cyPMElecOutletTablePowerFactorValue = _CyPMElecOutletTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 11),
    _CyPMElecOutletTablePowerFactorValue_Type()
)
cyPMElecOutletTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerFactorValue.setStatus("current")
_CyPMElecOutletTablePowerFactorMax_Type = Integer32
_CyPMElecOutletTablePowerFactorMax_Object = MibTableColumn
cyPMElecOutletTablePowerFactorMax = _CyPMElecOutletTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 12),
    _CyPMElecOutletTablePowerFactorMax_Type()
)
cyPMElecOutletTablePowerFactorMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerFactorMax.setStatus("current")


class _CyPMElecOutletTablePowerType_Type(Integer32):
    """Custom type cyPMElecOutletTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecOutletTablePowerType_Type.__name__ = "Integer32"
_CyPMElecOutletTablePowerType_Object = MibTableColumn
cyPMElecOutletTablePowerType = _CyPMElecOutletTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 13),
    _CyPMElecOutletTablePowerType_Type()
)
cyPMElecOutletTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerType.setStatus("current")


class _CyPMElecOutletTableVoltageType_Type(Integer32):
    """Custom type cyPMElecOutletTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecOutletTableVoltageType_Type.__name__ = "Integer32"
_CyPMElecOutletTableVoltageType_Object = MibTableColumn
cyPMElecOutletTableVoltageType = _CyPMElecOutletTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 14),
    _CyPMElecOutletTableVoltageType_Type()
)
cyPMElecOutletTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTableVoltageType.setStatus("current")


class _CyPMElecOutletTablePowerFactorType_Type(Integer32):
    """Custom type cyPMElecOutletTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("measured", 2))
    )


_CyPMElecOutletTablePowerFactorType_Type.__name__ = "Integer32"
_CyPMElecOutletTablePowerFactorType_Object = MibTableColumn
cyPMElecOutletTablePowerFactorType = _CyPMElecOutletTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 8, 1, 15),
    _CyPMElecOutletTablePowerFactorType_Type()
)
cyPMElecOutletTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMElecOutletTablePowerFactorType.setStatus("current")
_CyPMEnvMonTable_Object = MibTable
cyPMEnvMonTable = _CyPMEnvMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9)
)
if mibBuilder.loadTexts:
    cyPMEnvMonTable.setStatus("current")
_CyPMEnvMonTableEntry_Object = MibTableRow
cyPMEnvMonTableEntry = _CyPMEnvMonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1)
)
cyPMEnvMonTableEntry.setIndexNames(
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMEnvMonTablePortNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMEnvMonTablePduNumber"),
    (0, "CYCLADES-ACS5K-PM-MIB", "cyPMEnvMonTableIndex"),
)
if mibBuilder.loadTexts:
    cyPMEnvMonTableEntry.setStatus("current")
_CyPMEnvMonTablePortNumber_Type = InterfaceIndex
_CyPMEnvMonTablePortNumber_Object = MibTableColumn
cyPMEnvMonTablePortNumber = _CyPMEnvMonTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 1),
    _CyPMEnvMonTablePortNumber_Type()
)
cyPMEnvMonTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTablePortNumber.setStatus("current")
_CyPMEnvMonTablePduNumber_Type = InterfaceIndex
_CyPMEnvMonTablePduNumber_Object = MibTableColumn
cyPMEnvMonTablePduNumber = _CyPMEnvMonTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 2),
    _CyPMEnvMonTablePduNumber_Type()
)
cyPMEnvMonTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTablePduNumber.setStatus("current")
_CyPMEnvMonTableIndex_Type = InterfaceIndex
_CyPMEnvMonTableIndex_Object = MibTableColumn
cyPMEnvMonTableIndex = _CyPMEnvMonTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 3),
    _CyPMEnvMonTableIndex_Type()
)
cyPMEnvMonTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTableIndex.setStatus("current")
_CyPMEnvMonTableName_Type = DisplayString
_CyPMEnvMonTableName_Object = MibTableColumn
cyPMEnvMonTableName = _CyPMEnvMonTableName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 4),
    _CyPMEnvMonTableName_Type()
)
cyPMEnvMonTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTableName.setStatus("current")


class _CyPMEnvMonTableType_Type(Integer32):
    """Custom type cyPMEnvMonTableType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("temp-internal", 1),
          ("temperature", 2),
          ("humidity", 3),
          ("air-flow", 4),
          ("smoke", 5),
          ("dry-concact", 6),
          ("water-level", 7),
          ("motion", 8),
          ("unplugged", 9),
          ("unknown", 10))
    )


_CyPMEnvMonTableType_Type.__name__ = "Integer32"
_CyPMEnvMonTableType_Object = MibTableColumn
cyPMEnvMonTableType = _CyPMEnvMonTableType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 5),
    _CyPMEnvMonTableType_Type()
)
cyPMEnvMonTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTableType.setStatus("current")


class _CyPMEnvMonTableStatus_Type(Integer32):
    """Custom type cyPMEnvMonTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("triggered", 2),
          ("not-applicable", 3))
    )


_CyPMEnvMonTableStatus_Type.__name__ = "Integer32"
_CyPMEnvMonTableStatus_Object = MibTableColumn
cyPMEnvMonTableStatus = _CyPMEnvMonTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 6),
    _CyPMEnvMonTableStatus_Type()
)
cyPMEnvMonTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTableStatus.setStatus("current")
_CyPMEnvMonTableValue_Type = Integer32
_CyPMEnvMonTableValue_Object = MibTableColumn
cyPMEnvMonTableValue = _CyPMEnvMonTableValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 7),
    _CyPMEnvMonTableValue_Type()
)
cyPMEnvMonTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyPMEnvMonTableValue.setStatus("current")
_CyPMEnvMonTableMaxValue_Type = Integer32
_CyPMEnvMonTableMaxValue_Object = MibTableColumn
cyPMEnvMonTableMaxValue = _CyPMEnvMonTableMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 2925, 8, 5, 9, 1, 8),
    _CyPMEnvMonTableMaxValue_Type()
)
cyPMEnvMonTableMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyPMEnvMonTableMaxValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS5K-PM-MIB",
    **{"cyACS5KPM": cyACS5KPM,
       "cyNumberOfPM": cyNumberOfPM,
       "cyPMTable": cyPMTable,
       "cyPMEntry": cyPMEntry,
       "cyPMSerialPortNumber": cyPMSerialPortNumber,
       "cyPMNumberOutlets": cyPMNumberOutlets,
       "cyPMNumberUnits": cyPMNumberUnits,
       "cyPMCurrent": cyPMCurrent,
       "cyPMVersion": cyPMVersion,
       "cyPMCommand": cyPMCommand,
       "cyPMUnitTable": cyPMUnitTable,
       "cyPMUnitEntry": cyPMUnitEntry,
       "cyPMUnitNumber": cyPMUnitNumber,
       "cyPMUnitVersion": cyPMUnitVersion,
       "cyPMUnitOutlets": cyPMUnitOutlets,
       "cyPMUnitFirstOutlet": cyPMUnitFirstOutlet,
       "cyPMUnitCurrent": cyPMUnitCurrent,
       "cyPMUnitMaxCurrent": cyPMUnitMaxCurrent,
       "cyPMUnitSequenceInterval": cyPMUnitSequenceInterval,
       "cyPMUnitCycleInterval": cyPMUnitCycleInterval,
       "cyPMUnitID": cyPMUnitID,
       "cyPMUnitPhases": cyPMUnitPhases,
       "cyPMUnitBanks": cyPMUnitBanks,
       "cyPMUnitNominalVoltage": cyPMUnitNominalVoltage,
       "cyPMUnitPower": cyPMUnitPower,
       "cyOutletTable": cyOutletTable,
       "cyOutletEntry": cyOutletEntry,
       "cyOutletNumber": cyOutletNumber,
       "cyOutletName": cyOutletName,
       "cyOutletServer": cyOutletServer,
       "cyOutletPower": cyOutletPower,
       "cyOutletLock": cyOutletLock,
       "cyOutletPUInterval": cyOutletPUInterval,
       "cyOutletMinimumOnInterval": cyOutletMinimumOnInterval,
       "cyOutletMinimumOffInterval": cyOutletMinimumOffInterval,
       "cyOutletWakeupState": cyOutletWakeupState,
       "cyOutletPduID": cyOutletPduID,
       "cyOutletPduNumber": cyOutletPduNumber,
       "cyPMElecPduTable": cyPMElecPduTable,
       "cyPMElecPduTableEntry": cyPMElecPduTableEntry,
       "cyPMElecPduTablePortNumber": cyPMElecPduTablePortNumber,
       "cyPMElecPduTablePduNumber": cyPMElecPduTablePduNumber,
       "cyPMElecPduTableCurrentValue": cyPMElecPduTableCurrentValue,
       "cyPMElecPduTableCurrentMax": cyPMElecPduTableCurrentMax,
       "cyPMElecPduTablePowerValue": cyPMElecPduTablePowerValue,
       "cyPMElecPduTablePowerMax": cyPMElecPduTablePowerMax,
       "cyPMElecPduTableVoltageValue": cyPMElecPduTableVoltageValue,
       "cyPMElecPduTableVoltageMax": cyPMElecPduTableVoltageMax,
       "cyPMElecPduTablePowerFactorValue": cyPMElecPduTablePowerFactorValue,
       "cyPMElecPduTablePowerFactorMax": cyPMElecPduTablePowerFactorMax,
       "cyPMElecPduTablePowerType": cyPMElecPduTablePowerType,
       "cyPMElecPduTableVoltageType": cyPMElecPduTableVoltageType,
       "cyPMElecPduTablePowerFactorType": cyPMElecPduTablePowerFactorType,
       "cyPMElecPhaseTable": cyPMElecPhaseTable,
       "cyPMElecPhaseTableEntry": cyPMElecPhaseTableEntry,
       "cyPMElecPhaseTablePortNumber": cyPMElecPhaseTablePortNumber,
       "cyPMElecPhaseTablePduNumber": cyPMElecPhaseTablePduNumber,
       "cyPMElecPhaseTableIndex": cyPMElecPhaseTableIndex,
       "cyPMElecPhaseTableName": cyPMElecPhaseTableName,
       "cyPMElecPhaseTableCurrentValue": cyPMElecPhaseTableCurrentValue,
       "cyPMElecPhaseTableCurrentMax": cyPMElecPhaseTableCurrentMax,
       "cyPMElecPhaseTablePowerValue": cyPMElecPhaseTablePowerValue,
       "cyPMElecPhaseTablePowerMax": cyPMElecPhaseTablePowerMax,
       "cyPMElecPhaseTableVoltageValue": cyPMElecPhaseTableVoltageValue,
       "cyPMElecPhaseTableVoltageMax": cyPMElecPhaseTableVoltageMax,
       "cyPMElecPhaseTablePowerFactorValue": cyPMElecPhaseTablePowerFactorValue,
       "cyPMElecPhaseTablePowerFactorMax": cyPMElecPhaseTablePowerFactorMax,
       "cyPMElecPhaseTablePowerType": cyPMElecPhaseTablePowerType,
       "cyPMElecPhaseTableVoltageType": cyPMElecPhaseTableVoltageType,
       "cyPMElecPhaseTablePowerFactorType": cyPMElecPhaseTablePowerFactorType,
       "cyPMElecBankTable": cyPMElecBankTable,
       "cyPMElecBankTableEntry": cyPMElecBankTableEntry,
       "cyPMElecBankTablePortNumber": cyPMElecBankTablePortNumber,
       "cyPMElecBankTablePduNumber": cyPMElecBankTablePduNumber,
       "cyPMElecBankTableIndex": cyPMElecBankTableIndex,
       "cyPMElecBankTableName": cyPMElecBankTableName,
       "cyPMElecBankTableCurrentValue": cyPMElecBankTableCurrentValue,
       "cyPMElecBankTableCurrentMax": cyPMElecBankTableCurrentMax,
       "cyPMElecBankTablePowerValue": cyPMElecBankTablePowerValue,
       "cyPMElecBankTablePowerMax": cyPMElecBankTablePowerMax,
       "cyPMElecBankTableVoltageValue": cyPMElecBankTableVoltageValue,
       "cyPMElecBankTableVoltageMax": cyPMElecBankTableVoltageMax,
       "cyPMElecBankTablePowerFactorValue": cyPMElecBankTablePowerFactorValue,
       "cyPMElecBankTablePowerFactorMax": cyPMElecBankTablePowerFactorMax,
       "cyPMElecBankTablePowerType": cyPMElecBankTablePowerType,
       "cyPMElecBankTableVoltageType": cyPMElecBankTableVoltageType,
       "cyPMElecBankTablePowerFactorType": cyPMElecBankTablePowerFactorType,
       "cyPMElecOutletTable": cyPMElecOutletTable,
       "cyPMElecOutletTableEntry": cyPMElecOutletTableEntry,
       "cyPMElecOutletTablePortNumber": cyPMElecOutletTablePortNumber,
       "cyPMElecOutletTablePduNumber": cyPMElecOutletTablePduNumber,
       "cyPMElecOutletTableNumber": cyPMElecOutletTableNumber,
       "cyPMElecOutletTableName": cyPMElecOutletTableName,
       "cyPMElecOutletTableCurrentValue": cyPMElecOutletTableCurrentValue,
       "cyPMElecOutletTableCurrentMax": cyPMElecOutletTableCurrentMax,
       "cyPMElecOutletTablePowerValue": cyPMElecOutletTablePowerValue,
       "cyPMElecOutletTablePowerMax": cyPMElecOutletTablePowerMax,
       "cyPMElecOutletTableVoltageValue": cyPMElecOutletTableVoltageValue,
       "cyPMElecOutletTableVoltageMax": cyPMElecOutletTableVoltageMax,
       "cyPMElecOutletTablePowerFactorValue": cyPMElecOutletTablePowerFactorValue,
       "cyPMElecOutletTablePowerFactorMax": cyPMElecOutletTablePowerFactorMax,
       "cyPMElecOutletTablePowerType": cyPMElecOutletTablePowerType,
       "cyPMElecOutletTableVoltageType": cyPMElecOutletTableVoltageType,
       "cyPMElecOutletTablePowerFactorType": cyPMElecOutletTablePowerFactorType,
       "cyPMEnvMonTable": cyPMEnvMonTable,
       "cyPMEnvMonTableEntry": cyPMEnvMonTableEntry,
       "cyPMEnvMonTablePortNumber": cyPMEnvMonTablePortNumber,
       "cyPMEnvMonTablePduNumber": cyPMEnvMonTablePduNumber,
       "cyPMEnvMonTableIndex": cyPMEnvMonTableIndex,
       "cyPMEnvMonTableName": cyPMEnvMonTableName,
       "cyPMEnvMonTableType": cyPMEnvMonTableType,
       "cyPMEnvMonTableStatus": cyPMEnvMonTableStatus,
       "cyPMEnvMonTableValue": cyPMEnvMonTableValue,
       "cyPMEnvMonTableMaxValue": cyPMEnvMonTableMaxValue}
)
