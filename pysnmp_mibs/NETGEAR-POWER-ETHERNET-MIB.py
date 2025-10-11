# SNMP MIB module (NETGEAR-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-POWER-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:27:05 2025
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

(ng7000managedswitch,) = mibBuilder.importSymbols(
    "NETGEAR-REF-MIB",
    "ng7000managedswitch")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

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

fastPathpowerEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15)
)
if mibBuilder.loadTexts:
    fastPathpowerEthernetMIB.setRevisions(
        ("2018-03-02 00:00",
         "2018-01-25 00:00",
         "2015-03-13 00:00",
         "2014-04-16 00:00",
         "2011-01-26 00:00",
         "2007-08-19 12:00",
         "2007-05-23 00:00",
         "2003-11-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentPethObjects_ObjectIdentity = ObjectIdentity
agentPethObjects = _AgentPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1)
)
_AgentPethPsePortTable_Object = MibTable
agentPethPsePortTable = _AgentPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortTable.setStatus("current")
_AgentPethPsePortEntry_Object = MibTableRow
agentPethPsePortEntry = _AgentPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortEntry.setStatus("current")
_AgentPethPowerLimit_Type = Gauge32
_AgentPethPowerLimit_Object = MibTableColumn
agentPethPowerLimit = _AgentPethPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 1),
    _AgentPethPowerLimit_Type()
)
agentPethPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setUnits("Milliwatts")
_AgentPethOutputPower_Type = Gauge32
_AgentPethOutputPower_Object = MibTableColumn
agentPethOutputPower = _AgentPethOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 2),
    _AgentPethOutputPower_Type()
)
agentPethOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputPower.setUnits("Milliwatts")
_AgentPethOutputCurrent_Type = Gauge32
_AgentPethOutputCurrent_Object = MibTableColumn
agentPethOutputCurrent = _AgentPethOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 3),
    _AgentPethOutputCurrent_Type()
)
agentPethOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setUnits("Milliamps")
_AgentPethOutputVolts_Type = Gauge32
_AgentPethOutputVolts_Object = MibTableColumn
agentPethOutputVolts = _AgentPethOutputVolts_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 4),
    _AgentPethOutputVolts_Type()
)
agentPethOutputVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setUnits("Volts")
_AgentPethTemperature_Type = Gauge32
_AgentPethTemperature_Object = MibTableColumn
agentPethTemperature = _AgentPethTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 5),
    _AgentPethTemperature_Type()
)
agentPethTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethTemperature.setStatus("obsolete")
if mibBuilder.loadTexts:
    agentPethTemperature.setUnits("DEGREES")


class _AgentPethPowerLimitType_Type(Integer32):
    """Custom type agentPethPowerLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot3af", 1),
          ("user", 2),
          ("none", 3))
    )


_AgentPethPowerLimitType_Type.__name__ = "Integer32"
_AgentPethPowerLimitType_Object = MibTableColumn
agentPethPowerLimitType = _AgentPethPowerLimitType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 6),
    _AgentPethPowerLimitType_Type()
)
agentPethPowerLimitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerLimitType.setStatus("current")
_AgentPethHighPowerEnable_Type = TruthValue
_AgentPethHighPowerEnable_Object = MibTableColumn
agentPethHighPowerEnable = _AgentPethHighPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 7),
    _AgentPethHighPowerEnable_Type()
)
agentPethHighPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethHighPowerEnable.setStatus("current")


class _AgentPethPowerDetectionType_Type(Integer32):
    """Custom type agentPethPowerDetectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("legacy", 1),
          ("fourPtdot3afonly", 2),
          ("fourPtdot3afandlegacy", 3),
          ("twoPtdot3afonly", 4),
          ("twoPtdot3afandlegacy", 5))
    )


_AgentPethPowerDetectionType_Type.__name__ = "Integer32"
_AgentPethPowerDetectionType_Object = MibTableColumn
agentPethPowerDetectionType = _AgentPethPowerDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 8),
    _AgentPethPowerDetectionType_Type()
)
agentPethPowerDetectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerDetectionType.setStatus("current")


class _AgentPethFaultStatus_Type(Integer32):
    """Custom type agentPethFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mpsAbsent", 1),
          ("short", 2),
          ("overload", 3),
          ("powerDenied", 4),
          ("thermalShutdown", 5),
          ("startupFailure", 6))
    )


_AgentPethFaultStatus_Type.__name__ = "Integer32"
_AgentPethFaultStatus_Object = MibTableColumn
agentPethFaultStatus = _AgentPethFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 9),
    _AgentPethFaultStatus_Type()
)
agentPethFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethFaultStatus.setStatus("current")


class _AgentPethPortReset_Type(Integer32):
    """Custom type agentPethPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AgentPethPortReset_Type.__name__ = "Integer32"
