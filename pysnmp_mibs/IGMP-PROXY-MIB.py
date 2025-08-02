_N='fsIgmpProxyQuerierAddress'
_M='fsIgmpProxyQuerierIfIndex'
_L='fsIgmpProxyNextHopIndex'
_K='fsIgmpProxyNextHopGroup'
_J='fsIgmpProxyNextHopSource'
_I='fsIgmpProxyMRouteGroup'
_H='fsIgmpProxyMRouteSource'
_G='fsIgmpProxyRtrIfaceIndex'
_F='read-write'
_E='not-accessible'
_D='IGMP-PROXY-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsigmpproxy=ModuleIdentity((1,3,6,1,4,1,10876,101,1,124))
if mibBuilder.loadTexts:fsigmpproxy.setRevisions(('2012-09-05 00:00',))
_FsigmpproxyStatus_ObjectIdentity=ObjectIdentity
fsigmpproxyStatus=_FsigmpproxyStatus_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,1))
class _FsIgmpProxyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsIgmpProxyStatus_Type.__name__=_C
_FsIgmpProxyStatus_Object=MibScalar
fsIgmpProxyStatus=_FsIgmpProxyStatus_Object((1,3,6,1,4,1,10876,101,1,124,1,1),_FsIgmpProxyStatus_Type())
fsIgmpProxyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpProxyStatus.setStatus(_A)
_FsigmpproxyRtr_ObjectIdentity=ObjectIdentity
fsigmpproxyRtr=_FsigmpproxyRtr_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,2))
_FsIgmpProxyRtrIfaceTable_Object=MibTable
fsIgmpProxyRtrIfaceTable=_FsIgmpProxyRtrIfaceTable_Object((1,3,6,1,4,1,10876,101,1,124,2,1))
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceTable.setStatus(_A)
_FsIgmpProxyRtrIfaceEntry_Object=MibTableRow
fsIgmpProxyRtrIfaceEntry=_FsIgmpProxyRtrIfaceEntry_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1))
fsIgmpProxyRtrIfaceEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceEntry.setStatus(_A)
class _FsIgmpProxyRtrIfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIgmpProxyRtrIfaceIndex_Type.__name__=_C
_FsIgmpProxyRtrIfaceIndex_Object=MibTableColumn
fsIgmpProxyRtrIfaceIndex=_FsIgmpProxyRtrIfaceIndex_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,1),_FsIgmpProxyRtrIfaceIndex_Type())
fsIgmpProxyRtrIfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceIndex.setStatus(_A)
class _FsIgmpProxyRtrIfaceOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_FsIgmpProxyRtrIfaceOperVersion_Type.__name__=_C
_FsIgmpProxyRtrIfaceOperVersion_Object=MibTableColumn
fsIgmpProxyRtrIfaceOperVersion=_FsIgmpProxyRtrIfaceOperVersion_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,2),_FsIgmpProxyRtrIfaceOperVersion_Type())
fsIgmpProxyRtrIfaceOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceOperVersion.setStatus(_A)
class _FsIgmpProxyRtrIfaceCfgOperVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_FsIgmpProxyRtrIfaceCfgOperVersion_Type.__name__=_C
_FsIgmpProxyRtrIfaceCfgOperVersion_Object=MibTableColumn
fsIgmpProxyRtrIfaceCfgOperVersion=_FsIgmpProxyRtrIfaceCfgOperVersion_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,3),_FsIgmpProxyRtrIfaceCfgOperVersion_Type())
fsIgmpProxyRtrIfaceCfgOperVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceCfgOperVersion.setStatus(_A)
class _FsIgmpProxyRtrIfacePurgeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_FsIgmpProxyRtrIfacePurgeInterval_Type.__name__=_C
_FsIgmpProxyRtrIfacePurgeInterval_Object=MibTableColumn
fsIgmpProxyRtrIfacePurgeInterval=_FsIgmpProxyRtrIfacePurgeInterval_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,4),_FsIgmpProxyRtrIfacePurgeInterval_Type())
fsIgmpProxyRtrIfacePurgeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfacePurgeInterval.setStatus(_A)
_FsIgmpProxyRtrIfaceUpTime_Type=TimeTicks
_FsIgmpProxyRtrIfaceUpTime_Object=MibTableColumn
fsIgmpProxyRtrIfaceUpTime=_FsIgmpProxyRtrIfaceUpTime_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,5),_FsIgmpProxyRtrIfaceUpTime_Type())
fsIgmpProxyRtrIfaceUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceUpTime.setStatus(_A)
_FsIgmpProxyRtrIfaceExpiryTime_Type=TimeTicks
_FsIgmpProxyRtrIfaceExpiryTime_Object=MibTableColumn
fsIgmpProxyRtrIfaceExpiryTime=_FsIgmpProxyRtrIfaceExpiryTime_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,6),_FsIgmpProxyRtrIfaceExpiryTime_Type())
fsIgmpProxyRtrIfaceExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceExpiryTime.setStatus(_A)
_FsIgmpProxyRtrIfaceRowStatus_Type=RowStatus
_FsIgmpProxyRtrIfaceRowStatus_Object=MibTableColumn
fsIgmpProxyRtrIfaceRowStatus=_FsIgmpProxyRtrIfaceRowStatus_Object((1,3,6,1,4,1,10876,101,1,124,2,1,1,7),_FsIgmpProxyRtrIfaceRowStatus_Type())
fsIgmpProxyRtrIfaceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIgmpProxyRtrIfaceRowStatus.setStatus(_A)
_FsigmpproxyMRoute_ObjectIdentity=ObjectIdentity
fsigmpproxyMRoute=_FsigmpproxyMRoute_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,3))
_FsIgmpProxyMrouteTable_Object=MibTable
fsIgmpProxyMrouteTable=_FsIgmpProxyMrouteTable_Object((1,3,6,1,4,1,10876,101,1,124,3,1))
if mibBuilder.loadTexts:fsIgmpProxyMrouteTable.setStatus(_A)
_FsIgmpProxyMrouteEntry_Object=MibTableRow
fsIgmpProxyMrouteEntry=_FsIgmpProxyMrouteEntry_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1))
fsIgmpProxyMrouteEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:fsIgmpProxyMrouteEntry.setStatus(_A)
_FsIgmpProxyMRouteSource_Type=IpAddress
_FsIgmpProxyMRouteSource_Object=MibTableColumn
fsIgmpProxyMRouteSource=_FsIgmpProxyMRouteSource_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1,1),_FsIgmpProxyMRouteSource_Type())
fsIgmpProxyMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyMRouteSource.setStatus(_A)
_FsIgmpProxyMRouteGroup_Type=IpAddress
_FsIgmpProxyMRouteGroup_Object=MibTableColumn
fsIgmpProxyMRouteGroup=_FsIgmpProxyMRouteGroup_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1,2),_FsIgmpProxyMRouteGroup_Type())
fsIgmpProxyMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyMRouteGroup.setStatus(_A)
_FsIgmpProxyMRouteIifIndex_Type=Integer32
_FsIgmpProxyMRouteIifIndex_Object=MibTableColumn
fsIgmpProxyMRouteIifIndex=_FsIgmpProxyMRouteIifIndex_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1,3),_FsIgmpProxyMRouteIifIndex_Type())
fsIgmpProxyMRouteIifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyMRouteIifIndex.setStatus(_A)
_FsIgmpProxyMRouteUpTime_Type=TimeTicks
_FsIgmpProxyMRouteUpTime_Object=MibTableColumn
fsIgmpProxyMRouteUpTime=_FsIgmpProxyMRouteUpTime_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1,4),_FsIgmpProxyMRouteUpTime_Type())
fsIgmpProxyMRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyMRouteUpTime.setStatus(_A)
_FsIgmpProxyMRouteExpiryTime_Type=TimeTicks
_FsIgmpProxyMRouteExpiryTime_Object=MibTableColumn
fsIgmpProxyMRouteExpiryTime=_FsIgmpProxyMRouteExpiryTime_Object((1,3,6,1,4,1,10876,101,1,124,3,1,1,5),_FsIgmpProxyMRouteExpiryTime_Type())
fsIgmpProxyMRouteExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyMRouteExpiryTime.setStatus(_A)
_FsIgmpProxyNextHopTable_Object=MibTable
fsIgmpProxyNextHopTable=_FsIgmpProxyNextHopTable_Object((1,3,6,1,4,1,10876,101,1,124,3,2))
if mibBuilder.loadTexts:fsIgmpProxyNextHopTable.setStatus(_A)
_FsIgmpProxyNextHopEntry_Object=MibTableRow
fsIgmpProxyNextHopEntry=_FsIgmpProxyNextHopEntry_Object((1,3,6,1,4,1,10876,101,1,124,3,2,1))
fsIgmpProxyNextHopEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:fsIgmpProxyNextHopEntry.setStatus(_A)
_FsIgmpProxyNextHopSource_Type=IpAddress
_FsIgmpProxyNextHopSource_Object=MibTableColumn
fsIgmpProxyNextHopSource=_FsIgmpProxyNextHopSource_Object((1,3,6,1,4,1,10876,101,1,124,3,2,1,1),_FsIgmpProxyNextHopSource_Type())
fsIgmpProxyNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyNextHopSource.setStatus(_A)
_FsIgmpProxyNextHopGroup_Type=IpAddress
_FsIgmpProxyNextHopGroup_Object=MibTableColumn
fsIgmpProxyNextHopGroup=_FsIgmpProxyNextHopGroup_Object((1,3,6,1,4,1,10876,101,1,124,3,2,1,2),_FsIgmpProxyNextHopGroup_Type())
fsIgmpProxyNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyNextHopGroup.setStatus(_A)
class _FsIgmpProxyNextHopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIgmpProxyNextHopIndex_Type.__name__=_C
_FsIgmpProxyNextHopIndex_Object=MibTableColumn
fsIgmpProxyNextHopIndex=_FsIgmpProxyNextHopIndex_Object((1,3,6,1,4,1,10876,101,1,124,3,2,1,3),_FsIgmpProxyNextHopIndex_Type())
fsIgmpProxyNextHopIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpProxyNextHopIndex.setStatus(_A)
class _FsIgmpProxyNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('pruned',2)))
_FsIgmpProxyNextHopState_Type.__name__=_C
_FsIgmpProxyNextHopState_Object=MibTableColumn
fsIgmpProxyNextHopState=_FsIgmpProxyNextHopState_Object((1,3,6,1,4,1,10876,101,1,124,3,2,1,4),_FsIgmpProxyNextHopState_Type())
fsIgmpProxyNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyNextHopState.setStatus(_A)
_IgmpproxyTrapsControl_ObjectIdentity=ObjectIdentity
igmpproxyTrapsControl=_IgmpproxyTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,5))
_FsIgmpProxyQuerierIfIndex_Type=Integer32
_FsIgmpProxyQuerierIfIndex_Object=MibScalar
fsIgmpProxyQuerierIfIndex=_FsIgmpProxyQuerierIfIndex_Object((1,3,6,1,4,1,10876,101,1,124,5,1),_FsIgmpProxyQuerierIfIndex_Type())
fsIgmpProxyQuerierIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyQuerierIfIndex.setStatus(_A)
_FsIgmpProxyQuerierAddress_Type=IpAddress
_FsIgmpProxyQuerierAddress_Object=MibScalar
fsIgmpProxyQuerierAddress=_FsIgmpProxyQuerierAddress_Object((1,3,6,1,4,1,10876,101,1,124,5,2),_FsIgmpProxyQuerierAddress_Type())
fsIgmpProxyQuerierAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyQuerierAddress.setStatus(_A)
_FsigmpproxyTraps_ObjectIdentity=ObjectIdentity
fsigmpproxyTraps=_FsigmpproxyTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,6))
_FsigmpTraps_ObjectIdentity=ObjectIdentity
fsigmpTraps=_FsigmpTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,6,0))
_FsigmpproxyScalars_ObjectIdentity=ObjectIdentity
fsigmpproxyScalars=_FsigmpproxyScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,124,7))
class _FsIgmpProxyForwardingTblEntryCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIgmpProxyForwardingTblEntryCnt_Type.__name__=_C
_FsIgmpProxyForwardingTblEntryCnt_Object=MibScalar
fsIgmpProxyForwardingTblEntryCnt=_FsIgmpProxyForwardingTblEntryCnt_Object((1,3,6,1,4,1,10876,101,1,124,7,1),_FsIgmpProxyForwardingTblEntryCnt_Type())
fsIgmpProxyForwardingTblEntryCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIgmpProxyForwardingTblEntryCnt.setStatus(_A)
fsIgmpProxyQuerierPresent=NotificationType((1,3,6,1,4,1,10876,101,1,124,6,0,1))
fsIgmpProxyQuerierPresent.setObjects(*((_D,_M),(_D,_N)))
if mibBuilder.loadTexts:fsIgmpProxyQuerierPresent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsigmpproxy':fsigmpproxy,'fsigmpproxyStatus':fsigmpproxyStatus,'fsIgmpProxyStatus':fsIgmpProxyStatus,'fsigmpproxyRtr':fsigmpproxyRtr,'fsIgmpProxyRtrIfaceTable':fsIgmpProxyRtrIfaceTable,'fsIgmpProxyRtrIfaceEntry':fsIgmpProxyRtrIfaceEntry,_G:fsIgmpProxyRtrIfaceIndex,'fsIgmpProxyRtrIfaceOperVersion':fsIgmpProxyRtrIfaceOperVersion,'fsIgmpProxyRtrIfaceCfgOperVersion':fsIgmpProxyRtrIfaceCfgOperVersion,'fsIgmpProxyRtrIfacePurgeInterval':fsIgmpProxyRtrIfacePurgeInterval,'fsIgmpProxyRtrIfaceUpTime':fsIgmpProxyRtrIfaceUpTime,'fsIgmpProxyRtrIfaceExpiryTime':fsIgmpProxyRtrIfaceExpiryTime,'fsIgmpProxyRtrIfaceRowStatus':fsIgmpProxyRtrIfaceRowStatus,'fsigmpproxyMRoute':fsigmpproxyMRoute,'fsIgmpProxyMrouteTable':fsIgmpProxyMrouteTable,'fsIgmpProxyMrouteEntry':fsIgmpProxyMrouteEntry,_H:fsIgmpProxyMRouteSource,_I:fsIgmpProxyMRouteGroup,'fsIgmpProxyMRouteIifIndex':fsIgmpProxyMRouteIifIndex,'fsIgmpProxyMRouteUpTime':fsIgmpProxyMRouteUpTime,'fsIgmpProxyMRouteExpiryTime':fsIgmpProxyMRouteExpiryTime,'fsIgmpProxyNextHopTable':fsIgmpProxyNextHopTable,'fsIgmpProxyNextHopEntry':fsIgmpProxyNextHopEntry,_J:fsIgmpProxyNextHopSource,_K:fsIgmpProxyNextHopGroup,_L:fsIgmpProxyNextHopIndex,'fsIgmpProxyNextHopState':fsIgmpProxyNextHopState,'igmpproxyTrapsControl':igmpproxyTrapsControl,_M:fsIgmpProxyQuerierIfIndex,_N:fsIgmpProxyQuerierAddress,'fsigmpproxyTraps':fsigmpproxyTraps,'fsigmpTraps':fsigmpTraps,'fsIgmpProxyQuerierPresent':fsIgmpProxyQuerierPresent,'fsigmpproxyScalars':fsigmpproxyScalars,'fsIgmpProxyForwardingTblEntryCnt':fsIgmpProxyForwardingTblEntryCnt})