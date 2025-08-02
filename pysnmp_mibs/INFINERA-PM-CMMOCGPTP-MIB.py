_X='cmmOcgPtpPmRealGroup'
_W='cmmOcgPtpPmGroup'
_V='cmmOcgPtpPmRealCmmEdfaLbcTx'
_U='cmmOcgPtpPmRealCmmOcgOpr'
_T='cmmOcgPtpPmRealCmmOcgOpt'
_S='cmmOcgPtpPmCmmEdfaLbcTxAve'
_R='cmmOcgPtpPmCmmEdfaLbcTxMax'
_Q='cmmOcgPtpPmCmmEdfaLbcTxMin'
_P='cmmOcgPtpPmCmmOcgOprAve'
_O='cmmOcgPtpPmCmmOcgOprMax'
_N='cmmOcgPtpPmCmmOcgOprMin'
_M='cmmOcgPtpPmCmmOcgOptAve'
_L='cmmOcgPtpPmCmmOcgOptMax'
_K='cmmOcgPtpPmCmmOcgOptMin'
_J='cmmOcgPtpPmValidity'
_I='not-accessible'
_H='cmmOcgPtpPmTimestamp'
_G='cmmOcgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-CMMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cmmOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,25))
if mibBuilder.loadTexts:cmmOcgPtpPmMIB.setRevisions(('2011-05-23 00:00',))
_CmmOcgPtpPmRealTable_Object=MibTable
cmmOcgPtpPmRealTable=_CmmOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,25,1))
if mibBuilder.loadTexts:cmmOcgPtpPmRealTable.setStatus(_A)
_CmmOcgPtpPmRealEntry_Object=MibTableRow
cmmOcgPtpPmRealEntry=_CmmOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,25,1,1))
cmmOcgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cmmOcgPtpPmRealEntry.setStatus(_A)
_CmmOcgPtpPmRealCmmOcgOpt_Type=FloatHundredths
_CmmOcgPtpPmRealCmmOcgOpt_Object=MibTableColumn
cmmOcgPtpPmRealCmmOcgOpt=_CmmOcgPtpPmRealCmmOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,25,1,1,1),_CmmOcgPtpPmRealCmmOcgOpt_Type())
cmmOcgPtpPmRealCmmOcgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmRealCmmOcgOpt.setStatus(_A)
_CmmOcgPtpPmRealCmmOcgOpr_Type=FloatHundredths
_CmmOcgPtpPmRealCmmOcgOpr_Object=MibTableColumn
cmmOcgPtpPmRealCmmOcgOpr=_CmmOcgPtpPmRealCmmOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,25,1,1,2),_CmmOcgPtpPmRealCmmOcgOpr_Type())
cmmOcgPtpPmRealCmmOcgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmRealCmmOcgOpr.setStatus(_A)
_CmmOcgPtpPmRealCmmEdfaLbcTx_Type=FloatHundredths
_CmmOcgPtpPmRealCmmEdfaLbcTx_Object=MibTableColumn
cmmOcgPtpPmRealCmmEdfaLbcTx=_CmmOcgPtpPmRealCmmEdfaLbcTx_Object((1,3,6,1,4,1,21296,2,2,2,3,25,1,1,3),_CmmOcgPtpPmRealCmmEdfaLbcTx_Type())
cmmOcgPtpPmRealCmmEdfaLbcTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmRealCmmEdfaLbcTx.setStatus(_A)
_CmmOcgPtpPmTable_Object=MibTable
cmmOcgPtpPmTable=_CmmOcgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2))
if mibBuilder.loadTexts:cmmOcgPtpPmTable.setStatus(_A)
_CmmOcgPtpPmEntry_Object=MibTableRow
cmmOcgPtpPmEntry=_CmmOcgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1))
cmmOcgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cmmOcgPtpPmEntry.setStatus(_A)
class _CmmOcgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CmmOcgPtpPmTimestamp_Type.__name__=_F
_CmmOcgPtpPmTimestamp_Object=MibTableColumn
cmmOcgPtpPmTimestamp=_CmmOcgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,1),_CmmOcgPtpPmTimestamp_Type())
cmmOcgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOcgPtpPmTimestamp.setStatus(_A)
class _CmmOcgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_CmmOcgPtpPmSampleDuration_Type.__name__=_F
_CmmOcgPtpPmSampleDuration_Object=MibTableColumn
cmmOcgPtpPmSampleDuration=_CmmOcgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,2),_CmmOcgPtpPmSampleDuration_Type())
cmmOcgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOcgPtpPmSampleDuration.setStatus(_A)
_CmmOcgPtpPmValidity_Type=TruthValue
_CmmOcgPtpPmValidity_Object=MibTableColumn
cmmOcgPtpPmValidity=_CmmOcgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,3),_CmmOcgPtpPmValidity_Type())
cmmOcgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmValidity.setStatus(_A)
_CmmOcgPtpPmCmmOcgOptMin_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOptMin_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOptMin=_CmmOcgPtpPmCmmOcgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,4),_CmmOcgPtpPmCmmOcgOptMin_Type())
cmmOcgPtpPmCmmOcgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOptMin.setStatus(_A)
_CmmOcgPtpPmCmmOcgOptMax_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOptMax_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOptMax=_CmmOcgPtpPmCmmOcgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,5),_CmmOcgPtpPmCmmOcgOptMax_Type())
cmmOcgPtpPmCmmOcgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOptMax.setStatus(_A)
_CmmOcgPtpPmCmmOcgOptAve_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOptAve_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOptAve=_CmmOcgPtpPmCmmOcgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,6),_CmmOcgPtpPmCmmOcgOptAve_Type())
cmmOcgPtpPmCmmOcgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOptAve.setStatus(_A)
_CmmOcgPtpPmCmmOcgOprMin_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOprMin_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOprMin=_CmmOcgPtpPmCmmOcgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,7),_CmmOcgPtpPmCmmOcgOprMin_Type())
cmmOcgPtpPmCmmOcgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOprMin.setStatus(_A)
_CmmOcgPtpPmCmmOcgOprMax_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOprMax_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOprMax=_CmmOcgPtpPmCmmOcgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,8),_CmmOcgPtpPmCmmOcgOprMax_Type())
cmmOcgPtpPmCmmOcgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOprMax.setStatus(_A)
_CmmOcgPtpPmCmmOcgOprAve_Type=FloatHundredths
_CmmOcgPtpPmCmmOcgOprAve_Object=MibTableColumn
cmmOcgPtpPmCmmOcgOprAve=_CmmOcgPtpPmCmmOcgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,9),_CmmOcgPtpPmCmmOcgOprAve_Type())
cmmOcgPtpPmCmmOcgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmOcgOprAve.setStatus(_A)
_CmmOcgPtpPmCmmEdfaLbcTxMin_Type=FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxMin_Object=MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxMin=_CmmOcgPtpPmCmmEdfaLbcTxMin_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,10),_CmmOcgPtpPmCmmEdfaLbcTxMin_Type())
cmmOcgPtpPmCmmEdfaLbcTxMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmEdfaLbcTxMin.setStatus(_A)
_CmmOcgPtpPmCmmEdfaLbcTxMax_Type=FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxMax_Object=MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxMax=_CmmOcgPtpPmCmmEdfaLbcTxMax_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,11),_CmmOcgPtpPmCmmEdfaLbcTxMax_Type())
cmmOcgPtpPmCmmEdfaLbcTxMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmEdfaLbcTxMax.setStatus(_A)
_CmmOcgPtpPmCmmEdfaLbcTxAve_Type=FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxAve_Object=MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxAve=_CmmOcgPtpPmCmmEdfaLbcTxAve_Object((1,3,6,1,4,1,21296,2,2,2,3,25,2,1,12),_CmmOcgPtpPmCmmEdfaLbcTxAve_Type())
cmmOcgPtpPmCmmEdfaLbcTxAve.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOcgPtpPmCmmEdfaLbcTxAve.setStatus(_A)
_CmmOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
cmmOcgPtpPmConformance=_CmmOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,25,3))
_CmmOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
cmmOcgPtpPmCompliances=_CmmOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,25,3,1))
_CmmOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
cmmOcgPtpPmGroups=_CmmOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,25,3,2))
cmmOcgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,25,3,2,1))
cmmOcgPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cmmOcgPtpPmGroup.setStatus(_A)
cmmOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,25,3,2,2))
cmmOcgPtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cmmOcgPtpPmRealGroup.setStatus(_A)
cmmOcgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,25,3,1,1))
cmmOcgPtpPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:cmmOcgPtpPmCompliance.setStatus(_A)
cmmOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,25,3,1,2))
cmmOcgPtpPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:cmmOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmOcgPtpPmMIB':cmmOcgPtpPmMIB,'cmmOcgPtpPmRealTable':cmmOcgPtpPmRealTable,'cmmOcgPtpPmRealEntry':cmmOcgPtpPmRealEntry,_T:cmmOcgPtpPmRealCmmOcgOpt,_U:cmmOcgPtpPmRealCmmOcgOpr,_V:cmmOcgPtpPmRealCmmEdfaLbcTx,'cmmOcgPtpPmTable':cmmOcgPtpPmTable,'cmmOcgPtpPmEntry':cmmOcgPtpPmEntry,_H:cmmOcgPtpPmTimestamp,_G:cmmOcgPtpPmSampleDuration,_J:cmmOcgPtpPmValidity,_K:cmmOcgPtpPmCmmOcgOptMin,_L:cmmOcgPtpPmCmmOcgOptMax,_M:cmmOcgPtpPmCmmOcgOptAve,_N:cmmOcgPtpPmCmmOcgOprMin,_O:cmmOcgPtpPmCmmOcgOprMax,_P:cmmOcgPtpPmCmmOcgOprAve,_Q:cmmOcgPtpPmCmmEdfaLbcTxMin,_R:cmmOcgPtpPmCmmEdfaLbcTxMax,_S:cmmOcgPtpPmCmmEdfaLbcTxAve,'cmmOcgPtpPmConformance':cmmOcgPtpPmConformance,'cmmOcgPtpPmCompliances':cmmOcgPtpPmCompliances,'cmmOcgPtpPmCompliance':cmmOcgPtpPmCompliance,'cmmOcgPtpPmRealCompliance':cmmOcgPtpPmRealCompliance,'cmmOcgPtpPmGroups':cmmOcgPtpPmGroups,_W:cmmOcgPtpPmGroup,_X:cmmOcgPtpPmRealGroup})