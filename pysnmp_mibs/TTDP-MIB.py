# SNMP MIB module (TTDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/TTDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:21 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

iec61375 = ModuleIdentity(
    (1, 0, 61375, 2)
)
if mibBuilder.loadTexts:
    iec61375.setRevisions(
        ("2016-06-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TtdpPhysicalLineId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(45,
              65,
              66,
              67,
              68)
        )
    )
    namedValues = NamedValues(
        *(("lineNone", 45),
          ("lineA", 65),
          ("lineB", 66),
          ("lineC", 67),
          ("lineD", 68))
    )



class TtdpOrientation(TextualConvention, Integer32):
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
        *(("direct", 1),
          ("inverse", 2),
          ("undefined", 3))
    )



class Antivalent2(TextualConvention, Integer32):
    status = "current"
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
        *(("error", 0),
          ("false", 1),
          ("true", 2),
          ("undefined", 3))
    )



class TtdpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dir1", 1),
          ("dir2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Std_ObjectIdentity = ObjectIdentity
std = _Std_ObjectIdentity(
    (1, 0)
)
_Stdx61375_ObjectIdentity = ObjectIdentity
stdx61375 = _Stdx61375_ObjectIdentity(
    (1, 0, 61375)
)
_Ttdp_ObjectIdentity = ObjectIdentity
ttdp = _Ttdp_ObjectIdentity(
    (1, 0, 61375, 2, 5)
)
_TtdpObjects_ObjectIdentity = ObjectIdentity
ttdpObjects = _TtdpObjects_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1)
)
_TtdpGenInfo_ObjectIdentity = ObjectIdentity
ttdpGenInfo = _TtdpGenInfo_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1, 1)
)
_TtdpVersion_Type = Unsigned32
_TtdpVersion_Object = MibScalar
ttdpVersion = _TtdpVersion_Object(
    (1, 0, 61375, 2, 5, 1, 1, 1),
    _TtdpVersion_Type()
)
ttdpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpVersion.setStatus("current")
_TtdpSlowTimeout_Type = Unsigned32
_TtdpSlowTimeout_Object = MibScalar
ttdpSlowTimeout = _TtdpSlowTimeout_Object(
    (1, 0, 61375, 2, 5, 1, 1, 2),
    _TtdpSlowTimeout_Type()
)
ttdpSlowTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpSlowTimeout.setStatus("current")
_TtdpFastTimeout_Type = Unsigned32
_TtdpFastTimeout_Object = MibScalar
ttdpFastTimeout = _TtdpFastTimeout_Object(
    (1, 0, 61375, 2, 5, 1, 1, 3),
    _TtdpFastTimeout_Type()
)
ttdpFastTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpFastTimeout.setStatus("current")
_TtdpTopoTtl_Type = Unsigned32
_TtdpTopoTtl_Object = MibScalar
ttdpTopoTtl = _TtdpTopoTtl_Object(
    (1, 0, 61375, 2, 5, 1, 1, 4),
    _TtdpTopoTtl_Type()
)
ttdpTopoTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpTopoTtl.setStatus("current")
_TtdpGlobalTopoTimeout_Type = Unsigned32
_TtdpGlobalTopoTimeout_Object = MibScalar
ttdpGlobalTopoTimeout = _TtdpGlobalTopoTimeout_Object(
    (1, 0, 61375, 2, 5, 1, 1, 5),
    _TtdpGlobalTopoTimeout_Type()
)
ttdpGlobalTopoTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpGlobalTopoTimeout.setStatus("current")
_TtdpLinksInfo_ObjectIdentity = ObjectIdentity
ttdpLinksInfo = _TtdpLinksInfo_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1, 3)
)


class _TtdpLogicalLinksNb_Type(Unsigned32):
    """Custom type ttdpLogicalLinksNb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_TtdpLogicalLinksNb_Type.__name__ = "Unsigned32"
_TtdpLogicalLinksNb_Object = MibScalar
ttdpLogicalLinksNb = _TtdpLogicalLinksNb_Object(
    (1, 0, 61375, 2, 5, 1, 3, 1),
    _TtdpLogicalLinksNb_Type()
)
ttdpLogicalLinksNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLogicalLinksNb.setStatus("current")
_TtdpLogicalLinksTable_Object = MibTable
ttdpLogicalLinksTable = _TtdpLogicalLinksTable_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ttdpLogicalLinksTable.setStatus("current")
_TtdpLogicalLinksEntry_Object = MibTableRow
ttdpLogicalLinksEntry = _TtdpLogicalLinksEntry_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2, 1)
)
ttdpLogicalLinksEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpLogicalLinksIdx"),
)
if mibBuilder.loadTexts:
    ttdpLogicalLinksEntry.setStatus("current")
_TtdpLogicalLinksIdx_Type = TtdpDirection
_TtdpLogicalLinksIdx_Object = MibTableColumn
ttdpLogicalLinksIdx = _TtdpLogicalLinksIdx_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2, 1, 1),
    _TtdpLogicalLinksIdx_Type()
)
ttdpLogicalLinksIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLogicalLinksIdx.setStatus("current")


class _TtdpConfiguredPhysLinesNb_Type(Unsigned32):
    """Custom type ttdpConfiguredPhysLinesNb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TtdpConfiguredPhysLinesNb_Type.__name__ = "Unsigned32"
