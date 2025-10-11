# SNMP MIB module (INFINERA-TOPONODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TOPONODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:47 2025
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

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(infnNE,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "infnNE")

(InfnNeType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnNeType")

(SnmpEngineID,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpEngineID")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

topoNodeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TopoNodeTable_Object = MibTable
topoNodeTable = _TopoNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    topoNodeTable.setStatus("current")
_TopoNodeEntry_Object = MibTableRow
topoNodeEntry = _TopoNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1)
)
topoNodeEntry.setIndexNames(
    (0, "INFINERA-TOPONODE-MIB", "topoNodeRouterId"),
)
if mibBuilder.loadTexts:
    topoNodeEntry.setStatus("current")
_TopoNodeMeName_Type = DisplayString
_TopoNodeMeName_Object = MibTableColumn
topoNodeMeName = _TopoNodeMeName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 1),
    _TopoNodeMeName_Type()
)
topoNodeMeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeMeName.setStatus("current")
_TopoNodeNodeId_Type = DisplayString
_TopoNodeNodeId_Object = MibTableColumn
topoNodeNodeId = _TopoNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 2),
    _TopoNodeNodeId_Type()
)
topoNodeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeNodeId.setStatus("current")
_TopoNodeNeType_Type = InfnNeType
_TopoNodeNeType_Object = MibTableColumn
topoNodeNeType = _TopoNodeNeType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 3),
    _TopoNodeNeType_Type()
)
topoNodeNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeNeType.setStatus("current")
_TopoNodeRouterId_Type = InetAddressIPv4
_TopoNodeRouterId_Object = MibTableColumn
topoNodeRouterId = _TopoNodeRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 4),
    _TopoNodeRouterId_Type()
)
topoNodeRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeRouterId.setStatus("current")
_TopoNodeDcnIp_Type = InetAddressIPv4
_TopoNodeDcnIp_Object = MibTableColumn
topoNodeDcnIp = _TopoNodeDcnIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 5),
    _TopoNodeDcnIp_Type()
)
topoNodeDcnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnIp.setStatus("current")
_TopoNodeDcnIpNetMask_Type = InetAddressIPv4
_TopoNodeDcnIpNetMask_Object = MibTableColumn
topoNodeDcnIpNetMask = _TopoNodeDcnIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 6),
    _TopoNodeDcnIpNetMask_Type()
)
topoNodeDcnIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnIpNetMask.setStatus("current")
_TopoNodeDcnEnabled_Type = TruthValue
_TopoNodeDcnEnabled_Object = MibTableColumn
topoNodeDcnEnabled = _TopoNodeDcnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 7),
    _TopoNodeDcnEnabled_Type()
)
topoNodeDcnEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnEnabled.setStatus("current")
_TopoNodeGatewayProxyEnabled_Type = TruthValue
_TopoNodeGatewayProxyEnabled_Object = MibTableColumn
topoNodeGatewayProxyEnabled = _TopoNodeGatewayProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 8),
    _TopoNodeGatewayProxyEnabled_Type()
)
topoNodeGatewayProxyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeGatewayProxyEnabled.setStatus("current")
_TopoNodeXmlPortId_Type = Integer32
_TopoNodeXmlPortId_Object = MibTableColumn
topoNodeXmlPortId = _TopoNodeXmlPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 9),
    _TopoNodeXmlPortId_Type()
)
topoNodeXmlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeXmlPortId.setStatus("current")
_TopoNodeTl1PortId_Type = Integer32
_TopoNodeTl1PortId_Object = MibTableColumn
topoNodeTl1PortId = _TopoNodeTl1PortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 10),
    _TopoNodeTl1PortId_Type()
)
topoNodeTl1PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeTl1PortId.setStatus("current")
_TopoNodeXmlProxyPort_Type = Integer32
_TopoNodeXmlProxyPort_Object = MibTableColumn
topoNodeXmlProxyPort = _TopoNodeXmlProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 11),
    _TopoNodeXmlProxyPort_Type()
)
topoNodeXmlProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeXmlProxyPort.setStatus("current")
_TopoNodeFtpProxyPort_Type = Integer32
_TopoNodeFtpProxyPort_Object = MibTableColumn
topoNodeFtpProxyPort = _TopoNodeFtpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 12),
    _TopoNodeFtpProxyPort_Type()
)
topoNodeFtpProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeFtpProxyPort.setStatus("current")
_TopoNodeTelnetProxyPort_Type = Integer32
_TopoNodeTelnetProxyPort_Object = MibTableColumn
topoNodeTelnetProxyPort = _TopoNodeTelnetProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 13),
    _TopoNodeTelnetProxyPort_Type()
)
topoNodeTelnetProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeTelnetProxyPort.setStatus("current")
_TopoNodeHttpProxyPort_Type = Integer32
_TopoNodeHttpProxyPort_Object = MibTableColumn
topoNodeHttpProxyPort = _TopoNodeHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 14),
    _TopoNodeHttpProxyPort_Type()
)
topoNodeHttpProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeHttpProxyPort.setStatus("current")
_TopoNodePrimaryGneIp_Type = InetAddressIPv4
_TopoNodePrimaryGneIp_Object = MibTableColumn
topoNodePrimaryGneIp = _TopoNodePrimaryGneIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 15),
    _TopoNodePrimaryGneIp_Type()
)
topoNodePrimaryGneIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodePrimaryGneIp.setStatus("current")
_TopoNodeSecondaryGneIp_Type = InetAddressIPv4
_TopoNodeSecondaryGneIp_Object = MibTableColumn
topoNodeSecondaryGneIp = _TopoNodeSecondaryGneIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 16),
    _TopoNodeSecondaryGneIp_Type()
)
topoNodeSecondaryGneIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeSecondaryGneIp.setStatus("current")
_TopoNodeEnableAuxTosByteAlteration_Type = TruthValue
_TopoNodeEnableAuxTosByteAlteration_Object = MibTableColumn
topoNodeEnableAuxTosByteAlteration = _TopoNodeEnableAuxTosByteAlteration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 17),
    _TopoNodeEnableAuxTosByteAlteration_Type()
)
topoNodeEnableAuxTosByteAlteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeEnableAuxTosByteAlteration.setStatus("current")
_TopoNodeSnmpEngineId_Type = SnmpEngineID
_TopoNodeSnmpEngineId_Object = MibTableColumn
topoNodeSnmpEngineId = _TopoNodeSnmpEngineId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 18),
    _TopoNodeSnmpEngineId_Type()
)
topoNodeSnmpEngineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeSnmpEngineId.setStatus("current")
_TopoNodeSecondaryDcnIp_Type = InetAddressIPv4
_TopoNodeSecondaryDcnIp_Object = MibTableColumn
topoNodeSecondaryDcnIp = _TopoNodeSecondaryDcnIp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 19),
    _TopoNodeSecondaryDcnIp_Type()
)
topoNodeSecondaryDcnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeSecondaryDcnIp.setStatus("current")
_TopoNodeDcnIp6_Type = InetAddressIPv6
_TopoNodeDcnIp6_Object = MibTableColumn
topoNodeDcnIp6 = _TopoNodeDcnIp6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 20),
    _TopoNodeDcnIp6_Type()
)
topoNodeDcnIp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnIp6.setStatus("current")
_TopoNodeDcnIpNetMask6_Type = Integer32
_TopoNodeDcnIpNetMask6_Object = MibTableColumn
topoNodeDcnIpNetMask6 = _TopoNodeDcnIpNetMask6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 21),
    _TopoNodeDcnIpNetMask6_Type()
)
topoNodeDcnIpNetMask6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnIpNetMask6.setStatus("current")
_TopoNodeDcnLinkLocal_Type = InetAddressIPv6
_TopoNodeDcnLinkLocal_Object = MibTableColumn
topoNodeDcnLinkLocal = _TopoNodeDcnLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 1, 1, 22),
    _TopoNodeDcnLinkLocal_Type()
)
topoNodeDcnLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoNodeDcnLinkLocal.setStatus("current")
_TopoNodeConformance_ObjectIdentity = ObjectIdentity
topoNodeConformance = _TopoNodeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 3)
)
_TopoNodeCompliances_ObjectIdentity = ObjectIdentity
topoNodeCompliances = _TopoNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 3, 1)
)
_TopoNodeGroups_ObjectIdentity = ObjectIdentity
topoNodeGroups = _TopoNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 3, 2)
)

