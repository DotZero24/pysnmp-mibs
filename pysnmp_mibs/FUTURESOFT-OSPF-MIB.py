# SNMP MIB module (FUTURESOFT-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/FUTURESOFT-OSPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:39 2025
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

(AreaID,
 BigMetric,
 InterfaceIndex,
 PositiveInteger,
 RouterID,
 Status,
 TOSType,
 ospfIfEntry,
 ospfNbrRtrId,
 ospfRouterId,
 ospfVirtIfEntry,
 ospfVirtNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "InterfaceIndex",
    "PositiveInteger",
    "RouterID",
    "Status",
    "TOSType",
    "ospfIfEntry",
    "ospfNbrRtrId",
    "ospfRouterId",
    "ospfVirtIfEntry",
    "ospfVirtNbrEntry")

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

futospf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10)
)
if mibBuilder.loadTexts:
    futospf.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FutospfGeneralGroup_ObjectIdentity = ObjectIdentity
futospfGeneralGroup = _FutospfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1)
)


class _FutOspfOverFlowState_Type(TruthValue):
    """Custom type futOspfOverFlowState based on TruthValue"""
    defaultValue = 2


_FutOspfOverFlowState_Type.__name__ = "TruthValue"
_FutOspfOverFlowState_Object = MibScalar
futOspfOverFlowState = _FutOspfOverFlowState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 1),
    _FutOspfOverFlowState_Type()
)
futOspfOverFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfOverFlowState.setStatus("current")
_FutOspfPktsRcvd_Type = Counter32
_FutOspfPktsRcvd_Object = MibScalar
futOspfPktsRcvd = _FutOspfPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 2),
    _FutOspfPktsRcvd_Type()
)
futOspfPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfPktsRcvd.setStatus("current")
_FutOspfPktsTxed_Type = Counter32
_FutOspfPktsTxed_Object = MibScalar
futOspfPktsTxed = _FutOspfPktsTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 3),
    _FutOspfPktsTxed_Type()
)
futOspfPktsTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfPktsTxed.setStatus("current")
_FutOspfPktsDisd_Type = Counter32
_FutOspfPktsDisd_Object = MibScalar
futOspfPktsDisd = _FutOspfPktsDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 4),
    _FutOspfPktsDisd_Type()
)
futOspfPktsDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfPktsDisd.setStatus("current")


class _FutOspfRFC1583Compatibility_Type(Status):
    """Custom type futOspfRFC1583Compatibility based on Status"""
    defaultValue = 1


_FutOspfRFC1583Compatibility_Type.__name__ = "Status"
_FutOspfRFC1583Compatibility_Object = MibScalar
futOspfRFC1583Compatibility = _FutOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 5),
    _FutOspfRFC1583Compatibility_Type()
)
futOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRFC1583Compatibility.setStatus("current")


class _FutOspfMaxAreas_Type(Integer32):
    """Custom type futOspfMaxAreas based on Integer32"""
    defaultValue = 4


_FutOspfMaxAreas_Type.__name__ = "Integer32"
_FutOspfMaxAreas_Object = MibScalar
futOspfMaxAreas = _FutOspfMaxAreas_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 6),
    _FutOspfMaxAreas_Type()
)
futOspfMaxAreas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxAreas.setStatus("deprecated")


class _FutOspfMaxLSAperArea_Type(Integer32):
    """Custom type futOspfMaxLSAperArea based on Integer32"""
    defaultValue = 128


_FutOspfMaxLSAperArea_Type.__name__ = "Integer32"
_FutOspfMaxLSAperArea_Object = MibScalar
futOspfMaxLSAperArea = _FutOspfMaxLSAperArea_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 7),
    _FutOspfMaxLSAperArea_Type()
)
futOspfMaxLSAperArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxLSAperArea.setStatus("deprecated")


class _FutOspfMaxExtLSAs_Type(Integer32):
    """Custom type futOspfMaxExtLSAs based on Integer32"""
    defaultValue = 512


_FutOspfMaxExtLSAs_Type.__name__ = "Integer32"
_FutOspfMaxExtLSAs_Object = MibScalar
futOspfMaxExtLSAs = _FutOspfMaxExtLSAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 8),
    _FutOspfMaxExtLSAs_Type()
)
futOspfMaxExtLSAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxExtLSAs.setStatus("deprecated")


class _FutOspfMaxSelfOrgLSAs_Type(Integer32):
    """Custom type futOspfMaxSelfOrgLSAs based on Integer32"""
    defaultValue = 128


_FutOspfMaxSelfOrgLSAs_Type.__name__ = "Integer32"
_FutOspfMaxSelfOrgLSAs_Object = MibScalar
futOspfMaxSelfOrgLSAs = _FutOspfMaxSelfOrgLSAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 9),
    _FutOspfMaxSelfOrgLSAs_Type()
)
futOspfMaxSelfOrgLSAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxSelfOrgLSAs.setStatus("deprecated")


class _FutOspfMaxRoutes_Type(Integer32):
    """Custom type futOspfMaxRoutes based on Integer32"""
    defaultValue = 256


_FutOspfMaxRoutes_Type.__name__ = "Integer32"
_FutOspfMaxRoutes_Object = MibScalar
futOspfMaxRoutes = _FutOspfMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 10),
    _FutOspfMaxRoutes_Type()
)
futOspfMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxRoutes.setStatus("deprecated")


class _FutOspfMaxLsaSize_Type(Integer32):
    """Custom type futOspfMaxLsaSize based on Integer32"""
    defaultValue = 128


_FutOspfMaxLsaSize_Type.__name__ = "Integer32"
_FutOspfMaxLsaSize_Object = MibScalar
futOspfMaxLsaSize = _FutOspfMaxLsaSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 11),
    _FutOspfMaxLsaSize_Type()
)
futOspfMaxLsaSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMaxLsaSize.setStatus("deprecated")


class _FutOspfTraceLevel_Type(Integer32):
    """Custom type futOspfTraceLevel based on Integer32"""
    defaultValue = 2048


_FutOspfTraceLevel_Type.__name__ = "Integer32"
_FutOspfTraceLevel_Object = MibScalar
futOspfTraceLevel = _FutOspfTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 12),
    _FutOspfTraceLevel_Type()
)
futOspfTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfTraceLevel.setStatus("current")


class _FutOspfMinLsaInterval_Type(Integer32):
    """Custom type futOspfMinLsaInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FutOspfMinLsaInterval_Type.__name__ = "Integer32"
_FutOspfMinLsaInterval_Object = MibScalar
futOspfMinLsaInterval = _FutOspfMinLsaInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 13),
    _FutOspfMinLsaInterval_Type()
)
futOspfMinLsaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfMinLsaInterval.setStatus("current")


class _FutOspfABRType_Type(Integer32):
    """Custom type futOspfABRType based on Integer32"""
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


_FutOspfABRType_Type.__name__ = "Integer32"
_FutOspfABRType_Object = MibScalar
futOspfABRType = _FutOspfABRType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 14),
    _FutOspfABRType_Type()
)
futOspfABRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfABRType.setStatus("current")


class _FutOspfNssaAsbrDefRtTrans_Type(Integer32):
    """Custom type futOspfNssaAsbrDefRtTrans based on Integer32"""
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


_FutOspfNssaAsbrDefRtTrans_Type.__name__ = "Integer32"
_FutOspfNssaAsbrDefRtTrans_Object = MibScalar
futOspfNssaAsbrDefRtTrans = _FutOspfNssaAsbrDefRtTrans_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 15),
    _FutOspfNssaAsbrDefRtTrans_Type()
)
futOspfNssaAsbrDefRtTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfNssaAsbrDefRtTrans.setStatus("current")


class _FutOspfDefaultPassiveInterface_Type(TruthValue):
    """Custom type futOspfDefaultPassiveInterface based on TruthValue"""
    defaultValue = 2


_FutOspfDefaultPassiveInterface_Type.__name__ = "TruthValue"
_FutOspfDefaultPassiveInterface_Object = MibScalar
futOspfDefaultPassiveInterface = _FutOspfDefaultPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 16),
    _FutOspfDefaultPassiveInterface_Type()
)
futOspfDefaultPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfDefaultPassiveInterface.setStatus("current")


class _FutOspfSpfHoldtime_Type(Integer32):
    """Custom type futOspfSpfHoldtime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfSpfHoldtime_Type.__name__ = "Integer32"
_FutOspfSpfHoldtime_Object = MibScalar
futOspfSpfHoldtime = _FutOspfSpfHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 17),
    _FutOspfSpfHoldtime_Type()
)
futOspfSpfHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfSpfHoldtime.setStatus("current")


class _FutOspfSpfDelay_Type(Integer32):
    """Custom type futOspfSpfDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfSpfDelay_Type.__name__ = "Integer32"
_FutOspfSpfDelay_Object = MibScalar
futOspfSpfDelay = _FutOspfSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 18),
    _FutOspfSpfDelay_Type()
)
futOspfSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfSpfDelay.setStatus("current")


class _FutOspfRestartSupport_Type(Integer32):
    """Custom type futOspfRestartSupport based on Integer32"""
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


_FutOspfRestartSupport_Type.__name__ = "Integer32"
_FutOspfRestartSupport_Object = MibScalar
futOspfRestartSupport = _FutOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 19),
    _FutOspfRestartSupport_Type()
)
futOspfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRestartSupport.setStatus("current")


class _FutOspfRestartInterval_Type(Integer32):
    """Custom type futOspfRestartInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_FutOspfRestartInterval_Type.__name__ = "Integer32"
_FutOspfRestartInterval_Object = MibScalar
futOspfRestartInterval = _FutOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 20),
    _FutOspfRestartInterval_Type()
)
futOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRestartInterval.setStatus("current")


class _FutOspfRestartStrictLsaChecking_Type(TruthValue):
    """Custom type futOspfRestartStrictLsaChecking based on TruthValue"""
    defaultValue = 2


_FutOspfRestartStrictLsaChecking_Type.__name__ = "TruthValue"
_FutOspfRestartStrictLsaChecking_Object = MibScalar
futOspfRestartStrictLsaChecking = _FutOspfRestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 21),
    _FutOspfRestartStrictLsaChecking_Type()
)
futOspfRestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRestartStrictLsaChecking.setStatus("current")


class _FutOspfRestartStatus_Type(Integer32):
    """Custom type futOspfRestartStatus based on Integer32"""
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


_FutOspfRestartStatus_Type.__name__ = "Integer32"
_FutOspfRestartStatus_Object = MibScalar
futOspfRestartStatus = _FutOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 22),
    _FutOspfRestartStatus_Type()
)
futOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRestartStatus.setStatus("current")
_FutOspfRestartAge_Type = Unsigned32
_FutOspfRestartAge_Object = MibScalar
futOspfRestartAge = _FutOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 23),
    _FutOspfRestartAge_Type()
)
futOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    futOspfRestartAge.setUnits("seconds")


class _FutOspfRestartExitReason_Type(Integer32):
    """Custom type futOspfRestartExitReason based on Integer32"""
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


_FutOspfRestartExitReason_Type.__name__ = "Integer32"
_FutOspfRestartExitReason_Object = MibScalar
futOspfRestartExitReason = _FutOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 24),
    _FutOspfRestartExitReason_Type()
)
futOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRestartExitReason.setStatus("current")


class _FutOspfHelperSupport_Type(Bits):
    """Custom type futOspfHelperSupport based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2),
          ("switchToRedundant", 3))
    )

_FutOspfHelperSupport_Type.__name__ = "Bits"
_FutOspfHelperSupport_Object = MibScalar
futOspfHelperSupport = _FutOspfHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 25),
    _FutOspfHelperSupport_Type()
)
futOspfHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfHelperSupport.setStatus("current")


class _FutOspfHelperGraceTimeLimit_Type(Integer32):
    """Custom type futOspfHelperGraceTimeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_FutOspfHelperGraceTimeLimit_Type.__name__ = "Integer32"
_FutOspfHelperGraceTimeLimit_Object = MibScalar
futOspfHelperGraceTimeLimit = _FutOspfHelperGraceTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 26),
    _FutOspfHelperGraceTimeLimit_Type()
)
futOspfHelperGraceTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfHelperGraceTimeLimit.setStatus("current")


class _FutOspfRestartAckState_Type(Integer32):
    """Custom type futOspfRestartAckState based on Integer32"""
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


_FutOspfRestartAckState_Type.__name__ = "Integer32"
_FutOspfRestartAckState_Object = MibScalar
futOspfRestartAckState = _FutOspfRestartAckState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 27),
    _FutOspfRestartAckState_Type()
)
futOspfRestartAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRestartAckState.setStatus("current")


