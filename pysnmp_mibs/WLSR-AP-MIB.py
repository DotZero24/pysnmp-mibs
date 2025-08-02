_v='wlsrInterferingAPInfoURL'
_u='wlsrAddressType'
_t='wlsrReceiverMac'
_s='wlsrTransmitterMac'
_r='wlsrSignatureName'
_q='wlsrMatchedIp'
_p='wlsrMatchedMac'
_o='wlsrAmApBSSID'
_n='rate1Mbps'
_m='rate2Mbps'
_l='rate5Mbps'
_k='rate11Mbps'
_j='rate6Mbps'
_i='rate9Mbps'
_h='rate12Mbps'
_g='rate18Mbps'
_f='rate24Mbps'
_e='rate36Mbps'
_d='rate48Mbps'
_c='rate54Mbps'
_b='wlsrBSSID'
_a='OctetString'
_Z='wlsrRogueInfoURL'
_Y='unused3'
_X='unused2'
_W='unused1'
_V='unused0'
_U='disable'
_T='enable'
_S='wlsrFrameType'
_R='wlsrTargetApChannel'
_Q='not-accessible'
_P='Bits'
_O='wlsrSourceMac'
_N='wlsrStaAddress'
_M='wlsrChStatsChannel'
_L='deprecated'
_K='wlsrRSSI'
_J='DisplayString'
_I='wlsrNodeMac'
_H='Integer32'
_G='wlsrTargetApSSID'
_F='wlsrTargetApBSSID'
_E='wlsrCurrentChannel'
_D='wlsrLocation'
_C='WLSR-AP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsrEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsrEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsrMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,3,1,1))
if mibBuilder.loadTexts:wlsrMIB.setRevisions(('2020-08-14 17:45',))
_WlsrConfigGroup_ObjectIdentity=ObjectIdentity
wlsrConfigGroup=_WlsrConfigGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,1))
_WlsrConfigTable_Object=MibTable
wlsrConfigTable=_WlsrConfigTable_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1))
if mibBuilder.loadTexts:wlsrConfigTable.setStatus(_A)
_WlsrConfigEntry_Object=MibTableRow
wlsrConfigEntry=_WlsrConfigEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1))
wlsrConfigEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:wlsrConfigEntry.setStatus(_A)
_WlsrBSSID_Type=MacAddress
_WlsrBSSID_Object=MibTableColumn
wlsrBSSID=_WlsrBSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,1),_WlsrBSSID_Type())
wlsrBSSID.setMaxAccess(_Q)
if mibBuilder.loadTexts:wlsrBSSID.setStatus(_A)
class _WlsrESSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsrESSID_Type.__name__=_J
_WlsrESSID_Object=MibTableColumn
wlsrESSID=_WlsrESSID_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,2),_WlsrESSID_Type())
wlsrESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrESSID.setStatus(_A)
class _WlsrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('conductor',1),('adhoc',2),('monitor',3)))
_WlsrMode_Type.__name__=_H
_WlsrMode_Object=MibTableColumn
wlsrMode=_WlsrMode_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,3),_WlsrMode_Type())
wlsrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrMode.setStatus(_A)
class _WlsrCurrentChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,165))
_WlsrCurrentChannel_Type.__name__=_H
_WlsrCurrentChannel_Object=MibTableColumn
wlsrCurrentChannel=_WlsrCurrentChannel_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,4),_WlsrCurrentChannel_Type())
wlsrCurrentChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrCurrentChannel.setStatus(_A)
_WlsrTxPower_Type=Integer32
_WlsrTxPower_Object=MibTableColumn
wlsrTxPower=_WlsrTxPower_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,5),_WlsrTxPower_Type())
wlsrTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTxPower.setStatus(_A)
class _WlsrRTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_WlsrRTSThreshold_Type.__name__=_H
_WlsrRTSThreshold_Object=MibTableColumn
wlsrRTSThreshold=_WlsrRTSThreshold_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,6),_WlsrRTSThreshold_Type())
wlsrRTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrRTSThreshold.setStatus(_A)
class _WlsrRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WlsrRetryLimit_Type.__name__=_H
_WlsrRetryLimit_Object=MibTableColumn
wlsrRetryLimit=_WlsrRetryLimit_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,7),_WlsrRetryLimit_Type())
wlsrRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrRetryLimit.setStatus(_A)
class _WlsrPreamble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_WlsrPreamble_Type.__name__=_H
_WlsrPreamble_Object=MibTableColumn
wlsrPreamble=_WlsrPreamble_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,8),_WlsrPreamble_Type())
wlsrPreamble.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrPreamble.setStatus(_A)
class _WlsrBeaconInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WlsrBeaconInterval_Type.__name__=_H
_WlsrBeaconInterval_Object=MibTableColumn
wlsrBeaconInterval=_WlsrBeaconInterval_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,9),_WlsrBeaconInterval_Type())
wlsrBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrBeaconInterval.setStatus(_A)
class _WlsrPowerMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_WlsrPowerMgmt_Type.__name__=_H
_WlsrPowerMgmt_Object=MibTableColumn
wlsrPowerMgmt=_WlsrPowerMgmt_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,10),_WlsrPowerMgmt_Type())
wlsrPowerMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrPowerMgmt.setStatus(_A)
class _WlsrLoadBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_WlsrLoadBalance_Type.__name__=_H
_WlsrLoadBalance_Object=MibTableColumn
wlsrLoadBalance=_WlsrLoadBalance_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,11),_WlsrLoadBalance_Type())
wlsrLoadBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrLoadBalance.setStatus(_A)
class _WlsrSupportedRates_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14),(_n,15)))
_WlsrSupportedRates_Type.__name__=_P
_WlsrSupportedRates_Object=MibTableColumn
wlsrSupportedRates=_WlsrSupportedRates_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,12),_WlsrSupportedRates_Type())
wlsrSupportedRates.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrSupportedRates.setStatus(_A)
class _WlsrDTIMPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WlsrDTIMPeriod_Type.__name__=_H
_WlsrDTIMPeriod_Object=MibTableColumn
wlsrDTIMPeriod=_WlsrDTIMPeriod_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,13),_WlsrDTIMPeriod_Type())
wlsrDTIMPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrDTIMPeriod.setStatus(_A)
_WlsrLMSAddress_Type=IpAddress
_WlsrLMSAddress_Object=MibTableColumn
wlsrLMSAddress=_WlsrLMSAddress_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,14),_WlsrLMSAddress_Type())
wlsrLMSAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrLMSAddress.setStatus(_A)
class _WlsrEncryption_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),('unused4',4),('unused5',5),('unused6',6),('xSec',7),('wpa2PreAuth',8),('aes8021x',9),('aesPSK',10),('dynamicTkip',11),('staticTkip',12),('dynamicWep',13),('staticWep',14),('disabled',15)))
_WlsrEncryption_Type.__name__=_P
_WlsrEncryption_Object=MibTableColumn
wlsrEncryption=_WlsrEncryption_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,15),_WlsrEncryption_Type())
wlsrEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrEncryption.setStatus(_A)
_WlsrStatus_Type=TruthValue
_WlsrStatus_Object=MibTableColumn
wlsrStatus=_WlsrStatus_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,17),_WlsrStatus_Type())
wlsrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStatus.setStatus(_A)
_WlsrAgeout_Type=Integer32
_WlsrAgeout_Object=MibTableColumn
wlsrAgeout=_WlsrAgeout_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,18),_WlsrAgeout_Type())
wlsrAgeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAgeout.setStatus(_A)
class _WlsrMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_WlsrMTU_Type.__name__=_H
_WlsrMTU_Object=MibTableColumn
wlsrMTU=_WlsrMTU_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,19),_WlsrMTU_Type())
wlsrMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrMTU.setStatus(_A)
class _WlsrLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlsrLocation_Type.__name__=_J
_WlsrLocation_Object=MibTableColumn
wlsrLocation=_WlsrLocation_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,20),_WlsrLocation_Type())
wlsrLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrLocation.setStatus(_A)
_WlsrHideSSID_Type=TruthValue
_WlsrHideSSID_Object=MibTableColumn
wlsrHideSSID=_WlsrHideSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,21),_WlsrHideSSID_Type())
wlsrHideSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrHideSSID.setStatus(_A)
_WlsrDenyBroadcast_Type=TruthValue
_WlsrDenyBroadcast_Object=MibTableColumn
wlsrDenyBroadcast=_WlsrDenyBroadcast_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,22),_WlsrDenyBroadcast_Type())
wlsrDenyBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrDenyBroadcast.setStatus(_A)
class _WlsrBGmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bgMixed',1),('bOnly',2),('gOnly',3)))
_WlsrBGmode_Type.__name__=_H
_WlsrBGmode_Object=MibTableColumn
wlsrBGmode=_WlsrBGmode_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,23),_WlsrBGmode_Type())
wlsrBGmode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrBGmode.setStatus(_A)
class _WlsrCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,10,11,12)));namedValues=NamedValues(*(('noCard',1),('intersil',2),('atherosA',3),('atherosBG',4),('atherosABG',5),('ar5212A',10),('ar5212BG',11),('ar5212ABG',12)))
_WlsrCardType_Type.__name__=_H
_WlsrCardType_Object=MibTableColumn
wlsrCardType=_WlsrCardType_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,24),_WlsrCardType_Type())
wlsrCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrCardType.setStatus(_A)
_WlsrRegDomain_Type=Integer32
_WlsrRegDomain_Object=MibTableColumn
wlsrRegDomain=_WlsrRegDomain_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,25),_WlsrRegDomain_Type())
wlsrRegDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrRegDomain.setStatus(_L)
class _WlsrCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsrCountryCode_Type.__name__=_J
_WlsrCountryCode_Object=MibTableColumn
wlsrCountryCode=_WlsrCountryCode_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,26),_WlsrCountryCode_Type())
wlsrCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrCountryCode.setStatus(_A)
class _WlsrTxRates_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3),(_c,4),(_d,5),(_e,6),(_f,7),(_g,8),(_h,9),(_i,10),(_j,11),(_k,12),(_l,13),(_m,14),(_n,15)))
_WlsrTxRates_Type.__name__=_P
_WlsrTxRates_Object=MibTableColumn
wlsrTxRates=_WlsrTxRates_Object((1,3,6,1,4,1,14823,2,3,1,1,1,1,1,27),_WlsrTxRates_Type())
wlsrTxRates.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTxRates.setStatus(_A)
_WlsrStatsGroup_ObjectIdentity=ObjectIdentity
wlsrStatsGroup=_WlsrStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,3))
_WlsrStatsChannelGroup_ObjectIdentity=ObjectIdentity
wlsrStatsChannelGroup=_WlsrStatsChannelGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,3,3))
_WlsrChannelStatsTable_Object=MibTable
wlsrChannelStatsTable=_WlsrChannelStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1))
if mibBuilder.loadTexts:wlsrChannelStatsTable.setStatus(_A)
_WlsrChannelStatsEntry_Object=MibTableRow
wlsrChannelStatsEntry=_WlsrChannelStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1))
wlsrChannelStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wlsrChannelStatsEntry.setStatus(_A)
class _WlsrChStatsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,165))
_WlsrChStatsChannel_Type.__name__=_H
_WlsrChStatsChannel_Object=MibTableColumn
wlsrChStatsChannel=_WlsrChStatsChannel_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,1),_WlsrChStatsChannel_Type())
wlsrChStatsChannel.setMaxAccess(_Q)
if mibBuilder.loadTexts:wlsrChStatsChannel.setStatus(_A)
_WlsrChStatsNumAPs_Type=Integer32
_WlsrChStatsNumAPs_Object=MibTableColumn
wlsrChStatsNumAPs=_WlsrChStatsNumAPs_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,2),_WlsrChStatsNumAPs_Type())
wlsrChStatsNumAPs.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsNumAPs.setStatus(_A)
_WlsrChStatsNumStations_Type=Integer32
_WlsrChStatsNumStations_Object=MibTableColumn
wlsrChStatsNumStations=_WlsrChStatsNumStations_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,3),_WlsrChStatsNumStations_Type())
wlsrChStatsNumStations.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsNumStations.setStatus(_A)
_WlsrChStatsTotPkts_Type=Counter32
_WlsrChStatsTotPkts_Object=MibTableColumn
wlsrChStatsTotPkts=_WlsrChStatsTotPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,4),_WlsrChStatsTotPkts_Type())
wlsrChStatsTotPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPkts.setStatus(_A)
_WlsrChStatsTotBytes_Type=Counter32
_WlsrChStatsTotBytes_Object=MibTableColumn
wlsrChStatsTotBytes=_WlsrChStatsTotBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,5),_WlsrChStatsTotBytes_Type())
wlsrChStatsTotBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytes.setStatus(_A)
_WlsrChStatsTotRetryPkts_Type=Counter32
_WlsrChStatsTotRetryPkts_Object=MibTableColumn
wlsrChStatsTotRetryPkts=_WlsrChStatsTotRetryPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,6),_WlsrChStatsTotRetryPkts_Type())
wlsrChStatsTotRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotRetryPkts.setStatus(_A)
_WlsrChStatsTotFragmentedPkts_Type=Counter32
_WlsrChStatsTotFragmentedPkts_Object=MibTableColumn
wlsrChStatsTotFragmentedPkts=_WlsrChStatsTotFragmentedPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,7),_WlsrChStatsTotFragmentedPkts_Type())
wlsrChStatsTotFragmentedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotFragmentedPkts.setStatus(_A)
_WlsrChStatsTotPhyErrPkts_Type=Counter32
_WlsrChStatsTotPhyErrPkts_Object=MibTableColumn
wlsrChStatsTotPhyErrPkts=_WlsrChStatsTotPhyErrPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,8),_WlsrChStatsTotPhyErrPkts_Type())
wlsrChStatsTotPhyErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPhyErrPkts.setStatus(_A)
_WlsrChStatsTotMacErrPkts_Type=Counter32
_WlsrChStatsTotMacErrPkts_Object=MibTableColumn
wlsrChStatsTotMacErrPkts=_WlsrChStatsTotMacErrPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,9),_WlsrChStatsTotMacErrPkts_Type())
wlsrChStatsTotMacErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotMacErrPkts.setStatus(_A)
_WlsrChStatsFrameErrorRate_Type=Integer32
_WlsrChStatsFrameErrorRate_Object=MibTableColumn
wlsrChStatsFrameErrorRate=_WlsrChStatsFrameErrorRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,10),_WlsrChStatsFrameErrorRate_Type())
wlsrChStatsFrameErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameErrorRate.setStatus(_A)
_WlsrChStatsFrameRetryRate_Type=Integer32
_WlsrChStatsFrameRetryRate_Object=MibTableColumn
wlsrChStatsFrameRetryRate=_WlsrChStatsFrameRetryRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,11),_WlsrChStatsFrameRetryRate_Type())
wlsrChStatsFrameRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameRetryRate.setStatus(_A)
_WlsrChStatsFrameLowSpeedRate_Type=Integer32
_WlsrChStatsFrameLowSpeedRate_Object=MibTableColumn
wlsrChStatsFrameLowSpeedRate=_WlsrChStatsFrameLowSpeedRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,12),_WlsrChStatsFrameLowSpeedRate_Type())
wlsrChStatsFrameLowSpeedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameLowSpeedRate.setStatus(_A)
_WlsrChStatsFrameNonUnicastRate_Type=Integer32
_WlsrChStatsFrameNonUnicastRate_Object=MibTableColumn
wlsrChStatsFrameNonUnicastRate=_WlsrChStatsFrameNonUnicastRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,13),_WlsrChStatsFrameNonUnicastRate_Type())
wlsrChStatsFrameNonUnicastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameNonUnicastRate.setStatus(_A)
_WlsrChStatsFrameBandwidthRate_Type=Integer32
_WlsrChStatsFrameBandwidthRate_Object=MibTableColumn
wlsrChStatsFrameBandwidthRate=_WlsrChStatsFrameBandwidthRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,14),_WlsrChStatsFrameBandwidthRate_Type())
wlsrChStatsFrameBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameBandwidthRate.setStatus(_A)
_WlsrChStatsFrameFragmentationRate_Type=Integer32
_WlsrChStatsFrameFragmentationRate_Object=MibTableColumn
wlsrChStatsFrameFragmentationRate=_WlsrChStatsFrameFragmentationRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,15),_WlsrChStatsFrameFragmentationRate_Type())
wlsrChStatsFrameFragmentationRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsFrameFragmentationRate.setStatus(_A)
_WlsrChStatsMonitoredTime_Type=TimeTicks
_WlsrChStatsMonitoredTime_Object=MibTableColumn
wlsrChStatsMonitoredTime=_WlsrChStatsMonitoredTime_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,1,1,16),_WlsrChStatsMonitoredTime_Type())
wlsrChStatsMonitoredTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsMonitoredTime.setStatus(_A)
_WlsrChannelRateStatsTable_Object=MibTable
wlsrChannelRateStatsTable=_WlsrChannelRateStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2))
if mibBuilder.loadTexts:wlsrChannelRateStatsTable.setStatus(_A)
_WlsrChannelRateStatsEntry_Object=MibTableRow
wlsrChannelRateStatsEntry=_WlsrChannelRateStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1))
wlsrChannelRateStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wlsrChannelRateStatsEntry.setStatus(_A)
_WlsrChStatsTotPktsAt1Mbps_Type=Counter32
_WlsrChStatsTotPktsAt1Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt1Mbps=_WlsrChStatsTotPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,1),_WlsrChStatsTotPktsAt1Mbps_Type())
wlsrChStatsTotPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt1Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt1Mbps_Type=Counter32
_WlsrChStatsTotBytesAt1Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt1Mbps=_WlsrChStatsTotBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,2),_WlsrChStatsTotBytesAt1Mbps_Type())
wlsrChStatsTotBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt1Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt2Mbps_Type=Counter32
_WlsrChStatsTotPktsAt2Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt2Mbps=_WlsrChStatsTotPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,3),_WlsrChStatsTotPktsAt2Mbps_Type())
wlsrChStatsTotPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt2Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt2Mbps_Type=Counter32
_WlsrChStatsTotBytesAt2Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt2Mbps=_WlsrChStatsTotBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,4),_WlsrChStatsTotBytesAt2Mbps_Type())
wlsrChStatsTotBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt2Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt5Mbps_Type=Counter32
_WlsrChStatsTotPktsAt5Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt5Mbps=_WlsrChStatsTotPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,5),_WlsrChStatsTotPktsAt5Mbps_Type())
wlsrChStatsTotPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt5Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt5Mbps_Type=Counter32
_WlsrChStatsTotBytesAt5Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt5Mbps=_WlsrChStatsTotBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,6),_WlsrChStatsTotBytesAt5Mbps_Type())
wlsrChStatsTotBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt5Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt11Mbps_Type=Counter32
_WlsrChStatsTotPktsAt11Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt11Mbps=_WlsrChStatsTotPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,7),_WlsrChStatsTotPktsAt11Mbps_Type())
wlsrChStatsTotPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt11Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt11Mbps_Type=Counter32
_WlsrChStatsTotBytesAt11Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt11Mbps=_WlsrChStatsTotBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,8),_WlsrChStatsTotBytesAt11Mbps_Type())
wlsrChStatsTotBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt11Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt6Mbps_Type=Counter32
_WlsrChStatsTotPktsAt6Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt6Mbps=_WlsrChStatsTotPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,9),_WlsrChStatsTotPktsAt6Mbps_Type())
wlsrChStatsTotPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt6Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt6Mbps_Type=Counter32
_WlsrChStatsTotBytesAt6Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt6Mbps=_WlsrChStatsTotBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,10),_WlsrChStatsTotBytesAt6Mbps_Type())
wlsrChStatsTotBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt6Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt12Mbps_Type=Counter32
_WlsrChStatsTotPktsAt12Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt12Mbps=_WlsrChStatsTotPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,11),_WlsrChStatsTotPktsAt12Mbps_Type())
wlsrChStatsTotPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt12Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt12Mbps_Type=Counter32
_WlsrChStatsTotBytesAt12Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt12Mbps=_WlsrChStatsTotBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,12),_WlsrChStatsTotBytesAt12Mbps_Type())
wlsrChStatsTotBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt12Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt18Mbps_Type=Counter32
_WlsrChStatsTotPktsAt18Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt18Mbps=_WlsrChStatsTotPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,13),_WlsrChStatsTotPktsAt18Mbps_Type())
wlsrChStatsTotPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt18Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt18Mbps_Type=Counter32
_WlsrChStatsTotBytesAt18Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt18Mbps=_WlsrChStatsTotBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,14),_WlsrChStatsTotBytesAt18Mbps_Type())
wlsrChStatsTotBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt18Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt24Mbps_Type=Counter32
_WlsrChStatsTotPktsAt24Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt24Mbps=_WlsrChStatsTotPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,15),_WlsrChStatsTotPktsAt24Mbps_Type())
wlsrChStatsTotPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt24Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt24Mbps_Type=Counter32
_WlsrChStatsTotBytesAt24Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt24Mbps=_WlsrChStatsTotBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,16),_WlsrChStatsTotBytesAt24Mbps_Type())
wlsrChStatsTotBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt24Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt36Mbps_Type=Counter32
_WlsrChStatsTotPktsAt36Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt36Mbps=_WlsrChStatsTotPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,17),_WlsrChStatsTotPktsAt36Mbps_Type())
wlsrChStatsTotPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt36Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt36Mbps_Type=Counter32
_WlsrChStatsTotBytesAt36Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt36Mbps=_WlsrChStatsTotBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,18),_WlsrChStatsTotBytesAt36Mbps_Type())
wlsrChStatsTotBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt36Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt48Mbps_Type=Counter32
_WlsrChStatsTotPktsAt48Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt48Mbps=_WlsrChStatsTotPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,19),_WlsrChStatsTotPktsAt48Mbps_Type())
wlsrChStatsTotPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt48Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt48Mbps_Type=Counter32
_WlsrChStatsTotBytesAt48Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt48Mbps=_WlsrChStatsTotBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,20),_WlsrChStatsTotBytesAt48Mbps_Type())
wlsrChStatsTotBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt48Mbps.setStatus(_A)
_WlsrChStatsTotPktsAt54Mbps_Type=Counter32
_WlsrChStatsTotPktsAt54Mbps_Object=MibTableColumn
wlsrChStatsTotPktsAt54Mbps=_WlsrChStatsTotPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,21),_WlsrChStatsTotPktsAt54Mbps_Type())
wlsrChStatsTotPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotPktsAt54Mbps.setStatus(_A)
_WlsrChStatsTotBytesAt54Mbps_Type=Counter32
_WlsrChStatsTotBytesAt54Mbps_Object=MibTableColumn
wlsrChStatsTotBytesAt54Mbps=_WlsrChStatsTotBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,2,1,22),_WlsrChStatsTotBytesAt54Mbps_Type())
wlsrChStatsTotBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotBytesAt54Mbps.setStatus(_A)
_WlsrChannelDATypeStatsTable_Object=MibTable
wlsrChannelDATypeStatsTable=_WlsrChannelDATypeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3))
if mibBuilder.loadTexts:wlsrChannelDATypeStatsTable.setStatus(_A)
_WlsrChannelDATypeStatsEntry_Object=MibTableRow
wlsrChannelDATypeStatsEntry=_WlsrChannelDATypeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1))
wlsrChannelDATypeStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wlsrChannelDATypeStatsEntry.setStatus(_A)
_WlsrChStatsTotDABroadcastPkts_Type=Counter32
_WlsrChStatsTotDABroadcastPkts_Object=MibTableColumn
wlsrChStatsTotDABroadcastPkts=_WlsrChStatsTotDABroadcastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,1),_WlsrChStatsTotDABroadcastPkts_Type())
wlsrChStatsTotDABroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDABroadcastPkts.setStatus(_A)
_WlsrChStatsTotDABroadcastBytes_Type=Counter32
_WlsrChStatsTotDABroadcastBytes_Object=MibTableColumn
wlsrChStatsTotDABroadcastBytes=_WlsrChStatsTotDABroadcastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,2),_WlsrChStatsTotDABroadcastBytes_Type())
wlsrChStatsTotDABroadcastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDABroadcastBytes.setStatus(_A)
_WlsrChStatsTotDAMulticastPkts_Type=Counter32
_WlsrChStatsTotDAMulticastPkts_Object=MibTableColumn
wlsrChStatsTotDAMulticastPkts=_WlsrChStatsTotDAMulticastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,3),_WlsrChStatsTotDAMulticastPkts_Type())
wlsrChStatsTotDAMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDAMulticastPkts.setStatus(_A)
_WlsrChStatsTotDAMulticastBytes_Type=Counter32
_WlsrChStatsTotDAMulticastBytes_Object=MibTableColumn
wlsrChStatsTotDAMulticastBytes=_WlsrChStatsTotDAMulticastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,4),_WlsrChStatsTotDAMulticastBytes_Type())
wlsrChStatsTotDAMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDAMulticastBytes.setStatus(_A)
_WlsrChStatsTotDAUnicastPkts_Type=Counter32
_WlsrChStatsTotDAUnicastPkts_Object=MibTableColumn
wlsrChStatsTotDAUnicastPkts=_WlsrChStatsTotDAUnicastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,5),_WlsrChStatsTotDAUnicastPkts_Type())
wlsrChStatsTotDAUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDAUnicastPkts.setStatus(_A)
_WlsrChStatsTotDAUnicastBytes_Type=Counter32
_WlsrChStatsTotDAUnicastBytes_Object=MibTableColumn
wlsrChStatsTotDAUnicastBytes=_WlsrChStatsTotDAUnicastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,3,1,6),_WlsrChStatsTotDAUnicastBytes_Type())
wlsrChStatsTotDAUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDAUnicastBytes.setStatus(_A)
_WlsrChannelFrameTypeStatsTable_Object=MibTable
wlsrChannelFrameTypeStatsTable=_WlsrChannelFrameTypeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4))
if mibBuilder.loadTexts:wlsrChannelFrameTypeStatsTable.setStatus(_A)
_WlsrChannelFrameTypeStatsEntry_Object=MibTableRow
wlsrChannelFrameTypeStatsEntry=_WlsrChannelFrameTypeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1))
wlsrChannelFrameTypeStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wlsrChannelFrameTypeStatsEntry.setStatus(_A)
_WlsrChStatsTotMgmtPkts_Type=Counter32
_WlsrChStatsTotMgmtPkts_Object=MibTableColumn
wlsrChStatsTotMgmtPkts=_WlsrChStatsTotMgmtPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,1),_WlsrChStatsTotMgmtPkts_Type())
wlsrChStatsTotMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotMgmtPkts.setStatus(_A)
_WlsrChStatsTotMgmtBytes_Type=Counter32
_WlsrChStatsTotMgmtBytes_Object=MibTableColumn
wlsrChStatsTotMgmtBytes=_WlsrChStatsTotMgmtBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,2),_WlsrChStatsTotMgmtBytes_Type())
wlsrChStatsTotMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotMgmtBytes.setStatus(_A)
_WlsrChStatsTotCtrlPkts_Type=Counter32
_WlsrChStatsTotCtrlPkts_Object=MibTableColumn
wlsrChStatsTotCtrlPkts=_WlsrChStatsTotCtrlPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,3),_WlsrChStatsTotCtrlPkts_Type())
wlsrChStatsTotCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotCtrlPkts.setStatus(_A)
_WlsrChStatsTotCtrlBytes_Type=Counter32
_WlsrChStatsTotCtrlBytes_Object=MibTableColumn
wlsrChStatsTotCtrlBytes=_WlsrChStatsTotCtrlBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,4),_WlsrChStatsTotCtrlBytes_Type())
wlsrChStatsTotCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotCtrlBytes.setStatus(_A)
_WlsrChStatsTotDataPkts_Type=Counter32
_WlsrChStatsTotDataPkts_Object=MibTableColumn
wlsrChStatsTotDataPkts=_WlsrChStatsTotDataPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,5),_WlsrChStatsTotDataPkts_Type())
wlsrChStatsTotDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDataPkts.setStatus(_A)
_WlsrChStatsTotDataBytes_Type=Counter32
_WlsrChStatsTotDataBytes_Object=MibTableColumn
wlsrChStatsTotDataBytes=_WlsrChStatsTotDataBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,4,1,6),_WlsrChStatsTotDataBytes_Type())
wlsrChStatsTotDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsTotDataBytes.setStatus(_A)
_WlsrChannelPktSizeStatsTable_Object=MibTable
wlsrChannelPktSizeStatsTable=_WlsrChannelPktSizeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5))
if mibBuilder.loadTexts:wlsrChannelPktSizeStatsTable.setStatus(_A)
_WlsrChannelPktSizeStatsEntry_Object=MibTableRow
wlsrChannelPktSizeStatsEntry=_WlsrChannelPktSizeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1))
wlsrChannelPktSizeStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:wlsrChannelPktSizeStatsEntry.setStatus(_A)
_WlsrChStatsPkts63Bytes_Type=Counter32
_WlsrChStatsPkts63Bytes_Object=MibTableColumn
wlsrChStatsPkts63Bytes=_WlsrChStatsPkts63Bytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,1),_WlsrChStatsPkts63Bytes_Type())
wlsrChStatsPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts63Bytes.setStatus(_A)
_WlsrChStatsPkts64To127_Type=Counter32
_WlsrChStatsPkts64To127_Object=MibTableColumn
wlsrChStatsPkts64To127=_WlsrChStatsPkts64To127_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,2),_WlsrChStatsPkts64To127_Type())
wlsrChStatsPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts64To127.setStatus(_A)
_WlsrChStatsPkts128To255_Type=Counter32
_WlsrChStatsPkts128To255_Object=MibTableColumn
wlsrChStatsPkts128To255=_WlsrChStatsPkts128To255_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,3),_WlsrChStatsPkts128To255_Type())
wlsrChStatsPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts128To255.setStatus(_A)
_WlsrChStatsPkts256To511_Type=Counter32
_WlsrChStatsPkts256To511_Object=MibTableColumn
wlsrChStatsPkts256To511=_WlsrChStatsPkts256To511_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,4),_WlsrChStatsPkts256To511_Type())
wlsrChStatsPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts256To511.setStatus(_A)
_WlsrChStatsPkts512To1023_Type=Counter32
_WlsrChStatsPkts512To1023_Object=MibTableColumn
wlsrChStatsPkts512To1023=_WlsrChStatsPkts512To1023_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,5),_WlsrChStatsPkts512To1023_Type())
wlsrChStatsPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts512To1023.setStatus(_A)
_WlsrChStatsPkts1024To1518_Type=Counter32
_WlsrChStatsPkts1024To1518_Object=MibTableColumn
wlsrChStatsPkts1024To1518=_WlsrChStatsPkts1024To1518_Object((1,3,6,1,4,1,14823,2,3,1,1,3,3,5,1,6),_WlsrChStatsPkts1024To1518_Type())
wlsrChStatsPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrChStatsPkts1024To1518.setStatus(_A)
_WlsrStatsStaGroup_ObjectIdentity=ObjectIdentity
wlsrStatsStaGroup=_WlsrStatsStaGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,3,4))
_WlsrStaStatsTable_Object=MibTable
wlsrStaStatsTable=_WlsrStaStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1))
if mibBuilder.loadTexts:wlsrStaStatsTable.setStatus(_A)
_WlsrStaStatsEntry_Object=MibTableRow
wlsrStaStatsEntry=_WlsrStaStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1))
wlsrStaStatsEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:wlsrStaStatsEntry.setStatus(_A)
_WlsrStaAddress_Type=MacAddress
_WlsrStaAddress_Object=MibTableColumn
wlsrStaAddress=_WlsrStaAddress_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,1),_WlsrStaAddress_Type())
wlsrStaAddress.setMaxAccess(_Q)
if mibBuilder.loadTexts:wlsrStaAddress.setStatus(_A)
_WlsrStaTxPkts_Type=Counter32
_WlsrStaTxPkts_Object=MibTableColumn
wlsrStaTxPkts=_WlsrStaTxPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,2),_WlsrStaTxPkts_Type())
wlsrStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts.setStatus(_A)
_WlsrStaTxBytes_Type=Counter32
_WlsrStaTxBytes_Object=MibTableColumn
wlsrStaTxBytes=_WlsrStaTxBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,3),_WlsrStaTxBytes_Type())
wlsrStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytes.setStatus(_A)
_WlsrStaRxPkts_Type=Counter32
_WlsrStaRxPkts_Object=MibTableColumn
wlsrStaRxPkts=_WlsrStaRxPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,4),_WlsrStaRxPkts_Type())
wlsrStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts.setStatus(_A)
_WlsrStaRxBytes_Type=Counter32
_WlsrStaRxBytes_Object=MibTableColumn
wlsrStaRxBytes=_WlsrStaRxBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,5),_WlsrStaRxBytes_Type())
wlsrStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytes.setStatus(_A)
_WlsrStaTxRetryPkts_Type=Counter32
_WlsrStaTxRetryPkts_Object=MibTableColumn
wlsrStaTxRetryPkts=_WlsrStaTxRetryPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,6),_WlsrStaTxRetryPkts_Type())
wlsrStaTxRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxRetryPkts.setStatus(_A)
_WlsrStaRxRetryPkts_Type=Counter32
_WlsrStaRxRetryPkts_Object=MibTableColumn
wlsrStaRxRetryPkts=_WlsrStaRxRetryPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,7),_WlsrStaRxRetryPkts_Type())
wlsrStaRxRetryPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxRetryPkts.setStatus(_A)
_WlsrStaTxFragmentedPkts_Type=Counter32
_WlsrStaTxFragmentedPkts_Object=MibTableColumn
wlsrStaTxFragmentedPkts=_WlsrStaTxFragmentedPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,8),_WlsrStaTxFragmentedPkts_Type())
wlsrStaTxFragmentedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxFragmentedPkts.setStatus(_A)
_WlsrStaRxFragmentedPkts_Type=Counter32
_WlsrStaRxFragmentedPkts_Object=MibTableColumn
wlsrStaRxFragmentedPkts=_WlsrStaRxFragmentedPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,9),_WlsrStaRxFragmentedPkts_Type())
wlsrStaRxFragmentedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxFragmentedPkts.setStatus(_A)
_WlsrStaReceiveErrPkts_Type=Counter32
_WlsrStaReceiveErrPkts_Object=MibTableColumn
wlsrStaReceiveErrPkts=_WlsrStaReceiveErrPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,10),_WlsrStaReceiveErrPkts_Type())
wlsrStaReceiveErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaReceiveErrPkts.setStatus(_A)
_WlsrStaTxTotSignal_Type=Integer32
_WlsrStaTxTotSignal_Object=MibTableColumn
wlsrStaTxTotSignal=_WlsrStaTxTotSignal_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,11),_WlsrStaTxTotSignal_Type())
wlsrStaTxTotSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxTotSignal.setStatus(_A)
_WlsrStaTxSignalPkts_Type=Counter32
_WlsrStaTxSignalPkts_Object=MibTableColumn
wlsrStaTxSignalPkts=_WlsrStaTxSignalPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,12),_WlsrStaTxSignalPkts_Type())
wlsrStaTxSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxSignalPkts.setStatus(_A)
_WlsrStaTxCurSignal_Type=Integer32
_WlsrStaTxCurSignal_Object=MibTableColumn
wlsrStaTxCurSignal=_WlsrStaTxCurSignal_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,13),_WlsrStaTxCurSignal_Type())
wlsrStaTxCurSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxCurSignal.setStatus(_A)
_WlsrStaTxHighSignal_Type=Integer32
_WlsrStaTxHighSignal_Object=MibTableColumn
wlsrStaTxHighSignal=_WlsrStaTxHighSignal_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,14),_WlsrStaTxHighSignal_Type())
wlsrStaTxHighSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxHighSignal.setStatus(_A)
_WlsrStaRxTotNoise_Type=Counter32
_WlsrStaRxTotNoise_Object=MibTableColumn
wlsrStaRxTotNoise=_WlsrStaRxTotNoise_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,15),_WlsrStaRxTotNoise_Type())
wlsrStaRxTotNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxTotNoise.setStatus(_L)
_WlsrStaRxNoisePkts_Type=Counter32
_WlsrStaRxNoisePkts_Object=MibTableColumn
wlsrStaRxNoisePkts=_WlsrStaRxNoisePkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,16),_WlsrStaRxNoisePkts_Type())
wlsrStaRxNoisePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxNoisePkts.setStatus(_L)
_WlsrStaRxCurrentNoise_Type=Integer32
_WlsrStaRxCurrentNoise_Object=MibTableColumn
wlsrStaRxCurrentNoise=_WlsrStaRxCurrentNoise_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,17),_WlsrStaRxCurrentNoise_Type())
wlsrStaRxCurrentNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxCurrentNoise.setStatus(_L)
_WlsrStaRxHighNoise_Type=Integer32
_WlsrStaRxHighNoise_Object=MibTableColumn
wlsrStaRxHighNoise=_WlsrStaRxHighNoise_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,18),_WlsrStaRxHighNoise_Type())
wlsrStaRxHighNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxHighNoise.setStatus(_L)
_WlsrStaRxLowNoise_Type=Integer32
_WlsrStaRxLowNoise_Object=MibTableColumn
wlsrStaRxLowNoise=_WlsrStaRxLowNoise_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,19),_WlsrStaRxLowNoise_Type())
wlsrStaRxLowNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxLowNoise.setStatus(_L)
_WlsrStaFrameRetryRate_Type=Integer32
_WlsrStaFrameRetryRate_Object=MibTableColumn
wlsrStaFrameRetryRate=_WlsrStaFrameRetryRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,20),_WlsrStaFrameRetryRate_Type())
wlsrStaFrameRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameRetryRate.setStatus(_A)
_WlsrStaFrameLowSpeedRate_Type=Integer32
_WlsrStaFrameLowSpeedRate_Object=MibTableColumn
wlsrStaFrameLowSpeedRate=_WlsrStaFrameLowSpeedRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,21),_WlsrStaFrameLowSpeedRate_Type())
wlsrStaFrameLowSpeedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameLowSpeedRate.setStatus(_A)
_WlsrStaFrameNonUnicastRate_Type=Integer32
_WlsrStaFrameNonUnicastRate_Object=MibTableColumn
wlsrStaFrameNonUnicastRate=_WlsrStaFrameNonUnicastRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,22),_WlsrStaFrameNonUnicastRate_Type())
wlsrStaFrameNonUnicastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameNonUnicastRate.setStatus(_A)
_WlsrStaFrameRetryErrorRate_Type=Integer32
_WlsrStaFrameRetryErrorRate_Object=MibTableColumn
wlsrStaFrameRetryErrorRate=_WlsrStaFrameRetryErrorRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,23),_WlsrStaFrameRetryErrorRate_Type())
wlsrStaFrameRetryErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameRetryErrorRate.setStatus(_A)
_WlsrStaFrameBandwidthRate_Type=Integer32
_WlsrStaFrameBandwidthRate_Object=MibTableColumn
wlsrStaFrameBandwidthRate=_WlsrStaFrameBandwidthRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,24),_WlsrStaFrameBandwidthRate_Type())
wlsrStaFrameBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameBandwidthRate.setStatus(_A)
_WlsrStaFrameFragmentationRate_Type=Integer32
_WlsrStaFrameFragmentationRate_Object=MibTableColumn
wlsrStaFrameFragmentationRate=_WlsrStaFrameFragmentationRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,25),_WlsrStaFrameFragmentationRate_Type())
wlsrStaFrameFragmentationRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameFragmentationRate.setStatus(_A)
_WlsrStaFrameHighBandwidthRate_Type=Integer32
_WlsrStaFrameHighBandwidthRate_Object=MibTableColumn
wlsrStaFrameHighBandwidthRate=_WlsrStaFrameHighBandwidthRate_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,1,1,26),_WlsrStaFrameHighBandwidthRate_Type())
wlsrStaFrameHighBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaFrameHighBandwidthRate.setStatus(_A)
_WlsrStaRateStatsTable_Object=MibTable
wlsrStaRateStatsTable=_WlsrStaRateStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2))
if mibBuilder.loadTexts:wlsrStaRateStatsTable.setStatus(_A)
_WlsrStaRateStatsEntry_Object=MibTableRow
wlsrStaRateStatsEntry=_WlsrStaRateStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1))
wlsrStaRateStatsEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:wlsrStaRateStatsEntry.setStatus(_A)
_WlsrStaTxPktsAt1Mbps_Type=Counter32
_WlsrStaTxPktsAt1Mbps_Object=MibTableColumn
wlsrStaTxPktsAt1Mbps=_WlsrStaTxPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,1),_WlsrStaTxPktsAt1Mbps_Type())
wlsrStaTxPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt1Mbps.setStatus(_A)
_WlsrStaTxBytesAt1Mbps_Type=Counter32
_WlsrStaTxBytesAt1Mbps_Object=MibTableColumn
wlsrStaTxBytesAt1Mbps=_WlsrStaTxBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,2),_WlsrStaTxBytesAt1Mbps_Type())
wlsrStaTxBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt1Mbps.setStatus(_A)
_WlsrStaTxPktsAt2Mbps_Type=Counter32
_WlsrStaTxPktsAt2Mbps_Object=MibTableColumn
wlsrStaTxPktsAt2Mbps=_WlsrStaTxPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,3),_WlsrStaTxPktsAt2Mbps_Type())
wlsrStaTxPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt2Mbps.setStatus(_A)
_WlsrStaTxBytesAt2Mbps_Type=Counter32
_WlsrStaTxBytesAt2Mbps_Object=MibTableColumn
wlsrStaTxBytesAt2Mbps=_WlsrStaTxBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,4),_WlsrStaTxBytesAt2Mbps_Type())
wlsrStaTxBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt2Mbps.setStatus(_A)
_WlsrStaTxPktsAt5Mbps_Type=Counter32
_WlsrStaTxPktsAt5Mbps_Object=MibTableColumn
wlsrStaTxPktsAt5Mbps=_WlsrStaTxPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,5),_WlsrStaTxPktsAt5Mbps_Type())
wlsrStaTxPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt5Mbps.setStatus(_A)
_WlsrStaTxBytesAt5Mbps_Type=Counter32
_WlsrStaTxBytesAt5Mbps_Object=MibTableColumn
wlsrStaTxBytesAt5Mbps=_WlsrStaTxBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,6),_WlsrStaTxBytesAt5Mbps_Type())
wlsrStaTxBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt5Mbps.setStatus(_A)
_WlsrStaTxPktsAt11Mbps_Type=Counter32
_WlsrStaTxPktsAt11Mbps_Object=MibTableColumn
wlsrStaTxPktsAt11Mbps=_WlsrStaTxPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,7),_WlsrStaTxPktsAt11Mbps_Type())
wlsrStaTxPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt11Mbps.setStatus(_A)
_WlsrStaTxBytesAt11Mbps_Type=Counter32
_WlsrStaTxBytesAt11Mbps_Object=MibTableColumn
wlsrStaTxBytesAt11Mbps=_WlsrStaTxBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,8),_WlsrStaTxBytesAt11Mbps_Type())
wlsrStaTxBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt11Mbps.setStatus(_A)
_WlsrStaTxPktsAt6Mbps_Type=Counter32
_WlsrStaTxPktsAt6Mbps_Object=MibTableColumn
wlsrStaTxPktsAt6Mbps=_WlsrStaTxPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,9),_WlsrStaTxPktsAt6Mbps_Type())
wlsrStaTxPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt6Mbps.setStatus(_A)
_WlsrStaTxBytesAt6Mbps_Type=Counter32
_WlsrStaTxBytesAt6Mbps_Object=MibTableColumn
wlsrStaTxBytesAt6Mbps=_WlsrStaTxBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,10),_WlsrStaTxBytesAt6Mbps_Type())
wlsrStaTxBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt6Mbps.setStatus(_A)
_WlsrStaTxPktsAt12Mbps_Type=Counter32
_WlsrStaTxPktsAt12Mbps_Object=MibTableColumn
wlsrStaTxPktsAt12Mbps=_WlsrStaTxPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,11),_WlsrStaTxPktsAt12Mbps_Type())
wlsrStaTxPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt12Mbps.setStatus(_A)
_WlsrStaTxBytesAt12Mbps_Type=Counter32
_WlsrStaTxBytesAt12Mbps_Object=MibTableColumn
wlsrStaTxBytesAt12Mbps=_WlsrStaTxBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,12),_WlsrStaTxBytesAt12Mbps_Type())
wlsrStaTxBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt12Mbps.setStatus(_A)
_WlsrStaTxPktsAt18Mbps_Type=Counter32
_WlsrStaTxPktsAt18Mbps_Object=MibTableColumn
wlsrStaTxPktsAt18Mbps=_WlsrStaTxPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,13),_WlsrStaTxPktsAt18Mbps_Type())
wlsrStaTxPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt18Mbps.setStatus(_A)
_WlsrStaTxBytesAt18Mbps_Type=Counter32
_WlsrStaTxBytesAt18Mbps_Object=MibTableColumn
wlsrStaTxBytesAt18Mbps=_WlsrStaTxBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,14),_WlsrStaTxBytesAt18Mbps_Type())
wlsrStaTxBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt18Mbps.setStatus(_A)
_WlsrStaTxPktsAt24Mbps_Type=Counter32
_WlsrStaTxPktsAt24Mbps_Object=MibTableColumn
wlsrStaTxPktsAt24Mbps=_WlsrStaTxPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,15),_WlsrStaTxPktsAt24Mbps_Type())
wlsrStaTxPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt24Mbps.setStatus(_A)
_WlsrStaTxBytesAt24Mbps_Type=Counter32
_WlsrStaTxBytesAt24Mbps_Object=MibTableColumn
wlsrStaTxBytesAt24Mbps=_WlsrStaTxBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,16),_WlsrStaTxBytesAt24Mbps_Type())
wlsrStaTxBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt24Mbps.setStatus(_A)
_WlsrStaTxPktsAt36Mbps_Type=Counter32
_WlsrStaTxPktsAt36Mbps_Object=MibTableColumn
wlsrStaTxPktsAt36Mbps=_WlsrStaTxPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,17),_WlsrStaTxPktsAt36Mbps_Type())
wlsrStaTxPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt36Mbps.setStatus(_A)
_WlsrStaTxBytesAt36Mbps_Type=Counter32
_WlsrStaTxBytesAt36Mbps_Object=MibTableColumn
wlsrStaTxBytesAt36Mbps=_WlsrStaTxBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,18),_WlsrStaTxBytesAt36Mbps_Type())
wlsrStaTxBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt36Mbps.setStatus(_A)
_WlsrStaTxPktsAt48Mbps_Type=Counter32
_WlsrStaTxPktsAt48Mbps_Object=MibTableColumn
wlsrStaTxPktsAt48Mbps=_WlsrStaTxPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,19),_WlsrStaTxPktsAt48Mbps_Type())
wlsrStaTxPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt48Mbps.setStatus(_A)
_WlsrStaTxBytesAt48Mbps_Type=Counter32
_WlsrStaTxBytesAt48Mbps_Object=MibTableColumn
wlsrStaTxBytesAt48Mbps=_WlsrStaTxBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,20),_WlsrStaTxBytesAt48Mbps_Type())
wlsrStaTxBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt48Mbps.setStatus(_A)
_WlsrStaTxPktsAt54Mbps_Type=Counter32
_WlsrStaTxPktsAt54Mbps_Object=MibTableColumn
wlsrStaTxPktsAt54Mbps=_WlsrStaTxPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,21),_WlsrStaTxPktsAt54Mbps_Type())
wlsrStaTxPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPktsAt54Mbps.setStatus(_A)
_WlsrStaTxBytesAt54Mbps_Type=Counter32
_WlsrStaTxBytesAt54Mbps_Object=MibTableColumn
wlsrStaTxBytesAt54Mbps=_WlsrStaTxBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,22),_WlsrStaTxBytesAt54Mbps_Type())
wlsrStaTxBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxBytesAt54Mbps.setStatus(_A)
_WlsrStaRxPktsAt1Mbps_Type=Counter32
_WlsrStaRxPktsAt1Mbps_Object=MibTableColumn
wlsrStaRxPktsAt1Mbps=_WlsrStaRxPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,23),_WlsrStaRxPktsAt1Mbps_Type())
wlsrStaRxPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt1Mbps.setStatus(_A)
_WlsrStaRxBytesAt1Mbps_Type=Counter32
_WlsrStaRxBytesAt1Mbps_Object=MibTableColumn
wlsrStaRxBytesAt1Mbps=_WlsrStaRxBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,24),_WlsrStaRxBytesAt1Mbps_Type())
wlsrStaRxBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt1Mbps.setStatus(_A)
_WlsrStaRxPktsAt2Mbps_Type=Counter32
_WlsrStaRxPktsAt2Mbps_Object=MibTableColumn
wlsrStaRxPktsAt2Mbps=_WlsrStaRxPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,25),_WlsrStaRxPktsAt2Mbps_Type())
wlsrStaRxPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt2Mbps.setStatus(_A)
_WlsrStaRxBytesAt2Mbps_Type=Counter32
_WlsrStaRxBytesAt2Mbps_Object=MibTableColumn
wlsrStaRxBytesAt2Mbps=_WlsrStaRxBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,26),_WlsrStaRxBytesAt2Mbps_Type())
wlsrStaRxBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt2Mbps.setStatus(_A)
_WlsrStaRxPktsAt5Mbps_Type=Counter32
_WlsrStaRxPktsAt5Mbps_Object=MibTableColumn
wlsrStaRxPktsAt5Mbps=_WlsrStaRxPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,27),_WlsrStaRxPktsAt5Mbps_Type())
wlsrStaRxPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt5Mbps.setStatus(_A)
_WlsrStaRxBytesAt5Mbps_Type=Counter32
_WlsrStaRxBytesAt5Mbps_Object=MibTableColumn
wlsrStaRxBytesAt5Mbps=_WlsrStaRxBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,28),_WlsrStaRxBytesAt5Mbps_Type())
wlsrStaRxBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt5Mbps.setStatus(_A)
_WlsrStaRxPktsAt11Mbps_Type=Counter32
_WlsrStaRxPktsAt11Mbps_Object=MibTableColumn
wlsrStaRxPktsAt11Mbps=_WlsrStaRxPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,29),_WlsrStaRxPktsAt11Mbps_Type())
wlsrStaRxPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt11Mbps.setStatus(_A)
_WlsrStaRxBytesAt11Mbps_Type=Counter32
_WlsrStaRxBytesAt11Mbps_Object=MibTableColumn
wlsrStaRxBytesAt11Mbps=_WlsrStaRxBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,30),_WlsrStaRxBytesAt11Mbps_Type())
wlsrStaRxBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt11Mbps.setStatus(_A)
_WlsrStaRxPktsAt6Mbps_Type=Counter32
_WlsrStaRxPktsAt6Mbps_Object=MibTableColumn
wlsrStaRxPktsAt6Mbps=_WlsrStaRxPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,31),_WlsrStaRxPktsAt6Mbps_Type())
wlsrStaRxPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt6Mbps.setStatus(_A)
_WlsrStaRxBytesAt6Mbps_Type=Counter32
_WlsrStaRxBytesAt6Mbps_Object=MibTableColumn
wlsrStaRxBytesAt6Mbps=_WlsrStaRxBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,32),_WlsrStaRxBytesAt6Mbps_Type())
wlsrStaRxBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt6Mbps.setStatus(_A)
_WlsrStaRxPktsAt12Mbps_Type=Counter32
_WlsrStaRxPktsAt12Mbps_Object=MibTableColumn
wlsrStaRxPktsAt12Mbps=_WlsrStaRxPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,33),_WlsrStaRxPktsAt12Mbps_Type())
wlsrStaRxPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt12Mbps.setStatus(_A)
_WlsrStaRxBytesAt12Mbps_Type=Counter32
_WlsrStaRxBytesAt12Mbps_Object=MibTableColumn
wlsrStaRxBytesAt12Mbps=_WlsrStaRxBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,34),_WlsrStaRxBytesAt12Mbps_Type())
wlsrStaRxBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt12Mbps.setStatus(_A)
_WlsrStaRxPktsAt18Mbps_Type=Counter32
_WlsrStaRxPktsAt18Mbps_Object=MibTableColumn
wlsrStaRxPktsAt18Mbps=_WlsrStaRxPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,35),_WlsrStaRxPktsAt18Mbps_Type())
wlsrStaRxPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt18Mbps.setStatus(_A)
_WlsrStaRxBytesAt18Mbps_Type=Counter32
_WlsrStaRxBytesAt18Mbps_Object=MibTableColumn
wlsrStaRxBytesAt18Mbps=_WlsrStaRxBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,36),_WlsrStaRxBytesAt18Mbps_Type())
wlsrStaRxBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt18Mbps.setStatus(_A)
_WlsrStaRxPktsAt24Mbps_Type=Counter32
_WlsrStaRxPktsAt24Mbps_Object=MibTableColumn
wlsrStaRxPktsAt24Mbps=_WlsrStaRxPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,37),_WlsrStaRxPktsAt24Mbps_Type())
wlsrStaRxPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt24Mbps.setStatus(_A)
_WlsrStaRxBytesAt24Mbps_Type=Counter32
_WlsrStaRxBytesAt24Mbps_Object=MibTableColumn
wlsrStaRxBytesAt24Mbps=_WlsrStaRxBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,38),_WlsrStaRxBytesAt24Mbps_Type())
wlsrStaRxBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt24Mbps.setStatus(_A)
_WlsrStaRxPktsAt36Mbps_Type=Counter32
_WlsrStaRxPktsAt36Mbps_Object=MibTableColumn
wlsrStaRxPktsAt36Mbps=_WlsrStaRxPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,39),_WlsrStaRxPktsAt36Mbps_Type())
wlsrStaRxPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt36Mbps.setStatus(_A)
_WlsrStaRxBytesAt36Mbps_Type=Counter32
_WlsrStaRxBytesAt36Mbps_Object=MibTableColumn
wlsrStaRxBytesAt36Mbps=_WlsrStaRxBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,40),_WlsrStaRxBytesAt36Mbps_Type())
wlsrStaRxBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt36Mbps.setStatus(_A)
_WlsrStaRxPktsAt48Mbps_Type=Counter32
_WlsrStaRxPktsAt48Mbps_Object=MibTableColumn
wlsrStaRxPktsAt48Mbps=_WlsrStaRxPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,41),_WlsrStaRxPktsAt48Mbps_Type())
wlsrStaRxPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt48Mbps.setStatus(_A)
_WlsrStaRxBytesAt48Mbps_Type=Counter32
_WlsrStaRxBytesAt48Mbps_Object=MibTableColumn
wlsrStaRxBytesAt48Mbps=_WlsrStaRxBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,42),_WlsrStaRxBytesAt48Mbps_Type())
wlsrStaRxBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt48Mbps.setStatus(_A)
_WlsrStaRxPktsAt54Mbps_Type=Counter32
_WlsrStaRxPktsAt54Mbps_Object=MibTableColumn
wlsrStaRxPktsAt54Mbps=_WlsrStaRxPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,43),_WlsrStaRxPktsAt54Mbps_Type())
wlsrStaRxPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPktsAt54Mbps.setStatus(_A)
_WlsrStaRxBytesAt54Mbps_Type=Counter32
_WlsrStaRxBytesAt54Mbps_Object=MibTableColumn
wlsrStaRxBytesAt54Mbps=_WlsrStaRxBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,2,1,44),_WlsrStaRxBytesAt54Mbps_Type())
wlsrStaRxBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxBytesAt54Mbps.setStatus(_A)
_WlsrStaDATypeStatsTable_Object=MibTable
wlsrStaDATypeStatsTable=_WlsrStaDATypeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3))
if mibBuilder.loadTexts:wlsrStaDATypeStatsTable.setStatus(_A)
_WlsrStaDATypeStatsEntry_Object=MibTableRow
wlsrStaDATypeStatsEntry=_WlsrStaDATypeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1))
wlsrStaDATypeStatsEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:wlsrStaDATypeStatsEntry.setStatus(_A)
_WlsrStaTxDABroadcastPkts_Type=Counter32
_WlsrStaTxDABroadcastPkts_Object=MibTableColumn
wlsrStaTxDABroadcastPkts=_WlsrStaTxDABroadcastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,1),_WlsrStaTxDABroadcastPkts_Type())
wlsrStaTxDABroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDABroadcastPkts.setStatus(_A)
_WlsrStaTxDABroadcastBytes_Type=Counter32
_WlsrStaTxDABroadcastBytes_Object=MibTableColumn
wlsrStaTxDABroadcastBytes=_WlsrStaTxDABroadcastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,2),_WlsrStaTxDABroadcastBytes_Type())
wlsrStaTxDABroadcastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDABroadcastBytes.setStatus(_A)
_WlsrStaTxDAMulticastPkts_Type=Counter32
_WlsrStaTxDAMulticastPkts_Object=MibTableColumn
wlsrStaTxDAMulticastPkts=_WlsrStaTxDAMulticastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,3),_WlsrStaTxDAMulticastPkts_Type())
wlsrStaTxDAMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDAMulticastPkts.setStatus(_A)
_WlsrStaTxDAMulticastBytes_Type=Counter32
_WlsrStaTxDAMulticastBytes_Object=MibTableColumn
wlsrStaTxDAMulticastBytes=_WlsrStaTxDAMulticastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,4),_WlsrStaTxDAMulticastBytes_Type())
wlsrStaTxDAMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDAMulticastBytes.setStatus(_A)
_WlsrStaTxDAUnicastPkts_Type=Counter32
_WlsrStaTxDAUnicastPkts_Object=MibTableColumn
wlsrStaTxDAUnicastPkts=_WlsrStaTxDAUnicastPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,5),_WlsrStaTxDAUnicastPkts_Type())
wlsrStaTxDAUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDAUnicastPkts.setStatus(_A)
_WlsrStaTxDAUnicastBytes_Type=Counter32
_WlsrStaTxDAUnicastBytes_Object=MibTableColumn
wlsrStaTxDAUnicastBytes=_WlsrStaTxDAUnicastBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,3,1,6),_WlsrStaTxDAUnicastBytes_Type())
wlsrStaTxDAUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDAUnicastBytes.setStatus(_A)
_WlsrStaFrameTypeStatsTable_Object=MibTable
wlsrStaFrameTypeStatsTable=_WlsrStaFrameTypeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4))
if mibBuilder.loadTexts:wlsrStaFrameTypeStatsTable.setStatus(_A)
_WlsrStaFrameTypeStatsEntry_Object=MibTableRow
wlsrStaFrameTypeStatsEntry=_WlsrStaFrameTypeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1))
wlsrStaFrameTypeStatsEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:wlsrStaFrameTypeStatsEntry.setStatus(_A)
_WlsrStaTxMgmtPkts_Type=Counter32
_WlsrStaTxMgmtPkts_Object=MibTableColumn
wlsrStaTxMgmtPkts=_WlsrStaTxMgmtPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,1),_WlsrStaTxMgmtPkts_Type())
wlsrStaTxMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxMgmtPkts.setStatus(_A)
_WlsrStaTxMgmtBytes_Type=Counter32
_WlsrStaTxMgmtBytes_Object=MibTableColumn
wlsrStaTxMgmtBytes=_WlsrStaTxMgmtBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,2),_WlsrStaTxMgmtBytes_Type())
wlsrStaTxMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxMgmtBytes.setStatus(_A)
_WlsrStaTxCtrlPkts_Type=Counter32
_WlsrStaTxCtrlPkts_Object=MibTableColumn
wlsrStaTxCtrlPkts=_WlsrStaTxCtrlPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,3),_WlsrStaTxCtrlPkts_Type())
wlsrStaTxCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxCtrlPkts.setStatus(_A)
_WlsrStaTxCtrlBytes_Type=Counter32
_WlsrStaTxCtrlBytes_Object=MibTableColumn
wlsrStaTxCtrlBytes=_WlsrStaTxCtrlBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,4),_WlsrStaTxCtrlBytes_Type())
wlsrStaTxCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxCtrlBytes.setStatus(_A)
_WlsrStaTxDataPkts_Type=Counter32
_WlsrStaTxDataPkts_Object=MibTableColumn
wlsrStaTxDataPkts=_WlsrStaTxDataPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,5),_WlsrStaTxDataPkts_Type())
wlsrStaTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDataPkts.setStatus(_A)
_WlsrStaTxDataBytes_Type=Counter32
_WlsrStaTxDataBytes_Object=MibTableColumn
wlsrStaTxDataBytes=_WlsrStaTxDataBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,6),_WlsrStaTxDataBytes_Type())
wlsrStaTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxDataBytes.setStatus(_A)
_WlsrStaRxMgmtPkts_Type=Counter32
_WlsrStaRxMgmtPkts_Object=MibTableColumn
wlsrStaRxMgmtPkts=_WlsrStaRxMgmtPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,7),_WlsrStaRxMgmtPkts_Type())
wlsrStaRxMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxMgmtPkts.setStatus(_A)
_WlsrStaRxMgmtBytes_Type=Counter32
_WlsrStaRxMgmtBytes_Object=MibTableColumn
wlsrStaRxMgmtBytes=_WlsrStaRxMgmtBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,8),_WlsrStaRxMgmtBytes_Type())
wlsrStaRxMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxMgmtBytes.setStatus(_A)
_WlsrStaRxCtrlPkts_Type=Counter32
_WlsrStaRxCtrlPkts_Object=MibTableColumn
wlsrStaRxCtrlPkts=_WlsrStaRxCtrlPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,9),_WlsrStaRxCtrlPkts_Type())
wlsrStaRxCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxCtrlPkts.setStatus(_A)
_WlsrStaRxCtrlBytes_Type=Counter32
_WlsrStaRxCtrlBytes_Object=MibTableColumn
wlsrStaRxCtrlBytes=_WlsrStaRxCtrlBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,10),_WlsrStaRxCtrlBytes_Type())
wlsrStaRxCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxCtrlBytes.setStatus(_A)
_WlsrStaRxDataPkts_Type=Counter32
_WlsrStaRxDataPkts_Object=MibTableColumn
wlsrStaRxDataPkts=_WlsrStaRxDataPkts_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,11),_WlsrStaRxDataPkts_Type())
wlsrStaRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxDataPkts.setStatus(_A)
_WlsrStaRxDataBytes_Type=Counter32
_WlsrStaRxDataBytes_Object=MibTableColumn
wlsrStaRxDataBytes=_WlsrStaRxDataBytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,4,1,12),_WlsrStaRxDataBytes_Type())
wlsrStaRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxDataBytes.setStatus(_A)
_WlsrStaPktSizeStatsTable_Object=MibTable
wlsrStaPktSizeStatsTable=_WlsrStaPktSizeStatsTable_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5))
if mibBuilder.loadTexts:wlsrStaPktSizeStatsTable.setStatus(_A)
_WlsrStaPktSizeStatsEntry_Object=MibTableRow
wlsrStaPktSizeStatsEntry=_WlsrStaPktSizeStatsEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1))
wlsrStaPktSizeStatsEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:wlsrStaPktSizeStatsEntry.setStatus(_A)
_WlsrStaTxPkts63Bytes_Type=Counter32
_WlsrStaTxPkts63Bytes_Object=MibTableColumn
wlsrStaTxPkts63Bytes=_WlsrStaTxPkts63Bytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,1),_WlsrStaTxPkts63Bytes_Type())
wlsrStaTxPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts63Bytes.setStatus(_A)
_WlsrStaTxPkts64To127_Type=Counter32
_WlsrStaTxPkts64To127_Object=MibTableColumn
wlsrStaTxPkts64To127=_WlsrStaTxPkts64To127_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,2),_WlsrStaTxPkts64To127_Type())
wlsrStaTxPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts64To127.setStatus(_A)
_WlsrStaTxPkts128To255_Type=Counter32
_WlsrStaTxPkts128To255_Object=MibTableColumn
wlsrStaTxPkts128To255=_WlsrStaTxPkts128To255_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,3),_WlsrStaTxPkts128To255_Type())
wlsrStaTxPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts128To255.setStatus(_A)
_WlsrStaTxPkts256To511_Type=Counter32
_WlsrStaTxPkts256To511_Object=MibTableColumn
wlsrStaTxPkts256To511=_WlsrStaTxPkts256To511_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,4),_WlsrStaTxPkts256To511_Type())
wlsrStaTxPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts256To511.setStatus(_A)
_WlsrStaTxPkts512To1023_Type=Counter32
_WlsrStaTxPkts512To1023_Object=MibTableColumn
wlsrStaTxPkts512To1023=_WlsrStaTxPkts512To1023_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,5),_WlsrStaTxPkts512To1023_Type())
wlsrStaTxPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts512To1023.setStatus(_A)
_WlsrStaTxPkts1024To1518_Type=Counter32
_WlsrStaTxPkts1024To1518_Object=MibTableColumn
wlsrStaTxPkts1024To1518=_WlsrStaTxPkts1024To1518_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,6),_WlsrStaTxPkts1024To1518_Type())
wlsrStaTxPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaTxPkts1024To1518.setStatus(_A)
_WlsrStaRxPkts63Bytes_Type=Counter32
_WlsrStaRxPkts63Bytes_Object=MibTableColumn
wlsrStaRxPkts63Bytes=_WlsrStaRxPkts63Bytes_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,7),_WlsrStaRxPkts63Bytes_Type())
wlsrStaRxPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts63Bytes.setStatus(_A)
_WlsrStaRxPkts64To127_Type=Counter32
_WlsrStaRxPkts64To127_Object=MibTableColumn
wlsrStaRxPkts64To127=_WlsrStaRxPkts64To127_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,8),_WlsrStaRxPkts64To127_Type())
wlsrStaRxPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts64To127.setStatus(_A)
_WlsrStaRxPkts128To255_Type=Counter32
_WlsrStaRxPkts128To255_Object=MibTableColumn
wlsrStaRxPkts128To255=_WlsrStaRxPkts128To255_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,9),_WlsrStaRxPkts128To255_Type())
wlsrStaRxPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts128To255.setStatus(_A)
_WlsrStaRxPkts256To511_Type=Counter32
_WlsrStaRxPkts256To511_Object=MibTableColumn
wlsrStaRxPkts256To511=_WlsrStaRxPkts256To511_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,10),_WlsrStaRxPkts256To511_Type())
wlsrStaRxPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts256To511.setStatus(_A)
_WlsrStaRxPkts512To1023_Type=Counter32
_WlsrStaRxPkts512To1023_Object=MibTableColumn
wlsrStaRxPkts512To1023=_WlsrStaRxPkts512To1023_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,11),_WlsrStaRxPkts512To1023_Type())
wlsrStaRxPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts512To1023.setStatus(_A)
_WlsrStaRxPkts1024To1518_Type=Counter32
_WlsrStaRxPkts1024To1518_Object=MibTableColumn
wlsrStaRxPkts1024To1518=_WlsrStaRxPkts1024To1518_Object((1,3,6,1,4,1,14823,2,3,1,1,3,4,5,1,12),_WlsrStaRxPkts1024To1518_Type())
wlsrStaRxPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrStaRxPkts1024To1518.setStatus(_A)
_WlsrAirMonitorGroup_ObjectIdentity=ObjectIdentity
wlsrAirMonitorGroup=_WlsrAirMonitorGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,4))
_WlsrAirMonitorApListTable_Object=MibTable
wlsrAirMonitorApListTable=_WlsrAirMonitorApListTable_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1))
if mibBuilder.loadTexts:wlsrAirMonitorApListTable.setStatus(_A)
_WlsrAirMonitorApListEntry_Object=MibTableRow
wlsrAirMonitorApListEntry=_WlsrAirMonitorApListEntry_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1))
wlsrAirMonitorApListEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:wlsrAirMonitorApListEntry.setStatus(_A)
_WlsrAmApBSSID_Type=MacAddress
_WlsrAmApBSSID_Object=MibTableColumn
wlsrAmApBSSID=_WlsrAmApBSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,1),_WlsrAmApBSSID_Type())
wlsrAmApBSSID.setMaxAccess(_Q)
if mibBuilder.loadTexts:wlsrAmApBSSID.setStatus(_A)
class _WlsrAmSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_WlsrAmSSID_Type.__name__=_J
_WlsrAmSSID_Object=MibTableColumn
wlsrAmSSID=_WlsrAmSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,2),_WlsrAmSSID_Type())
wlsrAmSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmSSID.setStatus(_A)
class _WlsrAmChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,165))
_WlsrAmChannel_Type.__name__=_H
_WlsrAmChannel_Object=MibTableColumn
wlsrAmChannel=_WlsrAmChannel_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,3),_WlsrAmChannel_Type())
wlsrAmChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmChannel.setStatus(_A)
class _WlsrAmPhysicalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot11b',1),('dot11a',2),('dot11g',3)))
_WlsrAmPhysicalType_Type.__name__=_H
_WlsrAmPhysicalType_Object=MibTableColumn
wlsrAmPhysicalType=_WlsrAmPhysicalType_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,4),_WlsrAmPhysicalType_Type())
wlsrAmPhysicalType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmPhysicalType.setStatus(_A)
class _WlsrAmAccessPointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('genericAp',1),('softAp',2),('ciscoAp',3)))
_WlsrAmAccessPointType_Type.__name__=_H
_WlsrAmAccessPointType_Object=MibTableColumn
wlsrAmAccessPointType=_WlsrAmAccessPointType_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,5),_WlsrAmAccessPointType_Type())
wlsrAmAccessPointType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmAccessPointType.setStatus(_A)
class _WlsrAmRAPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('valid',1),('interfering',2),('unsecure',3),('dos',4),('unknown',5)))
_WlsrAmRAPType_Type.__name__=_H
_WlsrAmRAPType_Object=MibTableColumn
wlsrAmRAPType=_WlsrAmRAPType_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,6),_WlsrAmRAPType_Type())
wlsrAmRAPType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmRAPType.setStatus(_A)
_WlsrAmRSSI_Type=Integer32
_WlsrAmRSSI_Object=MibTableColumn
wlsrAmRSSI=_WlsrAmRSSI_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,7),_WlsrAmRSSI_Type())
wlsrAmRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmRSSI.setStatus(_A)
_WlsrAmMonitoredTime_Type=TimeTicks
_WlsrAmMonitoredTime_Object=MibTableColumn
wlsrAmMonitoredTime=_WlsrAmMonitoredTime_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,8),_WlsrAmMonitoredTime_Type())
wlsrAmMonitoredTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmMonitoredTime.setStatus(_A)
_WlsrAmInactivityTime_Type=TimeTicks
_WlsrAmInactivityTime_Object=MibTableColumn
wlsrAmInactivityTime=_WlsrAmInactivityTime_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,9),_WlsrAmInactivityTime_Type())
wlsrAmInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmInactivityTime.setStatus(_A)
class _WlsrAmLoadBalancing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_WlsrAmLoadBalancing_Type.__name__=_H
_WlsrAmLoadBalancing_Object=MibTableColumn
wlsrAmLoadBalancing=_WlsrAmLoadBalancing_Object((1,3,6,1,4,1,14823,2,3,1,1,4,1,1,10),_WlsrAmLoadBalancing_Type())
wlsrAmLoadBalancing.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAmLoadBalancing.setStatus(_A)
_WlsrTrapsGroup_ObjectIdentity=ObjectIdentity
wlsrTrapsGroup=_WlsrTrapsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,100))
_WlsrTrapObjectsGroup_ObjectIdentity=ObjectIdentity
wlsrTrapObjectsGroup=_WlsrTrapObjectsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,1,1,100,100))
_WlsrTargetApBSSID_Type=MacAddress
_WlsrTargetApBSSID_Object=MibScalar
wlsrTargetApBSSID=_WlsrTargetApBSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,1),_WlsrTargetApBSSID_Type())
wlsrTargetApBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTargetApBSSID.setStatus(_A)
class _WlsrTargetApSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsrTargetApSSID_Type.__name__=_J
_WlsrTargetApSSID_Object=MibScalar
wlsrTargetApSSID=_WlsrTargetApSSID_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,2),_WlsrTargetApSSID_Type())
wlsrTargetApSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTargetApSSID.setStatus(_A)
class _WlsrTargetApChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,165))
_WlsrTargetApChannel_Type.__name__=_H
_WlsrTargetApChannel_Object=MibScalar
wlsrTargetApChannel=_WlsrTargetApChannel_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,3),_WlsrTargetApChannel_Type())
wlsrTargetApChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTargetApChannel.setStatus(_A)
_WlsrSourceMac_Type=MacAddress
_WlsrSourceMac_Object=MibScalar
wlsrSourceMac=_WlsrSourceMac_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,4),_WlsrSourceMac_Type())
wlsrSourceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrSourceMac.setStatus(_A)
_WlsrNodeMac_Type=MacAddress
_WlsrNodeMac_Object=MibScalar
wlsrNodeMac=_WlsrNodeMac_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,5),_WlsrNodeMac_Type())
wlsrNodeMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrNodeMac.setStatus(_A)
class _WlsrFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,9,10,11,12,13)));namedValues=NamedValues(*(('associateRequest',1),('associateResponse',2),('reassociateRequest',3),('reassociateResponse',4),('probeRequest',5),('probeResponse',6),('beacon',9),('atim',10),('disassociate',11),('auth',12),('deauth',13)))
_WlsrFrameType_Type.__name__=_H
_WlsrFrameType_Object=MibScalar
wlsrFrameType=_WlsrFrameType_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,6),_WlsrFrameType_Type())
wlsrFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrFrameType.setStatus(_A)
class _WlsrAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('srcAddress',1),('dstAddress',2),('bssid',3)))
_WlsrAddressType_Type.__name__=_H
_WlsrAddressType_Object=MibScalar
wlsrAddressType=_WlsrAddressType_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,7),_WlsrAddressType_Type())
wlsrAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrAddressType.setStatus(_A)
class _WlsrSignatureName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsrSignatureName_Type.__name__=_a
_WlsrSignatureName_Object=MibScalar
wlsrSignatureName=_WlsrSignatureName_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,8),_WlsrSignatureName_Type())
wlsrSignatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrSignatureName.setStatus(_A)
_WlsrMatchedMac_Type=MacAddress
_WlsrMatchedMac_Object=MibScalar
wlsrMatchedMac=_WlsrMatchedMac_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,9),_WlsrMatchedMac_Type())
wlsrMatchedMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrMatchedMac.setStatus(_A)
_WlsrMatchedIp_Type=IpAddress
_WlsrMatchedIp_Object=MibScalar
wlsrMatchedIp=_WlsrMatchedIp_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,10),_WlsrMatchedIp_Type())
wlsrMatchedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrMatchedIp.setStatus(_A)
_WlsrReceiverMac_Type=MacAddress
_WlsrReceiverMac_Object=MibScalar
wlsrReceiverMac=_WlsrReceiverMac_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,11),_WlsrReceiverMac_Type())
wlsrReceiverMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrReceiverMac.setStatus(_A)
_WlsrTransmitterMac_Type=MacAddress
_WlsrTransmitterMac_Object=MibScalar
wlsrTransmitterMac=_WlsrTransmitterMac_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,12),_WlsrTransmitterMac_Type())
wlsrTransmitterMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrTransmitterMac.setStatus(_A)
_WlsrRSSI_Type=Integer32
_WlsrRSSI_Object=MibScalar
wlsrRSSI=_WlsrRSSI_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,13),_WlsrRSSI_Type())
wlsrRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrRSSI.setStatus(_A)
class _WlsrRogueInfoURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WlsrRogueInfoURL_Type.__name__=_J
_WlsrRogueInfoURL_Object=MibScalar
wlsrRogueInfoURL=_WlsrRogueInfoURL_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,14),_WlsrRogueInfoURL_Type())
wlsrRogueInfoURL.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrRogueInfoURL.setStatus(_A)
class _WlsrInterferingAPInfoURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WlsrInterferingAPInfoURL_Type.__name__=_J
_WlsrInterferingAPInfoURL_Object=MibScalar
wlsrInterferingAPInfoURL=_WlsrInterferingAPInfoURL_Object((1,3,6,1,4,1,14823,2,3,1,1,100,100,15),_WlsrInterferingAPInfoURL_Type())
wlsrInterferingAPInfoURL.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsrInterferingAPInfoURL.setStatus(_A)
wlsrUnsecureApDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1001))
wlsrUnsecureApDetected.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E),(_C,_p),(_C,_q),(_C,_Z)))
if mibBuilder.loadTexts:wlsrUnsecureApDetected.setStatus(_A)
wlsrStaImpersonation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1002))
wlsrStaImpersonation.setObjects(*((_C,_I),(_C,_D)))
if mibBuilder.loadTexts:wlsrStaImpersonation.setStatus(_A)
wlsrReservedChannelViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1003))
wlsrReservedChannelViolation.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrReservedChannelViolation.setStatus(_A)
wlsrValidSSIDViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1004))
wlsrValidSSIDViolation.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrValidSSIDViolation.setStatus(_A)
wlsrChannelMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1005))
wlsrChannelMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelMisconfiguration.setStatus(_A)
wlsrOUIMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1006))
wlsrOUIMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrOUIMisconfiguration.setStatus(_A)
wlsrSSIDMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1007))
wlsrSSIDMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrSSIDMisconfiguration.setStatus(_A)
wlsrShortPreableMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1008))
wlsrShortPreableMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrShortPreableMisconfiguration.setStatus(_A)
wlsrWPAMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1009))
wlsrWPAMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrWPAMisconfiguration.setStatus(_A)
wlsrAdhocNetworkDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1010))
wlsrAdhocNetworkDetected.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrAdhocNetworkDetected.setStatus(_A)
wlsrStaPolicyViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1011))
wlsrStaPolicyViolation.setObjects(*((_C,_F),(_C,_I),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrStaPolicyViolation.setStatus(_A)
wlsrRepeatWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1012))
wlsrRepeatWEPIVViolation.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrRepeatWEPIVViolation.setStatus(_A)
wlsrWeakWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1013))
wlsrWeakWEPIVViolation.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrWeakWEPIVViolation.setStatus(_A)
wlsrChannelInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1014))
wlsrChannelInterferenceDetected.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelInterferenceDetected.setStatus(_A)
wlsrAPInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1015))
wlsrAPInterferenceDetected.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrAPInterferenceDetected.setStatus(_A)
wlsrStaInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1016))
wlsrStaInterferenceDetected.setObjects(*((_C,_F),(_C,_G),(_C,_I),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrStaInterferenceDetected.setStatus(_A)
wlsrFrameRetryRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1017))
wlsrFrameRetryRateExceeded.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrFrameRetryRateExceeded.setStatus(_A)
wlsrFrameReceiveErrorRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1018))
wlsrFrameReceiveErrorRateExceeded.setObjects(*((_C,_F),(_C,_G),(_C,_R),(_C,_D)))
if mibBuilder.loadTexts:wlsrFrameReceiveErrorRateExceeded.setStatus(_A)
wlsrFrameFragmentationRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1019))
wlsrFrameFragmentationRateExceeded.setObjects(*((_C,_F),(_C,_G),(_C,_R),(_C,_D)))
if mibBuilder.loadTexts:wlsrFrameFragmentationRateExceeded.setStatus(_A)
wlsrFrameBandWidthRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1020))
wlsrFrameBandWidthRateExceeded.setObjects(*((_C,_I),(_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrFrameBandWidthRateExceeded.setStatus(_A)
wlsrFrameLowSpeedRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1021))
wlsrFrameLowSpeedRateExceeded.setObjects(*((_C,_I),(_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrFrameLowSpeedRateExceeded.setStatus(_A)
wlsrFrameNonUnicastRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1022))
wlsrFrameNonUnicastRateExceeded.setObjects(*((_C,_I),(_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrFrameNonUnicastRateExceeded.setStatus(_A)
wlsrLoadbalancingEnabled=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1023))
wlsrLoadbalancingEnabled.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrLoadbalancingEnabled.setStatus(_A)
wlsrChannelFrameRetryRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1024))
wlsrChannelFrameRetryRateExceeded.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelFrameRetryRateExceeded.setStatus(_A)
wlsrChannelFrameFragmentationRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1025))
wlsrChannelFrameFragmentationRateExceeded.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelFrameFragmentationRateExceeded.setStatus(_A)
wlsrChannelFrameErrorRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1026))
wlsrChannelFrameErrorRateExceeded.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelFrameErrorRateExceeded.setStatus(_A)
wlsrSignatureMatch=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1027))
wlsrSignatureMatch.setObjects(*((_C,_r),(_C,_O),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrSignatureMatch.setStatus(_A)
wlsrChannelRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1028))
wlsrChannelRateAnomaly.setObjects(*((_C,_S),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrChannelRateAnomaly.setStatus(_A)
wlsrNodeRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1029))
wlsrNodeRateAnomaly.setObjects(*((_C,_S),(_C,_I),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrNodeRateAnomaly.setStatus(_A)
wlsrEAPRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1030))
wlsrEAPRateAnomaly.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrEAPRateAnomaly.setStatus(_A)
wlsrSignalAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1031))
wlsrSignalAnomaly.setObjects(*((_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrSignalAnomaly.setStatus(_A)
wlsrSequenceNumberAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1032))
wlsrSequenceNumberAnomaly.setObjects(*((_C,_O),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrSequenceNumberAnomaly.setStatus(_A)
wlsrDisconnectStationAttack=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1033))
wlsrDisconnectStationAttack.setObjects(*((_C,_S),(_C,_O),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrDisconnectStationAttack.setStatus(_A)
wlsrApFloodAttack=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1034))
wlsrApFloodAttack.setObjects((_C,_D))
if mibBuilder.loadTexts:wlsrApFloodAttack.setStatus(_A)
wlsrAdhocNetwork=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1035))
wlsrAdhocNetwork.setObjects(*((_C,_O),(_C,_F),(_C,_G),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrAdhocNetwork.setStatus(_A)
wlsrWirelessBridge=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1036))
wlsrWirelessBridge.setObjects(*((_C,_s),(_C,_t),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrWirelessBridge.setStatus(_A)
wlsrInvalidMacOUI=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1037))
wlsrInvalidMacOUI.setObjects(*((_C,_u),(_C,_I),(_C,_K),(_C,_D)))
if mibBuilder.loadTexts:wlsrInvalidMacOUI.setStatus(_A)
wlsrLoadbalancingDisabled=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1038))
wlsrLoadbalancingDisabled.setObjects(*((_C,_F),(_C,_G),(_C,_R),(_C,_D)))
if mibBuilder.loadTexts:wlsrLoadbalancingDisabled.setStatus(_A)
wlsrWEPMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1039))
wlsrWEPMisconfiguration.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrWEPMisconfiguration.setStatus(_A)
wlsrStaRepeatWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1040))
wlsrStaRepeatWEPIVViolation.setObjects(*((_C,_F),(_C,_G),(_C,_I),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrStaRepeatWEPIVViolation.setStatus(_A)
wlsrStaWeakWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1041))
wlsrStaWeakWEPIVViolation.setObjects(*((_C,_F),(_C,_G),(_C,_I),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrStaWeakWEPIVViolation.setStatus(_A)
wlsrStaAssociatedToUnsecureAp=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1042))
wlsrStaAssociatedToUnsecureAp.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E),(_C,_I),(_C,_Z)))
if mibBuilder.loadTexts:wlsrStaAssociatedToUnsecureAp.setStatus(_A)
wlsrAdhocNetworkBridgeDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1043))
wlsrAdhocNetworkBridgeDetected.setObjects(*((_C,_O),(_C,_F),(_C,_G),(_C,_D),(_C,_E)))
if mibBuilder.loadTexts:wlsrAdhocNetworkBridgeDetected.setStatus(_A)
wlsrInterferingApDetected=NotificationType((1,3,6,1,4,1,14823,2,3,1,1,100,1044))
wlsrInterferingApDetected.setObjects(*((_C,_F),(_C,_G),(_C,_D),(_C,_E),(_C,_v)))
if mibBuilder.loadTexts:wlsrInterferingApDetected.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsrMIB':wlsrMIB,'wlsrConfigGroup':wlsrConfigGroup,'wlsrConfigTable':wlsrConfigTable,'wlsrConfigEntry':wlsrConfigEntry,_b:wlsrBSSID,'wlsrESSID':wlsrESSID,'wlsrMode':wlsrMode,_E:wlsrCurrentChannel,'wlsrTxPower':wlsrTxPower,'wlsrRTSThreshold':wlsrRTSThreshold,'wlsrRetryLimit':wlsrRetryLimit,'wlsrPreamble':wlsrPreamble,'wlsrBeaconInterval':wlsrBeaconInterval,'wlsrPowerMgmt':wlsrPowerMgmt,'wlsrLoadBalance':wlsrLoadBalance,'wlsrSupportedRates':wlsrSupportedRates,'wlsrDTIMPeriod':wlsrDTIMPeriod,'wlsrLMSAddress':wlsrLMSAddress,'wlsrEncryption':wlsrEncryption,'wlsrStatus':wlsrStatus,'wlsrAgeout':wlsrAgeout,'wlsrMTU':wlsrMTU,_D:wlsrLocation,'wlsrHideSSID':wlsrHideSSID,'wlsrDenyBroadcast':wlsrDenyBroadcast,'wlsrBGmode':wlsrBGmode,'wlsrCardType':wlsrCardType,'wlsrRegDomain':wlsrRegDomain,'wlsrCountryCode':wlsrCountryCode,'wlsrTxRates':wlsrTxRates,'wlsrStatsGroup':wlsrStatsGroup,'wlsrStatsChannelGroup':wlsrStatsChannelGroup,'wlsrChannelStatsTable':wlsrChannelStatsTable,'wlsrChannelStatsEntry':wlsrChannelStatsEntry,_M:wlsrChStatsChannel,'wlsrChStatsNumAPs':wlsrChStatsNumAPs,'wlsrChStatsNumStations':wlsrChStatsNumStations,'wlsrChStatsTotPkts':wlsrChStatsTotPkts,'wlsrChStatsTotBytes':wlsrChStatsTotBytes,'wlsrChStatsTotRetryPkts':wlsrChStatsTotRetryPkts,'wlsrChStatsTotFragmentedPkts':wlsrChStatsTotFragmentedPkts,'wlsrChStatsTotPhyErrPkts':wlsrChStatsTotPhyErrPkts,'wlsrChStatsTotMacErrPkts':wlsrChStatsTotMacErrPkts,'wlsrChStatsFrameErrorRate':wlsrChStatsFrameErrorRate,'wlsrChStatsFrameRetryRate':wlsrChStatsFrameRetryRate,'wlsrChStatsFrameLowSpeedRate':wlsrChStatsFrameLowSpeedRate,'wlsrChStatsFrameNonUnicastRate':wlsrChStatsFrameNonUnicastRate,'wlsrChStatsFrameBandwidthRate':wlsrChStatsFrameBandwidthRate,'wlsrChStatsFrameFragmentationRate':wlsrChStatsFrameFragmentationRate,'wlsrChStatsMonitoredTime':wlsrChStatsMonitoredTime,'wlsrChannelRateStatsTable':wlsrChannelRateStatsTable,'wlsrChannelRateStatsEntry':wlsrChannelRateStatsEntry,'wlsrChStatsTotPktsAt1Mbps':wlsrChStatsTotPktsAt1Mbps,'wlsrChStatsTotBytesAt1Mbps':wlsrChStatsTotBytesAt1Mbps,'wlsrChStatsTotPktsAt2Mbps':wlsrChStatsTotPktsAt2Mbps,'wlsrChStatsTotBytesAt2Mbps':wlsrChStatsTotBytesAt2Mbps,'wlsrChStatsTotPktsAt5Mbps':wlsrChStatsTotPktsAt5Mbps,'wlsrChStatsTotBytesAt5Mbps':wlsrChStatsTotBytesAt5Mbps,'wlsrChStatsTotPktsAt11Mbps':wlsrChStatsTotPktsAt11Mbps,'wlsrChStatsTotBytesAt11Mbps':wlsrChStatsTotBytesAt11Mbps,'wlsrChStatsTotPktsAt6Mbps':wlsrChStatsTotPktsAt6Mbps,'wlsrChStatsTotBytesAt6Mbps':wlsrChStatsTotBytesAt6Mbps,'wlsrChStatsTotPktsAt12Mbps':wlsrChStatsTotPktsAt12Mbps,'wlsrChStatsTotBytesAt12Mbps':wlsrChStatsTotBytesAt12Mbps,'wlsrChStatsTotPktsAt18Mbps':wlsrChStatsTotPktsAt18Mbps,'wlsrChStatsTotBytesAt18Mbps':wlsrChStatsTotBytesAt18Mbps,'wlsrChStatsTotPktsAt24Mbps':wlsrChStatsTotPktsAt24Mbps,'wlsrChStatsTotBytesAt24Mbps':wlsrChStatsTotBytesAt24Mbps,'wlsrChStatsTotPktsAt36Mbps':wlsrChStatsTotPktsAt36Mbps,'wlsrChStatsTotBytesAt36Mbps':wlsrChStatsTotBytesAt36Mbps,'wlsrChStatsTotPktsAt48Mbps':wlsrChStatsTotPktsAt48Mbps,'wlsrChStatsTotBytesAt48Mbps':wlsrChStatsTotBytesAt48Mbps,'wlsrChStatsTotPktsAt54Mbps':wlsrChStatsTotPktsAt54Mbps,'wlsrChStatsTotBytesAt54Mbps':wlsrChStatsTotBytesAt54Mbps,'wlsrChannelDATypeStatsTable':wlsrChannelDATypeStatsTable,'wlsrChannelDATypeStatsEntry':wlsrChannelDATypeStatsEntry,'wlsrChStatsTotDABroadcastPkts':wlsrChStatsTotDABroadcastPkts,'wlsrChStatsTotDABroadcastBytes':wlsrChStatsTotDABroadcastBytes,'wlsrChStatsTotDAMulticastPkts':wlsrChStatsTotDAMulticastPkts,'wlsrChStatsTotDAMulticastBytes':wlsrChStatsTotDAMulticastBytes,'wlsrChStatsTotDAUnicastPkts':wlsrChStatsTotDAUnicastPkts,'wlsrChStatsTotDAUnicastBytes':wlsrChStatsTotDAUnicastBytes,'wlsrChannelFrameTypeStatsTable':wlsrChannelFrameTypeStatsTable,'wlsrChannelFrameTypeStatsEntry':wlsrChannelFrameTypeStatsEntry,'wlsrChStatsTotMgmtPkts':wlsrChStatsTotMgmtPkts,'wlsrChStatsTotMgmtBytes':wlsrChStatsTotMgmtBytes,'wlsrChStatsTotCtrlPkts':wlsrChStatsTotCtrlPkts,'wlsrChStatsTotCtrlBytes':wlsrChStatsTotCtrlBytes,'wlsrChStatsTotDataPkts':wlsrChStatsTotDataPkts,'wlsrChStatsTotDataBytes':wlsrChStatsTotDataBytes,'wlsrChannelPktSizeStatsTable':wlsrChannelPktSizeStatsTable,'wlsrChannelPktSizeStatsEntry':wlsrChannelPktSizeStatsEntry,'wlsrChStatsPkts63Bytes':wlsrChStatsPkts63Bytes,'wlsrChStatsPkts64To127':wlsrChStatsPkts64To127,'wlsrChStatsPkts128To255':wlsrChStatsPkts128To255,'wlsrChStatsPkts256To511':wlsrChStatsPkts256To511,'wlsrChStatsPkts512To1023':wlsrChStatsPkts512To1023,'wlsrChStatsPkts1024To1518':wlsrChStatsPkts1024To1518,'wlsrStatsStaGroup':wlsrStatsStaGroup,'wlsrStaStatsTable':wlsrStaStatsTable,'wlsrStaStatsEntry':wlsrStaStatsEntry,_N:wlsrStaAddress,'wlsrStaTxPkts':wlsrStaTxPkts,'wlsrStaTxBytes':wlsrStaTxBytes,'wlsrStaRxPkts':wlsrStaRxPkts,'wlsrStaRxBytes':wlsrStaRxBytes,'wlsrStaTxRetryPkts':wlsrStaTxRetryPkts,'wlsrStaRxRetryPkts':wlsrStaRxRetryPkts,'wlsrStaTxFragmentedPkts':wlsrStaTxFragmentedPkts,'wlsrStaRxFragmentedPkts':wlsrStaRxFragmentedPkts,'wlsrStaReceiveErrPkts':wlsrStaReceiveErrPkts,'wlsrStaTxTotSignal':wlsrStaTxTotSignal,'wlsrStaTxSignalPkts':wlsrStaTxSignalPkts,'wlsrStaTxCurSignal':wlsrStaTxCurSignal,'wlsrStaTxHighSignal':wlsrStaTxHighSignal,'wlsrStaRxTotNoise':wlsrStaRxTotNoise,'wlsrStaRxNoisePkts':wlsrStaRxNoisePkts,'wlsrStaRxCurrentNoise':wlsrStaRxCurrentNoise,'wlsrStaRxHighNoise':wlsrStaRxHighNoise,'wlsrStaRxLowNoise':wlsrStaRxLowNoise,'wlsrStaFrameRetryRate':wlsrStaFrameRetryRate,'wlsrStaFrameLowSpeedRate':wlsrStaFrameLowSpeedRate,'wlsrStaFrameNonUnicastRate':wlsrStaFrameNonUnicastRate,'wlsrStaFrameRetryErrorRate':wlsrStaFrameRetryErrorRate,'wlsrStaFrameBandwidthRate':wlsrStaFrameBandwidthRate,'wlsrStaFrameFragmentationRate':wlsrStaFrameFragmentationRate,'wlsrStaFrameHighBandwidthRate':wlsrStaFrameHighBandwidthRate,'wlsrStaRateStatsTable':wlsrStaRateStatsTable,'wlsrStaRateStatsEntry':wlsrStaRateStatsEntry,'wlsrStaTxPktsAt1Mbps':wlsrStaTxPktsAt1Mbps,'wlsrStaTxBytesAt1Mbps':wlsrStaTxBytesAt1Mbps,'wlsrStaTxPktsAt2Mbps':wlsrStaTxPktsAt2Mbps,'wlsrStaTxBytesAt2Mbps':wlsrStaTxBytesAt2Mbps,'wlsrStaTxPktsAt5Mbps':wlsrStaTxPktsAt5Mbps,'wlsrStaTxBytesAt5Mbps':wlsrStaTxBytesAt5Mbps,'wlsrStaTxPktsAt11Mbps':wlsrStaTxPktsAt11Mbps,'wlsrStaTxBytesAt11Mbps':wlsrStaTxBytesAt11Mbps,'wlsrStaTxPktsAt6Mbps':wlsrStaTxPktsAt6Mbps,'wlsrStaTxBytesAt6Mbps':wlsrStaTxBytesAt6Mbps,'wlsrStaTxPktsAt12Mbps':wlsrStaTxPktsAt12Mbps,'wlsrStaTxBytesAt12Mbps':wlsrStaTxBytesAt12Mbps,'wlsrStaTxPktsAt18Mbps':wlsrStaTxPktsAt18Mbps,'wlsrStaTxBytesAt18Mbps':wlsrStaTxBytesAt18Mbps,'wlsrStaTxPktsAt24Mbps':wlsrStaTxPktsAt24Mbps,'wlsrStaTxBytesAt24Mbps':wlsrStaTxBytesAt24Mbps,'wlsrStaTxPktsAt36Mbps':wlsrStaTxPktsAt36Mbps,'wlsrStaTxBytesAt36Mbps':wlsrStaTxBytesAt36Mbps,'wlsrStaTxPktsAt48Mbps':wlsrStaTxPktsAt48Mbps,'wlsrStaTxBytesAt48Mbps':wlsrStaTxBytesAt48Mbps,'wlsrStaTxPktsAt54Mbps':wlsrStaTxPktsAt54Mbps,'wlsrStaTxBytesAt54Mbps':wlsrStaTxBytesAt54Mbps,'wlsrStaRxPktsAt1Mbps':wlsrStaRxPktsAt1Mbps,'wlsrStaRxBytesAt1Mbps':wlsrStaRxBytesAt1Mbps,'wlsrStaRxPktsAt2Mbps':wlsrStaRxPktsAt2Mbps,'wlsrStaRxBytesAt2Mbps':wlsrStaRxBytesAt2Mbps,'wlsrStaRxPktsAt5Mbps':wlsrStaRxPktsAt5Mbps,'wlsrStaRxBytesAt5Mbps':wlsrStaRxBytesAt5Mbps,'wlsrStaRxPktsAt11Mbps':wlsrStaRxPktsAt11Mbps,'wlsrStaRxBytesAt11Mbps':wlsrStaRxBytesAt11Mbps,'wlsrStaRxPktsAt6Mbps':wlsrStaRxPktsAt6Mbps,'wlsrStaRxBytesAt6Mbps':wlsrStaRxBytesAt6Mbps,'wlsrStaRxPktsAt12Mbps':wlsrStaRxPktsAt12Mbps,'wlsrStaRxBytesAt12Mbps':wlsrStaRxBytesAt12Mbps,'wlsrStaRxPktsAt18Mbps':wlsrStaRxPktsAt18Mbps,'wlsrStaRxBytesAt18Mbps':wlsrStaRxBytesAt18Mbps,'wlsrStaRxPktsAt24Mbps':wlsrStaRxPktsAt24Mbps,'wlsrStaRxBytesAt24Mbps':wlsrStaRxBytesAt24Mbps,'wlsrStaRxPktsAt36Mbps':wlsrStaRxPktsAt36Mbps,'wlsrStaRxBytesAt36Mbps':wlsrStaRxBytesAt36Mbps,'wlsrStaRxPktsAt48Mbps':wlsrStaRxPktsAt48Mbps,'wlsrStaRxBytesAt48Mbps':wlsrStaRxBytesAt48Mbps,'wlsrStaRxPktsAt54Mbps':wlsrStaRxPktsAt54Mbps,'wlsrStaRxBytesAt54Mbps':wlsrStaRxBytesAt54Mbps,'wlsrStaDATypeStatsTable':wlsrStaDATypeStatsTable,'wlsrStaDATypeStatsEntry':wlsrStaDATypeStatsEntry,'wlsrStaTxDABroadcastPkts':wlsrStaTxDABroadcastPkts,'wlsrStaTxDABroadcastBytes':wlsrStaTxDABroadcastBytes,'wlsrStaTxDAMulticastPkts':wlsrStaTxDAMulticastPkts,'wlsrStaTxDAMulticastBytes':wlsrStaTxDAMulticastBytes,'wlsrStaTxDAUnicastPkts':wlsrStaTxDAUnicastPkts,'wlsrStaTxDAUnicastBytes':wlsrStaTxDAUnicastBytes,'wlsrStaFrameTypeStatsTable':wlsrStaFrameTypeStatsTable,'wlsrStaFrameTypeStatsEntry':wlsrStaFrameTypeStatsEntry,'wlsrStaTxMgmtPkts':wlsrStaTxMgmtPkts,'wlsrStaTxMgmtBytes':wlsrStaTxMgmtBytes,'wlsrStaTxCtrlPkts':wlsrStaTxCtrlPkts,'wlsrStaTxCtrlBytes':wlsrStaTxCtrlBytes,'wlsrStaTxDataPkts':wlsrStaTxDataPkts,'wlsrStaTxDataBytes':wlsrStaTxDataBytes,'wlsrStaRxMgmtPkts':wlsrStaRxMgmtPkts,'wlsrStaRxMgmtBytes':wlsrStaRxMgmtBytes,'wlsrStaRxCtrlPkts':wlsrStaRxCtrlPkts,'wlsrStaRxCtrlBytes':wlsrStaRxCtrlBytes,'wlsrStaRxDataPkts':wlsrStaRxDataPkts,'wlsrStaRxDataBytes':wlsrStaRxDataBytes,'wlsrStaPktSizeStatsTable':wlsrStaPktSizeStatsTable,'wlsrStaPktSizeStatsEntry':wlsrStaPktSizeStatsEntry,'wlsrStaTxPkts63Bytes':wlsrStaTxPkts63Bytes,'wlsrStaTxPkts64To127':wlsrStaTxPkts64To127,'wlsrStaTxPkts128To255':wlsrStaTxPkts128To255,'wlsrStaTxPkts256To511':wlsrStaTxPkts256To511,'wlsrStaTxPkts512To1023':wlsrStaTxPkts512To1023,'wlsrStaTxPkts1024To1518':wlsrStaTxPkts1024To1518,'wlsrStaRxPkts63Bytes':wlsrStaRxPkts63Bytes,'wlsrStaRxPkts64To127':wlsrStaRxPkts64To127,'wlsrStaRxPkts128To255':wlsrStaRxPkts128To255,'wlsrStaRxPkts256To511':wlsrStaRxPkts256To511,'wlsrStaRxPkts512To1023':wlsrStaRxPkts512To1023,'wlsrStaRxPkts1024To1518':wlsrStaRxPkts1024To1518,'wlsrAirMonitorGroup':wlsrAirMonitorGroup,'wlsrAirMonitorApListTable':wlsrAirMonitorApListTable,'wlsrAirMonitorApListEntry':wlsrAirMonitorApListEntry,_o:wlsrAmApBSSID,'wlsrAmSSID':wlsrAmSSID,'wlsrAmChannel':wlsrAmChannel,'wlsrAmPhysicalType':wlsrAmPhysicalType,'wlsrAmAccessPointType':wlsrAmAccessPointType,'wlsrAmRAPType':wlsrAmRAPType,'wlsrAmRSSI':wlsrAmRSSI,'wlsrAmMonitoredTime':wlsrAmMonitoredTime,'wlsrAmInactivityTime':wlsrAmInactivityTime,'wlsrAmLoadBalancing':wlsrAmLoadBalancing,'wlsrTrapsGroup':wlsrTrapsGroup,'wlsrTrapObjectsGroup':wlsrTrapObjectsGroup,_F:wlsrTargetApBSSID,_G:wlsrTargetApSSID,_R:wlsrTargetApChannel,_O:wlsrSourceMac,_I:wlsrNodeMac,_S:wlsrFrameType,_u:wlsrAddressType,_r:wlsrSignatureName,_p:wlsrMatchedMac,_q:wlsrMatchedIp,_t:wlsrReceiverMac,_s:wlsrTransmitterMac,_K:wlsrRSSI,_Z:wlsrRogueInfoURL,_v:wlsrInterferingAPInfoURL,'wlsrUnsecureApDetected':wlsrUnsecureApDetected,'wlsrStaImpersonation':wlsrStaImpersonation,'wlsrReservedChannelViolation':wlsrReservedChannelViolation,'wlsrValidSSIDViolation':wlsrValidSSIDViolation,'wlsrChannelMisconfiguration':wlsrChannelMisconfiguration,'wlsrOUIMisconfiguration':wlsrOUIMisconfiguration,'wlsrSSIDMisconfiguration':wlsrSSIDMisconfiguration,'wlsrShortPreableMisconfiguration':wlsrShortPreableMisconfiguration,'wlsrWPAMisconfiguration':wlsrWPAMisconfiguration,'wlsrAdhocNetworkDetected':wlsrAdhocNetworkDetected,'wlsrStaPolicyViolation':wlsrStaPolicyViolation,'wlsrRepeatWEPIVViolation':wlsrRepeatWEPIVViolation,'wlsrWeakWEPIVViolation':wlsrWeakWEPIVViolation,'wlsrChannelInterferenceDetected':wlsrChannelInterferenceDetected,'wlsrAPInterferenceDetected':wlsrAPInterferenceDetected,'wlsrStaInterferenceDetected':wlsrStaInterferenceDetected,'wlsrFrameRetryRateExceeded':wlsrFrameRetryRateExceeded,'wlsrFrameReceiveErrorRateExceeded':wlsrFrameReceiveErrorRateExceeded,'wlsrFrameFragmentationRateExceeded':wlsrFrameFragmentationRateExceeded,'wlsrFrameBandWidthRateExceeded':wlsrFrameBandWidthRateExceeded,'wlsrFrameLowSpeedRateExceeded':wlsrFrameLowSpeedRateExceeded,'wlsrFrameNonUnicastRateExceeded':wlsrFrameNonUnicastRateExceeded,'wlsrLoadbalancingEnabled':wlsrLoadbalancingEnabled,'wlsrChannelFrameRetryRateExceeded':wlsrChannelFrameRetryRateExceeded,'wlsrChannelFrameFragmentationRateExceeded':wlsrChannelFrameFragmentationRateExceeded,'wlsrChannelFrameErrorRateExceeded':wlsrChannelFrameErrorRateExceeded,'wlsrSignatureMatch':wlsrSignatureMatch,'wlsrChannelRateAnomaly':wlsrChannelRateAnomaly,'wlsrNodeRateAnomaly':wlsrNodeRateAnomaly,'wlsrEAPRateAnomaly':wlsrEAPRateAnomaly,'wlsrSignalAnomaly':wlsrSignalAnomaly,'wlsrSequenceNumberAnomaly':wlsrSequenceNumberAnomaly,'wlsrDisconnectStationAttack':wlsrDisconnectStationAttack,'wlsrApFloodAttack':wlsrApFloodAttack,'wlsrAdhocNetwork':wlsrAdhocNetwork,'wlsrWirelessBridge':wlsrWirelessBridge,'wlsrInvalidMacOUI':wlsrInvalidMacOUI,'wlsrLoadbalancingDisabled':wlsrLoadbalancingDisabled,'wlsrWEPMisconfiguration':wlsrWEPMisconfiguration,'wlsrStaRepeatWEPIVViolation':wlsrStaRepeatWEPIVViolation,'wlsrStaWeakWEPIVViolation':wlsrStaWeakWEPIVViolation,'wlsrStaAssociatedToUnsecureAp':wlsrStaAssociatedToUnsecureAp,'wlsrAdhocNetworkBridgeDetected':wlsrAdhocNetworkBridgeDetected,'wlsrInterferingApDetected':wlsrInterferingApDetected})