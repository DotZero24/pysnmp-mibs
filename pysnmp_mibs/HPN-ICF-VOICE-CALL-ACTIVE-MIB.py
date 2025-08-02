_F='callActiveSetupTime'
_E='callActiveIndex'
_D='Integer32'
_C='DIAL-CONTROL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_C,_E,_F)
hpnicfVoice,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfVoice')
HpnicfCodecType,=mibBuilder.importSymbols('HPN-ICF-VOICE-DIAL-CONTROL-MIB','HpnicfCodecType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfVoCallActive=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,15))
if mibBuilder.loadTexts:hpnicfVoCallActive.setRevisions(('2008-02-17 00:00',))
class HpnicfGUid(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnicfVoiceCallActiveObjects_ObjectIdentity=ObjectIdentity
hpnicfVoiceCallActiveObjects=_HpnicfVoiceCallActiveObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1))
_HpnicfVoiceCallActiveTable_Object=MibTable
hpnicfVoiceCallActiveTable=_HpnicfVoiceCallActiveTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1))
if mibBuilder.loadTexts:hpnicfVoiceCallActiveTable.setStatus(_A)
_HpnicfVoiceCallActiveEntry_Object=MibTableRow
hpnicfVoiceCallActiveEntry=_HpnicfVoiceCallActiveEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1))
hpnicfVoiceCallActiveEntry.setIndexNames((0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:hpnicfVoiceCallActiveEntry.setStatus(_A)
_HpnicfVoCallActiveConnectionId_Type=HpnicfGUid
_HpnicfVoCallActiveConnectionId_Object=MibTableColumn
hpnicfVoCallActiveConnectionId=_HpnicfVoCallActiveConnectionId_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,1),_HpnicfVoCallActiveConnectionId_Type())
hpnicfVoCallActiveConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveConnectionId.setStatus(_A)
_HpnicfVoCallActiveTxDuration_Type=Gauge32
_HpnicfVoCallActiveTxDuration_Object=MibTableColumn
hpnicfVoCallActiveTxDuration=_HpnicfVoCallActiveTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,2),_HpnicfVoCallActiveTxDuration_Type())
hpnicfVoCallActiveTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveTxDuration.setStatus(_A)
_HpnicfVoCallActiveVoiceTxDuration_Type=Gauge32
_HpnicfVoCallActiveVoiceTxDuration_Object=MibTableColumn
hpnicfVoCallActiveVoiceTxDuration=_HpnicfVoCallActiveVoiceTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,3),_HpnicfVoCallActiveVoiceTxDuration_Type())
hpnicfVoCallActiveVoiceTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveVoiceTxDuration.setStatus(_A)
_HpnicfVoCallActiveFaxTxDuration_Type=Gauge32
_HpnicfVoCallActiveFaxTxDuration_Object=MibTableColumn
hpnicfVoCallActiveFaxTxDuration=_HpnicfVoCallActiveFaxTxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,4),_HpnicfVoCallActiveFaxTxDuration_Type())
hpnicfVoCallActiveFaxTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveFaxTxDuration.setStatus(_A)
_HpnicfVoCallActiveCoderType_Type=HpnicfCodecType
_HpnicfVoCallActiveCoderType_Object=MibTableColumn
hpnicfVoCallActiveCoderType=_HpnicfVoCallActiveCoderType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,5),_HpnicfVoCallActiveCoderType_Type())
hpnicfVoCallActiveCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveCoderType.setStatus(_A)
_HpnicfVoCallActiveImgPageCount_Type=Gauge32
_HpnicfVoCallActiveImgPageCount_Object=MibTableColumn
hpnicfVoCallActiveImgPageCount=_HpnicfVoCallActiveImgPageCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,1,1,6),_HpnicfVoCallActiveImgPageCount_Type())
hpnicfVoCallActiveImgPageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoCallActiveImgPageCount.setStatus(_A)
_HpnicfVoiceVoIPCallActiveTable_Object=MibTable
hpnicfVoiceVoIPCallActiveTable=_HpnicfVoiceVoIPCallActiveTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2))
if mibBuilder.loadTexts:hpnicfVoiceVoIPCallActiveTable.setStatus(_A)
_HpnicfVoiceVoIPCallActiveEntry_Object=MibTableRow
hpnicfVoiceVoIPCallActiveEntry=_HpnicfVoiceVoIPCallActiveEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1))
hpnicfVoiceVoIPCallActiveEntry.setIndexNames((0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:hpnicfVoiceVoIPCallActiveEntry.setStatus(_A)
_HpnicfVoVoIPCallActiveConnectionId_Type=HpnicfGUid
_HpnicfVoVoIPCallActiveConnectionId_Object=MibTableColumn
hpnicfVoVoIPCallActiveConnectionId=_HpnicfVoVoIPCallActiveConnectionId_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,1),_HpnicfVoVoIPCallActiveConnectionId_Type())
hpnicfVoVoIPCallActiveConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveConnectionId.setStatus(_A)
_HpnicfVoVoIPCallActiveRemSigIPType_Type=InetAddressType
_HpnicfVoVoIPCallActiveRemSigIPType_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemSigIPType=_HpnicfVoVoIPCallActiveRemSigIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,2),_HpnicfVoVoIPCallActiveRemSigIPType_Type())
hpnicfVoVoIPCallActiveRemSigIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemSigIPType.setStatus(_A)
_HpnicfVoVoIPCallActiveRemSigIPAddr_Type=InetAddress
_HpnicfVoVoIPCallActiveRemSigIPAddr_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemSigIPAddr=_HpnicfVoVoIPCallActiveRemSigIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,3),_HpnicfVoVoIPCallActiveRemSigIPAddr_Type())
hpnicfVoVoIPCallActiveRemSigIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemSigIPAddr.setStatus(_A)
class _HpnicfVoVoIPCallActiveRemSigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfVoVoIPCallActiveRemSigPort_Type.__name__=_D
_HpnicfVoVoIPCallActiveRemSigPort_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemSigPort=_HpnicfVoVoIPCallActiveRemSigPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,4),_HpnicfVoVoIPCallActiveRemSigPort_Type())
hpnicfVoVoIPCallActiveRemSigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemSigPort.setStatus(_A)
_HpnicfVoVoIPCallActiveRemMedIPType_Type=InetAddressType
_HpnicfVoVoIPCallActiveRemMedIPType_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemMedIPType=_HpnicfVoVoIPCallActiveRemMedIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,5),_HpnicfVoVoIPCallActiveRemMedIPType_Type())
hpnicfVoVoIPCallActiveRemMedIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemMedIPType.setStatus(_A)
_HpnicfVoVoIPCallActiveRemMedIPAddr_Type=InetAddress
_HpnicfVoVoIPCallActiveRemMedIPAddr_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemMedIPAddr=_HpnicfVoVoIPCallActiveRemMedIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,6),_HpnicfVoVoIPCallActiveRemMedIPAddr_Type())
hpnicfVoVoIPCallActiveRemMedIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemMedIPAddr.setStatus(_A)
class _HpnicfVoVoIPCallActiveRemMedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfVoVoIPCallActiveRemMedPort_Type.__name__=_D
_HpnicfVoVoIPCallActiveRemMedPort_Object=MibTableColumn
hpnicfVoVoIPCallActiveRemMedPort=_HpnicfVoVoIPCallActiveRemMedPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,7),_HpnicfVoVoIPCallActiveRemMedPort_Type())
hpnicfVoVoIPCallActiveRemMedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveRemMedPort.setStatus(_A)
class _HpnicfVoVoIPCallActiveSessProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('h323',2),('sip',3)))
_HpnicfVoVoIPCallActiveSessProtocol_Type.__name__=_D
_HpnicfVoVoIPCallActiveSessProtocol_Object=MibTableColumn
hpnicfVoVoIPCallActiveSessProtocol=_HpnicfVoVoIPCallActiveSessProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,8),_HpnicfVoVoIPCallActiveSessProtocol_Type())
hpnicfVoVoIPCallActiveSessProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveSessProtocol.setStatus(_A)
_HpnicfVoVoIPCallActiveCoderType_Type=HpnicfCodecType
_HpnicfVoVoIPCallActiveCoderType_Object=MibTableColumn
hpnicfVoVoIPCallActiveCoderType=_HpnicfVoVoIPCallActiveCoderType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,15,1,2,1,9),_HpnicfVoVoIPCallActiveCoderType_Type())
hpnicfVoVoIPCallActiveCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPCallActiveCoderType.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-VOICE-CALL-ACTIVE-MIB',**{'HpnicfGUid':HpnicfGUid,'hpnicfVoCallActive':hpnicfVoCallActive,'hpnicfVoiceCallActiveObjects':hpnicfVoiceCallActiveObjects,'hpnicfVoiceCallActiveTable':hpnicfVoiceCallActiveTable,'hpnicfVoiceCallActiveEntry':hpnicfVoiceCallActiveEntry,'hpnicfVoCallActiveConnectionId':hpnicfVoCallActiveConnectionId,'hpnicfVoCallActiveTxDuration':hpnicfVoCallActiveTxDuration,'hpnicfVoCallActiveVoiceTxDuration':hpnicfVoCallActiveVoiceTxDuration,'hpnicfVoCallActiveFaxTxDuration':hpnicfVoCallActiveFaxTxDuration,'hpnicfVoCallActiveCoderType':hpnicfVoCallActiveCoderType,'hpnicfVoCallActiveImgPageCount':hpnicfVoCallActiveImgPageCount,'hpnicfVoiceVoIPCallActiveTable':hpnicfVoiceVoIPCallActiveTable,'hpnicfVoiceVoIPCallActiveEntry':hpnicfVoiceVoIPCallActiveEntry,'hpnicfVoVoIPCallActiveConnectionId':hpnicfVoVoIPCallActiveConnectionId,'hpnicfVoVoIPCallActiveRemSigIPType':hpnicfVoVoIPCallActiveRemSigIPType,'hpnicfVoVoIPCallActiveRemSigIPAddr':hpnicfVoVoIPCallActiveRemSigIPAddr,'hpnicfVoVoIPCallActiveRemSigPort':hpnicfVoVoIPCallActiveRemSigPort,'hpnicfVoVoIPCallActiveRemMedIPType':hpnicfVoVoIPCallActiveRemMedIPType,'hpnicfVoVoIPCallActiveRemMedIPAddr':hpnicfVoVoIPCallActiveRemMedIPAddr,'hpnicfVoVoIPCallActiveRemMedPort':hpnicfVoVoIPCallActiveRemMedPort,'hpnicfVoVoIPCallActiveSessProtocol':hpnicfVoVoIPCallActiveSessProtocol,'hpnicfVoVoIPCallActiveCoderType':hpnicfVoVoIPCallActiveCoderType})