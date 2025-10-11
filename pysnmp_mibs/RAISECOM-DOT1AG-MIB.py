# SNMP MIB module (RAISECOM-DOT1AG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-DOT1AG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:38 2025
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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmCcmInterval,
 Dot1agCfmConfigErrors,
 Dot1agCfmEgressActionFieldValue,
 Dot1agCfmFngState,
 Dot1agCfmHighestDefectPri,
 Dot1agCfmIdPermission,
 Dot1agCfmIngressActionFieldValue,
 Dot1agCfmInterfaceStatus,
 Dot1agCfmLowestAlarmPri,
 Dot1agCfmMDLevel,
 Dot1agCfmMDLevelOrNone,
 Dot1agCfmMaintAssocName,
 Dot1agCfmMaintAssocNameType,
 Dot1agCfmMaintDomainName,
 Dot1agCfmMaintDomainNameType,
 Dot1agCfmMepDefects,
 Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMhfCreation,
 Dot1agCfmMpDirection,
 Dot1agCfmPbbComponentIdentifier,
 Dot1agCfmPortStatus,
 Dot1agCfmRelayActionFieldValue,
 Dot1agCfmRemoteMepState,
 dot1agCfmMepHighestPrDefect) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmConfigErrors",
    "Dot1agCfmEgressActionFieldValue",
    "Dot1agCfmFngState",
    "Dot1agCfmHighestDefectPri",
    "Dot1agCfmIdPermission",
    "Dot1agCfmIngressActionFieldValue",
    "Dot1agCfmInterfaceStatus",
    "Dot1agCfmLowestAlarmPri",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintAssocNameType",
    "Dot1agCfmMaintDomainName",
    "Dot1agCfmMaintDomainNameType",
    "Dot1agCfmMepDefects",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMhfCreation",
    "Dot1agCfmMpDirection",
    "Dot1agCfmPbbComponentIdentifier",
    "Dot1agCfmPortStatus",
    "Dot1agCfmRelayActionFieldValue",
    "Dot1agCfmRemoteMepState",
    "dot1agCfmMepHighestPrDefect")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rcDot1ag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32)
)
if mibBuilder.loadTexts:
    rcDot1ag.setRevisions(
        ("2007-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDot1agNotifications_ObjectIdentity = ObjectIdentity
rcDot1agNotifications = _RcDot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 0)
)
_RcDot1agMIBObjects_ObjectIdentity = ObjectIdentity
rcDot1agMIBObjects = _RcDot1agMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1)
)
_RcDot1agCfmStack_ObjectIdentity = ObjectIdentity
rcDot1agCfmStack = _RcDot1agCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1)
)
_RcDot1agCfmStackTable_Object = MibTable
rcDot1agCfmStackTable = _RcDot1agCfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcDot1agCfmStackTable.setStatus("current")
_RcDot1agCfmStackEntry_Object = MibTableRow
rcDot1agCfmStackEntry = _RcDot1agCfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1)
)
rcDot1agCfmStackEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackifIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackVlanIdOrNone"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackMdLevel"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackDirection"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmStackEntry.setStatus("current")
_RcDot1agCfmStackifIndex_Type = InterfaceIndex
_RcDot1agCfmStackifIndex_Object = MibTableColumn
rcDot1agCfmStackifIndex = _RcDot1agCfmStackifIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 1),
    _RcDot1agCfmStackifIndex_Type()
)
rcDot1agCfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmStackifIndex.setStatus("current")
_RcDot1agCfmStackVlanIdOrNone_Type = VlanIdOrNone
_RcDot1agCfmStackVlanIdOrNone_Object = MibTableColumn
rcDot1agCfmStackVlanIdOrNone = _RcDot1agCfmStackVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 2),
    _RcDot1agCfmStackVlanIdOrNone_Type()
)
rcDot1agCfmStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmStackVlanIdOrNone.setStatus("current")
_RcDot1agCfmStackMdLevel_Type = Dot1agCfmMDLevel
_RcDot1agCfmStackMdLevel_Object = MibTableColumn
rcDot1agCfmStackMdLevel = _RcDot1agCfmStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 3),
    _RcDot1agCfmStackMdLevel_Type()
)
rcDot1agCfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmStackMdLevel.setStatus("current")
_RcDot1agCfmStackDirection_Type = Dot1agCfmMpDirection
_RcDot1agCfmStackDirection_Object = MibTableColumn
rcDot1agCfmStackDirection = _RcDot1agCfmStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 4),
    _RcDot1agCfmStackDirection_Type()
)
rcDot1agCfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmStackDirection.setStatus("current")
_RcDot1agCfmStackMdIndex_Type = Unsigned32
_RcDot1agCfmStackMdIndex_Object = MibTableColumn
rcDot1agCfmStackMdIndex = _RcDot1agCfmStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 5),
    _RcDot1agCfmStackMdIndex_Type()
)
rcDot1agCfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmStackMdIndex.setStatus("current")
_RcDot1agCfmStackMaIndex_Type = Unsigned32
_RcDot1agCfmStackMaIndex_Object = MibTableColumn
rcDot1agCfmStackMaIndex = _RcDot1agCfmStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 6),
    _RcDot1agCfmStackMaIndex_Type()
)
rcDot1agCfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmStackMaIndex.setStatus("current")
_RcDot1agCfmStackMepId_Type = Dot1agCfmMepIdOrZero
_RcDot1agCfmStackMepId_Object = MibTableColumn
rcDot1agCfmStackMepId = _RcDot1agCfmStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 7),
    _RcDot1agCfmStackMepId_Type()
)
rcDot1agCfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmStackMepId.setStatus("current")
_RcDot1agCfmStackMacAddress_Type = MacAddress
_RcDot1agCfmStackMacAddress_Object = MibTableColumn
rcDot1agCfmStackMacAddress = _RcDot1agCfmStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 1, 1, 1, 8),
    _RcDot1agCfmStackMacAddress_Type()
)
rcDot1agCfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmStackMacAddress.setStatus("current")
_RcDot1agCfmDefaultMd_ObjectIdentity = ObjectIdentity
rcDot1agCfmDefaultMd = _RcDot1agCfmDefaultMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2)
)


