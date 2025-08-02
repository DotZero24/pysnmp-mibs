_A3='otuPmRealGroup'
_A2='otuPmGroup'
_A1='otuPmRealTxBIAE'
_A0='otuPmRealRxBIAE'
_z='otuPmRealTxIAE'
_y='otuPmRealRxIAE'
_x='otuPmRealCorrectedBits'
_w='otuPmRealTxBeiCount'
_v='otuPmRealRxBeiCount'
_u='otuPmRealLinePRBSSyncErr'
_t='otuPmRealTribPRBSSyncErr'
_s='otuPmRealLinePRBSErr'
_r='otuPmRealTribPRBSErr'
_q='otuPmRealTxDefectSeconds'
_p='otuPmRealRxDefectSeconds'
_o='otuPmRealTxErroredBlocks'
_n='otuPmRealRxErroredBlocks'
_m='otuPmRealNumberOfCorrectedOnes'
_l='otuPmRealNumberOfCorrectedZeros'
_k='otuPmRealNumberOfUncorrectedWords'
_j='otuPmRealNumberOfCodeWords'
_i='otuPmTxBIAE'
_h='otuPmRxBIAE'
_g='otuPmTxIAE'
_f='otuPmRxIAE'
_e='otuPmCorrectedBits'
_d='otuPmPayloadType'
_c='otuPmCircuitId'
_b='otuPmTxBeiCount'
_a='otuPmRxBeiCount'
_Z='otuPmLinePRBSSyncErr'
_Y='otuPmTribPRBSSyncErr'
_X='otuPmLinePRBSErr'
_W='otuPmTribPRBSErr'
_V='otuPmTxDefectSeconds'
_U='otuPmRxDefectSeconds'
_T='otuPmTxErroredBlocks'
_S='otuPmRxErroredBlocks'
_R='otuPmTxCVS'
_Q='otuPmRxCVS'
_P='otuPmNumberOfCorrectedOnes'
_O='otuPmNumberOfCorrectedZeros'
_N='otuPmNumberOfUncorrectedWords'
_M='otuPmNumberOfCodeWords'
_L='otuPmValidity'
_K='not-accessible'
_J='Integer32'
_I='otuPmRealTxCVS'
_H='otuPmRealRxCVS'
_G='otuPmTimestamp'
_F='otuPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OTU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,InfnSampleDuration,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnSampleDuration','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
otuPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,22))
if mibBuilder.loadTexts:otuPmMIB.setRevisions(('2009-07-20 00:00',))
_OtuPmRealTable_Object=MibTable
otuPmRealTable=_OtuPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1))
if mibBuilder.loadTexts:otuPmRealTable.setStatus(_A)
_OtuPmRealEntry_Object=MibTableRow
otuPmRealEntry=_OtuPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1))
otuPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otuPmRealEntry.setStatus(_A)
_OtuPmRealNumberOfCodeWords_Type=HCPerfIntervalCount
_OtuPmRealNumberOfCodeWords_Object=MibTableColumn
otuPmRealNumberOfCodeWords=_OtuPmRealNumberOfCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,1),_OtuPmRealNumberOfCodeWords_Type())
otuPmRealNumberOfCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealNumberOfCodeWords.setStatus(_A)
_OtuPmRealNumberOfUncorrectedWords_Type=HCPerfIntervalCount
_OtuPmRealNumberOfUncorrectedWords_Object=MibTableColumn
otuPmRealNumberOfUncorrectedWords=_OtuPmRealNumberOfUncorrectedWords_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,2),_OtuPmRealNumberOfUncorrectedWords_Type())
otuPmRealNumberOfUncorrectedWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealNumberOfUncorrectedWords.setStatus(_A)
_OtuPmRealNumberOfCorrectedZeros_Type=HCPerfIntervalCount
_OtuPmRealNumberOfCorrectedZeros_Object=MibTableColumn
otuPmRealNumberOfCorrectedZeros=_OtuPmRealNumberOfCorrectedZeros_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,3),_OtuPmRealNumberOfCorrectedZeros_Type())
otuPmRealNumberOfCorrectedZeros.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealNumberOfCorrectedZeros.setStatus(_A)
_OtuPmRealNumberOfCorrectedOnes_Type=HCPerfIntervalCount
_OtuPmRealNumberOfCorrectedOnes_Object=MibTableColumn
otuPmRealNumberOfCorrectedOnes=_OtuPmRealNumberOfCorrectedOnes_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,4),_OtuPmRealNumberOfCorrectedOnes_Type())
otuPmRealNumberOfCorrectedOnes.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealNumberOfCorrectedOnes.setStatus(_A)
_OtuPmRealRxCVS_Type=HCPerfIntervalCount
_OtuPmRealRxCVS_Object=MibTableColumn
otuPmRealRxCVS=_OtuPmRealRxCVS_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,5),_OtuPmRealRxCVS_Type())
otuPmRealRxCVS.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxCVS.setStatus(_A)
_OtuPmRealTxCVS_Type=HCPerfIntervalCount
_OtuPmRealTxCVS_Object=MibTableColumn
otuPmRealTxCVS=_OtuPmRealTxCVS_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,6),_OtuPmRealTxCVS_Type())
otuPmRealTxCVS.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxCVS.setStatus(_A)
_OtuPmRealRxErroredBlocks_Type=HCPerfIntervalCount
_OtuPmRealRxErroredBlocks_Object=MibTableColumn
otuPmRealRxErroredBlocks=_OtuPmRealRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,7),_OtuPmRealRxErroredBlocks_Type())
otuPmRealRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxErroredBlocks.setStatus(_A)
_OtuPmRealTxErroredBlocks_Type=HCPerfIntervalCount
_OtuPmRealTxErroredBlocks_Object=MibTableColumn
otuPmRealTxErroredBlocks=_OtuPmRealTxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,8),_OtuPmRealTxErroredBlocks_Type())
otuPmRealTxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxErroredBlocks.setStatus(_A)
_OtuPmRealRxDefectSeconds_Type=Integer32
_OtuPmRealRxDefectSeconds_Object=MibTableColumn
otuPmRealRxDefectSeconds=_OtuPmRealRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,9),_OtuPmRealRxDefectSeconds_Type())
otuPmRealRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxDefectSeconds.setStatus(_A)
_OtuPmRealTxDefectSeconds_Type=Integer32
_OtuPmRealTxDefectSeconds_Object=MibTableColumn
otuPmRealTxDefectSeconds=_OtuPmRealTxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,10),_OtuPmRealTxDefectSeconds_Type())
otuPmRealTxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxDefectSeconds.setStatus(_A)
_OtuPmRealTribPRBSErr_Type=HCPerfIntervalCount
_OtuPmRealTribPRBSErr_Object=MibTableColumn
otuPmRealTribPRBSErr=_OtuPmRealTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,11),_OtuPmRealTribPRBSErr_Type())
otuPmRealTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTribPRBSErr.setStatus(_A)
_OtuPmRealLinePRBSErr_Type=HCPerfIntervalCount
_OtuPmRealLinePRBSErr_Object=MibTableColumn
otuPmRealLinePRBSErr=_OtuPmRealLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,12),_OtuPmRealLinePRBSErr_Type())
otuPmRealLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealLinePRBSErr.setStatus(_A)
_OtuPmRealTribPRBSSyncErr_Type=Integer32
_OtuPmRealTribPRBSSyncErr_Object=MibTableColumn
otuPmRealTribPRBSSyncErr=_OtuPmRealTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,13),_OtuPmRealTribPRBSSyncErr_Type())
otuPmRealTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTribPRBSSyncErr.setStatus(_A)
_OtuPmRealLinePRBSSyncErr_Type=Integer32
_OtuPmRealLinePRBSSyncErr_Object=MibTableColumn
otuPmRealLinePRBSSyncErr=_OtuPmRealLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,14),_OtuPmRealLinePRBSSyncErr_Type())
otuPmRealLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealLinePRBSSyncErr.setStatus(_A)
_OtuPmRealRxBeiCount_Type=HCPerfIntervalCount
_OtuPmRealRxBeiCount_Object=MibTableColumn
otuPmRealRxBeiCount=_OtuPmRealRxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,15),_OtuPmRealRxBeiCount_Type())
otuPmRealRxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxBeiCount.setStatus(_A)
_OtuPmRealTxBeiCount_Type=HCPerfIntervalCount
_OtuPmRealTxBeiCount_Object=MibTableColumn
otuPmRealTxBeiCount=_OtuPmRealTxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,16),_OtuPmRealTxBeiCount_Type())
otuPmRealTxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxBeiCount.setStatus(_A)
_OtuPmRealRxErroredBlocksFEND_Type=HCPerfIntervalCount
_OtuPmRealRxErroredBlocksFEND_Object=MibTableColumn
otuPmRealRxErroredBlocksFEND=_OtuPmRealRxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,17),_OtuPmRealRxErroredBlocksFEND_Type())
otuPmRealRxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxErroredBlocksFEND.setStatus(_A)
_OtuPmRealTxErroredBlocksFEND_Type=HCPerfIntervalCount
_OtuPmRealTxErroredBlocksFEND_Object=MibTableColumn
otuPmRealTxErroredBlocksFEND=_OtuPmRealTxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,18),_OtuPmRealTxErroredBlocksFEND_Type())
otuPmRealTxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxErroredBlocksFEND.setStatus(_A)
_OtuPmRealRxDefectSecondsFEND_Type=Integer32
_OtuPmRealRxDefectSecondsFEND_Object=MibTableColumn
otuPmRealRxDefectSecondsFEND=_OtuPmRealRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,19),_OtuPmRealRxDefectSecondsFEND_Type())
otuPmRealRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxDefectSecondsFEND.setStatus(_A)
_OtuPmRealTxDefectSecondsFEND_Type=Integer32
_OtuPmRealTxDefectSecondsFEND_Object=MibTableColumn
otuPmRealTxDefectSecondsFEND=_OtuPmRealTxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,20),_OtuPmRealTxDefectSecondsFEND_Type())
otuPmRealTxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxDefectSecondsFEND.setStatus(_A)
_OtuPmRealCorrectedBits_Type=HCPerfIntervalCount
_OtuPmRealCorrectedBits_Object=MibTableColumn
otuPmRealCorrectedBits=_OtuPmRealCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,21),_OtuPmRealCorrectedBits_Type())
otuPmRealCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealCorrectedBits.setStatus(_A)
_OtuPmRealRxIAE_Type=Integer32
_OtuPmRealRxIAE_Object=MibTableColumn
otuPmRealRxIAE=_OtuPmRealRxIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,22),_OtuPmRealRxIAE_Type())
otuPmRealRxIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxIAE.setStatus(_A)
_OtuPmRealTxIAE_Type=Integer32
_OtuPmRealTxIAE_Object=MibTableColumn
otuPmRealTxIAE=_OtuPmRealTxIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,23),_OtuPmRealTxIAE_Type())
otuPmRealTxIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxIAE.setStatus(_A)
_OtuPmRealRxBIAE_Type=Integer32
_OtuPmRealRxBIAE_Object=MibTableColumn
otuPmRealRxBIAE=_OtuPmRealRxBIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,24),_OtuPmRealRxBIAE_Type())
otuPmRealRxBIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealRxBIAE.setStatus(_A)
_OtuPmRealTxBIAE_Type=Integer32
_OtuPmRealTxBIAE_Object=MibTableColumn
otuPmRealTxBIAE=_OtuPmRealTxBIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,1,1,25),_OtuPmRealTxBIAE_Type())
otuPmRealTxBIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRealTxBIAE.setStatus(_A)
_OtuPmTable_Object=MibTable
otuPmTable=_OtuPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2))
if mibBuilder.loadTexts:otuPmTable.setStatus(_A)
_OtuPmEntry_Object=MibTableRow
otuPmEntry=_OtuPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1))
otuPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:otuPmEntry.setStatus(_A)
class _OtuPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OtuPmTimestamp_Type.__name__=_J
_OtuPmTimestamp_Object=MibTableColumn
otuPmTimestamp=_OtuPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,1),_OtuPmTimestamp_Type())
otuPmTimestamp.setMaxAccess(_K)
if mibBuilder.loadTexts:otuPmTimestamp.setStatus(_A)
_OtuPmSampleDuration_Type=InfnSampleDuration
_OtuPmSampleDuration_Object=MibTableColumn
otuPmSampleDuration=_OtuPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,2),_OtuPmSampleDuration_Type())
otuPmSampleDuration.setMaxAccess(_K)
if mibBuilder.loadTexts:otuPmSampleDuration.setStatus(_A)
_OtuPmValidity_Type=TruthValue
_OtuPmValidity_Object=MibTableColumn
otuPmValidity=_OtuPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,3),_OtuPmValidity_Type())
otuPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmValidity.setStatus(_A)
_OtuPmNumberOfCodeWords_Type=HCPerfIntervalCount
_OtuPmNumberOfCodeWords_Object=MibTableColumn
otuPmNumberOfCodeWords=_OtuPmNumberOfCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,4),_OtuPmNumberOfCodeWords_Type())
otuPmNumberOfCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmNumberOfCodeWords.setStatus(_A)
_OtuPmNumberOfUncorrectedWords_Type=HCPerfIntervalCount
_OtuPmNumberOfUncorrectedWords_Object=MibTableColumn
otuPmNumberOfUncorrectedWords=_OtuPmNumberOfUncorrectedWords_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,5),_OtuPmNumberOfUncorrectedWords_Type())
otuPmNumberOfUncorrectedWords.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmNumberOfUncorrectedWords.setStatus(_A)
_OtuPmNumberOfCorrectedZeros_Type=HCPerfIntervalCount
_OtuPmNumberOfCorrectedZeros_Object=MibTableColumn
otuPmNumberOfCorrectedZeros=_OtuPmNumberOfCorrectedZeros_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,6),_OtuPmNumberOfCorrectedZeros_Type())
otuPmNumberOfCorrectedZeros.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmNumberOfCorrectedZeros.setStatus(_A)
_OtuPmNumberOfCorrectedOnes_Type=HCPerfIntervalCount
_OtuPmNumberOfCorrectedOnes_Object=MibTableColumn
otuPmNumberOfCorrectedOnes=_OtuPmNumberOfCorrectedOnes_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,7),_OtuPmNumberOfCorrectedOnes_Type())
otuPmNumberOfCorrectedOnes.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmNumberOfCorrectedOnes.setStatus(_A)
_OtuPmRxCVS_Type=HCPerfIntervalCount
_OtuPmRxCVS_Object=MibTableColumn
otuPmRxCVS=_OtuPmRxCVS_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,8),_OtuPmRxCVS_Type())
otuPmRxCVS.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxCVS.setStatus(_A)
_OtuPmTxCVS_Type=HCPerfIntervalCount
_OtuPmTxCVS_Object=MibTableColumn
otuPmTxCVS=_OtuPmTxCVS_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,9),_OtuPmTxCVS_Type())
otuPmTxCVS.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxCVS.setStatus(_A)
_OtuPmRxErroredBlocks_Type=HCPerfIntervalCount
_OtuPmRxErroredBlocks_Object=MibTableColumn
otuPmRxErroredBlocks=_OtuPmRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,10),_OtuPmRxErroredBlocks_Type())
otuPmRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxErroredBlocks.setStatus(_A)
_OtuPmTxErroredBlocks_Type=HCPerfIntervalCount
_OtuPmTxErroredBlocks_Object=MibTableColumn
otuPmTxErroredBlocks=_OtuPmTxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,11),_OtuPmTxErroredBlocks_Type())
otuPmTxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxErroredBlocks.setStatus(_A)
_OtuPmRxDefectSeconds_Type=Integer32
_OtuPmRxDefectSeconds_Object=MibTableColumn
otuPmRxDefectSeconds=_OtuPmRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,12),_OtuPmRxDefectSeconds_Type())
otuPmRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxDefectSeconds.setStatus(_A)
_OtuPmTxDefectSeconds_Type=Integer32
_OtuPmTxDefectSeconds_Object=MibTableColumn
otuPmTxDefectSeconds=_OtuPmTxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,13),_OtuPmTxDefectSeconds_Type())
otuPmTxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxDefectSeconds.setStatus(_A)
_OtuPmTribPRBSErr_Type=HCPerfIntervalCount
_OtuPmTribPRBSErr_Object=MibTableColumn
otuPmTribPRBSErr=_OtuPmTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,14),_OtuPmTribPRBSErr_Type())
otuPmTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTribPRBSErr.setStatus(_A)
_OtuPmLinePRBSErr_Type=HCPerfIntervalCount
_OtuPmLinePRBSErr_Object=MibTableColumn
otuPmLinePRBSErr=_OtuPmLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,15),_OtuPmLinePRBSErr_Type())
otuPmLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmLinePRBSErr.setStatus(_A)
_OtuPmTribPRBSSyncErr_Type=Integer32
_OtuPmTribPRBSSyncErr_Object=MibTableColumn
otuPmTribPRBSSyncErr=_OtuPmTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,16),_OtuPmTribPRBSSyncErr_Type())
otuPmTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTribPRBSSyncErr.setStatus(_A)
_OtuPmLinePRBSSyncErr_Type=Integer32
_OtuPmLinePRBSSyncErr_Object=MibTableColumn
otuPmLinePRBSSyncErr=_OtuPmLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,17),_OtuPmLinePRBSSyncErr_Type())
otuPmLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmLinePRBSSyncErr.setStatus(_A)
_OtuPmRxBeiCount_Type=HCPerfIntervalCount
_OtuPmRxBeiCount_Object=MibTableColumn
otuPmRxBeiCount=_OtuPmRxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,18),_OtuPmRxBeiCount_Type())
otuPmRxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxBeiCount.setStatus(_A)
_OtuPmTxBeiCount_Type=HCPerfIntervalCount
_OtuPmTxBeiCount_Object=MibTableColumn
otuPmTxBeiCount=_OtuPmTxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,19),_OtuPmTxBeiCount_Type())
otuPmTxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxBeiCount.setStatus(_A)
_OtuPmCircuitId_Type=DisplayString
_OtuPmCircuitId_Object=MibTableColumn
otuPmCircuitId=_OtuPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,20),_OtuPmCircuitId_Type())
otuPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmCircuitId.setStatus(_A)
_OtuPmPayloadType_Type=InfnServiceType
_OtuPmPayloadType_Object=MibTableColumn
otuPmPayloadType=_OtuPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,21),_OtuPmPayloadType_Type())
otuPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmPayloadType.setStatus(_A)
_OtuPmRxErroredBlocksFEND_Type=HCPerfIntervalCount
_OtuPmRxErroredBlocksFEND_Object=MibTableColumn
otuPmRxErroredBlocksFEND=_OtuPmRxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,22),_OtuPmRxErroredBlocksFEND_Type())
otuPmRxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxErroredBlocksFEND.setStatus(_A)
_OtuPmTxErroredBlocksFEND_Type=HCPerfIntervalCount
_OtuPmTxErroredBlocksFEND_Object=MibTableColumn
otuPmTxErroredBlocksFEND=_OtuPmTxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,23),_OtuPmTxErroredBlocksFEND_Type())
otuPmTxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxErroredBlocksFEND.setStatus(_A)
_OtuPmRxDefectSecondsFEND_Type=Integer32
_OtuPmRxDefectSecondsFEND_Object=MibTableColumn
otuPmRxDefectSecondsFEND=_OtuPmRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,24),_OtuPmRxDefectSecondsFEND_Type())
otuPmRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxDefectSecondsFEND.setStatus(_A)
_OtuPmTxDefectSecondsFEND_Type=Integer32
_OtuPmTxDefectSecondsFEND_Object=MibTableColumn
otuPmTxDefectSecondsFEND=_OtuPmTxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,25),_OtuPmTxDefectSecondsFEND_Type())
otuPmTxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxDefectSecondsFEND.setStatus(_A)
_OtuPmCorrectedBits_Type=HCPerfIntervalCount
_OtuPmCorrectedBits_Object=MibTableColumn
otuPmCorrectedBits=_OtuPmCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,26),_OtuPmCorrectedBits_Type())
otuPmCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmCorrectedBits.setStatus(_A)
_OtuPmRxIAE_Type=Integer32
_OtuPmRxIAE_Object=MibTableColumn
otuPmRxIAE=_OtuPmRxIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,27),_OtuPmRxIAE_Type())
otuPmRxIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxIAE.setStatus(_A)
_OtuPmTxIAE_Type=Integer32
_OtuPmTxIAE_Object=MibTableColumn
otuPmTxIAE=_OtuPmTxIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,28),_OtuPmTxIAE_Type())
otuPmTxIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxIAE.setStatus(_A)
_OtuPmRxBIAE_Type=Integer32
_OtuPmRxBIAE_Object=MibTableColumn
otuPmRxBIAE=_OtuPmRxBIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,29),_OtuPmRxBIAE_Type())
otuPmRxBIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmRxBIAE.setStatus(_A)
_OtuPmTxBIAE_Type=Integer32
_OtuPmTxBIAE_Object=MibTableColumn
otuPmTxBIAE=_OtuPmTxBIAE_Object((1,3,6,1,4,1,21296,2,2,2,3,22,2,1,30),_OtuPmTxBIAE_Type())
otuPmTxBIAE.setMaxAccess(_C)
if mibBuilder.loadTexts:otuPmTxBIAE.setStatus(_A)
_OtuPmConformance_ObjectIdentity=ObjectIdentity
otuPmConformance=_OtuPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,22,3))
_OtuPmCompliances_ObjectIdentity=ObjectIdentity
otuPmCompliances=_OtuPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,22,3,1))
_OtuPmGroups_ObjectIdentity=ObjectIdentity
otuPmGroups=_OtuPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,22,3,2))
otuPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,22,3,2,1))
otuPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:otuPmGroup.setStatus(_A)
otuPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,22,3,2,2))
otuPmRealGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_H),(_B,_I),(_B,_n),(_B,_o),(_B,_H),(_B,_I),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:otuPmRealGroup.setStatus(_A)
otuPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,22,3,1,1))
otuPmCompliance.setObjects((_B,_A2))
if mibBuilder.loadTexts:otuPmCompliance.setStatus(_A)
otuPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,22,3,1,2))
otuPmRealCompliance.setObjects((_B,_A3))
if mibBuilder.loadTexts:otuPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otuPmMIB':otuPmMIB,'otuPmRealTable':otuPmRealTable,'otuPmRealEntry':otuPmRealEntry,_j:otuPmRealNumberOfCodeWords,_k:otuPmRealNumberOfUncorrectedWords,_l:otuPmRealNumberOfCorrectedZeros,_m:otuPmRealNumberOfCorrectedOnes,_H:otuPmRealRxCVS,_I:otuPmRealTxCVS,_n:otuPmRealRxErroredBlocks,_o:otuPmRealTxErroredBlocks,_p:otuPmRealRxDefectSeconds,_q:otuPmRealTxDefectSeconds,_r:otuPmRealTribPRBSErr,_s:otuPmRealLinePRBSErr,_t:otuPmRealTribPRBSSyncErr,_u:otuPmRealLinePRBSSyncErr,_v:otuPmRealRxBeiCount,_w:otuPmRealTxBeiCount,'otuPmRealRxErroredBlocksFEND':otuPmRealRxErroredBlocksFEND,'otuPmRealTxErroredBlocksFEND':otuPmRealTxErroredBlocksFEND,'otuPmRealRxDefectSecondsFEND':otuPmRealRxDefectSecondsFEND,'otuPmRealTxDefectSecondsFEND':otuPmRealTxDefectSecondsFEND,_x:otuPmRealCorrectedBits,_y:otuPmRealRxIAE,_z:otuPmRealTxIAE,_A0:otuPmRealRxBIAE,_A1:otuPmRealTxBIAE,'otuPmTable':otuPmTable,'otuPmEntry':otuPmEntry,_G:otuPmTimestamp,_F:otuPmSampleDuration,_L:otuPmValidity,_M:otuPmNumberOfCodeWords,_N:otuPmNumberOfUncorrectedWords,_O:otuPmNumberOfCorrectedZeros,_P:otuPmNumberOfCorrectedOnes,_Q:otuPmRxCVS,_R:otuPmTxCVS,_S:otuPmRxErroredBlocks,_T:otuPmTxErroredBlocks,_U:otuPmRxDefectSeconds,_V:otuPmTxDefectSeconds,_W:otuPmTribPRBSErr,_X:otuPmLinePRBSErr,_Y:otuPmTribPRBSSyncErr,_Z:otuPmLinePRBSSyncErr,_a:otuPmRxBeiCount,_b:otuPmTxBeiCount,_c:otuPmCircuitId,_d:otuPmPayloadType,'otuPmRxErroredBlocksFEND':otuPmRxErroredBlocksFEND,'otuPmTxErroredBlocksFEND':otuPmTxErroredBlocksFEND,'otuPmRxDefectSecondsFEND':otuPmRxDefectSecondsFEND,'otuPmTxDefectSecondsFEND':otuPmTxDefectSecondsFEND,_e:otuPmCorrectedBits,_f:otuPmRxIAE,_g:otuPmTxIAE,_h:otuPmRxBIAE,_i:otuPmTxBIAE,'otuPmConformance':otuPmConformance,'otuPmCompliances':otuPmCompliances,'otuPmCompliance':otuPmCompliance,'otuPmRealCompliance':otuPmRealCompliance,'otuPmGroups':otuPmGroups,_A2:otuPmGroup,_A3:otuPmRealGroup})