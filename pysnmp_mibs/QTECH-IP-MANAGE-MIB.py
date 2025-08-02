_G='qtechL2L3DhcpManageMIBGroup'
_F='qtechDhcpServerIp'
_E='qtechDhcpRelayAgentGlobalStatus'
_D='EnabledStatus'
_C='read-write'
_B='QTECH-IP-MANAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechIpManageMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,12))
if mibBuilder.loadTexts:qtechIpManageMIB.setRevisions(('2002-03-20 00:00',))
_QtechDhcpMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpMIBObjects=_QtechDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,12,1))
class _QtechDhcpRelayAgentGlobalStatus_Type(EnabledStatus):defaultValue=2
_QtechDhcpRelayAgentGlobalStatus_Type.__name__=_D
_QtechDhcpRelayAgentGlobalStatus_Object=MibScalar
qtechDhcpRelayAgentGlobalStatus=_QtechDhcpRelayAgentGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,12,1,2),_QtechDhcpRelayAgentGlobalStatus_Type())
qtechDhcpRelayAgentGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpRelayAgentGlobalStatus.setStatus(_A)
_QtechDhcpServerIp_Type=IpAddress
_QtechDhcpServerIp_Object=MibScalar
qtechDhcpServerIp=_QtechDhcpServerIp_Object((1,3,6,1,4,1,27514,1,1,10,2,12,1,3),_QtechDhcpServerIp_Type())
qtechDhcpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpServerIp.setStatus(_A)
_QtechIpMIBObjects_ObjectIdentity=ObjectIdentity
qtechIpMIBObjects=_QtechIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,12,2))
_QtechIpDefaultGateWay_Type=IpAddress
_QtechIpDefaultGateWay_Object=MibScalar
qtechIpDefaultGateWay=_QtechIpDefaultGateWay_Object((1,3,6,1,4,1,27514,1,1,10,2,12,2,1),_QtechIpDefaultGateWay_Type())
qtechIpDefaultGateWay.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpDefaultGateWay.setStatus(_A)
_QtechIpManageMIBConformance_ObjectIdentity=ObjectIdentity
qtechIpManageMIBConformance=_QtechIpManageMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,12,3))
_QtechIpManageMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIpManageMIBCompliances=_QtechIpManageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,12,3,1))
_QtechIpManageMIBGroups_ObjectIdentity=ObjectIdentity
qtechIpManageMIBGroups=_QtechIpManageMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,12,3,2))
qtechL2L3DhcpManageMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,12,3,2,1))
qtechL2L3DhcpManageMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:qtechL2L3DhcpManageMIBGroup.setStatus(_A)
qtechIpManageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,12,3,1,1))
qtechIpManageMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechIpManageMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechIpManageMIB':qtechIpManageMIB,'qtechDhcpMIBObjects':qtechDhcpMIBObjects,_E:qtechDhcpRelayAgentGlobalStatus,_F:qtechDhcpServerIp,'qtechIpMIBObjects':qtechIpMIBObjects,'qtechIpDefaultGateWay':qtechIpDefaultGateWay,'qtechIpManageMIBConformance':qtechIpManageMIBConformance,'qtechIpManageMIBCompliances':qtechIpManageMIBCompliances,'qtechIpManageMIBCompliance':qtechIpManageMIBCompliance,'qtechIpManageMIBGroups':qtechIpManageMIBGroups,_G:qtechL2L3DhcpManageMIBGroup})