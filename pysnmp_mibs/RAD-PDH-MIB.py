# SNMP MIB module (RAD-PDH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-PDH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:20 2025
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

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pdhInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdhIfConfig_ObjectIdentity = ObjectIdentity
pdhIfConfig = _PdhIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1)
)
_PdhLogPrtConfigTable_Object = MibTable
pdhLogPrtConfigTable = _PdhLogPrtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1, 1)
)
if mibBuilder.loadTexts:
    pdhLogPrtConfigTable.setStatus("current")
_PdhLogPrtConfigEntry_Object = MibTableRow
pdhLogPrtConfigEntry = _PdhLogPrtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1, 1, 1)
)
pdhLogPrtConfigEntry.setIndexNames(
    (0, "RAD-PDH-MIB", "pdhLogPrtCnfgIdx"),
    (0, "RAD-PDH-MIB", "pdhLogPrtIndex"),
)
if mibBuilder.loadTexts:
    pdhLogPrtConfigEntry.setStatus("current")


class _PdhLogPrtCnfgIdx_Type(Integer32):
    """Custom type pdhLogPrtCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PdhLogPrtCnfgIdx_Type.__name__ = "Integer32"
_PdhLogPrtCnfgIdx_Object = MibTableColumn
pdhLogPrtCnfgIdx = _PdhLogPrtCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1, 1, 1, 1),
    _PdhLogPrtCnfgIdx_Type()
)
pdhLogPrtCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdhLogPrtCnfgIdx.setStatus("current")
_PdhLogPrtIndex_Type = Unsigned32
_PdhLogPrtIndex_Object = MibTableColumn
pdhLogPrtIndex = _PdhLogPrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1, 1, 1, 2),
    _PdhLogPrtIndex_Type()
)
pdhLogPrtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdhLogPrtIndex.setStatus("current")
_PdhLogPrtMaxDiffDelay_Type = Unsigned32
_PdhLogPrtMaxDiffDelay_Object = MibTableColumn
pdhLogPrtMaxDiffDelay = _PdhLogPrtMaxDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 1, 1, 1, 3),
    _PdhLogPrtMaxDiffDelay_Type()
)
pdhLogPrtMaxDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdhLogPrtMaxDiffDelay.setStatus("current")
_PdhIfStatus_ObjectIdentity = ObjectIdentity
pdhIfStatus = _PdhIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2)
)
_PdhLogPrtStatusTable_Object = MibTable
pdhLogPrtStatusTable = _PdhLogPrtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    pdhLogPrtStatusTable.setStatus("current")
_PdhLogPrtStatusEntry_Object = MibTableRow
pdhLogPrtStatusEntry = _PdhLogPrtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 1, 1)
)
pdhLogPrtStatusEntry.setIndexNames(
    (0, "RAD-PDH-MIB", "pdhLogPrtStatusIndex"),
)
if mibBuilder.loadTexts:
    pdhLogPrtStatusEntry.setStatus("current")
_PdhLogPrtStatusIndex_Type = Unsigned32
_PdhLogPrtStatusIndex_Object = MibTableColumn
pdhLogPrtStatusIndex = _PdhLogPrtStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 1, 1, 1),
    _PdhLogPrtStatusIndex_Type()
)
pdhLogPrtStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdhLogPrtStatusIndex.setStatus("current")


class _PdhLogPrtFrameDelineation_Type(Integer32):
    """Custom type pdhLogPrtFrameDelineation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notDelineated", 2),
          ("delineated", 3))
    )


_PdhLogPrtFrameDelineation_Type.__name__ = "Integer32"
_PdhLogPrtFrameDelineation_Object = MibTableColumn
pdhLogPrtFrameDelineation = _PdhLogPrtFrameDelineation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 1, 1, 2),
    _PdhLogPrtFrameDelineation_Type()
)
pdhLogPrtFrameDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtFrameDelineation.setStatus("current")
_PdhLogPrtDiffDelay_Type = Unsigned32
_PdhLogPrtDiffDelay_Object = MibTableColumn
pdhLogPrtDiffDelay = _PdhLogPrtDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 1, 1, 3),
    _PdhLogPrtDiffDelay_Type()
)
pdhLogPrtDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtDiffDelay.setStatus("current")
_VcgLcasMembersStatusTable_Object = MibTable
vcgLcasMembersStatusTable = _VcgLcasMembersStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2)
)
if mibBuilder.loadTexts:
    vcgLcasMembersStatusTable.setStatus("current")
_VcgLcasMembersStatusEntry_Object = MibTableRow
vcgLcasMembersStatusEntry = _VcgLcasMembersStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1)
)
vcgLcasMembersStatusEntry.setIndexNames(
    (0, "RAD-PDH-MIB", "vcgLcasMembersVcgIndex"),
    (0, "RAD-PDH-MIB", "vcgLcasMembersLinkIndex"),
)
if mibBuilder.loadTexts:
    vcgLcasMembersStatusEntry.setStatus("current")
