# SNMP MIB module (ELTEX-MES-ISS-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:51 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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

eltMesIssPoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11)
)
if mibBuilder.loadTexts:
    eltMesIssPoeMIB.setRevisions(
        ("2022-07-27 00:00",
         "2019-07-12 00:00",
         "2019-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssPoeInrushTestStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssPoeNotifications_ObjectIdentity = ObjectIdentity
eltMesIssPoeNotifications = _EltMesIssPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 0)
)
_EltMesIssPoeObjects_ObjectIdentity = ObjectIdentity
eltMesIssPoeObjects = _EltMesIssPoeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1)
)
_EltMesIssPoeGlobals_ObjectIdentity = ObjectIdentity
eltMesIssPoeGlobals = _EltMesIssPoeGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1)
)
_EltMesIssPoeGlobalConfigTable_Object = MibTable
eltMesIssPoeGlobalConfigTable = _EltMesIssPoeGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPoeGlobalConfigTable.setStatus("current")
_EltMesIssPoeGlobalConfigEntry_Object = MibTableRow
eltMesIssPoeGlobalConfigEntry = _EltMesIssPoeGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 1, 1)
)
eltMesIssPoeGlobalConfigEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoeGlobalConfigGroupIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssPoeGlobalConfigEntry.setStatus("current")


class _EltMesIssPoeGlobalConfigGroupIndex_Type(Integer32):
    """Custom type eltMesIssPoeGlobalConfigGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoeGlobalConfigGroupIndex_Type.__name__ = "Integer32"
_EltMesIssPoeGlobalConfigGroupIndex_Object = MibTableColumn
eltMesIssPoeGlobalConfigGroupIndex = _EltMesIssPoeGlobalConfigGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 1, 1, 1),
    _EltMesIssPoeGlobalConfigGroupIndex_Type()
)
eltMesIssPoeGlobalConfigGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoeGlobalConfigGroupIndex.setStatus("current")


class _EltMesIssPoeInrushTest_Type(EltMesIssPoeInrushTestStatus):
    """Custom type eltMesIssPoeInrushTest based on EltMesIssPoeInrushTestStatus"""
    defaultValue = 1


_EltMesIssPoeInrushTest_Type.__name__ = "EltMesIssPoeInrushTestStatus"
_EltMesIssPoeInrushTest_Object = MibTableColumn
eltMesIssPoeInrushTest = _EltMesIssPoeInrushTest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 1, 1, 2),
    _EltMesIssPoeInrushTest_Type()
)
eltMesIssPoeInrushTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPoeInrushTest.setStatus("current")


class _EltMesIssPoeAutoRestart_Type(TruthValue):
    """Custom type eltMesIssPoeAutoRestart based on TruthValue"""
    defaultValue = 1


_EltMesIssPoeAutoRestart_Type.__name__ = "TruthValue"
_EltMesIssPoeAutoRestart_Object = MibScalar
eltMesIssPoeAutoRestart = _EltMesIssPoeAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 2),
    _EltMesIssPoeAutoRestart_Type()
)
eltMesIssPoeAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPoeAutoRestart.setStatus("current")
_EltMesIssPoeRestartAction_Type = TruthValue
_EltMesIssPoeRestartAction_Object = MibScalar
eltMesIssPoeRestartAction = _EltMesIssPoeRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 1, 3),
    _EltMesIssPoeRestartAction_Type()
)
eltMesIssPoeRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPoeRestartAction.setStatus("current")
_EltMesIssPoeStatistics_ObjectIdentity = ObjectIdentity
eltMesIssPoeStatistics = _EltMesIssPoeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 2)
)
_EltMesIssPoeStatTable_Object = MibTable
eltMesIssPoeStatTable = _EltMesIssPoeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPoeStatTable.setStatus("current")
_EltMesIssPoeStatEntry_Object = MibTableRow
eltMesIssPoeStatEntry = _EltMesIssPoeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 2, 1, 1)
)
eltMesIssPoeStatEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoeStatGroupIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssPoeStatEntry.setStatus("current")


class _EltMesIssPoeStatGroupIndex_Type(Integer32):
    """Custom type eltMesIssPoeStatGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoeStatGroupIndex_Type.__name__ = "Integer32"
