_V='hpnicfIpxIfStatIndex'
_U='hpnicfIpxStaticServiceNetId'
_T='hpnicfIpxStaticServiceName'
_S='hpnicfIpxStaticServiceType'
_R='hpnicfIpxServiceIndex'
_Q='hpnicfIpxRouteStatPro'
_P='inactive'
_O='active'
_N='hpnicfIpxStaticRouteNextHop'
_M='hpnicfIpxStaticRouteDestNetId'
_L='direct'
_K='hpnicfIpxRouteIndex'
_J='hpnicfIpxIfIndex'
_I='EnabledStatus'
_H='not-accessible'
_G='read-write'
_F='HPN-ICF-IPX-MIB'
_E='OctetString'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfIpx=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfIpxConfig_ObjectIdentity=ObjectIdentity
hpnicfIpxConfig=_HpnicfIpxConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,1))
class _HpnicfIpxStatus_Type(EnabledStatus):defaultValue=2
_HpnicfIpxStatus_Type.__name__=_I
_HpnicfIpxStatus_Object=MibScalar
hpnicfIpxStatus=_HpnicfIpxStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,1),_HpnicfIpxStatus_Type())
hpnicfIpxStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxStatus.setStatus(_A)
_HpnicfIpxIfConfigTable_Object=MibTable
hpnicfIpxIfConfigTable=_HpnicfIpxIfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2))
if mibBuilder.loadTexts:hpnicfIpxIfConfigTable.setStatus(_A)
_HpnicfIpxIfConfigEntry_Object=MibTableRow
hpnicfIpxIfConfigEntry=_HpnicfIpxIfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1))
hpnicfIpxIfConfigEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:hpnicfIpxIfConfigEntry.setStatus(_A)
class _HpnicfIpxIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpxIfIndex_Type.__name__=_C
_HpnicfIpxIfIndex_Object=MibTableColumn
hpnicfIpxIfIndex=_HpnicfIpxIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,1),_HpnicfIpxIfIndex_Type())
hpnicfIpxIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxIfIndex.setStatus(_A)
class _HpnicfIpxIfNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxIfNetId_Type.__name__=_E
_HpnicfIpxIfNetId_Object=MibTableColumn
hpnicfIpxIfNetId=_HpnicfIpxIfNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,2),_HpnicfIpxIfNetId_Type())
hpnicfIpxIfNetId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfNetId.setStatus(_A)
class _HpnicfIpxIfNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnicfIpxIfNodeId_Type.__name__=_E
_HpnicfIpxIfNodeId_Object=MibTableColumn
hpnicfIpxIfNodeId=_HpnicfIpxIfNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,3),_HpnicfIpxIfNodeId_Type())
hpnicfIpxIfNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfNodeId.setStatus(_A)
class _HpnicfIpxIfSplitHorizon_Type(EnabledStatus):defaultValue=1
_HpnicfIpxIfSplitHorizon_Type.__name__=_I
_HpnicfIpxIfSplitHorizon_Object=MibTableColumn
hpnicfIpxIfSplitHorizon=_HpnicfIpxIfSplitHorizon_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,4),_HpnicfIpxIfSplitHorizon_Type())
hpnicfIpxIfSplitHorizon.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfSplitHorizon.setStatus(_A)
class _HpnicfIPxIfTick_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30000))
_HpnicfIPxIfTick_Type.__name__=_C
_HpnicfIPxIfTick_Object=MibTableColumn
hpnicfIPxIfTick=_HpnicfIPxIfTick_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,5),_HpnicfIPxIfTick_Type())
hpnicfIPxIfTick.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIPxIfTick.setStatus(_A)
class _HpnicfIpxIfUpdateChangeOnly_Type(EnabledStatus):defaultValue=2
_HpnicfIpxIfUpdateChangeOnly_Type.__name__=_I
_HpnicfIpxIfUpdateChangeOnly_Object=MibTableColumn
hpnicfIpxIfUpdateChangeOnly=_HpnicfIpxIfUpdateChangeOnly_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,6),_HpnicfIpxIfUpdateChangeOnly_Type())
hpnicfIpxIfUpdateChangeOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfUpdateChangeOnly.setStatus(_A)
class _HpnicfIpxIfRipMtu_Type(Integer32):defaultValue=432;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(432,1500))
_HpnicfIpxIfRipMtu_Type.__name__=_C
_HpnicfIpxIfRipMtu_Object=MibTableColumn
hpnicfIpxIfRipMtu=_HpnicfIpxIfRipMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,7),_HpnicfIpxIfRipMtu_Type())
hpnicfIpxIfRipMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfRipMtu.setStatus(_A)
class _HpnicfIpxIfEncapsuleType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dot2',1),('dot3',2),('ethernet-2',3),('snap',4),('unkown',5)))
_HpnicfIpxIfEncapsuleType_Type.__name__=_C
_HpnicfIpxIfEncapsuleType_Object=MibTableColumn
hpnicfIpxIfEncapsuleType=_HpnicfIpxIfEncapsuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,8),_HpnicfIpxIfEncapsuleType_Type())
hpnicfIpxIfEncapsuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfEncapsuleType.setStatus(_A)
class _HpnicfIpxIfNetbiosPropagation_Type(EnabledStatus):defaultValue=2
_HpnicfIpxIfNetbiosPropagation_Type.__name__=_I
_HpnicfIpxIfNetbiosPropagation_Object=MibTableColumn
hpnicfIpxIfNetbiosPropagation=_HpnicfIpxIfNetbiosPropagation_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,9),_HpnicfIpxIfNetbiosPropagation_Type())
hpnicfIpxIfNetbiosPropagation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfNetbiosPropagation.setStatus(_A)
class _HpnicfIpxIfSapStatus_Type(EnabledStatus):defaultValue=1
_HpnicfIpxIfSapStatus_Type.__name__=_I
_HpnicfIpxIfSapStatus_Object=MibTableColumn
hpnicfIpxIfSapStatus=_HpnicfIpxIfSapStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,10),_HpnicfIpxIfSapStatus_Type())
hpnicfIpxIfSapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfSapStatus.setStatus(_A)
class _HpnicfIpxIfSapMtu_Type(Integer32):defaultValue=480;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(480,1500))
_HpnicfIpxIfSapMtu_Type.__name__=_C
_HpnicfIpxIfSapMtu_Object=MibTableColumn
hpnicfIpxIfSapMtu=_HpnicfIpxIfSapMtu_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,11),_HpnicfIpxIfSapMtu_Type())
hpnicfIpxIfSapMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfSapMtu.setStatus(_A)
class _HpnicfIpxIfGnsReply_Type(EnabledStatus):defaultValue=1
_HpnicfIpxIfGnsReply_Type.__name__=_I
_HpnicfIpxIfGnsReply_Object=MibTableColumn
hpnicfIpxIfGnsReply=_HpnicfIpxIfGnsReply_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,12),_HpnicfIpxIfGnsReply_Type())
hpnicfIpxIfGnsReply.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfGnsReply.setStatus(_A)
_HpnicfIpxIfRowStatus_Type=RowStatus
_HpnicfIpxIfRowStatus_Object=MibTableColumn
hpnicfIpxIfRowStatus=_HpnicfIpxIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,1,2,1,13),_HpnicfIpxIfRowStatus_Type())
hpnicfIpxIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxIfRowStatus.setStatus(_A)
_HpnicfIpxRip_ObjectIdentity=ObjectIdentity
hpnicfIpxRip=_HpnicfIpxRip_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,2))
class _HpnicfIpxRouteMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HpnicfIpxRouteMultiplier_Type.__name__=_C
_HpnicfIpxRouteMultiplier_Object=MibScalar
hpnicfIpxRouteMultiplier=_HpnicfIpxRouteMultiplier_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,1),_HpnicfIpxRouteMultiplier_Type())
hpnicfIpxRouteMultiplier.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxRouteMultiplier.setStatus(_A)
class _HpnicfIpxRouteUpdateTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60000))
_HpnicfIpxRouteUpdateTimer_Type.__name__=_C
_HpnicfIpxRouteUpdateTimer_Object=MibScalar
hpnicfIpxRouteUpdateTimer=_HpnicfIpxRouteUpdateTimer_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,2),_HpnicfIpxRouteUpdateTimer_Type())
hpnicfIpxRouteUpdateTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxRouteUpdateTimer.setStatus(_A)
class _HpnicfIpxRouteImpRouteStatic_Type(EnabledStatus):defaultValue=2
_HpnicfIpxRouteImpRouteStatic_Type.__name__=_I
_HpnicfIpxRouteImpRouteStatic_Object=MibScalar
hpnicfIpxRouteImpRouteStatic=_HpnicfIpxRouteImpRouteStatic_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,3),_HpnicfIpxRouteImpRouteStatic_Type())
hpnicfIpxRouteImpRouteStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxRouteImpRouteStatic.setStatus(_A)
class _HpnicfIpxRouteLoadBalancePaths_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfIpxRouteLoadBalancePaths_Type.__name__=_C
_HpnicfIpxRouteLoadBalancePaths_Object=MibScalar
hpnicfIpxRouteLoadBalancePaths=_HpnicfIpxRouteLoadBalancePaths_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,4),_HpnicfIpxRouteLoadBalancePaths_Type())
hpnicfIpxRouteLoadBalancePaths.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxRouteLoadBalancePaths.setStatus(_A)
class _HpnicfIpxRouteMaxResPaths_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfIpxRouteMaxResPaths_Type.__name__=_C
_HpnicfIpxRouteMaxResPaths_Object=MibScalar
hpnicfIpxRouteMaxResPaths=_HpnicfIpxRouteMaxResPaths_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,5),_HpnicfIpxRouteMaxResPaths_Type())
hpnicfIpxRouteMaxResPaths.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxRouteMaxResPaths.setStatus(_A)
_HpnicfIpxRouteTable_Object=MibTable
hpnicfIpxRouteTable=_HpnicfIpxRouteTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6))
if mibBuilder.loadTexts:hpnicfIpxRouteTable.setStatus(_A)
_HpnicfIpxRouteEntry_Object=MibTableRow
hpnicfIpxRouteEntry=_HpnicfIpxRouteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1))
hpnicfIpxRouteEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:hpnicfIpxRouteEntry.setStatus(_A)
_HpnicfIpxRouteIndex_Type=Integer32
_HpnicfIpxRouteIndex_Object=MibTableColumn
hpnicfIpxRouteIndex=_HpnicfIpxRouteIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,1),_HpnicfIpxRouteIndex_Type())
hpnicfIpxRouteIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxRouteIndex.setStatus(_A)
class _HpnicfIpxRouteDestNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxRouteDestNetId_Type.__name__=_E
_HpnicfIpxRouteDestNetId_Object=MibTableColumn
hpnicfIpxRouteDestNetId=_HpnicfIpxRouteDestNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,2),_HpnicfIpxRouteDestNetId_Type())
hpnicfIpxRouteDestNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteDestNetId.setStatus(_A)
class _HpnicfIpxRouteNextHop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfIpxRouteNextHop_Type.__name__=_E
_HpnicfIpxRouteNextHop_Object=MibTableColumn
hpnicfIpxRouteNextHop=_HpnicfIpxRouteNextHop_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,3),_HpnicfIpxRouteNextHop_Type())
hpnicfIpxRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteNextHop.setStatus(_A)
class _HpnicfIpxRoutePro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('rip',2)))
_HpnicfIpxRoutePro_Type.__name__=_C
_HpnicfIpxRoutePro_Object=MibTableColumn
hpnicfIpxRoutePro=_HpnicfIpxRoutePro_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,4),_HpnicfIpxRoutePro_Type())
hpnicfIpxRoutePro.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRoutePro.setStatus(_A)
_HpnicfIpxRoutePre_Type=Integer32
_HpnicfIpxRoutePre_Object=MibTableColumn
hpnicfIpxRoutePre=_HpnicfIpxRoutePre_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,5),_HpnicfIpxRoutePre_Type())
hpnicfIpxRoutePre.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRoutePre.setStatus(_A)
class _HpnicfIpxRouteTicks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnicfIpxRouteTicks_Type.__name__=_C
_HpnicfIpxRouteTicks_Object=MibTableColumn
hpnicfIpxRouteTicks=_HpnicfIpxRouteTicks_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,6),_HpnicfIpxRouteTicks_Type())
hpnicfIpxRouteTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteTicks.setStatus(_A)
class _HpnicfIpxRouteHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfIpxRouteHops_Type.__name__=_C
_HpnicfIpxRouteHops_Object=MibTableColumn
hpnicfIpxRouteHops=_HpnicfIpxRouteHops_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,7),_HpnicfIpxRouteHops_Type())
hpnicfIpxRouteHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteHops.setStatus(_A)
class _HpnicfIpxRouteTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000000))
_HpnicfIpxRouteTime_Type.__name__=_C
_HpnicfIpxRouteTime_Object=MibTableColumn
hpnicfIpxRouteTime=_HpnicfIpxRouteTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,8),_HpnicfIpxRouteTime_Type())
hpnicfIpxRouteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteTime.setStatus(_A)
class _HpnicfIpxRouteOutInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_HpnicfIpxRouteOutInterface_Type.__name__=_E
_HpnicfIpxRouteOutInterface_Object=MibTableColumn
hpnicfIpxRouteOutInterface=_HpnicfIpxRouteOutInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,6,1,9),_HpnicfIpxRouteOutInterface_Type())
hpnicfIpxRouteOutInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteOutInterface.setStatus(_A)
_HpnicfIpxStaticRouteTable_Object=MibTable
hpnicfIpxStaticRouteTable=_HpnicfIpxStaticRouteTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7))
if mibBuilder.loadTexts:hpnicfIpxStaticRouteTable.setStatus(_A)
_HpnicfIpxStaticRouteEntry_Object=MibTableRow
hpnicfIpxStaticRouteEntry=_HpnicfIpxStaticRouteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1))
hpnicfIpxStaticRouteEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:hpnicfIpxStaticRouteEntry.setStatus(_A)
class _HpnicfIpxStaticRouteDestNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxStaticRouteDestNetId_Type.__name__=_E
_HpnicfIpxStaticRouteDestNetId_Object=MibTableColumn
hpnicfIpxStaticRouteDestNetId=_HpnicfIpxStaticRouteDestNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,1),_HpnicfIpxStaticRouteDestNetId_Type())
hpnicfIpxStaticRouteDestNetId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteDestNetId.setStatus(_A)
class _HpnicfIpxStaticRouteNextHop_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HpnicfIpxStaticRouteNextHop_Type.__name__=_E
_HpnicfIpxStaticRouteNextHop_Object=MibTableColumn
hpnicfIpxStaticRouteNextHop=_HpnicfIpxStaticRouteNextHop_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,2),_HpnicfIpxStaticRouteNextHop_Type())
hpnicfIpxStaticRouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteNextHop.setStatus(_A)
class _HpnicfIpxStaticRoutePre_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfIpxStaticRoutePre_Type.__name__=_C
_HpnicfIpxStaticRoutePre_Object=MibTableColumn
hpnicfIpxStaticRoutePre=_HpnicfIpxStaticRoutePre_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,3),_HpnicfIpxStaticRoutePre_Type())
hpnicfIpxStaticRoutePre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRoutePre.setStatus(_A)
class _HpnicfIpxStaticRouteOutIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_HpnicfIpxStaticRouteOutIf_Type.__name__=_E
_HpnicfIpxStaticRouteOutIf_Object=MibTableColumn
hpnicfIpxStaticRouteOutIf=_HpnicfIpxStaticRouteOutIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,4),_HpnicfIpxStaticRouteOutIf_Type())
hpnicfIpxStaticRouteOutIf.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteOutIf.setStatus(_A)
class _HpnicfIpxStaticRouteTicks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnicfIpxStaticRouteTicks_Type.__name__=_C
_HpnicfIpxStaticRouteTicks_Object=MibTableColumn
hpnicfIpxStaticRouteTicks=_HpnicfIpxStaticRouteTicks_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,5),_HpnicfIpxStaticRouteTicks_Type())
hpnicfIpxStaticRouteTicks.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteTicks.setStatus(_A)
class _HpnicfIpxStaticRouteHops_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfIpxStaticRouteHops_Type.__name__=_C
_HpnicfIpxStaticRouteHops_Object=MibTableColumn
hpnicfIpxStaticRouteHops=_HpnicfIpxStaticRouteHops_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,6),_HpnicfIpxStaticRouteHops_Type())
hpnicfIpxStaticRouteHops.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteHops.setStatus(_A)
class _HpnicfIpxStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_HpnicfIpxStaticRouteStatus_Type.__name__=_C
_HpnicfIpxStaticRouteStatus_Object=MibTableColumn
hpnicfIpxStaticRouteStatus=_HpnicfIpxStaticRouteStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,7),_HpnicfIpxStaticRouteStatus_Type())
hpnicfIpxStaticRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteStatus.setStatus(_A)
_HpnicfIpxStaticRouteRowStatus_Type=RowStatus
_HpnicfIpxStaticRouteRowStatus_Object=MibTableColumn
hpnicfIpxStaticRouteRowStatus=_HpnicfIpxStaticRouteRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,7,1,8),_HpnicfIpxStaticRouteRowStatus_Type())
hpnicfIpxStaticRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticRouteRowStatus.setStatus(_A)
_HpnicfIpxRouteStatTable_Object=MibTable
hpnicfIpxRouteStatTable=_HpnicfIpxRouteStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8))
if mibBuilder.loadTexts:hpnicfIpxRouteStatTable.setStatus(_A)
_HpnicfIpxRouteStatEntry_Object=MibTableRow
hpnicfIpxRouteStatEntry=_HpnicfIpxRouteStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1))
hpnicfIpxRouteStatEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:hpnicfIpxRouteStatEntry.setStatus(_A)
class _HpnicfIpxRouteStatPro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('static',2),('rip',3),('default',4),('total',5)))
_HpnicfIpxRouteStatPro_Type.__name__=_C
_HpnicfIpxRouteStatPro_Object=MibTableColumn
hpnicfIpxRouteStatPro=_HpnicfIpxRouteStatPro_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,1),_HpnicfIpxRouteStatPro_Type())
hpnicfIpxRouteStatPro.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxRouteStatPro.setStatus(_A)
_HpnicfIpxRouteStatRoutes_Type=Counter32
_HpnicfIpxRouteStatRoutes_Object=MibTableColumn
hpnicfIpxRouteStatRoutes=_HpnicfIpxRouteStatRoutes_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,2),_HpnicfIpxRouteStatRoutes_Type())
hpnicfIpxRouteStatRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteStatRoutes.setStatus(_A)
_HpnicfIpxRouteStatActives_Type=Counter32
_HpnicfIpxRouteStatActives_Object=MibTableColumn
hpnicfIpxRouteStatActives=_HpnicfIpxRouteStatActives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,3),_HpnicfIpxRouteStatActives_Type())
hpnicfIpxRouteStatActives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteStatActives.setStatus(_A)
_HpnicfIpxRouteStatAddeds_Type=Counter32
_HpnicfIpxRouteStatAddeds_Object=MibTableColumn
hpnicfIpxRouteStatAddeds=_HpnicfIpxRouteStatAddeds_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,4),_HpnicfIpxRouteStatAddeds_Type())
hpnicfIpxRouteStatAddeds.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteStatAddeds.setStatus(_A)
_HpnicfIpxRouteStatDeleteds_Type=Counter32
_HpnicfIpxRouteStatDeleteds_Object=MibTableColumn
hpnicfIpxRouteStatDeleteds=_HpnicfIpxRouteStatDeleteds_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,5),_HpnicfIpxRouteStatDeleteds_Type())
hpnicfIpxRouteStatDeleteds.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteStatDeleteds.setStatus(_A)
_HpnicfIpxRouteStatFreeds_Type=Counter32
_HpnicfIpxRouteStatFreeds_Object=MibTableColumn
hpnicfIpxRouteStatFreeds=_HpnicfIpxRouteStatFreeds_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,2,8,1,6),_HpnicfIpxRouteStatFreeds_Type())
hpnicfIpxRouteStatFreeds.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxRouteStatFreeds.setStatus(_A)
_HpnicfIpxSap_ObjectIdentity=ObjectIdentity
hpnicfIpxSap=_HpnicfIpxSap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,3))
class _HpnicfIpxSapMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HpnicfIpxSapMultiplier_Type.__name__=_C
_HpnicfIpxSapMultiplier_Object=MibScalar
hpnicfIpxSapMultiplier=_HpnicfIpxSapMultiplier_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,1),_HpnicfIpxSapMultiplier_Type())
hpnicfIpxSapMultiplier.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxSapMultiplier.setStatus(_A)
class _HpnicfIpxSapUpdateTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60000))
_HpnicfIpxSapUpdateTimer_Type.__name__=_C
_HpnicfIpxSapUpdateTimer_Object=MibScalar
hpnicfIpxSapUpdateTimer=_HpnicfIpxSapUpdateTimer_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,2),_HpnicfIpxSapUpdateTimer_Type())
hpnicfIpxSapUpdateTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxSapUpdateTimer.setStatus(_A)
class _HpnicfIpxSapGnsLoadBalance_Type(EnabledStatus):defaultValue=1
_HpnicfIpxSapGnsLoadBalance_Type.__name__=_I
_HpnicfIpxSapGnsLoadBalance_Object=MibScalar
hpnicfIpxSapGnsLoadBalance=_HpnicfIpxSapGnsLoadBalance_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,3),_HpnicfIpxSapGnsLoadBalance_Type())
hpnicfIpxSapGnsLoadBalance.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxSapGnsLoadBalance.setStatus(_A)
class _HpnicfIpxSapMaxResServers_Type(Integer32):defaultValue=2048;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_HpnicfIpxSapMaxResServers_Type.__name__=_C
_HpnicfIpxSapMaxResServers_Object=MibScalar
hpnicfIpxSapMaxResServers=_HpnicfIpxSapMaxResServers_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,4),_HpnicfIpxSapMaxResServers_Type())
hpnicfIpxSapMaxResServers.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpxSapMaxResServers.setStatus(_A)
_HpnicfIpxServiceTable_Object=MibTable
hpnicfIpxServiceTable=_HpnicfIpxServiceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5))
if mibBuilder.loadTexts:hpnicfIpxServiceTable.setStatus(_A)
_HpnicfIpxServiceEntry_Object=MibTableRow
hpnicfIpxServiceEntry=_HpnicfIpxServiceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1))
hpnicfIpxServiceEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:hpnicfIpxServiceEntry.setStatus(_A)
_HpnicfIpxServiceIndex_Type=Integer32
_HpnicfIpxServiceIndex_Object=MibTableColumn
hpnicfIpxServiceIndex=_HpnicfIpxServiceIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,1),_HpnicfIpxServiceIndex_Type())
hpnicfIpxServiceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxServiceIndex.setStatus(_A)
class _HpnicfIpxServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,47))
_HpnicfIpxServiceName_Type.__name__=_E
_HpnicfIpxServiceName_Object=MibTableColumn
hpnicfIpxServiceName=_HpnicfIpxServiceName_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,2),_HpnicfIpxServiceName_Type())
hpnicfIpxServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceName.setStatus(_A)
class _HpnicfIpxServiceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnicfIpxServiceType_Type.__name__=_E
_HpnicfIpxServiceType_Object=MibTableColumn
hpnicfIpxServiceType=_HpnicfIpxServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,3),_HpnicfIpxServiceType_Type())
hpnicfIpxServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceType.setStatus(_A)
class _HpnicfIpxServiceNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxServiceNetId_Type.__name__=_E
_HpnicfIpxServiceNetId_Object=MibTableColumn
hpnicfIpxServiceNetId=_HpnicfIpxServiceNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,4),_HpnicfIpxServiceNetId_Type())
hpnicfIpxServiceNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceNetId.setStatus(_A)
class _HpnicfIpxServiceNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnicfIpxServiceNodeId_Type.__name__=_E
_HpnicfIpxServiceNodeId_Object=MibTableColumn
hpnicfIpxServiceNodeId=_HpnicfIpxServiceNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,5),_HpnicfIpxServiceNodeId_Type())
hpnicfIpxServiceNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceNodeId.setStatus(_A)
class _HpnicfIpxServiceSocketNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnicfIpxServiceSocketNo_Type.__name__=_E
_HpnicfIpxServiceSocketNo_Object=MibTableColumn
hpnicfIpxServiceSocketNo=_HpnicfIpxServiceSocketNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,6),_HpnicfIpxServiceSocketNo_Type())
hpnicfIpxServiceSocketNo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceSocketNo.setStatus(_A)
_HpnicfIpxServicePreference_Type=Integer32
_HpnicfIpxServicePreference_Object=MibTableColumn
hpnicfIpxServicePreference=_HpnicfIpxServicePreference_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,7),_HpnicfIpxServicePreference_Type())
hpnicfIpxServicePreference.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServicePreference.setStatus(_A)
class _HpnicfIpxServiceHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfIpxServiceHops_Type.__name__=_C
_HpnicfIpxServiceHops_Object=MibTableColumn
hpnicfIpxServiceHops=_HpnicfIpxServiceHops_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,8),_HpnicfIpxServiceHops_Type())
hpnicfIpxServiceHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceHops.setStatus(_A)
class _HpnicfIpxServiceRecvIf_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_HpnicfIpxServiceRecvIf_Type.__name__=_E
_HpnicfIpxServiceRecvIf_Object=MibTableColumn
hpnicfIpxServiceRecvIf=_HpnicfIpxServiceRecvIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,5,1,9),_HpnicfIpxServiceRecvIf_Type())
hpnicfIpxServiceRecvIf.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxServiceRecvIf.setStatus(_A)
_HpnicfIpxStaticServiceTable_Object=MibTable
hpnicfIpxStaticServiceTable=_HpnicfIpxStaticServiceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6))
if mibBuilder.loadTexts:hpnicfIpxStaticServiceTable.setStatus(_A)
_HpnicfIpxStaticServiceEntry_Object=MibTableRow
hpnicfIpxStaticServiceEntry=_HpnicfIpxStaticServiceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1))
hpnicfIpxStaticServiceEntry.setIndexNames((0,_F,_S),(0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:hpnicfIpxStaticServiceEntry.setStatus(_A)
class _HpnicfIpxStaticServiceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnicfIpxStaticServiceType_Type.__name__=_E
_HpnicfIpxStaticServiceType_Object=MibTableColumn
hpnicfIpxStaticServiceType=_HpnicfIpxStaticServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,1),_HpnicfIpxStaticServiceType_Type())
hpnicfIpxStaticServiceType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceType.setStatus(_A)
class _HpnicfIpxStaticServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,47))
_HpnicfIpxStaticServiceName_Type.__name__=_E
_HpnicfIpxStaticServiceName_Object=MibTableColumn
hpnicfIpxStaticServiceName=_HpnicfIpxStaticServiceName_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,2),_HpnicfIpxStaticServiceName_Type())
hpnicfIpxStaticServiceName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceName.setStatus(_A)
class _HpnicfIpxStaticServiceNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxStaticServiceNetId_Type.__name__=_E
_HpnicfIpxStaticServiceNetId_Object=MibTableColumn
hpnicfIpxStaticServiceNetId=_HpnicfIpxStaticServiceNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,3),_HpnicfIpxStaticServiceNetId_Type())
hpnicfIpxStaticServiceNetId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceNetId.setStatus(_A)
class _HpnicfIpxStaticServiceNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnicfIpxStaticServiceNodeId_Type.__name__=_E
_HpnicfIpxStaticServiceNodeId_Object=MibTableColumn
hpnicfIpxStaticServiceNodeId=_HpnicfIpxStaticServiceNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,4),_HpnicfIpxStaticServiceNodeId_Type())
hpnicfIpxStaticServiceNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceNodeId.setStatus(_A)
class _HpnicfIpxStatciServiceSocketNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnicfIpxStatciServiceSocketNo_Type.__name__=_E
_HpnicfIpxStatciServiceSocketNo_Object=MibTableColumn
hpnicfIpxStatciServiceSocketNo=_HpnicfIpxStatciServiceSocketNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,5),_HpnicfIpxStatciServiceSocketNo_Type())
hpnicfIpxStatciServiceSocketNo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStatciServiceSocketNo.setStatus(_A)
class _HpnicfIpxStaticServicePreference_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfIpxStaticServicePreference_Type.__name__=_C
_HpnicfIpxStaticServicePreference_Object=MibTableColumn
hpnicfIpxStaticServicePreference=_HpnicfIpxStaticServicePreference_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,6),_HpnicfIpxStaticServicePreference_Type())
hpnicfIpxStaticServicePreference.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticServicePreference.setStatus(_A)
class _HpnicfIpxStaticServiceHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfIpxStaticServiceHops_Type.__name__=_C
_HpnicfIpxStaticServiceHops_Object=MibTableColumn
hpnicfIpxStaticServiceHops=_HpnicfIpxStaticServiceHops_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,7),_HpnicfIpxStaticServiceHops_Type())
hpnicfIpxStaticServiceHops.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceHops.setStatus(_A)
class _HpnicfIpxStaticServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_HpnicfIpxStaticServiceStatus_Type.__name__=_C
_HpnicfIpxStaticServiceStatus_Object=MibTableColumn
hpnicfIpxStaticServiceStatus=_HpnicfIpxStaticServiceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,8),_HpnicfIpxStaticServiceStatus_Type())
hpnicfIpxStaticServiceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceStatus.setStatus(_A)
_HpnicfIpxStaticServiceRowStatus_Type=RowStatus
_HpnicfIpxStaticServiceRowStatus_Object=MibTableColumn
hpnicfIpxStaticServiceRowStatus=_HpnicfIpxStaticServiceRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,3,6,1,9),_HpnicfIpxStaticServiceRowStatus_Type())
hpnicfIpxStaticServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpxStaticServiceRowStatus.setStatus(_A)
_HpnicfIpxStat_ObjectIdentity=ObjectIdentity
hpnicfIpxStat=_HpnicfIpxStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,4))
_HpnicfIpxStatGlobal_ObjectIdentity=ObjectIdentity
hpnicfIpxStatGlobal=_HpnicfIpxStatGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1))
_HpnicfIpxStatTotalReceives_Type=Counter32
_HpnicfIpxStatTotalReceives_Object=MibScalar
hpnicfIpxStatTotalReceives=_HpnicfIpxStatTotalReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,1),_HpnicfIpxStatTotalReceives_Type())
hpnicfIpxStatTotalReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatTotalReceives.setStatus(_A)
_HpnicfIpxStatPitchs_Type=Counter32
_HpnicfIpxStatPitchs_Object=MibScalar
hpnicfIpxStatPitchs=_HpnicfIpxStatPitchs_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,2),_HpnicfIpxStatPitchs_Type())
hpnicfIpxStatPitchs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatPitchs.setStatus(_A)
_HpnicfIpxStatLenErrors_Type=Counter32
_HpnicfIpxStatLenErrors_Object=MibScalar
hpnicfIpxStatLenErrors=_HpnicfIpxStatLenErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,3),_HpnicfIpxStatLenErrors_Type())
hpnicfIpxStatLenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatLenErrors.setStatus(_A)
_HpnicfIpxStatFormatErrors_Type=Counter32
_HpnicfIpxStatFormatErrors_Object=MibScalar
hpnicfIpxStatFormatErrors=_HpnicfIpxStatFormatErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,4),_HpnicfIpxStatFormatErrors_Type())
hpnicfIpxStatFormatErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatFormatErrors.setStatus(_A)
_HpnicfIpxStatBadHops_Type=Counter32
_HpnicfIpxStatBadHops_Object=MibScalar
hpnicfIpxStatBadHops=_HpnicfIpxStatBadHops_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,5),_HpnicfIpxStatBadHops_Type())
hpnicfIpxStatBadHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatBadHops.setStatus(_A)
_HpnicfIpxStatHopsDiscards_Type=Counter32
_HpnicfIpxStatHopsDiscards_Object=MibScalar
hpnicfIpxStatHopsDiscards=_HpnicfIpxStatHopsDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,6),_HpnicfIpxStatHopsDiscards_Type())
hpnicfIpxStatHopsDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatHopsDiscards.setStatus(_A)
_HpnicfIpxStatOtherErrors_Type=Counter32
_HpnicfIpxStatOtherErrors_Object=MibScalar
hpnicfIpxStatOtherErrors=_HpnicfIpxStatOtherErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,7),_HpnicfIpxStatOtherErrors_Type())
hpnicfIpxStatOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatOtherErrors.setStatus(_A)
_HpnicfIpxStatLocalDests_Type=Counter32
_HpnicfIpxStatLocalDests_Object=MibScalar
hpnicfIpxStatLocalDests=_HpnicfIpxStatLocalDests_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,8),_HpnicfIpxStatLocalDests_Type())
hpnicfIpxStatLocalDests.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatLocalDests.setStatus(_A)
_HpnicfIpxStatCantDeals_Type=Counter32
_HpnicfIpxStatCantDeals_Object=MibScalar
hpnicfIpxStatCantDeals=_HpnicfIpxStatCantDeals_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,9),_HpnicfIpxStatCantDeals_Type())
hpnicfIpxStatCantDeals.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatCantDeals.setStatus(_A)
_HpnicfIpxStatForwards_Type=Counter32
_HpnicfIpxStatForwards_Object=MibScalar
hpnicfIpxStatForwards=_HpnicfIpxStatForwards_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,10),_HpnicfIpxStatForwards_Type())
hpnicfIpxStatForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatForwards.setStatus(_A)
_HpnicfIpxStatGenerates_Type=Counter32
_HpnicfIpxStatGenerates_Object=MibScalar
hpnicfIpxStatGenerates=_HpnicfIpxStatGenerates_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,11),_HpnicfIpxStatGenerates_Type())
hpnicfIpxStatGenerates.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatGenerates.setStatus(_A)
_HpnicfIpxStatNoRoutes_Type=Counter32
_HpnicfIpxStatNoRoutes_Object=MibScalar
hpnicfIpxStatNoRoutes=_HpnicfIpxStatNoRoutes_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,12),_HpnicfIpxStatNoRoutes_Type())
hpnicfIpxStatNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatNoRoutes.setStatus(_A)
_HpnicfIpxStatOutDiscards_Type=Counter32
_HpnicfIpxStatOutDiscards_Object=MibScalar
hpnicfIpxStatOutDiscards=_HpnicfIpxStatOutDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,13),_HpnicfIpxStatOutDiscards_Type())
hpnicfIpxStatOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatOutDiscards.setStatus(_A)
_HpnicfIpxStatRipSends_Type=Counter32
_HpnicfIpxStatRipSends_Object=MibScalar
hpnicfIpxStatRipSends=_HpnicfIpxStatRipSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,14),_HpnicfIpxStatRipSends_Type())
hpnicfIpxStatRipSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipSends.setStatus(_A)
_HpnicfIpxStatRipReceives_Type=Counter32
_HpnicfIpxStatRipReceives_Object=MibScalar
hpnicfIpxStatRipReceives=_HpnicfIpxStatRipReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,15),_HpnicfIpxStatRipReceives_Type())
hpnicfIpxStatRipReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipReceives.setStatus(_A)
_HpnicfIpxStaRipRspSends_Type=Counter32
_HpnicfIpxStaRipRspSends_Object=MibScalar
hpnicfIpxStaRipRspSends=_HpnicfIpxStaRipRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,16),_HpnicfIpxStaRipRspSends_Type())
hpnicfIpxStaRipRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStaRipRspSends.setStatus(_A)
_HpnicfIpxStaRipRspReceives_Type=Counter32
_HpnicfIpxStaRipRspReceives_Object=MibScalar
hpnicfIpxStaRipRspReceives=_HpnicfIpxStaRipRspReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,17),_HpnicfIpxStaRipRspReceives_Type())
hpnicfIpxStaRipRspReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStaRipRspReceives.setStatus(_A)
_HpnicfIpxStatRipReqReceives_Type=Counter32
_HpnicfIpxStatRipReqReceives_Object=MibScalar
hpnicfIpxStatRipReqReceives=_HpnicfIpxStatRipReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,18),_HpnicfIpxStatRipReqReceives_Type())
hpnicfIpxStatRipReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipReqReceives.setStatus(_A)
_HpnicfIpxStatRipReqDeals_Type=Counter32
_HpnicfIpxStatRipReqDeals_Object=MibScalar
hpnicfIpxStatRipReqDeals=_HpnicfIpxStatRipReqDeals_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,19),_HpnicfIpxStatRipReqDeals_Type())
hpnicfIpxStatRipReqDeals.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipReqDeals.setStatus(_A)
_HpnicfIpxStatRipReqSends_Type=Counter32
_HpnicfIpxStatRipReqSends_Object=MibScalar
hpnicfIpxStatRipReqSends=_HpnicfIpxStatRipReqSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,20),_HpnicfIpxStatRipReqSends_Type())
hpnicfIpxStatRipReqSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipReqSends.setStatus(_A)
_HpnicfIpxStatRipPeriUpdates_Type=Counter32
_HpnicfIpxStatRipPeriUpdates_Object=MibScalar
hpnicfIpxStatRipPeriUpdates=_HpnicfIpxStatRipPeriUpdates_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,21),_HpnicfIpxStatRipPeriUpdates_Type())
hpnicfIpxStatRipPeriUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatRipPeriUpdates.setStatus(_A)
_HpnicfIpxStatSapGenReqReceives_Type=Counter32
_HpnicfIpxStatSapGenReqReceives_Object=MibScalar
hpnicfIpxStatSapGenReqReceives=_HpnicfIpxStatSapGenReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,22),_HpnicfIpxStatSapGenReqReceives_Type())
hpnicfIpxStatSapGenReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapGenReqReceives.setStatus(_A)
_HpnicfIpxStatSapSpecReqReceives_Type=Counter32
_HpnicfIpxStatSapSpecReqReceives_Object=MibScalar
hpnicfIpxStatSapSpecReqReceives=_HpnicfIpxStatSapSpecReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,23),_HpnicfIpxStatSapSpecReqReceives_Type())
hpnicfIpxStatSapSpecReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapSpecReqReceives.setStatus(_A)
_HpnicfIpxStatSapGnsReqReceives_Type=Counter32
_HpnicfIpxStatSapGnsReqReceives_Object=MibScalar
hpnicfIpxStatSapGnsReqReceives=_HpnicfIpxStatSapGnsReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,24),_HpnicfIpxStatSapGnsReqReceives_Type())
hpnicfIpxStatSapGnsReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapGnsReqReceives.setStatus(_A)
_HpnicfIpxStatSapGenRspSends_Type=Counter32
_HpnicfIpxStatSapGenRspSends_Object=MibScalar
hpnicfIpxStatSapGenRspSends=_HpnicfIpxStatSapGenRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,25),_HpnicfIpxStatSapGenRspSends_Type())
hpnicfIpxStatSapGenRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapGenRspSends.setStatus(_A)
_HpnicfIpxStatSapSpecRspSends_Type=Counter32
_HpnicfIpxStatSapSpecRspSends_Object=MibScalar
hpnicfIpxStatSapSpecRspSends=_HpnicfIpxStatSapSpecRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,26),_HpnicfIpxStatSapSpecRspSends_Type())
hpnicfIpxStatSapSpecRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapSpecRspSends.setStatus(_A)
_HpnicfIpxStatSapGnsRspSends_Type=Counter32
_HpnicfIpxStatSapGnsRspSends_Object=MibScalar
hpnicfIpxStatSapGnsRspSends=_HpnicfIpxStatSapGnsRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,27),_HpnicfIpxStatSapGnsRspSends_Type())
hpnicfIpxStatSapGnsRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapGnsRspSends.setStatus(_A)
_HpnicfIpxStatSapPeriUpdates_Type=Counter32
_HpnicfIpxStatSapPeriUpdates_Object=MibScalar
hpnicfIpxStatSapPeriUpdates=_HpnicfIpxStatSapPeriUpdates_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,28),_HpnicfIpxStatSapPeriUpdates_Type())
hpnicfIpxStatSapPeriUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapPeriUpdates.setStatus(_A)
_HpnicfIpxStatSapInPktErrors_Type=Counter32
_HpnicfIpxStatSapInPktErrors_Object=MibScalar
hpnicfIpxStatSapInPktErrors=_HpnicfIpxStatSapInPktErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,1,29),_HpnicfIpxStatSapInPktErrors_Type())
hpnicfIpxStatSapInPktErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxStatSapInPktErrors.setStatus(_A)
_HpnicfIpxStatInterface_ObjectIdentity=ObjectIdentity
hpnicfIpxStatInterface=_HpnicfIpxStatInterface_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2))
_HpnicfIpxIfStatTable_Object=MibTable
hpnicfIpxIfStatTable=_HpnicfIpxIfStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1))
if mibBuilder.loadTexts:hpnicfIpxIfStatTable.setStatus(_A)
_HpnicfIpxIfStatEntry_Object=MibTableRow
hpnicfIpxIfStatEntry=_HpnicfIpxIfStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1))
hpnicfIpxIfStatEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:hpnicfIpxIfStatEntry.setStatus(_A)
class _HpnicfIpxIfStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpxIfStatIndex_Type.__name__=_C
_HpnicfIpxIfStatIndex_Object=MibTableColumn
hpnicfIpxIfStatIndex=_HpnicfIpxIfStatIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,1),_HpnicfIpxIfStatIndex_Type())
hpnicfIpxIfStatIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfIpxIfStatIndex.setStatus(_A)
class _HpnicfIpxIfStatNetId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpxIfStatNetId_Type.__name__=_E
_HpnicfIpxIfStatNetId_Object=MibTableColumn
hpnicfIpxIfStatNetId=_HpnicfIpxIfStatNetId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,2),_HpnicfIpxIfStatNetId_Type())
hpnicfIpxIfStatNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatNetId.setStatus(_A)
class _HpnicfIpxIfStatNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnicfIpxIfStatNodeId_Type.__name__=_E
_HpnicfIpxIfStatNodeId_Object=MibTableColumn
hpnicfIpxIfStatNodeId=_HpnicfIpxIfStatNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,3),_HpnicfIpxIfStatNodeId_Type())
hpnicfIpxIfStatNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatNodeId.setStatus(_A)
_HpnicfIpxIfStatIpxReceives_Type=Counter32
_HpnicfIpxIfStatIpxReceives_Object=MibTableColumn
hpnicfIpxIfStatIpxReceives=_HpnicfIpxIfStatIpxReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,4),_HpnicfIpxIfStatIpxReceives_Type())
hpnicfIpxIfStatIpxReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatIpxReceives.setStatus(_A)
_HpnicfIpxIfStatIpxSends_Type=Counter32
_HpnicfIpxIfStatIpxSends_Object=MibTableColumn
hpnicfIpxIfStatIpxSends=_HpnicfIpxIfStatIpxSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,5),_HpnicfIpxIfStatIpxSends_Type())
hpnicfIpxIfStatIpxSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatIpxSends.setStatus(_A)
_HpnicfIpxIfStatIpxRecvBytes_Type=Counter32
_HpnicfIpxIfStatIpxRecvBytes_Object=MibTableColumn
hpnicfIpxIfStatIpxRecvBytes=_HpnicfIpxIfStatIpxRecvBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,6),_HpnicfIpxIfStatIpxRecvBytes_Type())
hpnicfIpxIfStatIpxRecvBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatIpxRecvBytes.setStatus(_A)
_HpnicfIpxIfStatIpxSendBytes_Type=Counter32
_HpnicfIpxIfStatIpxSendBytes_Object=MibTableColumn
hpnicfIpxIfStatIpxSendBytes=_HpnicfIpxIfStatIpxSendBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,7),_HpnicfIpxIfStatIpxSendBytes_Type())
hpnicfIpxIfStatIpxSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatIpxSendBytes.setStatus(_A)
_HpnicfIpxIfStatRipReceives_Type=Counter32
_HpnicfIpxIfStatRipReceives_Object=MibTableColumn
hpnicfIpxIfStatRipReceives=_HpnicfIpxIfStatRipReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,8),_HpnicfIpxIfStatRipReceives_Type())
hpnicfIpxIfStatRipReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipReceives.setStatus(_A)
_HpnicfIpxIfStatRipSends_Type=Counter32
_HpnicfIpxIfStatRipSends_Object=MibTableColumn
hpnicfIpxIfStatRipSends=_HpnicfIpxIfStatRipSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,9),_HpnicfIpxIfStatRipSends_Type())
hpnicfIpxIfStatRipSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipSends.setStatus(_A)
_HpnicfIpxIfStatRipDiscards_Type=Counter32
_HpnicfIpxIfStatRipDiscards_Object=MibTableColumn
hpnicfIpxIfStatRipDiscards=_HpnicfIpxIfStatRipDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,10),_HpnicfIpxIfStatRipDiscards_Type())
hpnicfIpxIfStatRipDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipDiscards.setStatus(_A)
_HpnicfIpxIfStatRipSpecReqReceives_Type=Counter32
_HpnicfIpxIfStatRipSpecReqReceives_Object=MibTableColumn
hpnicfIpxIfStatRipSpecReqReceives=_HpnicfIpxIfStatRipSpecReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,11),_HpnicfIpxIfStatRipSpecReqReceives_Type())
hpnicfIpxIfStatRipSpecReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipSpecReqReceives.setStatus(_A)
_HpnicfIpxIfStatRipSpecRspSends_Type=Counter32
_HpnicfIpxIfStatRipSpecRspSends_Object=MibTableColumn
hpnicfIpxIfStatRipSpecRspSends=_HpnicfIpxIfStatRipSpecRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,12),_HpnicfIpxIfStatRipSpecRspSends_Type())
hpnicfIpxIfStatRipSpecRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipSpecRspSends.setStatus(_A)
_HpnicfIpxIfStatRipGenReqReceives_Type=Counter32
_HpnicfIpxIfStatRipGenReqReceives_Object=MibTableColumn
hpnicfIpxIfStatRipGenReqReceives=_HpnicfIpxIfStatRipGenReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,13),_HpnicfIpxIfStatRipGenReqReceives_Type())
hpnicfIpxIfStatRipGenReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipGenReqReceives.setStatus(_A)
_HpnicfIpxIfStatRipGenRspSends_Type=Counter32
_HpnicfIpxIfStatRipGenRspSends_Object=MibTableColumn
hpnicfIpxIfStatRipGenRspSends=_HpnicfIpxIfStatRipGenRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,14),_HpnicfIpxIfStatRipGenRspSends_Type())
hpnicfIpxIfStatRipGenRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatRipGenRspSends.setStatus(_A)
_HpnicfIpxIfStatSapReceives_Type=Counter32
_HpnicfIpxIfStatSapReceives_Object=MibTableColumn
hpnicfIpxIfStatSapReceives=_HpnicfIpxIfStatSapReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,15),_HpnicfIpxIfStatSapReceives_Type())
hpnicfIpxIfStatSapReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatSapReceives.setStatus(_A)
_HpnicfIpxIfStatSapSends_Type=Counter32
_HpnicfIpxIfStatSapSends_Object=MibTableColumn
hpnicfIpxIfStatSapSends=_HpnicfIpxIfStatSapSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,16),_HpnicfIpxIfStatSapSends_Type())
hpnicfIpxIfStatSapSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatSapSends.setStatus(_A)
_HpnicfIpxIfStatSapDiscards_Type=Counter32
_HpnicfIpxIfStatSapDiscards_Object=MibTableColumn
hpnicfIpxIfStatSapDiscards=_HpnicfIpxIfStatSapDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,17),_HpnicfIpxIfStatSapDiscards_Type())
hpnicfIpxIfStatSapDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatSapDiscards.setStatus(_A)
_HpnicfIpxIfStatSapGnsReqReceives_Type=Counter32
_HpnicfIpxIfStatSapGnsReqReceives_Object=MibTableColumn
hpnicfIpxIfStatSapGnsReqReceives=_HpnicfIpxIfStatSapGnsReqReceives_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,18),_HpnicfIpxIfStatSapGnsReqReceives_Type())
hpnicfIpxIfStatSapGnsReqReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatSapGnsReqReceives.setStatus(_A)
_HpnicfIpxIfStatSapGnsRspSends_Type=Counter32
_HpnicfIpxIfStatSapGnsRspSends_Object=MibTableColumn
hpnicfIpxIfStatSapGnsRspSends=_HpnicfIpxIfStatSapGnsRspSends_Object((1,3,6,1,4,1,11,2,14,11,15,2,34,4,2,1,1,19),_HpnicfIpxIfStatSapGnsRspSends_Type())
hpnicfIpxIfStatSapGnsRspSends.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpxIfStatSapGnsRspSends.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_I:EnabledStatus,'hpnicfIpx':hpnicfIpx,'hpnicfIpxConfig':hpnicfIpxConfig,'hpnicfIpxStatus':hpnicfIpxStatus,'hpnicfIpxIfConfigTable':hpnicfIpxIfConfigTable,'hpnicfIpxIfConfigEntry':hpnicfIpxIfConfigEntry,_J:hpnicfIpxIfIndex,'hpnicfIpxIfNetId':hpnicfIpxIfNetId,'hpnicfIpxIfNodeId':hpnicfIpxIfNodeId,'hpnicfIpxIfSplitHorizon':hpnicfIpxIfSplitHorizon,'hpnicfIPxIfTick':hpnicfIPxIfTick,'hpnicfIpxIfUpdateChangeOnly':hpnicfIpxIfUpdateChangeOnly,'hpnicfIpxIfRipMtu':hpnicfIpxIfRipMtu,'hpnicfIpxIfEncapsuleType':hpnicfIpxIfEncapsuleType,'hpnicfIpxIfNetbiosPropagation':hpnicfIpxIfNetbiosPropagation,'hpnicfIpxIfSapStatus':hpnicfIpxIfSapStatus,'hpnicfIpxIfSapMtu':hpnicfIpxIfSapMtu,'hpnicfIpxIfGnsReply':hpnicfIpxIfGnsReply,'hpnicfIpxIfRowStatus':hpnicfIpxIfRowStatus,'hpnicfIpxRip':hpnicfIpxRip,'hpnicfIpxRouteMultiplier':hpnicfIpxRouteMultiplier,'hpnicfIpxRouteUpdateTimer':hpnicfIpxRouteUpdateTimer,'hpnicfIpxRouteImpRouteStatic':hpnicfIpxRouteImpRouteStatic,'hpnicfIpxRouteLoadBalancePaths':hpnicfIpxRouteLoadBalancePaths,'hpnicfIpxRouteMaxResPaths':hpnicfIpxRouteMaxResPaths,'hpnicfIpxRouteTable':hpnicfIpxRouteTable,'hpnicfIpxRouteEntry':hpnicfIpxRouteEntry,_K:hpnicfIpxRouteIndex,'hpnicfIpxRouteDestNetId':hpnicfIpxRouteDestNetId,'hpnicfIpxRouteNextHop':hpnicfIpxRouteNextHop,'hpnicfIpxRoutePro':hpnicfIpxRoutePro,'hpnicfIpxRoutePre':hpnicfIpxRoutePre,'hpnicfIpxRouteTicks':hpnicfIpxRouteTicks,'hpnicfIpxRouteHops':hpnicfIpxRouteHops,'hpnicfIpxRouteTime':hpnicfIpxRouteTime,'hpnicfIpxRouteOutInterface':hpnicfIpxRouteOutInterface,'hpnicfIpxStaticRouteTable':hpnicfIpxStaticRouteTable,'hpnicfIpxStaticRouteEntry':hpnicfIpxStaticRouteEntry,_M:hpnicfIpxStaticRouteDestNetId,_N:hpnicfIpxStaticRouteNextHop,'hpnicfIpxStaticRoutePre':hpnicfIpxStaticRoutePre,'hpnicfIpxStaticRouteOutIf':hpnicfIpxStaticRouteOutIf,'hpnicfIpxStaticRouteTicks':hpnicfIpxStaticRouteTicks,'hpnicfIpxStaticRouteHops':hpnicfIpxStaticRouteHops,'hpnicfIpxStaticRouteStatus':hpnicfIpxStaticRouteStatus,'hpnicfIpxStaticRouteRowStatus':hpnicfIpxStaticRouteRowStatus,'hpnicfIpxRouteStatTable':hpnicfIpxRouteStatTable,'hpnicfIpxRouteStatEntry':hpnicfIpxRouteStatEntry,_Q:hpnicfIpxRouteStatPro,'hpnicfIpxRouteStatRoutes':hpnicfIpxRouteStatRoutes,'hpnicfIpxRouteStatActives':hpnicfIpxRouteStatActives,'hpnicfIpxRouteStatAddeds':hpnicfIpxRouteStatAddeds,'hpnicfIpxRouteStatDeleteds':hpnicfIpxRouteStatDeleteds,'hpnicfIpxRouteStatFreeds':hpnicfIpxRouteStatFreeds,'hpnicfIpxSap':hpnicfIpxSap,'hpnicfIpxSapMultiplier':hpnicfIpxSapMultiplier,'hpnicfIpxSapUpdateTimer':hpnicfIpxSapUpdateTimer,'hpnicfIpxSapGnsLoadBalance':hpnicfIpxSapGnsLoadBalance,'hpnicfIpxSapMaxResServers':hpnicfIpxSapMaxResServers,'hpnicfIpxServiceTable':hpnicfIpxServiceTable,'hpnicfIpxServiceEntry':hpnicfIpxServiceEntry,_R:hpnicfIpxServiceIndex,'hpnicfIpxServiceName':hpnicfIpxServiceName,'hpnicfIpxServiceType':hpnicfIpxServiceType,'hpnicfIpxServiceNetId':hpnicfIpxServiceNetId,'hpnicfIpxServiceNodeId':hpnicfIpxServiceNodeId,'hpnicfIpxServiceSocketNo':hpnicfIpxServiceSocketNo,'hpnicfIpxServicePreference':hpnicfIpxServicePreference,'hpnicfIpxServiceHops':hpnicfIpxServiceHops,'hpnicfIpxServiceRecvIf':hpnicfIpxServiceRecvIf,'hpnicfIpxStaticServiceTable':hpnicfIpxStaticServiceTable,'hpnicfIpxStaticServiceEntry':hpnicfIpxStaticServiceEntry,_S:hpnicfIpxStaticServiceType,_T:hpnicfIpxStaticServiceName,_U:hpnicfIpxStaticServiceNetId,'hpnicfIpxStaticServiceNodeId':hpnicfIpxStaticServiceNodeId,'hpnicfIpxStatciServiceSocketNo':hpnicfIpxStatciServiceSocketNo,'hpnicfIpxStaticServicePreference':hpnicfIpxStaticServicePreference,'hpnicfIpxStaticServiceHops':hpnicfIpxStaticServiceHops,'hpnicfIpxStaticServiceStatus':hpnicfIpxStaticServiceStatus,'hpnicfIpxStaticServiceRowStatus':hpnicfIpxStaticServiceRowStatus,'hpnicfIpxStat':hpnicfIpxStat,'hpnicfIpxStatGlobal':hpnicfIpxStatGlobal,'hpnicfIpxStatTotalReceives':hpnicfIpxStatTotalReceives,'hpnicfIpxStatPitchs':hpnicfIpxStatPitchs,'hpnicfIpxStatLenErrors':hpnicfIpxStatLenErrors,'hpnicfIpxStatFormatErrors':hpnicfIpxStatFormatErrors,'hpnicfIpxStatBadHops':hpnicfIpxStatBadHops,'hpnicfIpxStatHopsDiscards':hpnicfIpxStatHopsDiscards,'hpnicfIpxStatOtherErrors':hpnicfIpxStatOtherErrors,'hpnicfIpxStatLocalDests':hpnicfIpxStatLocalDests,'hpnicfIpxStatCantDeals':hpnicfIpxStatCantDeals,'hpnicfIpxStatForwards':hpnicfIpxStatForwards,'hpnicfIpxStatGenerates':hpnicfIpxStatGenerates,'hpnicfIpxStatNoRoutes':hpnicfIpxStatNoRoutes,'hpnicfIpxStatOutDiscards':hpnicfIpxStatOutDiscards,'hpnicfIpxStatRipSends':hpnicfIpxStatRipSends,'hpnicfIpxStatRipReceives':hpnicfIpxStatRipReceives,'hpnicfIpxStaRipRspSends':hpnicfIpxStaRipRspSends,'hpnicfIpxStaRipRspReceives':hpnicfIpxStaRipRspReceives,'hpnicfIpxStatRipReqReceives':hpnicfIpxStatRipReqReceives,'hpnicfIpxStatRipReqDeals':hpnicfIpxStatRipReqDeals,'hpnicfIpxStatRipReqSends':hpnicfIpxStatRipReqSends,'hpnicfIpxStatRipPeriUpdates':hpnicfIpxStatRipPeriUpdates,'hpnicfIpxStatSapGenReqReceives':hpnicfIpxStatSapGenReqReceives,'hpnicfIpxStatSapSpecReqReceives':hpnicfIpxStatSapSpecReqReceives,'hpnicfIpxStatSapGnsReqReceives':hpnicfIpxStatSapGnsReqReceives,'hpnicfIpxStatSapGenRspSends':hpnicfIpxStatSapGenRspSends,'hpnicfIpxStatSapSpecRspSends':hpnicfIpxStatSapSpecRspSends,'hpnicfIpxStatSapGnsRspSends':hpnicfIpxStatSapGnsRspSends,'hpnicfIpxStatSapPeriUpdates':hpnicfIpxStatSapPeriUpdates,'hpnicfIpxStatSapInPktErrors':hpnicfIpxStatSapInPktErrors,'hpnicfIpxStatInterface':hpnicfIpxStatInterface,'hpnicfIpxIfStatTable':hpnicfIpxIfStatTable,'hpnicfIpxIfStatEntry':hpnicfIpxIfStatEntry,_V:hpnicfIpxIfStatIndex,'hpnicfIpxIfStatNetId':hpnicfIpxIfStatNetId,'hpnicfIpxIfStatNodeId':hpnicfIpxIfStatNodeId,'hpnicfIpxIfStatIpxReceives':hpnicfIpxIfStatIpxReceives,'hpnicfIpxIfStatIpxSends':hpnicfIpxIfStatIpxSends,'hpnicfIpxIfStatIpxRecvBytes':hpnicfIpxIfStatIpxRecvBytes,'hpnicfIpxIfStatIpxSendBytes':hpnicfIpxIfStatIpxSendBytes,'hpnicfIpxIfStatRipReceives':hpnicfIpxIfStatRipReceives,'hpnicfIpxIfStatRipSends':hpnicfIpxIfStatRipSends,'hpnicfIpxIfStatRipDiscards':hpnicfIpxIfStatRipDiscards,'hpnicfIpxIfStatRipSpecReqReceives':hpnicfIpxIfStatRipSpecReqReceives,'hpnicfIpxIfStatRipSpecRspSends':hpnicfIpxIfStatRipSpecRspSends,'hpnicfIpxIfStatRipGenReqReceives':hpnicfIpxIfStatRipGenReqReceives,'hpnicfIpxIfStatRipGenRspSends':hpnicfIpxIfStatRipGenRspSends,'hpnicfIpxIfStatSapReceives':hpnicfIpxIfStatSapReceives,'hpnicfIpxIfStatSapSends':hpnicfIpxIfStatSapSends,'hpnicfIpxIfStatSapDiscards':hpnicfIpxIfStatSapDiscards,'hpnicfIpxIfStatSapGnsReqReceives':hpnicfIpxIfStatSapGnsReqReceives,'hpnicfIpxIfStatSapGnsRspSends':hpnicfIpxIfStatSapGnsRspSends})