_TtdpConfiguredPhysLinesNb_Object = MibTableColumn
ttdpConfiguredPhysLinesNb = _TtdpConfiguredPhysLinesNb_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2, 1, 2),
    _TtdpConfiguredPhysLinesNb_Type()
)
ttdpConfiguredPhysLinesNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpConfiguredPhysLinesNb.setStatus("current")


class _TtdpActivePhysLinesNb_Type(Unsigned32):
    """Custom type ttdpActivePhysLinesNb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TtdpActivePhysLinesNb_Type.__name__ = "Unsigned32"
_TtdpActivePhysLinesNb_Object = MibTableColumn
ttdpActivePhysLinesNb = _TtdpActivePhysLinesNb_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2, 1, 3),
    _TtdpActivePhysLinesNb_Type()
)
ttdpActivePhysLinesNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpActivePhysLinesNb.setStatus("current")
_TtdpIsEndLink_Type = TruthValue
_TtdpIsEndLink_Object = MibTableColumn
ttdpIsEndLink = _TtdpIsEndLink_Object(
    (1, 0, 61375, 2, 5, 1, 3, 2, 1, 4),
    _TtdpIsEndLink_Type()
)
ttdpIsEndLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpIsEndLink.setStatus("current")
_TtdpPhysicalLinesTable_Object = MibTable
ttdpPhysicalLinesTable = _TtdpPhysicalLinesTable_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ttdpPhysicalLinesTable.setStatus("current")
_TtdpPhysicalLinesEntry_Object = MibTableRow
ttdpPhysicalLinesEntry = _TtdpPhysicalLinesEntry_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3, 1)
)
ttdpPhysicalLinesEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpLogicalLinksIdx"),
    (0, "TTDP-MIB", "ttdpPhysicalLinesIdx"),
)
if mibBuilder.loadTexts:
    ttdpPhysicalLinesEntry.setStatus("current")
_TtdpPhysicalLinesIdx_Type = TtdpPhysicalLineId
_TtdpPhysicalLinesIdx_Object = MibTableColumn
ttdpPhysicalLinesIdx = _TtdpPhysicalLinesIdx_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3, 1, 1),
    _TtdpPhysicalLinesIdx_Type()
)
ttdpPhysicalLinesIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpPhysicalLinesIdx.setStatus("current")


class _TtdpPortState_Type(Integer32):
    """Custom type ttdpPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("forwarding", 2),
          ("discarding", 3))
    )


_TtdpPortState_Type.__name__ = "Integer32"
_TtdpPortState_Object = MibTableColumn
ttdpPortState = _TtdpPortState_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3, 1, 2),
    _TtdpPortState_Type()
)
ttdpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpPortState.setStatus("current")


class _TtdpLineRcvState_Type(Integer32):
    """Custom type ttdpLineRcvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineNotOK", 1),
          ("lineOK", 2),
          ("notAvailable", 3))
    )


_TtdpLineRcvState_Type.__name__ = "Integer32"
_TtdpLineRcvState_Object = MibTableColumn
ttdpLineRcvState = _TtdpLineRcvState_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3, 1, 3),
    _TtdpLineRcvState_Type()
)
ttdpLineRcvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLineRcvState.setStatus("current")
_TtdpPeerLineId_Type = TtdpPhysicalLineId
_TtdpPeerLineId_Object = MibTableColumn
ttdpPeerLineId = _TtdpPeerLineId_Object(
    (1, 0, 61375, 2, 5, 1, 3, 3, 1, 4),
    _TtdpPeerLineId_Type()
)
ttdpPeerLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpPeerLineId.setStatus("current")
_TtdpPhysicalLinesStatsTable_Object = MibTable
ttdpPhysicalLinesStatsTable = _TtdpPhysicalLinesStatsTable_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ttdpPhysicalLinesStatsTable.setStatus("current")
_TtdpPhysicalLinesStatsEntry_Object = MibTableRow
ttdpPhysicalLinesStatsEntry = _TtdpPhysicalLinesStatsEntry_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4, 1)
)
ttdpPhysicalLinesStatsEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpLogicalLinksIdx"),
    (0, "TTDP-MIB", "ttdpPhysicalLinesIdx"),
)
if mibBuilder.loadTexts:
    ttdpPhysicalLinesStatsEntry.setStatus("current")
_TtdpHelloSentFrames_Type = Integer32
_TtdpHelloSentFrames_Object = MibTableColumn
ttdpHelloSentFrames = _TtdpHelloSentFrames_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4, 1, 1),
    _TtdpHelloSentFrames_Type()
)
ttdpHelloSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpHelloSentFrames.setStatus("current")
_TtdpHelloReceivedFrames_Type = Integer32
_TtdpHelloReceivedFrames_Object = MibTableColumn
ttdpHelloReceivedFrames = _TtdpHelloReceivedFrames_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4, 1, 2),
    _TtdpHelloReceivedFrames_Type()
)
ttdpHelloReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpHelloReceivedFrames.setStatus("current")
_TtdpRemoteFastModeCnt_Type = Integer32
_TtdpRemoteFastModeCnt_Object = MibTableColumn
ttdpRemoteFastModeCnt = _TtdpRemoteFastModeCnt_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4, 1, 3),
    _TtdpRemoteFastModeCnt_Type()
)
ttdpRemoteFastModeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpRemoteFastModeCnt.setStatus("current")
_TtdpLocalFastModeCnt_Type = Integer32
_TtdpLocalFastModeCnt_Object = MibTableColumn
ttdpLocalFastModeCnt = _TtdpLocalFastModeCnt_Object(
    (1, 0, 61375, 2, 5, 1, 3, 4, 1, 4),
    _TtdpLocalFastModeCnt_Type()
)
ttdpLocalFastModeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLocalFastModeCnt.setStatus("current")
_TtdpTopoInfo_ObjectIdentity = ObjectIdentity
ttdpTopoInfo = _TtdpTopoInfo_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1, 5)
)
_TtdpLocalEtbnInfo_ObjectIdentity = ObjectIdentity
ttdpLocalEtbnInfo = _TtdpLocalEtbnInfo_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1, 5, 1)
)


class _TtdpEtbId_Type(Unsigned32):
    """Custom type ttdpEtbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TtdpEtbId_Type.__name__ = "Unsigned32"
