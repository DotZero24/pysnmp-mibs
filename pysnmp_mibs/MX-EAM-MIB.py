_V='master'
_U='physicalLinkInterfaceName'
_T='physicalLinkInfoInterfaceName'
_S='bearerChannelInfoIndex'
_R='eamToneVariantsInterfaceName'
_Q='eamLinkTimerVariantsInterfaceName'
_P='eamDigitTimerVariantsInterfaceName'
_O='eamTimerVariantsInterfaceName'
_N='%dnis%t'
_M='eamSignalingVariantsInterfaceName'
_L='eamName'
_K='none'
_J='OctetString'
_I='resetSpecific'
_H='noOp'
_G='Unsigned32'
_F='MX-EAM-MIB'
_E='MxEnableState'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_E,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eamMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880))
_EamMIBObjects_ObjectIdentity=ObjectIdentity
eamMIBObjects=_EamMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1))
_EamGroup_ObjectIdentity=ObjectIdentity
eamGroup=_EamGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100))
_EamTable_Object=MibTable
eamTable=_EamTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100))
if mibBuilder.loadTexts:eamTable.setStatus(_A)
_EamEntry_Object=MibTableRow
eamEntry=_EamEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1))
eamEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:eamEntry.setStatus(_A)
_EamName_Type=OctetString
_EamName_Object=MibTableColumn
eamName=_EamName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,100),_EamName_Type())
eamName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamName.setStatus(_A)
class _EamChannelRange_Type(OctetString):defaultValue=OctetString('1-24');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_EamChannelRange_Type.__name__=_J
_EamChannelRange_Object=MibTableColumn
eamChannelRange=_EamChannelRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,200),_EamChannelRange_Type())
eamChannelRange.setMaxAccess(_B)
if mibBuilder.loadTexts:eamChannelRange.setStatus(_A)
class _EamChannelAllocationStrategy_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('ascending',100),('descending',200),('roundRobinAscending',300),('roundRobinDescending',400)))
_EamChannelAllocationStrategy_Type.__name__=_C
_EamChannelAllocationStrategy_Object=MibTableColumn
eamChannelAllocationStrategy=_EamChannelAllocationStrategy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,300),_EamChannelAllocationStrategy_Type())
eamChannelAllocationStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:eamChannelAllocationStrategy.setStatus(_A)
class _EamMaxActiveCalls_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_EamMaxActiveCalls_Type.__name__=_G
_EamMaxActiveCalls_Object=MibTableColumn
eamMaxActiveCalls=_EamMaxActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,400),_EamMaxActiveCalls_Type())
eamMaxActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:eamMaxActiveCalls.setStatus(_A)
class _EamEncodingScheme_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('g711alaw',100),('g711ulaw',200)))
_EamEncodingScheme_Type.__name__=_C
_EamEncodingScheme_Object=MibTableColumn
eamEncodingScheme=_EamEncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,500),_EamEncodingScheme_Type())
eamEncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:eamEncodingScheme.setStatus(_A)
class _EamSignalingType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('winkStart',100),('immediateStart',200),('fgb',300),('fgd',400)))
_EamSignalingType_Type.__name__=_C
_EamSignalingType_Object=MibTableColumn
eamSignalingType=_EamSignalingType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,600),_EamSignalingType_Type())
eamSignalingType.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingType.setStatus(_A)
class _EamDigitAttenuation_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_EamDigitAttenuation_Type.__name__=_G
_EamDigitAttenuation_Object=MibTableColumn
eamDigitAttenuation=_EamDigitAttenuation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,100,1,700),_EamDigitAttenuation_Type())
eamDigitAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:eamDigitAttenuation.setStatus(_A)
_EamSignalingVariantsTable_Object=MibTable
eamSignalingVariantsTable=_EamSignalingVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200))
if mibBuilder.loadTexts:eamSignalingVariantsTable.setStatus(_A)
_EamSignalingVariantsEntry_Object=MibTableRow
eamSignalingVariantsEntry=_EamSignalingVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1))
eamSignalingVariantsEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:eamSignalingVariantsEntry.setStatus(_A)
_EamSignalingVariantsInterfaceName_Type=OctetString
_EamSignalingVariantsInterfaceName_Object=MibTableColumn
eamSignalingVariantsInterfaceName=_EamSignalingVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,100),_EamSignalingVariantsInterfaceName_Type())
eamSignalingVariantsInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamSignalingVariantsInterfaceName.setStatus(_A)
class _EamSignalingVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_EamSignalingVariantsOverrideDefault_Type.__name__=_E
_EamSignalingVariantsOverrideDefault_Object=MibTableColumn
eamSignalingVariantsOverrideDefault=_EamSignalingVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,200),_EamSignalingVariantsOverrideDefault_Type())
eamSignalingVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsOverrideDefault.setStatus(_A)
class _EamSignalingVariantsBitsBCD_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_EamSignalingVariantsBitsBCD_Type.__name__=_C
_EamSignalingVariantsBitsBCD_Object=MibTableColumn
eamSignalingVariantsBitsBCD=_EamSignalingVariantsBitsBCD_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,300),_EamSignalingVariantsBitsBCD_Type())
eamSignalingVariantsBitsBCD.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsBitsBCD.setStatus(_A)
class _EamSignalingVariantsDnisLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_EamSignalingVariantsDnisLength_Type.__name__=_G
_EamSignalingVariantsDnisLength_Object=MibTableColumn
eamSignalingVariantsDnisLength=_EamSignalingVariantsDnisLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,400),_EamSignalingVariantsDnisLength_Type())
eamSignalingVariantsDnisLength.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsDnisLength.setStatus(_A)
class _EamSignalingVariantsAniLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_EamSignalingVariantsAniLength_Type.__name__=_G
_EamSignalingVariantsAniLength_Object=MibTableColumn
eamSignalingVariantsAniLength=_EamSignalingVariantsAniLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,500),_EamSignalingVariantsAniLength_Type())
eamSignalingVariantsAniLength.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsAniLength.setStatus(_A)
class _EamSignalingVariantsIncomingRegisterSignaling_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mfR1',100),('dtmf',200)))
_EamSignalingVariantsIncomingRegisterSignaling_Type.__name__=_C
_EamSignalingVariantsIncomingRegisterSignaling_Object=MibTableColumn
eamSignalingVariantsIncomingRegisterSignaling=_EamSignalingVariantsIncomingRegisterSignaling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,600),_EamSignalingVariantsIncomingRegisterSignaling_Type())
eamSignalingVariantsIncomingRegisterSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsIncomingRegisterSignaling.setStatus(_A)
class _EamSignalingVariantsOutgoingRegisterSignaling_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mfR1',100),('dtmf',200)))
_EamSignalingVariantsOutgoingRegisterSignaling_Type.__name__=_C
_EamSignalingVariantsOutgoingRegisterSignaling_Object=MibTableColumn
eamSignalingVariantsOutgoingRegisterSignaling=_EamSignalingVariantsOutgoingRegisterSignaling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,700),_EamSignalingVariantsOutgoingRegisterSignaling_Type())
eamSignalingVariantsOutgoingRegisterSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsOutgoingRegisterSignaling.setStatus(_A)
class _EamSignalingVariantsIncomingDialMap_Type(OctetString):defaultValue=OctetString(_N);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EamSignalingVariantsIncomingDialMap_Type.__name__=_J
_EamSignalingVariantsIncomingDialMap_Object=MibTableColumn
eamSignalingVariantsIncomingDialMap=_EamSignalingVariantsIncomingDialMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,800),_EamSignalingVariantsIncomingDialMap_Type())
eamSignalingVariantsIncomingDialMap.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsIncomingDialMap.setStatus(_A)
class _EamSignalingVariantsOutgoingDialMap_Type(OctetString):defaultValue=OctetString(_N);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EamSignalingVariantsOutgoingDialMap_Type.__name__=_J
_EamSignalingVariantsOutgoingDialMap_Object=MibTableColumn
eamSignalingVariantsOutgoingDialMap=_EamSignalingVariantsOutgoingDialMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,900),_EamSignalingVariantsOutgoingDialMap_Type())
eamSignalingVariantsOutgoingDialMap.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsOutgoingDialMap.setStatus(_A)
class _EamSignalingVariantsWaitWink_Type(MxEnableState):defaultValue=1
_EamSignalingVariantsWaitWink_Type.__name__=_E
_EamSignalingVariantsWaitWink_Object=MibTableColumn
eamSignalingVariantsWaitWink=_EamSignalingVariantsWaitWink_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,1000),_EamSignalingVariantsWaitWink_Type())
eamSignalingVariantsWaitWink.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsWaitWink.setStatus(_A)
class _EamSignalingVariantsWaitWinkAck_Type(MxEnableState):defaultValue=0
_EamSignalingVariantsWaitWinkAck_Type.__name__=_E
_EamSignalingVariantsWaitWinkAck_Object=MibTableColumn
eamSignalingVariantsWaitWinkAck=_EamSignalingVariantsWaitWinkAck_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,1100),_EamSignalingVariantsWaitWinkAck_Type())
eamSignalingVariantsWaitWinkAck.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsWaitWinkAck.setStatus(_A)
class _EamSignalingVariantsSendWink_Type(MxEnableState):defaultValue=1
_EamSignalingVariantsSendWink_Type.__name__=_E
_EamSignalingVariantsSendWink_Object=MibTableColumn
eamSignalingVariantsSendWink=_EamSignalingVariantsSendWink_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,1200),_EamSignalingVariantsSendWink_Type())
eamSignalingVariantsSendWink.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsSendWink.setStatus(_A)
class _EamSignalingVariantsSendWinkAck_Type(MxEnableState):defaultValue=0
_EamSignalingVariantsSendWinkAck_Type.__name__=_E
_EamSignalingVariantsSendWinkAck_Object=MibTableColumn
eamSignalingVariantsSendWinkAck=_EamSignalingVariantsSendWinkAck_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,1300),_EamSignalingVariantsSendWinkAck_Type())
eamSignalingVariantsSendWinkAck.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsSendWinkAck.setStatus(_A)
class _EamSignalingVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),(_I,10)))
_EamSignalingVariantsResetSpecific_Type.__name__=_C
_EamSignalingVariantsResetSpecific_Object=MibTableColumn
eamSignalingVariantsResetSpecific=_EamSignalingVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,200,1,2000),_EamSignalingVariantsResetSpecific_Type())
eamSignalingVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:eamSignalingVariantsResetSpecific.setStatus(_A)
_EamTimerVariantsTable_Object=MibTable
eamTimerVariantsTable=_EamTimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300))
if mibBuilder.loadTexts:eamTimerVariantsTable.setStatus(_A)
_EamTimerVariantsEntry_Object=MibTableRow
eamTimerVariantsEntry=_EamTimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1))
eamTimerVariantsEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:eamTimerVariantsEntry.setStatus(_A)
_EamTimerVariantsInterfaceName_Type=OctetString
_EamTimerVariantsInterfaceName_Object=MibTableColumn
eamTimerVariantsInterfaceName=_EamTimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,100),_EamTimerVariantsInterfaceName_Type())
eamTimerVariantsInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamTimerVariantsInterfaceName.setStatus(_A)
class _EamTimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_EamTimerVariantsOverrideDefault_Type.__name__=_E
_EamTimerVariantsOverrideDefault_Object=MibTableColumn
eamTimerVariantsOverrideDefault=_EamTimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,200),_EamTimerVariantsOverrideDefault_Type())
eamTimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsOverrideDefault.setStatus(_A)
class _EamTimerVariantsBwdWaitPreWinkTimeout_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_EamTimerVariantsBwdWaitPreWinkTimeout_Type.__name__=_C
_EamTimerVariantsBwdWaitPreWinkTimeout_Object=MibTableColumn
eamTimerVariantsBwdWaitPreWinkTimeout=_EamTimerVariantsBwdWaitPreWinkTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,300),_EamTimerVariantsBwdWaitPreWinkTimeout_Type())
eamTimerVariantsBwdWaitPreWinkTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsBwdWaitPreWinkTimeout.setStatus(_A)
class _EamTimerVariantsBwdSendWinkTimeout_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_EamTimerVariantsBwdSendWinkTimeout_Type.__name__=_C
_EamTimerVariantsBwdSendWinkTimeout_Object=MibTableColumn
eamTimerVariantsBwdSendWinkTimeout=_EamTimerVariantsBwdSendWinkTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,400),_EamTimerVariantsBwdSendWinkTimeout_Type())
eamTimerVariantsBwdSendWinkTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsBwdSendWinkTimeout.setStatus(_A)
class _EamTimerVariantsBwdWait1stDigitTimeout_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_EamTimerVariantsBwdWait1stDigitTimeout_Type.__name__=_C
_EamTimerVariantsBwdWait1stDigitTimeout_Object=MibTableColumn
eamTimerVariantsBwdWait1stDigitTimeout=_EamTimerVariantsBwdWait1stDigitTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,500),_EamTimerVariantsBwdWait1stDigitTimeout_Type())
eamTimerVariantsBwdWait1stDigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsBwdWait1stDigitTimeout.setStatus(_A)
class _EamTimerVariantsBwdClearBackwardTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_EamTimerVariantsBwdClearBackwardTimeout_Type.__name__=_C
_EamTimerVariantsBwdClearBackwardTimeout_Object=MibTableColumn
eamTimerVariantsBwdClearBackwardTimeout=_EamTimerVariantsBwdClearBackwardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,600),_EamTimerVariantsBwdClearBackwardTimeout_Type())
eamTimerVariantsBwdClearBackwardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsBwdClearBackwardTimeout.setStatus(_A)
class _EamTimerVariantsBwdDigitCompleteTimeout_Type(Integer32):defaultValue=4000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_EamTimerVariantsBwdDigitCompleteTimeout_Type.__name__=_C
_EamTimerVariantsBwdDigitCompleteTimeout_Object=MibTableColumn
eamTimerVariantsBwdDigitCompleteTimeout=_EamTimerVariantsBwdDigitCompleteTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,700),_EamTimerVariantsBwdDigitCompleteTimeout_Type())
eamTimerVariantsBwdDigitCompleteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsBwdDigitCompleteTimeout.setStatus(_A)
class _EamTimerVariantsFwdWaitWinkTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamTimerVariantsFwdWaitWinkTimeout_Type.__name__=_C
_EamTimerVariantsFwdWaitWinkTimeout_Object=MibTableColumn
eamTimerVariantsFwdWaitWinkTimeout=_EamTimerVariantsFwdWaitWinkTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,800),_EamTimerVariantsFwdWaitWinkTimeout_Type())
eamTimerVariantsFwdWaitWinkTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsFwdWaitWinkTimeout.setStatus(_A)
class _EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type.__name__=_C
_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Object=MibTableColumn
eamTimerVariantsFwdWaitMaxWinkOnTimeout=_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,900),_EamTimerVariantsFwdWaitMaxWinkOnTimeout_Type())
eamTimerVariantsFwdWaitMaxWinkOnTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsFwdWaitMaxWinkOnTimeout.setStatus(_A)
class _EamTimerVariantsFwdWaitPreDialTimeout_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_EamTimerVariantsFwdWaitPreDialTimeout_Type.__name__=_C
_EamTimerVariantsFwdWaitPreDialTimeout_Object=MibTableColumn
eamTimerVariantsFwdWaitPreDialTimeout=_EamTimerVariantsFwdWaitPreDialTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,1000),_EamTimerVariantsFwdWaitPreDialTimeout_Type())
eamTimerVariantsFwdWaitPreDialTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsFwdWaitPreDialTimeout.setStatus(_A)
class _EamTimerVariantsFwdWaitAnswerTimeout_Type(Integer32):defaultValue=180000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_EamTimerVariantsFwdWaitAnswerTimeout_Type.__name__=_C
_EamTimerVariantsFwdWaitAnswerTimeout_Object=MibTableColumn
eamTimerVariantsFwdWaitAnswerTimeout=_EamTimerVariantsFwdWaitAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,1100),_EamTimerVariantsFwdWaitAnswerTimeout_Type())
eamTimerVariantsFwdWaitAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsFwdWaitAnswerTimeout.setStatus(_A)
class _EamTimerVariantsFwdClearForwardTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_EamTimerVariantsFwdClearForwardTimeout_Type.__name__=_C
_EamTimerVariantsFwdClearForwardTimeout_Object=MibTableColumn
eamTimerVariantsFwdClearForwardTimeout=_EamTimerVariantsFwdClearForwardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,1200),_EamTimerVariantsFwdClearForwardTimeout_Type())
eamTimerVariantsFwdClearForwardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsFwdClearForwardTimeout.setStatus(_A)
class _EamTimerVariantsReleaseGuardTimeout_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamTimerVariantsReleaseGuardTimeout_Type.__name__=_C
_EamTimerVariantsReleaseGuardTimeout_Object=MibTableColumn
eamTimerVariantsReleaseGuardTimeout=_EamTimerVariantsReleaseGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,1300),_EamTimerVariantsReleaseGuardTimeout_Type())
eamTimerVariantsReleaseGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsReleaseGuardTimeout.setStatus(_A)
class _EamTimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),(_I,10)))
_EamTimerVariantsResetSpecific_Type.__name__=_C
_EamTimerVariantsResetSpecific_Object=MibTableColumn
eamTimerVariantsResetSpecific=_EamTimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,300,1,1900),_EamTimerVariantsResetSpecific_Type())
eamTimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:eamTimerVariantsResetSpecific.setStatus(_A)
_EamDigitTimerVariantsTable_Object=MibTable
eamDigitTimerVariantsTable=_EamDigitTimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400))
if mibBuilder.loadTexts:eamDigitTimerVariantsTable.setStatus(_A)
_EamDigitTimerVariantsEntry_Object=MibTableRow
eamDigitTimerVariantsEntry=_EamDigitTimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1))
eamDigitTimerVariantsEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:eamDigitTimerVariantsEntry.setStatus(_A)
_EamDigitTimerVariantsInterfaceName_Type=OctetString
_EamDigitTimerVariantsInterfaceName_Object=MibTableColumn
eamDigitTimerVariantsInterfaceName=_EamDigitTimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1,100),_EamDigitTimerVariantsInterfaceName_Type())
eamDigitTimerVariantsInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamDigitTimerVariantsInterfaceName.setStatus(_A)
class _EamDigitTimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_EamDigitTimerVariantsOverrideDefault_Type.__name__=_E
_EamDigitTimerVariantsOverrideDefault_Object=MibTableColumn
eamDigitTimerVariantsOverrideDefault=_EamDigitTimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1,200),_EamDigitTimerVariantsOverrideDefault_Type())
eamDigitTimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eamDigitTimerVariantsOverrideDefault.setStatus(_A)
class _EamDigitTimerVariantsKPOnTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamDigitTimerVariantsKPOnTimeout_Type.__name__=_C
_EamDigitTimerVariantsKPOnTimeout_Object=MibTableColumn
eamDigitTimerVariantsKPOnTimeout=_EamDigitTimerVariantsKPOnTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1,300),_EamDigitTimerVariantsKPOnTimeout_Type())
eamDigitTimerVariantsKPOnTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamDigitTimerVariantsKPOnTimeout.setStatus(_A)
class _EamDigitTimerVariantsKPOffTimeout_Type(Integer32):defaultValue=68;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamDigitTimerVariantsKPOffTimeout_Type.__name__=_C
_EamDigitTimerVariantsKPOffTimeout_Object=MibTableColumn
eamDigitTimerVariantsKPOffTimeout=_EamDigitTimerVariantsKPOffTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1,400),_EamDigitTimerVariantsKPOffTimeout_Type())
eamDigitTimerVariantsKPOffTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamDigitTimerVariantsKPOffTimeout.setStatus(_A)
class _EamDigitTimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),(_I,10)))
_EamDigitTimerVariantsResetSpecific_Type.__name__=_C
_EamDigitTimerVariantsResetSpecific_Object=MibTableColumn
eamDigitTimerVariantsResetSpecific=_EamDigitTimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,400,1,900),_EamDigitTimerVariantsResetSpecific_Type())
eamDigitTimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:eamDigitTimerVariantsResetSpecific.setStatus(_A)
_EamLinkTimerVariantsTable_Object=MibTable
eamLinkTimerVariantsTable=_EamLinkTimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500))
if mibBuilder.loadTexts:eamLinkTimerVariantsTable.setStatus(_A)
_EamLinkTimerVariantsEntry_Object=MibTableRow
eamLinkTimerVariantsEntry=_EamLinkTimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1))
eamLinkTimerVariantsEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:eamLinkTimerVariantsEntry.setStatus(_A)
_EamLinkTimerVariantsInterfaceName_Type=OctetString
_EamLinkTimerVariantsInterfaceName_Object=MibTableColumn
eamLinkTimerVariantsInterfaceName=_EamLinkTimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1,100),_EamLinkTimerVariantsInterfaceName_Type())
eamLinkTimerVariantsInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamLinkTimerVariantsInterfaceName.setStatus(_A)
class _EamLinkTimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_EamLinkTimerVariantsOverrideDefault_Type.__name__=_E
_EamLinkTimerVariantsOverrideDefault_Object=MibTableColumn
eamLinkTimerVariantsOverrideDefault=_EamLinkTimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1,200),_EamLinkTimerVariantsOverrideDefault_Type())
eamLinkTimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eamLinkTimerVariantsOverrideDefault.setStatus(_A)
class _EamLinkTimerVariantsLinkActivationTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamLinkTimerVariantsLinkActivationTimeout_Type.__name__=_C
_EamLinkTimerVariantsLinkActivationTimeout_Object=MibTableColumn
eamLinkTimerVariantsLinkActivationTimeout=_EamLinkTimerVariantsLinkActivationTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1,300),_EamLinkTimerVariantsLinkActivationTimeout_Type())
eamLinkTimerVariantsLinkActivationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamLinkTimerVariantsLinkActivationTimeout.setStatus(_A)
class _EamLinkTimerVariantsLinkActivationRetryTimeout_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EamLinkTimerVariantsLinkActivationRetryTimeout_Type.__name__=_C
_EamLinkTimerVariantsLinkActivationRetryTimeout_Object=MibTableColumn
eamLinkTimerVariantsLinkActivationRetryTimeout=_EamLinkTimerVariantsLinkActivationRetryTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1,400),_EamLinkTimerVariantsLinkActivationRetryTimeout_Type())
eamLinkTimerVariantsLinkActivationRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eamLinkTimerVariantsLinkActivationRetryTimeout.setStatus(_A)
class _EamLinkTimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),(_I,10)))
_EamLinkTimerVariantsResetSpecific_Type.__name__=_C
_EamLinkTimerVariantsResetSpecific_Object=MibTableColumn
eamLinkTimerVariantsResetSpecific=_EamLinkTimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,500,1,900),_EamLinkTimerVariantsResetSpecific_Type())
eamLinkTimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:eamLinkTimerVariantsResetSpecific.setStatus(_A)
_EamToneVariantsTable_Object=MibTable
eamToneVariantsTable=_EamToneVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600))
if mibBuilder.loadTexts:eamToneVariantsTable.setStatus(_A)
_EamToneVariantsEntry_Object=MibTableRow
eamToneVariantsEntry=_EamToneVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1))
eamToneVariantsEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:eamToneVariantsEntry.setStatus(_A)
_EamToneVariantsInterfaceName_Type=OctetString
_EamToneVariantsInterfaceName_Object=MibTableColumn
eamToneVariantsInterfaceName=_EamToneVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1,100),_EamToneVariantsInterfaceName_Type())
eamToneVariantsInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:eamToneVariantsInterfaceName.setStatus(_A)
class _EamToneVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_EamToneVariantsOverrideDefault_Type.__name__=_E
_EamToneVariantsOverrideDefault_Object=MibTableColumn
eamToneVariantsOverrideDefault=_EamToneVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1,200),_EamToneVariantsOverrideDefault_Type())
eamToneVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:eamToneVariantsOverrideDefault.setStatus(_A)
class _EamToneVariantsKpTone_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_K,100),('mF0',200),('mF1',300),('mF2',400),('mF3',500),('mF4',600),('mF5',700),('mF6',800),('mF7',900),('mF8',1000),('mF9',1100),('mF10',1200),('mF11',1300),('mF12',1400),('mF13',1500),('mF14',1600)))
_EamToneVariantsKpTone_Type.__name__=_C
_EamToneVariantsKpTone_Object=MibTableColumn
eamToneVariantsKpTone=_EamToneVariantsKpTone_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1,300),_EamToneVariantsKpTone_Type())
eamToneVariantsKpTone.setMaxAccess(_B)
if mibBuilder.loadTexts:eamToneVariantsKpTone.setStatus(_A)
class _EamToneVariantsStTone_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_K,100),('mF0',200),('mF1',300),('mF2',400),('mF3',500),('mF4',600),('mF5',700),('mF6',800),('mF7',900),('mF8',1000),('mF9',1100),('mF10',1200),('mF11',1300),('mF12',1400),('mF13',1500),('mF14',1600)))
_EamToneVariantsStTone_Type.__name__=_C
_EamToneVariantsStTone_Object=MibTableColumn
eamToneVariantsStTone=_EamToneVariantsStTone_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1,400),_EamToneVariantsStTone_Type())
eamToneVariantsStTone.setMaxAccess(_B)
if mibBuilder.loadTexts:eamToneVariantsStTone.setStatus(_A)
class _EamToneVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),(_I,10)))
_EamToneVariantsResetSpecific_Type.__name__=_C
_EamToneVariantsResetSpecific_Object=MibTableColumn
eamToneVariantsResetSpecific=_EamToneVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,100,600,1,900),_EamToneVariantsResetSpecific_Type())
eamToneVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:eamToneVariantsResetSpecific.setStatus(_A)
_BearerChannelGroup_ObjectIdentity=ObjectIdentity
bearerChannelGroup=_BearerChannelGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,200))
_BearerChannelInfoTable_Object=MibTable
bearerChannelInfoTable=_BearerChannelInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,200,100))
if mibBuilder.loadTexts:bearerChannelInfoTable.setStatus(_A)
_BearerChannelInfoEntry_Object=MibTableRow
bearerChannelInfoEntry=_BearerChannelInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,200,100,1))
bearerChannelInfoEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:bearerChannelInfoEntry.setStatus(_A)
_BearerChannelInfoIndex_Type=OctetString
_BearerChannelInfoIndex_Object=MibTableColumn
bearerChannelInfoIndex=_BearerChannelInfoIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,200,100,1,100),_BearerChannelInfoIndex_Type())
bearerChannelInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bearerChannelInfoIndex.setStatus(_A)
class _BearerChannelInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('idle',100),('inUse',200),('maintenance',300),('error',400),('disabled',500)))
_BearerChannelInfoState_Type.__name__=_C
_BearerChannelInfoState_Object=MibTableColumn
bearerChannelInfoState=_BearerChannelInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,200,100,1,200),_BearerChannelInfoState_Type())
bearerChannelInfoState.setMaxAccess(_D)
if mibBuilder.loadTexts:bearerChannelInfoState.setStatus(_A)
_PhysicalGroup_ObjectIdentity=ObjectIdentity
physicalGroup=_PhysicalGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300))
_PhysicalLinkInfoTable_Object=MibTable
physicalLinkInfoTable=_PhysicalLinkInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,100))
if mibBuilder.loadTexts:physicalLinkInfoTable.setStatus(_A)
_PhysicalLinkInfoEntry_Object=MibTableRow
physicalLinkInfoEntry=_PhysicalLinkInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,100,1))
physicalLinkInfoEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:physicalLinkInfoEntry.setStatus(_A)
_PhysicalLinkInfoInterfaceName_Type=OctetString
_PhysicalLinkInfoInterfaceName_Object=MibTableColumn
physicalLinkInfoInterfaceName=_PhysicalLinkInfoInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,100,1,100),_PhysicalLinkInfoInterfaceName_Type())
physicalLinkInfoInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:physicalLinkInfoInterfaceName.setStatus(_A)
class _PhysicalLinkInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('up',100),('down',200)))
_PhysicalLinkInfoState_Type.__name__=_C
_PhysicalLinkInfoState_Object=MibTableColumn
physicalLinkInfoState=_PhysicalLinkInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,100,1,200),_PhysicalLinkInfoState_Type())
physicalLinkInfoState.setMaxAccess(_D)
if mibBuilder.loadTexts:physicalLinkInfoState.setStatus(_A)
_PhysicalLinkTable_Object=MibTable
physicalLinkTable=_PhysicalLinkTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200))
if mibBuilder.loadTexts:physicalLinkTable.setStatus(_A)
_PhysicalLinkEntry_Object=MibTableRow
physicalLinkEntry=_PhysicalLinkEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1))
physicalLinkEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:physicalLinkEntry.setStatus(_A)
_PhysicalLinkInterfaceName_Type=OctetString
_PhysicalLinkInterfaceName_Object=MibTableColumn
physicalLinkInterfaceName=_PhysicalLinkInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,100),_PhysicalLinkInterfaceName_Type())
physicalLinkInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:physicalLinkInterfaceName.setStatus(_A)
class _PhysicalLinkLineCoding_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('b8zs',100),('hdb3',200),('ami',300)))
_PhysicalLinkLineCoding_Type.__name__=_C
_PhysicalLinkLineCoding_Object=MibTableColumn
physicalLinkLineCoding=_PhysicalLinkLineCoding_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,200),_PhysicalLinkLineCoding_Type())
physicalLinkLineCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkLineCoding.setStatus(_A)
class _PhysicalLinkLineFraming_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sf',100),('esf',200),('crc4',300),('noCrc4',400)))
_PhysicalLinkLineFraming_Type.__name__=_C
_PhysicalLinkLineFraming_Object=MibTableColumn
physicalLinkLineFraming=_PhysicalLinkLineFraming_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,300),_PhysicalLinkLineFraming_Type())
physicalLinkLineFraming.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkLineFraming.setStatus(_A)
class _PhysicalLinkClockMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_V,100),('slave',200)))
_PhysicalLinkClockMode_Type.__name__=_C
_PhysicalLinkClockMode_Object=MibTableColumn
physicalLinkClockMode=_PhysicalLinkClockMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,400),_PhysicalLinkClockMode_Type())
physicalLinkClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkClockMode.setStatus(_A)
class _PhysicalLinkMonitorLinkStateEnable_Type(MxEnableState):defaultValue=1
_PhysicalLinkMonitorLinkStateEnable_Type.__name__=_E
_PhysicalLinkMonitorLinkStateEnable_Object=MibTableColumn
physicalLinkMonitorLinkStateEnable=_PhysicalLinkMonitorLinkStateEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,500),_PhysicalLinkMonitorLinkStateEnable_Type())
physicalLinkMonitorLinkStateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkMonitorLinkStateEnable.setStatus(_A)
class _PhysicalLinkPortPinout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('auto',100),(_V,200),('slave',300)))
_PhysicalLinkPortPinout_Type.__name__=_C
_PhysicalLinkPortPinout_Object=MibTableColumn
physicalLinkPortPinout=_PhysicalLinkPortPinout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,300,200,1,600),_PhysicalLinkPortPinout_Type())
physicalLinkPortPinout.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkPortPinout.setStatus(_A)
_AutoConfigure_ObjectIdentity=ObjectIdentity
autoConfigure=_AutoConfigure_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,400))
class _AutoConfigureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('idle',100),('sensing',200)))
_AutoConfigureStatus_Type.__name__=_C
_AutoConfigureStatus_Object=MibScalar
autoConfigureStatus=_AutoConfigureStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,400,100),_AutoConfigureStatus_Type())
autoConfigureStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:autoConfigureStatus.setStatus(_A)
class _LastAutoConfigureResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_K,100),('success',200),('fail',300),('aborted',400)))
_LastAutoConfigureResult_Type.__name__=_C
_LastAutoConfigureResult_Object=MibScalar
lastAutoConfigureResult=_LastAutoConfigureResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,400,200),_LastAutoConfigureResult_Type())
lastAutoConfigureResult.setMaxAccess(_D)
if mibBuilder.loadTexts:lastAutoConfigureResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1880,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'eamMIB':eamMIB,'eamMIBObjects':eamMIBObjects,'eamGroup':eamGroup,'eamTable':eamTable,'eamEntry':eamEntry,_L:eamName,'eamChannelRange':eamChannelRange,'eamChannelAllocationStrategy':eamChannelAllocationStrategy,'eamMaxActiveCalls':eamMaxActiveCalls,'eamEncodingScheme':eamEncodingScheme,'eamSignalingType':eamSignalingType,'eamDigitAttenuation':eamDigitAttenuation,'eamSignalingVariantsTable':eamSignalingVariantsTable,'eamSignalingVariantsEntry':eamSignalingVariantsEntry,_M:eamSignalingVariantsInterfaceName,'eamSignalingVariantsOverrideDefault':eamSignalingVariantsOverrideDefault,'eamSignalingVariantsBitsBCD':eamSignalingVariantsBitsBCD,'eamSignalingVariantsDnisLength':eamSignalingVariantsDnisLength,'eamSignalingVariantsAniLength':eamSignalingVariantsAniLength,'eamSignalingVariantsIncomingRegisterSignaling':eamSignalingVariantsIncomingRegisterSignaling,'eamSignalingVariantsOutgoingRegisterSignaling':eamSignalingVariantsOutgoingRegisterSignaling,'eamSignalingVariantsIncomingDialMap':eamSignalingVariantsIncomingDialMap,'eamSignalingVariantsOutgoingDialMap':eamSignalingVariantsOutgoingDialMap,'eamSignalingVariantsWaitWink':eamSignalingVariantsWaitWink,'eamSignalingVariantsWaitWinkAck':eamSignalingVariantsWaitWinkAck,'eamSignalingVariantsSendWink':eamSignalingVariantsSendWink,'eamSignalingVariantsSendWinkAck':eamSignalingVariantsSendWinkAck,'eamSignalingVariantsResetSpecific':eamSignalingVariantsResetSpecific,'eamTimerVariantsTable':eamTimerVariantsTable,'eamTimerVariantsEntry':eamTimerVariantsEntry,_O:eamTimerVariantsInterfaceName,'eamTimerVariantsOverrideDefault':eamTimerVariantsOverrideDefault,'eamTimerVariantsBwdWaitPreWinkTimeout':eamTimerVariantsBwdWaitPreWinkTimeout,'eamTimerVariantsBwdSendWinkTimeout':eamTimerVariantsBwdSendWinkTimeout,'eamTimerVariantsBwdWait1stDigitTimeout':eamTimerVariantsBwdWait1stDigitTimeout,'eamTimerVariantsBwdClearBackwardTimeout':eamTimerVariantsBwdClearBackwardTimeout,'eamTimerVariantsBwdDigitCompleteTimeout':eamTimerVariantsBwdDigitCompleteTimeout,'eamTimerVariantsFwdWaitWinkTimeout':eamTimerVariantsFwdWaitWinkTimeout,'eamTimerVariantsFwdWaitMaxWinkOnTimeout':eamTimerVariantsFwdWaitMaxWinkOnTimeout,'eamTimerVariantsFwdWaitPreDialTimeout':eamTimerVariantsFwdWaitPreDialTimeout,'eamTimerVariantsFwdWaitAnswerTimeout':eamTimerVariantsFwdWaitAnswerTimeout,'eamTimerVariantsFwdClearForwardTimeout':eamTimerVariantsFwdClearForwardTimeout,'eamTimerVariantsReleaseGuardTimeout':eamTimerVariantsReleaseGuardTimeout,'eamTimerVariantsResetSpecific':eamTimerVariantsResetSpecific,'eamDigitTimerVariantsTable':eamDigitTimerVariantsTable,'eamDigitTimerVariantsEntry':eamDigitTimerVariantsEntry,_P:eamDigitTimerVariantsInterfaceName,'eamDigitTimerVariantsOverrideDefault':eamDigitTimerVariantsOverrideDefault,'eamDigitTimerVariantsKPOnTimeout':eamDigitTimerVariantsKPOnTimeout,'eamDigitTimerVariantsKPOffTimeout':eamDigitTimerVariantsKPOffTimeout,'eamDigitTimerVariantsResetSpecific':eamDigitTimerVariantsResetSpecific,'eamLinkTimerVariantsTable':eamLinkTimerVariantsTable,'eamLinkTimerVariantsEntry':eamLinkTimerVariantsEntry,_Q:eamLinkTimerVariantsInterfaceName,'eamLinkTimerVariantsOverrideDefault':eamLinkTimerVariantsOverrideDefault,'eamLinkTimerVariantsLinkActivationTimeout':eamLinkTimerVariantsLinkActivationTimeout,'eamLinkTimerVariantsLinkActivationRetryTimeout':eamLinkTimerVariantsLinkActivationRetryTimeout,'eamLinkTimerVariantsResetSpecific':eamLinkTimerVariantsResetSpecific,'eamToneVariantsTable':eamToneVariantsTable,'eamToneVariantsEntry':eamToneVariantsEntry,_R:eamToneVariantsInterfaceName,'eamToneVariantsOverrideDefault':eamToneVariantsOverrideDefault,'eamToneVariantsKpTone':eamToneVariantsKpTone,'eamToneVariantsStTone':eamToneVariantsStTone,'eamToneVariantsResetSpecific':eamToneVariantsResetSpecific,'bearerChannelGroup':bearerChannelGroup,'bearerChannelInfoTable':bearerChannelInfoTable,'bearerChannelInfoEntry':bearerChannelInfoEntry,_S:bearerChannelInfoIndex,'bearerChannelInfoState':bearerChannelInfoState,'physicalGroup':physicalGroup,'physicalLinkInfoTable':physicalLinkInfoTable,'physicalLinkInfoEntry':physicalLinkInfoEntry,_T:physicalLinkInfoInterfaceName,'physicalLinkInfoState':physicalLinkInfoState,'physicalLinkTable':physicalLinkTable,'physicalLinkEntry':physicalLinkEntry,_U:physicalLinkInterfaceName,'physicalLinkLineCoding':physicalLinkLineCoding,'physicalLinkLineFraming':physicalLinkLineFraming,'physicalLinkClockMode':physicalLinkClockMode,'physicalLinkMonitorLinkStateEnable':physicalLinkMonitorLinkStateEnable,'physicalLinkPortPinout':physicalLinkPortPinout,'autoConfigure':autoConfigure,'autoConfigureStatus':autoConfigureStatus,'lastAutoConfigureResult':lastAutoConfigureResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})