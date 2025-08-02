_BF='brMultiIFIPv6StaticAddressIndex'
_BE='brMultiIFIPv6AddressIndex'
_BD='brMultiIFServiceStringIndex'
_BC='brMultiIFServiceIndex'
_BB='wirelesslan'
_BA='brSNMPTrapIndex'
_B9='brProxyServerInfoIndex'
_B8='brLdapServerAttrNameIndex'
_B7='brpsNetwareServerIndex'
_B6='brpsTCPIPAccessIndex'
_B5='brpsServiceStringIndex'
_B4='brpsPortIndex'
_B3='brpsWLanWepKeyIndex'
_B2='invalidAuthUserPass'
_B1='invalidAuthUserID'
_B0='invalidWLanNetKey'
_A_='noSuchWLan'
_Az='dot11b-gAuto'
_Ay='brpsAvailableWLanIndex'
_Ax='brpsWLanCapabilityAuthEAPIndex'
_Aw='brpsWLanCapabilitAuthModeIndex'
_Av='brpsWLanCapabilityEncryptModeIndex'
_Au='brEmailReportsIndex'
_At='brPJLInfoFirmwareUpdateconfigIndex'
_As='brPJLInfoStorageconfigIndex'
_Ar='brPJLInfoDXconfigIndex'
_Aq='brPJLInfoOuttrayconfigIndex'
_Ap='brPJLInfoIntrayconfigIndex'
_Ao='brPJLInfoOptionsIndex'
_An='brNotificationRuleIndex'
_Am='brFirmwareUpdateKeywordIndex'
_Al='brScanCountIndex'
_Ak='brPfKitIndex'
_Aj='brCapabilityResolutionIndex'
_Ai='brCapabilityMediatypeIndex'
_Ah='brCapabilityPaperIndex'
_Ag='brCapabilityOrientationIndex'
_Af='brPrintPagesPaperTypeIndex'
_Ae='brPrintPagesFuncIndex'
_Ad='brPrintPagesMediaPlaceIndex'
_Ac='brPrintPagesIndex'
_Ab='brCommunicationErrorHistoryIndex'
_Aa='brErrorHistoryIndex'
_AZ='brPrtAvoidMailboxFullIndex'
_AY='brPrtMailboxProtectIndex'
_AX='brFuncLockPcLoginNameAuthIndex'
_AW='brFuncLockUserPrintPageIndex'
_AV='brFuncLockUserFuncIndex'
_AU='brFuncLockPublicFuncIndex'
_AT='brCarbonCopyIndex'
_AS='brTrayPriorityIndex'
_AR='prc16k197x273'
_AQ='prc16k184x260'
_AP='prc16k195x270'
_AO='brSpeedDialIndex'
_AN='brOneTouchDialIndex'
_AM='brLdapServerInfoIndex'
_AL='brpsServiceIndex'
_AK='brNotificationIndex'
_AJ='brFuncLockUserIndex'
_AI='print'
_AH='copycolor'
_AG='eapfast-tls'
_AF='eapfast-gtc'
_AE='eapfast-mschapv2'
_AD='eapfast-none'
_AC='leap'
_AB='blinkScroll'
_AA='none'
_A9='scroll'
_A8='blink'
_A7='fix'
_A6='recycled'
_A5='envThin'
_A4='envThick'
_A3='bond'
_A2='thin'
_A1='thicker'
_A0='thick'
_z='regular'
_y='noCasette'
_x='transparency'
_w='auto'
_v='on'
_u='largestEnvelopesTheWest'
_t='envelopesY4'
_s='inches3x5'
_r='detectsensor'
_q='userdefined'
_p='organaizerM'
_o='organaizerL'
_n='organaizerK'
_m='organaizerJ'
_l='folio'
_k='hagaki'
_j='dll'
_i='b5Executive'
_h='a4Letter'
_g='custom'
_f='b5ISOShortEdge'
_e='executiveShortEdge'
_d='a4LONG'
_c='a4ShortEdge'
_b='letterShortEdge'
_a='a3PLUS'
_Z='ledger'
_Y='b5'
_X='b6'
_W='c5'
_V='dl'
_U='com10'
_T='monarch'
_S='b4JIS'
_R='b5JIS'
_Q='a3ISO'
_P='a4'
_O='a5'
_N='a6'
_M='legal'
_L='letter'
_K='executive'
_J='brMultiIFConfigureIndex'
_I='envelopes'
_H='off'
_G='OctetString'
_F='DisplayString'
_E='BROTHER-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','TextualConvention')
_Brother_ObjectIdentity=ObjectIdentity
brother=_Brother_ObjectIdentity((1,3,6,1,4,1,2435))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,2435,2))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,2435,2,3))
_Net_peripheral_ObjectIdentity=ObjectIdentity
net_peripheral=_Net_peripheral_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9))
_Net_printer_ObjectIdentity=ObjectIdentity
net_printer=_Net_printer_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,1))
_GeneralDeviceStatus_ObjectIdentity=ObjectIdentity
generalDeviceStatus=_GeneralDeviceStatus_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,1,1))
_Status_ObjectIdentity=ObjectIdentity
status=_Status_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,1,1,2))
class _BrJamPlace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrJamPlace_Type.__name__=_B
_BrJamPlace_Object=MibScalar
brJamPlace=_BrJamPlace_Object((1,3,6,1,4,1,2435,2,3,9,1,1,2,9),_BrJamPlace_Type())
brJamPlace.setMaxAccess(_D)
if mibBuilder.loadTexts:brJamPlace.setStatus(_A)
_Tonerlow_ObjectIdentity=ObjectIdentity
tonerlow=_Tonerlow_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,1,1,2,10))
class _BrToner1Low_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrToner1Low_Type.__name__=_B
_BrToner1Low_Object=MibScalar
brToner1Low=_BrToner1Low_Object((1,3,6,1,4,1,2435,2,3,9,1,1,2,10,1),_BrToner1Low_Type())
brToner1Low.setMaxAccess(_D)
if mibBuilder.loadTexts:brToner1Low.setStatus(_A)
class _BrToner2Low_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrToner2Low_Type.__name__=_B
_BrToner2Low_Object=MibScalar
brToner2Low=_BrToner2Low_Object((1,3,6,1,4,1,2435,2,3,9,1,1,2,10,2),_BrToner2Low_Type())
brToner2Low.setMaxAccess(_D)
if mibBuilder.loadTexts:brToner2Low.setStatus(_A)
class _BrToner3Low_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrToner3Low_Type.__name__=_B
_BrToner3Low_Object=MibScalar
brToner3Low=_BrToner3Low_Object((1,3,6,1,4,1,2435,2,3,9,1,1,2,10,3),_BrToner3Low_Type())
brToner3Low.setMaxAccess(_D)
if mibBuilder.loadTexts:brToner3Low.setStatus(_A)
class _BrToner4Low_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrToner4Low_Type.__name__=_B
_BrToner4Low_Object=MibScalar
brToner4Low=_BrToner4Low_Object((1,3,6,1,4,1,2435,2,3,9,1,1,2,10,4),_BrToner4Low_Type())
brToner4Low.setMaxAccess(_D)
if mibBuilder.loadTexts:brToner4Low.setStatus(_A)
_Brieee1284id_Type=OctetString
_Brieee1284id_Object=MibScalar
brieee1284id=_Brieee1284id_Object((1,3,6,1,4,1,2435,2,3,9,1,1,7),_Brieee1284id_Type())
brieee1284id.setMaxAccess(_D)
if mibBuilder.loadTexts:brieee1284id.setStatus(_A)
class _Brttt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Brttt1_Type.__name__=_B
_Brttt1_Object=MibScalar
brttt1=_Brttt1_Object((1,3,6,1,4,1,2435,2,3,9,1,1,10),_Brttt1_Type())
brttt1.setMaxAccess(_D)
if mibBuilder.loadTexts:brttt1.setStatus(_A)
_Net_MFP_ObjectIdentity=ObjectIdentity
net_MFP=_Net_MFP_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2))
_Fax_setup_ObjectIdentity=ObjectIdentity
fax_setup=_Fax_setup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,1))
_Autodial_ObjectIdentity=ObjectIdentity
autodial=_Autodial_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,1,1))
_OnetouchDial_ObjectIdentity=ObjectIdentity
onetouchDial=_OnetouchDial_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,1,1,1))
class _BrOneTouchDialCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrOneTouchDialCount_Type.__name__=_B
_BrOneTouchDialCount_Object=MibScalar
brOneTouchDialCount=_BrOneTouchDialCount_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,1,1),_BrOneTouchDialCount_Type())
brOneTouchDialCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brOneTouchDialCount.setStatus(_A)
_BrOneTouchDialTable_Object=MibTable
brOneTouchDialTable=_BrOneTouchDialTable_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,1,2))
if mibBuilder.loadTexts:brOneTouchDialTable.setStatus(_A)
_BrOneTouchDialEntry_Object=MibTableRow
brOneTouchDialEntry=_BrOneTouchDialEntry_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,1,2,1))
brOneTouchDialEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:brOneTouchDialEntry.setStatus(_A)
class _BrOneTouchDialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrOneTouchDialIndex_Type.__name__=_B
_BrOneTouchDialIndex_Object=MibTableColumn
brOneTouchDialIndex=_BrOneTouchDialIndex_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,1,2,1,1),_BrOneTouchDialIndex_Type())
brOneTouchDialIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brOneTouchDialIndex.setStatus(_A)
_BrOneTouchDialData_Type=OctetString
_BrOneTouchDialData_Object=MibTableColumn
brOneTouchDialData=_BrOneTouchDialData_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,1,2,1,2),_BrOneTouchDialData_Type())
brOneTouchDialData.setMaxAccess(_C)
if mibBuilder.loadTexts:brOneTouchDialData.setStatus(_A)
_SpeedDial_ObjectIdentity=ObjectIdentity
speedDial=_SpeedDial_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,1,1,2))
class _BrSpeedDialCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrSpeedDialCount_Type.__name__=_B
_BrSpeedDialCount_Object=MibScalar
brSpeedDialCount=_BrSpeedDialCount_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,2,1),_BrSpeedDialCount_Type())
brSpeedDialCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brSpeedDialCount.setStatus(_A)
_BrSpeedDialTable_Object=MibTable
brSpeedDialTable=_BrSpeedDialTable_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,2,2))
if mibBuilder.loadTexts:brSpeedDialTable.setStatus(_A)
_BrSpeedDialEntry_Object=MibTableRow
brSpeedDialEntry=_BrSpeedDialEntry_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,2,2,1))
brSpeedDialEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:brSpeedDialEntry.setStatus(_A)
class _BrSpeedDialIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrSpeedDialIndex_Type.__name__=_B
_BrSpeedDialIndex_Object=MibTableColumn
brSpeedDialIndex=_BrSpeedDialIndex_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,2,2,1,1),_BrSpeedDialIndex_Type())
brSpeedDialIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brSpeedDialIndex.setStatus(_A)
_BrSpeedDialData_Type=OctetString
_BrSpeedDialData_Object=MibTableColumn
brSpeedDialData=_BrSpeedDialData_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,2,2,1,2),_BrSpeedDialData_Type())
brSpeedDialData.setMaxAccess(_C)
if mibBuilder.loadTexts:brSpeedDialData.setStatus(_A)
class _BrDialDataAllClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrDialDataAllClear_Type.__name__=_B
_BrDialDataAllClear_Object=MibScalar
brDialDataAllClear=_BrDialDataAllClear_Object((1,3,6,1,4,1,2435,2,3,9,2,1,1,3),_BrDialDataAllClear_Type())
brDialDataAllClear.setMaxAccess(_C)
if mibBuilder.loadTexts:brDialDataAllClear.setStatus(_A)
_Fax_general_ObjectIdentity=ObjectIdentity
fax_general=_Fax_general_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,1,2))
_BrFaxReceiveMode_Type=Integer32
_BrFaxReceiveMode_Object=MibScalar
brFaxReceiveMode=_BrFaxReceiveMode_Object((1,3,6,1,4,1,2435,2,3,9,2,1,2,1),_BrFaxReceiveMode_Type())
brFaxReceiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brFaxReceiveMode.setStatus(_A)
class _BrRingDelayCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrRingDelayCount_Type.__name__=_B
_BrRingDelayCount_Object=MibScalar
brRingDelayCount=_BrRingDelayCount_Object((1,3,6,1,4,1,2435,2,3,9,2,1,2,2),_BrRingDelayCount_Type())
brRingDelayCount.setMaxAccess(_C)
if mibBuilder.loadTexts:brRingDelayCount.setStatus(_A)
_BrOwnFaxNumber_Type=OctetString
_BrOwnFaxNumber_Object=MibScalar
brOwnFaxNumber=_BrOwnFaxNumber_Object((1,3,6,1,4,1,2435,2,3,9,2,1,2,3),_BrOwnFaxNumber_Type())
brOwnFaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brOwnFaxNumber.setStatus(_A)
_Scanner_setup_ObjectIdentity=ObjectIdentity
scanner_setup=_Scanner_setup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,11))
_ScanToInfo_ObjectIdentity=ObjectIdentity
scanToInfo=_ScanToInfo_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,11,1))
_BrRegisterKeyInfo_Type=OctetString
_BrRegisterKeyInfo_Object=MibScalar
brRegisterKeyInfo=_BrRegisterKeyInfo_Object((1,3,6,1,4,1,2435,2,3,9,2,11,1,1),_BrRegisterKeyInfo_Type())
brRegisterKeyInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegisterKeyInfo.setStatus(_A)
_BrUnRegisterKeyInfo_Type=OctetString
_BrUnRegisterKeyInfo_Object=MibScalar
brUnRegisterKeyInfo=_BrUnRegisterKeyInfo_Object((1,3,6,1,4,1,2435,2,3,9,2,11,1,2),_BrUnRegisterKeyInfo_Type())
brUnRegisterKeyInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brUnRegisterKeyInfo.setStatus(_A)
class _BrNetSKeyReceiverAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_BrNetSKeyReceiverAddress_Type.__name__=_G
_BrNetSKeyReceiverAddress_Object=MibScalar
brNetSKeyReceiverAddress=_BrNetSKeyReceiverAddress_Object((1,3,6,1,4,1,2435,2,3,9,2,11,1,5),_BrNetSKeyReceiverAddress_Type())
brNetSKeyReceiverAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetSKeyReceiverAddress.setStatus(_A)
_MfpCapability_ObjectIdentity=ObjectIdentity
mfpCapability=_MfpCapability_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101))
_McGeneral_ObjectIdentity=ObjectIdentity
mcGeneral=_McGeneral_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,1))
_McgRemoteSetup_ObjectIdentity=ObjectIdentity
mcgRemoteSetup=_McgRemoteSetup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,1,11))
class _BrNetRemoteSetUpSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetRemoteSetUpSupported_Type.__name__=_B
_BrNetRemoteSetUpSupported_Object=MibScalar
brNetRemoteSetUpSupported=_BrNetRemoteSetUpSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,1,11,1),_BrNetRemoteSetUpSupported_Type())
brNetRemoteSetUpSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetRemoteSetUpSupported.setStatus(_A)
class _BrNetRemoteSetUpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetRemoteSetUpEnable_Type.__name__=_B
_BrNetRemoteSetUpEnable_Object=MibScalar
brNetRemoteSetUpEnable=_BrNetRemoteSetUpEnable_Object((1,3,6,1,4,1,2435,2,3,9,2,101,1,11,2),_BrNetRemoteSetUpEnable_Type())
brNetRemoteSetUpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetRemoteSetUpEnable.setStatus(_A)
class _BrNetRemoteSetUpFileFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rms',1),('rmd',2),('rmsrmd',3)))
_BrNetRemoteSetUpFileFormat_Type.__name__=_B
_BrNetRemoteSetUpFileFormat_Object=MibScalar
brNetRemoteSetUpFileFormat=_BrNetRemoteSetUpFileFormat_Object((1,3,6,1,4,1,2435,2,3,9,2,101,1,11,3),_BrNetRemoteSetUpFileFormat_Type())
brNetRemoteSetUpFileFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetRemoteSetUpFileFormat.setStatus(_A)
_McFax_ObjectIdentity=ObjectIdentity
mcFax=_McFax_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,2))
_McfGeneral_ObjectIdentity=ObjectIdentity
mcfGeneral=_McfGeneral_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,2,1))
class _BrFaxSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFaxSupported_Type.__name__=_B
_BrFaxSupported_Object=MibScalar
brFaxSupported=_BrFaxSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,1,1),_BrFaxSupported_Type())
brFaxSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brFaxSupported.setStatus(_A)
class _BrIFaxSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIFaxSupported_Type.__name__=_B
_BrIFaxSupported_Object=MibScalar
brIFaxSupported=_BrIFaxSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,1,3),_BrIFaxSupported_Type())
brIFaxSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brIFaxSupported.setStatus(_A)
_McfNetFaxShare_ObjectIdentity=ObjectIdentity
mcfNetFaxShare=_McfNetFaxShare_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,2,11))
class _BrNetFaxShareSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetFaxShareSupported_Type.__name__=_B
_BrNetFaxShareSupported_Object=MibScalar
brNetFaxShareSupported=_BrNetFaxShareSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,11,1),_BrNetFaxShareSupported_Type())
brNetFaxShareSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetFaxShareSupported.setStatus(_A)
class _BrNetFaxShareEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetFaxShareEnable_Type.__name__=_B
_BrNetFaxShareEnable_Object=MibScalar
brNetFaxShareEnable=_BrNetFaxShareEnable_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,11,2),_BrNetFaxShareEnable_Type())
brNetFaxShareEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetFaxShareEnable.setStatus(_A)
_McfNetPcFaxRx_ObjectIdentity=ObjectIdentity
mcfNetPcFaxRx=_McfNetPcFaxRx_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,2,12))
class _BrNetPcFaxRxSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetPcFaxRxSupported_Type.__name__=_B
_BrNetPcFaxRxSupported_Object=MibScalar
brNetPcFaxRxSupported=_BrNetPcFaxRxSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,12,1),_BrNetPcFaxRxSupported_Type())
brNetPcFaxRxSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetPcFaxRxSupported.setStatus(_A)
class _BrNetPcFaxRxEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetPcFaxRxEnable_Type.__name__=_B
_BrNetPcFaxRxEnable_Object=MibScalar
brNetPcFaxRxEnable=_BrNetPcFaxRxEnable_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,12,2),_BrNetPcFaxRxEnable_Type())
brNetPcFaxRxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetPcFaxRxEnable.setStatus(_A)
_BrNetRegisterPcFaxInfo_Type=OctetString
_BrNetRegisterPcFaxInfo_Object=MibScalar
brNetRegisterPcFaxInfo=_BrNetRegisterPcFaxInfo_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,12,3),_BrNetRegisterPcFaxInfo_Type())
brNetRegisterPcFaxInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetRegisterPcFaxInfo.setStatus(_A)
_McfFaxInfomation_ObjectIdentity=ObjectIdentity
mcfFaxInfomation=_McfFaxInfomation_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,2,101))
class _BrPhoneNumberLastFax_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BrPhoneNumberLastFax_Type.__name__=_G
_BrPhoneNumberLastFax_Object=MibScalar
brPhoneNumberLastFax=_BrPhoneNumberLastFax_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,101,1),_BrPhoneNumberLastFax_Type())
brPhoneNumberLastFax.setMaxAccess(_D)
if mibBuilder.loadTexts:brPhoneNumberLastFax.setStatus(_A)
_BrPagesSentLastFax_Type=Counter32
_BrPagesSentLastFax_Object=MibScalar
brPagesSentLastFax=_BrPagesSentLastFax_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,101,2),_BrPagesSentLastFax_Type())
brPagesSentLastFax.setMaxAccess(_D)
if mibBuilder.loadTexts:brPagesSentLastFax.setStatus(_A)
_BrTimestampLastFax_Type=DateAndTime
_BrTimestampLastFax_Object=MibScalar
brTimestampLastFax=_BrTimestampLastFax_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,101,3),_BrTimestampLastFax_Type())
brTimestampLastFax.setMaxAccess(_D)
if mibBuilder.loadTexts:brTimestampLastFax.setStatus(_A)
class _BrFaxHeaderInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_BrFaxHeaderInfo_Type.__name__=_F
_BrFaxHeaderInfo_Object=MibScalar
brFaxHeaderInfo=_BrFaxHeaderInfo_Object((1,3,6,1,4,1,2435,2,3,9,2,101,2,101,4),_BrFaxHeaderInfo_Type())
brFaxHeaderInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brFaxHeaderInfo.setStatus(_A)
_McScanner_ObjectIdentity=ObjectIdentity
mcScanner=_McScanner_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,3))
_McsNetScanner_ObjectIdentity=ObjectIdentity
mcsNetScanner=_McsNetScanner_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,3,11))
class _BrNetScannerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetScannerSupported_Type.__name__=_B
_BrNetScannerSupported_Object=MibScalar
brNetScannerSupported=_BrNetScannerSupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,3,11,1),_BrNetScannerSupported_Type())
brNetScannerSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetScannerSupported.setStatus(_A)
class _BrNetScannerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetScannerEnable_Type.__name__=_B
_BrNetScannerEnable_Object=MibScalar
brNetScannerEnable=_BrNetScannerEnable_Object((1,3,6,1,4,1,2435,2,3,9,2,101,3,11,2),_BrNetScannerEnable_Type())
brNetScannerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetScannerEnable.setStatus(_A)
_McsNetSKy_ObjectIdentity=ObjectIdentity
mcsNetSKy=_McsNetSKy_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,101,3,12))
class _BrNetSKeySupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetSKeySupported_Type.__name__=_B
_BrNetSKeySupported_Object=MibScalar
brNetSKeySupported=_BrNetSKeySupported_Object((1,3,6,1,4,1,2435,2,3,9,2,101,3,12,1),_BrNetSKeySupported_Type())
brNetSKeySupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brNetSKeySupported.setStatus(_A)
class _BrNetSKeyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrNetSKeyEnable_Type.__name__=_B
_BrNetSKeyEnable_Object=MibScalar
brNetSKeyEnable=_BrNetSKeyEnable_Object((1,3,6,1,4,1,2435,2,3,9,2,101,3,12,2),_BrNetSKeyEnable_Type())
brNetSKeyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brNetSKeyEnable.setStatus(_A)
_Mfpgeneral_setup_ObjectIdentity=ObjectIdentity
mfpgeneral_setup=_Mfpgeneral_setup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,2,111))
_BrServiceMode_Type=OctetString
_BrServiceMode_Object=MibScalar
brServiceMode=_BrServiceMode_Object((1,3,6,1,4,1,2435,2,3,9,2,111,1),_BrServiceMode_Type())
brServiceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brServiceMode.setStatus(_A)
class _BrLockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrLockMode_Type.__name__=_B
_BrLockMode_Object=MibScalar
brLockMode=_BrLockMode_Object((1,3,6,1,4,1,2435,2,3,9,2,111,2),_BrLockMode_Type())
brLockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brLockMode.setStatus(_A)
_BrActivityReportSetting_Type=Integer32
_BrActivityReportSetting_Object=MibScalar
brActivityReportSetting=_BrActivityReportSetting_Object((1,3,6,1,4,1,2435,2,3,9,2,111,3),_BrActivityReportSetting_Type())
brActivityReportSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:brActivityReportSetting.setStatus(_A)
_NetPML_ObjectIdentity=ObjectIdentity
netPML=_NetPML_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4))
_NetPMLmgmt_ObjectIdentity=ObjectIdentity
netPMLmgmt=_NetPMLmgmt_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1))
_Destination_subsystem1_ObjectIdentity=ObjectIdentity
destination_subsystem1=_Destination_subsystem1_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1))
_Sleep_ObjectIdentity=ObjectIdentity
sleep=_Sleep_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,1))
class _Brpowerstime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Brpowerstime_Type.__name__=_B
_Brpowerstime_Object=MibScalar
brpowerstime=_Brpowerstime_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,1,1),_Brpowerstime_Type())
brpowerstime.setMaxAccess(_C)
if mibBuilder.loadTexts:brpowerstime.setStatus(_A)
_Autoc_ObjectIdentity=ObjectIdentity
autoc=_Autoc_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,2))
class _Brautocont_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Brautocont_Type.__name__=_B
_Brautocont_Object=MibScalar
brautocont=_Brautocont_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,2,7),_Brautocont_Type())
brautocont.setMaxAccess(_C)
if mibBuilder.loadTexts:brautocont.setStatus(_A)
_Simm_ObjectIdentity=ObjectIdentity
simm=_Simm_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4))
_Specification_ObjectIdentity=ObjectIdentity
specification=_Specification_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1))
_Simmkind0_ObjectIdentity=ObjectIdentity
simmkind0=_Simmkind0_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,1))
_Brsimmtype0_Type=Integer32
_Brsimmtype0_Object=MibScalar
brsimmtype0=_Brsimmtype0_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,1,4),_Brsimmtype0_Type())
brsimmtype0.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmtype0.setStatus(_A)
_Brsimmsize0_Type=Integer32
_Brsimmsize0_Object=MibScalar
brsimmsize0=_Brsimmsize0_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,1,5),_Brsimmsize0_Type())
brsimmsize0.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmsize0.setStatus(_A)
_Simmkind1_ObjectIdentity=ObjectIdentity
simmkind1=_Simmkind1_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,2))
_Brsimmtype1_Type=Integer32
_Brsimmtype1_Object=MibScalar
brsimmtype1=_Brsimmtype1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,2,4),_Brsimmtype1_Type())
brsimmtype1.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmtype1.setStatus(_A)
_Brsimmsize1_Type=Integer32
_Brsimmsize1_Object=MibScalar
brsimmsize1=_Brsimmsize1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,2,5),_Brsimmsize1_Type())
brsimmsize1.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmsize1.setStatus(_A)
_Simmkind2_ObjectIdentity=ObjectIdentity
simmkind2=_Simmkind2_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,3))
_Brsimmtype2_Type=Integer32
_Brsimmtype2_Object=MibScalar
brsimmtype2=_Brsimmtype2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,3,4),_Brsimmtype2_Type())
brsimmtype2.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmtype2.setStatus(_A)
_Brsimmsize2_Type=Integer32
_Brsimmsize2_Object=MibScalar
brsimmsize2=_Brsimmsize2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,3,5),_Brsimmsize2_Type())
brsimmsize2.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmsize2.setStatus(_A)
_Simmkind3_ObjectIdentity=ObjectIdentity
simmkind3=_Simmkind3_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,4))
_Brsimmtype3_Type=Integer32
_Brsimmtype3_Object=MibScalar
brsimmtype3=_Brsimmtype3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,4,4),_Brsimmtype3_Type())
brsimmtype3.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmtype3.setStatus(_A)
_Brsimmsize3_Type=Integer32
_Brsimmsize3_Object=MibScalar
brsimmsize3=_Brsimmsize3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,1,4,5),_Brsimmsize3_Type())
brsimmsize3.setMaxAccess(_D)
if mibBuilder.loadTexts:brsimmsize3.setStatus(_A)
_Bio1_explanation_ObjectIdentity=ObjectIdentity
bio1_explanation=_Bio1_explanation_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,3))
_Determined_ObjectIdentity=ObjectIdentity
determined=_Determined_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,3,1))
class _BrTBD1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BrTBD1_Type.__name__=_B
_BrTBD1_Object=MibScalar
brTBD1=_BrTBD1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,1,4,3,1,4),_BrTBD1_Type())
brTBD1.setMaxAccess(_C)
if mibBuilder.loadTexts:brTBD1.setStatus(_A)
_Destination_subsystem2_ObjectIdentity=ObjectIdentity
destination_subsystem2=_Destination_subsystem2_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,2))
_Printerjob_ObjectIdentity=ObjectIdentity
printerjob=_Printerjob_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,2,1))
_Jobend_ObjectIdentity=ObjectIdentity
jobend=_Jobend_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,2,1,1))
class _Brtimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Brtimeout_Type.__name__=_B
_Brtimeout_Object=MibScalar
brtimeout=_Brtimeout_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,2,1,1,1),_Brtimeout_Type())
brtimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brtimeout.setStatus(_A)
class _BrTBD2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BrTBD2_Type.__name__=_B
_BrTBD2_Object=MibScalar
brTBD2=_BrTBD2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,2,1,1,5),_BrTBD2_Type())
brTBD2.setMaxAccess(_C)
if mibBuilder.loadTexts:brTBD2.setStatus(_A)
_Destination_subsystem3_ObjectIdentity=ObjectIdentity
destination_subsystem3=_Destination_subsystem3_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,3))
_Prt_setup_ObjectIdentity=ObjectIdentity
prt_setup=_Prt_setup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3))
_Prt_condition_ObjectIdentity=ObjectIdentity
prt_condition=_Prt_condition_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1))
class _Brpersonality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7,8)));namedValues=NamedValues(*(('pcl',1),('hpgl',2),('ps',4),(_w,5),('ibm',6),('epson',7),('hbp',8)))
_Brpersonality_Type.__name__=_B
_Brpersonality_Object=MibScalar
brpersonality=_Brpersonality_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,1),_Brpersonality_Type())
brpersonality.setMaxAccess(_C)
if mibBuilder.loadTexts:brpersonality.setStatus(_A)
class _Brorientation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Brorientation_Type.__name__=_B
_Brorientation_Object=MibScalar
brorientation=_Brorientation_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,2),_Brorientation_Type())
brorientation.setMaxAccess(_C)
if mibBuilder.loadTexts:brorientation.setStatus(_A)
class _Brcopies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Brcopies_Type.__name__=_B
_Brcopies_Object=MibScalar
brcopies=_Brcopies_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,4),_Brcopies_Type())
brcopies.setMaxAccess(_C)
if mibBuilder.loadTexts:brcopies.setStatus(_A)
class _BrTBD3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BrTBD3_Type.__name__=_B
_BrTBD3_Object=MibScalar
brTBD3=_BrTBD3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,6),_BrTBD3_Type())
brTBD3.setMaxAccess(_C)
if mibBuilder.loadTexts:brTBD3.setStatus(_A)
class _Brresolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_Brresolution_Type.__name__=_B
_Brresolution_Object=MibScalar
brresolution=_Brresolution_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,8),_Brresolution_Type())
brresolution.setMaxAccess(_C)
if mibBuilder.loadTexts:brresolution.setStatus(_A)
class _Brpageprotect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_Brpageprotect_Type.__name__=_B
_Brpageprotect_Object=MibScalar
brpageprotect=_Brpageprotect_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,10),_Brpageprotect_Type())
brpageprotect.setMaxAccess(_C)
if mibBuilder.loadTexts:brpageprotect.setStatus(_A)
class _Brlines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,128))
_Brlines_Type.__name__=_B
_Brlines_Object=MibScalar
brlines=_Brlines_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,11),_Brlines_Type())
brlines.setMaxAccess(_C)
if mibBuilder.loadTexts:brlines.setStatus(_A)
class _Brpaper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,923,924,925,926,927,1001)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),('a5l',923),('b6JIS',924),(_AP,925),(_AQ,926),(_AR,927),(_w,1001)))
_Brpaper_Type.__name__=_B
_Brpaper_Object=MibScalar
brpaper=_Brpaper_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,13),_Brpaper_Type())
brpaper.setMaxAccess(_C)
if mibBuilder.loadTexts:brpaper.setStatus(_A)
_Brpapertype_Type=Integer32
_Brpapertype_Object=MibScalar
brpapertype=_Brpapertype_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,22),_Brpapertype_Type())
brpapertype.setMaxAccess(_C)
if mibBuilder.loadTexts:brpapertype.setStatus(_A)
_Brpapertype2_Type=Integer32
_Brpapertype2_Object=MibScalar
brpapertype2=_Brpapertype2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,23),_Brpapertype2_Type())
brpapertype2.setMaxAccess(_C)
if mibBuilder.loadTexts:brpapertype2.setStatus(_A)
_BrpapertypeMP_Type=Integer32
_BrpapertypeMP_Object=MibScalar
brpapertypeMP=_BrpapertypeMP_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,3,3,1,26),_BrpapertypeMP_Type())
brpapertypeMP.setMaxAccess(_C)
if mibBuilder.loadTexts:brpapertypeMP.setStatus(_A)
_Destination_subsystem4_ObjectIdentity=ObjectIdentity
destination_subsystem4=_Destination_subsystem4_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1))
_Prt_density_ObjectIdentity=ObjectIdentity
prt_density=_Prt_density_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,1))
class _Brdensity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,15))
_Brdensity_Type.__name__=_B
_Brdensity_Object=MibScalar
brdensity=_Brdensity_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,1,5),_Brdensity_Type())
brdensity.setMaxAccess(_C)
if mibBuilder.loadTexts:brdensity.setStatus(_A)
_Status_prt_eng_ObjectIdentity=ObjectIdentity
status_prt_eng=_Status_prt_eng_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,2))
_Tray_ObjectIdentity=ObjectIdentity
tray=_Tray_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3))
_Manual_ObjectIdentity=ObjectIdentity
manual=_Manual_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,1))
class _Brmanualfeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Brmanualfeed_Type.__name__=_B
_Brmanualfeed_Object=MibScalar
brmanualfeed=_Brmanualfeed_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,1,4),_Brmanualfeed_Type())
brmanualfeed.setMaxAccess(_C)
if mibBuilder.loadTexts:brmanualfeed.setStatus(_A)
_Traysize_ObjectIdentity=ObjectIdentity
traysize=_Traysize_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3))
_Mp_ObjectIdentity=ObjectIdentity
mp=_Mp_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,1))
class _Brmpsize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_Brmpsize_Type.__name__=_B
_Brmpsize_Object=MibScalar
brmpsize=_Brmpsize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,1,1),_Brmpsize_Type())
brmpsize.setMaxAccess(_C)
if mibBuilder.loadTexts:brmpsize.setStatus(_A)
_Cassette_ObjectIdentity=ObjectIdentity
cassette=_Cassette_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,2))
class _Brtray1size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_Brtray1size_Type.__name__=_B
_Brtray1size_Object=MibScalar
brtray1size=_Brtray1size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,2,1),_Brtray1size_Type())
brtray1size.setMaxAccess(_C)
if mibBuilder.loadTexts:brtray1size.setStatus(_A)
_Cassette2_ObjectIdentity=ObjectIdentity
cassette2=_Cassette2_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,3))
class _Brtray2size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_Brtray2size_Type.__name__=_B
_Brtray2size_Object=MibScalar
brtray2size=_Brtray2size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,3,1),_Brtray2size_Type())
brtray2size.setMaxAccess(_C)
if mibBuilder.loadTexts:brtray2size.setStatus(_A)
_Cassette3_ObjectIdentity=ObjectIdentity
cassette3=_Cassette3_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,4))
class _Brtray3size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_Brtray3size_Type.__name__=_B
_Brtray3size_Object=MibScalar
brtray3size=_Brtray3size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,4,1),_Brtray3size_Type())
brtray3size.setMaxAccess(_C)
if mibBuilder.loadTexts:brtray3size.setStatus(_A)
_Cassette4_ObjectIdentity=ObjectIdentity
cassette4=_Cassette4_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,5))
class _Brtray4size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_Brtray4size_Type.__name__=_B
_Brtray4size_Object=MibScalar
brtray4size=_Brtray4size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,3,3,5,1),_Brtray4size_Type())
brtray4size.setMaxAccess(_C)
if mibBuilder.loadTexts:brtray4size.setStatus(_A)
_Economy_ObjectIdentity=ObjectIdentity
economy=_Economy_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,6))
class _Brret_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Brret_Type.__name__=_B
_Brret_Object=MibScalar
brret=_Brret_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,6,5),_Brret_Type())
brret.setMaxAccess(_C)
if mibBuilder.loadTexts:brret.setStatus(_A)
class _Breconomode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Breconomode_Type.__name__=_B
_Breconomode_Object=MibScalar
breconomode=_Breconomode_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,4,1,6,7),_Breconomode_Type())
breconomode.setMaxAccess(_C)
if mibBuilder.loadTexts:breconomode.setStatus(_A)
_Brorg_ObjectIdentity=ObjectIdentity
brorg=_Brorg_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5))
_Printersetup_ObjectIdentity=ObjectIdentity
printersetup=_Printersetup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1))
_General_ObjectIdentity=ObjectIdentity
general=_General_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1))
class _BrPrtGeneralEmulationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_BrPrtGeneralEmulationTimeout_Type.__name__=_B
_BrPrtGeneralEmulationTimeout_Object=MibScalar
brPrtGeneralEmulationTimeout=_BrPrtGeneralEmulationTimeout_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,1),_BrPrtGeneralEmulationTimeout_Type())
brPrtGeneralEmulationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralEmulationTimeout.setStatus(_A)
class _BrPrtGeneralFeeder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPrtGeneralFeeder_Type.__name__=_B
_BrPrtGeneralFeeder_Object=MibScalar
brPrtGeneralFeeder=_BrPrtGeneralFeeder_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,2),_BrPrtGeneralFeeder_Type())
brPrtGeneralFeeder.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralFeeder.setStatus(_A)
class _BrPrtGeneralPowerSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtGeneralPowerSave_Type.__name__=_B
_BrPrtGeneralPowerSave_Object=MibScalar
brPrtGeneralPowerSave=_BrPrtGeneralPowerSave_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,3),_BrPrtGeneralPowerSave_Type())
brPrtGeneralPowerSave.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralPowerSave.setStatus(_A)
class _BrPrtGeneralBuzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtGeneralBuzzer_Type.__name__=_B
_BrPrtGeneralBuzzer_Object=MibScalar
brPrtGeneralBuzzer=_BrPrtGeneralBuzzer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,4),_BrPrtGeneralBuzzer_Type())
brPrtGeneralBuzzer.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralBuzzer.setStatus(_A)
class _BrPrtGeneralColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrPrtGeneralColor_Type.__name__=_B
_BrPrtGeneralColor_Object=MibScalar
brPrtGeneralColor=_BrPrtGeneralColor_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,5),_BrPrtGeneralColor_Type())
brPrtGeneralColor.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralColor.setStatus(_A)
class _BrPrtGeneralDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtGeneralDuplex_Type.__name__=_B
_BrPrtGeneralDuplex_Object=MibScalar
brPrtGeneralDuplex=_BrPrtGeneralDuplex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,6),_BrPrtGeneralDuplex_Type())
brPrtGeneralDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralDuplex.setStatus(_A)
class _BrPrtGeneralBinding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrPrtGeneralBinding_Type.__name__=_B
_BrPrtGeneralBinding_Object=MibScalar
brPrtGeneralBinding=_BrPrtGeneralBinding_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,1,7),_BrPrtGeneralBinding_Type())
brPrtGeneralBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtGeneralBinding.setStatus(_A)
_Advanced_ObjectIdentity=ObjectIdentity
advanced=_Advanced_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2))
class _BrPrtAdvancedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedPriority_Type.__name__=_B
_BrPrtAdvancedPriority_Object=MibScalar
brPrtAdvancedPriority=_BrPrtAdvancedPriority_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,1),_BrPrtAdvancedPriority_Type())
brPrtAdvancedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedPriority.setStatus(_A)
class _BrPrtAdvancedUseMPTrayFirst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedUseMPTrayFirst_Type.__name__=_B
_BrPrtAdvancedUseMPTrayFirst_Object=MibScalar
brPrtAdvancedUseMPTrayFirst=_BrPrtAdvancedUseMPTrayFirst_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,2),_BrPrtAdvancedUseMPTrayFirst_Type())
brPrtAdvancedUseMPTrayFirst.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedUseMPTrayFirst.setStatus(_A)
class _BrPrtAdvancedMPTrayFeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedMPTrayFeed_Type.__name__=_B
_BrPrtAdvancedMPTrayFeed_Object=MibScalar
brPrtAdvancedMPTrayFeed=_BrPrtAdvancedMPTrayFeed_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,3),_BrPrtAdvancedMPTrayFeed_Type())
brPrtAdvancedMPTrayFeed.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedMPTrayFeed.setStatus(_A)
class _BrPrtAdvancedXOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_BrPrtAdvancedXOffset_Type.__name__=_B
_BrPrtAdvancedXOffset_Object=MibScalar
brPrtAdvancedXOffset=_BrPrtAdvancedXOffset_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,4),_BrPrtAdvancedXOffset_Type())
brPrtAdvancedXOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedXOffset.setStatus(_A)
class _BrPrtAdvancedYOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_BrPrtAdvancedYOffset_Type.__name__=_B
_BrPrtAdvancedYOffset_Object=MibScalar
brPrtAdvancedYOffset=_BrPrtAdvancedYOffset_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,5),_BrPrtAdvancedYOffset_Type())
brPrtAdvancedYOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedYOffset.setStatus(_A)
class _BrPrtAdvancedImageCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedImageCompression_Type.__name__=_B
_BrPrtAdvancedImageCompression_Object=MibScalar
brPrtAdvancedImageCompression=_BrPrtAdvancedImageCompression_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,6),_BrPrtAdvancedImageCompression_Type())
brPrtAdvancedImageCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedImageCompression.setStatus(_A)
_Autoff_ObjectIdentity=ObjectIdentity
autoff=_Autoff_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,7))
class _BrPrtAdvancedAutoFormFeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedAutoFormFeed_Type.__name__=_B
_BrPrtAdvancedAutoFormFeed_Object=MibScalar
brPrtAdvancedAutoFormFeed=_BrPrtAdvancedAutoFormFeed_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,7,1),_BrPrtAdvancedAutoFormFeed_Type())
brPrtAdvancedAutoFormFeed.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedAutoFormFeed.setStatus(_A)
class _BrPrtAdvancedAutoTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_BrPrtAdvancedAutoTimeout_Type.__name__=_B
_BrPrtAdvancedAutoTimeout_Object=MibScalar
brPrtAdvancedAutoTimeout=_BrPrtAdvancedAutoTimeout_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,7,2),_BrPrtAdvancedAutoTimeout_Type())
brPrtAdvancedAutoTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedAutoTimeout.setStatus(_A)
class _BrPrtAdvancedFFSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedFFSuppress_Type.__name__=_B
_BrPrtAdvancedFFSuppress_Object=MibScalar
brPrtAdvancedFFSuppress=_BrPrtAdvancedFFSuppress_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,8),_BrPrtAdvancedFFSuppress_Type())
brPrtAdvancedFFSuppress.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedFFSuppress.setStatus(_A)
class _BrPrtAdvancedTonerLowPrint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAdvancedTonerLowPrint_Type.__name__=_B
_BrPrtAdvancedTonerLowPrint_Object=MibScalar
brPrtAdvancedTonerLowPrint=_BrPrtAdvancedTonerLowPrint_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,9),_BrPrtAdvancedTonerLowPrint_Type())
brPrtAdvancedTonerLowPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedTonerLowPrint.setStatus(_A)
class _BrPrtAdvancedPrintDensity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BrPrtAdvancedPrintDensity_Type.__name__=_B
_BrPrtAdvancedPrintDensity_Object=MibScalar
brPrtAdvancedPrintDensity=_BrPrtAdvancedPrintDensity_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,10),_BrPrtAdvancedPrintDensity_Type())
brPrtAdvancedPrintDensity.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedPrintDensity.setStatus(_A)
class _BrPrtAdvancedInputBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BrPrtAdvancedInputBuffer_Type.__name__=_B
_BrPrtAdvancedInputBuffer_Object=MibScalar
brPrtAdvancedInputBuffer=_BrPrtAdvancedInputBuffer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,11),_BrPrtAdvancedInputBuffer_Type())
brPrtAdvancedInputBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedInputBuffer.setStatus(_A)
class _BrPrtAdvancedLanguage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('english',1),('danish',2),('dutch',3),('finish',4),('french',5),('german',6),('italian',7),('norwegian',8),('portuguse',9),('swedish',10),('spanish',11),('turkish',12),('polish',13),('japanese',14),('russian',15),('czech',16),('hungarian',17),('romanian',18),('bulgarian',19),('slovakian',20),('chinese',21),('brazil',22)))
_BrPrtAdvancedLanguage_Type.__name__=_B
_BrPrtAdvancedLanguage_Object=MibScalar
brPrtAdvancedLanguage=_BrPrtAdvancedLanguage_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,12),_BrPrtAdvancedLanguage_Type())
brPrtAdvancedLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedLanguage.setStatus(_A)
class _BrSecurePrintRAMSizeMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrSecurePrintRAMSizeMax_Type.__name__=_B
_BrSecurePrintRAMSizeMax_Object=MibScalar
brSecurePrintRAMSizeMax=_BrSecurePrintRAMSizeMax_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,13),_BrSecurePrintRAMSizeMax_Type())
brSecurePrintRAMSizeMax.setMaxAccess(_D)
if mibBuilder.loadTexts:brSecurePrintRAMSizeMax.setStatus(_A)
class _BrSecurePrintRAMSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrSecurePrintRAMSize_Type.__name__=_B
_BrSecurePrintRAMSize_Object=MibScalar
brSecurePrintRAMSize=_BrSecurePrintRAMSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,14),_BrSecurePrintRAMSize_Type())
brSecurePrintRAMSize.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecurePrintRAMSize.setStatus(_A)
class _BrPrtAdvancedJamRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPrtAdvancedJamRecovery_Type.__name__=_B
_BrPrtAdvancedJamRecovery_Object=MibScalar
brPrtAdvancedJamRecovery=_BrPrtAdvancedJamRecovery_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,15),_BrPrtAdvancedJamRecovery_Type())
brPrtAdvancedJamRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedJamRecovery.setStatus(_A)
class _BrPrtAdvancedSleepIndication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('dimmed',2)))
_BrPrtAdvancedSleepIndication_Type.__name__=_B
_BrPrtAdvancedSleepIndication_Object=MibScalar
brPrtAdvancedSleepIndication=_BrPrtAdvancedSleepIndication_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,16),_BrPrtAdvancedSleepIndication_Type())
brPrtAdvancedSleepIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedSleepIndication.setStatus(_A)
class _BrPrtAdvancedDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardOutputTray',1),('oct',2),('octStack',3)))
_BrPrtAdvancedDestination_Type.__name__=_B
_BrPrtAdvancedDestination_Object=MibScalar
brPrtAdvancedDestination=_BrPrtAdvancedDestination_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,17),_BrPrtAdvancedDestination_Type())
brPrtAdvancedDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedDestination.setStatus(_A)
class _BrPrtAdvancedLowerLCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonePage',1),('counter',2),('jobName',3)))
_BrPrtAdvancedLowerLCD_Type.__name__=_B
_BrPrtAdvancedLowerLCD_Object=MibScalar
brPrtAdvancedLowerLCD=_BrPrtAdvancedLowerLCD_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,18),_BrPrtAdvancedLowerLCD_Type())
brPrtAdvancedLowerLCD.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedLowerLCD.setStatus(_A)
class _BrPrtAdvancedAutoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPrtAdvancedAutoOnline_Type.__name__=_B
_BrPrtAdvancedAutoOnline_Object=MibScalar
brPrtAdvancedAutoOnline=_BrPrtAdvancedAutoOnline_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,19),_BrPrtAdvancedAutoOnline_Type())
brPrtAdvancedAutoOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedAutoOnline.setStatus(_A)
class _BrPrtAdvancedButtonRepeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BrPrtAdvancedButtonRepeat_Type.__name__=_B
_BrPrtAdvancedButtonRepeat_Object=MibScalar
brPrtAdvancedButtonRepeat=_BrPrtAdvancedButtonRepeat_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,20),_BrPrtAdvancedButtonRepeat_Type())
brPrtAdvancedButtonRepeat.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedButtonRepeat.setStatus(_A)
class _BrPrtAdvancedMessageScroll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BrPrtAdvancedMessageScroll_Type.__name__=_B
_BrPrtAdvancedMessageScroll_Object=MibScalar
brPrtAdvancedMessageScroll=_BrPrtAdvancedMessageScroll_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,21),_BrPrtAdvancedMessageScroll_Type())
brPrtAdvancedMessageScroll.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedMessageScroll.setStatus(_A)
_Buzzer_ObjectIdentity=ObjectIdentity
buzzer=_Buzzer_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,22))
class _BrPrtAdvancedErrorBuzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('normal',2),('special',3)))
_BrPrtAdvancedErrorBuzzer_Type.__name__=_B
_BrPrtAdvancedErrorBuzzer_Object=MibScalar
brPrtAdvancedErrorBuzzer=_BrPrtAdvancedErrorBuzzer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,22,1),_BrPrtAdvancedErrorBuzzer_Type())
brPrtAdvancedErrorBuzzer.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedErrorBuzzer.setStatus(_A)
class _BrPrtAdvancedPanelBuzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPrtAdvancedPanelBuzzer_Type.__name__=_B
_BrPrtAdvancedPanelBuzzer_Object=MibScalar
brPrtAdvancedPanelBuzzer=_BrPrtAdvancedPanelBuzzer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,22,2),_BrPrtAdvancedPanelBuzzer_Type())
brPrtAdvancedPanelBuzzer.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedPanelBuzzer.setStatus(_A)
class _BrPrtAdvancedBuzzerVolume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_BrPrtAdvancedBuzzerVolume_Type.__name__=_B
_BrPrtAdvancedBuzzerVolume_Object=MibScalar
brPrtAdvancedBuzzerVolume=_BrPrtAdvancedBuzzerVolume_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,22,3),_BrPrtAdvancedBuzzerVolume_Type())
brPrtAdvancedBuzzerVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedBuzzerVolume.setStatus(_A)
_BrPrtAdvancedLCDDensity_Type=Integer32
_BrPrtAdvancedLCDDensity_Object=MibScalar
brPrtAdvancedLCDDensity=_BrPrtAdvancedLCDDensity_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,23),_BrPrtAdvancedLCDDensity_Type())
brPrtAdvancedLCDDensity.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedLCDDensity.setStatus(_A)
_SmallPaperSize_ObjectIdentity=ObjectIdentity
smallPaperSize=_SmallPaperSize_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51))
class _BrSmallPaperSizeMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,1000)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),(_y,1000)))
_BrSmallPaperSizeMP_Type.__name__=_B
_BrSmallPaperSizeMP_Object=MibScalar
brSmallPaperSizeMP=_BrSmallPaperSizeMP_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51,1),_BrSmallPaperSizeMP_Type())
brSmallPaperSizeMP.setMaxAccess(_C)
if mibBuilder.loadTexts:brSmallPaperSizeMP.setStatus(_A)
class _BrSmallPaperSize1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,1000)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),(_y,1000)))
_BrSmallPaperSize1_Type.__name__=_B
_BrSmallPaperSize1_Object=MibScalar
brSmallPaperSize1=_BrSmallPaperSize1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51,2),_BrSmallPaperSize1_Type())
brSmallPaperSize1.setMaxAccess(_C)
if mibBuilder.loadTexts:brSmallPaperSize1.setStatus(_A)
class _BrSmallPaperSize2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,1000)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),(_y,1000)))
_BrSmallPaperSize2_Type.__name__=_B
_BrSmallPaperSize2_Object=MibScalar
brSmallPaperSize2=_BrSmallPaperSize2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51,3),_BrSmallPaperSize2_Type())
brSmallPaperSize2.setMaxAccess(_C)
if mibBuilder.loadTexts:brSmallPaperSize2.setStatus(_A)
class _BrSmallPaperSize3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,1000)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),(_y,1000)))
_BrSmallPaperSize3_Type.__name__=_B
_BrSmallPaperSize3_Object=MibScalar
brSmallPaperSize3=_BrSmallPaperSize3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51,4),_BrSmallPaperSize3_Type())
brSmallPaperSize3.setMaxAccess(_C)
if mibBuilder.loadTexts:brSmallPaperSize3.setStatus(_A)
class _BrSmallPaperSize4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,1000)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),(_y,1000)))
_BrSmallPaperSize4_Type.__name__=_B
_BrSmallPaperSize4_Object=MibScalar
brSmallPaperSize4=_BrSmallPaperSize4_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,51,5),_BrSmallPaperSize4_Type())
brSmallPaperSize4.setMaxAccess(_C)
if mibBuilder.loadTexts:brSmallPaperSize4.setStatus(_A)
_TrayPriority_ObjectIdentity=ObjectIdentity
trayPriority=_TrayPriority_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52))
_BrPrtAdvancedTrayPriority_Type=Integer32
_BrPrtAdvancedTrayPriority_Object=MibScalar
brPrtAdvancedTrayPriority=_BrPrtAdvancedTrayPriority_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,1),_BrPrtAdvancedTrayPriority_Type())
brPrtAdvancedTrayPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAdvancedTrayPriority.setStatus(_A)
_BrTrayPriorityCount_Type=Integer32
_BrTrayPriorityCount_Object=MibScalar
brTrayPriorityCount=_BrTrayPriorityCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,2),_BrTrayPriorityCount_Type())
brTrayPriorityCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brTrayPriorityCount.setStatus(_A)
_BrTrayPriorityTable_Object=MibTable
brTrayPriorityTable=_BrTrayPriorityTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,3))
if mibBuilder.loadTexts:brTrayPriorityTable.setStatus(_A)
_BrTrayPriorityEntry_Object=MibTableRow
brTrayPriorityEntry=_BrTrayPriorityEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,3,1))
brTrayPriorityEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:brTrayPriorityEntry.setStatus(_A)
class _BrTrayPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrTrayPriorityIndex_Type.__name__=_B
_BrTrayPriorityIndex_Object=MibTableColumn
brTrayPriorityIndex=_BrTrayPriorityIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,3,1,1),_BrTrayPriorityIndex_Type())
brTrayPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brTrayPriorityIndex.setStatus(_A)
_BrTrayPriorityMember_Type=OctetString
_BrTrayPriorityMember_Object=MibTableColumn
brTrayPriorityMember=_BrTrayPriorityMember_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,52,3,1,2),_BrTrayPriorityMember_Type())
brTrayPriorityMember.setMaxAccess(_D)
if mibBuilder.loadTexts:brTrayPriorityMember.setStatus(_A)
_CarbonCopy_ObjectIdentity=ObjectIdentity
carbonCopy=_CarbonCopy_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53))
class _BrCarbonCopyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_v,2),(_w,3),('parallel',4)))
_BrCarbonCopyMode_Type.__name__=_B
_BrCarbonCopyMode_Object=MibScalar
brCarbonCopyMode=_BrCarbonCopyMode_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,1),_BrCarbonCopyMode_Type())
brCarbonCopyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brCarbonCopyMode.setStatus(_A)
_BrCarbonCopies_Type=Integer32
_BrCarbonCopies_Object=MibScalar
brCarbonCopies=_BrCarbonCopies_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,2),_BrCarbonCopies_Type())
brCarbonCopies.setMaxAccess(_C)
if mibBuilder.loadTexts:brCarbonCopies.setStatus(_A)
_BrCarbonCopyTable_Object=MibTable
brCarbonCopyTable=_BrCarbonCopyTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10))
if mibBuilder.loadTexts:brCarbonCopyTable.setStatus(_A)
_BrCarbonCopyEntry_Object=MibTableRow
brCarbonCopyEntry=_BrCarbonCopyEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10,1))
brCarbonCopyEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:brCarbonCopyEntry.setStatus(_A)
class _BrCarbonCopyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCarbonCopyIndex_Type.__name__=_B
_BrCarbonCopyIndex_Object=MibTableColumn
brCarbonCopyIndex=_BrCarbonCopyIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10,1,1),_BrCarbonCopyIndex_Type())
brCarbonCopyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCarbonCopyIndex.setStatus(_A)
class _BrCarbonCopyTray_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10,11)));namedValues=NamedValues(*(('tray1',1),('tray2',2),('tray3',3),('tray4',4),('mpTray',10),(_w,11)))
_BrCarbonCopyTray_Type.__name__=_B
_BrCarbonCopyTray_Object=MibTableColumn
brCarbonCopyTray=_BrCarbonCopyTray_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10,1,2),_BrCarbonCopyTray_Type())
brCarbonCopyTray.setMaxAccess(_C)
if mibBuilder.loadTexts:brCarbonCopyTray.setStatus(_A)
class _BrCarbonCopyMacro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrCarbonCopyMacro_Type.__name__=_B
_BrCarbonCopyMacro_Object=MibTableColumn
brCarbonCopyMacro=_BrCarbonCopyMacro_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10,1,3),_BrCarbonCopyMacro_Type())
brCarbonCopyMacro.setMaxAccess(_C)
if mibBuilder.loadTexts:brCarbonCopyMacro.setStatus(_A)
_BrCarbonCopyMacroID_Type=Integer32
_BrCarbonCopyMacroID_Object=MibTableColumn
brCarbonCopyMacroID=_BrCarbonCopyMacroID_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,53,10,1,4),_BrCarbonCopyMacroID_Type())
brCarbonCopyMacroID.setMaxAccess(_C)
if mibBuilder.loadTexts:brCarbonCopyMacroID.setStatus(_A)
_MediaFix_ObjectIdentity=ObjectIdentity
mediaFix=_MediaFix_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54))
class _BrMediaFixTray1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_z,2),(_A0,3),(_A1,4),(_x,5),(_A2,6),(_A3,7),(_I,8),(_A4,9),(_A5,10),(_A6,11)))
_BrMediaFixTray1_Type.__name__=_B
_BrMediaFixTray1_Object=MibScalar
brMediaFixTray1=_BrMediaFixTray1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54,1),_BrMediaFixTray1_Type())
brMediaFixTray1.setMaxAccess(_C)
if mibBuilder.loadTexts:brMediaFixTray1.setStatus(_A)
class _BrMediaFixTray2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_z,2),(_A0,3),(_A1,4),(_x,5),(_A2,6),(_A3,7),(_I,8),(_A4,9),(_A5,10),(_A6,11)))
_BrMediaFixTray2_Type.__name__=_B
_BrMediaFixTray2_Object=MibScalar
brMediaFixTray2=_BrMediaFixTray2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54,2),_BrMediaFixTray2_Type())
brMediaFixTray2.setMaxAccess(_C)
if mibBuilder.loadTexts:brMediaFixTray2.setStatus(_A)
class _BrMediaFixTray3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_z,2),(_A0,3),(_A1,4),(_x,5),(_A2,6),(_A3,7),(_I,8),(_A4,9),(_A5,10),(_A6,11)))
_BrMediaFixTray3_Type.__name__=_B
_BrMediaFixTray3_Object=MibScalar
brMediaFixTray3=_BrMediaFixTray3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54,3),_BrMediaFixTray3_Type())
brMediaFixTray3.setMaxAccess(_C)
if mibBuilder.loadTexts:brMediaFixTray3.setStatus(_A)
class _BrMediaFixTray4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_z,2),(_A0,3),(_A1,4),(_x,5),(_A2,6),(_A3,7),(_I,8),(_A4,9),(_A5,10),(_A6,11)))
_BrMediaFixTray4_Type.__name__=_B
_BrMediaFixTray4_Object=MibScalar
brMediaFixTray4=_BrMediaFixTray4_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54,4),_BrMediaFixTray4_Type())
brMediaFixTray4.setMaxAccess(_C)
if mibBuilder.loadTexts:brMediaFixTray4.setStatus(_A)
class _BrMediaFixMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_z,2),(_A0,3),(_A1,4),(_x,5),(_A2,6),(_A3,7),(_I,8),(_A4,9),(_A5,10),(_A6,11)))
_BrMediaFixMP_Type.__name__=_B
_BrMediaFixMP_Object=MibScalar
brMediaFixMP=_BrMediaFixMP_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,54,10),_BrMediaFixMP_Type())
brMediaFixMP.setMaxAccess(_C)
if mibBuilder.loadTexts:brMediaFixMP.setStatus(_A)
_Directprint_ObjectIdentity=ObjectIdentity
directprint=_Directprint_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60))
class _BrDirectPrintPaperSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922,923,924,925,926,927)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922),('a5l',923),('b6jis',924),(_AP,925),(_AQ,926),(_AR,927)))
_BrDirectPrintPaperSize_Type.__name__=_B
_BrDirectPrintPaperSize_Object=MibScalar
brDirectPrintPaperSize=_BrDirectPrintPaperSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,1),_BrDirectPrintPaperSize_Type())
brDirectPrintPaperSize.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintPaperSize.setStatus(_A)
_BrDirectPrintMediaType_Type=Integer32
_BrDirectPrintMediaType_Object=MibScalar
brDirectPrintMediaType=_BrDirectPrintMediaType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,2),_BrDirectPrintMediaType_Type())
brDirectPrintMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintMediaType.setStatus(_A)
_BrDirectPrintMultipulPage_Type=Integer32
_BrDirectPrintMultipulPage_Object=MibScalar
brDirectPrintMultipulPage=_BrDirectPrintMultipulPage_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,3),_BrDirectPrintMultipulPage_Type())
brDirectPrintMultipulPage.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintMultipulPage.setStatus(_A)
_BrDirectPrintOrientation_Type=Integer32
_BrDirectPrintOrientation_Object=MibScalar
brDirectPrintOrientation=_BrDirectPrintOrientation_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,4),_BrDirectPrintOrientation_Type())
brDirectPrintOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintOrientation.setStatus(_A)
_BrDirectPrintCollate_Type=Integer32
_BrDirectPrintCollate_Object=MibScalar
brDirectPrintCollate=_BrDirectPrintCollate_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,5),_BrDirectPrintCollate_Type())
brDirectPrintCollate.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintCollate.setStatus(_A)
_BrDirectPrintOutputColor_Type=Integer32
_BrDirectPrintOutputColor_Object=MibScalar
brDirectPrintOutputColor=_BrDirectPrintOutputColor_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,6),_BrDirectPrintOutputColor_Type())
brDirectPrintOutputColor.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintOutputColor.setStatus(_A)
_BrDirectPrintPrintQuality_Type=Integer32
_BrDirectPrintPrintQuality_Object=MibScalar
brDirectPrintPrintQuality=_BrDirectPrintPrintQuality_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,7),_BrDirectPrintPrintQuality_Type())
brDirectPrintPrintQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintPrintQuality.setStatus(_A)
_BrDirectPrintPdfOption_Type=Integer32
_BrDirectPrintPdfOption_Object=MibScalar
brDirectPrintPdfOption=_BrDirectPrintPdfOption_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,8),_BrDirectPrintPdfOption_Type())
brDirectPrintPdfOption.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintPdfOption.setStatus(_A)
_BrDirectPrintSetting_Type=Integer32
_BrDirectPrintSetting_Object=MibScalar
brDirectPrintSetting=_BrDirectPrintSetting_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,9),_BrDirectPrintSetting_Type())
brDirectPrintSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:brDirectPrintSetting.setStatus(_A)
class _BrDirectPrintPdfThumbnailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alternativeImage',1),('reductionImage',2)))
_BrDirectPrintPdfThumbnailType_Type.__name__=_B
_BrDirectPrintPdfThumbnailType_Object=MibScalar
brDirectPrintPdfThumbnailType=_BrDirectPrintPdfThumbnailType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,60,10),_BrDirectPrintPdfThumbnailType_Type())
brDirectPrintPdfThumbnailType.setMaxAccess(_C)
if mibBuilder.loadTexts:brDirectPrintPdfThumbnailType.setStatus(_A)
_Pictbridge_ObjectIdentity=ObjectIdentity
pictbridge=_Pictbridge_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61))
class _BrPictBridgePaperSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,911,920,921,922)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),(_r,911),(_s,920),(_t,921),(_u,922)))
_BrPictBridgePaperSize_Type.__name__=_B
_BrPictBridgePaperSize_Object=MibScalar
brPictBridgePaperSize=_BrPictBridgePaperSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,1),_BrPictBridgePaperSize_Type())
brPictBridgePaperSize.setMaxAccess(_C)
if mibBuilder.loadTexts:brPictBridgePaperSize.setStatus(_A)
_BrPictBridgeOrientation_Type=Integer32
_BrPictBridgeOrientation_Object=MibScalar
brPictBridgeOrientation=_BrPictBridgeOrientation_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,2),_BrPictBridgeOrientation_Type())
brPictBridgeOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:brPictBridgeOrientation.setStatus(_A)
_BrPictBridgeDateTime_Type=Integer32
_BrPictBridgeDateTime_Object=MibScalar
brPictBridgeDateTime=_BrPictBridgeDateTime_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,3),_BrPictBridgeDateTime_Type())
brPictBridgeDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brPictBridgeDateTime.setStatus(_A)
_BrPictBridgeFileName_Type=Integer32
_BrPictBridgeFileName_Object=MibScalar
brPictBridgeFileName=_BrPictBridgeFileName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,4),_BrPictBridgeFileName_Type())
brPictBridgeFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:brPictBridgeFileName.setStatus(_A)
_BrPictBridgePrintQuality_Type=Integer32
_BrPictBridgePrintQuality_Object=MibScalar
brPictBridgePrintQuality=_BrPictBridgePrintQuality_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,5),_BrPictBridgePrintQuality_Type())
brPictBridgePrintQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:brPictBridgePrintQuality.setStatus(_A)
_BrPictBridgePrintSetting_Type=Integer32
_BrPictBridgePrintSetting_Object=MibScalar
brPictBridgePrintSetting=_BrPictBridgePrintSetting_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,61,6),_BrPictBridgePrintSetting_Type())
brPictBridgePrintSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:brPictBridgePrintSetting.setStatus(_A)
_Colorcorrection_ObjectIdentity=ObjectIdentity
colorcorrection=_Colorcorrection_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62))
_BrColorCalibration_Type=Integer32
_BrColorCalibration_Object=MibScalar
brColorCalibration=_BrColorCalibration_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,1),_BrColorCalibration_Type())
brColorCalibration.setMaxAccess(_C)
if mibBuilder.loadTexts:brColorCalibration.setStatus(_A)
_BrColorCalibrationReset_Type=Integer32
_BrColorCalibrationReset_Object=MibScalar
brColorCalibrationReset=_BrColorCalibrationReset_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,2),_BrColorCalibrationReset_Type())
brColorCalibrationReset.setMaxAccess(_C)
if mibBuilder.loadTexts:brColorCalibrationReset.setStatus(_A)
_BrAutoRegistRegistrate_Type=Integer32
_BrAutoRegistRegistrate_Object=MibScalar
brAutoRegistRegistrate=_BrAutoRegistRegistrate_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,3),_BrAutoRegistRegistrate_Type())
brAutoRegistRegistrate.setMaxAccess(_C)
if mibBuilder.loadTexts:brAutoRegistRegistrate.setStatus(_A)
_BrAutoRegistSetInterval_Type=Integer32
_BrAutoRegistSetInterval_Object=MibScalar
brAutoRegistSetInterval=_BrAutoRegistSetInterval_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,4),_BrAutoRegistSetInterval_Type())
brAutoRegistSetInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:brAutoRegistSetInterval.setStatus(_A)
_BrRegistrationPrintChart_Type=Integer32
_BrRegistrationPrintChart_Object=MibScalar
brRegistrationPrintChart=_BrRegistrationPrintChart_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,5),_BrRegistrationPrintChart_Type())
brRegistrationPrintChart.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationPrintChart.setStatus(_A)
_BrRegistrationXMagentaLeft_Type=Integer32
_BrRegistrationXMagentaLeft_Object=MibScalar
brRegistrationXMagentaLeft=_BrRegistrationXMagentaLeft_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,6),_BrRegistrationXMagentaLeft_Type())
brRegistrationXMagentaLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXMagentaLeft.setStatus(_A)
_BrRegistrationXMagentaRight_Type=Integer32
_BrRegistrationXMagentaRight_Object=MibScalar
brRegistrationXMagentaRight=_BrRegistrationXMagentaRight_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,7),_BrRegistrationXMagentaRight_Type())
brRegistrationXMagentaRight.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXMagentaRight.setStatus(_A)
_BrRegistrationXCyanLeft_Type=Integer32
_BrRegistrationXCyanLeft_Object=MibScalar
brRegistrationXCyanLeft=_BrRegistrationXCyanLeft_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,8),_BrRegistrationXCyanLeft_Type())
brRegistrationXCyanLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXCyanLeft.setStatus(_A)
_BrRegistrationXCyanRight_Type=Integer32
_BrRegistrationXCyanRight_Object=MibScalar
brRegistrationXCyanRight=_BrRegistrationXCyanRight_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,9),_BrRegistrationXCyanRight_Type())
brRegistrationXCyanRight.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXCyanRight.setStatus(_A)
_BrRegistrationXYellowLeft_Type=Integer32
_BrRegistrationXYellowLeft_Object=MibScalar
brRegistrationXYellowLeft=_BrRegistrationXYellowLeft_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,10),_BrRegistrationXYellowLeft_Type())
brRegistrationXYellowLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXYellowLeft.setStatus(_A)
_BrRegistrationXYellowRight_Type=Integer32
_BrRegistrationXYellowRight_Object=MibScalar
brRegistrationXYellowRight=_BrRegistrationXYellowRight_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,11),_BrRegistrationXYellowRight_Type())
brRegistrationXYellowRight.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationXYellowRight.setStatus(_A)
_BrRegistrationYMagenta_Type=Integer32
_BrRegistrationYMagenta_Object=MibScalar
brRegistrationYMagenta=_BrRegistrationYMagenta_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,12),_BrRegistrationYMagenta_Type())
brRegistrationYMagenta.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationYMagenta.setStatus(_A)
_BrRegistrationYCyan_Type=Integer32
_BrRegistrationYCyan_Object=MibScalar
brRegistrationYCyan=_BrRegistrationYCyan_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,13),_BrRegistrationYCyan_Type())
brRegistrationYCyan.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationYCyan.setStatus(_A)
_BrRegistrationYYellow_Type=Integer32
_BrRegistrationYYellow_Object=MibScalar
brRegistrationYYellow=_BrRegistrationYYellow_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,62,14),_BrRegistrationYYellow_Type())
brRegistrationYYellow.setMaxAccess(_C)
if mibBuilder.loadTexts:brRegistrationYYellow.setStatus(_A)
_Funclock_ObjectIdentity=ObjectIdentity
funclock=_Funclock_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63))
_BrFuncLockSettingInit_Type=Integer32
_BrFuncLockSettingInit_Object=MibScalar
brFuncLockSettingInit=_BrFuncLockSettingInit_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,1),_BrFuncLockSettingInit_Type())
brFuncLockSettingInit.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockSettingInit.setStatus(_A)
_BrFuncLockAdminPassword_Type=DisplayString
_BrFuncLockAdminPassword_Object=MibScalar
brFuncLockAdminPassword=_BrFuncLockAdminPassword_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,2),_BrFuncLockAdminPassword_Type())
brFuncLockAdminPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockAdminPassword.setStatus(_A)
class _BrFuncLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_BrFuncLock_Type.__name__=_B
_BrFuncLock_Object=MibScalar
brFuncLock=_BrFuncLock_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,3),_BrFuncLock_Type())
brFuncLock.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLock.setStatus(_A)
class _BrFuncLockPublicFuncCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrFuncLockPublicFuncCount_Type.__name__=_B
_BrFuncLockPublicFuncCount_Object=MibScalar
brFuncLockPublicFuncCount=_BrFuncLockPublicFuncCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,4),_BrFuncLockPublicFuncCount_Type())
brFuncLockPublicFuncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicFuncCount.setStatus(_A)
_BrFuncLockPublicTable_Object=MibTable
brFuncLockPublicTable=_BrFuncLockPublicTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5))
if mibBuilder.loadTexts:brFuncLockPublicTable.setStatus(_A)
_BrFuncLockPublicEntry_Object=MibTableRow
brFuncLockPublicEntry=_BrFuncLockPublicEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5,1))
brFuncLockPublicEntry.setIndexNames((0,_E,_AU))
if mibBuilder.loadTexts:brFuncLockPublicEntry.setStatus(_A)
class _BrFuncLockPublicFuncIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrFuncLockPublicFuncIndex_Type.__name__=_B
_BrFuncLockPublicFuncIndex_Object=MibTableColumn
brFuncLockPublicFuncIndex=_BrFuncLockPublicFuncIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5,1,1),_BrFuncLockPublicFuncIndex_Type())
brFuncLockPublicFuncIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicFuncIndex.setStatus(_A)
class _BrFuncLockPublicFuncMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AH,1),('copybr',2),('faxtx',3),('faxrx',4),('scan',5),(_AI,6),('pcc',7)))
_BrFuncLockPublicFuncMember_Type.__name__=_B
_BrFuncLockPublicFuncMember_Object=MibTableColumn
brFuncLockPublicFuncMember=_BrFuncLockPublicFuncMember_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5,1,2),_BrFuncLockPublicFuncMember_Type())
brFuncLockPublicFuncMember.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicFuncMember.setStatus(_A)
class _BrFuncLockPublicFuncSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockPublicFuncSupported_Type.__name__=_B
_BrFuncLockPublicFuncSupported_Object=MibTableColumn
brFuncLockPublicFuncSupported=_BrFuncLockPublicFuncSupported_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5,1,3),_BrFuncLockPublicFuncSupported_Type())
brFuncLockPublicFuncSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicFuncSupported.setStatus(_A)
class _BrFuncLockPublicFuncEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockPublicFuncEnable_Type.__name__=_B
_BrFuncLockPublicFuncEnable_Object=MibTableColumn
brFuncLockPublicFuncEnable=_BrFuncLockPublicFuncEnable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,5,1,4),_BrFuncLockPublicFuncEnable_Type())
brFuncLockPublicFuncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPublicFuncEnable.setStatus(_A)
class _BrFuncLockUserCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrFuncLockUserCount_Type.__name__=_B
_BrFuncLockUserCount_Object=MibScalar
brFuncLockUserCount=_BrFuncLockUserCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,6),_BrFuncLockUserCount_Type())
brFuncLockUserCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserCount.setStatus(_A)
_BrFuncLockUserTable_Object=MibTable
brFuncLockUserTable=_BrFuncLockUserTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,7))
if mibBuilder.loadTexts:brFuncLockUserTable.setStatus(_A)
_BrFuncLockUserEntry_Object=MibTableRow
brFuncLockUserEntry=_BrFuncLockUserEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,7,1))
brFuncLockUserEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:brFuncLockUserEntry.setStatus(_A)
class _BrFuncLockUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrFuncLockUserIndex_Type.__name__=_B
_BrFuncLockUserIndex_Object=MibTableColumn
brFuncLockUserIndex=_BrFuncLockUserIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,7,1,1),_BrFuncLockUserIndex_Type())
brFuncLockUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserIndex.setStatus(_A)
_BrFuncLockUserName_Type=DisplayString
_BrFuncLockUserName_Object=MibTableColumn
brFuncLockUserName=_BrFuncLockUserName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,7,1,2),_BrFuncLockUserName_Type())
brFuncLockUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserName.setStatus(_A)
_BrFuncLockUserPassword_Type=DisplayString
_BrFuncLockUserPassword_Object=MibTableColumn
brFuncLockUserPassword=_BrFuncLockUserPassword_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,7,1,3),_BrFuncLockUserPassword_Type())
brFuncLockUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserPassword.setStatus(_A)
class _BrFuncLockUserFuncCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BrFuncLockUserFuncCount_Type.__name__=_B
_BrFuncLockUserFuncCount_Object=MibScalar
brFuncLockUserFuncCount=_BrFuncLockUserFuncCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,8),_BrFuncLockUserFuncCount_Type())
brFuncLockUserFuncCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserFuncCount.setStatus(_A)
_BrFuncLockUserFuncTable_Object=MibTable
brFuncLockUserFuncTable=_BrFuncLockUserFuncTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9))
if mibBuilder.loadTexts:brFuncLockUserFuncTable.setStatus(_A)
_BrFuncLockUserFuncEntry_Object=MibTableRow
brFuncLockUserFuncEntry=_BrFuncLockUserFuncEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9,1))
brFuncLockUserFuncEntry.setIndexNames((0,_E,_AJ),(0,_E,_AV))
if mibBuilder.loadTexts:brFuncLockUserFuncEntry.setStatus(_A)
class _BrFuncLockUserFuncIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrFuncLockUserFuncIndex_Type.__name__=_B
_BrFuncLockUserFuncIndex_Object=MibTableColumn
brFuncLockUserFuncIndex=_BrFuncLockUserFuncIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9,1,1),_BrFuncLockUserFuncIndex_Type())
brFuncLockUserFuncIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserFuncIndex.setStatus(_A)
class _BrFuncLockUserFuncMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AH,1),('copybr',2),('faxtx',3),('faxrx',4),('scan',5),(_AI,6),('pcc',7)))
_BrFuncLockUserFuncMember_Type.__name__=_B
_BrFuncLockUserFuncMember_Object=MibTableColumn
brFuncLockUserFuncMember=_BrFuncLockUserFuncMember_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9,1,2),_BrFuncLockUserFuncMember_Type())
brFuncLockUserFuncMember.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserFuncMember.setStatus(_A)
class _BrFuncLockUserFuncSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockUserFuncSupported_Type.__name__=_B
_BrFuncLockUserFuncSupported_Object=MibTableColumn
brFuncLockUserFuncSupported=_BrFuncLockUserFuncSupported_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9,1,3),_BrFuncLockUserFuncSupported_Type())
brFuncLockUserFuncSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserFuncSupported.setStatus(_A)
class _BrFuncLockUserFuncEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockUserFuncEnable_Type.__name__=_B
_BrFuncLockUserFuncEnable_Object=MibTableColumn
brFuncLockUserFuncEnable=_BrFuncLockUserFuncEnable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,9,1,4),_BrFuncLockUserFuncEnable_Type())
brFuncLockUserFuncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserFuncEnable.setStatus(_A)
_BrFuncLockSetting_Type=Integer32
_BrFuncLockSetting_Object=MibScalar
brFuncLockSetting=_BrFuncLockSetting_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,10),_BrFuncLockSetting_Type())
brFuncLockSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockSetting.setStatus(_A)
class _BrFuncLockUserPrintPageCounterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_BrFuncLockUserPrintPageCounterReset_Type.__name__=_B
_BrFuncLockUserPrintPageCounterReset_Object=MibScalar
brFuncLockUserPrintPageCounterReset=_BrFuncLockUserPrintPageCounterReset_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,20),_BrFuncLockUserPrintPageCounterReset_Type())
brFuncLockUserPrintPageCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserPrintPageCounterReset.setStatus(_A)
class _BrFuncLockPublicPrintLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockPublicPrintLimitEnable_Type.__name__=_B
_BrFuncLockPublicPrintLimitEnable_Object=MibScalar
brFuncLockPublicPrintLimitEnable=_BrFuncLockPublicPrintLimitEnable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,21),_BrFuncLockPublicPrintLimitEnable_Type())
brFuncLockPublicPrintLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPublicPrintLimitEnable.setStatus(_A)
class _BrFuncLockPublicPrintPageMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999))
_BrFuncLockPublicPrintPageMax_Type.__name__=_B
_BrFuncLockPublicPrintPageMax_Object=MibScalar
brFuncLockPublicPrintPageMax=_BrFuncLockPublicPrintPageMax_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,22),_BrFuncLockPublicPrintPageMax_Type())
brFuncLockPublicPrintPageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPublicPrintPageMax.setStatus(_A)
class _BrFuncLockPublicPrintPageCountMono_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockPublicPrintPageCountMono_Type.__name__=_B
_BrFuncLockPublicPrintPageCountMono_Object=MibScalar
brFuncLockPublicPrintPageCountMono=_BrFuncLockPublicPrintPageCountMono_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,23),_BrFuncLockPublicPrintPageCountMono_Type())
brFuncLockPublicPrintPageCountMono.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicPrintPageCountMono.setStatus(_A)
class _BrFuncLockPublicPrintPageCountColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockPublicPrintPageCountColor_Type.__name__=_B
_BrFuncLockPublicPrintPageCountColor_Object=MibScalar
brFuncLockPublicPrintPageCountColor=_BrFuncLockPublicPrintPageCountColor_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,24),_BrFuncLockPublicPrintPageCountColor_Type())
brFuncLockPublicPrintPageCountColor.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicPrintPageCountColor.setStatus(_A)
_BrFuncLockUserPrintPageTable_Object=MibTable
brFuncLockUserPrintPageTable=_BrFuncLockUserPrintPageTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25))
if mibBuilder.loadTexts:brFuncLockUserPrintPageTable.setStatus(_A)
_BrFuncLockUserPrintPageEntry_Object=MibTableRow
brFuncLockUserPrintPageEntry=_BrFuncLockUserPrintPageEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1))
brFuncLockUserPrintPageEntry.setIndexNames((0,_E,_AW))
if mibBuilder.loadTexts:brFuncLockUserPrintPageEntry.setStatus(_A)
class _BrFuncLockUserPrintPageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrFuncLockUserPrintPageIndex_Type.__name__=_B
_BrFuncLockUserPrintPageIndex_Object=MibTableColumn
brFuncLockUserPrintPageIndex=_BrFuncLockUserPrintPageIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,1),_BrFuncLockUserPrintPageIndex_Type())
brFuncLockUserPrintPageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserPrintPageIndex.setStatus(_A)
class _BrFuncLockUserPrintPageLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockUserPrintPageLimitEnable_Type.__name__=_B
_BrFuncLockUserPrintPageLimitEnable_Object=MibTableColumn
brFuncLockUserPrintPageLimitEnable=_BrFuncLockUserPrintPageLimitEnable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,2),_BrFuncLockUserPrintPageLimitEnable_Type())
brFuncLockUserPrintPageLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserPrintPageLimitEnable.setStatus(_A)
class _BrFuncLockUserPrintPageCountMono_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockUserPrintPageCountMono_Type.__name__=_B
_BrFuncLockUserPrintPageCountMono_Object=MibTableColumn
brFuncLockUserPrintPageCountMono=_BrFuncLockUserPrintPageCountMono_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,3),_BrFuncLockUserPrintPageCountMono_Type())
brFuncLockUserPrintPageCountMono.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserPrintPageCountMono.setStatus(_A)
class _BrFuncLockUserPrintPageCountColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockUserPrintPageCountColor_Type.__name__=_B
_BrFuncLockUserPrintPageCountColor_Object=MibTableColumn
brFuncLockUserPrintPageCountColor=_BrFuncLockUserPrintPageCountColor_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,4),_BrFuncLockUserPrintPageCountColor_Type())
brFuncLockUserPrintPageCountColor.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserPrintPageCountColor.setStatus(_A)
class _BrFuncLockUserPrintPageMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999))
_BrFuncLockUserPrintPageMax_Type.__name__=_B
_BrFuncLockUserPrintPageMax_Object=MibTableColumn
brFuncLockUserPrintPageMax=_BrFuncLockUserPrintPageMax_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,5),_BrFuncLockUserPrintPageMax_Type())
brFuncLockUserPrintPageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockUserPrintPageMax.setStatus(_A)
class _BrFuncLockUserPrintPageCountMonoLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockUserPrintPageCountMonoLast_Type.__name__=_B
_BrFuncLockUserPrintPageCountMonoLast_Object=MibTableColumn
brFuncLockUserPrintPageCountMonoLast=_BrFuncLockUserPrintPageCountMonoLast_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,6),_BrFuncLockUserPrintPageCountMonoLast_Type())
brFuncLockUserPrintPageCountMonoLast.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserPrintPageCountMonoLast.setStatus(_A)
class _BrFuncLockUserPrintPageCountColorLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockUserPrintPageCountColorLast_Type.__name__=_B
_BrFuncLockUserPrintPageCountColorLast_Object=MibTableColumn
brFuncLockUserPrintPageCountColorLast=_BrFuncLockUserPrintPageCountColorLast_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,25,1,7),_BrFuncLockUserPrintPageCountColorLast_Type())
brFuncLockUserPrintPageCountColorLast.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockUserPrintPageCountColorLast.setStatus(_A)
class _BrFuncLockPcLoginNameAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFuncLockPcLoginNameAuthEnable_Type.__name__=_B
_BrFuncLockPcLoginNameAuthEnable_Object=MibScalar
brFuncLockPcLoginNameAuthEnable=_BrFuncLockPcLoginNameAuthEnable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,26),_BrFuncLockPcLoginNameAuthEnable_Type())
brFuncLockPcLoginNameAuthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPcLoginNameAuthEnable.setStatus(_A)
_BrFuncLockPcLoginNameAuthCount_Type=Integer32
_BrFuncLockPcLoginNameAuthCount_Object=MibScalar
brFuncLockPcLoginNameAuthCount=_BrFuncLockPcLoginNameAuthCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,27),_BrFuncLockPcLoginNameAuthCount_Type())
brFuncLockPcLoginNameAuthCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPcLoginNameAuthCount.setStatus(_A)
_BrFuncLockPcLoginNameTable_Object=MibTable
brFuncLockPcLoginNameTable=_BrFuncLockPcLoginNameTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,28))
if mibBuilder.loadTexts:brFuncLockPcLoginNameTable.setStatus(_A)
_BrFuncLockPcLoginNameEntry_Object=MibTableRow
brFuncLockPcLoginNameEntry=_BrFuncLockPcLoginNameEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,28,1))
brFuncLockPcLoginNameEntry.setIndexNames((0,_E,_AX))
if mibBuilder.loadTexts:brFuncLockPcLoginNameEntry.setStatus(_A)
class _BrFuncLockPcLoginNameAuthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_BrFuncLockPcLoginNameAuthIndex_Type.__name__=_B
_BrFuncLockPcLoginNameAuthIndex_Object=MibTableColumn
brFuncLockPcLoginNameAuthIndex=_BrFuncLockPcLoginNameAuthIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,28,1,1),_BrFuncLockPcLoginNameAuthIndex_Type())
brFuncLockPcLoginNameAuthIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPcLoginNameAuthIndex.setStatus(_A)
_BrFuncLockPcLoginName_Type=OctetString
_BrFuncLockPcLoginName_Object=MibTableColumn
brFuncLockPcLoginName=_BrFuncLockPcLoginName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,28,1,2),_BrFuncLockPcLoginName_Type())
brFuncLockPcLoginName.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPcLoginName.setStatus(_A)
class _BrFuncLockPcLoginNameAuthID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_BrFuncLockPcLoginNameAuthID_Type.__name__=_B
_BrFuncLockPcLoginNameAuthID_Object=MibTableColumn
brFuncLockPcLoginNameAuthID=_BrFuncLockPcLoginNameAuthID_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,28,1,3),_BrFuncLockPcLoginNameAuthID_Type())
brFuncLockPcLoginNameAuthID.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockPcLoginNameAuthID.setStatus(_A)
class _BrFuncLockPublicPrintPageCountMonoLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockPublicPrintPageCountMonoLast_Type.__name__=_B
_BrFuncLockPublicPrintPageCountMonoLast_Object=MibScalar
brFuncLockPublicPrintPageCountMonoLast=_BrFuncLockPublicPrintPageCountMonoLast_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,29),_BrFuncLockPublicPrintPageCountMonoLast_Type())
brFuncLockPublicPrintPageCountMonoLast.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicPrintPageCountMonoLast.setStatus(_A)
class _BrFuncLockPublicPrintPageCountColorLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFuncLockPublicPrintPageCountColorLast_Type.__name__=_B
_BrFuncLockPublicPrintPageCountColorLast_Object=MibScalar
brFuncLockPublicPrintPageCountColorLast=_BrFuncLockPublicPrintPageCountColorLast_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,30),_BrFuncLockPublicPrintPageCountColorLast_Type())
brFuncLockPublicPrintPageCountColorLast.setMaxAccess(_D)
if mibBuilder.loadTexts:brFuncLockPublicPrintPageCountColorLast.setStatus(_A)
_Autocountreset_ObjectIdentity=ObjectIdentity
autocountreset=_Autocountreset_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,31))
class _BrFuncLockAutoCountResetFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrFuncLockAutoCountResetFrequency_Type.__name__=_B
_BrFuncLockAutoCountResetFrequency_Object=MibScalar
brFuncLockAutoCountResetFrequency=_BrFuncLockAutoCountResetFrequency_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,31,1),_BrFuncLockAutoCountResetFrequency_Type())
brFuncLockAutoCountResetFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockAutoCountResetFrequency.setStatus(_A)
class _BrFuncLockAutoCountResetTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_BrFuncLockAutoCountResetTime_Type.__name__=_G
_BrFuncLockAutoCountResetTime_Object=MibScalar
brFuncLockAutoCountResetTime=_BrFuncLockAutoCountResetTime_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,31,2),_BrFuncLockAutoCountResetTime_Type())
brFuncLockAutoCountResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockAutoCountResetTime.setStatus(_A)
class _BrFuncLockAutoCountResetWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_BrFuncLockAutoCountResetWeek_Type.__name__=_B
_BrFuncLockAutoCountResetWeek_Object=MibScalar
brFuncLockAutoCountResetWeek=_BrFuncLockAutoCountResetWeek_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,31,3),_BrFuncLockAutoCountResetWeek_Type())
brFuncLockAutoCountResetWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockAutoCountResetWeek.setStatus(_A)
class _BrFuncLockAutoCountResetDate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_BrFuncLockAutoCountResetDate_Type.__name__=_B
_BrFuncLockAutoCountResetDate_Object=MibScalar
brFuncLockAutoCountResetDate=_BrFuncLockAutoCountResetDate_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,2,63,31,4),_BrFuncLockAutoCountResetDate_Type())
brFuncLockAutoCountResetDate.setMaxAccess(_C)
if mibBuilder.loadTexts:brFuncLockAutoCountResetDate.setStatus(_A)
_Mail_ObjectIdentity=ObjectIdentity
mail=_Mail_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3))
class _BrPrtMailbox_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtMailbox_Type.__name__=_B
_BrPrtMailbox_Object=MibScalar
brPrtMailbox=_BrPrtMailbox_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,1),_BrPrtMailbox_Type())
brPrtMailbox.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtMailbox.setStatus(_A)
_BrPrtMailboxProtectTable_Object=MibTable
brPrtMailboxProtectTable=_BrPrtMailboxProtectTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,2))
if mibBuilder.loadTexts:brPrtMailboxProtectTable.setStatus(_A)
_BrPrtMailboxProtectEntry_Object=MibTableRow
brPrtMailboxProtectEntry=_BrPrtMailboxProtectEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,2,1))
brPrtMailboxProtectEntry.setIndexNames((0,_E,_AY))
if mibBuilder.loadTexts:brPrtMailboxProtectEntry.setStatus(_A)
class _BrPrtMailboxProtectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPrtMailboxProtectIndex_Type.__name__=_B
_BrPrtMailboxProtectIndex_Object=MibTableColumn
brPrtMailboxProtectIndex=_BrPrtMailboxProtectIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,2,1,1),_BrPrtMailboxProtectIndex_Type())
brPrtMailboxProtectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtMailboxProtectIndex.setStatus(_A)
class _BrPrtMailboxProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtMailboxProtect_Type.__name__=_B
_BrPrtMailboxProtect_Object=MibTableColumn
brPrtMailboxProtect=_BrPrtMailboxProtect_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,2,1,2),_BrPrtMailboxProtect_Type())
brPrtMailboxProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtMailboxProtect.setStatus(_A)
_BrPrtAvoidMailboxFullTable_Object=MibTable
brPrtAvoidMailboxFullTable=_BrPrtAvoidMailboxFullTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,3))
if mibBuilder.loadTexts:brPrtAvoidMailboxFullTable.setStatus(_A)
_BrPrtAvoidMailboxFullEntry_Object=MibTableRow
brPrtAvoidMailboxFullEntry=_BrPrtAvoidMailboxFullEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,3,1))
brPrtAvoidMailboxFullEntry.setIndexNames((0,_E,_AZ))
if mibBuilder.loadTexts:brPrtAvoidMailboxFullEntry.setStatus(_A)
class _BrPrtAvoidMailboxFullIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPrtAvoidMailboxFullIndex_Type.__name__=_B
_BrPrtAvoidMailboxFullIndex_Object=MibTableColumn
brPrtAvoidMailboxFullIndex=_BrPrtAvoidMailboxFullIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,3,1,1),_BrPrtAvoidMailboxFullIndex_Type())
brPrtAvoidMailboxFullIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAvoidMailboxFullIndex.setStatus(_A)
class _BrPrtAvoidMailboxFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtAvoidMailboxFull_Type.__name__=_B
_BrPrtAvoidMailboxFull_Object=MibTableColumn
brPrtAvoidMailboxFull=_BrPrtAvoidMailboxFull_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,3,1,2),_BrPrtAvoidMailboxFull_Type())
brPrtAvoidMailboxFull.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAvoidMailboxFull.setStatus(_A)
class _BrPrtMailboxOutbin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,110))
_BrPrtMailboxOutbin_Type.__name__=_B
_BrPrtMailboxOutbin_Object=MibScalar
brPrtMailboxOutbin=_BrPrtMailboxOutbin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,4),_BrPrtMailboxOutbin_Type())
brPrtMailboxOutbin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtMailboxOutbin.setStatus(_A)
class _BrPrtMailboxProtectGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_BrPrtMailboxProtectGroup_Type.__name__=_B
_BrPrtMailboxProtectGroup_Object=MibScalar
brPrtMailboxProtectGroup=_BrPrtMailboxProtectGroup_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,5),_BrPrtMailboxProtectGroup_Type())
brPrtMailboxProtectGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtMailboxProtectGroup.setStatus(_A)
class _BrPrtAvoidMailboxFullGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPrtAvoidMailboxFullGroup_Type.__name__=_B
_BrPrtAvoidMailboxFullGroup_Object=MibScalar
brPrtAvoidMailboxFullGroup=_BrPrtAvoidMailboxFullGroup_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,3,6),_BrPrtAvoidMailboxFullGroup_Type())
brPrtAvoidMailboxFullGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrtAvoidMailboxFullGroup.setStatus(_A)
_Finisher_ObjectIdentity=ObjectIdentity
finisher=_Finisher_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,4))
class _BrPrtFinisher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPrtFinisher_Type.__name__=_B
_BrPrtFinisher_Object=MibScalar
brPrtFinisher=_BrPrtFinisher_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,4,1),_BrPrtFinisher_Type())
brPrtFinisher.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrtFinisher.setStatus(_A)
_Catch_tray_ObjectIdentity=ObjectIdentity
catch_tray=_Catch_tray_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,5))
class _BrPrtCatchTray_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPrtCatchTray_Type.__name__=_B
_BrPrtCatchTray_Object=MibScalar
brPrtCatchTray=_BrPrtCatchTray_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,1,5,1),_BrPrtCatchTray_Type())
brPrtCatchTray.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrtCatchTray.setStatus(_A)
_Pagesetup_ObjectIdentity=ObjectIdentity
pagesetup=_Pagesetup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2))
_Pcl_ObjectIdentity=ObjectIdentity
pcl=_Pcl_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1))
_Margin_p_ObjectIdentity=ObjectIdentity
margin_p=_Margin_p_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1))
class _BrPagePCLLeftMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPagePCLLeftMargin_Type.__name__=_B
_BrPagePCLLeftMargin_Object=MibScalar
brPagePCLLeftMargin=_BrPagePCLLeftMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1,1),_BrPagePCLLeftMargin_Type())
brPagePCLLeftMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLLeftMargin.setStatus(_A)
class _BrPagePCLRightMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPagePCLRightMargin_Type.__name__=_B
_BrPagePCLRightMargin_Object=MibScalar
brPagePCLRightMargin=_BrPagePCLRightMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1,2),_BrPagePCLRightMargin_Type())
brPagePCLRightMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLRightMargin.setStatus(_A)
class _BrPagePCLTopMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPagePCLTopMargin_Type.__name__=_B
_BrPagePCLTopMargin_Object=MibScalar
brPagePCLTopMargin=_BrPagePCLTopMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1,3),_BrPagePCLTopMargin_Type())
brPagePCLTopMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLTopMargin.setStatus(_A)
class _BrPagePCLBottomMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPagePCLBottomMargin_Type.__name__=_B
_BrPagePCLBottomMargin_Object=MibScalar
brPagePCLBottomMargin=_BrPagePCLBottomMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1,4),_BrPagePCLBottomMargin_Type())
brPagePCLBottomMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLBottomMargin.setStatus(_A)
class _BrPagePCLLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,128))
_BrPagePCLLines_Type.__name__=_B
_BrPagePCLLines_Object=MibScalar
brPagePCLLines=_BrPagePCLLines_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,1,5),_BrPagePCLLines_Type())
brPagePCLLines.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLLines.setStatus(_A)
_Auto_p_ObjectIdentity=ObjectIdentity
auto_p=_Auto_p_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,2))
class _BrPagePCLAutoLF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPagePCLAutoLF_Type.__name__=_B
_BrPagePCLAutoLF_Object=MibScalar
brPagePCLAutoLF=_BrPagePCLAutoLF_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,2,1),_BrPagePCLAutoLF_Type())
brPagePCLAutoLF.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLAutoLF.setStatus(_A)
class _BrPagePCLAutoCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPagePCLAutoCR_Type.__name__=_B
_BrPagePCLAutoCR_Object=MibScalar
brPagePCLAutoCR=_BrPagePCLAutoCR_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,2,2),_BrPagePCLAutoCR_Type())
brPagePCLAutoCR.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLAutoCR.setStatus(_A)
class _BrPagePCLAutoWrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPagePCLAutoWrap_Type.__name__=_B
_BrPagePCLAutoWrap_Object=MibScalar
brPagePCLAutoWrap=_BrPagePCLAutoWrap_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,2,3),_BrPagePCLAutoWrap_Type())
brPagePCLAutoWrap.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLAutoWrap.setStatus(_A)
class _BrPagePCLAutoSkip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPagePCLAutoSkip_Type.__name__=_B
_BrPagePCLAutoSkip_Object=MibScalar
brPagePCLAutoSkip=_BrPagePCLAutoSkip_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,1,2,4),_BrPagePCLAutoSkip_Type())
brPagePCLAutoSkip.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePCLAutoSkip.setStatus(_A)
_Ps_ObjectIdentity=ObjectIdentity
ps=_Ps_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,2))
class _BrPagePSPrintPSError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPagePSPrintPSError_Type.__name__=_B
_BrPagePSPrintPSError_Object=MibScalar
brPagePSPrintPSError=_BrPagePSPrintPSError_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,2,1),_BrPagePSPrintPSError_Type())
brPagePSPrintPSError.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePSPrintPSError.setStatus(_A)
class _BrPagePSKeepPCLFonts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPagePSKeepPCLFonts_Type.__name__=_B
_BrPagePSKeepPCLFonts_Object=MibScalar
brPagePSKeepPCLFonts=_BrPagePSKeepPCLFonts_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,2,2),_BrPagePSKeepPCLFonts_Type())
brPagePSKeepPCLFonts.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePSKeepPCLFonts.setStatus(_A)
class _BrPagePSCAPTsetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPagePSCAPTsetting_Type.__name__=_B
_BrPagePSCAPTsetting_Object=MibScalar
brPagePSCAPTsetting=_BrPagePSCAPTsetting_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,2,3),_BrPagePSCAPTsetting_Type())
brPagePSCAPTsetting.setMaxAccess(_C)
if mibBuilder.loadTexts:brPagePSCAPTsetting.setStatus(_A)
_Gl_ObjectIdentity=ObjectIdentity
gl=_Gl_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3))
_Pen1_ObjectIdentity=ObjectIdentity
pen1=_Pen1_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,1))
class _BrPageGLPen1Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen1Size_Type.__name__=_B
_BrPageGLPen1Size_Object=MibScalar
brPageGLPen1Size=_BrPageGLPen1Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,1,1),_BrPageGLPen1Size_Type())
brPageGLPen1Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen1Size.setStatus(_A)
class _BrPageGLPen1GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen1GrayLevel_Type.__name__=_B
_BrPageGLPen1GrayLevel_Object=MibScalar
brPageGLPen1GrayLevel=_BrPageGLPen1GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,1,2),_BrPageGLPen1GrayLevel_Type())
brPageGLPen1GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen1GrayLevel.setStatus(_A)
_Pen2_ObjectIdentity=ObjectIdentity
pen2=_Pen2_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,2))
class _BrPageGLPen2Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen2Size_Type.__name__=_B
_BrPageGLPen2Size_Object=MibScalar
brPageGLPen2Size=_BrPageGLPen2Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,2,1),_BrPageGLPen2Size_Type())
brPageGLPen2Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen2Size.setStatus(_A)
class _BrPageGLPen2GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen2GrayLevel_Type.__name__=_B
_BrPageGLPen2GrayLevel_Object=MibScalar
brPageGLPen2GrayLevel=_BrPageGLPen2GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,2,2),_BrPageGLPen2GrayLevel_Type())
brPageGLPen2GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen2GrayLevel.setStatus(_A)
_Pen3_ObjectIdentity=ObjectIdentity
pen3=_Pen3_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,3))
class _BrPageGLPen3Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen3Size_Type.__name__=_B
_BrPageGLPen3Size_Object=MibScalar
brPageGLPen3Size=_BrPageGLPen3Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,3,1),_BrPageGLPen3Size_Type())
brPageGLPen3Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen3Size.setStatus(_A)
class _BrPageGLPen3GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen3GrayLevel_Type.__name__=_B
_BrPageGLPen3GrayLevel_Object=MibScalar
brPageGLPen3GrayLevel=_BrPageGLPen3GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,3,2),_BrPageGLPen3GrayLevel_Type())
brPageGLPen3GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen3GrayLevel.setStatus(_A)
_Pen4_ObjectIdentity=ObjectIdentity
pen4=_Pen4_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,4))
class _BrPageGLPen4Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen4Size_Type.__name__=_B
_BrPageGLPen4Size_Object=MibScalar
brPageGLPen4Size=_BrPageGLPen4Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,4,1),_BrPageGLPen4Size_Type())
brPageGLPen4Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen4Size.setStatus(_A)
class _BrPageGLPen4GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen4GrayLevel_Type.__name__=_B
_BrPageGLPen4GrayLevel_Object=MibScalar
brPageGLPen4GrayLevel=_BrPageGLPen4GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,4,2),_BrPageGLPen4GrayLevel_Type())
brPageGLPen4GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen4GrayLevel.setStatus(_A)
_Pen5_ObjectIdentity=ObjectIdentity
pen5=_Pen5_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,5))
class _BrPageGLPen5Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen5Size_Type.__name__=_B
_BrPageGLPen5Size_Object=MibScalar
brPageGLPen5Size=_BrPageGLPen5Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,5,1),_BrPageGLPen5Size_Type())
brPageGLPen5Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen5Size.setStatus(_A)
class _BrPageGLPen5GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen5GrayLevel_Type.__name__=_B
_BrPageGLPen5GrayLevel_Object=MibScalar
brPageGLPen5GrayLevel=_BrPageGLPen5GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,5,2),_BrPageGLPen5GrayLevel_Type())
brPageGLPen5GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen5GrayLevel.setStatus(_A)
_Pen6_ObjectIdentity=ObjectIdentity
pen6=_Pen6_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,6))
class _BrPageGLPen6Size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_BrPageGLPen6Size_Type.__name__=_B
_BrPageGLPen6Size_Object=MibScalar
brPageGLPen6Size=_BrPageGLPen6Size_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,6,1),_BrPageGLPen6Size_Type())
brPageGLPen6Size.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen6Size.setStatus(_A)
class _BrPageGLPen6GrayLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrPageGLPen6GrayLevel_Type.__name__=_B
_BrPageGLPen6GrayLevel_Object=MibScalar
brPageGLPen6GrayLevel=_BrPageGLPen6GrayLevel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,3,6,2),_BrPageGLPen6GrayLevel_Type())
brPageGLPen6GrayLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageGLPen6GrayLevel.setStatus(_A)
_Epson_ObjectIdentity=ObjectIdentity
epson=_Epson_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4))
_Margin_e_ObjectIdentity=ObjectIdentity
margin_e=_Margin_e_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1))
class _BrPageEPSONLeftMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPageEPSONLeftMargin_Type.__name__=_B
_BrPageEPSONLeftMargin_Object=MibScalar
brPageEPSONLeftMargin=_BrPageEPSONLeftMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1,1),_BrPageEPSONLeftMargin_Type())
brPageEPSONLeftMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONLeftMargin.setStatus(_A)
class _BrPageEPSONRightMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPageEPSONRightMargin_Type.__name__=_B
_BrPageEPSONRightMargin_Object=MibScalar
brPageEPSONRightMargin=_BrPageEPSONRightMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1,2),_BrPageEPSONRightMargin_Type())
brPageEPSONRightMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONRightMargin.setStatus(_A)
class _BrPageEPSONTopMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPageEPSONTopMargin_Type.__name__=_B
_BrPageEPSONTopMargin_Object=MibScalar
brPageEPSONTopMargin=_BrPageEPSONTopMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1,3),_BrPageEPSONTopMargin_Type())
brPageEPSONTopMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONTopMargin.setStatus(_A)
class _BrPageEPSONBottomMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPageEPSONBottomMargin_Type.__name__=_B
_BrPageEPSONBottomMargin_Object=MibScalar
brPageEPSONBottomMargin=_BrPageEPSONBottomMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1,4),_BrPageEPSONBottomMargin_Type())
brPageEPSONBottomMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONBottomMargin.setStatus(_A)
class _BrPageEPSONLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,128))
_BrPageEPSONLines_Type.__name__=_B
_BrPageEPSONLines_Object=MibScalar
brPageEPSONLines=_BrPageEPSONLines_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,1,5),_BrPageEPSONLines_Type())
brPageEPSONLines.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONLines.setStatus(_A)
_Auto_e_ObjectIdentity=ObjectIdentity
auto_e=_Auto_e_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,2))
class _BrPageEPSONAutoLF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPageEPSONAutoLF_Type.__name__=_B
_BrPageEPSONAutoLF_Object=MibScalar
brPageEPSONAutoLF=_BrPageEPSONAutoLF_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,2,1),_BrPageEPSONAutoLF_Type())
brPageEPSONAutoLF.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONAutoLF.setStatus(_A)
class _BrPageEPSONAutoMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPageEPSONAutoMask_Type.__name__=_B
_BrPageEPSONAutoMask_Object=MibScalar
brPageEPSONAutoMask=_BrPageEPSONAutoMask_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,4,2,5),_BrPageEPSONAutoMask_Type())
brPageEPSONAutoMask.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageEPSONAutoMask.setStatus(_A)
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5))
_Margin_i_ObjectIdentity=ObjectIdentity
margin_i=_Margin_i_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1))
class _BrPageIBMLeftMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPageIBMLeftMargin_Type.__name__=_B
_BrPageIBMLeftMargin_Object=MibScalar
brPageIBMLeftMargin=_BrPageIBMLeftMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1,1),_BrPageIBMLeftMargin_Type())
brPageIBMLeftMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMLeftMargin.setStatus(_A)
class _BrPageIBMRightMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrPageIBMRightMargin_Type.__name__=_B
_BrPageIBMRightMargin_Object=MibScalar
brPageIBMRightMargin=_BrPageIBMRightMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1,2),_BrPageIBMRightMargin_Type())
brPageIBMRightMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMRightMargin.setStatus(_A)
class _BrPageIBMTopMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPageIBMTopMargin_Type.__name__=_B
_BrPageIBMTopMargin_Object=MibScalar
brPageIBMTopMargin=_BrPageIBMTopMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1,3),_BrPageIBMTopMargin_Type())
brPageIBMTopMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMTopMargin.setStatus(_A)
class _BrPageIBMBottomMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_BrPageIBMBottomMargin_Type.__name__=_B
_BrPageIBMBottomMargin_Object=MibScalar
brPageIBMBottomMargin=_BrPageIBMBottomMargin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1,4),_BrPageIBMBottomMargin_Type())
brPageIBMBottomMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMBottomMargin.setStatus(_A)
class _BrPageIBMLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,128))
_BrPageIBMLines_Type.__name__=_B
_BrPageIBMLines_Object=MibScalar
brPageIBMLines=_BrPageIBMLines_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,1,5),_BrPageIBMLines_Type())
brPageIBMLines.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMLines.setStatus(_A)
_Auto_i_ObjectIdentity=ObjectIdentity
auto_i=_Auto_i_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,2))
class _BrPageIBMAutoLF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPageIBMAutoLF_Type.__name__=_B
_BrPageIBMAutoLF_Object=MibScalar
brPageIBMAutoLF=_BrPageIBMAutoLF_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,2,1),_BrPageIBMAutoLF_Type())
brPageIBMAutoLF.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMAutoLF.setStatus(_A)
class _BrPageIBMAutoCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPageIBMAutoCR_Type.__name__=_B
_BrPageIBMAutoCR_Object=MibScalar
brPageIBMAutoCR=_BrPageIBMAutoCR_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,2,2),_BrPageIBMAutoCR_Type())
brPageIBMAutoCR.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMAutoCR.setStatus(_A)
class _BrPageIBMAutoMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrPageIBMAutoMask_Type.__name__=_B
_BrPageIBMAutoMask_Object=MibScalar
brPageIBMAutoMask=_BrPageIBMAutoMask_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,2,5,2,5),_BrPageIBMAutoMask_Type())
brPageIBMAutoMask.setMaxAccess(_C)
if mibBuilder.loadTexts:brPageIBMAutoMask.setStatus(_A)
_Fontsetup_ObjectIdentity=ObjectIdentity
fontsetup=_Fontsetup_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,3))
class _BrFontName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_BrFontName_Type.__name__=_B
_BrFontName_Object=MibScalar
brFontName=_BrFontName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,3,1),_BrFontName_Type())
brFontName.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontName.setStatus(_A)
class _BrFontPointSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,99999))
_BrFontPointSize_Type.__name__=_B
_BrFontPointSize_Object=MibScalar
brFontPointSize=_BrFontPointSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,3,2),_BrFontPointSize_Type())
brFontPointSize.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontPointSize.setStatus(_A)
class _BrFontPitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_BrFontPitch_Type.__name__=_B
_BrFontPitch_Object=MibScalar
brFontPitch=_BrFontPitch_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,3,3),_BrFontPitch_Type())
brFontPitch.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontPitch.setStatus(_A)
class _BrFontSymbolSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_BrFontSymbolSet_Type.__name__=_B
_BrFontSymbolSet_Object=MibScalar
brFontSymbolSet=_BrFontSymbolSet_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,3,4),_BrFontSymbolSet_Type())
brFontSymbolSet.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontSymbolSet.setStatus(_A)
_Controlpanel_ObjectIdentity=ObjectIdentity
controlpanel=_Controlpanel_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4))
_Reset_ObjectIdentity=ObjectIdentity
reset=_Reset_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,1))
class _BrPanelResetUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelResetUser_Type.__name__=_B
_BrPanelResetUser_Object=MibScalar
brPanelResetUser=_BrPanelResetUser_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,1,1),_BrPanelResetUser_Type())
brPanelResetUser.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelResetUser.setStatus(_A)
class _BrPanelResetFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelResetFactory_Type.__name__=_B
_BrPanelResetFactory_Object=MibScalar
brPanelResetFactory=_BrPanelResetFactory_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,1,2),_BrPanelResetFactory_Type())
brPanelResetFactory.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelResetFactory.setStatus(_A)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,2))
class _BrPanelTestConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelTestConfiguration_Type.__name__=_B
_BrPanelTestConfiguration_Object=MibScalar
brPanelTestConfiguration=_BrPanelTestConfiguration_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,2,1),_BrPanelTestConfiguration_Type())
brPanelTestConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelTestConfiguration.setStatus(_A)
class _BrPanelTestFontList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelTestFontList_Type.__name__=_B
_BrPanelTestFontList_Object=MibScalar
brPanelTestFontList=_BrPanelTestFontList_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,2,2),_BrPanelTestFontList_Type())
brPanelTestFontList.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelTestFontList.setStatus(_A)
class _BrPanelTestTestPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelTestTestPage_Type.__name__=_B
_BrPanelTestTestPage_Object=MibScalar
brPanelTestTestPage=_BrPanelTestTestPage_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,2,3),_BrPanelTestTestPage_Type())
brPanelTestTestPage.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelTestTestPage.setStatus(_A)
class _BrPanelTestDemoPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelTestDemoPage_Type.__name__=_B
_BrPanelTestDemoPage_Object=MibScalar
brPanelTestDemoPage=_BrPanelTestDemoPage_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,2,4),_BrPanelTestDemoPage_Type())
brPanelTestDemoPage.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelTestDemoPage.setStatus(_A)
_Panellock_ObjectIdentity=ObjectIdentity
panellock=_Panellock_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,3))
class _BrPanelLockPasswd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BrPanelLockPasswd_Type.__name__=_B
_BrPanelLockPasswd_Object=MibScalar
brPanelLockPasswd=_BrPanelLockPasswd_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,3,1),_BrPanelLockPasswd_Type())
brPanelLockPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelLockPasswd.setStatus(_A)
class _BrPanelLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrPanelLock_Type.__name__=_B
_BrPanelLock_Object=MibScalar
brPanelLock=_BrPanelLock_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,3,2),_BrPanelLock_Type())
brPanelLock.setMaxAccess(_D)
if mibBuilder.loadTexts:brPanelLock.setStatus(_A)
_BrPanelLockOn_Type=OctetString
_BrPanelLockOn_Object=MibScalar
brPanelLockOn=_BrPanelLockOn_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,3,3),_BrPanelLockOn_Type())
brPanelLockOn.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelLockOn.setStatus(_A)
_BrPanelLockOff_Type=OctetString
_BrPanelLockOff_Object=MibScalar
brPanelLockOff=_BrPanelLockOff_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,3,4),_BrPanelLockOff_Type())
brPanelLockOff.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelLockOff.setStatus(_A)
_Key_ObjectIdentity=ObjectIdentity
key=_Key_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4))
class _BrPanelKeyOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyOnline_Type.__name__=_B
_BrPanelKeyOnline_Object=MibScalar
brPanelKeyOnline=_BrPanelKeyOnline_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,1),_BrPanelKeyOnline_Type())
brPanelKeyOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyOnline.setStatus(_A)
class _BrPanelKeyFormFeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyFormFeed_Type.__name__=_B
_BrPanelKeyFormFeed_Object=MibScalar
brPanelKeyFormFeed=_BrPanelKeyFormFeed_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,2),_BrPanelKeyFormFeed_Type())
brPanelKeyFormFeed.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyFormFeed.setStatus(_A)
class _BrPanelKeyContinue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyContinue_Type.__name__=_B
_BrPanelKeyContinue_Object=MibScalar
brPanelKeyContinue=_BrPanelKeyContinue_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,3),_BrPanelKeyContinue_Type())
brPanelKeyContinue.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyContinue.setStatus(_A)
class _BrPanelKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyMode_Type.__name__=_B
_BrPanelKeyMode_Object=MibScalar
brPanelKeyMode=_BrPanelKeyMode_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,4),_BrPanelKeyMode_Type())
brPanelKeyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyMode.setStatus(_A)
class _BrPanelKeyGo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyGo_Type.__name__=_B
_BrPanelKeyGo_Object=MibScalar
brPanelKeyGo=_BrPanelKeyGo_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,5),_BrPanelKeyGo_Type())
brPanelKeyGo.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyGo.setStatus(_A)
class _BrPanelKeyJobCancel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyJobCancel_Type.__name__=_B
_BrPanelKeyJobCancel_Object=MibScalar
brPanelKeyJobCancel=_BrPanelKeyJobCancel_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,6),_BrPanelKeyJobCancel_Type())
brPanelKeyJobCancel.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyJobCancel.setStatus(_A)
class _BrPanelKeyReprint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeyReprint_Type.__name__=_B
_BrPanelKeyReprint_Object=MibScalar
brPanelKeyReprint=_BrPanelKeyReprint_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,7),_BrPanelKeyReprint_Type())
brPanelKeyReprint.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeyReprint.setStatus(_A)
class _BrPanelKeySecure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPanelKeySecure_Type.__name__=_B
_BrPanelKeySecure_Object=MibScalar
brPanelKeySecure=_BrPanelKeySecure_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,4,8),_BrPanelKeySecure_Type())
brPanelKeySecure.setMaxAccess(_C)
if mibBuilder.loadTexts:brPanelKeySecure.setStatus(_A)
_Panelinfo_ObjectIdentity=ObjectIdentity
panelinfo=_Panelinfo_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5))
class _BrLCDMode1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A7,1),(_A8,2),(_A9,3),(_AB,4)))
_BrLCDMode1_Type.__name__=_B
_BrLCDMode1_Object=MibScalar
brLCDMode1=_BrLCDMode1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,1),_BrLCDMode1_Type())
brLCDMode1.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDMode1.setStatus(_A)
_BrLCDString1_Type=OctetString
_BrLCDString1_Object=MibScalar
brLCDString1=_BrLCDString1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,2),_BrLCDString1_Type())
brLCDString1.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString1.setStatus(_A)
class _BrLCDMode2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A7,1),(_A8,2),(_A9,3)))
_BrLCDMode2_Type.__name__=_B
_BrLCDMode2_Object=MibScalar
brLCDMode2=_BrLCDMode2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,3),_BrLCDMode2_Type())
brLCDMode2.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDMode2.setStatus(_A)
_BrLCDString2_Type=OctetString
_BrLCDString2_Object=MibScalar
brLCDString2=_BrLCDString2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,4),_BrLCDString2_Type())
brLCDString2.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString2.setStatus(_A)
_BrLCDString16fix_Type=DisplayString
_BrLCDString16fix_Object=MibScalar
brLCDString16fix=_BrLCDString16fix_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,5),_BrLCDString16fix_Type())
brLCDString16fix.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString16fix.setStatus(_A)
class _BrBackLightColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('green',1),('orange',2),('red',3),('notsupport',255)))
_BrBackLightColor_Type.__name__=_B
_BrBackLightColor_Object=MibScalar
brBackLightColor=_BrBackLightColor_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,6),_BrBackLightColor_Type())
brBackLightColor.setMaxAccess(_D)
if mibBuilder.loadTexts:brBackLightColor.setStatus(_A)
class _BrLCDMode3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A7,1),(_A8,2),(_A9,3),(_AB,4)))
_BrLCDMode3_Type.__name__=_B
_BrLCDMode3_Object=MibScalar
brLCDMode3=_BrLCDMode3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,7),_BrLCDMode3_Type())
brLCDMode3.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDMode3.setStatus(_A)
_BrLCDString3_Type=OctetString
_BrLCDString3_Object=MibScalar
brLCDString3=_BrLCDString3_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,8),_BrLCDString3_Type())
brLCDString3.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString3.setStatus(_A)
class _BrLCDMode4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A7,1),(_A8,2),(_A9,3),(_AB,4)))
_BrLCDMode4_Type.__name__=_B
_BrLCDMode4_Object=MibScalar
brLCDMode4=_BrLCDMode4_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,9),_BrLCDMode4_Type())
brLCDMode4.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDMode4.setStatus(_A)
_BrLCDString4_Type=OctetString
_BrLCDString4_Object=MibScalar
brLCDString4=_BrLCDString4_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,10),_BrLCDString4_Type())
brLCDString4.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString4.setStatus(_A)
class _BrLCDMode5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A7,1),(_A8,2),(_A9,3),(_AB,4)))
_BrLCDMode5_Type.__name__=_B
_BrLCDMode5_Object=MibScalar
brLCDMode5=_BrLCDMode5_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,11),_BrLCDMode5_Type())
brLCDMode5.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDMode5.setStatus(_A)
_BrLCDString5_Type=OctetString
_BrLCDString5_Object=MibScalar
brLCDString5=_BrLCDString5_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,12),_BrLCDString5_Type())
brLCDString5.setMaxAccess(_D)
if mibBuilder.loadTexts:brLCDString5.setStatus(_A)
_BrLCDContrast_Type=Integer32
_BrLCDContrast_Object=MibScalar
brLCDContrast=_BrLCDContrast_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,4,5,13),_BrLCDContrast_Type())
brLCDContrast.setMaxAccess(_C)
if mibBuilder.loadTexts:brLCDContrast.setStatus(_A)
_Printerinfomation_ObjectIdentity=ObjectIdentity
printerinfomation=_Printerinfomation_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5))
_BrInfoSerialNumber_Type=OctetString
_BrInfoSerialNumber_Object=MibScalar
brInfoSerialNumber=_BrInfoSerialNumber_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,1),_BrInfoSerialNumber_Type())
brInfoSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoSerialNumber.setStatus(_A)
class _BrInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrInfoType_Type.__name__=_B
_BrInfoType_Object=MibScalar
brInfoType=_BrInfoType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,2),_BrInfoType_Type())
brInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoType.setStatus(_A)
_Version_ObjectIdentity=ObjectIdentity
version=_Version_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,3))
class _BrInfoUpperMIBVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrInfoUpperMIBVer_Type.__name__=_B
_BrInfoUpperMIBVer_Object=MibScalar
brInfoUpperMIBVer=_BrInfoUpperMIBVer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,3,1),_BrInfoUpperMIBVer_Type())
brInfoUpperMIBVer.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoUpperMIBVer.setStatus(_A)
class _BrInfoLowerMIBVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrInfoLowerMIBVer_Type.__name__=_B
_BrInfoLowerMIBVer_Object=MibScalar
brInfoLowerMIBVer=_BrInfoLowerMIBVer_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,3,2),_BrInfoLowerMIBVer_Type())
brInfoLowerMIBVer.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoLowerMIBVer.setStatus(_A)
class _BrInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrInfoStatus_Type.__name__=_B
_BrInfoStatus_Object=MibScalar
brInfoStatus=_BrInfoStatus_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,4),_BrInfoStatus_Type())
brInfoStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoStatus.setStatus(_A)
class _BrInfoNetVerUpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrInfoNetVerUpStatus_Type.__name__=_B
_BrInfoNetVerUpStatus_Object=MibScalar
brInfoNetVerUpStatus=_BrInfoNetVerUpStatus_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,5),_BrInfoNetVerUpStatus_Type())
brInfoNetVerUpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoNetVerUpStatus.setStatus(_A)
_BrInfoPrinterUStatus_Type=Integer32
_BrInfoPrinterUStatus_Object=MibScalar
brInfoPrinterUStatus=_BrInfoPrinterUStatus_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,6),_BrInfoPrinterUStatus_Type())
brInfoPrinterUStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoPrinterUStatus.setStatus(_A)
_BrInfoPConSupported_Type=Integer32
_BrInfoPConSupported_Object=MibScalar
brInfoPConSupported=_BrInfoPConSupported_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,7),_BrInfoPConSupported_Type())
brInfoPConSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoPConSupported.setStatus(_A)
_BrInfoMaintenance_Type=OctetString
_BrInfoMaintenance_Object=MibScalar
brInfoMaintenance=_BrInfoMaintenance_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,8),_BrInfoMaintenance_Type())
brInfoMaintenance.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoMaintenance.setStatus(_A)
class _BrInfoModelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6,8,9,11,13,14,15,16,17,18,19,20,21,22,23,24,25,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148)));namedValues=NamedValues(*(('hl2400ce',4),('hl3400CN',5),('hl3260',6),('hl2460',8),('hl2600cn',9),('hl3450cn',11),('am',13),('zlhe',14),('zl2',15),('jigen',16),('aml',17),('l4c',18),('all',19),('alLedModel',20),('alLcdModel',21),('hl4040',22),('allchn',23),('hl4050hl4070',24),('all2',25),('zlfb',101),('zl',102),('bh',103),('bhfb',104),('zlhs',105),('bhhs',106),('zl2fb',107),('bhl2mfc',108),('bhl2fb',109),('zl2mfc',110),('mini2',111),('mini2adf',112),('bh3fb',113),('bh3mfc',114),('allmfc',115),('allfb',116),('slow4c',117),('mini2eColorLCD',118),('mini2eColorLCDADF',119),('alfb',120),('dcp540',121),('dcp750',122),('mfc440',123),('mfc665',124),('mfc850',125),('mfc860',126),('mfc5460',127),('mfc5860',128),('dcp6150',129),('dcp6260',130),('dcp6460',131),('dcp6860',132),('dcp770',133),('mfc480',134),('acfbCIS',135),('acfbCCD',136),('mfc7440',137),('mfc7840',138),('mfc5490',139),('mfc5890',140),('mfc6490',141),('dcp6690',142),('mfc6890',143),('dcp585',144),('mfc490',145),('mfc790',146),('mfc990',147),('mfc930',148)))
_BrInfoModelNumber_Type.__name__=_B
_BrInfoModelNumber_Object=MibScalar
brInfoModelNumber=_BrInfoModelNumber_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,9),_BrInfoModelNumber_Type())
brInfoModelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoModelNumber.setStatus(_A)
_BrInfoCounter_Type=OctetString
_BrInfoCounter_Object=MibScalar
brInfoCounter=_BrInfoCounter_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,10),_BrInfoCounter_Type())
brInfoCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoCounter.setStatus(_A)
_BrInfoNextCare_Type=OctetString
_BrInfoNextCare_Object=MibScalar
brInfoNextCare=_BrInfoNextCare_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,11),_BrInfoNextCare_Type())
brInfoNextCare.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoNextCare.setStatus(_A)
class _BrInfoHDDSlot1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_BrInfoHDDSlot1_Type.__name__=_B
_BrInfoHDDSlot1_Object=MibScalar
brInfoHDDSlot1=_BrInfoHDDSlot1_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,12),_BrInfoHDDSlot1_Type())
brInfoHDDSlot1.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoHDDSlot1.setStatus(_A)
class _BrInfoHDDSlot2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_BrInfoHDDSlot2_Type.__name__=_B
_BrInfoHDDSlot2_Object=MibScalar
brInfoHDDSlot2=_BrInfoHDDSlot2_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,13),_BrInfoHDDSlot2_Type())
brInfoHDDSlot2.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoHDDSlot2.setStatus(_A)
class _BrInfoHDDInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_BrInfoHDDInternal_Type.__name__=_B
_BrInfoHDDInternal_Object=MibScalar
brInfoHDDInternal=_BrInfoHDDInternal_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,14),_BrInfoHDDInternal_Type())
brInfoHDDInternal.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoHDDInternal.setStatus(_A)
_BrInfoHDDSize_Type=OctetString
_BrInfoHDDSize_Object=MibScalar
brInfoHDDSize=_BrInfoHDDSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,15),_BrInfoHDDSize_Type())
brInfoHDDSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoHDDSize.setStatus(_A)
_BrInfoSolutionsCenterURL_Type=DisplayString
_BrInfoSolutionsCenterURL_Object=MibScalar
brInfoSolutionsCenterURL=_BrInfoSolutionsCenterURL_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,16),_BrInfoSolutionsCenterURL_Type())
brInfoSolutionsCenterURL.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoSolutionsCenterURL.setStatus(_A)
_BrInfoDeviceRomVersion_Type=DisplayString
_BrInfoDeviceRomVersion_Object=MibScalar
brInfoDeviceRomVersion=_BrInfoDeviceRomVersion_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,17),_BrInfoDeviceRomVersion_Type())
brInfoDeviceRomVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoDeviceRomVersion.setStatus(_A)
_BrInfoCoverage_Type=OctetString
_BrInfoCoverage_Object=MibScalar
brInfoCoverage=_BrInfoCoverage_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,18),_BrInfoCoverage_Type())
brInfoCoverage.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoCoverage.setStatus(_A)
_BrInfoEstimatedPagesRemaining_Type=Counter32
_BrInfoEstimatedPagesRemaining_Object=MibScalar
brInfoEstimatedPagesRemaining=_BrInfoEstimatedPagesRemaining_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,19),_BrInfoEstimatedPagesRemaining_Type())
brInfoEstimatedPagesRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoEstimatedPagesRemaining.setStatus(_A)
_BrInfoReplaceCount_Type=OctetString
_BrInfoReplaceCount_Object=MibScalar
brInfoReplaceCount=_BrInfoReplaceCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,20),_BrInfoReplaceCount_Type())
brInfoReplaceCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoReplaceCount.setStatus(_A)
_BrInfoJamCount_Type=OctetString
_BrInfoJamCount_Object=MibScalar
brInfoJamCount=_BrInfoJamCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,21),_BrInfoJamCount_Type())
brInfoJamCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoJamCount.setStatus(_A)
_BrInfoJamCountClear_Type=Integer32
_BrInfoJamCountClear_Object=MibScalar
brInfoJamCountClear=_BrInfoJamCountClear_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,22),_BrInfoJamCountClear_Type())
brInfoJamCountClear.setMaxAccess(_C)
if mibBuilder.loadTexts:brInfoJamCountClear.setStatus(_A)
_BrInfoReplaceTime_Type=OctetString
_BrInfoReplaceTime_Object=MibScalar
brInfoReplaceTime=_BrInfoReplaceTime_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,23),_BrInfoReplaceTime_Type())
brInfoReplaceTime.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoReplaceTime.setStatus(_A)
_BrInfoDeviceSubRomVersion_Type=OctetString
_BrInfoDeviceSubRomVersion_Object=MibScalar
brInfoDeviceSubRomVersion=_BrInfoDeviceSubRomVersion_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,24),_BrInfoDeviceSubRomVersion_Type())
brInfoDeviceSubRomVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoDeviceSubRomVersion.setStatus(_A)
_BrInfoAlertVersion_Type=Integer32
_BrInfoAlertVersion_Object=MibScalar
brInfoAlertVersion=_BrInfoAlertVersion_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,25),_BrInfoAlertVersion_Type())
brInfoAlertVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoAlertVersion.setStatus(_A)
class _BrInfoBlackPrint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrInfoBlackPrint_Type.__name__=_B
_BrInfoBlackPrint_Object=MibScalar
brInfoBlackPrint=_BrInfoBlackPrint_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,26),_BrInfoBlackPrint_Type())
brInfoBlackPrint.setMaxAccess(_D)
if mibBuilder.loadTexts:brInfoBlackPrint.setStatus(_A)
_ErrorHistory_ObjectIdentity=ObjectIdentity
errorHistory=_ErrorHistory_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51))
_BrErrorHistoryCount_Type=Integer32
_BrErrorHistoryCount_Object=MibScalar
brErrorHistoryCount=_BrErrorHistoryCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,1),_BrErrorHistoryCount_Type())
brErrorHistoryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brErrorHistoryCount.setStatus(_A)
_BrErrorHistoryTable_Object=MibTable
brErrorHistoryTable=_BrErrorHistoryTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,2))
if mibBuilder.loadTexts:brErrorHistoryTable.setStatus(_A)
_BrErrorHistoryEntry_Object=MibTableRow
brErrorHistoryEntry=_BrErrorHistoryEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,2,1))
brErrorHistoryEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:brErrorHistoryEntry.setStatus(_A)
class _BrErrorHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrErrorHistoryIndex_Type.__name__=_B
_BrErrorHistoryIndex_Object=MibTableColumn
brErrorHistoryIndex=_BrErrorHistoryIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,2,1,1),_BrErrorHistoryIndex_Type())
brErrorHistoryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brErrorHistoryIndex.setStatus(_A)
_BrErrorHistoryDescription_Type=OctetString
_BrErrorHistoryDescription_Object=MibTableColumn
brErrorHistoryDescription=_BrErrorHistoryDescription_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,2,1,2),_BrErrorHistoryDescription_Type())
brErrorHistoryDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brErrorHistoryDescription.setStatus(_A)
_BrErrorHistoryAllClear_Type=Integer32
_BrErrorHistoryAllClear_Object=MibScalar
brErrorHistoryAllClear=_BrErrorHistoryAllClear_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,3),_BrErrorHistoryAllClear_Type())
brErrorHistoryAllClear.setMaxAccess(_C)
if mibBuilder.loadTexts:brErrorHistoryAllClear.setStatus(_A)
_BrCommunicationErrorHistoryCount_Type=Integer32
_BrCommunicationErrorHistoryCount_Object=MibScalar
brCommunicationErrorHistoryCount=_BrCommunicationErrorHistoryCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,11),_BrCommunicationErrorHistoryCount_Type())
brCommunicationErrorHistoryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brCommunicationErrorHistoryCount.setStatus(_A)
_BrCommunicationErrorHistoryTable_Object=MibTable
brCommunicationErrorHistoryTable=_BrCommunicationErrorHistoryTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,12))
if mibBuilder.loadTexts:brCommunicationErrorHistoryTable.setStatus(_A)
_BrCommunicationErrorHistoryEntry_Object=MibTableRow
brCommunicationErrorHistoryEntry=_BrCommunicationErrorHistoryEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,12,1))
brCommunicationErrorHistoryEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:brCommunicationErrorHistoryEntry.setStatus(_A)
class _BrCommunicationErrorHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCommunicationErrorHistoryIndex_Type.__name__=_B
_BrCommunicationErrorHistoryIndex_Object=MibTableColumn
brCommunicationErrorHistoryIndex=_BrCommunicationErrorHistoryIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,12,1,1),_BrCommunicationErrorHistoryIndex_Type())
brCommunicationErrorHistoryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCommunicationErrorHistoryIndex.setStatus(_A)
_BrCommunicationErrorHistoryDescription_Type=OctetString
_BrCommunicationErrorHistoryDescription_Object=MibTableColumn
brCommunicationErrorHistoryDescription=_BrCommunicationErrorHistoryDescription_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,51,12,1,2),_BrCommunicationErrorHistoryDescription_Type())
brCommunicationErrorHistoryDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brCommunicationErrorHistoryDescription.setStatus(_A)
_PrintPages_ObjectIdentity=ObjectIdentity
printPages=_PrintPages_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52))
_BrPrintPagesTable_Object=MibTable
brPrintPagesTable=_BrPrintPagesTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,1))
if mibBuilder.loadTexts:brPrintPagesTable.setStatus(_A)
_BrPrintPagesEntry_Object=MibTableRow
brPrintPagesEntry=_BrPrintPagesEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,1,1))
brPrintPagesEntry.setIndexNames((0,_E,_Ac))
if mibBuilder.loadTexts:brPrintPagesEntry.setStatus(_A)
class _BrPrintPagesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPrintPagesIndex_Type.__name__=_B
_BrPrintPagesIndex_Object=MibTableColumn
brPrintPagesIndex=_BrPrintPagesIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,1,1,1),_BrPrintPagesIndex_Type())
brPrintPagesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesIndex.setStatus(_A)
class _BrPrintPagesPaperSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,24,25,26,27,45,46,80,81,90,91,99,100,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,920,921,922,924,999)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,45),(_S,46),(_T,80),(_U,81),(_V,90),(_W,91),(_X,99),(_Y,100),(_Z,890),(_a,891),(_b,892),(_c,893),(_d,894),(_e,895),(_f,896),(_g,897),(_h,898),(_i,899),(_I,900),(_j,901),(_k,902),(_l,903),(_m,904),(_n,905),(_o,906),(_p,907),(_q,908),('legalA4Long',909),('b6A5A6',910),(_r,911),(_s,920),(_t,921),(_u,922),('b6JIS',924),('otherPage',999)))
_BrPrintPagesPaperSize_Type.__name__=_B
_BrPrintPagesPaperSize_Object=MibTableColumn
brPrintPagesPaperSize=_BrPrintPagesPaperSize_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,1,1,2),_BrPrintPagesPaperSize_Type())
brPrintPagesPaperSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesPaperSize.setStatus(_A)
_BrPrintPages_Type=Counter32
_BrPrintPages_Object=MibTableColumn
brPrintPages=_BrPrintPages_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,1,1,3),_BrPrintPages_Type())
brPrintPages.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPages.setStatus(_A)
_BrPrintPagesMediaPlaceTable_Object=MibTable
brPrintPagesMediaPlaceTable=_BrPrintPagesMediaPlaceTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,11))
if mibBuilder.loadTexts:brPrintPagesMediaPlaceTable.setStatus(_A)
_BrPrintPagesMediaPlaceEntry_Object=MibTableRow
brPrintPagesMediaPlaceEntry=_BrPrintPagesMediaPlaceEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,11,1))
brPrintPagesMediaPlaceEntry.setIndexNames((0,_E,_Ad))
if mibBuilder.loadTexts:brPrintPagesMediaPlaceEntry.setStatus(_A)
class _BrPrintPagesMediaPlaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPrintPagesMediaPlaceIndex_Type.__name__=_B
_BrPrintPagesMediaPlaceIndex_Object=MibTableColumn
brPrintPagesMediaPlaceIndex=_BrPrintPagesMediaPlaceIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,11,1,1),_BrPrintPagesMediaPlaceIndex_Type())
brPrintPagesMediaPlaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesMediaPlaceIndex.setStatus(_A)
class _BrPrintPagesMediaPlaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('face',1),('back',2)))
_BrPrintPagesMediaPlaceType_Type.__name__=_B
_BrPrintPagesMediaPlaceType_Object=MibTableColumn
brPrintPagesMediaPlaceType=_BrPrintPagesMediaPlaceType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,11,1,2),_BrPrintPagesMediaPlaceType_Type())
brPrintPagesMediaPlaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesMediaPlaceType.setStatus(_A)
_BrPrintPagesMediaPlaceCounter_Type=Counter32
_BrPrintPagesMediaPlaceCounter_Object=MibTableColumn
brPrintPagesMediaPlaceCounter=_BrPrintPagesMediaPlaceCounter_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,11,1,3),_BrPrintPagesMediaPlaceCounter_Type())
brPrintPagesMediaPlaceCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesMediaPlaceCounter.setStatus(_A)
_BrPrintPagesFuncTable_Object=MibTable
brPrintPagesFuncTable=_BrPrintPagesFuncTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,21))
if mibBuilder.loadTexts:brPrintPagesFuncTable.setStatus(_A)
_BrPrintPagesFuncEntry_Object=MibTableRow
brPrintPagesFuncEntry=_BrPrintPagesFuncEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,21,1))
brPrintPagesFuncEntry.setIndexNames((0,_E,_Ae))
if mibBuilder.loadTexts:brPrintPagesFuncEntry.setStatus(_A)
class _BrPrintPagesFuncIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPrintPagesFuncIndex_Type.__name__=_B
_BrPrintPagesFuncIndex_Object=MibTableColumn
brPrintPagesFuncIndex=_BrPrintPagesFuncIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,21,1,1),_BrPrintPagesFuncIndex_Type())
brPrintPagesFuncIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesFuncIndex.setStatus(_A)
class _BrPrintPagesFuncType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('pcPrinttotal',1),('faxtotal',2),('copytotal',3),(_AH,4),('pcPrintcolor',5),('faxcolor',6),('pcPrintmono',7),('faxmono',8),('copymono',9)))
_BrPrintPagesFuncType_Type.__name__=_B
_BrPrintPagesFuncType_Object=MibTableColumn
brPrintPagesFuncType=_BrPrintPagesFuncType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,21,1,2),_BrPrintPagesFuncType_Type())
brPrintPagesFuncType.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesFuncType.setStatus(_A)
_BrPrintPagesFuncCounter_Type=Counter32
_BrPrintPagesFuncCounter_Object=MibTableColumn
brPrintPagesFuncCounter=_BrPrintPagesFuncCounter_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,21,1,3),_BrPrintPagesFuncCounter_Type())
brPrintPagesFuncCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesFuncCounter.setStatus(_A)
_BrPrintPagesPaperTypeTable_Object=MibTable
brPrintPagesPaperTypeTable=_BrPrintPagesPaperTypeTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,31))
if mibBuilder.loadTexts:brPrintPagesPaperTypeTable.setStatus(_A)
_BrPrintPagesPaperTypeEntry_Object=MibTableRow
brPrintPagesPaperTypeEntry=_BrPrintPagesPaperTypeEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,31,1))
brPrintPagesPaperTypeEntry.setIndexNames((0,_E,_Af))
if mibBuilder.loadTexts:brPrintPagesPaperTypeEntry.setStatus(_A)
class _BrPrintPagesPaperTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_BrPrintPagesPaperTypeIndex_Type.__name__=_B
_BrPrintPagesPaperTypeIndex_Object=MibTableColumn
brPrintPagesPaperTypeIndex=_BrPrintPagesPaperTypeIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,31,1,1),_BrPrintPagesPaperTypeIndex_Type())
brPrintPagesPaperTypeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesPaperTypeIndex.setStatus(_A)
class _BrPrintPagesPaperTypeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,12,13,14)));namedValues=NamedValues(*((_x,3),('regularthinrecycled',12),('thickthickerbond',13),('envelopesenvthickenvthin',14)))
_BrPrintPagesPaperTypeType_Type.__name__=_B
_BrPrintPagesPaperTypeType_Object=MibTableColumn
brPrintPagesPaperTypeType=_BrPrintPagesPaperTypeType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,31,1,2),_BrPrintPagesPaperTypeType_Type())
brPrintPagesPaperTypeType.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesPaperTypeType.setStatus(_A)
_BrPrintPagesPaperTypeCounter_Type=Counter32
_BrPrintPagesPaperTypeCounter_Object=MibTableColumn
brPrintPagesPaperTypeCounter=_BrPrintPagesPaperTypeCounter_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,52,31,1,3),_BrPrintPagesPaperTypeCounter_Type())
brPrintPagesPaperTypeCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:brPrintPagesPaperTypeCounter.setStatus(_A)
_Capability_ObjectIdentity=ObjectIdentity
capability=_Capability_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53))
_Copies_ObjectIdentity=ObjectIdentity
copies=_Copies_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,1))
_BrCapabilityCopiesMax_Type=Integer32
_BrCapabilityCopiesMax_Object=MibScalar
brCapabilityCopiesMax=_BrCapabilityCopiesMax_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,1,1),_BrCapabilityCopiesMax_Type())
brCapabilityCopiesMax.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityCopiesMax.setStatus(_A)
_BrCapabilityCopiesMin_Type=Integer32
_BrCapabilityCopiesMin_Object=MibScalar
brCapabilityCopiesMin=_BrCapabilityCopiesMin_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,1,2),_BrCapabilityCopiesMin_Type())
brCapabilityCopiesMin.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityCopiesMin.setStatus(_A)
_Orientation_ObjectIdentity=ObjectIdentity
orientation=_Orientation_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2))
_BrCapabilityOrientationCount_Type=Integer32
_BrCapabilityOrientationCount_Object=MibScalar
brCapabilityOrientationCount=_BrCapabilityOrientationCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2,1),_BrCapabilityOrientationCount_Type())
brCapabilityOrientationCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityOrientationCount.setStatus(_A)
_BrCapabilityOrientationTable_Object=MibTable
brCapabilityOrientationTable=_BrCapabilityOrientationTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2,2))
if mibBuilder.loadTexts:brCapabilityOrientationTable.setStatus(_A)
_BrCapabilityOrientationEntry_Object=MibTableRow
brCapabilityOrientationEntry=_BrCapabilityOrientationEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2,2,1))
brCapabilityOrientationEntry.setIndexNames((0,_E,_Ag))
if mibBuilder.loadTexts:brCapabilityOrientationEntry.setStatus(_A)
class _BrCapabilityOrientationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCapabilityOrientationIndex_Type.__name__=_B
_BrCapabilityOrientationIndex_Object=MibTableColumn
brCapabilityOrientationIndex=_BrCapabilityOrientationIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2,2,1,1),_BrCapabilityOrientationIndex_Type())
brCapabilityOrientationIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityOrientationIndex.setStatus(_A)
_BrCapabilityOrientationName_Type=DisplayString
_BrCapabilityOrientationName_Object=MibTableColumn
brCapabilityOrientationName=_BrCapabilityOrientationName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,2,2,1,2),_BrCapabilityOrientationName_Type())
brCapabilityOrientationName.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityOrientationName.setStatus(_A)
_Paper_ObjectIdentity=ObjectIdentity
paper=_Paper_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3))
_BrCapabilityPaperCount_Type=Integer32
_BrCapabilityPaperCount_Object=MibScalar
brCapabilityPaperCount=_BrCapabilityPaperCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3,1),_BrCapabilityPaperCount_Type())
brCapabilityPaperCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityPaperCount.setStatus(_A)
_BrCapabilityPaperTable_Object=MibTable
brCapabilityPaperTable=_BrCapabilityPaperTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3,2))
if mibBuilder.loadTexts:brCapabilityPaperTable.setStatus(_A)
_BrCapabilityPaperEntry_Object=MibTableRow
brCapabilityPaperEntry=_BrCapabilityPaperEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3,2,1))
brCapabilityPaperEntry.setIndexNames((0,_E,_Ah))
if mibBuilder.loadTexts:brCapabilityPaperEntry.setStatus(_A)
class _BrCapabilityPaperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCapabilityPaperIndex_Type.__name__=_B
_BrCapabilityPaperIndex_Object=MibTableColumn
brCapabilityPaperIndex=_BrCapabilityPaperIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3,2,1,1),_BrCapabilityPaperIndex_Type())
brCapabilityPaperIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityPaperIndex.setStatus(_A)
_BrCapabilityPaperName_Type=DisplayString
_BrCapabilityPaperName_Object=MibTableColumn
brCapabilityPaperName=_BrCapabilityPaperName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,3,2,1,2),_BrCapabilityPaperName_Type())
brCapabilityPaperName.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityPaperName.setStatus(_A)
_Mediatype_ObjectIdentity=ObjectIdentity
mediatype=_Mediatype_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4))
_BrCapabilityMediatypeCount_Type=Integer32
_BrCapabilityMediatypeCount_Object=MibScalar
brCapabilityMediatypeCount=_BrCapabilityMediatypeCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4,1),_BrCapabilityMediatypeCount_Type())
brCapabilityMediatypeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityMediatypeCount.setStatus(_A)
_BrCapabilityMediatypeTable_Object=MibTable
brCapabilityMediatypeTable=_BrCapabilityMediatypeTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4,2))
if mibBuilder.loadTexts:brCapabilityMediatypeTable.setStatus(_A)
_BrCapabilityMediatypeEntry_Object=MibTableRow
brCapabilityMediatypeEntry=_BrCapabilityMediatypeEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4,2,1))
brCapabilityMediatypeEntry.setIndexNames((0,_E,_Ai))
if mibBuilder.loadTexts:brCapabilityMediatypeEntry.setStatus(_A)
class _BrCapabilityMediatypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCapabilityMediatypeIndex_Type.__name__=_B
_BrCapabilityMediatypeIndex_Object=MibTableColumn
brCapabilityMediatypeIndex=_BrCapabilityMediatypeIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4,2,1,1),_BrCapabilityMediatypeIndex_Type())
brCapabilityMediatypeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityMediatypeIndex.setStatus(_A)
_BrCapabilityMediatypeName_Type=DisplayString
_BrCapabilityMediatypeName_Object=MibTableColumn
brCapabilityMediatypeName=_BrCapabilityMediatypeName_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,4,2,1,2),_BrCapabilityMediatypeName_Type())
brCapabilityMediatypeName.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityMediatypeName.setStatus(_A)
_Resolution_ObjectIdentity=ObjectIdentity
resolution=_Resolution_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5))
_BrCapabilityResolutionCount_Type=Integer32
_BrCapabilityResolutionCount_Object=MibScalar
brCapabilityResolutionCount=_BrCapabilityResolutionCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5,1),_BrCapabilityResolutionCount_Type())
brCapabilityResolutionCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityResolutionCount.setStatus(_A)
_BrCapabilityResolutionTable_Object=MibTable
brCapabilityResolutionTable=_BrCapabilityResolutionTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5,2))
if mibBuilder.loadTexts:brCapabilityResolutionTable.setStatus(_A)
_BrCapabilityResolutionEntry_Object=MibTableRow
brCapabilityResolutionEntry=_BrCapabilityResolutionEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5,2,1))
brCapabilityResolutionEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:brCapabilityResolutionEntry.setStatus(_A)
class _BrCapabilityResolutionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrCapabilityResolutionIndex_Type.__name__=_B
_BrCapabilityResolutionIndex_Object=MibTableColumn
brCapabilityResolutionIndex=_BrCapabilityResolutionIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5,2,1,1),_BrCapabilityResolutionIndex_Type())
brCapabilityResolutionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityResolutionIndex.setStatus(_A)
_BrCapabilityResolution_Type=Integer32
_BrCapabilityResolution_Object=MibTableColumn
brCapabilityResolution=_BrCapabilityResolution_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,53,5,2,1,2),_BrCapabilityResolution_Type())
brCapabilityResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:brCapabilityResolution.setStatus(_A)
_Countinfo_ObjectIdentity=ObjectIdentity
countinfo=_Countinfo_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54))
_Pfkit_ObjectIdentity=ObjectIdentity
pfkit=_Pfkit_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1))
_BrPfKitIndexCount_Type=Integer32
_BrPfKitIndexCount_Object=MibScalar
brPfKitIndexCount=_BrPfKitIndexCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,1),_BrPfKitIndexCount_Type())
brPfKitIndexCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brPfKitIndexCount.setStatus(_A)
_BrPfKitTable_Object=MibTable
brPfKitTable=_BrPfKitTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,2))
if mibBuilder.loadTexts:brPfKitTable.setStatus(_A)
_BrPfKitEntry_Object=MibTableRow
brPfKitEntry=_BrPfKitEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,2,1))
brPfKitEntry.setIndexNames((0,_E,_Ak))
if mibBuilder.loadTexts:brPfKitEntry.setStatus(_A)
class _BrPfKitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPfKitIndex_Type.__name__=_B
_BrPfKitIndex_Object=MibTableColumn
brPfKitIndex=_BrPfKitIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,2,1,1),_BrPfKitIndex_Type())
brPfKitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPfKitIndex.setStatus(_A)
class _BrPfKitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10,20)));namedValues=NamedValues(*(('pfkit1',1),('pfkit2',2),('pfkit3',3),('pfkit4',4),('pfkitmp',10),('pfkitdx',20)))
_BrPfKitType_Type.__name__=_B
_BrPfKitType_Object=MibTableColumn
brPfKitType=_BrPfKitType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,2,1,2),_BrPfKitType_Type())
brPfKitType.setMaxAccess(_D)
if mibBuilder.loadTexts:brPfKitType.setStatus(_A)
_BrPfKitCount_Type=Counter32
_BrPfKitCount_Object=MibTableColumn
brPfKitCount=_BrPfKitCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,1,2,1,3),_BrPfKitCount_Type())
brPfKitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brPfKitCount.setStatus(_A)
_Scancount_ObjectIdentity=ObjectIdentity
scancount=_Scancount_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2))
_BrScanCountIndexCount_Type=Integer32
_BrScanCountIndexCount_Object=MibScalar
brScanCountIndexCount=_BrScanCountIndexCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,1),_BrScanCountIndexCount_Type())
brScanCountIndexCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brScanCountIndexCount.setStatus(_A)
_BrScanCountTable_Object=MibTable
brScanCountTable=_BrScanCountTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,2))
if mibBuilder.loadTexts:brScanCountTable.setStatus(_A)
_BrScanCountEntry_Object=MibTableRow
brScanCountEntry=_BrScanCountEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,2,1))
brScanCountEntry.setIndexNames((0,_E,_Al))
if mibBuilder.loadTexts:brScanCountEntry.setStatus(_A)
class _BrScanCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrScanCountIndex_Type.__name__=_B
_BrScanCountIndex_Object=MibTableColumn
brScanCountIndex=_BrScanCountIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,2,1,1),_BrScanCountIndex_Type())
brScanCountIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brScanCountIndex.setStatus(_A)
class _BrScanCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adf',1),('fb',2),('adfdx',3)))
_BrScanCountType_Type.__name__=_B
_BrScanCountType_Object=MibTableColumn
brScanCountType=_BrScanCountType_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,2,1,2),_BrScanCountType_Type())
brScanCountType.setMaxAccess(_D)
if mibBuilder.loadTexts:brScanCountType.setStatus(_A)
_BrScanCountCounter_Type=Counter32
_BrScanCountCounter_Object=MibTableColumn
brScanCountCounter=_BrScanCountCounter_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,54,2,2,1,3),_BrScanCountCounter_Type())
brScanCountCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:brScanCountCounter.setStatus(_A)
_Firmwareupdatekeyword_ObjectIdentity=ObjectIdentity
firmwareupdatekeyword=_Firmwareupdatekeyword_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55))
class _BrFirmwareUpdateKeywordCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrFirmwareUpdateKeywordCount_Type.__name__=_B
_BrFirmwareUpdateKeywordCount_Object=MibScalar
brFirmwareUpdateKeywordCount=_BrFirmwareUpdateKeywordCount_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55,1),_BrFirmwareUpdateKeywordCount_Type())
brFirmwareUpdateKeywordCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brFirmwareUpdateKeywordCount.setStatus(_A)
_BrFirmwareUpdateKeywordTable_Object=MibTable
brFirmwareUpdateKeywordTable=_BrFirmwareUpdateKeywordTable_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55,2))
if mibBuilder.loadTexts:brFirmwareUpdateKeywordTable.setStatus(_A)
_BrFirmwareUpdateKeywordEntry_Object=MibTableRow
brFirmwareUpdateKeywordEntry=_BrFirmwareUpdateKeywordEntry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55,2,1))
brFirmwareUpdateKeywordEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:brFirmwareUpdateKeywordEntry.setStatus(_A)
class _BrFirmwareUpdateKeywordIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrFirmwareUpdateKeywordIndex_Type.__name__=_B
_BrFirmwareUpdateKeywordIndex_Object=MibTableColumn
brFirmwareUpdateKeywordIndex=_BrFirmwareUpdateKeywordIndex_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55,2,1,1),_BrFirmwareUpdateKeywordIndex_Type())
brFirmwareUpdateKeywordIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brFirmwareUpdateKeywordIndex.setStatus(_A)
class _BrFirmwareUpdateKeyword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrFirmwareUpdateKeyword_Type.__name__=_G
_BrFirmwareUpdateKeyword_Object=MibTableColumn
brFirmwareUpdateKeyword=_BrFirmwareUpdateKeyword_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,5,55,2,1,2),_BrFirmwareUpdateKeyword_Type())
brFirmwareUpdateKeyword.setMaxAccess(_D)
if mibBuilder.loadTexts:brFirmwareUpdateKeyword.setStatus(_A)
_Printerstatus_ObjectIdentity=ObjectIdentity
printerstatus=_Printerstatus_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,6))
class _BrStatusSleep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrStatusSleep_Type.__name__=_B
_BrStatusSleep_Object=MibScalar
brStatusSleep=_BrStatusSleep_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,6,1),_BrStatusSleep_Type())
brStatusSleep.setMaxAccess(_D)
if mibBuilder.loadTexts:brStatusSleep.setStatus(_A)
_Secret_ObjectIdentity=ObjectIdentity
secret=_Secret_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7))
class _BrSecretMPRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrSecretMPRetry_Type.__name__=_B
_BrSecretMPRetry_Object=MibScalar
brSecretMPRetry=_BrSecretMPRetry_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7,1),_BrSecretMPRetry_Type())
brSecretMPRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecretMPRetry.setStatus(_A)
_BrSecretReprint_Type=Integer32
_BrSecretReprint_Object=MibScalar
brSecretReprint=_BrSecretReprint_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7,2),_BrSecretReprint_Type())
brSecretReprint.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecretReprint.setStatus(_A)
class _BrFontSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFontSetting_Type.__name__=_B
_BrFontSetting_Object=MibScalar
brFontSetting=_BrFontSetting_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7,3),_BrFontSetting_Type())
brFontSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:brFontSetting.setStatus(_A)
class _BrFontSwitchOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFontSwitchOn_Type.__name__=_B
_BrFontSwitchOn_Object=MibScalar
brFontSwitchOn=_BrFontSwitchOn_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7,4),_BrFontSwitchOn_Type())
brFontSwitchOn.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontSwitchOn.setStatus(_A)
class _BrFontSwitchOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_BrFontSwitchOff_Type.__name__=_B
_BrFontSwitchOff_Object=MibScalar
brFontSwitchOff=_BrFontSwitchOff_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,7,5),_BrFontSwitchOff_Type())
brFontSwitchOff.setMaxAccess(_C)
if mibBuilder.loadTexts:brFontSwitchOff.setStatus(_A)
_Adminsetting_ObjectIdentity=ObjectIdentity
adminsetting=_Adminsetting_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8))
_Clockfunction_ObjectIdentity=ObjectIdentity
clockfunction=_Clockfunction_ObjectIdentity((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8,1))
class _BrClockFuncTimeStyle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrClockFuncTimeStyle_Type.__name__=_B
_BrClockFuncTimeStyle_Object=MibScalar
brClockFuncTimeStyle=_BrClockFuncTimeStyle_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8,1,1),_BrClockFuncTimeStyle_Type())
brClockFuncTimeStyle.setMaxAccess(_C)
if mibBuilder.loadTexts:brClockFuncTimeStyle.setStatus(_A)
class _BrClockFuncSummerTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrClockFuncSummerTime_Type.__name__=_B
_BrClockFuncSummerTime_Object=MibScalar
brClockFuncSummerTime=_BrClockFuncSummerTime_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8,1,2),_BrClockFuncSummerTime_Type())
brClockFuncSummerTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brClockFuncSummerTime.setStatus(_A)
class _BrClockFuncTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
_BrClockFuncTimeZone_Type.__name__=_B
_BrClockFuncTimeZone_Object=MibScalar
brClockFuncTimeZone=_BrClockFuncTimeZone_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8,1,3),_BrClockFuncTimeZone_Type())
brClockFuncTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:brClockFuncTimeZone.setStatus(_A)
class _BrClockFuncZoneSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrClockFuncZoneSet_Type.__name__=_B
_BrClockFuncZoneSet_Object=MibScalar
brClockFuncZoneSet=_BrClockFuncZoneSet_Object((1,3,6,1,4,1,2435,2,3,9,4,2,1,5,8,1,4),_BrClockFuncZoneSet_Type())
brClockFuncZoneSet.setMaxAccess(_C)
if mibBuilder.loadTexts:brClockFuncZoneSet.setStatus(_A)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,2435,2,4))
_NpCard_ObjectIdentity=ObjectIdentity
npCard=_NpCard_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3))
_NpSys_ObjectIdentity=ObjectIdentity
npSys=_NpSys_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1))
_NpConfig_ObjectIdentity=ObjectIdentity
npConfig=_NpConfig_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1,1))
class _BrBasicSettingConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unconfigured',1),('configured',2)))
_BrBasicSettingConfigured_Type.__name__=_B
_BrBasicSettingConfigured_Object=MibScalar
brBasicSettingConfigured=_BrBasicSettingConfigured_Object((1,3,6,1,4,1,2435,2,4,3,1,1,1),_BrBasicSettingConfigured_Type())
brBasicSettingConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:brBasicSettingConfigured.setStatus(_A)
_AdminCapa_ObjectIdentity=ObjectIdentity
adminCapa=_AdminCapa_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1,99))
_BrAdminCapability_Type=OctetString
_BrAdminCapability_Object=MibScalar
brAdminCapability=_BrAdminCapability_Object((1,3,6,1,4,1,2435,2,4,3,1,99,1),_BrAdminCapability_Type())
brAdminCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:brAdminCapability.setStatus(_A)
_UserSetting_ObjectIdentity=ObjectIdentity
userSetting=_UserSetting_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1,100))
_BrUserPasswordVerify_Type=DisplayString
_BrUserPasswordVerify_Object=MibScalar
brUserPasswordVerify=_BrUserPasswordVerify_Object((1,3,6,1,4,1,2435,2,4,3,1,100,1),_BrUserPasswordVerify_Type())
brUserPasswordVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:brUserPasswordVerify.setStatus(_A)
_BrUserPassword_Type=DisplayString
_BrUserPassword_Object=MibScalar
brUserPassword=_BrUserPassword_Object((1,3,6,1,4,1,2435,2,4,3,1,100,2),_BrUserPassword_Type())
brUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brUserPassword.setStatus(_A)
_Verify_ObjectIdentity=ObjectIdentity
verify=_Verify_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1,101))
class _BrpsVerifyPhysAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_BrpsVerifyPhysAddress_Type.__name__=_G
_BrpsVerifyPhysAddress_Object=MibScalar
brpsVerifyPhysAddress=_BrpsVerifyPhysAddress_Object((1,3,6,1,4,1,2435,2,4,3,1,101,1),_BrpsVerifyPhysAddress_Type())
brpsVerifyPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsVerifyPhysAddress.setStatus(_A)
_NpTcp_ObjectIdentity=ObjectIdentity
npTcp=_NpTcp_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,6))
_Lpd_ObjectIdentity=ObjectIdentity
lpd=_Lpd_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,6,99))
_Banner_ObjectIdentity=ObjectIdentity
banner=_Banner_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,6,99,1))
class _BrLPDBannerPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrLPDBannerPage_Type.__name__=_B
_BrLPDBannerPage_Object=MibScalar
brLPDBannerPage=_BrLPDBannerPage_Object((1,3,6,1,4,1,2435,2,4,3,6,99,1,1),_BrLPDBannerPage_Type())
brLPDBannerPage.setMaxAccess(_C)
if mibBuilder.loadTexts:brLPDBannerPage.setStatus(_A)
_NpCtl_ObjectIdentity=ObjectIdentity
npCtl=_NpCtl_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,7))
_EtherN_ObjectIdentity=ObjectIdentity
etherN=_EtherN_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,7,99))
_ENet_ObjectIdentity=ObjectIdentity
eNet=_ENet_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,7,99,1))
class _BrENetModeSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrENetModeSupported_Type.__name__=_B
_BrENetModeSupported_Object=MibScalar
brENetModeSupported=_BrENetModeSupported_Object((1,3,6,1,4,1,2435,2,4,3,7,99,1,1),_BrENetModeSupported_Type())
brENetModeSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brENetModeSupported.setStatus(_A)
class _BrENetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrENetMode_Type.__name__=_B
_BrENetMode_Object=MibScalar
brENetMode=_BrENetMode_Object((1,3,6,1,4,1,2435,2,4,3,7,99,1,2),_BrENetMode_Type())
brENetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brENetMode.setStatus(_A)
_NpPort_ObjectIdentity=ObjectIdentity
npPort=_NpPort_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,13))
_Funa_ObjectIdentity=ObjectIdentity
funa=_Funa_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,13,10))
class _BrFindPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrFindPort_Type.__name__=_B
_BrFindPort_Object=MibScalar
brFindPort=_BrFindPort_Object((1,3,6,1,4,1,2435,2,4,3,13,10,1),_BrFindPort_Type())
brFindPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brFindPort.setStatus(_A)
class _BrFindTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrFindTime_Type.__name__=_B
_BrFindTime_Object=MibScalar
brFindTime=_BrFindTime_Object((1,3,6,1,4,1,2435,2,4,3,13,10,2),_BrFindTime_Type())
brFindTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brFindTime.setStatus(_A)
_NpSet_ObjectIdentity=ObjectIdentity
npSet=_NpSet_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99))
_Dns_ObjectIdentity=ObjectIdentity
dns=_Dns_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,1))
class _BrDNSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrDNSSupported_Type.__name__=_B
_BrDNSSupported_Object=MibScalar
brDNSSupported=_BrDNSSupported_Object((1,3,6,1,4,1,2435,2,4,3,99,1,1),_BrDNSSupported_Type())
brDNSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brDNSSupported.setStatus(_A)
_BrPrimaryDNSIP_Type=OctetString
_BrPrimaryDNSIP_Object=MibScalar
brPrimaryDNSIP=_BrPrimaryDNSIP_Object((1,3,6,1,4,1,2435,2,4,3,99,1,2),_BrPrimaryDNSIP_Type())
brPrimaryDNSIP.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrimaryDNSIP.setStatus(_A)
_BrSecondaryDNSIP_Type=OctetString
_BrSecondaryDNSIP_Object=MibScalar
brSecondaryDNSIP=_BrSecondaryDNSIP_Object((1,3,6,1,4,1,2435,2,4,3,99,1,3),_BrSecondaryDNSIP_Type())
brSecondaryDNSIP.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecondaryDNSIP.setStatus(_A)
class _BrDNSIPSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),(_w,2)))
_BrDNSIPSetup_Type.__name__=_B
_BrDNSIPSetup_Object=MibScalar
brDNSIPSetup=_BrDNSIPSetup_Object((1,3,6,1,4,1,2435,2,4,3,99,1,4),_BrDNSIPSetup_Type())
brDNSIPSetup.setMaxAccess(_C)
if mibBuilder.loadTexts:brDNSIPSetup.setStatus(_A)
_BrTCPIPConnectTime_Type=Integer32
_BrTCPIPConnectTime_Object=MibScalar
brTCPIPConnectTime=_BrTCPIPConnectTime_Object((1,3,6,1,4,1,2435,2,4,3,99,1,5),_BrTCPIPConnectTime_Type())
brTCPIPConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brTCPIPConnectTime.setStatus(_A)
class _BrAdvancedDNSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrAdvancedDNSSupported_Type.__name__=_B
_BrAdvancedDNSSupported_Object=MibScalar
brAdvancedDNSSupported=_BrAdvancedDNSSupported_Object((1,3,6,1,4,1,2435,2,4,3,99,1,6),_BrAdvancedDNSSupported_Type())
brAdvancedDNSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brAdvancedDNSSupported.setStatus(_A)
_BrPrimaryDNSIPAddress_Type=IpAddress
_BrPrimaryDNSIPAddress_Object=MibScalar
brPrimaryDNSIPAddress=_BrPrimaryDNSIPAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,1,7),_BrPrimaryDNSIPAddress_Type())
brPrimaryDNSIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrimaryDNSIPAddress.setStatus(_A)
_BrSecondaryDNSIPAddress_Type=IpAddress
_BrSecondaryDNSIPAddress_Object=MibScalar
brSecondaryDNSIPAddress=_BrSecondaryDNSIPAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,1,8),_BrSecondaryDNSIPAddress_Type())
brSecondaryDNSIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecondaryDNSIPAddress.setStatus(_A)
class _BrPOP3ServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrPOP3ServerName_Type.__name__=_G
_BrPOP3ServerName_Object=MibScalar
brPOP3ServerName=_BrPOP3ServerName_Object((1,3,6,1,4,1,2435,2,4,3,99,1,9),_BrPOP3ServerName_Type())
brPOP3ServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brPOP3ServerName.setStatus(_A)
class _BrSMTPServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrSMTPServerName_Type.__name__=_G
_BrSMTPServerName_Object=MibScalar
brSMTPServerName=_BrSMTPServerName_Object((1,3,6,1,4,1,2435,2,4,3,99,1,10),_BrSMTPServerName_Type())
brSMTPServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brSMTPServerName.setStatus(_A)
_Pushstatus_ObjectIdentity=ObjectIdentity
pushstatus=_Pushstatus_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,2))
class _BrPushStatusSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrPushStatusSupported_Type.__name__=_B
_BrPushStatusSupported_Object=MibScalar
brPushStatusSupported=_BrPushStatusSupported_Object((1,3,6,1,4,1,2435,2,4,3,99,2,1),_BrPushStatusSupported_Type())
brPushStatusSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brPushStatusSupported.setStatus(_A)
_Priadmin_ObjectIdentity=ObjectIdentity
priadmin=_Priadmin_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,2,2))
_BrPriMailAddress_Type=OctetString
_BrPriMailAddress_Object=MibScalar
brPriMailAddress=_BrPriMailAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,2,2,1),_BrPriMailAddress_Type())
brPriMailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brPriMailAddress.setStatus(_A)
class _BrPriError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrPriError_Type.__name__=_B
_BrPriError_Object=MibScalar
brPriError=_BrPriError_Object((1,3,6,1,4,1,2435,2,4,3,99,2,2,2),_BrPriError_Type())
brPriError.setMaxAccess(_C)
if mibBuilder.loadTexts:brPriError.setStatus(_A)
_Secadmin_ObjectIdentity=ObjectIdentity
secadmin=_Secadmin_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,2,3))
_BrSecMailAddress_Type=OctetString
_BrSecMailAddress_Object=MibScalar
brSecMailAddress=_BrSecMailAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,2,3,1),_BrSecMailAddress_Type())
brSecMailAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecMailAddress.setStatus(_A)
class _BrSecError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrSecError_Type.__name__=_B
_BrSecError_Object=MibScalar
brSecError=_BrSecError_Object((1,3,6,1,4,1,2435,2,4,3,99,2,3,2),_BrSecError_Type())
brSecError.setMaxAccess(_C)
if mibBuilder.loadTexts:brSecError.setStatus(_A)
class _BrNotificationCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_BrNotificationCount_Type.__name__=_B
_BrNotificationCount_Object=MibScalar
brNotificationCount=_BrNotificationCount_Object((1,3,6,1,4,1,2435,2,4,3,99,2,4),_BrNotificationCount_Type())
brNotificationCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brNotificationCount.setStatus(_A)
_BrNotificationTable_Object=MibTable
brNotificationTable=_BrNotificationTable_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5))
if mibBuilder.loadTexts:brNotificationTable.setStatus(_A)
_BrNotificationEntry_Object=MibTableRow
brNotificationEntry=_BrNotificationEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1))
brNotificationEntry.setIndexNames((0,_E,_AK))
if mibBuilder.loadTexts:brNotificationEntry.setStatus(_A)
class _BrNotificationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrNotificationIndex_Type.__name__=_B
_BrNotificationIndex_Object=MibTableColumn
brNotificationIndex=_BrNotificationIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,1),_BrNotificationIndex_Type())
brNotificationIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brNotificationIndex.setStatus(_A)
_BrNotificationAddress_Type=OctetString
_BrNotificationAddress_Object=MibTableColumn
brNotificationAddress=_BrNotificationAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,2),_BrNotificationAddress_Type())
brNotificationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationAddress.setStatus(_A)
_BrNotificationStatusGroup_Type=Integer32
_BrNotificationStatusGroup_Object=MibTableColumn
brNotificationStatusGroup=_BrNotificationStatusGroup_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,3),_BrNotificationStatusGroup_Type())
brNotificationStatusGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationStatusGroup.setStatus(_A)
_BrNotificationShowURLInfo_Type=Integer32
_BrNotificationShowURLInfo_Object=MibTableColumn
brNotificationShowURLInfo=_BrNotificationShowURLInfo_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,4),_BrNotificationShowURLInfo_Type())
brNotificationShowURLInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationShowURLInfo.setStatus(_A)
_BrNotificationErrorRule_Type=OctetString
_BrNotificationErrorRule_Object=MibTableColumn
brNotificationErrorRule=_BrNotificationErrorRule_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,5),_BrNotificationErrorRule_Type())
brNotificationErrorRule.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationErrorRule.setStatus(_A)
class _BrNotificationRestoration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrNotificationRestoration_Type.__name__=_B
_BrNotificationRestoration_Object=MibTableColumn
brNotificationRestoration=_BrNotificationRestoration_Object((1,3,6,1,4,1,2435,2,4,3,99,2,5,1,6),_BrNotificationRestoration_Type())
brNotificationRestoration.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationRestoration.setStatus(_A)
_BrPrintersEmailaddress_Type=OctetString
_BrPrintersEmailaddress_Object=MibScalar
brPrintersEmailaddress=_BrPrintersEmailaddress_Object((1,3,6,1,4,1,2435,2,4,3,99,2,6),_BrPrintersEmailaddress_Type())
brPrintersEmailaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brPrintersEmailaddress.setStatus(_A)
_BrNotificationVersion_Type=OctetString
_BrNotificationVersion_Object=MibScalar
brNotificationVersion=_BrNotificationVersion_Object((1,3,6,1,4,1,2435,2,4,3,99,2,7),_BrNotificationVersion_Type())
brNotificationVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:brNotificationVersion.setStatus(_A)
class _BrShowIPAddressInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrShowIPAddressInfo_Type.__name__=_B
_BrShowIPAddressInfo_Object=MibScalar
brShowIPAddressInfo=_BrShowIPAddressInfo_Object((1,3,6,1,4,1,2435,2,4,3,99,2,8),_BrShowIPAddressInfo_Type())
brShowIPAddressInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:brShowIPAddressInfo.setStatus(_A)
_BrNotificationRuleTable_Object=MibTable
brNotificationRuleTable=_BrNotificationRuleTable_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50))
if mibBuilder.loadTexts:brNotificationRuleTable.setStatus(_A)
_BrNotificationRuleEntry_Object=MibTableRow
brNotificationRuleEntry=_BrNotificationRuleEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50,1))
brNotificationRuleEntry.setIndexNames((0,_E,_AK),(0,_E,_An))
if mibBuilder.loadTexts:brNotificationRuleEntry.setStatus(_A)
class _BrNotificationRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrNotificationRuleIndex_Type.__name__=_B
_BrNotificationRuleIndex_Object=MibTableColumn
brNotificationRuleIndex=_BrNotificationRuleIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50,1,1),_BrNotificationRuleIndex_Type())
brNotificationRuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brNotificationRuleIndex.setStatus(_A)
class _BrNotificationStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('coverOpen',1),('jam',2),('tonerLow',3),('tonerEmpty',4),('userConsumableWarning',5),('userConsumableError',6),('servicemanConsumableWarning',7),('servicemanConsumableError',8),('changeDrum',9),('memoryFull',10),('inputMediaError',11),('outputFull',12),('notInstalled',13),('machineError',14),('otherErrors',15)))
_BrNotificationStatusID_Type.__name__=_B
_BrNotificationStatusID_Object=MibTableColumn
brNotificationStatusID=_BrNotificationStatusID_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50,1,2),_BrNotificationStatusID_Type())
brNotificationStatusID.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationStatusID.setStatus(_A)
class _BrNotificationMainRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('everytime',2),('times',3),('minutes',4)))
_BrNotificationMainRule_Type.__name__=_B
_BrNotificationMainRule_Object=MibTableColumn
brNotificationMainRule=_BrNotificationMainRule_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50,1,3),_BrNotificationMainRule_Type())
brNotificationMainRule.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationMainRule.setStatus(_A)
_BrNotificationRuleValue_Type=Integer32
_BrNotificationRuleValue_Object=MibTableColumn
brNotificationRuleValue=_BrNotificationRuleValue_Object((1,3,6,1,4,1,2435,2,4,3,99,2,50,1,4),_BrNotificationRuleValue_Type())
brNotificationRuleValue.setMaxAccess(_C)
if mibBuilder.loadTexts:brNotificationRuleValue.setStatus(_A)
_Pjl_ObjectIdentity=ObjectIdentity
pjl=_Pjl_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,3))
_Pjlinfo_ObjectIdentity=ObjectIdentity
pjlinfo=_Pjlinfo_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,3,1))
_BrPJLInfoOptionsTable_Object=MibTable
brPJLInfoOptionsTable=_BrPJLInfoOptionsTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,1))
if mibBuilder.loadTexts:brPJLInfoOptionsTable.setStatus(_A)
_BrPJLInfoOptionsEntry_Object=MibTableRow
brPJLInfoOptionsEntry=_BrPJLInfoOptionsEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,1,1))
brPJLInfoOptionsEntry.setIndexNames((0,_E,_Ao))
if mibBuilder.loadTexts:brPJLInfoOptionsEntry.setStatus(_A)
class _BrPJLInfoOptionsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoOptionsIndex_Type.__name__=_B
_BrPJLInfoOptionsIndex_Object=MibTableColumn
brPJLInfoOptionsIndex=_BrPJLInfoOptionsIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,1,1,1),_BrPJLInfoOptionsIndex_Type())
brPJLInfoOptionsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoOptionsIndex.setStatus(_A)
class _BrPJLInfoOptions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrPJLInfoOptions_Type.__name__=_G
_BrPJLInfoOptions_Object=MibTableColumn
brPJLInfoOptions=_BrPJLInfoOptions_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,1,1,2),_BrPJLInfoOptions_Type())
brPJLInfoOptions.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoOptions.setStatus(_A)
_BrPJLInfoIntrayconfigTable_Object=MibTable
brPJLInfoIntrayconfigTable=_BrPJLInfoIntrayconfigTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,2))
if mibBuilder.loadTexts:brPJLInfoIntrayconfigTable.setStatus(_A)
_BrPJLInfoIntrayconfigEntry_Object=MibTableRow
brPJLInfoIntrayconfigEntry=_BrPJLInfoIntrayconfigEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,2,1))
brPJLInfoIntrayconfigEntry.setIndexNames((0,_E,_Ap))
if mibBuilder.loadTexts:brPJLInfoIntrayconfigEntry.setStatus(_A)
class _BrPJLInfoIntrayconfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoIntrayconfigIndex_Type.__name__=_B
_BrPJLInfoIntrayconfigIndex_Object=MibTableColumn
brPJLInfoIntrayconfigIndex=_BrPJLInfoIntrayconfigIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,2,1,1),_BrPJLInfoIntrayconfigIndex_Type())
brPJLInfoIntrayconfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoIntrayconfigIndex.setStatus(_A)
class _BrPJLInfoIntrayconfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrPJLInfoIntrayconfig_Type.__name__=_G
_BrPJLInfoIntrayconfig_Object=MibTableColumn
brPJLInfoIntrayconfig=_BrPJLInfoIntrayconfig_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,2,1,2),_BrPJLInfoIntrayconfig_Type())
brPJLInfoIntrayconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoIntrayconfig.setStatus(_A)
_BrPJLInfoOuttrayconfigTable_Object=MibTable
brPJLInfoOuttrayconfigTable=_BrPJLInfoOuttrayconfigTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,3))
if mibBuilder.loadTexts:brPJLInfoOuttrayconfigTable.setStatus(_A)
_BrPJLInfoOuttrayconfigEntry_Object=MibTableRow
brPJLInfoOuttrayconfigEntry=_BrPJLInfoOuttrayconfigEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,3,1))
brPJLInfoOuttrayconfigEntry.setIndexNames((0,_E,_Aq))
if mibBuilder.loadTexts:brPJLInfoOuttrayconfigEntry.setStatus(_A)
class _BrPJLInfoOuttrayconfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoOuttrayconfigIndex_Type.__name__=_B
_BrPJLInfoOuttrayconfigIndex_Object=MibTableColumn
brPJLInfoOuttrayconfigIndex=_BrPJLInfoOuttrayconfigIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,3,1,1),_BrPJLInfoOuttrayconfigIndex_Type())
brPJLInfoOuttrayconfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoOuttrayconfigIndex.setStatus(_A)
class _BrPJLInfoOuttrayconfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrPJLInfoOuttrayconfig_Type.__name__=_G
_BrPJLInfoOuttrayconfig_Object=MibTableColumn
brPJLInfoOuttrayconfig=_BrPJLInfoOuttrayconfig_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,3,1,2),_BrPJLInfoOuttrayconfig_Type())
brPJLInfoOuttrayconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoOuttrayconfig.setStatus(_A)
_BrPJLInfoDXconfigTable_Object=MibTable
brPJLInfoDXconfigTable=_BrPJLInfoDXconfigTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,4))
if mibBuilder.loadTexts:brPJLInfoDXconfigTable.setStatus(_A)
_BrPJLInfoDXconfigEntry_Object=MibTableRow
brPJLInfoDXconfigEntry=_BrPJLInfoDXconfigEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,4,1))
brPJLInfoDXconfigEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:brPJLInfoDXconfigEntry.setStatus(_A)
class _BrPJLInfoDXconfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoDXconfigIndex_Type.__name__=_B
_BrPJLInfoDXconfigIndex_Object=MibTableColumn
brPJLInfoDXconfigIndex=_BrPJLInfoDXconfigIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,4,1,1),_BrPJLInfoDXconfigIndex_Type())
brPJLInfoDXconfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoDXconfigIndex.setStatus(_A)
class _BrPJLInfoDXconfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrPJLInfoDXconfig_Type.__name__=_G
_BrPJLInfoDXconfig_Object=MibTableColumn
brPJLInfoDXconfig=_BrPJLInfoDXconfig_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,4,1,2),_BrPJLInfoDXconfig_Type())
brPJLInfoDXconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoDXconfig.setStatus(_A)
_BrPJLInfoStorageconfigTable_Object=MibTable
brPJLInfoStorageconfigTable=_BrPJLInfoStorageconfigTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,5))
if mibBuilder.loadTexts:brPJLInfoStorageconfigTable.setStatus(_A)
_BrPJLInfoStorageconfigEntry_Object=MibTableRow
brPJLInfoStorageconfigEntry=_BrPJLInfoStorageconfigEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,5,1))
brPJLInfoStorageconfigEntry.setIndexNames((0,_E,_As))
if mibBuilder.loadTexts:brPJLInfoStorageconfigEntry.setStatus(_A)
class _BrPJLInfoStorageconfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoStorageconfigIndex_Type.__name__=_B
_BrPJLInfoStorageconfigIndex_Object=MibTableColumn
brPJLInfoStorageconfigIndex=_BrPJLInfoStorageconfigIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,5,1,1),_BrPJLInfoStorageconfigIndex_Type())
brPJLInfoStorageconfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoStorageconfigIndex.setStatus(_A)
class _BrPJLInfoStorageconfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrPJLInfoStorageconfig_Type.__name__=_G
_BrPJLInfoStorageconfig_Object=MibTableColumn
brPJLInfoStorageconfig=_BrPJLInfoStorageconfig_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,5,1,2),_BrPJLInfoStorageconfig_Type())
brPJLInfoStorageconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoStorageconfig.setStatus(_A)
_BrPJLInfoFirmwareUpdateconfigTable_Object=MibTable
brPJLInfoFirmwareUpdateconfigTable=_BrPJLInfoFirmwareUpdateconfigTable_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,6))
if mibBuilder.loadTexts:brPJLInfoFirmwareUpdateconfigTable.setStatus(_A)
_BrPJLInfoFirmwareUpdateconfigEntry_Object=MibTableRow
brPJLInfoFirmwareUpdateconfigEntry=_BrPJLInfoFirmwareUpdateconfigEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,6,1))
brPJLInfoFirmwareUpdateconfigEntry.setIndexNames((0,_E,_At))
if mibBuilder.loadTexts:brPJLInfoFirmwareUpdateconfigEntry.setStatus(_A)
class _BrPJLInfoFirmwareUpdateconfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrPJLInfoFirmwareUpdateconfigIndex_Type.__name__=_B
_BrPJLInfoFirmwareUpdateconfigIndex_Object=MibTableColumn
brPJLInfoFirmwareUpdateconfigIndex=_BrPJLInfoFirmwareUpdateconfigIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,6,1,1),_BrPJLInfoFirmwareUpdateconfigIndex_Type())
brPJLInfoFirmwareUpdateconfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoFirmwareUpdateconfigIndex.setStatus(_A)
class _BrPJLInfoFirmwareUpdateconfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrPJLInfoFirmwareUpdateconfig_Type.__name__=_G
_BrPJLInfoFirmwareUpdateconfig_Object=MibTableColumn
brPJLInfoFirmwareUpdateconfig=_BrPJLInfoFirmwareUpdateconfig_Object((1,3,6,1,4,1,2435,2,4,3,99,3,1,6,1,2),_BrPJLInfoFirmwareUpdateconfig_Type())
brPJLInfoFirmwareUpdateconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:brPJLInfoFirmwareUpdateconfig.setStatus(_A)
_EMailReports_ObjectIdentity=ObjectIdentity
eMailReports=_EMailReports_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,99,4))
class _BrEmailReportsSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrEmailReportsSupported_Type.__name__=_B
_BrEmailReportsSupported_Object=MibScalar
brEmailReportsSupported=_BrEmailReportsSupported_Object((1,3,6,1,4,1,2435,2,4,3,99,4,1),_BrEmailReportsSupported_Type())
brEmailReportsSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brEmailReportsSupported.setStatus(_A)
_BrEmailReportsCount_Type=Integer32
_BrEmailReportsCount_Object=MibScalar
brEmailReportsCount=_BrEmailReportsCount_Object((1,3,6,1,4,1,2435,2,4,3,99,4,2),_BrEmailReportsCount_Type())
brEmailReportsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brEmailReportsCount.setStatus(_A)
_BrEmailReportsTable_Object=MibTable
brEmailReportsTable=_BrEmailReportsTable_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11))
if mibBuilder.loadTexts:brEmailReportsTable.setStatus(_A)
_BrEmailReportsEntry_Object=MibTableRow
brEmailReportsEntry=_BrEmailReportsEntry_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1))
brEmailReportsEntry.setIndexNames((0,_E,_Au))
if mibBuilder.loadTexts:brEmailReportsEntry.setStatus(_A)
class _BrEmailReportsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrEmailReportsIndex_Type.__name__=_B
_BrEmailReportsIndex_Object=MibTableColumn
brEmailReportsIndex=_BrEmailReportsIndex_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,1),_BrEmailReportsIndex_Type())
brEmailReportsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brEmailReportsIndex.setStatus(_A)
class _BrEmailReportsAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_BrEmailReportsAddress_Type.__name__=_G
_BrEmailReportsAddress_Object=MibTableColumn
brEmailReportsAddress=_BrEmailReportsAddress_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,2),_BrEmailReportsAddress_Type())
brEmailReportsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsAddress.setStatus(_A)
class _BrEmailReportsFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('daily',1),('weekly',2),('monthly',3)))
_BrEmailReportsFrequency_Type.__name__=_B
_BrEmailReportsFrequency_Object=MibTableColumn
brEmailReportsFrequency=_BrEmailReportsFrequency_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,3),_BrEmailReportsFrequency_Type())
brEmailReportsFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsFrequency.setStatus(_A)
_BrEmailReportsTime_Type=OctetString
_BrEmailReportsTime_Object=MibTableColumn
brEmailReportsTime=_BrEmailReportsTime_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,4),_BrEmailReportsTime_Type())
brEmailReportsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsTime.setStatus(_A)
class _BrEmailReportsWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sunday',1),('monday',2),('tuesday',3),('wednesday',4),('thursday',5),('friday',6),('saturday',7)))
_BrEmailReportsWeek_Type.__name__=_B
_BrEmailReportsWeek_Object=MibTableColumn
brEmailReportsWeek=_BrEmailReportsWeek_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,5),_BrEmailReportsWeek_Type())
brEmailReportsWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsWeek.setStatus(_A)
class _BrEmailReportsDate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_BrEmailReportsDate_Type.__name__=_B
_BrEmailReportsDate_Object=MibTableColumn
brEmailReportsDate=_BrEmailReportsDate_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,6),_BrEmailReportsDate_Type())
brEmailReportsDate.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsDate.setStatus(_A)
class _BrEmailReportsSendReportNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrEmailReportsSendReportNow_Type.__name__=_B
_BrEmailReportsSendReportNow_Object=MibTableColumn
brEmailReportsSendReportNow=_BrEmailReportsSendReportNow_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,7),_BrEmailReportsSendReportNow_Type())
brEmailReportsSendReportNow.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsSendReportNow.setStatus(_A)
class _BrEmailReportsSendReportatPowerOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrEmailReportsSendReportatPowerOn_Type.__name__=_B
_BrEmailReportsSendReportatPowerOn_Object=MibTableColumn
brEmailReportsSendReportatPowerOn=_BrEmailReportsSendReportatPowerOn_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,8),_BrEmailReportsSendReportatPowerOn_Type())
brEmailReportsSendReportatPowerOn.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsSendReportatPowerOn.setStatus(_A)
class _BrEmailReportsNoRTCFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_BrEmailReportsNoRTCFrequency_Type.__name__=_B
_BrEmailReportsNoRTCFrequency_Object=MibTableColumn
brEmailReportsNoRTCFrequency=_BrEmailReportsNoRTCFrequency_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,9),_BrEmailReportsNoRTCFrequency_Type())
brEmailReportsNoRTCFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsNoRTCFrequency.setStatus(_A)
class _BrEmailReportsReportFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('plaintext',1),('xml',2)))
_BrEmailReportsReportFormat_Type.__name__=_B
_BrEmailReportsReportFormat_Object=MibTableColumn
brEmailReportsReportFormat=_BrEmailReportsReportFormat_Object((1,3,6,1,4,1,2435,2,4,3,99,4,11,1,10),_BrEmailReportsReportFormat_Type())
brEmailReportsReportFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:brEmailReportsReportFormat.setStatus(_A)
_Wireless_ObjectIdentity=ObjectIdentity
wireless=_Wireless_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100))
_WlInfo_ObjectIdentity=ObjectIdentity
wlInfo=_WlInfo_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1))
_WlCapability_ObjectIdentity=ObjectIdentity
wlCapability=_WlCapability_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,1))
_BrpsWLanDot11Supported_Type=Integer32
_BrpsWLanDot11Supported_Object=MibScalar
brpsWLanDot11Supported=_BrpsWLanDot11Supported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,1),_BrpsWLanDot11Supported_Type())
brpsWLanDot11Supported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanDot11Supported.setStatus(_A)
_BrpsWLanAvailableChannel_Type=OctetString
_BrpsWLanAvailableChannel_Object=MibScalar
brpsWLanAvailableChannel=_BrpsWLanAvailableChannel_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,2),_BrpsWLanAvailableChannel_Type())
brpsWLanAvailableChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAvailableChannel.setStatus(_A)
_BrpsWLanCapabilityEncryptModeCount_Type=Integer32
_BrpsWLanCapabilityEncryptModeCount_Object=MibScalar
brpsWLanCapabilityEncryptModeCount=_BrpsWLanCapabilityEncryptModeCount_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,3),_BrpsWLanCapabilityEncryptModeCount_Type())
brpsWLanCapabilityEncryptModeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeCount.setStatus(_A)
_BrpsWLanCapabilityEncryptModeTable_Object=MibTable
brpsWLanCapabilityEncryptModeTable=_BrpsWLanCapabilityEncryptModeTable_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4))
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeTable.setStatus(_A)
_BrpsWLanCapabilityEncryptModeEntry_Object=MibTableRow
brpsWLanCapabilityEncryptModeEntry=_BrpsWLanCapabilityEncryptModeEntry_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4,1))
brpsWLanCapabilityEncryptModeEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeEntry.setStatus(_A)
class _BrpsWLanCapabilityEncryptModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrpsWLanCapabilityEncryptModeIndex_Type.__name__=_B
_BrpsWLanCapabilityEncryptModeIndex_Object=MibTableColumn
brpsWLanCapabilityEncryptModeIndex=_BrpsWLanCapabilityEncryptModeIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4,1,1),_BrpsWLanCapabilityEncryptModeIndex_Type())
brpsWLanCapabilityEncryptModeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeIndex.setStatus(_A)
class _BrpsWLanCapabilityEncryptModeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_AA,1),('wep',2),('tkip',3),('aes',4),('ckip',5)))
_BrpsWLanCapabilityEncryptModeType_Type.__name__=_B
_BrpsWLanCapabilityEncryptModeType_Object=MibTableColumn
brpsWLanCapabilityEncryptModeType=_BrpsWLanCapabilityEncryptModeType_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4,1,2),_BrpsWLanCapabilityEncryptModeType_Type())
brpsWLanCapabilityEncryptModeType.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeType.setStatus(_A)
_BrpsWLanCapabilityEncryptModeDescription_Type=OctetString
_BrpsWLanCapabilityEncryptModeDescription_Object=MibTableColumn
brpsWLanCapabilityEncryptModeDescription=_BrpsWLanCapabilityEncryptModeDescription_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4,1,3),_BrpsWLanCapabilityEncryptModeDescription_Type())
brpsWLanCapabilityEncryptModeDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeDescription.setStatus(_A)
_BrpsWLanCapabilityEncryptModeSupported_Type=Integer32
_BrpsWLanCapabilityEncryptModeSupported_Object=MibTableColumn
brpsWLanCapabilityEncryptModeSupported=_BrpsWLanCapabilityEncryptModeSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,4,1,4),_BrpsWLanCapabilityEncryptModeSupported_Type())
brpsWLanCapabilityEncryptModeSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityEncryptModeSupported.setStatus(_A)
_BrpsWLanCapabilityAuthModeCount_Type=Integer32
_BrpsWLanCapabilityAuthModeCount_Object=MibScalar
brpsWLanCapabilityAuthModeCount=_BrpsWLanCapabilityAuthModeCount_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,5),_BrpsWLanCapabilityAuthModeCount_Type())
brpsWLanCapabilityAuthModeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeCount.setStatus(_A)
_BrpsWLanCapabilityAuthModeTable_Object=MibTable
brpsWLanCapabilityAuthModeTable=_BrpsWLanCapabilityAuthModeTable_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6))
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeTable.setStatus(_A)
_BrpsWLanCapabilityAuthModeEntry_Object=MibTableRow
brpsWLanCapabilityAuthModeEntry=_BrpsWLanCapabilityAuthModeEntry_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6,1))
brpsWLanCapabilityAuthModeEntry.setIndexNames((0,_E,_Aw))
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeEntry.setStatus(_A)
class _BrpsWLanCapabilitAuthModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrpsWLanCapabilitAuthModeIndex_Type.__name__=_B
_BrpsWLanCapabilitAuthModeIndex_Object=MibTableColumn
brpsWLanCapabilitAuthModeIndex=_BrpsWLanCapabilitAuthModeIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6,1,1),_BrpsWLanCapabilitAuthModeIndex_Type())
brpsWLanCapabilitAuthModeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilitAuthModeIndex.setStatus(_A)
class _BrpsWLanCapabilityAuthModeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('opensystem',1),('shardkey',2),('wpa-psk',3),('wpa-none',4),('wpa',5),('wpa2',6),(_AC,7),(_AD,8),(_AE,9),(_AF,10),(_AG,11),('wpa2-psk',12)))
_BrpsWLanCapabilityAuthModeType_Type.__name__=_B
_BrpsWLanCapabilityAuthModeType_Object=MibTableColumn
brpsWLanCapabilityAuthModeType=_BrpsWLanCapabilityAuthModeType_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6,1,2),_BrpsWLanCapabilityAuthModeType_Type())
brpsWLanCapabilityAuthModeType.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeType.setStatus(_A)
_BrpsWLanCapabilityAuthModeDescription_Type=OctetString
_BrpsWLanCapabilityAuthModeDescription_Object=MibTableColumn
brpsWLanCapabilityAuthModeDescription=_BrpsWLanCapabilityAuthModeDescription_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6,1,3),_BrpsWLanCapabilityAuthModeDescription_Type())
brpsWLanCapabilityAuthModeDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeDescription.setStatus(_A)
_BrpsWLanCapabilityAuthModeSupported_Type=Integer32
_BrpsWLanCapabilityAuthModeSupported_Object=MibTableColumn
brpsWLanCapabilityAuthModeSupported=_BrpsWLanCapabilityAuthModeSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,6,1,4),_BrpsWLanCapabilityAuthModeSupported_Type())
brpsWLanCapabilityAuthModeSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthModeSupported.setStatus(_A)
_BrpsWLanCapabilityAuthEAPCount_Type=Integer32
_BrpsWLanCapabilityAuthEAPCount_Object=MibScalar
brpsWLanCapabilityAuthEAPCount=_BrpsWLanCapabilityAuthEAPCount_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,7),_BrpsWLanCapabilityAuthEAPCount_Type())
brpsWLanCapabilityAuthEAPCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPCount.setStatus(_A)
_BrpsWLanCapabilityAuthEAPTable_Object=MibTable
brpsWLanCapabilityAuthEAPTable=_BrpsWLanCapabilityAuthEAPTable_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8))
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPTable.setStatus(_A)
_BrpsWLanCapabilityAuthEAPEntry_Object=MibTableRow
brpsWLanCapabilityAuthEAPEntry=_BrpsWLanCapabilityAuthEAPEntry_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1))
brpsWLanCapabilityAuthEAPEntry.setIndexNames((0,_E,_Ax))
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPEntry.setStatus(_A)
class _BrpsWLanCapabilityAuthEAPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrpsWLanCapabilityAuthEAPIndex_Type.__name__=_B
_BrpsWLanCapabilityAuthEAPIndex_Object=MibTableColumn
brpsWLanCapabilityAuthEAPIndex=_BrpsWLanCapabilityAuthEAPIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,1),_BrpsWLanCapabilityAuthEAPIndex_Type())
brpsWLanCapabilityAuthEAPIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPIndex.setStatus(_A)
class _BrpsWLanCapabilityAuthEAPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('eap-md5',1),('eap-tls',2),('eap-ttls',3),('peap',4),(_AC,5),(_AD,6),(_AE,7),(_AF,8),(_AG,9)))
_BrpsWLanCapabilityAuthEAPType_Type.__name__=_B
_BrpsWLanCapabilityAuthEAPType_Object=MibTableColumn
brpsWLanCapabilityAuthEAPType=_BrpsWLanCapabilityAuthEAPType_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,2),_BrpsWLanCapabilityAuthEAPType_Type())
brpsWLanCapabilityAuthEAPType.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPType.setStatus(_A)
_BrpsWLanCapabilityAuthEAPDescription_Type=OctetString
_BrpsWLanCapabilityAuthEAPDescription_Object=MibTableColumn
brpsWLanCapabilityAuthEAPDescription=_BrpsWLanCapabilityAuthEAPDescription_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,3),_BrpsWLanCapabilityAuthEAPDescription_Type())
brpsWLanCapabilityAuthEAPDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPDescription.setStatus(_A)
_BrpsWLanCapabilityAuthEAPSupported_Type=Integer32
_BrpsWLanCapabilityAuthEAPSupported_Object=MibTableColumn
brpsWLanCapabilityAuthEAPSupported=_BrpsWLanCapabilityAuthEAPSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,4),_BrpsWLanCapabilityAuthEAPSupported_Type())
brpsWLanCapabilityAuthEAPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPSupported.setStatus(_A)
class _BrpsWLanCapabilityAuthEAPSupportAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BrpsWLanCapabilityAuthEAPSupportAuthentication_Type.__name__=_B
_BrpsWLanCapabilityAuthEAPSupportAuthentication_Object=MibTableColumn
brpsWLanCapabilityAuthEAPSupportAuthentication=_BrpsWLanCapabilityAuthEAPSupportAuthentication_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,5),_BrpsWLanCapabilityAuthEAPSupportAuthentication_Type())
brpsWLanCapabilityAuthEAPSupportAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPSupportAuthentication.setStatus(_A)
class _BrpsWLanCapabilityAuthEAPSupportEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BrpsWLanCapabilityAuthEAPSupportEncryption_Type.__name__=_B
_BrpsWLanCapabilityAuthEAPSupportEncryption_Object=MibTableColumn
brpsWLanCapabilityAuthEAPSupportEncryption=_BrpsWLanCapabilityAuthEAPSupportEncryption_Object((1,3,6,1,4,1,2435,2,4,3,100,1,1,8,1,6),_BrpsWLanCapabilityAuthEAPSupportEncryption_Type())
brpsWLanCapabilityAuthEAPSupportEncryption.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCapabilityAuthEAPSupportEncryption.setStatus(_A)
_WlGeneralInfo_ObjectIdentity=ObjectIdentity
wlGeneralInfo=_WlGeneralInfo_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,2))
_BrpsWLanDestination_Type=Integer32
_BrpsWLanDestination_Object=MibScalar
brpsWLanDestination=_BrpsWLanDestination_Object((1,3,6,1,4,1,2435,2,4,3,100,1,2,1),_BrpsWLanDestination_Type())
brpsWLanDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanDestination.setStatus(_A)
_BrpsWLanTransmitLevel_Type=Integer32
_BrpsWLanTransmitLevel_Object=MibScalar
brpsWLanTransmitLevel=_BrpsWLanTransmitLevel_Object((1,3,6,1,4,1,2435,2,4,3,100,1,2,2),_BrpsWLanTransmitLevel_Type())
brpsWLanTransmitLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanTransmitLevel.setStatus(_A)
_BrpsPit3WLanTestStatus_Type=Integer32
_BrpsPit3WLanTestStatus_Object=MibScalar
brpsPit3WLanTestStatus=_BrpsPit3WLanTestStatus_Object((1,3,6,1,4,1,2435,2,4,3,100,1,2,3),_BrpsPit3WLanTestStatus_Type())
brpsPit3WLanTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPit3WLanTestStatus.setStatus(_A)
_WlNetSearch_ObjectIdentity=ObjectIdentity
wlNetSearch=_WlNetSearch_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,11))
_BrpsWLanNetSearchSupported_Type=Integer32
_BrpsWLanNetSearchSupported_Object=MibScalar
brpsWLanNetSearchSupported=_BrpsWLanNetSearchSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,1),_BrpsWLanNetSearchSupported_Type())
brpsWLanNetSearchSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanNetSearchSupported.setStatus(_A)
_BrpsAvailableWLanScan_Type=OctetString
_BrpsAvailableWLanScan_Object=MibScalar
brpsAvailableWLanScan=_BrpsAvailableWLanScan_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,2),_BrpsAvailableWLanScan_Type())
brpsAvailableWLanScan.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAvailableWLanScan.setStatus(_A)
_BrpsAvailableWLanScanWaitTime_Type=Integer32
_BrpsAvailableWLanScanWaitTime_Object=MibScalar
brpsAvailableWLanScanWaitTime=_BrpsAvailableWLanScanWaitTime_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,3),_BrpsAvailableWLanScanWaitTime_Type())
brpsAvailableWLanScanWaitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanScanWaitTime.setStatus(_A)
_BrpsAvailableWLanCount_Type=Integer32
_BrpsAvailableWLanCount_Object=MibScalar
brpsAvailableWLanCount=_BrpsAvailableWLanCount_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,10),_BrpsAvailableWLanCount_Type())
brpsAvailableWLanCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanCount.setStatus(_A)
_BrpsAvailableWLanTable_Object=MibTable
brpsAvailableWLanTable=_BrpsAvailableWLanTable_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11))
if mibBuilder.loadTexts:brpsAvailableWLanTable.setStatus(_A)
_BrpsAvailableWLanEntry_Object=MibTableRow
brpsAvailableWLanEntry=_BrpsAvailableWLanEntry_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1))
brpsAvailableWLanEntry.setIndexNames((0,_E,_Ay))
if mibBuilder.loadTexts:brpsAvailableWLanEntry.setStatus(_A)
class _BrpsAvailableWLanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrpsAvailableWLanIndex_Type.__name__=_B
_BrpsAvailableWLanIndex_Object=MibTableColumn
brpsAvailableWLanIndex=_BrpsAvailableWLanIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,1),_BrpsAvailableWLanIndex_Type())
brpsAvailableWLanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanIndex.setStatus(_A)
class _BrpsAvailableWLanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsAvailableWLanName_Type.__name__=_G
_BrpsAvailableWLanName_Object=MibTableColumn
brpsAvailableWLanName=_BrpsAvailableWLanName_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,2),_BrpsAvailableWLanName_Type())
brpsAvailableWLanName.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanName.setStatus(_A)
class _BrpsAvailableWLanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Az,1),('dot11b',2),('dot11g',3)))
_BrpsAvailableWLanMode_Type.__name__=_B
_BrpsAvailableWLanMode_Object=MibTableColumn
brpsAvailableWLanMode=_BrpsAvailableWLanMode_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,3),_BrpsAvailableWLanMode_Type())
brpsAvailableWLanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanMode.setStatus(_A)
class _BrpsAvailableWLanCommMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accesPoint',1),('adhoc-Wi-Fi',2)))
_BrpsAvailableWLanCommMode_Type.__name__=_B
_BrpsAvailableWLanCommMode_Object=MibTableColumn
brpsAvailableWLanCommMode=_BrpsAvailableWLanCommMode_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,4),_BrpsAvailableWLanCommMode_Type())
brpsAvailableWLanCommMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanCommMode.setStatus(_A)
_BrpsAvailableWLanChannel_Type=Integer32
_BrpsAvailableWLanChannel_Object=MibTableColumn
brpsAvailableWLanChannel=_BrpsAvailableWLanChannel_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,5),_BrpsAvailableWLanChannel_Type())
brpsAvailableWLanChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanChannel.setStatus(_A)
_BrpsAvailableWLanPowerLevel_Type=Integer32
_BrpsAvailableWLanPowerLevel_Object=MibTableColumn
brpsAvailableWLanPowerLevel=_BrpsAvailableWLanPowerLevel_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,6),_BrpsAvailableWLanPowerLevel_Type())
brpsAvailableWLanPowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanPowerLevel.setStatus(_A)
class _BrpsAvailableWLanAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AA,1),('active',2)))
_BrpsAvailableWLanAuthMode_Type.__name__=_B
_BrpsAvailableWLanAuthMode_Object=MibTableColumn
brpsAvailableWLanAuthMode=_BrpsAvailableWLanAuthMode_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,7),_BrpsAvailableWLanAuthMode_Type())
brpsAvailableWLanAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanAuthMode.setStatus(_A)
class _BrpsAvailableWLanEncryptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),('active',2),('wep',3),('tkip',4)))
_BrpsAvailableWLanEncryptMode_Type.__name__=_B
_BrpsAvailableWLanEncryptMode_Object=MibTableColumn
brpsAvailableWLanEncryptMode=_BrpsAvailableWLanEncryptMode_Object((1,3,6,1,4,1,2435,2,4,3,100,1,11,11,1,8),_BrpsAvailableWLanEncryptMode_Type())
brpsAvailableWLanEncryptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAvailableWLanEncryptMode.setStatus(_A)
_WlAOSS_ObjectIdentity=ObjectIdentity
wlAOSS=_WlAOSS_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,12))
class _BrpsWLanAOSSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsWLanAOSSSupported_Type.__name__=_B
_BrpsWLanAOSSSupported_Object=MibScalar
brpsWLanAOSSSupported=_BrpsWLanAOSSSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,12,1),_BrpsWLanAOSSSupported_Type())
brpsWLanAOSSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAOSSSupported.setStatus(_A)
class _BrpsWLanAOSSIsRunnning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsWLanAOSSIsRunnning_Type.__name__=_B
_BrpsWLanAOSSIsRunnning_Object=MibScalar
brpsWLanAOSSIsRunnning=_BrpsWLanAOSSIsRunnning_Object((1,3,6,1,4,1,2435,2,4,3,100,1,12,2),_BrpsWLanAOSSIsRunnning_Type())
brpsWLanAOSSIsRunnning.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAOSSIsRunnning.setStatus(_A)
_WlSES_ObjectIdentity=ObjectIdentity
wlSES=_WlSES_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,13))
class _BrpsWLanSESSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsWLanSESSupported_Type.__name__=_B
_BrpsWLanSESSupported_Object=MibScalar
brpsWLanSESSupported=_BrpsWLanSESSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,13,1),_BrpsWLanSESSupported_Type())
brpsWLanSESSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanSESSupported.setStatus(_A)
_WlWPS_ObjectIdentity=ObjectIdentity
wlWPS=_WlWPS_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,14))
class _BrpsWLanWPSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsWLanWPSSupported_Type.__name__=_B
_BrpsWLanWPSSupported_Object=MibScalar
brpsWLanWPSSupported=_BrpsWLanWPSSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,14,1),_BrpsWLanWPSSupported_Type())
brpsWLanWPSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanWPSSupported.setStatus(_A)
class _BrpsWLanWPSResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_BrpsWLanWPSResult_Type.__name__=_B
_BrpsWLanWPSResult_Object=MibScalar
brpsWLanWPSResult=_BrpsWLanWPSResult_Object((1,3,6,1,4,1,2435,2,4,3,100,1,14,2),_BrpsWLanWPSResult_Type())
brpsWLanWPSResult.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanWPSResult.setStatus(_A)
_WlSimpleWizard_ObjectIdentity=ObjectIdentity
wlSimpleWizard=_WlSimpleWizard_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,1,15))
class _BrWlanSimpleWizardSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrWlanSimpleWizardSupported_Type.__name__=_B
_BrWlanSimpleWizardSupported_Object=MibScalar
brWlanSimpleWizardSupported=_BrWlanSimpleWizardSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,1,15,1),_BrWlanSimpleWizardSupported_Type())
brWlanSimpleWizardSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brWlanSimpleWizardSupported.setStatus(_A)
class _BrWlanSimpleWizardPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrWlanSimpleWizardPassword_Type.__name__=_G
_BrWlanSimpleWizardPassword_Object=MibScalar
brWlanSimpleWizardPassword=_BrWlanSimpleWizardPassword_Object((1,3,6,1,4,1,2435,2,4,3,100,1,15,2),_BrWlanSimpleWizardPassword_Type())
brWlanSimpleWizardPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brWlanSimpleWizardPassword.setStatus(_A)
_WlSetup_ObjectIdentity=ObjectIdentity
wlSetup=_WlSetup_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11))
_WlGeneral_ObjectIdentity=ObjectIdentity
wlGeneral=_WlGeneral_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,1))
class _BrpsWLanAPSetupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_BrpsWLanAPSetupMode_Type.__name__=_B
_BrpsWLanAPSetupMode_Object=MibScalar
brpsWLanAPSetupMode=_BrpsWLanAPSetupMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,1,1),_BrpsWLanAPSetupMode_Type())
brpsWLanAPSetupMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAPSetupMode.setStatus(_A)
class _BrpsWLanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Az,1),('dot11b',2),('dot11g',3),('dot11g-turbo',4)))
_BrpsWLanMode_Type.__name__=_B
_BrpsWLanMode_Object=MibScalar
brpsWLanMode=_BrpsWLanMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,1,2),_BrpsWLanMode_Type())
brpsWLanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanMode.setStatus(_A)
class _BrpsWLanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsWLanName_Type.__name__=_G
_BrpsWLanName_Object=MibScalar
brpsWLanName=_BrpsWLanName_Object((1,3,6,1,4,1,2435,2,4,3,100,11,1,3),_BrpsWLanName_Type())
brpsWLanName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanName.setStatus(_A)
class _BrpsWLanCommMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infrastructure',1),('ad-Hoc-WiFi',2),('ad-Hoc',3)))
_BrpsWLanCommMode_Type.__name__=_B
_BrpsWLanCommMode_Object=MibScalar
brpsWLanCommMode=_BrpsWLanCommMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,1,4),_BrpsWLanCommMode_Type())
brpsWLanCommMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanCommMode.setStatus(_A)
_BrpsWLanChannel_Type=Integer32
_BrpsWLanChannel_Object=MibScalar
brpsWLanChannel=_BrpsWLanChannel_Object((1,3,6,1,4,1,2435,2,4,3,100,11,1,5),_BrpsWLanChannel_Type())
brpsWLanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanChannel.setStatus(_A)
_WlAdvanced_ObjectIdentity=ObjectIdentity
wlAdvanced=_WlAdvanced_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,5))
class _BrpsWLanCtsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_w,1),('always',2),(_AA,3)))
_BrpsWLanCtsMode_Type.__name__=_B
_BrpsWLanCtsMode_Object=MibScalar
brpsWLanCtsMode=_BrpsWLanCtsMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,1),_BrpsWLanCtsMode_Type())
brpsWLanCtsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanCtsMode.setStatus(_A)
class _BrpsWLanCtsRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsWLanCtsRate_Type.__name__=_B
_BrpsWLanCtsRate_Object=MibScalar
brpsWLanCtsRate=_BrpsWLanCtsRate_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,2),_BrpsWLanCtsRate_Type())
brpsWLanCtsRate.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanCtsRate.setStatus(_A)
class _BrpsWLanCtsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('only',1),('rts-cts',2)))
_BrpsWLanCtsType_Type.__name__=_B
_BrpsWLanCtsType_Object=MibScalar
brpsWLanCtsType=_BrpsWLanCtsType_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,3),_BrpsWLanCtsType_Type())
brpsWLanCtsType.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanCtsType.setStatus(_A)
class _BrpsWLanRtsCtsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_BrpsWLanRtsCtsThreshold_Type.__name__=_B
_BrpsWLanRtsCtsThreshold_Object=MibScalar
brpsWLanRtsCtsThreshold=_BrpsWLanRtsCtsThreshold_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,4),_BrpsWLanRtsCtsThreshold_Type())
brpsWLanRtsCtsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanRtsCtsThreshold.setStatus(_A)
class _BrpsWLanLengthThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_BrpsWLanLengthThreshold_Type.__name__=_B
_BrpsWLanLengthThreshold_Object=MibScalar
brpsWLanLengthThreshold=_BrpsWLanLengthThreshold_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,5),_BrpsWLanLengthThreshold_Type())
brpsWLanLengthThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanLengthThreshold.setStatus(_A)
class _BrpsWLanDataRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BrpsWLanDataRetry_Type.__name__=_B
_BrpsWLanDataRetry_Object=MibScalar
brpsWLanDataRetry=_BrpsWLanDataRetry_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,6),_BrpsWLanDataRetry_Type())
brpsWLanDataRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanDataRetry.setStatus(_A)
class _BrpsWLanTransmitPowerSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('full',1),('half',2),('quarter',3),('one-eighth',4),('minimum',5),(_H,6)))
_BrpsWLanTransmitPowerSetting_Type.__name__=_B
_BrpsWLanTransmitPowerSetting_Object=MibScalar
brpsWLanTransmitPowerSetting=_BrpsWLanTransmitPowerSetting_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,7),_BrpsWLanTransmitPowerSetting_Type())
brpsWLanTransmitPowerSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanTransmitPowerSetting.setStatus(_A)
class _BrpsWLanDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stationMode',1),('accessPointMode',2)))
_BrpsWLanDeviceType_Type.__name__=_B
_BrpsWLanDeviceType_Object=MibScalar
brpsWLanDeviceType=_BrpsWLanDeviceType_Object((1,3,6,1,4,1,2435,2,4,3,100,11,5,8),_BrpsWLanDeviceType_Type())
brpsWLanDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanDeviceType.setStatus(_A)
_WlAssociate_ObjectIdentity=ObjectIdentity
wlAssociate=_WlAssociate_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,11))
class _BrpsWLanEncryptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),('wep',2),('tkip',3),('aes',4)))
_BrpsWLanEncryptMode_Type.__name__=_B
_BrpsWLanEncryptMode_Object=MibScalar
brpsWLanEncryptMode=_BrpsWLanEncryptMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,1),_BrpsWLanEncryptMode_Type())
brpsWLanEncryptMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanEncryptMode.setStatus(_A)
class _BrpsWLanAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2),('wpa-psk',3),('wpa-none',4),('wpa',5),('wpa2',6),(_AC,7),(_AD,8),(_AE,9),(_AF,10),(_AG,11),('wpa2-psk',12)))
_BrpsWLanAuthMode_Type.__name__=_B
_BrpsWLanAuthMode_Object=MibScalar
brpsWLanAuthMode=_BrpsWLanAuthMode_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,11),_BrpsWLanAuthMode_Type())
brpsWLanAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanAuthMode.setStatus(_A)
class _BrpsWLanAuthEAP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('eapMD5',1),('eapTLS',2),('eapTTLS',3),('peap',4),(_AC,5),(_AD,6),(_AE,7),(_AF,8),(_AG,9)))
_BrpsWLanAuthEAP_Type.__name__=_B
_BrpsWLanAuthEAP_Object=MibScalar
brpsWLanAuthEAP=_BrpsWLanAuthEAP_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,12),_BrpsWLanAuthEAP_Type())
brpsWLanAuthEAP.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanAuthEAP.setStatus(_A)
class _BrpsWLanAuthUserID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsWLanAuthUserID_Type.__name__=_G
_BrpsWLanAuthUserID_Object=MibScalar
brpsWLanAuthUserID=_BrpsWLanAuthUserID_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,13),_BrpsWLanAuthUserID_Type())
brpsWLanAuthUserID.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanAuthUserID.setStatus(_A)
class _BrpsWLanAuthUserPass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsWLanAuthUserPass_Type.__name__=_G
_BrpsWLanAuthUserPass_Object=MibScalar
brpsWLanAuthUserPass=_BrpsWLanAuthUserPass_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,14),_BrpsWLanAuthUserPass_Type())
brpsWLanAuthUserPass.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanAuthUserPass.setStatus(_A)
class _BrpsWLanAssociate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('update',1),(_AI,2),('test',3),('applyonly',4),('simplewizard',5)))
_BrpsWLanAssociate_Type.__name__=_B
_BrpsWLanAssociate_Object=MibScalar
brpsWLanAssociate=_BrpsWLanAssociate_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,21),_BrpsWLanAssociate_Type())
brpsWLanAssociate.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanAssociate.setStatus(_A)
class _BrpsWLanAssociateTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('linkOK',1),(_A_,2),(_B0,3),(_B1,4),(_B2,5)))
_BrpsWLanAssociateTestResult_Type.__name__=_B
_BrpsWLanAssociateTestResult_Object=MibScalar
brpsWLanAssociateTestResult=_BrpsWLanAssociateTestResult_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,22),_BrpsWLanAssociateTestResult_Type())
brpsWLanAssociateTestResult.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAssociateTestResult.setStatus(_A)
class _BrpsWLanAssociateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('linkOK',1),(_A_,2),(_B0,3),(_B1,4),(_B2,5)))
_BrpsWLanAssociateResult_Type.__name__=_B
_BrpsWLanAssociateResult_Object=MibScalar
brpsWLanAssociateResult=_BrpsWLanAssociateResult_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,23),_BrpsWLanAssociateResult_Type())
brpsWLanAssociateResult.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAssociateResult.setStatus(_A)
_BrpsWLanAssociateTestSupported_Type=Integer32
_BrpsWLanAssociateTestSupported_Object=MibScalar
brpsWLanAssociateTestSupported=_BrpsWLanAssociateTestSupported_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,24),_BrpsWLanAssociateTestSupported_Type())
brpsWLanAssociateTestSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanAssociateTestSupported.setStatus(_A)
_WlWEP_ObjectIdentity=ObjectIdentity
wlWEP=_WlWEP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,11,101))
_BrpsWLanWepKeyDefaultIndex_Type=Integer32
_BrpsWLanWepKeyDefaultIndex_Object=MibScalar
brpsWLanWepKeyDefaultIndex=_BrpsWLanWepKeyDefaultIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,1),_BrpsWLanWepKeyDefaultIndex_Type())
brpsWLanWepKeyDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanWepKeyDefaultIndex.setStatus(_A)
_BrpsWLanWepKeyTable_Object=MibTable
brpsWLanWepKeyTable=_BrpsWLanWepKeyTable_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11))
if mibBuilder.loadTexts:brpsWLanWepKeyTable.setStatus(_A)
_BrpsWLanWepKeyEntry_Object=MibTableRow
brpsWLanWepKeyEntry=_BrpsWLanWepKeyEntry_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11,1))
brpsWLanWepKeyEntry.setIndexNames((0,_E,_B3))
if mibBuilder.loadTexts:brpsWLanWepKeyEntry.setStatus(_A)
class _BrpsWLanWepKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrpsWLanWepKeyIndex_Type.__name__=_B
_BrpsWLanWepKeyIndex_Object=MibTableColumn
brpsWLanWepKeyIndex=_BrpsWLanWepKeyIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11,1,1),_BrpsWLanWepKeyIndex_Type())
brpsWLanWepKeyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanWepKeyIndex.setStatus(_A)
class _BrpsWLanWepKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('size40',1),('size104',2)))
_BrpsWLanWepKeySize_Type.__name__=_B
_BrpsWLanWepKeySize_Object=MibTableColumn
brpsWLanWepKeySize=_BrpsWLanWepKeySize_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11,1,2),_BrpsWLanWepKeySize_Type())
brpsWLanWepKeySize.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanWepKeySize.setStatus(_A)
class _BrpsWLanWepKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex',1),('ascii',2)))
_BrpsWLanWepKeyType_Type.__name__=_B
_BrpsWLanWepKeyType_Object=MibTableColumn
brpsWLanWepKeyType=_BrpsWLanWepKeyType_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11,1,3),_BrpsWLanWepKeyType_Type())
brpsWLanWepKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanWepKeyType.setStatus(_A)
_BrpsWLanWepKey_Type=OctetString
_BrpsWLanWepKey_Object=MibTableColumn
brpsWLanWepKey=_BrpsWLanWepKey_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,101,11,1,4),_BrpsWLanWepKey_Type())
brpsWLanWepKey.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanWepKey.setStatus(_A)
_WlWPA_ObjectIdentity=ObjectIdentity
wlWPA=_WlWPA_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,11,102))
_BrpsWLanNetworkKey_Type=OctetString
_BrpsWLanNetworkKey_Object=MibScalar
brpsWLanNetworkKey=_BrpsWLanNetworkKey_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,102,1),_BrpsWLanNetworkKey_Type())
brpsWLanNetworkKey.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanNetworkKey.setStatus(_A)
_WlTKIP_ObjectIdentity=ObjectIdentity
wlTKIP=_WlTKIP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,11,103))
_BrpsWLanTKIPChangeInterval_Type=Integer32
_BrpsWLanTKIPChangeInterval_Object=MibScalar
brpsWLanTKIPChangeInterval=_BrpsWLanTKIPChangeInterval_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,103,1),_BrpsWLanTKIPChangeInterval_Type())
brpsWLanTKIPChangeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanTKIPChangeInterval.setStatus(_A)
_WlLEAP_ObjectIdentity=ObjectIdentity
wlLEAP=_WlLEAP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,11,11,104))
_BrpsWLanLEAPTimeout_Type=Integer32
_BrpsWLanLEAPTimeout_Object=MibScalar
brpsWLanLEAPTimeout=_BrpsWLanLEAPTimeout_Object((1,3,6,1,4,1,2435,2,4,3,100,11,11,104,1),_BrpsWLanLEAPTimeout_Type())
brpsWLanLEAPTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsWLanLEAPTimeout.setStatus(_A)
_WlStatus_ObjectIdentity=ObjectIdentity
wlStatus=_WlStatus_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,21))
_WlGeneralStatus_ObjectIdentity=ObjectIdentity
wlGeneralStatus=_WlGeneralStatus_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,100,21,1))
_BrpsWLanOperatingMode_Type=Integer32
_BrpsWLanOperatingMode_Object=MibScalar
brpsWLanOperatingMode=_BrpsWLanOperatingMode_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,1),_BrpsWLanOperatingMode_Type())
brpsWLanOperatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingMode.setStatus(_A)
class _BrpsWLanRSSLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrpsWLanRSSLevel_Type.__name__=_B
_BrpsWLanRSSLevel_Object=MibScalar
brpsWLanRSSLevel=_BrpsWLanRSSLevel_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,2),_BrpsWLanRSSLevel_Type())
brpsWLanRSSLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanRSSLevel.setStatus(_A)
class _BrpsWLanCommSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsWLanCommSpeed_Type.__name__=_B
_BrpsWLanCommSpeed_Object=MibScalar
brpsWLanCommSpeed=_BrpsWLanCommSpeed_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,3),_BrpsWLanCommSpeed_Type())
brpsWLanCommSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanCommSpeed.setStatus(_A)
_BrpsWLanOperatingChannel_Type=Integer32
_BrpsWLanOperatingChannel_Object=MibScalar
brpsWLanOperatingChannel=_BrpsWLanOperatingChannel_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,4),_BrpsWLanOperatingChannel_Type())
brpsWLanOperatingChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingChannel.setStatus(_A)
_BrpsWLanOperatingName_Type=OctetString
_BrpsWLanOperatingName_Object=MibScalar
brpsWLanOperatingName=_BrpsWLanOperatingName_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,5),_BrpsWLanOperatingName_Type())
brpsWLanOperatingName.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingName.setStatus(_A)
_BrpsWLanOperatingCommMode_Type=Integer32
_BrpsWLanOperatingCommMode_Object=MibScalar
brpsWLanOperatingCommMode=_BrpsWLanOperatingCommMode_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,6),_BrpsWLanOperatingCommMode_Type())
brpsWLanOperatingCommMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingCommMode.setStatus(_A)
_BrpsWLanOperatingEncryptMode_Type=Integer32
_BrpsWLanOperatingEncryptMode_Object=MibScalar
brpsWLanOperatingEncryptMode=_BrpsWLanOperatingEncryptMode_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,7),_BrpsWLanOperatingEncryptMode_Type())
brpsWLanOperatingEncryptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingEncryptMode.setStatus(_A)
_BrpsWLanOperatingAuthMode_Type=Integer32
_BrpsWLanOperatingAuthMode_Object=MibScalar
brpsWLanOperatingAuthMode=_BrpsWLanOperatingAuthMode_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,8),_BrpsWLanOperatingAuthMode_Type())
brpsWLanOperatingAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingAuthMode.setStatus(_A)
_BrpsWLanOperatingWepKeyDefaultIndex_Type=Integer32
_BrpsWLanOperatingWepKeyDefaultIndex_Object=MibScalar
brpsWLanOperatingWepKeyDefaultIndex=_BrpsWLanOperatingWepKeyDefaultIndex_Object((1,3,6,1,4,1,2435,2,4,3,100,21,1,9),_BrpsWLanOperatingWepKeyDefaultIndex_Type())
brpsWLanOperatingWepKeyDefaultIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsWLanOperatingWepKeyDefaultIndex.setStatus(_A)
_BrnetConfig_ObjectIdentity=ObjectIdentity
brnetConfig=_BrnetConfig_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240))
_Brconfig_ObjectIdentity=ObjectIdentity
brconfig=_Brconfig_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,1))
class _BrpsNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsNodeName_Type.__name__=_F
_BrpsNodeName_Object=MibScalar
brpsNodeName=_BrpsNodeName_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,1),_BrpsNodeName_Type())
brpsNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNodeName.setStatus(_A)
class _BrpsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsSerialNumber_Type.__name__=_F
_BrpsSerialNumber_Object=MibScalar
brpsSerialNumber=_BrpsSerialNumber_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,2),_BrpsSerialNumber_Type())
brpsSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSerialNumber.setStatus(_A)
class _BrpsHardwareType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsHardwareType_Type.__name__=_B
_BrpsHardwareType_Object=MibScalar
brpsHardwareType=_BrpsHardwareType_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,3),_BrpsHardwareType_Type())
brpsHardwareType.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsHardwareType.setStatus(_A)
class _BrpsMainRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BrpsMainRevision_Type.__name__=_F
_BrpsMainRevision_Object=MibScalar
brpsMainRevision=_BrpsMainRevision_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,4),_BrpsMainRevision_Type())
brpsMainRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsMainRevision.setStatus(_A)
class _BrpsBootRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BrpsBootRevision_Type.__name__=_F
_BrpsBootRevision_Object=MibScalar
brpsBootRevision=_BrpsBootRevision_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,5),_BrpsBootRevision_Type())
brpsBootRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBootRevision.setStatus(_A)
_BrpsPasswordVerify_Type=DisplayString
_BrpsPasswordVerify_Object=MibScalar
brpsPasswordVerify=_BrpsPasswordVerify_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,6),_BrpsPasswordVerify_Type())
brpsPasswordVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPasswordVerify.setStatus(_A)
_BrpsPassword_Type=DisplayString
_BrpsPassword_Object=MibScalar
brpsPassword=_BrpsPassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,7),_BrpsPassword_Type())
brpsPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPassword.setStatus(_A)
class _BrpsMIBVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_BrpsMIBVersion_Type.__name__=_F
_BrpsMIBVersion_Object=MibScalar
brpsMIBVersion=_BrpsMIBVersion_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,8),_BrpsMIBVersion_Type())
brpsMIBVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsMIBVersion.setStatus(_A)
class _BrpsOEMString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_BrpsOEMString_Type.__name__=_F
_BrpsOEMString_Object=MibScalar
brpsOEMString=_BrpsOEMString_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,9),_BrpsOEMString_Type())
brpsOEMString.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsOEMString.setStatus(_A)
class _BrpsMIBMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_BrpsMIBMajor_Type.__name__=_B
_BrpsMIBMajor_Object=MibScalar
brpsMIBMajor=_BrpsMIBMajor_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,10),_BrpsMIBMajor_Type())
brpsMIBMajor.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsMIBMajor.setStatus(_A)
class _BrpsMIBMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_BrpsMIBMinor_Type.__name__=_B
_BrpsMIBMinor_Object=MibScalar
brpsMIBMinor=_BrpsMIBMinor_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,11),_BrpsMIBMinor_Type())
brpsMIBMinor.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsMIBMinor.setStatus(_A)
class _BrpsServerDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsServerDescription_Type.__name__=_F
_BrpsServerDescription_Object=MibScalar
brpsServerDescription=_BrpsServerDescription_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,12),_BrpsServerDescription_Type())
brpsServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServerDescription.setStatus(_A)
class _BrpsEnetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrpsEnetMode_Type.__name__=_B
_BrpsEnetMode_Object=MibScalar
brpsEnetMode=_BrpsEnetMode_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,13),_BrpsEnetMode_Type())
brpsEnetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEnetMode.setStatus(_A)
class _BrpsFlashROMSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsFlashROMSize_Type.__name__=_B
_BrpsFlashROMSize_Object=MibScalar
brpsFlashROMSize=_BrpsFlashROMSize_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,14),_BrpsFlashROMSize_Type())
brpsFlashROMSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsFlashROMSize.setStatus(_A)
class _BrpsSNMPGetCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsSNMPGetCommunity_Type.__name__=_F
_BrpsSNMPGetCommunity_Object=MibScalar
brpsSNMPGetCommunity=_BrpsSNMPGetCommunity_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,15),_BrpsSNMPGetCommunity_Type())
brpsSNMPGetCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSNMPGetCommunity.setStatus(_A)
class _BrpsSNMPJetAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsSNMPJetAdmin_Type.__name__=_B
_BrpsSNMPJetAdmin_Object=MibScalar
brpsSNMPJetAdmin=_BrpsSNMPJetAdmin_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,16),_BrpsSNMPJetAdmin_Type())
brpsSNMPJetAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSNMPJetAdmin.setStatus(_A)
class _BrpsSNMPSetCommunity1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsSNMPSetCommunity1_Type.__name__=_F
_BrpsSNMPSetCommunity1_Object=MibScalar
brpsSNMPSetCommunity1=_BrpsSNMPSetCommunity1_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,17),_BrpsSNMPSetCommunity1_Type())
brpsSNMPSetCommunity1.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSNMPSetCommunity1.setStatus(_A)
class _BrpsSNMPSetCommunity2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsSNMPSetCommunity2_Type.__name__=_F
_BrpsSNMPSetCommunity2_Object=MibScalar
brpsSNMPSetCommunity2=_BrpsSNMPSetCommunity2_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,18),_BrpsSNMPSetCommunity2_Type())
brpsSNMPSetCommunity2.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSNMPSetCommunity2.setStatus(_A)
class _BrSupportedInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrSupportedInfo_Type.__name__=_G
_BrSupportedInfo_Object=MibScalar
brSupportedInfo=_BrSupportedInfo_Object((1,3,6,1,4,1,2435,2,4,3,1240,1,200),_BrSupportedInfo_Type())
brSupportedInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:brSupportedInfo.setStatus(_A)
_Brcontrol_ObjectIdentity=ObjectIdentity
brcontrol=_Brcontrol_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,2))
class _BrpsTestPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsTestPage_Type.__name__=_B
_BrpsTestPage_Object=MibScalar
brpsTestPage=_BrpsTestPage_Object((1,3,6,1,4,1,2435,2,4,3,1240,2,1),_BrpsTestPage_Type())
brpsTestPage.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTestPage.setStatus(_A)
class _BrpsSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsSetDefault_Type.__name__=_B
_BrpsSetDefault_Object=MibScalar
brpsSetDefault=_BrpsSetDefault_Object((1,3,6,1,4,1,2435,2,4,3,1240,2,2),_BrpsSetDefault_Type())
brpsSetDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSetDefault.setStatus(_A)
class _BrpsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsReset_Type.__name__=_B
_BrpsReset_Object=MibScalar
brpsReset=_BrpsReset_Object((1,3,6,1,4,1,2435,2,4,3,1240,2,3),_BrpsReset_Type())
brpsReset.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsReset.setStatus(_A)
class _BrpsProtectModeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsProtectModeEnable_Type.__name__=_B
_BrpsProtectModeEnable_Object=MibScalar
brpsProtectModeEnable=_BrpsProtectModeEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,2,4),_BrpsProtectModeEnable_Type())
brpsProtectModeEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsProtectModeEnable.setStatus(_A)
class _BrpsProtectPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsProtectPassword_Type.__name__=_F
_BrpsProtectPassword_Object=MibScalar
brpsProtectPassword=_BrpsProtectPassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,2,5),_BrpsProtectPassword_Type())
brpsProtectPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsProtectPassword.setStatus(_A)
_Brport_ObjectIdentity=ObjectIdentity
brport=_Brport_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,3))
class _BrpsPortCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_BrpsPortCount_Type.__name__=_B
_BrpsPortCount_Object=MibScalar
brpsPortCount=_BrpsPortCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,1),_BrpsPortCount_Type())
brpsPortCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortCount.setStatus(_A)
_BrpsPortInfoTable_Object=MibTable
brpsPortInfoTable=_BrpsPortInfoTable_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2))
if mibBuilder.loadTexts:brpsPortInfoTable.setStatus(_A)
_BrpsPortInfoEntry_Object=MibTableRow
brpsPortInfoEntry=_BrpsPortInfoEntry_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1))
brpsPortInfoEntry.setIndexNames((0,_E,_B4))
if mibBuilder.loadTexts:brpsPortInfoEntry.setStatus(_A)
class _BrpsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrpsPortIndex_Type.__name__=_B
_BrpsPortIndex_Object=MibTableColumn
brpsPortIndex=_BrpsPortIndex_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,1),_BrpsPortIndex_Type())
brpsPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortIndex.setStatus(_A)
class _BrpsPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsPortName_Type.__name__=_F
_BrpsPortName_Object=MibTableColumn
brpsPortName=_BrpsPortName_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,2),_BrpsPortName_Type())
brpsPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPortName.setStatus(_A)
class _BrpsPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('parallel',1),('serial',2)))
_BrpsPortType_Type.__name__=_B
_BrpsPortType_Object=MibTableColumn
brpsPortType=_BrpsPortType_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,3),_BrpsPortType_Type())
brpsPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortType.setStatus(_A)
class _BrpsPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BrpsPortStatus_Type.__name__=_B
_BrpsPortStatus_Object=MibTableColumn
brpsPortStatus=_BrpsPortStatus_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,4),_BrpsPortStatus_Type())
brpsPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortStatus.setStatus(_A)
class _BrpsPortStatusString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsPortStatusString_Type.__name__=_F
_BrpsPortStatusString_Object=MibTableColumn
brpsPortStatusString=_BrpsPortStatusString_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,5),_BrpsPortStatusString_Type())
brpsPortStatusString.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortStatusString.setStatus(_A)
class _BrpsPortProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_BrpsPortProtocol_Type.__name__=_B
_BrpsPortProtocol_Object=MibTableColumn
brpsPortProtocol=_BrpsPortProtocol_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,6),_BrpsPortProtocol_Type())
brpsPortProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortProtocol.setStatus(_A)
_BrpsPortQueueSize_Type=Integer32
_BrpsPortQueueSize_Object=MibTableColumn
brpsPortQueueSize=_BrpsPortQueueSize_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,7),_BrpsPortQueueSize_Type())
brpsPortQueueSize.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortQueueSize.setStatus(_A)
class _BrpsPortDescriptionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_BrpsPortDescriptionString_Type.__name__=_F
_BrpsPortDescriptionString_Object=MibTableColumn
brpsPortDescriptionString=_BrpsPortDescriptionString_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,8),_BrpsPortDescriptionString_Type())
brpsPortDescriptionString.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortDescriptionString.setStatus(_A)
class _BrpsPortInfoString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_BrpsPortInfoString_Type.__name__=_F
_BrpsPortInfoString_Object=MibTableColumn
brpsPortInfoString=_BrpsPortInfoString_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,9),_BrpsPortInfoString_Type())
brpsPortInfoString.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortInfoString.setStatus(_A)
class _BrpsPortHTTPExtensions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsPortHTTPExtensions_Type.__name__=_B
_BrpsPortHTTPExtensions_Object=MibTableColumn
brpsPortHTTPExtensions=_BrpsPortHTTPExtensions_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,10),_BrpsPortHTTPExtensions_Type())
brpsPortHTTPExtensions.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortHTTPExtensions.setStatus(_A)
class _BrpsPortSNMPExtensions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsPortSNMPExtensions_Type.__name__=_B
_BrpsPortSNMPExtensions_Object=MibTableColumn
brpsPortSNMPExtensions=_BrpsPortSNMPExtensions_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,11),_BrpsPortSNMPExtensions_Type())
brpsPortSNMPExtensions.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPortSNMPExtensions.setStatus(_A)
class _BrpsPortAttribute_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsPortAttribute_Type.__name__=_F
_BrpsPortAttribute_Object=MibTableColumn
brpsPortAttribute=_BrpsPortAttribute_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,12),_BrpsPortAttribute_Type())
brpsPortAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPortAttribute.setStatus(_A)
class _BrpsPortBinaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrpsPortBinaryMode_Type.__name__=_B
_BrpsPortBinaryMode_Object=MibTableColumn
brpsPortBinaryMode=_BrpsPortBinaryMode_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,13),_BrpsPortBinaryMode_Type())
brpsPortBinaryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPortBinaryMode.setStatus(_A)
class _BrpsPortInhibitDatagramSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsPortInhibitDatagramSupport_Type.__name__=_B
_BrpsPortInhibitDatagramSupport_Object=MibTableColumn
brpsPortInhibitDatagramSupport=_BrpsPortInhibitDatagramSupport_Object((1,3,6,1,4,1,2435,2,4,3,1240,3,2,1,14),_BrpsPortInhibitDatagramSupport_Type())
brpsPortInhibitDatagramSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPortInhibitDatagramSupport.setStatus(_A)
_Brservice_ObjectIdentity=ObjectIdentity
brservice=_Brservice_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,4))
class _BrpsServiceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_BrpsServiceCount_Type.__name__=_B
_BrpsServiceCount_Object=MibScalar
brpsServiceCount=_BrpsServiceCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,1),_BrpsServiceCount_Type())
brpsServiceCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceCount.setStatus(_A)
_BrpsServiceInfoTable_Object=MibTable
brpsServiceInfoTable=_BrpsServiceInfoTable_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2))
if mibBuilder.loadTexts:brpsServiceInfoTable.setStatus(_A)
_BrpsServiceInfoEntry_Object=MibTableRow
brpsServiceInfoEntry=_BrpsServiceInfoEntry_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1))
brpsServiceInfoEntry.setIndexNames((0,_E,_AL))
if mibBuilder.loadTexts:brpsServiceInfoEntry.setStatus(_A)
class _BrpsServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BrpsServiceIndex_Type.__name__=_B
_BrpsServiceIndex_Object=MibTableColumn
brpsServiceIndex=_BrpsServiceIndex_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,1),_BrpsServiceIndex_Type())
brpsServiceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceIndex.setStatus(_A)
class _BrpsServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsServiceName_Type.__name__=_F
_BrpsServiceName_Object=MibTableColumn
brpsServiceName=_BrpsServiceName_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,2),_BrpsServiceName_Type())
brpsServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceName.setStatus(_A)
class _BrpsServicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BrpsServicePort_Type.__name__=_B
_BrpsServicePort_Object=MibTableColumn
brpsServicePort=_BrpsServicePort_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,3),_BrpsServicePort_Type())
brpsServicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServicePort.setStatus(_A)
class _BrpsServiceFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceFilter_Type.__name__=_B
_BrpsServiceFilter_Object=MibTableColumn
brpsServiceFilter=_BrpsServiceFilter_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,4),_BrpsServiceFilter_Type())
brpsServiceFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceFilter.setStatus(_A)
class _BrpsServiceBOT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceBOT_Type.__name__=_B
_BrpsServiceBOT_Object=MibTableColumn
brpsServiceBOT=_BrpsServiceBOT_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,5),_BrpsServiceBOT_Type())
brpsServiceBOT.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceBOT.setStatus(_A)
class _BrpsServiceEOT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceEOT_Type.__name__=_B
_BrpsServiceEOT_Object=MibTableColumn
brpsServiceEOT=_BrpsServiceEOT_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,6),_BrpsServiceEOT_Type())
brpsServiceEOT.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceEOT.setStatus(_A)
class _BrpsServiceMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceMatch_Type.__name__=_B
_BrpsServiceMatch_Object=MibTableColumn
brpsServiceMatch=_BrpsServiceMatch_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,7),_BrpsServiceMatch_Type())
brpsServiceMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceMatch.setStatus(_A)
class _BrpsServiceReplace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceReplace_Type.__name__=_B
_BrpsServiceReplace_Object=MibTableColumn
brpsServiceReplace=_BrpsServiceReplace_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,8),_BrpsServiceReplace_Type())
brpsServiceReplace.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceReplace.setStatus(_A)
class _BrpsServiceTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsServiceTCPPort_Type.__name__=_B
_BrpsServiceTCPPort_Object=MibTableColumn
brpsServiceTCPPort=_BrpsServiceTCPPort_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,9),_BrpsServiceTCPPort_Type())
brpsServiceTCPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceTCPPort.setStatus(_A)
class _BrpsServiceNDSTree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrpsServiceNDSTree_Type.__name__=_F
_BrpsServiceNDSTree_Object=MibTableColumn
brpsServiceNDSTree=_BrpsServiceNDSTree_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,10),_BrpsServiceNDSTree_Type())
brpsServiceNDSTree.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceNDSTree.setStatus(_A)
class _BrpsServiceNDSContext_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsServiceNDSContext_Type.__name__=_G
_BrpsServiceNDSContext_Object=MibTableColumn
brpsServiceNDSContext=_BrpsServiceNDSContext_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,11),_BrpsServiceNDSContext_Type())
brpsServiceNDSContext.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceNDSContext.setStatus(_A)
class _BrpsServiceVines_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrpsServiceVines_Type.__name__=_F
_BrpsServiceVines_Object=MibTableColumn
brpsServiceVines=_BrpsServiceVines_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,12),_BrpsServiceVines_Type())
brpsServiceVines.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceVines.setStatus(_A)
class _BrpsServiceObsolete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_BrpsServiceObsolete_Type.__name__=_B
_BrpsServiceObsolete_Object=MibTableColumn
brpsServiceObsolete=_BrpsServiceObsolete_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,13),_BrpsServiceObsolete_Type())
brpsServiceObsolete.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceObsolete.setStatus(_A)
class _BrpsServiceNetwareServerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_BrpsServiceNetwareServerCount_Type.__name__=_B
_BrpsServiceNetwareServerCount_Object=MibTableColumn
brpsServiceNetwareServerCount=_BrpsServiceNetwareServerCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,14),_BrpsServiceNetwareServerCount_Type())
brpsServiceNetwareServerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceNetwareServerCount.setStatus(_A)
class _BrpsServiceReceiveOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceReceiveOnly_Type.__name__=_B
_BrpsServiceReceiveOnly_Object=MibTableColumn
brpsServiceReceiveOnly=_BrpsServiceReceiveOnly_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,15),_BrpsServiceReceiveOnly_Type())
brpsServiceReceiveOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceReceiveOnly.setStatus(_A)
class _BrpsServiceTCPQueued_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceTCPQueued_Type.__name__=_B
_BrpsServiceTCPQueued_Object=MibTableColumn
brpsServiceTCPQueued=_BrpsServiceTCPQueued_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,16),_BrpsServiceTCPQueued_Type())
brpsServiceTCPQueued.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceTCPQueued.setStatus(_A)
class _BrpsServiceProtocolLAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolLAT_Type.__name__=_B
_BrpsServiceProtocolLAT_Object=MibTableColumn
brpsServiceProtocolLAT=_BrpsServiceProtocolLAT_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,17),_BrpsServiceProtocolLAT_Type())
brpsServiceProtocolLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolLAT.setStatus(_A)
class _BrpsServiceProtocolTCPIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolTCPIP_Type.__name__=_B
_BrpsServiceProtocolTCPIP_Object=MibTableColumn
brpsServiceProtocolTCPIP=_BrpsServiceProtocolTCPIP_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,18),_BrpsServiceProtocolTCPIP_Type())
brpsServiceProtocolTCPIP.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolTCPIP.setStatus(_A)
class _BrpsServiceProtocolNetware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolNetware_Type.__name__=_B
_BrpsServiceProtocolNetware_Object=MibTableColumn
brpsServiceProtocolNetware=_BrpsServiceProtocolNetware_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,19),_BrpsServiceProtocolNetware_Type())
brpsServiceProtocolNetware.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolNetware.setStatus(_A)
class _BrpsServiceProtocolAppleTalk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolAppleTalk_Type.__name__=_B
_BrpsServiceProtocolAppleTalk_Object=MibTableColumn
brpsServiceProtocolAppleTalk=_BrpsServiceProtocolAppleTalk_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,20),_BrpsServiceProtocolAppleTalk_Type())
brpsServiceProtocolAppleTalk.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolAppleTalk.setStatus(_A)
class _BrpsServiceProtocolBanyan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolBanyan_Type.__name__=_B
_BrpsServiceProtocolBanyan_Object=MibTableColumn
brpsServiceProtocolBanyan=_BrpsServiceProtocolBanyan_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,21),_BrpsServiceProtocolBanyan_Type())
brpsServiceProtocolBanyan.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolBanyan.setStatus(_A)
class _BrpsServiceProtocolDLC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolDLC_Type.__name__=_B
_BrpsServiceProtocolDLC_Object=MibTableColumn
brpsServiceProtocolDLC=_BrpsServiceProtocolDLC_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,22),_BrpsServiceProtocolDLC_Type())
brpsServiceProtocolDLC.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolDLC.setStatus(_A)
class _BrpsServiceProtocolNetBEUI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolNetBEUI_Type.__name__=_B
_BrpsServiceProtocolNetBEUI_Object=MibTableColumn
brpsServiceProtocolNetBEUI=_BrpsServiceProtocolNetBEUI_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,23),_BrpsServiceProtocolNetBEUI_Type())
brpsServiceProtocolNetBEUI.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolNetBEUI.setStatus(_A)
class _BrpsServiceNetwareServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceNetwareServerMode_Type.__name__=_B
_BrpsServiceNetwareServerMode_Object=MibTableColumn
brpsServiceNetwareServerMode=_BrpsServiceNetwareServerMode_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,24),_BrpsServiceNetwareServerMode_Type())
brpsServiceNetwareServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceNetwareServerMode.setStatus(_A)
class _BrpsServiceNetwareRemotePrinterNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsServiceNetwareRemotePrinterNum_Type.__name__=_B
_BrpsServiceNetwareRemotePrinterNum_Object=MibTableColumn
brpsServiceNetwareRemotePrinterNum=_BrpsServiceNetwareRemotePrinterNum_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,25),_BrpsServiceNetwareRemotePrinterNum_Type())
brpsServiceNetwareRemotePrinterNum.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceNetwareRemotePrinterNum.setStatus(_A)
class _BrpsServiceProtocolIPP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsServiceProtocolIPP_Type.__name__=_B
_BrpsServiceProtocolIPP_Object=MibTableColumn
brpsServiceProtocolIPP=_BrpsServiceProtocolIPP_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,26),_BrpsServiceProtocolIPP_Type())
brpsServiceProtocolIPP.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceProtocolIPP.setStatus(_A)
class _BrpsServiceAppleTalkType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsServiceAppleTalkType_Type.__name__=_F
_BrpsServiceAppleTalkType_Object=MibTableColumn
brpsServiceAppleTalkType=_BrpsServiceAppleTalkType_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,2,1,27),_BrpsServiceAppleTalkType_Type())
brpsServiceAppleTalkType.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceAppleTalkType.setStatus(_A)
class _BrpsServiceStringLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_BrpsServiceStringLimit_Type.__name__=_B
_BrpsServiceStringLimit_Object=MibScalar
brpsServiceStringLimit=_BrpsServiceStringLimit_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,3),_BrpsServiceStringLimit_Type())
brpsServiceStringLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceStringLimit.setStatus(_A)
_BrpsServiceStringInfoTable_Object=MibTable
brpsServiceStringInfoTable=_BrpsServiceStringInfoTable_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,4))
if mibBuilder.loadTexts:brpsServiceStringInfoTable.setStatus(_A)
_BrpsServiceStringInfoEntry_Object=MibTableRow
brpsServiceStringInfoEntry=_BrpsServiceStringInfoEntry_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,4,1))
brpsServiceStringInfoEntry.setIndexNames((0,_E,_B5))
if mibBuilder.loadTexts:brpsServiceStringInfoEntry.setStatus(_A)
class _BrpsServiceStringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrpsServiceStringIndex_Type.__name__=_B
_BrpsServiceStringIndex_Object=MibTableColumn
brpsServiceStringIndex=_BrpsServiceStringIndex_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,4,1,1),_BrpsServiceStringIndex_Type())
brpsServiceStringIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceStringIndex.setStatus(_A)
class _BrpsServiceString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrpsServiceString_Type.__name__=_F
_BrpsServiceString_Object=MibTableColumn
brpsServiceString=_BrpsServiceString_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,4,1,2),_BrpsServiceString_Type())
brpsServiceString.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsServiceString.setStatus(_A)
_BrpsServiceStringCount_Type=Integer32
_BrpsServiceStringCount_Object=MibScalar
brpsServiceStringCount=_BrpsServiceStringCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,5),_BrpsServiceStringCount_Type())
brpsServiceStringCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceStringCount.setStatus(_A)
_BrpsServiceFilterCount_Type=Integer32
_BrpsServiceFilterCount_Object=MibScalar
brpsServiceFilterCount=_BrpsServiceFilterCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,4,6),_BrpsServiceFilterCount_Type())
brpsServiceFilterCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServiceFilterCount.setStatus(_A)
_Brprotocol_ObjectIdentity=ObjectIdentity
brprotocol=_Brprotocol_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5))
_Brlat_ObjectIdentity=ObjectIdentity
brlat=_Brlat_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,1))
class _BrpsLATSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsLATSupported_Type.__name__=_B
_BrpsLATSupported_Object=MibScalar
brpsLATSupported=_BrpsLATSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,1),_BrpsLATSupported_Type())
brpsLATSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsLATSupported.setStatus(_A)
class _BrpsLATEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsLATEnable_Type.__name__=_B
_BrpsLATEnable_Object=MibScalar
brpsLATEnable=_BrpsLATEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,2),_BrpsLATEnable_Type())
brpsLATEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATEnable.setStatus(_A)
class _BrpsLATCircuitTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,499))
_BrpsLATCircuitTimer_Type.__name__=_B
_BrpsLATCircuitTimer_Object=MibScalar
brpsLATCircuitTimer=_BrpsLATCircuitTimer_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,3),_BrpsLATCircuitTimer_Type())
brpsLATCircuitTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATCircuitTimer.setStatus(_A)
class _BrpsLATKeepAliveTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_BrpsLATKeepAliveTimer_Type.__name__=_B
_BrpsLATKeepAliveTimer_Object=MibScalar
brpsLATKeepAliveTimer=_BrpsLATKeepAliveTimer_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,4),_BrpsLATKeepAliveTimer_Type())
brpsLATKeepAliveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATKeepAliveTimer.setStatus(_A)
class _BrpsLATReceiveBufferMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrpsLATReceiveBufferMax_Type.__name__=_B
_BrpsLATReceiveBufferMax_Object=MibScalar
brpsLATReceiveBufferMax=_BrpsLATReceiveBufferMax_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,5),_BrpsLATReceiveBufferMax_Type())
brpsLATReceiveBufferMax.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATReceiveBufferMax.setStatus(_A)
class _BrpsLATTransmitBufferMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_BrpsLATTransmitBufferMax_Type.__name__=_B
_BrpsLATTransmitBufferMax_Object=MibScalar
brpsLATTransmitBufferMax=_BrpsLATTransmitBufferMax_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,6),_BrpsLATTransmitBufferMax_Type())
brpsLATTransmitBufferMax.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATTransmitBufferMax.setStatus(_A)
class _BrpsLATTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_BrpsLATTimeout_Type.__name__=_B
_BrpsLATTimeout_Object=MibScalar
brpsLATTimeout=_BrpsLATTimeout_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,7),_BrpsLATTimeout_Type())
brpsLATTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATTimeout.setStatus(_A)
class _BrpsLATGroup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_BrpsLATGroup_Type.__name__=_F
_BrpsLATGroup_Object=MibScalar
brpsLATGroup=_BrpsLATGroup_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,1,8),_BrpsLATGroup_Type())
brpsLATGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsLATGroup.setStatus(_A)
_Brtcpip_ObjectIdentity=ObjectIdentity
brtcpip=_Brtcpip_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,2))
class _BrpsTCPIPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPSupported_Type.__name__=_B
_BrpsTCPIPSupported_Object=MibScalar
brpsTCPIPSupported=_BrpsTCPIPSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,1),_BrpsTCPIPSupported_Type())
brpsTCPIPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsTCPIPSupported.setStatus(_A)
class _BrpsTCPIPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPEnable_Type.__name__=_B
_BrpsTCPIPEnable_Object=MibScalar
brpsTCPIPEnable=_BrpsTCPIPEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,2),_BrpsTCPIPEnable_Type())
brpsTCPIPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPEnable.setStatus(_A)
_BrpsTCPIPAddress_Type=IpAddress
_BrpsTCPIPAddress_Object=MibScalar
brpsTCPIPAddress=_BrpsTCPIPAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,3),_BrpsTCPIPAddress_Type())
brpsTCPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPAddress.setStatus(_A)
_BrpsTCPIPSubnetMask_Type=IpAddress
_BrpsTCPIPSubnetMask_Object=MibScalar
brpsTCPIPSubnetMask=_BrpsTCPIPSubnetMask_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,4),_BrpsTCPIPSubnetMask_Type())
brpsTCPIPSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPSubnetMask.setStatus(_A)
_BrpsTCPIPGateway_Type=IpAddress
_BrpsTCPIPGateway_Object=MibScalar
brpsTCPIPGateway=_BrpsTCPIPGateway_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,5),_BrpsTCPIPGateway_Type())
brpsTCPIPGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPGateway.setStatus(_A)
class _BrpsTCPIPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrpsTCPIPMethod_Type.__name__=_B
_BrpsTCPIPMethod_Object=MibScalar
brpsTCPIPMethod=_BrpsTCPIPMethod_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,6),_BrpsTCPIPMethod_Type())
brpsTCPIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPMethod.setStatus(_A)
class _BrpsTCPIPTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsTCPIPTimeout_Type.__name__=_B
_BrpsTCPIPTimeout_Object=MibScalar
brpsTCPIPTimeout=_BrpsTCPIPTimeout_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,7),_BrpsTCPIPTimeout_Type())
brpsTCPIPTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPTimeout.setStatus(_A)
class _BrpsTCPIPBootTries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsTCPIPBootTries_Type.__name__=_B
_BrpsTCPIPBootTries_Object=MibScalar
brpsTCPIPBootTries=_BrpsTCPIPBootTries_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,8),_BrpsTCPIPBootTries_Type())
brpsTCPIPBootTries.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPBootTries.setStatus(_A)
class _BrpsTCPIPMaxWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,65535))
_BrpsTCPIPMaxWindow_Type.__name__=_B
_BrpsTCPIPMaxWindow_Object=MibScalar
brpsTCPIPMaxWindow=_BrpsTCPIPMaxWindow_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,9),_BrpsTCPIPMaxWindow_Type())
brpsTCPIPMaxWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPMaxWindow.setStatus(_A)
class _BrpsTCPIPRARPNoSubnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPRARPNoSubnet_Type.__name__=_B
_BrpsTCPIPRARPNoSubnet_Object=MibScalar
brpsTCPIPRARPNoSubnet=_BrpsTCPIPRARPNoSubnet_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,10),_BrpsTCPIPRARPNoSubnet_Type())
brpsTCPIPRARPNoSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPRARPNoSubnet.setStatus(_A)
class _BrpsTCPIPRARPNoGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPRARPNoGateway_Type.__name__=_B
_BrpsTCPIPRARPNoGateway_Object=MibScalar
brpsTCPIPRARPNoGateway=_BrpsTCPIPRARPNoGateway_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,11),_BrpsTCPIPRARPNoGateway_Type())
brpsTCPIPRARPNoGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPRARPNoGateway.setStatus(_A)
class _BrpsTCPIPUpdate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_BrpsTCPIPUpdate_Type.__name__=_G
_BrpsTCPIPUpdate_Object=MibScalar
brpsTCPIPUpdate=_BrpsTCPIPUpdate_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,12),_BrpsTCPIPUpdate_Type())
brpsTCPIPUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPUpdate.setStatus(_A)
class _BrpsTCPIPBanner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPBanner_Type.__name__=_B
_BrpsTCPIPBanner_Object=MibScalar
brpsTCPIPBanner=_BrpsTCPIPBanner_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,13),_BrpsTCPIPBanner_Type())
brpsTCPIPBanner.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPBanner.setStatus(_A)
class _BrpsTCPIPFastTimeoutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPFastTimeoutEnable_Type.__name__=_B
_BrpsTCPIPFastTimeoutEnable_Object=MibScalar
brpsTCPIPFastTimeoutEnable=_BrpsTCPIPFastTimeoutEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,14),_BrpsTCPIPFastTimeoutEnable_Type())
brpsTCPIPFastTimeoutEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPFastTimeoutEnable.setStatus(_A)
class _BrpsTCPIPLPRRetryEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTCPIPLPRRetryEnable_Type.__name__=_B
_BrpsTCPIPLPRRetryEnable_Object=MibScalar
brpsTCPIPLPRRetryEnable=_BrpsTCPIPLPRRetryEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,15),_BrpsTCPIPLPRRetryEnable_Type())
brpsTCPIPLPRRetryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPLPRRetryEnable.setStatus(_A)
class _BrpsTCPIPUseMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrpsTCPIPUseMethod_Type.__name__=_B
_BrpsTCPIPUseMethod_Object=MibScalar
brpsTCPIPUseMethod=_BrpsTCPIPUseMethod_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,16),_BrpsTCPIPUseMethod_Type())
brpsTCPIPUseMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPUseMethod.setStatus(_A)
_BrpsTCPIPMethodServer_Type=IpAddress
_BrpsTCPIPMethodServer_Object=MibScalar
brpsTCPIPMethodServer=_BrpsTCPIPMethodServer_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,17),_BrpsTCPIPMethodServer_Type())
brpsTCPIPMethodServer.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPMethodServer.setStatus(_A)
_BrpsTCPIPAccessTable_Object=MibTable
brpsTCPIPAccessTable=_BrpsTCPIPAccessTable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,18))
if mibBuilder.loadTexts:brpsTCPIPAccessTable.setStatus(_A)
_BrpsTCPIPAccessEntry_Object=MibTableRow
brpsTCPIPAccessEntry=_BrpsTCPIPAccessEntry_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,18,1))
brpsTCPIPAccessEntry.setIndexNames((0,_E,_B6))
if mibBuilder.loadTexts:brpsTCPIPAccessEntry.setStatus(_A)
class _BrpsTCPIPAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrpsTCPIPAccessIndex_Type.__name__=_B
_BrpsTCPIPAccessIndex_Object=MibTableColumn
brpsTCPIPAccessIndex=_BrpsTCPIPAccessIndex_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,18,1,1),_BrpsTCPIPAccessIndex_Type())
brpsTCPIPAccessIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsTCPIPAccessIndex.setStatus(_A)
_BrpsTCPIPAccessNodeAddress_Type=IpAddress
_BrpsTCPIPAccessNodeAddress_Object=MibTableColumn
brpsTCPIPAccessNodeAddress=_BrpsTCPIPAccessNodeAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,18,1,2),_BrpsTCPIPAccessNodeAddress_Type())
brpsTCPIPAccessNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPAccessNodeAddress.setStatus(_A)
_BrpsTCPIPAccessSubnetMask_Type=IpAddress
_BrpsTCPIPAccessSubnetMask_Object=MibTableColumn
brpsTCPIPAccessSubnetMask=_BrpsTCPIPAccessSubnetMask_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,18,1,3),_BrpsTCPIPAccessSubnetMask_Type())
brpsTCPIPAccessSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTCPIPAccessSubnetMask.setStatus(_A)
class _BrpsAdvancedTCPIPAccessSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAdvancedTCPIPAccessSupported_Type.__name__=_B
_BrpsAdvancedTCPIPAccessSupported_Object=MibScalar
brpsAdvancedTCPIPAccessSupported=_BrpsAdvancedTCPIPAccessSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,19),_BrpsAdvancedTCPIPAccessSupported_Type())
brpsAdvancedTCPIPAccessSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAdvancedTCPIPAccessSupported.setStatus(_A)
class _BrpsAdvancedTCPIPAccessEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAdvancedTCPIPAccessEnable_Type.__name__=_B
_BrpsAdvancedTCPIPAccessEnable_Object=MibScalar
brpsAdvancedTCPIPAccessEnable=_BrpsAdvancedTCPIPAccessEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,20),_BrpsAdvancedTCPIPAccessEnable_Type())
brpsAdvancedTCPIPAccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAdvancedTCPIPAccessEnable.setStatus(_A)
_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Type=IpAddress
_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Object=MibScalar
brpsAdvancedTCPIPAccessAdministratorIPAddress=_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,21),_BrpsAdvancedTCPIPAccessAdministratorIPAddress_Type())
brpsAdvancedTCPIPAccessAdministratorIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAdvancedTCPIPAccessAdministratorIPAddress.setStatus(_A)
class _BrpsAdvancedTCPIPAccessSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAdvancedTCPIPAccessSetting_Type.__name__=_B
_BrpsAdvancedTCPIPAccessSetting_Object=MibScalar
brpsAdvancedTCPIPAccessSetting=_BrpsAdvancedTCPIPAccessSetting_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,2,22),_BrpsAdvancedTCPIPAccessSetting_Type())
brpsAdvancedTCPIPAccessSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAdvancedTCPIPAccessSetting.setStatus(_A)
_Brnetware_ObjectIdentity=ObjectIdentity
brnetware=_Brnetware_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,3))
class _BrpsNetwareSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsNetwareSupported_Type.__name__=_B
_BrpsNetwareSupported_Object=MibScalar
brpsNetwareSupported=_BrpsNetwareSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,1),_BrpsNetwareSupported_Type())
brpsNetwareSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareSupported.setStatus(_A)
class _BrpsNetwareEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetwareEnable_Type.__name__=_B
_BrpsNetwareEnable_Object=MibScalar
brpsNetwareEnable=_BrpsNetwareEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,2),_BrpsNetwareEnable_Type())
brpsNetwareEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwareEnable.setStatus(_A)
class _BrpsNetwareFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrpsNetwareFrameType_Type.__name__=_B
_BrpsNetwareFrameType_Object=MibScalar
brpsNetwareFrameType=_BrpsNetwareFrameType_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,3),_BrpsNetwareFrameType_Type())
brpsNetwareFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwareFrameType.setStatus(_A)
class _BrpsNetwarePollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_BrpsNetwarePollFreq_Type.__name__=_B
_BrpsNetwarePollFreq_Object=MibScalar
brpsNetwarePollFreq=_BrpsNetwarePollFreq_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,4),_BrpsNetwarePollFreq_Type())
brpsNetwarePollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwarePollFreq.setStatus(_A)
class _BrpsNetwareAdvFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,210))
_BrpsNetwareAdvFreq_Type.__name__=_B
_BrpsNetwareAdvFreq_Object=MibScalar
brpsNetwareAdvFreq=_BrpsNetwareAdvFreq_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,5),_BrpsNetwareAdvFreq_Type())
brpsNetwareAdvFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwareAdvFreq.setStatus(_A)
class _BrpsNetwarePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsNetwarePassword_Type.__name__=_F
_BrpsNetwarePassword_Object=MibScalar
brpsNetwarePassword=_BrpsNetwarePassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,6),_BrpsNetwarePassword_Type())
brpsNetwarePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwarePassword.setStatus(_A)
class _BrpsNetwareRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetwareRestart_Type.__name__=_B
_BrpsNetwareRestart_Object=MibScalar
brpsNetwareRestart=_BrpsNetwareRestart_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,7),_BrpsNetwareRestart_Type())
brpsNetwareRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwareRestart.setStatus(_A)
_BrpsNetwareServerTable_Object=MibTable
brpsNetwareServerTable=_BrpsNetwareServerTable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,8))
if mibBuilder.loadTexts:brpsNetwareServerTable.setStatus(_A)
_BrpsNetwareServerEntry_Object=MibTableRow
brpsNetwareServerEntry=_BrpsNetwareServerEntry_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,8,1))
brpsNetwareServerEntry.setIndexNames((0,_E,_AL),(0,_E,_B7))
if mibBuilder.loadTexts:brpsNetwareServerEntry.setStatus(_A)
class _BrpsNetwareServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrpsNetwareServerIndex_Type.__name__=_B
_BrpsNetwareServerIndex_Object=MibTableColumn
brpsNetwareServerIndex=_BrpsNetwareServerIndex_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,8,1,1),_BrpsNetwareServerIndex_Type())
brpsNetwareServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareServerIndex.setStatus(_A)
class _BrpsNetwareServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrpsNetwareServerName_Type.__name__=_F
_BrpsNetwareServerName_Object=MibTableColumn
brpsNetwareServerName=_BrpsNetwareServerName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,8,1,2),_BrpsNetwareServerName_Type())
brpsNetwareServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetwareServerName.setStatus(_A)
class _BrpsNetwarePasswordSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetwarePasswordSet_Type.__name__=_B
_BrpsNetwarePasswordSet_Object=MibScalar
brpsNetwarePasswordSet=_BrpsNetwarePasswordSet_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,9),_BrpsNetwarePasswordSet_Type())
brpsNetwarePasswordSet.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwarePasswordSet.setStatus(_A)
class _BrpsNDSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNDSSupported_Type.__name__=_B
_BrpsNDSSupported_Object=MibScalar
brpsNDSSupported=_BrpsNDSSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,10),_BrpsNDSSupported_Type())
brpsNDSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNDSSupported.setStatus(_A)
class _BrpsNetwareEtherIINetInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsNetwareEtherIINetInfo_Type.__name__=_F
_BrpsNetwareEtherIINetInfo_Object=MibScalar
brpsNetwareEtherIINetInfo=_BrpsNetwareEtherIINetInfo_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,11),_BrpsNetwareEtherIINetInfo_Type())
brpsNetwareEtherIINetInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareEtherIINetInfo.setStatus(_A)
class _BrpsNetwareEtherIICount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsNetwareEtherIICount_Type.__name__=_B
_BrpsNetwareEtherIICount_Object=MibScalar
brpsNetwareEtherIICount=_BrpsNetwareEtherIICount_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,12),_BrpsNetwareEtherIICount_Type())
brpsNetwareEtherIICount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareEtherIICount.setStatus(_A)
class _BrpsNetware8022NetInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsNetware8022NetInfo_Type.__name__=_F
_BrpsNetware8022NetInfo_Object=MibScalar
brpsNetware8022NetInfo=_BrpsNetware8022NetInfo_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,13),_BrpsNetware8022NetInfo_Type())
brpsNetware8022NetInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetware8022NetInfo.setStatus(_A)
class _BrpsNetware8022Count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsNetware8022Count_Type.__name__=_B
_BrpsNetware8022Count_Object=MibScalar
brpsNetware8022Count=_BrpsNetware8022Count_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,14),_BrpsNetware8022Count_Type())
brpsNetware8022Count.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetware8022Count.setStatus(_A)
class _BrpsNetware8023NetInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsNetware8023NetInfo_Type.__name__=_F
_BrpsNetware8023NetInfo_Object=MibScalar
brpsNetware8023NetInfo=_BrpsNetware8023NetInfo_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,15),_BrpsNetware8023NetInfo_Type())
brpsNetware8023NetInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetware8023NetInfo.setStatus(_A)
class _BrpsNetware8023Count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsNetware8023Count_Type.__name__=_B
_BrpsNetware8023Count_Object=MibScalar
brpsNetware8023Count=_BrpsNetware8023Count_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,16),_BrpsNetware8023Count_Type())
brpsNetware8023Count.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetware8023Count.setStatus(_A)
class _BrpsNetwareSNAPNetInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsNetwareSNAPNetInfo_Type.__name__=_F
_BrpsNetwareSNAPNetInfo_Object=MibScalar
brpsNetwareSNAPNetInfo=_BrpsNetwareSNAPNetInfo_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,17),_BrpsNetwareSNAPNetInfo_Type())
brpsNetwareSNAPNetInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareSNAPNetInfo.setStatus(_A)
class _BrpsNetwareSNAPCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsNetwareSNAPCount_Type.__name__=_B
_BrpsNetwareSNAPCount_Object=MibScalar
brpsNetwareSNAPCount=_BrpsNetwareSNAPCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,18),_BrpsNetwareSNAPCount_Type())
brpsNetwareSNAPCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareSNAPCount.setStatus(_A)
class _BrpsNetwareServicingServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrpsNetwareServicingServerName_Type.__name__=_F
_BrpsNetwareServicingServerName_Object=MibScalar
brpsNetwareServicingServerName=_BrpsNetwareServicingServerName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,19),_BrpsNetwareServicingServerName_Type())
brpsNetwareServicingServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareServicingServerName.setStatus(_A)
class _BrpsNetwareServicingQueueName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrpsNetwareServicingQueueName_Type.__name__=_F
_BrpsNetwareServicingQueueName_Object=MibScalar
brpsNetwareServicingQueueName=_BrpsNetwareServicingQueueName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,20),_BrpsNetwareServicingQueueName_Type())
brpsNetwareServicingQueueName.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareServicingQueueName.setStatus(_A)
class _BrpsNetwareServicingServerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsNetwareServicingServerCount_Type.__name__=_B
_BrpsNetwareServicingServerCount_Object=MibScalar
brpsNetwareServicingServerCount=_BrpsNetwareServicingServerCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,21),_BrpsNetwareServicingServerCount_Type())
brpsNetwareServicingServerCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareServicingServerCount.setStatus(_A)
class _BrpsNetwareServicingQueueCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrpsNetwareServicingQueueCount_Type.__name__=_B
_BrpsNetwareServicingQueueCount_Object=MibScalar
brpsNetwareServicingQueueCount=_BrpsNetwareServicingQueueCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,22),_BrpsNetwareServicingQueueCount_Type())
brpsNetwareServicingQueueCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwareServicingQueueCount.setStatus(_A)
class _BrpsNetwarePrintJob_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsNetwarePrintJob_Type.__name__=_B
_BrpsNetwarePrintJob_Object=MibScalar
brpsNetwarePrintJob=_BrpsNetwarePrintJob_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,3,23),_BrpsNetwarePrintJob_Type())
brpsNetwarePrintJob.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetwarePrintJob.setStatus(_A)
_Brappletalk_ObjectIdentity=ObjectIdentity
brappletalk=_Brappletalk_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,4))
class _BrpsAppleTalkSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAppleTalkSupported_Type.__name__=_B
_BrpsAppleTalkSupported_Object=MibScalar
brpsAppleTalkSupported=_BrpsAppleTalkSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,1),_BrpsAppleTalkSupported_Type())
brpsAppleTalkSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkSupported.setStatus(_A)
class _BrpsAppleTalkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAppleTalkEnable_Type.__name__=_B
_BrpsAppleTalkEnable_Object=MibScalar
brpsAppleTalkEnable=_BrpsAppleTalkEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,2),_BrpsAppleTalkEnable_Type())
brpsAppleTalkEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAppleTalkEnable.setStatus(_A)
_BrpsAppleTalkZone_Type=DisplayString
_BrpsAppleTalkZone_Object=MibScalar
brpsAppleTalkZone=_BrpsAppleTalkZone_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,3),_BrpsAppleTalkZone_Type())
brpsAppleTalkZone.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAppleTalkZone.setStatus(_A)
class _BrpsAppleTalkPrintJob_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsAppleTalkPrintJob_Type.__name__=_B
_BrpsAppleTalkPrintJob_Object=MibScalar
brpsAppleTalkPrintJob=_BrpsAppleTalkPrintJob_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,4),_BrpsAppleTalkPrintJob_Type())
brpsAppleTalkPrintJob.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkPrintJob.setStatus(_A)
class _BrpsAppleTalkReadByte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsAppleTalkReadByte_Type.__name__=_B
_BrpsAppleTalkReadByte_Object=MibScalar
brpsAppleTalkReadByte=_BrpsAppleTalkReadByte_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,5),_BrpsAppleTalkReadByte_Type())
brpsAppleTalkReadByte.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkReadByte.setStatus(_A)
class _BrpsAppleTalkWriteByte_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsAppleTalkWriteByte_Type.__name__=_B
_BrpsAppleTalkWriteByte_Object=MibScalar
brpsAppleTalkWriteByte=_BrpsAppleTalkWriteByte_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,6),_BrpsAppleTalkWriteByte_Type())
brpsAppleTalkWriteByte.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkWriteByte.setStatus(_A)
class _BrpsAppleTalkReadError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsAppleTalkReadError_Type.__name__=_B
_BrpsAppleTalkReadError_Object=MibScalar
brpsAppleTalkReadError=_BrpsAppleTalkReadError_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,7),_BrpsAppleTalkReadError_Type())
brpsAppleTalkReadError.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkReadError.setStatus(_A)
class _BrpsAppleTalkWriteError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsAppleTalkWriteError_Type.__name__=_B
_BrpsAppleTalkWriteError_Object=MibScalar
brpsAppleTalkWriteError=_BrpsAppleTalkWriteError_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,4,8),_BrpsAppleTalkWriteError_Type())
brpsAppleTalkWriteError.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAppleTalkWriteError.setStatus(_A)
_Brbanyan_ObjectIdentity=ObjectIdentity
brbanyan=_Brbanyan_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,5))
class _BrpsBanyanSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsBanyanSupported_Type.__name__=_B
_BrpsBanyanSupported_Object=MibScalar
brpsBanyanSupported=_BrpsBanyanSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,1),_BrpsBanyanSupported_Type())
brpsBanyanSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanSupported.setStatus(_A)
class _BrpsBanyanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsBanyanEnable_Type.__name__=_B
_BrpsBanyanEnable_Object=MibScalar
brpsBanyanEnable=_BrpsBanyanEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,2),_BrpsBanyanEnable_Type())
brpsBanyanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsBanyanEnable.setStatus(_A)
class _BrpsBanyanLoginName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsBanyanLoginName_Type.__name__=_F
_BrpsBanyanLoginName_Object=MibScalar
brpsBanyanLoginName=_BrpsBanyanLoginName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,3),_BrpsBanyanLoginName_Type())
brpsBanyanLoginName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsBanyanLoginName.setStatus(_A)
class _BrpsBanyanPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BrpsBanyanPassword_Type.__name__=_F
_BrpsBanyanPassword_Object=MibScalar
brpsBanyanPassword=_BrpsBanyanPassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,4),_BrpsBanyanPassword_Type())
brpsBanyanPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsBanyanPassword.setStatus(_A)
class _BrpsBanyanHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsBanyanHopCount_Type.__name__=_B
_BrpsBanyanHopCount_Object=MibScalar
brpsBanyanHopCount=_BrpsBanyanHopCount_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,5),_BrpsBanyanHopCount_Type())
brpsBanyanHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsBanyanHopCount.setStatus(_A)
class _BrpsBanyanTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsBanyanTimeout_Type.__name__=_B
_BrpsBanyanTimeout_Object=MibScalar
brpsBanyanTimeout=_BrpsBanyanTimeout_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,6),_BrpsBanyanTimeout_Type())
brpsBanyanTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsBanyanTimeout.setStatus(_A)
class _BrpsBanyanPasswordSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsBanyanPasswordSet_Type.__name__=_B
_BrpsBanyanPasswordSet_Object=MibScalar
brpsBanyanPasswordSet=_BrpsBanyanPasswordSet_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,7),_BrpsBanyanPasswordSet_Type())
brpsBanyanPasswordSet.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanPasswordSet.setStatus(_A)
class _BrpsBanyanIPNetworkID1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_BrpsBanyanIPNetworkID1_Type.__name__=_G
_BrpsBanyanIPNetworkID1_Object=MibScalar
brpsBanyanIPNetworkID1=_BrpsBanyanIPNetworkID1_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,8),_BrpsBanyanIPNetworkID1_Type())
brpsBanyanIPNetworkID1.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPNetworkID1.setStatus(_A)
class _BrpsBanyanIPNetworkID2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_BrpsBanyanIPNetworkID2_Type.__name__=_G
_BrpsBanyanIPNetworkID2_Object=MibScalar
brpsBanyanIPNetworkID2=_BrpsBanyanIPNetworkID2_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,9),_BrpsBanyanIPNetworkID2_Type())
brpsBanyanIPNetworkID2.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPNetworkID2.setStatus(_A)
class _BrpsBanyanRouter1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_BrpsBanyanRouter1_Type.__name__=_G
_BrpsBanyanRouter1_Object=MibScalar
brpsBanyanRouter1=_BrpsBanyanRouter1_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,10),_BrpsBanyanRouter1_Type())
brpsBanyanRouter1.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanRouter1.setStatus(_A)
class _BrpsBanyanRouter2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_BrpsBanyanRouter2_Type.__name__=_G
_BrpsBanyanRouter2_Object=MibScalar
brpsBanyanRouter2=_BrpsBanyanRouter2_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,11),_BrpsBanyanRouter2_Type())
brpsBanyanRouter2.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanRouter2.setStatus(_A)
class _BrpsBanyanIPPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanIPPacket_Type.__name__=_B
_BrpsBanyanIPPacket_Object=MibScalar
brpsBanyanIPPacket=_BrpsBanyanIPPacket_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,12),_BrpsBanyanIPPacket_Type())
brpsBanyanIPPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPPacket.setStatus(_A)
class _BrpsBanyanErrorCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanErrorCS_Type.__name__=_B
_BrpsBanyanErrorCS_Object=MibScalar
brpsBanyanErrorCS=_BrpsBanyanErrorCS_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,13),_BrpsBanyanErrorCS_Type())
brpsBanyanErrorCS.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanErrorCS.setStatus(_A)
class _BrpsBanyanErrorPT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanErrorPT_Type.__name__=_B
_BrpsBanyanErrorPT_Object=MibScalar
brpsBanyanErrorPT=_BrpsBanyanErrorPT_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,14),_BrpsBanyanErrorPT_Type())
brpsBanyanErrorPT.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanErrorPT.setStatus(_A)
class _BrpsBanyanErrorLE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanErrorLE_Type.__name__=_B
_BrpsBanyanErrorLE_Object=MibScalar
brpsBanyanErrorLE=_BrpsBanyanErrorLE_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,15),_BrpsBanyanErrorLE_Type())
brpsBanyanErrorLE.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanErrorLE.setStatus(_A)
class _BrpsBanyanPrintServerStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsBanyanPrintServerStatus_Type.__name__=_F
_BrpsBanyanPrintServerStatus_Object=MibScalar
brpsBanyanPrintServerStatus=_BrpsBanyanPrintServerStatus_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,16),_BrpsBanyanPrintServerStatus_Type())
brpsBanyanPrintServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanPrintServerStatus.setStatus(_A)
class _BrpsBanyanServerAddress1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_BrpsBanyanServerAddress1_Type.__name__=_G
_BrpsBanyanServerAddress1_Object=MibScalar
brpsBanyanServerAddress1=_BrpsBanyanServerAddress1_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,17),_BrpsBanyanServerAddress1_Type())
brpsBanyanServerAddress1.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanServerAddress1.setStatus(_A)
class _BrpsBanyanServerAddress2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_BrpsBanyanServerAddress2_Type.__name__=_G
_BrpsBanyanServerAddress2_Object=MibScalar
brpsBanyanServerAddress2=_BrpsBanyanServerAddress2_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,18),_BrpsBanyanServerAddress2_Type())
brpsBanyanServerAddress2.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanServerAddress2.setStatus(_A)
class _BrpsBanyanIPCConnectionInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsBanyanIPCConnectionInformation_Type.__name__=_F
_BrpsBanyanIPCConnectionInformation_Object=MibScalar
brpsBanyanIPCConnectionInformation=_BrpsBanyanIPCConnectionInformation_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,19),_BrpsBanyanIPCConnectionInformation_Type())
brpsBanyanIPCConnectionInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPCConnectionInformation.setStatus(_A)
class _BrpsBanyanIPCSequenceError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanIPCSequenceError_Type.__name__=_B
_BrpsBanyanIPCSequenceError_Object=MibScalar
brpsBanyanIPCSequenceError=_BrpsBanyanIPCSequenceError_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,20),_BrpsBanyanIPCSequenceError_Type())
brpsBanyanIPCSequenceError.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPCSequenceError.setStatus(_A)
class _BrpsBanyanIPCListen_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsBanyanIPCListen_Type.__name__=_F
_BrpsBanyanIPCListen_Object=MibScalar
brpsBanyanIPCListen=_BrpsBanyanIPCListen_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,21),_BrpsBanyanIPCListen_Type())
brpsBanyanIPCListen.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanIPCListen.setStatus(_A)
class _BrpsBanyanSPPConnectionInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsBanyanSPPConnectionInformation_Type.__name__=_F
_BrpsBanyanSPPConnectionInformation_Object=MibScalar
brpsBanyanSPPConnectionInformation=_BrpsBanyanSPPConnectionInformation_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,22),_BrpsBanyanSPPConnectionInformation_Type())
brpsBanyanSPPConnectionInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanSPPConnectionInformation.setStatus(_A)
class _BrpsBanyanSPPSequenceError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsBanyanSPPSequenceError_Type.__name__=_B
_BrpsBanyanSPPSequenceError_Object=MibScalar
brpsBanyanSPPSequenceError=_BrpsBanyanSPPSequenceError_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,23),_BrpsBanyanSPPSequenceError_Type())
brpsBanyanSPPSequenceError.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanSPPSequenceError.setStatus(_A)
class _BrpsBanyanSPPListen_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrpsBanyanSPPListen_Type.__name__=_F
_BrpsBanyanSPPListen_Object=MibScalar
brpsBanyanSPPListen=_BrpsBanyanSPPListen_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,5,24),_BrpsBanyanSPPListen_Type())
brpsBanyanSPPListen.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsBanyanSPPListen.setStatus(_A)
_Bremail_ObjectIdentity=ObjectIdentity
bremail=_Bremail_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,6))
class _BrpsEmailSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsEmailSupported_Type.__name__=_B
_BrpsEmailSupported_Object=MibScalar
brpsEmailSupported=_BrpsEmailSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,1),_BrpsEmailSupported_Type())
brpsEmailSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsEmailSupported.setStatus(_A)
class _BrpsEmailEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsEmailEnable_Type.__name__=_B
_BrpsEmailEnable_Object=MibScalar
brpsEmailEnable=_BrpsEmailEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,2),_BrpsEmailEnable_Type())
brpsEmailEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailEnable.setStatus(_A)
_BrpsPOP3Address_Type=IpAddress
_BrpsPOP3Address_Object=MibScalar
brpsPOP3Address=_BrpsPOP3Address_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,3),_BrpsPOP3Address_Type())
brpsPOP3Address.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3Address.setStatus(_A)
_BrpsSMTPAddress_Type=IpAddress
_BrpsSMTPAddress_Object=MibScalar
brpsSMTPAddress=_BrpsSMTPAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,4),_BrpsSMTPAddress_Type())
brpsSMTPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSMTPAddress.setStatus(_A)
_BrpsPOP3Name_Type=DisplayString
_BrpsPOP3Name_Object=MibScalar
brpsPOP3Name=_BrpsPOP3Name_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,5),_BrpsPOP3Name_Type())
brpsPOP3Name.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3Name.setStatus(_A)
_BrpsPOP3Password_Type=DisplayString
_BrpsPOP3Password_Object=MibScalar
brpsPOP3Password=_BrpsPOP3Password_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,6),_BrpsPOP3Password_Type())
brpsPOP3Password.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3Password.setStatus(_A)
class _BrpsPOP3PollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,32767))
_BrpsPOP3PollFreq_Type.__name__=_B
_BrpsPOP3PollFreq_Object=MibScalar
brpsPOP3PollFreq=_BrpsPOP3PollFreq_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,7),_BrpsPOP3PollFreq_Type())
brpsPOP3PollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3PollFreq.setStatus(_A)
class _BrpsPOP3Timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,32767))
_BrpsPOP3Timeout_Type.__name__=_B
_BrpsPOP3Timeout_Object=MibScalar
brpsPOP3Timeout=_BrpsPOP3Timeout_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,8),_BrpsPOP3Timeout_Type())
brpsPOP3Timeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3Timeout.setStatus(_A)
class _BrpsPOP3PasswordSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsPOP3PasswordSet_Type.__name__=_B
_BrpsPOP3PasswordSet_Object=MibScalar
brpsPOP3PasswordSet=_BrpsPOP3PasswordSet_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,9),_BrpsPOP3PasswordSet_Type())
brpsPOP3PasswordSet.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3PasswordSet.setStatus(_A)
class _BrpsPOP3TotalMessage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalMessage_Type.__name__=_B
_BrpsPOP3TotalMessage_Object=MibScalar
brpsPOP3TotalMessage=_BrpsPOP3TotalMessage_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,10),_BrpsPOP3TotalMessage_Type())
brpsPOP3TotalMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalMessage.setStatus(_A)
class _BrpsPOP3TotalConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalConnect_Type.__name__=_B
_BrpsPOP3TotalConnect_Object=MibScalar
brpsPOP3TotalConnect=_BrpsPOP3TotalConnect_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,11),_BrpsPOP3TotalConnect_Type())
brpsPOP3TotalConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalConnect.setStatus(_A)
class _BrpsPOP3TotalConnectFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalConnectFailure_Type.__name__=_B
_BrpsPOP3TotalConnectFailure_Object=MibScalar
brpsPOP3TotalConnectFailure=_BrpsPOP3TotalConnectFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,12),_BrpsPOP3TotalConnectFailure_Type())
brpsPOP3TotalConnectFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalConnectFailure.setStatus(_A)
class _BrpsPOP3TotalConnectionLost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalConnectionLost_Type.__name__=_B
_BrpsPOP3TotalConnectionLost_Object=MibScalar
brpsPOP3TotalConnectionLost=_BrpsPOP3TotalConnectionLost_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,13),_BrpsPOP3TotalConnectionLost_Type())
brpsPOP3TotalConnectionLost.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalConnectionLost.setStatus(_A)
class _BrpsPOP3TotalUserFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalUserFailure_Type.__name__=_B
_BrpsPOP3TotalUserFailure_Object=MibScalar
brpsPOP3TotalUserFailure=_BrpsPOP3TotalUserFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,14),_BrpsPOP3TotalUserFailure_Type())
brpsPOP3TotalUserFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalUserFailure.setStatus(_A)
class _BrpsPOP3TotalPasswordFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalPasswordFailure_Type.__name__=_B
_BrpsPOP3TotalPasswordFailure_Object=MibScalar
brpsPOP3TotalPasswordFailure=_BrpsPOP3TotalPasswordFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,15),_BrpsPOP3TotalPasswordFailure_Type())
brpsPOP3TotalPasswordFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalPasswordFailure.setStatus(_A)
class _BrpsPOP3TotalIOError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalIOError_Type.__name__=_B
_BrpsPOP3TotalIOError_Object=MibScalar
brpsPOP3TotalIOError=_BrpsPOP3TotalIOError_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,16),_BrpsPOP3TotalIOError_Type())
brpsPOP3TotalIOError.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalIOError.setStatus(_A)
class _BrpsSMTPTotalMessage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsSMTPTotalMessage_Type.__name__=_B
_BrpsSMTPTotalMessage_Object=MibScalar
brpsSMTPTotalMessage=_BrpsSMTPTotalMessage_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,17),_BrpsSMTPTotalMessage_Type())
brpsSMTPTotalMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPTotalMessage.setStatus(_A)
class _BrpsSMTPTotalConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsSMTPTotalConnect_Type.__name__=_B
_BrpsSMTPTotalConnect_Object=MibScalar
brpsSMTPTotalConnect=_BrpsSMTPTotalConnect_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,18),_BrpsSMTPTotalConnect_Type())
brpsSMTPTotalConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPTotalConnect.setStatus(_A)
class _BrpsSMTPTotalConnectFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsSMTPTotalConnectFailure_Type.__name__=_B
_BrpsSMTPTotalConnectFailure_Object=MibScalar
brpsSMTPTotalConnectFailure=_BrpsSMTPTotalConnectFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,19),_BrpsSMTPTotalConnectFailure_Type())
brpsSMTPTotalConnectFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPTotalConnectFailure.setStatus(_A)
class _BrpsSMTPTotalRecvFromFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsSMTPTotalRecvFromFailure_Type.__name__=_B
_BrpsSMTPTotalRecvFromFailure_Object=MibScalar
brpsSMTPTotalRecvFromFailure=_BrpsSMTPTotalRecvFromFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,20),_BrpsSMTPTotalRecvFromFailure_Type())
brpsSMTPTotalRecvFromFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPTotalRecvFromFailure.setStatus(_A)
class _BrpsSMTPTotalSendToFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsSMTPTotalSendToFailure_Type.__name__=_B
_BrpsSMTPTotalSendToFailure_Object=MibScalar
brpsSMTPTotalSendToFailure=_BrpsSMTPTotalSendToFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,21),_BrpsSMTPTotalSendToFailure_Type())
brpsSMTPTotalSendToFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPTotalSendToFailure.setStatus(_A)
class _BrpsPOP3Supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsPOP3Supported_Type.__name__=_B
_BrpsPOP3Supported_Object=MibScalar
brpsPOP3Supported=_BrpsPOP3Supported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,101),_BrpsPOP3Supported_Type())
brpsPOP3Supported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3Supported.setStatus(_A)
class _BrpsSMTPServerAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsSMTPServerAuthMethod_Type.__name__=_B
_BrpsSMTPServerAuthMethod_Object=MibScalar
brpsSMTPServerAuthMethod=_BrpsSMTPServerAuthMethod_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,102),_BrpsSMTPServerAuthMethod_Type())
brpsSMTPServerAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSMTPServerAuthMethod.setStatus(_A)
class _BrpsSMTPAUTHUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_BrpsSMTPAUTHUsername_Type.__name__=_G
_BrpsSMTPAUTHUsername_Object=MibScalar
brpsSMTPAUTHUsername=_BrpsSMTPAUTHUsername_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,103),_BrpsSMTPAUTHUsername_Type())
brpsSMTPAUTHUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSMTPAUTHUsername.setStatus(_A)
class _BrpsSMTPAUTHPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsSMTPAUTHPassword_Type.__name__=_G
_BrpsSMTPAUTHPassword_Object=MibScalar
brpsSMTPAUTHPassword=_BrpsSMTPAUTHPassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,104),_BrpsSMTPAUTHPassword_Type())
brpsSMTPAUTHPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSMTPAUTHPassword.setStatus(_A)
class _BrpsSMTPAUTHPasswordSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsSMTPAUTHPasswordSet_Type.__name__=_B
_BrpsSMTPAUTHPasswordSet_Object=MibScalar
brpsSMTPAUTHPasswordSet=_BrpsSMTPAUTHPasswordSet_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,105),_BrpsSMTPAUTHPasswordSet_Type())
brpsSMTPAUTHPasswordSet.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPAUTHPasswordSet.setStatus(_A)
class _BrpsSmtpAUTHTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,32767))
_BrpsSmtpAUTHTimeout_Type.__name__=_B
_BrpsSmtpAUTHTimeout_Object=MibScalar
brpsSmtpAUTHTimeout=_BrpsSmtpAUTHTimeout_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,106),_BrpsSmtpAUTHTimeout_Type())
brpsSmtpAUTHTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSmtpAUTHTimeout.setStatus(_A)
class _BrpsPOPbeforeSMTPWait_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrpsPOPbeforeSMTPWait_Type.__name__=_B
_BrpsPOPbeforeSMTPWait_Object=MibScalar
brpsPOPbeforeSMTPWait=_BrpsPOPbeforeSMTPWait_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,107),_BrpsPOPbeforeSMTPWait_Type())
brpsPOPbeforeSMTPWait.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOPbeforeSMTPWait.setStatus(_A)
class _BrpsAPOPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAPOPEnable_Type.__name__=_B
_BrpsAPOPEnable_Object=MibScalar
brpsAPOPEnable=_BrpsAPOPEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,108),_BrpsAPOPEnable_Type())
brpsAPOPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsAPOPEnable.setStatus(_A)
class _BrpsSMTPEnhancedAuthSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrpsSMTPEnhancedAuthSupported_Type.__name__=_B
_BrpsSMTPEnhancedAuthSupported_Object=MibScalar
brpsSMTPEnhancedAuthSupported=_BrpsSMTPEnhancedAuthSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,150),_BrpsSMTPEnhancedAuthSupported_Type())
brpsSMTPEnhancedAuthSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsSMTPEnhancedAuthSupported.setStatus(_A)
class _BrpsAPOPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsAPOPSupported_Type.__name__=_B
_BrpsAPOPSupported_Object=MibScalar
brpsAPOPSupported=_BrpsAPOPSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,151),_BrpsAPOPSupported_Type())
brpsAPOPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsAPOPSupported.setStatus(_A)
class _BrpsEmailSendTestSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsEmailSendTestSupported_Type.__name__=_B
_BrpsEmailSendTestSupported_Object=MibScalar
brpsEmailSendTestSupported=_BrpsEmailSendTestSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,152),_BrpsEmailSendTestSupported_Type())
brpsEmailSendTestSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsEmailSendTestSupported.setStatus(_A)
class _BrpsEmailRecvTestSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsEmailRecvTestSupported_Type.__name__=_B
_BrpsEmailRecvTestSupported_Object=MibScalar
brpsEmailRecvTestSupported=_BrpsEmailRecvTestSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,153),_BrpsEmailRecvTestSupported_Type())
brpsEmailRecvTestSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsEmailRecvTestSupported.setStatus(_A)
class _BrpsChangeSMTPPortSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsChangeSMTPPortSupported_Type.__name__=_B
_BrpsChangeSMTPPortSupported_Object=MibScalar
brpsChangeSMTPPortSupported=_BrpsChangeSMTPPortSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,154),_BrpsChangeSMTPPortSupported_Type())
brpsChangeSMTPPortSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsChangeSMTPPortSupported.setStatus(_A)
class _BrpsSMTPPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrpsSMTPPortNumber_Type.__name__=_B
_BrpsSMTPPortNumber_Object=MibScalar
brpsSMTPPortNumber=_BrpsSMTPPortNumber_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,155),_BrpsSMTPPortNumber_Type())
brpsSMTPPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsSMTPPortNumber.setStatus(_A)
class _BrpsChangePOP3PortSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsChangePOP3PortSupported_Type.__name__=_B
_BrpsChangePOP3PortSupported_Object=MibScalar
brpsChangePOP3PortSupported=_BrpsChangePOP3PortSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,156),_BrpsChangePOP3PortSupported_Type())
brpsChangePOP3PortSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsChangePOP3PortSupported.setStatus(_A)
class _BrpsPOP3PortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrpsPOP3PortNumber_Type.__name__=_B
_BrpsPOP3PortNumber_Object=MibScalar
brpsPOP3PortNumber=_BrpsPOP3PortNumber_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,157),_BrpsPOP3PortNumber_Type())
brpsPOP3PortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsPOP3PortNumber.setStatus(_A)
class _BrpsTmpSMTPServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrpsTmpSMTPServerName_Type.__name__=_G
_BrpsTmpSMTPServerName_Object=MibScalar
brpsTmpSMTPServerName=_BrpsTmpSMTPServerName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,170),_BrpsTmpSMTPServerName_Type())
brpsTmpSMTPServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPServerName.setStatus(_A)
class _BrpsTmpSMTPServerAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsTmpSMTPServerAuthMethod_Type.__name__=_B
_BrpsTmpSMTPServerAuthMethod_Object=MibScalar
brpsTmpSMTPServerAuthMethod=_BrpsTmpSMTPServerAuthMethod_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,171),_BrpsTmpSMTPServerAuthMethod_Type())
brpsTmpSMTPServerAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPServerAuthMethod.setStatus(_A)
class _BrpsTmpSMTPAUTHUsername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_BrpsTmpSMTPAUTHUsername_Type.__name__=_G
_BrpsTmpSMTPAUTHUsername_Object=MibScalar
brpsTmpSMTPAUTHUsername=_BrpsTmpSMTPAUTHUsername_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,172),_BrpsTmpSMTPAUTHUsername_Type())
brpsTmpSMTPAUTHUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPAUTHUsername.setStatus(_A)
class _BrpsTmpSMTPAUTHPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsTmpSMTPAUTHPassword_Type.__name__=_G
_BrpsTmpSMTPAUTHPassword_Object=MibScalar
brpsTmpSMTPAUTHPassword=_BrpsTmpSMTPAUTHPassword_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,173),_BrpsTmpSMTPAUTHPassword_Type())
brpsTmpSMTPAUTHPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPAUTHPassword.setStatus(_A)
class _BrpsTmpPOP3ServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrpsTmpPOP3ServerName_Type.__name__=_G
_BrpsTmpPOP3ServerName_Object=MibScalar
brpsTmpPOP3ServerName=_BrpsTmpPOP3ServerName_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,174),_BrpsTmpPOP3ServerName_Type())
brpsTmpPOP3ServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPOP3ServerName.setStatus(_A)
_BrpsTmpPOP3Name_Type=DisplayString
_BrpsTmpPOP3Name_Object=MibScalar
brpsTmpPOP3Name=_BrpsTmpPOP3Name_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,175),_BrpsTmpPOP3Name_Type())
brpsTmpPOP3Name.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPOP3Name.setStatus(_A)
_BrpsTmpPOP3Password_Type=DisplayString
_BrpsTmpPOP3Password_Object=MibScalar
brpsTmpPOP3Password=_BrpsTmpPOP3Password_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,176),_BrpsTmpPOP3Password_Type())
brpsTmpPOP3Password.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPOP3Password.setStatus(_A)
_BrpsTmpPrintersEmailaddress_Type=OctetString
_BrpsTmpPrintersEmailaddress_Object=MibScalar
brpsTmpPrintersEmailaddress=_BrpsTmpPrintersEmailaddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,177),_BrpsTmpPrintersEmailaddress_Type())
brpsTmpPrintersEmailaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPrintersEmailaddress.setStatus(_A)
class _BrpsTmpAPOPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTmpAPOPEnable_Type.__name__=_B
_BrpsTmpAPOPEnable_Object=MibScalar
brpsTmpAPOPEnable=_BrpsTmpAPOPEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,178),_BrpsTmpAPOPEnable_Type())
brpsTmpAPOPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpAPOPEnable.setStatus(_A)
class _BrpsTmpSMTPAUTHPasswordModified_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTmpSMTPAUTHPasswordModified_Type.__name__=_B
_BrpsTmpSMTPAUTHPasswordModified_Object=MibScalar
brpsTmpSMTPAUTHPasswordModified=_BrpsTmpSMTPAUTHPasswordModified_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,179),_BrpsTmpSMTPAUTHPasswordModified_Type())
brpsTmpSMTPAUTHPasswordModified.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPAUTHPasswordModified.setStatus(_A)
class _BrpsTmpPOP3PasswordModified_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsTmpPOP3PasswordModified_Type.__name__=_B
_BrpsTmpPOP3PasswordModified_Object=MibScalar
brpsTmpPOP3PasswordModified=_BrpsTmpPOP3PasswordModified_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,180),_BrpsTmpPOP3PasswordModified_Type())
brpsTmpPOP3PasswordModified.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPOP3PasswordModified.setStatus(_A)
class _BrpsTmpSMTPPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrpsTmpSMTPPortNumber_Type.__name__=_B
_BrpsTmpSMTPPortNumber_Object=MibScalar
brpsTmpSMTPPortNumber=_BrpsTmpSMTPPortNumber_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,181),_BrpsTmpSMTPPortNumber_Type())
brpsTmpSMTPPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpSMTPPortNumber.setStatus(_A)
class _BrpsTmpPOP3PortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrpsTmpPOP3PortNumber_Type.__name__=_B
_BrpsTmpPOP3PortNumber_Object=MibScalar
brpsTmpPOP3PortNumber=_BrpsTmpPOP3PortNumber_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,182),_BrpsTmpPOP3PortNumber_Type())
brpsTmpPOP3PortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsTmpPOP3PortNumber.setStatus(_A)
class _BrpsEmailSendTestMail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsEmailSendTestMail_Type.__name__=_B
_BrpsEmailSendTestMail_Object=MibScalar
brpsEmailSendTestMail=_BrpsEmailSendTestMail_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,200),_BrpsEmailSendTestMail_Type())
brpsEmailSendTestMail.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailSendTestMail.setStatus(_A)
class _BrpsEmailTestDestinationAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_BrpsEmailTestDestinationAddress_Type.__name__=_F
_BrpsEmailTestDestinationAddress_Object=MibScalar
brpsEmailTestDestinationAddress=_BrpsEmailTestDestinationAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,201),_BrpsEmailTestDestinationAddress_Type())
brpsEmailTestDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailTestDestinationAddress.setStatus(_A)
class _BrpsEmailSendTestCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsEmailSendTestCall_Type.__name__=_B
_BrpsEmailSendTestCall_Object=MibScalar
brpsEmailSendTestCall=_BrpsEmailSendTestCall_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,210),_BrpsEmailSendTestCall_Type())
brpsEmailSendTestCall.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailSendTestCall.setStatus(_A)
class _BrpsEmailRecvTestCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsEmailRecvTestCall_Type.__name__=_B
_BrpsEmailRecvTestCall_Object=MibScalar
brpsEmailRecvTestCall=_BrpsEmailRecvTestCall_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,211),_BrpsEmailRecvTestCall_Type())
brpsEmailRecvTestCall.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailRecvTestCall.setStatus(_A)
class _BrpsEmailSendRecvTestCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BrpsEmailSendRecvTestCall_Type.__name__=_B
_BrpsEmailSendRecvTestCall_Object=MibScalar
brpsEmailSendRecvTestCall=_BrpsEmailSendRecvTestCall_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,212),_BrpsEmailSendRecvTestCall_Type())
brpsEmailSendRecvTestCall.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailSendRecvTestCall.setStatus(_A)
class _BrpsEmailTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsEmailTestResult_Type.__name__=_B
_BrpsEmailTestResult_Object=MibScalar
brpsEmailTestResult=_BrpsEmailTestResult_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,220),_BrpsEmailTestResult_Type())
brpsEmailTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsEmailTestResult.setStatus(_A)
class _BrpsPOP3TotalAPOPFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsPOP3TotalAPOPFailure_Type.__name__=_B
_BrpsPOP3TotalAPOPFailure_Object=MibScalar
brpsPOP3TotalAPOPFailure=_BrpsPOP3TotalAPOPFailure_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,6,221),_BrpsPOP3TotalAPOPFailure_Type())
brpsPOP3TotalAPOPFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsPOP3TotalAPOPFailure.setStatus(_A)
_Brdlc_ObjectIdentity=ObjectIdentity
brdlc=_Brdlc_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,7))
class _BrpsDLCSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsDLCSupported_Type.__name__=_B
_BrpsDLCSupported_Object=MibScalar
brpsDLCSupported=_BrpsDLCSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,1),_BrpsDLCSupported_Type())
brpsDLCSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCSupported.setStatus(_A)
class _BrpsDLCEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsDLCEnable_Type.__name__=_B
_BrpsDLCEnable_Object=MibScalar
brpsDLCEnable=_BrpsDLCEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,2),_BrpsDLCEnable_Type())
brpsDLCEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsDLCEnable.setStatus(_A)
class _BrpsDLCPrintStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsDLCPrintStatus_Type.__name__=_F
_BrpsDLCPrintStatus_Object=MibScalar
brpsDLCPrintStatus=_BrpsDLCPrintStatus_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,3),_BrpsDLCPrintStatus_Type())
brpsDLCPrintStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCPrintStatus.setStatus(_A)
class _BrpsDLCLLCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsDLCLLCState_Type.__name__=_B
_BrpsDLCLLCState_Object=MibScalar
brpsDLCLLCState=_BrpsDLCLLCState_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,4),_BrpsDLCLLCState_Type())
brpsDLCLLCState.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCLLCState.setStatus(_A)
class _BrpsDLCLLCConnectHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsDLCLLCConnectHost_Type.__name__=_F
_BrpsDLCLLCConnectHost_Object=MibScalar
brpsDLCLLCConnectHost=_BrpsDLCLLCConnectHost_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,5),_BrpsDLCLLCConnectHost_Type())
brpsDLCLLCConnectHost.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCLLCConnectHost.setStatus(_A)
class _BrpsDLCLLCLastIFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsDLCLLCLastIFrame_Type.__name__=_B
_BrpsDLCLLCLastIFrame_Object=MibScalar
brpsDLCLLCLastIFrame=_BrpsDLCLLCLastIFrame_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,6),_BrpsDLCLLCLastIFrame_Type())
brpsDLCLLCLastIFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCLLCLastIFrame.setStatus(_A)
class _BrpsDLCLLCRecvPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrpsDLCLLCRecvPacket_Type.__name__=_B
_BrpsDLCLLCRecvPacket_Object=MibScalar
brpsDLCLLCRecvPacket=_BrpsDLCLLCRecvPacket_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,7),_BrpsDLCLLCRecvPacket_Type())
brpsDLCLLCRecvPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCLLCRecvPacket.setStatus(_A)
class _BrpsDLCLLCPortStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrpsDLCLLCPortStatus_Type.__name__=_F
_BrpsDLCLLCPortStatus_Object=MibScalar
brpsDLCLLCPortStatus=_BrpsDLCLLCPortStatus_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,7,8),_BrpsDLCLLCPortStatus_Type())
brpsDLCLLCPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsDLCLLCPortStatus.setStatus(_A)
_Brnetbeui_ObjectIdentity=ObjectIdentity
brnetbeui=_Brnetbeui_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,8))
class _BrpsNetBEUISupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBEUISupported_Type.__name__=_B
_BrpsNetBEUISupported_Object=MibScalar
brpsNetBEUISupported=_BrpsNetBEUISupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,1),_BrpsNetBEUISupported_Type())
brpsNetBEUISupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetBEUISupported.setStatus(_A)
class _BrpsNetBEUIEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBEUIEnable_Type.__name__=_B
_BrpsNetBEUIEnable_Object=MibScalar
brpsNetBEUIEnable=_BrpsNetBEUIEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,2),_BrpsNetBEUIEnable_Type())
brpsNetBEUIEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBEUIEnable.setStatus(_A)
class _BrpsNetBEUIDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_BrpsNetBEUIDomain_Type.__name__=_F
_BrpsNetBEUIDomain_Object=MibScalar
brpsNetBEUIDomain=_BrpsNetBEUIDomain_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,3),_BrpsNetBEUIDomain_Type())
brpsNetBEUIDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBEUIDomain.setStatus(_A)
class _BrpsNetBIOSIPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBIOSIPSupported_Type.__name__=_B
_BrpsNetBIOSIPSupported_Object=MibScalar
brpsNetBIOSIPSupported=_BrpsNetBIOSIPSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,4),_BrpsNetBIOSIPSupported_Type())
brpsNetBIOSIPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetBIOSIPSupported.setStatus(_A)
class _BrpsNetBIOSIPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBIOSIPEnable_Type.__name__=_B
_BrpsNetBIOSIPEnable_Object=MibScalar
brpsNetBIOSIPEnable=_BrpsNetBIOSIPEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,5),_BrpsNetBIOSIPEnable_Type())
brpsNetBIOSIPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBIOSIPEnable.setStatus(_A)
class _BrpsNetBIOSIPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBIOSIPMethod_Type.__name__=_B
_BrpsNetBIOSIPMethod_Object=MibScalar
brpsNetBIOSIPMethod=_BrpsNetBIOSIPMethod_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,6),_BrpsNetBIOSIPMethod_Type())
brpsNetBIOSIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBIOSIPMethod.setStatus(_A)
_BrpsNetBIOSPrimaryWINSAddr_Type=IpAddress
_BrpsNetBIOSPrimaryWINSAddr_Object=MibScalar
brpsNetBIOSPrimaryWINSAddr=_BrpsNetBIOSPrimaryWINSAddr_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,7),_BrpsNetBIOSPrimaryWINSAddr_Type())
brpsNetBIOSPrimaryWINSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBIOSPrimaryWINSAddr.setStatus(_A)
_BrpsNetBIOSSecondaryWINSAddr_Type=IpAddress
_BrpsNetBIOSSecondaryWINSAddr_Object=MibScalar
brpsNetBIOSSecondaryWINSAddr=_BrpsNetBIOSSecondaryWINSAddr_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,8),_BrpsNetBIOSSecondaryWINSAddr_Type())
brpsNetBIOSSecondaryWINSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNetBIOSSecondaryWINSAddr.setStatus(_A)
class _BrpsNetBIOSPrintingSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNetBIOSPrintingSupported_Type.__name__=_B
_BrpsNetBIOSPrintingSupported_Object=MibScalar
brpsNetBIOSPrintingSupported=_BrpsNetBIOSPrintingSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,8,101),_BrpsNetBIOSPrintingSupported_Type())
brpsNetBIOSPrintingSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNetBIOSPrintingSupported.setStatus(_A)
_Bripp_ObjectIdentity=ObjectIdentity
bripp=_Bripp_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,9))
class _BrpsIPPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsIPPSupported_Type.__name__=_B
_BrpsIPPSupported_Object=MibScalar
brpsIPPSupported=_BrpsIPPSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,9,1),_BrpsIPPSupported_Type())
brpsIPPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsIPPSupported.setStatus(_A)
class _BrpsIPPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsIPPEnable_Type.__name__=_B
_BrpsIPPEnable_Object=MibScalar
brpsIPPEnable=_BrpsIPPEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,9,2),_BrpsIPPEnable_Type())
brpsIPPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsIPPEnable.setStatus(_A)
class _BrIPPRegularPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPPRegularPortEnable_Type.__name__=_B
_BrIPPRegularPortEnable_Object=MibScalar
brIPPRegularPortEnable=_BrIPPRegularPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,9,3),_BrIPPRegularPortEnable_Type())
brIPPRegularPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brIPPRegularPortEnable.setStatus(_A)
class _BrIPPSSLPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPPSSLPortEnable_Type.__name__=_B
_BrIPPSSLPortEnable_Object=MibScalar
brIPPSSLPortEnable=_BrIPPSSLPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,9,4),_BrIPPSSLPortEnable_Type())
brIPPSSLPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brIPPSSLPortEnable.setStatus(_A)
class _BrIPPOriginalPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPPOriginalPortEnable_Type.__name__=_B
_BrIPPOriginalPortEnable_Object=MibScalar
brIPPOriginalPortEnable=_BrIPPOriginalPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,9,5),_BrIPPOriginalPortEnable_Type())
brIPPOriginalPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brIPPOriginalPortEnable.setStatus(_A)
_Brntsend_ObjectIdentity=ObjectIdentity
brntsend=_Brntsend_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,5,10))
class _BrpsNtSendSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNtSendSupported_Type.__name__=_B
_BrpsNtSendSupported_Object=MibScalar
brpsNtSendSupported=_BrpsNtSendSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,10,1),_BrpsNtSendSupported_Type())
brpsNtSendSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsNtSendSupported.setStatus(_A)
class _BrpsNtSendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsNtSendEnable_Type.__name__=_B
_BrpsNtSendEnable_Object=MibScalar
brpsNtSendEnable=_BrpsNtSendEnable_Object((1,3,6,1,4,1,2435,2,4,3,1240,5,10,2),_BrpsNtSendEnable_Type())
brpsNtSendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsNtSendEnable.setStatus(_A)
_Brfirmware_ObjectIdentity=ObjectIdentity
brfirmware=_Brfirmware_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,1240,6))
_BrpsFirmwareIPAddress_Type=IpAddress
_BrpsFirmwareIPAddress_Object=MibScalar
brpsFirmwareIPAddress=_BrpsFirmwareIPAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,1),_BrpsFirmwareIPAddress_Type())
brpsFirmwareIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareIPAddress.setStatus(_A)
_BrpsFirmwareHost_Type=DisplayString
_BrpsFirmwareHost_Object=MibScalar
brpsFirmwareHost=_BrpsFirmwareHost_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,2),_BrpsFirmwareHost_Type())
brpsFirmwareHost.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareHost.setStatus(_A)
_BrpsFirmwareFile_Type=DisplayString
_BrpsFirmwareFile_Object=MibScalar
brpsFirmwareFile=_BrpsFirmwareFile_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,3),_BrpsFirmwareFile_Type())
brpsFirmwareFile.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareFile.setStatus(_A)
class _BrpsFirmwareReload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsFirmwareReload_Type.__name__=_B
_BrpsFirmwareReload_Object=MibScalar
brpsFirmwareReload=_BrpsFirmwareReload_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,4),_BrpsFirmwareReload_Type())
brpsFirmwareReload.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareReload.setStatus(_A)
_BrpsFirmwareDescription_Type=DisplayString
_BrpsFirmwareDescription_Object=MibScalar
brpsFirmwareDescription=_BrpsFirmwareDescription_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,5),_BrpsFirmwareDescription_Type())
brpsFirmwareDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsFirmwareDescription.setStatus(_A)
class _BrpsFirmwareXModem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsFirmwareXModem_Type.__name__=_B
_BrpsFirmwareXModem_Object=MibScalar
brpsFirmwareXModem=_BrpsFirmwareXModem_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,6),_BrpsFirmwareXModem_Type())
brpsFirmwareXModem.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareXModem.setStatus(_A)
class _BrpsFirmwareAdvancedAddressSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrpsFirmwareAdvancedAddressSupported_Type.__name__=_B
_BrpsFirmwareAdvancedAddressSupported_Object=MibScalar
brpsFirmwareAdvancedAddressSupported=_BrpsFirmwareAdvancedAddressSupported_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,7),_BrpsFirmwareAdvancedAddressSupported_Type())
brpsFirmwareAdvancedAddressSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsFirmwareAdvancedAddressSupported.setStatus(_A)
class _BrpsFirmwareAdvancedAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrpsFirmwareAdvancedAddress_Type.__name__=_F
_BrpsFirmwareAdvancedAddress_Object=MibScalar
brpsFirmwareAdvancedAddress=_BrpsFirmwareAdvancedAddress_Object((1,3,6,1,4,1,2435,2,4,3,1240,6,8),_BrpsFirmwareAdvancedAddress_Type())
brpsFirmwareAdvancedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brpsFirmwareAdvancedAddress.setStatus(_A)
_BrnetConfigOpt_ObjectIdentity=ObjectIdentity
brnetConfigOpt=_BrnetConfigOpt_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435))
_Broriginalprotocol_ObjectIdentity=ObjectIdentity
broriginalprotocol=_Broriginalprotocol_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5))
_Broriginaltcpip_ObjectIdentity=ObjectIdentity
broriginaltcpip=_Broriginaltcpip_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,2))
class _BrLPDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_BrLPDType_Type.__name__=_B
_BrLPDType_Object=MibScalar
brLPDType=_BrLPDType_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,2,1),_BrLPDType_Type())
brLPDType.setMaxAccess(_C)
if mibBuilder.loadTexts:brLPDType.setStatus(_A)
_Broriginalftp_ObjectIdentity=ObjectIdentity
broriginalftp=_Broriginalftp_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,10))
class _BrFTPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFTPSupported_Type.__name__=_B
_BrFTPSupported_Object=MibScalar
brFTPSupported=_BrFTPSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,10,1),_BrFTPSupported_Type())
brFTPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brFTPSupported.setStatus(_A)
class _BrFTPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrFTPEnable_Type.__name__=_B
_BrFTPEnable_Object=MibScalar
brFTPEnable=_BrFTPEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,10,2),_BrFTPEnable_Type())
brFTPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brFTPEnable.setStatus(_A)
_Broriginalupnp_ObjectIdentity=ObjectIdentity
broriginalupnp=_Broriginalupnp_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,11))
class _BrUPnPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrUPnPSupported_Type.__name__=_B
_BrUPnPSupported_Object=MibScalar
brUPnPSupported=_BrUPnPSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,11,1),_BrUPnPSupported_Type())
brUPnPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brUPnPSupported.setStatus(_A)
class _BrUPnPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrUPnPEnable_Type.__name__=_B
_BrUPnPEnable_Object=MibScalar
brUPnPEnable=_BrUPnPEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,11,2),_BrUPnPEnable_Type())
brUPnPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brUPnPEnable.setStatus(_A)
_Broriginalapipa_ObjectIdentity=ObjectIdentity
broriginalapipa=_Broriginalapipa_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,12))
class _BrAPIPASupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrAPIPASupported_Type.__name__=_B
_BrAPIPASupported_Object=MibScalar
brAPIPASupported=_BrAPIPASupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,12,1),_BrAPIPASupported_Type())
brAPIPASupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brAPIPASupported.setStatus(_A)
class _BrAPIPAEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrAPIPAEnable_Type.__name__=_B
_BrAPIPAEnable_Object=MibScalar
brAPIPAEnable=_BrAPIPAEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,12,2),_BrAPIPAEnable_Type())
brAPIPAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brAPIPAEnable.setStatus(_A)
_Broriginalmdns_ObjectIdentity=ObjectIdentity
broriginalmdns=_Broriginalmdns_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,13))
class _BrmDNSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrmDNSSupported_Type.__name__=_B
_BrmDNSSupported_Object=MibScalar
brmDNSSupported=_BrmDNSSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,13,1),_BrmDNSSupported_Type())
brmDNSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brmDNSSupported.setStatus(_A)
class _BrmDNSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrmDNSEnable_Type.__name__=_B
_BrmDNSEnable_Object=MibScalar
brmDNSEnable=_BrmDNSEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,13,2),_BrmDNSEnable_Type())
brmDNSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brmDNSEnable.setStatus(_A)
class _BrmDNSPrinterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrmDNSPrinterName_Type.__name__=_F
_BrmDNSPrinterName_Object=MibScalar
brmDNSPrinterName=_BrmDNSPrinterName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,13,3),_BrmDNSPrinterName_Type())
brmDNSPrinterName.setMaxAccess(_C)
if mibBuilder.loadTexts:brmDNSPrinterName.setStatus(_A)
_BroriginalLAA_ObjectIdentity=ObjectIdentity
broriginalLAA=_BroriginalLAA_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,14))
class _BrLAASupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLAASupported_Type.__name__=_B
_BrLAASupported_Object=MibScalar
brLAASupported=_BrLAASupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,14,1),_BrLAASupported_Type())
brLAASupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brLAASupported.setStatus(_A)
class _BrLAAMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_BrLAAMacAddress_Type.__name__=_G
_BrLAAMacAddress_Object=MibScalar
brLAAMacAddress=_BrLAAMacAddress_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,14,2),_BrLAAMacAddress_Type())
brLAAMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brLAAMacAddress.setStatus(_A)
_BroriginalIPv6_ObjectIdentity=ObjectIdentity
broriginalIPv6=_BroriginalIPv6_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,15))
class _BrIPv6Supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPv6Supported_Type.__name__=_B
_BrIPv6Supported_Object=MibScalar
brIPv6Supported=_BrIPv6Supported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,15,1),_BrIPv6Supported_Type())
brIPv6Supported.setMaxAccess(_D)
if mibBuilder.loadTexts:brIPv6Supported.setStatus(_A)
class _BrIPv6Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPv6Enable_Type.__name__=_B
_BrIPv6Enable_Object=MibScalar
brIPv6Enable=_BrIPv6Enable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,15,2),_BrIPv6Enable_Type())
brIPv6Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:brIPv6Enable.setStatus(_A)
class _BrIPv6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrIPv6Priority_Type.__name__=_B
_BrIPv6Priority_Object=MibScalar
brIPv6Priority=_BrIPv6Priority_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,15,3),_BrIPv6Priority_Type())
brIPv6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:brIPv6Priority.setStatus(_A)
_Broriginaltelnet_ObjectIdentity=ObjectIdentity
broriginaltelnet=_Broriginaltelnet_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,16))
class _BrtelnetSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrtelnetSupported_Type.__name__=_B
_BrtelnetSupported_Object=MibScalar
brtelnetSupported=_BrtelnetSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,16,1),_BrtelnetSupported_Type())
brtelnetSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brtelnetSupported.setStatus(_A)
class _BrtelnetEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrtelnetEnable_Type.__name__=_B
_BrtelnetEnable_Object=MibScalar
brtelnetEnable=_BrtelnetEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,16,2),_BrtelnetEnable_Type())
brtelnetEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brtelnetEnable.setStatus(_A)
_BroriginalEWS_ObjectIdentity=ObjectIdentity
broriginalEWS=_BroriginalEWS_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,17))
class _BrEWSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrEWSSupported_Type.__name__=_B
_BrEWSSupported_Object=MibScalar
brEWSSupported=_BrEWSSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,17,1),_BrEWSSupported_Type())
brEWSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brEWSSupported.setStatus(_A)
class _BrEWSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrEWSEnable_Type.__name__=_B
_BrEWSEnable_Object=MibScalar
brEWSEnable=_BrEWSEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,17,2),_BrEWSEnable_Type())
brEWSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brEWSEnable.setStatus(_A)
class _BrEWSRegularPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrEWSRegularPortEnable_Type.__name__=_B
_BrEWSRegularPortEnable_Object=MibScalar
brEWSRegularPortEnable=_BrEWSRegularPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,17,3),_BrEWSRegularPortEnable_Type())
brEWSRegularPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brEWSRegularPortEnable.setStatus(_A)
class _BrEWSSSLPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrEWSSSLPortEnable_Type.__name__=_B
_BrEWSSSLPortEnable_Object=MibScalar
brEWSSSLPortEnable=_BrEWSSSLPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,17,4),_BrEWSSSLPortEnable_Type())
brEWSSSLPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brEWSSSLPortEnable.setStatus(_A)
_BroriginalSNMP_ObjectIdentity=ObjectIdentity
broriginalSNMP=_BroriginalSNMP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,18))
class _BrSNMPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrSNMPSupported_Type.__name__=_B
_BrSNMPSupported_Object=MibScalar
brSNMPSupported=_BrSNMPSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,1),_BrSNMPSupported_Type())
brSNMPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brSNMPSupported.setStatus(_A)
class _BrSNMPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrSNMPEnable_Type.__name__=_B
_BrSNMPEnable_Object=MibScalar
brSNMPEnable=_BrSNMPEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,2),_BrSNMPEnable_Type())
brSNMPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPEnable.setStatus(_A)
class _BrSNMPV3Supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrSNMPV3Supported_Type.__name__=_B
_BrSNMPV3Supported_Object=MibScalar
brSNMPV3Supported=_BrSNMPV3Supported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,10),_BrSNMPV3Supported_Type())
brSNMPV3Supported.setMaxAccess(_D)
if mibBuilder.loadTexts:brSNMPV3Supported.setStatus(_A)
class _BrSNMPCommMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_BrSNMPCommMode_Type.__name__=_B
_BrSNMPCommMode_Object=MibScalar
brSNMPCommMode=_BrSNMPCommMode_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,11),_BrSNMPCommMode_Type())
brSNMPCommMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPCommMode.setStatus(_A)
class _BrSNMPV3UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrSNMPV3UserName_Type.__name__=_F
_BrSNMPV3UserName_Object=MibScalar
brSNMPV3UserName=_BrSNMPV3UserName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,12),_BrSNMPV3UserName_Type())
brSNMPV3UserName.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3UserName.setStatus(_A)
class _BrSNMPV3KeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_BrSNMPV3KeyType_Type.__name__=_B
_BrSNMPV3KeyType_Object=MibScalar
brSNMPV3KeyType=_BrSNMPV3KeyType_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,13),_BrSNMPV3KeyType_Type())
brSNMPV3KeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3KeyType.setStatus(_A)
class _BrSNMPV3AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BrSNMPV3AuthKey_Type.__name__=_G
_BrSNMPV3AuthKey_Object=MibScalar
brSNMPV3AuthKey=_BrSNMPV3AuthKey_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,14),_BrSNMPV3AuthKey_Type())
brSNMPV3AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3AuthKey.setStatus(_A)
class _BrSNMPV3AuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_BrSNMPV3AuthPassword_Type.__name__=_F
_BrSNMPV3AuthPassword_Object=MibScalar
brSNMPV3AuthPassword=_BrSNMPV3AuthPassword_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,15),_BrSNMPV3AuthPassword_Type())
brSNMPV3AuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3AuthPassword.setStatus(_A)
class _BrSNMPV3PrivKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BrSNMPV3PrivKey_Type.__name__=_G
_BrSNMPV3PrivKey_Object=MibScalar
brSNMPV3PrivKey=_BrSNMPV3PrivKey_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,16),_BrSNMPV3PrivKey_Type())
brSNMPV3PrivKey.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3PrivKey.setStatus(_A)
class _BrSNMPV3PrivPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_BrSNMPV3PrivPassword_Type.__name__=_F
_BrSNMPV3PrivPassword_Object=MibScalar
brSNMPV3PrivPassword=_BrSNMPV3PrivPassword_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,17),_BrSNMPV3PrivPassword_Type())
brSNMPV3PrivPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3PrivPassword.setStatus(_A)
class _BrSNMPV3ContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrSNMPV3ContextName_Type.__name__=_F
_BrSNMPV3ContextName_Object=MibScalar
brSNMPV3ContextName=_BrSNMPV3ContextName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,18,18),_BrSNMPV3ContextName_Type())
brSNMPV3ContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNMPV3ContextName.setStatus(_A)
_Broriginalldap_ObjectIdentity=ObjectIdentity
broriginalldap=_Broriginalldap_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,19))
class _BrLdapSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapSupported_Type.__name__=_B
_BrLdapSupported_Object=MibScalar
brLdapSupported=_BrLdapSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,1),_BrLdapSupported_Type())
brLdapSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapSupported.setStatus(_A)
class _BrLdapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapEnable_Type.__name__=_B
_BrLdapEnable_Object=MibScalar
brLdapEnable=_BrLdapEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,2),_BrLdapEnable_Type())
brLdapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapEnable.setStatus(_A)
class _BrLdapTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_BrLdapTimeout_Type.__name__=_B
_BrLdapTimeout_Object=MibScalar
brLdapTimeout=_BrLdapTimeout_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,3),_BrLdapTimeout_Type())
brLdapTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapTimeout.setStatus(_A)
class _BrLdapTimeoutSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapTimeoutSupported_Type.__name__=_B
_BrLdapTimeoutSupported_Object=MibScalar
brLdapTimeoutSupported=_BrLdapTimeoutSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,4),_BrLdapTimeoutSupported_Type())
brLdapTimeoutSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapTimeoutSupported.setStatus(_A)
_BrLdapServerCount_Type=Integer32
_BrLdapServerCount_Object=MibScalar
brLdapServerCount=_BrLdapServerCount_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,11),_BrLdapServerCount_Type())
brLdapServerCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapServerCount.setStatus(_A)
_BrLdapServerInfoTable_Object=MibTable
brLdapServerInfoTable=_BrLdapServerInfoTable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12))
if mibBuilder.loadTexts:brLdapServerInfoTable.setStatus(_A)
_BrLdapServerInfoEntry_Object=MibTableRow
brLdapServerInfoEntry=_BrLdapServerInfoEntry_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1))
brLdapServerInfoEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:brLdapServerInfoEntry.setStatus(_A)
class _BrLdapServerInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerInfoIndex_Type.__name__=_B
_BrLdapServerInfoIndex_Object=MibTableColumn
brLdapServerInfoIndex=_BrLdapServerInfoIndex_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,1),_BrLdapServerInfoIndex_Type())
brLdapServerInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapServerInfoIndex.setStatus(_A)
class _BrLdapServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerName_Type.__name__=_F
_BrLdapServerName_Object=MibTableColumn
brLdapServerName=_BrLdapServerName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,2),_BrLdapServerName_Type())
brLdapServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerName.setStatus(_A)
class _BrLdapServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrLdapServerPort_Type.__name__=_B
_BrLdapServerPort_Object=MibTableColumn
brLdapServerPort=_BrLdapServerPort_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,3),_BrLdapServerPort_Type())
brLdapServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerPort.setStatus(_A)
class _BrLdapServerAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('anonymous',1),('simple',2),('kerberos',3)))
_BrLdapServerAuth_Type.__name__=_B
_BrLdapServerAuth_Object=MibTableColumn
brLdapServerAuth=_BrLdapServerAuth_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,4),_BrLdapServerAuth_Type())
brLdapServerAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAuth.setStatus(_A)
class _BrLdapServerUserDN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrLdapServerUserDN_Type.__name__=_G
_BrLdapServerUserDN_Object=MibTableColumn
brLdapServerUserDN=_BrLdapServerUserDN_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,5),_BrLdapServerUserDN_Type())
brLdapServerUserDN.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerUserDN.setStatus(_A)
class _BrLdapServerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BrLdapServerPassword_Type.__name__=_G
_BrLdapServerPassword_Object=MibTableColumn
brLdapServerPassword=_BrLdapServerPassword_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,6),_BrLdapServerPassword_Type())
brLdapServerPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerPassword.setStatus(_A)
class _BrLdapServerPasswordSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerPasswordSet_Type.__name__=_B
_BrLdapServerPasswordSet_Object=MibTableColumn
brLdapServerPasswordSet=_BrLdapServerPasswordSet_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,7),_BrLdapServerPasswordSet_Type())
brLdapServerPasswordSet.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapServerPasswordSet.setStatus(_A)
class _BrLdapServerBaseDN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrLdapServerBaseDN_Type.__name__=_G
_BrLdapServerBaseDN_Object=MibTableColumn
brLdapServerBaseDN=_BrLdapServerBaseDN_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,8),_BrLdapServerBaseDN_Type())
brLdapServerBaseDN.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerBaseDN.setStatus(_A)
class _BrLdapServerAttrEMail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrEMail_Type.__name__=_F
_BrLdapServerAttrEMail_Object=MibTableColumn
brLdapServerAttrEMail=_BrLdapServerAttrEMail_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,10),_BrLdapServerAttrEMail_Type())
brLdapServerAttrEMail.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrEMail.setStatus(_A)
class _BrLdapServerAttrFAXNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrFAXNumber_Type.__name__=_F
_BrLdapServerAttrFAXNumber_Object=MibTableColumn
brLdapServerAttrFAXNumber=_BrLdapServerAttrFAXNumber_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,11),_BrLdapServerAttrFAXNumber_Type())
brLdapServerAttrFAXNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrFAXNumber.setStatus(_A)
class _BrLdapServerAttrDetail1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrDetail1_Type.__name__=_F
_BrLdapServerAttrDetail1_Object=MibTableColumn
brLdapServerAttrDetail1=_BrLdapServerAttrDetail1_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,12),_BrLdapServerAttrDetail1_Type())
brLdapServerAttrDetail1.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetail1.setStatus(_A)
class _BrLdapServerAttrDetail2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrDetail2_Type.__name__=_F
_BrLdapServerAttrDetail2_Object=MibTableColumn
brLdapServerAttrDetail2=_BrLdapServerAttrDetail2_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,13),_BrLdapServerAttrDetail2_Type())
brLdapServerAttrDetail2.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetail2.setStatus(_A)
class _BrLdapServerAttrDetail3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrDetail3_Type.__name__=_F
_BrLdapServerAttrDetail3_Object=MibTableColumn
brLdapServerAttrDetail3=_BrLdapServerAttrDetail3_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,14),_BrLdapServerAttrDetail3_Type())
brLdapServerAttrDetail3.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetail3.setStatus(_A)
class _BrLdapServerAttrDetail4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrDetail4_Type.__name__=_F
_BrLdapServerAttrDetail4_Object=MibTableColumn
brLdapServerAttrDetail4=_BrLdapServerAttrDetail4_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,15),_BrLdapServerAttrDetail4_Type())
brLdapServerAttrDetail4.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetail4.setStatus(_A)
class _BrLdapServerAttrDetailEnable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerAttrDetailEnable1_Type.__name__=_B
_BrLdapServerAttrDetailEnable1_Object=MibTableColumn
brLdapServerAttrDetailEnable1=_BrLdapServerAttrDetailEnable1_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,16),_BrLdapServerAttrDetailEnable1_Type())
brLdapServerAttrDetailEnable1.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetailEnable1.setStatus(_A)
class _BrLdapServerAttrDetailEnable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerAttrDetailEnable2_Type.__name__=_B
_BrLdapServerAttrDetailEnable2_Object=MibTableColumn
brLdapServerAttrDetailEnable2=_BrLdapServerAttrDetailEnable2_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,17),_BrLdapServerAttrDetailEnable2_Type())
brLdapServerAttrDetailEnable2.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetailEnable2.setStatus(_A)
class _BrLdapServerAttrDetailEnable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerAttrDetailEnable3_Type.__name__=_B
_BrLdapServerAttrDetailEnable3_Object=MibTableColumn
brLdapServerAttrDetailEnable3=_BrLdapServerAttrDetailEnable3_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,18),_BrLdapServerAttrDetailEnable3_Type())
brLdapServerAttrDetailEnable3.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetailEnable3.setStatus(_A)
class _BrLdapServerAttrDetailEnable4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLdapServerAttrDetailEnable4_Type.__name__=_B
_BrLdapServerAttrDetailEnable4_Object=MibTableColumn
brLdapServerAttrDetailEnable4=_BrLdapServerAttrDetailEnable4_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,19),_BrLdapServerAttrDetailEnable4_Type())
brLdapServerAttrDetailEnable4.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrDetailEnable4.setStatus(_A)
class _BrLdapKerberosServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapKerberosServerName_Type.__name__=_F
_BrLdapKerberosServerName_Object=MibTableColumn
brLdapKerberosServerName=_BrLdapKerberosServerName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,20),_BrLdapKerberosServerName_Type())
brLdapKerberosServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapKerberosServerName.setStatus(_A)
class _BrLdapKerberosServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrLdapKerberosServerPort_Type.__name__=_B
_BrLdapKerberosServerPort_Object=MibTableColumn
brLdapKerberosServerPort=_BrLdapKerberosServerPort_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,12,1,21),_BrLdapKerberosServerPort_Type())
brLdapKerberosServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapKerberosServerPort.setStatus(_A)
_BrLdapServerAttrNameCount_Type=Integer32
_BrLdapServerAttrNameCount_Object=MibScalar
brLdapServerAttrNameCount=_BrLdapServerAttrNameCount_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,21),_BrLdapServerAttrNameCount_Type())
brLdapServerAttrNameCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapServerAttrNameCount.setStatus(_A)
_BrLdapServerAttrNameTable_Object=MibTable
brLdapServerAttrNameTable=_BrLdapServerAttrNameTable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,22))
if mibBuilder.loadTexts:brLdapServerAttrNameTable.setStatus(_A)
_BrLdapServerAttrNameEntry_Object=MibTableRow
brLdapServerAttrNameEntry=_BrLdapServerAttrNameEntry_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,22,1))
brLdapServerAttrNameEntry.setIndexNames((0,_E,_AM),(0,_E,_B8))
if mibBuilder.loadTexts:brLdapServerAttrNameEntry.setStatus(_A)
class _BrLdapServerAttrNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrLdapServerAttrNameIndex_Type.__name__=_B
_BrLdapServerAttrNameIndex_Object=MibTableColumn
brLdapServerAttrNameIndex=_BrLdapServerAttrNameIndex_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,22,1,1),_BrLdapServerAttrNameIndex_Type())
brLdapServerAttrNameIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brLdapServerAttrNameIndex.setStatus(_A)
class _BrLdapServerAttrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrLdapServerAttrName_Type.__name__=_F
_BrLdapServerAttrName_Object=MibTableColumn
brLdapServerAttrName=_BrLdapServerAttrName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,22,1,2),_BrLdapServerAttrName_Type())
brLdapServerAttrName.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapServerAttrName.setStatus(_A)
class _BrLdapSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrLdapSetDefault_Type.__name__=_B
_BrLdapSetDefault_Object=MibScalar
brLdapSetDefault=_BrLdapSetDefault_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,19,99),_BrLdapSetDefault_Type())
brLdapSetDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:brLdapSetDefault.setStatus(_A)
_BroriginalTFTP_ObjectIdentity=ObjectIdentity
broriginalTFTP=_BroriginalTFTP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,20))
class _BrTFTPSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrTFTPSupported_Type.__name__=_B
_BrTFTPSupported_Object=MibScalar
brTFTPSupported=_BrTFTPSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,20,1),_BrTFTPSupported_Type())
brTFTPSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brTFTPSupported.setStatus(_A)
class _BrTFTPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrTFTPEnable_Type.__name__=_B
_BrTFTPEnable_Object=MibScalar
brTFTPEnable=_BrTFTPEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,20,2),_BrTFTPEnable_Type())
brTFTPEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brTFTPEnable.setStatus(_A)
_BroriginalHTTPS_ObjectIdentity=ObjectIdentity
broriginalHTTPS=_BroriginalHTTPS_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,21))
class _BrHTTPSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrHTTPSSupported_Type.__name__=_B
_BrHTTPSSupported_Object=MibScalar
brHTTPSSupported=_BrHTTPSSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,21,1),_BrHTTPSSupported_Type())
brHTTPSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brHTTPSSupported.setStatus(_A)
class _BrHTTPSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrHTTPSEnable_Type.__name__=_B
_BrHTTPSEnable_Object=MibScalar
brHTTPSEnable=_BrHTTPSEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,21,2),_BrHTTPSEnable_Type())
brHTTPSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brHTTPSEnable.setStatus(_A)
_BroriginalLPD_ObjectIdentity=ObjectIdentity
broriginalLPD=_BroriginalLPD_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,22))
class _BrLPDSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLPDSupported_Type.__name__=_B
_BrLPDSupported_Object=MibScalar
brLPDSupported=_BrLPDSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,22,1),_BrLPDSupported_Type())
brLPDSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brLPDSupported.setStatus(_A)
class _BrLPDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLPDEnable_Type.__name__=_B
_BrLPDEnable_Object=MibScalar
brLPDEnable=_BrLPDEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,22,2),_BrLPDEnable_Type())
brLPDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brLPDEnable.setStatus(_A)
_BroriginalRawPort_ObjectIdentity=ObjectIdentity
broriginalRawPort=_BroriginalRawPort_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,23))
class _BrRawPortSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrRawPortSupported_Type.__name__=_B
_BrRawPortSupported_Object=MibScalar
brRawPortSupported=_BrRawPortSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,23,1),_BrRawPortSupported_Type())
brRawPortSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brRawPortSupported.setStatus(_A)
class _BrRawPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrRawPortEnable_Type.__name__=_B
_BrRawPortEnable_Object=MibScalar
brRawPortEnable=_BrRawPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,23,2),_BrRawPortEnable_Type())
brRawPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brRawPortEnable.setStatus(_A)
_BroriginalLLTD_ObjectIdentity=ObjectIdentity
broriginalLLTD=_BroriginalLLTD_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,24))
class _BrLLTDSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLLTDSupported_Type.__name__=_B
_BrLLTDSupported_Object=MibScalar
brLLTDSupported=_BrLLTDSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,24,1),_BrLLTDSupported_Type())
brLLTDSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brLLTDSupported.setStatus(_A)
class _BrLLTDEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLLTDEnable_Type.__name__=_B
_BrLLTDEnable_Object=MibScalar
brLLTDEnable=_BrLLTDEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,24,2),_BrLLTDEnable_Type())
brLLTDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brLLTDEnable.setStatus(_A)
_BroriginalWebServices_ObjectIdentity=ObjectIdentity
broriginalWebServices=_BroriginalWebServices_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,25))
class _BrWebServicesSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrWebServicesSupported_Type.__name__=_B
_BrWebServicesSupported_Object=MibScalar
brWebServicesSupported=_BrWebServicesSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,25,1),_BrWebServicesSupported_Type())
brWebServicesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brWebServicesSupported.setStatus(_A)
class _BrWebServicesEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrWebServicesEnable_Type.__name__=_B
_BrWebServicesEnable_Object=MibScalar
brWebServicesEnable=_BrWebServicesEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,25,2),_BrWebServicesEnable_Type())
brWebServicesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brWebServicesEnable.setStatus(_A)
class _BrWebServicesRegularPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrWebServicesRegularPortEnable_Type.__name__=_B
_BrWebServicesRegularPortEnable_Object=MibScalar
brWebServicesRegularPortEnable=_BrWebServicesRegularPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,25,3),_BrWebServicesRegularPortEnable_Type())
brWebServicesRegularPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brWebServicesRegularPortEnable.setStatus(_A)
class _BrWebServicesSSLPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrWebServicesSSLPortEnable_Type.__name__=_B
_BrWebServicesSSLPortEnable_Object=MibScalar
brWebServicesSSLPortEnable=_BrWebServicesSSLPortEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,25,4),_BrWebServicesSSLPortEnable_Type())
brWebServicesSSLPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brWebServicesSSLPortEnable.setStatus(_A)
_BroriginalLLMNR_ObjectIdentity=ObjectIdentity
broriginalLLMNR=_BroriginalLLMNR_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,26))
class _BrLLMNREnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrLLMNREnable_Type.__name__=_B
_BrLLMNREnable_Object=MibScalar
brLLMNREnable=_BrLLMNREnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,26,1),_BrLLMNREnable_Type())
brLLMNREnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brLLMNREnable.setStatus(_A)
_BroriginalKerberos_ObjectIdentity=ObjectIdentity
broriginalKerberos=_BroriginalKerberos_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,27))
class _BrKerberosSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrKerberosSupported_Type.__name__=_B
_BrKerberosSupported_Object=MibScalar
brKerberosSupported=_BrKerberosSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,27,1),_BrKerberosSupported_Type())
brKerberosSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brKerberosSupported.setStatus(_A)
_BroriginalCIFS_ObjectIdentity=ObjectIdentity
broriginalCIFS=_BroriginalCIFS_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,28))
class _BrCIFSSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrCIFSSupported_Type.__name__=_B
_BrCIFSSupported_Object=MibScalar
brCIFSSupported=_BrCIFSSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,28,1),_BrCIFSSupported_Type())
brCIFSSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brCIFSSupported.setStatus(_A)
class _BrCIFSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrCIFSEnable_Type.__name__=_B
_BrCIFSEnable_Object=MibScalar
brCIFSEnable=_BrCIFSEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,28,2),_BrCIFSEnable_Type())
brCIFSEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brCIFSEnable.setStatus(_A)
_BroriginalSNTP_ObjectIdentity=ObjectIdentity
broriginalSNTP=_BroriginalSNTP_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,29))
class _BrSNTPCSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrSNTPCSupported_Type.__name__=_B
_BrSNTPCSupported_Object=MibScalar
brSNTPCSupported=_BrSNTPCSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,1),_BrSNTPCSupported_Type())
brSNTPCSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brSNTPCSupported.setStatus(_A)
class _BrSNTPCEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrSNTPCEnable_Type.__name__=_B
_BrSNTPCEnable_Object=MibScalar
brSNTPCEnable=_BrSNTPCEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,2),_BrSNTPCEnable_Type())
brSNTPCEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCEnable.setStatus(_A)
class _BrSNTPCServerMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_BrSNTPCServerMethod_Type.__name__=_B
_BrSNTPCServerMethod_Object=MibScalar
brSNTPCServerMethod=_BrSNTPCServerMethod_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,3),_BrSNTPCServerMethod_Type())
brSNTPCServerMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCServerMethod.setStatus(_A)
class _BrSNTPCSyncMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_BrSNTPCSyncMethod_Type.__name__=_B
_BrSNTPCSyncMethod_Object=MibScalar
brSNTPCSyncMethod=_BrSNTPCSyncMethod_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,4),_BrSNTPCSyncMethod_Type())
brSNTPCSyncMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCSyncMethod.setStatus(_A)
class _BrSNTPCIntervalMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_BrSNTPCIntervalMin_Type.__name__=_B
_BrSNTPCIntervalMin_Object=MibScalar
brSNTPCIntervalMin=_BrSNTPCIntervalMin_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,5),_BrSNTPCIntervalMin_Type())
brSNTPCIntervalMin.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCIntervalMin.setStatus(_A)
class _BrSNTPCInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_BrSNTPCInterval_Type.__name__=_B
_BrSNTPCInterval_Object=MibScalar
brSNTPCInterval=_BrSNTPCInterval_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,6),_BrSNTPCInterval_Type())
brSNTPCInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCInterval.setStatus(_A)
class _BrSNTPCSyncResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrSNTPCSyncResult_Type.__name__=_B
_BrSNTPCSyncResult_Object=MibScalar
brSNTPCSyncResult=_BrSNTPCSyncResult_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,7),_BrSNTPCSyncResult_Type())
brSNTPCSyncResult.setMaxAccess(_D)
if mibBuilder.loadTexts:brSNTPCSyncResult.setStatus(_A)
class _BrSNTPCPrimaryServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrSNTPCPrimaryServerName_Type.__name__=_F
_BrSNTPCPrimaryServerName_Object=MibScalar
brSNTPCPrimaryServerName=_BrSNTPCPrimaryServerName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,8),_BrSNTPCPrimaryServerName_Type())
brSNTPCPrimaryServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCPrimaryServerName.setStatus(_A)
class _BrSNTPCPrimaryServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrSNTPCPrimaryServerPort_Type.__name__=_B
_BrSNTPCPrimaryServerPort_Object=MibScalar
brSNTPCPrimaryServerPort=_BrSNTPCPrimaryServerPort_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,9),_BrSNTPCPrimaryServerPort_Type())
brSNTPCPrimaryServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCPrimaryServerPort.setStatus(_A)
class _BrSNTPCSecondaryServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrSNTPCSecondaryServerName_Type.__name__=_F
_BrSNTPCSecondaryServerName_Object=MibScalar
brSNTPCSecondaryServerName=_BrSNTPCSecondaryServerName_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,10),_BrSNTPCSecondaryServerName_Type())
brSNTPCSecondaryServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCSecondaryServerName.setStatus(_A)
class _BrSNTPCSecondaryServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrSNTPCSecondaryServerPort_Type.__name__=_B
_BrSNTPCSecondaryServerPort_Object=MibScalar
brSNTPCSecondaryServerPort=_BrSNTPCSecondaryServerPort_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,29,11),_BrSNTPCSecondaryServerPort_Type())
brSNTPCSecondaryServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brSNTPCSecondaryServerPort.setStatus(_A)
_BroriginalSecurity_ObjectIdentity=ObjectIdentity
broriginalSecurity=_BroriginalSecurity_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,100))
_BrSecurityGeneralStatus_ObjectIdentity=ObjectIdentity
brSecurityGeneralStatus=_BrSecurityGeneralStatus_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,100,1))
class _BrDeviceNegotiationEncryptVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrDeviceNegotiationEncryptVer_Type.__name__=_B
_BrDeviceNegotiationEncryptVer_Object=MibScalar
brDeviceNegotiationEncryptVer=_BrDeviceNegotiationEncryptVer_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,100,1,1),_BrDeviceNegotiationEncryptVer_Type())
brDeviceNegotiationEncryptVer.setMaxAccess(_D)
if mibBuilder.loadTexts:brDeviceNegotiationEncryptVer.setStatus(_A)
_BrpsServerCertificateNum_Type=Integer32
_BrpsServerCertificateNum_Object=MibScalar
brpsServerCertificateNum=_BrpsServerCertificateNum_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,100,1,2),_BrpsServerCertificateNum_Type())
brpsServerCertificateNum.setMaxAccess(_D)
if mibBuilder.loadTexts:brpsServerCertificateNum.setStatus(_A)
_BrSecurityGeneralSetup_ObjectIdentity=ObjectIdentity
brSecurityGeneralSetup=_BrSecurityGeneralSetup_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,100,2))
_BrSecurityDeviceNegotiation_ObjectIdentity=ObjectIdentity
brSecurityDeviceNegotiation=_BrSecurityDeviceNegotiation_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,5,100,10))
class _BrDeviceNegotiationGetChallenge_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_BrDeviceNegotiationGetChallenge_Type.__name__=_G
_BrDeviceNegotiationGetChallenge_Object=MibScalar
brDeviceNegotiationGetChallenge=_BrDeviceNegotiationGetChallenge_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,100,10,1),_BrDeviceNegotiationGetChallenge_Type())
brDeviceNegotiationGetChallenge.setMaxAccess(_D)
if mibBuilder.loadTexts:brDeviceNegotiationGetChallenge.setStatus(_A)
class _BrDeviceNegotiationConfirmPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(60,60));fixedLength=60
_BrDeviceNegotiationConfirmPassword_Type.__name__=_G
_BrDeviceNegotiationConfirmPassword_Object=MibScalar
brDeviceNegotiationConfirmPassword=_BrDeviceNegotiationConfirmPassword_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,100,10,2),_BrDeviceNegotiationConfirmPassword_Type())
brDeviceNegotiationConfirmPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brDeviceNegotiationConfirmPassword.setStatus(_A)
class _BrDeviceNegotiationChangePassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(48,48));fixedLength=48
_BrDeviceNegotiationChangePassword_Type.__name__=_G
_BrDeviceNegotiationChangePassword_Object=MibScalar
brDeviceNegotiationChangePassword=_BrDeviceNegotiationChangePassword_Object((1,3,6,1,4,1,2435,2,4,3,2435,5,100,10,3),_BrDeviceNegotiationChangePassword_Type())
brDeviceNegotiationChangePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:brDeviceNegotiationChangePassword.setStatus(_A)
_Broriginalinternetsetting_ObjectIdentity=ObjectIdentity
broriginalinternetsetting=_Broriginalinternetsetting_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,10))
_Broriginalproxy_ObjectIdentity=ObjectIdentity
broriginalproxy=_Broriginalproxy_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,10,1))
class _BrProxySupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrProxySupported_Type.__name__=_B
_BrProxySupported_Object=MibScalar
brProxySupported=_BrProxySupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,1),_BrProxySupported_Type())
brProxySupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brProxySupported.setStatus(_A)
class _BrProxyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrProxyEnable_Type.__name__=_B
_BrProxyEnable_Object=MibScalar
brProxyEnable=_BrProxyEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,2),_BrProxyEnable_Type())
brProxyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brProxyEnable.setStatus(_A)
class _BrProxyBypassServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_v,2)))
_BrProxyBypassServer_Type.__name__=_B
_BrProxyBypassServer_Object=MibScalar
brProxyBypassServer=_BrProxyBypassServer_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,3),_BrProxyBypassServer_Type())
brProxyBypassServer.setMaxAccess(_C)
if mibBuilder.loadTexts:brProxyBypassServer.setStatus(_A)
_BrProxyServerCount_Type=Integer32
_BrProxyServerCount_Object=MibScalar
brProxyServerCount=_BrProxyServerCount_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,11),_BrProxyServerCount_Type())
brProxyServerCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brProxyServerCount.setStatus(_A)
_BrProxyServerInfoTable_Object=MibTable
brProxyServerInfoTable=_BrProxyServerInfoTable_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12))
if mibBuilder.loadTexts:brProxyServerInfoTable.setStatus(_A)
_BrProxyServerInfoEntry_Object=MibTableRow
brProxyServerInfoEntry=_BrProxyServerInfoEntry_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12,1))
brProxyServerInfoEntry.setIndexNames((0,_E,_B9))
if mibBuilder.loadTexts:brProxyServerInfoEntry.setStatus(_A)
class _BrProxyServerInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrProxyServerInfoIndex_Type.__name__=_B
_BrProxyServerInfoIndex_Object=MibTableColumn
brProxyServerInfoIndex=_BrProxyServerInfoIndex_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12,1,1),_BrProxyServerInfoIndex_Type())
brProxyServerInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brProxyServerInfoIndex.setStatus(_A)
class _BrProxyServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('http',1),('secure',2),('ftp',3),('gopher',4),('socks',5)))
_BrProxyServerType_Type.__name__=_B
_BrProxyServerType_Object=MibTableColumn
brProxyServerType=_BrProxyServerType_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12,1,2),_BrProxyServerType_Type())
brProxyServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:brProxyServerType.setStatus(_A)
class _BrProxyServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_BrProxyServerName_Type.__name__=_G
_BrProxyServerName_Object=MibTableColumn
brProxyServerName=_BrProxyServerName_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12,1,3),_BrProxyServerName_Type())
brProxyServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:brProxyServerName.setStatus(_A)
class _BrProxyServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrProxyServerPort_Type.__name__=_B
_BrProxyServerPort_Object=MibTableColumn
brProxyServerPort=_BrProxyServerPort_Object((1,3,6,1,4,1,2435,2,4,3,2435,10,1,12,1,4),_BrProxyServerPort_Type())
brProxyServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brProxyServerPort.setStatus(_A)
_BroriginalOtherSetting_ObjectIdentity=ObjectIdentity
broriginalOtherSetting=_BroriginalOtherSetting_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,20))
_BroriginalJobTermination_ObjectIdentity=ObjectIdentity
broriginalJobTermination=_BroriginalJobTermination_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,20,1))
class _BrJobTerminationSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrJobTerminationSupported_Type.__name__=_B
_BrJobTerminationSupported_Object=MibScalar
brJobTerminationSupported=_BrJobTerminationSupported_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,1,1),_BrJobTerminationSupported_Type())
brJobTerminationSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brJobTerminationSupported.setStatus(_A)
class _BrJobTerminationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrJobTerminationEnable_Type.__name__=_B
_BrJobTerminationEnable_Object=MibScalar
brJobTerminationEnable=_BrJobTerminationEnable_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,1,2),_BrJobTerminationEnable_Type())
brJobTerminationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brJobTerminationEnable.setStatus(_A)
_BroriginalSNMPTrap_ObjectIdentity=ObjectIdentity
broriginalSNMPTrap=_BroriginalSNMPTrap_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,20,2))
_BrSNMPTrapTable_Object=MibTable
brSNMPTrapTable=_BrSNMPTrapTable_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,2,1))
if mibBuilder.loadTexts:brSNMPTrapTable.setStatus(_A)
_BrSNMPTrapEntry_Object=MibTableRow
brSNMPTrapEntry=_BrSNMPTrapEntry_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,2,1,1))
brSNMPTrapEntry.setIndexNames((0,_E,_BA))
if mibBuilder.loadTexts:brSNMPTrapEntry.setStatus(_A)
class _BrSNMPTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrSNMPTrapIndex_Type.__name__=_B
_BrSNMPTrapIndex_Object=MibTableColumn
brSNMPTrapIndex=_BrSNMPTrapIndex_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,2,1,1,1),_BrSNMPTrapIndex_Type())
brSNMPTrapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brSNMPTrapIndex.setStatus(_A)
_BrTCPIPServerAddress_Type=IpAddress
_BrTCPIPServerAddress_Object=MibTableColumn
brTCPIPServerAddress=_BrTCPIPServerAddress_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,2,1,1,2),_BrTCPIPServerAddress_Type())
brTCPIPServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brTCPIPServerAddress.setStatus(_A)
_BroriginalLegacy_ObjectIdentity=ObjectIdentity
broriginalLegacy=_BroriginalLegacy_ObjectIdentity((1,3,6,1,4,1,2435,2,4,3,2435,20,3))
_BrLegacyCompatible_Type=Integer32
_BrLegacyCompatible_Object=MibScalar
brLegacyCompatible=_BrLegacyCompatible_Object((1,3,6,1,4,1,2435,2,4,3,2435,20,3,1),_BrLegacyCompatible_Type())
brLegacyCompatible.setMaxAccess(_C)
if mibBuilder.loadTexts:brLegacyCompatible.setStatus(_A)
_NpMultiCards_ObjectIdentity=ObjectIdentity
npMultiCards=_NpMultiCards_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4))
_NpMultiIFSet_ObjectIdentity=ObjectIdentity
npMultiIFSet=_NpMultiIFSet_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,99))
_BrMultiIFdns_ObjectIdentity=ObjectIdentity
brMultiIFdns=_BrMultiIFdns_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,99,1))
_BrMultiIFDNSTable_Object=MibTable
brMultiIFDNSTable=_BrMultiIFDNSTable_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1))
if mibBuilder.loadTexts:brMultiIFDNSTable.setStatus(_A)
_BrMultiIFDNSEntry_Object=MibTableRow
brMultiIFDNSEntry=_BrMultiIFDNSEntry_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1,1))
brMultiIFDNSEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFDNSEntry.setStatus(_A)
class _BrMultiIFTCPIPDNSIPSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),(_w,2)))
_BrMultiIFTCPIPDNSIPSetup_Type.__name__=_B
_BrMultiIFTCPIPDNSIPSetup_Object=MibTableColumn
brMultiIFTCPIPDNSIPSetup=_BrMultiIFTCPIPDNSIPSetup_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1,1,1),_BrMultiIFTCPIPDNSIPSetup_Type())
brMultiIFTCPIPDNSIPSetup.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPDNSIPSetup.setStatus(_A)
_BrMultiIFPrimaryDNSIPAddress_Type=IpAddress
_BrMultiIFPrimaryDNSIPAddress_Object=MibTableColumn
brMultiIFPrimaryDNSIPAddress=_BrMultiIFPrimaryDNSIPAddress_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1,1,2),_BrMultiIFPrimaryDNSIPAddress_Type())
brMultiIFPrimaryDNSIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFPrimaryDNSIPAddress.setStatus(_A)
_BrMultiIFSecondaryDNSIPAddress_Type=IpAddress
_BrMultiIFSecondaryDNSIPAddress_Object=MibTableColumn
brMultiIFSecondaryDNSIPAddress=_BrMultiIFSecondaryDNSIPAddress_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1,1,3),_BrMultiIFSecondaryDNSIPAddress_Type())
brMultiIFSecondaryDNSIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFSecondaryDNSIPAddress.setStatus(_A)
_BrMultiIFTCPIPConnectTime_Type=Integer32
_BrMultiIFTCPIPConnectTime_Object=MibTableColumn
brMultiIFTCPIPConnectTime=_BrMultiIFTCPIPConnectTime_Object((1,3,6,1,4,1,2435,2,4,4,99,1,1,1,4),_BrMultiIFTCPIPConnectTime_Type())
brMultiIFTCPIPConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPConnectTime.setStatus(_A)
_BrnetMultiIFConfig_ObjectIdentity=ObjectIdentity
brnetMultiIFConfig=_BrnetMultiIFConfig_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240))
_BrMultiIFconfig_ObjectIdentity=ObjectIdentity
brMultiIFconfig=_BrMultiIFconfig_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,1))
class _BrMultiIFSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFSupported_Type.__name__=_B
_BrMultiIFSupported_Object=MibScalar
brMultiIFSupported=_BrMultiIFSupported_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,1),_BrMultiIFSupported_Type())
brMultiIFSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFSupported.setStatus(_A)
class _BrMultiIFActiveIF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lan',1),(_BB,2),('both',3)))
_BrMultiIFActiveIF_Type.__name__=_B
_BrMultiIFActiveIF_Object=MibScalar
brMultiIFActiveIF=_BrMultiIFActiveIF_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,2),_BrMultiIFActiveIF_Type())
brMultiIFActiveIF.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFActiveIF.setStatus(_A)
class _BrMultiIFAllSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrMultiIFAllSetDefault_Type.__name__=_B
_BrMultiIFAllSetDefault_Object=MibScalar
brMultiIFAllSetDefault=_BrMultiIFAllSetDefault_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,3),_BrMultiIFAllSetDefault_Type())
brMultiIFAllSetDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFAllSetDefault.setStatus(_A)
_BrMultiIFCount_Type=Integer32
_BrMultiIFCount_Object=MibScalar
brMultiIFCount=_BrMultiIFCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,4),_BrMultiIFCount_Type())
brMultiIFCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFCount.setStatus(_A)
_BrMultiIFConfigureTable_Object=MibTable
brMultiIFConfigureTable=_BrMultiIFConfigureTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5))
if mibBuilder.loadTexts:brMultiIFConfigureTable.setStatus(_A)
_BrMultiIFConfigureEntry_Object=MibTableRow
brMultiIFConfigureEntry=_BrMultiIFConfigureEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1))
brMultiIFConfigureEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFConfigureEntry.setStatus(_A)
class _BrMultiIFConfigureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrMultiIFConfigureIndex_Type.__name__=_B
_BrMultiIFConfigureIndex_Object=MibTableColumn
brMultiIFConfigureIndex=_BrMultiIFConfigureIndex_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,1),_BrMultiIFConfigureIndex_Type())
brMultiIFConfigureIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFConfigureIndex.setStatus(_A)
class _BrMultiIFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lan',1),(_BB,2)))
_BrMultiIFType_Type.__name__=_B
_BrMultiIFType_Object=MibTableColumn
brMultiIFType=_BrMultiIFType_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,2),_BrMultiIFType_Type())
brMultiIFType.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFType.setStatus(_A)
class _BrMultiIFDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrMultiIFDescription_Type.__name__=_F
_BrMultiIFDescription_Object=MibTableColumn
brMultiIFDescription=_BrMultiIFDescription_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,3),_BrMultiIFDescription_Type())
brMultiIFDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFDescription.setStatus(_A)
_BrMultiIFNodeName_Type=OctetString
_BrMultiIFNodeName_Object=MibTableColumn
brMultiIFNodeName=_BrMultiIFNodeName_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,4),_BrMultiIFNodeName_Type())
brMultiIFNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFNodeName.setStatus(_A)
class _BrMultiIFInterfaceEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFInterfaceEnable_Type.__name__=_B
_BrMultiIFInterfaceEnable_Object=MibTableColumn
brMultiIFInterfaceEnable=_BrMultiIFInterfaceEnable_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,5),_BrMultiIFInterfaceEnable_Type())
brMultiIFInterfaceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFInterfaceEnable.setStatus(_A)
class _BrMultiIFEnetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BrMultiIFEnetMode_Type.__name__=_B
_BrMultiIFEnetMode_Object=MibTableColumn
brMultiIFEnetMode=_BrMultiIFEnetMode_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,6),_BrMultiIFEnetMode_Type())
brMultiIFEnetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFEnetMode.setStatus(_A)
class _BrMultiIFHardwareType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrMultiIFHardwareType_Type.__name__=_B
_BrMultiIFHardwareType_Object=MibTableColumn
brMultiIFHardwareType=_BrMultiIFHardwareType_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,7),_BrMultiIFHardwareType_Type())
brMultiIFHardwareType.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFHardwareType.setStatus(_A)
_BrMultiIFNodeType_Type=OctetString
_BrMultiIFNodeType_Object=MibTableColumn
brMultiIFNodeType=_BrMultiIFNodeType_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,8),_BrMultiIFNodeType_Type())
brMultiIFNodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFNodeType.setStatus(_A)
class _BrMultiIFInterfaceEnableImmediate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFInterfaceEnableImmediate_Type.__name__=_B
_BrMultiIFInterfaceEnableImmediate_Object=MibTableColumn
brMultiIFInterfaceEnableImmediate=_BrMultiIFInterfaceEnableImmediate_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,5,1,9),_BrMultiIFInterfaceEnableImmediate_Type())
brMultiIFInterfaceEnableImmediate.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFInterfaceEnableImmediate.setStatus(_A)
_BrMultiIFPrimaryInterface_Type=Integer32
_BrMultiIFPrimaryInterface_Object=MibScalar
brMultiIFPrimaryInterface=_BrMultiIFPrimaryInterface_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,6),_BrMultiIFPrimaryInterface_Type())
brMultiIFPrimaryInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFPrimaryInterface.setStatus(_A)
_BrMultiIFInterfaceInformation_Type=Integer32
_BrMultiIFInterfaceInformation_Object=MibScalar
brMultiIFInterfaceInformation=_BrMultiIFInterfaceInformation_Object((1,3,6,1,4,1,2435,2,4,4,1240,1,7),_BrMultiIFInterfaceInformation_Type())
brMultiIFInterfaceInformation.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFInterfaceInformation.setStatus(_A)
_BrMultiIFcontrol_ObjectIdentity=ObjectIdentity
brMultiIFcontrol=_BrMultiIFcontrol_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,2))
_BrMultiIFControlTable_Object=MibTable
brMultiIFControlTable=_BrMultiIFControlTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,2,1))
if mibBuilder.loadTexts:brMultiIFControlTable.setStatus(_A)
_BrMultiIFControlEntry_Object=MibTableRow
brMultiIFControlEntry=_BrMultiIFControlEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,2,1,1))
brMultiIFControlEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFControlEntry.setStatus(_A)
class _BrMultiIFSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrMultiIFSetDefault_Type.__name__=_B
_BrMultiIFSetDefault_Object=MibTableColumn
brMultiIFSetDefault=_BrMultiIFSetDefault_Object((1,3,6,1,4,1,2435,2,4,4,1240,2,1,1,1),_BrMultiIFSetDefault_Type())
brMultiIFSetDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFSetDefault.setStatus(_A)
_BrMultiIFservice_ObjectIdentity=ObjectIdentity
brMultiIFservice=_BrMultiIFservice_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,4))
_BrMultiIFServiceTable_Object=MibTable
brMultiIFServiceTable=_BrMultiIFServiceTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1))
if mibBuilder.loadTexts:brMultiIFServiceTable.setStatus(_A)
_BrMultiIFServiceEntry_Object=MibTableRow
brMultiIFServiceEntry=_BrMultiIFServiceEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1,1))
brMultiIFServiceEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFServiceEntry.setStatus(_A)
class _BrMultiIFServiceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_BrMultiIFServiceCount_Type.__name__=_B
_BrMultiIFServiceCount_Object=MibTableColumn
brMultiIFServiceCount=_BrMultiIFServiceCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1,1,1),_BrMultiIFServiceCount_Type())
brMultiIFServiceCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceCount.setStatus(_A)
class _BrMultiIFServiceStringLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_BrMultiIFServiceStringLimit_Type.__name__=_B
_BrMultiIFServiceStringLimit_Object=MibTableColumn
brMultiIFServiceStringLimit=_BrMultiIFServiceStringLimit_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1,1,2),_BrMultiIFServiceStringLimit_Type())
brMultiIFServiceStringLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceStringLimit.setStatus(_A)
_BrMultiIFServiceStringCount_Type=Integer32
_BrMultiIFServiceStringCount_Object=MibTableColumn
brMultiIFServiceStringCount=_BrMultiIFServiceStringCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1,1,3),_BrMultiIFServiceStringCount_Type())
brMultiIFServiceStringCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceStringCount.setStatus(_A)
_BrMultiIFServiceFilterCount_Type=Integer32
_BrMultiIFServiceFilterCount_Object=MibTableColumn
brMultiIFServiceFilterCount=_BrMultiIFServiceFilterCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,1,1,4),_BrMultiIFServiceFilterCount_Type())
brMultiIFServiceFilterCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceFilterCount.setStatus(_A)
_BrMultiIFServiceInfoTable_Object=MibTable
brMultiIFServiceInfoTable=_BrMultiIFServiceInfoTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2))
if mibBuilder.loadTexts:brMultiIFServiceInfoTable.setStatus(_A)
_BrMultiIFServiceInfoEntry_Object=MibTableRow
brMultiIFServiceInfoEntry=_BrMultiIFServiceInfoEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1))
brMultiIFServiceInfoEntry.setIndexNames((0,_E,_J),(0,_E,_BC))
if mibBuilder.loadTexts:brMultiIFServiceInfoEntry.setStatus(_A)
class _BrMultiIFServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BrMultiIFServiceIndex_Type.__name__=_B
_BrMultiIFServiceIndex_Object=MibTableColumn
brMultiIFServiceIndex=_BrMultiIFServiceIndex_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,1),_BrMultiIFServiceIndex_Type())
brMultiIFServiceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceIndex.setStatus(_A)
class _BrMultiIFServiceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrMultiIFServiceName_Type.__name__=_F
_BrMultiIFServiceName_Object=MibTableColumn
brMultiIFServiceName=_BrMultiIFServiceName_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,2),_BrMultiIFServiceName_Type())
brMultiIFServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceName.setStatus(_A)
class _BrMultiIFServicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BrMultiIFServicePort_Type.__name__=_B
_BrMultiIFServicePort_Object=MibTableColumn
brMultiIFServicePort=_BrMultiIFServicePort_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,3),_BrMultiIFServicePort_Type())
brMultiIFServicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServicePort.setStatus(_A)
class _BrMultiIFServiceFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceFilter_Type.__name__=_B
_BrMultiIFServiceFilter_Object=MibTableColumn
brMultiIFServiceFilter=_BrMultiIFServiceFilter_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,4),_BrMultiIFServiceFilter_Type())
brMultiIFServiceFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceFilter.setStatus(_A)
class _BrMultiIFServiceBOT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceBOT_Type.__name__=_B
_BrMultiIFServiceBOT_Object=MibTableColumn
brMultiIFServiceBOT=_BrMultiIFServiceBOT_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,5),_BrMultiIFServiceBOT_Type())
brMultiIFServiceBOT.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceBOT.setStatus(_A)
class _BrMultiIFServiceEOT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceEOT_Type.__name__=_B
_BrMultiIFServiceEOT_Object=MibTableColumn
brMultiIFServiceEOT=_BrMultiIFServiceEOT_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,6),_BrMultiIFServiceEOT_Type())
brMultiIFServiceEOT.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceEOT.setStatus(_A)
class _BrMultiIFServiceMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceMatch_Type.__name__=_B
_BrMultiIFServiceMatch_Object=MibTableColumn
brMultiIFServiceMatch=_BrMultiIFServiceMatch_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,7),_BrMultiIFServiceMatch_Type())
brMultiIFServiceMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceMatch.setStatus(_A)
class _BrMultiIFServiceReplace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceReplace_Type.__name__=_B
_BrMultiIFServiceReplace_Object=MibTableColumn
brMultiIFServiceReplace=_BrMultiIFServiceReplace_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,8),_BrMultiIFServiceReplace_Type())
brMultiIFServiceReplace.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceReplace.setStatus(_A)
class _BrMultiIFServiceTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BrMultiIFServiceTCPPort_Type.__name__=_B
_BrMultiIFServiceTCPPort_Object=MibTableColumn
brMultiIFServiceTCPPort=_BrMultiIFServiceTCPPort_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,9),_BrMultiIFServiceTCPPort_Type())
brMultiIFServiceTCPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceTCPPort.setStatus(_A)
class _BrMultiIFServiceNDSTree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrMultiIFServiceNDSTree_Type.__name__=_F
_BrMultiIFServiceNDSTree_Object=MibTableColumn
brMultiIFServiceNDSTree=_BrMultiIFServiceNDSTree_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,10),_BrMultiIFServiceNDSTree_Type())
brMultiIFServiceNDSTree.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceNDSTree.setStatus(_A)
class _BrMultiIFServiceNDSContext_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BrMultiIFServiceNDSContext_Type.__name__=_G
_BrMultiIFServiceNDSContext_Object=MibTableColumn
brMultiIFServiceNDSContext=_BrMultiIFServiceNDSContext_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,11),_BrMultiIFServiceNDSContext_Type())
brMultiIFServiceNDSContext.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceNDSContext.setStatus(_A)
class _BrMultiIFServiceVines_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_BrMultiIFServiceVines_Type.__name__=_F
_BrMultiIFServiceVines_Object=MibTableColumn
brMultiIFServiceVines=_BrMultiIFServiceVines_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,12),_BrMultiIFServiceVines_Type())
brMultiIFServiceVines.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceVines.setStatus(_A)
class _BrMultiIFServiceObsolete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_BrMultiIFServiceObsolete_Type.__name__=_B
_BrMultiIFServiceObsolete_Object=MibTableColumn
brMultiIFServiceObsolete=_BrMultiIFServiceObsolete_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,13),_BrMultiIFServiceObsolete_Type())
brMultiIFServiceObsolete.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceObsolete.setStatus(_A)
class _BrMultiIFServiceNetwareServerCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_BrMultiIFServiceNetwareServerCount_Type.__name__=_B
_BrMultiIFServiceNetwareServerCount_Object=MibTableColumn
brMultiIFServiceNetwareServerCount=_BrMultiIFServiceNetwareServerCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,14),_BrMultiIFServiceNetwareServerCount_Type())
brMultiIFServiceNetwareServerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceNetwareServerCount.setStatus(_A)
class _BrMultiIFServiceReceiveOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceReceiveOnly_Type.__name__=_B
_BrMultiIFServiceReceiveOnly_Object=MibTableColumn
brMultiIFServiceReceiveOnly=_BrMultiIFServiceReceiveOnly_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,15),_BrMultiIFServiceReceiveOnly_Type())
brMultiIFServiceReceiveOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceReceiveOnly.setStatus(_A)
class _BrMultiIFServiceTCPQueued_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceTCPQueued_Type.__name__=_B
_BrMultiIFServiceTCPQueued_Object=MibTableColumn
brMultiIFServiceTCPQueued=_BrMultiIFServiceTCPQueued_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,16),_BrMultiIFServiceTCPQueued_Type())
brMultiIFServiceTCPQueued.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceTCPQueued.setStatus(_A)
class _BrMultiIFServiceProtocolLAT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolLAT_Type.__name__=_B
_BrMultiIFServiceProtocolLAT_Object=MibTableColumn
brMultiIFServiceProtocolLAT=_BrMultiIFServiceProtocolLAT_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,17),_BrMultiIFServiceProtocolLAT_Type())
brMultiIFServiceProtocolLAT.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolLAT.setStatus(_A)
class _BrMultiIFServiceProtocolTCPIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolTCPIP_Type.__name__=_B
_BrMultiIFServiceProtocolTCPIP_Object=MibTableColumn
brMultiIFServiceProtocolTCPIP=_BrMultiIFServiceProtocolTCPIP_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,18),_BrMultiIFServiceProtocolTCPIP_Type())
brMultiIFServiceProtocolTCPIP.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolTCPIP.setStatus(_A)
class _BrMultiIFServiceProtocolNetware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolNetware_Type.__name__=_B
_BrMultiIFServiceProtocolNetware_Object=MibTableColumn
brMultiIFServiceProtocolNetware=_BrMultiIFServiceProtocolNetware_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,19),_BrMultiIFServiceProtocolNetware_Type())
brMultiIFServiceProtocolNetware.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolNetware.setStatus(_A)
class _BrMultiIFServiceProtocolAppleTalk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolAppleTalk_Type.__name__=_B
_BrMultiIFServiceProtocolAppleTalk_Object=MibTableColumn
brMultiIFServiceProtocolAppleTalk=_BrMultiIFServiceProtocolAppleTalk_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,20),_BrMultiIFServiceProtocolAppleTalk_Type())
brMultiIFServiceProtocolAppleTalk.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolAppleTalk.setStatus(_A)
class _BrMultiIFServiceProtocolBanyan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolBanyan_Type.__name__=_B
_BrMultiIFServiceProtocolBanyan_Object=MibTableColumn
brMultiIFServiceProtocolBanyan=_BrMultiIFServiceProtocolBanyan_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,21),_BrMultiIFServiceProtocolBanyan_Type())
brMultiIFServiceProtocolBanyan.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolBanyan.setStatus(_A)
class _BrMultiIFServiceProtocolDLC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolDLC_Type.__name__=_B
_BrMultiIFServiceProtocolDLC_Object=MibTableColumn
brMultiIFServiceProtocolDLC=_BrMultiIFServiceProtocolDLC_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,22),_BrMultiIFServiceProtocolDLC_Type())
brMultiIFServiceProtocolDLC.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolDLC.setStatus(_A)
class _BrMultiIFServiceProtocolNetBEUI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolNetBEUI_Type.__name__=_B
_BrMultiIFServiceProtocolNetBEUI_Object=MibTableColumn
brMultiIFServiceProtocolNetBEUI=_BrMultiIFServiceProtocolNetBEUI_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,23),_BrMultiIFServiceProtocolNetBEUI_Type())
brMultiIFServiceProtocolNetBEUI.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolNetBEUI.setStatus(_A)
class _BrMultiIFServiceNetwareServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceNetwareServerMode_Type.__name__=_B
_BrMultiIFServiceNetwareServerMode_Object=MibTableColumn
brMultiIFServiceNetwareServerMode=_BrMultiIFServiceNetwareServerMode_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,24),_BrMultiIFServiceNetwareServerMode_Type())
brMultiIFServiceNetwareServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceNetwareServerMode.setStatus(_A)
class _BrMultiIFServiceNetwareRemotePrinterNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BrMultiIFServiceNetwareRemotePrinterNum_Type.__name__=_B
_BrMultiIFServiceNetwareRemotePrinterNum_Object=MibTableColumn
brMultiIFServiceNetwareRemotePrinterNum=_BrMultiIFServiceNetwareRemotePrinterNum_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,25),_BrMultiIFServiceNetwareRemotePrinterNum_Type())
brMultiIFServiceNetwareRemotePrinterNum.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceNetwareRemotePrinterNum.setStatus(_A)
class _BrMultiIFServiceProtocolIPP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFServiceProtocolIPP_Type.__name__=_B
_BrMultiIFServiceProtocolIPP_Object=MibTableColumn
brMultiIFServiceProtocolIPP=_BrMultiIFServiceProtocolIPP_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,26),_BrMultiIFServiceProtocolIPP_Type())
brMultiIFServiceProtocolIPP.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceProtocolIPP.setStatus(_A)
class _BrMultiIFServiceAppleTalkType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrMultiIFServiceAppleTalkType_Type.__name__=_F
_BrMultiIFServiceAppleTalkType_Object=MibTableColumn
brMultiIFServiceAppleTalkType=_BrMultiIFServiceAppleTalkType_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,2,1,27),_BrMultiIFServiceAppleTalkType_Type())
brMultiIFServiceAppleTalkType.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceAppleTalkType.setStatus(_A)
_BrMultiIFServiceStringInfoTable_Object=MibTable
brMultiIFServiceStringInfoTable=_BrMultiIFServiceStringInfoTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,3))
if mibBuilder.loadTexts:brMultiIFServiceStringInfoTable.setStatus(_A)
_BrMultiIFServiceStringInfoEntry_Object=MibTableRow
brMultiIFServiceStringInfoEntry=_BrMultiIFServiceStringInfoEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,3,1))
brMultiIFServiceStringInfoEntry.setIndexNames((0,_E,_J),(0,_E,_BD))
if mibBuilder.loadTexts:brMultiIFServiceStringInfoEntry.setStatus(_A)
class _BrMultiIFServiceStringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BrMultiIFServiceStringIndex_Type.__name__=_B
_BrMultiIFServiceStringIndex_Object=MibTableColumn
brMultiIFServiceStringIndex=_BrMultiIFServiceStringIndex_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,3,1,1),_BrMultiIFServiceStringIndex_Type())
brMultiIFServiceStringIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFServiceStringIndex.setStatus(_A)
class _BrMultiIFServiceString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrMultiIFServiceString_Type.__name__=_F
_BrMultiIFServiceString_Object=MibTableColumn
brMultiIFServiceString=_BrMultiIFServiceString_Object((1,3,6,1,4,1,2435,2,4,4,1240,4,3,1,2),_BrMultiIFServiceString_Type())
brMultiIFServiceString.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFServiceString.setStatus(_A)
_BrMultiIFprotocol_ObjectIdentity=ObjectIdentity
brMultiIFprotocol=_BrMultiIFprotocol_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5))
_BrMultiIFtcpip_ObjectIdentity=ObjectIdentity
brMultiIFtcpip=_BrMultiIFtcpip_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,2))
_BrMultiIFTCPIPTable_Object=MibTable
brMultiIFTCPIPTable=_BrMultiIFTCPIPTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1))
if mibBuilder.loadTexts:brMultiIFTCPIPTable.setStatus(_A)
_BrMultiIFTCPIPEntry_Object=MibTableRow
brMultiIFTCPIPEntry=_BrMultiIFTCPIPEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1))
brMultiIFTCPIPEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFTCPIPEntry.setStatus(_A)
_BrMultiIFTCPIPAddress_Type=IpAddress
_BrMultiIFTCPIPAddress_Object=MibTableColumn
brMultiIFTCPIPAddress=_BrMultiIFTCPIPAddress_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,1),_BrMultiIFTCPIPAddress_Type())
brMultiIFTCPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPAddress.setStatus(_A)
_BrMultiIFTCPIPSubnetMask_Type=IpAddress
_BrMultiIFTCPIPSubnetMask_Object=MibTableColumn
brMultiIFTCPIPSubnetMask=_BrMultiIFTCPIPSubnetMask_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,2),_BrMultiIFTCPIPSubnetMask_Type())
brMultiIFTCPIPSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPSubnetMask.setStatus(_A)
_BrMultiIFTCPIPGateway_Type=IpAddress
_BrMultiIFTCPIPGateway_Object=MibTableColumn
brMultiIFTCPIPGateway=_BrMultiIFTCPIPGateway_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,3),_BrMultiIFTCPIPGateway_Type())
brMultiIFTCPIPGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPGateway.setStatus(_A)
class _BrMultiIFTCPIPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrMultiIFTCPIPMethod_Type.__name__=_B
_BrMultiIFTCPIPMethod_Object=MibTableColumn
brMultiIFTCPIPMethod=_BrMultiIFTCPIPMethod_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,4),_BrMultiIFTCPIPMethod_Type())
brMultiIFTCPIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPMethod.setStatus(_A)
class _BrMultiIFTCPIPUpdate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_BrMultiIFTCPIPUpdate_Type.__name__=_G
_BrMultiIFTCPIPUpdate_Object=MibTableColumn
brMultiIFTCPIPUpdate=_BrMultiIFTCPIPUpdate_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,5),_BrMultiIFTCPIPUpdate_Type())
brMultiIFTCPIPUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPUpdate.setStatus(_A)
class _BrMultiIFTCPIPTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrMultiIFTCPIPTimeout_Type.__name__=_B
_BrMultiIFTCPIPTimeout_Object=MibTableColumn
brMultiIFTCPIPTimeout=_BrMultiIFTCPIPTimeout_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,6),_BrMultiIFTCPIPTimeout_Type())
brMultiIFTCPIPTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPTimeout.setStatus(_A)
class _BrMultiIFTCPIPBootTries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_BrMultiIFTCPIPBootTries_Type.__name__=_B
_BrMultiIFTCPIPBootTries_Object=MibTableColumn
brMultiIFTCPIPBootTries=_BrMultiIFTCPIPBootTries_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,7),_BrMultiIFTCPIPBootTries_Type())
brMultiIFTCPIPBootTries.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPBootTries.setStatus(_A)
class _BrMultiIFTCPIPRARPNoSubnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFTCPIPRARPNoSubnet_Type.__name__=_B
_BrMultiIFTCPIPRARPNoSubnet_Object=MibTableColumn
brMultiIFTCPIPRARPNoSubnet=_BrMultiIFTCPIPRARPNoSubnet_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,8),_BrMultiIFTCPIPRARPNoSubnet_Type())
brMultiIFTCPIPRARPNoSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPRARPNoSubnet.setStatus(_A)
class _BrMultiIFTCPIPRARPNoGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFTCPIPRARPNoGateway_Type.__name__=_B
_BrMultiIFTCPIPRARPNoGateway_Object=MibTableColumn
brMultiIFTCPIPRARPNoGateway=_BrMultiIFTCPIPRARPNoGateway_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,9),_BrMultiIFTCPIPRARPNoGateway_Type())
brMultiIFTCPIPRARPNoGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPRARPNoGateway.setStatus(_A)
class _BrMultiIFTCPIPUseMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrMultiIFTCPIPUseMethod_Type.__name__=_B
_BrMultiIFTCPIPUseMethod_Object=MibTableColumn
brMultiIFTCPIPUseMethod=_BrMultiIFTCPIPUseMethod_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,10),_BrMultiIFTCPIPUseMethod_Type())
brMultiIFTCPIPUseMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPUseMethod.setStatus(_A)
_BrMultiIFTCPIPMethodServer_Type=IpAddress
_BrMultiIFTCPIPMethodServer_Object=MibTableColumn
brMultiIFTCPIPMethodServer=_BrMultiIFTCPIPMethodServer_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,2,1,1,11),_BrMultiIFTCPIPMethodServer_Type())
brMultiIFTCPIPMethodServer.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPMethodServer.setStatus(_A)
_BrMultiIFnetbeui_ObjectIdentity=ObjectIdentity
brMultiIFnetbeui=_BrMultiIFnetbeui_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,8))
_BrMultiIFNetBIOSTable_Object=MibTable
brMultiIFNetBIOSTable=_BrMultiIFNetBIOSTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1))
if mibBuilder.loadTexts:brMultiIFNetBIOSTable.setStatus(_A)
_BrMultiIFNetBIOSEntry_Object=MibTableRow
brMultiIFNetBIOSEntry=_BrMultiIFNetBIOSEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1,1))
brMultiIFNetBIOSEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFNetBIOSEntry.setStatus(_A)
class _BrMultiIFNetBIOSIPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFNetBIOSIPMethod_Type.__name__=_B
_BrMultiIFNetBIOSIPMethod_Object=MibTableColumn
brMultiIFNetBIOSIPMethod=_BrMultiIFNetBIOSIPMethod_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1,1,1),_BrMultiIFNetBIOSIPMethod_Type())
brMultiIFNetBIOSIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFNetBIOSIPMethod.setStatus(_A)
_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Type=IpAddress
_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Object=MibTableColumn
brMultiIFTCPIPNetBIOSPrimaryWINSAddr=_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1,1,2),_BrMultiIFTCPIPNetBIOSPrimaryWINSAddr_Type())
brMultiIFTCPIPNetBIOSPrimaryWINSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPNetBIOSPrimaryWINSAddr.setStatus(_A)
_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Type=IpAddress
_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Object=MibTableColumn
brMultiIFTCPIPNetBIOSSecondaryWINSAddr=_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1,1,3),_BrMultiIFTCPIPNetBIOSSecondaryWINSAddr_Type())
brMultiIFTCPIPNetBIOSSecondaryWINSAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFTCPIPNetBIOSSecondaryWINSAddr.setStatus(_A)
class _BrMultiIFNetBEUIDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_BrMultiIFNetBEUIDomain_Type.__name__=_F
_BrMultiIFNetBEUIDomain_Object=MibTableColumn
brMultiIFNetBEUIDomain=_BrMultiIFNetBEUIDomain_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,8,1,1,4),_BrMultiIFNetBEUIDomain_Type())
brMultiIFNetBEUIDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFNetBEUIDomain.setStatus(_A)
_BrMultiIForiginalapipa_ObjectIdentity=ObjectIdentity
brMultiIForiginalapipa=_BrMultiIForiginalapipa_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,12))
_BrMultiIFAPIPATable_Object=MibTable
brMultiIFAPIPATable=_BrMultiIFAPIPATable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,12,1))
if mibBuilder.loadTexts:brMultiIFAPIPATable.setStatus(_A)
_BrMultiIFAPIPAEntry_Object=MibTableRow
brMultiIFAPIPAEntry=_BrMultiIFAPIPAEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,12,1,1))
brMultiIFAPIPAEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFAPIPAEntry.setStatus(_A)
class _BrMultiIFAPIPASupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFAPIPASupported_Type.__name__=_B
_BrMultiIFAPIPASupported_Object=MibTableColumn
brMultiIFAPIPASupported=_BrMultiIFAPIPASupported_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,12,1,1,1),_BrMultiIFAPIPASupported_Type())
brMultiIFAPIPASupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFAPIPASupported.setStatus(_A)
class _BrMultiIFAPIPAEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFAPIPAEnable_Type.__name__=_B
_BrMultiIFAPIPAEnable_Object=MibTableColumn
brMultiIFAPIPAEnable=_BrMultiIFAPIPAEnable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,12,1,1,2),_BrMultiIFAPIPAEnable_Type())
brMultiIFAPIPAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFAPIPAEnable.setStatus(_A)
_BrMultiIForiginalLAA_ObjectIdentity=ObjectIdentity
brMultiIForiginalLAA=_BrMultiIForiginalLAA_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,14))
_BrMultiIFLAATable_Object=MibTable
brMultiIFLAATable=_BrMultiIFLAATable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,14,1))
if mibBuilder.loadTexts:brMultiIFLAATable.setStatus(_A)
_BrMultiIFLAAEntry_Object=MibTableRow
brMultiIFLAAEntry=_BrMultiIFLAAEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,14,1,1))
brMultiIFLAAEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFLAAEntry.setStatus(_A)
class _BrMultiIFLAASupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BrMultiIFLAASupported_Type.__name__=_B
_BrMultiIFLAASupported_Object=MibTableColumn
brMultiIFLAASupported=_BrMultiIFLAASupported_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,14,1,1,1),_BrMultiIFLAASupported_Type())
brMultiIFLAASupported.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFLAASupported.setStatus(_A)
class _BrMultiIFLAAMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_BrMultiIFLAAMacAddress_Type.__name__=_G
_BrMultiIFLAAMacAddress_Object=MibTableColumn
brMultiIFLAAMacAddress=_BrMultiIFLAAMacAddress_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,14,1,1,2),_BrMultiIFLAAMacAddress_Type())
brMultiIFLAAMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFLAAMacAddress.setStatus(_A)
_BrMultiIForiginalIPv6_ObjectIdentity=ObjectIdentity
brMultiIForiginalIPv6=_BrMultiIForiginalIPv6_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,15))
_BrMultiIFIPv6AddressCountTable_Object=MibTable
brMultiIFIPv6AddressCountTable=_BrMultiIFIPv6AddressCountTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,1))
if mibBuilder.loadTexts:brMultiIFIPv6AddressCountTable.setStatus(_A)
_BrMultiIFIPv6AddressCountEntry_Object=MibTableRow
brMultiIFIPv6AddressCountEntry=_BrMultiIFIPv6AddressCountEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,1,1))
brMultiIFIPv6AddressCountEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFIPv6AddressCountEntry.setStatus(_A)
_BrMultiIFIPv6AddressCount_Type=Integer32
_BrMultiIFIPv6AddressCount_Object=MibTableColumn
brMultiIFIPv6AddressCount=_BrMultiIFIPv6AddressCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,1,1,1),_BrMultiIFIPv6AddressCount_Type())
brMultiIFIPv6AddressCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6AddressCount.setStatus(_A)
_BrMultiIFIPv6AddressTable_Object=MibTable
brMultiIFIPv6AddressTable=_BrMultiIFIPv6AddressTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2))
if mibBuilder.loadTexts:brMultiIFIPv6AddressTable.setStatus(_A)
_BrMultiIFIPv6AddressEntry_Object=MibTableRow
brMultiIFIPv6AddressEntry=_BrMultiIFIPv6AddressEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2,1))
brMultiIFIPv6AddressEntry.setIndexNames((0,_E,_J),(0,_E,_BE))
if mibBuilder.loadTexts:brMultiIFIPv6AddressEntry.setStatus(_A)
class _BrMultiIFIPv6AddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrMultiIFIPv6AddressIndex_Type.__name__=_B
_BrMultiIFIPv6AddressIndex_Object=MibTableColumn
brMultiIFIPv6AddressIndex=_BrMultiIFIPv6AddressIndex_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2,1,1),_BrMultiIFIPv6AddressIndex_Type())
brMultiIFIPv6AddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6AddressIndex.setStatus(_A)
_BrMultiIFIPv6Address_Type=Ipv6Address
_BrMultiIFIPv6Address_Object=MibTableColumn
brMultiIFIPv6Address=_BrMultiIFIPv6Address_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2,1,2),_BrMultiIFIPv6Address_Type())
brMultiIFIPv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6Address.setStatus(_A)
class _BrMultiIFIPv6UseMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BrMultiIFIPv6UseMethod_Type.__name__=_B
_BrMultiIFIPv6UseMethod_Object=MibTableColumn
brMultiIFIPv6UseMethod=_BrMultiIFIPv6UseMethod_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2,1,3),_BrMultiIFIPv6UseMethod_Type())
brMultiIFIPv6UseMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6UseMethod.setStatus(_A)
class _BrMultiIFIPv6MethodServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrMultiIFIPv6MethodServer_Type.__name__=_F
_BrMultiIFIPv6MethodServer_Object=MibTableColumn
brMultiIFIPv6MethodServer=_BrMultiIFIPv6MethodServer_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,2,1,4),_BrMultiIFIPv6MethodServer_Type())
brMultiIFIPv6MethodServer.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6MethodServer.setStatus(_A)
_BrMultiIFIPv6StaticAddressCountTable_Object=MibTable
brMultiIFIPv6StaticAddressCountTable=_BrMultiIFIPv6StaticAddressCountTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,3))
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressCountTable.setStatus(_A)
_BrMultiIFIPv6StaticAddressCountEntry_Object=MibTableRow
brMultiIFIPv6StaticAddressCountEntry=_BrMultiIFIPv6StaticAddressCountEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,3,1))
brMultiIFIPv6StaticAddressCountEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressCountEntry.setStatus(_A)
_BrMultiIFIPv6StaticAddressCount_Type=Integer32
_BrMultiIFIPv6StaticAddressCount_Object=MibTableColumn
brMultiIFIPv6StaticAddressCount=_BrMultiIFIPv6StaticAddressCount_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,3,1,1),_BrMultiIFIPv6StaticAddressCount_Type())
brMultiIFIPv6StaticAddressCount.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressCount.setStatus(_A)
_BrMultiIFIPv6StaticAddressTable_Object=MibTable
brMultiIFIPv6StaticAddressTable=_BrMultiIFIPv6StaticAddressTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4))
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressTable.setStatus(_A)
_BrMultiIFIPv6StaticAddressEntry_Object=MibTableRow
brMultiIFIPv6StaticAddressEntry=_BrMultiIFIPv6StaticAddressEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4,1))
brMultiIFIPv6StaticAddressEntry.setIndexNames((0,_E,_J),(0,_E,_BF))
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressEntry.setStatus(_A)
class _BrMultiIFIPv6StaticAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BrMultiIFIPv6StaticAddressIndex_Type.__name__=_B
_BrMultiIFIPv6StaticAddressIndex_Object=MibTableColumn
brMultiIFIPv6StaticAddressIndex=_BrMultiIFIPv6StaticAddressIndex_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4,1,1),_BrMultiIFIPv6StaticAddressIndex_Type())
brMultiIFIPv6StaticAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressIndex.setStatus(_A)
_BrMultiIFIPv6StaticAddressEnable_Type=Integer32
_BrMultiIFIPv6StaticAddressEnable_Object=MibTableColumn
brMultiIFIPv6StaticAddressEnable=_BrMultiIFIPv6StaticAddressEnable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4,1,2),_BrMultiIFIPv6StaticAddressEnable_Type())
brMultiIFIPv6StaticAddressEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressEnable.setStatus(_A)
_BrMultiIFIPv6StaticAddress_Type=Ipv6Address
_BrMultiIFIPv6StaticAddress_Object=MibTableColumn
brMultiIFIPv6StaticAddress=_BrMultiIFIPv6StaticAddress_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4,1,3),_BrMultiIFIPv6StaticAddress_Type())
brMultiIFIPv6StaticAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddress.setStatus(_A)
_BrMultiIFIPv6StaticAddressPrefixLength_Type=Integer32
_BrMultiIFIPv6StaticAddressPrefixLength_Object=MibTableColumn
brMultiIFIPv6StaticAddressPrefixLength=_BrMultiIFIPv6StaticAddressPrefixLength_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,4,1,4),_BrMultiIFIPv6StaticAddressPrefixLength_Type())
brMultiIFIPv6StaticAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFIPv6StaticAddressPrefixLength.setStatus(_A)
_BrMultiIFDNSIPv6AddressTable_Object=MibTable
brMultiIFDNSIPv6AddressTable=_BrMultiIFDNSIPv6AddressTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,5))
if mibBuilder.loadTexts:brMultiIFDNSIPv6AddressTable.setStatus(_A)
_BrMultiIFDNSIPv6AddressEntry_Object=MibTableRow
brMultiIFDNSIPv6AddressEntry=_BrMultiIFDNSIPv6AddressEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,5,1))
brMultiIFDNSIPv6AddressEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFDNSIPv6AddressEntry.setStatus(_A)
_BrMultiIFPrimaryDNSIPv6Address_Type=Ipv6Address
_BrMultiIFPrimaryDNSIPv6Address_Object=MibTableColumn
brMultiIFPrimaryDNSIPv6Address=_BrMultiIFPrimaryDNSIPv6Address_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,5,1,1),_BrMultiIFPrimaryDNSIPv6Address_Type())
brMultiIFPrimaryDNSIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFPrimaryDNSIPv6Address.setStatus(_A)
_BrMultiIFSecondaryDNSIPv6Address_Type=Ipv6Address
_BrMultiIFSecondaryDNSIPv6Address_Object=MibTableColumn
brMultiIFSecondaryDNSIPv6Address=_BrMultiIFSecondaryDNSIPv6Address_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,15,5,1,2),_BrMultiIFSecondaryDNSIPv6Address_Type())
brMultiIFSecondaryDNSIPv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFSecondaryDNSIPv6Address.setStatus(_A)
_BrMultiIForiginalWebServices_ObjectIdentity=ObjectIdentity
brMultiIForiginalWebServices=_BrMultiIForiginalWebServices_ObjectIdentity((1,3,6,1,4,1,2435,2,4,4,1240,5,16))
_BrMultiIFWebServicesTable_Object=MibTable
brMultiIFWebServicesTable=_BrMultiIFWebServicesTable_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,16,1))
if mibBuilder.loadTexts:brMultiIFWebServicesTable.setStatus(_A)
_BrMultiIFWebServicesEntry_Object=MibTableRow
brMultiIFWebServicesEntry=_BrMultiIFWebServicesEntry_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,16,1,1))
brMultiIFWebServicesEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:brMultiIFWebServicesEntry.setStatus(_A)
class _BrMultiIFWebServicesName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BrMultiIFWebServicesName_Type.__name__=_F
_BrMultiIFWebServicesName_Object=MibTableColumn
brMultiIFWebServicesName=_BrMultiIFWebServicesName_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,16,1,1,1),_BrMultiIFWebServicesName_Type())
brMultiIFWebServicesName.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFWebServicesName.setStatus(_A)
class _BrMultiIFWebServicesInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrMultiIFWebServicesInstanceID_Type.__name__=_B
_BrMultiIFWebServicesInstanceID_Object=MibTableColumn
brMultiIFWebServicesInstanceID=_BrMultiIFWebServicesInstanceID_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,16,1,1,2),_BrMultiIFWebServicesInstanceID_Type())
brMultiIFWebServicesInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFWebServicesInstanceID.setStatus(_A)
class _BrMultiIFWebServicesMetadataVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BrMultiIFWebServicesMetadataVersion_Type.__name__=_B
_BrMultiIFWebServicesMetadataVersion_Object=MibTableColumn
brMultiIFWebServicesMetadataVersion=_BrMultiIFWebServicesMetadataVersion_Object((1,3,6,1,4,1,2435,2,4,4,1240,5,16,1,1,3),_BrMultiIFWebServicesMetadataVersion_Type())
brMultiIFWebServicesMetadataVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:brMultiIFWebServicesMetadataVersion.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'brother':brother,'nm':nm,'system':system,'net-peripheral':net_peripheral,'net-printer':net_printer,'generalDeviceStatus':generalDeviceStatus,'status':status,'brJamPlace':brJamPlace,'tonerlow':tonerlow,'brToner1Low':brToner1Low,'brToner2Low':brToner2Low,'brToner3Low':brToner3Low,'brToner4Low':brToner4Low,'brieee1284id':brieee1284id,'brttt1':brttt1,'net-MFP':net_MFP,'fax-setup':fax_setup,'autodial':autodial,'onetouchDial':onetouchDial,'brOneTouchDialCount':brOneTouchDialCount,'brOneTouchDialTable':brOneTouchDialTable,'brOneTouchDialEntry':brOneTouchDialEntry,_AN:brOneTouchDialIndex,'brOneTouchDialData':brOneTouchDialData,'speedDial':speedDial,'brSpeedDialCount':brSpeedDialCount,'brSpeedDialTable':brSpeedDialTable,'brSpeedDialEntry':brSpeedDialEntry,_AO:brSpeedDialIndex,'brSpeedDialData':brSpeedDialData,'brDialDataAllClear':brDialDataAllClear,'fax-general':fax_general,'brFaxReceiveMode':brFaxReceiveMode,'brRingDelayCount':brRingDelayCount,'brOwnFaxNumber':brOwnFaxNumber,'scanner-setup':scanner_setup,'scanToInfo':scanToInfo,'brRegisterKeyInfo':brRegisterKeyInfo,'brUnRegisterKeyInfo':brUnRegisterKeyInfo,'brNetSKeyReceiverAddress':brNetSKeyReceiverAddress,'mfpCapability':mfpCapability,'mcGeneral':mcGeneral,'mcgRemoteSetup':mcgRemoteSetup,'brNetRemoteSetUpSupported':brNetRemoteSetUpSupported,'brNetRemoteSetUpEnable':brNetRemoteSetUpEnable,'brNetRemoteSetUpFileFormat':brNetRemoteSetUpFileFormat,'mcFax':mcFax,'mcfGeneral':mcfGeneral,'brFaxSupported':brFaxSupported,'brIFaxSupported':brIFaxSupported,'mcfNetFaxShare':mcfNetFaxShare,'brNetFaxShareSupported':brNetFaxShareSupported,'brNetFaxShareEnable':brNetFaxShareEnable,'mcfNetPcFaxRx':mcfNetPcFaxRx,'brNetPcFaxRxSupported':brNetPcFaxRxSupported,'brNetPcFaxRxEnable':brNetPcFaxRxEnable,'brNetRegisterPcFaxInfo':brNetRegisterPcFaxInfo,'mcfFaxInfomation':mcfFaxInfomation,'brPhoneNumberLastFax':brPhoneNumberLastFax,'brPagesSentLastFax':brPagesSentLastFax,'brTimestampLastFax':brTimestampLastFax,'brFaxHeaderInfo':brFaxHeaderInfo,'mcScanner':mcScanner,'mcsNetScanner':mcsNetScanner,'brNetScannerSupported':brNetScannerSupported,'brNetScannerEnable':brNetScannerEnable,'mcsNetSKy':mcsNetSKy,'brNetSKeySupported':brNetSKeySupported,'brNetSKeyEnable':brNetSKeyEnable,'mfpgeneral-setup':mfpgeneral_setup,'brServiceMode':brServiceMode,'brLockMode':brLockMode,'brActivityReportSetting':brActivityReportSetting,'netPML':netPML,'netPMLmgmt':netPMLmgmt,'device':device,'destination-subsystem1':destination_subsystem1,'sleep':sleep,'brpowerstime':brpowerstime,'autoc':autoc,'brautocont':brautocont,'simm':simm,'specification':specification,'simmkind0':simmkind0,'brsimmtype0':brsimmtype0,'brsimmsize0':brsimmsize0,'simmkind1':simmkind1,'brsimmtype1':brsimmtype1,'brsimmsize1':brsimmsize1,'simmkind2':simmkind2,'brsimmtype2':brsimmtype2,'brsimmsize2':brsimmsize2,'simmkind3':simmkind3,'brsimmtype3':brsimmtype3,'brsimmsize3':brsimmsize3,'bio1-explanation':bio1_explanation,'determined':determined,'brTBD1':brTBD1,'destination-subsystem2':destination_subsystem2,'printerjob':printerjob,'jobend':jobend,'brtimeout':brtimeout,'brTBD2':brTBD2,'destination-subsystem3':destination_subsystem3,'prt-setup':prt_setup,'prt-condition':prt_condition,'brpersonality':brpersonality,'brorientation':brorientation,'brcopies':brcopies,'brTBD3':brTBD3,'brresolution':brresolution,'brpageprotect':brpageprotect,'brlines':brlines,'brpaper':brpaper,'brpapertype':brpapertype,'brpapertype2':brpapertype2,'brpapertypeMP':brpapertypeMP,'destination-subsystem4':destination_subsystem4,'print-engine':print_engine,'prt-density':prt_density,'brdensity':brdensity,'status-prt-eng':status_prt_eng,'tray':tray,'manual':manual,'brmanualfeed':brmanualfeed,'traysize':traysize,'mp':mp,'brmpsize':brmpsize,'cassette':cassette,'brtray1size':brtray1size,'cassette2':cassette2,'brtray2size':brtray2size,'cassette3':cassette3,'brtray3size':brtray3size,'cassette4':cassette4,'brtray4size':brtray4size,'economy':economy,'brret':brret,'breconomode':breconomode,'brorg':brorg,'printersetup':printersetup,'general':general,'brPrtGeneralEmulationTimeout':brPrtGeneralEmulationTimeout,'brPrtGeneralFeeder':brPrtGeneralFeeder,'brPrtGeneralPowerSave':brPrtGeneralPowerSave,'brPrtGeneralBuzzer':brPrtGeneralBuzzer,'brPrtGeneralColor':brPrtGeneralColor,'brPrtGeneralDuplex':brPrtGeneralDuplex,'brPrtGeneralBinding':brPrtGeneralBinding,'advanced':advanced,'brPrtAdvancedPriority':brPrtAdvancedPriority,'brPrtAdvancedUseMPTrayFirst':brPrtAdvancedUseMPTrayFirst,'brPrtAdvancedMPTrayFeed':brPrtAdvancedMPTrayFeed,'brPrtAdvancedXOffset':brPrtAdvancedXOffset,'brPrtAdvancedYOffset':brPrtAdvancedYOffset,'brPrtAdvancedImageCompression':brPrtAdvancedImageCompression,'autoff':autoff,'brPrtAdvancedAutoFormFeed':brPrtAdvancedAutoFormFeed,'brPrtAdvancedAutoTimeout':brPrtAdvancedAutoTimeout,'brPrtAdvancedFFSuppress':brPrtAdvancedFFSuppress,'brPrtAdvancedTonerLowPrint':brPrtAdvancedTonerLowPrint,'brPrtAdvancedPrintDensity':brPrtAdvancedPrintDensity,'brPrtAdvancedInputBuffer':brPrtAdvancedInputBuffer,'brPrtAdvancedLanguage':brPrtAdvancedLanguage,'brSecurePrintRAMSizeMax':brSecurePrintRAMSizeMax,'brSecurePrintRAMSize':brSecurePrintRAMSize,'brPrtAdvancedJamRecovery':brPrtAdvancedJamRecovery,'brPrtAdvancedSleepIndication':brPrtAdvancedSleepIndication,'brPrtAdvancedDestination':brPrtAdvancedDestination,'brPrtAdvancedLowerLCD':brPrtAdvancedLowerLCD,'brPrtAdvancedAutoOnline':brPrtAdvancedAutoOnline,'brPrtAdvancedButtonRepeat':brPrtAdvancedButtonRepeat,'brPrtAdvancedMessageScroll':brPrtAdvancedMessageScroll,'buzzer':buzzer,'brPrtAdvancedErrorBuzzer':brPrtAdvancedErrorBuzzer,'brPrtAdvancedPanelBuzzer':brPrtAdvancedPanelBuzzer,'brPrtAdvancedBuzzerVolume':brPrtAdvancedBuzzerVolume,'brPrtAdvancedLCDDensity':brPrtAdvancedLCDDensity,'smallPaperSize':smallPaperSize,'brSmallPaperSizeMP':brSmallPaperSizeMP,'brSmallPaperSize1':brSmallPaperSize1,'brSmallPaperSize2':brSmallPaperSize2,'brSmallPaperSize3':brSmallPaperSize3,'brSmallPaperSize4':brSmallPaperSize4,'trayPriority':trayPriority,'brPrtAdvancedTrayPriority':brPrtAdvancedTrayPriority,'brTrayPriorityCount':brTrayPriorityCount,'brTrayPriorityTable':brTrayPriorityTable,'brTrayPriorityEntry':brTrayPriorityEntry,_AS:brTrayPriorityIndex,'brTrayPriorityMember':brTrayPriorityMember,'carbonCopy':carbonCopy,'brCarbonCopyMode':brCarbonCopyMode,'brCarbonCopies':brCarbonCopies,'brCarbonCopyTable':brCarbonCopyTable,'brCarbonCopyEntry':brCarbonCopyEntry,_AT:brCarbonCopyIndex,'brCarbonCopyTray':brCarbonCopyTray,'brCarbonCopyMacro':brCarbonCopyMacro,'brCarbonCopyMacroID':brCarbonCopyMacroID,'mediaFix':mediaFix,'brMediaFixTray1':brMediaFixTray1,'brMediaFixTray2':brMediaFixTray2,'brMediaFixTray3':brMediaFixTray3,'brMediaFixTray4':brMediaFixTray4,'brMediaFixMP':brMediaFixMP,'directprint':directprint,'brDirectPrintPaperSize':brDirectPrintPaperSize,'brDirectPrintMediaType':brDirectPrintMediaType,'brDirectPrintMultipulPage':brDirectPrintMultipulPage,'brDirectPrintOrientation':brDirectPrintOrientation,'brDirectPrintCollate':brDirectPrintCollate,'brDirectPrintOutputColor':brDirectPrintOutputColor,'brDirectPrintPrintQuality':brDirectPrintPrintQuality,'brDirectPrintPdfOption':brDirectPrintPdfOption,'brDirectPrintSetting':brDirectPrintSetting,'brDirectPrintPdfThumbnailType':brDirectPrintPdfThumbnailType,'pictbridge':pictbridge,'brPictBridgePaperSize':brPictBridgePaperSize,'brPictBridgeOrientation':brPictBridgeOrientation,'brPictBridgeDateTime':brPictBridgeDateTime,'brPictBridgeFileName':brPictBridgeFileName,'brPictBridgePrintQuality':brPictBridgePrintQuality,'brPictBridgePrintSetting':brPictBridgePrintSetting,'colorcorrection':colorcorrection,'brColorCalibration':brColorCalibration,'brColorCalibrationReset':brColorCalibrationReset,'brAutoRegistRegistrate':brAutoRegistRegistrate,'brAutoRegistSetInterval':brAutoRegistSetInterval,'brRegistrationPrintChart':brRegistrationPrintChart,'brRegistrationXMagentaLeft':brRegistrationXMagentaLeft,'brRegistrationXMagentaRight':brRegistrationXMagentaRight,'brRegistrationXCyanLeft':brRegistrationXCyanLeft,'brRegistrationXCyanRight':brRegistrationXCyanRight,'brRegistrationXYellowLeft':brRegistrationXYellowLeft,'brRegistrationXYellowRight':brRegistrationXYellowRight,'brRegistrationYMagenta':brRegistrationYMagenta,'brRegistrationYCyan':brRegistrationYCyan,'brRegistrationYYellow':brRegistrationYYellow,'funclock':funclock,'brFuncLockSettingInit':brFuncLockSettingInit,'brFuncLockAdminPassword':brFuncLockAdminPassword,'brFuncLock':brFuncLock,'brFuncLockPublicFuncCount':brFuncLockPublicFuncCount,'brFuncLockPublicTable':brFuncLockPublicTable,'brFuncLockPublicEntry':brFuncLockPublicEntry,_AU:brFuncLockPublicFuncIndex,'brFuncLockPublicFuncMember':brFuncLockPublicFuncMember,'brFuncLockPublicFuncSupported':brFuncLockPublicFuncSupported,'brFuncLockPublicFuncEnable':brFuncLockPublicFuncEnable,'brFuncLockUserCount':brFuncLockUserCount,'brFuncLockUserTable':brFuncLockUserTable,'brFuncLockUserEntry':brFuncLockUserEntry,_AJ:brFuncLockUserIndex,'brFuncLockUserName':brFuncLockUserName,'brFuncLockUserPassword':brFuncLockUserPassword,'brFuncLockUserFuncCount':brFuncLockUserFuncCount,'brFuncLockUserFuncTable':brFuncLockUserFuncTable,'brFuncLockUserFuncEntry':brFuncLockUserFuncEntry,_AV:brFuncLockUserFuncIndex,'brFuncLockUserFuncMember':brFuncLockUserFuncMember,'brFuncLockUserFuncSupported':brFuncLockUserFuncSupported,'brFuncLockUserFuncEnable':brFuncLockUserFuncEnable,'brFuncLockSetting':brFuncLockSetting,'brFuncLockUserPrintPageCounterReset':brFuncLockUserPrintPageCounterReset,'brFuncLockPublicPrintLimitEnable':brFuncLockPublicPrintLimitEnable,'brFuncLockPublicPrintPageMax':brFuncLockPublicPrintPageMax,'brFuncLockPublicPrintPageCountMono':brFuncLockPublicPrintPageCountMono,'brFuncLockPublicPrintPageCountColor':brFuncLockPublicPrintPageCountColor,'brFuncLockUserPrintPageTable':brFuncLockUserPrintPageTable,'brFuncLockUserPrintPageEntry':brFuncLockUserPrintPageEntry,_AW:brFuncLockUserPrintPageIndex,'brFuncLockUserPrintPageLimitEnable':brFuncLockUserPrintPageLimitEnable,'brFuncLockUserPrintPageCountMono':brFuncLockUserPrintPageCountMono,'brFuncLockUserPrintPageCountColor':brFuncLockUserPrintPageCountColor,'brFuncLockUserPrintPageMax':brFuncLockUserPrintPageMax,'brFuncLockUserPrintPageCountMonoLast':brFuncLockUserPrintPageCountMonoLast,'brFuncLockUserPrintPageCountColorLast':brFuncLockUserPrintPageCountColorLast,'brFuncLockPcLoginNameAuthEnable':brFuncLockPcLoginNameAuthEnable,'brFuncLockPcLoginNameAuthCount':brFuncLockPcLoginNameAuthCount,'brFuncLockPcLoginNameTable':brFuncLockPcLoginNameTable,'brFuncLockPcLoginNameEntry':brFuncLockPcLoginNameEntry,_AX:brFuncLockPcLoginNameAuthIndex,'brFuncLockPcLoginName':brFuncLockPcLoginName,'brFuncLockPcLoginNameAuthID':brFuncLockPcLoginNameAuthID,'brFuncLockPublicPrintPageCountMonoLast':brFuncLockPublicPrintPageCountMonoLast,'brFuncLockPublicPrintPageCountColorLast':brFuncLockPublicPrintPageCountColorLast,'autocountreset':autocountreset,'brFuncLockAutoCountResetFrequency':brFuncLockAutoCountResetFrequency,'brFuncLockAutoCountResetTime':brFuncLockAutoCountResetTime,'brFuncLockAutoCountResetWeek':brFuncLockAutoCountResetWeek,'brFuncLockAutoCountResetDate':brFuncLockAutoCountResetDate,'mail':mail,'brPrtMailbox':brPrtMailbox,'brPrtMailboxProtectTable':brPrtMailboxProtectTable,'brPrtMailboxProtectEntry':brPrtMailboxProtectEntry,_AY:brPrtMailboxProtectIndex,'brPrtMailboxProtect':brPrtMailboxProtect,'brPrtAvoidMailboxFullTable':brPrtAvoidMailboxFullTable,'brPrtAvoidMailboxFullEntry':brPrtAvoidMailboxFullEntry,_AZ:brPrtAvoidMailboxFullIndex,'brPrtAvoidMailboxFull':brPrtAvoidMailboxFull,'brPrtMailboxOutbin':brPrtMailboxOutbin,'brPrtMailboxProtectGroup':brPrtMailboxProtectGroup,'brPrtAvoidMailboxFullGroup':brPrtAvoidMailboxFullGroup,'finisher':finisher,'brPrtFinisher':brPrtFinisher,'catch-tray':catch_tray,'brPrtCatchTray':brPrtCatchTray,'pagesetup':pagesetup,'pcl':pcl,'margin-p':margin_p,'brPagePCLLeftMargin':brPagePCLLeftMargin,'brPagePCLRightMargin':brPagePCLRightMargin,'brPagePCLTopMargin':brPagePCLTopMargin,'brPagePCLBottomMargin':brPagePCLBottomMargin,'brPagePCLLines':brPagePCLLines,'auto-p':auto_p,'brPagePCLAutoLF':brPagePCLAutoLF,'brPagePCLAutoCR':brPagePCLAutoCR,'brPagePCLAutoWrap':brPagePCLAutoWrap,'brPagePCLAutoSkip':brPagePCLAutoSkip,'ps':ps,'brPagePSPrintPSError':brPagePSPrintPSError,'brPagePSKeepPCLFonts':brPagePSKeepPCLFonts,'brPagePSCAPTsetting':brPagePSCAPTsetting,'gl':gl,'pen1':pen1,'brPageGLPen1Size':brPageGLPen1Size,'brPageGLPen1GrayLevel':brPageGLPen1GrayLevel,'pen2':pen2,'brPageGLPen2Size':brPageGLPen2Size,'brPageGLPen2GrayLevel':brPageGLPen2GrayLevel,'pen3':pen3,'brPageGLPen3Size':brPageGLPen3Size,'brPageGLPen3GrayLevel':brPageGLPen3GrayLevel,'pen4':pen4,'brPageGLPen4Size':brPageGLPen4Size,'brPageGLPen4GrayLevel':brPageGLPen4GrayLevel,'pen5':pen5,'brPageGLPen5Size':brPageGLPen5Size,'brPageGLPen5GrayLevel':brPageGLPen5GrayLevel,'pen6':pen6,'brPageGLPen6Size':brPageGLPen6Size,'brPageGLPen6GrayLevel':brPageGLPen6GrayLevel,'epson':epson,'margin-e':margin_e,'brPageEPSONLeftMargin':brPageEPSONLeftMargin,'brPageEPSONRightMargin':brPageEPSONRightMargin,'brPageEPSONTopMargin':brPageEPSONTopMargin,'brPageEPSONBottomMargin':brPageEPSONBottomMargin,'brPageEPSONLines':brPageEPSONLines,'auto-e':auto_e,'brPageEPSONAutoLF':brPageEPSONAutoLF,'brPageEPSONAutoMask':brPageEPSONAutoMask,'ibm':ibm,'margin-i':margin_i,'brPageIBMLeftMargin':brPageIBMLeftMargin,'brPageIBMRightMargin':brPageIBMRightMargin,'brPageIBMTopMargin':brPageIBMTopMargin,'brPageIBMBottomMargin':brPageIBMBottomMargin,'brPageIBMLines':brPageIBMLines,'auto-i':auto_i,'brPageIBMAutoLF':brPageIBMAutoLF,'brPageIBMAutoCR':brPageIBMAutoCR,'brPageIBMAutoMask':brPageIBMAutoMask,'fontsetup':fontsetup,'brFontName':brFontName,'brFontPointSize':brFontPointSize,'brFontPitch':brFontPitch,'brFontSymbolSet':brFontSymbolSet,'controlpanel':controlpanel,'reset':reset,'brPanelResetUser':brPanelResetUser,'brPanelResetFactory':brPanelResetFactory,'test':test,'brPanelTestConfiguration':brPanelTestConfiguration,'brPanelTestFontList':brPanelTestFontList,'brPanelTestTestPage':brPanelTestTestPage,'brPanelTestDemoPage':brPanelTestDemoPage,'panellock':panellock,'brPanelLockPasswd':brPanelLockPasswd,'brPanelLock':brPanelLock,'brPanelLockOn':brPanelLockOn,'brPanelLockOff':brPanelLockOff,'key':key,'brPanelKeyOnline':brPanelKeyOnline,'brPanelKeyFormFeed':brPanelKeyFormFeed,'brPanelKeyContinue':brPanelKeyContinue,'brPanelKeyMode':brPanelKeyMode,'brPanelKeyGo':brPanelKeyGo,'brPanelKeyJobCancel':brPanelKeyJobCancel,'brPanelKeyReprint':brPanelKeyReprint,'brPanelKeySecure':brPanelKeySecure,'panelinfo':panelinfo,'brLCDMode1':brLCDMode1,'brLCDString1':brLCDString1,'brLCDMode2':brLCDMode2,'brLCDString2':brLCDString2,'brLCDString16fix':brLCDString16fix,'brBackLightColor':brBackLightColor,'brLCDMode3':brLCDMode3,'brLCDString3':brLCDString3,'brLCDMode4':brLCDMode4,'brLCDString4':brLCDString4,'brLCDMode5':brLCDMode5,'brLCDString5':brLCDString5,'brLCDContrast':brLCDContrast,'printerinfomation':printerinfomation,'brInfoSerialNumber':brInfoSerialNumber,'brInfoType':brInfoType,'version':version,'brInfoUpperMIBVer':brInfoUpperMIBVer,'brInfoLowerMIBVer':brInfoLowerMIBVer,'brInfoStatus':brInfoStatus,'brInfoNetVerUpStatus':brInfoNetVerUpStatus,'brInfoPrinterUStatus':brInfoPrinterUStatus,'brInfoPConSupported':brInfoPConSupported,'brInfoMaintenance':brInfoMaintenance,'brInfoModelNumber':brInfoModelNumber,'brInfoCounter':brInfoCounter,'brInfoNextCare':brInfoNextCare,'brInfoHDDSlot1':brInfoHDDSlot1,'brInfoHDDSlot2':brInfoHDDSlot2,'brInfoHDDInternal':brInfoHDDInternal,'brInfoHDDSize':brInfoHDDSize,'brInfoSolutionsCenterURL':brInfoSolutionsCenterURL,'brInfoDeviceRomVersion':brInfoDeviceRomVersion,'brInfoCoverage':brInfoCoverage,'brInfoEstimatedPagesRemaining':brInfoEstimatedPagesRemaining,'brInfoReplaceCount':brInfoReplaceCount,'brInfoJamCount':brInfoJamCount,'brInfoJamCountClear':brInfoJamCountClear,'brInfoReplaceTime':brInfoReplaceTime,'brInfoDeviceSubRomVersion':brInfoDeviceSubRomVersion,'brInfoAlertVersion':brInfoAlertVersion,'brInfoBlackPrint':brInfoBlackPrint,'errorHistory':errorHistory,'brErrorHistoryCount':brErrorHistoryCount,'brErrorHistoryTable':brErrorHistoryTable,'brErrorHistoryEntry':brErrorHistoryEntry,_Aa:brErrorHistoryIndex,'brErrorHistoryDescription':brErrorHistoryDescription,'brErrorHistoryAllClear':brErrorHistoryAllClear,'brCommunicationErrorHistoryCount':brCommunicationErrorHistoryCount,'brCommunicationErrorHistoryTable':brCommunicationErrorHistoryTable,'brCommunicationErrorHistoryEntry':brCommunicationErrorHistoryEntry,_Ab:brCommunicationErrorHistoryIndex,'brCommunicationErrorHistoryDescription':brCommunicationErrorHistoryDescription,'printPages':printPages,'brPrintPagesTable':brPrintPagesTable,'brPrintPagesEntry':brPrintPagesEntry,_Ac:brPrintPagesIndex,'brPrintPagesPaperSize':brPrintPagesPaperSize,'brPrintPages':brPrintPages,'brPrintPagesMediaPlaceTable':brPrintPagesMediaPlaceTable,'brPrintPagesMediaPlaceEntry':brPrintPagesMediaPlaceEntry,_Ad:brPrintPagesMediaPlaceIndex,'brPrintPagesMediaPlaceType':brPrintPagesMediaPlaceType,'brPrintPagesMediaPlaceCounter':brPrintPagesMediaPlaceCounter,'brPrintPagesFuncTable':brPrintPagesFuncTable,'brPrintPagesFuncEntry':brPrintPagesFuncEntry,_Ae:brPrintPagesFuncIndex,'brPrintPagesFuncType':brPrintPagesFuncType,'brPrintPagesFuncCounter':brPrintPagesFuncCounter,'brPrintPagesPaperTypeTable':brPrintPagesPaperTypeTable,'brPrintPagesPaperTypeEntry':brPrintPagesPaperTypeEntry,_Af:brPrintPagesPaperTypeIndex,'brPrintPagesPaperTypeType':brPrintPagesPaperTypeType,'brPrintPagesPaperTypeCounter':brPrintPagesPaperTypeCounter,'capability':capability,'copies':copies,'brCapabilityCopiesMax':brCapabilityCopiesMax,'brCapabilityCopiesMin':brCapabilityCopiesMin,'orientation':orientation,'brCapabilityOrientationCount':brCapabilityOrientationCount,'brCapabilityOrientationTable':brCapabilityOrientationTable,'brCapabilityOrientationEntry':brCapabilityOrientationEntry,_Ag:brCapabilityOrientationIndex,'brCapabilityOrientationName':brCapabilityOrientationName,'paper':paper,'brCapabilityPaperCount':brCapabilityPaperCount,'brCapabilityPaperTable':brCapabilityPaperTable,'brCapabilityPaperEntry':brCapabilityPaperEntry,_Ah:brCapabilityPaperIndex,'brCapabilityPaperName':brCapabilityPaperName,'mediatype':mediatype,'brCapabilityMediatypeCount':brCapabilityMediatypeCount,'brCapabilityMediatypeTable':brCapabilityMediatypeTable,'brCapabilityMediatypeEntry':brCapabilityMediatypeEntry,_Ai:brCapabilityMediatypeIndex,'brCapabilityMediatypeName':brCapabilityMediatypeName,'resolution':resolution,'brCapabilityResolutionCount':brCapabilityResolutionCount,'brCapabilityResolutionTable':brCapabilityResolutionTable,'brCapabilityResolutionEntry':brCapabilityResolutionEntry,_Aj:brCapabilityResolutionIndex,'brCapabilityResolution':brCapabilityResolution,'countinfo':countinfo,'pfkit':pfkit,'brPfKitIndexCount':brPfKitIndexCount,'brPfKitTable':brPfKitTable,'brPfKitEntry':brPfKitEntry,_Ak:brPfKitIndex,'brPfKitType':brPfKitType,'brPfKitCount':brPfKitCount,'scancount':scancount,'brScanCountIndexCount':brScanCountIndexCount,'brScanCountTable':brScanCountTable,'brScanCountEntry':brScanCountEntry,_Al:brScanCountIndex,'brScanCountType':brScanCountType,'brScanCountCounter':brScanCountCounter,'firmwareupdatekeyword':firmwareupdatekeyword,'brFirmwareUpdateKeywordCount':brFirmwareUpdateKeywordCount,'brFirmwareUpdateKeywordTable':brFirmwareUpdateKeywordTable,'brFirmwareUpdateKeywordEntry':brFirmwareUpdateKeywordEntry,_Am:brFirmwareUpdateKeywordIndex,'brFirmwareUpdateKeyword':brFirmwareUpdateKeyword,'printerstatus':printerstatus,'brStatusSleep':brStatusSleep,'secret':secret,'brSecretMPRetry':brSecretMPRetry,'brSecretReprint':brSecretReprint,'brFontSetting':brFontSetting,'brFontSwitchOn':brFontSwitchOn,'brFontSwitchOff':brFontSwitchOff,'adminsetting':adminsetting,'clockfunction':clockfunction,'brClockFuncTimeStyle':brClockFuncTimeStyle,'brClockFuncSummerTime':brClockFuncSummerTime,'brClockFuncTimeZone':brClockFuncTimeZone,'brClockFuncZoneSet':brClockFuncZoneSet,'interface':interface,'npCard':npCard,'npSys':npSys,'npConfig':npConfig,'brBasicSettingConfigured':brBasicSettingConfigured,'adminCapa':adminCapa,'brAdminCapability':brAdminCapability,'userSetting':userSetting,'brUserPasswordVerify':brUserPasswordVerify,'brUserPassword':brUserPassword,'verify':verify,'brpsVerifyPhysAddress':brpsVerifyPhysAddress,'npTcp':npTcp,'lpd':lpd,'banner':banner,'brLPDBannerPage':brLPDBannerPage,'npCtl':npCtl,'etherN':etherN,'eNet':eNet,'brENetModeSupported':brENetModeSupported,'brENetMode':brENetMode,'npPort':npPort,'funa':funa,'brFindPort':brFindPort,'brFindTime':brFindTime,'npSet':npSet,'dns':dns,'brDNSSupported':brDNSSupported,'brPrimaryDNSIP':brPrimaryDNSIP,'brSecondaryDNSIP':brSecondaryDNSIP,'brDNSIPSetup':brDNSIPSetup,'brTCPIPConnectTime':brTCPIPConnectTime,'brAdvancedDNSSupported':brAdvancedDNSSupported,'brPrimaryDNSIPAddress':brPrimaryDNSIPAddress,'brSecondaryDNSIPAddress':brSecondaryDNSIPAddress,'brPOP3ServerName':brPOP3ServerName,'brSMTPServerName':brSMTPServerName,'pushstatus':pushstatus,'brPushStatusSupported':brPushStatusSupported,'priadmin':priadmin,'brPriMailAddress':brPriMailAddress,'brPriError':brPriError,'secadmin':secadmin,'brSecMailAddress':brSecMailAddress,'brSecError':brSecError,'brNotificationCount':brNotificationCount,'brNotificationTable':brNotificationTable,'brNotificationEntry':brNotificationEntry,_AK:brNotificationIndex,'brNotificationAddress':brNotificationAddress,'brNotificationStatusGroup':brNotificationStatusGroup,'brNotificationShowURLInfo':brNotificationShowURLInfo,'brNotificationErrorRule':brNotificationErrorRule,'brNotificationRestoration':brNotificationRestoration,'brPrintersEmailaddress':brPrintersEmailaddress,'brNotificationVersion':brNotificationVersion,'brShowIPAddressInfo':brShowIPAddressInfo,'brNotificationRuleTable':brNotificationRuleTable,'brNotificationRuleEntry':brNotificationRuleEntry,_An:brNotificationRuleIndex,'brNotificationStatusID':brNotificationStatusID,'brNotificationMainRule':brNotificationMainRule,'brNotificationRuleValue':brNotificationRuleValue,'pjl':pjl,'pjlinfo':pjlinfo,'brPJLInfoOptionsTable':brPJLInfoOptionsTable,'brPJLInfoOptionsEntry':brPJLInfoOptionsEntry,_Ao:brPJLInfoOptionsIndex,'brPJLInfoOptions':brPJLInfoOptions,'brPJLInfoIntrayconfigTable':brPJLInfoIntrayconfigTable,'brPJLInfoIntrayconfigEntry':brPJLInfoIntrayconfigEntry,_Ap:brPJLInfoIntrayconfigIndex,'brPJLInfoIntrayconfig':brPJLInfoIntrayconfig,'brPJLInfoOuttrayconfigTable':brPJLInfoOuttrayconfigTable,'brPJLInfoOuttrayconfigEntry':brPJLInfoOuttrayconfigEntry,_Aq:brPJLInfoOuttrayconfigIndex,'brPJLInfoOuttrayconfig':brPJLInfoOuttrayconfig,'brPJLInfoDXconfigTable':brPJLInfoDXconfigTable,'brPJLInfoDXconfigEntry':brPJLInfoDXconfigEntry,_Ar:brPJLInfoDXconfigIndex,'brPJLInfoDXconfig':brPJLInfoDXconfig,'brPJLInfoStorageconfigTable':brPJLInfoStorageconfigTable,'brPJLInfoStorageconfigEntry':brPJLInfoStorageconfigEntry,_As:brPJLInfoStorageconfigIndex,'brPJLInfoStorageconfig':brPJLInfoStorageconfig,'brPJLInfoFirmwareUpdateconfigTable':brPJLInfoFirmwareUpdateconfigTable,'brPJLInfoFirmwareUpdateconfigEntry':brPJLInfoFirmwareUpdateconfigEntry,_At:brPJLInfoFirmwareUpdateconfigIndex,'brPJLInfoFirmwareUpdateconfig':brPJLInfoFirmwareUpdateconfig,'eMailReports':eMailReports,'brEmailReportsSupported':brEmailReportsSupported,'brEmailReportsCount':brEmailReportsCount,'brEmailReportsTable':brEmailReportsTable,'brEmailReportsEntry':brEmailReportsEntry,_Au:brEmailReportsIndex,'brEmailReportsAddress':brEmailReportsAddress,'brEmailReportsFrequency':brEmailReportsFrequency,'brEmailReportsTime':brEmailReportsTime,'brEmailReportsWeek':brEmailReportsWeek,'brEmailReportsDate':brEmailReportsDate,'brEmailReportsSendReportNow':brEmailReportsSendReportNow,'brEmailReportsSendReportatPowerOn':brEmailReportsSendReportatPowerOn,'brEmailReportsNoRTCFrequency':brEmailReportsNoRTCFrequency,'brEmailReportsReportFormat':brEmailReportsReportFormat,'wireless':wireless,'wlInfo':wlInfo,'wlCapability':wlCapability,'brpsWLanDot11Supported':brpsWLanDot11Supported,'brpsWLanAvailableChannel':brpsWLanAvailableChannel,'brpsWLanCapabilityEncryptModeCount':brpsWLanCapabilityEncryptModeCount,'brpsWLanCapabilityEncryptModeTable':brpsWLanCapabilityEncryptModeTable,'brpsWLanCapabilityEncryptModeEntry':brpsWLanCapabilityEncryptModeEntry,_Av:brpsWLanCapabilityEncryptModeIndex,'brpsWLanCapabilityEncryptModeType':brpsWLanCapabilityEncryptModeType,'brpsWLanCapabilityEncryptModeDescription':brpsWLanCapabilityEncryptModeDescription,'brpsWLanCapabilityEncryptModeSupported':brpsWLanCapabilityEncryptModeSupported,'brpsWLanCapabilityAuthModeCount':brpsWLanCapabilityAuthModeCount,'brpsWLanCapabilityAuthModeTable':brpsWLanCapabilityAuthModeTable,'brpsWLanCapabilityAuthModeEntry':brpsWLanCapabilityAuthModeEntry,_Aw:brpsWLanCapabilitAuthModeIndex,'brpsWLanCapabilityAuthModeType':brpsWLanCapabilityAuthModeType,'brpsWLanCapabilityAuthModeDescription':brpsWLanCapabilityAuthModeDescription,'brpsWLanCapabilityAuthModeSupported':brpsWLanCapabilityAuthModeSupported,'brpsWLanCapabilityAuthEAPCount':brpsWLanCapabilityAuthEAPCount,'brpsWLanCapabilityAuthEAPTable':brpsWLanCapabilityAuthEAPTable,'brpsWLanCapabilityAuthEAPEntry':brpsWLanCapabilityAuthEAPEntry,_Ax:brpsWLanCapabilityAuthEAPIndex,'brpsWLanCapabilityAuthEAPType':brpsWLanCapabilityAuthEAPType,'brpsWLanCapabilityAuthEAPDescription':brpsWLanCapabilityAuthEAPDescription,'brpsWLanCapabilityAuthEAPSupported':brpsWLanCapabilityAuthEAPSupported,'brpsWLanCapabilityAuthEAPSupportAuthentication':brpsWLanCapabilityAuthEAPSupportAuthentication,'brpsWLanCapabilityAuthEAPSupportEncryption':brpsWLanCapabilityAuthEAPSupportEncryption,'wlGeneralInfo':wlGeneralInfo,'brpsWLanDestination':brpsWLanDestination,'brpsWLanTransmitLevel':brpsWLanTransmitLevel,'brpsPit3WLanTestStatus':brpsPit3WLanTestStatus,'wlNetSearch':wlNetSearch,'brpsWLanNetSearchSupported':brpsWLanNetSearchSupported,'brpsAvailableWLanScan':brpsAvailableWLanScan,'brpsAvailableWLanScanWaitTime':brpsAvailableWLanScanWaitTime,'brpsAvailableWLanCount':brpsAvailableWLanCount,'brpsAvailableWLanTable':brpsAvailableWLanTable,'brpsAvailableWLanEntry':brpsAvailableWLanEntry,_Ay:brpsAvailableWLanIndex,'brpsAvailableWLanName':brpsAvailableWLanName,'brpsAvailableWLanMode':brpsAvailableWLanMode,'brpsAvailableWLanCommMode':brpsAvailableWLanCommMode,'brpsAvailableWLanChannel':brpsAvailableWLanChannel,'brpsAvailableWLanPowerLevel':brpsAvailableWLanPowerLevel,'brpsAvailableWLanAuthMode':brpsAvailableWLanAuthMode,'brpsAvailableWLanEncryptMode':brpsAvailableWLanEncryptMode,'wlAOSS':wlAOSS,'brpsWLanAOSSSupported':brpsWLanAOSSSupported,'brpsWLanAOSSIsRunnning':brpsWLanAOSSIsRunnning,'wlSES':wlSES,'brpsWLanSESSupported':brpsWLanSESSupported,'wlWPS':wlWPS,'brpsWLanWPSSupported':brpsWLanWPSSupported,'brpsWLanWPSResult':brpsWLanWPSResult,'wlSimpleWizard':wlSimpleWizard,'brWlanSimpleWizardSupported':brWlanSimpleWizardSupported,'brWlanSimpleWizardPassword':brWlanSimpleWizardPassword,'wlSetup':wlSetup,'wlGeneral':wlGeneral,'brpsWLanAPSetupMode':brpsWLanAPSetupMode,'brpsWLanMode':brpsWLanMode,'brpsWLanName':brpsWLanName,'brpsWLanCommMode':brpsWLanCommMode,'brpsWLanChannel':brpsWLanChannel,'wlAdvanced':wlAdvanced,'brpsWLanCtsMode':brpsWLanCtsMode,'brpsWLanCtsRate':brpsWLanCtsRate,'brpsWLanCtsType':brpsWLanCtsType,'brpsWLanRtsCtsThreshold':brpsWLanRtsCtsThreshold,'brpsWLanLengthThreshold':brpsWLanLengthThreshold,'brpsWLanDataRetry':brpsWLanDataRetry,'brpsWLanTransmitPowerSetting':brpsWLanTransmitPowerSetting,'brpsWLanDeviceType':brpsWLanDeviceType,'wlAssociate':wlAssociate,'brpsWLanEncryptMode':brpsWLanEncryptMode,'brpsWLanAuthMode':brpsWLanAuthMode,'brpsWLanAuthEAP':brpsWLanAuthEAP,'brpsWLanAuthUserID':brpsWLanAuthUserID,'brpsWLanAuthUserPass':brpsWLanAuthUserPass,'brpsWLanAssociate':brpsWLanAssociate,'brpsWLanAssociateTestResult':brpsWLanAssociateTestResult,'brpsWLanAssociateResult':brpsWLanAssociateResult,'brpsWLanAssociateTestSupported':brpsWLanAssociateTestSupported,'wlWEP':wlWEP,'brpsWLanWepKeyDefaultIndex':brpsWLanWepKeyDefaultIndex,'brpsWLanWepKeyTable':brpsWLanWepKeyTable,'brpsWLanWepKeyEntry':brpsWLanWepKeyEntry,_B3:brpsWLanWepKeyIndex,'brpsWLanWepKeySize':brpsWLanWepKeySize,'brpsWLanWepKeyType':brpsWLanWepKeyType,'brpsWLanWepKey':brpsWLanWepKey,'wlWPA':wlWPA,'brpsWLanNetworkKey':brpsWLanNetworkKey,'wlTKIP':wlTKIP,'brpsWLanTKIPChangeInterval':brpsWLanTKIPChangeInterval,'wlLEAP':wlLEAP,'brpsWLanLEAPTimeout':brpsWLanLEAPTimeout,'wlStatus':wlStatus,'wlGeneralStatus':wlGeneralStatus,'brpsWLanOperatingMode':brpsWLanOperatingMode,'brpsWLanRSSLevel':brpsWLanRSSLevel,'brpsWLanCommSpeed':brpsWLanCommSpeed,'brpsWLanOperatingChannel':brpsWLanOperatingChannel,'brpsWLanOperatingName':brpsWLanOperatingName,'brpsWLanOperatingCommMode':brpsWLanOperatingCommMode,'brpsWLanOperatingEncryptMode':brpsWLanOperatingEncryptMode,'brpsWLanOperatingAuthMode':brpsWLanOperatingAuthMode,'brpsWLanOperatingWepKeyDefaultIndex':brpsWLanOperatingWepKeyDefaultIndex,'brnetConfig':brnetConfig,'brconfig':brconfig,'brpsNodeName':brpsNodeName,'brpsSerialNumber':brpsSerialNumber,'brpsHardwareType':brpsHardwareType,'brpsMainRevision':brpsMainRevision,'brpsBootRevision':brpsBootRevision,'brpsPasswordVerify':brpsPasswordVerify,'brpsPassword':brpsPassword,'brpsMIBVersion':brpsMIBVersion,'brpsOEMString':brpsOEMString,'brpsMIBMajor':brpsMIBMajor,'brpsMIBMinor':brpsMIBMinor,'brpsServerDescription':brpsServerDescription,'brpsEnetMode':brpsEnetMode,'brpsFlashROMSize':brpsFlashROMSize,'brpsSNMPGetCommunity':brpsSNMPGetCommunity,'brpsSNMPJetAdmin':brpsSNMPJetAdmin,'brpsSNMPSetCommunity1':brpsSNMPSetCommunity1,'brpsSNMPSetCommunity2':brpsSNMPSetCommunity2,'brSupportedInfo':brSupportedInfo,'brcontrol':brcontrol,'brpsTestPage':brpsTestPage,'brpsSetDefault':brpsSetDefault,'brpsReset':brpsReset,'brpsProtectModeEnable':brpsProtectModeEnable,'brpsProtectPassword':brpsProtectPassword,'brport':brport,'brpsPortCount':brpsPortCount,'brpsPortInfoTable':brpsPortInfoTable,'brpsPortInfoEntry':brpsPortInfoEntry,_B4:brpsPortIndex,'brpsPortName':brpsPortName,'brpsPortType':brpsPortType,'brpsPortStatus':brpsPortStatus,'brpsPortStatusString':brpsPortStatusString,'brpsPortProtocol':brpsPortProtocol,'brpsPortQueueSize':brpsPortQueueSize,'brpsPortDescriptionString':brpsPortDescriptionString,'brpsPortInfoString':brpsPortInfoString,'brpsPortHTTPExtensions':brpsPortHTTPExtensions,'brpsPortSNMPExtensions':brpsPortSNMPExtensions,'brpsPortAttribute':brpsPortAttribute,'brpsPortBinaryMode':brpsPortBinaryMode,'brpsPortInhibitDatagramSupport':brpsPortInhibitDatagramSupport,'brservice':brservice,'brpsServiceCount':brpsServiceCount,'brpsServiceInfoTable':brpsServiceInfoTable,'brpsServiceInfoEntry':brpsServiceInfoEntry,_AL:brpsServiceIndex,'brpsServiceName':brpsServiceName,'brpsServicePort':brpsServicePort,'brpsServiceFilter':brpsServiceFilter,'brpsServiceBOT':brpsServiceBOT,'brpsServiceEOT':brpsServiceEOT,'brpsServiceMatch':brpsServiceMatch,'brpsServiceReplace':brpsServiceReplace,'brpsServiceTCPPort':brpsServiceTCPPort,'brpsServiceNDSTree':brpsServiceNDSTree,'brpsServiceNDSContext':brpsServiceNDSContext,'brpsServiceVines':brpsServiceVines,'brpsServiceObsolete':brpsServiceObsolete,'brpsServiceNetwareServerCount':brpsServiceNetwareServerCount,'brpsServiceReceiveOnly':brpsServiceReceiveOnly,'brpsServiceTCPQueued':brpsServiceTCPQueued,'brpsServiceProtocolLAT':brpsServiceProtocolLAT,'brpsServiceProtocolTCPIP':brpsServiceProtocolTCPIP,'brpsServiceProtocolNetware':brpsServiceProtocolNetware,'brpsServiceProtocolAppleTalk':brpsServiceProtocolAppleTalk,'brpsServiceProtocolBanyan':brpsServiceProtocolBanyan,'brpsServiceProtocolDLC':brpsServiceProtocolDLC,'brpsServiceProtocolNetBEUI':brpsServiceProtocolNetBEUI,'brpsServiceNetwareServerMode':brpsServiceNetwareServerMode,'brpsServiceNetwareRemotePrinterNum':brpsServiceNetwareRemotePrinterNum,'brpsServiceProtocolIPP':brpsServiceProtocolIPP,'brpsServiceAppleTalkType':brpsServiceAppleTalkType,'brpsServiceStringLimit':brpsServiceStringLimit,'brpsServiceStringInfoTable':brpsServiceStringInfoTable,'brpsServiceStringInfoEntry':brpsServiceStringInfoEntry,_B5:brpsServiceStringIndex,'brpsServiceString':brpsServiceString,'brpsServiceStringCount':brpsServiceStringCount,'brpsServiceFilterCount':brpsServiceFilterCount,'brprotocol':brprotocol,'brlat':brlat,'brpsLATSupported':brpsLATSupported,'brpsLATEnable':brpsLATEnable,'brpsLATCircuitTimer':brpsLATCircuitTimer,'brpsLATKeepAliveTimer':brpsLATKeepAliveTimer,'brpsLATReceiveBufferMax':brpsLATReceiveBufferMax,'brpsLATTransmitBufferMax':brpsLATTransmitBufferMax,'brpsLATTimeout':brpsLATTimeout,'brpsLATGroup':brpsLATGroup,'brtcpip':brtcpip,'brpsTCPIPSupported':brpsTCPIPSupported,'brpsTCPIPEnable':brpsTCPIPEnable,'brpsTCPIPAddress':brpsTCPIPAddress,'brpsTCPIPSubnetMask':brpsTCPIPSubnetMask,'brpsTCPIPGateway':brpsTCPIPGateway,'brpsTCPIPMethod':brpsTCPIPMethod,'brpsTCPIPTimeout':brpsTCPIPTimeout,'brpsTCPIPBootTries':brpsTCPIPBootTries,'brpsTCPIPMaxWindow':brpsTCPIPMaxWindow,'brpsTCPIPRARPNoSubnet':brpsTCPIPRARPNoSubnet,'brpsTCPIPRARPNoGateway':brpsTCPIPRARPNoGateway,'brpsTCPIPUpdate':brpsTCPIPUpdate,'brpsTCPIPBanner':brpsTCPIPBanner,'brpsTCPIPFastTimeoutEnable':brpsTCPIPFastTimeoutEnable,'brpsTCPIPLPRRetryEnable':brpsTCPIPLPRRetryEnable,'brpsTCPIPUseMethod':brpsTCPIPUseMethod,'brpsTCPIPMethodServer':brpsTCPIPMethodServer,'brpsTCPIPAccessTable':brpsTCPIPAccessTable,'brpsTCPIPAccessEntry':brpsTCPIPAccessEntry,_B6:brpsTCPIPAccessIndex,'brpsTCPIPAccessNodeAddress':brpsTCPIPAccessNodeAddress,'brpsTCPIPAccessSubnetMask':brpsTCPIPAccessSubnetMask,'brpsAdvancedTCPIPAccessSupported':brpsAdvancedTCPIPAccessSupported,'brpsAdvancedTCPIPAccessEnable':brpsAdvancedTCPIPAccessEnable,'brpsAdvancedTCPIPAccessAdministratorIPAddress':brpsAdvancedTCPIPAccessAdministratorIPAddress,'brpsAdvancedTCPIPAccessSetting':brpsAdvancedTCPIPAccessSetting,'brnetware':brnetware,'brpsNetwareSupported':brpsNetwareSupported,'brpsNetwareEnable':brpsNetwareEnable,'brpsNetwareFrameType':brpsNetwareFrameType,'brpsNetwarePollFreq':brpsNetwarePollFreq,'brpsNetwareAdvFreq':brpsNetwareAdvFreq,'brpsNetwarePassword':brpsNetwarePassword,'brpsNetwareRestart':brpsNetwareRestart,'brpsNetwareServerTable':brpsNetwareServerTable,'brpsNetwareServerEntry':brpsNetwareServerEntry,_B7:brpsNetwareServerIndex,'brpsNetwareServerName':brpsNetwareServerName,'brpsNetwarePasswordSet':brpsNetwarePasswordSet,'brpsNDSSupported':brpsNDSSupported,'brpsNetwareEtherIINetInfo':brpsNetwareEtherIINetInfo,'brpsNetwareEtherIICount':brpsNetwareEtherIICount,'brpsNetware8022NetInfo':brpsNetware8022NetInfo,'brpsNetware8022Count':brpsNetware8022Count,'brpsNetware8023NetInfo':brpsNetware8023NetInfo,'brpsNetware8023Count':brpsNetware8023Count,'brpsNetwareSNAPNetInfo':brpsNetwareSNAPNetInfo,'brpsNetwareSNAPCount':brpsNetwareSNAPCount,'brpsNetwareServicingServerName':brpsNetwareServicingServerName,'brpsNetwareServicingQueueName':brpsNetwareServicingQueueName,'brpsNetwareServicingServerCount':brpsNetwareServicingServerCount,'brpsNetwareServicingQueueCount':brpsNetwareServicingQueueCount,'brpsNetwarePrintJob':brpsNetwarePrintJob,'brappletalk':brappletalk,'brpsAppleTalkSupported':brpsAppleTalkSupported,'brpsAppleTalkEnable':brpsAppleTalkEnable,'brpsAppleTalkZone':brpsAppleTalkZone,'brpsAppleTalkPrintJob':brpsAppleTalkPrintJob,'brpsAppleTalkReadByte':brpsAppleTalkReadByte,'brpsAppleTalkWriteByte':brpsAppleTalkWriteByte,'brpsAppleTalkReadError':brpsAppleTalkReadError,'brpsAppleTalkWriteError':brpsAppleTalkWriteError,'brbanyan':brbanyan,'brpsBanyanSupported':brpsBanyanSupported,'brpsBanyanEnable':brpsBanyanEnable,'brpsBanyanLoginName':brpsBanyanLoginName,'brpsBanyanPassword':brpsBanyanPassword,'brpsBanyanHopCount':brpsBanyanHopCount,'brpsBanyanTimeout':brpsBanyanTimeout,'brpsBanyanPasswordSet':brpsBanyanPasswordSet,'brpsBanyanIPNetworkID1':brpsBanyanIPNetworkID1,'brpsBanyanIPNetworkID2':brpsBanyanIPNetworkID2,'brpsBanyanRouter1':brpsBanyanRouter1,'brpsBanyanRouter2':brpsBanyanRouter2,'brpsBanyanIPPacket':brpsBanyanIPPacket,'brpsBanyanErrorCS':brpsBanyanErrorCS,'brpsBanyanErrorPT':brpsBanyanErrorPT,'brpsBanyanErrorLE':brpsBanyanErrorLE,'brpsBanyanPrintServerStatus':brpsBanyanPrintServerStatus,'brpsBanyanServerAddress1':brpsBanyanServerAddress1,'brpsBanyanServerAddress2':brpsBanyanServerAddress2,'brpsBanyanIPCConnectionInformation':brpsBanyanIPCConnectionInformation,'brpsBanyanIPCSequenceError':brpsBanyanIPCSequenceError,'brpsBanyanIPCListen':brpsBanyanIPCListen,'brpsBanyanSPPConnectionInformation':brpsBanyanSPPConnectionInformation,'brpsBanyanSPPSequenceError':brpsBanyanSPPSequenceError,'brpsBanyanSPPListen':brpsBanyanSPPListen,'bremail':bremail,'brpsEmailSupported':brpsEmailSupported,'brpsEmailEnable':brpsEmailEnable,'brpsPOP3Address':brpsPOP3Address,'brpsSMTPAddress':brpsSMTPAddress,'brpsPOP3Name':brpsPOP3Name,'brpsPOP3Password':brpsPOP3Password,'brpsPOP3PollFreq':brpsPOP3PollFreq,'brpsPOP3Timeout':brpsPOP3Timeout,'brpsPOP3PasswordSet':brpsPOP3PasswordSet,'brpsPOP3TotalMessage':brpsPOP3TotalMessage,'brpsPOP3TotalConnect':brpsPOP3TotalConnect,'brpsPOP3TotalConnectFailure':brpsPOP3TotalConnectFailure,'brpsPOP3TotalConnectionLost':brpsPOP3TotalConnectionLost,'brpsPOP3TotalUserFailure':brpsPOP3TotalUserFailure,'brpsPOP3TotalPasswordFailure':brpsPOP3TotalPasswordFailure,'brpsPOP3TotalIOError':brpsPOP3TotalIOError,'brpsSMTPTotalMessage':brpsSMTPTotalMessage,'brpsSMTPTotalConnect':brpsSMTPTotalConnect,'brpsSMTPTotalConnectFailure':brpsSMTPTotalConnectFailure,'brpsSMTPTotalRecvFromFailure':brpsSMTPTotalRecvFromFailure,'brpsSMTPTotalSendToFailure':brpsSMTPTotalSendToFailure,'brpsPOP3Supported':brpsPOP3Supported,'brpsSMTPServerAuthMethod':brpsSMTPServerAuthMethod,'brpsSMTPAUTHUsername':brpsSMTPAUTHUsername,'brpsSMTPAUTHPassword':brpsSMTPAUTHPassword,'brpsSMTPAUTHPasswordSet':brpsSMTPAUTHPasswordSet,'brpsSmtpAUTHTimeout':brpsSmtpAUTHTimeout,'brpsPOPbeforeSMTPWait':brpsPOPbeforeSMTPWait,'brpsAPOPEnable':brpsAPOPEnable,'brpsSMTPEnhancedAuthSupported':brpsSMTPEnhancedAuthSupported,'brpsAPOPSupported':brpsAPOPSupported,'brpsEmailSendTestSupported':brpsEmailSendTestSupported,'brpsEmailRecvTestSupported':brpsEmailRecvTestSupported,'brpsChangeSMTPPortSupported':brpsChangeSMTPPortSupported,'brpsSMTPPortNumber':brpsSMTPPortNumber,'brpsChangePOP3PortSupported':brpsChangePOP3PortSupported,'brpsPOP3PortNumber':brpsPOP3PortNumber,'brpsTmpSMTPServerName':brpsTmpSMTPServerName,'brpsTmpSMTPServerAuthMethod':brpsTmpSMTPServerAuthMethod,'brpsTmpSMTPAUTHUsername':brpsTmpSMTPAUTHUsername,'brpsTmpSMTPAUTHPassword':brpsTmpSMTPAUTHPassword,'brpsTmpPOP3ServerName':brpsTmpPOP3ServerName,'brpsTmpPOP3Name':brpsTmpPOP3Name,'brpsTmpPOP3Password':brpsTmpPOP3Password,'brpsTmpPrintersEmailaddress':brpsTmpPrintersEmailaddress,'brpsTmpAPOPEnable':brpsTmpAPOPEnable,'brpsTmpSMTPAUTHPasswordModified':brpsTmpSMTPAUTHPasswordModified,'brpsTmpPOP3PasswordModified':brpsTmpPOP3PasswordModified,'brpsTmpSMTPPortNumber':brpsTmpSMTPPortNumber,'brpsTmpPOP3PortNumber':brpsTmpPOP3PortNumber,'brpsEmailSendTestMail':brpsEmailSendTestMail,'brpsEmailTestDestinationAddress':brpsEmailTestDestinationAddress,'brpsEmailSendTestCall':brpsEmailSendTestCall,'brpsEmailRecvTestCall':brpsEmailRecvTestCall,'brpsEmailSendRecvTestCall':brpsEmailSendRecvTestCall,'brpsEmailTestResult':brpsEmailTestResult,'brpsPOP3TotalAPOPFailure':brpsPOP3TotalAPOPFailure,'brdlc':brdlc,'brpsDLCSupported':brpsDLCSupported,'brpsDLCEnable':brpsDLCEnable,'brpsDLCPrintStatus':brpsDLCPrintStatus,'brpsDLCLLCState':brpsDLCLLCState,'brpsDLCLLCConnectHost':brpsDLCLLCConnectHost,'brpsDLCLLCLastIFrame':brpsDLCLLCLastIFrame,'brpsDLCLLCRecvPacket':brpsDLCLLCRecvPacket,'brpsDLCLLCPortStatus':brpsDLCLLCPortStatus,'brnetbeui':brnetbeui,'brpsNetBEUISupported':brpsNetBEUISupported,'brpsNetBEUIEnable':brpsNetBEUIEnable,'brpsNetBEUIDomain':brpsNetBEUIDomain,'brpsNetBIOSIPSupported':brpsNetBIOSIPSupported,'brpsNetBIOSIPEnable':brpsNetBIOSIPEnable,'brpsNetBIOSIPMethod':brpsNetBIOSIPMethod,'brpsNetBIOSPrimaryWINSAddr':brpsNetBIOSPrimaryWINSAddr,'brpsNetBIOSSecondaryWINSAddr':brpsNetBIOSSecondaryWINSAddr,'brpsNetBIOSPrintingSupported':brpsNetBIOSPrintingSupported,'bripp':bripp,'brpsIPPSupported':brpsIPPSupported,'brpsIPPEnable':brpsIPPEnable,'brIPPRegularPortEnable':brIPPRegularPortEnable,'brIPPSSLPortEnable':brIPPSSLPortEnable,'brIPPOriginalPortEnable':brIPPOriginalPortEnable,'brntsend':brntsend,'brpsNtSendSupported':brpsNtSendSupported,'brpsNtSendEnable':brpsNtSendEnable,'brfirmware':brfirmware,'brpsFirmwareIPAddress':brpsFirmwareIPAddress,'brpsFirmwareHost':brpsFirmwareHost,'brpsFirmwareFile':brpsFirmwareFile,'brpsFirmwareReload':brpsFirmwareReload,'brpsFirmwareDescription':brpsFirmwareDescription,'brpsFirmwareXModem':brpsFirmwareXModem,'brpsFirmwareAdvancedAddressSupported':brpsFirmwareAdvancedAddressSupported,'brpsFirmwareAdvancedAddress':brpsFirmwareAdvancedAddress,'brnetConfigOpt':brnetConfigOpt,'broriginalprotocol':broriginalprotocol,'broriginaltcpip':broriginaltcpip,'brLPDType':brLPDType,'broriginalftp':broriginalftp,'brFTPSupported':brFTPSupported,'brFTPEnable':brFTPEnable,'broriginalupnp':broriginalupnp,'brUPnPSupported':brUPnPSupported,'brUPnPEnable':brUPnPEnable,'broriginalapipa':broriginalapipa,'brAPIPASupported':brAPIPASupported,'brAPIPAEnable':brAPIPAEnable,'broriginalmdns':broriginalmdns,'brmDNSSupported':brmDNSSupported,'brmDNSEnable':brmDNSEnable,'brmDNSPrinterName':brmDNSPrinterName,'broriginalLAA':broriginalLAA,'brLAASupported':brLAASupported,'brLAAMacAddress':brLAAMacAddress,'broriginalIPv6':broriginalIPv6,'brIPv6Supported':brIPv6Supported,'brIPv6Enable':brIPv6Enable,'brIPv6Priority':brIPv6Priority,'broriginaltelnet':broriginaltelnet,'brtelnetSupported':brtelnetSupported,'brtelnetEnable':brtelnetEnable,'broriginalEWS':broriginalEWS,'brEWSSupported':brEWSSupported,'brEWSEnable':brEWSEnable,'brEWSRegularPortEnable':brEWSRegularPortEnable,'brEWSSSLPortEnable':brEWSSSLPortEnable,'broriginalSNMP':broriginalSNMP,'brSNMPSupported':brSNMPSupported,'brSNMPEnable':brSNMPEnable,'brSNMPV3Supported':brSNMPV3Supported,'brSNMPCommMode':brSNMPCommMode,'brSNMPV3UserName':brSNMPV3UserName,'brSNMPV3KeyType':brSNMPV3KeyType,'brSNMPV3AuthKey':brSNMPV3AuthKey,'brSNMPV3AuthPassword':brSNMPV3AuthPassword,'brSNMPV3PrivKey':brSNMPV3PrivKey,'brSNMPV3PrivPassword':brSNMPV3PrivPassword,'brSNMPV3ContextName':brSNMPV3ContextName,'broriginalldap':broriginalldap,'brLdapSupported':brLdapSupported,'brLdapEnable':brLdapEnable,'brLdapTimeout':brLdapTimeout,'brLdapTimeoutSupported':brLdapTimeoutSupported,'brLdapServerCount':brLdapServerCount,'brLdapServerInfoTable':brLdapServerInfoTable,'brLdapServerInfoEntry':brLdapServerInfoEntry,_AM:brLdapServerInfoIndex,'brLdapServerName':brLdapServerName,'brLdapServerPort':brLdapServerPort,'brLdapServerAuth':brLdapServerAuth,'brLdapServerUserDN':brLdapServerUserDN,'brLdapServerPassword':brLdapServerPassword,'brLdapServerPasswordSet':brLdapServerPasswordSet,'brLdapServerBaseDN':brLdapServerBaseDN,'brLdapServerAttrEMail':brLdapServerAttrEMail,'brLdapServerAttrFAXNumber':brLdapServerAttrFAXNumber,'brLdapServerAttrDetail1':brLdapServerAttrDetail1,'brLdapServerAttrDetail2':brLdapServerAttrDetail2,'brLdapServerAttrDetail3':brLdapServerAttrDetail3,'brLdapServerAttrDetail4':brLdapServerAttrDetail4,'brLdapServerAttrDetailEnable1':brLdapServerAttrDetailEnable1,'brLdapServerAttrDetailEnable2':brLdapServerAttrDetailEnable2,'brLdapServerAttrDetailEnable3':brLdapServerAttrDetailEnable3,'brLdapServerAttrDetailEnable4':brLdapServerAttrDetailEnable4,'brLdapKerberosServerName':brLdapKerberosServerName,'brLdapKerberosServerPort':brLdapKerberosServerPort,'brLdapServerAttrNameCount':brLdapServerAttrNameCount,'brLdapServerAttrNameTable':brLdapServerAttrNameTable,'brLdapServerAttrNameEntry':brLdapServerAttrNameEntry,_B8:brLdapServerAttrNameIndex,'brLdapServerAttrName':brLdapServerAttrName,'brLdapSetDefault':brLdapSetDefault,'broriginalTFTP':broriginalTFTP,'brTFTPSupported':brTFTPSupported,'brTFTPEnable':brTFTPEnable,'broriginalHTTPS':broriginalHTTPS,'brHTTPSSupported':brHTTPSSupported,'brHTTPSEnable':brHTTPSEnable,'broriginalLPD':broriginalLPD,'brLPDSupported':brLPDSupported,'brLPDEnable':brLPDEnable,'broriginalRawPort':broriginalRawPort,'brRawPortSupported':brRawPortSupported,'brRawPortEnable':brRawPortEnable,'broriginalLLTD':broriginalLLTD,'brLLTDSupported':brLLTDSupported,'brLLTDEnable':brLLTDEnable,'broriginalWebServices':broriginalWebServices,'brWebServicesSupported':brWebServicesSupported,'brWebServicesEnable':brWebServicesEnable,'brWebServicesRegularPortEnable':brWebServicesRegularPortEnable,'brWebServicesSSLPortEnable':brWebServicesSSLPortEnable,'broriginalLLMNR':broriginalLLMNR,'brLLMNREnable':brLLMNREnable,'broriginalKerberos':broriginalKerberos,'brKerberosSupported':brKerberosSupported,'broriginalCIFS':broriginalCIFS,'brCIFSSupported':brCIFSSupported,'brCIFSEnable':brCIFSEnable,'broriginalSNTP':broriginalSNTP,'brSNTPCSupported':brSNTPCSupported,'brSNTPCEnable':brSNTPCEnable,'brSNTPCServerMethod':brSNTPCServerMethod,'brSNTPCSyncMethod':brSNTPCSyncMethod,'brSNTPCIntervalMin':brSNTPCIntervalMin,'brSNTPCInterval':brSNTPCInterval,'brSNTPCSyncResult':brSNTPCSyncResult,'brSNTPCPrimaryServerName':brSNTPCPrimaryServerName,'brSNTPCPrimaryServerPort':brSNTPCPrimaryServerPort,'brSNTPCSecondaryServerName':brSNTPCSecondaryServerName,'brSNTPCSecondaryServerPort':brSNTPCSecondaryServerPort,'broriginalSecurity':broriginalSecurity,'brSecurityGeneralStatus':brSecurityGeneralStatus,'brDeviceNegotiationEncryptVer':brDeviceNegotiationEncryptVer,'brpsServerCertificateNum':brpsServerCertificateNum,'brSecurityGeneralSetup':brSecurityGeneralSetup,'brSecurityDeviceNegotiation':brSecurityDeviceNegotiation,'brDeviceNegotiationGetChallenge':brDeviceNegotiationGetChallenge,'brDeviceNegotiationConfirmPassword':brDeviceNegotiationConfirmPassword,'brDeviceNegotiationChangePassword':brDeviceNegotiationChangePassword,'broriginalinternetsetting':broriginalinternetsetting,'broriginalproxy':broriginalproxy,'brProxySupported':brProxySupported,'brProxyEnable':brProxyEnable,'brProxyBypassServer':brProxyBypassServer,'brProxyServerCount':brProxyServerCount,'brProxyServerInfoTable':brProxyServerInfoTable,'brProxyServerInfoEntry':brProxyServerInfoEntry,_B9:brProxyServerInfoIndex,'brProxyServerType':brProxyServerType,'brProxyServerName':brProxyServerName,'brProxyServerPort':brProxyServerPort,'broriginalOtherSetting':broriginalOtherSetting,'broriginalJobTermination':broriginalJobTermination,'brJobTerminationSupported':brJobTerminationSupported,'brJobTerminationEnable':brJobTerminationEnable,'broriginalSNMPTrap':broriginalSNMPTrap,'brSNMPTrapTable':brSNMPTrapTable,'brSNMPTrapEntry':brSNMPTrapEntry,_BA:brSNMPTrapIndex,'brTCPIPServerAddress':brTCPIPServerAddress,'broriginalLegacy':broriginalLegacy,'brLegacyCompatible':brLegacyCompatible,'npMultiCards':npMultiCards,'npMultiIFSet':npMultiIFSet,'brMultiIFdns':brMultiIFdns,'brMultiIFDNSTable':brMultiIFDNSTable,'brMultiIFDNSEntry':brMultiIFDNSEntry,'brMultiIFTCPIPDNSIPSetup':brMultiIFTCPIPDNSIPSetup,'brMultiIFPrimaryDNSIPAddress':brMultiIFPrimaryDNSIPAddress,'brMultiIFSecondaryDNSIPAddress':brMultiIFSecondaryDNSIPAddress,'brMultiIFTCPIPConnectTime':brMultiIFTCPIPConnectTime,'brnetMultiIFConfig':brnetMultiIFConfig,'brMultiIFconfig':brMultiIFconfig,'brMultiIFSupported':brMultiIFSupported,'brMultiIFActiveIF':brMultiIFActiveIF,'brMultiIFAllSetDefault':brMultiIFAllSetDefault,'brMultiIFCount':brMultiIFCount,'brMultiIFConfigureTable':brMultiIFConfigureTable,'brMultiIFConfigureEntry':brMultiIFConfigureEntry,_J:brMultiIFConfigureIndex,'brMultiIFType':brMultiIFType,'brMultiIFDescription':brMultiIFDescription,'brMultiIFNodeName':brMultiIFNodeName,'brMultiIFInterfaceEnable':brMultiIFInterfaceEnable,'brMultiIFEnetMode':brMultiIFEnetMode,'brMultiIFHardwareType':brMultiIFHardwareType,'brMultiIFNodeType':brMultiIFNodeType,'brMultiIFInterfaceEnableImmediate':brMultiIFInterfaceEnableImmediate,'brMultiIFPrimaryInterface':brMultiIFPrimaryInterface,'brMultiIFInterfaceInformation':brMultiIFInterfaceInformation,'brMultiIFcontrol':brMultiIFcontrol,'brMultiIFControlTable':brMultiIFControlTable,'brMultiIFControlEntry':brMultiIFControlEntry,'brMultiIFSetDefault':brMultiIFSetDefault,'brMultiIFservice':brMultiIFservice,'brMultiIFServiceTable':brMultiIFServiceTable,'brMultiIFServiceEntry':brMultiIFServiceEntry,'brMultiIFServiceCount':brMultiIFServiceCount,'brMultiIFServiceStringLimit':brMultiIFServiceStringLimit,'brMultiIFServiceStringCount':brMultiIFServiceStringCount,'brMultiIFServiceFilterCount':brMultiIFServiceFilterCount,'brMultiIFServiceInfoTable':brMultiIFServiceInfoTable,'brMultiIFServiceInfoEntry':brMultiIFServiceInfoEntry,_BC:brMultiIFServiceIndex,'brMultiIFServiceName':brMultiIFServiceName,'brMultiIFServicePort':brMultiIFServicePort,'brMultiIFServiceFilter':brMultiIFServiceFilter,'brMultiIFServiceBOT':brMultiIFServiceBOT,'brMultiIFServiceEOT':brMultiIFServiceEOT,'brMultiIFServiceMatch':brMultiIFServiceMatch,'brMultiIFServiceReplace':brMultiIFServiceReplace,'brMultiIFServiceTCPPort':brMultiIFServiceTCPPort,'brMultiIFServiceNDSTree':brMultiIFServiceNDSTree,'brMultiIFServiceNDSContext':brMultiIFServiceNDSContext,'brMultiIFServiceVines':brMultiIFServiceVines,'brMultiIFServiceObsolete':brMultiIFServiceObsolete,'brMultiIFServiceNetwareServerCount':brMultiIFServiceNetwareServerCount,'brMultiIFServiceReceiveOnly':brMultiIFServiceReceiveOnly,'brMultiIFServiceTCPQueued':brMultiIFServiceTCPQueued,'brMultiIFServiceProtocolLAT':brMultiIFServiceProtocolLAT,'brMultiIFServiceProtocolTCPIP':brMultiIFServiceProtocolTCPIP,'brMultiIFServiceProtocolNetware':brMultiIFServiceProtocolNetware,'brMultiIFServiceProtocolAppleTalk':brMultiIFServiceProtocolAppleTalk,'brMultiIFServiceProtocolBanyan':brMultiIFServiceProtocolBanyan,'brMultiIFServiceProtocolDLC':brMultiIFServiceProtocolDLC,'brMultiIFServiceProtocolNetBEUI':brMultiIFServiceProtocolNetBEUI,'brMultiIFServiceNetwareServerMode':brMultiIFServiceNetwareServerMode,'brMultiIFServiceNetwareRemotePrinterNum':brMultiIFServiceNetwareRemotePrinterNum,'brMultiIFServiceProtocolIPP':brMultiIFServiceProtocolIPP,'brMultiIFServiceAppleTalkType':brMultiIFServiceAppleTalkType,'brMultiIFServiceStringInfoTable':brMultiIFServiceStringInfoTable,'brMultiIFServiceStringInfoEntry':brMultiIFServiceStringInfoEntry,_BD:brMultiIFServiceStringIndex,'brMultiIFServiceString':brMultiIFServiceString,'brMultiIFprotocol':brMultiIFprotocol,'brMultiIFtcpip':brMultiIFtcpip,'brMultiIFTCPIPTable':brMultiIFTCPIPTable,'brMultiIFTCPIPEntry':brMultiIFTCPIPEntry,'brMultiIFTCPIPAddress':brMultiIFTCPIPAddress,'brMultiIFTCPIPSubnetMask':brMultiIFTCPIPSubnetMask,'brMultiIFTCPIPGateway':brMultiIFTCPIPGateway,'brMultiIFTCPIPMethod':brMultiIFTCPIPMethod,'brMultiIFTCPIPUpdate':brMultiIFTCPIPUpdate,'brMultiIFTCPIPTimeout':brMultiIFTCPIPTimeout,'brMultiIFTCPIPBootTries':brMultiIFTCPIPBootTries,'brMultiIFTCPIPRARPNoSubnet':brMultiIFTCPIPRARPNoSubnet,'brMultiIFTCPIPRARPNoGateway':brMultiIFTCPIPRARPNoGateway,'brMultiIFTCPIPUseMethod':brMultiIFTCPIPUseMethod,'brMultiIFTCPIPMethodServer':brMultiIFTCPIPMethodServer,'brMultiIFnetbeui':brMultiIFnetbeui,'brMultiIFNetBIOSTable':brMultiIFNetBIOSTable,'brMultiIFNetBIOSEntry':brMultiIFNetBIOSEntry,'brMultiIFNetBIOSIPMethod':brMultiIFNetBIOSIPMethod,'brMultiIFTCPIPNetBIOSPrimaryWINSAddr':brMultiIFTCPIPNetBIOSPrimaryWINSAddr,'brMultiIFTCPIPNetBIOSSecondaryWINSAddr':brMultiIFTCPIPNetBIOSSecondaryWINSAddr,'brMultiIFNetBEUIDomain':brMultiIFNetBEUIDomain,'brMultiIForiginalapipa':brMultiIForiginalapipa,'brMultiIFAPIPATable':brMultiIFAPIPATable,'brMultiIFAPIPAEntry':brMultiIFAPIPAEntry,'brMultiIFAPIPASupported':brMultiIFAPIPASupported,'brMultiIFAPIPAEnable':brMultiIFAPIPAEnable,'brMultiIForiginalLAA':brMultiIForiginalLAA,'brMultiIFLAATable':brMultiIFLAATable,'brMultiIFLAAEntry':brMultiIFLAAEntry,'brMultiIFLAASupported':brMultiIFLAASupported,'brMultiIFLAAMacAddress':brMultiIFLAAMacAddress,'brMultiIForiginalIPv6':brMultiIForiginalIPv6,'brMultiIFIPv6AddressCountTable':brMultiIFIPv6AddressCountTable,'brMultiIFIPv6AddressCountEntry':brMultiIFIPv6AddressCountEntry,'brMultiIFIPv6AddressCount':brMultiIFIPv6AddressCount,'brMultiIFIPv6AddressTable':brMultiIFIPv6AddressTable,'brMultiIFIPv6AddressEntry':brMultiIFIPv6AddressEntry,_BE:brMultiIFIPv6AddressIndex,'brMultiIFIPv6Address':brMultiIFIPv6Address,'brMultiIFIPv6UseMethod':brMultiIFIPv6UseMethod,'brMultiIFIPv6MethodServer':brMultiIFIPv6MethodServer,'brMultiIFIPv6StaticAddressCountTable':brMultiIFIPv6StaticAddressCountTable,'brMultiIFIPv6StaticAddressCountEntry':brMultiIFIPv6StaticAddressCountEntry,'brMultiIFIPv6StaticAddressCount':brMultiIFIPv6StaticAddressCount,'brMultiIFIPv6StaticAddressTable':brMultiIFIPv6StaticAddressTable,'brMultiIFIPv6StaticAddressEntry':brMultiIFIPv6StaticAddressEntry,_BF:brMultiIFIPv6StaticAddressIndex,'brMultiIFIPv6StaticAddressEnable':brMultiIFIPv6StaticAddressEnable,'brMultiIFIPv6StaticAddress':brMultiIFIPv6StaticAddress,'brMultiIFIPv6StaticAddressPrefixLength':brMultiIFIPv6StaticAddressPrefixLength,'brMultiIFDNSIPv6AddressTable':brMultiIFDNSIPv6AddressTable,'brMultiIFDNSIPv6AddressEntry':brMultiIFDNSIPv6AddressEntry,'brMultiIFPrimaryDNSIPv6Address':brMultiIFPrimaryDNSIPv6Address,'brMultiIFSecondaryDNSIPv6Address':brMultiIFSecondaryDNSIPv6Address,'brMultiIForiginalWebServices':brMultiIForiginalWebServices,'brMultiIFWebServicesTable':brMultiIFWebServicesTable,'brMultiIFWebServicesEntry':brMultiIFWebServicesEntry,'brMultiIFWebServicesName':brMultiIFWebServicesName,'brMultiIFWebServicesInstanceID':brMultiIFWebServicesInstanceID,'brMultiIFWebServicesMetadataVersion':brMultiIFWebServicesMetadataVersion})