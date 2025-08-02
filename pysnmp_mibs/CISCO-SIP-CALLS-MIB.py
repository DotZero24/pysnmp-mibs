_s='cSipMediaStreamGroup'
_r='cSipCallActiveGroup'
_q='cSipMediaStreamDestPort'
_p='cSipMediaStreamDestIpAddr'
_o='cSipMediaStreamDestIpAddrType'
_n='cSipMediaStreamSrcPort'
_m='cSipMediaStreamSrcIpAddr'
_l='cSipMediaStreamSrcIpAddrType'
_k='cSipMediaStreamDtmfPayloadType'
_j='cSipMediaStreamNegotdDtmfRelay'
_i='cSipMediaStreamCodecPayloadType'
_h='cSipMediaStreamNegotdCodec'
_g='cSipMediaStreamType'
_f='cSipMediaStreamCallId'
_e='cSipMediaStreamState'
_d='cSipCallActiveMediaStreamsActive'
_c='cSipCallActiveMediaStreams'
_b='cSipCallActiveDestIpAddr'
_a='cSipCallActiveDestIpAddrType'
_Z='cSipCallActiveDestResPort'
_Y='cSipCallActiveDestResIpAddr'
_X='cSipCallActiveDestResIpAddrType'
_W='cSipCallActiveDestReqPort'
_V='cSipCallActiveDestReqIpAddr'
_U='cSipCallActiveDestReqIpAddrType'
_T='cSipCallActiveSigSrcIpAddr'
_S='cSipCallActiveSigSrcIpAddrType'
_R='cSipCallActiveCalledNumber'
_Q='cSipCallActiveCallingNumber'
_P='cSipCallActiveSubstate'
_O='cSipCallActiveState'
_N='cSipCallActiveType'
_M='cSipCallActiveId'
_L='cSipUASActiveCalls'
_K='cSipUACActiveCalls'
_J='cSipMediaStreamIndex'
_I='active'
_H='SnmpAdminString'
_G='callActiveSetupTime'
_F='callActiveIndex'
_E='DIAL-CONTROL-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-SIP-CALLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CvcCoderTypeRate,=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcCoderTypeRate')
callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_E,_F,_G)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSipCallsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,995))
if mibBuilder.loadTexts:ciscoSipCallsMIB.setRevisions(('2004-04-16 00:00',))
class CSipCallState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('none',1),('idle',2),('setupBuffered',3),('sentInvite',4),('rcvdProceeding',5),('outgoingResrResv',6),('outgoingResrAllocated',7),(_I,8),('rcvdTransfer',9),('disconnecting',10),('dead',11),('rcvdInvite',12),('sentQosProgress',13),('incomingResrResv',14),('sentAlerting',15),('sentSuccess',16),('midCallLocalRespPending',17),('sendMidCallInvitePending',18),('sentMidCallInvite',19),('rcvdSubscribe',20),('subscribeSuccess',21),('subscribeExpired',22),('sentPreAuthRequest',23),('sendNotify',24),('subscribeIdle',25),('sentSubscribe',26),('subscribed',27),('initTransfer',28),('outgoingRegister',29),('incomingRegister',30),('rcvdUnsolicitedNotify',31)))
class CSipCallSubstate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',1),('sentDns',2),('proceedingProceeding',3),('rcvdInviteCallSetup',4),('rcvdInviteProceeding',5),('sentEnum',6),('ackPending',7),('sentNotify',8),('callTransferSendByeAlso',9)))
_CiscoSipCallsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSipCallsMIBNotifs=_CiscoSipCallsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,995,0))
_CiscoSipCallsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSipCallsMIBObjects=_CiscoSipCallsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,995,1))
_CSipCallActive_ObjectIdentity=ObjectIdentity
cSipCallActive=_CSipCallActive_ObjectIdentity((1,3,6,1,4,1,9,9,995,1,1))
_CSipUACActiveCalls_Type=Gauge32
_CSipUACActiveCalls_Object=MibScalar
cSipUACActiveCalls=_CSipUACActiveCalls_Object((1,3,6,1,4,1,9,9,995,1,1,1),_CSipUACActiveCalls_Type())
cSipUACActiveCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipUACActiveCalls.setStatus(_A)
_CSipUASActiveCalls_Type=Gauge32
_CSipUASActiveCalls_Object=MibScalar
cSipUASActiveCalls=_CSipUASActiveCalls_Object((1,3,6,1,4,1,9,9,995,1,1,2),_CSipUASActiveCalls_Type())
cSipUASActiveCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipUASActiveCalls.setStatus(_A)
_CSipCallActiveTable_Object=MibTable
cSipCallActiveTable=_CSipCallActiveTable_Object((1,3,6,1,4,1,9,9,995,1,1,3))
if mibBuilder.loadTexts:cSipCallActiveTable.setStatus(_A)
_CSipCallActiveEntry_Object=MibTableRow
cSipCallActiveEntry=_CSipCallActiveEntry_Object((1,3,6,1,4,1,9,9,995,1,1,3,1))
cSipCallActiveEntry.setIndexNames((0,_E,_G),(0,_E,_F))
if mibBuilder.loadTexts:cSipCallActiveEntry.setStatus(_A)
_CSipCallActiveId_Type=SnmpAdminString
_CSipCallActiveId_Object=MibTableColumn
cSipCallActiveId=_CSipCallActiveId_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,1),_CSipCallActiveId_Type())
cSipCallActiveId.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveId.setStatus(_A)
class _CSipCallActiveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uac',1),('uas',2)))
_CSipCallActiveType_Type.__name__=_D
_CSipCallActiveType_Object=MibTableColumn
cSipCallActiveType=_CSipCallActiveType_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,2),_CSipCallActiveType_Type())
cSipCallActiveType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveType.setStatus(_A)
_CSipCallActiveState_Type=CSipCallState
_CSipCallActiveState_Object=MibTableColumn
cSipCallActiveState=_CSipCallActiveState_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,3),_CSipCallActiveState_Type())
cSipCallActiveState.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveState.setStatus(_A)
_CSipCallActiveSubstate_Type=CSipCallSubstate
_CSipCallActiveSubstate_Object=MibTableColumn
cSipCallActiveSubstate=_CSipCallActiveSubstate_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,4),_CSipCallActiveSubstate_Type())
cSipCallActiveSubstate.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveSubstate.setStatus(_A)
class _CSipCallActiveCallingNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CSipCallActiveCallingNumber_Type.__name__=_H
_CSipCallActiveCallingNumber_Object=MibTableColumn
cSipCallActiveCallingNumber=_CSipCallActiveCallingNumber_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,5),_CSipCallActiveCallingNumber_Type())
cSipCallActiveCallingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveCallingNumber.setStatus(_A)
class _CSipCallActiveCalledNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CSipCallActiveCalledNumber_Type.__name__=_H
_CSipCallActiveCalledNumber_Object=MibTableColumn
cSipCallActiveCalledNumber=_CSipCallActiveCalledNumber_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,6),_CSipCallActiveCalledNumber_Type())
cSipCallActiveCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveCalledNumber.setStatus(_A)
_CSipCallActiveSigSrcIpAddrType_Type=InetAddressType
_CSipCallActiveSigSrcIpAddrType_Object=MibTableColumn
cSipCallActiveSigSrcIpAddrType=_CSipCallActiveSigSrcIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,7),_CSipCallActiveSigSrcIpAddrType_Type())
cSipCallActiveSigSrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveSigSrcIpAddrType.setStatus(_A)
_CSipCallActiveSigSrcIpAddr_Type=InetAddress
_CSipCallActiveSigSrcIpAddr_Object=MibTableColumn
cSipCallActiveSigSrcIpAddr=_CSipCallActiveSigSrcIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,8),_CSipCallActiveSigSrcIpAddr_Type())
cSipCallActiveSigSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveSigSrcIpAddr.setStatus(_A)
_CSipCallActiveDestReqIpAddrType_Type=InetAddressType
_CSipCallActiveDestReqIpAddrType_Object=MibTableColumn
cSipCallActiveDestReqIpAddrType=_CSipCallActiveDestReqIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,9),_CSipCallActiveDestReqIpAddrType_Type())
cSipCallActiveDestReqIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestReqIpAddrType.setStatus(_A)
_CSipCallActiveDestReqIpAddr_Type=InetAddress
_CSipCallActiveDestReqIpAddr_Object=MibTableColumn
cSipCallActiveDestReqIpAddr=_CSipCallActiveDestReqIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,10),_CSipCallActiveDestReqIpAddr_Type())
cSipCallActiveDestReqIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestReqIpAddr.setStatus(_A)
_CSipCallActiveDestReqPort_Type=InetPortNumber
_CSipCallActiveDestReqPort_Object=MibTableColumn
cSipCallActiveDestReqPort=_CSipCallActiveDestReqPort_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,11),_CSipCallActiveDestReqPort_Type())
cSipCallActiveDestReqPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestReqPort.setStatus(_A)
_CSipCallActiveDestResIpAddrType_Type=InetAddressType
_CSipCallActiveDestResIpAddrType_Object=MibTableColumn
cSipCallActiveDestResIpAddrType=_CSipCallActiveDestResIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,12),_CSipCallActiveDestResIpAddrType_Type())
cSipCallActiveDestResIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestResIpAddrType.setStatus(_A)
_CSipCallActiveDestResIpAddr_Type=InetAddress
_CSipCallActiveDestResIpAddr_Object=MibTableColumn
cSipCallActiveDestResIpAddr=_CSipCallActiveDestResIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,13),_CSipCallActiveDestResIpAddr_Type())
cSipCallActiveDestResIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestResIpAddr.setStatus(_A)
_CSipCallActiveDestResPort_Type=InetPortNumber
_CSipCallActiveDestResPort_Object=MibTableColumn
cSipCallActiveDestResPort=_CSipCallActiveDestResPort_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,14),_CSipCallActiveDestResPort_Type())
cSipCallActiveDestResPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestResPort.setStatus(_A)
_CSipCallActiveDestIpAddrType_Type=InetAddressType
_CSipCallActiveDestIpAddrType_Object=MibTableColumn
cSipCallActiveDestIpAddrType=_CSipCallActiveDestIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,15),_CSipCallActiveDestIpAddrType_Type())
cSipCallActiveDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestIpAddrType.setStatus(_A)
_CSipCallActiveDestIpAddr_Type=InetAddress
_CSipCallActiveDestIpAddr_Object=MibTableColumn
cSipCallActiveDestIpAddr=_CSipCallActiveDestIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,16),_CSipCallActiveDestIpAddr_Type())
cSipCallActiveDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveDestIpAddr.setStatus(_A)
_CSipCallActiveMediaStreams_Type=Unsigned32
_CSipCallActiveMediaStreams_Object=MibTableColumn
cSipCallActiveMediaStreams=_CSipCallActiveMediaStreams_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,17),_CSipCallActiveMediaStreams_Type())
cSipCallActiveMediaStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveMediaStreams.setStatus(_A)
_CSipCallActiveMediaStreamsActive_Type=Unsigned32
_CSipCallActiveMediaStreamsActive_Object=MibTableColumn
cSipCallActiveMediaStreamsActive=_CSipCallActiveMediaStreamsActive_Object((1,3,6,1,4,1,9,9,995,1,1,3,1,18),_CSipCallActiveMediaStreamsActive_Type())
cSipCallActiveMediaStreamsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipCallActiveMediaStreamsActive.setStatus(_A)
_CSipMediaStreamsTable_Object=MibTable
cSipMediaStreamsTable=_CSipMediaStreamsTable_Object((1,3,6,1,4,1,9,9,995,1,1,4))
if mibBuilder.loadTexts:cSipMediaStreamsTable.setStatus(_A)
_CSipMediaStreamsEntry_Object=MibTableRow
cSipMediaStreamsEntry=_CSipMediaStreamsEntry_Object((1,3,6,1,4,1,9,9,995,1,1,4,1))
cSipMediaStreamsEntry.setIndexNames((0,_E,_G),(0,_E,_F),(0,_B,_J))
if mibBuilder.loadTexts:cSipMediaStreamsEntry.setStatus(_A)
_CSipMediaStreamIndex_Type=Unsigned32
_CSipMediaStreamIndex_Object=MibTableColumn
cSipMediaStreamIndex=_CSipMediaStreamIndex_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,1),_CSipMediaStreamIndex_Type())
cSipMediaStreamIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cSipMediaStreamIndex.setStatus(_A)
class _CSipMediaStreamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('invalidStreamState',1),('idle',2),('adding',3),('deleting',4),('changing',5),(_I,6),('dead',7)))
_CSipMediaStreamState_Type.__name__=_D
_CSipMediaStreamState_Object=MibTableColumn
cSipMediaStreamState=_CSipMediaStreamState_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,2),_CSipMediaStreamState_Type())
cSipMediaStreamState.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamState.setStatus(_A)
class _CSipMediaStreamCallId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CSipMediaStreamCallId_Type.__name__=_D
_CSipMediaStreamCallId_Object=MibTableColumn
cSipMediaStreamCallId=_CSipMediaStreamCallId_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,3),_CSipMediaStreamCallId_Type())
cSipMediaStreamCallId.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamCallId.setStatus(_A)
class _CSipMediaStreamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('voiceOnly',1),('dtmfRelay',2),('voiceAndDtmfRelay',3)))
_CSipMediaStreamType_Type.__name__=_D
_CSipMediaStreamType_Object=MibTableColumn
cSipMediaStreamType=_CSipMediaStreamType_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,4),_CSipMediaStreamType_Type())
cSipMediaStreamType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamType.setStatus(_A)
_CSipMediaStreamNegotdCodec_Type=CvcCoderTypeRate
_CSipMediaStreamNegotdCodec_Object=MibTableColumn
cSipMediaStreamNegotdCodec=_CSipMediaStreamNegotdCodec_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,5),_CSipMediaStreamNegotdCodec_Type())
cSipMediaStreamNegotdCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamNegotdCodec.setStatus(_A)
class _CSipMediaStreamCodecPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,127))
_CSipMediaStreamCodecPayloadType_Type.__name__=_D
_CSipMediaStreamCodecPayloadType_Object=MibTableColumn
cSipMediaStreamCodecPayloadType=_CSipMediaStreamCodecPayloadType_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,6),_CSipMediaStreamCodecPayloadType_Type())
cSipMediaStreamCodecPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamCodecPayloadType.setStatus(_A)
class _CSipMediaStreamNegotdDtmfRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inBandVoice',1),('rtpNte',2)))
_CSipMediaStreamNegotdDtmfRelay_Type.__name__=_D
_CSipMediaStreamNegotdDtmfRelay_Object=MibTableColumn
cSipMediaStreamNegotdDtmfRelay=_CSipMediaStreamNegotdDtmfRelay_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,7),_CSipMediaStreamNegotdDtmfRelay_Type())
cSipMediaStreamNegotdDtmfRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamNegotdDtmfRelay.setStatus(_A)
class _CSipMediaStreamDtmfPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,127))
_CSipMediaStreamDtmfPayloadType_Type.__name__=_D
_CSipMediaStreamDtmfPayloadType_Object=MibTableColumn
cSipMediaStreamDtmfPayloadType=_CSipMediaStreamDtmfPayloadType_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,8),_CSipMediaStreamDtmfPayloadType_Type())
cSipMediaStreamDtmfPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamDtmfPayloadType.setStatus(_A)
_CSipMediaStreamSrcIpAddrType_Type=InetAddressType
_CSipMediaStreamSrcIpAddrType_Object=MibTableColumn
cSipMediaStreamSrcIpAddrType=_CSipMediaStreamSrcIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,9),_CSipMediaStreamSrcIpAddrType_Type())
cSipMediaStreamSrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamSrcIpAddrType.setStatus(_A)
_CSipMediaStreamSrcIpAddr_Type=InetAddress
_CSipMediaStreamSrcIpAddr_Object=MibTableColumn
cSipMediaStreamSrcIpAddr=_CSipMediaStreamSrcIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,10),_CSipMediaStreamSrcIpAddr_Type())
cSipMediaStreamSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamSrcIpAddr.setStatus(_A)
_CSipMediaStreamSrcPort_Type=InetPortNumber
_CSipMediaStreamSrcPort_Object=MibTableColumn
cSipMediaStreamSrcPort=_CSipMediaStreamSrcPort_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,11),_CSipMediaStreamSrcPort_Type())
cSipMediaStreamSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamSrcPort.setStatus(_A)
_CSipMediaStreamDestIpAddrType_Type=InetAddressType
_CSipMediaStreamDestIpAddrType_Object=MibTableColumn
cSipMediaStreamDestIpAddrType=_CSipMediaStreamDestIpAddrType_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,12),_CSipMediaStreamDestIpAddrType_Type())
cSipMediaStreamDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamDestIpAddrType.setStatus(_A)
_CSipMediaStreamDestIpAddr_Type=InetAddress
_CSipMediaStreamDestIpAddr_Object=MibTableColumn
cSipMediaStreamDestIpAddr=_CSipMediaStreamDestIpAddr_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,13),_CSipMediaStreamDestIpAddr_Type())
cSipMediaStreamDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamDestIpAddr.setStatus(_A)
_CSipMediaStreamDestPort_Type=InetPortNumber
_CSipMediaStreamDestPort_Object=MibTableColumn
cSipMediaStreamDestPort=_CSipMediaStreamDestPort_Object((1,3,6,1,4,1,9,9,995,1,1,4,1,14),_CSipMediaStreamDestPort_Type())
cSipMediaStreamDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSipMediaStreamDestPort.setStatus(_A)
_CSipCallsMIBConformance_ObjectIdentity=ObjectIdentity
cSipCallsMIBConformance=_CSipCallsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,995,1,2))
_CSipCallsMIBCompliances_ObjectIdentity=ObjectIdentity
cSipCallsMIBCompliances=_CSipCallsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,995,1,2,1))
_CSipCallsMIBGroups_ObjectIdentity=ObjectIdentity
cSipCallsMIBGroups=_CSipCallsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,995,1,2,2))
cSipCallActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,995,1,2,2,1))
cSipCallActiveGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:cSipCallActiveGroup.setStatus(_A)
cSipMediaStreamGroup=ObjectGroup((1,3,6,1,4,1,9,9,995,1,2,2,2))
cSipMediaStreamGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cSipMediaStreamGroup.setStatus(_A)
cSipCallsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,995,1,2,1,1))
cSipCallsMIBCompliance.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:cSipCallsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CSipCallState':CSipCallState,'CSipCallSubstate':CSipCallSubstate,'ciscoSipCallsMIB':ciscoSipCallsMIB,'ciscoSipCallsMIBNotifs':ciscoSipCallsMIBNotifs,'ciscoSipCallsMIBObjects':ciscoSipCallsMIBObjects,'cSipCallActive':cSipCallActive,_K:cSipUACActiveCalls,_L:cSipUASActiveCalls,'cSipCallActiveTable':cSipCallActiveTable,'cSipCallActiveEntry':cSipCallActiveEntry,_M:cSipCallActiveId,_N:cSipCallActiveType,_O:cSipCallActiveState,_P:cSipCallActiveSubstate,_Q:cSipCallActiveCallingNumber,_R:cSipCallActiveCalledNumber,_S:cSipCallActiveSigSrcIpAddrType,_T:cSipCallActiveSigSrcIpAddr,_U:cSipCallActiveDestReqIpAddrType,_V:cSipCallActiveDestReqIpAddr,_W:cSipCallActiveDestReqPort,_X:cSipCallActiveDestResIpAddrType,_Y:cSipCallActiveDestResIpAddr,_Z:cSipCallActiveDestResPort,_a:cSipCallActiveDestIpAddrType,_b:cSipCallActiveDestIpAddr,_c:cSipCallActiveMediaStreams,_d:cSipCallActiveMediaStreamsActive,'cSipMediaStreamsTable':cSipMediaStreamsTable,'cSipMediaStreamsEntry':cSipMediaStreamsEntry,_J:cSipMediaStreamIndex,_e:cSipMediaStreamState,_f:cSipMediaStreamCallId,_g:cSipMediaStreamType,_h:cSipMediaStreamNegotdCodec,_i:cSipMediaStreamCodecPayloadType,_j:cSipMediaStreamNegotdDtmfRelay,_k:cSipMediaStreamDtmfPayloadType,_l:cSipMediaStreamSrcIpAddrType,_m:cSipMediaStreamSrcIpAddr,_n:cSipMediaStreamSrcPort,_o:cSipMediaStreamDestIpAddrType,_p:cSipMediaStreamDestIpAddr,_q:cSipMediaStreamDestPort,'cSipCallsMIBConformance':cSipCallsMIBConformance,'cSipCallsMIBCompliances':cSipCallsMIBCompliances,'cSipCallsMIBCompliance':cSipCallsMIBCompliance,'cSipCallsMIBGroups':cSipCallsMIBGroups,_r:cSipCallActiveGroup,_s:cSipMediaStreamGroup})