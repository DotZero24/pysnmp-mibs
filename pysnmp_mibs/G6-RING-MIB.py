# SNMP MIB module (G6-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-RING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:11 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ring_ObjectIdentity = ObjectIdentity
ring = _Ring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45)
)
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1)
)
configEntry.setIndexNames(
    (0, "G6-RING-MIB", "configIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigIndex_Type(Integer32):
    """Custom type configIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigIndex_Type.__name__ = "Integer32"
_ConfigIndex_Object = MibTableColumn
configIndex = _ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 1),
    _ConfigIndex_Type()
)
configIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configIndex.setStatus("current")
_ConfigName_Type = DisplayString
_ConfigName_Object = MibTableColumn
configName = _ConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 2),
    _ConfigName_Type()
)
configName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configName.setStatus("current")


class _ConfigEnableRing_Type(Integer32):
    """Custom type configEnableRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableRing_Type.__name__ = "Integer32"
_ConfigEnableRing_Object = MibTableColumn
configEnableRing = _ConfigEnableRing_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 3),
    _ConfigEnableRing_Type()
)
configEnableRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableRing.setStatus("current")


class _ConfigRingMaster_Type(Integer32):
    """Custom type configRingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigRingMaster_Type.__name__ = "Integer32"
_ConfigRingMaster_Object = MibTableColumn
configRingMaster = _ConfigRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 4),
    _ConfigRingMaster_Type()
)
configRingMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRingMaster.setStatus("current")


class _ConfigNumber_Type(Integer32):
    """Custom type configNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigNumber_Type.__name__ = "Integer32"
_ConfigNumber_Object = MibTableColumn
configNumber = _ConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 5),
    _ConfigNumber_Type()
)
configNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNumber.setStatus("current")


class _ConfigPortA_Type(Integer32):
    """Custom type configPortA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigPortA_Type.__name__ = "Integer32"
_ConfigPortA_Object = MibTableColumn
configPortA = _ConfigPortA_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 6),
    _ConfigPortA_Type()
)
configPortA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortA.setStatus("current")


class _ConfigPortB_Type(Integer32):
    """Custom type configPortB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigPortB_Type.__name__ = "Integer32"
_ConfigPortB_Object = MibTableColumn
configPortB = _ConfigPortB_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 1, 1, 7),
    _ConfigPortB_Type()
)
configPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortB.setStatus("current")
_MrpConfigTable_Object = MibTable
mrpConfigTable = _MrpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2)
)
if mibBuilder.loadTexts:
    mrpConfigTable.setStatus("current")
_MrpConfigEntry_Object = MibTableRow
mrpConfigEntry = _MrpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1)
)
mrpConfigEntry.setIndexNames(
    (0, "G6-RING-MIB", "mrpConfigIndex"),
)
if mibBuilder.loadTexts:
    mrpConfigEntry.setStatus("current")


class _MrpConfigIndex_Type(Integer32):
    """Custom type mrpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MrpConfigIndex_Type.__name__ = "Integer32"
_MrpConfigIndex_Object = MibTableColumn
mrpConfigIndex = _MrpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 1),
    _MrpConfigIndex_Type()
)
mrpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mrpConfigIndex.setStatus("current")


class _MrpConfigEnableMrp_Type(Integer32):
    """Custom type mrpConfigEnableMrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MrpConfigEnableMrp_Type.__name__ = "Integer32"
_MrpConfigEnableMrp_Object = MibTableColumn
mrpConfigEnableMrp = _MrpConfigEnableMrp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 2),
    _MrpConfigEnableMrp_Type()
)
mrpConfigEnableMrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigEnableMrp.setStatus("current")
_MrpConfigDomainName_Type = DisplayString
_MrpConfigDomainName_Object = MibTableColumn
mrpConfigDomainName = _MrpConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 3),
    _MrpConfigDomainName_Type()
)
mrpConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigDomainName.setStatus("current")


class _MrpConfigExpectedRole_Type(Integer32):
    """Custom type mrpConfigExpectedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client", 0),
          ("manager", 1))
    )


_MrpConfigExpectedRole_Type.__name__ = "Integer32"
_MrpConfigExpectedRole_Object = MibTableColumn
mrpConfigExpectedRole = _MrpConfigExpectedRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 4),
    _MrpConfigExpectedRole_Type()
)
mrpConfigExpectedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigExpectedRole.setStatus("current")


class _MrpConfigReactOnLinkChange_Type(Integer32):
    """Custom type mrpConfigReactOnLinkChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MrpConfigReactOnLinkChange_Type.__name__ = "Integer32"
