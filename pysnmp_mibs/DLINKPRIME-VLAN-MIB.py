# SNMP MIB module (DLINKPRIME-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:58 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(PortList,
 VlanId,
 VlanIdOrNone,
 dot1vProtocolPortGroupId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIdOrNone",
    "dot1vProtocolPortGroupId")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26)
)
if mibBuilder.loadTexts:
    dlinkPrimeVlanMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions



class Dlink2kVlanList(OctetString):
    """Custom type Dlink2kVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpVlanMIBNotifications_ObjectIdentity = ObjectIdentity
dpVlanMIBNotifications = _DpVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 0)
)
_DpVlanMIBObjects_ObjectIdentity = ObjectIdentity
dpVlanMIBObjects = _DpVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1)
)
_DpVlanPortIfCtrlTable_Object = MibTable
dpVlanPortIfCtrlTable = _DpVlanPortIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1)
)
if mibBuilder.loadTexts:
    dpVlanPortIfCtrlTable.setStatus("current")
_DpVlanPortIfCtrlEntry_Object = MibTableRow
dpVlanPortIfCtrlEntry = _DpVlanPortIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1)
)
dpVlanPortIfCtrlEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    dpVlanPortIfCtrlEntry.setStatus("current")


class _DpVlanPortIfMode_Type(Integer32):
    """Custom type dpVlanPortIfMode based on Integer32"""
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
        *(("access", 1),
          ("hybrid", 2),
          ("trunk", 3),
          ("dot1qTunnel", 4),
          ("privateVlanHost", 5),
          ("privateVlanPromiscuous", 6),
          ("privateVlanTrunkPromiscuous", 7),
          ("privateVlanTrunkSecondary", 8))
    )


_DpVlanPortIfMode_Type.__name__ = "Integer32"
_DpVlanPortIfMode_Object = MibTableColumn
dpVlanPortIfMode = _DpVlanPortIfMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 1),
    _DpVlanPortIfMode_Type()
)
dpVlanPortIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfMode.setStatus("current")
_DpVlanPortIfTrunkNativeVlanTagged_Type = TruthValue
_DpVlanPortIfTrunkNativeVlanTagged_Object = MibTableColumn
dpVlanPortIfTrunkNativeVlanTagged = _DpVlanPortIfTrunkNativeVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 2),
    _DpVlanPortIfTrunkNativeVlanTagged_Type()
)
dpVlanPortIfTrunkNativeVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfTrunkNativeVlanTagged.setStatus("current")


class _DpVlanPortIfAcceptableFrameTypes_Type(Integer32):
    """Custom type dpVlanPortIfAcceptableFrameTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitUntaggedAndPriority", 2),
          ("admitTagged", 3))
    )


