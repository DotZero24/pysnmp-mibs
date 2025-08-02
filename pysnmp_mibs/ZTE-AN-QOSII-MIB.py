_x='zxAnQosIIMVlan2CosMVlanValue'
_w='read-only'
_v='zxAnQosIITrafficDirection'
_u='zxAnQosIITrafficLogicalId'
_t='zxAnQosIITrafficVCircuitType'
_s='zxAnQosIITrafficOnu'
_r='zxAnQosIITrafficPort'
_q='zxAnQosIITrafficSlot'
_p='zxAnQosIITrafficShelf'
_o='zxAnQosIITrafficRack'
_n='serviceport'
_m='epononu'
_l='bridgeport'
_k='physicalport'
_j='zxAnQosIILogicalId'
_i='zxAnQosIIVCircuitType'
_h='zxAnQosIIOnu'
_g='zxAnQosIIPort'
_f='zxAnQosIISlot'
_e='zxAnQosIIShelf'
_d='zxAnQosIIRack'
_c='trustCosMap'
_b='zxAnQosIIVPortPrfName'
_a='kbytes'
_Z='zxAnQosIITrafficPrfName'
_Y='zxAnQosIICosRemarkPrfName'
_X='zxAnQosIIQueuesBlockPrfName'
_W='zxAnQosIICos2QueuesPrfName'
_V='zxAnQosIIDscp2CosDscpValue'
_U='zxAnQosIICos2DscpCosValue'
_T='zxAnQosIINniIngressDscp'
_S='trustDscpMap'
_R='remark'
_Q='override'
_P='disable'
_O='enable'
_N='OctetString'
_M='notSupport'
_L='ifIndex'
_K='IF-MIB'
_J='trust'
_I='notsupport'
_H='read-write'
_G='kbps'
_F='DisplayString'
_E='not-accessible'
_D='ZTE-AN-QOSII-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnQosMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,21))
_ZxAnQosIIObjects_ObjectIdentity=ObjectIdentity
zxAnQosIIObjects=_ZxAnQosIIObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,3))
class _ZxAnQosIINniCos2DropMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosIINniCos2DropMap_Type.__name__=_N
_ZxAnQosIINniCos2DropMap_Object=MibScalar
zxAnQosIINniCos2DropMap=_ZxAnQosIINniCos2DropMap_Object((1,3,6,1,4,1,3902,1015,21,3,1),_ZxAnQosIINniCos2DropMap_Type())
zxAnQosIINniCos2DropMap.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIINniCos2DropMap.setStatus(_A)
class _ZxAnQosIINniCos2LocalMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosIINniCos2LocalMap_Type.__name__=_N
_ZxAnQosIINniCos2LocalMap_Object=MibScalar
zxAnQosIINniCos2LocalMap=_ZxAnQosIINniCos2LocalMap_Object((1,3,6,1,4,1,3902,1015,21,3,2),_ZxAnQosIINniCos2LocalMap_Type())
zxAnQosIINniCos2LocalMap.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIINniCos2LocalMap.setStatus(_A)
_ZxAnQosIINniDscpMappingTable_Object=MibTable
zxAnQosIINniDscpMappingTable=_ZxAnQosIINniDscpMappingTable_Object((1,3,6,1,4,1,3902,1015,21,3,3))
if mibBuilder.loadTexts:zxAnQosIINniDscpMappingTable.setStatus(_A)
_ZxAnQosIINniDscpMappingEntry_Object=MibTableRow
zxAnQosIINniDscpMappingEntry=_ZxAnQosIINniDscpMappingEntry_Object((1,3,6,1,4,1,3902,1015,21,3,3,1))
zxAnQosIINniDscpMappingEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:zxAnQosIINniDscpMappingEntry.setStatus(_A)
class _ZxAnQosIINniIngressDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosIINniIngressDscp_Type.__name__=_C
_ZxAnQosIINniIngressDscp_Object=MibTableColumn
zxAnQosIINniIngressDscp=_ZxAnQosIINniIngressDscp_Object((1,3,6,1,4,1,3902,1015,21,3,3,1,1),_ZxAnQosIINniIngressDscp_Type())
zxAnQosIINniIngressDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIINniIngressDscp.setStatus(_A)
class _ZxAnQosIINniEgressDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosIINniEgressDscp_Type.__name__=_C
_ZxAnQosIINniEgressDscp_Object=MibTableColumn
zxAnQosIINniEgressDscp=_ZxAnQosIINniEgressDscp_Object((1,3,6,1,4,1,3902,1015,21,3,3,1,2),_ZxAnQosIINniEgressDscp_Type())
zxAnQosIINniEgressDscp.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIINniEgressDscp.setStatus(_A)
class _ZxAnQosIINniEgressCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIINniEgressCos_Type.__name__=_C
_ZxAnQosIINniEgressCos_Object=MibTableColumn
zxAnQosIINniEgressCos=_ZxAnQosIINniEgressCos_Object((1,3,6,1,4,1,3902,1015,21,3,3,1,3),_ZxAnQosIINniEgressCos_Type())
zxAnQosIINniEgressCos.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIINniEgressCos.setStatus(_A)
class _ZxAnQosIINniEgressDropPrecedence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_ZxAnQosIINniEgressDropPrecedence_Type.__name__=_C
_ZxAnQosIINniEgressDropPrecedence_Object=MibTableColumn
zxAnQosIINniEgressDropPrecedence=_ZxAnQosIINniEgressDropPrecedence_Object((1,3,6,1,4,1,3902,1015,21,3,3,1,4),_ZxAnQosIINniEgressDropPrecedence_Type())
zxAnQosIINniEgressDropPrecedence.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIINniEgressDropPrecedence.setStatus(_A)
_ZxAnQosIINniPortCfgTable_Object=MibTable
zxAnQosIINniPortCfgTable=_ZxAnQosIINniPortCfgTable_Object((1,3,6,1,4,1,3902,1015,21,3,4))
if mibBuilder.loadTexts:zxAnQosIINniPortCfgTable.setStatus(_A)
_ZxAnQosIINniPortCfgEntry_Object=MibTableRow
zxAnQosIINniPortCfgEntry=_ZxAnQosIINniPortCfgEntry_Object((1,3,6,1,4,1,3902,1015,21,3,4,1))
zxAnQosIINniPortCfgEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:zxAnQosIINniPortCfgEntry.setStatus(_A)
class _ZxAnQosIINniDefPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIINniDefPriority_Type.__name__=_C
_ZxAnQosIINniDefPriority_Object=MibTableColumn
zxAnQosIINniDefPriority=_ZxAnQosIINniDefPriority_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,1),_ZxAnQosIINniDefPriority_Type())
zxAnQosIINniDefPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniDefPriority.setStatus(_A)
class _ZxAnQosIINniTrustDscp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_P,2),(_I,255)))
_ZxAnQosIINniTrustDscp_Type.__name__=_C
_ZxAnQosIINniTrustDscp_Object=MibTableColumn
zxAnQosIINniTrustDscp=_ZxAnQosIINniTrustDscp_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,2),_ZxAnQosIINniTrustDscp_Type())
zxAnQosIINniTrustDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniTrustDscp.setStatus(_A)
class _ZxAnQosIINniTrustCos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_O,1),(_P,2),(_I,255)))
_ZxAnQosIINniTrustCos_Type.__name__=_C
_ZxAnQosIINniTrustCos_Object=MibTableColumn
zxAnQosIINniTrustCos=_ZxAnQosIINniTrustCos_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,3),_ZxAnQosIINniTrustCos_Type())
zxAnQosIINniTrustCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniTrustCos.setStatus(_A)
class _ZxAnQosIINniQueuesAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr',2),('fq',3)))
_ZxAnQosIINniQueuesAlgorithm_Type.__name__=_C
_ZxAnQosIINniQueuesAlgorithm_Object=MibTableColumn
zxAnQosIINniQueuesAlgorithm=_ZxAnQosIINniQueuesAlgorithm_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,4),_ZxAnQosIINniQueuesAlgorithm_Type())
zxAnQosIINniQueuesAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniQueuesAlgorithm.setStatus(_A)
_ZxAnQosIINniQueuesWeight_Type=ObjectIdentifier
_ZxAnQosIINniQueuesWeight_Object=MibTableColumn
zxAnQosIINniQueuesWeight=_ZxAnQosIINniQueuesWeight_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,5),_ZxAnQosIINniQueuesWeight_Type())
zxAnQosIINniQueuesWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniQueuesWeight.setStatus(_A)
_ZxAnQosIINniQueuesMinRate_Type=ObjectIdentifier
_ZxAnQosIINniQueuesMinRate_Object=MibTableColumn
zxAnQosIINniQueuesMinRate=_ZxAnQosIINniQueuesMinRate_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,6),_ZxAnQosIINniQueuesMinRate_Type())
zxAnQosIINniQueuesMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniQueuesMinRate.setStatus(_A)
_ZxAnQosIINniQueuesMaxRate_Type=ObjectIdentifier
_ZxAnQosIINniQueuesMaxRate_Object=MibTableColumn
zxAnQosIINniQueuesMaxRate=_ZxAnQosIINniQueuesMaxRate_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,7),_ZxAnQosIINniQueuesMaxRate_Type())
zxAnQosIINniQueuesMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniQueuesMaxRate.setStatus(_A)
class _ZxAnQosIINniShapeRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,1000000))
_ZxAnQosIINniShapeRateLimit_Type.__name__=_C
_ZxAnQosIINniShapeRateLimit_Object=MibTableColumn
zxAnQosIINniShapeRateLimit=_ZxAnQosIINniShapeRateLimit_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,8),_ZxAnQosIINniShapeRateLimit_Type())
zxAnQosIINniShapeRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniShapeRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIINniShapeRateLimit.setUnits(_G)
class _ZxAnQosIINniShapeBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,16000))
_ZxAnQosIINniShapeBurstSize_Type.__name__=_C
_ZxAnQosIINniShapeBurstSize_Object=MibTableColumn
zxAnQosIINniShapeBurstSize=_ZxAnQosIINniShapeBurstSize_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,9),_ZxAnQosIINniShapeBurstSize_Type())
zxAnQosIINniShapeBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniShapeBurstSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIINniShapeBurstSize.setUnits(_G)
_ZxAnQosIINniQueuesDepth_Type=ObjectIdentifier
_ZxAnQosIINniQueuesDepth_Object=MibTableColumn
zxAnQosIINniQueuesDepth=_ZxAnQosIINniQueuesDepth_Object((1,3,6,1,4,1,3902,1015,21,3,4,1,10),_ZxAnQosIINniQueuesDepth_Type())
zxAnQosIINniQueuesDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniQueuesDepth.setStatus(_A)
_ZxAnQosIINniGlobal_ObjectIdentity=ObjectIdentity
zxAnQosIINniGlobal=_ZxAnQosIINniGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,3,5))
class _ZxAnQosIINniGlobalTrustMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('untrust',1),('trustcosonly',2),('trustdscponly',3),(_I,255)))
_ZxAnQosIINniGlobalTrustMode_Type.__name__=_C
_ZxAnQosIINniGlobalTrustMode_Object=MibScalar
zxAnQosIINniGlobalTrustMode=_ZxAnQosIINniGlobalTrustMode_Object((1,3,6,1,4,1,3902,1015,21,3,5,1),_ZxAnQosIINniGlobalTrustMode_Type())
zxAnQosIINniGlobalTrustMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIINniGlobalTrustMode.setStatus(_A)
_ZxAnQosIICos2DscpTable_Object=MibTable
zxAnQosIICos2DscpTable=_ZxAnQosIICos2DscpTable_Object((1,3,6,1,4,1,3902,1015,21,3,10))
if mibBuilder.loadTexts:zxAnQosIICos2DscpTable.setStatus(_A)
_ZxAnQosIICos2DscpEntry_Object=MibTableRow
zxAnQosIICos2DscpEntry=_ZxAnQosIICos2DscpEntry_Object((1,3,6,1,4,1,3902,1015,21,3,10,1))
zxAnQosIICos2DscpEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:zxAnQosIICos2DscpEntry.setStatus(_A)
class _ZxAnQosIICos2DscpCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIICos2DscpCosValue_Type.__name__=_C
_ZxAnQosIICos2DscpCosValue_Object=MibTableColumn
zxAnQosIICos2DscpCosValue=_ZxAnQosIICos2DscpCosValue_Object((1,3,6,1,4,1,3902,1015,21,3,10,1,1),_ZxAnQosIICos2DscpCosValue_Type())
zxAnQosIICos2DscpCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIICos2DscpCosValue.setStatus(_A)
class _ZxAnQosIICos2DscpDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosIICos2DscpDscpValue_Type.__name__=_C
_ZxAnQosIICos2DscpDscpValue_Object=MibTableColumn
zxAnQosIICos2DscpDscpValue=_ZxAnQosIICos2DscpDscpValue_Object((1,3,6,1,4,1,3902,1015,21,3,10,1,2),_ZxAnQosIICos2DscpDscpValue_Type())
zxAnQosIICos2DscpDscpValue.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIICos2DscpDscpValue.setStatus(_A)
_ZxAnQosIIDscp2CosTable_Object=MibTable
zxAnQosIIDscp2CosTable=_ZxAnQosIIDscp2CosTable_Object((1,3,6,1,4,1,3902,1015,21,3,11))
if mibBuilder.loadTexts:zxAnQosIIDscp2CosTable.setStatus(_A)
_ZxAnQosIIDscp2CosEntry_Object=MibTableRow
zxAnQosIIDscp2CosEntry=_ZxAnQosIIDscp2CosEntry_Object((1,3,6,1,4,1,3902,1015,21,3,11,1))
zxAnQosIIDscp2CosEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:zxAnQosIIDscp2CosEntry.setStatus(_A)
class _ZxAnQosIIDscp2CosDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnQosIIDscp2CosDscpValue_Type.__name__=_C
_ZxAnQosIIDscp2CosDscpValue_Object=MibTableColumn
zxAnQosIIDscp2CosDscpValue=_ZxAnQosIIDscp2CosDscpValue_Object((1,3,6,1,4,1,3902,1015,21,3,11,1,1),_ZxAnQosIIDscp2CosDscpValue_Type())
zxAnQosIIDscp2CosDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIDscp2CosDscpValue.setStatus(_A)
class _ZxAnQosIIDscp2CosCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIIDscp2CosCosValue_Type.__name__=_C
_ZxAnQosIIDscp2CosCosValue_Object=MibTableColumn
zxAnQosIIDscp2CosCosValue=_ZxAnQosIIDscp2CosCosValue_Object((1,3,6,1,4,1,3902,1015,21,3,11,1,2),_ZxAnQosIIDscp2CosCosValue_Type())
zxAnQosIIDscp2CosCosValue.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnQosIIDscp2CosCosValue.setStatus(_A)
_ZxAnQosIICos2QueuesProfileTable_Object=MibTable
zxAnQosIICos2QueuesProfileTable=_ZxAnQosIICos2QueuesProfileTable_Object((1,3,6,1,4,1,3902,1015,21,3,13))
if mibBuilder.loadTexts:zxAnQosIICos2QueuesProfileTable.setStatus(_A)
_ZxAnQosIICos2QueuesProfileEntry_Object=MibTableRow
zxAnQosIICos2QueuesProfileEntry=_ZxAnQosIICos2QueuesProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,3,13,1))
zxAnQosIICos2QueuesProfileEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:zxAnQosIICos2QueuesProfileEntry.setStatus(_A)
class _ZxAnQosIICos2QueuesPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIICos2QueuesPrfName_Type.__name__=_F
_ZxAnQosIICos2QueuesPrfName_Object=MibTableColumn
zxAnQosIICos2QueuesPrfName=_ZxAnQosIICos2QueuesPrfName_Object((1,3,6,1,4,1,3902,1015,21,3,13,1,1),_ZxAnQosIICos2QueuesPrfName_Type())
zxAnQosIICos2QueuesPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIICos2QueuesPrfName.setStatus(_A)
_ZxAnQosIICos2Queues_Type=ObjectIdentifier
_ZxAnQosIICos2Queues_Object=MibTableColumn
zxAnQosIICos2Queues=_ZxAnQosIICos2Queues_Object((1,3,6,1,4,1,3902,1015,21,3,13,1,2),_ZxAnQosIICos2Queues_Type())
zxAnQosIICos2Queues.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIICos2Queues.setStatus(_A)
_ZxAnQosIIDropPrecedence_Type=ObjectIdentifier
_ZxAnQosIIDropPrecedence_Object=MibTableColumn
zxAnQosIIDropPrecedence=_ZxAnQosIIDropPrecedence_Object((1,3,6,1,4,1,3902,1015,21,3,13,1,3),_ZxAnQosIIDropPrecedence_Type())
zxAnQosIIDropPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIDropPrecedence.setStatus(_A)
_ZxAnQosIICos2QueuesRowStatus_Type=RowStatus
_ZxAnQosIICos2QueuesRowStatus_Object=MibTableColumn
zxAnQosIICos2QueuesRowStatus=_ZxAnQosIICos2QueuesRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,13,1,20),_ZxAnQosIICos2QueuesRowStatus_Type())
zxAnQosIICos2QueuesRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIICos2QueuesRowStatus.setStatus(_A)
_ZxAnQosIIQueuesBlockProfileTable_Object=MibTable
zxAnQosIIQueuesBlockProfileTable=_ZxAnQosIIQueuesBlockProfileTable_Object((1,3,6,1,4,1,3902,1015,21,3,14))
if mibBuilder.loadTexts:zxAnQosIIQueuesBlockProfileTable.setStatus(_A)
_ZxAnQosIIQueuesBlockProfileEntry_Object=MibTableRow
zxAnQosIIQueuesBlockProfileEntry=_ZxAnQosIIQueuesBlockProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,3,14,1))
zxAnQosIIQueuesBlockProfileEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:zxAnQosIIQueuesBlockProfileEntry.setStatus(_A)
class _ZxAnQosIIQueuesBlockPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIQueuesBlockPrfName_Type.__name__=_F
_ZxAnQosIIQueuesBlockPrfName_Object=MibTableColumn
zxAnQosIIQueuesBlockPrfName=_ZxAnQosIIQueuesBlockPrfName_Object((1,3,6,1,4,1,3902,1015,21,3,14,1,1),_ZxAnQosIIQueuesBlockPrfName_Type())
zxAnQosIIQueuesBlockPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIQueuesBlockPrfName.setStatus(_A)
_ZxAnQosIIQueuesPriority_Type=ObjectIdentifier
_ZxAnQosIIQueuesPriority_Object=MibTableColumn
zxAnQosIIQueuesPriority=_ZxAnQosIIQueuesPriority_Object((1,3,6,1,4,1,3902,1015,21,3,14,1,2),_ZxAnQosIIQueuesPriority_Type())
zxAnQosIIQueuesPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIQueuesPriority.setStatus(_A)
_ZxAnQosIIQueuesWeight_Type=ObjectIdentifier
_ZxAnQosIIQueuesWeight_Object=MibTableColumn
zxAnQosIIQueuesWeight=_ZxAnQosIIQueuesWeight_Object((1,3,6,1,4,1,3902,1015,21,3,14,1,3),_ZxAnQosIIQueuesWeight_Type())
zxAnQosIIQueuesWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIQueuesWeight.setStatus(_A)
_ZxAnQosIIQueuesDepth_Type=ObjectIdentifier
_ZxAnQosIIQueuesDepth_Object=MibTableColumn
zxAnQosIIQueuesDepth=_ZxAnQosIIQueuesDepth_Object((1,3,6,1,4,1,3902,1015,21,3,14,1,4),_ZxAnQosIIQueuesDepth_Type())
zxAnQosIIQueuesDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIQueuesDepth.setStatus(_A)
_ZxAnQosIIQueuesBlockRowStatus_Type=RowStatus
_ZxAnQosIIQueuesBlockRowStatus_Object=MibTableColumn
zxAnQosIIQueuesBlockRowStatus=_ZxAnQosIIQueuesBlockRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,14,1,20),_ZxAnQosIIQueuesBlockRowStatus_Type())
zxAnQosIIQueuesBlockRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIQueuesBlockRowStatus.setStatus(_A)
_ZxAnQosIICosRemarkProfileTable_Object=MibTable
zxAnQosIICosRemarkProfileTable=_ZxAnQosIICosRemarkProfileTable_Object((1,3,6,1,4,1,3902,1015,21,3,15))
if mibBuilder.loadTexts:zxAnQosIICosRemarkProfileTable.setStatus(_A)
_ZxAnQosIICosRemarkProfileEntry_Object=MibTableRow
zxAnQosIICosRemarkProfileEntry=_ZxAnQosIICosRemarkProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,3,15,1))
zxAnQosIICosRemarkProfileEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:zxAnQosIICosRemarkProfileEntry.setStatus(_A)
class _ZxAnQosIICosRemarkPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIICosRemarkPrfName_Type.__name__=_F
_ZxAnQosIICosRemarkPrfName_Object=MibTableColumn
zxAnQosIICosRemarkPrfName=_ZxAnQosIICosRemarkPrfName_Object((1,3,6,1,4,1,3902,1015,21,3,15,1,1),_ZxAnQosIICosRemarkPrfName_Type())
zxAnQosIICosRemarkPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIICosRemarkPrfName.setStatus(_A)
_ZxAnQosIIEgressPriority_Type=ObjectIdentifier
_ZxAnQosIIEgressPriority_Object=MibTableColumn
zxAnQosIIEgressPriority=_ZxAnQosIIEgressPriority_Object((1,3,6,1,4,1,3902,1015,21,3,15,1,2),_ZxAnQosIIEgressPriority_Type())
zxAnQosIIEgressPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIEgressPriority.setStatus(_A)
_ZxAnQosIICosRemarkRowStatus_Type=RowStatus
_ZxAnQosIICosRemarkRowStatus_Object=MibTableColumn
zxAnQosIICosRemarkRowStatus=_ZxAnQosIICosRemarkRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,15,1,20),_ZxAnQosIICosRemarkRowStatus_Type())
zxAnQosIICosRemarkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIICosRemarkRowStatus.setStatus(_A)
_ZxAnQosIITrafficProfileTable_Object=MibTable
zxAnQosIITrafficProfileTable=_ZxAnQosIITrafficProfileTable_Object((1,3,6,1,4,1,3902,1015,21,3,16))
if mibBuilder.loadTexts:zxAnQosIITrafficProfileTable.setStatus(_A)
_ZxAnQosIITrafficProfileEntry_Object=MibTableRow
zxAnQosIITrafficProfileEntry=_ZxAnQosIITrafficProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,3,16,1))
zxAnQosIITrafficProfileEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:zxAnQosIITrafficProfileEntry.setStatus(_A)
class _ZxAnQosIITrafficPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIITrafficPrfName_Type.__name__=_F
_ZxAnQosIITrafficPrfName_Object=MibTableColumn
zxAnQosIITrafficPrfName=_ZxAnQosIITrafficPrfName_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,1),_ZxAnQosIITrafficPrfName_Type())
zxAnQosIITrafficPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficPrfName.setStatus(_A)
class _ZxAnQosIITrafficConfCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2621440))
_ZxAnQosIITrafficConfCir_Type.__name__=_C
_ZxAnQosIITrafficConfCir_Object=MibTableColumn
zxAnQosIITrafficConfCir=_ZxAnQosIITrafficConfCir_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,2),_ZxAnQosIITrafficConfCir_Type())
zxAnQosIITrafficConfCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficConfCir.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficConfCir.setUnits(_G)
class _ZxAnQosIITrafficConfCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_ZxAnQosIITrafficConfCbs_Type.__name__=_C
_ZxAnQosIITrafficConfCbs_Object=MibTableColumn
zxAnQosIITrafficConfCbs=_ZxAnQosIITrafficConfCbs_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,3),_ZxAnQosIITrafficConfCbs_Type())
zxAnQosIITrafficConfCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficConfCbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficConfCbs.setUnits(_a)
class _ZxAnQosIITrafficConfPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2621440))
_ZxAnQosIITrafficConfPir_Type.__name__=_C
_ZxAnQosIITrafficConfPir_Object=MibTableColumn
zxAnQosIITrafficConfPir=_ZxAnQosIITrafficConfPir_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,4),_ZxAnQosIITrafficConfPir_Type())
zxAnQosIITrafficConfPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficConfPir.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficConfPir.setUnits(_G)
class _ZxAnQosIITrafficConfPbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_ZxAnQosIITrafficConfPbs_Type.__name__=_C
_ZxAnQosIITrafficConfPbs_Object=MibTableColumn
zxAnQosIITrafficConfPbs=_ZxAnQosIITrafficConfPbs_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,5),_ZxAnQosIITrafficConfPbs_Type())
zxAnQosIITrafficConfPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficConfPbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficConfPbs.setUnits(_a)
class _ZxAnQosIITrafficCosPriorityTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_Q,1),(_J,2),(_M,255)))
_ZxAnQosIITrafficCosPriorityTrust_Type.__name__=_C
_ZxAnQosIITrafficCosPriorityTrust_Object=MibTableColumn
zxAnQosIITrafficCosPriorityTrust=_ZxAnQosIITrafficCosPriorityTrust_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,6),_ZxAnQosIITrafficCosPriorityTrust_Type())
zxAnQosIITrafficCosPriorityTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficCosPriorityTrust.setStatus(_A)
class _ZxAnQosIITrafficCosPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIITrafficCosPriority_Type.__name__=_C
_ZxAnQosIITrafficCosPriority_Object=MibTableColumn
zxAnQosIITrafficCosPriority=_ZxAnQosIITrafficCosPriority_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,7),_ZxAnQosIITrafficCosPriority_Type())
zxAnQosIITrafficCosPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficCosPriority.setStatus(_A)
class _ZxAnQosIITrafficDiscardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noDistinction',1),('lowPriorityFirst',2)))
_ZxAnQosIITrafficDiscardMode_Type.__name__=_C
_ZxAnQosIITrafficDiscardMode_Object=MibTableColumn
zxAnQosIITrafficDiscardMode=_ZxAnQosIITrafficDiscardMode_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,8),_ZxAnQosIITrafficDiscardMode_Type())
zxAnQosIITrafficDiscardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficDiscardMode.setStatus(_A)
_ZxAnQosIITrafficRowStatus_Type=RowStatus
_ZxAnQosIITrafficRowStatus_Object=MibTableColumn
zxAnQosIITrafficRowStatus=_ZxAnQosIITrafficRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,16,1,20),_ZxAnQosIITrafficRowStatus_Type())
zxAnQosIITrafficRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficRowStatus.setStatus(_A)
_ZxAnQosIIVPortProfileTable_Object=MibTable
zxAnQosIIVPortProfileTable=_ZxAnQosIIVPortProfileTable_Object((1,3,6,1,4,1,3902,1015,21,3,17))
if mibBuilder.loadTexts:zxAnQosIIVPortProfileTable.setStatus(_A)
_ZxAnQosIIVPortProfileEntry_Object=MibTableRow
zxAnQosIIVPortProfileEntry=_ZxAnQosIIVPortProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,3,17,1))
zxAnQosIIVPortProfileEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:zxAnQosIIVPortProfileEntry.setStatus(_A)
class _ZxAnQosIIVPortPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIVPortPrfName_Type.__name__=_F
_ZxAnQosIIVPortPrfName_Object=MibTableColumn
zxAnQosIIVPortPrfName=_ZxAnQosIIVPortPrfName_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,1),_ZxAnQosIIVPortPrfName_Type())
zxAnQosIIVPortPrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIVPortPrfName.setStatus(_A)
class _ZxAnQosIIConfCosRemark_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIConfCosRemark_Type.__name__=_F
_ZxAnQosIIConfCosRemark_Object=MibTableColumn
zxAnQosIIConfCosRemark=_ZxAnQosIIConfCosRemark_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,2),_ZxAnQosIIConfCosRemark_Type())
zxAnQosIIConfCosRemark.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfCosRemark.setStatus(_A)
class _ZxAnQosIIConfDefCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIConfDefCos_Type.__name__=_C
_ZxAnQosIIConfDefCos_Object=MibTableColumn
zxAnQosIIConfDefCos=_ZxAnQosIIConfDefCos_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,3),_ZxAnQosIIConfDefCos_Type())
zxAnQosIIConfDefCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfDefCos.setStatus(_A)
class _ZxAnQosIIConfDefCtagCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIConfDefCtagCos_Type.__name__=_C
_ZxAnQosIIConfDefCtagCos_Object=MibTableColumn
zxAnQosIIConfDefCtagCos=_ZxAnQosIIConfDefCtagCos_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,4),_ZxAnQosIIConfDefCtagCos_Type())
zxAnQosIIConfDefCtagCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfDefCtagCos.setStatus(_A)
class _ZxAnQosIIConfCosFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ZxAnQosIIConfCosFilter_Type.__name__=_C
_ZxAnQosIIConfCosFilter_Object=MibTableColumn
zxAnQosIIConfCosFilter=_ZxAnQosIIConfCosFilter_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,5),_ZxAnQosIIConfCosFilter_Type())
zxAnQosIIConfCosFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfCosFilter.setStatus(_A)
class _ZxAnQosIIConfCosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_S,4),(_I,255)))
_ZxAnQosIIConfCosMode_Type.__name__=_C
_ZxAnQosIIConfCosMode_Object=MibTableColumn
zxAnQosIIConfCosMode=_ZxAnQosIIConfCosMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,6),_ZxAnQosIIConfCosMode_Type())
zxAnQosIIConfCosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfCosMode.setStatus(_A)
class _ZxAnQosIIConfCtagCosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_S,4),(_I,255)))
_ZxAnQosIIConfCtagCosMode_Type.__name__=_C
_ZxAnQosIIConfCtagCosMode_Object=MibTableColumn
zxAnQosIIConfCtagCosMode=_ZxAnQosIIConfCtagCosMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,7),_ZxAnQosIIConfCtagCosMode_Type())
zxAnQosIIConfCtagCosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfCtagCosMode.setStatus(_A)
class _ZxAnQosIIConfDscpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_c,2),(_I,255)))
_ZxAnQosIIConfDscpMode_Type.__name__=_C
_ZxAnQosIIConfDscpMode_Object=MibTableColumn
zxAnQosIIConfDscpMode=_ZxAnQosIIConfDscpMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,8),_ZxAnQosIIConfDscpMode_Type())
zxAnQosIIConfDscpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfDscpMode.setStatus(_A)
class _ZxAnQosIIConfDefScos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIConfDefScos_Type.__name__=_C
_ZxAnQosIIConfDefScos_Object=MibTableColumn
zxAnQosIIConfDefScos=_ZxAnQosIIConfDefScos_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,9),_ZxAnQosIIConfDefScos_Type())
zxAnQosIIConfDefScos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfDefScos.setStatus(_A)
class _ZxAnQosIIConfIngressCosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_J,1),('scosOverride',2),('scosRemark',3),('ccosScosRemark',4),('ccosScosOverride',5),(_M,255)))
_ZxAnQosIIConfIngressCosMode_Type.__name__=_C
_ZxAnQosIIConfIngressCosMode_Object=MibTableColumn
zxAnQosIIConfIngressCosMode=_ZxAnQosIIConfIngressCosMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,10),_ZxAnQosIIConfIngressCosMode_Type())
zxAnQosIIConfIngressCosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfIngressCosMode.setStatus(_A)
class _ZxAnQosIIConfEgressCosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_J,1),(_R,2),(_S,3),(_M,255)))
_ZxAnQosIIConfEgressCosMode_Type.__name__=_C
_ZxAnQosIIConfEgressCosMode_Object=MibTableColumn
zxAnQosIIConfEgressCosMode=_ZxAnQosIIConfEgressCosMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,11),_ZxAnQosIIConfEgressCosMode_Type())
zxAnQosIIConfEgressCosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfEgressCosMode.setStatus(_A)
class _ZxAnQosIIConfIngressDscpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_J,1),(_c,2),(_M,255)))
_ZxAnQosIIConfIngressDscpMode_Type.__name__=_C
_ZxAnQosIIConfIngressDscpMode_Object=MibTableColumn
zxAnQosIIConfIngressDscpMode=_ZxAnQosIIConfIngressDscpMode_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,12),_ZxAnQosIIConfIngressDscpMode_Type())
zxAnQosIIConfIngressDscpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfIngressDscpMode.setStatus(_A)
class _ZxAnQosIIVPortPrfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pon',1),('dsl',2)))
_ZxAnQosIIVPortPrfType_Type.__name__=_C
_ZxAnQosIIVPortPrfType_Object=MibTableColumn
zxAnQosIIVPortPrfType=_ZxAnQosIIVPortPrfType_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,13),_ZxAnQosIIVPortPrfType_Type())
zxAnQosIIVPortPrfType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortPrfType.setStatus(_A)
class _ZxAnQosIIConfEgressCosRemark_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIConfEgressCosRemark_Type.__name__=_F
_ZxAnQosIIConfEgressCosRemark_Object=MibTableColumn
zxAnQosIIConfEgressCosRemark=_ZxAnQosIIConfEgressCosRemark_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,14),_ZxAnQosIIConfEgressCosRemark_Type())
zxAnQosIIConfEgressCosRemark.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIConfEgressCosRemark.setStatus(_A)
_ZxAnQosIIVPortPrfRowStatus_Type=RowStatus
_ZxAnQosIIVPortPrfRowStatus_Object=MibTableColumn
zxAnQosIIVPortPrfRowStatus=_ZxAnQosIIVPortPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,17,1,20),_ZxAnQosIIVPortPrfRowStatus_Type())
zxAnQosIIVPortPrfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortPrfRowStatus.setStatus(_A)
_ZxAnQosIIPortCfgTable_Object=MibTable
zxAnQosIIPortCfgTable=_ZxAnQosIIPortCfgTable_Object((1,3,6,1,4,1,3902,1015,21,3,21))
if mibBuilder.loadTexts:zxAnQosIIPortCfgTable.setStatus(_A)
_ZxAnQosIIPortCfgEntry_Object=MibTableRow
zxAnQosIIPortCfgEntry=_ZxAnQosIIPortCfgEntry_Object((1,3,6,1,4,1,3902,1015,21,3,21,1))
zxAnQosIIPortCfgEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:zxAnQosIIPortCfgEntry.setStatus(_A)
class _ZxAnQosIICosQueuePrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIICosQueuePrf_Type.__name__=_F
_ZxAnQosIICosQueuePrf_Object=MibTableColumn
zxAnQosIICosQueuePrf=_ZxAnQosIICosQueuePrf_Object((1,3,6,1,4,1,3902,1015,21,3,21,1,1),_ZxAnQosIICosQueuePrf_Type())
zxAnQosIICosQueuePrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIICosQueuePrf.setStatus(_A)
class _ZxAnQosIIQueueBlockPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIQueueBlockPrf_Type.__name__=_F
_ZxAnQosIIQueueBlockPrf_Object=MibTableColumn
zxAnQosIIQueueBlockPrf=_ZxAnQosIIQueueBlockPrf_Object((1,3,6,1,4,1,3902,1015,21,3,21,1,2),_ZxAnQosIIQueueBlockPrf_Type())
zxAnQosIIQueueBlockPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIQueueBlockPrf.setStatus(_A)
class _ZxAnQosIICosRemarkPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIICosRemarkPrf_Type.__name__=_F
_ZxAnQosIICosRemarkPrf_Object=MibTableColumn
zxAnQosIICosRemarkPrf=_ZxAnQosIICosRemarkPrf_Object((1,3,6,1,4,1,3902,1015,21,3,21,1,3),_ZxAnQosIICosRemarkPrf_Type())
zxAnQosIICosRemarkPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIICosRemarkPrf.setStatus(_A)
_ZxAnQosIIVPortCfgTable_Object=MibTable
zxAnQosIIVPortCfgTable=_ZxAnQosIIVPortCfgTable_Object((1,3,6,1,4,1,3902,1015,21,3,22))
if mibBuilder.loadTexts:zxAnQosIIVPortCfgTable.setStatus(_A)
_ZxAnQosIIVPortCfgEntry_Object=MibTableRow
zxAnQosIIVPortCfgEntry=_ZxAnQosIIVPortCfgEntry_Object((1,3,6,1,4,1,3902,1015,21,3,22,1))
zxAnQosIIVPortCfgEntry.setIndexNames((0,_D,_d),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:zxAnQosIIVPortCfgEntry.setStatus(_A)
_ZxAnQosIIRack_Type=Integer32
_ZxAnQosIIRack_Object=MibTableColumn
zxAnQosIIRack=_ZxAnQosIIRack_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,1),_ZxAnQosIIRack_Type())
zxAnQosIIRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIRack.setStatus(_A)
_ZxAnQosIIShelf_Type=Integer32
_ZxAnQosIIShelf_Object=MibTableColumn
zxAnQosIIShelf=_ZxAnQosIIShelf_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,2),_ZxAnQosIIShelf_Type())
zxAnQosIIShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIShelf.setStatus(_A)
_ZxAnQosIISlot_Type=Integer32
_ZxAnQosIISlot_Object=MibTableColumn
zxAnQosIISlot=_ZxAnQosIISlot_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,3),_ZxAnQosIISlot_Type())
zxAnQosIISlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIISlot.setStatus(_A)
_ZxAnQosIIPort_Type=Integer32
_ZxAnQosIIPort_Object=MibTableColumn
zxAnQosIIPort=_ZxAnQosIIPort_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,4),_ZxAnQosIIPort_Type())
zxAnQosIIPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIPort.setStatus(_A)
_ZxAnQosIIOnu_Type=Integer32
_ZxAnQosIIOnu_Object=MibTableColumn
zxAnQosIIOnu=_ZxAnQosIIOnu_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,5),_ZxAnQosIIOnu_Type())
zxAnQosIIOnu.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIOnu.setStatus(_A)
class _ZxAnQosIIVCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,12)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),('gpon',4),(_n,11),('vlan',12)))
_ZxAnQosIIVCircuitType_Type.__name__=_C
_ZxAnQosIIVCircuitType_Object=MibTableColumn
zxAnQosIIVCircuitType=_ZxAnQosIIVCircuitType_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,6),_ZxAnQosIIVCircuitType_Type())
zxAnQosIIVCircuitType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIVCircuitType.setStatus(_A)
_ZxAnQosIILogicalId_Type=Integer32
_ZxAnQosIILogicalId_Object=MibTableColumn
zxAnQosIILogicalId=_ZxAnQosIILogicalId_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,7),_ZxAnQosIILogicalId_Type())
zxAnQosIILogicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIILogicalId.setStatus(_A)
class _ZxAnQosIIVPortCfgPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIIVPortCfgPrf_Type.__name__=_F
_ZxAnQosIIVPortCfgPrf_Object=MibTableColumn
zxAnQosIIVPortCfgPrf=_ZxAnQosIIVPortCfgPrf_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,8),_ZxAnQosIIVPortCfgPrf_Type())
zxAnQosIIVPortCfgPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortCfgPrf.setStatus(_A)
class _ZxAnQosIIVPortMapQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ZxAnQosIIVPortMapQueue_Type.__name__=_C
_ZxAnQosIIVPortMapQueue_Object=MibTableColumn
zxAnQosIIVPortMapQueue=_ZxAnQosIIVPortMapQueue_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,9),_ZxAnQosIIVPortMapQueue_Type())
zxAnQosIIVPortMapQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortMapQueue.setStatus(_A)
class _ZxAnQosIIVPortServiceCategory_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('cbr',1),('ubr',2),('vbr',3),('unconfigured',255)))
_ZxAnQosIIVPortServiceCategory_Type.__name__=_C
_ZxAnQosIIVPortServiceCategory_Object=MibTableColumn
zxAnQosIIVPortServiceCategory=_ZxAnQosIIVPortServiceCategory_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,10),_ZxAnQosIIVPortServiceCategory_Type())
zxAnQosIIVPortServiceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortServiceCategory.setStatus(_A)
class _ZxAnQosIIVPortPcr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosIIVPortPcr_Type.__name__=_C
_ZxAnQosIIVPortPcr_Object=MibTableColumn
zxAnQosIIVPortPcr=_ZxAnQosIIVPortPcr_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,11),_ZxAnQosIIVPortPcr_Type())
zxAnQosIIVPortPcr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortPcr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIIVPortPcr.setUnits(_G)
class _ZxAnQosIIVPortMcr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosIIVPortMcr_Type.__name__=_C
_ZxAnQosIIVPortMcr_Object=MibTableColumn
zxAnQosIIVPortMcr=_ZxAnQosIIVPortMcr_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,12),_ZxAnQosIIVPortMcr_Type())
zxAnQosIIVPortMcr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortMcr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIIVPortMcr.setUnits(_G)
class _ZxAnQosIIVPortScr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosIIVPortScr_Type.__name__=_C
_ZxAnQosIIVPortScr_Object=MibTableColumn
zxAnQosIIVPortScr=_ZxAnQosIIVPortScr_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,13),_ZxAnQosIIVPortScr_Type())
zxAnQosIIVPortScr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortScr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIIVPortScr.setUnits(_G)
class _ZxAnQosIIVPortPcrRemarkCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIVPortPcrRemarkCos_Type.__name__=_C
_ZxAnQosIIVPortPcrRemarkCos_Object=MibTableColumn
zxAnQosIIVPortPcrRemarkCos=_ZxAnQosIIVPortPcrRemarkCos_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,14),_ZxAnQosIIVPortPcrRemarkCos_Type())
zxAnQosIIVPortPcrRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortPcrRemarkCos.setStatus(_A)
class _ZxAnQosIIVPortMcrRemarkCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIVPortMcrRemarkCos_Type.__name__=_C
_ZxAnQosIIVPortMcrRemarkCos_Object=MibTableColumn
zxAnQosIIVPortMcrRemarkCos=_ZxAnQosIIVPortMcrRemarkCos_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,15),_ZxAnQosIIVPortMcrRemarkCos_Type())
zxAnQosIIVPortMcrRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortMcrRemarkCos.setStatus(_A)
class _ZxAnQosIIVPortScrRemarkCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIIVPortScrRemarkCos_Type.__name__=_C
_ZxAnQosIIVPortScrRemarkCos_Object=MibTableColumn
zxAnQosIIVPortScrRemarkCos=_ZxAnQosIIVPortScrRemarkCos_Object((1,3,6,1,4,1,3902,1015,21,3,22,1,16),_ZxAnQosIIVPortScrRemarkCos_Type())
zxAnQosIIVPortScrRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIVPortScrRemarkCos.setStatus(_A)
_ZxAnQosIITrafficCfgTable_Object=MibTable
zxAnQosIITrafficCfgTable=_ZxAnQosIITrafficCfgTable_Object((1,3,6,1,4,1,3902,1015,21,3,23))
if mibBuilder.loadTexts:zxAnQosIITrafficCfgTable.setStatus(_A)
_ZxAnQosIITrafficCfgEntry_Object=MibTableRow
zxAnQosIITrafficCfgEntry=_ZxAnQosIITrafficCfgEntry_Object((1,3,6,1,4,1,3902,1015,21,3,23,1))
zxAnQosIITrafficCfgEntry.setIndexNames((0,_D,_o),(0,_D,_p),(0,_D,_q),(0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:zxAnQosIITrafficCfgEntry.setStatus(_A)
_ZxAnQosIITrafficRack_Type=Integer32
_ZxAnQosIITrafficRack_Object=MibTableColumn
zxAnQosIITrafficRack=_ZxAnQosIITrafficRack_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,1),_ZxAnQosIITrafficRack_Type())
zxAnQosIITrafficRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficRack.setStatus(_A)
_ZxAnQosIITrafficShelf_Type=Integer32
_ZxAnQosIITrafficShelf_Object=MibTableColumn
zxAnQosIITrafficShelf=_ZxAnQosIITrafficShelf_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,2),_ZxAnQosIITrafficShelf_Type())
zxAnQosIITrafficShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficShelf.setStatus(_A)
_ZxAnQosIITrafficSlot_Type=Integer32
_ZxAnQosIITrafficSlot_Object=MibTableColumn
zxAnQosIITrafficSlot=_ZxAnQosIITrafficSlot_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,3),_ZxAnQosIITrafficSlot_Type())
zxAnQosIITrafficSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficSlot.setStatus(_A)
_ZxAnQosIITrafficPort_Type=Integer32
_ZxAnQosIITrafficPort_Object=MibTableColumn
zxAnQosIITrafficPort=_ZxAnQosIITrafficPort_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,4),_ZxAnQosIITrafficPort_Type())
zxAnQosIITrafficPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficPort.setStatus(_A)
_ZxAnQosIITrafficOnu_Type=Integer32
_ZxAnQosIITrafficOnu_Object=MibTableColumn
zxAnQosIITrafficOnu=_ZxAnQosIITrafficOnu_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,5),_ZxAnQosIITrafficOnu_Type())
zxAnQosIITrafficOnu.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficOnu.setStatus(_A)
class _ZxAnQosIITrafficVCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,12)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),('gpon',4),(_n,11),('vlan',12)))
_ZxAnQosIITrafficVCircuitType_Type.__name__=_C
_ZxAnQosIITrafficVCircuitType_Object=MibTableColumn
zxAnQosIITrafficVCircuitType=_ZxAnQosIITrafficVCircuitType_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,6),_ZxAnQosIITrafficVCircuitType_Type())
zxAnQosIITrafficVCircuitType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficVCircuitType.setStatus(_A)
_ZxAnQosIITrafficLogicalId_Type=ObjectIdentifier
_ZxAnQosIITrafficLogicalId_Object=MibTableColumn
zxAnQosIITrafficLogicalId=_ZxAnQosIITrafficLogicalId_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,7),_ZxAnQosIITrafficLogicalId_Type())
zxAnQosIITrafficLogicalId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficLogicalId.setStatus(_A)
class _ZxAnQosIITrafficDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_ZxAnQosIITrafficDirection_Type.__name__=_C
_ZxAnQosIITrafficDirection_Object=MibTableColumn
zxAnQosIITrafficDirection=_ZxAnQosIITrafficDirection_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,8),_ZxAnQosIITrafficDirection_Type())
zxAnQosIITrafficDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIITrafficDirection.setStatus(_A)
class _ZxAnQosIITrafficSvcEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('pppoe',1),('ipoe',2),('all',3),(_I,255)))
_ZxAnQosIITrafficSvcEncapType_Type.__name__=_C
_ZxAnQosIITrafficSvcEncapType_Object=MibTableColumn
zxAnQosIITrafficSvcEncapType=_ZxAnQosIITrafficSvcEncapType_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,9),_ZxAnQosIITrafficSvcEncapType_Type())
zxAnQosIITrafficSvcEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficSvcEncapType.setStatus(_A)
_ZxAnQosIITrafficPrf_Type=DisplayString
_ZxAnQosIITrafficPrf_Object=MibTableColumn
zxAnQosIITrafficPrf=_ZxAnQosIITrafficPrf_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,10),_ZxAnQosIITrafficPrf_Type())
zxAnQosIITrafficPrf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficPrf.setStatus(_A)
_ZxAnQosIITrafficCfgRowStatus_Type=RowStatus
_ZxAnQosIITrafficCfgRowStatus_Object=MibTableColumn
zxAnQosIITrafficCfgRowStatus=_ZxAnQosIITrafficCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,23,1,20),_ZxAnQosIITrafficCfgRowStatus_Type())
zxAnQosIITrafficCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIITrafficCfgRowStatus.setStatus(_A)
_ZxAnQosIITrafficBandwidthTable_Object=MibTable
zxAnQosIITrafficBandwidthTable=_ZxAnQosIITrafficBandwidthTable_Object((1,3,6,1,4,1,3902,1015,21,3,24))
if mibBuilder.loadTexts:zxAnQosIITrafficBandwidthTable.setStatus(_A)
_ZxAnQosIITrafficBandwidthEntry_Object=MibTableRow
zxAnQosIITrafficBandwidthEntry=_ZxAnQosIITrafficBandwidthEntry_Object((1,3,6,1,4,1,3902,1015,21,3,24,1))
zxAnQosIITrafficBandwidthEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:zxAnQosIITrafficBandwidthEntry.setStatus(_A)
_ZxAnQosIITrafficTotalBandwidth_Type=Integer32
_ZxAnQosIITrafficTotalBandwidth_Object=MibTableColumn
zxAnQosIITrafficTotalBandwidth=_ZxAnQosIITrafficTotalBandwidth_Object((1,3,6,1,4,1,3902,1015,21,3,24,1,1),_ZxAnQosIITrafficTotalBandwidth_Type())
zxAnQosIITrafficTotalBandwidth.setMaxAccess(_w)
if mibBuilder.loadTexts:zxAnQosIITrafficTotalBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficTotalBandwidth.setUnits(_G)
_ZxAnQosIITrafficRemainBandwidth_Type=Integer32
_ZxAnQosIITrafficRemainBandwidth_Object=MibTableColumn
zxAnQosIITrafficRemainBandwidth=_ZxAnQosIITrafficRemainBandwidth_Object((1,3,6,1,4,1,3902,1015,21,3,24,1,2),_ZxAnQosIITrafficRemainBandwidth_Type())
zxAnQosIITrafficRemainBandwidth.setMaxAccess(_w)
if mibBuilder.loadTexts:zxAnQosIITrafficRemainBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIITrafficRemainBandwidth.setUnits(_G)
_ZxAnQosIIMVlan2CosTable_Object=MibTable
zxAnQosIIMVlan2CosTable=_ZxAnQosIIMVlan2CosTable_Object((1,3,6,1,4,1,3902,1015,21,3,25))
if mibBuilder.loadTexts:zxAnQosIIMVlan2CosTable.setStatus(_A)
_ZxAnQosIIMVlan2CosEntry_Object=MibTableRow
zxAnQosIIMVlan2CosEntry=_ZxAnQosIIMVlan2CosEntry_Object((1,3,6,1,4,1,3902,1015,21,3,25,1))
zxAnQosIIMVlan2CosEntry.setIndexNames((0,_D,_x))
if mibBuilder.loadTexts:zxAnQosIIMVlan2CosEntry.setStatus(_A)
class _ZxAnQosIIMVlan2CosMVlanValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_ZxAnQosIIMVlan2CosMVlanValue_Type.__name__=_C
_ZxAnQosIIMVlan2CosMVlanValue_Object=MibTableColumn
zxAnQosIIMVlan2CosMVlanValue=_ZxAnQosIIMVlan2CosMVlanValue_Object((1,3,6,1,4,1,3902,1015,21,3,25,1,1),_ZxAnQosIIMVlan2CosMVlanValue_Type())
zxAnQosIIMVlan2CosMVlanValue.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIIMVlan2CosMVlanValue.setStatus(_A)
class _ZxAnQosIIMVlan2CosCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIIMVlan2CosCosValue_Type.__name__=_C
_ZxAnQosIIMVlan2CosCosValue_Object=MibTableColumn
zxAnQosIIMVlan2CosCosValue=_ZxAnQosIIMVlan2CosCosValue_Object((1,3,6,1,4,1,3902,1015,21,3,25,1,2),_ZxAnQosIIMVlan2CosCosValue_Type())
zxAnQosIIMVlan2CosCosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIMVlan2CosCosValue.setStatus(_A)
_ZxAnQosIIMVlan2CosRowStatus_Type=RowStatus
_ZxAnQosIIMVlan2CosRowStatus_Object=MibTableColumn
zxAnQosIIMVlan2CosRowStatus=_ZxAnQosIIMVlan2CosRowStatus_Object((1,3,6,1,4,1,3902,1015,21,3,25,1,20),_ZxAnQosIIMVlan2CosRowStatus_Type())
zxAnQosIIMVlan2CosRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnQosIIMVlan2CosRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnQosMib':zxAnQosMib,'zxAnQosIIObjects':zxAnQosIIObjects,'zxAnQosIINniCos2DropMap':zxAnQosIINniCos2DropMap,'zxAnQosIINniCos2LocalMap':zxAnQosIINniCos2LocalMap,'zxAnQosIINniDscpMappingTable':zxAnQosIINniDscpMappingTable,'zxAnQosIINniDscpMappingEntry':zxAnQosIINniDscpMappingEntry,_T:zxAnQosIINniIngressDscp,'zxAnQosIINniEgressDscp':zxAnQosIINniEgressDscp,'zxAnQosIINniEgressCos':zxAnQosIINniEgressCos,'zxAnQosIINniEgressDropPrecedence':zxAnQosIINniEgressDropPrecedence,'zxAnQosIINniPortCfgTable':zxAnQosIINniPortCfgTable,'zxAnQosIINniPortCfgEntry':zxAnQosIINniPortCfgEntry,'zxAnQosIINniDefPriority':zxAnQosIINniDefPriority,'zxAnQosIINniTrustDscp':zxAnQosIINniTrustDscp,'zxAnQosIINniTrustCos':zxAnQosIINniTrustCos,'zxAnQosIINniQueuesAlgorithm':zxAnQosIINniQueuesAlgorithm,'zxAnQosIINniQueuesWeight':zxAnQosIINniQueuesWeight,'zxAnQosIINniQueuesMinRate':zxAnQosIINniQueuesMinRate,'zxAnQosIINniQueuesMaxRate':zxAnQosIINniQueuesMaxRate,'zxAnQosIINniShapeRateLimit':zxAnQosIINniShapeRateLimit,'zxAnQosIINniShapeBurstSize':zxAnQosIINniShapeBurstSize,'zxAnQosIINniQueuesDepth':zxAnQosIINniQueuesDepth,'zxAnQosIINniGlobal':zxAnQosIINniGlobal,'zxAnQosIINniGlobalTrustMode':zxAnQosIINniGlobalTrustMode,'zxAnQosIICos2DscpTable':zxAnQosIICos2DscpTable,'zxAnQosIICos2DscpEntry':zxAnQosIICos2DscpEntry,_U:zxAnQosIICos2DscpCosValue,'zxAnQosIICos2DscpDscpValue':zxAnQosIICos2DscpDscpValue,'zxAnQosIIDscp2CosTable':zxAnQosIIDscp2CosTable,'zxAnQosIIDscp2CosEntry':zxAnQosIIDscp2CosEntry,_V:zxAnQosIIDscp2CosDscpValue,'zxAnQosIIDscp2CosCosValue':zxAnQosIIDscp2CosCosValue,'zxAnQosIICos2QueuesProfileTable':zxAnQosIICos2QueuesProfileTable,'zxAnQosIICos2QueuesProfileEntry':zxAnQosIICos2QueuesProfileEntry,_W:zxAnQosIICos2QueuesPrfName,'zxAnQosIICos2Queues':zxAnQosIICos2Queues,'zxAnQosIIDropPrecedence':zxAnQosIIDropPrecedence,'zxAnQosIICos2QueuesRowStatus':zxAnQosIICos2QueuesRowStatus,'zxAnQosIIQueuesBlockProfileTable':zxAnQosIIQueuesBlockProfileTable,'zxAnQosIIQueuesBlockProfileEntry':zxAnQosIIQueuesBlockProfileEntry,_X:zxAnQosIIQueuesBlockPrfName,'zxAnQosIIQueuesPriority':zxAnQosIIQueuesPriority,'zxAnQosIIQueuesWeight':zxAnQosIIQueuesWeight,'zxAnQosIIQueuesDepth':zxAnQosIIQueuesDepth,'zxAnQosIIQueuesBlockRowStatus':zxAnQosIIQueuesBlockRowStatus,'zxAnQosIICosRemarkProfileTable':zxAnQosIICosRemarkProfileTable,'zxAnQosIICosRemarkProfileEntry':zxAnQosIICosRemarkProfileEntry,_Y:zxAnQosIICosRemarkPrfName,'zxAnQosIIEgressPriority':zxAnQosIIEgressPriority,'zxAnQosIICosRemarkRowStatus':zxAnQosIICosRemarkRowStatus,'zxAnQosIITrafficProfileTable':zxAnQosIITrafficProfileTable,'zxAnQosIITrafficProfileEntry':zxAnQosIITrafficProfileEntry,_Z:zxAnQosIITrafficPrfName,'zxAnQosIITrafficConfCir':zxAnQosIITrafficConfCir,'zxAnQosIITrafficConfCbs':zxAnQosIITrafficConfCbs,'zxAnQosIITrafficConfPir':zxAnQosIITrafficConfPir,'zxAnQosIITrafficConfPbs':zxAnQosIITrafficConfPbs,'zxAnQosIITrafficCosPriorityTrust':zxAnQosIITrafficCosPriorityTrust,'zxAnQosIITrafficCosPriority':zxAnQosIITrafficCosPriority,'zxAnQosIITrafficDiscardMode':zxAnQosIITrafficDiscardMode,'zxAnQosIITrafficRowStatus':zxAnQosIITrafficRowStatus,'zxAnQosIIVPortProfileTable':zxAnQosIIVPortProfileTable,'zxAnQosIIVPortProfileEntry':zxAnQosIIVPortProfileEntry,_b:zxAnQosIIVPortPrfName,'zxAnQosIIConfCosRemark':zxAnQosIIConfCosRemark,'zxAnQosIIConfDefCos':zxAnQosIIConfDefCos,'zxAnQosIIConfDefCtagCos':zxAnQosIIConfDefCtagCos,'zxAnQosIIConfCosFilter':zxAnQosIIConfCosFilter,'zxAnQosIIConfCosMode':zxAnQosIIConfCosMode,'zxAnQosIIConfCtagCosMode':zxAnQosIIConfCtagCosMode,'zxAnQosIIConfDscpMode':zxAnQosIIConfDscpMode,'zxAnQosIIConfDefScos':zxAnQosIIConfDefScos,'zxAnQosIIConfIngressCosMode':zxAnQosIIConfIngressCosMode,'zxAnQosIIConfEgressCosMode':zxAnQosIIConfEgressCosMode,'zxAnQosIIConfIngressDscpMode':zxAnQosIIConfIngressDscpMode,'zxAnQosIIVPortPrfType':zxAnQosIIVPortPrfType,'zxAnQosIIConfEgressCosRemark':zxAnQosIIConfEgressCosRemark,'zxAnQosIIVPortPrfRowStatus':zxAnQosIIVPortPrfRowStatus,'zxAnQosIIPortCfgTable':zxAnQosIIPortCfgTable,'zxAnQosIIPortCfgEntry':zxAnQosIIPortCfgEntry,'zxAnQosIICosQueuePrf':zxAnQosIICosQueuePrf,'zxAnQosIIQueueBlockPrf':zxAnQosIIQueueBlockPrf,'zxAnQosIICosRemarkPrf':zxAnQosIICosRemarkPrf,'zxAnQosIIVPortCfgTable':zxAnQosIIVPortCfgTable,'zxAnQosIIVPortCfgEntry':zxAnQosIIVPortCfgEntry,_d:zxAnQosIIRack,_e:zxAnQosIIShelf,_f:zxAnQosIISlot,_g:zxAnQosIIPort,_h:zxAnQosIIOnu,_i:zxAnQosIIVCircuitType,_j:zxAnQosIILogicalId,'zxAnQosIIVPortCfgPrf':zxAnQosIIVPortCfgPrf,'zxAnQosIIVPortMapQueue':zxAnQosIIVPortMapQueue,'zxAnQosIIVPortServiceCategory':zxAnQosIIVPortServiceCategory,'zxAnQosIIVPortPcr':zxAnQosIIVPortPcr,'zxAnQosIIVPortMcr':zxAnQosIIVPortMcr,'zxAnQosIIVPortScr':zxAnQosIIVPortScr,'zxAnQosIIVPortPcrRemarkCos':zxAnQosIIVPortPcrRemarkCos,'zxAnQosIIVPortMcrRemarkCos':zxAnQosIIVPortMcrRemarkCos,'zxAnQosIIVPortScrRemarkCos':zxAnQosIIVPortScrRemarkCos,'zxAnQosIITrafficCfgTable':zxAnQosIITrafficCfgTable,'zxAnQosIITrafficCfgEntry':zxAnQosIITrafficCfgEntry,_o:zxAnQosIITrafficRack,_p:zxAnQosIITrafficShelf,_q:zxAnQosIITrafficSlot,_r:zxAnQosIITrafficPort,_s:zxAnQosIITrafficOnu,_t:zxAnQosIITrafficVCircuitType,_u:zxAnQosIITrafficLogicalId,_v:zxAnQosIITrafficDirection,'zxAnQosIITrafficSvcEncapType':zxAnQosIITrafficSvcEncapType,'zxAnQosIITrafficPrf':zxAnQosIITrafficPrf,'zxAnQosIITrafficCfgRowStatus':zxAnQosIITrafficCfgRowStatus,'zxAnQosIITrafficBandwidthTable':zxAnQosIITrafficBandwidthTable,'zxAnQosIITrafficBandwidthEntry':zxAnQosIITrafficBandwidthEntry,'zxAnQosIITrafficTotalBandwidth':zxAnQosIITrafficTotalBandwidth,'zxAnQosIITrafficRemainBandwidth':zxAnQosIITrafficRemainBandwidth,'zxAnQosIIMVlan2CosTable':zxAnQosIIMVlan2CosTable,'zxAnQosIIMVlan2CosEntry':zxAnQosIIMVlan2CosEntry,_x:zxAnQosIIMVlan2CosMVlanValue,'zxAnQosIIMVlan2CosCosValue':zxAnQosIIMVlan2CosCosValue,'zxAnQosIIMVlan2CosRowStatus':zxAnQosIIMVlan2CosRowStatus})