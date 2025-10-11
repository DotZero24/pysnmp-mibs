# SNMP MIB module (ADTRAN-GENERIC-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-IMA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:57 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenIma,
 adGenImaID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenIma",
    "adGenImaID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(ImaFrameLength,
 ImaGroupFailureStatus,
 ImaGroupState,
 ImaGroupSymmetry,
 ImaGroupTxClkMode,
 ImaLinkFailureStatus,
 ImaLinkState,
 ImaTestProcStatus,
 MilliSeconds) = mibBuilder.importSymbols(
    "IMA-MIB",
    "ImaFrameLength",
    "ImaGroupFailureStatus",
    "ImaGroupState",
    "ImaGroupSymmetry",
    "ImaGroupTxClkMode",
    "ImaLinkFailureStatus",
    "ImaLinkState",
    "ImaTestProcStatus",
    "MilliSeconds")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenImaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 25, 1)
)
if mibBuilder.loadTexts:
    adGenImaMIB.setRevisions(
        ("2011-10-07 00:00",
         "2008-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenImaProvisioning_ObjectIdentity = ObjectIdentity
adGenImaProvisioning = _AdGenImaProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1)
)
_AdGenImaGroupProvTable_Object = MibTable
adGenImaGroupProvTable = _AdGenImaGroupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    adGenImaGroupProvTable.setStatus("current")
_AdGenImaGroupProvEntry_Object = MibTableRow
adGenImaGroupProvEntry = _AdGenImaGroupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1)
)
adGenImaGroupProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupProvEntry.setStatus("current")


class _AdGenImaGroupVersion_Type(Integer32):
    """Custom type adGenImaGroupVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1Point0Alt", 1),
          ("version1Point1", 2),
          ("version1Point0", 3))
    )


_AdGenImaGroupVersion_Type.__name__ = "Integer32"
_AdGenImaGroupVersion_Object = MibTableColumn
adGenImaGroupVersion = _AdGenImaGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 1),
    _AdGenImaGroupVersion_Type()
)
adGenImaGroupVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupVersion.setStatus("current")


class _AdGenImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type adGenImaGroupSymmetry based on ImaGroupSymmetry"""
    defaultValue = 1


_AdGenImaGroupSymmetry_Type.__name__ = "ImaGroupSymmetry"
_AdGenImaGroupSymmetry_Object = MibTableColumn
adGenImaGroupSymmetry = _AdGenImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 2),
    _AdGenImaGroupSymmetry_Type()
)
adGenImaGroupSymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupSymmetry.setStatus("current")


class _AdGenImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):
    """Custom type adGenImaGroupNeTxClkMode based on ImaGroupTxClkMode"""
    defaultValue = 1


_AdGenImaGroupNeTxClkMode_Type.__name__ = "ImaGroupTxClkMode"
_AdGenImaGroupNeTxClkMode_Object = MibTableColumn
adGenImaGroupNeTxClkMode = _AdGenImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 3),
    _AdGenImaGroupNeTxClkMode_Type()
)
adGenImaGroupNeTxClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupNeTxClkMode.setStatus("current")


class _AdGenImaGroupTxImaId_Type(Integer32):
    """Custom type adGenImaGroupTxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenImaGroupTxImaId_Type.__name__ = "Integer32"
_AdGenImaGroupTxImaId_Object = MibTableColumn
adGenImaGroupTxImaId = _AdGenImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 4),
    _AdGenImaGroupTxImaId_Type()
)
adGenImaGroupTxImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTxImaId.setStatus("current")


class _AdGenImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type adGenImaGroupTxFrameLength based on ImaFrameLength"""
    defaultValue = 128


_AdGenImaGroupTxFrameLength_Type.__name__ = "ImaFrameLength"
_AdGenImaGroupTxFrameLength_Object = MibTableColumn
adGenImaGroupTxFrameLength = _AdGenImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 5),
    _AdGenImaGroupTxFrameLength_Type()
)
adGenImaGroupTxFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTxFrameLength.setStatus("current")


class _AdGenImaGroupDiffDelayMax_Type(MilliSeconds):
    """Custom type adGenImaGroupDiffDelayMax based on MilliSeconds"""
    defaultValue = 25


_AdGenImaGroupDiffDelayMax_Type.__name__ = "MilliSeconds"
_AdGenImaGroupDiffDelayMax_Object = MibTableColumn
adGenImaGroupDiffDelayMax = _AdGenImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 6),
    _AdGenImaGroupDiffDelayMax_Type()
)
adGenImaGroupDiffDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupDiffDelayMax.setStatus("current")


class _AdGenImaGroupAlphaValue_Type(Integer32):
    """Custom type adGenImaGroupAlphaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdGenImaGroupAlphaValue_Type.__name__ = "Integer32"
_AdGenImaGroupAlphaValue_Object = MibTableColumn
adGenImaGroupAlphaValue = _AdGenImaGroupAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 7),
    _AdGenImaGroupAlphaValue_Type()
)
adGenImaGroupAlphaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupAlphaValue.setStatus("current")


class _AdGenImaGroupBetaValue_Type(Integer32):
    """Custom type adGenImaGroupBetaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AdGenImaGroupBetaValue_Type.__name__ = "Integer32"
_AdGenImaGroupBetaValue_Object = MibTableColumn
adGenImaGroupBetaValue = _AdGenImaGroupBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 8),
    _AdGenImaGroupBetaValue_Type()
)
adGenImaGroupBetaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupBetaValue.setStatus("current")


class _AdGenImaGroupGammaValue_Type(Integer32):
    """Custom type adGenImaGroupGammaValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AdGenImaGroupGammaValue_Type.__name__ = "Integer32"
_AdGenImaGroupGammaValue_Object = MibTableColumn
adGenImaGroupGammaValue = _AdGenImaGroupGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 9),
    _AdGenImaGroupGammaValue_Type()
)
adGenImaGroupGammaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupGammaValue.setStatus("current")


class _AdGenImaGroupTxClkSource_Type(Integer32):
    """Custom type adGenImaGroupTxClkSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("loop", 2))
    )


_AdGenImaGroupTxClkSource_Type.__name__ = "Integer32"
_AdGenImaGroupTxClkSource_Object = MibTableColumn
adGenImaGroupTxClkSource = _AdGenImaGroupTxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 1, 1, 10),
    _AdGenImaGroupTxClkSource_Type()
)
adGenImaGroupTxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTxClkSource.setStatus("current")
_AdGenImaAtmGroupCommonProvTable_Object = MibTable
adGenImaAtmGroupCommonProvTable = _AdGenImaAtmGroupCommonProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 2)
)
if mibBuilder.loadTexts:
    adGenImaAtmGroupCommonProvTable.setStatus("current")
_AdGenImaAtmGroupCommonProvEntry_Object = MibTableRow
adGenImaAtmGroupCommonProvEntry = _AdGenImaAtmGroupCommonProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 2, 1)
)
adGenImaAtmGroupCommonProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaAtmGroupCommonProvEntry.setStatus("current")


class _AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type(DisplayString):
    """Custom type adGenImaAtmGroupCommonProvDhcpCircuitIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type.__name__ = "DisplayString"
_AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Object = MibTableColumn
adGenImaAtmGroupCommonProvDhcpCircuitIdFormat = _AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 1, 2, 1, 1),
    _AdGenImaAtmGroupCommonProvDhcpCircuitIdFormat_Type()
)
adGenImaAtmGroupCommonProvDhcpCircuitIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaAtmGroupCommonProvDhcpCircuitIdFormat.setStatus("current")
_AdGenImaStatus_ObjectIdentity = ObjectIdentity
adGenImaStatus = _AdGenImaStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2)
)
_AdGenImaGroupStatusTable_Object = MibTable
adGenImaGroupStatusTable = _AdGenImaGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    adGenImaGroupStatusTable.setStatus("current")
_AdGenImaGroupStatusEntry_Object = MibTableRow
adGenImaGroupStatusEntry = _AdGenImaGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1)
)
adGenImaGroupStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupStatusEntry.setStatus("current")
_AdGenImaGroupNeState_Type = ImaGroupState
_AdGenImaGroupNeState_Object = MibTableColumn
adGenImaGroupNeState = _AdGenImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 1),
    _AdGenImaGroupNeState_Type()
)
adGenImaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupNeState.setStatus("current")
_AdGenImaGroupFeState_Type = ImaGroupState
_AdGenImaGroupFeState_Object = MibTableColumn
adGenImaGroupFeState = _AdGenImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 2),
    _AdGenImaGroupFeState_Type()
)
adGenImaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupFeState.setStatus("current")
_AdGenImaGroupFailureStatus_Type = ImaGroupFailureStatus
_AdGenImaGroupFailureStatus_Object = MibTableColumn
adGenImaGroupFailureStatus = _AdGenImaGroupFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 3),
    _AdGenImaGroupFailureStatus_Type()
)
adGenImaGroupFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupFailureStatus.setStatus("current")
_AdGenImaGroupLastChange_Type = DateAndTime
_AdGenImaGroupLastChange_Object = MibTableColumn
adGenImaGroupLastChange = _AdGenImaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 4),
    _AdGenImaGroupLastChange_Type()
)
adGenImaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupLastChange.setStatus("current")
_AdGenImaGroupRunningSecs_Type = Gauge32
_AdGenImaGroupRunningSecs_Object = MibTableColumn
adGenImaGroupRunningSecs = _AdGenImaGroupRunningSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 5),
    _AdGenImaGroupRunningSecs_Type()
)
adGenImaGroupRunningSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRunningSecs.setStatus("current")
_AdGenImaGroupFeTxClkMode_Type = ImaGroupTxClkMode
_AdGenImaGroupFeTxClkMode_Object = MibTableColumn
adGenImaGroupFeTxClkMode = _AdGenImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 6),
    _AdGenImaGroupFeTxClkMode_Type()
)
adGenImaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupFeTxClkMode.setStatus("current")
_AdGenImaGroupTxTimingRefLink_Type = InterfaceIndexOrZero
_AdGenImaGroupTxTimingRefLink_Object = MibTableColumn
adGenImaGroupTxTimingRefLink = _AdGenImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 7),
    _AdGenImaGroupTxTimingRefLink_Type()
)
adGenImaGroupTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTxTimingRefLink.setStatus("current")
_AdGenImaGroupRxTimingRefLink_Type = InterfaceIndexOrZero
_AdGenImaGroupRxTimingRefLink_Object = MibTableColumn
adGenImaGroupRxTimingRefLink = _AdGenImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 8),
    _AdGenImaGroupRxTimingRefLink_Type()
)
adGenImaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRxTimingRefLink.setStatus("current")


class _AdGenImaGroupRxImaId_Type(Integer32):
    """Custom type adGenImaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenImaGroupRxImaId_Type.__name__ = "Integer32"
_AdGenImaGroupRxImaId_Object = MibTableColumn
adGenImaGroupRxImaId = _AdGenImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 9),
    _AdGenImaGroupRxImaId_Type()
)
adGenImaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRxImaId.setStatus("current")
_AdGenImaGroupRxFrameLength_Type = ImaFrameLength
_AdGenImaGroupRxFrameLength_Object = MibTableColumn
adGenImaGroupRxFrameLength = _AdGenImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 10),
    _AdGenImaGroupRxFrameLength_Type()
)
adGenImaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRxFrameLength.setStatus("current")
_AdGenImaGroupLeastDelayLink_Type = InterfaceIndexOrZero
_AdGenImaGroupLeastDelayLink_Object = MibTableColumn
adGenImaGroupLeastDelayLink = _AdGenImaGroupLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 11),
    _AdGenImaGroupLeastDelayLink_Type()
)
adGenImaGroupLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupLeastDelayLink.setStatus("current")
_AdGenImaGroupDiffDelayMaxObs_Type = MilliSeconds
_AdGenImaGroupDiffDelayMaxObs_Object = MibTableColumn
adGenImaGroupDiffDelayMaxObs = _AdGenImaGroupDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 12),
    _AdGenImaGroupDiffDelayMaxObs_Type()
)
adGenImaGroupDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDiffDelayMaxObs.setStatus("current")
_AdGenImaGroupTxAvailCellRate_Type = Gauge32
_AdGenImaGroupTxAvailCellRate_Object = MibTableColumn
adGenImaGroupTxAvailCellRate = _AdGenImaGroupTxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 13),
    _AdGenImaGroupTxAvailCellRate_Type()
)
adGenImaGroupTxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTxAvailCellRate.setStatus("current")
_AdGenImaGroupRxAvailCellRate_Type = Gauge32
_AdGenImaGroupRxAvailCellRate_Object = MibTableColumn
adGenImaGroupRxAvailCellRate = _AdGenImaGroupRxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 14),
    _AdGenImaGroupRxAvailCellRate_Type()
)
adGenImaGroupRxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRxAvailCellRate.setStatus("current")


class _AdGenImaGroupTxOamLabelValue_Type(Integer32):
    """Custom type adGenImaGroupTxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenImaGroupTxOamLabelValue_Type.__name__ = "Integer32"
_AdGenImaGroupTxOamLabelValue_Object = MibTableColumn
adGenImaGroupTxOamLabelValue = _AdGenImaGroupTxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 15),
    _AdGenImaGroupTxOamLabelValue_Type()
)
adGenImaGroupTxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTxOamLabelValue.setStatus("current")


class _AdGenImaGroupRxOamLabelValue_Type(Integer32):
    """Custom type adGenImaGroupRxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenImaGroupRxOamLabelValue_Type.__name__ = "Integer32"
