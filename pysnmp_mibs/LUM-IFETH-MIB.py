# SNMP MIB module (LUM-IFETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFETH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:03 2025
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

(lumIfEthMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfEthMIB",
    "lumModules")

(AutoNegotiationStatus,
 FaultStatusWithNA,
 FlowControlMode,
 MgmtNameString,
 OnOff,
 RsFecMode,
 RsFecOnOff,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AutoNegotiationStatus",
    "FaultStatusWithNA",
    "FlowControlMode",
    "MgmtNameString",
    "OnOff",
    "RsFecMode",
    "RsFecOnOff",
    "SignalStatusWithNA",
    "Unsigned32WithNA")

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

lumIfEthMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 54)
)
if mibBuilder.loadTexts:
    lumIfEthMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-11-30 00:00",
         "2015-12-22 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2012-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfEthConfs_ObjectIdentity = ObjectIdentity
lumIfEthConfs = _LumIfEthConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1)
)
_LumIfEthGroups_ObjectIdentity = ObjectIdentity
lumIfEthGroups = _LumIfEthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1)
)
_LumIfEthCompl_ObjectIdentity = ObjectIdentity
lumIfEthCompl = _LumIfEthCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2)
)
_LumIfEthMIBObjects_ObjectIdentity = ObjectIdentity
lumIfEthMIBObjects = _LumIfEthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2)
)
_IfEthGeneral_ObjectIdentity = ObjectIdentity
ifEthGeneral = _IfEthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1)
)
_IfEthGeneralConfigLastChangeTime_Type = DateAndTime
_IfEthGeneralConfigLastChangeTime_Object = MibScalar
ifEthGeneralConfigLastChangeTime = _IfEthGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 1),
    _IfEthGeneralConfigLastChangeTime_Type()
)
ifEthGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralConfigLastChangeTime.setStatus("current")
_IfEthGeneralStateLastChangeTime_Type = DateAndTime
_IfEthGeneralStateLastChangeTime_Object = MibScalar
ifEthGeneralStateLastChangeTime = _IfEthGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 2),
    _IfEthGeneralStateLastChangeTime_Type()
)
ifEthGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralStateLastChangeTime.setStatus("current")
_IfEthGeneralIfEthPhysicalTableSize_Type = Unsigned32
_IfEthGeneralIfEthPhysicalTableSize_Object = MibScalar
ifEthGeneralIfEthPhysicalTableSize = _IfEthGeneralIfEthPhysicalTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 3),
    _IfEthGeneralIfEthPhysicalTableSize_Type()
)
ifEthGeneralIfEthPhysicalTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthPhysicalTableSize.setStatus("current")
_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Object = MibScalar
ifEthGeneralIfEthPhysicalConfigLastChangeTime = _IfEthGeneralIfEthPhysicalConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 4),
    _IfEthGeneralIfEthPhysicalConfigLastChangeTime_Type()
)
ifEthGeneralIfEthPhysicalConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthPhysicalConfigLastChangeTime.setStatus("current")
_IfEthGeneralIfEthPhysicalStateLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthPhysicalStateLastChangeTime_Object = MibScalar
ifEthGeneralIfEthPhysicalStateLastChangeTime = _IfEthGeneralIfEthPhysicalStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 5),
    _IfEthGeneralIfEthPhysicalStateLastChangeTime_Type()
)
ifEthGeneralIfEthPhysicalStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthPhysicalStateLastChangeTime.setStatus("current")
_IfEthGeneralIfEthMacTableSize_Type = Unsigned32
_IfEthGeneralIfEthMacTableSize_Object = MibScalar
ifEthGeneralIfEthMacTableSize = _IfEthGeneralIfEthMacTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 6),
    _IfEthGeneralIfEthMacTableSize_Type()
)
ifEthGeneralIfEthMacTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthMacTableSize.setStatus("current")
_IfEthGeneralIfEthMacConfigLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthMacConfigLastChangeTime_Object = MibScalar
ifEthGeneralIfEthMacConfigLastChangeTime = _IfEthGeneralIfEthMacConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 7),
    _IfEthGeneralIfEthMacConfigLastChangeTime_Type()
)
ifEthGeneralIfEthMacConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthMacConfigLastChangeTime.setStatus("current")
_IfEthGeneralIfEthMacStateLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthMacStateLastChangeTime_Object = MibScalar
ifEthGeneralIfEthMacStateLastChangeTime = _IfEthGeneralIfEthMacStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 8),
    _IfEthGeneralIfEthMacStateLastChangeTime_Type()
)
ifEthGeneralIfEthMacStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthMacStateLastChangeTime.setStatus("current")
_IfEthGeneralIfEthRsFecTableSize_Type = Unsigned32
_IfEthGeneralIfEthRsFecTableSize_Object = MibScalar
ifEthGeneralIfEthRsFecTableSize = _IfEthGeneralIfEthRsFecTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 9),
    _IfEthGeneralIfEthRsFecTableSize_Type()
)
ifEthGeneralIfEthRsFecTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthRsFecTableSize.setStatus("current")
_IfEthGeneralIfEthRsFecConfigLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthRsFecConfigLastChangeTime_Object = MibScalar
ifEthGeneralIfEthRsFecConfigLastChangeTime = _IfEthGeneralIfEthRsFecConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 10),
    _IfEthGeneralIfEthRsFecConfigLastChangeTime_Type()
)
ifEthGeneralIfEthRsFecConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthRsFecConfigLastChangeTime.setStatus("current")
_IfEthGeneralIfEthRsFecStateLastChangeTime_Type = DateAndTime
_IfEthGeneralIfEthRsFecStateLastChangeTime_Object = MibScalar
ifEthGeneralIfEthRsFecStateLastChangeTime = _IfEthGeneralIfEthRsFecStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 1, 11),
    _IfEthGeneralIfEthRsFecStateLastChangeTime_Type()
)
ifEthGeneralIfEthRsFecStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthGeneralIfEthRsFecStateLastChangeTime.setStatus("current")
_IfEthPhysicalList_ObjectIdentity = ObjectIdentity
ifEthPhysicalList = _IfEthPhysicalList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2)
)
_IfEthPhysicalTable_Object = MibTable
ifEthPhysicalTable = _IfEthPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifEthPhysicalTable.setStatus("current")
_IfEthPhysicalEntry_Object = MibTableRow
ifEthPhysicalEntry = _IfEthPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1)
)
ifEthPhysicalEntry.setIndexNames(
    (0, "LUM-IFETH-MIB", "ifEthPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ifEthPhysicalEntry.setStatus("current")
_IfEthPhysicalIndex_Type = Unsigned32
_IfEthPhysicalIndex_Object = MibTableColumn
ifEthPhysicalIndex = _IfEthPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 1),
    _IfEthPhysicalIndex_Type()
)
ifEthPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalIndex.setStatus("current")
_IfEthPhysicalName_Type = MgmtNameString
_IfEthPhysicalName_Object = MibTableColumn
ifEthPhysicalName = _IfEthPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 2),
    _IfEthPhysicalName_Type()
)
ifEthPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalName.setStatus("current")
_IfEthPhysicalConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfEthPhysicalConnIfBasicIfIndex_Object = MibTableColumn
ifEthPhysicalConnIfBasicIfIndex = _IfEthPhysicalConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 3),
    _IfEthPhysicalConnIfBasicIfIndex_Type()
)
ifEthPhysicalConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalConnIfBasicIfIndex.setStatus("current")