_TtdpEtbId_Object = MibScalar
ttdpEtbId = _TtdpEtbId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 1),
    _TtdpEtbId_Type()
)
ttdpEtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbId.setStatus("current")
_TtdpLocalEtbnMacAddr_Type = MacAddress
_TtdpLocalEtbnMacAddr_Object = MibScalar
ttdpLocalEtbnMacAddr = _TtdpLocalEtbnMacAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 2),
    _TtdpLocalEtbnMacAddr_Type()
)
ttdpLocalEtbnMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLocalEtbnMacAddr.setStatus("current")


class _TtdpLocalEtbnId_Type(Unsigned32):
    """Custom type ttdpLocalEtbnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpLocalEtbnId_Type.__name__ = "Unsigned32"
_TtdpLocalEtbnId_Object = MibScalar
ttdpLocalEtbnId = _TtdpLocalEtbnId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 3),
    _TtdpLocalEtbnId_Type()
)
ttdpLocalEtbnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLocalEtbnId.setStatus("current")


class _TtdpNodePosition_Type(Integer32):
    """Custom type ttdpNodePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 0),
          ("extremity1", 1),
          ("extremity2", 2))
    )


_TtdpNodePosition_Type.__name__ = "Integer32"
_TtdpNodePosition_Object = MibScalar
ttdpNodePosition = _TtdpNodePosition_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 4),
    _TtdpNodePosition_Type()
)
ttdpNodePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpNodePosition.setStatus("current")
_TtdpIsAlone_Type = TruthValue
_TtdpIsAlone_Object = MibScalar
ttdpIsAlone = _TtdpIsAlone_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 5),
    _TtdpIsAlone_Type()
)
ttdpIsAlone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpIsAlone.setStatus("current")
_TtdpConnTableValid_Type = TruthValue
_TtdpConnTableValid_Object = MibScalar
ttdpConnTableValid = _TtdpConnTableValid_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 6),
    _TtdpConnTableValid_Type()
)
ttdpConnTableValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpConnTableValid.setStatus("current")
_TtdpEtbTopoCntValid_Type = TruthValue
_TtdpEtbTopoCntValid_Object = MibScalar
ttdpEtbTopoCntValid = _TtdpEtbTopoCntValid_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 7),
    _TtdpEtbTopoCntValid_Type()
)
ttdpEtbTopoCntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbTopoCntValid.setStatus("current")
_TtdpTopoFrameStats_ObjectIdentity = ObjectIdentity
ttdpTopoFrameStats = _TtdpTopoFrameStats_ObjectIdentity(
    (1, 0, 61375, 2, 5, 1, 5, 1, 8)
)
_TtdpTopoSentFrames_Type = Integer32
_TtdpTopoSentFrames_Object = MibScalar
ttdpTopoSentFrames = _TtdpTopoSentFrames_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 8, 1),
    _TtdpTopoSentFrames_Type()
)
ttdpTopoSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpTopoSentFrames.setStatus("current")
_TtdpTopoReceivedFrames_Type = Integer32
_TtdpTopoReceivedFrames_Object = MibScalar
ttdpTopoReceivedFrames = _TtdpTopoReceivedFrames_Object(
    (1, 0, 61375, 2, 5, 1, 5, 1, 8, 2),
    _TtdpTopoReceivedFrames_Type()
)
ttdpTopoReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpTopoReceivedFrames.setStatus("current")


class _TtdpEtbnCnt_Type(Unsigned32):
    """Custom type ttdpEtbnCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpEtbnCnt_Type.__name__ = "Unsigned32"
_TtdpEtbnCnt_Object = MibScalar
ttdpEtbnCnt = _TtdpEtbnCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 2),
    _TtdpEtbnCnt_Type()
)
ttdpEtbnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnCnt.setStatus("current")
_TtdpEtbnTable_Object = MibTable
ttdpEtbnTable = _TtdpEtbnTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ttdpEtbnTable.setStatus("current")
_TtdpEtbnEntry_Object = MibTableRow
ttdpEtbnEntry = _TtdpEtbnEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1)
)
ttdpEtbnEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpEtbnTableIdx"),
)
if mibBuilder.loadTexts:
    ttdpEtbnEntry.setStatus("current")


class _TtdpEtbnTableIdx_Type(Unsigned32):
    """Custom type ttdpEtbnTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpEtbnTableIdx_Type.__name__ = "Unsigned32"
_TtdpEtbnTableIdx_Object = MibTableColumn
ttdpEtbnTableIdx = _TtdpEtbnTableIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 1),
    _TtdpEtbnTableIdx_Type()
)
ttdpEtbnTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnTableIdx.setStatus("current")


