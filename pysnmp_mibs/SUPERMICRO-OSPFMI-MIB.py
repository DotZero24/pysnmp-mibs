# SNMP MIB module (SUPERMICRO-OSPFMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-OSPFMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:26 2025
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

(AreaID,
 BigMetric,
 PositiveInteger,
 RouterID,
 Status,
 TOSType,
 fsMIStdOspfContextId,
 fsMIStdOspfEntry,
 fsMIStdOspfNbrRtrId,
 fsMIStdOspfRouterId,
 fsMIStdOspfVirtNbrEntry) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTDOSPF-MIB",
    "AreaID",
    "BigMetric",
    "PositiveInteger",
    "RouterID",
    "Status",
    "TOSType",
    "fsMIStdOspfContextId",
    "fsMIStdOspfEntry",
    "fsMIStdOspfNbrRtrId",
    "fsMIStdOspfRouterId",
    "fsMIStdOspfVirtNbrEntry")


# MODULE-IDENTITY

fsMIOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145)
)
if mibBuilder.loadTexts:
    fsMIOspf.setRevisions(
        ("2012-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIOspfGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIOspfGeneralGroup = _FsMIOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1)
)
_FsMIOspfGlobalTraceLevel_Type = Integer32
_FsMIOspfGlobalTraceLevel_Object = MibScalar
fsMIOspfGlobalTraceLevel = _FsMIOspfGlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 1),
    _FsMIOspfGlobalTraceLevel_Type()
)
fsMIOspfGlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfGlobalTraceLevel.setStatus("current")


class _FsMIOspfVrfSpfInterval_Type(Integer32):
    """Custom type fsMIOspfVrfSpfInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsMIOspfVrfSpfInterval_Type.__name__ = "Integer32"
_FsMIOspfVrfSpfInterval_Object = MibScalar
fsMIOspfVrfSpfInterval = _FsMIOspfVrfSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 2),
    _FsMIOspfVrfSpfInterval_Type()
)
fsMIOspfVrfSpfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVrfSpfInterval.setStatus("current")
_FsMIOspfTable_Object = MibTable
fsMIOspfTable = _FsMIOspfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIOspfTable.setStatus("current")
_FsMIOspfEntry_Object = MibTableRow
fsMIOspfEntry = _FsMIOspfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfEntry.setStatus("current")


class _FsMIOspfOverFlowState_Type(TruthValue):
    """Custom type fsMIOspfOverFlowState based on TruthValue"""
    defaultValue = 2


_FsMIOspfOverFlowState_Type.__name__ = "TruthValue"
_FsMIOspfOverFlowState_Object = MibTableColumn
fsMIOspfOverFlowState = _FsMIOspfOverFlowState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 1),
    _FsMIOspfOverFlowState_Type()
)
fsMIOspfOverFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfOverFlowState.setStatus("current")
_FsMIOspfPktsRcvd_Type = Counter32
_FsMIOspfPktsRcvd_Object = MibTableColumn
fsMIOspfPktsRcvd = _FsMIOspfPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 2),
    _FsMIOspfPktsRcvd_Type()
)
fsMIOspfPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfPktsRcvd.setStatus("current")
_FsMIOspfPktsTxed_Type = Counter32
_FsMIOspfPktsTxed_Object = MibTableColumn
fsMIOspfPktsTxed = _FsMIOspfPktsTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 3),
    _FsMIOspfPktsTxed_Type()
)
fsMIOspfPktsTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfPktsTxed.setStatus("current")
_FsMIOspfPktsDisd_Type = Counter32
_FsMIOspfPktsDisd_Object = MibTableColumn
fsMIOspfPktsDisd = _FsMIOspfPktsDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 4),
    _FsMIOspfPktsDisd_Type()
)
fsMIOspfPktsDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfPktsDisd.setStatus("current")


class _FsMIOspfRFC1583Compatibility_Type(Status):
    """Custom type fsMIOspfRFC1583Compatibility based on Status"""
    defaultValue = 1


_FsMIOspfRFC1583Compatibility_Type.__name__ = "Status"
_FsMIOspfRFC1583Compatibility_Object = MibTableColumn
fsMIOspfRFC1583Compatibility = _FsMIOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 5),
    _FsMIOspfRFC1583Compatibility_Type()
)
fsMIOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRFC1583Compatibility.setStatus("current")


class _FsMIOspfTraceLevel_Type(Integer32):
    """Custom type fsMIOspfTraceLevel based on Integer32"""
    defaultValue = 2048


_FsMIOspfTraceLevel_Type.__name__ = "Integer32"
_FsMIOspfTraceLevel_Object = MibTableColumn
fsMIOspfTraceLevel = _FsMIOspfTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 12),
    _FsMIOspfTraceLevel_Type()
)
fsMIOspfTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfTraceLevel.setStatus("current")


class _FsMIOspfMinLsaInterval_Type(Integer32):
    """Custom type fsMIOspfMinLsaInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIOspfMinLsaInterval_Type.__name__ = "Integer32"
_FsMIOspfMinLsaInterval_Object = MibTableColumn
fsMIOspfMinLsaInterval = _FsMIOspfMinLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 13),
    _FsMIOspfMinLsaInterval_Type()
)
fsMIOspfMinLsaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfMinLsaInterval.setStatus("current")


class _FsMIOspfABRType_Type(Integer32):
    """Custom type fsMIOspfABRType based on Integer32"""
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


_FsMIOspfABRType_Type.__name__ = "Integer32"
_FsMIOspfABRType_Object = MibTableColumn
fsMIOspfABRType = _FsMIOspfABRType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 14),
    _FsMIOspfABRType_Type()
)
fsMIOspfABRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfABRType.setStatus("current")


class _FsMIOspfNssaAsbrDefRtTrans_Type(Integer32):
    """Custom type fsMIOspfNssaAsbrDefRtTrans based on Integer32"""
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


_FsMIOspfNssaAsbrDefRtTrans_Type.__name__ = "Integer32"
_FsMIOspfNssaAsbrDefRtTrans_Object = MibTableColumn
fsMIOspfNssaAsbrDefRtTrans = _FsMIOspfNssaAsbrDefRtTrans_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 15),
    _FsMIOspfNssaAsbrDefRtTrans_Type()
)
fsMIOspfNssaAsbrDefRtTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfNssaAsbrDefRtTrans.setStatus("current")


class _FsMIOspfDefaultPassiveInterface_Type(TruthValue):
    """Custom type fsMIOspfDefaultPassiveInterface based on TruthValue"""
    defaultValue = 2


_FsMIOspfDefaultPassiveInterface_Type.__name__ = "TruthValue"
_FsMIOspfDefaultPassiveInterface_Object = MibTableColumn
fsMIOspfDefaultPassiveInterface = _FsMIOspfDefaultPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 16),
    _FsMIOspfDefaultPassiveInterface_Type()
)
fsMIOspfDefaultPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfDefaultPassiveInterface.setStatus("current")


class _FsMIOspfSpfHoldtime_Type(Integer32):
    """Custom type fsMIOspfSpfHoldtime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfSpfHoldtime_Type.__name__ = "Integer32"
_FsMIOspfSpfHoldtime_Object = MibTableColumn
fsMIOspfSpfHoldtime = _FsMIOspfSpfHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 17),
    _FsMIOspfSpfHoldtime_Type()
)
fsMIOspfSpfHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfSpfHoldtime.setStatus("current")


class _FsMIOspfSpfDelay_Type(Integer32):
    """Custom type fsMIOspfSpfDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfSpfDelay_Type.__name__ = "Integer32"
_FsMIOspfSpfDelay_Object = MibTableColumn
fsMIOspfSpfDelay = _FsMIOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 18),
    _FsMIOspfSpfDelay_Type()
)
fsMIOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfSpfDelay.setStatus("current")


class _FsMIOspfRestartSupport_Type(Integer32):
    """Custom type fsMIOspfRestartSupport based on Integer32"""
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
        *(("none", 1),
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_FsMIOspfRestartSupport_Type.__name__ = "Integer32"
_FsMIOspfRestartSupport_Object = MibTableColumn
fsMIOspfRestartSupport = _FsMIOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 19),
    _FsMIOspfRestartSupport_Type()
)
fsMIOspfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRestartSupport.setStatus("current")


class _FsMIOspfRestartInterval_Type(Integer32):
    """Custom type fsMIOspfRestartInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_FsMIOspfRestartInterval_Type.__name__ = "Integer32"
_FsMIOspfRestartInterval_Object = MibTableColumn
fsMIOspfRestartInterval = _FsMIOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 20),
    _FsMIOspfRestartInterval_Type()
)
fsMIOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRestartInterval.setStatus("current")


class _FsMIOspfRestartStrictLsaChecking_Type(TruthValue):
    """Custom type fsMIOspfRestartStrictLsaChecking based on TruthValue"""
    defaultValue = 2


_FsMIOspfRestartStrictLsaChecking_Type.__name__ = "TruthValue"
_FsMIOspfRestartStrictLsaChecking_Object = MibTableColumn
fsMIOspfRestartStrictLsaChecking = _FsMIOspfRestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 21),
    _FsMIOspfRestartStrictLsaChecking_Type()
)
fsMIOspfRestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRestartStrictLsaChecking.setStatus("current")


class _FsMIOspfRestartStatus_Type(Integer32):
    """Custom type fsMIOspfRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_FsMIOspfRestartStatus_Type.__name__ = "Integer32"
_FsMIOspfRestartStatus_Object = MibTableColumn
fsMIOspfRestartStatus = _FsMIOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 22),
    _FsMIOspfRestartStatus_Type()
)
fsMIOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRestartStatus.setStatus("current")
_FsMIOspfRestartAge_Type = Unsigned32
_FsMIOspfRestartAge_Object = MibTableColumn
fsMIOspfRestartAge = _FsMIOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 23),
    _FsMIOspfRestartAge_Type()
)
fsMIOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMIOspfRestartAge.setUnits("seconds")


class _FsMIOspfRestartExitReason_Type(Integer32):
    """Custom type fsMIOspfRestartExitReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_FsMIOspfRestartExitReason_Type.__name__ = "Integer32"
_FsMIOspfRestartExitReason_Object = MibTableColumn
fsMIOspfRestartExitReason = _FsMIOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 24),
    _FsMIOspfRestartExitReason_Type()
)
fsMIOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRestartExitReason.setStatus("current")


class _FsMIOspfHelperSupport_Type(Bits):
    """Custom type fsMIOspfHelperSupport based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2),
          ("switchToRedundant", 3))
    )

_FsMIOspfHelperSupport_Type.__name__ = "Bits"
_FsMIOspfHelperSupport_Object = MibTableColumn
fsMIOspfHelperSupport = _FsMIOspfHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 25),
    _FsMIOspfHelperSupport_Type()
)
fsMIOspfHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfHelperSupport.setStatus("current")
_FsMIOspfExtTraceLevel_Type = Integer32
_FsMIOspfExtTraceLevel_Object = MibTableColumn
fsMIOspfExtTraceLevel = _FsMIOspfExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 26),
    _FsMIOspfExtTraceLevel_Type()
)
fsMIOspfExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfExtTraceLevel.setStatus("current")


class _FsMIOspfHelperGraceTimeLimit_Type(Integer32):
    """Custom type fsMIOspfHelperGraceTimeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_FsMIOspfHelperGraceTimeLimit_Type.__name__ = "Integer32"
_FsMIOspfHelperGraceTimeLimit_Object = MibTableColumn
fsMIOspfHelperGraceTimeLimit = _FsMIOspfHelperGraceTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 27),
    _FsMIOspfHelperGraceTimeLimit_Type()
)
fsMIOspfHelperGraceTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfHelperGraceTimeLimit.setStatus("current")


class _FsMIOspfRestartAckState_Type(Integer32):
    """Custom type fsMIOspfRestartAckState based on Integer32"""
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


_FsMIOspfRestartAckState_Type.__name__ = "Integer32"
_FsMIOspfRestartAckState_Object = MibTableColumn
fsMIOspfRestartAckState = _FsMIOspfRestartAckState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 28),
    _FsMIOspfRestartAckState_Type()
)
fsMIOspfRestartAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRestartAckState.setStatus("current")


class _FsMIOspfGraceLsaRetransmitCount_Type(Integer32):
    """Custom type fsMIOspfGraceLsaRetransmitCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FsMIOspfGraceLsaRetransmitCount_Type.__name__ = "Integer32"
_FsMIOspfGraceLsaRetransmitCount_Object = MibTableColumn
fsMIOspfGraceLsaRetransmitCount = _FsMIOspfGraceLsaRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 29),
    _FsMIOspfGraceLsaRetransmitCount_Type()
)
fsMIOspfGraceLsaRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfGraceLsaRetransmitCount.setStatus("current")


class _FsMIOspfRestartReason_Type(Integer32):
    """Custom type fsMIOspfRestartReason based on Integer32"""
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


_FsMIOspfRestartReason_Type.__name__ = "Integer32"
_FsMIOspfRestartReason_Object = MibTableColumn
fsMIOspfRestartReason = _FsMIOspfRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 30),
    _FsMIOspfRestartReason_Type()
)
fsMIOspfRestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRestartReason.setStatus("current")


class _FsMIOspfRTStaggeringInterval_Type(TimeTicks):
    """Custom type fsMIOspfRTStaggeringInterval based on TimeTicks"""
    defaultValue = 10000


_FsMIOspfRTStaggeringInterval_Type.__name__ = "TimeTicks"
_FsMIOspfRTStaggeringInterval_Object = MibTableColumn
fsMIOspfRTStaggeringInterval = _FsMIOspfRTStaggeringInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 31),
    _FsMIOspfRTStaggeringInterval_Type()
)
fsMIOspfRTStaggeringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRTStaggeringInterval.setStatus("current")


