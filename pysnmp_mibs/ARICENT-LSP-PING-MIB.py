# SNMP MIB module (ARICENT-LSP-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LSP-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:56 2025
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

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsLspp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11)
)
if mibBuilder.loadTexts:
    fsLspp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsLsppTimeUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("milliseconds", 1),
          ("seconds", 2),
          ("minutes", 3))
    )



class FsLsppAddressType(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("ipv4Numbered", 1),
          ("ipv4UnNumbered", 2),
          ("ipv6Numbered", 3),
          ("ipv6UnNumbered", 4))
    )



# MIB Managed Objects in the order of their OIDs

_FsLsppGlobals_ObjectIdentity = ObjectIdentity
fsLsppGlobals = _FsLsppGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1)
)
_FsLsppGlobalConfigTable_Object = MibTable
fsLsppGlobalConfigTable = _FsLsppGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1)
)
if mibBuilder.loadTexts:
    fsLsppGlobalConfigTable.setStatus("current")
_FsLsppGlobalConfigTableEntry_Object = MibTableRow
fsLsppGlobalConfigTableEntry = _FsLsppGlobalConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1)
)
fsLsppGlobalConfigTableEntry.setIndexNames(
    (0, "ARICENT-LSP-PING-MIB", "fsLsppContextId"),
)
if mibBuilder.loadTexts:
    fsLsppGlobalConfigTableEntry.setStatus("current")
_FsLsppContextId_Type = Unsigned32
_FsLsppContextId_Object = MibTableColumn
fsLsppContextId = _FsLsppContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 1),
    _FsLsppContextId_Type()
)
fsLsppContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLsppContextId.setStatus("current")


class _FsLsppSystemControl_Type(Integer32):
    """Custom type fsLsppSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsLsppSystemControl_Type.__name__ = "Integer32"
_FsLsppSystemControl_Object = MibTableColumn
fsLsppSystemControl = _FsLsppSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 2),
    _FsLsppSystemControl_Type()
)
fsLsppSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSystemControl.setStatus("current")


class _FsLsppTrapStatus_Type(Integer32):
    """Custom type fsLsppTrapStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsLsppTrapStatus_Type.__name__ = "Integer32"
_FsLsppTrapStatus_Object = MibTableColumn
fsLsppTrapStatus = _FsLsppTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 3),
    _FsLsppTrapStatus_Type()
)
fsLsppTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTrapStatus.setStatus("current")


class _FsLsppTraceLevel_Type(Integer32):
    """Custom type fsLsppTraceLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_FsLsppTraceLevel_Type.__name__ = "Integer32"
_FsLsppTraceLevel_Object = MibTableColumn
fsLsppTraceLevel = _FsLsppTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 4),
    _FsLsppTraceLevel_Type()
)
fsLsppTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTraceLevel.setStatus("current")


class _FsLsppAgeOutTime_Type(Unsigned32):
    """Custom type fsLsppAgeOutTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsLsppAgeOutTime_Type.__name__ = "Unsigned32"
_FsLsppAgeOutTime_Object = MibTableColumn
fsLsppAgeOutTime = _FsLsppAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 5),
    _FsLsppAgeOutTime_Type()
)
fsLsppAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppAgeOutTime.setStatus("current")


class _FsLsppAgeOutTmrUnit_Type(FsLsppTimeUnit):
    """Custom type fsLsppAgeOutTmrUnit based on FsLsppTimeUnit"""
    defaultValue = 3


_FsLsppAgeOutTmrUnit_Type.__name__ = "FsLsppTimeUnit"
_FsLsppAgeOutTmrUnit_Object = MibTableColumn
fsLsppAgeOutTmrUnit = _FsLsppAgeOutTmrUnit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 6),
    _FsLsppAgeOutTmrUnit_Type()
)
fsLsppAgeOutTmrUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppAgeOutTmrUnit.setStatus("current")


class _FsLsppClearEchoStats_Type(TruthValue):
    """Custom type fsLsppClearEchoStats based on TruthValue"""
    defaultValue = 2


_FsLsppClearEchoStats_Type.__name__ = "TruthValue"
_FsLsppClearEchoStats_Object = MibTableColumn
fsLsppClearEchoStats = _FsLsppClearEchoStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 7),
    _FsLsppClearEchoStats_Type()
)
fsLsppClearEchoStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppClearEchoStats.setStatus("current")


class _FsLsppBfdBtStrapRespReq_Type(TruthValue):
    """Custom type fsLsppBfdBtStrapRespReq based on TruthValue"""
    defaultValue = 1


_FsLsppBfdBtStrapRespReq_Type.__name__ = "TruthValue"
_FsLsppBfdBtStrapRespReq_Object = MibTableColumn
fsLsppBfdBtStrapRespReq = _FsLsppBfdBtStrapRespReq_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 8),
    _FsLsppBfdBtStrapRespReq_Type()
)
fsLsppBfdBtStrapRespReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppBfdBtStrapRespReq.setStatus("current")


