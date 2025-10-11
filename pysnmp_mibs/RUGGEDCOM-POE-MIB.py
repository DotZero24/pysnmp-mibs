# SNMP MIB module (RUGGEDCOM-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:45 2025
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

(ruggedcomMgmt,
 ruggedcomTraps) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt",
    "ruggedcomTraps")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7)
)
if mibBuilder.loadTexts:
    rcPoe.setRevisions(
        ("2021-09-07 14:00",
         "2012-06-01 17:00",
         "2011-02-20 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPoeBase_ObjectIdentity = ObjectIdentity
rcPoeBase = _RcPoeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1)
)


class _RcPoeCapacity_Type(Integer32):
    """Custom type rcPoeCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcPoeCapacity_Type.__name__ = "Integer32"
_RcPoeCapacity_Object = MibScalar
rcPoeCapacity = _RcPoeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 1),
    _RcPoeCapacity_Type()
)
rcPoeCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPoeCapacity.setStatus("current")
if mibBuilder.loadTexts:
    rcPoeCapacity.setUnits("W")


class _RcPoeMinimumVoltage_Type(Integer32):
    """Custom type rcPoeMinimumVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(39, 57),
    )


_RcPoeMinimumVoltage_Type.__name__ = "Integer32"
_RcPoeMinimumVoltage_Object = MibScalar
rcPoeMinimumVoltage = _RcPoeMinimumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 2),
    _RcPoeMinimumVoltage_Type()
)
rcPoeMinimumVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPoeMinimumVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rcPoeMinimumVoltage.setUnits("V")


class _RcPoeReenableTime_Type(Unsigned32):
    """Custom type rcPoeReenableTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4294967295),
    )


_RcPoeReenableTime_Type.__name__ = "Unsigned32"
_RcPoeReenableTime_Object = MibScalar
rcPoeReenableTime = _RcPoeReenableTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 3),
    _RcPoeReenableTime_Type()
)
rcPoeReenableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPoeReenableTime.setStatus("current")
if mibBuilder.loadTexts:
    rcPoeReenableTime.setUnits("seconds")
_RcPoeConsumption_Type = Integer32
_RcPoeConsumption_Object = MibScalar
rcPoeConsumption = _RcPoeConsumption_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 4),
    _RcPoeConsumption_Type()
)
rcPoeConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoeConsumption.setStatus("current")
if mibBuilder.loadTexts:
    rcPoeConsumption.setUnits("seconds")
_RcPoeOverheatStatus_Type = TruthValue
_RcPoeOverheatStatus_Object = MibScalar
rcPoeOverheatStatus = _RcPoeOverheatStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 5),
    _RcPoeOverheatStatus_Type()
)
rcPoeOverheatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoeOverheatStatus.setStatus("current")
_RcPoeOverloadStatus_Type = TruthValue
_RcPoeOverloadStatus_Object = MibScalar
rcPoeOverloadStatus = _RcPoeOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 6),
    _RcPoeOverloadStatus_Type()
)
rcPoeOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoeOverloadStatus.setStatus("current")
_RcPoeUndervoltageStatus_Type = TruthValue
_RcPoeUndervoltageStatus_Object = MibScalar
rcPoeUndervoltageStatus = _RcPoeUndervoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 1, 7),
    _RcPoeUndervoltageStatus_Type()
)
rcPoeUndervoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoeUndervoltageStatus.setStatus("current")
_RcPoeTables_ObjectIdentity = ObjectIdentity
rcPoeTables = _RcPoeTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2)
)
_RcPoePortTable_Object = MibTable
rcPoePortTable = _RcPoePortTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    rcPoePortTable.setStatus("current")
_RcPoePortEntry_Object = MibTableRow
rcPoePortEntry = _RcPoePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1)
)
rcPoePortEntry.setIndexNames(
    (0, "RUGGEDCOM-POE-MIB", "rcPoePortNumber"),
)
if mibBuilder.loadTexts:
    rcPoePortEntry.setStatus("current")


class _RcPoePort_Type(Integer32):
    """Custom type rcPoePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcPoePort_Type.__name__ = "Integer32"
