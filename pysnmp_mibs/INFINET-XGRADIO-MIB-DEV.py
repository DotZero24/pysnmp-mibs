# SNMP MIB module (INFINET-XGRADIO-MIB-DEV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-XGRADIO-MIB-DEV
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:12 2025
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

(xg,) = mibBuilder.importSymbols(
    "INFINET-XG-MIB",
    "xg")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

xgRadio = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xgRadio.setRevisions(
        ("2015-11-02 11:29",
         "2015-10-13 11:01",
         "2015-07-31 10:52",
         "2015-07-01 09:28",
         "2015-01-29 07:20",
         "2014-10-28 05:59",
         "2014-10-28 05:50",
         "2014-09-30 03:50",
         "2014-09-29 06:45",
         "2014-09-04 05:02",
         "2014-09-03 10:48",
         "2014-08-29 02:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XgRfCfg_ObjectIdentity = ObjectIdentity
xgRfCfg = _XgRfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1)
)


class _XgUnitType_Type(Integer32):
    """Custom type xgUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_XgUnitType_Type.__name__ = "Integer32"
_XgUnitType_Object = MibScalar
xgUnitType = _XgUnitType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 1),
    _XgUnitType_Type()
)
xgUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgUnitType.setStatus("current")


class _XgCellId_Type(Integer32):
    """Custom type xgCellId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 167),
    )


_XgCellId_Type.__name__ = "Integer32"
_XgCellId_Object = MibScalar
xgCellId = _XgCellId_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 2),
    _XgCellId_Type()
)
xgCellId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCellId.setStatus("current")


class _XgQosStrategy_Type(Integer32):
    """Custom type xgQosStrategy based on Integer32"""
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
        *(("normal", 0),
          ("conservative", 1),
          ("aggressive", 2),
          ("off", 3))
    )


_XgQosStrategy_Type.__name__ = "Integer32"
_XgQosStrategy_Object = MibScalar
xgQosStrategy = _XgQosStrategy_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 3),
    _XgQosStrategy_Type()
)
xgQosStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgQosStrategy.setStatus("current")


class _XgDlQuota_Type(Integer32):
    """Custom type xgDlQuota based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_XgDlQuota_Type.__name__ = "Integer32"
_XgDlQuota_Object = MibScalar
xgDlQuota = _XgDlQuota_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 4),
    _XgDlQuota_Type()
)
xgDlQuota.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgDlQuota.setStatus("current")


class _XgFrameLength_Type(Integer32):
    """Custom type xgFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("len-1-ms", 1),
          ("len-2-ms", 2),
          ("len-4-ms", 4),
          ("len-5-ms", 5),
          ("len-8-ms", 8),
          ("len-10-ms", 10))
    )


_XgFrameLength_Type.__name__ = "Integer32"
_XgFrameLength_Object = MibScalar
xgFrameLength = _XgFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 5),
    _XgFrameLength_Type()
)
xgFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgFrameLength.setStatus("current")


class _XgMaxDistance_Type(Integer32):
    """Custom type xgMaxDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59600),
    )


_XgMaxDistance_Type.__name__ = "Integer32"
_XgMaxDistance_Object = MibScalar
xgMaxDistance = _XgMaxDistance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 6),
    _XgMaxDistance_Type()
)
xgMaxDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgMaxDistance.setStatus("current")


class _XgChannelWidth_Type(Integer32):
    """Custom type xgChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              40)
        )
    )
    namedValues = NamedValues(
        *(("band-10-mhz", 10),
          ("band-20-mhz", 20),
          ("band-40-mhz", 40))
    )


_XgChannelWidth_Type.__name__ = "Integer32"
_XgChannelWidth_Object = MibScalar
xgChannelWidth = _XgChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 7),
    _XgChannelWidth_Type()
)
xgChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgChannelWidth.setStatus("current")
_XgCarrierCfgTable_Object = MibTable
xgCarrierCfgTable = _XgCarrierCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    xgCarrierCfgTable.setStatus("current")
_XgCarrierCfgEntry_Object = MibTableRow
xgCarrierCfgEntry = _XgCarrierCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1)
)
xgCarrierCfgEntry.setIndexNames(
    (0, "INFINET-XGRADIO-MIB-DEV", "xgCCIndex"),
)
if mibBuilder.loadTexts:
    xgCarrierCfgEntry.setStatus("current")


