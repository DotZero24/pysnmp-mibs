_W='qosSwitch8948PortEntry'
_V='qosSwitch8948TCCountersTrafficClassIndex'
_U='qosSwitch8948TCCountersPolicyIndex'
_T='qosSwitch8948TCCountersPortIndex'
_S='qosSwitchTrafficClassIndex'
_R='bwclass_priority'
_Q='priority'
_P='bwclass'
_O='usedscpmap'
_N='usedscp'
_M='usemarkvalue'
_L='qosSwitchPolicyIndex'
_K='qosSwitchPortIndex'
_J='OctetString'
_I='none'
_H='yes'
_G='no'
_F='not-accessible'
_E='kbps'
_D='AT-QOS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qos=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,99))
if mibBuilder.loadTexts:qos.setRevisions(('2004-12-01 15:25',))
_QosSwitch_ObjectIdentity=ObjectIdentity
qosSwitch=_QosSwitch_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,99,1))
_QosSwitchPortTable_Object=MibTable
qosSwitchPortTable=_QosSwitchPortTable_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,1))
if mibBuilder.loadTexts:qosSwitchPortTable.setStatus(_A)
_QosSwitchPortEntry_Object=MibTableRow
qosSwitchPortEntry=_QosSwitchPortEntry_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,1,1))
qosSwitchPortEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:qosSwitchPortEntry.setStatus(_A)
class _QosSwitchPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QosSwitchPortIndex_Type.__name__=_C
_QosSwitchPortIndex_Object=MibTableColumn
qosSwitchPortIndex=_QosSwitchPortIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,1,1,1),_QosSwitchPortIndex_Type())
qosSwitchPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitchPortIndex.setStatus(_A)
class _QosSwitchPortPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QosSwitchPortPolicyIndex_Type.__name__=_C
_QosSwitchPortPolicyIndex_Object=MibTableColumn
qosSwitchPortPolicyIndex=_QosSwitchPortPolicyIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,1,1,2),_QosSwitchPortPolicyIndex_Type())
qosSwitchPortPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPortPolicyIndex.setStatus(_A)
_QosSwitchPolicyTable_Object=MibTable
qosSwitchPolicyTable=_QosSwitchPolicyTable_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2))
if mibBuilder.loadTexts:qosSwitchPolicyTable.setStatus(_A)
_QosSwitchPolicyEntry_Object=MibTableRow
qosSwitchPolicyEntry=_QosSwitchPolicyEntry_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1))
qosSwitchPolicyEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:qosSwitchPolicyEntry.setStatus(_A)
class _QosSwitchPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QosSwitchPolicyIndex_Type.__name__=_C
_QosSwitchPolicyIndex_Object=MibTableColumn
qosSwitchPolicyIndex=_QosSwitchPolicyIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,1),_QosSwitchPolicyIndex_Type())
qosSwitchPolicyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitchPolicyIndex.setStatus(_A)
class _QosSwitchPolicyDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_QosSwitchPolicyDescription_Type.__name__=_J
_QosSwitchPolicyDescription_Object=MibTableColumn
qosSwitchPolicyDescription=_QosSwitchPolicyDescription_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,2),_QosSwitchPolicyDescription_Type())
qosSwitchPolicyDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDescription.setStatus(_A)
class _QosSwitchPolicyDefaultTCDropBWClass3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_QosSwitchPolicyDefaultTCDropBWClass3_Type.__name__=_C
_QosSwitchPolicyDefaultTCDropBWClass3_Object=MibTableColumn
qosSwitchPolicyDefaultTCDropBWClass3=_QosSwitchPolicyDefaultTCDropBWClass3_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,3),_QosSwitchPolicyDefaultTCDropBWClass3_Type())
qosSwitchPolicyDefaultTCDropBWClass3.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCDropBWClass3.setStatus(_A)
class _QosSwitchPolicyDefaultTCIgnoreBWClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_QosSwitchPolicyDefaultTCIgnoreBWClass_Type.__name__=_C
_QosSwitchPolicyDefaultTCIgnoreBWClass_Object=MibTableColumn
qosSwitchPolicyDefaultTCIgnoreBWClass=_QosSwitchPolicyDefaultTCIgnoreBWClass_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,4),_QosSwitchPolicyDefaultTCIgnoreBWClass_Type())
qosSwitchPolicyDefaultTCIgnoreBWClass.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCIgnoreBWClass.setStatus(_A)
class _QosSwitchPolicyDefaultTCMarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(256,256))
_QosSwitchPolicyDefaultTCMarkValue_Type.__name__=_C
_QosSwitchPolicyDefaultTCMarkValue_Object=MibTableColumn
qosSwitchPolicyDefaultTCMarkValue=_QosSwitchPolicyDefaultTCMarkValue_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,5),_QosSwitchPolicyDefaultTCMarkValue_Type())
qosSwitchPolicyDefaultTCMarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMarkValue.setStatus(_A)
class _QosSwitchPolicyDefaultTCMaxBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000),ValueRangeConstraint(2147483647,2147483647))
_QosSwitchPolicyDefaultTCMaxBandwidth_Type.__name__=_C
_QosSwitchPolicyDefaultTCMaxBandwidth_Object=MibTableColumn
qosSwitchPolicyDefaultTCMaxBandwidth=_QosSwitchPolicyDefaultTCMaxBandwidth_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,6),_QosSwitchPolicyDefaultTCMaxBandwidth_Type())
qosSwitchPolicyDefaultTCMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMaxBandwidth.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMaxBandwidth.setUnits(_E)
class _QosSwitchPolicyDefaultTCMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000))
_QosSwitchPolicyDefaultTCMaxBurstSize_Type.__name__=_C
_QosSwitchPolicyDefaultTCMaxBurstSize_Object=MibTableColumn
qosSwitchPolicyDefaultTCMaxBurstSize=_QosSwitchPolicyDefaultTCMaxBurstSize_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,7),_QosSwitchPolicyDefaultTCMaxBurstSize_Type())
qosSwitchPolicyDefaultTCMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMaxBurstSize.setUnits(_E)
class _QosSwitchPolicyDefaultTCMinBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000),ValueRangeConstraint(2147483647,2147483647))
_QosSwitchPolicyDefaultTCMinBandwidth_Type.__name__=_C
_QosSwitchPolicyDefaultTCMinBandwidth_Object=MibTableColumn
qosSwitchPolicyDefaultTCMinBandwidth=_QosSwitchPolicyDefaultTCMinBandwidth_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,8),_QosSwitchPolicyDefaultTCMinBandwidth_Type())
qosSwitchPolicyDefaultTCMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMinBandwidth.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMinBandwidth.setUnits(_E)
class _QosSwitchPolicyDefaultTCMinBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000))
_QosSwitchPolicyDefaultTCMinBurstSize_Type.__name__=_C
_QosSwitchPolicyDefaultTCMinBurstSize_Object=MibTableColumn
qosSwitchPolicyDefaultTCMinBurstSize=_QosSwitchPolicyDefaultTCMinBurstSize_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,9),_QosSwitchPolicyDefaultTCMinBurstSize_Type())
qosSwitchPolicyDefaultTCMinBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMinBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCMinBurstSize.setUnits(_E)
class _QosSwitchPolicyDefaultTCPremarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_M,1),(_N,2)))
_QosSwitchPolicyDefaultTCPremarking_Type.__name__=_C
_QosSwitchPolicyDefaultTCPremarking_Object=MibTableColumn
qosSwitchPolicyDefaultTCPremarking=_QosSwitchPolicyDefaultTCPremarking_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,10),_QosSwitchPolicyDefaultTCPremarking_Type())
qosSwitchPolicyDefaultTCPremarking.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCPremarking.setStatus(_A)
class _QosSwitchPolicyDefaultTCRemarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3),(_R,4)))
_QosSwitchPolicyDefaultTCRemarking_Type.__name__=_C
_QosSwitchPolicyDefaultTCRemarking_Object=MibTableColumn
qosSwitchPolicyDefaultTCRemarking=_QosSwitchPolicyDefaultTCRemarking_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,2,1,11),_QosSwitchPolicyDefaultTCRemarking_Type())
qosSwitchPolicyDefaultTCRemarking.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchPolicyDefaultTCRemarking.setStatus(_A)
_QosSwitchTrafficClassTable_Object=MibTable
qosSwitchTrafficClassTable=_QosSwitchTrafficClassTable_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3))
if mibBuilder.loadTexts:qosSwitchTrafficClassTable.setStatus(_A)
_QosSwitchTrafficClassEntry_Object=MibTableRow
qosSwitchTrafficClassEntry=_QosSwitchTrafficClassEntry_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1))
qosSwitchTrafficClassEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:qosSwitchTrafficClassEntry.setStatus(_A)
class _QosSwitchTrafficClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosSwitchTrafficClassIndex_Type.__name__=_C
_QosSwitchTrafficClassIndex_Object=MibTableColumn
qosSwitchTrafficClassIndex=_QosSwitchTrafficClassIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,1),_QosSwitchTrafficClassIndex_Type())
qosSwitchTrafficClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitchTrafficClassIndex.setStatus(_A)
class _QosSwitchTrafficClassPolicyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_QosSwitchTrafficClassPolicyNumber_Type.__name__=_C
_QosSwitchTrafficClassPolicyNumber_Object=MibTableColumn
qosSwitchTrafficClassPolicyNumber=_QosSwitchTrafficClassPolicyNumber_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,2),_QosSwitchTrafficClassPolicyNumber_Type())
qosSwitchTrafficClassPolicyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassPolicyNumber.setStatus(_A)
class _QosSwitchTrafficClassDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_QosSwitchTrafficClassDescription_Type.__name__=_J
_QosSwitchTrafficClassDescription_Object=MibTableColumn
qosSwitchTrafficClassDescription=_QosSwitchTrafficClassDescription_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,3),_QosSwitchTrafficClassDescription_Type())
qosSwitchTrafficClassDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassDescription.setStatus(_A)
class _QosSwitchTrafficClassDropBWClass3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_QosSwitchTrafficClassDropBWClass3_Type.__name__=_C
_QosSwitchTrafficClassDropBWClass3_Object=MibTableColumn
qosSwitchTrafficClassDropBWClass3=_QosSwitchTrafficClassDropBWClass3_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,4),_QosSwitchTrafficClassDropBWClass3_Type())
qosSwitchTrafficClassDropBWClass3.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassDropBWClass3.setStatus(_A)
class _QosSwitchTrafficClassIgnoreBWClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_QosSwitchTrafficClassIgnoreBWClass_Type.__name__=_C
_QosSwitchTrafficClassIgnoreBWClass_Object=MibTableColumn
qosSwitchTrafficClassIgnoreBWClass=_QosSwitchTrafficClassIgnoreBWClass_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,5),_QosSwitchTrafficClassIgnoreBWClass_Type())
qosSwitchTrafficClassIgnoreBWClass.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassIgnoreBWClass.setStatus(_A)
class _QosSwitchTrafficClassMarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(256,256))
_QosSwitchTrafficClassMarkValue_Type.__name__=_C
_QosSwitchTrafficClassMarkValue_Object=MibTableColumn
qosSwitchTrafficClassMarkValue=_QosSwitchTrafficClassMarkValue_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,6),_QosSwitchTrafficClassMarkValue_Type())
qosSwitchTrafficClassMarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassMarkValue.setStatus(_A)
class _QosSwitchTrafficClassMaxBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000),ValueRangeConstraint(2147483647,2147483647))
_QosSwitchTrafficClassMaxBandwidth_Type.__name__=_C
_QosSwitchTrafficClassMaxBandwidth_Object=MibTableColumn
qosSwitchTrafficClassMaxBandwidth=_QosSwitchTrafficClassMaxBandwidth_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,7),_QosSwitchTrafficClassMaxBandwidth_Type())
qosSwitchTrafficClassMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassMaxBandwidth.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchTrafficClassMaxBandwidth.setUnits(_E)
class _QosSwitchTrafficClassMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000))
_QosSwitchTrafficClassMaxBurstSize_Type.__name__=_C
_QosSwitchTrafficClassMaxBurstSize_Object=MibTableColumn
qosSwitchTrafficClassMaxBurstSize=_QosSwitchTrafficClassMaxBurstSize_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,8),_QosSwitchTrafficClassMaxBurstSize_Type())
qosSwitchTrafficClassMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchTrafficClassMaxBurstSize.setUnits(_E)
class _QosSwitchTrafficClassMinBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000),ValueRangeConstraint(2147483647,2147483647))
_QosSwitchTrafficClassMinBandwidth_Type.__name__=_C
_QosSwitchTrafficClassMinBandwidth_Object=MibTableColumn
qosSwitchTrafficClassMinBandwidth=_QosSwitchTrafficClassMinBandwidth_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,9),_QosSwitchTrafficClassMinBandwidth_Type())
qosSwitchTrafficClassMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassMinBandwidth.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchTrafficClassMinBandwidth.setUnits(_E)
class _QosSwitchTrafficClassMinBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000000))
_QosSwitchTrafficClassMinBurstSize_Type.__name__=_C
_QosSwitchTrafficClassMinBurstSize_Object=MibTableColumn
qosSwitchTrafficClassMinBurstSize=_QosSwitchTrafficClassMinBurstSize_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,10),_QosSwitchTrafficClassMinBurstSize_Type())
qosSwitchTrafficClassMinBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassMinBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosSwitchTrafficClassMinBurstSize.setUnits(_E)
class _QosSwitchTrafficClassPremarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_M,1),(_N,2)))
_QosSwitchTrafficClassPremarking_Type.__name__=_C
_QosSwitchTrafficClassPremarking_Object=MibTableColumn
qosSwitchTrafficClassPremarking=_QosSwitchTrafficClassPremarking_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,11),_QosSwitchTrafficClassPremarking_Type())
qosSwitchTrafficClassPremarking.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassPremarking.setStatus(_A)
class _QosSwitchTrafficClassRemarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3),(_R,4)))
_QosSwitchTrafficClassRemarking_Type.__name__=_C
_QosSwitchTrafficClassRemarking_Object=MibTableColumn
qosSwitchTrafficClassRemarking=_QosSwitchTrafficClassRemarking_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,3,1,12),_QosSwitchTrafficClassRemarking_Type())
qosSwitchTrafficClassRemarking.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitchTrafficClassRemarking.setStatus(_A)
_QosSwitch8948_ObjectIdentity=ObjectIdentity
qosSwitch8948=_QosSwitch8948_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,99,1,4))
_QosSwitch8948PortTable_Object=MibTable
qosSwitch8948PortTable=_QosSwitch8948PortTable_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1))
if mibBuilder.loadTexts:qosSwitch8948PortTable.setStatus(_A)
_QosSwitch8948PortEntry_Object=MibTableRow
qosSwitch8948PortEntry=_QosSwitch8948PortEntry_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1))
if mibBuilder.loadTexts:qosSwitch8948PortEntry.setStatus(_A)
_QosSwitch8948PortDefaultTCCountersAggregateBytes_Type=Counter64
_QosSwitch8948PortDefaultTCCountersAggregateBytes_Object=MibTableColumn
qosSwitch8948PortDefaultTCCountersAggregateBytes=_QosSwitch8948PortDefaultTCCountersAggregateBytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,1),_QosSwitch8948PortDefaultTCCountersAggregateBytes_Type())
qosSwitch8948PortDefaultTCCountersAggregateBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortDefaultTCCountersAggregateBytes.setStatus(_A)
_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Type=Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Object=MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes=_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,2),_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Type())
qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes.setStatus(_A)
_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Type=Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Object=MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes=_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,3),_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Type())
qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes.setStatus(_A)
_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Type=Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Object=MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes=_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,4),_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Type())
qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes.setStatus(_A)
_QosSwitch8948PortDefaultTCCountersDroppedBytes_Type=Counter64
_QosSwitch8948PortDefaultTCCountersDroppedBytes_Object=MibTableColumn
qosSwitch8948PortDefaultTCCountersDroppedBytes=_QosSwitch8948PortDefaultTCCountersDroppedBytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,5),_QosSwitch8948PortDefaultTCCountersDroppedBytes_Type())
qosSwitch8948PortDefaultTCCountersDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortDefaultTCCountersDroppedBytes.setStatus(_A)
_QosSwitch8948PortQueueLength_Type=Gauge32
_QosSwitch8948PortQueueLength_Object=MibTableColumn
qosSwitch8948PortQueueLength=_QosSwitch8948PortQueueLength_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,6),_QosSwitch8948PortQueueLength_Type())
qosSwitch8948PortQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueueLength.setStatus(_A)
_QosSwitch8948PortQueue0Length_Type=Gauge32
_QosSwitch8948PortQueue0Length_Object=MibTableColumn
qosSwitch8948PortQueue0Length=_QosSwitch8948PortQueue0Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,7),_QosSwitch8948PortQueue0Length_Type())
qosSwitch8948PortQueue0Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue0Length.setStatus(_A)
_QosSwitch8948PortQueue1Length_Type=Gauge32
_QosSwitch8948PortQueue1Length_Object=MibTableColumn
qosSwitch8948PortQueue1Length=_QosSwitch8948PortQueue1Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,8),_QosSwitch8948PortQueue1Length_Type())
qosSwitch8948PortQueue1Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue1Length.setStatus(_A)
_QosSwitch8948PortQueue2Length_Type=Gauge32
_QosSwitch8948PortQueue2Length_Object=MibTableColumn
qosSwitch8948PortQueue2Length=_QosSwitch8948PortQueue2Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,9),_QosSwitch8948PortQueue2Length_Type())
qosSwitch8948PortQueue2Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue2Length.setStatus(_A)
_QosSwitch8948PortQueue3Length_Type=Gauge32
_QosSwitch8948PortQueue3Length_Object=MibTableColumn
qosSwitch8948PortQueue3Length=_QosSwitch8948PortQueue3Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,10),_QosSwitch8948PortQueue3Length_Type())
qosSwitch8948PortQueue3Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue3Length.setStatus(_A)
_QosSwitch8948PortQueue4Length_Type=Gauge32
_QosSwitch8948PortQueue4Length_Object=MibTableColumn
qosSwitch8948PortQueue4Length=_QosSwitch8948PortQueue4Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,11),_QosSwitch8948PortQueue4Length_Type())
qosSwitch8948PortQueue4Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue4Length.setStatus(_A)
_QosSwitch8948PortQueue5Length_Type=Gauge32
_QosSwitch8948PortQueue5Length_Object=MibTableColumn
qosSwitch8948PortQueue5Length=_QosSwitch8948PortQueue5Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,12),_QosSwitch8948PortQueue5Length_Type())
qosSwitch8948PortQueue5Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue5Length.setStatus(_A)
_QosSwitch8948PortQueue6Length_Type=Gauge32
_QosSwitch8948PortQueue6Length_Object=MibTableColumn
qosSwitch8948PortQueue6Length=_QosSwitch8948PortQueue6Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,13),_QosSwitch8948PortQueue6Length_Type())
qosSwitch8948PortQueue6Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue6Length.setStatus(_A)
_QosSwitch8948PortQueue7Length_Type=Gauge32
_QosSwitch8948PortQueue7Length_Object=MibTableColumn
qosSwitch8948PortQueue7Length=_QosSwitch8948PortQueue7Length_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,1,1,14),_QosSwitch8948PortQueue7Length_Type())
qosSwitch8948PortQueue7Length.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948PortQueue7Length.setStatus(_A)
_QosSwitch8948TrafficClassCountersTable_Object=MibTable
qosSwitch8948TrafficClassCountersTable=_QosSwitch8948TrafficClassCountersTable_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2))
if mibBuilder.loadTexts:qosSwitch8948TrafficClassCountersTable.setStatus(_A)
_QosSwitch8948TrafficClassCountersEntry_Object=MibTableRow
qosSwitch8948TrafficClassCountersEntry=_QosSwitch8948TrafficClassCountersEntry_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1))
qosSwitch8948TrafficClassCountersEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:qosSwitch8948TrafficClassCountersEntry.setStatus(_A)
class _QosSwitch8948TCCountersPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QosSwitch8948TCCountersPortIndex_Type.__name__=_C
_QosSwitch8948TCCountersPortIndex_Object=MibTableColumn
qosSwitch8948TCCountersPortIndex=_QosSwitch8948TCCountersPortIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,1),_QosSwitch8948TCCountersPortIndex_Type())
qosSwitch8948TCCountersPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitch8948TCCountersPortIndex.setStatus(_A)
class _QosSwitch8948TCCountersPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_QosSwitch8948TCCountersPolicyIndex_Type.__name__=_C
_QosSwitch8948TCCountersPolicyIndex_Object=MibTableColumn
qosSwitch8948TCCountersPolicyIndex=_QosSwitch8948TCCountersPolicyIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,2),_QosSwitch8948TCCountersPolicyIndex_Type())
qosSwitch8948TCCountersPolicyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitch8948TCCountersPolicyIndex.setStatus(_A)
class _QosSwitch8948TCCountersTrafficClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_QosSwitch8948TCCountersTrafficClassIndex_Type.__name__=_C
_QosSwitch8948TCCountersTrafficClassIndex_Object=MibTableColumn
qosSwitch8948TCCountersTrafficClassIndex=_QosSwitch8948TCCountersTrafficClassIndex_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,3),_QosSwitch8948TCCountersTrafficClassIndex_Type())
qosSwitch8948TCCountersTrafficClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qosSwitch8948TCCountersTrafficClassIndex.setStatus(_A)
_QosSwitch8948TCCountersAggregateBytes_Type=Counter32
_QosSwitch8948TCCountersAggregateBytes_Object=MibTableColumn
qosSwitch8948TCCountersAggregateBytes=_QosSwitch8948TCCountersAggregateBytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,4),_QosSwitch8948TCCountersAggregateBytes_Type())
qosSwitch8948TCCountersAggregateBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948TCCountersAggregateBytes.setStatus(_A)
_QosSwitch8948TCCountersBwConformanceClass1Bytes_Type=Counter32
_QosSwitch8948TCCountersBwConformanceClass1Bytes_Object=MibTableColumn
qosSwitch8948TCCountersBwConformanceClass1Bytes=_QosSwitch8948TCCountersBwConformanceClass1Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,5),_QosSwitch8948TCCountersBwConformanceClass1Bytes_Type())
qosSwitch8948TCCountersBwConformanceClass1Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948TCCountersBwConformanceClass1Bytes.setStatus(_A)
_QosSwitch8948TCCountersBwConformanceClass2Bytes_Type=Counter32
_QosSwitch8948TCCountersBwConformanceClass2Bytes_Object=MibTableColumn
qosSwitch8948TCCountersBwConformanceClass2Bytes=_QosSwitch8948TCCountersBwConformanceClass2Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,6),_QosSwitch8948TCCountersBwConformanceClass2Bytes_Type())
qosSwitch8948TCCountersBwConformanceClass2Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948TCCountersBwConformanceClass2Bytes.setStatus(_A)
_QosSwitch8948TCCountersBwConformanceClass3Bytes_Type=Counter32
_QosSwitch8948TCCountersBwConformanceClass3Bytes_Object=MibTableColumn
qosSwitch8948TCCountersBwConformanceClass3Bytes=_QosSwitch8948TCCountersBwConformanceClass3Bytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,7),_QosSwitch8948TCCountersBwConformanceClass3Bytes_Type())
qosSwitch8948TCCountersBwConformanceClass3Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948TCCountersBwConformanceClass3Bytes.setStatus(_A)
_QosSwitch8948TCCountersDroppedBytes_Type=Counter32
_QosSwitch8948TCCountersDroppedBytes_Object=MibTableColumn
qosSwitch8948TCCountersDroppedBytes=_QosSwitch8948TCCountersDroppedBytes_Object((1,3,6,1,4,1,207,8,4,4,4,99,1,4,2,1,8),_QosSwitch8948TCCountersDroppedBytes_Type())
qosSwitch8948TCCountersDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSwitch8948TCCountersDroppedBytes.setStatus(_A)
qosSwitchPortEntry.registerAugmentions((_D,_W))
qosSwitch8948PortEntry.setIndexNames(*qosSwitchPortEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'qos':qos,'qosSwitch':qosSwitch,'qosSwitchPortTable':qosSwitchPortTable,'qosSwitchPortEntry':qosSwitchPortEntry,_K:qosSwitchPortIndex,'qosSwitchPortPolicyIndex':qosSwitchPortPolicyIndex,'qosSwitchPolicyTable':qosSwitchPolicyTable,'qosSwitchPolicyEntry':qosSwitchPolicyEntry,_L:qosSwitchPolicyIndex,'qosSwitchPolicyDescription':qosSwitchPolicyDescription,'qosSwitchPolicyDefaultTCDropBWClass3':qosSwitchPolicyDefaultTCDropBWClass3,'qosSwitchPolicyDefaultTCIgnoreBWClass':qosSwitchPolicyDefaultTCIgnoreBWClass,'qosSwitchPolicyDefaultTCMarkValue':qosSwitchPolicyDefaultTCMarkValue,'qosSwitchPolicyDefaultTCMaxBandwidth':qosSwitchPolicyDefaultTCMaxBandwidth,'qosSwitchPolicyDefaultTCMaxBurstSize':qosSwitchPolicyDefaultTCMaxBurstSize,'qosSwitchPolicyDefaultTCMinBandwidth':qosSwitchPolicyDefaultTCMinBandwidth,'qosSwitchPolicyDefaultTCMinBurstSize':qosSwitchPolicyDefaultTCMinBurstSize,'qosSwitchPolicyDefaultTCPremarking':qosSwitchPolicyDefaultTCPremarking,'qosSwitchPolicyDefaultTCRemarking':qosSwitchPolicyDefaultTCRemarking,'qosSwitchTrafficClassTable':qosSwitchTrafficClassTable,'qosSwitchTrafficClassEntry':qosSwitchTrafficClassEntry,_S:qosSwitchTrafficClassIndex,'qosSwitchTrafficClassPolicyNumber':qosSwitchTrafficClassPolicyNumber,'qosSwitchTrafficClassDescription':qosSwitchTrafficClassDescription,'qosSwitchTrafficClassDropBWClass3':qosSwitchTrafficClassDropBWClass3,'qosSwitchTrafficClassIgnoreBWClass':qosSwitchTrafficClassIgnoreBWClass,'qosSwitchTrafficClassMarkValue':qosSwitchTrafficClassMarkValue,'qosSwitchTrafficClassMaxBandwidth':qosSwitchTrafficClassMaxBandwidth,'qosSwitchTrafficClassMaxBurstSize':qosSwitchTrafficClassMaxBurstSize,'qosSwitchTrafficClassMinBandwidth':qosSwitchTrafficClassMinBandwidth,'qosSwitchTrafficClassMinBurstSize':qosSwitchTrafficClassMinBurstSize,'qosSwitchTrafficClassPremarking':qosSwitchTrafficClassPremarking,'qosSwitchTrafficClassRemarking':qosSwitchTrafficClassRemarking,'qosSwitch8948':qosSwitch8948,'qosSwitch8948PortTable':qosSwitch8948PortTable,_W:qosSwitch8948PortEntry,'qosSwitch8948PortDefaultTCCountersAggregateBytes':qosSwitch8948PortDefaultTCCountersAggregateBytes,'qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes':qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes,'qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes':qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes,'qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes':qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes,'qosSwitch8948PortDefaultTCCountersDroppedBytes':qosSwitch8948PortDefaultTCCountersDroppedBytes,'qosSwitch8948PortQueueLength':qosSwitch8948PortQueueLength,'qosSwitch8948PortQueue0Length':qosSwitch8948PortQueue0Length,'qosSwitch8948PortQueue1Length':qosSwitch8948PortQueue1Length,'qosSwitch8948PortQueue2Length':qosSwitch8948PortQueue2Length,'qosSwitch8948PortQueue3Length':qosSwitch8948PortQueue3Length,'qosSwitch8948PortQueue4Length':qosSwitch8948PortQueue4Length,'qosSwitch8948PortQueue5Length':qosSwitch8948PortQueue5Length,'qosSwitch8948PortQueue6Length':qosSwitch8948PortQueue6Length,'qosSwitch8948PortQueue7Length':qosSwitch8948PortQueue7Length,'qosSwitch8948TrafficClassCountersTable':qosSwitch8948TrafficClassCountersTable,'qosSwitch8948TrafficClassCountersEntry':qosSwitch8948TrafficClassCountersEntry,_T:qosSwitch8948TCCountersPortIndex,_U:qosSwitch8948TCCountersPolicyIndex,_V:qosSwitch8948TCCountersTrafficClassIndex,'qosSwitch8948TCCountersAggregateBytes':qosSwitch8948TCCountersAggregateBytes,'qosSwitch8948TCCountersBwConformanceClass1Bytes':qosSwitch8948TCCountersBwConformanceClass1Bytes,'qosSwitch8948TCCountersBwConformanceClass2Bytes':qosSwitch8948TCCountersBwConformanceClass2Bytes,'qosSwitch8948TCCountersBwConformanceClass3Bytes':qosSwitch8948TCCountersBwConformanceClass3Bytes,'qosSwitch8948TCCountersDroppedBytes':qosSwitch8948TCCountersDroppedBytes})