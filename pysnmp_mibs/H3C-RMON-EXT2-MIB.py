# SNMP MIB module (H3C-RMON-EXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-RMON-EXT2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:13 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

h3cRmonExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125)
)
if mibBuilder.loadTexts:
    h3cRmonExt.setRevisions(
        ("2012-06-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRmonExtEvent_ObjectIdentity = ObjectIdentity
h3cRmonExtEvent = _H3cRmonExtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 0)
)
if mibBuilder.loadTexts:
    h3cRmonExtEvent.setStatus("current")
_H3cRmonExtAlarmTable_Object = MibTable
h3cRmonExtAlarmTable = _H3cRmonExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1)
)
if mibBuilder.loadTexts:
    h3cRmonExtAlarmTable.setStatus("current")
_H3cRmonExtAlarmEntry_Object = MibTableRow
h3cRmonExtAlarmEntry = _H3cRmonExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1)
)
h3cRmonExtAlarmEntry.setIndexNames(
    (0, "H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    h3cRmonExtAlarmEntry.setStatus("current")


class _H3cRmonExtAlarmIndex_Type(Integer32):
    """Custom type h3cRmonExtAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cRmonExtAlarmIndex_Type.__name__ = "Integer32"
_H3cRmonExtAlarmIndex_Object = MibTableColumn
h3cRmonExtAlarmIndex = _H3cRmonExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 1),
    _H3cRmonExtAlarmIndex_Type()
)
h3cRmonExtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmIndex.setStatus("current")


class _H3cRmonExtAlarmInterval_Type(Integer32):
    """Custom type h3cRmonExtAlarmInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_H3cRmonExtAlarmInterval_Type.__name__ = "Integer32"
_H3cRmonExtAlarmInterval_Object = MibTableColumn
h3cRmonExtAlarmInterval = _H3cRmonExtAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 2),
    _H3cRmonExtAlarmInterval_Type()
)
h3cRmonExtAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmInterval.setStatus("current")
_H3cRmonExtAlarmVariable_Type = DisplayString
_H3cRmonExtAlarmVariable_Object = MibTableColumn
h3cRmonExtAlarmVariable = _H3cRmonExtAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 3),
    _H3cRmonExtAlarmVariable_Type()
)
h3cRmonExtAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmVariable.setStatus("current")
_H3cRmonExtAlarmSympol_Type = DisplayString
_H3cRmonExtAlarmSympol_Object = MibTableColumn
h3cRmonExtAlarmSympol = _H3cRmonExtAlarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 4),
    _H3cRmonExtAlarmSympol_Type()
)
h3cRmonExtAlarmSympol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmSympol.setStatus("current")


class _H3cRmonExtAlarmSampleType_Type(Integer32):
    """Custom type h3cRmonExtAlarmSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2),
          ("speedValue", 3))
    )


_H3cRmonExtAlarmSampleType_Type.__name__ = "Integer32"
_H3cRmonExtAlarmSampleType_Object = MibTableColumn
h3cRmonExtAlarmSampleType = _H3cRmonExtAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 5),
    _H3cRmonExtAlarmSampleType_Type()
)
h3cRmonExtAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmSampleType.setStatus("current")
_H3cRmonExtAlarmValue_Type = Integer32
_H3cRmonExtAlarmValue_Object = MibTableColumn
h3cRmonExtAlarmValue = _H3cRmonExtAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 6),
    _H3cRmonExtAlarmValue_Type()
)
h3cRmonExtAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmValue.setStatus("current")


class _H3cRmonExtAlarmStartupAlarm_Type(Integer32):
    """Custom type h3cRmonExtAlarmStartupAlarm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_H3cRmonExtAlarmStartupAlarm_Type.__name__ = "Integer32"
_H3cRmonExtAlarmStartupAlarm_Object = MibTableColumn
h3cRmonExtAlarmStartupAlarm = _H3cRmonExtAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 7),
    _H3cRmonExtAlarmStartupAlarm_Type()
)
h3cRmonExtAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmStartupAlarm.setStatus("current")


class _H3cRmonExtAlarmRisingThreshold_Type(Integer32):
    """Custom type h3cRmonExtAlarmRisingThreshold based on Integer32"""
    defaultValue = 1


_H3cRmonExtAlarmRisingThreshold_Type.__name__ = "Integer32"
_H3cRmonExtAlarmRisingThreshold_Object = MibTableColumn
h3cRmonExtAlarmRisingThreshold = _H3cRmonExtAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 8),
    _H3cRmonExtAlarmRisingThreshold_Type()
)
h3cRmonExtAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmRisingThreshold.setStatus("current")


class _H3cRmonExtAlarmFallingThreshold_Type(Integer32):
    """Custom type h3cRmonExtAlarmFallingThreshold based on Integer32"""
    defaultValue = 0


_H3cRmonExtAlarmFallingThreshold_Type.__name__ = "Integer32"
_H3cRmonExtAlarmFallingThreshold_Object = MibTableColumn
h3cRmonExtAlarmFallingThreshold = _H3cRmonExtAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 9),
    _H3cRmonExtAlarmFallingThreshold_Type()
)
h3cRmonExtAlarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmFallingThreshold.setStatus("current")


