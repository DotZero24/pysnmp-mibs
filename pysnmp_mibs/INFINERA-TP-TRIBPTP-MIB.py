# SNMP MIB module (INFINERA-TP-TRIBPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-TRIBPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:57 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,
 InfnAutoCableEqualization,
 InfnCfgProtState,
 InfnCurrProtState,
 InfnDirectionality,
 InfnEnableDisable,
 InfnEnetPswLaserCtrlState,
 InfnFecEncodingMode,
 InfnInterfaceType,
 InfnOperationalState,
 InfnPmHistStatsControl,
 InfnProtectionMode,
 InfnPsDirn,
 InfnReporting,
 InfnServiceType,
 InfnServiceTypeList,
 InfnSwitchReason,
 InfnSwitchRequestState,
 InfnTribAction) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnAutoCableEqualization",
    "InfnCfgProtState",
    "InfnCurrProtState",
    "InfnDirectionality",
    "InfnEnableDisable",
    "InfnEnetPswLaserCtrlState",
    "InfnFecEncodingMode",
    "InfnInterfaceType",
    "InfnOperationalState",
    "InfnPmHistStatsControl",
    "InfnProtectionMode",
    "InfnPsDirn",
    "InfnReporting",
    "InfnServiceType",
    "InfnServiceTypeList",
    "InfnSwitchReason",
    "InfnSwitchRequestState",
    "InfnTribAction")

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

tribPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17)
)
if mibBuilder.loadTexts:
    tribPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TribPtpTable_Object = MibTable
tribPtpTable = _TribPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    tribPtpTable.setStatus("current")
_TribPtpEntry_Object = MibTableRow
tribPtpEntry = _TribPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1)
)
tribPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tribPtpEntry.setStatus("current")
_TribPtpPgMoId_Type = DisplayString
_TribPtpPgMoId_Object = MibTableColumn
tribPtpPgMoId = _TribPtpPgMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 1),
    _TribPtpPgMoId_Type()
)
tribPtpPgMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPgMoId.setStatus("current")
_TribPtpProtMod_Type = InfnProtectionMode
_TribPtpProtMod_Object = MibTableColumn
tribPtpProtMod = _TribPtpProtMod_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 2),
    _TribPtpProtMod_Type()
)
tribPtpProtMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpProtMod.setStatus("current")
_TribPtpCfgProtSt_Type = InfnProtectionMode
_TribPtpCfgProtSt_Object = MibTableColumn
tribPtpCfgProtSt = _TribPtpCfgProtSt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 3),
    _TribPtpCfgProtSt_Type()
)
tribPtpCfgProtSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpCfgProtSt.setStatus("current")
_TribPtpCurProtSt_Type = InfnCurrProtState
_TribPtpCurProtSt_Object = MibTableColumn
tribPtpCurProtSt = _TribPtpCurProtSt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 4),
    _TribPtpCurProtSt_Type()
)
tribPtpCurProtSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpCurProtSt.setStatus("current")
_TribPtpPsDirn_Type = InfnPsDirn
_TribPtpPsDirn_Object = MibTableColumn
tribPtpPsDirn = _TribPtpPsDirn_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 5),
    _TribPtpPsDirn_Type()
)
tribPtpPsDirn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPsDirn.setStatus("current")
_TribPtpSwReason_Type = InfnSwitchReason
_TribPtpSwReason_Object = MibTableColumn
tribPtpSwReason = _TribPtpSwReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 6),
    _TribPtpSwReason_Type()
)
tribPtpSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpSwReason.setStatus("current")
_TribPtpSwRqState_Type = InfnSwitchRequestState
_TribPtpSwRqState_Object = MibTableColumn
tribPtpSwRqState = _TribPtpSwRqState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 7),
    _TribPtpSwRqState_Type()
)
tribPtpSwRqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpSwRqState.setStatus("current")
_TribPtpMaxPerChannelCapacity_Type = InfnServiceType
_TribPtpMaxPerChannelCapacity_Object = MibTableColumn
tribPtpMaxPerChannelCapacity = _TribPtpMaxPerChannelCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 8),
    _TribPtpMaxPerChannelCapacity_Type()
)
tribPtpMaxPerChannelCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpMaxPerChannelCapacity.setStatus("current")


