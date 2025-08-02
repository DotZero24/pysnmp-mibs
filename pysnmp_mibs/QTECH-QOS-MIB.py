_y='qtechQoSTrafficClassMIBGroup'
_x='qtechQoSPriorityMIBGroup'
_w='qtechIfOutPoliceMapName'
_v='qtechIfInPoliceMapName'
_u='qtechQoSPoliceMapConfMaxHighBandWidth'
_t='qtechQoSPoliceMapCfgEntryStatus'
_s='qtechQoSPoliceMapConfNewDscp'
_r='qtechQoSPoliceMapConfExceedDscp'
_q='qtechQoSPoliceMapConfExceedAction'
_p='qtechQoSPoliceMapConfMaxBandWidth'
_o='qtechQosPoliceMapEntryStatus'
_n='qtechQosClassMapEntryStatus'
_m='qtechQosClassAclName'
_l='qtechIpPreToDscp'
_k='qtechIfPriorityQosTrustMode'
_j='qtechIfPriorityBandwidth'
_i='qtechIfPriTrafficClassOperMode'
_h='qtechIfPriority'
_g='qtechPriorityBandWidth'
_f='qtechPriorityTrafficClassOperMode'
_e='qtechDscpTrafficClassPriority'
_d='qtechPriorityToDscp'
_c='qtechTrafficClass'
_b='qtechPriorityDscpMaxValue'
_a='qtechPriorityClassNum'
_Z='qtechPriorityTrafficClassNum'
_Y='qtechQoSGlobalStatus'
_X='qtechIfMulticastQueueIndex'
_W='qtechIfIndexMulticast'
_V='qtechIfQueueIndex'
_U='qtechIfIndex'
_T='qtechIfRateLimitIndex'
_S='qos-drr'
_R='qos-wrr'
_Q='qos-sp'
_P='qtechQosPoliceIfIndex'
_O='qtechQoSPoliceCfgClassMapName'
_N='qtechQoSPoliceCfgPoliceMapName'
_M='qtechQosPoliceMapName'
_L='qtechQosClassMapName'
_K='qtechIpPreClassPriority'
_J='qtechIfPriorityIfIndex'
_I='qtechDscpClass'
_H='qtechTrafficClassPriority'
_G='Integer32'
_F='DisplayString'
_E='read-create'
_D='read-write'
_C='read-only'
_B='QTECH-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
qtechQoSMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,18))
if mibBuilder.loadTexts:qtechQoSMIB.setRevisions(('2002-03-20 00:00',))
_QtechQoSPriorityMIBObjects_ObjectIdentity=ObjectIdentity
qtechQoSPriorityMIBObjects=_QtechQoSPriorityMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,18,1))
_QtechQoSGlobalStatus_Type=EnabledStatus
_QtechQoSGlobalStatus_Object=MibScalar
qtechQoSGlobalStatus=_QtechQoSGlobalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,1),_QtechQoSGlobalStatus_Type())
qtechQoSGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechQoSGlobalStatus.setStatus(_A)
_QtechPriorityTrafficClassNum_Type=Integer32
_QtechPriorityTrafficClassNum_Object=MibScalar
qtechPriorityTrafficClassNum=_QtechPriorityTrafficClassNum_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,2),_QtechPriorityTrafficClassNum_Type())
qtechPriorityTrafficClassNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPriorityTrafficClassNum.setStatus(_A)
_QtechPriorityClassNum_Type=Integer32
_QtechPriorityClassNum_Object=MibScalar
qtechPriorityClassNum=_QtechPriorityClassNum_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,3),_QtechPriorityClassNum_Type())
qtechPriorityClassNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPriorityClassNum.setStatus(_A)
_QtechPriorityDscpMaxValue_Type=Integer32
_QtechPriorityDscpMaxValue_Object=MibScalar
qtechPriorityDscpMaxValue=_QtechPriorityDscpMaxValue_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,4),_QtechPriorityDscpMaxValue_Type())
qtechPriorityDscpMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPriorityDscpMaxValue.setStatus(_A)
_QtechTrafficClassTable_Object=MibTable
qtechTrafficClassTable=_QtechTrafficClassTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,5))
if mibBuilder.loadTexts:qtechTrafficClassTable.setStatus(_A)
_QtechTrafficClassEntry_Object=MibTableRow
qtechTrafficClassEntry=_QtechTrafficClassEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,5,1))
qtechTrafficClassEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechTrafficClassEntry.setStatus(_A)
_QtechTrafficClassPriority_Type=Integer32
_QtechTrafficClassPriority_Object=MibTableColumn
qtechTrafficClassPriority=_QtechTrafficClassPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,5,1,1),_QtechTrafficClassPriority_Type())
qtechTrafficClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrafficClassPriority.setStatus(_A)
_QtechTrafficClass_Type=Integer32
_QtechTrafficClass_Object=MibTableColumn
qtechTrafficClass=_QtechTrafficClass_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,5,1,2),_QtechTrafficClass_Type())
qtechTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTrafficClass.setStatus(_A)
_QtechPriorityToDscp_Type=Integer32
_QtechPriorityToDscp_Object=MibTableColumn
qtechPriorityToDscp=_QtechPriorityToDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,5,1,3),_QtechPriorityToDscp_Type())
qtechPriorityToDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPriorityToDscp.setStatus(_A)
_QtechDscpClassTable_Object=MibTable
qtechDscpClassTable=_QtechDscpClassTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,6))
if mibBuilder.loadTexts:qtechDscpClassTable.setStatus(_A)
_QtechDscpClassEntry_Object=MibTableRow
qtechDscpClassEntry=_QtechDscpClassEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,6,1))
qtechDscpClassEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechDscpClassEntry.setStatus(_A)
_QtechDscpClass_Type=Integer32
_QtechDscpClass_Object=MibTableColumn
qtechDscpClass=_QtechDscpClass_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,6,1,1),_QtechDscpClass_Type())
qtechDscpClass.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDscpClass.setStatus(_A)
_QtechDscpTrafficClassPriority_Type=Integer32
_QtechDscpTrafficClassPriority_Object=MibTableColumn
qtechDscpTrafficClassPriority=_QtechDscpTrafficClassPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,6,1,2),_QtechDscpTrafficClassPriority_Type())
qtechDscpTrafficClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDscpTrafficClassPriority.setStatus(_A)
class _QtechPriorityTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_QtechPriorityTrafficClassOperMode_Type.__name__=_G
_QtechPriorityTrafficClassOperMode_Object=MibScalar
qtechPriorityTrafficClassOperMode=_QtechPriorityTrafficClassOperMode_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,7),_QtechPriorityTrafficClassOperMode_Type())
qtechPriorityTrafficClassOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPriorityTrafficClassOperMode.setStatus(_A)
_QtechPriorityBandWidth_Type=OctetString
_QtechPriorityBandWidth_Object=MibScalar
qtechPriorityBandWidth=_QtechPriorityBandWidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,8),_QtechPriorityBandWidth_Type())
qtechPriorityBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPriorityBandWidth.setStatus(_A)
_QtechIfPriorityTable_Object=MibTable
qtechIfPriorityTable=_QtechIfPriorityTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9))
if mibBuilder.loadTexts:qtechIfPriorityTable.setStatus(_A)
_QtechIfPriorityEntry_Object=MibTableRow
qtechIfPriorityEntry=_QtechIfPriorityEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1))
qtechIfPriorityEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechIfPriorityEntry.setStatus(_A)
_QtechIfPriorityIfIndex_Type=IfIndex
_QtechIfPriorityIfIndex_Object=MibTableColumn
qtechIfPriorityIfIndex=_QtechIfPriorityIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1,1),_QtechIfPriorityIfIndex_Type())
qtechIfPriorityIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfPriorityIfIndex.setStatus(_A)
_QtechIfPriority_Type=Integer32
_QtechIfPriority_Object=MibTableColumn
qtechIfPriority=_QtechIfPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1,2),_QtechIfPriority_Type())
qtechIfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfPriority.setStatus(_A)
class _QtechIfPriTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_QtechIfPriTrafficClassOperMode_Type.__name__=_G
_QtechIfPriTrafficClassOperMode_Object=MibTableColumn
qtechIfPriTrafficClassOperMode=_QtechIfPriTrafficClassOperMode_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1,3),_QtechIfPriTrafficClassOperMode_Type())
qtechIfPriTrafficClassOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfPriTrafficClassOperMode.setStatus(_A)
_QtechIfPriorityBandwidth_Type=OctetString
_QtechIfPriorityBandwidth_Object=MibTableColumn
qtechIfPriorityBandwidth=_QtechIfPriorityBandwidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1,4),_QtechIfPriorityBandwidth_Type())
qtechIfPriorityBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfPriorityBandwidth.setStatus(_A)
class _QtechIfPriorityQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-trust',1),('trust-cos',2),('trust-dscp',3),('trust-ip-precedence',4)))
_QtechIfPriorityQosTrustMode_Type.__name__=_G
_QtechIfPriorityQosTrustMode_Object=MibTableColumn
qtechIfPriorityQosTrustMode=_QtechIfPriorityQosTrustMode_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,9,1,5),_QtechIfPriorityQosTrustMode_Type())
qtechIfPriorityQosTrustMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfPriorityQosTrustMode.setStatus(_A)
_QtechIpPreClassTable_Object=MibTable
qtechIpPreClassTable=_QtechIpPreClassTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,10))
if mibBuilder.loadTexts:qtechIpPreClassTable.setStatus(_A)
_QtechIpPreClassEntry_Object=MibTableRow
qtechIpPreClassEntry=_QtechIpPreClassEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,10,1))
qtechIpPreClassEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechIpPreClassEntry.setStatus(_A)
_QtechIpPreClassPriority_Type=Integer32
_QtechIpPreClassPriority_Object=MibTableColumn
qtechIpPreClassPriority=_QtechIpPreClassPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,10,1,1),_QtechIpPreClassPriority_Type())
qtechIpPreClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPreClassPriority.setStatus(_A)
_QtechIpPreToDscp_Type=Integer32
_QtechIpPreToDscp_Object=MibTableColumn
qtechIpPreToDscp=_QtechIpPreToDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,10,1,2),_QtechIpPreToDscp_Type())
qtechIpPreToDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpPreToDscp.setStatus(_A)
_QtechIfRateLimitTable_Object=MibTable
qtechIfRateLimitTable=_QtechIfRateLimitTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11))
if mibBuilder.loadTexts:qtechIfRateLimitTable.setStatus(_A)
_QtechIfRateLimitEntry_Object=MibTableRow
qtechIfRateLimitEntry=_QtechIfRateLimitEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1))
qtechIfRateLimitEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:qtechIfRateLimitEntry.setStatus(_A)
_QtechIfRateLimitIndex_Type=IfIndex
_QtechIfRateLimitIndex_Object=MibTableColumn
qtechIfRateLimitIndex=_QtechIfRateLimitIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1,1),_QtechIfRateLimitIndex_Type())
qtechIfRateLimitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfRateLimitIndex.setStatus(_A)
_QtechIfRateLimitInMaxBandWidth_Type=Unsigned32
_QtechIfRateLimitInMaxBandWidth_Object=MibTableColumn
qtechIfRateLimitInMaxBandWidth=_QtechIfRateLimitInMaxBandWidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1,2),_QtechIfRateLimitInMaxBandWidth_Type())
qtechIfRateLimitInMaxBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfRateLimitInMaxBandWidth.setStatus(_A)
_QtechIfRateLimitInBurstFlowLimit_Type=Integer32
_QtechIfRateLimitInBurstFlowLimit_Object=MibTableColumn
qtechIfRateLimitInBurstFlowLimit=_QtechIfRateLimitInBurstFlowLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1,3),_QtechIfRateLimitInBurstFlowLimit_Type())
qtechIfRateLimitInBurstFlowLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfRateLimitInBurstFlowLimit.setStatus(_A)
_QtechIfRateLimitOutMaxBandWidth_Type=Unsigned32
_QtechIfRateLimitOutMaxBandWidth_Object=MibTableColumn
qtechIfRateLimitOutMaxBandWidth=_QtechIfRateLimitOutMaxBandWidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1,4),_QtechIfRateLimitOutMaxBandWidth_Type())
qtechIfRateLimitOutMaxBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfRateLimitOutMaxBandWidth.setStatus(_A)
_QtechIfRateLimitOutBurstFlowLimit_Type=Integer32
_QtechIfRateLimitOutBurstFlowLimit_Object=MibTableColumn
qtechIfRateLimitOutBurstFlowLimit=_QtechIfRateLimitOutBurstFlowLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,11,1,5),_QtechIfRateLimitOutBurstFlowLimit_Type())
qtechIfRateLimitOutBurstFlowLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfRateLimitOutBurstFlowLimit.setStatus(_A)
_QtechIfQueueSupportTable_Object=MibTable
qtechIfQueueSupportTable=_QtechIfQueueSupportTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12))
if mibBuilder.loadTexts:qtechIfQueueSupportTable.setStatus(_A)
_QtechIfQueueSupportEntry_Object=MibTableRow
qtechIfQueueSupportEntry=_QtechIfQueueSupportEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1))
qtechIfQueueSupportEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:qtechIfQueueSupportEntry.setStatus(_A)
_QtechIfIndex_Type=IfIndex
_QtechIfIndex_Object=MibTableColumn
qtechIfIndex=_QtechIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,1),_QtechIfIndex_Type())
qtechIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfIndex.setStatus(_A)
_QtechIfQueueIndex_Type=Integer32
_QtechIfQueueIndex_Object=MibTableColumn
qtechIfQueueIndex=_QtechIfQueueIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,2),_QtechIfQueueIndex_Type())
qtechIfQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQueueIndex.setStatus(_A)
_QtechIfQueueSupportTransmitPacket_Type=Counter64
_QtechIfQueueSupportTransmitPacket_Object=MibTableColumn
qtechIfQueueSupportTransmitPacket=_QtechIfQueueSupportTransmitPacket_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,3),_QtechIfQueueSupportTransmitPacket_Type())
qtechIfQueueSupportTransmitPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQueueSupportTransmitPacket.setStatus(_A)
_QtechIfQueueSupportTransmitBytes_Type=Counter64
_QtechIfQueueSupportTransmitBytes_Object=MibTableColumn
qtechIfQueueSupportTransmitBytes=_QtechIfQueueSupportTransmitBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,4),_QtechIfQueueSupportTransmitBytes_Type())
qtechIfQueueSupportTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQueueSupportTransmitBytes.setStatus(_A)
_QtechIfQueueSupportDropPacket_Type=Counter64
_QtechIfQueueSupportDropPacket_Object=MibTableColumn
qtechIfQueueSupportDropPacket=_QtechIfQueueSupportDropPacket_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,5),_QtechIfQueueSupportDropPacket_Type())
qtechIfQueueSupportDropPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQueueSupportDropPacket.setStatus(_A)
_QtechIfQueueSupportDropBytes_Type=Counter64
_QtechIfQueueSupportDropBytes_Object=MibTableColumn
qtechIfQueueSupportDropBytes=_QtechIfQueueSupportDropBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,12,1,6),_QtechIfQueueSupportDropBytes_Type())
qtechIfQueueSupportDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfQueueSupportDropBytes.setStatus(_A)
_QtechIfMulticastQueueSupportTable_Object=MibTable
qtechIfMulticastQueueSupportTable=_QtechIfMulticastQueueSupportTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13))
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportTable.setStatus(_A)
_QtechIfMulticastQueueSupportEntry_Object=MibTableRow
qtechIfMulticastQueueSupportEntry=_QtechIfMulticastQueueSupportEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1))
qtechIfMulticastQueueSupportEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportEntry.setStatus(_A)
_QtechIfIndexMulticast_Type=IfIndex
_QtechIfIndexMulticast_Object=MibTableColumn
qtechIfIndexMulticast=_QtechIfIndexMulticast_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,1),_QtechIfIndexMulticast_Type())
qtechIfIndexMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfIndexMulticast.setStatus(_A)
_QtechIfMulticastQueueIndex_Type=Integer32
_QtechIfMulticastQueueIndex_Object=MibTableColumn
qtechIfMulticastQueueIndex=_QtechIfMulticastQueueIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,2),_QtechIfMulticastQueueIndex_Type())
qtechIfMulticastQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfMulticastQueueIndex.setStatus(_A)
_QtechIfMulticastQueueSupportTransmitPacket_Type=Counter64
_QtechIfMulticastQueueSupportTransmitPacket_Object=MibTableColumn
qtechIfMulticastQueueSupportTransmitPacket=_QtechIfMulticastQueueSupportTransmitPacket_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,3),_QtechIfMulticastQueueSupportTransmitPacket_Type())
qtechIfMulticastQueueSupportTransmitPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportTransmitPacket.setStatus(_A)
_QtechIfMulticastQueueSupportTransmitBytes_Type=Counter64
_QtechIfMulticastQueueSupportTransmitBytes_Object=MibTableColumn
qtechIfMulticastQueueSupportTransmitBytes=_QtechIfMulticastQueueSupportTransmitBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,4),_QtechIfMulticastQueueSupportTransmitBytes_Type())
qtechIfMulticastQueueSupportTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportTransmitBytes.setStatus(_A)
_QtechIfMulticastQueueSupportDropPacket_Type=Counter64
_QtechIfMulticastQueueSupportDropPacket_Object=MibTableColumn
qtechIfMulticastQueueSupportDropPacket=_QtechIfMulticastQueueSupportDropPacket_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,5),_QtechIfMulticastQueueSupportDropPacket_Type())
qtechIfMulticastQueueSupportDropPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportDropPacket.setStatus(_A)
_QtechIfMulticastQueueSupportDropBytes_Type=Counter64
_QtechIfMulticastQueueSupportDropBytes_Object=MibTableColumn
qtechIfMulticastQueueSupportDropBytes=_QtechIfMulticastQueueSupportDropBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,18,1,13,1,6),_QtechIfMulticastQueueSupportDropBytes_Type())
qtechIfMulticastQueueSupportDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIfMulticastQueueSupportDropBytes.setStatus(_A)
_QtechQoSTrafficClassMIBObjects_ObjectIdentity=ObjectIdentity
qtechQoSTrafficClassMIBObjects=_QtechQoSTrafficClassMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,18,2))
_QtechQoSTrafficClassTable_Object=MibTable
qtechQoSTrafficClassTable=_QtechQoSTrafficClassTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,1))
if mibBuilder.loadTexts:qtechQoSTrafficClassTable.setStatus(_A)
_QtechQoSTrafficClassEntry_Object=MibTableRow
qtechQoSTrafficClassEntry=_QtechQoSTrafficClassEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,1,1))
qtechQoSTrafficClassEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechQoSTrafficClassEntry.setStatus(_A)
class _QtechQosClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechQosClassMapName_Type.__name__=_F
_QtechQosClassMapName_Object=MibTableColumn
qtechQosClassMapName=_QtechQosClassMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,1,1,1),_QtechQosClassMapName_Type())
qtechQosClassMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQosClassMapName.setStatus(_A)
class _QtechQosClassAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechQosClassAclName_Type.__name__=_F
_QtechQosClassAclName_Object=MibTableColumn
qtechQosClassAclName=_QtechQosClassAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,1,1,2),_QtechQosClassAclName_Type())
qtechQosClassAclName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQosClassAclName.setStatus(_A)
_QtechQosClassMapEntryStatus_Type=ConfigStatus
_QtechQosClassMapEntryStatus_Object=MibTableColumn
qtechQosClassMapEntryStatus=_QtechQosClassMapEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,1,1,3),_QtechQosClassMapEntryStatus_Type())
qtechQosClassMapEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQosClassMapEntryStatus.setStatus(_A)
_QtechQoSPoliceMapTable_Object=MibTable
qtechQoSPoliceMapTable=_QtechQoSPoliceMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,2))
if mibBuilder.loadTexts:qtechQoSPoliceMapTable.setStatus(_A)
_QtechQoSPoliceMapEntry_Object=MibTableRow
qtechQoSPoliceMapEntry=_QtechQoSPoliceMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,2,1))
qtechQoSPoliceMapEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechQoSPoliceMapEntry.setStatus(_A)
class _QtechQosPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechQosPoliceMapName_Type.__name__=_F
_QtechQosPoliceMapName_Object=MibTableColumn
qtechQosPoliceMapName=_QtechQosPoliceMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,2,1,1),_QtechQosPoliceMapName_Type())
qtechQosPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQosPoliceMapName.setStatus(_A)
_QtechQosPoliceMapEntryStatus_Type=ConfigStatus
_QtechQosPoliceMapEntryStatus_Object=MibTableColumn
qtechQosPoliceMapEntryStatus=_QtechQosPoliceMapEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,2,1,2),_QtechQosPoliceMapEntryStatus_Type())
qtechQosPoliceMapEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQosPoliceMapEntryStatus.setStatus(_A)
_QtechQoSPoliceMapConfTable_Object=MibTable
qtechQoSPoliceMapConfTable=_QtechQoSPoliceMapConfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3))
if mibBuilder.loadTexts:qtechQoSPoliceMapConfTable.setStatus(_A)
_QtechQoSPoliceMapConfEntry_Object=MibTableRow
qtechQoSPoliceMapConfEntry=_QtechQoSPoliceMapConfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1))
qtechQoSPoliceMapConfEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qtechQoSPoliceMapConfEntry.setStatus(_A)
class _QtechQoSPoliceCfgPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechQoSPoliceCfgPoliceMapName_Type.__name__=_F
_QtechQoSPoliceCfgPoliceMapName_Object=MibTableColumn
qtechQoSPoliceCfgPoliceMapName=_QtechQoSPoliceCfgPoliceMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,1),_QtechQoSPoliceCfgPoliceMapName_Type())
qtechQoSPoliceCfgPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSPoliceCfgPoliceMapName.setStatus(_A)
class _QtechQoSPoliceCfgClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechQoSPoliceCfgClassMapName_Type.__name__=_F
_QtechQoSPoliceCfgClassMapName_Object=MibTableColumn
qtechQoSPoliceCfgClassMapName=_QtechQoSPoliceCfgClassMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,2),_QtechQoSPoliceCfgClassMapName_Type())
qtechQoSPoliceCfgClassMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceCfgClassMapName.setStatus(_A)
_QtechQoSPoliceMapConfMaxBandWidth_Type=Unsigned32
_QtechQoSPoliceMapConfMaxBandWidth_Object=MibTableColumn
qtechQoSPoliceMapConfMaxBandWidth=_QtechQoSPoliceMapConfMaxBandWidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,3),_QtechQoSPoliceMapConfMaxBandWidth_Type())
qtechQoSPoliceMapConfMaxBandWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfMaxBandWidth.setStatus(_A)
_QtechQoSPoliceMapConfBurstFlowLimit_Type=Integer32
_QtechQoSPoliceMapConfBurstFlowLimit_Object=MibTableColumn
qtechQoSPoliceMapConfBurstFlowLimit=_QtechQoSPoliceMapConfBurstFlowLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,4),_QtechQoSPoliceMapConfBurstFlowLimit_Type())
qtechQoSPoliceMapConfBurstFlowLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfBurstFlowLimit.setStatus(_A)
class _QtechQoSPoliceMapConfExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('modify-dscp',2)))
_QtechQoSPoliceMapConfExceedAction_Type.__name__=_G
_QtechQoSPoliceMapConfExceedAction_Object=MibTableColumn
qtechQoSPoliceMapConfExceedAction=_QtechQoSPoliceMapConfExceedAction_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,5),_QtechQoSPoliceMapConfExceedAction_Type())
qtechQoSPoliceMapConfExceedAction.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfExceedAction.setStatus(_A)
_QtechQoSPoliceMapConfExceedDscp_Type=Integer32
_QtechQoSPoliceMapConfExceedDscp_Object=MibTableColumn
qtechQoSPoliceMapConfExceedDscp=_QtechQoSPoliceMapConfExceedDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,6),_QtechQoSPoliceMapConfExceedDscp_Type())
qtechQoSPoliceMapConfExceedDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfExceedDscp.setStatus(_A)
_QtechQoSPoliceMapConfNewDscp_Type=Integer32
_QtechQoSPoliceMapConfNewDscp_Object=MibTableColumn
qtechQoSPoliceMapConfNewDscp=_QtechQoSPoliceMapConfNewDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,7),_QtechQoSPoliceMapConfNewDscp_Type())
qtechQoSPoliceMapConfNewDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfNewDscp.setStatus(_A)
_QtechQoSPoliceMapCfgEntryStatus_Type=ConfigStatus
_QtechQoSPoliceMapCfgEntryStatus_Object=MibTableColumn
qtechQoSPoliceMapCfgEntryStatus=_QtechQoSPoliceMapCfgEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,8),_QtechQoSPoliceMapCfgEntryStatus_Type())
qtechQoSPoliceMapCfgEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapCfgEntryStatus.setStatus(_A)
_QtechQoSPoliceMapConfMaxHighBandWidth_Type=Unsigned32
_QtechQoSPoliceMapConfMaxHighBandWidth_Object=MibTableColumn
qtechQoSPoliceMapConfMaxHighBandWidth=_QtechQoSPoliceMapConfMaxHighBandWidth_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,3,1,9),_QtechQoSPoliceMapConfMaxHighBandWidth_Type())
qtechQoSPoliceMapConfMaxHighBandWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQoSPoliceMapConfMaxHighBandWidth.setStatus(_A)
_QtechQosPoliceIfExtTable_Object=MibTable
qtechQosPoliceIfExtTable=_QtechQosPoliceIfExtTable_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,5))
if mibBuilder.loadTexts:qtechQosPoliceIfExtTable.setStatus(_A)
_QtechQosPoliceIfExtEntry_Object=MibTableRow
qtechQosPoliceIfExtEntry=_QtechQosPoliceIfExtEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,5,1))
qtechQosPoliceIfExtEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qtechQosPoliceIfExtEntry.setStatus(_A)
_QtechQosPoliceIfIndex_Type=IfIndex
_QtechQosPoliceIfIndex_Object=MibTableColumn
qtechQosPoliceIfIndex=_QtechQosPoliceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,5,1,1),_QtechQosPoliceIfIndex_Type())
qtechQosPoliceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQosPoliceIfIndex.setStatus(_A)
class _QtechIfInPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechIfInPoliceMapName_Type.__name__=_F
_QtechIfInPoliceMapName_Object=MibTableColumn
qtechIfInPoliceMapName=_QtechIfInPoliceMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,5,1,2),_QtechIfInPoliceMapName_Type())
qtechIfInPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfInPoliceMapName.setStatus(_A)
class _QtechIfOutPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechIfOutPoliceMapName_Type.__name__=_F
_QtechIfOutPoliceMapName_Object=MibTableColumn
qtechIfOutPoliceMapName=_QtechIfOutPoliceMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,18,2,5,1,3),_QtechIfOutPoliceMapName_Type())
qtechIfOutPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIfOutPoliceMapName.setStatus(_A)
_QtechQoSMIBConformance_ObjectIdentity=ObjectIdentity
qtechQoSMIBConformance=_QtechQoSMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,18,3))
_QtechQoSMIBCompliances_ObjectIdentity=ObjectIdentity
qtechQoSMIBCompliances=_QtechQoSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,18,3,1))
_QtechQoSMIBGroups_ObjectIdentity=ObjectIdentity
qtechQoSMIBGroups=_QtechQoSMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,18,3,2))
qtechQoSPriorityMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,18,3,2,1))
qtechQoSPriorityMIBGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_H),(_B,_c),(_B,_d),(_B,_I),(_B,_e),(_B,_f),(_B,_g),(_B,_J),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_K),(_B,_l)))
if mibBuilder.loadTexts:qtechQoSPriorityMIBGroup.setStatus(_A)
qtechQoSTrafficClassMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,18,3,2,2))
qtechQoSTrafficClassMIBGroup.setObjects(*((_B,_L),(_B,_m),(_B,_n),(_B,_M),(_B,_o),(_B,_N),(_B,_O),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_P),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechQoSTrafficClassMIBGroup.setStatus(_A)
qtechQoSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,18,3,1,1))
qtechQoSMIBCompliance.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qtechQoSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechQoSMIB':qtechQoSMIB,'qtechQoSPriorityMIBObjects':qtechQoSPriorityMIBObjects,_Y:qtechQoSGlobalStatus,_Z:qtechPriorityTrafficClassNum,_a:qtechPriorityClassNum,_b:qtechPriorityDscpMaxValue,'qtechTrafficClassTable':qtechTrafficClassTable,'qtechTrafficClassEntry':qtechTrafficClassEntry,_H:qtechTrafficClassPriority,_c:qtechTrafficClass,_d:qtechPriorityToDscp,'qtechDscpClassTable':qtechDscpClassTable,'qtechDscpClassEntry':qtechDscpClassEntry,_I:qtechDscpClass,_e:qtechDscpTrafficClassPriority,_f:qtechPriorityTrafficClassOperMode,_g:qtechPriorityBandWidth,'qtechIfPriorityTable':qtechIfPriorityTable,'qtechIfPriorityEntry':qtechIfPriorityEntry,_J:qtechIfPriorityIfIndex,_h:qtechIfPriority,_i:qtechIfPriTrafficClassOperMode,_j:qtechIfPriorityBandwidth,_k:qtechIfPriorityQosTrustMode,'qtechIpPreClassTable':qtechIpPreClassTable,'qtechIpPreClassEntry':qtechIpPreClassEntry,_K:qtechIpPreClassPriority,_l:qtechIpPreToDscp,'qtechIfRateLimitTable':qtechIfRateLimitTable,'qtechIfRateLimitEntry':qtechIfRateLimitEntry,_T:qtechIfRateLimitIndex,'qtechIfRateLimitInMaxBandWidth':qtechIfRateLimitInMaxBandWidth,'qtechIfRateLimitInBurstFlowLimit':qtechIfRateLimitInBurstFlowLimit,'qtechIfRateLimitOutMaxBandWidth':qtechIfRateLimitOutMaxBandWidth,'qtechIfRateLimitOutBurstFlowLimit':qtechIfRateLimitOutBurstFlowLimit,'qtechIfQueueSupportTable':qtechIfQueueSupportTable,'qtechIfQueueSupportEntry':qtechIfQueueSupportEntry,_U:qtechIfIndex,_V:qtechIfQueueIndex,'qtechIfQueueSupportTransmitPacket':qtechIfQueueSupportTransmitPacket,'qtechIfQueueSupportTransmitBytes':qtechIfQueueSupportTransmitBytes,'qtechIfQueueSupportDropPacket':qtechIfQueueSupportDropPacket,'qtechIfQueueSupportDropBytes':qtechIfQueueSupportDropBytes,'qtechIfMulticastQueueSupportTable':qtechIfMulticastQueueSupportTable,'qtechIfMulticastQueueSupportEntry':qtechIfMulticastQueueSupportEntry,_W:qtechIfIndexMulticast,_X:qtechIfMulticastQueueIndex,'qtechIfMulticastQueueSupportTransmitPacket':qtechIfMulticastQueueSupportTransmitPacket,'qtechIfMulticastQueueSupportTransmitBytes':qtechIfMulticastQueueSupportTransmitBytes,'qtechIfMulticastQueueSupportDropPacket':qtechIfMulticastQueueSupportDropPacket,'qtechIfMulticastQueueSupportDropBytes':qtechIfMulticastQueueSupportDropBytes,'qtechQoSTrafficClassMIBObjects':qtechQoSTrafficClassMIBObjects,'qtechQoSTrafficClassTable':qtechQoSTrafficClassTable,'qtechQoSTrafficClassEntry':qtechQoSTrafficClassEntry,_L:qtechQosClassMapName,_m:qtechQosClassAclName,_n:qtechQosClassMapEntryStatus,'qtechQoSPoliceMapTable':qtechQoSPoliceMapTable,'qtechQoSPoliceMapEntry':qtechQoSPoliceMapEntry,_M:qtechQosPoliceMapName,_o:qtechQosPoliceMapEntryStatus,'qtechQoSPoliceMapConfTable':qtechQoSPoliceMapConfTable,'qtechQoSPoliceMapConfEntry':qtechQoSPoliceMapConfEntry,_N:qtechQoSPoliceCfgPoliceMapName,_O:qtechQoSPoliceCfgClassMapName,_p:qtechQoSPoliceMapConfMaxBandWidth,'qtechQoSPoliceMapConfBurstFlowLimit':qtechQoSPoliceMapConfBurstFlowLimit,_q:qtechQoSPoliceMapConfExceedAction,_r:qtechQoSPoliceMapConfExceedDscp,_s:qtechQoSPoliceMapConfNewDscp,_t:qtechQoSPoliceMapCfgEntryStatus,_u:qtechQoSPoliceMapConfMaxHighBandWidth,'qtechQosPoliceIfExtTable':qtechQosPoliceIfExtTable,'qtechQosPoliceIfExtEntry':qtechQosPoliceIfExtEntry,_P:qtechQosPoliceIfIndex,_v:qtechIfInPoliceMapName,_w:qtechIfOutPoliceMapName,'qtechQoSMIBConformance':qtechQoSMIBConformance,'qtechQoSMIBCompliances':qtechQoSMIBCompliances,'qtechQoSMIBCompliance':qtechQoSMIBCompliance,'qtechQoSMIBGroups':qtechQoSMIBGroups,_x:qtechQoSPriorityMIBGroup,_y:qtechQoSTrafficClassMIBGroup})