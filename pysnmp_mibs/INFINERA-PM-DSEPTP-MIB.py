_T='dsePtpPmRealGroup'
_S='dsePtpPmGroup'
_R='dsePtpPmRealOpr'
_Q='dsePtpPmRealOpt'
_P='dsePtpPmOprAve'
_O='dsePtpPmOprMax'
_N='dsePtpPmOprMin'
_M='dsePtpPmOptAve'
_L='dsePtpPmOptMax'
_K='dsePtpPmOptMin'
_J='dsePtpPmValidity'
_I='not-accessible'
_H='dsePtpPmTimestamp'
_G='dsePtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-DSEPTP-MIB'
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
dsePtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,18))
if mibBuilder.loadTexts:dsePtpPmMIB.setRevisions(('2008-10-20 00:00',))
_DsePtpPmRealTable_Object=MibTable
dsePtpPmRealTable=_DsePtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,18,1))
if mibBuilder.loadTexts:dsePtpPmRealTable.setStatus(_A)
_DsePtpPmRealEntry_Object=MibTableRow
dsePtpPmRealEntry=_DsePtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,18,1,1))
dsePtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dsePtpPmRealEntry.setStatus(_A)
_DsePtpPmRealOpt_Type=FloatHundredths
_DsePtpPmRealOpt_Object=MibTableColumn
dsePtpPmRealOpt=_DsePtpPmRealOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,18,1,1,1),_DsePtpPmRealOpt_Type())
dsePtpPmRealOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmRealOpt.setStatus(_A)
_DsePtpPmRealOpr_Type=FloatHundredths
_DsePtpPmRealOpr_Object=MibTableColumn
dsePtpPmRealOpr=_DsePtpPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,18,1,1,2),_DsePtpPmRealOpr_Type())
dsePtpPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmRealOpr.setStatus(_A)
_DsePtpPmTable_Object=MibTable
dsePtpPmTable=_DsePtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2))
if mibBuilder.loadTexts:dsePtpPmTable.setStatus(_A)
_DsePtpPmEntry_Object=MibTableRow
dsePtpPmEntry=_DsePtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1))
dsePtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dsePtpPmEntry.setStatus(_A)
class _DsePtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DsePtpPmTimestamp_Type.__name__=_F
_DsePtpPmTimestamp_Object=MibTableColumn
dsePtpPmTimestamp=_DsePtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,1),_DsePtpPmTimestamp_Type())
dsePtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:dsePtpPmTimestamp.setStatus(_A)
class _DsePtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_DsePtpPmSampleDuration_Type.__name__=_F
_DsePtpPmSampleDuration_Object=MibTableColumn
dsePtpPmSampleDuration=_DsePtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,2),_DsePtpPmSampleDuration_Type())
dsePtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:dsePtpPmSampleDuration.setStatus(_A)
_DsePtpPmValidity_Type=TruthValue
_DsePtpPmValidity_Object=MibTableColumn
dsePtpPmValidity=_DsePtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,3),_DsePtpPmValidity_Type())
dsePtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmValidity.setStatus(_A)
_DsePtpPmOptMin_Type=FloatHundredths
_DsePtpPmOptMin_Object=MibTableColumn
dsePtpPmOptMin=_DsePtpPmOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,4),_DsePtpPmOptMin_Type())
dsePtpPmOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOptMin.setStatus(_A)
_DsePtpPmOptMax_Type=FloatHundredths
_DsePtpPmOptMax_Object=MibTableColumn
dsePtpPmOptMax=_DsePtpPmOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,5),_DsePtpPmOptMax_Type())
dsePtpPmOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOptMax.setStatus(_A)
_DsePtpPmOptAve_Type=FloatHundredths
_DsePtpPmOptAve_Object=MibTableColumn
dsePtpPmOptAve=_DsePtpPmOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,6),_DsePtpPmOptAve_Type())
dsePtpPmOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOptAve.setStatus(_A)
_DsePtpPmOprMin_Type=FloatHundredths
_DsePtpPmOprMin_Object=MibTableColumn
dsePtpPmOprMin=_DsePtpPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,7),_DsePtpPmOprMin_Type())
dsePtpPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOprMin.setStatus(_A)
_DsePtpPmOprMax_Type=FloatHundredths
_DsePtpPmOprMax_Object=MibTableColumn
dsePtpPmOprMax=_DsePtpPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,8),_DsePtpPmOprMax_Type())
dsePtpPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOprMax.setStatus(_A)
_DsePtpPmOprAve_Type=FloatHundredths
_DsePtpPmOprAve_Object=MibTableColumn
dsePtpPmOprAve=_DsePtpPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,18,2,1,9),_DsePtpPmOprAve_Type())
dsePtpPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dsePtpPmOprAve.setStatus(_A)
_DsePtpPmConformance_ObjectIdentity=ObjectIdentity
dsePtpPmConformance=_DsePtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,18,3))
_DsePtpPmCompliances_ObjectIdentity=ObjectIdentity
dsePtpPmCompliances=_DsePtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,18,3,1))
_DsePtpPmGroups_ObjectIdentity=ObjectIdentity
dsePtpPmGroups=_DsePtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,18,3,2))
dsePtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,18,3,2,1))
dsePtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dsePtpPmGroup.setStatus(_A)
dsePtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,18,3,2,2))
dsePtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:dsePtpPmRealGroup.setStatus(_A)
dsePtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,18,3,1,1))
dsePtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:dsePtpPmCompliance.setStatus(_A)
dsePtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,18,3,1,2))
dsePtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:dsePtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsePtpPmMIB':dsePtpPmMIB,'dsePtpPmRealTable':dsePtpPmRealTable,'dsePtpPmRealEntry':dsePtpPmRealEntry,_Q:dsePtpPmRealOpt,_R:dsePtpPmRealOpr,'dsePtpPmTable':dsePtpPmTable,'dsePtpPmEntry':dsePtpPmEntry,_H:dsePtpPmTimestamp,_G:dsePtpPmSampleDuration,_J:dsePtpPmValidity,_K:dsePtpPmOptMin,_L:dsePtpPmOptMax,_M:dsePtpPmOptAve,_N:dsePtpPmOprMin,_O:dsePtpPmOprMax,_P:dsePtpPmOprAve,'dsePtpPmConformance':dsePtpPmConformance,'dsePtpPmCompliances':dsePtpPmCompliances,'dsePtpPmCompliance':dsePtpPmCompliance,'dsePtpPmRealCompliance':dsePtpPmRealCompliance,'dsePtpPmGroups':dsePtpPmGroups,_S:dsePtpPmGroup,_T:dsePtpPmRealGroup})