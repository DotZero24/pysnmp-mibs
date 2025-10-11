# SNMP MIB module (SWITCH-RATELIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-RATELIMIT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:03 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcRateLimit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcUplinkPort_Type = Integer32
_RcUplinkPort_Object = MibScalar
rcUplinkPort = _RcUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 1),
    _RcUplinkPort_Type()
)
rcUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcUplinkPort.setStatus("deprecated")
_RcRateLimitPortTable_Object = MibTable
rcRateLimitPortTable = _RcRateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rcRateLimitPortTable.setStatus("current")
_RcRateLimitPortEntry_Object = MibTableRow
rcRateLimitPortEntry = _RcRateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1)
)
rcRateLimitPortEntry.setIndexNames(
    (0, "SWITCH-RATELIMIT-MIB", "rcRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    rcRateLimitPortEntry.setStatus("current")
_RcRateLimitPortIndex_Type = Integer32
_RcRateLimitPortIndex_Object = MibTableColumn
rcRateLimitPortIndex = _RcRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 1),
    _RcRateLimitPortIndex_Type()
)
rcRateLimitPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitPortIndex.setStatus("current")


class _RcRateLimitPortRule_Type(Integer32):
    """Custom type rcRateLimitPortRule based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_RcRateLimitPortRule_Type.__name__ = "Integer32"
_RcRateLimitPortRule_Object = MibTableColumn
rcRateLimitPortRule = _RcRateLimitPortRule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 2),
    _RcRateLimitPortRule_Type()
)
rcRateLimitPortRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitPortRule.setStatus("obsolete")


class _RcRateLimitPortIngressRate_Type(Integer32):
    """Custom type rcRateLimitPortIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcRateLimitPortIngressRate_Type.__name__ = "Integer32"
_RcRateLimitPortIngressRate_Object = MibTableColumn
rcRateLimitPortIngressRate = _RcRateLimitPortIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 3),
    _RcRateLimitPortIngressRate_Type()
)
rcRateLimitPortIngressRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitPortIngressRate.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitPortIngressRate.setUnits("kbps")


class _RcRateLimitPortIngressBurst_Type(Integer32):
    """Custom type rcRateLimitPortIngressBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcRateLimitPortIngressBurst_Type.__name__ = "Integer32"
_RcRateLimitPortIngressBurst_Object = MibTableColumn
rcRateLimitPortIngressBurst = _RcRateLimitPortIngressBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 4),
    _RcRateLimitPortIngressBurst_Type()
)
rcRateLimitPortIngressBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitPortIngressBurst.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitPortIngressBurst.setUnits("kB")


class _RcRateLimitPortEgressRate_Type(Integer32):
    """Custom type rcRateLimitPortEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcRateLimitPortEgressRate_Type.__name__ = "Integer32"
_RcRateLimitPortEgressRate_Object = MibTableColumn
rcRateLimitPortEgressRate = _RcRateLimitPortEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 5),
    _RcRateLimitPortEgressRate_Type()
)
rcRateLimitPortEgressRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitPortEgressRate.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitPortEgressRate.setUnits("kbps")


class _RcRateLimitPortEgressBurst_Type(Integer32):
    """Custom type rcRateLimitPortEgressBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcRateLimitPortEgressBurst_Type.__name__ = "Integer32"
_RcRateLimitPortEgressBurst_Object = MibTableColumn
rcRateLimitPortEgressBurst = _RcRateLimitPortEgressBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 2, 1, 6),
    _RcRateLimitPortEgressBurst_Type()
)
rcRateLimitPortEgressBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitPortEgressBurst.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitPortEgressBurst.setUnits("kB")
_RcRateLimitVlanTable_Object = MibTable
rcRateLimitVlanTable = _RcRateLimitVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rcRateLimitVlanTable.setStatus("current")
_RcRateLimitVlanEntry_Object = MibTableRow
rcRateLimitVlanEntry = _RcRateLimitVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1)
)
rcRateLimitVlanEntry.setIndexNames(
    (0, "SWITCH-RATELIMIT-MIB", "rcRateLimitVlanType"),
    (0, "SWITCH-RATELIMIT-MIB", "rcRateLimitVlanCVlanID"),
    (0, "SWITCH-RATELIMIT-MIB", "rcRateLimitVlanSPVlanID"),
)
if mibBuilder.loadTexts:
    rcRateLimitVlanEntry.setStatus("current")


class _RcRateLimitVlanType_Type(Integer32):
    """Custom type rcRateLimitVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("double", 2))
    )