_RcPoePort_Object = MibTableColumn
rcPoePort = _RcPoePort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 1),
    _RcPoePort_Type()
)
rcPoePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPoePort.setStatus("current")
_RcPoePortAdmin_Type = TruthValue
_RcPoePortAdmin_Object = MibTableColumn
rcPoePortAdmin = _RcPoePortAdmin_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 2),
    _RcPoePortAdmin_Type()
)
rcPoePortAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPoePortAdmin.setStatus("current")


class _RcPoePortPriority_Type(Integer32):
    """Custom type rcPoePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("low", 2))
    )


_RcPoePortPriority_Type.__name__ = "Integer32"
_RcPoePortPriority_Object = MibTableColumn
rcPoePortPriority = _RcPoePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 3),
    _RcPoePortPriority_Type()
)
rcPoePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPoePortPriority.setStatus("current")


class _RcPoePortPowered_Type(Integer32):
    """Custom type rcPoePortPowered based on Integer32"""
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
        *(("powerOn", 1),
          ("powerOff", 2),
          ("twoPairsOn", 3),
          ("fourPairsOn", 4))
    )


_RcPoePortPowered_Type.__name__ = "Integer32"
_RcPoePortPowered_Object = MibTableColumn
rcPoePortPowered = _RcPoePortPowered_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 4),
    _RcPoePortPowered_Type()
)
rcPoePortPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoePortPowered.setStatus("current")


class _RcPoePortClass_Type(Integer32):
    """Custom type rcPoePortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcPoePortClass_Type.__name__ = "Integer32"
_RcPoePortClass_Object = MibTableColumn
rcPoePortClass = _RcPoePortClass_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 5),
    _RcPoePortClass_Type()
)
rcPoePortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoePortClass.setStatus("current")


class _RcPoePortVoltage_Type(Integer32):
    """Custom type rcPoePortVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcPoePortVoltage_Type.__name__ = "Integer32"
_RcPoePortVoltage_Object = MibTableColumn
rcPoePortVoltage = _RcPoePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 6),
    _RcPoePortVoltage_Type()
)
rcPoePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rcPoePortVoltage.setUnits("V")


class _RcPoePortCurrent_Type(Integer32):
    """Custom type rcPoePortCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcPoePortCurrent_Type.__name__ = "Integer32"
_RcPoePortCurrent_Object = MibTableColumn
rcPoePortCurrent = _RcPoePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 2, 1, 1, 7),
    _RcPoePortCurrent_Type()
)
rcPoePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPoePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rcPoePortCurrent.setUnits("mA")
_RcPoeConformance_ObjectIdentity = ObjectIdentity
rcPoeConformance = _RcPoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3)
)
_RcPoeGroups_ObjectIdentity = ObjectIdentity
rcPoeGroups = _RcPoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2)
)
_RuggedcomPoeTraps_ObjectIdentity = ObjectIdentity
ruggedcomPoeTraps = _RuggedcomPoeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 5, 12)
)

# Managed Objects groups

rcBasePoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2, 1)
)
rcBasePoeGroup.setObjects(
      *(("RUGGEDCOM-POE-MIB", "rcPoeCapacity"),
        ("RUGGEDCOM-POE-MIB", "rcPoeMinimumVoltage"),
        ("RUGGEDCOM-POE-MIB", "rcPoeReenableTime"),
        ("RUGGEDCOM-POE-MIB", "rcPoeConsumption"))
)
if mibBuilder.loadTexts:
    rcBasePoeGroup.setStatus("current")

rcBasePoeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2, 2)
)
rcBasePoeStatusGroup.setObjects(
      *(("RUGGEDCOM-POE-MIB", "rcPoeOverheatStatus"),
        ("RUGGEDCOM-POE-MIB", "rcPoeOverloadStatus"),
        ("RUGGEDCOM-POE-MIB", "rcPoeUndervoltageStatus"))
)
if mibBuilder.loadTexts:
    rcBasePoeStatusGroup.setStatus("current")

rcPoeTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2, 3)
)
rcPoeTableGroup.setObjects(
      *(("RUGGEDCOM-POE-MIB", "rcPoePort"),
        ("RUGGEDCOM-POE-MIB", "rcPoePortAdmin"),
        ("RUGGEDCOM-POE-MIB", "rcPoePortPowered"),
        ("RUGGEDCOM-POE-MIB", "rcPoePortClass"),
        ("RUGGEDCOM-POE-MIB", "rcPoePortVoltage"),
        ("RUGGEDCOM-POE-MIB", "rcPoePortCurrent"))
)
if mibBuilder.loadTexts:
    rcPoeTableGroup.setStatus("current")

rcPoeTablePriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2, 4)
)
rcPoeTablePriorityGroup.setObjects(
    ("RUGGEDCOM-POE-MIB", "rcPoePortPriority")
)
if mibBuilder.loadTexts:
    rcPoeTablePriorityGroup.setStatus("current")

rcPoeNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 7, 3, 2, 5)
)
rcPoeNotifyGroup.setObjects(
      *(("RUGGEDCOM-POE-MIB", "rcPoeOverheat"),
        ("RUGGEDCOM-POE-MIB", "rcPoeOverload"),
        ("RUGGEDCOM-POE-MIB", "rcPoeUndervoltage"))
)
if mibBuilder.loadTexts:
    rcPoeNotifyGroup.setStatus("current")


# Notification objects

rcPoeOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 12, 1)
)
if mibBuilder.loadTexts:
    rcPoeOverheat.setStatus(
        "current"
    )

rcPoeOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 12, 2)
)
if mibBuilder.loadTexts:
    rcPoeOverload.setStatus(
        "current"
    )

rcPoeUndervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 12, 3)
)
if mibBuilder.loadTexts:
    rcPoeUndervoltage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-POE-MIB",
    **{"rcPoe": rcPoe,
       "rcPoeBase": rcPoeBase,
       "rcPoeCapacity": rcPoeCapacity,
       "rcPoeMinimumVoltage": rcPoeMinimumVoltage,
       "rcPoeReenableTime": rcPoeReenableTime,
       "rcPoeConsumption": rcPoeConsumption,
       "rcPoeOverheatStatus": rcPoeOverheatStatus,
       "rcPoeOverloadStatus": rcPoeOverloadStatus,
       "rcPoeUndervoltageStatus": rcPoeUndervoltageStatus,
       "rcPoeTables": rcPoeTables,
       "rcPoePortTable": rcPoePortTable,
       "rcPoePortEntry": rcPoePortEntry,
       "rcPoePort": rcPoePort,
       "rcPoePortAdmin": rcPoePortAdmin,
       "rcPoePortPriority": rcPoePortPriority,
       "rcPoePortPowered": rcPoePortPowered,
       "rcPoePortClass": rcPoePortClass,
       "rcPoePortVoltage": rcPoePortVoltage,
       "rcPoePortCurrent": rcPoePortCurrent,
       "rcPoeConformance": rcPoeConformance,
       "rcPoeGroups": rcPoeGroups,
       "rcBasePoeGroup": rcBasePoeGroup,
       "rcBasePoeStatusGroup": rcBasePoeStatusGroup,
       "rcPoeTableGroup": rcPoeTableGroup,
       "rcPoeTablePriorityGroup": rcPoeTablePriorityGroup,
       "rcPoeNotifyGroup": rcPoeNotifyGroup,
       "ruggedcomPoeTraps": ruggedcomPoeTraps,
       "rcPoeOverheat": rcPoeOverheat,
       "rcPoeOverload": rcPoeOverload,
       "rcPoeUndervoltage": rcPoeUndervoltage}
)