class _FsMIOspfRouterIdPermanence_Type(Integer32):
    """Custom type fsMIOspfRouterIdPermanence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_FsMIOspfRouterIdPermanence_Type.__name__ = "Integer32"
_FsMIOspfRouterIdPermanence_Object = MibTableColumn
fsMIOspfRouterIdPermanence = _FsMIOspfRouterIdPermanence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 32),
    _FsMIOspfRouterIdPermanence_Type()
)
fsMIOspfRouterIdPermanence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRouterIdPermanence.setStatus("current")


class _FsMIOspfBfdStatus_Type(Integer32):
    """Custom type fsMIOspfBfdStatus based on Integer32"""
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


_FsMIOspfBfdStatus_Type.__name__ = "Integer32"
_FsMIOspfBfdStatus_Object = MibTableColumn
fsMIOspfBfdStatus = _FsMIOspfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 33),
    _FsMIOspfBfdStatus_Type()
)
fsMIOspfBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfBfdStatus.setStatus("current")


class _FsMIOspfBfdAllIfState_Type(Integer32):
    """Custom type fsMIOspfBfdAllIfState based on Integer32"""
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


_FsMIOspfBfdAllIfState_Type.__name__ = "Integer32"
_FsMIOspfBfdAllIfState_Object = MibTableColumn
fsMIOspfBfdAllIfState = _FsMIOspfBfdAllIfState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 3, 1, 34),
    _FsMIOspfBfdAllIfState_Type()
)
fsMIOspfBfdAllIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfBfdAllIfState.setStatus("current")


class _FsMIOspfRTStaggeringStatus_Type(Integer32):
    """Custom type fsMIOspfRTStaggeringStatus based on Integer32"""
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


_FsMIOspfRTStaggeringStatus_Type.__name__ = "Integer32"
_FsMIOspfRTStaggeringStatus_Object = MibScalar
fsMIOspfRTStaggeringStatus = _FsMIOspfRTStaggeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 4),
    _FsMIOspfRTStaggeringStatus_Type()
)
fsMIOspfRTStaggeringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRTStaggeringStatus.setStatus("current")


class _FsMIOspfHotStandbyAdminStatus_Type(Integer32):
    """Custom type fsMIOspfHotStandbyAdminStatus based on Integer32"""
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


_FsMIOspfHotStandbyAdminStatus_Type.__name__ = "Integer32"
_FsMIOspfHotStandbyAdminStatus_Object = MibScalar
fsMIOspfHotStandbyAdminStatus = _FsMIOspfHotStandbyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 5),
    _FsMIOspfHotStandbyAdminStatus_Type()
)
fsMIOspfHotStandbyAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfHotStandbyAdminStatus.setStatus("current")


class _FsMIOspfHotStandbyState_Type(Integer32):
    """Custom type fsMIOspfHotStandbyState based on Integer32"""
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


_FsMIOspfHotStandbyState_Type.__name__ = "Integer32"
_FsMIOspfHotStandbyState_Object = MibScalar
fsMIOspfHotStandbyState = _FsMIOspfHotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 6),
    _FsMIOspfHotStandbyState_Type()
)
fsMIOspfHotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfHotStandbyState.setStatus("current")


class _FsMIOspfDynamicBulkUpdStatus_Type(Integer32):
    """Custom type fsMIOspfDynamicBulkUpdStatus based on Integer32"""
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


_FsMIOspfDynamicBulkUpdStatus_Type.__name__ = "Integer32"
_FsMIOspfDynamicBulkUpdStatus_Object = MibScalar
fsMIOspfDynamicBulkUpdStatus = _FsMIOspfDynamicBulkUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 7),
    _FsMIOspfDynamicBulkUpdStatus_Type()
)
fsMIOspfDynamicBulkUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfDynamicBulkUpdStatus.setStatus("current")
_FsMIOspfStanbyHelloSyncCount_Type = Counter32
_FsMIOspfStanbyHelloSyncCount_Object = MibScalar
fsMIOspfStanbyHelloSyncCount = _FsMIOspfStanbyHelloSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 8),
    _FsMIOspfStanbyHelloSyncCount_Type()
)
fsMIOspfStanbyHelloSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfStanbyHelloSyncCount.setStatus("current")
_FsMIOspfStanbyLsaSyncCount_Type = Counter32
_FsMIOspfStanbyLsaSyncCount_Object = MibScalar
fsMIOspfStanbyLsaSyncCount = _FsMIOspfStanbyLsaSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 9),
    _FsMIOspfStanbyLsaSyncCount_Type()
)
fsMIOspfStanbyLsaSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfStanbyLsaSyncCount.setStatus("current")
_FsMIOspfGlobalExtTraceLevel_Type = Integer32
_FsMIOspfGlobalExtTraceLevel_Object = MibScalar
fsMIOspfGlobalExtTraceLevel = _FsMIOspfGlobalExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 1, 10),
    _FsMIOspfGlobalExtTraceLevel_Type()
)
fsMIOspfGlobalExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfGlobalExtTraceLevel.setStatus("current")
_FsMIOspfAreaTable_Object = MibTable
fsMIOspfAreaTable = _FsMIOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfAreaTable.setStatus("current")
_FsMIOspfAreaEntry_Object = MibTableRow
fsMIOspfAreaEntry = _FsMIOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1)
)
fsMIOspfAreaEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAreaId"),
)
if mibBuilder.loadTexts:
    fsMIOspfAreaEntry.setStatus("current")
_FsMIOspfAreaId_Type = AreaID
_FsMIOspfAreaId_Object = MibTableColumn
fsMIOspfAreaId = _FsMIOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 1),
    _FsMIOspfAreaId_Type()
)
fsMIOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAreaId.setStatus("current")
_FsMIOspfAreaIfCount_Type = Gauge32
_FsMIOspfAreaIfCount_Object = MibTableColumn
fsMIOspfAreaIfCount = _FsMIOspfAreaIfCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 2),
    _FsMIOspfAreaIfCount_Type()
)
fsMIOspfAreaIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAreaIfCount.setStatus("current")
_FsMIOspfAreaNetCount_Type = Gauge32
_FsMIOspfAreaNetCount_Object = MibTableColumn
fsMIOspfAreaNetCount = _FsMIOspfAreaNetCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 3),
    _FsMIOspfAreaNetCount_Type()
)
fsMIOspfAreaNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAreaNetCount.setStatus("current")
_FsMIOspfAreaRtrCount_Type = Gauge32
_FsMIOspfAreaRtrCount_Object = MibTableColumn
fsMIOspfAreaRtrCount = _FsMIOspfAreaRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 4),
    _FsMIOspfAreaRtrCount_Type()
)
fsMIOspfAreaRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAreaRtrCount.setStatus("current")


class _FsMIOspfAreaNSSATranslatorRole_Type(Integer32):
    """Custom type fsMIOspfAreaNSSATranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_FsMIOspfAreaNSSATranslatorRole_Type.__name__ = "Integer32"
_FsMIOspfAreaNSSATranslatorRole_Object = MibTableColumn
fsMIOspfAreaNSSATranslatorRole = _FsMIOspfAreaNSSATranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 5),
    _FsMIOspfAreaNSSATranslatorRole_Type()
)
fsMIOspfAreaNSSATranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAreaNSSATranslatorRole.setStatus("current")


class _FsMIOspfAreaNSSATranslatorState_Type(Integer32):
    """Custom type fsMIOspfAreaNSSATranslatorState based on Integer32"""
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
        *(("enabled", 1),
          ("elected", 2),
          ("disabled", 3))
    )


_FsMIOspfAreaNSSATranslatorState_Type.__name__ = "Integer32"
_FsMIOspfAreaNSSATranslatorState_Object = MibTableColumn
fsMIOspfAreaNSSATranslatorState = _FsMIOspfAreaNSSATranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 6),
    _FsMIOspfAreaNSSATranslatorState_Type()
)
fsMIOspfAreaNSSATranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAreaNSSATranslatorState.setStatus("current")


class _FsMIOspfAreaNSSATranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type fsMIOspfAreaNSSATranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_FsMIOspfAreaNSSATranslatorStabilityInterval_Type.__name__ = "PositiveInteger"
_FsMIOspfAreaNSSATranslatorStabilityInterval_Object = MibTableColumn
fsMIOspfAreaNSSATranslatorStabilityInterval = _FsMIOspfAreaNSSATranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 7),
    _FsMIOspfAreaNSSATranslatorStabilityInterval_Type()
)
fsMIOspfAreaNSSATranslatorStabilityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAreaNSSATranslatorStabilityInterval.setStatus("current")
_FsMIOspfAreaNSSATranslatorEvents_Type = Counter32
_FsMIOspfAreaNSSATranslatorEvents_Object = MibTableColumn
fsMIOspfAreaNSSATranslatorEvents = _FsMIOspfAreaNSSATranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 8),
    _FsMIOspfAreaNSSATranslatorEvents_Type()
)
fsMIOspfAreaNSSATranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAreaNSSATranslatorEvents.setStatus("current")


class _FsMIOspfAreaDfInfOriginate_Type(Integer32):
    """Custom type fsMIOspfAreaDfInfOriginate based on Integer32"""
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


_FsMIOspfAreaDfInfOriginate_Type.__name__ = "Integer32"
_FsMIOspfAreaDfInfOriginate_Object = MibTableColumn
fsMIOspfAreaDfInfOriginate = _FsMIOspfAreaDfInfOriginate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 2, 1, 9),
    _FsMIOspfAreaDfInfOriginate_Type()
)
fsMIOspfAreaDfInfOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAreaDfInfOriginate.setStatus("current")
_FsMIOspfHostTable_Object = MibTable
fsMIOspfHostTable = _FsMIOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 3)
)
if mibBuilder.loadTexts:
    fsMIOspfHostTable.setStatus("current")
_FsMIOspfHostEntry_Object = MibTableRow
fsMIOspfHostEntry = _FsMIOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 3, 1)
)
fsMIOspfHostEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfHostIpAddress"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfHostTOS"),
)
if mibBuilder.loadTexts:
    fsMIOspfHostEntry.setStatus("current")
_FsMIOspfHostIpAddress_Type = IpAddress
_FsMIOspfHostIpAddress_Object = MibTableColumn
fsMIOspfHostIpAddress = _FsMIOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 3, 1, 1),
    _FsMIOspfHostIpAddress_Type()
)
fsMIOspfHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfHostIpAddress.setStatus("current")
_FsMIOspfHostTOS_Type = TOSType
_FsMIOspfHostTOS_Object = MibTableColumn
fsMIOspfHostTOS = _FsMIOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 3, 1, 2),
    _FsMIOspfHostTOS_Type()
)
fsMIOspfHostTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfHostTOS.setStatus("current")


class _FsMIOspfHostRouteIfIndex_Type(Integer32):
    """Custom type fsMIOspfHostRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfHostRouteIfIndex_Type.__name__ = "Integer32"
_FsMIOspfHostRouteIfIndex_Object = MibTableColumn
fsMIOspfHostRouteIfIndex = _FsMIOspfHostRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 3, 1, 3),
    _FsMIOspfHostRouteIfIndex_Type()
)
fsMIOspfHostRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfHostRouteIfIndex.setStatus("current")
_FsMIOspfIfTable_Object = MibTable
fsMIOspfIfTable = _FsMIOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4)
)
if mibBuilder.loadTexts:
    fsMIOspfIfTable.setStatus("current")
_FsMIOspfIfEntry_Object = MibTableRow
fsMIOspfIfEntry = _FsMIOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1)
)
fsMIOspfIfEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfIpAddress"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    fsMIOspfIfEntry.setStatus("current")
_FsMIOspfIfIpAddress_Type = IpAddress
_FsMIOspfIfIpAddress_Object = MibTableColumn
fsMIOspfIfIpAddress = _FsMIOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 1),
    _FsMIOspfIfIpAddress_Type()
)
fsMIOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfIpAddress.setStatus("current")


class _FsMIOspfAddressLessIf_Type(Integer32):
    """Custom type fsMIOspfAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfAddressLessIf_Type.__name__ = "Integer32"
_FsMIOspfAddressLessIf_Object = MibTableColumn
fsMIOspfAddressLessIf = _FsMIOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 2),
    _FsMIOspfAddressLessIf_Type()
)
fsMIOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAddressLessIf.setStatus("current")


class _FsMIOspfIfOperState_Type(Integer32):
    """Custom type fsMIOspfIfOperState based on Integer32"""
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


_FsMIOspfIfOperState_Type.__name__ = "Integer32"
_FsMIOspfIfOperState_Object = MibTableColumn
fsMIOspfIfOperState = _FsMIOspfIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 3),
    _FsMIOspfIfOperState_Type()
)
fsMIOspfIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfOperState.setStatus("current")


class _FsMIOspfIfPassive_Type(TruthValue):
    """Custom type fsMIOspfIfPassive based on TruthValue"""
    defaultValue = 2


_FsMIOspfIfPassive_Type.__name__ = "TruthValue"
_FsMIOspfIfPassive_Object = MibTableColumn
fsMIOspfIfPassive = _FsMIOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 4),
    _FsMIOspfIfPassive_Type()
)
fsMIOspfIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfPassive.setStatus("current")
_FsMIOspfIfNbrCount_Type = Gauge32
_FsMIOspfIfNbrCount_Object = MibTableColumn
fsMIOspfIfNbrCount = _FsMIOspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 5),
    _FsMIOspfIfNbrCount_Type()
)
fsMIOspfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfNbrCount.setStatus("current")
_FsMIOspfIfAdjCount_Type = Gauge32
_FsMIOspfIfAdjCount_Object = MibTableColumn
fsMIOspfIfAdjCount = _FsMIOspfIfAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 6),
    _FsMIOspfIfAdjCount_Type()
)
fsMIOspfIfAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfAdjCount.setStatus("current")
_FsMIOspfIfHelloRcvd_Type = Counter32
_FsMIOspfIfHelloRcvd_Object = MibTableColumn
fsMIOspfIfHelloRcvd = _FsMIOspfIfHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 7),
    _FsMIOspfIfHelloRcvd_Type()
)
fsMIOspfIfHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfHelloRcvd.setStatus("current")
_FsMIOspfIfHelloTxed_Type = Counter32
_FsMIOspfIfHelloTxed_Object = MibTableColumn
fsMIOspfIfHelloTxed = _FsMIOspfIfHelloTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 8),
    _FsMIOspfIfHelloTxed_Type()
)
fsMIOspfIfHelloTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfHelloTxed.setStatus("current")
_FsMIOspfIfHelloDisd_Type = Counter32
_FsMIOspfIfHelloDisd_Object = MibTableColumn
fsMIOspfIfHelloDisd = _FsMIOspfIfHelloDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 9),
    _FsMIOspfIfHelloDisd_Type()
)
fsMIOspfIfHelloDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfHelloDisd.setStatus("current")
_FsMIOspfIfDdpRcvd_Type = Counter32
_FsMIOspfIfDdpRcvd_Object = MibTableColumn
fsMIOspfIfDdpRcvd = _FsMIOspfIfDdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 10),
    _FsMIOspfIfDdpRcvd_Type()
)
fsMIOspfIfDdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfDdpRcvd.setStatus("current")
_FsMIOspfIfDdpTxed_Type = Counter32
_FsMIOspfIfDdpTxed_Object = MibTableColumn
fsMIOspfIfDdpTxed = _FsMIOspfIfDdpTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 11),
    _FsMIOspfIfDdpTxed_Type()
)
fsMIOspfIfDdpTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfDdpTxed.setStatus("current")
_FsMIOspfIfDdpDisd_Type = Counter32
_FsMIOspfIfDdpDisd_Object = MibTableColumn
fsMIOspfIfDdpDisd = _FsMIOspfIfDdpDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 12),
    _FsMIOspfIfDdpDisd_Type()
)
fsMIOspfIfDdpDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfDdpDisd.setStatus("current")
_FsMIOspfIfLrqRcvd_Type = Counter32
_FsMIOspfIfLrqRcvd_Object = MibTableColumn
fsMIOspfIfLrqRcvd = _FsMIOspfIfLrqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 13),
    _FsMIOspfIfLrqRcvd_Type()
)
fsMIOspfIfLrqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLrqRcvd.setStatus("current")
_FsMIOspfIfLrqTxed_Type = Counter32
_FsMIOspfIfLrqTxed_Object = MibTableColumn
fsMIOspfIfLrqTxed = _FsMIOspfIfLrqTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 14),
    _FsMIOspfIfLrqTxed_Type()
)
fsMIOspfIfLrqTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLrqTxed.setStatus("current")
_FsMIOspfIfLrqDisd_Type = Counter32
_FsMIOspfIfLrqDisd_Object = MibTableColumn
fsMIOspfIfLrqDisd = _FsMIOspfIfLrqDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 15),
    _FsMIOspfIfLrqDisd_Type()
)
fsMIOspfIfLrqDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLrqDisd.setStatus("current")
_FsMIOspfIfLsuRcvd_Type = Counter32
_FsMIOspfIfLsuRcvd_Object = MibTableColumn
fsMIOspfIfLsuRcvd = _FsMIOspfIfLsuRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 16),
    _FsMIOspfIfLsuRcvd_Type()
)
fsMIOspfIfLsuRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLsuRcvd.setStatus("current")
_FsMIOspfIfLsuTxed_Type = Counter32
_FsMIOspfIfLsuTxed_Object = MibTableColumn
fsMIOspfIfLsuTxed = _FsMIOspfIfLsuTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 17),
    _FsMIOspfIfLsuTxed_Type()
)
fsMIOspfIfLsuTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLsuTxed.setStatus("current")
_FsMIOspfIfLsuDisd_Type = Counter32
_FsMIOspfIfLsuDisd_Object = MibTableColumn
fsMIOspfIfLsuDisd = _FsMIOspfIfLsuDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 18),
    _FsMIOspfIfLsuDisd_Type()
)
fsMIOspfIfLsuDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLsuDisd.setStatus("current")
_FsMIOspfIfLakRcvd_Type = Counter32
_FsMIOspfIfLakRcvd_Object = MibTableColumn
fsMIOspfIfLakRcvd = _FsMIOspfIfLakRcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 19),
    _FsMIOspfIfLakRcvd_Type()
)
fsMIOspfIfLakRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLakRcvd.setStatus("current")
_FsMIOspfIfLakTxed_Type = Counter32
_FsMIOspfIfLakTxed_Object = MibTableColumn
fsMIOspfIfLakTxed = _FsMIOspfIfLakTxed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 20),
    _FsMIOspfIfLakTxed_Type()
)
fsMIOspfIfLakTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLakTxed.setStatus("current")
_FsMIOspfIfLakDisd_Type = Counter32
_FsMIOspfIfLakDisd_Object = MibTableColumn
fsMIOspfIfLakDisd = _FsMIOspfIfLakDisd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 21),
    _FsMIOspfIfLakDisd_Type()
)
fsMIOspfIfLakDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfIfLakDisd.setStatus("current")


