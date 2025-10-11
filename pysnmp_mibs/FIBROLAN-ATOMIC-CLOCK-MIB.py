# SNMP MIB module (FIBROLAN-ATOMIC-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fibrolan/FIBROLAN-ATOMIC-CLOCK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:13 2025
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

(fibrolanGeneric,) = mibBuilder.importSymbols(
    "FIBROLAN-COMMON-MIB",
    "fibrolanGeneric")

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

flAtomicClock = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220)
)
if mibBuilder.loadTexts:
    flAtomicClock.setRevisions(
        ("2015-09-15 00:00",
         "2015-08-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlAtomicClockNotifications_ObjectIdentity = ObjectIdentity
flAtomicClockNotifications = _FlAtomicClockNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 0)
)
_FlAtomicClockMIBObjects_ObjectIdentity = ObjectIdentity
flAtomicClockMIBObjects = _FlAtomicClockMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1)
)
_FlAtomicClockTable_Object = MibTable
flAtomicClockTable = _FlAtomicClockTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10)
)
if mibBuilder.loadTexts:
    flAtomicClockTable.setStatus("current")
_FlAtomicClockEntry_Object = MibTableRow
flAtomicClockEntry = _FlAtomicClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1)
)
flAtomicClockEntry.setIndexNames(
    (0, "FIBROLAN-ATOMIC-CLOCK-MIB", "flAtomicClockModuleId"),
)
if mibBuilder.loadTexts:
    flAtomicClockEntry.setStatus("current")


class _FlAtomicClockModuleId_Type(Integer32):
    """Custom type flAtomicClockModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlAtomicClockModuleId_Type.__name__ = "Integer32"
_FlAtomicClockModuleId_Object = MibTableColumn
flAtomicClockModuleId = _FlAtomicClockModuleId_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 1),
    _FlAtomicClockModuleId_Type()
)
flAtomicClockModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flAtomicClockModuleId.setStatus("current")


class _FlAtomicClockModuleType_Type(DisplayString):
    """Custom type flAtomicClockModuleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockModuleType_Type.__name__ = "DisplayString"
_FlAtomicClockModuleType_Object = MibTableColumn
flAtomicClockModuleType = _FlAtomicClockModuleType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 2),
    _FlAtomicClockModuleType_Type()
)
flAtomicClockModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockModuleType.setStatus("current")


class _FlAtomicClockModulePartNumber_Type(DisplayString):
    """Custom type flAtomicClockModulePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockModulePartNumber_Type.__name__ = "DisplayString"
_FlAtomicClockModulePartNumber_Object = MibTableColumn
flAtomicClockModulePartNumber = _FlAtomicClockModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 3),
    _FlAtomicClockModulePartNumber_Type()
)
flAtomicClockModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockModulePartNumber.setStatus("current")


class _FlAtomicClockModuleSerialNumber_Type(DisplayString):
    """Custom type flAtomicClockModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockModuleSerialNumber_Type.__name__ = "DisplayString"
_FlAtomicClockModuleSerialNumber_Object = MibTableColumn
flAtomicClockModuleSerialNumber = _FlAtomicClockModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 4),
    _FlAtomicClockModuleSerialNumber_Type()
)
flAtomicClockModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockModuleSerialNumber.setStatus("current")


class _FlAtomicClockOscillatorType_Type(Integer32):
    """Custom type flAtomicClockOscillatorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("rubidium", 1),
          ("cesium", 2),
          ("other", 99))
    )


_FlAtomicClockOscillatorType_Type.__name__ = "Integer32"
_FlAtomicClockOscillatorType_Object = MibTableColumn
flAtomicClockOscillatorType = _FlAtomicClockOscillatorType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 5),
    _FlAtomicClockOscillatorType_Type()
)
flAtomicClockOscillatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockOscillatorType.setStatus("current")


class _FlAtomicClockOscillatorPartNumber_Type(DisplayString):
    """Custom type flAtomicClockOscillatorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockOscillatorPartNumber_Type.__name__ = "DisplayString"