_AdGenImaGroupRxOamLabelValue_Object = MibTableColumn
adGenImaGroupRxOamLabelValue = _AdGenImaGroupRxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 1, 1, 16),
    _AdGenImaGroupRxOamLabelValue_Type()
)
adGenImaGroupRxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupRxOamLabelValue.setStatus("current")
_AdGenImaLinkStatusTable_Object = MibTable
adGenImaLinkStatusTable = _AdGenImaLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2)
)
if mibBuilder.loadTexts:
    adGenImaLinkStatusTable.setStatus("current")
_AdGenImaLinkStatusEntry_Object = MibTableRow
adGenImaLinkStatusEntry = _AdGenImaLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1)
)
adGenImaLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkStatusEntry.setStatus("current")
_AdGenImaLinkNeTxState_Type = ImaLinkState
_AdGenImaLinkNeTxState_Object = MibTableColumn
adGenImaLinkNeTxState = _AdGenImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 1),
    _AdGenImaLinkNeTxState_Type()
)
adGenImaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeTxState.setStatus("current")
_AdGenImaLinkNeRxState_Type = ImaLinkState
_AdGenImaLinkNeRxState_Object = MibTableColumn
adGenImaLinkNeRxState = _AdGenImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 2),
    _AdGenImaLinkNeRxState_Type()
)
adGenImaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeRxState.setStatus("current")
_AdGenImaLinkFeTxState_Type = ImaLinkState
_AdGenImaLinkFeTxState_Object = MibTableColumn
adGenImaLinkFeTxState = _AdGenImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 3),
    _AdGenImaLinkFeTxState_Type()
)
adGenImaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeTxState.setStatus("current")
_AdGenImaLinkFeRxState_Type = ImaLinkState
_AdGenImaLinkFeRxState_Object = MibTableColumn
adGenImaLinkFeRxState = _AdGenImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 4),
    _AdGenImaLinkFeRxState_Type()
)
adGenImaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeRxState.setStatus("current")
_AdGenImaLinkNeRxFailureStatus_Type = ImaLinkFailureStatus
_AdGenImaLinkNeRxFailureStatus_Object = MibTableColumn
adGenImaLinkNeRxFailureStatus = _AdGenImaLinkNeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 5),
    _AdGenImaLinkNeRxFailureStatus_Type()
)
adGenImaLinkNeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeRxFailureStatus.setStatus("current")
_AdGenImaLinkFeRxFailureStatus_Type = ImaLinkFailureStatus
_AdGenImaLinkFeRxFailureStatus_Object = MibTableColumn
adGenImaLinkFeRxFailureStatus = _AdGenImaLinkFeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 6),
    _AdGenImaLinkFeRxFailureStatus_Type()
)
adGenImaLinkFeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeRxFailureStatus.setStatus("current")


class _AdGenImaLinkTxLid_Type(Integer32):
    """Custom type adGenImaLinkTxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AdGenImaLinkTxLid_Type.__name__ = "Integer32"
_AdGenImaLinkTxLid_Object = MibTableColumn
adGenImaLinkTxLid = _AdGenImaLinkTxLid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 7),
    _AdGenImaLinkTxLid_Type()
)
adGenImaLinkTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTxLid.setStatus("current")


class _AdGenImaLinkRxLid_Type(Integer32):
    """Custom type adGenImaLinkRxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AdGenImaLinkRxLid_Type.__name__ = "Integer32"
_AdGenImaLinkRxLid_Object = MibTableColumn
adGenImaLinkRxLid = _AdGenImaLinkRxLid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 8),
    _AdGenImaLinkRxLid_Type()
)
adGenImaLinkRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkRxLid.setStatus("current")
_AdGenImaLinkRelDelay_Type = MilliSeconds
_AdGenImaLinkRelDelay_Object = MibTableColumn
adGenImaLinkRelDelay = _AdGenImaLinkRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 2, 2, 1, 9),
    _AdGenImaLinkRelDelay_Type()
)
adGenImaLinkRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkRelDelay.setStatus("current")
_AdGenImaTest_ObjectIdentity = ObjectIdentity
adGenImaTest = _AdGenImaTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3)
)
_AdGenImaGroupTestTable_Object = MibTable
adGenImaGroupTestTable = _AdGenImaGroupTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 1)
)
if mibBuilder.loadTexts:
    adGenImaGroupTestTable.setStatus("current")
_AdGenImaGroupTestEntry_Object = MibTableRow
adGenImaGroupTestEntry = _AdGenImaGroupTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 1, 1)
)
adGenImaGroupTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupTestEntry.setStatus("current")


class _AdGenImaGroupTestLinkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type adGenImaGroupTestLinkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_AdGenImaGroupTestLinkIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_AdGenImaGroupTestLinkIfIndex_Object = MibTableColumn
adGenImaGroupTestLinkIfIndex = _AdGenImaGroupTestLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 1, 1, 1),
    _AdGenImaGroupTestLinkIfIndex_Type()
)
adGenImaGroupTestLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTestLinkIfIndex.setStatus("current")


class _AdGenImaGroupTestPattern_Type(Integer32):
    """Custom type adGenImaGroupTestPattern based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AdGenImaGroupTestPattern_Type.__name__ = "Integer32"
_AdGenImaGroupTestPattern_Object = MibTableColumn
adGenImaGroupTestPattern = _AdGenImaGroupTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 1, 1, 2),
    _AdGenImaGroupTestPattern_Type()
)
adGenImaGroupTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTestPattern.setStatus("current")


class _AdGenImaGroupTestProcStatus_Type(ImaTestProcStatus):
    """Custom type adGenImaGroupTestProcStatus based on ImaTestProcStatus"""
    defaultValue = 1


_AdGenImaGroupTestProcStatus_Type.__name__ = "ImaTestProcStatus"
_AdGenImaGroupTestProcStatus_Object = MibTableColumn
adGenImaGroupTestProcStatus = _AdGenImaGroupTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 1, 1, 3),
    _AdGenImaGroupTestProcStatus_Type()
)
adGenImaGroupTestProcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupTestProcStatus.setStatus("current")
_AdGenImaLinkTestTable_Object = MibTable
adGenImaLinkTestTable = _AdGenImaLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 2)
)
if mibBuilder.loadTexts:
    adGenImaLinkTestTable.setStatus("current")
_AdGenImaLinkTestEntry_Object = MibTableRow
adGenImaLinkTestEntry = _AdGenImaLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 2, 1)
)
adGenImaLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkTestEntry.setStatus("current")


class _AdGenImaLinkRxTestPattern_Type(Integer32):
    """Custom type adGenImaLinkRxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenImaLinkRxTestPattern_Type.__name__ = "Integer32"
_AdGenImaLinkRxTestPattern_Object = MibTableColumn
adGenImaLinkRxTestPattern = _AdGenImaLinkRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 2, 1, 1),
    _AdGenImaLinkRxTestPattern_Type()
)
adGenImaLinkRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkRxTestPattern.setStatus("current")
_AdGenImaLinkTestProcStatus_Type = ImaTestProcStatus
_AdGenImaLinkTestProcStatus_Object = MibTableColumn
adGenImaLinkTestProcStatus = _AdGenImaLinkTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 3, 2, 1, 2),
    _AdGenImaLinkTestProcStatus_Type()
)
adGenImaLinkTestProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTestProcStatus.setStatus("current")
_AdGenImaPerformance_ObjectIdentity = ObjectIdentity
adGenImaPerformance = _AdGenImaPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4)
)
_AdGenImaGroupPerfTable_Object = MibTable
adGenImaGroupPerfTable = _AdGenImaGroupPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1)
)
if mibBuilder.loadTexts:
    adGenImaGroupPerfTable.setStatus("current")
_AdGenImaGroupPerfEntry_Object = MibTableRow
adGenImaGroupPerfEntry = _AdGenImaGroupPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1)
)
adGenImaGroupPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupPerfEntry.setStatus("current")
_AdGenImaGroupUnavailSecs_Type = Counter32
_AdGenImaGroupUnavailSecs_Object = MibTableColumn
adGenImaGroupUnavailSecs = _AdGenImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 1),
    _AdGenImaGroupUnavailSecs_Type()
)
adGenImaGroupUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupUnavailSecs.setStatus("current")
_AdGenImaGroupNeNumFailures_Type = Counter32
_AdGenImaGroupNeNumFailures_Object = MibTableColumn
adGenImaGroupNeNumFailures = _AdGenImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 2),
    _AdGenImaGroupNeNumFailures_Type()
)
adGenImaGroupNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupNeNumFailures.setStatus("current")
_AdGenImaGroupFeNumFailures_Type = Counter32
_AdGenImaGroupFeNumFailures_Object = MibTableColumn
adGenImaGroupFeNumFailures = _AdGenImaGroupFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 3),
    _AdGenImaGroupFeNumFailures_Type()
)
adGenImaGroupFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupFeNumFailures.setStatus("current")


class _AdGenImaGroupValidIntervals_Type(Integer32):
    """Custom type adGenImaGroupValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenImaGroupValidIntervals_Type.__name__ = "Integer32"
_AdGenImaGroupValidIntervals_Object = MibTableColumn
adGenImaGroupValidIntervals = _AdGenImaGroupValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 4),
    _AdGenImaGroupValidIntervals_Type()
)
adGenImaGroupValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupValidIntervals.setStatus("current")


class _AdGenImaGroupInvalidIntervals_Type(Integer32):
    """Custom type adGenImaGroupInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenImaGroupInvalidIntervals_Type.__name__ = "Integer32"
_AdGenImaGroupInvalidIntervals_Object = MibTableColumn
adGenImaGroupInvalidIntervals = _AdGenImaGroupInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 5),
    _AdGenImaGroupInvalidIntervals_Type()
)
adGenImaGroupInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupInvalidIntervals.setStatus("current")


class _AdGenImaGroupTimeElapsed_Type(Integer32):
    """Custom type adGenImaGroupTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenImaGroupTimeElapsed_Type.__name__ = "Integer32"
_AdGenImaGroupTimeElapsed_Object = MibTableColumn
adGenImaGroupTimeElapsed = _AdGenImaGroupTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 6),
    _AdGenImaGroupTimeElapsed_Type()
)
adGenImaGroupTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTimeElapsed.setStatus("current")


class _AdGenImaGroupResetStats_Type(Integer32):
    """Custom type adGenImaGroupResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenImaGroupResetStats_Type.__name__ = "Integer32"
_AdGenImaGroupResetStats_Object = MibTableColumn
adGenImaGroupResetStats = _AdGenImaGroupResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 7),
    _AdGenImaGroupResetStats_Type()
)
adGenImaGroupResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupResetStats.setStatus("current")