_DpVlanPortIfAcceptableFrameTypes_Type.__name__ = "Integer32"
_DpVlanPortIfAcceptableFrameTypes_Object = MibTableColumn
dpVlanPortIfAcceptableFrameTypes = _DpVlanPortIfAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 3),
    _DpVlanPortIfAcceptableFrameTypes_Type()
)
dpVlanPortIfAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfAcceptableFrameTypes.setStatus("current")
_DpVlanPortIfTagAllowVlanLstFirst2K_Type = Dlink2kVlanList
_DpVlanPortIfTagAllowVlanLstFirst2K_Object = MibTableColumn
dpVlanPortIfTagAllowVlanLstFirst2K = _DpVlanPortIfTagAllowVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 4),
    _DpVlanPortIfTagAllowVlanLstFirst2K_Type()
)
dpVlanPortIfTagAllowVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfTagAllowVlanLstFirst2K.setStatus("current")
_DpVlanPortIfTagAllowVlanLstSecond2K_Type = Dlink2kVlanList
_DpVlanPortIfTagAllowVlanLstSecond2K_Object = MibTableColumn
dpVlanPortIfTagAllowVlanLstSecond2K = _DpVlanPortIfTagAllowVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 5),
    _DpVlanPortIfTagAllowVlanLstSecond2K_Type()
)
dpVlanPortIfTagAllowVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfTagAllowVlanLstSecond2K.setStatus("current")
_DpVlanPortIfUntagAllowVlanLstFirst2K_Type = Dlink2kVlanList
_DpVlanPortIfUntagAllowVlanLstFirst2K_Object = MibTableColumn
dpVlanPortIfUntagAllowVlanLstFirst2K = _DpVlanPortIfUntagAllowVlanLstFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 6),
    _DpVlanPortIfUntagAllowVlanLstFirst2K_Type()
)
dpVlanPortIfUntagAllowVlanLstFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfUntagAllowVlanLstFirst2K.setStatus("current")
_DpVlanPortIfUntagAllowVlanLstSecond2K_Type = Dlink2kVlanList
_DpVlanPortIfUntagAllowVlanLstSecond2K_Object = MibTableColumn
dpVlanPortIfUntagAllowVlanLstSecond2K = _DpVlanPortIfUntagAllowVlanLstSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 1, 1, 7),
    _DpVlanPortIfUntagAllowVlanLstSecond2K_Type()
)
dpVlanPortIfUntagAllowVlanLstSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortIfUntagAllowVlanLstSecond2K.setStatus("current")
_DpVlanAsymVlanStateEnabled_Type = TruthValue
_DpVlanAsymVlanStateEnabled_Object = MibScalar
dpVlanAsymVlanStateEnabled = _DpVlanAsymVlanStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 2),
    _DpVlanAsymVlanStateEnabled_Type()
)
dpVlanAsymVlanStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanAsymVlanStateEnabled.setStatus("current")
_DpVlanManagementVlanGlobal_ObjectIdentity = ObjectIdentity
dpVlanManagementVlanGlobal = _DpVlanManagementVlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 3)
)
_DpVlanManagementVlanEnabled_Type = TruthValue
_DpVlanManagementVlanEnabled_Object = MibScalar
dpVlanManagementVlanEnabled = _DpVlanManagementVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 3, 1),
    _DpVlanManagementVlanEnabled_Type()
)
dpVlanManagementVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanManagementVlanEnabled.setStatus("current")


class _DpVlanManagementVlanId_Type(VlanIdOrNone):
    """Custom type dpVlanManagementVlanId based on VlanIdOrNone"""
    defaultValue = 0


_DpVlanManagementVlanId_Type.__name__ = "VlanIdOrNone"
_DpVlanManagementVlanId_Object = MibScalar
dpVlanManagementVlanId = _DpVlanManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 3, 2),
    _DpVlanManagementVlanId_Type()
)
dpVlanManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanManagementVlanId.setStatus("current")
_DpVlanPortBasedVlan_ObjectIdentity = ObjectIdentity
dpVlanPortBasedVlan = _DpVlanPortBasedVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4)
)
_DpVlanPortBasedVlanEnabled_Type = TruthValue
_DpVlanPortBasedVlanEnabled_Object = MibScalar
dpVlanPortBasedVlanEnabled = _DpVlanPortBasedVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 1),
    _DpVlanPortBasedVlanEnabled_Type()
)
dpVlanPortBasedVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVlanPortBasedVlanEnabled.setStatus("current")
_DpPortBasedVlanTable_Object = MibTable
dpPortBasedVlanTable = _DpPortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dpPortBasedVlanTable.setStatus("current")
_DpPortBasedVlanEntry_Object = MibTableRow
dpPortBasedVlanEntry = _DpPortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 2, 1)
)
dpPortBasedVlanEntry.setIndexNames(
    (0, "DLINKPRIME-VLAN-MIB", "dpPortBasedVlanIndex"),
)
if mibBuilder.loadTexts:
    dpPortBasedVlanEntry.setStatus("current")
_DpPortBasedVlanIndex_Type = Integer32
_DpPortBasedVlanIndex_Object = MibTableColumn
dpPortBasedVlanIndex = _DpPortBasedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 2, 1, 1),
    _DpPortBasedVlanIndex_Type()
)
dpPortBasedVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpPortBasedVlanIndex.setStatus("current")
_DpPortBasedVlanEgressPorts_Type = PortList
_DpPortBasedVlanEgressPorts_Object = MibTableColumn
dpPortBasedVlanEgressPorts = _DpPortBasedVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 2, 1, 2),
    _DpPortBasedVlanEgressPorts_Type()
)
dpPortBasedVlanEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpPortBasedVlanEgressPorts.setStatus("current")
_DpPortBasedVlanRowStatus_Type = RowStatus
_DpPortBasedVlanRowStatus_Object = MibTableColumn
dpPortBasedVlanRowStatus = _DpPortBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 1, 4, 2, 1, 3),
    _DpPortBasedVlanRowStatus_Type()
)
dpPortBasedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpPortBasedVlanRowStatus.setStatus("current")
_DpVlanMIBConformance_ObjectIdentity = ObjectIdentity
dpVlanMIBConformance = _DpVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2)
)
_DpVlanCompliances_ObjectIdentity = ObjectIdentity
dpVlanCompliances = _DpVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2, 1)
)
_DpVlanGroups_ObjectIdentity = ObjectIdentity
dpVlanGroups = _DpVlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2, 2)
)