class _FutOspfGraceLsaRetransmitCount_Type(Integer32):
    """Custom type futOspfGraceLsaRetransmitCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FutOspfGraceLsaRetransmitCount_Type.__name__ = "Integer32"
_FutOspfGraceLsaRetransmitCount_Object = MibScalar
futOspfGraceLsaRetransmitCount = _FutOspfGraceLsaRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 28),
    _FutOspfGraceLsaRetransmitCount_Type()
)
futOspfGraceLsaRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfGraceLsaRetransmitCount.setStatus("current")


class _FutOspfRestartReason_Type(Integer32):
    """Custom type futOspfRestartReason based on Integer32"""
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


_FutOspfRestartReason_Type.__name__ = "Integer32"
_FutOspfRestartReason_Object = MibScalar
futOspfRestartReason = _FutOspfRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 29),
    _FutOspfRestartReason_Type()
)
futOspfRestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRestartReason.setStatus("current")


class _FutOspfRTStaggeringInterval_Type(TimeTicks):
    """Custom type futOspfRTStaggeringInterval based on TimeTicks"""
    defaultValue = 10000


_FutOspfRTStaggeringInterval_Type.__name__ = "TimeTicks"
_FutOspfRTStaggeringInterval_Object = MibScalar
futOspfRTStaggeringInterval = _FutOspfRTStaggeringInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 30),
    _FutOspfRTStaggeringInterval_Type()
)
futOspfRTStaggeringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRTStaggeringInterval.setStatus("current")


class _FutOspfRTStaggeringStatus_Type(Integer32):
    """Custom type futOspfRTStaggeringStatus based on Integer32"""
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


_FutOspfRTStaggeringStatus_Type.__name__ = "Integer32"
_FutOspfRTStaggeringStatus_Object = MibScalar
futOspfRTStaggeringStatus = _FutOspfRTStaggeringStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 31),
    _FutOspfRTStaggeringStatus_Type()
)
futOspfRTStaggeringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRTStaggeringStatus.setStatus("current")


class _FutOspfHotStandbyAdminStatus_Type(Integer32):
    """Custom type futOspfHotStandbyAdminStatus based on Integer32"""
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


_FutOspfHotStandbyAdminStatus_Type.__name__ = "Integer32"
_FutOspfHotStandbyAdminStatus_Object = MibScalar
futOspfHotStandbyAdminStatus = _FutOspfHotStandbyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 32),
    _FutOspfHotStandbyAdminStatus_Type()
)
futOspfHotStandbyAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfHotStandbyAdminStatus.setStatus("current")


class _FutOspfHotStandbyState_Type(Integer32):
    """Custom type futOspfHotStandbyState based on Integer32"""
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


_FutOspfHotStandbyState_Type.__name__ = "Integer32"
_FutOspfHotStandbyState_Object = MibScalar
futOspfHotStandbyState = _FutOspfHotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 33),
    _FutOspfHotStandbyState_Type()
)
futOspfHotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfHotStandbyState.setStatus("current")


class _FutOspfDynamicBulkUpdStatus_Type(Integer32):
    """Custom type futOspfDynamicBulkUpdStatus based on Integer32"""
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


_FutOspfDynamicBulkUpdStatus_Type.__name__ = "Integer32"
_FutOspfDynamicBulkUpdStatus_Object = MibScalar
futOspfDynamicBulkUpdStatus = _FutOspfDynamicBulkUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 34),
    _FutOspfDynamicBulkUpdStatus_Type()
)
futOspfDynamicBulkUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfDynamicBulkUpdStatus.setStatus("current")
_FutOspfStanbyHelloSyncCount_Type = Counter32
_FutOspfStanbyHelloSyncCount_Object = MibScalar
futOspfStanbyHelloSyncCount = _FutOspfStanbyHelloSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 35),
    _FutOspfStanbyHelloSyncCount_Type()
)
futOspfStanbyHelloSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfStanbyHelloSyncCount.setStatus("current")
_FutOspfStanbyLsaSyncCount_Type = Counter32
_FutOspfStanbyLsaSyncCount_Object = MibScalar
futOspfStanbyLsaSyncCount = _FutOspfStanbyLsaSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 36),
    _FutOspfStanbyLsaSyncCount_Type()
)
futOspfStanbyLsaSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfStanbyLsaSyncCount.setStatus("current")
_FutOspfExtTraceLevel_Type = Integer32
_FutOspfExtTraceLevel_Object = MibScalar
futOspfExtTraceLevel = _FutOspfExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 37),
    _FutOspfExtTraceLevel_Type()
)
futOspfExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfExtTraceLevel.setStatus("current")


class _FutospfRouterIdPermanence_Type(Integer32):
    """Custom type futospfRouterIdPermanence based on Integer32"""
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


_FutospfRouterIdPermanence_Type.__name__ = "Integer32"
_FutospfRouterIdPermanence_Object = MibScalar
futospfRouterIdPermanence = _FutospfRouterIdPermanence_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 38),
    _FutospfRouterIdPermanence_Type()
)
futospfRouterIdPermanence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futospfRouterIdPermanence.setStatus("current")


class _FutOspfBfdStatus_Type(Integer32):
    """Custom type futOspfBfdStatus based on Integer32"""
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


_FutOspfBfdStatus_Type.__name__ = "Integer32"
_FutOspfBfdStatus_Object = MibScalar
futOspfBfdStatus = _FutOspfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 39),
    _FutOspfBfdStatus_Type()
)
futOspfBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfBfdStatus.setStatus("current")


class _FutOspfBfdAllIfState_Type(Integer32):
    """Custom type futOspfBfdAllIfState based on Integer32"""
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


_FutOspfBfdAllIfState_Type.__name__ = "Integer32"
_FutOspfBfdAllIfState_Object = MibScalar
futOspfBfdAllIfState = _FutOspfBfdAllIfState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 1, 40),
    _FutOspfBfdAllIfState_Type()
)
futOspfBfdAllIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfBfdAllIfState.setStatus("current")
_FutOspfAreaTable_Object = MibTable
futOspfAreaTable = _FutOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2)
)
if mibBuilder.loadTexts:
    futOspfAreaTable.setStatus("current")
_FutOspfAreaEntry_Object = MibTableRow
futOspfAreaEntry = _FutOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1)
)
futOspfAreaEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAreaId"),
)
if mibBuilder.loadTexts:
    futOspfAreaEntry.setStatus("current")
_FutOspfAreaId_Type = AreaID
_FutOspfAreaId_Object = MibTableColumn
futOspfAreaId = _FutOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 1),
    _FutOspfAreaId_Type()
)
futOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAreaId.setStatus("current")
_FutOspfAreaIfCount_Type = Gauge32
_FutOspfAreaIfCount_Object = MibTableColumn
futOspfAreaIfCount = _FutOspfAreaIfCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 2),
    _FutOspfAreaIfCount_Type()
)
futOspfAreaIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAreaIfCount.setStatus("current")
_FutOspfAreaNetCount_Type = Gauge32
_FutOspfAreaNetCount_Object = MibTableColumn
futOspfAreaNetCount = _FutOspfAreaNetCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 3),
    _FutOspfAreaNetCount_Type()
)
futOspfAreaNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAreaNetCount.setStatus("current")
_FutOspfAreaRtrCount_Type = Gauge32
_FutOspfAreaRtrCount_Object = MibTableColumn
futOspfAreaRtrCount = _FutOspfAreaRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 4),
    _FutOspfAreaRtrCount_Type()
)
futOspfAreaRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAreaRtrCount.setStatus("current")


class _FutOspfAreaNSSATranslatorRole_Type(Integer32):
    """Custom type futOspfAreaNSSATranslatorRole based on Integer32"""
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


_FutOspfAreaNSSATranslatorRole_Type.__name__ = "Integer32"
_FutOspfAreaNSSATranslatorRole_Object = MibTableColumn
futOspfAreaNSSATranslatorRole = _FutOspfAreaNSSATranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 5),
    _FutOspfAreaNSSATranslatorRole_Type()
)
futOspfAreaNSSATranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAreaNSSATranslatorRole.setStatus("current")


class _FutOspfAreaNSSATranslatorState_Type(Integer32):
    """Custom type futOspfAreaNSSATranslatorState based on Integer32"""
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


_FutOspfAreaNSSATranslatorState_Type.__name__ = "Integer32"
_FutOspfAreaNSSATranslatorState_Object = MibTableColumn
futOspfAreaNSSATranslatorState = _FutOspfAreaNSSATranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 6),
    _FutOspfAreaNSSATranslatorState_Type()
)
futOspfAreaNSSATranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAreaNSSATranslatorState.setStatus("current")


class _FutOspfAreaNSSATranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type futOspfAreaNSSATranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_FutOspfAreaNSSATranslatorStabilityInterval_Type.__name__ = "PositiveInteger"
_FutOspfAreaNSSATranslatorStabilityInterval_Object = MibTableColumn
futOspfAreaNSSATranslatorStabilityInterval = _FutOspfAreaNSSATranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 7),
    _FutOspfAreaNSSATranslatorStabilityInterval_Type()
)
futOspfAreaNSSATranslatorStabilityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAreaNSSATranslatorStabilityInterval.setStatus("current")
_FutOspfAreaNSSATranslatorEvents_Type = Counter32
_FutOspfAreaNSSATranslatorEvents_Object = MibTableColumn
futOspfAreaNSSATranslatorEvents = _FutOspfAreaNSSATranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 8),
    _FutOspfAreaNSSATranslatorEvents_Type()
)
futOspfAreaNSSATranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAreaNSSATranslatorEvents.setStatus("current")


class _FutOspfAreaDfInfOriginate_Type(Integer32):
    """Custom type futOspfAreaDfInfOriginate based on Integer32"""
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


_FutOspfAreaDfInfOriginate_Type.__name__ = "Integer32"
_FutOspfAreaDfInfOriginate_Object = MibTableColumn
futOspfAreaDfInfOriginate = _FutOspfAreaDfInfOriginate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 2, 1, 9),
    _FutOspfAreaDfInfOriginate_Type()
)
futOspfAreaDfInfOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAreaDfInfOriginate.setStatus("current")
_FutOspfHostTable_Object = MibTable
futOspfHostTable = _FutOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 3)
)
if mibBuilder.loadTexts:
    futOspfHostTable.setStatus("current")
_FutOspfHostEntry_Object = MibTableRow
futOspfHostEntry = _FutOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 3, 1)
)
futOspfHostEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfHostIpAddress"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfHostTOS"),
)
if mibBuilder.loadTexts:
    futOspfHostEntry.setStatus("current")
_FutOspfHostIpAddress_Type = IpAddress
_FutOspfHostIpAddress_Object = MibTableColumn
futOspfHostIpAddress = _FutOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 3, 1, 1),
    _FutOspfHostIpAddress_Type()
)
futOspfHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfHostIpAddress.setStatus("current")
_FutOspfHostTOS_Type = TOSType
_FutOspfHostTOS_Object = MibTableColumn
futOspfHostTOS = _FutOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 3, 1, 2),
    _FutOspfHostTOS_Type()
)
futOspfHostTOS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfHostTOS.setStatus("current")


class _FutOspfHostRouteIfIndex_Type(Integer32):
    """Custom type futOspfHostRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfHostRouteIfIndex_Type.__name__ = "Integer32"
_FutOspfHostRouteIfIndex_Object = MibTableColumn
futOspfHostRouteIfIndex = _FutOspfHostRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 3, 1, 3),
    _FutOspfHostRouteIfIndex_Type()
)
futOspfHostRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfHostRouteIfIndex.setStatus("current")
_FutOspfIfTable_Object = MibTable
futOspfIfTable = _FutOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4)
)
if mibBuilder.loadTexts:
    futOspfIfTable.setStatus("current")
_FutOspfIfEntry_Object = MibTableRow
futOspfIfEntry = _FutOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1)
)
futOspfIfEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfIpAddress"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    futOspfIfEntry.setStatus("current")
_FutOspfIfIpAddress_Type = IpAddress
_FutOspfIfIpAddress_Object = MibTableColumn
futOspfIfIpAddress = _FutOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 1),
    _FutOspfIfIpAddress_Type()
)
futOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfIpAddress.setStatus("current")


class _FutOspfAddressLessIf_Type(InterfaceIndex):
    """Custom type futOspfAddressLessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfAddressLessIf_Type.__name__ = "InterfaceIndex"
_FutOspfAddressLessIf_Object = MibTableColumn
futOspfAddressLessIf = _FutOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 2),
    _FutOspfAddressLessIf_Type()
)
futOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAddressLessIf.setStatus("current")


class _FutOspfIfOperState_Type(Integer32):
    """Custom type futOspfIfOperState based on Integer32"""
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


_FutOspfIfOperState_Type.__name__ = "Integer32"
_FutOspfIfOperState_Object = MibTableColumn
futOspfIfOperState = _FutOspfIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 3),
    _FutOspfIfOperState_Type()
)
futOspfIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfOperState.setStatus("current")
_FutOspfIfPassive_Type = TruthValue
_FutOspfIfPassive_Object = MibTableColumn
futOspfIfPassive = _FutOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 4),
    _FutOspfIfPassive_Type()
)
futOspfIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfPassive.setStatus("current")
_FutOspfIfNbrCount_Type = Gauge32
_FutOspfIfNbrCount_Object = MibTableColumn
futOspfIfNbrCount = _FutOspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 5),
    _FutOspfIfNbrCount_Type()
)
futOspfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfNbrCount.setStatus("current")
_FutOspfIfAdjCount_Type = Gauge32
_FutOspfIfAdjCount_Object = MibTableColumn
futOspfIfAdjCount = _FutOspfIfAdjCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 6),
    _FutOspfIfAdjCount_Type()
)
futOspfIfAdjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfAdjCount.setStatus("current")
_FutOspfIfHelloRcvd_Type = Counter32
_FutOspfIfHelloRcvd_Object = MibTableColumn
futOspfIfHelloRcvd = _FutOspfIfHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 7),
    _FutOspfIfHelloRcvd_Type()
)
futOspfIfHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfHelloRcvd.setStatus("current")
_FutOspfIfHelloTxed_Type = Counter32
_FutOspfIfHelloTxed_Object = MibTableColumn
futOspfIfHelloTxed = _FutOspfIfHelloTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 8),
    _FutOspfIfHelloTxed_Type()
)
futOspfIfHelloTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfHelloTxed.setStatus("current")
_FutOspfIfHelloDisd_Type = Counter32
_FutOspfIfHelloDisd_Object = MibTableColumn
futOspfIfHelloDisd = _FutOspfIfHelloDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 9),
    _FutOspfIfHelloDisd_Type()
)
futOspfIfHelloDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfHelloDisd.setStatus("current")
_FutOspfIfDdpRcvd_Type = Counter32
_FutOspfIfDdpRcvd_Object = MibTableColumn
futOspfIfDdpRcvd = _FutOspfIfDdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 10),
    _FutOspfIfDdpRcvd_Type()
)
futOspfIfDdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfDdpRcvd.setStatus("current")
_FutOspfIfDdpTxed_Type = Counter32
_FutOspfIfDdpTxed_Object = MibTableColumn
futOspfIfDdpTxed = _FutOspfIfDdpTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 11),
    _FutOspfIfDdpTxed_Type()
)
futOspfIfDdpTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfDdpTxed.setStatus("current")
_FutOspfIfDdpDisd_Type = Counter32
_FutOspfIfDdpDisd_Object = MibTableColumn
futOspfIfDdpDisd = _FutOspfIfDdpDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 12),
    _FutOspfIfDdpDisd_Type()
)
futOspfIfDdpDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfDdpDisd.setStatus("current")
_FutOspfIfLrqRcvd_Type = Counter32
_FutOspfIfLrqRcvd_Object = MibTableColumn
futOspfIfLrqRcvd = _FutOspfIfLrqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 13),
    _FutOspfIfLrqRcvd_Type()
)
futOspfIfLrqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLrqRcvd.setStatus("current")
_FutOspfIfLrqTxed_Type = Counter32
_FutOspfIfLrqTxed_Object = MibTableColumn
futOspfIfLrqTxed = _FutOspfIfLrqTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 14),
    _FutOspfIfLrqTxed_Type()
)
futOspfIfLrqTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLrqTxed.setStatus("current")
_FutOspfIfLrqDisd_Type = Counter32
_FutOspfIfLrqDisd_Object = MibTableColumn
futOspfIfLrqDisd = _FutOspfIfLrqDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 15),
    _FutOspfIfLrqDisd_Type()
)
futOspfIfLrqDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLrqDisd.setStatus("current")
_FutOspfIfLsuRcvd_Type = Counter32
_FutOspfIfLsuRcvd_Object = MibTableColumn
futOspfIfLsuRcvd = _FutOspfIfLsuRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 16),
    _FutOspfIfLsuRcvd_Type()
)
futOspfIfLsuRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLsuRcvd.setStatus("current")
_FutOspfIfLsuTxed_Type = Counter32
_FutOspfIfLsuTxed_Object = MibTableColumn
futOspfIfLsuTxed = _FutOspfIfLsuTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 17),
    _FutOspfIfLsuTxed_Type()
)
futOspfIfLsuTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLsuTxed.setStatus("current")
_FutOspfIfLsuDisd_Type = Counter32
_FutOspfIfLsuDisd_Object = MibTableColumn
futOspfIfLsuDisd = _FutOspfIfLsuDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 18),
    _FutOspfIfLsuDisd_Type()
)
futOspfIfLsuDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLsuDisd.setStatus("current")
_FutOspfIfLakRcvd_Type = Counter32
_FutOspfIfLakRcvd_Object = MibTableColumn
futOspfIfLakRcvd = _FutOspfIfLakRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 19),
    _FutOspfIfLakRcvd_Type()
)
futOspfIfLakRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLakRcvd.setStatus("current")
_FutOspfIfLakTxed_Type = Counter32
_FutOspfIfLakTxed_Object = MibTableColumn
futOspfIfLakTxed = _FutOspfIfLakTxed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 20),
    _FutOspfIfLakTxed_Type()
)
futOspfIfLakTxed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLakTxed.setStatus("current")
_FutOspfIfLakDisd_Type = Counter32
_FutOspfIfLakDisd_Object = MibTableColumn
futOspfIfLakDisd = _FutOspfIfLakDisd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 21),
    _FutOspfIfLakDisd_Type()
)
futOspfIfLakDisd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfIfLakDisd.setStatus("current")


class _FutOspfIfBfdState_Type(Integer32):
    """Custom type futOspfIfBfdState based on Integer32"""
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


_FutOspfIfBfdState_Type.__name__ = "Integer32"
_FutOspfIfBfdState_Object = MibTableColumn
futOspfIfBfdState = _FutOspfIfBfdState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 4, 1, 22),
    _FutOspfIfBfdState_Type()
)
futOspfIfBfdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfBfdState.setStatus("current")
_FutOspfIfMD5AuthTable_Object = MibTable
futOspfIfMD5AuthTable = _FutOspfIfMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5)
)
if mibBuilder.loadTexts:
    futOspfIfMD5AuthTable.setStatus("current")
_FutOspfIfMD5AuthEntry_Object = MibTableRow
futOspfIfMD5AuthEntry = _FutOspfIfMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1)
)
futOspfIfMD5AuthEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfMD5AuthIpAddress"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfMD5AuthAddressLessIf"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfMD5AuthKeyId"),
)
if mibBuilder.loadTexts:
    futOspfIfMD5AuthEntry.setStatus("current")
_FutOspfIfMD5AuthIpAddress_Type = IpAddress
_FutOspfIfMD5AuthIpAddress_Object = MibTableColumn
futOspfIfMD5AuthIpAddress = _FutOspfIfMD5AuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 1),
    _FutOspfIfMD5AuthIpAddress_Type()
)
futOspfIfMD5AuthIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthIpAddress.setStatus("current")


class _FutOspfIfMD5AuthAddressLessIf_Type(InterfaceIndex):
    """Custom type futOspfIfMD5AuthAddressLessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfIfMD5AuthAddressLessIf_Type.__name__ = "InterfaceIndex"
