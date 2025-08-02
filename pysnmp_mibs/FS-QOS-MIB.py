_A0='fsQoSTrafficClassMIBGroup'
_z='fsQoSPriorityMIBGroup'
_y='fsIfOutPoliceMapName'
_x='fsIfInPoliceMapName'
_w='fsQoSPoliceMapConfMaxHighBandWidth'
_v='fsQoSPoliceMapCfgEntryStatus'
_u='fsQoSPoliceMapConfNewDscp'
_t='fsQoSPoliceMapConfExceedDscp'
_s='fsQoSPoliceMapConfExceedAction'
_r='fsQoSPoliceMapConfMaxBandWidth'
_q='fsQosPoliceMapEntryStatus'
_p='fsQosClassMapEntryStatus'
_o='fsQosClassAclName'
_n='fsIpPreToDscp'
_m='fsIfPriorityQosTrustMode'
_l='fsIfPriorityBandwidth'
_k='fsIfPriTrafficClassOperMode'
_j='fsIfPriority'
_i='fsPriorityBandWidth'
_h='fsPriorityTrafficClassOperMode'
_g='fsDscpTrafficClassPriority'
_f='fsPriorityToDscp'
_e='fsTrafficClass'
_d='fsPriorityDscpMaxValue'
_c='fsPriorityClassNum'
_b='fsPriorityTrafficClassNum'
_a='fsQoSGlobalStatus'
_Z='fsWredEcnStatsIfIndex'
_Y='fsIfMulticastQueueIndex'
_X='fsIfIndexMulticast'
_W='fsIfQueueIndex'
_V='fsIfIndex'
_U='fsIfRateLimitIndex'
_T='qos-drr'
_S='qos-wrr'
_R='qos-sp'
_Q='fsQosPoliceIfIndex'
_P='fsQoSPoliceCfgClassMapName'
_O='fsQoSPoliceCfgPoliceMapName'
_N='fsQosPoliceMapName'
_M='fsQosClassMapName'
_L='fsIpPreClassPriority'
_K='fsIfPriorityIfIndex'
_J='fsDscpClass'
_I='fsTrafficClassPriority'
_H='Counter64'
_G='Integer32'
_F='DisplayString'
_E='read-create'
_D='read-write'
_C='read-only'
_B='FS-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_H,'Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
fsQoSMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,18))
if mibBuilder.loadTexts:fsQoSMIB.setRevisions(('2002-03-20 00:00',))
_FsQoSPriorityMIBObjects_ObjectIdentity=ObjectIdentity
fsQoSPriorityMIBObjects=_FsQoSPriorityMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,18,1))
_FsQoSGlobalStatus_Type=EnabledStatus
_FsQoSGlobalStatus_Object=MibScalar
fsQoSGlobalStatus=_FsQoSGlobalStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,1),_FsQoSGlobalStatus_Type())
fsQoSGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsQoSGlobalStatus.setStatus(_A)
_FsPriorityTrafficClassNum_Type=Integer32
_FsPriorityTrafficClassNum_Object=MibScalar
fsPriorityTrafficClassNum=_FsPriorityTrafficClassNum_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,2),_FsPriorityTrafficClassNum_Type())
fsPriorityTrafficClassNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPriorityTrafficClassNum.setStatus(_A)
_FsPriorityClassNum_Type=Integer32
_FsPriorityClassNum_Object=MibScalar
fsPriorityClassNum=_FsPriorityClassNum_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,3),_FsPriorityClassNum_Type())
fsPriorityClassNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPriorityClassNum.setStatus(_A)
_FsPriorityDscpMaxValue_Type=Integer32
_FsPriorityDscpMaxValue_Object=MibScalar
fsPriorityDscpMaxValue=_FsPriorityDscpMaxValue_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,4),_FsPriorityDscpMaxValue_Type())
fsPriorityDscpMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPriorityDscpMaxValue.setStatus(_A)
_FsTrafficClassTable_Object=MibTable
fsTrafficClassTable=_FsTrafficClassTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,5))
if mibBuilder.loadTexts:fsTrafficClassTable.setStatus(_A)
_FsTrafficClassEntry_Object=MibTableRow
fsTrafficClassEntry=_FsTrafficClassEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,5,1))
fsTrafficClassEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsTrafficClassEntry.setStatus(_A)
_FsTrafficClassPriority_Type=Integer32
_FsTrafficClassPriority_Object=MibTableColumn
fsTrafficClassPriority=_FsTrafficClassPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,5,1,1),_FsTrafficClassPriority_Type())
fsTrafficClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrafficClassPriority.setStatus(_A)
_FsTrafficClass_Type=Integer32
_FsTrafficClass_Object=MibTableColumn
fsTrafficClass=_FsTrafficClass_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,5,1,2),_FsTrafficClass_Type())
fsTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTrafficClass.setStatus(_A)
_FsPriorityToDscp_Type=Integer32
_FsPriorityToDscp_Object=MibTableColumn
fsPriorityToDscp=_FsPriorityToDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,5,1,3),_FsPriorityToDscp_Type())
fsPriorityToDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPriorityToDscp.setStatus(_A)
_FsDscpClassTable_Object=MibTable
fsDscpClassTable=_FsDscpClassTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,6))
if mibBuilder.loadTexts:fsDscpClassTable.setStatus(_A)
_FsDscpClassEntry_Object=MibTableRow
fsDscpClassEntry=_FsDscpClassEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,6,1))
fsDscpClassEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsDscpClassEntry.setStatus(_A)
_FsDscpClass_Type=Integer32
_FsDscpClass_Object=MibTableColumn
fsDscpClass=_FsDscpClass_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,6,1,1),_FsDscpClass_Type())
fsDscpClass.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDscpClass.setStatus(_A)
_FsDscpTrafficClassPriority_Type=Integer32
_FsDscpTrafficClassPriority_Object=MibTableColumn
fsDscpTrafficClassPriority=_FsDscpTrafficClassPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,6,1,2),_FsDscpTrafficClassPriority_Type())
fsDscpTrafficClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDscpTrafficClassPriority.setStatus(_A)
class _FsPriorityTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_FsPriorityTrafficClassOperMode_Type.__name__=_G
_FsPriorityTrafficClassOperMode_Object=MibScalar
fsPriorityTrafficClassOperMode=_FsPriorityTrafficClassOperMode_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,7),_FsPriorityTrafficClassOperMode_Type())
fsPriorityTrafficClassOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPriorityTrafficClassOperMode.setStatus(_A)
_FsPriorityBandWidth_Type=OctetString
_FsPriorityBandWidth_Object=MibScalar
fsPriorityBandWidth=_FsPriorityBandWidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,8),_FsPriorityBandWidth_Type())
fsPriorityBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPriorityBandWidth.setStatus(_A)
_FsIfPriorityTable_Object=MibTable
fsIfPriorityTable=_FsIfPriorityTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9))
if mibBuilder.loadTexts:fsIfPriorityTable.setStatus(_A)
_FsIfPriorityEntry_Object=MibTableRow
fsIfPriorityEntry=_FsIfPriorityEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1))
fsIfPriorityEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsIfPriorityEntry.setStatus(_A)
_FsIfPriorityIfIndex_Type=IfIndex
_FsIfPriorityIfIndex_Object=MibTableColumn
fsIfPriorityIfIndex=_FsIfPriorityIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1,1),_FsIfPriorityIfIndex_Type())
fsIfPriorityIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfPriorityIfIndex.setStatus(_A)
_FsIfPriority_Type=Integer32
_FsIfPriority_Object=MibTableColumn
fsIfPriority=_FsIfPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1,2),_FsIfPriority_Type())
fsIfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfPriority.setStatus(_A)
class _FsIfPriTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_FsIfPriTrafficClassOperMode_Type.__name__=_G
_FsIfPriTrafficClassOperMode_Object=MibTableColumn
fsIfPriTrafficClassOperMode=_FsIfPriTrafficClassOperMode_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1,3),_FsIfPriTrafficClassOperMode_Type())
fsIfPriTrafficClassOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfPriTrafficClassOperMode.setStatus(_A)
_FsIfPriorityBandwidth_Type=OctetString
_FsIfPriorityBandwidth_Object=MibTableColumn
fsIfPriorityBandwidth=_FsIfPriorityBandwidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1,4),_FsIfPriorityBandwidth_Type())
fsIfPriorityBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfPriorityBandwidth.setStatus(_A)
class _FsIfPriorityQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-trust',1),('trust-cos',2),('trust-dscp',3),('trust-ip-precedence',4)))
_FsIfPriorityQosTrustMode_Type.__name__=_G
_FsIfPriorityQosTrustMode_Object=MibTableColumn
fsIfPriorityQosTrustMode=_FsIfPriorityQosTrustMode_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,9,1,5),_FsIfPriorityQosTrustMode_Type())
fsIfPriorityQosTrustMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfPriorityQosTrustMode.setStatus(_A)
_FsIpPreClassTable_Object=MibTable
fsIpPreClassTable=_FsIpPreClassTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,10))
if mibBuilder.loadTexts:fsIpPreClassTable.setStatus(_A)
_FsIpPreClassEntry_Object=MibTableRow
fsIpPreClassEntry=_FsIpPreClassEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,10,1))
fsIpPreClassEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsIpPreClassEntry.setStatus(_A)
_FsIpPreClassPriority_Type=Integer32
_FsIpPreClassPriority_Object=MibTableColumn
fsIpPreClassPriority=_FsIpPreClassPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,10,1,1),_FsIpPreClassPriority_Type())
fsIpPreClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPreClassPriority.setStatus(_A)
_FsIpPreToDscp_Type=Integer32
_FsIpPreToDscp_Object=MibTableColumn
fsIpPreToDscp=_FsIpPreToDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,10,1,2),_FsIpPreToDscp_Type())
fsIpPreToDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpPreToDscp.setStatus(_A)
_FsIfRateLimitTable_Object=MibTable
fsIfRateLimitTable=_FsIfRateLimitTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11))
if mibBuilder.loadTexts:fsIfRateLimitTable.setStatus(_A)
_FsIfRateLimitEntry_Object=MibTableRow
fsIfRateLimitEntry=_FsIfRateLimitEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1))
fsIfRateLimitEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:fsIfRateLimitEntry.setStatus(_A)
_FsIfRateLimitIndex_Type=IfIndex
_FsIfRateLimitIndex_Object=MibTableColumn
fsIfRateLimitIndex=_FsIfRateLimitIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1,1),_FsIfRateLimitIndex_Type())
fsIfRateLimitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfRateLimitIndex.setStatus(_A)
_FsIfRateLimitInMaxBandWidth_Type=Unsigned32
_FsIfRateLimitInMaxBandWidth_Object=MibTableColumn
fsIfRateLimitInMaxBandWidth=_FsIfRateLimitInMaxBandWidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1,2),_FsIfRateLimitInMaxBandWidth_Type())
fsIfRateLimitInMaxBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfRateLimitInMaxBandWidth.setStatus(_A)
_FsIfRateLimitInBurstFlowLimit_Type=Integer32
_FsIfRateLimitInBurstFlowLimit_Object=MibTableColumn
fsIfRateLimitInBurstFlowLimit=_FsIfRateLimitInBurstFlowLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1,3),_FsIfRateLimitInBurstFlowLimit_Type())
fsIfRateLimitInBurstFlowLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfRateLimitInBurstFlowLimit.setStatus(_A)
_FsIfRateLimitOutMaxBandWidth_Type=Unsigned32
_FsIfRateLimitOutMaxBandWidth_Object=MibTableColumn
fsIfRateLimitOutMaxBandWidth=_FsIfRateLimitOutMaxBandWidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1,4),_FsIfRateLimitOutMaxBandWidth_Type())
fsIfRateLimitOutMaxBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfRateLimitOutMaxBandWidth.setStatus(_A)
_FsIfRateLimitOutBurstFlowLimit_Type=Integer32
_FsIfRateLimitOutBurstFlowLimit_Object=MibTableColumn
fsIfRateLimitOutBurstFlowLimit=_FsIfRateLimitOutBurstFlowLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,11,1,5),_FsIfRateLimitOutBurstFlowLimit_Type())
fsIfRateLimitOutBurstFlowLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfRateLimitOutBurstFlowLimit.setStatus(_A)
_FsIfQueueSupportTable_Object=MibTable
fsIfQueueSupportTable=_FsIfQueueSupportTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12))
if mibBuilder.loadTexts:fsIfQueueSupportTable.setStatus(_A)
_FsIfQueueSupportEntry_Object=MibTableRow
fsIfQueueSupportEntry=_FsIfQueueSupportEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1))
fsIfQueueSupportEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:fsIfQueueSupportEntry.setStatus(_A)
_FsIfIndex_Type=IfIndex
_FsIfIndex_Object=MibTableColumn
fsIfIndex=_FsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,1),_FsIfIndex_Type())
fsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfIndex.setStatus(_A)
_FsIfQueueIndex_Type=Integer32
_FsIfQueueIndex_Object=MibTableColumn
fsIfQueueIndex=_FsIfQueueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,2),_FsIfQueueIndex_Type())
fsIfQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfQueueIndex.setStatus(_A)
_FsIfQueueSupportTransmitPacket_Type=Counter64
_FsIfQueueSupportTransmitPacket_Object=MibTableColumn
fsIfQueueSupportTransmitPacket=_FsIfQueueSupportTransmitPacket_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,3),_FsIfQueueSupportTransmitPacket_Type())
fsIfQueueSupportTransmitPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfQueueSupportTransmitPacket.setStatus(_A)
_FsIfQueueSupportTransmitBytes_Type=Counter64
_FsIfQueueSupportTransmitBytes_Object=MibTableColumn
fsIfQueueSupportTransmitBytes=_FsIfQueueSupportTransmitBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,4),_FsIfQueueSupportTransmitBytes_Type())
fsIfQueueSupportTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfQueueSupportTransmitBytes.setStatus(_A)
_FsIfQueueSupportDropPacket_Type=Counter64
_FsIfQueueSupportDropPacket_Object=MibTableColumn
fsIfQueueSupportDropPacket=_FsIfQueueSupportDropPacket_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,5),_FsIfQueueSupportDropPacket_Type())
fsIfQueueSupportDropPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfQueueSupportDropPacket.setStatus(_A)
_FsIfQueueSupportDropBytes_Type=Counter64
_FsIfQueueSupportDropBytes_Object=MibTableColumn
fsIfQueueSupportDropBytes=_FsIfQueueSupportDropBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,12,1,6),_FsIfQueueSupportDropBytes_Type())
fsIfQueueSupportDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfQueueSupportDropBytes.setStatus(_A)
_FsIfMulticastQueueSupportTable_Object=MibTable
fsIfMulticastQueueSupportTable=_FsIfMulticastQueueSupportTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13))
if mibBuilder.loadTexts:fsIfMulticastQueueSupportTable.setStatus(_A)
_FsIfMulticastQueueSupportEntry_Object=MibTableRow
fsIfMulticastQueueSupportEntry=_FsIfMulticastQueueSupportEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1))
fsIfMulticastQueueSupportEntry.setIndexNames((0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:fsIfMulticastQueueSupportEntry.setStatus(_A)
_FsIfIndexMulticast_Type=IfIndex
_FsIfIndexMulticast_Object=MibTableColumn
fsIfIndexMulticast=_FsIfIndexMulticast_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,1),_FsIfIndexMulticast_Type())
fsIfIndexMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfIndexMulticast.setStatus(_A)
_FsIfMulticastQueueIndex_Type=Integer32
_FsIfMulticastQueueIndex_Object=MibTableColumn
fsIfMulticastQueueIndex=_FsIfMulticastQueueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,2),_FsIfMulticastQueueIndex_Type())
fsIfMulticastQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfMulticastQueueIndex.setStatus(_A)
_FsIfMulticastQueueSupportTransmitPacket_Type=Counter64
_FsIfMulticastQueueSupportTransmitPacket_Object=MibTableColumn
fsIfMulticastQueueSupportTransmitPacket=_FsIfMulticastQueueSupportTransmitPacket_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,3),_FsIfMulticastQueueSupportTransmitPacket_Type())
fsIfMulticastQueueSupportTransmitPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfMulticastQueueSupportTransmitPacket.setStatus(_A)
_FsIfMulticastQueueSupportTransmitBytes_Type=Counter64
_FsIfMulticastQueueSupportTransmitBytes_Object=MibTableColumn
fsIfMulticastQueueSupportTransmitBytes=_FsIfMulticastQueueSupportTransmitBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,4),_FsIfMulticastQueueSupportTransmitBytes_Type())
fsIfMulticastQueueSupportTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfMulticastQueueSupportTransmitBytes.setStatus(_A)
_FsIfMulticastQueueSupportDropPacket_Type=Counter64
_FsIfMulticastQueueSupportDropPacket_Object=MibTableColumn
fsIfMulticastQueueSupportDropPacket=_FsIfMulticastQueueSupportDropPacket_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,5),_FsIfMulticastQueueSupportDropPacket_Type())
fsIfMulticastQueueSupportDropPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfMulticastQueueSupportDropPacket.setStatus(_A)
_FsIfMulticastQueueSupportDropBytes_Type=Counter64
_FsIfMulticastQueueSupportDropBytes_Object=MibTableColumn
fsIfMulticastQueueSupportDropBytes=_FsIfMulticastQueueSupportDropBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,13,1,6),_FsIfMulticastQueueSupportDropBytes_Type())
fsIfMulticastQueueSupportDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIfMulticastQueueSupportDropBytes.setStatus(_A)
_FsWredEcnStatsTable_Object=MibTable
fsWredEcnStatsTable=_FsWredEcnStatsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,14))
if mibBuilder.loadTexts:fsWredEcnStatsTable.setStatus(_A)
_FsWredEcnStatsEntry_Object=MibTableRow
fsWredEcnStatsEntry=_FsWredEcnStatsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,14,1))
fsWredEcnStatsEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:fsWredEcnStatsEntry.setStatus(_A)
_FsWredEcnStatsIfIndex_Type=Unsigned32
_FsWredEcnStatsIfIndex_Object=MibTableColumn
fsWredEcnStatsIfIndex=_FsWredEcnStatsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,14,1,1),_FsWredEcnStatsIfIndex_Type())
fsWredEcnStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWredEcnStatsIfIndex.setStatus(_A)
class _FsWredDropped_Type(Counter64):defaultValue=0
_FsWredDropped_Type.__name__=_H
_FsWredDropped_Object=MibTableColumn
fsWredDropped=_FsWredDropped_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,14,1,2),_FsWredDropped_Type())
fsWredDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWredDropped.setStatus(_A)
class _FsEcnSended_Type(Counter64):defaultValue=0
_FsEcnSended_Type.__name__=_H
_FsEcnSended_Object=MibTableColumn
fsEcnSended=_FsEcnSended_Object((1,3,6,1,4,1,52642,1,1,10,2,18,1,14,1,3),_FsEcnSended_Type())
fsEcnSended.setMaxAccess(_C)
if mibBuilder.loadTexts:fsEcnSended.setStatus(_A)
_FsQoSTrafficClassMIBObjects_ObjectIdentity=ObjectIdentity
fsQoSTrafficClassMIBObjects=_FsQoSTrafficClassMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,18,2))
_FsQoSTrafficClassTable_Object=MibTable
fsQoSTrafficClassTable=_FsQoSTrafficClassTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,1))
if mibBuilder.loadTexts:fsQoSTrafficClassTable.setStatus(_A)
_FsQoSTrafficClassEntry_Object=MibTableRow
fsQoSTrafficClassEntry=_FsQoSTrafficClassEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,1,1))
fsQoSTrafficClassEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:fsQoSTrafficClassEntry.setStatus(_A)
class _FsQosClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsQosClassMapName_Type.__name__=_F
_FsQosClassMapName_Object=MibTableColumn
fsQosClassMapName=_FsQosClassMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,1,1,1),_FsQosClassMapName_Type())
fsQosClassMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQosClassMapName.setStatus(_A)
class _FsQosClassAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsQosClassAclName_Type.__name__=_F
_FsQosClassAclName_Object=MibTableColumn
fsQosClassAclName=_FsQosClassAclName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,1,1,2),_FsQosClassAclName_Type())
fsQosClassAclName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQosClassAclName.setStatus(_A)
_FsQosClassMapEntryStatus_Type=ConfigStatus
_FsQosClassMapEntryStatus_Object=MibTableColumn
fsQosClassMapEntryStatus=_FsQosClassMapEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,1,1,3),_FsQosClassMapEntryStatus_Type())
fsQosClassMapEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQosClassMapEntryStatus.setStatus(_A)
_FsQoSPoliceMapTable_Object=MibTable
fsQoSPoliceMapTable=_FsQoSPoliceMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,2))
if mibBuilder.loadTexts:fsQoSPoliceMapTable.setStatus(_A)
_FsQoSPoliceMapEntry_Object=MibTableRow
fsQoSPoliceMapEntry=_FsQoSPoliceMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,2,1))
fsQoSPoliceMapEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsQoSPoliceMapEntry.setStatus(_A)
class _FsQosPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsQosPoliceMapName_Type.__name__=_F
_FsQosPoliceMapName_Object=MibTableColumn
fsQosPoliceMapName=_FsQosPoliceMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,2,1,1),_FsQosPoliceMapName_Type())
fsQosPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQosPoliceMapName.setStatus(_A)
_FsQosPoliceMapEntryStatus_Type=ConfigStatus
_FsQosPoliceMapEntryStatus_Object=MibTableColumn
fsQosPoliceMapEntryStatus=_FsQosPoliceMapEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,2,1,2),_FsQosPoliceMapEntryStatus_Type())
fsQosPoliceMapEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQosPoliceMapEntryStatus.setStatus(_A)
_FsQoSPoliceMapConfTable_Object=MibTable
fsQoSPoliceMapConfTable=_FsQoSPoliceMapConfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3))
if mibBuilder.loadTexts:fsQoSPoliceMapConfTable.setStatus(_A)
_FsQoSPoliceMapConfEntry_Object=MibTableRow
fsQoSPoliceMapConfEntry=_FsQoSPoliceMapConfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1))
fsQoSPoliceMapConfEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsQoSPoliceMapConfEntry.setStatus(_A)
class _FsQoSPoliceCfgPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsQoSPoliceCfgPoliceMapName_Type.__name__=_F
_FsQoSPoliceCfgPoliceMapName_Object=MibTableColumn
fsQoSPoliceCfgPoliceMapName=_FsQoSPoliceCfgPoliceMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,1),_FsQoSPoliceCfgPoliceMapName_Type())
fsQoSPoliceCfgPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSPoliceCfgPoliceMapName.setStatus(_A)
class _FsQoSPoliceCfgClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsQoSPoliceCfgClassMapName_Type.__name__=_F
_FsQoSPoliceCfgClassMapName_Object=MibTableColumn
fsQoSPoliceCfgClassMapName=_FsQoSPoliceCfgClassMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,2),_FsQoSPoliceCfgClassMapName_Type())
fsQoSPoliceCfgClassMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceCfgClassMapName.setStatus(_A)
_FsQoSPoliceMapConfMaxBandWidth_Type=Unsigned32
_FsQoSPoliceMapConfMaxBandWidth_Object=MibTableColumn
fsQoSPoliceMapConfMaxBandWidth=_FsQoSPoliceMapConfMaxBandWidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,3),_FsQoSPoliceMapConfMaxBandWidth_Type())
fsQoSPoliceMapConfMaxBandWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfMaxBandWidth.setStatus(_A)
_FsQoSPoliceMapConfBurstFlowLimit_Type=Integer32
_FsQoSPoliceMapConfBurstFlowLimit_Object=MibTableColumn
fsQoSPoliceMapConfBurstFlowLimit=_FsQoSPoliceMapConfBurstFlowLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,4),_FsQoSPoliceMapConfBurstFlowLimit_Type())
fsQoSPoliceMapConfBurstFlowLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfBurstFlowLimit.setStatus(_A)
class _FsQoSPoliceMapConfExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('modify-dscp',2)))
_FsQoSPoliceMapConfExceedAction_Type.__name__=_G
_FsQoSPoliceMapConfExceedAction_Object=MibTableColumn
fsQoSPoliceMapConfExceedAction=_FsQoSPoliceMapConfExceedAction_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,5),_FsQoSPoliceMapConfExceedAction_Type())
fsQoSPoliceMapConfExceedAction.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfExceedAction.setStatus(_A)
_FsQoSPoliceMapConfExceedDscp_Type=Integer32
_FsQoSPoliceMapConfExceedDscp_Object=MibTableColumn
fsQoSPoliceMapConfExceedDscp=_FsQoSPoliceMapConfExceedDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,6),_FsQoSPoliceMapConfExceedDscp_Type())
fsQoSPoliceMapConfExceedDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfExceedDscp.setStatus(_A)
_FsQoSPoliceMapConfNewDscp_Type=Integer32
_FsQoSPoliceMapConfNewDscp_Object=MibTableColumn
fsQoSPoliceMapConfNewDscp=_FsQoSPoliceMapConfNewDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,7),_FsQoSPoliceMapConfNewDscp_Type())
fsQoSPoliceMapConfNewDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfNewDscp.setStatus(_A)
_FsQoSPoliceMapCfgEntryStatus_Type=ConfigStatus
_FsQoSPoliceMapCfgEntryStatus_Object=MibTableColumn
fsQoSPoliceMapCfgEntryStatus=_FsQoSPoliceMapCfgEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,8),_FsQoSPoliceMapCfgEntryStatus_Type())
fsQoSPoliceMapCfgEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapCfgEntryStatus.setStatus(_A)
_FsQoSPoliceMapConfMaxHighBandWidth_Type=Unsigned32
_FsQoSPoliceMapConfMaxHighBandWidth_Object=MibTableColumn
fsQoSPoliceMapConfMaxHighBandWidth=_FsQoSPoliceMapConfMaxHighBandWidth_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,3,1,9),_FsQoSPoliceMapConfMaxHighBandWidth_Type())
fsQoSPoliceMapConfMaxHighBandWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQoSPoliceMapConfMaxHighBandWidth.setStatus(_A)
_FsQosPoliceIfExtTable_Object=MibTable
fsQosPoliceIfExtTable=_FsQosPoliceIfExtTable_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,5))
if mibBuilder.loadTexts:fsQosPoliceIfExtTable.setStatus(_A)
_FsQosPoliceIfExtEntry_Object=MibTableRow
fsQosPoliceIfExtEntry=_FsQosPoliceIfExtEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,5,1))
fsQosPoliceIfExtEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:fsQosPoliceIfExtEntry.setStatus(_A)
_FsQosPoliceIfIndex_Type=IfIndex
_FsQosPoliceIfIndex_Object=MibTableColumn
fsQosPoliceIfIndex=_FsQosPoliceIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,5,1,1),_FsQosPoliceIfIndex_Type())
fsQosPoliceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQosPoliceIfIndex.setStatus(_A)
class _FsIfInPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIfInPoliceMapName_Type.__name__=_F
_FsIfInPoliceMapName_Object=MibTableColumn
fsIfInPoliceMapName=_FsIfInPoliceMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,5,1,2),_FsIfInPoliceMapName_Type())
fsIfInPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfInPoliceMapName.setStatus(_A)
class _FsIfOutPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIfOutPoliceMapName_Type.__name__=_F
_FsIfOutPoliceMapName_Object=MibTableColumn
fsIfOutPoliceMapName=_FsIfOutPoliceMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,18,2,5,1,3),_FsIfOutPoliceMapName_Type())
fsIfOutPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIfOutPoliceMapName.setStatus(_A)
_FsQoSMIBConformance_ObjectIdentity=ObjectIdentity
fsQoSMIBConformance=_FsQoSMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,18,3))
_FsQoSMIBCompliances_ObjectIdentity=ObjectIdentity
fsQoSMIBCompliances=_FsQoSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,18,3,1))
_FsQoSMIBGroups_ObjectIdentity=ObjectIdentity
fsQoSMIBGroups=_FsQoSMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,18,3,2))
fsQoSPriorityMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,18,3,2,1))
fsQoSPriorityMIBGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_I),(_B,_e),(_B,_f),(_B,_J),(_B,_g),(_B,_h),(_B,_i),(_B,_K),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_L),(_B,_n)))
if mibBuilder.loadTexts:fsQoSPriorityMIBGroup.setStatus(_A)
fsQoSTrafficClassMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,18,3,2,2))
fsQoSTrafficClassMIBGroup.setObjects(*((_B,_M),(_B,_o),(_B,_p),(_B,_N),(_B,_q),(_B,_O),(_B,_P),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_Q),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:fsQoSTrafficClassMIBGroup.setStatus(_A)
fsQoSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,18,3,1,1))
fsQoSMIBCompliance.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:fsQoSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsQoSMIB':fsQoSMIB,'fsQoSPriorityMIBObjects':fsQoSPriorityMIBObjects,_a:fsQoSGlobalStatus,_b:fsPriorityTrafficClassNum,_c:fsPriorityClassNum,_d:fsPriorityDscpMaxValue,'fsTrafficClassTable':fsTrafficClassTable,'fsTrafficClassEntry':fsTrafficClassEntry,_I:fsTrafficClassPriority,_e:fsTrafficClass,_f:fsPriorityToDscp,'fsDscpClassTable':fsDscpClassTable,'fsDscpClassEntry':fsDscpClassEntry,_J:fsDscpClass,_g:fsDscpTrafficClassPriority,_h:fsPriorityTrafficClassOperMode,_i:fsPriorityBandWidth,'fsIfPriorityTable':fsIfPriorityTable,'fsIfPriorityEntry':fsIfPriorityEntry,_K:fsIfPriorityIfIndex,_j:fsIfPriority,_k:fsIfPriTrafficClassOperMode,_l:fsIfPriorityBandwidth,_m:fsIfPriorityQosTrustMode,'fsIpPreClassTable':fsIpPreClassTable,'fsIpPreClassEntry':fsIpPreClassEntry,_L:fsIpPreClassPriority,_n:fsIpPreToDscp,'fsIfRateLimitTable':fsIfRateLimitTable,'fsIfRateLimitEntry':fsIfRateLimitEntry,_U:fsIfRateLimitIndex,'fsIfRateLimitInMaxBandWidth':fsIfRateLimitInMaxBandWidth,'fsIfRateLimitInBurstFlowLimit':fsIfRateLimitInBurstFlowLimit,'fsIfRateLimitOutMaxBandWidth':fsIfRateLimitOutMaxBandWidth,'fsIfRateLimitOutBurstFlowLimit':fsIfRateLimitOutBurstFlowLimit,'fsIfQueueSupportTable':fsIfQueueSupportTable,'fsIfQueueSupportEntry':fsIfQueueSupportEntry,_V:fsIfIndex,_W:fsIfQueueIndex,'fsIfQueueSupportTransmitPacket':fsIfQueueSupportTransmitPacket,'fsIfQueueSupportTransmitBytes':fsIfQueueSupportTransmitBytes,'fsIfQueueSupportDropPacket':fsIfQueueSupportDropPacket,'fsIfQueueSupportDropBytes':fsIfQueueSupportDropBytes,'fsIfMulticastQueueSupportTable':fsIfMulticastQueueSupportTable,'fsIfMulticastQueueSupportEntry':fsIfMulticastQueueSupportEntry,_X:fsIfIndexMulticast,_Y:fsIfMulticastQueueIndex,'fsIfMulticastQueueSupportTransmitPacket':fsIfMulticastQueueSupportTransmitPacket,'fsIfMulticastQueueSupportTransmitBytes':fsIfMulticastQueueSupportTransmitBytes,'fsIfMulticastQueueSupportDropPacket':fsIfMulticastQueueSupportDropPacket,'fsIfMulticastQueueSupportDropBytes':fsIfMulticastQueueSupportDropBytes,'fsWredEcnStatsTable':fsWredEcnStatsTable,'fsWredEcnStatsEntry':fsWredEcnStatsEntry,_Z:fsWredEcnStatsIfIndex,'fsWredDropped':fsWredDropped,'fsEcnSended':fsEcnSended,'fsQoSTrafficClassMIBObjects':fsQoSTrafficClassMIBObjects,'fsQoSTrafficClassTable':fsQoSTrafficClassTable,'fsQoSTrafficClassEntry':fsQoSTrafficClassEntry,_M:fsQosClassMapName,_o:fsQosClassAclName,_p:fsQosClassMapEntryStatus,'fsQoSPoliceMapTable':fsQoSPoliceMapTable,'fsQoSPoliceMapEntry':fsQoSPoliceMapEntry,_N:fsQosPoliceMapName,_q:fsQosPoliceMapEntryStatus,'fsQoSPoliceMapConfTable':fsQoSPoliceMapConfTable,'fsQoSPoliceMapConfEntry':fsQoSPoliceMapConfEntry,_O:fsQoSPoliceCfgPoliceMapName,_P:fsQoSPoliceCfgClassMapName,_r:fsQoSPoliceMapConfMaxBandWidth,'fsQoSPoliceMapConfBurstFlowLimit':fsQoSPoliceMapConfBurstFlowLimit,_s:fsQoSPoliceMapConfExceedAction,_t:fsQoSPoliceMapConfExceedDscp,_u:fsQoSPoliceMapConfNewDscp,_v:fsQoSPoliceMapCfgEntryStatus,_w:fsQoSPoliceMapConfMaxHighBandWidth,'fsQosPoliceIfExtTable':fsQosPoliceIfExtTable,'fsQosPoliceIfExtEntry':fsQosPoliceIfExtEntry,_Q:fsQosPoliceIfIndex,_x:fsIfInPoliceMapName,_y:fsIfOutPoliceMapName,'fsQoSMIBConformance':fsQoSMIBConformance,'fsQoSMIBCompliances':fsQoSMIBCompliances,'fsQoSMIBCompliance':fsQoSMIBCompliance,'fsQoSMIBGroups':fsQoSMIBGroups,_z:fsQoSPriorityMIBGroup,_A0:fsQoSTrafficClassMIBGroup})