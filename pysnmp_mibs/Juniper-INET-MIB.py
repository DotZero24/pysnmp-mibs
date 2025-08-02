_V='juniInetRouteGroup'
_U='juniInetRouteStaticNullIntf'
_T='juniInetRouteStaticTag'
_S='juniInetRouteStaticMetric'
_R='juniInetRouteStaticNextHopAS'
_Q='juniInetRouteStaticStatus'
_P='juniInetRouteIfIndex'
_O='juniInetRouteStaticRowStatus'
_N='read-only'
_M='juniInetRouteStaticPref'
_L='juniInetRouteNextHop'
_K='juniInetRouteNextHopType'
_J='juniInetRoutePolicy'
_I='juniInetRoutePfxLen'
_H='juniInetRouteDest'
_G='juniInetRouteDestType'
_F='Unsigned32'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='Juniper-INET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressIPv6,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniInetMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,82))
if mibBuilder.loadTexts:juniInetMIB.setRevisions(('2010-08-03 09:30',))
_JuniInetObjects_ObjectIdentity=ObjectIdentity
juniInetObjects=_JuniInetObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,82,1))
_JuniInetRoute_ObjectIdentity=ObjectIdentity
juniInetRoute=_JuniInetRoute_ObjectIdentity((1,3,6,1,4,1,4874,2,2,82,1,1))
_JuniInetStaticRouteTable_Object=MibTable
juniInetStaticRouteTable=_JuniInetStaticRouteTable_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1))
if mibBuilder.loadTexts:juniInetStaticRouteTable.setStatus(_A)
_JuniInetStaticRouteEntry_Object=MibTableRow
juniInetStaticRouteEntry=_JuniInetStaticRouteEntry_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1))
juniInetStaticRouteEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:juniInetStaticRouteEntry.setStatus(_A)
_JuniInetRouteDestType_Type=InetAddressType
_JuniInetRouteDestType_Object=MibTableColumn
juniInetRouteDestType=_JuniInetRouteDestType_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,1),_JuniInetRouteDestType_Type())
juniInetRouteDestType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRouteDestType.setStatus(_A)
_JuniInetRouteDest_Type=InetAddress
_JuniInetRouteDest_Object=MibTableColumn
juniInetRouteDest=_JuniInetRouteDest_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,2),_JuniInetRouteDest_Type())
juniInetRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRouteDest.setStatus(_A)
_JuniInetRoutePfxLen_Type=InetAddressPrefixLength
_JuniInetRoutePfxLen_Object=MibTableColumn
juniInetRoutePfxLen=_JuniInetRoutePfxLen_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,3),_JuniInetRoutePfxLen_Type())
juniInetRoutePfxLen.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRoutePfxLen.setStatus(_A)
_JuniInetRoutePolicy_Type=ObjectIdentifier
_JuniInetRoutePolicy_Object=MibTableColumn
juniInetRoutePolicy=_JuniInetRoutePolicy_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,4),_JuniInetRoutePolicy_Type())
juniInetRoutePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRoutePolicy.setStatus(_A)
_JuniInetRouteNextHopType_Type=InetAddressType
_JuniInetRouteNextHopType_Object=MibTableColumn
juniInetRouteNextHopType=_JuniInetRouteNextHopType_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,5),_JuniInetRouteNextHopType_Type())
juniInetRouteNextHopType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRouteNextHopType.setStatus(_A)
_JuniInetRouteNextHop_Type=InetAddress
_JuniInetRouteNextHop_Object=MibTableColumn
juniInetRouteNextHop=_JuniInetRouteNextHop_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,6),_JuniInetRouteNextHop_Type())
juniInetRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:juniInetRouteNextHop.setStatus(_A)
class _JuniInetRouteStaticPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniInetRouteStaticPref_Type.__name__=_C
_JuniInetRouteStaticPref_Object=MibTableColumn
juniInetRouteStaticPref=_JuniInetRouteStaticPref_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,7),_JuniInetRouteStaticPref_Type())
juniInetRouteStaticPref.setMaxAccess(_N)
if mibBuilder.loadTexts:juniInetRouteStaticPref.setStatus(_A)
_JuniInetRouteStaticRowStatus_Type=RowStatus
_JuniInetRouteStaticRowStatus_Object=MibTableColumn
juniInetRouteStaticRowStatus=_JuniInetRouteStaticRowStatus_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,8),_JuniInetRouteStaticRowStatus_Type())
juniInetRouteStaticRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteStaticRowStatus.setStatus(_A)
_JuniInetRouteIfIndex_Type=InterfaceIndexOrZero
_JuniInetRouteIfIndex_Object=MibTableColumn
juniInetRouteIfIndex=_JuniInetRouteIfIndex_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,9),_JuniInetRouteIfIndex_Type())
juniInetRouteIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteIfIndex.setStatus(_A)
class _JuniInetRouteStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('active',0),('inactive',1),('incomplete',2)))
_JuniInetRouteStaticStatus_Type.__name__=_C
_JuniInetRouteStaticStatus_Object=MibTableColumn
juniInetRouteStaticStatus=_JuniInetRouteStaticStatus_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,10),_JuniInetRouteStaticStatus_Type())
juniInetRouteStaticStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:juniInetRouteStaticStatus.setStatus(_A)
class _JuniInetRouteStaticNextHopAS_Type(Integer32):defaultValue=0
_JuniInetRouteStaticNextHopAS_Type.__name__=_C
_JuniInetRouteStaticNextHopAS_Object=MibTableColumn
juniInetRouteStaticNextHopAS=_JuniInetRouteStaticNextHopAS_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,11),_JuniInetRouteStaticNextHopAS_Type())
juniInetRouteStaticNextHopAS.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteStaticNextHopAS.setStatus(_A)
class _JuniInetRouteStaticMetric_Type(Integer32):defaultValue=-1
_JuniInetRouteStaticMetric_Type.__name__=_C
_JuniInetRouteStaticMetric_Object=MibTableColumn
juniInetRouteStaticMetric=_JuniInetRouteStaticMetric_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,12),_JuniInetRouteStaticMetric_Type())
juniInetRouteStaticMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteStaticMetric.setStatus(_A)
class _JuniInetRouteStaticTag_Type(Unsigned32):defaultValue=0
_JuniInetRouteStaticTag_Type.__name__=_F
_JuniInetRouteStaticTag_Object=MibTableColumn
juniInetRouteStaticTag=_JuniInetRouteStaticTag_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,13),_JuniInetRouteStaticTag_Type())
juniInetRouteStaticTag.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteStaticTag.setStatus(_A)
class _JuniInetRouteStaticNullIntf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('reject',2)))
_JuniInetRouteStaticNullIntf_Type.__name__=_C
_JuniInetRouteStaticNullIntf_Object=MibTableColumn
juniInetRouteStaticNullIntf=_JuniInetRouteStaticNullIntf_Object((1,3,6,1,4,1,4874,2,2,82,1,1,1,1,14),_JuniInetRouteStaticNullIntf_Type())
juniInetRouteStaticNullIntf.setMaxAccess(_E)
if mibBuilder.loadTexts:juniInetRouteStaticNullIntf.setStatus(_A)
_JuniInetConformance_ObjectIdentity=ObjectIdentity
juniInetConformance=_JuniInetConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,82,2))
_JuniInetCompliances_ObjectIdentity=ObjectIdentity
juniInetCompliances=_JuniInetCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,82,2,1))
_JuniInetGroups_ObjectIdentity=ObjectIdentity
juniInetGroups=_JuniInetGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,82,2,2))
juniInetRouteGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,82,2,2,1))
juniInetRouteGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:juniInetRouteGroup.setStatus(_A)
juniInetCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,82,2,1,1))
juniInetCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:juniInetCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniInetMIB':juniInetMIB,'juniInetObjects':juniInetObjects,'juniInetRoute':juniInetRoute,'juniInetStaticRouteTable':juniInetStaticRouteTable,'juniInetStaticRouteEntry':juniInetStaticRouteEntry,_G:juniInetRouteDestType,_H:juniInetRouteDest,_I:juniInetRoutePfxLen,_J:juniInetRoutePolicy,_K:juniInetRouteNextHopType,_L:juniInetRouteNextHop,_M:juniInetRouteStaticPref,_O:juniInetRouteStaticRowStatus,_P:juniInetRouteIfIndex,_Q:juniInetRouteStaticStatus,_R:juniInetRouteStaticNextHopAS,_S:juniInetRouteStaticMetric,_T:juniInetRouteStaticTag,_U:juniInetRouteStaticNullIntf,'juniInetConformance':juniInetConformance,'juniInetCompliances':juniInetCompliances,'juniInetCompliance':juniInetCompliance,'juniInetGroups':juniInetGroups,_V:juniInetRouteGroup})