class _FsLsppBfdBtStrapAgeOutTime_Type(Unsigned32):
    """Custom type fsLsppBfdBtStrapAgeOutTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsLsppBfdBtStrapAgeOutTime_Type.__name__ = "Unsigned32"
_FsLsppBfdBtStrapAgeOutTime_Object = MibTableColumn
fsLsppBfdBtStrapAgeOutTime = _FsLsppBfdBtStrapAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 9),
    _FsLsppBfdBtStrapAgeOutTime_Type()
)
fsLsppBfdBtStrapAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppBfdBtStrapAgeOutTime.setStatus("current")


class _FsLsppBfdBtStrapAgeOutTmrUnit_Type(FsLsppTimeUnit):
    """Custom type fsLsppBfdBtStrapAgeOutTmrUnit based on FsLsppTimeUnit"""
    defaultValue = 3


_FsLsppBfdBtStrapAgeOutTmrUnit_Type.__name__ = "FsLsppTimeUnit"
_FsLsppBfdBtStrapAgeOutTmrUnit_Object = MibTableColumn
fsLsppBfdBtStrapAgeOutTmrUnit = _FsLsppBfdBtStrapAgeOutTmrUnit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 1, 1, 10),
    _FsLsppBfdBtStrapAgeOutTmrUnit_Type()
)
fsLsppBfdBtStrapAgeOutTmrUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppBfdBtStrapAgeOutTmrUnit.setStatus("current")
_FsLsppGlobalStatsTable_Object = MibTable
fsLsppGlobalStatsTable = _FsLsppGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2)
)
if mibBuilder.loadTexts:
    fsLsppGlobalStatsTable.setStatus("current")
_FsLsppGlobalStatsTableEntry_Object = MibTableRow
fsLsppGlobalStatsTableEntry = _FsLsppGlobalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1)
)
fsLsppGlobalStatsTableEntry.setIndexNames(
    (0, "ARICENT-LSP-PING-MIB", "fsLsppContextId"),
)
if mibBuilder.loadTexts:
    fsLsppGlobalStatsTableEntry.setStatus("current")
_FsLsppGlbStatReqTx_Type = Counter32
_FsLsppGlbStatReqTx_Object = MibTableColumn
fsLsppGlbStatReqTx = _FsLsppGlbStatReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 1),
    _FsLsppGlbStatReqTx_Type()
)
fsLsppGlbStatReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqTx.setStatus("current")
_FsLsppGlbStatReqRx_Type = Counter32
_FsLsppGlbStatReqRx_Object = MibTableColumn
fsLsppGlbStatReqRx = _FsLsppGlbStatReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 2),
    _FsLsppGlbStatReqRx_Type()
)
fsLsppGlbStatReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqRx.setStatus("current")
_FsLsppGlbStatReqTimedOut_Type = Counter32
_FsLsppGlbStatReqTimedOut_Object = MibTableColumn
fsLsppGlbStatReqTimedOut = _FsLsppGlbStatReqTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 3),
    _FsLsppGlbStatReqTimedOut_Type()
)
fsLsppGlbStatReqTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqTimedOut.setStatus("current")
_FsLsppGlbStatReqUnSent_Type = Counter32
_FsLsppGlbStatReqUnSent_Object = MibTableColumn
fsLsppGlbStatReqUnSent = _FsLsppGlbStatReqUnSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 4),
    _FsLsppGlbStatReqUnSent_Type()
)
fsLsppGlbStatReqUnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqUnSent.setStatus("current")
_FsLsppGlbStatReplyTx_Type = Counter32
_FsLsppGlbStatReplyTx_Object = MibTableColumn
fsLsppGlbStatReplyTx = _FsLsppGlbStatReplyTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 5),
    _FsLsppGlbStatReplyTx_Type()
)
fsLsppGlbStatReplyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReplyTx.setStatus("current")
_FsLsppGlbStatReplyRx_Type = Counter32
_FsLsppGlbStatReplyRx_Object = MibTableColumn
fsLsppGlbStatReplyRx = _FsLsppGlbStatReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 6),
    _FsLsppGlbStatReplyRx_Type()
)
fsLsppGlbStatReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReplyRx.setStatus("current")
_FsLsppGlbStatReplyDropped_Type = Counter32
_FsLsppGlbStatReplyDropped_Object = MibTableColumn
fsLsppGlbStatReplyDropped = _FsLsppGlbStatReplyDropped_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 7),
    _FsLsppGlbStatReplyDropped_Type()
)
fsLsppGlbStatReplyDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReplyDropped.setStatus("current")
_FsLsppGlbStatReplyUnSent_Type = Counter32
_FsLsppGlbStatReplyUnSent_Object = MibTableColumn
fsLsppGlbStatReplyUnSent = _FsLsppGlbStatReplyUnSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 8),
    _FsLsppGlbStatReplyUnSent_Type()
)
fsLsppGlbStatReplyUnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReplyUnSent.setStatus("current")
_FsLsppGlbStatReplyFromEgr_Type = Counter32
_FsLsppGlbStatReplyFromEgr_Object = MibTableColumn
fsLsppGlbStatReplyFromEgr = _FsLsppGlbStatReplyFromEgr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 9),
    _FsLsppGlbStatReplyFromEgr_Type()
)
fsLsppGlbStatReplyFromEgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReplyFromEgr.setStatus("current")
_FsLsppGlbStatUnLbldOutIf_Type = Counter32
_FsLsppGlbStatUnLbldOutIf_Object = MibTableColumn
fsLsppGlbStatUnLbldOutIf = _FsLsppGlbStatUnLbldOutIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 10),
    _FsLsppGlbStatUnLbldOutIf_Type()
)
fsLsppGlbStatUnLbldOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatUnLbldOutIf.setStatus("current")
_FsLsppGlbStatDsMapMismatch_Type = Counter32
_FsLsppGlbStatDsMapMismatch_Object = MibTableColumn
fsLsppGlbStatDsMapMismatch = _FsLsppGlbStatDsMapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 11),
    _FsLsppGlbStatDsMapMismatch_Type()
)
fsLsppGlbStatDsMapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatDsMapMismatch.setStatus("current")
_FsLsppGlbStatFecLblMismatch_Type = Counter32
_FsLsppGlbStatFecLblMismatch_Object = MibTableColumn
fsLsppGlbStatFecLblMismatch = _FsLsppGlbStatFecLblMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 12),
    _FsLsppGlbStatFecLblMismatch_Type()
)
fsLsppGlbStatFecLblMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatFecLblMismatch.setStatus("current")
_FsLsppGlbStatNoFecMapping_Type = Counter32
_FsLsppGlbStatNoFecMapping_Object = MibTableColumn
fsLsppGlbStatNoFecMapping = _FsLsppGlbStatNoFecMapping_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 13),
    _FsLsppGlbStatNoFecMapping_Type()
)
fsLsppGlbStatNoFecMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatNoFecMapping.setStatus("current")
_FsLsppGlbStatUnKUpstreamIf_Type = Counter32
_FsLsppGlbStatUnKUpstreamIf_Object = MibTableColumn
fsLsppGlbStatUnKUpstreamIf = _FsLsppGlbStatUnKUpstreamIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 14),
    _FsLsppGlbStatUnKUpstreamIf_Type()
)
fsLsppGlbStatUnKUpstreamIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatUnKUpstreamIf.setStatus("current")
_FsLsppGlbStatReqLblSwitched_Type = Counter32
_FsLsppGlbStatReqLblSwitched_Object = MibTableColumn
fsLsppGlbStatReqLblSwitched = _FsLsppGlbStatReqLblSwitched_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 15),
    _FsLsppGlbStatReqLblSwitched_Type()
)
fsLsppGlbStatReqLblSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqLblSwitched.setStatus("current")
_FsLsppGlbStatReqUnSupptdTlv_Type = Counter32
_FsLsppGlbStatReqUnSupptdTlv_Object = MibTableColumn
fsLsppGlbStatReqUnSupptdTlv = _FsLsppGlbStatReqUnSupptdTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 16),
    _FsLsppGlbStatReqUnSupptdTlv_Type()
)
fsLsppGlbStatReqUnSupptdTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatReqUnSupptdTlv.setStatus("current")
_FsLsppGlbStatMalformedReq_Type = Counter32
_FsLsppGlbStatMalformedReq_Object = MibTableColumn
fsLsppGlbStatMalformedReq = _FsLsppGlbStatMalformedReq_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 17),
    _FsLsppGlbStatMalformedReq_Type()
)
fsLsppGlbStatMalformedReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatMalformedReq.setStatus("current")
_FsLsppGlbStatNoLblEntry_Type = Counter32
_FsLsppGlbStatNoLblEntry_Object = MibTableColumn
fsLsppGlbStatNoLblEntry = _FsLsppGlbStatNoLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 18),
    _FsLsppGlbStatNoLblEntry_Type()
)
fsLsppGlbStatNoLblEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatNoLblEntry.setStatus("current")
_FsLsppGlbStatPreTermReq_Type = Counter32
_FsLsppGlbStatPreTermReq_Object = MibTableColumn
fsLsppGlbStatPreTermReq = _FsLsppGlbStatPreTermReq_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 19),
    _FsLsppGlbStatPreTermReq_Type()
)
fsLsppGlbStatPreTermReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatPreTermReq.setStatus("current")
_FsLsppGlbStatProtMismatch_Type = Counter32
_FsLsppGlbStatProtMismatch_Object = MibTableColumn
fsLsppGlbStatProtMismatch = _FsLsppGlbStatProtMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 20),
    _FsLsppGlbStatProtMismatch_Type()
)
fsLsppGlbStatProtMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatProtMismatch.setStatus("current")
_FsLsppGlbStatRsvdRetCode_Type = Counter32
_FsLsppGlbStatRsvdRetCode_Object = MibTableColumn
fsLsppGlbStatRsvdRetCode = _FsLsppGlbStatRsvdRetCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 21),
    _FsLsppGlbStatRsvdRetCode_Type()
)
fsLsppGlbStatRsvdRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatRsvdRetCode.setStatus("current")
_FsLsppGlbStatNoRetCode_Type = Counter32
_FsLsppGlbStatNoRetCode_Object = MibTableColumn
fsLsppGlbStatNoRetCode = _FsLsppGlbStatNoRetCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 22),
    _FsLsppGlbStatNoRetCode_Type()
)
fsLsppGlbStatNoRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatNoRetCode.setStatus("current")
_FsLsppGlbStatUndefRetCode_Type = Counter32
_FsLsppGlbStatUndefRetCode_Object = MibTableColumn
fsLsppGlbStatUndefRetCode = _FsLsppGlbStatUndefRetCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 23),
    _FsLsppGlbStatUndefRetCode_Type()
)
fsLsppGlbStatUndefRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatUndefRetCode.setStatus("current")
_FsLsppGlbStatInvalidPktDropped_Type = Counter32
_FsLsppGlbStatInvalidPktDropped_Object = MibTableColumn
fsLsppGlbStatInvalidPktDropped = _FsLsppGlbStatInvalidPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 1, 2, 1, 24),
    _FsLsppGlbStatInvalidPktDropped_Type()
)
fsLsppGlbStatInvalidPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppGlbStatInvalidPktDropped.setStatus("current")
_FsLsppPingTrace_ObjectIdentity = ObjectIdentity
fsLsppPingTrace = _FsLsppPingTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2)
)
_FsLsppPingTraceTable_Object = MibTable
fsLsppPingTraceTable = _FsLsppPingTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1)
)
if mibBuilder.loadTexts:
    fsLsppPingTraceTable.setStatus("current")
_FsLsppPingTraceTableEntry_Object = MibTableRow
fsLsppPingTraceTableEntry = _FsLsppPingTraceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1)
)
fsLsppPingTraceTableEntry.setIndexNames(
    (0, "ARICENT-LSP-PING-MIB", "fsLsppContextId"),
    (0, "ARICENT-LSP-PING-MIB", "fsLsppSenderHandle"),
)
if mibBuilder.loadTexts:
    fsLsppPingTraceTableEntry.setStatus("current")


class _FsLsppSenderHandle_Type(Unsigned32):
    """Custom type fsLsppSenderHandle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsLsppSenderHandle_Type.__name__ = "Unsigned32"
