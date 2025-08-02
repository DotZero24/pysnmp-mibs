_T='osctCtpPmRealGroup'
_S='osctCtpPmGroup'
_R='osctCtpPmRealOscTOPR'
_Q='osctCtpPmRealOscTOPT'
_P='osctCtpPmOscTOPRAve'
_O='osctCtpPmOscTOPRMax'
_N='osctCtpPmOscTOPRMin'
_M='osctCtpPmOscTOPTAve'
_L='osctCtpPmOscTOPTMax'
_K='osctCtpPmOscTOPTMin'
_J='osctCtpPmValidity'
_I='not-accessible'
_H='osctCtpPmTimestamp'
_G='osctCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OSCTCTP-MIB'
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
osctCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,11))
if mibBuilder.loadTexts:osctCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_OsctCtpPmRealTable_Object=MibTable
osctCtpPmRealTable=_OsctCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,11,1))
if mibBuilder.loadTexts:osctCtpPmRealTable.setStatus(_A)
_OsctCtpPmRealEntry_Object=MibTableRow
osctCtpPmRealEntry=_OsctCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,11,1,1))
osctCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:osctCtpPmRealEntry.setStatus(_A)
_OsctCtpPmRealOscTOPT_Type=FloatHundredths
_OsctCtpPmRealOscTOPT_Object=MibTableColumn
osctCtpPmRealOscTOPT=_OsctCtpPmRealOscTOPT_Object((1,3,6,1,4,1,21296,2,2,2,3,11,1,1,1),_OsctCtpPmRealOscTOPT_Type())
osctCtpPmRealOscTOPT.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmRealOscTOPT.setStatus(_A)
_OsctCtpPmRealOscTOPR_Type=FloatHundredths
_OsctCtpPmRealOscTOPR_Object=MibTableColumn
osctCtpPmRealOscTOPR=_OsctCtpPmRealOscTOPR_Object((1,3,6,1,4,1,21296,2,2,2,3,11,1,1,2),_OsctCtpPmRealOscTOPR_Type())
osctCtpPmRealOscTOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmRealOscTOPR.setStatus(_A)
_OsctCtpPmTable_Object=MibTable
osctCtpPmTable=_OsctCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2))
if mibBuilder.loadTexts:osctCtpPmTable.setStatus(_A)
_OsctCtpPmEntry_Object=MibTableRow
osctCtpPmEntry=_OsctCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1))
osctCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:osctCtpPmEntry.setStatus(_A)
class _OsctCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OsctCtpPmTimestamp_Type.__name__=_F
_OsctCtpPmTimestamp_Object=MibTableColumn
osctCtpPmTimestamp=_OsctCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,1),_OsctCtpPmTimestamp_Type())
osctCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:osctCtpPmTimestamp.setStatus(_A)
class _OsctCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OsctCtpPmSampleDuration_Type.__name__=_F
_OsctCtpPmSampleDuration_Object=MibTableColumn
osctCtpPmSampleDuration=_OsctCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,2),_OsctCtpPmSampleDuration_Type())
osctCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:osctCtpPmSampleDuration.setStatus(_A)
_OsctCtpPmValidity_Type=TruthValue
_OsctCtpPmValidity_Object=MibTableColumn
osctCtpPmValidity=_OsctCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,3),_OsctCtpPmValidity_Type())
osctCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmValidity.setStatus(_A)
_OsctCtpPmOscTOPTMin_Type=FloatHundredths
_OsctCtpPmOscTOPTMin_Object=MibTableColumn
osctCtpPmOscTOPTMin=_OsctCtpPmOscTOPTMin_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,4),_OsctCtpPmOscTOPTMin_Type())
osctCtpPmOscTOPTMin.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPTMin.setStatus(_A)
_OsctCtpPmOscTOPTMax_Type=FloatHundredths
_OsctCtpPmOscTOPTMax_Object=MibTableColumn
osctCtpPmOscTOPTMax=_OsctCtpPmOscTOPTMax_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,5),_OsctCtpPmOscTOPTMax_Type())
osctCtpPmOscTOPTMax.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPTMax.setStatus(_A)
_OsctCtpPmOscTOPTAve_Type=FloatHundredths
_OsctCtpPmOscTOPTAve_Object=MibTableColumn
osctCtpPmOscTOPTAve=_OsctCtpPmOscTOPTAve_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,6),_OsctCtpPmOscTOPTAve_Type())
osctCtpPmOscTOPTAve.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPTAve.setStatus(_A)
_OsctCtpPmOscTOPRMin_Type=FloatHundredths
_OsctCtpPmOscTOPRMin_Object=MibTableColumn
osctCtpPmOscTOPRMin=_OsctCtpPmOscTOPRMin_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,7),_OsctCtpPmOscTOPRMin_Type())
osctCtpPmOscTOPRMin.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPRMin.setStatus(_A)
_OsctCtpPmOscTOPRMax_Type=FloatHundredths
_OsctCtpPmOscTOPRMax_Object=MibTableColumn
osctCtpPmOscTOPRMax=_OsctCtpPmOscTOPRMax_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,8),_OsctCtpPmOscTOPRMax_Type())
osctCtpPmOscTOPRMax.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPRMax.setStatus(_A)
_OsctCtpPmOscTOPRAve_Type=FloatHundredths
_OsctCtpPmOscTOPRAve_Object=MibTableColumn
osctCtpPmOscTOPRAve=_OsctCtpPmOscTOPRAve_Object((1,3,6,1,4,1,21296,2,2,2,3,11,2,1,9),_OsctCtpPmOscTOPRAve_Type())
osctCtpPmOscTOPRAve.setMaxAccess(_C)
if mibBuilder.loadTexts:osctCtpPmOscTOPRAve.setStatus(_A)
_OsctCtpPmConformance_ObjectIdentity=ObjectIdentity
osctCtpPmConformance=_OsctCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,11,3))
_OsctCtpPmCompliances_ObjectIdentity=ObjectIdentity
osctCtpPmCompliances=_OsctCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,11,3,1))
_OsctCtpPmGroups_ObjectIdentity=ObjectIdentity
osctCtpPmGroups=_OsctCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,11,3,2))
osctCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,11,3,2,1))
osctCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:osctCtpPmGroup.setStatus(_A)
osctCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,11,3,2,2))
osctCtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:osctCtpPmRealGroup.setStatus(_A)
osctCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,11,3,1,1))
osctCtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:osctCtpPmCompliance.setStatus(_A)
osctCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,11,3,1,2))
osctCtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:osctCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osctCtpPmMIB':osctCtpPmMIB,'osctCtpPmRealTable':osctCtpPmRealTable,'osctCtpPmRealEntry':osctCtpPmRealEntry,_Q:osctCtpPmRealOscTOPT,_R:osctCtpPmRealOscTOPR,'osctCtpPmTable':osctCtpPmTable,'osctCtpPmEntry':osctCtpPmEntry,_H:osctCtpPmTimestamp,_G:osctCtpPmSampleDuration,_J:osctCtpPmValidity,_K:osctCtpPmOscTOPTMin,_L:osctCtpPmOscTOPTMax,_M:osctCtpPmOscTOPTAve,_N:osctCtpPmOscTOPRMin,_O:osctCtpPmOscTOPRMax,_P:osctCtpPmOscTOPRAve,'osctCtpPmConformance':osctCtpPmConformance,'osctCtpPmCompliances':osctCtpPmCompliances,'osctCtpPmCompliance':osctCtpPmCompliance,'osctCtpPmRealCompliance':osctCtpPmRealCompliance,'osctCtpPmGroups':osctCtpPmGroups,_S:osctCtpPmGroup,_T:osctCtpPmRealGroup})