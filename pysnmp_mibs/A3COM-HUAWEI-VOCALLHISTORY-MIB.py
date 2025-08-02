_I='h3cVoCallHisPSTNIndex'
_H='h3cVoCallHisVoIPIndex'
_G='h3cVoCallHisIndex'
_F='read-write'
_E='not-accessible'
_D='A3COM-HUAWEI-VOCALLHISTORY-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
CodecType,=mibBuilder.importSymbols('A3COM-HUAWEI-VO-TYPE-MIB','CodecType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp')
h3cVoiceCallHistory=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,7))
if mibBuilder.loadTexts:h3cVoiceCallHistory.setRevisions(('2005-03-15 00:00',))
_H3cVoCallHistoryObjects_ObjectIdentity=ObjectIdentity
h3cVoCallHistoryObjects=_H3cVoCallHistoryObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,7,1))
_H3cVoCallHistoryMaxLen_Type=Integer32
_H3cVoCallHistoryMaxLen_Object=MibScalar
h3cVoCallHistoryMaxLen=_H3cVoCallHistoryMaxLen_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,1,1),_H3cVoCallHistoryMaxLen_Type())
h3cVoCallHistoryMaxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoCallHistoryMaxLen.setStatus(_A)
class _H3cVoCallHistoryMaxRetainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cVoCallHistoryMaxRetainTime_Type.__name__=_C
_H3cVoCallHistoryMaxRetainTime_Object=MibScalar
h3cVoCallHistoryMaxRetainTime=_H3cVoCallHistoryMaxRetainTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,1,2),_H3cVoCallHistoryMaxRetainTime_Type())
h3cVoCallHistoryMaxRetainTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoCallHistoryMaxRetainTime.setStatus(_A)
_H3cVoCallHistoryGenericTable_Object=MibTable
h3cVoCallHistoryGenericTable=_H3cVoCallHistoryGenericTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2))
if mibBuilder.loadTexts:h3cVoCallHistoryGenericTable.setStatus(_A)
_H3cVoCallHistoryGenericEntry_Object=MibTableRow
h3cVoCallHistoryGenericEntry=_H3cVoCallHistoryGenericEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1))
h3cVoCallHistoryGenericEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:h3cVoCallHistoryGenericEntry.setStatus(_A)
class _H3cVoCallHisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoCallHisIndex_Type.__name__=_C
_H3cVoCallHisIndex_Object=MibTableColumn
h3cVoCallHisIndex=_H3cVoCallHisIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,1),_H3cVoCallHisIndex_Type())
h3cVoCallHisIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoCallHisIndex.setStatus(_A)
_H3cVoCallHisCallerNumber_Type=OctetString
_H3cVoCallHisCallerNumber_Object=MibTableColumn
h3cVoCallHisCallerNumber=_H3cVoCallHisCallerNumber_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,2),_H3cVoCallHisCallerNumber_Type())
h3cVoCallHisCallerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisCallerNumber.setStatus(_A)
_H3cVoCallHisCalledNumber_Type=OctetString
_H3cVoCallHisCalledNumber_Object=MibTableColumn
h3cVoCallHisCalledNumber=_H3cVoCallHisCalledNumber_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,3),_H3cVoCallHisCalledNumber_Type())
h3cVoCallHisCalledNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisCalledNumber.setStatus(_A)
_H3cVoCallHisEncodeType_Type=CodecType
_H3cVoCallHisEncodeType_Object=MibTableColumn
h3cVoCallHisEncodeType=_H3cVoCallHisEncodeType_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,4),_H3cVoCallHisEncodeType_Type())
h3cVoCallHisEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisEncodeType.setStatus(_A)
_H3cVoCallHisChannel_Type=Integer32
_H3cVoCallHisChannel_Object=MibTableColumn
h3cVoCallHisChannel=_H3cVoCallHisChannel_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,5),_H3cVoCallHisChannel_Type())
h3cVoCallHisChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisChannel.setStatus(_A)
_H3cVoCallHisLocalAddressType_Type=InetAddressType
_H3cVoCallHisLocalAddressType_Object=MibTableColumn
h3cVoCallHisLocalAddressType=_H3cVoCallHisLocalAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,6),_H3cVoCallHisLocalAddressType_Type())
h3cVoCallHisLocalAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisLocalAddressType.setStatus(_A)
_H3cVoCallHisLocalAddress_Type=InetAddress
_H3cVoCallHisLocalAddress_Object=MibTableColumn
h3cVoCallHisLocalAddress=_H3cVoCallHisLocalAddress_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,7),_H3cVoCallHisLocalAddress_Type())
h3cVoCallHisLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisLocalAddress.setStatus(_A)
_H3cVoCallHisPeerAddressType_Type=InetAddressType
_H3cVoCallHisPeerAddressType_Object=MibTableColumn
h3cVoCallHisPeerAddressType=_H3cVoCallHisPeerAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,8),_H3cVoCallHisPeerAddressType_Type())
h3cVoCallHisPeerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPeerAddressType.setStatus(_A)
_H3cVoCallHisPeerAddress_Type=InetAddress
_H3cVoCallHisPeerAddress_Object=MibTableColumn
h3cVoCallHisPeerAddress=_H3cVoCallHisPeerAddress_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,9),_H3cVoCallHisPeerAddress_Type())
h3cVoCallHisPeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPeerAddress.setStatus(_A)
class _H3cVoCallHisDisconnectText_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('normalRelease',1),('cardNumberNotExist',2),('invalidPassword',3),('thisAccountsIsUsing',4),('noEnoughBalance',5),('theAccountsIsExpired',6),('creditLimit',7),('userReject',8),('serviceInvalid',9),('calledLimit',10),('maxRedialTimesLimit',11),('invalidParameter',12),('callerHookOn',13),('calledHookOn',14),('networkProblem',15),('unknownReason',16)))
_H3cVoCallHisDisconnectText_Type.__name__=_C
_H3cVoCallHisDisconnectText_Object=MibTableColumn
h3cVoCallHisDisconnectText=_H3cVoCallHisDisconnectText_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,10),_H3cVoCallHisDisconnectText_Type())
h3cVoCallHisDisconnectText.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisDisconnectText.setStatus(_A)
_H3cVoCallHisCallDuration_Type=TimeTicks
_H3cVoCallHisCallDuration_Object=MibTableColumn
h3cVoCallHisCallDuration=_H3cVoCallHisCallDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,11),_H3cVoCallHisCallDuration_Type())
h3cVoCallHisCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisCallDuration.setStatus(_A)
_H3cVoCallHisVoCallDuration_Type=TimeTicks
_H3cVoCallHisVoCallDuration_Object=MibTableColumn
h3cVoCallHisVoCallDuration=_H3cVoCallHisVoCallDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,12),_H3cVoCallHisVoCallDuration_Type())
h3cVoCallHisVoCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoCallDuration.setStatus(_A)
_H3cVoCallHisFaxCallDuration_Type=TimeTicks
_H3cVoCallHisFaxCallDuration_Object=MibTableColumn
h3cVoCallHisFaxCallDuration=_H3cVoCallHisFaxCallDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,13),_H3cVoCallHisFaxCallDuration_Type())
h3cVoCallHisFaxCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisFaxCallDuration.setStatus(_A)
_H3cVoCallHisImgPages_Type=Integer32
_H3cVoCallHisImgPages_Object=MibTableColumn
h3cVoCallHisImgPages=_H3cVoCallHisImgPages_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,14),_H3cVoCallHisImgPages_Type())
h3cVoCallHisImgPages.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisImgPages.setStatus(_A)
class _H3cVoCallHisCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('caller',1),('called',2)))
_H3cVoCallHisCallOrigin_Type.__name__=_C
_H3cVoCallHisCallOrigin_Object=MibTableColumn
h3cVoCallHisCallOrigin=_H3cVoCallHisCallOrigin_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,2,1,15),_H3cVoCallHisCallOrigin_Type())
h3cVoCallHisCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisCallOrigin.setStatus(_A)
_H3cVoCallHistoryVoIPTable_Object=MibTable
h3cVoCallHistoryVoIPTable=_H3cVoCallHistoryVoIPTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3))
if mibBuilder.loadTexts:h3cVoCallHistoryVoIPTable.setStatus(_A)
_H3cVoCallHistoryVoIPEntry_Object=MibTableRow
h3cVoCallHistoryVoIPEntry=_H3cVoCallHistoryVoIPEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1))
h3cVoCallHistoryVoIPEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cVoCallHistoryVoIPEntry.setStatus(_A)
class _H3cVoCallHisVoIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoCallHisVoIPIndex_Type.__name__=_C
_H3cVoCallHisVoIPIndex_Object=MibTableColumn
h3cVoCallHisVoIPIndex=_H3cVoCallHisVoIPIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,1),_H3cVoCallHisVoIPIndex_Type())
h3cVoCallHisVoIPIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoCallHisVoIPIndex.setStatus(_A)
_H3cVoCallHisVoIPSetupTime_Type=DateAndTime
_H3cVoCallHisVoIPSetupTime_Object=MibTableColumn
h3cVoCallHisVoIPSetupTime=_H3cVoCallHisVoIPSetupTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,2),_H3cVoCallHisVoIPSetupTime_Type())
h3cVoCallHisVoIPSetupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPSetupTime.setStatus(_A)
_H3cVoCallHisVoIPConnTime_Type=DateAndTime
_H3cVoCallHisVoIPConnTime_Object=MibTableColumn
h3cVoCallHisVoIPConnTime=_H3cVoCallHisVoIPConnTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,3),_H3cVoCallHisVoIPConnTime_Type())
h3cVoCallHisVoIPConnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPConnTime.setStatus(_A)
_H3cVoCallHisVoIPDiscTime_Type=DateAndTime
_H3cVoCallHisVoIPDiscTime_Object=MibTableColumn
h3cVoCallHisVoIPDiscTime=_H3cVoCallHisVoIPDiscTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,4),_H3cVoCallHisVoIPDiscTime_Type())
h3cVoCallHisVoIPDiscTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPDiscTime.setStatus(_A)
_H3cVoCallHisVoIPTxPackets_Type=Counter32
_H3cVoCallHisVoIPTxPackets_Object=MibTableColumn
h3cVoCallHisVoIPTxPackets=_H3cVoCallHisVoIPTxPackets_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,5),_H3cVoCallHisVoIPTxPackets_Type())
h3cVoCallHisVoIPTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPTxPackets.setStatus(_A)
_H3cVoCallHisVoIPTxBytes_Type=Counter32
_H3cVoCallHisVoIPTxBytes_Object=MibTableColumn
h3cVoCallHisVoIPTxBytes=_H3cVoCallHisVoIPTxBytes_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,6),_H3cVoCallHisVoIPTxBytes_Type())
h3cVoCallHisVoIPTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPTxBytes.setStatus(_A)
_H3cVoCallHisVoIPRxPackets_Type=Counter32
_H3cVoCallHisVoIPRxPackets_Object=MibTableColumn
h3cVoCallHisVoIPRxPackets=_H3cVoCallHisVoIPRxPackets_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,7),_H3cVoCallHisVoIPRxPackets_Type())
h3cVoCallHisVoIPRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPRxPackets.setStatus(_A)
_H3cVoCallHisVoIPRxeBytes_Type=Counter32
_H3cVoCallHisVoIPRxeBytes_Object=MibTableColumn
h3cVoCallHisVoIPRxeBytes=_H3cVoCallHisVoIPRxeBytes_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,3,1,8),_H3cVoCallHisVoIPRxeBytes_Type())
h3cVoCallHisVoIPRxeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisVoIPRxeBytes.setStatus(_A)
_H3cVoCallHistoryPSTNTable_Object=MibTable
h3cVoCallHistoryPSTNTable=_H3cVoCallHistoryPSTNTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4))
if mibBuilder.loadTexts:h3cVoCallHistoryPSTNTable.setStatus(_A)
_H3cVoCallHistoryPSTNEntry_Object=MibTableRow
h3cVoCallHistoryPSTNEntry=_H3cVoCallHistoryPSTNEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1))
h3cVoCallHistoryPSTNEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cVoCallHistoryPSTNEntry.setStatus(_A)
class _H3cVoCallHisPSTNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoCallHisPSTNIndex_Type.__name__=_C
_H3cVoCallHisPSTNIndex_Object=MibTableColumn
h3cVoCallHisPSTNIndex=_H3cVoCallHisPSTNIndex_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,1),_H3cVoCallHisPSTNIndex_Type())
h3cVoCallHisPSTNIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cVoCallHisPSTNIndex.setStatus(_A)
_H3cVoCallHisPSTNSetupTime_Type=DateAndTime
_H3cVoCallHisPSTNSetupTime_Object=MibTableColumn
h3cVoCallHisPSTNSetupTime=_H3cVoCallHisPSTNSetupTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,2),_H3cVoCallHisPSTNSetupTime_Type())
h3cVoCallHisPSTNSetupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNSetupTime.setStatus(_A)
_H3cVoCallHisPSTNConnTime_Type=DateAndTime
_H3cVoCallHisPSTNConnTime_Object=MibTableColumn
h3cVoCallHisPSTNConnTime=_H3cVoCallHisPSTNConnTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,3),_H3cVoCallHisPSTNConnTime_Type())
h3cVoCallHisPSTNConnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNConnTime.setStatus(_A)
_H3cVoCallHisPSTNDiscTime_Type=DateAndTime
_H3cVoCallHisPSTNDiscTime_Object=MibTableColumn
h3cVoCallHisPSTNDiscTime=_H3cVoCallHisPSTNDiscTime_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,4),_H3cVoCallHisPSTNDiscTime_Type())
h3cVoCallHisPSTNDiscTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNDiscTime.setStatus(_A)
_H3cVoCallHisPSTNTxPackets_Type=Counter32
_H3cVoCallHisPSTNTxPackets_Object=MibTableColumn
h3cVoCallHisPSTNTxPackets=_H3cVoCallHisPSTNTxPackets_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,5),_H3cVoCallHisPSTNTxPackets_Type())
h3cVoCallHisPSTNTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNTxPackets.setStatus(_A)
_H3cVoCallHisPSTNTxBytes_Type=Counter32
_H3cVoCallHisPSTNTxBytes_Object=MibTableColumn
h3cVoCallHisPSTNTxBytes=_H3cVoCallHisPSTNTxBytes_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,6),_H3cVoCallHisPSTNTxBytes_Type())
h3cVoCallHisPSTNTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNTxBytes.setStatus(_A)
_H3cVoCallHisPSTNRxPackets_Type=Counter32
_H3cVoCallHisPSTNRxPackets_Object=MibTableColumn
h3cVoCallHisPSTNRxPackets=_H3cVoCallHisPSTNRxPackets_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,7),_H3cVoCallHisPSTNRxPackets_Type())
h3cVoCallHisPSTNRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNRxPackets.setStatus(_A)
_H3cVoCallHisPSTNRxBytes_Type=Counter32
_H3cVoCallHisPSTNRxBytes_Object=MibTableColumn
h3cVoCallHisPSTNRxBytes=_H3cVoCallHisPSTNRxBytes_Object((1,3,6,1,4,1,43,45,1,10,2,39,7,4,1,8),_H3cVoCallHisPSTNRxBytes_Type())
h3cVoCallHisPSTNRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallHisPSTNRxBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cVoiceCallHistory':h3cVoiceCallHistory,'h3cVoCallHistoryObjects':h3cVoCallHistoryObjects,'h3cVoCallHistoryMaxLen':h3cVoCallHistoryMaxLen,'h3cVoCallHistoryMaxRetainTime':h3cVoCallHistoryMaxRetainTime,'h3cVoCallHistoryGenericTable':h3cVoCallHistoryGenericTable,'h3cVoCallHistoryGenericEntry':h3cVoCallHistoryGenericEntry,_G:h3cVoCallHisIndex,'h3cVoCallHisCallerNumber':h3cVoCallHisCallerNumber,'h3cVoCallHisCalledNumber':h3cVoCallHisCalledNumber,'h3cVoCallHisEncodeType':h3cVoCallHisEncodeType,'h3cVoCallHisChannel':h3cVoCallHisChannel,'h3cVoCallHisLocalAddressType':h3cVoCallHisLocalAddressType,'h3cVoCallHisLocalAddress':h3cVoCallHisLocalAddress,'h3cVoCallHisPeerAddressType':h3cVoCallHisPeerAddressType,'h3cVoCallHisPeerAddress':h3cVoCallHisPeerAddress,'h3cVoCallHisDisconnectText':h3cVoCallHisDisconnectText,'h3cVoCallHisCallDuration':h3cVoCallHisCallDuration,'h3cVoCallHisVoCallDuration':h3cVoCallHisVoCallDuration,'h3cVoCallHisFaxCallDuration':h3cVoCallHisFaxCallDuration,'h3cVoCallHisImgPages':h3cVoCallHisImgPages,'h3cVoCallHisCallOrigin':h3cVoCallHisCallOrigin,'h3cVoCallHistoryVoIPTable':h3cVoCallHistoryVoIPTable,'h3cVoCallHistoryVoIPEntry':h3cVoCallHistoryVoIPEntry,_H:h3cVoCallHisVoIPIndex,'h3cVoCallHisVoIPSetupTime':h3cVoCallHisVoIPSetupTime,'h3cVoCallHisVoIPConnTime':h3cVoCallHisVoIPConnTime,'h3cVoCallHisVoIPDiscTime':h3cVoCallHisVoIPDiscTime,'h3cVoCallHisVoIPTxPackets':h3cVoCallHisVoIPTxPackets,'h3cVoCallHisVoIPTxBytes':h3cVoCallHisVoIPTxBytes,'h3cVoCallHisVoIPRxPackets':h3cVoCallHisVoIPRxPackets,'h3cVoCallHisVoIPRxeBytes':h3cVoCallHisVoIPRxeBytes,'h3cVoCallHistoryPSTNTable':h3cVoCallHistoryPSTNTable,'h3cVoCallHistoryPSTNEntry':h3cVoCallHistoryPSTNEntry,_I:h3cVoCallHisPSTNIndex,'h3cVoCallHisPSTNSetupTime':h3cVoCallHisPSTNSetupTime,'h3cVoCallHisPSTNConnTime':h3cVoCallHisPSTNConnTime,'h3cVoCallHisPSTNDiscTime':h3cVoCallHisPSTNDiscTime,'h3cVoCallHisPSTNTxPackets':h3cVoCallHisPSTNTxPackets,'h3cVoCallHisPSTNTxBytes':h3cVoCallHisPSTNTxBytes,'h3cVoCallHisPSTNRxPackets':h3cVoCallHisPSTNRxPackets,'h3cVoCallHisPSTNRxBytes':h3cVoCallHisPSTNRxBytes})