class _TtdpEtbnId_Type(Unsigned32):
    """Custom type ttdpEtbnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TtdpEtbnId_Type.__name__ = "Unsigned32"
_TtdpEtbnId_Object = MibTableColumn
ttdpEtbnId = _TtdpEtbnId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 2),
    _TtdpEtbnId_Type()
)
ttdpEtbnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnId.setStatus("current")
_TtdpEtbnMacAddr_Type = MacAddress
_TtdpEtbnMacAddr_Object = MibTableColumn
ttdpEtbnMacAddr = _TtdpEtbnMacAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 3),
    _TtdpEtbnMacAddr_Type()
)
ttdpEtbnMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnMacAddr.setStatus("current")
_TtdpEtbnOrientation_Type = TtdpOrientation
_TtdpEtbnOrientation_Object = MibTableColumn
ttdpEtbnOrientation = _TtdpEtbnOrientation_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 4),
    _TtdpEtbnOrientation_Type()
)
ttdpEtbnOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnOrientation.setStatus("current")
_TtdpEtbnIpAddr_Type = IpAddress
_TtdpEtbnIpAddr_Object = MibTableColumn
ttdpEtbnIpAddr = _TtdpEtbnIpAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 5),
    _TtdpEtbnIpAddr_Type()
)
ttdpEtbnIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnIpAddr.setStatus("current")


class _TtdpEtbnNodeRole_Type(Integer32):
    """Custom type ttdpEtbnNodeRole based on Integer32"""
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
        *(("undefined", 0),
          ("master", 1),
          ("backup", 2),
          ("notRedundant", 3))
    )


_TtdpEtbnNodeRole_Type.__name__ = "Integer32"
_TtdpEtbnNodeRole_Object = MibTableColumn
ttdpEtbnNodeRole = _TtdpEtbnNodeRole_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 6),
    _TtdpEtbnNodeRole_Type()
)
ttdpEtbnNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnNodeRole.setStatus("current")


class _TtdpEtbnInaugState_Type(Integer32):
    """Custom type ttdpEtbnInaugState based on Integer32"""
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
        *(("init", 0),
          ("notInaugurated", 1),
          ("inaugurated", 2),
          ("readyForInauguration", 3))
    )


_TtdpEtbnInaugState_Type.__name__ = "Integer32"
_TtdpEtbnInaugState_Object = MibTableColumn
ttdpEtbnInaugState = _TtdpEtbnInaugState_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 7),
    _TtdpEtbnInaugState_Type()
)
ttdpEtbnInaugState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnInaugState.setStatus("current")
_TtdpEtbnInhibit_Type = TruthValue
_TtdpEtbnInhibit_Object = MibTableColumn
ttdpEtbnInhibit = _TtdpEtbnInhibit_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 8),
    _TtdpEtbnInhibit_Type()
)
ttdpEtbnInhibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnInhibit.setStatus("current")
_TtdpRemoteInhibit_Type = TruthValue
_TtdpRemoteInhibit_Object = MibTableColumn
ttdpRemoteInhibit = _TtdpRemoteInhibit_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 9),
    _TtdpRemoteInhibit_Type()
)
ttdpRemoteInhibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpRemoteInhibit.setStatus("current")
_TtdpConnTableCrc32_Type = Unsigned32
_TtdpConnTableCrc32_Object = MibTableColumn
ttdpConnTableCrc32 = _TtdpConnTableCrc32_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 10),
    _TtdpConnTableCrc32_Type()
)
ttdpConnTableCrc32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpConnTableCrc32.setStatus("current")
_TtdpEtbTopoCnt_Type = Unsigned32
_TtdpEtbTopoCnt_Object = MibTableColumn
ttdpEtbTopoCnt = _TtdpEtbTopoCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 11),
    _TtdpEtbTopoCnt_Type()
)
ttdpEtbTopoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbTopoCnt.setStatus("current")
_TtdpLengthen_Type = Antivalent2
_TtdpLengthen_Object = MibTableColumn
ttdpLengthen = _TtdpLengthen_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 12),
    _TtdpLengthen_Type()
)
ttdpLengthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpLengthen.setStatus("current")
_TtdpShorten_Type = Antivalent2
_TtdpShorten_Object = MibTableColumn
ttdpShorten = _TtdpShorten_Object(
    (1, 0, 61375, 2, 5, 1, 5, 3, 1, 13),
    _TtdpShorten_Type()
)
ttdpShorten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpShorten.setStatus("current")
_TtdpConnectTable_Object = MibTable
ttdpConnectTable = _TtdpConnectTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ttdpConnectTable.setStatus("current")
_TtdpConnectEntry_Object = MibTableRow
ttdpConnectEntry = _TtdpConnectEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 4, 1)
)
ttdpConnectEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpEtbnTableIdx"),
    (0, "TTDP-MIB", "ttdpConnectTableIdx"),
)
if mibBuilder.loadTexts:
    ttdpConnectEntry.setStatus("current")
_TtdpConnectTableIdx_Type = TtdpDirection
_TtdpConnectTableIdx_Object = MibTableColumn
ttdpConnectTableIdx = _TtdpConnectTableIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 4, 1, 1),
    _TtdpConnectTableIdx_Type()
)
ttdpConnectTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpConnectTableIdx.setStatus("current")
_TtdpNeighbourMacAddr_Type = MacAddress
_TtdpNeighbourMacAddr_Object = MibTableColumn
ttdpNeighbourMacAddr = _TtdpNeighbourMacAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 4, 1, 2),
    _TtdpNeighbourMacAddr_Type()
)
ttdpNeighbourMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpNeighbourMacAddr.setStatus("current")


class _TtdpEtbnDirCnt_Type(Unsigned32):
    """Custom type ttdpEtbnDirCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_TtdpEtbnDirCnt_Type.__name__ = "Unsigned32"