class _XgCCIndex_Type(Integer32):
    """Custom type xgCCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XgCCIndex_Type.__name__ = "Integer32"
_XgCCIndex_Object = MibTableColumn
xgCCIndex = _XgCCIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 1),
    _XgCCIndex_Type()
)
xgCCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgCCIndex.setStatus("current")


class _XgCcMaxTxPwr_Type(Integer32):
    """Custom type xgCcMaxTxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 27000),
    )


_XgCcMaxTxPwr_Type.__name__ = "Integer32"
_XgCcMaxTxPwr_Object = MibTableColumn
xgCcMaxTxPwr = _XgCcMaxTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 2),
    _XgCcMaxTxPwr_Type()
)
xgCcMaxTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCcMaxTxPwr.setStatus("current")
_XgCcFreqDl_Type = Integer32
_XgCcFreqDl_Object = MibTableColumn
xgCcFreqDl = _XgCcFreqDl_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 3),
    _XgCcFreqDl_Type()
)
xgCcFreqDl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCcFreqDl.setStatus("current")
_XgCcFreqUl_Type = Integer32
_XgCcFreqUl_Object = MibTableColumn
xgCcFreqUl = _XgCcFreqUl_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 4),
    _XgCcFreqUl_Type()
)
xgCcFreqUl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCcFreqUl.setStatus("current")


class _XgCcAmcMode_Type(Integer32):
    """Custom type xgCcAmcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_XgCcAmcMode_Type.__name__ = "Integer32"
_XgCcAmcMode_Object = MibTableColumn
xgCcAmcMode = _XgCcAmcMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 5),
    _XgCcAmcMode_Type()
)
xgCcAmcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCcAmcMode.setStatus("current")


class _XgCcAmcStrategy_Type(Integer32):
    """Custom type xgCcAmcStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("conservative", 1),
          ("agressive", 2))
    )


_XgCcAmcStrategy_Type.__name__ = "Integer32"
_XgCcAmcStrategy_Object = MibTableColumn
xgCcAmcStrategy = _XgCcAmcStrategy_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 8, 1, 6),
    _XgCcAmcStrategy_Type()
)
xgCcAmcStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xgCcAmcStrategy.setStatus("current")


class _XgOwnRadioIfIndex_Type(Integer32):
    """Custom type xgOwnRadioIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XgOwnRadioIfIndex_Type.__name__ = "Integer32"
_XgOwnRadioIfIndex_Object = MibScalar
xgOwnRadioIfIndex = _XgOwnRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 1, 9),
    _XgOwnRadioIfIndex_Type()
)
xgOwnRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgOwnRadioIfIndex.setStatus("current")
_XgRfStat_ObjectIdentity = ObjectIdentity
xgRfStat = _XgRfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2)
)


class _XgLinkStatus_Type(Integer32):
    """Custom type xgLinkStatus based on Integer32"""
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
        *(("stopped", 0),
          ("starting", 1),
          ("down", 2),
          ("up", 3),
          ("error", 4))
    )


_XgLinkStatus_Type.__name__ = "Integer32"
_XgLinkStatus_Object = MibScalar
xgLinkStatus = _XgLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 1),
    _XgLinkStatus_Type()
)
xgLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgLinkStatus.setStatus("current")
_XgDistance_Type = Integer32
_XgDistance_Object = MibScalar
xgDistance = _XgDistance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 2),
    _XgDistance_Type()
)
xgDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgDistance.setStatus("current")


class _XgDlQuotaActual_Type(Integer32):
    """Custom type xgDlQuotaActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_XgDlQuotaActual_Type.__name__ = "Integer32"
