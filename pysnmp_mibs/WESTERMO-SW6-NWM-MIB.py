_AJ='groupCfgAfcNeighbourOffsetTable'
_AI='groupCfgAfcAfmTable'
_AH='groupCfgAfcGlobal'
_AG='groupCfgAfmAfcTable'
_AF='groupCfgAfmNeighbourTable'
_AE='groupCfgAfmRedundant'
_AD='groupCfgAfmGlobal'
_AC='groupCfgChannelCleaner'
_AB='groupRpcNvram'
_AA='groupRpcNwm'
_A9='groupRpcChannelManager'
_A8='groupCfgIdf'
_A7='groupCfgNwm'
_A6='groupCfgChannelManager'
_A5='groupCfgHttpReport'
_A4='rpcNvramFreqStatesReset'
_A3='rpcNwmHttpReport'
_A2='rpcChMgrHttpReport'
_A1='cfgAfcNeighbourOffset'
_A0='cfgAfcAfmName'
_z='cfgAfcAfmIp'
_y='cfgAfcReportEnabled'
_x='cfgAfcBackupFreq'
_w='cfgAfcIndex'
_v='cfgAfcName'
_u='cfgAfcEnabled'
_t='cfgAfmAfcName'
_s='cfgAfmAfcIp'
_r='cfgAfmNeighbourName'
_q='cfgAfmNeighbourIp'
_p='cfgAfmRedundantName'
_o='cfgAfmRedundantIp'
_n='cfgAfmReportEnabled'
_m='cfgAfmPrimary'
_l='cfgAfmAreaSize'
_k='cfgAfmIndex'
_j='cfgAfmName'
_i='cfgAfmEnabled'
_h='cfgChanCleanUsableFrequencyList'
_g='cfgChanCleanDfsUseNvram'
_f='cfgChanCleanEnabled'
_e='cfgNwmEnabled'
_d='cfgChMgrDfsUseNvram'
_c='cfgChMgrUsableFrequencyList'
_b='cfgChMgrEnabled'
_a='cfgIdfScanWorkSeconds'
_Z='cfgIdfScanWorkAction'
_Y='cfgIdfScanWorkFreq'
_X='cfgIdfTrigDomMaxRssiTh'
_W='cfgIdfTrigAlienMaxRssiTh'
_V='cfgIdfTrigDomLoadTh'
_U='cfgIdfTrigAlienLoadTh'
_T='cfgIdfTrigChanLoadTh'
_S='cfgIdfTrigRadarCntTh'
_R='cfgIdfName'
_Q='cfgIdfInterval'
_P='cfgIdfEnabled'
_O='cfgHttpRprtServerUrl'
_N='freqstate'
_M='cfgAfcNeighbourOffsetTableIndex'
_L='cfgAfcAfmTableIndex'
_K='cfgAfmAfcTableIndex'
_J='cfgAfmNeighbourTableIndex'
_I='cfgIdfScanWorkIndex'
_H='not-accessible'
_G='DisplayString'
_F='enabled'
_E='disabled'
_D='Integer32'
_C='read-write'
_B='WESTERMO-SW6-NWM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
nwm=ModuleIdentity((1,3,6,1,4,1,16177,1,400,2,3))
if mibBuilder.loadTexts:nwm.setRevisions(('2019-09-06 00:00',))
_Configuration_ObjectIdentity=ObjectIdentity
configuration=_Configuration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1))
_CfgHttpReport_ObjectIdentity=ObjectIdentity
cfgHttpReport=_CfgHttpReport_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,1))
class _CfgHttpRprtServerUrl_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgHttpRprtServerUrl_Type.__name__=_G
_CfgHttpRprtServerUrl_Object=MibScalar
cfgHttpRprtServerUrl=_CfgHttpRprtServerUrl_Object((1,3,6,1,4,1,16177,1,400,2,3,1,1,1),_CfgHttpRprtServerUrl_Type())
cfgHttpRprtServerUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgHttpRprtServerUrl.setStatus(_A)
_CfgChannelManager_ObjectIdentity=ObjectIdentity
cfgChannelManager=_CfgChannelManager_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,3))
class _CfgChMgrEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgChMgrEnabled_Type.__name__=_D
_CfgChMgrEnabled_Object=MibScalar
cfgChMgrEnabled=_CfgChMgrEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,3,1),_CfgChMgrEnabled_Type())
cfgChMgrEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChMgrEnabled.setStatus(_A)
class _CfgChMgrUsableFrequencyList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,23))
_CfgChMgrUsableFrequencyList_Type.__name__=_D
_CfgChMgrUsableFrequencyList_Object=MibScalar
cfgChMgrUsableFrequencyList=_CfgChMgrUsableFrequencyList_Object((1,3,6,1,4,1,16177,1,400,2,3,1,3,2),_CfgChMgrUsableFrequencyList_Type())
cfgChMgrUsableFrequencyList.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChMgrUsableFrequencyList.setStatus(_A)
class _CfgChMgrDfsUseNvram_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgChMgrDfsUseNvram_Type.__name__=_D
_CfgChMgrDfsUseNvram_Object=MibScalar
cfgChMgrDfsUseNvram=_CfgChMgrDfsUseNvram_Object((1,3,6,1,4,1,16177,1,400,2,3,1,3,3),_CfgChMgrDfsUseNvram_Type())
cfgChMgrDfsUseNvram.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChMgrDfsUseNvram.setStatus(_A)
_CfgNwm_ObjectIdentity=ObjectIdentity
cfgNwm=_CfgNwm_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,4))
class _CfgNwmEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgNwmEnabled_Type.__name__=_D
_CfgNwmEnabled_Object=MibScalar
cfgNwmEnabled=_CfgNwmEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,4,1),_CfgNwmEnabled_Type())
cfgNwmEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgNwmEnabled.setStatus(_A)
_CfgIdf_ObjectIdentity=ObjectIdentity
cfgIdf=_CfgIdf_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,5))
class _CfgIdfEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgIdfEnabled_Type.__name__=_D
_CfgIdfEnabled_Object=MibScalar
cfgIdfEnabled=_CfgIdfEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,1),_CfgIdfEnabled_Type())
cfgIdfEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfEnabled.setStatus(_A)
class _CfgIdfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CfgIdfInterval_Type.__name__=_D
_CfgIdfInterval_Object=MibScalar
cfgIdfInterval=_CfgIdfInterval_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,3),_CfgIdfInterval_Type())
cfgIdfInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfInterval.setStatus(_A)
class _CfgIdfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgIdfName_Type.__name__=_G
_CfgIdfName_Object=MibScalar
cfgIdfName=_CfgIdfName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,4),_CfgIdfName_Type())
cfgIdfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfName.setStatus(_A)
_CfgIdfTrigger_ObjectIdentity=ObjectIdentity
cfgIdfTrigger=_CfgIdfTrigger_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,5,5))
_CfgIdfTrigRadarCntTh_Type=Integer32
_CfgIdfTrigRadarCntTh_Object=MibScalar
cfgIdfTrigRadarCntTh=_CfgIdfTrigRadarCntTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,1),_CfgIdfTrigRadarCntTh_Type())
cfgIdfTrigRadarCntTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigRadarCntTh.setStatus(_A)
class _CfgIdfTrigChanLoadTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CfgIdfTrigChanLoadTh_Type.__name__=_D
_CfgIdfTrigChanLoadTh_Object=MibScalar
cfgIdfTrigChanLoadTh=_CfgIdfTrigChanLoadTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,2),_CfgIdfTrigChanLoadTh_Type())
cfgIdfTrigChanLoadTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigChanLoadTh.setStatus(_A)
class _CfgIdfTrigAlienLoadTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CfgIdfTrigAlienLoadTh_Type.__name__=_D
_CfgIdfTrigAlienLoadTh_Object=MibScalar
cfgIdfTrigAlienLoadTh=_CfgIdfTrigAlienLoadTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,3),_CfgIdfTrigAlienLoadTh_Type())
cfgIdfTrigAlienLoadTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigAlienLoadTh.setStatus(_A)
class _CfgIdfTrigDomLoadTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CfgIdfTrigDomLoadTh_Type.__name__=_D
_CfgIdfTrigDomLoadTh_Object=MibScalar
cfgIdfTrigDomLoadTh=_CfgIdfTrigDomLoadTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,4),_CfgIdfTrigDomLoadTh_Type())
cfgIdfTrigDomLoadTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigDomLoadTh.setStatus(_A)
class _CfgIdfTrigAlienMaxRssiTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CfgIdfTrigAlienMaxRssiTh_Type.__name__=_D
_CfgIdfTrigAlienMaxRssiTh_Object=MibScalar
cfgIdfTrigAlienMaxRssiTh=_CfgIdfTrigAlienMaxRssiTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,5),_CfgIdfTrigAlienMaxRssiTh_Type())
cfgIdfTrigAlienMaxRssiTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigAlienMaxRssiTh.setStatus(_A)
class _CfgIdfTrigDomMaxRssiTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CfgIdfTrigDomMaxRssiTh_Type.__name__=_D
_CfgIdfTrigDomMaxRssiTh_Object=MibScalar
cfgIdfTrigDomMaxRssiTh=_CfgIdfTrigDomMaxRssiTh_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,5,6),_CfgIdfTrigDomMaxRssiTh_Type())
cfgIdfTrigDomMaxRssiTh.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfTrigDomMaxRssiTh.setStatus(_A)
_CfgIdfScanWorkTable_Object=MibTable
cfgIdfScanWorkTable=_CfgIdfScanWorkTable_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10))
if mibBuilder.loadTexts:cfgIdfScanWorkTable.setStatus(_A)
_CfgIdfScanWorkTableEntry_Object=MibTableRow
cfgIdfScanWorkTableEntry=_CfgIdfScanWorkTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10,1))
cfgIdfScanWorkTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cfgIdfScanWorkTableEntry.setStatus(_A)
class _CfgIdfScanWorkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CfgIdfScanWorkIndex_Type.__name__=_D
_CfgIdfScanWorkIndex_Object=MibTableColumn
cfgIdfScanWorkIndex=_CfgIdfScanWorkIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10,1,1),_CfgIdfScanWorkIndex_Type())
cfgIdfScanWorkIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgIdfScanWorkIndex.setStatus(_A)
class _CfgIdfScanWorkFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6100))
_CfgIdfScanWorkFreq_Type.__name__=_D
_CfgIdfScanWorkFreq_Object=MibTableColumn
cfgIdfScanWorkFreq=_CfgIdfScanWorkFreq_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10,1,2),_CfgIdfScanWorkFreq_Type())
cfgIdfScanWorkFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfScanWorkFreq.setStatus(_A)
class _CfgIdfScanWorkAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*(('none',0),('spectral',2),('radar',3),('wifi',4)))
_CfgIdfScanWorkAction_Type.__name__=_D
_CfgIdfScanWorkAction_Object=MibTableColumn
cfgIdfScanWorkAction=_CfgIdfScanWorkAction_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10,1,3),_CfgIdfScanWorkAction_Type())
cfgIdfScanWorkAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfScanWorkAction.setStatus(_A)
class _CfgIdfScanWorkSeconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_CfgIdfScanWorkSeconds_Type.__name__=_D
_CfgIdfScanWorkSeconds_Object=MibTableColumn
cfgIdfScanWorkSeconds=_CfgIdfScanWorkSeconds_Object((1,3,6,1,4,1,16177,1,400,2,3,1,5,10,1,4),_CfgIdfScanWorkSeconds_Type())
cfgIdfScanWorkSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgIdfScanWorkSeconds.setStatus(_A)
_CfgChannelCleaner_ObjectIdentity=ObjectIdentity
cfgChannelCleaner=_CfgChannelCleaner_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,6))
class _CfgChanCleanEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgChanCleanEnabled_Type.__name__=_D
_CfgChanCleanEnabled_Object=MibScalar
cfgChanCleanEnabled=_CfgChanCleanEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,6,1),_CfgChanCleanEnabled_Type())
cfgChanCleanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChanCleanEnabled.setStatus(_A)
class _CfgChanCleanDfsUseNvram_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgChanCleanDfsUseNvram_Type.__name__=_D
_CfgChanCleanDfsUseNvram_Object=MibScalar
cfgChanCleanDfsUseNvram=_CfgChanCleanDfsUseNvram_Object((1,3,6,1,4,1,16177,1,400,2,3,1,6,9),_CfgChanCleanDfsUseNvram_Type())
cfgChanCleanDfsUseNvram.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChanCleanDfsUseNvram.setStatus(_A)
class _CfgChanCleanUsableFrequencyList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_CfgChanCleanUsableFrequencyList_Type.__name__=_D
_CfgChanCleanUsableFrequencyList_Object=MibScalar
cfgChanCleanUsableFrequencyList=_CfgChanCleanUsableFrequencyList_Object((1,3,6,1,4,1,16177,1,400,2,3,1,6,10),_CfgChanCleanUsableFrequencyList_Type())
cfgChanCleanUsableFrequencyList.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgChanCleanUsableFrequencyList.setStatus(_A)
_CfgAfm_ObjectIdentity=ObjectIdentity
cfgAfm=_CfgAfm_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,7))
class _CfgAfmEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgAfmEnabled_Type.__name__=_D
_CfgAfmEnabled_Object=MibScalar
cfgAfmEnabled=_CfgAfmEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,1),_CfgAfmEnabled_Type())
cfgAfmEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmEnabled.setStatus(_A)
class _CfgAfmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgAfmName_Type.__name__=_G
_CfgAfmName_Object=MibScalar
cfgAfmName=_CfgAfmName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,2),_CfgAfmName_Type())
cfgAfmName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmName.setStatus(_A)
_CfgAfmIndex_Type=Integer32
_CfgAfmIndex_Object=MibScalar
cfgAfmIndex=_CfgAfmIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,3),_CfgAfmIndex_Type())
cfgAfmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmIndex.setStatus(_A)
class _CfgAfmAreaSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CfgAfmAreaSize_Type.__name__=_D
_CfgAfmAreaSize_Object=MibScalar
cfgAfmAreaSize=_CfgAfmAreaSize_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,5),_CfgAfmAreaSize_Type())
cfgAfmAreaSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmAreaSize.setStatus(_A)
class _CfgAfmPrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgAfmPrimary_Type.__name__=_D
_CfgAfmPrimary_Object=MibScalar
cfgAfmPrimary=_CfgAfmPrimary_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,6),_CfgAfmPrimary_Type())
cfgAfmPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmPrimary.setStatus(_A)
class _CfgAfmReportEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgAfmReportEnabled_Type.__name__=_D
_CfgAfmReportEnabled_Object=MibScalar
cfgAfmReportEnabled=_CfgAfmReportEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,7),_CfgAfmReportEnabled_Type())
cfgAfmReportEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmReportEnabled.setStatus(_A)
_CfgAfmRedundant_ObjectIdentity=ObjectIdentity
cfgAfmRedundant=_CfgAfmRedundant_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,7,10))
_CfgAfmRedundantIp_Type=IpAddress
_CfgAfmRedundantIp_Object=MibScalar
cfgAfmRedundantIp=_CfgAfmRedundantIp_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,10,1),_CfgAfmRedundantIp_Type())
cfgAfmRedundantIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmRedundantIp.setStatus(_A)
_CfgAfmRedundantName_Type=DisplayString
_CfgAfmRedundantName_Object=MibScalar
cfgAfmRedundantName=_CfgAfmRedundantName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,10,2),_CfgAfmRedundantName_Type())
cfgAfmRedundantName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmRedundantName.setStatus(_A)
_CfgAfmNeighbourTable_Object=MibTable
cfgAfmNeighbourTable=_CfgAfmNeighbourTable_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,20))
if mibBuilder.loadTexts:cfgAfmNeighbourTable.setStatus(_A)
_CfgAfmNeighbourTableEntry_Object=MibTableRow
cfgAfmNeighbourTableEntry=_CfgAfmNeighbourTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,20,1))
cfgAfmNeighbourTableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cfgAfmNeighbourTableEntry.setStatus(_A)
class _CfgAfmNeighbourTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CfgAfmNeighbourTableIndex_Type.__name__=_D
_CfgAfmNeighbourTableIndex_Object=MibTableColumn
cfgAfmNeighbourTableIndex=_CfgAfmNeighbourTableIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,20,1,1),_CfgAfmNeighbourTableIndex_Type())
cfgAfmNeighbourTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgAfmNeighbourTableIndex.setStatus(_A)
_CfgAfmNeighbourIp_Type=IpAddress
_CfgAfmNeighbourIp_Object=MibTableColumn
cfgAfmNeighbourIp=_CfgAfmNeighbourIp_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,20,1,2),_CfgAfmNeighbourIp_Type())
cfgAfmNeighbourIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmNeighbourIp.setStatus(_A)
_CfgAfmNeighbourName_Type=DisplayString
_CfgAfmNeighbourName_Object=MibTableColumn
cfgAfmNeighbourName=_CfgAfmNeighbourName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,20,1,3),_CfgAfmNeighbourName_Type())
cfgAfmNeighbourName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmNeighbourName.setStatus(_A)
_CfgAfmAfcTable_Object=MibTable
cfgAfmAfcTable=_CfgAfmAfcTable_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,30))
if mibBuilder.loadTexts:cfgAfmAfcTable.setStatus(_A)
_CfgAfmAfcTableEntry_Object=MibTableRow
cfgAfmAfcTableEntry=_CfgAfmAfcTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,30,1))
cfgAfmAfcTableEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cfgAfmAfcTableEntry.setStatus(_A)
class _CfgAfmAfcTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CfgAfmAfcTableIndex_Type.__name__=_D
_CfgAfmAfcTableIndex_Object=MibTableColumn
cfgAfmAfcTableIndex=_CfgAfmAfcTableIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,30,1,1),_CfgAfmAfcTableIndex_Type())
cfgAfmAfcTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgAfmAfcTableIndex.setStatus(_A)
class _CfgAfmAfcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgAfmAfcName_Type.__name__=_G
_CfgAfmAfcName_Object=MibTableColumn
cfgAfmAfcName=_CfgAfmAfcName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,30,1,2),_CfgAfmAfcName_Type())
cfgAfmAfcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmAfcName.setStatus(_A)
_CfgAfmAfcIp_Type=IpAddress
_CfgAfmAfcIp_Object=MibTableColumn
cfgAfmAfcIp=_CfgAfmAfcIp_Object((1,3,6,1,4,1,16177,1,400,2,3,1,7,30,1,3),_CfgAfmAfcIp_Type())
cfgAfmAfcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfmAfcIp.setStatus(_A)
_CfgAfc_ObjectIdentity=ObjectIdentity
cfgAfc=_CfgAfc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,1,8))
class _CfgAfcEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgAfcEnabled_Type.__name__=_D
_CfgAfcEnabled_Object=MibScalar
cfgAfcEnabled=_CfgAfcEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,1),_CfgAfcEnabled_Type())
cfgAfcEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcEnabled.setStatus(_A)
class _CfgAfcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgAfcName_Type.__name__=_G
_CfgAfcName_Object=MibScalar
cfgAfcName=_CfgAfcName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,2),_CfgAfcName_Type())
cfgAfcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcName.setStatus(_A)
class _CfgAfcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CfgAfcIndex_Type.__name__=_D
_CfgAfcIndex_Object=MibScalar
cfgAfcIndex=_CfgAfcIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,3),_CfgAfcIndex_Type())
cfgAfcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcIndex.setStatus(_A)
class _CfgAfcBackupFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6100))
_CfgAfcBackupFreq_Type.__name__=_D
_CfgAfcBackupFreq_Object=MibScalar
cfgAfcBackupFreq=_CfgAfcBackupFreq_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,5),_CfgAfcBackupFreq_Type())
cfgAfcBackupFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcBackupFreq.setStatus(_A)
class _CfgAfcReportEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CfgAfcReportEnabled_Type.__name__=_D
_CfgAfcReportEnabled_Object=MibScalar
cfgAfcReportEnabled=_CfgAfcReportEnabled_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,6),_CfgAfcReportEnabled_Type())
cfgAfcReportEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcReportEnabled.setStatus(_A)
_CfgAfcAfmTable_Object=MibTable
cfgAfcAfmTable=_CfgAfcAfmTable_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,10))
if mibBuilder.loadTexts:cfgAfcAfmTable.setStatus(_A)
_CfgAfcAfmTableEntry_Object=MibTableRow
cfgAfcAfmTableEntry=_CfgAfcAfmTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,10,1))
cfgAfcAfmTableEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cfgAfcAfmTableEntry.setStatus(_A)
class _CfgAfcAfmTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CfgAfcAfmTableIndex_Type.__name__=_D
_CfgAfcAfmTableIndex_Object=MibTableColumn
cfgAfcAfmTableIndex=_CfgAfcAfmTableIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,10,1,1),_CfgAfcAfmTableIndex_Type())
cfgAfcAfmTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgAfcAfmTableIndex.setStatus(_A)
class _CfgAfcAfmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfgAfcAfmName_Type.__name__=_G
_CfgAfcAfmName_Object=MibTableColumn
cfgAfcAfmName=_CfgAfcAfmName_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,10,1,2),_CfgAfcAfmName_Type())
cfgAfcAfmName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcAfmName.setStatus(_A)
_CfgAfcAfmIp_Type=IpAddress
_CfgAfcAfmIp_Object=MibTableColumn
cfgAfcAfmIp=_CfgAfcAfmIp_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,10,1,3),_CfgAfcAfmIp_Type())
cfgAfcAfmIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcAfmIp.setStatus(_A)
_CfgAfcNeighbourOffsetTable_Object=MibTable
cfgAfcNeighbourOffsetTable=_CfgAfcNeighbourOffsetTable_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,40))
if mibBuilder.loadTexts:cfgAfcNeighbourOffsetTable.setStatus(_A)
_CfgAfcNeighbourOffsetTableEntry_Object=MibTableRow
cfgAfcNeighbourOffsetTableEntry=_CfgAfcNeighbourOffsetTableEntry_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,40,1))
cfgAfcNeighbourOffsetTableEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cfgAfcNeighbourOffsetTableEntry.setStatus(_A)
class _CfgAfcNeighbourOffsetTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_CfgAfcNeighbourOffsetTableIndex_Type.__name__=_D
_CfgAfcNeighbourOffsetTableIndex_Object=MibTableColumn
cfgAfcNeighbourOffsetTableIndex=_CfgAfcNeighbourOffsetTableIndex_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,40,1,1),_CfgAfcNeighbourOffsetTableIndex_Type())
cfgAfcNeighbourOffsetTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cfgAfcNeighbourOffsetTableIndex.setStatus(_A)
class _CfgAfcNeighbourOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,15))
_CfgAfcNeighbourOffset_Type.__name__=_D
_CfgAfcNeighbourOffset_Object=MibTableColumn
cfgAfcNeighbourOffset=_CfgAfcNeighbourOffset_Object((1,3,6,1,4,1,16177,1,400,2,3,1,8,40,1,2),_CfgAfcNeighbourOffset_Type())
cfgAfcNeighbourOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:cfgAfcNeighbourOffset.setStatus(_A)
_Rpc_ObjectIdentity=ObjectIdentity
rpc=_Rpc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,3))
_RpcChannelManager_ObjectIdentity=ObjectIdentity
rpcChannelManager=_RpcChannelManager_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,3,1))
class _RpcChMgrHttpReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nop',0),(_N,1),('channels',2)))
_RpcChMgrHttpReport_Type.__name__=_D
_RpcChMgrHttpReport_Object=MibScalar
rpcChMgrHttpReport=_RpcChMgrHttpReport_Object((1,3,6,1,4,1,16177,1,400,2,3,3,1,1),_RpcChMgrHttpReport_Type())
rpcChMgrHttpReport.setMaxAccess(_C)
if mibBuilder.loadTexts:rpcChMgrHttpReport.setStatus(_A)
_RpcNwm_ObjectIdentity=ObjectIdentity
rpcNwm=_RpcNwm_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,3,2))
class _RpcNwmHttpReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nop',0),('status',1),(_N,2)))
_RpcNwmHttpReport_Type.__name__=_D
_RpcNwmHttpReport_Object=MibScalar
rpcNwmHttpReport=_RpcNwmHttpReport_Object((1,3,6,1,4,1,16177,1,400,2,3,3,2,1),_RpcNwmHttpReport_Type())
rpcNwmHttpReport.setMaxAccess(_C)
if mibBuilder.loadTexts:rpcNwmHttpReport.setStatus(_A)
_RpcNvram_ObjectIdentity=ObjectIdentity
rpcNvram=_RpcNvram_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,3,3))
class _RpcNvramFreqStatesReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('reset',0))
_RpcNvramFreqStatesReset_Type.__name__=_D
_RpcNvramFreqStatesReset_Object=MibScalar
rpcNvramFreqStatesReset=_RpcNvramFreqStatesReset_Object((1,3,6,1,4,1,16177,1,400,2,3,3,3,1),_RpcNvramFreqStatesReset_Type())
rpcNvramFreqStatesReset.setMaxAccess(_C)
if mibBuilder.loadTexts:rpcNvramFreqStatesReset.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000))
_Groups_ObjectIdentity=ObjectIdentity
groups=_Groups_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,1))
_GroupConfiguration_ObjectIdentity=ObjectIdentity
groupConfiguration=_GroupConfiguration_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1))
_GroupCfgAfm_ObjectIdentity=ObjectIdentity
groupCfgAfm=_GroupCfgAfm_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,7))
_GroupCfgAfc_ObjectIdentity=ObjectIdentity
groupCfgAfc=_GroupCfgAfc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,8))
_GroupRpc_ObjectIdentity=ObjectIdentity
groupRpc=_GroupRpc_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,1,2))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,16177,1,400,2,3,10000,2))
groupCfgHttpReport=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,1))
groupCfgHttpReport.setObjects((_B,_O))
if mibBuilder.loadTexts:groupCfgHttpReport.setStatus(_A)
groupCfgIdf=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,2))
groupCfgIdf.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:groupCfgIdf.setStatus(_A)
groupCfgChannelManager=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,4))
groupCfgChannelManager.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:groupCfgChannelManager.setStatus(_A)
groupCfgNwm=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,5))
groupCfgNwm.setObjects((_B,_e))
if mibBuilder.loadTexts:groupCfgNwm.setStatus(_A)
groupCfgChannelCleaner=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,6))
groupCfgChannelCleaner.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:groupCfgChannelCleaner.setStatus(_A)
groupCfgAfmGlobal=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,7,1))
groupCfgAfmGlobal.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:groupCfgAfmGlobal.setStatus(_A)
groupCfgAfmRedundant=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,7,2))
groupCfgAfmRedundant.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:groupCfgAfmRedundant.setStatus(_A)
groupCfgAfmNeighbourTable=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,7,3))
groupCfgAfmNeighbourTable.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:groupCfgAfmNeighbourTable.setStatus(_A)
groupCfgAfmAfcTable=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,7,4))
groupCfgAfmAfcTable.setObjects(*((_B,_s),(_B,_t)))
if mibBuilder.loadTexts:groupCfgAfmAfcTable.setStatus(_A)
groupCfgAfcGlobal=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,8,1))
groupCfgAfcGlobal.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:groupCfgAfcGlobal.setStatus(_A)
groupCfgAfcAfmTable=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,8,2))
groupCfgAfcAfmTable.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:groupCfgAfcAfmTable.setStatus(_A)
groupCfgAfcNeighbourOffsetTable=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,1,8,4))
groupCfgAfcNeighbourOffsetTable.setObjects((_B,_A1))
if mibBuilder.loadTexts:groupCfgAfcNeighbourOffsetTable.setStatus(_A)
groupRpcChannelManager=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,2,1))
groupRpcChannelManager.setObjects((_B,_A2))
if mibBuilder.loadTexts:groupRpcChannelManager.setStatus(_A)
groupRpcNwm=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,2,2))
groupRpcNwm.setObjects((_B,_A3))
if mibBuilder.loadTexts:groupRpcNwm.setStatus(_A)
groupRpcNvram=ObjectGroup((1,3,6,1,4,1,16177,1,400,2,3,10000,1,2,3))
groupRpcNvram.setObjects((_B,_A4))
if mibBuilder.loadTexts:groupRpcNvram.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,16177,1,400,2,3,10000,2,1))
compliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nwm':nwm,'configuration':configuration,'cfgHttpReport':cfgHttpReport,_O:cfgHttpRprtServerUrl,'cfgChannelManager':cfgChannelManager,_b:cfgChMgrEnabled,_c:cfgChMgrUsableFrequencyList,_d:cfgChMgrDfsUseNvram,'cfgNwm':cfgNwm,_e:cfgNwmEnabled,'cfgIdf':cfgIdf,_P:cfgIdfEnabled,_Q:cfgIdfInterval,_R:cfgIdfName,'cfgIdfTrigger':cfgIdfTrigger,_S:cfgIdfTrigRadarCntTh,_T:cfgIdfTrigChanLoadTh,_U:cfgIdfTrigAlienLoadTh,_V:cfgIdfTrigDomLoadTh,_W:cfgIdfTrigAlienMaxRssiTh,_X:cfgIdfTrigDomMaxRssiTh,'cfgIdfScanWorkTable':cfgIdfScanWorkTable,'cfgIdfScanWorkTableEntry':cfgIdfScanWorkTableEntry,_I:cfgIdfScanWorkIndex,_Y:cfgIdfScanWorkFreq,_Z:cfgIdfScanWorkAction,_a:cfgIdfScanWorkSeconds,'cfgChannelCleaner':cfgChannelCleaner,_f:cfgChanCleanEnabled,_g:cfgChanCleanDfsUseNvram,_h:cfgChanCleanUsableFrequencyList,'cfgAfm':cfgAfm,_i:cfgAfmEnabled,_j:cfgAfmName,_k:cfgAfmIndex,_l:cfgAfmAreaSize,_m:cfgAfmPrimary,_n:cfgAfmReportEnabled,'cfgAfmRedundant':cfgAfmRedundant,_o:cfgAfmRedundantIp,_p:cfgAfmRedundantName,'cfgAfmNeighbourTable':cfgAfmNeighbourTable,'cfgAfmNeighbourTableEntry':cfgAfmNeighbourTableEntry,_J:cfgAfmNeighbourTableIndex,_q:cfgAfmNeighbourIp,_r:cfgAfmNeighbourName,'cfgAfmAfcTable':cfgAfmAfcTable,'cfgAfmAfcTableEntry':cfgAfmAfcTableEntry,_K:cfgAfmAfcTableIndex,_t:cfgAfmAfcName,_s:cfgAfmAfcIp,'cfgAfc':cfgAfc,_u:cfgAfcEnabled,_v:cfgAfcName,_w:cfgAfcIndex,_x:cfgAfcBackupFreq,_y:cfgAfcReportEnabled,'cfgAfcAfmTable':cfgAfcAfmTable,'cfgAfcAfmTableEntry':cfgAfcAfmTableEntry,_L:cfgAfcAfmTableIndex,_A0:cfgAfcAfmName,_z:cfgAfcAfmIp,'cfgAfcNeighbourOffsetTable':cfgAfcNeighbourOffsetTable,'cfgAfcNeighbourOffsetTableEntry':cfgAfcNeighbourOffsetTableEntry,_M:cfgAfcNeighbourOffsetTableIndex,_A1:cfgAfcNeighbourOffset,'rpc':rpc,'rpcChannelManager':rpcChannelManager,_A2:rpcChMgrHttpReport,'rpcNwm':rpcNwm,_A3:rpcNwmHttpReport,'rpcNvram':rpcNvram,_A4:rpcNvramFreqStatesReset,'conformance':conformance,'groups':groups,'groupConfiguration':groupConfiguration,_A5:groupCfgHttpReport,_A8:groupCfgIdf,_A6:groupCfgChannelManager,_A7:groupCfgNwm,_AC:groupCfgChannelCleaner,'groupCfgAfm':groupCfgAfm,_AD:groupCfgAfmGlobal,_AE:groupCfgAfmRedundant,_AF:groupCfgAfmNeighbourTable,_AG:groupCfgAfmAfcTable,'groupCfgAfc':groupCfgAfc,_AH:groupCfgAfcGlobal,_AI:groupCfgAfcAfmTable,_AJ:groupCfgAfcNeighbourOffsetTable,'groupRpc':groupRpc,_A9:groupRpcChannelManager,_AA:groupRpcNwm,_AB:groupRpcNvram,'compliances':compliances,'compliance':compliance})