_RcRateLimitVlanType_Type.__name__ = "Integer32"
_RcRateLimitVlanType_Object = MibTableColumn
rcRateLimitVlanType = _RcRateLimitVlanType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 1),
    _RcRateLimitVlanType_Type()
)
rcRateLimitVlanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRateLimitVlanType.setStatus("current")


class _RcRateLimitVlanCVlanID_Type(Integer32):
    """Custom type rcRateLimitVlanCVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcRateLimitVlanCVlanID_Type.__name__ = "Integer32"
_RcRateLimitVlanCVlanID_Object = MibTableColumn
rcRateLimitVlanCVlanID = _RcRateLimitVlanCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 2),
    _RcRateLimitVlanCVlanID_Type()
)
rcRateLimitVlanCVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRateLimitVlanCVlanID.setStatus("current")


class _RcRateLimitVlanSPVlanID_Type(Integer32):
    """Custom type rcRateLimitVlanSPVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcRateLimitVlanSPVlanID_Type.__name__ = "Integer32"
_RcRateLimitVlanSPVlanID_Object = MibTableColumn
rcRateLimitVlanSPVlanID = _RcRateLimitVlanSPVlanID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 3),
    _RcRateLimitVlanSPVlanID_Type()
)
rcRateLimitVlanSPVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRateLimitVlanSPVlanID.setStatus("current")


class _RcRateLimitVlanRate_Type(Integer32):
    """Custom type rcRateLimitVlanRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcRateLimitVlanRate_Type.__name__ = "Integer32"
_RcRateLimitVlanRate_Object = MibTableColumn
rcRateLimitVlanRate = _RcRateLimitVlanRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 4),
    _RcRateLimitVlanRate_Type()
)
rcRateLimitVlanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitVlanRate.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitVlanRate.setUnits("kbps")


class _RcRateLimitVlanBurst_Type(Integer32):
    """Custom type rcRateLimitVlanBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcRateLimitVlanBurst_Type.__name__ = "Integer32"
_RcRateLimitVlanBurst_Object = MibTableColumn
rcRateLimitVlanBurst = _RcRateLimitVlanBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 5),
    _RcRateLimitVlanBurst_Type()
)
rcRateLimitVlanBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitVlanBurst.setStatus("current")
if mibBuilder.loadTexts:
    rcRateLimitVlanBurst.setUnits("kB")
