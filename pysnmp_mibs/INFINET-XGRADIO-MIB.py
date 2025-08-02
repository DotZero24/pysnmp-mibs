_AD='xgRadioGroup'
_AC='xgTotalRxOctets'
_AB='xgTotalTxOctets'
_AA='xgCatalinaTemp'
_A9='xgBerAmcOneHourErr'
_A8='xgBerAmcTenMinutesErr'
_A7='xgBerAmcOneMinuteErr'
_A6='xgBerAmcWindowErr'
_A5='xgBerAmcCorrection'
_A4='xgADCRSSI'
_A3='xgTxPwrActual'
_A2='xgRxErrorABs'
_A1='xgRxOkABs'
_A0='xgABSRSSI'
_z='xgRfRxAccFER'
_y='xgRfDfsStatus'
_x='xgRfRxFrequency'
_w='xgRfTxFrequency'
_v='xgRfBadRxFrames'
_u='xgRfGoodRxFrames'
_t='xgTotalUlCapacity'
_s='xgTotalDlCapacity'
_r='xgTotalRxErrorABs'
_q='xgTotalRxOkABs'
_p='xgTotalRxPackets'
_o='xgTotalRxAirFrames'
_n='xgTotalTxPackets'
_m='xgTotalTxAirFrames'
_l='xgDlQuotaActual'
_k='xgDistance'
_j='xgLinkStatus'
_i='xgOwnRadioIfIndex'
_h='xgCcAmcStrategy'
_g='xgCcAmcMode'
_f='xgCcFreqUl'
_e='xgCcFreqDl'
_d='xgCcMaxTxPwr'
_c='xgChannelWidth'
_b='xgMaxDistance'
_a='xgFrameLength'
_Z='xgDlQuota'
_Y='xgQosStrategy'
_X='xgCellId'
_W='xgUnitType'
_V='qam1024-8-10'
_U='qam256-30-32'
_T='qam256-7-8'
_S='qam256-6-8'
_R='qam256-5-8'
_Q='qam64-4-6'
_P='qam16-3-4'
_O='qam16-1-2'
_N='qpsk-3-4'
_M='qpsk-1-2'
_L='qpsk-1-4'
_K='conservative'
_J='normal'
_I='xgRfChainStreamIndex'
_H='xgRfChainCarrierIndex'
_G='xgRfCarrierIndex'
_F='xgCCIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='INFINET-XGRADIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
xg,=mibBuilder.importSymbols('INFINET-XG-MIB','xg')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
xgRadio=ModuleIdentity((1,3,6,1,4,1,3942,4,1,1))
if mibBuilder.loadTexts:xgRadio.setRevisions(('2017-05-24 04:13','2017-03-23 11:39','2015-11-02 11:29','2015-10-13 11:01','2014-10-28 05:50','2014-09-30 03:50','2014-09-29 06:45','2014-09-04 05:02','2014-09-03 10:48','2014-08-29 02:40'))
_XgRfCfg_ObjectIdentity=ObjectIdentity
xgRfCfg=_XgRfCfg_ObjectIdentity((1,3,6,1,4,1,3942,4,1,1,1))
class _XgUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('master',0),('slave',1)))
_XgUnitType_Type.__name__=_D
_XgUnitType_Object=MibScalar
xgUnitType=_XgUnitType_Object((1,3,6,1,4,1,3942,4,1,1,1,1),_XgUnitType_Type())
xgUnitType.setMaxAccess(_E)
if mibBuilder.loadTexts:xgUnitType.setStatus(_A)
class _XgCellId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,167))
_XgCellId_Type.__name__=_D
_XgCellId_Object=MibScalar
xgCellId=_XgCellId_Object((1,3,6,1,4,1,3942,4,1,1,1,2),_XgCellId_Type())
xgCellId.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCellId.setStatus(_A)
class _XgQosStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_K,1),('aggressive',2),('off',3)))
_XgQosStrategy_Type.__name__=_D
_XgQosStrategy_Object=MibScalar
xgQosStrategy=_XgQosStrategy_Object((1,3,6,1,4,1,3942,4,1,1,1,3),_XgQosStrategy_Type())
xgQosStrategy.setMaxAccess(_E)
if mibBuilder.loadTexts:xgQosStrategy.setStatus(_A)
class _XgDlQuota_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_XgDlQuota_Type.__name__=_D
_XgDlQuota_Object=MibScalar
xgDlQuota=_XgDlQuota_Object((1,3,6,1,4,1,3942,4,1,1,1,4),_XgDlQuota_Type())
xgDlQuota.setMaxAccess(_E)
if mibBuilder.loadTexts:xgDlQuota.setStatus('deprecated')
class _XgFrameLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,8,10)));namedValues=NamedValues(*(('len-1-ms',1),('len-2-ms',2),('len-4-ms',4),('len-5-ms',5),('len-8-ms',8),('len-10-ms',10)))
_XgFrameLength_Type.__name__=_D
_XgFrameLength_Object=MibScalar
xgFrameLength=_XgFrameLength_Object((1,3,6,1,4,1,3942,4,1,1,1,5),_XgFrameLength_Type())
xgFrameLength.setMaxAccess(_E)
if mibBuilder.loadTexts:xgFrameLength.setStatus(_A)
class _XgMaxDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59600))
_XgMaxDistance_Type.__name__=_D
_XgMaxDistance_Object=MibScalar
xgMaxDistance=_XgMaxDistance_Object((1,3,6,1,4,1,3942,4,1,1,1,6),_XgMaxDistance_Type())
xgMaxDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:xgMaxDistance.setStatus(_A)
class _XgChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,40)));namedValues=NamedValues(*(('band-10-mhz',10),('band-20-mhz',20),('band-40-mhz',40)))
_XgChannelWidth_Type.__name__=_D
_XgChannelWidth_Object=MibScalar
xgChannelWidth=_XgChannelWidth_Object((1,3,6,1,4,1,3942,4,1,1,1,7),_XgChannelWidth_Type())
xgChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:xgChannelWidth.setStatus(_A)
_XgCarrierCfgTable_Object=MibTable
xgCarrierCfgTable=_XgCarrierCfgTable_Object((1,3,6,1,4,1,3942,4,1,1,1,8))
if mibBuilder.loadTexts:xgCarrierCfgTable.setStatus(_A)
_XgCarrierCfgEntry_Object=MibTableRow
xgCarrierCfgEntry=_XgCarrierCfgEntry_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1))
xgCarrierCfgEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:xgCarrierCfgEntry.setStatus(_A)
class _XgCCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_XgCCIndex_Type.__name__=_D
_XgCCIndex_Object=MibTableColumn
xgCCIndex=_XgCCIndex_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,1),_XgCCIndex_Type())
xgCCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgCCIndex.setStatus(_A)
class _XgCcMaxTxPwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,27000))
_XgCcMaxTxPwr_Type.__name__=_D
_XgCcMaxTxPwr_Object=MibTableColumn
xgCcMaxTxPwr=_XgCcMaxTxPwr_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,2),_XgCcMaxTxPwr_Type())
xgCcMaxTxPwr.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCcMaxTxPwr.setStatus(_A)
_XgCcFreqDl_Type=Integer32
_XgCcFreqDl_Object=MibTableColumn
xgCcFreqDl=_XgCcFreqDl_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,3),_XgCcFreqDl_Type())
xgCcFreqDl.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCcFreqDl.setStatus(_A)
_XgCcFreqUl_Type=Integer32
_XgCcFreqUl_Object=MibTableColumn
xgCcFreqUl=_XgCcFreqUl_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,4),_XgCcFreqUl_Type())
xgCcFreqUl.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCcFreqUl.setStatus(_A)
class _XgCcAmcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('auto',0),('manual',1)))
_XgCcAmcMode_Type.__name__=_D
_XgCcAmcMode_Object=MibTableColumn
xgCcAmcMode=_XgCcAmcMode_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,5),_XgCcAmcMode_Type())
xgCcAmcMode.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCcAmcMode.setStatus(_A)
class _XgCcAmcStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),('agressive',2)))
_XgCcAmcStrategy_Type.__name__=_D
_XgCcAmcStrategy_Object=MibTableColumn
xgCcAmcStrategy=_XgCcAmcStrategy_Object((1,3,6,1,4,1,3942,4,1,1,1,8,1,6),_XgCcAmcStrategy_Type())
xgCcAmcStrategy.setMaxAccess(_E)
if mibBuilder.loadTexts:xgCcAmcStrategy.setStatus(_A)
class _XgOwnRadioIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_XgOwnRadioIfIndex_Type.__name__=_D
_XgOwnRadioIfIndex_Object=MibScalar
xgOwnRadioIfIndex=_XgOwnRadioIfIndex_Object((1,3,6,1,4,1,3942,4,1,1,1,9),_XgOwnRadioIfIndex_Type())
xgOwnRadioIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgOwnRadioIfIndex.setStatus(_A)
_XgRfStat_ObjectIdentity=ObjectIdentity
xgRfStat=_XgRfStat_ObjectIdentity((1,3,6,1,4,1,3942,4,1,1,2))
class _XgLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('stopped',0),('starting',1),('down',2),('up',3),('error',4),('phy',5)))
_XgLinkStatus_Type.__name__=_D
_XgLinkStatus_Object=MibScalar
xgLinkStatus=_XgLinkStatus_Object((1,3,6,1,4,1,3942,4,1,1,2,1),_XgLinkStatus_Type())
xgLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgLinkStatus.setStatus(_A)
_XgDistance_Type=Integer32
_XgDistance_Object=MibScalar
xgDistance=_XgDistance_Object((1,3,6,1,4,1,3942,4,1,1,2,2),_XgDistance_Type())
xgDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:xgDistance.setStatus(_A)
class _XgDlQuotaActual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_XgDlQuotaActual_Type.__name__=_D
_XgDlQuotaActual_Object=MibScalar
xgDlQuotaActual=_XgDlQuotaActual_Object((1,3,6,1,4,1,3942,4,1,1,2,3),_XgDlQuotaActual_Type())
xgDlQuotaActual.setMaxAccess(_C)
if mibBuilder.loadTexts:xgDlQuotaActual.setStatus(_A)
_XgTotalTxAirFrames_Type=Counter32
_XgTotalTxAirFrames_Object=MibScalar
xgTotalTxAirFrames=_XgTotalTxAirFrames_Object((1,3,6,1,4,1,3942,4,1,1,2,4),_XgTotalTxAirFrames_Type())
xgTotalTxAirFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalTxAirFrames.setStatus(_A)
_XgTotalTxPackets_Type=Counter32
_XgTotalTxPackets_Object=MibScalar
xgTotalTxPackets=_XgTotalTxPackets_Object((1,3,6,1,4,1,3942,4,1,1,2,5),_XgTotalTxPackets_Type())
xgTotalTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalTxPackets.setStatus(_A)
_XgTotalRxAirFrames_Type=Counter32
_XgTotalRxAirFrames_Object=MibScalar
xgTotalRxAirFrames=_XgTotalRxAirFrames_Object((1,3,6,1,4,1,3942,4,1,1,2,6),_XgTotalRxAirFrames_Type())
xgTotalRxAirFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalRxAirFrames.setStatus(_A)
_XgTotalRxPackets_Type=Counter32
_XgTotalRxPackets_Object=MibScalar
xgTotalRxPackets=_XgTotalRxPackets_Object((1,3,6,1,4,1,3942,4,1,1,2,7),_XgTotalRxPackets_Type())
xgTotalRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalRxPackets.setStatus(_A)
_XgTotalRxOkABs_Type=Counter32
_XgTotalRxOkABs_Object=MibScalar
xgTotalRxOkABs=_XgTotalRxOkABs_Object((1,3,6,1,4,1,3942,4,1,1,2,8),_XgTotalRxOkABs_Type())
xgTotalRxOkABs.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalRxOkABs.setStatus(_A)
_XgTotalRxErrorABs_Type=Counter32
_XgTotalRxErrorABs_Object=MibScalar
xgTotalRxErrorABs=_XgTotalRxErrorABs_Object((1,3,6,1,4,1,3942,4,1,1,2,9),_XgTotalRxErrorABs_Type())
xgTotalRxErrorABs.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalRxErrorABs.setStatus(_A)
_XgTotalDlCapacity_Type=Integer32
_XgTotalDlCapacity_Object=MibScalar
xgTotalDlCapacity=_XgTotalDlCapacity_Object((1,3,6,1,4,1,3942,4,1,1,2,10),_XgTotalDlCapacity_Type())
xgTotalDlCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalDlCapacity.setStatus(_A)
_XgTotalUlCapacity_Type=Integer32
_XgTotalUlCapacity_Object=MibScalar
xgTotalUlCapacity=_XgTotalUlCapacity_Object((1,3,6,1,4,1,3942,4,1,1,2,11),_XgTotalUlCapacity_Type())
xgTotalUlCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalUlCapacity.setStatus(_A)
_XgRfCarrierStatTable_Object=MibTable
xgRfCarrierStatTable=_XgRfCarrierStatTable_Object((1,3,6,1,4,1,3942,4,1,1,2,12))
if mibBuilder.loadTexts:xgRfCarrierStatTable.setStatus(_A)
_XgRfCarrierStatEntry_Object=MibTableRow
xgRfCarrierStatEntry=_XgRfCarrierStatEntry_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1))
xgRfCarrierStatEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:xgRfCarrierStatEntry.setStatus(_A)
class _XgRfCarrierIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_XgRfCarrierIndex_Type.__name__=_D
_XgRfCarrierIndex_Object=MibTableColumn
xgRfCarrierIndex=_XgRfCarrierIndex_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,1),_XgRfCarrierIndex_Type())
xgRfCarrierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfCarrierIndex.setStatus(_A)
_XgRfGoodRxFrames_Type=Counter32
_XgRfGoodRxFrames_Object=MibTableColumn
xgRfGoodRxFrames=_XgRfGoodRxFrames_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,2),_XgRfGoodRxFrames_Type())
xgRfGoodRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfGoodRxFrames.setStatus(_A)
_XgRfBadRxFrames_Type=Counter32
_XgRfBadRxFrames_Object=MibTableColumn
xgRfBadRxFrames=_XgRfBadRxFrames_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,3),_XgRfBadRxFrames_Type())
xgRfBadRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfBadRxFrames.setStatus(_A)
_XgRfTxFrequency_Type=Integer32
_XgRfTxFrequency_Object=MibTableColumn
xgRfTxFrequency=_XgRfTxFrequency_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,4),_XgRfTxFrequency_Type())
xgRfTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfTxFrequency.setStatus(_A)
_XgRfRxFrequency_Type=Integer32
_XgRfRxFrequency_Object=MibTableColumn
xgRfRxFrequency=_XgRfRxFrequency_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,5),_XgRfRxFrequency_Type())
xgRfRxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfRxFrequency.setStatus(_A)
class _XgRfDfsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('dfs-no-init',0),('dfs-disabled',1),('dfs-enabled',2),('dfs-fg-radar-search',3),('dfs-fg-rssi-scan',4),('dfs-radar-found',5),('dfs-bg-rssi-v',6),('dfs-bg-rssi-h',7),('dfs-bg-rdrdt-main',8),('dfs-bg-rdrdt-announce',9),('dfs-bg-FF-ul',10),('dfs-bg-FF-dl',11)))
_XgRfDfsStatus_Type.__name__=_D
_XgRfDfsStatus_Object=MibTableColumn
xgRfDfsStatus=_XgRfDfsStatus_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,6),_XgRfDfsStatus_Type())
xgRfDfsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfDfsStatus.setStatus(_A)
_XgRfRxAccFER_Type=Integer32
_XgRfRxAccFER_Object=MibTableColumn
xgRfRxAccFER=_XgRfRxAccFER_Object((1,3,6,1,4,1,3942,4,1,1,2,12,1,7),_XgRfRxAccFER_Type())
xgRfRxAccFER.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfRxAccFER.setStatus(_A)
_XgRfChainStatTable_Object=MibTable
xgRfChainStatTable=_XgRfChainStatTable_Object((1,3,6,1,4,1,3942,4,1,1,2,13))
if mibBuilder.loadTexts:xgRfChainStatTable.setStatus(_A)
_XgRfChainStatEntry_Object=MibTableRow
xgRfChainStatEntry=_XgRfChainStatEntry_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1))
xgRfChainStatEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:xgRfChainStatEntry.setStatus(_A)
class _XgRfChainCarrierIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_XgRfChainCarrierIndex_Type.__name__=_D
_XgRfChainCarrierIndex_Object=MibTableColumn
xgRfChainCarrierIndex=_XgRfChainCarrierIndex_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,1),_XgRfChainCarrierIndex_Type())
xgRfChainCarrierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfChainCarrierIndex.setStatus(_A)
class _XgRfChainStreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_XgRfChainStreamIndex_Type.__name__=_D
_XgRfChainStreamIndex_Object=MibTableColumn
xgRfChainStreamIndex=_XgRfChainStreamIndex_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,2),_XgRfChainStreamIndex_Type())
xgRfChainStreamIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRfChainStreamIndex.setStatus(_A)
class _XgTxMCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10),(_V,11)))
_XgTxMCS_Type.__name__=_D
_XgTxMCS_Object=MibTableColumn
xgTxMCS=_XgTxMCS_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,3),_XgTxMCS_Type())
xgTxMCS.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTxMCS.setStatus(_A)
class _XgRxMCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10),(_V,11)))
_XgRxMCS_Type.__name__=_D
_XgRxMCS_Object=MibTableColumn
xgRxMCS=_XgRxMCS_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,4),_XgRxMCS_Type())
xgRxMCS.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRxMCS.setStatus(_A)
_XgCINR_Type=Integer32
_XgCINR_Object=MibTableColumn
xgCINR=_XgCINR_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,5),_XgCINR_Type())
xgCINR.setMaxAccess(_C)
if mibBuilder.loadTexts:xgCINR.setStatus(_A)
_XgABSRSSI_Type=Integer32
_XgABSRSSI_Object=MibTableColumn
xgABSRSSI=_XgABSRSSI_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,6),_XgABSRSSI_Type())
xgABSRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:xgABSRSSI.setStatus(_A)
_XgRxOkABs_Type=Counter32
_XgRxOkABs_Object=MibTableColumn
xgRxOkABs=_XgRxOkABs_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,7),_XgRxOkABs_Type())
xgRxOkABs.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRxOkABs.setStatus(_A)
_XgRxErrorABs_Type=Counter32
_XgRxErrorABs_Object=MibTableColumn
xgRxErrorABs=_XgRxErrorABs_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,8),_XgRxErrorABs_Type())
xgRxErrorABs.setMaxAccess(_C)
if mibBuilder.loadTexts:xgRxErrorABs.setStatus(_A)
class _XgTxPwrActual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2700))
_XgTxPwrActual_Type.__name__=_D
_XgTxPwrActual_Object=MibTableColumn
xgTxPwrActual=_XgTxPwrActual_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,9),_XgTxPwrActual_Type())
xgTxPwrActual.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTxPwrActual.setStatus(_A)
_XgADCRSSI_Type=Integer32
_XgADCRSSI_Object=MibTableColumn
xgADCRSSI=_XgADCRSSI_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,10),_XgADCRSSI_Type())
xgADCRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:xgADCRSSI.setStatus(_A)
_XgTxGain_Type=Integer32
_XgTxGain_Object=MibTableColumn
xgTxGain=_XgTxGain_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,11),_XgTxGain_Type())
xgTxGain.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTxGain.setStatus(_A)
_XgBerAmcCorrection_Type=Integer32
_XgBerAmcCorrection_Object=MibTableColumn
xgBerAmcCorrection=_XgBerAmcCorrection_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,12),_XgBerAmcCorrection_Type())
xgBerAmcCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:xgBerAmcCorrection.setStatus(_A)
class _XgBerAmcWindowErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100000000))
_XgBerAmcWindowErr_Type.__name__=_D
_XgBerAmcWindowErr_Object=MibTableColumn
xgBerAmcWindowErr=_XgBerAmcWindowErr_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,13),_XgBerAmcWindowErr_Type())
xgBerAmcWindowErr.setMaxAccess(_C)
if mibBuilder.loadTexts:xgBerAmcWindowErr.setStatus(_A)
class _XgBerAmcOneMinuteErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100000000))
_XgBerAmcOneMinuteErr_Type.__name__=_D
_XgBerAmcOneMinuteErr_Object=MibTableColumn
xgBerAmcOneMinuteErr=_XgBerAmcOneMinuteErr_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,14),_XgBerAmcOneMinuteErr_Type())
xgBerAmcOneMinuteErr.setMaxAccess(_C)
if mibBuilder.loadTexts:xgBerAmcOneMinuteErr.setStatus(_A)
class _XgBerAmcTenMinutesErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100000000))
_XgBerAmcTenMinutesErr_Type.__name__=_D
_XgBerAmcTenMinutesErr_Object=MibTableColumn
xgBerAmcTenMinutesErr=_XgBerAmcTenMinutesErr_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,15),_XgBerAmcTenMinutesErr_Type())
xgBerAmcTenMinutesErr.setMaxAccess(_C)
if mibBuilder.loadTexts:xgBerAmcTenMinutesErr.setStatus(_A)
class _XgBerAmcOneHourErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100000000))
_XgBerAmcOneHourErr_Type.__name__=_D
_XgBerAmcOneHourErr_Object=MibTableColumn
xgBerAmcOneHourErr=_XgBerAmcOneHourErr_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,16),_XgBerAmcOneHourErr_Type())
xgBerAmcOneHourErr.setMaxAccess(_C)
if mibBuilder.loadTexts:xgBerAmcOneHourErr.setStatus(_A)
_XgSTOD_Type=Integer32
_XgSTOD_Object=MibTableColumn
xgSTOD=_XgSTOD_Object((1,3,6,1,4,1,3942,4,1,1,2,13,1,17),_XgSTOD_Type())
xgSTOD.setMaxAccess(_C)
if mibBuilder.loadTexts:xgSTOD.setStatus(_A)
_XgCatalinaTemp_Type=Integer32
_XgCatalinaTemp_Object=MibScalar
xgCatalinaTemp=_XgCatalinaTemp_Object((1,3,6,1,4,1,3942,4,1,1,2,14),_XgCatalinaTemp_Type())
xgCatalinaTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:xgCatalinaTemp.setStatus(_A)
_XgTotalTxOctets_Type=Counter32
_XgTotalTxOctets_Object=MibScalar
xgTotalTxOctets=_XgTotalTxOctets_Object((1,3,6,1,4,1,3942,4,1,1,2,15),_XgTotalTxOctets_Type())
xgTotalTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalTxOctets.setStatus(_A)
_XgTotalRxOctets_Type=Counter32
_XgTotalRxOctets_Object=MibScalar
xgTotalRxOctets=_XgTotalRxOctets_Object((1,3,6,1,4,1,3942,4,1,1,2,16),_XgTotalRxOctets_Type())
xgTotalRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:xgTotalRxOctets.setStatus(_A)
_XgRadioMIBConformance_ObjectIdentity=ObjectIdentity
xgRadioMIBConformance=_XgRadioMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,4,1,1,3))
_XgRadioMIBCompliances_ObjectIdentity=ObjectIdentity
xgRadioMIBCompliances=_XgRadioMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3942,4,1,1,3,1))
_XgRadioMIBGroups_ObjectIdentity=ObjectIdentity
xgRadioMIBGroups=_XgRadioMIBGroups_ObjectIdentity((1,3,6,1,4,1,3942,4,1,1,3,2))
xgRadioGroup=ObjectGroup((1,3,6,1,4,1,3942,4,1,1,3,2,1))
xgRadioGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_F),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_G),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_H),(_B,_I),(_B,'xgTxMCS'),(_B,'xgRxMCS'),(_B,'xgCINR'),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,'xgTxGain'),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,'xgSTOD'),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:xgRadioGroup.setStatus(_A)
xgRadioMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3942,4,1,1,3,1,1))
xgRadioMIBCompliance.setObjects((_B,_AD))
if mibBuilder.loadTexts:xgRadioMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xgRadio':xgRadio,'xgRfCfg':xgRfCfg,_W:xgUnitType,_X:xgCellId,_Y:xgQosStrategy,_Z:xgDlQuota,_a:xgFrameLength,_b:xgMaxDistance,_c:xgChannelWidth,'xgCarrierCfgTable':xgCarrierCfgTable,'xgCarrierCfgEntry':xgCarrierCfgEntry,_F:xgCCIndex,_d:xgCcMaxTxPwr,_e:xgCcFreqDl,_f:xgCcFreqUl,_g:xgCcAmcMode,_h:xgCcAmcStrategy,_i:xgOwnRadioIfIndex,'xgRfStat':xgRfStat,_j:xgLinkStatus,_k:xgDistance,_l:xgDlQuotaActual,_m:xgTotalTxAirFrames,_n:xgTotalTxPackets,_o:xgTotalRxAirFrames,_p:xgTotalRxPackets,_q:xgTotalRxOkABs,_r:xgTotalRxErrorABs,_s:xgTotalDlCapacity,_t:xgTotalUlCapacity,'xgRfCarrierStatTable':xgRfCarrierStatTable,'xgRfCarrierStatEntry':xgRfCarrierStatEntry,_G:xgRfCarrierIndex,_u:xgRfGoodRxFrames,_v:xgRfBadRxFrames,_w:xgRfTxFrequency,_x:xgRfRxFrequency,_y:xgRfDfsStatus,_z:xgRfRxAccFER,'xgRfChainStatTable':xgRfChainStatTable,'xgRfChainStatEntry':xgRfChainStatEntry,_H:xgRfChainCarrierIndex,_I:xgRfChainStreamIndex,'xgTxMCS':xgTxMCS,'xgRxMCS':xgRxMCS,'xgCINR':xgCINR,_A0:xgABSRSSI,_A1:xgRxOkABs,_A2:xgRxErrorABs,_A3:xgTxPwrActual,_A4:xgADCRSSI,'xgTxGain':xgTxGain,_A5:xgBerAmcCorrection,_A6:xgBerAmcWindowErr,_A7:xgBerAmcOneMinuteErr,_A8:xgBerAmcTenMinutesErr,_A9:xgBerAmcOneHourErr,'xgSTOD':xgSTOD,_AA:xgCatalinaTemp,_AB:xgTotalTxOctets,_AC:xgTotalRxOctets,'xgRadioMIBConformance':xgRadioMIBConformance,'xgRadioMIBCompliances':xgRadioMIBCompliances,'xgRadioMIBCompliance':xgRadioMIBCompliance,'xgRadioMIBGroups':xgRadioMIBGroups,_AD:xgRadioGroup})