_FsLsppSenderHandle_Object = MibTableColumn
fsLsppSenderHandle = _FsLsppSenderHandle_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 1),
    _FsLsppSenderHandle_Type()
)
fsLsppSenderHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLsppSenderHandle.setStatus("current")


class _FsLsppRequestType_Type(Integer32):
    """Custom type fsLsppRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ping", 1),
          ("traceRoute", 2))
    )


_FsLsppRequestType_Type.__name__ = "Integer32"
_FsLsppRequestType_Object = MibTableColumn
fsLsppRequestType = _FsLsppRequestType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 2),
    _FsLsppRequestType_Type()
)
fsLsppRequestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppRequestType.setStatus("current")


class _FsLsppRequestOwner_Type(Integer32):
    """Custom type fsLsppRequestOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 1),
          ("bfd", 2))
    )


_FsLsppRequestOwner_Type.__name__ = "Integer32"
_FsLsppRequestOwner_Object = MibTableColumn
fsLsppRequestOwner = _FsLsppRequestOwner_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 3),
    _FsLsppRequestOwner_Type()
)
fsLsppRequestOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppRequestOwner.setStatus("current")


class _FsLsppPathType_Type(Integer32):
    """Custom type fsLsppPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ldpIpv4", 1),
          ("ldpIpv6", 2),
          ("rsvpIpv4", 3),
          ("rsvpIpv6", 4),
          ("fec128Pw", 5),
          ("fec129Pw", 6),
          ("mep", 7))
    )


_FsLsppPathType_Type.__name__ = "Integer32"
_FsLsppPathType_Object = MibTableColumn
fsLsppPathType = _FsLsppPathType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 4),
    _FsLsppPathType_Type()
)
fsLsppPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppPathType.setStatus("current")
_FsLsppPathPointer_Type = RowPointer
_FsLsppPathPointer_Object = MibTableColumn
fsLsppPathPointer = _FsLsppPathPointer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 5),
    _FsLsppPathPointer_Type()
)
fsLsppPathPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppPathPointer.setStatus("current")
_FsLsppTgtMipGlobalId_Type = Unsigned32
_FsLsppTgtMipGlobalId_Object = MibTableColumn
fsLsppTgtMipGlobalId = _FsLsppTgtMipGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 6),
    _FsLsppTgtMipGlobalId_Type()
)
fsLsppTgtMipGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTgtMipGlobalId.setStatus("current")
_FsLsppTgtMipNodeId_Type = Unsigned32
_FsLsppTgtMipNodeId_Object = MibTableColumn
fsLsppTgtMipNodeId = _FsLsppTgtMipNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 7),
    _FsLsppTgtMipNodeId_Type()
)
fsLsppTgtMipNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTgtMipNodeId.setStatus("current")
_FsLsppTgtMipIfNum_Type = Unsigned32
_FsLsppTgtMipIfNum_Object = MibTableColumn
fsLsppTgtMipIfNum = _FsLsppTgtMipIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 8),
    _FsLsppTgtMipIfNum_Type()
)
fsLsppTgtMipIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTgtMipIfNum.setStatus("current")


class _FsLsppReplyMode_Type(Integer32):
    """Custom type fsLsppReplyMode based on Integer32"""
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
        *(("noReply", 1),
          ("ip", 2),
          ("ipRouterAlert", 3),
          ("controlChannel", 4))
    )


_FsLsppReplyMode_Type.__name__ = "Integer32"
_FsLsppReplyMode_Object = MibTableColumn
fsLsppReplyMode = _FsLsppReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 9),
    _FsLsppReplyMode_Type()
)
fsLsppReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppReplyMode.setStatus("current")


class _FsLsppRepeatCount_Type(Unsigned32):
    """Custom type fsLsppRepeatCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsLsppRepeatCount_Type.__name__ = "Unsigned32"
_FsLsppRepeatCount_Object = MibTableColumn
fsLsppRepeatCount = _FsLsppRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 10),
    _FsLsppRepeatCount_Type()
)
fsLsppRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppRepeatCount.setStatus("current")


class _FsLsppPacketSize_Type(Unsigned32):
    """Custom type fsLsppPacketSize based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1450),
    )


_FsLsppPacketSize_Type.__name__ = "Unsigned32"
_FsLsppPacketSize_Object = MibTableColumn
fsLsppPacketSize = _FsLsppPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 11),
    _FsLsppPacketSize_Type()
)
fsLsppPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppPacketSize.setStatus("current")


class _FsLsppPadPattern_Type(OctetString):
    """Custom type fsLsppPadPattern based on OctetString"""
    defaultHexValue = "ABCD"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppPadPattern_Type.__name__ = "OctetString"
_FsLsppPadPattern_Object = MibTableColumn
fsLsppPadPattern = _FsLsppPadPattern_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 12),
    _FsLsppPadPattern_Type()
)
fsLsppPadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppPadPattern.setStatus("current")


class _FsLsppTTLValue_Type(Unsigned32):
    """Custom type fsLsppTTLValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsLsppTTLValue_Type.__name__ = "Unsigned32"
_FsLsppTTLValue_Object = MibTableColumn
fsLsppTTLValue = _FsLsppTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 13),
    _FsLsppTTLValue_Type()
)
fsLsppTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppTTLValue.setStatus("current")


class _FsLsppWFRInterval_Type(Unsigned32):
    """Custom type fsLsppWFRInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsLsppWFRInterval_Type.__name__ = "Unsigned32"
_FsLsppWFRInterval_Object = MibTableColumn
fsLsppWFRInterval = _FsLsppWFRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 14),
    _FsLsppWFRInterval_Type()
)
fsLsppWFRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppWFRInterval.setStatus("current")


class _FsLsppWFRTmrUnit_Type(FsLsppTimeUnit):
    """Custom type fsLsppWFRTmrUnit based on FsLsppTimeUnit"""
    defaultValue = 2


_FsLsppWFRTmrUnit_Type.__name__ = "FsLsppTimeUnit"
_FsLsppWFRTmrUnit_Object = MibTableColumn
fsLsppWFRTmrUnit = _FsLsppWFRTmrUnit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 15),
    _FsLsppWFRTmrUnit_Type()
)
fsLsppWFRTmrUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppWFRTmrUnit.setStatus("current")


class _FsLsppWTSInterval_Type(Unsigned32):
    """Custom type fsLsppWTSInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsLsppWTSInterval_Type.__name__ = "Unsigned32"