_EltMesIssPoeStatGroupIndex_Object = MibTableColumn
eltMesIssPoeStatGroupIndex = _EltMesIssPoeStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 2, 1, 1, 1),
    _EltMesIssPoeStatGroupIndex_Type()
)
eltMesIssPoeStatGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoeStatGroupIndex.setStatus("current")
_EltMesIssPoeTemperature_Type = Integer32
_EltMesIssPoeTemperature_Object = MibTableColumn
eltMesIssPoeTemperature = _EltMesIssPoeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 2, 1, 1, 2),
    _EltMesIssPoeTemperature_Type()
)
eltMesIssPoeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPoeTemperature.setStatus("current")
_EltMesIssPoePortConfig_ObjectIdentity = ObjectIdentity
eltMesIssPoePortConfig = _EltMesIssPoePortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3)
)
_EltMesIssPoePortConfigTable_Object = MibTable
eltMesIssPoePortConfigTable = _EltMesIssPoePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPoePortConfigTable.setStatus("current")
_EltMesIssPoePortConfigEntry_Object = MibTableRow
eltMesIssPoePortConfigEntry = _EltMesIssPoePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3, 1, 1)
)
eltMesIssPoePortConfigEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoePortConfigGroupIndex"),
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoePortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssPoePortConfigEntry.setStatus("current")


class _EltMesIssPoePortConfigGroupIndex_Type(Integer32):
    """Custom type eltMesIssPoePortConfigGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoePortConfigGroupIndex_Type.__name__ = "Integer32"
_EltMesIssPoePortConfigGroupIndex_Object = MibTableColumn
eltMesIssPoePortConfigGroupIndex = _EltMesIssPoePortConfigGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3, 1, 1, 1),
    _EltMesIssPoePortConfigGroupIndex_Type()
)
eltMesIssPoePortConfigGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoePortConfigGroupIndex.setStatus("current")


class _EltMesIssPoePortConfigIfIndex_Type(Integer32):
    """Custom type eltMesIssPoePortConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoePortConfigIfIndex_Type.__name__ = "Integer32"
_EltMesIssPoePortConfigIfIndex_Object = MibTableColumn
eltMesIssPoePortConfigIfIndex = _EltMesIssPoePortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3, 1, 1, 2),
    _EltMesIssPoePortConfigIfIndex_Type()
)
eltMesIssPoePortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoePortConfigIfIndex.setStatus("current")


class _EltMesIssPoePortMaxPowerLimit_Type(Integer32):
    """Custom type eltMesIssPoePortMaxPowerLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31200),
    )


_EltMesIssPoePortMaxPowerLimit_Type.__name__ = "Integer32"
_EltMesIssPoePortMaxPowerLimit_Object = MibTableColumn
eltMesIssPoePortMaxPowerLimit = _EltMesIssPoePortMaxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 3, 1, 1, 3),
    _EltMesIssPoePortMaxPowerLimit_Type()
)
eltMesIssPoePortMaxPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssPoePortMaxPowerLimit.setStatus("current")
_EltMesIssPoePortStatistics_ObjectIdentity = ObjectIdentity
eltMesIssPoePortStatistics = _EltMesIssPoePortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4)
)
_EltMesIssPoePortUtilTable_Object = MibTable
eltMesIssPoePortUtilTable = _EltMesIssPoePortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilTable.setStatus("current")
_EltMesIssPoePortUtilEntry_Object = MibTableRow
eltMesIssPoePortUtilEntry = _EltMesIssPoePortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1)
)
eltMesIssPoePortUtilEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoePortUtilGroupIndex"),
    (0, "ELTEX-MES-ISS-POE-MIB", "eltMesIssPoePortUtilIfIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilEntry.setStatus("current")


class _EltMesIssPoePortUtilGroupIndex_Type(Integer32):
    """Custom type eltMesIssPoePortUtilGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoePortUtilGroupIndex_Type.__name__ = "Integer32"
_EltMesIssPoePortUtilGroupIndex_Object = MibTableColumn
eltMesIssPoePortUtilGroupIndex = _EltMesIssPoePortUtilGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 1),
    _EltMesIssPoePortUtilGroupIndex_Type()
)
eltMesIssPoePortUtilGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilGroupIndex.setStatus("current")


