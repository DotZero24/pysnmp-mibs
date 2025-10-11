# SNMP MIB module (FDRY-MPLS-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FDRY-MPLS-L2VPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:37 2025
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

(pwEnetPwInstance,) = mibBuilder.importSymbols(
    "FOUNDRY-PW-ENET-STD-MIB",
    "pwEnetPwInstance")

(fdryPwServiceType,
 pwID,
 pwIndex,
 pwName) = mibBuilder.importSymbols(
    "FOUNDRY-PW-STD-MIB",
    "fdryPwServiceType",
    "pwID",
    "pwIndex",
    "pwName")

(PwOperStatusTC,
 PwVlanCfg) = mibBuilder.importSymbols(
    "FOUNDRY-PW-TC-STD-MIB",
    "PwOperStatusTC",
    "PwVlanCfg")

(snMpls,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snMpls")

(VlanTagMode,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "VlanTagMode")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vplsConfigEntry,
 vplsConfigIndex,
 vplsConfigName) = mibBuilder.importSymbols(
    "VPLS-GENERIC-DRAFT-01-MIB",
    "vplsConfigEntry",
    "vplsConfigIndex",
    "vplsConfigName")


# MODULE-IDENTITY

fdryMplsL2VpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    fdryMplsL2VpnMIB.setRevisions(
        ("2008-02-07 00:00",
         "2017-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsServiceType(TextualConvention, Integer32):
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
        *(("vll", 1),
          ("vllLocal", 2),
          ("vpls", 3))
    )



class AdminStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )



class ClassOfService(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



class Layer2StateTC(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("preforwarding", 5),
          ("forwarding", 6))
    )



# MIB Managed Objects in the order of their OIDs

_FdryMplsVpnNotifications_ObjectIdentity = ObjectIdentity
fdryMplsVpnNotifications = _FdryMplsVpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0)
)
_FdryMplsVllInfo_ObjectIdentity = ObjectIdentity
fdryMplsVllInfo = _FdryMplsVllInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1)
)
_FdryVllEndPointTable_Object = MibTable
fdryVllEndPointTable = _FdryVllEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fdryVllEndPointTable.setStatus("current")
_FdryVllEndPointEntry_Object = MibTableRow
fdryVllEndPointEntry = _FdryVllEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1)
)
fdryVllEndPointEntry.setIndexNames(
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVllEndPointServiceType"),
    (0, "FOUNDRY-PW-STD-MIB", "pwIndex"),
    (0, "FOUNDRY-PW-ENET-STD-MIB", "pwEnetPwInstance"),
)
if mibBuilder.loadTexts:
    fdryVllEndPointEntry.setStatus("current")
_FdryVllEndPointServiceType_Type = MplsServiceType
_FdryVllEndPointServiceType_Object = MibTableColumn
fdryVllEndPointServiceType = _FdryVllEndPointServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 1),
    _FdryVllEndPointServiceType_Type()
)
fdryVllEndPointServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVllEndPointServiceType.setStatus("current")
_FdryVllEndPointVlanTagMode_Type = VlanTagMode
_FdryVllEndPointVlanTagMode_Object = MibTableColumn
fdryVllEndPointVlanTagMode = _FdryVllEndPointVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 2),
    _FdryVllEndPointVlanTagMode_Type()
)
fdryVllEndPointVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointVlanTagMode.setStatus("current")


class _FdryVllEndPointClassOfService_Type(ClassOfService):
    """Custom type fdryVllEndPointClassOfService based on ClassOfService"""
    defaultValue = 0


