_N='enetResultsIndex'
_M='not-accessible'
_L='enetTestIndex'
_K='OctetString'
_J='ELECTROLINE-DHT-ENET-MIB'
_I='Unsigned32'
_H='Gauge32'
_G='active'
_F='notLicensed'
_E='notSupported'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtExtensionsMibObjects,=mibBuilder.importSymbols('ELECTROLINE-DHT-EXTENSIONS-MIB','dhtExtensionsMibObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_H,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
dhtEnetMib=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12))
if mibBuilder.loadTexts:dhtEnetMib.setRevisions(('2006-07-20 00:00','2006-07-27 00:00','2006-08-01 00:00'))
class Rfactor(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120),ValueRangeConstraint(127,127))
class ScaledMOSscore(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,50),ValueRangeConstraint(127,127))
class ScaledPercentage(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_DhtEnetMibObjects_ObjectIdentity=ObjectIdentity
dhtEnetMibObjects=_DhtEnetMibObjects_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1))
_DhtEnetCapabilities_ObjectIdentity=ObjectIdentity
dhtEnetCapabilities=_DhtEnetCapabilities_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1))
_EnetSupport_Type=TruthValue
_EnetSupport_Object=MibScalar
enetSupport=_EnetSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,1),_EnetSupport_Type())
enetSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:enetSupport.setStatus(_A)
_EnetModuleVersion_Type=OctetString
_EnetModuleVersion_Object=MibScalar
enetModuleVersion=_EnetModuleVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,2),_EnetModuleVersion_Type())
enetModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:enetModuleVersion.setStatus(_A)
_EnetMaxTestInstance_Type=Unsigned32
_EnetMaxTestInstance_Object=MibScalar
enetMaxTestInstance=_EnetMaxTestInstance_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,3),_EnetMaxTestInstance_Type())
enetMaxTestInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:enetMaxTestInstance.setStatus(_A)
_EnetPerFeatureSupport_ObjectIdentity=ObjectIdentity
enetPerFeatureSupport=_EnetPerFeatureSupport_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,11))
class _EnetConstellationDisplaySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_EnetConstellationDisplaySupport_Type.__name__=_C
_EnetConstellationDisplaySupport_Object=MibScalar
enetConstellationDisplaySupport=_EnetConstellationDisplaySupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,11,1),_EnetConstellationDisplaySupport_Type())
enetConstellationDisplaySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:enetConstellationDisplaySupport.setStatus(_A)
class _EnetUDPTestSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_EnetUDPTestSupport_Type.__name__=_C
_EnetUDPTestSupport_Object=MibScalar
enetUDPTestSupport=_EnetUDPTestSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,11,2),_EnetUDPTestSupport_Type())
enetUDPTestSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:enetUDPTestSupport.setStatus(_A)
class _EnetVOIPTestSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_EnetVOIPTestSupport_Type.__name__=_C
_EnetVOIPTestSupport_Object=MibScalar
enetVOIPTestSupport=_EnetVOIPTestSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,11,3),_EnetVOIPTestSupport_Type())
enetVOIPTestSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:enetVOIPTestSupport.setStatus(_A)
class _EnetSMRPTestSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_EnetSMRPTestSupport_Type.__name__=_C
_EnetSMRPTestSupport_Object=MibScalar
enetSMRPTestSupport=_EnetSMRPTestSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,1,11,4),_EnetSMRPTestSupport_Type())
enetSMRPTestSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:enetSMRPTestSupport.setStatus(_A)
_DhtEnetGlobalControls_ObjectIdentity=ObjectIdentity
dhtEnetGlobalControls=_DhtEnetGlobalControls_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,2))
_EnetLicenseKey_Type=OctetString
_EnetLicenseKey_Object=MibScalar
enetLicenseKey=_EnetLicenseKey_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,2,1),_EnetLicenseKey_Type())
enetLicenseKey.setMaxAccess(_D)
if mibBuilder.loadTexts:enetLicenseKey.setStatus(_A)
class _EnetPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_EnetPollingInterval_Type.__name__=_C
_EnetPollingInterval_Object=MibScalar
enetPollingInterval=_EnetPollingInterval_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,2,2),_EnetPollingInterval_Type())
enetPollingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:enetPollingInterval.setStatus(_A)
_DhtEnetPacketTests_ObjectIdentity=ObjectIdentity
dhtEnetPacketTests=_DhtEnetPacketTests_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3))
_DhtEnetPktTestControls_ObjectIdentity=ObjectIdentity
dhtEnetPktTestControls=_DhtEnetPktTestControls_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1))
_EnetTestControlTable_Object=MibTable
enetTestControlTable=_EnetTestControlTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1))
if mibBuilder.loadTexts:enetTestControlTable.setStatus(_A)
_EnetTestControlEntry_Object=MibTableRow
enetTestControlEntry=_EnetTestControlEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1))
enetTestControlEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:enetTestControlEntry.setStatus(_A)
_EnetTestIndex_Type=Integer32
_EnetTestIndex_Object=MibTableColumn
enetTestIndex=_EnetTestIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,1),_EnetTestIndex_Type())
enetTestIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:enetTestIndex.setStatus(_A)
_EnetTestIdString_Type=OctetString
_EnetTestIdString_Object=MibTableColumn
enetTestIdString=_EnetTestIdString_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,2),_EnetTestIdString_Type())
enetTestIdString.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestIdString.setStatus(_A)
class _EnetTestControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stopTest',1),('setupTest',2),('startTest',3)))
_EnetTestControl_Type.__name__=_C
_EnetTestControl_Object=MibTableColumn
enetTestControl=_EnetTestControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,3),_EnetTestControl_Type())
enetTestControl.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestControl.setStatus(_A)
_EnetTestSenderIP_Type=IpAddress
_EnetTestSenderIP_Object=MibTableColumn
enetTestSenderIP=_EnetTestSenderIP_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,4),_EnetTestSenderIP_Type())
enetTestSenderIP.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestSenderIP.setStatus(_A)
class _EnetTestSenderUDPPort_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EnetTestSenderUDPPort_Type.__name__=_H
_EnetTestSenderUDPPort_Object=MibTableColumn
enetTestSenderUDPPort=_EnetTestSenderUDPPort_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,5),_EnetTestSenderUDPPort_Type())
enetTestSenderUDPPort.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestSenderUDPPort.setStatus(_A)
_EnetTestReceiverIP_Type=IpAddress
_EnetTestReceiverIP_Object=MibTableColumn
enetTestReceiverIP=_EnetTestReceiverIP_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,6),_EnetTestReceiverIP_Type())
enetTestReceiverIP.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestReceiverIP.setStatus(_A)
class _EnetTestReceiverUDPPort_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EnetTestReceiverUDPPort_Type.__name__=_H
_EnetTestReceiverUDPPort_Object=MibTableColumn
enetTestReceiverUDPPort=_EnetTestReceiverUDPPort_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,7),_EnetTestReceiverUDPPort_Type())
enetTestReceiverUDPPort.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestReceiverUDPPort.setStatus(_A)
class _EnetTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('voip',1),('packetLoss',2)))
_EnetTestType_Type.__name__=_C
_EnetTestType_Object=MibTableColumn
enetTestType=_EnetTestType_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,8),_EnetTestType_Type())
enetTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestType.setStatus(_A)
class _EnetTestPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1514))
_EnetTestPacketSize_Type.__name__=_C
_EnetTestPacketSize_Object=MibTableColumn
enetTestPacketSize=_EnetTestPacketSize_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,9),_EnetTestPacketSize_Type())
enetTestPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestPacketSize.setStatus(_A)
class _EnetTestPacketInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30))
_EnetTestPacketInterval_Type.__name__=_C
_EnetTestPacketInterval_Object=MibTableColumn
enetTestPacketInterval=_EnetTestPacketInterval_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,10),_EnetTestPacketInterval_Type())
enetTestPacketInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestPacketInterval.setStatus(_A)
class _EnetTestPacketRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255000))
_EnetTestPacketRate_Type.__name__=_C
_EnetTestPacketRate_Object=MibTableColumn
enetTestPacketRate=_EnetTestPacketRate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,11),_EnetTestPacketRate_Type())
enetTestPacketRate.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestPacketRate.setStatus(_A)
class _EnetTestNumOfPackets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EnetTestNumOfPackets_Type.__name__=_I
_EnetTestNumOfPackets_Object=MibTableColumn
enetTestNumOfPackets=_EnetTestNumOfPackets_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,12),_EnetTestNumOfPackets_Type())
enetTestNumOfPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestNumOfPackets.setStatus(_A)
class _EnetTestJitterBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_EnetTestJitterBufferSize_Type.__name__=_C
_EnetTestJitterBufferSize_Object=MibTableColumn
enetTestJitterBufferSize=_EnetTestJitterBufferSize_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,13),_EnetTestJitterBufferSize_Type())
enetTestJitterBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestJitterBufferSize.setStatus(_A)
class _EnetTestQosControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('preestablished',2),('dsa',3)))
_EnetTestQosControl_Type.__name__=_C
_EnetTestQosControl_Object=MibTableColumn
enetTestQosControl=_EnetTestQosControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,14),_EnetTestQosControl_Type())
enetTestQosControl.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestQosControl.setStatus(_A)
class _EnetTestCodecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('na',0),('g711',1)))
_EnetTestCodecType_Type.__name__=_C
_EnetTestCodecType_Object=MibTableColumn
enetTestCodecType=_EnetTestCodecType_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,15),_EnetTestCodecType_Type())
enetTestCodecType.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestCodecType.setStatus(_A)
class _EnetTestTosByte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EnetTestTosByte_Type.__name__=_C
_EnetTestTosByte_Object=MibTableColumn
enetTestTosByte=_EnetTestTosByte_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,16),_EnetTestTosByte_Type())
enetTestTosByte.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestTosByte.setStatus(_A)
class _EnetTestRoundTripTimeEstimate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_EnetTestRoundTripTimeEstimate_Type.__name__=_C
_EnetTestRoundTripTimeEstimate_Object=MibTableColumn
enetTestRoundTripTimeEstimate=_EnetTestRoundTripTimeEstimate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,17),_EnetTestRoundTripTimeEstimate_Type())
enetTestRoundTripTimeEstimate.setMaxAccess(_D)
if mibBuilder.loadTexts:enetTestRoundTripTimeEstimate.setStatus(_A)
class _EnetTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('na',0),('running',1),('completed',2),('ressourceUnavailable',3),('invalidParameter',4),('ready',5)))
_EnetTestStatus_Type.__name__=_C
_EnetTestStatus_Object=MibTableColumn
enetTestStatus=_EnetTestStatus_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,18),_EnetTestStatus_Type())
enetTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:enetTestStatus.setStatus(_A)
class _EnetTestStatusString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EnetTestStatusString_Type.__name__=_K
_EnetTestStatusString_Object=MibTableColumn
enetTestStatusString=_EnetTestStatusString_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,1,1,1,19),_EnetTestStatusString_Type())
enetTestStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:enetTestStatusString.setStatus(_A)
_DhtEnetPktTestResults_ObjectIdentity=ObjectIdentity
dhtEnetPktTestResults=_DhtEnetPktTestResults_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3))
_EnetCurrentResultsTable_Object=MibTable
enetCurrentResultsTable=_EnetCurrentResultsTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1))
if mibBuilder.loadTexts:enetCurrentResultsTable.setStatus(_A)
_EnetCurrentResultsEntry_Object=MibTableRow
enetCurrentResultsEntry=_EnetCurrentResultsEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1))
enetCurrentResultsEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:enetCurrentResultsEntry.setStatus(_A)
class _EnetResultsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EnetResultsIndex_Type.__name__=_I
_EnetResultsIndex_Object=MibTableColumn
enetResultsIndex=_EnetResultsIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,1),_EnetResultsIndex_Type())
enetResultsIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:enetResultsIndex.setStatus(_A)
_EnetResultsIdString_Type=OctetString
_EnetResultsIdString_Object=MibTableColumn
enetResultsIdString=_EnetResultsIdString_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,2),_EnetResultsIdString_Type())
enetResultsIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsIdString.setStatus(_A)
class _EnetResultsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inconsistent',0),('partial',1),('complete',2)))
_EnetResultsStatus_Type.__name__=_C
_EnetResultsStatus_Object=MibTableColumn
enetResultsStatus=_EnetResultsStatus_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,3),_EnetResultsStatus_Type())
enetResultsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsStatus.setStatus(_A)
_EnetResultsDuration_Type=Unsigned32
_EnetResultsDuration_Object=MibTableColumn
enetResultsDuration=_EnetResultsDuration_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,4),_EnetResultsDuration_Type())
enetResultsDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsDuration.setStatus(_A)
_EnetResultsStartTime_Type=DateAndTime
_EnetResultsStartTime_Object=MibTableColumn
enetResultsStartTime=_EnetResultsStartTime_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,5),_EnetResultsStartTime_Type())
enetResultsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsStartTime.setStatus(_A)
_EnetResultsStopTime_Type=DateAndTime
_EnetResultsStopTime_Object=MibTableColumn
enetResultsStopTime=_EnetResultsStopTime_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,6),_EnetResultsStopTime_Type())
enetResultsStopTime.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsStopTime.setStatus(_A)
_EnetResultsProcessedPacketCount_Type=Gauge32
_EnetResultsProcessedPacketCount_Object=MibTableColumn
enetResultsProcessedPacketCount=_EnetResultsProcessedPacketCount_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,7),_EnetResultsProcessedPacketCount_Type())
enetResultsProcessedPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsProcessedPacketCount.setStatus(_A)
_EnetResultsLossPacketCount_Type=Gauge32
_EnetResultsLossPacketCount_Object=MibTableColumn
enetResultsLossPacketCount=_EnetResultsLossPacketCount_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,8),_EnetResultsLossPacketCount_Type())
enetResultsLossPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsLossPacketCount.setStatus(_A)
_EnetResultsDiscardedPacketCount_Type=Gauge32
_EnetResultsDiscardedPacketCount_Object=MibTableColumn
enetResultsDiscardedPacketCount=_EnetResultsDiscardedPacketCount_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,9),_EnetResultsDiscardedPacketCount_Type())
enetResultsDiscardedPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsDiscardedPacketCount.setStatus(_A)
_EnetResultsPacketLossRate_Type=ScaledPercentage
_EnetResultsPacketLossRate_Object=MibTableColumn
enetResultsPacketLossRate=_EnetResultsPacketLossRate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,10),_EnetResultsPacketLossRate_Type())
enetResultsPacketLossRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsPacketLossRate.setStatus(_A)
_EnetResultsPacketDiscardRate_Type=ScaledPercentage
_EnetResultsPacketDiscardRate_Object=MibTableColumn
enetResultsPacketDiscardRate=_EnetResultsPacketDiscardRate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,11),_EnetResultsPacketDiscardRate_Type())
enetResultsPacketDiscardRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsPacketDiscardRate.setStatus(_A)
_EnetResultsMinInstantJitter_Type=Gauge32
_EnetResultsMinInstantJitter_Object=MibTableColumn
enetResultsMinInstantJitter=_EnetResultsMinInstantJitter_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,12),_EnetResultsMinInstantJitter_Type())
enetResultsMinInstantJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMinInstantJitter.setStatus(_A)
_EnetResultsMaxInstantJitter_Type=Gauge32
_EnetResultsMaxInstantJitter_Object=MibTableColumn
enetResultsMaxInstantJitter=_EnetResultsMaxInstantJitter_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,13),_EnetResultsMaxInstantJitter_Type())
enetResultsMaxInstantJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMaxInstantJitter.setStatus(_A)
_EnetResultsAvgInstantJitter_Type=Gauge32
_EnetResultsAvgInstantJitter_Object=MibTableColumn
enetResultsAvgInstantJitter=_EnetResultsAvgInstantJitter_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,14),_EnetResultsAvgInstantJitter_Type())
enetResultsAvgInstantJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsAvgInstantJitter.setStatus(_A)
_EnetResultsMinRfcJitterLevel_Type=Gauge32
_EnetResultsMinRfcJitterLevel_Object=MibTableColumn
enetResultsMinRfcJitterLevel=_EnetResultsMinRfcJitterLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,15),_EnetResultsMinRfcJitterLevel_Type())
enetResultsMinRfcJitterLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMinRfcJitterLevel.setStatus(_A)
_EnetResultsMaxRfcJitterLevel_Type=Gauge32
_EnetResultsMaxRfcJitterLevel_Object=MibTableColumn
enetResultsMaxRfcJitterLevel=_EnetResultsMaxRfcJitterLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,16),_EnetResultsMaxRfcJitterLevel_Type())
enetResultsMaxRfcJitterLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMaxRfcJitterLevel.setStatus(_A)
_EnetResultsAvgRfcJitterLevel_Type=Gauge32
_EnetResultsAvgRfcJitterLevel_Object=MibTableColumn
enetResultsAvgRfcJitterLevel=_EnetResultsAvgRfcJitterLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,17),_EnetResultsAvgRfcJitterLevel_Type())
enetResultsAvgRfcJitterLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsAvgRfcJitterLevel.setStatus(_A)
_EnetResultsRCQ_Type=Rfactor
_EnetResultsRCQ_Object=MibTableColumn
enetResultsRCQ=_EnetResultsRCQ_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,18),_EnetResultsRCQ_Type())
enetResultsRCQ.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsRCQ.setStatus(_A)
_EnetResultsRLQ_Type=Rfactor
_EnetResultsRLQ_Object=MibTableColumn
enetResultsRLQ=_EnetResultsRLQ_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,19),_EnetResultsRLQ_Type())
enetResultsRLQ.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsRLQ.setStatus(_A)
_EnetResultsMOSCQ_Type=ScaledMOSscore
_EnetResultsMOSCQ_Object=MibTableColumn
enetResultsMOSCQ=_EnetResultsMOSCQ_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,20),_EnetResultsMOSCQ_Type())
enetResultsMOSCQ.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMOSCQ.setStatus(_A)
_EnetResultsMOSLQ_Type=ScaledMOSscore
_EnetResultsMOSLQ_Object=MibTableColumn
enetResultsMOSLQ=_EnetResultsMOSLQ_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,3,3,1,1,21),_EnetResultsMOSLQ_Type())
enetResultsMOSLQ.setMaxAccess(_B)
if mibBuilder.loadTexts:enetResultsMOSLQ.setStatus(_A)
_DhtEnetDOCSISMonitoring_ObjectIdentity=ObjectIdentity
dhtEnetDOCSISMonitoring=_DhtEnetDOCSISMonitoring_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4))
class _EnetDocsisMonResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_EnetDocsisMonResetCounters_Type.__name__=_C
_EnetDocsisMonResetCounters_Object=MibScalar
enetDocsisMonResetCounters=_EnetDocsisMonResetCounters_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,1),_EnetDocsisMonResetCounters_Type())
enetDocsisMonResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:enetDocsisMonResetCounters.setStatus(_A)
_EnetDocsisMonPreFECErrorRate_Type=OctetString
_EnetDocsisMonPreFECErrorRate_Object=MibScalar
enetDocsisMonPreFECErrorRate=_EnetDocsisMonPreFECErrorRate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,2),_EnetDocsisMonPreFECErrorRate_Type())
enetDocsisMonPreFECErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enetDocsisMonPreFECErrorRate.setStatus(_A)
_EnetDocsisMonPostFECErrorRate_Type=OctetString
_EnetDocsisMonPostFECErrorRate_Object=MibScalar
enetDocsisMonPostFECErrorRate=_EnetDocsisMonPostFECErrorRate_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,3),_EnetDocsisMonPostFECErrorRate_Type())
enetDocsisMonPostFECErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:enetDocsisMonPostFECErrorRate.setStatus(_A)
_EnetDocsisMonErroredSeconds_Type=Gauge32
_EnetDocsisMonErroredSeconds_Object=MibScalar
enetDocsisMonErroredSeconds=_EnetDocsisMonErroredSeconds_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,4),_EnetDocsisMonErroredSeconds_Type())
enetDocsisMonErroredSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:enetDocsisMonErroredSeconds.setStatus(_A)
_EnetDocsisMonSeverelyErroredSeconds_Type=Gauge32
_EnetDocsisMonSeverelyErroredSeconds_Object=MibScalar
enetDocsisMonSeverelyErroredSeconds=_EnetDocsisMonSeverelyErroredSeconds_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,5),_EnetDocsisMonSeverelyErroredSeconds_Type())
enetDocsisMonSeverelyErroredSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:enetDocsisMonSeverelyErroredSeconds.setStatus(_A)
_EnetDocsisMonTimeElapsed_Type=Gauge32
_EnetDocsisMonTimeElapsed_Object=MibScalar
enetDocsisMonTimeElapsed=_EnetDocsisMonTimeElapsed_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,12,1,4,6),_EnetDocsisMonTimeElapsed_Type())
enetDocsisMonTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:enetDocsisMonTimeElapsed.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'Rfactor':Rfactor,'ScaledMOSscore':ScaledMOSscore,'ScaledPercentage':ScaledPercentage,'dhtEnetMib':dhtEnetMib,'dhtEnetMibObjects':dhtEnetMibObjects,'dhtEnetCapabilities':dhtEnetCapabilities,'enetSupport':enetSupport,'enetModuleVersion':enetModuleVersion,'enetMaxTestInstance':enetMaxTestInstance,'enetPerFeatureSupport':enetPerFeatureSupport,'enetConstellationDisplaySupport':enetConstellationDisplaySupport,'enetUDPTestSupport':enetUDPTestSupport,'enetVOIPTestSupport':enetVOIPTestSupport,'enetSMRPTestSupport':enetSMRPTestSupport,'dhtEnetGlobalControls':dhtEnetGlobalControls,'enetLicenseKey':enetLicenseKey,'enetPollingInterval':enetPollingInterval,'dhtEnetPacketTests':dhtEnetPacketTests,'dhtEnetPktTestControls':dhtEnetPktTestControls,'enetTestControlTable':enetTestControlTable,'enetTestControlEntry':enetTestControlEntry,_L:enetTestIndex,'enetTestIdString':enetTestIdString,'enetTestControl':enetTestControl,'enetTestSenderIP':enetTestSenderIP,'enetTestSenderUDPPort':enetTestSenderUDPPort,'enetTestReceiverIP':enetTestReceiverIP,'enetTestReceiverUDPPort':enetTestReceiverUDPPort,'enetTestType':enetTestType,'enetTestPacketSize':enetTestPacketSize,'enetTestPacketInterval':enetTestPacketInterval,'enetTestPacketRate':enetTestPacketRate,'enetTestNumOfPackets':enetTestNumOfPackets,'enetTestJitterBufferSize':enetTestJitterBufferSize,'enetTestQosControl':enetTestQosControl,'enetTestCodecType':enetTestCodecType,'enetTestTosByte':enetTestTosByte,'enetTestRoundTripTimeEstimate':enetTestRoundTripTimeEstimate,'enetTestStatus':enetTestStatus,'enetTestStatusString':enetTestStatusString,'dhtEnetPktTestResults':dhtEnetPktTestResults,'enetCurrentResultsTable':enetCurrentResultsTable,'enetCurrentResultsEntry':enetCurrentResultsEntry,_N:enetResultsIndex,'enetResultsIdString':enetResultsIdString,'enetResultsStatus':enetResultsStatus,'enetResultsDuration':enetResultsDuration,'enetResultsStartTime':enetResultsStartTime,'enetResultsStopTime':enetResultsStopTime,'enetResultsProcessedPacketCount':enetResultsProcessedPacketCount,'enetResultsLossPacketCount':enetResultsLossPacketCount,'enetResultsDiscardedPacketCount':enetResultsDiscardedPacketCount,'enetResultsPacketLossRate':enetResultsPacketLossRate,'enetResultsPacketDiscardRate':enetResultsPacketDiscardRate,'enetResultsMinInstantJitter':enetResultsMinInstantJitter,'enetResultsMaxInstantJitter':enetResultsMaxInstantJitter,'enetResultsAvgInstantJitter':enetResultsAvgInstantJitter,'enetResultsMinRfcJitterLevel':enetResultsMinRfcJitterLevel,'enetResultsMaxRfcJitterLevel':enetResultsMaxRfcJitterLevel,'enetResultsAvgRfcJitterLevel':enetResultsAvgRfcJitterLevel,'enetResultsRCQ':enetResultsRCQ,'enetResultsRLQ':enetResultsRLQ,'enetResultsMOSCQ':enetResultsMOSCQ,'enetResultsMOSLQ':enetResultsMOSLQ,'dhtEnetDOCSISMonitoring':dhtEnetDOCSISMonitoring,'enetDocsisMonResetCounters':enetDocsisMonResetCounters,'enetDocsisMonPreFECErrorRate':enetDocsisMonPreFECErrorRate,'enetDocsisMonPostFECErrorRate':enetDocsisMonPostFECErrorRate,'enetDocsisMonErroredSeconds':enetDocsisMonErroredSeconds,'enetDocsisMonSeverelyErroredSeconds':enetDocsisMonSeverelyErroredSeconds,'enetDocsisMonTimeElapsed':enetDocsisMonTimeElapsed})