class _RcDot1agCfmDefaultMdDefLevel_Type(Dot1agCfmMDLevel):
    """Custom type rcDot1agCfmDefaultMdDefLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_RcDot1agCfmDefaultMdDefLevel_Type.__name__ = "Dot1agCfmMDLevel"
_RcDot1agCfmDefaultMdDefLevel_Object = MibScalar
rcDot1agCfmDefaultMdDefLevel = _RcDot1agCfmDefaultMdDefLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 1),
    _RcDot1agCfmDefaultMdDefLevel_Type()
)
rcDot1agCfmDefaultMdDefLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdDefLevel.setStatus("current")


class _RcDot1agCfmDefaultMdDefMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type rcDot1agCfmDefaultMdDefMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 1


_RcDot1agCfmDefaultMdDefMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_RcDot1agCfmDefaultMdDefMhfCreation_Object = MibScalar
rcDot1agCfmDefaultMdDefMhfCreation = _RcDot1agCfmDefaultMdDefMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 2),
    _RcDot1agCfmDefaultMdDefMhfCreation_Type()
)
rcDot1agCfmDefaultMdDefMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdDefMhfCreation.setStatus("current")


class _RcDot1agCfmDefaultMdDefIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type rcDot1agCfmDefaultMdDefIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1


_RcDot1agCfmDefaultMdDefIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_RcDot1agCfmDefaultMdDefIdPermission_Object = MibScalar
rcDot1agCfmDefaultMdDefIdPermission = _RcDot1agCfmDefaultMdDefIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 3),
    _RcDot1agCfmDefaultMdDefIdPermission_Type()
)
rcDot1agCfmDefaultMdDefIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdDefIdPermission.setStatus("current")
_RcDot1agCfmDefaultMdTable_Object = MibTable
rcDot1agCfmDefaultMdTable = _RcDot1agCfmDefaultMdTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdTable.setStatus("current")
_RcDot1agCfmDefaultMdEntry_Object = MibTableRow
rcDot1agCfmDefaultMdEntry = _RcDot1agCfmDefaultMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1)
)
rcDot1agCfmDefaultMdEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdComponentId"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdPrimaryVid"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdEntry.setStatus("current")
_RcDot1agCfmDefaultMdComponentId_Type = Dot1agCfmPbbComponentIdentifier
_RcDot1agCfmDefaultMdComponentId_Object = MibTableColumn
rcDot1agCfmDefaultMdComponentId = _RcDot1agCfmDefaultMdComponentId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 1),
    _RcDot1agCfmDefaultMdComponentId_Type()
)
rcDot1agCfmDefaultMdComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdComponentId.setStatus("current")
_RcDot1agCfmDefaultMdPrimaryVid_Type = VlanId
_RcDot1agCfmDefaultMdPrimaryVid_Object = MibTableColumn
rcDot1agCfmDefaultMdPrimaryVid = _RcDot1agCfmDefaultMdPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 2),
    _RcDot1agCfmDefaultMdPrimaryVid_Type()
)
rcDot1agCfmDefaultMdPrimaryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdPrimaryVid.setStatus("current")
_RcDot1agCfmDefaultMdStatus_Type = TruthValue
_RcDot1agCfmDefaultMdStatus_Object = MibTableColumn
rcDot1agCfmDefaultMdStatus = _RcDot1agCfmDefaultMdStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 3),
    _RcDot1agCfmDefaultMdStatus_Type()
)
rcDot1agCfmDefaultMdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdStatus.setStatus("current")


class _RcDot1agCfmDefaultMdLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type rcDot1agCfmDefaultMdLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_RcDot1agCfmDefaultMdLevel_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_RcDot1agCfmDefaultMdLevel_Object = MibTableColumn
rcDot1agCfmDefaultMdLevel = _RcDot1agCfmDefaultMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 4),
    _RcDot1agCfmDefaultMdLevel_Type()
)
rcDot1agCfmDefaultMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdLevel.setStatus("current")


class _RcDot1agCfmDefaultMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type rcDot1agCfmDefaultMdMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 4


_RcDot1agCfmDefaultMdMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_RcDot1agCfmDefaultMdMhfCreation_Object = MibTableColumn
rcDot1agCfmDefaultMdMhfCreation = _RcDot1agCfmDefaultMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 5),
    _RcDot1agCfmDefaultMdMhfCreation_Type()
)
rcDot1agCfmDefaultMdMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdMhfCreation.setStatus("current")


class _RcDot1agCfmDefaultMdIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type rcDot1agCfmDefaultMdIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 5


_RcDot1agCfmDefaultMdIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_RcDot1agCfmDefaultMdIdPermission_Object = MibTableColumn
rcDot1agCfmDefaultMdIdPermission = _RcDot1agCfmDefaultMdIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 2, 4, 1, 6),
    _RcDot1agCfmDefaultMdIdPermission_Type()
)
rcDot1agCfmDefaultMdIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdIdPermission.setStatus("current")
_RcDot1agCfmVlan_ObjectIdentity = ObjectIdentity
rcDot1agCfmVlan = _RcDot1agCfmVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3)
)
_RcDot1agCfmVlanTable_Object = MibTable
rcDot1agCfmVlanTable = _RcDot1agCfmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rcDot1agCfmVlanTable.setStatus("current")
_RcDot1agCfmVlanEntry_Object = MibTableRow
rcDot1agCfmVlanEntry = _RcDot1agCfmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1, 1)
)
rcDot1agCfmVlanEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmVlanComponentId"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmVlanVid"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmVlanEntry.setStatus("current")
_RcDot1agCfmVlanComponentId_Type = Dot1agCfmPbbComponentIdentifier
_RcDot1agCfmVlanComponentId_Object = MibTableColumn
rcDot1agCfmVlanComponentId = _RcDot1agCfmVlanComponentId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1, 1, 1),
    _RcDot1agCfmVlanComponentId_Type()
)
rcDot1agCfmVlanComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmVlanComponentId.setStatus("current")
_RcDot1agCfmVlanVid_Type = VlanId
_RcDot1agCfmVlanVid_Object = MibTableColumn
rcDot1agCfmVlanVid = _RcDot1agCfmVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1, 1, 2),
    _RcDot1agCfmVlanVid_Type()
)
rcDot1agCfmVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmVlanVid.setStatus("current")
_RcDot1agCfmVlanPrimaryVid_Type = VlanId
_RcDot1agCfmVlanPrimaryVid_Object = MibTableColumn
rcDot1agCfmVlanPrimaryVid = _RcDot1agCfmVlanPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1, 1, 3),
    _RcDot1agCfmVlanPrimaryVid_Type()
)
rcDot1agCfmVlanPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmVlanPrimaryVid.setStatus("current")
_RcDot1agCfmVlanRowStatus_Type = RowStatus
_RcDot1agCfmVlanRowStatus_Object = MibTableColumn
rcDot1agCfmVlanRowStatus = _RcDot1agCfmVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 3, 1, 1, 4),
    _RcDot1agCfmVlanRowStatus_Type()
)
rcDot1agCfmVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmVlanRowStatus.setStatus("current")
_RcDot1agCfmConfigErrorList_ObjectIdentity = ObjectIdentity
rcDot1agCfmConfigErrorList = _RcDot1agCfmConfigErrorList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4)
)
_RcDot1agCfmConfigErrorListTable_Object = MibTable
rcDot1agCfmConfigErrorListTable = _RcDot1agCfmConfigErrorListTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListTable.setStatus("current")
_RcDot1agCfmConfigErrorListEntry_Object = MibTableRow
rcDot1agCfmConfigErrorListEntry = _RcDot1agCfmConfigErrorListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4, 1, 1)
)
rcDot1agCfmConfigErrorListEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmConfigErrorListVid"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListEntry.setStatus("current")
_RcDot1agCfmConfigErrorListVid_Type = VlanId
_RcDot1agCfmConfigErrorListVid_Object = MibTableColumn
rcDot1agCfmConfigErrorListVid = _RcDot1agCfmConfigErrorListVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4, 1, 1, 1),
    _RcDot1agCfmConfigErrorListVid_Type()
)
rcDot1agCfmConfigErrorListVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListVid.setStatus("current")
_RcDot1agCfmConfigErrorListIfIndex_Type = InterfaceIndex
_RcDot1agCfmConfigErrorListIfIndex_Object = MibTableColumn
rcDot1agCfmConfigErrorListIfIndex = _RcDot1agCfmConfigErrorListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4, 1, 1, 2),
    _RcDot1agCfmConfigErrorListIfIndex_Type()
)
rcDot1agCfmConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListIfIndex.setStatus("current")
_RcDot1agCfmConfigErrorListErrorType_Type = Dot1agCfmConfigErrors
_RcDot1agCfmConfigErrorListErrorType_Object = MibTableColumn
rcDot1agCfmConfigErrorListErrorType = _RcDot1agCfmConfigErrorListErrorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 4, 1, 1, 3),
    _RcDot1agCfmConfigErrorListErrorType_Type()
)
rcDot1agCfmConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListErrorType.setStatus("current")
_RcDot1agCfmMd_ObjectIdentity = ObjectIdentity
rcDot1agCfmMd = _RcDot1agCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5)
)
_RcDot1agCfmMdTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_RcDot1agCfmMdTableNextIndex_Object = MibScalar
rcDot1agCfmMdTableNextIndex = _RcDot1agCfmMdTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 1),
    _RcDot1agCfmMdTableNextIndex_Type()
)
rcDot1agCfmMdTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMdTableNextIndex.setStatus("current")
_RcDot1agCfmMdTable_Object = MibTable
rcDot1agCfmMdTable = _RcDot1agCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMdTable.setStatus("current")
_RcDot1agCfmMdEntry_Object = MibTableRow
rcDot1agCfmMdEntry = _RcDot1agCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1)
)
rcDot1agCfmMdEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMdEntry.setStatus("current")


class _RcDot1agCfmMdIndex_Type(Unsigned32):
    """Custom type rcDot1agCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RcDot1agCfmMdIndex_Type.__name__ = "Unsigned32"
_RcDot1agCfmMdIndex_Object = MibTableColumn
rcDot1agCfmMdIndex = _RcDot1agCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 1),
    _RcDot1agCfmMdIndex_Type()
)
rcDot1agCfmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMdIndex.setStatus("current")


class _RcDot1agCfmMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type rcDot1agCfmMdFormat based on Dot1agCfmMaintDomainNameType"""
    defaultValue = 4


_RcDot1agCfmMdFormat_Type.__name__ = "Dot1agCfmMaintDomainNameType"
_RcDot1agCfmMdFormat_Object = MibTableColumn
rcDot1agCfmMdFormat = _RcDot1agCfmMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 2),
    _RcDot1agCfmMdFormat_Type()
)
rcDot1agCfmMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdFormat.setStatus("current")


class _RcDot1agCfmMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type rcDot1agCfmMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_RcDot1agCfmMdName_Type.__name__ = "Dot1agCfmMaintDomainName"
_RcDot1agCfmMdName_Object = MibTableColumn
rcDot1agCfmMdName = _RcDot1agCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 3),
    _RcDot1agCfmMdName_Type()
)
rcDot1agCfmMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdName.setStatus("current")


class _RcDot1agCfmMdMdLevel_Type(Dot1agCfmMDLevel):
    """Custom type rcDot1agCfmMdMdLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_RcDot1agCfmMdMdLevel_Type.__name__ = "Dot1agCfmMDLevel"
_RcDot1agCfmMdMdLevel_Object = MibTableColumn
rcDot1agCfmMdMdLevel = _RcDot1agCfmMdMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 4),
    _RcDot1agCfmMdMdLevel_Type()
)
rcDot1agCfmMdMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdMdLevel.setStatus("current")


class _RcDot1agCfmMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type rcDot1agCfmMdMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 1


_RcDot1agCfmMdMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_RcDot1agCfmMdMhfCreation_Object = MibTableColumn
rcDot1agCfmMdMhfCreation = _RcDot1agCfmMdMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 5),
    _RcDot1agCfmMdMhfCreation_Type()
)
rcDot1agCfmMdMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdMhfCreation.setStatus("current")


class _RcDot1agCfmMdMhfIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type rcDot1agCfmMdMhfIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1


_RcDot1agCfmMdMhfIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_RcDot1agCfmMdMhfIdPermission_Object = MibTableColumn
rcDot1agCfmMdMhfIdPermission = _RcDot1agCfmMdMhfIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 6),
    _RcDot1agCfmMdMhfIdPermission_Type()
)
rcDot1agCfmMdMhfIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdMhfIdPermission.setStatus("current")
_RcDot1agCfmMdMaNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_RcDot1agCfmMdMaNextIndex_Object = MibTableColumn
rcDot1agCfmMdMaNextIndex = _RcDot1agCfmMdMaNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 7),
    _RcDot1agCfmMdMaNextIndex_Type()
)
rcDot1agCfmMdMaNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMdMaNextIndex.setStatus("current")
_RcDot1agCfmMdRowStatus_Type = RowStatus
_RcDot1agCfmMdRowStatus_Object = MibTableColumn
rcDot1agCfmMdRowStatus = _RcDot1agCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 5, 2, 1, 8),
    _RcDot1agCfmMdRowStatus_Type()
)
rcDot1agCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMdRowStatus.setStatus("current")
_RcDot1agCfmMa_ObjectIdentity = ObjectIdentity
rcDot1agCfmMa = _RcDot1agCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6)
)
_RcDot1agCfmMaNetTable_Object = MibTable
rcDot1agCfmMaNetTable = _RcDot1agCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetTable.setStatus("current")
_RcDot1agCfmMaNetEntry_Object = MibTableRow
rcDot1agCfmMaNetEntry = _RcDot1agCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1)
)
rcDot1agCfmMaNetEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetEntry.setStatus("current")


