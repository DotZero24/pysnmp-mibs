_M='zyIpRouteGateway'
_L='zyIpRouteDestinationMaskBits'
_K='zyIpRouteDestinationIpAddress'
_J='static'
_I='zyHostVid'
_H='zyHostIpAddress'
_G='zyRouteDomainIpMaskBits'
_F='zyRouteDomainIpAddress'
_E='Integer32'
_D='read-only'
_C='not-accessible'
_B='ZYXEL-IP-FORWARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpForward=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,32))
_ZyxelRouteDomainStatus_ObjectIdentity=ObjectIdentity
zyxelRouteDomainStatus=_ZyxelRouteDomainStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,32,1))
_ZyxelRouteDomainTable_Object=MibTable
zyxelRouteDomainTable=_ZyxelRouteDomainTable_Object((1,3,6,1,4,1,890,1,15,3,32,1,1))
if mibBuilder.loadTexts:zyxelRouteDomainTable.setStatus(_A)
_ZyxelRouteDomainEntry_Object=MibTableRow
zyxelRouteDomainEntry=_ZyxelRouteDomainEntry_Object((1,3,6,1,4,1,890,1,15,3,32,1,1,1))
zyxelRouteDomainEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:zyxelRouteDomainEntry.setStatus(_A)
_ZyRouteDomainIpAddress_Type=IpAddress
_ZyRouteDomainIpAddress_Object=MibTableColumn
zyRouteDomainIpAddress=_ZyRouteDomainIpAddress_Object((1,3,6,1,4,1,890,1,15,3,32,1,1,1,1),_ZyRouteDomainIpAddress_Type())
zyRouteDomainIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyRouteDomainIpAddress.setStatus(_A)
_ZyRouteDomainIpMaskBits_Type=Integer32
_ZyRouteDomainIpMaskBits_Object=MibTableColumn
zyRouteDomainIpMaskBits=_ZyRouteDomainIpMaskBits_Object((1,3,6,1,4,1,890,1,15,3,32,1,1,1,2),_ZyRouteDomainIpMaskBits_Type())
zyRouteDomainIpMaskBits.setMaxAccess(_C)
if mibBuilder.loadTexts:zyRouteDomainIpMaskBits.setStatus(_A)
_ZyRouteDomainVid_Type=Integer32
_ZyRouteDomainVid_Object=MibTableColumn
zyRouteDomainVid=_ZyRouteDomainVid_Object((1,3,6,1,4,1,890,1,15,3,32,1,1,1,3),_ZyRouteDomainVid_Type())
zyRouteDomainVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zyRouteDomainVid.setStatus(_A)
_ZyxelHostStatus_ObjectIdentity=ObjectIdentity
zyxelHostStatus=_ZyxelHostStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,32,2))
_ZyxelHostTable_Object=MibTable
zyxelHostTable=_ZyxelHostTable_Object((1,3,6,1,4,1,890,1,15,3,32,2,1))
if mibBuilder.loadTexts:zyxelHostTable.setStatus(_A)
_ZyxelHostEntry_Object=MibTableRow
zyxelHostEntry=_ZyxelHostEntry_Object((1,3,6,1,4,1,890,1,15,3,32,2,1,1))
zyxelHostEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:zyxelHostEntry.setStatus(_A)
_ZyHostIpAddress_Type=IpAddress
_ZyHostIpAddress_Object=MibTableColumn
zyHostIpAddress=_ZyHostIpAddress_Object((1,3,6,1,4,1,890,1,15,3,32,2,1,1,1),_ZyHostIpAddress_Type())
zyHostIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHostIpAddress.setStatus(_A)
_ZyHostVid_Type=Integer32
_ZyHostVid_Object=MibTableColumn
zyHostVid=_ZyHostVid_Object((1,3,6,1,4,1,890,1,15,3,32,2,1,1,2),_ZyHostVid_Type())
zyHostVid.setMaxAccess(_C)
if mibBuilder.loadTexts:zyHostVid.setStatus(_A)
_ZyHostPort_Type=DisplayString
_ZyHostPort_Object=MibTableColumn
zyHostPort=_ZyHostPort_Object((1,3,6,1,4,1,890,1,15,3,32,2,1,1,3),_ZyHostPort_Type())
zyHostPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHostPort.setStatus(_A)
class _ZyHostType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('dynamic',2)))
_ZyHostType_Type.__name__=_E
_ZyHostType_Object=MibTableColumn
zyHostType=_ZyHostType_Object((1,3,6,1,4,1,890,1,15,3,32,2,1,1,4),_ZyHostType_Type())
zyHostType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyHostType.setStatus(_A)
_ZyxelIpRouteStatus_ObjectIdentity=ObjectIdentity
zyxelIpRouteStatus=_ZyxelIpRouteStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,32,3))
_ZyxelIpRouteTable_Object=MibTable
zyxelIpRouteTable=_ZyxelIpRouteTable_Object((1,3,6,1,4,1,890,1,15,3,32,3,1))
if mibBuilder.loadTexts:zyxelIpRouteTable.setStatus(_A)
_ZyxelIpRouteEntry_Object=MibTableRow
zyxelIpRouteEntry=_ZyxelIpRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1))
zyxelIpRouteEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:zyxelIpRouteEntry.setStatus(_A)
_ZyIpRouteDestinationIpAddress_Type=IpAddress
_ZyIpRouteDestinationIpAddress_Object=MibTableColumn
zyIpRouteDestinationIpAddress=_ZyIpRouteDestinationIpAddress_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,1),_ZyIpRouteDestinationIpAddress_Type())
zyIpRouteDestinationIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpRouteDestinationIpAddress.setStatus(_A)
_ZyIpRouteDestinationMaskBits_Type=Integer32
_ZyIpRouteDestinationMaskBits_Object=MibTableColumn
zyIpRouteDestinationMaskBits=_ZyIpRouteDestinationMaskBits_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,2),_ZyIpRouteDestinationMaskBits_Type())
zyIpRouteDestinationMaskBits.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpRouteDestinationMaskBits.setStatus(_A)
_ZyIpRouteGateway_Type=IpAddress
_ZyIpRouteGateway_Object=MibTableColumn
zyIpRouteGateway=_ZyIpRouteGateway_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,3),_ZyIpRouteGateway_Type())
zyIpRouteGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpRouteGateway.setStatus(_A)
_ZyIpRouteIf_Type=IpAddress
_ZyIpRouteIf_Object=MibTableColumn
zyIpRouteIf=_ZyIpRouteIf_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,4),_ZyIpRouteIf_Type())
zyIpRouteIf.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpRouteIf.setStatus(_A)
_ZyIpRouteMetric_Type=Integer32
_ZyIpRouteMetric_Object=MibTableColumn
zyIpRouteMetric=_ZyIpRouteMetric_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,5),_ZyIpRouteMetric_Type())
zyIpRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpRouteMetric.setStatus(_A)
class _ZyIpRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip',1),('bgp',2),('ospf',3),(_J,4)))
_ZyIpRouteType_Type.__name__=_E
_ZyIpRouteType_Object=MibTableColumn
zyIpRouteType=_ZyIpRouteType_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,6),_ZyIpRouteType_Type())
zyIpRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpRouteType.setStatus(_A)
_ZyIpRouteUptime_Type=TimeTicks
_ZyIpRouteUptime_Object=MibTableColumn
zyIpRouteUptime=_ZyIpRouteUptime_Object((1,3,6,1,4,1,890,1,15,3,32,3,1,1,7),_ZyIpRouteUptime_Type())
zyIpRouteUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpRouteUptime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIpForward':zyxelIpForward,'zyxelRouteDomainStatus':zyxelRouteDomainStatus,'zyxelRouteDomainTable':zyxelRouteDomainTable,'zyxelRouteDomainEntry':zyxelRouteDomainEntry,_F:zyRouteDomainIpAddress,_G:zyRouteDomainIpMaskBits,'zyRouteDomainVid':zyRouteDomainVid,'zyxelHostStatus':zyxelHostStatus,'zyxelHostTable':zyxelHostTable,'zyxelHostEntry':zyxelHostEntry,_H:zyHostIpAddress,_I:zyHostVid,'zyHostPort':zyHostPort,'zyHostType':zyHostType,'zyxelIpRouteStatus':zyxelIpRouteStatus,'zyxelIpRouteTable':zyxelIpRouteTable,'zyxelIpRouteEntry':zyxelIpRouteEntry,_K:zyIpRouteDestinationIpAddress,_L:zyIpRouteDestinationMaskBits,_M:zyIpRouteGateway,'zyIpRouteIf':zyIpRouteIf,'zyIpRouteMetric':zyIpRouteMetric,'zyIpRouteType':zyIpRouteType,'zyIpRouteUptime':zyIpRouteUptime})