class _AdGenImaGroupResetPerfHistory_Type(Integer32):
    """Custom type adGenImaGroupResetPerfHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenImaGroupResetPerfHistory_Type.__name__ = "Integer32"
_AdGenImaGroupResetPerfHistory_Object = MibTableColumn
adGenImaGroupResetPerfHistory = _AdGenImaGroupResetPerfHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 1, 1, 8),
    _AdGenImaGroupResetPerfHistory_Type()
)
adGenImaGroupResetPerfHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaGroupResetPerfHistory.setStatus("current")
_AdGenImaLinkPerfTable_Object = MibTable
adGenImaLinkPerfTable = _AdGenImaLinkPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2)
)
if mibBuilder.loadTexts:
    adGenImaLinkPerfTable.setStatus("current")
_AdGenImaLinkPerfEntry_Object = MibTableRow
adGenImaLinkPerfEntry = _AdGenImaLinkPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1)
)
adGenImaLinkPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkPerfEntry.setStatus("current")
_AdGenImaLinkImaViolations_Type = Counter32
_AdGenImaLinkImaViolations_Object = MibTableColumn
adGenImaLinkImaViolations = _AdGenImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 1),
    _AdGenImaLinkImaViolations_Type()
)
adGenImaLinkImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkImaViolations.setStatus("current")
_AdGenImaLinkOifAnomalies_Type = Counter32
_AdGenImaLinkOifAnomalies_Object = MibTableColumn
adGenImaLinkOifAnomalies = _AdGenImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 2),
    _AdGenImaLinkOifAnomalies_Type()
)
adGenImaLinkOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkOifAnomalies.setStatus("current")
_AdGenImaLinkNeSevErroredSecs_Type = Counter32
_AdGenImaLinkNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkNeSevErroredSecs = _AdGenImaLinkNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 3),
    _AdGenImaLinkNeSevErroredSecs_Type()
)
adGenImaLinkNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeSevErroredSecs.setStatus("current")
_AdGenImaLinkFeSevErroredSecs_Type = Counter32
_AdGenImaLinkFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkFeSevErroredSecs = _AdGenImaLinkFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 4),
    _AdGenImaLinkFeSevErroredSecs_Type()
)
adGenImaLinkFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeSevErroredSecs.setStatus("current")
_AdGenImaLinkNeUnavailSecs_Type = Counter32
_AdGenImaLinkNeUnavailSecs_Object = MibTableColumn
adGenImaLinkNeUnavailSecs = _AdGenImaLinkNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 5),
    _AdGenImaLinkNeUnavailSecs_Type()
)
adGenImaLinkNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeUnavailSecs.setStatus("current")
_AdGenImaLinkFeUnavailSecs_Type = Counter32
_AdGenImaLinkFeUnavailSecs_Object = MibTableColumn
adGenImaLinkFeUnavailSecs = _AdGenImaLinkFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 6),
    _AdGenImaLinkFeUnavailSecs_Type()
)
adGenImaLinkFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeUnavailSecs.setStatus("current")
_AdGenImaLinkNeTxUnusableSecs_Type = Counter32
_AdGenImaLinkNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkNeTxUnusableSecs = _AdGenImaLinkNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 7),
    _AdGenImaLinkNeTxUnusableSecs_Type()
)
adGenImaLinkNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkNeRxUnusableSecs_Type = Counter32
_AdGenImaLinkNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkNeRxUnusableSecs = _AdGenImaLinkNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 8),
    _AdGenImaLinkNeRxUnusableSecs_Type()
)
adGenImaLinkNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkFeTxUnusableSecs_Type = Counter32
_AdGenImaLinkFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkFeTxUnusableSecs = _AdGenImaLinkFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 9),
    _AdGenImaLinkFeTxUnusableSecs_Type()
)
adGenImaLinkFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkFeRxUnusableSecs_Type = Counter32
_AdGenImaLinkFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkFeRxUnusableSecs = _AdGenImaLinkFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 10),
    _AdGenImaLinkFeRxUnusableSecs_Type()
)
adGenImaLinkFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkNeTxNumFailures_Type = Counter32
_AdGenImaLinkNeTxNumFailures_Object = MibTableColumn
adGenImaLinkNeTxNumFailures = _AdGenImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 11),
    _AdGenImaLinkNeTxNumFailures_Type()
)
adGenImaLinkNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeTxNumFailures.setStatus("current")
_AdGenImaLinkNeRxNumFailures_Type = Counter32
_AdGenImaLinkNeRxNumFailures_Object = MibTableColumn
adGenImaLinkNeRxNumFailures = _AdGenImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 12),
    _AdGenImaLinkNeRxNumFailures_Type()
)
adGenImaLinkNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkNeRxNumFailures.setStatus("current")
_AdGenImaLinkFeTxNumFailures_Type = Counter32
_AdGenImaLinkFeTxNumFailures_Object = MibTableColumn
adGenImaLinkFeTxNumFailures = _AdGenImaLinkFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 13),
    _AdGenImaLinkFeTxNumFailures_Type()
)
adGenImaLinkFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeTxNumFailures.setStatus("current")
_AdGenImaLinkFeRxNumFailures_Type = Counter32
_AdGenImaLinkFeRxNumFailures_Object = MibTableColumn
adGenImaLinkFeRxNumFailures = _AdGenImaLinkFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 14),
    _AdGenImaLinkFeRxNumFailures_Type()
)
adGenImaLinkFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkFeRxNumFailures.setStatus("current")
_AdGenImaLinkTxStuffs_Type = Counter32
_AdGenImaLinkTxStuffs_Object = MibTableColumn
adGenImaLinkTxStuffs = _AdGenImaLinkTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 15),
    _AdGenImaLinkTxStuffs_Type()
)
adGenImaLinkTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTxStuffs.setStatus("current")
_AdGenImaLinkRxStuffs_Type = Counter32
_AdGenImaLinkRxStuffs_Object = MibTableColumn
adGenImaLinkRxStuffs = _AdGenImaLinkRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 16),
    _AdGenImaLinkRxStuffs_Type()
)
adGenImaLinkRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkRxStuffs.setStatus("current")


class _AdGenImaLinkValidIntervals_Type(Integer32):
    """Custom type adGenImaLinkValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenImaLinkValidIntervals_Type.__name__ = "Integer32"
_AdGenImaLinkValidIntervals_Object = MibTableColumn
adGenImaLinkValidIntervals = _AdGenImaLinkValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 17),
    _AdGenImaLinkValidIntervals_Type()
)
adGenImaLinkValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkValidIntervals.setStatus("current")


class _AdGenImaLinkInvalidIntervals_Type(Integer32):
    """Custom type adGenImaLinkInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenImaLinkInvalidIntervals_Type.__name__ = "Integer32"
_AdGenImaLinkInvalidIntervals_Object = MibTableColumn
adGenImaLinkInvalidIntervals = _AdGenImaLinkInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 18),
    _AdGenImaLinkInvalidIntervals_Type()
)
adGenImaLinkInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkInvalidIntervals.setStatus("current")


class _AdGenImaLinkTimeElapsed_Type(Integer32):
    """Custom type adGenImaLinkTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenImaLinkTimeElapsed_Type.__name__ = "Integer32"
_AdGenImaLinkTimeElapsed_Object = MibTableColumn
adGenImaLinkTimeElapsed = _AdGenImaLinkTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 19),
    _AdGenImaLinkTimeElapsed_Type()
)
adGenImaLinkTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTimeElapsed.setStatus("current")


class _AdGenImaLinkResetStats_Type(Integer32):
    """Custom type adGenImaLinkResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenImaLinkResetStats_Type.__name__ = "Integer32"
_AdGenImaLinkResetStats_Object = MibTableColumn
adGenImaLinkResetStats = _AdGenImaLinkResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 20),
    _AdGenImaLinkResetStats_Type()
)
adGenImaLinkResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaLinkResetStats.setStatus("current")


class _AdGenImaLinkResetPerfHistory_Type(Integer32):
    """Custom type adGenImaLinkResetPerfHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenImaLinkResetPerfHistory_Type.__name__ = "Integer32"
_AdGenImaLinkResetPerfHistory_Object = MibTableColumn
adGenImaLinkResetPerfHistory = _AdGenImaLinkResetPerfHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 2, 1, 21),
    _AdGenImaLinkResetPerfHistory_Type()
)
adGenImaLinkResetPerfHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenImaLinkResetPerfHistory.setStatus("current")
_AdGenImaGroupCurrentTable_Object = MibTable
adGenImaGroupCurrentTable = _AdGenImaGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 3)
)
if mibBuilder.loadTexts:
    adGenImaGroupCurrentTable.setStatus("current")
_AdGenImaGroupCurrentEntry_Object = MibTableRow
adGenImaGroupCurrentEntry = _AdGenImaGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 3, 1)
)
adGenImaGroupCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupCurrentEntry.setStatus("current")
_AdGenImaGroupCurrentUnavailSecs_Type = Gauge32
_AdGenImaGroupCurrentUnavailSecs_Object = MibTableColumn
adGenImaGroupCurrentUnavailSecs = _AdGenImaGroupCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 3, 1, 1),
    _AdGenImaGroupCurrentUnavailSecs_Type()
)
adGenImaGroupCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupCurrentUnavailSecs.setStatus("current")
_AdGenImaGroupCurrentNeNumFailures_Type = Gauge32
_AdGenImaGroupCurrentNeNumFailures_Object = MibTableColumn
adGenImaGroupCurrentNeNumFailures = _AdGenImaGroupCurrentNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 3, 1, 2),
    _AdGenImaGroupCurrentNeNumFailures_Type()
)
adGenImaGroupCurrentNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupCurrentNeNumFailures.setStatus("current")
_AdGenImaGroupCurrentFeNumFailures_Type = Gauge32
_AdGenImaGroupCurrentFeNumFailures_Object = MibTableColumn
adGenImaGroupCurrentFeNumFailures = _AdGenImaGroupCurrentFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 3, 1, 3),
    _AdGenImaGroupCurrentFeNumFailures_Type()
)
adGenImaGroupCurrentFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupCurrentFeNumFailures.setStatus("current")
_AdGenImaGroupIntervalTable_Object = MibTable
adGenImaGroupIntervalTable = _AdGenImaGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4)
)
if mibBuilder.loadTexts:
    adGenImaGroupIntervalTable.setStatus("current")
_AdGenImaGroupIntervalEntry_Object = MibTableRow
adGenImaGroupIntervalEntry = _AdGenImaGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1)
)
adGenImaGroupIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-IMA-MIB", "adGenImaGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenImaGroupIntervalEntry.setStatus("current")


class _AdGenImaGroupIntervalNumber_Type(Integer32):
    """Custom type adGenImaGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenImaGroupIntervalNumber_Type.__name__ = "Integer32"
_AdGenImaGroupIntervalNumber_Object = MibTableColumn
adGenImaGroupIntervalNumber = _AdGenImaGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1, 1),
    _AdGenImaGroupIntervalNumber_Type()
)
adGenImaGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenImaGroupIntervalNumber.setStatus("current")
_AdGenImaGroupIntervalUnavailSecs_Type = Gauge32
_AdGenImaGroupIntervalUnavailSecs_Object = MibTableColumn
adGenImaGroupIntervalUnavailSecs = _AdGenImaGroupIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1, 2),
    _AdGenImaGroupIntervalUnavailSecs_Type()
)
adGenImaGroupIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupIntervalUnavailSecs.setStatus("current")
_AdGenImaGroupIntervalNeNumFailures_Type = Gauge32
_AdGenImaGroupIntervalNeNumFailures_Object = MibTableColumn
adGenImaGroupIntervalNeNumFailures = _AdGenImaGroupIntervalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1, 3),
    _AdGenImaGroupIntervalNeNumFailures_Type()
)
adGenImaGroupIntervalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupIntervalNeNumFailures.setStatus("current")
_AdGenImaGroupIntervalFeNumFailures_Type = Gauge32
_AdGenImaGroupIntervalFeNumFailures_Object = MibTableColumn
adGenImaGroupIntervalFeNumFailures = _AdGenImaGroupIntervalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1, 4),
    _AdGenImaGroupIntervalFeNumFailures_Type()
)
adGenImaGroupIntervalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupIntervalFeNumFailures.setStatus("current")
_AdGenImaGroupIntervalTimeStamp_Type = DisplayString
_AdGenImaGroupIntervalTimeStamp_Object = MibTableColumn
adGenImaGroupIntervalTimeStamp = _AdGenImaGroupIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 4, 1, 5),
    _AdGenImaGroupIntervalTimeStamp_Type()
)
adGenImaGroupIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupIntervalTimeStamp.setStatus("current")
_AdGenImaGroupTotalTable_Object = MibTable
adGenImaGroupTotalTable = _AdGenImaGroupTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 5)
)
if mibBuilder.loadTexts:
    adGenImaGroupTotalTable.setStatus("current")
_AdGenImaGroupTotalEntry_Object = MibTableRow
adGenImaGroupTotalEntry = _AdGenImaGroupTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 5, 1)
)
adGenImaGroupTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupTotalEntry.setStatus("current")
_AdGenImaGroupTotalUnavailSecs_Type = Gauge32
_AdGenImaGroupTotalUnavailSecs_Object = MibTableColumn
adGenImaGroupTotalUnavailSecs = _AdGenImaGroupTotalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 5, 1, 1),
    _AdGenImaGroupTotalUnavailSecs_Type()
)
adGenImaGroupTotalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTotalUnavailSecs.setStatus("current")
_AdGenImaGroupTotalNeNumFailures_Type = Gauge32
_AdGenImaGroupTotalNeNumFailures_Object = MibTableColumn
adGenImaGroupTotalNeNumFailures = _AdGenImaGroupTotalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 5, 1, 2),
    _AdGenImaGroupTotalNeNumFailures_Type()
)
adGenImaGroupTotalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTotalNeNumFailures.setStatus("current")
_AdGenImaGroupTotalFeNumFailures_Type = Gauge32
_AdGenImaGroupTotalFeNumFailures_Object = MibTableColumn
adGenImaGroupTotalFeNumFailures = _AdGenImaGroupTotalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 5, 1, 3),
    _AdGenImaGroupTotalFeNumFailures_Type()
)
adGenImaGroupTotalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupTotalFeNumFailures.setStatus("current")
_AdGenImaGroupDayCurrentTable_Object = MibTable
adGenImaGroupDayCurrentTable = _AdGenImaGroupDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 6)
)
if mibBuilder.loadTexts:
    adGenImaGroupDayCurrentTable.setStatus("current")
_AdGenImaGroupDayCurrentEntry_Object = MibTableRow
adGenImaGroupDayCurrentEntry = _AdGenImaGroupDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 6, 1)
)
adGenImaGroupDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaGroupDayCurrentEntry.setStatus("current")
_AdGenImaGroupDayCurrentUnavailSecs_Type = Gauge32
_AdGenImaGroupDayCurrentUnavailSecs_Object = MibTableColumn
adGenImaGroupDayCurrentUnavailSecs = _AdGenImaGroupDayCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 6, 1, 1),
    _AdGenImaGroupDayCurrentUnavailSecs_Type()
)
adGenImaGroupDayCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayCurrentUnavailSecs.setStatus("current")
_AdGenImaGroupDayCurrentNeNumFailures_Type = Gauge32
_AdGenImaGroupDayCurrentNeNumFailures_Object = MibTableColumn
adGenImaGroupDayCurrentNeNumFailures = _AdGenImaGroupDayCurrentNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 6, 1, 2),
    _AdGenImaGroupDayCurrentNeNumFailures_Type()
)
adGenImaGroupDayCurrentNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayCurrentNeNumFailures.setStatus("current")
_AdGenImaGroupDayCurrentFeNumFailures_Type = Gauge32
_AdGenImaGroupDayCurrentFeNumFailures_Object = MibTableColumn
adGenImaGroupDayCurrentFeNumFailures = _AdGenImaGroupDayCurrentFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 6, 1, 3),
    _AdGenImaGroupDayCurrentFeNumFailures_Type()
)
adGenImaGroupDayCurrentFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayCurrentFeNumFailures.setStatus("current")
_AdGenImaGroupDayIntervalTable_Object = MibTable
adGenImaGroupDayIntervalTable = _AdGenImaGroupDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7)
)
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalTable.setStatus("current")
_AdGenImaGroupDayIntervalEntry_Object = MibTableRow
adGenImaGroupDayIntervalEntry = _AdGenImaGroupDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1)
)
adGenImaGroupDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-IMA-MIB", "adGenImaGroupDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalEntry.setStatus("current")


class _AdGenImaGroupDayIntervalNumber_Type(Integer32):
    """Custom type adGenImaGroupDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenImaGroupDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenImaGroupDayIntervalNumber_Object = MibTableColumn