_FsLsppWTSInterval_Object = MibTableColumn
fsLsppWTSInterval = _FsLsppWTSInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 16),
    _FsLsppWTSInterval_Type()
)
fsLsppWTSInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppWTSInterval.setStatus("current")


class _FsLsppWTSTmrUnit_Type(FsLsppTimeUnit):
    """Custom type fsLsppWTSTmrUnit based on FsLsppTimeUnit"""
    defaultValue = 2


_FsLsppWTSTmrUnit_Type.__name__ = "FsLsppTimeUnit"
_FsLsppWTSTmrUnit_Object = MibTableColumn
fsLsppWTSTmrUnit = _FsLsppWTSTmrUnit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 17),
    _FsLsppWTSTmrUnit_Type()
)
fsLsppWTSTmrUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppWTSTmrUnit.setStatus("current")


class _FsLsppReplyDscpValue_Type(Unsigned32):
    """Custom type fsLsppReplyDscpValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FsLsppReplyDscpValue_Type.__name__ = "Unsigned32"
_FsLsppReplyDscpValue_Object = MibTableColumn
fsLsppReplyDscpValue = _FsLsppReplyDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 18),
    _FsLsppReplyDscpValue_Type()
)
fsLsppReplyDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppReplyDscpValue.setStatus("current")


class _FsLsppSweepOption_Type(TruthValue):
    """Custom type fsLsppSweepOption based on TruthValue"""
    defaultValue = 2


_FsLsppSweepOption_Type.__name__ = "TruthValue"
_FsLsppSweepOption_Object = MibTableColumn
fsLsppSweepOption = _FsLsppSweepOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 19),
    _FsLsppSweepOption_Type()
)
fsLsppSweepOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSweepOption.setStatus("current")


class _FsLsppSweepMinimum_Type(Unsigned32):
    """Custom type fsLsppSweepMinimum based on Unsigned32"""
    defaultValue = 100


_FsLsppSweepMinimum_Type.__name__ = "Unsigned32"
_FsLsppSweepMinimum_Object = MibTableColumn
fsLsppSweepMinimum = _FsLsppSweepMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 20),
    _FsLsppSweepMinimum_Type()
)
fsLsppSweepMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSweepMinimum.setStatus("current")


class _FsLsppSweepMaximum_Type(Unsigned32):
    """Custom type fsLsppSweepMaximum based on Unsigned32"""
    defaultValue = 17986


_FsLsppSweepMaximum_Type.__name__ = "Unsigned32"
_FsLsppSweepMaximum_Object = MibTableColumn
fsLsppSweepMaximum = _FsLsppSweepMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 21),
    _FsLsppSweepMaximum_Type()
)
fsLsppSweepMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSweepMaximum.setStatus("current")


class _FsLsppSweepIncrement_Type(Unsigned32):
    """Custom type fsLsppSweepIncrement based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_FsLsppSweepIncrement_Type.__name__ = "Unsigned32"
_FsLsppSweepIncrement_Object = MibTableColumn
fsLsppSweepIncrement = _FsLsppSweepIncrement_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 22),
    _FsLsppSweepIncrement_Type()
)
fsLsppSweepIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSweepIncrement.setStatus("current")


class _FsLsppBurstOption_Type(TruthValue):
    """Custom type fsLsppBurstOption based on TruthValue"""
    defaultValue = 2


_FsLsppBurstOption_Type.__name__ = "TruthValue"
_FsLsppBurstOption_Object = MibTableColumn
fsLsppBurstOption = _FsLsppBurstOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 23),
    _FsLsppBurstOption_Type()
)
fsLsppBurstOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppBurstOption.setStatus("current")


class _FsLsppBurstSize_Type(Unsigned32):
    """Custom type fsLsppBurstSize based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsLsppBurstSize_Type.__name__ = "Unsigned32"
_FsLsppBurstSize_Object = MibTableColumn
fsLsppBurstSize = _FsLsppBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 24),
    _FsLsppBurstSize_Type()
)
fsLsppBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppBurstSize.setStatus("current")


class _FsLsppEXPValue_Type(Unsigned32):
    """Custom type fsLsppEXPValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsLsppEXPValue_Type.__name__ = "Unsigned32"
_FsLsppEXPValue_Object = MibTableColumn
fsLsppEXPValue = _FsLsppEXPValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 25),
    _FsLsppEXPValue_Type()
)
fsLsppEXPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppEXPValue.setStatus("current")


class _FsLsppDsMap_Type(TruthValue):
    """Custom type fsLsppDsMap based on TruthValue"""
    defaultValue = 2


_FsLsppDsMap_Type.__name__ = "TruthValue"
_FsLsppDsMap_Object = MibTableColumn
fsLsppDsMap = _FsLsppDsMap_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 26),
    _FsLsppDsMap_Type()
)
fsLsppDsMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppDsMap.setStatus("current")


class _FsLsppFecValidate_Type(TruthValue):
    """Custom type fsLsppFecValidate based on TruthValue"""
    defaultValue = 1


_FsLsppFecValidate_Type.__name__ = "TruthValue"
_FsLsppFecValidate_Object = MibTableColumn
fsLsppFecValidate = _FsLsppFecValidate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 27),
    _FsLsppFecValidate_Type()
)
fsLsppFecValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppFecValidate.setStatus("current")


class _FsLsppReplyPadTlv_Type(TruthValue):
    """Custom type fsLsppReplyPadTlv based on TruthValue"""
    defaultValue = 2


_FsLsppReplyPadTlv_Type.__name__ = "TruthValue"
_FsLsppReplyPadTlv_Object = MibTableColumn
fsLsppReplyPadTlv = _FsLsppReplyPadTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 28),
    _FsLsppReplyPadTlv_Type()
)
fsLsppReplyPadTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppReplyPadTlv.setStatus("current")


class _FsLsppForceExplicitNull_Type(TruthValue):
    """Custom type fsLsppForceExplicitNull based on TruthValue"""
    defaultValue = 2


_FsLsppForceExplicitNull_Type.__name__ = "TruthValue"
_FsLsppForceExplicitNull_Object = MibTableColumn
fsLsppForceExplicitNull = _FsLsppForceExplicitNull_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 29),
    _FsLsppForceExplicitNull_Type()
)
fsLsppForceExplicitNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppForceExplicitNull.setStatus("current")


class _FsLsppInterfaceLabelTlv_Type(TruthValue):
    """Custom type fsLsppInterfaceLabelTlv based on TruthValue"""
    defaultValue = 2


_FsLsppInterfaceLabelTlv_Type.__name__ = "TruthValue"
_FsLsppInterfaceLabelTlv_Object = MibTableColumn
fsLsppInterfaceLabelTlv = _FsLsppInterfaceLabelTlv_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 30),
    _FsLsppInterfaceLabelTlv_Type()
)
fsLsppInterfaceLabelTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppInterfaceLabelTlv.setStatus("current")


class _FsLsppSameSeqNumOption_Type(TruthValue):
    """Custom type fsLsppSameSeqNumOption based on TruthValue"""
    defaultValue = 2


_FsLsppSameSeqNumOption_Type.__name__ = "TruthValue"
_FsLsppSameSeqNumOption_Object = MibTableColumn
fsLsppSameSeqNumOption = _FsLsppSameSeqNumOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 31),
    _FsLsppSameSeqNumOption_Type()
)
fsLsppSameSeqNumOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppSameSeqNumOption.setStatus("current")


class _FsLsppVerbose_Type(TruthValue):
    """Custom type fsLsppVerbose based on TruthValue"""
    defaultValue = 2


