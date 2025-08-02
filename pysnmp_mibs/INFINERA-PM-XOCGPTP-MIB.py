_l='xOcgPtpPmRealGroup'
_k='xOcgPtpPmGroup'
_j='xOcgPtpPmRealRxEdfaLbc'
_i='xOcgPtpPmRealRxEdfaOpt'
_h='xOcgPtpPmRealRxEdfaOpr'
_g='xOcgPtpPmRealTxEdfaLbc'
_f='xOcgPtpPmRealTxEdfaOpt'
_e='xOcgPtpPmRealTxEdfaOpr'
_d='xOcgPtpPmRealDlmOcgOpr'
_c='xOcgPtpPmRealDlmOcgOpt'
_b='xOcgPtpPmValidity'
_a='xOcgPtpPmRxEdfaLbcAve'
_Z='xOcgPtpPmRxEdfaLbcMax'
_Y='xOcgPtpPmRxEdfaLbcMin'
_X='xOcgPtpPmRxEdfaOptAve'
_W='xOcgPtpPmRxEdfaOptMax'
_V='xOcgPtpPmRxEdfaOptMin'
_U='xOcgPtpPmRxEdfaOprAve'
_T='xOcgPtpPmRxEdfaOprMax'
_S='xOcgPtpPmRxEdfaOprMin'
_R='xOcgPtpPmTxEdfaLbcAve'
_Q='xOcgPtpPmTxEdfaLbcMax'
_P='xOcgPtpPmTxEdfaLbcMin'
_O='xOcgPtpPmTxEdfaOptAve'
_N='xOcgPtpPmTxEdfaOptMax'
_M='xOcgPtpPmTxEdfaOptMin'
_L='xOcgPtpPmTxEdfaOprAve'
_K='xOcgPtpPmTxEdfaOprMax'
_J='xOcgPtpPmTxEdfaOprMin'
_I='not-accessible'
_H='xOcgPtpPmTimestamp'
_G='xOcgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-XOCGPTP-MIB'
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
xOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,42))
if mibBuilder.loadTexts:xOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_XOcgPtpPmRealTable_Object=MibTable
xOcgPtpPmRealTable=_XOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1))
if mibBuilder.loadTexts:xOcgPtpPmRealTable.setStatus(_A)
_XOcgPtpPmRealEntry_Object=MibTableRow
xOcgPtpPmRealEntry=_XOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1))
xOcgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:xOcgPtpPmRealEntry.setStatus(_A)
_XOcgPtpPmRealDlmOcgOpt_Type=FloatHundredths
_XOcgPtpPmRealDlmOcgOpt_Object=MibTableColumn
xOcgPtpPmRealDlmOcgOpt=_XOcgPtpPmRealDlmOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,1),_XOcgPtpPmRealDlmOcgOpt_Type())
xOcgPtpPmRealDlmOcgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealDlmOcgOpt.setStatus(_A)
_XOcgPtpPmRealDlmOcgOpr_Type=FloatHundredths
_XOcgPtpPmRealDlmOcgOpr_Object=MibTableColumn
xOcgPtpPmRealDlmOcgOpr=_XOcgPtpPmRealDlmOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,2),_XOcgPtpPmRealDlmOcgOpr_Type())
xOcgPtpPmRealDlmOcgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealDlmOcgOpr.setStatus(_A)
_XOcgPtpPmRealTxEdfaOpr_Type=FloatHundredths
_XOcgPtpPmRealTxEdfaOpr_Object=MibTableColumn
xOcgPtpPmRealTxEdfaOpr=_XOcgPtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,3),_XOcgPtpPmRealTxEdfaOpr_Type())
xOcgPtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealTxEdfaOpr.setStatus(_A)
_XOcgPtpPmRealTxEdfaOpt_Type=FloatHundredths
_XOcgPtpPmRealTxEdfaOpt_Object=MibTableColumn
xOcgPtpPmRealTxEdfaOpt=_XOcgPtpPmRealTxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,4),_XOcgPtpPmRealTxEdfaOpt_Type())
xOcgPtpPmRealTxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealTxEdfaOpt.setStatus(_A)
_XOcgPtpPmRealTxEdfaLbc_Type=FloatHundredths
_XOcgPtpPmRealTxEdfaLbc_Object=MibTableColumn
xOcgPtpPmRealTxEdfaLbc=_XOcgPtpPmRealTxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,5),_XOcgPtpPmRealTxEdfaLbc_Type())
xOcgPtpPmRealTxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealTxEdfaLbc.setStatus(_A)
_XOcgPtpPmRealRxEdfaOpr_Type=FloatHundredths
_XOcgPtpPmRealRxEdfaOpr_Object=MibTableColumn
xOcgPtpPmRealRxEdfaOpr=_XOcgPtpPmRealRxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,6),_XOcgPtpPmRealRxEdfaOpr_Type())
xOcgPtpPmRealRxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealRxEdfaOpr.setStatus(_A)
_XOcgPtpPmRealRxEdfaOpt_Type=FloatHundredths
_XOcgPtpPmRealRxEdfaOpt_Object=MibTableColumn
xOcgPtpPmRealRxEdfaOpt=_XOcgPtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,7),_XOcgPtpPmRealRxEdfaOpt_Type())
xOcgPtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealRxEdfaOpt.setStatus(_A)
_XOcgPtpPmRealRxEdfaLbc_Type=FloatHundredths
_XOcgPtpPmRealRxEdfaLbc_Object=MibTableColumn
xOcgPtpPmRealRxEdfaLbc=_XOcgPtpPmRealRxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,42,1,1,8),_XOcgPtpPmRealRxEdfaLbc_Type())
xOcgPtpPmRealRxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRealRxEdfaLbc.setStatus(_A)
_XOcgPtpPmTable_Object=MibTable
xOcgPtpPmTable=_XOcgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2))
if mibBuilder.loadTexts:xOcgPtpPmTable.setStatus(_A)
_XOcgPtpPmEntry_Object=MibTableRow
xOcgPtpPmEntry=_XOcgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1))
xOcgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:xOcgPtpPmEntry.setStatus(_A)
class _XOcgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_XOcgPtpPmTimestamp_Type.__name__=_F
_XOcgPtpPmTimestamp_Object=MibTableColumn
xOcgPtpPmTimestamp=_XOcgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,1),_XOcgPtpPmTimestamp_Type())
xOcgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:xOcgPtpPmTimestamp.setStatus(_A)
class _XOcgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_XOcgPtpPmSampleDuration_Type.__name__=_F
_XOcgPtpPmSampleDuration_Object=MibTableColumn
xOcgPtpPmSampleDuration=_XOcgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,2),_XOcgPtpPmSampleDuration_Type())
xOcgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:xOcgPtpPmSampleDuration.setStatus(_A)
_XOcgPtpPmTxEdfaOprMin_Type=FloatHundredths
_XOcgPtpPmTxEdfaOprMin_Object=MibTableColumn
xOcgPtpPmTxEdfaOprMin=_XOcgPtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,3),_XOcgPtpPmTxEdfaOprMin_Type())
xOcgPtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOprMin.setStatus(_A)
_XOcgPtpPmTxEdfaOprMax_Type=FloatHundredths
_XOcgPtpPmTxEdfaOprMax_Object=MibTableColumn
xOcgPtpPmTxEdfaOprMax=_XOcgPtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,4),_XOcgPtpPmTxEdfaOprMax_Type())
xOcgPtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOprMax.setStatus(_A)
_XOcgPtpPmTxEdfaOprAve_Type=FloatHundredths
_XOcgPtpPmTxEdfaOprAve_Object=MibTableColumn
xOcgPtpPmTxEdfaOprAve=_XOcgPtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,5),_XOcgPtpPmTxEdfaOprAve_Type())
xOcgPtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOprAve.setStatus(_A)
_XOcgPtpPmTxEdfaOptMin_Type=FloatHundredths
_XOcgPtpPmTxEdfaOptMin_Object=MibTableColumn
xOcgPtpPmTxEdfaOptMin=_XOcgPtpPmTxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,6),_XOcgPtpPmTxEdfaOptMin_Type())
xOcgPtpPmTxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOptMin.setStatus(_A)
_XOcgPtpPmTxEdfaOptMax_Type=FloatHundredths
_XOcgPtpPmTxEdfaOptMax_Object=MibTableColumn
xOcgPtpPmTxEdfaOptMax=_XOcgPtpPmTxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,7),_XOcgPtpPmTxEdfaOptMax_Type())
xOcgPtpPmTxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOptMax.setStatus(_A)
_XOcgPtpPmTxEdfaOptAve_Type=FloatHundredths
_XOcgPtpPmTxEdfaOptAve_Object=MibTableColumn
xOcgPtpPmTxEdfaOptAve=_XOcgPtpPmTxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,8),_XOcgPtpPmTxEdfaOptAve_Type())
xOcgPtpPmTxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaOptAve.setStatus(_A)
_XOcgPtpPmTxEdfaLbcMin_Type=FloatHundredths
_XOcgPtpPmTxEdfaLbcMin_Object=MibTableColumn
xOcgPtpPmTxEdfaLbcMin=_XOcgPtpPmTxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,9),_XOcgPtpPmTxEdfaLbcMin_Type())
xOcgPtpPmTxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaLbcMin.setStatus(_A)
_XOcgPtpPmTxEdfaLbcMax_Type=FloatHundredths
_XOcgPtpPmTxEdfaLbcMax_Object=MibTableColumn
xOcgPtpPmTxEdfaLbcMax=_XOcgPtpPmTxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,10),_XOcgPtpPmTxEdfaLbcMax_Type())
xOcgPtpPmTxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaLbcMax.setStatus(_A)
_XOcgPtpPmTxEdfaLbcAve_Type=FloatHundredths
_XOcgPtpPmTxEdfaLbcAve_Object=MibTableColumn
xOcgPtpPmTxEdfaLbcAve=_XOcgPtpPmTxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,11),_XOcgPtpPmTxEdfaLbcAve_Type())
xOcgPtpPmTxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmTxEdfaLbcAve.setStatus(_A)
_XOcgPtpPmRxEdfaOprMin_Type=FloatHundredths
_XOcgPtpPmRxEdfaOprMin_Object=MibTableColumn
xOcgPtpPmRxEdfaOprMin=_XOcgPtpPmRxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,12),_XOcgPtpPmRxEdfaOprMin_Type())
xOcgPtpPmRxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOprMin.setStatus(_A)
_XOcgPtpPmRxEdfaOprMax_Type=FloatHundredths
_XOcgPtpPmRxEdfaOprMax_Object=MibTableColumn
xOcgPtpPmRxEdfaOprMax=_XOcgPtpPmRxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,13),_XOcgPtpPmRxEdfaOprMax_Type())
xOcgPtpPmRxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOprMax.setStatus(_A)
_XOcgPtpPmRxEdfaOprAve_Type=FloatHundredths
_XOcgPtpPmRxEdfaOprAve_Object=MibTableColumn
xOcgPtpPmRxEdfaOprAve=_XOcgPtpPmRxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,14),_XOcgPtpPmRxEdfaOprAve_Type())
xOcgPtpPmRxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOprAve.setStatus(_A)
_XOcgPtpPmRxEdfaOptMin_Type=FloatHundredths
_XOcgPtpPmRxEdfaOptMin_Object=MibTableColumn
xOcgPtpPmRxEdfaOptMin=_XOcgPtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,15),_XOcgPtpPmRxEdfaOptMin_Type())
xOcgPtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOptMin.setStatus(_A)
_XOcgPtpPmRxEdfaOptMax_Type=FloatHundredths
_XOcgPtpPmRxEdfaOptMax_Object=MibTableColumn
xOcgPtpPmRxEdfaOptMax=_XOcgPtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,16),_XOcgPtpPmRxEdfaOptMax_Type())
xOcgPtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOptMax.setStatus(_A)
_XOcgPtpPmRxEdfaOptAve_Type=FloatHundredths
_XOcgPtpPmRxEdfaOptAve_Object=MibTableColumn
xOcgPtpPmRxEdfaOptAve=_XOcgPtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,17),_XOcgPtpPmRxEdfaOptAve_Type())
xOcgPtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaOptAve.setStatus(_A)
_XOcgPtpPmRxEdfaLbcMin_Type=FloatHundredths
_XOcgPtpPmRxEdfaLbcMin_Object=MibTableColumn
xOcgPtpPmRxEdfaLbcMin=_XOcgPtpPmRxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,18),_XOcgPtpPmRxEdfaLbcMin_Type())
xOcgPtpPmRxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaLbcMin.setStatus(_A)
_XOcgPtpPmRxEdfaLbcMax_Type=FloatHundredths
_XOcgPtpPmRxEdfaLbcMax_Object=MibTableColumn
xOcgPtpPmRxEdfaLbcMax=_XOcgPtpPmRxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,19),_XOcgPtpPmRxEdfaLbcMax_Type())
xOcgPtpPmRxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaLbcMax.setStatus(_A)
_XOcgPtpPmRxEdfaLbcAve_Type=FloatHundredths
_XOcgPtpPmRxEdfaLbcAve_Object=MibTableColumn
xOcgPtpPmRxEdfaLbcAve=_XOcgPtpPmRxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,20),_XOcgPtpPmRxEdfaLbcAve_Type())
xOcgPtpPmRxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmRxEdfaLbcAve.setStatus(_A)
_XOcgPtpPmValidity_Type=TruthValue
_XOcgPtpPmValidity_Object=MibTableColumn
xOcgPtpPmValidity=_XOcgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,42,2,1,21),_XOcgPtpPmValidity_Type())
xOcgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpPmValidity.setStatus(_A)
_XOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
xOcgPtpPmConformance=_XOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,42,3))
_XOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
xOcgPtpPmCompliances=_XOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,42,3,1))
_XOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
xOcgPtpPmGroups=_XOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,42,3,2))
xOcgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,42,3,2,1))
xOcgPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:xOcgPtpPmGroup.setStatus(_A)
xOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,42,3,2,2))
xOcgPtpPmRealGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:xOcgPtpPmRealGroup.setStatus(_A)
xOcgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,42,3,1,1))
xOcgPtpPmCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:xOcgPtpPmCompliance.setStatus(_A)
xOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,42,3,1,2))
xOcgPtpPmRealCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:xOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xOcgPtpPmMIB':xOcgPtpPmMIB,'xOcgPtpPmRealTable':xOcgPtpPmRealTable,'xOcgPtpPmRealEntry':xOcgPtpPmRealEntry,_c:xOcgPtpPmRealDlmOcgOpt,_d:xOcgPtpPmRealDlmOcgOpr,_e:xOcgPtpPmRealTxEdfaOpr,_f:xOcgPtpPmRealTxEdfaOpt,_g:xOcgPtpPmRealTxEdfaLbc,_h:xOcgPtpPmRealRxEdfaOpr,_i:xOcgPtpPmRealRxEdfaOpt,_j:xOcgPtpPmRealRxEdfaLbc,'xOcgPtpPmTable':xOcgPtpPmTable,'xOcgPtpPmEntry':xOcgPtpPmEntry,_H:xOcgPtpPmTimestamp,_G:xOcgPtpPmSampleDuration,_J:xOcgPtpPmTxEdfaOprMin,_K:xOcgPtpPmTxEdfaOprMax,_L:xOcgPtpPmTxEdfaOprAve,_M:xOcgPtpPmTxEdfaOptMin,_N:xOcgPtpPmTxEdfaOptMax,_O:xOcgPtpPmTxEdfaOptAve,_P:xOcgPtpPmTxEdfaLbcMin,_Q:xOcgPtpPmTxEdfaLbcMax,_R:xOcgPtpPmTxEdfaLbcAve,_S:xOcgPtpPmRxEdfaOprMin,_T:xOcgPtpPmRxEdfaOprMax,_U:xOcgPtpPmRxEdfaOprAve,_V:xOcgPtpPmRxEdfaOptMin,_W:xOcgPtpPmRxEdfaOptMax,_X:xOcgPtpPmRxEdfaOptAve,_Y:xOcgPtpPmRxEdfaLbcMin,_Z:xOcgPtpPmRxEdfaLbcMax,_a:xOcgPtpPmRxEdfaLbcAve,_b:xOcgPtpPmValidity,'xOcgPtpPmConformance':xOcgPtpPmConformance,'xOcgPtpPmCompliances':xOcgPtpPmCompliances,'xOcgPtpPmCompliance':xOcgPtpPmCompliance,'xOcgPtpPmRealCompliance':xOcgPtpPmRealCompliance,'xOcgPtpPmGroups':xOcgPtpPmGroups,_k:xOcgPtpPmGroup,_l:xOcgPtpPmRealGroup})