adGenImaGroupDayIntervalNumber = _AdGenImaGroupDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1, 1),
    _AdGenImaGroupDayIntervalNumber_Type()
)
adGenImaGroupDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalNumber.setStatus("current")
_AdGenImaGroupDayIntervalUnavailSecs_Type = Gauge32
_AdGenImaGroupDayIntervalUnavailSecs_Object = MibTableColumn
adGenImaGroupDayIntervalUnavailSecs = _AdGenImaGroupDayIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1, 2),
    _AdGenImaGroupDayIntervalUnavailSecs_Type()
)
adGenImaGroupDayIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalUnavailSecs.setStatus("current")
_AdGenImaGroupDayIntervalNeNumFailures_Type = Gauge32
_AdGenImaGroupDayIntervalNeNumFailures_Object = MibTableColumn
adGenImaGroupDayIntervalNeNumFailures = _AdGenImaGroupDayIntervalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1, 3),
    _AdGenImaGroupDayIntervalNeNumFailures_Type()
)
adGenImaGroupDayIntervalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalNeNumFailures.setStatus("current")
_AdGenImaGroupDayIntervalFeNumFailures_Type = Gauge32
_AdGenImaGroupDayIntervalFeNumFailures_Object = MibTableColumn
adGenImaGroupDayIntervalFeNumFailures = _AdGenImaGroupDayIntervalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1, 4),
    _AdGenImaGroupDayIntervalFeNumFailures_Type()
)
adGenImaGroupDayIntervalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalFeNumFailures.setStatus("current")
_AdGenImaGroupDayIntervalTimeStamp_Type = DisplayString
_AdGenImaGroupDayIntervalTimeStamp_Object = MibTableColumn
adGenImaGroupDayIntervalTimeStamp = _AdGenImaGroupDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 7, 1, 5),
    _AdGenImaGroupDayIntervalTimeStamp_Type()
)
adGenImaGroupDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaGroupDayIntervalTimeStamp.setStatus("current")
_AdGenImaLinkCurrentTable_Object = MibTable
adGenImaLinkCurrentTable = _AdGenImaLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8)
)
if mibBuilder.loadTexts:
    adGenImaLinkCurrentTable.setStatus("current")
_AdGenImaLinkCurrentEntry_Object = MibTableRow
adGenImaLinkCurrentEntry = _AdGenImaLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1)
)
adGenImaLinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkCurrentEntry.setStatus("current")
_AdGenImaLinkCurrentImaViolations_Type = Gauge32
_AdGenImaLinkCurrentImaViolations_Object = MibTableColumn
adGenImaLinkCurrentImaViolations = _AdGenImaLinkCurrentImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 1),
    _AdGenImaLinkCurrentImaViolations_Type()
)
adGenImaLinkCurrentImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentImaViolations.setStatus("current")
_AdGenImaLinkCurrentOifAnomalies_Type = Gauge32
_AdGenImaLinkCurrentOifAnomalies_Object = MibTableColumn
adGenImaLinkCurrentOifAnomalies = _AdGenImaLinkCurrentOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 2),
    _AdGenImaLinkCurrentOifAnomalies_Type()
)
adGenImaLinkCurrentOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentOifAnomalies.setStatus("current")
_AdGenImaLinkCurrentNeSevErroredSecs_Type = Gauge32
_AdGenImaLinkCurrentNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkCurrentNeSevErroredSecs = _AdGenImaLinkCurrentNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 3),
    _AdGenImaLinkCurrentNeSevErroredSecs_Type()
)
adGenImaLinkCurrentNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeSevErroredSecs.setStatus("current")
_AdGenImaLinkCurrentFeSevErroredSecs_Type = Gauge32
_AdGenImaLinkCurrentFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkCurrentFeSevErroredSecs = _AdGenImaLinkCurrentFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 4),
    _AdGenImaLinkCurrentFeSevErroredSecs_Type()
)
adGenImaLinkCurrentFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeSevErroredSecs.setStatus("current")
_AdGenImaLinkCurrentNeUnavailSecs_Type = Gauge32
_AdGenImaLinkCurrentNeUnavailSecs_Object = MibTableColumn
adGenImaLinkCurrentNeUnavailSecs = _AdGenImaLinkCurrentNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 5),
    _AdGenImaLinkCurrentNeUnavailSecs_Type()
)
adGenImaLinkCurrentNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeUnavailSecs.setStatus("current")
_AdGenImaLinkCurrentFeUnavailSecs_Type = Gauge32
_AdGenImaLinkCurrentFeUnavailSecs_Object = MibTableColumn
adGenImaLinkCurrentFeUnavailSecs = _AdGenImaLinkCurrentFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 6),
    _AdGenImaLinkCurrentFeUnavailSecs_Type()
)
adGenImaLinkCurrentFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeUnavailSecs.setStatus("current")
_AdGenImaLinkCurrentNeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkCurrentNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkCurrentNeTxUnusableSecs = _AdGenImaLinkCurrentNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 7),
    _AdGenImaLinkCurrentNeTxUnusableSecs_Type()
)
adGenImaLinkCurrentNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkCurrentNeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkCurrentNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkCurrentNeRxUnusableSecs = _AdGenImaLinkCurrentNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 8),
    _AdGenImaLinkCurrentNeRxUnusableSecs_Type()
)
adGenImaLinkCurrentNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkCurrentFeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkCurrentFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkCurrentFeTxUnusableSecs = _AdGenImaLinkCurrentFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 9),
    _AdGenImaLinkCurrentFeTxUnusableSecs_Type()
)
adGenImaLinkCurrentFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkCurrentFeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkCurrentFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkCurrentFeRxUnusableSecs = _AdGenImaLinkCurrentFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 10),
    _AdGenImaLinkCurrentFeRxUnusableSecs_Type()
)
adGenImaLinkCurrentFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkCurrentNeTxNumFailures_Type = Gauge32
_AdGenImaLinkCurrentNeTxNumFailures_Object = MibTableColumn
adGenImaLinkCurrentNeTxNumFailures = _AdGenImaLinkCurrentNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 11),
    _AdGenImaLinkCurrentNeTxNumFailures_Type()
)
adGenImaLinkCurrentNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeTxNumFailures.setStatus("current")
_AdGenImaLinkCurrentNeRxNumFailures_Type = Gauge32
_AdGenImaLinkCurrentNeRxNumFailures_Object = MibTableColumn
adGenImaLinkCurrentNeRxNumFailures = _AdGenImaLinkCurrentNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 12),
    _AdGenImaLinkCurrentNeRxNumFailures_Type()
)
adGenImaLinkCurrentNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentNeRxNumFailures.setStatus("current")
_AdGenImaLinkCurrentFeTxNumFailures_Type = Gauge32
_AdGenImaLinkCurrentFeTxNumFailures_Object = MibTableColumn
adGenImaLinkCurrentFeTxNumFailures = _AdGenImaLinkCurrentFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 13),
    _AdGenImaLinkCurrentFeTxNumFailures_Type()
)
adGenImaLinkCurrentFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeTxNumFailures.setStatus("current")
_AdGenImaLinkCurrentFeRxNumFailures_Type = Gauge32
_AdGenImaLinkCurrentFeRxNumFailures_Object = MibTableColumn
adGenImaLinkCurrentFeRxNumFailures = _AdGenImaLinkCurrentFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 14),
    _AdGenImaLinkCurrentFeRxNumFailures_Type()
)
adGenImaLinkCurrentFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentFeRxNumFailures.setStatus("current")
_AdGenImaLinkCurrentTxStuffs_Type = Gauge32
_AdGenImaLinkCurrentTxStuffs_Object = MibTableColumn
adGenImaLinkCurrentTxStuffs = _AdGenImaLinkCurrentTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 15),
    _AdGenImaLinkCurrentTxStuffs_Type()
)
adGenImaLinkCurrentTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentTxStuffs.setStatus("current")
_AdGenImaLinkCurrentRxStuffs_Type = Gauge32
_AdGenImaLinkCurrentRxStuffs_Object = MibTableColumn
adGenImaLinkCurrentRxStuffs = _AdGenImaLinkCurrentRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 8, 1, 16),
    _AdGenImaLinkCurrentRxStuffs_Type()
)
adGenImaLinkCurrentRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkCurrentRxStuffs.setStatus("current")
_AdGenImaLinkIntervalTable_Object = MibTable
adGenImaLinkIntervalTable = _AdGenImaLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9)
)
if mibBuilder.loadTexts:
    adGenImaLinkIntervalTable.setStatus("current")
_AdGenImaLinkIntervalEntry_Object = MibTableRow
adGenImaLinkIntervalEntry = _AdGenImaLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1)
)
adGenImaLinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-IMA-MIB", "adGenImaLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenImaLinkIntervalEntry.setStatus("current")


