_A7='aosCoreFacilityStatsObjectGroup'
_A6='aosCoreFacHist1DaySnrSuspectReason'
_A5='aosCoreFacHist1DaySnrValueHigh'
_A4='aosCoreFacHist1DaySnrValueMean'
_A3='aosCoreFacHist1DaySnrValueLow'
_A2='aosCoreFacHist1DaySnrSampleTime'
_A1='aosCoreFacHist15MinSnrSuspectReason'
_A0='aosCoreFacHist15MinSnrValueHigh'
_z='aosCoreFacHist15MinSnrValueMean'
_y='aosCoreFacHist15MinSnrValueLow'
_x='aosCoreFacHist15MinSnrSampleTime'
_w='aosCoreFacCurrSnrSuspectReason'
_v='aosCoreFacCurrSnrValue'
_u='aosCoreFacHist1DayFecSuspectReason'
_t='aosCoreFacHist1DayFecBitErrorRate'
_s='aosCoreFacHist1DayFecUncorrectedBlocks'
_r='aosCoreFacHist1DayFecCorrectedErrors'
_q='aosCoreFacHist1DayFecSampleTime'
_p='aosCoreFacHist15MinFecSuspectReason'
_o='aosCoreFacHist15MinFecBitErrorRate'
_n='aosCoreFacHist15MinFecUncorrectedBlocks'
_m='aosCoreFacHist15MinFecCorrectedErrors'
_l='aosCoreFacHist15MinFecSampleTime'
_k='aosCoreFacCurrFecSuspectReason'
_j='aosCoreFacCurrFecBitErrorRate'
_i='aosCoreFacCurrFecUncorrectedBlocks'
_h='aosCoreFacCurrFecCorrectedErrors'
_g='aosCoreFacHist1DayOpticalPowerSuspectReason'
_f='aosCoreFacHist1DayOpticalPowerTxHi'
_e='aosCoreFacHist1DayOpticalPowerTxMed'
_d='aosCoreFacHist1DayOpticalPowerTxLow'
_c='aosCoreFacHist1DayOpticalPowerRxHi'
_b='aosCoreFacHist1DayOpticalPowerRxMed'
_a='aosCoreFacHist1DayOpticalPowerRxLow'
_Z='aosCoreFacHist1DayOpticalPowerSampleTime'
_Y='aosCoreFacHist15MinOpticalPowerSuspectReason'
_X='aosCoreFacHist15MinOpticalPowerTxHi'
_W='aosCoreFacHist15MinOpticalPowerTxMed'
_V='aosCoreFacHist15MinOpticalPowerTxLow'
_U='aosCoreFacHist15MinOpticalPowerRxHi'
_T='aosCoreFacHist15MinOpticalPowerRxMed'
_S='aosCoreFacHist15MinOpticalPowerRxLow'
_R='aosCoreFacHist15MinOpticalPowerSampleTime'
_Q='aosCoreFacCurrOpticalPowerSuspectReason'
_P='aosCoreFacCurrOpticalPowerTx'
_O='aosCoreFacCurrOpticalPowerRx'
_N='aosCoreFacHist1DaySnrSample'
_M='aosCoreFacHist15MinSnrSample'
_L='aosCoreFacHist1DayFecSample'
_K='aosCoreFacHist15MinFecSample'
_J='aosCoreFacHist1DayOpticalPowerSample'
_I='aosCoreFacHist15MinOpticalPowerSample'
_H='10 dB'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='0.1 dbm'
_C='read-only'
_B='AOS-CORE-FACILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aosCommon,=mibBuilder.importSymbols('ADVA-MIB','aosCommon')
PmSuspectReasonType,=mibBuilder.importSymbols('AOS-COMMON-PM-MIB','PmSuspectReasonType')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aosCoreFacilityMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,20,1,3))
if mibBuilder.loadTexts:aosCoreFacilityMIB.setRevisions(('2016-06-05 00:00',))
_AosCoreFacilityObjects_ObjectIdentity=ObjectIdentity
aosCoreFacilityObjects=_AosCoreFacilityObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,3,1))
_AosCoreFacilityStatsObjects_ObjectIdentity=ObjectIdentity
aosCoreFacilityStatsObjects=_AosCoreFacilityStatsObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,3,2))
_AosCoreFacCurrOpticalPowerTable_Object=MibTable
aosCoreFacCurrOpticalPowerTable=_AosCoreFacCurrOpticalPowerTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,1))
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerTable.setStatus(_A)
_AosCoreFacCurrOpticalPowerEntry_Object=MibTableRow
aosCoreFacCurrOpticalPowerEntry=_AosCoreFacCurrOpticalPowerEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,1,1))
aosCoreFacCurrOpticalPowerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerEntry.setStatus(_A)
_AosCoreFacCurrOpticalPowerRx_Type=Integer32
_AosCoreFacCurrOpticalPowerRx_Object=MibTableColumn
aosCoreFacCurrOpticalPowerRx=_AosCoreFacCurrOpticalPowerRx_Object((1,3,6,1,4,1,2544,1,20,1,3,2,1,1,1),_AosCoreFacCurrOpticalPowerRx_Type())
aosCoreFacCurrOpticalPowerRx.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerRx.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerRx.setUnits(_D)
_AosCoreFacCurrOpticalPowerTx_Type=Integer32
_AosCoreFacCurrOpticalPowerTx_Object=MibTableColumn
aosCoreFacCurrOpticalPowerTx=_AosCoreFacCurrOpticalPowerTx_Object((1,3,6,1,4,1,2544,1,20,1,3,2,1,1,2),_AosCoreFacCurrOpticalPowerTx_Type())
aosCoreFacCurrOpticalPowerTx.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerTx.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerTx.setUnits(_D)
_AosCoreFacCurrOpticalPowerSuspectReason_Type=PmSuspectReasonType
_AosCoreFacCurrOpticalPowerSuspectReason_Object=MibTableColumn
aosCoreFacCurrOpticalPowerSuspectReason=_AosCoreFacCurrOpticalPowerSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,1,1,3),_AosCoreFacCurrOpticalPowerSuspectReason_Type())
aosCoreFacCurrOpticalPowerSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrOpticalPowerSuspectReason.setStatus(_A)
_AosCoreFacHist15MinOpticalPowerTable_Object=MibTable
aosCoreFacHist15MinOpticalPowerTable=_AosCoreFacHist15MinOpticalPowerTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2))
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTable.setStatus(_A)
_AosCoreFacHist15MinOpticalPowerEntry_Object=MibTableRow
aosCoreFacHist15MinOpticalPowerEntry=_AosCoreFacHist15MinOpticalPowerEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1))
aosCoreFacHist15MinOpticalPowerEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerEntry.setStatus(_A)
class _AosCoreFacHist15MinOpticalPowerSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AosCoreFacHist15MinOpticalPowerSample_Type.__name__=_G
_AosCoreFacHist15MinOpticalPowerSample_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerSample=_AosCoreFacHist15MinOpticalPowerSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,1),_AosCoreFacHist15MinOpticalPowerSample_Type())
aosCoreFacHist15MinOpticalPowerSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerSample.setStatus(_A)
_AosCoreFacHist15MinOpticalPowerSampleTime_Type=TimeTicks
_AosCoreFacHist15MinOpticalPowerSampleTime_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerSampleTime=_AosCoreFacHist15MinOpticalPowerSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,2),_AosCoreFacHist15MinOpticalPowerSampleTime_Type())
aosCoreFacHist15MinOpticalPowerSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerSampleTime.setStatus(_A)
_AosCoreFacHist15MinOpticalPowerRxLow_Type=Integer32
_AosCoreFacHist15MinOpticalPowerRxLow_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerRxLow=_AosCoreFacHist15MinOpticalPowerRxLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,3),_AosCoreFacHist15MinOpticalPowerRxLow_Type())
aosCoreFacHist15MinOpticalPowerRxLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxLow.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerRxMed_Type=Integer32
_AosCoreFacHist15MinOpticalPowerRxMed_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerRxMed=_AosCoreFacHist15MinOpticalPowerRxMed_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,4),_AosCoreFacHist15MinOpticalPowerRxMed_Type())
aosCoreFacHist15MinOpticalPowerRxMed.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxMed.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxMed.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerRxHi_Type=Integer32
_AosCoreFacHist15MinOpticalPowerRxHi_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerRxHi=_AosCoreFacHist15MinOpticalPowerRxHi_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,5),_AosCoreFacHist15MinOpticalPowerRxHi_Type())
aosCoreFacHist15MinOpticalPowerRxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxHi.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerRxHi.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerTxLow_Type=Integer32
_AosCoreFacHist15MinOpticalPowerTxLow_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerTxLow=_AosCoreFacHist15MinOpticalPowerTxLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,6),_AosCoreFacHist15MinOpticalPowerTxLow_Type())
aosCoreFacHist15MinOpticalPowerTxLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxLow.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerTxMed_Type=Integer32
_AosCoreFacHist15MinOpticalPowerTxMed_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerTxMed=_AosCoreFacHist15MinOpticalPowerTxMed_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,7),_AosCoreFacHist15MinOpticalPowerTxMed_Type())
aosCoreFacHist15MinOpticalPowerTxMed.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxMed.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxMed.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerTxHi_Type=Integer32
_AosCoreFacHist15MinOpticalPowerTxHi_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerTxHi=_AosCoreFacHist15MinOpticalPowerTxHi_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,8),_AosCoreFacHist15MinOpticalPowerTxHi_Type())
aosCoreFacHist15MinOpticalPowerTxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxHi.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerTxHi.setUnits(_D)
_AosCoreFacHist15MinOpticalPowerSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist15MinOpticalPowerSuspectReason_Object=MibTableColumn
aosCoreFacHist15MinOpticalPowerSuspectReason=_AosCoreFacHist15MinOpticalPowerSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,2,1,9),_AosCoreFacHist15MinOpticalPowerSuspectReason_Type())
aosCoreFacHist15MinOpticalPowerSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinOpticalPowerSuspectReason.setStatus(_A)
_AosCoreFacHist1DayOpticalPowerTable_Object=MibTable
aosCoreFacHist1DayOpticalPowerTable=_AosCoreFacHist1DayOpticalPowerTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3))
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTable.setStatus(_A)
_AosCoreFacHist1DayOpticalPowerEntry_Object=MibTableRow
aosCoreFacHist1DayOpticalPowerEntry=_AosCoreFacHist1DayOpticalPowerEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1))
aosCoreFacHist1DayOpticalPowerEntry.setIndexNames((0,_E,_F),(0,_B,_J))
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerEntry.setStatus(_A)
class _AosCoreFacHist1DayOpticalPowerSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AosCoreFacHist1DayOpticalPowerSample_Type.__name__=_G
_AosCoreFacHist1DayOpticalPowerSample_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerSample=_AosCoreFacHist1DayOpticalPowerSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,1),_AosCoreFacHist1DayOpticalPowerSample_Type())
aosCoreFacHist1DayOpticalPowerSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerSample.setStatus(_A)
_AosCoreFacHist1DayOpticalPowerSampleTime_Type=TimeTicks
_AosCoreFacHist1DayOpticalPowerSampleTime_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerSampleTime=_AosCoreFacHist1DayOpticalPowerSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,2),_AosCoreFacHist1DayOpticalPowerSampleTime_Type())
aosCoreFacHist1DayOpticalPowerSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerSampleTime.setStatus(_A)
_AosCoreFacHist1DayOpticalPowerRxLow_Type=Integer32
_AosCoreFacHist1DayOpticalPowerRxLow_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerRxLow=_AosCoreFacHist1DayOpticalPowerRxLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,3),_AosCoreFacHist1DayOpticalPowerRxLow_Type())
aosCoreFacHist1DayOpticalPowerRxLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxLow.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerRxMed_Type=Integer32
_AosCoreFacHist1DayOpticalPowerRxMed_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerRxMed=_AosCoreFacHist1DayOpticalPowerRxMed_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,4),_AosCoreFacHist1DayOpticalPowerRxMed_Type())
aosCoreFacHist1DayOpticalPowerRxMed.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxMed.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxMed.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerRxHi_Type=Integer32
_AosCoreFacHist1DayOpticalPowerRxHi_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerRxHi=_AosCoreFacHist1DayOpticalPowerRxHi_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,5),_AosCoreFacHist1DayOpticalPowerRxHi_Type())
aosCoreFacHist1DayOpticalPowerRxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxHi.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerRxHi.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerTxLow_Type=Integer32
_AosCoreFacHist1DayOpticalPowerTxLow_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerTxLow=_AosCoreFacHist1DayOpticalPowerTxLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,6),_AosCoreFacHist1DayOpticalPowerTxLow_Type())
aosCoreFacHist1DayOpticalPowerTxLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxLow.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerTxMed_Type=Integer32
_AosCoreFacHist1DayOpticalPowerTxMed_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerTxMed=_AosCoreFacHist1DayOpticalPowerTxMed_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,7),_AosCoreFacHist1DayOpticalPowerTxMed_Type())
aosCoreFacHist1DayOpticalPowerTxMed.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxMed.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxMed.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerTxHi_Type=Integer32
_AosCoreFacHist1DayOpticalPowerTxHi_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerTxHi=_AosCoreFacHist1DayOpticalPowerTxHi_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,8),_AosCoreFacHist1DayOpticalPowerTxHi_Type())
aosCoreFacHist1DayOpticalPowerTxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxHi.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerTxHi.setUnits(_D)
_AosCoreFacHist1DayOpticalPowerSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist1DayOpticalPowerSuspectReason_Object=MibTableColumn
aosCoreFacHist1DayOpticalPowerSuspectReason=_AosCoreFacHist1DayOpticalPowerSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,3,1,9),_AosCoreFacHist1DayOpticalPowerSuspectReason_Type())
aosCoreFacHist1DayOpticalPowerSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayOpticalPowerSuspectReason.setStatus(_A)
_AosCoreFacCurrFecTable_Object=MibTable
aosCoreFacCurrFecTable=_AosCoreFacCurrFecTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4))
if mibBuilder.loadTexts:aosCoreFacCurrFecTable.setStatus(_A)
_AosCoreFacCurrFecEntry_Object=MibTableRow
aosCoreFacCurrFecEntry=_AosCoreFacCurrFecEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4,1))
aosCoreFacCurrFecEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aosCoreFacCurrFecEntry.setStatus(_A)
_AosCoreFacCurrFecCorrectedErrors_Type=Counter64
_AosCoreFacCurrFecCorrectedErrors_Object=MibTableColumn
aosCoreFacCurrFecCorrectedErrors=_AosCoreFacCurrFecCorrectedErrors_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4,1,1),_AosCoreFacCurrFecCorrectedErrors_Type())
aosCoreFacCurrFecCorrectedErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrFecCorrectedErrors.setStatus(_A)
_AosCoreFacCurrFecUncorrectedBlocks_Type=Counter64
_AosCoreFacCurrFecUncorrectedBlocks_Object=MibTableColumn
aosCoreFacCurrFecUncorrectedBlocks=_AosCoreFacCurrFecUncorrectedBlocks_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4,1,2),_AosCoreFacCurrFecUncorrectedBlocks_Type())
aosCoreFacCurrFecUncorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrFecUncorrectedBlocks.setStatus(_A)
_AosCoreFacCurrFecBitErrorRate_Type=Counter64
_AosCoreFacCurrFecBitErrorRate_Object=MibTableColumn
aosCoreFacCurrFecBitErrorRate=_AosCoreFacCurrFecBitErrorRate_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4,1,3),_AosCoreFacCurrFecBitErrorRate_Type())
aosCoreFacCurrFecBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrFecBitErrorRate.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacCurrFecBitErrorRate.setUnits('1e-18')
_AosCoreFacCurrFecSuspectReason_Type=PmSuspectReasonType
_AosCoreFacCurrFecSuspectReason_Object=MibTableColumn
aosCoreFacCurrFecSuspectReason=_AosCoreFacCurrFecSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,4,1,4),_AosCoreFacCurrFecSuspectReason_Type())
aosCoreFacCurrFecSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrFecSuspectReason.setStatus(_A)
_AosCoreFacHist15MinFecTable_Object=MibTable
aosCoreFacHist15MinFecTable=_AosCoreFacHist15MinFecTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5))
if mibBuilder.loadTexts:aosCoreFacHist15MinFecTable.setStatus(_A)
_AosCoreFacHist15MinFecEntry_Object=MibTableRow
aosCoreFacHist15MinFecEntry=_AosCoreFacHist15MinFecEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1))
aosCoreFacHist15MinFecEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:aosCoreFacHist15MinFecEntry.setStatus(_A)
class _AosCoreFacHist15MinFecSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AosCoreFacHist15MinFecSample_Type.__name__=_G
_AosCoreFacHist15MinFecSample_Object=MibTableColumn
aosCoreFacHist15MinFecSample=_AosCoreFacHist15MinFecSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,1),_AosCoreFacHist15MinFecSample_Type())
aosCoreFacHist15MinFecSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecSample.setStatus(_A)
_AosCoreFacHist15MinFecSampleTime_Type=TimeTicks
_AosCoreFacHist15MinFecSampleTime_Object=MibTableColumn
aosCoreFacHist15MinFecSampleTime=_AosCoreFacHist15MinFecSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,2),_AosCoreFacHist15MinFecSampleTime_Type())
aosCoreFacHist15MinFecSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecSampleTime.setStatus(_A)
_AosCoreFacHist15MinFecCorrectedErrors_Type=Counter64
_AosCoreFacHist15MinFecCorrectedErrors_Object=MibTableColumn
aosCoreFacHist15MinFecCorrectedErrors=_AosCoreFacHist15MinFecCorrectedErrors_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,3),_AosCoreFacHist15MinFecCorrectedErrors_Type())
aosCoreFacHist15MinFecCorrectedErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecCorrectedErrors.setStatus(_A)
_AosCoreFacHist15MinFecUncorrectedBlocks_Type=Counter64
_AosCoreFacHist15MinFecUncorrectedBlocks_Object=MibTableColumn
aosCoreFacHist15MinFecUncorrectedBlocks=_AosCoreFacHist15MinFecUncorrectedBlocks_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,4),_AosCoreFacHist15MinFecUncorrectedBlocks_Type())
aosCoreFacHist15MinFecUncorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecUncorrectedBlocks.setStatus(_A)
_AosCoreFacHist15MinFecBitErrorRate_Type=Counter64
_AosCoreFacHist15MinFecBitErrorRate_Object=MibTableColumn
aosCoreFacHist15MinFecBitErrorRate=_AosCoreFacHist15MinFecBitErrorRate_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,5),_AosCoreFacHist15MinFecBitErrorRate_Type())
aosCoreFacHist15MinFecBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecBitErrorRate.setStatus(_A)
_AosCoreFacHist15MinFecSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist15MinFecSuspectReason_Object=MibTableColumn
aosCoreFacHist15MinFecSuspectReason=_AosCoreFacHist15MinFecSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,5,1,6),_AosCoreFacHist15MinFecSuspectReason_Type())
aosCoreFacHist15MinFecSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinFecSuspectReason.setStatus(_A)
_AosCoreFacHist1DayFecTable_Object=MibTable
aosCoreFacHist1DayFecTable=_AosCoreFacHist1DayFecTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6))
if mibBuilder.loadTexts:aosCoreFacHist1DayFecTable.setStatus(_A)
_AosCoreFacHist1DayFecEntry_Object=MibTableRow
aosCoreFacHist1DayFecEntry=_AosCoreFacHist1DayFecEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1))
aosCoreFacHist1DayFecEntry.setIndexNames((0,_E,_F),(0,_B,_L))
if mibBuilder.loadTexts:aosCoreFacHist1DayFecEntry.setStatus(_A)
class _AosCoreFacHist1DayFecSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AosCoreFacHist1DayFecSample_Type.__name__=_G
_AosCoreFacHist1DayFecSample_Object=MibTableColumn
aosCoreFacHist1DayFecSample=_AosCoreFacHist1DayFecSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,1),_AosCoreFacHist1DayFecSample_Type())
aosCoreFacHist1DayFecSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecSample.setStatus(_A)
_AosCoreFacHist1DayFecSampleTime_Type=TimeTicks
_AosCoreFacHist1DayFecSampleTime_Object=MibTableColumn
aosCoreFacHist1DayFecSampleTime=_AosCoreFacHist1DayFecSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,2),_AosCoreFacHist1DayFecSampleTime_Type())
aosCoreFacHist1DayFecSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecSampleTime.setStatus(_A)
_AosCoreFacHist1DayFecCorrectedErrors_Type=Counter64
_AosCoreFacHist1DayFecCorrectedErrors_Object=MibTableColumn
aosCoreFacHist1DayFecCorrectedErrors=_AosCoreFacHist1DayFecCorrectedErrors_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,3),_AosCoreFacHist1DayFecCorrectedErrors_Type())
aosCoreFacHist1DayFecCorrectedErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecCorrectedErrors.setStatus(_A)
_AosCoreFacHist1DayFecUncorrectedBlocks_Type=Counter64
_AosCoreFacHist1DayFecUncorrectedBlocks_Object=MibTableColumn
aosCoreFacHist1DayFecUncorrectedBlocks=_AosCoreFacHist1DayFecUncorrectedBlocks_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,4),_AosCoreFacHist1DayFecUncorrectedBlocks_Type())
aosCoreFacHist1DayFecUncorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecUncorrectedBlocks.setStatus(_A)
_AosCoreFacHist1DayFecBitErrorRate_Type=Counter64
_AosCoreFacHist1DayFecBitErrorRate_Object=MibTableColumn
aosCoreFacHist1DayFecBitErrorRate=_AosCoreFacHist1DayFecBitErrorRate_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,5),_AosCoreFacHist1DayFecBitErrorRate_Type())
aosCoreFacHist1DayFecBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecBitErrorRate.setStatus(_A)
_AosCoreFacHist1DayFecSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist1DayFecSuspectReason_Object=MibTableColumn
aosCoreFacHist1DayFecSuspectReason=_AosCoreFacHist1DayFecSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,6,1,6),_AosCoreFacHist1DayFecSuspectReason_Type())
aosCoreFacHist1DayFecSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DayFecSuspectReason.setStatus(_A)
_AosCoreFacCurrSnrTable_Object=MibTable
aosCoreFacCurrSnrTable=_AosCoreFacCurrSnrTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,7))
if mibBuilder.loadTexts:aosCoreFacCurrSnrTable.setStatus(_A)
_AosCoreFacCurrSnrEntry_Object=MibTableRow
aosCoreFacCurrSnrEntry=_AosCoreFacCurrSnrEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,7,1))
aosCoreFacCurrSnrEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aosCoreFacCurrSnrEntry.setStatus(_A)
_AosCoreFacCurrSnrValue_Type=Counter64
_AosCoreFacCurrSnrValue_Object=MibTableColumn
aosCoreFacCurrSnrValue=_AosCoreFacCurrSnrValue_Object((1,3,6,1,4,1,2544,1,20,1,3,2,7,1,1),_AosCoreFacCurrSnrValue_Type())
aosCoreFacCurrSnrValue.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrSnrValue.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacCurrSnrValue.setUnits(_H)
_AosCoreFacCurrSnrSuspectReason_Type=PmSuspectReasonType
_AosCoreFacCurrSnrSuspectReason_Object=MibTableColumn
aosCoreFacCurrSnrSuspectReason=_AosCoreFacCurrSnrSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,7,1,2),_AosCoreFacCurrSnrSuspectReason_Type())
aosCoreFacCurrSnrSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacCurrSnrSuspectReason.setStatus(_A)
_AosCoreFacHist15MinSnrTable_Object=MibTable
aosCoreFacHist15MinSnrTable=_AosCoreFacHist15MinSnrTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8))
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrTable.setStatus(_A)
_AosCoreFacHist15MinSnrEntry_Object=MibTableRow
aosCoreFacHist15MinSnrEntry=_AosCoreFacHist15MinSnrEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1))
aosCoreFacHist15MinSnrEntry.setIndexNames((0,_E,_F),(0,_B,_M))
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrEntry.setStatus(_A)
class _AosCoreFacHist15MinSnrSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AosCoreFacHist15MinSnrSample_Type.__name__=_G
_AosCoreFacHist15MinSnrSample_Object=MibTableColumn
aosCoreFacHist15MinSnrSample=_AosCoreFacHist15MinSnrSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,1),_AosCoreFacHist15MinSnrSample_Type())
aosCoreFacHist15MinSnrSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrSample.setStatus(_A)
_AosCoreFacHist15MinSnrSampleTime_Type=TimeTicks
_AosCoreFacHist15MinSnrSampleTime_Object=MibTableColumn
aosCoreFacHist15MinSnrSampleTime=_AosCoreFacHist15MinSnrSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,2),_AosCoreFacHist15MinSnrSampleTime_Type())
aosCoreFacHist15MinSnrSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrSampleTime.setStatus(_A)
_AosCoreFacHist15MinSnrValueLow_Type=Counter64
_AosCoreFacHist15MinSnrValueLow_Object=MibTableColumn
aosCoreFacHist15MinSnrValueLow=_AosCoreFacHist15MinSnrValueLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,3),_AosCoreFacHist15MinSnrValueLow_Type())
aosCoreFacHist15MinSnrValueLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueLow.setUnits(_H)
_AosCoreFacHist15MinSnrValueMean_Type=Counter64
_AosCoreFacHist15MinSnrValueMean_Object=MibTableColumn
aosCoreFacHist15MinSnrValueMean=_AosCoreFacHist15MinSnrValueMean_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,4),_AosCoreFacHist15MinSnrValueMean_Type())
aosCoreFacHist15MinSnrValueMean.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueMean.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueMean.setUnits(_H)
_AosCoreFacHist15MinSnrValueHigh_Type=Counter64
_AosCoreFacHist15MinSnrValueHigh_Object=MibTableColumn
aosCoreFacHist15MinSnrValueHigh=_AosCoreFacHist15MinSnrValueHigh_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,5),_AosCoreFacHist15MinSnrValueHigh_Type())
aosCoreFacHist15MinSnrValueHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueHigh.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrValueHigh.setUnits(_H)
_AosCoreFacHist15MinSnrSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist15MinSnrSuspectReason_Object=MibTableColumn
aosCoreFacHist15MinSnrSuspectReason=_AosCoreFacHist15MinSnrSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,8,1,6),_AosCoreFacHist15MinSnrSuspectReason_Type())
aosCoreFacHist15MinSnrSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist15MinSnrSuspectReason.setStatus(_A)
_AosCoreFacHist1DaySnrTable_Object=MibTable
aosCoreFacHist1DaySnrTable=_AosCoreFacHist1DaySnrTable_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9))
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrTable.setStatus(_A)
_AosCoreFacHist1DaySnrEntry_Object=MibTableRow
aosCoreFacHist1DaySnrEntry=_AosCoreFacHist1DaySnrEntry_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1))
aosCoreFacHist1DaySnrEntry.setIndexNames((0,_E,_F),(0,_B,_N))
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrEntry.setStatus(_A)
class _AosCoreFacHist1DaySnrSample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AosCoreFacHist1DaySnrSample_Type.__name__=_G
_AosCoreFacHist1DaySnrSample_Object=MibTableColumn
aosCoreFacHist1DaySnrSample=_AosCoreFacHist1DaySnrSample_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,1),_AosCoreFacHist1DaySnrSample_Type())
aosCoreFacHist1DaySnrSample.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrSample.setStatus(_A)
_AosCoreFacHist1DaySnrSampleTime_Type=TimeTicks
_AosCoreFacHist1DaySnrSampleTime_Object=MibTableColumn
aosCoreFacHist1DaySnrSampleTime=_AosCoreFacHist1DaySnrSampleTime_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,2),_AosCoreFacHist1DaySnrSampleTime_Type())
aosCoreFacHist1DaySnrSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrSampleTime.setStatus(_A)
_AosCoreFacHist1DaySnrValueLow_Type=Counter64
_AosCoreFacHist1DaySnrValueLow_Object=MibTableColumn
aosCoreFacHist1DaySnrValueLow=_AosCoreFacHist1DaySnrValueLow_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,3),_AosCoreFacHist1DaySnrValueLow_Type())
aosCoreFacHist1DaySnrValueLow.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueLow.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueLow.setUnits(_H)
_AosCoreFacHist1DaySnrValueMean_Type=Counter64
_AosCoreFacHist1DaySnrValueMean_Object=MibTableColumn
aosCoreFacHist1DaySnrValueMean=_AosCoreFacHist1DaySnrValueMean_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,4),_AosCoreFacHist1DaySnrValueMean_Type())
aosCoreFacHist1DaySnrValueMean.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueMean.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueMean.setUnits(_H)
_AosCoreFacHist1DaySnrValueHigh_Type=Counter64
_AosCoreFacHist1DaySnrValueHigh_Object=MibTableColumn
aosCoreFacHist1DaySnrValueHigh=_AosCoreFacHist1DaySnrValueHigh_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,5),_AosCoreFacHist1DaySnrValueHigh_Type())
aosCoreFacHist1DaySnrValueHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueHigh.setStatus(_A)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrValueHigh.setUnits(_H)
_AosCoreFacHist1DaySnrSuspectReason_Type=PmSuspectReasonType
_AosCoreFacHist1DaySnrSuspectReason_Object=MibTableColumn
aosCoreFacHist1DaySnrSuspectReason=_AosCoreFacHist1DaySnrSuspectReason_Object((1,3,6,1,4,1,2544,1,20,1,3,2,9,1,6),_AosCoreFacHist1DaySnrSuspectReason_Type())
aosCoreFacHist1DaySnrSuspectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreFacHist1DaySnrSuspectReason.setStatus(_A)
_AosCoreFacilityConformance_ObjectIdentity=ObjectIdentity
aosCoreFacilityConformance=_AosCoreFacilityConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,3,3))
_AosCoreFacilityCompliances_ObjectIdentity=ObjectIdentity
aosCoreFacilityCompliances=_AosCoreFacilityCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,3,3,1))
_AosCoreFacilityGroups_ObjectIdentity=ObjectIdentity
aosCoreFacilityGroups=_AosCoreFacilityGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,3,3,2))
aosCoreFacilityStatsObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,20,1,3,3,2,1))
aosCoreFacilityStatsObjectGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_J),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_K),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_L),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_M),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_N),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:aosCoreFacilityStatsObjectGroup.setStatus(_A)
aosCoreFacilityCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,20,1,3,3,1,1))
aosCoreFacilityCompliance.setObjects((_B,_A7))
if mibBuilder.loadTexts:aosCoreFacilityCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aosCoreFacilityMIB':aosCoreFacilityMIB,'aosCoreFacilityObjects':aosCoreFacilityObjects,'aosCoreFacilityStatsObjects':aosCoreFacilityStatsObjects,'aosCoreFacCurrOpticalPowerTable':aosCoreFacCurrOpticalPowerTable,'aosCoreFacCurrOpticalPowerEntry':aosCoreFacCurrOpticalPowerEntry,_O:aosCoreFacCurrOpticalPowerRx,_P:aosCoreFacCurrOpticalPowerTx,_Q:aosCoreFacCurrOpticalPowerSuspectReason,'aosCoreFacHist15MinOpticalPowerTable':aosCoreFacHist15MinOpticalPowerTable,'aosCoreFacHist15MinOpticalPowerEntry':aosCoreFacHist15MinOpticalPowerEntry,_I:aosCoreFacHist15MinOpticalPowerSample,_R:aosCoreFacHist15MinOpticalPowerSampleTime,_S:aosCoreFacHist15MinOpticalPowerRxLow,_T:aosCoreFacHist15MinOpticalPowerRxMed,_U:aosCoreFacHist15MinOpticalPowerRxHi,_V:aosCoreFacHist15MinOpticalPowerTxLow,_W:aosCoreFacHist15MinOpticalPowerTxMed,_X:aosCoreFacHist15MinOpticalPowerTxHi,_Y:aosCoreFacHist15MinOpticalPowerSuspectReason,'aosCoreFacHist1DayOpticalPowerTable':aosCoreFacHist1DayOpticalPowerTable,'aosCoreFacHist1DayOpticalPowerEntry':aosCoreFacHist1DayOpticalPowerEntry,_J:aosCoreFacHist1DayOpticalPowerSample,_Z:aosCoreFacHist1DayOpticalPowerSampleTime,_a:aosCoreFacHist1DayOpticalPowerRxLow,_b:aosCoreFacHist1DayOpticalPowerRxMed,_c:aosCoreFacHist1DayOpticalPowerRxHi,_d:aosCoreFacHist1DayOpticalPowerTxLow,_e:aosCoreFacHist1DayOpticalPowerTxMed,_f:aosCoreFacHist1DayOpticalPowerTxHi,_g:aosCoreFacHist1DayOpticalPowerSuspectReason,'aosCoreFacCurrFecTable':aosCoreFacCurrFecTable,'aosCoreFacCurrFecEntry':aosCoreFacCurrFecEntry,_h:aosCoreFacCurrFecCorrectedErrors,_i:aosCoreFacCurrFecUncorrectedBlocks,_j:aosCoreFacCurrFecBitErrorRate,_k:aosCoreFacCurrFecSuspectReason,'aosCoreFacHist15MinFecTable':aosCoreFacHist15MinFecTable,'aosCoreFacHist15MinFecEntry':aosCoreFacHist15MinFecEntry,_K:aosCoreFacHist15MinFecSample,_l:aosCoreFacHist15MinFecSampleTime,_m:aosCoreFacHist15MinFecCorrectedErrors,_n:aosCoreFacHist15MinFecUncorrectedBlocks,_o:aosCoreFacHist15MinFecBitErrorRate,_p:aosCoreFacHist15MinFecSuspectReason,'aosCoreFacHist1DayFecTable':aosCoreFacHist1DayFecTable,'aosCoreFacHist1DayFecEntry':aosCoreFacHist1DayFecEntry,_L:aosCoreFacHist1DayFecSample,_q:aosCoreFacHist1DayFecSampleTime,_r:aosCoreFacHist1DayFecCorrectedErrors,_s:aosCoreFacHist1DayFecUncorrectedBlocks,_t:aosCoreFacHist1DayFecBitErrorRate,_u:aosCoreFacHist1DayFecSuspectReason,'aosCoreFacCurrSnrTable':aosCoreFacCurrSnrTable,'aosCoreFacCurrSnrEntry':aosCoreFacCurrSnrEntry,_v:aosCoreFacCurrSnrValue,_w:aosCoreFacCurrSnrSuspectReason,'aosCoreFacHist15MinSnrTable':aosCoreFacHist15MinSnrTable,'aosCoreFacHist15MinSnrEntry':aosCoreFacHist15MinSnrEntry,_M:aosCoreFacHist15MinSnrSample,_x:aosCoreFacHist15MinSnrSampleTime,_y:aosCoreFacHist15MinSnrValueLow,_z:aosCoreFacHist15MinSnrValueMean,_A0:aosCoreFacHist15MinSnrValueHigh,_A1:aosCoreFacHist15MinSnrSuspectReason,'aosCoreFacHist1DaySnrTable':aosCoreFacHist1DaySnrTable,'aosCoreFacHist1DaySnrEntry':aosCoreFacHist1DaySnrEntry,_N:aosCoreFacHist1DaySnrSample,_A2:aosCoreFacHist1DaySnrSampleTime,_A3:aosCoreFacHist1DaySnrValueLow,_A4:aosCoreFacHist1DaySnrValueMean,_A5:aosCoreFacHist1DaySnrValueHigh,_A6:aosCoreFacHist1DaySnrSuspectReason,'aosCoreFacilityConformance':aosCoreFacilityConformance,'aosCoreFacilityCompliances':aosCoreFacilityCompliances,'aosCoreFacilityCompliance':aosCoreFacilityCompliance,'aosCoreFacilityGroups':aosCoreFacilityGroups,_A7:aosCoreFacilityStatsObjectGroup})