class _RcDot1agCfmMaIndex_Type(Unsigned32):
    """Custom type rcDot1agCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RcDot1agCfmMaIndex_Type.__name__ = "Unsigned32"
_RcDot1agCfmMaIndex_Object = MibTableColumn
rcDot1agCfmMaIndex = _RcDot1agCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1, 1),
    _RcDot1agCfmMaIndex_Type()
)
rcDot1agCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMaIndex.setStatus("current")
_RcDot1agCfmMaNetFormat_Type = Dot1agCfmMaintAssocNameType
_RcDot1agCfmMaNetFormat_Object = MibTableColumn
rcDot1agCfmMaNetFormat = _RcDot1agCfmMaNetFormat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1, 2),
    _RcDot1agCfmMaNetFormat_Type()
)
rcDot1agCfmMaNetFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetFormat.setStatus("current")
_RcDot1agCfmMaNetName_Type = Dot1agCfmMaintAssocName
_RcDot1agCfmMaNetName_Object = MibTableColumn
rcDot1agCfmMaNetName = _RcDot1agCfmMaNetName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1, 3),
    _RcDot1agCfmMaNetName_Type()
)
rcDot1agCfmMaNetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetName.setStatus("current")


class _RcDot1agCfmMaNetCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type rcDot1agCfmMaNetCcmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_RcDot1agCfmMaNetCcmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_RcDot1agCfmMaNetCcmInterval_Object = MibTableColumn
rcDot1agCfmMaNetCcmInterval = _RcDot1agCfmMaNetCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1, 4),
    _RcDot1agCfmMaNetCcmInterval_Type()
)
rcDot1agCfmMaNetCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetCcmInterval.setStatus("current")
_RcDot1agCfmMaNetRowStatus_Type = RowStatus
_RcDot1agCfmMaNetRowStatus_Object = MibTableColumn
rcDot1agCfmMaNetRowStatus = _RcDot1agCfmMaNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 1, 1, 5),
    _RcDot1agCfmMaNetRowStatus_Type()
)
rcDot1agCfmMaNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaNetRowStatus.setStatus("current")
_RcDot1agCfmMaCompTable_Object = MibTable
rcDot1agCfmMaCompTable = _RcDot1agCfmMaCompTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompTable.setStatus("current")
_RcDot1agCfmMaCompEntry_Object = MibTableRow
rcDot1agCfmMaCompEntry = _RcDot1agCfmMaCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1)
)
rcDot1agCfmMaCompEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaComponentId"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompEntry.setStatus("current")
_RcDot1agCfmMaComponentId_Type = Dot1agCfmPbbComponentIdentifier
_RcDot1agCfmMaComponentId_Object = MibTableColumn
rcDot1agCfmMaComponentId = _RcDot1agCfmMaComponentId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 1),
    _RcDot1agCfmMaComponentId_Type()
)
rcDot1agCfmMaComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMaComponentId.setStatus("current")
_RcDot1agCfmMaCompPrimaryVlanId_Type = VlanIdOrNone
_RcDot1agCfmMaCompPrimaryVlanId_Object = MibTableColumn
rcDot1agCfmMaCompPrimaryVlanId = _RcDot1agCfmMaCompPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 2),
    _RcDot1agCfmMaCompPrimaryVlanId_Type()
)
rcDot1agCfmMaCompPrimaryVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompPrimaryVlanId.setStatus("current")


class _RcDot1agCfmMaCompMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type rcDot1agCfmMaCompMhfCreation based on Dot1agCfmMhfCreation"""
    defaultValue = 4


_RcDot1agCfmMaCompMhfCreation_Type.__name__ = "Dot1agCfmMhfCreation"
_RcDot1agCfmMaCompMhfCreation_Object = MibTableColumn
rcDot1agCfmMaCompMhfCreation = _RcDot1agCfmMaCompMhfCreation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 3),
    _RcDot1agCfmMaCompMhfCreation_Type()
)
rcDot1agCfmMaCompMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompMhfCreation.setStatus("current")


class _RcDot1agCfmMaCompIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type rcDot1agCfmMaCompIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 5


_RcDot1agCfmMaCompIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_RcDot1agCfmMaCompIdPermission_Object = MibTableColumn
rcDot1agCfmMaCompIdPermission = _RcDot1agCfmMaCompIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 4),
    _RcDot1agCfmMaCompIdPermission_Type()
)
rcDot1agCfmMaCompIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompIdPermission.setStatus("current")
_RcDot1agCfmMaCompNumberOfVids_Type = Unsigned32
_RcDot1agCfmMaCompNumberOfVids_Object = MibTableColumn
rcDot1agCfmMaCompNumberOfVids = _RcDot1agCfmMaCompNumberOfVids_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 5),
    _RcDot1agCfmMaCompNumberOfVids_Type()
)
rcDot1agCfmMaCompNumberOfVids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompNumberOfVids.setStatus("current")
_RcDot1agCfmMaCompRowStatus_Type = RowStatus
_RcDot1agCfmMaCompRowStatus_Object = MibTableColumn
rcDot1agCfmMaCompRowStatus = _RcDot1agCfmMaCompRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 2, 1, 6),
    _RcDot1agCfmMaCompRowStatus_Type()
)
rcDot1agCfmMaCompRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaCompRowStatus.setStatus("current")
_RcDot1agCfmMaMepListTable_Object = MibTable
rcDot1agCfmMaMepListTable = _RcDot1agCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 3)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaMepListTable.setStatus("current")
_RcDot1agCfmMaMepListEntry_Object = MibTableRow
rcDot1agCfmMaMepListEntry = _RcDot1agCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 3, 1)
)
rcDot1agCfmMaMepListEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaMepListEntry.setStatus("current")
_RcDot1agCfmMaMepListIdentifier_Type = Dot1agCfmMepId
_RcDot1agCfmMaMepListIdentifier_Object = MibTableColumn
rcDot1agCfmMaMepListIdentifier = _RcDot1agCfmMaMepListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 3, 1, 1),
    _RcDot1agCfmMaMepListIdentifier_Type()
)
rcDot1agCfmMaMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMaMepListIdentifier.setStatus("current")
_RcDot1agCfmMaMepListRowStatus_Type = RowStatus
_RcDot1agCfmMaMepListRowStatus_Object = MibTableColumn
rcDot1agCfmMaMepListRowStatus = _RcDot1agCfmMaMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 6, 3, 1, 2),
    _RcDot1agCfmMaMepListRowStatus_Type()
)
rcDot1agCfmMaMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMaMepListRowStatus.setStatus("current")
_RcDot1agCfmMep_ObjectIdentity = ObjectIdentity
rcDot1agCfmMep = _RcDot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7)
)
_RcDot1agCfmMepTable_Object = MibTable
rcDot1agCfmMepTable = _RcDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepTable.setStatus("current")
_RcDot1agCfmMepEntry_Object = MibTableRow
rcDot1agCfmMepEntry = _RcDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1)
)
rcDot1agCfmMepEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepEntry.setStatus("current")
_RcDot1agCfmMepIdentifier_Type = Dot1agCfmMepId
_RcDot1agCfmMepIdentifier_Object = MibTableColumn
rcDot1agCfmMepIdentifier = _RcDot1agCfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 1),
    _RcDot1agCfmMepIdentifier_Type()
)
rcDot1agCfmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMepIdentifier.setStatus("current")
_RcDot1agCfmMepIfIndex_Type = InterfaceIndexOrZero
_RcDot1agCfmMepIfIndex_Object = MibTableColumn
rcDot1agCfmMepIfIndex = _RcDot1agCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 2),
    _RcDot1agCfmMepIfIndex_Type()
)
rcDot1agCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepIfIndex.setStatus("current")
_RcDot1agCfmMepDirection_Type = Dot1agCfmMpDirection
_RcDot1agCfmMepDirection_Object = MibTableColumn
rcDot1agCfmMepDirection = _RcDot1agCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 3),
    _RcDot1agCfmMepDirection_Type()
)
rcDot1agCfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDirection.setStatus("current")


class _RcDot1agCfmMepPrimaryVid_Type(Unsigned32):
    """Custom type rcDot1agCfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_RcDot1agCfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_RcDot1agCfmMepPrimaryVid_Object = MibTableColumn
rcDot1agCfmMepPrimaryVid = _RcDot1agCfmMepPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 4),
    _RcDot1agCfmMepPrimaryVid_Type()
)
rcDot1agCfmMepPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepPrimaryVid.setStatus("current")


class _RcDot1agCfmMepActive_Type(TruthValue):
    """Custom type rcDot1agCfmMepActive based on TruthValue"""
    defaultValue = 2


_RcDot1agCfmMepActive_Type.__name__ = "TruthValue"
_RcDot1agCfmMepActive_Object = MibTableColumn
rcDot1agCfmMepActive = _RcDot1agCfmMepActive_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 5),
    _RcDot1agCfmMepActive_Type()
)
rcDot1agCfmMepActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepActive.setStatus("current")


class _RcDot1agCfmMepFngState_Type(Dot1agCfmFngState):
    """Custom type rcDot1agCfmMepFngState based on Dot1agCfmFngState"""
    defaultValue = 1


_RcDot1agCfmMepFngState_Type.__name__ = "Dot1agCfmFngState"
_RcDot1agCfmMepFngState_Object = MibTableColumn
rcDot1agCfmMepFngState = _RcDot1agCfmMepFngState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 6),
    _RcDot1agCfmMepFngState_Type()
)
rcDot1agCfmMepFngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepFngState.setStatus("current")


class _RcDot1agCfmMepCciEnabled_Type(TruthValue):
    """Custom type rcDot1agCfmMepCciEnabled based on TruthValue"""
    defaultValue = 2


_RcDot1agCfmMepCciEnabled_Type.__name__ = "TruthValue"
_RcDot1agCfmMepCciEnabled_Object = MibTableColumn
rcDot1agCfmMepCciEnabled = _RcDot1agCfmMepCciEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 7),
    _RcDot1agCfmMepCciEnabled_Type()
)
rcDot1agCfmMepCciEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepCciEnabled.setStatus("current")


class _RcDot1agCfmMepCcmLtmPriority_Type(Unsigned32):
    """Custom type rcDot1agCfmMepCcmLtmPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcDot1agCfmMepCcmLtmPriority_Type.__name__ = "Unsigned32"
_RcDot1agCfmMepCcmLtmPriority_Object = MibTableColumn
rcDot1agCfmMepCcmLtmPriority = _RcDot1agCfmMepCcmLtmPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 8),
    _RcDot1agCfmMepCcmLtmPriority_Type()
)
rcDot1agCfmMepCcmLtmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepCcmLtmPriority.setStatus("current")
_RcDot1agCfmMepMacAddress_Type = MacAddress
_RcDot1agCfmMepMacAddress_Object = MibTableColumn
rcDot1agCfmMepMacAddress = _RcDot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 9),
    _RcDot1agCfmMepMacAddress_Type()
)
rcDot1agCfmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepMacAddress.setStatus("current")