class _FsMIOspfIfBfdState_Type(Integer32):
    """Custom type fsMIOspfIfBfdState based on Integer32"""
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


_FsMIOspfIfBfdState_Type.__name__ = "Integer32"
_FsMIOspfIfBfdState_Object = MibTableColumn
fsMIOspfIfBfdState = _FsMIOspfIfBfdState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 4, 1, 22),
    _FsMIOspfIfBfdState_Type()
)
fsMIOspfIfBfdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfBfdState.setStatus("current")
_FsMIOspfIfMD5AuthTable_Object = MibTable
fsMIOspfIfMD5AuthTable = _FsMIOspfIfMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5)
)
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthTable.setStatus("current")
_FsMIOspfIfMD5AuthEntry_Object = MibTableRow
fsMIOspfIfMD5AuthEntry = _FsMIOspfIfMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1)
)
fsMIOspfIfMD5AuthEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfMD5AuthIpAddress"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfMD5AuthAddressLessIf"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfMD5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthEntry.setStatus("current")
_FsMIOspfIfMD5AuthIpAddress_Type = IpAddress
_FsMIOspfIfMD5AuthIpAddress_Object = MibTableColumn
fsMIOspfIfMD5AuthIpAddress = _FsMIOspfIfMD5AuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 1),
    _FsMIOspfIfMD5AuthIpAddress_Type()
)
fsMIOspfIfMD5AuthIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthIpAddress.setStatus("current")


class _FsMIOspfIfMD5AuthAddressLessIf_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfIfMD5AuthAddressLessIf_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthAddressLessIf_Object = MibTableColumn
fsMIOspfIfMD5AuthAddressLessIf = _FsMIOspfIfMD5AuthAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 2),
    _FsMIOspfIfMD5AuthAddressLessIf_Type()
)
fsMIOspfIfMD5AuthAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthAddressLessIf.setStatus("current")


class _FsMIOspfIfMD5AuthKeyId_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfIfMD5AuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyId_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyId = _FsMIOspfIfMD5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 3),
    _FsMIOspfIfMD5AuthKeyId_Type()
)
fsMIOspfIfMD5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyId.setStatus("current")


class _FsMIOspfIfMD5AuthKey_Type(OctetString):
    """Custom type fsMIOspfIfMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfIfMD5AuthKey_Type.__name__ = "OctetString"
_FsMIOspfIfMD5AuthKey_Object = MibTableColumn
fsMIOspfIfMD5AuthKey = _FsMIOspfIfMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 4),
    _FsMIOspfIfMD5AuthKey_Type()
)
fsMIOspfIfMD5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKey.setStatus("current")


class _FsMIOspfIfMD5AuthKeyStartAccept_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyStartAccept based on Integer32"""
    defaultValue = 0


_FsMIOspfIfMD5AuthKeyStartAccept_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyStartAccept_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyStartAccept = _FsMIOspfIfMD5AuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 5),
    _FsMIOspfIfMD5AuthKeyStartAccept_Type()
)
fsMIOspfIfMD5AuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyStartAccept.setStatus("current")


class _FsMIOspfIfMD5AuthKeyStartGenerate_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyStartGenerate based on Integer32"""
    defaultValue = 0


_FsMIOspfIfMD5AuthKeyStartGenerate_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyStartGenerate = _FsMIOspfIfMD5AuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 6),
    _FsMIOspfIfMD5AuthKeyStartGenerate_Type()
)
fsMIOspfIfMD5AuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyStartGenerate.setStatus("current")


class _FsMIOspfIfMD5AuthKeyStopGenerate_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyStopGenerate based on Integer32"""
    defaultValue = -1


_FsMIOspfIfMD5AuthKeyStopGenerate_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyStopGenerate = _FsMIOspfIfMD5AuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 7),
    _FsMIOspfIfMD5AuthKeyStopGenerate_Type()
)
fsMIOspfIfMD5AuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyStopGenerate.setStatus("current")


class _FsMIOspfIfMD5AuthKeyStopAccept_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyStopAccept based on Integer32"""
    defaultValue = -1


_FsMIOspfIfMD5AuthKeyStopAccept_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyStopAccept_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyStopAccept = _FsMIOspfIfMD5AuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 8),
    _FsMIOspfIfMD5AuthKeyStopAccept_Type()
)
fsMIOspfIfMD5AuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyStopAccept.setStatus("current")


class _FsMIOspfIfMD5AuthKeyStatus_Type(Integer32):
    """Custom type fsMIOspfIfMD5AuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 3))
    )


_FsMIOspfIfMD5AuthKeyStatus_Type.__name__ = "Integer32"
_FsMIOspfIfMD5AuthKeyStatus_Object = MibTableColumn
fsMIOspfIfMD5AuthKeyStatus = _FsMIOspfIfMD5AuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 5, 1, 9),
    _FsMIOspfIfMD5AuthKeyStatus_Type()
)
fsMIOspfIfMD5AuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfMD5AuthKeyStatus.setStatus("current")
_FsMIOspfVirtIfMD5AuthTable_Object = MibTable
fsMIOspfVirtIfMD5AuthTable = _FsMIOspfVirtIfMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6)
)
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthTable.setStatus("current")
_FsMIOspfVirtIfMD5AuthEntry_Object = MibTableRow
fsMIOspfVirtIfMD5AuthEntry = _FsMIOspfVirtIfMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1)
)
fsMIOspfVirtIfMD5AuthEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfMD5AuthAreaId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfMD5AuthNeighbor"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfMD5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthEntry.setStatus("current")
_FsMIOspfVirtIfMD5AuthAreaId_Type = AreaID
_FsMIOspfVirtIfMD5AuthAreaId_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthAreaId = _FsMIOspfVirtIfMD5AuthAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 1),
    _FsMIOspfVirtIfMD5AuthAreaId_Type()
)
fsMIOspfVirtIfMD5AuthAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthAreaId.setStatus("current")
_FsMIOspfVirtIfMD5AuthNeighbor_Type = RouterID
_FsMIOspfVirtIfMD5AuthNeighbor_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthNeighbor = _FsMIOspfVirtIfMD5AuthNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 2),
    _FsMIOspfVirtIfMD5AuthNeighbor_Type()
)
fsMIOspfVirtIfMD5AuthNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthNeighbor.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyId_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfVirtIfMD5AuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyId_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyId = _FsMIOspfVirtIfMD5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 3),
    _FsMIOspfVirtIfMD5AuthKeyId_Type()
)
fsMIOspfVirtIfMD5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyId.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKey_Type(OctetString):
    """Custom type fsMIOspfVirtIfMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfVirtIfMD5AuthKey_Type.__name__ = "OctetString"
_FsMIOspfVirtIfMD5AuthKey_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKey = _FsMIOspfVirtIfMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 4),
    _FsMIOspfVirtIfMD5AuthKey_Type()
)
fsMIOspfVirtIfMD5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKey.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyStartAccept_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyStartAccept based on Integer32"""
    defaultValue = 0


_FsMIOspfVirtIfMD5AuthKeyStartAccept_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyStartAccept_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStartAccept = _FsMIOspfVirtIfMD5AuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 5),
    _FsMIOspfVirtIfMD5AuthKeyStartAccept_Type()
)
fsMIOspfVirtIfMD5AuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyStartAccept.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyStartGenerate based on Integer32"""
    defaultValue = 0


_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStartGenerate = _FsMIOspfVirtIfMD5AuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 6),
    _FsMIOspfVirtIfMD5AuthKeyStartGenerate_Type()
)
fsMIOspfVirtIfMD5AuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyStartGenerate.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyStopGenerate based on Integer32"""
    defaultValue = -1


_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStopGenerate = _FsMIOspfVirtIfMD5AuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 7),
    _FsMIOspfVirtIfMD5AuthKeyStopGenerate_Type()
)
fsMIOspfVirtIfMD5AuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyStopGenerate.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyStopAccept_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyStopAccept based on Integer32"""
    defaultValue = -1


_FsMIOspfVirtIfMD5AuthKeyStopAccept_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyStopAccept_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStopAccept = _FsMIOspfVirtIfMD5AuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 8),
    _FsMIOspfVirtIfMD5AuthKeyStopAccept_Type()
)
fsMIOspfVirtIfMD5AuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyStopAccept.setStatus("current")


class _FsMIOspfVirtIfMD5AuthKeyStatus_Type(Integer32):
    """Custom type fsMIOspfVirtIfMD5AuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 3))
    )


_FsMIOspfVirtIfMD5AuthKeyStatus_Type.__name__ = "Integer32"
_FsMIOspfVirtIfMD5AuthKeyStatus_Object = MibTableColumn
fsMIOspfVirtIfMD5AuthKeyStatus = _FsMIOspfVirtIfMD5AuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 6, 1, 9),
    _FsMIOspfVirtIfMD5AuthKeyStatus_Type()
)
fsMIOspfVirtIfMD5AuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfMD5AuthKeyStatus.setStatus("current")
_FsMIOspfNbrTable_Object = MibTable
fsMIOspfNbrTable = _FsMIOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7)
)
if mibBuilder.loadTexts:
    fsMIOspfNbrTable.setStatus("current")
_FsMIOspfNbrEntry_Object = MibTableRow
fsMIOspfNbrEntry = _FsMIOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1)
)
fsMIOspfNbrEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfNbrIpAddr"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    fsMIOspfNbrEntry.setStatus("current")
_FsMIOspfNbrIpAddr_Type = IpAddress
_FsMIOspfNbrIpAddr_Object = MibTableColumn
fsMIOspfNbrIpAddr = _FsMIOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 1),
    _FsMIOspfNbrIpAddr_Type()
)
fsMIOspfNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfNbrIpAddr.setStatus("current")


class _FsMIOspfNbrAddressLessIndex_Type(Integer32):
    """Custom type fsMIOspfNbrAddressLessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfNbrAddressLessIndex_Type.__name__ = "Integer32"
_FsMIOspfNbrAddressLessIndex_Object = MibTableColumn
fsMIOspfNbrAddressLessIndex = _FsMIOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 2),
    _FsMIOspfNbrAddressLessIndex_Type()
)
fsMIOspfNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfNbrAddressLessIndex.setStatus("current")
_FsMIOspfNbrDBSummaryQLen_Type = Gauge32
_FsMIOspfNbrDBSummaryQLen_Object = MibTableColumn
fsMIOspfNbrDBSummaryQLen = _FsMIOspfNbrDBSummaryQLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 3),
    _FsMIOspfNbrDBSummaryQLen_Type()
)
fsMIOspfNbrDBSummaryQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrDBSummaryQLen.setStatus("current")
_FsMIOspfNbrLSReqQLen_Type = Gauge32
_FsMIOspfNbrLSReqQLen_Object = MibTableColumn
fsMIOspfNbrLSReqQLen = _FsMIOspfNbrLSReqQLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 4),
    _FsMIOspfNbrLSReqQLen_Type()
)
fsMIOspfNbrLSReqQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrLSReqQLen.setStatus("current")


class _FsMIOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type fsMIOspfNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_FsMIOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_FsMIOspfNbrRestartHelperStatus_Object = MibTableColumn
fsMIOspfNbrRestartHelperStatus = _FsMIOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 5),
    _FsMIOspfNbrRestartHelperStatus_Type()
)
fsMIOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrRestartHelperStatus.setStatus("current")
_FsMIOspfNbrRestartHelperAge_Type = Unsigned32
_FsMIOspfNbrRestartHelperAge_Object = MibTableColumn
fsMIOspfNbrRestartHelperAge = _FsMIOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 6),
    _FsMIOspfNbrRestartHelperAge_Type()
)
fsMIOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMIOspfNbrRestartHelperAge.setUnits("seconds")


class _FsMIOspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type fsMIOspfNbrRestartHelperExitReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_FsMIOspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_FsMIOspfNbrRestartHelperExitReason_Object = MibTableColumn
fsMIOspfNbrRestartHelperExitReason = _FsMIOspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 7),
    _FsMIOspfNbrRestartHelperExitReason_Type()
)
fsMIOspfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrRestartHelperExitReason.setStatus("current")


class _FsMIOspfNbrBfdState_Type(Integer32):
    """Custom type fsMIOspfNbrBfdState based on Integer32"""
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


_FsMIOspfNbrBfdState_Type.__name__ = "Integer32"
_FsMIOspfNbrBfdState_Object = MibTableColumn
fsMIOspfNbrBfdState = _FsMIOspfNbrBfdState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 7, 1, 8),
    _FsMIOspfNbrBfdState_Type()
)
fsMIOspfNbrBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfNbrBfdState.setStatus("current")
_FsMIOspfRoutingTable_Object = MibTable
fsMIOspfRoutingTable = _FsMIOspfRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8)
)
if mibBuilder.loadTexts:
    fsMIOspfRoutingTable.setStatus("current")
_FsMIOspfRoutingEntry_Object = MibTableRow
fsMIOspfRoutingEntry = _FsMIOspfRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1)
)
fsMIOspfRoutingEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRouteIpAddr"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRouteIpAddrMask"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRouteIpTos"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRouteIpNextHop"),
)
if mibBuilder.loadTexts:
    fsMIOspfRoutingEntry.setStatus("current")
_FsMIOspfRouteIpAddr_Type = IpAddress
_FsMIOspfRouteIpAddr_Object = MibTableColumn
fsMIOspfRouteIpAddr = _FsMIOspfRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 1),
    _FsMIOspfRouteIpAddr_Type()
)
fsMIOspfRouteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRouteIpAddr.setStatus("current")
_FsMIOspfRouteIpAddrMask_Type = IpAddress
_FsMIOspfRouteIpAddrMask_Object = MibTableColumn
fsMIOspfRouteIpAddrMask = _FsMIOspfRouteIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 2),
    _FsMIOspfRouteIpAddrMask_Type()
)
fsMIOspfRouteIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRouteIpAddrMask.setStatus("current")
_FsMIOspfRouteIpTos_Type = TOSType
_FsMIOspfRouteIpTos_Object = MibTableColumn
fsMIOspfRouteIpTos = _FsMIOspfRouteIpTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 3),
    _FsMIOspfRouteIpTos_Type()
)
fsMIOspfRouteIpTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRouteIpTos.setStatus("current")
_FsMIOspfRouteIpNextHop_Type = IpAddress
_FsMIOspfRouteIpNextHop_Object = MibTableColumn
fsMIOspfRouteIpNextHop = _FsMIOspfRouteIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 4),
    _FsMIOspfRouteIpNextHop_Type()
)
fsMIOspfRouteIpNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRouteIpNextHop.setStatus("current")


class _FsMIOspfRouteType_Type(Integer32):
    """Custom type fsMIOspfRouteType based on Integer32"""
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


_FsMIOspfRouteType_Type.__name__ = "Integer32"
_FsMIOspfRouteType_Object = MibTableColumn
fsMIOspfRouteType = _FsMIOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 5),
    _FsMIOspfRouteType_Type()
)
fsMIOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRouteType.setStatus("current")
_FsMIOspfRouteAreaId_Type = IpAddress
_FsMIOspfRouteAreaId_Object = MibTableColumn
fsMIOspfRouteAreaId = _FsMIOspfRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 6),
    _FsMIOspfRouteAreaId_Type()
)
fsMIOspfRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRouteAreaId.setStatus("current")
_FsMIOspfRouteCost_Type = BigMetric
_FsMIOspfRouteCost_Object = MibTableColumn
fsMIOspfRouteCost = _FsMIOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 7),
    _FsMIOspfRouteCost_Type()
)
fsMIOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRouteCost.setStatus("current")
_FsMIOspfRouteType2Cost_Type = BigMetric
_FsMIOspfRouteType2Cost_Object = MibTableColumn
fsMIOspfRouteType2Cost = _FsMIOspfRouteType2Cost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 8),
    _FsMIOspfRouteType2Cost_Type()
)
fsMIOspfRouteType2Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRouteType2Cost.setStatus("current")


class _FsMIOspfRouteInterfaceIndex_Type(Integer32):
    """Custom type fsMIOspfRouteInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfRouteInterfaceIndex_Type.__name__ = "Integer32"