_TtdpEtbnDirCnt_Object = MibTableColumn
ttdpEtbnDirCnt = _TtdpEtbnDirCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 4, 1, 3),
    _TtdpEtbnDirCnt_Type()
)
ttdpEtbnDirCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnDirCnt.setStatus("current")
_TtdpEtbnVectorTable_Object = MibTable
ttdpEtbnVectorTable = _TtdpEtbnVectorTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ttdpEtbnVectorTable.setStatus("current")
_TtdpEtbnVectorEntry_Object = MibTableRow
ttdpEtbnVectorEntry = _TtdpEtbnVectorEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 5, 1)
)
ttdpEtbnVectorEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpEtbnTableIdx"),
    (0, "TTDP-MIB", "ttdpConnectTableIdx"),
    (0, "TTDP-MIB", "ttdpEtbnVectorIdx"),
)
if mibBuilder.loadTexts:
    ttdpEtbnVectorEntry.setStatus("current")


class _TtdpEtbnVectorIdx_Type(Unsigned32):
    """Custom type ttdpEtbnVectorIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_TtdpEtbnVectorIdx_Type.__name__ = "Unsigned32"
_TtdpEtbnVectorIdx_Object = MibTableColumn
ttdpEtbnVectorIdx = _TtdpEtbnVectorIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 5, 1, 1),
    _TtdpEtbnVectorIdx_Type()
)
ttdpEtbnVectorIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnVectorIdx.setStatus("current")
_TtdpEtbnVectorMacAddr_Type = MacAddress
_TtdpEtbnVectorMacAddr_Object = MibTableColumn
ttdpEtbnVectorMacAddr = _TtdpEtbnVectorMacAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 5, 1, 2),
    _TtdpEtbnVectorMacAddr_Type()
)
ttdpEtbnVectorMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpEtbnVectorMacAddr.setStatus("current")


class _TtdpCstCnt_Type(Unsigned32):
    """Custom type ttdpCstCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TtdpCstCnt_Type.__name__ = "Unsigned32"
_TtdpCstCnt_Object = MibScalar
ttdpCstCnt = _TtdpCstCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 6),
    _TtdpCstCnt_Type()
)
ttdpCstCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstCnt.setStatus("current")
_TtdpCstTable_Object = MibTable
ttdpCstTable = _TtdpCstTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7)
)
if mibBuilder.loadTexts:
    ttdpCstTable.setStatus("current")
_TtdpCstEntry_Object = MibTableRow
ttdpCstEntry = _TtdpCstEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1)
)
ttdpCstEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpCstTableIdx"),
)
if mibBuilder.loadTexts:
    ttdpCstEntry.setStatus("current")


class _TtdpCstTableIdx_Type(Unsigned32):
    """Custom type ttdpCstTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TtdpCstTableIdx_Type.__name__ = "Unsigned32"
_TtdpCstTableIdx_Object = MibTableColumn
ttdpCstTableIdx = _TtdpCstTableIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1, 1),
    _TtdpCstTableIdx_Type()
)
ttdpCstTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstTableIdx.setStatus("current")


class _TtdpCstUuid_Type(OctetString):
    """Custom type ttdpCstUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TtdpCstUuid_Type.__name__ = "OctetString"
_TtdpCstUuid_Object = MibTableColumn
ttdpCstUuid = _TtdpCstUuid_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1, 2),
    _TtdpCstUuid_Type()
)
ttdpCstUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstUuid.setStatus("current")
_TtdpCstOrientation_Type = TtdpOrientation
_TtdpCstOrientation_Object = MibTableColumn
ttdpCstOrientation = _TtdpCstOrientation_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1, 3),
    _TtdpCstOrientation_Type()
)
ttdpCstOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstOrientation.setStatus("current")


class _TtdpCstCnCnt_Type(Unsigned32):
    """Custom type ttdpCstCnCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TtdpCstCnCnt_Type.__name__ = "Unsigned32"
_TtdpCstCnCnt_Object = MibTableColumn
ttdpCstCnCnt = _TtdpCstCnCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1, 4),
    _TtdpCstCnCnt_Type()
)
ttdpCstCnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstCnCnt.setStatus("current")


class _TtdpCstEtbnCnt_Type(Unsigned32):
    """Custom type ttdpCstEtbnCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TtdpCstEtbnCnt_Type.__name__ = "Unsigned32"
_TtdpCstEtbnCnt_Object = MibTableColumn
ttdpCstEtbnCnt = _TtdpCstEtbnCnt_Object(
    (1, 0, 61375, 2, 5, 1, 5, 7, 1, 5),
    _TtdpCstEtbnCnt_Type()
)
ttdpCstEtbnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstEtbnCnt.setStatus("current")
_TtdpCstCnTable_Object = MibTable
ttdpCstCnTable = _TtdpCstCnTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8)
)
if mibBuilder.loadTexts:
    ttdpCstCnTable.setStatus("current")
_TtdpCstCnEntry_Object = MibTableRow
ttdpCstCnEntry = _TtdpCstCnEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1)
)
ttdpCstCnEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpCstTableIdx"),
    (0, "TTDP-MIB", "ttdpCstCnTableIdx"),
)
if mibBuilder.loadTexts:
    ttdpCstCnEntry.setStatus("current")


