_F='unknown'
_E='hpnicfCallHistoryIndex'
_D='HPN-ICF-VOICE-CALL-HISTORY-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AbsoluteCounter32,=mibBuilder.importSymbols('DIAL-CONTROL-MIB','AbsoluteCounter32')
hpnicfVoice,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfVoice')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
hpnicfVoCallHistory=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,16))
if mibBuilder.loadTexts:hpnicfVoCallHistory.setRevisions(('2008-02-17 00:00',))
class HpnicfGUid(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class HpnicfCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('g711a',1),('g711u',2),('g723r53',3),('g723r63',4),('g729r8',5),('g729a',6),('g726r16',7),('g726r24',8),('g726r32',9),('g726r40',10),(_F,11),('g729br8',12)))
_HpnicfVoiceCallHistoryObjects_ObjectIdentity=ObjectIdentity
hpnicfVoiceCallHistoryObjects=_HpnicfVoiceCallHistoryObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1))
_HpnicfCallHistoryTable_Object=MibTable
hpnicfCallHistoryTable=_HpnicfCallHistoryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1))
if mibBuilder.loadTexts:hpnicfCallHistoryTable.setStatus(_A)
_HpnicfCallHistoryEntry_Object=MibTableRow
hpnicfCallHistoryEntry=_HpnicfCallHistoryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1))
hpnicfCallHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfCallHistoryEntry.setStatus(_A)
class _HpnicfCallHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCallHistoryIndex_Type.__name__=_C
_HpnicfCallHistoryIndex_Object=MibTableColumn
hpnicfCallHistoryIndex=_HpnicfCallHistoryIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,1),_HpnicfCallHistoryIndex_Type())
hpnicfCallHistoryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfCallHistoryIndex.setStatus(_A)
_HpnicfCallHistorySetupTime_Type=TimeStamp
_HpnicfCallHistorySetupTime_Object=MibTableColumn
hpnicfCallHistorySetupTime=_HpnicfCallHistorySetupTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,2),_HpnicfCallHistorySetupTime_Type())
hpnicfCallHistorySetupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistorySetupTime.setStatus(_A)
_HpnicfCallHistoryConnectTime_Type=TimeStamp
_HpnicfCallHistoryConnectTime_Object=MibTableColumn
hpnicfCallHistoryConnectTime=_HpnicfCallHistoryConnectTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,3),_HpnicfCallHistoryConnectTime_Type())
hpnicfCallHistoryConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryConnectTime.setStatus(_A)
_HpnicfCallHistoryTerminateTime_Type=TimeStamp
_HpnicfCallHistoryTerminateTime_Object=MibTableColumn
hpnicfCallHistoryTerminateTime=_HpnicfCallHistoryTerminateTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,4),_HpnicfCallHistoryTerminateTime_Type())
hpnicfCallHistoryTerminateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryTerminateTime.setStatus(_A)
_HpnicfCallHistoryPeerAddress_Type=DisplayString
_HpnicfCallHistoryPeerAddress_Object=MibTableColumn
hpnicfCallHistoryPeerAddress=_HpnicfCallHistoryPeerAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,5),_HpnicfCallHistoryPeerAddress_Type())
hpnicfCallHistoryPeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryPeerAddress.setStatus(_A)
class _HpnicfCallHistoryPeerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfCallHistoryPeerId_Type.__name__=_C
_HpnicfCallHistoryPeerId_Object=MibTableColumn
hpnicfCallHistoryPeerId=_HpnicfCallHistoryPeerId_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,6),_HpnicfCallHistoryPeerId_Type())
hpnicfCallHistoryPeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryPeerId.setStatus(_A)
_HpnicfCallHistoryLogicalIfIndex_Type=InterfaceIndexOrZero
_HpnicfCallHistoryLogicalIfIndex_Object=MibTableColumn
hpnicfCallHistoryLogicalIfIndex=_HpnicfCallHistoryLogicalIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,7),_HpnicfCallHistoryLogicalIfIndex_Type())
hpnicfCallHistoryLogicalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryLogicalIfIndex.setStatus(_A)
class _HpnicfCallHistoryCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('originate',1),('answer',2),('callback',3)))
_HpnicfCallHistoryCallOrigin_Type.__name__=_C
_HpnicfCallHistoryCallOrigin_Object=MibTableColumn
hpnicfCallHistoryCallOrigin=_HpnicfCallHistoryCallOrigin_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,8),_HpnicfCallHistoryCallOrigin_Type())
hpnicfCallHistoryCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryCallOrigin.setStatus(_A)
_HpnicfCallHistoryChargedUnits_Type=AbsoluteCounter32
_HpnicfCallHistoryChargedUnits_Object=MibTableColumn
hpnicfCallHistoryChargedUnits=_HpnicfCallHistoryChargedUnits_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,9),_HpnicfCallHistoryChargedUnits_Type())
hpnicfCallHistoryChargedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryChargedUnits.setStatus(_A)
class _HpnicfCallHistoryInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('speech',2),('unrestrictedDigital',3),('unrestrictedDigital56',4),('restrictedDigital',5),('audio31',6),('audio7',7),('video',8),('packetSwitched',9),('fax',10)))
_HpnicfCallHistoryInfoType_Type.__name__=_C
_HpnicfCallHistoryInfoType_Object=MibTableColumn
hpnicfCallHistoryInfoType=_HpnicfCallHistoryInfoType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,10),_HpnicfCallHistoryInfoType_Type())
hpnicfCallHistoryInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryInfoType.setStatus(_A)
_HpnicfCallHistoryTransmitPackets_Type=AbsoluteCounter32
_HpnicfCallHistoryTransmitPackets_Object=MibTableColumn
hpnicfCallHistoryTransmitPackets=_HpnicfCallHistoryTransmitPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,11),_HpnicfCallHistoryTransmitPackets_Type())
hpnicfCallHistoryTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryTransmitPackets.setStatus(_A)
_HpnicfCallHistoryTransmitBytes_Type=AbsoluteCounter32
_HpnicfCallHistoryTransmitBytes_Object=MibTableColumn
hpnicfCallHistoryTransmitBytes=_HpnicfCallHistoryTransmitBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,12),_HpnicfCallHistoryTransmitBytes_Type())
hpnicfCallHistoryTransmitBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryTransmitBytes.setStatus(_A)
_HpnicfCallHistoryReceivePackets_Type=AbsoluteCounter32
_HpnicfCallHistoryReceivePackets_Object=MibTableColumn
hpnicfCallHistoryReceivePackets=_HpnicfCallHistoryReceivePackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,13),_HpnicfCallHistoryReceivePackets_Type())
hpnicfCallHistoryReceivePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryReceivePackets.setStatus(_A)
_HpnicfCallHistoryReceiveBytes_Type=AbsoluteCounter32
_HpnicfCallHistoryReceiveBytes_Object=MibTableColumn
hpnicfCallHistoryReceiveBytes=_HpnicfCallHistoryReceiveBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,1,1,14),_HpnicfCallHistoryReceiveBytes_Type())
hpnicfCallHistoryReceiveBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfCallHistoryReceiveBytes.setStatus(_A)
_HpnicfVoiceCallHistoryTable_Object=MibTable
hpnicfVoiceCallHistoryTable=_HpnicfVoiceCallHistoryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2))
if mibBuilder.loadTexts:hpnicfVoiceCallHistoryTable.setStatus(_A)
_HpnicfVoiceCallHistoryEntry_Object=MibTableRow
hpnicfVoiceCallHistoryEntry=_HpnicfVoiceCallHistoryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1))
hpnicfVoiceCallHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfVoiceCallHistoryEntry.setStatus(_A)
_HpnicfVoCallHistoryConnectionId_Type=HpnicfGUid
_HpnicfVoCallHistoryConnectionId_Object=MibTableColumn
hpnicfVoCallHistoryConnectionId=_HpnicfVoCallHistoryConnectionId_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,1),_HpnicfVoCallHistoryConnectionId_Type())
hpnicfVoCallHistoryConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryConnectionId.setStatus(_A)
_HpnicfVoCallHistoryTxDuration_Type=Gauge32
_HpnicfVoCallHistoryTxDuration_Object=MibTableColumn
hpnicfVoCallHistoryTxDuration=_HpnicfVoCallHistoryTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,2),_HpnicfVoCallHistoryTxDuration_Type())
hpnicfVoCallHistoryTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryTxDuration.setStatus(_A)
_HpnicfVoCallHistoryVoiceTxDuration_Type=Gauge32
_HpnicfVoCallHistoryVoiceTxDuration_Object=MibTableColumn
hpnicfVoCallHistoryVoiceTxDuration=_HpnicfVoCallHistoryVoiceTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,3),_HpnicfVoCallHistoryVoiceTxDuration_Type())
hpnicfVoCallHistoryVoiceTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryVoiceTxDuration.setStatus(_A)
_HpnicfVoCallHistoryFaxTxDuration_Type=Gauge32
_HpnicfVoCallHistoryFaxTxDuration_Object=MibTableColumn
hpnicfVoCallHistoryFaxTxDuration=_HpnicfVoCallHistoryFaxTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,4),_HpnicfVoCallHistoryFaxTxDuration_Type())
hpnicfVoCallHistoryFaxTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryFaxTxDuration.setStatus(_A)
_HpnicfVoCallHistoryCoderType_Type=HpnicfCodecType
_HpnicfVoCallHistoryCoderType_Object=MibTableColumn
hpnicfVoCallHistoryCoderType=_HpnicfVoCallHistoryCoderType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,5),_HpnicfVoCallHistoryCoderType_Type())
hpnicfVoCallHistoryCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryCoderType.setStatus(_A)
_HpnicfVoCallHistoryImgPageCount_Type=Gauge32
_HpnicfVoCallHistoryImgPageCount_Object=MibTableColumn
hpnicfVoCallHistoryImgPageCount=_HpnicfVoCallHistoryImgPageCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,2,1,6),_HpnicfVoCallHistoryImgPageCount_Type())
hpnicfVoCallHistoryImgPageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallHistoryImgPageCount.setStatus(_A)
_HpnicfVoiceVoIPCallHistoryTable_Object=MibTable
hpnicfVoiceVoIPCallHistoryTable=_HpnicfVoiceVoIPCallHistoryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3))
if mibBuilder.loadTexts:hpnicfVoiceVoIPCallHistoryTable.setStatus(_A)
_HpnicfVoiceVoIPCallHistoryEntry_Object=MibTableRow
hpnicfVoiceVoIPCallHistoryEntry=_HpnicfVoiceVoIPCallHistoryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1))
hpnicfVoiceVoIPCallHistoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfVoiceVoIPCallHistoryEntry.setStatus(_A)
_HpnicfVoVoIPCallHistoryConnectionId_Type=HpnicfGUid
_HpnicfVoVoIPCallHistoryConnectionId_Object=MibTableColumn
hpnicfVoVoIPCallHistoryConnectionId=_HpnicfVoVoIPCallHistoryConnectionId_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,1),_HpnicfVoVoIPCallHistoryConnectionId_Type())
hpnicfVoVoIPCallHistoryConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryConnectionId.setStatus(_A)
_HpnicfVoVoIPCallHistoryRemSigIPType_Type=InetAddressType
_HpnicfVoVoIPCallHistoryRemSigIPType_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemSigIPType=_HpnicfVoVoIPCallHistoryRemSigIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,2),_HpnicfVoVoIPCallHistoryRemSigIPType_Type())
hpnicfVoVoIPCallHistoryRemSigIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemSigIPType.setStatus(_A)
_HpnicfVoVoIPCallHistoryRemSigIPAddr_Type=InetAddress
_HpnicfVoVoIPCallHistoryRemSigIPAddr_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemSigIPAddr=_HpnicfVoVoIPCallHistoryRemSigIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,3),_HpnicfVoVoIPCallHistoryRemSigIPAddr_Type())
hpnicfVoVoIPCallHistoryRemSigIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemSigIPAddr.setStatus(_A)
class _HpnicfVoVoIPCallHistoryRemSigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfVoVoIPCallHistoryRemSigPort_Type.__name__=_C
_HpnicfVoVoIPCallHistoryRemSigPort_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemSigPort=_HpnicfVoVoIPCallHistoryRemSigPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,4),_HpnicfVoVoIPCallHistoryRemSigPort_Type())
hpnicfVoVoIPCallHistoryRemSigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemSigPort.setStatus(_A)
_HpnicfVoVoIPCallHistoryRemMedIPType_Type=InetAddressType
_HpnicfVoVoIPCallHistoryRemMedIPType_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemMedIPType=_HpnicfVoVoIPCallHistoryRemMedIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,5),_HpnicfVoVoIPCallHistoryRemMedIPType_Type())
hpnicfVoVoIPCallHistoryRemMedIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemMedIPType.setStatus(_A)
_HpnicfVoVoIPCallHistoryRemMedIPAddr_Type=InetAddress
_HpnicfVoVoIPCallHistoryRemMedIPAddr_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemMedIPAddr=_HpnicfVoVoIPCallHistoryRemMedIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,6),_HpnicfVoVoIPCallHistoryRemMedIPAddr_Type())
hpnicfVoVoIPCallHistoryRemMedIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemMedIPAddr.setStatus(_A)
class _HpnicfVoVoIPCallHistoryRemMedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfVoVoIPCallHistoryRemMedPort_Type.__name__=_C
_HpnicfVoVoIPCallHistoryRemMedPort_Object=MibTableColumn
hpnicfVoVoIPCallHistoryRemMedPort=_HpnicfVoVoIPCallHistoryRemMedPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,7),_HpnicfVoVoIPCallHistoryRemMedPort_Type())
hpnicfVoVoIPCallHistoryRemMedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryRemMedPort.setStatus(_A)
class _HpnicfVoVoIPCallHistorySessProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('h323',2),('sip',3)))
_HpnicfVoVoIPCallHistorySessProtocol_Type.__name__=_C
_HpnicfVoVoIPCallHistorySessProtocol_Object=MibTableColumn
hpnicfVoVoIPCallHistorySessProtocol=_HpnicfVoVoIPCallHistorySessProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,8),_HpnicfVoVoIPCallHistorySessProtocol_Type())
hpnicfVoVoIPCallHistorySessProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistorySessProtocol.setStatus(_A)
_HpnicfVoVoIPCallHistoryCoderType_Type=HpnicfCodecType
_HpnicfVoVoIPCallHistoryCoderType_Object=MibTableColumn
hpnicfVoVoIPCallHistoryCoderType=_HpnicfVoVoIPCallHistoryCoderType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,16,1,3,1,9),_HpnicfVoVoIPCallHistoryCoderType_Type())
hpnicfVoVoIPCallHistoryCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallHistoryCoderType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HpnicfGUid':HpnicfGUid,'HpnicfCodecType':HpnicfCodecType,'hpnicfVoCallHistory':hpnicfVoCallHistory,'hpnicfVoiceCallHistoryObjects':hpnicfVoiceCallHistoryObjects,'hpnicfCallHistoryTable':hpnicfCallHistoryTable,'hpnicfCallHistoryEntry':hpnicfCallHistoryEntry,_E:hpnicfCallHistoryIndex,'hpnicfCallHistorySetupTime':hpnicfCallHistorySetupTime,'hpnicfCallHistoryConnectTime':hpnicfCallHistoryConnectTime,'hpnicfCallHistoryTerminateTime':hpnicfCallHistoryTerminateTime,'hpnicfCallHistoryPeerAddress':hpnicfCallHistoryPeerAddress,'hpnicfCallHistoryPeerId':hpnicfCallHistoryPeerId,'hpnicfCallHistoryLogicalIfIndex':hpnicfCallHistoryLogicalIfIndex,'hpnicfCallHistoryCallOrigin':hpnicfCallHistoryCallOrigin,'hpnicfCallHistoryChargedUnits':hpnicfCallHistoryChargedUnits,'hpnicfCallHistoryInfoType':hpnicfCallHistoryInfoType,'hpnicfCallHistoryTransmitPackets':hpnicfCallHistoryTransmitPackets,'hpnicfCallHistoryTransmitBytes':hpnicfCallHistoryTransmitBytes,'hpnicfCallHistoryReceivePackets':hpnicfCallHistoryReceivePackets,'hpnicfCallHistoryReceiveBytes':hpnicfCallHistoryReceiveBytes,'hpnicfVoiceCallHistoryTable':hpnicfVoiceCallHistoryTable,'hpnicfVoiceCallHistoryEntry':hpnicfVoiceCallHistoryEntry,'hpnicfVoCallHistoryConnectionId':hpnicfVoCallHistoryConnectionId,'hpnicfVoCallHistoryTxDuration':hpnicfVoCallHistoryTxDuration,'hpnicfVoCallHistoryVoiceTxDuration':hpnicfVoCallHistoryVoiceTxDuration,'hpnicfVoCallHistoryFaxTxDuration':hpnicfVoCallHistoryFaxTxDuration,'hpnicfVoCallHistoryCoderType':hpnicfVoCallHistoryCoderType,'hpnicfVoCallHistoryImgPageCount':hpnicfVoCallHistoryImgPageCount,'hpnicfVoiceVoIPCallHistoryTable':hpnicfVoiceVoIPCallHistoryTable,'hpnicfVoiceVoIPCallHistoryEntry':hpnicfVoiceVoIPCallHistoryEntry,'hpnicfVoVoIPCallHistoryConnectionId':hpnicfVoVoIPCallHistoryConnectionId,'hpnicfVoVoIPCallHistoryRemSigIPType':hpnicfVoVoIPCallHistoryRemSigIPType,'hpnicfVoVoIPCallHistoryRemSigIPAddr':hpnicfVoVoIPCallHistoryRemSigIPAddr,'hpnicfVoVoIPCallHistoryRemSigPort':hpnicfVoVoIPCallHistoryRemSigPort,'hpnicfVoVoIPCallHistoryRemMedIPType':hpnicfVoVoIPCallHistoryRemMedIPType,'hpnicfVoVoIPCallHistoryRemMedIPAddr':hpnicfVoVoIPCallHistoryRemMedIPAddr,'hpnicfVoVoIPCallHistoryRemMedPort':hpnicfVoVoIPCallHistoryRemMedPort,'hpnicfVoVoIPCallHistorySessProtocol':hpnicfVoVoIPCallHistorySessProtocol,'hpnicfVoVoIPCallHistoryCoderType':hpnicfVoVoIPCallHistoryCoderType})