class _TribPtpTribDisableAction_Type(InfnTribAction):
    """Custom type tribPtpTribDisableAction based on InfnTribAction"""
    defaultValue = 3


_TribPtpTribDisableAction_Type.__name__ = "InfnTribAction"
_TribPtpTribDisableAction_Object = MibTableColumn
tribPtpTribDisableAction = _TribPtpTribDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 9),
    _TribPtpTribDisableAction_Type()
)
tribPtpTribDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpTribDisableAction.setStatus("current")
_TribPtpProvisionedServiceType_Type = InfnServiceType
_TribPtpProvisionedServiceType_Object = MibTableColumn
tribPtpProvisionedServiceType = _TribPtpProvisionedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 10),
    _TribPtpProvisionedServiceType_Type()
)
tribPtpProvisionedServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpProvisionedServiceType.setStatus("current")


class _TribPtpOprOorHighThresholdOffset_Type(FloatTenths):
    """Custom type tribPtpOprOorHighThresholdOffset based on FloatTenths"""
    defaultValue = 0


_TribPtpOprOorHighThresholdOffset_Type.__name__ = "FloatTenths"
_TribPtpOprOorHighThresholdOffset_Object = MibTableColumn
tribPtpOprOorHighThresholdOffset = _TribPtpOprOorHighThresholdOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 11),
    _TribPtpOprOorHighThresholdOffset_Type()
)
tribPtpOprOorHighThresholdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpOprOorHighThresholdOffset.setStatus("current")


class _TribPtpOprOorLowThresholdOffset_Type(FloatTenths):
    """Custom type tribPtpOprOorLowThresholdOffset based on FloatTenths"""
    defaultValue = 0


_TribPtpOprOorLowThresholdOffset_Type.__name__ = "FloatTenths"
_TribPtpOprOorLowThresholdOffset_Object = MibTableColumn
tribPtpOprOorLowThresholdOffset = _TribPtpOprOorLowThresholdOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 12),
    _TribPtpOprOorLowThresholdOffset_Type()
)
tribPtpOprOorLowThresholdOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpOprOorLowThresholdOffset.setStatus("current")


class _TribPtpOprOorAlarmReporting_Type(InfnReporting):
    """Custom type tribPtpOprOorAlarmReporting based on InfnReporting"""
    defaultValue = 1


_TribPtpOprOorAlarmReporting_Type.__name__ = "InfnReporting"
_TribPtpOprOorAlarmReporting_Object = MibTableColumn
tribPtpOprOorAlarmReporting = _TribPtpOprOorAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 13),
    _TribPtpOprOorAlarmReporting_Type()
)
tribPtpOprOorAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpOprOorAlarmReporting.setStatus("current")
_TribPtpOprOverloadThreshold_Type = FloatTenths
_TribPtpOprOverloadThreshold_Object = MibTableColumn
tribPtpOprOverloadThreshold = _TribPtpOprOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 14),
    _TribPtpOprOverloadThreshold_Type()
)
tribPtpOprOverloadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpOprOverloadThreshold.setStatus("current")
_TribPtpOprSensitivityThreshold_Type = FloatTenths
_TribPtpOprSensitivityThreshold_Object = MibTableColumn
tribPtpOprSensitivityThreshold = _TribPtpOprSensitivityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 15),
    _TribPtpOprSensitivityThreshold_Type()
)
tribPtpOprSensitivityThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpOprSensitivityThreshold.setStatus("current")


class _TribPtpAINS_Type(InfnOperationalState):
    """Custom type tribPtpAINS based on InfnOperationalState"""
    defaultValue = 1


