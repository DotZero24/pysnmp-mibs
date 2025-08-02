_M='read-only'
_L='hpnicfVoVoIPEntityCfgIndex'
_K='hpnicfVoPOTSEntityConfigIndex'
_J='hpnicfVoEntityCfgIndex'
_I='read-create'
_H='unknown'
_G='hpnicfVoEntityIndex'
_F='not-accessible'
_E='OctetString'
_D='HPN-ICF-VOICE-DIAL-CONTROL-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AbsoluteCounter32,=mibBuilder.importSymbols('DIAL-CONTROL-MIB','AbsoluteCounter32')
hpnicfVoice,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfVoice')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfVoiceEntityControl=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,14))
if mibBuilder.loadTexts:hpnicfVoiceEntityControl.setRevisions(('2009-04-16 00:00',))
class HpnicfCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('g711a',1),('g711u',2),('g723r53',3),('g723r63',4),('g729r8',5),('g729a',6),('g726r16',7),('g726r24',8),('g726r32',9),('g726r40',10),(_H,11),('g729br8',12)))
class HpnicfOutBandMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('voice',1),('h245AlphaNumeric',2),('h225',3),('sip',4),('nte',5),('vofr',6)))
class HpnicfFaxProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t38',1),('standardt38',2),('pcmG711alaw',3),('pcmG711ulaw',4)))
class HpnicfFaxBaudrateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disable',1),('voice',2),('b2400',3),('b4800',4),('b9600',5),('b14400',6)))
class HpnicfFaxTrainMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('ppp',2)))
class HpnicfRegisterdStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('offline',2),('online',3),('login',4),('logout',5)))
_HpnicfVoEntityObjects_ObjectIdentity=ObjectIdentity
hpnicfVoEntityObjects=_HpnicfVoEntityObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1))
_HpnicfVoEntityCreateTable_Object=MibTable
hpnicfVoEntityCreateTable=_HpnicfVoEntityCreateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,1))
if mibBuilder.loadTexts:hpnicfVoEntityCreateTable.setStatus(_A)
_HpnicfVoEntityCreateEntry_Object=MibTableRow
hpnicfVoEntityCreateEntry=_HpnicfVoEntityCreateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,1,1))
hpnicfVoEntityCreateEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfVoEntityCreateEntry.setStatus(_A)
class _HpnicfVoEntityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfVoEntityIndex_Type.__name__=_C
_HpnicfVoEntityIndex_Object=MibTableColumn
hpnicfVoEntityIndex=_HpnicfVoEntityIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,1,1,1),_HpnicfVoEntityIndex_Type())
hpnicfVoEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVoEntityIndex.setStatus(_A)
class _HpnicfVoEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pots',1),('voip',2),('vofr',3)))
_HpnicfVoEntityType_Type.__name__=_C
_HpnicfVoEntityType_Object=MibTableColumn
hpnicfVoEntityType=_HpnicfVoEntityType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,1,1,2),_HpnicfVoEntityType_Type())
hpnicfVoEntityType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfVoEntityType.setStatus(_A)
_HpnicfVoEntityRowStatus_Type=RowStatus
_HpnicfVoEntityRowStatus_Object=MibTableColumn
hpnicfVoEntityRowStatus=_HpnicfVoEntityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,1,1,3),_HpnicfVoEntityRowStatus_Type())
hpnicfVoEntityRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfVoEntityRowStatus.setStatus(_A)
_HpnicfVoEntityCommonConfigTable_Object=MibTable
hpnicfVoEntityCommonConfigTable=_HpnicfVoEntityCommonConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2))
if mibBuilder.loadTexts:hpnicfVoEntityCommonConfigTable.setStatus(_A)
_HpnicfVoEntityCommonConfigEntry_Object=MibTableRow
hpnicfVoEntityCommonConfigEntry=_HpnicfVoEntityCommonConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1))
hpnicfVoEntityCommonConfigEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfVoEntityCommonConfigEntry.setStatus(_A)
class _HpnicfVoEntityCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfVoEntityCfgIndex_Type.__name__=_C
_HpnicfVoEntityCfgIndex_Object=MibTableColumn
hpnicfVoEntityCfgIndex=_HpnicfVoEntityCfgIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,1),_HpnicfVoEntityCfgIndex_Type())
hpnicfVoEntityCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVoEntityCfgIndex.setStatus(_A)
_HpnicfVoEntityCfgCodec1st_Type=HpnicfCodecType
_HpnicfVoEntityCfgCodec1st_Object=MibTableColumn
hpnicfVoEntityCfgCodec1st=_HpnicfVoEntityCfgCodec1st_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,2),_HpnicfVoEntityCfgCodec1st_Type())
hpnicfVoEntityCfgCodec1st.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgCodec1st.setStatus(_A)
_HpnicfVoEntityCfgCodec2nd_Type=HpnicfCodecType
_HpnicfVoEntityCfgCodec2nd_Object=MibTableColumn
hpnicfVoEntityCfgCodec2nd=_HpnicfVoEntityCfgCodec2nd_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,3),_HpnicfVoEntityCfgCodec2nd_Type())
hpnicfVoEntityCfgCodec2nd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgCodec2nd.setStatus(_A)
_HpnicfVoEntityCfgCodec3rd_Type=HpnicfCodecType
_HpnicfVoEntityCfgCodec3rd_Object=MibTableColumn
hpnicfVoEntityCfgCodec3rd=_HpnicfVoEntityCfgCodec3rd_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,4),_HpnicfVoEntityCfgCodec3rd_Type())
hpnicfVoEntityCfgCodec3rd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgCodec3rd.setStatus(_A)
_HpnicfVoEntityCfgCodec4th_Type=HpnicfCodecType
_HpnicfVoEntityCfgCodec4th_Object=MibTableColumn
hpnicfVoEntityCfgCodec4th=_HpnicfVoEntityCfgCodec4th_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,5),_HpnicfVoEntityCfgCodec4th_Type())
hpnicfVoEntityCfgCodec4th.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgCodec4th.setStatus(_A)
class _HpnicfVoEntityCfgDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfVoEntityCfgDSCP_Type.__name__=_C
_HpnicfVoEntityCfgDSCP_Object=MibTableColumn
hpnicfVoEntityCfgDSCP=_HpnicfVoEntityCfgDSCP_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,6),_HpnicfVoEntityCfgDSCP_Type())
hpnicfVoEntityCfgDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgDSCP.setStatus(_A)
_HpnicfVoEntityCfgVADEnable_Type=TruthValue
_HpnicfVoEntityCfgVADEnable_Object=MibTableColumn
hpnicfVoEntityCfgVADEnable=_HpnicfVoEntityCfgVADEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,7),_HpnicfVoEntityCfgVADEnable_Type())
hpnicfVoEntityCfgVADEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgVADEnable.setStatus(_A)
_HpnicfVoEntityCfgOutbandMode_Type=HpnicfOutBandMode
_HpnicfVoEntityCfgOutbandMode_Object=MibTableColumn
hpnicfVoEntityCfgOutbandMode=_HpnicfVoEntityCfgOutbandMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,8),_HpnicfVoEntityCfgOutbandMode_Type())
hpnicfVoEntityCfgOutbandMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgOutbandMode.setStatus(_A)
class _HpnicfVoEntityCfgFaxLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,-3))
_HpnicfVoEntityCfgFaxLevel_Type.__name__=_C
_HpnicfVoEntityCfgFaxLevel_Object=MibTableColumn
hpnicfVoEntityCfgFaxLevel=_HpnicfVoEntityCfgFaxLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,9),_HpnicfVoEntityCfgFaxLevel_Type())
hpnicfVoEntityCfgFaxLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxLevel.setStatus(_A)
_HpnicfVoEntityCfgFaxBaudrate_Type=HpnicfFaxBaudrateType
_HpnicfVoEntityCfgFaxBaudrate_Object=MibTableColumn
hpnicfVoEntityCfgFaxBaudrate=_HpnicfVoEntityCfgFaxBaudrate_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,10),_HpnicfVoEntityCfgFaxBaudrate_Type())
hpnicfVoEntityCfgFaxBaudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxBaudrate.setStatus(_A)
class _HpnicfVoEntityCfgFaxLocalTrainPara_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfVoEntityCfgFaxLocalTrainPara_Type.__name__=_C
_HpnicfVoEntityCfgFaxLocalTrainPara_Object=MibTableColumn
hpnicfVoEntityCfgFaxLocalTrainPara=_HpnicfVoEntityCfgFaxLocalTrainPara_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,11),_HpnicfVoEntityCfgFaxLocalTrainPara_Type())
hpnicfVoEntityCfgFaxLocalTrainPara.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxLocalTrainPara.setStatus(_A)
_HpnicfVoEntityCfgFaxProtocol_Type=HpnicfFaxProtocolType
_HpnicfVoEntityCfgFaxProtocol_Object=MibTableColumn
hpnicfVoEntityCfgFaxProtocol=_HpnicfVoEntityCfgFaxProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,12),_HpnicfVoEntityCfgFaxProtocol_Type())
hpnicfVoEntityCfgFaxProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxProtocol.setStatus(_A)
class _HpnicfVoEntityCfgFaxHRPackNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfVoEntityCfgFaxHRPackNum_Type.__name__=_C
_HpnicfVoEntityCfgFaxHRPackNum_Object=MibTableColumn
hpnicfVoEntityCfgFaxHRPackNum=_HpnicfVoEntityCfgFaxHRPackNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,13),_HpnicfVoEntityCfgFaxHRPackNum_Type())
hpnicfVoEntityCfgFaxHRPackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxHRPackNum.setStatus(_A)
class _HpnicfVoEntityCfgFaxLRPackNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HpnicfVoEntityCfgFaxLRPackNum_Type.__name__=_C
_HpnicfVoEntityCfgFaxLRPackNum_Object=MibTableColumn
hpnicfVoEntityCfgFaxLRPackNum=_HpnicfVoEntityCfgFaxLRPackNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,14),_HpnicfVoEntityCfgFaxLRPackNum_Type())
hpnicfVoEntityCfgFaxLRPackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxLRPackNum.setStatus(_A)
_HpnicfVoEntityCfgFaxSendNSFEnable_Type=TruthValue
_HpnicfVoEntityCfgFaxSendNSFEnable_Object=MibTableColumn
hpnicfVoEntityCfgFaxSendNSFEnable=_HpnicfVoEntityCfgFaxSendNSFEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,15),_HpnicfVoEntityCfgFaxSendNSFEnable_Type())
hpnicfVoEntityCfgFaxSendNSFEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxSendNSFEnable.setStatus(_A)
_HpnicfVoEntityCfgFaxTrainMode_Type=HpnicfFaxTrainMode
_HpnicfVoEntityCfgFaxTrainMode_Object=MibTableColumn
hpnicfVoEntityCfgFaxTrainMode=_HpnicfVoEntityCfgFaxTrainMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,16),_HpnicfVoEntityCfgFaxTrainMode_Type())
hpnicfVoEntityCfgFaxTrainMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxTrainMode.setStatus(_A)
_HpnicfVoEntityCfgFaxEcm_Type=TruthValue
_HpnicfVoEntityCfgFaxEcm_Object=MibTableColumn
hpnicfVoEntityCfgFaxEcm=_HpnicfVoEntityCfgFaxEcm_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,17),_HpnicfVoEntityCfgFaxEcm_Type())
hpnicfVoEntityCfgFaxEcm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgFaxEcm.setStatus(_A)
class _HpnicfVoEntityCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HpnicfVoEntityCfgPriority_Type.__name__=_C
_HpnicfVoEntityCfgPriority_Object=MibTableColumn
hpnicfVoEntityCfgPriority=_HpnicfVoEntityCfgPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,18),_HpnicfVoEntityCfgPriority_Type())
hpnicfVoEntityCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgPriority.setStatus(_A)
class _HpnicfVoEntityCfgDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnicfVoEntityCfgDescription_Type.__name__=_E
_HpnicfVoEntityCfgDescription_Object=MibTableColumn
hpnicfVoEntityCfgDescription=_HpnicfVoEntityCfgDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,2,1,19),_HpnicfVoEntityCfgDescription_Type())
hpnicfVoEntityCfgDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityCfgDescription.setStatus(_A)
_HpnicfVoPOTSEntityConfigTable_Object=MibTable
hpnicfVoPOTSEntityConfigTable=_HpnicfVoPOTSEntityConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3))
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigTable.setStatus(_A)
_HpnicfVoPOTSEntityConfigEntry_Object=MibTableRow
hpnicfVoPOTSEntityConfigEntry=_HpnicfVoPOTSEntityConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3,1))
hpnicfVoPOTSEntityConfigEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigEntry.setStatus(_A)
class _HpnicfVoPOTSEntityConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfVoPOTSEntityConfigIndex_Type.__name__=_C
_HpnicfVoPOTSEntityConfigIndex_Object=MibTableColumn
hpnicfVoPOTSEntityConfigIndex=_HpnicfVoPOTSEntityConfigIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3,1,1),_HpnicfVoPOTSEntityConfigIndex_Type())
hpnicfVoPOTSEntityConfigIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigIndex.setStatus(_A)
class _HpnicfVoPOTSEntityConfigPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfVoPOTSEntityConfigPrefix_Type.__name__=_E
_HpnicfVoPOTSEntityConfigPrefix_Object=MibTableColumn
hpnicfVoPOTSEntityConfigPrefix=_HpnicfVoPOTSEntityConfigPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3,1,2),_HpnicfVoPOTSEntityConfigPrefix_Type())
hpnicfVoPOTSEntityConfigPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigPrefix.setStatus(_A)
_HpnicfVoPOTSEntityConfigSubLine_Type=OctetString
_HpnicfVoPOTSEntityConfigSubLine_Object=MibTableColumn
hpnicfVoPOTSEntityConfigSubLine=_HpnicfVoPOTSEntityConfigSubLine_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3,1,3),_HpnicfVoPOTSEntityConfigSubLine_Type())
hpnicfVoPOTSEntityConfigSubLine.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigSubLine.setStatus(_A)
class _HpnicfVoPOTSEntityConfigSendNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31),ValueRangeConstraint(65534,65534),ValueRangeConstraint(65535,65535))
_HpnicfVoPOTSEntityConfigSendNum_Type.__name__=_C
_HpnicfVoPOTSEntityConfigSendNum_Object=MibTableColumn
hpnicfVoPOTSEntityConfigSendNum=_HpnicfVoPOTSEntityConfigSendNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,3,1,4),_HpnicfVoPOTSEntityConfigSendNum_Type())
hpnicfVoPOTSEntityConfigSendNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoPOTSEntityConfigSendNum.setStatus(_A)
_HpnicfVoVoIPEntityConfigTable_Object=MibTable
hpnicfVoVoIPEntityConfigTable=_HpnicfVoVoIPEntityConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4))
if mibBuilder.loadTexts:hpnicfVoVoIPEntityConfigTable.setStatus(_A)
_HpnicfVoVoIPEntityConfigEntry_Object=MibTableRow
hpnicfVoVoIPEntityConfigEntry=_HpnicfVoVoIPEntityConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4,1))
hpnicfVoVoIPEntityConfigEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:hpnicfVoVoIPEntityConfigEntry.setStatus(_A)
class _HpnicfVoVoIPEntityCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfVoVoIPEntityCfgIndex_Type.__name__=_C
_HpnicfVoVoIPEntityCfgIndex_Object=MibTableColumn
hpnicfVoVoIPEntityCfgIndex=_HpnicfVoVoIPEntityCfgIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4,1,1),_HpnicfVoVoIPEntityCfgIndex_Type())
hpnicfVoVoIPEntityCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfVoVoIPEntityCfgIndex.setStatus(_A)
class _HpnicfVoVoIPEntityCfgTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('ras',2),('h323IpAddress',3),('sipIpAddress',4),('sipProxy',5)))
_HpnicfVoVoIPEntityCfgTargetType_Type.__name__=_C
_HpnicfVoVoIPEntityCfgTargetType_Object=MibTableColumn
hpnicfVoVoIPEntityCfgTargetType=_HpnicfVoVoIPEntityCfgTargetType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4,1,2),_HpnicfVoVoIPEntityCfgTargetType_Type())
hpnicfVoVoIPEntityCfgTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPEntityCfgTargetType.setStatus(_A)
_HpnicfVoVoIPEntityCfgTargetAddrType_Type=InetAddressType
_HpnicfVoVoIPEntityCfgTargetAddrType_Object=MibTableColumn
hpnicfVoVoIPEntityCfgTargetAddrType=_HpnicfVoVoIPEntityCfgTargetAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4,1,3),_HpnicfVoVoIPEntityCfgTargetAddrType_Type())
hpnicfVoVoIPEntityCfgTargetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPEntityCfgTargetAddrType.setStatus(_A)
_HpnicfVoVoIPEntityCfgTargetAddr_Type=InetAddress
_HpnicfVoVoIPEntityCfgTargetAddr_Object=MibTableColumn
hpnicfVoVoIPEntityCfgTargetAddr=_HpnicfVoVoIPEntityCfgTargetAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,4,1,4),_HpnicfVoVoIPEntityCfgTargetAddr_Type())
hpnicfVoVoIPEntityCfgTargetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoVoIPEntityCfgTargetAddr.setStatus(_A)
_HpnicfVoEntityNumberTable_Object=MibTable
hpnicfVoEntityNumberTable=_HpnicfVoEntityNumberTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5))
if mibBuilder.loadTexts:hpnicfVoEntityNumberTable.setStatus(_A)
_HpnicfVoEntityNumberEntry_Object=MibTableRow
hpnicfVoEntityNumberEntry=_HpnicfVoEntityNumberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1))
hpnicfVoEntityNumberEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfVoEntityNumberEntry.setStatus(_A)
class _HpnicfVoEntityNumberAuthUser_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfVoEntityNumberAuthUser_Type.__name__=_E
_HpnicfVoEntityNumberAuthUser_Object=MibTableColumn
hpnicfVoEntityNumberAuthUser=_HpnicfVoEntityNumberAuthUser_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1,1),_HpnicfVoEntityNumberAuthUser_Type())
hpnicfVoEntityNumberAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityNumberAuthUser.setStatus(_A)
_HpnicfVoEntityNumberPasswordType_Type=Integer32
_HpnicfVoEntityNumberPasswordType_Object=MibTableColumn
hpnicfVoEntityNumberPasswordType=_HpnicfVoEntityNumberPasswordType_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1,2),_HpnicfVoEntityNumberPasswordType_Type())
hpnicfVoEntityNumberPasswordType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityNumberPasswordType.setStatus(_A)
class _HpnicfVoEntityNumberPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16),ValueSizeConstraint(24,24))
_HpnicfVoEntityNumberPassword_Type.__name__=_E
_HpnicfVoEntityNumberPassword_Object=MibTableColumn
hpnicfVoEntityNumberPassword=_HpnicfVoEntityNumberPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1,3),_HpnicfVoEntityNumberPassword_Type())
hpnicfVoEntityNumberPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoEntityNumberPassword.setStatus(_A)
_HpnicfVoEntityNumberStatus_Type=HpnicfRegisterdStatus
_HpnicfVoEntityNumberStatus_Object=MibTableColumn
hpnicfVoEntityNumberStatus=_HpnicfVoEntityNumberStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1,4),_HpnicfVoEntityNumberStatus_Type())
hpnicfVoEntityNumberStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfVoEntityNumberStatus.setStatus(_A)
_HpnicfVoEntityNumberExpires_Type=Integer32
_HpnicfVoEntityNumberExpires_Object=MibTableColumn
hpnicfVoEntityNumberExpires=_HpnicfVoEntityNumberExpires_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,14,1,5,1,5),_HpnicfVoEntityNumberExpires_Type())
hpnicfVoEntityNumberExpires.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfVoEntityNumberExpires.setStatus(_A)
if mibBuilder.loadTexts:hpnicfVoEntityNumberExpires.setUnits('seconds')
mibBuilder.exportSymbols(_D,**{'HpnicfCodecType':HpnicfCodecType,'HpnicfOutBandMode':HpnicfOutBandMode,'HpnicfFaxProtocolType':HpnicfFaxProtocolType,'HpnicfFaxBaudrateType':HpnicfFaxBaudrateType,'HpnicfFaxTrainMode':HpnicfFaxTrainMode,'HpnicfRegisterdStatus':HpnicfRegisterdStatus,'hpnicfVoiceEntityControl':hpnicfVoiceEntityControl,'hpnicfVoEntityObjects':hpnicfVoEntityObjects,'hpnicfVoEntityCreateTable':hpnicfVoEntityCreateTable,'hpnicfVoEntityCreateEntry':hpnicfVoEntityCreateEntry,_G:hpnicfVoEntityIndex,'hpnicfVoEntityType':hpnicfVoEntityType,'hpnicfVoEntityRowStatus':hpnicfVoEntityRowStatus,'hpnicfVoEntityCommonConfigTable':hpnicfVoEntityCommonConfigTable,'hpnicfVoEntityCommonConfigEntry':hpnicfVoEntityCommonConfigEntry,_J:hpnicfVoEntityCfgIndex,'hpnicfVoEntityCfgCodec1st':hpnicfVoEntityCfgCodec1st,'hpnicfVoEntityCfgCodec2nd':hpnicfVoEntityCfgCodec2nd,'hpnicfVoEntityCfgCodec3rd':hpnicfVoEntityCfgCodec3rd,'hpnicfVoEntityCfgCodec4th':hpnicfVoEntityCfgCodec4th,'hpnicfVoEntityCfgDSCP':hpnicfVoEntityCfgDSCP,'hpnicfVoEntityCfgVADEnable':hpnicfVoEntityCfgVADEnable,'hpnicfVoEntityCfgOutbandMode':hpnicfVoEntityCfgOutbandMode,'hpnicfVoEntityCfgFaxLevel':hpnicfVoEntityCfgFaxLevel,'hpnicfVoEntityCfgFaxBaudrate':hpnicfVoEntityCfgFaxBaudrate,'hpnicfVoEntityCfgFaxLocalTrainPara':hpnicfVoEntityCfgFaxLocalTrainPara,'hpnicfVoEntityCfgFaxProtocol':hpnicfVoEntityCfgFaxProtocol,'hpnicfVoEntityCfgFaxHRPackNum':hpnicfVoEntityCfgFaxHRPackNum,'hpnicfVoEntityCfgFaxLRPackNum':hpnicfVoEntityCfgFaxLRPackNum,'hpnicfVoEntityCfgFaxSendNSFEnable':hpnicfVoEntityCfgFaxSendNSFEnable,'hpnicfVoEntityCfgFaxTrainMode':hpnicfVoEntityCfgFaxTrainMode,'hpnicfVoEntityCfgFaxEcm':hpnicfVoEntityCfgFaxEcm,'hpnicfVoEntityCfgPriority':hpnicfVoEntityCfgPriority,'hpnicfVoEntityCfgDescription':hpnicfVoEntityCfgDescription,'hpnicfVoPOTSEntityConfigTable':hpnicfVoPOTSEntityConfigTable,'hpnicfVoPOTSEntityConfigEntry':hpnicfVoPOTSEntityConfigEntry,_K:hpnicfVoPOTSEntityConfigIndex,'hpnicfVoPOTSEntityConfigPrefix':hpnicfVoPOTSEntityConfigPrefix,'hpnicfVoPOTSEntityConfigSubLine':hpnicfVoPOTSEntityConfigSubLine,'hpnicfVoPOTSEntityConfigSendNum':hpnicfVoPOTSEntityConfigSendNum,'hpnicfVoVoIPEntityConfigTable':hpnicfVoVoIPEntityConfigTable,'hpnicfVoVoIPEntityConfigEntry':hpnicfVoVoIPEntityConfigEntry,_L:hpnicfVoVoIPEntityCfgIndex,'hpnicfVoVoIPEntityCfgTargetType':hpnicfVoVoIPEntityCfgTargetType,'hpnicfVoVoIPEntityCfgTargetAddrType':hpnicfVoVoIPEntityCfgTargetAddrType,'hpnicfVoVoIPEntityCfgTargetAddr':hpnicfVoVoIPEntityCfgTargetAddr,'hpnicfVoEntityNumberTable':hpnicfVoEntityNumberTable,'hpnicfVoEntityNumberEntry':hpnicfVoEntityNumberEntry,'hpnicfVoEntityNumberAuthUser':hpnicfVoEntityNumberAuthUser,'hpnicfVoEntityNumberPasswordType':hpnicfVoEntityNumberPasswordType,'hpnicfVoEntityNumberPassword':hpnicfVoEntityNumberPassword,'hpnicfVoEntityNumberStatus':hpnicfVoEntityNumberStatus,'hpnicfVoEntityNumberExpires':hpnicfVoEntityNumberExpires})