# Managed Objects groups

dpVlanIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2, 2, 1)
)
dpVlanIfCfgGroup.setObjects(
      *(("DLINKPRIME-VLAN-MIB", "dpVlanPortIfMode"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfTrunkNativeVlanTagged"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfAcceptableFrameTypes"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfTagAllowVlanLstFirst2K"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfTagAllowVlanLstSecond2K"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfUntagAllowVlanLstFirst2K"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanPortIfUntagAllowVlanLstSecond2K"))
)
if mibBuilder.loadTexts:
    dpVlanIfCfgGroup.setStatus("current")

dpVlanAsymmetricVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2, 2, 2)
)
dpVlanAsymmetricVlanCfgGroup.setObjects(
    ("DLINKPRIME-VLAN-MIB", "dpVlanAsymVlanStateEnabled")
)
if mibBuilder.loadTexts:
    dpVlanAsymmetricVlanCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 26, 2, 1, 1)
)
dpVlanCompliance.setObjects(
      *(("DLINKPRIME-VLAN-MIB", "dpVlanIfCfgGroup"),
        ("DLINKPRIME-VLAN-MIB", "dpVlanAsymmetricVlanCfgGroup"))
)
if mibBuilder.loadTexts:
    dpVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-VLAN-MIB",
    **{"Dlink2kVlanList": Dlink2kVlanList,
       "dlinkPrimeVlanMIB": dlinkPrimeVlanMIB,
       "dpVlanMIBNotifications": dpVlanMIBNotifications,
       "dpVlanMIBObjects": dpVlanMIBObjects,
       "dpVlanPortIfCtrlTable": dpVlanPortIfCtrlTable,
       "dpVlanPortIfCtrlEntry": dpVlanPortIfCtrlEntry,
       "dpVlanPortIfMode": dpVlanPortIfMode,
       "dpVlanPortIfTrunkNativeVlanTagged": dpVlanPortIfTrunkNativeVlanTagged,
       "dpVlanPortIfAcceptableFrameTypes": dpVlanPortIfAcceptableFrameTypes,
       "dpVlanPortIfTagAllowVlanLstFirst2K": dpVlanPortIfTagAllowVlanLstFirst2K,
       "dpVlanPortIfTagAllowVlanLstSecond2K": dpVlanPortIfTagAllowVlanLstSecond2K,
       "dpVlanPortIfUntagAllowVlanLstFirst2K": dpVlanPortIfUntagAllowVlanLstFirst2K,
       "dpVlanPortIfUntagAllowVlanLstSecond2K": dpVlanPortIfUntagAllowVlanLstSecond2K,
       "dpVlanAsymVlanStateEnabled": dpVlanAsymVlanStateEnabled,
       "dpVlanManagementVlanGlobal": dpVlanManagementVlanGlobal,
       "dpVlanManagementVlanEnabled": dpVlanManagementVlanEnabled,
       "dpVlanManagementVlanId": dpVlanManagementVlanId,
       "dpVlanPortBasedVlan": dpVlanPortBasedVlan,
       "dpVlanPortBasedVlanEnabled": dpVlanPortBasedVlanEnabled,
       "dpPortBasedVlanTable": dpPortBasedVlanTable,
       "dpPortBasedVlanEntry": dpPortBasedVlanEntry,
       "dpPortBasedVlanIndex": dpPortBasedVlanIndex,
       "dpPortBasedVlanEgressPorts": dpPortBasedVlanEgressPorts,
       "dpPortBasedVlanRowStatus": dpPortBasedVlanRowStatus,
       "dpVlanMIBConformance": dpVlanMIBConformance,
       "dpVlanCompliances": dpVlanCompliances,
       "dpVlanCompliance": dpVlanCompliance,
       "dpVlanGroups": dpVlanGroups,
       "dpVlanIfCfgGroup": dpVlanIfCfgGroup,
       "dpVlanAsymmetricVlanCfgGroup": dpVlanAsymmetricVlanCfgGroup}
)