_MrpConfigReactOnLinkChange_Object = MibTableColumn
mrpConfigReactOnLinkChange = _MrpConfigReactOnLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 5),
    _MrpConfigReactOnLinkChange_Type()
)
mrpConfigReactOnLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigReactOnLinkChange.setStatus("current")


class _MrpConfigRecoveryTime_Type(Integer32):
    """Custom type mrpConfigRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("recoveryTime500Ms", 0),
          ("recoveryTime200Ms", 1))
    )


_MrpConfigRecoveryTime_Type.__name__ = "Integer32"
_MrpConfigRecoveryTime_Object = MibTableColumn
mrpConfigRecoveryTime = _MrpConfigRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 6),
    _MrpConfigRecoveryTime_Type()
)
mrpConfigRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigRecoveryTime.setStatus("current")


class _MrpConfigPort1_Type(Integer32):
    """Custom type mrpConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MrpConfigPort1_Type.__name__ = "Integer32"
_MrpConfigPort1_Object = MibTableColumn
mrpConfigPort1 = _MrpConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 7),
    _MrpConfigPort1_Type()
)
mrpConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigPort1.setStatus("current")


class _MrpConfigPort2_Type(Integer32):
    """Custom type mrpConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MrpConfigPort2_Type.__name__ = "Integer32"
_MrpConfigPort2_Object = MibTableColumn
mrpConfigPort2 = _MrpConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 8),
    _MrpConfigPort2_Type()
)
mrpConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigPort2.setStatus("current")


class _MrpConfigVlanId_Type(Integer32):
    """Custom type mrpConfigVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MrpConfigVlanId_Type.__name__ = "Integer32"
_MrpConfigVlanId_Object = MibTableColumn
mrpConfigVlanId = _MrpConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 9),
    _MrpConfigVlanId_Type()
)
mrpConfigVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigVlanId.setStatus("current")
_MrpConfigResetRoundTripDelays_Type = DisplayString
_MrpConfigResetRoundTripDelays_Object = MibTableColumn
mrpConfigResetRoundTripDelays = _MrpConfigResetRoundTripDelays_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 10),
    _MrpConfigResetRoundTripDelays_Type()
)
mrpConfigResetRoundTripDelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigResetRoundTripDelays.setStatus("current")
_MrpConfigResetStatistics_Type = DisplayString
_MrpConfigResetStatistics_Object = MibTableColumn
mrpConfigResetStatistics = _MrpConfigResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 2, 1, 11),
    _MrpConfigResetStatistics_Type()
)
mrpConfigResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrpConfigResetStatistics.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1)
)
statusEntry.setIndexNames(
    (0, "G6-RING-MIB", "statusIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusIndex_Type(Integer32):
    """Custom type statusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_StatusIndex_Type.__name__ = "Integer32"
_StatusIndex_Object = MibTableColumn
statusIndex = _StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 1),
    _StatusIndex_Type()
)
statusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusIndex.setStatus("current")


class _StatusState_Type(Integer32):
    """Custom type statusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("normal", 1),
          ("backup", 2),
          ("error", 3),
          ("misconfigured", 4))
    )


_StatusState_Type.__name__ = "Integer32"
_StatusState_Object = MibTableColumn
statusState = _StatusState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 2),
    _StatusState_Type()
)
statusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusState.setStatus("current")
_StatusLastStateChange_Type = DisplayString
_StatusLastStateChange_Object = MibTableColumn
statusLastStateChange = _StatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 3),
    _StatusLastStateChange_Type()
)
statusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLastStateChange.setStatus("current")


class _StatusRingInterrupt_Type(Integer32):
    """Custom type statusRingInterrupt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusRingInterrupt_Type.__name__ = "Integer32"
_StatusRingInterrupt_Object = MibTableColumn
statusRingInterrupt = _StatusRingInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 4),
    _StatusRingInterrupt_Type()
)
statusRingInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRingInterrupt.setStatus("current")


class _StatusGlobalRingAlarm_Type(Integer32):
    """Custom type statusGlobalRingAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusGlobalRingAlarm_Type.__name__ = "Integer32"
_StatusGlobalRingAlarm_Object = MibTableColumn
statusGlobalRingAlarm = _StatusGlobalRingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 5),
    _StatusGlobalRingAlarm_Type()
)
statusGlobalRingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusGlobalRingAlarm.setStatus("current")