_XgDlQuotaActual_Object = MibScalar
xgDlQuotaActual = _XgDlQuotaActual_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 3),
    _XgDlQuotaActual_Type()
)
xgDlQuotaActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgDlQuotaActual.setStatus("current")
_XgTotalTxAirFrames_Type = Counter32
_XgTotalTxAirFrames_Object = MibScalar
xgTotalTxAirFrames = _XgTotalTxAirFrames_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 4),
    _XgTotalTxAirFrames_Type()
)
xgTotalTxAirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalTxAirFrames.setStatus("current")
_XgTotalTxPackets_Type = Counter32
_XgTotalTxPackets_Object = MibScalar
xgTotalTxPackets = _XgTotalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 5),
    _XgTotalTxPackets_Type()
)
xgTotalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalTxPackets.setStatus("current")
_XgTotalRxAirFrames_Type = Counter32
_XgTotalRxAirFrames_Object = MibScalar
xgTotalRxAirFrames = _XgTotalRxAirFrames_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 6),
    _XgTotalRxAirFrames_Type()
)
xgTotalRxAirFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalRxAirFrames.setStatus("current")
_XgTotalRxPackets_Type = Counter32
_XgTotalRxPackets_Object = MibScalar
xgTotalRxPackets = _XgTotalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 7),
    _XgTotalRxPackets_Type()
)
xgTotalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalRxPackets.setStatus("current")
_XgTotalRxOkABs_Type = Counter32
_XgTotalRxOkABs_Object = MibScalar
xgTotalRxOkABs = _XgTotalRxOkABs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 8),
    _XgTotalRxOkABs_Type()
)
xgTotalRxOkABs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalRxOkABs.setStatus("current")
_XgTotalRxErrorABs_Type = Counter32
_XgTotalRxErrorABs_Object = MibScalar
xgTotalRxErrorABs = _XgTotalRxErrorABs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 9),
    _XgTotalRxErrorABs_Type()
)
xgTotalRxErrorABs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalRxErrorABs.setStatus("current")
_XgTotalDlCapacity_Type = Integer32
_XgTotalDlCapacity_Object = MibScalar
xgTotalDlCapacity = _XgTotalDlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 10),
    _XgTotalDlCapacity_Type()
)
xgTotalDlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalDlCapacity.setStatus("current")
_XgTotalUlCapacity_Type = Integer32
_XgTotalUlCapacity_Object = MibScalar
xgTotalUlCapacity = _XgTotalUlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 11),
    _XgTotalUlCapacity_Type()
)
xgTotalUlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalUlCapacity.setStatus("current")
_XgRfCarrierStatTable_Object = MibTable
xgRfCarrierStatTable = _XgRfCarrierStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    xgRfCarrierStatTable.setStatus("current")
_XgRfCarrierStatEntry_Object = MibTableRow
xgRfCarrierStatEntry = _XgRfCarrierStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 12, 1)
)
xgRfCarrierStatEntry.setIndexNames(
    (0, "INFINET-XGRADIO-MIB-DEV", "xgRfCarrierIndex"),
)
if mibBuilder.loadTexts:
    xgRfCarrierStatEntry.setStatus("current")


class _XgRfCarrierIndex_Type(Integer32):
    """Custom type xgRfCarrierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XgRfCarrierIndex_Type.__name__ = "Integer32"
_XgRfCarrierIndex_Object = MibTableColumn
xgRfCarrierIndex = _XgRfCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 12, 1, 1),
    _XgRfCarrierIndex_Type()
)
xgRfCarrierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRfCarrierIndex.setStatus("current")
_XgRfGoodRxFrames_Type = Counter32
_XgRfGoodRxFrames_Object = MibTableColumn
xgRfGoodRxFrames = _XgRfGoodRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 12, 1, 2),
    _XgRfGoodRxFrames_Type()
)
xgRfGoodRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRfGoodRxFrames.setStatus("current")
_XgRfBadRxFrames_Type = Counter32
_XgRfBadRxFrames_Object = MibTableColumn
xgRfBadRxFrames = _XgRfBadRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 12, 1, 3),
    _XgRfBadRxFrames_Type()
)
xgRfBadRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRfBadRxFrames.setStatus("current")
_XgRfChainStatTable_Object = MibTable
xgRfChainStatTable = _XgRfChainStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    xgRfChainStatTable.setStatus("current")
_XgRfChainStatEntry_Object = MibTableRow
xgRfChainStatEntry = _XgRfChainStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1)
)
xgRfChainStatEntry.setIndexNames(
    (0, "INFINET-XGRADIO-MIB-DEV", "xgRfChainCarrierIndex"),
    (0, "INFINET-XGRADIO-MIB-DEV", "xgRfChainStreamIndex"),
)
if mibBuilder.loadTexts:
    xgRfChainStatEntry.setStatus("current")


class _XgRfChainCarrierIndex_Type(Integer32):
    """Custom type xgRfChainCarrierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XgRfChainCarrierIndex_Type.__name__ = "Integer32"
_XgRfChainCarrierIndex_Object = MibTableColumn
xgRfChainCarrierIndex = _XgRfChainCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 1),
    _XgRfChainCarrierIndex_Type()
)
xgRfChainCarrierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRfChainCarrierIndex.setStatus("current")


