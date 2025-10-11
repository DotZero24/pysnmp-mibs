# SNMP MIB module (SUPERMICRO-OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFV3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:45 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(AreaID,
 BigMetric,
 RouterID,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "RouterID",
    "Status")

(ospfv3NbrRestartHelperAge,
 ospfv3NbrRestartHelperExitReason,
 ospfv3NbrRestartHelperStatus,
 ospfv3RestartExitReason,
 ospfv3RestartInterval,
 ospfv3RestartStatus,
 ospfv3RouterId,
 ospfv3VirtNbrRestartHelperAge,
 ospfv3VirtNbrRestartHelperExitReason,
 ospfv3VirtNbrRestartHelperStatus) = mibBuilder.importSymbols(
    "OSPFV3-MIB",
    "ospfv3NbrRestartHelperAge",
    "ospfv3NbrRestartHelperExitReason",
    "ospfv3NbrRestartHelperStatus",
    "ospfv3RestartExitReason",
    "ospfv3RestartInterval",
    "ospfv3RestartStatus",
    "ospfv3RouterId",
    "ospfv3VirtNbrRestartHelperAge",
    "ospfv3VirtNbrRestartHelperExitReason",
    "ospfv3VirtNbrRestartHelperStatus")

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

futospfv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90)
)
if mibBuilder.loadTexts:
    futospfv3.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Futospfv3GeneralGroup_ObjectIdentity = ObjectIdentity
futospfv3GeneralGroup = _Futospfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1)
)


class _FutOspfv3OverFlowState_Type(TruthValue):
    """Custom type futOspfv3OverFlowState based on TruthValue"""
    defaultValue = 2


_FutOspfv3OverFlowState_Type.__name__ = "TruthValue"
_FutOspfv3OverFlowState_Object = MibScalar
futOspfv3OverFlowState = _FutOspfv3OverFlowState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 1),
    _FutOspfv3OverFlowState_Type()
)
futOspfv3OverFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3OverFlowState.setStatus("current")


class _FutOspfv3TraceLevel_Type(Integer32):
    """Custom type futOspfv3TraceLevel based on Integer32"""
    defaultValue = 2048


_FutOspfv3TraceLevel_Type.__name__ = "Integer32"
_FutOspfv3TraceLevel_Object = MibScalar
futOspfv3TraceLevel = _FutOspfv3TraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 2),
    _FutOspfv3TraceLevel_Type()
)
futOspfv3TraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3TraceLevel.setStatus("current")


class _FutOspfv3ABRType_Type(Integer32):
    """Custom type futOspfv3ABRType based on Integer32"""
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
        *(("standardABR", 1),
          ("ciscoABR", 2),
          ("ibmABR", 3))
    )


_FutOspfv3ABRType_Type.__name__ = "Integer32"
_FutOspfv3ABRType_Object = MibScalar
futOspfv3ABRType = _FutOspfv3ABRType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 3),
    _FutOspfv3ABRType_Type()
)
futOspfv3ABRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3ABRType.setStatus("current")


class _FutOspfv3NssaAsbrDefRtTrans_Type(Integer32):
    """Custom type futOspfv3NssaAsbrDefRtTrans based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FutOspfv3NssaAsbrDefRtTrans_Type.__name__ = "Integer32"
_FutOspfv3NssaAsbrDefRtTrans_Object = MibScalar
futOspfv3NssaAsbrDefRtTrans = _FutOspfv3NssaAsbrDefRtTrans_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 4),
    _FutOspfv3NssaAsbrDefRtTrans_Type()
)
futOspfv3NssaAsbrDefRtTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3NssaAsbrDefRtTrans.setStatus("current")


class _FutOspfv3DefaultPassiveInterface_Type(TruthValue):
    """Custom type futOspfv3DefaultPassiveInterface based on TruthValue"""
    defaultValue = 2


_FutOspfv3DefaultPassiveInterface_Type.__name__ = "TruthValue"
_FutOspfv3DefaultPassiveInterface_Object = MibScalar
futOspfv3DefaultPassiveInterface = _FutOspfv3DefaultPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 5),
    _FutOspfv3DefaultPassiveInterface_Type()
)
futOspfv3DefaultPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3DefaultPassiveInterface.setStatus("current")


class _FutOspfv3SpfDelay_Type(Integer32):
    """Custom type futOspfv3SpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfv3SpfDelay_Type.__name__ = "Integer32"
_FutOspfv3SpfDelay_Object = MibScalar
futOspfv3SpfDelay = _FutOspfv3SpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 6),
    _FutOspfv3SpfDelay_Type()
)
futOspfv3SpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3SpfDelay.setStatus("current")


class _FutOspfv3SpfHoldTime_Type(Integer32):
    """Custom type futOspfv3SpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfv3SpfHoldTime_Type.__name__ = "Integer32"
_FutOspfv3SpfHoldTime_Object = MibScalar
futOspfv3SpfHoldTime = _FutOspfv3SpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 7),
    _FutOspfv3SpfHoldTime_Type()
)
futOspfv3SpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3SpfHoldTime.setStatus("current")


class _FutOspfv3RTStaggeringInterval_Type(Integer32):
    """Custom type futOspfv3RTStaggeringInterval based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_FutOspfv3RTStaggeringInterval_Type.__name__ = "Integer32"
_FutOspfv3RTStaggeringInterval_Object = MibScalar
futOspfv3RTStaggeringInterval = _FutOspfv3RTStaggeringInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 8),
    _FutOspfv3RTStaggeringInterval_Type()
)
futOspfv3RTStaggeringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RTStaggeringInterval.setStatus("current")


class _FutOspfv3RTStaggeringStatus_Type(Integer32):
    """Custom type futOspfv3RTStaggeringStatus based on Integer32"""
    defaultValue = 1

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


_FutOspfv3RTStaggeringStatus_Type.__name__ = "Integer32"
_FutOspfv3RTStaggeringStatus_Object = MibScalar
futOspfv3RTStaggeringStatus = _FutOspfv3RTStaggeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 9),
    _FutOspfv3RTStaggeringStatus_Type()
)
futOspfv3RTStaggeringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RTStaggeringStatus.setStatus("current")


class _FutOspfv3RestartStrictLsaChecking_Type(TruthValue):
    """Custom type futOspfv3RestartStrictLsaChecking based on TruthValue"""
    defaultValue = 2


_FutOspfv3RestartStrictLsaChecking_Type.__name__ = "TruthValue"
_FutOspfv3RestartStrictLsaChecking_Object = MibScalar
futOspfv3RestartStrictLsaChecking = _FutOspfv3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 10),
    _FutOspfv3RestartStrictLsaChecking_Type()
)
futOspfv3RestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RestartStrictLsaChecking.setStatus("current")


class _FutOspfv3HelperSupport_Type(Bits):
    """Custom type futOspfv3HelperSupport based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2),
          ("switchToRedundant", 3))
    )

_FutOspfv3HelperSupport_Type.__name__ = "Bits"
_FutOspfv3HelperSupport_Object = MibScalar
futOspfv3HelperSupport = _FutOspfv3HelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 11),
    _FutOspfv3HelperSupport_Type()
)
futOspfv3HelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3HelperSupport.setStatus("current")


class _FutOspfv3HelperGraceTimeLimit_Type(Integer32):
    """Custom type futOspfv3HelperGraceTimeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_FutOspfv3HelperGraceTimeLimit_Type.__name__ = "Integer32"
