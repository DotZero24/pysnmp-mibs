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
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
H3cCodecType,=mibBuilder.importSymbols('A3COM-HUAWEI-VOICE-DIAL-CONTROL-MIB','H3cCodecType')
callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_C,_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoCallActive=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,15))
if mibBuilder.loadTexts:h3cVoCallActive.setRevisions(('2008-02-17 00:00',))
class H3cGUid(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_H3cVoiceCallActiveObjects_ObjectIdentity=ObjectIdentity
h3cVoiceCallActiveObjects=_H3cVoiceCallActiveObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,15,1))
_H3cVoiceCallActiveTable_Object=MibTable
h3cVoiceCallActiveTable=_H3cVoiceCallActiveTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1))
if mibBuilder.loadTexts:h3cVoiceCallActiveTable.setStatus(_A)
_H3cVoiceCallActiveEntry_Object=MibTableRow
h3cVoiceCallActiveEntry=_H3cVoiceCallActiveEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1))
h3cVoiceCallActiveEntry.setIndexNames((0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:h3cVoiceCallActiveEntry.setStatus(_A)
_H3cVoCallActiveConnectionId_Type=H3cGUid
_H3cVoCallActiveConnectionId_Object=MibTableColumn
h3cVoCallActiveConnectionId=_H3cVoCallActiveConnectionId_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,1),_H3cVoCallActiveConnectionId_Type())
h3cVoCallActiveConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveConnectionId.setStatus(_A)
_H3cVoCallActiveTxDuration_Type=Gauge32
_H3cVoCallActiveTxDuration_Object=MibTableColumn
h3cVoCallActiveTxDuration=_H3cVoCallActiveTxDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,2),_H3cVoCallActiveTxDuration_Type())
h3cVoCallActiveTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveTxDuration.setStatus(_A)
_H3cVoCallActiveVoiceTxDuration_Type=Gauge32
_H3cVoCallActiveVoiceTxDuration_Object=MibTableColumn
h3cVoCallActiveVoiceTxDuration=_H3cVoCallActiveVoiceTxDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,3),_H3cVoCallActiveVoiceTxDuration_Type())
h3cVoCallActiveVoiceTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveVoiceTxDuration.setStatus(_A)
_H3cVoCallActiveFaxTxDuration_Type=Gauge32
_H3cVoCallActiveFaxTxDuration_Object=MibTableColumn
h3cVoCallActiveFaxTxDuration=_H3cVoCallActiveFaxTxDuration_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,4),_H3cVoCallActiveFaxTxDuration_Type())
h3cVoCallActiveFaxTxDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveFaxTxDuration.setStatus(_A)
_H3cVoCallActiveCoderType_Type=H3cCodecType
_H3cVoCallActiveCoderType_Object=MibTableColumn
h3cVoCallActiveCoderType=_H3cVoCallActiveCoderType_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,5),_H3cVoCallActiveCoderType_Type())
h3cVoCallActiveCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveCoderType.setStatus(_A)
_H3cVoCallActiveImgPageCount_Type=Gauge32
_H3cVoCallActiveImgPageCount_Object=MibTableColumn
h3cVoCallActiveImgPageCount=_H3cVoCallActiveImgPageCount_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,1,1,6),_H3cVoCallActiveImgPageCount_Type())
h3cVoCallActiveImgPageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveImgPageCount.setStatus(_A)
_H3cVoiceVoIPCallActiveTable_Object=MibTable
h3cVoiceVoIPCallActiveTable=_H3cVoiceVoIPCallActiveTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2))
if mibBuilder.loadTexts:h3cVoiceVoIPCallActiveTable.setStatus(_A)
_H3cVoiceVoIPCallActiveEntry_Object=MibTableRow
h3cVoiceVoIPCallActiveEntry=_H3cVoiceVoIPCallActiveEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1))
h3cVoiceVoIPCallActiveEntry.setIndexNames((0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:h3cVoiceVoIPCallActiveEntry.setStatus(_A)
_H3cVoVoIPCallActiveConnectionId_Type=H3cGUid
_H3cVoVoIPCallActiveConnectionId_Object=MibTableColumn
h3cVoVoIPCallActiveConnectionId=_H3cVoVoIPCallActiveConnectionId_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,1),_H3cVoVoIPCallActiveConnectionId_Type())
h3cVoVoIPCallActiveConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveConnectionId.setStatus(_A)
_H3cVoVoIPCallActiveRemSigIPType_Type=InetAddressType
_H3cVoVoIPCallActiveRemSigIPType_Object=MibTableColumn
h3cVoVoIPCallActiveRemSigIPType=_H3cVoVoIPCallActiveRemSigIPType_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,2),_H3cVoVoIPCallActiveRemSigIPType_Type())
h3cVoVoIPCallActiveRemSigIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemSigIPType.setStatus(_A)
_H3cVoVoIPCallActiveRemSigIPAddr_Type=InetAddress
_H3cVoVoIPCallActiveRemSigIPAddr_Object=MibTableColumn
h3cVoVoIPCallActiveRemSigIPAddr=_H3cVoVoIPCallActiveRemSigIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,3),_H3cVoVoIPCallActiveRemSigIPAddr_Type())
h3cVoVoIPCallActiveRemSigIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemSigIPAddr.setStatus(_A)
class _H3cVoVoIPCallActiveRemSigPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cVoVoIPCallActiveRemSigPort_Type.__name__=_D
_H3cVoVoIPCallActiveRemSigPort_Object=MibTableColumn
h3cVoVoIPCallActiveRemSigPort=_H3cVoVoIPCallActiveRemSigPort_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,4),_H3cVoVoIPCallActiveRemSigPort_Type())
h3cVoVoIPCallActiveRemSigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemSigPort.setStatus(_A)
_H3cVoVoIPCallActiveRemMedIPType_Type=InetAddressType
_H3cVoVoIPCallActiveRemMedIPType_Object=MibTableColumn
h3cVoVoIPCallActiveRemMedIPType=_H3cVoVoIPCallActiveRemMedIPType_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,5),_H3cVoVoIPCallActiveRemMedIPType_Type())
h3cVoVoIPCallActiveRemMedIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemMedIPType.setStatus(_A)
_H3cVoVoIPCallActiveRemMedIPAddr_Type=InetAddress
_H3cVoVoIPCallActiveRemMedIPAddr_Object=MibTableColumn
h3cVoVoIPCallActiveRemMedIPAddr=_H3cVoVoIPCallActiveRemMedIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,6),_H3cVoVoIPCallActiveRemMedIPAddr_Type())
h3cVoVoIPCallActiveRemMedIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemMedIPAddr.setStatus(_A)
class _H3cVoVoIPCallActiveRemMedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cVoVoIPCallActiveRemMedPort_Type.__name__=_D
_H3cVoVoIPCallActiveRemMedPort_Object=MibTableColumn
h3cVoVoIPCallActiveRemMedPort=_H3cVoVoIPCallActiveRemMedPort_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,7),_H3cVoVoIPCallActiveRemMedPort_Type())
h3cVoVoIPCallActiveRemMedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveRemMedPort.setStatus(_A)
class _H3cVoVoIPCallActiveSessProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('h323',2),('sip',3)))
_H3cVoVoIPCallActiveSessProtocol_Type.__name__=_D
_H3cVoVoIPCallActiveSessProtocol_Object=MibTableColumn
h3cVoVoIPCallActiveSessProtocol=_H3cVoVoIPCallActiveSessProtocol_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,8),_H3cVoVoIPCallActiveSessProtocol_Type())
h3cVoVoIPCallActiveSessProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveSessProtocol.setStatus(_A)
_H3cVoVoIPCallActiveCoderType_Type=H3cCodecType
_H3cVoVoIPCallActiveCoderType_Object=MibTableColumn
h3cVoVoIPCallActiveCoderType=_H3cVoVoIPCallActiveCoderType_Object((1,3,6,1,4,1,43,45,1,10,2,39,15,1,2,1,9),_H3cVoVoIPCallActiveCoderType_Type())
h3cVoVoIPCallActiveCoderType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoVoIPCallActiveCoderType.setStatus(_A)
mibBuilder.exportSymbols('A3COM-HUAWEI-VOICE-CALL-ACTIVE-MIB',**{'H3cGUid':H3cGUid,'h3cVoCallActive':h3cVoCallActive,'h3cVoiceCallActiveObjects':h3cVoiceCallActiveObjects,'h3cVoiceCallActiveTable':h3cVoiceCallActiveTable,'h3cVoiceCallActiveEntry':h3cVoiceCallActiveEntry,'h3cVoCallActiveConnectionId':h3cVoCallActiveConnectionId,'h3cVoCallActiveTxDuration':h3cVoCallActiveTxDuration,'h3cVoCallActiveVoiceTxDuration':h3cVoCallActiveVoiceTxDuration,'h3cVoCallActiveFaxTxDuration':h3cVoCallActiveFaxTxDuration,'h3cVoCallActiveCoderType':h3cVoCallActiveCoderType,'h3cVoCallActiveImgPageCount':h3cVoCallActiveImgPageCount,'h3cVoiceVoIPCallActiveTable':h3cVoiceVoIPCallActiveTable,'h3cVoiceVoIPCallActiveEntry':h3cVoiceVoIPCallActiveEntry,'h3cVoVoIPCallActiveConnectionId':h3cVoVoIPCallActiveConnectionId,'h3cVoVoIPCallActiveRemSigIPType':h3cVoVoIPCallActiveRemSigIPType,'h3cVoVoIPCallActiveRemSigIPAddr':h3cVoVoIPCallActiveRemSigIPAddr,'h3cVoVoIPCallActiveRemSigPort':h3cVoVoIPCallActiveRemSigPort,'h3cVoVoIPCallActiveRemMedIPType':h3cVoVoIPCallActiveRemMedIPType,'h3cVoVoIPCallActiveRemMedIPAddr':h3cVoVoIPCallActiveRemMedIPAddr,'h3cVoVoIPCallActiveRemMedPort':h3cVoVoIPCallActiveRemMedPort,'h3cVoVoIPCallActiveSessProtocol':h3cVoVoIPCallActiveSessProtocol,'h3cVoVoIPCallActiveCoderType':h3cVoVoIPCallActiveCoderType})