_FlAtomicClockOscillatorPartNumber_Object = MibTableColumn
flAtomicClockOscillatorPartNumber = _FlAtomicClockOscillatorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 6),
    _FlAtomicClockOscillatorPartNumber_Type()
)
flAtomicClockOscillatorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockOscillatorPartNumber.setStatus("current")


class _FlAtomicClockOscillatorSerialNumber_Type(DisplayString):
    """Custom type flAtomicClockOscillatorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockOscillatorSerialNumber_Type.__name__ = "DisplayString"
_FlAtomicClockOscillatorSerialNumber_Object = MibTableColumn
flAtomicClockOscillatorSerialNumber = _FlAtomicClockOscillatorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 7),
    _FlAtomicClockOscillatorSerialNumber_Type()
)
flAtomicClockOscillatorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockOscillatorSerialNumber.setStatus("current")


class _FlAtomicClockOscillatorFwVersion_Type(DisplayString):
    """Custom type flAtomicClockOscillatorFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlAtomicClockOscillatorFwVersion_Type.__name__ = "DisplayString"
_FlAtomicClockOscillatorFwVersion_Object = MibTableColumn
flAtomicClockOscillatorFwVersion = _FlAtomicClockOscillatorFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 8),
    _FlAtomicClockOscillatorFwVersion_Type()
)
flAtomicClockOscillatorFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockOscillatorFwVersion.setStatus("current")


class _FlAtomicClockState_Type(Integer32):
    """Custom type flAtomicClockState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("unplugged", 1),
          ("warming", 2),
          ("ppsShifting", 3),
          ("shortTermSteering", 4),
          ("averaging", 5),
          ("longTermSteering", 6),
          ("holdover", 7),
          ("holdoverRecovery", 8),
          ("freeRunning", 9),
          ("other", 99))
    )


_FlAtomicClockState_Type.__name__ = "Integer32"
_FlAtomicClockState_Object = MibTableColumn
flAtomicClockState = _FlAtomicClockState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 9),
    _FlAtomicClockState_Type()
)
flAtomicClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockState.setStatus("current")
_FlAtomicClockStateLastChange_Type = TimeTicks
_FlAtomicClockStateLastChange_Object = MibTableColumn
flAtomicClockStateLastChange = _FlAtomicClockStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 10),
    _FlAtomicClockStateLastChange_Type()
)
flAtomicClockStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockStateLastChange.setStatus("current")


class _FlAtomicClockTemperature_Type(Integer32):
    """Custom type flAtomicClockTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FlAtomicClockTemperature_Type.__name__ = "Integer32"
_FlAtomicClockTemperature_Object = MibTableColumn
flAtomicClockTemperature = _FlAtomicClockTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 11),
    _FlAtomicClockTemperature_Type()
)
flAtomicClockTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockTemperature.setStatus("current")


class _FlAtomicClockTemperatureAlarmState_Type(Integer32):
    """Custom type flAtomicClockTemperatureAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("error", 3),
          ("other", 99))
    )


_FlAtomicClockTemperatureAlarmState_Type.__name__ = "Integer32"
_FlAtomicClockTemperatureAlarmState_Object = MibTableColumn
flAtomicClockTemperatureAlarmState = _FlAtomicClockTemperatureAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 12),
    _FlAtomicClockTemperatureAlarmState_Type()
)
flAtomicClockTemperatureAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockTemperatureAlarmState.setStatus("current")


class _FlAtomicClockCellHeaterCurrent_Type(Integer32):
    """Custom type flAtomicClockCellHeaterCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_FlAtomicClockCellHeaterCurrent_Type.__name__ = "Integer32"
_FlAtomicClockCellHeaterCurrent_Object = MibTableColumn
flAtomicClockCellHeaterCurrent = _FlAtomicClockCellHeaterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 13),
    _FlAtomicClockCellHeaterCurrent_Type()
)
flAtomicClockCellHeaterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockCellHeaterCurrent.setStatus("current")