_FsLsppVerbose_Type.__name__ = "TruthValue"
_FsLsppVerbose_Object = MibTableColumn
fsLsppVerbose = _FsLsppVerbose_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 32),
    _FsLsppVerbose_Type()
)
fsLsppVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppVerbose.setStatus("current")


class _FsLsppReversePathVerify_Type(TruthValue):
    """Custom type fsLsppReversePathVerify based on TruthValue"""
    defaultValue = 2


_FsLsppReversePathVerify_Type.__name__ = "TruthValue"
_FsLsppReversePathVerify_Object = MibTableColumn
fsLsppReversePathVerify = _FsLsppReversePathVerify_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 33),
    _FsLsppReversePathVerify_Type()
)
fsLsppReversePathVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppReversePathVerify.setStatus("current")


class _FsLsppEncapType_Type(Integer32):
    """Custom type fsLsppEncapType based on Integer32"""
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
        *(("mplsIp", 1),
          ("mplsAch", 2),
          ("mplsAchIp", 3),
          ("vccvNegotiated", 4))
    )


_FsLsppEncapType_Type.__name__ = "Integer32"
_FsLsppEncapType_Object = MibTableColumn
fsLsppEncapType = _FsLsppEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 34),
    _FsLsppEncapType_Type()
)
fsLsppEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLsppEncapType.setStatus("current")


class _FsLsppStatus_Type(Integer32):
    """Custom type fsLsppStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("success", 2),
          ("failure", 3))
    )


_FsLsppStatus_Type.__name__ = "Integer32"
_FsLsppStatus_Object = MibTableColumn
fsLsppStatus = _FsLsppStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 35),
    _FsLsppStatus_Type()
)
fsLsppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppStatus.setStatus("current")
_FsLsppActualHopCount_Type = Unsigned32
_FsLsppActualHopCount_Object = MibTableColumn
fsLsppActualHopCount = _FsLsppActualHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 36),
    _FsLsppActualHopCount_Type()
)
fsLsppActualHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppActualHopCount.setStatus("current")
_FsLsppResponderAddrType_Type = FsLsppAddressType
_FsLsppResponderAddrType_Object = MibTableColumn
fsLsppResponderAddrType = _FsLsppResponderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 37),
    _FsLsppResponderAddrType_Type()
)
fsLsppResponderAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderAddrType.setStatus("current")


class _FsLsppResponderAddr_Type(OctetString):
    """Custom type fsLsppResponderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppResponderAddr_Type.__name__ = "OctetString"
_FsLsppResponderAddr_Object = MibTableColumn
fsLsppResponderAddr = _FsLsppResponderAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 38),
    _FsLsppResponderAddr_Type()
)
fsLsppResponderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderAddr.setStatus("current")
_FsLsppResponderGlobalId_Type = Unsigned32
_FsLsppResponderGlobalId_Object = MibTableColumn
fsLsppResponderGlobalId = _FsLsppResponderGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 39),
    _FsLsppResponderGlobalId_Type()
)
fsLsppResponderGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderGlobalId.setStatus("current")
_FsLsppResponderId_Type = Unsigned32
_FsLsppResponderId_Object = MibTableColumn
fsLsppResponderId = _FsLsppResponderId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 40),
    _FsLsppResponderId_Type()
)
fsLsppResponderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderId.setStatus("current")
_FsLsppMaxRtt_Type = Unsigned32
_FsLsppMaxRtt_Object = MibTableColumn
fsLsppMaxRtt = _FsLsppMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 41),
    _FsLsppMaxRtt_Type()
)
fsLsppMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppMaxRtt.setStatus("current")
_FsLsppMinRtt_Type = Unsigned32
_FsLsppMinRtt_Object = MibTableColumn
fsLsppMinRtt = _FsLsppMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 42),
    _FsLsppMinRtt_Type()
)
fsLsppMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppMinRtt.setStatus("current")
_FsLsppAverageRtt_Type = Unsigned32
_FsLsppAverageRtt_Object = MibTableColumn
fsLsppAverageRtt = _FsLsppAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 43),
    _FsLsppAverageRtt_Type()
)
fsLsppAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppAverageRtt.setStatus("current")
_FsLsppPktsTx_Type = Counter32
_FsLsppPktsTx_Object = MibTableColumn
fsLsppPktsTx = _FsLsppPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 44),
    _FsLsppPktsTx_Type()
)
fsLsppPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppPktsTx.setStatus("current")
_FsLsppPktsRx_Type = Counter32
_FsLsppPktsRx_Object = MibTableColumn
fsLsppPktsRx = _FsLsppPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 45),
    _FsLsppPktsRx_Type()
)
fsLsppPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppPktsRx.setStatus("current")
_FsLsppPktsUnSent_Type = Counter32
_FsLsppPktsUnSent_Object = MibTableColumn
fsLsppPktsUnSent = _FsLsppPktsUnSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 46),
    _FsLsppPktsUnSent_Type()
)
fsLsppPktsUnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppPktsUnSent.setStatus("current")
_FsLsppRowStatus_Type = RowStatus
_FsLsppRowStatus_Object = MibTableColumn
fsLsppRowStatus = _FsLsppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 47),
    _FsLsppRowStatus_Type()
)
fsLsppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLsppRowStatus.setStatus("current")


class _FsLsppStatusPathDirection_Type(Integer32):
    """Custom type fsLsppStatusPathDirection based on Integer32"""
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
        *(("forward", 1),
          ("reverse", 2),
          ("both", 3))
    )


_FsLsppStatusPathDirection_Type.__name__ = "Integer32"
_FsLsppStatusPathDirection_Object = MibTableColumn
fsLsppStatusPathDirection = _FsLsppStatusPathDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 48),
    _FsLsppStatusPathDirection_Type()
)
fsLsppStatusPathDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppStatusPathDirection.setStatus("current")


class _FsLsppResponderIcc_Type(OctetString):
    """Custom type fsLsppResponderIcc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsLsppResponderIcc_Type.__name__ = "OctetString"
_FsLsppResponderIcc_Object = MibTableColumn
fsLsppResponderIcc = _FsLsppResponderIcc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 49),
    _FsLsppResponderIcc_Type()
)
fsLsppResponderIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderIcc.setStatus("current")


class _FsLsppResponderUMC_Type(OctetString):
    """Custom type fsLsppResponderUMC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_FsLsppResponderUMC_Type.__name__ = "OctetString"
_FsLsppResponderUMC_Object = MibTableColumn
fsLsppResponderUMC = _FsLsppResponderUMC_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 50),
    _FsLsppResponderUMC_Type()
)
fsLsppResponderUMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderUMC.setStatus("current")
_FsLsppResponderMepIndex_Type = Unsigned32
_FsLsppResponderMepIndex_Object = MibTableColumn
fsLsppResponderMepIndex = _FsLsppResponderMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 1, 1, 51),
    _FsLsppResponderMepIndex_Type()
)
fsLsppResponderMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppResponderMepIndex.setStatus("current")
_FsLsppEchoSequenceTable_Object = MibTable
fsLsppEchoSequenceTable = _FsLsppEchoSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2)
)
if mibBuilder.loadTexts:
    fsLsppEchoSequenceTable.setStatus("current")
_FsLsppEchoSequenceTableEntry_Object = MibTableRow
fsLsppEchoSequenceTableEntry = _FsLsppEchoSequenceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2, 1)
)
fsLsppEchoSequenceTableEntry.setIndexNames(
    (0, "ARICENT-LSP-PING-MIB", "fsLsppContextId"),
    (0, "ARICENT-LSP-PING-MIB", "fsLsppSenderHandle"),
    (0, "ARICENT-LSP-PING-MIB", "fsLsppSequenceNumber"),
)
if mibBuilder.loadTexts:
    fsLsppEchoSequenceTableEntry.setStatus("current")