class _XgRfChainStreamIndex_Type(Integer32):
    """Custom type xgRfChainStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XgRfChainStreamIndex_Type.__name__ = "Integer32"
_XgRfChainStreamIndex_Object = MibTableColumn
xgRfChainStreamIndex = _XgRfChainStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 2),
    _XgRfChainStreamIndex_Type()
)
xgRfChainStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRfChainStreamIndex.setStatus("current")


class _XgTxMCS_Type(Integer32):
    """Custom type xgTxMCS based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("qpsk-1-2", 1),
          ("qpsk-3-4", 2),
          ("qam16-1-2", 3),
          ("qam16-3-4", 4),
          ("qam64-4-6", 5),
          ("qam256-5-8", 6),
          ("qam256-6-8", 7),
          ("qam256-7-8", 8),
          ("qam256-30-32", 9),
          ("qam1024-8-10", 10))
    )


_XgTxMCS_Type.__name__ = "Integer32"
_XgTxMCS_Object = MibTableColumn
xgTxMCS = _XgTxMCS_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 3),
    _XgTxMCS_Type()
)
xgTxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTxMCS.setStatus("current")


class _XgRxMCS_Type(Integer32):
    """Custom type xgRxMCS based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("qpsk-1-2", 1),
          ("qpsk-3-4", 2),
          ("qam16-1-2", 3),
          ("qam16-3-4", 4),
          ("qam64-4-6", 5),
          ("qam256-5-8", 6),
          ("qam256-6-8", 7),
          ("qam256-7-8", 8),
          ("qam256-30-32", 9),
          ("qam1024-8-10", 10))
    )


_XgRxMCS_Type.__name__ = "Integer32"
_XgRxMCS_Object = MibTableColumn
xgRxMCS = _XgRxMCS_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 4),
    _XgRxMCS_Type()
)
xgRxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRxMCS.setStatus("current")
_XgCINR_Type = Integer32
_XgCINR_Object = MibTableColumn
xgCINR = _XgCINR_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 5),
    _XgCINR_Type()
)
xgCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgCINR.setStatus("current")
_XgABSRSSI_Type = Integer32
_XgABSRSSI_Object = MibTableColumn
xgABSRSSI = _XgABSRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 6),
    _XgABSRSSI_Type()
)
xgABSRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgABSRSSI.setStatus("current")
_XgRxOkABs_Type = Counter32
_XgRxOkABs_Object = MibTableColumn
xgRxOkABs = _XgRxOkABs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 7),
    _XgRxOkABs_Type()
)
xgRxOkABs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRxOkABs.setStatus("current")
_XgRxErrorABs_Type = Counter32
_XgRxErrorABs_Object = MibTableColumn
xgRxErrorABs = _XgRxErrorABs_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 8),
    _XgRxErrorABs_Type()
)
xgRxErrorABs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgRxErrorABs.setStatus("current")


class _XgTxPwrActual_Type(Integer32):
    """Custom type xgTxPwrActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2700),
    )


