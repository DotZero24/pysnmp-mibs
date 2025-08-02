_l='pdnReachDSLQuadModeGroup'
_k='pdnReachDSLLoopLengthModeGroup'
_j='pdnReachDSLEWLModeGroup'
_i='pdnReachDSLGeneralInformationGroup'
_h='pdnReachDSLGeneralConfigGroup'
_g='pdnReachDSLInformationGroup'
_f='pdnReachDSLConfigurationGroup'
_e='reachDSLSpectrumMgmtConfQuadMode'
_d='reachDSLSpectrumMgmtZone'
_c='DisplayString'
_b='reachDSLSpectrumMgmtMode'
_a='reachDSLSpectrumMgmtEWLUnits'
_Z='reachDSLSpectrumMgmtLoopMeasurementMethod'
_Y='reachDSLSpectrumMgmtMaxEWL'
_X='reachDSLSpectrumMgmtMinEWL'
_W='reachDSLSpectrumMgmtAturMaxTxPower'
_V='reachDSLSpectrumMgmtAturMinTxRate'
_U='reachDSLSpectrumMgmtAturMaxTxRate'
_T='reachDSLSpectrumMgmtAtucMaxTxPower'
_S='reachDSLSpectrumMgmtAtucMinTxRate'
_R='reachDSLSpectrumMgmtAtucMaxTxRate'
_Q='reachDSLCircuitIdentifier'
_P='reachDSLPotsDetectionVoltage'
_O='reachDSLSpectrumMgmtConfAturMaxTxPower'
_N='reachDSLSpectrumMgmtConfAtucMaxTxPower'
_M='reachDSLSpectrumMgmtConfLoopLength'
_L='reachDSLSpectrumMgmtConfEWL'
_K='reachDSLSpectrumMgmtSelection'
_J='bps'
_I='tenth dB'
_H='ifIndex'
_G='IF-MIB'
_F='deprecated'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='current'
_A='PDN-REACHDSL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_c,'PhysAddress','TextualConvention')
pdnReachDSL=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,20))
if mibBuilder.loadTexts:pdnReachDSL.setRevisions(('2003-01-15 12:00','2003-01-12 12:00','2002-10-15 17:00','2002-07-12 03:15'))
_PdnReachDSLObjects_ObjectIdentity=ObjectIdentity
pdnReachDSLObjects=_PdnReachDSLObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,20,1))
class _ReachDSLSpectrumMgmtSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ReachDSLSpectrumMgmtSelection_Type.__name__=_C
_ReachDSLSpectrumMgmtSelection_Object=MibScalar
reachDSLSpectrumMgmtSelection=_ReachDSLSpectrumMgmtSelection_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,1),_ReachDSLSpectrumMgmtSelection_Type())
reachDSLSpectrumMgmtSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtSelection.setStatus(_B)
class _ReachDSLSpectrumMgmtZone_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('usa1',1),('uk1',2),('canada1',3),('japan1',4),('emea1',5)))
_ReachDSLSpectrumMgmtZone_Type.__name__=_C
_ReachDSLSpectrumMgmtZone_Object=MibScalar
reachDSLSpectrumMgmtZone=_ReachDSLSpectrumMgmtZone_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,2),_ReachDSLSpectrumMgmtZone_Type())
reachDSLSpectrumMgmtZone.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtZone.setStatus(_F)
_ReachDSLSpectrumMgmtConfTable_Object=MibTable
reachDSLSpectrumMgmtConfTable=_ReachDSLSpectrumMgmtConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3))
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfTable.setStatus(_B)
_ReachDSLSpectrumMgmtConfEntry_Object=MibTableRow
reachDSLSpectrumMgmtConfEntry=_ReachDSLSpectrumMgmtConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1))
reachDSLSpectrumMgmtConfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfEntry.setStatus(_B)
_ReachDSLSpectrumMgmtConfEWL_Type=Unsigned32
_ReachDSLSpectrumMgmtConfEWL_Object=MibTableColumn
reachDSLSpectrumMgmtConfEWL=_ReachDSLSpectrumMgmtConfEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1,1),_ReachDSLSpectrumMgmtConfEWL_Type())
reachDSLSpectrumMgmtConfEWL.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfEWL.setStatus(_B)
class _ReachDSLSpectrumMgmtConfLoopLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('short',1),('medium',2),('long',3)))
_ReachDSLSpectrumMgmtConfLoopLength_Type.__name__=_C
_ReachDSLSpectrumMgmtConfLoopLength_Object=MibTableColumn
reachDSLSpectrumMgmtConfLoopLength=_ReachDSLSpectrumMgmtConfLoopLength_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1,2),_ReachDSLSpectrumMgmtConfLoopLength_Type())
reachDSLSpectrumMgmtConfLoopLength.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfLoopLength.setStatus(_B)
class _ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type.__name__=_C
_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Object=MibTableColumn
reachDSLSpectrumMgmtConfAtucMaxTxPower=_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1,3),_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type())
reachDSLSpectrumMgmtConfAtucMaxTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfAtucMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfAtucMaxTxPower.setUnits(_I)
class _ReachDSLSpectrumMgmtConfAturMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_ReachDSLSpectrumMgmtConfAturMaxTxPower_Type.__name__=_C
_ReachDSLSpectrumMgmtConfAturMaxTxPower_Object=MibTableColumn
reachDSLSpectrumMgmtConfAturMaxTxPower=_ReachDSLSpectrumMgmtConfAturMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1,4),_ReachDSLSpectrumMgmtConfAturMaxTxPower_Type())
reachDSLSpectrumMgmtConfAturMaxTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfAturMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfAturMaxTxPower.setUnits(_I)
class _ReachDSLSpectrumMgmtConfQuadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sameQuad',1),('segregatedQuadUpto3km',2),('segregatedQuadAbove3km',3)))
_ReachDSLSpectrumMgmtConfQuadMode_Type.__name__=_C
_ReachDSLSpectrumMgmtConfQuadMode_Object=MibTableColumn
reachDSLSpectrumMgmtConfQuadMode=_ReachDSLSpectrumMgmtConfQuadMode_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,3,1,5),_ReachDSLSpectrumMgmtConfQuadMode_Type())
reachDSLSpectrumMgmtConfQuadMode.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtConfQuadMode.setStatus(_B)
_ReachDSLSpectrumMgmtLineInfoTable_Object=MibTable
reachDSLSpectrumMgmtLineInfoTable=_ReachDSLSpectrumMgmtLineInfoTable_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4))
if mibBuilder.loadTexts:reachDSLSpectrumMgmtLineInfoTable.setStatus(_B)
_ReachDSLSpectrumMgmtLineInfoEntry_Object=MibTableRow
reachDSLSpectrumMgmtLineInfoEntry=_ReachDSLSpectrumMgmtLineInfoEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1))
reachDSLSpectrumMgmtLineInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:reachDSLSpectrumMgmtLineInfoEntry.setStatus(_B)
_ReachDSLSpectrumMgmtAtucMaxTxRate_Type=Unsigned32
_ReachDSLSpectrumMgmtAtucMaxTxRate_Object=MibTableColumn
reachDSLSpectrumMgmtAtucMaxTxRate=_ReachDSLSpectrumMgmtAtucMaxTxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,1),_ReachDSLSpectrumMgmtAtucMaxTxRate_Type())
reachDSLSpectrumMgmtAtucMaxTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMaxTxRate.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMaxTxRate.setUnits(_J)
_ReachDSLSpectrumMgmtAtucMinTxRate_Type=Unsigned32
_ReachDSLSpectrumMgmtAtucMinTxRate_Object=MibTableColumn
reachDSLSpectrumMgmtAtucMinTxRate=_ReachDSLSpectrumMgmtAtucMinTxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,2),_ReachDSLSpectrumMgmtAtucMinTxRate_Type())
reachDSLSpectrumMgmtAtucMinTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMinTxRate.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMinTxRate.setUnits(_J)
class _ReachDSLSpectrumMgmtAtucMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_ReachDSLSpectrumMgmtAtucMaxTxPower_Type.__name__=_C
_ReachDSLSpectrumMgmtAtucMaxTxPower_Object=MibTableColumn
reachDSLSpectrumMgmtAtucMaxTxPower=_ReachDSLSpectrumMgmtAtucMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,3),_ReachDSLSpectrumMgmtAtucMaxTxPower_Type())
reachDSLSpectrumMgmtAtucMaxTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAtucMaxTxPower.setUnits(_I)
_ReachDSLSpectrumMgmtAturMaxTxRate_Type=Unsigned32
_ReachDSLSpectrumMgmtAturMaxTxRate_Object=MibTableColumn
reachDSLSpectrumMgmtAturMaxTxRate=_ReachDSLSpectrumMgmtAturMaxTxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,4),_ReachDSLSpectrumMgmtAturMaxTxRate_Type())
reachDSLSpectrumMgmtAturMaxTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMaxTxRate.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMaxTxRate.setUnits(_J)
_ReachDSLSpectrumMgmtAturMinTxRate_Type=Unsigned32
_ReachDSLSpectrumMgmtAturMinTxRate_Object=MibTableColumn
reachDSLSpectrumMgmtAturMinTxRate=_ReachDSLSpectrumMgmtAturMinTxRate_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,5),_ReachDSLSpectrumMgmtAturMinTxRate_Type())
reachDSLSpectrumMgmtAturMinTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMinTxRate.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMinTxRate.setUnits(_J)
class _ReachDSLSpectrumMgmtAturMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,120))
_ReachDSLSpectrumMgmtAturMaxTxPower_Type.__name__=_C
_ReachDSLSpectrumMgmtAturMaxTxPower_Object=MibTableColumn
reachDSLSpectrumMgmtAturMaxTxPower=_ReachDSLSpectrumMgmtAturMaxTxPower_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,6),_ReachDSLSpectrumMgmtAturMaxTxPower_Type())
reachDSLSpectrumMgmtAturMaxTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMaxTxPower.setStatus(_B)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtAturMaxTxPower.setUnits(_I)
_ReachDSLSpectrumMgmtMinEWL_Type=Unsigned32
_ReachDSLSpectrumMgmtMinEWL_Object=MibTableColumn
reachDSLSpectrumMgmtMinEWL=_ReachDSLSpectrumMgmtMinEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,7),_ReachDSLSpectrumMgmtMinEWL_Type())
reachDSLSpectrumMgmtMinEWL.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtMinEWL.setStatus(_B)
_ReachDSLSpectrumMgmtMaxEWL_Type=Unsigned32
_ReachDSLSpectrumMgmtMaxEWL_Object=MibTableColumn
reachDSLSpectrumMgmtMaxEWL=_ReachDSLSpectrumMgmtMaxEWL_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,4,1,8),_ReachDSLSpectrumMgmtMaxEWL_Type())
reachDSLSpectrumMgmtMaxEWL.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtMaxEWL.setStatus(_B)
_ReachDSLLineTable_Object=MibTable
reachDSLLineTable=_ReachDSLLineTable_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,5))
if mibBuilder.loadTexts:reachDSLLineTable.setStatus(_B)
_ReachDSLLineEntry_Object=MibTableRow
reachDSLLineEntry=_ReachDSLLineEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,5,1))
reachDSLLineEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:reachDSLLineEntry.setStatus(_B)
class _ReachDSLPotsDetectionVoltage_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,74))
_ReachDSLPotsDetectionVoltage_Type.__name__=_C
_ReachDSLPotsDetectionVoltage_Object=MibTableColumn
reachDSLPotsDetectionVoltage=_ReachDSLPotsDetectionVoltage_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,5,1,1),_ReachDSLPotsDetectionVoltage_Type())
reachDSLPotsDetectionVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLPotsDetectionVoltage.setStatus(_B)
if mibBuilder.loadTexts:reachDSLPotsDetectionVoltage.setUnits('volts')
class _ReachDSLCircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ReachDSLCircuitIdentifier_Type.__name__=_c
_ReachDSLCircuitIdentifier_Object=MibTableColumn
reachDSLCircuitIdentifier=_ReachDSLCircuitIdentifier_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,5,1,2),_ReachDSLCircuitIdentifier_Type())
reachDSLCircuitIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:reachDSLCircuitIdentifier.setStatus(_F)
class _ReachDSLSpectrumMgmtLoopMeasurementMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('loopLength',2),('ewl',3),('quadMode',4)))
_ReachDSLSpectrumMgmtLoopMeasurementMethod_Type.__name__=_C
_ReachDSLSpectrumMgmtLoopMeasurementMethod_Object=MibScalar
reachDSLSpectrumMgmtLoopMeasurementMethod=_ReachDSLSpectrumMgmtLoopMeasurementMethod_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,6),_ReachDSLSpectrumMgmtLoopMeasurementMethod_Type())
reachDSLSpectrumMgmtLoopMeasurementMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtLoopMeasurementMethod.setStatus(_B)
class _ReachDSLSpectrumMgmtEWLUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('feet',2),('meters',3)))
_ReachDSLSpectrumMgmtEWLUnits_Type.__name__=_C
_ReachDSLSpectrumMgmtEWLUnits_Object=MibScalar
reachDSLSpectrumMgmtEWLUnits=_ReachDSLSpectrumMgmtEWLUnits_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,7),_ReachDSLSpectrumMgmtEWLUnits_Type())
reachDSLSpectrumMgmtEWLUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtEWLUnits.setStatus(_B)
class _ReachDSLSpectrumMgmtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enableOnly',1),('disableOnly',2),('both',3)))
_ReachDSLSpectrumMgmtMode_Type.__name__=_C
_ReachDSLSpectrumMgmtMode_Object=MibScalar
reachDSLSpectrumMgmtMode=_ReachDSLSpectrumMgmtMode_Object((1,3,6,1,4,1,1795,2,24,2,6,20,1,8),_ReachDSLSpectrumMgmtMode_Type())
reachDSLSpectrumMgmtMode.setMaxAccess(_D)
if mibBuilder.loadTexts:reachDSLSpectrumMgmtMode.setStatus(_B)
_PdnReachDSLConformance_ObjectIdentity=ObjectIdentity
pdnReachDSLConformance=_PdnReachDSLConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,20,2))
_PdnReachDSLGroups_ObjectIdentity=ObjectIdentity
pdnReachDSLGroups=_PdnReachDSLGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,20,2,1))
_PdnReachDSLCompliances_ObjectIdentity=ObjectIdentity
pdnReachDSLCompliances=_PdnReachDSLCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,20,2,2))
pdnReachDSLConfigurationGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,1))
pdnReachDSLConfigurationGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pdnReachDSLConfigurationGroup.setStatus(_F)
pdnReachDSLInformationGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,2))
pdnReachDSLInformationGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:pdnReachDSLInformationGroup.setStatus(_F)
pdnReachDSLDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,3))
pdnReachDSLDeprecatedGroup.setObjects(*((_A,_d),(_A,_Q)))
if mibBuilder.loadTexts:pdnReachDSLDeprecatedGroup.setStatus(_F)
pdnReachDSLGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,4))
pdnReachDSLGeneralConfigGroup.setObjects(*((_A,_K),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:pdnReachDSLGeneralConfigGroup.setStatus(_B)
pdnReachDSLGeneralInformationGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,5))
pdnReachDSLGeneralInformationGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:pdnReachDSLGeneralInformationGroup.setStatus(_B)
pdnReachDSLEWLModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,6))
pdnReachDSLEWLModeGroup.setObjects(*((_A,_L),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:pdnReachDSLEWLModeGroup.setStatus(_B)
pdnReachDSLLoopLengthModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,7))
pdnReachDSLLoopLengthModeGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:pdnReachDSLLoopLengthModeGroup.setStatus(_B)
pdnReachDSLQuadModeGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,20,2,1,8))
pdnReachDSLQuadModeGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:pdnReachDSLQuadModeGroup.setStatus(_B)
pdnReachDSLCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,20,2,2,1))
pdnReachDSLCompliance.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:pdnReachDSLCompliance.setStatus(_F)
pdnReachDSLCompliance1=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,20,2,2,2))
pdnReachDSLCompliance1.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:pdnReachDSLCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pdnReachDSL':pdnReachDSL,'pdnReachDSLObjects':pdnReachDSLObjects,_K:reachDSLSpectrumMgmtSelection,_d:reachDSLSpectrumMgmtZone,'reachDSLSpectrumMgmtConfTable':reachDSLSpectrumMgmtConfTable,'reachDSLSpectrumMgmtConfEntry':reachDSLSpectrumMgmtConfEntry,_L:reachDSLSpectrumMgmtConfEWL,_M:reachDSLSpectrumMgmtConfLoopLength,_N:reachDSLSpectrumMgmtConfAtucMaxTxPower,_O:reachDSLSpectrumMgmtConfAturMaxTxPower,_e:reachDSLSpectrumMgmtConfQuadMode,'reachDSLSpectrumMgmtLineInfoTable':reachDSLSpectrumMgmtLineInfoTable,'reachDSLSpectrumMgmtLineInfoEntry':reachDSLSpectrumMgmtLineInfoEntry,_R:reachDSLSpectrumMgmtAtucMaxTxRate,_S:reachDSLSpectrumMgmtAtucMinTxRate,_T:reachDSLSpectrumMgmtAtucMaxTxPower,_U:reachDSLSpectrumMgmtAturMaxTxRate,_V:reachDSLSpectrumMgmtAturMinTxRate,_W:reachDSLSpectrumMgmtAturMaxTxPower,_X:reachDSLSpectrumMgmtMinEWL,_Y:reachDSLSpectrumMgmtMaxEWL,'reachDSLLineTable':reachDSLLineTable,'reachDSLLineEntry':reachDSLLineEntry,_P:reachDSLPotsDetectionVoltage,_Q:reachDSLCircuitIdentifier,_Z:reachDSLSpectrumMgmtLoopMeasurementMethod,_a:reachDSLSpectrumMgmtEWLUnits,_b:reachDSLSpectrumMgmtMode,'pdnReachDSLConformance':pdnReachDSLConformance,'pdnReachDSLGroups':pdnReachDSLGroups,_f:pdnReachDSLConfigurationGroup,_g:pdnReachDSLInformationGroup,'pdnReachDSLDeprecatedGroup':pdnReachDSLDeprecatedGroup,_h:pdnReachDSLGeneralConfigGroup,_i:pdnReachDSLGeneralInformationGroup,_j:pdnReachDSLEWLModeGroup,_k:pdnReachDSLLoopLengthModeGroup,_l:pdnReachDSLQuadModeGroup,'pdnReachDSLCompliances':pdnReachDSLCompliances,'pdnReachDSLCompliance':pdnReachDSLCompliance,'pdnReachDSLCompliance1':pdnReachDSLCompliance1})