_FsMIOspfRouteInterfaceIndex_Object = MibTableColumn
fsMIOspfRouteInterfaceIndex = _FsMIOspfRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 8, 1, 9),
    _FsMIOspfRouteInterfaceIndex_Type()
)
fsMIOspfRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfRouteInterfaceIndex.setStatus("current")
_FsMIOspfSecIfTable_Object = MibTable
fsMIOspfSecIfTable = _FsMIOspfSecIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9)
)
if mibBuilder.loadTexts:
    fsMIOspfSecIfTable.setStatus("current")
_FsMIOspfSecIfEntry_Object = MibTableRow
fsMIOspfSecIfEntry = _FsMIOspfSecIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1)
)
fsMIOspfSecIfEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfPrimIpAddr"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfPrimAddresslessIf"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfSecIpAddr"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfSecIpAddrMask"),
)
if mibBuilder.loadTexts:
    fsMIOspfSecIfEntry.setStatus("current")
_FsMIOspfPrimIpAddr_Type = IpAddress
_FsMIOspfPrimIpAddr_Object = MibTableColumn
fsMIOspfPrimIpAddr = _FsMIOspfPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1, 1),
    _FsMIOspfPrimIpAddr_Type()
)
fsMIOspfPrimIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfPrimIpAddr.setStatus("current")


class _FsMIOspfPrimAddresslessIf_Type(Integer32):
    """Custom type fsMIOspfPrimAddresslessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfPrimAddresslessIf_Type.__name__ = "Integer32"
_FsMIOspfPrimAddresslessIf_Object = MibTableColumn
fsMIOspfPrimAddresslessIf = _FsMIOspfPrimAddresslessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1, 2),
    _FsMIOspfPrimAddresslessIf_Type()
)
fsMIOspfPrimAddresslessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfPrimAddresslessIf.setStatus("current")
_FsMIOspfSecIpAddr_Type = IpAddress
_FsMIOspfSecIpAddr_Object = MibTableColumn
fsMIOspfSecIpAddr = _FsMIOspfSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1, 3),
    _FsMIOspfSecIpAddr_Type()
)
fsMIOspfSecIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfSecIpAddr.setStatus("current")
_FsMIOspfSecIpAddrMask_Type = IpAddress
_FsMIOspfSecIpAddrMask_Object = MibTableColumn
fsMIOspfSecIpAddrMask = _FsMIOspfSecIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1, 4),
    _FsMIOspfSecIpAddrMask_Type()
)
fsMIOspfSecIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfSecIpAddrMask.setStatus("current")
_FsMIOspfSecIfStatus_Type = RowStatus
_FsMIOspfSecIfStatus_Object = MibTableColumn
fsMIOspfSecIfStatus = _FsMIOspfSecIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 9, 1, 5),
    _FsMIOspfSecIfStatus_Type()
)
fsMIOspfSecIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfSecIfStatus.setStatus("current")
_FsMIOspfAreaAggregateTable_Object = MibTable
fsMIOspfAreaAggregateTable = _FsMIOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10)
)
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateTable.setStatus("current")
_FsMIOspfAreaAggregateEntry_Object = MibTableRow
fsMIOspfAreaAggregateEntry = _FsMIOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1)
)
fsMIOspfAreaAggregateEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAreaAggregateAreaID"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAreaAggregateLsdbType"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAreaAggregateNet"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateEntry.setStatus("current")
_FsMIOspfAreaAggregateAreaID_Type = AreaID
_FsMIOspfAreaAggregateAreaID_Object = MibTableColumn
fsMIOspfAreaAggregateAreaID = _FsMIOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1, 1),
    _FsMIOspfAreaAggregateAreaID_Type()
)
fsMIOspfAreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateAreaID.setStatus("current")


class _FsMIOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type fsMIOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("summaryLink", 3),
          ("nssaExternalLink", 7))
    )


_FsMIOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_FsMIOspfAreaAggregateLsdbType_Object = MibTableColumn
fsMIOspfAreaAggregateLsdbType = _FsMIOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1, 2),
    _FsMIOspfAreaAggregateLsdbType_Type()
)
fsMIOspfAreaAggregateLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateLsdbType.setStatus("current")
_FsMIOspfAreaAggregateNet_Type = IpAddress
_FsMIOspfAreaAggregateNet_Object = MibTableColumn
fsMIOspfAreaAggregateNet = _FsMIOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1, 3),
    _FsMIOspfAreaAggregateNet_Type()
)
fsMIOspfAreaAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateNet.setStatus("current")
_FsMIOspfAreaAggregateMask_Type = IpAddress
_FsMIOspfAreaAggregateMask_Object = MibTableColumn
fsMIOspfAreaAggregateMask = _FsMIOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1, 4),
    _FsMIOspfAreaAggregateMask_Type()
)
fsMIOspfAreaAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateMask.setStatus("current")
_FsMIOspfAreaAggregateExternalTag_Type = Integer32
_FsMIOspfAreaAggregateExternalTag_Object = MibTableColumn
fsMIOspfAreaAggregateExternalTag = _FsMIOspfAreaAggregateExternalTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 10, 1, 5),
    _FsMIOspfAreaAggregateExternalTag_Type()
)
fsMIOspfAreaAggregateExternalTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAreaAggregateExternalTag.setStatus("current")
_FsMIOspfAsExternalAggregationTable_Object = MibTable
fsMIOspfAsExternalAggregationTable = _FsMIOspfAsExternalAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11)
)
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationTable.setStatus("current")
_FsMIOspfAsExternalAggregationEntry_Object = MibTableRow
fsMIOspfAsExternalAggregationEntry = _FsMIOspfAsExternalAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1)
)
fsMIOspfAsExternalAggregationEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAsExternalAggregationNet"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAsExternalAggregationMask"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAsExternalAggregationAreaId"),
)
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationEntry.setStatus("current")
_FsMIOspfAsExternalAggregationNet_Type = IpAddress
_FsMIOspfAsExternalAggregationNet_Object = MibTableColumn
fsMIOspfAsExternalAggregationNet = _FsMIOspfAsExternalAggregationNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 1),
    _FsMIOspfAsExternalAggregationNet_Type()
)
fsMIOspfAsExternalAggregationNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationNet.setStatus("current")
_FsMIOspfAsExternalAggregationMask_Type = IpAddress
_FsMIOspfAsExternalAggregationMask_Object = MibTableColumn
fsMIOspfAsExternalAggregationMask = _FsMIOspfAsExternalAggregationMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 2),
    _FsMIOspfAsExternalAggregationMask_Type()
)
fsMIOspfAsExternalAggregationMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationMask.setStatus("current")
_FsMIOspfAsExternalAggregationAreaId_Type = AreaID
_FsMIOspfAsExternalAggregationAreaId_Object = MibTableColumn
fsMIOspfAsExternalAggregationAreaId = _FsMIOspfAsExternalAggregationAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 3),
    _FsMIOspfAsExternalAggregationAreaId_Type()
)
fsMIOspfAsExternalAggregationAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationAreaId.setStatus("current")


class _FsMIOspfAsExternalAggregationEffect_Type(Integer32):
    """Custom type fsMIOspfAsExternalAggregationEffect based on Integer32"""
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


_FsMIOspfAsExternalAggregationEffect_Type.__name__ = "Integer32"
_FsMIOspfAsExternalAggregationEffect_Object = MibTableColumn
fsMIOspfAsExternalAggregationEffect = _FsMIOspfAsExternalAggregationEffect_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 4),
    _FsMIOspfAsExternalAggregationEffect_Type()
)
fsMIOspfAsExternalAggregationEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationEffect.setStatus("current")


class _FsMIOspfAsExternalAggregationTranslation_Type(Integer32):
    """Custom type fsMIOspfAsExternalAggregationTranslation based on Integer32"""
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


_FsMIOspfAsExternalAggregationTranslation_Type.__name__ = "Integer32"
_FsMIOspfAsExternalAggregationTranslation_Object = MibTableColumn
fsMIOspfAsExternalAggregationTranslation = _FsMIOspfAsExternalAggregationTranslation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 5),
    _FsMIOspfAsExternalAggregationTranslation_Type()
)
fsMIOspfAsExternalAggregationTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationTranslation.setStatus("current")
_FsMIOspfAsExternalAggregationStatus_Type = RowStatus
_FsMIOspfAsExternalAggregationStatus_Object = MibTableColumn
fsMIOspfAsExternalAggregationStatus = _FsMIOspfAsExternalAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 11, 1, 6),
    _FsMIOspfAsExternalAggregationStatus_Type()
)
fsMIOspfAsExternalAggregationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfAsExternalAggregationStatus.setStatus("current")
_FsMIOspfOpaqueLSAGroup_ObjectIdentity = ObjectIdentity
fsMIOspfOpaqueLSAGroup = _FsMIOspfOpaqueLSAGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12)
)
_FsMIOspfOpaqueLSAGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIOspfOpaqueLSAGeneralGroup = _FsMIOspfOpaqueLSAGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1)
)
_FsMIOspfOpaqueTable_Object = MibTable
fsMIOspfOpaqueTable = _FsMIOspfOpaqueTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfOpaqueTable.setStatus("current")
_FsMIOspfOpaqueEntry_Object = MibTableRow
fsMIOspfOpaqueEntry = _FsMIOspfOpaqueEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfOpaqueEntry.setStatus("current")


class _FsMIOspfOpaqueOption_Type(Integer32):
    """Custom type fsMIOspfOpaqueOption based on Integer32"""
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


_FsMIOspfOpaqueOption_Type.__name__ = "Integer32"
_FsMIOspfOpaqueOption_Object = MibTableColumn
fsMIOspfOpaqueOption = _FsMIOspfOpaqueOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1, 1, 1),
    _FsMIOspfOpaqueOption_Type()
)
fsMIOspfOpaqueOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfOpaqueOption.setStatus("current")
_FsMIOspfType11LsaCount_Type = Gauge32
_FsMIOspfType11LsaCount_Object = MibTableColumn
fsMIOspfType11LsaCount = _FsMIOspfType11LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1, 1, 2),
    _FsMIOspfType11LsaCount_Type()
)
fsMIOspfType11LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsaCount.setStatus("current")
_FsMIOspfType11LsaCksumSum_Type = Integer32
_FsMIOspfType11LsaCksumSum_Object = MibTableColumn
fsMIOspfType11LsaCksumSum = _FsMIOspfType11LsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1, 1, 3),
    _FsMIOspfType11LsaCksumSum_Type()
)
fsMIOspfType11LsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsaCksumSum.setStatus("current")


class _FsMIOspfAreaIDValid_Type(TruthValue):
    """Custom type fsMIOspfAreaIDValid based on TruthValue"""
    defaultValue = 2


_FsMIOspfAreaIDValid_Type.__name__ = "TruthValue"
_FsMIOspfAreaIDValid_Object = MibTableColumn
fsMIOspfAreaIDValid = _FsMIOspfAreaIDValid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 1, 1, 1, 4),
    _FsMIOspfAreaIDValid_Type()
)
fsMIOspfAreaIDValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfAreaIDValid.setStatus("current")
_FsMIOspfOpaqueInterfaceTable_Object = MibTable
fsMIOspfOpaqueInterfaceTable = _FsMIOspfOpaqueInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfOpaqueInterfaceTable.setStatus("current")
_FsMIOspfOpaqueInterfaceEntry_Object = MibTableRow
fsMIOspfOpaqueInterfaceEntry = _FsMIOspfOpaqueInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfOpaqueInterfaceEntry.setStatus("current")
_FsMIOspfOpaqueType9LsaCount_Type = Gauge32
_FsMIOspfOpaqueType9LsaCount_Object = MibTableColumn
fsMIOspfOpaqueType9LsaCount = _FsMIOspfOpaqueType9LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 2, 1, 1),
    _FsMIOspfOpaqueType9LsaCount_Type()
)
fsMIOspfOpaqueType9LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfOpaqueType9LsaCount.setStatus("current")


class _FsMIOspfOpaqueType9LsaCksumSum_Type(Integer32):
    """Custom type fsMIOspfOpaqueType9LsaCksumSum based on Integer32"""
    defaultValue = 0


_FsMIOspfOpaqueType9LsaCksumSum_Type.__name__ = "Integer32"
_FsMIOspfOpaqueType9LsaCksumSum_Object = MibTableColumn
fsMIOspfOpaqueType9LsaCksumSum = _FsMIOspfOpaqueType9LsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 2, 1, 2),
    _FsMIOspfOpaqueType9LsaCksumSum_Type()
)
fsMIOspfOpaqueType9LsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfOpaqueType9LsaCksumSum.setStatus("current")
_FsMIOspfType9LsdbTable_Object = MibTable
fsMIOspfType9LsdbTable = _FsMIOspfType9LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3)
)
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbTable.setStatus("current")
_FsMIOspfType9LsdbEntry_Object = MibTableRow
fsMIOspfType9LsdbEntry = _FsMIOspfType9LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1)
)
fsMIOspfType9LsdbEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType9LsdbIfIpAddress"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType9LsdbOpaqueType"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType9LsdbLsid"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType9LsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbEntry.setStatus("current")
_FsMIOspfType9LsdbIfIpAddress_Type = IpAddress
_FsMIOspfType9LsdbIfIpAddress_Object = MibTableColumn
fsMIOspfType9LsdbIfIpAddress = _FsMIOspfType9LsdbIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 1),
    _FsMIOspfType9LsdbIfIpAddress_Type()
)
fsMIOspfType9LsdbIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbIfIpAddress.setStatus("current")


class _FsMIOspfType9LsdbOpaqueType_Type(Integer32):
    """Custom type fsMIOspfType9LsdbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FsMIOspfType9LsdbOpaqueType_Type.__name__ = "Integer32"