_RcRateLimitVlanRowStatus_Type = RowStatus
_RcRateLimitVlanRowStatus_Object = MibTableColumn
rcRateLimitVlanRowStatus = _RcRateLimitVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 6),
    _RcRateLimitVlanRowStatus_Type()
)
rcRateLimitVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitVlanRowStatus.setStatus("current")
_RcRateLimitVlanStatsEnable_Type = EnableVar
_RcRateLimitVlanStatsEnable_Object = MibTableColumn
rcRateLimitVlanStatsEnable = _RcRateLimitVlanStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 7),
    _RcRateLimitVlanStatsEnable_Type()
)
rcRateLimitVlanStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitVlanStatsEnable.setStatus("current")
_RcRateLimitVlanStatHwStatus_Type = EnableVar
_RcRateLimitVlanStatHwStatus_Object = MibTableColumn
rcRateLimitVlanStatHwStatus = _RcRateLimitVlanStatHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 3, 1, 8),
    _RcRateLimitVlanStatHwStatus_Type()
)
rcRateLimitVlanStatHwStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRateLimitVlanStatHwStatus.setStatus("current")
_RcRateLimitVlanStatisticsTable_Object = MibTable
rcRateLimitVlanStatisticsTable = _RcRateLimitVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rcRateLimitVlanStatisticsTable.setStatus("current")
_RcRateLimitVlanStatisticsEntry_Object = MibTableRow
rcRateLimitVlanStatisticsEntry = _RcRateLimitVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rcRateLimitVlanStatisticsEntry.setStatus("current")
_RcRateLimitVlanCounterReset_Type = EnableVar
_RcRateLimitVlanCounterReset_Object = MibTableColumn
rcRateLimitVlanCounterReset = _RcRateLimitVlanCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 1),
    _RcRateLimitVlanCounterReset_Type()
)
rcRateLimitVlanCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterReset.setStatus("current")
_RcRateLimitVlanCounterInprofilePkt64_Type = Counter64
_RcRateLimitVlanCounterInprofilePkt64_Object = MibTableColumn
rcRateLimitVlanCounterInprofilePkt64 = _RcRateLimitVlanCounterInprofilePkt64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 2),
    _RcRateLimitVlanCounterInprofilePkt64_Type()
)
rcRateLimitVlanCounterInprofilePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterInprofilePkt64.setStatus("current")
_RcRateLimitVlanCounterInprofileByte64_Type = Counter64
_RcRateLimitVlanCounterInprofileByte64_Object = MibTableColumn
rcRateLimitVlanCounterInprofileByte64 = _RcRateLimitVlanCounterInprofileByte64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 3),
    _RcRateLimitVlanCounterInprofileByte64_Type()
)
rcRateLimitVlanCounterInprofileByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterInprofileByte64.setStatus("current")
_RcRateLimitVlanCounterOutprofilePkt64_Type = Counter64
_RcRateLimitVlanCounterOutprofilePkt64_Object = MibTableColumn
rcRateLimitVlanCounterOutprofilePkt64 = _RcRateLimitVlanCounterOutprofilePkt64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 4),
    _RcRateLimitVlanCounterOutprofilePkt64_Type()
)
rcRateLimitVlanCounterOutprofilePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterOutprofilePkt64.setStatus("current")
_RcRateLimitVlanCounterOutprofileByte64_Type = Counter64
_RcRateLimitVlanCounterOutprofileByte64_Object = MibTableColumn
rcRateLimitVlanCounterOutprofileByte64 = _RcRateLimitVlanCounterOutprofileByte64_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 5),
    _RcRateLimitVlanCounterOutprofileByte64_Type()
)
rcRateLimitVlanCounterOutprofileByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterOutprofileByte64.setStatus("current")
_RcRateLimitVlanCounterStatisticUnit_Type = Integer32
_RcRateLimitVlanCounterStatisticUnit_Object = MibTableColumn
rcRateLimitVlanCounterStatisticUnit = _RcRateLimitVlanCounterStatisticUnit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 4, 1, 6),
    _RcRateLimitVlanCounterStatisticUnit_Type()
)
rcRateLimitVlanCounterStatisticUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRateLimitVlanCounterStatisticUnit.setStatus("current")
rcRateLimitVlanEntry.registerAugmentions(
    ("SWITCH-RATELIMIT-MIB",
     "rcRateLimitVlanStatisticsEntry")
)
rcRateLimitVlanStatisticsEntry.setIndexNames(*rcRateLimitVlanEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-RATELIMIT-MIB",
    **{"rcRateLimit": rcRateLimit,
       "rcUplinkPort": rcUplinkPort,
       "rcRateLimitPortTable": rcRateLimitPortTable,
       "rcRateLimitPortEntry": rcRateLimitPortEntry,
       "rcRateLimitPortIndex": rcRateLimitPortIndex,
       "rcRateLimitPortRule": rcRateLimitPortRule,
       "rcRateLimitPortIngressRate": rcRateLimitPortIngressRate,
       "rcRateLimitPortIngressBurst": rcRateLimitPortIngressBurst,
       "rcRateLimitPortEgressRate": rcRateLimitPortEgressRate,
       "rcRateLimitPortEgressBurst": rcRateLimitPortEgressBurst,
       "rcRateLimitVlanTable": rcRateLimitVlanTable,
       "rcRateLimitVlanEntry": rcRateLimitVlanEntry,
       "rcRateLimitVlanType": rcRateLimitVlanType,
       "rcRateLimitVlanCVlanID": rcRateLimitVlanCVlanID,
       "rcRateLimitVlanSPVlanID": rcRateLimitVlanSPVlanID,
       "rcRateLimitVlanRate": rcRateLimitVlanRate,
       "rcRateLimitVlanBurst": rcRateLimitVlanBurst,
       "rcRateLimitVlanRowStatus": rcRateLimitVlanRowStatus,
       "rcRateLimitVlanStatsEnable": rcRateLimitVlanStatsEnable,
       "rcRateLimitVlanStatHwStatus": rcRateLimitVlanStatHwStatus,
       "rcRateLimitVlanStatisticsTable": rcRateLimitVlanStatisticsTable,
       "rcRateLimitVlanStatisticsEntry": rcRateLimitVlanStatisticsEntry,
       "rcRateLimitVlanCounterReset": rcRateLimitVlanCounterReset,
       "rcRateLimitVlanCounterInprofilePkt64": rcRateLimitVlanCounterInprofilePkt64,
       "rcRateLimitVlanCounterInprofileByte64": rcRateLimitVlanCounterInprofileByte64,
       "rcRateLimitVlanCounterOutprofilePkt64": rcRateLimitVlanCounterOutprofilePkt64,
       "rcRateLimitVlanCounterOutprofileByte64": rcRateLimitVlanCounterOutprofileByte64,
       "rcRateLimitVlanCounterStatisticUnit": rcRateLimitVlanCounterStatisticUnit}
)
