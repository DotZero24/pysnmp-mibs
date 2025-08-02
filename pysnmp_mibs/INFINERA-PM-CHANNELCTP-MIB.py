_s='channelCtpPmRealGroup'
_r='channelCtpPmGroup'
_q='channelCtpPmRealPrbsErr'
_p='channelCtpPmRealPrbsSyncErr'
_o='channelCtpPmRealOchDtsSES'
_n='channelCtpPmRealOchDtsES'
_m='channelCtpPmRealOchDtsCV'
_l='channelCtpPmRealFecTotalCodeWords'
_k='channelCtpPmRealFecUncorrectedRows'
_j='channelCtpPmRealFecCorrectedBits'
_i='channelCtpPmRealBerPostFec'
_h='channelCtpPmRealBerPreFec'
_g='channelCtpPmRealQFactor'
_f='channelCtpPmRealChanOchWavelength'
_e='channelCtpPmRealChanOchLBC'
_d='channelCtpPmRealChanOchOpt'
_c='channelCtpPmRealChanOchOpr'
_b='channelCtpPmChanOchQValueAve'
_a='channelCtpPmChanOchQValueMax'
_Z='channelCtpPmChanOchQValueMin'
_Y='channelCtpPmOchDtsSES'
_X='channelCtpPmOchDtsES'
_W='channelCtpPmOchDtsCV'
_V='channelCtpPmFecTotalCodeWords'
_U='channelCtpPmFecUncorrectedRows'
_T='channelCtpPmFecCorrectedBits'
_S='channelCtpPmChanOchLBCAve'
_R='channelCtpPmChanOchLBCMax'
_Q='channelCtpPmChanOchLBCMin'
_P='channelCtpPmChanOchOptAve'
_O='channelCtpPmChanOchOptMax'
_N='channelCtpPmChanOchOptMin'
_M='channelCtpPmChanOchOprAve'
_L='channelCtpPmChanOchOprMax'
_K='channelCtpPmChanOchOprMin'
_J='channelCtpPmValidity'
_I='not-accessible'
_H='channelCtpPmTimestamp'
_G='channelCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-CHANNELCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,FloatHundredths=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
channelCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,3))
if mibBuilder.loadTexts:channelCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_ChannelCtpPmRealTable_Object=MibTable
channelCtpPmRealTable=_ChannelCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1))
if mibBuilder.loadTexts:channelCtpPmRealTable.setStatus(_A)
_ChannelCtpPmRealEntry_Object=MibTableRow
channelCtpPmRealEntry=_ChannelCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1))
channelCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:channelCtpPmRealEntry.setStatus(_A)
_ChannelCtpPmRealChanOchOpr_Type=FloatHundredths
_ChannelCtpPmRealChanOchOpr_Object=MibTableColumn
channelCtpPmRealChanOchOpr=_ChannelCtpPmRealChanOchOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,1),_ChannelCtpPmRealChanOchOpr_Type())
channelCtpPmRealChanOchOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealChanOchOpr.setStatus(_A)
_ChannelCtpPmRealChanOchOpt_Type=FloatHundredths
_ChannelCtpPmRealChanOchOpt_Object=MibTableColumn
channelCtpPmRealChanOchOpt=_ChannelCtpPmRealChanOchOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,2),_ChannelCtpPmRealChanOchOpt_Type())
channelCtpPmRealChanOchOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealChanOchOpt.setStatus(_A)
_ChannelCtpPmRealChanOchLBC_Type=FloatHundredths
_ChannelCtpPmRealChanOchLBC_Object=MibTableColumn
channelCtpPmRealChanOchLBC=_ChannelCtpPmRealChanOchLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,3),_ChannelCtpPmRealChanOchLBC_Type())
channelCtpPmRealChanOchLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealChanOchLBC.setStatus(_A)
_ChannelCtpPmRealChanOchWavelength_Type=FloatHundredths
_ChannelCtpPmRealChanOchWavelength_Object=MibTableColumn
channelCtpPmRealChanOchWavelength=_ChannelCtpPmRealChanOchWavelength_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,4),_ChannelCtpPmRealChanOchWavelength_Type())
channelCtpPmRealChanOchWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealChanOchWavelength.setStatus(_A)
_ChannelCtpPmRealQFactor_Type=FloatHundredths
_ChannelCtpPmRealQFactor_Object=MibTableColumn
channelCtpPmRealQFactor=_ChannelCtpPmRealQFactor_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,5),_ChannelCtpPmRealQFactor_Type())
channelCtpPmRealQFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealQFactor.setStatus(_A)
_ChannelCtpPmRealBerPreFec_Type=FloatArbitraryPrecision
_ChannelCtpPmRealBerPreFec_Object=MibTableColumn
channelCtpPmRealBerPreFec=_ChannelCtpPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,6),_ChannelCtpPmRealBerPreFec_Type())
channelCtpPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealBerPreFec.setStatus(_A)
_ChannelCtpPmRealBerPostFec_Type=FloatArbitraryPrecision
_ChannelCtpPmRealBerPostFec_Object=MibTableColumn
channelCtpPmRealBerPostFec=_ChannelCtpPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,7),_ChannelCtpPmRealBerPostFec_Type())
channelCtpPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealBerPostFec.setStatus(_A)
_ChannelCtpPmRealFecCorrectedBits_Type=Counter64
_ChannelCtpPmRealFecCorrectedBits_Object=MibTableColumn
channelCtpPmRealFecCorrectedBits=_ChannelCtpPmRealFecCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,8),_ChannelCtpPmRealFecCorrectedBits_Type())
channelCtpPmRealFecCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealFecCorrectedBits.setStatus(_A)
_ChannelCtpPmRealFecUncorrectedRows_Type=Counter64
_ChannelCtpPmRealFecUncorrectedRows_Object=MibTableColumn
channelCtpPmRealFecUncorrectedRows=_ChannelCtpPmRealFecUncorrectedRows_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,9),_ChannelCtpPmRealFecUncorrectedRows_Type())
channelCtpPmRealFecUncorrectedRows.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealFecUncorrectedRows.setStatus(_A)
_ChannelCtpPmRealFecTotalCodeWords_Type=Counter64
_ChannelCtpPmRealFecTotalCodeWords_Object=MibTableColumn
channelCtpPmRealFecTotalCodeWords=_ChannelCtpPmRealFecTotalCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,10),_ChannelCtpPmRealFecTotalCodeWords_Type())
channelCtpPmRealFecTotalCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealFecTotalCodeWords.setStatus(_A)
_ChannelCtpPmRealOchDtsCV_Type=Counter64
_ChannelCtpPmRealOchDtsCV_Object=MibTableColumn
channelCtpPmRealOchDtsCV=_ChannelCtpPmRealOchDtsCV_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,11),_ChannelCtpPmRealOchDtsCV_Type())
channelCtpPmRealOchDtsCV.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealOchDtsCV.setStatus(_A)
_ChannelCtpPmRealOchDtsES_Type=Integer32
_ChannelCtpPmRealOchDtsES_Object=MibTableColumn
channelCtpPmRealOchDtsES=_ChannelCtpPmRealOchDtsES_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,12),_ChannelCtpPmRealOchDtsES_Type())
channelCtpPmRealOchDtsES.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealOchDtsES.setStatus(_A)
_ChannelCtpPmRealOchDtsSES_Type=Integer32
_ChannelCtpPmRealOchDtsSES_Object=MibTableColumn
channelCtpPmRealOchDtsSES=_ChannelCtpPmRealOchDtsSES_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,13),_ChannelCtpPmRealOchDtsSES_Type())
channelCtpPmRealOchDtsSES.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealOchDtsSES.setStatus(_A)
_ChannelCtpPmRealPrbsSyncErr_Type=Integer32
_ChannelCtpPmRealPrbsSyncErr_Object=MibTableColumn
channelCtpPmRealPrbsSyncErr=_ChannelCtpPmRealPrbsSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,14),_ChannelCtpPmRealPrbsSyncErr_Type())
channelCtpPmRealPrbsSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealPrbsSyncErr.setStatus(_A)
_ChannelCtpPmRealPrbsErr_Type=Integer32
_ChannelCtpPmRealPrbsErr_Object=MibTableColumn
channelCtpPmRealPrbsErr=_ChannelCtpPmRealPrbsErr_Object((1,3,6,1,4,1,21296,2,2,2,3,3,1,1,15),_ChannelCtpPmRealPrbsErr_Type())
channelCtpPmRealPrbsErr.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmRealPrbsErr.setStatus(_A)
_ChannelCtpPmTable_Object=MibTable
channelCtpPmTable=_ChannelCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2))
if mibBuilder.loadTexts:channelCtpPmTable.setStatus(_A)
_ChannelCtpPmEntry_Object=MibTableRow
channelCtpPmEntry=_ChannelCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1))
channelCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:channelCtpPmEntry.setStatus(_A)
class _ChannelCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ChannelCtpPmTimestamp_Type.__name__=_F
_ChannelCtpPmTimestamp_Object=MibTableColumn
channelCtpPmTimestamp=_ChannelCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,1),_ChannelCtpPmTimestamp_Type())
channelCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:channelCtpPmTimestamp.setStatus(_A)
class _ChannelCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_ChannelCtpPmSampleDuration_Type.__name__=_F
_ChannelCtpPmSampleDuration_Object=MibTableColumn
channelCtpPmSampleDuration=_ChannelCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,2),_ChannelCtpPmSampleDuration_Type())
channelCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:channelCtpPmSampleDuration.setStatus(_A)
_ChannelCtpPmValidity_Type=TruthValue
_ChannelCtpPmValidity_Object=MibTableColumn
channelCtpPmValidity=_ChannelCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,3),_ChannelCtpPmValidity_Type())
channelCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmValidity.setStatus(_A)
_ChannelCtpPmChanOchOprMin_Type=FloatHundredths
_ChannelCtpPmChanOchOprMin_Object=MibTableColumn
channelCtpPmChanOchOprMin=_ChannelCtpPmChanOchOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,4),_ChannelCtpPmChanOchOprMin_Type())
channelCtpPmChanOchOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOprMin.setStatus(_A)
_ChannelCtpPmChanOchOprMax_Type=FloatHundredths
_ChannelCtpPmChanOchOprMax_Object=MibTableColumn
channelCtpPmChanOchOprMax=_ChannelCtpPmChanOchOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,5),_ChannelCtpPmChanOchOprMax_Type())
channelCtpPmChanOchOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOprMax.setStatus(_A)
_ChannelCtpPmChanOchOprAve_Type=FloatHundredths
_ChannelCtpPmChanOchOprAve_Object=MibTableColumn
channelCtpPmChanOchOprAve=_ChannelCtpPmChanOchOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,6),_ChannelCtpPmChanOchOprAve_Type())
channelCtpPmChanOchOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOprAve.setStatus(_A)
_ChannelCtpPmChanOchOptMin_Type=FloatHundredths
_ChannelCtpPmChanOchOptMin_Object=MibTableColumn
channelCtpPmChanOchOptMin=_ChannelCtpPmChanOchOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,7),_ChannelCtpPmChanOchOptMin_Type())
channelCtpPmChanOchOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOptMin.setStatus(_A)
_ChannelCtpPmChanOchOptMax_Type=FloatHundredths
_ChannelCtpPmChanOchOptMax_Object=MibTableColumn
channelCtpPmChanOchOptMax=_ChannelCtpPmChanOchOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,8),_ChannelCtpPmChanOchOptMax_Type())
channelCtpPmChanOchOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOptMax.setStatus(_A)
_ChannelCtpPmChanOchOptAve_Type=FloatHundredths
_ChannelCtpPmChanOchOptAve_Object=MibTableColumn
channelCtpPmChanOchOptAve=_ChannelCtpPmChanOchOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,9),_ChannelCtpPmChanOchOptAve_Type())
channelCtpPmChanOchOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchOptAve.setStatus(_A)
_ChannelCtpPmChanOchLBCMin_Type=FloatHundredths
_ChannelCtpPmChanOchLBCMin_Object=MibTableColumn
channelCtpPmChanOchLBCMin=_ChannelCtpPmChanOchLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,10),_ChannelCtpPmChanOchLBCMin_Type())
channelCtpPmChanOchLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchLBCMin.setStatus(_A)
_ChannelCtpPmChanOchLBCMax_Type=FloatHundredths
_ChannelCtpPmChanOchLBCMax_Object=MibTableColumn
channelCtpPmChanOchLBCMax=_ChannelCtpPmChanOchLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,11),_ChannelCtpPmChanOchLBCMax_Type())
channelCtpPmChanOchLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchLBCMax.setStatus(_A)
_ChannelCtpPmChanOchLBCAve_Type=FloatHundredths
_ChannelCtpPmChanOchLBCAve_Object=MibTableColumn
channelCtpPmChanOchLBCAve=_ChannelCtpPmChanOchLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,12),_ChannelCtpPmChanOchLBCAve_Type())
channelCtpPmChanOchLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchLBCAve.setStatus(_A)
_ChannelCtpPmFecCorrectedBits_Type=HCPerfIntervalCount
_ChannelCtpPmFecCorrectedBits_Object=MibTableColumn
channelCtpPmFecCorrectedBits=_ChannelCtpPmFecCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,13),_ChannelCtpPmFecCorrectedBits_Type())
channelCtpPmFecCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmFecCorrectedBits.setStatus(_A)
_ChannelCtpPmFecUncorrectedRows_Type=HCPerfIntervalCount
_ChannelCtpPmFecUncorrectedRows_Object=MibTableColumn
channelCtpPmFecUncorrectedRows=_ChannelCtpPmFecUncorrectedRows_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,14),_ChannelCtpPmFecUncorrectedRows_Type())
channelCtpPmFecUncorrectedRows.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmFecUncorrectedRows.setStatus(_A)
_ChannelCtpPmFecTotalCodeWords_Type=HCPerfIntervalCount
_ChannelCtpPmFecTotalCodeWords_Object=MibTableColumn
channelCtpPmFecTotalCodeWords=_ChannelCtpPmFecTotalCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,15),_ChannelCtpPmFecTotalCodeWords_Type())
channelCtpPmFecTotalCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmFecTotalCodeWords.setStatus(_A)
_ChannelCtpPmOchDtsCV_Type=HCPerfIntervalCount
_ChannelCtpPmOchDtsCV_Object=MibTableColumn
channelCtpPmOchDtsCV=_ChannelCtpPmOchDtsCV_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,16),_ChannelCtpPmOchDtsCV_Type())
channelCtpPmOchDtsCV.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmOchDtsCV.setStatus(_A)
_ChannelCtpPmOchDtsES_Type=Integer32
_ChannelCtpPmOchDtsES_Object=MibTableColumn
channelCtpPmOchDtsES=_ChannelCtpPmOchDtsES_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,17),_ChannelCtpPmOchDtsES_Type())
channelCtpPmOchDtsES.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmOchDtsES.setStatus(_A)
_ChannelCtpPmOchDtsSES_Type=Integer32
_ChannelCtpPmOchDtsSES_Object=MibTableColumn
channelCtpPmOchDtsSES=_ChannelCtpPmOchDtsSES_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,18),_ChannelCtpPmOchDtsSES_Type())
channelCtpPmOchDtsSES.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmOchDtsSES.setStatus(_A)
_ChannelCtpPmChanOchQValueMin_Type=FloatHundredths
_ChannelCtpPmChanOchQValueMin_Object=MibTableColumn
channelCtpPmChanOchQValueMin=_ChannelCtpPmChanOchQValueMin_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,19),_ChannelCtpPmChanOchQValueMin_Type())
channelCtpPmChanOchQValueMin.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchQValueMin.setStatus(_A)
_ChannelCtpPmChanOchQValueMax_Type=FloatHundredths
_ChannelCtpPmChanOchQValueMax_Object=MibTableColumn
channelCtpPmChanOchQValueMax=_ChannelCtpPmChanOchQValueMax_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,20),_ChannelCtpPmChanOchQValueMax_Type())
channelCtpPmChanOchQValueMax.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchQValueMax.setStatus(_A)
_ChannelCtpPmChanOchQValueAve_Type=FloatHundredths
_ChannelCtpPmChanOchQValueAve_Object=MibTableColumn
channelCtpPmChanOchQValueAve=_ChannelCtpPmChanOchQValueAve_Object((1,3,6,1,4,1,21296,2,2,2,3,3,2,1,21),_ChannelCtpPmChanOchQValueAve_Type())
channelCtpPmChanOchQValueAve.setMaxAccess(_C)
if mibBuilder.loadTexts:channelCtpPmChanOchQValueAve.setStatus(_A)
_ChannelCtpPmConformance_ObjectIdentity=ObjectIdentity
channelCtpPmConformance=_ChannelCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,3,3))
_ChannelCtpPmCompliances_ObjectIdentity=ObjectIdentity
channelCtpPmCompliances=_ChannelCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,3,3,1))
_ChannelCtpPmGroups_ObjectIdentity=ObjectIdentity
channelCtpPmGroups=_ChannelCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,3,3,2))
channelCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,3,3,2,1))
channelCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:channelCtpPmGroup.setStatus(_A)
channelCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,3,3,2,2))
channelCtpPmRealGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:channelCtpPmRealGroup.setStatus(_A)
channelCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,3,3,1,1))
channelCtpPmCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:channelCtpPmCompliance.setStatus(_A)
channelCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,3,3,1,2))
channelCtpPmRealCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:channelCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'channelCtpPmMIB':channelCtpPmMIB,'channelCtpPmRealTable':channelCtpPmRealTable,'channelCtpPmRealEntry':channelCtpPmRealEntry,_c:channelCtpPmRealChanOchOpr,_d:channelCtpPmRealChanOchOpt,_e:channelCtpPmRealChanOchLBC,_f:channelCtpPmRealChanOchWavelength,_g:channelCtpPmRealQFactor,_h:channelCtpPmRealBerPreFec,_i:channelCtpPmRealBerPostFec,_j:channelCtpPmRealFecCorrectedBits,_k:channelCtpPmRealFecUncorrectedRows,_l:channelCtpPmRealFecTotalCodeWords,_m:channelCtpPmRealOchDtsCV,_n:channelCtpPmRealOchDtsES,_o:channelCtpPmRealOchDtsSES,_p:channelCtpPmRealPrbsSyncErr,_q:channelCtpPmRealPrbsErr,'channelCtpPmTable':channelCtpPmTable,'channelCtpPmEntry':channelCtpPmEntry,_H:channelCtpPmTimestamp,_G:channelCtpPmSampleDuration,_J:channelCtpPmValidity,_K:channelCtpPmChanOchOprMin,_L:channelCtpPmChanOchOprMax,_M:channelCtpPmChanOchOprAve,_N:channelCtpPmChanOchOptMin,_O:channelCtpPmChanOchOptMax,_P:channelCtpPmChanOchOptAve,_Q:channelCtpPmChanOchLBCMin,_R:channelCtpPmChanOchLBCMax,_S:channelCtpPmChanOchLBCAve,_T:channelCtpPmFecCorrectedBits,_U:channelCtpPmFecUncorrectedRows,_V:channelCtpPmFecTotalCodeWords,_W:channelCtpPmOchDtsCV,_X:channelCtpPmOchDtsES,_Y:channelCtpPmOchDtsSES,_Z:channelCtpPmChanOchQValueMin,_a:channelCtpPmChanOchQValueMax,_b:channelCtpPmChanOchQValueAve,'channelCtpPmConformance':channelCtpPmConformance,'channelCtpPmCompliances':channelCtpPmCompliances,'channelCtpPmCompliance':channelCtpPmCompliance,'channelCtpPmRealCompliance':channelCtpPmRealCompliance,'channelCtpPmGroups':channelCtpPmGroups,_r:channelCtpPmGroup,_s:channelCtpPmRealGroup})