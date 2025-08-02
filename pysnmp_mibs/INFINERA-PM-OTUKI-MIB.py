_r='otuKiPmRealGroup'
_q='otuKiPmGroup'
_p='otuKiPmRealRxBEICount'
_o='otuKiPmRealCorrectedBits'
_n='otuKiPmRealRxDefectSecondsFEND'
_m='otuKiPmRealBerPostFec'
_l='otuKiPmRealBerPreFec'
_k='otuKiPmRealQValue'
_j='otuKiPmRealRxDefectSeconds'
_i='otuKiPmRealRxErroredBlocks'
_h='otuKiPmRealNumberOfCorrectedOnes'
_g='otuKiPmRealNumberOfCorrectedZeros'
_f='otuKiPmRealNumberOfUncorrectedWords'
_e='otuKiPmRealNumberOfCodeWords'
_d='otuKiPmRxBEICount'
_c='otuKiPmCorrectedBits'
_b='otuKiPmRxDefectSecondsFEND'
_a='otuKiPmBerPostFecAve'
_Z='otuKiPmBerPostFecMax'
_Y='otuKiPmBerPostFecMin'
_X='otuKiPmBerPreFecAve'
_W='otuKiPmBerPreFecMax'
_V='otuKiPmBerPreFecMin'
_U='otuKiPmQValueAve'
_T='otuKiPmQValueMax'
_S='otuKiPmQValueMin'
_R='otuKiPmPayloadType'
_Q='otuKiPmCircuitId'
_P='otuKiPmRxDefectSeconds'
_O='otuKiPmRxErroredBlocks'
_N='otuKiPmNumberOfCorrectedOnes'
_M='otuKiPmNumberOfCorrectedZeros'
_L='otuKiPmNumberOfUncorrectedWords'
_K='otuKiPmNumberOfCodeWords'
_J='otuKiPmValidity'
_I='not-accessible'
_H='Integer32'
_G='otuKiPmTimestamp'
_F='otuKiPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OTUKI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,FloatHundredths,InfnSampleDuration,InfnServiceType,InfnValidityBitmap=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','InfnSampleDuration','InfnServiceType','InfnValidityBitmap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
otuKiPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,27))
if mibBuilder.loadTexts:otuKiPmMIB.setRevisions(('2011-07-20 00:00',))
_OtuKiPmRealTable_Object=MibTable
otuKiPmRealTable=_OtuKiPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1))
if mibBuilder.loadTexts:otuKiPmRealTable.setStatus(_A)
_OtuKiPmRealEntry_Object=MibTableRow
otuKiPmRealEntry=_OtuKiPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1))
otuKiPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otuKiPmRealEntry.setStatus(_A)
_OtuKiPmRealNumberOfCodeWords_Type=HCPerfIntervalCount
_OtuKiPmRealNumberOfCodeWords_Object=MibTableColumn
otuKiPmRealNumberOfCodeWords=_OtuKiPmRealNumberOfCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,1),_OtuKiPmRealNumberOfCodeWords_Type())
otuKiPmRealNumberOfCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealNumberOfCodeWords.setStatus(_A)
_OtuKiPmRealNumberOfUncorrectedWords_Type=HCPerfIntervalCount
_OtuKiPmRealNumberOfUncorrectedWords_Object=MibTableColumn
otuKiPmRealNumberOfUncorrectedWords=_OtuKiPmRealNumberOfUncorrectedWords_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,2),_OtuKiPmRealNumberOfUncorrectedWords_Type())
otuKiPmRealNumberOfUncorrectedWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealNumberOfUncorrectedWords.setStatus(_A)
_OtuKiPmRealNumberOfCorrectedZeros_Type=HCPerfIntervalCount
_OtuKiPmRealNumberOfCorrectedZeros_Object=MibTableColumn
otuKiPmRealNumberOfCorrectedZeros=_OtuKiPmRealNumberOfCorrectedZeros_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,3),_OtuKiPmRealNumberOfCorrectedZeros_Type())
otuKiPmRealNumberOfCorrectedZeros.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealNumberOfCorrectedZeros.setStatus(_A)
_OtuKiPmRealNumberOfCorrectedOnes_Type=HCPerfIntervalCount
_OtuKiPmRealNumberOfCorrectedOnes_Object=MibTableColumn
otuKiPmRealNumberOfCorrectedOnes=_OtuKiPmRealNumberOfCorrectedOnes_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,4),_OtuKiPmRealNumberOfCorrectedOnes_Type())
otuKiPmRealNumberOfCorrectedOnes.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealNumberOfCorrectedOnes.setStatus(_A)
_OtuKiPmRealRxErroredBlocks_Type=HCPerfIntervalCount
_OtuKiPmRealRxErroredBlocks_Object=MibTableColumn
otuKiPmRealRxErroredBlocks=_OtuKiPmRealRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,5),_OtuKiPmRealRxErroredBlocks_Type())
otuKiPmRealRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealRxErroredBlocks.setStatus(_A)
_OtuKiPmRealRxDefectSeconds_Type=Integer32
_OtuKiPmRealRxDefectSeconds_Object=MibTableColumn
otuKiPmRealRxDefectSeconds=_OtuKiPmRealRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,6),_OtuKiPmRealRxDefectSeconds_Type())
otuKiPmRealRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealRxDefectSeconds.setStatus(_A)
_OtuKiPmRealQValue_Type=FloatHundredths
_OtuKiPmRealQValue_Object=MibTableColumn
otuKiPmRealQValue=_OtuKiPmRealQValue_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,7),_OtuKiPmRealQValue_Type())
otuKiPmRealQValue.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealQValue.setStatus(_A)
_OtuKiPmRealBerPreFec_Type=FloatArbitraryPrecision
_OtuKiPmRealBerPreFec_Object=MibTableColumn
otuKiPmRealBerPreFec=_OtuKiPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,8),_OtuKiPmRealBerPreFec_Type())
otuKiPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealBerPreFec.setStatus(_A)
_OtuKiPmRealBerPostFec_Type=FloatArbitraryPrecision
_OtuKiPmRealBerPostFec_Object=MibTableColumn
otuKiPmRealBerPostFec=_OtuKiPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,9),_OtuKiPmRealBerPostFec_Type())
otuKiPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealBerPostFec.setStatus(_A)
_OtuKiPmRealRxDefectSecondsFEND_Type=Integer32
_OtuKiPmRealRxDefectSecondsFEND_Object=MibTableColumn
otuKiPmRealRxDefectSecondsFEND=_OtuKiPmRealRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,10),_OtuKiPmRealRxDefectSecondsFEND_Type())
otuKiPmRealRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealRxDefectSecondsFEND.setStatus(_A)
_OtuKiPmRealCorrectedBits_Type=HCPerfIntervalCount
_OtuKiPmRealCorrectedBits_Object=MibTableColumn
otuKiPmRealCorrectedBits=_OtuKiPmRealCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,11),_OtuKiPmRealCorrectedBits_Type())
otuKiPmRealCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealCorrectedBits.setStatus(_A)
_OtuKiPmRealRxBEICount_Type=HCPerfIntervalCount
_OtuKiPmRealRxBEICount_Object=MibTableColumn
otuKiPmRealRxBEICount=_OtuKiPmRealRxBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,27,1,1,12),_OtuKiPmRealRxBEICount_Type())
otuKiPmRealRxBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRealRxBEICount.setStatus(_A)
_OtuKiPmTable_Object=MibTable
otuKiPmTable=_OtuKiPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2))
if mibBuilder.loadTexts:otuKiPmTable.setStatus(_A)
_OtuKiPmEntry_Object=MibTableRow
otuKiPmEntry=_OtuKiPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1))
otuKiPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:otuKiPmEntry.setStatus(_A)
class _OtuKiPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OtuKiPmTimestamp_Type.__name__=_H
_OtuKiPmTimestamp_Object=MibTableColumn
otuKiPmTimestamp=_OtuKiPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,1),_OtuKiPmTimestamp_Type())
otuKiPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:otuKiPmTimestamp.setStatus(_A)
_OtuKiPmSampleDuration_Type=InfnSampleDuration
_OtuKiPmSampleDuration_Object=MibTableColumn
otuKiPmSampleDuration=_OtuKiPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,2),_OtuKiPmSampleDuration_Type())
otuKiPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:otuKiPmSampleDuration.setStatus(_A)
_OtuKiPmValidity_Type=InfnValidityBitmap
_OtuKiPmValidity_Object=MibTableColumn
otuKiPmValidity=_OtuKiPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,3),_OtuKiPmValidity_Type())
otuKiPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmValidity.setStatus(_A)
_OtuKiPmNumberOfCodeWords_Type=HCPerfIntervalCount
_OtuKiPmNumberOfCodeWords_Object=MibTableColumn
otuKiPmNumberOfCodeWords=_OtuKiPmNumberOfCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,4),_OtuKiPmNumberOfCodeWords_Type())
otuKiPmNumberOfCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmNumberOfCodeWords.setStatus(_A)
_OtuKiPmNumberOfUncorrectedWords_Type=HCPerfIntervalCount
_OtuKiPmNumberOfUncorrectedWords_Object=MibTableColumn
otuKiPmNumberOfUncorrectedWords=_OtuKiPmNumberOfUncorrectedWords_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,5),_OtuKiPmNumberOfUncorrectedWords_Type())
otuKiPmNumberOfUncorrectedWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmNumberOfUncorrectedWords.setStatus(_A)
_OtuKiPmNumberOfCorrectedZeros_Type=HCPerfIntervalCount
_OtuKiPmNumberOfCorrectedZeros_Object=MibTableColumn
otuKiPmNumberOfCorrectedZeros=_OtuKiPmNumberOfCorrectedZeros_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,6),_OtuKiPmNumberOfCorrectedZeros_Type())
otuKiPmNumberOfCorrectedZeros.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmNumberOfCorrectedZeros.setStatus(_A)
_OtuKiPmNumberOfCorrectedOnes_Type=HCPerfIntervalCount
_OtuKiPmNumberOfCorrectedOnes_Object=MibTableColumn
otuKiPmNumberOfCorrectedOnes=_OtuKiPmNumberOfCorrectedOnes_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,7),_OtuKiPmNumberOfCorrectedOnes_Type())
otuKiPmNumberOfCorrectedOnes.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmNumberOfCorrectedOnes.setStatus(_A)
_OtuKiPmRxErroredBlocks_Type=HCPerfIntervalCount
_OtuKiPmRxErroredBlocks_Object=MibTableColumn
otuKiPmRxErroredBlocks=_OtuKiPmRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,8),_OtuKiPmRxErroredBlocks_Type())
otuKiPmRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRxErroredBlocks.setStatus(_A)
_OtuKiPmRxDefectSeconds_Type=Integer32
_OtuKiPmRxDefectSeconds_Object=MibTableColumn
otuKiPmRxDefectSeconds=_OtuKiPmRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,9),_OtuKiPmRxDefectSeconds_Type())
otuKiPmRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRxDefectSeconds.setStatus(_A)
_OtuKiPmCircuitId_Type=DisplayString
_OtuKiPmCircuitId_Object=MibTableColumn
otuKiPmCircuitId=_OtuKiPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,10),_OtuKiPmCircuitId_Type())
otuKiPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmCircuitId.setStatus(_A)
_OtuKiPmPayloadType_Type=InfnServiceType
_OtuKiPmPayloadType_Object=MibTableColumn
otuKiPmPayloadType=_OtuKiPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,11),_OtuKiPmPayloadType_Type())
otuKiPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmPayloadType.setStatus(_A)
_OtuKiPmQValueMin_Type=FloatHundredths
_OtuKiPmQValueMin_Object=MibTableColumn
otuKiPmQValueMin=_OtuKiPmQValueMin_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,12),_OtuKiPmQValueMin_Type())
otuKiPmQValueMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmQValueMin.setStatus(_A)
_OtuKiPmQValueMax_Type=FloatHundredths
_OtuKiPmQValueMax_Object=MibTableColumn
otuKiPmQValueMax=_OtuKiPmQValueMax_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,13),_OtuKiPmQValueMax_Type())
otuKiPmQValueMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmQValueMax.setStatus(_A)
_OtuKiPmQValueAve_Type=FloatHundredths
_OtuKiPmQValueAve_Object=MibTableColumn
otuKiPmQValueAve=_OtuKiPmQValueAve_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,14),_OtuKiPmQValueAve_Type())
otuKiPmQValueAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmQValueAve.setStatus(_A)
_OtuKiPmBerPreFecMin_Type=FloatArbitraryPrecision
_OtuKiPmBerPreFecMin_Object=MibTableColumn
otuKiPmBerPreFecMin=_OtuKiPmBerPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,15),_OtuKiPmBerPreFecMin_Type())
otuKiPmBerPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPreFecMin.setStatus(_A)
_OtuKiPmBerPreFecMax_Type=FloatArbitraryPrecision
_OtuKiPmBerPreFecMax_Object=MibTableColumn
otuKiPmBerPreFecMax=_OtuKiPmBerPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,16),_OtuKiPmBerPreFecMax_Type())
otuKiPmBerPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPreFecMax.setStatus(_A)
_OtuKiPmBerPreFecAve_Type=FloatArbitraryPrecision
_OtuKiPmBerPreFecAve_Object=MibTableColumn
otuKiPmBerPreFecAve=_OtuKiPmBerPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,17),_OtuKiPmBerPreFecAve_Type())
otuKiPmBerPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPreFecAve.setStatus(_A)
_OtuKiPmBerPostFecMin_Type=FloatArbitraryPrecision
_OtuKiPmBerPostFecMin_Object=MibTableColumn
otuKiPmBerPostFecMin=_OtuKiPmBerPostFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,18),_OtuKiPmBerPostFecMin_Type())
otuKiPmBerPostFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPostFecMin.setStatus(_A)
_OtuKiPmBerPostFecMax_Type=FloatArbitraryPrecision
_OtuKiPmBerPostFecMax_Object=MibTableColumn
otuKiPmBerPostFecMax=_OtuKiPmBerPostFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,19),_OtuKiPmBerPostFecMax_Type())
otuKiPmBerPostFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPostFecMax.setStatus(_A)
_OtuKiPmBerPostFecAve_Type=FloatArbitraryPrecision
_OtuKiPmBerPostFecAve_Object=MibTableColumn
otuKiPmBerPostFecAve=_OtuKiPmBerPostFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,20),_OtuKiPmBerPostFecAve_Type())
otuKiPmBerPostFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmBerPostFecAve.setStatus(_A)
_OtuKiPmRxDefectSecondsFEND_Type=Integer32
_OtuKiPmRxDefectSecondsFEND_Object=MibTableColumn
otuKiPmRxDefectSecondsFEND=_OtuKiPmRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,21),_OtuKiPmRxDefectSecondsFEND_Type())
otuKiPmRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRxDefectSecondsFEND.setStatus(_A)
_OtuKiPmCorrectedBits_Type=HCPerfIntervalCount
_OtuKiPmCorrectedBits_Object=MibTableColumn
otuKiPmCorrectedBits=_OtuKiPmCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,22),_OtuKiPmCorrectedBits_Type())
otuKiPmCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmCorrectedBits.setStatus(_A)
_OtuKiPmRxBEICount_Type=HCPerfIntervalCount
_OtuKiPmRxBEICount_Object=MibTableColumn
otuKiPmRxBEICount=_OtuKiPmRxBEICount_Object((1,3,6,1,4,1,21296,2,2,2,3,27,2,1,23),_OtuKiPmRxBEICount_Type())
otuKiPmRxBEICount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuKiPmRxBEICount.setStatus(_A)
_OtuKiPmConformance_ObjectIdentity=ObjectIdentity
otuKiPmConformance=_OtuKiPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,27,3))
_OtuKiPmCompliances_ObjectIdentity=ObjectIdentity
otuKiPmCompliances=_OtuKiPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,27,3,1))
_OtuKiPmGroups_ObjectIdentity=ObjectIdentity
otuKiPmGroups=_OtuKiPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,27,3,2))
otuKiPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,27,3,2,1))
otuKiPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:otuKiPmGroup.setStatus(_A)
otuKiPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,27,3,2,2))
otuKiPmRealGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:otuKiPmRealGroup.setStatus(_A)
otuKiPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,27,3,1,1))
otuKiPmCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:otuKiPmCompliance.setStatus(_A)
otuKiPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,27,3,1,2))
otuKiPmRealCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:otuKiPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otuKiPmMIB':otuKiPmMIB,'otuKiPmRealTable':otuKiPmRealTable,'otuKiPmRealEntry':otuKiPmRealEntry,_e:otuKiPmRealNumberOfCodeWords,_f:otuKiPmRealNumberOfUncorrectedWords,_g:otuKiPmRealNumberOfCorrectedZeros,_h:otuKiPmRealNumberOfCorrectedOnes,_i:otuKiPmRealRxErroredBlocks,_j:otuKiPmRealRxDefectSeconds,_k:otuKiPmRealQValue,_l:otuKiPmRealBerPreFec,_m:otuKiPmRealBerPostFec,_n:otuKiPmRealRxDefectSecondsFEND,_o:otuKiPmRealCorrectedBits,_p:otuKiPmRealRxBEICount,'otuKiPmTable':otuKiPmTable,'otuKiPmEntry':otuKiPmEntry,_G:otuKiPmTimestamp,_F:otuKiPmSampleDuration,_J:otuKiPmValidity,_K:otuKiPmNumberOfCodeWords,_L:otuKiPmNumberOfUncorrectedWords,_M:otuKiPmNumberOfCorrectedZeros,_N:otuKiPmNumberOfCorrectedOnes,_O:otuKiPmRxErroredBlocks,_P:otuKiPmRxDefectSeconds,_Q:otuKiPmCircuitId,_R:otuKiPmPayloadType,_S:otuKiPmQValueMin,_T:otuKiPmQValueMax,_U:otuKiPmQValueAve,_V:otuKiPmBerPreFecMin,_W:otuKiPmBerPreFecMax,_X:otuKiPmBerPreFecAve,_Y:otuKiPmBerPostFecMin,_Z:otuKiPmBerPostFecMax,_a:otuKiPmBerPostFecAve,_b:otuKiPmRxDefectSecondsFEND,_c:otuKiPmCorrectedBits,_d:otuKiPmRxBEICount,'otuKiPmConformance':otuKiPmConformance,'otuKiPmCompliances':otuKiPmCompliances,'otuKiPmCompliance':otuKiPmCompliance,'otuKiPmRealCompliance':otuKiPmRealCompliance,'otuKiPmGroups':otuKiPmGroups,_q:otuKiPmGroup,_r:otuKiPmRealGroup})