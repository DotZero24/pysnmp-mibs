_s='pdnQuadModeGroup'
_r='pdnLoopLengthModeGroup'
_q='pdnEWLModeGroup'
_p='pdnLineInfoGroup'
_o='pdnGeneralConfigGroup'
_n='spectrumMgmtAllowedSpeedsMax2'
_m='spectrumMgmtAllowedSpeedsMin2'
_l='spectrumMgmtAllowedSpeedsMax1'
_k='spectrumMgmtAllowedSpeedsMin1'
_j='spectrumMgmtLineLength'
_i='spectrumMgmtEWL'
_h='spectrumMgmtCountryCode'
_g='newSpectrumMgmtConfQuadMode'
_f='newSpectrumMgmtConfLoopLength'
_e='newSpectrumMgmtConfEWL'
_d='newSpectrumMgmtXturMaxTxPower'
_c='newSpectrumMgmtXturMin2TxRate'
_b='newSpectrumMgmtXturMax2TxRate'
_a='newSpectrumMgmtXturMin1TxRate'
_Z='newSpectrumMgmtXturMax1TxRate'
_Y='newSpectrumMgmtXtucMaxTxPower'
_X='newSpectrumMgmtXtucMin2TxRate'
_W='newSpectrumMgmtXtucMax2TxRate'
_V='newSpectrumMgmtXtucMin1TxRate'
_U='newSpectrumMgmtXtucMax1TxRate'
_T='newSpectrumMgmtEWLUnits'
_S='newSpectrumMgmtLoopMeasurementMethod'
_R='newSpectrumMgmtMode'
_Q='newSpectrumMgmtSelection'
_P='tenth dB'
_O='medium'
_N='ifType'
_M='entPhysicalIndex'
_L='ENTITY-MIB'
_K='newSpectrumMgmtMaxEWL'
_J='newSpectrumMgmtMinEWL'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='bps'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='PDN-SPECTRUMMGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_L,_M)
ifIndex,ifType=mibBuilder.importSymbols(_H,_I,_N)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnSpectrumMgmt=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,19))
if mibBuilder.loadTexts:pdnSpectrumMgmt.setRevisions(('2003-01-15 13:00','2003-01-09 15:00','1901-05-16 15:30','1901-05-08 05:50'))
_PdnSpecMgmtObjects_ObjectIdentity=ObjectIdentity
pdnSpecMgmtObjects=_PdnSpecMgmtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,19,1))
class _SpectrumMgmtCountryCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usa',1),('uk',2)))
_SpectrumMgmtCountryCode_Type.__name__=_D
_SpectrumMgmtCountryCode_Object=MibScalar
spectrumMgmtCountryCode=_SpectrumMgmtCountryCode_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,2),_SpectrumMgmtCountryCode_Type())
spectrumMgmtCountryCode.setMaxAccess(_G)
if mibBuilder.loadTexts:spectrumMgmtCountryCode.setStatus(_E)
_SpectrumMgmtTable_Object=MibTable
spectrumMgmtTable=_SpectrumMgmtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3))
if mibBuilder.loadTexts:spectrumMgmtTable.setStatus(_E)
_SpectrumMgmtEntry_Object=MibTableRow
spectrumMgmtEntry=_SpectrumMgmtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1))
spectrumMgmtEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:spectrumMgmtEntry.setStatus(_E)
_SpectrumMgmtEWL_Type=Integer32
_SpectrumMgmtEWL_Object=MibTableColumn
spectrumMgmtEWL=_SpectrumMgmtEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,1),_SpectrumMgmtEWL_Type())
spectrumMgmtEWL.setMaxAccess(_G)
if mibBuilder.loadTexts:spectrumMgmtEWL.setStatus(_E)
_SpectrumMgmtAllowedSpeedsMin1_Type=Integer32
_SpectrumMgmtAllowedSpeedsMin1_Object=MibTableColumn
spectrumMgmtAllowedSpeedsMin1=_SpectrumMgmtAllowedSpeedsMin1_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,2),_SpectrumMgmtAllowedSpeedsMin1_Type())
spectrumMgmtAllowedSpeedsMin1.setMaxAccess(_C)
if mibBuilder.loadTexts:spectrumMgmtAllowedSpeedsMin1.setStatus(_E)
_SpectrumMgmtAllowedSpeedsMax1_Type=Integer32
_SpectrumMgmtAllowedSpeedsMax1_Object=MibTableColumn
spectrumMgmtAllowedSpeedsMax1=_SpectrumMgmtAllowedSpeedsMax1_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,3),_SpectrumMgmtAllowedSpeedsMax1_Type())
spectrumMgmtAllowedSpeedsMax1.setMaxAccess(_C)
if mibBuilder.loadTexts:spectrumMgmtAllowedSpeedsMax1.setStatus(_E)
_SpectrumMgmtAllowedSpeedsMin2_Type=Integer32
_SpectrumMgmtAllowedSpeedsMin2_Object=MibTableColumn
spectrumMgmtAllowedSpeedsMin2=_SpectrumMgmtAllowedSpeedsMin2_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,4),_SpectrumMgmtAllowedSpeedsMin2_Type())
spectrumMgmtAllowedSpeedsMin2.setMaxAccess(_C)
if mibBuilder.loadTexts:spectrumMgmtAllowedSpeedsMin2.setStatus(_E)
_SpectrumMgmtAllowedSpeedsMax2_Type=Integer32
_SpectrumMgmtAllowedSpeedsMax2_Object=MibTableColumn
spectrumMgmtAllowedSpeedsMax2=_SpectrumMgmtAllowedSpeedsMax2_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,5),_SpectrumMgmtAllowedSpeedsMax2_Type())
spectrumMgmtAllowedSpeedsMax2.setMaxAccess(_C)
if mibBuilder.loadTexts:spectrumMgmtAllowedSpeedsMax2.setStatus(_E)
class _SpectrumMgmtLineLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('short',1),(_O,2),('long',3)))
_SpectrumMgmtLineLength_Type.__name__=_D
_SpectrumMgmtLineLength_Object=MibTableColumn
spectrumMgmtLineLength=_SpectrumMgmtLineLength_Object((1,3,6,1,4,1,1795,2,24,2,6,19,1,3,1,6),_SpectrumMgmtLineLength_Type())
spectrumMgmtLineLength.setMaxAccess(_G)
if mibBuilder.loadTexts:spectrumMgmtLineLength.setStatus(_E)
_PdnNewSpecMgmtObjects_ObjectIdentity=ObjectIdentity
pdnNewSpecMgmtObjects=_PdnNewSpecMgmtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,19,2))
_NewSpectrumMgmtGeneralConfigTable_Object=MibTable
newSpectrumMgmtGeneralConfigTable=_NewSpectrumMgmtGeneralConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1))
if mibBuilder.loadTexts:newSpectrumMgmtGeneralConfigTable.setStatus(_B)
_NewSpectrumMgmtGeneralConfigEntry_Object=MibTableRow
newSpectrumMgmtGeneralConfigEntry=_NewSpectrumMgmtGeneralConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1,1))
newSpectrumMgmtGeneralConfigEntry.setIndexNames((0,_L,_M),(0,_H,_N))
if mibBuilder.loadTexts:newSpectrumMgmtGeneralConfigEntry.setStatus(_B)
class _NewSpectrumMgmtSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NewSpectrumMgmtSelection_Type.__name__=_D
_NewSpectrumMgmtSelection_Object=MibTableColumn
newSpectrumMgmtSelection=_NewSpectrumMgmtSelection_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1,1,1),_NewSpectrumMgmtSelection_Type())
newSpectrumMgmtSelection.setMaxAccess(_G)
if mibBuilder.loadTexts:newSpectrumMgmtSelection.setStatus(_B)
class _NewSpectrumMgmtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enableOnly',1),('disableOnly',2),('both',3)))
_NewSpectrumMgmtMode_Type.__name__=_D
_NewSpectrumMgmtMode_Object=MibTableColumn
newSpectrumMgmtMode=_NewSpectrumMgmtMode_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1,1,2),_NewSpectrumMgmtMode_Type())
newSpectrumMgmtMode.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtMode.setStatus(_B)
class _NewSpectrumMgmtLoopMeasurementMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('loopLength',2),('ewl',3),('quadMode',4)))
_NewSpectrumMgmtLoopMeasurementMethod_Type.__name__=_D
_NewSpectrumMgmtLoopMeasurementMethod_Object=MibTableColumn
newSpectrumMgmtLoopMeasurementMethod=_NewSpectrumMgmtLoopMeasurementMethod_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1,1,3),_NewSpectrumMgmtLoopMeasurementMethod_Type())
newSpectrumMgmtLoopMeasurementMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtLoopMeasurementMethod.setStatus(_B)
class _NewSpectrumMgmtEWLUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('feet',2),('meters',3)))
_NewSpectrumMgmtEWLUnits_Type.__name__=_D
_NewSpectrumMgmtEWLUnits_Object=MibTableColumn
newSpectrumMgmtEWLUnits=_NewSpectrumMgmtEWLUnits_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,1,1,4),_NewSpectrumMgmtEWLUnits_Type())
newSpectrumMgmtEWLUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtEWLUnits.setStatus(_B)
_NewSpectrumMgmtConfTable_Object=MibTable
newSpectrumMgmtConfTable=_NewSpectrumMgmtConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,2))
if mibBuilder.loadTexts:newSpectrumMgmtConfTable.setStatus(_B)
_NewSpectrumMgmtConfEntry_Object=MibTableRow
newSpectrumMgmtConfEntry=_NewSpectrumMgmtConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,2,1))
newSpectrumMgmtConfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:newSpectrumMgmtConfEntry.setStatus(_B)
_NewSpectrumMgmtConfEWL_Type=Unsigned32
_NewSpectrumMgmtConfEWL_Object=MibTableColumn
newSpectrumMgmtConfEWL=_NewSpectrumMgmtConfEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,2,1,1),_NewSpectrumMgmtConfEWL_Type())
newSpectrumMgmtConfEWL.setMaxAccess(_G)
if mibBuilder.loadTexts:newSpectrumMgmtConfEWL.setStatus(_B)
class _NewSpectrumMgmtConfLoopLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('short',1),(_O,2),('long',3)))
_NewSpectrumMgmtConfLoopLength_Type.__name__=_D
_NewSpectrumMgmtConfLoopLength_Object=MibTableColumn
newSpectrumMgmtConfLoopLength=_NewSpectrumMgmtConfLoopLength_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,2,1,2),_NewSpectrumMgmtConfLoopLength_Type())
newSpectrumMgmtConfLoopLength.setMaxAccess(_G)
if mibBuilder.loadTexts:newSpectrumMgmtConfLoopLength.setStatus(_B)
class _NewSpectrumMgmtConfQuadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sameQuad',1),('segregatedQuadUpto3km',2),('segregatedQuadAbove3km',3)))
_NewSpectrumMgmtConfQuadMode_Type.__name__=_D
_NewSpectrumMgmtConfQuadMode_Object=MibTableColumn
newSpectrumMgmtConfQuadMode=_NewSpectrumMgmtConfQuadMode_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,2,1,3),_NewSpectrumMgmtConfQuadMode_Type())
newSpectrumMgmtConfQuadMode.setMaxAccess(_G)
if mibBuilder.loadTexts:newSpectrumMgmtConfQuadMode.setStatus(_B)
_NewSpectrumMgmtLineInfoTable_Object=MibTable
newSpectrumMgmtLineInfoTable=_NewSpectrumMgmtLineInfoTable_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3))
if mibBuilder.loadTexts:newSpectrumMgmtLineInfoTable.setStatus(_B)
_NewSpectrumMgmtLineInfoEntry_Object=MibTableRow
newSpectrumMgmtLineInfoEntry=_NewSpectrumMgmtLineInfoEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1))
newSpectrumMgmtLineInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:newSpectrumMgmtLineInfoEntry.setStatus(_B)
_NewSpectrumMgmtXtucMax1TxRate_Type=Unsigned32
_NewSpectrumMgmtXtucMax1TxRate_Object=MibTableColumn
newSpectrumMgmtXtucMax1TxRate=_NewSpectrumMgmtXtucMax1TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,1),_NewSpectrumMgmtXtucMax1TxRate_Type())
newSpectrumMgmtXtucMax1TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMax1TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMax1TxRate.setUnits(_F)
_NewSpectrumMgmtXtucMin1TxRate_Type=Unsigned32
_NewSpectrumMgmtXtucMin1TxRate_Object=MibTableColumn
newSpectrumMgmtXtucMin1TxRate=_NewSpectrumMgmtXtucMin1TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,2),_NewSpectrumMgmtXtucMin1TxRate_Type())
newSpectrumMgmtXtucMin1TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMin1TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMin1TxRate.setUnits(_F)
_NewSpectrumMgmtXtucMax2TxRate_Type=Unsigned32
_NewSpectrumMgmtXtucMax2TxRate_Object=MibTableColumn
newSpectrumMgmtXtucMax2TxRate=_NewSpectrumMgmtXtucMax2TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,3),_NewSpectrumMgmtXtucMax2TxRate_Type())
newSpectrumMgmtXtucMax2TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMax2TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMax2TxRate.setUnits(_F)
_NewSpectrumMgmtXtucMin2TxRate_Type=Unsigned32
_NewSpectrumMgmtXtucMin2TxRate_Object=MibTableColumn
newSpectrumMgmtXtucMin2TxRate=_NewSpectrumMgmtXtucMin2TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,4),_NewSpectrumMgmtXtucMin2TxRate_Type())
newSpectrumMgmtXtucMin2TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMin2TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMin2TxRate.setUnits(_F)
class _NewSpectrumMgmtXtucMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_NewSpectrumMgmtXtucMaxTxPower_Type.__name__=_D
_NewSpectrumMgmtXtucMaxTxPower_Object=MibTableColumn
newSpectrumMgmtXtucMaxTxPower=_NewSpectrumMgmtXtucMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,5),_NewSpectrumMgmtXtucMaxTxPower_Type())
newSpectrumMgmtXtucMaxTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXtucMaxTxPower.setUnits(_P)
_NewSpectrumMgmtXturMax1TxRate_Type=Unsigned32
_NewSpectrumMgmtXturMax1TxRate_Object=MibTableColumn
newSpectrumMgmtXturMax1TxRate=_NewSpectrumMgmtXturMax1TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,6),_NewSpectrumMgmtXturMax1TxRate_Type())
newSpectrumMgmtXturMax1TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXturMax1TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXturMax1TxRate.setUnits(_F)
_NewSpectrumMgmtXturMin1TxRate_Type=Unsigned32
_NewSpectrumMgmtXturMin1TxRate_Object=MibTableColumn
newSpectrumMgmtXturMin1TxRate=_NewSpectrumMgmtXturMin1TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,7),_NewSpectrumMgmtXturMin1TxRate_Type())
newSpectrumMgmtXturMin1TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXturMin1TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXturMin1TxRate.setUnits(_F)
_NewSpectrumMgmtXturMax2TxRate_Type=Unsigned32
_NewSpectrumMgmtXturMax2TxRate_Object=MibTableColumn
newSpectrumMgmtXturMax2TxRate=_NewSpectrumMgmtXturMax2TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,8),_NewSpectrumMgmtXturMax2TxRate_Type())
newSpectrumMgmtXturMax2TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXturMax2TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXturMax2TxRate.setUnits(_F)
_NewSpectrumMgmtXturMin2TxRate_Type=Unsigned32
_NewSpectrumMgmtXturMin2TxRate_Object=MibTableColumn
newSpectrumMgmtXturMin2TxRate=_NewSpectrumMgmtXturMin2TxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,9),_NewSpectrumMgmtXturMin2TxRate_Type())
newSpectrumMgmtXturMin2TxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXturMin2TxRate.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXturMin2TxRate.setUnits(_F)
class _NewSpectrumMgmtXturMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_NewSpectrumMgmtXturMaxTxPower_Type.__name__=_D
_NewSpectrumMgmtXturMaxTxPower_Object=MibTableColumn
newSpectrumMgmtXturMaxTxPower=_NewSpectrumMgmtXturMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,10),_NewSpectrumMgmtXturMaxTxPower_Type())
newSpectrumMgmtXturMaxTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtXturMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:newSpectrumMgmtXturMaxTxPower.setUnits(_P)
_NewSpectrumMgmtMinEWL_Type=Unsigned32
_NewSpectrumMgmtMinEWL_Object=MibTableColumn
newSpectrumMgmtMinEWL=_NewSpectrumMgmtMinEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,11),_NewSpectrumMgmtMinEWL_Type())
newSpectrumMgmtMinEWL.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtMinEWL.setStatus(_B)
_NewSpectrumMgmtMaxEWL_Type=Unsigned32
_NewSpectrumMgmtMaxEWL_Object=MibTableColumn
newSpectrumMgmtMaxEWL=_NewSpectrumMgmtMaxEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,19,2,3,1,12),_NewSpectrumMgmtMaxEWL_Type())
newSpectrumMgmtMaxEWL.setMaxAccess(_C)
if mibBuilder.loadTexts:newSpectrumMgmtMaxEWL.setStatus(_B)
_PdnSpecMgmtConformance_ObjectIdentity=ObjectIdentity
pdnSpecMgmtConformance=_PdnSpecMgmtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,19,3))
_PdnSpecMgmtGroups_ObjectIdentity=ObjectIdentity
pdnSpecMgmtGroups=_PdnSpecMgmtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,19,3,1))
_PdnSpecMgmtCompliances_ObjectIdentity=ObjectIdentity
pdnSpecMgmtCompliances=_PdnSpecMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,19,3,2))
pdnGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,1))
pdnGeneralConfigGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:pdnGeneralConfigGroup.setStatus(_B)
pdnLineInfoGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,2))
pdnLineInfoGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:pdnLineInfoGroup.setStatus(_B)
pdnEWLModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,3))
pdnEWLModeGroup.setObjects(*((_A,_e),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:pdnEWLModeGroup.setStatus(_B)
pdnLoopLengthModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,4))
pdnLoopLengthModeGroup.setObjects((_A,_f))
if mibBuilder.loadTexts:pdnLoopLengthModeGroup.setStatus(_B)
pdnQuadModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,5))
pdnQuadModeGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:pdnQuadModeGroup.setStatus(_B)
pdnSpectrumMgmtDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,19,3,1,7))
pdnSpectrumMgmtDeprecatedGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:pdnSpectrumMgmtDeprecatedGroup.setStatus(_E)
pdnSpecMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,19,3,2,1))
pdnSpecMgmtCompliance.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:pdnSpecMgmtCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pdnSpectrumMgmt':pdnSpectrumMgmt,'pdnSpecMgmtObjects':pdnSpecMgmtObjects,_h:spectrumMgmtCountryCode,'spectrumMgmtTable':spectrumMgmtTable,'spectrumMgmtEntry':spectrumMgmtEntry,_i:spectrumMgmtEWL,_k:spectrumMgmtAllowedSpeedsMin1,_l:spectrumMgmtAllowedSpeedsMax1,_m:spectrumMgmtAllowedSpeedsMin2,_n:spectrumMgmtAllowedSpeedsMax2,_j:spectrumMgmtLineLength,'pdnNewSpecMgmtObjects':pdnNewSpecMgmtObjects,'newSpectrumMgmtGeneralConfigTable':newSpectrumMgmtGeneralConfigTable,'newSpectrumMgmtGeneralConfigEntry':newSpectrumMgmtGeneralConfigEntry,_Q:newSpectrumMgmtSelection,_R:newSpectrumMgmtMode,_S:newSpectrumMgmtLoopMeasurementMethod,_T:newSpectrumMgmtEWLUnits,'newSpectrumMgmtConfTable':newSpectrumMgmtConfTable,'newSpectrumMgmtConfEntry':newSpectrumMgmtConfEntry,_e:newSpectrumMgmtConfEWL,_f:newSpectrumMgmtConfLoopLength,_g:newSpectrumMgmtConfQuadMode,'newSpectrumMgmtLineInfoTable':newSpectrumMgmtLineInfoTable,'newSpectrumMgmtLineInfoEntry':newSpectrumMgmtLineInfoEntry,_U:newSpectrumMgmtXtucMax1TxRate,_V:newSpectrumMgmtXtucMin1TxRate,_W:newSpectrumMgmtXtucMax2TxRate,_X:newSpectrumMgmtXtucMin2TxRate,_Y:newSpectrumMgmtXtucMaxTxPower,_Z:newSpectrumMgmtXturMax1TxRate,_a:newSpectrumMgmtXturMin1TxRate,_b:newSpectrumMgmtXturMax2TxRate,_c:newSpectrumMgmtXturMin2TxRate,_d:newSpectrumMgmtXturMaxTxPower,_J:newSpectrumMgmtMinEWL,_K:newSpectrumMgmtMaxEWL,'pdnSpecMgmtConformance':pdnSpecMgmtConformance,'pdnSpecMgmtGroups':pdnSpecMgmtGroups,_o:pdnGeneralConfigGroup,_p:pdnLineInfoGroup,_q:pdnEWLModeGroup,_r:pdnLoopLengthModeGroup,_s:pdnQuadModeGroup,'pdnSpectrumMgmtDeprecatedGroup':pdnSpectrumMgmtDeprecatedGroup,'pdnSpecMgmtCompliances':pdnSpecMgmtCompliances,'pdnSpecMgmtCompliance':pdnSpecMgmtCompliance})