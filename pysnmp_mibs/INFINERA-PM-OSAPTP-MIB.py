_Q='osaPtpPmRealGroup'
_P='osaPtpPmGroup'
_O='osaOprOsaTapRatio'
_N='osaPtpPmRealOpr'
_M='osaPtpPmOprAve'
_L='osaPtpPmOprMax'
_K='osaPtpPmOprMin'
_J='osaPtpPmValidity'
_I='not-accessible'
_H='osaPtpPmTimestamp'
_G='osaPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OSAPTP-MIB'
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
osaPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,19))
if mibBuilder.loadTexts:osaPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_OsaPtpPmRealTable_Object=MibTable
osaPtpPmRealTable=_OsaPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,19,1))
if mibBuilder.loadTexts:osaPtpPmRealTable.setStatus(_A)
_OsaPtpPmRealEntry_Object=MibTableRow
osaPtpPmRealEntry=_OsaPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,19,1,1))
osaPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:osaPtpPmRealEntry.setStatus(_A)
_OsaPtpPmRealOpr_Type=FloatHundredths
_OsaPtpPmRealOpr_Object=MibTableColumn
osaPtpPmRealOpr=_OsaPtpPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,19,1,1,1),_OsaPtpPmRealOpr_Type())
osaPtpPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:osaPtpPmRealOpr.setStatus(_A)
_OsaOprOsaTapRatio_Type=FloatHundredths
_OsaOprOsaTapRatio_Object=MibTableColumn
osaOprOsaTapRatio=_OsaOprOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,19,1,1,2),_OsaOprOsaTapRatio_Type())
osaOprOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:osaOprOsaTapRatio.setStatus(_A)
_OsaPtpPmTable_Object=MibTable
osaPtpPmTable=_OsaPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2))
if mibBuilder.loadTexts:osaPtpPmTable.setStatus(_A)
_OsaPtpPmEntry_Object=MibTableRow
osaPtpPmEntry=_OsaPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1))
osaPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:osaPtpPmEntry.setStatus(_A)
class _OsaPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OsaPtpPmTimestamp_Type.__name__=_F
_OsaPtpPmTimestamp_Object=MibTableColumn
osaPtpPmTimestamp=_OsaPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,1),_OsaPtpPmTimestamp_Type())
osaPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:osaPtpPmTimestamp.setStatus(_A)
class _OsaPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OsaPtpPmSampleDuration_Type.__name__=_F
_OsaPtpPmSampleDuration_Object=MibTableColumn
osaPtpPmSampleDuration=_OsaPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,2),_OsaPtpPmSampleDuration_Type())
osaPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:osaPtpPmSampleDuration.setStatus(_A)
_OsaPtpPmValidity_Type=TruthValue
_OsaPtpPmValidity_Object=MibTableColumn
osaPtpPmValidity=_OsaPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,3),_OsaPtpPmValidity_Type())
osaPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:osaPtpPmValidity.setStatus(_A)
_OsaPtpPmOprMin_Type=FloatHundredths
_OsaPtpPmOprMin_Object=MibTableColumn
osaPtpPmOprMin=_OsaPtpPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,4),_OsaPtpPmOprMin_Type())
osaPtpPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:osaPtpPmOprMin.setStatus(_A)
_OsaPtpPmOprMax_Type=FloatHundredths
_OsaPtpPmOprMax_Object=MibTableColumn
osaPtpPmOprMax=_OsaPtpPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,5),_OsaPtpPmOprMax_Type())
osaPtpPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:osaPtpPmOprMax.setStatus(_A)
_OsaPtpPmOprAve_Type=FloatHundredths
_OsaPtpPmOprAve_Object=MibTableColumn
osaPtpPmOprAve=_OsaPtpPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,19,2,1,6),_OsaPtpPmOprAve_Type())
osaPtpPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:osaPtpPmOprAve.setStatus(_A)
_OsaPtpPmConformance_ObjectIdentity=ObjectIdentity
osaPtpPmConformance=_OsaPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,19,3))
_OsaPtpPmCompliances_ObjectIdentity=ObjectIdentity
osaPtpPmCompliances=_OsaPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,19,3,1))
_OsaPtpPmGroups_ObjectIdentity=ObjectIdentity
osaPtpPmGroups=_OsaPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,19,3,2))
osaPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,19,3,2,1))
osaPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:osaPtpPmGroup.setStatus(_A)
osaPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,19,3,2,2))
osaPtpPmRealGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:osaPtpPmRealGroup.setStatus(_A)
osaPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,19,3,1,1))
osaPtpPmCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:osaPtpPmCompliance.setStatus(_A)
osaPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,19,3,1,2))
osaPtpPmRealCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:osaPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osaPtpPmMIB':osaPtpPmMIB,'osaPtpPmRealTable':osaPtpPmRealTable,'osaPtpPmRealEntry':osaPtpPmRealEntry,_N:osaPtpPmRealOpr,_O:osaOprOsaTapRatio,'osaPtpPmTable':osaPtpPmTable,'osaPtpPmEntry':osaPtpPmEntry,_H:osaPtpPmTimestamp,_G:osaPtpPmSampleDuration,_J:osaPtpPmValidity,_K:osaPtpPmOprMin,_L:osaPtpPmOprMax,_M:osaPtpPmOprAve,'osaPtpPmConformance':osaPtpPmConformance,'osaPtpPmCompliances':osaPtpPmCompliances,'osaPtpPmCompliance':osaPtpPmCompliance,'osaPtpPmRealCompliance':osaPtpPmRealCompliance,'osaPtpPmGroups':osaPtpPmGroups,_P:osaPtpPmGroup,_Q:osaPtpPmRealGroup})