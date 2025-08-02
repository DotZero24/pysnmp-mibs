_T='fbmScgptpPmRealGroup'
_S='fbmScgptpPmGroup'
_R='fbmScgptpPmRealCmnScgOpr'
_Q='fbmScgptpPmRealCmnScgOpt'
_P='fbmScgptpPmCmnScgOprAve'
_O='fbmScgptpPmCmnScgOprMax'
_N='fbmScgptpPmCmnScgOprMin'
_M='fbmScgptpPmCmnScgOptAve'
_L='fbmScgptpPmCmnScgOptMax'
_K='fbmScgptpPmCmnScgOptMin'
_J='fbmScgptpPmValidity'
_I='not-accessible'
_H='Integer32'
_G='fbmScgptpPmTimestamp'
_F='fbmScgptpPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FBMSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,InfnSampleDuration=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','InfnSampleDuration')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fbmScgptpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,83))
if mibBuilder.loadTexts:fbmScgptpPmMIB.setRevisions(('2017-02-13 00:00',))
_FbmScgptpPmRealTable_Object=MibTable
fbmScgptpPmRealTable=_FbmScgptpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,83,1))
if mibBuilder.loadTexts:fbmScgptpPmRealTable.setStatus(_A)
_FbmScgptpPmRealEntry_Object=MibTableRow
fbmScgptpPmRealEntry=_FbmScgptpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,83,1,1))
fbmScgptpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fbmScgptpPmRealEntry.setStatus(_A)
_FbmScgptpPmRealCmnScgOpt_Type=FloatArbitraryPrecision
_FbmScgptpPmRealCmnScgOpt_Object=MibTableColumn
fbmScgptpPmRealCmnScgOpt=_FbmScgptpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,83,1,1,1),_FbmScgptpPmRealCmnScgOpt_Type())
fbmScgptpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmRealCmnScgOpt.setStatus(_A)
_FbmScgptpPmRealCmnScgOpr_Type=FloatArbitraryPrecision
_FbmScgptpPmRealCmnScgOpr_Object=MibTableColumn
fbmScgptpPmRealCmnScgOpr=_FbmScgptpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,83,1,1,2),_FbmScgptpPmRealCmnScgOpr_Type())
fbmScgptpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmRealCmnScgOpr.setStatus(_A)
_FbmScgptpPmTable_Object=MibTable
fbmScgptpPmTable=_FbmScgptpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2))
if mibBuilder.loadTexts:fbmScgptpPmTable.setStatus(_A)
_FbmScgptpPmEntry_Object=MibTableRow
fbmScgptpPmEntry=_FbmScgptpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1))
fbmScgptpPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:fbmScgptpPmEntry.setStatus(_A)
class _FbmScgptpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FbmScgptpPmTimestamp_Type.__name__=_H
_FbmScgptpPmTimestamp_Object=MibTableColumn
fbmScgptpPmTimestamp=_FbmScgptpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,1),_FbmScgptpPmTimestamp_Type())
fbmScgptpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:fbmScgptpPmTimestamp.setStatus(_A)
_FbmScgptpPmSampleDuration_Type=InfnSampleDuration
_FbmScgptpPmSampleDuration_Object=MibTableColumn
fbmScgptpPmSampleDuration=_FbmScgptpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,2),_FbmScgptpPmSampleDuration_Type())
fbmScgptpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:fbmScgptpPmSampleDuration.setStatus(_A)
_FbmScgptpPmValidity_Type=TruthValue
_FbmScgptpPmValidity_Object=MibTableColumn
fbmScgptpPmValidity=_FbmScgptpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,3),_FbmScgptpPmValidity_Type())
fbmScgptpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmValidity.setStatus(_A)
_FbmScgptpPmCmnScgOptMin_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptMin_Object=MibTableColumn
fbmScgptpPmCmnScgOptMin=_FbmScgptpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,4),_FbmScgptpPmCmnScgOptMin_Type())
fbmScgptpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOptMin.setStatus(_A)
_FbmScgptpPmCmnScgOptMax_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptMax_Object=MibTableColumn
fbmScgptpPmCmnScgOptMax=_FbmScgptpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,5),_FbmScgptpPmCmnScgOptMax_Type())
fbmScgptpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOptMax.setStatus(_A)
_FbmScgptpPmCmnScgOptAve_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptAve_Object=MibTableColumn
fbmScgptpPmCmnScgOptAve=_FbmScgptpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,6),_FbmScgptpPmCmnScgOptAve_Type())
fbmScgptpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOptAve.setStatus(_A)
_FbmScgptpPmCmnScgOprMin_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprMin_Object=MibTableColumn
fbmScgptpPmCmnScgOprMin=_FbmScgptpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,7),_FbmScgptpPmCmnScgOprMin_Type())
fbmScgptpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOprMin.setStatus(_A)
_FbmScgptpPmCmnScgOprMax_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprMax_Object=MibTableColumn
fbmScgptpPmCmnScgOprMax=_FbmScgptpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,8),_FbmScgptpPmCmnScgOprMax_Type())
fbmScgptpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOprMax.setStatus(_A)
_FbmScgptpPmCmnScgOprAve_Type=FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprAve_Object=MibTableColumn
fbmScgptpPmCmnScgOprAve=_FbmScgptpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,83,2,1,9),_FbmScgptpPmCmnScgOprAve_Type())
fbmScgptpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgptpPmCmnScgOprAve.setStatus(_A)
_FbmScgptpPmConformance_ObjectIdentity=ObjectIdentity
fbmScgptpPmConformance=_FbmScgptpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,83,3))
_FbmScgptpPmCompliances_ObjectIdentity=ObjectIdentity
fbmScgptpPmCompliances=_FbmScgptpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,83,3,1))
_FbmScgptpPmGroups_ObjectIdentity=ObjectIdentity
fbmScgptpPmGroups=_FbmScgptpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,83,3,2))
fbmScgptpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,83,3,2,1))
fbmScgptpPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fbmScgptpPmGroup.setStatus(_A)
fbmScgptpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,83,3,2,2))
fbmScgptpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:fbmScgptpPmRealGroup.setStatus(_A)
fbmScgptpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,83,3,1,1))
fbmScgptpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:fbmScgptpPmCompliance.setStatus(_A)
fbmScgptpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,83,3,1,2))
fbmScgptpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:fbmScgptpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fbmScgptpPmMIB':fbmScgptpPmMIB,'fbmScgptpPmRealTable':fbmScgptpPmRealTable,'fbmScgptpPmRealEntry':fbmScgptpPmRealEntry,_Q:fbmScgptpPmRealCmnScgOpt,_R:fbmScgptpPmRealCmnScgOpr,'fbmScgptpPmTable':fbmScgptpPmTable,'fbmScgptpPmEntry':fbmScgptpPmEntry,_G:fbmScgptpPmTimestamp,_F:fbmScgptpPmSampleDuration,_J:fbmScgptpPmValidity,_K:fbmScgptpPmCmnScgOptMin,_L:fbmScgptpPmCmnScgOptMax,_M:fbmScgptpPmCmnScgOptAve,_N:fbmScgptpPmCmnScgOprMin,_O:fbmScgptpPmCmnScgOprMax,_P:fbmScgptpPmCmnScgOprAve,'fbmScgptpPmConformance':fbmScgptpPmConformance,'fbmScgptpPmCompliances':fbmScgptpPmCompliances,'fbmScgptpPmCompliance':fbmScgptpPmCompliance,'fbmScgptpPmRealCompliance':fbmScgptpPmRealCompliance,'fbmScgptpPmGroups':fbmScgptpPmGroups,_S:fbmScgptpPmGroup,_T:fbmScgptpPmRealGroup})