_Q='destroy'
_P='deactivate'
_O='activate'
_N='a3ComPollIndex'
_M='NotificationType'
_L='a3ComPollFramesReceived'
_K='a3ComPollFramesSent'
_J='a3ComPollRate'
_I='a3ComPollAttempts'
_H='a3ComPollAddressType'
_G='a3ComPollAddress'
_F='DisplayString'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='A3COM-SWITCHING-SYSTEMS-POLL-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_M,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComPoll_ObjectIdentity=ObjectIdentity
a3ComPoll=_A3ComPoll_ObjectIdentity((1,3,6,1,4,1,43,29,4,22))
_A3ComPollTable_Object=MibTable
a3ComPollTable=_A3ComPollTable_Object((1,3,6,1,4,1,43,29,4,22,1))
if mibBuilder.loadTexts:a3ComPollTable.setStatus(_A)
_A3ComPollEntry_Object=MibTableRow
a3ComPollEntry=_A3ComPollEntry_Object((1,3,6,1,4,1,43,29,4,22,1,1))
a3ComPollEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:a3ComPollEntry.setStatus(_A)
class _A3ComPollIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3ComPollIndex_Type.__name__=_C
_A3ComPollIndex_Object=MibTableColumn
a3ComPollIndex=_A3ComPollIndex_Object((1,3,6,1,4,1,43,29,4,22,1,1,1),_A3ComPollIndex_Type())
a3ComPollIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollIndex.setStatus(_A)
class _A3ComPollAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3ComPollAddress_Type.__name__=_F
_A3ComPollAddress_Object=MibTableColumn
a3ComPollAddress=_A3ComPollAddress_Object((1,3,6,1,4,1,43,29,4,22,1,1,2),_A3ComPollAddress_Type())
a3ComPollAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollAddress.setStatus(_A)
class _A3ComPollAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('ip',2),('ipdotted',3),('ipname',4),('ipx',5),('appletalk',6)))
_A3ComPollAddressType_Type.__name__=_C
_A3ComPollAddressType_Object=MibTableColumn
a3ComPollAddressType=_A3ComPollAddressType_Object((1,3,6,1,4,1,43,29,4,22,1,1,3),_A3ComPollAddressType_Type())
a3ComPollAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollAddressType.setStatus(_A)
class _A3ComPollCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_A3ComPollCount_Type.__name__=_C
_A3ComPollCount_Object=MibTableColumn
a3ComPollCount=_A3ComPollCount_Object((1,3,6,1,4,1,43,29,4,22,1,1,4),_A3ComPollCount_Type())
a3ComPollCount.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollCount.setStatus(_A)
class _A3ComPollAttempts_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A3ComPollAttempts_Type.__name__=_C
_A3ComPollAttempts_Object=MibTableColumn
a3ComPollAttempts=_A3ComPollAttempts_Object((1,3,6,1,4,1,43,29,4,22,1,1,5),_A3ComPollAttempts_Type())
a3ComPollAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollAttempts.setStatus(_A)
class _A3ComPollRate_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5400))
_A3ComPollRate_Type.__name__=_C
_A3ComPollRate_Object=MibTableColumn
a3ComPollRate=_A3ComPollRate_Object((1,3,6,1,4,1,43,29,4,22,1,1,6),_A3ComPollRate_Type())
a3ComPollRate.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollRate.setStatus(_A)
class _A3ComPollResponseTimeOut_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComPollResponseTimeOut_Type.__name__=_C
_A3ComPollResponseTimeOut_Object=MibTableColumn
a3ComPollResponseTimeOut=_A3ComPollResponseTimeOut_Object((1,3,6,1,4,1,43,29,4,22,1,1,7),_A3ComPollResponseTimeOut_Type())
a3ComPollResponseTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollResponseTimeOut.setStatus(_A)
class _A3ComPollPacketSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_A3ComPollPacketSize_Type.__name__=_C
_A3ComPollPacketSize_Object=MibTableColumn
a3ComPollPacketSize=_A3ComPollPacketSize_Object((1,3,6,1,4,1,43,29,4,22,1,1,8),_A3ComPollPacketSize_Type())
a3ComPollPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollPacketSize.setStatus(_A)
class _A3ComPollSourceAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_A3ComPollSourceAddress_Type.__name__=_F
_A3ComPollSourceAddress_Object=MibTableColumn
a3ComPollSourceAddress=_A3ComPollSourceAddress_Object((1,3,6,1,4,1,43,29,4,22,1,1,9),_A3ComPollSourceAddress_Type())
a3ComPollSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollSourceAddress.setStatus(_A)
_A3ComPollMinRoundTripTime_Type=Integer32
_A3ComPollMinRoundTripTime_Object=MibTableColumn
a3ComPollMinRoundTripTime=_A3ComPollMinRoundTripTime_Object((1,3,6,1,4,1,43,29,4,22,1,1,10),_A3ComPollMinRoundTripTime_Type())
a3ComPollMinRoundTripTime.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollMinRoundTripTime.setStatus(_A)
_A3ComPollAvgRoundTripTime_Type=Integer32
_A3ComPollAvgRoundTripTime_Object=MibTableColumn
a3ComPollAvgRoundTripTime=_A3ComPollAvgRoundTripTime_Object((1,3,6,1,4,1,43,29,4,22,1,1,11),_A3ComPollAvgRoundTripTime_Type())
a3ComPollAvgRoundTripTime.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollAvgRoundTripTime.setStatus(_A)
_A3ComPollMaxRoundTripTime_Type=Integer32
_A3ComPollMaxRoundTripTime_Object=MibTableColumn
a3ComPollMaxRoundTripTime=_A3ComPollMaxRoundTripTime_Object((1,3,6,1,4,1,43,29,4,22,1,1,12),_A3ComPollMaxRoundTripTime_Type())
a3ComPollMaxRoundTripTime.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollMaxRoundTripTime.setStatus(_A)
_A3ComPollFramesSent_Type=Integer32
_A3ComPollFramesSent_Object=MibTableColumn
a3ComPollFramesSent=_A3ComPollFramesSent_Object((1,3,6,1,4,1,43,29,4,22,1,1,13),_A3ComPollFramesSent_Type())
a3ComPollFramesSent.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollFramesSent.setStatus(_A)
_A3ComPollFramesReceived_Type=Integer32
_A3ComPollFramesReceived_Object=MibTableColumn
a3ComPollFramesReceived=_A3ComPollFramesReceived_Object((1,3,6,1,4,1,43,29,4,22,1,1,14),_A3ComPollFramesReceived_Type())
a3ComPollFramesReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollFramesReceived.setStatus(_A)
class _A3ComPollInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_A3ComPollInformation_Type.__name__=_F
_A3ComPollInformation_Object=MibTableColumn
a3ComPollInformation=_A3ComPollInformation_Object((1,3,6,1,4,1,43,29,4,22,1,1,15),_A3ComPollInformation_Type())
a3ComPollInformation.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollInformation.setStatus(_A)
_A3ComPollOwner_Type=DisplayString
_A3ComPollOwner_Object=MibTableColumn
a3ComPollOwner=_A3ComPollOwner_Object((1,3,6,1,4,1,43,29,4,22,1,1,16),_A3ComPollOwner_Type())
a3ComPollOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollOwner.setStatus(_A)
class _A3ComPollReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('idle',1),('busy',2),('badArgument',3),('noResource',4),('nameLookupFailed',5),('hostAlive',6),('hostUnreachable',7),('hostNotResponding',8)))
_A3ComPollReport_Type.__name__=_C
_A3ComPollReport_Object=MibTableColumn
a3ComPollReport=_A3ComPollReport_Object((1,3,6,1,4,1,43,29,4,22,1,1,17),_A3ComPollReport_Type())
a3ComPollReport.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollReport.setStatus(_A)
class _A3ComPollAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noop',1),(_O,2),(_P,3),('reset',4),(_Q,5)))
_A3ComPollAction_Type.__name__=_C
_A3ComPollAction_Object=MibTableColumn
a3ComPollAction=_A3ComPollAction_Object((1,3,6,1,4,1,43,29,4,22,1,1,18),_A3ComPollAction_Type())
a3ComPollAction.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollAction.setStatus(_A)
_A3ComPollNextFreeIndex_Type=Integer32
_A3ComPollNextFreeIndex_Object=MibScalar
a3ComPollNextFreeIndex=_A3ComPollNextFreeIndex_Object((1,3,6,1,4,1,43,29,4,22,2),_A3ComPollNextFreeIndex_Type())
a3ComPollNextFreeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollNextFreeIndex.setStatus(_A)
class _A3ComPollTableInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_A3ComPollTableInformation_Type.__name__=_F
_A3ComPollTableInformation_Object=MibScalar
a3ComPollTableInformation=_A3ComPollTableInformation_Object((1,3,6,1,4,1,43,29,4,22,3),_A3ComPollTableInformation_Type())
a3ComPollTableInformation.setMaxAccess(_E)
if mibBuilder.loadTexts:a3ComPollTableInformation.setStatus(_A)
class _A3ComPollTableActionAll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noop',1),(_O,2),(_P,3),('reset',4),(_Q,5)))
_A3ComPollTableActionAll_Type.__name__=_C
_A3ComPollTableActionAll_Object=MibScalar
a3ComPollTableActionAll=_A3ComPollTableActionAll_Object((1,3,6,1,4,1,43,29,4,22,4),_A3ComPollTableActionAll_Type())
a3ComPollTableActionAll.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPollTableActionAll.setStatus(_A)
a3ComPollResponseReceived=NotificationType((1,3,6,1,4,1,43,29,4,0,61))
a3ComPollResponseReceived.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:a3ComPollResponseReceived.setStatus('')
a3ComPollResponseNotReceived=NotificationType((1,3,6,1,4,1,43,29,4,0,62))
a3ComPollResponseNotReceived.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:a3ComPollResponseNotReceived.setStatus('')
mibBuilder.exportSymbols(_B,**{'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComPollResponseReceived':a3ComPollResponseReceived,'a3ComPollResponseNotReceived':a3ComPollResponseNotReceived,'a3ComPoll':a3ComPoll,'a3ComPollTable':a3ComPollTable,'a3ComPollEntry':a3ComPollEntry,_N:a3ComPollIndex,_G:a3ComPollAddress,_H:a3ComPollAddressType,'a3ComPollCount':a3ComPollCount,_I:a3ComPollAttempts,_J:a3ComPollRate,'a3ComPollResponseTimeOut':a3ComPollResponseTimeOut,'a3ComPollPacketSize':a3ComPollPacketSize,'a3ComPollSourceAddress':a3ComPollSourceAddress,'a3ComPollMinRoundTripTime':a3ComPollMinRoundTripTime,'a3ComPollAvgRoundTripTime':a3ComPollAvgRoundTripTime,'a3ComPollMaxRoundTripTime':a3ComPollMaxRoundTripTime,_K:a3ComPollFramesSent,_L:a3ComPollFramesReceived,'a3ComPollInformation':a3ComPollInformation,'a3ComPollOwner':a3ComPollOwner,'a3ComPollReport':a3ComPollReport,'a3ComPollAction':a3ComPollAction,'a3ComPollNextFreeIndex':a3ComPollNextFreeIndex,'a3ComPollTableInformation':a3ComPollTableInformation,'a3ComPollTableActionAll':a3ComPollTableActionAll})