_TribPtpAINS_Type.__name__ = "InfnOperationalState"
_TribPtpAINS_Object = MibTableColumn
tribPtpAINS = _TribPtpAINS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 16),
    _TribPtpAINS_Type()
)
tribPtpAINS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpAINS.setStatus("current")


class _TribPtpValidSignalTimeInterval_Type(Integer32):
    """Custom type tribPtpValidSignalTimeInterval based on Integer32"""
    defaultValue = 480


_TribPtpValidSignalTimeInterval_Type.__name__ = "Integer32"
_TribPtpValidSignalTimeInterval_Object = MibTableColumn
tribPtpValidSignalTimeInterval = _TribPtpValidSignalTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 17),
    _TribPtpValidSignalTimeInterval_Type()
)
tribPtpValidSignalTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpValidSignalTimeInterval.setStatus("current")
_TribPtpRemValidSignalTimer_Type = Integer32
_TribPtpRemValidSignalTimer_Object = MibTableColumn
tribPtpRemValidSignalTimer = _TribPtpRemValidSignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 18),
    _TribPtpRemValidSignalTimer_Type()
)
tribPtpRemValidSignalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpRemValidSignalTimer.setStatus("current")
_TribPtpSupportedServiceTypes_Type = InfnServiceTypeList
_TribPtpSupportedServiceTypes_Object = MibTableColumn
tribPtpSupportedServiceTypes = _TribPtpSupportedServiceTypes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 19),
    _TribPtpSupportedServiceTypes_Type()
)
tribPtpSupportedServiceTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpSupportedServiceTypes.setStatus("current")


class _TribPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type tribPtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_TribPtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_TribPtpPmHistStatsEnable_Object = MibTableColumn
tribPtpPmHistStatsEnable = _TribPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 20),
    _TribPtpPmHistStatsEnable_Type()
)
tribPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpPmHistStatsEnable.setStatus("current")
_TribPtpMaxAllowedDrops_Type = Integer32
_TribPtpMaxAllowedDrops_Object = MibTableColumn
tribPtpMaxAllowedDrops = _TribPtpMaxAllowedDrops_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 21),
    _TribPtpMaxAllowedDrops_Type()
)
tribPtpMaxAllowedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpMaxAllowedDrops.setStatus("current")
_TribPtpCurrNumOfDrops_Type = Integer32
_TribPtpCurrNumOfDrops_Object = MibTableColumn
tribPtpCurrNumOfDrops = _TribPtpCurrNumOfDrops_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 22),
    _TribPtpCurrNumOfDrops_Type()
)
tribPtpCurrNumOfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpCurrNumOfDrops.setStatus("current")
_TribPtpLocalInterfaceIndex_Type = Integer32
_TribPtpLocalInterfaceIndex_Object = MibTableColumn
tribPtpLocalInterfaceIndex = _TribPtpLocalInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 23),
    _TribPtpLocalInterfaceIndex_Type()
)
tribPtpLocalInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpLocalInterfaceIndex.setStatus("current")


class _TribPtpRemoteInterfaceIndex_Type(Integer32):
    """Custom type tribPtpRemoteInterfaceIndex based on Integer32"""
    defaultValue = 0


_TribPtpRemoteInterfaceIndex_Type.__name__ = "Integer32"
_TribPtpRemoteInterfaceIndex_Object = MibTableColumn
tribPtpRemoteInterfaceIndex = _TribPtpRemoteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 24),
    _TribPtpRemoteInterfaceIndex_Type()
)
tribPtpRemoteInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpRemoteInterfaceIndex.setStatus("current")
_TribPtpAssocMoInteropCPTEInterface_Type = DisplayString
_TribPtpAssocMoInteropCPTEInterface_Object = MibTableColumn
tribPtpAssocMoInteropCPTEInterface = _TribPtpAssocMoInteropCPTEInterface_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 25),
    _TribPtpAssocMoInteropCPTEInterface_Type()
)
tribPtpAssocMoInteropCPTEInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpAssocMoInteropCPTEInterface.setStatus("current")