class _EltMesIssPoePortUtilIfIndex_Type(Integer32):
    """Custom type eltMesIssPoePortUtilIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EltMesIssPoePortUtilIfIndex_Type.__name__ = "Integer32"
_EltMesIssPoePortUtilIfIndex_Object = MibTableColumn
eltMesIssPoePortUtilIfIndex = _EltMesIssPoePortUtilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 2),
    _EltMesIssPoePortUtilIfIndex_Type()
)
eltMesIssPoePortUtilIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilIfIndex.setStatus("current")
_EltMesIssPoePortUtilOutputVoltage_Type = Integer32
_EltMesIssPoePortUtilOutputVoltage_Object = MibTableColumn
eltMesIssPoePortUtilOutputVoltage = _EltMesIssPoePortUtilOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 3),
    _EltMesIssPoePortUtilOutputVoltage_Type()
)
eltMesIssPoePortUtilOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilOutputVoltage.setStatus("current")
_EltMesIssPoePortUtilOutputCurrent_Type = Integer32
_EltMesIssPoePortUtilOutputCurrent_Object = MibTableColumn
eltMesIssPoePortUtilOutputCurrent = _EltMesIssPoePortUtilOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 4),
    _EltMesIssPoePortUtilOutputCurrent_Type()
)
eltMesIssPoePortUtilOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilOutputCurrent.setStatus("current")
_EltMesIssPoePortUtilOutputPower_Type = Integer32
_EltMesIssPoePortUtilOutputPower_Object = MibTableColumn
eltMesIssPoePortUtilOutputPower = _EltMesIssPoePortUtilOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 5),
    _EltMesIssPoePortUtilOutputPower_Type()
)
eltMesIssPoePortUtilOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilOutputPower.setStatus("current")
_EltMesIssPoePortUtilMaxPower_Type = Integer32
_EltMesIssPoePortUtilMaxPower_Object = MibTableColumn
eltMesIssPoePortUtilMaxPower = _EltMesIssPoePortUtilMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11, 1, 4, 1, 1, 6),
    _EltMesIssPoePortUtilMaxPower_Type()
)
eltMesIssPoePortUtilMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssPoePortUtilMaxPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-POE-MIB",
    **{"EltMesIssPoeInrushTestStatus": EltMesIssPoeInrushTestStatus,
       "eltMesIssPoeMIB": eltMesIssPoeMIB,
       "eltMesIssPoeNotifications": eltMesIssPoeNotifications,
       "eltMesIssPoeObjects": eltMesIssPoeObjects,
       "eltMesIssPoeGlobals": eltMesIssPoeGlobals,
       "eltMesIssPoeGlobalConfigTable": eltMesIssPoeGlobalConfigTable,
       "eltMesIssPoeGlobalConfigEntry": eltMesIssPoeGlobalConfigEntry,
       "eltMesIssPoeGlobalConfigGroupIndex": eltMesIssPoeGlobalConfigGroupIndex,
       "eltMesIssPoeInrushTest": eltMesIssPoeInrushTest,
       "eltMesIssPoeAutoRestart": eltMesIssPoeAutoRestart,
       "eltMesIssPoeRestartAction": eltMesIssPoeRestartAction,
       "eltMesIssPoeStatistics": eltMesIssPoeStatistics,
       "eltMesIssPoeStatTable": eltMesIssPoeStatTable,
       "eltMesIssPoeStatEntry": eltMesIssPoeStatEntry,
       "eltMesIssPoeStatGroupIndex": eltMesIssPoeStatGroupIndex,
       "eltMesIssPoeTemperature": eltMesIssPoeTemperature,
       "eltMesIssPoePortConfig": eltMesIssPoePortConfig,
       "eltMesIssPoePortConfigTable": eltMesIssPoePortConfigTable,
       "eltMesIssPoePortConfigEntry": eltMesIssPoePortConfigEntry,
       "eltMesIssPoePortConfigGroupIndex": eltMesIssPoePortConfigGroupIndex,
       "eltMesIssPoePortConfigIfIndex": eltMesIssPoePortConfigIfIndex,
       "eltMesIssPoePortMaxPowerLimit": eltMesIssPoePortMaxPowerLimit,
       "eltMesIssPoePortStatistics": eltMesIssPoePortStatistics,
       "eltMesIssPoePortUtilTable": eltMesIssPoePortUtilTable,
       "eltMesIssPoePortUtilEntry": eltMesIssPoePortUtilEntry,
       "eltMesIssPoePortUtilGroupIndex": eltMesIssPoePortUtilGroupIndex,
       "eltMesIssPoePortUtilIfIndex": eltMesIssPoePortUtilIfIndex,
       "eltMesIssPoePortUtilOutputVoltage": eltMesIssPoePortUtilOutputVoltage,
       "eltMesIssPoePortUtilOutputCurrent": eltMesIssPoePortUtilOutputCurrent,
       "eltMesIssPoePortUtilOutputPower": eltMesIssPoePortUtilOutputPower,
       "eltMesIssPoePortUtilMaxPower": eltMesIssPoePortUtilMaxPower}
)
