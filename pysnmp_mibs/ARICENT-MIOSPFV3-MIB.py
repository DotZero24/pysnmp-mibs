# SNMP MIB module (ARICENT-MIOSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MIOSPFV3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:57 2025
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

(fsMIStdOspfv3ContextId,
 fsMIStdOspfv3Entry,
 fsMIStdOspfv3NbrEntry,
 fsMIStdOspfv3NbrRestartHelperAge,
 fsMIStdOspfv3NbrRestartHelperExitReason,
 fsMIStdOspfv3NbrRestartHelperStatus,
 fsMIStdOspfv3RestartExitReason,
 fsMIStdOspfv3RestartInterval,
 fsMIStdOspfv3RestartStatus,
 fsMIStdOspfv3RouterId,
 fsMIStdOspfv3VirtIfEntry,
 fsMIStdOspfv3VirtNbrRestartHelperAge,
 fsMIStdOspfv3VirtNbrRestartHelperExitReason,
 fsMIStdOspfv3VirtNbrRestartHelperStatus) = mibBuilder.importSymbols(
    "ARICENT-MISTDOSPFV3-MIB",
    "fsMIStdOspfv3ContextId",
    "fsMIStdOspfv3Entry",
    "fsMIStdOspfv3NbrEntry",
    "fsMIStdOspfv3NbrRestartHelperAge",
    "fsMIStdOspfv3NbrRestartHelperExitReason",
    "fsMIStdOspfv3NbrRestartHelperStatus",
    "fsMIStdOspfv3RestartExitReason",
    "fsMIStdOspfv3RestartInterval",
    "fsMIStdOspfv3RestartStatus",
    "fsMIStdOspfv3RouterId",
    "fsMIStdOspfv3VirtIfEntry",
    "fsMIStdOspfv3VirtNbrRestartHelperAge",
    "fsMIStdOspfv3VirtNbrRestartHelperExitReason",
    "fsMIStdOspfv3VirtNbrRestartHelperStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMIOspfv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24)
)
if mibBuilder.loadTexts:
    fsMIOspfv3.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
fsMIOspfv3GeneralGroup = _FsMIOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1)
)
_FsMIOspfv3GlobalTraceLevel_Type = Integer32
_FsMIOspfv3GlobalTraceLevel_Object = MibScalar
fsMIOspfv3GlobalTraceLevel = _FsMIOspfv3GlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 1),
    _FsMIOspfv3GlobalTraceLevel_Type()
)
fsMIOspfv3GlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3GlobalTraceLevel.setStatus("current")


class _FsMIOspfv3VrfSpfInterval_Type(Integer32):
    """Custom type fsMIOspfv3VrfSpfInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_FsMIOspfv3VrfSpfInterval_Type.__name__ = "Integer32"
_FsMIOspfv3VrfSpfInterval_Object = MibScalar
fsMIOspfv3VrfSpfInterval = _FsMIOspfv3VrfSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 2),
    _FsMIOspfv3VrfSpfInterval_Type()
)
fsMIOspfv3VrfSpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VrfSpfInterval.setStatus("current")


class _FsMIOspfv3RTStaggeringStatus_Type(Integer32):
    """Custom type fsMIOspfv3RTStaggeringStatus based on Integer32"""
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


_FsMIOspfv3RTStaggeringStatus_Type.__name__ = "Integer32"
_FsMIOspfv3RTStaggeringStatus_Object = MibScalar
fsMIOspfv3RTStaggeringStatus = _FsMIOspfv3RTStaggeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 3),
    _FsMIOspfv3RTStaggeringStatus_Type()
)
fsMIOspfv3RTStaggeringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RTStaggeringStatus.setStatus("current")


class _FsMIOspfv3HotStandbyAdminStatus_Type(Integer32):
    """Custom type fsMIOspfv3HotStandbyAdminStatus based on Integer32"""
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


_FsMIOspfv3HotStandbyAdminStatus_Type.__name__ = "Integer32"
_FsMIOspfv3HotStandbyAdminStatus_Object = MibScalar
fsMIOspfv3HotStandbyAdminStatus = _FsMIOspfv3HotStandbyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 4),
    _FsMIOspfv3HotStandbyAdminStatus_Type()
)
fsMIOspfv3HotStandbyAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3HotStandbyAdminStatus.setStatus("current")


class _FsMIOspfv3HotStandbyState_Type(Integer32):
    """Custom type fsMIOspfv3HotStandbyState based on Integer32"""
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


_FsMIOspfv3HotStandbyState_Type.__name__ = "Integer32"
_FsMIOspfv3HotStandbyState_Object = MibScalar
fsMIOspfv3HotStandbyState = _FsMIOspfv3HotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 5),
    _FsMIOspfv3HotStandbyState_Type()
)
fsMIOspfv3HotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3HotStandbyState.setStatus("current")


class _FsMIOspfv3DynamicBulkUpdStatus_Type(Integer32):
    """Custom type fsMIOspfv3DynamicBulkUpdStatus based on Integer32"""
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


_FsMIOspfv3DynamicBulkUpdStatus_Type.__name__ = "Integer32"
_FsMIOspfv3DynamicBulkUpdStatus_Object = MibScalar
fsMIOspfv3DynamicBulkUpdStatus = _FsMIOspfv3DynamicBulkUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 6),
    _FsMIOspfv3DynamicBulkUpdStatus_Type()
)
fsMIOspfv3DynamicBulkUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3DynamicBulkUpdStatus.setStatus("current")
_FsMIOspfv3StandbyHelloSyncCount_Type = Counter32
_FsMIOspfv3StandbyHelloSyncCount_Object = MibScalar
fsMIOspfv3StandbyHelloSyncCount = _FsMIOspfv3StandbyHelloSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 7),
    _FsMIOspfv3StandbyHelloSyncCount_Type()
)
fsMIOspfv3StandbyHelloSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3StandbyHelloSyncCount.setStatus("current")
_FsMIOspfv3StandbyLsaSyncCount_Type = Counter32
_FsMIOspfv3StandbyLsaSyncCount_Object = MibScalar
fsMIOspfv3StandbyLsaSyncCount = _FsMIOspfv3StandbyLsaSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 1, 8),
    _FsMIOspfv3StandbyLsaSyncCount_Type()
)
fsMIOspfv3StandbyLsaSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3StandbyLsaSyncCount.setStatus("current")
_FsMIOspfv3Table_Object = MibTable
fsMIOspfv3Table = _FsMIOspfv3Table_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfv3Table.setStatus("current")
_FsMIOspfv3Entry_Object = MibTableRow
fsMIOspfv3Entry = _FsMIOspfv3Entry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3Entry.setStatus("current")


class _FsMIOspfv3OverFlowState_Type(TruthValue):
    """Custom type fsMIOspfv3OverFlowState based on TruthValue"""
    defaultValue = 2


_FsMIOspfv3OverFlowState_Type.__name__ = "TruthValue"
_FsMIOspfv3OverFlowState_Object = MibTableColumn
fsMIOspfv3OverFlowState = _FsMIOspfv3OverFlowState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 1),
    _FsMIOspfv3OverFlowState_Type()
)
fsMIOspfv3OverFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3OverFlowState.setStatus("current")


class _FsMIOspfv3TraceLevel_Type(Integer32):
    """Custom type fsMIOspfv3TraceLevel based on Integer32"""
    defaultValue = 2048


_FsMIOspfv3TraceLevel_Type.__name__ = "Integer32"
_FsMIOspfv3TraceLevel_Object = MibTableColumn
fsMIOspfv3TraceLevel = _FsMIOspfv3TraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 2),
    _FsMIOspfv3TraceLevel_Type()
)
fsMIOspfv3TraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3TraceLevel.setStatus("current")


class _FsMIOspfv3ABRType_Type(Integer32):
    """Custom type fsMIOspfv3ABRType based on Integer32"""
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


_FsMIOspfv3ABRType_Type.__name__ = "Integer32"
_FsMIOspfv3ABRType_Object = MibTableColumn
fsMIOspfv3ABRType = _FsMIOspfv3ABRType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 3),
    _FsMIOspfv3ABRType_Type()
)
fsMIOspfv3ABRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3ABRType.setStatus("current")


class _FsMIOspfv3NssaAsbrDefRtTrans_Type(Integer32):
    """Custom type fsMIOspfv3NssaAsbrDefRtTrans based on Integer32"""
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


_FsMIOspfv3NssaAsbrDefRtTrans_Type.__name__ = "Integer32"
_FsMIOspfv3NssaAsbrDefRtTrans_Object = MibTableColumn
fsMIOspfv3NssaAsbrDefRtTrans = _FsMIOspfv3NssaAsbrDefRtTrans_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 4),
    _FsMIOspfv3NssaAsbrDefRtTrans_Type()
)
fsMIOspfv3NssaAsbrDefRtTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3NssaAsbrDefRtTrans.setStatus("current")


class _FsMIOspfv3DefaultPassiveInterface_Type(TruthValue):
    """Custom type fsMIOspfv3DefaultPassiveInterface based on TruthValue"""
    defaultValue = 2


_FsMIOspfv3DefaultPassiveInterface_Type.__name__ = "TruthValue"
_FsMIOspfv3DefaultPassiveInterface_Object = MibTableColumn
fsMIOspfv3DefaultPassiveInterface = _FsMIOspfv3DefaultPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 5),
    _FsMIOspfv3DefaultPassiveInterface_Type()
)
fsMIOspfv3DefaultPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3DefaultPassiveInterface.setStatus("current")


class _FsMIOspfv3SpfDelay_Type(Integer32):
    """Custom type fsMIOspfv3SpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfv3SpfDelay_Type.__name__ = "Integer32"
_FsMIOspfv3SpfDelay_Object = MibTableColumn
fsMIOspfv3SpfDelay = _FsMIOspfv3SpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 6),
    _FsMIOspfv3SpfDelay_Type()
)
fsMIOspfv3SpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3SpfDelay.setStatus("current")


class _FsMIOspfv3SpfHoldTime_Type(Integer32):
    """Custom type fsMIOspfv3SpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfv3SpfHoldTime_Type.__name__ = "Integer32"
_FsMIOspfv3SpfHoldTime_Object = MibTableColumn
fsMIOspfv3SpfHoldTime = _FsMIOspfv3SpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 7),
    _FsMIOspfv3SpfHoldTime_Type()
)
fsMIOspfv3SpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3SpfHoldTime.setStatus("current")


class _FsMIOspfv3RTStaggeringInterval_Type(Integer32):
    """Custom type fsMIOspfv3RTStaggeringInterval based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_FsMIOspfv3RTStaggeringInterval_Type.__name__ = "Integer32"