_FdryVllEndPointClassOfService_Type.__name__ = "ClassOfService"
_FdryVllEndPointClassOfService_Object = MibTableColumn
fdryVllEndPointClassOfService = _FdryVllEndPointClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 3),
    _FdryVllEndPointClassOfService_Type()
)
fdryVllEndPointClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointClassOfService.setStatus("current")
_FdryVllEndPointInHCPkts_Type = Counter64
_FdryVllEndPointInHCPkts_Object = MibTableColumn
fdryVllEndPointInHCPkts = _FdryVllEndPointInHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 4),
    _FdryVllEndPointInHCPkts_Type()
)
fdryVllEndPointInHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointInHCPkts.setStatus("current")
_FdryVllEndPointOutHCPkts_Type = Counter64
_FdryVllEndPointOutHCPkts_Object = MibTableColumn
fdryVllEndPointOutHCPkts = _FdryVllEndPointOutHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 5),
    _FdryVllEndPointOutHCPkts_Type()
)
fdryVllEndPointOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOutHCPkts.setStatus("current")
_FdryVllEndPointAdminStatus_Type = AdminStatus
_FdryVllEndPointAdminStatus_Object = MibTableColumn
fdryVllEndPointAdminStatus = _FdryVllEndPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 6),
    _FdryVllEndPointAdminStatus_Type()
)
fdryVllEndPointAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointAdminStatus.setStatus("current")
_FdryVllEndPointOperStatus_Type = PwOperStatusTC
_FdryVllEndPointOperStatus_Object = MibTableColumn
fdryVllEndPointOperStatus = _FdryVllEndPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 7),
    _FdryVllEndPointOperStatus_Type()
)
fdryVllEndPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOperStatus.setStatus("current")
_FdryVllEndPointRowStatus_Type = RowStatus
_FdryVllEndPointRowStatus_Object = MibTableColumn
fdryVllEndPointRowStatus = _FdryVllEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 8),
    _FdryVllEndPointRowStatus_Type()
)
fdryVllEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointRowStatus.setStatus("current")


class _FdryVllEndPointInnerVlanId_Type(PwVlanCfg):
    """Custom type fdryVllEndPointInnerVlanId based on PwVlanCfg"""
    defaultValue = 0


_FdryVllEndPointInnerVlanId_Type.__name__ = "PwVlanCfg"
_FdryVllEndPointInnerVlanId_Object = MibTableColumn
fdryVllEndPointInnerVlanId = _FdryVllEndPointInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 9),
    _FdryVllEndPointInnerVlanId_Type()
)
fdryVllEndPointInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVllEndPointInnerVlanId.setStatus("current")
_FdryVllEndPointInHCOctets_Type = Counter64
_FdryVllEndPointInHCOctets_Object = MibTableColumn
fdryVllEndPointInHCOctets = _FdryVllEndPointInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 10),
    _FdryVllEndPointInHCOctets_Type()
)
fdryVllEndPointInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointInHCOctets.setStatus("current")
_FdryVllEndPointOutHCOctets_Type = Counter64
_FdryVllEndPointOutHCOctets_Object = MibTableColumn
fdryVllEndPointOutHCOctets = _FdryVllEndPointOutHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 1, 1, 1, 11),
    _FdryVllEndPointOutHCOctets_Type()
)
fdryVllEndPointOutHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVllEndPointOutHCOctets.setStatus("current")
_FdryMplsVplsInfo_ObjectIdentity = ObjectIdentity
fdryMplsVplsInfo = _FdryMplsVplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2)
)
_FdryVplsEndPointTable_Object = MibTable
fdryVplsEndPointTable = _FdryVplsEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fdryVplsEndPointTable.setStatus("deprecated")
_FdryVplsEndPointEntry_Object = MibTableRow
fdryVplsEndPointEntry = _FdryVplsEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1)
)
fdryVplsEndPointEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointPortVlan"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPointIfIndex"),
)
if mibBuilder.loadTexts:
    fdryVplsEndPointEntry.setStatus("deprecated")
_FdryVplsEndPointPortVlan_Type = PwVlanCfg
_FdryVplsEndPointPortVlan_Object = MibTableColumn
fdryVplsEndPointPortVlan = _FdryVplsEndPointPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 1),
    _FdryVplsEndPointPortVlan_Type()
)
fdryVplsEndPointPortVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPointPortVlan.setStatus("deprecated")
_FdryVplsEndPointIfIndex_Type = InterfaceIndex
_FdryVplsEndPointIfIndex_Object = MibTableColumn
fdryVplsEndPointIfIndex = _FdryVplsEndPointIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 2),
    _FdryVplsEndPointIfIndex_Type()
)
fdryVplsEndPointIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPointIfIndex.setStatus("deprecated")
_FdryVplsEndPointVlanTagMode_Type = VlanTagMode
_FdryVplsEndPointVlanTagMode_Object = MibTableColumn
fdryVplsEndPointVlanTagMode = _FdryVplsEndPointVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 3),
    _FdryVplsEndPointVlanTagMode_Type()
)
fdryVplsEndPointVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointVlanTagMode.setStatus("deprecated")
_FdryVplsEndPointOutHCPkts_Type = Counter64
_FdryVplsEndPointOutHCPkts_Object = MibTableColumn
fdryVplsEndPointOutHCPkts = _FdryVplsEndPointOutHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 4),
    _FdryVplsEndPointOutHCPkts_Type()
)
fdryVplsEndPointOutHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointOutHCPkts.setStatus("deprecated")


