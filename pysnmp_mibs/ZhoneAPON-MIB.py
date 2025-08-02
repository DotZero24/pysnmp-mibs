_Ad='zhoneOltLineStatusChangeTrap'
_Ac='zhoneOnuStatusLastChange'
_Ab='zhoneOltTrafficContainerGuaranteedBW'
_Aa='zhoneOltTrafficContainerRowStatus'
_AZ='zhoneOltTrafficContainerCbrCompensate'
_AY='zhoneOltTrafficContainerIndexNext'
_AX='zhoneOltTrafficContainerCBR'
_AW='zhoneOltTrafficContainerMaximumBW'
_AV='zhoneOnuStatusOperStatus'
_AU='zhoneOnuStatusAlarmMIS'
_AT='zhoneOnuStatusAlarmDIS'
_AS='zhoneOnuStatusAlarmDACT'
_AR='zhoneOnuStatusAlarmMEM'
_AQ='zhoneOnuStatusAlarmSD'
_AP='zhoneOnuStatusAlarmERR'
_AO='zhoneOnuStatusAlarmFRML'
_AN='zhoneOnuStatusAlarmLCD'
_AM='zhoneOnuStatusAlarmOAML'
_AL='zhoneOnuStatusAlarmSUF'
_AK='zhoneOnuStatusAlarmPEE'
_AJ='zhoneOnuStatusAlarmLOS'
_AI='zhoneOnuStatusAlarmTF'
_AH='zhoneOnuStatusLoopback'
_AG='zhoneOnuConfigOverheadSize'
_AF='zhoneOnuConfigLoopback'
_AE='zhoneOnuConfigHEC'
_AD='zhoneOnuConfigNetworkRefClk'
_AC='zhoneOnuConfigPassword'
_AB='zhoneOnuConfigSerialNumber'
_AA='zhoneOltOnuStatusPonAlarmRXINH'
_A9='zhoneOltOnuStatusPonAlarmMEM'
_A8='zhoneOltOnuStatusPonAlarmREI'
_A7='zhoneOltOnuStatusPonAlarmSD'
_A6='zhoneOltOnuStatusPonAlarmERR'
_A5='zhoneOltOnuStatusPonAlarmLOA'
_A4='zhoneOltOnuConfigLineStatusChangeTrapEnable'
_A3='zhoneOltOnuConfigChurnkey'
_A2='zhoneOltOnuConfigSerialNum'
_A1='zhoneOltOnuConfigPassword'
_A0='zhoneOltStatusPonAlarmCPE'
_z='zhoneOltStatusPonAlarmOAML'
_y='zhoneOltStatusPonAlarmLOS'
_x='zhoneOltStatusPonAlarmLCD'
_w='zhoneOltStatusPonAlarmPEE'
_v='zhoneOltStatusPonAlarmSUF'
_u='zhoneOltStatusPonAlarmTF'
_t='zhoneOltStatusPonAlarmLPHY'
_s='zhoneOltStatusLoopback'
_r='zhoneOltStatusState'
_q='zhoneOltConfigMaxPonDistance'
_p='zhoneOltConfigTxSyncBytes'
_o='zhoneOltConfigSyncBytesClkDivisor'
_n='zhoneOltConfigAutoLearn'
_m='zhoneOltConfigLoopback'
_l='zhoneOltConfigLineStatusChangeTrapEnable'
_k='zhoneOltConfigUtopiaDiscard'
_j='zhoneOltConfigTxDiscardNonMatchingVpi'
_i='zhoneOltConfigLcdDelta'
_h='zhoneOltConfigLcdAlpha'
_g='zhoneOltConfigLcdLimit'
_f='zhoneOltConfigCpeLimit'
_e='zhoneOltConfigCdrActiveHigh'
_d='zhoneOltConfigCdrLocation'
_c='zhoneOltConfigCdrPattern'
_b='zhoneOltConfigDelimiterSize'
_a='zhoneOltConfigDelimiterPattern'
_Z='zhoneOltConfigOverheadSize'
_Y='zhoneOltConfigCrcRx'
_X='zhoneOltConfigHecRxBypass'
_W='zhoneOltConfigHec'
_V='zhoneOltConfigBip8'
_U='zhoneOltConfigCellScrambling'
_T='zhoneOltTrafficContainerIndex'
_S='onuLine'
_R='onuInward'
_Q='onuNone'
_P='ZhoneAdminString'
_O='zhoneOltStatusLastChange'
_N='disabled'
_M='enabled'
_L='TimeStamp'
_K='Unsigned32'
_J='ifAlias'
_I='read-create'
_H='ifIndex'
_G='TruthValue'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ZhoneAPON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAlias,ifCompliance,ifCompliance2,ifConnectorPresent,ifCounterDiscontinuityGroup,ifCounterDiscontinuityTime,ifFixedLengthGroup,ifGeneralGroup,ifGeneralInformationGroup,ifHCFixedLengthGroup,ifHCInBroadcastPkts,ifHCInMulticastPkts,ifHCInOctets,ifHCInUcastPkts,ifHCOutBroadcastPkts,ifHCOutMulticastPkts,ifHCOutOctets,ifHCOutUcastPkts,ifHCPacketGroup,ifHighSpeed,ifInBroadcastPkts,ifInMulticastPkts,ifIndex,ifLinkUpDownTrapEnable,ifName,ifNumber,ifOldObjectsGroup,ifOutBroadcastPkts,ifOutMulticastPkts,ifPacketGroup,ifPromiscuousMode,ifRcvAddressAddress,ifRcvAddressGroup,ifRcvAddressStatus,ifRcvAddressType,ifStackGroup,ifStackGroup2,ifStackHigherLayer,ifStackLastChange,ifStackLowerLayer,ifStackStatus,ifTableLastChange,ifTestCode,ifTestGroup,ifTestId,ifTestOwner,ifTestResult,ifTestStatus,ifTestType,ifVHCPacketGroup=mibBuilder.importSymbols(_F,_J,'ifCompliance','ifCompliance2','ifConnectorPresent','ifCounterDiscontinuityGroup','ifCounterDiscontinuityTime','ifFixedLengthGroup','ifGeneralGroup','ifGeneralInformationGroup','ifHCFixedLengthGroup','ifHCInBroadcastPkts','ifHCInMulticastPkts','ifHCInOctets','ifHCInUcastPkts','ifHCOutBroadcastPkts','ifHCOutMulticastPkts','ifHCOutOctets','ifHCOutUcastPkts','ifHCPacketGroup','ifHighSpeed','ifInBroadcastPkts','ifInMulticastPkts',_H,'ifLinkUpDownTrapEnable','ifName','ifNumber','ifOldObjectsGroup','ifOutBroadcastPkts','ifOutMulticastPkts','ifPacketGroup','ifPromiscuousMode','ifRcvAddressAddress','ifRcvAddressGroup','ifRcvAddressStatus','ifRcvAddressType','ifStackGroup','ifStackGroup2','ifStackHigherLayer','ifStackLastChange','ifStackLowerLayer','ifStackStatus','ifTableLastChange','ifTestCode','ifTestGroup','ifTestId','ifTestOwner','ifTestResult','ifTestStatus','ifTestType','ifVHCPacketGroup')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L,_G)
apsMIB,sechtor100,sechtor300,sipCommonMIB,sipTC,sipUAMIB,zhoneAtm,zhoneBridge,zhoneCard,zhoneConsole,zhoneDrafts,zhoneDs3Ext,zhoneDsl,zhoneDsx,zhoneEnet,zhoneGenWtn,zhoneGroups,zhoneIma,zhoneInterfaceGroup,zhoneInterfaceTranslation,zhoneIp,zhoneLineTypes,zhoneMalc,zhoneMasterAgent,zhoneModules,zhoneOcx,zhonePhysical,zhonePls,zhonePpp,zhoneRadio,zhoneRegCpe,zhoneRegMalc,zhoneRegMux,zhoneRegPls,zhoneRegSechtor,zhoneRegWtn,zhoneShelf,zhoneShelfIndex,zhoneShelfSlotCompliance,zhoneShelfSlotGroup,zhoneSlotIndex,zhoneSonet,zhoneSubscriber,zhoneSystem,zhoneTrapModules,zhoneVoice,zhoneVoiceStats,zhoneVoip,zhoneWtn,zhoneZAP,zhoneZedge,zhoneZmsProduct,zhoneZplex=mibBuilder.importSymbols('Zhone','apsMIB','sechtor100','sechtor300','sipCommonMIB','sipTC','sipUAMIB','zhoneAtm','zhoneBridge','zhoneCard','zhoneConsole','zhoneDrafts','zhoneDs3Ext','zhoneDsl','zhoneDsx','zhoneEnet','zhoneGenWtn','zhoneGroups','zhoneIma','zhoneInterfaceGroup','zhoneInterfaceTranslation','zhoneIp','zhoneLineTypes','zhoneMalc','zhoneMasterAgent','zhoneModules','zhoneOcx','zhonePhysical','zhonePls','zhonePpp','zhoneRadio','zhoneRegCpe','zhoneRegMalc','zhoneRegMux','zhoneRegPls','zhoneRegSechtor','zhoneRegWtn','zhoneShelf','zhoneShelfIndex','zhoneShelfSlotCompliance','zhoneShelfSlotGroup','zhoneSlotIndex','zhoneSonet','zhoneSubscriber','zhoneSystem','zhoneTrapModules','zhoneVoice','zhoneVoiceStats','zhoneVoip','zhoneWtn','zhoneZAP','zhoneZedge','zhoneZmsProduct','zhoneZplex')
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC',_P,'ZhoneRowStatus')
zhoneAponMIB=ModuleIdentity((1,3,6,1,4,1,5504,5,12,1))
if mibBuilder.loadTexts:zhoneAponMIB.setRevisions(('2006-04-25 11:03','2005-04-18 14:42','2004-06-09 11:56','2004-03-25 16:27','2003-12-08 15:29','2003-11-19 12:49','2003-08-18 15:59','2003-08-12 11:25','2003-08-05 10:12'))
_ZhoneApon_ObjectIdentity=ObjectIdentity
zhoneApon=_ZhoneApon_ObjectIdentity((1,3,6,1,4,1,5504,5,12))
if mibBuilder.loadTexts:zhoneApon.setStatus(_A)
_ZhoneOltConfigTable_Object=MibTable
zhoneOltConfigTable=_ZhoneOltConfigTable_Object((1,3,6,1,4,1,5504,5,12,1,2))
if mibBuilder.loadTexts:zhoneOltConfigTable.setStatus(_A)
_ZhoneOltConfigEntry_Object=MibTableRow
zhoneOltConfigEntry=_ZhoneOltConfigEntry_Object((1,3,6,1,4,1,5504,5,12,1,2,1))
zhoneOltConfigEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOltConfigEntry.setStatus(_A)
class _ZhoneOltConfigAutoLearn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oltAutolearnEnable',1),('oltAutolearnDisable',2)))
_ZhoneOltConfigAutoLearn_Type.__name__=_D
_ZhoneOltConfigAutoLearn_Object=MibTableColumn
zhoneOltConfigAutoLearn=_ZhoneOltConfigAutoLearn_Object((1,3,6,1,4,1,5504,5,12,1,2,1,1),_ZhoneOltConfigAutoLearn_Type())
zhoneOltConfigAutoLearn.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigAutoLearn.setStatus(_A)
class _ZhoneOltConfigCellScrambling_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oltCellScramblingOff',1),('oltCellScramblingRxOnly',2),('oltCellScramblingTxOnly',3),('oltCellScramblingRxAndTx',4)))
_ZhoneOltConfigCellScrambling_Type.__name__=_D
_ZhoneOltConfigCellScrambling_Object=MibTableColumn
zhoneOltConfigCellScrambling=_ZhoneOltConfigCellScrambling_Object((1,3,6,1,4,1,5504,5,12,1,2,1,2),_ZhoneOltConfigCellScrambling_Type())
zhoneOltConfigCellScrambling.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCellScrambling.setStatus(_A)
class _ZhoneOltConfigBip8_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oltBip8Off',1),('oltBip8RxCorrectionOnly',2),('oltBip8TxGenerationOnly',3),('oltBip8RxAndTx',4)))
_ZhoneOltConfigBip8_Type.__name__=_D
_ZhoneOltConfigBip8_Object=MibTableColumn
zhoneOltConfigBip8=_ZhoneOltConfigBip8_Object((1,3,6,1,4,1,5504,5,12,1,2,1,3),_ZhoneOltConfigBip8_Type())
zhoneOltConfigBip8.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigBip8.setStatus(_A)
class _ZhoneOltConfigHec_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oltHecOff',1),('oltHecRxCorrectionOnly',2),('oltHecTxGenerationOnly',3),('oltHecRxAndTx',4)))
_ZhoneOltConfigHec_Type.__name__=_D
_ZhoneOltConfigHec_Object=MibTableColumn
zhoneOltConfigHec=_ZhoneOltConfigHec_Object((1,3,6,1,4,1,5504,5,12,1,2,1,4),_ZhoneOltConfigHec_Type())
zhoneOltConfigHec.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigHec.setStatus(_A)
class _ZhoneOltConfigHecRxBypass_Type(TruthValue):defaultValue=2
_ZhoneOltConfigHecRxBypass_Type.__name__=_G
_ZhoneOltConfigHecRxBypass_Object=MibTableColumn
zhoneOltConfigHecRxBypass=_ZhoneOltConfigHecRxBypass_Object((1,3,6,1,4,1,5504,5,12,1,2,1,5),_ZhoneOltConfigHecRxBypass_Type())
zhoneOltConfigHecRxBypass.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigHecRxBypass.setStatus(_A)
class _ZhoneOltConfigCrcRx_Type(TruthValue):defaultValue=1
_ZhoneOltConfigCrcRx_Type.__name__=_G
_ZhoneOltConfigCrcRx_Object=MibTableColumn
zhoneOltConfigCrcRx=_ZhoneOltConfigCrcRx_Object((1,3,6,1,4,1,5504,5,12,1,2,1,6),_ZhoneOltConfigCrcRx_Type())
zhoneOltConfigCrcRx.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCrcRx.setStatus(_A)
class _ZhoneOltConfigOverheadSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oltPonOverhead3Bytes',1),('oltPonOverhead6Bytes',2),('oltPonOverhead12Bytes',3)))
_ZhoneOltConfigOverheadSize_Type.__name__=_D
_ZhoneOltConfigOverheadSize_Object=MibTableColumn
zhoneOltConfigOverheadSize=_ZhoneOltConfigOverheadSize_Object((1,3,6,1,4,1,5504,5,12,1,2,1,7),_ZhoneOltConfigOverheadSize_Type())
zhoneOltConfigOverheadSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigOverheadSize.setStatus(_A)
class _ZhoneOltConfigDelimiterPattern_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneOltConfigDelimiterPattern_Type.__name__=_D
_ZhoneOltConfigDelimiterPattern_Object=MibTableColumn
zhoneOltConfigDelimiterPattern=_ZhoneOltConfigDelimiterPattern_Object((1,3,6,1,4,1,5504,5,12,1,2,1,8),_ZhoneOltConfigDelimiterPattern_Type())
zhoneOltConfigDelimiterPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigDelimiterPattern.setStatus(_A)
class _ZhoneOltConfigDelimiterSize_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,16))
_ZhoneOltConfigDelimiterSize_Type.__name__=_D
_ZhoneOltConfigDelimiterSize_Object=MibTableColumn
zhoneOltConfigDelimiterSize=_ZhoneOltConfigDelimiterSize_Object((1,3,6,1,4,1,5504,5,12,1,2,1,9),_ZhoneOltConfigDelimiterSize_Type())
zhoneOltConfigDelimiterSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigDelimiterSize.setStatus(_A)
if mibBuilder.loadTexts:zhoneOltConfigDelimiterSize.setUnits('Number of bits')
class _ZhoneOltConfigCdrPattern_Type(Integer32):defaultValue=192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneOltConfigCdrPattern_Type.__name__=_D
_ZhoneOltConfigCdrPattern_Object=MibTableColumn
zhoneOltConfigCdrPattern=_ZhoneOltConfigCdrPattern_Object((1,3,6,1,4,1,5504,5,12,1,2,1,10),_ZhoneOltConfigCdrPattern_Type())
zhoneOltConfigCdrPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCdrPattern.setStatus(_A)
class _ZhoneOltConfigCdrLocation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_ZhoneOltConfigCdrLocation_Type.__name__=_D
_ZhoneOltConfigCdrLocation_Object=MibTableColumn
zhoneOltConfigCdrLocation=_ZhoneOltConfigCdrLocation_Object((1,3,6,1,4,1,5504,5,12,1,2,1,11),_ZhoneOltConfigCdrLocation_Type())
zhoneOltConfigCdrLocation.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCdrLocation.setStatus(_A)
class _ZhoneOltConfigCdrActiveHigh_Type(TruthValue):defaultValue=2
_ZhoneOltConfigCdrActiveHigh_Type.__name__=_G
_ZhoneOltConfigCdrActiveHigh_Object=MibTableColumn
zhoneOltConfigCdrActiveHigh=_ZhoneOltConfigCdrActiveHigh_Object((1,3,6,1,4,1,5504,5,12,1,2,1,12),_ZhoneOltConfigCdrActiveHigh_Type())
zhoneOltConfigCdrActiveHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCdrActiveHigh.setStatus(_A)
class _ZhoneOltConfigCpeLimit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ZhoneOltConfigCpeLimit_Type.__name__=_D
_ZhoneOltConfigCpeLimit_Object=MibTableColumn
zhoneOltConfigCpeLimit=_ZhoneOltConfigCpeLimit_Object((1,3,6,1,4,1,5504,5,12,1,2,1,13),_ZhoneOltConfigCpeLimit_Type())
zhoneOltConfigCpeLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigCpeLimit.setStatus(_A)
class _ZhoneOltConfigLcdLimit_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_ZhoneOltConfigLcdLimit_Type.__name__=_D
_ZhoneOltConfigLcdLimit_Object=MibTableColumn
zhoneOltConfigLcdLimit=_ZhoneOltConfigLcdLimit_Object((1,3,6,1,4,1,5504,5,12,1,2,1,14),_ZhoneOltConfigLcdLimit_Type())
zhoneOltConfigLcdLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigLcdLimit.setStatus(_A)
class _ZhoneOltConfigLcdAlpha_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZhoneOltConfigLcdAlpha_Type.__name__=_D
_ZhoneOltConfigLcdAlpha_Object=MibTableColumn
zhoneOltConfigLcdAlpha=_ZhoneOltConfigLcdAlpha_Object((1,3,6,1,4,1,5504,5,12,1,2,1,15),_ZhoneOltConfigLcdAlpha_Type())
zhoneOltConfigLcdAlpha.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigLcdAlpha.setStatus(_A)
class _ZhoneOltConfigLcdDelta_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZhoneOltConfigLcdDelta_Type.__name__=_D
_ZhoneOltConfigLcdDelta_Object=MibTableColumn
zhoneOltConfigLcdDelta=_ZhoneOltConfigLcdDelta_Object((1,3,6,1,4,1,5504,5,12,1,2,1,16),_ZhoneOltConfigLcdDelta_Type())
zhoneOltConfigLcdDelta.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigLcdDelta.setStatus(_A)
class _ZhoneOltConfigTxDiscardNonMatchingVpi_Type(TruthValue):defaultValue=2
_ZhoneOltConfigTxDiscardNonMatchingVpi_Type.__name__=_G
_ZhoneOltConfigTxDiscardNonMatchingVpi_Object=MibTableColumn
zhoneOltConfigTxDiscardNonMatchingVpi=_ZhoneOltConfigTxDiscardNonMatchingVpi_Object((1,3,6,1,4,1,5504,5,12,1,2,1,17),_ZhoneOltConfigTxDiscardNonMatchingVpi_Type())
zhoneOltConfigTxDiscardNonMatchingVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigTxDiscardNonMatchingVpi.setStatus(_A)
class _ZhoneOltConfigUtopiaDiscard_Type(TruthValue):defaultValue=2
_ZhoneOltConfigUtopiaDiscard_Type.__name__=_G
_ZhoneOltConfigUtopiaDiscard_Object=MibTableColumn
zhoneOltConfigUtopiaDiscard=_ZhoneOltConfigUtopiaDiscard_Object((1,3,6,1,4,1,5504,5,12,1,2,1,18),_ZhoneOltConfigUtopiaDiscard_Type())
zhoneOltConfigUtopiaDiscard.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigUtopiaDiscard.setStatus(_A)
class _ZhoneOltConfigSyncBytesClkDivisor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneOltConfigSyncBytesClkDivisor_Type.__name__=_D
_ZhoneOltConfigSyncBytesClkDivisor_Object=MibTableColumn
zhoneOltConfigSyncBytesClkDivisor=_ZhoneOltConfigSyncBytesClkDivisor_Object((1,3,6,1,4,1,5504,5,12,1,2,1,19),_ZhoneOltConfigSyncBytesClkDivisor_Type())
zhoneOltConfigSyncBytesClkDivisor.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigSyncBytesClkDivisor.setStatus(_A)
class _ZhoneOltConfigTxSyncBytes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('txSyncBytesEnable',1),('txSyncBytesDisable',2)))
_ZhoneOltConfigTxSyncBytes_Type.__name__=_D
_ZhoneOltConfigTxSyncBytes_Object=MibTableColumn
zhoneOltConfigTxSyncBytes=_ZhoneOltConfigTxSyncBytes_Object((1,3,6,1,4,1,5504,5,12,1,2,1,20),_ZhoneOltConfigTxSyncBytes_Type())
zhoneOltConfigTxSyncBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigTxSyncBytes.setStatus(_A)
class _ZhoneOltConfigLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopbackNone',1),('loopbackInward',2),('loopbackLine',3)))
_ZhoneOltConfigLoopback_Type.__name__=_D
_ZhoneOltConfigLoopback_Object=MibTableColumn
zhoneOltConfigLoopback=_ZhoneOltConfigLoopback_Object((1,3,6,1,4,1,5504,5,12,1,2,1,21),_ZhoneOltConfigLoopback_Type())
zhoneOltConfigLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigLoopback.setStatus(_A)
class _ZhoneOltConfigMaxPonDistance_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhoneOltConfigMaxPonDistance_Type.__name__=_D
_ZhoneOltConfigMaxPonDistance_Object=MibTableColumn
zhoneOltConfigMaxPonDistance=_ZhoneOltConfigMaxPonDistance_Object((1,3,6,1,4,1,5504,5,12,1,2,1,22),_ZhoneOltConfigMaxPonDistance_Type())
zhoneOltConfigMaxPonDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigMaxPonDistance.setStatus(_A)
if mibBuilder.loadTexts:zhoneOltConfigMaxPonDistance.setUnits('Distance in microseconds, used in the ranging process.')
class _ZhoneOltConfigLineStatusChangeTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZhoneOltConfigLineStatusChangeTrapEnable_Type.__name__=_D
_ZhoneOltConfigLineStatusChangeTrapEnable_Object=MibTableColumn
zhoneOltConfigLineStatusChangeTrapEnable=_ZhoneOltConfigLineStatusChangeTrapEnable_Object((1,3,6,1,4,1,5504,5,12,1,2,1,23),_ZhoneOltConfigLineStatusChangeTrapEnable_Type())
zhoneOltConfigLineStatusChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltConfigLineStatusChangeTrapEnable.setStatus(_A)
_ZhoneOltStatusTable_Object=MibTable
zhoneOltStatusTable=_ZhoneOltStatusTable_Object((1,3,6,1,4,1,5504,5,12,1,3))
if mibBuilder.loadTexts:zhoneOltStatusTable.setStatus(_A)
_ZhoneOltStatusEntry_Object=MibTableRow
zhoneOltStatusEntry=_ZhoneOltStatusEntry_Object((1,3,6,1,4,1,5504,5,12,1,3,1))
zhoneOltStatusEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOltStatusEntry.setStatus(_A)
class _ZhoneOltStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oltStateDown',1),('oltStateUp',2)))
_ZhoneOltStatusState_Type.__name__=_D
_ZhoneOltStatusState_Object=MibTableColumn
zhoneOltStatusState=_ZhoneOltStatusState_Object((1,3,6,1,4,1,5504,5,12,1,3,1,1),_ZhoneOltStatusState_Type())
zhoneOltStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusState.setStatus(_A)
class _ZhoneOltStatusLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oltLoopbackNone',1),('oltLoopbackInward',2),('oltLoopbackLine',3)))
_ZhoneOltStatusLoopback_Type.__name__=_D
_ZhoneOltStatusLoopback_Object=MibTableColumn
zhoneOltStatusLoopback=_ZhoneOltStatusLoopback_Object((1,3,6,1,4,1,5504,5,12,1,3,1,2),_ZhoneOltStatusLoopback_Type())
zhoneOltStatusLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusLoopback.setStatus(_A)
_ZhoneOltStatusPonAlarmLPHY_Type=TruthValue
_ZhoneOltStatusPonAlarmLPHY_Object=MibTableColumn
zhoneOltStatusPonAlarmLPHY=_ZhoneOltStatusPonAlarmLPHY_Object((1,3,6,1,4,1,5504,5,12,1,3,1,3),_ZhoneOltStatusPonAlarmLPHY_Type())
zhoneOltStatusPonAlarmLPHY.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmLPHY.setStatus(_A)
_ZhoneOltStatusPonAlarmTF_Type=TruthValue
_ZhoneOltStatusPonAlarmTF_Object=MibTableColumn
zhoneOltStatusPonAlarmTF=_ZhoneOltStatusPonAlarmTF_Object((1,3,6,1,4,1,5504,5,12,1,3,1,4),_ZhoneOltStatusPonAlarmTF_Type())
zhoneOltStatusPonAlarmTF.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmTF.setStatus(_A)
_ZhoneOltStatusPonAlarmSUF_Type=TruthValue
_ZhoneOltStatusPonAlarmSUF_Object=MibTableColumn
zhoneOltStatusPonAlarmSUF=_ZhoneOltStatusPonAlarmSUF_Object((1,3,6,1,4,1,5504,5,12,1,3,1,5),_ZhoneOltStatusPonAlarmSUF_Type())
zhoneOltStatusPonAlarmSUF.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmSUF.setStatus(_A)
_ZhoneOltStatusPonAlarmPEE_Type=TruthValue
_ZhoneOltStatusPonAlarmPEE_Object=MibTableColumn
zhoneOltStatusPonAlarmPEE=_ZhoneOltStatusPonAlarmPEE_Object((1,3,6,1,4,1,5504,5,12,1,3,1,6),_ZhoneOltStatusPonAlarmPEE_Type())
zhoneOltStatusPonAlarmPEE.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmPEE.setStatus(_A)
_ZhoneOltStatusPonAlarmLCD_Type=TruthValue
_ZhoneOltStatusPonAlarmLCD_Object=MibTableColumn
zhoneOltStatusPonAlarmLCD=_ZhoneOltStatusPonAlarmLCD_Object((1,3,6,1,4,1,5504,5,12,1,3,1,7),_ZhoneOltStatusPonAlarmLCD_Type())
zhoneOltStatusPonAlarmLCD.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmLCD.setStatus(_A)
_ZhoneOltStatusPonAlarmLOS_Type=TruthValue
_ZhoneOltStatusPonAlarmLOS_Object=MibTableColumn
zhoneOltStatusPonAlarmLOS=_ZhoneOltStatusPonAlarmLOS_Object((1,3,6,1,4,1,5504,5,12,1,3,1,8),_ZhoneOltStatusPonAlarmLOS_Type())
zhoneOltStatusPonAlarmLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmLOS.setStatus(_A)
_ZhoneOltStatusPonAlarmOAML_Type=TruthValue
_ZhoneOltStatusPonAlarmOAML_Object=MibTableColumn
zhoneOltStatusPonAlarmOAML=_ZhoneOltStatusPonAlarmOAML_Object((1,3,6,1,4,1,5504,5,12,1,3,1,9),_ZhoneOltStatusPonAlarmOAML_Type())
zhoneOltStatusPonAlarmOAML.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmOAML.setStatus(_A)
_ZhoneOltStatusPonAlarmCPE_Type=TruthValue
_ZhoneOltStatusPonAlarmCPE_Object=MibTableColumn
zhoneOltStatusPonAlarmCPE=_ZhoneOltStatusPonAlarmCPE_Object((1,3,6,1,4,1,5504,5,12,1,3,1,10),_ZhoneOltStatusPonAlarmCPE_Type())
zhoneOltStatusPonAlarmCPE.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusPonAlarmCPE.setStatus(_A)
class _ZhoneOltStatusLastChange_Type(TimeStamp):defaultValue=0
_ZhoneOltStatusLastChange_Type.__name__=_L
_ZhoneOltStatusLastChange_Object=MibTableColumn
zhoneOltStatusLastChange=_ZhoneOltStatusLastChange_Object((1,3,6,1,4,1,5504,5,12,1,3,1,11),_ZhoneOltStatusLastChange_Type())
zhoneOltStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltStatusLastChange.setStatus(_A)
_ZhoneOltOnuConfigTable_Object=MibTable
zhoneOltOnuConfigTable=_ZhoneOltOnuConfigTable_Object((1,3,6,1,4,1,5504,5,12,1,4))
if mibBuilder.loadTexts:zhoneOltOnuConfigTable.setStatus(_A)
_ZhoneOltOnuConfigEntry_Object=MibTableRow
zhoneOltOnuConfigEntry=_ZhoneOltOnuConfigEntry_Object((1,3,6,1,4,1,5504,5,12,1,4,1))
zhoneOltOnuConfigEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOltOnuConfigEntry.setStatus(_A)
class _ZhoneOltOnuConfigPassword_Type(ZhoneAdminString):subtypeSpec=ZhoneAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ZhoneOltOnuConfigPassword_Type.__name__=_P
_ZhoneOltOnuConfigPassword_Object=MibTableColumn
zhoneOltOnuConfigPassword=_ZhoneOltOnuConfigPassword_Object((1,3,6,1,4,1,5504,5,12,1,4,1,1),_ZhoneOltOnuConfigPassword_Type())
zhoneOltOnuConfigPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltOnuConfigPassword.setStatus(_A)
class _ZhoneOltOnuConfigSerialNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneOltOnuConfigSerialNum_Type.__name__=_D
_ZhoneOltOnuConfigSerialNum_Object=MibTableColumn
zhoneOltOnuConfigSerialNum=_ZhoneOltOnuConfigSerialNum_Object((1,3,6,1,4,1,5504,5,12,1,4,1,2),_ZhoneOltOnuConfigSerialNum_Type())
zhoneOltOnuConfigSerialNum.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltOnuConfigSerialNum.setStatus(_A)
class _ZhoneOltOnuConfigChurnkey_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onuChurnkeyEnable',1),('onuChurnkeyDisable',2)))
_ZhoneOltOnuConfigChurnkey_Type.__name__=_D
_ZhoneOltOnuConfigChurnkey_Object=MibTableColumn
zhoneOltOnuConfigChurnkey=_ZhoneOltOnuConfigChurnkey_Object((1,3,6,1,4,1,5504,5,12,1,4,1,3),_ZhoneOltOnuConfigChurnkey_Type())
zhoneOltOnuConfigChurnkey.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltOnuConfigChurnkey.setStatus(_A)
class _ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type.__name__=_D
_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Object=MibTableColumn
zhoneOltOnuConfigLineStatusChangeTrapEnable=_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Object((1,3,6,1,4,1,5504,5,12,1,4,1,4),_ZhoneOltOnuConfigLineStatusChangeTrapEnable_Type())
zhoneOltOnuConfigLineStatusChangeTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOltOnuConfigLineStatusChangeTrapEnable.setStatus(_A)
_ZhoneOltOnuStatusTable_Object=MibTable
zhoneOltOnuStatusTable=_ZhoneOltOnuStatusTable_Object((1,3,6,1,4,1,5504,5,12,1,5))
if mibBuilder.loadTexts:zhoneOltOnuStatusTable.setStatus(_A)
_ZhoneOltOnuStatusEntry_Object=MibTableRow
zhoneOltOnuStatusEntry=_ZhoneOltOnuStatusEntry_Object((1,3,6,1,4,1,5504,5,12,1,5,1))
zhoneOltOnuStatusEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOltOnuStatusEntry.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmLOA_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmLOA_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmLOA=_ZhoneOltOnuStatusPonAlarmLOA_Object((1,3,6,1,4,1,5504,5,12,1,5,1,1),_ZhoneOltOnuStatusPonAlarmLOA_Type())
zhoneOltOnuStatusPonAlarmLOA.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmLOA.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmERR_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmERR_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmERR=_ZhoneOltOnuStatusPonAlarmERR_Object((1,3,6,1,4,1,5504,5,12,1,5,1,2),_ZhoneOltOnuStatusPonAlarmERR_Type())
zhoneOltOnuStatusPonAlarmERR.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmERR.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmSD_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmSD_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmSD=_ZhoneOltOnuStatusPonAlarmSD_Object((1,3,6,1,4,1,5504,5,12,1,5,1,3),_ZhoneOltOnuStatusPonAlarmSD_Type())
zhoneOltOnuStatusPonAlarmSD.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmSD.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmREI_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmREI_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmREI=_ZhoneOltOnuStatusPonAlarmREI_Object((1,3,6,1,4,1,5504,5,12,1,5,1,4),_ZhoneOltOnuStatusPonAlarmREI_Type())
zhoneOltOnuStatusPonAlarmREI.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmREI.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmMEM_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmMEM_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmMEM=_ZhoneOltOnuStatusPonAlarmMEM_Object((1,3,6,1,4,1,5504,5,12,1,5,1,5),_ZhoneOltOnuStatusPonAlarmMEM_Type())
zhoneOltOnuStatusPonAlarmMEM.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmMEM.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmRXINH_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmRXINH_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmRXINH=_ZhoneOltOnuStatusPonAlarmRXINH_Object((1,3,6,1,4,1,5504,5,12,1,5,1,6),_ZhoneOltOnuStatusPonAlarmRXINH_Type())
zhoneOltOnuStatusPonAlarmRXINH.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmRXINH.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmLOS_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmLOS_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmLOS=_ZhoneOltOnuStatusPonAlarmLOS_Object((1,3,6,1,4,1,5504,5,12,1,5,1,7),_ZhoneOltOnuStatusPonAlarmLOS_Type())
zhoneOltOnuStatusPonAlarmLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmLOS.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmPEE_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmPEE_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmPEE=_ZhoneOltOnuStatusPonAlarmPEE_Object((1,3,6,1,4,1,5504,5,12,1,5,1,8),_ZhoneOltOnuStatusPonAlarmPEE_Type())
zhoneOltOnuStatusPonAlarmPEE.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmPEE.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmSUF_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmSUF_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmSUF=_ZhoneOltOnuStatusPonAlarmSUF_Object((1,3,6,1,4,1,5504,5,12,1,5,1,9),_ZhoneOltOnuStatusPonAlarmSUF_Type())
zhoneOltOnuStatusPonAlarmSUF.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmSUF.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmOAML_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmOAML_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmOAML=_ZhoneOltOnuStatusPonAlarmOAML_Object((1,3,6,1,4,1,5504,5,12,1,5,1,10),_ZhoneOltOnuStatusPonAlarmOAML_Type())
zhoneOltOnuStatusPonAlarmOAML.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmOAML.setStatus(_A)
_ZhoneOltOnuStatusPonAlarmLCD_Type=TruthValue
_ZhoneOltOnuStatusPonAlarmLCD_Object=MibTableColumn
zhoneOltOnuStatusPonAlarmLCD=_ZhoneOltOnuStatusPonAlarmLCD_Object((1,3,6,1,4,1,5504,5,12,1,5,1,11),_ZhoneOltOnuStatusPonAlarmLCD_Type())
zhoneOltOnuStatusPonAlarmLCD.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltOnuStatusPonAlarmLCD.setStatus(_A)
_ZhoneOnuConfigTable_Object=MibTable
zhoneOnuConfigTable=_ZhoneOnuConfigTable_Object((1,3,6,1,4,1,5504,5,12,1,6))
if mibBuilder.loadTexts:zhoneOnuConfigTable.setStatus(_A)
_ZhoneOnuConfigEntry_Object=MibTableRow
zhoneOnuConfigEntry=_ZhoneOnuConfigEntry_Object((1,3,6,1,4,1,5504,5,12,1,6,1))
zhoneOnuConfigEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOnuConfigEntry.setStatus(_A)
class _ZhoneOnuConfigSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneOnuConfigSerialNumber_Type.__name__=_D
_ZhoneOnuConfigSerialNumber_Object=MibTableColumn
zhoneOnuConfigSerialNumber=_ZhoneOnuConfigSerialNumber_Object((1,3,6,1,4,1,5504,5,12,1,6,1,1),_ZhoneOnuConfigSerialNumber_Type())
zhoneOnuConfigSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuConfigSerialNumber.setStatus(_A)
_ZhoneOnuConfigPassword_Type=ZhoneAdminString
_ZhoneOnuConfigPassword_Object=MibTableColumn
zhoneOnuConfigPassword=_ZhoneOnuConfigPassword_Object((1,3,6,1,4,1,5504,5,12,1,6,1,2),_ZhoneOnuConfigPassword_Type())
zhoneOnuConfigPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigPassword.setStatus(_A)
class _ZhoneOnuConfigNetworkRefClk_Type(TruthValue):defaultValue=2
_ZhoneOnuConfigNetworkRefClk_Type.__name__=_G
_ZhoneOnuConfigNetworkRefClk_Object=MibTableColumn
zhoneOnuConfigNetworkRefClk=_ZhoneOnuConfigNetworkRefClk_Object((1,3,6,1,4,1,5504,5,12,1,6,1,3),_ZhoneOnuConfigNetworkRefClk_Type())
zhoneOnuConfigNetworkRefClk.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigNetworkRefClk.setStatus(_A)
class _ZhoneOnuConfigHEC_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onuOff',1),('onuRxCorrectionOnly',2),('onuTxGenerationOnly',3),('onuRxAndTx',4)))
_ZhoneOnuConfigHEC_Type.__name__=_D
_ZhoneOnuConfigHEC_Object=MibTableColumn
zhoneOnuConfigHEC=_ZhoneOnuConfigHEC_Object((1,3,6,1,4,1,5504,5,12,1,6,1,4),_ZhoneOnuConfigHEC_Type())
zhoneOnuConfigHEC.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigHEC.setStatus(_A)
class _ZhoneOnuConfigLoopback_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_ZhoneOnuConfigLoopback_Type.__name__=_D
_ZhoneOnuConfigLoopback_Object=MibTableColumn
zhoneOnuConfigLoopback=_ZhoneOnuConfigLoopback_Object((1,3,6,1,4,1,5504,5,12,1,6,1,5),_ZhoneOnuConfigLoopback_Type())
zhoneOnuConfigLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigLoopback.setStatus(_A)
class _ZhoneOnuConfigOverheadSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onuOverheadSize3Bytes',1),('onuOverheadSize6Bytes',2),('onuOverheadSize12Bytes',3)))
_ZhoneOnuConfigOverheadSize_Type.__name__=_D
_ZhoneOnuConfigOverheadSize_Object=MibTableColumn
zhoneOnuConfigOverheadSize=_ZhoneOnuConfigOverheadSize_Object((1,3,6,1,4,1,5504,5,12,1,6,1,6),_ZhoneOnuConfigOverheadSize_Type())
zhoneOnuConfigOverheadSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigOverheadSize.setStatus(_A)
class _ZhoneOnuConfigRfVideo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZhoneOnuConfigRfVideo_Type.__name__=_D
_ZhoneOnuConfigRfVideo_Object=MibTableColumn
zhoneOnuConfigRfVideo=_ZhoneOnuConfigRfVideo_Object((1,3,6,1,4,1,5504,5,12,1,6,1,7),_ZhoneOnuConfigRfVideo_Type())
zhoneOnuConfigRfVideo.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneOnuConfigRfVideo.setStatus(_A)
_ZhoneOnuStatusTable_Object=MibTable
zhoneOnuStatusTable=_ZhoneOnuStatusTable_Object((1,3,6,1,4,1,5504,5,12,1,7))
if mibBuilder.loadTexts:zhoneOnuStatusTable.setStatus(_A)
_ZhoneOnuStatusEntry_Object=MibTableRow
zhoneOnuStatusEntry=_ZhoneOnuStatusEntry_Object((1,3,6,1,4,1,5504,5,12,1,7,1))
zhoneOnuStatusEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zhoneOnuStatusEntry.setStatus(_A)
class _ZhoneOnuStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onuStateDown',1),('onuStateUp',2)))
_ZhoneOnuStatusOperStatus_Type.__name__=_D
_ZhoneOnuStatusOperStatus_Object=MibTableColumn
zhoneOnuStatusOperStatus=_ZhoneOnuStatusOperStatus_Object((1,3,6,1,4,1,5504,5,12,1,7,1,1),_ZhoneOnuStatusOperStatus_Type())
zhoneOnuStatusOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusOperStatus.setStatus(_A)
class _ZhoneOnuStatusLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_ZhoneOnuStatusLoopback_Type.__name__=_D
_ZhoneOnuStatusLoopback_Object=MibTableColumn
zhoneOnuStatusLoopback=_ZhoneOnuStatusLoopback_Object((1,3,6,1,4,1,5504,5,12,1,7,1,2),_ZhoneOnuStatusLoopback_Type())
zhoneOnuStatusLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusLoopback.setStatus(_A)
_ZhoneOnuStatusAlarmTF_Type=TruthValue
_ZhoneOnuStatusAlarmTF_Object=MibTableColumn
zhoneOnuStatusAlarmTF=_ZhoneOnuStatusAlarmTF_Object((1,3,6,1,4,1,5504,5,12,1,7,1,3),_ZhoneOnuStatusAlarmTF_Type())
zhoneOnuStatusAlarmTF.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmTF.setStatus(_A)
_ZhoneOnuStatusAlarmLOS_Type=TruthValue
_ZhoneOnuStatusAlarmLOS_Object=MibTableColumn
zhoneOnuStatusAlarmLOS=_ZhoneOnuStatusAlarmLOS_Object((1,3,6,1,4,1,5504,5,12,1,7,1,4),_ZhoneOnuStatusAlarmLOS_Type())
zhoneOnuStatusAlarmLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmLOS.setStatus(_A)
_ZhoneOnuStatusAlarmPEE_Type=TruthValue
_ZhoneOnuStatusAlarmPEE_Object=MibTableColumn
zhoneOnuStatusAlarmPEE=_ZhoneOnuStatusAlarmPEE_Object((1,3,6,1,4,1,5504,5,12,1,7,1,5),_ZhoneOnuStatusAlarmPEE_Type())
zhoneOnuStatusAlarmPEE.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmPEE.setStatus(_A)
_ZhoneOnuStatusAlarmSUF_Type=TruthValue
_ZhoneOnuStatusAlarmSUF_Object=MibTableColumn
zhoneOnuStatusAlarmSUF=_ZhoneOnuStatusAlarmSUF_Object((1,3,6,1,4,1,5504,5,12,1,7,1,6),_ZhoneOnuStatusAlarmSUF_Type())
zhoneOnuStatusAlarmSUF.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmSUF.setStatus(_A)
_ZhoneOnuStatusAlarmOAML_Type=TruthValue
_ZhoneOnuStatusAlarmOAML_Object=MibTableColumn
zhoneOnuStatusAlarmOAML=_ZhoneOnuStatusAlarmOAML_Object((1,3,6,1,4,1,5504,5,12,1,7,1,7),_ZhoneOnuStatusAlarmOAML_Type())
zhoneOnuStatusAlarmOAML.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmOAML.setStatus(_A)
_ZhoneOnuStatusAlarmLCD_Type=TruthValue
_ZhoneOnuStatusAlarmLCD_Object=MibTableColumn
zhoneOnuStatusAlarmLCD=_ZhoneOnuStatusAlarmLCD_Object((1,3,6,1,4,1,5504,5,12,1,7,1,8),_ZhoneOnuStatusAlarmLCD_Type())
zhoneOnuStatusAlarmLCD.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmLCD.setStatus(_A)
_ZhoneOnuStatusAlarmFRML_Type=TruthValue
_ZhoneOnuStatusAlarmFRML_Object=MibTableColumn
zhoneOnuStatusAlarmFRML=_ZhoneOnuStatusAlarmFRML_Object((1,3,6,1,4,1,5504,5,12,1,7,1,9),_ZhoneOnuStatusAlarmFRML_Type())
zhoneOnuStatusAlarmFRML.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmFRML.setStatus(_A)
_ZhoneOnuStatusAlarmERR_Type=TruthValue
_ZhoneOnuStatusAlarmERR_Object=MibTableColumn
zhoneOnuStatusAlarmERR=_ZhoneOnuStatusAlarmERR_Object((1,3,6,1,4,1,5504,5,12,1,7,1,10),_ZhoneOnuStatusAlarmERR_Type())
zhoneOnuStatusAlarmERR.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmERR.setStatus(_A)
_ZhoneOnuStatusAlarmSD_Type=TruthValue
_ZhoneOnuStatusAlarmSD_Object=MibTableColumn
zhoneOnuStatusAlarmSD=_ZhoneOnuStatusAlarmSD_Object((1,3,6,1,4,1,5504,5,12,1,7,1,11),_ZhoneOnuStatusAlarmSD_Type())
zhoneOnuStatusAlarmSD.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmSD.setStatus(_A)
_ZhoneOnuStatusAlarmMEM_Type=TruthValue
_ZhoneOnuStatusAlarmMEM_Object=MibTableColumn
zhoneOnuStatusAlarmMEM=_ZhoneOnuStatusAlarmMEM_Object((1,3,6,1,4,1,5504,5,12,1,7,1,12),_ZhoneOnuStatusAlarmMEM_Type())
zhoneOnuStatusAlarmMEM.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmMEM.setStatus(_A)
_ZhoneOnuStatusAlarmDACT_Type=TruthValue
_ZhoneOnuStatusAlarmDACT_Object=MibTableColumn
zhoneOnuStatusAlarmDACT=_ZhoneOnuStatusAlarmDACT_Object((1,3,6,1,4,1,5504,5,12,1,7,1,13),_ZhoneOnuStatusAlarmDACT_Type())
zhoneOnuStatusAlarmDACT.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmDACT.setStatus(_A)
_ZhoneOnuStatusAlarmDIS_Type=TruthValue
_ZhoneOnuStatusAlarmDIS_Object=MibTableColumn
zhoneOnuStatusAlarmDIS=_ZhoneOnuStatusAlarmDIS_Object((1,3,6,1,4,1,5504,5,12,1,7,1,14),_ZhoneOnuStatusAlarmDIS_Type())
zhoneOnuStatusAlarmDIS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmDIS.setStatus(_A)
_ZhoneOnuStatusAlarmMIS_Type=TruthValue
_ZhoneOnuStatusAlarmMIS_Object=MibTableColumn
zhoneOnuStatusAlarmMIS=_ZhoneOnuStatusAlarmMIS_Object((1,3,6,1,4,1,5504,5,12,1,7,1,15),_ZhoneOnuStatusAlarmMIS_Type())
zhoneOnuStatusAlarmMIS.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusAlarmMIS.setStatus(_A)
class _ZhoneOnuStatusLastChange_Type(TimeStamp):defaultValue=0
_ZhoneOnuStatusLastChange_Type.__name__=_L
_ZhoneOnuStatusLastChange_Object=MibTableColumn
zhoneOnuStatusLastChange=_ZhoneOnuStatusLastChange_Object((1,3,6,1,4,1,5504,5,12,1,7,1,16),_ZhoneOnuStatusLastChange_Type())
zhoneOnuStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOnuStatusLastChange.setStatus(_A)
class _ZhoneOltTrafficContainerIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneOltTrafficContainerIndexNext_Type.__name__=_D
_ZhoneOltTrafficContainerIndexNext_Object=MibScalar
zhoneOltTrafficContainerIndexNext=_ZhoneOltTrafficContainerIndexNext_Object((1,3,6,1,4,1,5504,5,12,1,8),_ZhoneOltTrafficContainerIndexNext_Type())
zhoneOltTrafficContainerIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneOltTrafficContainerIndexNext.setStatus(_A)
_ZhoneOltTrafficContainerTable_Object=MibTable
zhoneOltTrafficContainerTable=_ZhoneOltTrafficContainerTable_Object((1,3,6,1,4,1,5504,5,12,1,9))
if mibBuilder.loadTexts:zhoneOltTrafficContainerTable.setStatus(_A)
_ZhoneOltTrafficContainerEntry_Object=MibTableRow
zhoneOltTrafficContainerEntry=_ZhoneOltTrafficContainerEntry_Object((1,3,6,1,4,1,5504,5,12,1,9,1))
zhoneOltTrafficContainerEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:zhoneOltTrafficContainerEntry.setStatus(_A)
class _ZhoneOltTrafficContainerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZhoneOltTrafficContainerIndex_Type.__name__=_D
_ZhoneOltTrafficContainerIndex_Object=MibTableColumn
zhoneOltTrafficContainerIndex=_ZhoneOltTrafficContainerIndex_Object((1,3,6,1,4,1,5504,5,12,1,9,1,1),_ZhoneOltTrafficContainerIndex_Type())
zhoneOltTrafficContainerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhoneOltTrafficContainerIndex.setStatus(_A)
class _ZhoneOltTrafficContainerGuaranteedBW_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneOltTrafficContainerGuaranteedBW_Type.__name__=_K
_ZhoneOltTrafficContainerGuaranteedBW_Object=MibTableColumn
zhoneOltTrafficContainerGuaranteedBW=_ZhoneOltTrafficContainerGuaranteedBW_Object((1,3,6,1,4,1,5504,5,12,1,9,1,2),_ZhoneOltTrafficContainerGuaranteedBW_Type())
zhoneOltTrafficContainerGuaranteedBW.setMaxAccess(_I)
if mibBuilder.loadTexts:zhoneOltTrafficContainerGuaranteedBW.setStatus(_A)
if mibBuilder.loadTexts:zhoneOltTrafficContainerGuaranteedBW.setUnits('Megabits per second')
class _ZhoneOltTrafficContainerMaximumBW_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneOltTrafficContainerMaximumBW_Type.__name__=_K
_ZhoneOltTrafficContainerMaximumBW_Object=MibTableColumn
zhoneOltTrafficContainerMaximumBW=_ZhoneOltTrafficContainerMaximumBW_Object((1,3,6,1,4,1,5504,5,12,1,9,1,3),_ZhoneOltTrafficContainerMaximumBW_Type())
zhoneOltTrafficContainerMaximumBW.setMaxAccess(_I)
if mibBuilder.loadTexts:zhoneOltTrafficContainerMaximumBW.setStatus(_A)
class _ZhoneOltTrafficContainerCBR_Type(TruthValue):defaultValue=1
_ZhoneOltTrafficContainerCBR_Type.__name__=_G
_ZhoneOltTrafficContainerCBR_Object=MibTableColumn
zhoneOltTrafficContainerCBR=_ZhoneOltTrafficContainerCBR_Object((1,3,6,1,4,1,5504,5,12,1,9,1,4),_ZhoneOltTrafficContainerCBR_Type())
zhoneOltTrafficContainerCBR.setMaxAccess(_I)
if mibBuilder.loadTexts:zhoneOltTrafficContainerCBR.setStatus(_A)
class _ZhoneOltTrafficContainerCbrCompensate_Type(TruthValue):defaultValue=2
_ZhoneOltTrafficContainerCbrCompensate_Type.__name__=_G
_ZhoneOltTrafficContainerCbrCompensate_Object=MibTableColumn
zhoneOltTrafficContainerCbrCompensate=_ZhoneOltTrafficContainerCbrCompensate_Object((1,3,6,1,4,1,5504,5,12,1,9,1,5),_ZhoneOltTrafficContainerCbrCompensate_Type())
zhoneOltTrafficContainerCbrCompensate.setMaxAccess(_I)
if mibBuilder.loadTexts:zhoneOltTrafficContainerCbrCompensate.setStatus(_A)
_ZhoneOltTrafficContainerRowStatus_Type=ZhoneRowStatus
_ZhoneOltTrafficContainerRowStatus_Object=MibTableColumn
zhoneOltTrafficContainerRowStatus=_ZhoneOltTrafficContainerRowStatus_Object((1,3,6,1,4,1,5504,5,12,1,9,1,6),_ZhoneOltTrafficContainerRowStatus_Type())
zhoneOltTrafficContainerRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:zhoneOltTrafficContainerRowStatus.setStatus(_A)
_ZhoneAponTraps_ObjectIdentity=ObjectIdentity
zhoneAponTraps=_ZhoneAponTraps_ObjectIdentity((1,3,6,1,4,1,5504,5,12,3))
if mibBuilder.loadTexts:zhoneAponTraps.setStatus(_A)
_ZhoneAPONV2Traps_ObjectIdentity=ObjectIdentity
zhoneAPONV2Traps=_ZhoneAPONV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,5,12,3,0))
if mibBuilder.loadTexts:zhoneAPONV2Traps.setStatus(_A)
zhoneAponOltConfigGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,2))
zhoneAponOltConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:zhoneAponOltConfigGroup.setStatus(_A)
zhoneAponOltStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,3))
zhoneAponOltStatusGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_O)))
if mibBuilder.loadTexts:zhoneAponOltStatusGroup.setStatus(_A)
zhoneAponOltOnuConfigGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,4))
zhoneAponOltOnuConfigGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:zhoneAponOltOnuConfigGroup.setStatus(_A)
zhoneAponOltOnuStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,5))
zhoneAponOltOnuStatusGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:zhoneAponOltOnuStatusGroup.setStatus(_A)
zhoneAponOnuConfigGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,6))
zhoneAponOnuConfigGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:zhoneAponOnuConfigGroup.setStatus(_A)
zhoneAponOnuStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,7))
zhoneAponOnuStatusGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:zhoneAponOnuStatusGroup.setStatus(_A)
zhoneAponOltTrafficContainerGroup=ObjectGroup((1,3,6,1,4,1,5504,9,1,8))
zhoneAponOltTrafficContainerGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:zhoneAponOltTrafficContainerGroup.setStatus(_A)
zhoneOltLineStatusChangeTrap=NotificationType((1,3,6,1,4,1,5504,5,12,3,0,1))
zhoneOltLineStatusChangeTrap.setObjects(*((_B,_O),(_F,_J)))
if mibBuilder.loadTexts:zhoneOltLineStatusChangeTrap.setStatus(_A)
zhoneOnuLineStatusChangeTrap=NotificationType((1,3,6,1,4,1,5504,5,12,3,0,2))
zhoneOnuLineStatusChangeTrap.setObjects(*((_B,_Ac),(_F,_J)))
if mibBuilder.loadTexts:zhoneOnuLineStatusChangeTrap.setStatus(_A)
zhoneAponTrapsGroup=NotificationGroup((1,3,6,1,4,1,5504,9,1,9))
zhoneAponTrapsGroup.setObjects((_B,_Ad))
if mibBuilder.loadTexts:zhoneAponTrapsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhoneApon':zhoneApon,'zhoneAponMIB':zhoneAponMIB,'zhoneOltConfigTable':zhoneOltConfigTable,'zhoneOltConfigEntry':zhoneOltConfigEntry,_n:zhoneOltConfigAutoLearn,_U:zhoneOltConfigCellScrambling,_V:zhoneOltConfigBip8,_W:zhoneOltConfigHec,_X:zhoneOltConfigHecRxBypass,_Y:zhoneOltConfigCrcRx,_Z:zhoneOltConfigOverheadSize,_a:zhoneOltConfigDelimiterPattern,_b:zhoneOltConfigDelimiterSize,_c:zhoneOltConfigCdrPattern,_d:zhoneOltConfigCdrLocation,_e:zhoneOltConfigCdrActiveHigh,_f:zhoneOltConfigCpeLimit,_g:zhoneOltConfigLcdLimit,_h:zhoneOltConfigLcdAlpha,_i:zhoneOltConfigLcdDelta,_j:zhoneOltConfigTxDiscardNonMatchingVpi,_k:zhoneOltConfigUtopiaDiscard,_o:zhoneOltConfigSyncBytesClkDivisor,_p:zhoneOltConfigTxSyncBytes,_m:zhoneOltConfigLoopback,_q:zhoneOltConfigMaxPonDistance,_l:zhoneOltConfigLineStatusChangeTrapEnable,'zhoneOltStatusTable':zhoneOltStatusTable,'zhoneOltStatusEntry':zhoneOltStatusEntry,_r:zhoneOltStatusState,_s:zhoneOltStatusLoopback,_t:zhoneOltStatusPonAlarmLPHY,_u:zhoneOltStatusPonAlarmTF,_v:zhoneOltStatusPonAlarmSUF,_w:zhoneOltStatusPonAlarmPEE,_x:zhoneOltStatusPonAlarmLCD,_y:zhoneOltStatusPonAlarmLOS,_z:zhoneOltStatusPonAlarmOAML,_A0:zhoneOltStatusPonAlarmCPE,_O:zhoneOltStatusLastChange,'zhoneOltOnuConfigTable':zhoneOltOnuConfigTable,'zhoneOltOnuConfigEntry':zhoneOltOnuConfigEntry,_A1:zhoneOltOnuConfigPassword,_A2:zhoneOltOnuConfigSerialNum,_A3:zhoneOltOnuConfigChurnkey,_A4:zhoneOltOnuConfigLineStatusChangeTrapEnable,'zhoneOltOnuStatusTable':zhoneOltOnuStatusTable,'zhoneOltOnuStatusEntry':zhoneOltOnuStatusEntry,_A5:zhoneOltOnuStatusPonAlarmLOA,_A6:zhoneOltOnuStatusPonAlarmERR,_A7:zhoneOltOnuStatusPonAlarmSD,_A8:zhoneOltOnuStatusPonAlarmREI,_A9:zhoneOltOnuStatusPonAlarmMEM,_AA:zhoneOltOnuStatusPonAlarmRXINH,'zhoneOltOnuStatusPonAlarmLOS':zhoneOltOnuStatusPonAlarmLOS,'zhoneOltOnuStatusPonAlarmPEE':zhoneOltOnuStatusPonAlarmPEE,'zhoneOltOnuStatusPonAlarmSUF':zhoneOltOnuStatusPonAlarmSUF,'zhoneOltOnuStatusPonAlarmOAML':zhoneOltOnuStatusPonAlarmOAML,'zhoneOltOnuStatusPonAlarmLCD':zhoneOltOnuStatusPonAlarmLCD,'zhoneOnuConfigTable':zhoneOnuConfigTable,'zhoneOnuConfigEntry':zhoneOnuConfigEntry,_AB:zhoneOnuConfigSerialNumber,_AC:zhoneOnuConfigPassword,_AD:zhoneOnuConfigNetworkRefClk,_AE:zhoneOnuConfigHEC,_AF:zhoneOnuConfigLoopback,_AG:zhoneOnuConfigOverheadSize,'zhoneOnuConfigRfVideo':zhoneOnuConfigRfVideo,'zhoneOnuStatusTable':zhoneOnuStatusTable,'zhoneOnuStatusEntry':zhoneOnuStatusEntry,_AV:zhoneOnuStatusOperStatus,_AH:zhoneOnuStatusLoopback,_AI:zhoneOnuStatusAlarmTF,_AJ:zhoneOnuStatusAlarmLOS,_AK:zhoneOnuStatusAlarmPEE,_AL:zhoneOnuStatusAlarmSUF,_AM:zhoneOnuStatusAlarmOAML,_AN:zhoneOnuStatusAlarmLCD,_AO:zhoneOnuStatusAlarmFRML,_AP:zhoneOnuStatusAlarmERR,_AQ:zhoneOnuStatusAlarmSD,_AR:zhoneOnuStatusAlarmMEM,_AS:zhoneOnuStatusAlarmDACT,_AT:zhoneOnuStatusAlarmDIS,_AU:zhoneOnuStatusAlarmMIS,_Ac:zhoneOnuStatusLastChange,_AY:zhoneOltTrafficContainerIndexNext,'zhoneOltTrafficContainerTable':zhoneOltTrafficContainerTable,'zhoneOltTrafficContainerEntry':zhoneOltTrafficContainerEntry,_T:zhoneOltTrafficContainerIndex,_Ab:zhoneOltTrafficContainerGuaranteedBW,_AW:zhoneOltTrafficContainerMaximumBW,_AX:zhoneOltTrafficContainerCBR,_AZ:zhoneOltTrafficContainerCbrCompensate,_Aa:zhoneOltTrafficContainerRowStatus,'zhoneAponTraps':zhoneAponTraps,'zhoneAPONV2Traps':zhoneAPONV2Traps,_Ad:zhoneOltLineStatusChangeTrap,'zhoneOnuLineStatusChangeTrap':zhoneOnuLineStatusChangeTrap,'zhoneAponOltConfigGroup':zhoneAponOltConfigGroup,'zhoneAponOltStatusGroup':zhoneAponOltStatusGroup,'zhoneAponOltOnuConfigGroup':zhoneAponOltOnuConfigGroup,'zhoneAponOltOnuStatusGroup':zhoneAponOltOnuStatusGroup,'zhoneAponOnuConfigGroup':zhoneAponOnuConfigGroup,'zhoneAponOnuStatusGroup':zhoneAponOnuStatusGroup,'zhoneAponOltTrafficContainerGroup':zhoneAponOltTrafficContainerGroup,'zhoneAponTrapsGroup':zhoneAponTrapsGroup})