class _RcDot1agCfmMepLowPrDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type rcDot1agCfmMepLowPrDef based on Dot1agCfmLowestAlarmPri"""
    defaultValue = 2


_RcDot1agCfmMepLowPrDef_Type.__name__ = "Dot1agCfmLowestAlarmPri"
_RcDot1agCfmMepLowPrDef_Object = MibTableColumn
rcDot1agCfmMepLowPrDef = _RcDot1agCfmMepLowPrDef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 10),
    _RcDot1agCfmMepLowPrDef_Type()
)
rcDot1agCfmMepLowPrDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLowPrDef.setStatus("current")


class _RcDot1agCfmMepFngAlarmTime_Type(TimeInterval):
    """Custom type rcDot1agCfmMepFngAlarmTime based on TimeInterval"""
    defaultValue = 250

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_RcDot1agCfmMepFngAlarmTime_Type.__name__ = "TimeInterval"
_RcDot1agCfmMepFngAlarmTime_Object = MibTableColumn
rcDot1agCfmMepFngAlarmTime = _RcDot1agCfmMepFngAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 11),
    _RcDot1agCfmMepFngAlarmTime_Type()
)
rcDot1agCfmMepFngAlarmTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepFngAlarmTime.setStatus("current")


class _RcDot1agCfmMepFngResetTime_Type(TimeInterval):
    """Custom type rcDot1agCfmMepFngResetTime based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1000),
    )


_RcDot1agCfmMepFngResetTime_Type.__name__ = "TimeInterval"
_RcDot1agCfmMepFngResetTime_Object = MibTableColumn
rcDot1agCfmMepFngResetTime = _RcDot1agCfmMepFngResetTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 12),
    _RcDot1agCfmMepFngResetTime_Type()
)
rcDot1agCfmMepFngResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepFngResetTime.setStatus("current")
_RcDot1agCfmMepHighestPrDefect_Type = Dot1agCfmHighestDefectPri
_RcDot1agCfmMepHighestPrDefect_Object = MibTableColumn
rcDot1agCfmMepHighestPrDefect = _RcDot1agCfmMepHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 13),
    _RcDot1agCfmMepHighestPrDefect_Type()
)
rcDot1agCfmMepHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepHighestPrDefect.setStatus("current")
_RcDot1agCfmMepDefects_Type = Dot1agCfmMepDefects
_RcDot1agCfmMepDefects_Object = MibTableColumn
rcDot1agCfmMepDefects = _RcDot1agCfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 14),
    _RcDot1agCfmMepDefects_Type()
)
rcDot1agCfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDefects.setStatus("current")


class _RcDot1agCfmMepErrorCcmLastFailure_Type(OctetString):
    """Custom type rcDot1agCfmMepErrorCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_RcDot1agCfmMepErrorCcmLastFailure_Type.__name__ = "OctetString"
_RcDot1agCfmMepErrorCcmLastFailure_Object = MibTableColumn
rcDot1agCfmMepErrorCcmLastFailure = _RcDot1agCfmMepErrorCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 15),
    _RcDot1agCfmMepErrorCcmLastFailure_Type()
)
rcDot1agCfmMepErrorCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepErrorCcmLastFailure.setStatus("current")


class _RcDot1agCfmMepXconCcmLastFailure_Type(OctetString):
    """Custom type rcDot1agCfmMepXconCcmLastFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1522),
    )


_RcDot1agCfmMepXconCcmLastFailure_Type.__name__ = "OctetString"
_RcDot1agCfmMepXconCcmLastFailure_Object = MibTableColumn
rcDot1agCfmMepXconCcmLastFailure = _RcDot1agCfmMepXconCcmLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 16),
    _RcDot1agCfmMepXconCcmLastFailure_Type()
)
rcDot1agCfmMepXconCcmLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepXconCcmLastFailure.setStatus("current")
_RcDot1agCfmMepCcmSequenceErrors_Type = Counter32
_RcDot1agCfmMepCcmSequenceErrors_Object = MibTableColumn
rcDot1agCfmMepCcmSequenceErrors = _RcDot1agCfmMepCcmSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 17),
    _RcDot1agCfmMepCcmSequenceErrors_Type()
)
rcDot1agCfmMepCcmSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepCcmSequenceErrors.setStatus("current")
_RcDot1agCfmMepCciSentCcms_Type = Counter32
_RcDot1agCfmMepCciSentCcms_Object = MibTableColumn
rcDot1agCfmMepCciSentCcms = _RcDot1agCfmMepCciSentCcms_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 18),
    _RcDot1agCfmMepCciSentCcms_Type()
)
rcDot1agCfmMepCciSentCcms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepCciSentCcms.setStatus("current")
_RcDot1agCfmMepNextLbmTransId_Type = Unsigned32
_RcDot1agCfmMepNextLbmTransId_Object = MibTableColumn
rcDot1agCfmMepNextLbmTransId = _RcDot1agCfmMepNextLbmTransId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 19),
    _RcDot1agCfmMepNextLbmTransId_Type()
)
rcDot1agCfmMepNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepNextLbmTransId.setStatus("current")
_RcDot1agCfmMepLbrIn_Type = Counter32
_RcDot1agCfmMepLbrIn_Object = MibTableColumn
rcDot1agCfmMepLbrIn = _RcDot1agCfmMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 20),
    _RcDot1agCfmMepLbrIn_Type()
)
rcDot1agCfmMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLbrIn.setStatus("current")
_RcDot1agCfmMepLbrInOutOfOrder_Type = Counter32
_RcDot1agCfmMepLbrInOutOfOrder_Object = MibTableColumn
rcDot1agCfmMepLbrInOutOfOrder = _RcDot1agCfmMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 21),
    _RcDot1agCfmMepLbrInOutOfOrder_Type()
)
rcDot1agCfmMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLbrInOutOfOrder.setStatus("current")
_RcDot1agCfmMepLbrBadMsdu_Type = Counter32
_RcDot1agCfmMepLbrBadMsdu_Object = MibTableColumn
rcDot1agCfmMepLbrBadMsdu = _RcDot1agCfmMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 22),
    _RcDot1agCfmMepLbrBadMsdu_Type()
)
rcDot1agCfmMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLbrBadMsdu.setStatus("current")
_RcDot1agCfmMepLtmNextSeqNumber_Type = Unsigned32
_RcDot1agCfmMepLtmNextSeqNumber_Object = MibTableColumn
rcDot1agCfmMepLtmNextSeqNumber = _RcDot1agCfmMepLtmNextSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 23),
    _RcDot1agCfmMepLtmNextSeqNumber_Type()
)
rcDot1agCfmMepLtmNextSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLtmNextSeqNumber.setStatus("current")
_RcDot1agCfmMepUnexpLtrIn_Type = Counter32
_RcDot1agCfmMepUnexpLtrIn_Object = MibTableColumn
rcDot1agCfmMepUnexpLtrIn = _RcDot1agCfmMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 24),
    _RcDot1agCfmMepUnexpLtrIn_Type()
)
rcDot1agCfmMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepUnexpLtrIn.setStatus("current")
_RcDot1agCfmMepLbrOut_Type = Counter32
_RcDot1agCfmMepLbrOut_Object = MibTableColumn
rcDot1agCfmMepLbrOut = _RcDot1agCfmMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 25),
    _RcDot1agCfmMepLbrOut_Type()
)
rcDot1agCfmMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepLbrOut.setStatus("current")


class _RcDot1agCfmMepTransmitLbmStatus_Type(TruthValue):
    """Custom type rcDot1agCfmMepTransmitLbmStatus based on TruthValue"""
    defaultValue = 1


_RcDot1agCfmMepTransmitLbmStatus_Type.__name__ = "TruthValue"
_RcDot1agCfmMepTransmitLbmStatus_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmStatus = _RcDot1agCfmMepTransmitLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 26),
    _RcDot1agCfmMepTransmitLbmStatus_Type()
)
rcDot1agCfmMepTransmitLbmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmStatus.setStatus("current")
_RcDot1agCfmMepTransmitLbmDestMacAddress_Type = MacAddress
_RcDot1agCfmMepTransmitLbmDestMacAddress_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmDestMacAddress = _RcDot1agCfmMepTransmitLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 27),
    _RcDot1agCfmMepTransmitLbmDestMacAddress_Type()
)
rcDot1agCfmMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmDestMacAddress.setStatus("current")
_RcDot1agCfmMepTransmitLbmDestMepId_Type = Dot1agCfmMepIdOrZero
_RcDot1agCfmMepTransmitLbmDestMepId_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmDestMepId = _RcDot1agCfmMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 28),
    _RcDot1agCfmMepTransmitLbmDestMepId_Type()
)
rcDot1agCfmMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmDestMepId.setStatus("current")
_RcDot1agCfmMepTransmitLbmDestIsMepId_Type = TruthValue
_RcDot1agCfmMepTransmitLbmDestIsMepId_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmDestIsMepId = _RcDot1agCfmMepTransmitLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 29),
    _RcDot1agCfmMepTransmitLbmDestIsMepId_Type()
)
rcDot1agCfmMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmDestIsMepId.setStatus("current")


class _RcDot1agCfmMepTransmitLbmMessages_Type(Integer32):
    """Custom type rcDot1agCfmMepTransmitLbmMessages based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RcDot1agCfmMepTransmitLbmMessages_Type.__name__ = "Integer32"
_RcDot1agCfmMepTransmitLbmMessages_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmMessages = _RcDot1agCfmMepTransmitLbmMessages_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 30),
    _RcDot1agCfmMepTransmitLbmMessages_Type()
)
rcDot1agCfmMepTransmitLbmMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmMessages.setStatus("current")


class _RcDot1agCfmMepTransmitLbmDataTlv_Type(OctetString):
    """Custom type rcDot1agCfmMepTransmitLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_RcDot1agCfmMepTransmitLbmDataTlv_Type.__name__ = "OctetString"
_RcDot1agCfmMepTransmitLbmDataTlv_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmDataTlv = _RcDot1agCfmMepTransmitLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 31),
    _RcDot1agCfmMepTransmitLbmDataTlv_Type()
)
rcDot1agCfmMepTransmitLbmDataTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmDataTlv.setStatus("current")