class _StatusErrorDetected_Type(Integer32):
    """Custom type statusErrorDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusErrorDetected_Type.__name__ = "Integer32"
_StatusErrorDetected_Object = MibTableColumn
statusErrorDetected = _StatusErrorDetected_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 6),
    _StatusErrorDetected_Type()
)
statusErrorDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusErrorDetected.setStatus("current")


class _StatusRingPortAInterrupted_Type(Integer32):
    """Custom type statusRingPortAInterrupted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusRingPortAInterrupted_Type.__name__ = "Integer32"
_StatusRingPortAInterrupted_Object = MibTableColumn
statusRingPortAInterrupted = _StatusRingPortAInterrupted_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 7),
    _StatusRingPortAInterrupted_Type()
)
statusRingPortAInterrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRingPortAInterrupted.setStatus("current")


class _StatusRingPortBInterrupted_Type(Integer32):
    """Custom type statusRingPortBInterrupted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusRingPortBInterrupted_Type.__name__ = "Integer32"
_StatusRingPortBInterrupted_Object = MibTableColumn
statusRingPortBInterrupted = _StatusRingPortBInterrupted_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 100, 1, 8),
    _StatusRingPortBInterrupted_Type()
)
statusRingPortBInterrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRingPortBInterrupted.setStatus("current")
_StatisticsTable_Object = MibTable
statisticsTable = _StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101)
)
if mibBuilder.loadTexts:
    statisticsTable.setStatus("current")
_StatisticsEntry_Object = MibTableRow
statisticsEntry = _StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1)
)
statisticsEntry.setIndexNames(
    (0, "G6-RING-MIB", "statisticsIndex"),
)
if mibBuilder.loadTexts:
    statisticsEntry.setStatus("current")


class _StatisticsIndex_Type(Integer32):
    """Custom type statisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_StatisticsIndex_Type.__name__ = "Integer32"
_StatisticsIndex_Object = MibTableColumn
statisticsIndex = _StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1, 1),
    _StatisticsIndex_Type()
)
statisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statisticsIndex.setStatus("current")
_StatisticsNumberOfBackups_Type = Unsigned32
_StatisticsNumberOfBackups_Object = MibTableColumn
statisticsNumberOfBackups = _StatisticsNumberOfBackups_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1, 2),
    _StatisticsNumberOfBackups_Type()
)
statisticsNumberOfBackups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsNumberOfBackups.setStatus("current")
_StatisticsCurrentBackupDuration_Type = Counter32
_StatisticsCurrentBackupDuration_Object = MibTableColumn
statisticsCurrentBackupDuration = _StatisticsCurrentBackupDuration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1, 3),
    _StatisticsCurrentBackupDuration_Type()
)
statisticsCurrentBackupDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsCurrentBackupDuration.setStatus("current")
_StatisticsLastBackupDuration_Type = Counter32
_StatisticsLastBackupDuration_Object = MibTableColumn
statisticsLastBackupDuration = _StatisticsLastBackupDuration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1, 4),
    _StatisticsLastBackupDuration_Type()
)
statisticsLastBackupDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsLastBackupDuration.setStatus("current")
_StatisticsTotalBackupDuration_Type = Counter32
_StatisticsTotalBackupDuration_Object = MibTableColumn
statisticsTotalBackupDuration = _StatisticsTotalBackupDuration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 101, 1, 5),
    _StatisticsTotalBackupDuration_Type()
)
statisticsTotalBackupDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsTotalBackupDuration.setStatus("current")
_CouplingStatusTable_Object = MibTable
couplingStatusTable = _CouplingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102)
)
if mibBuilder.loadTexts:
    couplingStatusTable.setStatus("current")
_CouplingStatusEntry_Object = MibTableRow
couplingStatusEntry = _CouplingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1)
)
couplingStatusEntry.setIndexNames(
    (0, "G6-RING-MIB", "couplingStatusIndex"),
)
if mibBuilder.loadTexts:
    couplingStatusEntry.setStatus("current")


class _CouplingStatusIndex_Type(Integer32):
    """Custom type couplingStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_CouplingStatusIndex_Type.__name__ = "Integer32"
_CouplingStatusIndex_Object = MibTableColumn
couplingStatusIndex = _CouplingStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 1),
    _CouplingStatusIndex_Type()
)
couplingStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    couplingStatusIndex.setStatus("current")


class _CouplingStatusControllerState_Type(Integer32):
    """Custom type couplingStatusControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("blocking", 1),
          ("link", 2),
          ("forwarding", 3),
          ("standby", 4))
    )


