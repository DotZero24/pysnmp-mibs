_H='rcIpConfigDfltMgmtIpSubnet'
_G='rcIpConfigDfltMgmtIpAddress'
_F='rcIpConfigDefaultGateway'
_E='rcIpConfigMgmtIpSubnet'
_D='rcIpConfigMgmtIpAddress'
_C='read-write'
_B='RUGGEDCOM-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rcIp=ModuleIdentity((1,3,6,1,4,1,15004,4,3))
if mibBuilder.loadTexts:rcIp.setRevisions(('2013-12-11 10:00','2008-11-11 10:00'))
_RcIpConfig_ObjectIdentity=ObjectIdentity
rcIpConfig=_RcIpConfig_ObjectIdentity((1,3,6,1,4,1,15004,4,3,1))
if mibBuilder.loadTexts:rcIpConfig.setStatus(_A)
_RcIpConfigMgmtIpAddress_Type=IpAddress
_RcIpConfigMgmtIpAddress_Object=MibScalar
rcIpConfigMgmtIpAddress=_RcIpConfigMgmtIpAddress_Object((1,3,6,1,4,1,15004,4,3,1,1),_RcIpConfigMgmtIpAddress_Type())
rcIpConfigMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpConfigMgmtIpAddress.setStatus(_A)
_RcIpConfigMgmtIpSubnet_Type=IpAddress
_RcIpConfigMgmtIpSubnet_Object=MibScalar
rcIpConfigMgmtIpSubnet=_RcIpConfigMgmtIpSubnet_Object((1,3,6,1,4,1,15004,4,3,1,2),_RcIpConfigMgmtIpSubnet_Type())
rcIpConfigMgmtIpSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpConfigMgmtIpSubnet.setStatus(_A)
_RcIpConfigDefaultGateway_Type=IpAddress
_RcIpConfigDefaultGateway_Object=MibScalar
rcIpConfigDefaultGateway=_RcIpConfigDefaultGateway_Object((1,3,6,1,4,1,15004,4,3,1,3),_RcIpConfigDefaultGateway_Type())
rcIpConfigDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpConfigDefaultGateway.setStatus(_A)
_RcIpConfigDfltMgmtIpAddress_Type=IpAddress
_RcIpConfigDfltMgmtIpAddress_Object=MibScalar
rcIpConfigDfltMgmtIpAddress=_RcIpConfigDfltMgmtIpAddress_Object((1,3,6,1,4,1,15004,4,3,1,4),_RcIpConfigDfltMgmtIpAddress_Type())
rcIpConfigDfltMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpConfigDfltMgmtIpAddress.setStatus(_A)
_RcIpConfigDfltMgmtIpSubnet_Type=IpAddress
_RcIpConfigDfltMgmtIpSubnet_Object=MibScalar
rcIpConfigDfltMgmtIpSubnet=_RcIpConfigDfltMgmtIpSubnet_Object((1,3,6,1,4,1,15004,4,3,1,5),_RcIpConfigDfltMgmtIpSubnet_Type())
rcIpConfigDfltMgmtIpSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpConfigDfltMgmtIpSubnet.setStatus(_A)
_RcIpConformance_ObjectIdentity=ObjectIdentity
rcIpConformance=_RcIpConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,3,5))
_RcIpGroups_ObjectIdentity=ObjectIdentity
rcIpGroups=_RcIpGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,3,5,1))
rcIpObjectsGroup=ObjectGroup((1,3,6,1,4,1,15004,4,3,5,1,1))
rcIpObjectsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:rcIpObjectsGroup.setStatus(_A)
rcIpObjectsGroupDflt=ObjectGroup((1,3,6,1,4,1,15004,4,3,5,1,2))
rcIpObjectsGroupDflt.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:rcIpObjectsGroupDflt.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcIp':rcIp,'rcIpConfig':rcIpConfig,_D:rcIpConfigMgmtIpAddress,_E:rcIpConfigMgmtIpSubnet,_F:rcIpConfigDefaultGateway,_G:rcIpConfigDfltMgmtIpAddress,_H:rcIpConfigDfltMgmtIpSubnet,'rcIpConformance':rcIpConformance,'rcIpGroups':rcIpGroups,'rcIpObjectsGroup':rcIpObjectsGroup,'rcIpObjectsGroupDflt':rcIpObjectsGroupDflt})