_FsMIOspfv3RTStaggeringInterval_Object = MibTableColumn
fsMIOspfv3RTStaggeringInterval = _FsMIOspfv3RTStaggeringInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 8),
    _FsMIOspfv3RTStaggeringInterval_Type()
)
fsMIOspfv3RTStaggeringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RTStaggeringInterval.setStatus("current")


class _FsMIOspfv3RestartStrictLsaChecking_Type(TruthValue):
    """Custom type fsMIOspfv3RestartStrictLsaChecking based on TruthValue"""
    defaultValue = 2


_FsMIOspfv3RestartStrictLsaChecking_Type.__name__ = "TruthValue"
_FsMIOspfv3RestartStrictLsaChecking_Object = MibTableColumn
fsMIOspfv3RestartStrictLsaChecking = _FsMIOspfv3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 9),
    _FsMIOspfv3RestartStrictLsaChecking_Type()
)
fsMIOspfv3RestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RestartStrictLsaChecking.setStatus("current")


class _FsMIOspfv3HelperSupport_Type(Bits):
    """Custom type fsMIOspfv3HelperSupport based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2),
          ("switchToRedundant", 3))
    )

_FsMIOspfv3HelperSupport_Type.__name__ = "Bits"
_FsMIOspfv3HelperSupport_Object = MibTableColumn
fsMIOspfv3HelperSupport = _FsMIOspfv3HelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 10),
    _FsMIOspfv3HelperSupport_Type()
)
fsMIOspfv3HelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3HelperSupport.setStatus("current")


class _FsMIOspfv3HelperGraceTimeLimit_Type(Integer32):
    """Custom type fsMIOspfv3HelperGraceTimeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_FsMIOspfv3HelperGraceTimeLimit_Type.__name__ = "Integer32"
_FsMIOspfv3HelperGraceTimeLimit_Object = MibTableColumn
fsMIOspfv3HelperGraceTimeLimit = _FsMIOspfv3HelperGraceTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 11),
    _FsMIOspfv3HelperGraceTimeLimit_Type()
)
fsMIOspfv3HelperGraceTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3HelperGraceTimeLimit.setStatus("current")


class _FsMIOspfv3RestartAckState_Type(Integer32):
    """Custom type fsMIOspfv3RestartAckState based on Integer32"""
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


_FsMIOspfv3RestartAckState_Type.__name__ = "Integer32"
_FsMIOspfv3RestartAckState_Object = MibTableColumn
fsMIOspfv3RestartAckState = _FsMIOspfv3RestartAckState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 12),
    _FsMIOspfv3RestartAckState_Type()
)
fsMIOspfv3RestartAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RestartAckState.setStatus("current")


class _FsMIOspfv3GraceLsaRetransmitCount_Type(Integer32):
    """Custom type fsMIOspfv3GraceLsaRetransmitCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FsMIOspfv3GraceLsaRetransmitCount_Type.__name__ = "Integer32"
_FsMIOspfv3GraceLsaRetransmitCount_Object = MibTableColumn
fsMIOspfv3GraceLsaRetransmitCount = _FsMIOspfv3GraceLsaRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 13),
    _FsMIOspfv3GraceLsaRetransmitCount_Type()
)
fsMIOspfv3GraceLsaRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3GraceLsaRetransmitCount.setStatus("current")


class _FsMIOspfv3RestartReason_Type(Integer32):
    """Custom type fsMIOspfv3RestartReason based on Integer32"""
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


_FsMIOspfv3RestartReason_Type.__name__ = "Integer32"
_FsMIOspfv3RestartReason_Object = MibTableColumn
fsMIOspfv3RestartReason = _FsMIOspfv3RestartReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 14),
    _FsMIOspfv3RestartReason_Type()
)
fsMIOspfv3RestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RestartReason.setStatus("current")
_FsMIOspfv3ExtTraceLevel_Type = Integer32
_FsMIOspfv3ExtTraceLevel_Object = MibTableColumn
fsMIOspfv3ExtTraceLevel = _FsMIOspfv3ExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 15),
    _FsMIOspfv3ExtTraceLevel_Type()
)
fsMIOspfv3ExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3ExtTraceLevel.setStatus("current")
_FsMIOspfv3SetTraps_Type = Integer32
_FsMIOspfv3SetTraps_Object = MibTableColumn
fsMIOspfv3SetTraps = _FsMIOspfv3SetTraps_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 16),
    _FsMIOspfv3SetTraps_Type()
)
fsMIOspfv3SetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3SetTraps.setStatus("current")


class _FsMIOspfv3BfdStatus_Type(Integer32):
    """Custom type fsMIOspfv3BfdStatus based on Integer32"""
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


_FsMIOspfv3BfdStatus_Type.__name__ = "Integer32"
_FsMIOspfv3BfdStatus_Object = MibTableColumn
fsMIOspfv3BfdStatus = _FsMIOspfv3BfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 17),
    _FsMIOspfv3BfdStatus_Type()
)
fsMIOspfv3BfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3BfdStatus.setStatus("current")


class _FsMIOspfv3BfdAllIfState_Type(Integer32):
    """Custom type fsMIOspfv3BfdAllIfState based on Integer32"""
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


_FsMIOspfv3BfdAllIfState_Type.__name__ = "Integer32"
_FsMIOspfv3BfdAllIfState_Object = MibTableColumn
fsMIOspfv3BfdAllIfState = _FsMIOspfv3BfdAllIfState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 2, 1, 18),
    _FsMIOspfv3BfdAllIfState_Type()
)
fsMIOspfv3BfdAllIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3BfdAllIfState.setStatus("current")
_FsMIOspfv3IfTable_Object = MibTable
fsMIOspfv3IfTable = _FsMIOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3)
)
if mibBuilder.loadTexts:
    fsMIOspfv3IfTable.setStatus("current")
_FsMIOspfv3IfEntry_Object = MibTableRow
fsMIOspfv3IfEntry = _FsMIOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1)
)
fsMIOspfv3IfEntry.setIndexNames(
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3IfIndex"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3IfEntry.setStatus("current")
_FsMIOspfv3IfIndex_Type = InterfaceIndex
_FsMIOspfv3IfIndex_Object = MibTableColumn
fsMIOspfv3IfIndex = _FsMIOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 1),
    _FsMIOspfv3IfIndex_Type()
)
fsMIOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3IfIndex.setStatus("current")


class _FsMIOspfv3IfOperState_Type(Integer32):
    """Custom type fsMIOspfv3IfOperState based on Integer32"""
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


_FsMIOspfv3IfOperState_Type.__name__ = "Integer32"
_FsMIOspfv3IfOperState_Object = MibTableColumn
fsMIOspfv3IfOperState = _FsMIOspfv3IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 2),
    _FsMIOspfv3IfOperState_Type()
)
fsMIOspfv3IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfOperState.setStatus("current")


class _FsMIOspfv3IfPassive_Type(TruthValue):
    """Custom type fsMIOspfv3IfPassive based on TruthValue"""
    defaultValue = 2


_FsMIOspfv3IfPassive_Type.__name__ = "TruthValue"
_FsMIOspfv3IfPassive_Object = MibTableColumn
fsMIOspfv3IfPassive = _FsMIOspfv3IfPassive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 3),
    _FsMIOspfv3IfPassive_Type()
)
fsMIOspfv3IfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfPassive.setStatus("current")
_FsMIOspfv3IfNbrCount_Type = Gauge32
_FsMIOspfv3IfNbrCount_Object = MibTableColumn
fsMIOspfv3IfNbrCount = _FsMIOspfv3IfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 4),
    _FsMIOspfv3IfNbrCount_Type()
)
fsMIOspfv3IfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfNbrCount.setStatus("current")
_FsMIOspfv3IfAdjCount_Type = Gauge32
_FsMIOspfv3IfAdjCount_Object = MibTableColumn
fsMIOspfv3IfAdjCount = _FsMIOspfv3IfAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 5),
    _FsMIOspfv3IfAdjCount_Type()
)
fsMIOspfv3IfAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAdjCount.setStatus("current")
_FsMIOspfv3IfHelloRcvd_Type = Counter32
_FsMIOspfv3IfHelloRcvd_Object = MibTableColumn
fsMIOspfv3IfHelloRcvd = _FsMIOspfv3IfHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 6),
    _FsMIOspfv3IfHelloRcvd_Type()
)
fsMIOspfv3IfHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfHelloRcvd.setStatus("current")
_FsMIOspfv3IfHelloTxed_Type = Counter32
_FsMIOspfv3IfHelloTxed_Object = MibTableColumn
fsMIOspfv3IfHelloTxed = _FsMIOspfv3IfHelloTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 7),
    _FsMIOspfv3IfHelloTxed_Type()
)
fsMIOspfv3IfHelloTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfHelloTxed.setStatus("current")
_FsMIOspfv3IfHelloDisd_Type = Counter32
_FsMIOspfv3IfHelloDisd_Object = MibTableColumn
fsMIOspfv3IfHelloDisd = _FsMIOspfv3IfHelloDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 8),
    _FsMIOspfv3IfHelloDisd_Type()
)
fsMIOspfv3IfHelloDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfHelloDisd.setStatus("current")
_FsMIOspfv3IfDdpRcvd_Type = Counter32
_FsMIOspfv3IfDdpRcvd_Object = MibTableColumn
fsMIOspfv3IfDdpRcvd = _FsMIOspfv3IfDdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 9),
    _FsMIOspfv3IfDdpRcvd_Type()
)
fsMIOspfv3IfDdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfDdpRcvd.setStatus("current")
_FsMIOspfv3IfDdpTxed_Type = Counter32
_FsMIOspfv3IfDdpTxed_Object = MibTableColumn
fsMIOspfv3IfDdpTxed = _FsMIOspfv3IfDdpTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 10),
    _FsMIOspfv3IfDdpTxed_Type()
)
fsMIOspfv3IfDdpTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfDdpTxed.setStatus("current")
_FsMIOspfv3IfDdpDisd_Type = Counter32
_FsMIOspfv3IfDdpDisd_Object = MibTableColumn
fsMIOspfv3IfDdpDisd = _FsMIOspfv3IfDdpDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 11),
    _FsMIOspfv3IfDdpDisd_Type()
)
fsMIOspfv3IfDdpDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfDdpDisd.setStatus("current")
_FsMIOspfv3IfLrqRcvd_Type = Counter32
_FsMIOspfv3IfLrqRcvd_Object = MibTableColumn
fsMIOspfv3IfLrqRcvd = _FsMIOspfv3IfLrqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 12),
    _FsMIOspfv3IfLrqRcvd_Type()
)
fsMIOspfv3IfLrqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLrqRcvd.setStatus("current")
_FsMIOspfv3IfLrqTxed_Type = Counter32
_FsMIOspfv3IfLrqTxed_Object = MibTableColumn
fsMIOspfv3IfLrqTxed = _FsMIOspfv3IfLrqTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 13),
    _FsMIOspfv3IfLrqTxed_Type()
)
fsMIOspfv3IfLrqTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLrqTxed.setStatus("current")
_FsMIOspfv3IfLrqDisd_Type = Counter32
_FsMIOspfv3IfLrqDisd_Object = MibTableColumn
fsMIOspfv3IfLrqDisd = _FsMIOspfv3IfLrqDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 14),
    _FsMIOspfv3IfLrqDisd_Type()
)
fsMIOspfv3IfLrqDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLrqDisd.setStatus("current")
_FsMIOspfv3IfLsuRcvd_Type = Counter32
_FsMIOspfv3IfLsuRcvd_Object = MibTableColumn
fsMIOspfv3IfLsuRcvd = _FsMIOspfv3IfLsuRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 15),
    _FsMIOspfv3IfLsuRcvd_Type()
)
fsMIOspfv3IfLsuRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLsuRcvd.setStatus("current")
_FsMIOspfv3IfLsuTxed_Type = Counter32
_FsMIOspfv3IfLsuTxed_Object = MibTableColumn
fsMIOspfv3IfLsuTxed = _FsMIOspfv3IfLsuTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 16),
    _FsMIOspfv3IfLsuTxed_Type()
)
fsMIOspfv3IfLsuTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLsuTxed.setStatus("current")
_FsMIOspfv3IfLsuDisd_Type = Counter32
_FsMIOspfv3IfLsuDisd_Object = MibTableColumn
fsMIOspfv3IfLsuDisd = _FsMIOspfv3IfLsuDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 17),
    _FsMIOspfv3IfLsuDisd_Type()
)
fsMIOspfv3IfLsuDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLsuDisd.setStatus("current")
_FsMIOspfv3IfLakRcvd_Type = Counter32
_FsMIOspfv3IfLakRcvd_Object = MibTableColumn
fsMIOspfv3IfLakRcvd = _FsMIOspfv3IfLakRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 18),
    _FsMIOspfv3IfLakRcvd_Type()
)
fsMIOspfv3IfLakRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLakRcvd.setStatus("current")
_FsMIOspfv3IfLakTxed_Type = Counter32
_FsMIOspfv3IfLakTxed_Object = MibTableColumn
fsMIOspfv3IfLakTxed = _FsMIOspfv3IfLakTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 19),
    _FsMIOspfv3IfLakTxed_Type()
)
fsMIOspfv3IfLakTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLakTxed.setStatus("current")
_FsMIOspfv3IfLakDisd_Type = Counter32
_FsMIOspfv3IfLakDisd_Object = MibTableColumn
fsMIOspfv3IfLakDisd = _FsMIOspfv3IfLakDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 20),
    _FsMIOspfv3IfLakDisd_Type()
)
fsMIOspfv3IfLakDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLakDisd.setStatus("current")
_FsMIOspfv3IfContextId_Type = Integer32
_FsMIOspfv3IfContextId_Object = MibTableColumn
fsMIOspfv3IfContextId = _FsMIOspfv3IfContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 21),
    _FsMIOspfv3IfContextId_Type()
)
fsMIOspfv3IfContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfContextId.setStatus("current")


class _FsMIOspfv3IfLinkLSASuppression_Type(TruthValue):
    """Custom type fsMIOspfv3IfLinkLSASuppression based on TruthValue"""
    defaultValue = 2


_FsMIOspfv3IfLinkLSASuppression_Type.__name__ = "TruthValue"
_FsMIOspfv3IfLinkLSASuppression_Object = MibTableColumn
fsMIOspfv3IfLinkLSASuppression = _FsMIOspfv3IfLinkLSASuppression_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 22),
    _FsMIOspfv3IfLinkLSASuppression_Type()
)
fsMIOspfv3IfLinkLSASuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfLinkLSASuppression.setStatus("current")


class _FsMIOspfv3IfBfdState_Type(Integer32):
    """Custom type fsMIOspfv3IfBfdState based on Integer32"""
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


_FsMIOspfv3IfBfdState_Type.__name__ = "Integer32"
_FsMIOspfv3IfBfdState_Object = MibTableColumn
fsMIOspfv3IfBfdState = _FsMIOspfv3IfBfdState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 23),
    _FsMIOspfv3IfBfdState_Type()
)
fsMIOspfv3IfBfdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfBfdState.setStatus("current")


class _FsMIOspfv3IfCryptoAuthType_Type(Integer32):
    """Custom type fsMIOspfv3IfCryptoAuthType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5),
          ("none", 6))
    )