_CouplingStatusControllerState_Type.__name__ = "Integer32"
_CouplingStatusControllerState_Object = MibTableColumn
couplingStatusControllerState = _CouplingStatusControllerState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 2),
    _CouplingStatusControllerState_Type()
)
couplingStatusControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusControllerState.setStatus("current")


class _CouplingStatusCportLink_Type(Integer32):
    """Custom type couplingStatusCportLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusCportLink_Type.__name__ = "Integer32"
_CouplingStatusCportLink_Object = MibTableColumn
couplingStatusCportLink = _CouplingStatusCportLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 3),
    _CouplingStatusCportLink_Type()
)
couplingStatusCportLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusCportLink.setStatus("current")


class _CouplingStatusCportForward_Type(Integer32):
    """Custom type couplingStatusCportForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusCportForward_Type.__name__ = "Integer32"
_CouplingStatusCportForward_Object = MibTableColumn
couplingStatusCportForward = _CouplingStatusCportForward_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 4),
    _CouplingStatusCportForward_Type()
)
couplingStatusCportForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusCportForward.setStatus("current")


class _CouplingStatusCportTimeout_Type(Integer32):
    """Custom type couplingStatusCportTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusCportTimeout_Type.__name__ = "Integer32"
_CouplingStatusCportTimeout_Object = MibTableColumn
couplingStatusCportTimeout = _CouplingStatusCportTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 5),
    _CouplingStatusCportTimeout_Type()
)
couplingStatusCportTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusCportTimeout.setStatus("current")


class _CouplingStatusConnectionValid_Type(Integer32):
    """Custom type couplingStatusConnectionValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusConnectionValid_Type.__name__ = "Integer32"
_CouplingStatusConnectionValid_Object = MibTableColumn
couplingStatusConnectionValid = _CouplingStatusConnectionValid_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 6),
    _CouplingStatusConnectionValid_Type()
)
couplingStatusConnectionValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusConnectionValid.setStatus("current")


class _CouplingStatusValidPartnerIp_Type(Integer32):
    """Custom type couplingStatusValidPartnerIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusValidPartnerIp_Type.__name__ = "Integer32"
_CouplingStatusValidPartnerIp_Object = MibTableColumn
couplingStatusValidPartnerIp = _CouplingStatusValidPartnerIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 7),
    _CouplingStatusValidPartnerIp_Type()
)
couplingStatusValidPartnerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusValidPartnerIp.setStatus("current")


class _CouplingStatusValidPartnerId_Type(Integer32):
    """Custom type couplingStatusValidPartnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CouplingStatusValidPartnerId_Type.__name__ = "Integer32"
_CouplingStatusValidPartnerId_Object = MibTableColumn
couplingStatusValidPartnerId = _CouplingStatusValidPartnerId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 102, 1, 8),
    _CouplingStatusValidPartnerId_Type()
)
couplingStatusValidPartnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    couplingStatusValidPartnerId.setStatus("current")
_MrpStatusTable_Object = MibTable
mrpStatusTable = _MrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103)
)
if mibBuilder.loadTexts:
    mrpStatusTable.setStatus("current")
_MrpStatusEntry_Object = MibTableRow
mrpStatusEntry = _MrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1)
)
mrpStatusEntry.setIndexNames(
    (0, "G6-RING-MIB", "mrpStatusIndex"),
)
if mibBuilder.loadTexts:
    mrpStatusEntry.setStatus("current")


class _MrpStatusIndex_Type(Integer32):
    """Custom type mrpStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MrpStatusIndex_Type.__name__ = "Integer32"
_MrpStatusIndex_Object = MibTableColumn
mrpStatusIndex = _MrpStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 1),
    _MrpStatusIndex_Type()
)
mrpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mrpStatusIndex.setStatus("current")


class _MrpStatusAdminRole_Type(Integer32):
    """Custom type mrpStatusAdminRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("client", 1),
          ("manager", 2))
    )


_MrpStatusAdminRole_Type.__name__ = "Integer32"
_MrpStatusAdminRole_Object = MibTableColumn
mrpStatusAdminRole = _MrpStatusAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 2),
    _MrpStatusAdminRole_Type()
)
mrpStatusAdminRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusAdminRole.setStatus("current")