_AgentPethPortReset_Object = MibTableColumn
agentPethPortReset = _AgentPethPortReset_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 10),
    _AgentPethPortReset_Type()
)
agentPethPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPortReset.setStatus("current")
_AgentPethPowerLimitMin_Type = Gauge32
_AgentPethPowerLimitMin_Object = MibTableColumn
agentPethPowerLimitMin = _AgentPethPowerLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 11),
    _AgentPethPowerLimitMin_Type()
)
agentPethPowerLimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPowerLimitMin.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPowerLimitMin.setUnits("Milliwatts")
_AgentPethPowerLimitMax_Type = Gauge32
_AgentPethPowerLimitMax_Object = MibTableColumn
agentPethPowerLimitMax = _AgentPethPowerLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 1, 1, 12),
    _AgentPethPowerLimitMax_Type()
)
agentPethPowerLimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPowerLimitMax.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPowerLimitMax.setUnits("Milliwatts")
_AgentPethMainPseObjects_ObjectIdentity = ObjectIdentity
agentPethMainPseObjects = _AgentPethMainPseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 2)
)
_AgentPethMainPseTable_Object = MibTable
agentPethMainPseTable = _AgentPethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentPethMainPseTable.setStatus("current")
_AgentPethMainPseEntry_Object = MibTableRow
agentPethMainPseEntry = _AgentPethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethMainPseEntry.setStatus("current")
_AgentPethMainPseLegacy_Type = TruthValue
_AgentPethMainPseLegacy_Object = MibTableColumn
agentPethMainPseLegacy = _AgentPethMainPseLegacy_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 2, 1, 1, 1),
    _AgentPethMainPseLegacy_Type()
)
agentPethMainPseLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethMainPseLegacy.setStatus("current")
_AgentPethPseTable_Object = MibTable
agentPethPseTable = _AgentPethPseTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 3)
)
if mibBuilder.loadTexts:
    agentPethPseTable.setStatus("current")
_AgentPethPseEntry_Object = MibTableRow
agentPethPseEntry = _AgentPethPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agentPethPseEntry.setStatus("current")


class _AgentPethPsePowerManagementMode_Type(Integer32):
    """Custom type agentPethPsePowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_AgentPethPsePowerManagementMode_Type.__name__ = "Integer32"
_AgentPethPsePowerManagementMode_Object = MibTableColumn
agentPethPsePowerManagementMode = _AgentPethPsePowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 3, 1, 1),
    _AgentPethPsePowerManagementMode_Type()
)
agentPethPsePowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPsePowerManagementMode.setStatus("current")
_AgentPethPseThresholdPower_Type = Gauge32
_AgentPethPseThresholdPower_Object = MibTableColumn
agentPethPseThresholdPower = _AgentPethPseThresholdPower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 3, 1, 6),
    _AgentPethPseThresholdPower_Type()
)
agentPethPseThresholdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPseThresholdPower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPseThresholdPower.setUnits("Watts")
_AgentPethPoeMainPseObjects_ObjectIdentity = ObjectIdentity
agentPethPoeMainPseObjects = _AgentPethPoeMainPseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4)
)
_AgentPethPoeMainPseTable_Object = MibTable
agentPethPoeMainPseTable = _AgentPethPoeMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    agentPethPoeMainPseTable.setStatus("current")
_AgentPethPoeMainPseEntry_Object = MibTableRow
agentPethPoeMainPseEntry = _AgentPethPoeMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1)
)
agentPethPoeMainPseEntry.setIndexNames(
    (0, "NETGEAR-POWER-ETHERNET-MIB", "agentPethPoeMainPseGroupIndex"),
    (0, "NETGEAR-POWER-ETHERNET-MIB", "agentPethPoeMainPseSlotIndex"),
)
if mibBuilder.loadTexts:
    agentPethPoeMainPseEntry.setStatus("current")


class _AgentPethPoeMainPseGroupIndex_Type(Integer32):
    """Custom type agentPethPoeMainPseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentPethPoeMainPseGroupIndex_Type.__name__ = "Integer32"
_AgentPethPoeMainPseGroupIndex_Object = MibTableColumn
agentPethPoeMainPseGroupIndex = _AgentPethPoeMainPseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 1),
    _AgentPethPoeMainPseGroupIndex_Type()
)
agentPethPoeMainPseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPethPoeMainPseGroupIndex.setStatus("current")