class _RcDot1agCfmMepTransmitLbmVlanPriority_Type(Integer32):
    """Custom type rcDot1agCfmMepTransmitLbmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcDot1agCfmMepTransmitLbmVlanPriority_Type.__name__ = "Integer32"
_RcDot1agCfmMepTransmitLbmVlanPriority_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmVlanPriority = _RcDot1agCfmMepTransmitLbmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 32),
    _RcDot1agCfmMepTransmitLbmVlanPriority_Type()
)
rcDot1agCfmMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmVlanPriority.setStatus("current")


class _RcDot1agCfmMepTransmitLbmVlanDropEnable_Type(TruthValue):
    """Custom type rcDot1agCfmMepTransmitLbmVlanDropEnable based on TruthValue"""
    defaultValue = 1


_RcDot1agCfmMepTransmitLbmVlanDropEnable_Type.__name__ = "TruthValue"
_RcDot1agCfmMepTransmitLbmVlanDropEnable_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmVlanDropEnable = _RcDot1agCfmMepTransmitLbmVlanDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 33),
    _RcDot1agCfmMepTransmitLbmVlanDropEnable_Type()
)
rcDot1agCfmMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmVlanDropEnable.setStatus("current")


class _RcDot1agCfmMepTransmitLbmResultOK_Type(TruthValue):
    """Custom type rcDot1agCfmMepTransmitLbmResultOK based on TruthValue"""
    defaultValue = 1


_RcDot1agCfmMepTransmitLbmResultOK_Type.__name__ = "TruthValue"
_RcDot1agCfmMepTransmitLbmResultOK_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmResultOK = _RcDot1agCfmMepTransmitLbmResultOK_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 34),
    _RcDot1agCfmMepTransmitLbmResultOK_Type()
)
rcDot1agCfmMepTransmitLbmResultOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmResultOK.setStatus("current")
_RcDot1agCfmMepTransmitLbmSeqNumber_Type = Unsigned32
_RcDot1agCfmMepTransmitLbmSeqNumber_Object = MibTableColumn
rcDot1agCfmMepTransmitLbmSeqNumber = _RcDot1agCfmMepTransmitLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 35),
    _RcDot1agCfmMepTransmitLbmSeqNumber_Type()
)
rcDot1agCfmMepTransmitLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLbmSeqNumber.setStatus("current")


class _RcDot1agCfmMepTransmitLtmStatus_Type(TruthValue):
    """Custom type rcDot1agCfmMepTransmitLtmStatus based on TruthValue"""
    defaultValue = 1


_RcDot1agCfmMepTransmitLtmStatus_Type.__name__ = "TruthValue"
_RcDot1agCfmMepTransmitLtmStatus_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmStatus = _RcDot1agCfmMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 36),
    _RcDot1agCfmMepTransmitLtmStatus_Type()
)
rcDot1agCfmMepTransmitLtmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmStatus.setStatus("current")


class _RcDot1agCfmMepTransmitLtmFlags_Type(Bits):
    """Custom type rcDot1agCfmMepTransmitLtmFlags based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_RcDot1agCfmMepTransmitLtmFlags_Type.__name__ = "Bits"
_RcDot1agCfmMepTransmitLtmFlags_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmFlags = _RcDot1agCfmMepTransmitLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 37),
    _RcDot1agCfmMepTransmitLtmFlags_Type()
)
rcDot1agCfmMepTransmitLtmFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmFlags.setStatus("current")
_RcDot1agCfmMepTransmitLtmTargetMacAddress_Type = MacAddress
_RcDot1agCfmMepTransmitLtmTargetMacAddress_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmTargetMacAddress = _RcDot1agCfmMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 38),
    _RcDot1agCfmMepTransmitLtmTargetMacAddress_Type()
)
rcDot1agCfmMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmTargetMacAddress.setStatus("current")
_RcDot1agCfmMepTransmitLtmTargetMepId_Type = Dot1agCfmMepIdOrZero
_RcDot1agCfmMepTransmitLtmTargetMepId_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmTargetMepId = _RcDot1agCfmMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 39),
    _RcDot1agCfmMepTransmitLtmTargetMepId_Type()
)
rcDot1agCfmMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmTargetMepId.setStatus("current")
_RcDot1agCfmMepTransmitLtmTargetIsMepId_Type = TruthValue
_RcDot1agCfmMepTransmitLtmTargetIsMepId_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmTargetIsMepId = _RcDot1agCfmMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 40),
    _RcDot1agCfmMepTransmitLtmTargetIsMepId_Type()
)
rcDot1agCfmMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmTargetIsMepId.setStatus("current")


class _RcDot1agCfmMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type rcDot1agCfmMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcDot1agCfmMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_RcDot1agCfmMepTransmitLtmTtl_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmTtl = _RcDot1agCfmMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 41),
    _RcDot1agCfmMepTransmitLtmTtl_Type()
)
rcDot1agCfmMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmTtl.setStatus("current")


class _RcDot1agCfmMepTransmitLtmResult_Type(TruthValue):
    """Custom type rcDot1agCfmMepTransmitLtmResult based on TruthValue"""
    defaultValue = 1


_RcDot1agCfmMepTransmitLtmResult_Type.__name__ = "TruthValue"
_RcDot1agCfmMepTransmitLtmResult_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmResult = _RcDot1agCfmMepTransmitLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 42),
    _RcDot1agCfmMepTransmitLtmResult_Type()
)
rcDot1agCfmMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmResult.setStatus("current")
_RcDot1agCfmMepTransmitLtmSeqNumber_Type = Unsigned32
_RcDot1agCfmMepTransmitLtmSeqNumber_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmSeqNumber = _RcDot1agCfmMepTransmitLtmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 43),
    _RcDot1agCfmMepTransmitLtmSeqNumber_Type()
)
rcDot1agCfmMepTransmitLtmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmSeqNumber.setStatus("current")


class _RcDot1agCfmMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type rcDot1agCfmMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RcDot1agCfmMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_RcDot1agCfmMepTransmitLtmEgressIdentifier_Object = MibTableColumn
rcDot1agCfmMepTransmitLtmEgressIdentifier = _RcDot1agCfmMepTransmitLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 44),
    _RcDot1agCfmMepTransmitLtmEgressIdentifier_Type()
)
rcDot1agCfmMepTransmitLtmEgressIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepTransmitLtmEgressIdentifier.setStatus("current")
_RcDot1agCfmMepRowStatus_Type = RowStatus
_RcDot1agCfmMepRowStatus_Object = MibTableColumn
rcDot1agCfmMepRowStatus = _RcDot1agCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 1, 1, 45),
    _RcDot1agCfmMepRowStatus_Type()
)
rcDot1agCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDot1agCfmMepRowStatus.setStatus("current")
_RcDot1agCfmLtrTable_Object = MibTable
rcDot1agCfmLtrTable = _RcDot1agCfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2)
)
if mibBuilder.loadTexts:
    rcDot1agCfmLtrTable.setStatus("current")
_RcDot1agCfmLtrEntry_Object = MibTableRow
rcDot1agCfmLtrEntry = _RcDot1agCfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1)
)
rcDot1agCfmLtrEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepIdentifier"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrSeqNumber"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmLtrEntry.setStatus("current")


class _RcDot1agCfmLtrSeqNumber_Type(Unsigned32):
    """Custom type rcDot1agCfmLtrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RcDot1agCfmLtrSeqNumber_Type.__name__ = "Unsigned32"
_RcDot1agCfmLtrSeqNumber_Object = MibTableColumn
rcDot1agCfmLtrSeqNumber = _RcDot1agCfmLtrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 1),
    _RcDot1agCfmLtrSeqNumber_Type()
)
rcDot1agCfmLtrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrSeqNumber.setStatus("current")


class _RcDot1agCfmLtrReceiveOrder_Type(Unsigned32):
    """Custom type rcDot1agCfmLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RcDot1agCfmLtrReceiveOrder_Type.__name__ = "Unsigned32"
_RcDot1agCfmLtrReceiveOrder_Object = MibTableColumn
rcDot1agCfmLtrReceiveOrder = _RcDot1agCfmLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 2),
    _RcDot1agCfmLtrReceiveOrder_Type()
)
rcDot1agCfmLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrReceiveOrder.setStatus("current")


class _RcDot1agCfmLtrTtl_Type(Unsigned32):
    """Custom type rcDot1agCfmLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcDot1agCfmLtrTtl_Type.__name__ = "Unsigned32"
_RcDot1agCfmLtrTtl_Object = MibTableColumn
rcDot1agCfmLtrTtl = _RcDot1agCfmLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 3),
    _RcDot1agCfmLtrTtl_Type()
)
rcDot1agCfmLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrTtl.setStatus("current")
_RcDot1agCfmLtrForwarded_Type = TruthValue
_RcDot1agCfmLtrForwarded_Object = MibTableColumn
rcDot1agCfmLtrForwarded = _RcDot1agCfmLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 4),
    _RcDot1agCfmLtrForwarded_Type()
)
rcDot1agCfmLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrForwarded.setStatus("current")
_RcDot1agCfmLtrTerminalMep_Type = TruthValue
_RcDot1agCfmLtrTerminalMep_Object = MibTableColumn
rcDot1agCfmLtrTerminalMep = _RcDot1agCfmLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 5),
    _RcDot1agCfmLtrTerminalMep_Type()
)
rcDot1agCfmLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrTerminalMep.setStatus("current")


class _RcDot1agCfmLtrLastEgressIdentifier_Type(OctetString):
    """Custom type rcDot1agCfmLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RcDot1agCfmLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_RcDot1agCfmLtrLastEgressIdentifier_Object = MibTableColumn
rcDot1agCfmLtrLastEgressIdentifier = _RcDot1agCfmLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 6),
    _RcDot1agCfmLtrLastEgressIdentifier_Type()
)
rcDot1agCfmLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrLastEgressIdentifier.setStatus("current")