class _FdryVplsEndPointState_Type(Integer32):
    """Custom type fdryVplsEndPointState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("forwarding", 5))
    )


_FdryVplsEndPointState_Type.__name__ = "Integer32"
_FdryVplsEndPointState_Object = MibTableColumn
fdryVplsEndPointState = _FdryVplsEndPointState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 5),
    _FdryVplsEndPointState_Type()
)
fdryVplsEndPointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointState.setStatus("deprecated")
_FdryVplsEndPointAdminStatus_Type = AdminStatus
_FdryVplsEndPointAdminStatus_Object = MibTableColumn
fdryVplsEndPointAdminStatus = _FdryVplsEndPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 6),
    _FdryVplsEndPointAdminStatus_Type()
)
fdryVplsEndPointAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointAdminStatus.setStatus("deprecated")
_FdryVplsEndPointOperStatus_Type = PwOperStatusTC
_FdryVplsEndPointOperStatus_Object = MibTableColumn
fdryVplsEndPointOperStatus = _FdryVplsEndPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 7),
    _FdryVplsEndPointOperStatus_Type()
)
fdryVplsEndPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointOperStatus.setStatus("deprecated")
_FdryVplsEndPointRowStatus_Type = RowStatus
_FdryVplsEndPointRowStatus_Object = MibTableColumn
fdryVplsEndPointRowStatus = _FdryVplsEndPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 8),
    _FdryVplsEndPointRowStatus_Type()
)
fdryVplsEndPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPointRowStatus.setStatus("deprecated")
_FdryVplsEndPointInHCOctets_Type = Counter64
_FdryVplsEndPointInHCOctets_Object = MibTableColumn
fdryVplsEndPointInHCOctets = _FdryVplsEndPointInHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 1, 1, 9),
    _FdryVplsEndPointInHCOctets_Type()
)
fdryVplsEndPointInHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPointInHCOctets.setStatus("deprecated")
_FdryVplsTable_Object = MibTable
fdryVplsTable = _FdryVplsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fdryVplsTable.setStatus("current")
_FdryVplsEntry_Object = MibTableRow
fdryVplsEntry = _FdryVplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fdryVplsEntry.setStatus("current")


class _FdryVplsClassOfService_Type(ClassOfService):
    """Custom type fdryVplsClassOfService based on ClassOfService"""
    defaultValue = 0


_FdryVplsClassOfService_Type.__name__ = "ClassOfService"
_FdryVplsClassOfService_Object = MibTableColumn
fdryVplsClassOfService = _FdryVplsClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 1),
    _FdryVplsClassOfService_Type()
)
fdryVplsClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsClassOfService.setStatus("current")
_FdryVplsMaxMacLearned_Type = Unsigned32
_FdryVplsMaxMacLearned_Object = MibTableColumn
fdryVplsMaxMacLearned = _FdryVplsMaxMacLearned_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 2),
    _FdryVplsMaxMacLearned_Type()
)
fdryVplsMaxMacLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsMaxMacLearned.setStatus("current")
_FdryVplsClearMac_Type = TruthValue
_FdryVplsClearMac_Object = MibTableColumn
fdryVplsClearMac = _FdryVplsClearMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 3),
    _FdryVplsClearMac_Type()
)
fdryVplsClearMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsClearMac.setStatus("current")
_FdryVplsVcId_Type = Unsigned32
_FdryVplsVcId_Object = MibTableColumn
fdryVplsVcId = _FdryVplsVcId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 2, 1, 4),
    _FdryVplsVcId_Type()
)
fdryVplsVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsVcId.setStatus("current")
_FdryVplsEndPoint2Table_Object = MibTable
fdryVplsEndPoint2Table = _FdryVplsEndPoint2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3)
)
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Table.setStatus("current")
_FdryVplsEndPoint2Entry_Object = MibTableRow
fdryVplsEndPoint2Entry = _FdryVplsEndPoint2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1)
)
fdryVplsEndPoint2Entry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigIndex"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2VlanId"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTagType"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2InnerTag"),
    (0, "FDRY-MPLS-L2VPN-MIB", "fdryVplsEndPoint2IfIndex"),
)
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Entry.setStatus("current")
_FdryVplsEndPoint2VlanId_Type = PwVlanCfg
_FdryVplsEndPoint2VlanId_Object = MibTableColumn
fdryVplsEndPoint2VlanId = _FdryVplsEndPoint2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 1),
    _FdryVplsEndPoint2VlanId_Type()
)
fdryVplsEndPoint2VlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2VlanId.setStatus("current")


class _FdryVplsEndPoint2InnerTagType_Type(Integer32):
    """Custom type fdryVplsEndPoint2InnerTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("innerVlan", 2),
          ("isid", 3))
    )