class _TribPtpDtpAISOnClientSF_Type(InfnOperationalState):
    """Custom type tribPtpDtpAISOnClientSF based on InfnOperationalState"""
    defaultValue = 1


_TribPtpDtpAISOnClientSF_Type.__name__ = "InfnOperationalState"
_TribPtpDtpAISOnClientSF_Object = MibTableColumn
tribPtpDtpAISOnClientSF = _TribPtpDtpAISOnClientSF_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 26),
    _TribPtpDtpAISOnClientSF_Type()
)
tribPtpDtpAISOnClientSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpDtpAISOnClientSF.setStatus("current")


class _TribPtpEnetPswLaserCtrl_Type(InfnEnetPswLaserCtrlState):
    """Custom type tribPtpEnetPswLaserCtrl based on InfnEnetPswLaserCtrlState"""
    defaultValue = 1


_TribPtpEnetPswLaserCtrl_Type.__name__ = "InfnEnetPswLaserCtrlState"
_TribPtpEnetPswLaserCtrl_Object = MibTableColumn
tribPtpEnetPswLaserCtrl = _TribPtpEnetPswLaserCtrl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 27),
    _TribPtpEnetPswLaserCtrl_Type()
)
tribPtpEnetPswLaserCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpEnetPswLaserCtrl.setStatus("current")


class _TribPtpDisableActionOnBERSF_Type(InfnEnableDisable):
    """Custom type tribPtpDisableActionOnBERSF based on InfnEnableDisable"""
    defaultValue = 1


_TribPtpDisableActionOnBERSF_Type.__name__ = "InfnEnableDisable"
_TribPtpDisableActionOnBERSF_Object = MibTableColumn
tribPtpDisableActionOnBERSF = _TribPtpDisableActionOnBERSF_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 28),
    _TribPtpDisableActionOnBERSF_Type()
)
tribPtpDisableActionOnBERSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpDisableActionOnBERSF.setStatus("current")


class _TribPtpAutoCableEqualization_Type(InfnAutoCableEqualization):
    """Custom type tribPtpAutoCableEqualization based on InfnAutoCableEqualization"""
    defaultValue = 1


_TribPtpAutoCableEqualization_Type.__name__ = "InfnAutoCableEqualization"
_TribPtpAutoCableEqualization_Object = MibTableColumn
tribPtpAutoCableEqualization = _TribPtpAutoCableEqualization_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 29),
    _TribPtpAutoCableEqualization_Type()
)
tribPtpAutoCableEqualization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpAutoCableEqualization.setStatus("current")


class _TribPtpDirectionality_Type(InfnDirectionality):
    """Custom type tribPtpDirectionality based on InfnDirectionality"""
    defaultValue = 3


_TribPtpDirectionality_Type.__name__ = "InfnDirectionality"
_TribPtpDirectionality_Object = MibTableColumn
tribPtpDirectionality = _TribPtpDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 30),
    _TribPtpDirectionality_Type()
)
tribPtpDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpDirectionality.setStatus("current")
_TribPtpInterfaceType_Type = InfnInterfaceType
_TribPtpInterfaceType_Object = MibTableColumn
tribPtpInterfaceType = _TribPtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 31),
    _TribPtpInterfaceType_Type()
)
tribPtpInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpInterfaceType.setStatus("current")


class _TribPtpAutoDiscovery_Type(InfnEnableDisable):
    """Custom type tribPtpAutoDiscovery based on InfnEnableDisable"""
    defaultValue = 2


