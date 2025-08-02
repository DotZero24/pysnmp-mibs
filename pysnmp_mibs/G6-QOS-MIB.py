_O='rateShapingPortIndex'
_N='diffservPrioMappingIndex'
_M='ieee802dot1pPrioMappingIndex'
_L='configPortIndex'
_K='not-accessible'
_J='enabled'
_I='G6-QOS-MIB'
_H='disabled'
_G='queue3'
_F='queue2'
_E='queue1'
_D='queue0'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Qos_ObjectIdentity=ObjectIdentity
qos=_Qos_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,83))
class _QosEnableQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_QosEnableQos_Type.__name__=_B
_QosEnableQos_Object=MibScalar
qosEnableQos=_QosEnableQos_Object((1,3,6,1,4,1,3181,10,6,2,83,1),_QosEnableQos_Type())
qosEnableQos.setMaxAccess(_C)
if mibBuilder.loadTexts:qosEnableQos.setStatus(_A)
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,83,2))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1))
configEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_ConfigPortIndex_Type.__name__=_B
_ConfigPortIndex_Object=MibTableColumn
configPortIndex=_ConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,1),_ConfigPortIndex_Type())
configPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:configPortIndex.setStatus(_A)
class _ConfigEnable802dot1p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_ConfigEnable802dot1p_Type.__name__=_B
_ConfigEnable802dot1p_Object=MibTableColumn
configEnable802dot1p=_ConfigEnable802dot1p_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,2),_ConfigEnable802dot1p_Type())
configEnable802dot1p.setMaxAccess(_C)
if mibBuilder.loadTexts:configEnable802dot1p.setStatus(_A)
class _ConfigEnableDiffserv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_ConfigEnableDiffserv_Type.__name__=_B
_ConfigEnableDiffserv_Object=MibTableColumn
configEnableDiffserv=_ConfigEnableDiffserv_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,3),_ConfigEnableDiffserv_Type())
configEnableDiffserv.setMaxAccess(_C)
if mibBuilder.loadTexts:configEnableDiffserv.setStatus(_A)
class _ConfigPriorityScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('weighted',0),('strict',1)))
_ConfigPriorityScheme_Type.__name__=_B
_ConfigPriorityScheme_Object=MibTableColumn
configPriorityScheme=_ConfigPriorityScheme_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,4),_ConfigPriorityScheme_Type())
configPriorityScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:configPriorityScheme.setStatus(_A)
class _ConfigForceDefaultPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_ConfigForceDefaultPriorityQueue_Type.__name__=_B
_ConfigForceDefaultPriorityQueue_Object=MibTableColumn
configForceDefaultPriorityQueue=_ConfigForceDefaultPriorityQueue_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,5),_ConfigForceDefaultPriorityQueue_Type())
configForceDefaultPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:configForceDefaultPriorityQueue.setStatus(_A)
class _ConfigDefaultPriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_ConfigDefaultPriorityQueue_Type.__name__=_B
_ConfigDefaultPriorityQueue_Object=MibTableColumn
configDefaultPriorityQueue=_ConfigDefaultPriorityQueue_Object((1,3,6,1,4,1,3181,10,6,2,83,2,1,6),_ConfigDefaultPriorityQueue_Type())
configDefaultPriorityQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:configDefaultPriorityQueue.setStatus(_A)
_Ieee802dot1pPrioMappingTable_Object=MibTable
ieee802dot1pPrioMappingTable=_Ieee802dot1pPrioMappingTable_Object((1,3,6,1,4,1,3181,10,6,2,83,3))
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTable.setStatus(_A)
_Ieee802dot1pPrioMappingEntry_Object=MibTableRow
ieee802dot1pPrioMappingEntry=_Ieee802dot1pPrioMappingEntry_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1))
ieee802dot1pPrioMappingEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:ieee802dot1pPrioMappingEntry.setStatus(_A)
class _Ieee802dot1pPrioMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_Ieee802dot1pPrioMappingIndex_Type.__name__=_B
_Ieee802dot1pPrioMappingIndex_Object=MibTableColumn
ieee802dot1pPrioMappingIndex=_Ieee802dot1pPrioMappingIndex_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,1),_Ieee802dot1pPrioMappingIndex_Type())
ieee802dot1pPrioMappingIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingIndex.setStatus(_A)
class _Ieee802dot1pPrioMappingTag0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag0_Type.__name__=_B
_Ieee802dot1pPrioMappingTag0_Object=MibTableColumn
ieee802dot1pPrioMappingTag0=_Ieee802dot1pPrioMappingTag0_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,2),_Ieee802dot1pPrioMappingTag0_Type())
ieee802dot1pPrioMappingTag0.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag0.setStatus(_A)
class _Ieee802dot1pPrioMappingTag1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag1_Type.__name__=_B
_Ieee802dot1pPrioMappingTag1_Object=MibTableColumn
ieee802dot1pPrioMappingTag1=_Ieee802dot1pPrioMappingTag1_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,3),_Ieee802dot1pPrioMappingTag1_Type())
ieee802dot1pPrioMappingTag1.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag1.setStatus(_A)
class _Ieee802dot1pPrioMappingTag2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag2_Type.__name__=_B
_Ieee802dot1pPrioMappingTag2_Object=MibTableColumn
ieee802dot1pPrioMappingTag2=_Ieee802dot1pPrioMappingTag2_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,4),_Ieee802dot1pPrioMappingTag2_Type())
ieee802dot1pPrioMappingTag2.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag2.setStatus(_A)
class _Ieee802dot1pPrioMappingTag3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag3_Type.__name__=_B
_Ieee802dot1pPrioMappingTag3_Object=MibTableColumn
ieee802dot1pPrioMappingTag3=_Ieee802dot1pPrioMappingTag3_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,5),_Ieee802dot1pPrioMappingTag3_Type())
ieee802dot1pPrioMappingTag3.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag3.setStatus(_A)
class _Ieee802dot1pPrioMappingTag4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag4_Type.__name__=_B
_Ieee802dot1pPrioMappingTag4_Object=MibTableColumn
ieee802dot1pPrioMappingTag4=_Ieee802dot1pPrioMappingTag4_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,6),_Ieee802dot1pPrioMappingTag4_Type())
ieee802dot1pPrioMappingTag4.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag4.setStatus(_A)
class _Ieee802dot1pPrioMappingTag5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag5_Type.__name__=_B
_Ieee802dot1pPrioMappingTag5_Object=MibTableColumn
ieee802dot1pPrioMappingTag5=_Ieee802dot1pPrioMappingTag5_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,7),_Ieee802dot1pPrioMappingTag5_Type())
ieee802dot1pPrioMappingTag5.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag5.setStatus(_A)
class _Ieee802dot1pPrioMappingTag6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag6_Type.__name__=_B
_Ieee802dot1pPrioMappingTag6_Object=MibTableColumn
ieee802dot1pPrioMappingTag6=_Ieee802dot1pPrioMappingTag6_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,8),_Ieee802dot1pPrioMappingTag6_Type())
ieee802dot1pPrioMappingTag6.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag6.setStatus(_A)
class _Ieee802dot1pPrioMappingTag7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_Ieee802dot1pPrioMappingTag7_Type.__name__=_B
_Ieee802dot1pPrioMappingTag7_Object=MibTableColumn
ieee802dot1pPrioMappingTag7=_Ieee802dot1pPrioMappingTag7_Object((1,3,6,1,4,1,3181,10,6,2,83,3,1,9),_Ieee802dot1pPrioMappingTag7_Type())
ieee802dot1pPrioMappingTag7.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee802dot1pPrioMappingTag7.setStatus(_A)
_DiffservPrioMappingTable_Object=MibTable
diffservPrioMappingTable=_DiffservPrioMappingTable_Object((1,3,6,1,4,1,3181,10,6,2,83,4))
if mibBuilder.loadTexts:diffservPrioMappingTable.setStatus(_A)
_DiffservPrioMappingEntry_Object=MibTableRow
diffservPrioMappingEntry=_DiffservPrioMappingEntry_Object((1,3,6,1,4,1,3181,10,6,2,83,4,1))
diffservPrioMappingEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:diffservPrioMappingEntry.setStatus(_A)
class _DiffservPrioMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DiffservPrioMappingIndex_Type.__name__=_B
_DiffservPrioMappingIndex_Object=MibTableColumn
diffservPrioMappingIndex=_DiffservPrioMappingIndex_Object((1,3,6,1,4,1,3181,10,6,2,83,4,1,1),_DiffservPrioMappingIndex_Type())
diffservPrioMappingIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:diffservPrioMappingIndex.setStatus(_A)
class _DiffservPrioMappingDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3)))
_DiffservPrioMappingDscp_Type.__name__=_B
_DiffservPrioMappingDscp_Object=MibTableColumn
diffservPrioMappingDscp=_DiffservPrioMappingDscp_Object((1,3,6,1,4,1,3181,10,6,2,83,4,1,2),_DiffservPrioMappingDscp_Type())
diffservPrioMappingDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:diffservPrioMappingDscp.setStatus(_A)
_RateShapingTable_Object=MibTable
rateShapingTable=_RateShapingTable_Object((1,3,6,1,4,1,3181,10,6,2,83,5))
if mibBuilder.loadTexts:rateShapingTable.setStatus(_A)
_RateShapingEntry_Object=MibTableRow
rateShapingEntry=_RateShapingEntry_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1))
rateShapingEntry.setIndexNames((0,_I,_O))
if mibBuilder.loadTexts:rateShapingEntry.setStatus(_A)
class _RateShapingPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_RateShapingPortIndex_Type.__name__=_B
_RateShapingPortIndex_Object=MibTableColumn
rateShapingPortIndex=_RateShapingPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,1),_RateShapingPortIndex_Type())
rateShapingPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rateShapingPortIndex.setStatus(_A)
class _RateShapingEgressBandwidthPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingEgressBandwidthPercent_Type.__name__=_B
_RateShapingEgressBandwidthPercent_Object=MibTableColumn
rateShapingEgressBandwidthPercent=_RateShapingEgressBandwidthPercent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,2),_RateShapingEgressBandwidthPercent_Type())
rateShapingEgressBandwidthPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingEgressBandwidthPercent.setStatus(_A)
class _RateShapingIngressUnicastPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingIngressUnicastPercent_Type.__name__=_B
_RateShapingIngressUnicastPercent_Object=MibTableColumn
rateShapingIngressUnicastPercent=_RateShapingIngressUnicastPercent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,3),_RateShapingIngressUnicastPercent_Type())
rateShapingIngressUnicastPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingIngressUnicastPercent.setStatus(_A)
class _RateShapingIngressMulticastPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingIngressMulticastPercent_Type.__name__=_B
_RateShapingIngressMulticastPercent_Object=MibTableColumn
rateShapingIngressMulticastPercent=_RateShapingIngressMulticastPercent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,4),_RateShapingIngressMulticastPercent_Type())
rateShapingIngressMulticastPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingIngressMulticastPercent.setStatus(_A)
class _RateShapingIngressBroadcastPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingIngressBroadcastPercent_Type.__name__=_B
_RateShapingIngressBroadcastPercent_Object=MibTableColumn
rateShapingIngressBroadcastPercent=_RateShapingIngressBroadcastPercent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,5),_RateShapingIngressBroadcastPercent_Type())
rateShapingIngressBroadcastPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingIngressBroadcastPercent.setStatus(_A)
class _RateShapingIngressUser1Percent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingIngressUser1Percent_Type.__name__=_B
_RateShapingIngressUser1Percent_Object=MibTableColumn
rateShapingIngressUser1Percent=_RateShapingIngressUser1Percent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,6),_RateShapingIngressUser1Percent_Type())
rateShapingIngressUser1Percent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingIngressUser1Percent.setStatus(_A)
class _RateShapingIngressUser2Percent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RateShapingIngressUser2Percent_Type.__name__=_B
_RateShapingIngressUser2Percent_Object=MibTableColumn
rateShapingIngressUser2Percent=_RateShapingIngressUser2Percent_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,7),_RateShapingIngressUser2Percent_Type())
rateShapingIngressUser2Percent.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingIngressUser2Percent.setStatus(_A)
class _RateShapingUser1FrameTypes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('arp',1),('tcpControl',2),('arpAndTcpCtrl',3)))
_RateShapingUser1FrameTypes_Type.__name__=_B
_RateShapingUser1FrameTypes_Object=MibTableColumn
rateShapingUser1FrameTypes=_RateShapingUser1FrameTypes_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,8),_RateShapingUser1FrameTypes_Type())
rateShapingUser1FrameTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingUser1FrameTypes.setStatus(_A)
class _RateShapingUser2FrameTypes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('udpData',1),('tcpData',2),('udpAndTcpData',3),('nonUdpTcpData',4)))
_RateShapingUser2FrameTypes_Type.__name__=_B
_RateShapingUser2FrameTypes_Object=MibTableColumn
rateShapingUser2FrameTypes=_RateShapingUser2FrameTypes_Object((1,3,6,1,4,1,3181,10,6,2,83,5,1,9),_RateShapingUser2FrameTypes_Type())
rateShapingUser2FrameTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:rateShapingUser2FrameTypes.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'protocol':protocol,'qos':qos,'qosEnableQos':qosEnableQos,'configTable':configTable,'configEntry':configEntry,_L:configPortIndex,'configEnable802dot1p':configEnable802dot1p,'configEnableDiffserv':configEnableDiffserv,'configPriorityScheme':configPriorityScheme,'configForceDefaultPriorityQueue':configForceDefaultPriorityQueue,'configDefaultPriorityQueue':configDefaultPriorityQueue,'ieee802dot1pPrioMappingTable':ieee802dot1pPrioMappingTable,'ieee802dot1pPrioMappingEntry':ieee802dot1pPrioMappingEntry,_M:ieee802dot1pPrioMappingIndex,'ieee802dot1pPrioMappingTag0':ieee802dot1pPrioMappingTag0,'ieee802dot1pPrioMappingTag1':ieee802dot1pPrioMappingTag1,'ieee802dot1pPrioMappingTag2':ieee802dot1pPrioMappingTag2,'ieee802dot1pPrioMappingTag3':ieee802dot1pPrioMappingTag3,'ieee802dot1pPrioMappingTag4':ieee802dot1pPrioMappingTag4,'ieee802dot1pPrioMappingTag5':ieee802dot1pPrioMappingTag5,'ieee802dot1pPrioMappingTag6':ieee802dot1pPrioMappingTag6,'ieee802dot1pPrioMappingTag7':ieee802dot1pPrioMappingTag7,'diffservPrioMappingTable':diffservPrioMappingTable,'diffservPrioMappingEntry':diffservPrioMappingEntry,_N:diffservPrioMappingIndex,'diffservPrioMappingDscp':diffservPrioMappingDscp,'rateShapingTable':rateShapingTable,'rateShapingEntry':rateShapingEntry,_O:rateShapingPortIndex,'rateShapingEgressBandwidthPercent':rateShapingEgressBandwidthPercent,'rateShapingIngressUnicastPercent':rateShapingIngressUnicastPercent,'rateShapingIngressMulticastPercent':rateShapingIngressMulticastPercent,'rateShapingIngressBroadcastPercent':rateShapingIngressBroadcastPercent,'rateShapingIngressUser1Percent':rateShapingIngressUser1Percent,'rateShapingIngressUser2Percent':rateShapingIngressUser2Percent,'rateShapingUser1FrameTypes':rateShapingUser1FrameTypes,'rateShapingUser2FrameTypes':rateShapingUser2FrameTypes})