# Managed Objects groups

topoNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 3, 2, 1)
)
topoNodeGroup.setObjects(
      *(("INFINERA-TOPONODE-MIB", "topoNodeRouterId"),
        ("INFINERA-TOPONODE-MIB", "topoNodeMeName"),
        ("INFINERA-TOPONODE-MIB", "topoNodeNodeId"),
        ("INFINERA-TOPONODE-MIB", "topoNodeNeType"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnIp"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnIpNetMask"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnIp6"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnIpNetMask6"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnLinkLocal"),
        ("INFINERA-TOPONODE-MIB", "topoNodeDcnEnabled"),
        ("INFINERA-TOPONODE-MIB", "topoNodeGatewayProxyEnabled"),
        ("INFINERA-TOPONODE-MIB", "topoNodeSecondaryDcnIp"),
        ("INFINERA-TOPONODE-MIB", "topoNodeXmlPortId"),
        ("INFINERA-TOPONODE-MIB", "topoNodeTl1PortId"),
        ("INFINERA-TOPONODE-MIB", "topoNodeXmlProxyPort"),
        ("INFINERA-TOPONODE-MIB", "topoNodeFtpProxyPort"),
        ("INFINERA-TOPONODE-MIB", "topoNodeTelnetProxyPort"),
        ("INFINERA-TOPONODE-MIB", "topoNodeHttpProxyPort"),
        ("INFINERA-TOPONODE-MIB", "topoNodePrimaryGneIp"),
        ("INFINERA-TOPONODE-MIB", "topoNodeSecondaryGneIp"),
        ("INFINERA-TOPONODE-MIB", "topoNodeEnableAuxTosByteAlteration"),
        ("INFINERA-TOPONODE-MIB", "topoNodeSnmpEngineId"))
)
if mibBuilder.loadTexts:
    topoNodeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

topoNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 8, 2, 3, 1, 1)
)
topoNodeCompliance.setObjects(
    ("INFINERA-TOPONODE-MIB", "topoNodeGroup")
)
if mibBuilder.loadTexts:
    topoNodeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TOPONODE-MIB",
    **{"topoNodeMIB": topoNodeMIB,
       "topoNodeTable": topoNodeTable,
       "topoNodeEntry": topoNodeEntry,
       "topoNodeMeName": topoNodeMeName,
       "topoNodeNodeId": topoNodeNodeId,
       "topoNodeNeType": topoNodeNeType,
       "topoNodeRouterId": topoNodeRouterId,
       "topoNodeDcnIp": topoNodeDcnIp,
       "topoNodeDcnIpNetMask": topoNodeDcnIpNetMask,
       "topoNodeDcnEnabled": topoNodeDcnEnabled,
       "topoNodeGatewayProxyEnabled": topoNodeGatewayProxyEnabled,
       "topoNodeXmlPortId": topoNodeXmlPortId,
       "topoNodeTl1PortId": topoNodeTl1PortId,
       "topoNodeXmlProxyPort": topoNodeXmlProxyPort,
       "topoNodeFtpProxyPort": topoNodeFtpProxyPort,
       "topoNodeTelnetProxyPort": topoNodeTelnetProxyPort,
       "topoNodeHttpProxyPort": topoNodeHttpProxyPort,
       "topoNodePrimaryGneIp": topoNodePrimaryGneIp,
       "topoNodeSecondaryGneIp": topoNodeSecondaryGneIp,
       "topoNodeEnableAuxTosByteAlteration": topoNodeEnableAuxTosByteAlteration,
       "topoNodeSnmpEngineId": topoNodeSnmpEngineId,
       "topoNodeSecondaryDcnIp": topoNodeSecondaryDcnIp,
       "topoNodeDcnIp6": topoNodeDcnIp6,
       "topoNodeDcnIpNetMask6": topoNodeDcnIpNetMask6,
       "topoNodeDcnLinkLocal": topoNodeDcnLinkLocal,
       "topoNodeConformance": topoNodeConformance,
       "topoNodeCompliances": topoNodeCompliances,
       "topoNodeCompliance": topoNodeCompliance,
       "topoNodeGroups": topoNodeGroups,
       "topoNodeGroup": topoNodeGroup}
)
