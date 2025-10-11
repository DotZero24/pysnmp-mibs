# SNMP MIB module (ZXPW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXPW-TDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:00 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zxPwCTDM,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCTDM")

(zxPwIndex,) = mibBuilder.importSymbols(
    "ZXPW-STD-MIB",
    "zxPwIndex")


# MODULE-IDENTITY

zxPwCTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwTDMCfgIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ZxPwCTDMObjects_ObjectIdentity = ObjectIdentity
zxPwCTDMObjects = _ZxPwCTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1)
)
_ZxPwCTDMTable_Object = MibTable
zxPwCTDMTable = _ZxPwCTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zxPwCTDMTable.setStatus("current")
_ZxPwCTDMEntry_Object = MibTableRow
zxPwCTDMEntry = _ZxPwCTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1)
)
zxPwCTDMEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxPwCTDMEntry.setStatus("current")


class _ZxPwCTDMRate_Type(Integer32):
    """Custom type zxPwCTDMRate based on Integer32"""
    defaultValue = 32


_ZxPwCTDMRate_Type.__name__ = "Integer32"
_ZxPwCTDMRate_Object = MibTableColumn
zxPwCTDMRate = _ZxPwCTDMRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 1),
    _ZxPwCTDMRate_Type()
)
zxPwCTDMRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwCTDMRate.setStatus("current")
_ZxPwCTDMIfIndex_Type = InterfaceIndexOrZero
_ZxPwCTDMIfIndex_Object = MibTableColumn
zxPwCTDMIfIndex = _ZxPwCTDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 2),
    _ZxPwCTDMIfIndex_Type()
)
zxPwCTDMIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwCTDMIfIndex.setStatus("current")
_ZxPwCGenTDMCfgIndex_Type = PwTDMCfgIndex
_ZxPwCGenTDMCfgIndex_Object = MibTableColumn
zxPwCGenTDMCfgIndex = _ZxPwCGenTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 3),
    _ZxPwCGenTDMCfgIndex_Type()
)
zxPwCGenTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwCGenTDMCfgIndex.setStatus("current")
_ZxPwCRelTDMCfgIndex_Type = PwTDMCfgIndex
_ZxPwCRelTDMCfgIndex_Object = MibTableColumn
zxPwCRelTDMCfgIndex = _ZxPwCRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 4),
    _ZxPwCRelTDMCfgIndex_Type()
)
zxPwCRelTDMCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxPwCRelTDMCfgIndex.setStatus("current")


class _ZxPwCTDMConfigError_Type(Bits):
    """Custom type zxPwCTDMConfigError based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("tdmTypeIncompatible", 1),
          ("peerRtpIncompatible", 2),
          ("peerPayloadSizeIncompatible", 3))
    )

_ZxPwCTDMConfigError_Type.__name__ = "Bits"
_ZxPwCTDMConfigError_Object = MibTableColumn
zxPwCTDMConfigError = _ZxPwCTDMConfigError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 5),
    _ZxPwCTDMConfigError_Type()
)
zxPwCTDMConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMConfigError.setStatus("current")


class _ZxPwCTDMTimeElapsed_Type(Integer32):
    """Custom type zxPwCTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_ZxPwCTDMTimeElapsed_Type.__name__ = "Integer32"
_ZxPwCTDMTimeElapsed_Object = MibTableColumn
zxPwCTDMTimeElapsed = _ZxPwCTDMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 6),
    _ZxPwCTDMTimeElapsed_Type()
)
zxPwCTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMTimeElapsed.setStatus("current")


class _ZxPwCTDMValidIntervals_Type(Integer32):
    """Custom type zxPwCTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZxPwCTDMValidIntervals_Type.__name__ = "Integer32"
_ZxPwCTDMValidIntervals_Object = MibTableColumn
zxPwCTDMValidIntervals = _ZxPwCTDMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 7),
    _ZxPwCTDMValidIntervals_Type()
)
zxPwCTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMValidIntervals.setStatus("current")


class _ZxPwCTDMValidDayIntervals_Type(Integer32):
    """Custom type zxPwCTDMValidDayIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ZxPwCTDMValidDayIntervals_Type.__name__ = "Integer32"
_ZxPwCTDMValidDayIntervals_Object = MibTableColumn
zxPwCTDMValidDayIntervals = _ZxPwCTDMValidDayIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 8),
    _ZxPwCTDMValidDayIntervals_Type()
)
zxPwCTDMValidDayIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMValidDayIntervals.setStatus("current")


