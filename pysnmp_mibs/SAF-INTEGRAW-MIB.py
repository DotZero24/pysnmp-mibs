_BG='integraWEthernetMiiPortGroup'
_BF='integraWEthernetGeneralGroup'
_BE='integraWSystemGroup'
_BD='integraWModemGroup'
_BC='integraWRadioGroup'
_BB='integraWMiscGroup'
_BA='integraWtxCollisions'
_B9='integraWtxCarrierErrors'
_B8='integraWtxAlignErrors'
_B7='integraWtxExcessDeferral'
_B6='integraWtxExcessCollisions'
_B5='integraWtxLateCollisions'
_B4='integraWtxDeferred'
_B3='integraWtxMultiCollisions'
_B2='integraWtxSingleCollisions'
_B1='integraWtxPauseFrames'
_B0='integraWtxVlanFrames'
_A_='integraWtxCntrlFrames'
_Az='integraWtxUrunErrors'
_Ay='integraWtxMcastFrames'
_Ax='integraWtxBcastFrames'
_Aw='integraWtxFifoErr'
_Av='integraWtxErrors'
_Au='integraWtxGoodFrames'
_At='integraWrxFrameErrors'
_As='integraWrxOpErrors'
_Ar='integraWrxPauseFrames'
_Aq='integraWrxVlanFrames'
_Ap='integraWrxLenErrors'
_Ao='integraWrxCntrlFrames'
_An='integraWrxMcastFrames'
_Am='integraWrxBcastFrames'
_Al='integraWrxCRCErrors'
_Ak='integraWrxFifoErr'
_Aj='integraWrxErrors'
_Ai='integraWrxGoodFrames'
_Ah='integraWtxOsizeFrames'
_Ag='integraWtxUsizeFrames'
_Af='integraWtx1024toMaxFrames'
_Ae='integraWtx512to1023Frames'
_Ad='integraWtx256to511Frames'
_Ac='integraWtx128to255Frames'
_Ab='integraWtx65to127Frames'
_Aa='integraWtx64Frames'
_AZ='integraWrxOsizeFrames'
_AY='integraWrxUsizeFrames'
_AX='integraWrx1024toMaxFrames'
_AW='integraWrx512to1023Frames'
_AV='integraWrx256to511Frames'
_AU='integraWrx128to255Frames'
_AT='integraWrx65to127Frames'
_AS='integraWrx64Frames'
_AR='integraWtxBytes'
_AQ='integraWrxBytes'
_AP='integraWtxDropped'
_AO='integraWtxDetected'
_AN='integraWrxDropped'
_AM='integraWrxDetected'
_AL='integraWnetCfgRemoteIPaddress'
_AK='integraWnetCfgIPgateway'
_AJ='integraWnetCfgIPmask'
_AI='integraWnetCfgIPaddress'
_AH='integraWifTimePassed'
_AG='integraWifPortStcDescr'
_AF='integraWifPortFlowControl'
_AE='integraWifPortSyncEthPrio'
_AD='integraWifPortSyncEthActive'
_AC='integraWifPortDuplex'
_AB='integraWifPortAutoneg'
_AA='integraWifPortLastChange'
_A9='integraWifPortOperStatus'
_A8='integraWifPortAdminStatus'
_A7='integraWifPortPhysAddress'
_A6='integraWifPortSpeed'
_A5='integraWifPortMtu'
_A4='integraWifPortType'
_A3='integraWifPortStatDescr'
_A2='integraWstoreConfig'
_A1='integraWneedStore'
_A0='integraWexecuteConfig'
_z='integraWsysCPUidle'
_y='integraWsysFreeMemory'
_x='integraWsysBoardTemperature'
_w='integraWsysPSUpower'
_v='integraWsysPSUcurrent'
_u='integraWsysPSUvoltage'
_t='integraWsysLicenseGenStatus'
_s='integraWsysLicenseExpire'
_r='integraWsysCPUtemperature'
_q='integraWmodemSignalQuality'
_p='integraWmodemAcmEngine'
_o='integraWmodemTxCapacity'
_n='integraWmodemRxCapacity'
_m='integraWmodemTxModulation'
_l='integraWmodemRxModulation'
_k='integraWmodemModulation'
_j='integraWmodemBandwidth'
_i='integraWmodemSyncLoss'
_h='integraWmodemFecLoad'
_g='integraWmodemMse'
_f='integraWmodemAcquireStatus'
_e='integraWradioPLL'
_d='integraWradioRangeTxFrequency'
_c='integraWradioRangeTxPower'
_b='integraWradioRangeDescr'
_a='integraWradioTxMuteDuration'
_Z='integraWradioTemperature'
_Y='integraWradioRxFrequency'
_X='integraWradioDuplexShift'
_W='integraWradioTxMute'
_V='integraWradioSide'
_U='integraWradioRxLevel'
_T='integraWradioTxFrequency'
_S='integraWradioTxPower'
_R='integraWtimestamp'
_Q='integraWifPortStcIndex'
_P='integraWifPortStatIndex'
_O='integraWradioRangeEntryIndex'
_N='dBm'
_M='disabled'
_L='enabled'
_K='DisplayString'
_J='error'
_I='kHz'
_H='unknown'
_G='read-write'
_F='packet'
_E='Integer32'
_D='frame'
_C='read-only'
_B='SAF-INTEGRAW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
pointToPoint,=mibBuilder.importSymbols('SAF-ENTERPRISE','pointToPoint')
safIntegra,=mibBuilder.importSymbols('SAF-INTEGRA-MIB','safIntegra')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'PhysAddress','TextualConvention')
integraW=ModuleIdentity((1,3,6,1,4,1,7571,100,1,1,7,2))
if mibBuilder.loadTexts:integraW.setRevisions(('2016-05-11 00:00','2015-09-17 00:00','2015-09-15 00:00','2015-08-12 00:00','2015-07-29 00:00','2015-05-29 00:00','2015-05-20 00:00','2015-04-21 00:00','2015-04-14 00:00','2015-03-24 00:00','2015-02-04 00:00','2015-01-20 00:00','2015-01-08 00:00','2015-01-06 00:00'))
_IntegraWtimestamp_Type=DateAndTime
_IntegraWtimestamp_Object=MibScalar
integraWtimestamp=_IntegraWtimestamp_Object((1,3,6,1,4,1,7571,100,1,1,7,2,1),_IntegraWtimestamp_Type())
integraWtimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtimestamp.setStatus(_A)
_IntegraWradio_ObjectIdentity=ObjectIdentity
integraWradio=_IntegraWradio_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,2))
_IntegraWradioTxPower_Type=Integer32
_IntegraWradioTxPower_Object=MibScalar
integraWradioTxPower=_IntegraWradioTxPower_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,1),_IntegraWradioTxPower_Type())
integraWradioTxPower.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWradioTxPower.setStatus(_A)
if mibBuilder.loadTexts:integraWradioTxPower.setUnits(_N)
_IntegraWradioTxFrequency_Type=Integer32
_IntegraWradioTxFrequency_Object=MibScalar
integraWradioTxFrequency=_IntegraWradioTxFrequency_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,2),_IntegraWradioTxFrequency_Type())
integraWradioTxFrequency.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWradioTxFrequency.setStatus(_A)
if mibBuilder.loadTexts:integraWradioTxFrequency.setUnits(_I)
_IntegraWradioRxLevel_Type=Integer32
_IntegraWradioRxLevel_Object=MibScalar
integraWradioRxLevel=_IntegraWradioRxLevel_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,3),_IntegraWradioRxLevel_Type())
integraWradioRxLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRxLevel.setStatus(_A)
if mibBuilder.loadTexts:integraWradioRxLevel.setUnits(_N)
class _IntegraWradioSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('high',1),('low',2),(_J,3)))
_IntegraWradioSide_Type.__name__=_E
_IntegraWradioSide_Object=MibScalar
integraWradioSide=_IntegraWradioSide_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,4),_IntegraWradioSide_Type())
integraWradioSide.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioSide.setStatus(_A)
class _IntegraWradioTxMute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),(_J,3)))
_IntegraWradioTxMute_Type.__name__=_E
_IntegraWradioTxMute_Object=MibScalar
integraWradioTxMute=_IntegraWradioTxMute_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,5),_IntegraWradioTxMute_Type())
integraWradioTxMute.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioTxMute.setStatus(_A)
_IntegraWradioDuplexShift_Type=Integer32
_IntegraWradioDuplexShift_Object=MibScalar
integraWradioDuplexShift=_IntegraWradioDuplexShift_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,6),_IntegraWradioDuplexShift_Type())
integraWradioDuplexShift.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioDuplexShift.setStatus(_A)
if mibBuilder.loadTexts:integraWradioDuplexShift.setUnits(_I)
_IntegraWradioRxFrequency_Type=Integer32
_IntegraWradioRxFrequency_Object=MibScalar
integraWradioRxFrequency=_IntegraWradioRxFrequency_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,7),_IntegraWradioRxFrequency_Type())
integraWradioRxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRxFrequency.setStatus(_A)
if mibBuilder.loadTexts:integraWradioRxFrequency.setUnits(_I)
_IntegraWradioTemperature_Type=Integer32
_IntegraWradioTemperature_Object=MibScalar
integraWradioTemperature=_IntegraWradioTemperature_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,8),_IntegraWradioTemperature_Type())
integraWradioTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioTemperature.setStatus(_A)
if mibBuilder.loadTexts:integraWradioTemperature.setUnits('C')
class _IntegraWradioTxMuteDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214748364))
_IntegraWradioTxMuteDuration_Type.__name__=_E
_IntegraWradioTxMuteDuration_Object=MibScalar
integraWradioTxMuteDuration=_IntegraWradioTxMuteDuration_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,9),_IntegraWradioTxMuteDuration_Type())
integraWradioTxMuteDuration.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWradioTxMuteDuration.setStatus(_A)
if mibBuilder.loadTexts:integraWradioTxMuteDuration.setUnits('s')
_IntegraWradioRangesTable_Object=MibTable
integraWradioRangesTable=_IntegraWradioRangesTable_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10))
if mibBuilder.loadTexts:integraWradioRangesTable.setStatus(_A)
_IntegraWradioRangeEntry_Object=MibTableRow
integraWradioRangeEntry=_IntegraWradioRangeEntry_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10,1))
integraWradioRangeEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:integraWradioRangeEntry.setStatus(_A)
class _IntegraWradioRangeEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IntegraWradioRangeEntryIndex_Type.__name__=_E
_IntegraWradioRangeEntryIndex_Object=MibTableColumn
integraWradioRangeEntryIndex=_IntegraWradioRangeEntryIndex_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10,1,1),_IntegraWradioRangeEntryIndex_Type())
integraWradioRangeEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRangeEntryIndex.setStatus(_A)
class _IntegraWradioRangeDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IntegraWradioRangeDescr_Type.__name__=_K
_IntegraWradioRangeDescr_Object=MibTableColumn
integraWradioRangeDescr=_IntegraWradioRangeDescr_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10,1,2),_IntegraWradioRangeDescr_Type())
integraWradioRangeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRangeDescr.setStatus(_A)
_IntegraWradioRangeTxPower_Type=Integer32
_IntegraWradioRangeTxPower_Object=MibTableColumn
integraWradioRangeTxPower=_IntegraWradioRangeTxPower_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10,1,3),_IntegraWradioRangeTxPower_Type())
integraWradioRangeTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRangeTxPower.setStatus(_A)
if mibBuilder.loadTexts:integraWradioRangeTxPower.setUnits(_N)
_IntegraWradioRangeTxFrequency_Type=Integer32
_IntegraWradioRangeTxFrequency_Object=MibTableColumn
integraWradioRangeTxFrequency=_IntegraWradioRangeTxFrequency_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,10,1,4),_IntegraWradioRangeTxFrequency_Type())
integraWradioRangeTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRangeTxFrequency.setStatus(_A)
if mibBuilder.loadTexts:integraWradioRangeTxFrequency.setUnits(_I)
class _IntegraWradioPLL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('ok',2)))
_IntegraWradioPLL_Type.__name__=_E
_IntegraWradioPLL_Object=MibScalar
integraWradioPLL=_IntegraWradioPLL_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,11),_IntegraWradioPLL_Type())
integraWradioPLL.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioPLL.setStatus(_A)
class _IntegraWradioRxLevelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('low',2),('high',3),(_J,4)))
_IntegraWradioRxLevelState_Type.__name__=_E
_IntegraWradioRxLevelState_Object=MibScalar
integraWradioRxLevelState=_IntegraWradioRxLevelState_Object((1,3,6,1,4,1,7571,100,1,1,7,2,2,12),_IntegraWradioRxLevelState_Type())
integraWradioRxLevelState.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWradioRxLevelState.setStatus(_A)
_IntegraWmodem_ObjectIdentity=ObjectIdentity
integraWmodem=_IntegraWmodem_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,3))
class _IntegraWmodemAcquireStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acquireInProgress',1),('acquireLocked',2),('acquireFailed',3)))
_IntegraWmodemAcquireStatus_Type.__name__=_E
_IntegraWmodemAcquireStatus_Object=MibScalar
integraWmodemAcquireStatus=_IntegraWmodemAcquireStatus_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,1),_IntegraWmodemAcquireStatus_Type())
integraWmodemAcquireStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemAcquireStatus.setStatus(_A)
_IntegraWmodemMse_Type=Integer32
_IntegraWmodemMse_Object=MibScalar
integraWmodemMse=_IntegraWmodemMse_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,2),_IntegraWmodemMse_Type())
integraWmodemMse.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemMse.setStatus(_A)
if mibBuilder.loadTexts:integraWmodemMse.setUnits('dB')
_IntegraWmodemFecLoad_Type=DisplayString
_IntegraWmodemFecLoad_Object=MibScalar
integraWmodemFecLoad=_IntegraWmodemFecLoad_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,3),_IntegraWmodemFecLoad_Type())
integraWmodemFecLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemFecLoad.setStatus(_A)
class _IntegraWmodemSyncLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('locked',1),('unlocked',2),(_H,3)))
_IntegraWmodemSyncLoss_Type.__name__=_E
_IntegraWmodemSyncLoss_Object=MibScalar
integraWmodemSyncLoss=_IntegraWmodemSyncLoss_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,4),_IntegraWmodemSyncLoss_Type())
integraWmodemSyncLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemSyncLoss.setStatus(_A)
_IntegraWmodemBandwidth_Type=Integer32
_IntegraWmodemBandwidth_Object=MibScalar
integraWmodemBandwidth=_IntegraWmodemBandwidth_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,6),_IntegraWmodemBandwidth_Type())
integraWmodemBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemBandwidth.setStatus(_A)
if mibBuilder.loadTexts:integraWmodemBandwidth.setUnits(_I)
_IntegraWmodemModulation_Type=DisplayString
_IntegraWmodemModulation_Object=MibScalar
integraWmodemModulation=_IntegraWmodemModulation_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,7),_IntegraWmodemModulation_Type())
integraWmodemModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemModulation.setStatus(_A)
_IntegraWmodemRxModulation_Type=DisplayString
_IntegraWmodemRxModulation_Object=MibScalar
integraWmodemRxModulation=_IntegraWmodemRxModulation_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,8),_IntegraWmodemRxModulation_Type())
integraWmodemRxModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemRxModulation.setStatus(_A)
_IntegraWmodemTxModulation_Type=DisplayString
_IntegraWmodemTxModulation_Object=MibScalar
integraWmodemTxModulation=_IntegraWmodemTxModulation_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,9),_IntegraWmodemTxModulation_Type())
integraWmodemTxModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemTxModulation.setStatus(_A)
_IntegraWmodemRxCapacity_Type=Integer32
_IntegraWmodemRxCapacity_Object=MibScalar
integraWmodemRxCapacity=_IntegraWmodemRxCapacity_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,10),_IntegraWmodemRxCapacity_Type())
integraWmodemRxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemRxCapacity.setStatus(_A)
if mibBuilder.loadTexts:integraWmodemRxCapacity.setUnits('kb/s')
_IntegraWmodemTxCapacity_Type=Integer32
_IntegraWmodemTxCapacity_Object=MibScalar
integraWmodemTxCapacity=_IntegraWmodemTxCapacity_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,11),_IntegraWmodemTxCapacity_Type())
integraWmodemTxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemTxCapacity.setStatus(_A)
if mibBuilder.loadTexts:integraWmodemTxCapacity.setUnits('kb/s')
class _IntegraWmodemAcmEngine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_J,3)))
_IntegraWmodemAcmEngine_Type.__name__=_E
_IntegraWmodemAcmEngine_Object=MibScalar
integraWmodemAcmEngine=_IntegraWmodemAcmEngine_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,12),_IntegraWmodemAcmEngine_Type())
integraWmodemAcmEngine.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemAcmEngine.setStatus(_A)
_IntegraWmodemSignalQuality_Type=Integer32
_IntegraWmodemSignalQuality_Object=MibScalar
integraWmodemSignalQuality=_IntegraWmodemSignalQuality_Object((1,3,6,1,4,1,7571,100,1,1,7,2,3,14),_IntegraWmodemSignalQuality_Type())
integraWmodemSignalQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWmodemSignalQuality.setStatus(_A)
if mibBuilder.loadTexts:integraWmodemSignalQuality.setUnits('%')
_IntegraWsystem_ObjectIdentity=ObjectIdentity
integraWsystem=_IntegraWsystem_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,4))
_IntegraWsysCPUtemperature_Type=Integer32
_IntegraWsysCPUtemperature_Object=MibScalar
integraWsysCPUtemperature=_IntegraWsysCPUtemperature_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,2),_IntegraWsysCPUtemperature_Type())
integraWsysCPUtemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysCPUtemperature.setStatus(_A)
if mibBuilder.loadTexts:integraWsysCPUtemperature.setUnits('C')
_IntegraWsysLicenseExpire_Type=Gauge32
_IntegraWsysLicenseExpire_Object=MibScalar
integraWsysLicenseExpire=_IntegraWsysLicenseExpire_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,3),_IntegraWsysLicenseExpire_Type())
integraWsysLicenseExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysLicenseExpire.setStatus(_A)
if mibBuilder.loadTexts:integraWsysLicenseExpire.setUnits('s')
class _IntegraWsysLicenseGenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('expired',2),(_H,3),('unlimitedTime',4)))
_IntegraWsysLicenseGenStatus_Type.__name__=_E
_IntegraWsysLicenseGenStatus_Object=MibScalar
integraWsysLicenseGenStatus=_IntegraWsysLicenseGenStatus_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,4),_IntegraWsysLicenseGenStatus_Type())
integraWsysLicenseGenStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysLicenseGenStatus.setStatus(_A)
_IntegraWsysPSUvoltage_Type=Integer32
_IntegraWsysPSUvoltage_Object=MibScalar
integraWsysPSUvoltage=_IntegraWsysPSUvoltage_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,5),_IntegraWsysPSUvoltage_Type())
integraWsysPSUvoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysPSUvoltage.setStatus(_A)
if mibBuilder.loadTexts:integraWsysPSUvoltage.setUnits('mV')
_IntegraWsysPSUcurrent_Type=Integer32
_IntegraWsysPSUcurrent_Object=MibScalar
integraWsysPSUcurrent=_IntegraWsysPSUcurrent_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,6),_IntegraWsysPSUcurrent_Type())
integraWsysPSUcurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysPSUcurrent.setStatus(_A)
if mibBuilder.loadTexts:integraWsysPSUcurrent.setUnits('mA')
_IntegraWsysPSUpower_Type=Integer32
_IntegraWsysPSUpower_Object=MibScalar
integraWsysPSUpower=_IntegraWsysPSUpower_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,7),_IntegraWsysPSUpower_Type())
integraWsysPSUpower.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysPSUpower.setStatus(_A)
if mibBuilder.loadTexts:integraWsysPSUpower.setUnits('mW')
_IntegraWsysBoardTemperature_Type=Integer32
_IntegraWsysBoardTemperature_Object=MibScalar
integraWsysBoardTemperature=_IntegraWsysBoardTemperature_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,8),_IntegraWsysBoardTemperature_Type())
integraWsysBoardTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysBoardTemperature.setStatus(_A)
if mibBuilder.loadTexts:integraWsysBoardTemperature.setUnits('C')
_IntegraWsysFreeMemory_Type=Integer32
_IntegraWsysFreeMemory_Object=MibScalar
integraWsysFreeMemory=_IntegraWsysFreeMemory_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,9),_IntegraWsysFreeMemory_Type())
integraWsysFreeMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysFreeMemory.setStatus(_A)
if mibBuilder.loadTexts:integraWsysFreeMemory.setUnits('%')
_IntegraWsysCPUidle_Type=Integer32
_IntegraWsysCPUidle_Object=MibScalar
integraWsysCPUidle=_IntegraWsysCPUidle_Object((1,3,6,1,4,1,7571,100,1,1,7,2,4,10),_IntegraWsysCPUidle_Type())
integraWsysCPUidle.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWsysCPUidle.setStatus(_A)
if mibBuilder.loadTexts:integraWsysCPUidle.setUnits('%')
_IntegraWethernet_ObjectIdentity=ObjectIdentity
integraWethernet=_IntegraWethernet_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,5))
_IntegraWifStatusTable_Object=MibTable
integraWifStatusTable=_IntegraWifStatusTable_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1))
if mibBuilder.loadTexts:integraWifStatusTable.setStatus(_A)
_IntegraWifPortEntry_Object=MibTableRow
integraWifPortEntry=_IntegraWifPortEntry_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1))
integraWifPortEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:integraWifPortEntry.setStatus(_A)
class _IntegraWifPortStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IntegraWifPortStatIndex_Type.__name__=_E
_IntegraWifPortStatIndex_Object=MibTableColumn
integraWifPortStatIndex=_IntegraWifPortStatIndex_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,1),_IntegraWifPortStatIndex_Type())
integraWifPortStatIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortStatIndex.setStatus(_A)
class _IntegraWifPortStatDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IntegraWifPortStatDescr_Type.__name__=_K
_IntegraWifPortStatDescr_Object=MibTableColumn
integraWifPortStatDescr=_IntegraWifPortStatDescr_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,2),_IntegraWifPortStatDescr_Type())
integraWifPortStatDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortStatDescr.setStatus(_A)
_IntegraWifPortType_Type=IANAifType
_IntegraWifPortType_Object=MibTableColumn
integraWifPortType=_IntegraWifPortType_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,3),_IntegraWifPortType_Type())
integraWifPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortType.setStatus(_A)
_IntegraWifPortMtu_Type=Integer32
_IntegraWifPortMtu_Object=MibTableColumn
integraWifPortMtu=_IntegraWifPortMtu_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,4),_IntegraWifPortMtu_Type())
integraWifPortMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortMtu.setStatus(_A)
if mibBuilder.loadTexts:integraWifPortMtu.setUnits('B')
_IntegraWifPortSpeed_Type=Gauge32
_IntegraWifPortSpeed_Object=MibTableColumn
integraWifPortSpeed=_IntegraWifPortSpeed_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,5),_IntegraWifPortSpeed_Type())
integraWifPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:integraWifPortSpeed.setUnits('bps')
_IntegraWifPortPhysAddress_Type=PhysAddress
_IntegraWifPortPhysAddress_Object=MibTableColumn
integraWifPortPhysAddress=_IntegraWifPortPhysAddress_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,6),_IntegraWifPortPhysAddress_Type())
integraWifPortPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortPhysAddress.setStatus(_A)
class _IntegraWifPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_H,3)))
_IntegraWifPortAdminStatus_Type.__name__=_E
_IntegraWifPortAdminStatus_Object=MibTableColumn
integraWifPortAdminStatus=_IntegraWifPortAdminStatus_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,7),_IntegraWifPortAdminStatus_Type())
integraWifPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortAdminStatus.setStatus(_A)
class _IntegraWifPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_H,3)))
_IntegraWifPortOperStatus_Type.__name__=_E
_IntegraWifPortOperStatus_Object=MibTableColumn
integraWifPortOperStatus=_IntegraWifPortOperStatus_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,8),_IntegraWifPortOperStatus_Type())
integraWifPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortOperStatus.setStatus(_A)
_IntegraWifPortLastChange_Type=TimeTicks
_IntegraWifPortLastChange_Object=MibTableColumn
integraWifPortLastChange=_IntegraWifPortLastChange_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,9),_IntegraWifPortLastChange_Type())
integraWifPortLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortLastChange.setStatus(_A)
class _IntegraWifPortAutoneg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_H,3)))
_IntegraWifPortAutoneg_Type.__name__=_E
_IntegraWifPortAutoneg_Object=MibTableColumn
integraWifPortAutoneg=_IntegraWifPortAutoneg_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,10),_IntegraWifPortAutoneg_Type())
integraWifPortAutoneg.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortAutoneg.setStatus(_A)
class _IntegraWifPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),(_H,3)))
_IntegraWifPortDuplex_Type.__name__=_E
_IntegraWifPortDuplex_Object=MibTableColumn
integraWifPortDuplex=_IntegraWifPortDuplex_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,11),_IntegraWifPortDuplex_Type())
integraWifPortDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortDuplex.setStatus(_A)
class _IntegraWifPortSyncEthActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_IntegraWifPortSyncEthActive_Type.__name__=_E
_IntegraWifPortSyncEthActive_Object=MibTableColumn
integraWifPortSyncEthActive=_IntegraWifPortSyncEthActive_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,12),_IntegraWifPortSyncEthActive_Type())
integraWifPortSyncEthActive.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortSyncEthActive.setStatus(_A)
_IntegraWifPortSyncEthPrio_Type=Integer32
_IntegraWifPortSyncEthPrio_Object=MibTableColumn
integraWifPortSyncEthPrio=_IntegraWifPortSyncEthPrio_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,13),_IntegraWifPortSyncEthPrio_Type())
integraWifPortSyncEthPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortSyncEthPrio.setStatus(_A)
class _IntegraWifPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_H,3)))
_IntegraWifPortFlowControl_Type.__name__=_E
_IntegraWifPortFlowControl_Object=MibTableColumn
integraWifPortFlowControl=_IntegraWifPortFlowControl_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,1,1,14),_IntegraWifPortFlowControl_Type())
integraWifPortFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortFlowControl.setStatus(_A)
_IntegraWifStatisticsTable_Object=MibTable
integraWifStatisticsTable=_IntegraWifStatisticsTable_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2))
if mibBuilder.loadTexts:integraWifStatisticsTable.setStatus(_A)
_IntegraWifPortStcEntry_Object=MibTableRow
integraWifPortStcEntry=_IntegraWifPortStcEntry_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1))
integraWifPortStcEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:integraWifPortStcEntry.setStatus(_A)
class _IntegraWifPortStcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_IntegraWifPortStcIndex_Type.__name__=_E
_IntegraWifPortStcIndex_Object=MibTableColumn
integraWifPortStcIndex=_IntegraWifPortStcIndex_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,1),_IntegraWifPortStcIndex_Type())
integraWifPortStcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortStcIndex.setStatus(_A)
class _IntegraWifPortStcDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IntegraWifPortStcDescr_Type.__name__=_K
_IntegraWifPortStcDescr_Object=MibTableColumn
integraWifPortStcDescr=_IntegraWifPortStcDescr_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,2),_IntegraWifPortStcDescr_Type())
integraWifPortStcDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifPortStcDescr.setStatus(_A)
_IntegraWifTimePassed_Type=TimeTicks
_IntegraWifTimePassed_Object=MibTableColumn
integraWifTimePassed=_IntegraWifTimePassed_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,3),_IntegraWifTimePassed_Type())
integraWifTimePassed.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWifTimePassed.setStatus(_A)
if mibBuilder.loadTexts:integraWifTimePassed.setUnits('s/100')
_IntegraWrxDetected_Type=Counter64
_IntegraWrxDetected_Object=MibTableColumn
integraWrxDetected=_IntegraWrxDetected_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,4),_IntegraWrxDetected_Type())
integraWrxDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxDetected.setStatus(_A)
if mibBuilder.loadTexts:integraWrxDetected.setUnits(_F)
_IntegraWrxDropped_Type=Counter64
_IntegraWrxDropped_Object=MibTableColumn
integraWrxDropped=_IntegraWrxDropped_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,5),_IntegraWrxDropped_Type())
integraWrxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxDropped.setStatus(_A)
if mibBuilder.loadTexts:integraWrxDropped.setUnits(_F)
_IntegraWtxDetected_Type=Counter64
_IntegraWtxDetected_Object=MibTableColumn
integraWtxDetected=_IntegraWtxDetected_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,6),_IntegraWtxDetected_Type())
integraWtxDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxDetected.setStatus(_A)
if mibBuilder.loadTexts:integraWtxDetected.setUnits(_F)
_IntegraWtxDropped_Type=Counter64
_IntegraWtxDropped_Object=MibTableColumn
integraWtxDropped=_IntegraWtxDropped_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,7),_IntegraWtxDropped_Type())
integraWtxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxDropped.setStatus(_A)
if mibBuilder.loadTexts:integraWtxDropped.setUnits(_F)
_IntegraWrxBytes_Type=Counter64
_IntegraWrxBytes_Object=MibTableColumn
integraWrxBytes=_IntegraWrxBytes_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,8),_IntegraWrxBytes_Type())
integraWrxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxBytes.setStatus(_A)
if mibBuilder.loadTexts:integraWrxBytes.setUnits('B')
_IntegraWtxBytes_Type=Counter64
_IntegraWtxBytes_Object=MibTableColumn
integraWtxBytes=_IntegraWtxBytes_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,9),_IntegraWtxBytes_Type())
integraWtxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxBytes.setStatus(_A)
if mibBuilder.loadTexts:integraWtxBytes.setUnits('B')
_IntegraWrx64Frames_Type=Counter64
_IntegraWrx64Frames_Object=MibTableColumn
integraWrx64Frames=_IntegraWrx64Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,10),_IntegraWrx64Frames_Type())
integraWrx64Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx64Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx64Frames.setUnits(_D)
_IntegraWrx65to127Frames_Type=Counter64
_IntegraWrx65to127Frames_Object=MibTableColumn
integraWrx65to127Frames=_IntegraWrx65to127Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,11),_IntegraWrx65to127Frames_Type())
integraWrx65to127Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx65to127Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx65to127Frames.setUnits(_D)
_IntegraWrx128to255Frames_Type=Counter64
_IntegraWrx128to255Frames_Object=MibTableColumn
integraWrx128to255Frames=_IntegraWrx128to255Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,12),_IntegraWrx128to255Frames_Type())
integraWrx128to255Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx128to255Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx128to255Frames.setUnits(_D)
_IntegraWrx256to511Frames_Type=Counter64
_IntegraWrx256to511Frames_Object=MibTableColumn
integraWrx256to511Frames=_IntegraWrx256to511Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,13),_IntegraWrx256to511Frames_Type())
integraWrx256to511Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx256to511Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx256to511Frames.setUnits(_D)
_IntegraWrx512to1023Frames_Type=Counter64
_IntegraWrx512to1023Frames_Object=MibTableColumn
integraWrx512to1023Frames=_IntegraWrx512to1023Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,14),_IntegraWrx512to1023Frames_Type())
integraWrx512to1023Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx512to1023Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx512to1023Frames.setUnits(_D)
_IntegraWrx1024toMaxFrames_Type=Counter64
_IntegraWrx1024toMaxFrames_Object=MibTableColumn
integraWrx1024toMaxFrames=_IntegraWrx1024toMaxFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,15),_IntegraWrx1024toMaxFrames_Type())
integraWrx1024toMaxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrx1024toMaxFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrx1024toMaxFrames.setUnits(_D)
_IntegraWrxUsizeFrames_Type=Counter64
_IntegraWrxUsizeFrames_Object=MibTableColumn
integraWrxUsizeFrames=_IntegraWrxUsizeFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,16),_IntegraWrxUsizeFrames_Type())
integraWrxUsizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxUsizeFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxUsizeFrames.setUnits(_D)
_IntegraWrxOsizeFrames_Type=Counter64
_IntegraWrxOsizeFrames_Object=MibTableColumn
integraWrxOsizeFrames=_IntegraWrxOsizeFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,17),_IntegraWrxOsizeFrames_Type())
integraWrxOsizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxOsizeFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxOsizeFrames.setUnits(_D)
_IntegraWtx64Frames_Type=Counter64
_IntegraWtx64Frames_Object=MibTableColumn
integraWtx64Frames=_IntegraWtx64Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,18),_IntegraWtx64Frames_Type())
integraWtx64Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx64Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx64Frames.setUnits(_D)
_IntegraWtx65to127Frames_Type=Counter64
_IntegraWtx65to127Frames_Object=MibTableColumn
integraWtx65to127Frames=_IntegraWtx65to127Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,19),_IntegraWtx65to127Frames_Type())
integraWtx65to127Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx65to127Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx65to127Frames.setUnits(_D)
_IntegraWtx128to255Frames_Type=Counter64
_IntegraWtx128to255Frames_Object=MibTableColumn
integraWtx128to255Frames=_IntegraWtx128to255Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,20),_IntegraWtx128to255Frames_Type())
integraWtx128to255Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx128to255Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx128to255Frames.setUnits(_D)
_IntegraWtx256to511Frames_Type=Counter64
_IntegraWtx256to511Frames_Object=MibTableColumn
integraWtx256to511Frames=_IntegraWtx256to511Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,21),_IntegraWtx256to511Frames_Type())
integraWtx256to511Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx256to511Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx256to511Frames.setUnits(_D)
_IntegraWtx512to1023Frames_Type=Counter64
_IntegraWtx512to1023Frames_Object=MibTableColumn
integraWtx512to1023Frames=_IntegraWtx512to1023Frames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,22),_IntegraWtx512to1023Frames_Type())
integraWtx512to1023Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx512to1023Frames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx512to1023Frames.setUnits(_D)
_IntegraWtx1024toMaxFrames_Type=Counter64
_IntegraWtx1024toMaxFrames_Object=MibTableColumn
integraWtx1024toMaxFrames=_IntegraWtx1024toMaxFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,23),_IntegraWtx1024toMaxFrames_Type())
integraWtx1024toMaxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtx1024toMaxFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtx1024toMaxFrames.setUnits(_D)
_IntegraWtxUsizeFrames_Type=Counter64
_IntegraWtxUsizeFrames_Object=MibTableColumn
integraWtxUsizeFrames=_IntegraWtxUsizeFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,24),_IntegraWtxUsizeFrames_Type())
integraWtxUsizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxUsizeFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxUsizeFrames.setUnits(_D)
_IntegraWtxOsizeFrames_Type=Counter64
_IntegraWtxOsizeFrames_Object=MibTableColumn
integraWtxOsizeFrames=_IntegraWtxOsizeFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,25),_IntegraWtxOsizeFrames_Type())
integraWtxOsizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxOsizeFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxOsizeFrames.setUnits(_D)
_IntegraWrxGoodFrames_Type=Counter64
_IntegraWrxGoodFrames_Object=MibTableColumn
integraWrxGoodFrames=_IntegraWrxGoodFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,26),_IntegraWrxGoodFrames_Type())
integraWrxGoodFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxGoodFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxGoodFrames.setUnits(_D)
_IntegraWrxErrors_Type=Counter64
_IntegraWrxErrors_Object=MibTableColumn
integraWrxErrors=_IntegraWrxErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,27),_IntegraWrxErrors_Type())
integraWrxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWrxErrors.setUnits(_F)
_IntegraWrxFifoErr_Type=Counter64
_IntegraWrxFifoErr_Object=MibTableColumn
integraWrxFifoErr=_IntegraWrxFifoErr_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,28),_IntegraWrxFifoErr_Type())
integraWrxFifoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxFifoErr.setStatus(_A)
if mibBuilder.loadTexts:integraWrxFifoErr.setUnits(_F)
_IntegraWrxCRCErrors_Type=Counter64
_IntegraWrxCRCErrors_Object=MibTableColumn
integraWrxCRCErrors=_IntegraWrxCRCErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,29),_IntegraWrxCRCErrors_Type())
integraWrxCRCErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxCRCErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWrxCRCErrors.setUnits(_F)
_IntegraWrxBcastFrames_Type=Counter64
_IntegraWrxBcastFrames_Object=MibTableColumn
integraWrxBcastFrames=_IntegraWrxBcastFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,30),_IntegraWrxBcastFrames_Type())
integraWrxBcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxBcastFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxBcastFrames.setUnits(_D)
_IntegraWrxMcastFrames_Type=Counter64
_IntegraWrxMcastFrames_Object=MibTableColumn
integraWrxMcastFrames=_IntegraWrxMcastFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,31),_IntegraWrxMcastFrames_Type())
integraWrxMcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxMcastFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxMcastFrames.setUnits(_D)
_IntegraWrxCntrlFrames_Type=Counter64
_IntegraWrxCntrlFrames_Object=MibTableColumn
integraWrxCntrlFrames=_IntegraWrxCntrlFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,32),_IntegraWrxCntrlFrames_Type())
integraWrxCntrlFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxCntrlFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxCntrlFrames.setUnits(_D)
_IntegraWrxLenErrors_Type=Counter64
_IntegraWrxLenErrors_Object=MibTableColumn
integraWrxLenErrors=_IntegraWrxLenErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,33),_IntegraWrxLenErrors_Type())
integraWrxLenErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxLenErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWrxLenErrors.setUnits(_F)
_IntegraWrxVlanFrames_Type=Counter64
_IntegraWrxVlanFrames_Object=MibTableColumn
integraWrxVlanFrames=_IntegraWrxVlanFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,34),_IntegraWrxVlanFrames_Type())
integraWrxVlanFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxVlanFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxVlanFrames.setUnits(_D)
_IntegraWrxPauseFrames_Type=Counter64
_IntegraWrxPauseFrames_Object=MibTableColumn
integraWrxPauseFrames=_IntegraWrxPauseFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,35),_IntegraWrxPauseFrames_Type())
integraWrxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxPauseFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWrxPauseFrames.setUnits(_D)
_IntegraWrxOpErrors_Type=Counter64
_IntegraWrxOpErrors_Object=MibTableColumn
integraWrxOpErrors=_IntegraWrxOpErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,36),_IntegraWrxOpErrors_Type())
integraWrxOpErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxOpErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWrxOpErrors.setUnits(_F)
_IntegraWrxFrameErrors_Type=Counter64
_IntegraWrxFrameErrors_Object=MibTableColumn
integraWrxFrameErrors=_IntegraWrxFrameErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,37),_IntegraWrxFrameErrors_Type())
integraWrxFrameErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWrxFrameErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWrxFrameErrors.setUnits(_D)
_IntegraWtxGoodFrames_Type=Counter64
_IntegraWtxGoodFrames_Object=MibTableColumn
integraWtxGoodFrames=_IntegraWtxGoodFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,38),_IntegraWtxGoodFrames_Type())
integraWtxGoodFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxGoodFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxGoodFrames.setUnits(_D)
_IntegraWtxErrors_Type=Counter64
_IntegraWtxErrors_Object=MibTableColumn
integraWtxErrors=_IntegraWtxErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,39),_IntegraWtxErrors_Type())
integraWtxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWtxErrors.setUnits(_F)
_IntegraWtxFifoErr_Type=Counter64
_IntegraWtxFifoErr_Object=MibTableColumn
integraWtxFifoErr=_IntegraWtxFifoErr_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,40),_IntegraWtxFifoErr_Type())
integraWtxFifoErr.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxFifoErr.setStatus(_A)
if mibBuilder.loadTexts:integraWtxFifoErr.setUnits(_F)
_IntegraWtxBcastFrames_Type=Counter64
_IntegraWtxBcastFrames_Object=MibTableColumn
integraWtxBcastFrames=_IntegraWtxBcastFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,41),_IntegraWtxBcastFrames_Type())
integraWtxBcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxBcastFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxBcastFrames.setUnits(_D)
_IntegraWtxMcastFrames_Type=Counter64
_IntegraWtxMcastFrames_Object=MibTableColumn
integraWtxMcastFrames=_IntegraWtxMcastFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,42),_IntegraWtxMcastFrames_Type())
integraWtxMcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxMcastFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxMcastFrames.setUnits(_D)
_IntegraWtxUrunErrors_Type=Counter64
_IntegraWtxUrunErrors_Object=MibTableColumn
integraWtxUrunErrors=_IntegraWtxUrunErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,43),_IntegraWtxUrunErrors_Type())
integraWtxUrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxUrunErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWtxUrunErrors.setUnits(_F)
_IntegraWtxCntrlFrames_Type=Counter64
_IntegraWtxCntrlFrames_Object=MibTableColumn
integraWtxCntrlFrames=_IntegraWtxCntrlFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,44),_IntegraWtxCntrlFrames_Type())
integraWtxCntrlFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxCntrlFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxCntrlFrames.setUnits(_D)
_IntegraWtxVlanFrames_Type=Counter64
_IntegraWtxVlanFrames_Object=MibTableColumn
integraWtxVlanFrames=_IntegraWtxVlanFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,45),_IntegraWtxVlanFrames_Type())
integraWtxVlanFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxVlanFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxVlanFrames.setUnits(_D)
_IntegraWtxPauseFrames_Type=Counter64
_IntegraWtxPauseFrames_Object=MibTableColumn
integraWtxPauseFrames=_IntegraWtxPauseFrames_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,46),_IntegraWtxPauseFrames_Type())
integraWtxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxPauseFrames.setStatus(_A)
if mibBuilder.loadTexts:integraWtxPauseFrames.setUnits(_D)
_IntegraWtxSingleCollisions_Type=Counter64
_IntegraWtxSingleCollisions_Object=MibTableColumn
integraWtxSingleCollisions=_IntegraWtxSingleCollisions_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,47),_IntegraWtxSingleCollisions_Type())
integraWtxSingleCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxSingleCollisions.setStatus(_A)
if mibBuilder.loadTexts:integraWtxSingleCollisions.setUnits(_F)
_IntegraWtxMultiCollisions_Type=Counter64
_IntegraWtxMultiCollisions_Object=MibTableColumn
integraWtxMultiCollisions=_IntegraWtxMultiCollisions_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,48),_IntegraWtxMultiCollisions_Type())
integraWtxMultiCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxMultiCollisions.setStatus(_A)
if mibBuilder.loadTexts:integraWtxMultiCollisions.setUnits(_F)
_IntegraWtxDeferred_Type=Counter64
_IntegraWtxDeferred_Object=MibTableColumn
integraWtxDeferred=_IntegraWtxDeferred_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,49),_IntegraWtxDeferred_Type())
integraWtxDeferred.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxDeferred.setStatus(_A)
if mibBuilder.loadTexts:integraWtxDeferred.setUnits(_F)
_IntegraWtxLateCollisions_Type=Counter64
_IntegraWtxLateCollisions_Object=MibTableColumn
integraWtxLateCollisions=_IntegraWtxLateCollisions_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,50),_IntegraWtxLateCollisions_Type())
integraWtxLateCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxLateCollisions.setStatus(_A)
if mibBuilder.loadTexts:integraWtxLateCollisions.setUnits(_F)
_IntegraWtxExcessCollisions_Type=Counter64
_IntegraWtxExcessCollisions_Object=MibTableColumn
integraWtxExcessCollisions=_IntegraWtxExcessCollisions_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,51),_IntegraWtxExcessCollisions_Type())
integraWtxExcessCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxExcessCollisions.setStatus(_A)
if mibBuilder.loadTexts:integraWtxExcessCollisions.setUnits(_F)
_IntegraWtxExcessDeferral_Type=Counter64
_IntegraWtxExcessDeferral_Object=MibTableColumn
integraWtxExcessDeferral=_IntegraWtxExcessDeferral_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,52),_IntegraWtxExcessDeferral_Type())
integraWtxExcessDeferral.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxExcessDeferral.setStatus(_A)
if mibBuilder.loadTexts:integraWtxExcessDeferral.setUnits(_F)
_IntegraWtxAlignErrors_Type=Counter64
_IntegraWtxAlignErrors_Object=MibTableColumn
integraWtxAlignErrors=_IntegraWtxAlignErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,53),_IntegraWtxAlignErrors_Type())
integraWtxAlignErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxAlignErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWtxAlignErrors.setUnits(_F)
_IntegraWtxCarrierErrors_Type=Counter64
_IntegraWtxCarrierErrors_Object=MibTableColumn
integraWtxCarrierErrors=_IntegraWtxCarrierErrors_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,54),_IntegraWtxCarrierErrors_Type())
integraWtxCarrierErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxCarrierErrors.setStatus(_A)
if mibBuilder.loadTexts:integraWtxCarrierErrors.setUnits(_F)
_IntegraWtxCollisions_Type=Counter64
_IntegraWtxCollisions_Object=MibTableColumn
integraWtxCollisions=_IntegraWtxCollisions_Object((1,3,6,1,4,1,7571,100,1,1,7,2,5,2,1,55),_IntegraWtxCollisions_Type())
integraWtxCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWtxCollisions.setStatus(_A)
if mibBuilder.loadTexts:integraWtxCollisions.setUnits(_F)
class _IntegraWexecuteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('execute',1))
_IntegraWexecuteConfig_Type.__name__=_E
_IntegraWexecuteConfig_Object=MibScalar
integraWexecuteConfig=_IntegraWexecuteConfig_Object((1,3,6,1,4,1,7571,100,1,1,7,2,6),_IntegraWexecuteConfig_Type())
integraWexecuteConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWexecuteConfig.setStatus(_A)
class _IntegraWneedStore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('no',0))
_IntegraWneedStore_Type.__name__=_E
_IntegraWneedStore_Object=MibScalar
integraWneedStore=_IntegraWneedStore_Object((1,3,6,1,4,1,7571,100,1,1,7,2,7),_IntegraWneedStore_Type())
integraWneedStore.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWneedStore.setStatus(_A)
class _IntegraWstoreConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('store',1))
_IntegraWstoreConfig_Type.__name__=_E
_IntegraWstoreConfig_Object=MibScalar
integraWstoreConfig=_IntegraWstoreConfig_Object((1,3,6,1,4,1,7571,100,1,1,7,2,8),_IntegraWstoreConfig_Type())
integraWstoreConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWstoreConfig.setStatus(_A)
_IntegraWnetCfg_ObjectIdentity=ObjectIdentity
integraWnetCfg=_IntegraWnetCfg_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,9))
_IntegraWnetCfgIPaddress_Type=IpAddress
_IntegraWnetCfgIPaddress_Object=MibScalar
integraWnetCfgIPaddress=_IntegraWnetCfgIPaddress_Object((1,3,6,1,4,1,7571,100,1,1,7,2,9,1),_IntegraWnetCfgIPaddress_Type())
integraWnetCfgIPaddress.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWnetCfgIPaddress.setStatus(_A)
_IntegraWnetCfgIPmask_Type=IpAddress
_IntegraWnetCfgIPmask_Object=MibScalar
integraWnetCfgIPmask=_IntegraWnetCfgIPmask_Object((1,3,6,1,4,1,7571,100,1,1,7,2,9,2),_IntegraWnetCfgIPmask_Type())
integraWnetCfgIPmask.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWnetCfgIPmask.setStatus(_A)
_IntegraWnetCfgIPgateway_Type=IpAddress
_IntegraWnetCfgIPgateway_Object=MibScalar
integraWnetCfgIPgateway=_IntegraWnetCfgIPgateway_Object((1,3,6,1,4,1,7571,100,1,1,7,2,9,3),_IntegraWnetCfgIPgateway_Type())
integraWnetCfgIPgateway.setMaxAccess(_G)
if mibBuilder.loadTexts:integraWnetCfgIPgateway.setStatus(_A)
_IntegraWnetCfgRemoteIPaddress_Type=IpAddress
_IntegraWnetCfgRemoteIPaddress_Object=MibScalar
integraWnetCfgRemoteIPaddress=_IntegraWnetCfgRemoteIPaddress_Object((1,3,6,1,4,1,7571,100,1,1,7,2,9,4),_IntegraWnetCfgRemoteIPaddress_Type())
integraWnetCfgRemoteIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:integraWnetCfgRemoteIPaddress.setStatus(_A)
_IntegraWConformance_ObjectIdentity=ObjectIdentity
integraWConformance=_IntegraWConformance_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,10))
_IntegraWCompliances_ObjectIdentity=ObjectIdentity
integraWCompliances=_IntegraWCompliances_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,10,1))
_IntegraWGroups_ObjectIdentity=ObjectIdentity
integraWGroups=_IntegraWGroups_ObjectIdentity((1,3,6,1,4,1,7571,100,1,1,7,2,10,2))
integraWMiscGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,1))
integraWMiscGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:integraWMiscGroup.setStatus(_A)
integraWRadioGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,2))
integraWRadioGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_O),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:integraWRadioGroup.setStatus(_A)
integraWModemGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,3))
integraWModemGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:integraWModemGroup.setStatus(_A)
integraWSystemGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,4))
integraWSystemGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:integraWSystemGroup.setStatus(_A)
integraWEthernetGeneralGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,5))
integraWEthernetGeneralGroup.setObjects(*((_B,_P),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_Q),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:integraWEthernetGeneralGroup.setStatus(_A)
integraWEthernetMiiPortGroup=ObjectGroup((1,3,6,1,4,1,7571,100,1,1,7,2,10,2,6))
integraWEthernetMiiPortGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA)))
if mibBuilder.loadTexts:integraWEthernetMiiPortGroup.setStatus(_A)
integraWCompliance=ModuleCompliance((1,3,6,1,4,1,7571,100,1,1,7,2,10,1,1))
integraWCompliance.setObjects(*((_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG)))
if mibBuilder.loadTexts:integraWCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'integraW':integraW,_R:integraWtimestamp,'integraWradio':integraWradio,_S:integraWradioTxPower,_T:integraWradioTxFrequency,_U:integraWradioRxLevel,_V:integraWradioSide,_W:integraWradioTxMute,_X:integraWradioDuplexShift,_Y:integraWradioRxFrequency,_Z:integraWradioTemperature,_a:integraWradioTxMuteDuration,'integraWradioRangesTable':integraWradioRangesTable,'integraWradioRangeEntry':integraWradioRangeEntry,_O:integraWradioRangeEntryIndex,_b:integraWradioRangeDescr,_c:integraWradioRangeTxPower,_d:integraWradioRangeTxFrequency,_e:integraWradioPLL,'integraWradioRxLevelState':integraWradioRxLevelState,'integraWmodem':integraWmodem,_f:integraWmodemAcquireStatus,_g:integraWmodemMse,_h:integraWmodemFecLoad,_i:integraWmodemSyncLoss,_j:integraWmodemBandwidth,_k:integraWmodemModulation,_l:integraWmodemRxModulation,_m:integraWmodemTxModulation,_n:integraWmodemRxCapacity,_o:integraWmodemTxCapacity,_p:integraWmodemAcmEngine,_q:integraWmodemSignalQuality,'integraWsystem':integraWsystem,_r:integraWsysCPUtemperature,_s:integraWsysLicenseExpire,_t:integraWsysLicenseGenStatus,_u:integraWsysPSUvoltage,_v:integraWsysPSUcurrent,_w:integraWsysPSUpower,_x:integraWsysBoardTemperature,_y:integraWsysFreeMemory,_z:integraWsysCPUidle,'integraWethernet':integraWethernet,'integraWifStatusTable':integraWifStatusTable,'integraWifPortEntry':integraWifPortEntry,_P:integraWifPortStatIndex,_A3:integraWifPortStatDescr,_A4:integraWifPortType,_A5:integraWifPortMtu,_A6:integraWifPortSpeed,_A7:integraWifPortPhysAddress,_A8:integraWifPortAdminStatus,_A9:integraWifPortOperStatus,_AA:integraWifPortLastChange,_AB:integraWifPortAutoneg,_AC:integraWifPortDuplex,_AD:integraWifPortSyncEthActive,_AE:integraWifPortSyncEthPrio,_AF:integraWifPortFlowControl,'integraWifStatisticsTable':integraWifStatisticsTable,'integraWifPortStcEntry':integraWifPortStcEntry,_Q:integraWifPortStcIndex,_AG:integraWifPortStcDescr,_AH:integraWifTimePassed,_AM:integraWrxDetected,_AN:integraWrxDropped,_AO:integraWtxDetected,_AP:integraWtxDropped,_AQ:integraWrxBytes,_AR:integraWtxBytes,_AS:integraWrx64Frames,_AT:integraWrx65to127Frames,_AU:integraWrx128to255Frames,_AV:integraWrx256to511Frames,_AW:integraWrx512to1023Frames,_AX:integraWrx1024toMaxFrames,_AY:integraWrxUsizeFrames,_AZ:integraWrxOsizeFrames,_Aa:integraWtx64Frames,_Ab:integraWtx65to127Frames,_Ac:integraWtx128to255Frames,_Ad:integraWtx256to511Frames,_Ae:integraWtx512to1023Frames,_Af:integraWtx1024toMaxFrames,_Ag:integraWtxUsizeFrames,_Ah:integraWtxOsizeFrames,_Ai:integraWrxGoodFrames,_Aj:integraWrxErrors,_Ak:integraWrxFifoErr,_Al:integraWrxCRCErrors,_Am:integraWrxBcastFrames,_An:integraWrxMcastFrames,_Ao:integraWrxCntrlFrames,_Ap:integraWrxLenErrors,_Aq:integraWrxVlanFrames,_Ar:integraWrxPauseFrames,_As:integraWrxOpErrors,_At:integraWrxFrameErrors,_Au:integraWtxGoodFrames,_Av:integraWtxErrors,_Aw:integraWtxFifoErr,_Ax:integraWtxBcastFrames,_Ay:integraWtxMcastFrames,_Az:integraWtxUrunErrors,_A_:integraWtxCntrlFrames,_B0:integraWtxVlanFrames,_B1:integraWtxPauseFrames,_B2:integraWtxSingleCollisions,_B3:integraWtxMultiCollisions,_B4:integraWtxDeferred,_B5:integraWtxLateCollisions,_B6:integraWtxExcessCollisions,_B7:integraWtxExcessDeferral,_B8:integraWtxAlignErrors,_B9:integraWtxCarrierErrors,_BA:integraWtxCollisions,_A0:integraWexecuteConfig,_A1:integraWneedStore,_A2:integraWstoreConfig,'integraWnetCfg':integraWnetCfg,_AI:integraWnetCfgIPaddress,_AJ:integraWnetCfgIPmask,_AK:integraWnetCfgIPgateway,_AL:integraWnetCfgRemoteIPaddress,'integraWConformance':integraWConformance,'integraWCompliances':integraWCompliances,'integraWCompliance':integraWCompliance,'integraWGroups':integraWGroups,_BB:integraWMiscGroup,_BC:integraWRadioGroup,_BD:integraWModemGroup,_BE:integraWSystemGroup,_BF:integraWEthernetGeneralGroup,_BG:integraWEthernetMiiPortGroup})