_m='dwCtpPmRealGroup'
_l='dwCtpPmGroup'
_k='dwCtpPmRealPropagationDelay'
_j='dwCtpPmRealCorrectedBits'
_i='dwCtpPmRealUnCorrectedBits'
_h='dwCtpPmRealBerPostFec'
_g='dwCtpPmRealBerPreFec'
_f='dwCtpPmRealPreFecQ'
_e='dwCtpPmRealPostFecQ'
_d='dwCtpPmRealFecUncorCodeWords'
_c='dwCtpPmRealFecCodeWords'
_b='dwCtpPmPropagationDelayAve'
_a='dwCtpPmPropagationDelayMax'
_Z='dwCtpPmPropagationDelayMin'
_Y='dwCtpPmCorrectedBits'
_X='dwCtpPmUnCorrectedBits'
_W='dwCtpPmBerPostFecAve'
_V='dwCtpPmBerPostFecMax'
_U='dwCtpPmBerPostFecMin'
_T='dwCtpPmBerPreFecAve'
_S='dwCtpPmBerPreFecMax'
_R='dwCtpPmBerPreFecMin'
_Q='dwCtpPmPreFecQAve'
_P='dwCtpPmPreFecQMax'
_O='dwCtpPmPreFecQMin'
_N='dwCtpPmPostFecQave'
_M='dwCtpPmPostFecQmax'
_L='dwCtpPmPostFecQmin'
_K='dwCtpPmFecUncorCodeWords'
_J='dwCtpPmFecCodeWords'
_I='not-accessible'
_H='dwCtpPmTimestamp'
_G='dwCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-DWCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dwCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,47))
if mibBuilder.loadTexts:dwCtpPmMIB.setRevisions(('2017-01-03 00:00',))
_DwCtpPmRealTable_Object=MibTable
dwCtpPmRealTable=_DwCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1))
if mibBuilder.loadTexts:dwCtpPmRealTable.setStatus(_A)
_DwCtpPmRealEntry_Object=MibTableRow
dwCtpPmRealEntry=_DwCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1))
dwCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dwCtpPmRealEntry.setStatus(_A)
_DwCtpPmRealFecCodeWords_Type=Counter64
_DwCtpPmRealFecCodeWords_Object=MibTableColumn
dwCtpPmRealFecCodeWords=_DwCtpPmRealFecCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,1),_DwCtpPmRealFecCodeWords_Type())
dwCtpPmRealFecCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealFecCodeWords.setStatus(_A)
_DwCtpPmRealFecUncorCodeWords_Type=Counter64
_DwCtpPmRealFecUncorCodeWords_Object=MibTableColumn
dwCtpPmRealFecUncorCodeWords=_DwCtpPmRealFecUncorCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,2),_DwCtpPmRealFecUncorCodeWords_Type())
dwCtpPmRealFecUncorCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealFecUncorCodeWords.setStatus(_A)
_DwCtpPmRealPostFecQ_Type=FloatArbitraryPrecision
_DwCtpPmRealPostFecQ_Object=MibTableColumn
dwCtpPmRealPostFecQ=_DwCtpPmRealPostFecQ_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,3),_DwCtpPmRealPostFecQ_Type())
dwCtpPmRealPostFecQ.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealPostFecQ.setStatus(_A)
_DwCtpPmRealPreFecQ_Type=FloatArbitraryPrecision
_DwCtpPmRealPreFecQ_Object=MibTableColumn
dwCtpPmRealPreFecQ=_DwCtpPmRealPreFecQ_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,4),_DwCtpPmRealPreFecQ_Type())
dwCtpPmRealPreFecQ.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealPreFecQ.setStatus(_A)
_DwCtpPmRealBerPreFec_Type=FloatArbitraryPrecision
_DwCtpPmRealBerPreFec_Object=MibTableColumn
dwCtpPmRealBerPreFec=_DwCtpPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,5),_DwCtpPmRealBerPreFec_Type())
dwCtpPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealBerPreFec.setStatus(_A)
_DwCtpPmRealBerPostFec_Type=FloatArbitraryPrecision
_DwCtpPmRealBerPostFec_Object=MibTableColumn
dwCtpPmRealBerPostFec=_DwCtpPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,6),_DwCtpPmRealBerPostFec_Type())
dwCtpPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealBerPostFec.setStatus(_A)
_DwCtpPmRealUnCorrectedBits_Type=Counter64
_DwCtpPmRealUnCorrectedBits_Object=MibTableColumn
dwCtpPmRealUnCorrectedBits=_DwCtpPmRealUnCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,7),_DwCtpPmRealUnCorrectedBits_Type())
dwCtpPmRealUnCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealUnCorrectedBits.setStatus(_A)
_DwCtpPmRealCorrectedBits_Type=Counter64
_DwCtpPmRealCorrectedBits_Object=MibTableColumn
dwCtpPmRealCorrectedBits=_DwCtpPmRealCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,8),_DwCtpPmRealCorrectedBits_Type())
dwCtpPmRealCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealCorrectedBits.setStatus(_A)
_DwCtpPmRealPropagationDelay_Type=FloatArbitraryPrecision
_DwCtpPmRealPropagationDelay_Object=MibTableColumn
dwCtpPmRealPropagationDelay=_DwCtpPmRealPropagationDelay_Object((1,3,6,1,4,1,21296,2,2,2,3,47,1,1,9),_DwCtpPmRealPropagationDelay_Type())
dwCtpPmRealPropagationDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmRealPropagationDelay.setStatus(_A)
_DwCtpPmTable_Object=MibTable
dwCtpPmTable=_DwCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2))
if mibBuilder.loadTexts:dwCtpPmTable.setStatus(_A)
_DwCtpPmEntry_Object=MibTableRow
dwCtpPmEntry=_DwCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1))
dwCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dwCtpPmEntry.setStatus(_A)
class _DwCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DwCtpPmTimestamp_Type.__name__=_F
_DwCtpPmTimestamp_Object=MibTableColumn
dwCtpPmTimestamp=_DwCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,1),_DwCtpPmTimestamp_Type())
dwCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:dwCtpPmTimestamp.setStatus(_A)
class _DwCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_DwCtpPmSampleDuration_Type.__name__=_F
_DwCtpPmSampleDuration_Object=MibTableColumn
dwCtpPmSampleDuration=_DwCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,2),_DwCtpPmSampleDuration_Type())
dwCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:dwCtpPmSampleDuration.setStatus(_A)
_DwCtpPmValidity_Type=TruthValue
_DwCtpPmValidity_Object=MibTableColumn
dwCtpPmValidity=_DwCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,3),_DwCtpPmValidity_Type())
dwCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmValidity.setStatus(_A)
_DwCtpPmFecCodeWords_Type=Counter64
_DwCtpPmFecCodeWords_Object=MibTableColumn
dwCtpPmFecCodeWords=_DwCtpPmFecCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,4),_DwCtpPmFecCodeWords_Type())
dwCtpPmFecCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmFecCodeWords.setStatus(_A)
_DwCtpPmFecUncorCodeWords_Type=Counter64
_DwCtpPmFecUncorCodeWords_Object=MibTableColumn
dwCtpPmFecUncorCodeWords=_DwCtpPmFecUncorCodeWords_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,5),_DwCtpPmFecUncorCodeWords_Type())
dwCtpPmFecUncorCodeWords.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmFecUncorCodeWords.setStatus(_A)
_DwCtpPmPostFecQmin_Type=FloatArbitraryPrecision
_DwCtpPmPostFecQmin_Object=MibTableColumn
dwCtpPmPostFecQmin=_DwCtpPmPostFecQmin_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,6),_DwCtpPmPostFecQmin_Type())
dwCtpPmPostFecQmin.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPostFecQmin.setStatus(_A)
_DwCtpPmPostFecQmax_Type=FloatArbitraryPrecision
_DwCtpPmPostFecQmax_Object=MibTableColumn
dwCtpPmPostFecQmax=_DwCtpPmPostFecQmax_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,7),_DwCtpPmPostFecQmax_Type())
dwCtpPmPostFecQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPostFecQmax.setStatus(_A)
_DwCtpPmPostFecQave_Type=FloatArbitraryPrecision
_DwCtpPmPostFecQave_Object=MibTableColumn
dwCtpPmPostFecQave=_DwCtpPmPostFecQave_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,8),_DwCtpPmPostFecQave_Type())
dwCtpPmPostFecQave.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPostFecQave.setStatus(_A)
_DwCtpPmPreFecQMin_Type=FloatArbitraryPrecision
_DwCtpPmPreFecQMin_Object=MibTableColumn
dwCtpPmPreFecQMin=_DwCtpPmPreFecQMin_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,9),_DwCtpPmPreFecQMin_Type())
dwCtpPmPreFecQMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPreFecQMin.setStatus(_A)
_DwCtpPmPreFecQMax_Type=FloatArbitraryPrecision
_DwCtpPmPreFecQMax_Object=MibTableColumn
dwCtpPmPreFecQMax=_DwCtpPmPreFecQMax_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,10),_DwCtpPmPreFecQMax_Type())
dwCtpPmPreFecQMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPreFecQMax.setStatus(_A)
_DwCtpPmPreFecQAve_Type=FloatArbitraryPrecision
_DwCtpPmPreFecQAve_Object=MibTableColumn
dwCtpPmPreFecQAve=_DwCtpPmPreFecQAve_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,11),_DwCtpPmPreFecQAve_Type())
dwCtpPmPreFecQAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPreFecQAve.setStatus(_A)
_DwCtpPmBerPreFecMin_Type=FloatArbitraryPrecision
_DwCtpPmBerPreFecMin_Object=MibTableColumn
dwCtpPmBerPreFecMin=_DwCtpPmBerPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,12),_DwCtpPmBerPreFecMin_Type())
dwCtpPmBerPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPreFecMin.setStatus(_A)
_DwCtpPmBerPreFecMax_Type=FloatArbitraryPrecision
_DwCtpPmBerPreFecMax_Object=MibTableColumn
dwCtpPmBerPreFecMax=_DwCtpPmBerPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,13),_DwCtpPmBerPreFecMax_Type())
dwCtpPmBerPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPreFecMax.setStatus(_A)
_DwCtpPmBerPreFecAve_Type=FloatArbitraryPrecision
_DwCtpPmBerPreFecAve_Object=MibTableColumn
dwCtpPmBerPreFecAve=_DwCtpPmBerPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,14),_DwCtpPmBerPreFecAve_Type())
dwCtpPmBerPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPreFecAve.setStatus(_A)
_DwCtpPmBerPostFecMin_Type=FloatArbitraryPrecision
_DwCtpPmBerPostFecMin_Object=MibTableColumn
dwCtpPmBerPostFecMin=_DwCtpPmBerPostFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,15),_DwCtpPmBerPostFecMin_Type())
dwCtpPmBerPostFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPostFecMin.setStatus(_A)
_DwCtpPmBerPostFecMax_Type=FloatArbitraryPrecision
_DwCtpPmBerPostFecMax_Object=MibTableColumn
dwCtpPmBerPostFecMax=_DwCtpPmBerPostFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,16),_DwCtpPmBerPostFecMax_Type())
dwCtpPmBerPostFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPostFecMax.setStatus(_A)
_DwCtpPmBerPostFecAve_Type=FloatArbitraryPrecision
_DwCtpPmBerPostFecAve_Object=MibTableColumn
dwCtpPmBerPostFecAve=_DwCtpPmBerPostFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,17),_DwCtpPmBerPostFecAve_Type())
dwCtpPmBerPostFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmBerPostFecAve.setStatus(_A)
_DwCtpPmUnCorrectedBits_Type=Counter64
_DwCtpPmUnCorrectedBits_Object=MibTableColumn
dwCtpPmUnCorrectedBits=_DwCtpPmUnCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,18),_DwCtpPmUnCorrectedBits_Type())
dwCtpPmUnCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmUnCorrectedBits.setStatus(_A)
_DwCtpPmCorrectedBits_Type=Counter64
_DwCtpPmCorrectedBits_Object=MibTableColumn
dwCtpPmCorrectedBits=_DwCtpPmCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,19),_DwCtpPmCorrectedBits_Type())
dwCtpPmCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmCorrectedBits.setStatus(_A)
_DwCtpPmPropagationDelayMin_Type=FloatArbitraryPrecision
_DwCtpPmPropagationDelayMin_Object=MibTableColumn
dwCtpPmPropagationDelayMin=_DwCtpPmPropagationDelayMin_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,20),_DwCtpPmPropagationDelayMin_Type())
dwCtpPmPropagationDelayMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPropagationDelayMin.setStatus(_A)
_DwCtpPmPropagationDelayMax_Type=FloatArbitraryPrecision
_DwCtpPmPropagationDelayMax_Object=MibTableColumn
dwCtpPmPropagationDelayMax=_DwCtpPmPropagationDelayMax_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,21),_DwCtpPmPropagationDelayMax_Type())
dwCtpPmPropagationDelayMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPropagationDelayMax.setStatus(_A)
_DwCtpPmPropagationDelayAve_Type=FloatArbitraryPrecision
_DwCtpPmPropagationDelayAve_Object=MibTableColumn
dwCtpPmPropagationDelayAve=_DwCtpPmPropagationDelayAve_Object((1,3,6,1,4,1,21296,2,2,2,3,47,2,1,22),_DwCtpPmPropagationDelayAve_Type())
dwCtpPmPropagationDelayAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dwCtpPmPropagationDelayAve.setStatus(_A)
_DwCtpPmConformance_ObjectIdentity=ObjectIdentity
dwCtpPmConformance=_DwCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,47,3))
_DwCtpPmCompliances_ObjectIdentity=ObjectIdentity
dwCtpPmCompliances=_DwCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,47,3,1))
_DwCtpPmGroups_ObjectIdentity=ObjectIdentity
dwCtpPmGroups=_DwCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,47,3,2))
dwCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,47,3,2,1))
dwCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:dwCtpPmGroup.setStatus(_A)
dwCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,47,3,2,2))
dwCtpPmRealGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:dwCtpPmRealGroup.setStatus(_A)
dwCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,47,3,1,1))
dwCtpPmCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:dwCtpPmCompliance.setStatus(_A)
dwCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,47,3,1,2))
dwCtpPmRealCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:dwCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dwCtpPmMIB':dwCtpPmMIB,'dwCtpPmRealTable':dwCtpPmRealTable,'dwCtpPmRealEntry':dwCtpPmRealEntry,_c:dwCtpPmRealFecCodeWords,_d:dwCtpPmRealFecUncorCodeWords,_e:dwCtpPmRealPostFecQ,_f:dwCtpPmRealPreFecQ,_g:dwCtpPmRealBerPreFec,_h:dwCtpPmRealBerPostFec,_i:dwCtpPmRealUnCorrectedBits,_j:dwCtpPmRealCorrectedBits,_k:dwCtpPmRealPropagationDelay,'dwCtpPmTable':dwCtpPmTable,'dwCtpPmEntry':dwCtpPmEntry,_H:dwCtpPmTimestamp,_G:dwCtpPmSampleDuration,'dwCtpPmValidity':dwCtpPmValidity,_J:dwCtpPmFecCodeWords,_K:dwCtpPmFecUncorCodeWords,_L:dwCtpPmPostFecQmin,_M:dwCtpPmPostFecQmax,_N:dwCtpPmPostFecQave,_O:dwCtpPmPreFecQMin,_P:dwCtpPmPreFecQMax,_Q:dwCtpPmPreFecQAve,_R:dwCtpPmBerPreFecMin,_S:dwCtpPmBerPreFecMax,_T:dwCtpPmBerPreFecAve,_U:dwCtpPmBerPostFecMin,_V:dwCtpPmBerPostFecMax,_W:dwCtpPmBerPostFecAve,_X:dwCtpPmUnCorrectedBits,_Y:dwCtpPmCorrectedBits,_Z:dwCtpPmPropagationDelayMin,_a:dwCtpPmPropagationDelayMax,_b:dwCtpPmPropagationDelayAve,'dwCtpPmConformance':dwCtpPmConformance,'dwCtpPmCompliances':dwCtpPmCompliances,'dwCtpPmCompliance':dwCtpPmCompliance,'dwCtpPmRealCompliance':dwCtpPmRealCompliance,'dwCtpPmGroups':dwCtpPmGroups,_l:dwCtpPmGroup,_m:dwCtpPmRealGroup})