class _RcDot1agCfmLtrNextEgressIdentifier_Type(OctetString):
    """Custom type rcDot1agCfmLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RcDot1agCfmLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_RcDot1agCfmLtrNextEgressIdentifier_Object = MibTableColumn
rcDot1agCfmLtrNextEgressIdentifier = _RcDot1agCfmLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 7),
    _RcDot1agCfmLtrNextEgressIdentifier_Type()
)
rcDot1agCfmLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrNextEgressIdentifier.setStatus("current")
_RcDot1agCfmLtrRelay_Type = Dot1agCfmRelayActionFieldValue
_RcDot1agCfmLtrRelay_Object = MibTableColumn
rcDot1agCfmLtrRelay = _RcDot1agCfmLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 8),
    _RcDot1agCfmLtrRelay_Type()
)
rcDot1agCfmLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrRelay.setStatus("current")
_RcDot1agCfmLtrChassisIdSubtype_Type = LldpChassisIdSubtype
_RcDot1agCfmLtrChassisIdSubtype_Object = MibTableColumn
rcDot1agCfmLtrChassisIdSubtype = _RcDot1agCfmLtrChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 9),
    _RcDot1agCfmLtrChassisIdSubtype_Type()
)
rcDot1agCfmLtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrChassisIdSubtype.setStatus("current")
_RcDot1agCfmLtrChassisId_Type = LldpChassisId
_RcDot1agCfmLtrChassisId_Object = MibTableColumn
rcDot1agCfmLtrChassisId = _RcDot1agCfmLtrChassisId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 10),
    _RcDot1agCfmLtrChassisId_Type()
)
rcDot1agCfmLtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrChassisId.setStatus("current")
_RcDot1agCfmLtrManAddressDomain_Type = TDomain
_RcDot1agCfmLtrManAddressDomain_Object = MibTableColumn
rcDot1agCfmLtrManAddressDomain = _RcDot1agCfmLtrManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 11),
    _RcDot1agCfmLtrManAddressDomain_Type()
)
rcDot1agCfmLtrManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrManAddressDomain.setStatus("current")
_RcDot1agCfmLtrManAddress_Type = TAddress
_RcDot1agCfmLtrManAddress_Object = MibTableColumn
rcDot1agCfmLtrManAddress = _RcDot1agCfmLtrManAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 12),
    _RcDot1agCfmLtrManAddress_Type()
)
rcDot1agCfmLtrManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrManAddress.setStatus("current")
_RcDot1agCfmLtrIngress_Type = Dot1agCfmIngressActionFieldValue
_RcDot1agCfmLtrIngress_Object = MibTableColumn
rcDot1agCfmLtrIngress = _RcDot1agCfmLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 13),
    _RcDot1agCfmLtrIngress_Type()
)
rcDot1agCfmLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrIngress.setStatus("current")
_RcDot1agCfmLtrIngressMac_Type = MacAddress
_RcDot1agCfmLtrIngressMac_Object = MibTableColumn
rcDot1agCfmLtrIngressMac = _RcDot1agCfmLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 14),
    _RcDot1agCfmLtrIngressMac_Type()
)
rcDot1agCfmLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrIngressMac.setStatus("current")
_RcDot1agCfmLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_RcDot1agCfmLtrIngressPortIdSubtype_Object = MibTableColumn
rcDot1agCfmLtrIngressPortIdSubtype = _RcDot1agCfmLtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 15),
    _RcDot1agCfmLtrIngressPortIdSubtype_Type()
)
rcDot1agCfmLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrIngressPortIdSubtype.setStatus("current")
_RcDot1agCfmLtrIngressPortId_Type = LldpPortId
_RcDot1agCfmLtrIngressPortId_Object = MibTableColumn
rcDot1agCfmLtrIngressPortId = _RcDot1agCfmLtrIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 16),
    _RcDot1agCfmLtrIngressPortId_Type()
)
rcDot1agCfmLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrIngressPortId.setStatus("current")
_RcDot1agCfmLtrEgress_Type = Dot1agCfmEgressActionFieldValue
_RcDot1agCfmLtrEgress_Object = MibTableColumn
rcDot1agCfmLtrEgress = _RcDot1agCfmLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 17),
    _RcDot1agCfmLtrEgress_Type()
)
rcDot1agCfmLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrEgress.setStatus("current")
_RcDot1agCfmLtrEgressMac_Type = MacAddress
_RcDot1agCfmLtrEgressMac_Object = MibTableColumn
rcDot1agCfmLtrEgressMac = _RcDot1agCfmLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 18),
    _RcDot1agCfmLtrEgressMac_Type()
)
rcDot1agCfmLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrEgressMac.setStatus("current")
_RcDot1agCfmLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_RcDot1agCfmLtrEgressPortIdSubtype_Object = MibTableColumn
rcDot1agCfmLtrEgressPortIdSubtype = _RcDot1agCfmLtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 19),
    _RcDot1agCfmLtrEgressPortIdSubtype_Type()
)
rcDot1agCfmLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrEgressPortIdSubtype.setStatus("current")
_RcDot1agCfmLtrEgressPortId_Type = LldpPortId
_RcDot1agCfmLtrEgressPortId_Object = MibTableColumn
rcDot1agCfmLtrEgressPortId = _RcDot1agCfmLtrEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 20),
    _RcDot1agCfmLtrEgressPortId_Type()
)
rcDot1agCfmLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrEgressPortId.setStatus("current")


class _RcDot1agCfmLtrOrganizationSpecificTlv_Type(OctetString):
    """Custom type rcDot1agCfmLtrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_RcDot1agCfmLtrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_RcDot1agCfmLtrOrganizationSpecificTlv_Object = MibTableColumn
rcDot1agCfmLtrOrganizationSpecificTlv = _RcDot1agCfmLtrOrganizationSpecificTlv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 2, 1, 21),
    _RcDot1agCfmLtrOrganizationSpecificTlv_Type()
)
rcDot1agCfmLtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmLtrOrganizationSpecificTlv.setStatus("current")
_RcDot1agCfmMepDbTable_Object = MibTable
rcDot1agCfmMepDbTable = _RcDot1agCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3)
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbTable.setStatus("current")
_RcDot1agCfmMepDbEntry_Object = MibTableRow
rcDot1agCfmMepDbEntry = _RcDot1agCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1)
)
rcDot1agCfmMepDbEntry.setIndexNames(
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaIndex"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepIdentifier"),
    (0, "RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbEntry.setStatus("current")
_RcDot1agCfmMepDbRMepIdentifier_Type = Dot1agCfmMepId
_RcDot1agCfmMepDbRMepIdentifier_Object = MibTableColumn
rcDot1agCfmMepDbRMepIdentifier = _RcDot1agCfmMepDbRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 1),
    _RcDot1agCfmMepDbRMepIdentifier_Type()
)
rcDot1agCfmMepDbRMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbRMepIdentifier.setStatus("current")
_RcDot1agCfmMepDbRMepState_Type = Dot1agCfmRemoteMepState
_RcDot1agCfmMepDbRMepState_Object = MibTableColumn
rcDot1agCfmMepDbRMepState = _RcDot1agCfmMepDbRMepState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 2),
    _RcDot1agCfmMepDbRMepState_Type()
)
rcDot1agCfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbRMepState.setStatus("current")
_RcDot1agCfmMepDbRMepFailedOkTime_Type = TimeStamp
_RcDot1agCfmMepDbRMepFailedOkTime_Object = MibTableColumn
rcDot1agCfmMepDbRMepFailedOkTime = _RcDot1agCfmMepDbRMepFailedOkTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 3),
    _RcDot1agCfmMepDbRMepFailedOkTime_Type()
)
rcDot1agCfmMepDbRMepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbRMepFailedOkTime.setStatus("current")
_RcDot1agCfmMepDbMacAddress_Type = MacAddress
_RcDot1agCfmMepDbMacAddress_Object = MibTableColumn
rcDot1agCfmMepDbMacAddress = _RcDot1agCfmMepDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 4),
    _RcDot1agCfmMepDbMacAddress_Type()
)
rcDot1agCfmMepDbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbMacAddress.setStatus("current")
_RcDot1agCfmMepDbRdi_Type = TruthValue
_RcDot1agCfmMepDbRdi_Object = MibTableColumn
rcDot1agCfmMepDbRdi = _RcDot1agCfmMepDbRdi_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 5),
    _RcDot1agCfmMepDbRdi_Type()
)
rcDot1agCfmMepDbRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbRdi.setStatus("current")


class _RcDot1agCfmMepDbPortStatusTlv_Type(Dot1agCfmPortStatus):
    """Custom type rcDot1agCfmMepDbPortStatusTlv based on Dot1agCfmPortStatus"""
    defaultValue = 0


_RcDot1agCfmMepDbPortStatusTlv_Type.__name__ = "Dot1agCfmPortStatus"
_RcDot1agCfmMepDbPortStatusTlv_Object = MibTableColumn
rcDot1agCfmMepDbPortStatusTlv = _RcDot1agCfmMepDbPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 6),
    _RcDot1agCfmMepDbPortStatusTlv_Type()
)
rcDot1agCfmMepDbPortStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbPortStatusTlv.setStatus("current")


class _RcDot1agCfmMepDbInterfaceStatusTlv_Type(Dot1agCfmInterfaceStatus):
    """Custom type rcDot1agCfmMepDbInterfaceStatusTlv based on Dot1agCfmInterfaceStatus"""
    defaultValue = 0


_RcDot1agCfmMepDbInterfaceStatusTlv_Type.__name__ = "Dot1agCfmInterfaceStatus"
_RcDot1agCfmMepDbInterfaceStatusTlv_Object = MibTableColumn
rcDot1agCfmMepDbInterfaceStatusTlv = _RcDot1agCfmMepDbInterfaceStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 7),
    _RcDot1agCfmMepDbInterfaceStatusTlv_Type()
)
rcDot1agCfmMepDbInterfaceStatusTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbInterfaceStatusTlv.setStatus("current")
_RcDot1agCfmMepDbChassisIdSubtype_Type = LldpChassisIdSubtype
_RcDot1agCfmMepDbChassisIdSubtype_Object = MibTableColumn
rcDot1agCfmMepDbChassisIdSubtype = _RcDot1agCfmMepDbChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 8),
    _RcDot1agCfmMepDbChassisIdSubtype_Type()
)
rcDot1agCfmMepDbChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbChassisIdSubtype.setStatus("current")
_RcDot1agCfmMepDbChassisId_Type = LldpChassisId
_RcDot1agCfmMepDbChassisId_Object = MibTableColumn
rcDot1agCfmMepDbChassisId = _RcDot1agCfmMepDbChassisId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 9),
    _RcDot1agCfmMepDbChassisId_Type()
)
rcDot1agCfmMepDbChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbChassisId.setStatus("current")
_RcDot1agCfmMepDbManAddressDomain_Type = TDomain
_RcDot1agCfmMepDbManAddressDomain_Object = MibTableColumn
rcDot1agCfmMepDbManAddressDomain = _RcDot1agCfmMepDbManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 10),
    _RcDot1agCfmMepDbManAddressDomain_Type()
)
rcDot1agCfmMepDbManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbManAddressDomain.setStatus("current")
_RcDot1agCfmMepDbManAddress_Type = TAddress
_RcDot1agCfmMepDbManAddress_Object = MibTableColumn
rcDot1agCfmMepDbManAddress = _RcDot1agCfmMepDbManAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 1, 7, 3, 1, 11),
    _RcDot1agCfmMepDbManAddress_Type()
)
rcDot1agCfmMepDbManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbManAddress.setStatus("current")
_RcDot1agCfmConformance_ObjectIdentity = ObjectIdentity
rcDot1agCfmConformance = _RcDot1agCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2)
)
_RcDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
rcDot1agCfmCompliances = _RcDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 1)
)
_RcDot1agCfmGroups_ObjectIdentity = ObjectIdentity
rcDot1agCfmGroups = _RcDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2)
)

# Managed Objects groups

rcDot1agCfmStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 1)
)
rcDot1agCfmStackGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackMdIndex"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackMaIndex"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackMepId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackMacAddress"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmStackGroup.setStatus("current")

