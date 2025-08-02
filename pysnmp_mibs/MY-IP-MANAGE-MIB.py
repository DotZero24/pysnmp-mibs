_G='myL2L3DhcpManageMIBGroup'
_F='myDhcpServerIp'
_E='myDhcpRelayAgentGlobalStatus'
_D='EnabledStatus'
_C='read-write'
_B='MY-IP-MANAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,MemberMap=mibBuilder.importSymbols('MY-TC','ConfigStatus','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myIpManageMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,12))
if mibBuilder.loadTexts:myIpManageMIB.setRevisions(('2002-03-20 00:00',))
_MyDhcpMIBObjects_ObjectIdentity=ObjectIdentity
myDhcpMIBObjects=_MyDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,12,1))
class _MyDhcpRelayAgentGlobalStatus_Type(EnabledStatus):defaultValue=2
_MyDhcpRelayAgentGlobalStatus_Type.__name__=_D
_MyDhcpRelayAgentGlobalStatus_Object=MibScalar
myDhcpRelayAgentGlobalStatus=_MyDhcpRelayAgentGlobalStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,12,1,2),_MyDhcpRelayAgentGlobalStatus_Type())
myDhcpRelayAgentGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDhcpRelayAgentGlobalStatus.setStatus(_A)
_MyDhcpServerIp_Type=IpAddress
_MyDhcpServerIp_Object=MibScalar
myDhcpServerIp=_MyDhcpServerIp_Object((1,3,6,1,4,1,4881,1,1,10,2,12,1,3),_MyDhcpServerIp_Type())
myDhcpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:myDhcpServerIp.setStatus(_A)
_MyIpMIBObjects_ObjectIdentity=ObjectIdentity
myIpMIBObjects=_MyIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,12,2))
_MyIpDefaultGateWay_Type=IpAddress
_MyIpDefaultGateWay_Object=MibScalar
myIpDefaultGateWay=_MyIpDefaultGateWay_Object((1,3,6,1,4,1,4881,1,1,10,2,12,2,1),_MyIpDefaultGateWay_Type())
myIpDefaultGateWay.setMaxAccess(_C)
if mibBuilder.loadTexts:myIpDefaultGateWay.setStatus(_A)
_MyIpManageMIBConformance_ObjectIdentity=ObjectIdentity
myIpManageMIBConformance=_MyIpManageMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,12,3))
_MyIpManageMIBCompliances_ObjectIdentity=ObjectIdentity
myIpManageMIBCompliances=_MyIpManageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,12,3,1))
_MyIpManageMIBGroups_ObjectIdentity=ObjectIdentity
myIpManageMIBGroups=_MyIpManageMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,12,3,2))
myL2L3DhcpManageMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,12,3,2,1))
myL2L3DhcpManageMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:myL2L3DhcpManageMIBGroup.setStatus(_A)
myIpManageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,12,3,1,1))
myIpManageMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:myIpManageMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myIpManageMIB':myIpManageMIB,'myDhcpMIBObjects':myDhcpMIBObjects,_E:myDhcpRelayAgentGlobalStatus,_F:myDhcpServerIp,'myIpMIBObjects':myIpMIBObjects,'myIpDefaultGateWay':myIpDefaultGateWay,'myIpManageMIBConformance':myIpManageMIBConformance,'myIpManageMIBCompliances':myIpManageMIBCompliances,'myIpManageMIBCompliance':myIpManageMIBCompliance,'myIpManageMIBGroups':myIpManageMIBGroups,_G:myL2L3DhcpManageMIBGroup})