_FutOspfv3HelperGraceTimeLimit_Object = MibScalar
futOspfv3HelperGraceTimeLimit = _FutOspfv3HelperGraceTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 12),
    _FutOspfv3HelperGraceTimeLimit_Type()
)
futOspfv3HelperGraceTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3HelperGraceTimeLimit.setStatus("current")


class _FutOspfv3RestartAckState_Type(Integer32):
    """Custom type futOspfv3RestartAckState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FutOspfv3RestartAckState_Type.__name__ = "Integer32"
_FutOspfv3RestartAckState_Object = MibScalar
futOspfv3RestartAckState = _FutOspfv3RestartAckState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 13),
    _FutOspfv3RestartAckState_Type()
)
futOspfv3RestartAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RestartAckState.setStatus("current")


class _FutOspfv3GraceLsaRetransmitCount_Type(Integer32):
    """Custom type futOspfv3GraceLsaRetransmitCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FutOspfv3GraceLsaRetransmitCount_Type.__name__ = "Integer32"
_FutOspfv3GraceLsaRetransmitCount_Object = MibScalar
futOspfv3GraceLsaRetransmitCount = _FutOspfv3GraceLsaRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 14),
    _FutOspfv3GraceLsaRetransmitCount_Type()
)
futOspfv3GraceLsaRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3GraceLsaRetransmitCount.setStatus("current")


class _FutOspfv3RestartReason_Type(Integer32):
    """Custom type futOspfv3RestartReason based on Integer32"""
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
        *(("unknown", 0),
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2),
          ("switchToRedundant", 3))
    )


_FutOspfv3RestartReason_Type.__name__ = "Integer32"
_FutOspfv3RestartReason_Object = MibScalar
futOspfv3RestartReason = _FutOspfv3RestartReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 15),
    _FutOspfv3RestartReason_Type()
)
futOspfv3RestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RestartReason.setStatus("current")
_FutOspfv3ExtTraceLevel_Type = Integer32
_FutOspfv3ExtTraceLevel_Object = MibScalar
futOspfv3ExtTraceLevel = _FutOspfv3ExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 16),
    _FutOspfv3ExtTraceLevel_Type()
)
futOspfv3ExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3ExtTraceLevel.setStatus("current")
_FutOspfv3SetTraps_Type = Integer32
_FutOspfv3SetTraps_Object = MibScalar
futOspfv3SetTraps = _FutOspfv3SetTraps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 17),
    _FutOspfv3SetTraps_Type()
)
futOspfv3SetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3SetTraps.setStatus("current")


class _FutOspfv3HotStandbyAdminStatus_Type(Integer32):
    """Custom type futOspfv3HotStandbyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FutOspfv3HotStandbyAdminStatus_Type.__name__ = "Integer32"
_FutOspfv3HotStandbyAdminStatus_Object = MibScalar
futOspfv3HotStandbyAdminStatus = _FutOspfv3HotStandbyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 18),
    _FutOspfv3HotStandbyAdminStatus_Type()
)
futOspfv3HotStandbyAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3HotStandbyAdminStatus.setStatus("current")


class _FutOspfv3HotStandbyState_Type(Integer32):
    """Custom type futOspfv3HotStandbyState based on Integer32"""
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
        *(("init", 1),
          ("activeStandbyUp", 2),
          ("activeStandbyDown", 3),
          ("standby", 4))
    )


_FutOspfv3HotStandbyState_Type.__name__ = "Integer32"
_FutOspfv3HotStandbyState_Object = MibScalar
futOspfv3HotStandbyState = _FutOspfv3HotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 19),
    _FutOspfv3HotStandbyState_Type()
)
futOspfv3HotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3HotStandbyState.setStatus("current")


class _FutOspfv3DynamicBulkUpdStatus_Type(Integer32):
    """Custom type futOspfv3DynamicBulkUpdStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("aborted", 4))
    )


_FutOspfv3DynamicBulkUpdStatus_Type.__name__ = "Integer32"
_FutOspfv3DynamicBulkUpdStatus_Object = MibScalar
futOspfv3DynamicBulkUpdStatus = _FutOspfv3DynamicBulkUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 20),
    _FutOspfv3DynamicBulkUpdStatus_Type()
)
futOspfv3DynamicBulkUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3DynamicBulkUpdStatus.setStatus("current")
_FutOspfv3StandbyHelloSyncCount_Type = Counter32
_FutOspfv3StandbyHelloSyncCount_Object = MibScalar
futOspfv3StandbyHelloSyncCount = _FutOspfv3StandbyHelloSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 21),
    _FutOspfv3StandbyHelloSyncCount_Type()
)
futOspfv3StandbyHelloSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3StandbyHelloSyncCount.setStatus("current")
_FutOspfv3StandbyLsaSyncCount_Type = Counter32
_FutOspfv3StandbyLsaSyncCount_Object = MibScalar
futOspfv3StandbyLsaSyncCount = _FutOspfv3StandbyLsaSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 1, 22),
    _FutOspfv3StandbyLsaSyncCount_Type()
)
futOspfv3StandbyLsaSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3StandbyLsaSyncCount.setStatus("current")
_FutOspfv3IfTable_Object = MibTable
futOspfv3IfTable = _FutOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2)
)
if mibBuilder.loadTexts:
    futOspfv3IfTable.setStatus("current")
_FutOspfv3IfEntry_Object = MibTableRow
futOspfv3IfEntry = _FutOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1)
)
futOspfv3IfEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3IfIndex"),
)
if mibBuilder.loadTexts:
    futOspfv3IfEntry.setStatus("current")
_FutOspfv3IfIndex_Type = InterfaceIndex
_FutOspfv3IfIndex_Object = MibTableColumn
futOspfv3IfIndex = _FutOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 1),
    _FutOspfv3IfIndex_Type()
)
futOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3IfIndex.setStatus("current")


class _FutOspfv3IfOperState_Type(Integer32):
    """Custom type futOspfv3IfOperState based on Integer32"""
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
        *(("operup", 1),
          ("operdown", 2),
          ("loopback", 3),
          ("unloop", 4))
    )


_FutOspfv3IfOperState_Type.__name__ = "Integer32"
_FutOspfv3IfOperState_Object = MibTableColumn
futOspfv3IfOperState = _FutOspfv3IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 2),
    _FutOspfv3IfOperState_Type()
)
futOspfv3IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfOperState.setStatus("current")


class _FutOspfv3IfPassive_Type(TruthValue):
    """Custom type futOspfv3IfPassive based on TruthValue"""
    defaultValue = 2