class _AgentPethPoeMainPseSlotIndex_Type(Integer32):
    """Custom type agentPethPoeMainPseSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentPethPoeMainPseSlotIndex_Type.__name__ = "Integer32"
_AgentPethPoeMainPseSlotIndex_Object = MibTableColumn
agentPethPoeMainPseSlotIndex = _AgentPethPoeMainPseSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 2),
    _AgentPethPoeMainPseSlotIndex_Type()
)
agentPethPoeMainPseSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentPethPoeMainPseSlotIndex.setStatus("current")


class _AgentPethPoeMainPsePower_Type(Gauge32):
    """Custom type agentPethPoeMainPsePower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPethPoeMainPsePower_Type.__name__ = "Gauge32"
_AgentPethPoeMainPsePower_Object = MibTableColumn
agentPethPoeMainPsePower = _AgentPethPoeMainPsePower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 3),
    _AgentPethPoeMainPsePower_Type()
)
agentPethPoeMainPsePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoeMainPsePower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPoeMainPsePower.setUnits("Watts")


class _AgentPethPoeMainPseOperStatus_Type(Integer32):
    """Custom type agentPethPoeMainPseOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("faulty", 3))
    )


_AgentPethPoeMainPseOperStatus_Type.__name__ = "Integer32"
_AgentPethPoeMainPseOperStatus_Object = MibTableColumn
agentPethPoeMainPseOperStatus = _AgentPethPoeMainPseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 4),
    _AgentPethPoeMainPseOperStatus_Type()
)
agentPethPoeMainPseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoeMainPseOperStatus.setStatus("current")
_AgentPethPoeMainPseThresholdPower_Type = Gauge32
_AgentPethPoeMainPseThresholdPower_Object = MibTableColumn
agentPethPoeMainPseThresholdPower = _AgentPethPoeMainPseThresholdPower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 5),
    _AgentPethPoeMainPseThresholdPower_Type()
)
agentPethPoeMainPseThresholdPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoeMainPseThresholdPower.setStatus("deprecated")
if mibBuilder.loadTexts:
    agentPethPoeMainPseThresholdPower.setUnits("Watts")
_AgentPethPoeMainPseConsumptionPower_Type = Gauge32
_AgentPethPoeMainPseConsumptionPower_Object = MibTableColumn
agentPethPoeMainPseConsumptionPower = _AgentPethPoeMainPseConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 6),
    _AgentPethPoeMainPseConsumptionPower_Type()
)
agentPethPoeMainPseConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoeMainPseConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPoeMainPseConsumptionPower.setUnits("Milliwatts")


class _AgentPethPoeMainPseUsageThreshold_Type(Integer32):
    """Custom type agentPethPoeMainPseUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AgentPethPoeMainPseUsageThreshold_Type.__name__ = "Integer32"
_AgentPethPoeMainPseUsageThreshold_Object = MibTableColumn
agentPethPoeMainPseUsageThreshold = _AgentPethPoeMainPseUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 7),
    _AgentPethPoeMainPseUsageThreshold_Type()
)
agentPethPoeMainPseUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPoeMainPseUsageThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    agentPethPoeMainPseUsageThreshold.setUnits("%")


class _AgentPethPoeMainPseFWImageVersion_Type(OctetString):
    """Custom type agentPethPoeMainPseFWImageVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_AgentPethPoeMainPseFWImageVersion_Type.__name__ = "OctetString"
_AgentPethPoeMainPseFWImageVersion_Object = MibTableColumn
agentPethPoeMainPseFWImageVersion = _AgentPethPoeMainPseFWImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 8),
    _AgentPethPoeMainPseFWImageVersion_Type()
)
agentPethPoeMainPseFWImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoeMainPseFWImageVersion.setStatus("current")


class _AgentPethPoePsePowerManagementMode_Type(Integer32):
    """Custom type agentPethPoePsePowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_AgentPethPoePsePowerManagementMode_Type.__name__ = "Integer32"
_AgentPethPoePsePowerManagementMode_Object = MibTableColumn
agentPethPoePsePowerManagementMode = _AgentPethPoePsePowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 9),
    _AgentPethPoePsePowerManagementMode_Type()
)
agentPethPoePsePowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPoePsePowerManagementMode.setStatus("current")


