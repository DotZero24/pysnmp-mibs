_Z='topoNodeGroup'
_Y='topoNodeSnmpEngineId'
_X='topoNodeEnableAuxTosByteAlteration'
_W='topoNodeSecondaryGneIp'
_V='topoNodePrimaryGneIp'
_U='topoNodeHttpProxyPort'
_T='topoNodeTelnetProxyPort'
_S='topoNodeFtpProxyPort'
_R='topoNodeXmlProxyPort'
_Q='topoNodeTl1PortId'
_P='topoNodeXmlPortId'
_O='topoNodeSecondaryDcnIp'
_N='topoNodeGatewayProxyEnabled'
_M='topoNodeDcnEnabled'
_L='topoNodeDcnLinkLocal'
_K='topoNodeDcnIpNetMask6'
_J='topoNodeDcnIp6'
_I='topoNodeDcnIpNetMask'
_H='topoNodeDcnIp'
_G='topoNodeNeType'
_F='topoNodeNodeId'
_E='topoNodeMeName'
_D='topoNodeRouterId'
_C='read-only'
_B='INFINERA-TOPONODE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
infnNE,=mibBuilder.importSymbols('INFINERA-REG-MIB','infnNE')
InfnNeType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnNeType')
SnmpEngineID,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpEngineID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
topoNodeMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,8,2))
_TopoNodeTable_Object=MibTable
topoNodeTable=_TopoNodeTable_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1))
if mibBuilder.loadTexts:topoNodeTable.setStatus(_A)
_TopoNodeEntry_Object=MibTableRow
topoNodeEntry=_TopoNodeEntry_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1))
topoNodeEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:topoNodeEntry.setStatus(_A)
_TopoNodeMeName_Type=DisplayString
_TopoNodeMeName_Object=MibTableColumn
topoNodeMeName=_TopoNodeMeName_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,1),_TopoNodeMeName_Type())
topoNodeMeName.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeMeName.setStatus(_A)
_TopoNodeNodeId_Type=DisplayString
_TopoNodeNodeId_Object=MibTableColumn
topoNodeNodeId=_TopoNodeNodeId_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,2),_TopoNodeNodeId_Type())
topoNodeNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeNodeId.setStatus(_A)
_TopoNodeNeType_Type=InfnNeType
_TopoNodeNeType_Object=MibTableColumn
topoNodeNeType=_TopoNodeNeType_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,3),_TopoNodeNeType_Type())
topoNodeNeType.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeNeType.setStatus(_A)
_TopoNodeRouterId_Type=InetAddressIPv4
_TopoNodeRouterId_Object=MibTableColumn
topoNodeRouterId=_TopoNodeRouterId_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,4),_TopoNodeRouterId_Type())
topoNodeRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeRouterId.setStatus(_A)
_TopoNodeDcnIp_Type=InetAddressIPv4
_TopoNodeDcnIp_Object=MibTableColumn
topoNodeDcnIp=_TopoNodeDcnIp_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,5),_TopoNodeDcnIp_Type())
topoNodeDcnIp.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnIp.setStatus(_A)
_TopoNodeDcnIpNetMask_Type=InetAddressIPv4
_TopoNodeDcnIpNetMask_Object=MibTableColumn
topoNodeDcnIpNetMask=_TopoNodeDcnIpNetMask_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,6),_TopoNodeDcnIpNetMask_Type())
topoNodeDcnIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnIpNetMask.setStatus(_A)
_TopoNodeDcnEnabled_Type=TruthValue
_TopoNodeDcnEnabled_Object=MibTableColumn
topoNodeDcnEnabled=_TopoNodeDcnEnabled_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,7),_TopoNodeDcnEnabled_Type())
topoNodeDcnEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnEnabled.setStatus(_A)
_TopoNodeGatewayProxyEnabled_Type=TruthValue
_TopoNodeGatewayProxyEnabled_Object=MibTableColumn
topoNodeGatewayProxyEnabled=_TopoNodeGatewayProxyEnabled_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,8),_TopoNodeGatewayProxyEnabled_Type())
topoNodeGatewayProxyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeGatewayProxyEnabled.setStatus(_A)
_TopoNodeXmlPortId_Type=Integer32
_TopoNodeXmlPortId_Object=MibTableColumn
topoNodeXmlPortId=_TopoNodeXmlPortId_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,9),_TopoNodeXmlPortId_Type())
topoNodeXmlPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeXmlPortId.setStatus(_A)
_TopoNodeTl1PortId_Type=Integer32
_TopoNodeTl1PortId_Object=MibTableColumn
topoNodeTl1PortId=_TopoNodeTl1PortId_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,10),_TopoNodeTl1PortId_Type())
topoNodeTl1PortId.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeTl1PortId.setStatus(_A)
_TopoNodeXmlProxyPort_Type=Integer32
_TopoNodeXmlProxyPort_Object=MibTableColumn
topoNodeXmlProxyPort=_TopoNodeXmlProxyPort_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,11),_TopoNodeXmlProxyPort_Type())
topoNodeXmlProxyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeXmlProxyPort.setStatus(_A)
_TopoNodeFtpProxyPort_Type=Integer32
_TopoNodeFtpProxyPort_Object=MibTableColumn
topoNodeFtpProxyPort=_TopoNodeFtpProxyPort_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,12),_TopoNodeFtpProxyPort_Type())
topoNodeFtpProxyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeFtpProxyPort.setStatus(_A)
_TopoNodeTelnetProxyPort_Type=Integer32
_TopoNodeTelnetProxyPort_Object=MibTableColumn
topoNodeTelnetProxyPort=_TopoNodeTelnetProxyPort_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,13),_TopoNodeTelnetProxyPort_Type())
topoNodeTelnetProxyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeTelnetProxyPort.setStatus(_A)
_TopoNodeHttpProxyPort_Type=Integer32
_TopoNodeHttpProxyPort_Object=MibTableColumn
topoNodeHttpProxyPort=_TopoNodeHttpProxyPort_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,14),_TopoNodeHttpProxyPort_Type())
topoNodeHttpProxyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeHttpProxyPort.setStatus(_A)
_TopoNodePrimaryGneIp_Type=InetAddressIPv4
_TopoNodePrimaryGneIp_Object=MibTableColumn
topoNodePrimaryGneIp=_TopoNodePrimaryGneIp_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,15),_TopoNodePrimaryGneIp_Type())
topoNodePrimaryGneIp.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodePrimaryGneIp.setStatus(_A)
_TopoNodeSecondaryGneIp_Type=InetAddressIPv4
_TopoNodeSecondaryGneIp_Object=MibTableColumn
topoNodeSecondaryGneIp=_TopoNodeSecondaryGneIp_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,16),_TopoNodeSecondaryGneIp_Type())
topoNodeSecondaryGneIp.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeSecondaryGneIp.setStatus(_A)
_TopoNodeEnableAuxTosByteAlteration_Type=TruthValue
_TopoNodeEnableAuxTosByteAlteration_Object=MibTableColumn
topoNodeEnableAuxTosByteAlteration=_TopoNodeEnableAuxTosByteAlteration_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,17),_TopoNodeEnableAuxTosByteAlteration_Type())
topoNodeEnableAuxTosByteAlteration.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeEnableAuxTosByteAlteration.setStatus(_A)
_TopoNodeSnmpEngineId_Type=SnmpEngineID
_TopoNodeSnmpEngineId_Object=MibTableColumn
topoNodeSnmpEngineId=_TopoNodeSnmpEngineId_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,18),_TopoNodeSnmpEngineId_Type())
topoNodeSnmpEngineId.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeSnmpEngineId.setStatus(_A)
_TopoNodeSecondaryDcnIp_Type=InetAddressIPv4
_TopoNodeSecondaryDcnIp_Object=MibTableColumn
topoNodeSecondaryDcnIp=_TopoNodeSecondaryDcnIp_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,19),_TopoNodeSecondaryDcnIp_Type())
topoNodeSecondaryDcnIp.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeSecondaryDcnIp.setStatus(_A)
_TopoNodeDcnIp6_Type=InetAddressIPv6
_TopoNodeDcnIp6_Object=MibTableColumn
topoNodeDcnIp6=_TopoNodeDcnIp6_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,20),_TopoNodeDcnIp6_Type())
topoNodeDcnIp6.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnIp6.setStatus(_A)
_TopoNodeDcnIpNetMask6_Type=Integer32
_TopoNodeDcnIpNetMask6_Object=MibTableColumn
topoNodeDcnIpNetMask6=_TopoNodeDcnIpNetMask6_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,21),_TopoNodeDcnIpNetMask6_Type())
topoNodeDcnIpNetMask6.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnIpNetMask6.setStatus(_A)
_TopoNodeDcnLinkLocal_Type=InetAddressIPv6
_TopoNodeDcnLinkLocal_Object=MibTableColumn
topoNodeDcnLinkLocal=_TopoNodeDcnLinkLocal_Object((1,3,6,1,4,1,21296,2,2,1,8,2,1,1,22),_TopoNodeDcnLinkLocal_Type())
topoNodeDcnLinkLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:topoNodeDcnLinkLocal.setStatus(_A)
_TopoNodeConformance_ObjectIdentity=ObjectIdentity
topoNodeConformance=_TopoNodeConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,2,3))
_TopoNodeCompliances_ObjectIdentity=ObjectIdentity
topoNodeCompliances=_TopoNodeCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,2,3,1))
_TopoNodeGroups_ObjectIdentity=ObjectIdentity
topoNodeGroups=_TopoNodeGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,8,2,3,2))
topoNodeGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,8,2,3,2,1))
topoNodeGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:topoNodeGroup.setStatus(_A)
topoNodeCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,8,2,3,1,1))
topoNodeCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:topoNodeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'topoNodeMIB':topoNodeMIB,'topoNodeTable':topoNodeTable,'topoNodeEntry':topoNodeEntry,_E:topoNodeMeName,_F:topoNodeNodeId,_G:topoNodeNeType,_D:topoNodeRouterId,_H:topoNodeDcnIp,_I:topoNodeDcnIpNetMask,_M:topoNodeDcnEnabled,_N:topoNodeGatewayProxyEnabled,_P:topoNodeXmlPortId,_Q:topoNodeTl1PortId,_R:topoNodeXmlProxyPort,_S:topoNodeFtpProxyPort,_T:topoNodeTelnetProxyPort,_U:topoNodeHttpProxyPort,_V:topoNodePrimaryGneIp,_W:topoNodeSecondaryGneIp,_X:topoNodeEnableAuxTosByteAlteration,_Y:topoNodeSnmpEngineId,_O:topoNodeSecondaryDcnIp,_J:topoNodeDcnIp6,_K:topoNodeDcnIpNetMask6,_L:topoNodeDcnLinkLocal,'topoNodeConformance':topoNodeConformance,'topoNodeCompliances':topoNodeCompliances,'topoNodeCompliance':topoNodeCompliance,'topoNodeGroups':topoNodeGroups,_Z:topoNodeGroup})