_FsMIOspfv3IfCryptoAuthType_Type.__name__ = "Integer32"
_FsMIOspfv3IfCryptoAuthType_Object = MibTableColumn
fsMIOspfv3IfCryptoAuthType = _FsMIOspfv3IfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 24),
    _FsMIOspfv3IfCryptoAuthType_Type()
)
fsMIOspfv3IfCryptoAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfCryptoAuthType.setStatus("current")


class _FsMIOspfv3IfCryptoAuthMode_Type(Integer32):
    """Custom type fsMIOspfv3IfCryptoAuthMode based on Integer32"""
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
        *(("full", 1),
          ("transition", 2),
          ("none", 3))
    )


_FsMIOspfv3IfCryptoAuthMode_Type.__name__ = "Integer32"
_FsMIOspfv3IfCryptoAuthMode_Object = MibTableColumn
fsMIOspfv3IfCryptoAuthMode = _FsMIOspfv3IfCryptoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 25),
    _FsMIOspfv3IfCryptoAuthMode_Type()
)
fsMIOspfv3IfCryptoAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfCryptoAuthMode.setStatus("current")
_FsMIOspfv3IfAuthTxed_Type = Counter32
_FsMIOspfv3IfAuthTxed_Object = MibTableColumn
fsMIOspfv3IfAuthTxed = _FsMIOspfv3IfAuthTxed_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 26),
    _FsMIOspfv3IfAuthTxed_Type()
)
fsMIOspfv3IfAuthTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthTxed.setStatus("current")
_FsMIOspfv3IfAuthRcvd_Type = Counter32
_FsMIOspfv3IfAuthRcvd_Object = MibTableColumn
fsMIOspfv3IfAuthRcvd = _FsMIOspfv3IfAuthRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 27),
    _FsMIOspfv3IfAuthRcvd_Type()
)
fsMIOspfv3IfAuthRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthRcvd.setStatus("current")
_FsMIOspfv3IfAuthDisd_Type = Counter32
_FsMIOspfv3IfAuthDisd_Object = MibTableColumn
fsMIOspfv3IfAuthDisd = _FsMIOspfv3IfAuthDisd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 3, 1, 28),
    _FsMIOspfv3IfAuthDisd_Type()
)
fsMIOspfv3IfAuthDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthDisd.setStatus("current")
_FsMIOspfv3RoutingTable_Object = MibTable
fsMIOspfv3RoutingTable = _FsMIOspfv3RoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4)
)
if mibBuilder.loadTexts:
    fsMIOspfv3RoutingTable.setStatus("current")
_FsMIOspfv3RoutingEntry_Object = MibTableRow
fsMIOspfv3RoutingEntry = _FsMIOspfv3RoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1)
)
fsMIOspfv3RoutingEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RouteDestType"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RouteDest"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RoutePfxLength"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RouteNextHopType"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RouteNextHop"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3RoutingEntry.setStatus("current")
_FsMIOspfv3RouteDestType_Type = InetAddressType
_FsMIOspfv3RouteDestType_Object = MibTableColumn
fsMIOspfv3RouteDestType = _FsMIOspfv3RouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 1),
    _FsMIOspfv3RouteDestType_Type()
)
fsMIOspfv3RouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteDestType.setStatus("current")


class _FsMIOspfv3RouteDest_Type(InetAddress):
    """Custom type fsMIOspfv3RouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3RouteDest_Type.__name__ = "InetAddress"
_FsMIOspfv3RouteDest_Object = MibTableColumn
fsMIOspfv3RouteDest = _FsMIOspfv3RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 2),
    _FsMIOspfv3RouteDest_Type()
)
fsMIOspfv3RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteDest.setStatus("current")
_FsMIOspfv3RoutePfxLength_Type = InetAddressPrefixLength
_FsMIOspfv3RoutePfxLength_Object = MibTableColumn
fsMIOspfv3RoutePfxLength = _FsMIOspfv3RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 3),
    _FsMIOspfv3RoutePfxLength_Type()
)
fsMIOspfv3RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RoutePfxLength.setStatus("current")
_FsMIOspfv3RouteNextHopType_Type = InetAddressType
_FsMIOspfv3RouteNextHopType_Object = MibTableColumn
fsMIOspfv3RouteNextHopType = _FsMIOspfv3RouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 4),
    _FsMIOspfv3RouteNextHopType_Type()
)
fsMIOspfv3RouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteNextHopType.setStatus("current")


class _FsMIOspfv3RouteNextHop_Type(InetAddress):
    """Custom type fsMIOspfv3RouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3RouteNextHop_Type.__name__ = "InetAddress"
_FsMIOspfv3RouteNextHop_Object = MibTableColumn
fsMIOspfv3RouteNextHop = _FsMIOspfv3RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 5),
    _FsMIOspfv3RouteNextHop_Type()
)
fsMIOspfv3RouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteNextHop.setStatus("current")


class _FsMIOspfv3RouteType_Type(Integer32):
    """Custom type fsMIOspfv3RouteType based on Integer32"""
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


_FsMIOspfv3RouteType_Type.__name__ = "Integer32"
_FsMIOspfv3RouteType_Object = MibTableColumn
fsMIOspfv3RouteType = _FsMIOspfv3RouteType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 6),
    _FsMIOspfv3RouteType_Type()
)
fsMIOspfv3RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteType.setStatus("current")
_FsMIOspfv3RouteAreaId_Type = AreaID
_FsMIOspfv3RouteAreaId_Object = MibTableColumn
fsMIOspfv3RouteAreaId = _FsMIOspfv3RouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 7),
    _FsMIOspfv3RouteAreaId_Type()
)
fsMIOspfv3RouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteAreaId.setStatus("current")
_FsMIOspfv3RouteCost_Type = BigMetric
_FsMIOspfv3RouteCost_Object = MibTableColumn
fsMIOspfv3RouteCost = _FsMIOspfv3RouteCost_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 8),
    _FsMIOspfv3RouteCost_Type()
)
fsMIOspfv3RouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteCost.setStatus("current")
_FsMIOspfv3RouteType2Cost_Type = BigMetric
_FsMIOspfv3RouteType2Cost_Object = MibTableColumn
fsMIOspfv3RouteType2Cost = _FsMIOspfv3RouteType2Cost_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 9),
    _FsMIOspfv3RouteType2Cost_Type()
)
fsMIOspfv3RouteType2Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteType2Cost.setStatus("current")


