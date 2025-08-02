_Ae='mimosaPtmpMgmtInfoGroup'
_Ad='mimosaPtmpClientInfoGroup'
_Ac='mimosaPtmpClientStatsGroup'
_Ab='mimosaPtmpApStatsGroup'
_Aa='mimosaPtmpChannelPowerGroup'
_AZ='mimosaPtmpLinkInfoGroup'
_AY='mimosaPtmpSsidGroup'
_AX='mimosaPtmpMgmtEthernetMac'
_AW='mimosaPtmpMgmtVlanPassthrough'
_AV='mimosaPtmpMgmtVlanId'
_AU='mimosaPtmpMgmtVlanStatus'
_AT='mimosaPtmpMgmtSecondaryDNS'
_AS='mimosaPtmpMgmtPrimaryDNS'
_AR='mimosaPtmpMgmtIpMode'
_AQ='mimosaPtmpMgmtIpGateway'
_AP='mimosaPtmpMgmtIpNetmask'
_AO='mimosaPtmpMgmtIpAddress'
_AN='mimosaPtmpClientTxMcs'
_AM='mimosaPtmpClientRxMcs'
_AL='mimosaPtmpClientTxNss'
_AK='mimosaPtmpClientRxNss'
_AJ='mimosaPtmpClientRxEVM4'
_AI='mimosaPtmpClientRxEVM3'
_AH='mimosaPtmpClientRxEVM2'
_AG='mimosaPtmpClientRxEVM1'
_AF='mimosaPtmpClientRssi4'
_AE='mimosaPtmpClientRssi3'
_AD='mimosaPtmpClientRssi2'
_AC='mimosaPtmpClientRssi1'
_AB='mimosaPtmpClientStatsLastUpdated'
_AA='mimosaPtmpClientTxBytes'
_A9='mimosaPtmpClientTxPhyRate'
_A8='mimosaPtmpClientTxAvgPer'
_A7='mimosaPtmpClientRxPhyRate'
_A6='mimosaPtmpClientRssiAvg'
_A5='mimosaPtmpClientTxPkts'
_A4='mimosaPtmpClientRxPkts'
_A3='mimosaPtmpClientRxBytes'
_A2='mimosaPtmpClientAssocBW'
_A1='mimosaPtmpClientStatsMacAddress'
_A0='mimosaPtmpClientInfoLastUpdated'
_z='mimosaPtmpClientDlPeak'
_y='mimosaPtmpClientDlCommitted'
_x='mimosaPtmpClientUlPeak'
_w='mimosaPtmpClientUlCommitted'
_v='mimosaPtmpClientPlanName'
_u='mimosaPtmpClientAssociatedTime'
_t='mimosaPtmpClientIPAddress'
_s='mimosaPtmpClientFWVersion'
_r='mimosaPtmpClientName'
_q='mimosaPtmpApStatsLastUpdated'
_p='mimosaPtmpApStatsTxPer'
_o='mimosaPtmpApStatsTxPkts'
_n='mimosaPtmpApStatsRxPkts'
_m='mimosaPtmpApStatsTxBytes'
_l='mimosaPtmpApStatsRxBytes'
_k='mimosaPtmpChannelExclusionEnd'
_j='mimosaPtmpChannelExclusionStart'
_i='mimosaPtmpChPwrMinRxPower'
_h='mimosaPtmpChPwrAgcMode'
_g='mimosaPtmpChPwrTxPowerCur'
_f='mimosaPtmpChPwrChWidthCur'
_e='mimosaPtmpChPwrPrimChannelCur'
_d='mimosaPtmpChPwrCntrFreqCur'
_c='mimosaPtmpChPwrTxPowerCfg'
_b='mimosaPtmpChPwrChWidthCfg'
_a='mimosaPtmpChPwrPrimChannelCfg'
_Z='mimosaPtmpChPwrCntrFreqCfg'
_Y='mimosaPtmpChPwrRadioName'
_X='mimosaPtmpAntennaGain'
_W='mimosaPtmpAutoChannelEnabled'
_V='mimosaPtmpWirelessWindowLength'
_U='mimosaPtmpWirelessTrafficSplit'
_T='mimosaPtmpWirelessGender'
_S='mimosaPtmpWirelessMode'
_R='mimosaPtmpSsidIsolationEnabled'
_Q='mimosaPtmpSsidBroadcastEnabled'
_P='mimosaPtmpSsidEnabled'
_O='mimosaPtmpSsidType'
_N='mimosaPtmpSsidName'
_M='enable'
_L='disable'
_K='mimosaPtmpClientStatsIndex'
_J='mimosaPtmpClientInfoIndex'
_I='mimosaPtmpChannelExclusionIndex'
_H='mimosaPtmpChPwrRadioIndex'
_G='mimosaPtmpSsidIndex'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='MIMOSA-NETWORKS-PTMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DecimalOne,DecimalTwo,Mimosa5GHzChannelNumber,Mimosa5GHzFrequency=mibBuilder.importSymbols('MIMOSA-MIB-TC','DecimalOne','DecimalTwo','Mimosa5GHzChannelNumber','Mimosa5GHzFrequency')
mimosaConformanceGroup,mimosaWireless=mibBuilder.importSymbols('MIMOSA-NETWORKS-BASE-MIB','mimosaConformanceGroup','mimosaWireless')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
mimosaPtmp=ModuleIdentity((1,3,6,1,4,1,43356,2,1,2,9))
if mibBuilder.loadTexts:mimosaPtmp.setRevisions(('2017-04-05 00:00',))
_MimosaPtmpSsid_ObjectIdentity=ObjectIdentity
mimosaPtmpSsid=_MimosaPtmpSsid_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,1))
_MimosaPtmpSsidTable_Object=MibTable
mimosaPtmpSsidTable=_MimosaPtmpSsidTable_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1))
if mibBuilder.loadTexts:mimosaPtmpSsidTable.setStatus(_A)
_MimosaPtmpSsidEntry_Object=MibTableRow
mimosaPtmpSsidEntry=_MimosaPtmpSsidEntry_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1))
mimosaPtmpSsidEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mimosaPtmpSsidEntry.setStatus(_A)
class _MimosaPtmpSsidIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_MimosaPtmpSsidIndex_Type.__name__=_D
_MimosaPtmpSsidIndex_Object=MibTableColumn
mimosaPtmpSsidIndex=_MimosaPtmpSsidIndex_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,1),_MimosaPtmpSsidIndex_Type())
mimosaPtmpSsidIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mimosaPtmpSsidIndex.setStatus(_A)
class _MimosaPtmpSsidName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MimosaPtmpSsidName_Type.__name__=_E
_MimosaPtmpSsidName_Object=MibTableColumn
mimosaPtmpSsidName=_MimosaPtmpSsidName_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,2),_MimosaPtmpSsidName_Type())
mimosaPtmpSsidName.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpSsidName.setStatus(_A)
class _MimosaPtmpSsidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hotspot',0),('cpe',1)))
_MimosaPtmpSsidType_Type.__name__=_D
_MimosaPtmpSsidType_Object=MibTableColumn
mimosaPtmpSsidType=_MimosaPtmpSsidType_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,3),_MimosaPtmpSsidType_Type())
mimosaPtmpSsidType.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpSsidType.setStatus(_A)
_MimosaPtmpSsidEnabled_Type=TruthValue
_MimosaPtmpSsidEnabled_Object=MibTableColumn
mimosaPtmpSsidEnabled=_MimosaPtmpSsidEnabled_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,4),_MimosaPtmpSsidEnabled_Type())
mimosaPtmpSsidEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpSsidEnabled.setStatus(_A)
_MimosaPtmpSsidBroadcastEnabled_Type=TruthValue
_MimosaPtmpSsidBroadcastEnabled_Object=MibTableColumn
mimosaPtmpSsidBroadcastEnabled=_MimosaPtmpSsidBroadcastEnabled_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,5),_MimosaPtmpSsidBroadcastEnabled_Type())
mimosaPtmpSsidBroadcastEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpSsidBroadcastEnabled.setStatus(_A)
_MimosaPtmpSsidIsolationEnabled_Type=TruthValue
_MimosaPtmpSsidIsolationEnabled_Object=MibTableColumn
mimosaPtmpSsidIsolationEnabled=_MimosaPtmpSsidIsolationEnabled_Object((1,3,6,1,4,1,43356,2,1,2,9,1,1,1,6),_MimosaPtmpSsidIsolationEnabled_Type())
mimosaPtmpSsidIsolationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpSsidIsolationEnabled.setStatus(_A)
_MimosaPtmpLinkInfo_ObjectIdentity=ObjectIdentity
mimosaPtmpLinkInfo=_MimosaPtmpLinkInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,2))
class _MimosaPtmpWirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('srs',1),('wifiinterop',2)))
_MimosaPtmpWirelessMode_Type.__name__=_D
_MimosaPtmpWirelessMode_Object=MibScalar
mimosaPtmpWirelessMode=_MimosaPtmpWirelessMode_Object((1,3,6,1,4,1,43356,2,1,2,9,2,1),_MimosaPtmpWirelessMode_Type())
mimosaPtmpWirelessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpWirelessMode.setStatus(_A)
class _MimosaPtmpWirelessGender_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('a',1),('b',2)))
_MimosaPtmpWirelessGender_Type.__name__=_D
_MimosaPtmpWirelessGender_Object=MibScalar
mimosaPtmpWirelessGender=_MimosaPtmpWirelessGender_Object((1,3,6,1,4,1,43356,2,1,2,9,2,2),_MimosaPtmpWirelessGender_Type())
mimosaPtmpWirelessGender.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpWirelessGender.setStatus(_A)
_MimosaPtmpWirelessTrafficSplit_Type=DisplayString
_MimosaPtmpWirelessTrafficSplit_Object=MibScalar
mimosaPtmpWirelessTrafficSplit=_MimosaPtmpWirelessTrafficSplit_Object((1,3,6,1,4,1,43356,2,1,2,9,2,3),_MimosaPtmpWirelessTrafficSplit_Type())
mimosaPtmpWirelessTrafficSplit.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpWirelessTrafficSplit.setStatus(_A)
_MimosaPtmpWirelessWindowLength_Type=Integer32
_MimosaPtmpWirelessWindowLength_Object=MibScalar
mimosaPtmpWirelessWindowLength=_MimosaPtmpWirelessWindowLength_Object((1,3,6,1,4,1,43356,2,1,2,9,2,4),_MimosaPtmpWirelessWindowLength_Type())
mimosaPtmpWirelessWindowLength.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpWirelessWindowLength.setStatus(_A)
_MimosaPtmpChannelPower_ObjectIdentity=ObjectIdentity
mimosaPtmpChannelPower=_MimosaPtmpChannelPower_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,3))
_MimosaPtmpAutoChannelEnabled_Type=TruthValue
_MimosaPtmpAutoChannelEnabled_Object=MibScalar
mimosaPtmpAutoChannelEnabled=_MimosaPtmpAutoChannelEnabled_Object((1,3,6,1,4,1,43356,2,1,2,9,3,1),_MimosaPtmpAutoChannelEnabled_Type())
mimosaPtmpAutoChannelEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpAutoChannelEnabled.setStatus(_A)
_MimosaPtmpAntennaGain_Type=Unsigned32
_MimosaPtmpAntennaGain_Object=MibScalar
mimosaPtmpAntennaGain=_MimosaPtmpAntennaGain_Object((1,3,6,1,4,1,43356,2,1,2,9,3,2),_MimosaPtmpAntennaGain_Type())
mimosaPtmpAntennaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpAntennaGain.setStatus(_A)
_MimosaPtmpChannelPowerTable_Object=MibTable
mimosaPtmpChannelPowerTable=_MimosaPtmpChannelPowerTable_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3))
if mibBuilder.loadTexts:mimosaPtmpChannelPowerTable.setStatus(_A)
_MimosaPtmpChannelPowerEntry_Object=MibTableRow
mimosaPtmpChannelPowerEntry=_MimosaPtmpChannelPowerEntry_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1))
mimosaPtmpChannelPowerEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:mimosaPtmpChannelPowerEntry.setStatus(_A)
_MimosaPtmpChPwrRadioIndex_Type=Unsigned32
_MimosaPtmpChPwrRadioIndex_Object=MibTableColumn
mimosaPtmpChPwrRadioIndex=_MimosaPtmpChPwrRadioIndex_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,1),_MimosaPtmpChPwrRadioIndex_Type())
mimosaPtmpChPwrRadioIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mimosaPtmpChPwrRadioIndex.setStatus(_A)
class _MimosaPtmpChPwrRadioName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MimosaPtmpChPwrRadioName_Type.__name__=_E
_MimosaPtmpChPwrRadioName_Object=MibTableColumn
mimosaPtmpChPwrRadioName=_MimosaPtmpChPwrRadioName_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,2),_MimosaPtmpChPwrRadioName_Type())
mimosaPtmpChPwrRadioName.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrRadioName.setStatus(_A)
_MimosaPtmpChPwrCntrFreqCfg_Type=Mimosa5GHzFrequency
_MimosaPtmpChPwrCntrFreqCfg_Object=MibTableColumn
mimosaPtmpChPwrCntrFreqCfg=_MimosaPtmpChPwrCntrFreqCfg_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,3),_MimosaPtmpChPwrCntrFreqCfg_Type())
mimosaPtmpChPwrCntrFreqCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrCntrFreqCfg.setStatus(_A)
_MimosaPtmpChPwrPrimChannelCfg_Type=Mimosa5GHzChannelNumber
_MimosaPtmpChPwrPrimChannelCfg_Object=MibTableColumn
mimosaPtmpChPwrPrimChannelCfg=_MimosaPtmpChPwrPrimChannelCfg_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,4),_MimosaPtmpChPwrPrimChannelCfg_Type())
mimosaPtmpChPwrPrimChannelCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrPrimChannelCfg.setStatus(_A)
_MimosaPtmpChPwrChWidthCfg_Type=Unsigned32
_MimosaPtmpChPwrChWidthCfg_Object=MibTableColumn
mimosaPtmpChPwrChWidthCfg=_MimosaPtmpChPwrChWidthCfg_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,5),_MimosaPtmpChPwrChWidthCfg_Type())
mimosaPtmpChPwrChWidthCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrChWidthCfg.setStatus(_A)
_MimosaPtmpChPwrTxPowerCfg_Type=Integer32
_MimosaPtmpChPwrTxPowerCfg_Object=MibTableColumn
mimosaPtmpChPwrTxPowerCfg=_MimosaPtmpChPwrTxPowerCfg_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,6),_MimosaPtmpChPwrTxPowerCfg_Type())
mimosaPtmpChPwrTxPowerCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrTxPowerCfg.setStatus(_A)
_MimosaPtmpChPwrCntrFreqCur_Type=Mimosa5GHzFrequency
_MimosaPtmpChPwrCntrFreqCur_Object=MibTableColumn
mimosaPtmpChPwrCntrFreqCur=_MimosaPtmpChPwrCntrFreqCur_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,7),_MimosaPtmpChPwrCntrFreqCur_Type())
mimosaPtmpChPwrCntrFreqCur.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrCntrFreqCur.setStatus(_A)
_MimosaPtmpChPwrPrimChannelCur_Type=Mimosa5GHzChannelNumber
_MimosaPtmpChPwrPrimChannelCur_Object=MibTableColumn
mimosaPtmpChPwrPrimChannelCur=_MimosaPtmpChPwrPrimChannelCur_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,8),_MimosaPtmpChPwrPrimChannelCur_Type())
mimosaPtmpChPwrPrimChannelCur.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrPrimChannelCur.setStatus(_A)
_MimosaPtmpChPwrChWidthCur_Type=Unsigned32
_MimosaPtmpChPwrChWidthCur_Object=MibTableColumn
mimosaPtmpChPwrChWidthCur=_MimosaPtmpChPwrChWidthCur_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,9),_MimosaPtmpChPwrChWidthCur_Type())
mimosaPtmpChPwrChWidthCur.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrChWidthCur.setStatus(_A)
_MimosaPtmpChPwrTxPowerCur_Type=Integer32
_MimosaPtmpChPwrTxPowerCur_Object=MibTableColumn
mimosaPtmpChPwrTxPowerCur=_MimosaPtmpChPwrTxPowerCur_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,10),_MimosaPtmpChPwrTxPowerCur_Type())
mimosaPtmpChPwrTxPowerCur.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrTxPowerCur.setStatus(_A)
class _MimosaPtmpChPwrAgcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('manual',1)))
_MimosaPtmpChPwrAgcMode_Type.__name__=_D
_MimosaPtmpChPwrAgcMode_Object=MibTableColumn
mimosaPtmpChPwrAgcMode=_MimosaPtmpChPwrAgcMode_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,11),_MimosaPtmpChPwrAgcMode_Type())
mimosaPtmpChPwrAgcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrAgcMode.setStatus(_A)
class _MimosaPtmpChPwrMinRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,-10))
_MimosaPtmpChPwrMinRxPower_Type.__name__=_D
_MimosaPtmpChPwrMinRxPower_Object=MibTableColumn
mimosaPtmpChPwrMinRxPower=_MimosaPtmpChPwrMinRxPower_Object((1,3,6,1,4,1,43356,2,1,2,9,3,3,1,12),_MimosaPtmpChPwrMinRxPower_Type())
mimosaPtmpChPwrMinRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChPwrMinRxPower.setStatus(_A)
_MimosaPtmpChannelExclusionTable_Object=MibTable
mimosaPtmpChannelExclusionTable=_MimosaPtmpChannelExclusionTable_Object((1,3,6,1,4,1,43356,2,1,2,9,3,4))
if mibBuilder.loadTexts:mimosaPtmpChannelExclusionTable.setStatus(_A)
_MimosaPtmpChannelExclusionEntry_Object=MibTableRow
mimosaPtmpChannelExclusionEntry=_MimosaPtmpChannelExclusionEntry_Object((1,3,6,1,4,1,43356,2,1,2,9,3,4,1))
mimosaPtmpChannelExclusionEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:mimosaPtmpChannelExclusionEntry.setStatus(_A)
class _MimosaPtmpChannelExclusionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MimosaPtmpChannelExclusionIndex_Type.__name__=_D
_MimosaPtmpChannelExclusionIndex_Object=MibTableColumn
mimosaPtmpChannelExclusionIndex=_MimosaPtmpChannelExclusionIndex_Object((1,3,6,1,4,1,43356,2,1,2,9,3,4,1,1),_MimosaPtmpChannelExclusionIndex_Type())
mimosaPtmpChannelExclusionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mimosaPtmpChannelExclusionIndex.setStatus(_A)
_MimosaPtmpChannelExclusionStart_Type=Integer32
_MimosaPtmpChannelExclusionStart_Object=MibTableColumn
mimosaPtmpChannelExclusionStart=_MimosaPtmpChannelExclusionStart_Object((1,3,6,1,4,1,43356,2,1,2,9,3,4,1,2),_MimosaPtmpChannelExclusionStart_Type())
mimosaPtmpChannelExclusionStart.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChannelExclusionStart.setStatus(_A)
_MimosaPtmpChannelExclusionEnd_Type=Integer32
_MimosaPtmpChannelExclusionEnd_Object=MibTableColumn
mimosaPtmpChannelExclusionEnd=_MimosaPtmpChannelExclusionEnd_Object((1,3,6,1,4,1,43356,2,1,2,9,3,4,1,3),_MimosaPtmpChannelExclusionEnd_Type())
mimosaPtmpChannelExclusionEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpChannelExclusionEnd.setStatus(_A)
_MimosaPtmpApStats_ObjectIdentity=ObjectIdentity
mimosaPtmpApStats=_MimosaPtmpApStats_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,4))
_MimosaPtmpApStatsRxBytes_Type=Counter64
_MimosaPtmpApStatsRxBytes_Object=MibScalar
mimosaPtmpApStatsRxBytes=_MimosaPtmpApStatsRxBytes_Object((1,3,6,1,4,1,43356,2,1,2,9,4,1),_MimosaPtmpApStatsRxBytes_Type())
mimosaPtmpApStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsRxBytes.setStatus(_A)
_MimosaPtmpApStatsTxBytes_Type=Counter64
_MimosaPtmpApStatsTxBytes_Object=MibScalar
mimosaPtmpApStatsTxBytes=_MimosaPtmpApStatsTxBytes_Object((1,3,6,1,4,1,43356,2,1,2,9,4,2),_MimosaPtmpApStatsTxBytes_Type())
mimosaPtmpApStatsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsTxBytes.setStatus(_A)
_MimosaPtmpApStatsRxPkts_Type=Counter64
_MimosaPtmpApStatsRxPkts_Object=MibScalar
mimosaPtmpApStatsRxPkts=_MimosaPtmpApStatsRxPkts_Object((1,3,6,1,4,1,43356,2,1,2,9,4,3),_MimosaPtmpApStatsRxPkts_Type())
mimosaPtmpApStatsRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsRxPkts.setStatus(_A)
_MimosaPtmpApStatsTxPkts_Type=Counter64
_MimosaPtmpApStatsTxPkts_Object=MibScalar
mimosaPtmpApStatsTxPkts=_MimosaPtmpApStatsTxPkts_Object((1,3,6,1,4,1,43356,2,1,2,9,4,4),_MimosaPtmpApStatsTxPkts_Type())
mimosaPtmpApStatsTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsTxPkts.setStatus(_A)
_MimosaPtmpApStatsTxPer_Type=Integer32
_MimosaPtmpApStatsTxPer_Object=MibScalar
mimosaPtmpApStatsTxPer=_MimosaPtmpApStatsTxPer_Object((1,3,6,1,4,1,43356,2,1,2,9,4,5),_MimosaPtmpApStatsTxPer_Type())
mimosaPtmpApStatsTxPer.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsTxPer.setStatus(_A)
_MimosaPtmpApStatsLastUpdated_Type=TimeStamp
_MimosaPtmpApStatsLastUpdated_Object=MibScalar
mimosaPtmpApStatsLastUpdated=_MimosaPtmpApStatsLastUpdated_Object((1,3,6,1,4,1,43356,2,1,2,9,4,6),_MimosaPtmpApStatsLastUpdated_Type())
mimosaPtmpApStatsLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpApStatsLastUpdated.setStatus(_A)
_MimosaPtmpClientInfo_ObjectIdentity=ObjectIdentity
mimosaPtmpClientInfo=_MimosaPtmpClientInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,5))
_MimosaPtmpClientInfoTable_Object=MibTable
mimosaPtmpClientInfoTable=_MimosaPtmpClientInfoTable_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1))
if mibBuilder.loadTexts:mimosaPtmpClientInfoTable.setStatus(_A)
_MimosaPtmpClientInfoEntry_Object=MibTableRow
mimosaPtmpClientInfoEntry=_MimosaPtmpClientInfoEntry_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1))
mimosaPtmpClientInfoEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:mimosaPtmpClientInfoEntry.setStatus(_A)
_MimosaPtmpClientInfoIndex_Type=Unsigned32
_MimosaPtmpClientInfoIndex_Object=MibTableColumn
mimosaPtmpClientInfoIndex=_MimosaPtmpClientInfoIndex_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,1),_MimosaPtmpClientInfoIndex_Type())
mimosaPtmpClientInfoIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mimosaPtmpClientInfoIndex.setStatus(_A)
_MimosaPtmpClientInfoMacAddress_Type=MacAddress
_MimosaPtmpClientInfoMacAddress_Object=MibTableColumn
mimosaPtmpClientInfoMacAddress=_MimosaPtmpClientInfoMacAddress_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,2),_MimosaPtmpClientInfoMacAddress_Type())
mimosaPtmpClientInfoMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientInfoMacAddress.setStatus(_A)
class _MimosaPtmpClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MimosaPtmpClientName_Type.__name__=_E
_MimosaPtmpClientName_Object=MibTableColumn
mimosaPtmpClientName=_MimosaPtmpClientName_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,3),_MimosaPtmpClientName_Type())
mimosaPtmpClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientName.setStatus(_A)
class _MimosaPtmpClientFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MimosaPtmpClientFWVersion_Type.__name__=_E
_MimosaPtmpClientFWVersion_Object=MibTableColumn
mimosaPtmpClientFWVersion=_MimosaPtmpClientFWVersion_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,4),_MimosaPtmpClientFWVersion_Type())
mimosaPtmpClientFWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientFWVersion.setStatus(_A)
_MimosaPtmpClientIPAddress_Type=IpAddress
_MimosaPtmpClientIPAddress_Object=MibTableColumn
mimosaPtmpClientIPAddress=_MimosaPtmpClientIPAddress_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,5),_MimosaPtmpClientIPAddress_Type())
mimosaPtmpClientIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientIPAddress.setStatus(_A)
_MimosaPtmpClientAssociatedTime_Type=TimeStamp
_MimosaPtmpClientAssociatedTime_Object=MibTableColumn
mimosaPtmpClientAssociatedTime=_MimosaPtmpClientAssociatedTime_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,6),_MimosaPtmpClientAssociatedTime_Type())
mimosaPtmpClientAssociatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientAssociatedTime.setStatus(_A)
_MimosaPtmpClientPlanName_Type=DisplayString
_MimosaPtmpClientPlanName_Object=MibTableColumn
mimosaPtmpClientPlanName=_MimosaPtmpClientPlanName_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,7),_MimosaPtmpClientPlanName_Type())
mimosaPtmpClientPlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientPlanName.setStatus(_A)
_MimosaPtmpClientUlCommitted_Type=Unsigned32
_MimosaPtmpClientUlCommitted_Object=MibTableColumn
mimosaPtmpClientUlCommitted=_MimosaPtmpClientUlCommitted_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,8),_MimosaPtmpClientUlCommitted_Type())
mimosaPtmpClientUlCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientUlCommitted.setStatus(_A)
_MimosaPtmpClientUlPeak_Type=Unsigned32
_MimosaPtmpClientUlPeak_Object=MibTableColumn
mimosaPtmpClientUlPeak=_MimosaPtmpClientUlPeak_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,9),_MimosaPtmpClientUlPeak_Type())
mimosaPtmpClientUlPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientUlPeak.setStatus(_A)
_MimosaPtmpClientDlCommitted_Type=Unsigned32
_MimosaPtmpClientDlCommitted_Object=MibTableColumn
mimosaPtmpClientDlCommitted=_MimosaPtmpClientDlCommitted_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,10),_MimosaPtmpClientDlCommitted_Type())
mimosaPtmpClientDlCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientDlCommitted.setStatus(_A)
_MimosaPtmpClientDlPeak_Type=Unsigned32
_MimosaPtmpClientDlPeak_Object=MibTableColumn
mimosaPtmpClientDlPeak=_MimosaPtmpClientDlPeak_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,11),_MimosaPtmpClientDlPeak_Type())
mimosaPtmpClientDlPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientDlPeak.setStatus(_A)
_MimosaPtmpClientInfoLastUpdated_Type=TimeStamp
_MimosaPtmpClientInfoLastUpdated_Object=MibTableColumn
mimosaPtmpClientInfoLastUpdated=_MimosaPtmpClientInfoLastUpdated_Object((1,3,6,1,4,1,43356,2,1,2,9,5,1,1,12),_MimosaPtmpClientInfoLastUpdated_Type())
mimosaPtmpClientInfoLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientInfoLastUpdated.setStatus(_A)
_MimosaPtmpClientStats_ObjectIdentity=ObjectIdentity
mimosaPtmpClientStats=_MimosaPtmpClientStats_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,6))
_MimosaPtmpClientStatsTable_Object=MibTable
mimosaPtmpClientStatsTable=_MimosaPtmpClientStatsTable_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1))
if mibBuilder.loadTexts:mimosaPtmpClientStatsTable.setStatus(_A)
_MimosaPtmpClientStatsEntry_Object=MibTableRow
mimosaPtmpClientStatsEntry=_MimosaPtmpClientStatsEntry_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1))
mimosaPtmpClientStatsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:mimosaPtmpClientStatsEntry.setStatus(_A)
_MimosaPtmpClientStatsIndex_Type=Unsigned32
_MimosaPtmpClientStatsIndex_Object=MibTableColumn
mimosaPtmpClientStatsIndex=_MimosaPtmpClientStatsIndex_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,1),_MimosaPtmpClientStatsIndex_Type())
mimosaPtmpClientStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mimosaPtmpClientStatsIndex.setStatus(_A)
_MimosaPtmpClientStatsMacAddress_Type=MacAddress
_MimosaPtmpClientStatsMacAddress_Object=MibTableColumn
mimosaPtmpClientStatsMacAddress=_MimosaPtmpClientStatsMacAddress_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,2),_MimosaPtmpClientStatsMacAddress_Type())
mimosaPtmpClientStatsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientStatsMacAddress.setStatus(_A)
_MimosaPtmpClientAssocBW_Type=Unsigned32
_MimosaPtmpClientAssocBW_Object=MibTableColumn
mimosaPtmpClientAssocBW=_MimosaPtmpClientAssocBW_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,3),_MimosaPtmpClientAssocBW_Type())
mimosaPtmpClientAssocBW.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientAssocBW.setStatus(_A)
_MimosaPtmpClientRxBytes_Type=Counter64
_MimosaPtmpClientRxBytes_Object=MibTableColumn
mimosaPtmpClientRxBytes=_MimosaPtmpClientRxBytes_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,4),_MimosaPtmpClientRxBytes_Type())
mimosaPtmpClientRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxBytes.setStatus(_A)
_MimosaPtmpClientTxBytes_Type=Counter64
_MimosaPtmpClientTxBytes_Object=MibTableColumn
mimosaPtmpClientTxBytes=_MimosaPtmpClientTxBytes_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,5),_MimosaPtmpClientTxBytes_Type())
mimosaPtmpClientTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxBytes.setStatus(_A)
_MimosaPtmpClientRxPkts_Type=Counter64
_MimosaPtmpClientRxPkts_Object=MibTableColumn
mimosaPtmpClientRxPkts=_MimosaPtmpClientRxPkts_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,6),_MimosaPtmpClientRxPkts_Type())
mimosaPtmpClientRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxPkts.setStatus(_A)
_MimosaPtmpClientTxPkts_Type=Counter64
_MimosaPtmpClientTxPkts_Object=MibTableColumn
mimosaPtmpClientTxPkts=_MimosaPtmpClientTxPkts_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,7),_MimosaPtmpClientTxPkts_Type())
mimosaPtmpClientTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxPkts.setStatus(_A)
_MimosaPtmpClientRxPhyRate_Type=Unsigned32
_MimosaPtmpClientRxPhyRate_Object=MibTableColumn
mimosaPtmpClientRxPhyRate=_MimosaPtmpClientRxPhyRate_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,8),_MimosaPtmpClientRxPhyRate_Type())
mimosaPtmpClientRxPhyRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxPhyRate.setStatus(_A)
_MimosaPtmpClientTxPhyRate_Type=Unsigned32
_MimosaPtmpClientTxPhyRate_Object=MibTableColumn
mimosaPtmpClientTxPhyRate=_MimosaPtmpClientTxPhyRate_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,9),_MimosaPtmpClientTxPhyRate_Type())
mimosaPtmpClientTxPhyRate.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxPhyRate.setStatus(_A)
_MimosaPtmpClientTxAvgPer_Type=DecimalTwo
_MimosaPtmpClientTxAvgPer_Object=MibTableColumn
mimosaPtmpClientTxAvgPer=_MimosaPtmpClientTxAvgPer_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,10),_MimosaPtmpClientTxAvgPer_Type())
mimosaPtmpClientTxAvgPer.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxAvgPer.setStatus(_A)
_MimosaPtmpClientRssiAvg_Type=DecimalOne
_MimosaPtmpClientRssiAvg_Object=MibTableColumn
mimosaPtmpClientRssiAvg=_MimosaPtmpClientRssiAvg_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,11),_MimosaPtmpClientRssiAvg_Type())
mimosaPtmpClientRssiAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRssiAvg.setStatus(_A)
_MimosaPtmpClientStatsLastUpdated_Type=TimeStamp
_MimosaPtmpClientStatsLastUpdated_Object=MibTableColumn
mimosaPtmpClientStatsLastUpdated=_MimosaPtmpClientStatsLastUpdated_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,12),_MimosaPtmpClientStatsLastUpdated_Type())
mimosaPtmpClientStatsLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientStatsLastUpdated.setStatus(_A)
_MimosaPtmpClientRssi1_Type=DecimalOne
_MimosaPtmpClientRssi1_Object=MibTableColumn
mimosaPtmpClientRssi1=_MimosaPtmpClientRssi1_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,13),_MimosaPtmpClientRssi1_Type())
mimosaPtmpClientRssi1.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRssi1.setStatus(_A)
_MimosaPtmpClientRssi2_Type=DecimalOne
_MimosaPtmpClientRssi2_Object=MibTableColumn
mimosaPtmpClientRssi2=_MimosaPtmpClientRssi2_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,14),_MimosaPtmpClientRssi2_Type())
mimosaPtmpClientRssi2.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRssi2.setStatus(_A)
_MimosaPtmpClientRssi3_Type=DecimalOne
_MimosaPtmpClientRssi3_Object=MibTableColumn
mimosaPtmpClientRssi3=_MimosaPtmpClientRssi3_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,15),_MimosaPtmpClientRssi3_Type())
mimosaPtmpClientRssi3.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRssi3.setStatus(_A)
_MimosaPtmpClientRssi4_Type=DecimalOne
_MimosaPtmpClientRssi4_Object=MibTableColumn
mimosaPtmpClientRssi4=_MimosaPtmpClientRssi4_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,16),_MimosaPtmpClientRssi4_Type())
mimosaPtmpClientRssi4.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRssi4.setStatus(_A)
_MimosaPtmpClientRxEVM1_Type=DecimalOne
_MimosaPtmpClientRxEVM1_Object=MibTableColumn
mimosaPtmpClientRxEVM1=_MimosaPtmpClientRxEVM1_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,17),_MimosaPtmpClientRxEVM1_Type())
mimosaPtmpClientRxEVM1.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxEVM1.setStatus(_A)
_MimosaPtmpClientRxEVM2_Type=DecimalOne
_MimosaPtmpClientRxEVM2_Object=MibTableColumn
mimosaPtmpClientRxEVM2=_MimosaPtmpClientRxEVM2_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,18),_MimosaPtmpClientRxEVM2_Type())
mimosaPtmpClientRxEVM2.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxEVM2.setStatus(_A)
_MimosaPtmpClientRxEVM3_Type=DecimalOne
_MimosaPtmpClientRxEVM3_Object=MibTableColumn
mimosaPtmpClientRxEVM3=_MimosaPtmpClientRxEVM3_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,19),_MimosaPtmpClientRxEVM3_Type())
mimosaPtmpClientRxEVM3.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxEVM3.setStatus(_A)
_MimosaPtmpClientRxEVM4_Type=DecimalOne
_MimosaPtmpClientRxEVM4_Object=MibTableColumn
mimosaPtmpClientRxEVM4=_MimosaPtmpClientRxEVM4_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,20),_MimosaPtmpClientRxEVM4_Type())
mimosaPtmpClientRxEVM4.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxEVM4.setStatus(_A)
_MimosaPtmpClientRxNss_Type=Unsigned32
_MimosaPtmpClientRxNss_Object=MibTableColumn
mimosaPtmpClientRxNss=_MimosaPtmpClientRxNss_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,21),_MimosaPtmpClientRxNss_Type())
mimosaPtmpClientRxNss.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxNss.setStatus(_A)
_MimosaPtmpClientTxNss_Type=Unsigned32
_MimosaPtmpClientTxNss_Object=MibTableColumn
mimosaPtmpClientTxNss=_MimosaPtmpClientTxNss_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,22),_MimosaPtmpClientTxNss_Type())
mimosaPtmpClientTxNss.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxNss.setStatus(_A)
_MimosaPtmpClientRxMcs_Type=Unsigned32
_MimosaPtmpClientRxMcs_Object=MibTableColumn
mimosaPtmpClientRxMcs=_MimosaPtmpClientRxMcs_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,23),_MimosaPtmpClientRxMcs_Type())
mimosaPtmpClientRxMcs.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientRxMcs.setStatus(_A)
_MimosaPtmpClientTxMcs_Type=Unsigned32
_MimosaPtmpClientTxMcs_Object=MibTableColumn
mimosaPtmpClientTxMcs=_MimosaPtmpClientTxMcs_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,24),_MimosaPtmpClientTxMcs_Type())
mimosaPtmpClientTxMcs.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientTxMcs.setStatus(_A)
_MimosaPtmpClientSNR_Type=DecimalOne
_MimosaPtmpClientSNR_Object=MibTableColumn
mimosaPtmpClientSNR=_MimosaPtmpClientSNR_Object((1,3,6,1,4,1,43356,2,1,2,9,6,1,1,25),_MimosaPtmpClientSNR_Type())
mimosaPtmpClientSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpClientSNR.setStatus(_A)
_MimosaPtmpMgmtInfo_ObjectIdentity=ObjectIdentity
mimosaPtmpMgmtInfo=_MimosaPtmpMgmtInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,9,7))
_MimosaPtmpMgmtIpAddress_Type=IpAddress
_MimosaPtmpMgmtIpAddress_Object=MibScalar
mimosaPtmpMgmtIpAddress=_MimosaPtmpMgmtIpAddress_Object((1,3,6,1,4,1,43356,2,1,2,9,7,1),_MimosaPtmpMgmtIpAddress_Type())
mimosaPtmpMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtIpAddress.setStatus(_A)
_MimosaPtmpMgmtIpNetmask_Type=IpAddress
_MimosaPtmpMgmtIpNetmask_Object=MibScalar
mimosaPtmpMgmtIpNetmask=_MimosaPtmpMgmtIpNetmask_Object((1,3,6,1,4,1,43356,2,1,2,9,7,2),_MimosaPtmpMgmtIpNetmask_Type())
mimosaPtmpMgmtIpNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtIpNetmask.setStatus(_A)
_MimosaPtmpMgmtIpGateway_Type=IpAddress
_MimosaPtmpMgmtIpGateway_Object=MibScalar
mimosaPtmpMgmtIpGateway=_MimosaPtmpMgmtIpGateway_Object((1,3,6,1,4,1,43356,2,1,2,9,7,3),_MimosaPtmpMgmtIpGateway_Type())
mimosaPtmpMgmtIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtIpGateway.setStatus(_A)
class _MimosaPtmpMgmtIpMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,6))
_MimosaPtmpMgmtIpMode_Type.__name__=_E
_MimosaPtmpMgmtIpMode_Object=MibScalar
mimosaPtmpMgmtIpMode=_MimosaPtmpMgmtIpMode_Object((1,3,6,1,4,1,43356,2,1,2,9,7,4),_MimosaPtmpMgmtIpMode_Type())
mimosaPtmpMgmtIpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtIpMode.setStatus(_A)
_MimosaPtmpMgmtPrimaryDNS_Type=IpAddress
_MimosaPtmpMgmtPrimaryDNS_Object=MibScalar
mimosaPtmpMgmtPrimaryDNS=_MimosaPtmpMgmtPrimaryDNS_Object((1,3,6,1,4,1,43356,2,1,2,9,7,5),_MimosaPtmpMgmtPrimaryDNS_Type())
mimosaPtmpMgmtPrimaryDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtPrimaryDNS.setStatus(_A)
_MimosaPtmpMgmtSecondaryDNS_Type=IpAddress
_MimosaPtmpMgmtSecondaryDNS_Object=MibScalar
mimosaPtmpMgmtSecondaryDNS=_MimosaPtmpMgmtSecondaryDNS_Object((1,3,6,1,4,1,43356,2,1,2,9,7,6),_MimosaPtmpMgmtSecondaryDNS_Type())
mimosaPtmpMgmtSecondaryDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtSecondaryDNS.setStatus(_A)
class _MimosaPtmpMgmtVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MimosaPtmpMgmtVlanStatus_Type.__name__=_D
_MimosaPtmpMgmtVlanStatus_Object=MibScalar
mimosaPtmpMgmtVlanStatus=_MimosaPtmpMgmtVlanStatus_Object((1,3,6,1,4,1,43356,2,1,2,9,7,7),_MimosaPtmpMgmtVlanStatus_Type())
mimosaPtmpMgmtVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtVlanStatus.setStatus(_A)
_MimosaPtmpMgmtVlanId_Type=Integer32
_MimosaPtmpMgmtVlanId_Object=MibScalar
mimosaPtmpMgmtVlanId=_MimosaPtmpMgmtVlanId_Object((1,3,6,1,4,1,43356,2,1,2,9,7,8),_MimosaPtmpMgmtVlanId_Type())
mimosaPtmpMgmtVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtVlanId.setStatus(_A)
class _MimosaPtmpMgmtVlanPassthrough_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MimosaPtmpMgmtVlanPassthrough_Type.__name__=_D
_MimosaPtmpMgmtVlanPassthrough_Object=MibScalar
mimosaPtmpMgmtVlanPassthrough=_MimosaPtmpMgmtVlanPassthrough_Object((1,3,6,1,4,1,43356,2,1,2,9,7,9),_MimosaPtmpMgmtVlanPassthrough_Type())
mimosaPtmpMgmtVlanPassthrough.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtVlanPassthrough.setStatus(_A)
_MimosaPtmpMgmtEthernetMac_Type=MacAddress
_MimosaPtmpMgmtEthernetMac_Object=MibScalar
mimosaPtmpMgmtEthernetMac=_MimosaPtmpMgmtEthernetMac_Object((1,3,6,1,4,1,43356,2,1,2,9,7,10),_MimosaPtmpMgmtEthernetMac_Type())
mimosaPtmpMgmtEthernetMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaPtmpMgmtEthernetMac.setStatus(_A)
_MimosaPtmpConformance_ObjectIdentity=ObjectIdentity
mimosaPtmpConformance=_MimosaPtmpConformance_ObjectIdentity((1,3,6,1,4,1,43356,2,4,2))
_MimosaPtmpCompliances_ObjectIdentity=ObjectIdentity
mimosaPtmpCompliances=_MimosaPtmpCompliances_ObjectIdentity((1,3,6,1,4,1,43356,2,4,2,1))
_MimosaPtmpGroups_ObjectIdentity=ObjectIdentity
mimosaPtmpGroups=_MimosaPtmpGroups_ObjectIdentity((1,3,6,1,4,1,43356,2,4,2,2))
mimosaPtmpSsidGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,1))
mimosaPtmpSsidGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:mimosaPtmpSsidGroup.setStatus(_A)
mimosaPtmpLinkInfoGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,2))
mimosaPtmpLinkInfoGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:mimosaPtmpLinkInfoGroup.setStatus(_A)
mimosaPtmpChannelPowerGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,3))
mimosaPtmpChannelPowerGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:mimosaPtmpChannelPowerGroup.setStatus(_A)
mimosaPtmpApStatsGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,4))
mimosaPtmpApStatsGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mimosaPtmpApStatsGroup.setStatus(_A)
mimosaPtmpClientInfoGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,5))
mimosaPtmpClientInfoGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:mimosaPtmpClientInfoGroup.setStatus(_A)
mimosaPtmpClientStatsGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,6))
mimosaPtmpClientStatsGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:mimosaPtmpClientStatsGroup.setStatus(_A)
mimosaPtmpMgmtInfoGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,2,2,7))
mimosaPtmpMgmtInfoGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:mimosaPtmpMgmtInfoGroup.setStatus(_A)
mimosaPtmpCompliance=ModuleCompliance((1,3,6,1,4,1,43356,2,4,2,1,1))
mimosaPtmpCompliance.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:mimosaPtmpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mimosaPtmp':mimosaPtmp,'mimosaPtmpSsid':mimosaPtmpSsid,'mimosaPtmpSsidTable':mimosaPtmpSsidTable,'mimosaPtmpSsidEntry':mimosaPtmpSsidEntry,_G:mimosaPtmpSsidIndex,_N:mimosaPtmpSsidName,_O:mimosaPtmpSsidType,_P:mimosaPtmpSsidEnabled,_Q:mimosaPtmpSsidBroadcastEnabled,_R:mimosaPtmpSsidIsolationEnabled,'mimosaPtmpLinkInfo':mimosaPtmpLinkInfo,_S:mimosaPtmpWirelessMode,_T:mimosaPtmpWirelessGender,_U:mimosaPtmpWirelessTrafficSplit,_V:mimosaPtmpWirelessWindowLength,'mimosaPtmpChannelPower':mimosaPtmpChannelPower,_W:mimosaPtmpAutoChannelEnabled,_X:mimosaPtmpAntennaGain,'mimosaPtmpChannelPowerTable':mimosaPtmpChannelPowerTable,'mimosaPtmpChannelPowerEntry':mimosaPtmpChannelPowerEntry,_H:mimosaPtmpChPwrRadioIndex,_Y:mimosaPtmpChPwrRadioName,_Z:mimosaPtmpChPwrCntrFreqCfg,_a:mimosaPtmpChPwrPrimChannelCfg,_b:mimosaPtmpChPwrChWidthCfg,_c:mimosaPtmpChPwrTxPowerCfg,_d:mimosaPtmpChPwrCntrFreqCur,_e:mimosaPtmpChPwrPrimChannelCur,_f:mimosaPtmpChPwrChWidthCur,_g:mimosaPtmpChPwrTxPowerCur,_h:mimosaPtmpChPwrAgcMode,_i:mimosaPtmpChPwrMinRxPower,'mimosaPtmpChannelExclusionTable':mimosaPtmpChannelExclusionTable,'mimosaPtmpChannelExclusionEntry':mimosaPtmpChannelExclusionEntry,_I:mimosaPtmpChannelExclusionIndex,_j:mimosaPtmpChannelExclusionStart,_k:mimosaPtmpChannelExclusionEnd,'mimosaPtmpApStats':mimosaPtmpApStats,_l:mimosaPtmpApStatsRxBytes,_m:mimosaPtmpApStatsTxBytes,_n:mimosaPtmpApStatsRxPkts,_o:mimosaPtmpApStatsTxPkts,_p:mimosaPtmpApStatsTxPer,_q:mimosaPtmpApStatsLastUpdated,'mimosaPtmpClientInfo':mimosaPtmpClientInfo,'mimosaPtmpClientInfoTable':mimosaPtmpClientInfoTable,'mimosaPtmpClientInfoEntry':mimosaPtmpClientInfoEntry,_J:mimosaPtmpClientInfoIndex,'mimosaPtmpClientInfoMacAddress':mimosaPtmpClientInfoMacAddress,_r:mimosaPtmpClientName,_s:mimosaPtmpClientFWVersion,_t:mimosaPtmpClientIPAddress,_u:mimosaPtmpClientAssociatedTime,_v:mimosaPtmpClientPlanName,_w:mimosaPtmpClientUlCommitted,_x:mimosaPtmpClientUlPeak,_y:mimosaPtmpClientDlCommitted,_z:mimosaPtmpClientDlPeak,_A0:mimosaPtmpClientInfoLastUpdated,'mimosaPtmpClientStats':mimosaPtmpClientStats,'mimosaPtmpClientStatsTable':mimosaPtmpClientStatsTable,'mimosaPtmpClientStatsEntry':mimosaPtmpClientStatsEntry,_K:mimosaPtmpClientStatsIndex,_A1:mimosaPtmpClientStatsMacAddress,_A2:mimosaPtmpClientAssocBW,_A3:mimosaPtmpClientRxBytes,_AA:mimosaPtmpClientTxBytes,_A4:mimosaPtmpClientRxPkts,_A5:mimosaPtmpClientTxPkts,_A7:mimosaPtmpClientRxPhyRate,_A9:mimosaPtmpClientTxPhyRate,_A8:mimosaPtmpClientTxAvgPer,_A6:mimosaPtmpClientRssiAvg,_AB:mimosaPtmpClientStatsLastUpdated,_AC:mimosaPtmpClientRssi1,_AD:mimosaPtmpClientRssi2,_AE:mimosaPtmpClientRssi3,_AF:mimosaPtmpClientRssi4,_AG:mimosaPtmpClientRxEVM1,_AH:mimosaPtmpClientRxEVM2,_AI:mimosaPtmpClientRxEVM3,_AJ:mimosaPtmpClientRxEVM4,_AK:mimosaPtmpClientRxNss,_AL:mimosaPtmpClientTxNss,_AM:mimosaPtmpClientRxMcs,_AN:mimosaPtmpClientTxMcs,'mimosaPtmpClientSNR':mimosaPtmpClientSNR,'mimosaPtmpMgmtInfo':mimosaPtmpMgmtInfo,_AO:mimosaPtmpMgmtIpAddress,_AP:mimosaPtmpMgmtIpNetmask,_AQ:mimosaPtmpMgmtIpGateway,_AR:mimosaPtmpMgmtIpMode,_AS:mimosaPtmpMgmtPrimaryDNS,_AT:mimosaPtmpMgmtSecondaryDNS,_AU:mimosaPtmpMgmtVlanStatus,_AV:mimosaPtmpMgmtVlanId,_AW:mimosaPtmpMgmtVlanPassthrough,_AX:mimosaPtmpMgmtEthernetMac,'mimosaPtmpConformance':mimosaPtmpConformance,'mimosaPtmpCompliances':mimosaPtmpCompliances,'mimosaPtmpCompliance':mimosaPtmpCompliance,'mimosaPtmpGroups':mimosaPtmpGroups,_AY:mimosaPtmpSsidGroup,_AZ:mimosaPtmpLinkInfoGroup,_Aa:mimosaPtmpChannelPowerGroup,_Ab:mimosaPtmpApStatsGroup,_Ad:mimosaPtmpClientInfoGroup,_Ac:mimosaPtmpClientStatsGroup,_Ae:mimosaPtmpMgmtInfoGroup})