class _AdGenImaLinkIntervalNumber_Type(Integer32):
    """Custom type adGenImaLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenImaLinkIntervalNumber_Type.__name__ = "Integer32"
_AdGenImaLinkIntervalNumber_Object = MibTableColumn
adGenImaLinkIntervalNumber = _AdGenImaLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 1),
    _AdGenImaLinkIntervalNumber_Type()
)
adGenImaLinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNumber.setStatus("current")
_AdGenImaLinkIntervalImaViolations_Type = Gauge32
_AdGenImaLinkIntervalImaViolations_Object = MibTableColumn
adGenImaLinkIntervalImaViolations = _AdGenImaLinkIntervalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 2),
    _AdGenImaLinkIntervalImaViolations_Type()
)
adGenImaLinkIntervalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalImaViolations.setStatus("current")
_AdGenImaLinkIntervalOifAnomalies_Type = Gauge32
_AdGenImaLinkIntervalOifAnomalies_Object = MibTableColumn
adGenImaLinkIntervalOifAnomalies = _AdGenImaLinkIntervalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 3),
    _AdGenImaLinkIntervalOifAnomalies_Type()
)
adGenImaLinkIntervalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalOifAnomalies.setStatus("current")
_AdGenImaLinkIntervalNeSevErroredSecs_Type = Gauge32
_AdGenImaLinkIntervalNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkIntervalNeSevErroredSecs = _AdGenImaLinkIntervalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 4),
    _AdGenImaLinkIntervalNeSevErroredSecs_Type()
)
adGenImaLinkIntervalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeSevErroredSecs.setStatus("current")
_AdGenImaLinkIntervalFeSevErroredSecs_Type = Gauge32
_AdGenImaLinkIntervalFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkIntervalFeSevErroredSecs = _AdGenImaLinkIntervalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 5),
    _AdGenImaLinkIntervalFeSevErroredSecs_Type()
)
adGenImaLinkIntervalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeSevErroredSecs.setStatus("current")
_AdGenImaLinkIntervalNeUnavailSecs_Type = Gauge32
_AdGenImaLinkIntervalNeUnavailSecs_Object = MibTableColumn
adGenImaLinkIntervalNeUnavailSecs = _AdGenImaLinkIntervalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 6),
    _AdGenImaLinkIntervalNeUnavailSecs_Type()
)
adGenImaLinkIntervalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeUnavailSecs.setStatus("current")
_AdGenImaLinkIntervalFeUnavailSecs_Type = Gauge32
_AdGenImaLinkIntervalFeUnavailSecs_Object = MibTableColumn
adGenImaLinkIntervalFeUnavailSecs = _AdGenImaLinkIntervalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 7),
    _AdGenImaLinkIntervalFeUnavailSecs_Type()
)
adGenImaLinkIntervalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeUnavailSecs.setStatus("current")
_AdGenImaLinkIntervalNeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkIntervalNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkIntervalNeTxUnusableSecs = _AdGenImaLinkIntervalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 8),
    _AdGenImaLinkIntervalNeTxUnusableSecs_Type()
)
adGenImaLinkIntervalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkIntervalNeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkIntervalNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkIntervalNeRxUnusableSecs = _AdGenImaLinkIntervalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 9),
    _AdGenImaLinkIntervalNeRxUnusableSecs_Type()
)
adGenImaLinkIntervalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkIntervalFeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkIntervalFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkIntervalFeTxUnusableSecs = _AdGenImaLinkIntervalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 10),
    _AdGenImaLinkIntervalFeTxUnusableSecs_Type()
)
adGenImaLinkIntervalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkIntervalFeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkIntervalFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkIntervalFeRxUnusableSecs = _AdGenImaLinkIntervalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 11),
    _AdGenImaLinkIntervalFeRxUnusableSecs_Type()
)
adGenImaLinkIntervalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkIntervalNeTxNumFailures_Type = Gauge32
_AdGenImaLinkIntervalNeTxNumFailures_Object = MibTableColumn
adGenImaLinkIntervalNeTxNumFailures = _AdGenImaLinkIntervalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 12),
    _AdGenImaLinkIntervalNeTxNumFailures_Type()
)
adGenImaLinkIntervalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeTxNumFailures.setStatus("current")
_AdGenImaLinkIntervalNeRxNumFailures_Type = Gauge32
_AdGenImaLinkIntervalNeRxNumFailures_Object = MibTableColumn
adGenImaLinkIntervalNeRxNumFailures = _AdGenImaLinkIntervalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 13),
    _AdGenImaLinkIntervalNeRxNumFailures_Type()
)
adGenImaLinkIntervalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalNeRxNumFailures.setStatus("current")
_AdGenImaLinkIntervalFeTxNumFailures_Type = Gauge32
_AdGenImaLinkIntervalFeTxNumFailures_Object = MibTableColumn
adGenImaLinkIntervalFeTxNumFailures = _AdGenImaLinkIntervalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 14),
    _AdGenImaLinkIntervalFeTxNumFailures_Type()
)
adGenImaLinkIntervalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeTxNumFailures.setStatus("current")
_AdGenImaLinkIntervalFeRxNumFailures_Type = Gauge32
_AdGenImaLinkIntervalFeRxNumFailures_Object = MibTableColumn
adGenImaLinkIntervalFeRxNumFailures = _AdGenImaLinkIntervalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 15),
    _AdGenImaLinkIntervalFeRxNumFailures_Type()
)
adGenImaLinkIntervalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalFeRxNumFailures.setStatus("current")
_AdGenImaLinkIntervalTxStuffs_Type = Gauge32
_AdGenImaLinkIntervalTxStuffs_Object = MibTableColumn
adGenImaLinkIntervalTxStuffs = _AdGenImaLinkIntervalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 16),
    _AdGenImaLinkIntervalTxStuffs_Type()
)
adGenImaLinkIntervalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalTxStuffs.setStatus("current")
_AdGenImaLinkIntervalRxStuffs_Type = Gauge32
_AdGenImaLinkIntervalRxStuffs_Object = MibTableColumn
adGenImaLinkIntervalRxStuffs = _AdGenImaLinkIntervalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 17),
    _AdGenImaLinkIntervalRxStuffs_Type()
)
adGenImaLinkIntervalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalRxStuffs.setStatus("current")
_AdGenImaLinkIntervalTimeStamp_Type = DisplayString
_AdGenImaLinkIntervalTimeStamp_Object = MibTableColumn
adGenImaLinkIntervalTimeStamp = _AdGenImaLinkIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 9, 1, 18),
    _AdGenImaLinkIntervalTimeStamp_Type()
)
adGenImaLinkIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkIntervalTimeStamp.setStatus("current")
_AdGenImaLinkTotalTable_Object = MibTable
adGenImaLinkTotalTable = _AdGenImaLinkTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10)
)
if mibBuilder.loadTexts:
    adGenImaLinkTotalTable.setStatus("current")
_AdGenImaLinkTotalEntry_Object = MibTableRow
adGenImaLinkTotalEntry = _AdGenImaLinkTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1)
)
adGenImaLinkTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkTotalEntry.setStatus("current")
_AdGenImaLinkTotalImaViolations_Type = Gauge32
_AdGenImaLinkTotalImaViolations_Object = MibTableColumn
adGenImaLinkTotalImaViolations = _AdGenImaLinkTotalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 1),
    _AdGenImaLinkTotalImaViolations_Type()
)
adGenImaLinkTotalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalImaViolations.setStatus("current")
_AdGenImaLinkTotalOifAnomalies_Type = Gauge32
_AdGenImaLinkTotalOifAnomalies_Object = MibTableColumn
adGenImaLinkTotalOifAnomalies = _AdGenImaLinkTotalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 2),
    _AdGenImaLinkTotalOifAnomalies_Type()
)
adGenImaLinkTotalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalOifAnomalies.setStatus("current")
_AdGenImaLinkTotalNeSevErroredSecs_Type = Gauge32
_AdGenImaLinkTotalNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkTotalNeSevErroredSecs = _AdGenImaLinkTotalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 3),
    _AdGenImaLinkTotalNeSevErroredSecs_Type()
)
adGenImaLinkTotalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeSevErroredSecs.setStatus("current")
_AdGenImaLinkTotalFeSevErroredSecs_Type = Gauge32
_AdGenImaLinkTotalFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkTotalFeSevErroredSecs = _AdGenImaLinkTotalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 4),
    _AdGenImaLinkTotalFeSevErroredSecs_Type()
)
adGenImaLinkTotalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeSevErroredSecs.setStatus("current")
_AdGenImaLinkTotalNeUnavailSecs_Type = Gauge32
_AdGenImaLinkTotalNeUnavailSecs_Object = MibTableColumn
adGenImaLinkTotalNeUnavailSecs = _AdGenImaLinkTotalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 5),
    _AdGenImaLinkTotalNeUnavailSecs_Type()
)
adGenImaLinkTotalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeUnavailSecs.setStatus("current")
_AdGenImaLinkTotalFeUnavailSecs_Type = Gauge32
_AdGenImaLinkTotalFeUnavailSecs_Object = MibTableColumn
adGenImaLinkTotalFeUnavailSecs = _AdGenImaLinkTotalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 6),
    _AdGenImaLinkTotalFeUnavailSecs_Type()
)
adGenImaLinkTotalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeUnavailSecs.setStatus("current")
_AdGenImaLinkTotalNeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkTotalNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkTotalNeTxUnusableSecs = _AdGenImaLinkTotalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 7),
    _AdGenImaLinkTotalNeTxUnusableSecs_Type()
)
adGenImaLinkTotalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkTotalNeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkTotalNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkTotalNeRxUnusableSecs = _AdGenImaLinkTotalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 8),
    _AdGenImaLinkTotalNeRxUnusableSecs_Type()
)
adGenImaLinkTotalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkTotalFeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkTotalFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkTotalFeTxUnusableSecs = _AdGenImaLinkTotalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 9),
    _AdGenImaLinkTotalFeTxUnusableSecs_Type()
)
adGenImaLinkTotalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkTotalFeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkTotalFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkTotalFeRxUnusableSecs = _AdGenImaLinkTotalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 10),
    _AdGenImaLinkTotalFeRxUnusableSecs_Type()
)
adGenImaLinkTotalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkTotalNeTxNumFailures_Type = Gauge32
_AdGenImaLinkTotalNeTxNumFailures_Object = MibTableColumn
adGenImaLinkTotalNeTxNumFailures = _AdGenImaLinkTotalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 11),
    _AdGenImaLinkTotalNeTxNumFailures_Type()
)
adGenImaLinkTotalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeTxNumFailures.setStatus("current")
_AdGenImaLinkTotalNeRxNumFailures_Type = Gauge32
_AdGenImaLinkTotalNeRxNumFailures_Object = MibTableColumn
adGenImaLinkTotalNeRxNumFailures = _AdGenImaLinkTotalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 12),
    _AdGenImaLinkTotalNeRxNumFailures_Type()
)
adGenImaLinkTotalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalNeRxNumFailures.setStatus("current")
_AdGenImaLinkTotalFeTxNumFailures_Type = Gauge32
_AdGenImaLinkTotalFeTxNumFailures_Object = MibTableColumn
adGenImaLinkTotalFeTxNumFailures = _AdGenImaLinkTotalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 13),
    _AdGenImaLinkTotalFeTxNumFailures_Type()
)
adGenImaLinkTotalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeTxNumFailures.setStatus("current")
_AdGenImaLinkTotalFeRxNumFailures_Type = Gauge32
_AdGenImaLinkTotalFeRxNumFailures_Object = MibTableColumn
adGenImaLinkTotalFeRxNumFailures = _AdGenImaLinkTotalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 14),
    _AdGenImaLinkTotalFeRxNumFailures_Type()
)
adGenImaLinkTotalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalFeRxNumFailures.setStatus("current")
_AdGenImaLinkTotalTxStuffs_Type = Gauge32
_AdGenImaLinkTotalTxStuffs_Object = MibTableColumn
adGenImaLinkTotalTxStuffs = _AdGenImaLinkTotalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 15),
    _AdGenImaLinkTotalTxStuffs_Type()
)
adGenImaLinkTotalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalTxStuffs.setStatus("current")
_AdGenImaLinkTotalRxStuffs_Type = Gauge32
_AdGenImaLinkTotalRxStuffs_Object = MibTableColumn
adGenImaLinkTotalRxStuffs = _AdGenImaLinkTotalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 10, 1, 16),
    _AdGenImaLinkTotalRxStuffs_Type()
)
adGenImaLinkTotalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkTotalRxStuffs.setStatus("current")
_AdGenImaLinkDayCurrentTable_Object = MibTable
adGenImaLinkDayCurrentTable = _AdGenImaLinkDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11)
)
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentTable.setStatus("current")
_AdGenImaLinkDayCurrentEntry_Object = MibTableRow
adGenImaLinkDayCurrentEntry = _AdGenImaLinkDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1)
)
adGenImaLinkDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentEntry.setStatus("current")
_AdGenImaLinkDayCurrentImaViolations_Type = Gauge32
_AdGenImaLinkDayCurrentImaViolations_Object = MibTableColumn
adGenImaLinkDayCurrentImaViolations = _AdGenImaLinkDayCurrentImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 1),
    _AdGenImaLinkDayCurrentImaViolations_Type()
)
adGenImaLinkDayCurrentImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentImaViolations.setStatus("current")
_AdGenImaLinkDayCurrentOifAnomalies_Type = Gauge32
_AdGenImaLinkDayCurrentOifAnomalies_Object = MibTableColumn
adGenImaLinkDayCurrentOifAnomalies = _AdGenImaLinkDayCurrentOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 2),
    _AdGenImaLinkDayCurrentOifAnomalies_Type()
)
adGenImaLinkDayCurrentOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentOifAnomalies.setStatus("current")
_AdGenImaLinkDayCurrentNeSevErroredSecs_Type = Gauge32
_AdGenImaLinkDayCurrentNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkDayCurrentNeSevErroredSecs = _AdGenImaLinkDayCurrentNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 3),
    _AdGenImaLinkDayCurrentNeSevErroredSecs_Type()
)
adGenImaLinkDayCurrentNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeSevErroredSecs.setStatus("current")
_AdGenImaLinkDayCurrentFeSevErroredSecs_Type = Gauge32
_AdGenImaLinkDayCurrentFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkDayCurrentFeSevErroredSecs = _AdGenImaLinkDayCurrentFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 4),
    _AdGenImaLinkDayCurrentFeSevErroredSecs_Type()
)
adGenImaLinkDayCurrentFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeSevErroredSecs.setStatus("current")
_AdGenImaLinkDayCurrentNeUnavailSecs_Type = Gauge32
_AdGenImaLinkDayCurrentNeUnavailSecs_Object = MibTableColumn
adGenImaLinkDayCurrentNeUnavailSecs = _AdGenImaLinkDayCurrentNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 5),
    _AdGenImaLinkDayCurrentNeUnavailSecs_Type()
)
adGenImaLinkDayCurrentNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeUnavailSecs.setStatus("current")
_AdGenImaLinkDayCurrentFeUnavailSecs_Type = Gauge32
_AdGenImaLinkDayCurrentFeUnavailSecs_Object = MibTableColumn
adGenImaLinkDayCurrentFeUnavailSecs = _AdGenImaLinkDayCurrentFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 6),
    _AdGenImaLinkDayCurrentFeUnavailSecs_Type()
)
adGenImaLinkDayCurrentFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeUnavailSecs.setStatus("current")
_AdGenImaLinkDayCurrentNeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayCurrentNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayCurrentNeTxUnusableSecs = _AdGenImaLinkDayCurrentNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 7),
    _AdGenImaLinkDayCurrentNeTxUnusableSecs_Type()
)
adGenImaLinkDayCurrentNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkDayCurrentNeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayCurrentNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayCurrentNeRxUnusableSecs = _AdGenImaLinkDayCurrentNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 8),
    _AdGenImaLinkDayCurrentNeRxUnusableSecs_Type()
)
adGenImaLinkDayCurrentNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkDayCurrentFeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayCurrentFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayCurrentFeTxUnusableSecs = _AdGenImaLinkDayCurrentFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 9),
    _AdGenImaLinkDayCurrentFeTxUnusableSecs_Type()
)
adGenImaLinkDayCurrentFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkDayCurrentFeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayCurrentFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayCurrentFeRxUnusableSecs = _AdGenImaLinkDayCurrentFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 10),
    _AdGenImaLinkDayCurrentFeRxUnusableSecs_Type()
)
adGenImaLinkDayCurrentFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkDayCurrentNeTxNumFailures_Type = Gauge32
_AdGenImaLinkDayCurrentNeTxNumFailures_Object = MibTableColumn
adGenImaLinkDayCurrentNeTxNumFailures = _AdGenImaLinkDayCurrentNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 11),
    _AdGenImaLinkDayCurrentNeTxNumFailures_Type()
)
adGenImaLinkDayCurrentNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeTxNumFailures.setStatus("current")
_AdGenImaLinkDayCurrentNeRxNumFailures_Type = Gauge32
_AdGenImaLinkDayCurrentNeRxNumFailures_Object = MibTableColumn
adGenImaLinkDayCurrentNeRxNumFailures = _AdGenImaLinkDayCurrentNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 12),
    _AdGenImaLinkDayCurrentNeRxNumFailures_Type()
)
adGenImaLinkDayCurrentNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentNeRxNumFailures.setStatus("current")
_AdGenImaLinkDayCurrentFeTxNumFailures_Type = Gauge32
_AdGenImaLinkDayCurrentFeTxNumFailures_Object = MibTableColumn
adGenImaLinkDayCurrentFeTxNumFailures = _AdGenImaLinkDayCurrentFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 13),
    _AdGenImaLinkDayCurrentFeTxNumFailures_Type()
)
adGenImaLinkDayCurrentFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeTxNumFailures.setStatus("current")
_AdGenImaLinkDayCurrentFeRxNumFailures_Type = Gauge32
_AdGenImaLinkDayCurrentFeRxNumFailures_Object = MibTableColumn
adGenImaLinkDayCurrentFeRxNumFailures = _AdGenImaLinkDayCurrentFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 14),
    _AdGenImaLinkDayCurrentFeRxNumFailures_Type()
)
adGenImaLinkDayCurrentFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentFeRxNumFailures.setStatus("current")
_AdGenImaLinkDayCurrentTxStuffs_Type = Gauge32
_AdGenImaLinkDayCurrentTxStuffs_Object = MibTableColumn
adGenImaLinkDayCurrentTxStuffs = _AdGenImaLinkDayCurrentTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 15),
    _AdGenImaLinkDayCurrentTxStuffs_Type()
)
adGenImaLinkDayCurrentTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentTxStuffs.setStatus("current")
_AdGenImaLinkDayCurrentRxStuffs_Type = Gauge32
_AdGenImaLinkDayCurrentRxStuffs_Object = MibTableColumn
adGenImaLinkDayCurrentRxStuffs = _AdGenImaLinkDayCurrentRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 11, 1, 16),
    _AdGenImaLinkDayCurrentRxStuffs_Type()
)
adGenImaLinkDayCurrentRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayCurrentRxStuffs.setStatus("current")
_AdGenImaLinkDayIntervalTable_Object = MibTable
adGenImaLinkDayIntervalTable = _AdGenImaLinkDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12)
)
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalTable.setStatus("current")
_AdGenImaLinkDayIntervalEntry_Object = MibTableRow
adGenImaLinkDayIntervalEntry = _AdGenImaLinkDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1)
)
adGenImaLinkDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-IMA-MIB", "adGenImaLinkDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalEntry.setStatus("current")


class _AdGenImaLinkDayIntervalNumber_Type(Integer32):
    """Custom type adGenImaLinkDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenImaLinkDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenImaLinkDayIntervalNumber_Object = MibTableColumn