_VcgLcasMembersVcgIndex_Type = Unsigned32
_VcgLcasMembersVcgIndex_Object = MibTableColumn
vcgLcasMembersVcgIndex = _VcgLcasMembersVcgIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 1),
    _VcgLcasMembersVcgIndex_Type()
)
vcgLcasMembersVcgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcgLcasMembersVcgIndex.setStatus("current")
_VcgLcasMembersLinkIndex_Type = Unsigned32
_VcgLcasMembersLinkIndex_Object = MibTableColumn
vcgLcasMembersLinkIndex = _VcgLcasMembersLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 2),
    _VcgLcasMembersLinkIndex_Type()
)
vcgLcasMembersLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vcgLcasMembersLinkIndex.setStatus("current")


class _VcgLcasMembersSourceStatus_Type(Integer32):
    """Custom type vcgLcasMembersSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3),
          ("fixed", 4),
          ("add", 5),
          ("norm", 6),
          ("eos", 7),
          ("idle", 8),
          ("trSwitchLoopDetect", 9),
          ("dnu", 10),
          ("illegal", 11))
    )


_VcgLcasMembersSourceStatus_Type.__name__ = "Integer32"
_VcgLcasMembersSourceStatus_Object = MibTableColumn
vcgLcasMembersSourceStatus = _VcgLcasMembersSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 3),
    _VcgLcasMembersSourceStatus_Type()
)
vcgLcasMembersSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersSourceStatus.setStatus("current")


class _VcgLcasMembersSinkStatus_Type(Integer32):
    """Custom type vcgLcasMembersSinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3),
          ("fixed", 4),
          ("add", 5),
          ("norm", 6),
          ("eos", 7),
          ("idle", 8),
          ("trSwitchLoopDetect", 9),
          ("dnu", 10),
          ("illegal", 11))
    )


_VcgLcasMembersSinkStatus_Type.__name__ = "Integer32"
_VcgLcasMembersSinkStatus_Object = MibTableColumn
vcgLcasMembersSinkStatus = _VcgLcasMembersSinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 4),
    _VcgLcasMembersSinkStatus_Type()
)
vcgLcasMembersSinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersSinkStatus.setStatus("current")


class _VcgLcasMembersLoopStatus_Type(Integer32):
    """Custom type vcgLcasMembersLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("noLoop", 2),
          ("loop", 3))
    )


_VcgLcasMembersLoopStatus_Type.__name__ = "Integer32"
_VcgLcasMembersLoopStatus_Object = MibTableColumn
vcgLcasMembersLoopStatus = _VcgLcasMembersLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 5),
    _VcgLcasMembersLoopStatus_Type()
)
vcgLcasMembersLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersLoopStatus.setStatus("current")


class _VcgLcasMembersTxStateMachineStatus_Type(Integer32):
    """Custom type vcgLcasMembersTxStateMachineStatus based on Integer32"""
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
        *(("idle", 1),
          ("add", 2),
          ("norm", 3),
          ("dnu", 4),
          ("remove", 5),
          ("illegal", 6))
    )


_VcgLcasMembersTxStateMachineStatus_Type.__name__ = "Integer32"
_VcgLcasMembersTxStateMachineStatus_Object = MibTableColumn
vcgLcasMembersTxStateMachineStatus = _VcgLcasMembersTxStateMachineStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 6),
    _VcgLcasMembersTxStateMachineStatus_Type()
)
vcgLcasMembersTxStateMachineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersTxStateMachineStatus.setStatus("current")


class _VcgLcasMembersRxStateMachineStatus_Type(Integer32):
    """Custom type vcgLcasMembersRxStateMachineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("fail", 2),
          ("ok", 3),
          ("wtrFail", 4),
          ("wtrOk", 5),
          ("ho", 6),
          ("remove", 7),
          ("illegal", 8))
    )


_VcgLcasMembersRxStateMachineStatus_Type.__name__ = "Integer32"
_VcgLcasMembersRxStateMachineStatus_Object = MibTableColumn
vcgLcasMembersRxStateMachineStatus = _VcgLcasMembersRxStateMachineStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 7),
    _VcgLcasMembersRxStateMachineStatus_Type()
)
vcgLcasMembersRxStateMachineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersRxStateMachineStatus.setStatus("current")


class _VcgLcasMembersStatus_Type(Integer32):
    """Custom type vcgLcasMembersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3))
    )


_VcgLcasMembersStatus_Type.__name__ = "Integer32"
_VcgLcasMembersStatus_Object = MibTableColumn
vcgLcasMembersStatus = _VcgLcasMembersStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 8),
    _VcgLcasMembersStatus_Type()
)
vcgLcasMembersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersStatus.setStatus("current")


class _VcgLcasMembersSignalUnavailable_Type(Integer32):
    """Custom type vcgLcasMembersSignalUnavailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_VcgLcasMembersSignalUnavailable_Type.__name__ = "Integer32"