class _ZxPwCTDMCurrentIndications_Type(Bits):
    """Custom type zxPwCTDMCurrentIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("strayPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("pktMisOrder", 7),
          ("packetLoss", 8),
          ("tdmFault", 9))
    )

_ZxPwCTDMCurrentIndications_Type.__name__ = "Bits"
_ZxPwCTDMCurrentIndications_Object = MibTableColumn
zxPwCTDMCurrentIndications = _ZxPwCTDMCurrentIndications_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 9),
    _ZxPwCTDMCurrentIndications_Type()
)
zxPwCTDMCurrentIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMCurrentIndications.setStatus("current")


class _ZxPwCTDMLatchedIndications_Type(Bits):
    """Custom type zxPwCTDMLatchedIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("staryPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("pktMisOrder", 7),
          ("packetLoss", 8),
          ("tdmFault", 9))
    )

_ZxPwCTDMLatchedIndications_Type.__name__ = "Bits"
_ZxPwCTDMLatchedIndications_Object = MibTableColumn
zxPwCTDMLatchedIndications = _ZxPwCTDMLatchedIndications_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 10),
    _ZxPwCTDMLatchedIndications_Type()
)
zxPwCTDMLatchedIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMLatchedIndications.setStatus("current")
_ZxPwCTDMLastEsTimeStamp_Type = TimeStamp
_ZxPwCTDMLastEsTimeStamp_Object = MibTableColumn
zxPwCTDMLastEsTimeStamp = _ZxPwCTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 1, 1, 11),
    _ZxPwCTDMLastEsTimeStamp_Type()
)
zxPwCTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMLastEsTimeStamp.setStatus("current")
_ZxPwCTDMCfgIndexNext_Type = Unsigned32
_ZxPwCTDMCfgIndexNext_Object = MibScalar
zxPwCTDMCfgIndexNext = _ZxPwCTDMCfgIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 2),
    _ZxPwCTDMCfgIndexNext_Type()
)
zxPwCTDMCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMCfgIndexNext.setStatus("current")
_ZxPwCTDMCfgTable_Object = MibTable
zxPwCTDMCfgTable = _ZxPwCTDMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zxPwCTDMCfgTable.setStatus("current")
_ZxPwCTDMCfgEntry_Object = MibTableRow
zxPwCTDMCfgEntry = _ZxPwCTDMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1)
)
zxPwCTDMCfgEntry.setIndexNames(
    (0, "ZXPW-TDM-MIB", "zxPwCTDMCfgIndex"),
)
if mibBuilder.loadTexts:
    zxPwCTDMCfgEntry.setStatus("current")
_ZxPwCTDMCfgIndex_Type = PwTDMCfgIndex
_ZxPwCTDMCfgIndex_Object = MibTableColumn
zxPwCTDMCfgIndex = _ZxPwCTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 1),
    _ZxPwCTDMCfgIndex_Type()
)
zxPwCTDMCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxPwCTDMCfgIndex.setStatus("current")
_ZxPwCTDMCfgRowStatus_Type = RowStatus
_ZxPwCTDMCfgRowStatus_Object = MibTableColumn
zxPwCTDMCfgRowStatus = _ZxPwCTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 2),
    _ZxPwCTDMCfgRowStatus_Type()
)
zxPwCTDMCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgRowStatus.setStatus("current")


class _ZxPwCTDMCfgConfErr_Type(Bits):
    """Custom type zxPwCTDMCfgConfErr based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("payloadSize", 1),
          ("jtrBfrDepth", 2))
    )

_ZxPwCTDMCfgConfErr_Type.__name__ = "Bits"
_ZxPwCTDMCfgConfErr_Object = MibTableColumn
zxPwCTDMCfgConfErr = _ZxPwCTDMCfgConfErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 3),
    _ZxPwCTDMCfgConfErr_Type()
)
zxPwCTDMCfgConfErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMCfgConfErr.setStatus("current")
_ZxPwCTDMCfgPayloadSize_Type = Unsigned32
_ZxPwCTDMCfgPayloadSize_Object = MibTableColumn
zxPwCTDMCfgPayloadSize = _ZxPwCTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 4),
    _ZxPwCTDMCfgPayloadSize_Type()
)
zxPwCTDMCfgPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgPayloadSize.setStatus("current")
_ZxPwCTDMCfgPktReorder_Type = TruthValue
_ZxPwCTDMCfgPktReorder_Object = MibTableColumn
zxPwCTDMCfgPktReorder = _ZxPwCTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 5),
    _ZxPwCTDMCfgPktReorder_Type()
)
zxPwCTDMCfgPktReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgPktReorder.setStatus("current")


class _ZxPwCTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type zxPwCTDMCfgRtpHdrUsed based on TruthValue"""
    defaultValue = 2