class _FsMIOspfv3RouteInterfaceIndex_Type(Integer32):
    """Custom type fsMIOspfv3RouteInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIOspfv3RouteInterfaceIndex_Type.__name__ = "Integer32"
_FsMIOspfv3RouteInterfaceIndex_Object = MibTableColumn
fsMIOspfv3RouteInterfaceIndex = _FsMIOspfv3RouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 4, 1, 10),
    _FsMIOspfv3RouteInterfaceIndex_Type()
)
fsMIOspfv3RouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3RouteInterfaceIndex.setStatus("current")
_FsMIOspfv3AsExternalAggregationTable_Object = MibTable
fsMIOspfv3AsExternalAggregationTable = _FsMIOspfv3AsExternalAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5)
)
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationTable.setStatus("current")
_FsMIOspfv3AsExternalAggregationEntry_Object = MibTableRow
fsMIOspfv3AsExternalAggregationEntry = _FsMIOspfv3AsExternalAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1)
)
fsMIOspfv3AsExternalAggregationEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3AsExternalAggregationNetType"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3AsExternalAggregationNet"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3AsExternalAggregationPfxLength"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3AsExternalAggregationAreaId"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationEntry.setStatus("current")
_FsMIOspfv3AsExternalAggregationNetType_Type = InetAddressType
_FsMIOspfv3AsExternalAggregationNetType_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationNetType = _FsMIOspfv3AsExternalAggregationNetType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 1),
    _FsMIOspfv3AsExternalAggregationNetType_Type()
)
fsMIOspfv3AsExternalAggregationNetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationNetType.setStatus("current")


class _FsMIOspfv3AsExternalAggregationNet_Type(InetAddress):
    """Custom type fsMIOspfv3AsExternalAggregationNet based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3AsExternalAggregationNet_Type.__name__ = "InetAddress"
_FsMIOspfv3AsExternalAggregationNet_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationNet = _FsMIOspfv3AsExternalAggregationNet_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 2),
    _FsMIOspfv3AsExternalAggregationNet_Type()
)
fsMIOspfv3AsExternalAggregationNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationNet.setStatus("current")
_FsMIOspfv3AsExternalAggregationPfxLength_Type = InetAddressPrefixLength
_FsMIOspfv3AsExternalAggregationPfxLength_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationPfxLength = _FsMIOspfv3AsExternalAggregationPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 3),
    _FsMIOspfv3AsExternalAggregationPfxLength_Type()
)
fsMIOspfv3AsExternalAggregationPfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationPfxLength.setStatus("current")
_FsMIOspfv3AsExternalAggregationAreaId_Type = AreaID
_FsMIOspfv3AsExternalAggregationAreaId_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationAreaId = _FsMIOspfv3AsExternalAggregationAreaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 4),
    _FsMIOspfv3AsExternalAggregationAreaId_Type()
)
fsMIOspfv3AsExternalAggregationAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationAreaId.setStatus("current")


class _FsMIOspfv3AsExternalAggregationEffect_Type(Integer32):
    """Custom type fsMIOspfv3AsExternalAggregationEffect based on Integer32"""
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


_FsMIOspfv3AsExternalAggregationEffect_Type.__name__ = "Integer32"
_FsMIOspfv3AsExternalAggregationEffect_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationEffect = _FsMIOspfv3AsExternalAggregationEffect_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 5),
    _FsMIOspfv3AsExternalAggregationEffect_Type()
)
fsMIOspfv3AsExternalAggregationEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationEffect.setStatus("current")


class _FsMIOspfv3AsExternalAggregationTranslation_Type(Integer32):
    """Custom type fsMIOspfv3AsExternalAggregationTranslation based on Integer32"""
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


_FsMIOspfv3AsExternalAggregationTranslation_Type.__name__ = "Integer32"
_FsMIOspfv3AsExternalAggregationTranslation_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationTranslation = _FsMIOspfv3AsExternalAggregationTranslation_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 6),
    _FsMIOspfv3AsExternalAggregationTranslation_Type()
)
fsMIOspfv3AsExternalAggregationTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationTranslation.setStatus("current")
_FsMIOspfv3AsExternalAggregationStatus_Type = RowStatus
_FsMIOspfv3AsExternalAggregationStatus_Object = MibTableColumn
fsMIOspfv3AsExternalAggregationStatus = _FsMIOspfv3AsExternalAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 5, 1, 7),
    _FsMIOspfv3AsExternalAggregationStatus_Type()
)
fsMIOspfv3AsExternalAggregationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfv3AsExternalAggregationStatus.setStatus("current")
_FsMIOspfv3BRRouteTable_Object = MibTable
fsMIOspfv3BRRouteTable = _FsMIOspfv3BRRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6)
)
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteTable.setStatus("current")
_FsMIOspfv3BRRouteEntry_Object = MibTableRow
fsMIOspfv3BRRouteEntry = _FsMIOspfv3BRRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1)
)
fsMIOspfv3BRRouteEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3BRRouteDest"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3BRRouteNextHopType"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3BRRouteNextHop"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3BRRouteDestType"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteEntry.setStatus("current")
_FsMIOspfv3BRRouteDest_Type = IpAddress
_FsMIOspfv3BRRouteDest_Object = MibTableColumn
fsMIOspfv3BRRouteDest = _FsMIOspfv3BRRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 1),
    _FsMIOspfv3BRRouteDest_Type()
)
fsMIOspfv3BRRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteDest.setStatus("current")
_FsMIOspfv3BRRouteNextHopType_Type = InetAddressType
_FsMIOspfv3BRRouteNextHopType_Object = MibTableColumn
fsMIOspfv3BRRouteNextHopType = _FsMIOspfv3BRRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 2),
    _FsMIOspfv3BRRouteNextHopType_Type()
)
fsMIOspfv3BRRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteNextHopType.setStatus("current")


class _FsMIOspfv3BRRouteNextHop_Type(InetAddress):
    """Custom type fsMIOspfv3BRRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3BRRouteNextHop_Type.__name__ = "InetAddress"
_FsMIOspfv3BRRouteNextHop_Object = MibTableColumn
fsMIOspfv3BRRouteNextHop = _FsMIOspfv3BRRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 3),
    _FsMIOspfv3BRRouteNextHop_Type()
)
fsMIOspfv3BRRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteNextHop.setStatus("current")


class _FsMIOspfv3BRRouteDestType_Type(Integer32):
    """Custom type fsMIOspfv3BRRouteDestType based on Integer32"""
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


_FsMIOspfv3BRRouteDestType_Type.__name__ = "Integer32"
_FsMIOspfv3BRRouteDestType_Object = MibTableColumn
fsMIOspfv3BRRouteDestType = _FsMIOspfv3BRRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 4),
    _FsMIOspfv3BRRouteDestType_Type()
)
fsMIOspfv3BRRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteDestType.setStatus("current")


class _FsMIOspfv3BRRouteType_Type(Integer32):
    """Custom type fsMIOspfv3BRRouteType based on Integer32"""
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


_FsMIOspfv3BRRouteType_Type.__name__ = "Integer32"
_FsMIOspfv3BRRouteType_Object = MibTableColumn
fsMIOspfv3BRRouteType = _FsMIOspfv3BRRouteType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 5),
    _FsMIOspfv3BRRouteType_Type()
)
fsMIOspfv3BRRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteType.setStatus("current")
_FsMIOspfv3BRRouteAreaId_Type = AreaID
_FsMIOspfv3BRRouteAreaId_Object = MibTableColumn
fsMIOspfv3BRRouteAreaId = _FsMIOspfv3BRRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 6),
    _FsMIOspfv3BRRouteAreaId_Type()
)
fsMIOspfv3BRRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteAreaId.setStatus("current")
_FsMIOspfv3BRRouteCost_Type = BigMetric
_FsMIOspfv3BRRouteCost_Object = MibTableColumn
fsMIOspfv3BRRouteCost = _FsMIOspfv3BRRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 7),
    _FsMIOspfv3BRRouteCost_Type()
)
fsMIOspfv3BRRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteCost.setStatus("current")
_FsMIOspfv3BRRouteInterfaceIndex_Type = InterfaceIndex
_FsMIOspfv3BRRouteInterfaceIndex_Object = MibTableColumn
fsMIOspfv3BRRouteInterfaceIndex = _FsMIOspfv3BRRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 6, 1, 8),
    _FsMIOspfv3BRRouteInterfaceIndex_Type()
)
fsMIOspfv3BRRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3BRRouteInterfaceIndex.setStatus("current")
_FsMIOspfv3RedistRouteCfgTable_Object = MibTable
fsMIOspfv3RedistRouteCfgTable = _FsMIOspfv3RedistRouteCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7)
)
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteCfgTable.setStatus("current")
_FsMIOspfv3RedistRouteCfgEntry_Object = MibTableRow
fsMIOspfv3RedistRouteCfgEntry = _FsMIOspfv3RedistRouteCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1)
)
fsMIOspfv3RedistRouteCfgEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RedistRouteDestType"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RedistRouteDest"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3RedistRoutePfxLength"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteCfgEntry.setStatus("current")
_FsMIOspfv3RedistRouteDestType_Type = InetAddressType
_FsMIOspfv3RedistRouteDestType_Object = MibTableColumn
fsMIOspfv3RedistRouteDestType = _FsMIOspfv3RedistRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 1),
    _FsMIOspfv3RedistRouteDestType_Type()
)
fsMIOspfv3RedistRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteDestType.setStatus("current")


class _FsMIOspfv3RedistRouteDest_Type(InetAddress):
    """Custom type fsMIOspfv3RedistRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIOspfv3RedistRouteDest_Type.__name__ = "InetAddress"
_FsMIOspfv3RedistRouteDest_Object = MibTableColumn
fsMIOspfv3RedistRouteDest = _FsMIOspfv3RedistRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 2),
    _FsMIOspfv3RedistRouteDest_Type()
)
fsMIOspfv3RedistRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteDest.setStatus("current")
_FsMIOspfv3RedistRoutePfxLength_Type = InetAddressPrefixLength
_FsMIOspfv3RedistRoutePfxLength_Object = MibTableColumn
fsMIOspfv3RedistRoutePfxLength = _FsMIOspfv3RedistRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 3),
    _FsMIOspfv3RedistRoutePfxLength_Type()
)
fsMIOspfv3RedistRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRoutePfxLength.setStatus("current")


class _FsMIOspfv3RedistRouteMetric_Type(BigMetric):
    """Custom type fsMIOspfv3RedistRouteMetric based on BigMetric"""
    defaultValue = 10