class _IfEthPhysicalAutoNegotiationMode_Type(OnOff):
    """Custom type ifEthPhysicalAutoNegotiationMode based on OnOff"""
    defaultValue = 2


_IfEthPhysicalAutoNegotiationMode_Type.__name__ = "OnOff"
_IfEthPhysicalAutoNegotiationMode_Object = MibTableColumn
ifEthPhysicalAutoNegotiationMode = _IfEthPhysicalAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 4),
    _IfEthPhysicalAutoNegotiationMode_Type()
)
ifEthPhysicalAutoNegotiationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalAutoNegotiationMode.setStatus("current")
_IfEthPhysicalAutoNegotiationStatus_Type = AutoNegotiationStatus
_IfEthPhysicalAutoNegotiationStatus_Object = MibTableColumn
ifEthPhysicalAutoNegotiationStatus = _IfEthPhysicalAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 5),
    _IfEthPhysicalAutoNegotiationStatus_Type()
)
ifEthPhysicalAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalAutoNegotiationStatus.setStatus("current")


class _IfEthPhysicalRxUtilization_Type(Unsigned32WithNA):
    """Custom type ifEthPhysicalRxUtilization based on Unsigned32WithNA"""
    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthPhysicalRxUtilization_Type.__name__ = "Unsigned32WithNA"
_IfEthPhysicalRxUtilization_Object = MibTableColumn
ifEthPhysicalRxUtilization = _IfEthPhysicalRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 6),
    _IfEthPhysicalRxUtilization_Type()
)
ifEthPhysicalRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRxUtilization.setStatus("current")


class _IfEthPhysicalTxUtilization_Type(Unsigned32WithNA):
    """Custom type ifEthPhysicalTxUtilization based on Unsigned32WithNA"""
    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthPhysicalTxUtilization_Type.__name__ = "Unsigned32WithNA"