_FdryVplsEndPoint2InnerTagType_Type.__name__ = "Integer32"
_FdryVplsEndPoint2InnerTagType_Object = MibTableColumn
fdryVplsEndPoint2InnerTagType = _FdryVplsEndPoint2InnerTagType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 2),
    _FdryVplsEndPoint2InnerTagType_Type()
)
fdryVplsEndPoint2InnerTagType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InnerTagType.setStatus("current")
_FdryVplsEndPoint2InnerTag_Type = Unsigned32
_FdryVplsEndPoint2InnerTag_Object = MibTableColumn
fdryVplsEndPoint2InnerTag = _FdryVplsEndPoint2InnerTag_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 3),
    _FdryVplsEndPoint2InnerTag_Type()
)
fdryVplsEndPoint2InnerTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InnerTag.setStatus("current")
_FdryVplsEndPoint2IfIndex_Type = InterfaceIndex
_FdryVplsEndPoint2IfIndex_Object = MibTableColumn
fdryVplsEndPoint2IfIndex = _FdryVplsEndPoint2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 4),
    _FdryVplsEndPoint2IfIndex_Type()
)
fdryVplsEndPoint2IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2IfIndex.setStatus("current")
_FdryVplsEndPoint2VlanTagMode_Type = VlanTagMode
_FdryVplsEndPoint2VlanTagMode_Object = MibTableColumn
fdryVplsEndPoint2VlanTagMode = _FdryVplsEndPoint2VlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 5),
    _FdryVplsEndPoint2VlanTagMode_Type()
)
fdryVplsEndPoint2VlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2VlanTagMode.setStatus("current")
_FdryVplsEndPoint2InHCOctets_Type = Counter64
_FdryVplsEndPoint2InHCOctets_Object = MibTableColumn
fdryVplsEndPoint2InHCOctets = _FdryVplsEndPoint2InHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 6),
    _FdryVplsEndPoint2InHCOctets_Type()
)
fdryVplsEndPoint2InHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2InHCOctets.setStatus("current")
_FdryVplsEndPoint2Layer2State_Type = Layer2StateTC
_FdryVplsEndPoint2Layer2State_Object = MibTableColumn
fdryVplsEndPoint2Layer2State = _FdryVplsEndPoint2Layer2State_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 7),
    _FdryVplsEndPoint2Layer2State_Type()
)
fdryVplsEndPoint2Layer2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2Layer2State.setStatus("current")
_FdryVplsEndPoint2OperStatus_Type = PwOperStatusTC
_FdryVplsEndPoint2OperStatus_Object = MibTableColumn
fdryVplsEndPoint2OperStatus = _FdryVplsEndPoint2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 8),
    _FdryVplsEndPoint2OperStatus_Type()
)
fdryVplsEndPoint2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2OperStatus.setStatus("current")
_FdryVplsEndPoint2RowStatus_Type = RowStatus
_FdryVplsEndPoint2RowStatus_Object = MibTableColumn
fdryVplsEndPoint2RowStatus = _FdryVplsEndPoint2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 2, 3, 1, 9),
    _FdryVplsEndPoint2RowStatus_Type()
)
fdryVplsEndPoint2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryVplsEndPoint2RowStatus.setStatus("current")
vplsConfigEntry.registerAugmentions(
    ("FDRY-MPLS-L2VPN-MIB",
     "fdryVplsEntry")
)
fdryVplsEntry.setIndexNames(*vplsConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fdryVplsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 1)
)
fdryVplsCreated.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigName"),
        ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
)
if mibBuilder.loadTexts:
    fdryVplsCreated.setStatus(
        "current"
    )

fdryVplsDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 2)
)
fdryVplsDeleted.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "vplsConfigName"),
        ("FDRY-MPLS-L2VPN-MIB", "fdryVplsVcId"))
)
if mibBuilder.loadTexts:
    fdryVplsDeleted.setStatus(
        "current"
    )

fdryPwCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 2, 0, 3)
)
fdryPwCreated.setObjects(
      *(("FOUNDRY-PW-STD-MIB", "fdryPwServiceType"),
        ("FOUNDRY-PW-STD-MIB", "pwName"),
        ("FOUNDRY-PW-STD-MIB", "pwID"))
)
if mibBuilder.loadTexts:
    fdryPwCreated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-MPLS-L2VPN-MIB",
    **{"MplsServiceType": MplsServiceType,
       "AdminStatus": AdminStatus,
       "ClassOfService": ClassOfService,
       "Layer2StateTC": Layer2StateTC,
       "fdryMplsL2VpnMIB": fdryMplsL2VpnMIB,
       "fdryMplsVpnNotifications": fdryMplsVpnNotifications,
       "fdryVplsCreated": fdryVplsCreated,
       "fdryVplsDeleted": fdryVplsDeleted,
       "fdryPwCreated": fdryPwCreated,
       "fdryMplsVllInfo": fdryMplsVllInfo,
       "fdryVllEndPointTable": fdryVllEndPointTable,
       "fdryVllEndPointEntry": fdryVllEndPointEntry,
       "fdryVllEndPointServiceType": fdryVllEndPointServiceType,
       "fdryVllEndPointVlanTagMode": fdryVllEndPointVlanTagMode,
       "fdryVllEndPointClassOfService": fdryVllEndPointClassOfService,
       "fdryVllEndPointInHCPkts": fdryVllEndPointInHCPkts,
       "fdryVllEndPointOutHCPkts": fdryVllEndPointOutHCPkts,
       "fdryVllEndPointAdminStatus": fdryVllEndPointAdminStatus,
       "fdryVllEndPointOperStatus": fdryVllEndPointOperStatus,
       "fdryVllEndPointRowStatus": fdryVllEndPointRowStatus,
       "fdryVllEndPointInnerVlanId": fdryVllEndPointInnerVlanId,
       "fdryVllEndPointInHCOctets": fdryVllEndPointInHCOctets,
       "fdryVllEndPointOutHCOctets": fdryVllEndPointOutHCOctets,
       "fdryMplsVplsInfo": fdryMplsVplsInfo,
       "fdryVplsEndPointTable": fdryVplsEndPointTable,
       "fdryVplsEndPointEntry": fdryVplsEndPointEntry,
       "fdryVplsEndPointPortVlan": fdryVplsEndPointPortVlan,
       "fdryVplsEndPointIfIndex": fdryVplsEndPointIfIndex,
       "fdryVplsEndPointVlanTagMode": fdryVplsEndPointVlanTagMode,
       "fdryVplsEndPointOutHCPkts": fdryVplsEndPointOutHCPkts,
       "fdryVplsEndPointState": fdryVplsEndPointState,
       "fdryVplsEndPointAdminStatus": fdryVplsEndPointAdminStatus,
       "fdryVplsEndPointOperStatus": fdryVplsEndPointOperStatus,
       "fdryVplsEndPointRowStatus": fdryVplsEndPointRowStatus,
       "fdryVplsEndPointInHCOctets": fdryVplsEndPointInHCOctets,
       "fdryVplsTable": fdryVplsTable,
       "fdryVplsEntry": fdryVplsEntry,
       "fdryVplsClassOfService": fdryVplsClassOfService,
       "fdryVplsMaxMacLearned": fdryVplsMaxMacLearned,
       "fdryVplsClearMac": fdryVplsClearMac,
       "fdryVplsVcId": fdryVplsVcId,
       "fdryVplsEndPoint2Table": fdryVplsEndPoint2Table,
       "fdryVplsEndPoint2Entry": fdryVplsEndPoint2Entry,
       "fdryVplsEndPoint2VlanId": fdryVplsEndPoint2VlanId,
       "fdryVplsEndPoint2InnerTagType": fdryVplsEndPoint2InnerTagType,
       "fdryVplsEndPoint2InnerTag": fdryVplsEndPoint2InnerTag,
       "fdryVplsEndPoint2IfIndex": fdryVplsEndPoint2IfIndex,
       "fdryVplsEndPoint2VlanTagMode": fdryVplsEndPoint2VlanTagMode,
       "fdryVplsEndPoint2InHCOctets": fdryVplsEndPoint2InHCOctets,
       "fdryVplsEndPoint2Layer2State": fdryVplsEndPoint2Layer2State,
       "fdryVplsEndPoint2OperStatus": fdryVplsEndPoint2OperStatus,
       "fdryVplsEndPoint2RowStatus": fdryVplsEndPoint2RowStatus}
)
