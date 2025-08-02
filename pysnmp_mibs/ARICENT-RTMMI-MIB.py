_j='fsMIRtmCommonRouteNextHop'
_i='fsMIRtmCommonRouteTos'
_h='fsMIRtmCommonRouteMask'
_g='fsMIRtmCommonRouteDest'
_f='fsMIRrdRoutingProtoId'
_e='fsMIRrdControlNetMask'
_d='fsMIRrdControlDestIpAddress'
_c='disabled'
_b='enabled'
_a='Unsigned32'
_Z='ciscoEigrp'
_Y='idpr'
_X='bgp'
_W='ospf'
_V='bbnSpfIgp'
_U='ciscoIgrp'
_T='esIs'
_S='isIs'
_R='rip'
_Q='hello'
_P='ggp'
_O='egp'
_N='icmp'
_M='netmgmt'
_L='local'
_K='other'
_J='fsMIRtmContextId'
_I='disable'
_H='enable'
_G='read-create'
_F='read-only'
_E='not-accessible'
_D='ARICENT-RTMMI-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsMIRtm=ModuleIdentity((1,3,6,1,4,1,29601,2,31))
if mibBuilder.loadTexts:fsMIRtm.setRevisions(('2012-09-11 00:00',))
_FsMIRtmGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIRtmGeneralGroup=_FsMIRtmGeneralGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,31,1))
class _FsMIRtmThrottleLimit_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsMIRtmThrottleLimit_Type.__name__=_a
_FsMIRtmThrottleLimit_Object=MibScalar
fsMIRtmThrottleLimit=_FsMIRtmThrottleLimit_Object((1,3,6,1,4,1,29601,2,31,1,1),_FsMIRtmThrottleLimit_Type())
fsMIRtmThrottleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmThrottleLimit.setStatus(_A)
class _FsMIEcmpAcrossProtocolAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIEcmpAcrossProtocolAdminStatus_Type.__name__=_B
_FsMIEcmpAcrossProtocolAdminStatus_Object=MibScalar
fsMIEcmpAcrossProtocolAdminStatus=_FsMIEcmpAcrossProtocolAdminStatus_Object((1,3,6,1,4,1,29601,2,31,1,2),_FsMIEcmpAcrossProtocolAdminStatus_Type())
fsMIEcmpAcrossProtocolAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIEcmpAcrossProtocolAdminStatus.setStatus(_A)
class _FsMIRtmRouteLeakStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRtmRouteLeakStatus_Type.__name__=_B
_FsMIRtmRouteLeakStatus_Object=MibScalar
fsMIRtmRouteLeakStatus=_FsMIRtmRouteLeakStatus_Object((1,3,6,1,4,1,29601,2,31,1,3),_FsMIRtmRouteLeakStatus_Type())
fsMIRtmRouteLeakStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmRouteLeakStatus.setStatus(_A)
_FsMIRtmTable_Object=MibTable
fsMIRtmTable=_FsMIRtmTable_Object((1,3,6,1,4,1,29601,2,31,2))
if mibBuilder.loadTexts:fsMIRtmTable.setStatus(_A)
_FsMIRtmEntry_Object=MibTableRow
fsMIRtmEntry=_FsMIRtmEntry_Object((1,3,6,1,4,1,29601,2,31,2,1))
fsMIRtmEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fsMIRtmEntry.setStatus(_A)
class _FsMIRtmContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_FsMIRtmContextId_Type.__name__=_B
_FsMIRtmContextId_Object=MibTableColumn
fsMIRtmContextId=_FsMIRtmContextId_Object((1,3,6,1,4,1,29601,2,31,2,1,1),_FsMIRtmContextId_Type())
fsMIRtmContextId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtmContextId.setStatus(_A)
_FsMIRrdRouterId_Type=IpAddress
_FsMIRrdRouterId_Object=MibTableColumn
fsMIRrdRouterId=_FsMIRrdRouterId_Object((1,3,6,1,4,1,29601,2,31,2,1,2),_FsMIRrdRouterId_Type())
fsMIRrdRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdRouterId.setStatus(_A)
class _FsMIRrdFilterByOspfTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrdFilterByOspfTag_Type.__name__=_B
_FsMIRrdFilterByOspfTag_Object=MibTableColumn
fsMIRrdFilterByOspfTag=_FsMIRrdFilterByOspfTag_Object((1,3,6,1,4,1,29601,2,31,2,1,3),_FsMIRrdFilterByOspfTag_Type())
fsMIRrdFilterByOspfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdFilterByOspfTag.setStatus(_A)
_FsMIRrdFilterOspfTag_Type=Integer32
_FsMIRrdFilterOspfTag_Object=MibTableColumn
fsMIRrdFilterOspfTag=_FsMIRrdFilterOspfTag_Object((1,3,6,1,4,1,29601,2,31,2,1,4),_FsMIRrdFilterOspfTag_Type())
fsMIRrdFilterOspfTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdFilterOspfTag.setStatus(_A)
class _FsMIRrdFilterOspfTagMask_Type(Integer32):defaultValue=-1
_FsMIRrdFilterOspfTagMask_Type.__name__=_B
_FsMIRrdFilterOspfTagMask_Object=MibTableColumn
fsMIRrdFilterOspfTagMask=_FsMIRrdFilterOspfTagMask_Object((1,3,6,1,4,1,29601,2,31,2,1,5),_FsMIRrdFilterOspfTagMask_Type())
fsMIRrdFilterOspfTagMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdFilterOspfTagMask.setStatus(_A)
class _FsMIRrdRouterASNumber_Type(Integer32):defaultValue=0
_FsMIRrdRouterASNumber_Type.__name__=_B
_FsMIRrdRouterASNumber_Object=MibTableColumn
fsMIRrdRouterASNumber=_FsMIRrdRouterASNumber_Object((1,3,6,1,4,1,29601,2,31,2,1,6),_FsMIRrdRouterASNumber_Type())
fsMIRrdRouterASNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdRouterASNumber.setStatus(_A)
class _FsMIRrdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_FsMIRrdAdminStatus_Type.__name__=_B
_FsMIRrdAdminStatus_Object=MibTableColumn
fsMIRrdAdminStatus=_FsMIRrdAdminStatus_Object((1,3,6,1,4,1,29601,2,31,2,1,7),_FsMIRrdAdminStatus_Type())
fsMIRrdAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdAdminStatus.setStatus(_A)
class _FsMIRrdForce_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_FsMIRrdForce_Type.__name__=_B
_FsMIRrdForce_Object=MibTableColumn
fsMIRrdForce=_FsMIRrdForce_Object((1,3,6,1,4,1,29601,2,31,2,1,8),_FsMIRrdForce_Type())
fsMIRrdForce.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdForce.setStatus(_A)
class _FsMIRTMIpStaticRouteDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIRTMIpStaticRouteDistance_Type.__name__=_B
_FsMIRTMIpStaticRouteDistance_Object=MibTableColumn
fsMIRTMIpStaticRouteDistance=_FsMIRTMIpStaticRouteDistance_Object((1,3,6,1,4,1,29601,2,31,2,1,9),_FsMIRTMIpStaticRouteDistance_Type())
fsMIRTMIpStaticRouteDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRTMIpStaticRouteDistance.setStatus(_A)
_FsMIRrdControlTable_Object=MibTable
fsMIRrdControlTable=_FsMIRrdControlTable_Object((1,3,6,1,4,1,29601,2,31,3))
if mibBuilder.loadTexts:fsMIRrdControlTable.setStatus(_A)
_FsMIRrdControlEntry_Object=MibTableRow
fsMIRrdControlEntry=_FsMIRrdControlEntry_Object((1,3,6,1,4,1,29601,2,31,3,1))
fsMIRrdControlEntry.setIndexNames((0,_D,_J),(0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:fsMIRrdControlEntry.setStatus(_A)
_FsMIRrdControlDestIpAddress_Type=IpAddress
_FsMIRrdControlDestIpAddress_Object=MibTableColumn
fsMIRrdControlDestIpAddress=_FsMIRrdControlDestIpAddress_Object((1,3,6,1,4,1,29601,2,31,3,1,1),_FsMIRrdControlDestIpAddress_Type())
fsMIRrdControlDestIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrdControlDestIpAddress.setStatus(_A)
_FsMIRrdControlNetMask_Type=IpAddress
_FsMIRrdControlNetMask_Object=MibTableColumn
fsMIRrdControlNetMask=_FsMIRrdControlNetMask_Object((1,3,6,1,4,1,29601,2,31,3,1,2),_FsMIRrdControlNetMask_Type())
fsMIRrdControlNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrdControlNetMask.setStatus(_A)
class _FsMIRrdControlSourceProto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('any',0),(_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10),(_U,11),(_V,12),(_W,13),(_X,14),(_Y,15),(_Z,16)))
_FsMIRrdControlSourceProto_Type.__name__=_B
_FsMIRrdControlSourceProto_Object=MibTableColumn
fsMIRrdControlSourceProto=_FsMIRrdControlSourceProto_Object((1,3,6,1,4,1,29601,2,31,3,1,3),_FsMIRrdControlSourceProto_Type())
fsMIRrdControlSourceProto.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdControlSourceProto.setStatus(_A)
class _FsMIRrdControlDestProto_Type(Integer32):defaultValue=0
_FsMIRrdControlDestProto_Type.__name__=_B
_FsMIRrdControlDestProto_Object=MibTableColumn
fsMIRrdControlDestProto=_FsMIRrdControlDestProto_Object((1,3,6,1,4,1,29601,2,31,3,1,4),_FsMIRrdControlDestProto_Type())
fsMIRrdControlDestProto.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdControlDestProto.setStatus(_A)
class _FsMIRrdControlRouteExportFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsMIRrdControlRouteExportFlag_Type.__name__=_B
_FsMIRrdControlRouteExportFlag_Object=MibTableColumn
fsMIRrdControlRouteExportFlag=_FsMIRrdControlRouteExportFlag_Object((1,3,6,1,4,1,29601,2,31,3,1,5),_FsMIRrdControlRouteExportFlag_Type())
fsMIRrdControlRouteExportFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdControlRouteExportFlag.setStatus(_A)
_FsMIRrdControlRowStatus_Type=RowStatus
_FsMIRrdControlRowStatus_Object=MibTableColumn
fsMIRrdControlRowStatus=_FsMIRrdControlRowStatus_Object((1,3,6,1,4,1,29601,2,31,3,1,6),_FsMIRrdControlRowStatus_Type())
fsMIRrdControlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdControlRowStatus.setStatus(_A)
_FsMIRrdRoutingProtoTable_Object=MibTable
fsMIRrdRoutingProtoTable=_FsMIRrdRoutingProtoTable_Object((1,3,6,1,4,1,29601,2,31,4))
if mibBuilder.loadTexts:fsMIRrdRoutingProtoTable.setStatus(_A)
_FsMIRrdRoutingProtoEntry_Object=MibTableRow
fsMIRrdRoutingProtoEntry=_FsMIRrdRoutingProtoEntry_Object((1,3,6,1,4,1,29601,2,31,4,1))
fsMIRrdRoutingProtoEntry.setIndexNames((0,_D,_J),(0,_D,_f))
if mibBuilder.loadTexts:fsMIRrdRoutingProtoEntry.setStatus(_A)
class _FsMIRrdRoutingProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10),(_U,11),(_V,12),(_W,13),(_X,14),(_Y,15),(_Z,16)))
_FsMIRrdRoutingProtoId_Type.__name__=_B
_FsMIRrdRoutingProtoId_Object=MibTableColumn
fsMIRrdRoutingProtoId=_FsMIRrdRoutingProtoId_Object((1,3,6,1,4,1,29601,2,31,4,1,1),_FsMIRrdRoutingProtoId_Type())
fsMIRrdRoutingProtoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrdRoutingProtoId.setStatus(_A)
_FsMIRrdRoutingRegnId_Type=Integer32
_FsMIRrdRoutingRegnId_Object=MibTableColumn
fsMIRrdRoutingRegnId=_FsMIRrdRoutingRegnId_Object((1,3,6,1,4,1,29601,2,31,4,1,2),_FsMIRrdRoutingRegnId_Type())
fsMIRrdRoutingRegnId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRrdRoutingRegnId.setStatus(_A)
_FsMIRrdRoutingProtoTaskIdent_Type=OctetString
_FsMIRrdRoutingProtoTaskIdent_Object=MibTableColumn
fsMIRrdRoutingProtoTaskIdent=_FsMIRrdRoutingProtoTaskIdent_Object((1,3,6,1,4,1,29601,2,31,4,1,3),_FsMIRrdRoutingProtoTaskIdent_Type())
fsMIRrdRoutingProtoTaskIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRrdRoutingProtoTaskIdent.setStatus(_A)
_FsMIRrdRoutingProtoQueueIdent_Type=OctetString
_FsMIRrdRoutingProtoQueueIdent_Object=MibTableColumn
fsMIRrdRoutingProtoQueueIdent=_FsMIRrdRoutingProtoQueueIdent_Object((1,3,6,1,4,1,29601,2,31,4,1,4),_FsMIRrdRoutingProtoQueueIdent_Type())
fsMIRrdRoutingProtoQueueIdent.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRrdRoutingProtoQueueIdent.setStatus(_A)
class _FsMIRrdAllowOspfAreaRoutes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrdAllowOspfAreaRoutes_Type.__name__=_B
_FsMIRrdAllowOspfAreaRoutes_Object=MibTableColumn
fsMIRrdAllowOspfAreaRoutes=_FsMIRrdAllowOspfAreaRoutes_Object((1,3,6,1,4,1,29601,2,31,4,1,5),_FsMIRrdAllowOspfAreaRoutes_Type())
fsMIRrdAllowOspfAreaRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdAllowOspfAreaRoutes.setStatus(_A)
class _FsMIRrdAllowOspfExtRoutes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrdAllowOspfExtRoutes_Type.__name__=_B
_FsMIRrdAllowOspfExtRoutes_Object=MibTableColumn
fsMIRrdAllowOspfExtRoutes=_FsMIRrdAllowOspfExtRoutes_Object((1,3,6,1,4,1,29601,2,31,4,1,6),_FsMIRrdAllowOspfExtRoutes_Type())
fsMIRrdAllowOspfExtRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRrdAllowOspfExtRoutes.setStatus(_A)
_FsMIRtmCommonRouteTable_Object=MibTable
fsMIRtmCommonRouteTable=_FsMIRtmCommonRouteTable_Object((1,3,6,1,4,1,29601,2,31,5))
if mibBuilder.loadTexts:fsMIRtmCommonRouteTable.setStatus(_A)
_FsMIRtmCommonRouteEntry_Object=MibTableRow
fsMIRtmCommonRouteEntry=_FsMIRtmCommonRouteEntry_Object((1,3,6,1,4,1,29601,2,31,5,1))
fsMIRtmCommonRouteEntry.setIndexNames((0,_D,_J),(0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:fsMIRtmCommonRouteEntry.setStatus(_A)
_FsMIRtmCommonRouteDest_Type=IpAddress
_FsMIRtmCommonRouteDest_Object=MibTableColumn
fsMIRtmCommonRouteDest=_FsMIRtmCommonRouteDest_Object((1,3,6,1,4,1,29601,2,31,5,1,1),_FsMIRtmCommonRouteDest_Type())
fsMIRtmCommonRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtmCommonRouteDest.setStatus(_A)
_FsMIRtmCommonRouteMask_Type=IpAddress
_FsMIRtmCommonRouteMask_Object=MibTableColumn
fsMIRtmCommonRouteMask=_FsMIRtmCommonRouteMask_Object((1,3,6,1,4,1,29601,2,31,5,1,2),_FsMIRtmCommonRouteMask_Type())
fsMIRtmCommonRouteMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtmCommonRouteMask.setStatus(_A)
class _FsMIRtmCommonRouteTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIRtmCommonRouteTos_Type.__name__=_B
_FsMIRtmCommonRouteTos_Object=MibTableColumn
fsMIRtmCommonRouteTos=_FsMIRtmCommonRouteTos_Object((1,3,6,1,4,1,29601,2,31,5,1,3),_FsMIRtmCommonRouteTos_Type())
fsMIRtmCommonRouteTos.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtmCommonRouteTos.setStatus(_A)
_FsMIRtmCommonRouteNextHop_Type=IpAddress
_FsMIRtmCommonRouteNextHop_Object=MibTableColumn
fsMIRtmCommonRouteNextHop=_FsMIRtmCommonRouteNextHop_Object((1,3,6,1,4,1,29601,2,31,5,1,4),_FsMIRtmCommonRouteNextHop_Type())
fsMIRtmCommonRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtmCommonRouteNextHop.setStatus(_A)
class _FsMIRtmCommonRouteIfIndex_Type(Integer32):defaultValue=0
_FsMIRtmCommonRouteIfIndex_Type.__name__=_B
_FsMIRtmCommonRouteIfIndex_Object=MibTableColumn
fsMIRtmCommonRouteIfIndex=_FsMIRtmCommonRouteIfIndex_Object((1,3,6,1,4,1,29601,2,31,5,1,5),_FsMIRtmCommonRouteIfIndex_Type())
fsMIRtmCommonRouteIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteIfIndex.setStatus(_A)
class _FsMIRtmCommonRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('reject',2),(_L,3),('remote',4)))
_FsMIRtmCommonRouteType_Type.__name__=_B
_FsMIRtmCommonRouteType_Object=MibTableColumn
fsMIRtmCommonRouteType=_FsMIRtmCommonRouteType_Object((1,3,6,1,4,1,29601,2,31,5,1,6),_FsMIRtmCommonRouteType_Type())
fsMIRtmCommonRouteType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteType.setStatus(_A)
class _FsMIRtmCommonRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6),(_Q,7),(_R,8),(_S,9),(_T,10),(_U,11),(_V,12),(_W,13),(_X,14),(_Y,15),(_Z,16)))
_FsMIRtmCommonRouteProto_Type.__name__=_B
_FsMIRtmCommonRouteProto_Object=MibTableColumn
fsMIRtmCommonRouteProto=_FsMIRtmCommonRouteProto_Object((1,3,6,1,4,1,29601,2,31,5,1,7),_FsMIRtmCommonRouteProto_Type())
fsMIRtmCommonRouteProto.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRtmCommonRouteProto.setStatus(_A)
class _FsMIRtmCommonRouteAge_Type(Integer32):defaultValue=0
_FsMIRtmCommonRouteAge_Type.__name__=_B
_FsMIRtmCommonRouteAge_Object=MibTableColumn
fsMIRtmCommonRouteAge=_FsMIRtmCommonRouteAge_Object((1,3,6,1,4,1,29601,2,31,5,1,8),_FsMIRtmCommonRouteAge_Type())
fsMIRtmCommonRouteAge.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRtmCommonRouteAge.setStatus(_A)
_FsMIRtmCommonRouteInfo_Type=ObjectIdentifier
_FsMIRtmCommonRouteInfo_Object=MibTableColumn
fsMIRtmCommonRouteInfo=_FsMIRtmCommonRouteInfo_Object((1,3,6,1,4,1,29601,2,31,5,1,9),_FsMIRtmCommonRouteInfo_Type())
fsMIRtmCommonRouteInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteInfo.setStatus(_A)
class _FsMIRtmCommonRouteNextHopAS_Type(Integer32):defaultValue=0
_FsMIRtmCommonRouteNextHopAS_Type.__name__=_B
_FsMIRtmCommonRouteNextHopAS_Object=MibTableColumn
fsMIRtmCommonRouteNextHopAS=_FsMIRtmCommonRouteNextHopAS_Object((1,3,6,1,4,1,29601,2,31,5,1,10),_FsMIRtmCommonRouteNextHopAS_Type())
fsMIRtmCommonRouteNextHopAS.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteNextHopAS.setStatus(_A)
class _FsMIRtmCommonRouteMetric1_Type(Integer32):defaultValue=-1
_FsMIRtmCommonRouteMetric1_Type.__name__=_B
_FsMIRtmCommonRouteMetric1_Object=MibTableColumn
fsMIRtmCommonRouteMetric1=_FsMIRtmCommonRouteMetric1_Object((1,3,6,1,4,1,29601,2,31,5,1,11),_FsMIRtmCommonRouteMetric1_Type())
fsMIRtmCommonRouteMetric1.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteMetric1.setStatus(_A)
_FsMIRtmCommonRoutePrivateStatus_Type=TruthValue
_FsMIRtmCommonRoutePrivateStatus_Object=MibTableColumn
fsMIRtmCommonRoutePrivateStatus=_FsMIRtmCommonRoutePrivateStatus_Object((1,3,6,1,4,1,29601,2,31,5,1,12),_FsMIRtmCommonRoutePrivateStatus_Type())
fsMIRtmCommonRoutePrivateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRoutePrivateStatus.setStatus(_A)
_FsMIRtmCommonRouteStatus_Type=RowStatus
_FsMIRtmCommonRouteStatus_Object=MibTableColumn
fsMIRtmCommonRouteStatus=_FsMIRtmCommonRouteStatus_Object((1,3,6,1,4,1,29601,2,31,5,1,13),_FsMIRtmCommonRouteStatus_Type())
fsMIRtmCommonRouteStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtmCommonRouteStatus.setStatus(_A)
class _FsMIRtmCommonRoutePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIRtmCommonRoutePreference_Type.__name__=_B
_FsMIRtmCommonRoutePreference_Object=MibTableColumn
fsMIRtmCommonRoutePreference=_FsMIRtmCommonRoutePreference_Object((1,3,6,1,4,1,29601,2,31,5,1,14),_FsMIRtmCommonRoutePreference_Type())
fsMIRtmCommonRoutePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmCommonRoutePreference.setStatus(_A)
_FsMIRtmRedTest_ObjectIdentity=ObjectIdentity
fsMIRtmRedTest=_FsMIRtmRedTest_ObjectIdentity((1,3,6,1,4,1,29601,2,31,6))
_FsMIRtmRedEntryTime_Type=Integer32
_FsMIRtmRedEntryTime_Object=MibScalar
fsMIRtmRedEntryTime=_FsMIRtmRedEntryTime_Object((1,3,6,1,4,1,29601,2,31,6,1),_FsMIRtmRedEntryTime_Type())
fsMIRtmRedEntryTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRtmRedEntryTime.setStatus(_A)
_FsMIRtmRedExitTime_Type=Integer32
_FsMIRtmRedExitTime_Object=MibScalar
fsMIRtmRedExitTime=_FsMIRtmRedExitTime_Object((1,3,6,1,4,1,29601,2,31,6,2),_FsMIRtmRedExitTime_Type())
fsMIRtmRedExitTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIRtmRedExitTime.setStatus(_A)
_FsMIRtmMaximumBgpRoutes_Type=Unsigned32
_FsMIRtmMaximumBgpRoutes_Object=MibScalar
fsMIRtmMaximumBgpRoutes=_FsMIRtmMaximumBgpRoutes_Object((1,3,6,1,4,1,29601,2,31,7),_FsMIRtmMaximumBgpRoutes_Type())
fsMIRtmMaximumBgpRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmMaximumBgpRoutes.setStatus(_A)
_FsMIRtmMaximumOspfRoutes_Type=Unsigned32
_FsMIRtmMaximumOspfRoutes_Object=MibScalar
fsMIRtmMaximumOspfRoutes=_FsMIRtmMaximumOspfRoutes_Object((1,3,6,1,4,1,29601,2,31,8),_FsMIRtmMaximumOspfRoutes_Type())
fsMIRtmMaximumOspfRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmMaximumOspfRoutes.setStatus(_A)
_FsMIRtmMaximumRipRoutes_Type=Unsigned32
_FsMIRtmMaximumRipRoutes_Object=MibScalar
fsMIRtmMaximumRipRoutes=_FsMIRtmMaximumRipRoutes_Object((1,3,6,1,4,1,29601,2,31,9),_FsMIRtmMaximumRipRoutes_Type())
fsMIRtmMaximumRipRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmMaximumRipRoutes.setStatus(_A)
_FsMIRtmMaximumStaticRoutes_Type=Unsigned32
_FsMIRtmMaximumStaticRoutes_Object=MibScalar
fsMIRtmMaximumStaticRoutes=_FsMIRtmMaximumStaticRoutes_Object((1,3,6,1,4,1,29601,2,31,10),_FsMIRtmMaximumStaticRoutes_Type())
fsMIRtmMaximumStaticRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmMaximumStaticRoutes.setStatus(_A)
_FsMIRtmMaximumISISRoutes_Type=Unsigned32
_FsMIRtmMaximumISISRoutes_Object=MibScalar
fsMIRtmMaximumISISRoutes=_FsMIRtmMaximumISISRoutes_Object((1,3,6,1,4,1,29601,2,31,11),_FsMIRtmMaximumISISRoutes_Type())
fsMIRtmMaximumISISRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIRtmMaximumISISRoutes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsMIRtm':fsMIRtm,'fsMIRtmGeneralGroup':fsMIRtmGeneralGroup,'fsMIRtmThrottleLimit':fsMIRtmThrottleLimit,'fsMIEcmpAcrossProtocolAdminStatus':fsMIEcmpAcrossProtocolAdminStatus,'fsMIRtmRouteLeakStatus':fsMIRtmRouteLeakStatus,'fsMIRtmTable':fsMIRtmTable,'fsMIRtmEntry':fsMIRtmEntry,_J:fsMIRtmContextId,'fsMIRrdRouterId':fsMIRrdRouterId,'fsMIRrdFilterByOspfTag':fsMIRrdFilterByOspfTag,'fsMIRrdFilterOspfTag':fsMIRrdFilterOspfTag,'fsMIRrdFilterOspfTagMask':fsMIRrdFilterOspfTagMask,'fsMIRrdRouterASNumber':fsMIRrdRouterASNumber,'fsMIRrdAdminStatus':fsMIRrdAdminStatus,'fsMIRrdForce':fsMIRrdForce,'fsMIRTMIpStaticRouteDistance':fsMIRTMIpStaticRouteDistance,'fsMIRrdControlTable':fsMIRrdControlTable,'fsMIRrdControlEntry':fsMIRrdControlEntry,_d:fsMIRrdControlDestIpAddress,_e:fsMIRrdControlNetMask,'fsMIRrdControlSourceProto':fsMIRrdControlSourceProto,'fsMIRrdControlDestProto':fsMIRrdControlDestProto,'fsMIRrdControlRouteExportFlag':fsMIRrdControlRouteExportFlag,'fsMIRrdControlRowStatus':fsMIRrdControlRowStatus,'fsMIRrdRoutingProtoTable':fsMIRrdRoutingProtoTable,'fsMIRrdRoutingProtoEntry':fsMIRrdRoutingProtoEntry,_f:fsMIRrdRoutingProtoId,'fsMIRrdRoutingRegnId':fsMIRrdRoutingRegnId,'fsMIRrdRoutingProtoTaskIdent':fsMIRrdRoutingProtoTaskIdent,'fsMIRrdRoutingProtoQueueIdent':fsMIRrdRoutingProtoQueueIdent,'fsMIRrdAllowOspfAreaRoutes':fsMIRrdAllowOspfAreaRoutes,'fsMIRrdAllowOspfExtRoutes':fsMIRrdAllowOspfExtRoutes,'fsMIRtmCommonRouteTable':fsMIRtmCommonRouteTable,'fsMIRtmCommonRouteEntry':fsMIRtmCommonRouteEntry,_g:fsMIRtmCommonRouteDest,_h:fsMIRtmCommonRouteMask,_i:fsMIRtmCommonRouteTos,_j:fsMIRtmCommonRouteNextHop,'fsMIRtmCommonRouteIfIndex':fsMIRtmCommonRouteIfIndex,'fsMIRtmCommonRouteType':fsMIRtmCommonRouteType,'fsMIRtmCommonRouteProto':fsMIRtmCommonRouteProto,'fsMIRtmCommonRouteAge':fsMIRtmCommonRouteAge,'fsMIRtmCommonRouteInfo':fsMIRtmCommonRouteInfo,'fsMIRtmCommonRouteNextHopAS':fsMIRtmCommonRouteNextHopAS,'fsMIRtmCommonRouteMetric1':fsMIRtmCommonRouteMetric1,'fsMIRtmCommonRoutePrivateStatus':fsMIRtmCommonRoutePrivateStatus,'fsMIRtmCommonRouteStatus':fsMIRtmCommonRouteStatus,'fsMIRtmCommonRoutePreference':fsMIRtmCommonRoutePreference,'fsMIRtmRedTest':fsMIRtmRedTest,'fsMIRtmRedEntryTime':fsMIRtmRedEntryTime,'fsMIRtmRedExitTime':fsMIRtmRedExitTime,'fsMIRtmMaximumBgpRoutes':fsMIRtmMaximumBgpRoutes,'fsMIRtmMaximumOspfRoutes':fsMIRtmMaximumOspfRoutes,'fsMIRtmMaximumRipRoutes':fsMIRtmMaximumRipRoutes,'fsMIRtmMaximumStaticRoutes':fsMIRtmMaximumStaticRoutes,'fsMIRtmMaximumISISRoutes':fsMIRtmMaximumISISRoutes})