_IfEthPhysicalTxUtilization_Object = MibTableColumn
ifEthPhysicalTxUtilization = _IfEthPhysicalTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 7),
    _IfEthPhysicalTxUtilization_Type()
)
ifEthPhysicalTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxUtilization.setStatus("current")
_IfEthPhysicalTxSignalStatus_Type = SignalStatusWithNA
_IfEthPhysicalTxSignalStatus_Object = MibTableColumn
ifEthPhysicalTxSignalStatus = _IfEthPhysicalTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 8),
    _IfEthPhysicalTxSignalStatus_Type()
)
ifEthPhysicalTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxSignalStatus.setStatus("current")
_IfEthPhysicalRxSignalStatus_Type = SignalStatusWithNA
_IfEthPhysicalRxSignalStatus_Object = MibTableColumn
ifEthPhysicalRxSignalStatus = _IfEthPhysicalRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 9),
    _IfEthPhysicalRxSignalStatus_Type()
)
ifEthPhysicalRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRxSignalStatus.setStatus("current")
_IfEthPhysicalRemoteLinkFault_Type = FaultStatusWithNA
_IfEthPhysicalRemoteLinkFault_Object = MibTableColumn
ifEthPhysicalRemoteLinkFault = _IfEthPhysicalRemoteLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 10),
    _IfEthPhysicalRemoteLinkFault_Type()
)
ifEthPhysicalRemoteLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRemoteLinkFault.setStatus("current")
_IfEthPhysicalLocalLinkFault_Type = FaultStatusWithNA
_IfEthPhysicalLocalLinkFault_Object = MibTableColumn
ifEthPhysicalLocalLinkFault = _IfEthPhysicalLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 11),
    _IfEthPhysicalLocalLinkFault_Type()
)
ifEthPhysicalLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalLocalLinkFault.setStatus("current")
_IfEthPhysicalLinkDown_Type = FaultStatusWithNA
_IfEthPhysicalLinkDown_Object = MibTableColumn
ifEthPhysicalLinkDown = _IfEthPhysicalLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 12),
    _IfEthPhysicalLinkDown_Type()
)
ifEthPhysicalLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalLinkDown.setStatus("current")
_IfEthPhysicalHighBitErrorRate_Type = FaultStatusWithNA
_IfEthPhysicalHighBitErrorRate_Object = MibTableColumn
ifEthPhysicalHighBitErrorRate = _IfEthPhysicalHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 13),
    _IfEthPhysicalHighBitErrorRate_Type()
)
ifEthPhysicalHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalHighBitErrorRate.setStatus("current")
_IfEthPhysicalPcsLossOfFrame_Type = FaultStatusWithNA
_IfEthPhysicalPcsLossOfFrame_Object = MibTableColumn
ifEthPhysicalPcsLossOfFrame = _IfEthPhysicalPcsLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 14),
    _IfEthPhysicalPcsLossOfFrame_Type()
)
ifEthPhysicalPcsLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalPcsLossOfFrame.setStatus("current")
_IfEthPhysicalRxLocalLinkFault_Type = FaultStatusWithNA
_IfEthPhysicalRxLocalLinkFault_Object = MibTableColumn
ifEthPhysicalRxLocalLinkFault = _IfEthPhysicalRxLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 15),
    _IfEthPhysicalRxLocalLinkFault_Type()
)
ifEthPhysicalRxLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRxLocalLinkFault.setStatus("current")
_IfEthPhysicalTxLocalLinkFault_Type = FaultStatusWithNA
_IfEthPhysicalTxLocalLinkFault_Object = MibTableColumn
ifEthPhysicalTxLocalLinkFault = _IfEthPhysicalTxLocalLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 16),
    _IfEthPhysicalTxLocalLinkFault_Type()
)
ifEthPhysicalTxLocalLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxLocalLinkFault.setStatus("current")
_IfEthPhysicalRxHighBitErrorRate_Type = FaultStatusWithNA
_IfEthPhysicalRxHighBitErrorRate_Object = MibTableColumn
ifEthPhysicalRxHighBitErrorRate = _IfEthPhysicalRxHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 17),
    _IfEthPhysicalRxHighBitErrorRate_Type()
)
ifEthPhysicalRxHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRxHighBitErrorRate.setStatus("current")
_IfEthPhysicalTxHighBitErrorRate_Type = FaultStatusWithNA
_IfEthPhysicalTxHighBitErrorRate_Object = MibTableColumn
ifEthPhysicalTxHighBitErrorRate = _IfEthPhysicalTxHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 18),
    _IfEthPhysicalTxHighBitErrorRate_Type()
)
ifEthPhysicalTxHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxHighBitErrorRate.setStatus("current")
_IfEthPhysicalTxPcsLossOfFrame_Type = FaultStatusWithNA
_IfEthPhysicalTxPcsLossOfFrame_Object = MibTableColumn
ifEthPhysicalTxPcsLossOfFrame = _IfEthPhysicalTxPcsLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 19),
    _IfEthPhysicalTxPcsLossOfFrame_Type()
)
ifEthPhysicalTxPcsLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxPcsLossOfFrame.setStatus("current")
_IfEthPhysicalUId_Type = Unsigned32
_IfEthPhysicalUId_Object = MibTableColumn
ifEthPhysicalUId = _IfEthPhysicalUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 20),
    _IfEthPhysicalUId_Type()
)
ifEthPhysicalUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalUId.setStatus("current")
_IfEthPhysicalRxPcsLossOfSync_Type = FaultStatusWithNA
_IfEthPhysicalRxPcsLossOfSync_Object = MibTableColumn
ifEthPhysicalRxPcsLossOfSync = _IfEthPhysicalRxPcsLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 21),
    _IfEthPhysicalRxPcsLossOfSync_Type()
)
ifEthPhysicalRxPcsLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalRxPcsLossOfSync.setStatus("current")
_IfEthPhysicalTxPcsLossOfSync_Type = FaultStatusWithNA
_IfEthPhysicalTxPcsLossOfSync_Object = MibTableColumn
ifEthPhysicalTxPcsLossOfSync = _IfEthPhysicalTxPcsLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 2, 1, 1, 22),
    _IfEthPhysicalTxPcsLossOfSync_Type()
)
ifEthPhysicalTxPcsLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthPhysicalTxPcsLossOfSync.setStatus("current")
_IfEthMacList_ObjectIdentity = ObjectIdentity
ifEthMacList = _IfEthMacList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3)
)
_IfEthMacTable_Object = MibTable
ifEthMacTable = _IfEthMacTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifEthMacTable.setStatus("current")
_IfEthMacEntry_Object = MibTableRow
ifEthMacEntry = _IfEthMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1)
)
ifEthMacEntry.setIndexNames(
    (0, "LUM-IFETH-MIB", "ifEthMacIndex"),
)
if mibBuilder.loadTexts:
    ifEthMacEntry.setStatus("current")