class _H3cRmonExtAlarmRisingEvtIndex_Type(Integer32):
    """Custom type h3cRmonExtAlarmRisingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cRmonExtAlarmRisingEvtIndex_Type.__name__ = "Integer32"
_H3cRmonExtAlarmRisingEvtIndex_Object = MibTableColumn
h3cRmonExtAlarmRisingEvtIndex = _H3cRmonExtAlarmRisingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 10),
    _H3cRmonExtAlarmRisingEvtIndex_Type()
)
h3cRmonExtAlarmRisingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmRisingEvtIndex.setStatus("current")


class _H3cRmonExtAlarmFallingEvtIndex_Type(Integer32):
    """Custom type h3cRmonExtAlarmFallingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cRmonExtAlarmFallingEvtIndex_Type.__name__ = "Integer32"
_H3cRmonExtAlarmFallingEvtIndex_Object = MibTableColumn
h3cRmonExtAlarmFallingEvtIndex = _H3cRmonExtAlarmFallingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 11),
    _H3cRmonExtAlarmFallingEvtIndex_Type()
)
h3cRmonExtAlarmFallingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmFallingEvtIndex.setStatus("current")


class _H3cRmonExtAlarmStatCycle_Type(Integer32):
    """Custom type h3cRmonExtAlarmStatCycle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967),
    )


_H3cRmonExtAlarmStatCycle_Type.__name__ = "Integer32"
_H3cRmonExtAlarmStatCycle_Object = MibTableColumn
h3cRmonExtAlarmStatCycle = _H3cRmonExtAlarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 12),
    _H3cRmonExtAlarmStatCycle_Type()
)
h3cRmonExtAlarmStatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmStatCycle.setStatus("current")


class _H3cRmonExtAlarmStatType_Type(Integer32):
    """Custom type h3cRmonExtAlarmStatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forever", 1),
          ("during", 2))
    )


_H3cRmonExtAlarmStatType_Type.__name__ = "Integer32"
_H3cRmonExtAlarmStatType_Object = MibTableColumn
h3cRmonExtAlarmStatType = _H3cRmonExtAlarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 13),
    _H3cRmonExtAlarmStatType_Type()
)
h3cRmonExtAlarmStatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmStatType.setStatus("current")
_H3cRmonExtAlarmOwner_Type = OwnerString
_H3cRmonExtAlarmOwner_Object = MibTableColumn
h3cRmonExtAlarmOwner = _H3cRmonExtAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 14),
    _H3cRmonExtAlarmOwner_Type()
)
h3cRmonExtAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmOwner.setStatus("current")
_H3cRmonExtAlarmStatus_Type = EntryStatus
_H3cRmonExtAlarmStatus_Object = MibTableColumn
h3cRmonExtAlarmStatus = _H3cRmonExtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 1, 1, 15),
    _H3cRmonExtAlarmStatus_Type()
)
h3cRmonExtAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRmonExtAlarmStatus.setStatus("current")

# Managed Objects groups


# Notification objects

h3cRmonExtRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 0, 1)
)
h3cRmonExtRisingAlarm.setObjects(
      *(("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmIndex"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmSympol"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmSampleType"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmValue"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    h3cRmonExtRisingAlarm.setStatus(
        "current"
    )

h3cRmonExtFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 125, 0, 2)
)
h3cRmonExtFallingAlarm.setObjects(
      *(("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmIndex"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmSympol"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmSampleType"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmValue"),
        ("H3C-RMON-EXT2-MIB", "h3cRmonExtAlarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    h3cRmonExtFallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-RMON-EXT2-MIB",
    **{"h3cRmonExt": h3cRmonExt,
       "h3cRmonExtEvent": h3cRmonExtEvent,
       "h3cRmonExtRisingAlarm": h3cRmonExtRisingAlarm,
       "h3cRmonExtFallingAlarm": h3cRmonExtFallingAlarm,
       "h3cRmonExtAlarmTable": h3cRmonExtAlarmTable,
       "h3cRmonExtAlarmEntry": h3cRmonExtAlarmEntry,
       "h3cRmonExtAlarmIndex": h3cRmonExtAlarmIndex,
       "h3cRmonExtAlarmInterval": h3cRmonExtAlarmInterval,
       "h3cRmonExtAlarmVariable": h3cRmonExtAlarmVariable,
       "h3cRmonExtAlarmSympol": h3cRmonExtAlarmSympol,
       "h3cRmonExtAlarmSampleType": h3cRmonExtAlarmSampleType,
       "h3cRmonExtAlarmValue": h3cRmonExtAlarmValue,
       "h3cRmonExtAlarmStartupAlarm": h3cRmonExtAlarmStartupAlarm,
       "h3cRmonExtAlarmRisingThreshold": h3cRmonExtAlarmRisingThreshold,
       "h3cRmonExtAlarmFallingThreshold": h3cRmonExtAlarmFallingThreshold,
       "h3cRmonExtAlarmRisingEvtIndex": h3cRmonExtAlarmRisingEvtIndex,
       "h3cRmonExtAlarmFallingEvtIndex": h3cRmonExtAlarmFallingEvtIndex,
       "h3cRmonExtAlarmStatCycle": h3cRmonExtAlarmStatCycle,
       "h3cRmonExtAlarmStatType": h3cRmonExtAlarmStatType,
       "h3cRmonExtAlarmOwner": h3cRmonExtAlarmOwner,
       "h3cRmonExtAlarmStatus": h3cRmonExtAlarmStatus}
)