_FutOspfv3IfPassive_Type.__name__ = "TruthValue"
_FutOspfv3IfPassive_Object = MibTableColumn
futOspfv3IfPassive = _FutOspfv3IfPassive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 3),
    _FutOspfv3IfPassive_Type()
)
futOspfv3IfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3IfPassive.setStatus("current")
_FutOspfv3IfNbrCount_Type = Gauge32
_FutOspfv3IfNbrCount_Object = MibTableColumn
futOspfv3IfNbrCount = _FutOspfv3IfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 4),
    _FutOspfv3IfNbrCount_Type()
)
futOspfv3IfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfNbrCount.setStatus("current")
_FutOspfv3IfAdjCount_Type = Gauge32
_FutOspfv3IfAdjCount_Object = MibTableColumn
futOspfv3IfAdjCount = _FutOspfv3IfAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 5),
    _FutOspfv3IfAdjCount_Type()
)
futOspfv3IfAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfAdjCount.setStatus("current")
_FutOspfv3IfHelloRcvd_Type = Counter32
_FutOspfv3IfHelloRcvd_Object = MibTableColumn
futOspfv3IfHelloRcvd = _FutOspfv3IfHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 6),
    _FutOspfv3IfHelloRcvd_Type()
)
futOspfv3IfHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfHelloRcvd.setStatus("current")
_FutOspfv3IfHelloTxed_Type = Counter32
_FutOspfv3IfHelloTxed_Object = MibTableColumn
futOspfv3IfHelloTxed = _FutOspfv3IfHelloTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 7),
    _FutOspfv3IfHelloTxed_Type()
)
futOspfv3IfHelloTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfHelloTxed.setStatus("current")
_FutOspfv3IfHelloDisd_Type = Counter32
_FutOspfv3IfHelloDisd_Object = MibTableColumn
futOspfv3IfHelloDisd = _FutOspfv3IfHelloDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 8),
    _FutOspfv3IfHelloDisd_Type()
)
futOspfv3IfHelloDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfHelloDisd.setStatus("current")
_FutOspfv3IfDdpRcvd_Type = Counter32
_FutOspfv3IfDdpRcvd_Object = MibTableColumn
futOspfv3IfDdpRcvd = _FutOspfv3IfDdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 9),
    _FutOspfv3IfDdpRcvd_Type()
)
futOspfv3IfDdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfDdpRcvd.setStatus("current")
_FutOspfv3IfDdpTxed_Type = Counter32
_FutOspfv3IfDdpTxed_Object = MibTableColumn
futOspfv3IfDdpTxed = _FutOspfv3IfDdpTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 10),
    _FutOspfv3IfDdpTxed_Type()
)
futOspfv3IfDdpTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfDdpTxed.setStatus("current")
_FutOspfv3IfDdpDisd_Type = Counter32
_FutOspfv3IfDdpDisd_Object = MibTableColumn
futOspfv3IfDdpDisd = _FutOspfv3IfDdpDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 11),
    _FutOspfv3IfDdpDisd_Type()
)
futOspfv3IfDdpDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfDdpDisd.setStatus("current")
_FutOspfv3IfLrqRcvd_Type = Counter32
_FutOspfv3IfLrqRcvd_Object = MibTableColumn
futOspfv3IfLrqRcvd = _FutOspfv3IfLrqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 12),
    _FutOspfv3IfLrqRcvd_Type()
)
futOspfv3IfLrqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLrqRcvd.setStatus("current")
_FutOspfv3IfLrqTxed_Type = Counter32
_FutOspfv3IfLrqTxed_Object = MibTableColumn
futOspfv3IfLrqTxed = _FutOspfv3IfLrqTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 13),
    _FutOspfv3IfLrqTxed_Type()
)
futOspfv3IfLrqTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLrqTxed.setStatus("current")
_FutOspfv3IfLrqDisd_Type = Counter32
_FutOspfv3IfLrqDisd_Object = MibTableColumn
futOspfv3IfLrqDisd = _FutOspfv3IfLrqDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 14),
    _FutOspfv3IfLrqDisd_Type()
)
futOspfv3IfLrqDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLrqDisd.setStatus("current")
_FutOspfv3IfLsuRcvd_Type = Counter32
_FutOspfv3IfLsuRcvd_Object = MibTableColumn
futOspfv3IfLsuRcvd = _FutOspfv3IfLsuRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 15),
    _FutOspfv3IfLsuRcvd_Type()
)
futOspfv3IfLsuRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLsuRcvd.setStatus("current")
_FutOspfv3IfLsuTxed_Type = Counter32
_FutOspfv3IfLsuTxed_Object = MibTableColumn
futOspfv3IfLsuTxed = _FutOspfv3IfLsuTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 16),
    _FutOspfv3IfLsuTxed_Type()
)
futOspfv3IfLsuTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLsuTxed.setStatus("current")
_FutOspfv3IfLsuDisd_Type = Counter32
_FutOspfv3IfLsuDisd_Object = MibTableColumn
futOspfv3IfLsuDisd = _FutOspfv3IfLsuDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 17),
    _FutOspfv3IfLsuDisd_Type()
)
futOspfv3IfLsuDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLsuDisd.setStatus("current")
_FutOspfv3IfLakRcvd_Type = Counter32
_FutOspfv3IfLakRcvd_Object = MibTableColumn
futOspfv3IfLakRcvd = _FutOspfv3IfLakRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 18),
    _FutOspfv3IfLakRcvd_Type()
)
futOspfv3IfLakRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLakRcvd.setStatus("current")
_FutOspfv3IfLakTxed_Type = Counter32
_FutOspfv3IfLakTxed_Object = MibTableColumn
futOspfv3IfLakTxed = _FutOspfv3IfLakTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 19),
    _FutOspfv3IfLakTxed_Type()
)
futOspfv3IfLakTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLakTxed.setStatus("current")
_FutOspfv3IfLakDisd_Type = Counter32
_FutOspfv3IfLakDisd_Object = MibTableColumn
futOspfv3IfLakDisd = _FutOspfv3IfLakDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 20),
    _FutOspfv3IfLakDisd_Type()
)
futOspfv3IfLakDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3IfLakDisd.setStatus("current")


class _FutOspfv3IfLinkLSASuppression_Type(TruthValue):
    """Custom type futOspfv3IfLinkLSASuppression based on TruthValue"""
    defaultValue = 2


_FutOspfv3IfLinkLSASuppression_Type.__name__ = "TruthValue"
_FutOspfv3IfLinkLSASuppression_Object = MibTableColumn
futOspfv3IfLinkLSASuppression = _FutOspfv3IfLinkLSASuppression_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 2, 1, 21),
    _FutOspfv3IfLinkLSASuppression_Type()
)
futOspfv3IfLinkLSASuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3IfLinkLSASuppression.setStatus("current")
_FutOspfv3RoutingTable_Object = MibTable
futOspfv3RoutingTable = _FutOspfv3RoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3)
)
if mibBuilder.loadTexts:
    futOspfv3RoutingTable.setStatus("current")
_FutOspfv3RoutingEntry_Object = MibTableRow
futOspfv3RoutingEntry = _FutOspfv3RoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1)
)
futOspfv3RoutingEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RouteDestType"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RouteDest"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RoutePfxLength"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RouteNextHopType"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RouteNextHop"),
)
if mibBuilder.loadTexts:
    futOspfv3RoutingEntry.setStatus("current")