_FsMIOspfv3RedistRouteMetric_Type.__name__ = "BigMetric"
_FsMIOspfv3RedistRouteMetric_Object = MibTableColumn
fsMIOspfv3RedistRouteMetric = _FsMIOspfv3RedistRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 4),
    _FsMIOspfv3RedistRouteMetric_Type()
)
fsMIOspfv3RedistRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteMetric.setStatus("current")


class _FsMIOspfv3RedistRouteMetricType_Type(Integer32):
    """Custom type fsMIOspfv3RedistRouteMetricType based on Integer32"""
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


_FsMIOspfv3RedistRouteMetricType_Type.__name__ = "Integer32"
_FsMIOspfv3RedistRouteMetricType_Object = MibTableColumn
fsMIOspfv3RedistRouteMetricType = _FsMIOspfv3RedistRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 5),
    _FsMIOspfv3RedistRouteMetricType_Type()
)
fsMIOspfv3RedistRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteMetricType.setStatus("current")


class _FsMIOspfv3RedistRouteTagType_Type(Integer32):
    """Custom type fsMIOspfv3RedistRouteTagType based on Integer32"""
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


_FsMIOspfv3RedistRouteTagType_Type.__name__ = "Integer32"
_FsMIOspfv3RedistRouteTagType_Object = MibTableColumn
fsMIOspfv3RedistRouteTagType = _FsMIOspfv3RedistRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 6),
    _FsMIOspfv3RedistRouteTagType_Type()
)
fsMIOspfv3RedistRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteTagType.setStatus("current")


class _FsMIOspfv3RedistRouteTag_Type(Integer32):
    """Custom type fsMIOspfv3RedistRouteTag based on Integer32"""
    defaultValue = 0


_FsMIOspfv3RedistRouteTag_Type.__name__ = "Integer32"
_FsMIOspfv3RedistRouteTag_Object = MibTableColumn
fsMIOspfv3RedistRouteTag = _FsMIOspfv3RedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 7),
    _FsMIOspfv3RedistRouteTag_Type()
)
fsMIOspfv3RedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteTag.setStatus("current")
_FsMIOspfv3RedistRouteStatus_Type = RowStatus
_FsMIOspfv3RedistRouteStatus_Object = MibTableColumn
fsMIOspfv3RedistRouteStatus = _FsMIOspfv3RedistRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 7, 1, 8),
    _FsMIOspfv3RedistRouteStatus_Type()
)
fsMIOspfv3RedistRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfv3RedistRouteStatus.setStatus("current")
_FsMIOspfv3RRDGroup_ObjectIdentity = ObjectIdentity
fsMIOspfv3RRDGroup = _FsMIOspfv3RRDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8)
)
_FsMIOspfv3RRDGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIOspfv3RRDGeneralGroup = _FsMIOspfv3RRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1)
)
_FsMIOspfv3RRDRouteTable_Object = MibTable
fsMIOspfv3RRDRouteTable = _FsMIOspfv3RRDRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3RRDRouteTable.setStatus("current")
_FsMIOspfv3RRDRouteEntry_Object = MibTableRow
fsMIOspfv3RRDRouteEntry = _FsMIOspfv3RRDRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3RRDRouteEntry.setStatus("current")


class _FsMIOspfv3RRDStatus_Type(Status):
    """Custom type fsMIOspfv3RRDStatus based on Status"""
    defaultValue = 2


_FsMIOspfv3RRDStatus_Type.__name__ = "Status"
_FsMIOspfv3RRDStatus_Object = MibTableColumn
fsMIOspfv3RRDStatus = _FsMIOspfv3RRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1, 1, 1, 1),
    _FsMIOspfv3RRDStatus_Type()
)
fsMIOspfv3RRDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RRDStatus.setStatus("current")


class _FsMIOspfv3RRDSrcProtoMask_Type(Integer32):
    """Custom type fsMIOspfv3RRDSrcProtoMask based on Integer32"""
    defaultValue = 0


_FsMIOspfv3RRDSrcProtoMask_Type.__name__ = "Integer32"
_FsMIOspfv3RRDSrcProtoMask_Object = MibTableColumn
fsMIOspfv3RRDSrcProtoMask = _FsMIOspfv3RRDSrcProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1, 1, 1, 2),
    _FsMIOspfv3RRDSrcProtoMask_Type()
)
fsMIOspfv3RRDSrcProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RRDSrcProtoMask.setStatus("current")


class _FsMIOspfv3RRDRouteMapName_Type(OctetString):
    """Custom type fsMIOspfv3RRDRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsMIOspfv3RRDRouteMapName_Type.__name__ = "OctetString"
_FsMIOspfv3RRDRouteMapName_Object = MibTableColumn
fsMIOspfv3RRDRouteMapName = _FsMIOspfv3RRDRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 8, 1, 1, 1, 3),
    _FsMIOspfv3RRDRouteMapName_Type()
)
fsMIOspfv3RRDRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3RRDRouteMapName.setStatus("current")
_FsMIOspfv3DistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsMIOspfv3DistInOutRouteMap = _FsMIOspfv3DistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9)
)
_FsMIOspfv3DistInOutRouteMapTable_Object = MibTable
fsMIOspfv3DistInOutRouteMapTable = _FsMIOspfv3DistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapTable.setStatus("current")
_FsMIOspfv3DistInOutRouteMapEntry_Object = MibTableRow
fsMIOspfv3DistInOutRouteMapEntry = _FsMIOspfv3DistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1, 1)
)
fsMIOspfv3DistInOutRouteMapEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3DistInOutRouteMapName"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3DistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapEntry.setStatus("current")


class _FsMIOspfv3DistInOutRouteMapName_Type(DisplayString):
    """Custom type fsMIOspfv3DistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIOspfv3DistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsMIOspfv3DistInOutRouteMapName_Object = MibTableColumn
fsMIOspfv3DistInOutRouteMapName = _FsMIOspfv3DistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1, 1, 1),
    _FsMIOspfv3DistInOutRouteMapName_Type()
)
fsMIOspfv3DistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapName.setStatus("current")


class _FsMIOspfv3DistInOutRouteMapType_Type(Integer32):
    """Custom type fsMIOspfv3DistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsMIOspfv3DistInOutRouteMapType_Type.__name__ = "Integer32"
_FsMIOspfv3DistInOutRouteMapType_Object = MibTableColumn
fsMIOspfv3DistInOutRouteMapType = _FsMIOspfv3DistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1, 1, 2),
    _FsMIOspfv3DistInOutRouteMapType_Type()
)
fsMIOspfv3DistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapType.setStatus("current")


class _FsMIOspfv3DistInOutRouteMapValue_Type(Integer32):
    """Custom type fsMIOspfv3DistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIOspfv3DistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsMIOspfv3DistInOutRouteMapValue_Object = MibTableColumn
fsMIOspfv3DistInOutRouteMapValue = _FsMIOspfv3DistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1, 1, 3),
    _FsMIOspfv3DistInOutRouteMapValue_Type()
)
fsMIOspfv3DistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapValue.setStatus("current")
_FsMIOspfv3DistInOutRouteMapRowStatus_Type = RowStatus
_FsMIOspfv3DistInOutRouteMapRowStatus_Object = MibTableColumn
fsMIOspfv3DistInOutRouteMapRowStatus = _FsMIOspfv3DistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 9, 1, 1, 4),
    _FsMIOspfv3DistInOutRouteMapRowStatus_Type()
)
fsMIOspfv3DistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3DistInOutRouteMapRowStatus.setStatus("current")
_FsMIOspfv3PreferenceGroup_ObjectIdentity = ObjectIdentity
fsMIOspfv3PreferenceGroup = _FsMIOspfv3PreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 10)
)
_FsMIOspfv3PreferenceTable_Object = MibTable
fsMIOspfv3PreferenceTable = _FsMIOspfv3PreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 10, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3PreferenceTable.setStatus("current")
_FsMIOspfv3PreferenceEntry_Object = MibTableRow
fsMIOspfv3PreferenceEntry = _FsMIOspfv3PreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 10, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3PreferenceEntry.setStatus("current")


class _FsMIOspfv3PreferenceValue_Type(Integer32):
    """Custom type fsMIOspfv3PreferenceValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfv3PreferenceValue_Type.__name__ = "Integer32"
_FsMIOspfv3PreferenceValue_Object = MibTableColumn
fsMIOspfv3PreferenceValue = _FsMIOspfv3PreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 10, 1, 1, 1),
    _FsMIOspfv3PreferenceValue_Type()
)
fsMIOspfv3PreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3PreferenceValue.setStatus("current")
_FsMIOspfv3NeighborBfdGroup_ObjectIdentity = ObjectIdentity
fsMIOspfv3NeighborBfdGroup = _FsMIOspfv3NeighborBfdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 11)
)
_FsMIOspfv3NeighborBfdTable_Object = MibTable
fsMIOspfv3NeighborBfdTable = _FsMIOspfv3NeighborBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 11, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3NeighborBfdTable.setStatus("current")
_FsMIOspfv3NeighborBfdEntry_Object = MibTableRow
fsMIOspfv3NeighborBfdEntry = _FsMIOspfv3NeighborBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 11, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3NeighborBfdEntry.setStatus("current")


class _FsMIOspfv3NbrBfdState_Type(Integer32):
    """Custom type fsMIOspfv3NbrBfdState based on Integer32"""
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


_FsMIOspfv3NbrBfdState_Type.__name__ = "Integer32"
_FsMIOspfv3NbrBfdState_Object = MibTableColumn
fsMIOspfv3NbrBfdState = _FsMIOspfv3NbrBfdState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 11, 1, 1, 1),
    _FsMIOspfv3NbrBfdState_Type()
)
fsMIOspfv3NbrBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfv3NbrBfdState.setStatus("current")
_FsMIOspfv3IfAuthTable_Object = MibTable
fsMIOspfv3IfAuthTable = _FsMIOspfv3IfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12)
)
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthTable.setStatus("current")
_FsMIOspfv3IfAuthEntry_Object = MibTableRow
fsMIOspfv3IfAuthEntry = _FsMIOspfv3IfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1)
)
fsMIOspfv3IfAuthEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3IfAuthIfIndex"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3IfAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthEntry.setStatus("current")


class _FsMIOspfv3IfAuthIfIndex_Type(InterfaceIndex):
    """Custom type fsMIOspfv3IfAuthIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfv3IfAuthIfIndex_Type.__name__ = "InterfaceIndex"