_TribPtpAutoDiscovery_Type.__name__ = "InfnEnableDisable"
_TribPtpAutoDiscovery_Object = MibTableColumn
tribPtpAutoDiscovery = _TribPtpAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 32),
    _TribPtpAutoDiscovery_Type()
)
tribPtpAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpAutoDiscovery.setStatus("current")
_TribPtpDiscoveredRemoteTP_Type = DisplayString
_TribPtpDiscoveredRemoteTP_Object = MibTableColumn
tribPtpDiscoveredRemoteTP = _TribPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 33),
    _TribPtpDiscoveredRemoteTP_Type()
)
tribPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpDiscoveredRemoteTP.setStatus("current")
_TribPtpProvisionedRemoteTP_Type = DisplayString
_TribPtpProvisionedRemoteTP_Object = MibTableColumn
tribPtpProvisionedRemoteTP = _TribPtpProvisionedRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 34),
    _TribPtpProvisionedRemoteTP_Type()
)
tribPtpProvisionedRemoteTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpProvisionedRemoteTP.setStatus("current")


class _TribPtpForwardDefectTDATrigger_Type(InfnEnableDisable):
    """Custom type tribPtpForwardDefectTDATrigger based on InfnEnableDisable"""
    defaultValue = 1


_TribPtpForwardDefectTDATrigger_Type.__name__ = "InfnEnableDisable"
_TribPtpForwardDefectTDATrigger_Object = MibTableColumn
tribPtpForwardDefectTDATrigger = _TribPtpForwardDefectTDATrigger_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 35),
    _TribPtpForwardDefectTDATrigger_Type()
)
tribPtpForwardDefectTDATrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpForwardDefectTDATrigger.setStatus("current")
_TribPtpProvisionedFecEncodingMode_Type = InfnFecEncodingMode
_TribPtpProvisionedFecEncodingMode_Object = MibTableColumn
tribPtpProvisionedFecEncodingMode = _TribPtpProvisionedFecEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 36),
    _TribPtpProvisionedFecEncodingMode_Type()
)
tribPtpProvisionedFecEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tribPtpProvisionedFecEncodingMode.setStatus("current")
_TribPtpAppliedFecEncodingMode_Type = InfnFecEncodingMode
_TribPtpAppliedFecEncodingMode_Object = MibTableColumn
tribPtpAppliedFecEncodingMode = _TribPtpAppliedFecEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 1, 1, 37),
    _TribPtpAppliedFecEncodingMode_Type()
)
tribPtpAppliedFecEncodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpAppliedFecEncodingMode.setStatus("current")
_TribPtpConformance_ObjectIdentity = ObjectIdentity
tribPtpConformance = _TribPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 3)
)
_TribPtpCompliances_ObjectIdentity = ObjectIdentity
tribPtpCompliances = _TribPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 3, 1)
)
_TribPtpGroups_ObjectIdentity = ObjectIdentity
tribPtpGroups = _TribPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 3, 2)
)

# Managed Objects groups

tribPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 3, 2, 1)
)
tribPtpGroup.setObjects(
      *(("INFINERA-TP-TRIBPTP-MIB", "tribPtpPgMoId"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpProtMod"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpCfgProtSt"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpCurProtSt"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpPsDirn"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpSwReason"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpSwRqState"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpMaxPerChannelCapacity"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpTribDisableAction"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpProvisionedServiceType"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpOprOorHighThresholdOffset"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpOprOorLowThresholdOffset"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpOprOorAlarmReporting"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpOprOverloadThreshold"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpOprSensitivityThreshold"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpAINS"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpValidSignalTimeInterval"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpRemValidSignalTimer"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpSupportedServiceTypes"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpPmHistStatsEnable"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpMaxAllowedDrops"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpCurrNumOfDrops"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpLocalInterfaceIndex"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpRemoteInterfaceIndex"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpAssocMoInteropCPTEInterface"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpDtpAISOnClientSF"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpEnetPswLaserCtrl"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpDisableActionOnBERSF"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpAutoCableEqualization"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpDirectionality"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpInterfaceType"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpAutoDiscovery"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpProvisionedRemoteTP"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpForwardDefectTDATrigger"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpProvisionedFecEncodingMode"),
        ("INFINERA-TP-TRIBPTP-MIB", "tribPtpAppliedFecEncodingMode"))
)
if mibBuilder.loadTexts:
    tribPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tribPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 17, 3, 1, 1)
)
tribPtpCompliance.setObjects(
    ("INFINERA-TP-TRIBPTP-MIB", "tribPtpGroup")
)
if mibBuilder.loadTexts:
    tribPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-TRIBPTP-MIB",
    **{"tribPtpMIB": tribPtpMIB,
       "tribPtpTable": tribPtpTable,
       "tribPtpEntry": tribPtpEntry,
       "tribPtpPgMoId": tribPtpPgMoId,
       "tribPtpProtMod": tribPtpProtMod,
       "tribPtpCfgProtSt": tribPtpCfgProtSt,
       "tribPtpCurProtSt": tribPtpCurProtSt,
       "tribPtpPsDirn": tribPtpPsDirn,
       "tribPtpSwReason": tribPtpSwReason,
       "tribPtpSwRqState": tribPtpSwRqState,
       "tribPtpMaxPerChannelCapacity": tribPtpMaxPerChannelCapacity,
       "tribPtpTribDisableAction": tribPtpTribDisableAction,
       "tribPtpProvisionedServiceType": tribPtpProvisionedServiceType,
       "tribPtpOprOorHighThresholdOffset": tribPtpOprOorHighThresholdOffset,
       "tribPtpOprOorLowThresholdOffset": tribPtpOprOorLowThresholdOffset,
       "tribPtpOprOorAlarmReporting": tribPtpOprOorAlarmReporting,
       "tribPtpOprOverloadThreshold": tribPtpOprOverloadThreshold,
       "tribPtpOprSensitivityThreshold": tribPtpOprSensitivityThreshold,
       "tribPtpAINS": tribPtpAINS,
       "tribPtpValidSignalTimeInterval": tribPtpValidSignalTimeInterval,
       "tribPtpRemValidSignalTimer": tribPtpRemValidSignalTimer,
       "tribPtpSupportedServiceTypes": tribPtpSupportedServiceTypes,
       "tribPtpPmHistStatsEnable": tribPtpPmHistStatsEnable,
       "tribPtpMaxAllowedDrops": tribPtpMaxAllowedDrops,
       "tribPtpCurrNumOfDrops": tribPtpCurrNumOfDrops,
       "tribPtpLocalInterfaceIndex": tribPtpLocalInterfaceIndex,
       "tribPtpRemoteInterfaceIndex": tribPtpRemoteInterfaceIndex,
       "tribPtpAssocMoInteropCPTEInterface": tribPtpAssocMoInteropCPTEInterface,
       "tribPtpDtpAISOnClientSF": tribPtpDtpAISOnClientSF,
       "tribPtpEnetPswLaserCtrl": tribPtpEnetPswLaserCtrl,
       "tribPtpDisableActionOnBERSF": tribPtpDisableActionOnBERSF,
       "tribPtpAutoCableEqualization": tribPtpAutoCableEqualization,
       "tribPtpDirectionality": tribPtpDirectionality,
       "tribPtpInterfaceType": tribPtpInterfaceType,
       "tribPtpAutoDiscovery": tribPtpAutoDiscovery,
       "tribPtpDiscoveredRemoteTP": tribPtpDiscoveredRemoteTP,
       "tribPtpProvisionedRemoteTP": tribPtpProvisionedRemoteTP,
       "tribPtpForwardDefectTDATrigger": tribPtpForwardDefectTDATrigger,
       "tribPtpProvisionedFecEncodingMode": tribPtpProvisionedFecEncodingMode,
       "tribPtpAppliedFecEncodingMode": tribPtpAppliedFecEncodingMode,
       "tribPtpConformance": tribPtpConformance,
       "tribPtpCompliances": tribPtpCompliances,
       "tribPtpCompliance": tribPtpCompliance,
       "tribPtpGroups": tribPtpGroups,
       "tribPtpGroup": tribPtpGroup}
)