_ZxPwCTDMCfgRtpHdrUsed_Type.__name__ = "TruthValue"
_ZxPwCTDMCfgRtpHdrUsed_Object = MibTableColumn
zxPwCTDMCfgRtpHdrUsed = _ZxPwCTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 6),
    _ZxPwCTDMCfgRtpHdrUsed_Type()
)
zxPwCTDMCfgRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgRtpHdrUsed.setStatus("current")


class _ZxPwCTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type zxPwCTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3000


_ZxPwCTDMCfgJtrBfrDepth_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgJtrBfrDepth_Object = MibTableColumn
zxPwCTDMCfgJtrBfrDepth = _ZxPwCTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 7),
    _ZxPwCTDMCfgJtrBfrDepth_Type()
)
zxPwCTDMCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    zxPwCTDMCfgJtrBfrDepth.setUnits("microsecond")


class _ZxPwCTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type zxPwCTDMCfgPayloadSuppression based on Integer32"""
    defaultValue = 2

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


_ZxPwCTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_ZxPwCTDMCfgPayloadSuppression_Object = MibTableColumn
zxPwCTDMCfgPayloadSuppression = _ZxPwCTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 8),
    _ZxPwCTDMCfgPayloadSuppression_Type()
)
zxPwCTDMCfgPayloadSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgPayloadSuppression.setStatus("current")


class _ZxPwCTDMCfgConsecPktsInSynch_Type(Unsigned32):
    """Custom type zxPwCTDMCfgConsecPktsInSynch based on Unsigned32"""
    defaultValue = 2


_ZxPwCTDMCfgConsecPktsInSynch_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgConsecPktsInSynch_Object = MibTableColumn
zxPwCTDMCfgConsecPktsInSynch = _ZxPwCTDMCfgConsecPktsInSynch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 9),
    _ZxPwCTDMCfgConsecPktsInSynch_Type()
)
zxPwCTDMCfgConsecPktsInSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgConsecPktsInSynch.setStatus("current")


class _ZxPwCTDMCfgConsecMissPktsOutSynch_Type(Unsigned32):
    """Custom type zxPwCTDMCfgConsecMissPktsOutSynch based on Unsigned32"""
    defaultValue = 10


_ZxPwCTDMCfgConsecMissPktsOutSynch_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgConsecMissPktsOutSynch_Object = MibTableColumn
zxPwCTDMCfgConsecMissPktsOutSynch = _ZxPwCTDMCfgConsecMissPktsOutSynch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 10),
    _ZxPwCTDMCfgConsecMissPktsOutSynch_Type()
)
zxPwCTDMCfgConsecMissPktsOutSynch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgConsecMissPktsOutSynch.setStatus("current")


class _ZxPwCTDMCfgSetUp2SynchTimeOut_Type(Unsigned32):
    """Custom type zxPwCTDMCfgSetUp2SynchTimeOut based on Unsigned32"""
    defaultValue = 5000


_ZxPwCTDMCfgSetUp2SynchTimeOut_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgSetUp2SynchTimeOut_Object = MibTableColumn
zxPwCTDMCfgSetUp2SynchTimeOut = _ZxPwCTDMCfgSetUp2SynchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 11),
    _ZxPwCTDMCfgSetUp2SynchTimeOut_Type()
)
zxPwCTDMCfgSetUp2SynchTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgSetUp2SynchTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    zxPwCTDMCfgSetUp2SynchTimeOut.setUnits("millisecond")


class _ZxPwCTDMCfgPktReplacePolicy_Type(Integer32):
    """Custom type zxPwCTDMCfgPktReplacePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("implementationSpecific", 2))
    )


_ZxPwCTDMCfgPktReplacePolicy_Type.__name__ = "Integer32"
_ZxPwCTDMCfgPktReplacePolicy_Object = MibTableColumn
zxPwCTDMCfgPktReplacePolicy = _ZxPwCTDMCfgPktReplacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 12),
    _ZxPwCTDMCfgPktReplacePolicy_Type()
)
zxPwCTDMCfgPktReplacePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgPktReplacePolicy.setStatus("current")
_ZxPwCTDMCfgAvePktLossTimeWindow_Type = Integer32
_ZxPwCTDMCfgAvePktLossTimeWindow_Object = MibTableColumn
zxPwCTDMCfgAvePktLossTimeWindow = _ZxPwCTDMCfgAvePktLossTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 13),
    _ZxPwCTDMCfgAvePktLossTimeWindow_Type()
)
zxPwCTDMCfgAvePktLossTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgAvePktLossTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    zxPwCTDMCfgAvePktLossTimeWindow.setUnits("millisecond")
_ZxPwCTDMCfgExcessivePktLossThreshold_Type = Unsigned32
_ZxPwCTDMCfgExcessivePktLossThreshold_Object = MibTableColumn
zxPwCTDMCfgExcessivePktLossThreshold = _ZxPwCTDMCfgExcessivePktLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 14),
    _ZxPwCTDMCfgExcessivePktLossThreshold_Type()
)
zxPwCTDMCfgExcessivePktLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgExcessivePktLossThreshold.setStatus("current")


