_I='hwVoCallHistoryPSTNIndex'
_H='hwVoCallHistoryVoIPIndex'
_G='hwVoCallHistoryGenericIndex'
_F='read-write'
_E='OctetString'
_D='HUAWEI-VO-CALL-HISTORY-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp')
hwVoiceCallHistoryMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,7))
if mibBuilder.loadTexts:hwVoiceCallHistoryMIB.setRevisions(('2004-04-08 13:45',))
_HwVoCallHistoryObjects_ObjectIdentity=ObjectIdentity
hwVoCallHistoryObjects=_HwVoCallHistoryObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,7,1))
class _HwVoCallHistoryMaxLen_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_HwVoCallHistoryMaxLen_Type.__name__=_C
_HwVoCallHistoryMaxLen_Object=MibScalar
hwVoCallHistoryMaxLen=_HwVoCallHistoryMaxLen_Object((1,3,6,1,4,1,2011,5,25,1,7,1,1),_HwVoCallHistoryMaxLen_Type())
hwVoCallHistoryMaxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:hwVoCallHistoryMaxLen.setStatus(_A)
_HwVoCallHistoryGenericTable_Object=MibTable
hwVoCallHistoryGenericTable=_HwVoCallHistoryGenericTable_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2))
if mibBuilder.loadTexts:hwVoCallHistoryGenericTable.setStatus(_A)
_HwVoCallHistoryGenericEntry_Object=MibTableRow
hwVoCallHistoryGenericEntry=_HwVoCallHistoryGenericEntry_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1))
hwVoCallHistoryGenericEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hwVoCallHistoryGenericEntry.setStatus(_A)
class _HwVoCallHistoryGenericIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoCallHistoryGenericIndex_Type.__name__=_C
_HwVoCallHistoryGenericIndex_Object=MibTableColumn
hwVoCallHistoryGenericIndex=_HwVoCallHistoryGenericIndex_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,1),_HwVoCallHistoryGenericIndex_Type())
hwVoCallHistoryGenericIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericIndex.setStatus(_A)
class _HwVoCallHistoryGenericCallerNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoCallHistoryGenericCallerNumber_Type.__name__=_E
_HwVoCallHistoryGenericCallerNumber_Object=MibTableColumn
hwVoCallHistoryGenericCallerNumber=_HwVoCallHistoryGenericCallerNumber_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,2),_HwVoCallHistoryGenericCallerNumber_Type())
hwVoCallHistoryGenericCallerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericCallerNumber.setStatus(_A)
class _HwVoCallHistoryGenericCalledNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoCallHistoryGenericCalledNumber_Type.__name__=_E
_HwVoCallHistoryGenericCalledNumber_Object=MibTableColumn
hwVoCallHistoryGenericCalledNumber=_HwVoCallHistoryGenericCalledNumber_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,3),_HwVoCallHistoryGenericCalledNumber_Type())
hwVoCallHistoryGenericCalledNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericCalledNumber.setStatus(_A)
class _HwVoCallHistoryGenericEncodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknown',0),('g711a',1),('g711u',2),('g723',3),('g729',4),('g729a',5)))
_HwVoCallHistoryGenericEncodeType_Type.__name__=_C
_HwVoCallHistoryGenericEncodeType_Object=MibTableColumn
hwVoCallHistoryGenericEncodeType=_HwVoCallHistoryGenericEncodeType_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,4),_HwVoCallHistoryGenericEncodeType_Type())
hwVoCallHistoryGenericEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericEncodeType.setStatus(_A)
_HwVoCallHistoryGenericChannel_Type=Integer32
_HwVoCallHistoryGenericChannel_Object=MibTableColumn
hwVoCallHistoryGenericChannel=_HwVoCallHistoryGenericChannel_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,5),_HwVoCallHistoryGenericChannel_Type())
hwVoCallHistoryGenericChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericChannel.setStatus(_A)
_HwVoCallHistoryGenericLocalAddress_Type=IpAddress
_HwVoCallHistoryGenericLocalAddress_Object=MibTableColumn
hwVoCallHistoryGenericLocalAddress=_HwVoCallHistoryGenericLocalAddress_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,6),_HwVoCallHistoryGenericLocalAddress_Type())
hwVoCallHistoryGenericLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericLocalAddress.setStatus(_A)
_HwVoCallHistoryGenericPeerAddress_Type=IpAddress
_HwVoCallHistoryGenericPeerAddress_Object=MibTableColumn
hwVoCallHistoryGenericPeerAddress=_HwVoCallHistoryGenericPeerAddress_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,7),_HwVoCallHistoryGenericPeerAddress_Type())
hwVoCallHistoryGenericPeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericPeerAddress.setStatus(_A)
class _HwVoCallHistoryGenericDisconnectText_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('normalRelease',1),('cardNumberNotExist',2),('invalidPassword',3),('thisAccountsIsUsing',4),('noEnoughBalance',5),('theAccountsIsExpired',6),('creditLimit',7),('userReject',8),('serviceInvalid',9),('calledLimit',10),('maxRedialTimesLimit',11),('invalidParameter',12),('callerHookOn',13),('calledHookOn',14),('networkProblem',15),('unknownReason',16)))
_HwVoCallHistoryGenericDisconnectText_Type.__name__=_C
_HwVoCallHistoryGenericDisconnectText_Object=MibTableColumn
hwVoCallHistoryGenericDisconnectText=_HwVoCallHistoryGenericDisconnectText_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,8),_HwVoCallHistoryGenericDisconnectText_Type())
hwVoCallHistoryGenericDisconnectText.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericDisconnectText.setStatus(_A)
_HwVoCallHistoryGenericCallDuration_Type=TimeTicks
_HwVoCallHistoryGenericCallDuration_Object=MibTableColumn
hwVoCallHistoryGenericCallDuration=_HwVoCallHistoryGenericCallDuration_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,9),_HwVoCallHistoryGenericCallDuration_Type())
hwVoCallHistoryGenericCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericCallDuration.setStatus(_A)
_HwVoCallHistoryGenericVoiceCallDuration_Type=TimeTicks
_HwVoCallHistoryGenericVoiceCallDuration_Object=MibTableColumn
hwVoCallHistoryGenericVoiceCallDuration=_HwVoCallHistoryGenericVoiceCallDuration_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,10),_HwVoCallHistoryGenericVoiceCallDuration_Type())
hwVoCallHistoryGenericVoiceCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericVoiceCallDuration.setStatus(_A)
_HwVoCallHistoryGenericFaxCallDuration_Type=TimeTicks
_HwVoCallHistoryGenericFaxCallDuration_Object=MibTableColumn
hwVoCallHistoryGenericFaxCallDuration=_HwVoCallHistoryGenericFaxCallDuration_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,11),_HwVoCallHistoryGenericFaxCallDuration_Type())
hwVoCallHistoryGenericFaxCallDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericFaxCallDuration.setStatus(_A)
_HwVoCallHistoryGenericImgPages_Type=Integer32
_HwVoCallHistoryGenericImgPages_Object=MibTableColumn
hwVoCallHistoryGenericImgPages=_HwVoCallHistoryGenericImgPages_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,12),_HwVoCallHistoryGenericImgPages_Type())
hwVoCallHistoryGenericImgPages.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericImgPages.setStatus(_A)
class _HwVoCallHistoryGenericCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('caller',1),('called',2)))
_HwVoCallHistoryGenericCallOrigin_Type.__name__=_C
_HwVoCallHistoryGenericCallOrigin_Object=MibTableColumn
hwVoCallHistoryGenericCallOrigin=_HwVoCallHistoryGenericCallOrigin_Object((1,3,6,1,4,1,2011,5,25,1,7,1,2,1,13),_HwVoCallHistoryGenericCallOrigin_Type())
hwVoCallHistoryGenericCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryGenericCallOrigin.setStatus(_A)
_HwVoCallHistoryVoIPTable_Object=MibTable
hwVoCallHistoryVoIPTable=_HwVoCallHistoryVoIPTable_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3))
if mibBuilder.loadTexts:hwVoCallHistoryVoIPTable.setStatus(_A)
_HwVoCallHistoryVoIPEntry_Object=MibTableRow
hwVoCallHistoryVoIPEntry=_HwVoCallHistoryVoIPEntry_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1))
hwVoCallHistoryVoIPEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hwVoCallHistoryVoIPEntry.setStatus(_A)
class _HwVoCallHistoryVoIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoCallHistoryVoIPIndex_Type.__name__=_C
_HwVoCallHistoryVoIPIndex_Object=MibTableColumn
hwVoCallHistoryVoIPIndex=_HwVoCallHistoryVoIPIndex_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,1),_HwVoCallHistoryVoIPIndex_Type())
hwVoCallHistoryVoIPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPIndex.setStatus(_A)
_HwVoCallHistoryVoIPSetupTime_Type=DateAndTime
_HwVoCallHistoryVoIPSetupTime_Object=MibTableColumn
hwVoCallHistoryVoIPSetupTime=_HwVoCallHistoryVoIPSetupTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,2),_HwVoCallHistoryVoIPSetupTime_Type())
hwVoCallHistoryVoIPSetupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPSetupTime.setStatus(_A)
_HwVoCallHistoryVoIPConnectTime_Type=DateAndTime
_HwVoCallHistoryVoIPConnectTime_Object=MibTableColumn
hwVoCallHistoryVoIPConnectTime=_HwVoCallHistoryVoIPConnectTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,3),_HwVoCallHistoryVoIPConnectTime_Type())
hwVoCallHistoryVoIPConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPConnectTime.setStatus(_A)
_HwVoCallHistoryVoIPDisconectTime_Type=DateAndTime
_HwVoCallHistoryVoIPDisconectTime_Object=MibTableColumn
hwVoCallHistoryVoIPDisconectTime=_HwVoCallHistoryVoIPDisconectTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,4),_HwVoCallHistoryVoIPDisconectTime_Type())
hwVoCallHistoryVoIPDisconectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPDisconectTime.setStatus(_A)
_HwVoCallHistoryVoIPSendPackets_Type=Integer32
_HwVoCallHistoryVoIPSendPackets_Object=MibTableColumn
hwVoCallHistoryVoIPSendPackets=_HwVoCallHistoryVoIPSendPackets_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,5),_HwVoCallHistoryVoIPSendPackets_Type())
hwVoCallHistoryVoIPSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPSendPackets.setStatus(_A)
_HwVoCallHistoryVoIPSendBytes_Type=Integer32
_HwVoCallHistoryVoIPSendBytes_Object=MibTableColumn
hwVoCallHistoryVoIPSendBytes=_HwVoCallHistoryVoIPSendBytes_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,6),_HwVoCallHistoryVoIPSendBytes_Type())
hwVoCallHistoryVoIPSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPSendBytes.setStatus(_A)
_HwVoCallHistoryVoIPReceivePackets_Type=Integer32
_HwVoCallHistoryVoIPReceivePackets_Object=MibTableColumn
hwVoCallHistoryVoIPReceivePackets=_HwVoCallHistoryVoIPReceivePackets_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,7),_HwVoCallHistoryVoIPReceivePackets_Type())
hwVoCallHistoryVoIPReceivePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPReceivePackets.setStatus(_A)
_HwVoCallHistoryVoIPReceiveBytes_Type=Integer32
_HwVoCallHistoryVoIPReceiveBytes_Object=MibTableColumn
hwVoCallHistoryVoIPReceiveBytes=_HwVoCallHistoryVoIPReceiveBytes_Object((1,3,6,1,4,1,2011,5,25,1,7,1,3,1,8),_HwVoCallHistoryVoIPReceiveBytes_Type())
hwVoCallHistoryVoIPReceiveBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryVoIPReceiveBytes.setStatus(_A)
_HwVoCallHistoryPSTNTable_Object=MibTable
hwVoCallHistoryPSTNTable=_HwVoCallHistoryPSTNTable_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4))
if mibBuilder.loadTexts:hwVoCallHistoryPSTNTable.setStatus(_A)
_HwVoCallHistoryPSTNEntry_Object=MibTableRow
hwVoCallHistoryPSTNEntry=_HwVoCallHistoryPSTNEntry_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1))
hwVoCallHistoryPSTNEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hwVoCallHistoryPSTNEntry.setStatus(_A)
class _HwVoCallHistoryPSTNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoCallHistoryPSTNIndex_Type.__name__=_C
_HwVoCallHistoryPSTNIndex_Object=MibTableColumn
hwVoCallHistoryPSTNIndex=_HwVoCallHistoryPSTNIndex_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,1),_HwVoCallHistoryPSTNIndex_Type())
hwVoCallHistoryPSTNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNIndex.setStatus(_A)
_HwVoCallHistoryPSTNSetupTime_Type=DateAndTime
_HwVoCallHistoryPSTNSetupTime_Object=MibTableColumn
hwVoCallHistoryPSTNSetupTime=_HwVoCallHistoryPSTNSetupTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,2),_HwVoCallHistoryPSTNSetupTime_Type())
hwVoCallHistoryPSTNSetupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNSetupTime.setStatus(_A)
_HwVoCallHistoryPSTNConnectTime_Type=DateAndTime
_HwVoCallHistoryPSTNConnectTime_Object=MibTableColumn
hwVoCallHistoryPSTNConnectTime=_HwVoCallHistoryPSTNConnectTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,3),_HwVoCallHistoryPSTNConnectTime_Type())
hwVoCallHistoryPSTNConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNConnectTime.setStatus(_A)
_HwVoCallHistoryPSTNDisconectTime_Type=DateAndTime
_HwVoCallHistoryPSTNDisconectTime_Object=MibTableColumn
hwVoCallHistoryPSTNDisconectTime=_HwVoCallHistoryPSTNDisconectTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,4),_HwVoCallHistoryPSTNDisconectTime_Type())
hwVoCallHistoryPSTNDisconectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNDisconectTime.setStatus(_A)
_HwVoCallHistoryPSTNSendPackets_Type=Integer32
_HwVoCallHistoryPSTNSendPackets_Object=MibTableColumn
hwVoCallHistoryPSTNSendPackets=_HwVoCallHistoryPSTNSendPackets_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,5),_HwVoCallHistoryPSTNSendPackets_Type())
hwVoCallHistoryPSTNSendPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNSendPackets.setStatus(_A)
_HwVoCallHistoryPSTNSendBytes_Type=Integer32
_HwVoCallHistoryPSTNSendBytes_Object=MibTableColumn
hwVoCallHistoryPSTNSendBytes=_HwVoCallHistoryPSTNSendBytes_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,6),_HwVoCallHistoryPSTNSendBytes_Type())
hwVoCallHistoryPSTNSendBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNSendBytes.setStatus(_A)
_HwVoCallHistoryPSTNReceivePackets_Type=Integer32
_HwVoCallHistoryPSTNReceivePackets_Object=MibTableColumn
hwVoCallHistoryPSTNReceivePackets=_HwVoCallHistoryPSTNReceivePackets_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,7),_HwVoCallHistoryPSTNReceivePackets_Type())
hwVoCallHistoryPSTNReceivePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNReceivePackets.setStatus(_A)
_HwVoCallHistoryPSTNReceiveBytes_Type=Integer32
_HwVoCallHistoryPSTNReceiveBytes_Object=MibTableColumn
hwVoCallHistoryPSTNReceiveBytes=_HwVoCallHistoryPSTNReceiveBytes_Object((1,3,6,1,4,1,2011,5,25,1,7,1,4,1,8),_HwVoCallHistoryPSTNReceiveBytes_Type())
hwVoCallHistoryPSTNReceiveBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallHistoryPSTNReceiveBytes.setStatus(_A)
class _HwVoCallHistoryMaxRetainTime_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoCallHistoryMaxRetainTime_Type.__name__=_C
_HwVoCallHistoryMaxRetainTime_Object=MibScalar
hwVoCallHistoryMaxRetainTime=_HwVoCallHistoryMaxRetainTime_Object((1,3,6,1,4,1,2011,5,25,1,7,1,5),_HwVoCallHistoryMaxRetainTime_Type())
hwVoCallHistoryMaxRetainTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwVoCallHistoryMaxRetainTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hwVoiceCallHistoryMIB':hwVoiceCallHistoryMIB,'hwVoCallHistoryObjects':hwVoCallHistoryObjects,'hwVoCallHistoryMaxLen':hwVoCallHistoryMaxLen,'hwVoCallHistoryGenericTable':hwVoCallHistoryGenericTable,'hwVoCallHistoryGenericEntry':hwVoCallHistoryGenericEntry,_G:hwVoCallHistoryGenericIndex,'hwVoCallHistoryGenericCallerNumber':hwVoCallHistoryGenericCallerNumber,'hwVoCallHistoryGenericCalledNumber':hwVoCallHistoryGenericCalledNumber,'hwVoCallHistoryGenericEncodeType':hwVoCallHistoryGenericEncodeType,'hwVoCallHistoryGenericChannel':hwVoCallHistoryGenericChannel,'hwVoCallHistoryGenericLocalAddress':hwVoCallHistoryGenericLocalAddress,'hwVoCallHistoryGenericPeerAddress':hwVoCallHistoryGenericPeerAddress,'hwVoCallHistoryGenericDisconnectText':hwVoCallHistoryGenericDisconnectText,'hwVoCallHistoryGenericCallDuration':hwVoCallHistoryGenericCallDuration,'hwVoCallHistoryGenericVoiceCallDuration':hwVoCallHistoryGenericVoiceCallDuration,'hwVoCallHistoryGenericFaxCallDuration':hwVoCallHistoryGenericFaxCallDuration,'hwVoCallHistoryGenericImgPages':hwVoCallHistoryGenericImgPages,'hwVoCallHistoryGenericCallOrigin':hwVoCallHistoryGenericCallOrigin,'hwVoCallHistoryVoIPTable':hwVoCallHistoryVoIPTable,'hwVoCallHistoryVoIPEntry':hwVoCallHistoryVoIPEntry,_H:hwVoCallHistoryVoIPIndex,'hwVoCallHistoryVoIPSetupTime':hwVoCallHistoryVoIPSetupTime,'hwVoCallHistoryVoIPConnectTime':hwVoCallHistoryVoIPConnectTime,'hwVoCallHistoryVoIPDisconectTime':hwVoCallHistoryVoIPDisconectTime,'hwVoCallHistoryVoIPSendPackets':hwVoCallHistoryVoIPSendPackets,'hwVoCallHistoryVoIPSendBytes':hwVoCallHistoryVoIPSendBytes,'hwVoCallHistoryVoIPReceivePackets':hwVoCallHistoryVoIPReceivePackets,'hwVoCallHistoryVoIPReceiveBytes':hwVoCallHistoryVoIPReceiveBytes,'hwVoCallHistoryPSTNTable':hwVoCallHistoryPSTNTable,'hwVoCallHistoryPSTNEntry':hwVoCallHistoryPSTNEntry,_I:hwVoCallHistoryPSTNIndex,'hwVoCallHistoryPSTNSetupTime':hwVoCallHistoryPSTNSetupTime,'hwVoCallHistoryPSTNConnectTime':hwVoCallHistoryPSTNConnectTime,'hwVoCallHistoryPSTNDisconectTime':hwVoCallHistoryPSTNDisconectTime,'hwVoCallHistoryPSTNSendPackets':hwVoCallHistoryPSTNSendPackets,'hwVoCallHistoryPSTNSendBytes':hwVoCallHistoryPSTNSendBytes,'hwVoCallHistoryPSTNReceivePackets':hwVoCallHistoryPSTNReceivePackets,'hwVoCallHistoryPSTNReceiveBytes':hwVoCallHistoryPSTNReceiveBytes,'hwVoCallHistoryMaxRetainTime':hwVoCallHistoryMaxRetainTime})