_FutOspfv3RouteDestType_Type = InetAddressType
_FutOspfv3RouteDestType_Object = MibTableColumn
futOspfv3RouteDestType = _FutOspfv3RouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 1),
    _FutOspfv3RouteDestType_Type()
)
futOspfv3RouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RouteDestType.setStatus("current")


class _FutOspfv3RouteDest_Type(InetAddress):
    """Custom type futOspfv3RouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3RouteDest_Type.__name__ = "InetAddress"
_FutOspfv3RouteDest_Object = MibTableColumn
futOspfv3RouteDest = _FutOspfv3RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 2),
    _FutOspfv3RouteDest_Type()
)
futOspfv3RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RouteDest.setStatus("current")
_FutOspfv3RoutePfxLength_Type = InetAddressPrefixLength
_FutOspfv3RoutePfxLength_Object = MibTableColumn
futOspfv3RoutePfxLength = _FutOspfv3RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 3),
    _FutOspfv3RoutePfxLength_Type()
)
futOspfv3RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RoutePfxLength.setStatus("current")
_FutOspfv3RouteNextHopType_Type = InetAddressType
_FutOspfv3RouteNextHopType_Object = MibTableColumn
futOspfv3RouteNextHopType = _FutOspfv3RouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 4),
    _FutOspfv3RouteNextHopType_Type()
)
futOspfv3RouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RouteNextHopType.setStatus("current")


class _FutOspfv3RouteNextHop_Type(InetAddress):
    """Custom type futOspfv3RouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3RouteNextHop_Type.__name__ = "InetAddress"
_FutOspfv3RouteNextHop_Object = MibTableColumn
futOspfv3RouteNextHop = _FutOspfv3RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 5),
    _FutOspfv3RouteNextHop_Type()
)
futOspfv3RouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RouteNextHop.setStatus("current")


class _FutOspfv3RouteType_Type(Integer32):
    """Custom type futOspfv3RouteType based on Integer32"""
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
        *(("intraArea", 1),
          ("interArea", 2),
          ("type1External", 3),
          ("type2External", 4))
    )


_FutOspfv3RouteType_Type.__name__ = "Integer32"
_FutOspfv3RouteType_Object = MibTableColumn
futOspfv3RouteType = _FutOspfv3RouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 6),
    _FutOspfv3RouteType_Type()
)
futOspfv3RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3RouteType.setStatus("current")
_FutOspfv3RouteAreaId_Type = AreaID
_FutOspfv3RouteAreaId_Object = MibTableColumn
futOspfv3RouteAreaId = _FutOspfv3RouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 7),
    _FutOspfv3RouteAreaId_Type()
)
futOspfv3RouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3RouteAreaId.setStatus("current")
_FutOspfv3RouteCost_Type = BigMetric
_FutOspfv3RouteCost_Object = MibTableColumn
futOspfv3RouteCost = _FutOspfv3RouteCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 8),
    _FutOspfv3RouteCost_Type()
)
futOspfv3RouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3RouteCost.setStatus("current")
_FutOspfv3RouteType2Cost_Type = BigMetric
_FutOspfv3RouteType2Cost_Object = MibTableColumn
futOspfv3RouteType2Cost = _FutOspfv3RouteType2Cost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 9),
    _FutOspfv3RouteType2Cost_Type()
)
futOspfv3RouteType2Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3RouteType2Cost.setStatus("current")


class _FutOspfv3RouteInterfaceIndex_Type(Integer32):
    """Custom type futOspfv3RouteInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FutOspfv3RouteInterfaceIndex_Type.__name__ = "Integer32"
_FutOspfv3RouteInterfaceIndex_Object = MibTableColumn
futOspfv3RouteInterfaceIndex = _FutOspfv3RouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 3, 1, 10),
    _FutOspfv3RouteInterfaceIndex_Type()
)
futOspfv3RouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3RouteInterfaceIndex.setStatus("current")
_FutOspfv3AsExternalAggregationTable_Object = MibTable
futOspfv3AsExternalAggregationTable = _FutOspfv3AsExternalAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4)
)
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationTable.setStatus("current")
_FutOspfv3AsExternalAggregationEntry_Object = MibTableRow
futOspfv3AsExternalAggregationEntry = _FutOspfv3AsExternalAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1)
)
futOspfv3AsExternalAggregationEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3AsExternalAggregationNetType"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3AsExternalAggregationNet"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3AsExternalAggregationPfxLength"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3AsExternalAggregationAreaId"),
)
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationEntry.setStatus("current")
_FutOspfv3AsExternalAggregationNetType_Type = InetAddressType
_FutOspfv3AsExternalAggregationNetType_Object = MibTableColumn
futOspfv3AsExternalAggregationNetType = _FutOspfv3AsExternalAggregationNetType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 1),
    _FutOspfv3AsExternalAggregationNetType_Type()
)
futOspfv3AsExternalAggregationNetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationNetType.setStatus("current")


class _FutOspfv3AsExternalAggregationNet_Type(InetAddress):
    """Custom type futOspfv3AsExternalAggregationNet based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3AsExternalAggregationNet_Type.__name__ = "InetAddress"
_FutOspfv3AsExternalAggregationNet_Object = MibTableColumn
futOspfv3AsExternalAggregationNet = _FutOspfv3AsExternalAggregationNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 2),
    _FutOspfv3AsExternalAggregationNet_Type()
)
futOspfv3AsExternalAggregationNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationNet.setStatus("current")
_FutOspfv3AsExternalAggregationPfxLength_Type = InetAddressPrefixLength
_FutOspfv3AsExternalAggregationPfxLength_Object = MibTableColumn
futOspfv3AsExternalAggregationPfxLength = _FutOspfv3AsExternalAggregationPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 3),
    _FutOspfv3AsExternalAggregationPfxLength_Type()
)
futOspfv3AsExternalAggregationPfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationPfxLength.setStatus("current")
_FutOspfv3AsExternalAggregationAreaId_Type = AreaID
_FutOspfv3AsExternalAggregationAreaId_Object = MibTableColumn
futOspfv3AsExternalAggregationAreaId = _FutOspfv3AsExternalAggregationAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 4),
    _FutOspfv3AsExternalAggregationAreaId_Type()
)
futOspfv3AsExternalAggregationAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationAreaId.setStatus("current")


class _FutOspfv3AsExternalAggregationEffect_Type(Integer32):
    """Custom type futOspfv3AsExternalAggregationEffect based on Integer32"""
    defaultValue = 1

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
        *(("advertise", 1),
          ("doNotAdvertise", 2),
          ("allowAll", 3),
          ("denyAll", 4))
    )


_FutOspfv3AsExternalAggregationEffect_Type.__name__ = "Integer32"
_FutOspfv3AsExternalAggregationEffect_Object = MibTableColumn
futOspfv3AsExternalAggregationEffect = _FutOspfv3AsExternalAggregationEffect_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 5),
    _FutOspfv3AsExternalAggregationEffect_Type()
)
futOspfv3AsExternalAggregationEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationEffect.setStatus("current")