class _ZxPwCTDMCfgAlarmThreshold_Type(Unsigned32):
    """Custom type zxPwCTDMCfgAlarmThreshold based on Unsigned32"""
    defaultValue = 2500


_ZxPwCTDMCfgAlarmThreshold_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgAlarmThreshold_Object = MibTableColumn
zxPwCTDMCfgAlarmThreshold = _ZxPwCTDMCfgAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 15),
    _ZxPwCTDMCfgAlarmThreshold_Type()
)
zxPwCTDMCfgAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgAlarmThreshold.setStatus("current")


class _ZxPwCTDMCfgClearAlarmThreshold_Type(Unsigned32):
    """Custom type zxPwCTDMCfgClearAlarmThreshold based on Unsigned32"""
    defaultValue = 10000


_ZxPwCTDMCfgClearAlarmThreshold_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgClearAlarmThreshold_Object = MibTableColumn
zxPwCTDMCfgClearAlarmThreshold = _ZxPwCTDMCfgClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 16),
    _ZxPwCTDMCfgClearAlarmThreshold_Type()
)
zxPwCTDMCfgClearAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgClearAlarmThreshold.setStatus("current")


class _ZxPwCTDMCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type zxPwCTDMCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 3


_ZxPwCTDMCfgMissingPktsToSes_Type.__name__ = "Unsigned32"
_ZxPwCTDMCfgMissingPktsToSes_Object = MibTableColumn
zxPwCTDMCfgMissingPktsToSes = _ZxPwCTDMCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 17),
    _ZxPwCTDMCfgMissingPktsToSes_Type()
)
zxPwCTDMCfgMissingPktsToSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    zxPwCTDMCfgMissingPktsToSes.setUnits("seconds")


class _ZxPwCTDMCfgTimestampMode_Type(Integer32):
    """Custom type zxPwCTDMCfgTimestampMode based on Integer32"""
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
          ("absolute", 2),
          ("differential", 3))
    )


_ZxPwCTDMCfgTimestampMode_Type.__name__ = "Integer32"
_ZxPwCTDMCfgTimestampMode_Object = MibTableColumn
zxPwCTDMCfgTimestampMode = _ZxPwCTDMCfgTimestampMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 18),
    _ZxPwCTDMCfgTimestampMode_Type()
)
zxPwCTDMCfgTimestampMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgTimestampMode.setStatus("current")
_ZxPwCTDMCfgQueueSize_Type = Unsigned32
_ZxPwCTDMCfgQueueSize_Object = MibTableColumn
zxPwCTDMCfgQueueSize = _ZxPwCTDMCfgQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 19),
    _ZxPwCTDMCfgQueueSize_Type()
)
zxPwCTDMCfgQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgQueueSize.setStatus("current")