adGenImaLinkDayIntervalNumber = _AdGenImaLinkDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 1),
    _AdGenImaLinkDayIntervalNumber_Type()
)
adGenImaLinkDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNumber.setStatus("current")
_AdGenImaLinkDayIntervalImaViolations_Type = Gauge32
_AdGenImaLinkDayIntervalImaViolations_Object = MibTableColumn
adGenImaLinkDayIntervalImaViolations = _AdGenImaLinkDayIntervalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 2),
    _AdGenImaLinkDayIntervalImaViolations_Type()
)
adGenImaLinkDayIntervalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalImaViolations.setStatus("current")
_AdGenImaLinkDayIntervalOifAnomalies_Type = Gauge32
_AdGenImaLinkDayIntervalOifAnomalies_Object = MibTableColumn
adGenImaLinkDayIntervalOifAnomalies = _AdGenImaLinkDayIntervalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 3),
    _AdGenImaLinkDayIntervalOifAnomalies_Type()
)
adGenImaLinkDayIntervalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalOifAnomalies.setStatus("current")
_AdGenImaLinkDayIntervalNeSevErroredSecs_Type = Gauge32
_AdGenImaLinkDayIntervalNeSevErroredSecs_Object = MibTableColumn
adGenImaLinkDayIntervalNeSevErroredSecs = _AdGenImaLinkDayIntervalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 4),
    _AdGenImaLinkDayIntervalNeSevErroredSecs_Type()
)
adGenImaLinkDayIntervalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeSevErroredSecs.setStatus("current")
_AdGenImaLinkDayIntervalFeSevErroredSecs_Type = Gauge32
_AdGenImaLinkDayIntervalFeSevErroredSecs_Object = MibTableColumn
adGenImaLinkDayIntervalFeSevErroredSecs = _AdGenImaLinkDayIntervalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 5),
    _AdGenImaLinkDayIntervalFeSevErroredSecs_Type()
)
adGenImaLinkDayIntervalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeSevErroredSecs.setStatus("current")
_AdGenImaLinkDayIntervalNeUnavailSecs_Type = Gauge32
_AdGenImaLinkDayIntervalNeUnavailSecs_Object = MibTableColumn
adGenImaLinkDayIntervalNeUnavailSecs = _AdGenImaLinkDayIntervalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 6),
    _AdGenImaLinkDayIntervalNeUnavailSecs_Type()
)
adGenImaLinkDayIntervalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeUnavailSecs.setStatus("current")
_AdGenImaLinkDayIntervalFeUnavailSecs_Type = Gauge32
_AdGenImaLinkDayIntervalFeUnavailSecs_Object = MibTableColumn
adGenImaLinkDayIntervalFeUnavailSecs = _AdGenImaLinkDayIntervalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 7),
    _AdGenImaLinkDayIntervalFeUnavailSecs_Type()
)
adGenImaLinkDayIntervalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeUnavailSecs.setStatus("current")
_AdGenImaLinkDayIntervalNeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayIntervalNeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayIntervalNeTxUnusableSecs = _AdGenImaLinkDayIntervalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 8),
    _AdGenImaLinkDayIntervalNeTxUnusableSecs_Type()
)
adGenImaLinkDayIntervalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeTxUnusableSecs.setStatus("current")
_AdGenImaLinkDayIntervalNeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayIntervalNeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayIntervalNeRxUnusableSecs = _AdGenImaLinkDayIntervalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 9),
    _AdGenImaLinkDayIntervalNeRxUnusableSecs_Type()
)
adGenImaLinkDayIntervalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeRxUnusableSecs.setStatus("current")
_AdGenImaLinkDayIntervalFeTxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayIntervalFeTxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayIntervalFeTxUnusableSecs = _AdGenImaLinkDayIntervalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 10),
    _AdGenImaLinkDayIntervalFeTxUnusableSecs_Type()
)
adGenImaLinkDayIntervalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeTxUnusableSecs.setStatus("current")
_AdGenImaLinkDayIntervalFeRxUnusableSecs_Type = Gauge32
_AdGenImaLinkDayIntervalFeRxUnusableSecs_Object = MibTableColumn
adGenImaLinkDayIntervalFeRxUnusableSecs = _AdGenImaLinkDayIntervalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 11),
    _AdGenImaLinkDayIntervalFeRxUnusableSecs_Type()
)
adGenImaLinkDayIntervalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeRxUnusableSecs.setStatus("current")
_AdGenImaLinkDayIntervalNeTxNumFailures_Type = Gauge32
_AdGenImaLinkDayIntervalNeTxNumFailures_Object = MibTableColumn
adGenImaLinkDayIntervalNeTxNumFailures = _AdGenImaLinkDayIntervalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 12),
    _AdGenImaLinkDayIntervalNeTxNumFailures_Type()
)
adGenImaLinkDayIntervalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeTxNumFailures.setStatus("current")
_AdGenImaLinkDayIntervalNeRxNumFailures_Type = Gauge32
_AdGenImaLinkDayIntervalNeRxNumFailures_Object = MibTableColumn
adGenImaLinkDayIntervalNeRxNumFailures = _AdGenImaLinkDayIntervalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 13),
    _AdGenImaLinkDayIntervalNeRxNumFailures_Type()
)
adGenImaLinkDayIntervalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalNeRxNumFailures.setStatus("current")
_AdGenImaLinkDayIntervalFeTxNumFailures_Type = Gauge32
_AdGenImaLinkDayIntervalFeTxNumFailures_Object = MibTableColumn
adGenImaLinkDayIntervalFeTxNumFailures = _AdGenImaLinkDayIntervalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 14),
    _AdGenImaLinkDayIntervalFeTxNumFailures_Type()
)
adGenImaLinkDayIntervalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeTxNumFailures.setStatus("current")
_AdGenImaLinkDayIntervalFeRxNumFailures_Type = Gauge32
_AdGenImaLinkDayIntervalFeRxNumFailures_Object = MibTableColumn
adGenImaLinkDayIntervalFeRxNumFailures = _AdGenImaLinkDayIntervalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 15),
    _AdGenImaLinkDayIntervalFeRxNumFailures_Type()
)
adGenImaLinkDayIntervalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalFeRxNumFailures.setStatus("current")
_AdGenImaLinkDayIntervalTxStuffs_Type = Gauge32
_AdGenImaLinkDayIntervalTxStuffs_Object = MibTableColumn
adGenImaLinkDayIntervalTxStuffs = _AdGenImaLinkDayIntervalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 16),
    _AdGenImaLinkDayIntervalTxStuffs_Type()
)
adGenImaLinkDayIntervalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalTxStuffs.setStatus("current")
_AdGenImaLinkDayIntervalRxStuffs_Type = Gauge32
_AdGenImaLinkDayIntervalRxStuffs_Object = MibTableColumn
adGenImaLinkDayIntervalRxStuffs = _AdGenImaLinkDayIntervalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 17),
    _AdGenImaLinkDayIntervalRxStuffs_Type()
)
adGenImaLinkDayIntervalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalRxStuffs.setStatus("current")
_AdGenImaLinkDayIntervalTimeStamp_Type = DisplayString
_AdGenImaLinkDayIntervalTimeStamp_Object = MibTableColumn
adGenImaLinkDayIntervalTimeStamp = _AdGenImaLinkDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 4, 12, 1, 18),
    _AdGenImaLinkDayIntervalTimeStamp_Type()
)
adGenImaLinkDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenImaLinkDayIntervalTimeStamp.setStatus("current")
_AdGenImaAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenImaAlarmsPrefix = _AdGenImaAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10)
)
_AdGenImaAlarms_ObjectIdentity = ObjectIdentity
adGenImaAlarms = _AdGenImaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0)
)

# Managed Objects groups


# Notification objects

adGenImaGroupCfgAbortClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 2)
)
adGenImaGroupCfgAbortClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupCfgAbortClr.setStatus(
        "current"
    )

adGenImaGroupCfgAbortAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 3)
)
adGenImaGroupCfgAbortAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupCfgAbortAct.setStatus(
        "current"
    )

adGenImaGroupCfgInsufficentLinksClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 4)
)
adGenImaGroupCfgInsufficentLinksClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupCfgInsufficentLinksClr.setStatus(
        "current"
    )

adGenImaGroupCfgInsufficentLinksAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 5)
)
adGenImaGroupCfgInsufficentLinksAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupCfgInsufficentLinksAct.setStatus(
        "current"
    )

adGenImaGroupFeStartupClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 6)
)
adGenImaGroupFeStartupClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeStartupClr.setStatus(
        "current"
    )

adGenImaGroupFeStartupAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 7)
)
adGenImaGroupFeStartupAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeStartupAct.setStatus(
        "current"
    )

adGenImaGroupFeCfgAbortClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 8)
)
adGenImaGroupFeCfgAbortClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeCfgAbortClr.setStatus(
        "current"
    )

adGenImaGroupFeCfgAbortAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 9)
)
adGenImaGroupFeCfgAbortAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeCfgAbortAct.setStatus(
        "current"
    )

adGenImaGroupFeCfgInsufficentLinksClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 10)
)
adGenImaGroupFeCfgInsufficentLinksClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeCfgInsufficentLinksClr.setStatus(
        "current"
    )

adGenImaGroupFeCfgInsufficentLinksAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 11)
)
adGenImaGroupFeCfgInsufficentLinksAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeCfgInsufficentLinksAct.setStatus(
        "current"
    )

adGenImaGroupFeBlockedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 12)
)
adGenImaGroupFeBlockedClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeBlockedClr.setStatus(
        "current"
    )

adGenImaGroupFeBlockedAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 13)
)
adGenImaGroupFeBlockedAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupFeBlockedAct.setStatus(
        "current"
    )

adGenImaGroupTimingMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 14)
)
adGenImaGroupTimingMismatchClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupTimingMismatchClr.setStatus(
        "current"
    )

adGenImaGroupTimingMismatchAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 15)
)
adGenImaGroupTimingMismatchAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaGroupTimingMismatchAct.setStatus(
        "current"
    )

adGenImaLinkLifClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 16)
)
adGenImaLinkLifClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkLifClr.setStatus(
        "current"
    )

adGenImaLinkLifAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 17)
)
adGenImaLinkLifAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkLifAct.setStatus(
        "current"
    )

adGenImaLinkLodsClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 18)
)
adGenImaLinkLodsClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkLodsClr.setStatus(
        "current"
    )

adGenImaLinkLodsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 19)
)
adGenImaLinkLodsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkLodsAct.setStatus(
        "current"
    )

adGenImaLinkRfiClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 20)
)
adGenImaLinkRfiClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRfiClr.setStatus(
        "current"
    )

adGenImaLinkRfiAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 21)
)
adGenImaLinkRfiAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRfiAct.setStatus(
        "current"
    )

adGenImaLinkTxMisconnectedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 22)
)
adGenImaLinkTxMisconnectedClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkTxMisconnectedClr.setStatus(
        "current"
    )

adGenImaLinkTxMisconnectedAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 23)
)
adGenImaLinkTxMisconnectedAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkTxMisconnectedAct.setStatus(
        "current"
    )

adGenImaLinkRxMisconnectedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 24)
)
adGenImaLinkRxMisconnectedClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRxMisconnectedClr.setStatus(
        "current"
    )

adGenImaLinkRxMisconnectedAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 25)
)
adGenImaLinkRxMisconnectedAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRxMisconnectedAct.setStatus(
        "current"
    )

adGenImaLinkTxFaultClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 26)
)
adGenImaLinkTxFaultClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkTxFaultClr.setStatus(
        "current"
    )

adGenImaLinkTxFaultAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 27)
)
adGenImaLinkTxFaultAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkTxFaultAct.setStatus(
        "current"
    )

adGenImaLinkRxFaultClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 28)
)
adGenImaLinkRxFaultClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRxFaultClr.setStatus(
        "current"
    )

adGenImaLinkRxFaultAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 29)
)
adGenImaLinkRxFaultAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkRxFaultAct.setStatus(
        "current"
    )

adGenImaLinkFeTxUnusableClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 30)
)
adGenImaLinkFeTxUnusableClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkFeTxUnusableClr.setStatus(
        "current"
    )

adGenImaLinkFeTxUnusableAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 31)
)
adGenImaLinkFeTxUnusableAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkFeTxUnusableAct.setStatus(
        "current"
    )

adGenImaLinkFeRxUnusableClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 32)
)
adGenImaLinkFeRxUnusableClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkFeRxUnusableClr.setStatus(
        "current"
    )

adGenImaLinkFeRxUnusableAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 25, 10, 0, 33)
)
adGenImaLinkFeRxUnusableAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenImaLinkFeRxUnusableAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-IMA-MIB",
    **{"adGenImaProvisioning": adGenImaProvisioning,
       "adGenImaGroupProvTable": adGenImaGroupProvTable,
       "adGenImaGroupProvEntry": adGenImaGroupProvEntry,
       "adGenImaGroupVersion": adGenImaGroupVersion,
       "adGenImaGroupSymmetry": adGenImaGroupSymmetry,
       "adGenImaGroupNeTxClkMode": adGenImaGroupNeTxClkMode,
       "adGenImaGroupTxImaId": adGenImaGroupTxImaId,
       "adGenImaGroupTxFrameLength": adGenImaGroupTxFrameLength,
       "adGenImaGroupDiffDelayMax": adGenImaGroupDiffDelayMax,
       "adGenImaGroupAlphaValue": adGenImaGroupAlphaValue,
       "adGenImaGroupBetaValue": adGenImaGroupBetaValue,
       "adGenImaGroupGammaValue": adGenImaGroupGammaValue,
       "adGenImaGroupTxClkSource": adGenImaGroupTxClkSource,
       "adGenImaAtmGroupCommonProvTable": adGenImaAtmGroupCommonProvTable,
       "adGenImaAtmGroupCommonProvEntry": adGenImaAtmGroupCommonProvEntry,
       "adGenImaAtmGroupCommonProvDhcpCircuitIdFormat": adGenImaAtmGroupCommonProvDhcpCircuitIdFormat,
       "adGenImaStatus": adGenImaStatus,
       "adGenImaGroupStatusTable": adGenImaGroupStatusTable,
       "adGenImaGroupStatusEntry": adGenImaGroupStatusEntry,
       "adGenImaGroupNeState": adGenImaGroupNeState,
       "adGenImaGroupFeState": adGenImaGroupFeState,
       "adGenImaGroupFailureStatus": adGenImaGroupFailureStatus,
       "adGenImaGroupLastChange": adGenImaGroupLastChange,
       "adGenImaGroupRunningSecs": adGenImaGroupRunningSecs,
       "adGenImaGroupFeTxClkMode": adGenImaGroupFeTxClkMode,
       "adGenImaGroupTxTimingRefLink": adGenImaGroupTxTimingRefLink,
       "adGenImaGroupRxTimingRefLink": adGenImaGroupRxTimingRefLink,
       "adGenImaGroupRxImaId": adGenImaGroupRxImaId,
       "adGenImaGroupRxFrameLength": adGenImaGroupRxFrameLength,
       "adGenImaGroupLeastDelayLink": adGenImaGroupLeastDelayLink,
       "adGenImaGroupDiffDelayMaxObs": adGenImaGroupDiffDelayMaxObs,
       "adGenImaGroupTxAvailCellRate": adGenImaGroupTxAvailCellRate,
       "adGenImaGroupRxAvailCellRate": adGenImaGroupRxAvailCellRate,
       "adGenImaGroupTxOamLabelValue": adGenImaGroupTxOamLabelValue,
       "adGenImaGroupRxOamLabelValue": adGenImaGroupRxOamLabelValue,
       "adGenImaLinkStatusTable": adGenImaLinkStatusTable,
       "adGenImaLinkStatusEntry": adGenImaLinkStatusEntry,
       "adGenImaLinkNeTxState": adGenImaLinkNeTxState,
       "adGenImaLinkNeRxState": adGenImaLinkNeRxState,
       "adGenImaLinkFeTxState": adGenImaLinkFeTxState,
       "adGenImaLinkFeRxState": adGenImaLinkFeRxState,
       "adGenImaLinkNeRxFailureStatus": adGenImaLinkNeRxFailureStatus,
       "adGenImaLinkFeRxFailureStatus": adGenImaLinkFeRxFailureStatus,
       "adGenImaLinkTxLid": adGenImaLinkTxLid,
       "adGenImaLinkRxLid": adGenImaLinkRxLid,
       "adGenImaLinkRelDelay": adGenImaLinkRelDelay,
       "adGenImaTest": adGenImaTest,
       "adGenImaGroupTestTable": adGenImaGroupTestTable,
       "adGenImaGroupTestEntry": adGenImaGroupTestEntry,
       "adGenImaGroupTestLinkIfIndex": adGenImaGroupTestLinkIfIndex,
       "adGenImaGroupTestPattern": adGenImaGroupTestPattern,
       "adGenImaGroupTestProcStatus": adGenImaGroupTestProcStatus,
       "adGenImaLinkTestTable": adGenImaLinkTestTable,
       "adGenImaLinkTestEntry": adGenImaLinkTestEntry,
       "adGenImaLinkRxTestPattern": adGenImaLinkRxTestPattern,
       "adGenImaLinkTestProcStatus": adGenImaLinkTestProcStatus,
       "adGenImaPerformance": adGenImaPerformance,
       "adGenImaGroupPerfTable": adGenImaGroupPerfTable,
       "adGenImaGroupPerfEntry": adGenImaGroupPerfEntry,
       "adGenImaGroupUnavailSecs": adGenImaGroupUnavailSecs,
       "adGenImaGroupNeNumFailures": adGenImaGroupNeNumFailures,
       "adGenImaGroupFeNumFailures": adGenImaGroupFeNumFailures,
       "adGenImaGroupValidIntervals": adGenImaGroupValidIntervals,
       "adGenImaGroupInvalidIntervals": adGenImaGroupInvalidIntervals,
       "adGenImaGroupTimeElapsed": adGenImaGroupTimeElapsed,
       "adGenImaGroupResetStats": adGenImaGroupResetStats,
       "adGenImaGroupResetPerfHistory": adGenImaGroupResetPerfHistory,
       "adGenImaLinkPerfTable": adGenImaLinkPerfTable,
       "adGenImaLinkPerfEntry": adGenImaLinkPerfEntry,
       "adGenImaLinkImaViolations": adGenImaLinkImaViolations,
       "adGenImaLinkOifAnomalies": adGenImaLinkOifAnomalies,
       "adGenImaLinkNeSevErroredSecs": adGenImaLinkNeSevErroredSecs,
       "adGenImaLinkFeSevErroredSecs": adGenImaLinkFeSevErroredSecs,
       "adGenImaLinkNeUnavailSecs": adGenImaLinkNeUnavailSecs,
       "adGenImaLinkFeUnavailSecs": adGenImaLinkFeUnavailSecs,
       "adGenImaLinkNeTxUnusableSecs": adGenImaLinkNeTxUnusableSecs,
       "adGenImaLinkNeRxUnusableSecs": adGenImaLinkNeRxUnusableSecs,
       "adGenImaLinkFeTxUnusableSecs": adGenImaLinkFeTxUnusableSecs,
       "adGenImaLinkFeRxUnusableSecs": adGenImaLinkFeRxUnusableSecs,
       "adGenImaLinkNeTxNumFailures": adGenImaLinkNeTxNumFailures,
       "adGenImaLinkNeRxNumFailures": adGenImaLinkNeRxNumFailures,
       "adGenImaLinkFeTxNumFailures": adGenImaLinkFeTxNumFailures,
       "adGenImaLinkFeRxNumFailures": adGenImaLinkFeRxNumFailures,
       "adGenImaLinkTxStuffs": adGenImaLinkTxStuffs,
       "adGenImaLinkRxStuffs": adGenImaLinkRxStuffs,
       "adGenImaLinkValidIntervals": adGenImaLinkValidIntervals,
       "adGenImaLinkInvalidIntervals": adGenImaLinkInvalidIntervals,
       "adGenImaLinkTimeElapsed": adGenImaLinkTimeElapsed,
       "adGenImaLinkResetStats": adGenImaLinkResetStats,
       "adGenImaLinkResetPerfHistory": adGenImaLinkResetPerfHistory,
       "adGenImaGroupCurrentTable": adGenImaGroupCurrentTable,
       "adGenImaGroupCurrentEntry": adGenImaGroupCurrentEntry,
       "adGenImaGroupCurrentUnavailSecs": adGenImaGroupCurrentUnavailSecs,
       "adGenImaGroupCurrentNeNumFailures": adGenImaGroupCurrentNeNumFailures,
       "adGenImaGroupCurrentFeNumFailures": adGenImaGroupCurrentFeNumFailures,
       "adGenImaGroupIntervalTable": adGenImaGroupIntervalTable,
       "adGenImaGroupIntervalEntry": adGenImaGroupIntervalEntry,
       "adGenImaGroupIntervalNumber": adGenImaGroupIntervalNumber,
       "adGenImaGroupIntervalUnavailSecs": adGenImaGroupIntervalUnavailSecs,
       "adGenImaGroupIntervalNeNumFailures": adGenImaGroupIntervalNeNumFailures,
       "adGenImaGroupIntervalFeNumFailures": adGenImaGroupIntervalFeNumFailures,
       "adGenImaGroupIntervalTimeStamp": adGenImaGroupIntervalTimeStamp,
       "adGenImaGroupTotalTable": adGenImaGroupTotalTable,
       "adGenImaGroupTotalEntry": adGenImaGroupTotalEntry,
       "adGenImaGroupTotalUnavailSecs": adGenImaGroupTotalUnavailSecs,
       "adGenImaGroupTotalNeNumFailures": adGenImaGroupTotalNeNumFailures,
       "adGenImaGroupTotalFeNumFailures": adGenImaGroupTotalFeNumFailures,
       "adGenImaGroupDayCurrentTable": adGenImaGroupDayCurrentTable,
       "adGenImaGroupDayCurrentEntry": adGenImaGroupDayCurrentEntry,
       "adGenImaGroupDayCurrentUnavailSecs": adGenImaGroupDayCurrentUnavailSecs,
       "adGenImaGroupDayCurrentNeNumFailures": adGenImaGroupDayCurrentNeNumFailures,
       "adGenImaGroupDayCurrentFeNumFailures": adGenImaGroupDayCurrentFeNumFailures,
       "adGenImaGroupDayIntervalTable": adGenImaGroupDayIntervalTable,
       "adGenImaGroupDayIntervalEntry": adGenImaGroupDayIntervalEntry,
       "adGenImaGroupDayIntervalNumber": adGenImaGroupDayIntervalNumber,
       "adGenImaGroupDayIntervalUnavailSecs": adGenImaGroupDayIntervalUnavailSecs,
       "adGenImaGroupDayIntervalNeNumFailures": adGenImaGroupDayIntervalNeNumFailures,
       "adGenImaGroupDayIntervalFeNumFailures": adGenImaGroupDayIntervalFeNumFailures,
       "adGenImaGroupDayIntervalTimeStamp": adGenImaGroupDayIntervalTimeStamp,
       "adGenImaLinkCurrentTable": adGenImaLinkCurrentTable,
       "adGenImaLinkCurrentEntry": adGenImaLinkCurrentEntry,
       "adGenImaLinkCurrentImaViolations": adGenImaLinkCurrentImaViolations,
       "adGenImaLinkCurrentOifAnomalies": adGenImaLinkCurrentOifAnomalies,
       "adGenImaLinkCurrentNeSevErroredSecs": adGenImaLinkCurrentNeSevErroredSecs,
       "adGenImaLinkCurrentFeSevErroredSecs": adGenImaLinkCurrentFeSevErroredSecs,
       "adGenImaLinkCurrentNeUnavailSecs": adGenImaLinkCurrentNeUnavailSecs,
       "adGenImaLinkCurrentFeUnavailSecs": adGenImaLinkCurrentFeUnavailSecs,
       "adGenImaLinkCurrentNeTxUnusableSecs": adGenImaLinkCurrentNeTxUnusableSecs,
       "adGenImaLinkCurrentNeRxUnusableSecs": adGenImaLinkCurrentNeRxUnusableSecs,
       "adGenImaLinkCurrentFeTxUnusableSecs": adGenImaLinkCurrentFeTxUnusableSecs,
       "adGenImaLinkCurrentFeRxUnusableSecs": adGenImaLinkCurrentFeRxUnusableSecs,
       "adGenImaLinkCurrentNeTxNumFailures": adGenImaLinkCurrentNeTxNumFailures,
       "adGenImaLinkCurrentNeRxNumFailures": adGenImaLinkCurrentNeRxNumFailures,
       "adGenImaLinkCurrentFeTxNumFailures": adGenImaLinkCurrentFeTxNumFailures,
       "adGenImaLinkCurrentFeRxNumFailures": adGenImaLinkCurrentFeRxNumFailures,
       "adGenImaLinkCurrentTxStuffs": adGenImaLinkCurrentTxStuffs,
       "adGenImaLinkCurrentRxStuffs": adGenImaLinkCurrentRxStuffs,
       "adGenImaLinkIntervalTable": adGenImaLinkIntervalTable,
       "adGenImaLinkIntervalEntry": adGenImaLinkIntervalEntry,
       "adGenImaLinkIntervalNumber": adGenImaLinkIntervalNumber,
       "adGenImaLinkIntervalImaViolations": adGenImaLinkIntervalImaViolations,
       "adGenImaLinkIntervalOifAnomalies": adGenImaLinkIntervalOifAnomalies,
       "adGenImaLinkIntervalNeSevErroredSecs": adGenImaLinkIntervalNeSevErroredSecs,
       "adGenImaLinkIntervalFeSevErroredSecs": adGenImaLinkIntervalFeSevErroredSecs,
       "adGenImaLinkIntervalNeUnavailSecs": adGenImaLinkIntervalNeUnavailSecs,
       "adGenImaLinkIntervalFeUnavailSecs": adGenImaLinkIntervalFeUnavailSecs,
       "adGenImaLinkIntervalNeTxUnusableSecs": adGenImaLinkIntervalNeTxUnusableSecs,
       "adGenImaLinkIntervalNeRxUnusableSecs": adGenImaLinkIntervalNeRxUnusableSecs,
       "adGenImaLinkIntervalFeTxUnusableSecs": adGenImaLinkIntervalFeTxUnusableSecs,
       "adGenImaLinkIntervalFeRxUnusableSecs": adGenImaLinkIntervalFeRxUnusableSecs,
       "adGenImaLinkIntervalNeTxNumFailures": adGenImaLinkIntervalNeTxNumFailures,
       "adGenImaLinkIntervalNeRxNumFailures": adGenImaLinkIntervalNeRxNumFailures,
       "adGenImaLinkIntervalFeTxNumFailures": adGenImaLinkIntervalFeTxNumFailures,
       "adGenImaLinkIntervalFeRxNumFailures": adGenImaLinkIntervalFeRxNumFailures,
       "adGenImaLinkIntervalTxStuffs": adGenImaLinkIntervalTxStuffs,
       "adGenImaLinkIntervalRxStuffs": adGenImaLinkIntervalRxStuffs,
       "adGenImaLinkIntervalTimeStamp": adGenImaLinkIntervalTimeStamp,
       "adGenImaLinkTotalTable": adGenImaLinkTotalTable,
       "adGenImaLinkTotalEntry": adGenImaLinkTotalEntry,
       "adGenImaLinkTotalImaViolations": adGenImaLinkTotalImaViolations,
       "adGenImaLinkTotalOifAnomalies": adGenImaLinkTotalOifAnomalies,
       "adGenImaLinkTotalNeSevErroredSecs": adGenImaLinkTotalNeSevErroredSecs,
       "adGenImaLinkTotalFeSevErroredSecs": adGenImaLinkTotalFeSevErroredSecs,
       "adGenImaLinkTotalNeUnavailSecs": adGenImaLinkTotalNeUnavailSecs,
       "adGenImaLinkTotalFeUnavailSecs": adGenImaLinkTotalFeUnavailSecs,
       "adGenImaLinkTotalNeTxUnusableSecs": adGenImaLinkTotalNeTxUnusableSecs,
       "adGenImaLinkTotalNeRxUnusableSecs": adGenImaLinkTotalNeRxUnusableSecs,
       "adGenImaLinkTotalFeTxUnusableSecs": adGenImaLinkTotalFeTxUnusableSecs,
       "adGenImaLinkTotalFeRxUnusableSecs": adGenImaLinkTotalFeRxUnusableSecs,
       "adGenImaLinkTotalNeTxNumFailures": adGenImaLinkTotalNeTxNumFailures,
       "adGenImaLinkTotalNeRxNumFailures": adGenImaLinkTotalNeRxNumFailures,
       "adGenImaLinkTotalFeTxNumFailures": adGenImaLinkTotalFeTxNumFailures,
       "adGenImaLinkTotalFeRxNumFailures": adGenImaLinkTotalFeRxNumFailures,
       "adGenImaLinkTotalTxStuffs": adGenImaLinkTotalTxStuffs,
       "adGenImaLinkTotalRxStuffs": adGenImaLinkTotalRxStuffs,
       "adGenImaLinkDayCurrentTable": adGenImaLinkDayCurrentTable,
       "adGenImaLinkDayCurrentEntry": adGenImaLinkDayCurrentEntry,
       "adGenImaLinkDayCurrentImaViolations": adGenImaLinkDayCurrentImaViolations,
       "adGenImaLinkDayCurrentOifAnomalies": adGenImaLinkDayCurrentOifAnomalies,
       "adGenImaLinkDayCurrentNeSevErroredSecs": adGenImaLinkDayCurrentNeSevErroredSecs,
       "adGenImaLinkDayCurrentFeSevErroredSecs": adGenImaLinkDayCurrentFeSevErroredSecs,
       "adGenImaLinkDayCurrentNeUnavailSecs": adGenImaLinkDayCurrentNeUnavailSecs,
       "adGenImaLinkDayCurrentFeUnavailSecs": adGenImaLinkDayCurrentFeUnavailSecs,
       "adGenImaLinkDayCurrentNeTxUnusableSecs": adGenImaLinkDayCurrentNeTxUnusableSecs,
       "adGenImaLinkDayCurrentNeRxUnusableSecs": adGenImaLinkDayCurrentNeRxUnusableSecs,
       "adGenImaLinkDayCurrentFeTxUnusableSecs": adGenImaLinkDayCurrentFeTxUnusableSecs,
       "adGenImaLinkDayCurrentFeRxUnusableSecs": adGenImaLinkDayCurrentFeRxUnusableSecs,
       "adGenImaLinkDayCurrentNeTxNumFailures": adGenImaLinkDayCurrentNeTxNumFailures,
       "adGenImaLinkDayCurrentNeRxNumFailures": adGenImaLinkDayCurrentNeRxNumFailures,
       "adGenImaLinkDayCurrentFeTxNumFailures": adGenImaLinkDayCurrentFeTxNumFailures,
       "adGenImaLinkDayCurrentFeRxNumFailures": adGenImaLinkDayCurrentFeRxNumFailures,
       "adGenImaLinkDayCurrentTxStuffs": adGenImaLinkDayCurrentTxStuffs,
       "adGenImaLinkDayCurrentRxStuffs": adGenImaLinkDayCurrentRxStuffs,
       "adGenImaLinkDayIntervalTable": adGenImaLinkDayIntervalTable,
       "adGenImaLinkDayIntervalEntry": adGenImaLinkDayIntervalEntry,
       "adGenImaLinkDayIntervalNumber": adGenImaLinkDayIntervalNumber,
       "adGenImaLinkDayIntervalImaViolations": adGenImaLinkDayIntervalImaViolations,
       "adGenImaLinkDayIntervalOifAnomalies": adGenImaLinkDayIntervalOifAnomalies,
       "adGenImaLinkDayIntervalNeSevErroredSecs": adGenImaLinkDayIntervalNeSevErroredSecs,
       "adGenImaLinkDayIntervalFeSevErroredSecs": adGenImaLinkDayIntervalFeSevErroredSecs,
       "adGenImaLinkDayIntervalNeUnavailSecs": adGenImaLinkDayIntervalNeUnavailSecs,
       "adGenImaLinkDayIntervalFeUnavailSecs": adGenImaLinkDayIntervalFeUnavailSecs,
       "adGenImaLinkDayIntervalNeTxUnusableSecs": adGenImaLinkDayIntervalNeTxUnusableSecs,
       "adGenImaLinkDayIntervalNeRxUnusableSecs": adGenImaLinkDayIntervalNeRxUnusableSecs,
       "adGenImaLinkDayIntervalFeTxUnusableSecs": adGenImaLinkDayIntervalFeTxUnusableSecs,
       "adGenImaLinkDayIntervalFeRxUnusableSecs": adGenImaLinkDayIntervalFeRxUnusableSecs,
       "adGenImaLinkDayIntervalNeTxNumFailures": adGenImaLinkDayIntervalNeTxNumFailures,
       "adGenImaLinkDayIntervalNeRxNumFailures": adGenImaLinkDayIntervalNeRxNumFailures,
       "adGenImaLinkDayIntervalFeTxNumFailures": adGenImaLinkDayIntervalFeTxNumFailures,
       "adGenImaLinkDayIntervalFeRxNumFailures": adGenImaLinkDayIntervalFeRxNumFailures,
       "adGenImaLinkDayIntervalTxStuffs": adGenImaLinkDayIntervalTxStuffs,
       "adGenImaLinkDayIntervalRxStuffs": adGenImaLinkDayIntervalRxStuffs,
       "adGenImaLinkDayIntervalTimeStamp": adGenImaLinkDayIntervalTimeStamp,
       "adGenImaAlarmsPrefix": adGenImaAlarmsPrefix,
       "adGenImaAlarms": adGenImaAlarms,
       "adGenImaGroupCfgAbortClr": adGenImaGroupCfgAbortClr,
       "adGenImaGroupCfgAbortAct": adGenImaGroupCfgAbortAct,
       "adGenImaGroupCfgInsufficentLinksClr": adGenImaGroupCfgInsufficentLinksClr,
       "adGenImaGroupCfgInsufficentLinksAct": adGenImaGroupCfgInsufficentLinksAct,
       "adGenImaGroupFeStartupClr": adGenImaGroupFeStartupClr,
       "adGenImaGroupFeStartupAct": adGenImaGroupFeStartupAct,
       "adGenImaGroupFeCfgAbortClr": adGenImaGroupFeCfgAbortClr,
       "adGenImaGroupFeCfgAbortAct": adGenImaGroupFeCfgAbortAct,
       "adGenImaGroupFeCfgInsufficentLinksClr": adGenImaGroupFeCfgInsufficentLinksClr,
       "adGenImaGroupFeCfgInsufficentLinksAct": adGenImaGroupFeCfgInsufficentLinksAct,
       "adGenImaGroupFeBlockedClr": adGenImaGroupFeBlockedClr,
       "adGenImaGroupFeBlockedAct": adGenImaGroupFeBlockedAct,
       "adGenImaGroupTimingMismatchClr": adGenImaGroupTimingMismatchClr,
       "adGenImaGroupTimingMismatchAct": adGenImaGroupTimingMismatchAct,
       "adGenImaLinkLifClr": adGenImaLinkLifClr,
       "adGenImaLinkLifAct": adGenImaLinkLifAct,
       "adGenImaLinkLodsClr": adGenImaLinkLodsClr,
       "adGenImaLinkLodsAct": adGenImaLinkLodsAct,
       "adGenImaLinkRfiClr": adGenImaLinkRfiClr,
       "adGenImaLinkRfiAct": adGenImaLinkRfiAct,
       "adGenImaLinkTxMisconnectedClr": adGenImaLinkTxMisconnectedClr,
       "adGenImaLinkTxMisconnectedAct": adGenImaLinkTxMisconnectedAct,
       "adGenImaLinkRxMisconnectedClr": adGenImaLinkRxMisconnectedClr,
       "adGenImaLinkRxMisconnectedAct": adGenImaLinkRxMisconnectedAct,
       "adGenImaLinkTxFaultClr": adGenImaLinkTxFaultClr,
       "adGenImaLinkTxFaultAct": adGenImaLinkTxFaultAct,
       "adGenImaLinkRxFaultClr": adGenImaLinkRxFaultClr,
       "adGenImaLinkRxFaultAct": adGenImaLinkRxFaultAct,
       "adGenImaLinkFeTxUnusableClr": adGenImaLinkFeTxUnusableClr,
       "adGenImaLinkFeTxUnusableAct": adGenImaLinkFeTxUnusableAct,
       "adGenImaLinkFeRxUnusableClr": adGenImaLinkFeRxUnusableClr,
       "adGenImaLinkFeRxUnusableAct": adGenImaLinkFeRxUnusableAct,
       "adGenImaMIB": adGenImaMIB}
)
