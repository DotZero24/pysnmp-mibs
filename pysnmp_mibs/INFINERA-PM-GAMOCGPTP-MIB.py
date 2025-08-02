_X='gamOcgPtpPmRealGroup'
_W='gamOcgPtpPmGroup'
_V='gamOcgPtpPmRealGamOcgLbc'
_U='gamOcgPtpPmRealGamOcgOpr'
_T='gamOcgPtpPmRealGamOcgOpt'
_S='gamOcgPtpPmGamOcgLbcAve'
_R='gamOcgPtpPmGamOcgLbcMax'
_Q='gamOcgPtpPmGamOcgLbcMin'
_P='gamOcgPtpPmGamOcgOprAve'
_O='gamOcgPtpPmGamOcgOprMax'
_N='gamOcgPtpPmGamOcgOprMin'
_M='gamOcgPtpPmGamOcgOptAve'
_L='gamOcgPtpPmGamOcgOptMax'
_K='gamOcgPtpPmGamOcgOptMin'
_J='gamOcgPtpPmValidity'
_I='not-accessible'
_H='gamOcgPtpPmTimestamp'
_G='gamOcgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-GAMOCGPTP-MIB'
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
gamOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,7))
if mibBuilder.loadTexts:gamOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_GamOcgPtpPmRealTable_Object=MibTable
gamOcgPtpPmRealTable=_GamOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,7,1))
if mibBuilder.loadTexts:gamOcgPtpPmRealTable.setStatus(_A)
_GamOcgPtpPmRealEntry_Object=MibTableRow
gamOcgPtpPmRealEntry=_GamOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,7,1,1))
gamOcgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:gamOcgPtpPmRealEntry.setStatus(_A)
_GamOcgPtpPmRealGamOcgOpt_Type=FloatHundredths
_GamOcgPtpPmRealGamOcgOpt_Object=MibTableColumn
gamOcgPtpPmRealGamOcgOpt=_GamOcgPtpPmRealGamOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,7,1,1,1),_GamOcgPtpPmRealGamOcgOpt_Type())
gamOcgPtpPmRealGamOcgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmRealGamOcgOpt.setStatus(_A)
_GamOcgPtpPmRealGamOcgOpr_Type=FloatHundredths
_GamOcgPtpPmRealGamOcgOpr_Object=MibTableColumn
gamOcgPtpPmRealGamOcgOpr=_GamOcgPtpPmRealGamOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,7,1,1,2),_GamOcgPtpPmRealGamOcgOpr_Type())
gamOcgPtpPmRealGamOcgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmRealGamOcgOpr.setStatus(_A)
_GamOcgPtpPmRealGamOcgLbc_Type=FloatHundredths
_GamOcgPtpPmRealGamOcgLbc_Object=MibTableColumn
gamOcgPtpPmRealGamOcgLbc=_GamOcgPtpPmRealGamOcgLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,7,1,1,3),_GamOcgPtpPmRealGamOcgLbc_Type())
gamOcgPtpPmRealGamOcgLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmRealGamOcgLbc.setStatus(_A)
_GamOcgPtpPmTable_Object=MibTable
gamOcgPtpPmTable=_GamOcgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2))
if mibBuilder.loadTexts:gamOcgPtpPmTable.setStatus(_A)
_GamOcgPtpPmEntry_Object=MibTableRow
gamOcgPtpPmEntry=_GamOcgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1))
gamOcgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:gamOcgPtpPmEntry.setStatus(_A)
class _GamOcgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_GamOcgPtpPmTimestamp_Type.__name__=_F
_GamOcgPtpPmTimestamp_Object=MibTableColumn
gamOcgPtpPmTimestamp=_GamOcgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,1),_GamOcgPtpPmTimestamp_Type())
gamOcgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:gamOcgPtpPmTimestamp.setStatus(_A)
class _GamOcgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_GamOcgPtpPmSampleDuration_Type.__name__=_F
_GamOcgPtpPmSampleDuration_Object=MibTableColumn
gamOcgPtpPmSampleDuration=_GamOcgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,2),_GamOcgPtpPmSampleDuration_Type())
gamOcgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:gamOcgPtpPmSampleDuration.setStatus(_A)
_GamOcgPtpPmValidity_Type=TruthValue
_GamOcgPtpPmValidity_Object=MibTableColumn
gamOcgPtpPmValidity=_GamOcgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,3),_GamOcgPtpPmValidity_Type())
gamOcgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmValidity.setStatus(_A)
_GamOcgPtpPmGamOcgOptMin_Type=FloatHundredths
_GamOcgPtpPmGamOcgOptMin_Object=MibTableColumn
gamOcgPtpPmGamOcgOptMin=_GamOcgPtpPmGamOcgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,4),_GamOcgPtpPmGamOcgOptMin_Type())
gamOcgPtpPmGamOcgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOptMin.setStatus(_A)
_GamOcgPtpPmGamOcgOptMax_Type=FloatHundredths
_GamOcgPtpPmGamOcgOptMax_Object=MibTableColumn
gamOcgPtpPmGamOcgOptMax=_GamOcgPtpPmGamOcgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,5),_GamOcgPtpPmGamOcgOptMax_Type())
gamOcgPtpPmGamOcgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOptMax.setStatus(_A)
_GamOcgPtpPmGamOcgOptAve_Type=FloatHundredths
_GamOcgPtpPmGamOcgOptAve_Object=MibTableColumn
gamOcgPtpPmGamOcgOptAve=_GamOcgPtpPmGamOcgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,6),_GamOcgPtpPmGamOcgOptAve_Type())
gamOcgPtpPmGamOcgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOptAve.setStatus(_A)
_GamOcgPtpPmGamOcgOprMin_Type=FloatHundredths
_GamOcgPtpPmGamOcgOprMin_Object=MibTableColumn
gamOcgPtpPmGamOcgOprMin=_GamOcgPtpPmGamOcgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,7),_GamOcgPtpPmGamOcgOprMin_Type())
gamOcgPtpPmGamOcgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOprMin.setStatus(_A)
_GamOcgPtpPmGamOcgOprMax_Type=FloatHundredths
_GamOcgPtpPmGamOcgOprMax_Object=MibTableColumn
gamOcgPtpPmGamOcgOprMax=_GamOcgPtpPmGamOcgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,8),_GamOcgPtpPmGamOcgOprMax_Type())
gamOcgPtpPmGamOcgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOprMax.setStatus(_A)
_GamOcgPtpPmGamOcgOprAve_Type=FloatHundredths
_GamOcgPtpPmGamOcgOprAve_Object=MibTableColumn
gamOcgPtpPmGamOcgOprAve=_GamOcgPtpPmGamOcgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,9),_GamOcgPtpPmGamOcgOprAve_Type())
gamOcgPtpPmGamOcgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgOprAve.setStatus(_A)
_GamOcgPtpPmGamOcgLbcMin_Type=FloatHundredths
_GamOcgPtpPmGamOcgLbcMin_Object=MibTableColumn
gamOcgPtpPmGamOcgLbcMin=_GamOcgPtpPmGamOcgLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,10),_GamOcgPtpPmGamOcgLbcMin_Type())
gamOcgPtpPmGamOcgLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgLbcMin.setStatus(_A)
_GamOcgPtpPmGamOcgLbcMax_Type=FloatHundredths
_GamOcgPtpPmGamOcgLbcMax_Object=MibTableColumn
gamOcgPtpPmGamOcgLbcMax=_GamOcgPtpPmGamOcgLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,11),_GamOcgPtpPmGamOcgLbcMax_Type())
gamOcgPtpPmGamOcgLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgLbcMax.setStatus(_A)
_GamOcgPtpPmGamOcgLbcAve_Type=FloatHundredths
_GamOcgPtpPmGamOcgLbcAve_Object=MibTableColumn
gamOcgPtpPmGamOcgLbcAve=_GamOcgPtpPmGamOcgLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,7,2,1,12),_GamOcgPtpPmGamOcgLbcAve_Type())
gamOcgPtpPmGamOcgLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:gamOcgPtpPmGamOcgLbcAve.setStatus(_A)
_GamOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
gamOcgPtpPmConformance=_GamOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,7,3))
_GamOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
gamOcgPtpPmCompliances=_GamOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,7,3,1))
_GamOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
gamOcgPtpPmGroups=_GamOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,7,3,2))
gamOcgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,7,3,2,1))
gamOcgPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:gamOcgPtpPmGroup.setStatus(_A)
gamOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,7,3,2,2))
gamOcgPtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:gamOcgPtpPmRealGroup.setStatus(_A)
gamOcgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,7,3,1,1))
gamOcgPtpPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:gamOcgPtpPmCompliance.setStatus(_A)
gamOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,7,3,1,2))
gamOcgPtpPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:gamOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gamOcgPtpPmMIB':gamOcgPtpPmMIB,'gamOcgPtpPmRealTable':gamOcgPtpPmRealTable,'gamOcgPtpPmRealEntry':gamOcgPtpPmRealEntry,_T:gamOcgPtpPmRealGamOcgOpt,_U:gamOcgPtpPmRealGamOcgOpr,_V:gamOcgPtpPmRealGamOcgLbc,'gamOcgPtpPmTable':gamOcgPtpPmTable,'gamOcgPtpPmEntry':gamOcgPtpPmEntry,_H:gamOcgPtpPmTimestamp,_G:gamOcgPtpPmSampleDuration,_J:gamOcgPtpPmValidity,_K:gamOcgPtpPmGamOcgOptMin,_L:gamOcgPtpPmGamOcgOptMax,_M:gamOcgPtpPmGamOcgOptAve,_N:gamOcgPtpPmGamOcgOprMin,_O:gamOcgPtpPmGamOcgOprMax,_P:gamOcgPtpPmGamOcgOprAve,_Q:gamOcgPtpPmGamOcgLbcMin,_R:gamOcgPtpPmGamOcgLbcMax,_S:gamOcgPtpPmGamOcgLbcAve,'gamOcgPtpPmConformance':gamOcgPtpPmConformance,'gamOcgPtpPmCompliances':gamOcgPtpPmCompliances,'gamOcgPtpPmCompliance':gamOcgPtpPmCompliance,'gamOcgPtpPmRealCompliance':gamOcgPtpPmRealCompliance,'gamOcgPtpPmGroups':gamOcgPtpPmGroups,_W:gamOcgPtpPmGroup,_X:gamOcgPtpPmRealGroup})