_VcgLcasMembersSignalUnavailable_Object = MibTableColumn
vcgLcasMembersSignalUnavailable = _VcgLcasMembersSignalUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 9),
    _VcgLcasMembersSignalUnavailable_Type()
)
vcgLcasMembersSignalUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersSignalUnavailable.setStatus("current")


class _VcgLcasMembersTrailSignalDegrade_Type(Integer32):
    """Custom type vcgLcasMembersTrailSignalDegrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("no", 2),
          ("yes", 3))
    )


_VcgLcasMembersTrailSignalDegrade_Type.__name__ = "Integer32"
_VcgLcasMembersTrailSignalDegrade_Object = MibTableColumn
vcgLcasMembersTrailSignalDegrade = _VcgLcasMembersTrailSignalDegrade_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 10),
    _VcgLcasMembersTrailSignalDegrade_Type()
)
vcgLcasMembersTrailSignalDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersTrailSignalDegrade.setStatus("current")
_VcgLcasMembersMfiDiffDelay_Type = Unsigned32
_VcgLcasMembersMfiDiffDelay_Object = MibTableColumn
vcgLcasMembersMfiDiffDelay = _VcgLcasMembersMfiDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 11),
    _VcgLcasMembersMfiDiffDelay_Type()
)
vcgLcasMembersMfiDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersMfiDiffDelay.setStatus("current")


class _VcgLcasMembersVcLoMF_Type(Integer32):
    """Custom type vcgLcasMembersVcLoMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_VcgLcasMembersVcLoMF_Type.__name__ = "Integer32"
_VcgLcasMembersVcLoMF_Object = MibTableColumn
vcgLcasMembersVcLoMF = _VcgLcasMembersVcLoMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 12),
    _VcgLcasMembersVcLoMF_Type()
)
vcgLcasMembersVcLoMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersVcLoMF.setStatus("current")
_VcgLcasMembersTxSeqNumber_Type = Unsigned32
_VcgLcasMembersTxSeqNumber_Object = MibTableColumn
vcgLcasMembersTxSeqNumber = _VcgLcasMembersTxSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 13),
    _VcgLcasMembersTxSeqNumber_Type()
)
vcgLcasMembersTxSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersTxSeqNumber.setStatus("current")
_VcgLcasMembersRxSeqNumber_Type = Unsigned32
_VcgLcasMembersRxSeqNumber_Object = MibTableColumn
vcgLcasMembersRxSeqNumber = _VcgLcasMembersRxSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 2, 2, 1, 14),
    _VcgLcasMembersRxSeqNumber_Type()
)
vcgLcasMembersRxSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgLcasMembersRxSeqNumber.setStatus("current")
_PdhIfStatis_ObjectIdentity = ObjectIdentity
pdhIfStatis = _PdhIfStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3)
)
_PdhLogPrtStatisTable_Object = MibTable
pdhLogPrtStatisTable = _PdhLogPrtStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1)
)
if mibBuilder.loadTexts:
    pdhLogPrtStatisTable.setStatus("current")
_PdhLogPrtStatisEntry_Object = MibTableRow
pdhLogPrtStatisEntry = _PdhLogPrtStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1)
)
pdhLogPrtStatisEntry.setIndexNames(
    (0, "RAD-PDH-MIB", "pdhLogPrtStatisIndex"),
)
if mibBuilder.loadTexts:
    pdhLogPrtStatisEntry.setStatus("current")