class _MrpStatusOperationalRole_Type(Integer32):
    """Custom type mrpStatusOperationalRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("client", 1),
          ("manager", 2))
    )


_MrpStatusOperationalRole_Type.__name__ = "Integer32"
_MrpStatusOperationalRole_Object = MibTableColumn
mrpStatusOperationalRole = _MrpStatusOperationalRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 3),
    _MrpStatusOperationalRole_Type()
)
mrpStatusOperationalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusOperationalRole.setStatus("current")


class _MrpStatusPortAState_Type(Integer32):
    """Custom type mrpStatusPortAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("blocking", 1),
          ("forwarding", 3),
          ("notConnected", 4))
    )


_MrpStatusPortAState_Type.__name__ = "Integer32"
_MrpStatusPortAState_Object = MibTableColumn
mrpStatusPortAState = _MrpStatusPortAState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 4),
    _MrpStatusPortAState_Type()
)
mrpStatusPortAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusPortAState.setStatus("current")


class _MrpStatusPortBState_Type(Integer32):
    """Custom type mrpStatusPortBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("blocking", 1),
          ("forwarding", 3),
          ("notConnected", 4))
    )


_MrpStatusPortBState_Type.__name__ = "Integer32"
_MrpStatusPortBState_Object = MibTableColumn
mrpStatusPortBState = _MrpStatusPortBState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 5),
    _MrpStatusPortBState_Type()
)
mrpStatusPortBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusPortBState.setStatus("current")
_MrpStatusDomainId_Type = DisplayString
_MrpStatusDomainId_Object = MibTableColumn
mrpStatusDomainId = _MrpStatusDomainId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 6),
    _MrpStatusDomainId_Type()
)
mrpStatusDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusDomainId.setStatus("current")


class _MrpStatusDomainState_Type(Integer32):
    """Custom type mrpStatusDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ok", 1),
          ("ringOpen", 2))
    )


_MrpStatusDomainState_Type.__name__ = "Integer32"
_MrpStatusDomainState_Object = MibTableColumn
mrpStatusDomainState = _MrpStatusDomainState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 7),
    _MrpStatusDomainState_Type()
)
mrpStatusDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusDomainState.setStatus("current")


class _MrpStatusDomainError_Type(Integer32):
    """Custom type mrpStatusDomainError based on Integer32"""
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
        *(("disabled", 0),
          ("noError", 1),
          ("invalidVlan", 2),
          ("invalid", 3),
          ("multiMgr", 4),
          ("singleSide", 5),
          ("linkError", 6))
    )


_MrpStatusDomainError_Type.__name__ = "Integer32"
_MrpStatusDomainError_Object = MibTableColumn
mrpStatusDomainError = _MrpStatusDomainError_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 8),
    _MrpStatusDomainError_Type()
)
mrpStatusDomainError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusDomainError.setStatus("current")


