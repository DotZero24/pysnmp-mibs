# SNMP MIB module (RAISECOM-FANMONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-FANMONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:49 2025
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

(raisecomSystem,) = mibBuilder.importSymbols(
    "RAISECOM-SYSTEM-MIB",
    "raisecomSystem")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raisecomFanMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5)
)
if mibBuilder.loadTexts:
    raisecomFanMonitor.setRevisions(
        ("2010-12-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomFanMonitorNotification_ObjectIdentity = ObjectIdentity
raisecomFanMonitorNotification = _RaisecomFanMonitorNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 1)
)
_RaisecomFanMonitorMibObjects_ObjectIdentity = ObjectIdentity
raisecomFanMonitorMibObjects = _RaisecomFanMonitorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2)
)
_RaisecomFanMonitorGlobalGroup_ObjectIdentity = ObjectIdentity
raisecomFanMonitorGlobalGroup = _RaisecomFanMonitorGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1)
)


class _RaisecomFanMonitorMode_Type(Integer32):
    """Custom type raisecomFanMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enforce", 1),
          ("auto", 2))
    )


_RaisecomFanMonitorMode_Type.__name__ = "Integer32"
_RaisecomFanMonitorMode_Object = MibScalar
raisecomFanMonitorMode = _RaisecomFanMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 1),
    _RaisecomFanMonitorMode_Type()
)
raisecomFanMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomFanMonitorMode.setStatus("current")


class _RaisecomFanMonitorSpdLevel_Type(Unsigned32):
    """Custom type raisecomFanMonitorSpdLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RaisecomFanMonitorSpdLevel_Type.__name__ = "Unsigned32"
_RaisecomFanMonitorSpdLevel_Object = MibScalar
raisecomFanMonitorSpdLevel = _RaisecomFanMonitorSpdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 2),
    _RaisecomFanMonitorSpdLevel_Type()
)
raisecomFanMonitorSpdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomFanMonitorSpdLevel.setStatus("current")
_RaisecomFanMonitorNumber_Type = Unsigned32
_RaisecomFanMonitorNumber_Object = MibScalar
raisecomFanMonitorNumber = _RaisecomFanMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 3),
    _RaisecomFanMonitorNumber_Type()
)
raisecomFanMonitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanMonitorNumber.setStatus("current")
_RaisecomFanMonitorLevlNumber_Type = Unsigned32
_RaisecomFanMonitorLevlNumber_Object = MibScalar
raisecomFanMonitorLevlNumber = _RaisecomFanMonitorLevlNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 4),
    _RaisecomFanMonitorLevlNumber_Type()
)
raisecomFanMonitorLevlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanMonitorLevlNumber.setStatus("current")


class _RaisecomFanCardState_Type(Integer32):
    """Custom type raisecomFanCardState based on Integer32"""
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
        *(("all-down", 1),
          ("all-up", 2),
          ("card1-up", 3),
          ("card2-up", 4))
    )


_RaisecomFanCardState_Type.__name__ = "Integer32"
_RaisecomFanCardState_Object = MibScalar
raisecomFanCardState = _RaisecomFanCardState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 5),
    _RaisecomFanCardState_Type()
)
raisecomFanCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanCardState.setStatus("current")
_RaisecomFanCardSerialNumber_Type = OctetString
_RaisecomFanCardSerialNumber_Object = MibScalar
raisecomFanCardSerialNumber = _RaisecomFanCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 6),
    _RaisecomFanCardSerialNumber_Type()
)
raisecomFanCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanCardSerialNumber.setStatus("current")


class _RaisecomFanMonitorTrapSendEnable_Type(Integer32):
    """Custom type raisecomFanMonitorTrapSendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RaisecomFanMonitorTrapSendEnable_Type.__name__ = "Integer32"
_RaisecomFanMonitorTrapSendEnable_Object = MibScalar
raisecomFanMonitorTrapSendEnable = _RaisecomFanMonitorTrapSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 1, 7),
    _RaisecomFanMonitorTrapSendEnable_Type()
)
raisecomFanMonitorTrapSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomFanMonitorTrapSendEnable.setStatus("current")
_RaisecomFanMonitorStateTable_Object = MibTable
raisecomFanMonitorStateTable = _RaisecomFanMonitorStateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomFanMonitorStateTable.setStatus("current")
_RaisecomFanMonitorStateEntry_Object = MibTableRow
raisecomFanMonitorStateEntry = _RaisecomFanMonitorStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 2, 1)
)
raisecomFanMonitorStateEntry.setIndexNames(
    (0, "RAISECOM-FANMONITOR-MIB", "raisecomFanIndex"),
)
if mibBuilder.loadTexts:
    raisecomFanMonitorStateEntry.setStatus("current")
_RaisecomFanIndex_Type = Unsigned32
_RaisecomFanIndex_Object = MibTableColumn
raisecomFanIndex = _RaisecomFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 2, 1, 1),
    _RaisecomFanIndex_Type()
)
raisecomFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomFanIndex.setStatus("current")
_RaisecomFanSpeedValue_Type = Unsigned32
_RaisecomFanSpeedValue_Object = MibTableColumn
raisecomFanSpeedValue = _RaisecomFanSpeedValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 2, 1, 2),
    _RaisecomFanSpeedValue_Type()
)
raisecomFanSpeedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanSpeedValue.setStatus("current")


class _RaisecomFanWorkState_Type(Integer32):
    """Custom type raisecomFanWorkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RaisecomFanWorkState_Type.__name__ = "Integer32"
