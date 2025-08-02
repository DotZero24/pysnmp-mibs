_b='idlerPtpPmRealGroup'
_a='idlerPtpPmGroup'
_Z='idlerPtpPmRealTotalLaserPwr'
_Y='idlerPtpPmRealIdlerPostRxVoa'
_X='idlerPtpPmRealIdlerOpr'
_W='idlerPtpPmRealIdlerOpt'
_V='idlerPtpPmTotalLaserPwrAve'
_U='idlerPtpPmTotalLaserPwrMax'
_T='idlerPtpPmTotalLaserPwrMin'
_S='idlerPtpPmIdlerPostRxVoaAve'
_R='idlerPtpPmIdlerPostRxVoaMax'
_Q='idlerPtpPmIdlerPostRxVoaMin'
_P='idlerPtpPmIdlerOprAve'
_O='idlerPtpPmIdlerOprMax'
_N='idlerPtpPmIdlerOprMin'
_M='idlerPtpPmIdlerOptAve'
_L='idlerPtpPmIdlerOptMax'
_K='idlerPtpPmIdlerOptMin'
_J='idlerPtpPmValidity'
_I='not-accessible'
_H='idlerPtpPmTimestamp'
_G='idlerPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-IDLERPTP-MIB'
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
idlerPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,85))
if mibBuilder.loadTexts:idlerPtpPmMIB.setRevisions(('2017-06-21 00:00',))
_IdlerPtpPmRealTable_Object=MibTable
idlerPtpPmRealTable=_IdlerPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1))
if mibBuilder.loadTexts:idlerPtpPmRealTable.setStatus(_A)
_IdlerPtpPmRealEntry_Object=MibTableRow
idlerPtpPmRealEntry=_IdlerPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1,1))
idlerPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:idlerPtpPmRealEntry.setStatus(_A)
_IdlerPtpPmRealIdlerOpt_Type=FloatArbitraryPrecision
_IdlerPtpPmRealIdlerOpt_Object=MibTableColumn
idlerPtpPmRealIdlerOpt=_IdlerPtpPmRealIdlerOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1,1,1),_IdlerPtpPmRealIdlerOpt_Type())
idlerPtpPmRealIdlerOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmRealIdlerOpt.setStatus(_A)
_IdlerPtpPmRealIdlerOpr_Type=FloatArbitraryPrecision
_IdlerPtpPmRealIdlerOpr_Object=MibTableColumn
idlerPtpPmRealIdlerOpr=_IdlerPtpPmRealIdlerOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1,1,2),_IdlerPtpPmRealIdlerOpr_Type())
idlerPtpPmRealIdlerOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmRealIdlerOpr.setStatus(_A)
_IdlerPtpPmRealIdlerPostRxVoa_Type=FloatArbitraryPrecision
_IdlerPtpPmRealIdlerPostRxVoa_Object=MibTableColumn
idlerPtpPmRealIdlerPostRxVoa=_IdlerPtpPmRealIdlerPostRxVoa_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1,1,3),_IdlerPtpPmRealIdlerPostRxVoa_Type())
idlerPtpPmRealIdlerPostRxVoa.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmRealIdlerPostRxVoa.setStatus(_A)
_IdlerPtpPmRealTotalLaserPwr_Type=FloatArbitraryPrecision
_IdlerPtpPmRealTotalLaserPwr_Object=MibTableColumn
idlerPtpPmRealTotalLaserPwr=_IdlerPtpPmRealTotalLaserPwr_Object((1,3,6,1,4,1,21296,2,2,2,3,85,1,1,4),_IdlerPtpPmRealTotalLaserPwr_Type())
idlerPtpPmRealTotalLaserPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmRealTotalLaserPwr.setStatus(_A)
_IdlerPtpPmTable_Object=MibTable
idlerPtpPmTable=_IdlerPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2))
if mibBuilder.loadTexts:idlerPtpPmTable.setStatus(_A)
_IdlerPtpPmEntry_Object=MibTableRow
idlerPtpPmEntry=_IdlerPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1))
idlerPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:idlerPtpPmEntry.setStatus(_A)
class _IdlerPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IdlerPtpPmTimestamp_Type.__name__=_F
_IdlerPtpPmTimestamp_Object=MibTableColumn
idlerPtpPmTimestamp=_IdlerPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,1),_IdlerPtpPmTimestamp_Type())
idlerPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:idlerPtpPmTimestamp.setStatus(_A)
class _IdlerPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_IdlerPtpPmSampleDuration_Type.__name__=_F
_IdlerPtpPmSampleDuration_Object=MibTableColumn
idlerPtpPmSampleDuration=_IdlerPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,2),_IdlerPtpPmSampleDuration_Type())
idlerPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:idlerPtpPmSampleDuration.setStatus(_A)
_IdlerPtpPmValidity_Type=TruthValue
_IdlerPtpPmValidity_Object=MibTableColumn
idlerPtpPmValidity=_IdlerPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,3),_IdlerPtpPmValidity_Type())
idlerPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmValidity.setStatus(_A)
_IdlerPtpPmIdlerOptMin_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOptMin_Object=MibTableColumn
idlerPtpPmIdlerOptMin=_IdlerPtpPmIdlerOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,4),_IdlerPtpPmIdlerOptMin_Type())
idlerPtpPmIdlerOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOptMin.setStatus(_A)
_IdlerPtpPmIdlerOptMax_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOptMax_Object=MibTableColumn
idlerPtpPmIdlerOptMax=_IdlerPtpPmIdlerOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,5),_IdlerPtpPmIdlerOptMax_Type())
idlerPtpPmIdlerOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOptMax.setStatus(_A)
_IdlerPtpPmIdlerOptAve_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOptAve_Object=MibTableColumn
idlerPtpPmIdlerOptAve=_IdlerPtpPmIdlerOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,6),_IdlerPtpPmIdlerOptAve_Type())
idlerPtpPmIdlerOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOptAve.setStatus(_A)
_IdlerPtpPmIdlerOprMin_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOprMin_Object=MibTableColumn
idlerPtpPmIdlerOprMin=_IdlerPtpPmIdlerOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,7),_IdlerPtpPmIdlerOprMin_Type())
idlerPtpPmIdlerOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOprMin.setStatus(_A)
_IdlerPtpPmIdlerOprMax_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOprMax_Object=MibTableColumn
idlerPtpPmIdlerOprMax=_IdlerPtpPmIdlerOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,8),_IdlerPtpPmIdlerOprMax_Type())
idlerPtpPmIdlerOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOprMax.setStatus(_A)
_IdlerPtpPmIdlerOprAve_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerOprAve_Object=MibTableColumn
idlerPtpPmIdlerOprAve=_IdlerPtpPmIdlerOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,9),_IdlerPtpPmIdlerOprAve_Type())
idlerPtpPmIdlerOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerOprAve.setStatus(_A)
_IdlerPtpPmIdlerPostRxVoaMin_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaMin_Object=MibTableColumn
idlerPtpPmIdlerPostRxVoaMin=_IdlerPtpPmIdlerPostRxVoaMin_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,10),_IdlerPtpPmIdlerPostRxVoaMin_Type())
idlerPtpPmIdlerPostRxVoaMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerPostRxVoaMin.setStatus(_A)
_IdlerPtpPmIdlerPostRxVoaMax_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaMax_Object=MibTableColumn
idlerPtpPmIdlerPostRxVoaMax=_IdlerPtpPmIdlerPostRxVoaMax_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,11),_IdlerPtpPmIdlerPostRxVoaMax_Type())
idlerPtpPmIdlerPostRxVoaMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerPostRxVoaMax.setStatus(_A)
_IdlerPtpPmIdlerPostRxVoaAve_Type=FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaAve_Object=MibTableColumn
idlerPtpPmIdlerPostRxVoaAve=_IdlerPtpPmIdlerPostRxVoaAve_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,12),_IdlerPtpPmIdlerPostRxVoaAve_Type())
idlerPtpPmIdlerPostRxVoaAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmIdlerPostRxVoaAve.setStatus(_A)
_IdlerPtpPmTotalLaserPwrMin_Type=FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrMin_Object=MibTableColumn
idlerPtpPmTotalLaserPwrMin=_IdlerPtpPmTotalLaserPwrMin_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,13),_IdlerPtpPmTotalLaserPwrMin_Type())
idlerPtpPmTotalLaserPwrMin.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmTotalLaserPwrMin.setStatus(_A)
_IdlerPtpPmTotalLaserPwrMax_Type=FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrMax_Object=MibTableColumn
idlerPtpPmTotalLaserPwrMax=_IdlerPtpPmTotalLaserPwrMax_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,14),_IdlerPtpPmTotalLaserPwrMax_Type())
idlerPtpPmTotalLaserPwrMax.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmTotalLaserPwrMax.setStatus(_A)
_IdlerPtpPmTotalLaserPwrAve_Type=FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrAve_Object=MibTableColumn
idlerPtpPmTotalLaserPwrAve=_IdlerPtpPmTotalLaserPwrAve_Object((1,3,6,1,4,1,21296,2,2,2,3,85,2,1,15),_IdlerPtpPmTotalLaserPwrAve_Type())
idlerPtpPmTotalLaserPwrAve.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmTotalLaserPwrAve.setStatus(_A)
_IdlerPtpPmConformance_ObjectIdentity=ObjectIdentity
idlerPtpPmConformance=_IdlerPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,85,3))
_IdlerPtpPmCompliances_ObjectIdentity=ObjectIdentity
idlerPtpPmCompliances=_IdlerPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,85,3,1))
_IdlerPtpPmGroups_ObjectIdentity=ObjectIdentity
idlerPtpPmGroups=_IdlerPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,85,3,2))
idlerPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,85,3,2,1))
idlerPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:idlerPtpPmGroup.setStatus(_A)
idlerPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,85,3,2,2))
idlerPtpPmRealGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:idlerPtpPmRealGroup.setStatus(_A)
idlerPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,85,3,1,1))
idlerPtpPmCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:idlerPtpPmCompliance.setStatus(_A)
idlerPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,85,3,1,2))
idlerPtpPmRealCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:idlerPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'idlerPtpPmMIB':idlerPtpPmMIB,'idlerPtpPmRealTable':idlerPtpPmRealTable,'idlerPtpPmRealEntry':idlerPtpPmRealEntry,_W:idlerPtpPmRealIdlerOpt,_X:idlerPtpPmRealIdlerOpr,_Y:idlerPtpPmRealIdlerPostRxVoa,_Z:idlerPtpPmRealTotalLaserPwr,'idlerPtpPmTable':idlerPtpPmTable,'idlerPtpPmEntry':idlerPtpPmEntry,_H:idlerPtpPmTimestamp,_G:idlerPtpPmSampleDuration,_J:idlerPtpPmValidity,_K:idlerPtpPmIdlerOptMin,_L:idlerPtpPmIdlerOptMax,_M:idlerPtpPmIdlerOptAve,_N:idlerPtpPmIdlerOprMin,_O:idlerPtpPmIdlerOprMax,_P:idlerPtpPmIdlerOprAve,_Q:idlerPtpPmIdlerPostRxVoaMin,_R:idlerPtpPmIdlerPostRxVoaMax,_S:idlerPtpPmIdlerPostRxVoaAve,_T:idlerPtpPmTotalLaserPwrMin,_U:idlerPtpPmTotalLaserPwrMax,_V:idlerPtpPmTotalLaserPwrAve,'idlerPtpPmConformance':idlerPtpPmConformance,'idlerPtpPmCompliances':idlerPtpPmCompliances,'idlerPtpPmCompliance':idlerPtpPmCompliance,'idlerPtpPmRealCompliance':idlerPtpPmRealCompliance,'idlerPtpPmGroups':idlerPtpPmGroups,_a:idlerPtpPmGroup,_b:idlerPtpPmRealGroup})