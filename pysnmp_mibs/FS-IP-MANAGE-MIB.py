_G='fsL2L3DhcpManageMIBGroup'
_F='fsDhcpServerIp'
_E='fsDhcpRelayAgentGlobalStatus'
_D='EnabledStatus'
_C='read-write'
_B='FS-IP-MANAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsIpManageMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,12))
if mibBuilder.loadTexts:fsIpManageMIB.setRevisions(('2002-03-20 00:00',))
_FsDhcpMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpMIBObjects=_FsDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,12,1))
class _FsDhcpRelayAgentGlobalStatus_Type(EnabledStatus):defaultValue=2
_FsDhcpRelayAgentGlobalStatus_Type.__name__=_D
_FsDhcpRelayAgentGlobalStatus_Object=MibScalar
fsDhcpRelayAgentGlobalStatus=_FsDhcpRelayAgentGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,12,1,2),_FsDhcpRelayAgentGlobalStatus_Type())
fsDhcpRelayAgentGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpRelayAgentGlobalStatus.setStatus(_A)
_FsDhcpServerIp_Type=IpAddress
_FsDhcpServerIp_Object=MibScalar
fsDhcpServerIp=_FsDhcpServerIp_Object((1,3,6,1,4,1,52642,1,1,10,2,12,1,3),_FsDhcpServerIp_Type())
fsDhcpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpServerIp.setStatus(_A)
_FsIpMIBObjects_ObjectIdentity=ObjectIdentity
fsIpMIBObjects=_FsIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,12,2))
_FsIpDefaultGateWay_Type=IpAddress
_FsIpDefaultGateWay_Object=MibScalar
fsIpDefaultGateWay=_FsIpDefaultGateWay_Object((1,3,6,1,4,1,52642,1,1,10,2,12,2,1),_FsIpDefaultGateWay_Type())
fsIpDefaultGateWay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDefaultGateWay.setStatus(_A)
_FsIpManageMIBConformance_ObjectIdentity=ObjectIdentity
fsIpManageMIBConformance=_FsIpManageMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,12,3))
_FsIpManageMIBCompliances_ObjectIdentity=ObjectIdentity
fsIpManageMIBCompliances=_FsIpManageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,12,3,1))
_FsIpManageMIBGroups_ObjectIdentity=ObjectIdentity
fsIpManageMIBGroups=_FsIpManageMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,12,3,2))
fsL2L3DhcpManageMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,12,3,2,1))
fsL2L3DhcpManageMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:fsL2L3DhcpManageMIBGroup.setStatus(_A)
fsIpManageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,12,3,1,1))
fsIpManageMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:fsIpManageMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsIpManageMIB':fsIpManageMIB,'fsDhcpMIBObjects':fsDhcpMIBObjects,_E:fsDhcpRelayAgentGlobalStatus,_F:fsDhcpServerIp,'fsIpMIBObjects':fsIpMIBObjects,'fsIpDefaultGateWay':fsIpDefaultGateWay,'fsIpManageMIBConformance':fsIpManageMIBConformance,'fsIpManageMIBCompliances':fsIpManageMIBCompliances,'fsIpManageMIBCompliance':fsIpManageMIBCompliance,'fsIpManageMIBGroups':fsIpManageMIBGroups,_G:fsL2L3DhcpManageMIBGroup})