_FsMIOspfType9LsdbOpaqueType_Object = MibTableColumn
fsMIOspfType9LsdbOpaqueType = _FsMIOspfType9LsdbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 2),
    _FsMIOspfType9LsdbOpaqueType_Type()
)
fsMIOspfType9LsdbOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbOpaqueType.setStatus("current")
_FsMIOspfType9LsdbLsid_Type = IpAddress
_FsMIOspfType9LsdbLsid_Object = MibTableColumn
fsMIOspfType9LsdbLsid = _FsMIOspfType9LsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 3),
    _FsMIOspfType9LsdbLsid_Type()
)
fsMIOspfType9LsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbLsid.setStatus("current")
_FsMIOspfType9LsdbRouterId_Type = RouterID
_FsMIOspfType9LsdbRouterId_Object = MibTableColumn
fsMIOspfType9LsdbRouterId = _FsMIOspfType9LsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 4),
    _FsMIOspfType9LsdbRouterId_Type()
)
fsMIOspfType9LsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbRouterId.setStatus("current")
_FsMIOspfType9LsdbSequence_Type = Integer32
_FsMIOspfType9LsdbSequence_Object = MibTableColumn
fsMIOspfType9LsdbSequence = _FsMIOspfType9LsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 5),
    _FsMIOspfType9LsdbSequence_Type()
)
fsMIOspfType9LsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbSequence.setStatus("current")
_FsMIOspfType9LsdbAge_Type = Integer32
_FsMIOspfType9LsdbAge_Object = MibTableColumn
fsMIOspfType9LsdbAge = _FsMIOspfType9LsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 6),
    _FsMIOspfType9LsdbAge_Type()
)
fsMIOspfType9LsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbAge.setStatus("current")
_FsMIOspfType9LsdbChecksum_Type = Integer32
_FsMIOspfType9LsdbChecksum_Object = MibTableColumn
fsMIOspfType9LsdbChecksum = _FsMIOspfType9LsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 7),
    _FsMIOspfType9LsdbChecksum_Type()
)
fsMIOspfType9LsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbChecksum.setStatus("current")


class _FsMIOspfType9LsdbAdvertisement_Type(OctetString):
    """Custom type fsMIOspfType9LsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FsMIOspfType9LsdbAdvertisement_Type.__name__ = "OctetString"
_FsMIOspfType9LsdbAdvertisement_Object = MibTableColumn
fsMIOspfType9LsdbAdvertisement = _FsMIOspfType9LsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 3, 1, 8),
    _FsMIOspfType9LsdbAdvertisement_Type()
)
fsMIOspfType9LsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType9LsdbAdvertisement.setStatus("current")
_FsMIOspfType11LsdbTable_Object = MibTable
fsMIOspfType11LsdbTable = _FsMIOspfType11LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4)
)
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbTable.setStatus("current")
_FsMIOspfType11LsdbEntry_Object = MibTableRow
fsMIOspfType11LsdbEntry = _FsMIOspfType11LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1)
)
fsMIOspfType11LsdbEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType11LsdbOpaqueType"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType11LsdbLsid"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfType11LsdbRouterId"),
)
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbEntry.setStatus("current")


class _FsMIOspfType11LsdbOpaqueType_Type(Integer32):
    """Custom type fsMIOspfType11LsdbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FsMIOspfType11LsdbOpaqueType_Type.__name__ = "Integer32"
_FsMIOspfType11LsdbOpaqueType_Object = MibTableColumn
fsMIOspfType11LsdbOpaqueType = _FsMIOspfType11LsdbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 1),
    _FsMIOspfType11LsdbOpaqueType_Type()
)
fsMIOspfType11LsdbOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbOpaqueType.setStatus("current")
_FsMIOspfType11LsdbLsid_Type = IpAddress
_FsMIOspfType11LsdbLsid_Object = MibTableColumn
fsMIOspfType11LsdbLsid = _FsMIOspfType11LsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 2),
    _FsMIOspfType11LsdbLsid_Type()
)
fsMIOspfType11LsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbLsid.setStatus("current")
_FsMIOspfType11LsdbRouterId_Type = RouterID
_FsMIOspfType11LsdbRouterId_Object = MibTableColumn
fsMIOspfType11LsdbRouterId = _FsMIOspfType11LsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 3),
    _FsMIOspfType11LsdbRouterId_Type()
)
fsMIOspfType11LsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbRouterId.setStatus("current")
_FsMIOspfType11LsdbSequence_Type = Integer32
_FsMIOspfType11LsdbSequence_Object = MibTableColumn
fsMIOspfType11LsdbSequence = _FsMIOspfType11LsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 4),
    _FsMIOspfType11LsdbSequence_Type()
)
fsMIOspfType11LsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbSequence.setStatus("current")
_FsMIOspfType11LsdbAge_Type = Integer32
_FsMIOspfType11LsdbAge_Object = MibTableColumn
fsMIOspfType11LsdbAge = _FsMIOspfType11LsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 5),
    _FsMIOspfType11LsdbAge_Type()
)
fsMIOspfType11LsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbAge.setStatus("current")
_FsMIOspfType11LsdbChecksum_Type = Integer32
_FsMIOspfType11LsdbChecksum_Object = MibTableColumn
fsMIOspfType11LsdbChecksum = _FsMIOspfType11LsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 6),
    _FsMIOspfType11LsdbChecksum_Type()
)
fsMIOspfType11LsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbChecksum.setStatus("current")


class _FsMIOspfType11LsdbAdvertisement_Type(OctetString):
    """Custom type fsMIOspfType11LsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FsMIOspfType11LsdbAdvertisement_Type.__name__ = "OctetString"
_FsMIOspfType11LsdbAdvertisement_Object = MibTableColumn
fsMIOspfType11LsdbAdvertisement = _FsMIOspfType11LsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 4, 1, 7),
    _FsMIOspfType11LsdbAdvertisement_Type()
)
fsMIOspfType11LsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfType11LsdbAdvertisement.setStatus("current")
_FsMIOspfAppInfoDbTable_Object = MibTable
fsMIOspfAppInfoDbTable = _FsMIOspfAppInfoDbTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5)
)
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbTable.setStatus("current")
_FsMIOspfAppInfoDbEntry_Object = MibTableRow
fsMIOspfAppInfoDbEntry = _FsMIOspfAppInfoDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1)
)
fsMIOspfAppInfoDbEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfAppInfoDbAppid"),
)
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbEntry.setStatus("current")


class _FsMIOspfAppInfoDbAppid_Type(Integer32):
    """Custom type fsMIOspfAppInfoDbAppid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIOspfAppInfoDbAppid_Type.__name__ = "Integer32"
_FsMIOspfAppInfoDbAppid_Object = MibTableColumn
fsMIOspfAppInfoDbAppid = _FsMIOspfAppInfoDbAppid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 1),
    _FsMIOspfAppInfoDbAppid_Type()
)
fsMIOspfAppInfoDbAppid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbAppid.setStatus("current")


class _FsMIOspfAppInfoDbOpaqueType_Type(Integer32):
    """Custom type fsMIOspfAppInfoDbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfAppInfoDbOpaqueType_Type.__name__ = "Integer32"
_FsMIOspfAppInfoDbOpaqueType_Object = MibTableColumn
fsMIOspfAppInfoDbOpaqueType = _FsMIOspfAppInfoDbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 2),
    _FsMIOspfAppInfoDbOpaqueType_Type()
)
fsMIOspfAppInfoDbOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbOpaqueType.setStatus("current")


class _FsMIOspfAppInfoDbLsaTypesSupported_Type(Integer32):
    """Custom type fsMIOspfAppInfoDbLsaTypesSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIOspfAppInfoDbLsaTypesSupported_Type.__name__ = "Integer32"
_FsMIOspfAppInfoDbLsaTypesSupported_Object = MibTableColumn
fsMIOspfAppInfoDbLsaTypesSupported = _FsMIOspfAppInfoDbLsaTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 3),
    _FsMIOspfAppInfoDbLsaTypesSupported_Type()
)
fsMIOspfAppInfoDbLsaTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbLsaTypesSupported.setStatus("current")
_FsMIOspfAppInfoDbType9Gen_Type = Counter32
_FsMIOspfAppInfoDbType9Gen_Object = MibTableColumn
fsMIOspfAppInfoDbType9Gen = _FsMIOspfAppInfoDbType9Gen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 4),
    _FsMIOspfAppInfoDbType9Gen_Type()
)
fsMIOspfAppInfoDbType9Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType9Gen.setStatus("current")
_FsMIOspfAppInfoDbType9Rcvd_Type = Counter32
_FsMIOspfAppInfoDbType9Rcvd_Object = MibTableColumn
fsMIOspfAppInfoDbType9Rcvd = _FsMIOspfAppInfoDbType9Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 5),
    _FsMIOspfAppInfoDbType9Rcvd_Type()
)
fsMIOspfAppInfoDbType9Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType9Rcvd.setStatus("current")
_FsMIOspfAppInfoDbType10Gen_Type = Counter32
_FsMIOspfAppInfoDbType10Gen_Object = MibTableColumn
fsMIOspfAppInfoDbType10Gen = _FsMIOspfAppInfoDbType10Gen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 6),
    _FsMIOspfAppInfoDbType10Gen_Type()
)
fsMIOspfAppInfoDbType10Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType10Gen.setStatus("current")
_FsMIOspfAppInfoDbType10Rcvd_Type = Counter32
_FsMIOspfAppInfoDbType10Rcvd_Object = MibTableColumn
fsMIOspfAppInfoDbType10Rcvd = _FsMIOspfAppInfoDbType10Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 7),
    _FsMIOspfAppInfoDbType10Rcvd_Type()
)
fsMIOspfAppInfoDbType10Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType10Rcvd.setStatus("current")
_FsMIOspfAppInfoDbType11Gen_Type = Counter32
_FsMIOspfAppInfoDbType11Gen_Object = MibTableColumn
fsMIOspfAppInfoDbType11Gen = _FsMIOspfAppInfoDbType11Gen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 8),
    _FsMIOspfAppInfoDbType11Gen_Type()
)
fsMIOspfAppInfoDbType11Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType11Gen.setStatus("current")
_FsMIOspfAppInfoDbType11Rcvd_Type = Counter32
_FsMIOspfAppInfoDbType11Rcvd_Object = MibTableColumn
fsMIOspfAppInfoDbType11Rcvd = _FsMIOspfAppInfoDbType11Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 12, 5, 1, 9),
    _FsMIOspfAppInfoDbType11Rcvd_Type()
)
fsMIOspfAppInfoDbType11Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfAppInfoDbType11Rcvd.setStatus("current")
_FsMIOspfRRDGroup_ObjectIdentity = ObjectIdentity
fsMIOspfRRDGroup = _FsMIOspfRRDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13)
)
_FsMIOspfRRDGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIOspfRRDGeneralGroup = _FsMIOspfRRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1)
)
_FsMIOspfRRDRouteTable_Object = MibTable
fsMIOspfRRDRouteTable = _FsMIOspfRRDRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteTable.setStatus("current")
_FsMIOspfRRDRouteEntry_Object = MibTableRow
fsMIOspfRRDRouteEntry = _FsMIOspfRRDRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteEntry.setStatus("current")


class _FsMIOspfRRDStatus_Type(Status):
    """Custom type fsMIOspfRRDStatus based on Status"""
    defaultValue = 2


_FsMIOspfRRDStatus_Type.__name__ = "Status"
_FsMIOspfRRDStatus_Object = MibTableColumn
fsMIOspfRRDStatus = _FsMIOspfRRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1, 1, 1),
    _FsMIOspfRRDStatus_Type()
)
fsMIOspfRRDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDStatus.setStatus("current")


class _FsMIOspfRRDSrcProtoMaskEnable_Type(Integer32):
    """Custom type fsMIOspfRRDSrcProtoMaskEnable based on Integer32"""
    defaultValue = 0


_FsMIOspfRRDSrcProtoMaskEnable_Type.__name__ = "Integer32"
_FsMIOspfRRDSrcProtoMaskEnable_Object = MibTableColumn
fsMIOspfRRDSrcProtoMaskEnable = _FsMIOspfRRDSrcProtoMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1, 1, 2),
    _FsMIOspfRRDSrcProtoMaskEnable_Type()
)
fsMIOspfRRDSrcProtoMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDSrcProtoMaskEnable.setStatus("current")


class _FsMIOspfRRDSrcProtoMaskDisable_Type(Integer32):
    """Custom type fsMIOspfRRDSrcProtoMaskDisable based on Integer32"""
    defaultValue = 8326


_FsMIOspfRRDSrcProtoMaskDisable_Type.__name__ = "Integer32"
_FsMIOspfRRDSrcProtoMaskDisable_Object = MibTableColumn
fsMIOspfRRDSrcProtoMaskDisable = _FsMIOspfRRDSrcProtoMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1, 1, 3),
    _FsMIOspfRRDSrcProtoMaskDisable_Type()
)
fsMIOspfRRDSrcProtoMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDSrcProtoMaskDisable.setStatus("current")


