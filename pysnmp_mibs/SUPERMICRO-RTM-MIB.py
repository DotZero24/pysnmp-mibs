_g='fsRtmCommonRouteNextHop'
_f='fsRtmCommonRouteTos'
_e='fsRtmCommonRouteMask'
_d='fsRtmCommonRouteDest'
_c='fsRrdRoutingProtoId'
_b='fsRrdControlNetMask'
_a='fsRrdControlDestIpAddress'
_Z='Unsigned32'
_Y='ciscoEigrp'
_X='idpr'
_W='bgp'
_V='ospf'
_U='bbnSpfIgp'
_T='ciscoIgrp'
_S='esIs'
_R='isIs'
_Q='rip'
_P='hello'
_O='ggp'
_N='egp'
_M='icmp'
_L='netmgmt'
_K='disable'
_J='enable'
_I='local'
_H='other'
_G='read-create'
_F='read-only'
_E='not-accessible'
_D='SUPERMICRO-RTM-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
futurertm=ModuleIdentity((1,3,6,1,4,1,10876,101,1,107))
if mibBuilder.loadTexts:futurertm.setRevisions(('2012-09-05 00:00',))
_FsrrdScalar_ObjectIdentity=ObjectIdentity
fsrrdScalar=_FsrrdScalar_ObjectIdentity((1,3,6,1,4,1,10876,101,1,107,1))
_FsRrdRouterId_Type=IpAddress
_FsRrdRouterId_Object=MibScalar
fsRrdRouterId=_FsRrdRouterId_Object((1,3,6,1,4,1,10876,101,1,107,1,1),_FsRrdRouterId_Type())
fsRrdRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdRouterId.setStatus(_A)
class _FsRrdFilterByOspfTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsRrdFilterByOspfTag_Type.__name__=_B
_FsRrdFilterByOspfTag_Object=MibScalar
fsRrdFilterByOspfTag=_FsRrdFilterByOspfTag_Object((1,3,6,1,4,1,10876,101,1,107,1,2),_FsRrdFilterByOspfTag_Type())
fsRrdFilterByOspfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdFilterByOspfTag.setStatus(_A)
_FsRrdFilterOspfTag_Type=Integer32
_FsRrdFilterOspfTag_Object=MibScalar
fsRrdFilterOspfTag=_FsRrdFilterOspfTag_Object((1,3,6,1,4,1,10876,101,1,107,1,3),_FsRrdFilterOspfTag_Type())
fsRrdFilterOspfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdFilterOspfTag.setStatus(_A)
class _FsRrdFilterOspfTagMask_Type(Integer32):defaultValue=-1
_FsRrdFilterOspfTagMask_Type.__name__=_B
_FsRrdFilterOspfTagMask_Object=MibScalar
fsRrdFilterOspfTagMask=_FsRrdFilterOspfTagMask_Object((1,3,6,1,4,1,10876,101,1,107,1,4),_FsRrdFilterOspfTagMask_Type())
fsRrdFilterOspfTagMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdFilterOspfTagMask.setStatus(_A)
class _FsRrdRouterASNumber_Type(Integer32):defaultValue=0
_FsRrdRouterASNumber_Type.__name__=_B
_FsRrdRouterASNumber_Object=MibScalar
fsRrdRouterASNumber=_FsRrdRouterASNumber_Object((1,3,6,1,4,1,10876,101,1,107,1,5),_FsRrdRouterASNumber_Type())
fsRrdRouterASNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdRouterASNumber.setStatus(_A)
class _FsRrdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsRrdAdminStatus_Type.__name__=_B
_FsRrdAdminStatus_Object=MibScalar
fsRrdAdminStatus=_FsRrdAdminStatus_Object((1,3,6,1,4,1,10876,101,1,107,1,6),_FsRrdAdminStatus_Type())
fsRrdAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdAdminStatus.setStatus(_A)
class _FsRtmThrottleLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRtmThrottleLimit_Type.__name__=_Z
_FsRtmThrottleLimit_Object=MibScalar
fsRtmThrottleLimit=_FsRtmThrottleLimit_Object((1,3,6,1,4,1,10876,101,1,107,1,7),_FsRtmThrottleLimit_Type())
fsRtmThrottleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRtmThrottleLimit.setStatus(_A)
_FsRrdControlTable_Object=MibTable
fsRrdControlTable=_FsRrdControlTable_Object((1,3,6,1,4,1,10876,101,1,107,2))
if mibBuilder.loadTexts:fsRrdControlTable.setStatus(_A)
_FsRrdControlEntry_Object=MibTableRow
fsRrdControlEntry=_FsRrdControlEntry_Object((1,3,6,1,4,1,10876,101,1,107,2,1))
fsRrdControlEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:fsRrdControlEntry.setStatus(_A)
_FsRrdControlDestIpAddress_Type=IpAddress
_FsRrdControlDestIpAddress_Object=MibTableColumn
fsRrdControlDestIpAddress=_FsRrdControlDestIpAddress_Object((1,3,6,1,4,1,10876,101,1,107,2,1,1),_FsRrdControlDestIpAddress_Type())
fsRrdControlDestIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRrdControlDestIpAddress.setStatus(_A)
_FsRrdControlNetMask_Type=IpAddress
_FsRrdControlNetMask_Object=MibTableColumn
fsRrdControlNetMask=_FsRrdControlNetMask_Object((1,3,6,1,4,1,10876,101,1,107,2,1,2),_FsRrdControlNetMask_Type())
fsRrdControlNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRrdControlNetMask.setStatus(_A)
class _FsRrdControlSourceProto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('any',0),(_H,1),(_I,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16)))
_FsRrdControlSourceProto_Type.__name__=_B
_FsRrdControlSourceProto_Object=MibTableColumn
fsRrdControlSourceProto=_FsRrdControlSourceProto_Object((1,3,6,1,4,1,10876,101,1,107,2,1,3),_FsRrdControlSourceProto_Type())
fsRrdControlSourceProto.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdControlSourceProto.setStatus(_A)
class _FsRrdControlDestProto_Type(Integer32):defaultValue=0
_FsRrdControlDestProto_Type.__name__=_B
_FsRrdControlDestProto_Object=MibTableColumn
fsRrdControlDestProto=_FsRrdControlDestProto_Object((1,3,6,1,4,1,10876,101,1,107,2,1,4),_FsRrdControlDestProto_Type())
fsRrdControlDestProto.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdControlDestProto.setStatus(_A)
class _FsRrdControlRouteExportFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsRrdControlRouteExportFlag_Type.__name__=_B
_FsRrdControlRouteExportFlag_Object=MibTableColumn
fsRrdControlRouteExportFlag=_FsRrdControlRouteExportFlag_Object((1,3,6,1,4,1,10876,101,1,107,2,1,5),_FsRrdControlRouteExportFlag_Type())
fsRrdControlRouteExportFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdControlRouteExportFlag.setStatus(_A)
_FsRrdControlRowStatus_Type=RowStatus
_FsRrdControlRowStatus_Object=MibTableColumn
fsRrdControlRowStatus=_FsRrdControlRowStatus_Object((1,3,6,1,4,1,10876,101,1,107,2,1,6),_FsRrdControlRowStatus_Type())
fsRrdControlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdControlRowStatus.setStatus(_A)
_FsRrdRoutingProtoTable_Object=MibTable
fsRrdRoutingProtoTable=_FsRrdRoutingProtoTable_Object((1,3,6,1,4,1,10876,101,1,107,3))
if mibBuilder.loadTexts:fsRrdRoutingProtoTable.setStatus(_A)
_FsRrdRoutingProtoEntry_Object=MibTableRow
fsRrdRoutingProtoEntry=_FsRrdRoutingProtoEntry_Object((1,3,6,1,4,1,10876,101,1,107,3,1))
fsRrdRoutingProtoEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:fsRrdRoutingProtoEntry.setStatus(_A)
class _FsRrdRoutingProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_H,1),(_I,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16)))
_FsRrdRoutingProtoId_Type.__name__=_B
_FsRrdRoutingProtoId_Object=MibTableColumn
fsRrdRoutingProtoId=_FsRrdRoutingProtoId_Object((1,3,6,1,4,1,10876,101,1,107,3,1,1),_FsRrdRoutingProtoId_Type())
fsRrdRoutingProtoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRrdRoutingProtoId.setStatus(_A)
_FsRrdRoutingRegnId_Type=Integer32
_FsRrdRoutingRegnId_Object=MibTableColumn
fsRrdRoutingRegnId=_FsRrdRoutingRegnId_Object((1,3,6,1,4,1,10876,101,1,107,3,1,2),_FsRrdRoutingRegnId_Type())
fsRrdRoutingRegnId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRrdRoutingRegnId.setStatus(_A)
_FsRrdRoutingProtoTaskIdent_Type=OctetString
_FsRrdRoutingProtoTaskIdent_Object=MibTableColumn
fsRrdRoutingProtoTaskIdent=_FsRrdRoutingProtoTaskIdent_Object((1,3,6,1,4,1,10876,101,1,107,3,1,3),_FsRrdRoutingProtoTaskIdent_Type())
fsRrdRoutingProtoTaskIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRrdRoutingProtoTaskIdent.setStatus(_A)
_FsRrdRoutingProtoQueueIdent_Type=OctetString
_FsRrdRoutingProtoQueueIdent_Object=MibTableColumn
fsRrdRoutingProtoQueueIdent=_FsRrdRoutingProtoQueueIdent_Object((1,3,6,1,4,1,10876,101,1,107,3,1,4),_FsRrdRoutingProtoQueueIdent_Type())
fsRrdRoutingProtoQueueIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRrdRoutingProtoQueueIdent.setStatus(_A)
class _FsRrdAllowOspfAreaRoutes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsRrdAllowOspfAreaRoutes_Type.__name__=_B
_FsRrdAllowOspfAreaRoutes_Object=MibTableColumn
fsRrdAllowOspfAreaRoutes=_FsRrdAllowOspfAreaRoutes_Object((1,3,6,1,4,1,10876,101,1,107,3,1,5),_FsRrdAllowOspfAreaRoutes_Type())
fsRrdAllowOspfAreaRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdAllowOspfAreaRoutes.setStatus(_A)
class _FsRrdAllowOspfExtRoutes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsRrdAllowOspfExtRoutes_Type.__name__=_B
_FsRrdAllowOspfExtRoutes_Object=MibTableColumn
fsRrdAllowOspfExtRoutes=_FsRrdAllowOspfExtRoutes_Object((1,3,6,1,4,1,10876,101,1,107,3,1,6),_FsRrdAllowOspfExtRoutes_Type())
fsRrdAllowOspfExtRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRrdAllowOspfExtRoutes.setStatus(_A)
_FsRtmCommonRouteTable_Object=MibTable
fsRtmCommonRouteTable=_FsRtmCommonRouteTable_Object((1,3,6,1,4,1,10876,101,1,107,4))
if mibBuilder.loadTexts:fsRtmCommonRouteTable.setStatus(_A)
_FsRtmCommonRouteEntry_Object=MibTableRow
fsRtmCommonRouteEntry=_FsRtmCommonRouteEntry_Object((1,3,6,1,4,1,10876,101,1,107,4,1))
fsRtmCommonRouteEntry.setIndexNames((0,_D,_d),(0,_D,_e),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:fsRtmCommonRouteEntry.setStatus(_A)
_FsRtmCommonRouteDest_Type=IpAddress
_FsRtmCommonRouteDest_Object=MibTableColumn
fsRtmCommonRouteDest=_FsRtmCommonRouteDest_Object((1,3,6,1,4,1,10876,101,1,107,4,1,1),_FsRtmCommonRouteDest_Type())
fsRtmCommonRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRtmCommonRouteDest.setStatus(_A)
_FsRtmCommonRouteMask_Type=IpAddress
_FsRtmCommonRouteMask_Object=MibTableColumn
fsRtmCommonRouteMask=_FsRtmCommonRouteMask_Object((1,3,6,1,4,1,10876,101,1,107,4,1,2),_FsRtmCommonRouteMask_Type())
fsRtmCommonRouteMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRtmCommonRouteMask.setStatus(_A)
class _FsRtmCommonRouteTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsRtmCommonRouteTos_Type.__name__=_B
_FsRtmCommonRouteTos_Object=MibTableColumn
fsRtmCommonRouteTos=_FsRtmCommonRouteTos_Object((1,3,6,1,4,1,10876,101,1,107,4,1,3),_FsRtmCommonRouteTos_Type())
fsRtmCommonRouteTos.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRtmCommonRouteTos.setStatus(_A)
_FsRtmCommonRouteNextHop_Type=IpAddress
_FsRtmCommonRouteNextHop_Object=MibTableColumn
fsRtmCommonRouteNextHop=_FsRtmCommonRouteNextHop_Object((1,3,6,1,4,1,10876,101,1,107,4,1,4),_FsRtmCommonRouteNextHop_Type())
fsRtmCommonRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRtmCommonRouteNextHop.setStatus(_A)
class _FsRtmCommonRouteIfIndex_Type(Integer32):defaultValue=0
_FsRtmCommonRouteIfIndex_Type.__name__=_B
_FsRtmCommonRouteIfIndex_Object=MibTableColumn
fsRtmCommonRouteIfIndex=_FsRtmCommonRouteIfIndex_Object((1,3,6,1,4,1,10876,101,1,107,4,1,5),_FsRtmCommonRouteIfIndex_Type())
fsRtmCommonRouteIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteIfIndex.setStatus(_A)
class _FsRtmCommonRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('reject',2),(_I,3),('remote',4)))
_FsRtmCommonRouteType_Type.__name__=_B
_FsRtmCommonRouteType_Object=MibTableColumn
fsRtmCommonRouteType=_FsRtmCommonRouteType_Object((1,3,6,1,4,1,10876,101,1,107,4,1,6),_FsRtmCommonRouteType_Type())
fsRtmCommonRouteType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteType.setStatus(_A)
class _FsRtmCommonRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_H,1),(_I,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16)))
_FsRtmCommonRouteProto_Type.__name__=_B
_FsRtmCommonRouteProto_Object=MibTableColumn
fsRtmCommonRouteProto=_FsRtmCommonRouteProto_Object((1,3,6,1,4,1,10876,101,1,107,4,1,7),_FsRtmCommonRouteProto_Type())
fsRtmCommonRouteProto.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRtmCommonRouteProto.setStatus(_A)
class _FsRtmCommonRouteAge_Type(Integer32):defaultValue=0
_FsRtmCommonRouteAge_Type.__name__=_B
_FsRtmCommonRouteAge_Object=MibTableColumn
fsRtmCommonRouteAge=_FsRtmCommonRouteAge_Object((1,3,6,1,4,1,10876,101,1,107,4,1,8),_FsRtmCommonRouteAge_Type())
fsRtmCommonRouteAge.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRtmCommonRouteAge.setStatus(_A)
_FsRtmCommonRouteInfo_Type=ObjectIdentifier
_FsRtmCommonRouteInfo_Object=MibTableColumn
fsRtmCommonRouteInfo=_FsRtmCommonRouteInfo_Object((1,3,6,1,4,1,10876,101,1,107,4,1,9),_FsRtmCommonRouteInfo_Type())
fsRtmCommonRouteInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteInfo.setStatus(_A)
class _FsRtmCommonRouteNextHopAS_Type(Integer32):defaultValue=0
_FsRtmCommonRouteNextHopAS_Type.__name__=_B
_FsRtmCommonRouteNextHopAS_Object=MibTableColumn
fsRtmCommonRouteNextHopAS=_FsRtmCommonRouteNextHopAS_Object((1,3,6,1,4,1,10876,101,1,107,4,1,10),_FsRtmCommonRouteNextHopAS_Type())
fsRtmCommonRouteNextHopAS.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteNextHopAS.setStatus(_A)
class _FsRtmCommonRouteMetric1_Type(Integer32):defaultValue=-1
_FsRtmCommonRouteMetric1_Type.__name__=_B
_FsRtmCommonRouteMetric1_Object=MibTableColumn
fsRtmCommonRouteMetric1=_FsRtmCommonRouteMetric1_Object((1,3,6,1,4,1,10876,101,1,107,4,1,11),_FsRtmCommonRouteMetric1_Type())
fsRtmCommonRouteMetric1.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteMetric1.setStatus(_A)
_FsRtmCommonRoutePrivateStatus_Type=TruthValue
_FsRtmCommonRoutePrivateStatus_Object=MibTableColumn
fsRtmCommonRoutePrivateStatus=_FsRtmCommonRoutePrivateStatus_Object((1,3,6,1,4,1,10876,101,1,107,4,1,12),_FsRtmCommonRoutePrivateStatus_Type())
fsRtmCommonRoutePrivateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRoutePrivateStatus.setStatus(_A)
_FsRtmCommonRouteStatus_Type=RowStatus
_FsRtmCommonRouteStatus_Object=MibTableColumn
fsRtmCommonRouteStatus=_FsRtmCommonRouteStatus_Object((1,3,6,1,4,1,10876,101,1,107,4,1,13),_FsRtmCommonRouteStatus_Type())
fsRtmCommonRouteStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsRtmCommonRouteStatus.setStatus(_A)
class _FsRtmCommonRouteProvider_Type(Integer32):defaultValue=0
_FsRtmCommonRouteProvider_Type.__name__=_B
_FsRtmCommonRouteProvider_Object=MibTableColumn
fsRtmCommonRouteProvider=_FsRtmCommonRouteProvider_Object((1,3,6,1,4,1,10876,101,1,107,4,1,14),_FsRtmCommonRouteProvider_Type())
fsRtmCommonRouteProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRtmCommonRouteProvider.setStatus(_A)
_FsRtmRedTest_ObjectIdentity=ObjectIdentity
fsRtmRedTest=_FsRtmRedTest_ObjectIdentity((1,3,6,1,4,1,10876,101,1,107,5))
_FsRtmRedEntryTime_Type=Integer32
_FsRtmRedEntryTime_Object=MibScalar
fsRtmRedEntryTime=_FsRtmRedEntryTime_Object((1,3,6,1,4,1,10876,101,1,107,5,1),_FsRtmRedEntryTime_Type())
fsRtmRedEntryTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRtmRedEntryTime.setStatus(_A)
_FsRtmRedExitTime_Type=Integer32
_FsRtmRedExitTime_Object=MibScalar
fsRtmRedExitTime=_FsRtmRedExitTime_Object((1,3,6,1,4,1,10876,101,1,107,5,2),_FsRtmRedExitTime_Type())
fsRtmRedExitTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRtmRedExitTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'futurertm':futurertm,'fsrrdScalar':fsrrdScalar,'fsRrdRouterId':fsRrdRouterId,'fsRrdFilterByOspfTag':fsRrdFilterByOspfTag,'fsRrdFilterOspfTag':fsRrdFilterOspfTag,'fsRrdFilterOspfTagMask':fsRrdFilterOspfTagMask,'fsRrdRouterASNumber':fsRrdRouterASNumber,'fsRrdAdminStatus':fsRrdAdminStatus,'fsRtmThrottleLimit':fsRtmThrottleLimit,'fsRrdControlTable':fsRrdControlTable,'fsRrdControlEntry':fsRrdControlEntry,_a:fsRrdControlDestIpAddress,_b:fsRrdControlNetMask,'fsRrdControlSourceProto':fsRrdControlSourceProto,'fsRrdControlDestProto':fsRrdControlDestProto,'fsRrdControlRouteExportFlag':fsRrdControlRouteExportFlag,'fsRrdControlRowStatus':fsRrdControlRowStatus,'fsRrdRoutingProtoTable':fsRrdRoutingProtoTable,'fsRrdRoutingProtoEntry':fsRrdRoutingProtoEntry,_c:fsRrdRoutingProtoId,'fsRrdRoutingRegnId':fsRrdRoutingRegnId,'fsRrdRoutingProtoTaskIdent':fsRrdRoutingProtoTaskIdent,'fsRrdRoutingProtoQueueIdent':fsRrdRoutingProtoQueueIdent,'fsRrdAllowOspfAreaRoutes':fsRrdAllowOspfAreaRoutes,'fsRrdAllowOspfExtRoutes':fsRrdAllowOspfExtRoutes,'fsRtmCommonRouteTable':fsRtmCommonRouteTable,'fsRtmCommonRouteEntry':fsRtmCommonRouteEntry,_d:fsRtmCommonRouteDest,_e:fsRtmCommonRouteMask,_f:fsRtmCommonRouteTos,_g:fsRtmCommonRouteNextHop,'fsRtmCommonRouteIfIndex':fsRtmCommonRouteIfIndex,'fsRtmCommonRouteType':fsRtmCommonRouteType,'fsRtmCommonRouteProto':fsRtmCommonRouteProto,'fsRtmCommonRouteAge':fsRtmCommonRouteAge,'fsRtmCommonRouteInfo':fsRtmCommonRouteInfo,'fsRtmCommonRouteNextHopAS':fsRtmCommonRouteNextHopAS,'fsRtmCommonRouteMetric1':fsRtmCommonRouteMetric1,'fsRtmCommonRoutePrivateStatus':fsRtmCommonRoutePrivateStatus,'fsRtmCommonRouteStatus':fsRtmCommonRouteStatus,'fsRtmCommonRouteProvider':fsRtmCommonRouteProvider,'fsRtmRedTest':fsRtmRedTest,'fsRtmRedEntryTime':fsRtmRedEntryTime,'fsRtmRedExitTime':fsRtmRedExitTime})