_FsLsppSequenceNumber_Type = Unsigned32
_FsLsppSequenceNumber_Object = MibTableColumn
fsLsppSequenceNumber = _FsLsppSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2, 1, 1),
    _FsLsppSequenceNumber_Type()
)
fsLsppSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLsppSequenceNumber.setStatus("current")
_FsLsppReturnCode_Type = Unsigned32
_FsLsppReturnCode_Object = MibTableColumn
fsLsppReturnCode = _FsLsppReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2, 1, 2),
    _FsLsppReturnCode_Type()
)
fsLsppReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppReturnCode.setStatus("current")
_FsLsppReturnSubCode_Type = Unsigned32
_FsLsppReturnSubCode_Object = MibTableColumn
fsLsppReturnSubCode = _FsLsppReturnSubCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2, 1, 3),
    _FsLsppReturnSubCode_Type()
)
fsLsppReturnSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppReturnSubCode.setStatus("current")


class _FsLsppReturnCodeStr_Type(OctetString):
    """Custom type fsLsppReturnCodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsLsppReturnCodeStr_Type.__name__ = "OctetString"
_FsLsppReturnCodeStr_Object = MibTableColumn
fsLsppReturnCodeStr = _FsLsppReturnCodeStr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 2, 1, 4),
    _FsLsppReturnCodeStr_Type()
)
fsLsppReturnCodeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppReturnCodeStr.setStatus("current")
_FsLsppHopTable_Object = MibTable
fsLsppHopTable = _FsLsppHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3)
)
if mibBuilder.loadTexts:
    fsLsppHopTable.setStatus("current")
_FsLsppHopTableEntry_Object = MibTableRow
fsLsppHopTableEntry = _FsLsppHopTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1)
)
fsLsppHopTableEntry.setIndexNames(
    (0, "ARICENT-LSP-PING-MIB", "fsLsppContextId"),
    (0, "ARICENT-LSP-PING-MIB", "fsLsppSenderHandle"),
    (0, "ARICENT-LSP-PING-MIB", "fsLsppHopIndex"),
)
if mibBuilder.loadTexts:
    fsLsppHopTableEntry.setStatus("current")
_FsLsppHopIndex_Type = Unsigned32
_FsLsppHopIndex_Object = MibTableColumn
fsLsppHopIndex = _FsLsppHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 1),
    _FsLsppHopIndex_Type()
)
fsLsppHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLsppHopIndex.setStatus("current")
_FsLsppHopAddrType_Type = FsLsppAddressType
_FsLsppHopAddrType_Object = MibTableColumn
fsLsppHopAddrType = _FsLsppHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 2),
    _FsLsppHopAddrType_Type()
)
fsLsppHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopAddrType.setStatus("current")


class _FsLsppHopAddr_Type(OctetString):
    """Custom type fsLsppHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppHopAddr_Type.__name__ = "OctetString"
_FsLsppHopAddr_Object = MibTableColumn
fsLsppHopAddr = _FsLsppHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 3),
    _FsLsppHopAddr_Type()
)
fsLsppHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopAddr.setStatus("current")
_FsLsppHopGlobalId_Type = Unsigned32
_FsLsppHopGlobalId_Object = MibTableColumn
fsLsppHopGlobalId = _FsLsppHopGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 4),
    _FsLsppHopGlobalId_Type()
)
fsLsppHopGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopGlobalId.setStatus("current")
_FsLsppHopId_Type = Unsigned32
_FsLsppHopId_Object = MibTableColumn
fsLsppHopId = _FsLsppHopId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 5),
    _FsLsppHopId_Type()
)
fsLsppHopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopId.setStatus("current")
_FsLsppHopIfNum_Type = Unsigned32
_FsLsppHopIfNum_Object = MibTableColumn
fsLsppHopIfNum = _FsLsppHopIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 6),
    _FsLsppHopIfNum_Type()
)
fsLsppHopIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopIfNum.setStatus("current")
_FsLsppHopReturnCode_Type = Unsigned32
_FsLsppHopReturnCode_Object = MibTableColumn
fsLsppHopReturnCode = _FsLsppHopReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 7),
    _FsLsppHopReturnCode_Type()
)
fsLsppHopReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopReturnCode.setStatus("current")
_FsLsppHopReturnSubCode_Type = Unsigned32
_FsLsppHopReturnSubCode_Object = MibTableColumn
fsLsppHopReturnSubCode = _FsLsppHopReturnSubCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 8),
    _FsLsppHopReturnSubCode_Type()
)
fsLsppHopReturnSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopReturnSubCode.setStatus("current")


class _FsLsppHopReturnCodeStr_Type(OctetString):
    """Custom type fsLsppHopReturnCodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsLsppHopReturnCodeStr_Type.__name__ = "OctetString"
_FsLsppHopReturnCodeStr_Object = MibTableColumn
fsLsppHopReturnCodeStr = _FsLsppHopReturnCodeStr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 9),
    _FsLsppHopReturnCodeStr_Type()
)
fsLsppHopReturnCodeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopReturnCodeStr.setStatus("current")
_FsLsppHopRxAddrType_Type = FsLsppAddressType
_FsLsppHopRxAddrType_Object = MibTableColumn
fsLsppHopRxAddrType = _FsLsppHopRxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 10),
    _FsLsppHopRxAddrType_Type()
)
fsLsppHopRxAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxAddrType.setStatus("current")


class _FsLsppHopRxIPAddr_Type(OctetString):
    """Custom type fsLsppHopRxIPAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppHopRxIPAddr_Type.__name__ = "OctetString"
_FsLsppHopRxIPAddr_Object = MibTableColumn
fsLsppHopRxIPAddr = _FsLsppHopRxIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 11),
    _FsLsppHopRxIPAddr_Type()
)
fsLsppHopRxIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxIPAddr.setStatus("current")


class _FsLsppHopRxIfAddr_Type(OctetString):
    """Custom type fsLsppHopRxIfAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppHopRxIfAddr_Type.__name__ = "OctetString"
_FsLsppHopRxIfAddr_Object = MibTableColumn
fsLsppHopRxIfAddr = _FsLsppHopRxIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 12),
    _FsLsppHopRxIfAddr_Type()
)
fsLsppHopRxIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxIfAddr.setStatus("current")
_FsLsppHopRxIfNum_Type = Unsigned32
_FsLsppHopRxIfNum_Object = MibTableColumn
fsLsppHopRxIfNum = _FsLsppHopRxIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 13),
    _FsLsppHopRxIfNum_Type()
)
fsLsppHopRxIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxIfNum.setStatus("current")
_FsLsppHopRxLabelStack_Type = OctetString
_FsLsppHopRxLabelStack_Object = MibTableColumn
fsLsppHopRxLabelStack = _FsLsppHopRxLabelStack_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 14),
    _FsLsppHopRxLabelStack_Type()
)
fsLsppHopRxLabelStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxLabelStack.setStatus("current")
_FsLsppHopRxLabelExp_Type = OctetString
_FsLsppHopRxLabelExp_Object = MibTableColumn
fsLsppHopRxLabelExp = _FsLsppHopRxLabelExp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 15),
    _FsLsppHopRxLabelExp_Type()
)
fsLsppHopRxLabelExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRxLabelExp.setStatus("current")
_FsLsppHopRtt_Type = Unsigned32
_FsLsppHopRtt_Object = MibTableColumn
fsLsppHopRtt = _FsLsppHopRtt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 16),
    _FsLsppHopRtt_Type()
)
fsLsppHopRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopRtt.setStatus("current")
_FsLsppHopDsMtu_Type = Unsigned32
_FsLsppHopDsMtu_Object = MibTableColumn
fsLsppHopDsMtu = _FsLsppHopDsMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 17),
    _FsLsppHopDsMtu_Type()
)
fsLsppHopDsMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsMtu.setStatus("current")
_FsLsppHopDsAddrType_Type = FsLsppAddressType
_FsLsppHopDsAddrType_Object = MibTableColumn
fsLsppHopDsAddrType = _FsLsppHopDsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 18),
    _FsLsppHopDsAddrType_Type()
)
fsLsppHopDsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsAddrType.setStatus("current")


class _FsLsppHopDsIPAddr_Type(OctetString):
    """Custom type fsLsppHopDsIPAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppHopDsIPAddr_Type.__name__ = "OctetString"
