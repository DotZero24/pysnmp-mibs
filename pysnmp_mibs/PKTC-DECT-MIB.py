_Ax='pktcDectGroup'
_Aw='pktcDectPPCapabilitiesProfile'
_Av='pktcDectPPCapabilitiesScrollBehavior'
_Au='pktcDectPPCapabilitiesCharsPerDisplayLine'
_At='pktcDectPPCapabilitiesDisplayLines'
_As='pktcDectPPCapabilitiesStoredDisplayChars'
_Ar='pktcDectPPCapabilitiesSlotType'
_Aq='pktcDectPPCapabilitiesAdaptiveVolumeCtrl'
_Ap='pktcDectPPCapabilitiesAmbientNoiseRejection'
_Ao='pktcDectPPCapabilitiesEcho'
_An='pktcDectPPCapabilitiesTone'
_Am='pktcDectPPCapabilitiesDisplay'
_Al='pktcDectPPRegCtrl'
_Ak='pktcDectPPStatus'
_Aj='pktcDectPPTerminalID'
_Ai='pktcDectPPIPEI'
_Ah='pktcDectStatusRSSI'
_Ag='pktcDectStatusLastActivityFailure'
_Af='pktcDectStatusNumActivitySuccess'
_Ae='pktcDectStatusNumConnectionFailures'
_Ad='pktcDectStatusNumLocateMsgs'
_Ac='pktcDectStatusLastLocate'
_Ab='pktcDectPerformanceLinkErrsQbit'
_Aa='pktcDectPerformanceSlidingCollisions'
_AZ='pktcDectPerformancePayloadErrs'
_AY='pktcDectPerformanceControlFieldErrs'
_AX='pktcDectPerformanceSyncFailures'
_AW='pktcDectPerformanceRTDelay'
_AV='pktcDectPerformanceHandovers'
_AU='pktcDectPerformanceRecordNum'
_AT='pktcDectLineSettingsListIntrusionCall'
_AS='pktcDectLineSettingsListMultipleCalls'
_AR='pktcDectLineSettingsListBlockedNB'
_AQ='pktcDectLineSettingsListFPVolume'
_AP='pktcDectLineSettingsListFPMelody'
_AO='pktcDectLineSettingsListDialingPrefix'
_AN='pktcDectLineSettingsListAttachedHandsets'
_AM='pktcDectLineSettingsListLineName'
_AL='pktcDectLineSettingsListLineId'
_AK='pktcDectInternalNamesListName'
_AJ='pktcDectInternalNamesListNumber'
_AI='pktcDectListAccessDescr'
_AH='pktcDectListAccesslistID'
_AG='pktcDectAnalogAlarmCfgState'
_AF='pktcDectServiceStatusConnectivityDisplay'
_AE='pktcDectServiceStatusDeactivationDisplay'
_AD='pktcDectBargeInEnabled'
_AC='pktcDectDTMFToneDuration'
_AB='pktcDectCodecPrefList'
_AA='pktcDectHDVoiceProfileSIP'
_A9='pktcDectHDVoiceProfileNCS'
_A8='pktcDectHDVoiceProfileBasicService'
_A7='pktcDectFPExtendedCapabilities'
_A6='pktcDectFPGeneralCapabilities'
_A5='pktcDectFPName'
_A4='pktcDectFPEasyPairingActivate'
_A3='pktcDectFPPairingType'
_A2='pktcDectFPZeroEmissionEnabled'
_A1='pktcDectFPLockListCfg'
_A0='pktcDectFPMaxActivePP'
_z='pktcDectFPMaxNumPP'
_y='pktcDectLineSettingsListIndex'
_x='pktcDectInternalNamesListIndex'
_w='pktcDectListAccessIndex'
_v='parallelCall'
_u='unused8'
_t='unused7'
_s='unused5'
_r='unused4'
_q='unused3'
_p='unused27'
_o='unused26'
_n='unused23'
_m='unused19'
_l='unused14'
_k='OctetString'
_j='pktcDectPPId'
_i='unused6'
_h='unused2'
_g='unused1'
_f='unused0'
_e='unused31'
_d='unused30'
_c='unused29'
_b='unused28'
_a='unused25'
_Z='unused24'
_Y='unused22'
_X='unused21'
_W='unused20'
_V='unused18'
_U='unused17'
_T='unused16'
_S='unused15'
_R='unused13'
_Q='unused12'
_P='unused11'
_O='unused10'
_N='unused9'
_M='not-accessible'
_L='TruthValue'
_K='ifIndex'
_J='IF-MIB'
_I='SnmpAdminString'
_H='na'
_G='Bits'
_F='read-write'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='PKTC-DECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_k,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcApplicationMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcApplicationMibs')
ifIndex,=mibBuilder.importSymbols(_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_L)
pktcDectMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,8,4))
if mibBuilder.loadTexts:pktcDectMib.setRevisions(('2009-09-17 00:00','2009-02-26 00:00'))
class PktcSpecVersion(TextualConvention,Unsigned32):status=_A
class PktcDectPPState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unknown',1),('idleUnlocked',2),('activeUnlocked',3),('idleLocked',4),('activeLocked',5),('noFPInRange',6),('waitingEasyPairing',7),('easyPairingFailed',8),('easyPINFailed',9)))
_PktcDectNotifications_ObjectIdentity=ObjectIdentity
pktcDectNotifications=_PktcDectNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,0))
_PktcDectObjects_ObjectIdentity=ObjectIdentity
pktcDectObjects=_PktcDectObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1))
_PktcDectFP_ObjectIdentity=ObjectIdentity
pktcDectFP=_PktcDectFP_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,1))
_PktcDectFPMaxNumPP_Type=Unsigned32
_PktcDectFPMaxNumPP_Object=MibScalar
pktcDectFPMaxNumPP=_PktcDectFPMaxNumPP_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,1),_PktcDectFPMaxNumPP_Type())
pktcDectFPMaxNumPP.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPMaxNumPP.setStatus(_A)
if mibBuilder.loadTexts:pktcDectFPMaxNumPP.setUnits('PPs')
_PktcDectFPMaxActivePP_Type=Unsigned32
_PktcDectFPMaxActivePP_Object=MibScalar
pktcDectFPMaxActivePP=_PktcDectFPMaxActivePP_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,2),_PktcDectFPMaxActivePP_Type())
pktcDectFPMaxActivePP.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectFPMaxActivePP.setStatus(_A)
if mibBuilder.loadTexts:pktcDectFPMaxActivePP.setUnits('PPs')
class _PktcDectFPLockListCfg_Type(Bits):namedValues=NamedValues(*(('listOfSupportedLists',0),('missedCallsList',1),('outgoingCallsLlist',2),('incomingAcceptedCallsList',3),('allCallsList',4),('contactList',5),('internalNamesList',6),('dectSsystemSettingsList',7),('lineSettingsList',8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),(_l,14),(_S,15),(_T,16),(_U,17),(_V,18),(_m,19),(_W,20),(_X,21),(_Y,22),(_n,23),(_Z,24),(_a,25),(_o,26),(_p,27),(_b,28),(_c,29),(_d,30),(_e,31)))
_PktcDectFPLockListCfg_Type.__name__=_G
_PktcDectFPLockListCfg_Object=MibScalar
pktcDectFPLockListCfg=_PktcDectFPLockListCfg_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,3),_PktcDectFPLockListCfg_Type())
pktcDectFPLockListCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPLockListCfg.setStatus(_A)
class _PktcDectFPZeroEmissionEnabled_Type(TruthValue):defaultValue=1
_PktcDectFPZeroEmissionEnabled_Type.__name__=_L
_PktcDectFPZeroEmissionEnabled_Object=MibScalar
pktcDectFPZeroEmissionEnabled=_PktcDectFPZeroEmissionEnabled_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,4),_PktcDectFPZeroEmissionEnabled_Type())
pktcDectFPZeroEmissionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPZeroEmissionEnabled.setStatus(_A)
class _PktcDectFPPairingType_Type(SnmpAdminString):defaultValue=OctetString('0000')
_PktcDectFPPairingType_Type.__name__=_I
_PktcDectFPPairingType_Object=MibScalar
pktcDectFPPairingType=_PktcDectFPPairingType_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,5),_PktcDectFPPairingType_Type())
pktcDectFPPairingType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPPairingType.setStatus(_A)
class _PktcDectFPEasyPairingActivate_Type(TruthValue):defaultValue=1
_PktcDectFPEasyPairingActivate_Type.__name__=_L
_PktcDectFPEasyPairingActivate_Object=MibScalar
pktcDectFPEasyPairingActivate=_PktcDectFPEasyPairingActivate_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,6),_PktcDectFPEasyPairingActivate_Type())
pktcDectFPEasyPairingActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPEasyPairingActivate.setStatus(_A)
_PktcDectFPName_Type=SnmpAdminString
_PktcDectFPName_Object=MibScalar
pktcDectFPName=_PktcDectFPName_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,7),_PktcDectFPName_Type())
pktcDectFPName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPName.setStatus(_A)
class _PktcDectFPGeneralCapabilities_Type(Bits):namedValues=NamedValues(('none',0))
_PktcDectFPGeneralCapabilities_Type.__name__=_G
_PktcDectFPGeneralCapabilities_Object=MibScalar
pktcDectFPGeneralCapabilities=_PktcDectFPGeneralCapabilities_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,8),_PktcDectFPGeneralCapabilities_Type())
pktcDectFPGeneralCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPGeneralCapabilities.setStatus(_A)
class _PktcDectFPExtendedCapabilities_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_q,3),(_r,4),(_s,5),(_i,6),(_t,7),(_u,8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),('listAccess',14),(_S,15),(_T,16),(_U,17),(_V,18),(_v,19),(_W,20),(_X,21),(_Y,22),('zeroEmission',23),(_Z,24),(_a,25),('multipleLines',26),('multipleCalls',27),(_b,28),(_c,29),(_d,30),(_e,31)))
_PktcDectFPExtendedCapabilities_Type.__name__=_G
_PktcDectFPExtendedCapabilities_Object=MibScalar
pktcDectFPExtendedCapabilities=_PktcDectFPExtendedCapabilities_Object((1,3,6,1,4,1,4491,2,2,8,4,1,1,9),_PktcDectFPExtendedCapabilities_Type())
pktcDectFPExtendedCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectFPExtendedCapabilities.setStatus(_A)
_PktcDectHDVoiceProfile_ObjectIdentity=ObjectIdentity
pktcDectHDVoiceProfile=_PktcDectHDVoiceProfile_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,2))
_PktcDectHDVoiceProfileBasicService_Type=PktcSpecVersion
_PktcDectHDVoiceProfileBasicService_Object=MibScalar
pktcDectHDVoiceProfileBasicService=_PktcDectHDVoiceProfileBasicService_Object((1,3,6,1,4,1,4491,2,2,8,4,1,2,1),_PktcDectHDVoiceProfileBasicService_Type())
pktcDectHDVoiceProfileBasicService.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectHDVoiceProfileBasicService.setStatus(_A)
_PktcDectHDVoiceProfileNCS_Type=PktcSpecVersion
_PktcDectHDVoiceProfileNCS_Object=MibScalar
pktcDectHDVoiceProfileNCS=_PktcDectHDVoiceProfileNCS_Object((1,3,6,1,4,1,4491,2,2,8,4,1,2,2),_PktcDectHDVoiceProfileNCS_Type())
pktcDectHDVoiceProfileNCS.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectHDVoiceProfileNCS.setStatus(_A)
_PktcDectHDVoiceProfileSIP_Type=PktcSpecVersion
_PktcDectHDVoiceProfileSIP_Object=MibScalar
pktcDectHDVoiceProfileSIP=_PktcDectHDVoiceProfileSIP_Object((1,3,6,1,4,1,4491,2,2,8,4,1,2,3),_PktcDectHDVoiceProfileSIP_Type())
pktcDectHDVoiceProfileSIP.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectHDVoiceProfileSIP.setStatus(_A)
_PktcDectCodec_ObjectIdentity=ObjectIdentity
pktcDectCodec=_PktcDectCodec_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,3))
class _PktcDectCodecPrefList_Type(SnmpAdminString):defaultValue=OctetString('G722,PCMU,PCMA')
_PktcDectCodecPrefList_Type.__name__=_I
_PktcDectCodecPrefList_Object=MibScalar
pktcDectCodecPrefList=_PktcDectCodecPrefList_Object((1,3,6,1,4,1,4491,2,2,8,4,1,3,1),_PktcDectCodecPrefList_Type())
pktcDectCodecPrefList.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectCodecPrefList.setStatus(_A)
_PktcDectDTMF_ObjectIdentity=ObjectIdentity
pktcDectDTMF=_PktcDectDTMF_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,4))
class _PktcDectDTMFToneDuration_Type(Unsigned32):defaultValue=100
_PktcDectDTMFToneDuration_Type.__name__=_D
_PktcDectDTMFToneDuration_Object=MibScalar
pktcDectDTMFToneDuration=_PktcDectDTMFToneDuration_Object((1,3,6,1,4,1,4491,2,2,8,4,1,4,1),_PktcDectDTMFToneDuration_Type())
pktcDectDTMFToneDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectDTMFToneDuration.setStatus(_A)
if mibBuilder.loadTexts:pktcDectDTMFToneDuration.setUnits('milliseconds')
_PktcDectBargeIn_ObjectIdentity=ObjectIdentity
pktcDectBargeIn=_PktcDectBargeIn_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,5))
class _PktcDectBargeInEnabled_Type(TruthValue):defaultValue=1
_PktcDectBargeInEnabled_Type.__name__=_L
_PktcDectBargeInEnabled_Object=MibScalar
pktcDectBargeInEnabled=_PktcDectBargeInEnabled_Object((1,3,6,1,4,1,4491,2,2,8,4,1,5,1),_PktcDectBargeInEnabled_Type())
pktcDectBargeInEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectBargeInEnabled.setStatus(_A)
_PktcDectServiceStatus_ObjectIdentity=ObjectIdentity
pktcDectServiceStatus=_PktcDectServiceStatus_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,1,6))
class _PktcDectServiceStatusDeactivationDisplay_Type(SnmpAdminString):defaultValue=OctetString('Service Deactivated')
_PktcDectServiceStatusDeactivationDisplay_Type.__name__=_I
_PktcDectServiceStatusDeactivationDisplay_Object=MibScalar
pktcDectServiceStatusDeactivationDisplay=_PktcDectServiceStatusDeactivationDisplay_Object((1,3,6,1,4,1,4491,2,2,8,4,1,6,1),_PktcDectServiceStatusDeactivationDisplay_Type())
pktcDectServiceStatusDeactivationDisplay.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectServiceStatusDeactivationDisplay.setStatus(_A)
class _PktcDectServiceStatusConnectivityDisplay_Type(SnmpAdminString):defaultValue=OctetString('Network Unavailable')
_PktcDectServiceStatusConnectivityDisplay_Type.__name__=_I
_PktcDectServiceStatusConnectivityDisplay_Object=MibScalar
pktcDectServiceStatusConnectivityDisplay=_PktcDectServiceStatusConnectivityDisplay_Object((1,3,6,1,4,1,4491,2,2,8,4,1,6,2),_PktcDectServiceStatusConnectivityDisplay_Type())
pktcDectServiceStatusConnectivityDisplay.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectServiceStatusConnectivityDisplay.setStatus(_A)
_PktcDectAnalogAlarmCfgTable_Object=MibTable
pktcDectAnalogAlarmCfgTable=_PktcDectAnalogAlarmCfgTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,7))
if mibBuilder.loadTexts:pktcDectAnalogAlarmCfgTable.setStatus(_A)
_PktcDectAnalogAlarmCfgEntry_Object=MibTableRow
pktcDectAnalogAlarmCfgEntry=_PktcDectAnalogAlarmCfgEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,7,1))
pktcDectAnalogAlarmCfgEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:pktcDectAnalogAlarmCfgEntry.setStatus(_A)
class _PktcDectAnalogAlarmCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('preemptive',2),('simultanousCalls',3)))
_PktcDectAnalogAlarmCfgState_Type.__name__=_E
_PktcDectAnalogAlarmCfgState_Object=MibTableColumn
pktcDectAnalogAlarmCfgState=_PktcDectAnalogAlarmCfgState_Object((1,3,6,1,4,1,4491,2,2,8,4,1,7,1,1),_PktcDectAnalogAlarmCfgState_Type())
pktcDectAnalogAlarmCfgState.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectAnalogAlarmCfgState.setStatus(_A)
_PktcDectPPTable_Object=MibTable
pktcDectPPTable=_PktcDectPPTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8))
if mibBuilder.loadTexts:pktcDectPPTable.setStatus(_A)
_PktcDectPPEntry_Object=MibTableRow
pktcDectPPEntry=_PktcDectPPEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1))
pktcDectPPEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:pktcDectPPEntry.setStatus(_A)
class _PktcDectPPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PktcDectPPId_Type.__name__=_D
_PktcDectPPId_Object=MibTableColumn
pktcDectPPId=_PktcDectPPId_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1,1),_PktcDectPPId_Type())
pktcDectPPId.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcDectPPId.setStatus(_A)
class _PktcDectPPIPEI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_PktcDectPPIPEI_Type.__name__=_k
_PktcDectPPIPEI_Object=MibTableColumn
pktcDectPPIPEI=_PktcDectPPIPEI_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1,2),_PktcDectPPIPEI_Type())
pktcDectPPIPEI.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPIPEI.setStatus(_A)
class _PktcDectPPTerminalID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PktcDectPPTerminalID_Type.__name__=_D
_PktcDectPPTerminalID_Object=MibTableColumn
pktcDectPPTerminalID=_PktcDectPPTerminalID_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1,3),_PktcDectPPTerminalID_Type())
pktcDectPPTerminalID.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPTerminalID.setStatus(_A)
_PktcDectPPStatus_Type=PktcDectPPState
_PktcDectPPStatus_Object=MibTableColumn
pktcDectPPStatus=_PktcDectPPStatus_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1,4),_PktcDectPPStatus_Type())
pktcDectPPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPStatus.setStatus(_A)
class _PktcDectPPRegCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('register',1),('deregister',2),('remove',3)))
_PktcDectPPRegCtrl_Type.__name__=_E
_PktcDectPPRegCtrl_Object=MibTableColumn
pktcDectPPRegCtrl=_PktcDectPPRegCtrl_Object((1,3,6,1,4,1,4491,2,2,8,4,1,8,1,5),_PktcDectPPRegCtrl_Type())
pktcDectPPRegCtrl.setMaxAccess(_F)
if mibBuilder.loadTexts:pktcDectPPRegCtrl.setStatus(_A)
_PktcDectPPCapabilitiesTable_Object=MibTable
pktcDectPPCapabilitiesTable=_PktcDectPPCapabilitiesTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9))
if mibBuilder.loadTexts:pktcDectPPCapabilitiesTable.setStatus(_A)
_PktcDectPPCapabilitiesEntry_Object=MibTableRow
pktcDectPPCapabilitiesEntry=_PktcDectPPCapabilitiesEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1))
pktcDectPPCapabilitiesEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:pktcDectPPCapabilitiesEntry.setStatus(_A)
class _PktcDectPPCapabilitiesDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('noDisplay',1),('numeric',2),('numericPlus',3),('alphanumeric',4),('fullDisplay',5)))
_PktcDectPPCapabilitiesDisplay_Type.__name__=_E
_PktcDectPPCapabilitiesDisplay_Object=MibTableColumn
pktcDectPPCapabilitiesDisplay=_PktcDectPPCapabilitiesDisplay_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,1),_PktcDectPPCapabilitiesDisplay_Type())
pktcDectPPCapabilitiesDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesDisplay.setStatus(_A)
class _PktcDectPPCapabilitiesTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('notone',1),('dialTone',2),('e182',3),('dect',4)))
_PktcDectPPCapabilitiesTone_Type.__name__=_E
_PktcDectPPCapabilitiesTone_Object=MibTableColumn
pktcDectPPCapabilitiesTone=_PktcDectPPCapabilitiesTone_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,2),_PktcDectPPCapabilitiesTone_Type())
pktcDectPPCapabilitiesTone.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesTone.setStatus(_A)
class _PktcDectPPCapabilitiesEcho_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('minTCL',1),('fullTCL',2),('voip',3)))
_PktcDectPPCapabilitiesEcho_Type.__name__=_E
_PktcDectPPCapabilitiesEcho_Object=MibTableColumn
pktcDectPPCapabilitiesEcho=_PktcDectPPCapabilitiesEcho_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,3),_PktcDectPPCapabilitiesEcho_Type())
pktcDectPPCapabilitiesEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesEcho.setStatus(_A)
class _PktcDectPPCapabilitiesAmbientNoiseRejection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('noSupport',1),('support',2)))
_PktcDectPPCapabilitiesAmbientNoiseRejection_Type.__name__=_E
_PktcDectPPCapabilitiesAmbientNoiseRejection_Object=MibTableColumn
pktcDectPPCapabilitiesAmbientNoiseRejection=_PktcDectPPCapabilitiesAmbientNoiseRejection_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,4),_PktcDectPPCapabilitiesAmbientNoiseRejection_Type())
pktcDectPPCapabilitiesAmbientNoiseRejection.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesAmbientNoiseRejection.setStatus(_A)
class _PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('noSupported',1),('used',2),('disabled',3)))
_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type.__name__=_E
_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Object=MibTableColumn
pktcDectPPCapabilitiesAdaptiveVolumeCtrl=_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,5),_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type())
pktcDectPPCapabilitiesAdaptiveVolumeCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesAdaptiveVolumeCtrl.setStatus(_A)
class _PktcDectPPCapabilitiesSlotType_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),('doubleSlot',3),('fullSlot',4),(_s,5),(_i,6),('halfSlot',7)))
_PktcDectPPCapabilitiesSlotType_Type.__name__=_G
_PktcDectPPCapabilitiesSlotType_Object=MibTableColumn
pktcDectPPCapabilitiesSlotType=_PktcDectPPCapabilitiesSlotType_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,6),_PktcDectPPCapabilitiesSlotType_Type())
pktcDectPPCapabilitiesSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesSlotType.setStatus(_A)
class _PktcDectPPCapabilitiesStoredDisplayChars_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16363))
_PktcDectPPCapabilitiesStoredDisplayChars_Type.__name__=_D
_PktcDectPPCapabilitiesStoredDisplayChars_Object=MibTableColumn
pktcDectPPCapabilitiesStoredDisplayChars=_PktcDectPPCapabilitiesStoredDisplayChars_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,7),_PktcDectPPCapabilitiesStoredDisplayChars_Type())
pktcDectPPCapabilitiesStoredDisplayChars.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesStoredDisplayChars.setStatus(_A)
class _PktcDectPPCapabilitiesDisplayLines_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PktcDectPPCapabilitiesDisplayLines_Type.__name__=_D
_PktcDectPPCapabilitiesDisplayLines_Object=MibTableColumn
pktcDectPPCapabilitiesDisplayLines=_PktcDectPPCapabilitiesDisplayLines_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,8),_PktcDectPPCapabilitiesDisplayLines_Type())
pktcDectPPCapabilitiesDisplayLines.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesDisplayLines.setStatus(_A)
class _PktcDectPPCapabilitiesCharsPerDisplayLine_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PktcDectPPCapabilitiesCharsPerDisplayLine_Type.__name__=_D
_PktcDectPPCapabilitiesCharsPerDisplayLine_Object=MibTableColumn
pktcDectPPCapabilitiesCharsPerDisplayLine=_PktcDectPPCapabilitiesCharsPerDisplayLine_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,9),_PktcDectPPCapabilitiesCharsPerDisplayLine_Type())
pktcDectPPCapabilitiesCharsPerDisplayLine.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesCharsPerDisplayLine.setStatus(_A)
class _PktcDectPPCapabilitiesScrollBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('type1',1),('type',2)))
_PktcDectPPCapabilitiesScrollBehavior_Type.__name__=_E
_PktcDectPPCapabilitiesScrollBehavior_Object=MibTableColumn
pktcDectPPCapabilitiesScrollBehavior=_PktcDectPPCapabilitiesScrollBehavior_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,10),_PktcDectPPCapabilitiesScrollBehavior_Type())
pktcDectPPCapabilitiesScrollBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesScrollBehavior.setStatus(_A)
class _PktcDectPPCapabilitiesProfile_Type(Bits):namedValues=NamedValues(*((_f,0),(_g,1),(_h,2),(_q,3),(_r,4),('gapSupport',5),(_i,6),(_t,7),(_u,8),(_N,9),(_O,10),(_P,11),(_Q,12),(_R,13),(_l,14),(_S,15),(_T,16),(_U,17),(_V,18),(_m,19),(_W,20),(_X,21),(_Y,22),(_n,23),(_Z,24),(_a,25),(_o,26),(_p,27),(_b,28),(_c,29),(_d,30),(_e,31),('unused32',32),('unused33',33),('unused34',34),('unused35',35),('unused36',36),('unused37',37),('unused38',38),('unused39',39),('unused40',40),('zeroEmissionSupport',41),('unused42',42),('unused43',43),('unused44',44),('unused45',45),('unused46',46),('unused47',47),('unused48',48),('unused49',49),('multipleLlines',50),(_v,51),('callIdentification',52),('wideband',53),('part3',54),('unused55',55),('unused56',56),('unused57',57),('unused58',58),('unused59',59),('unused60',60),('unused61',61),('unused62',62),('unused63',63),('unused64',64)))
_PktcDectPPCapabilitiesProfile_Type.__name__=_G
_PktcDectPPCapabilitiesProfile_Object=MibTableColumn
pktcDectPPCapabilitiesProfile=_PktcDectPPCapabilitiesProfile_Object((1,3,6,1,4,1,4491,2,2,8,4,1,9,1,11),_PktcDectPPCapabilitiesProfile_Type())
pktcDectPPCapabilitiesProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPPCapabilitiesProfile.setStatus(_A)
_PktcDectListAccessTable_Object=MibTable
pktcDectListAccessTable=_PktcDectListAccessTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,10))
if mibBuilder.loadTexts:pktcDectListAccessTable.setStatus(_A)
_PktcDectListAccessEntry_Object=MibTableRow
pktcDectListAccessEntry=_PktcDectListAccessEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,10,1))
pktcDectListAccessEntry.setIndexNames((0,_B,_w))
if mibBuilder.loadTexts:pktcDectListAccessEntry.setStatus(_A)
class _PktcDectListAccessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PktcDectListAccessIndex_Type.__name__=_D
_PktcDectListAccessIndex_Object=MibTableColumn
pktcDectListAccessIndex=_PktcDectListAccessIndex_Object((1,3,6,1,4,1,4491,2,2,8,4,1,10,1,1),_PktcDectListAccessIndex_Type())
pktcDectListAccessIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcDectListAccessIndex.setStatus(_A)
class _PktcDectListAccesslistID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PktcDectListAccesslistID_Type.__name__=_D
_PktcDectListAccesslistID_Object=MibTableColumn
pktcDectListAccesslistID=_PktcDectListAccesslistID_Object((1,3,6,1,4,1,4491,2,2,8,4,1,10,1,2),_PktcDectListAccesslistID_Type())
pktcDectListAccesslistID.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectListAccesslistID.setStatus(_A)
_PktcDectListAccessDescr_Type=SnmpAdminString
_PktcDectListAccessDescr_Object=MibTableColumn
pktcDectListAccessDescr=_PktcDectListAccessDescr_Object((1,3,6,1,4,1,4491,2,2,8,4,1,10,1,3),_PktcDectListAccessDescr_Type())
pktcDectListAccessDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectListAccessDescr.setStatus(_A)
_PktcDectInternalNamesListTable_Object=MibTable
pktcDectInternalNamesListTable=_PktcDectInternalNamesListTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,11))
if mibBuilder.loadTexts:pktcDectInternalNamesListTable.setStatus(_A)
_PktcDectInternalNamesListEntry_Object=MibTableRow
pktcDectInternalNamesListEntry=_PktcDectInternalNamesListEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,11,1))
pktcDectInternalNamesListEntry.setIndexNames((0,_B,_x))
if mibBuilder.loadTexts:pktcDectInternalNamesListEntry.setStatus(_A)
class _PktcDectInternalNamesListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_PktcDectInternalNamesListIndex_Type.__name__=_D
_PktcDectInternalNamesListIndex_Object=MibTableColumn
pktcDectInternalNamesListIndex=_PktcDectInternalNamesListIndex_Object((1,3,6,1,4,1,4491,2,2,8,4,1,11,1,1),_PktcDectInternalNamesListIndex_Type())
pktcDectInternalNamesListIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcDectInternalNamesListIndex.setStatus(_A)
class _PktcDectInternalNamesListNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_PktcDectInternalNamesListNumber_Type.__name__=_D
_PktcDectInternalNamesListNumber_Object=MibTableColumn
pktcDectInternalNamesListNumber=_PktcDectInternalNamesListNumber_Object((1,3,6,1,4,1,4491,2,2,8,4,1,11,1,2),_PktcDectInternalNamesListNumber_Type())
pktcDectInternalNamesListNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectInternalNamesListNumber.setStatus(_A)
_PktcDectInternalNamesListName_Type=SnmpAdminString
_PktcDectInternalNamesListName_Object=MibTableColumn
pktcDectInternalNamesListName=_PktcDectInternalNamesListName_Object((1,3,6,1,4,1,4491,2,2,8,4,1,11,1,3),_PktcDectInternalNamesListName_Type())
pktcDectInternalNamesListName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectInternalNamesListName.setStatus(_A)
_PktcDectLineSettingsListTable_Object=MibTable
pktcDectLineSettingsListTable=_PktcDectLineSettingsListTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12))
if mibBuilder.loadTexts:pktcDectLineSettingsListTable.setStatus(_A)
_PktcDectLineSettingsListEntry_Object=MibTableRow
pktcDectLineSettingsListEntry=_PktcDectLineSettingsListEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1))
pktcDectLineSettingsListEntry.setIndexNames((0,_B,_y))
if mibBuilder.loadTexts:pktcDectLineSettingsListEntry.setStatus(_A)
class _PktcDectLineSettingsListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_PktcDectLineSettingsListIndex_Type.__name__=_D
_PktcDectLineSettingsListIndex_Object=MibTableColumn
pktcDectLineSettingsListIndex=_PktcDectLineSettingsListIndex_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,1),_PktcDectLineSettingsListIndex_Type())
pktcDectLineSettingsListIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcDectLineSettingsListIndex.setStatus(_A)
class _PktcDectLineSettingsListLineId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_PktcDectLineSettingsListLineId_Type.__name__=_D
_PktcDectLineSettingsListLineId_Object=MibTableColumn
pktcDectLineSettingsListLineId=_PktcDectLineSettingsListLineId_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,2),_PktcDectLineSettingsListLineId_Type())
pktcDectLineSettingsListLineId.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListLineId.setStatus(_A)
_PktcDectLineSettingsListLineName_Type=SnmpAdminString
_PktcDectLineSettingsListLineName_Object=MibTableColumn
pktcDectLineSettingsListLineName=_PktcDectLineSettingsListLineName_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,3),_PktcDectLineSettingsListLineName_Type())
pktcDectLineSettingsListLineName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListLineName.setStatus(_A)
_PktcDectLineSettingsListAttachedHandsets_Type=SnmpAdminString
_PktcDectLineSettingsListAttachedHandsets_Object=MibTableColumn
pktcDectLineSettingsListAttachedHandsets=_PktcDectLineSettingsListAttachedHandsets_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,4),_PktcDectLineSettingsListAttachedHandsets_Type())
pktcDectLineSettingsListAttachedHandsets.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListAttachedHandsets.setStatus(_A)
_PktcDectLineSettingsListDialingPrefix_Type=SnmpAdminString
_PktcDectLineSettingsListDialingPrefix_Object=MibTableColumn
pktcDectLineSettingsListDialingPrefix=_PktcDectLineSettingsListDialingPrefix_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,5),_PktcDectLineSettingsListDialingPrefix_Type())
pktcDectLineSettingsListDialingPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListDialingPrefix.setStatus(_A)
class _PktcDectLineSettingsListFPMelody_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PktcDectLineSettingsListFPMelody_Type.__name__=_D
_PktcDectLineSettingsListFPMelody_Object=MibTableColumn
pktcDectLineSettingsListFPMelody=_PktcDectLineSettingsListFPMelody_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,6),_PktcDectLineSettingsListFPMelody_Type())
pktcDectLineSettingsListFPMelody.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListFPMelody.setStatus(_A)
class _PktcDectLineSettingsListFPVolume_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PktcDectLineSettingsListFPVolume_Type.__name__=_D
_PktcDectLineSettingsListFPVolume_Object=MibTableColumn
pktcDectLineSettingsListFPVolume=_PktcDectLineSettingsListFPVolume_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,7),_PktcDectLineSettingsListFPVolume_Type())
pktcDectLineSettingsListFPVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListFPVolume.setStatus(_A)
_PktcDectLineSettingsListBlockedNB_Type=TruthValue
_PktcDectLineSettingsListBlockedNB_Object=MibTableColumn
pktcDectLineSettingsListBlockedNB=_PktcDectLineSettingsListBlockedNB_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,8),_PktcDectLineSettingsListBlockedNB_Type())
pktcDectLineSettingsListBlockedNB.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListBlockedNB.setStatus(_A)
_PktcDectLineSettingsListMultipleCalls_Type=TruthValue
_PktcDectLineSettingsListMultipleCalls_Object=MibTableColumn
pktcDectLineSettingsListMultipleCalls=_PktcDectLineSettingsListMultipleCalls_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,9),_PktcDectLineSettingsListMultipleCalls_Type())
pktcDectLineSettingsListMultipleCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListMultipleCalls.setStatus(_A)
_PktcDectLineSettingsListIntrusionCall_Type=TruthValue
_PktcDectLineSettingsListIntrusionCall_Object=MibTableColumn
pktcDectLineSettingsListIntrusionCall=_PktcDectLineSettingsListIntrusionCall_Object((1,3,6,1,4,1,4491,2,2,8,4,1,12,1,10),_PktcDectLineSettingsListIntrusionCall_Type())
pktcDectLineSettingsListIntrusionCall.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectLineSettingsListIntrusionCall.setStatus(_A)
_PktcDectPerformanceTable_Object=MibTable
pktcDectPerformanceTable=_PktcDectPerformanceTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13))
if mibBuilder.loadTexts:pktcDectPerformanceTable.setStatus(_A)
_PktcDectPerformanceEntry_Object=MibTableRow
pktcDectPerformanceEntry=_PktcDectPerformanceEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1))
pktcDectPerformanceEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:pktcDectPerformanceEntry.setStatus(_A)
_PktcDectPerformanceRecordNum_Type=Unsigned32
_PktcDectPerformanceRecordNum_Object=MibTableColumn
pktcDectPerformanceRecordNum=_PktcDectPerformanceRecordNum_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,1),_PktcDectPerformanceRecordNum_Type())
pktcDectPerformanceRecordNum.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceRecordNum.setStatus(_A)
_PktcDectPerformanceHandovers_Type=Counter32
_PktcDectPerformanceHandovers_Object=MibTableColumn
pktcDectPerformanceHandovers=_PktcDectPerformanceHandovers_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,2),_PktcDectPerformanceHandovers_Type())
pktcDectPerformanceHandovers.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceHandovers.setStatus(_A)
_PktcDectPerformanceRTDelay_Type=Unsigned32
_PktcDectPerformanceRTDelay_Object=MibTableColumn
pktcDectPerformanceRTDelay=_PktcDectPerformanceRTDelay_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,3),_PktcDectPerformanceRTDelay_Type())
pktcDectPerformanceRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceRTDelay.setStatus(_A)
_PktcDectPerformanceSyncFailures_Type=Counter32
_PktcDectPerformanceSyncFailures_Object=MibTableColumn
pktcDectPerformanceSyncFailures=_PktcDectPerformanceSyncFailures_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,4),_PktcDectPerformanceSyncFailures_Type())
pktcDectPerformanceSyncFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceSyncFailures.setStatus(_A)
_PktcDectPerformanceControlFieldErrs_Type=Counter32
_PktcDectPerformanceControlFieldErrs_Object=MibTableColumn
pktcDectPerformanceControlFieldErrs=_PktcDectPerformanceControlFieldErrs_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,5),_PktcDectPerformanceControlFieldErrs_Type())
pktcDectPerformanceControlFieldErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceControlFieldErrs.setStatus(_A)
_PktcDectPerformancePayloadErrs_Type=Counter32
_PktcDectPerformancePayloadErrs_Object=MibTableColumn
pktcDectPerformancePayloadErrs=_PktcDectPerformancePayloadErrs_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,6),_PktcDectPerformancePayloadErrs_Type())
pktcDectPerformancePayloadErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformancePayloadErrs.setStatus(_A)
_PktcDectPerformanceSlidingCollisions_Type=Counter32
_PktcDectPerformanceSlidingCollisions_Object=MibTableColumn
pktcDectPerformanceSlidingCollisions=_PktcDectPerformanceSlidingCollisions_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,7),_PktcDectPerformanceSlidingCollisions_Type())
pktcDectPerformanceSlidingCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceSlidingCollisions.setStatus(_A)
_PktcDectPerformanceLinkErrsQbit_Type=Counter32
_PktcDectPerformanceLinkErrsQbit_Object=MibTableColumn
pktcDectPerformanceLinkErrsQbit=_PktcDectPerformanceLinkErrsQbit_Object((1,3,6,1,4,1,4491,2,2,8,4,1,13,1,8),_PktcDectPerformanceLinkErrsQbit_Type())
pktcDectPerformanceLinkErrsQbit.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectPerformanceLinkErrsQbit.setStatus(_A)
_PktcDectStatusTable_Object=MibTable
pktcDectStatusTable=_PktcDectStatusTable_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14))
if mibBuilder.loadTexts:pktcDectStatusTable.setStatus(_A)
_PktcDectStatusEntry_Object=MibTableRow
pktcDectStatusEntry=_PktcDectStatusEntry_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1))
pktcDectStatusEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:pktcDectStatusEntry.setStatus(_A)
_PktcDectStatusLastLocate_Type=DateAndTime
_PktcDectStatusLastLocate_Object=MibTableColumn
pktcDectStatusLastLocate=_PktcDectStatusLastLocate_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,1),_PktcDectStatusLastLocate_Type())
pktcDectStatusLastLocate.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusLastLocate.setStatus(_A)
_PktcDectStatusNumLocateMsgs_Type=Counter32
_PktcDectStatusNumLocateMsgs_Object=MibTableColumn
pktcDectStatusNumLocateMsgs=_PktcDectStatusNumLocateMsgs_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,2),_PktcDectStatusNumLocateMsgs_Type())
pktcDectStatusNumLocateMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusNumLocateMsgs.setStatus(_A)
_PktcDectStatusNumConnectionFailures_Type=Counter32
_PktcDectStatusNumConnectionFailures_Object=MibTableColumn
pktcDectStatusNumConnectionFailures=_PktcDectStatusNumConnectionFailures_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,3),_PktcDectStatusNumConnectionFailures_Type())
pktcDectStatusNumConnectionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusNumConnectionFailures.setStatus(_A)
_PktcDectStatusNumActivitySuccess_Type=Counter32
_PktcDectStatusNumActivitySuccess_Object=MibTableColumn
pktcDectStatusNumActivitySuccess=_PktcDectStatusNumActivitySuccess_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,4),_PktcDectStatusNumActivitySuccess_Type())
pktcDectStatusNumActivitySuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusNumActivitySuccess.setStatus(_A)
_PktcDectStatusLastActivityFailure_Type=DateAndTime
_PktcDectStatusLastActivityFailure_Object=MibTableColumn
pktcDectStatusLastActivityFailure=_PktcDectStatusLastActivityFailure_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,5),_PktcDectStatusLastActivityFailure_Type())
pktcDectStatusLastActivityFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusLastActivityFailure.setStatus(_A)
_PktcDectStatusRSSI_Type=Unsigned32
_PktcDectStatusRSSI_Object=MibTableColumn
pktcDectStatusRSSI=_PktcDectStatusRSSI_Object((1,3,6,1,4,1,4491,2,2,8,4,1,14,1,6),_PktcDectStatusRSSI_Type())
pktcDectStatusRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcDectStatusRSSI.setStatus(_A)
_PktcDectMibConformance_ObjectIdentity=ObjectIdentity
pktcDectMibConformance=_PktcDectMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,2))
_PktcDectMibCompliances_ObjectIdentity=ObjectIdentity
pktcDectMibCompliances=_PktcDectMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,2,1))
_PktcDectMibGroups_ObjectIdentity=ObjectIdentity
pktcDectMibGroups=_PktcDectMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,4,2,2))
pktcDectGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,8,4,2,2,1))
pktcDectGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:pktcDectGroup.setStatus(_A)
pktcDectCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,8,4,2,1,1))
pktcDectCompliance.setObjects((_B,_Ax))
if mibBuilder.loadTexts:pktcDectCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PktcSpecVersion':PktcSpecVersion,'PktcDectPPState':PktcDectPPState,'pktcDectMib':pktcDectMib,'pktcDectNotifications':pktcDectNotifications,'pktcDectObjects':pktcDectObjects,'pktcDectFP':pktcDectFP,_z:pktcDectFPMaxNumPP,_A0:pktcDectFPMaxActivePP,_A1:pktcDectFPLockListCfg,_A2:pktcDectFPZeroEmissionEnabled,_A3:pktcDectFPPairingType,_A4:pktcDectFPEasyPairingActivate,_A5:pktcDectFPName,_A6:pktcDectFPGeneralCapabilities,_A7:pktcDectFPExtendedCapabilities,'pktcDectHDVoiceProfile':pktcDectHDVoiceProfile,_A8:pktcDectHDVoiceProfileBasicService,_A9:pktcDectHDVoiceProfileNCS,_AA:pktcDectHDVoiceProfileSIP,'pktcDectCodec':pktcDectCodec,_AB:pktcDectCodecPrefList,'pktcDectDTMF':pktcDectDTMF,_AC:pktcDectDTMFToneDuration,'pktcDectBargeIn':pktcDectBargeIn,_AD:pktcDectBargeInEnabled,'pktcDectServiceStatus':pktcDectServiceStatus,_AE:pktcDectServiceStatusDeactivationDisplay,_AF:pktcDectServiceStatusConnectivityDisplay,'pktcDectAnalogAlarmCfgTable':pktcDectAnalogAlarmCfgTable,'pktcDectAnalogAlarmCfgEntry':pktcDectAnalogAlarmCfgEntry,_AG:pktcDectAnalogAlarmCfgState,'pktcDectPPTable':pktcDectPPTable,'pktcDectPPEntry':pktcDectPPEntry,_j:pktcDectPPId,_Ai:pktcDectPPIPEI,_Aj:pktcDectPPTerminalID,_Ak:pktcDectPPStatus,_Al:pktcDectPPRegCtrl,'pktcDectPPCapabilitiesTable':pktcDectPPCapabilitiesTable,'pktcDectPPCapabilitiesEntry':pktcDectPPCapabilitiesEntry,_Am:pktcDectPPCapabilitiesDisplay,_An:pktcDectPPCapabilitiesTone,_Ao:pktcDectPPCapabilitiesEcho,_Ap:pktcDectPPCapabilitiesAmbientNoiseRejection,_Aq:pktcDectPPCapabilitiesAdaptiveVolumeCtrl,_Ar:pktcDectPPCapabilitiesSlotType,_As:pktcDectPPCapabilitiesStoredDisplayChars,_At:pktcDectPPCapabilitiesDisplayLines,_Au:pktcDectPPCapabilitiesCharsPerDisplayLine,_Av:pktcDectPPCapabilitiesScrollBehavior,_Aw:pktcDectPPCapabilitiesProfile,'pktcDectListAccessTable':pktcDectListAccessTable,'pktcDectListAccessEntry':pktcDectListAccessEntry,_w:pktcDectListAccessIndex,_AH:pktcDectListAccesslistID,_AI:pktcDectListAccessDescr,'pktcDectInternalNamesListTable':pktcDectInternalNamesListTable,'pktcDectInternalNamesListEntry':pktcDectInternalNamesListEntry,_x:pktcDectInternalNamesListIndex,_AJ:pktcDectInternalNamesListNumber,_AK:pktcDectInternalNamesListName,'pktcDectLineSettingsListTable':pktcDectLineSettingsListTable,'pktcDectLineSettingsListEntry':pktcDectLineSettingsListEntry,_y:pktcDectLineSettingsListIndex,_AL:pktcDectLineSettingsListLineId,_AM:pktcDectLineSettingsListLineName,_AN:pktcDectLineSettingsListAttachedHandsets,_AO:pktcDectLineSettingsListDialingPrefix,_AP:pktcDectLineSettingsListFPMelody,_AQ:pktcDectLineSettingsListFPVolume,_AR:pktcDectLineSettingsListBlockedNB,_AS:pktcDectLineSettingsListMultipleCalls,_AT:pktcDectLineSettingsListIntrusionCall,'pktcDectPerformanceTable':pktcDectPerformanceTable,'pktcDectPerformanceEntry':pktcDectPerformanceEntry,_AU:pktcDectPerformanceRecordNum,_AV:pktcDectPerformanceHandovers,_AW:pktcDectPerformanceRTDelay,_AX:pktcDectPerformanceSyncFailures,_AY:pktcDectPerformanceControlFieldErrs,_AZ:pktcDectPerformancePayloadErrs,_Aa:pktcDectPerformanceSlidingCollisions,_Ab:pktcDectPerformanceLinkErrsQbit,'pktcDectStatusTable':pktcDectStatusTable,'pktcDectStatusEntry':pktcDectStatusEntry,_Ac:pktcDectStatusLastLocate,_Ad:pktcDectStatusNumLocateMsgs,_Ae:pktcDectStatusNumConnectionFailures,_Af:pktcDectStatusNumActivitySuccess,_Ag:pktcDectStatusLastActivityFailure,_Ah:pktcDectStatusRSSI,'pktcDectMibConformance':pktcDectMibConformance,'pktcDectMibCompliances':pktcDectMibCompliances,'pktcDectCompliance':pktcDectCompliance,'pktcDectMibGroups':pktcDectMibGroups,_Ax:pktcDectGroup})