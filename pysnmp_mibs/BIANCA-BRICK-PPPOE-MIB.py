_J='pppoePassThroughEthIfIndex2'
_I='pppoePassThroughEthIfIndex1'
_H='pppoeCreditsService'
_G='pppoeCallId'
_F='delete'
_E='BIANCA-BRICK-PPPOE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Pppoe_ObjectIdentity=ObjectIdentity
pppoe=_Pppoe_ObjectIdentity((1,3,6,1,4,1,272,4,24))
_PppoeCallTable_Object=MibTable
pppoeCallTable=_PppoeCallTable_Object((1,3,6,1,4,1,272,4,24,1))
if mibBuilder.loadTexts:pppoeCallTable.setStatus(_A)
_PppoeCallEntry_Object=MibTableRow
pppoeCallEntry=_PppoeCallEntry_Object((1,3,6,1,4,1,272,4,24,1,1))
pppoeCallEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:pppoeCallEntry.setStatus(_A)
_PppoeCallId_Type=Integer32
_PppoeCallId_Object=MibTableColumn
pppoeCallId=_PppoeCallId_Object((1,3,6,1,4,1,272,4,24,1,1,1),_PppoeCallId_Type())
pppoeCallId.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallId.setStatus(_A)
class _PppoeCallDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('incoming',1),('outgoing',2)))
_PppoeCallDirection_Type.__name__=_D
_PppoeCallDirection_Object=MibTableColumn
pppoeCallDirection=_PppoeCallDirection_Object((1,3,6,1,4,1,272,4,24,1,1,2),_PppoeCallDirection_Type())
pppoeCallDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallDirection.setStatus(_A)
_PppoeCallAge_Type=TimeTicks
_PppoeCallAge_Object=MibTableColumn
pppoeCallAge=_PppoeCallAge_Object((1,3,6,1,4,1,272,4,24,1,1,3),_PppoeCallAge_Type())
pppoeCallAge.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallAge.setStatus(_A)
class _PppoeCallState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('idle',1),('wait-pado',2),('wait-padr',3),('wait-pads',4),('established',5),('terminated',6),('close',7),(_F,8)))
_PppoeCallState_Type.__name__=_D
_PppoeCallState_Object=MibTableColumn
pppoeCallState=_PppoeCallState_Object((1,3,6,1,4,1,272,4,24,1,1,4),_PppoeCallState_Type())
pppoeCallState.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCallState.setStatus(_A)
_PppoeCallRemotePhysAddress_Type=PhysAddress
_PppoeCallRemotePhysAddress_Object=MibTableColumn
pppoeCallRemotePhysAddress=_PppoeCallRemotePhysAddress_Object((1,3,6,1,4,1,272,4,24,1,1,5),_PppoeCallRemotePhysAddress_Type())
pppoeCallRemotePhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallRemotePhysAddress.setStatus(_A)
_PppoeCallLocalPhysAddress_Type=PhysAddress
_PppoeCallLocalPhysAddress_Object=MibTableColumn
pppoeCallLocalPhysAddress=_PppoeCallLocalPhysAddress_Object((1,3,6,1,4,1,272,4,24,1,1,6),_PppoeCallLocalPhysAddress_Type())
pppoeCallLocalPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallLocalPhysAddress.setStatus(_A)
_PppoeCallAcName_Type=DisplayString
_PppoeCallAcName_Object=MibTableColumn
pppoeCallAcName=_PppoeCallAcName_Object((1,3,6,1,4,1,272,4,24,1,1,7),_PppoeCallAcName_Type())
pppoeCallAcName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallAcName.setStatus(_A)
_PppoeCallService_Type=DisplayString
_PppoeCallService_Object=MibTableColumn
pppoeCallService=_PppoeCallService_Object((1,3,6,1,4,1,272,4,24,1,1,8),_PppoeCallService_Type())
pppoeCallService.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallService.setStatus(_A)
_PppoeCallReceivedPackets_Type=Counter32
_PppoeCallReceivedPackets_Object=MibTableColumn
pppoeCallReceivedPackets=_PppoeCallReceivedPackets_Object((1,3,6,1,4,1,272,4,24,1,1,9),_PppoeCallReceivedPackets_Type())
pppoeCallReceivedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallReceivedPackets.setStatus(_A)
_PppoeCallReceivedOctets_Type=Counter32
_PppoeCallReceivedOctets_Object=MibTableColumn
pppoeCallReceivedOctets=_PppoeCallReceivedOctets_Object((1,3,6,1,4,1,272,4,24,1,1,10),_PppoeCallReceivedOctets_Type())
pppoeCallReceivedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallReceivedOctets.setStatus(_A)
_PppoeCallReceivedErrors_Type=Counter32
_PppoeCallReceivedErrors_Object=MibTableColumn
pppoeCallReceivedErrors=_PppoeCallReceivedErrors_Object((1,3,6,1,4,1,272,4,24,1,1,11),_PppoeCallReceivedErrors_Type())
pppoeCallReceivedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallReceivedErrors.setStatus(_A)
_PppoeCallTransmitPackets_Type=Counter32
_PppoeCallTransmitPackets_Object=MibTableColumn
pppoeCallTransmitPackets=_PppoeCallTransmitPackets_Object((1,3,6,1,4,1,272,4,24,1,1,12),_PppoeCallTransmitPackets_Type())
pppoeCallTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallTransmitPackets.setStatus(_A)
_PppoeCallTransmitOctets_Type=Counter32
_PppoeCallTransmitOctets_Object=MibTableColumn
pppoeCallTransmitOctets=_PppoeCallTransmitOctets_Object((1,3,6,1,4,1,272,4,24,1,1,13),_PppoeCallTransmitOctets_Type())
pppoeCallTransmitOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallTransmitOctets.setStatus(_A)
_PppoeCallTransmitErrors_Type=Counter32
_PppoeCallTransmitErrors_Object=MibTableColumn
pppoeCallTransmitErrors=_PppoeCallTransmitErrors_Object((1,3,6,1,4,1,272,4,24,1,1,14),_PppoeCallTransmitErrors_Type())
pppoeCallTransmitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallTransmitErrors.setStatus(_A)
_PppoeCallInfo_Type=DisplayString
_PppoeCallInfo_Object=MibTableColumn
pppoeCallInfo=_PppoeCallInfo_Object((1,3,6,1,4,1,272,4,24,1,1,15),_PppoeCallInfo_Type())
pppoeCallInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallInfo.setStatus(_A)
_PppoeCallSessionId_Type=Integer32
_PppoeCallSessionId_Object=MibTableColumn
pppoeCallSessionId=_PppoeCallSessionId_Object((1,3,6,1,4,1,272,4,24,1,1,16),_PppoeCallSessionId_Type())
pppoeCallSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallSessionId.setStatus(_A)
_PppoeCallEthIfIndex_Type=Integer32
_PppoeCallEthIfIndex_Object=MibTableColumn
pppoeCallEthIfIndex=_PppoeCallEthIfIndex_Object((1,3,6,1,4,1,272,4,24,1,1,17),_PppoeCallEthIfIndex_Type())
pppoeCallEthIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallEthIfIndex.setStatus(_A)
_PppoeCallAssociatedIfIndex_Type=Integer32
_PppoeCallAssociatedIfIndex_Object=MibTableColumn
pppoeCallAssociatedIfIndex=_PppoeCallAssociatedIfIndex_Object((1,3,6,1,4,1,272,4,24,1,1,18),_PppoeCallAssociatedIfIndex_Type())
pppoeCallAssociatedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCallAssociatedIfIndex.setStatus(_A)
_PppoeCreditsTable_Object=MibTable
pppoeCreditsTable=_PppoeCreditsTable_Object((1,3,6,1,4,1,272,4,24,2))
if mibBuilder.loadTexts:pppoeCreditsTable.setStatus(_A)
_PppoeCreditsEntry_Object=MibTableRow
pppoeCreditsEntry=_PppoeCreditsEntry_Object((1,3,6,1,4,1,272,4,24,2,1))
pppoeCreditsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:pppoeCreditsEntry.setStatus(_A)
_PppoeCreditsService_Type=DisplayString
_PppoeCreditsService_Object=MibTableColumn
pppoeCreditsService=_PppoeCreditsService_Object((1,3,6,1,4,1,272,4,24,2,1,1),_PppoeCreditsService_Type())
pppoeCreditsService.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsService.setStatus(_A)
class _PppoeCreditsSurveillance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),(_F,3)))
_PppoeCreditsSurveillance_Type.__name__=_D
_PppoeCreditsSurveillance_Object=MibTableColumn
pppoeCreditsSurveillance=_PppoeCreditsSurveillance_Object((1,3,6,1,4,1,272,4,24,2,1,2),_PppoeCreditsSurveillance_Type())
pppoeCreditsSurveillance.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsSurveillance.setStatus(_A)
class _PppoeCreditsMeasuretime_Type(Integer32):defaultValue=86400
_PppoeCreditsMeasuretime_Type.__name__=_D
_PppoeCreditsMeasuretime_Object=MibTableColumn
pppoeCreditsMeasuretime=_PppoeCreditsMeasuretime_Object((1,3,6,1,4,1,272,4,24,2,1,3),_PppoeCreditsMeasuretime_Type())
pppoeCreditsMeasuretime.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsMeasuretime.setStatus(_A)
class _PppoeCreditsMaxInCon_Type(Integer32):defaultValue=-1
_PppoeCreditsMaxInCon_Type.__name__=_D
_PppoeCreditsMaxInCon_Object=MibTableColumn
pppoeCreditsMaxInCon=_PppoeCreditsMaxInCon_Object((1,3,6,1,4,1,272,4,24,2,1,4),_PppoeCreditsMaxInCon_Type())
pppoeCreditsMaxInCon.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsMaxInCon.setStatus(_A)
class _PppoeCreditsMaxOutCon_Type(Integer32):defaultValue=1000
_PppoeCreditsMaxOutCon_Type.__name__=_D
_PppoeCreditsMaxOutCon_Object=MibTableColumn
pppoeCreditsMaxOutCon=_PppoeCreditsMaxOutCon_Object((1,3,6,1,4,1,272,4,24,2,1,5),_PppoeCreditsMaxOutCon_Type())
pppoeCreditsMaxOutCon.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsMaxOutCon.setStatus(_A)
class _PppoeCreditsMaxInDuration_Type(Integer32):defaultValue=-1
_PppoeCreditsMaxInDuration_Type.__name__=_D
_PppoeCreditsMaxInDuration_Object=MibTableColumn
pppoeCreditsMaxInDuration=_PppoeCreditsMaxInDuration_Object((1,3,6,1,4,1,272,4,24,2,1,6),_PppoeCreditsMaxInDuration_Type())
pppoeCreditsMaxInDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsMaxInDuration.setStatus(_A)
class _PppoeCreditsMaxOutDuration_Type(Integer32):defaultValue=28800
_PppoeCreditsMaxOutDuration_Type.__name__=_D
_PppoeCreditsMaxOutDuration_Object=MibTableColumn
pppoeCreditsMaxOutDuration=_PppoeCreditsMaxOutDuration_Object((1,3,6,1,4,1,272,4,24,2,1,7),_PppoeCreditsMaxOutDuration_Type())
pppoeCreditsMaxOutDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsMaxOutDuration.setStatus(_A)
_PppoeCreditsTimeleft_Type=Integer32
_PppoeCreditsTimeleft_Object=MibTableColumn
pppoeCreditsTimeleft=_PppoeCreditsTimeleft_Object((1,3,6,1,4,1,272,4,24,2,1,8),_PppoeCreditsTimeleft_Type())
pppoeCreditsTimeleft.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeCreditsTimeleft.setStatus(_A)
_PppoeCreditsCurrentInCon_Type=Integer32
_PppoeCreditsCurrentInCon_Object=MibTableColumn
pppoeCreditsCurrentInCon=_PppoeCreditsCurrentInCon_Object((1,3,6,1,4,1,272,4,24,2,1,9),_PppoeCreditsCurrentInCon_Type())
pppoeCreditsCurrentInCon.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsCurrentInCon.setStatus(_A)
_PppoeCreditsCurrentOutCon_Type=Integer32
_PppoeCreditsCurrentOutCon_Object=MibTableColumn
pppoeCreditsCurrentOutCon=_PppoeCreditsCurrentOutCon_Object((1,3,6,1,4,1,272,4,24,2,1,10),_PppoeCreditsCurrentOutCon_Type())
pppoeCreditsCurrentOutCon.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsCurrentOutCon.setStatus(_A)
_PppoeCreditsTotalInCon_Type=Integer32
_PppoeCreditsTotalInCon_Object=MibTableColumn
pppoeCreditsTotalInCon=_PppoeCreditsTotalInCon_Object((1,3,6,1,4,1,272,4,24,2,1,11),_PppoeCreditsTotalInCon_Type())
pppoeCreditsTotalInCon.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsTotalInCon.setStatus(_A)
_PppoeCreditsTotalOutCon_Type=Integer32
_PppoeCreditsTotalOutCon_Object=MibTableColumn
pppoeCreditsTotalOutCon=_PppoeCreditsTotalOutCon_Object((1,3,6,1,4,1,272,4,24,2,1,12),_PppoeCreditsTotalOutCon_Type())
pppoeCreditsTotalOutCon.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsTotalOutCon.setStatus(_A)
_PppoeCreditsTotalInDuration_Type=Integer32
_PppoeCreditsTotalInDuration_Object=MibTableColumn
pppoeCreditsTotalInDuration=_PppoeCreditsTotalInDuration_Object((1,3,6,1,4,1,272,4,24,2,1,13),_PppoeCreditsTotalInDuration_Type())
pppoeCreditsTotalInDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsTotalInDuration.setStatus(_A)
_PppoeCreditsTotalOutDuration_Type=Integer32
_PppoeCreditsTotalOutDuration_Object=MibTableColumn
pppoeCreditsTotalOutDuration=_PppoeCreditsTotalOutDuration_Object((1,3,6,1,4,1,272,4,24,2,1,14),_PppoeCreditsTotalOutDuration_Type())
pppoeCreditsTotalOutDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsTotalOutDuration.setStatus(_A)
class _PppoeCreditsCurrentAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PppoeCreditsCurrentAccount_Type.__name__=_D
_PppoeCreditsCurrentAccount_Object=MibTableColumn
pppoeCreditsCurrentAccount=_PppoeCreditsCurrentAccount_Object((1,3,6,1,4,1,272,4,24,2,1,15),_PppoeCreditsCurrentAccount_Type())
pppoeCreditsCurrentAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeCreditsCurrentAccount.setStatus(_A)
_PppoePassThroughTable_Object=MibTable
pppoePassThroughTable=_PppoePassThroughTable_Object((1,3,6,1,4,1,272,4,24,5))
if mibBuilder.loadTexts:pppoePassThroughTable.setStatus(_A)
_PppoePassThroughEntry_Object=MibTableRow
pppoePassThroughEntry=_PppoePassThroughEntry_Object((1,3,6,1,4,1,272,4,24,5,1))
pppoePassThroughEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:pppoePassThroughEntry.setStatus(_A)
_PppoePassThroughEthIfIndex1_Type=Integer32
_PppoePassThroughEthIfIndex1_Object=MibTableColumn
pppoePassThroughEthIfIndex1=_PppoePassThroughEthIfIndex1_Object((1,3,6,1,4,1,272,4,24,5,1,1),_PppoePassThroughEthIfIndex1_Type())
pppoePassThroughEthIfIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoePassThroughEthIfIndex1.setStatus(_A)
_PppoePassThroughEthIfIndex2_Type=Integer32
_PppoePassThroughEthIfIndex2_Object=MibTableColumn
pppoePassThroughEthIfIndex2=_PppoePassThroughEthIfIndex2_Object((1,3,6,1,4,1,272,4,24,5,1,2),_PppoePassThroughEthIfIndex2_Type())
pppoePassThroughEthIfIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoePassThroughEthIfIndex2.setStatus(_A)
class _PppoePassThroughStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_F,3)))
_PppoePassThroughStatus_Type.__name__=_D
_PppoePassThroughStatus_Object=MibTableColumn
pppoePassThroughStatus=_PppoePassThroughStatus_Object((1,3,6,1,4,1,272,4,24,5,1,3),_PppoePassThroughStatus_Type())
pppoePassThroughStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoePassThroughStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'pppoe':pppoe,'pppoeCallTable':pppoeCallTable,'pppoeCallEntry':pppoeCallEntry,_G:pppoeCallId,'pppoeCallDirection':pppoeCallDirection,'pppoeCallAge':pppoeCallAge,'pppoeCallState':pppoeCallState,'pppoeCallRemotePhysAddress':pppoeCallRemotePhysAddress,'pppoeCallLocalPhysAddress':pppoeCallLocalPhysAddress,'pppoeCallAcName':pppoeCallAcName,'pppoeCallService':pppoeCallService,'pppoeCallReceivedPackets':pppoeCallReceivedPackets,'pppoeCallReceivedOctets':pppoeCallReceivedOctets,'pppoeCallReceivedErrors':pppoeCallReceivedErrors,'pppoeCallTransmitPackets':pppoeCallTransmitPackets,'pppoeCallTransmitOctets':pppoeCallTransmitOctets,'pppoeCallTransmitErrors':pppoeCallTransmitErrors,'pppoeCallInfo':pppoeCallInfo,'pppoeCallSessionId':pppoeCallSessionId,'pppoeCallEthIfIndex':pppoeCallEthIfIndex,'pppoeCallAssociatedIfIndex':pppoeCallAssociatedIfIndex,'pppoeCreditsTable':pppoeCreditsTable,'pppoeCreditsEntry':pppoeCreditsEntry,_H:pppoeCreditsService,'pppoeCreditsSurveillance':pppoeCreditsSurveillance,'pppoeCreditsMeasuretime':pppoeCreditsMeasuretime,'pppoeCreditsMaxInCon':pppoeCreditsMaxInCon,'pppoeCreditsMaxOutCon':pppoeCreditsMaxOutCon,'pppoeCreditsMaxInDuration':pppoeCreditsMaxInDuration,'pppoeCreditsMaxOutDuration':pppoeCreditsMaxOutDuration,'pppoeCreditsTimeleft':pppoeCreditsTimeleft,'pppoeCreditsCurrentInCon':pppoeCreditsCurrentInCon,'pppoeCreditsCurrentOutCon':pppoeCreditsCurrentOutCon,'pppoeCreditsTotalInCon':pppoeCreditsTotalInCon,'pppoeCreditsTotalOutCon':pppoeCreditsTotalOutCon,'pppoeCreditsTotalInDuration':pppoeCreditsTotalInDuration,'pppoeCreditsTotalOutDuration':pppoeCreditsTotalOutDuration,'pppoeCreditsCurrentAccount':pppoeCreditsCurrentAccount,'pppoePassThroughTable':pppoePassThroughTable,'pppoePassThroughEntry':pppoePassThroughEntry,_I:pppoePassThroughEthIfIndex1,_J:pppoePassThroughEthIfIndex2,'pppoePassThroughStatus':pppoePassThroughStatus})