_FutOspfIfMD5AuthAddressLessIf_Object = MibTableColumn
futOspfIfMD5AuthAddressLessIf = _FutOspfIfMD5AuthAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 2),
    _FutOspfIfMD5AuthAddressLessIf_Type()
)
futOspfIfMD5AuthAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthAddressLessIf.setStatus("current")


class _FutOspfIfMD5AuthKeyId_Type(Integer32):
    """Custom type futOspfIfMD5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfIfMD5AuthKeyId_Type.__name__ = "Integer32"
_FutOspfIfMD5AuthKeyId_Object = MibTableColumn
futOspfIfMD5AuthKeyId = _FutOspfIfMD5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 3),
    _FutOspfIfMD5AuthKeyId_Type()
)
futOspfIfMD5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyId.setStatus("current")


class _FutOspfIfMD5AuthKey_Type(OctetString):
    """Custom type futOspfIfMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FutOspfIfMD5AuthKey_Type.__name__ = "OctetString"
_FutOspfIfMD5AuthKey_Object = MibTableColumn
futOspfIfMD5AuthKey = _FutOspfIfMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 4),
    _FutOspfIfMD5AuthKey_Type()
)
futOspfIfMD5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKey.setStatus("current")
_FutOspfIfMD5AuthKeyStartAccept_Type = Integer32
_FutOspfIfMD5AuthKeyStartAccept_Object = MibTableColumn
futOspfIfMD5AuthKeyStartAccept = _FutOspfIfMD5AuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 5),
    _FutOspfIfMD5AuthKeyStartAccept_Type()
)
futOspfIfMD5AuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyStartAccept.setStatus("current")
_FutOspfIfMD5AuthKeyStartGenerate_Type = Integer32
_FutOspfIfMD5AuthKeyStartGenerate_Object = MibTableColumn
futOspfIfMD5AuthKeyStartGenerate = _FutOspfIfMD5AuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 6),
    _FutOspfIfMD5AuthKeyStartGenerate_Type()
)
futOspfIfMD5AuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyStartGenerate.setStatus("current")


class _FutOspfIfMD5AuthKeyStopGenerate_Type(Integer32):
    """Custom type futOspfIfMD5AuthKeyStopGenerate based on Integer32"""
    defaultValue = -1


_FutOspfIfMD5AuthKeyStopGenerate_Type.__name__ = "Integer32"
_FutOspfIfMD5AuthKeyStopGenerate_Object = MibTableColumn
futOspfIfMD5AuthKeyStopGenerate = _FutOspfIfMD5AuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 7),
    _FutOspfIfMD5AuthKeyStopGenerate_Type()
)
futOspfIfMD5AuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyStopGenerate.setStatus("current")


class _FutOspfIfMD5AuthKeyStopAccept_Type(Integer32):
    """Custom type futOspfIfMD5AuthKeyStopAccept based on Integer32"""
    defaultValue = -1


_FutOspfIfMD5AuthKeyStopAccept_Type.__name__ = "Integer32"
_FutOspfIfMD5AuthKeyStopAccept_Object = MibTableColumn
futOspfIfMD5AuthKeyStopAccept = _FutOspfIfMD5AuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 8),
    _FutOspfIfMD5AuthKeyStopAccept_Type()
)
futOspfIfMD5AuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyStopAccept.setStatus("current")


class _FutOspfIfMD5AuthKeyStatus_Type(Integer32):
    """Custom type futOspfIfMD5AuthKeyStatus based on Integer32"""
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


_FutOspfIfMD5AuthKeyStatus_Type.__name__ = "Integer32"
_FutOspfIfMD5AuthKeyStatus_Object = MibTableColumn
futOspfIfMD5AuthKeyStatus = _FutOspfIfMD5AuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 5, 1, 9),
    _FutOspfIfMD5AuthKeyStatus_Type()
)
futOspfIfMD5AuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfMD5AuthKeyStatus.setStatus("current")
_FutOspfVirtIfMD5AuthTable_Object = MibTable
futOspfVirtIfMD5AuthTable = _FutOspfVirtIfMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6)
)
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthTable.setStatus("current")
_FutOspfVirtIfMD5AuthEntry_Object = MibTableRow
futOspfVirtIfMD5AuthEntry = _FutOspfVirtIfMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1)
)
futOspfVirtIfMD5AuthEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfMD5AuthAreaId"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfMD5AuthNeighbor"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfMD5AuthKeyId"),
)
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthEntry.setStatus("current")
_FutOspfVirtIfMD5AuthAreaId_Type = AreaID
_FutOspfVirtIfMD5AuthAreaId_Object = MibTableColumn
futOspfVirtIfMD5AuthAreaId = _FutOspfVirtIfMD5AuthAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 1),
    _FutOspfVirtIfMD5AuthAreaId_Type()
)
futOspfVirtIfMD5AuthAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthAreaId.setStatus("current")
_FutOspfVirtIfMD5AuthNeighbor_Type = RouterID
_FutOspfVirtIfMD5AuthNeighbor_Object = MibTableColumn
futOspfVirtIfMD5AuthNeighbor = _FutOspfVirtIfMD5AuthNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 2),
    _FutOspfVirtIfMD5AuthNeighbor_Type()
)
futOspfVirtIfMD5AuthNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthNeighbor.setStatus("current")


class _FutOspfVirtIfMD5AuthKeyId_Type(Integer32):
    """Custom type futOspfVirtIfMD5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfVirtIfMD5AuthKeyId_Type.__name__ = "Integer32"
_FutOspfVirtIfMD5AuthKeyId_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyId = _FutOspfVirtIfMD5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 3),
    _FutOspfVirtIfMD5AuthKeyId_Type()
)
futOspfVirtIfMD5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyId.setStatus("current")


class _FutOspfVirtIfMD5AuthKey_Type(OctetString):
    """Custom type futOspfVirtIfMD5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FutOspfVirtIfMD5AuthKey_Type.__name__ = "OctetString"
_FutOspfVirtIfMD5AuthKey_Object = MibTableColumn
futOspfVirtIfMD5AuthKey = _FutOspfVirtIfMD5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 4),
    _FutOspfVirtIfMD5AuthKey_Type()
)
futOspfVirtIfMD5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKey.setStatus("current")
_FutOspfVirtIfMD5AuthKeyStartAccept_Type = Integer32
_FutOspfVirtIfMD5AuthKeyStartAccept_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyStartAccept = _FutOspfVirtIfMD5AuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 5),
    _FutOspfVirtIfMD5AuthKeyStartAccept_Type()
)
futOspfVirtIfMD5AuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyStartAccept.setStatus("current")
_FutOspfVirtIfMD5AuthKeyStartGenerate_Type = Integer32
_FutOspfVirtIfMD5AuthKeyStartGenerate_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyStartGenerate = _FutOspfVirtIfMD5AuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 6),
    _FutOspfVirtIfMD5AuthKeyStartGenerate_Type()
)
futOspfVirtIfMD5AuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyStartGenerate.setStatus("current")


class _FutOspfVirtIfMD5AuthKeyStopGenerate_Type(Integer32):
    """Custom type futOspfVirtIfMD5AuthKeyStopGenerate based on Integer32"""
    defaultValue = -1


_FutOspfVirtIfMD5AuthKeyStopGenerate_Type.__name__ = "Integer32"
_FutOspfVirtIfMD5AuthKeyStopGenerate_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyStopGenerate = _FutOspfVirtIfMD5AuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 7),
    _FutOspfVirtIfMD5AuthKeyStopGenerate_Type()
)
futOspfVirtIfMD5AuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyStopGenerate.setStatus("current")


class _FutOspfVirtIfMD5AuthKeyStopAccept_Type(Integer32):
    """Custom type futOspfVirtIfMD5AuthKeyStopAccept based on Integer32"""
    defaultValue = -1


_FutOspfVirtIfMD5AuthKeyStopAccept_Type.__name__ = "Integer32"
_FutOspfVirtIfMD5AuthKeyStopAccept_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyStopAccept = _FutOspfVirtIfMD5AuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 8),
    _FutOspfVirtIfMD5AuthKeyStopAccept_Type()
)
futOspfVirtIfMD5AuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyStopAccept.setStatus("current")


class _FutOspfVirtIfMD5AuthKeyStatus_Type(Integer32):
    """Custom type futOspfVirtIfMD5AuthKeyStatus based on Integer32"""
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


_FutOspfVirtIfMD5AuthKeyStatus_Type.__name__ = "Integer32"
_FutOspfVirtIfMD5AuthKeyStatus_Object = MibTableColumn
futOspfVirtIfMD5AuthKeyStatus = _FutOspfVirtIfMD5AuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 6, 1, 9),
    _FutOspfVirtIfMD5AuthKeyStatus_Type()
)
futOspfVirtIfMD5AuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfMD5AuthKeyStatus.setStatus("current")
_FutOspfNbrTable_Object = MibTable
futOspfNbrTable = _FutOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7)
)
if mibBuilder.loadTexts:
    futOspfNbrTable.setStatus("current")
_FutOspfNbrEntry_Object = MibTableRow
futOspfNbrEntry = _FutOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1)
)
futOspfNbrEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfNbrIpAddr"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    futOspfNbrEntry.setStatus("current")
_FutOspfNbrIpAddr_Type = IpAddress
_FutOspfNbrIpAddr_Object = MibTableColumn
futOspfNbrIpAddr = _FutOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 1),
    _FutOspfNbrIpAddr_Type()
)
futOspfNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfNbrIpAddr.setStatus("current")


class _FutOspfNbrAddressLessIndex_Type(InterfaceIndex):
    """Custom type futOspfNbrAddressLessIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfNbrAddressLessIndex_Type.__name__ = "InterfaceIndex"
_FutOspfNbrAddressLessIndex_Object = MibTableColumn
futOspfNbrAddressLessIndex = _FutOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 2),
    _FutOspfNbrAddressLessIndex_Type()
)
futOspfNbrAddressLessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfNbrAddressLessIndex.setStatus("current")
_FutOspfNbrDBSummaryQLen_Type = Gauge32
_FutOspfNbrDBSummaryQLen_Object = MibTableColumn
futOspfNbrDBSummaryQLen = _FutOspfNbrDBSummaryQLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 3),
    _FutOspfNbrDBSummaryQLen_Type()
)
futOspfNbrDBSummaryQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrDBSummaryQLen.setStatus("current")
_FutOspfNbrLSReqQLen_Type = Gauge32
_FutOspfNbrLSReqQLen_Object = MibTableColumn
futOspfNbrLSReqQLen = _FutOspfNbrLSReqQLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 4),
    _FutOspfNbrLSReqQLen_Type()
)
futOspfNbrLSReqQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrLSReqQLen.setStatus("current")


class _FutOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type futOspfNbrRestartHelperStatus based on Integer32"""
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


_FutOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_FutOspfNbrRestartHelperStatus_Object = MibTableColumn
futOspfNbrRestartHelperStatus = _FutOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 5),
    _FutOspfNbrRestartHelperStatus_Type()
)
futOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrRestartHelperStatus.setStatus("current")
_FutOspfNbrRestartHelperAge_Type = Unsigned32
_FutOspfNbrRestartHelperAge_Object = MibTableColumn
futOspfNbrRestartHelperAge = _FutOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 6),
    _FutOspfNbrRestartHelperAge_Type()
)
futOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    futOspfNbrRestartHelperAge.setUnits("seconds")


class _FutOspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type futOspfNbrRestartHelperExitReason based on Integer32"""
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


_FutOspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_FutOspfNbrRestartHelperExitReason_Object = MibTableColumn
futOspfNbrRestartHelperExitReason = _FutOspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 7),
    _FutOspfNbrRestartHelperExitReason_Type()
)
futOspfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrRestartHelperExitReason.setStatus("current")


class _FutOspfNbrBfdState_Type(Integer32):
    """Custom type futOspfNbrBfdState based on Integer32"""
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


_FutOspfNbrBfdState_Type.__name__ = "Integer32"
_FutOspfNbrBfdState_Object = MibTableColumn
futOspfNbrBfdState = _FutOspfNbrBfdState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 7, 1, 8),
    _FutOspfNbrBfdState_Type()
)
futOspfNbrBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfNbrBfdState.setStatus("current")
_FutOspfRoutingTable_Object = MibTable
futOspfRoutingTable = _FutOspfRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8)
)
if mibBuilder.loadTexts:
    futOspfRoutingTable.setStatus("current")
_FutOspfRoutingEntry_Object = MibTableRow
futOspfRoutingEntry = _FutOspfRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1)
)
futOspfRoutingEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRouteIpAddr"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRouteIpAddrMask"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRouteIpTos"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRouteIpNextHop"),
)
if mibBuilder.loadTexts:
    futOspfRoutingEntry.setStatus("current")
_FutOspfRouteIpAddr_Type = IpAddress
_FutOspfRouteIpAddr_Object = MibTableColumn
futOspfRouteIpAddr = _FutOspfRouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 1),
    _FutOspfRouteIpAddr_Type()
)
futOspfRouteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRouteIpAddr.setStatus("current")
_FutOspfRouteIpAddrMask_Type = IpAddress
_FutOspfRouteIpAddrMask_Object = MibTableColumn
futOspfRouteIpAddrMask = _FutOspfRouteIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 2),
    _FutOspfRouteIpAddrMask_Type()
)
futOspfRouteIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRouteIpAddrMask.setStatus("current")
_FutOspfRouteIpTos_Type = TOSType
_FutOspfRouteIpTos_Object = MibTableColumn
futOspfRouteIpTos = _FutOspfRouteIpTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 3),
    _FutOspfRouteIpTos_Type()
)
futOspfRouteIpTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRouteIpTos.setStatus("current")
_FutOspfRouteIpNextHop_Type = IpAddress
_FutOspfRouteIpNextHop_Object = MibTableColumn
futOspfRouteIpNextHop = _FutOspfRouteIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 4),
    _FutOspfRouteIpNextHop_Type()
)
futOspfRouteIpNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRouteIpNextHop.setStatus("current")


class _FutOspfRouteType_Type(Integer32):
    """Custom type futOspfRouteType based on Integer32"""
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


_FutOspfRouteType_Type.__name__ = "Integer32"
_FutOspfRouteType_Object = MibTableColumn
futOspfRouteType = _FutOspfRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 5),
    _FutOspfRouteType_Type()
)
futOspfRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRouteType.setStatus("current")
_FutOspfRouteAreaId_Type = IpAddress
_FutOspfRouteAreaId_Object = MibTableColumn
futOspfRouteAreaId = _FutOspfRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 6),
    _FutOspfRouteAreaId_Type()
)
futOspfRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRouteAreaId.setStatus("current")
_FutOspfRouteCost_Type = BigMetric
_FutOspfRouteCost_Object = MibTableColumn
futOspfRouteCost = _FutOspfRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 7),
    _FutOspfRouteCost_Type()
)
futOspfRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRouteCost.setStatus("current")
_FutOspfRouteType2Cost_Type = BigMetric
_FutOspfRouteType2Cost_Object = MibTableColumn
futOspfRouteType2Cost = _FutOspfRouteType2Cost_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 8),
    _FutOspfRouteType2Cost_Type()
)
futOspfRouteType2Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRouteType2Cost.setStatus("current")
_FutOspfRouteInterfaceIndex_Type = InterfaceIndex
_FutOspfRouteInterfaceIndex_Object = MibTableColumn
futOspfRouteInterfaceIndex = _FutOspfRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 8, 1, 9),
    _FutOspfRouteInterfaceIndex_Type()
)
futOspfRouteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfRouteInterfaceIndex.setStatus("current")
_FutOspfSecIfTable_Object = MibTable
futOspfSecIfTable = _FutOspfSecIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9)
)
if mibBuilder.loadTexts:
    futOspfSecIfTable.setStatus("current")
_FutOspfSecIfEntry_Object = MibTableRow
futOspfSecIfEntry = _FutOspfSecIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1)
)
futOspfSecIfEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfPrimIpAddr"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfPrimAddresslessIf"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfSecIpAddr"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfSecIpAddrMask"),
)
if mibBuilder.loadTexts:
    futOspfSecIfEntry.setStatus("current")
_FutOspfPrimIpAddr_Type = IpAddress
_FutOspfPrimIpAddr_Object = MibTableColumn
futOspfPrimIpAddr = _FutOspfPrimIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1, 1),
    _FutOspfPrimIpAddr_Type()
)
futOspfPrimIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfPrimIpAddr.setStatus("current")


class _FutOspfPrimAddresslessIf_Type(InterfaceIndex):
    """Custom type futOspfPrimAddresslessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfPrimAddresslessIf_Type.__name__ = "InterfaceIndex"
_FutOspfPrimAddresslessIf_Object = MibTableColumn
futOspfPrimAddresslessIf = _FutOspfPrimAddresslessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1, 2),
    _FutOspfPrimAddresslessIf_Type()
)
futOspfPrimAddresslessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfPrimAddresslessIf.setStatus("current")
_FutOspfSecIpAddr_Type = IpAddress
_FutOspfSecIpAddr_Object = MibTableColumn
futOspfSecIpAddr = _FutOspfSecIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1, 3),
    _FutOspfSecIpAddr_Type()
)
futOspfSecIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfSecIpAddr.setStatus("current")
_FutOspfSecIpAddrMask_Type = IpAddress
_FutOspfSecIpAddrMask_Object = MibTableColumn
futOspfSecIpAddrMask = _FutOspfSecIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1, 4),
    _FutOspfSecIpAddrMask_Type()
)
futOspfSecIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfSecIpAddrMask.setStatus("current")
_FutOspfSecIfStatus_Type = RowStatus
_FutOspfSecIfStatus_Object = MibTableColumn
futOspfSecIfStatus = _FutOspfSecIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 9, 1, 5),
    _FutOspfSecIfStatus_Type()
)
futOspfSecIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfSecIfStatus.setStatus("current")
_FutOspfAreaAggregateTable_Object = MibTable
futOspfAreaAggregateTable = _FutOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10)
)
if mibBuilder.loadTexts:
    futOspfAreaAggregateTable.setStatus("current")
_FutOspfAreaAggregateEntry_Object = MibTableRow
futOspfAreaAggregateEntry = _FutOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1)
)
futOspfAreaAggregateEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAreaAggregateAreaID"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAreaAggregateLsdbType"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAreaAggregateNet"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    futOspfAreaAggregateEntry.setStatus("current")
_FutOspfAreaAggregateAreaID_Type = AreaID
_FutOspfAreaAggregateAreaID_Object = MibTableColumn
futOspfAreaAggregateAreaID = _FutOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1, 1),
    _FutOspfAreaAggregateAreaID_Type()
)
futOspfAreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAreaAggregateAreaID.setStatus("current")


class _FutOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type futOspfAreaAggregateLsdbType based on Integer32"""
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


_FutOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_FutOspfAreaAggregateLsdbType_Object = MibTableColumn
futOspfAreaAggregateLsdbType = _FutOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1, 2),
    _FutOspfAreaAggregateLsdbType_Type()
)
futOspfAreaAggregateLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAreaAggregateLsdbType.setStatus("current")
_FutOspfAreaAggregateNet_Type = IpAddress
_FutOspfAreaAggregateNet_Object = MibTableColumn
futOspfAreaAggregateNet = _FutOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1, 3),
    _FutOspfAreaAggregateNet_Type()
)
futOspfAreaAggregateNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAreaAggregateNet.setStatus("current")
_FutOspfAreaAggregateMask_Type = IpAddress
_FutOspfAreaAggregateMask_Object = MibTableColumn
futOspfAreaAggregateMask = _FutOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1, 4),
    _FutOspfAreaAggregateMask_Type()
)
futOspfAreaAggregateMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAreaAggregateMask.setStatus("current")
_FutOspfAreaAggregateExternalTag_Type = Integer32
_FutOspfAreaAggregateExternalTag_Object = MibTableColumn
futOspfAreaAggregateExternalTag = _FutOspfAreaAggregateExternalTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 10, 1, 5),
    _FutOspfAreaAggregateExternalTag_Type()
)
futOspfAreaAggregateExternalTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAreaAggregateExternalTag.setStatus("current")
_FutOspfAsExternalAggregationTable_Object = MibTable
futOspfAsExternalAggregationTable = _FutOspfAsExternalAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11)
)
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationTable.setStatus("current")
_FutOspfAsExternalAggregationEntry_Object = MibTableRow
futOspfAsExternalAggregationEntry = _FutOspfAsExternalAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1)
)
futOspfAsExternalAggregationEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAsExternalAggregationNet"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAsExternalAggregationMask"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAsExternalAggregationAreaId"),
)
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationEntry.setStatus("current")
_FutOspfAsExternalAggregationNet_Type = IpAddress
_FutOspfAsExternalAggregationNet_Object = MibTableColumn
futOspfAsExternalAggregationNet = _FutOspfAsExternalAggregationNet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 1),
    _FutOspfAsExternalAggregationNet_Type()
)
futOspfAsExternalAggregationNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationNet.setStatus("current")
_FutOspfAsExternalAggregationMask_Type = IpAddress
_FutOspfAsExternalAggregationMask_Object = MibTableColumn
futOspfAsExternalAggregationMask = _FutOspfAsExternalAggregationMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 2),
    _FutOspfAsExternalAggregationMask_Type()
)
futOspfAsExternalAggregationMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationMask.setStatus("current")
_FutOspfAsExternalAggregationAreaId_Type = AreaID
_FutOspfAsExternalAggregationAreaId_Object = MibTableColumn
futOspfAsExternalAggregationAreaId = _FutOspfAsExternalAggregationAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 3),
    _FutOspfAsExternalAggregationAreaId_Type()
)
futOspfAsExternalAggregationAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationAreaId.setStatus("current")


class _FutOspfAsExternalAggregationEffect_Type(Integer32):
    """Custom type futOspfAsExternalAggregationEffect based on Integer32"""
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


_FutOspfAsExternalAggregationEffect_Type.__name__ = "Integer32"
_FutOspfAsExternalAggregationEffect_Object = MibTableColumn
futOspfAsExternalAggregationEffect = _FutOspfAsExternalAggregationEffect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 4),
    _FutOspfAsExternalAggregationEffect_Type()
)
futOspfAsExternalAggregationEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationEffect.setStatus("current")


class _FutOspfAsExternalAggregationTranslation_Type(Integer32):
    """Custom type futOspfAsExternalAggregationTranslation based on Integer32"""
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


_FutOspfAsExternalAggregationTranslation_Type.__name__ = "Integer32"
_FutOspfAsExternalAggregationTranslation_Object = MibTableColumn
futOspfAsExternalAggregationTranslation = _FutOspfAsExternalAggregationTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 5),
    _FutOspfAsExternalAggregationTranslation_Type()
)
futOspfAsExternalAggregationTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationTranslation.setStatus("current")
_FutOspfAsExternalAggregationStatus_Type = RowStatus
_FutOspfAsExternalAggregationStatus_Object = MibTableColumn
futOspfAsExternalAggregationStatus = _FutOspfAsExternalAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 11, 1, 6),
    _FutOspfAsExternalAggregationStatus_Type()
)
futOspfAsExternalAggregationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfAsExternalAggregationStatus.setStatus("current")
_FutOspfOpaqueLSAGroup_ObjectIdentity = ObjectIdentity
futOspfOpaqueLSAGroup = _FutOspfOpaqueLSAGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12)
)
_FutOspfOpaqueLSAGeneralGroup_ObjectIdentity = ObjectIdentity
futOspfOpaqueLSAGeneralGroup = _FutOspfOpaqueLSAGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 1)
)


class _FutOspfOpaqueOption_Type(Integer32):
    """Custom type futOspfOpaqueOption based on Integer32"""
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


_FutOspfOpaqueOption_Type.__name__ = "Integer32"
_FutOspfOpaqueOption_Object = MibScalar
futOspfOpaqueOption = _FutOspfOpaqueOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 1, 1),
    _FutOspfOpaqueOption_Type()
)
futOspfOpaqueOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfOpaqueOption.setStatus("current")
_FutOspfType11LsaCount_Type = Gauge32
_FutOspfType11LsaCount_Object = MibScalar
futOspfType11LsaCount = _FutOspfType11LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 1, 2),
    _FutOspfType11LsaCount_Type()
)
futOspfType11LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsaCount.setStatus("current")
_FutOspfType11LsaCksumSum_Type = Integer32
_FutOspfType11LsaCksumSum_Object = MibScalar
futOspfType11LsaCksumSum = _FutOspfType11LsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 1, 3),
    _FutOspfType11LsaCksumSum_Type()
)
futOspfType11LsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsaCksumSum.setStatus("current")


class _FutOspfAreaIDValid_Type(TruthValue):
    """Custom type futOspfAreaIDValid based on TruthValue"""
    defaultValue = 2


_FutOspfAreaIDValid_Type.__name__ = "TruthValue"
_FutOspfAreaIDValid_Object = MibScalar
futOspfAreaIDValid = _FutOspfAreaIDValid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 1, 4),
    _FutOspfAreaIDValid_Type()
)
futOspfAreaIDValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfAreaIDValid.setStatus("current")
_FutOspfOpaqueInterfaceTable_Object = MibTable
futOspfOpaqueInterfaceTable = _FutOspfOpaqueInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 2)
)
if mibBuilder.loadTexts:
    futOspfOpaqueInterfaceTable.setStatus("current")
_FutOspfOpaqueInterfaceEntry_Object = MibTableRow
futOspfOpaqueInterfaceEntry = _FutOspfOpaqueInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 2, 1)
)
if mibBuilder.loadTexts:
    futOspfOpaqueInterfaceEntry.setStatus("current")
_FutOspfOpaqueType9LsaCount_Type = Gauge32
_FutOspfOpaqueType9LsaCount_Object = MibTableColumn
futOspfOpaqueType9LsaCount = _FutOspfOpaqueType9LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 2, 1, 1),
    _FutOspfOpaqueType9LsaCount_Type()
)
futOspfOpaqueType9LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfOpaqueType9LsaCount.setStatus("current")


class _FutOspfOpaqueType9LsaCksumSum_Type(Integer32):
    """Custom type futOspfOpaqueType9LsaCksumSum based on Integer32"""
    defaultValue = 0


_FutOspfOpaqueType9LsaCksumSum_Type.__name__ = "Integer32"
_FutOspfOpaqueType9LsaCksumSum_Object = MibTableColumn
futOspfOpaqueType9LsaCksumSum = _FutOspfOpaqueType9LsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 2, 1, 2),
    _FutOspfOpaqueType9LsaCksumSum_Type()
)
futOspfOpaqueType9LsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfOpaqueType9LsaCksumSum.setStatus("current")
_FutOspfType9LsdbTable_Object = MibTable
futOspfType9LsdbTable = _FutOspfType9LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3)
)
if mibBuilder.loadTexts:
    futOspfType9LsdbTable.setStatus("current")
_FutOspfType9LsdbEntry_Object = MibTableRow
futOspfType9LsdbEntry = _FutOspfType9LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1)
)
futOspfType9LsdbEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType9LsdbIfIpAddress"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType9LsdbOpaqueType"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType9LsdbLsid"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType9LsdbRouterId"),
)
if mibBuilder.loadTexts:
    futOspfType9LsdbEntry.setStatus("current")
_FutOspfType9LsdbIfIpAddress_Type = IpAddress
_FutOspfType9LsdbIfIpAddress_Object = MibTableColumn
futOspfType9LsdbIfIpAddress = _FutOspfType9LsdbIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 1),
    _FutOspfType9LsdbIfIpAddress_Type()
)
futOspfType9LsdbIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType9LsdbIfIpAddress.setStatus("current")


class _FutOspfType9LsdbOpaqueType_Type(Integer32):
    """Custom type futOspfType9LsdbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FutOspfType9LsdbOpaqueType_Type.__name__ = "Integer32"
