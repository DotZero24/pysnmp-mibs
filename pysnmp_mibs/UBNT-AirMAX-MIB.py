_AX='ubntAirMAXStatusGroup'
_AW='ubntGpsHDOP'
_AV='ubntGpsSatsTracked'
_AU='ubntGpsSatsVisible'
_AT='ubntGpsAltFeet'
_AS='ubntGpsAltMeters'
_AR='ubntGpsLon'
_AQ='ubntGpsLat'
_AP='ubntGpsFix'
_AO='ubntGpsStatus'
_AN='ubntHostTemperature'
_AM='ubntHostCpuLoad'
_AL='ubntHostNetrole'
_AK='ubntHostLocaltime'
_AJ='ubntWlStatStaCount'
_AI='ubntWlStatChanWidth'
_AH='ubntWlStatApRepeater'
_AG='ubntWlStatWdsEnabled'
_AF='ubntWlStatSecurity'
_AE='ubntWlStatRxRate'
_AD='ubntWlStatTxRate'
_AC='ubntWlStatNoiseFloor'
_AB='ubntWlStatCcq'
_AA='ubntWlStatRssi'
_A9='ubntWlStatSignal'
_A8='ubntWlStatApMac'
_A7='ubntWlStatHideSsid'
_A6='ubntWlStatSsid'
_A5='ubntAirSelInterval'
_A4='ubntAirSelEnabled'
_A3='ubntAirSyncUpUtil'
_A2='ubntAirSyncDownUtil'
_A1='ubntAirSyncCount'
_A0='ubntAirSyncMode'
_z='ubntAirMaxTdd'
_y='ubntAirMaxGpsSync'
_x='ubntAirMaxAirtime'
_w='ubntAirMaxNoAck'
_v='ubntAirMaxPriority'
_u='ubntAirMaxCapacity'
_t='ubntAirMaxQuality'
_s='ubntAirMaxEnabled'
_r='ubntRadioRssiExt'
_q='ubntRadioRssiMgmt'
_p='ubntRadioRssi'
_o='ubntRadioAntenna'
_n='ubntRadioChainmask'
_m='ubntRadioDistance'
_l='ubntRadioTxPower'
_k='ubntRadioDfsEnabled'
_j='ubntRadioFreq'
_i='ubntRadioCCode'
_h='ubntRadioMode'
_g='ubntStaTxLatency'
_f='ubntStaRxAirtime'
_e='ubntStaTxAirtime'
_d='ubntStaRxCapacity'
_c='ubntStaTxCapacity'
_b='ubntStaLocalCINR'
_a='ubntStaConnTime'
_Z='ubntStaRxBytes'
_Y='ubntStaTxBytes'
_X='ubntStaRxRate'
_W='ubntStaTxRate'
_V='ubntStaLastIp'
_U='ubntStaAmc'
_T='ubntStaAmq'
_S='ubntStaAmp'
_R='ubntStaCcq'
_Q='ubntStaDistance'
_P='ubntStaNoiseFloor'
_O='ubntStaSignal'
_N='ubntStaName'
_M='unknown'
_L='ubntStaMac'
_K='ubntAirMaxIfIndex'
_J='ubntAirSelIfIndex'
_I='ubntAirSyncIfIndex'
_H='ubntRadioRssiIndex'
_G='ubntWlStatIndex'
_F='ubntRadioIndex'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='UBNT-AirMAX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ubntAirosGroups,ubntMIB=mibBuilder.importSymbols('UBNT-MIB','ubntAirosGroups','ubntMIB')
ubntAirMAX=ModuleIdentity((1,3,6,1,4,1,41112,1,4))
if mibBuilder.loadTexts:ubntAirMAX.setRevisions(('2017-10-03 00:00',))
_UbntRadioTable_Object=MibTable
ubntRadioTable=_UbntRadioTable_Object((1,3,6,1,4,1,41112,1,4,1))
if mibBuilder.loadTexts:ubntRadioTable.setStatus(_A)
_UbntRadioEntry_Object=MibTableRow
ubntRadioEntry=_UbntRadioEntry_Object((1,3,6,1,4,1,41112,1,4,1,1))
ubntRadioEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ubntRadioEntry.setStatus(_A)
class _UbntRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntRadioIndex_Type.__name__=_D
_UbntRadioIndex_Object=MibTableColumn
ubntRadioIndex=_UbntRadioIndex_Object((1,3,6,1,4,1,41112,1,4,1,1,1),_UbntRadioIndex_Type())
ubntRadioIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntRadioIndex.setStatus(_A)
class _UbntRadioMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sta',1),('ap',2),('aprepeater',3),('apwds',4)))
_UbntRadioMode_Type.__name__=_D
_UbntRadioMode_Object=MibTableColumn
ubntRadioMode=_UbntRadioMode_Object((1,3,6,1,4,1,41112,1,4,1,1,2),_UbntRadioMode_Type())
ubntRadioMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioMode.setStatus(_A)
_UbntRadioCCode_Type=Integer32
_UbntRadioCCode_Object=MibTableColumn
ubntRadioCCode=_UbntRadioCCode_Object((1,3,6,1,4,1,41112,1,4,1,1,3),_UbntRadioCCode_Type())
ubntRadioCCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioCCode.setStatus(_A)
class _UbntRadioFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UbntRadioFreq_Type.__name__=_D
_UbntRadioFreq_Object=MibTableColumn
ubntRadioFreq=_UbntRadioFreq_Object((1,3,6,1,4,1,41112,1,4,1,1,4),_UbntRadioFreq_Type())
ubntRadioFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioFreq.setStatus(_A)
_UbntRadioDfsEnabled_Type=TruthValue
_UbntRadioDfsEnabled_Object=MibTableColumn
ubntRadioDfsEnabled=_UbntRadioDfsEnabled_Object((1,3,6,1,4,1,41112,1,4,1,1,5),_UbntRadioDfsEnabled_Type())
ubntRadioDfsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioDfsEnabled.setStatus(_A)
class _UbntRadioTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UbntRadioTxPower_Type.__name__=_D
_UbntRadioTxPower_Object=MibTableColumn
ubntRadioTxPower=_UbntRadioTxPower_Object((1,3,6,1,4,1,41112,1,4,1,1,6),_UbntRadioTxPower_Type())
ubntRadioTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioTxPower.setStatus(_A)
class _UbntRadioDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UbntRadioDistance_Type.__name__=_D
_UbntRadioDistance_Object=MibTableColumn
ubntRadioDistance=_UbntRadioDistance_Object((1,3,6,1,4,1,41112,1,4,1,1,7),_UbntRadioDistance_Type())
ubntRadioDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioDistance.setStatus(_A)
class _UbntRadioChainmask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntRadioChainmask_Type.__name__=_D
_UbntRadioChainmask_Object=MibTableColumn
ubntRadioChainmask=_UbntRadioChainmask_Object((1,3,6,1,4,1,41112,1,4,1,1,8),_UbntRadioChainmask_Type())
ubntRadioChainmask.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioChainmask.setStatus(_A)
_UbntRadioAntenna_Type=DisplayString
_UbntRadioAntenna_Object=MibTableColumn
ubntRadioAntenna=_UbntRadioAntenna_Object((1,3,6,1,4,1,41112,1,4,1,1,9),_UbntRadioAntenna_Type())
ubntRadioAntenna.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioAntenna.setStatus(_A)
_UbntRadioRssiTable_Object=MibTable
ubntRadioRssiTable=_UbntRadioRssiTable_Object((1,3,6,1,4,1,41112,1,4,2))
if mibBuilder.loadTexts:ubntRadioRssiTable.setStatus(_A)
_UbntRadioRssiEntry_Object=MibTableRow
ubntRadioRssiEntry=_UbntRadioRssiEntry_Object((1,3,6,1,4,1,41112,1,4,2,1))
ubntRadioRssiEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:ubntRadioRssiEntry.setStatus(_A)
class _UbntRadioRssiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntRadioRssiIndex_Type.__name__=_D
_UbntRadioRssiIndex_Object=MibTableColumn
ubntRadioRssiIndex=_UbntRadioRssiIndex_Object((1,3,6,1,4,1,41112,1,4,2,1,1),_UbntRadioRssiIndex_Type())
ubntRadioRssiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntRadioRssiIndex.setStatus(_A)
_UbntRadioRssi_Type=Integer32
_UbntRadioRssi_Object=MibTableColumn
ubntRadioRssi=_UbntRadioRssi_Object((1,3,6,1,4,1,41112,1,4,2,1,2),_UbntRadioRssi_Type())
ubntRadioRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioRssi.setStatus(_A)
_UbntRadioRssiMgmt_Type=Integer32
_UbntRadioRssiMgmt_Object=MibTableColumn
ubntRadioRssiMgmt=_UbntRadioRssiMgmt_Object((1,3,6,1,4,1,41112,1,4,2,1,3),_UbntRadioRssiMgmt_Type())
ubntRadioRssiMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioRssiMgmt.setStatus(_A)
_UbntRadioRssiExt_Type=Integer32
_UbntRadioRssiExt_Object=MibTableColumn
ubntRadioRssiExt=_UbntRadioRssiExt_Object((1,3,6,1,4,1,41112,1,4,2,1,4),_UbntRadioRssiExt_Type())
ubntRadioRssiExt.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntRadioRssiExt.setStatus(_A)
_UbntAirSyncTable_Object=MibTable
ubntAirSyncTable=_UbntAirSyncTable_Object((1,3,6,1,4,1,41112,1,4,3))
if mibBuilder.loadTexts:ubntAirSyncTable.setStatus(_A)
_UbntAirSyncEntry_Object=MibTableRow
ubntAirSyncEntry=_UbntAirSyncEntry_Object((1,3,6,1,4,1,41112,1,4,3,1))
ubntAirSyncEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ubntAirSyncEntry.setStatus(_A)
class _UbntAirSyncIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntAirSyncIfIndex_Type.__name__=_D
_UbntAirSyncIfIndex_Object=MibTableColumn
ubntAirSyncIfIndex=_UbntAirSyncIfIndex_Object((1,3,6,1,4,1,41112,1,4,3,1,1),_UbntAirSyncIfIndex_Type())
ubntAirSyncIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntAirSyncIfIndex.setStatus(_A)
class _UbntAirSyncMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('master',1),('slave',2)))
_UbntAirSyncMode_Type.__name__=_D
_UbntAirSyncMode_Object=MibTableColumn
ubntAirSyncMode=_UbntAirSyncMode_Object((1,3,6,1,4,1,41112,1,4,3,1,2),_UbntAirSyncMode_Type())
ubntAirSyncMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSyncMode.setStatus(_A)
class _UbntAirSyncCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_UbntAirSyncCount_Type.__name__=_D
_UbntAirSyncCount_Object=MibTableColumn
ubntAirSyncCount=_UbntAirSyncCount_Object((1,3,6,1,4,1,41112,1,4,3,1,3),_UbntAirSyncCount_Type())
ubntAirSyncCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSyncCount.setStatus(_A)
class _UbntAirSyncDownUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UbntAirSyncDownUtil_Type.__name__=_D
_UbntAirSyncDownUtil_Object=MibTableColumn
ubntAirSyncDownUtil=_UbntAirSyncDownUtil_Object((1,3,6,1,4,1,41112,1,4,3,1,4),_UbntAirSyncDownUtil_Type())
ubntAirSyncDownUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSyncDownUtil.setStatus(_A)
class _UbntAirSyncUpUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UbntAirSyncUpUtil_Type.__name__=_D
_UbntAirSyncUpUtil_Object=MibTableColumn
ubntAirSyncUpUtil=_UbntAirSyncUpUtil_Object((1,3,6,1,4,1,41112,1,4,3,1,5),_UbntAirSyncUpUtil_Type())
ubntAirSyncUpUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSyncUpUtil.setStatus(_A)
_UbntAirSelTable_Object=MibTable
ubntAirSelTable=_UbntAirSelTable_Object((1,3,6,1,4,1,41112,1,4,4))
if mibBuilder.loadTexts:ubntAirSelTable.setStatus(_A)
_UbntAirSelEntry_Object=MibTableRow
ubntAirSelEntry=_UbntAirSelEntry_Object((1,3,6,1,4,1,41112,1,4,4,1))
ubntAirSelEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ubntAirSelEntry.setStatus(_A)
class _UbntAirSelIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntAirSelIfIndex_Type.__name__=_D
_UbntAirSelIfIndex_Object=MibTableColumn
ubntAirSelIfIndex=_UbntAirSelIfIndex_Object((1,3,6,1,4,1,41112,1,4,4,1,1),_UbntAirSelIfIndex_Type())
ubntAirSelIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntAirSelIfIndex.setStatus(_A)
_UbntAirSelEnabled_Type=TruthValue
_UbntAirSelEnabled_Object=MibTableColumn
ubntAirSelEnabled=_UbntAirSelEnabled_Object((1,3,6,1,4,1,41112,1,4,4,1,2),_UbntAirSelEnabled_Type())
ubntAirSelEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSelEnabled.setStatus(_A)
class _UbntAirSelInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UbntAirSelInterval_Type.__name__=_D
_UbntAirSelInterval_Object=MibTableColumn
ubntAirSelInterval=_UbntAirSelInterval_Object((1,3,6,1,4,1,41112,1,4,4,1,3),_UbntAirSelInterval_Type())
ubntAirSelInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirSelInterval.setStatus(_A)
_UbntWlStatTable_Object=MibTable
ubntWlStatTable=_UbntWlStatTable_Object((1,3,6,1,4,1,41112,1,4,5))
if mibBuilder.loadTexts:ubntWlStatTable.setStatus(_A)
_UbntWlStatEntry_Object=MibTableRow
ubntWlStatEntry=_UbntWlStatEntry_Object((1,3,6,1,4,1,41112,1,4,5,1))
ubntWlStatEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ubntWlStatEntry.setStatus(_A)
class _UbntWlStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntWlStatIndex_Type.__name__=_D
_UbntWlStatIndex_Object=MibTableColumn
ubntWlStatIndex=_UbntWlStatIndex_Object((1,3,6,1,4,1,41112,1,4,5,1,1),_UbntWlStatIndex_Type())
ubntWlStatIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntWlStatIndex.setStatus(_A)
_UbntWlStatSsid_Type=DisplayString
_UbntWlStatSsid_Object=MibTableColumn
ubntWlStatSsid=_UbntWlStatSsid_Object((1,3,6,1,4,1,41112,1,4,5,1,2),_UbntWlStatSsid_Type())
ubntWlStatSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatSsid.setStatus(_A)
_UbntWlStatHideSsid_Type=TruthValue
_UbntWlStatHideSsid_Object=MibTableColumn
ubntWlStatHideSsid=_UbntWlStatHideSsid_Object((1,3,6,1,4,1,41112,1,4,5,1,3),_UbntWlStatHideSsid_Type())
ubntWlStatHideSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatHideSsid.setStatus(_A)
_UbntWlStatApMac_Type=MacAddress
_UbntWlStatApMac_Object=MibTableColumn
ubntWlStatApMac=_UbntWlStatApMac_Object((1,3,6,1,4,1,41112,1,4,5,1,4),_UbntWlStatApMac_Type())
ubntWlStatApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatApMac.setStatus(_A)
_UbntWlStatSignal_Type=Integer32
_UbntWlStatSignal_Object=MibTableColumn
ubntWlStatSignal=_UbntWlStatSignal_Object((1,3,6,1,4,1,41112,1,4,5,1,5),_UbntWlStatSignal_Type())
ubntWlStatSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatSignal.setStatus(_A)
_UbntWlStatRssi_Type=Integer32
_UbntWlStatRssi_Object=MibTableColumn
ubntWlStatRssi=_UbntWlStatRssi_Object((1,3,6,1,4,1,41112,1,4,5,1,6),_UbntWlStatRssi_Type())
ubntWlStatRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatRssi.setStatus(_A)
_UbntWlStatCcq_Type=Integer32
_UbntWlStatCcq_Object=MibTableColumn
ubntWlStatCcq=_UbntWlStatCcq_Object((1,3,6,1,4,1,41112,1,4,5,1,7),_UbntWlStatCcq_Type())
ubntWlStatCcq.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatCcq.setStatus(_A)
_UbntWlStatNoiseFloor_Type=Integer32
_UbntWlStatNoiseFloor_Object=MibTableColumn
ubntWlStatNoiseFloor=_UbntWlStatNoiseFloor_Object((1,3,6,1,4,1,41112,1,4,5,1,8),_UbntWlStatNoiseFloor_Type())
ubntWlStatNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatNoiseFloor.setStatus(_A)
_UbntWlStatTxRate_Type=Integer32
_UbntWlStatTxRate_Object=MibTableColumn
ubntWlStatTxRate=_UbntWlStatTxRate_Object((1,3,6,1,4,1,41112,1,4,5,1,9),_UbntWlStatTxRate_Type())
ubntWlStatTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatTxRate.setStatus(_A)
_UbntWlStatRxRate_Type=Integer32
_UbntWlStatRxRate_Object=MibTableColumn
ubntWlStatRxRate=_UbntWlStatRxRate_Object((1,3,6,1,4,1,41112,1,4,5,1,10),_UbntWlStatRxRate_Type())
ubntWlStatRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatRxRate.setStatus(_A)
_UbntWlStatSecurity_Type=DisplayString
_UbntWlStatSecurity_Object=MibTableColumn
ubntWlStatSecurity=_UbntWlStatSecurity_Object((1,3,6,1,4,1,41112,1,4,5,1,11),_UbntWlStatSecurity_Type())
ubntWlStatSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatSecurity.setStatus(_A)
_UbntWlStatWdsEnabled_Type=TruthValue
_UbntWlStatWdsEnabled_Object=MibTableColumn
ubntWlStatWdsEnabled=_UbntWlStatWdsEnabled_Object((1,3,6,1,4,1,41112,1,4,5,1,12),_UbntWlStatWdsEnabled_Type())
ubntWlStatWdsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatWdsEnabled.setStatus(_A)
_UbntWlStatApRepeater_Type=TruthValue
_UbntWlStatApRepeater_Object=MibTableColumn
ubntWlStatApRepeater=_UbntWlStatApRepeater_Object((1,3,6,1,4,1,41112,1,4,5,1,13),_UbntWlStatApRepeater_Type())
ubntWlStatApRepeater.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatApRepeater.setStatus(_A)
_UbntWlStatChanWidth_Type=Integer32
_UbntWlStatChanWidth_Object=MibTableColumn
ubntWlStatChanWidth=_UbntWlStatChanWidth_Object((1,3,6,1,4,1,41112,1,4,5,1,14),_UbntWlStatChanWidth_Type())
ubntWlStatChanWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatChanWidth.setStatus(_A)
_UbntWlStatStaCount_Type=Gauge32
_UbntWlStatStaCount_Object=MibTableColumn
ubntWlStatStaCount=_UbntWlStatStaCount_Object((1,3,6,1,4,1,41112,1,4,5,1,15),_UbntWlStatStaCount_Type())
ubntWlStatStaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntWlStatStaCount.setStatus(_A)
_UbntAirMaxTable_Object=MibTable
ubntAirMaxTable=_UbntAirMaxTable_Object((1,3,6,1,4,1,41112,1,4,6))
if mibBuilder.loadTexts:ubntAirMaxTable.setStatus(_A)
_UbntAirMaxEntry_Object=MibTableRow
ubntAirMaxEntry=_UbntAirMaxEntry_Object((1,3,6,1,4,1,41112,1,4,6,1))
ubntAirMaxEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ubntAirMaxEntry.setStatus(_A)
class _UbntAirMaxIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_UbntAirMaxIfIndex_Type.__name__=_D
_UbntAirMaxIfIndex_Object=MibTableColumn
ubntAirMaxIfIndex=_UbntAirMaxIfIndex_Object((1,3,6,1,4,1,41112,1,4,6,1,1),_UbntAirMaxIfIndex_Type())
ubntAirMaxIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntAirMaxIfIndex.setStatus(_A)
_UbntAirMaxEnabled_Type=TruthValue
_UbntAirMaxEnabled_Object=MibTableColumn
ubntAirMaxEnabled=_UbntAirMaxEnabled_Object((1,3,6,1,4,1,41112,1,4,6,1,2),_UbntAirMaxEnabled_Type())
ubntAirMaxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxEnabled.setStatus(_A)
class _UbntAirMaxQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UbntAirMaxQuality_Type.__name__=_D
_UbntAirMaxQuality_Object=MibTableColumn
ubntAirMaxQuality=_UbntAirMaxQuality_Object((1,3,6,1,4,1,41112,1,4,6,1,3),_UbntAirMaxQuality_Type())
ubntAirMaxQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxQuality.setStatus(_A)
class _UbntAirMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UbntAirMaxCapacity_Type.__name__=_D
_UbntAirMaxCapacity_Object=MibTableColumn
ubntAirMaxCapacity=_UbntAirMaxCapacity_Object((1,3,6,1,4,1,41112,1,4,6,1,4),_UbntAirMaxCapacity_Type())
ubntAirMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxCapacity.setStatus(_A)
class _UbntAirMaxPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('high',0),('medium',1),('low',2),('none',3)))
_UbntAirMaxPriority_Type.__name__=_D
_UbntAirMaxPriority_Object=MibTableColumn
ubntAirMaxPriority=_UbntAirMaxPriority_Object((1,3,6,1,4,1,41112,1,4,6,1,5),_UbntAirMaxPriority_Type())
ubntAirMaxPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxPriority.setStatus(_A)
_UbntAirMaxNoAck_Type=TruthValue
_UbntAirMaxNoAck_Object=MibTableColumn
ubntAirMaxNoAck=_UbntAirMaxNoAck_Object((1,3,6,1,4,1,41112,1,4,6,1,6),_UbntAirMaxNoAck_Type())
ubntAirMaxNoAck.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxNoAck.setStatus(_A)
_UbntAirMaxAirtime_Type=Integer32
_UbntAirMaxAirtime_Object=MibTableColumn
ubntAirMaxAirtime=_UbntAirMaxAirtime_Object((1,3,6,1,4,1,41112,1,4,6,1,7),_UbntAirMaxAirtime_Type())
ubntAirMaxAirtime.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxAirtime.setStatus(_A)
_UbntAirMaxGpsSync_Type=TruthValue
_UbntAirMaxGpsSync_Object=MibTableColumn
ubntAirMaxGpsSync=_UbntAirMaxGpsSync_Object((1,3,6,1,4,1,41112,1,4,6,1,8),_UbntAirMaxGpsSync_Type())
ubntAirMaxGpsSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxGpsSync.setStatus(_A)
_UbntAirMaxTdd_Type=TruthValue
_UbntAirMaxTdd_Object=MibTableColumn
ubntAirMaxTdd=_UbntAirMaxTdd_Object((1,3,6,1,4,1,41112,1,4,6,1,9),_UbntAirMaxTdd_Type())
ubntAirMaxTdd.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntAirMaxTdd.setStatus(_A)
_UbntStaTable_Object=MibTable
ubntStaTable=_UbntStaTable_Object((1,3,6,1,4,1,41112,1,4,7))
if mibBuilder.loadTexts:ubntStaTable.setStatus(_A)
_UbntStaEntry_Object=MibTableRow
ubntStaEntry=_UbntStaEntry_Object((1,3,6,1,4,1,41112,1,4,7,1))
ubntStaEntry.setIndexNames((0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:ubntStaEntry.setStatus(_A)
_UbntStaMac_Type=MacAddress
_UbntStaMac_Object=MibTableColumn
ubntStaMac=_UbntStaMac_Object((1,3,6,1,4,1,41112,1,4,7,1,1),_UbntStaMac_Type())
ubntStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:ubntStaMac.setStatus(_A)
_UbntStaName_Type=DisplayString
_UbntStaName_Object=MibTableColumn
ubntStaName=_UbntStaName_Object((1,3,6,1,4,1,41112,1,4,7,1,2),_UbntStaName_Type())
ubntStaName.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaName.setStatus(_A)
_UbntStaSignal_Type=Integer32
_UbntStaSignal_Object=MibTableColumn
ubntStaSignal=_UbntStaSignal_Object((1,3,6,1,4,1,41112,1,4,7,1,3),_UbntStaSignal_Type())
ubntStaSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaSignal.setStatus(_A)
_UbntStaNoiseFloor_Type=Integer32
_UbntStaNoiseFloor_Object=MibTableColumn
ubntStaNoiseFloor=_UbntStaNoiseFloor_Object((1,3,6,1,4,1,41112,1,4,7,1,4),_UbntStaNoiseFloor_Type())
ubntStaNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaNoiseFloor.setStatus(_A)
class _UbntStaDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UbntStaDistance_Type.__name__=_D
_UbntStaDistance_Object=MibTableColumn
ubntStaDistance=_UbntStaDistance_Object((1,3,6,1,4,1,41112,1,4,7,1,5),_UbntStaDistance_Type())
ubntStaDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaDistance.setStatus(_A)
_UbntStaCcq_Type=Integer32
_UbntStaCcq_Object=MibTableColumn
ubntStaCcq=_UbntStaCcq_Object((1,3,6,1,4,1,41112,1,4,7,1,6),_UbntStaCcq_Type())
ubntStaCcq.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaCcq.setStatus(_A)
_UbntStaAmp_Type=Integer32
_UbntStaAmp_Object=MibTableColumn
ubntStaAmp=_UbntStaAmp_Object((1,3,6,1,4,1,41112,1,4,7,1,7),_UbntStaAmp_Type())
ubntStaAmp.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaAmp.setStatus(_A)
_UbntStaAmq_Type=Integer32
_UbntStaAmq_Object=MibTableColumn
ubntStaAmq=_UbntStaAmq_Object((1,3,6,1,4,1,41112,1,4,7,1,8),_UbntStaAmq_Type())
ubntStaAmq.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaAmq.setStatus(_A)
_UbntStaAmc_Type=Integer32
_UbntStaAmc_Object=MibTableColumn
ubntStaAmc=_UbntStaAmc_Object((1,3,6,1,4,1,41112,1,4,7,1,9),_UbntStaAmc_Type())
ubntStaAmc.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaAmc.setStatus(_A)
_UbntStaLastIp_Type=IpAddress
_UbntStaLastIp_Object=MibTableColumn
ubntStaLastIp=_UbntStaLastIp_Object((1,3,6,1,4,1,41112,1,4,7,1,10),_UbntStaLastIp_Type())
ubntStaLastIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaLastIp.setStatus(_A)
_UbntStaTxRate_Type=Integer32
_UbntStaTxRate_Object=MibTableColumn
ubntStaTxRate=_UbntStaTxRate_Object((1,3,6,1,4,1,41112,1,4,7,1,11),_UbntStaTxRate_Type())
ubntStaTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaTxRate.setStatus(_A)
_UbntStaRxRate_Type=Integer32
_UbntStaRxRate_Object=MibTableColumn
ubntStaRxRate=_UbntStaRxRate_Object((1,3,6,1,4,1,41112,1,4,7,1,12),_UbntStaRxRate_Type())
ubntStaRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaRxRate.setStatus(_A)
_UbntStaTxBytes_Type=Counter64
_UbntStaTxBytes_Object=MibTableColumn
ubntStaTxBytes=_UbntStaTxBytes_Object((1,3,6,1,4,1,41112,1,4,7,1,13),_UbntStaTxBytes_Type())
ubntStaTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaTxBytes.setStatus(_A)
_UbntStaRxBytes_Type=Counter64
_UbntStaRxBytes_Object=MibTableColumn
ubntStaRxBytes=_UbntStaRxBytes_Object((1,3,6,1,4,1,41112,1,4,7,1,14),_UbntStaRxBytes_Type())
ubntStaRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaRxBytes.setStatus(_A)
_UbntStaConnTime_Type=TimeTicks
_UbntStaConnTime_Object=MibTableColumn
ubntStaConnTime=_UbntStaConnTime_Object((1,3,6,1,4,1,41112,1,4,7,1,15),_UbntStaConnTime_Type())
ubntStaConnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaConnTime.setStatus(_A)
_UbntStaLocalCINR_Type=Integer32
_UbntStaLocalCINR_Object=MibTableColumn
ubntStaLocalCINR=_UbntStaLocalCINR_Object((1,3,6,1,4,1,41112,1,4,7,1,16),_UbntStaLocalCINR_Type())
ubntStaLocalCINR.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaLocalCINR.setStatus(_A)
_UbntStaTxCapacity_Type=Integer32
_UbntStaTxCapacity_Object=MibTableColumn
ubntStaTxCapacity=_UbntStaTxCapacity_Object((1,3,6,1,4,1,41112,1,4,7,1,17),_UbntStaTxCapacity_Type())
ubntStaTxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaTxCapacity.setStatus(_A)
_UbntStaRxCapacity_Type=Integer32
_UbntStaRxCapacity_Object=MibTableColumn
ubntStaRxCapacity=_UbntStaRxCapacity_Object((1,3,6,1,4,1,41112,1,4,7,1,18),_UbntStaRxCapacity_Type())
ubntStaRxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaRxCapacity.setStatus(_A)
_UbntStaTxAirtime_Type=Integer32
_UbntStaTxAirtime_Object=MibTableColumn
ubntStaTxAirtime=_UbntStaTxAirtime_Object((1,3,6,1,4,1,41112,1,4,7,1,19),_UbntStaTxAirtime_Type())
ubntStaTxAirtime.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaTxAirtime.setStatus(_A)
_UbntStaRxAirtime_Type=Integer32
_UbntStaRxAirtime_Object=MibTableColumn
ubntStaRxAirtime=_UbntStaRxAirtime_Object((1,3,6,1,4,1,41112,1,4,7,1,20),_UbntStaRxAirtime_Type())
ubntStaRxAirtime.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaRxAirtime.setStatus(_A)
_UbntStaTxLatency_Type=Integer32
_UbntStaTxLatency_Object=MibTableColumn
ubntStaTxLatency=_UbntStaTxLatency_Object((1,3,6,1,4,1,41112,1,4,7,1,21),_UbntStaTxLatency_Type())
ubntStaTxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntStaTxLatency.setStatus(_A)
_UbntHostInfo_ObjectIdentity=ObjectIdentity
ubntHostInfo=_UbntHostInfo_ObjectIdentity((1,3,6,1,4,1,41112,1,4,8))
_UbntHostLocaltime_Type=DisplayString
_UbntHostLocaltime_Object=MibScalar
ubntHostLocaltime=_UbntHostLocaltime_Object((1,3,6,1,4,1,41112,1,4,8,1),_UbntHostLocaltime_Type())
ubntHostLocaltime.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntHostLocaltime.setStatus(_A)
class _UbntHostNetrole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('bridge',1),('router',2),('soho',3)))
_UbntHostNetrole_Type.__name__=_D
_UbntHostNetrole_Object=MibScalar
ubntHostNetrole=_UbntHostNetrole_Object((1,3,6,1,4,1,41112,1,4,8,2),_UbntHostNetrole_Type())
ubntHostNetrole.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntHostNetrole.setStatus(_A)
class _UbntHostCpuLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UbntHostCpuLoad_Type.__name__=_D
_UbntHostCpuLoad_Object=MibScalar
ubntHostCpuLoad=_UbntHostCpuLoad_Object((1,3,6,1,4,1,41112,1,4,8,3),_UbntHostCpuLoad_Type())
ubntHostCpuLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntHostCpuLoad.setStatus(_A)
class _UbntHostTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_UbntHostTemperature_Type.__name__=_D
_UbntHostTemperature_Object=MibScalar
ubntHostTemperature=_UbntHostTemperature_Object((1,3,6,1,4,1,41112,1,4,8,4),_UbntHostTemperature_Type())
ubntHostTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntHostTemperature.setStatus(_A)
_UbntGpsInfo_ObjectIdentity=ObjectIdentity
ubntGpsInfo=_UbntGpsInfo_ObjectIdentity((1,3,6,1,4,1,41112,1,4,9))
class _UbntGpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('absent',0),('off',1),('on',2)))
_UbntGpsStatus_Type.__name__=_D
_UbntGpsStatus_Object=MibScalar
ubntGpsStatus=_UbntGpsStatus_Object((1,3,6,1,4,1,41112,1,4,9,1),_UbntGpsStatus_Type())
ubntGpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsStatus.setStatus(_A)
class _UbntGpsFix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('nofix',1),('fix2d',2),('fix3d',3)))
_UbntGpsFix_Type.__name__=_D
_UbntGpsFix_Object=MibScalar
ubntGpsFix=_UbntGpsFix_Object((1,3,6,1,4,1,41112,1,4,9,2),_UbntGpsFix_Type())
ubntGpsFix.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsFix.setStatus(_A)
_UbntGpsLat_Type=DisplayString
_UbntGpsLat_Object=MibScalar
ubntGpsLat=_UbntGpsLat_Object((1,3,6,1,4,1,41112,1,4,9,3),_UbntGpsLat_Type())
ubntGpsLat.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsLat.setStatus(_A)
_UbntGpsLon_Type=DisplayString
_UbntGpsLon_Object=MibScalar
ubntGpsLon=_UbntGpsLon_Object((1,3,6,1,4,1,41112,1,4,9,4),_UbntGpsLon_Type())
ubntGpsLon.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsLon.setStatus(_A)
_UbntGpsAltMeters_Type=DisplayString
_UbntGpsAltMeters_Object=MibScalar
ubntGpsAltMeters=_UbntGpsAltMeters_Object((1,3,6,1,4,1,41112,1,4,9,5),_UbntGpsAltMeters_Type())
ubntGpsAltMeters.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsAltMeters.setStatus(_A)
_UbntGpsAltFeet_Type=DisplayString
_UbntGpsAltFeet_Object=MibScalar
ubntGpsAltFeet=_UbntGpsAltFeet_Object((1,3,6,1,4,1,41112,1,4,9,6),_UbntGpsAltFeet_Type())
ubntGpsAltFeet.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsAltFeet.setStatus(_A)
_UbntGpsSatsVisible_Type=Integer32
_UbntGpsSatsVisible_Object=MibScalar
ubntGpsSatsVisible=_UbntGpsSatsVisible_Object((1,3,6,1,4,1,41112,1,4,9,7),_UbntGpsSatsVisible_Type())
ubntGpsSatsVisible.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsSatsVisible.setStatus(_A)
_UbntGpsSatsTracked_Type=Integer32
_UbntGpsSatsTracked_Object=MibScalar
ubntGpsSatsTracked=_UbntGpsSatsTracked_Object((1,3,6,1,4,1,41112,1,4,9,8),_UbntGpsSatsTracked_Type())
ubntGpsSatsTracked.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsSatsTracked.setStatus(_A)
_UbntGpsHDOP_Type=DisplayString
_UbntGpsHDOP_Object=MibScalar
ubntGpsHDOP=_UbntGpsHDOP_Object((1,3,6,1,4,1,41112,1,4,9,9),_UbntGpsHDOP_Type())
ubntGpsHDOP.setMaxAccess(_C)
if mibBuilder.loadTexts:ubntGpsHDOP.setStatus(_A)
ubntAirMAXStatusGroup=ObjectGroup((1,3,6,1,4,1,41112,1,2,2,1))
ubntAirMAXStatusGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:ubntAirMAXStatusGroup.setStatus(_A)
ubntAirMAXStatusCompliance=ModuleCompliance((1,3,6,1,4,1,41112,1,2,2,2))
ubntAirMAXStatusCompliance.setObjects((_B,_AX))
if mibBuilder.loadTexts:ubntAirMAXStatusCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_AX:ubntAirMAXStatusGroup,'ubntAirMAXStatusCompliance':ubntAirMAXStatusCompliance,'ubntAirMAX':ubntAirMAX,'ubntRadioTable':ubntRadioTable,'ubntRadioEntry':ubntRadioEntry,_F:ubntRadioIndex,_h:ubntRadioMode,_i:ubntRadioCCode,_j:ubntRadioFreq,_k:ubntRadioDfsEnabled,_l:ubntRadioTxPower,_m:ubntRadioDistance,_n:ubntRadioChainmask,_o:ubntRadioAntenna,'ubntRadioRssiTable':ubntRadioRssiTable,'ubntRadioRssiEntry':ubntRadioRssiEntry,_H:ubntRadioRssiIndex,_p:ubntRadioRssi,_q:ubntRadioRssiMgmt,_r:ubntRadioRssiExt,'ubntAirSyncTable':ubntAirSyncTable,'ubntAirSyncEntry':ubntAirSyncEntry,_I:ubntAirSyncIfIndex,_A0:ubntAirSyncMode,_A1:ubntAirSyncCount,_A2:ubntAirSyncDownUtil,_A3:ubntAirSyncUpUtil,'ubntAirSelTable':ubntAirSelTable,'ubntAirSelEntry':ubntAirSelEntry,_J:ubntAirSelIfIndex,_A4:ubntAirSelEnabled,_A5:ubntAirSelInterval,'ubntWlStatTable':ubntWlStatTable,'ubntWlStatEntry':ubntWlStatEntry,_G:ubntWlStatIndex,_A6:ubntWlStatSsid,_A7:ubntWlStatHideSsid,_A8:ubntWlStatApMac,_A9:ubntWlStatSignal,_AA:ubntWlStatRssi,_AB:ubntWlStatCcq,_AC:ubntWlStatNoiseFloor,_AD:ubntWlStatTxRate,_AE:ubntWlStatRxRate,_AF:ubntWlStatSecurity,_AG:ubntWlStatWdsEnabled,_AH:ubntWlStatApRepeater,_AI:ubntWlStatChanWidth,_AJ:ubntWlStatStaCount,'ubntAirMaxTable':ubntAirMaxTable,'ubntAirMaxEntry':ubntAirMaxEntry,_K:ubntAirMaxIfIndex,_s:ubntAirMaxEnabled,_t:ubntAirMaxQuality,_u:ubntAirMaxCapacity,_v:ubntAirMaxPriority,_w:ubntAirMaxNoAck,_x:ubntAirMaxAirtime,_y:ubntAirMaxGpsSync,_z:ubntAirMaxTdd,'ubntStaTable':ubntStaTable,'ubntStaEntry':ubntStaEntry,_L:ubntStaMac,_N:ubntStaName,_O:ubntStaSignal,_P:ubntStaNoiseFloor,_Q:ubntStaDistance,_R:ubntStaCcq,_S:ubntStaAmp,_T:ubntStaAmq,_U:ubntStaAmc,_V:ubntStaLastIp,_W:ubntStaTxRate,_X:ubntStaRxRate,_Y:ubntStaTxBytes,_Z:ubntStaRxBytes,_a:ubntStaConnTime,_b:ubntStaLocalCINR,_c:ubntStaTxCapacity,_d:ubntStaRxCapacity,_e:ubntStaTxAirtime,_f:ubntStaRxAirtime,_g:ubntStaTxLatency,'ubntHostInfo':ubntHostInfo,_AK:ubntHostLocaltime,_AL:ubntHostNetrole,_AM:ubntHostCpuLoad,_AN:ubntHostTemperature,'ubntGpsInfo':ubntGpsInfo,_AO:ubntGpsStatus,_AP:ubntGpsFix,_AQ:ubntGpsLat,_AR:ubntGpsLon,_AS:ubntGpsAltMeters,_AT:ubntGpsAltFeet,_AU:ubntGpsSatsVisible,_AV:ubntGpsSatsTracked,_AW:ubntGpsHDOP})