rcDot1agCfmDefaultMdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 2)
)
rcDot1agCfmDefaultMdGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdDefLevel"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdDefMhfCreation"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdDefIdPermission"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdLevel"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdMhfCreation"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdIdPermission"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmDefaultMdGroup.setStatus("current")

rcDot1agCfmVlanIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 3)
)
rcDot1agCfmVlanIdGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmVlanPrimaryVid"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmVlanRowStatus"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmVlanIdGroup.setStatus("current")

rcDot1agCfmConfigErrorListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 4)
)
rcDot1agCfmConfigErrorListGroup.setObjects(
    ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    rcDot1agCfmConfigErrorListGroup.setStatus("current")

rcDot1agCfmMdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 5)
)
rcDot1agCfmMdGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdTableNextIndex"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdName"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdFormat"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdMdLevel"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdMhfCreation"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdMhfIdPermission"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdMaNextIndex"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdRowStatus"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmMdGroup.setStatus("current")

rcDot1agCfmMaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 6)
)
rcDot1agCfmMaGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaNetFormat"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaNetName"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaNetCcmInterval"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaNetRowStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaCompPrimaryVlanId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaCompMhfCreation"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaCompIdPermission"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaCompRowStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaCompNumberOfVids"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaMepListRowStatus"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmMaGroup.setStatus("current")

rcDot1agCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 7)
)
rcDot1agCfmMepGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepIfIndex"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDirection"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepPrimaryVid"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepActive"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepFngState"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepCciEnabled"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepCcmLtmPriority"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepMacAddress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLowPrDef"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepFngAlarmTime"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepFngResetTime"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepHighestPrDefect"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDefects"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepErrorCcmLastFailure"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepXconCcmLastFailure"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepCcmSequenceErrors"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepCciSentCcms"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepNextLbmTransId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLbrIn"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLbrInOutOfOrder"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLbrBadMsdu"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLtmNextSeqNumber"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepUnexpLtrIn"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepLbrOut"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmDestMacAddress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmDestMepId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmDestIsMepId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmMessages"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmDataTlv"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmVlanPriority"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmVlanDropEnable"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmResultOK"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLbmSeqNumber"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmFlags"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmTargetMacAddress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmTargetMepId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmTargetIsMepId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmTtl"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmResult"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmSeqNumber"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepTransmitLtmEgressIdentifier"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepRowStatus"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrForwarded"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrRelay"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrChassisIdSubtype"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrChassisId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrManAddress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrManAddressDomain"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrIngress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrIngressMac"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrIngressPortIdSubtype"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrIngressPortId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrEgress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrEgressMac"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrEgressPortIdSubtype"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrEgressPortId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrTerminalMep"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrLastEgressIdentifier"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrNextEgressIdentifier"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrTtl"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmLtrOrganizationSpecificTlv"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepGroup.setStatus("current")

rcDot1agCfmMepDbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 8)
)
rcDot1agCfmMepDbGroup.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbRMepState"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbRMepFailedOkTime"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbMacAddress"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbRdi"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbPortStatusTlv"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbInterfaceStatusTlv"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbChassisIdSubtype"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbChassisId"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbManAddressDomain"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbManAddress"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmMepDbGroup.setStatus("current")


# Notification objects

rcDot1agCfmFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 0, 1)
)
rcDot1agCfmFaultAlarm.setObjects(
    ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepHighestPrDefect")
)
if mibBuilder.loadTexts:
    rcDot1agCfmFaultAlarm.setStatus(
        "current"
    )


# Notifications groups