_IfEthMacIndex_Type = Unsigned32
_IfEthMacIndex_Object = MibTableColumn
ifEthMacIndex = _IfEthMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 1),
    _IfEthMacIndex_Type()
)
ifEthMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacIndex.setStatus("current")
_IfEthMacName_Type = MgmtNameString
_IfEthMacName_Object = MibTableColumn
ifEthMacName = _IfEthMacName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 2),
    _IfEthMacName_Type()
)
ifEthMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacName.setStatus("current")
_IfEthMacConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfEthMacConnIfBasicIfIndex_Object = MibTableColumn
ifEthMacConnIfBasicIfIndex = _IfEthMacConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 3),
    _IfEthMacConnIfBasicIfIndex_Type()
)
ifEthMacConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacConnIfBasicIfIndex.setStatus("current")


class _IfEthMacRxUtilization_Type(Unsigned32WithNA):
    """Custom type ifEthMacRxUtilization based on Unsigned32WithNA"""
    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthMacRxUtilization_Type.__name__ = "Unsigned32WithNA"
_IfEthMacRxUtilization_Object = MibTableColumn
ifEthMacRxUtilization = _IfEthMacRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 4),
    _IfEthMacRxUtilization_Type()
)
ifEthMacRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacRxUtilization.setStatus("current")


class _IfEthMacTxUtilization_Type(Unsigned32WithNA):
    """Custom type ifEthMacTxUtilization based on Unsigned32WithNA"""
    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthMacTxUtilization_Type.__name__ = "Unsigned32WithNA"
_IfEthMacTxUtilization_Object = MibTableColumn
ifEthMacTxUtilization = _IfEthMacTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 5),
    _IfEthMacTxUtilization_Type()
)
ifEthMacTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacTxUtilization.setStatus("current")


class _IfEthMacMaxMtuSize_Type(Unsigned32WithNA):
    """Custom type ifEthMacMaxMtuSize based on Unsigned32WithNA"""
    defaultValue = 9600

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthMacMaxMtuSize_Type.__name__ = "Unsigned32WithNA"
_IfEthMacMaxMtuSize_Object = MibTableColumn
ifEthMacMaxMtuSize = _IfEthMacMaxMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 6),
    _IfEthMacMaxMtuSize_Type()
)
ifEthMacMaxMtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacMaxMtuSize.setStatus("current")