_FsMIOspfv3IfAuthIfIndex_Object = MibTableColumn
fsMIOspfv3IfAuthIfIndex = _FsMIOspfv3IfAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 1),
    _FsMIOspfv3IfAuthIfIndex_Type()
)
fsMIOspfv3IfAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthIfIndex.setStatus("current")


class _FsMIOspfv3IfAuthKeyId_Type(Integer32):
    """Custom type fsMIOspfv3IfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfv3IfAuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfv3IfAuthKeyId_Object = MibTableColumn
fsMIOspfv3IfAuthKeyId = _FsMIOspfv3IfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 2),
    _FsMIOspfv3IfAuthKeyId_Type()
)
fsMIOspfv3IfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyId.setStatus("current")


class _FsMIOspfv3IfAuthKey_Type(OctetString):
    """Custom type fsMIOspfv3IfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfv3IfAuthKey_Type.__name__ = "OctetString"
_FsMIOspfv3IfAuthKey_Object = MibTableColumn
fsMIOspfv3IfAuthKey = _FsMIOspfv3IfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 3),
    _FsMIOspfv3IfAuthKey_Type()
)
fsMIOspfv3IfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKey.setStatus("current")
_FsMIOspfv3IfAuthKeyStartAccept_Type = DateAndTime
_FsMIOspfv3IfAuthKeyStartAccept_Object = MibTableColumn
fsMIOspfv3IfAuthKeyStartAccept = _FsMIOspfv3IfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 4),
    _FsMIOspfv3IfAuthKeyStartAccept_Type()
)
fsMIOspfv3IfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyStartAccept.setStatus("current")
_FsMIOspfv3IfAuthKeyStartGenerate_Type = DateAndTime
_FsMIOspfv3IfAuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfv3IfAuthKeyStartGenerate = _FsMIOspfv3IfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 5),
    _FsMIOspfv3IfAuthKeyStartGenerate_Type()
)
fsMIOspfv3IfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyStartGenerate.setStatus("current")
_FsMIOspfv3IfAuthKeyStopGenerate_Type = DateAndTime
_FsMIOspfv3IfAuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfv3IfAuthKeyStopGenerate = _FsMIOspfv3IfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 6),
    _FsMIOspfv3IfAuthKeyStopGenerate_Type()
)
fsMIOspfv3IfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyStopGenerate.setStatus("current")
_FsMIOspfv3IfAuthKeyStopAccept_Type = DateAndTime
_FsMIOspfv3IfAuthKeyStopAccept_Object = MibTableColumn
fsMIOspfv3IfAuthKeyStopAccept = _FsMIOspfv3IfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 7),
    _FsMIOspfv3IfAuthKeyStopAccept_Type()
)
fsMIOspfv3IfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyStopAccept.setStatus("current")
_FsMIOspfv3IfAuthKeyStatus_Type = RowStatus
_FsMIOspfv3IfAuthKeyStatus_Object = MibTableColumn
fsMIOspfv3IfAuthKeyStatus = _FsMIOspfv3IfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 12, 1, 8),
    _FsMIOspfv3IfAuthKeyStatus_Type()
)
fsMIOspfv3IfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3IfAuthKeyStatus.setStatus("current")
_FsMIOspfv3VirtIfAuthTable_Object = MibTable
fsMIOspfv3VirtIfAuthTable = _FsMIOspfv3VirtIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13)
)
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthTable.setStatus("current")
_FsMIOspfv3VirtIfAuthEntry_Object = MibTableRow
fsMIOspfv3VirtIfAuthEntry = _FsMIOspfv3VirtIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1)
)
fsMIOspfv3VirtIfAuthEntry.setIndexNames(
    (0, "ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3ContextId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3VirtIfAuthAreaId"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3VirtIfAuthNeighbor"),
    (0, "ARICENT-MIOSPFV3-MIB", "fsMIOspfv3VirtIfAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthEntry.setStatus("current")
_FsMIOspfv3VirtIfAuthAreaId_Type = AreaID
_FsMIOspfv3VirtIfAuthAreaId_Object = MibTableColumn
fsMIOspfv3VirtIfAuthAreaId = _FsMIOspfv3VirtIfAuthAreaId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 1),
    _FsMIOspfv3VirtIfAuthAreaId_Type()
)
fsMIOspfv3VirtIfAuthAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthAreaId.setStatus("current")
_FsMIOspfv3VirtIfAuthNeighbor_Type = RouterID
_FsMIOspfv3VirtIfAuthNeighbor_Object = MibTableColumn
fsMIOspfv3VirtIfAuthNeighbor = _FsMIOspfv3VirtIfAuthNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 2),
    _FsMIOspfv3VirtIfAuthNeighbor_Type()
)
fsMIOspfv3VirtIfAuthNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthNeighbor.setStatus("current")


class _FsMIOspfv3VirtIfAuthKeyId_Type(Integer32):
    """Custom type fsMIOspfv3VirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfv3VirtIfAuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfv3VirtIfAuthKeyId_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyId = _FsMIOspfv3VirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 3),
    _FsMIOspfv3VirtIfAuthKeyId_Type()
)
fsMIOspfv3VirtIfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyId.setStatus("current")


class _FsMIOspfv3VirtIfAuthKey_Type(OctetString):
    """Custom type fsMIOspfv3VirtIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfv3VirtIfAuthKey_Type.__name__ = "OctetString"
_FsMIOspfv3VirtIfAuthKey_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKey = _FsMIOspfv3VirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 4),
    _FsMIOspfv3VirtIfAuthKey_Type()
)
fsMIOspfv3VirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKey.setStatus("current")
_FsMIOspfv3VirtIfAuthKeyStartAccept_Type = DateAndTime
_FsMIOspfv3VirtIfAuthKeyStartAccept_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyStartAccept = _FsMIOspfv3VirtIfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 5),
    _FsMIOspfv3VirtIfAuthKeyStartAccept_Type()
)
fsMIOspfv3VirtIfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyStartAccept.setStatus("current")
_FsMIOspfv3VirtIfAuthKeyStartGenerate_Type = DateAndTime
_FsMIOspfv3VirtIfAuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyStartGenerate = _FsMIOspfv3VirtIfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 6),
    _FsMIOspfv3VirtIfAuthKeyStartGenerate_Type()
)
fsMIOspfv3VirtIfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyStartGenerate.setStatus("current")
_FsMIOspfv3VirtIfAuthKeyStopGenerate_Type = DateAndTime
_FsMIOspfv3VirtIfAuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyStopGenerate = _FsMIOspfv3VirtIfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 7),
    _FsMIOspfv3VirtIfAuthKeyStopGenerate_Type()
)
fsMIOspfv3VirtIfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyStopGenerate.setStatus("current")
_FsMIOspfv3VirtIfAuthKeyStopAccept_Type = DateAndTime
_FsMIOspfv3VirtIfAuthKeyStopAccept_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyStopAccept = _FsMIOspfv3VirtIfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 8),
    _FsMIOspfv3VirtIfAuthKeyStopAccept_Type()
)
fsMIOspfv3VirtIfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyStopAccept.setStatus("current")
_FsMIOspfv3VirtIfAuthKeyStatus_Type = RowStatus
_FsMIOspfv3VirtIfAuthKeyStatus_Object = MibTableColumn
fsMIOspfv3VirtIfAuthKeyStatus = _FsMIOspfv3VirtIfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 13, 1, 9),
    _FsMIOspfv3VirtIfAuthKeyStatus_Type()
)
fsMIOspfv3VirtIfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfAuthKeyStatus.setStatus("current")
_FsMIOspfv3VirtIfCryptoAuthTable_Object = MibTable
fsMIOspfv3VirtIfCryptoAuthTable = _FsMIOspfv3VirtIfCryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 14)
)
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfCryptoAuthTable.setStatus("current")
_FsMIOspfv3VirtIfCryptoAuthEntry_Object = MibTableRow
fsMIOspfv3VirtIfCryptoAuthEntry = _FsMIOspfv3VirtIfCryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 14, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfCryptoAuthEntry.setStatus("current")