class _AgentPethPoePseCardModel_Type(DisplayString):
    """Custom type agentPethPoePseCardModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentPethPoePseCardModel_Type.__name__ = "DisplayString"
_AgentPethPoePseCardModel_Object = MibTableColumn
agentPethPoePseCardModel = _AgentPethPoePseCardModel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 10),
    _AgentPethPoePseCardModel_Type()
)
agentPethPoePseCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoePseCardModel.setStatus("current")


class _AgentPethPoePseCardHost_Type(DisplayString):
    """Custom type agentPethPoePseCardHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentPethPoePseCardHost_Type.__name__ = "DisplayString"
_AgentPethPoePseCardHost_Object = MibTableColumn
agentPethPoePseCardHost = _AgentPethPoePseCardHost_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 11),
    _AgentPethPoePseCardHost_Type()
)
agentPethPoePseCardHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoePseCardHost.setStatus("current")


class _AgentPethPoePseCardStatus_Type(Integer32):
    """Custom type agentPethPoePseCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent-or-failed", 0),
          ("running", 1))
    )


_AgentPethPoePseCardStatus_Type.__name__ = "Integer32"
_AgentPethPoePseCardStatus_Object = MibTableColumn
agentPethPoePseCardStatus = _AgentPethPoePseCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 15, 1, 4, 1, 1, 12),
    _AgentPethPoePseCardStatus_Type()
)
agentPethPoePseCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethPoePseCardStatus.setStatus("current")
pethPsePortEntry.registerAugmentions(
    ("NETGEAR-POWER-ETHERNET-MIB",
     "agentPethPsePortEntry")
)
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("NETGEAR-POWER-ETHERNET-MIB",
     "agentPethMainPseEntry")
)
agentPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("NETGEAR-POWER-ETHERNET-MIB",
     "agentPethPseEntry")
)
agentPethPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-POWER-ETHERNET-MIB",
    **{"fastPathpowerEthernetMIB": fastPathpowerEthernetMIB,
       "agentPethObjects": agentPethObjects,
       "agentPethPsePortTable": agentPethPsePortTable,
       "agentPethPsePortEntry": agentPethPsePortEntry,
       "agentPethPowerLimit": agentPethPowerLimit,
       "agentPethOutputPower": agentPethOutputPower,
       "agentPethOutputCurrent": agentPethOutputCurrent,
       "agentPethOutputVolts": agentPethOutputVolts,
       "agentPethTemperature": agentPethTemperature,
       "agentPethPowerLimitType": agentPethPowerLimitType,
       "agentPethHighPowerEnable": agentPethHighPowerEnable,
       "agentPethPowerDetectionType": agentPethPowerDetectionType,
       "agentPethFaultStatus": agentPethFaultStatus,
       "agentPethPortReset": agentPethPortReset,
       "agentPethPowerLimitMin": agentPethPowerLimitMin,
       "agentPethPowerLimitMax": agentPethPowerLimitMax,
       "agentPethMainPseObjects": agentPethMainPseObjects,
       "agentPethMainPseTable": agentPethMainPseTable,
       "agentPethMainPseEntry": agentPethMainPseEntry,
       "agentPethMainPseLegacy": agentPethMainPseLegacy,
       "agentPethPseTable": agentPethPseTable,
       "agentPethPseEntry": agentPethPseEntry,
       "agentPethPsePowerManagementMode": agentPethPsePowerManagementMode,
       "agentPethPseThresholdPower": agentPethPseThresholdPower,
       "agentPethPoeMainPseObjects": agentPethPoeMainPseObjects,
       "agentPethPoeMainPseTable": agentPethPoeMainPseTable,
       "agentPethPoeMainPseEntry": agentPethPoeMainPseEntry,
       "agentPethPoeMainPseGroupIndex": agentPethPoeMainPseGroupIndex,
       "agentPethPoeMainPseSlotIndex": agentPethPoeMainPseSlotIndex,
       "agentPethPoeMainPsePower": agentPethPoeMainPsePower,
       "agentPethPoeMainPseOperStatus": agentPethPoeMainPseOperStatus,
       "agentPethPoeMainPseThresholdPower": agentPethPoeMainPseThresholdPower,
       "agentPethPoeMainPseConsumptionPower": agentPethPoeMainPseConsumptionPower,
       "agentPethPoeMainPseUsageThreshold": agentPethPoeMainPseUsageThreshold,
       "agentPethPoeMainPseFWImageVersion": agentPethPoeMainPseFWImageVersion,
       "agentPethPoePsePowerManagementMode": agentPethPoePsePowerManagementMode,
       "agentPethPoePseCardModel": agentPethPoePseCardModel,
       "agentPethPoePseCardHost": agentPethPoePseCardHost,
       "agentPethPoePseCardStatus": agentPethPoePseCardStatus}
)