_PdhLogPrtStatisIndex_Type = Unsigned32
_PdhLogPrtStatisIndex_Object = MibTableColumn
pdhLogPrtStatisIndex = _PdhLogPrtStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 1),
    _PdhLogPrtStatisIndex_Type()
)
pdhLogPrtStatisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdhLogPrtStatisIndex.setStatus("current")
_PdhLogPrtStatisRxCorrFrames_Type = Counter32
_PdhLogPrtStatisRxCorrFrames_Object = MibTableColumn
pdhLogPrtStatisRxCorrFrames = _PdhLogPrtStatisRxCorrFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 2),
    _PdhLogPrtStatisRxCorrFrames_Type()
)
pdhLogPrtStatisRxCorrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtStatisRxCorrFrames.setStatus("current")
_PdhLogPrtStatisRxCorrOctets_Type = Counter32
_PdhLogPrtStatisRxCorrOctets_Object = MibTableColumn
pdhLogPrtStatisRxCorrOctets = _PdhLogPrtStatisRxCorrOctets_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 3),
    _PdhLogPrtStatisRxCorrOctets_Type()
)
pdhLogPrtStatisRxCorrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtStatisRxCorrOctets.setStatus("current")
_PdhLogPrtStatisRxCHecErrors_Type = Counter32
_PdhLogPrtStatisRxCHecErrors_Object = MibTableColumn
pdhLogPrtStatisRxCHecErrors = _PdhLogPrtStatisRxCHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 4),
    _PdhLogPrtStatisRxCHecErrors_Type()
)
pdhLogPrtStatisRxCHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtStatisRxCHecErrors.setStatus("current")
_PdhLogPrtStatisRxTHecErrors_Type = Counter32
_PdhLogPrtStatisRxTHecErrors_Object = MibTableColumn
pdhLogPrtStatisRxTHecErrors = _PdhLogPrtStatisRxTHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 5),
    _PdhLogPrtStatisRxTHecErrors_Type()
)
pdhLogPrtStatisRxTHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtStatisRxTHecErrors.setStatus("current")
_PdhLogPrtStatisRxFcsErrors_Type = Counter32
_PdhLogPrtStatisRxFcsErrors_Object = MibTableColumn
pdhLogPrtStatisRxFcsErrors = _PdhLogPrtStatisRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 16, 3, 1, 1, 6),
    _PdhLogPrtStatisRxFcsErrors_Type()
)
pdhLogPrtStatisRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdhLogPrtStatisRxFcsErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-PDH-MIB",
    **{"pdhInterface": pdhInterface,
       "pdhIfConfig": pdhIfConfig,
       "pdhLogPrtConfigTable": pdhLogPrtConfigTable,
       "pdhLogPrtConfigEntry": pdhLogPrtConfigEntry,
       "pdhLogPrtCnfgIdx": pdhLogPrtCnfgIdx,
       "pdhLogPrtIndex": pdhLogPrtIndex,
       "pdhLogPrtMaxDiffDelay": pdhLogPrtMaxDiffDelay,
       "pdhIfStatus": pdhIfStatus,
       "pdhLogPrtStatusTable": pdhLogPrtStatusTable,
       "pdhLogPrtStatusEntry": pdhLogPrtStatusEntry,
       "pdhLogPrtStatusIndex": pdhLogPrtStatusIndex,
       "pdhLogPrtFrameDelineation": pdhLogPrtFrameDelineation,
       "pdhLogPrtDiffDelay": pdhLogPrtDiffDelay,
       "vcgLcasMembersStatusTable": vcgLcasMembersStatusTable,
       "vcgLcasMembersStatusEntry": vcgLcasMembersStatusEntry,
       "vcgLcasMembersVcgIndex": vcgLcasMembersVcgIndex,
       "vcgLcasMembersLinkIndex": vcgLcasMembersLinkIndex,
       "vcgLcasMembersSourceStatus": vcgLcasMembersSourceStatus,
       "vcgLcasMembersSinkStatus": vcgLcasMembersSinkStatus,
       "vcgLcasMembersLoopStatus": vcgLcasMembersLoopStatus,
       "vcgLcasMembersTxStateMachineStatus": vcgLcasMembersTxStateMachineStatus,
       "vcgLcasMembersRxStateMachineStatus": vcgLcasMembersRxStateMachineStatus,
       "vcgLcasMembersStatus": vcgLcasMembersStatus,
       "vcgLcasMembersSignalUnavailable": vcgLcasMembersSignalUnavailable,
       "vcgLcasMembersTrailSignalDegrade": vcgLcasMembersTrailSignalDegrade,
       "vcgLcasMembersMfiDiffDelay": vcgLcasMembersMfiDiffDelay,
       "vcgLcasMembersVcLoMF": vcgLcasMembersVcLoMF,
       "vcgLcasMembersTxSeqNumber": vcgLcasMembersTxSeqNumber,
       "vcgLcasMembersRxSeqNumber": vcgLcasMembersRxSeqNumber,
       "pdhIfStatis": pdhIfStatis,
       "pdhLogPrtStatisTable": pdhLogPrtStatisTable,
       "pdhLogPrtStatisEntry": pdhLogPrtStatisEntry,
       "pdhLogPrtStatisIndex": pdhLogPrtStatisIndex,
       "pdhLogPrtStatisRxCorrFrames": pdhLogPrtStatisRxCorrFrames,
       "pdhLogPrtStatisRxCorrOctets": pdhLogPrtStatisRxCorrOctets,
       "pdhLogPrtStatisRxCHecErrors": pdhLogPrtStatisRxCHecErrors,
       "pdhLogPrtStatisRxTHecErrors": pdhLogPrtStatisRxTHecErrors,
       "pdhLogPrtStatisRxFcsErrors": pdhLogPrtStatisRxFcsErrors}
)