class _FlAtomicClockCellHeaterCurrentAlarmState_Type(Integer32):
    """Custom type flAtomicClockCellHeaterCurrentAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("error", 3),
          ("other", 99))
    )


_FlAtomicClockCellHeaterCurrentAlarmState_Type.__name__ = "Integer32"
_FlAtomicClockCellHeaterCurrentAlarmState_Object = MibTableColumn
flAtomicClockCellHeaterCurrentAlarmState = _FlAtomicClockCellHeaterCurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 14),
    _FlAtomicClockCellHeaterCurrentAlarmState_Type()
)
flAtomicClockCellHeaterCurrentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockCellHeaterCurrentAlarmState.setStatus("current")


class _FlAtomicClockAdjustPp15_Type(Integer32):
    """Custom type flAtomicClockAdjustPp15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000000, 10000000),
    )


_FlAtomicClockAdjustPp15_Type.__name__ = "Integer32"
_FlAtomicClockAdjustPp15_Object = MibTableColumn
flAtomicClockAdjustPp15 = _FlAtomicClockAdjustPp15_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 1, 10, 1, 15),
    _FlAtomicClockAdjustPp15_Type()
)
flAtomicClockAdjustPp15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAtomicClockAdjustPp15.setStatus("current")

# Managed Objects groups


# Notification objects

flAtomicClockStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 0, 10)
)
flAtomicClockStateChange.setObjects(
    ("FIBROLAN-ATOMIC-CLOCK-MIB", "flAtomicClockState")
)
if mibBuilder.loadTexts:
    flAtomicClockStateChange.setStatus(
        "current"
    )

flAtomicClockTemperatureAlarmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 220, 0, 20)
)
flAtomicClockTemperatureAlarmStateChange.setObjects(
    ("FIBROLAN-ATOMIC-CLOCK-MIB", "flAtomicClockTemperatureAlarmState")
)
if mibBuilder.loadTexts:
    flAtomicClockTemperatureAlarmStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-ATOMIC-CLOCK-MIB",
    **{"flAtomicClock": flAtomicClock,
       "flAtomicClockNotifications": flAtomicClockNotifications,
       "flAtomicClockStateChange": flAtomicClockStateChange,
       "flAtomicClockTemperatureAlarmStateChange": flAtomicClockTemperatureAlarmStateChange,
       "flAtomicClockMIBObjects": flAtomicClockMIBObjects,
       "flAtomicClockTable": flAtomicClockTable,
       "flAtomicClockEntry": flAtomicClockEntry,
       "flAtomicClockModuleId": flAtomicClockModuleId,
       "flAtomicClockModuleType": flAtomicClockModuleType,
       "flAtomicClockModulePartNumber": flAtomicClockModulePartNumber,
       "flAtomicClockModuleSerialNumber": flAtomicClockModuleSerialNumber,
       "flAtomicClockOscillatorType": flAtomicClockOscillatorType,
       "flAtomicClockOscillatorPartNumber": flAtomicClockOscillatorPartNumber,
       "flAtomicClockOscillatorSerialNumber": flAtomicClockOscillatorSerialNumber,
       "flAtomicClockOscillatorFwVersion": flAtomicClockOscillatorFwVersion,
       "flAtomicClockState": flAtomicClockState,
       "flAtomicClockStateLastChange": flAtomicClockStateLastChange,
       "flAtomicClockTemperature": flAtomicClockTemperature,
       "flAtomicClockTemperatureAlarmState": flAtomicClockTemperatureAlarmState,
       "flAtomicClockCellHeaterCurrent": flAtomicClockCellHeaterCurrent,
       "flAtomicClockCellHeaterCurrentAlarmState": flAtomicClockCellHeaterCurrentAlarmState,
       "flAtomicClockAdjustPp15": flAtomicClockAdjustPp15}
)
