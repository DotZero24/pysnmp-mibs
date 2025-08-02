_T='expnPtpPmRealGroup'
_S='expnPtpPmGroup'
_R='expnPtpPmRealOpr'
_Q='expnPtpPmRealOpt'
_P='expnPtpPmOprAve'
_O='expnPtpPmOprMax'
_N='expnPtpPmOprMin'
_M='expnPtpPmOptAve'
_L='expnPtpPmOptMax'
_K='expnPtpPmOptMin'
_J='expnPtpPmValidity'
_I='not-accessible'
_H='expnPtpPmTimestamp'
_G='expnPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-EXPNPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,InfnSampleDuration=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','InfnSampleDuration')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
expnPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,82))
if mibBuilder.loadTexts:expnPtpPmMIB.setRevisions(('2017-02-13 00:00',))
_ExpnPtpPmRealTable_Object=MibTable
expnPtpPmRealTable=_ExpnPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,82,1))
if mibBuilder.loadTexts:expnPtpPmRealTable.setStatus(_A)
_ExpnPtpPmRealEntry_Object=MibTableRow
expnPtpPmRealEntry=_ExpnPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,82,1,1))
expnPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:expnPtpPmRealEntry.setStatus(_A)
_ExpnPtpPmRealOpt_Type=FloatArbitraryPrecision
_ExpnPtpPmRealOpt_Object=MibTableColumn
expnPtpPmRealOpt=_ExpnPtpPmRealOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,82,1,1,1),_ExpnPtpPmRealOpt_Type())
expnPtpPmRealOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmRealOpt.setStatus(_A)
_ExpnPtpPmRealOpr_Type=FloatArbitraryPrecision
_ExpnPtpPmRealOpr_Object=MibTableColumn
expnPtpPmRealOpr=_ExpnPtpPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,82,1,1,2),_ExpnPtpPmRealOpr_Type())
expnPtpPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmRealOpr.setStatus(_A)
_ExpnPtpPmTable_Object=MibTable
expnPtpPmTable=_ExpnPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2))
if mibBuilder.loadTexts:expnPtpPmTable.setStatus(_A)
_ExpnPtpPmEntry_Object=MibTableRow
expnPtpPmEntry=_ExpnPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1))
expnPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:expnPtpPmEntry.setStatus(_A)
class _ExpnPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ExpnPtpPmTimestamp_Type.__name__=_F
_ExpnPtpPmTimestamp_Object=MibTableColumn
expnPtpPmTimestamp=_ExpnPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,1),_ExpnPtpPmTimestamp_Type())
expnPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:expnPtpPmTimestamp.setStatus(_A)
class _ExpnPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_ExpnPtpPmSampleDuration_Type.__name__=_F
_ExpnPtpPmSampleDuration_Object=MibTableColumn
expnPtpPmSampleDuration=_ExpnPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,2),_ExpnPtpPmSampleDuration_Type())
expnPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:expnPtpPmSampleDuration.setStatus(_A)
_ExpnPtpPmValidity_Type=TruthValue
_ExpnPtpPmValidity_Object=MibTableColumn
expnPtpPmValidity=_ExpnPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,3),_ExpnPtpPmValidity_Type())
expnPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmValidity.setStatus(_A)
_ExpnPtpPmOptMin_Type=FloatArbitraryPrecision
_ExpnPtpPmOptMin_Object=MibTableColumn
expnPtpPmOptMin=_ExpnPtpPmOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,4),_ExpnPtpPmOptMin_Type())
expnPtpPmOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOptMin.setStatus(_A)
_ExpnPtpPmOptMax_Type=FloatArbitraryPrecision
_ExpnPtpPmOptMax_Object=MibTableColumn
expnPtpPmOptMax=_ExpnPtpPmOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,5),_ExpnPtpPmOptMax_Type())
expnPtpPmOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOptMax.setStatus(_A)
_ExpnPtpPmOptAve_Type=FloatArbitraryPrecision
_ExpnPtpPmOptAve_Object=MibTableColumn
expnPtpPmOptAve=_ExpnPtpPmOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,6),_ExpnPtpPmOptAve_Type())
expnPtpPmOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOptAve.setStatus(_A)
_ExpnPtpPmOprMin_Type=FloatArbitraryPrecision
_ExpnPtpPmOprMin_Object=MibTableColumn
expnPtpPmOprMin=_ExpnPtpPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,7),_ExpnPtpPmOprMin_Type())
expnPtpPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOprMin.setStatus(_A)
_ExpnPtpPmOprMax_Type=FloatArbitraryPrecision
_ExpnPtpPmOprMax_Object=MibTableColumn
expnPtpPmOprMax=_ExpnPtpPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,8),_ExpnPtpPmOprMax_Type())
expnPtpPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOprMax.setStatus(_A)
_ExpnPtpPmOprAve_Type=FloatArbitraryPrecision
_ExpnPtpPmOprAve_Object=MibTableColumn
expnPtpPmOprAve=_ExpnPtpPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,82,2,1,9),_ExpnPtpPmOprAve_Type())
expnPtpPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:expnPtpPmOprAve.setStatus(_A)
_ExpnPtpPmConformance_ObjectIdentity=ObjectIdentity
expnPtpPmConformance=_ExpnPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,82,3))
_ExpnPtpPmCompliances_ObjectIdentity=ObjectIdentity
expnPtpPmCompliances=_ExpnPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,82,3,1))
_ExpnPtpPmGroups_ObjectIdentity=ObjectIdentity
expnPtpPmGroups=_ExpnPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,82,3,2))
expnPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,82,3,2,1))
expnPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:expnPtpPmGroup.setStatus(_A)
expnPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,82,3,2,2))
expnPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:expnPtpPmRealGroup.setStatus(_A)
expnPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,82,3,1,1))
expnPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:expnPtpPmCompliance.setStatus(_A)
expnPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,82,3,1,2))
expnPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:expnPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'expnPtpPmMIB':expnPtpPmMIB,'expnPtpPmRealTable':expnPtpPmRealTable,'expnPtpPmRealEntry':expnPtpPmRealEntry,_Q:expnPtpPmRealOpt,_R:expnPtpPmRealOpr,'expnPtpPmTable':expnPtpPmTable,'expnPtpPmEntry':expnPtpPmEntry,_H:expnPtpPmTimestamp,_G:expnPtpPmSampleDuration,_J:expnPtpPmValidity,_K:expnPtpPmOptMin,_L:expnPtpPmOptMax,_M:expnPtpPmOptAve,_N:expnPtpPmOprMin,_O:expnPtpPmOprMax,_P:expnPtpPmOprAve,'expnPtpPmConformance':expnPtpPmConformance,'expnPtpPmCompliances':expnPtpPmCompliances,'expnPtpPmCompliance':expnPtpPmCompliance,'expnPtpPmRealCompliance':expnPtpPmRealCompliance,'expnPtpPmGroups':expnPtpPmGroups,_S:expnPtpPmGroup,_T:expnPtpPmRealGroup})