class _ZxPwCTDMCfgName_Type(DisplayString):
    """Custom type zxPwCTDMCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxPwCTDMCfgName_Type.__name__ = "DisplayString"
_ZxPwCTDMCfgName_Object = MibTableColumn
zxPwCTDMCfgName = _ZxPwCTDMCfgName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 20),
    _ZxPwCTDMCfgName_Type()
)
zxPwCTDMCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgName.setStatus("current")
_ZxPwCTDMCfgSSRC_Type = Unsigned32
_ZxPwCTDMCfgSSRC_Object = MibTableColumn
zxPwCTDMCfgSSRC = _ZxPwCTDMCfgSSRC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 21),
    _ZxPwCTDMCfgSSRC_Type()
)
zxPwCTDMCfgSSRC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgSSRC.setStatus("current")
_ZxPwCTDMCfgStorageType_Type = StorageType
_ZxPwCTDMCfgStorageType_Object = MibTableColumn
zxPwCTDMCfgStorageType = _ZxPwCTDMCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 3, 1, 22),
    _ZxPwCTDMCfgStorageType_Type()
)
zxPwCTDMCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxPwCTDMCfgStorageType.setStatus("current")
_ZxPwCTDMGlobalObjects_ObjectIdentity = ObjectIdentity
zxPwCTDMGlobalObjects = _ZxPwCTDMGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 50)
)


class _ZxPwCTDMCompatible_Type(Bits):
    """Custom type zxPwCTDMCompatible based on Bits"""
    namedValues = NamedValues(
        ("structuredCes", 0)
    )

_ZxPwCTDMCompatible_Type.__name__ = "Bits"
_ZxPwCTDMCompatible_Object = MibScalar
zxPwCTDMCompatible = _ZxPwCTDMCompatible_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 2, 1, 50, 1),
    _ZxPwCTDMCompatible_Type()
)
zxPwCTDMCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPwCTDMCompatible.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXPW-TDM-MIB",
    **{"PwTDMCfgIndex": PwTDMCfgIndex,
       "zxPwCTDMMIB": zxPwCTDMMIB,
       "zxPwCTDMObjects": zxPwCTDMObjects,
       "zxPwCTDMTable": zxPwCTDMTable,
       "zxPwCTDMEntry": zxPwCTDMEntry,
       "zxPwCTDMRate": zxPwCTDMRate,
       "zxPwCTDMIfIndex": zxPwCTDMIfIndex,
       "zxPwCGenTDMCfgIndex": zxPwCGenTDMCfgIndex,
       "zxPwCRelTDMCfgIndex": zxPwCRelTDMCfgIndex,
       "zxPwCTDMConfigError": zxPwCTDMConfigError,
       "zxPwCTDMTimeElapsed": zxPwCTDMTimeElapsed,
       "zxPwCTDMValidIntervals": zxPwCTDMValidIntervals,
       "zxPwCTDMValidDayIntervals": zxPwCTDMValidDayIntervals,
       "zxPwCTDMCurrentIndications": zxPwCTDMCurrentIndications,
       "zxPwCTDMLatchedIndications": zxPwCTDMLatchedIndications,
       "zxPwCTDMLastEsTimeStamp": zxPwCTDMLastEsTimeStamp,
       "zxPwCTDMCfgIndexNext": zxPwCTDMCfgIndexNext,
       "zxPwCTDMCfgTable": zxPwCTDMCfgTable,
       "zxPwCTDMCfgEntry": zxPwCTDMCfgEntry,
       "zxPwCTDMCfgIndex": zxPwCTDMCfgIndex,
       "zxPwCTDMCfgRowStatus": zxPwCTDMCfgRowStatus,
       "zxPwCTDMCfgConfErr": zxPwCTDMCfgConfErr,
       "zxPwCTDMCfgPayloadSize": zxPwCTDMCfgPayloadSize,
       "zxPwCTDMCfgPktReorder": zxPwCTDMCfgPktReorder,
       "zxPwCTDMCfgRtpHdrUsed": zxPwCTDMCfgRtpHdrUsed,
       "zxPwCTDMCfgJtrBfrDepth": zxPwCTDMCfgJtrBfrDepth,
       "zxPwCTDMCfgPayloadSuppression": zxPwCTDMCfgPayloadSuppression,
       "zxPwCTDMCfgConsecPktsInSynch": zxPwCTDMCfgConsecPktsInSynch,
       "zxPwCTDMCfgConsecMissPktsOutSynch": zxPwCTDMCfgConsecMissPktsOutSynch,
       "zxPwCTDMCfgSetUp2SynchTimeOut": zxPwCTDMCfgSetUp2SynchTimeOut,
       "zxPwCTDMCfgPktReplacePolicy": zxPwCTDMCfgPktReplacePolicy,
       "zxPwCTDMCfgAvePktLossTimeWindow": zxPwCTDMCfgAvePktLossTimeWindow,
       "zxPwCTDMCfgExcessivePktLossThreshold": zxPwCTDMCfgExcessivePktLossThreshold,
       "zxPwCTDMCfgAlarmThreshold": zxPwCTDMCfgAlarmThreshold,
       "zxPwCTDMCfgClearAlarmThreshold": zxPwCTDMCfgClearAlarmThreshold,
       "zxPwCTDMCfgMissingPktsToSes": zxPwCTDMCfgMissingPktsToSes,
       "zxPwCTDMCfgTimestampMode": zxPwCTDMCfgTimestampMode,
       "zxPwCTDMCfgQueueSize": zxPwCTDMCfgQueueSize,
       "zxPwCTDMCfgName": zxPwCTDMCfgName,
       "zxPwCTDMCfgSSRC": zxPwCTDMCfgSSRC,
       "zxPwCTDMCfgStorageType": zxPwCTDMCfgStorageType,
       "zxPwCTDMGlobalObjects": zxPwCTDMGlobalObjects,
       "zxPwCTDMCompatible": zxPwCTDMCompatible}
)