_FutOspfType9LsdbOpaqueType_Object = MibTableColumn
futOspfType9LsdbOpaqueType = _FutOspfType9LsdbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 2),
    _FutOspfType9LsdbOpaqueType_Type()
)
futOspfType9LsdbOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType9LsdbOpaqueType.setStatus("current")
_FutOspfType9LsdbLsid_Type = IpAddress
_FutOspfType9LsdbLsid_Object = MibTableColumn
futOspfType9LsdbLsid = _FutOspfType9LsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 3),
    _FutOspfType9LsdbLsid_Type()
)
futOspfType9LsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType9LsdbLsid.setStatus("current")
_FutOspfType9LsdbRouterId_Type = RouterID
_FutOspfType9LsdbRouterId_Object = MibTableColumn
futOspfType9LsdbRouterId = _FutOspfType9LsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 4),
    _FutOspfType9LsdbRouterId_Type()
)
futOspfType9LsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType9LsdbRouterId.setStatus("current")
_FutOspfType9LsdbSequence_Type = Integer32
_FutOspfType9LsdbSequence_Object = MibTableColumn
futOspfType9LsdbSequence = _FutOspfType9LsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 5),
    _FutOspfType9LsdbSequence_Type()
)
futOspfType9LsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType9LsdbSequence.setStatus("current")
_FutOspfType9LsdbAge_Type = Integer32
_FutOspfType9LsdbAge_Object = MibTableColumn
futOspfType9LsdbAge = _FutOspfType9LsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 6),
    _FutOspfType9LsdbAge_Type()
)
futOspfType9LsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType9LsdbAge.setStatus("current")
_FutOspfType9LsdbChecksum_Type = Integer32
_FutOspfType9LsdbChecksum_Object = MibTableColumn
futOspfType9LsdbChecksum = _FutOspfType9LsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 7),
    _FutOspfType9LsdbChecksum_Type()
)
futOspfType9LsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType9LsdbChecksum.setStatus("current")


class _FutOspfType9LsdbAdvertisement_Type(OctetString):
    """Custom type futOspfType9LsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FutOspfType9LsdbAdvertisement_Type.__name__ = "OctetString"
_FutOspfType9LsdbAdvertisement_Object = MibTableColumn
futOspfType9LsdbAdvertisement = _FutOspfType9LsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 3, 1, 8),
    _FutOspfType9LsdbAdvertisement_Type()
)
futOspfType9LsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType9LsdbAdvertisement.setStatus("current")
_FutOspfType11LsdbTable_Object = MibTable
futOspfType11LsdbTable = _FutOspfType11LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4)
)
if mibBuilder.loadTexts:
    futOspfType11LsdbTable.setStatus("current")
_FutOspfType11LsdbEntry_Object = MibTableRow
futOspfType11LsdbEntry = _FutOspfType11LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1)
)
futOspfType11LsdbEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType11LsdbOpaqueType"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType11LsdbLsid"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfType11LsdbRouterId"),
)
if mibBuilder.loadTexts:
    futOspfType11LsdbEntry.setStatus("current")


class _FutOspfType11LsdbOpaqueType_Type(Integer32):
    """Custom type futOspfType11LsdbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FutOspfType11LsdbOpaqueType_Type.__name__ = "Integer32"
_FutOspfType11LsdbOpaqueType_Object = MibTableColumn
futOspfType11LsdbOpaqueType = _FutOspfType11LsdbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 1),
    _FutOspfType11LsdbOpaqueType_Type()
)
futOspfType11LsdbOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType11LsdbOpaqueType.setStatus("current")
_FutOspfType11LsdbLsid_Type = IpAddress
_FutOspfType11LsdbLsid_Object = MibTableColumn
futOspfType11LsdbLsid = _FutOspfType11LsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 2),
    _FutOspfType11LsdbLsid_Type()
)
futOspfType11LsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType11LsdbLsid.setStatus("current")
_FutOspfType11LsdbRouterId_Type = RouterID
_FutOspfType11LsdbRouterId_Object = MibTableColumn
futOspfType11LsdbRouterId = _FutOspfType11LsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 3),
    _FutOspfType11LsdbRouterId_Type()
)
futOspfType11LsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfType11LsdbRouterId.setStatus("current")
_FutOspfType11LsdbSequence_Type = Integer32
_FutOspfType11LsdbSequence_Object = MibTableColumn
futOspfType11LsdbSequence = _FutOspfType11LsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 4),
    _FutOspfType11LsdbSequence_Type()
)
futOspfType11LsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsdbSequence.setStatus("current")
_FutOspfType11LsdbAge_Type = Integer32
_FutOspfType11LsdbAge_Object = MibTableColumn
futOspfType11LsdbAge = _FutOspfType11LsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 5),
    _FutOspfType11LsdbAge_Type()
)
futOspfType11LsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsdbAge.setStatus("current")
_FutOspfType11LsdbChecksum_Type = Integer32
_FutOspfType11LsdbChecksum_Object = MibTableColumn
futOspfType11LsdbChecksum = _FutOspfType11LsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 6),
    _FutOspfType11LsdbChecksum_Type()
)
futOspfType11LsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsdbChecksum.setStatus("current")


class _FutOspfType11LsdbAdvertisement_Type(OctetString):
    """Custom type futOspfType11LsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FutOspfType11LsdbAdvertisement_Type.__name__ = "OctetString"
_FutOspfType11LsdbAdvertisement_Object = MibTableColumn
futOspfType11LsdbAdvertisement = _FutOspfType11LsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 4, 1, 7),
    _FutOspfType11LsdbAdvertisement_Type()
)
futOspfType11LsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfType11LsdbAdvertisement.setStatus("current")
_FutOspfAppInfoDbTable_Object = MibTable
futOspfAppInfoDbTable = _FutOspfAppInfoDbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5)
)
if mibBuilder.loadTexts:
    futOspfAppInfoDbTable.setStatus("current")
_FutOspfAppInfoDbEntry_Object = MibTableRow
futOspfAppInfoDbEntry = _FutOspfAppInfoDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1)
)
futOspfAppInfoDbEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfAppInfoDbAppid"),
)
if mibBuilder.loadTexts:
    futOspfAppInfoDbEntry.setStatus("current")


class _FutOspfAppInfoDbAppid_Type(Integer32):
    """Custom type futOspfAppInfoDbAppid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FutOspfAppInfoDbAppid_Type.__name__ = "Integer32"
_FutOspfAppInfoDbAppid_Object = MibTableColumn
futOspfAppInfoDbAppid = _FutOspfAppInfoDbAppid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 1),
    _FutOspfAppInfoDbAppid_Type()
)
futOspfAppInfoDbAppid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfAppInfoDbAppid.setStatus("current")


class _FutOspfAppInfoDbOpaqueType_Type(Integer32):
    """Custom type futOspfAppInfoDbOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfAppInfoDbOpaqueType_Type.__name__ = "Integer32"
_FutOspfAppInfoDbOpaqueType_Object = MibTableColumn
futOspfAppInfoDbOpaqueType = _FutOspfAppInfoDbOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 2),
    _FutOspfAppInfoDbOpaqueType_Type()
)
futOspfAppInfoDbOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbOpaqueType.setStatus("current")


class _FutOspfAppInfoDbLsaTypesSupported_Type(Integer32):
    """Custom type futOspfAppInfoDbLsaTypesSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FutOspfAppInfoDbLsaTypesSupported_Type.__name__ = "Integer32"
_FutOspfAppInfoDbLsaTypesSupported_Object = MibTableColumn
futOspfAppInfoDbLsaTypesSupported = _FutOspfAppInfoDbLsaTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 3),
    _FutOspfAppInfoDbLsaTypesSupported_Type()
)
futOspfAppInfoDbLsaTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbLsaTypesSupported.setStatus("current")
_FutOspfAppInfoDbType9Gen_Type = Counter32
_FutOspfAppInfoDbType9Gen_Object = MibTableColumn
futOspfAppInfoDbType9Gen = _FutOspfAppInfoDbType9Gen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 4),
    _FutOspfAppInfoDbType9Gen_Type()
)
futOspfAppInfoDbType9Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType9Gen.setStatus("current")
_FutOspfAppInfoDbType9Rcvd_Type = Counter32
_FutOspfAppInfoDbType9Rcvd_Object = MibTableColumn
futOspfAppInfoDbType9Rcvd = _FutOspfAppInfoDbType9Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 5),
    _FutOspfAppInfoDbType9Rcvd_Type()
)
futOspfAppInfoDbType9Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType9Rcvd.setStatus("current")
_FutOspfAppInfoDbType10Gen_Type = Counter32
_FutOspfAppInfoDbType10Gen_Object = MibTableColumn
futOspfAppInfoDbType10Gen = _FutOspfAppInfoDbType10Gen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 6),
    _FutOspfAppInfoDbType10Gen_Type()
)
futOspfAppInfoDbType10Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType10Gen.setStatus("current")
_FutOspfAppInfoDbType10Rcvd_Type = Counter32
_FutOspfAppInfoDbType10Rcvd_Object = MibTableColumn
futOspfAppInfoDbType10Rcvd = _FutOspfAppInfoDbType10Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 7),
    _FutOspfAppInfoDbType10Rcvd_Type()
)
futOspfAppInfoDbType10Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType10Rcvd.setStatus("current")
_FutOspfAppInfoDbType11Gen_Type = Counter32
_FutOspfAppInfoDbType11Gen_Object = MibTableColumn
futOspfAppInfoDbType11Gen = _FutOspfAppInfoDbType11Gen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 8),
    _FutOspfAppInfoDbType11Gen_Type()
)
futOspfAppInfoDbType11Gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType11Gen.setStatus("current")
_FutOspfAppInfoDbType11Rcvd_Type = Counter32
_FutOspfAppInfoDbType11Rcvd_Object = MibTableColumn
futOspfAppInfoDbType11Rcvd = _FutOspfAppInfoDbType11Rcvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 12, 5, 1, 9),
    _FutOspfAppInfoDbType11Rcvd_Type()
)
futOspfAppInfoDbType11Rcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfAppInfoDbType11Rcvd.setStatus("current")
_FutospfRRDGroup_ObjectIdentity = ObjectIdentity
futospfRRDGroup = _FutospfRRDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13)
)
_FutospfRRDGeneralGroup_ObjectIdentity = ObjectIdentity
futospfRRDGeneralGroup = _FutospfRRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 1)
)


class _FutOspfRRDStatus_Type(Status):
    """Custom type futOspfRRDStatus based on Status"""
    defaultValue = 2


_FutOspfRRDStatus_Type.__name__ = "Status"
_FutOspfRRDStatus_Object = MibScalar
futOspfRRDStatus = _FutOspfRRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 1, 1),
    _FutOspfRRDStatus_Type()
)
futOspfRRDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDStatus.setStatus("current")


class _FutOspfRRDSrcProtoMaskEnable_Type(Integer32):
    """Custom type futOspfRRDSrcProtoMaskEnable based on Integer32"""
    defaultValue = 0


_FutOspfRRDSrcProtoMaskEnable_Type.__name__ = "Integer32"
_FutOspfRRDSrcProtoMaskEnable_Object = MibScalar
futOspfRRDSrcProtoMaskEnable = _FutOspfRRDSrcProtoMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 1, 2),
    _FutOspfRRDSrcProtoMaskEnable_Type()
)
futOspfRRDSrcProtoMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDSrcProtoMaskEnable.setStatus("current")