class _FutOspfv3AsExternalAggregationTranslation_Type(Integer32):
    """Custom type futOspfv3AsExternalAggregationTranslation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FutOspfv3AsExternalAggregationTranslation_Type.__name__ = "Integer32"
_FutOspfv3AsExternalAggregationTranslation_Object = MibTableColumn
futOspfv3AsExternalAggregationTranslation = _FutOspfv3AsExternalAggregationTranslation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 6),
    _FutOspfv3AsExternalAggregationTranslation_Type()
)
futOspfv3AsExternalAggregationTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationTranslation.setStatus("current")
_FutOspfv3AsExternalAggregationStatus_Type = RowStatus
_FutOspfv3AsExternalAggregationStatus_Object = MibTableColumn
futOspfv3AsExternalAggregationStatus = _FutOspfv3AsExternalAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 4, 1, 7),
    _FutOspfv3AsExternalAggregationStatus_Type()
)
futOspfv3AsExternalAggregationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfv3AsExternalAggregationStatus.setStatus("current")
_FutOspfv3BRRouteTable_Object = MibTable
futOspfv3BRRouteTable = _FutOspfv3BRRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5)
)
if mibBuilder.loadTexts:
    futOspfv3BRRouteTable.setStatus("current")
_FutOspfv3BRRouteEntry_Object = MibTableRow
futOspfv3BRRouteEntry = _FutOspfv3BRRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1)
)
futOspfv3BRRouteEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3BRRouteDest"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3BRRouteNextHopType"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3BRRouteNextHop"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3BRRouteDestType"),
)
if mibBuilder.loadTexts:
    futOspfv3BRRouteEntry.setStatus("current")
_FutOspfv3BRRouteDest_Type = IpAddress
_FutOspfv3BRRouteDest_Object = MibTableColumn
futOspfv3BRRouteDest = _FutOspfv3BRRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 1),
    _FutOspfv3BRRouteDest_Type()
)
futOspfv3BRRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3BRRouteDest.setStatus("current")
_FutOspfv3BRRouteNextHopType_Type = InetAddressType
_FutOspfv3BRRouteNextHopType_Object = MibTableColumn
futOspfv3BRRouteNextHopType = _FutOspfv3BRRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 2),
    _FutOspfv3BRRouteNextHopType_Type()
)
futOspfv3BRRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3BRRouteNextHopType.setStatus("current")


class _FutOspfv3BRRouteNextHop_Type(InetAddress):
    """Custom type futOspfv3BRRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3BRRouteNextHop_Type.__name__ = "InetAddress"
_FutOspfv3BRRouteNextHop_Object = MibTableColumn
futOspfv3BRRouteNextHop = _FutOspfv3BRRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 3),
    _FutOspfv3BRRouteNextHop_Type()
)
futOspfv3BRRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3BRRouteNextHop.setStatus("current")


class _FutOspfv3BRRouteDestType_Type(Integer32):
    """Custom type futOspfv3BRRouteDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("areaBorder", 2),
          ("asBoundary", 3))
    )


_FutOspfv3BRRouteDestType_Type.__name__ = "Integer32"
_FutOspfv3BRRouteDestType_Object = MibTableColumn
futOspfv3BRRouteDestType = _FutOspfv3BRRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 4),
    _FutOspfv3BRRouteDestType_Type()
)
futOspfv3BRRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3BRRouteDestType.setStatus("current")


class _FutOspfv3BRRouteType_Type(Integer32):
    """Custom type futOspfv3BRRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intraArea", 1),
          ("interArea", 2))
    )


_FutOspfv3BRRouteType_Type.__name__ = "Integer32"
_FutOspfv3BRRouteType_Object = MibTableColumn
futOspfv3BRRouteType = _FutOspfv3BRRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 5),
    _FutOspfv3BRRouteType_Type()
)
futOspfv3BRRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3BRRouteType.setStatus("current")
_FutOspfv3BRRouteAreaId_Type = AreaID
_FutOspfv3BRRouteAreaId_Object = MibTableColumn
futOspfv3BRRouteAreaId = _FutOspfv3BRRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 6),
    _FutOspfv3BRRouteAreaId_Type()
)
futOspfv3BRRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3BRRouteAreaId.setStatus("current")
_FutOspfv3BRRouteCost_Type = BigMetric
_FutOspfv3BRRouteCost_Object = MibTableColumn
futOspfv3BRRouteCost = _FutOspfv3BRRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 7),
    _FutOspfv3BRRouteCost_Type()
)
futOspfv3BRRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3BRRouteCost.setStatus("current")
_FutOspfv3BRRouteInterfaceIndex_Type = InterfaceIndex
_FutOspfv3BRRouteInterfaceIndex_Object = MibTableColumn
futOspfv3BRRouteInterfaceIndex = _FutOspfv3BRRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 5, 1, 8),
    _FutOspfv3BRRouteInterfaceIndex_Type()
)
futOspfv3BRRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfv3BRRouteInterfaceIndex.setStatus("current")
_FutOspfv3RedistRouteCfgTable_Object = MibTable
futOspfv3RedistRouteCfgTable = _FutOspfv3RedistRouteCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6)
)
if mibBuilder.loadTexts:
    futOspfv3RedistRouteCfgTable.setStatus("current")
_FutOspfv3RedistRouteCfgEntry_Object = MibTableRow
futOspfv3RedistRouteCfgEntry = _FutOspfv3RedistRouteCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1)
)
futOspfv3RedistRouteCfgEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RedistRouteDestType"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RedistRouteDest"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3RedistRoutePfxLength"),
)
if mibBuilder.loadTexts:
    futOspfv3RedistRouteCfgEntry.setStatus("current")
_FutOspfv3RedistRouteDestType_Type = InetAddressType
_FutOspfv3RedistRouteDestType_Object = MibTableColumn
futOspfv3RedistRouteDestType = _FutOspfv3RedistRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 1),
    _FutOspfv3RedistRouteDestType_Type()
)
futOspfv3RedistRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteDestType.setStatus("current")


class _FutOspfv3RedistRouteDest_Type(InetAddress):
    """Custom type futOspfv3RedistRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FutOspfv3RedistRouteDest_Type.__name__ = "InetAddress"
_FutOspfv3RedistRouteDest_Object = MibTableColumn
futOspfv3RedistRouteDest = _FutOspfv3RedistRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 2),
    _FutOspfv3RedistRouteDest_Type()
)
futOspfv3RedistRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteDest.setStatus("current")
_FutOspfv3RedistRoutePfxLength_Type = InetAddressPrefixLength
_FutOspfv3RedistRoutePfxLength_Object = MibTableColumn
futOspfv3RedistRoutePfxLength = _FutOspfv3RedistRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 3),
    _FutOspfv3RedistRoutePfxLength_Type()
)
futOspfv3RedistRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3RedistRoutePfxLength.setStatus("current")


class _FutOspfv3RedistRouteMetric_Type(BigMetric):
    """Custom type futOspfv3RedistRouteMetric based on BigMetric"""
    defaultValue = 10


_FutOspfv3RedistRouteMetric_Type.__name__ = "BigMetric"
_FutOspfv3RedistRouteMetric_Object = MibTableColumn
futOspfv3RedistRouteMetric = _FutOspfv3RedistRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 4),
    _FutOspfv3RedistRouteMetric_Type()
)
futOspfv3RedistRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteMetric.setStatus("current")


class _FutOspfv3RedistRouteMetricType_Type(Integer32):
    """Custom type futOspfv3RedistRouteMetricType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("type1External", 3),
          ("type2External", 4))
    )


