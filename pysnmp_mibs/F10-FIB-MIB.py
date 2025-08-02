_Z='f10IpForwardObjectGroup'
_Y='f10InetCidrRouteCamIndex'
_X='f10InetCidrRouteEgressPort'
_W='f10InetCidrRouteMacAddress'
_V='f10InetCidrRouteIfIndex'
_U='f10IpForwardVersion'
_T='f10InetCidrRouteFirstHop'
_S='f10InetCidrRouteFirstHopType'
_R='f10InetCidrRouteNextHop'
_Q='f10InetCidrRouteNextHopType'
_P='f10InetCidrRoutePfxLen'
_O='f10InetCidrRouteDest'
_N='f10InetCidrRouteDestType'
_M='f10IpforwardFirstHop'
_L='f10IpforwardNextHop'
_K='f10IpforwardMask'
_J='f10IpforwardDest'
_I='f10IpForwardAddrFamily'
_H='OctetString'
_G='chSysCardNumber'
_F='F10-CHASSIS-MIB'
_E='not-accessible'
_D='deprecated'
_C='read-only'
_B='F10-FIB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
chSysCardNumber,=mibBuilder.importSymbols(_F,_G)
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
f10IpForwardMib=ModuleIdentity((1,3,6,1,4,1,6027,3,9))
if mibBuilder.loadTexts:f10IpForwardMib.setRevisions(('2011-07-08 12:00','2007-09-14 12:00'))
_F10IpForwardMibObjects_ObjectIdentity=ObjectIdentity
f10IpForwardMibObjects=_F10IpForwardMibObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,9,1))
_F10IpForwardVersionTable_Object=MibTable
f10IpForwardVersionTable=_F10IpForwardVersionTable_Object((1,3,6,1,4,1,6027,3,9,1,1))
if mibBuilder.loadTexts:f10IpForwardVersionTable.setStatus(_A)
_F10IpForwardVersionEntry_Object=MibTableRow
f10IpForwardVersionEntry=_F10IpForwardVersionEntry_Object((1,3,6,1,4,1,6027,3,9,1,1,1))
f10IpForwardVersionEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:f10IpForwardVersionEntry.setStatus(_A)
_F10IpForwardAddrFamily_Type=InetAddressType
_F10IpForwardAddrFamily_Object=MibTableColumn
f10IpForwardAddrFamily=_F10IpForwardAddrFamily_Object((1,3,6,1,4,1,6027,3,9,1,1,1,1),_F10IpForwardAddrFamily_Type())
f10IpForwardAddrFamily.setMaxAccess(_E)
if mibBuilder.loadTexts:f10IpForwardAddrFamily.setStatus(_A)
_F10IpForwardVersion_Type=Counter64
_F10IpForwardVersion_Object=MibTableColumn
f10IpForwardVersion=_F10IpForwardVersion_Object((1,3,6,1,4,1,6027,3,9,1,1,1,2),_F10IpForwardVersion_Type())
f10IpForwardVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpForwardVersion.setStatus(_A)
_F10IpForwardTable_Object=MibTable
f10IpForwardTable=_F10IpForwardTable_Object((1,3,6,1,4,1,6027,3,9,1,2))
if mibBuilder.loadTexts:f10IpForwardTable.setStatus(_D)
_F10IpForwardEntry_Object=MibTableRow
f10IpForwardEntry=_F10IpForwardEntry_Object((1,3,6,1,4,1,6027,3,9,1,2,1))
f10IpForwardEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:f10IpForwardEntry.setStatus(_D)
_F10IpforwardDest_Type=IpAddress
_F10IpforwardDest_Object=MibTableColumn
f10IpforwardDest=_F10IpforwardDest_Object((1,3,6,1,4,1,6027,3,9,1,2,1,1),_F10IpforwardDest_Type())
f10IpforwardDest.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardDest.setStatus(_D)
_F10IpforwardMask_Type=IpAddress
_F10IpforwardMask_Object=MibTableColumn
f10IpforwardMask=_F10IpforwardMask_Object((1,3,6,1,4,1,6027,3,9,1,2,1,2),_F10IpforwardMask_Type())
f10IpforwardMask.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardMask.setStatus(_D)
_F10IpforwardNextHop_Type=IpAddress
_F10IpforwardNextHop_Object=MibTableColumn
f10IpforwardNextHop=_F10IpforwardNextHop_Object((1,3,6,1,4,1,6027,3,9,1,2,1,3),_F10IpforwardNextHop_Type())
f10IpforwardNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardNextHop.setStatus(_D)
_F10IpforwardFirstHop_Type=IpAddress
_F10IpforwardFirstHop_Object=MibTableColumn
f10IpforwardFirstHop=_F10IpforwardFirstHop_Object((1,3,6,1,4,1,6027,3,9,1,2,1,4),_F10IpforwardFirstHop_Type())
f10IpforwardFirstHop.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardFirstHop.setStatus(_D)
_F10IpforwardIfIndex_Type=Integer32
_F10IpforwardIfIndex_Object=MibTableColumn
f10IpforwardIfIndex=_F10IpforwardIfIndex_Object((1,3,6,1,4,1,6027,3,9,1,2,1,5),_F10IpforwardIfIndex_Type())
f10IpforwardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardIfIndex.setStatus(_D)
_F10IpforwardMacAddress_Type=MacAddress
_F10IpforwardMacAddress_Object=MibTableColumn
f10IpforwardMacAddress=_F10IpforwardMacAddress_Object((1,3,6,1,4,1,6027,3,9,1,2,1,6),_F10IpforwardMacAddress_Type())
f10IpforwardMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardMacAddress.setStatus(_D)
class _F10IpforwardEgressPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_F10IpforwardEgressPort_Type.__name__=_H
_F10IpforwardEgressPort_Object=MibTableColumn
f10IpforwardEgressPort=_F10IpforwardEgressPort_Object((1,3,6,1,4,1,6027,3,9,1,2,1,7),_F10IpforwardEgressPort_Type())
f10IpforwardEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardEgressPort.setStatus(_D)
_F10IpforwardCamIndex_Type=Integer32
_F10IpforwardCamIndex_Object=MibTableColumn
f10IpforwardCamIndex=_F10IpforwardCamIndex_Object((1,3,6,1,4,1,6027,3,9,1,2,1,8),_F10IpforwardCamIndex_Type())
f10IpforwardCamIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IpforwardCamIndex.setStatus(_D)
_F10InetCidrIpv4RouteNumber_Type=Gauge32
_F10InetCidrIpv4RouteNumber_Object=MibScalar
f10InetCidrIpv4RouteNumber=_F10InetCidrIpv4RouteNumber_Object((1,3,6,1,4,1,6027,3,9,1,3),_F10InetCidrIpv4RouteNumber_Type())
f10InetCidrIpv4RouteNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrIpv4RouteNumber.setStatus(_A)
_F10InetCidrIpv6RouteNumber_Type=Gauge32
_F10InetCidrIpv6RouteNumber_Object=MibScalar
f10InetCidrIpv6RouteNumber=_F10InetCidrIpv6RouteNumber_Object((1,3,6,1,4,1,6027,3,9,1,4),_F10InetCidrIpv6RouteNumber_Type())
f10InetCidrIpv6RouteNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrIpv6RouteNumber.setStatus(_A)
_F10InetCidrRouteTable_Object=MibTable
f10InetCidrRouteTable=_F10InetCidrRouteTable_Object((1,3,6,1,4,1,6027,3,9,1,5))
if mibBuilder.loadTexts:f10InetCidrRouteTable.setStatus(_A)
_F10InetCidrRouteTableEntry_Object=MibTableRow
f10InetCidrRouteTableEntry=_F10InetCidrRouteTableEntry_Object((1,3,6,1,4,1,6027,3,9,1,5,1))
f10InetCidrRouteTableEntry.setIndexNames((0,_F,_G),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:f10InetCidrRouteTableEntry.setStatus(_A)
_F10InetCidrRouteDestType_Type=InetAddressType
_F10InetCidrRouteDestType_Object=MibTableColumn
f10InetCidrRouteDestType=_F10InetCidrRouteDestType_Object((1,3,6,1,4,1,6027,3,9,1,5,1,1),_F10InetCidrRouteDestType_Type())
f10InetCidrRouteDestType.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteDestType.setStatus(_A)
_F10InetCidrRouteDest_Type=InetAddress
_F10InetCidrRouteDest_Object=MibTableColumn
f10InetCidrRouteDest=_F10InetCidrRouteDest_Object((1,3,6,1,4,1,6027,3,9,1,5,1,2),_F10InetCidrRouteDest_Type())
f10InetCidrRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteDest.setStatus(_A)
_F10InetCidrRoutePfxLen_Type=InetAddressPrefixLength
_F10InetCidrRoutePfxLen_Object=MibTableColumn
f10InetCidrRoutePfxLen=_F10InetCidrRoutePfxLen_Object((1,3,6,1,4,1,6027,3,9,1,5,1,3),_F10InetCidrRoutePfxLen_Type())
f10InetCidrRoutePfxLen.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRoutePfxLen.setStatus(_A)
_F10InetCidrRouteNextHopType_Type=InetAddressType
_F10InetCidrRouteNextHopType_Object=MibTableColumn
f10InetCidrRouteNextHopType=_F10InetCidrRouteNextHopType_Object((1,3,6,1,4,1,6027,3,9,1,5,1,4),_F10InetCidrRouteNextHopType_Type())
f10InetCidrRouteNextHopType.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteNextHopType.setStatus(_A)
_F10InetCidrRouteNextHop_Type=InetAddress
_F10InetCidrRouteNextHop_Object=MibTableColumn
f10InetCidrRouteNextHop=_F10InetCidrRouteNextHop_Object((1,3,6,1,4,1,6027,3,9,1,5,1,5),_F10InetCidrRouteNextHop_Type())
f10InetCidrRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteNextHop.setStatus(_A)
_F10InetCidrRouteFirstHopType_Type=InetAddressType
_F10InetCidrRouteFirstHopType_Object=MibTableColumn
f10InetCidrRouteFirstHopType=_F10InetCidrRouteFirstHopType_Object((1,3,6,1,4,1,6027,3,9,1,5,1,6),_F10InetCidrRouteFirstHopType_Type())
f10InetCidrRouteFirstHopType.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteFirstHopType.setStatus(_A)
_F10InetCidrRouteFirstHop_Type=InetAddress
_F10InetCidrRouteFirstHop_Object=MibTableColumn
f10InetCidrRouteFirstHop=_F10InetCidrRouteFirstHop_Object((1,3,6,1,4,1,6027,3,9,1,5,1,7),_F10InetCidrRouteFirstHop_Type())
f10InetCidrRouteFirstHop.setMaxAccess(_E)
if mibBuilder.loadTexts:f10InetCidrRouteFirstHop.setStatus(_A)
_F10InetCidrRouteIfIndex_Type=InterfaceIndexOrZero
_F10InetCidrRouteIfIndex_Object=MibTableColumn
f10InetCidrRouteIfIndex=_F10InetCidrRouteIfIndex_Object((1,3,6,1,4,1,6027,3,9,1,5,1,8),_F10InetCidrRouteIfIndex_Type())
f10InetCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrRouteIfIndex.setStatus(_A)
_F10InetCidrRouteMacAddress_Type=MacAddress
_F10InetCidrRouteMacAddress_Object=MibTableColumn
f10InetCidrRouteMacAddress=_F10InetCidrRouteMacAddress_Object((1,3,6,1,4,1,6027,3,9,1,5,1,9),_F10InetCidrRouteMacAddress_Type())
f10InetCidrRouteMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrRouteMacAddress.setStatus(_A)
class _F10InetCidrRouteEgressPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_F10InetCidrRouteEgressPort_Type.__name__=_H
_F10InetCidrRouteEgressPort_Object=MibTableColumn
f10InetCidrRouteEgressPort=_F10InetCidrRouteEgressPort_Object((1,3,6,1,4,1,6027,3,9,1,5,1,10),_F10InetCidrRouteEgressPort_Type())
f10InetCidrRouteEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrRouteEgressPort.setStatus(_A)
_F10InetCidrRouteCamIndex_Type=Unsigned32
_F10InetCidrRouteCamIndex_Object=MibTableColumn
f10InetCidrRouteCamIndex=_F10InetCidrRouteCamIndex_Object((1,3,6,1,4,1,6027,3,9,1,5,1,11),_F10InetCidrRouteCamIndex_Type())
f10InetCidrRouteCamIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f10InetCidrRouteCamIndex.setStatus(_A)
_F10IpForwardMibConformance_ObjectIdentity=ObjectIdentity
f10IpForwardMibConformance=_F10IpForwardMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,9,2))
_F10IpForwardMibCompliances_ObjectIdentity=ObjectIdentity
f10IpForwardMibCompliances=_F10IpForwardMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,9,2,1))
_F10IpForwardMibGroups_ObjectIdentity=ObjectIdentity
f10IpForwardMibGroups=_F10IpForwardMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,9,2,2))
f10IpForwardObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,9,2,2,1))
f10IpForwardObjectGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:f10IpForwardObjectGroup.setStatus(_A)
f10IpForwardMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,9,2,1,1))
f10IpForwardMibCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:f10IpForwardMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'f10IpForwardMib':f10IpForwardMib,'f10IpForwardMibObjects':f10IpForwardMibObjects,'f10IpForwardVersionTable':f10IpForwardVersionTable,'f10IpForwardVersionEntry':f10IpForwardVersionEntry,_I:f10IpForwardAddrFamily,_U:f10IpForwardVersion,'f10IpForwardTable':f10IpForwardTable,'f10IpForwardEntry':f10IpForwardEntry,_J:f10IpforwardDest,_K:f10IpforwardMask,_L:f10IpforwardNextHop,_M:f10IpforwardFirstHop,'f10IpforwardIfIndex':f10IpforwardIfIndex,'f10IpforwardMacAddress':f10IpforwardMacAddress,'f10IpforwardEgressPort':f10IpforwardEgressPort,'f10IpforwardCamIndex':f10IpforwardCamIndex,'f10InetCidrIpv4RouteNumber':f10InetCidrIpv4RouteNumber,'f10InetCidrIpv6RouteNumber':f10InetCidrIpv6RouteNumber,'f10InetCidrRouteTable':f10InetCidrRouteTable,'f10InetCidrRouteTableEntry':f10InetCidrRouteTableEntry,_N:f10InetCidrRouteDestType,_O:f10InetCidrRouteDest,_P:f10InetCidrRoutePfxLen,_Q:f10InetCidrRouteNextHopType,_R:f10InetCidrRouteNextHop,_S:f10InetCidrRouteFirstHopType,_T:f10InetCidrRouteFirstHop,_V:f10InetCidrRouteIfIndex,_W:f10InetCidrRouteMacAddress,_X:f10InetCidrRouteEgressPort,_Y:f10InetCidrRouteCamIndex,'f10IpForwardMibConformance':f10IpForwardMibConformance,'f10IpForwardMibCompliances':f10IpForwardMibCompliances,'f10IpForwardMibCompliance':f10IpForwardMibCompliance,'f10IpForwardMibGroups':f10IpForwardMibGroups,_Z:f10IpForwardObjectGroup})