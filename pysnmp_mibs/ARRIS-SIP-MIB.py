_A1='sipStatusPortPortNumber'
_A0='sipCfgDialProxyNumber'
_z='stutterTone'
_y='sipCfgDialFeatNumber'
_x='forceEnable'
_w='forceDisable'
_v='ignore'
_u='sipCfgPortPortNumber'
_t='00000000'
_s='read-only'
_r='dns'
_q='not-accessible'
_p='ipv4'
_o='ARRIS-SIP-MIB'
_n='Unsigned32'
_m='TruthValue'
_l='OctetString'
_k='line01'
_j='line02'
_i='line03'
_h='line04'
_g='line05'
_f='line06'
_e='line07'
_d='line08'
_c='line09'
_b='line10'
_a='line11'
_Z='line12'
_Y='line13'
_X='line14'
_W='line15'
_V='line16'
_U='line17'
_T='line18'
_S='line19'
_R='line20'
_Q='line21'
_P='line22'
_O='line23'
_N='line24'
_M='line25'
_L='line26'
_K='line27'
_J='line28'
_I='line29'
_H='line30'
_G='line31'
_F='line32'
_E='DisplayString'
_D='Bits'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_l,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arris,=mibBuilder.importSymbols('ARRIS-MIB','arris')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_n,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention',_m)
arrisSipMib=ModuleIdentity((1,3,6,1,4,1,4115,11))
_SipConfiguration_ObjectIdentity=ObjectIdentity
sipConfiguration=_SipConfiguration_ObjectIdentity((1,3,6,1,4,1,4115,11,1))
_SipCfgPortTable_Object=MibTable
sipCfgPortTable=_SipCfgPortTable_Object((1,3,6,1,4,1,4115,11,1,1))
if mibBuilder.loadTexts:sipCfgPortTable.setStatus(_A)
_SipCfgPortEntry_Object=MibTableRow
sipCfgPortEntry=_SipCfgPortEntry_Object((1,3,6,1,4,1,4115,11,1,1,1))
sipCfgPortEntry.setIndexNames((0,_o,_u))
if mibBuilder.loadTexts:sipCfgPortEntry.setStatus(_A)
_SipCfgPortPortNumber_Type=Integer32
_SipCfgPortPortNumber_Object=MibTableColumn
sipCfgPortPortNumber=_SipCfgPortPortNumber_Object((1,3,6,1,4,1,4115,11,1,1,1,1),_SipCfgPortPortNumber_Type())
sipCfgPortPortNumber.setMaxAccess(_q)
if mibBuilder.loadTexts:sipCfgPortPortNumber.setStatus(_A)
class _SipCfgPortUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_SipCfgPortUserName_Type.__name__=_l
_SipCfgPortUserName_Object=MibTableColumn
sipCfgPortUserName=_SipCfgPortUserName_Object((1,3,6,1,4,1,4115,11,1,1,1,2),_SipCfgPortUserName_Type())
sipCfgPortUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortUserName.setStatus(_A)
_SipCfgPortDisplayName_Type=DisplayString
_SipCfgPortDisplayName_Object=MibTableColumn
sipCfgPortDisplayName=_SipCfgPortDisplayName_Object((1,3,6,1,4,1,4115,11,1,1,1,3),_SipCfgPortDisplayName_Type())
sipCfgPortDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortDisplayName.setStatus(_A)
class _SipCfgPortLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_SipCfgPortLogin_Type.__name__=_l
_SipCfgPortLogin_Object=MibTableColumn
sipCfgPortLogin=_SipCfgPortLogin_Object((1,3,6,1,4,1,4115,11,1,1,1,4),_SipCfgPortLogin_Type())
sipCfgPortLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortLogin.setStatus(_A)
class _SipCfgPortPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_SipCfgPortPassword_Type.__name__=_l
_SipCfgPortPassword_Object=MibTableColumn
sipCfgPortPassword=_SipCfgPortPassword_Object((1,3,6,1,4,1,4115,11,1,1,1,5),_SipCfgPortPassword_Type())
sipCfgPortPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortPassword.setStatus(_A)
_SipCfgPortWarmOrHotlineNumber_Type=DisplayString
_SipCfgPortWarmOrHotlineNumber_Object=MibTableColumn
sipCfgPortWarmOrHotlineNumber=_SipCfgPortWarmOrHotlineNumber_Object((1,3,6,1,4,1,4115,11,1,1,1,6),_SipCfgPortWarmOrHotlineNumber_Type())
sipCfgPortWarmOrHotlineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortWarmOrHotlineNumber.setStatus(_A)
class _SipCfgPortWarmLineTimeout_Type(Integer32):defaultValue=5
_SipCfgPortWarmLineTimeout_Type.__name__=_C
_SipCfgPortWarmLineTimeout_Object=MibTableColumn
sipCfgPortWarmLineTimeout=_SipCfgPortWarmLineTimeout_Object((1,3,6,1,4,1,4115,11,1,1,1,7),_SipCfgPortWarmLineTimeout_Type())
sipCfgPortWarmLineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortWarmLineTimeout.setStatus(_A)
_SipCfgPortRegistrarAdr_Type=DisplayString
_SipCfgPortRegistrarAdr_Object=MibTableColumn
sipCfgPortRegistrarAdr=_SipCfgPortRegistrarAdr_Object((1,3,6,1,4,1,4115,11,1,1,1,8),_SipCfgPortRegistrarAdr_Type())
sipCfgPortRegistrarAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortRegistrarAdr.setStatus(_A)
_SipCfgPortRegistrarPort_Type=Integer32
_SipCfgPortRegistrarPort_Object=MibTableColumn
sipCfgPortRegistrarPort=_SipCfgPortRegistrarPort_Object((1,3,6,1,4,1,4115,11,1,1,1,9),_SipCfgPortRegistrarPort_Type())
sipCfgPortRegistrarPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortRegistrarPort.setStatus(_A)
class _SipCfgPortRegistrarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_r,1)))
_SipCfgPortRegistrarType_Type.__name__=_C
_SipCfgPortRegistrarType_Object=MibTableColumn
sipCfgPortRegistrarType=_SipCfgPortRegistrarType_Object((1,3,6,1,4,1,4115,11,1,1,1,10),_SipCfgPortRegistrarType_Type())
sipCfgPortRegistrarType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortRegistrarType.setStatus(_A)
_SipCfgPortProxyAdr_Type=DisplayString
_SipCfgPortProxyAdr_Object=MibTableColumn
sipCfgPortProxyAdr=_SipCfgPortProxyAdr_Object((1,3,6,1,4,1,4115,11,1,1,1,11),_SipCfgPortProxyAdr_Type())
sipCfgPortProxyAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortProxyAdr.setStatus(_A)
_SipCfgPortProxyPort_Type=Integer32
_SipCfgPortProxyPort_Object=MibTableColumn
sipCfgPortProxyPort=_SipCfgPortProxyPort_Object((1,3,6,1,4,1,4115,11,1,1,1,12),_SipCfgPortProxyPort_Type())
sipCfgPortProxyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortProxyPort.setStatus(_A)
class _SipCfgPortProxyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_r,1)))
_SipCfgPortProxyType_Type.__name__=_C
_SipCfgPortProxyType_Object=MibTableColumn
sipCfgPortProxyType=_SipCfgPortProxyType_Object((1,3,6,1,4,1,4115,11,1,1,1,13),_SipCfgPortProxyType_Type())
sipCfgPortProxyType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortProxyType.setStatus(_A)
class _SipCfgPortFeatureSettings_Type(Bits):namedValues=NamedValues(*(('defaultFeatures',0),('callerIdPermanentDisable',1),('anonCallRejectionEnable',2),('callWaitingPermanentDisable',3),('threeWayCallingDisable',4),('callerIdReceiptDisable',5),('callTransferEnable',6)))
_SipCfgPortFeatureSettings_Type.__name__=_D
_SipCfgPortFeatureSettings_Object=MibTableColumn
sipCfgPortFeatureSettings=_SipCfgPortFeatureSettings_Object((1,3,6,1,4,1,4115,11,1,1,1,14),_SipCfgPortFeatureSettings_Type())
sipCfgPortFeatureSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortFeatureSettings.setStatus(_A)
class _SipCfgPortT38Mode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t38Off',1),('t38Loose',2),('t38Strict',3)))
_SipCfgPortT38Mode_Type.__name__=_C
_SipCfgPortT38Mode_Object=MibTableColumn
sipCfgPortT38Mode=_SipCfgPortT38Mode_Object((1,3,6,1,4,1,4115,11,1,1,1,15),_SipCfgPortT38Mode_Type())
sipCfgPortT38Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortT38Mode.setStatus(_A)
class _SipCfgPortFaxOnlyTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_SipCfgPortFaxOnlyTimeout_Type.__name__=_C
_SipCfgPortFaxOnlyTimeout_Object=MibTableColumn
sipCfgPortFaxOnlyTimeout=_SipCfgPortFaxOnlyTimeout_Object((1,3,6,1,4,1,4115,11,1,1,1,16),_SipCfgPortFaxOnlyTimeout_Type())
sipCfgPortFaxOnlyTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortFaxOnlyTimeout.setStatus(_A)
class _SipCfgPortMaxT38HSRedLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_SipCfgPortMaxT38HSRedLevel_Type.__name__=_C
_SipCfgPortMaxT38HSRedLevel_Object=MibTableColumn
sipCfgPortMaxT38HSRedLevel=_SipCfgPortMaxT38HSRedLevel_Object((1,3,6,1,4,1,4115,11,1,1,1,17),_SipCfgPortMaxT38HSRedLevel_Type())
sipCfgPortMaxT38HSRedLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortMaxT38HSRedLevel.setStatus(_A)
class _SipCfgPortCallByeDelay_Type(Unsigned32):defaultValue=0
_SipCfgPortCallByeDelay_Type.__name__=_n
_SipCfgPortCallByeDelay_Object=MibTableColumn
sipCfgPortCallByeDelay=_SipCfgPortCallByeDelay_Object((1,3,6,1,4,1,4115,11,1,1,1,18),_SipCfgPortCallByeDelay_Type())
sipCfgPortCallByeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortCallByeDelay.setStatus(_A)
class _SipCfgPortMWIClear_Type(TruthValue):defaultValue=2
_SipCfgPortMWIClear_Type.__name__=_m
_SipCfgPortMWIClear_Object=MibTableColumn
sipCfgPortMWIClear=_SipCfgPortMWIClear_Object((1,3,6,1,4,1,4115,11,1,1,1,19),_SipCfgPortMWIClear_Type())
sipCfgPortMWIClear.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortMWIClear.setStatus(_A)
class _SipCfgPortMWIVisualEnable_Type(TruthValue):defaultValue=1
_SipCfgPortMWIVisualEnable_Type.__name__=_m
_SipCfgPortMWIVisualEnable_Object=MibTableColumn
sipCfgPortMWIVisualEnable=_SipCfgPortMWIVisualEnable_Object((1,3,6,1,4,1,4115,11,1,1,1,20),_SipCfgPortMWIVisualEnable_Type())
sipCfgPortMWIVisualEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortMWIVisualEnable.setStatus(_A)
class _SipCfgPortMWIToneEnable_Type(TruthValue):defaultValue=1
_SipCfgPortMWIToneEnable_Type.__name__=_m
_SipCfgPortMWIToneEnable_Object=MibTableColumn
sipCfgPortMWIToneEnable=_SipCfgPortMWIToneEnable_Object((1,3,6,1,4,1,4115,11,1,1,1,21),_SipCfgPortMWIToneEnable_Type())
sipCfgPortMWIToneEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortMWIToneEnable.setStatus(_A)
class _SipCfgPortWarmOrHotlineEnable_Type(TruthValue):defaultValue=1
_SipCfgPortWarmOrHotlineEnable_Type.__name__=_m
_SipCfgPortWarmOrHotlineEnable_Object=MibTableColumn
sipCfgPortWarmOrHotlineEnable=_SipCfgPortWarmOrHotlineEnable_Object((1,3,6,1,4,1,4115,11,1,1,1,22),_SipCfgPortWarmOrHotlineEnable_Type())
sipCfgPortWarmOrHotlineEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortWarmOrHotlineEnable.setStatus(_A)
class _SipCfgPortDndRingReminderEnable_Type(TruthValue):defaultValue=2
_SipCfgPortDndRingReminderEnable_Type.__name__=_m
_SipCfgPortDndRingReminderEnable_Object=MibTableColumn
sipCfgPortDndRingReminderEnable=_SipCfgPortDndRingReminderEnable_Object((1,3,6,1,4,1,4115,11,1,1,1,23),_SipCfgPortDndRingReminderEnable_Type())
sipCfgPortDndRingReminderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortDndRingReminderEnable.setStatus(_A)
class _SipCfgPortLoopReversal_Type(TruthValue):defaultValue=2
_SipCfgPortLoopReversal_Type.__name__=_m
_SipCfgPortLoopReversal_Object=MibTableColumn
sipCfgPortLoopReversal=_SipCfgPortLoopReversal_Object((1,3,6,1,4,1,4115,11,1,1,1,24),_SipCfgPortLoopReversal_Type())
sipCfgPortLoopReversal.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortLoopReversal.setStatus(_A)
_SipCfgPortCurrentProxy_Type=DisplayString
_SipCfgPortCurrentProxy_Object=MibTableColumn
sipCfgPortCurrentProxy=_SipCfgPortCurrentProxy_Object((1,3,6,1,4,1,4115,11,1,1,1,25),_SipCfgPortCurrentProxy_Type())
sipCfgPortCurrentProxy.setMaxAccess(_s)
if mibBuilder.loadTexts:sipCfgPortCurrentProxy.setStatus(_A)
_SipCfgPortPrimaryProxy_Type=DisplayString
_SipCfgPortPrimaryProxy_Object=MibTableColumn
sipCfgPortPrimaryProxy=_SipCfgPortPrimaryProxy_Object((1,3,6,1,4,1,4115,11,1,1,1,26),_SipCfgPortPrimaryProxy_Type())
sipCfgPortPrimaryProxy.setMaxAccess(_s)
if mibBuilder.loadTexts:sipCfgPortPrimaryProxy.setStatus(_A)
class _SipCfgPortCallWaitingPermanentDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_v,0),(_w,1),(_x,2)))
_SipCfgPortCallWaitingPermanentDisable_Type.__name__=_C
_SipCfgPortCallWaitingPermanentDisable_Object=MibTableColumn
sipCfgPortCallWaitingPermanentDisable=_SipCfgPortCallWaitingPermanentDisable_Object((1,3,6,1,4,1,4115,11,1,1,1,27),_SipCfgPortCallWaitingPermanentDisable_Type())
sipCfgPortCallWaitingPermanentDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortCallWaitingPermanentDisable.setStatus(_A)
class _SipCfgPortCallerIDCallWaitingPermanentDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_v,0),(_w,1),(_x,2)))
_SipCfgPortCallerIDCallWaitingPermanentDisable_Type.__name__=_C
_SipCfgPortCallerIDCallWaitingPermanentDisable_Object=MibTableColumn
sipCfgPortCallerIDCallWaitingPermanentDisable=_SipCfgPortCallerIDCallWaitingPermanentDisable_Object((1,3,6,1,4,1,4115,11,1,1,1,28),_SipCfgPortCallerIDCallWaitingPermanentDisable_Type())
sipCfgPortCallerIDCallWaitingPermanentDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPortCallerIDCallWaitingPermanentDisable.setStatus(_A)
class _SipCfgDigitMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_SipCfgDigitMap_Type.__name__=_l
_SipCfgDigitMap_Object=MibScalar
sipCfgDigitMap=_SipCfgDigitMap_Object((1,3,6,1,4,1,4115,11,1,2),_SipCfgDigitMap_Type())
sipCfgDigitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDigitMap.setStatus(_A)
_SipCfgProxyAdr_Type=DisplayString
_SipCfgProxyAdr_Object=MibScalar
sipCfgProxyAdr=_SipCfgProxyAdr_Object((1,3,6,1,4,1,4115,11,1,3),_SipCfgProxyAdr_Type())
sipCfgProxyAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProxyAdr.setStatus(_A)
class _SipCfgProxyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_p,0),(_r,1),('unknown',2)))
_SipCfgProxyType_Type.__name__=_C
_SipCfgProxyType_Object=MibScalar
sipCfgProxyType=_SipCfgProxyType_Object((1,3,6,1,4,1,4115,11,1,4),_SipCfgProxyType_Type())
sipCfgProxyType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProxyType.setStatus(_A)
_SipCfgRegistrarAdr_Type=DisplayString
_SipCfgRegistrarAdr_Object=MibScalar
sipCfgRegistrarAdr=_SipCfgRegistrarAdr_Object((1,3,6,1,4,1,4115,11,1,5),_SipCfgRegistrarAdr_Type())
sipCfgRegistrarAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegistrarAdr.setStatus(_A)
class _SipCfgRegistrarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_r,1)))
_SipCfgRegistrarType_Type.__name__=_C
_SipCfgRegistrarType_Object=MibScalar
sipCfgRegistrarType=_SipCfgRegistrarType_Object((1,3,6,1,4,1,4115,11,1,6),_SipCfgRegistrarType_Type())
sipCfgRegistrarType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegistrarType.setStatus(_A)
class _SipCfgSipFeatureSwitch_Type(Bits):defaultHexValue=_t;namedValues=NamedValues(*(('telUriScheme',0),('mtaFQDN',1),('mwiRFC3842',2),('advFlashFeatures',3),('rfc3323Privacyheader',4),('overrideDomain',5),('disableCwCid',6),('useIpAddressOf0ForHold',7),('disable100REL',8),('useSrvLookups',9),('rtpKeepAlive',10),('ignoreEarlyMedia',11),('hookflashViaInfo',12),('limitSdpUpdates',13),('generateRemoteRT',14),('playLocalRtAfterEarlyMedia',15),('removeAuthHeaders',16),('useInactiveMedia',17),('noProvisionalSdpIn1XX',18),('disconnectOtherCallOnEmergency',19),('proxyPenaltyBox',20),('playBusyToneOnReject',21),('sessionTimerReInvite',22),('emergencyOnhookSendBye',23),('disableSessionTimers',24),('stutterToneHookFlash',25),('hookflashViaInfoStd',26),('subscribeUAProfileXML',27),('subscribeRegEventXML',28),('preferTelUriForCid',29),('callHoldWithoutReInvite',30),('restrictIncomingOffer',31)))
_SipCfgSipFeatureSwitch_Type.__name__=_D
_SipCfgSipFeatureSwitch_Object=MibScalar
sipCfgSipFeatureSwitch=_SipCfgSipFeatureSwitch_Object((1,3,6,1,4,1,4115,11,1,7),_SipCfgSipFeatureSwitch_Type())
sipCfgSipFeatureSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSipFeatureSwitch.setStatus(_A)
_SipCfgProvisionedCodecArray_Type=DisplayString
_SipCfgProvisionedCodecArray_Object=MibScalar
sipCfgProvisionedCodecArray=_SipCfgProvisionedCodecArray_Object((1,3,6,1,4,1,4115,11,1,8),_SipCfgProvisionedCodecArray_Type())
sipCfgProvisionedCodecArray.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProvisionedCodecArray.setStatus(_A)
class _SipCfgPacketizationRate_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30)));namedValues=NamedValues(*(('tenMilliSeconds',10),('twentyMilliSeconds',20),('thirtyMilliSeconds',30)))
_SipCfgPacketizationRate_Type.__name__=_C
_SipCfgPacketizationRate_Object=MibScalar
sipCfgPacketizationRate=_SipCfgPacketizationRate_Object((1,3,6,1,4,1,4115,11,1,9),_SipCfgPacketizationRate_Type())
sipCfgPacketizationRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPacketizationRate.setStatus(_A)
class _SipCfgDialFeatMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_SipCfgDialFeatMap_Type.__name__=_l
_SipCfgDialFeatMap_Object=MibScalar
sipCfgDialFeatMap=_SipCfgDialFeatMap_Object((1,3,6,1,4,1,4115,11,1,10),_SipCfgDialFeatMap_Type())
sipCfgDialFeatMap.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatMap.setStatus(_A)
_SipCfgDialFeatTable_Object=MibTable
sipCfgDialFeatTable=_SipCfgDialFeatTable_Object((1,3,6,1,4,1,4115,11,1,11))
if mibBuilder.loadTexts:sipCfgDialFeatTable.setStatus(_A)
_SipCfgDialFeatEntry_Object=MibTableRow
sipCfgDialFeatEntry=_SipCfgDialFeatEntry_Object((1,3,6,1,4,1,4115,11,1,11,1))
sipCfgDialFeatEntry.setIndexNames((0,_o,_y))
if mibBuilder.loadTexts:sipCfgDialFeatEntry.setStatus(_A)
_SipCfgDialFeatNumber_Type=Integer32
_SipCfgDialFeatNumber_Object=MibTableColumn
sipCfgDialFeatNumber=_SipCfgDialFeatNumber_Object((1,3,6,1,4,1,4115,11,1,11,1,1),_SipCfgDialFeatNumber_Type())
sipCfgDialFeatNumber.setMaxAccess(_q)
if mibBuilder.loadTexts:sipCfgDialFeatNumber.setStatus(_A)
class _SipCfgDialFeatName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,30,31,32,33,34,35,36,37,50,60,61,62,63,70,71,72,73,90,91,92)));namedValues=NamedValues(*(('anonCallReject',1),('anonCallRejectDisable',2),('callForwardBusy',30),('callForwardBusyDisable',31),('callForwardUncond',32),('callForwardUncondDisable',33),('callForwardNoAnswer',34),('callForwardNoAnswerDisable',35),('warmline',36),('warmlineDisable',37),('callReturn',50),('callReDial',60),('callHold',61),('repeatDialingEnable',62),('repeatDialingCancel',63),('callWaitTempDisable',70),('callWaitPermDisableToggle',71),('callWaitPermanentDisable',72),('callWaitPermanentEnable',73),('callerIDPermBlockToggle',90),('callerIDTempEnable',91),('callerIDTempBlock',92)))
_SipCfgDialFeatName_Type.__name__=_C
_SipCfgDialFeatName_Object=MibTableColumn
sipCfgDialFeatName=_SipCfgDialFeatName_Object((1,3,6,1,4,1,4115,11,1,11,1,2),_SipCfgDialFeatName_Type())
sipCfgDialFeatName.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatName.setStatus(_A)
_SipCfgDialFeatCode_Type=DisplayString
_SipCfgDialFeatCode_Object=MibTableColumn
sipCfgDialFeatCode=_SipCfgDialFeatCode_Object((1,3,6,1,4,1,4115,11,1,11,1,3),_SipCfgDialFeatCode_Type())
sipCfgDialFeatCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatCode.setStatus(_A)
class _SipCfgDialFeatTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),('dialTone',2)))
_SipCfgDialFeatTone_Type.__name__=_C
_SipCfgDialFeatTone_Object=MibTableColumn
sipCfgDialFeatTone=_SipCfgDialFeatTone_Object((1,3,6,1,4,1,4115,11,1,11,1,4),_SipCfgDialFeatTone_Type())
sipCfgDialFeatTone.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatTone.setStatus(_A)
class _SipCfgDialFeatActive_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgDialFeatActive_Type.__name__=_D
_SipCfgDialFeatActive_Object=MibTableColumn
sipCfgDialFeatActive=_SipCfgDialFeatActive_Object((1,3,6,1,4,1,4115,11,1,11,1,5),_SipCfgDialFeatActive_Type())
sipCfgDialFeatActive.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatActive.setStatus(_A)
class _SipCfgDialFeatMode_Type(Bits):namedValues=NamedValues(*(('unused0',0),('unused1',1),('unused2',2),('unused3',3),('unused4',4),('unused5',5),('busy',6),('initialDialing',7)))
_SipCfgDialFeatMode_Type.__name__=_D
_SipCfgDialFeatMode_Object=MibTableColumn
sipCfgDialFeatMode=_SipCfgDialFeatMode_Object((1,3,6,1,4,1,4115,11,1,11,1,6),_SipCfgDialFeatMode_Type())
sipCfgDialFeatMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialFeatMode.setStatus(_A)
class _SipCfgDialProxyMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_SipCfgDialProxyMap_Type.__name__=_l
_SipCfgDialProxyMap_Object=MibScalar
sipCfgDialProxyMap=_SipCfgDialProxyMap_Object((1,3,6,1,4,1,4115,11,1,12),_SipCfgDialProxyMap_Type())
sipCfgDialProxyMap.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyMap.setStatus(_A)
class _SipCfgAlertInfoR0_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR0_Type.__name__=_E
_SipCfgAlertInfoR0_Object=MibScalar
sipCfgAlertInfoR0=_SipCfgAlertInfoR0_Object((1,3,6,1,4,1,4115,11,1,13),_SipCfgAlertInfoR0_Type())
sipCfgAlertInfoR0.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR0.setStatus(_A)
class _SipCfgAlertInfoR1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR1_Type.__name__=_E
_SipCfgAlertInfoR1_Object=MibScalar
sipCfgAlertInfoR1=_SipCfgAlertInfoR1_Object((1,3,6,1,4,1,4115,11,1,14),_SipCfgAlertInfoR1_Type())
sipCfgAlertInfoR1.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR1.setStatus(_A)
class _SipCfgAlertInfoR2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR2_Type.__name__=_E
_SipCfgAlertInfoR2_Object=MibScalar
sipCfgAlertInfoR2=_SipCfgAlertInfoR2_Object((1,3,6,1,4,1,4115,11,1,15),_SipCfgAlertInfoR2_Type())
sipCfgAlertInfoR2.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR2.setStatus(_A)
class _SipCfgAlertInfoR3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR3_Type.__name__=_E
_SipCfgAlertInfoR3_Object=MibScalar
sipCfgAlertInfoR3=_SipCfgAlertInfoR3_Object((1,3,6,1,4,1,4115,11,1,16),_SipCfgAlertInfoR3_Type())
sipCfgAlertInfoR3.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR3.setStatus(_A)
class _SipCfgAlertInfoR4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR4_Type.__name__=_E
_SipCfgAlertInfoR4_Object=MibScalar
sipCfgAlertInfoR4=_SipCfgAlertInfoR4_Object((1,3,6,1,4,1,4115,11,1,17),_SipCfgAlertInfoR4_Type())
sipCfgAlertInfoR4.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR4.setStatus(_A)
class _SipCfgAlertInfoR5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR5_Type.__name__=_E
_SipCfgAlertInfoR5_Object=MibScalar
sipCfgAlertInfoR5=_SipCfgAlertInfoR5_Object((1,3,6,1,4,1,4115,11,1,18),_SipCfgAlertInfoR5_Type())
sipCfgAlertInfoR5.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR5.setStatus(_A)
class _SipCfgAlertInfoR6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR6_Type.__name__=_E
_SipCfgAlertInfoR6_Object=MibScalar
sipCfgAlertInfoR6=_SipCfgAlertInfoR6_Object((1,3,6,1,4,1,4115,11,1,19),_SipCfgAlertInfoR6_Type())
sipCfgAlertInfoR6.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR6.setStatus(_A)
class _SipCfgAlertInfoR7_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgAlertInfoR7_Type.__name__=_E
_SipCfgAlertInfoR7_Object=MibScalar
sipCfgAlertInfoR7=_SipCfgAlertInfoR7_Object((1,3,6,1,4,1,4115,11,1,20),_SipCfgAlertInfoR7_Type())
sipCfgAlertInfoR7.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAlertInfoR7.setStatus(_A)
_SipCfgDomainOverride_Type=DisplayString
_SipCfgDomainOverride_Object=MibScalar
sipCfgDomainOverride=_SipCfgDomainOverride_Object((1,3,6,1,4,1,4115,11,1,21),_SipCfgDomainOverride_Type())
sipCfgDomainOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDomainOverride.setStatus(_A)
class _SipCfgEmergencyNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgEmergencyNumber_Type.__name__=_E
_SipCfgEmergencyNumber_Object=MibScalar
sipCfgEmergencyNumber=_SipCfgEmergencyNumber_Object((1,3,6,1,4,1,4115,11,1,22),_SipCfgEmergencyNumber_Type())
sipCfgEmergencyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgEmergencyNumber.setStatus(_A)
_SipCfgRegTimerMin_Type=Integer32
_SipCfgRegTimerMin_Object=MibScalar
sipCfgRegTimerMin=_SipCfgRegTimerMin_Object((1,3,6,1,4,1,4115,11,1,23),_SipCfgRegTimerMin_Type())
sipCfgRegTimerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegTimerMin.setStatus(_A)
_SipCfgRegTimerMax_Type=Integer32
_SipCfgRegTimerMax_Object=MibScalar
sipCfgRegTimerMax=_SipCfgRegTimerMax_Object((1,3,6,1,4,1,4115,11,1,24),_SipCfgRegTimerMax_Type())
sipCfgRegTimerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegTimerMax.setStatus(_A)
_SipCfgT1_Type=Integer32
_SipCfgT1_Object=MibScalar
sipCfgT1=_SipCfgT1_Object((1,3,6,1,4,1,4115,11,1,25),_SipCfgT1_Type())
sipCfgT1.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgT1.setStatus(_A)
_SipCfgMaxRetrans_Type=Integer32
_SipCfgMaxRetrans_Object=MibScalar
sipCfgMaxRetrans=_SipCfgMaxRetrans_Object((1,3,6,1,4,1,4115,11,1,26),_SipCfgMaxRetrans_Type())
sipCfgMaxRetrans.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMaxRetrans.setStatus(_A)
class _SipCfgMediaLoopbackNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgMediaLoopbackNumber_Type.__name__=_E
_SipCfgMediaLoopbackNumber_Object=MibScalar
sipCfgMediaLoopbackNumber=_SipCfgMediaLoopbackNumber_Object((1,3,6,1,4,1,4115,11,1,27),_SipCfgMediaLoopbackNumber_Type())
sipCfgMediaLoopbackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMediaLoopbackNumber.setStatus(_A)
class _SipCfgPacketLoopbackNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgPacketLoopbackNumber_Type.__name__=_E
_SipCfgPacketLoopbackNumber_Object=MibScalar
sipCfgPacketLoopbackNumber=_SipCfgPacketLoopbackNumber_Object((1,3,6,1,4,1,4115,11,1,28),_SipCfgPacketLoopbackNumber_Type())
sipCfgPacketLoopbackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPacketLoopbackNumber.setStatus(_A)
class _SipCfgBusyDigitMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_SipCfgBusyDigitMap_Type.__name__=_l
_SipCfgBusyDigitMap_Object=MibScalar
sipCfgBusyDigitMap=_SipCfgBusyDigitMap_Object((1,3,6,1,4,1,4115,11,1,29),_SipCfgBusyDigitMap_Type())
sipCfgBusyDigitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgBusyDigitMap.setStatus(_A)
_SipCfgRepeatDialingInterval_Type=Integer32
_SipCfgRepeatDialingInterval_Object=MibScalar
sipCfgRepeatDialingInterval=_SipCfgRepeatDialingInterval_Object((1,3,6,1,4,1,4115,11,1,30),_SipCfgRepeatDialingInterval_Type())
sipCfgRepeatDialingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRepeatDialingInterval.setStatus(_A)
_SipCfgRepeatDialingTimeout_Type=Integer32
_SipCfgRepeatDialingTimeout_Object=MibScalar
sipCfgRepeatDialingTimeout=_SipCfgRepeatDialingTimeout_Object((1,3,6,1,4,1,4115,11,1,31),_SipCfgRepeatDialingTimeout_Type())
sipCfgRepeatDialingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRepeatDialingTimeout.setStatus(_A)
_SipCfgRepeatDialingSessionProgressTimer_Type=Integer32
_SipCfgRepeatDialingSessionProgressTimer_Object=MibScalar
sipCfgRepeatDialingSessionProgressTimer=_SipCfgRepeatDialingSessionProgressTimer_Object((1,3,6,1,4,1,4115,11,1,32),_SipCfgRepeatDialingSessionProgressTimer_Type())
sipCfgRepeatDialingSessionProgressTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRepeatDialingSessionProgressTimer.setStatus(_A)
_SipCfgFeatureCapability_ObjectIdentity=ObjectIdentity
sipCfgFeatureCapability=_SipCfgFeatureCapability_ObjectIdentity((1,3,6,1,4,1,4115,11,1,33))
class _SipCfgCallerIdDisplayCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallerIdDisplayCapability_Type.__name__=_D
_SipCfgCallerIdDisplayCapability_Object=MibScalar
sipCfgCallerIdDisplayCapability=_SipCfgCallerIdDisplayCapability_Object((1,3,6,1,4,1,4115,11,1,33,1),_SipCfgCallerIdDisplayCapability_Type())
sipCfgCallerIdDisplayCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallerIdDisplayCapability.setStatus(_A)
class _SipCfgCallerIdSendCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallerIdSendCapability_Type.__name__=_D
_SipCfgCallerIdSendCapability_Object=MibScalar
sipCfgCallerIdSendCapability=_SipCfgCallerIdSendCapability_Object((1,3,6,1,4,1,4115,11,1,33,2),_SipCfgCallerIdSendCapability_Type())
sipCfgCallerIdSendCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallerIdSendCapability.setStatus(_A)
class _SipCfgAnonCallRejectionCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgAnonCallRejectionCapability_Type.__name__=_D
_SipCfgAnonCallRejectionCapability_Object=MibScalar
sipCfgAnonCallRejectionCapability=_SipCfgAnonCallRejectionCapability_Object((1,3,6,1,4,1,4115,11,1,33,3),_SipCfgAnonCallRejectionCapability_Type())
sipCfgAnonCallRejectionCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAnonCallRejectionCapability.setStatus(_A)
class _SipCfgCallWaitingCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallWaitingCapability_Type.__name__=_D
_SipCfgCallWaitingCapability_Object=MibScalar
sipCfgCallWaitingCapability=_SipCfgCallWaitingCapability_Object((1,3,6,1,4,1,4115,11,1,33,4),_SipCfgCallWaitingCapability_Type())
sipCfgCallWaitingCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallWaitingCapability.setStatus(_A)
class _SipCfgThreeWayCallCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgThreeWayCallCapability_Type.__name__=_D
_SipCfgThreeWayCallCapability_Object=MibScalar
sipCfgThreeWayCallCapability=_SipCfgThreeWayCallCapability_Object((1,3,6,1,4,1,4115,11,1,33,5),_SipCfgThreeWayCallCapability_Type())
sipCfgThreeWayCallCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgThreeWayCallCapability.setStatus(_A)
class _SipCfgCallTransferCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallTransferCapability_Type.__name__=_D
_SipCfgCallTransferCapability_Object=MibScalar
sipCfgCallTransferCapability=_SipCfgCallTransferCapability_Object((1,3,6,1,4,1,4115,11,1,33,6),_SipCfgCallTransferCapability_Type())
sipCfgCallTransferCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallTransferCapability.setStatus(_A)
class _SipCfgCallForwardCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallForwardCapability_Type.__name__=_D
_SipCfgCallForwardCapability_Object=MibScalar
sipCfgCallForwardCapability=_SipCfgCallForwardCapability_Object((1,3,6,1,4,1,4115,11,1,33,7),_SipCfgCallForwardCapability_Type())
sipCfgCallForwardCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallForwardCapability.setStatus(_A)
class _SipCfgCallReturnCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallReturnCapability_Type.__name__=_D
_SipCfgCallReturnCapability_Object=MibScalar
sipCfgCallReturnCapability=_SipCfgCallReturnCapability_Object((1,3,6,1,4,1,4115,11,1,33,8),_SipCfgCallReturnCapability_Type())
sipCfgCallReturnCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallReturnCapability.setStatus(_A)
class _SipCfgCallRedialCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallRedialCapability_Type.__name__=_D
_SipCfgCallRedialCapability_Object=MibScalar
sipCfgCallRedialCapability=_SipCfgCallRedialCapability_Object((1,3,6,1,4,1,4115,11,1,33,9),_SipCfgCallRedialCapability_Type())
sipCfgCallRedialCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallRedialCapability.setStatus(_A)
class _SipCfgCallHoldCapability_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgCallHoldCapability_Type.__name__=_D
_SipCfgCallHoldCapability_Object=MibScalar
sipCfgCallHoldCapability=_SipCfgCallHoldCapability_Object((1,3,6,1,4,1,4115,11,1,33,10),_SipCfgCallHoldCapability_Type())
sipCfgCallHoldCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallHoldCapability.setStatus(_A)
class _SipCfgProxyDigitMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_SipCfgProxyDigitMap_Type.__name__=_l
_SipCfgProxyDigitMap_Object=MibScalar
sipCfgProxyDigitMap=_SipCfgProxyDigitMap_Object((1,3,6,1,4,1,4115,11,1,34),_SipCfgProxyDigitMap_Type())
sipCfgProxyDigitMap.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProxyDigitMap.setStatus(_A)
class _SipCfgCallWaitingStarCodeSurvivesReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_SipCfgCallWaitingStarCodeSurvivesReset_Type.__name__=_C
_SipCfgCallWaitingStarCodeSurvivesReset_Object=MibScalar
sipCfgCallWaitingStarCodeSurvivesReset=_SipCfgCallWaitingStarCodeSurvivesReset_Object((1,3,6,1,4,1,4115,11,1,35),_SipCfgCallWaitingStarCodeSurvivesReset_Type())
sipCfgCallWaitingStarCodeSurvivesReset.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallWaitingStarCodeSurvivesReset.setStatus(_A)
class _SipCfgResetCallWaitingStarCode_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgResetCallWaitingStarCode_Type.__name__=_D
_SipCfgResetCallWaitingStarCode_Object=MibScalar
sipCfgResetCallWaitingStarCode=_SipCfgResetCallWaitingStarCode_Object((1,3,6,1,4,1,4115,11,1,36),_SipCfgResetCallWaitingStarCode_Type())
sipCfgResetCallWaitingStarCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgResetCallWaitingStarCode.setStatus(_A)
_SipCfgDialProxyTable_Object=MibTable
sipCfgDialProxyTable=_SipCfgDialProxyTable_Object((1,3,6,1,4,1,4115,11,1,37))
if mibBuilder.loadTexts:sipCfgDialProxyTable.setStatus(_A)
_SipCfgDialProxyEntry_Object=MibTableRow
sipCfgDialProxyEntry=_SipCfgDialProxyEntry_Object((1,3,6,1,4,1,4115,11,1,37,1))
sipCfgDialProxyEntry.setIndexNames((0,_o,_A0))
if mibBuilder.loadTexts:sipCfgDialProxyEntry.setStatus(_A)
_SipCfgDialProxyNumber_Type=Integer32
_SipCfgDialProxyNumber_Object=MibTableColumn
sipCfgDialProxyNumber=_SipCfgDialProxyNumber_Object((1,3,6,1,4,1,4115,11,1,37,1,1),_SipCfgDialProxyNumber_Type())
sipCfgDialProxyNumber.setMaxAccess(_q)
if mibBuilder.loadTexts:sipCfgDialProxyNumber.setStatus(_A)
_SipCfgDialProxyCode_Type=DisplayString
_SipCfgDialProxyCode_Object=MibTableColumn
sipCfgDialProxyCode=_SipCfgDialProxyCode_Object((1,3,6,1,4,1,4115,11,1,37,1,2),_SipCfgDialProxyCode_Type())
sipCfgDialProxyCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyCode.setStatus(_A)
class _SipCfgDialProxyTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),('dialTone',2)))
_SipCfgDialProxyTone_Type.__name__=_C
_SipCfgDialProxyTone_Object=MibTableColumn
sipCfgDialProxyTone=_SipCfgDialProxyTone_Object((1,3,6,1,4,1,4115,11,1,37,1,3),_SipCfgDialProxyTone_Type())
sipCfgDialProxyTone.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyTone.setStatus(_A)
class _SipCfgDialProxyActive_Type(Bits):namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),(_k,31)))
_SipCfgDialProxyActive_Type.__name__=_D
_SipCfgDialProxyActive_Object=MibTableColumn
sipCfgDialProxyActive=_SipCfgDialProxyActive_Object((1,3,6,1,4,1,4115,11,1,37,1,4),_SipCfgDialProxyActive_Type())
sipCfgDialProxyActive.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyActive.setStatus(_A)
class _SipCfgDialProxyMessageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('invite',1),('refer',2)))
_SipCfgDialProxyMessageType_Type.__name__=_C
_SipCfgDialProxyMessageType_Object=MibTableColumn
sipCfgDialProxyMessageType=_SipCfgDialProxyMessageType_Object((1,3,6,1,4,1,4115,11,1,37,1,5),_SipCfgDialProxyMessageType_Type())
sipCfgDialProxyMessageType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyMessageType.setStatus(_A)
class _SipCfgDialProxyMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('default',0),('pc20',1)))
_SipCfgDialProxyMethod_Type.__name__=_C
_SipCfgDialProxyMethod_Object=MibTableColumn
sipCfgDialProxyMethod=_SipCfgDialProxyMethod_Object((1,3,6,1,4,1,4115,11,1,37,1,6),_SipCfgDialProxyMethod_Type())
sipCfgDialProxyMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyMethod.setStatus(_A)
_SipCfgDialProxyMethodDelimiter_Type=DisplayString
_SipCfgDialProxyMethodDelimiter_Object=MibTableColumn
sipCfgDialProxyMethodDelimiter=_SipCfgDialProxyMethodDelimiter_Object((1,3,6,1,4,1,4115,11,1,37,1,7),_SipCfgDialProxyMethodDelimiter_Type())
sipCfgDialProxyMethodDelimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDialProxyMethodDelimiter.setStatus(_A)
class _SipCfgDhcp60AnnouncementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_SipCfgDhcp60AnnouncementMode_Type.__name__=_C
_SipCfgDhcp60AnnouncementMode_Object=MibScalar
sipCfgDhcp60AnnouncementMode=_SipCfgDhcp60AnnouncementMode_Object((1,3,6,1,4,1,4115,11,1,38),_SipCfgDhcp60AnnouncementMode_Type())
sipCfgDhcp60AnnouncementMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDhcp60AnnouncementMode.setStatus(_A)
class _SipCfgCallForwardForbiddenNumbers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SipCfgCallForwardForbiddenNumbers_Type.__name__=_E
_SipCfgCallForwardForbiddenNumbers_Object=MibScalar
sipCfgCallForwardForbiddenNumbers=_SipCfgCallForwardForbiddenNumbers_Object((1,3,6,1,4,1,4115,11,1,39),_SipCfgCallForwardForbiddenNumbers_Type())
sipCfgCallForwardForbiddenNumbers.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCallForwardForbiddenNumbers.setStatus(_A)
class _SipCfgDefaultG711_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8)));namedValues=NamedValues(*(('pcmu',0),('pcma',8)))
_SipCfgDefaultG711_Type.__name__=_C
_SipCfgDefaultG711_Object=MibScalar
sipCfgDefaultG711=_SipCfgDefaultG711_Object((1,3,6,1,4,1,4115,11,1,40),_SipCfgDefaultG711_Type())
sipCfgDefaultG711.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDefaultG711.setStatus(_A)
_SipCfgGenLinger_Type=Integer32
_SipCfgGenLinger_Object=MibScalar
sipCfgGenLinger=_SipCfgGenLinger_Object((1,3,6,1,4,1,4115,11,1,41),_SipCfgGenLinger_Type())
sipCfgGenLinger.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgGenLinger.setStatus(_A)
_SipCfgInviteLinger_Type=Integer32
_SipCfgInviteLinger_Object=MibScalar
sipCfgInviteLinger=_SipCfgInviteLinger_Object((1,3,6,1,4,1,4115,11,1,42),_SipCfgInviteLinger_Type())
sipCfgInviteLinger.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgInviteLinger.setStatus(_A)
_SipCfgTimerB_Type=Integer32
_SipCfgTimerB_Object=MibScalar
sipCfgTimerB=_SipCfgTimerB_Object((1,3,6,1,4,1,4115,11,1,43),_SipCfgTimerB_Type())
sipCfgTimerB.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgTimerB.setStatus(_A)
_SipCfgTimerF_Type=Integer32
_SipCfgTimerF_Object=MibScalar
sipCfgTimerF=_SipCfgTimerF_Object((1,3,6,1,4,1,4115,11,1,44),_SipCfgTimerF_Type())
sipCfgTimerF.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgTimerF.setStatus(_A)
_SipCfgRegExpires_Type=Integer32
_SipCfgRegExpires_Object=MibScalar
sipCfgRegExpires=_SipCfgRegExpires_Object((1,3,6,1,4,1,4115,11,1,45),_SipCfgRegExpires_Type())
sipCfgRegExpires.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegExpires.setStatus(_A)
_SipCfgMaxUDPSize_Type=Integer32
_SipCfgMaxUDPSize_Object=MibScalar
sipCfgMaxUDPSize=_SipCfgMaxUDPSize_Object((1,3,6,1,4,1,4115,11,1,46),_SipCfgMaxUDPSize_Type())
sipCfgMaxUDPSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMaxUDPSize.setStatus(_A)
_SipCfgSessionExpires_Type=Integer32
_SipCfgSessionExpires_Object=MibScalar
sipCfgSessionExpires=_SipCfgSessionExpires_Object((1,3,6,1,4,1,4115,11,1,47),_SipCfgSessionExpires_Type())
sipCfgSessionExpires.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSessionExpires.setStatus(_A)
_SipCfgPenaltyBoxTimeout_Type=Integer32
_SipCfgPenaltyBoxTimeout_Object=MibScalar
sipCfgPenaltyBoxTimeout=_SipCfgPenaltyBoxTimeout_Object((1,3,6,1,4,1,4115,11,1,48),_SipCfgPenaltyBoxTimeout_Type())
sipCfgPenaltyBoxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPenaltyBoxTimeout.setStatus(_A)
class _SipCfgDisconnectReorderToneDelay_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_SipCfgDisconnectReorderToneDelay_Type.__name__=_n
_SipCfgDisconnectReorderToneDelay_Object=MibScalar
sipCfgDisconnectReorderToneDelay=_SipCfgDisconnectReorderToneDelay_Object((1,3,6,1,4,1,4115,11,1,49),_SipCfgDisconnectReorderToneDelay_Type())
sipCfgDisconnectReorderToneDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDisconnectReorderToneDelay.setStatus(_A)
class _SipCfgDistinctiveRingingForCallHold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('standard',0),('r0',1),('r1',2),('r2',3),('r3',4),('r4',5),('r5',6),('r6',7),('r7',8)))
_SipCfgDistinctiveRingingForCallHold_Type.__name__=_C
_SipCfgDistinctiveRingingForCallHold_Object=MibScalar
sipCfgDistinctiveRingingForCallHold=_SipCfgDistinctiveRingingForCallHold_Object((1,3,6,1,4,1,4115,11,1,50),_SipCfgDistinctiveRingingForCallHold_Type())
sipCfgDistinctiveRingingForCallHold.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgDistinctiveRingingForCallHold.setStatus(_A)
class _SipCfgSipFeatureSwitch2_Type(Bits):defaultHexValue=_t;namedValues=NamedValues(*(('pwdAutoGen',0),('sipFailover',1),('commonNonce',2),('unused3',3),('noRegOffhook',4),('perLineImpi',5),('dnsCache',6),('optDstTimezone',7),('rejectInviteWith480',8),('perLineProxySelection',9),('suppressTIASInSDP',10),('addRouteHeaderToInitialRegMsg',11),('dropInProgressCallsOnReregFailure',12),('byeRejectedErrorHandling',13),('strictMessageValidation',14),('directStatsPublish',15),('suppressUserphoneUrlParam',16),('useDomainNameAsPcscfAddr',17),('addPAccessNetworkInfoHeader',18),('addPAccessNetworkInfoHeaderCancel',19),('regUponNetworkRecovery',20),('deregisterLineEnable',21),('appendLocalIpAddressToCallid',22),('sessionTimerNegotiationEnable',23),('ignoreStandAloneMessage',24),('addAuthHeaderAfterChallenge',25),('hideRealTnInContactHeader',26),('inviteErrorHandlingEnhancement',27),('useDomainNameInRouteHeader',28),('unsubMwiDuringFailover',29),('serviceCapability',30),('useMTAIpInContactHeader',31)))
_SipCfgSipFeatureSwitch2_Type.__name__=_D
_SipCfgSipFeatureSwitch2_Object=MibScalar
sipCfgSipFeatureSwitch2=_SipCfgSipFeatureSwitch2_Object((1,3,6,1,4,1,4115,11,1,51),_SipCfgSipFeatureSwitch2_Type())
sipCfgSipFeatureSwitch2.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSipFeatureSwitch2.setStatus(_A)
class _SipCfgAuthPasswordKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SipCfgAuthPasswordKey_Type.__name__=_l
_SipCfgAuthPasswordKey_Object=MibScalar
sipCfgAuthPasswordKey=_SipCfgAuthPasswordKey_Object((1,3,6,1,4,1,4115,11,1,52),_SipCfgAuthPasswordKey_Type())
sipCfgAuthPasswordKey.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgAuthPasswordKey.setStatus(_A)
_SipCfgMWITargetAddrType_Type=InetAddressType
_SipCfgMWITargetAddrType_Object=MibScalar
sipCfgMWITargetAddrType=_SipCfgMWITargetAddrType_Object((1,3,6,1,4,1,4115,11,1,53),_SipCfgMWITargetAddrType_Type())
sipCfgMWITargetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMWITargetAddrType.setStatus(_A)
_SipCfgMWITargetAddr_Type=InetAddress
_SipCfgMWITargetAddr_Object=MibScalar
sipCfgMWITargetAddr=_SipCfgMWITargetAddr_Object((1,3,6,1,4,1,4115,11,1,54),_SipCfgMWITargetAddr_Type())
sipCfgMWITargetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMWITargetAddr.setStatus(_A)
class _SipCfgMWITargetPort_Type(Unsigned32):defaultValue=5060
_SipCfgMWITargetPort_Type.__name__=_n
_SipCfgMWITargetPort_Object=MibScalar
sipCfgMWITargetPort=_SipCfgMWITargetPort_Object((1,3,6,1,4,1,4115,11,1,55),_SipCfgMWITargetPort_Type())
sipCfgMWITargetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMWITargetPort.setStatus(_A)
_SipCfgEmergencyServiceURN_Type=DisplayString
_SipCfgEmergencyServiceURN_Object=MibScalar
sipCfgEmergencyServiceURN=_SipCfgEmergencyServiceURN_Object((1,3,6,1,4,1,4115,11,1,56),_SipCfgEmergencyServiceURN_Type())
sipCfgEmergencyServiceURN.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgEmergencyServiceURN.setStatus(_A)
class _SipCfgSubsAlertTimeout_Type(Unsigned32):defaultValue=60
_SipCfgSubsAlertTimeout_Type.__name__=_n
_SipCfgSubsAlertTimeout_Object=MibScalar
sipCfgSubsAlertTimeout=_SipCfgSubsAlertTimeout_Object((1,3,6,1,4,1,4115,11,1,57),_SipCfgSubsAlertTimeout_Type())
sipCfgSubsAlertTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSubsAlertTimeout.setStatus(_A)
_SipCfgProvisionalTimer_Type=Unsigned32
_SipCfgProvisionalTimer_Object=MibScalar
sipCfgProvisionalTimer=_SipCfgProvisionalTimer_Object((1,3,6,1,4,1,4115,11,1,58),_SipCfgProvisionalTimer_Type())
sipCfgProvisionalTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProvisionalTimer.setStatus(_A)
class _SipCfg3WCWaitHookHoldTimer_Type(Unsigned32):defaultValue=0
_SipCfg3WCWaitHookHoldTimer_Type.__name__=_n
_SipCfg3WCWaitHookHoldTimer_Object=MibScalar
sipCfg3WCWaitHookHoldTimer=_SipCfg3WCWaitHookHoldTimer_Object((1,3,6,1,4,1,4115,11,1,59),_SipCfg3WCWaitHookHoldTimer_Type())
sipCfg3WCWaitHookHoldTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfg3WCWaitHookHoldTimer.setStatus(_A)
_SipCfgWaitHookHoldTone_Type=DisplayString
_SipCfgWaitHookHoldTone_Object=MibScalar
sipCfgWaitHookHoldTone=_SipCfgWaitHookHoldTone_Object((1,3,6,1,4,1,4115,11,1,60),_SipCfgWaitHookHoldTone_Type())
sipCfgWaitHookHoldTone.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgWaitHookHoldTone.setStatus(_A)
_SipCfgMinSE_Type=Integer32
_SipCfgMinSE_Object=MibScalar
sipCfgMinSE=_SipCfgMinSE_Object((1,3,6,1,4,1,4115,11,1,61),_SipCfgMinSE_Type())
sipCfgMinSE.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMinSE.setStatus(_A)
class _SipCfgInDialogRefer_Type(TruthValue):defaultValue=2
_SipCfgInDialogRefer_Type.__name__=_m
_SipCfgInDialogRefer_Object=MibScalar
sipCfgInDialogRefer=_SipCfgInDialogRefer_Object((1,3,6,1,4,1,4115,11,1,62),_SipCfgInDialogRefer_Type())
sipCfgInDialogRefer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgInDialogRefer.setStatus(_A)
class _SipCfgFailoverSwitch_Type(Bits):defaultHexValue=_t;namedValues=NamedValues(*(('invite',0),('cancel',1),('bye',2),('update',3),('publish',4),('refer',5),('notify',6),('subscribe',7),('unused8',8),('unused9',9),('unused10',10),('unused11',11),('unused12',12),('unused13',13),('unused14',14),('unused15',15),('unused16',16),('unused17',17),('unused18',18),('unused19',19),('unused20',20),('unused21',21),('unused22',22),('unused23',23),('unused24',24),('unused25',25),('unused26',26),('unused27',27),('unused28',28),('unused29',29),('unused30',30),('unused31',31)))
_SipCfgFailoverSwitch_Type.__name__=_D
_SipCfgFailoverSwitch_Object=MibScalar
sipCfgFailoverSwitch=_SipCfgFailoverSwitch_Object((1,3,6,1,4,1,4115,11,1,63),_SipCfgFailoverSwitch_Type())
sipCfgFailoverSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgFailoverSwitch.setStatus(_A)
class _SipCfgSubsRetryTimeout_Type(Unsigned32):defaultValue=600
_SipCfgSubsRetryTimeout_Type.__name__=_n
_SipCfgSubsRetryTimeout_Object=MibScalar
sipCfgSubsRetryTimeout=_SipCfgSubsRetryTimeout_Object((1,3,6,1,4,1,4115,11,1,64),_SipCfgSubsRetryTimeout_Type())
sipCfgSubsRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSubsRetryTimeout.setStatus(_A)
class _SipCfgPAccessNetworkInfoHeaderValue_Type(OctetString):defaultValue=OctetString('DOCSIS');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SipCfgPAccessNetworkInfoHeaderValue_Type.__name__=_l
_SipCfgPAccessNetworkInfoHeaderValue_Object=MibScalar
sipCfgPAccessNetworkInfoHeaderValue=_SipCfgPAccessNetworkInfoHeaderValue_Object((1,3,6,1,4,1,4115,11,1,65),_SipCfgPAccessNetworkInfoHeaderValue_Type())
sipCfgPAccessNetworkInfoHeaderValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgPAccessNetworkInfoHeaderValue.setStatus(_A)
class _SipCfgTermOffHookProcessingDelay_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_SipCfgTermOffHookProcessingDelay_Type.__name__=_n
_SipCfgTermOffHookProcessingDelay_Object=MibScalar
sipCfgTermOffHookProcessingDelay=_SipCfgTermOffHookProcessingDelay_Object((1,3,6,1,4,1,4115,11,1,66),_SipCfgTermOffHookProcessingDelay_Type())
sipCfgTermOffHookProcessingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgTermOffHookProcessingDelay.setStatus(_A)
_SipCfgT2_Type=Integer32
_SipCfgT2_Object=MibScalar
sipCfgT2=_SipCfgT2_Object((1,3,6,1,4,1,4115,11,1,67),_SipCfgT2_Type())
sipCfgT2.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgT2.setStatus(_A)
class _SipCfgRegInterval_Type(Integer32):defaultValue=0
_SipCfgRegInterval_Type.__name__=_C
_SipCfgRegInterval_Object=MibScalar
sipCfgRegInterval=_SipCfgRegInterval_Object((1,3,6,1,4,1,4115,11,1,68),_SipCfgRegInterval_Type())
sipCfgRegInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegInterval.setStatus(_A)
class _SipCfgOnhookDelayTimer_Type(Integer32):defaultValue=0
_SipCfgOnhookDelayTimer_Type.__name__=_C
_SipCfgOnhookDelayTimer_Object=MibScalar
sipCfgOnhookDelayTimer=_SipCfgOnhookDelayTimer_Object((1,3,6,1,4,1,4115,11,1,69),_SipCfgOnhookDelayTimer_Type())
sipCfgOnhookDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgOnhookDelayTimer.setStatus(_A)
_SipCfgNetConfFactoryUri_Type=DisplayString
_SipCfgNetConfFactoryUri_Object=MibScalar
sipCfgNetConfFactoryUri=_SipCfgNetConfFactoryUri_Object((1,3,6,1,4,1,4115,11,1,70),_SipCfgNetConfFactoryUri_Type())
sipCfgNetConfFactoryUri.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgNetConfFactoryUri.setStatus(_A)
class _SipCfgSipFeatureSwitch3_Type(Bits):defaultHexValue=_t;namedValues=NamedValues(*(('publishTimestampsDST',0),('playRtpForSecond183WithoutSdp',1),('addSipInstanceToContact',2),('notPopulateFirstPAURIFrom200OK',3),('judgeSDPWhileReturnFalse',4),('tcpFailTryUDP',5),('reuseTCPConnection',6),('sdpEndsWithEmptyLine0x0d0a',7),('doNotRedirect3xxResponseForInvite',8),('pcscfWhiteList',9),('processUnsolicitedNotifyForRegEvent',10),('prependZerosToCIDDisplayNumber',11),('terminateConnBeforeInForkCallFlow',12),('unused13',13),('unused14',14),('unused15',15),('unused16',16),('unused17',17),('unused18',18),('unused19',19),('unused20',20),('unused21',21),('unused22',22),('unused23',23),('unused24',24),('unused25',25),('unused26',26),('unused27',27),('unused28',28),('unused29',29),('unused30',30),('unused31',31)))
_SipCfgSipFeatureSwitch3_Type.__name__=_D
_SipCfgSipFeatureSwitch3_Object=MibScalar
sipCfgSipFeatureSwitch3=_SipCfgSipFeatureSwitch3_Object((1,3,6,1,4,1,4115,11,1,71),_SipCfgSipFeatureSwitch3_Type())
sipCfgSipFeatureSwitch3.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgSipFeatureSwitch3.setStatus(_A)
class _SipCfgRegisterOnExpire_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_SipCfgRegisterOnExpire_Type.__name__=_C
_SipCfgRegisterOnExpire_Object=MibScalar
sipCfgRegisterOnExpire=_SipCfgRegisterOnExpire_Object((1,3,6,1,4,1,4115,11,1,72),_SipCfgRegisterOnExpire_Type())
sipCfgRegisterOnExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgRegisterOnExpire.setStatus(_A)
_SipCfgServiceCapabilities_Type=DisplayString
_SipCfgServiceCapabilities_Object=MibScalar
sipCfgServiceCapabilities=_SipCfgServiceCapabilities_Object((1,3,6,1,4,1,4115,11,1,73),_SipCfgServiceCapabilities_Type())
sipCfgServiceCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgServiceCapabilities.setStatus(_A)
_SipCfgCIDDisDSTInfo_Type=SnmpAdminString
_SipCfgCIDDisDSTInfo_Object=MibScalar
sipCfgCIDDisDSTInfo=_SipCfgCIDDisDSTInfo_Object((1,3,6,1,4,1,4115,11,1,74),_SipCfgCIDDisDSTInfo_Type())
sipCfgCIDDisDSTInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgCIDDisDSTInfo.setStatus(_A)
_SipCfgProtectedDnList_Type=DisplayString
_SipCfgProtectedDnList_Object=MibScalar
sipCfgProtectedDnList=_SipCfgProtectedDnList_Object((1,3,6,1,4,1,4115,11,1,75),_SipCfgProtectedDnList_Type())
sipCfgProtectedDnList.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgProtectedDnList.setStatus(_A)
class _SipCfgUnsetDontFragmentBit_Type(TruthValue):defaultValue=2
_SipCfgUnsetDontFragmentBit_Type.__name__=_m
_SipCfgUnsetDontFragmentBit_Object=MibScalar
sipCfgUnsetDontFragmentBit=_SipCfgUnsetDontFragmentBit_Object((1,3,6,1,4,1,4115,11,1,76),_SipCfgUnsetDontFragmentBit_Type())
sipCfgUnsetDontFragmentBit.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgUnsetDontFragmentBit.setStatus(_A)
_SipCfgMWISubscriptionCheckInterval_Type=Integer32
_SipCfgMWISubscriptionCheckInterval_Object=MibScalar
sipCfgMWISubscriptionCheckInterval=_SipCfgMWISubscriptionCheckInterval_Object((1,3,6,1,4,1,4115,11,1,77),_SipCfgMWISubscriptionCheckInterval_Type())
sipCfgMWISubscriptionCheckInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sipCfgMWISubscriptionCheckInterval.setStatus(_A)
_SipStatus_ObjectIdentity=ObjectIdentity
sipStatus=_SipStatus_ObjectIdentity((1,3,6,1,4,1,4115,11,2))
_SipStatusPortTable_Object=MibTable
sipStatusPortTable=_SipStatusPortTable_Object((1,3,6,1,4,1,4115,11,2,1))
if mibBuilder.loadTexts:sipStatusPortTable.setStatus(_A)
_SipStatusPortEntry_Object=MibTableRow
sipStatusPortEntry=_SipStatusPortEntry_Object((1,3,6,1,4,1,4115,11,2,1,1))
sipStatusPortEntry.setIndexNames((0,_o,_A1))
if mibBuilder.loadTexts:sipStatusPortEntry.setStatus(_A)
_SipStatusPortPortNumber_Type=Integer32
_SipStatusPortPortNumber_Object=MibTableColumn
sipStatusPortPortNumber=_SipStatusPortPortNumber_Object((1,3,6,1,4,1,4115,11,2,1,1,1),_SipStatusPortPortNumber_Type())
sipStatusPortPortNumber.setMaxAccess(_q)
if mibBuilder.loadTexts:sipStatusPortPortNumber.setStatus(_A)
class _SipStatusAlarms_Type(Bits):namedValues=NamedValues(*(('unused',0),('generalErrorAlrm',1),('networkErrorAlrm',2),('callLegSentAuth',3),('regClientSentAuthReq',4),('authFailAlrm',5),('registrarLocAlrm',6),('proxyLocAlrm',7)))
_SipStatusAlarms_Type.__name__=_D
_SipStatusAlarms_Object=MibTableColumn
sipStatusAlarms=_SipStatusAlarms_Object((1,3,6,1,4,1,4115,11,2,1,1,2),_SipStatusAlarms_Type())
sipStatusAlarms.setMaxAccess(_s)
if mibBuilder.loadTexts:sipStatusAlarms.setStatus(_A)
_SipStatusPortMWISubscribed_Type=TruthValue
_SipStatusPortMWISubscribed_Object=MibTableColumn
sipStatusPortMWISubscribed=_SipStatusPortMWISubscribed_Object((1,3,6,1,4,1,4115,11,2,1,1,3),_SipStatusPortMWISubscribed_Type())
sipStatusPortMWISubscribed.setMaxAccess(_s)
if mibBuilder.loadTexts:sipStatusPortMWISubscribed.setStatus(_A)
_ArrisSipIPv6Mib_ObjectIdentity=ObjectIdentity
arrisSipIPv6Mib=_ArrisSipIPv6Mib_ObjectIdentity((1,3,6,1,4,1,4115,11,4))
class _ArrisSipIPv6MaxUDPSize_Type(Integer32):defaultValue=1280
_ArrisSipIPv6MaxUDPSize_Type.__name__=_C
_ArrisSipIPv6MaxUDPSize_Object=MibScalar
arrisSipIPv6MaxUDPSize=_ArrisSipIPv6MaxUDPSize_Object((1,3,6,1,4,1,4115,11,4,1),_ArrisSipIPv6MaxUDPSize_Type())
arrisSipIPv6MaxUDPSize.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSipIPv6MaxUDPSize.setStatus(_A)
class _ArrisSipIPv6IpPreferenceOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('dhcp',0),(_p,1),('ipv6',2),('ipv4SecIpv6',3),('ipv6SecIpv4',4),('ipv6BypassDssid',5)))
_ArrisSipIPv6IpPreferenceOverride_Type.__name__=_C
_ArrisSipIPv6IpPreferenceOverride_Object=MibScalar
arrisSipIPv6IpPreferenceOverride=_ArrisSipIPv6IpPreferenceOverride_Object((1,3,6,1,4,1,4115,11,4,2),_ArrisSipIPv6IpPreferenceOverride_Type())
arrisSipIPv6IpPreferenceOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisSipIPv6IpPreferenceOverride.setStatus(_A)
mibBuilder.exportSymbols(_o,**{'arrisSipMib':arrisSipMib,'sipConfiguration':sipConfiguration,'sipCfgPortTable':sipCfgPortTable,'sipCfgPortEntry':sipCfgPortEntry,_u:sipCfgPortPortNumber,'sipCfgPortUserName':sipCfgPortUserName,'sipCfgPortDisplayName':sipCfgPortDisplayName,'sipCfgPortLogin':sipCfgPortLogin,'sipCfgPortPassword':sipCfgPortPassword,'sipCfgPortWarmOrHotlineNumber':sipCfgPortWarmOrHotlineNumber,'sipCfgPortWarmLineTimeout':sipCfgPortWarmLineTimeout,'sipCfgPortRegistrarAdr':sipCfgPortRegistrarAdr,'sipCfgPortRegistrarPort':sipCfgPortRegistrarPort,'sipCfgPortRegistrarType':sipCfgPortRegistrarType,'sipCfgPortProxyAdr':sipCfgPortProxyAdr,'sipCfgPortProxyPort':sipCfgPortProxyPort,'sipCfgPortProxyType':sipCfgPortProxyType,'sipCfgPortFeatureSettings':sipCfgPortFeatureSettings,'sipCfgPortT38Mode':sipCfgPortT38Mode,'sipCfgPortFaxOnlyTimeout':sipCfgPortFaxOnlyTimeout,'sipCfgPortMaxT38HSRedLevel':sipCfgPortMaxT38HSRedLevel,'sipCfgPortCallByeDelay':sipCfgPortCallByeDelay,'sipCfgPortMWIClear':sipCfgPortMWIClear,'sipCfgPortMWIVisualEnable':sipCfgPortMWIVisualEnable,'sipCfgPortMWIToneEnable':sipCfgPortMWIToneEnable,'sipCfgPortWarmOrHotlineEnable':sipCfgPortWarmOrHotlineEnable,'sipCfgPortDndRingReminderEnable':sipCfgPortDndRingReminderEnable,'sipCfgPortLoopReversal':sipCfgPortLoopReversal,'sipCfgPortCurrentProxy':sipCfgPortCurrentProxy,'sipCfgPortPrimaryProxy':sipCfgPortPrimaryProxy,'sipCfgPortCallWaitingPermanentDisable':sipCfgPortCallWaitingPermanentDisable,'sipCfgPortCallerIDCallWaitingPermanentDisable':sipCfgPortCallerIDCallWaitingPermanentDisable,'sipCfgDigitMap':sipCfgDigitMap,'sipCfgProxyAdr':sipCfgProxyAdr,'sipCfgProxyType':sipCfgProxyType,'sipCfgRegistrarAdr':sipCfgRegistrarAdr,'sipCfgRegistrarType':sipCfgRegistrarType,'sipCfgSipFeatureSwitch':sipCfgSipFeatureSwitch,'sipCfgProvisionedCodecArray':sipCfgProvisionedCodecArray,'sipCfgPacketizationRate':sipCfgPacketizationRate,'sipCfgDialFeatMap':sipCfgDialFeatMap,'sipCfgDialFeatTable':sipCfgDialFeatTable,'sipCfgDialFeatEntry':sipCfgDialFeatEntry,_y:sipCfgDialFeatNumber,'sipCfgDialFeatName':sipCfgDialFeatName,'sipCfgDialFeatCode':sipCfgDialFeatCode,'sipCfgDialFeatTone':sipCfgDialFeatTone,'sipCfgDialFeatActive':sipCfgDialFeatActive,'sipCfgDialFeatMode':sipCfgDialFeatMode,'sipCfgDialProxyMap':sipCfgDialProxyMap,'sipCfgAlertInfoR0':sipCfgAlertInfoR0,'sipCfgAlertInfoR1':sipCfgAlertInfoR1,'sipCfgAlertInfoR2':sipCfgAlertInfoR2,'sipCfgAlertInfoR3':sipCfgAlertInfoR3,'sipCfgAlertInfoR4':sipCfgAlertInfoR4,'sipCfgAlertInfoR5':sipCfgAlertInfoR5,'sipCfgAlertInfoR6':sipCfgAlertInfoR6,'sipCfgAlertInfoR7':sipCfgAlertInfoR7,'sipCfgDomainOverride':sipCfgDomainOverride,'sipCfgEmergencyNumber':sipCfgEmergencyNumber,'sipCfgRegTimerMin':sipCfgRegTimerMin,'sipCfgRegTimerMax':sipCfgRegTimerMax,'sipCfgT1':sipCfgT1,'sipCfgMaxRetrans':sipCfgMaxRetrans,'sipCfgMediaLoopbackNumber':sipCfgMediaLoopbackNumber,'sipCfgPacketLoopbackNumber':sipCfgPacketLoopbackNumber,'sipCfgBusyDigitMap':sipCfgBusyDigitMap,'sipCfgRepeatDialingInterval':sipCfgRepeatDialingInterval,'sipCfgRepeatDialingTimeout':sipCfgRepeatDialingTimeout,'sipCfgRepeatDialingSessionProgressTimer':sipCfgRepeatDialingSessionProgressTimer,'sipCfgFeatureCapability':sipCfgFeatureCapability,'sipCfgCallerIdDisplayCapability':sipCfgCallerIdDisplayCapability,'sipCfgCallerIdSendCapability':sipCfgCallerIdSendCapability,'sipCfgAnonCallRejectionCapability':sipCfgAnonCallRejectionCapability,'sipCfgCallWaitingCapability':sipCfgCallWaitingCapability,'sipCfgThreeWayCallCapability':sipCfgThreeWayCallCapability,'sipCfgCallTransferCapability':sipCfgCallTransferCapability,'sipCfgCallForwardCapability':sipCfgCallForwardCapability,'sipCfgCallReturnCapability':sipCfgCallReturnCapability,'sipCfgCallRedialCapability':sipCfgCallRedialCapability,'sipCfgCallHoldCapability':sipCfgCallHoldCapability,'sipCfgProxyDigitMap':sipCfgProxyDigitMap,'sipCfgCallWaitingStarCodeSurvivesReset':sipCfgCallWaitingStarCodeSurvivesReset,'sipCfgResetCallWaitingStarCode':sipCfgResetCallWaitingStarCode,'sipCfgDialProxyTable':sipCfgDialProxyTable,'sipCfgDialProxyEntry':sipCfgDialProxyEntry,_A0:sipCfgDialProxyNumber,'sipCfgDialProxyCode':sipCfgDialProxyCode,'sipCfgDialProxyTone':sipCfgDialProxyTone,'sipCfgDialProxyActive':sipCfgDialProxyActive,'sipCfgDialProxyMessageType':sipCfgDialProxyMessageType,'sipCfgDialProxyMethod':sipCfgDialProxyMethod,'sipCfgDialProxyMethodDelimiter':sipCfgDialProxyMethodDelimiter,'sipCfgDhcp60AnnouncementMode':sipCfgDhcp60AnnouncementMode,'sipCfgCallForwardForbiddenNumbers':sipCfgCallForwardForbiddenNumbers,'sipCfgDefaultG711':sipCfgDefaultG711,'sipCfgGenLinger':sipCfgGenLinger,'sipCfgInviteLinger':sipCfgInviteLinger,'sipCfgTimerB':sipCfgTimerB,'sipCfgTimerF':sipCfgTimerF,'sipCfgRegExpires':sipCfgRegExpires,'sipCfgMaxUDPSize':sipCfgMaxUDPSize,'sipCfgSessionExpires':sipCfgSessionExpires,'sipCfgPenaltyBoxTimeout':sipCfgPenaltyBoxTimeout,'sipCfgDisconnectReorderToneDelay':sipCfgDisconnectReorderToneDelay,'sipCfgDistinctiveRingingForCallHold':sipCfgDistinctiveRingingForCallHold,'sipCfgSipFeatureSwitch2':sipCfgSipFeatureSwitch2,'sipCfgAuthPasswordKey':sipCfgAuthPasswordKey,'sipCfgMWITargetAddrType':sipCfgMWITargetAddrType,'sipCfgMWITargetAddr':sipCfgMWITargetAddr,'sipCfgMWITargetPort':sipCfgMWITargetPort,'sipCfgEmergencyServiceURN':sipCfgEmergencyServiceURN,'sipCfgSubsAlertTimeout':sipCfgSubsAlertTimeout,'sipCfgProvisionalTimer':sipCfgProvisionalTimer,'sipCfg3WCWaitHookHoldTimer':sipCfg3WCWaitHookHoldTimer,'sipCfgWaitHookHoldTone':sipCfgWaitHookHoldTone,'sipCfgMinSE':sipCfgMinSE,'sipCfgInDialogRefer':sipCfgInDialogRefer,'sipCfgFailoverSwitch':sipCfgFailoverSwitch,'sipCfgSubsRetryTimeout':sipCfgSubsRetryTimeout,'sipCfgPAccessNetworkInfoHeaderValue':sipCfgPAccessNetworkInfoHeaderValue,'sipCfgTermOffHookProcessingDelay':sipCfgTermOffHookProcessingDelay,'sipCfgT2':sipCfgT2,'sipCfgRegInterval':sipCfgRegInterval,'sipCfgOnhookDelayTimer':sipCfgOnhookDelayTimer,'sipCfgNetConfFactoryUri':sipCfgNetConfFactoryUri,'sipCfgSipFeatureSwitch3':sipCfgSipFeatureSwitch3,'sipCfgRegisterOnExpire':sipCfgRegisterOnExpire,'sipCfgServiceCapabilities':sipCfgServiceCapabilities,'sipCfgCIDDisDSTInfo':sipCfgCIDDisDSTInfo,'sipCfgProtectedDnList':sipCfgProtectedDnList,'sipCfgUnsetDontFragmentBit':sipCfgUnsetDontFragmentBit,'sipCfgMWISubscriptionCheckInterval':sipCfgMWISubscriptionCheckInterval,'sipStatus':sipStatus,'sipStatusPortTable':sipStatusPortTable,'sipStatusPortEntry':sipStatusPortEntry,_A1:sipStatusPortPortNumber,'sipStatusAlarms':sipStatusAlarms,'sipStatusPortMWISubscribed':sipStatusPortMWISubscribed,'arrisSipIPv6Mib':arrisSipIPv6Mib,'arrisSipIPv6MaxUDPSize':arrisSipIPv6MaxUDPSize,'arrisSipIPv6IpPreferenceOverride':arrisSipIPv6IpPreferenceOverride})