_FutOspfv3RedistRouteMetricType_Type.__name__ = "Integer32"
_FutOspfv3RedistRouteMetricType_Object = MibTableColumn
futOspfv3RedistRouteMetricType = _FutOspfv3RedistRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 5),
    _FutOspfv3RedistRouteMetricType_Type()
)
futOspfv3RedistRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteMetricType.setStatus("current")


class _FutOspfv3RedistRouteTagType_Type(Integer32):
    """Custom type futOspfv3RedistRouteTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_FutOspfv3RedistRouteTagType_Type.__name__ = "Integer32"
_FutOspfv3RedistRouteTagType_Object = MibTableColumn
futOspfv3RedistRouteTagType = _FutOspfv3RedistRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 6),
    _FutOspfv3RedistRouteTagType_Type()
)
futOspfv3RedistRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteTagType.setStatus("current")


class _FutOspfv3RedistRouteTag_Type(Integer32):
    """Custom type futOspfv3RedistRouteTag based on Integer32"""
    defaultValue = 0


_FutOspfv3RedistRouteTag_Type.__name__ = "Integer32"
_FutOspfv3RedistRouteTag_Object = MibTableColumn
futOspfv3RedistRouteTag = _FutOspfv3RedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 7),
    _FutOspfv3RedistRouteTag_Type()
)
futOspfv3RedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteTag.setStatus("current")
_FutOspfv3RedistRouteStatus_Type = RowStatus
_FutOspfv3RedistRouteStatus_Object = MibTableColumn
futOspfv3RedistRouteStatus = _FutOspfv3RedistRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 6, 1, 8),
    _FutOspfv3RedistRouteStatus_Type()
)
futOspfv3RedistRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfv3RedistRouteStatus.setStatus("current")
_Futospfv3RRDGroup_ObjectIdentity = ObjectIdentity
futospfv3RRDGroup = _Futospfv3RRDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 7)
)
_FutOspfv3RRDGeneralGroup_ObjectIdentity = ObjectIdentity
futOspfv3RRDGeneralGroup = _FutOspfv3RRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 7, 1)
)


class _FutOspfv3RRDStatus_Type(Status):
    """Custom type futOspfv3RRDStatus based on Status"""
    defaultValue = 2


_FutOspfv3RRDStatus_Type.__name__ = "Status"
_FutOspfv3RRDStatus_Object = MibScalar
futOspfv3RRDStatus = _FutOspfv3RRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 7, 1, 1),
    _FutOspfv3RRDStatus_Type()
)
futOspfv3RRDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RRDStatus.setStatus("current")


class _FutOspfv3RRDSrcProtoMask_Type(Integer32):
    """Custom type futOspfv3RRDSrcProtoMask based on Integer32"""
    defaultValue = 0


_FutOspfv3RRDSrcProtoMask_Type.__name__ = "Integer32"
_FutOspfv3RRDSrcProtoMask_Object = MibScalar
futOspfv3RRDSrcProtoMask = _FutOspfv3RRDSrcProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 7, 1, 2),
    _FutOspfv3RRDSrcProtoMask_Type()
)
futOspfv3RRDSrcProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RRDSrcProtoMask.setStatus("current")


class _FutOspfv3RRDRouteMapName_Type(OctetString):
    """Custom type futOspfv3RRDRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FutOspfv3RRDRouteMapName_Type.__name__ = "OctetString"
_FutOspfv3RRDRouteMapName_Object = MibScalar
futOspfv3RRDRouteMapName = _FutOspfv3RRDRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 7, 1, 3),
    _FutOspfv3RRDRouteMapName_Type()
)
futOspfv3RRDRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3RRDRouteMapName.setStatus("current")
_Futospfv3DistInOutRouteMap_ObjectIdentity = ObjectIdentity
futospfv3DistInOutRouteMap = _Futospfv3DistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8)
)
_FutOspfv3DistInOutRouteMapTable_Object = MibTable
futOspfv3DistInOutRouteMapTable = _FutOspfv3DistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1)
)
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapTable.setStatus("current")
_FutOspfv3DistInOutRouteMapEntry_Object = MibTableRow
futOspfv3DistInOutRouteMapEntry = _FutOspfv3DistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1, 1)
)
futOspfv3DistInOutRouteMapEntry.setIndexNames(
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3DistInOutRouteMapName"),
    (0, "SUPERMICRO-OSPFV3-MIB", "futOspfv3DistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapEntry.setStatus("current")


class _FutOspfv3DistInOutRouteMapName_Type(DisplayString):
    """Custom type futOspfv3DistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FutOspfv3DistInOutRouteMapName_Type.__name__ = "DisplayString"
_FutOspfv3DistInOutRouteMapName_Object = MibTableColumn
futOspfv3DistInOutRouteMapName = _FutOspfv3DistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1, 1, 1),
    _FutOspfv3DistInOutRouteMapName_Type()
)
futOspfv3DistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapName.setStatus("current")


class _FutOspfv3DistInOutRouteMapType_Type(Integer32):
    """Custom type futOspfv3DistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FutOspfv3DistInOutRouteMapType_Type.__name__ = "Integer32"
_FutOspfv3DistInOutRouteMapType_Object = MibTableColumn
futOspfv3DistInOutRouteMapType = _FutOspfv3DistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1, 1, 2),
    _FutOspfv3DistInOutRouteMapType_Type()
)
futOspfv3DistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapType.setStatus("current")


class _FutOspfv3DistInOutRouteMapValue_Type(Integer32):
    """Custom type futOspfv3DistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FutOspfv3DistInOutRouteMapValue_Type.__name__ = "Integer32"
_FutOspfv3DistInOutRouteMapValue_Object = MibTableColumn
futOspfv3DistInOutRouteMapValue = _FutOspfv3DistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1, 1, 3),
    _FutOspfv3DistInOutRouteMapValue_Type()
)
futOspfv3DistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapValue.setStatus("current")
_FutOspfv3DistInOutRouteMapRowStatus_Type = RowStatus
_FutOspfv3DistInOutRouteMapRowStatus_Object = MibTableColumn
futOspfv3DistInOutRouteMapRowStatus = _FutOspfv3DistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 8, 1, 1, 4),
    _FutOspfv3DistInOutRouteMapRowStatus_Type()
)
futOspfv3DistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfv3DistInOutRouteMapRowStatus.setStatus("current")
_Futospf3PreferenceGroup_ObjectIdentity = ObjectIdentity
futospf3PreferenceGroup = _Futospf3PreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 9)
)


class _FutOspf3PreferenceValue_Type(Integer32):
    """Custom type futOspf3PreferenceValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspf3PreferenceValue_Type.__name__ = "Integer32"