class _FsMIOspfRRDRouteMapEnable_Type(DisplayString):
    """Custom type fsMIOspfRRDRouteMapEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsMIOspfRRDRouteMapEnable_Type.__name__ = "DisplayString"
_FsMIOspfRRDRouteMapEnable_Object = MibTableColumn
fsMIOspfRRDRouteMapEnable = _FsMIOspfRRDRouteMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 1, 1, 1, 4),
    _FsMIOspfRRDRouteMapEnable_Type()
)
fsMIOspfRRDRouteMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteMapEnable.setStatus("current")
_FsMIOspfRRDRouteConfigTable_Object = MibTable
fsMIOspfRRDRouteConfigTable = _FsMIOspfRRDRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2)
)
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteConfigTable.setStatus("current")
_FsMIOspfRRDRouteConfigEntry_Object = MibTableRow
fsMIOspfRRDRouteConfigEntry = _FsMIOspfRRDRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1)
)
fsMIOspfRRDRouteConfigEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRRDRouteDest"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRRDRouteMask"),
)
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteConfigEntry.setStatus("current")
_FsMIOspfRRDRouteDest_Type = IpAddress
_FsMIOspfRRDRouteDest_Object = MibTableColumn
fsMIOspfRRDRouteDest = _FsMIOspfRRDRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 1),
    _FsMIOspfRRDRouteDest_Type()
)
fsMIOspfRRDRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteDest.setStatus("current")
_FsMIOspfRRDRouteMask_Type = IpAddress
_FsMIOspfRRDRouteMask_Object = MibTableColumn
fsMIOspfRRDRouteMask = _FsMIOspfRRDRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 2),
    _FsMIOspfRRDRouteMask_Type()
)
fsMIOspfRRDRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteMask.setStatus("current")


class _FsMIOspfRRDRouteMetric_Type(BigMetric):
    """Custom type fsMIOspfRRDRouteMetric based on BigMetric"""
    defaultValue = 10


_FsMIOspfRRDRouteMetric_Type.__name__ = "BigMetric"
_FsMIOspfRRDRouteMetric_Object = MibTableColumn
fsMIOspfRRDRouteMetric = _FsMIOspfRRDRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 3),
    _FsMIOspfRRDRouteMetric_Type()
)
fsMIOspfRRDRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteMetric.setStatus("current")


class _FsMIOspfRRDRouteMetricType_Type(Integer32):
    """Custom type fsMIOspfRRDRouteMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asexttype1", 1),
          ("asexttype2", 2))
    )


_FsMIOspfRRDRouteMetricType_Type.__name__ = "Integer32"
_FsMIOspfRRDRouteMetricType_Object = MibTableColumn
fsMIOspfRRDRouteMetricType = _FsMIOspfRRDRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 4),
    _FsMIOspfRRDRouteMetricType_Type()
)
fsMIOspfRRDRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteMetricType.setStatus("current")


class _FsMIOspfRRDRouteTagType_Type(Integer32):
    """Custom type fsMIOspfRRDRouteTagType based on Integer32"""
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


_FsMIOspfRRDRouteTagType_Type.__name__ = "Integer32"
_FsMIOspfRRDRouteTagType_Object = MibTableColumn
fsMIOspfRRDRouteTagType = _FsMIOspfRRDRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 5),
    _FsMIOspfRRDRouteTagType_Type()
)
fsMIOspfRRDRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteTagType.setStatus("current")


class _FsMIOspfRRDRouteTag_Type(Unsigned32):
    """Custom type fsMIOspfRRDRouteTag based on Unsigned32"""
    defaultValue = 0


_FsMIOspfRRDRouteTag_Type.__name__ = "Unsigned32"
_FsMIOspfRRDRouteTag_Object = MibTableColumn
fsMIOspfRRDRouteTag = _FsMIOspfRRDRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 6),
    _FsMIOspfRRDRouteTag_Type()
)
fsMIOspfRRDRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteTag.setStatus("current")
_FsMIOspfRRDRouteStatus_Type = RowStatus
_FsMIOspfRRDRouteStatus_Object = MibTableColumn
fsMIOspfRRDRouteStatus = _FsMIOspfRRDRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 2, 1, 7),
    _FsMIOspfRRDRouteStatus_Type()
)
fsMIOspfRRDRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIOspfRRDRouteStatus.setStatus("current")
_FsMIOspfRRDMetricTable_Object = MibTable
fsMIOspfRRDMetricTable = _FsMIOspfRRDMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 3)
)
if mibBuilder.loadTexts:
    fsMIOspfRRDMetricTable.setStatus("current")
_FsMIOspfRRDMerticEntry_Object = MibTableRow
fsMIOspfRRDMerticEntry = _FsMIOspfRRDMerticEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 3, 1)
)
fsMIOspfRRDMerticEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfRRDProtocolId"),
)
if mibBuilder.loadTexts:
    fsMIOspfRRDMerticEntry.setStatus("current")


class _FsMIOspfRRDProtocolId_Type(Integer32):
    """Custom type fsMIOspfRRDProtocolId based on Integer32"""
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
        *(("bgp", 1),
          ("rip", 2),
          ("connected", 3),
          ("static", 4))
    )


_FsMIOspfRRDProtocolId_Type.__name__ = "Integer32"
_FsMIOspfRRDProtocolId_Object = MibTableColumn
fsMIOspfRRDProtocolId = _FsMIOspfRRDProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 3, 1, 1),
    _FsMIOspfRRDProtocolId_Type()
)
fsMIOspfRRDProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfRRDProtocolId.setStatus("current")
_FsMIOspfRRDMetricValue_Type = Integer32
_FsMIOspfRRDMetricValue_Object = MibTableColumn
fsMIOspfRRDMetricValue = _FsMIOspfRRDMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 3, 1, 2),
    _FsMIOspfRRDMetricValue_Type()
)
fsMIOspfRRDMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDMetricValue.setStatus("current")


class _FsMIOspfRRDMetricType_Type(Integer32):
    """Custom type fsMIOspfRRDMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1External", 1),
          ("type2External", 2))
    )


_FsMIOspfRRDMetricType_Type.__name__ = "Integer32"
_FsMIOspfRRDMetricType_Object = MibTableColumn
fsMIOspfRRDMetricType = _FsMIOspfRRDMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 13, 3, 1, 3),
    _FsMIOspfRRDMetricType_Type()
)
fsMIOspfRRDMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfRRDMetricType.setStatus("current")
_FsMIOspfVirtNbrTable_Object = MibTable
fsMIOspfVirtNbrTable = _FsMIOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 14)
)
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrTable.setStatus("current")
_FsMIOspfVirtNbrEntry_Object = MibTableRow
fsMIOspfVirtNbrEntry = _FsMIOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 14, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrEntry.setStatus("current")


class _FsMIOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type fsMIOspfVirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_FsMIOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_FsMIOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
fsMIOspfVirtNbrRestartHelperStatus = _FsMIOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 14, 1, 1),
    _FsMIOspfVirtNbrRestartHelperStatus_Type()
)
fsMIOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrRestartHelperStatus.setStatus("current")
_FsMIOspfVirtNbrRestartHelperAge_Type = Unsigned32
_FsMIOspfVirtNbrRestartHelperAge_Object = MibTableColumn
fsMIOspfVirtNbrRestartHelperAge = _FsMIOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 14, 1, 2),
    _FsMIOspfVirtNbrRestartHelperAge_Type()
)
fsMIOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _FsMIOspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type fsMIOspfVirtNbrRestartHelperExitReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_FsMIOspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_FsMIOspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
fsMIOspfVirtNbrRestartHelperExitReason = _FsMIOspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 14, 1, 3),
    _FsMIOspfVirtNbrRestartHelperExitReason_Type()
)
fsMIOspfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrRestartHelperExitReason.setStatus("current")
_FsMIospfDistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsMIospfDistInOutRouteMap = _FsMIospfDistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15)
)
_FsMIOspfDistInOutRouteMapTable_Object = MibTable
fsMIOspfDistInOutRouteMapTable = _FsMIOspfDistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapTable.setStatus("current")
_FsMIOspfDistInOutRouteMapEntry_Object = MibTableRow
fsMIOspfDistInOutRouteMapEntry = _FsMIOspfDistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1, 1)
)
fsMIOspfDistInOutRouteMapEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfDistInOutRouteMapName"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfDistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapEntry.setStatus("current")


class _FsMIOspfDistInOutRouteMapName_Type(DisplayString):
    """Custom type fsMIOspfDistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIOspfDistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsMIOspfDistInOutRouteMapName_Object = MibTableColumn
fsMIOspfDistInOutRouteMapName = _FsMIOspfDistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1, 1, 1),
    _FsMIOspfDistInOutRouteMapName_Type()
)
fsMIOspfDistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapName.setStatus("current")


class _FsMIOspfDistInOutRouteMapType_Type(Integer32):
    """Custom type fsMIOspfDistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsMIOspfDistInOutRouteMapType_Type.__name__ = "Integer32"
_FsMIOspfDistInOutRouteMapType_Object = MibTableColumn
fsMIOspfDistInOutRouteMapType = _FsMIOspfDistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1, 1, 3),
    _FsMIOspfDistInOutRouteMapType_Type()
)
fsMIOspfDistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapType.setStatus("current")


class _FsMIOspfDistInOutRouteMapValue_Type(Integer32):
    """Custom type fsMIOspfDistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIOspfDistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsMIOspfDistInOutRouteMapValue_Object = MibTableColumn
fsMIOspfDistInOutRouteMapValue = _FsMIOspfDistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1, 1, 4),
    _FsMIOspfDistInOutRouteMapValue_Type()
)
fsMIOspfDistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapValue.setStatus("current")
_FsMIOspfDistInOutRouteMapRowStatus_Type = RowStatus
_FsMIOspfDistInOutRouteMapRowStatus_Object = MibTableColumn
fsMIOspfDistInOutRouteMapRowStatus = _FsMIOspfDistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 15, 1, 1, 5),
    _FsMIOspfDistInOutRouteMapRowStatus_Type()
)
fsMIOspfDistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfDistInOutRouteMapRowStatus.setStatus("current")
_FsMIospfPreferenceGroup_ObjectIdentity = ObjectIdentity
fsMIospfPreferenceGroup = _FsMIospfPreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 16)
)
_FsMIOspfPreferenceTable_Object = MibTable
fsMIOspfPreferenceTable = _FsMIOspfPreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 16, 1)
)
if mibBuilder.loadTexts:
    fsMIOspfPreferenceTable.setStatus("current")
_FsMIOspfPreferenceEntry_Object = MibTableRow
fsMIOspfPreferenceEntry = _FsMIOspfPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 16, 1, 1)
)
fsMIOspfPreferenceEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
)
if mibBuilder.loadTexts:
    fsMIOspfPreferenceEntry.setStatus("current")


class _FsMIOspfPreferenceValue_Type(Integer32):
    """Custom type fsMIOspfPreferenceValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfPreferenceValue_Type.__name__ = "Integer32"
_FsMIOspfPreferenceValue_Object = MibTableColumn
fsMIOspfPreferenceValue = _FsMIOspfPreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 16, 1, 1, 1),
    _FsMIOspfPreferenceValue_Type()
)
fsMIOspfPreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfPreferenceValue.setStatus("current")
_FsMIOspfIfAuthTable_Object = MibTable
fsMIOspfIfAuthTable = _FsMIOspfIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17)
)
if mibBuilder.loadTexts:
    fsMIOspfIfAuthTable.setStatus("current")
_FsMIOspfIfAuthEntry_Object = MibTableRow
fsMIOspfIfAuthEntry = _FsMIOspfIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1)
)
fsMIOspfIfAuthEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfAuthIpAddress"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfAuthAddressLessIf"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfIfAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfIfAuthEntry.setStatus("current")
_FsMIOspfIfAuthIpAddress_Type = IpAddress
_FsMIOspfIfAuthIpAddress_Object = MibTableColumn
fsMIOspfIfAuthIpAddress = _FsMIOspfIfAuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 1),
    _FsMIOspfIfAuthIpAddress_Type()
)
fsMIOspfIfAuthIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthIpAddress.setStatus("current")


class _FsMIOspfIfAuthAddressLessIf_Type(Integer32):
    """Custom type fsMIOspfIfAuthAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIOspfIfAuthAddressLessIf_Type.__name__ = "Integer32"
_FsMIOspfIfAuthAddressLessIf_Object = MibTableColumn
fsMIOspfIfAuthAddressLessIf = _FsMIOspfIfAuthAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 2),
    _FsMIOspfIfAuthAddressLessIf_Type()
)
fsMIOspfIfAuthAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthAddressLessIf.setStatus("current")


class _FsMIOspfIfAuthKeyId_Type(Integer32):
    """Custom type fsMIOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfIfAuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfIfAuthKeyId_Object = MibTableColumn
fsMIOspfIfAuthKeyId = _FsMIOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 3),
    _FsMIOspfIfAuthKeyId_Type()
)
fsMIOspfIfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyId.setStatus("current")


class _FsMIOspfIfAuthKey_Type(OctetString):
    """Custom type fsMIOspfIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfIfAuthKey_Type.__name__ = "OctetString"
_FsMIOspfIfAuthKey_Object = MibTableColumn
fsMIOspfIfAuthKey = _FsMIOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 4),
    _FsMIOspfIfAuthKey_Type()
)
fsMIOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKey.setStatus("current")
_FsMIOspfIfAuthKeyStartAccept_Type = DateAndTime
_FsMIOspfIfAuthKeyStartAccept_Object = MibTableColumn
fsMIOspfIfAuthKeyStartAccept = _FsMIOspfIfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 5),
    _FsMIOspfIfAuthKeyStartAccept_Type()
)
fsMIOspfIfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyStartAccept.setStatus("current")
_FsMIOspfIfAuthKeyStartGenerate_Type = DateAndTime
_FsMIOspfIfAuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfIfAuthKeyStartGenerate = _FsMIOspfIfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 6),
    _FsMIOspfIfAuthKeyStartGenerate_Type()
)
fsMIOspfIfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyStartGenerate.setStatus("current")
_FsMIOspfIfAuthKeyStopGenerate_Type = DateAndTime
_FsMIOspfIfAuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfIfAuthKeyStopGenerate = _FsMIOspfIfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 7),
    _FsMIOspfIfAuthKeyStopGenerate_Type()
)
fsMIOspfIfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyStopGenerate.setStatus("current")
_FsMIOspfIfAuthKeyStopAccept_Type = DateAndTime
_FsMIOspfIfAuthKeyStopAccept_Object = MibTableColumn
fsMIOspfIfAuthKeyStopAccept = _FsMIOspfIfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 8),
    _FsMIOspfIfAuthKeyStopAccept_Type()
)
fsMIOspfIfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyStopAccept.setStatus("current")