class _FsMIOspfv3VirtIfCryptoAuthType_Type(Integer32):
    """Custom type fsMIOspfv3VirtIfCryptoAuthType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5),
          ("none", 6))
    )


_FsMIOspfv3VirtIfCryptoAuthType_Type.__name__ = "Integer32"
_FsMIOspfv3VirtIfCryptoAuthType_Object = MibTableColumn
fsMIOspfv3VirtIfCryptoAuthType = _FsMIOspfv3VirtIfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 14, 1, 1),
    _FsMIOspfv3VirtIfCryptoAuthType_Type()
)
fsMIOspfv3VirtIfCryptoAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfCryptoAuthType.setStatus("current")


class _FsMIOspfv3VirtIfCryptoAuthMode_Type(Integer32):
    """Custom type fsMIOspfv3VirtIfCryptoAuthMode based on Integer32"""
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
        *(("full", 1),
          ("transition", 2),
          ("none", 3))
    )


_FsMIOspfv3VirtIfCryptoAuthMode_Type.__name__ = "Integer32"
_FsMIOspfv3VirtIfCryptoAuthMode_Object = MibTableColumn
fsMIOspfv3VirtIfCryptoAuthMode = _FsMIOspfv3VirtIfCryptoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 14, 1, 2),
    _FsMIOspfv3VirtIfCryptoAuthMode_Type()
)
fsMIOspfv3VirtIfCryptoAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfv3VirtIfCryptoAuthMode.setStatus("current")
_FsMIOspfv3Notification_ObjectIdentity = ObjectIdentity
fsMIOspfv3Notification = _FsMIOspfv3Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101)
)
_FsMIOspfv3Traps_ObjectIdentity = ObjectIdentity
fsMIOspfv3Traps = _FsMIOspfv3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0)
)
_FsMIOspfv3TrapObject_ObjectIdentity = ObjectIdentity
fsMIOspfv3TrapObject = _FsMIOspfv3TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1)
)
_FsMIOspfv3TrapNbrIfIndex_Type = InterfaceIndex
_FsMIOspfv3TrapNbrIfIndex_Object = MibScalar
fsMIOspfv3TrapNbrIfIndex = _FsMIOspfv3TrapNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1, 1),
    _FsMIOspfv3TrapNbrIfIndex_Type()
)
fsMIOspfv3TrapNbrIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIOspfv3TrapNbrIfIndex.setStatus("current")
_FsMIOspfv3TrapVirtNbrRtrId_Type = RouterID
_FsMIOspfv3TrapVirtNbrRtrId_Object = MibScalar
fsMIOspfv3TrapVirtNbrRtrId = _FsMIOspfv3TrapVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1, 2),
    _FsMIOspfv3TrapVirtNbrRtrId_Type()
)
fsMIOspfv3TrapVirtNbrRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIOspfv3TrapVirtNbrRtrId.setStatus("current")
_FsMIOspfv3TrapNbrRtrId_Type = RouterID
_FsMIOspfv3TrapNbrRtrId_Object = MibScalar
fsMIOspfv3TrapNbrRtrId = _FsMIOspfv3TrapNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1, 3),
    _FsMIOspfv3TrapNbrRtrId_Type()
)
fsMIOspfv3TrapNbrRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIOspfv3TrapNbrRtrId.setStatus("current")
_FsMIOspfv3TrapVirtNbrArea_Type = AreaID
_FsMIOspfv3TrapVirtNbrArea_Object = MibScalar
fsMIOspfv3TrapVirtNbrArea = _FsMIOspfv3TrapVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1, 4),
    _FsMIOspfv3TrapVirtNbrArea_Type()
)
fsMIOspfv3TrapVirtNbrArea.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIOspfv3TrapVirtNbrArea.setStatus("current")


class _FsMIOspfv3TrapBulkUpdAbortReason_Type(Integer32):
    """Custom type fsMIOspfv3TrapBulkUpdAbortReason based on Integer32"""
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


_FsMIOspfv3TrapBulkUpdAbortReason_Type.__name__ = "Integer32"
_FsMIOspfv3TrapBulkUpdAbortReason_Object = MibScalar
fsMIOspfv3TrapBulkUpdAbortReason = _FsMIOspfv3TrapBulkUpdAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 1, 5),
    _FsMIOspfv3TrapBulkUpdAbortReason_Type()
)
fsMIOspfv3TrapBulkUpdAbortReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIOspfv3TrapBulkUpdAbortReason.setStatus("current")
fsMIStdOspfv3Entry.registerAugmentions(
    ("ARICENT-MIOSPFV3-MIB",
     "fsMIOspfv3Entry")
)
fsMIOspfv3Entry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions(
    ("ARICENT-MIOSPFV3-MIB",
     "fsMIOspfv3RRDRouteEntry")
)
fsMIOspfv3RRDRouteEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3Entry.registerAugmentions(
    ("ARICENT-MIOSPFV3-MIB",
     "fsMIOspfv3PreferenceEntry")
)
fsMIOspfv3PreferenceEntry.setIndexNames(*fsMIStdOspfv3Entry.getIndexNames())
fsMIStdOspfv3NbrEntry.registerAugmentions(
    ("ARICENT-MIOSPFV3-MIB",
     "fsMIOspfv3NeighborBfdEntry")
)
fsMIOspfv3NeighborBfdEntry.setIndexNames(*fsMIStdOspfv3NbrEntry.getIndexNames())
fsMIStdOspfv3VirtIfEntry.registerAugmentions(
    ("ARICENT-MIOSPFV3-MIB",
     "fsMIOspfv3VirtIfCryptoAuthEntry")
)
fsMIOspfv3VirtIfCryptoAuthEntry.setIndexNames(*fsMIStdOspfv3VirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsMIOspfv3RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 1)
)
fsMIOspfv3RestartStatusChange.setObjects(
      *(("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RestartStatus"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RestartInterval"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RestartExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfv3RestartStatusChange.setStatus(
        "current"
    )

fsMIOspfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 2)
)
fsMIOspfv3NbrRestartHelperStatusChange.setObjects(
      *(("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3TrapNbrIfIndex"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3TrapNbrRtrId"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3NbrRestartHelperStatus"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3NbrRestartHelperAge"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3NbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfv3NbrRestartHelperStatusChange.setStatus(
        "current"
    )

fsMIOspfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 3)
)
fsMIOspfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3TrapVirtNbrArea"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3TrapVirtNbrRtrId"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3VirtNbrRestartHelperStatus"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3VirtNbrRestartHelperAge"),
        ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3VirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfv3VirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )

fsMIOspfv3HotStandbyStateChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 4)
)
fsMIOspfv3HotStandbyStateChgTrap.setObjects(
      *(("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3HotStandbyState"))
)
if mibBuilder.loadTexts:
    fsMIOspfv3HotStandbyStateChgTrap.setStatus(
        "current"
    )

fsMIOspfv3HotStandbyBulkUpdAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 5)
)
fsMIOspfv3HotStandbyBulkUpdAbortTrap.setObjects(
      *(("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3DynamicBulkUpdStatus"),
        ("ARICENT-MIOSPFV3-MIB", "fsMIOspfv3TrapBulkUpdAbortReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfv3HotStandbyBulkUpdAbortTrap.setStatus(
        "current"
    )

fsMIOspfv3AuthSequenceNumWrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 24, 101, 0, 6)
)
fsMIOspfv3AuthSequenceNumWrap.setObjects(
    ("ARICENT-MISTDOSPFV3-MIB", "fsMIStdOspfv3RouterId")
)
if mibBuilder.loadTexts:
    fsMIOspfv3AuthSequenceNumWrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MIOSPFV3-MIB",
    **{"fsMIOspfv3": fsMIOspfv3,
       "fsMIOspfv3GeneralGroup": fsMIOspfv3GeneralGroup,
       "fsMIOspfv3GlobalTraceLevel": fsMIOspfv3GlobalTraceLevel,
       "fsMIOspfv3VrfSpfInterval": fsMIOspfv3VrfSpfInterval,
       "fsMIOspfv3RTStaggeringStatus": fsMIOspfv3RTStaggeringStatus,
       "fsMIOspfv3HotStandbyAdminStatus": fsMIOspfv3HotStandbyAdminStatus,
       "fsMIOspfv3HotStandbyState": fsMIOspfv3HotStandbyState,
       "fsMIOspfv3DynamicBulkUpdStatus": fsMIOspfv3DynamicBulkUpdStatus,
       "fsMIOspfv3StandbyHelloSyncCount": fsMIOspfv3StandbyHelloSyncCount,
       "fsMIOspfv3StandbyLsaSyncCount": fsMIOspfv3StandbyLsaSyncCount,
       "fsMIOspfv3Table": fsMIOspfv3Table,
       "fsMIOspfv3Entry": fsMIOspfv3Entry,
       "fsMIOspfv3OverFlowState": fsMIOspfv3OverFlowState,
       "fsMIOspfv3TraceLevel": fsMIOspfv3TraceLevel,
       "fsMIOspfv3ABRType": fsMIOspfv3ABRType,
       "fsMIOspfv3NssaAsbrDefRtTrans": fsMIOspfv3NssaAsbrDefRtTrans,
       "fsMIOspfv3DefaultPassiveInterface": fsMIOspfv3DefaultPassiveInterface,
       "fsMIOspfv3SpfDelay": fsMIOspfv3SpfDelay,
       "fsMIOspfv3SpfHoldTime": fsMIOspfv3SpfHoldTime,
       "fsMIOspfv3RTStaggeringInterval": fsMIOspfv3RTStaggeringInterval,
       "fsMIOspfv3RestartStrictLsaChecking": fsMIOspfv3RestartStrictLsaChecking,
       "fsMIOspfv3HelperSupport": fsMIOspfv3HelperSupport,
       "fsMIOspfv3HelperGraceTimeLimit": fsMIOspfv3HelperGraceTimeLimit,
       "fsMIOspfv3RestartAckState": fsMIOspfv3RestartAckState,
       "fsMIOspfv3GraceLsaRetransmitCount": fsMIOspfv3GraceLsaRetransmitCount,
       "fsMIOspfv3RestartReason": fsMIOspfv3RestartReason,
       "fsMIOspfv3ExtTraceLevel": fsMIOspfv3ExtTraceLevel,
       "fsMIOspfv3SetTraps": fsMIOspfv3SetTraps,
       "fsMIOspfv3BfdStatus": fsMIOspfv3BfdStatus,
       "fsMIOspfv3BfdAllIfState": fsMIOspfv3BfdAllIfState,
       "fsMIOspfv3IfTable": fsMIOspfv3IfTable,
       "fsMIOspfv3IfEntry": fsMIOspfv3IfEntry,
       "fsMIOspfv3IfIndex": fsMIOspfv3IfIndex,
       "fsMIOspfv3IfOperState": fsMIOspfv3IfOperState,
       "fsMIOspfv3IfPassive": fsMIOspfv3IfPassive,
       "fsMIOspfv3IfNbrCount": fsMIOspfv3IfNbrCount,
       "fsMIOspfv3IfAdjCount": fsMIOspfv3IfAdjCount,
       "fsMIOspfv3IfHelloRcvd": fsMIOspfv3IfHelloRcvd,
       "fsMIOspfv3IfHelloTxed": fsMIOspfv3IfHelloTxed,
       "fsMIOspfv3IfHelloDisd": fsMIOspfv3IfHelloDisd,
       "fsMIOspfv3IfDdpRcvd": fsMIOspfv3IfDdpRcvd,
       "fsMIOspfv3IfDdpTxed": fsMIOspfv3IfDdpTxed,
       "fsMIOspfv3IfDdpDisd": fsMIOspfv3IfDdpDisd,
       "fsMIOspfv3IfLrqRcvd": fsMIOspfv3IfLrqRcvd,
       "fsMIOspfv3IfLrqTxed": fsMIOspfv3IfLrqTxed,
       "fsMIOspfv3IfLrqDisd": fsMIOspfv3IfLrqDisd,
       "fsMIOspfv3IfLsuRcvd": fsMIOspfv3IfLsuRcvd,
       "fsMIOspfv3IfLsuTxed": fsMIOspfv3IfLsuTxed,
       "fsMIOspfv3IfLsuDisd": fsMIOspfv3IfLsuDisd,
       "fsMIOspfv3IfLakRcvd": fsMIOspfv3IfLakRcvd,
       "fsMIOspfv3IfLakTxed": fsMIOspfv3IfLakTxed,
       "fsMIOspfv3IfLakDisd": fsMIOspfv3IfLakDisd,
       "fsMIOspfv3IfContextId": fsMIOspfv3IfContextId,
       "fsMIOspfv3IfLinkLSASuppression": fsMIOspfv3IfLinkLSASuppression,
       "fsMIOspfv3IfBfdState": fsMIOspfv3IfBfdState,
       "fsMIOspfv3IfCryptoAuthType": fsMIOspfv3IfCryptoAuthType,
       "fsMIOspfv3IfCryptoAuthMode": fsMIOspfv3IfCryptoAuthMode,
       "fsMIOspfv3IfAuthTxed": fsMIOspfv3IfAuthTxed,
       "fsMIOspfv3IfAuthRcvd": fsMIOspfv3IfAuthRcvd,
       "fsMIOspfv3IfAuthDisd": fsMIOspfv3IfAuthDisd,
       "fsMIOspfv3RoutingTable": fsMIOspfv3RoutingTable,
       "fsMIOspfv3RoutingEntry": fsMIOspfv3RoutingEntry,
       "fsMIOspfv3RouteDestType": fsMIOspfv3RouteDestType,
       "fsMIOspfv3RouteDest": fsMIOspfv3RouteDest,
       "fsMIOspfv3RoutePfxLength": fsMIOspfv3RoutePfxLength,
       "fsMIOspfv3RouteNextHopType": fsMIOspfv3RouteNextHopType,
       "fsMIOspfv3RouteNextHop": fsMIOspfv3RouteNextHop,
       "fsMIOspfv3RouteType": fsMIOspfv3RouteType,
       "fsMIOspfv3RouteAreaId": fsMIOspfv3RouteAreaId,
       "fsMIOspfv3RouteCost": fsMIOspfv3RouteCost,
       "fsMIOspfv3RouteType2Cost": fsMIOspfv3RouteType2Cost,
       "fsMIOspfv3RouteInterfaceIndex": fsMIOspfv3RouteInterfaceIndex,
       "fsMIOspfv3AsExternalAggregationTable": fsMIOspfv3AsExternalAggregationTable,
       "fsMIOspfv3AsExternalAggregationEntry": fsMIOspfv3AsExternalAggregationEntry,
       "fsMIOspfv3AsExternalAggregationNetType": fsMIOspfv3AsExternalAggregationNetType,
       "fsMIOspfv3AsExternalAggregationNet": fsMIOspfv3AsExternalAggregationNet,
       "fsMIOspfv3AsExternalAggregationPfxLength": fsMIOspfv3AsExternalAggregationPfxLength,
       "fsMIOspfv3AsExternalAggregationAreaId": fsMIOspfv3AsExternalAggregationAreaId,
       "fsMIOspfv3AsExternalAggregationEffect": fsMIOspfv3AsExternalAggregationEffect,
       "fsMIOspfv3AsExternalAggregationTranslation": fsMIOspfv3AsExternalAggregationTranslation,
       "fsMIOspfv3AsExternalAggregationStatus": fsMIOspfv3AsExternalAggregationStatus,
       "fsMIOspfv3BRRouteTable": fsMIOspfv3BRRouteTable,
       "fsMIOspfv3BRRouteEntry": fsMIOspfv3BRRouteEntry,
       "fsMIOspfv3BRRouteDest": fsMIOspfv3BRRouteDest,
       "fsMIOspfv3BRRouteNextHopType": fsMIOspfv3BRRouteNextHopType,
       "fsMIOspfv3BRRouteNextHop": fsMIOspfv3BRRouteNextHop,
       "fsMIOspfv3BRRouteDestType": fsMIOspfv3BRRouteDestType,
       "fsMIOspfv3BRRouteType": fsMIOspfv3BRRouteType,
       "fsMIOspfv3BRRouteAreaId": fsMIOspfv3BRRouteAreaId,
       "fsMIOspfv3BRRouteCost": fsMIOspfv3BRRouteCost,
       "fsMIOspfv3BRRouteInterfaceIndex": fsMIOspfv3BRRouteInterfaceIndex,
       "fsMIOspfv3RedistRouteCfgTable": fsMIOspfv3RedistRouteCfgTable,
       "fsMIOspfv3RedistRouteCfgEntry": fsMIOspfv3RedistRouteCfgEntry,
       "fsMIOspfv3RedistRouteDestType": fsMIOspfv3RedistRouteDestType,
       "fsMIOspfv3RedistRouteDest": fsMIOspfv3RedistRouteDest,
       "fsMIOspfv3RedistRoutePfxLength": fsMIOspfv3RedistRoutePfxLength,
       "fsMIOspfv3RedistRouteMetric": fsMIOspfv3RedistRouteMetric,
       "fsMIOspfv3RedistRouteMetricType": fsMIOspfv3RedistRouteMetricType,
       "fsMIOspfv3RedistRouteTagType": fsMIOspfv3RedistRouteTagType,
       "fsMIOspfv3RedistRouteTag": fsMIOspfv3RedistRouteTag,
       "fsMIOspfv3RedistRouteStatus": fsMIOspfv3RedistRouteStatus,
       "fsMIOspfv3RRDGroup": fsMIOspfv3RRDGroup,
       "fsMIOspfv3RRDGeneralGroup": fsMIOspfv3RRDGeneralGroup,
       "fsMIOspfv3RRDRouteTable": fsMIOspfv3RRDRouteTable,
       "fsMIOspfv3RRDRouteEntry": fsMIOspfv3RRDRouteEntry,
       "fsMIOspfv3RRDStatus": fsMIOspfv3RRDStatus,
       "fsMIOspfv3RRDSrcProtoMask": fsMIOspfv3RRDSrcProtoMask,
       "fsMIOspfv3RRDRouteMapName": fsMIOspfv3RRDRouteMapName,
       "fsMIOspfv3DistInOutRouteMap": fsMIOspfv3DistInOutRouteMap,
       "fsMIOspfv3DistInOutRouteMapTable": fsMIOspfv3DistInOutRouteMapTable,
       "fsMIOspfv3DistInOutRouteMapEntry": fsMIOspfv3DistInOutRouteMapEntry,
       "fsMIOspfv3DistInOutRouteMapName": fsMIOspfv3DistInOutRouteMapName,
       "fsMIOspfv3DistInOutRouteMapType": fsMIOspfv3DistInOutRouteMapType,
       "fsMIOspfv3DistInOutRouteMapValue": fsMIOspfv3DistInOutRouteMapValue,
       "fsMIOspfv3DistInOutRouteMapRowStatus": fsMIOspfv3DistInOutRouteMapRowStatus,
       "fsMIOspfv3PreferenceGroup": fsMIOspfv3PreferenceGroup,
       "fsMIOspfv3PreferenceTable": fsMIOspfv3PreferenceTable,
       "fsMIOspfv3PreferenceEntry": fsMIOspfv3PreferenceEntry,
       "fsMIOspfv3PreferenceValue": fsMIOspfv3PreferenceValue,
       "fsMIOspfv3NeighborBfdGroup": fsMIOspfv3NeighborBfdGroup,
       "fsMIOspfv3NeighborBfdTable": fsMIOspfv3NeighborBfdTable,
       "fsMIOspfv3NeighborBfdEntry": fsMIOspfv3NeighborBfdEntry,
       "fsMIOspfv3NbrBfdState": fsMIOspfv3NbrBfdState,
       "fsMIOspfv3IfAuthTable": fsMIOspfv3IfAuthTable,
       "fsMIOspfv3IfAuthEntry": fsMIOspfv3IfAuthEntry,
       "fsMIOspfv3IfAuthIfIndex": fsMIOspfv3IfAuthIfIndex,
       "fsMIOspfv3IfAuthKeyId": fsMIOspfv3IfAuthKeyId,
       "fsMIOspfv3IfAuthKey": fsMIOspfv3IfAuthKey,
       "fsMIOspfv3IfAuthKeyStartAccept": fsMIOspfv3IfAuthKeyStartAccept,
       "fsMIOspfv3IfAuthKeyStartGenerate": fsMIOspfv3IfAuthKeyStartGenerate,
       "fsMIOspfv3IfAuthKeyStopGenerate": fsMIOspfv3IfAuthKeyStopGenerate,
       "fsMIOspfv3IfAuthKeyStopAccept": fsMIOspfv3IfAuthKeyStopAccept,
       "fsMIOspfv3IfAuthKeyStatus": fsMIOspfv3IfAuthKeyStatus,
       "fsMIOspfv3VirtIfAuthTable": fsMIOspfv3VirtIfAuthTable,
       "fsMIOspfv3VirtIfAuthEntry": fsMIOspfv3VirtIfAuthEntry,
       "fsMIOspfv3VirtIfAuthAreaId": fsMIOspfv3VirtIfAuthAreaId,
       "fsMIOspfv3VirtIfAuthNeighbor": fsMIOspfv3VirtIfAuthNeighbor,
       "fsMIOspfv3VirtIfAuthKeyId": fsMIOspfv3VirtIfAuthKeyId,
       "fsMIOspfv3VirtIfAuthKey": fsMIOspfv3VirtIfAuthKey,
       "fsMIOspfv3VirtIfAuthKeyStartAccept": fsMIOspfv3VirtIfAuthKeyStartAccept,
       "fsMIOspfv3VirtIfAuthKeyStartGenerate": fsMIOspfv3VirtIfAuthKeyStartGenerate,
       "fsMIOspfv3VirtIfAuthKeyStopGenerate": fsMIOspfv3VirtIfAuthKeyStopGenerate,
       "fsMIOspfv3VirtIfAuthKeyStopAccept": fsMIOspfv3VirtIfAuthKeyStopAccept,
       "fsMIOspfv3VirtIfAuthKeyStatus": fsMIOspfv3VirtIfAuthKeyStatus,
       "fsMIOspfv3VirtIfCryptoAuthTable": fsMIOspfv3VirtIfCryptoAuthTable,
       "fsMIOspfv3VirtIfCryptoAuthEntry": fsMIOspfv3VirtIfCryptoAuthEntry,
       "fsMIOspfv3VirtIfCryptoAuthType": fsMIOspfv3VirtIfCryptoAuthType,
       "fsMIOspfv3VirtIfCryptoAuthMode": fsMIOspfv3VirtIfCryptoAuthMode,
       "fsMIOspfv3Notification": fsMIOspfv3Notification,
       "fsMIOspfv3Traps": fsMIOspfv3Traps,
       "fsMIOspfv3RestartStatusChange": fsMIOspfv3RestartStatusChange,
       "fsMIOspfv3NbrRestartHelperStatusChange": fsMIOspfv3NbrRestartHelperStatusChange,
       "fsMIOspfv3VirtNbrRestartHelperStatusChange": fsMIOspfv3VirtNbrRestartHelperStatusChange,
       "fsMIOspfv3HotStandbyStateChgTrap": fsMIOspfv3HotStandbyStateChgTrap,
       "fsMIOspfv3HotStandbyBulkUpdAbortTrap": fsMIOspfv3HotStandbyBulkUpdAbortTrap,
       "fsMIOspfv3AuthSequenceNumWrap": fsMIOspfv3AuthSequenceNumWrap,
       "fsMIOspfv3TrapObject": fsMIOspfv3TrapObject,
       "fsMIOspfv3TrapNbrIfIndex": fsMIOspfv3TrapNbrIfIndex,
       "fsMIOspfv3TrapVirtNbrRtrId": fsMIOspfv3TrapVirtNbrRtrId,
       "fsMIOspfv3TrapNbrRtrId": fsMIOspfv3TrapNbrRtrId,
       "fsMIOspfv3TrapVirtNbrArea": fsMIOspfv3TrapVirtNbrArea,
       "fsMIOspfv3TrapBulkUpdAbortReason": fsMIOspfv3TrapBulkUpdAbortReason}
)