class _FutOspfRRDSrcProtoMaskDisable_Type(Integer32):
    """Custom type futOspfRRDSrcProtoMaskDisable based on Integer32"""
    defaultValue = 587478


_FutOspfRRDSrcProtoMaskDisable_Type.__name__ = "Integer32"
_FutOspfRRDSrcProtoMaskDisable_Object = MibScalar
futOspfRRDSrcProtoMaskDisable = _FutOspfRRDSrcProtoMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 1, 3),
    _FutOspfRRDSrcProtoMaskDisable_Type()
)
futOspfRRDSrcProtoMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDSrcProtoMaskDisable.setStatus("current")


class _FutOspfRRDRouteMapEnable_Type(DisplayString):
    """Custom type futOspfRRDRouteMapEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FutOspfRRDRouteMapEnable_Type.__name__ = "DisplayString"
_FutOspfRRDRouteMapEnable_Object = MibScalar
futOspfRRDRouteMapEnable = _FutOspfRRDRouteMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 1, 4),
    _FutOspfRRDRouteMapEnable_Type()
)
futOspfRRDRouteMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDRouteMapEnable.setStatus("current")
_FutOspfRRDRouteConfigTable_Object = MibTable
futOspfRRDRouteConfigTable = _FutOspfRRDRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2)
)
if mibBuilder.loadTexts:
    futOspfRRDRouteConfigTable.setStatus("current")
_FutOspfRRDRouteConfigEntry_Object = MibTableRow
futOspfRRDRouteConfigEntry = _FutOspfRRDRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1)
)
futOspfRRDRouteConfigEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRRDRouteDest"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfRRDRouteMask"),
)
if mibBuilder.loadTexts:
    futOspfRRDRouteConfigEntry.setStatus("current")
_FutOspfRRDRouteDest_Type = IpAddress
_FutOspfRRDRouteDest_Object = MibTableColumn
futOspfRRDRouteDest = _FutOspfRRDRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 1),
    _FutOspfRRDRouteDest_Type()
)
futOspfRRDRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRRDRouteDest.setStatus("current")
_FutOspfRRDRouteMask_Type = IpAddress
_FutOspfRRDRouteMask_Object = MibTableColumn
futOspfRRDRouteMask = _FutOspfRRDRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 2),
    _FutOspfRRDRouteMask_Type()
)
futOspfRRDRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfRRDRouteMask.setStatus("current")


class _FutOspfRRDRouteMetric_Type(BigMetric):
    """Custom type futOspfRRDRouteMetric based on BigMetric"""
    defaultValue = 10


_FutOspfRRDRouteMetric_Type.__name__ = "BigMetric"
_FutOspfRRDRouteMetric_Object = MibTableColumn
futOspfRRDRouteMetric = _FutOspfRRDRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 3),
    _FutOspfRRDRouteMetric_Type()
)
futOspfRRDRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDRouteMetric.setStatus("current")


class _FutOspfRRDRouteMetricType_Type(Integer32):
    """Custom type futOspfRRDRouteMetricType based on Integer32"""
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


_FutOspfRRDRouteMetricType_Type.__name__ = "Integer32"
_FutOspfRRDRouteMetricType_Object = MibTableColumn
futOspfRRDRouteMetricType = _FutOspfRRDRouteMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 4),
    _FutOspfRRDRouteMetricType_Type()
)
futOspfRRDRouteMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDRouteMetricType.setStatus("current")


class _FutOspfRRDRouteTagType_Type(Integer32):
    """Custom type futOspfRRDRouteTagType based on Integer32"""
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


_FutOspfRRDRouteTagType_Type.__name__ = "Integer32"
_FutOspfRRDRouteTagType_Object = MibTableColumn
futOspfRRDRouteTagType = _FutOspfRRDRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 5),
    _FutOspfRRDRouteTagType_Type()
)
futOspfRRDRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDRouteTagType.setStatus("current")


class _FutOspfRRDRouteTag_Type(Unsigned32):
    """Custom type futOspfRRDRouteTag based on Unsigned32"""
    defaultValue = 0


_FutOspfRRDRouteTag_Type.__name__ = "Unsigned32"
_FutOspfRRDRouteTag_Object = MibTableColumn
futOspfRRDRouteTag = _FutOspfRRDRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 6),
    _FutOspfRRDRouteTag_Type()
)
futOspfRRDRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfRRDRouteTag.setStatus("current")
_FutOspfRRDRouteStatus_Type = RowStatus
_FutOspfRRDRouteStatus_Object = MibTableColumn
futOspfRRDRouteStatus = _FutOspfRRDRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 13, 2, 1, 7),
    _FutOspfRRDRouteStatus_Type()
)
futOspfRRDRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futOspfRRDRouteStatus.setStatus("current")
_FutOspfVirtNbrTable_Object = MibTable
futOspfVirtNbrTable = _FutOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 14)
)
if mibBuilder.loadTexts:
    futOspfVirtNbrTable.setStatus("current")
_FutOspfVirtNbrEntry_Object = MibTableRow
futOspfVirtNbrEntry = _FutOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 14, 1)
)
if mibBuilder.loadTexts:
    futOspfVirtNbrEntry.setStatus("current")


class _FutOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type futOspfVirtNbrRestartHelperStatus based on Integer32"""
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


_FutOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_FutOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
futOspfVirtNbrRestartHelperStatus = _FutOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 14, 1, 1),
    _FutOspfVirtNbrRestartHelperStatus_Type()
)
futOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfVirtNbrRestartHelperStatus.setStatus("current")
_FutOspfVirtNbrRestartHelperAge_Type = Unsigned32
_FutOspfVirtNbrRestartHelperAge_Object = MibTableColumn
futOspfVirtNbrRestartHelperAge = _FutOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 14, 1, 2),
    _FutOspfVirtNbrRestartHelperAge_Type()
)
futOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    futOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _FutOspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type futOspfVirtNbrRestartHelperExitReason based on Integer32"""
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


_FutOspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_FutOspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
futOspfVirtNbrRestartHelperExitReason = _FutOspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 14, 1, 3),
    _FutOspfVirtNbrRestartHelperExitReason_Type()
)
futOspfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfVirtNbrRestartHelperExitReason.setStatus("current")
_FutospfDistInOutRouteMap_ObjectIdentity = ObjectIdentity
futospfDistInOutRouteMap = _FutospfDistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15)
)
_FutOspfDistInOutRouteMapTable_Object = MibTable
futOspfDistInOutRouteMapTable = _FutOspfDistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1)
)
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapTable.setStatus("current")
_FutOspfDistInOutRouteMapEntry_Object = MibTableRow
futOspfDistInOutRouteMapEntry = _FutOspfDistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1, 1)
)
futOspfDistInOutRouteMapEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfDistInOutRouteMapName"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfDistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapEntry.setStatus("current")


class _FutOspfDistInOutRouteMapName_Type(DisplayString):
    """Custom type futOspfDistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FutOspfDistInOutRouteMapName_Type.__name__ = "DisplayString"
_FutOspfDistInOutRouteMapName_Object = MibTableColumn
futOspfDistInOutRouteMapName = _FutOspfDistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1, 1, 1),
    _FutOspfDistInOutRouteMapName_Type()
)
futOspfDistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapName.setStatus("current")


class _FutOspfDistInOutRouteMapType_Type(Integer32):
    """Custom type futOspfDistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FutOspfDistInOutRouteMapType_Type.__name__ = "Integer32"
_FutOspfDistInOutRouteMapType_Object = MibTableColumn
futOspfDistInOutRouteMapType = _FutOspfDistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1, 1, 3),
    _FutOspfDistInOutRouteMapType_Type()
)
futOspfDistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapType.setStatus("current")


class _FutOspfDistInOutRouteMapValue_Type(Integer32):
    """Custom type futOspfDistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FutOspfDistInOutRouteMapValue_Type.__name__ = "Integer32"
_FutOspfDistInOutRouteMapValue_Object = MibTableColumn
futOspfDistInOutRouteMapValue = _FutOspfDistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1, 1, 4),
    _FutOspfDistInOutRouteMapValue_Type()
)
futOspfDistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapValue.setStatus("current")
_FutOspfDistInOutRouteMapRowStatus_Type = RowStatus
_FutOspfDistInOutRouteMapRowStatus_Object = MibTableColumn
futOspfDistInOutRouteMapRowStatus = _FutOspfDistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 15, 1, 1, 5),
    _FutOspfDistInOutRouteMapRowStatus_Type()
)
futOspfDistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfDistInOutRouteMapRowStatus.setStatus("current")
_FutospfPreferenceGroup_ObjectIdentity = ObjectIdentity
futospfPreferenceGroup = _FutospfPreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 16)
)


class _FutOspfPreferenceValue_Type(Integer32):
    """Custom type futOspfPreferenceValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfPreferenceValue_Type.__name__ = "Integer32"
_FutOspfPreferenceValue_Object = MibScalar
futOspfPreferenceValue = _FutOspfPreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 16, 1),
    _FutOspfPreferenceValue_Type()
)
futOspfPreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfPreferenceValue.setStatus("current")
_FutOspfIfAuthTable_Object = MibTable
futOspfIfAuthTable = _FutOspfIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17)
)
if mibBuilder.loadTexts:
    futOspfIfAuthTable.setStatus("current")
_FutOspfIfAuthEntry_Object = MibTableRow
futOspfIfAuthEntry = _FutOspfIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1)
)
futOspfIfAuthEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfAuthIpAddress"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfAuthAddressLessIf"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfIfAuthKeyId"),
)
if mibBuilder.loadTexts:
    futOspfIfAuthEntry.setStatus("current")
_FutOspfIfAuthIpAddress_Type = IpAddress
_FutOspfIfAuthIpAddress_Object = MibTableColumn
futOspfIfAuthIpAddress = _FutOspfIfAuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 1),
    _FutOspfIfAuthIpAddress_Type()
)
futOspfIfAuthIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfAuthIpAddress.setStatus("current")


class _FutOspfIfAuthAddressLessIf_Type(InterfaceIndex):
    """Custom type futOspfIfAuthAddressLessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FutOspfIfAuthAddressLessIf_Type.__name__ = "InterfaceIndex"
_FutOspfIfAuthAddressLessIf_Object = MibTableColumn
futOspfIfAuthAddressLessIf = _FutOspfIfAuthAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 2),
    _FutOspfIfAuthAddressLessIf_Type()
)
futOspfIfAuthAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfAuthAddressLessIf.setStatus("current")


class _FutOspfIfAuthKeyId_Type(Integer32):
    """Custom type futOspfIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfIfAuthKeyId_Type.__name__ = "Integer32"
_FutOspfIfAuthKeyId_Object = MibTableColumn
futOspfIfAuthKeyId = _FutOspfIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 3),
    _FutOspfIfAuthKeyId_Type()
)
futOspfIfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyId.setStatus("current")


class _FutOspfIfAuthKey_Type(OctetString):
    """Custom type futOspfIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FutOspfIfAuthKey_Type.__name__ = "OctetString"
_FutOspfIfAuthKey_Object = MibTableColumn
futOspfIfAuthKey = _FutOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 4),
    _FutOspfIfAuthKey_Type()
)
futOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKey.setStatus("current")
_FutOspfIfAuthKeyStartAccept_Type = DateAndTime
_FutOspfIfAuthKeyStartAccept_Object = MibTableColumn
futOspfIfAuthKeyStartAccept = _FutOspfIfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 5),
    _FutOspfIfAuthKeyStartAccept_Type()
)
futOspfIfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyStartAccept.setStatus("current")
_FutOspfIfAuthKeyStartGenerate_Type = DateAndTime
_FutOspfIfAuthKeyStartGenerate_Object = MibTableColumn
futOspfIfAuthKeyStartGenerate = _FutOspfIfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 6),
    _FutOspfIfAuthKeyStartGenerate_Type()
)
futOspfIfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyStartGenerate.setStatus("current")
_FutOspfIfAuthKeyStopGenerate_Type = DateAndTime
_FutOspfIfAuthKeyStopGenerate_Object = MibTableColumn
futOspfIfAuthKeyStopGenerate = _FutOspfIfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 7),
    _FutOspfIfAuthKeyStopGenerate_Type()
)
futOspfIfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyStopGenerate.setStatus("current")
_FutOspfIfAuthKeyStopAccept_Type = DateAndTime
_FutOspfIfAuthKeyStopAccept_Object = MibTableColumn
futOspfIfAuthKeyStopAccept = _FutOspfIfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 8),
    _FutOspfIfAuthKeyStopAccept_Type()
)
futOspfIfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyStopAccept.setStatus("current")


class _FutOspfIfAuthKeyStatus_Type(Integer32):
    """Custom type futOspfIfAuthKeyStatus based on Integer32"""
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


_FutOspfIfAuthKeyStatus_Type.__name__ = "Integer32"
_FutOspfIfAuthKeyStatus_Object = MibTableColumn
futOspfIfAuthKeyStatus = _FutOspfIfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 17, 1, 9),
    _FutOspfIfAuthKeyStatus_Type()
)
futOspfIfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfAuthKeyStatus.setStatus("current")
_FutOspfVirtIfAuthTable_Object = MibTable
futOspfVirtIfAuthTable = _FutOspfVirtIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18)
)
if mibBuilder.loadTexts:
    futOspfVirtIfAuthTable.setStatus("current")
_FutOspfVirtIfAuthEntry_Object = MibTableRow
futOspfVirtIfAuthEntry = _FutOspfVirtIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1)
)
futOspfVirtIfAuthEntry.setIndexNames(
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfAuthAreaId"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfAuthNeighbor"),
    (0, "FUTURESOFT-OSPF-MIB", "futOspfVirtIfAuthKeyId"),
)
if mibBuilder.loadTexts:
    futOspfVirtIfAuthEntry.setStatus("current")
_FutOspfVirtIfAuthAreaId_Type = AreaID
_FutOspfVirtIfAuthAreaId_Object = MibTableColumn
futOspfVirtIfAuthAreaId = _FutOspfVirtIfAuthAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 1),
    _FutOspfVirtIfAuthAreaId_Type()
)
futOspfVirtIfAuthAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthAreaId.setStatus("current")
_FutOspfVirtIfAuthNeighbor_Type = RouterID
_FutOspfVirtIfAuthNeighbor_Object = MibTableColumn
futOspfVirtIfAuthNeighbor = _FutOspfVirtIfAuthNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 2),
    _FutOspfVirtIfAuthNeighbor_Type()
)
futOspfVirtIfAuthNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthNeighbor.setStatus("current")


