_X='asePtpPmRealGroup'
_W='asePtpPmGroup'
_V='asePtpPmRealCmnAsePostRxVoa'
_U='asePtpPmRealCmnAseOpr'
_T='asePtpPmRealCmnAseOpt'
_S='asePtpPmCmnAsePostRxVoaAve'
_R='asePtpPmCmnAsePostRxVoaMax'
_Q='asePtpPmCmnAsePostRxVoaMin'
_P='asePtpPmCmnAseOprAve'
_O='asePtpPmCmnAseOprMax'
_N='asePtpPmCmnAseOprMin'
_M='asePtpPmCmnAseOptAve'
_L='asePtpPmCmnAseOptMax'
_K='asePtpPmCmnAseOptMin'
_J='asePtpPmValidity'
_I='not-accessible'
_H='asePtpPmTimestamp'
_G='asePtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-ASEPTP-MIB'
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
asePtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,84))
if mibBuilder.loadTexts:asePtpPmMIB.setRevisions(('2017-06-09 00:00',))
_AsePtpPmRealTable_Object=MibTable
asePtpPmRealTable=_AsePtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,84,1))
if mibBuilder.loadTexts:asePtpPmRealTable.setStatus(_A)
_AsePtpPmRealEntry_Object=MibTableRow
asePtpPmRealEntry=_AsePtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,84,1,1))
asePtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:asePtpPmRealEntry.setStatus(_A)
_AsePtpPmRealCmnAseOpt_Type=FloatArbitraryPrecision
_AsePtpPmRealCmnAseOpt_Object=MibTableColumn
asePtpPmRealCmnAseOpt=_AsePtpPmRealCmnAseOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,84,1,1,1),_AsePtpPmRealCmnAseOpt_Type())
asePtpPmRealCmnAseOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmRealCmnAseOpt.setStatus(_A)
_AsePtpPmRealCmnAseOpr_Type=FloatArbitraryPrecision
_AsePtpPmRealCmnAseOpr_Object=MibTableColumn
asePtpPmRealCmnAseOpr=_AsePtpPmRealCmnAseOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,84,1,1,2),_AsePtpPmRealCmnAseOpr_Type())
asePtpPmRealCmnAseOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmRealCmnAseOpr.setStatus(_A)
_AsePtpPmRealCmnAsePostRxVoa_Type=FloatArbitraryPrecision
_AsePtpPmRealCmnAsePostRxVoa_Object=MibTableColumn
asePtpPmRealCmnAsePostRxVoa=_AsePtpPmRealCmnAsePostRxVoa_Object((1,3,6,1,4,1,21296,2,2,2,3,84,1,1,3),_AsePtpPmRealCmnAsePostRxVoa_Type())
asePtpPmRealCmnAsePostRxVoa.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmRealCmnAsePostRxVoa.setStatus(_A)
_AsePtpPmTable_Object=MibTable
asePtpPmTable=_AsePtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2))
if mibBuilder.loadTexts:asePtpPmTable.setStatus(_A)
_AsePtpPmEntry_Object=MibTableRow
asePtpPmEntry=_AsePtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1))
asePtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:asePtpPmEntry.setStatus(_A)
class _AsePtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AsePtpPmTimestamp_Type.__name__=_F
_AsePtpPmTimestamp_Object=MibTableColumn
asePtpPmTimestamp=_AsePtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,1),_AsePtpPmTimestamp_Type())
asePtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:asePtpPmTimestamp.setStatus(_A)
class _AsePtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_AsePtpPmSampleDuration_Type.__name__=_F
_AsePtpPmSampleDuration_Object=MibTableColumn
asePtpPmSampleDuration=_AsePtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,2),_AsePtpPmSampleDuration_Type())
asePtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:asePtpPmSampleDuration.setStatus(_A)
_AsePtpPmValidity_Type=TruthValue
_AsePtpPmValidity_Object=MibTableColumn
asePtpPmValidity=_AsePtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,3),_AsePtpPmValidity_Type())
asePtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmValidity.setStatus(_A)
_AsePtpPmCmnAseOptMin_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOptMin_Object=MibTableColumn
asePtpPmCmnAseOptMin=_AsePtpPmCmnAseOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,4),_AsePtpPmCmnAseOptMin_Type())
asePtpPmCmnAseOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOptMin.setStatus(_A)
_AsePtpPmCmnAseOptMax_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOptMax_Object=MibTableColumn
asePtpPmCmnAseOptMax=_AsePtpPmCmnAseOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,5),_AsePtpPmCmnAseOptMax_Type())
asePtpPmCmnAseOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOptMax.setStatus(_A)
_AsePtpPmCmnAseOptAve_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOptAve_Object=MibTableColumn
asePtpPmCmnAseOptAve=_AsePtpPmCmnAseOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,6),_AsePtpPmCmnAseOptAve_Type())
asePtpPmCmnAseOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOptAve.setStatus(_A)
_AsePtpPmCmnAseOprMin_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOprMin_Object=MibTableColumn
asePtpPmCmnAseOprMin=_AsePtpPmCmnAseOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,7),_AsePtpPmCmnAseOprMin_Type())
asePtpPmCmnAseOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOprMin.setStatus(_A)
_AsePtpPmCmnAseOprMax_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOprMax_Object=MibTableColumn
asePtpPmCmnAseOprMax=_AsePtpPmCmnAseOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,8),_AsePtpPmCmnAseOprMax_Type())
asePtpPmCmnAseOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOprMax.setStatus(_A)
_AsePtpPmCmnAseOprAve_Type=FloatArbitraryPrecision
_AsePtpPmCmnAseOprAve_Object=MibTableColumn
asePtpPmCmnAseOprAve=_AsePtpPmCmnAseOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,9),_AsePtpPmCmnAseOprAve_Type())
asePtpPmCmnAseOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAseOprAve.setStatus(_A)
_AsePtpPmCmnAsePostRxVoaMin_Type=FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaMin_Object=MibTableColumn
asePtpPmCmnAsePostRxVoaMin=_AsePtpPmCmnAsePostRxVoaMin_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,10),_AsePtpPmCmnAsePostRxVoaMin_Type())
asePtpPmCmnAsePostRxVoaMin.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAsePostRxVoaMin.setStatus(_A)
_AsePtpPmCmnAsePostRxVoaMax_Type=FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaMax_Object=MibTableColumn
asePtpPmCmnAsePostRxVoaMax=_AsePtpPmCmnAsePostRxVoaMax_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,11),_AsePtpPmCmnAsePostRxVoaMax_Type())
asePtpPmCmnAsePostRxVoaMax.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAsePostRxVoaMax.setStatus(_A)
_AsePtpPmCmnAsePostRxVoaAve_Type=FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaAve_Object=MibTableColumn
asePtpPmCmnAsePostRxVoaAve=_AsePtpPmCmnAsePostRxVoaAve_Object((1,3,6,1,4,1,21296,2,2,2,3,84,2,1,12),_AsePtpPmCmnAsePostRxVoaAve_Type())
asePtpPmCmnAsePostRxVoaAve.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmCmnAsePostRxVoaAve.setStatus(_A)
_AsePtpPmConformance_ObjectIdentity=ObjectIdentity
asePtpPmConformance=_AsePtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,84,3))
_AsePtpPmCompliances_ObjectIdentity=ObjectIdentity
asePtpPmCompliances=_AsePtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,84,3,1))
_AsePtpPmGroups_ObjectIdentity=ObjectIdentity
asePtpPmGroups=_AsePtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,84,3,2))
asePtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,84,3,2,1))
asePtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:asePtpPmGroup.setStatus(_A)
asePtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,84,3,2,2))
asePtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:asePtpPmRealGroup.setStatus(_A)
asePtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,84,3,1,1))
asePtpPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:asePtpPmCompliance.setStatus(_A)
asePtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,84,3,1,2))
asePtpPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:asePtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'asePtpPmMIB':asePtpPmMIB,'asePtpPmRealTable':asePtpPmRealTable,'asePtpPmRealEntry':asePtpPmRealEntry,_T:asePtpPmRealCmnAseOpt,_U:asePtpPmRealCmnAseOpr,_V:asePtpPmRealCmnAsePostRxVoa,'asePtpPmTable':asePtpPmTable,'asePtpPmEntry':asePtpPmEntry,_H:asePtpPmTimestamp,_G:asePtpPmSampleDuration,_J:asePtpPmValidity,_K:asePtpPmCmnAseOptMin,_L:asePtpPmCmnAseOptMax,_M:asePtpPmCmnAseOptAve,_N:asePtpPmCmnAseOprMin,_O:asePtpPmCmnAseOprMax,_P:asePtpPmCmnAseOprAve,_Q:asePtpPmCmnAsePostRxVoaMin,_R:asePtpPmCmnAsePostRxVoaMax,_S:asePtpPmCmnAsePostRxVoaAve,'asePtpPmConformance':asePtpPmConformance,'asePtpPmCompliances':asePtpPmCompliances,'asePtpPmCompliance':asePtpPmCompliance,'asePtpPmRealCompliance':asePtpPmRealCompliance,'asePtpPmGroups':asePtpPmGroups,_W:asePtpPmGroup,_X:asePtpPmRealGroup})