_XgTxPwrActual_Type.__name__ = "Integer32"
_XgTxPwrActual_Object = MibTableColumn
xgTxPwrActual = _XgTxPwrActual_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 9),
    _XgTxPwrActual_Type()
)
xgTxPwrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTxPwrActual.setStatus("current")
_XgADCRSSI_Type = Integer32
_XgADCRSSI_Object = MibTableColumn
xgADCRSSI = _XgADCRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 10),
    _XgADCRSSI_Type()
)
xgADCRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgADCRSSI.setStatus("current")
_XgTxGain_Type = Integer32
_XgTxGain_Object = MibTableColumn
xgTxGain = _XgTxGain_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 11),
    _XgTxGain_Type()
)
xgTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTxGain.setStatus("current")
_XgBerAmcCorrection_Type = Integer32
_XgBerAmcCorrection_Object = MibTableColumn
xgBerAmcCorrection = _XgBerAmcCorrection_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 12),
    _XgBerAmcCorrection_Type()
)
xgBerAmcCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgBerAmcCorrection.setStatus("current")
_XgBerAmcWindowErr_Type = Integer32
_XgBerAmcWindowErr_Object = MibTableColumn
xgBerAmcWindowErr = _XgBerAmcWindowErr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 13),
    _XgBerAmcWindowErr_Type()
)
xgBerAmcWindowErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgBerAmcWindowErr.setStatus("current")
_XgBerAmcOneMinuteErr_Type = Integer32
_XgBerAmcOneMinuteErr_Object = MibTableColumn
xgBerAmcOneMinuteErr = _XgBerAmcOneMinuteErr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 14),
    _XgBerAmcOneMinuteErr_Type()
)
xgBerAmcOneMinuteErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgBerAmcOneMinuteErr.setStatus("current")
_XgBerAmcTenMinutesErr_Type = Integer32
_XgBerAmcTenMinutesErr_Object = MibTableColumn
xgBerAmcTenMinutesErr = _XgBerAmcTenMinutesErr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 15),
    _XgBerAmcTenMinutesErr_Type()
)
xgBerAmcTenMinutesErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgBerAmcTenMinutesErr.setStatus("current")
_XgBerAmcOneHourErr_Type = Integer32
_XgBerAmcOneHourErr_Object = MibTableColumn
xgBerAmcOneHourErr = _XgBerAmcOneHourErr_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 16),
    _XgBerAmcOneHourErr_Type()
)
xgBerAmcOneHourErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgBerAmcOneHourErr.setStatus("current")
_XgSTOD_Type = Integer32
_XgSTOD_Object = MibTableColumn
xgSTOD = _XgSTOD_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 13, 1, 17),
    _XgSTOD_Type()
)
xgSTOD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgSTOD.setStatus("current")
_XgCatalinaTemp_Type = Integer32
_XgCatalinaTemp_Object = MibScalar
xgCatalinaTemp = _XgCatalinaTemp_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 14),
    _XgCatalinaTemp_Type()
)
xgCatalinaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgCatalinaTemp.setStatus("current")
_XgTotalTxOctets_Type = Counter32
_XgTotalTxOctets_Object = MibScalar
xgTotalTxOctets = _XgTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 15),
    _XgTotalTxOctets_Type()
)
xgTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalTxOctets.setStatus("current")
_XgTotalRxOctets_Type = Counter32
_XgTotalRxOctets_Object = MibScalar
xgTotalRxOctets = _XgTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 2, 16),
    _XgTotalRxOctets_Type()
)
xgTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgTotalRxOctets.setStatus("current")
_XgRadioMIBConformance_ObjectIdentity = ObjectIdentity
xgRadioMIBConformance = _XgRadioMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 3)
)
_XgRadioMIBCompliances_ObjectIdentity = ObjectIdentity
xgRadioMIBCompliances = _XgRadioMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 3, 1)
)
_XgRadioMIBGroups_ObjectIdentity = ObjectIdentity
xgRadioMIBGroups = _XgRadioMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 3, 2)
)

# Managed Objects groups

xgRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 3, 2, 1)
)
xgRadioGroup.setObjects(
      *(("INFINET-XGRADIO-MIB-DEV", "xgUnitType"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCellId"),
        ("INFINET-XGRADIO-MIB-DEV", "xgQosStrategy"),
        ("INFINET-XGRADIO-MIB-DEV", "xgDlQuota"),
        ("INFINET-XGRADIO-MIB-DEV", "xgFrameLength"),
        ("INFINET-XGRADIO-MIB-DEV", "xgMaxDistance"),
        ("INFINET-XGRADIO-MIB-DEV", "xgChannelWidth"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCCIndex"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCcMaxTxPwr"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCcFreqDl"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCcFreqUl"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCcAmcMode"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCcAmcStrategy"),
        ("INFINET-XGRADIO-MIB-DEV", "xgOwnRadioIfIndex"),
        ("INFINET-XGRADIO-MIB-DEV", "xgLinkStatus"),
        ("INFINET-XGRADIO-MIB-DEV", "xgDistance"),
        ("INFINET-XGRADIO-MIB-DEV", "xgDlQuotaActual"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalTxAirFrames"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalTxPackets"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalRxAirFrames"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalRxPackets"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalRxOkABs"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalRxErrorABs"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalDlCapacity"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalUlCapacity"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRfCarrierIndex"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRfGoodRxFrames"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRfBadRxFrames"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRfChainCarrierIndex"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRfChainStreamIndex"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTxMCS"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRxMCS"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCINR"),
        ("INFINET-XGRADIO-MIB-DEV", "xgABSRSSI"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRxOkABs"),
        ("INFINET-XGRADIO-MIB-DEV", "xgRxErrorABs"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTxPwrActual"),
        ("INFINET-XGRADIO-MIB-DEV", "xgADCRSSI"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTxGain"),
        ("INFINET-XGRADIO-MIB-DEV", "xgBerAmcCorrection"),
        ("INFINET-XGRADIO-MIB-DEV", "xgBerAmcWindowErr"),
        ("INFINET-XGRADIO-MIB-DEV", "xgBerAmcOneMinuteErr"),
        ("INFINET-XGRADIO-MIB-DEV", "xgBerAmcTenMinutesErr"),
        ("INFINET-XGRADIO-MIB-DEV", "xgBerAmcOneHourErr"),
        ("INFINET-XGRADIO-MIB-DEV", "xgSTOD"),
        ("INFINET-XGRADIO-MIB-DEV", "xgCatalinaTemp"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalTxOctets"),
        ("INFINET-XGRADIO-MIB-DEV", "xgTotalRxOctets"))
)
if mibBuilder.loadTexts:
    xgRadioGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xgRadioMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 1, 3, 1, 1)
)
xgRadioMIBCompliance.setObjects(
    ("INFINET-XGRADIO-MIB-DEV", "xgRadioGroup")
)
if mibBuilder.loadTexts:
    xgRadioMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-XGRADIO-MIB-DEV",
    **{"xgRadio": xgRadio,
       "xgRfCfg": xgRfCfg,
       "xgUnitType": xgUnitType,
       "xgCellId": xgCellId,
       "xgQosStrategy": xgQosStrategy,
       "xgDlQuota": xgDlQuota,
       "xgFrameLength": xgFrameLength,
       "xgMaxDistance": xgMaxDistance,
       "xgChannelWidth": xgChannelWidth,
       "xgCarrierCfgTable": xgCarrierCfgTable,
       "xgCarrierCfgEntry": xgCarrierCfgEntry,
       "xgCCIndex": xgCCIndex,
       "xgCcMaxTxPwr": xgCcMaxTxPwr,
       "xgCcFreqDl": xgCcFreqDl,
       "xgCcFreqUl": xgCcFreqUl,
       "xgCcAmcMode": xgCcAmcMode,
       "xgCcAmcStrategy": xgCcAmcStrategy,
       "xgOwnRadioIfIndex": xgOwnRadioIfIndex,
       "xgRfStat": xgRfStat,
       "xgLinkStatus": xgLinkStatus,
       "xgDistance": xgDistance,
       "xgDlQuotaActual": xgDlQuotaActual,
       "xgTotalTxAirFrames": xgTotalTxAirFrames,
       "xgTotalTxPackets": xgTotalTxPackets,
       "xgTotalRxAirFrames": xgTotalRxAirFrames,
       "xgTotalRxPackets": xgTotalRxPackets,
       "xgTotalRxOkABs": xgTotalRxOkABs,
       "xgTotalRxErrorABs": xgTotalRxErrorABs,
       "xgTotalDlCapacity": xgTotalDlCapacity,
       "xgTotalUlCapacity": xgTotalUlCapacity,
       "xgRfCarrierStatTable": xgRfCarrierStatTable,
       "xgRfCarrierStatEntry": xgRfCarrierStatEntry,
       "xgRfCarrierIndex": xgRfCarrierIndex,
       "xgRfGoodRxFrames": xgRfGoodRxFrames,
       "xgRfBadRxFrames": xgRfBadRxFrames,
       "xgRfChainStatTable": xgRfChainStatTable,
       "xgRfChainStatEntry": xgRfChainStatEntry,
       "xgRfChainCarrierIndex": xgRfChainCarrierIndex,
       "xgRfChainStreamIndex": xgRfChainStreamIndex,
       "xgTxMCS": xgTxMCS,
       "xgRxMCS": xgRxMCS,
       "xgCINR": xgCINR,
       "xgABSRSSI": xgABSRSSI,
       "xgRxOkABs": xgRxOkABs,
       "xgRxErrorABs": xgRxErrorABs,
       "xgTxPwrActual": xgTxPwrActual,
       "xgADCRSSI": xgADCRSSI,
       "xgTxGain": xgTxGain,
       "xgBerAmcCorrection": xgBerAmcCorrection,
       "xgBerAmcWindowErr": xgBerAmcWindowErr,
       "xgBerAmcOneMinuteErr": xgBerAmcOneMinuteErr,
       "xgBerAmcTenMinutesErr": xgBerAmcTenMinutesErr,
       "xgBerAmcOneHourErr": xgBerAmcOneHourErr,
       "xgSTOD": xgSTOD,
       "xgCatalinaTemp": xgCatalinaTemp,
       "xgTotalTxOctets": xgTotalTxOctets,
       "xgTotalRxOctets": xgTotalRxOctets,
       "xgRadioMIBConformance": xgRadioMIBConformance,
       "xgRadioMIBCompliances": xgRadioMIBCompliances,
       "xgRadioMIBCompliance": xgRadioMIBCompliance,
       "xgRadioMIBGroups": xgRadioMIBGroups,
       "xgRadioGroup": xgRadioGroup}
)