_FsLsppHopDsIPAddr_Object = MibTableColumn
fsLsppHopDsIPAddr = _FsLsppHopDsIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 19),
    _FsLsppHopDsIPAddr_Type()
)
fsLsppHopDsIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsIPAddr.setStatus("current")


class _FsLsppHopDsIfAddr_Type(OctetString):
    """Custom type fsLsppHopDsIfAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsLsppHopDsIfAddr_Type.__name__ = "OctetString"
_FsLsppHopDsIfAddr_Object = MibTableColumn
fsLsppHopDsIfAddr = _FsLsppHopDsIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 20),
    _FsLsppHopDsIfAddr_Type()
)
fsLsppHopDsIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsIfAddr.setStatus("current")
_FsLsppHopDsIfNum_Type = Unsigned32
_FsLsppHopDsIfNum_Object = MibTableColumn
fsLsppHopDsIfNum = _FsLsppHopDsIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 21),
    _FsLsppHopDsIfNum_Type()
)
fsLsppHopDsIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsIfNum.setStatus("current")
_FsLsppHopDsLabelStack_Type = OctetString
_FsLsppHopDsLabelStack_Object = MibTableColumn
fsLsppHopDsLabelStack = _FsLsppHopDsLabelStack_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 22),
    _FsLsppHopDsLabelStack_Type()
)
fsLsppHopDsLabelStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsLabelStack.setStatus("current")
_FsLsppHopDsLabelExp_Type = OctetString
_FsLsppHopDsLabelExp_Object = MibTableColumn
fsLsppHopDsLabelExp = _FsLsppHopDsLabelExp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 23),
    _FsLsppHopDsLabelExp_Type()
)
fsLsppHopDsLabelExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopDsLabelExp.setStatus("current")


class _FsLsppHopIcc_Type(OctetString):
    """Custom type fsLsppHopIcc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsLsppHopIcc_Type.__name__ = "OctetString"
_FsLsppHopIcc_Object = MibTableColumn
fsLsppHopIcc = _FsLsppHopIcc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 24),
    _FsLsppHopIcc_Type()
)
fsLsppHopIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopIcc.setStatus("current")


class _FsLsppHopUMC_Type(OctetString):
    """Custom type fsLsppHopUMC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_FsLsppHopUMC_Type.__name__ = "OctetString"
_FsLsppHopUMC_Object = MibTableColumn
fsLsppHopUMC = _FsLsppHopUMC_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 25),
    _FsLsppHopUMC_Type()
)
fsLsppHopUMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopUMC.setStatus("current")
_FsLsppHopMepIndex_Type = Unsigned32
_FsLsppHopMepIndex_Object = MibTableColumn
fsLsppHopMepIndex = _FsLsppHopMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 2, 3, 1, 26),
    _FsLsppHopMepIndex_Type()
)
fsLsppHopMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLsppHopMepIndex.setStatus("current")
_FsLsppNotifications_ObjectIdentity = ObjectIdentity
fsLsppNotifications = _FsLsppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3)
)
_FsLsppTraps_ObjectIdentity = ObjectIdentity
fsLsppTraps = _FsLsppTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3, 0)
)


class _FsLsppTrapContextName_Type(DisplayString):
    """Custom type fsLsppTrapContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsLsppTrapContextName_Type.__name__ = "DisplayString"
_FsLsppTrapContextName_Object = MibScalar
fsLsppTrapContextName = _FsLsppTrapContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3, 1),
    _FsLsppTrapContextName_Type()
)
fsLsppTrapContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsLsppTrapContextName.setStatus("current")

# Managed Objects groups


# Notification objects

fsLsppPingCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3, 0, 1)
)
fsLsppPingCompletionTrap.setObjects(
      *(("ARICENT-LSP-PING-MIB", "fsLsppTrapContextName"),
        ("ARICENT-LSP-PING-MIB", "fsLsppStatus"))
)
if mibBuilder.loadTexts:
    fsLsppPingCompletionTrap.setStatus(
        "current"
    )

fsLsppTraceRouteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3, 0, 2)
)
fsLsppTraceRouteTrap.setObjects(
      *(("ARICENT-LSP-PING-MIB", "fsLsppTrapContextName"),
        ("ARICENT-LSP-PING-MIB", "fsLsppStatus"),
        ("ARICENT-LSP-PING-MIB", "fsLsppActualHopCount"))
)
if mibBuilder.loadTexts:
    fsLsppTraceRouteTrap.setStatus(
        "current"
    )

fsLsppBFDBootstrapReqRcvdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 13, 11, 3, 0, 3)
)
fsLsppBFDBootstrapReqRcvdTrap.setObjects(
      *(("ARICENT-LSP-PING-MIB", "fsLsppTrapContextName"),
        ("ARICENT-LSP-PING-MIB", "fsLsppRequestOwner"))
)
if mibBuilder.loadTexts:
    fsLsppBFDBootstrapReqRcvdTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LSP-PING-MIB",
    **{"FsLsppTimeUnit": FsLsppTimeUnit,
       "FsLsppAddressType": FsLsppAddressType,
       "fsLspp": fsLspp,
       "fsLsppGlobals": fsLsppGlobals,
       "fsLsppGlobalConfigTable": fsLsppGlobalConfigTable,
       "fsLsppGlobalConfigTableEntry": fsLsppGlobalConfigTableEntry,
       "fsLsppContextId": fsLsppContextId,
       "fsLsppSystemControl": fsLsppSystemControl,
       "fsLsppTrapStatus": fsLsppTrapStatus,
       "fsLsppTraceLevel": fsLsppTraceLevel,
       "fsLsppAgeOutTime": fsLsppAgeOutTime,
       "fsLsppAgeOutTmrUnit": fsLsppAgeOutTmrUnit,
       "fsLsppClearEchoStats": fsLsppClearEchoStats,
       "fsLsppBfdBtStrapRespReq": fsLsppBfdBtStrapRespReq,
       "fsLsppBfdBtStrapAgeOutTime": fsLsppBfdBtStrapAgeOutTime,
       "fsLsppBfdBtStrapAgeOutTmrUnit": fsLsppBfdBtStrapAgeOutTmrUnit,
       "fsLsppGlobalStatsTable": fsLsppGlobalStatsTable,
       "fsLsppGlobalStatsTableEntry": fsLsppGlobalStatsTableEntry,
       "fsLsppGlbStatReqTx": fsLsppGlbStatReqTx,
       "fsLsppGlbStatReqRx": fsLsppGlbStatReqRx,
       "fsLsppGlbStatReqTimedOut": fsLsppGlbStatReqTimedOut,
       "fsLsppGlbStatReqUnSent": fsLsppGlbStatReqUnSent,
       "fsLsppGlbStatReplyTx": fsLsppGlbStatReplyTx,
       "fsLsppGlbStatReplyRx": fsLsppGlbStatReplyRx,
       "fsLsppGlbStatReplyDropped": fsLsppGlbStatReplyDropped,
       "fsLsppGlbStatReplyUnSent": fsLsppGlbStatReplyUnSent,
       "fsLsppGlbStatReplyFromEgr": fsLsppGlbStatReplyFromEgr,
       "fsLsppGlbStatUnLbldOutIf": fsLsppGlbStatUnLbldOutIf,
       "fsLsppGlbStatDsMapMismatch": fsLsppGlbStatDsMapMismatch,
       "fsLsppGlbStatFecLblMismatch": fsLsppGlbStatFecLblMismatch,
       "fsLsppGlbStatNoFecMapping": fsLsppGlbStatNoFecMapping,
       "fsLsppGlbStatUnKUpstreamIf": fsLsppGlbStatUnKUpstreamIf,
       "fsLsppGlbStatReqLblSwitched": fsLsppGlbStatReqLblSwitched,
       "fsLsppGlbStatReqUnSupptdTlv": fsLsppGlbStatReqUnSupptdTlv,
       "fsLsppGlbStatMalformedReq": fsLsppGlbStatMalformedReq,
       "fsLsppGlbStatNoLblEntry": fsLsppGlbStatNoLblEntry,
       "fsLsppGlbStatPreTermReq": fsLsppGlbStatPreTermReq,
       "fsLsppGlbStatProtMismatch": fsLsppGlbStatProtMismatch,
       "fsLsppGlbStatRsvdRetCode": fsLsppGlbStatRsvdRetCode,
       "fsLsppGlbStatNoRetCode": fsLsppGlbStatNoRetCode,
       "fsLsppGlbStatUndefRetCode": fsLsppGlbStatUndefRetCode,
       "fsLsppGlbStatInvalidPktDropped": fsLsppGlbStatInvalidPktDropped,
       "fsLsppPingTrace": fsLsppPingTrace,
       "fsLsppPingTraceTable": fsLsppPingTraceTable,
       "fsLsppPingTraceTableEntry": fsLsppPingTraceTableEntry,
       "fsLsppSenderHandle": fsLsppSenderHandle,
       "fsLsppRequestType": fsLsppRequestType,
       "fsLsppRequestOwner": fsLsppRequestOwner,
       "fsLsppPathType": fsLsppPathType,
       "fsLsppPathPointer": fsLsppPathPointer,
       "fsLsppTgtMipGlobalId": fsLsppTgtMipGlobalId,
       "fsLsppTgtMipNodeId": fsLsppTgtMipNodeId,
       "fsLsppTgtMipIfNum": fsLsppTgtMipIfNum,
       "fsLsppReplyMode": fsLsppReplyMode,
       "fsLsppRepeatCount": fsLsppRepeatCount,
       "fsLsppPacketSize": fsLsppPacketSize,
       "fsLsppPadPattern": fsLsppPadPattern,
       "fsLsppTTLValue": fsLsppTTLValue,
       "fsLsppWFRInterval": fsLsppWFRInterval,
       "fsLsppWFRTmrUnit": fsLsppWFRTmrUnit,
       "fsLsppWTSInterval": fsLsppWTSInterval,
       "fsLsppWTSTmrUnit": fsLsppWTSTmrUnit,
       "fsLsppReplyDscpValue": fsLsppReplyDscpValue,
       "fsLsppSweepOption": fsLsppSweepOption,
       "fsLsppSweepMinimum": fsLsppSweepMinimum,
       "fsLsppSweepMaximum": fsLsppSweepMaximum,
       "fsLsppSweepIncrement": fsLsppSweepIncrement,
       "fsLsppBurstOption": fsLsppBurstOption,
       "fsLsppBurstSize": fsLsppBurstSize,
       "fsLsppEXPValue": fsLsppEXPValue,
       "fsLsppDsMap": fsLsppDsMap,
       "fsLsppFecValidate": fsLsppFecValidate,
       "fsLsppReplyPadTlv": fsLsppReplyPadTlv,
       "fsLsppForceExplicitNull": fsLsppForceExplicitNull,
       "fsLsppInterfaceLabelTlv": fsLsppInterfaceLabelTlv,
       "fsLsppSameSeqNumOption": fsLsppSameSeqNumOption,
       "fsLsppVerbose": fsLsppVerbose,
       "fsLsppReversePathVerify": fsLsppReversePathVerify,
       "fsLsppEncapType": fsLsppEncapType,
       "fsLsppStatus": fsLsppStatus,
       "fsLsppActualHopCount": fsLsppActualHopCount,
       "fsLsppResponderAddrType": fsLsppResponderAddrType,
       "fsLsppResponderAddr": fsLsppResponderAddr,
       "fsLsppResponderGlobalId": fsLsppResponderGlobalId,
       "fsLsppResponderId": fsLsppResponderId,
       "fsLsppMaxRtt": fsLsppMaxRtt,
       "fsLsppMinRtt": fsLsppMinRtt,
       "fsLsppAverageRtt": fsLsppAverageRtt,
       "fsLsppPktsTx": fsLsppPktsTx,
       "fsLsppPktsRx": fsLsppPktsRx,
       "fsLsppPktsUnSent": fsLsppPktsUnSent,
       "fsLsppRowStatus": fsLsppRowStatus,
       "fsLsppStatusPathDirection": fsLsppStatusPathDirection,
       "fsLsppResponderIcc": fsLsppResponderIcc,
       "fsLsppResponderUMC": fsLsppResponderUMC,
       "fsLsppResponderMepIndex": fsLsppResponderMepIndex,
       "fsLsppEchoSequenceTable": fsLsppEchoSequenceTable,
       "fsLsppEchoSequenceTableEntry": fsLsppEchoSequenceTableEntry,
       "fsLsppSequenceNumber": fsLsppSequenceNumber,
       "fsLsppReturnCode": fsLsppReturnCode,
       "fsLsppReturnSubCode": fsLsppReturnSubCode,
       "fsLsppReturnCodeStr": fsLsppReturnCodeStr,
       "fsLsppHopTable": fsLsppHopTable,
       "fsLsppHopTableEntry": fsLsppHopTableEntry,
       "fsLsppHopIndex": fsLsppHopIndex,
       "fsLsppHopAddrType": fsLsppHopAddrType,
       "fsLsppHopAddr": fsLsppHopAddr,
       "fsLsppHopGlobalId": fsLsppHopGlobalId,
       "fsLsppHopId": fsLsppHopId,
       "fsLsppHopIfNum": fsLsppHopIfNum,
       "fsLsppHopReturnCode": fsLsppHopReturnCode,
       "fsLsppHopReturnSubCode": fsLsppHopReturnSubCode,
       "fsLsppHopReturnCodeStr": fsLsppHopReturnCodeStr,
       "fsLsppHopRxAddrType": fsLsppHopRxAddrType,
       "fsLsppHopRxIPAddr": fsLsppHopRxIPAddr,
       "fsLsppHopRxIfAddr": fsLsppHopRxIfAddr,
       "fsLsppHopRxIfNum": fsLsppHopRxIfNum,
       "fsLsppHopRxLabelStack": fsLsppHopRxLabelStack,
       "fsLsppHopRxLabelExp": fsLsppHopRxLabelExp,
       "fsLsppHopRtt": fsLsppHopRtt,
       "fsLsppHopDsMtu": fsLsppHopDsMtu,
       "fsLsppHopDsAddrType": fsLsppHopDsAddrType,
       "fsLsppHopDsIPAddr": fsLsppHopDsIPAddr,
       "fsLsppHopDsIfAddr": fsLsppHopDsIfAddr,
       "fsLsppHopDsIfNum": fsLsppHopDsIfNum,
       "fsLsppHopDsLabelStack": fsLsppHopDsLabelStack,
       "fsLsppHopDsLabelExp": fsLsppHopDsLabelExp,
       "fsLsppHopIcc": fsLsppHopIcc,
       "fsLsppHopUMC": fsLsppHopUMC,
       "fsLsppHopMepIndex": fsLsppHopMepIndex,
       "fsLsppNotifications": fsLsppNotifications,
       "fsLsppTraps": fsLsppTraps,
       "fsLsppPingCompletionTrap": fsLsppPingCompletionTrap,
       "fsLsppTraceRouteTrap": fsLsppTraceRouteTrap,
       "fsLsppBFDBootstrapReqRcvdTrap": fsLsppBFDBootstrapReqRcvdTrap,
       "fsLsppTrapContextName": fsLsppTrapContextName}
)
