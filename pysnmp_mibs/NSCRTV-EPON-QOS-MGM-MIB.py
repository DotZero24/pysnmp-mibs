_O='portBaseQosPolicyPortIndex'
_N='portBaseQosPolicyCardIndex'
_M='portBaseQosMapPortIndex'
_L='portBaseQosMapCardIndex'
_K='diffserv'
_J='qosGlobalSetDeviceIndex'
_I='deviceBaseQosPolicyDeviceIndex'
_H='deviceBaseQosMapRuleIndex'
_G='deviceBaseQosMapDeviceIndex'
_F='OctetString'
_E='Integer32'
_D='read-write'
_C='not-accessible'
_B='NSCRTV-EPON-QOS-MGM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,qosManagementObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','qosManagementObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_QosGlobalSetTable_Object=MibTable
qosGlobalSetTable=_QosGlobalSetTable_Object((1,3,6,1,4,1,17409,2,3,8,1))
if mibBuilder.loadTexts:qosGlobalSetTable.setStatus(_A)
_QosGlobalSetEntry_Object=MibTableRow
qosGlobalSetEntry=_QosGlobalSetEntry_Object((1,3,6,1,4,1,17409,2,3,8,1,1))
qosGlobalSetEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qosGlobalSetEntry.setStatus(_A)
_QosGlobalSetDeviceIndex_Type=EponDeviceIndex
_QosGlobalSetDeviceIndex_Object=MibTableColumn
qosGlobalSetDeviceIndex=_QosGlobalSetDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,8,1,1,1),_QosGlobalSetDeviceIndex_Type())
qosGlobalSetDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosGlobalSetDeviceIndex.setStatus(_A)
class _QosGlobalSetMaxQueueCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QosGlobalSetMaxQueueCount_Type.__name__=_E
_QosGlobalSetMaxQueueCount_Object=MibTableColumn
qosGlobalSetMaxQueueCount=_QosGlobalSetMaxQueueCount_Object((1,3,6,1,4,1,17409,2,3,8,1,1,2),_QosGlobalSetMaxQueueCount_Type())
qosGlobalSetMaxQueueCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:qosGlobalSetMaxQueueCount.setStatus(_A)
class _QosGlobalSetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deviceBased',1),('portBased',2)))
_QosGlobalSetMode_Type.__name__=_E
_QosGlobalSetMode_Object=MibTableColumn
qosGlobalSetMode=_QosGlobalSetMode_Object((1,3,6,1,4,1,17409,2,3,8,1,1,3),_QosGlobalSetMode_Type())
qosGlobalSetMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qosGlobalSetMode.setStatus(_A)
_DeviceBaseQosMapTable_Object=MibTable
deviceBaseQosMapTable=_DeviceBaseQosMapTable_Object((1,3,6,1,4,1,17409,2,3,8,2))
if mibBuilder.loadTexts:deviceBaseQosMapTable.setStatus(_A)
_DeviceBaseQosMapEntry_Object=MibTableRow
deviceBaseQosMapEntry=_DeviceBaseQosMapEntry_Object((1,3,6,1,4,1,17409,2,3,8,2,1))
deviceBaseQosMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:deviceBaseQosMapEntry.setStatus(_A)
_DeviceBaseQosMapDeviceIndex_Type=EponDeviceIndex
_DeviceBaseQosMapDeviceIndex_Object=MibTableColumn
deviceBaseQosMapDeviceIndex=_DeviceBaseQosMapDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,8,2,1,1),_DeviceBaseQosMapDeviceIndex_Type())
deviceBaseQosMapDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceBaseQosMapDeviceIndex.setStatus(_A)
class _DeviceBaseQosMapRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cos',1),('tos',2),(_K,3)))
_DeviceBaseQosMapRuleIndex_Type.__name__=_E
_DeviceBaseQosMapRuleIndex_Object=MibTableColumn
deviceBaseQosMapRuleIndex=_DeviceBaseQosMapRuleIndex_Object((1,3,6,1,4,1,17409,2,3,8,2,1,2),_DeviceBaseQosMapRuleIndex_Type())
deviceBaseQosMapRuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceBaseQosMapRuleIndex.setStatus(_A)
class _DeviceBaseQosMapOctet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(64,64))
_DeviceBaseQosMapOctet_Type.__name__=_F
_DeviceBaseQosMapOctet_Object=MibTableColumn
deviceBaseQosMapOctet=_DeviceBaseQosMapOctet_Object((1,3,6,1,4,1,17409,2,3,8,2,1,3),_DeviceBaseQosMapOctet_Type())
deviceBaseQosMapOctet.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceBaseQosMapOctet.setStatus(_A)
_DeviceBaseQosPolicyTable_Object=MibTable
deviceBaseQosPolicyTable=_DeviceBaseQosPolicyTable_Object((1,3,6,1,4,1,17409,2,3,8,3))
if mibBuilder.loadTexts:deviceBaseQosPolicyTable.setStatus(_A)
_DeviceBaseQosPolicyEntry_Object=MibTableRow
deviceBaseQosPolicyEntry=_DeviceBaseQosPolicyEntry_Object((1,3,6,1,4,1,17409,2,3,8,3,1))
deviceBaseQosPolicyEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:deviceBaseQosPolicyEntry.setStatus(_A)
_DeviceBaseQosPolicyDeviceIndex_Type=EponDeviceIndex
_DeviceBaseQosPolicyDeviceIndex_Object=MibTableColumn
deviceBaseQosPolicyDeviceIndex=_DeviceBaseQosPolicyDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,8,3,1,1),_DeviceBaseQosPolicyDeviceIndex_Type())
deviceBaseQosPolicyDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceBaseQosPolicyDeviceIndex.setStatus(_A)
class _DeviceBaseQosPolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('wrr',2),('spWrr',3),('wfp',4)))
_DeviceBaseQosPolicyMode_Type.__name__=_E
_DeviceBaseQosPolicyMode_Object=MibTableColumn
deviceBaseQosPolicyMode=_DeviceBaseQosPolicyMode_Object((1,3,6,1,4,1,17409,2,3,8,3,1,2),_DeviceBaseQosPolicyMode_Type())
deviceBaseQosPolicyMode.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceBaseQosPolicyMode.setStatus(_A)
_DeviceBaseQosPolicyWeightOctet_Type=OctetString
_DeviceBaseQosPolicyWeightOctet_Object=MibTableColumn
deviceBaseQosPolicyWeightOctet=_DeviceBaseQosPolicyWeightOctet_Object((1,3,6,1,4,1,17409,2,3,8,3,1,3),_DeviceBaseQosPolicyWeightOctet_Type())
deviceBaseQosPolicyWeightOctet.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceBaseQosPolicyWeightOctet.setStatus(_A)
_DeviceBaseQosPolicySpBandwidthRange_Type=OctetString
_DeviceBaseQosPolicySpBandwidthRange_Object=MibTableColumn
deviceBaseQosPolicySpBandwidthRange=_DeviceBaseQosPolicySpBandwidthRange_Object((1,3,6,1,4,1,17409,2,3,8,3,1,4),_DeviceBaseQosPolicySpBandwidthRange_Type())
deviceBaseQosPolicySpBandwidthRange.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceBaseQosPolicySpBandwidthRange.setStatus(_A)
_PortBaseQosMapTable_Object=MibTable
portBaseQosMapTable=_PortBaseQosMapTable_Object((1,3,6,1,4,1,17409,2,3,8,4))
if mibBuilder.loadTexts:portBaseQosMapTable.setStatus(_A)
_PortBaseQosMapEntry_Object=MibTableRow
portBaseQosMapEntry=_PortBaseQosMapEntry_Object((1,3,6,1,4,1,17409,2,3,8,4,1))
portBaseQosMapEntry.setIndexNames((0,_B,_G),(0,_B,_L),(0,_B,_M),(0,_B,_H))
if mibBuilder.loadTexts:portBaseQosMapEntry.setStatus(_A)
_PortBaseQosMapDeviceIndex_Type=EponDeviceIndex
_PortBaseQosMapDeviceIndex_Object=MibTableColumn
portBaseQosMapDeviceIndex=_PortBaseQosMapDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,8,4,1,1),_PortBaseQosMapDeviceIndex_Type())
portBaseQosMapDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosMapDeviceIndex.setStatus(_A)
_PortBaseQosMapCardIndex_Type=EponPortIndex
_PortBaseQosMapCardIndex_Object=MibTableColumn
portBaseQosMapCardIndex=_PortBaseQosMapCardIndex_Object((1,3,6,1,4,1,17409,2,3,8,4,1,2),_PortBaseQosMapCardIndex_Type())
portBaseQosMapCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosMapCardIndex.setStatus(_A)
_PortBaseQosMapPortIndex_Type=EponPortIndex
_PortBaseQosMapPortIndex_Object=MibTableColumn
portBaseQosMapPortIndex=_PortBaseQosMapPortIndex_Object((1,3,6,1,4,1,17409,2,3,8,4,1,3),_PortBaseQosMapPortIndex_Type())
portBaseQosMapPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosMapPortIndex.setStatus(_A)
class _PortBaseQosMapRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cos',1),('tos',2),(_K,3)))
_PortBaseQosMapRuleIndex_Type.__name__=_E
_PortBaseQosMapRuleIndex_Object=MibTableColumn
portBaseQosMapRuleIndex=_PortBaseQosMapRuleIndex_Object((1,3,6,1,4,1,17409,2,3,8,4,1,4),_PortBaseQosMapRuleIndex_Type())
portBaseQosMapRuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosMapRuleIndex.setStatus(_A)
class _PortBaseQosMapOctet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_PortBaseQosMapOctet_Type.__name__=_F
_PortBaseQosMapOctet_Object=MibTableColumn
portBaseQosMapOctet=_PortBaseQosMapOctet_Object((1,3,6,1,4,1,17409,2,3,8,4,1,5),_PortBaseQosMapOctet_Type())
portBaseQosMapOctet.setMaxAccess(_D)
if mibBuilder.loadTexts:portBaseQosMapOctet.setStatus(_A)
_PortBaseQosPolicyTable_Object=MibTable
portBaseQosPolicyTable=_PortBaseQosPolicyTable_Object((1,3,6,1,4,1,17409,2,3,8,5))
if mibBuilder.loadTexts:portBaseQosPolicyTable.setStatus(_A)
_PortBaseQosPolicyEntry_Object=MibTableRow
portBaseQosPolicyEntry=_PortBaseQosPolicyEntry_Object((1,3,6,1,4,1,17409,2,3,8,5,1))
portBaseQosPolicyEntry.setIndexNames((0,_B,_I),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:portBaseQosPolicyEntry.setStatus(_A)
_PortBaseQosPolicyDeviceIndex_Type=EponDeviceIndex
_PortBaseQosPolicyDeviceIndex_Object=MibTableColumn
portBaseQosPolicyDeviceIndex=_PortBaseQosPolicyDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,8,5,1,1),_PortBaseQosPolicyDeviceIndex_Type())
portBaseQosPolicyDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosPolicyDeviceIndex.setStatus(_A)
_PortBaseQosPolicyCardIndex_Type=EponPortIndex
_PortBaseQosPolicyCardIndex_Object=MibTableColumn
portBaseQosPolicyCardIndex=_PortBaseQosPolicyCardIndex_Object((1,3,6,1,4,1,17409,2,3,8,5,1,2),_PortBaseQosPolicyCardIndex_Type())
portBaseQosPolicyCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosPolicyCardIndex.setStatus(_A)
_PortBaseQosPolicyPortIndex_Type=EponPortIndex
_PortBaseQosPolicyPortIndex_Object=MibTableColumn
portBaseQosPolicyPortIndex=_PortBaseQosPolicyPortIndex_Object((1,3,6,1,4,1,17409,2,3,8,5,1,3),_PortBaseQosPolicyPortIndex_Type())
portBaseQosPolicyPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBaseQosPolicyPortIndex.setStatus(_A)
class _PortBaseQosPolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('wrr',2),('spWrr',3),('wfp',4)))
_PortBaseQosPolicyMode_Type.__name__=_E
_PortBaseQosPolicyMode_Object=MibTableColumn
portBaseQosPolicyMode=_PortBaseQosPolicyMode_Object((1,3,6,1,4,1,17409,2,3,8,5,1,4),_PortBaseQosPolicyMode_Type())
portBaseQosPolicyMode.setMaxAccess(_D)
if mibBuilder.loadTexts:portBaseQosPolicyMode.setStatus(_A)
class _PortBaseQosPolicyWeightOctet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_PortBaseQosPolicyWeightOctet_Type.__name__=_F
_PortBaseQosPolicyWeightOctet_Object=MibTableColumn
portBaseQosPolicyWeightOctet=_PortBaseQosPolicyWeightOctet_Object((1,3,6,1,4,1,17409,2,3,8,5,1,5),_PortBaseQosPolicyWeightOctet_Type())
portBaseQosPolicyWeightOctet.setMaxAccess(_D)
if mibBuilder.loadTexts:portBaseQosPolicyWeightOctet.setStatus(_A)
_PortBaseQosPolicySpBandwidthRange_Type=OctetString
_PortBaseQosPolicySpBandwidthRange_Object=MibTableColumn
portBaseQosPolicySpBandwidthRange=_PortBaseQosPolicySpBandwidthRange_Object((1,3,6,1,4,1,17409,2,3,8,5,1,6),_PortBaseQosPolicySpBandwidthRange_Type())
portBaseQosPolicySpBandwidthRange.setMaxAccess(_D)
if mibBuilder.loadTexts:portBaseQosPolicySpBandwidthRange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qosGlobalSetTable':qosGlobalSetTable,'qosGlobalSetEntry':qosGlobalSetEntry,_J:qosGlobalSetDeviceIndex,'qosGlobalSetMaxQueueCount':qosGlobalSetMaxQueueCount,'qosGlobalSetMode':qosGlobalSetMode,'deviceBaseQosMapTable':deviceBaseQosMapTable,'deviceBaseQosMapEntry':deviceBaseQosMapEntry,_G:deviceBaseQosMapDeviceIndex,_H:deviceBaseQosMapRuleIndex,'deviceBaseQosMapOctet':deviceBaseQosMapOctet,'deviceBaseQosPolicyTable':deviceBaseQosPolicyTable,'deviceBaseQosPolicyEntry':deviceBaseQosPolicyEntry,_I:deviceBaseQosPolicyDeviceIndex,'deviceBaseQosPolicyMode':deviceBaseQosPolicyMode,'deviceBaseQosPolicyWeightOctet':deviceBaseQosPolicyWeightOctet,'deviceBaseQosPolicySpBandwidthRange':deviceBaseQosPolicySpBandwidthRange,'portBaseQosMapTable':portBaseQosMapTable,'portBaseQosMapEntry':portBaseQosMapEntry,'portBaseQosMapDeviceIndex':portBaseQosMapDeviceIndex,_L:portBaseQosMapCardIndex,_M:portBaseQosMapPortIndex,'portBaseQosMapRuleIndex':portBaseQosMapRuleIndex,'portBaseQosMapOctet':portBaseQosMapOctet,'portBaseQosPolicyTable':portBaseQosPolicyTable,'portBaseQosPolicyEntry':portBaseQosPolicyEntry,'portBaseQosPolicyDeviceIndex':portBaseQosPolicyDeviceIndex,_N:portBaseQosPolicyCardIndex,_O:portBaseQosPolicyPortIndex,'portBaseQosPolicyMode':portBaseQosPolicyMode,'portBaseQosPolicyWeightOctet':portBaseQosPolicyWeightOctet,'portBaseQosPolicySpBandwidthRange':portBaseQosPolicySpBandwidthRange})