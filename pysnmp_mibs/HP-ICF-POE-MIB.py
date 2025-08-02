_Ab='hpicfPoeLowPowerPortGroup'
_Aa='hpicfPoePethPsePortForceTwoPairMode'
_AZ='hpicfpethPsePortPLCClassB'
_AY='hpicfpethPsePortPLCClassA'
_AX='hpicfpethPsePortPLCClass'
_AW='hpicfpethPsePortAssignedClass'
_AV='hpicfpethPsePortPowerClassificationB'
_AU='hpicfpethPsePortPowerClassificationA'
_AT='hpicfpethPsePortDetectionStatusB'
_AS='hpicfpethPsePortDetectionStatusA'
_AR='hpicfpethPsePortPDSignature'
_AQ='hpicfPoePethMainPsePdPowerDraw'
_AP='hpicfPoePethPsePortPowerType'
_AO='hpicfPseCurrentPowerDraw'
_AN='hpicfPoePethPsePortLowPriority'
_AM='hpicfPoePowerSupplyAuxCapacity'
_AL='hpicfPoePethPsePortPreStdDetect'
_AK='hpicfPoeRemainingGuaranteedPower'
_AJ='hpicfPoeMaxGuaranteedPower'
_AI='hpicfPoePethPseRemGrntPower'
_AH='hpicfPoePethPseAvgPower'
_AG='hpicfPoePethPsePeakPower'
_AF='hpicfPoePowerSupplyCapacity'
_AE='hpicfPoePowerSupplyType'
_AD='hpicfPoePowerSupplySourceType'
_AC='hpicfPseAllowPreStdDetect'
_AB='hpicfPoeExtPwrSupplyCount'
_AA='hpicfPoePowerRedundancy'
_A9='hpicfPoeAllowPreStdDetect'
_A8='hpicfPoePethPsePortPeakPower'
_A7='hpicfPoePethPsePortAveragePower'
_A6='hpicfPoePethPsePortPowerMode'
_A5='hpicfPoePethPsePortOperStatus'
_A4='hpicfPoePethPsePortActualPower'
_A3='hpicfPoePethPsePortPoePlusPowerValue'
_A2='hpicfPoePethPsePortLLDPDetect'
_A1='hpicfPoePethPsePortPowerValue'
_A0='hpicfPoePethPsePortPowerAllocateBy'
_z='hpicfPoePethPsePortPower'
_y='hpicfPoePethPsePortVoltage'
_x='hpicfPoePethPsePortCurrent'
_w='hpicfPoePethPseFourPairPortEntry'
_v='hpicfPoePethPsePowerEntry'
_u='hpicfPoePethPseOperStateEntry'
_t='hpicfPoePethPsePortEntry'
_s='class8'
_r='class7'
_q='class6'
_p='unknown'
_o='nPlus1'
_n='hpicfPoePethPsePortForceTwoPairModeGroup'
_m='hpicfPoePethPseFourPairPortTableGroup'
_l='hpicfPoePethPsePortPowerGroup'
_k='hpicfPoeAuxPowerSupplyGroup'
_j='hpicfPseParamsGroup'
_i='hpicfPoeGlobalGroup'
_h='hpicfPoePethPsePortNum'
_g='hpicfPoePethPseOperState'
_f='entPhysicalIndex'
_e='ENTITY-MIB'
_d='hpicfPoePethPseOperStateTableGroup'
_c='hpicfPseRedundantPower'
_b='hpicfPseFailoverPower'
_a='hpicfPseUsedPower'
_Z='hpicfPseAvailablePower'
_Y='hpicfPseExtPwrSupplyCount'
_X='hpicfPsePowerRedundancy'
_W='watts'
_V='off'
_U='hpicfPoePethPseOperStateTableGroup1'
_T='hpicfPseParamsGroup1'
_S='class5'
_R='class4'
_Q='class3'
_P='class2'
_O='class1'
_N='class0'
_M='hpicfPoePowerUsageGlobalGroup'
_L='hpicfPoePethPsePowerTableGroup'
_K='hpicfPoePethPsePortPreStdDetectGroup'
_J='hpicfPseFeaturesGroup'
_I='Watts'
_H='read-write'
_G='hpicfPoePowerSupplyGroup'
_F='deprecated'
_E='hpicfPoePethPsePortTableGroup'
_D='read-only'
_C='Integer32'
_B='current'
_A='HP-ICF-POE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_e,_f)
hpicfCommon,=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpicfPoe=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,9,1))
if mibBuilder.loadTexts:hpicfPoe.setRevisions(('2021-01-20 00:00','2018-06-04 00:00','2017-01-30 00:00','2016-09-12 00:00','2016-05-02 00:00','2016-02-12 00:00','2015-07-14 00:00','2013-06-16 00:00','2012-04-27 00:00','2012-03-02 00:00','2010-05-26 10:36','2009-11-18 00:00','2007-02-01 00:00','2005-06-06 00:00','2004-07-07 00:00'))
_HpicfPOE_ObjectIdentity=ObjectIdentity
hpicfPOE=_HpicfPOE_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,9))
_HpicfPoePethPsePortTable_Object=MibTable
hpicfPoePethPsePortTable=_HpicfPoePethPsePortTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1))
if mibBuilder.loadTexts:hpicfPoePethPsePortTable.setStatus(_B)
_HpicfPoePethPsePortEntry_Object=MibTableRow
hpicfPoePethPsePortEntry=_HpicfPoePethPsePortEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1))
if mibBuilder.loadTexts:hpicfPoePethPsePortEntry.setStatus(_B)
class _HpicfPoePethPsePortCurrent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfPoePethPsePortCurrent_Type.__name__=_C
_HpicfPoePethPsePortCurrent_Object=MibTableColumn
hpicfPoePethPsePortCurrent=_HpicfPoePethPsePortCurrent_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,1),_HpicfPoePethPsePortCurrent_Type())
hpicfPoePethPsePortCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortCurrent.setStatus(_B)
class _HpicfPoePethPsePortVoltage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfPoePethPsePortVoltage_Type.__name__=_C
_HpicfPoePethPsePortVoltage_Object=MibTableColumn
hpicfPoePethPsePortVoltage=_HpicfPoePethPsePortVoltage_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,2),_HpicfPoePethPsePortVoltage_Type())
hpicfPoePethPsePortVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortVoltage.setStatus(_B)
class _HpicfPoePethPsePortPower_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfPoePethPsePortPower_Type.__name__=_C
_HpicfPoePethPsePortPower_Object=MibTableColumn
hpicfPoePethPsePortPower=_HpicfPoePethPsePortPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,3),_HpicfPoePethPsePortPower_Type())
hpicfPoePethPsePortPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortPower.setStatus(_B)
class _HpicfPoePethPsePortPowerAllocateBy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('usage',1),('class',2),('value',3)))
_HpicfPoePethPsePortPowerAllocateBy_Type.__name__=_C
_HpicfPoePethPsePortPowerAllocateBy_Object=MibTableColumn
hpicfPoePethPsePortPowerAllocateBy=_HpicfPoePethPsePortPowerAllocateBy_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,4),_HpicfPoePethPsePortPowerAllocateBy_Type())
hpicfPoePethPsePortPowerAllocateBy.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortPowerAllocateBy.setStatus(_B)
class _HpicfPoePethPsePortPowerValue_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,17))
_HpicfPoePethPsePortPowerValue_Type.__name__=_C
_HpicfPoePethPsePortPowerValue_Object=MibTableColumn
hpicfPoePethPsePortPowerValue=_HpicfPoePethPsePortPowerValue_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,5),_HpicfPoePethPsePortPowerValue_Type())
hpicfPoePethPsePortPowerValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortPowerValue.setStatus(_B)
class _HpicfPoePethPsePortLLDPDetect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_HpicfPoePethPsePortLLDPDetect_Type.__name__=_C
_HpicfPoePethPsePortLLDPDetect_Object=MibTableColumn
hpicfPoePethPsePortLLDPDetect=_HpicfPoePethPsePortLLDPDetect_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,6),_HpicfPoePethPsePortLLDPDetect_Type())
hpicfPoePethPsePortLLDPDetect.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortLLDPDetect.setStatus(_B)
class _HpicfPoePethPsePortPoePlusPowerValue_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpicfPoePethPsePortPoePlusPowerValue_Type.__name__=_C
_HpicfPoePethPsePortPoePlusPowerValue_Object=MibTableColumn
hpicfPoePethPsePortPoePlusPowerValue=_HpicfPoePethPsePortPoePlusPowerValue_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,7),_HpicfPoePethPsePortPoePlusPowerValue_Type())
hpicfPoePethPsePortPoePlusPowerValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortPoePlusPowerValue.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPsePortPoePlusPowerValue.setUnits(_I)
class _HpicfPoePethPsePortActualPower_Type(Integer32):defaultValue=0
_HpicfPoePethPsePortActualPower_Type.__name__=_C
_HpicfPoePethPsePortActualPower_Object=MibTableColumn
hpicfPoePethPsePortActualPower=_HpicfPoePethPsePortActualPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,8),_HpicfPoePethPsePortActualPower_Type())
hpicfPoePethPsePortActualPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortActualPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPsePortActualPower.setUnits('milli-watts')
class _HpicfPoePethPsePortOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_V,2),('on',3)))
_HpicfPoePethPsePortOperStatus_Type.__name__=_C
_HpicfPoePethPsePortOperStatus_Object=MibTableColumn
hpicfPoePethPsePortOperStatus=_HpicfPoePethPsePortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,9),_HpicfPoePethPsePortOperStatus_Type())
hpicfPoePethPsePortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortOperStatus.setStatus(_B)
class _HpicfPoePethPsePortPowerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*(('enable',1),('disable',2),('disableWithFiber',6)))
_HpicfPoePethPsePortPowerMode_Type.__name__=_C
_HpicfPoePethPsePortPowerMode_Object=MibTableColumn
hpicfPoePethPsePortPowerMode=_HpicfPoePethPsePortPowerMode_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,10),_HpicfPoePethPsePortPowerMode_Type())
hpicfPoePethPsePortPowerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortPowerMode.setStatus(_B)
class _HpicfPoePethPsePortAveragePower_Type(Integer32):defaultValue=0
_HpicfPoePethPsePortAveragePower_Type.__name__=_C
_HpicfPoePethPsePortAveragePower_Object=MibTableColumn
hpicfPoePethPsePortAveragePower=_HpicfPoePethPsePortAveragePower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,11),_HpicfPoePethPsePortAveragePower_Type())
hpicfPoePethPsePortAveragePower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortAveragePower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPsePortAveragePower.setUnits(_W)
class _HpicfPoePethPsePortPeakPower_Type(Integer32):defaultValue=0
_HpicfPoePethPsePortPeakPower_Type.__name__=_C
_HpicfPoePethPsePortPeakPower_Object=MibTableColumn
hpicfPoePethPsePortPeakPower=_HpicfPoePethPsePortPeakPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,12),_HpicfPoePethPsePortPeakPower_Type())
hpicfPoePethPsePortPeakPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortPeakPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPsePortPeakPower.setUnits(_W)
class _HpicfPoePethPsePortPreStdDetect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('on',2)))
_HpicfPoePethPsePortPreStdDetect_Type.__name__=_C
_HpicfPoePethPsePortPreStdDetect_Object=MibTableColumn
hpicfPoePethPsePortPreStdDetect=_HpicfPoePethPsePortPreStdDetect_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,13),_HpicfPoePethPsePortPreStdDetect_Type())
hpicfPoePethPsePortPreStdDetect.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortPreStdDetect.setStatus(_B)
class _HpicfPoePethPsePortLowPriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_HpicfPoePethPsePortLowPriority_Type.__name__=_C
_HpicfPoePethPsePortLowPriority_Object=MibTableColumn
hpicfPoePethPsePortLowPriority=_HpicfPoePethPsePortLowPriority_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,14),_HpicfPoePethPsePortLowPriority_Type())
hpicfPoePethPsePortLowPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortLowPriority.setStatus(_B)
class _HpicfPoePethPsePortResetState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noreset',0),('reset',1)))
_HpicfPoePethPsePortResetState_Type.__name__=_C
_HpicfPoePethPsePortResetState_Object=MibTableColumn
hpicfPoePethPsePortResetState=_HpicfPoePethPsePortResetState_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,15),_HpicfPoePethPsePortResetState_Type())
hpicfPoePethPsePortResetState.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortResetState.setStatus(_B)
class _HpicfPoePethPsePortPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4)));namedValues=NamedValues(*(('type0',-1),('type1',1),('type2',2),('type3',3),('type4',4)))
_HpicfPoePethPsePortPowerType_Type.__name__=_C
_HpicfPoePethPsePortPowerType_Object=MibTableColumn
hpicfPoePethPsePortPowerType=_HpicfPoePethPsePortPowerType_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,16),_HpicfPoePethPsePortPowerType_Type())
hpicfPoePethPsePortPowerType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortPowerType.setStatus(_B)
class _HpicfPoePethPsePortForceTwoPairMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('on',2)))
_HpicfPoePethPsePortForceTwoPairMode_Type.__name__=_C
_HpicfPoePethPsePortForceTwoPairMode_Object=MibTableColumn
hpicfPoePethPsePortForceTwoPairMode=_HpicfPoePethPsePortForceTwoPairMode_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,1,1,17),_HpicfPoePethPsePortForceTwoPairMode_Type())
hpicfPoePethPsePortForceTwoPairMode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePethPsePortForceTwoPairMode.setStatus(_B)
_HpicfPoeConformance_ObjectIdentity=ObjectIdentity
hpicfPoeConformance=_HpicfPoeConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,9,1,2))
_HpicfPoeCompliances_ObjectIdentity=ObjectIdentity
hpicfPoeCompliances=_HpicfPoeCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1))
_HpicfPoeGroups_ObjectIdentity=ObjectIdentity
hpicfPoeGroups=_HpicfPoeGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2))
_HpicfPoeAllowPreStdDetect_Type=TruthValue
_HpicfPoeAllowPreStdDetect_Object=MibScalar
hpicfPoeAllowPreStdDetect=_HpicfPoeAllowPreStdDetect_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,3),_HpicfPoeAllowPreStdDetect_Type())
hpicfPoeAllowPreStdDetect.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoeAllowPreStdDetect.setStatus(_F)
class _HpicfPoePowerRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_o,2),('full',3)))
_HpicfPoePowerRedundancy_Type.__name__=_C
_HpicfPoePowerRedundancy_Object=MibScalar
hpicfPoePowerRedundancy=_HpicfPoePowerRedundancy_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,4),_HpicfPoePowerRedundancy_Type())
hpicfPoePowerRedundancy.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoePowerRedundancy.setStatus(_F)
class _HpicfPoeExtPwrSupplyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfPoeExtPwrSupplyCount_Type.__name__=_C
_HpicfPoeExtPwrSupplyCount_Object=MibScalar
hpicfPoeExtPwrSupplyCount=_HpicfPoeExtPwrSupplyCount_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,5),_HpicfPoeExtPwrSupplyCount_Type())
hpicfPoeExtPwrSupplyCount.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPoeExtPwrSupplyCount.setStatus(_F)
_HpicfPseFeaturesTable_Object=MibTable
hpicfPseFeaturesTable=_HpicfPseFeaturesTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6))
if mibBuilder.loadTexts:hpicfPseFeaturesTable.setStatus(_B)
_HpicfPseFeaturesEntry_Object=MibTableRow
hpicfPseFeaturesEntry=_HpicfPseFeaturesEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1))
hpicfPseFeaturesEntry.setIndexNames((0,_e,_f))
if mibBuilder.loadTexts:hpicfPseFeaturesEntry.setStatus(_B)
_HpicfPseAllowPreStdDetect_Type=TruthValue
_HpicfPseAllowPreStdDetect_Object=MibTableColumn
hpicfPseAllowPreStdDetect=_HpicfPseAllowPreStdDetect_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,1),_HpicfPseAllowPreStdDetect_Type())
hpicfPseAllowPreStdDetect.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPseAllowPreStdDetect.setStatus(_F)
class _HpicfPsePowerRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_o,2),('full',3)))
_HpicfPsePowerRedundancy_Type.__name__=_C
_HpicfPsePowerRedundancy_Object=MibTableColumn
hpicfPsePowerRedundancy=_HpicfPsePowerRedundancy_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,2),_HpicfPsePowerRedundancy_Type())
hpicfPsePowerRedundancy.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPsePowerRedundancy.setStatus(_B)
class _HpicfPseExtPwrSupplyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfPseExtPwrSupplyCount_Type.__name__=_C
_HpicfPseExtPwrSupplyCount_Object=MibTableColumn
hpicfPseExtPwrSupplyCount=_HpicfPseExtPwrSupplyCount_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,3),_HpicfPseExtPwrSupplyCount_Type())
hpicfPseExtPwrSupplyCount.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfPseExtPwrSupplyCount.setStatus(_B)
class _HpicfPseAvailablePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPseAvailablePower_Type.__name__=_C
_HpicfPseAvailablePower_Object=MibTableColumn
hpicfPseAvailablePower=_HpicfPseAvailablePower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,4),_HpicfPseAvailablePower_Type())
hpicfPseAvailablePower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPseAvailablePower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPseAvailablePower.setUnits(_I)
class _HpicfPseUsedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPseUsedPower_Type.__name__=_C
_HpicfPseUsedPower_Object=MibTableColumn
hpicfPseUsedPower=_HpicfPseUsedPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,5),_HpicfPseUsedPower_Type())
hpicfPseUsedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPseUsedPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPseUsedPower.setUnits(_I)
class _HpicfPseFailoverPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPseFailoverPower_Type.__name__=_C
_HpicfPseFailoverPower_Object=MibTableColumn
hpicfPseFailoverPower=_HpicfPseFailoverPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,6),_HpicfPseFailoverPower_Type())
hpicfPseFailoverPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPseFailoverPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPseFailoverPower.setUnits(_I)
class _HpicfPseRedundantPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPseRedundantPower_Type.__name__=_C
_HpicfPseRedundantPower_Object=MibTableColumn
hpicfPseRedundantPower=_HpicfPseRedundantPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,7),_HpicfPseRedundantPower_Type())
hpicfPseRedundantPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPseRedundantPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPseRedundantPower.setUnits(_I)
class _HpicfPseCurrentPowerDraw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPseCurrentPowerDraw_Type.__name__=_C
_HpicfPseCurrentPowerDraw_Object=MibTableColumn
hpicfPseCurrentPowerDraw=_HpicfPseCurrentPowerDraw_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,6,1,8),_HpicfPseCurrentPowerDraw_Type())
hpicfPseCurrentPowerDraw.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPseCurrentPowerDraw.setStatus(_B)
if mibBuilder.loadTexts:hpicfPseCurrentPowerDraw.setUnits(_I)
_HpicfPoePowerSupplyTable_Object=MibTable
hpicfPoePowerSupplyTable=_HpicfPoePowerSupplyTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7))
if mibBuilder.loadTexts:hpicfPoePowerSupplyTable.setStatus(_B)
_HpicfPoePowerSupplyEntry_Object=MibTableRow
hpicfPoePowerSupplyEntry=_HpicfPoePowerSupplyEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7,1))
hpicfPoePowerSupplyEntry.setIndexNames((0,_e,_f))
if mibBuilder.loadTexts:hpicfPoePowerSupplyEntry.setStatus(_B)
class _HpicfPoePowerSupplySourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_HpicfPoePowerSupplySourceType_Type.__name__=_C
_HpicfPoePowerSupplySourceType_Object=MibTableColumn
hpicfPoePowerSupplySourceType=_HpicfPoePowerSupplySourceType_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7,1,1),_HpicfPoePowerSupplySourceType_Type())
hpicfPoePowerSupplySourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePowerSupplySourceType.setStatus(_B)
class _HpicfPoePowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('poe',1),('poePlus',2),('notPresent',3),('fault',4),('auxFault',5)))
_HpicfPoePowerSupplyType_Type.__name__=_C
_HpicfPoePowerSupplyType_Object=MibTableColumn
hpicfPoePowerSupplyType=_HpicfPoePowerSupplyType_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7,1,2),_HpicfPoePowerSupplyType_Type())
hpicfPoePowerSupplyType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePowerSupplyType.setStatus(_B)
class _HpicfPoePowerSupplyCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPoePowerSupplyCapacity_Type.__name__=_C
_HpicfPoePowerSupplyCapacity_Object=MibTableColumn
hpicfPoePowerSupplyCapacity=_HpicfPoePowerSupplyCapacity_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7,1,3),_HpicfPoePowerSupplyCapacity_Type())
hpicfPoePowerSupplyCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePowerSupplyCapacity.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePowerSupplyCapacity.setUnits(_I)
class _HpicfPoePowerSupplyAuxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HpicfPoePowerSupplyAuxCapacity_Type.__name__=_C
_HpicfPoePowerSupplyAuxCapacity_Object=MibTableColumn
hpicfPoePowerSupplyAuxCapacity=_HpicfPoePowerSupplyAuxCapacity_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,7,1,4),_HpicfPoePowerSupplyAuxCapacity_Type())
hpicfPoePowerSupplyAuxCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePowerSupplyAuxCapacity.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePowerSupplyAuxCapacity.setUnits(_I)
_HpicfPoePethPseOperStateTable_Object=MibTable
hpicfPoePethPseOperStateTable=_HpicfPoePethPseOperStateTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,8))
if mibBuilder.loadTexts:hpicfPoePethPseOperStateTable.setStatus(_B)
_HpicfPoePethPseOperStateEntry_Object=MibTableRow
hpicfPoePethPseOperStateEntry=_HpicfPoePethPseOperStateEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,8,1))
if mibBuilder.loadTexts:hpicfPoePethPseOperStateEntry.setStatus(_B)
class _HpicfPoePethPseOperState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('poeOn',1),('poePlusOn',2),(_V,3),('fault',4)))
_HpicfPoePethPseOperState_Type.__name__=_C
_HpicfPoePethPseOperState_Object=MibTableColumn
hpicfPoePethPseOperState=_HpicfPoePethPseOperState_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,8,1,1),_HpicfPoePethPseOperState_Type())
hpicfPoePethPseOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPseOperState.setStatus(_B)
class _HpicfPoePethPsePortNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfPoePethPsePortNum_Type.__name__=_C
_HpicfPoePethPsePortNum_Object=MibTableColumn
hpicfPoePethPsePortNum=_HpicfPoePethPsePortNum_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,8,1,2),_HpicfPoePethPsePortNum_Type())
hpicfPoePethPsePortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePortNum.setStatus(_B)
class _HpicfPoePethMainPsePdPowerDraw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfPoePethMainPsePdPowerDraw_Type.__name__=_C
_HpicfPoePethMainPsePdPowerDraw_Object=MibTableColumn
hpicfPoePethMainPsePdPowerDraw=_HpicfPoePethMainPsePdPowerDraw_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,8,1,3),_HpicfPoePethMainPsePdPowerDraw_Type())
hpicfPoePethMainPsePdPowerDraw.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethMainPsePdPowerDraw.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethMainPsePdPowerDraw.setUnits(_I)
_HpicfPoeMaxGuaranteedPower_Type=Integer32
_HpicfPoeMaxGuaranteedPower_Object=MibScalar
hpicfPoeMaxGuaranteedPower=_HpicfPoeMaxGuaranteedPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,9),_HpicfPoeMaxGuaranteedPower_Type())
hpicfPoeMaxGuaranteedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoeMaxGuaranteedPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoeMaxGuaranteedPower.setUnits(_W)
_HpicfPoeRemainingGuaranteedPower_Type=Integer32
_HpicfPoeRemainingGuaranteedPower_Object=MibScalar
hpicfPoeRemainingGuaranteedPower=_HpicfPoeRemainingGuaranteedPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,10),_HpicfPoeRemainingGuaranteedPower_Type())
hpicfPoeRemainingGuaranteedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoeRemainingGuaranteedPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoeRemainingGuaranteedPower.setUnits(_W)
_HpicfPoePethPsePowerTable_Object=MibTable
hpicfPoePethPsePowerTable=_HpicfPoePethPsePowerTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,11))
if mibBuilder.loadTexts:hpicfPoePethPsePowerTable.setStatus(_B)
_HpicfPoePethPsePowerEntry_Object=MibTableRow
hpicfPoePethPsePowerEntry=_HpicfPoePethPsePowerEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,11,1))
if mibBuilder.loadTexts:hpicfPoePethPsePowerEntry.setStatus(_B)
_HpicfPoePethPsePeakPower_Type=Integer32
_HpicfPoePethPsePeakPower_Object=MibTableColumn
hpicfPoePethPsePeakPower=_HpicfPoePethPsePeakPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,11,1,1),_HpicfPoePethPsePeakPower_Type())
hpicfPoePethPsePeakPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPsePeakPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPsePeakPower.setUnits(_I)
_HpicfPoePethPseAvgPower_Type=Integer32
_HpicfPoePethPseAvgPower_Object=MibTableColumn
hpicfPoePethPseAvgPower=_HpicfPoePethPseAvgPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,11,1,2),_HpicfPoePethPseAvgPower_Type())
hpicfPoePethPseAvgPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPseAvgPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPseAvgPower.setUnits(_I)
_HpicfPoePethPseRemGrntPower_Type=Integer32
_HpicfPoePethPseRemGrntPower_Object=MibTableColumn
hpicfPoePethPseRemGrntPower=_HpicfPoePethPseRemGrntPower_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,11,1,3),_HpicfPoePethPseRemGrntPower_Type())
hpicfPoePethPseRemGrntPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfPoePethPseRemGrntPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfPoePethPseRemGrntPower.setUnits(_I)
_HpicfPoePethPseFourPairPortTable_Object=MibTable
hpicfPoePethPseFourPairPortTable=_HpicfPoePethPseFourPairPortTable_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12))
if mibBuilder.loadTexts:hpicfPoePethPseFourPairPortTable.setStatus(_B)
_HpicfPoePethPseFourPairPortEntry_Object=MibTableRow
hpicfPoePethPseFourPairPortEntry=_HpicfPoePethPseFourPairPortEntry_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1))
if mibBuilder.loadTexts:hpicfPoePethPseFourPairPortEntry.setStatus(_B)
class _HpicfpethPsePortPDSignature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknownSignature',0),('singleSignature',1),('dualSignature',2)))
_HpicfpethPsePortPDSignature_Type.__name__=_C
_HpicfpethPsePortPDSignature_Object=MibTableColumn
hpicfpethPsePortPDSignature=_HpicfpethPsePortPDSignature_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,1),_HpicfpethPsePortPDSignature_Type())
hpicfpethPsePortPDSignature.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPDSignature.setStatus(_B)
class _HpicfpethPsePortDetectionStatusA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_p,0),('searchingAltA',1),('deliveringPowerAltA',2),('faultAltA',3)))
_HpicfpethPsePortDetectionStatusA_Type.__name__=_C
_HpicfpethPsePortDetectionStatusA_Object=MibTableColumn
hpicfpethPsePortDetectionStatusA=_HpicfpethPsePortDetectionStatusA_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,2),_HpicfpethPsePortDetectionStatusA_Type())
hpicfpethPsePortDetectionStatusA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortDetectionStatusA.setStatus(_B)
class _HpicfpethPsePortDetectionStatusB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_p,0),('searchingAltB',1),('deliveringPowerAltB',2),('faultAltB',3)))
_HpicfpethPsePortDetectionStatusB_Type.__name__=_C
_HpicfpethPsePortDetectionStatusB_Object=MibTableColumn
hpicfpethPsePortDetectionStatusB=_HpicfpethPsePortDetectionStatusB_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,3),_HpicfpethPsePortDetectionStatusB_Type())
hpicfpethPsePortDetectionStatusB.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortDetectionStatusB.setStatus(_B)
class _HpicfpethPsePortPowerClassificationA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_HpicfpethPsePortPowerClassificationA_Type.__name__=_C
_HpicfpethPsePortPowerClassificationA_Object=MibTableColumn
hpicfpethPsePortPowerClassificationA=_HpicfpethPsePortPowerClassificationA_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,4),_HpicfpethPsePortPowerClassificationA_Type())
hpicfpethPsePortPowerClassificationA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPowerClassificationA.setStatus(_B)
class _HpicfpethPsePortPowerClassificationB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_HpicfpethPsePortPowerClassificationB_Type.__name__=_C
_HpicfpethPsePortPowerClassificationB_Object=MibTableColumn
hpicfpethPsePortPowerClassificationB=_HpicfpethPsePortPowerClassificationB_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,5),_HpicfpethPsePortPowerClassificationB_Type())
hpicfpethPsePortPowerClassificationB.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPowerClassificationB.setStatus(_B)
class _HpicfpethPsePortAssignedClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_q,7),(_r,8),(_s,9)))
_HpicfpethPsePortAssignedClass_Type.__name__=_C
_HpicfpethPsePortAssignedClass_Object=MibTableColumn
hpicfpethPsePortAssignedClass=_HpicfpethPsePortAssignedClass_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,6),_HpicfpethPsePortAssignedClass_Type())
hpicfpethPsePortAssignedClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortAssignedClass.setStatus(_B)
class _HpicfpethPsePortPLCClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_q,7),(_r,8),(_s,9)))
_HpicfpethPsePortPLCClass_Type.__name__=_C
_HpicfpethPsePortPLCClass_Object=MibTableColumn
hpicfpethPsePortPLCClass=_HpicfpethPsePortPLCClass_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,7),_HpicfpethPsePortPLCClass_Type())
hpicfpethPsePortPLCClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPLCClass.setStatus(_B)
class _HpicfpethPsePortPLCClassA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_HpicfpethPsePortPLCClassA_Type.__name__=_C
_HpicfpethPsePortPLCClassA_Object=MibTableColumn
hpicfpethPsePortPLCClassA=_HpicfpethPsePortPLCClassA_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,8),_HpicfpethPsePortPLCClassA_Type())
hpicfpethPsePortPLCClassA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPLCClassA.setStatus(_B)
class _HpicfpethPsePortPLCClassB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_HpicfpethPsePortPLCClassB_Type.__name__=_C
_HpicfpethPsePortPLCClassB_Object=MibTableColumn
hpicfpethPsePortPLCClassB=_HpicfpethPsePortPLCClassB_Object((1,3,6,1,4,1,11,2,14,11,1,9,1,12,1,9),_HpicfpethPsePortPLCClassB_Type())
hpicfpethPsePortPLCClassB.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfpethPsePortPLCClassB.setStatus(_B)
pethPsePortEntry.registerAugmentions((_A,_t))
hpicfPoePethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_A,_u))
hpicfPoePethPseOperStateEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_A,_v))
hpicfPoePethPsePowerEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethPsePortEntry.registerAugmentions((_A,_w))
hpicfPoePethPseFourPairPortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
hpicfPoePethPsePortTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,1))
hpicfPoePethPsePortTableGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:hpicfPoePethPsePortTableGroup.setStatus(_B)
hpicfPoeGlobalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,2))
hpicfPoeGlobalGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:hpicfPoeGlobalGroup.setStatus(_F)
hpicfPseFeaturesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,3))
hpicfPseFeaturesGroup.setObjects(*((_A,_AC),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpicfPseFeaturesGroup.setStatus(_F)
hpicfPoePowerSupplyGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,4))
hpicfPoePowerSupplyGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:hpicfPoePowerSupplyGroup.setStatus(_B)
hpicfPoePethPseOperStateTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,5))
hpicfPoePethPseOperStateTableGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfPoePethPseOperStateTableGroup.setStatus(_F)
hpicfPoePethPsePowerTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,6))
hpicfPoePethPsePowerTableGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:hpicfPoePethPsePowerTableGroup.setStatus(_B)
hpicfPoePowerUsageGlobalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,7))
hpicfPoePowerUsageGlobalGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:hpicfPoePowerUsageGlobalGroup.setStatus(_B)
hpicfPseParamsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,8))
hpicfPseParamsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpicfPseParamsGroup.setStatus(_F)
hpicfPoePethPsePortPreStdDetectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,9))
hpicfPoePethPsePortPreStdDetectGroup.setObjects((_A,_AL))
if mibBuilder.loadTexts:hpicfPoePethPsePortPreStdDetectGroup.setStatus(_B)
hpicfPoeAuxPowerSupplyGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,10))
hpicfPoeAuxPowerSupplyGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:hpicfPoeAuxPowerSupplyGroup.setStatus(_B)
hpicfPoeLowPowerPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,11))
hpicfPoeLowPowerPortGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:hpicfPoeLowPowerPortGroup.setStatus(_B)
hpicfPseParamsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,12))
hpicfPseParamsGroup1.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_AO)))
if mibBuilder.loadTexts:hpicfPseParamsGroup1.setStatus(_B)
hpicfPoePethPsePortPowerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,13))
hpicfPoePethPsePortPowerGroup.setObjects((_A,_AP))
if mibBuilder.loadTexts:hpicfPoePethPsePortPowerGroup.setStatus(_B)
hpicfPoePethPseOperStateTableGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,14))
hpicfPoePethPseOperStateTableGroup1.setObjects(*((_A,_g),(_A,_h),(_A,_AQ)))
if mibBuilder.loadTexts:hpicfPoePethPseOperStateTableGroup1.setStatus(_B)
hpicfPoePethPseFourPairPortTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,15))
hpicfPoePethPseFourPairPortTableGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:hpicfPoePethPseFourPairPortTableGroup.setStatus(_B)
hpicfPoePethPsePortForceTwoPairModeGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,9,1,2,2,16))
hpicfPoePethPsePortForceTwoPairModeGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:hpicfPoePethPsePortForceTwoPairModeGroup.setStatus(_B)
hpicfPoeCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,1))
hpicfPoeCompliance.setObjects(*((_A,_E),(_A,_E)))
if mibBuilder.loadTexts:hpicfPoeCompliance.setStatus(_F)
hpicfPoeCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,2))
hpicfPoeCompliance1.setObjects(*((_A,_E),(_A,_i),(_A,_E),(_A,_i)))
if mibBuilder.loadTexts:hpicfPoeCompliance1.setStatus(_F)
hpicfPoeCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,3))
hpicfPoeCompliance2.setObjects(*((_A,_E),(_A,_J),(_A,_G),(_A,_E),(_A,_J),(_A,_G),(_A,_d)))
if mibBuilder.loadTexts:hpicfPoeCompliance2.setStatus(_F)
hpicfPoeCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,4))
hpicfPoeCompliance3.setObjects(*((_A,_E),(_A,_j),(_A,_G),(_A,_K),(_A,_E),(_A,_j),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:hpicfPoeCompliance3.setStatus(_F)
hpicfPoeCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,5))
hpicfPoeCompliance4.setObjects(*((_A,_E),(_A,_J),(_A,_G),(_A,_d),(_A,_L),(_A,_M),(_A,_E),(_A,_J),(_A,_G),(_A,_d),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfPoeCompliance4.setStatus(_F)
hpicfPoeCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,6))
hpicfPoeCompliance5.setObjects(*((_A,_k),(_A,_k),(_A,_Ab)))
if mibBuilder.loadTexts:hpicfPoeCompliance5.setStatus(_B)
hpicfPoeCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,7))
hpicfPoeCompliance6.setObjects(*((_A,_l),(_A,_l)))
if mibBuilder.loadTexts:hpicfPoeCompliance6.setStatus(_B)
hpicfPoeCompliance7=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,8))
hpicfPoeCompliance7.setObjects(*((_A,_E),(_A,_T),(_A,_G),(_A,_K),(_A,_E),(_A,_T),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:hpicfPoeCompliance7.setStatus(_F)
hpicfPoeCompliance8=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,9))
hpicfPoeCompliance8.setObjects(*((_A,_E),(_A,_J),(_A,_G),(_A,_L),(_A,_M),(_A,_U),(_A,_E),(_A,_J),(_A,_G),(_A,_L),(_A,_M),(_A,_U)))
if mibBuilder.loadTexts:hpicfPoeCompliance8.setStatus(_F)
hpicfPoeCompliance9=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,10))
hpicfPoeCompliance9.setObjects(*((_A,_E),(_A,_J),(_A,_G),(_A,_L),(_A,_M),(_A,_U),(_A,_m),(_A,_E),(_A,_J),(_A,_G),(_A,_L),(_A,_M),(_A,_U),(_A,_m)))
if mibBuilder.loadTexts:hpicfPoeCompliance9.setStatus(_B)
hpicfPoeCompliance10=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,9,1,2,1,11))
hpicfPoeCompliance10.setObjects(*((_A,_E),(_A,_T),(_A,_G),(_A,_K),(_A,_n),(_A,_E),(_A,_T),(_A,_G),(_A,_K),(_A,_n)))
if mibBuilder.loadTexts:hpicfPoeCompliance10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfPOE':hpicfPOE,'hpicfPoe':hpicfPoe,'hpicfPoePethPsePortTable':hpicfPoePethPsePortTable,_t:hpicfPoePethPsePortEntry,_x:hpicfPoePethPsePortCurrent,_y:hpicfPoePethPsePortVoltage,_z:hpicfPoePethPsePortPower,_A0:hpicfPoePethPsePortPowerAllocateBy,_A1:hpicfPoePethPsePortPowerValue,_A2:hpicfPoePethPsePortLLDPDetect,_A3:hpicfPoePethPsePortPoePlusPowerValue,_A4:hpicfPoePethPsePortActualPower,_A5:hpicfPoePethPsePortOperStatus,_A6:hpicfPoePethPsePortPowerMode,_A7:hpicfPoePethPsePortAveragePower,_A8:hpicfPoePethPsePortPeakPower,_AL:hpicfPoePethPsePortPreStdDetect,_AN:hpicfPoePethPsePortLowPriority,'hpicfPoePethPsePortResetState':hpicfPoePethPsePortResetState,_AP:hpicfPoePethPsePortPowerType,_Aa:hpicfPoePethPsePortForceTwoPairMode,'hpicfPoeConformance':hpicfPoeConformance,'hpicfPoeCompliances':hpicfPoeCompliances,'hpicfPoeCompliance':hpicfPoeCompliance,'hpicfPoeCompliance1':hpicfPoeCompliance1,'hpicfPoeCompliance2':hpicfPoeCompliance2,'hpicfPoeCompliance3':hpicfPoeCompliance3,'hpicfPoeCompliance4':hpicfPoeCompliance4,'hpicfPoeCompliance5':hpicfPoeCompliance5,'hpicfPoeCompliance6':hpicfPoeCompliance6,'hpicfPoeCompliance7':hpicfPoeCompliance7,'hpicfPoeCompliance8':hpicfPoeCompliance8,'hpicfPoeCompliance9':hpicfPoeCompliance9,'hpicfPoeCompliance10':hpicfPoeCompliance10,'hpicfPoeGroups':hpicfPoeGroups,_E:hpicfPoePethPsePortTableGroup,_i:hpicfPoeGlobalGroup,_J:hpicfPseFeaturesGroup,_G:hpicfPoePowerSupplyGroup,_d:hpicfPoePethPseOperStateTableGroup,_L:hpicfPoePethPsePowerTableGroup,_M:hpicfPoePowerUsageGlobalGroup,_j:hpicfPseParamsGroup,_K:hpicfPoePethPsePortPreStdDetectGroup,_k:hpicfPoeAuxPowerSupplyGroup,_Ab:hpicfPoeLowPowerPortGroup,_T:hpicfPseParamsGroup1,_l:hpicfPoePethPsePortPowerGroup,_U:hpicfPoePethPseOperStateTableGroup1,_m:hpicfPoePethPseFourPairPortTableGroup,_n:hpicfPoePethPsePortForceTwoPairModeGroup,_A9:hpicfPoeAllowPreStdDetect,_AA:hpicfPoePowerRedundancy,_AB:hpicfPoeExtPwrSupplyCount,'hpicfPseFeaturesTable':hpicfPseFeaturesTable,'hpicfPseFeaturesEntry':hpicfPseFeaturesEntry,_AC:hpicfPseAllowPreStdDetect,_X:hpicfPsePowerRedundancy,_Y:hpicfPseExtPwrSupplyCount,_Z:hpicfPseAvailablePower,_a:hpicfPseUsedPower,_b:hpicfPseFailoverPower,_c:hpicfPseRedundantPower,_AO:hpicfPseCurrentPowerDraw,'hpicfPoePowerSupplyTable':hpicfPoePowerSupplyTable,'hpicfPoePowerSupplyEntry':hpicfPoePowerSupplyEntry,_AD:hpicfPoePowerSupplySourceType,_AE:hpicfPoePowerSupplyType,_AF:hpicfPoePowerSupplyCapacity,_AM:hpicfPoePowerSupplyAuxCapacity,'hpicfPoePethPseOperStateTable':hpicfPoePethPseOperStateTable,_u:hpicfPoePethPseOperStateEntry,_g:hpicfPoePethPseOperState,_h:hpicfPoePethPsePortNum,_AQ:hpicfPoePethMainPsePdPowerDraw,_AJ:hpicfPoeMaxGuaranteedPower,_AK:hpicfPoeRemainingGuaranteedPower,'hpicfPoePethPsePowerTable':hpicfPoePethPsePowerTable,_v:hpicfPoePethPsePowerEntry,_AG:hpicfPoePethPsePeakPower,_AH:hpicfPoePethPseAvgPower,_AI:hpicfPoePethPseRemGrntPower,'hpicfPoePethPseFourPairPortTable':hpicfPoePethPseFourPairPortTable,_w:hpicfPoePethPseFourPairPortEntry,_AR:hpicfpethPsePortPDSignature,_AS:hpicfpethPsePortDetectionStatusA,_AT:hpicfpethPsePortDetectionStatusB,_AU:hpicfpethPsePortPowerClassificationA,_AV:hpicfpethPsePortPowerClassificationB,_AW:hpicfpethPsePortAssignedClass,_AX:hpicfpethPsePortPLCClass,_AY:hpicfpethPsePortPLCClassA,_AZ:hpicfpethPsePortPLCClassB})