class _TtdpCstCnTableIdx_Type(Unsigned32):
    """Custom type ttdpCstCnTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TtdpCstCnTableIdx_Type.__name__ = "Unsigned32"
_TtdpCstCnTableIdx_Object = MibTableColumn
ttdpCstCnTableIdx = _TtdpCstCnTableIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 1),
    _TtdpCstCnTableIdx_Type()
)
ttdpCstCnTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCstCnTableIdx.setStatus("current")


class _TtdpCnType_Type(Integer32):
    """Custom type ttdpCnType based on Integer32"""
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
        *(("mvb", 1),
          ("notUsed", 2),
          ("can", 3),
          ("ethernet", 4))
    )


_TtdpCnType_Type.__name__ = "Integer32"
_TtdpCnType_Object = MibTableColumn
ttdpCnType = _TtdpCnType_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 2),
    _TtdpCnType_Type()
)
ttdpCnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCnType.setStatus("current")


class _TtdpCnId_Type(Unsigned32):
    """Custom type ttdpCnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TtdpCnId_Type.__name__ = "Unsigned32"
_TtdpCnId_Object = MibTableColumn
ttdpCnId = _TtdpCnId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 3),
    _TtdpCnId_Type()
)
ttdpCnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCnId.setStatus("current")


class _TtdpSubnetId_Type(Unsigned32):
    """Custom type ttdpSubnetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpSubnetId_Type.__name__ = "Unsigned32"
_TtdpSubnetId_Object = MibTableColumn
ttdpSubnetId = _TtdpSubnetId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 4),
    _TtdpSubnetId_Type()
)
ttdpSubnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpSubnetId.setStatus("current")
_TtdpSubnetIpAddr_Type = IpAddress
_TtdpSubnetIpAddr_Object = MibTableColumn
ttdpSubnetIpAddr = _TtdpSubnetIpAddr_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 5),
    _TtdpSubnetIpAddr_Type()
)
ttdpSubnetIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpSubnetIpAddr.setStatus("current")
_TtdpSubnetIpMask_Type = IpAddress
_TtdpSubnetIpMask_Object = MibTableColumn
ttdpSubnetIpMask = _TtdpSubnetIpMask_Object(
    (1, 0, 61375, 2, 5, 1, 5, 8, 1, 6),
    _TtdpSubnetIpMask_Type()
)
ttdpSubnetIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpSubnetIpMask.setStatus("current")
_TtdpCnEtbnTable_Object = MibTable
ttdpCnEtbnTable = _TtdpCnEtbnTable_Object(
    (1, 0, 61375, 2, 5, 1, 5, 9)
)
if mibBuilder.loadTexts:
    ttdpCnEtbnTable.setStatus("current")
_TtdpCnEtbnEntry_Object = MibTableRow
ttdpCnEtbnEntry = _TtdpCnEtbnEntry_Object(
    (1, 0, 61375, 2, 5, 1, 5, 9, 1)
)
ttdpCnEtbnEntry.setIndexNames(
    (0, "TTDP-MIB", "ttdpCstTableIdx"),
    (0, "TTDP-MIB", "ttdpCstCnTableIdx"),
    (0, "TTDP-MIB", "ttdpCnEtbnTableIdx"),
)
if mibBuilder.loadTexts:
    ttdpCnEtbnEntry.setStatus("current")


class _TtdpCnEtbnTableIdx_Type(Unsigned32):
    """Custom type ttdpCnEtbnTableIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpCnEtbnTableIdx_Type.__name__ = "Unsigned32"
_TtdpCnEtbnTableIdx_Object = MibTableColumn
ttdpCnEtbnTableIdx = _TtdpCnEtbnTableIdx_Object(
    (1, 0, 61375, 2, 5, 1, 5, 9, 1, 1),
    _TtdpCnEtbnTableIdx_Type()
)
ttdpCnEtbnTableIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCnEtbnTableIdx.setStatus("current")