rcDot1agCfmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 2, 9)
)
rcDot1agCfmNotificationsGroup.setObjects(
    ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmFaultAlarm")
)
if mibBuilder.loadTexts:
    rcDot1agCfmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rcDot1agCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 32, 2, 1, 1)
)
rcDot1agCfmCompliance.setObjects(
      *(("RAISECOM-DOT1AG-MIB", "rcDot1agCfmStackGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmDefaultMdGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmConfigErrorListGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMdGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMaGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmMepDbGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmNotificationsGroup"),
        ("RAISECOM-DOT1AG-MIB", "rcDot1agCfmVlanIdGroup"))
)
if mibBuilder.loadTexts:
    rcDot1agCfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-DOT1AG-MIB",
    **{"rcDot1ag": rcDot1ag,
       "rcDot1agNotifications": rcDot1agNotifications,
       "rcDot1agCfmFaultAlarm": rcDot1agCfmFaultAlarm,
       "rcDot1agMIBObjects": rcDot1agMIBObjects,
       "rcDot1agCfmStack": rcDot1agCfmStack,
       "rcDot1agCfmStackTable": rcDot1agCfmStackTable,
       "rcDot1agCfmStackEntry": rcDot1agCfmStackEntry,
       "rcDot1agCfmStackifIndex": rcDot1agCfmStackifIndex,
       "rcDot1agCfmStackVlanIdOrNone": rcDot1agCfmStackVlanIdOrNone,
       "rcDot1agCfmStackMdLevel": rcDot1agCfmStackMdLevel,
       "rcDot1agCfmStackDirection": rcDot1agCfmStackDirection,
       "rcDot1agCfmStackMdIndex": rcDot1agCfmStackMdIndex,
       "rcDot1agCfmStackMaIndex": rcDot1agCfmStackMaIndex,
       "rcDot1agCfmStackMepId": rcDot1agCfmStackMepId,
       "rcDot1agCfmStackMacAddress": rcDot1agCfmStackMacAddress,
       "rcDot1agCfmDefaultMd": rcDot1agCfmDefaultMd,
       "rcDot1agCfmDefaultMdDefLevel": rcDot1agCfmDefaultMdDefLevel,
       "rcDot1agCfmDefaultMdDefMhfCreation": rcDot1agCfmDefaultMdDefMhfCreation,
       "rcDot1agCfmDefaultMdDefIdPermission": rcDot1agCfmDefaultMdDefIdPermission,
       "rcDot1agCfmDefaultMdTable": rcDot1agCfmDefaultMdTable,
       "rcDot1agCfmDefaultMdEntry": rcDot1agCfmDefaultMdEntry,
       "rcDot1agCfmDefaultMdComponentId": rcDot1agCfmDefaultMdComponentId,
       "rcDot1agCfmDefaultMdPrimaryVid": rcDot1agCfmDefaultMdPrimaryVid,
       "rcDot1agCfmDefaultMdStatus": rcDot1agCfmDefaultMdStatus,
       "rcDot1agCfmDefaultMdLevel": rcDot1agCfmDefaultMdLevel,
       "rcDot1agCfmDefaultMdMhfCreation": rcDot1agCfmDefaultMdMhfCreation,
       "rcDot1agCfmDefaultMdIdPermission": rcDot1agCfmDefaultMdIdPermission,
       "rcDot1agCfmVlan": rcDot1agCfmVlan,
       "rcDot1agCfmVlanTable": rcDot1agCfmVlanTable,
       "rcDot1agCfmVlanEntry": rcDot1agCfmVlanEntry,
       "rcDot1agCfmVlanComponentId": rcDot1agCfmVlanComponentId,
       "rcDot1agCfmVlanVid": rcDot1agCfmVlanVid,
       "rcDot1agCfmVlanPrimaryVid": rcDot1agCfmVlanPrimaryVid,
       "rcDot1agCfmVlanRowStatus": rcDot1agCfmVlanRowStatus,
       "rcDot1agCfmConfigErrorList": rcDot1agCfmConfigErrorList,
       "rcDot1agCfmConfigErrorListTable": rcDot1agCfmConfigErrorListTable,
       "rcDot1agCfmConfigErrorListEntry": rcDot1agCfmConfigErrorListEntry,
       "rcDot1agCfmConfigErrorListVid": rcDot1agCfmConfigErrorListVid,
       "rcDot1agCfmConfigErrorListIfIndex": rcDot1agCfmConfigErrorListIfIndex,
       "rcDot1agCfmConfigErrorListErrorType": rcDot1agCfmConfigErrorListErrorType,
       "rcDot1agCfmMd": rcDot1agCfmMd,
       "rcDot1agCfmMdTableNextIndex": rcDot1agCfmMdTableNextIndex,
       "rcDot1agCfmMdTable": rcDot1agCfmMdTable,
       "rcDot1agCfmMdEntry": rcDot1agCfmMdEntry,
       "rcDot1agCfmMdIndex": rcDot1agCfmMdIndex,
       "rcDot1agCfmMdFormat": rcDot1agCfmMdFormat,
       "rcDot1agCfmMdName": rcDot1agCfmMdName,
       "rcDot1agCfmMdMdLevel": rcDot1agCfmMdMdLevel,
       "rcDot1agCfmMdMhfCreation": rcDot1agCfmMdMhfCreation,
       "rcDot1agCfmMdMhfIdPermission": rcDot1agCfmMdMhfIdPermission,
       "rcDot1agCfmMdMaNextIndex": rcDot1agCfmMdMaNextIndex,
       "rcDot1agCfmMdRowStatus": rcDot1agCfmMdRowStatus,
       "rcDot1agCfmMa": rcDot1agCfmMa,
       "rcDot1agCfmMaNetTable": rcDot1agCfmMaNetTable,
       "rcDot1agCfmMaNetEntry": rcDot1agCfmMaNetEntry,
       "rcDot1agCfmMaIndex": rcDot1agCfmMaIndex,
       "rcDot1agCfmMaNetFormat": rcDot1agCfmMaNetFormat,
       "rcDot1agCfmMaNetName": rcDot1agCfmMaNetName,
       "rcDot1agCfmMaNetCcmInterval": rcDot1agCfmMaNetCcmInterval,
       "rcDot1agCfmMaNetRowStatus": rcDot1agCfmMaNetRowStatus,
       "rcDot1agCfmMaCompTable": rcDot1agCfmMaCompTable,
       "rcDot1agCfmMaCompEntry": rcDot1agCfmMaCompEntry,
       "rcDot1agCfmMaComponentId": rcDot1agCfmMaComponentId,
       "rcDot1agCfmMaCompPrimaryVlanId": rcDot1agCfmMaCompPrimaryVlanId,
       "rcDot1agCfmMaCompMhfCreation": rcDot1agCfmMaCompMhfCreation,
       "rcDot1agCfmMaCompIdPermission": rcDot1agCfmMaCompIdPermission,
       "rcDot1agCfmMaCompNumberOfVids": rcDot1agCfmMaCompNumberOfVids,
       "rcDot1agCfmMaCompRowStatus": rcDot1agCfmMaCompRowStatus,
       "rcDot1agCfmMaMepListTable": rcDot1agCfmMaMepListTable,
       "rcDot1agCfmMaMepListEntry": rcDot1agCfmMaMepListEntry,
       "rcDot1agCfmMaMepListIdentifier": rcDot1agCfmMaMepListIdentifier,
       "rcDot1agCfmMaMepListRowStatus": rcDot1agCfmMaMepListRowStatus,
       "rcDot1agCfmMep": rcDot1agCfmMep,
       "rcDot1agCfmMepTable": rcDot1agCfmMepTable,
       "rcDot1agCfmMepEntry": rcDot1agCfmMepEntry,
       "rcDot1agCfmMepIdentifier": rcDot1agCfmMepIdentifier,
       "rcDot1agCfmMepIfIndex": rcDot1agCfmMepIfIndex,
       "rcDot1agCfmMepDirection": rcDot1agCfmMepDirection,
       "rcDot1agCfmMepPrimaryVid": rcDot1agCfmMepPrimaryVid,
       "rcDot1agCfmMepActive": rcDot1agCfmMepActive,
       "rcDot1agCfmMepFngState": rcDot1agCfmMepFngState,
       "rcDot1agCfmMepCciEnabled": rcDot1agCfmMepCciEnabled,
       "rcDot1agCfmMepCcmLtmPriority": rcDot1agCfmMepCcmLtmPriority,
       "rcDot1agCfmMepMacAddress": rcDot1agCfmMepMacAddress,
       "rcDot1agCfmMepLowPrDef": rcDot1agCfmMepLowPrDef,
       "rcDot1agCfmMepFngAlarmTime": rcDot1agCfmMepFngAlarmTime,
       "rcDot1agCfmMepFngResetTime": rcDot1agCfmMepFngResetTime,
       "rcDot1agCfmMepHighestPrDefect": rcDot1agCfmMepHighestPrDefect,
       "rcDot1agCfmMepDefects": rcDot1agCfmMepDefects,
       "rcDot1agCfmMepErrorCcmLastFailure": rcDot1agCfmMepErrorCcmLastFailure,
       "rcDot1agCfmMepXconCcmLastFailure": rcDot1agCfmMepXconCcmLastFailure,
       "rcDot1agCfmMepCcmSequenceErrors": rcDot1agCfmMepCcmSequenceErrors,
       "rcDot1agCfmMepCciSentCcms": rcDot1agCfmMepCciSentCcms,
       "rcDot1agCfmMepNextLbmTransId": rcDot1agCfmMepNextLbmTransId,
       "rcDot1agCfmMepLbrIn": rcDot1agCfmMepLbrIn,
       "rcDot1agCfmMepLbrInOutOfOrder": rcDot1agCfmMepLbrInOutOfOrder,
       "rcDot1agCfmMepLbrBadMsdu": rcDot1agCfmMepLbrBadMsdu,
       "rcDot1agCfmMepLtmNextSeqNumber": rcDot1agCfmMepLtmNextSeqNumber,
       "rcDot1agCfmMepUnexpLtrIn": rcDot1agCfmMepUnexpLtrIn,
       "rcDot1agCfmMepLbrOut": rcDot1agCfmMepLbrOut,
       "rcDot1agCfmMepTransmitLbmStatus": rcDot1agCfmMepTransmitLbmStatus,
       "rcDot1agCfmMepTransmitLbmDestMacAddress": rcDot1agCfmMepTransmitLbmDestMacAddress,
       "rcDot1agCfmMepTransmitLbmDestMepId": rcDot1agCfmMepTransmitLbmDestMepId,
       "rcDot1agCfmMepTransmitLbmDestIsMepId": rcDot1agCfmMepTransmitLbmDestIsMepId,
       "rcDot1agCfmMepTransmitLbmMessages": rcDot1agCfmMepTransmitLbmMessages,
       "rcDot1agCfmMepTransmitLbmDataTlv": rcDot1agCfmMepTransmitLbmDataTlv,
       "rcDot1agCfmMepTransmitLbmVlanPriority": rcDot1agCfmMepTransmitLbmVlanPriority,
       "rcDot1agCfmMepTransmitLbmVlanDropEnable": rcDot1agCfmMepTransmitLbmVlanDropEnable,
       "rcDot1agCfmMepTransmitLbmResultOK": rcDot1agCfmMepTransmitLbmResultOK,
       "rcDot1agCfmMepTransmitLbmSeqNumber": rcDot1agCfmMepTransmitLbmSeqNumber,
       "rcDot1agCfmMepTransmitLtmStatus": rcDot1agCfmMepTransmitLtmStatus,
       "rcDot1agCfmMepTransmitLtmFlags": rcDot1agCfmMepTransmitLtmFlags,
       "rcDot1agCfmMepTransmitLtmTargetMacAddress": rcDot1agCfmMepTransmitLtmTargetMacAddress,
       "rcDot1agCfmMepTransmitLtmTargetMepId": rcDot1agCfmMepTransmitLtmTargetMepId,
       "rcDot1agCfmMepTransmitLtmTargetIsMepId": rcDot1agCfmMepTransmitLtmTargetIsMepId,
       "rcDot1agCfmMepTransmitLtmTtl": rcDot1agCfmMepTransmitLtmTtl,
       "rcDot1agCfmMepTransmitLtmResult": rcDot1agCfmMepTransmitLtmResult,
       "rcDot1agCfmMepTransmitLtmSeqNumber": rcDot1agCfmMepTransmitLtmSeqNumber,
       "rcDot1agCfmMepTransmitLtmEgressIdentifier": rcDot1agCfmMepTransmitLtmEgressIdentifier,
       "rcDot1agCfmMepRowStatus": rcDot1agCfmMepRowStatus,
       "rcDot1agCfmLtrTable": rcDot1agCfmLtrTable,
       "rcDot1agCfmLtrEntry": rcDot1agCfmLtrEntry,
       "rcDot1agCfmLtrSeqNumber": rcDot1agCfmLtrSeqNumber,
       "rcDot1agCfmLtrReceiveOrder": rcDot1agCfmLtrReceiveOrder,
       "rcDot1agCfmLtrTtl": rcDot1agCfmLtrTtl,
       "rcDot1agCfmLtrForwarded": rcDot1agCfmLtrForwarded,
       "rcDot1agCfmLtrTerminalMep": rcDot1agCfmLtrTerminalMep,
       "rcDot1agCfmLtrLastEgressIdentifier": rcDot1agCfmLtrLastEgressIdentifier,
       "rcDot1agCfmLtrNextEgressIdentifier": rcDot1agCfmLtrNextEgressIdentifier,
       "rcDot1agCfmLtrRelay": rcDot1agCfmLtrRelay,
       "rcDot1agCfmLtrChassisIdSubtype": rcDot1agCfmLtrChassisIdSubtype,
       "rcDot1agCfmLtrChassisId": rcDot1agCfmLtrChassisId,
       "rcDot1agCfmLtrManAddressDomain": rcDot1agCfmLtrManAddressDomain,
       "rcDot1agCfmLtrManAddress": rcDot1agCfmLtrManAddress,
       "rcDot1agCfmLtrIngress": rcDot1agCfmLtrIngress,
       "rcDot1agCfmLtrIngressMac": rcDot1agCfmLtrIngressMac,
       "rcDot1agCfmLtrIngressPortIdSubtype": rcDot1agCfmLtrIngressPortIdSubtype,
       "rcDot1agCfmLtrIngressPortId": rcDot1agCfmLtrIngressPortId,
       "rcDot1agCfmLtrEgress": rcDot1agCfmLtrEgress,
       "rcDot1agCfmLtrEgressMac": rcDot1agCfmLtrEgressMac,
       "rcDot1agCfmLtrEgressPortIdSubtype": rcDot1agCfmLtrEgressPortIdSubtype,
       "rcDot1agCfmLtrEgressPortId": rcDot1agCfmLtrEgressPortId,
       "rcDot1agCfmLtrOrganizationSpecificTlv": rcDot1agCfmLtrOrganizationSpecificTlv,
       "rcDot1agCfmMepDbTable": rcDot1agCfmMepDbTable,
       "rcDot1agCfmMepDbEntry": rcDot1agCfmMepDbEntry,
       "rcDot1agCfmMepDbRMepIdentifier": rcDot1agCfmMepDbRMepIdentifier,
       "rcDot1agCfmMepDbRMepState": rcDot1agCfmMepDbRMepState,
       "rcDot1agCfmMepDbRMepFailedOkTime": rcDot1agCfmMepDbRMepFailedOkTime,
       "rcDot1agCfmMepDbMacAddress": rcDot1agCfmMepDbMacAddress,
       "rcDot1agCfmMepDbRdi": rcDot1agCfmMepDbRdi,
       "rcDot1agCfmMepDbPortStatusTlv": rcDot1agCfmMepDbPortStatusTlv,
       "rcDot1agCfmMepDbInterfaceStatusTlv": rcDot1agCfmMepDbInterfaceStatusTlv,
       "rcDot1agCfmMepDbChassisIdSubtype": rcDot1agCfmMepDbChassisIdSubtype,
       "rcDot1agCfmMepDbChassisId": rcDot1agCfmMepDbChassisId,
       "rcDot1agCfmMepDbManAddressDomain": rcDot1agCfmMepDbManAddressDomain,
       "rcDot1agCfmMepDbManAddress": rcDot1agCfmMepDbManAddress,
       "rcDot1agCfmConformance": rcDot1agCfmConformance,
       "rcDot1agCfmCompliances": rcDot1agCfmCompliances,
       "rcDot1agCfmCompliance": rcDot1agCfmCompliance,
       "rcDot1agCfmGroups": rcDot1agCfmGroups,
       "rcDot1agCfmStackGroup": rcDot1agCfmStackGroup,
       "rcDot1agCfmDefaultMdGroup": rcDot1agCfmDefaultMdGroup,
       "rcDot1agCfmVlanIdGroup": rcDot1agCfmVlanIdGroup,
       "rcDot1agCfmConfigErrorListGroup": rcDot1agCfmConfigErrorListGroup,
       "rcDot1agCfmMdGroup": rcDot1agCfmMdGroup,
       "rcDot1agCfmMaGroup": rcDot1agCfmMaGroup,
       "rcDot1agCfmMepGroup": rcDot1agCfmMepGroup,
       "rcDot1agCfmMepDbGroup": rcDot1agCfmMepDbGroup,
       "rcDot1agCfmNotificationsGroup": rcDot1agCfmNotificationsGroup}
)