class _IfEthMacInterPacketGap_Type(Unsigned32WithNA):
    """Custom type ifEthMacInterPacketGap based on Unsigned32WithNA"""
    defaultValue = 96

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 456),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfEthMacInterPacketGap_Type.__name__ = "Unsigned32WithNA"
_IfEthMacInterPacketGap_Object = MibTableColumn
ifEthMacInterPacketGap = _IfEthMacInterPacketGap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 7),
    _IfEthMacInterPacketGap_Type()
)
ifEthMacInterPacketGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacInterPacketGap.setStatus("current")


class _IfEthMacFlowControlMode_Type(FlowControlMode):
    """Custom type ifEthMacFlowControlMode based on FlowControlMode"""
    defaultValue = 1


_IfEthMacFlowControlMode_Type.__name__ = "FlowControlMode"
_IfEthMacFlowControlMode_Object = MibTableColumn
ifEthMacFlowControlMode = _IfEthMacFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 8),
    _IfEthMacFlowControlMode_Type()
)
ifEthMacFlowControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacFlowControlMode.setStatus("current")
_IfEthMacTxSignalStatus_Type = SignalStatusWithNA
_IfEthMacTxSignalStatus_Object = MibTableColumn
ifEthMacTxSignalStatus = _IfEthMacTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 9),
    _IfEthMacTxSignalStatus_Type()
)
ifEthMacTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacTxSignalStatus.setStatus("current")
_IfEthMacRxSignalStatus_Type = SignalStatusWithNA
_IfEthMacRxSignalStatus_Object = MibTableColumn
ifEthMacRxSignalStatus = _IfEthMacRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 3, 1, 1, 10),
    _IfEthMacRxSignalStatus_Type()
)
ifEthMacRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthMacRxSignalStatus.setStatus("current")
_IfEthRsFecList_ObjectIdentity = ObjectIdentity
ifEthRsFecList = _IfEthRsFecList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4)
)
_IfEthRsFecTable_Object = MibTable
ifEthRsFecTable = _IfEthRsFecTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifEthRsFecTable.setStatus("current")
_IfEthRsFecEntry_Object = MibTableRow
ifEthRsFecEntry = _IfEthRsFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1)
)
ifEthRsFecEntry.setIndexNames(
    (0, "LUM-IFETH-MIB", "ifEthRsFecIndex"),
)
if mibBuilder.loadTexts:
    ifEthRsFecEntry.setStatus("current")
_IfEthRsFecIndex_Type = Unsigned32
_IfEthRsFecIndex_Object = MibTableColumn
ifEthRsFecIndex = _IfEthRsFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 1),
    _IfEthRsFecIndex_Type()
)
ifEthRsFecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthRsFecIndex.setStatus("current")
_IfEthRsFecName_Type = MgmtNameString
_IfEthRsFecName_Object = MibTableColumn
ifEthRsFecName = _IfEthRsFecName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 2),
    _IfEthRsFecName_Type()
)
ifEthRsFecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifEthRsFecName.setStatus("current")
_IfEthRsFecConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfEthRsFecConnIfBasicIfIndex_Object = MibTableColumn
ifEthRsFecConnIfBasicIfIndex = _IfEthRsFecConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 3),
    _IfEthRsFecConnIfBasicIfIndex_Type()
)
ifEthRsFecConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifEthRsFecConnIfBasicIfIndex.setStatus("current")
_IfEthRsFecTxSignalStatus_Type = SignalStatusWithNA
_IfEthRsFecTxSignalStatus_Object = MibTableColumn
ifEthRsFecTxSignalStatus = _IfEthRsFecTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 4),
    _IfEthRsFecTxSignalStatus_Type()
)
ifEthRsFecTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthRsFecTxSignalStatus.setStatus("current")
_IfEthRsFecRxSignalStatus_Type = SignalStatusWithNA
_IfEthRsFecRxSignalStatus_Object = MibTableColumn
ifEthRsFecRxSignalStatus = _IfEthRsFecRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 5),
    _IfEthRsFecRxSignalStatus_Type()
)
ifEthRsFecRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthRsFecRxSignalStatus.setStatus("current")


class _IfEthRsFecMode_Type(RsFecMode):
    """Custom type ifEthRsFecMode based on RsFecMode"""
    defaultValue = 2


_IfEthRsFecMode_Type.__name__ = "RsFecMode"
_IfEthRsFecMode_Object = MibTableColumn
ifEthRsFecMode = _IfEthRsFecMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 6),
    _IfEthRsFecMode_Type()
)
ifEthRsFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifEthRsFecMode.setStatus("current")


class _IfEthRsFecActualRsFec_Type(RsFecOnOff):
    """Custom type ifEthRsFecActualRsFec based on RsFecOnOff"""
    defaultValue = 2