_FutOspf3PreferenceValue_Object = MibScalar
futOspf3PreferenceValue = _FutOspf3PreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 9, 1),
    _FutOspf3PreferenceValue_Type()
)
futOspf3PreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspf3PreferenceValue.setStatus("current")
_FutOspfv3Notification_ObjectIdentity = ObjectIdentity
futOspfv3Notification = _FutOspfv3Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101)
)
_FutOspfv3Traps_ObjectIdentity = ObjectIdentity
futOspfv3Traps = _FutOspfv3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0)
)
_FutOspfv3TrapObject_ObjectIdentity = ObjectIdentity
futOspfv3TrapObject = _FutOspfv3TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1)
)
_FutOspfv3TrapNbrIfIndex_Type = InterfaceIndex
_FutOspfv3TrapNbrIfIndex_Object = MibScalar
futOspfv3TrapNbrIfIndex = _FutOspfv3TrapNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1, 1),
    _FutOspfv3TrapNbrIfIndex_Type()
)
futOspfv3TrapNbrIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    futOspfv3TrapNbrIfIndex.setStatus("current")
_FutOspfv3TrapVirtNbrRtrId_Type = RouterID
_FutOspfv3TrapVirtNbrRtrId_Object = MibScalar
futOspfv3TrapVirtNbrRtrId = _FutOspfv3TrapVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1, 2),
    _FutOspfv3TrapVirtNbrRtrId_Type()
)
futOspfv3TrapVirtNbrRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    futOspfv3TrapVirtNbrRtrId.setStatus("current")
_FutOspfv3TrapNbrRtrId_Type = RouterID
_FutOspfv3TrapNbrRtrId_Object = MibScalar
futOspfv3TrapNbrRtrId = _FutOspfv3TrapNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1, 3),
    _FutOspfv3TrapNbrRtrId_Type()
)
futOspfv3TrapNbrRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    futOspfv3TrapNbrRtrId.setStatus("current")
_FutOspfv3TrapVirtNbrArea_Type = AreaID
_FutOspfv3TrapVirtNbrArea_Object = MibScalar
futOspfv3TrapVirtNbrArea = _FutOspfv3TrapVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1, 4),
    _FutOspfv3TrapVirtNbrArea_Type()
)
futOspfv3TrapVirtNbrArea.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    futOspfv3TrapVirtNbrArea.setStatus("current")


class _FutOspfv3TrapBulkUpdAbortReason_Type(Integer32):
    """Custom type futOspfv3TrapBulkUpdAbortReason based on Integer32"""
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
        *(("none", 1),
          ("memAllocFailed", 2),
          ("sendFailed", 3),
          ("processFailed", 4))
    )


_FutOspfv3TrapBulkUpdAbortReason_Type.__name__ = "Integer32"
_FutOspfv3TrapBulkUpdAbortReason_Object = MibScalar
futOspfv3TrapBulkUpdAbortReason = _FutOspfv3TrapBulkUpdAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 1, 5),
    _FutOspfv3TrapBulkUpdAbortReason_Type()
)
futOspfv3TrapBulkUpdAbortReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    futOspfv3TrapBulkUpdAbortReason.setStatus("current")

# Managed Objects groups


# Notification objects

futOspfv3RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0, 1)
)
futOspfv3RestartStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3RestartStatus"),
        ("OSPFV3-MIB", "ospfv3RestartInterval"),
        ("OSPFV3-MIB", "ospfv3RestartExitReason"))
)
if mibBuilder.loadTexts:
    futOspfv3RestartStatusChange.setStatus(
        "current"
    )

futOspfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0, 2)
)
futOspfv3NbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3TrapNbrIfIndex"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3TrapNbrRtrId"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    futOspfv3NbrRestartHelperStatusChange.setStatus(
        "current"
    )

futOspfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0, 3)
)
futOspfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3TrapVirtNbrArea"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3TrapVirtNbrRtrId"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    futOspfv3VirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )

futOspfv3HotStandbyStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0, 4)
)
futOspfv3HotStandbyStateChgTrap.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3HotStandbyState"))
)
if mibBuilder.loadTexts:
    futOspfv3HotStandbyStateChgTrap.setStatus(
        "current"
    )

futOspfv3HotStandbyBulkUpdAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 90, 101, 0, 5)
)
futOspfv3HotStandbyBulkUpdAbortTrap.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3DynamicBulkUpdStatus"),
        ("SUPERMICRO-OSPFV3-MIB", "futOspfv3TrapBulkUpdAbortReason"))
)
if mibBuilder.loadTexts:
    futOspfv3HotStandbyBulkUpdAbortTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFV3-MIB",
    **{"futospfv3": futospfv3,
       "futospfv3GeneralGroup": futospfv3GeneralGroup,
       "futOspfv3OverFlowState": futOspfv3OverFlowState,
       "futOspfv3TraceLevel": futOspfv3TraceLevel,
       "futOspfv3ABRType": futOspfv3ABRType,
       "futOspfv3NssaAsbrDefRtTrans": futOspfv3NssaAsbrDefRtTrans,
       "futOspfv3DefaultPassiveInterface": futOspfv3DefaultPassiveInterface,
       "futOspfv3SpfDelay": futOspfv3SpfDelay,
       "futOspfv3SpfHoldTime": futOspfv3SpfHoldTime,
       "futOspfv3RTStaggeringInterval": futOspfv3RTStaggeringInterval,
       "futOspfv3RTStaggeringStatus": futOspfv3RTStaggeringStatus,
       "futOspfv3RestartStrictLsaChecking": futOspfv3RestartStrictLsaChecking,
       "futOspfv3HelperSupport": futOspfv3HelperSupport,
       "futOspfv3HelperGraceTimeLimit": futOspfv3HelperGraceTimeLimit,
       "futOspfv3RestartAckState": futOspfv3RestartAckState,
       "futOspfv3GraceLsaRetransmitCount": futOspfv3GraceLsaRetransmitCount,
       "futOspfv3RestartReason": futOspfv3RestartReason,
       "futOspfv3ExtTraceLevel": futOspfv3ExtTraceLevel,
       "futOspfv3SetTraps": futOspfv3SetTraps,
       "futOspfv3HotStandbyAdminStatus": futOspfv3HotStandbyAdminStatus,
       "futOspfv3HotStandbyState": futOspfv3HotStandbyState,
       "futOspfv3DynamicBulkUpdStatus": futOspfv3DynamicBulkUpdStatus,
       "futOspfv3StandbyHelloSyncCount": futOspfv3StandbyHelloSyncCount,
       "futOspfv3StandbyLsaSyncCount": futOspfv3StandbyLsaSyncCount,
       "futOspfv3IfTable": futOspfv3IfTable,
       "futOspfv3IfEntry": futOspfv3IfEntry,
       "futOspfv3IfIndex": futOspfv3IfIndex,
       "futOspfv3IfOperState": futOspfv3IfOperState,
       "futOspfv3IfPassive": futOspfv3IfPassive,
       "futOspfv3IfNbrCount": futOspfv3IfNbrCount,
       "futOspfv3IfAdjCount": futOspfv3IfAdjCount,
       "futOspfv3IfHelloRcvd": futOspfv3IfHelloRcvd,
       "futOspfv3IfHelloTxed": futOspfv3IfHelloTxed,
       "futOspfv3IfHelloDisd": futOspfv3IfHelloDisd,
       "futOspfv3IfDdpRcvd": futOspfv3IfDdpRcvd,
       "futOspfv3IfDdpTxed": futOspfv3IfDdpTxed,
       "futOspfv3IfDdpDisd": futOspfv3IfDdpDisd,
       "futOspfv3IfLrqRcvd": futOspfv3IfLrqRcvd,
       "futOspfv3IfLrqTxed": futOspfv3IfLrqTxed,
       "futOspfv3IfLrqDisd": futOspfv3IfLrqDisd,
       "futOspfv3IfLsuRcvd": futOspfv3IfLsuRcvd,
       "futOspfv3IfLsuTxed": futOspfv3IfLsuTxed,
       "futOspfv3IfLsuDisd": futOspfv3IfLsuDisd,
       "futOspfv3IfLakRcvd": futOspfv3IfLakRcvd,
       "futOspfv3IfLakTxed": futOspfv3IfLakTxed,
       "futOspfv3IfLakDisd": futOspfv3IfLakDisd,
       "futOspfv3IfLinkLSASuppression": futOspfv3IfLinkLSASuppression,
       "futOspfv3RoutingTable": futOspfv3RoutingTable,
       "futOspfv3RoutingEntry": futOspfv3RoutingEntry,
       "futOspfv3RouteDestType": futOspfv3RouteDestType,
       "futOspfv3RouteDest": futOspfv3RouteDest,
       "futOspfv3RoutePfxLength": futOspfv3RoutePfxLength,
       "futOspfv3RouteNextHopType": futOspfv3RouteNextHopType,
       "futOspfv3RouteNextHop": futOspfv3RouteNextHop,
       "futOspfv3RouteType": futOspfv3RouteType,
       "futOspfv3RouteAreaId": futOspfv3RouteAreaId,
       "futOspfv3RouteCost": futOspfv3RouteCost,
       "futOspfv3RouteType2Cost": futOspfv3RouteType2Cost,
       "futOspfv3RouteInterfaceIndex": futOspfv3RouteInterfaceIndex,
       "futOspfv3AsExternalAggregationTable": futOspfv3AsExternalAggregationTable,
       "futOspfv3AsExternalAggregationEntry": futOspfv3AsExternalAggregationEntry,
       "futOspfv3AsExternalAggregationNetType": futOspfv3AsExternalAggregationNetType,
       "futOspfv3AsExternalAggregationNet": futOspfv3AsExternalAggregationNet,
       "futOspfv3AsExternalAggregationPfxLength": futOspfv3AsExternalAggregationPfxLength,
       "futOspfv3AsExternalAggregationAreaId": futOspfv3AsExternalAggregationAreaId,
       "futOspfv3AsExternalAggregationEffect": futOspfv3AsExternalAggregationEffect,
       "futOspfv3AsExternalAggregationTranslation": futOspfv3AsExternalAggregationTranslation,
       "futOspfv3AsExternalAggregationStatus": futOspfv3AsExternalAggregationStatus,
       "futOspfv3BRRouteTable": futOspfv3BRRouteTable,
       "futOspfv3BRRouteEntry": futOspfv3BRRouteEntry,
       "futOspfv3BRRouteDest": futOspfv3BRRouteDest,
       "futOspfv3BRRouteNextHopType": futOspfv3BRRouteNextHopType,
       "futOspfv3BRRouteNextHop": futOspfv3BRRouteNextHop,
       "futOspfv3BRRouteDestType": futOspfv3BRRouteDestType,
       "futOspfv3BRRouteType": futOspfv3BRRouteType,
       "futOspfv3BRRouteAreaId": futOspfv3BRRouteAreaId,
       "futOspfv3BRRouteCost": futOspfv3BRRouteCost,
       "futOspfv3BRRouteInterfaceIndex": futOspfv3BRRouteInterfaceIndex,
       "futOspfv3RedistRouteCfgTable": futOspfv3RedistRouteCfgTable,
       "futOspfv3RedistRouteCfgEntry": futOspfv3RedistRouteCfgEntry,
       "futOspfv3RedistRouteDestType": futOspfv3RedistRouteDestType,
       "futOspfv3RedistRouteDest": futOspfv3RedistRouteDest,
       "futOspfv3RedistRoutePfxLength": futOspfv3RedistRoutePfxLength,
       "futOspfv3RedistRouteMetric": futOspfv3RedistRouteMetric,
       "futOspfv3RedistRouteMetricType": futOspfv3RedistRouteMetricType,
       "futOspfv3RedistRouteTagType": futOspfv3RedistRouteTagType,
       "futOspfv3RedistRouteTag": futOspfv3RedistRouteTag,
       "futOspfv3RedistRouteStatus": futOspfv3RedistRouteStatus,
       "futospfv3RRDGroup": futospfv3RRDGroup,
       "futOspfv3RRDGeneralGroup": futOspfv3RRDGeneralGroup,
       "futOspfv3RRDStatus": futOspfv3RRDStatus,
       "futOspfv3RRDSrcProtoMask": futOspfv3RRDSrcProtoMask,
       "futOspfv3RRDRouteMapName": futOspfv3RRDRouteMapName,
       "futospfv3DistInOutRouteMap": futospfv3DistInOutRouteMap,
       "futOspfv3DistInOutRouteMapTable": futOspfv3DistInOutRouteMapTable,
       "futOspfv3DistInOutRouteMapEntry": futOspfv3DistInOutRouteMapEntry,
       "futOspfv3DistInOutRouteMapName": futOspfv3DistInOutRouteMapName,
       "futOspfv3DistInOutRouteMapType": futOspfv3DistInOutRouteMapType,
       "futOspfv3DistInOutRouteMapValue": futOspfv3DistInOutRouteMapValue,
       "futOspfv3DistInOutRouteMapRowStatus": futOspfv3DistInOutRouteMapRowStatus,
       "futospf3PreferenceGroup": futospf3PreferenceGroup,
       "futOspf3PreferenceValue": futOspf3PreferenceValue,
       "futOspfv3Notification": futOspfv3Notification,
       "futOspfv3Traps": futOspfv3Traps,
       "futOspfv3RestartStatusChange": futOspfv3RestartStatusChange,
       "futOspfv3NbrRestartHelperStatusChange": futOspfv3NbrRestartHelperStatusChange,
       "futOspfv3VirtNbrRestartHelperStatusChange": futOspfv3VirtNbrRestartHelperStatusChange,
       "futOspfv3HotStandbyStateChgTrap": futOspfv3HotStandbyStateChgTrap,
       "futOspfv3HotStandbyBulkUpdAbortTrap": futOspfv3HotStandbyBulkUpdAbortTrap,
       "futOspfv3TrapObject": futOspfv3TrapObject,
       "futOspfv3TrapNbrIfIndex": futOspfv3TrapNbrIfIndex,
       "futOspfv3TrapVirtNbrRtrId": futOspfv3TrapVirtNbrRtrId,
       "futOspfv3TrapNbrRtrId": futOspfv3TrapNbrRtrId,
       "futOspfv3TrapVirtNbrArea": futOspfv3TrapVirtNbrArea,
       "futOspfv3TrapBulkUpdAbortReason": futOspfv3TrapBulkUpdAbortReason}
)