class _FutOspfVirtIfAuthKeyId_Type(Integer32):
    """Custom type futOspfVirtIfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FutOspfVirtIfAuthKeyId_Type.__name__ = "Integer32"
_FutOspfVirtIfAuthKeyId_Object = MibTableColumn
futOspfVirtIfAuthKeyId = _FutOspfVirtIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 3),
    _FutOspfVirtIfAuthKeyId_Type()
)
futOspfVirtIfAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyId.setStatus("current")


class _FutOspfVirtIfAuthKey_Type(OctetString):
    """Custom type futOspfVirtIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FutOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_FutOspfVirtIfAuthKey_Object = MibTableColumn
futOspfVirtIfAuthKey = _FutOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 4),
    _FutOspfVirtIfAuthKey_Type()
)
futOspfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKey.setStatus("current")
_FutOspfVirtIfAuthKeyStartAccept_Type = DateAndTime
_FutOspfVirtIfAuthKeyStartAccept_Object = MibTableColumn
futOspfVirtIfAuthKeyStartAccept = _FutOspfVirtIfAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 5),
    _FutOspfVirtIfAuthKeyStartAccept_Type()
)
futOspfVirtIfAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyStartAccept.setStatus("current")
_FutOspfVirtIfAuthKeyStartGenerate_Type = DateAndTime
_FutOspfVirtIfAuthKeyStartGenerate_Object = MibTableColumn
futOspfVirtIfAuthKeyStartGenerate = _FutOspfVirtIfAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 6),
    _FutOspfVirtIfAuthKeyStartGenerate_Type()
)
futOspfVirtIfAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyStartGenerate.setStatus("current")
_FutOspfVirtIfAuthKeyStopGenerate_Type = DateAndTime
_FutOspfVirtIfAuthKeyStopGenerate_Object = MibTableColumn
futOspfVirtIfAuthKeyStopGenerate = _FutOspfVirtIfAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 7),
    _FutOspfVirtIfAuthKeyStopGenerate_Type()
)
futOspfVirtIfAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyStopGenerate.setStatus("current")
_FutOspfVirtIfAuthKeyStopAccept_Type = DateAndTime
_FutOspfVirtIfAuthKeyStopAccept_Object = MibTableColumn
futOspfVirtIfAuthKeyStopAccept = _FutOspfVirtIfAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 8),
    _FutOspfVirtIfAuthKeyStopAccept_Type()
)
futOspfVirtIfAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyStopAccept.setStatus("current")


class _FutOspfVirtIfAuthKeyStatus_Type(Integer32):
    """Custom type futOspfVirtIfAuthKeyStatus based on Integer32"""
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


_FutOspfVirtIfAuthKeyStatus_Type.__name__ = "Integer32"
_FutOspfVirtIfAuthKeyStatus_Object = MibTableColumn
futOspfVirtIfAuthKeyStatus = _FutOspfVirtIfAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 18, 1, 9),
    _FutOspfVirtIfAuthKeyStatus_Type()
)
futOspfVirtIfAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfAuthKeyStatus.setStatus("current")
_FutOspfIfCryptoAuthTable_Object = MibTable
futOspfIfCryptoAuthTable = _FutOspfIfCryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 19)
)
if mibBuilder.loadTexts:
    futOspfIfCryptoAuthTable.setStatus("current")
_FutOspfIfCryptoAuthEntry_Object = MibTableRow
futOspfIfCryptoAuthEntry = _FutOspfIfCryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 19, 1)
)
if mibBuilder.loadTexts:
    futOspfIfCryptoAuthEntry.setStatus("current")


class _FutOspfIfCryptoAuthType_Type(Integer32):
    """Custom type futOspfIfCryptoAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2),
          ("sha224", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6))
    )


_FutOspfIfCryptoAuthType_Type.__name__ = "Integer32"
_FutOspfIfCryptoAuthType_Object = MibTableColumn
futOspfIfCryptoAuthType = _FutOspfIfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 19, 1, 1),
    _FutOspfIfCryptoAuthType_Type()
)
futOspfIfCryptoAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfIfCryptoAuthType.setStatus("current")
_FutOspfVirtIfCryptoAuthTable_Object = MibTable
futOspfVirtIfCryptoAuthTable = _FutOspfVirtIfCryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 20)
)
if mibBuilder.loadTexts:
    futOspfVirtIfCryptoAuthTable.setStatus("current")
_FutOspfVirtIfCryptoAuthEntry_Object = MibTableRow
futOspfVirtIfCryptoAuthEntry = _FutOspfVirtIfCryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 20, 1)
)
if mibBuilder.loadTexts:
    futOspfVirtIfCryptoAuthEntry.setStatus("current")


class _FutOspfVirtIfCryptoAuthType_Type(Integer32):
    """Custom type futOspfVirtIfCryptoAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2),
          ("sha224", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6))
    )


_FutOspfVirtIfCryptoAuthType_Type.__name__ = "Integer32"
_FutOspfVirtIfCryptoAuthType_Object = MibTableColumn
futOspfVirtIfCryptoAuthType = _FutOspfVirtIfCryptoAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 10, 20, 1, 1),
    _FutOspfVirtIfCryptoAuthType_Type()
)
futOspfVirtIfCryptoAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfVirtIfCryptoAuthType.setStatus("current")
_FutOspfTestGroup_ObjectIdentity = ObjectIdentity
futOspfTestGroup = _FutOspfTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 100)
)
_FutOspfNotification_ObjectIdentity = ObjectIdentity
futOspfNotification = _FutOspfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101)
)
_FutOspfTraps_ObjectIdentity = ObjectIdentity
futOspfTraps = _FutOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101, 0)
)
_FutOspfOasGroup_ObjectIdentity = ObjectIdentity
futOspfOasGroup = _FutOspfOasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 10, 102)
)
futOspfIfEntry.registerAugmentions(
    ("FUTURESOFT-OSPF-MIB",
     "futOspfOpaqueInterfaceEntry")
)
futOspfOpaqueInterfaceEntry.setIndexNames(*futOspfIfEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions(
    ("FUTURESOFT-OSPF-MIB",
     "futOspfVirtNbrEntry")
)
futOspfVirtNbrEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("FUTURESOFT-OSPF-MIB",
     "futOspfIfCryptoAuthEntry")
)
futOspfIfCryptoAuthEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("FUTURESOFT-OSPF-MIB",
     "futOspfVirtIfCryptoAuthEntry")
)
futOspfVirtIfCryptoAuthEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects

futOspfRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101, 0, 1)
)
futOspfRestartStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("FUTURESOFT-OSPF-MIB", "futOspfRestartStatus"),
        ("FUTURESOFT-OSPF-MIB", "futOspfRestartInterval"),
        ("FUTURESOFT-OSPF-MIB", "futOspfRestartExitReason"))
)
if mibBuilder.loadTexts:
    futOspfRestartStatusChange.setStatus(
        "current"
    )

futOspfNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101, 0, 2)
)
futOspfNbrRestartHelperStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("FUTURESOFT-OSPF-MIB", "futOspfNbrRestartHelperStatus"),
        ("FUTURESOFT-OSPF-MIB", "futOspfNbrRestartHelperAge"),
        ("FUTURESOFT-OSPF-MIB", "futOspfNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    futOspfNbrRestartHelperStatusChange.setStatus(
        "current"
    )

futOspfVirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101, 0, 3)
)
futOspfVirtNbrRestartHelperStatusChange.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("FUTURESOFT-OSPF-MIB", "futOspfVirtNbrRestartHelperStatus"),
        ("FUTURESOFT-OSPF-MIB", "futOspfVirtNbrRestartHelperAge"),
        ("FUTURESOFT-OSPF-MIB", "futOspfVirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    futOspfVirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )

futOspfHotStandbyEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 10, 101, 0, 4)
)
futOspfHotStandbyEventTrap.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("FUTURESOFT-OSPF-MIB", "futOspfHotStandbyState"),
        ("FUTURESOFT-OSPF-MIB", "futOspfDynamicBulkUpdStatus"))
)
if mibBuilder.loadTexts:
    futOspfHotStandbyEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUTURESOFT-OSPF-MIB",
    **{"futospf": futospf,
       "futospfGeneralGroup": futospfGeneralGroup,
       "futOspfOverFlowState": futOspfOverFlowState,
       "futOspfPktsRcvd": futOspfPktsRcvd,
       "futOspfPktsTxed": futOspfPktsTxed,
       "futOspfPktsDisd": futOspfPktsDisd,
       "futOspfRFC1583Compatibility": futOspfRFC1583Compatibility,
       "futOspfMaxAreas": futOspfMaxAreas,
       "futOspfMaxLSAperArea": futOspfMaxLSAperArea,
       "futOspfMaxExtLSAs": futOspfMaxExtLSAs,
       "futOspfMaxSelfOrgLSAs": futOspfMaxSelfOrgLSAs,
       "futOspfMaxRoutes": futOspfMaxRoutes,
       "futOspfMaxLsaSize": futOspfMaxLsaSize,
       "futOspfTraceLevel": futOspfTraceLevel,
       "futOspfMinLsaInterval": futOspfMinLsaInterval,
       "futOspfABRType": futOspfABRType,
       "futOspfNssaAsbrDefRtTrans": futOspfNssaAsbrDefRtTrans,
       "futOspfDefaultPassiveInterface": futOspfDefaultPassiveInterface,
       "futOspfSpfHoldtime": futOspfSpfHoldtime,
       "futOspfSpfDelay": futOspfSpfDelay,
       "futOspfRestartSupport": futOspfRestartSupport,
       "futOspfRestartInterval": futOspfRestartInterval,
       "futOspfRestartStrictLsaChecking": futOspfRestartStrictLsaChecking,
       "futOspfRestartStatus": futOspfRestartStatus,
       "futOspfRestartAge": futOspfRestartAge,
       "futOspfRestartExitReason": futOspfRestartExitReason,
       "futOspfHelperSupport": futOspfHelperSupport,
       "futOspfHelperGraceTimeLimit": futOspfHelperGraceTimeLimit,
       "futOspfRestartAckState": futOspfRestartAckState,
       "futOspfGraceLsaRetransmitCount": futOspfGraceLsaRetransmitCount,
       "futOspfRestartReason": futOspfRestartReason,
       "futOspfRTStaggeringInterval": futOspfRTStaggeringInterval,
       "futOspfRTStaggeringStatus": futOspfRTStaggeringStatus,
       "futOspfHotStandbyAdminStatus": futOspfHotStandbyAdminStatus,
       "futOspfHotStandbyState": futOspfHotStandbyState,
       "futOspfDynamicBulkUpdStatus": futOspfDynamicBulkUpdStatus,
       "futOspfStanbyHelloSyncCount": futOspfStanbyHelloSyncCount,
       "futOspfStanbyLsaSyncCount": futOspfStanbyLsaSyncCount,
       "futOspfExtTraceLevel": futOspfExtTraceLevel,
       "futospfRouterIdPermanence": futospfRouterIdPermanence,
       "futOspfBfdStatus": futOspfBfdStatus,
       "futOspfBfdAllIfState": futOspfBfdAllIfState,
       "futOspfAreaTable": futOspfAreaTable,
       "futOspfAreaEntry": futOspfAreaEntry,
       "futOspfAreaId": futOspfAreaId,
       "futOspfAreaIfCount": futOspfAreaIfCount,
       "futOspfAreaNetCount": futOspfAreaNetCount,
       "futOspfAreaRtrCount": futOspfAreaRtrCount,
       "futOspfAreaNSSATranslatorRole": futOspfAreaNSSATranslatorRole,
       "futOspfAreaNSSATranslatorState": futOspfAreaNSSATranslatorState,
       "futOspfAreaNSSATranslatorStabilityInterval": futOspfAreaNSSATranslatorStabilityInterval,
       "futOspfAreaNSSATranslatorEvents": futOspfAreaNSSATranslatorEvents,
       "futOspfAreaDfInfOriginate": futOspfAreaDfInfOriginate,
       "futOspfHostTable": futOspfHostTable,
       "futOspfHostEntry": futOspfHostEntry,
       "futOspfHostIpAddress": futOspfHostIpAddress,
       "futOspfHostTOS": futOspfHostTOS,
       "futOspfHostRouteIfIndex": futOspfHostRouteIfIndex,
       "futOspfIfTable": futOspfIfTable,
       "futOspfIfEntry": futOspfIfEntry,
       "futOspfIfIpAddress": futOspfIfIpAddress,
       "futOspfAddressLessIf": futOspfAddressLessIf,
       "futOspfIfOperState": futOspfIfOperState,
       "futOspfIfPassive": futOspfIfPassive,
       "futOspfIfNbrCount": futOspfIfNbrCount,
       "futOspfIfAdjCount": futOspfIfAdjCount,
       "futOspfIfHelloRcvd": futOspfIfHelloRcvd,
       "futOspfIfHelloTxed": futOspfIfHelloTxed,
       "futOspfIfHelloDisd": futOspfIfHelloDisd,
       "futOspfIfDdpRcvd": futOspfIfDdpRcvd,
       "futOspfIfDdpTxed": futOspfIfDdpTxed,
       "futOspfIfDdpDisd": futOspfIfDdpDisd,
       "futOspfIfLrqRcvd": futOspfIfLrqRcvd,
       "futOspfIfLrqTxed": futOspfIfLrqTxed,
       "futOspfIfLrqDisd": futOspfIfLrqDisd,
       "futOspfIfLsuRcvd": futOspfIfLsuRcvd,
       "futOspfIfLsuTxed": futOspfIfLsuTxed,
       "futOspfIfLsuDisd": futOspfIfLsuDisd,
       "futOspfIfLakRcvd": futOspfIfLakRcvd,
       "futOspfIfLakTxed": futOspfIfLakTxed,
       "futOspfIfLakDisd": futOspfIfLakDisd,
       "futOspfIfBfdState": futOspfIfBfdState,
       "futOspfIfMD5AuthTable": futOspfIfMD5AuthTable,
       "futOspfIfMD5AuthEntry": futOspfIfMD5AuthEntry,
       "futOspfIfMD5AuthIpAddress": futOspfIfMD5AuthIpAddress,
       "futOspfIfMD5AuthAddressLessIf": futOspfIfMD5AuthAddressLessIf,
       "futOspfIfMD5AuthKeyId": futOspfIfMD5AuthKeyId,
       "futOspfIfMD5AuthKey": futOspfIfMD5AuthKey,
       "futOspfIfMD5AuthKeyStartAccept": futOspfIfMD5AuthKeyStartAccept,
       "futOspfIfMD5AuthKeyStartGenerate": futOspfIfMD5AuthKeyStartGenerate,
       "futOspfIfMD5AuthKeyStopGenerate": futOspfIfMD5AuthKeyStopGenerate,
       "futOspfIfMD5AuthKeyStopAccept": futOspfIfMD5AuthKeyStopAccept,
       "futOspfIfMD5AuthKeyStatus": futOspfIfMD5AuthKeyStatus,
       "futOspfVirtIfMD5AuthTable": futOspfVirtIfMD5AuthTable,
       "futOspfVirtIfMD5AuthEntry": futOspfVirtIfMD5AuthEntry,
       "futOspfVirtIfMD5AuthAreaId": futOspfVirtIfMD5AuthAreaId,
       "futOspfVirtIfMD5AuthNeighbor": futOspfVirtIfMD5AuthNeighbor,
       "futOspfVirtIfMD5AuthKeyId": futOspfVirtIfMD5AuthKeyId,
       "futOspfVirtIfMD5AuthKey": futOspfVirtIfMD5AuthKey,
       "futOspfVirtIfMD5AuthKeyStartAccept": futOspfVirtIfMD5AuthKeyStartAccept,
       "futOspfVirtIfMD5AuthKeyStartGenerate": futOspfVirtIfMD5AuthKeyStartGenerate,
       "futOspfVirtIfMD5AuthKeyStopGenerate": futOspfVirtIfMD5AuthKeyStopGenerate,
       "futOspfVirtIfMD5AuthKeyStopAccept": futOspfVirtIfMD5AuthKeyStopAccept,
       "futOspfVirtIfMD5AuthKeyStatus": futOspfVirtIfMD5AuthKeyStatus,
       "futOspfNbrTable": futOspfNbrTable,
       "futOspfNbrEntry": futOspfNbrEntry,
       "futOspfNbrIpAddr": futOspfNbrIpAddr,
       "futOspfNbrAddressLessIndex": futOspfNbrAddressLessIndex,
       "futOspfNbrDBSummaryQLen": futOspfNbrDBSummaryQLen,
       "futOspfNbrLSReqQLen": futOspfNbrLSReqQLen,
       "futOspfNbrRestartHelperStatus": futOspfNbrRestartHelperStatus,
       "futOspfNbrRestartHelperAge": futOspfNbrRestartHelperAge,
       "futOspfNbrRestartHelperExitReason": futOspfNbrRestartHelperExitReason,
       "futOspfNbrBfdState": futOspfNbrBfdState,
       "futOspfRoutingTable": futOspfRoutingTable,
       "futOspfRoutingEntry": futOspfRoutingEntry,
       "futOspfRouteIpAddr": futOspfRouteIpAddr,
       "futOspfRouteIpAddrMask": futOspfRouteIpAddrMask,
       "futOspfRouteIpTos": futOspfRouteIpTos,
       "futOspfRouteIpNextHop": futOspfRouteIpNextHop,
       "futOspfRouteType": futOspfRouteType,
       "futOspfRouteAreaId": futOspfRouteAreaId,
       "futOspfRouteCost": futOspfRouteCost,
       "futOspfRouteType2Cost": futOspfRouteType2Cost,
       "futOspfRouteInterfaceIndex": futOspfRouteInterfaceIndex,
       "futOspfSecIfTable": futOspfSecIfTable,
       "futOspfSecIfEntry": futOspfSecIfEntry,
       "futOspfPrimIpAddr": futOspfPrimIpAddr,
       "futOspfPrimAddresslessIf": futOspfPrimAddresslessIf,
       "futOspfSecIpAddr": futOspfSecIpAddr,
       "futOspfSecIpAddrMask": futOspfSecIpAddrMask,
       "futOspfSecIfStatus": futOspfSecIfStatus,
       "futOspfAreaAggregateTable": futOspfAreaAggregateTable,
       "futOspfAreaAggregateEntry": futOspfAreaAggregateEntry,
       "futOspfAreaAggregateAreaID": futOspfAreaAggregateAreaID,
       "futOspfAreaAggregateLsdbType": futOspfAreaAggregateLsdbType,
       "futOspfAreaAggregateNet": futOspfAreaAggregateNet,
       "futOspfAreaAggregateMask": futOspfAreaAggregateMask,
       "futOspfAreaAggregateExternalTag": futOspfAreaAggregateExternalTag,
       "futOspfAsExternalAggregationTable": futOspfAsExternalAggregationTable,
       "futOspfAsExternalAggregationEntry": futOspfAsExternalAggregationEntry,
       "futOspfAsExternalAggregationNet": futOspfAsExternalAggregationNet,
       "futOspfAsExternalAggregationMask": futOspfAsExternalAggregationMask,
       "futOspfAsExternalAggregationAreaId": futOspfAsExternalAggregationAreaId,
       "futOspfAsExternalAggregationEffect": futOspfAsExternalAggregationEffect,
       "futOspfAsExternalAggregationTranslation": futOspfAsExternalAggregationTranslation,
       "futOspfAsExternalAggregationStatus": futOspfAsExternalAggregationStatus,
       "futOspfOpaqueLSAGroup": futOspfOpaqueLSAGroup,
       "futOspfOpaqueLSAGeneralGroup": futOspfOpaqueLSAGeneralGroup,
       "futOspfOpaqueOption": futOspfOpaqueOption,
       "futOspfType11LsaCount": futOspfType11LsaCount,
       "futOspfType11LsaCksumSum": futOspfType11LsaCksumSum,
       "futOspfAreaIDValid": futOspfAreaIDValid,
       "futOspfOpaqueInterfaceTable": futOspfOpaqueInterfaceTable,
       "futOspfOpaqueInterfaceEntry": futOspfOpaqueInterfaceEntry,
       "futOspfOpaqueType9LsaCount": futOspfOpaqueType9LsaCount,
       "futOspfOpaqueType9LsaCksumSum": futOspfOpaqueType9LsaCksumSum,
       "futOspfType9LsdbTable": futOspfType9LsdbTable,
       "futOspfType9LsdbEntry": futOspfType9LsdbEntry,
       "futOspfType9LsdbIfIpAddress": futOspfType9LsdbIfIpAddress,
       "futOspfType9LsdbOpaqueType": futOspfType9LsdbOpaqueType,
       "futOspfType9LsdbLsid": futOspfType9LsdbLsid,
       "futOspfType9LsdbRouterId": futOspfType9LsdbRouterId,
       "futOspfType9LsdbSequence": futOspfType9LsdbSequence,
       "futOspfType9LsdbAge": futOspfType9LsdbAge,
       "futOspfType9LsdbChecksum": futOspfType9LsdbChecksum,
       "futOspfType9LsdbAdvertisement": futOspfType9LsdbAdvertisement,
       "futOspfType11LsdbTable": futOspfType11LsdbTable,
       "futOspfType11LsdbEntry": futOspfType11LsdbEntry,
       "futOspfType11LsdbOpaqueType": futOspfType11LsdbOpaqueType,
       "futOspfType11LsdbLsid": futOspfType11LsdbLsid,
       "futOspfType11LsdbRouterId": futOspfType11LsdbRouterId,
       "futOspfType11LsdbSequence": futOspfType11LsdbSequence,
       "futOspfType11LsdbAge": futOspfType11LsdbAge,
       "futOspfType11LsdbChecksum": futOspfType11LsdbChecksum,
       "futOspfType11LsdbAdvertisement": futOspfType11LsdbAdvertisement,
       "futOspfAppInfoDbTable": futOspfAppInfoDbTable,
       "futOspfAppInfoDbEntry": futOspfAppInfoDbEntry,
       "futOspfAppInfoDbAppid": futOspfAppInfoDbAppid,
       "futOspfAppInfoDbOpaqueType": futOspfAppInfoDbOpaqueType,
       "futOspfAppInfoDbLsaTypesSupported": futOspfAppInfoDbLsaTypesSupported,
       "futOspfAppInfoDbType9Gen": futOspfAppInfoDbType9Gen,
       "futOspfAppInfoDbType9Rcvd": futOspfAppInfoDbType9Rcvd,
       "futOspfAppInfoDbType10Gen": futOspfAppInfoDbType10Gen,
       "futOspfAppInfoDbType10Rcvd": futOspfAppInfoDbType10Rcvd,
       "futOspfAppInfoDbType11Gen": futOspfAppInfoDbType11Gen,
       "futOspfAppInfoDbType11Rcvd": futOspfAppInfoDbType11Rcvd,
       "futospfRRDGroup": futospfRRDGroup,
       "futospfRRDGeneralGroup": futospfRRDGeneralGroup,
       "futOspfRRDStatus": futOspfRRDStatus,
       "futOspfRRDSrcProtoMaskEnable": futOspfRRDSrcProtoMaskEnable,
       "futOspfRRDSrcProtoMaskDisable": futOspfRRDSrcProtoMaskDisable,
       "futOspfRRDRouteMapEnable": futOspfRRDRouteMapEnable,
       "futOspfRRDRouteConfigTable": futOspfRRDRouteConfigTable,
       "futOspfRRDRouteConfigEntry": futOspfRRDRouteConfigEntry,
       "futOspfRRDRouteDest": futOspfRRDRouteDest,
       "futOspfRRDRouteMask": futOspfRRDRouteMask,
       "futOspfRRDRouteMetric": futOspfRRDRouteMetric,
       "futOspfRRDRouteMetricType": futOspfRRDRouteMetricType,
       "futOspfRRDRouteTagType": futOspfRRDRouteTagType,
       "futOspfRRDRouteTag": futOspfRRDRouteTag,
       "futOspfRRDRouteStatus": futOspfRRDRouteStatus,
       "futOspfVirtNbrTable": futOspfVirtNbrTable,
       "futOspfVirtNbrEntry": futOspfVirtNbrEntry,
       "futOspfVirtNbrRestartHelperStatus": futOspfVirtNbrRestartHelperStatus,
       "futOspfVirtNbrRestartHelperAge": futOspfVirtNbrRestartHelperAge,
       "futOspfVirtNbrRestartHelperExitReason": futOspfVirtNbrRestartHelperExitReason,
       "futospfDistInOutRouteMap": futospfDistInOutRouteMap,
       "futOspfDistInOutRouteMapTable": futOspfDistInOutRouteMapTable,
       "futOspfDistInOutRouteMapEntry": futOspfDistInOutRouteMapEntry,
       "futOspfDistInOutRouteMapName": futOspfDistInOutRouteMapName,
       "futOspfDistInOutRouteMapType": futOspfDistInOutRouteMapType,
       "futOspfDistInOutRouteMapValue": futOspfDistInOutRouteMapValue,
       "futOspfDistInOutRouteMapRowStatus": futOspfDistInOutRouteMapRowStatus,
       "futospfPreferenceGroup": futospfPreferenceGroup,
       "futOspfPreferenceValue": futOspfPreferenceValue,
       "futOspfIfAuthTable": futOspfIfAuthTable,
       "futOspfIfAuthEntry": futOspfIfAuthEntry,
       "futOspfIfAuthIpAddress": futOspfIfAuthIpAddress,
       "futOspfIfAuthAddressLessIf": futOspfIfAuthAddressLessIf,
       "futOspfIfAuthKeyId": futOspfIfAuthKeyId,
       "futOspfIfAuthKey": futOspfIfAuthKey,
       "futOspfIfAuthKeyStartAccept": futOspfIfAuthKeyStartAccept,
       "futOspfIfAuthKeyStartGenerate": futOspfIfAuthKeyStartGenerate,
       "futOspfIfAuthKeyStopGenerate": futOspfIfAuthKeyStopGenerate,
       "futOspfIfAuthKeyStopAccept": futOspfIfAuthKeyStopAccept,
       "futOspfIfAuthKeyStatus": futOspfIfAuthKeyStatus,
       "futOspfVirtIfAuthTable": futOspfVirtIfAuthTable,
       "futOspfVirtIfAuthEntry": futOspfVirtIfAuthEntry,
       "futOspfVirtIfAuthAreaId": futOspfVirtIfAuthAreaId,
       "futOspfVirtIfAuthNeighbor": futOspfVirtIfAuthNeighbor,
       "futOspfVirtIfAuthKeyId": futOspfVirtIfAuthKeyId,
       "futOspfVirtIfAuthKey": futOspfVirtIfAuthKey,
       "futOspfVirtIfAuthKeyStartAccept": futOspfVirtIfAuthKeyStartAccept,
       "futOspfVirtIfAuthKeyStartGenerate": futOspfVirtIfAuthKeyStartGenerate,
       "futOspfVirtIfAuthKeyStopGenerate": futOspfVirtIfAuthKeyStopGenerate,
       "futOspfVirtIfAuthKeyStopAccept": futOspfVirtIfAuthKeyStopAccept,
       "futOspfVirtIfAuthKeyStatus": futOspfVirtIfAuthKeyStatus,
       "futOspfIfCryptoAuthTable": futOspfIfCryptoAuthTable,
       "futOspfIfCryptoAuthEntry": futOspfIfCryptoAuthEntry,
       "futOspfIfCryptoAuthType": futOspfIfCryptoAuthType,
       "futOspfVirtIfCryptoAuthTable": futOspfVirtIfCryptoAuthTable,
       "futOspfVirtIfCryptoAuthEntry": futOspfVirtIfCryptoAuthEntry,
       "futOspfVirtIfCryptoAuthType": futOspfVirtIfCryptoAuthType,
       "futOspfTestGroup": futOspfTestGroup,
       "futOspfNotification": futOspfNotification,
       "futOspfTraps": futOspfTraps,
       "futOspfRestartStatusChange": futOspfRestartStatusChange,
       "futOspfNbrRestartHelperStatusChange": futOspfNbrRestartHelperStatusChange,
       "futOspfVirtNbrRestartHelperStatusChange": futOspfVirtNbrRestartHelperStatusChange,
       "futOspfHotStandbyEventTrap": futOspfHotStandbyEventTrap,
       "futOspfOasGroup": futOspfOasGroup}
)