class _FsMIOspfIfAuthKeyStatus_Type(Integer32):
    """Custom type fsMIOspfIfAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 3))
    )


_FsMIOspfIfAuthKeyStatus_Type.__name__ = "Integer32"
_FsMIOspfIfAuthKeyStatus_Object = MibTableColumn
fsMIOspfIfAuthKeyStatus = _FsMIOspfIfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 17, 1, 9),
    _FsMIOspfIfAuthKeyStatus_Type()
)
fsMIOspfIfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfIfAuthKeyStatus.setStatus("current")
_FsMIOspfVirtIfAuthTable_Object = MibTable
fsMIOspfVirtIfAuthTable = _FsMIOspfVirtIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18)
)
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthTable.setStatus("current")
_FsMIOspfVirtIfAuthEntry_Object = MibTableRow
fsMIOspfVirtIfAuthEntry = _FsMIOspfVirtIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1)
)
fsMIOspfVirtIfAuthEntry.setIndexNames(
    (0, "SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfContextId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfAuthAreaId"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfAuthNeighbor"),
    (0, "SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtIfAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthEntry.setStatus("current")
_FsMIOspfVirtIfAuthAreaId_Type = AreaID
_FsMIOspfVirtIfAuthAreaId_Object = MibTableColumn
fsMIOspfVirtIfAuthAreaId = _FsMIOspfVirtIfAuthAreaId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 1),
    _FsMIOspfVirtIfAuthAreaId_Type()
)
fsMIOspfVirtIfAuthAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthAreaId.setStatus("current")
_FsMIOspfVirtIfAuthNeighbor_Type = RouterID
_FsMIOspfVirtIfAuthNeighbor_Object = MibTableColumn
fsMIOspfVirtIfAuthNeighbor = _FsMIOspfVirtIfAuthNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 2),
    _FsMIOspfVirtIfAuthNeighbor_Type()
)
fsMIOspfVirtIfAuthNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthNeighbor.setStatus("current")


class _FsMIOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type fsMIOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_FsMIOspfVirtIfAuthKeyId_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyId = _FsMIOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 3),
    _FsMIOspfVirtIfAuthKeyId_Type()
)
fsMIOspfVirtIfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyId.setStatus("current")


class _FsMIOspfVirtIfAuthKey_Type(OctetString):
    """Custom type fsMIOspfVirtIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_FsMIOspfVirtIfAuthKey_Object = MibTableColumn
fsMIOspfVirtIfAuthKey = _FsMIOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 4),
    _FsMIOspfVirtIfAuthKey_Type()
)
fsMIOspfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKey.setStatus("current")
_FsMIOspfVirtIfAuthKeyStartAccept_Type = DateAndTime
_FsMIOspfVirtIfAuthKeyStartAccept_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyStartAccept = _FsMIOspfVirtIfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 5),
    _FsMIOspfVirtIfAuthKeyStartAccept_Type()
)
fsMIOspfVirtIfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyStartAccept.setStatus("current")
_FsMIOspfVirtIfAuthKeyStartGenerate_Type = DateAndTime
_FsMIOspfVirtIfAuthKeyStartGenerate_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyStartGenerate = _FsMIOspfVirtIfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 6),
    _FsMIOspfVirtIfAuthKeyStartGenerate_Type()
)
fsMIOspfVirtIfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyStartGenerate.setStatus("current")
_FsMIOspfVirtIfAuthKeyStopGenerate_Type = DateAndTime
_FsMIOspfVirtIfAuthKeyStopGenerate_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyStopGenerate = _FsMIOspfVirtIfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 7),
    _FsMIOspfVirtIfAuthKeyStopGenerate_Type()
)
fsMIOspfVirtIfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyStopGenerate.setStatus("current")
_FsMIOspfVirtIfAuthKeyStopAccept_Type = DateAndTime
_FsMIOspfVirtIfAuthKeyStopAccept_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyStopAccept = _FsMIOspfVirtIfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 8),
    _FsMIOspfVirtIfAuthKeyStopAccept_Type()
)
fsMIOspfVirtIfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyStopAccept.setStatus("current")