class _TtdpCnEtbnId_Type(Unsigned32):
    """Custom type ttdpCnEtbnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdpCnEtbnId_Type.__name__ = "Unsigned32"
_TtdpCnEtbnId_Object = MibTableColumn
ttdpCnEtbnId = _TtdpCnEtbnId_Object(
    (1, 0, 61375, 2, 5, 1, 5, 9, 1, 2),
    _TtdpCnEtbnId_Type()
)
ttdpCnEtbnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdpCnEtbnId.setStatus("current")
_TtdpConformance_ObjectIdentity = ObjectIdentity
ttdpConformance = _TtdpConformance_ObjectIdentity(
    (1, 0, 61375, 2, 5, 2)
)

# Managed Objects groups

ttdpBasicGroup = ObjectGroup(
    (1, 0, 61375, 2, 5, 2, 2)
)
ttdpBasicGroup.setObjects(
      *(("TTDP-MIB", "ttdpVersion"),
        ("TTDP-MIB", "ttdpSlowTimeout"),
        ("TTDP-MIB", "ttdpFastTimeout"),
        ("TTDP-MIB", "ttdpTopoTtl"),
        ("TTDP-MIB", "ttdpGlobalTopoTimeout"),
        ("TTDP-MIB", "ttdpLogicalLinksNb"),
        ("TTDP-MIB", "ttdpLogicalLinksIdx"),
        ("TTDP-MIB", "ttdpIsEndLink"),
        ("TTDP-MIB", "ttdpPortState"),
        ("TTDP-MIB", "ttdpEtbId"),
        ("TTDP-MIB", "ttdpLocalEtbnMacAddr"),
        ("TTDP-MIB", "ttdpLocalEtbnId"),
        ("TTDP-MIB", "ttdpNodePosition"),
        ("TTDP-MIB", "ttdpIsAlone"),
        ("TTDP-MIB", "ttdpConnTableValid"),
        ("TTDP-MIB", "ttdpEtbnCnt"),
        ("TTDP-MIB", "ttdpEtbnTableIdx"),
        ("TTDP-MIB", "ttdpEtbnId"),
        ("TTDP-MIB", "ttdpEtbnMacAddr"),
        ("TTDP-MIB", "ttdpEtbnOrientation"),
        ("TTDP-MIB", "ttdpEtbnIpAddr"),
        ("TTDP-MIB", "ttdpEtbnNodeRole"),
        ("TTDP-MIB", "ttdpEtbnInaugState"),
        ("TTDP-MIB", "ttdpEtbnInhibit"),
        ("TTDP-MIB", "ttdpRemoteInhibit"),
        ("TTDP-MIB", "ttdpConnTableCrc32"),
        ("TTDP-MIB", "ttdpLengthen"),
        ("TTDP-MIB", "ttdpShorten"),
        ("TTDP-MIB", "ttdpConnectTableIdx"),
        ("TTDP-MIB", "ttdpNeighbourMacAddr"),
        ("TTDP-MIB", "ttdpEtbnDirCnt"),
        ("TTDP-MIB", "ttdpEtbnVectorIdx"),
        ("TTDP-MIB", "ttdpEtbnVectorMacAddr"),
        ("TTDP-MIB", "ttdpCstCnt"),
        ("TTDP-MIB", "ttdpCstTableIdx"),
        ("TTDP-MIB", "ttdpCstUuid"),
        ("TTDP-MIB", "ttdpCstOrientation"),
        ("TTDP-MIB", "ttdpCstCnCnt"),
        ("TTDP-MIB", "ttdpCstEtbnCnt"),
        ("TTDP-MIB", "ttdpCstCnTableIdx"),
        ("TTDP-MIB", "ttdpCnType"),
        ("TTDP-MIB", "ttdpCnId"),
        ("TTDP-MIB", "ttdpSubnetId"),
        ("TTDP-MIB", "ttdpSubnetIpAddr"),
        ("TTDP-MIB", "ttdpSubnetIpMask"),
        ("TTDP-MIB", "ttdpCnEtbnTableIdx"),
        ("TTDP-MIB", "ttdpCnEtbnId"),
        ("TTDP-MIB", "ttdpEtbTopoCntValid"),
        ("TTDP-MIB", "ttdpEtbTopoCnt"),
        ("TTDP-MIB", "ttdpConfiguredPhysLinesNb"),
        ("TTDP-MIB", "ttdpActivePhysLinesNb"),
        ("TTDP-MIB", "ttdpPhysicalLinesIdx"),
        ("TTDP-MIB", "ttdpPeerLineId"),
        ("TTDP-MIB", "ttdpLineRcvState"))
)
if mibBuilder.loadTexts:
    ttdpBasicGroup.setStatus("current")

ttdpStatsGroup = ObjectGroup(
    (1, 0, 61375, 2, 5, 2, 3)
)
ttdpStatsGroup.setObjects(
      *(("TTDP-MIB", "ttdpHelloSentFrames"),
        ("TTDP-MIB", "ttdpHelloReceivedFrames"),
        ("TTDP-MIB", "ttdpRemoteFastModeCnt"),
        ("TTDP-MIB", "ttdpLocalFastModeCnt"),
        ("TTDP-MIB", "ttdpTopoSentFrames"),
        ("TTDP-MIB", "ttdpTopoReceivedFrames"))
)
if mibBuilder.loadTexts:
    ttdpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ttdpBasicCompliance = ModuleCompliance(
    (1, 0, 61375, 2, 5, 2, 4)
)
ttdpBasicCompliance.setObjects(
    ("TTDP-MIB", "ttdpBasicGroup")
)
if mibBuilder.loadTexts:
    ttdpBasicCompliance.setStatus(
        "current"
    )

ttdpStatsCompliance = ModuleCompliance(
    (1, 0, 61375, 2, 5, 2, 5)
)
ttdpStatsCompliance.setObjects(
    ("TTDP-MIB", "ttdpStatsGroup")
)
if mibBuilder.loadTexts:
    ttdpStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TTDP-MIB",
    **{"TtdpPhysicalLineId": TtdpPhysicalLineId,
       "TtdpOrientation": TtdpOrientation,
       "Antivalent2": Antivalent2,
       "TtdpDirection": TtdpDirection,
       "std": std,
       "stdx61375": stdx61375,
       "iec61375": iec61375,
       "ttdp": ttdp,
       "ttdpObjects": ttdpObjects,
       "ttdpGenInfo": ttdpGenInfo,
       "ttdpVersion": ttdpVersion,
       "ttdpSlowTimeout": ttdpSlowTimeout,
       "ttdpFastTimeout": ttdpFastTimeout,
       "ttdpTopoTtl": ttdpTopoTtl,
       "ttdpGlobalTopoTimeout": ttdpGlobalTopoTimeout,
       "ttdpLinksInfo": ttdpLinksInfo,
       "ttdpLogicalLinksNb": ttdpLogicalLinksNb,
       "ttdpLogicalLinksTable": ttdpLogicalLinksTable,
       "ttdpLogicalLinksEntry": ttdpLogicalLinksEntry,
       "ttdpLogicalLinksIdx": ttdpLogicalLinksIdx,
       "ttdpConfiguredPhysLinesNb": ttdpConfiguredPhysLinesNb,
       "ttdpActivePhysLinesNb": ttdpActivePhysLinesNb,
       "ttdpIsEndLink": ttdpIsEndLink,
       "ttdpPhysicalLinesTable": ttdpPhysicalLinesTable,
       "ttdpPhysicalLinesEntry": ttdpPhysicalLinesEntry,
       "ttdpPhysicalLinesIdx": ttdpPhysicalLinesIdx,
       "ttdpPortState": ttdpPortState,
       "ttdpLineRcvState": ttdpLineRcvState,
       "ttdpPeerLineId": ttdpPeerLineId,
       "ttdpPhysicalLinesStatsTable": ttdpPhysicalLinesStatsTable,
       "ttdpPhysicalLinesStatsEntry": ttdpPhysicalLinesStatsEntry,
       "ttdpHelloSentFrames": ttdpHelloSentFrames,
       "ttdpHelloReceivedFrames": ttdpHelloReceivedFrames,
       "ttdpRemoteFastModeCnt": ttdpRemoteFastModeCnt,
       "ttdpLocalFastModeCnt": ttdpLocalFastModeCnt,
       "ttdpTopoInfo": ttdpTopoInfo,
       "ttdpLocalEtbnInfo": ttdpLocalEtbnInfo,
       "ttdpEtbId": ttdpEtbId,
       "ttdpLocalEtbnMacAddr": ttdpLocalEtbnMacAddr,
       "ttdpLocalEtbnId": ttdpLocalEtbnId,
       "ttdpNodePosition": ttdpNodePosition,
       "ttdpIsAlone": ttdpIsAlone,
       "ttdpConnTableValid": ttdpConnTableValid,
       "ttdpEtbTopoCntValid": ttdpEtbTopoCntValid,
       "ttdpTopoFrameStats": ttdpTopoFrameStats,
       "ttdpTopoSentFrames": ttdpTopoSentFrames,
       "ttdpTopoReceivedFrames": ttdpTopoReceivedFrames,
       "ttdpEtbnCnt": ttdpEtbnCnt,
       "ttdpEtbnTable": ttdpEtbnTable,
       "ttdpEtbnEntry": ttdpEtbnEntry,
       "ttdpEtbnTableIdx": ttdpEtbnTableIdx,
       "ttdpEtbnId": ttdpEtbnId,
       "ttdpEtbnMacAddr": ttdpEtbnMacAddr,
       "ttdpEtbnOrientation": ttdpEtbnOrientation,
       "ttdpEtbnIpAddr": ttdpEtbnIpAddr,
       "ttdpEtbnNodeRole": ttdpEtbnNodeRole,
       "ttdpEtbnInaugState": ttdpEtbnInaugState,
       "ttdpEtbnInhibit": ttdpEtbnInhibit,
       "ttdpRemoteInhibit": ttdpRemoteInhibit,
       "ttdpConnTableCrc32": ttdpConnTableCrc32,
       "ttdpEtbTopoCnt": ttdpEtbTopoCnt,
       "ttdpLengthen": ttdpLengthen,
       "ttdpShorten": ttdpShorten,
       "ttdpConnectTable": ttdpConnectTable,
       "ttdpConnectEntry": ttdpConnectEntry,
       "ttdpConnectTableIdx": ttdpConnectTableIdx,
       "ttdpNeighbourMacAddr": ttdpNeighbourMacAddr,
       "ttdpEtbnDirCnt": ttdpEtbnDirCnt,
       "ttdpEtbnVectorTable": ttdpEtbnVectorTable,
       "ttdpEtbnVectorEntry": ttdpEtbnVectorEntry,
       "ttdpEtbnVectorIdx": ttdpEtbnVectorIdx,
       "ttdpEtbnVectorMacAddr": ttdpEtbnVectorMacAddr,
       "ttdpCstCnt": ttdpCstCnt,
       "ttdpCstTable": ttdpCstTable,
       "ttdpCstEntry": ttdpCstEntry,
       "ttdpCstTableIdx": ttdpCstTableIdx,
       "ttdpCstUuid": ttdpCstUuid,
       "ttdpCstOrientation": ttdpCstOrientation,
       "ttdpCstCnCnt": ttdpCstCnCnt,
       "ttdpCstEtbnCnt": ttdpCstEtbnCnt,
       "ttdpCstCnTable": ttdpCstCnTable,
       "ttdpCstCnEntry": ttdpCstCnEntry,
       "ttdpCstCnTableIdx": ttdpCstCnTableIdx,
       "ttdpCnType": ttdpCnType,
       "ttdpCnId": ttdpCnId,
       "ttdpSubnetId": ttdpSubnetId,
       "ttdpSubnetIpAddr": ttdpSubnetIpAddr,
       "ttdpSubnetIpMask": ttdpSubnetIpMask,
       "ttdpCnEtbnTable": ttdpCnEtbnTable,
       "ttdpCnEtbnEntry": ttdpCnEtbnEntry,
       "ttdpCnEtbnTableIdx": ttdpCnEtbnTableIdx,
       "ttdpCnEtbnId": ttdpCnEtbnId,
       "ttdpConformance": ttdpConformance,
       "ttdpBasicGroup": ttdpBasicGroup,
       "ttdpStatsGroup": ttdpStatsGroup,
       "ttdpBasicCompliance": ttdpBasicCompliance,
       "ttdpStatsCompliance": ttdpStatsCompliance}
)