_IfEthRsFecActualRsFec_Type.__name__ = "RsFecOnOff"
_IfEthRsFecActualRsFec_Object = MibTableColumn
ifEthRsFecActualRsFec = _IfEthRsFecActualRsFec_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 7),
    _IfEthRsFecActualRsFec_Type()
)
ifEthRsFecActualRsFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthRsFecActualRsFec.setStatus("current")
_IfEthRsFecLanesAlignmentError_Type = FaultStatusWithNA
_IfEthRsFecLanesAlignmentError_Object = MibTableColumn
ifEthRsFecLanesAlignmentError = _IfEthRsFecLanesAlignmentError_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 2, 4, 1, 1, 8),
    _IfEthRsFecLanesAlignmentError_Type()
)
ifEthRsFecLanesAlignmentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEthRsFecLanesAlignmentError.setStatus("current")

# Managed Objects groups

ifEthGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 1)
)
ifEthGeneralGroupV1.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralStateLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalTableSize"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalStateLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacTableSize"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifEthGeneralGroupV1.setStatus("deprecated")

ifEthPhysicalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 2)
)
ifEthPhysicalGroupV1.setObjects(
      *(("LUM-IFETH-MIB", "ifEthPhysicalIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalName"),
        ("LUM-IFETH-MIB", "ifEthPhysicalConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationMode"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRemoteLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLinkDown"),
        ("LUM-IFETH-MIB", "ifEthPhysicalHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalPcsLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifEthPhysicalGroupV1.setStatus("deprecated")

ifEthMacGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 3)
)
ifEthMacGroupV1.setObjects(
      *(("LUM-IFETH-MIB", "ifEthMacIndex"),
        ("LUM-IFETH-MIB", "ifEthMacName"),
        ("LUM-IFETH-MIB", "ifEthMacConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthMacRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthMacTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthMacMaxMtuSize"),
        ("LUM-IFETH-MIB", "ifEthMacInterPacketGap"),
        ("LUM-IFETH-MIB", "ifEthMacFlowControlMode"),
        ("LUM-IFETH-MIB", "ifEthMacTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthMacRxSignalStatus"))
)
if mibBuilder.loadTexts:
    ifEthMacGroupV1.setStatus("current")

ifEthPhysicalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 4)
)
ifEthPhysicalGroupV2.setObjects(
      *(("LUM-IFETH-MIB", "ifEthPhysicalIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalName"),
        ("LUM-IFETH-MIB", "ifEthPhysicalConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationMode"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRemoteLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLinkDown"),
        ("LUM-IFETH-MIB", "ifEthPhysicalHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalPcsLossOfFrame"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxLocalLinkFault"))
)
if mibBuilder.loadTexts:
    ifEthPhysicalGroupV2.setStatus("deprecated")

ifEthPhysicalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 5)
)
ifEthPhysicalGroupV3.setObjects(
      *(("LUM-IFETH-MIB", "ifEthPhysicalIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalName"),
        ("LUM-IFETH-MIB", "ifEthPhysicalConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationMode"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRemoteLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLinkDown"),
        ("LUM-IFETH-MIB", "ifEthPhysicalHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalPcsLossOfFrame"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxHighBitErrorRate"))
)
if mibBuilder.loadTexts:
    ifEthPhysicalGroupV3.setStatus("deprecated")

ifEthPhysicalGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 6)
)
ifEthPhysicalGroupV4.setObjects(
      *(("LUM-IFETH-MIB", "ifEthPhysicalIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalName"),
        ("LUM-IFETH-MIB", "ifEthPhysicalConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationMode"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRemoteLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLinkDown"),
        ("LUM-IFETH-MIB", "ifEthPhysicalHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalPcsLossOfFrame"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxPcsLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifEthPhysicalGroupV4.setStatus("deprecated")

ifEthPhysicalGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 7)
)
ifEthPhysicalGroupV5.setObjects(
      *(("LUM-IFETH-MIB", "ifEthPhysicalIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalName"),
        ("LUM-IFETH-MIB", "ifEthPhysicalConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationMode"),
        ("LUM-IFETH-MIB", "ifEthPhysicalAutoNegotiationStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxUtilization"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRemoteLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalLinkDown"),
        ("LUM-IFETH-MIB", "ifEthPhysicalHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalPcsLossOfFrame"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxLocalLinkFault"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxHighBitErrorRate"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxPcsLossOfFrame"),
        ("LUM-IFETH-MIB", "ifEthPhysicalUId"),
        ("LUM-IFETH-MIB", "ifEthPhysicalRxPcsLossOfSync"),
        ("LUM-IFETH-MIB", "ifEthPhysicalTxPcsLossOfSync"))
)
if mibBuilder.loadTexts:
    ifEthPhysicalGroupV5.setStatus("current")

ifEthRsFecGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 8)
)
ifEthRsFecGroupV1.setObjects(
      *(("LUM-IFETH-MIB", "ifEthRsFecIndex"),
        ("LUM-IFETH-MIB", "ifEthRsFecName"),
        ("LUM-IFETH-MIB", "ifEthRsFecConnIfBasicIfIndex"),
        ("LUM-IFETH-MIB", "ifEthRsFecTxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthRsFecRxSignalStatus"),
        ("LUM-IFETH-MIB", "ifEthRsFecMode"),
        ("LUM-IFETH-MIB", "ifEthRsFecActualRsFec"),
        ("LUM-IFETH-MIB", "ifEthRsFecLanesAlignmentError"))
)
if mibBuilder.loadTexts:
    ifEthRsFecGroupV1.setStatus("current")

ifEthGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 1, 9)
)
ifEthGeneralGroupV2.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralStateLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalTableSize"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthPhysicalStateLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacTableSize"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthMacStateLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthRsFecTableSize"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthRsFecConfigLastChangeTime"),
        ("LUM-IFETH-MIB", "ifEthGeneralIfEthRsFecStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifEthGeneralGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfEthComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 1)
)
lumIfEthComplV1.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV1"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV1.setStatus(
        "deprecated"
    )

lumIfEthComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 2)
)
lumIfEthComplV2.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV2"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV2.setStatus(
        "deprecated"
    )

lumIfEthComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 3)
)
lumIfEthComplV3.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV3"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV3.setStatus(
        "deprecated"
    )

lumIfEthComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 4)
)
lumIfEthComplV4.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV4"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV4.setStatus(
        "deprecated"
    )

lumIfEthComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 5)
)
lumIfEthComplV5.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV5"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV5.setStatus(
        "deprecated"
    )

lumIfEthComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 6)
)
lumIfEthComplV6.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV1"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV5"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"),
        ("LUM-IFETH-MIB", "ifEthRsFecGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV6.setStatus(
        "deprecated"
    )

lumIfEthComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 54, 1, 2, 7)
)
lumIfEthComplV7.setObjects(
      *(("LUM-IFETH-MIB", "ifEthGeneralGroupV2"),
        ("LUM-IFETH-MIB", "ifEthPhysicalGroupV5"),
        ("LUM-IFETH-MIB", "ifEthMacGroupV1"),
        ("LUM-IFETH-MIB", "ifEthRsFecGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfEthComplV7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFETH-MIB",
    **{"lumIfEthMIBModule": lumIfEthMIBModule,
       "lumIfEthConfs": lumIfEthConfs,
       "lumIfEthGroups": lumIfEthGroups,
       "ifEthGeneralGroupV1": ifEthGeneralGroupV1,
       "ifEthPhysicalGroupV1": ifEthPhysicalGroupV1,
       "ifEthMacGroupV1": ifEthMacGroupV1,
       "ifEthPhysicalGroupV2": ifEthPhysicalGroupV2,
       "ifEthPhysicalGroupV3": ifEthPhysicalGroupV3,
       "ifEthPhysicalGroupV4": ifEthPhysicalGroupV4,
       "ifEthPhysicalGroupV5": ifEthPhysicalGroupV5,
       "ifEthRsFecGroupV1": ifEthRsFecGroupV1,
       "ifEthGeneralGroupV2": ifEthGeneralGroupV2,
       "lumIfEthCompl": lumIfEthCompl,
       "lumIfEthComplV1": lumIfEthComplV1,
       "lumIfEthComplV2": lumIfEthComplV2,
       "lumIfEthComplV3": lumIfEthComplV3,
       "lumIfEthComplV4": lumIfEthComplV4,
       "lumIfEthComplV5": lumIfEthComplV5,
       "lumIfEthComplV6": lumIfEthComplV6,
       "lumIfEthComplV7": lumIfEthComplV7,
       "lumIfEthMIBObjects": lumIfEthMIBObjects,
       "ifEthGeneral": ifEthGeneral,
       "ifEthGeneralConfigLastChangeTime": ifEthGeneralConfigLastChangeTime,
       "ifEthGeneralStateLastChangeTime": ifEthGeneralStateLastChangeTime,
       "ifEthGeneralIfEthPhysicalTableSize": ifEthGeneralIfEthPhysicalTableSize,
       "ifEthGeneralIfEthPhysicalConfigLastChangeTime": ifEthGeneralIfEthPhysicalConfigLastChangeTime,
       "ifEthGeneralIfEthPhysicalStateLastChangeTime": ifEthGeneralIfEthPhysicalStateLastChangeTime,
       "ifEthGeneralIfEthMacTableSize": ifEthGeneralIfEthMacTableSize,
       "ifEthGeneralIfEthMacConfigLastChangeTime": ifEthGeneralIfEthMacConfigLastChangeTime,
       "ifEthGeneralIfEthMacStateLastChangeTime": ifEthGeneralIfEthMacStateLastChangeTime,
       "ifEthGeneralIfEthRsFecTableSize": ifEthGeneralIfEthRsFecTableSize,
       "ifEthGeneralIfEthRsFecConfigLastChangeTime": ifEthGeneralIfEthRsFecConfigLastChangeTime,
       "ifEthGeneralIfEthRsFecStateLastChangeTime": ifEthGeneralIfEthRsFecStateLastChangeTime,
       "ifEthPhysicalList": ifEthPhysicalList,
       "ifEthPhysicalTable": ifEthPhysicalTable,
       "ifEthPhysicalEntry": ifEthPhysicalEntry,
       "ifEthPhysicalIndex": ifEthPhysicalIndex,
       "ifEthPhysicalName": ifEthPhysicalName,
       "ifEthPhysicalConnIfBasicIfIndex": ifEthPhysicalConnIfBasicIfIndex,
       "ifEthPhysicalAutoNegotiationMode": ifEthPhysicalAutoNegotiationMode,
       "ifEthPhysicalAutoNegotiationStatus": ifEthPhysicalAutoNegotiationStatus,
       "ifEthPhysicalRxUtilization": ifEthPhysicalRxUtilization,
       "ifEthPhysicalTxUtilization": ifEthPhysicalTxUtilization,
       "ifEthPhysicalTxSignalStatus": ifEthPhysicalTxSignalStatus,
       "ifEthPhysicalRxSignalStatus": ifEthPhysicalRxSignalStatus,
       "ifEthPhysicalRemoteLinkFault": ifEthPhysicalRemoteLinkFault,
       "ifEthPhysicalLocalLinkFault": ifEthPhysicalLocalLinkFault,
       "ifEthPhysicalLinkDown": ifEthPhysicalLinkDown,
       "ifEthPhysicalHighBitErrorRate": ifEthPhysicalHighBitErrorRate,
       "ifEthPhysicalPcsLossOfFrame": ifEthPhysicalPcsLossOfFrame,
       "ifEthPhysicalRxLocalLinkFault": ifEthPhysicalRxLocalLinkFault,
       "ifEthPhysicalTxLocalLinkFault": ifEthPhysicalTxLocalLinkFault,
       "ifEthPhysicalRxHighBitErrorRate": ifEthPhysicalRxHighBitErrorRate,
       "ifEthPhysicalTxHighBitErrorRate": ifEthPhysicalTxHighBitErrorRate,
       "ifEthPhysicalTxPcsLossOfFrame": ifEthPhysicalTxPcsLossOfFrame,
       "ifEthPhysicalUId": ifEthPhysicalUId,
       "ifEthPhysicalRxPcsLossOfSync": ifEthPhysicalRxPcsLossOfSync,
       "ifEthPhysicalTxPcsLossOfSync": ifEthPhysicalTxPcsLossOfSync,
       "ifEthMacList": ifEthMacList,
       "ifEthMacTable": ifEthMacTable,
       "ifEthMacEntry": ifEthMacEntry,
       "ifEthMacIndex": ifEthMacIndex,
       "ifEthMacName": ifEthMacName,
       "ifEthMacConnIfBasicIfIndex": ifEthMacConnIfBasicIfIndex,
       "ifEthMacRxUtilization": ifEthMacRxUtilization,
       "ifEthMacTxUtilization": ifEthMacTxUtilization,
       "ifEthMacMaxMtuSize": ifEthMacMaxMtuSize,
       "ifEthMacInterPacketGap": ifEthMacInterPacketGap,
       "ifEthMacFlowControlMode": ifEthMacFlowControlMode,
       "ifEthMacTxSignalStatus": ifEthMacTxSignalStatus,
       "ifEthMacRxSignalStatus": ifEthMacRxSignalStatus,
       "ifEthRsFecList": ifEthRsFecList,
       "ifEthRsFecTable": ifEthRsFecTable,
       "ifEthRsFecEntry": ifEthRsFecEntry,
       "ifEthRsFecIndex": ifEthRsFecIndex,
       "ifEthRsFecName": ifEthRsFecName,
       "ifEthRsFecConnIfBasicIfIndex": ifEthRsFecConnIfBasicIfIndex,
       "ifEthRsFecTxSignalStatus": ifEthRsFecTxSignalStatus,
       "ifEthRsFecRxSignalStatus": ifEthRsFecRxSignalStatus,
       "ifEthRsFecMode": ifEthRsFecMode,
       "ifEthRsFecActualRsFec": ifEthRsFecActualRsFec,
       "ifEthRsFecLanesAlignmentError": ifEthRsFecLanesAlignmentError}
)
