_X='idlerCtpPmRealGroup'
_W='idlerCtpPmGroup'
_V='idlerCtpPmRealCmnIdlerPostRxVoa'
_U='idlerCtpPmRealCmnIdlerOpr'
_T='idlerCtpPmRealCmnIdlerOpt'
_S='idlerCtpPmCmnIdlerPostRxVoaAve'
_R='idlerCtpPmCmnIdlerPostRxVoaMax'
_Q='idlerCtpPmCmnIdlerPostRxVoaMin'
_P='idlerCtpPmCmnIdlerOprAve'
_O='idlerCtpPmCmnIdlerOprMax'
_N='idlerCtpPmCmnIdlerOprMin'
_M='idlerCtpPmCmnIdlerOptAve'
_L='idlerCtpPmCmnIdlerOptMax'
_K='idlerCtpPmCmnIdlerOptMin'
_J='idlerCtpPmValidity'
_I='not-accessible'
_H='idlerCtpPmTimestamp'
_G='idlerCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-IDLERCTP-MIB'
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
idlerCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,86))
if mibBuilder.loadTexts:idlerCtpPmMIB.setRevisions(('2017-06-09 00:00',))
_IdlerCtpPmRealTable_Object=MibTable
idlerCtpPmRealTable=_IdlerCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,86,1))
if mibBuilder.loadTexts:idlerCtpPmRealTable.setStatus(_A)
_IdlerCtpPmRealEntry_Object=MibTableRow
idlerCtpPmRealEntry=_IdlerCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,86,1,1))
idlerCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:idlerCtpPmRealEntry.setStatus(_A)
_IdlerCtpPmRealCmnIdlerOpt_Type=FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerOpt_Object=MibTableColumn
idlerCtpPmRealCmnIdlerOpt=_IdlerCtpPmRealCmnIdlerOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,86,1,1,1),_IdlerCtpPmRealCmnIdlerOpt_Type())
idlerCtpPmRealCmnIdlerOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmRealCmnIdlerOpt.setStatus(_A)
_IdlerCtpPmRealCmnIdlerOpr_Type=FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerOpr_Object=MibTableColumn
idlerCtpPmRealCmnIdlerOpr=_IdlerCtpPmRealCmnIdlerOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,86,1,1,2),_IdlerCtpPmRealCmnIdlerOpr_Type())
idlerCtpPmRealCmnIdlerOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmRealCmnIdlerOpr.setStatus(_A)
_IdlerCtpPmRealCmnIdlerPostRxVoa_Type=FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerPostRxVoa_Object=MibTableColumn
idlerCtpPmRealCmnIdlerPostRxVoa=_IdlerCtpPmRealCmnIdlerPostRxVoa_Object((1,3,6,1,4,1,21296,2,2,2,3,86,1,1,3),_IdlerCtpPmRealCmnIdlerPostRxVoa_Type())
idlerCtpPmRealCmnIdlerPostRxVoa.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmRealCmnIdlerPostRxVoa.setStatus(_A)
_IdlerCtpPmTable_Object=MibTable
idlerCtpPmTable=_IdlerCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2))
if mibBuilder.loadTexts:idlerCtpPmTable.setStatus(_A)
_IdlerCtpPmEntry_Object=MibTableRow
idlerCtpPmEntry=_IdlerCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1))
idlerCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:idlerCtpPmEntry.setStatus(_A)
class _IdlerCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IdlerCtpPmTimestamp_Type.__name__=_F
_IdlerCtpPmTimestamp_Object=MibTableColumn
idlerCtpPmTimestamp=_IdlerCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,1),_IdlerCtpPmTimestamp_Type())
idlerCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:idlerCtpPmTimestamp.setStatus(_A)
class _IdlerCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_IdlerCtpPmSampleDuration_Type.__name__=_F
_IdlerCtpPmSampleDuration_Object=MibTableColumn
idlerCtpPmSampleDuration=_IdlerCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,2),_IdlerCtpPmSampleDuration_Type())
idlerCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:idlerCtpPmSampleDuration.setStatus(_A)
_IdlerCtpPmValidity_Type=TruthValue
_IdlerCtpPmValidity_Object=MibTableColumn
idlerCtpPmValidity=_IdlerCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,3),_IdlerCtpPmValidity_Type())
idlerCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmValidity.setStatus(_A)
_IdlerCtpPmCmnIdlerOptMin_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptMin_Object=MibTableColumn
idlerCtpPmCmnIdlerOptMin=_IdlerCtpPmCmnIdlerOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,4),_IdlerCtpPmCmnIdlerOptMin_Type())
idlerCtpPmCmnIdlerOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOptMin.setStatus(_A)
_IdlerCtpPmCmnIdlerOptMax_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptMax_Object=MibTableColumn
idlerCtpPmCmnIdlerOptMax=_IdlerCtpPmCmnIdlerOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,5),_IdlerCtpPmCmnIdlerOptMax_Type())
idlerCtpPmCmnIdlerOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOptMax.setStatus(_A)
_IdlerCtpPmCmnIdlerOptAve_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptAve_Object=MibTableColumn
idlerCtpPmCmnIdlerOptAve=_IdlerCtpPmCmnIdlerOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,6),_IdlerCtpPmCmnIdlerOptAve_Type())
idlerCtpPmCmnIdlerOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOptAve.setStatus(_A)
_IdlerCtpPmCmnIdlerOprMin_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprMin_Object=MibTableColumn
idlerCtpPmCmnIdlerOprMin=_IdlerCtpPmCmnIdlerOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,7),_IdlerCtpPmCmnIdlerOprMin_Type())
idlerCtpPmCmnIdlerOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOprMin.setStatus(_A)
_IdlerCtpPmCmnIdlerOprMax_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprMax_Object=MibTableColumn
idlerCtpPmCmnIdlerOprMax=_IdlerCtpPmCmnIdlerOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,8),_IdlerCtpPmCmnIdlerOprMax_Type())
idlerCtpPmCmnIdlerOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOprMax.setStatus(_A)
_IdlerCtpPmCmnIdlerOprAve_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprAve_Object=MibTableColumn
idlerCtpPmCmnIdlerOprAve=_IdlerCtpPmCmnIdlerOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,9),_IdlerCtpPmCmnIdlerOprAve_Type())
idlerCtpPmCmnIdlerOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerOprAve.setStatus(_A)
_IdlerCtpPmCmnIdlerPostRxVoaMin_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaMin_Object=MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaMin=_IdlerCtpPmCmnIdlerPostRxVoaMin_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,10),_IdlerCtpPmCmnIdlerPostRxVoaMin_Type())
idlerCtpPmCmnIdlerPostRxVoaMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerPostRxVoaMin.setStatus(_A)
_IdlerCtpPmCmnIdlerPostRxVoaMax_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaMax_Object=MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaMax=_IdlerCtpPmCmnIdlerPostRxVoaMax_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,11),_IdlerCtpPmCmnIdlerPostRxVoaMax_Type())
idlerCtpPmCmnIdlerPostRxVoaMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerPostRxVoaMax.setStatus(_A)
_IdlerCtpPmCmnIdlerPostRxVoaAve_Type=FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaAve_Object=MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaAve=_IdlerCtpPmCmnIdlerPostRxVoaAve_Object((1,3,6,1,4,1,21296,2,2,2,3,86,2,1,12),_IdlerCtpPmCmnIdlerPostRxVoaAve_Type())
idlerCtpPmCmnIdlerPostRxVoaAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerCtpPmCmnIdlerPostRxVoaAve.setStatus(_A)
_IdlerCtpPmConformance_ObjectIdentity=ObjectIdentity
idlerCtpPmConformance=_IdlerCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,86,3))
_IdlerCtpPmCompliances_ObjectIdentity=ObjectIdentity
idlerCtpPmCompliances=_IdlerCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,86,3,1))
_IdlerCtpPmGroups_ObjectIdentity=ObjectIdentity
idlerCtpPmGroups=_IdlerCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,86,3,2))
idlerCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,86,3,2,1))
idlerCtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:idlerCtpPmGroup.setStatus(_A)
idlerCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,86,3,2,2))
idlerCtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:idlerCtpPmRealGroup.setStatus(_A)
idlerCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,86,3,1,1))
idlerCtpPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:idlerCtpPmCompliance.setStatus(_A)
idlerCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,86,3,1,2))
idlerCtpPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:idlerCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'idlerCtpPmMIB':idlerCtpPmMIB,'idlerCtpPmRealTable':idlerCtpPmRealTable,'idlerCtpPmRealEntry':idlerCtpPmRealEntry,_T:idlerCtpPmRealCmnIdlerOpt,_U:idlerCtpPmRealCmnIdlerOpr,_V:idlerCtpPmRealCmnIdlerPostRxVoa,'idlerCtpPmTable':idlerCtpPmTable,'idlerCtpPmEntry':idlerCtpPmEntry,_H:idlerCtpPmTimestamp,_G:idlerCtpPmSampleDuration,_J:idlerCtpPmValidity,_K:idlerCtpPmCmnIdlerOptMin,_L:idlerCtpPmCmnIdlerOptMax,_M:idlerCtpPmCmnIdlerOptAve,_N:idlerCtpPmCmnIdlerOprMin,_O:idlerCtpPmCmnIdlerOprMax,_P:idlerCtpPmCmnIdlerOprAve,_Q:idlerCtpPmCmnIdlerPostRxVoaMin,_R:idlerCtpPmCmnIdlerPostRxVoaMax,_S:idlerCtpPmCmnIdlerPostRxVoaAve,'idlerCtpPmConformance':idlerCtpPmConformance,'idlerCtpPmCompliances':idlerCtpPmCompliances,'idlerCtpPmCompliance':idlerCtpPmCompliance,'idlerCtpPmRealCompliance':idlerCtpPmRealCompliance,'idlerCtpPmGroups':idlerCtpPmGroups,_W:idlerCtpPmGroup,_X:idlerCtpPmRealGroup})