class _MrpStatusDomainBlocked_Type(Integer32):
    """Custom type mrpStatusDomainBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MrpStatusDomainBlocked_Type.__name__ = "Integer32"
_MrpStatusDomainBlocked_Object = MibTableColumn
mrpStatusDomainBlocked = _MrpStatusDomainBlocked_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 9),
    _MrpStatusDomainBlocked_Type()
)
mrpStatusDomainBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusDomainBlocked.setStatus("current")
_MrpStatusManagerPriority_Type = Unsigned32
_MrpStatusManagerPriority_Object = MibTableColumn
mrpStatusManagerPriority = _MrpStatusManagerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 10),
    _MrpStatusManagerPriority_Type()
)
mrpStatusManagerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusManagerPriority.setStatus("current")
_MrpStatusRingOpenCount_Type = Unsigned32
_MrpStatusRingOpenCount_Object = MibTableColumn
mrpStatusRingOpenCount = _MrpStatusRingOpenCount_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 11),
    _MrpStatusRingOpenCount_Type()
)
mrpStatusRingOpenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusRingOpenCount.setStatus("current")
_MrpStatusLastRingOpenTimeStamp_Type = Counter32
_MrpStatusLastRingOpenTimeStamp_Object = MibTableColumn
mrpStatusLastRingOpenTimeStamp = _MrpStatusLastRingOpenTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 12),
    _MrpStatusLastRingOpenTimeStamp_Type()
)
mrpStatusLastRingOpenTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusLastRingOpenTimeStamp.setStatus("current")
_MrpStatusMaxRoundTripDelay_Type = Unsigned32
_MrpStatusMaxRoundTripDelay_Object = MibTableColumn
mrpStatusMaxRoundTripDelay = _MrpStatusMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 13),
    _MrpStatusMaxRoundTripDelay_Type()
)
mrpStatusMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusMaxRoundTripDelay.setStatus("current")
_MrpStatusMinRoundTripDelay_Type = Unsigned32
_MrpStatusMinRoundTripDelay_Object = MibTableColumn
mrpStatusMinRoundTripDelay = _MrpStatusMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 45, 103, 1, 14),
    _MrpStatusMinRoundTripDelay_Type()
)
mrpStatusMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrpStatusMinRoundTripDelay.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-RING-MIB",
    **{"protocol": protocol,
       "ring": ring,
       "configTable": configTable,
       "configEntry": configEntry,
       "configIndex": configIndex,
       "configName": configName,
       "configEnableRing": configEnableRing,
       "configRingMaster": configRingMaster,
       "configNumber": configNumber,
       "configPortA": configPortA,
       "configPortB": configPortB,
       "mrpConfigTable": mrpConfigTable,
       "mrpConfigEntry": mrpConfigEntry,
       "mrpConfigIndex": mrpConfigIndex,
       "mrpConfigEnableMrp": mrpConfigEnableMrp,
       "mrpConfigDomainName": mrpConfigDomainName,
       "mrpConfigExpectedRole": mrpConfigExpectedRole,
       "mrpConfigReactOnLinkChange": mrpConfigReactOnLinkChange,
       "mrpConfigRecoveryTime": mrpConfigRecoveryTime,
       "mrpConfigPort1": mrpConfigPort1,
       "mrpConfigPort2": mrpConfigPort2,
       "mrpConfigVlanId": mrpConfigVlanId,
       "mrpConfigResetRoundTripDelays": mrpConfigResetRoundTripDelays,
       "mrpConfigResetStatistics": mrpConfigResetStatistics,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusIndex": statusIndex,
       "statusState": statusState,
       "statusLastStateChange": statusLastStateChange,
       "statusRingInterrupt": statusRingInterrupt,
       "statusGlobalRingAlarm": statusGlobalRingAlarm,
       "statusErrorDetected": statusErrorDetected,
       "statusRingPortAInterrupted": statusRingPortAInterrupted,
       "statusRingPortBInterrupted": statusRingPortBInterrupted,
       "statisticsTable": statisticsTable,
       "statisticsEntry": statisticsEntry,
       "statisticsIndex": statisticsIndex,
       "statisticsNumberOfBackups": statisticsNumberOfBackups,
       "statisticsCurrentBackupDuration": statisticsCurrentBackupDuration,
       "statisticsLastBackupDuration": statisticsLastBackupDuration,
       "statisticsTotalBackupDuration": statisticsTotalBackupDuration,
       "couplingStatusTable": couplingStatusTable,
       "couplingStatusEntry": couplingStatusEntry,
       "couplingStatusIndex": couplingStatusIndex,
       "couplingStatusControllerState": couplingStatusControllerState,
       "couplingStatusCportLink": couplingStatusCportLink,
       "couplingStatusCportForward": couplingStatusCportForward,
       "couplingStatusCportTimeout": couplingStatusCportTimeout,
       "couplingStatusConnectionValid": couplingStatusConnectionValid,
       "couplingStatusValidPartnerIp": couplingStatusValidPartnerIp,
       "couplingStatusValidPartnerId": couplingStatusValidPartnerId,
       "mrpStatusTable": mrpStatusTable,
       "mrpStatusEntry": mrpStatusEntry,
       "mrpStatusIndex": mrpStatusIndex,
       "mrpStatusAdminRole": mrpStatusAdminRole,
       "mrpStatusOperationalRole": mrpStatusOperationalRole,
       "mrpStatusPortAState": mrpStatusPortAState,
       "mrpStatusPortBState": mrpStatusPortBState,
       "mrpStatusDomainId": mrpStatusDomainId,
       "mrpStatusDomainState": mrpStatusDomainState,
       "mrpStatusDomainError": mrpStatusDomainError,
       "mrpStatusDomainBlocked": mrpStatusDomainBlocked,
       "mrpStatusManagerPriority": mrpStatusManagerPriority,
       "mrpStatusRingOpenCount": mrpStatusRingOpenCount,
       "mrpStatusLastRingOpenTimeStamp": mrpStatusLastRingOpenTimeStamp,
       "mrpStatusMaxRoundTripDelay": mrpStatusMaxRoundTripDelay,
       "mrpStatusMinRoundTripDelay": mrpStatusMinRoundTripDelay}
)