class _FsMIOspfVirtIfAuthKeyStatus_Type(Integer32):
    """Custom type fsMIOspfVirtIfAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 3))
    )


_FsMIOspfVirtIfAuthKeyStatus_Type.__name__ = "Integer32"
_FsMIOspfVirtIfAuthKeyStatus_Object = MibTableColumn
fsMIOspfVirtIfAuthKeyStatus = _FsMIOspfVirtIfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 18, 1, 9),
    _FsMIOspfVirtIfAuthKeyStatus_Type()
)
fsMIOspfVirtIfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIOspfVirtIfAuthKeyStatus.setStatus("current")
_FsMIOspfTestGroup_ObjectIdentity = ObjectIdentity
fsMIOspfTestGroup = _FsMIOspfTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 100)
)
_FsMIOspfNotification_ObjectIdentity = ObjectIdentity
fsMIOspfNotification = _FsMIOspfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101)
)
_FsMIOspfTraps_ObjectIdentity = ObjectIdentity
fsMIOspfTraps = _FsMIOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101, 0)
)
fsMIStdOspfEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-MIB",
     "fsMIOspfEntry")
)
fsMIOspfEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIStdOspfEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-MIB",
     "fsMIOspfOpaqueEntry")
)
fsMIOspfOpaqueEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIOspfIfEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-MIB",
     "fsMIOspfOpaqueInterfaceEntry")
)
fsMIOspfOpaqueInterfaceEntry.setIndexNames(*fsMIOspfIfEntry.getIndexNames())
fsMIStdOspfEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-MIB",
     "fsMIOspfRRDRouteEntry")
)
fsMIOspfRRDRouteEntry.setIndexNames(*fsMIStdOspfEntry.getIndexNames())
fsMIStdOspfVirtNbrEntry.registerAugmentions(
    ("SUPERMICRO-OSPFMI-MIB",
     "fsMIOspfVirtNbrEntry")
)
fsMIOspfVirtNbrEntry.setIndexNames(*fsMIStdOspfVirtNbrEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsMIOspfRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101, 0, 1)
)
fsMIOspfRestartStatusChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfRestartStatus"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfRestartInterval"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfRestartExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfRestartStatusChange.setStatus(
        "current"
    )

fsMIOspfNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101, 0, 2)
)
fsMIOspfNbrRestartHelperStatusChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfNbrRtrId"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfNbrRestartHelperStatus"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfNbrRestartHelperAge"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfNbrRestartHelperStatusChange.setStatus(
        "current"
    )

fsMIOspfVirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101, 0, 3)
)
fsMIOspfVirtNbrRestartHelperStatusChange.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtNbrRestartHelperStatus"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtNbrRestartHelperAge"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfVirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    fsMIOspfVirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )

fsMIOspfHotStandbyEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 145, 101, 0, 4)
)
fsMIOspfHotStandbyEventTrap.setObjects(
      *(("SUPERMICRO-MISTDOSPF-MIB", "fsMIStdOspfRouterId"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfHotStandbyState"),
        ("SUPERMICRO-OSPFMI-MIB", "fsMIOspfDynamicBulkUpdStatus"))
)
if mibBuilder.loadTexts:
    fsMIOspfHotStandbyEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-OSPFMI-MIB",
    **{"fsMIOspf": fsMIOspf,
       "fsMIOspfGeneralGroup": fsMIOspfGeneralGroup,
       "fsMIOspfGlobalTraceLevel": fsMIOspfGlobalTraceLevel,
       "fsMIOspfVrfSpfInterval": fsMIOspfVrfSpfInterval,
       "fsMIOspfTable": fsMIOspfTable,
       "fsMIOspfEntry": fsMIOspfEntry,
       "fsMIOspfOverFlowState": fsMIOspfOverFlowState,
       "fsMIOspfPktsRcvd": fsMIOspfPktsRcvd,
       "fsMIOspfPktsTxed": fsMIOspfPktsTxed,
       "fsMIOspfPktsDisd": fsMIOspfPktsDisd,
       "fsMIOspfRFC1583Compatibility": fsMIOspfRFC1583Compatibility,
       "fsMIOspfTraceLevel": fsMIOspfTraceLevel,
       "fsMIOspfMinLsaInterval": fsMIOspfMinLsaInterval,
       "fsMIOspfABRType": fsMIOspfABRType,
       "fsMIOspfNssaAsbrDefRtTrans": fsMIOspfNssaAsbrDefRtTrans,
       "fsMIOspfDefaultPassiveInterface": fsMIOspfDefaultPassiveInterface,
       "fsMIOspfSpfHoldtime": fsMIOspfSpfHoldtime,
       "fsMIOspfSpfDelay": fsMIOspfSpfDelay,
       "fsMIOspfRestartSupport": fsMIOspfRestartSupport,
       "fsMIOspfRestartInterval": fsMIOspfRestartInterval,
       "fsMIOspfRestartStrictLsaChecking": fsMIOspfRestartStrictLsaChecking,
       "fsMIOspfRestartStatus": fsMIOspfRestartStatus,
       "fsMIOspfRestartAge": fsMIOspfRestartAge,
       "fsMIOspfRestartExitReason": fsMIOspfRestartExitReason,
       "fsMIOspfHelperSupport": fsMIOspfHelperSupport,
       "fsMIOspfExtTraceLevel": fsMIOspfExtTraceLevel,
       "fsMIOspfHelperGraceTimeLimit": fsMIOspfHelperGraceTimeLimit,
       "fsMIOspfRestartAckState": fsMIOspfRestartAckState,
       "fsMIOspfGraceLsaRetransmitCount": fsMIOspfGraceLsaRetransmitCount,
       "fsMIOspfRestartReason": fsMIOspfRestartReason,
       "fsMIOspfRTStaggeringInterval": fsMIOspfRTStaggeringInterval,
       "fsMIOspfRouterIdPermanence": fsMIOspfRouterIdPermanence,
       "fsMIOspfBfdStatus": fsMIOspfBfdStatus,
       "fsMIOspfBfdAllIfState": fsMIOspfBfdAllIfState,
       "fsMIOspfRTStaggeringStatus": fsMIOspfRTStaggeringStatus,
       "fsMIOspfHotStandbyAdminStatus": fsMIOspfHotStandbyAdminStatus,
       "fsMIOspfHotStandbyState": fsMIOspfHotStandbyState,
       "fsMIOspfDynamicBulkUpdStatus": fsMIOspfDynamicBulkUpdStatus,
       "fsMIOspfStanbyHelloSyncCount": fsMIOspfStanbyHelloSyncCount,
       "fsMIOspfStanbyLsaSyncCount": fsMIOspfStanbyLsaSyncCount,
       "fsMIOspfGlobalExtTraceLevel": fsMIOspfGlobalExtTraceLevel,
       "fsMIOspfAreaTable": fsMIOspfAreaTable,
       "fsMIOspfAreaEntry": fsMIOspfAreaEntry,
       "fsMIOspfAreaId": fsMIOspfAreaId,
       "fsMIOspfAreaIfCount": fsMIOspfAreaIfCount,
       "fsMIOspfAreaNetCount": fsMIOspfAreaNetCount,
       "fsMIOspfAreaRtrCount": fsMIOspfAreaRtrCount,
       "fsMIOspfAreaNSSATranslatorRole": fsMIOspfAreaNSSATranslatorRole,
       "fsMIOspfAreaNSSATranslatorState": fsMIOspfAreaNSSATranslatorState,
       "fsMIOspfAreaNSSATranslatorStabilityInterval": fsMIOspfAreaNSSATranslatorStabilityInterval,
       "fsMIOspfAreaNSSATranslatorEvents": fsMIOspfAreaNSSATranslatorEvents,
       "fsMIOspfAreaDfInfOriginate": fsMIOspfAreaDfInfOriginate,
       "fsMIOspfHostTable": fsMIOspfHostTable,
       "fsMIOspfHostEntry": fsMIOspfHostEntry,
       "fsMIOspfHostIpAddress": fsMIOspfHostIpAddress,
       "fsMIOspfHostTOS": fsMIOspfHostTOS,
       "fsMIOspfHostRouteIfIndex": fsMIOspfHostRouteIfIndex,
       "fsMIOspfIfTable": fsMIOspfIfTable,
       "fsMIOspfIfEntry": fsMIOspfIfEntry,
       "fsMIOspfIfIpAddress": fsMIOspfIfIpAddress,
       "fsMIOspfAddressLessIf": fsMIOspfAddressLessIf,
       "fsMIOspfIfOperState": fsMIOspfIfOperState,
       "fsMIOspfIfPassive": fsMIOspfIfPassive,
       "fsMIOspfIfNbrCount": fsMIOspfIfNbrCount,
       "fsMIOspfIfAdjCount": fsMIOspfIfAdjCount,
       "fsMIOspfIfHelloRcvd": fsMIOspfIfHelloRcvd,
       "fsMIOspfIfHelloTxed": fsMIOspfIfHelloTxed,
       "fsMIOspfIfHelloDisd": fsMIOspfIfHelloDisd,
       "fsMIOspfIfDdpRcvd": fsMIOspfIfDdpRcvd,
       "fsMIOspfIfDdpTxed": fsMIOspfIfDdpTxed,
       "fsMIOspfIfDdpDisd": fsMIOspfIfDdpDisd,
       "fsMIOspfIfLrqRcvd": fsMIOspfIfLrqRcvd,
       "fsMIOspfIfLrqTxed": fsMIOspfIfLrqTxed,
       "fsMIOspfIfLrqDisd": fsMIOspfIfLrqDisd,
       "fsMIOspfIfLsuRcvd": fsMIOspfIfLsuRcvd,
       "fsMIOspfIfLsuTxed": fsMIOspfIfLsuTxed,
       "fsMIOspfIfLsuDisd": fsMIOspfIfLsuDisd,
       "fsMIOspfIfLakRcvd": fsMIOspfIfLakRcvd,
       "fsMIOspfIfLakTxed": fsMIOspfIfLakTxed,
       "fsMIOspfIfLakDisd": fsMIOspfIfLakDisd,
       "fsMIOspfIfBfdState": fsMIOspfIfBfdState,
       "fsMIOspfIfMD5AuthTable": fsMIOspfIfMD5AuthTable,
       "fsMIOspfIfMD5AuthEntry": fsMIOspfIfMD5AuthEntry,
       "fsMIOspfIfMD5AuthIpAddress": fsMIOspfIfMD5AuthIpAddress,
       "fsMIOspfIfMD5AuthAddressLessIf": fsMIOspfIfMD5AuthAddressLessIf,
       "fsMIOspfIfMD5AuthKeyId": fsMIOspfIfMD5AuthKeyId,
       "fsMIOspfIfMD5AuthKey": fsMIOspfIfMD5AuthKey,
       "fsMIOspfIfMD5AuthKeyStartAccept": fsMIOspfIfMD5AuthKeyStartAccept,
       "fsMIOspfIfMD5AuthKeyStartGenerate": fsMIOspfIfMD5AuthKeyStartGenerate,
       "fsMIOspfIfMD5AuthKeyStopGenerate": fsMIOspfIfMD5AuthKeyStopGenerate,
       "fsMIOspfIfMD5AuthKeyStopAccept": fsMIOspfIfMD5AuthKeyStopAccept,
       "fsMIOspfIfMD5AuthKeyStatus": fsMIOspfIfMD5AuthKeyStatus,
       "fsMIOspfVirtIfMD5AuthTable": fsMIOspfVirtIfMD5AuthTable,
       "fsMIOspfVirtIfMD5AuthEntry": fsMIOspfVirtIfMD5AuthEntry,
       "fsMIOspfVirtIfMD5AuthAreaId": fsMIOspfVirtIfMD5AuthAreaId,
       "fsMIOspfVirtIfMD5AuthNeighbor": fsMIOspfVirtIfMD5AuthNeighbor,
       "fsMIOspfVirtIfMD5AuthKeyId": fsMIOspfVirtIfMD5AuthKeyId,
       "fsMIOspfVirtIfMD5AuthKey": fsMIOspfVirtIfMD5AuthKey,
       "fsMIOspfVirtIfMD5AuthKeyStartAccept": fsMIOspfVirtIfMD5AuthKeyStartAccept,
       "fsMIOspfVirtIfMD5AuthKeyStartGenerate": fsMIOspfVirtIfMD5AuthKeyStartGenerate,
       "fsMIOspfVirtIfMD5AuthKeyStopGenerate": fsMIOspfVirtIfMD5AuthKeyStopGenerate,
       "fsMIOspfVirtIfMD5AuthKeyStopAccept": fsMIOspfVirtIfMD5AuthKeyStopAccept,
       "fsMIOspfVirtIfMD5AuthKeyStatus": fsMIOspfVirtIfMD5AuthKeyStatus,
       "fsMIOspfNbrTable": fsMIOspfNbrTable,
       "fsMIOspfNbrEntry": fsMIOspfNbrEntry,
       "fsMIOspfNbrIpAddr": fsMIOspfNbrIpAddr,
       "fsMIOspfNbrAddressLessIndex": fsMIOspfNbrAddressLessIndex,
       "fsMIOspfNbrDBSummaryQLen": fsMIOspfNbrDBSummaryQLen,
       "fsMIOspfNbrLSReqQLen": fsMIOspfNbrLSReqQLen,
       "fsMIOspfNbrRestartHelperStatus": fsMIOspfNbrRestartHelperStatus,
       "fsMIOspfNbrRestartHelperAge": fsMIOspfNbrRestartHelperAge,
       "fsMIOspfNbrRestartHelperExitReason": fsMIOspfNbrRestartHelperExitReason,
       "fsMIOspfNbrBfdState": fsMIOspfNbrBfdState,
       "fsMIOspfRoutingTable": fsMIOspfRoutingTable,
       "fsMIOspfRoutingEntry": fsMIOspfRoutingEntry,
       "fsMIOspfRouteIpAddr": fsMIOspfRouteIpAddr,
       "fsMIOspfRouteIpAddrMask": fsMIOspfRouteIpAddrMask,
       "fsMIOspfRouteIpTos": fsMIOspfRouteIpTos,
       "fsMIOspfRouteIpNextHop": fsMIOspfRouteIpNextHop,
       "fsMIOspfRouteType": fsMIOspfRouteType,
       "fsMIOspfRouteAreaId": fsMIOspfRouteAreaId,
       "fsMIOspfRouteCost": fsMIOspfRouteCost,
       "fsMIOspfRouteType2Cost": fsMIOspfRouteType2Cost,
       "fsMIOspfRouteInterfaceIndex": fsMIOspfRouteInterfaceIndex,
       "fsMIOspfSecIfTable": fsMIOspfSecIfTable,
       "fsMIOspfSecIfEntry": fsMIOspfSecIfEntry,
       "fsMIOspfPrimIpAddr": fsMIOspfPrimIpAddr,
       "fsMIOspfPrimAddresslessIf": fsMIOspfPrimAddresslessIf,
       "fsMIOspfSecIpAddr": fsMIOspfSecIpAddr,
       "fsMIOspfSecIpAddrMask": fsMIOspfSecIpAddrMask,
       "fsMIOspfSecIfStatus": fsMIOspfSecIfStatus,
       "fsMIOspfAreaAggregateTable": fsMIOspfAreaAggregateTable,
       "fsMIOspfAreaAggregateEntry": fsMIOspfAreaAggregateEntry,
       "fsMIOspfAreaAggregateAreaID": fsMIOspfAreaAggregateAreaID,
       "fsMIOspfAreaAggregateLsdbType": fsMIOspfAreaAggregateLsdbType,
       "fsMIOspfAreaAggregateNet": fsMIOspfAreaAggregateNet,
       "fsMIOspfAreaAggregateMask": fsMIOspfAreaAggregateMask,
       "fsMIOspfAreaAggregateExternalTag": fsMIOspfAreaAggregateExternalTag,
       "fsMIOspfAsExternalAggregationTable": fsMIOspfAsExternalAggregationTable,
       "fsMIOspfAsExternalAggregationEntry": fsMIOspfAsExternalAggregationEntry,
       "fsMIOspfAsExternalAggregationNet": fsMIOspfAsExternalAggregationNet,
       "fsMIOspfAsExternalAggregationMask": fsMIOspfAsExternalAggregationMask,
       "fsMIOspfAsExternalAggregationAreaId": fsMIOspfAsExternalAggregationAreaId,
       "fsMIOspfAsExternalAggregationEffect": fsMIOspfAsExternalAggregationEffect,
       "fsMIOspfAsExternalAggregationTranslation": fsMIOspfAsExternalAggregationTranslation,
       "fsMIOspfAsExternalAggregationStatus": fsMIOspfAsExternalAggregationStatus,
       "fsMIOspfOpaqueLSAGroup": fsMIOspfOpaqueLSAGroup,
       "fsMIOspfOpaqueLSAGeneralGroup": fsMIOspfOpaqueLSAGeneralGroup,
       "fsMIOspfOpaqueTable": fsMIOspfOpaqueTable,
       "fsMIOspfOpaqueEntry": fsMIOspfOpaqueEntry,
       "fsMIOspfOpaqueOption": fsMIOspfOpaqueOption,
       "fsMIOspfType11LsaCount": fsMIOspfType11LsaCount,
       "fsMIOspfType11LsaCksumSum": fsMIOspfType11LsaCksumSum,
       "fsMIOspfAreaIDValid": fsMIOspfAreaIDValid,
       "fsMIOspfOpaqueInterfaceTable": fsMIOspfOpaqueInterfaceTable,
       "fsMIOspfOpaqueInterfaceEntry": fsMIOspfOpaqueInterfaceEntry,
       "fsMIOspfOpaqueType9LsaCount": fsMIOspfOpaqueType9LsaCount,
       "fsMIOspfOpaqueType9LsaCksumSum": fsMIOspfOpaqueType9LsaCksumSum,
       "fsMIOspfType9LsdbTable": fsMIOspfType9LsdbTable,
       "fsMIOspfType9LsdbEntry": fsMIOspfType9LsdbEntry,
       "fsMIOspfType9LsdbIfIpAddress": fsMIOspfType9LsdbIfIpAddress,
       "fsMIOspfType9LsdbOpaqueType": fsMIOspfType9LsdbOpaqueType,
       "fsMIOspfType9LsdbLsid": fsMIOspfType9LsdbLsid,
       "fsMIOspfType9LsdbRouterId": fsMIOspfType9LsdbRouterId,
       "fsMIOspfType9LsdbSequence": fsMIOspfType9LsdbSequence,
       "fsMIOspfType9LsdbAge": fsMIOspfType9LsdbAge,
       "fsMIOspfType9LsdbChecksum": fsMIOspfType9LsdbChecksum,
       "fsMIOspfType9LsdbAdvertisement": fsMIOspfType9LsdbAdvertisement,
       "fsMIOspfType11LsdbTable": fsMIOspfType11LsdbTable,
       "fsMIOspfType11LsdbEntry": fsMIOspfType11LsdbEntry,
       "fsMIOspfType11LsdbOpaqueType": fsMIOspfType11LsdbOpaqueType,
       "fsMIOspfType11LsdbLsid": fsMIOspfType11LsdbLsid,
       "fsMIOspfType11LsdbRouterId": fsMIOspfType11LsdbRouterId,
       "fsMIOspfType11LsdbSequence": fsMIOspfType11LsdbSequence,
       "fsMIOspfType11LsdbAge": fsMIOspfType11LsdbAge,
       "fsMIOspfType11LsdbChecksum": fsMIOspfType11LsdbChecksum,
       "fsMIOspfType11LsdbAdvertisement": fsMIOspfType11LsdbAdvertisement,
       "fsMIOspfAppInfoDbTable": fsMIOspfAppInfoDbTable,
       "fsMIOspfAppInfoDbEntry": fsMIOspfAppInfoDbEntry,
       "fsMIOspfAppInfoDbAppid": fsMIOspfAppInfoDbAppid,
       "fsMIOspfAppInfoDbOpaqueType": fsMIOspfAppInfoDbOpaqueType,
       "fsMIOspfAppInfoDbLsaTypesSupported": fsMIOspfAppInfoDbLsaTypesSupported,
       "fsMIOspfAppInfoDbType9Gen": fsMIOspfAppInfoDbType9Gen,
       "fsMIOspfAppInfoDbType9Rcvd": fsMIOspfAppInfoDbType9Rcvd,
       "fsMIOspfAppInfoDbType10Gen": fsMIOspfAppInfoDbType10Gen,
       "fsMIOspfAppInfoDbType10Rcvd": fsMIOspfAppInfoDbType10Rcvd,
       "fsMIOspfAppInfoDbType11Gen": fsMIOspfAppInfoDbType11Gen,
       "fsMIOspfAppInfoDbType11Rcvd": fsMIOspfAppInfoDbType11Rcvd,
       "fsMIOspfRRDGroup": fsMIOspfRRDGroup,
       "fsMIOspfRRDGeneralGroup": fsMIOspfRRDGeneralGroup,
       "fsMIOspfRRDRouteTable": fsMIOspfRRDRouteTable,
       "fsMIOspfRRDRouteEntry": fsMIOspfRRDRouteEntry,
       "fsMIOspfRRDStatus": fsMIOspfRRDStatus,
       "fsMIOspfRRDSrcProtoMaskEnable": fsMIOspfRRDSrcProtoMaskEnable,
       "fsMIOspfRRDSrcProtoMaskDisable": fsMIOspfRRDSrcProtoMaskDisable,
       "fsMIOspfRRDRouteMapEnable": fsMIOspfRRDRouteMapEnable,
       "fsMIOspfRRDRouteConfigTable": fsMIOspfRRDRouteConfigTable,
       "fsMIOspfRRDRouteConfigEntry": fsMIOspfRRDRouteConfigEntry,
       "fsMIOspfRRDRouteDest": fsMIOspfRRDRouteDest,
       "fsMIOspfRRDRouteMask": fsMIOspfRRDRouteMask,
       "fsMIOspfRRDRouteMetric": fsMIOspfRRDRouteMetric,
       "fsMIOspfRRDRouteMetricType": fsMIOspfRRDRouteMetricType,
       "fsMIOspfRRDRouteTagType": fsMIOspfRRDRouteTagType,
       "fsMIOspfRRDRouteTag": fsMIOspfRRDRouteTag,
       "fsMIOspfRRDRouteStatus": fsMIOspfRRDRouteStatus,
       "fsMIOspfRRDMetricTable": fsMIOspfRRDMetricTable,
       "fsMIOspfRRDMerticEntry": fsMIOspfRRDMerticEntry,
       "fsMIOspfRRDProtocolId": fsMIOspfRRDProtocolId,
       "fsMIOspfRRDMetricValue": fsMIOspfRRDMetricValue,
       "fsMIOspfRRDMetricType": fsMIOspfRRDMetricType,
       "fsMIOspfVirtNbrTable": fsMIOspfVirtNbrTable,
       "fsMIOspfVirtNbrEntry": fsMIOspfVirtNbrEntry,
       "fsMIOspfVirtNbrRestartHelperStatus": fsMIOspfVirtNbrRestartHelperStatus,
       "fsMIOspfVirtNbrRestartHelperAge": fsMIOspfVirtNbrRestartHelperAge,
       "fsMIOspfVirtNbrRestartHelperExitReason": fsMIOspfVirtNbrRestartHelperExitReason,
       "fsMIospfDistInOutRouteMap": fsMIospfDistInOutRouteMap,
       "fsMIOspfDistInOutRouteMapTable": fsMIOspfDistInOutRouteMapTable,
       "fsMIOspfDistInOutRouteMapEntry": fsMIOspfDistInOutRouteMapEntry,
       "fsMIOspfDistInOutRouteMapName": fsMIOspfDistInOutRouteMapName,
       "fsMIOspfDistInOutRouteMapType": fsMIOspfDistInOutRouteMapType,
       "fsMIOspfDistInOutRouteMapValue": fsMIOspfDistInOutRouteMapValue,
       "fsMIOspfDistInOutRouteMapRowStatus": fsMIOspfDistInOutRouteMapRowStatus,
       "fsMIospfPreferenceGroup": fsMIospfPreferenceGroup,
       "fsMIOspfPreferenceTable": fsMIOspfPreferenceTable,
       "fsMIOspfPreferenceEntry": fsMIOspfPreferenceEntry,
       "fsMIOspfPreferenceValue": fsMIOspfPreferenceValue,
       "fsMIOspfIfAuthTable": fsMIOspfIfAuthTable,
       "fsMIOspfIfAuthEntry": fsMIOspfIfAuthEntry,
       "fsMIOspfIfAuthIpAddress": fsMIOspfIfAuthIpAddress,
       "fsMIOspfIfAuthAddressLessIf": fsMIOspfIfAuthAddressLessIf,
       "fsMIOspfIfAuthKeyId": fsMIOspfIfAuthKeyId,
       "fsMIOspfIfAuthKey": fsMIOspfIfAuthKey,
       "fsMIOspfIfAuthKeyStartAccept": fsMIOspfIfAuthKeyStartAccept,
       "fsMIOspfIfAuthKeyStartGenerate": fsMIOspfIfAuthKeyStartGenerate,
       "fsMIOspfIfAuthKeyStopGenerate": fsMIOspfIfAuthKeyStopGenerate,
       "fsMIOspfIfAuthKeyStopAccept": fsMIOspfIfAuthKeyStopAccept,
       "fsMIOspfIfAuthKeyStatus": fsMIOspfIfAuthKeyStatus,
       "fsMIOspfVirtIfAuthTable": fsMIOspfVirtIfAuthTable,
       "fsMIOspfVirtIfAuthEntry": fsMIOspfVirtIfAuthEntry,
       "fsMIOspfVirtIfAuthAreaId": fsMIOspfVirtIfAuthAreaId,
       "fsMIOspfVirtIfAuthNeighbor": fsMIOspfVirtIfAuthNeighbor,
       "fsMIOspfVirtIfAuthKeyId": fsMIOspfVirtIfAuthKeyId,
       "fsMIOspfVirtIfAuthKey": fsMIOspfVirtIfAuthKey,
       "fsMIOspfVirtIfAuthKeyStartAccept": fsMIOspfVirtIfAuthKeyStartAccept,
       "fsMIOspfVirtIfAuthKeyStartGenerate": fsMIOspfVirtIfAuthKeyStartGenerate,
       "fsMIOspfVirtIfAuthKeyStopGenerate": fsMIOspfVirtIfAuthKeyStopGenerate,
       "fsMIOspfVirtIfAuthKeyStopAccept": fsMIOspfVirtIfAuthKeyStopAccept,
       "fsMIOspfVirtIfAuthKeyStatus": fsMIOspfVirtIfAuthKeyStatus,
       "fsMIOspfTestGroup": fsMIOspfTestGroup,
       "fsMIOspfNotification": fsMIOspfNotification,
       "fsMIOspfTraps": fsMIOspfTraps,
       "fsMIOspfRestartStatusChange": fsMIOspfRestartStatusChange,
       "fsMIOspfNbrRestartHelperStatusChange": fsMIOspfNbrRestartHelperStatusChange,
       "fsMIOspfVirtNbrRestartHelperStatusChange": fsMIOspfVirtNbrRestartHelperStatusChange,
       "fsMIOspfHotStandbyEventTrap": fsMIOspfHotStandbyEventTrap}
)
