_V='h3cIpxIfStatIndex'
_U='h3cIpxStaticServiceNetId'
_T='h3cIpxStaticServiceName'
_S='h3cIpxStaticServiceType'
_R='h3cIpxServiceIndex'
_Q='h3cIpxRouteStatPro'
_P='inactive'
_O='active'
_N='h3cIpxStaticRouteNextHop'
_M='h3cIpxStaticRouteDestNetId'
_L='direct'
_K='h3cIpxRouteIndex'
_J='h3cIpxIfIndex'
_I='EnabledStatus'
_H='not-accessible'
_G='read-write'
_F='H3C-IPX-MIB'
_E='OctetString'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cIpx=ModuleIdentity((1,3,6,1,4,1,2011,10,2,34))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cIpxConfig_ObjectIdentity=ObjectIdentity
h3cIpxConfig=_H3cIpxConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,1))
class _H3cIpxStatus_Type(EnabledStatus):defaultValue=2
_H3cIpxStatus_Type.__name__=_I
_H3cIpxStatus_Object=MibScalar
h3cIpxStatus=_H3cIpxStatus_Object((1,3,6,1,4,1,2011,10,2,34,1,1),_H3cIpxStatus_Type())
h3cIpxStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxStatus.setStatus(_A)
_H3cIpxIfConfigTable_Object=MibTable
h3cIpxIfConfigTable=_H3cIpxIfConfigTable_Object((1,3,6,1,4,1,2011,10,2,34,1,2))
if mibBuilder.loadTexts:h3cIpxIfConfigTable.setStatus(_A)
_H3cIpxIfConfigEntry_Object=MibTableRow
h3cIpxIfConfigEntry=_H3cIpxIfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1))
h3cIpxIfConfigEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:h3cIpxIfConfigEntry.setStatus(_A)
class _H3cIpxIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpxIfIndex_Type.__name__=_C
_H3cIpxIfIndex_Object=MibTableColumn
h3cIpxIfIndex=_H3cIpxIfIndex_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,1),_H3cIpxIfIndex_Type())
h3cIpxIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxIfIndex.setStatus(_A)
class _H3cIpxIfNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxIfNetId_Type.__name__=_E
_H3cIpxIfNetId_Object=MibTableColumn
h3cIpxIfNetId=_H3cIpxIfNetId_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,2),_H3cIpxIfNetId_Type())
h3cIpxIfNetId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfNetId.setStatus(_A)
class _H3cIpxIfNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_H3cIpxIfNodeId_Type.__name__=_E
_H3cIpxIfNodeId_Object=MibTableColumn
h3cIpxIfNodeId=_H3cIpxIfNodeId_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,3),_H3cIpxIfNodeId_Type())
h3cIpxIfNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfNodeId.setStatus(_A)
class _H3cIpxIfSplitHorizon_Type(EnabledStatus):defaultValue=1
_H3cIpxIfSplitHorizon_Type.__name__=_I
_H3cIpxIfSplitHorizon_Object=MibTableColumn
h3cIpxIfSplitHorizon=_H3cIpxIfSplitHorizon_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,4),_H3cIpxIfSplitHorizon_Type())
h3cIpxIfSplitHorizon.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfSplitHorizon.setStatus(_A)
class _H3cIPxIfTick_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30000))
_H3cIPxIfTick_Type.__name__=_C
_H3cIPxIfTick_Object=MibTableColumn
h3cIPxIfTick=_H3cIPxIfTick_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,5),_H3cIPxIfTick_Type())
h3cIPxIfTick.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIPxIfTick.setStatus(_A)
class _H3cIpxIfUpdateChangeOnly_Type(EnabledStatus):defaultValue=2
_H3cIpxIfUpdateChangeOnly_Type.__name__=_I
_H3cIpxIfUpdateChangeOnly_Object=MibTableColumn
h3cIpxIfUpdateChangeOnly=_H3cIpxIfUpdateChangeOnly_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,6),_H3cIpxIfUpdateChangeOnly_Type())
h3cIpxIfUpdateChangeOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfUpdateChangeOnly.setStatus(_A)
class _H3cIpxIfRipMtu_Type(Integer32):defaultValue=432;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(432,1500))
_H3cIpxIfRipMtu_Type.__name__=_C
_H3cIpxIfRipMtu_Object=MibTableColumn
h3cIpxIfRipMtu=_H3cIpxIfRipMtu_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,7),_H3cIpxIfRipMtu_Type())
h3cIpxIfRipMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfRipMtu.setStatus(_A)
class _H3cIpxIfEncapsuleType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dot2',1),('dot3',2),('ethernet-2',3),('snap',4),('unkown',5)))
_H3cIpxIfEncapsuleType_Type.__name__=_C
_H3cIpxIfEncapsuleType_Object=MibTableColumn
h3cIpxIfEncapsuleType=_H3cIpxIfEncapsuleType_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,8),_H3cIpxIfEncapsuleType_Type())
h3cIpxIfEncapsuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfEncapsuleType.setStatus(_A)
class _H3cIpxIfNetbiosPropagation_Type(EnabledStatus):defaultValue=2
_H3cIpxIfNetbiosPropagation_Type.__name__=_I
_H3cIpxIfNetbiosPropagation_Object=MibTableColumn
h3cIpxIfNetbiosPropagation=_H3cIpxIfNetbiosPropagation_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,9),_H3cIpxIfNetbiosPropagation_Type())
h3cIpxIfNetbiosPropagation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfNetbiosPropagation.setStatus(_A)
class _H3cIpxIfSapStatus_Type(EnabledStatus):defaultValue=1
_H3cIpxIfSapStatus_Type.__name__=_I
_H3cIpxIfSapStatus_Object=MibTableColumn
h3cIpxIfSapStatus=_H3cIpxIfSapStatus_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,10),_H3cIpxIfSapStatus_Type())
h3cIpxIfSapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfSapStatus.setStatus(_A)
class _H3cIpxIfSapMtu_Type(Integer32):defaultValue=480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(480,1500))
_H3cIpxIfSapMtu_Type.__name__=_C
_H3cIpxIfSapMtu_Object=MibTableColumn
h3cIpxIfSapMtu=_H3cIpxIfSapMtu_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,11),_H3cIpxIfSapMtu_Type())
h3cIpxIfSapMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfSapMtu.setStatus(_A)
class _H3cIpxIfGnsReply_Type(EnabledStatus):defaultValue=1
_H3cIpxIfGnsReply_Type.__name__=_I
_H3cIpxIfGnsReply_Object=MibTableColumn
h3cIpxIfGnsReply=_H3cIpxIfGnsReply_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,12),_H3cIpxIfGnsReply_Type())
h3cIpxIfGnsReply.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfGnsReply.setStatus(_A)
_H3cIpxIfRowStatus_Type=RowStatus
_H3cIpxIfRowStatus_Object=MibTableColumn
h3cIpxIfRowStatus=_H3cIpxIfRowStatus_Object((1,3,6,1,4,1,2011,10,2,34,1,2,1,13),_H3cIpxIfRowStatus_Type())
h3cIpxIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxIfRowStatus.setStatus(_A)
_H3cIpxRip_ObjectIdentity=ObjectIdentity
h3cIpxRip=_H3cIpxRip_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,2))
class _H3cIpxRouteMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_H3cIpxRouteMultiplier_Type.__name__=_C
_H3cIpxRouteMultiplier_Object=MibScalar
h3cIpxRouteMultiplier=_H3cIpxRouteMultiplier_Object((1,3,6,1,4,1,2011,10,2,34,2,1),_H3cIpxRouteMultiplier_Type())
h3cIpxRouteMultiplier.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxRouteMultiplier.setStatus(_A)
class _H3cIpxRouteUpdateTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60000))
_H3cIpxRouteUpdateTimer_Type.__name__=_C
_H3cIpxRouteUpdateTimer_Object=MibScalar
h3cIpxRouteUpdateTimer=_H3cIpxRouteUpdateTimer_Object((1,3,6,1,4,1,2011,10,2,34,2,2),_H3cIpxRouteUpdateTimer_Type())
h3cIpxRouteUpdateTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxRouteUpdateTimer.setStatus(_A)
class _H3cIpxRouteImpRouteStatic_Type(EnabledStatus):defaultValue=2
_H3cIpxRouteImpRouteStatic_Type.__name__=_I
_H3cIpxRouteImpRouteStatic_Object=MibScalar
h3cIpxRouteImpRouteStatic=_H3cIpxRouteImpRouteStatic_Object((1,3,6,1,4,1,2011,10,2,34,2,3),_H3cIpxRouteImpRouteStatic_Type())
h3cIpxRouteImpRouteStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxRouteImpRouteStatic.setStatus(_A)
class _H3cIpxRouteLoadBalancePaths_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cIpxRouteLoadBalancePaths_Type.__name__=_C
_H3cIpxRouteLoadBalancePaths_Object=MibScalar
h3cIpxRouteLoadBalancePaths=_H3cIpxRouteLoadBalancePaths_Object((1,3,6,1,4,1,2011,10,2,34,2,4),_H3cIpxRouteLoadBalancePaths_Type())
h3cIpxRouteLoadBalancePaths.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxRouteLoadBalancePaths.setStatus(_A)
class _H3cIpxRouteMaxResPaths_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cIpxRouteMaxResPaths_Type.__name__=_C
_H3cIpxRouteMaxResPaths_Object=MibScalar
h3cIpxRouteMaxResPaths=_H3cIpxRouteMaxResPaths_Object((1,3,6,1,4,1,2011,10,2,34,2,5),_H3cIpxRouteMaxResPaths_Type())
h3cIpxRouteMaxResPaths.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxRouteMaxResPaths.setStatus(_A)
_H3cIpxRouteTable_Object=MibTable
h3cIpxRouteTable=_H3cIpxRouteTable_Object((1,3,6,1,4,1,2011,10,2,34,2,6))
if mibBuilder.loadTexts:h3cIpxRouteTable.setStatus(_A)
_H3cIpxRouteEntry_Object=MibTableRow
h3cIpxRouteEntry=_H3cIpxRouteEntry_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1))
h3cIpxRouteEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:h3cIpxRouteEntry.setStatus(_A)
_H3cIpxRouteIndex_Type=Integer32
_H3cIpxRouteIndex_Object=MibTableColumn
h3cIpxRouteIndex=_H3cIpxRouteIndex_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,1),_H3cIpxRouteIndex_Type())
h3cIpxRouteIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxRouteIndex.setStatus(_A)
class _H3cIpxRouteDestNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxRouteDestNetId_Type.__name__=_E
_H3cIpxRouteDestNetId_Object=MibTableColumn
h3cIpxRouteDestNetId=_H3cIpxRouteDestNetId_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,2),_H3cIpxRouteDestNetId_Type())
h3cIpxRouteDestNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteDestNetId.setStatus(_A)
class _H3cIpxRouteNextHop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_H3cIpxRouteNextHop_Type.__name__=_E
_H3cIpxRouteNextHop_Object=MibTableColumn
h3cIpxRouteNextHop=_H3cIpxRouteNextHop_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,3),_H3cIpxRouteNextHop_Type())
h3cIpxRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteNextHop.setStatus(_A)
class _H3cIpxRoutePro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('rip',2)))
_H3cIpxRoutePro_Type.__name__=_C
_H3cIpxRoutePro_Object=MibTableColumn
h3cIpxRoutePro=_H3cIpxRoutePro_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,4),_H3cIpxRoutePro_Type())
h3cIpxRoutePro.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRoutePro.setStatus(_A)
_H3cIpxRoutePre_Type=Integer32
_H3cIpxRoutePre_Object=MibTableColumn
h3cIpxRoutePre=_H3cIpxRoutePre_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,5),_H3cIpxRoutePre_Type())
h3cIpxRoutePre.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRoutePre.setStatus(_A)
class _H3cIpxRouteTicks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cIpxRouteTicks_Type.__name__=_C
_H3cIpxRouteTicks_Object=MibTableColumn
h3cIpxRouteTicks=_H3cIpxRouteTicks_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,6),_H3cIpxRouteTicks_Type())
h3cIpxRouteTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteTicks.setStatus(_A)
class _H3cIpxRouteHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cIpxRouteHops_Type.__name__=_C
_H3cIpxRouteHops_Object=MibTableColumn
h3cIpxRouteHops=_H3cIpxRouteHops_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,7),_H3cIpxRouteHops_Type())
h3cIpxRouteHops.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteHops.setStatus(_A)
class _H3cIpxRouteTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_H3cIpxRouteTime_Type.__name__=_C
_H3cIpxRouteTime_Object=MibTableColumn
h3cIpxRouteTime=_H3cIpxRouteTime_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,8),_H3cIpxRouteTime_Type())
h3cIpxRouteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteTime.setStatus(_A)
class _H3cIpxRouteOutInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_H3cIpxRouteOutInterface_Type.__name__=_E
_H3cIpxRouteOutInterface_Object=MibTableColumn
h3cIpxRouteOutInterface=_H3cIpxRouteOutInterface_Object((1,3,6,1,4,1,2011,10,2,34,2,6,1,9),_H3cIpxRouteOutInterface_Type())
h3cIpxRouteOutInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteOutInterface.setStatus(_A)
_H3cIpxStaticRouteTable_Object=MibTable
h3cIpxStaticRouteTable=_H3cIpxStaticRouteTable_Object((1,3,6,1,4,1,2011,10,2,34,2,7))
if mibBuilder.loadTexts:h3cIpxStaticRouteTable.setStatus(_A)
_H3cIpxStaticRouteEntry_Object=MibTableRow
h3cIpxStaticRouteEntry=_H3cIpxStaticRouteEntry_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1))
h3cIpxStaticRouteEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:h3cIpxStaticRouteEntry.setStatus(_A)
class _H3cIpxStaticRouteDestNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxStaticRouteDestNetId_Type.__name__=_E
_H3cIpxStaticRouteDestNetId_Object=MibTableColumn
h3cIpxStaticRouteDestNetId=_H3cIpxStaticRouteDestNetId_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,1),_H3cIpxStaticRouteDestNetId_Type())
h3cIpxStaticRouteDestNetId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxStaticRouteDestNetId.setStatus(_A)
class _H3cIpxStaticRouteNextHop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_H3cIpxStaticRouteNextHop_Type.__name__=_E
_H3cIpxStaticRouteNextHop_Object=MibTableColumn
h3cIpxStaticRouteNextHop=_H3cIpxStaticRouteNextHop_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,2),_H3cIpxStaticRouteNextHop_Type())
h3cIpxStaticRouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxStaticRouteNextHop.setStatus(_A)
class _H3cIpxStaticRoutePre_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cIpxStaticRoutePre_Type.__name__=_C
_H3cIpxStaticRoutePre_Object=MibTableColumn
h3cIpxStaticRoutePre=_H3cIpxStaticRoutePre_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,3),_H3cIpxStaticRoutePre_Type())
h3cIpxStaticRoutePre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRoutePre.setStatus(_A)
class _H3cIpxStaticRouteOutIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_H3cIpxStaticRouteOutIf_Type.__name__=_E
_H3cIpxStaticRouteOutIf_Object=MibTableColumn
h3cIpxStaticRouteOutIf=_H3cIpxStaticRouteOutIf_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,4),_H3cIpxStaticRouteOutIf_Type())
h3cIpxStaticRouteOutIf.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRouteOutIf.setStatus(_A)
class _H3cIpxStaticRouteTicks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cIpxStaticRouteTicks_Type.__name__=_C
_H3cIpxStaticRouteTicks_Object=MibTableColumn
h3cIpxStaticRouteTicks=_H3cIpxStaticRouteTicks_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,5),_H3cIpxStaticRouteTicks_Type())
h3cIpxStaticRouteTicks.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRouteTicks.setStatus(_A)
class _H3cIpxStaticRouteHops_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_H3cIpxStaticRouteHops_Type.__name__=_C
_H3cIpxStaticRouteHops_Object=MibTableColumn
h3cIpxStaticRouteHops=_H3cIpxStaticRouteHops_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,6),_H3cIpxStaticRouteHops_Type())
h3cIpxStaticRouteHops.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRouteHops.setStatus(_A)
class _H3cIpxStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_H3cIpxStaticRouteStatus_Type.__name__=_C
_H3cIpxStaticRouteStatus_Object=MibTableColumn
h3cIpxStaticRouteStatus=_H3cIpxStaticRouteStatus_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,7),_H3cIpxStaticRouteStatus_Type())
h3cIpxStaticRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRouteStatus.setStatus(_A)
_H3cIpxStaticRouteRowStatus_Type=RowStatus
_H3cIpxStaticRouteRowStatus_Object=MibTableColumn
h3cIpxStaticRouteRowStatus=_H3cIpxStaticRouteRowStatus_Object((1,3,6,1,4,1,2011,10,2,34,2,7,1,8),_H3cIpxStaticRouteRowStatus_Type())
h3cIpxStaticRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticRouteRowStatus.setStatus(_A)
_H3cIpxRouteStatTable_Object=MibTable
h3cIpxRouteStatTable=_H3cIpxRouteStatTable_Object((1,3,6,1,4,1,2011,10,2,34,2,8))
if mibBuilder.loadTexts:h3cIpxRouteStatTable.setStatus(_A)
_H3cIpxRouteStatEntry_Object=MibTableRow
h3cIpxRouteStatEntry=_H3cIpxRouteStatEntry_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1))
h3cIpxRouteStatEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:h3cIpxRouteStatEntry.setStatus(_A)
class _H3cIpxRouteStatPro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('static',2),('rip',3),('default',4),('total',5)))
_H3cIpxRouteStatPro_Type.__name__=_C
_H3cIpxRouteStatPro_Object=MibTableColumn
h3cIpxRouteStatPro=_H3cIpxRouteStatPro_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,1),_H3cIpxRouteStatPro_Type())
h3cIpxRouteStatPro.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxRouteStatPro.setStatus(_A)
_H3cIpxRouteStatRoutes_Type=Counter32
_H3cIpxRouteStatRoutes_Object=MibTableColumn
h3cIpxRouteStatRoutes=_H3cIpxRouteStatRoutes_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,2),_H3cIpxRouteStatRoutes_Type())
h3cIpxRouteStatRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteStatRoutes.setStatus(_A)
_H3cIpxRouteStatActives_Type=Counter32
_H3cIpxRouteStatActives_Object=MibTableColumn
h3cIpxRouteStatActives=_H3cIpxRouteStatActives_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,3),_H3cIpxRouteStatActives_Type())
h3cIpxRouteStatActives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteStatActives.setStatus(_A)
_H3cIpxRouteStatAddeds_Type=Counter32
_H3cIpxRouteStatAddeds_Object=MibTableColumn
h3cIpxRouteStatAddeds=_H3cIpxRouteStatAddeds_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,4),_H3cIpxRouteStatAddeds_Type())
h3cIpxRouteStatAddeds.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteStatAddeds.setStatus(_A)
_H3cIpxRouteStatDeleteds_Type=Counter32
_H3cIpxRouteStatDeleteds_Object=MibTableColumn
h3cIpxRouteStatDeleteds=_H3cIpxRouteStatDeleteds_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,5),_H3cIpxRouteStatDeleteds_Type())
h3cIpxRouteStatDeleteds.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteStatDeleteds.setStatus(_A)
_H3cIpxRouteStatFreeds_Type=Counter32
_H3cIpxRouteStatFreeds_Object=MibTableColumn
h3cIpxRouteStatFreeds=_H3cIpxRouteStatFreeds_Object((1,3,6,1,4,1,2011,10,2,34,2,8,1,6),_H3cIpxRouteStatFreeds_Type())
h3cIpxRouteStatFreeds.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxRouteStatFreeds.setStatus(_A)
_H3cIpxSap_ObjectIdentity=ObjectIdentity
h3cIpxSap=_H3cIpxSap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,3))
class _H3cIpxSapMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_H3cIpxSapMultiplier_Type.__name__=_C
_H3cIpxSapMultiplier_Object=MibScalar
h3cIpxSapMultiplier=_H3cIpxSapMultiplier_Object((1,3,6,1,4,1,2011,10,2,34,3,1),_H3cIpxSapMultiplier_Type())
h3cIpxSapMultiplier.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxSapMultiplier.setStatus(_A)
class _H3cIpxSapUpdateTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60000))
_H3cIpxSapUpdateTimer_Type.__name__=_C
_H3cIpxSapUpdateTimer_Object=MibScalar
h3cIpxSapUpdateTimer=_H3cIpxSapUpdateTimer_Object((1,3,6,1,4,1,2011,10,2,34,3,2),_H3cIpxSapUpdateTimer_Type())
h3cIpxSapUpdateTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxSapUpdateTimer.setStatus(_A)
class _H3cIpxSapGnsLoadBalance_Type(EnabledStatus):defaultValue=1
_H3cIpxSapGnsLoadBalance_Type.__name__=_I
_H3cIpxSapGnsLoadBalance_Object=MibScalar
h3cIpxSapGnsLoadBalance=_H3cIpxSapGnsLoadBalance_Object((1,3,6,1,4,1,2011,10,2,34,3,3),_H3cIpxSapGnsLoadBalance_Type())
h3cIpxSapGnsLoadBalance.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxSapGnsLoadBalance.setStatus(_A)
class _H3cIpxSapMaxResServers_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_H3cIpxSapMaxResServers_Type.__name__=_C
_H3cIpxSapMaxResServers_Object=MibScalar
h3cIpxSapMaxResServers=_H3cIpxSapMaxResServers_Object((1,3,6,1,4,1,2011,10,2,34,3,4),_H3cIpxSapMaxResServers_Type())
h3cIpxSapMaxResServers.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpxSapMaxResServers.setStatus(_A)
_H3cIpxServiceTable_Object=MibTable
h3cIpxServiceTable=_H3cIpxServiceTable_Object((1,3,6,1,4,1,2011,10,2,34,3,5))
if mibBuilder.loadTexts:h3cIpxServiceTable.setStatus(_A)
_H3cIpxServiceEntry_Object=MibTableRow
h3cIpxServiceEntry=_H3cIpxServiceEntry_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1))
h3cIpxServiceEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:h3cIpxServiceEntry.setStatus(_A)
_H3cIpxServiceIndex_Type=Integer32
_H3cIpxServiceIndex_Object=MibTableColumn
h3cIpxServiceIndex=_H3cIpxServiceIndex_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,1),_H3cIpxServiceIndex_Type())
h3cIpxServiceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxServiceIndex.setStatus(_A)
class _H3cIpxServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,47))
_H3cIpxServiceName_Type.__name__=_E
_H3cIpxServiceName_Object=MibTableColumn
h3cIpxServiceName=_H3cIpxServiceName_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,2),_H3cIpxServiceName_Type())
h3cIpxServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceName.setStatus(_A)
class _H3cIpxServiceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_H3cIpxServiceType_Type.__name__=_E
_H3cIpxServiceType_Object=MibTableColumn
h3cIpxServiceType=_H3cIpxServiceType_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,3),_H3cIpxServiceType_Type())
h3cIpxServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceType.setStatus(_A)
class _H3cIpxServiceNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxServiceNetId_Type.__name__=_E
_H3cIpxServiceNetId_Object=MibTableColumn
h3cIpxServiceNetId=_H3cIpxServiceNetId_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,4),_H3cIpxServiceNetId_Type())
h3cIpxServiceNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceNetId.setStatus(_A)
class _H3cIpxServiceNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_H3cIpxServiceNodeId_Type.__name__=_E
_H3cIpxServiceNodeId_Object=MibTableColumn
h3cIpxServiceNodeId=_H3cIpxServiceNodeId_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,5),_H3cIpxServiceNodeId_Type())
h3cIpxServiceNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceNodeId.setStatus(_A)
class _H3cIpxServiceSocketNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_H3cIpxServiceSocketNo_Type.__name__=_E
_H3cIpxServiceSocketNo_Object=MibTableColumn
h3cIpxServiceSocketNo=_H3cIpxServiceSocketNo_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,6),_H3cIpxServiceSocketNo_Type())
h3cIpxServiceSocketNo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceSocketNo.setStatus(_A)
_H3cIpxServicePreference_Type=Integer32
_H3cIpxServicePreference_Object=MibTableColumn
h3cIpxServicePreference=_H3cIpxServicePreference_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,7),_H3cIpxServicePreference_Type())
h3cIpxServicePreference.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServicePreference.setStatus(_A)
class _H3cIpxServiceHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cIpxServiceHops_Type.__name__=_C
_H3cIpxServiceHops_Object=MibTableColumn
h3cIpxServiceHops=_H3cIpxServiceHops_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,8),_H3cIpxServiceHops_Type())
h3cIpxServiceHops.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceHops.setStatus(_A)
class _H3cIpxServiceRecvIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_H3cIpxServiceRecvIf_Type.__name__=_E
_H3cIpxServiceRecvIf_Object=MibTableColumn
h3cIpxServiceRecvIf=_H3cIpxServiceRecvIf_Object((1,3,6,1,4,1,2011,10,2,34,3,5,1,9),_H3cIpxServiceRecvIf_Type())
h3cIpxServiceRecvIf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxServiceRecvIf.setStatus(_A)
_H3cIpxStaticServiceTable_Object=MibTable
h3cIpxStaticServiceTable=_H3cIpxStaticServiceTable_Object((1,3,6,1,4,1,2011,10,2,34,3,6))
if mibBuilder.loadTexts:h3cIpxStaticServiceTable.setStatus(_A)
_H3cIpxStaticServiceEntry_Object=MibTableRow
h3cIpxStaticServiceEntry=_H3cIpxStaticServiceEntry_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1))
h3cIpxStaticServiceEntry.setIndexNames((0,_F,_S),(0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:h3cIpxStaticServiceEntry.setStatus(_A)
class _H3cIpxStaticServiceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_H3cIpxStaticServiceType_Type.__name__=_E
_H3cIpxStaticServiceType_Object=MibTableColumn
h3cIpxStaticServiceType=_H3cIpxStaticServiceType_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,1),_H3cIpxStaticServiceType_Type())
h3cIpxStaticServiceType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxStaticServiceType.setStatus(_A)
class _H3cIpxStaticServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,47))
_H3cIpxStaticServiceName_Type.__name__=_E
_H3cIpxStaticServiceName_Object=MibTableColumn
h3cIpxStaticServiceName=_H3cIpxStaticServiceName_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,2),_H3cIpxStaticServiceName_Type())
h3cIpxStaticServiceName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxStaticServiceName.setStatus(_A)
class _H3cIpxStaticServiceNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxStaticServiceNetId_Type.__name__=_E
_H3cIpxStaticServiceNetId_Object=MibTableColumn
h3cIpxStaticServiceNetId=_H3cIpxStaticServiceNetId_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,3),_H3cIpxStaticServiceNetId_Type())
h3cIpxStaticServiceNetId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxStaticServiceNetId.setStatus(_A)
class _H3cIpxStaticServiceNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_H3cIpxStaticServiceNodeId_Type.__name__=_E
_H3cIpxStaticServiceNodeId_Object=MibTableColumn
h3cIpxStaticServiceNodeId=_H3cIpxStaticServiceNodeId_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,4),_H3cIpxStaticServiceNodeId_Type())
h3cIpxStaticServiceNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticServiceNodeId.setStatus(_A)
class _H3cIpxStatciServiceSocketNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_H3cIpxStatciServiceSocketNo_Type.__name__=_E
_H3cIpxStatciServiceSocketNo_Object=MibTableColumn
h3cIpxStatciServiceSocketNo=_H3cIpxStatciServiceSocketNo_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,5),_H3cIpxStatciServiceSocketNo_Type())
h3cIpxStatciServiceSocketNo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStatciServiceSocketNo.setStatus(_A)
class _H3cIpxStaticServicePreference_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cIpxStaticServicePreference_Type.__name__=_C
_H3cIpxStaticServicePreference_Object=MibTableColumn
h3cIpxStaticServicePreference=_H3cIpxStaticServicePreference_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,6),_H3cIpxStaticServicePreference_Type())
h3cIpxStaticServicePreference.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticServicePreference.setStatus(_A)
class _H3cIpxStaticServiceHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_H3cIpxStaticServiceHops_Type.__name__=_C
_H3cIpxStaticServiceHops_Object=MibTableColumn
h3cIpxStaticServiceHops=_H3cIpxStaticServiceHops_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,7),_H3cIpxStaticServiceHops_Type())
h3cIpxStaticServiceHops.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticServiceHops.setStatus(_A)
class _H3cIpxStaticServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_H3cIpxStaticServiceStatus_Type.__name__=_C
_H3cIpxStaticServiceStatus_Object=MibTableColumn
h3cIpxStaticServiceStatus=_H3cIpxStaticServiceStatus_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,8),_H3cIpxStaticServiceStatus_Type())
h3cIpxStaticServiceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticServiceStatus.setStatus(_A)
_H3cIpxStaticServiceRowStatus_Type=RowStatus
_H3cIpxStaticServiceRowStatus_Object=MibTableColumn
h3cIpxStaticServiceRowStatus=_H3cIpxStaticServiceRowStatus_Object((1,3,6,1,4,1,2011,10,2,34,3,6,1,9),_H3cIpxStaticServiceRowStatus_Type())
h3cIpxStaticServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpxStaticServiceRowStatus.setStatus(_A)
_H3cIpxStat_ObjectIdentity=ObjectIdentity
h3cIpxStat=_H3cIpxStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,4))
_H3cIpxStatGlobal_ObjectIdentity=ObjectIdentity
h3cIpxStatGlobal=_H3cIpxStatGlobal_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,4,1))
_H3cIpxStatTotalReceives_Type=Counter32
_H3cIpxStatTotalReceives_Object=MibScalar
h3cIpxStatTotalReceives=_H3cIpxStatTotalReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,1),_H3cIpxStatTotalReceives_Type())
h3cIpxStatTotalReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatTotalReceives.setStatus(_A)
_H3cIpxStatPitchs_Type=Counter32
_H3cIpxStatPitchs_Object=MibScalar
h3cIpxStatPitchs=_H3cIpxStatPitchs_Object((1,3,6,1,4,1,2011,10,2,34,4,1,2),_H3cIpxStatPitchs_Type())
h3cIpxStatPitchs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatPitchs.setStatus(_A)
_H3cIpxStatLenErrors_Type=Counter32
_H3cIpxStatLenErrors_Object=MibScalar
h3cIpxStatLenErrors=_H3cIpxStatLenErrors_Object((1,3,6,1,4,1,2011,10,2,34,4,1,3),_H3cIpxStatLenErrors_Type())
h3cIpxStatLenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatLenErrors.setStatus(_A)
_H3cIpxStatFormatErrors_Type=Counter32
_H3cIpxStatFormatErrors_Object=MibScalar
h3cIpxStatFormatErrors=_H3cIpxStatFormatErrors_Object((1,3,6,1,4,1,2011,10,2,34,4,1,4),_H3cIpxStatFormatErrors_Type())
h3cIpxStatFormatErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatFormatErrors.setStatus(_A)
_H3cIpxStatBadHops_Type=Counter32
_H3cIpxStatBadHops_Object=MibScalar
h3cIpxStatBadHops=_H3cIpxStatBadHops_Object((1,3,6,1,4,1,2011,10,2,34,4,1,5),_H3cIpxStatBadHops_Type())
h3cIpxStatBadHops.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatBadHops.setStatus(_A)
_H3cIpxStatHopsDiscards_Type=Counter32
_H3cIpxStatHopsDiscards_Object=MibScalar
h3cIpxStatHopsDiscards=_H3cIpxStatHopsDiscards_Object((1,3,6,1,4,1,2011,10,2,34,4,1,6),_H3cIpxStatHopsDiscards_Type())
h3cIpxStatHopsDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatHopsDiscards.setStatus(_A)
_H3cIpxStatOtherErrors_Type=Counter32
_H3cIpxStatOtherErrors_Object=MibScalar
h3cIpxStatOtherErrors=_H3cIpxStatOtherErrors_Object((1,3,6,1,4,1,2011,10,2,34,4,1,7),_H3cIpxStatOtherErrors_Type())
h3cIpxStatOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatOtherErrors.setStatus(_A)
_H3cIpxStatLocalDests_Type=Counter32
_H3cIpxStatLocalDests_Object=MibScalar
h3cIpxStatLocalDests=_H3cIpxStatLocalDests_Object((1,3,6,1,4,1,2011,10,2,34,4,1,8),_H3cIpxStatLocalDests_Type())
h3cIpxStatLocalDests.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatLocalDests.setStatus(_A)
_H3cIpxStatCantDeals_Type=Counter32
_H3cIpxStatCantDeals_Object=MibScalar
h3cIpxStatCantDeals=_H3cIpxStatCantDeals_Object((1,3,6,1,4,1,2011,10,2,34,4,1,9),_H3cIpxStatCantDeals_Type())
h3cIpxStatCantDeals.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatCantDeals.setStatus(_A)
_H3cIpxStatForwards_Type=Counter32
_H3cIpxStatForwards_Object=MibScalar
h3cIpxStatForwards=_H3cIpxStatForwards_Object((1,3,6,1,4,1,2011,10,2,34,4,1,10),_H3cIpxStatForwards_Type())
h3cIpxStatForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatForwards.setStatus(_A)
_H3cIpxStatGenerates_Type=Counter32
_H3cIpxStatGenerates_Object=MibScalar
h3cIpxStatGenerates=_H3cIpxStatGenerates_Object((1,3,6,1,4,1,2011,10,2,34,4,1,11),_H3cIpxStatGenerates_Type())
h3cIpxStatGenerates.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatGenerates.setStatus(_A)
_H3cIpxStatNoRoutes_Type=Counter32
_H3cIpxStatNoRoutes_Object=MibScalar
h3cIpxStatNoRoutes=_H3cIpxStatNoRoutes_Object((1,3,6,1,4,1,2011,10,2,34,4,1,12),_H3cIpxStatNoRoutes_Type())
h3cIpxStatNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatNoRoutes.setStatus(_A)
_H3cIpxStatOutDiscards_Type=Counter32
_H3cIpxStatOutDiscards_Object=MibScalar
h3cIpxStatOutDiscards=_H3cIpxStatOutDiscards_Object((1,3,6,1,4,1,2011,10,2,34,4,1,13),_H3cIpxStatOutDiscards_Type())
h3cIpxStatOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatOutDiscards.setStatus(_A)
_H3cIpxStatRipSends_Type=Counter32
_H3cIpxStatRipSends_Object=MibScalar
h3cIpxStatRipSends=_H3cIpxStatRipSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,14),_H3cIpxStatRipSends_Type())
h3cIpxStatRipSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipSends.setStatus(_A)
_H3cIpxStatRipReceives_Type=Counter32
_H3cIpxStatRipReceives_Object=MibScalar
h3cIpxStatRipReceives=_H3cIpxStatRipReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,15),_H3cIpxStatRipReceives_Type())
h3cIpxStatRipReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipReceives.setStatus(_A)
_H3cIpxStaRipRspSends_Type=Counter32
_H3cIpxStaRipRspSends_Object=MibScalar
h3cIpxStaRipRspSends=_H3cIpxStaRipRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,16),_H3cIpxStaRipRspSends_Type())
h3cIpxStaRipRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStaRipRspSends.setStatus(_A)
_H3cIpxStaRipRspReceives_Type=Counter32
_H3cIpxStaRipRspReceives_Object=MibScalar
h3cIpxStaRipRspReceives=_H3cIpxStaRipRspReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,17),_H3cIpxStaRipRspReceives_Type())
h3cIpxStaRipRspReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStaRipRspReceives.setStatus(_A)
_H3cIpxStatRipReqReceives_Type=Counter32
_H3cIpxStatRipReqReceives_Object=MibScalar
h3cIpxStatRipReqReceives=_H3cIpxStatRipReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,18),_H3cIpxStatRipReqReceives_Type())
h3cIpxStatRipReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipReqReceives.setStatus(_A)
_H3cIpxStatRipReqDeals_Type=Counter32
_H3cIpxStatRipReqDeals_Object=MibScalar
h3cIpxStatRipReqDeals=_H3cIpxStatRipReqDeals_Object((1,3,6,1,4,1,2011,10,2,34,4,1,19),_H3cIpxStatRipReqDeals_Type())
h3cIpxStatRipReqDeals.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipReqDeals.setStatus(_A)
_H3cIpxStatRipReqSends_Type=Counter32
_H3cIpxStatRipReqSends_Object=MibScalar
h3cIpxStatRipReqSends=_H3cIpxStatRipReqSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,20),_H3cIpxStatRipReqSends_Type())
h3cIpxStatRipReqSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipReqSends.setStatus(_A)
_H3cIpxStatRipPeriUpdates_Type=Counter32
_H3cIpxStatRipPeriUpdates_Object=MibScalar
h3cIpxStatRipPeriUpdates=_H3cIpxStatRipPeriUpdates_Object((1,3,6,1,4,1,2011,10,2,34,4,1,21),_H3cIpxStatRipPeriUpdates_Type())
h3cIpxStatRipPeriUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatRipPeriUpdates.setStatus(_A)
_H3cIpxStatSapGenReqReceives_Type=Counter32
_H3cIpxStatSapGenReqReceives_Object=MibScalar
h3cIpxStatSapGenReqReceives=_H3cIpxStatSapGenReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,22),_H3cIpxStatSapGenReqReceives_Type())
h3cIpxStatSapGenReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapGenReqReceives.setStatus(_A)
_H3cIpxStatSapSpecReqReceives_Type=Counter32
_H3cIpxStatSapSpecReqReceives_Object=MibScalar
h3cIpxStatSapSpecReqReceives=_H3cIpxStatSapSpecReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,23),_H3cIpxStatSapSpecReqReceives_Type())
h3cIpxStatSapSpecReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapSpecReqReceives.setStatus(_A)
_H3cIpxStatSapGnsReqReceives_Type=Counter32
_H3cIpxStatSapGnsReqReceives_Object=MibScalar
h3cIpxStatSapGnsReqReceives=_H3cIpxStatSapGnsReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,1,24),_H3cIpxStatSapGnsReqReceives_Type())
h3cIpxStatSapGnsReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapGnsReqReceives.setStatus(_A)
_H3cIpxStatSapGenRspSends_Type=Counter32
_H3cIpxStatSapGenRspSends_Object=MibScalar
h3cIpxStatSapGenRspSends=_H3cIpxStatSapGenRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,25),_H3cIpxStatSapGenRspSends_Type())
h3cIpxStatSapGenRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapGenRspSends.setStatus(_A)
_H3cIpxStatSapSpecRspSends_Type=Counter32
_H3cIpxStatSapSpecRspSends_Object=MibScalar
h3cIpxStatSapSpecRspSends=_H3cIpxStatSapSpecRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,26),_H3cIpxStatSapSpecRspSends_Type())
h3cIpxStatSapSpecRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapSpecRspSends.setStatus(_A)
_H3cIpxStatSapGnsRspSends_Type=Counter32
_H3cIpxStatSapGnsRspSends_Object=MibScalar
h3cIpxStatSapGnsRspSends=_H3cIpxStatSapGnsRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,1,27),_H3cIpxStatSapGnsRspSends_Type())
h3cIpxStatSapGnsRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapGnsRspSends.setStatus(_A)
_H3cIpxStatSapPeriUpdates_Type=Counter32
_H3cIpxStatSapPeriUpdates_Object=MibScalar
h3cIpxStatSapPeriUpdates=_H3cIpxStatSapPeriUpdates_Object((1,3,6,1,4,1,2011,10,2,34,4,1,28),_H3cIpxStatSapPeriUpdates_Type())
h3cIpxStatSapPeriUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapPeriUpdates.setStatus(_A)
_H3cIpxStatSapInPktErrors_Type=Counter32
_H3cIpxStatSapInPktErrors_Object=MibScalar
h3cIpxStatSapInPktErrors=_H3cIpxStatSapInPktErrors_Object((1,3,6,1,4,1,2011,10,2,34,4,1,29),_H3cIpxStatSapInPktErrors_Type())
h3cIpxStatSapInPktErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxStatSapInPktErrors.setStatus(_A)
_H3cIpxStatInterface_ObjectIdentity=ObjectIdentity
h3cIpxStatInterface=_H3cIpxStatInterface_ObjectIdentity((1,3,6,1,4,1,2011,10,2,34,4,2))
_H3cIpxIfStatTable_Object=MibTable
h3cIpxIfStatTable=_H3cIpxIfStatTable_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1))
if mibBuilder.loadTexts:h3cIpxIfStatTable.setStatus(_A)
_H3cIpxIfStatEntry_Object=MibTableRow
h3cIpxIfStatEntry=_H3cIpxIfStatEntry_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1))
h3cIpxIfStatEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:h3cIpxIfStatEntry.setStatus(_A)
class _H3cIpxIfStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpxIfStatIndex_Type.__name__=_C
_H3cIpxIfStatIndex_Object=MibTableColumn
h3cIpxIfStatIndex=_H3cIpxIfStatIndex_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,1),_H3cIpxIfStatIndex_Type())
h3cIpxIfStatIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cIpxIfStatIndex.setStatus(_A)
class _H3cIpxIfStatNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpxIfStatNetId_Type.__name__=_E
_H3cIpxIfStatNetId_Object=MibTableColumn
h3cIpxIfStatNetId=_H3cIpxIfStatNetId_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,2),_H3cIpxIfStatNetId_Type())
h3cIpxIfStatNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatNetId.setStatus(_A)
class _H3cIpxIfStatNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_H3cIpxIfStatNodeId_Type.__name__=_E
_H3cIpxIfStatNodeId_Object=MibTableColumn
h3cIpxIfStatNodeId=_H3cIpxIfStatNodeId_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,3),_H3cIpxIfStatNodeId_Type())
h3cIpxIfStatNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatNodeId.setStatus(_A)
_H3cIpxIfStatIpxReceives_Type=Counter32
_H3cIpxIfStatIpxReceives_Object=MibTableColumn
h3cIpxIfStatIpxReceives=_H3cIpxIfStatIpxReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,4),_H3cIpxIfStatIpxReceives_Type())
h3cIpxIfStatIpxReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatIpxReceives.setStatus(_A)
_H3cIpxIfStatIpxSends_Type=Counter32
_H3cIpxIfStatIpxSends_Object=MibTableColumn
h3cIpxIfStatIpxSends=_H3cIpxIfStatIpxSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,5),_H3cIpxIfStatIpxSends_Type())
h3cIpxIfStatIpxSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatIpxSends.setStatus(_A)
_H3cIpxIfStatIpxRecvBytes_Type=Counter32
_H3cIpxIfStatIpxRecvBytes_Object=MibTableColumn
h3cIpxIfStatIpxRecvBytes=_H3cIpxIfStatIpxRecvBytes_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,6),_H3cIpxIfStatIpxRecvBytes_Type())
h3cIpxIfStatIpxRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatIpxRecvBytes.setStatus(_A)
_H3cIpxIfStatIpxSendBytes_Type=Counter32
_H3cIpxIfStatIpxSendBytes_Object=MibTableColumn
h3cIpxIfStatIpxSendBytes=_H3cIpxIfStatIpxSendBytes_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,7),_H3cIpxIfStatIpxSendBytes_Type())
h3cIpxIfStatIpxSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatIpxSendBytes.setStatus(_A)
_H3cIpxIfStatRipReceives_Type=Counter32
_H3cIpxIfStatRipReceives_Object=MibTableColumn
h3cIpxIfStatRipReceives=_H3cIpxIfStatRipReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,8),_H3cIpxIfStatRipReceives_Type())
h3cIpxIfStatRipReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipReceives.setStatus(_A)
_H3cIpxIfStatRipSends_Type=Counter32
_H3cIpxIfStatRipSends_Object=MibTableColumn
h3cIpxIfStatRipSends=_H3cIpxIfStatRipSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,9),_H3cIpxIfStatRipSends_Type())
h3cIpxIfStatRipSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipSends.setStatus(_A)
_H3cIpxIfStatRipDiscards_Type=Counter32
_H3cIpxIfStatRipDiscards_Object=MibTableColumn
h3cIpxIfStatRipDiscards=_H3cIpxIfStatRipDiscards_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,10),_H3cIpxIfStatRipDiscards_Type())
h3cIpxIfStatRipDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipDiscards.setStatus(_A)
_H3cIpxIfStatRipSpecReqReceives_Type=Counter32
_H3cIpxIfStatRipSpecReqReceives_Object=MibTableColumn
h3cIpxIfStatRipSpecReqReceives=_H3cIpxIfStatRipSpecReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,11),_H3cIpxIfStatRipSpecReqReceives_Type())
h3cIpxIfStatRipSpecReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipSpecReqReceives.setStatus(_A)
_H3cIpxIfStatRipSpecRspSends_Type=Counter32
_H3cIpxIfStatRipSpecRspSends_Object=MibTableColumn
h3cIpxIfStatRipSpecRspSends=_H3cIpxIfStatRipSpecRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,12),_H3cIpxIfStatRipSpecRspSends_Type())
h3cIpxIfStatRipSpecRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipSpecRspSends.setStatus(_A)
_H3cIpxIfStatRipGenReqReceives_Type=Counter32
_H3cIpxIfStatRipGenReqReceives_Object=MibTableColumn
h3cIpxIfStatRipGenReqReceives=_H3cIpxIfStatRipGenReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,13),_H3cIpxIfStatRipGenReqReceives_Type())
h3cIpxIfStatRipGenReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipGenReqReceives.setStatus(_A)
_H3cIpxIfStatRipGenRspSends_Type=Counter32
_H3cIpxIfStatRipGenRspSends_Object=MibTableColumn
h3cIpxIfStatRipGenRspSends=_H3cIpxIfStatRipGenRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,14),_H3cIpxIfStatRipGenRspSends_Type())
h3cIpxIfStatRipGenRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatRipGenRspSends.setStatus(_A)
_H3cIpxIfStatSapReceives_Type=Counter32
_H3cIpxIfStatSapReceives_Object=MibTableColumn
h3cIpxIfStatSapReceives=_H3cIpxIfStatSapReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,15),_H3cIpxIfStatSapReceives_Type())
h3cIpxIfStatSapReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatSapReceives.setStatus(_A)
_H3cIpxIfStatSapSends_Type=Counter32
_H3cIpxIfStatSapSends_Object=MibTableColumn
h3cIpxIfStatSapSends=_H3cIpxIfStatSapSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,16),_H3cIpxIfStatSapSends_Type())
h3cIpxIfStatSapSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatSapSends.setStatus(_A)
_H3cIpxIfStatSapDiscards_Type=Counter32
_H3cIpxIfStatSapDiscards_Object=MibTableColumn
h3cIpxIfStatSapDiscards=_H3cIpxIfStatSapDiscards_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,17),_H3cIpxIfStatSapDiscards_Type())
h3cIpxIfStatSapDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatSapDiscards.setStatus(_A)
_H3cIpxIfStatSapGnsReqReceives_Type=Counter32
_H3cIpxIfStatSapGnsReqReceives_Object=MibTableColumn
h3cIpxIfStatSapGnsReqReceives=_H3cIpxIfStatSapGnsReqReceives_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,18),_H3cIpxIfStatSapGnsReqReceives_Type())
h3cIpxIfStatSapGnsReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatSapGnsReqReceives.setStatus(_A)
_H3cIpxIfStatSapGnsRspSends_Type=Counter32
_H3cIpxIfStatSapGnsRspSends_Object=MibTableColumn
h3cIpxIfStatSapGnsRspSends=_H3cIpxIfStatSapGnsRspSends_Object((1,3,6,1,4,1,2011,10,2,34,4,2,1,1,19),_H3cIpxIfStatSapGnsRspSends_Type())
h3cIpxIfStatSapGnsRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpxIfStatSapGnsRspSends.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_I:EnabledStatus,'h3cIpx':h3cIpx,'h3cIpxConfig':h3cIpxConfig,'h3cIpxStatus':h3cIpxStatus,'h3cIpxIfConfigTable':h3cIpxIfConfigTable,'h3cIpxIfConfigEntry':h3cIpxIfConfigEntry,_J:h3cIpxIfIndex,'h3cIpxIfNetId':h3cIpxIfNetId,'h3cIpxIfNodeId':h3cIpxIfNodeId,'h3cIpxIfSplitHorizon':h3cIpxIfSplitHorizon,'h3cIPxIfTick':h3cIPxIfTick,'h3cIpxIfUpdateChangeOnly':h3cIpxIfUpdateChangeOnly,'h3cIpxIfRipMtu':h3cIpxIfRipMtu,'h3cIpxIfEncapsuleType':h3cIpxIfEncapsuleType,'h3cIpxIfNetbiosPropagation':h3cIpxIfNetbiosPropagation,'h3cIpxIfSapStatus':h3cIpxIfSapStatus,'h3cIpxIfSapMtu':h3cIpxIfSapMtu,'h3cIpxIfGnsReply':h3cIpxIfGnsReply,'h3cIpxIfRowStatus':h3cIpxIfRowStatus,'h3cIpxRip':h3cIpxRip,'h3cIpxRouteMultiplier':h3cIpxRouteMultiplier,'h3cIpxRouteUpdateTimer':h3cIpxRouteUpdateTimer,'h3cIpxRouteImpRouteStatic':h3cIpxRouteImpRouteStatic,'h3cIpxRouteLoadBalancePaths':h3cIpxRouteLoadBalancePaths,'h3cIpxRouteMaxResPaths':h3cIpxRouteMaxResPaths,'h3cIpxRouteTable':h3cIpxRouteTable,'h3cIpxRouteEntry':h3cIpxRouteEntry,_K:h3cIpxRouteIndex,'h3cIpxRouteDestNetId':h3cIpxRouteDestNetId,'h3cIpxRouteNextHop':h3cIpxRouteNextHop,'h3cIpxRoutePro':h3cIpxRoutePro,'h3cIpxRoutePre':h3cIpxRoutePre,'h3cIpxRouteTicks':h3cIpxRouteTicks,'h3cIpxRouteHops':h3cIpxRouteHops,'h3cIpxRouteTime':h3cIpxRouteTime,'h3cIpxRouteOutInterface':h3cIpxRouteOutInterface,'h3cIpxStaticRouteTable':h3cIpxStaticRouteTable,'h3cIpxStaticRouteEntry':h3cIpxStaticRouteEntry,_M:h3cIpxStaticRouteDestNetId,_N:h3cIpxStaticRouteNextHop,'h3cIpxStaticRoutePre':h3cIpxStaticRoutePre,'h3cIpxStaticRouteOutIf':h3cIpxStaticRouteOutIf,'h3cIpxStaticRouteTicks':h3cIpxStaticRouteTicks,'h3cIpxStaticRouteHops':h3cIpxStaticRouteHops,'h3cIpxStaticRouteStatus':h3cIpxStaticRouteStatus,'h3cIpxStaticRouteRowStatus':h3cIpxStaticRouteRowStatus,'h3cIpxRouteStatTable':h3cIpxRouteStatTable,'h3cIpxRouteStatEntry':h3cIpxRouteStatEntry,_Q:h3cIpxRouteStatPro,'h3cIpxRouteStatRoutes':h3cIpxRouteStatRoutes,'h3cIpxRouteStatActives':h3cIpxRouteStatActives,'h3cIpxRouteStatAddeds':h3cIpxRouteStatAddeds,'h3cIpxRouteStatDeleteds':h3cIpxRouteStatDeleteds,'h3cIpxRouteStatFreeds':h3cIpxRouteStatFreeds,'h3cIpxSap':h3cIpxSap,'h3cIpxSapMultiplier':h3cIpxSapMultiplier,'h3cIpxSapUpdateTimer':h3cIpxSapUpdateTimer,'h3cIpxSapGnsLoadBalance':h3cIpxSapGnsLoadBalance,'h3cIpxSapMaxResServers':h3cIpxSapMaxResServers,'h3cIpxServiceTable':h3cIpxServiceTable,'h3cIpxServiceEntry':h3cIpxServiceEntry,_R:h3cIpxServiceIndex,'h3cIpxServiceName':h3cIpxServiceName,'h3cIpxServiceType':h3cIpxServiceType,'h3cIpxServiceNetId':h3cIpxServiceNetId,'h3cIpxServiceNodeId':h3cIpxServiceNodeId,'h3cIpxServiceSocketNo':h3cIpxServiceSocketNo,'h3cIpxServicePreference':h3cIpxServicePreference,'h3cIpxServiceHops':h3cIpxServiceHops,'h3cIpxServiceRecvIf':h3cIpxServiceRecvIf,'h3cIpxStaticServiceTable':h3cIpxStaticServiceTable,'h3cIpxStaticServiceEntry':h3cIpxStaticServiceEntry,_S:h3cIpxStaticServiceType,_T:h3cIpxStaticServiceName,_U:h3cIpxStaticServiceNetId,'h3cIpxStaticServiceNodeId':h3cIpxStaticServiceNodeId,'h3cIpxStatciServiceSocketNo':h3cIpxStatciServiceSocketNo,'h3cIpxStaticServicePreference':h3cIpxStaticServicePreference,'h3cIpxStaticServiceHops':h3cIpxStaticServiceHops,'h3cIpxStaticServiceStatus':h3cIpxStaticServiceStatus,'h3cIpxStaticServiceRowStatus':h3cIpxStaticServiceRowStatus,'h3cIpxStat':h3cIpxStat,'h3cIpxStatGlobal':h3cIpxStatGlobal,'h3cIpxStatTotalReceives':h3cIpxStatTotalReceives,'h3cIpxStatPitchs':h3cIpxStatPitchs,'h3cIpxStatLenErrors':h3cIpxStatLenErrors,'h3cIpxStatFormatErrors':h3cIpxStatFormatErrors,'h3cIpxStatBadHops':h3cIpxStatBadHops,'h3cIpxStatHopsDiscards':h3cIpxStatHopsDiscards,'h3cIpxStatOtherErrors':h3cIpxStatOtherErrors,'h3cIpxStatLocalDests':h3cIpxStatLocalDests,'h3cIpxStatCantDeals':h3cIpxStatCantDeals,'h3cIpxStatForwards':h3cIpxStatForwards,'h3cIpxStatGenerates':h3cIpxStatGenerates,'h3cIpxStatNoRoutes':h3cIpxStatNoRoutes,'h3cIpxStatOutDiscards':h3cIpxStatOutDiscards,'h3cIpxStatRipSends':h3cIpxStatRipSends,'h3cIpxStatRipReceives':h3cIpxStatRipReceives,'h3cIpxStaRipRspSends':h3cIpxStaRipRspSends,'h3cIpxStaRipRspReceives':h3cIpxStaRipRspReceives,'h3cIpxStatRipReqReceives':h3cIpxStatRipReqReceives,'h3cIpxStatRipReqDeals':h3cIpxStatRipReqDeals,'h3cIpxStatRipReqSends':h3cIpxStatRipReqSends,'h3cIpxStatRipPeriUpdates':h3cIpxStatRipPeriUpdates,'h3cIpxStatSapGenReqReceives':h3cIpxStatSapGenReqReceives,'h3cIpxStatSapSpecReqReceives':h3cIpxStatSapSpecReqReceives,'h3cIpxStatSapGnsReqReceives':h3cIpxStatSapGnsReqReceives,'h3cIpxStatSapGenRspSends':h3cIpxStatSapGenRspSends,'h3cIpxStatSapSpecRspSends':h3cIpxStatSapSpecRspSends,'h3cIpxStatSapGnsRspSends':h3cIpxStatSapGnsRspSends,'h3cIpxStatSapPeriUpdates':h3cIpxStatSapPeriUpdates,'h3cIpxStatSapInPktErrors':h3cIpxStatSapInPktErrors,'h3cIpxStatInterface':h3cIpxStatInterface,'h3cIpxIfStatTable':h3cIpxIfStatTable,'h3cIpxIfStatEntry':h3cIpxIfStatEntry,_V:h3cIpxIfStatIndex,'h3cIpxIfStatNetId':h3cIpxIfStatNetId,'h3cIpxIfStatNodeId':h3cIpxIfStatNodeId,'h3cIpxIfStatIpxReceives':h3cIpxIfStatIpxReceives,'h3cIpxIfStatIpxSends':h3cIpxIfStatIpxSends,'h3cIpxIfStatIpxRecvBytes':h3cIpxIfStatIpxRecvBytes,'h3cIpxIfStatIpxSendBytes':h3cIpxIfStatIpxSendBytes,'h3cIpxIfStatRipReceives':h3cIpxIfStatRipReceives,'h3cIpxIfStatRipSends':h3cIpxIfStatRipSends,'h3cIpxIfStatRipDiscards':h3cIpxIfStatRipDiscards,'h3cIpxIfStatRipSpecReqReceives':h3cIpxIfStatRipSpecReqReceives,'h3cIpxIfStatRipSpecRspSends':h3cIpxIfStatRipSpecRspSends,'h3cIpxIfStatRipGenReqReceives':h3cIpxIfStatRipGenReqReceives,'h3cIpxIfStatRipGenRspSends':h3cIpxIfStatRipGenRspSends,'h3cIpxIfStatSapReceives':h3cIpxIfStatSapReceives,'h3cIpxIfStatSapSends':h3cIpxIfStatSapSends,'h3cIpxIfStatSapDiscards':h3cIpxIfStatSapDiscards,'h3cIpxIfStatSapGnsReqReceives':h3cIpxIfStatSapGnsReqReceives,'h3cIpxIfStatSapGnsRspSends':h3cIpxIfStatSapGnsRspSends})