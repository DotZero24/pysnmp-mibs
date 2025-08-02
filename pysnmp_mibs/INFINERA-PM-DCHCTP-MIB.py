_k='dchCtpPmRealGroup'
_j='dchCtpPmGroup'
_i='dchCtpPmRealTribPRBSErr'
_h='dchCtpPmRealTribPRBSSyncErr'
_g='dchCtpPmRealLinePRBSErr'
_f='dchCtpPmRealLinePRBSSyncErr'
_e='dchCtpPmRealCktId'
_d='dchCtpPmRealDtsSEFS'
_c='dchCtpPmRealDtsSES'
_b='dchCtpPmRealDtsES'
_a='dchCtpPmRealDtsCV'
_Z='dchCtpPmRealFecTotalCodeWords'
_Y='dchCtpPmRealFecUncorrectedRows'
_X='dchCtpPmRealFecCorrectedBits'
_W='dchCtpPmRealBerPostFec'
_V='dchCtpPmRealBerPreFec'
_U='dchCtpPmRealQ'
_T='dchCtpPmTribPRBSErr'
_S='dchCtpPmTribPRBSSyncErr'
_R='dchCtpPmCktId'
_Q='dchCtpPmDtsSEFS'
_P='dchCtpPmDtsSES'
_O='dchCtpPmDtsES'
_N='dchCtpPmDtsCV'
_M='dchCtpPmFecTotalCodeWords'
_L='dchCtpPmFecUncorrectedRows'
_K='dchCtpPmFecCorrectedBits'
_J='dchCtpPmValidity'
_I='not-accessible'
_H='dchCtpPmTimestamp'
_G='dchCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-DCHCTP-MIB'
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
dchCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,4))
if mibBuilder.loadTexts:dchCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_DchCtpPmRealTable_Object=MibTable
dchCtpPmRealTable=_DchCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1))
if mibBuilder.loadTexts:dchCtpPmRealTable.setStatus(_A)
_DchCtpPmRealEntry_Object=MibTableRow
dchCtpPmRealEntry=_DchCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1))
dchCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dchCtpPmRealEntry.setStatus(_A)
_DchCtpPmRealQ_Type=FloatHundredths
_DchCtpPmRealQ_Object=MibTableColumn
dchCtpPmRealQ=_DchCtpPmRealQ_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,1),_DchCtpPmRealQ_Type())
dchCtpPmRealQ.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealQ.setStatus(_A)
_DchCtpPmRealBerPreFec_Type=FloatArbitraryPrecision
_DchCtpPmRealBerPreFec_Object=MibTableColumn
dchCtpPmRealBerPreFec=_DchCtpPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,2),_DchCtpPmRealBerPreFec_Type())
dchCtpPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealBerPreFec.setStatus(_A)
_DchCtpPmRealBerPostFec_Type=FloatArbitraryPrecision
_DchCtpPmRealBerPostFec_Object=MibTableColumn
dchCtpPmRealBerPostFec=_DchCtpPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,3),_DchCtpPmRealBerPostFec_Type())
dchCtpPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealBerPostFec.setStatus(_A)
_DchCtpPmRealFecCorrectedBits_Type=Counter64
_DchCtpPmRealFecCorrectedBits_Object=MibTableColumn
dchCtpPmRealFecCorrectedBits=_DchCtpPmRealFecCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,4),_DchCtpPmRealFecCorrectedBits_Type())
dchCtpPmRealFecCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealFecCorrectedBits.setStatus(_A)
_DchCtpPmRealFecUncorrectedRows_Type=Counter64
_DchCtpPmRealFecUncorrectedRows_Object=MibTableColumn
dchCtpPmRealFecUncorrectedRows=_DchCtpPmRealFecUncorrectedRows_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,5),_DchCtpPmRealFecUncorrectedRows_Type())
dchCtpPmRealFecUncorrectedRows.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealFecUncorrectedRows.setStatus(_A)
_DchCtpPmRealFecTotalCodeWords_Type=Counter64
_DchCtpPmRealFecTotalCodeWords_Object=MibTableColumn
dchCtpPmRealFecTotalCodeWords=_DchCtpPmRealFecTotalCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,6),_DchCtpPmRealFecTotalCodeWords_Type())
dchCtpPmRealFecTotalCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealFecTotalCodeWords.setStatus(_A)
_DchCtpPmRealDtsCV_Type=Counter64
_DchCtpPmRealDtsCV_Object=MibTableColumn
dchCtpPmRealDtsCV=_DchCtpPmRealDtsCV_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,7),_DchCtpPmRealDtsCV_Type())
dchCtpPmRealDtsCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealDtsCV.setStatus(_A)
_DchCtpPmRealDtsES_Type=Integer32
_DchCtpPmRealDtsES_Object=MibTableColumn
dchCtpPmRealDtsES=_DchCtpPmRealDtsES_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,8),_DchCtpPmRealDtsES_Type())
dchCtpPmRealDtsES.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealDtsES.setStatus(_A)
_DchCtpPmRealDtsSES_Type=Integer32
_DchCtpPmRealDtsSES_Object=MibTableColumn
dchCtpPmRealDtsSES=_DchCtpPmRealDtsSES_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,9),_DchCtpPmRealDtsSES_Type())
dchCtpPmRealDtsSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealDtsSES.setStatus(_A)
_DchCtpPmRealDtsSEFS_Type=Integer32
_DchCtpPmRealDtsSEFS_Object=MibTableColumn
dchCtpPmRealDtsSEFS=_DchCtpPmRealDtsSEFS_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,10),_DchCtpPmRealDtsSEFS_Type())
dchCtpPmRealDtsSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealDtsSEFS.setStatus(_A)
_DchCtpPmRealCktId_Type=DisplayString
_DchCtpPmRealCktId_Object=MibTableColumn
dchCtpPmRealCktId=_DchCtpPmRealCktId_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,11),_DchCtpPmRealCktId_Type())
dchCtpPmRealCktId.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealCktId.setStatus(_A)
_DchCtpPmRealLinePRBSSyncErr_Type=Integer32
_DchCtpPmRealLinePRBSSyncErr_Object=MibTableColumn
dchCtpPmRealLinePRBSSyncErr=_DchCtpPmRealLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,12),_DchCtpPmRealLinePRBSSyncErr_Type())
dchCtpPmRealLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealLinePRBSSyncErr.setStatus(_A)
_DchCtpPmRealLinePRBSErr_Type=HCPerfIntervalCount
_DchCtpPmRealLinePRBSErr_Object=MibTableColumn
dchCtpPmRealLinePRBSErr=_DchCtpPmRealLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,13),_DchCtpPmRealLinePRBSErr_Type())
dchCtpPmRealLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealLinePRBSErr.setStatus(_A)
_DchCtpPmRealTribPRBSSyncErr_Type=Integer32
_DchCtpPmRealTribPRBSSyncErr_Object=MibTableColumn
dchCtpPmRealTribPRBSSyncErr=_DchCtpPmRealTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,14),_DchCtpPmRealTribPRBSSyncErr_Type())
dchCtpPmRealTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealTribPRBSSyncErr.setStatus(_A)
_DchCtpPmRealTribPRBSErr_Type=HCPerfIntervalCount
_DchCtpPmRealTribPRBSErr_Object=MibTableColumn
dchCtpPmRealTribPRBSErr=_DchCtpPmRealTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,1,1,15),_DchCtpPmRealTribPRBSErr_Type())
dchCtpPmRealTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmRealTribPRBSErr.setStatus(_A)
_DchCtpPmTable_Object=MibTable
dchCtpPmTable=_DchCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2))
if mibBuilder.loadTexts:dchCtpPmTable.setStatus(_A)
_DchCtpPmEntry_Object=MibTableRow
dchCtpPmEntry=_DchCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1))
dchCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dchCtpPmEntry.setStatus(_A)
class _DchCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DchCtpPmTimestamp_Type.__name__=_F
_DchCtpPmTimestamp_Object=MibTableColumn
dchCtpPmTimestamp=_DchCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,1),_DchCtpPmTimestamp_Type())
dchCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:dchCtpPmTimestamp.setStatus(_A)
class _DchCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_DchCtpPmSampleDuration_Type.__name__=_F
_DchCtpPmSampleDuration_Object=MibTableColumn
dchCtpPmSampleDuration=_DchCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,2),_DchCtpPmSampleDuration_Type())
dchCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:dchCtpPmSampleDuration.setStatus(_A)
_DchCtpPmValidity_Type=TruthValue
_DchCtpPmValidity_Object=MibTableColumn
dchCtpPmValidity=_DchCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,3),_DchCtpPmValidity_Type())
dchCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmValidity.setStatus(_A)
_DchCtpPmFecCorrectedBits_Type=HCPerfIntervalCount
_DchCtpPmFecCorrectedBits_Object=MibTableColumn
dchCtpPmFecCorrectedBits=_DchCtpPmFecCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,4),_DchCtpPmFecCorrectedBits_Type())
dchCtpPmFecCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmFecCorrectedBits.setStatus(_A)
_DchCtpPmFecUncorrectedRows_Type=HCPerfIntervalCount
_DchCtpPmFecUncorrectedRows_Object=MibTableColumn
dchCtpPmFecUncorrectedRows=_DchCtpPmFecUncorrectedRows_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,5),_DchCtpPmFecUncorrectedRows_Type())
dchCtpPmFecUncorrectedRows.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmFecUncorrectedRows.setStatus(_A)
_DchCtpPmFecTotalCodeWords_Type=HCPerfIntervalCount
_DchCtpPmFecTotalCodeWords_Object=MibTableColumn
dchCtpPmFecTotalCodeWords=_DchCtpPmFecTotalCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,6),_DchCtpPmFecTotalCodeWords_Type())
dchCtpPmFecTotalCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmFecTotalCodeWords.setStatus(_A)
_DchCtpPmDtsCV_Type=HCPerfIntervalCount
_DchCtpPmDtsCV_Object=MibTableColumn
dchCtpPmDtsCV=_DchCtpPmDtsCV_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,7),_DchCtpPmDtsCV_Type())
dchCtpPmDtsCV.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmDtsCV.setStatus(_A)
_DchCtpPmDtsES_Type=Integer32
_DchCtpPmDtsES_Object=MibTableColumn
dchCtpPmDtsES=_DchCtpPmDtsES_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,8),_DchCtpPmDtsES_Type())
dchCtpPmDtsES.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmDtsES.setStatus(_A)
_DchCtpPmDtsSES_Type=Integer32
_DchCtpPmDtsSES_Object=MibTableColumn
dchCtpPmDtsSES=_DchCtpPmDtsSES_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,9),_DchCtpPmDtsSES_Type())
dchCtpPmDtsSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmDtsSES.setStatus(_A)
_DchCtpPmDtsSEFS_Type=Integer32
_DchCtpPmDtsSEFS_Object=MibTableColumn
dchCtpPmDtsSEFS=_DchCtpPmDtsSEFS_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,10),_DchCtpPmDtsSEFS_Type())
dchCtpPmDtsSEFS.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmDtsSEFS.setStatus(_A)
_DchCtpPmCktId_Type=DisplayString
_DchCtpPmCktId_Object=MibTableColumn
dchCtpPmCktId=_DchCtpPmCktId_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,11),_DchCtpPmCktId_Type())
dchCtpPmCktId.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmCktId.setStatus(_A)
_DchCtpPmTribPRBSSyncErr_Type=Integer32
_DchCtpPmTribPRBSSyncErr_Object=MibTableColumn
dchCtpPmTribPRBSSyncErr=_DchCtpPmTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,12),_DchCtpPmTribPRBSSyncErr_Type())
dchCtpPmTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmTribPRBSSyncErr.setStatus(_A)
_DchCtpPmTribPRBSErr_Type=HCPerfIntervalCount
_DchCtpPmTribPRBSErr_Object=MibTableColumn
dchCtpPmTribPRBSErr=_DchCtpPmTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,4,2,1,13),_DchCtpPmTribPRBSErr_Type())
dchCtpPmTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:dchCtpPmTribPRBSErr.setStatus(_A)
_DchCtpPmConformance_ObjectIdentity=ObjectIdentity
dchCtpPmConformance=_DchCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,4,3))
_DchCtpPmCompliances_ObjectIdentity=ObjectIdentity
dchCtpPmCompliances=_DchCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,4,3,1))
_DchCtpPmGroups_ObjectIdentity=ObjectIdentity
dchCtpPmGroups=_DchCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,4,3,2))
dchCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,4,3,2,1))
dchCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dchCtpPmGroup.setStatus(_A)
dchCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,4,3,2,2))
dchCtpPmRealGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:dchCtpPmRealGroup.setStatus(_A)
dchCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,4,3,1,1))
dchCtpPmCompliance.setObjects((_B,_j))
if mibBuilder.loadTexts:dchCtpPmCompliance.setStatus(_A)
dchCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,4,3,1,2))
dchCtpPmRealCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:dchCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dchCtpPmMIB':dchCtpPmMIB,'dchCtpPmRealTable':dchCtpPmRealTable,'dchCtpPmRealEntry':dchCtpPmRealEntry,_U:dchCtpPmRealQ,_V:dchCtpPmRealBerPreFec,_W:dchCtpPmRealBerPostFec,_X:dchCtpPmRealFecCorrectedBits,_Y:dchCtpPmRealFecUncorrectedRows,_Z:dchCtpPmRealFecTotalCodeWords,_a:dchCtpPmRealDtsCV,_b:dchCtpPmRealDtsES,_c:dchCtpPmRealDtsSES,_d:dchCtpPmRealDtsSEFS,_e:dchCtpPmRealCktId,_f:dchCtpPmRealLinePRBSSyncErr,_g:dchCtpPmRealLinePRBSErr,_h:dchCtpPmRealTribPRBSSyncErr,_i:dchCtpPmRealTribPRBSErr,'dchCtpPmTable':dchCtpPmTable,'dchCtpPmEntry':dchCtpPmEntry,_H:dchCtpPmTimestamp,_G:dchCtpPmSampleDuration,_J:dchCtpPmValidity,_K:dchCtpPmFecCorrectedBits,_L:dchCtpPmFecUncorrectedRows,_M:dchCtpPmFecTotalCodeWords,_N:dchCtpPmDtsCV,_O:dchCtpPmDtsES,_P:dchCtpPmDtsSES,_Q:dchCtpPmDtsSEFS,_R:dchCtpPmCktId,_S:dchCtpPmTribPRBSSyncErr,_T:dchCtpPmTribPRBSErr,'dchCtpPmConformance':dchCtpPmConformance,'dchCtpPmCompliances':dchCtpPmCompliances,'dchCtpPmCompliance':dchCtpPmCompliance,'dchCtpPmRealCompliance':dchCtpPmRealCompliance,'dchCtpPmGroups':dchCtpPmGroups,_j:dchCtpPmGroup,_k:dchCtpPmRealGroup})