_RaisecomFanWorkState_Object = MibTableColumn
raisecomFanWorkState = _RaisecomFanWorkState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 2, 1, 3),
    _RaisecomFanWorkState_Type()
)
raisecomFanWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFanWorkState.setStatus("current")
_RaisecomFanSpeedLevelTable_Object = MibTable
raisecomFanSpeedLevelTable = _RaisecomFanSpeedLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomFanSpeedLevelTable.setStatus("current")
_RaisecomFanSpeedLevelEntry_Object = MibTableRow
raisecomFanSpeedLevelEntry = _RaisecomFanSpeedLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 3, 1)
)
raisecomFanSpeedLevelEntry.setIndexNames(
    (0, "RAISECOM-FANMONITOR-MIB", "raisecomFanSpeedLevelIndex"),
)
if mibBuilder.loadTexts:
    raisecomFanSpeedLevelEntry.setStatus("current")
_RaisecomFanSpeedLevelIndex_Type = Unsigned32
_RaisecomFanSpeedLevelIndex_Object = MibTableColumn
raisecomFanSpeedLevelIndex = _RaisecomFanSpeedLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 3, 1, 1),
    _RaisecomFanSpeedLevelIndex_Type()
)
raisecomFanSpeedLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomFanSpeedLevelIndex.setStatus("current")
_RaisecomFanSpeedDueValue_Type = Unsigned32
_RaisecomFanSpeedDueValue_Object = MibTableColumn
raisecomFanSpeedDueValue = _RaisecomFanSpeedDueValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 3, 1, 2),
    _RaisecomFanSpeedDueValue_Type()
)
raisecomFanSpeedDueValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomFanSpeedDueValue.setStatus("current")


class _RaisecomFanSpeedTemperatureScale_Type(Unsigned32):
    """Custom type raisecomFanSpeedTemperatureScale based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 75),
    )


_RaisecomFanSpeedTemperatureScale_Type.__name__ = "Unsigned32"
_RaisecomFanSpeedTemperatureScale_Object = MibTableColumn
raisecomFanSpeedTemperatureScale = _RaisecomFanSpeedTemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 2, 3, 1, 3),
    _RaisecomFanSpeedTemperatureScale_Type()
)
raisecomFanSpeedTemperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomFanSpeedTemperatureScale.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomFanSpeedNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 1, 1)
)
raisecomFanSpeedNormal.setObjects(
      *(("RAISECOM-FANMONITOR-MIB", "raisecomFanIndex"),
        ("RAISECOM-FANMONITOR-MIB", "raisecomFanSpeedValue"))
)
if mibBuilder.loadTexts:
    raisecomFanSpeedNormal.setStatus(
        "current"
    )

raisecomFanSpeedAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 1, 2)
)
raisecomFanSpeedAbnormal.setObjects(
      *(("RAISECOM-FANMONITOR-MIB", "raisecomFanIndex"),
        ("RAISECOM-FANMONITOR-MIB", "raisecomFanSpeedValue"),
        ("RAISECOM-FANMONITOR-MIB", "raisecomFanSpeedDueValue"))
)
if mibBuilder.loadTexts:
    raisecomFanSpeedAbnormal.setStatus(
        "current"
    )

raisecomFanCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 1, 3)
)
raisecomFanCardUp.setObjects(
    ("RAISECOM-FANMONITOR-MIB", "raisecomFanCardState")
)
if mibBuilder.loadTexts:
    raisecomFanCardUp.setStatus(
        "current"
    )

raisecomFanCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 5, 1, 4)
)
raisecomFanCardDown.setObjects(
    ("RAISECOM-FANMONITOR-MIB", "raisecomFanCardState")
)
if mibBuilder.loadTexts:
    raisecomFanCardDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-FANMONITOR-MIB",
    **{"raisecomFanMonitor": raisecomFanMonitor,
       "raisecomFanMonitorNotification": raisecomFanMonitorNotification,
       "raisecomFanSpeedNormal": raisecomFanSpeedNormal,
       "raisecomFanSpeedAbnormal": raisecomFanSpeedAbnormal,
       "raisecomFanCardUp": raisecomFanCardUp,
       "raisecomFanCardDown": raisecomFanCardDown,
       "raisecomFanMonitorMibObjects": raisecomFanMonitorMibObjects,
       "raisecomFanMonitorGlobalGroup": raisecomFanMonitorGlobalGroup,
       "raisecomFanMonitorMode": raisecomFanMonitorMode,
       "raisecomFanMonitorSpdLevel": raisecomFanMonitorSpdLevel,
       "raisecomFanMonitorNumber": raisecomFanMonitorNumber,
       "raisecomFanMonitorLevlNumber": raisecomFanMonitorLevlNumber,
       "raisecomFanCardState": raisecomFanCardState,
       "raisecomFanCardSerialNumber": raisecomFanCardSerialNumber,
       "raisecomFanMonitorTrapSendEnable": raisecomFanMonitorTrapSendEnable,
       "raisecomFanMonitorStateTable": raisecomFanMonitorStateTable,
       "raisecomFanMonitorStateEntry": raisecomFanMonitorStateEntry,
       "raisecomFanIndex": raisecomFanIndex,
       "raisecomFanSpeedValue": raisecomFanSpeedValue,
       "raisecomFanWorkState": raisecomFanWorkState,
       "raisecomFanSpeedLevelTable": raisecomFanSpeedLevelTable,
       "raisecomFanSpeedLevelEntry": raisecomFanSpeedLevelEntry,
       "raisecomFanSpeedLevelIndex": raisecomFanSpeedLevelIndex,
       "raisecomFanSpeedDueValue": raisecomFanSpeedDueValue,
       "raisecomFanSpeedTemperatureScale": raisecomFanSpeedTemperatureScale}
)
