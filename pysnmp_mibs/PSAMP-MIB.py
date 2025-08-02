_m='psampGroupFiltHash'
_l='psampGroupFiltPropMatch'
_k='psampGroupSampUniProb'
_j='psampGroupSampRandOutOfN'
_i='psampGroupSampTimeBased'
_h='psampGroupSampCountBased'
_g='psampFiltHashOutputRangeMax'
_f='psampFiltHashOutputRangeMin'
_e='psampFiltHashSelectedRangeMax'
_d='psampFiltHashSelectedRangeMin'
_c='psampFiltHashIpPayloadSize'
_b='psampFiltHashIpPayloadOffset'
_a='psampFiltHashInitializerValue'
_Z='psampFiltHashFunction'
_Y='psampFiltHashAvail'
_X='psampFiltPropMatchAvail'
_W='psampSampUniProbProbability'
_V='psampSampUniProbAvail'
_U='psampSampRandOutOfNPopulation'
_T='psampSampRandOutOfNSize'
_S='psampSampRandOutOfNAvail'
_R='psampSampTimeBasedSpace'
_Q='psampSampTimeBasedInterval'
_P='psampSampTimeBasedAvail'
_O='psampSampCountBasedSpace'
_N='psampSampCountBasedInterval'
_M='psampSampCountBasedAvail'
_L='psampFiltHashIndex'
_K='psampSampUniProbIndex'
_J='psampSampRandOutOfNIndex'
_I='microseconds'
_H='psampSampTimeBasedIndex'
_G='psampSampCountBasedIndex'
_F='packets'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='PSAMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Unsigned64TC,=mibBuilder.importSymbols('APPLICATION-MIB','Unsigned64TC')
Float64TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float64TC')
ipfixSelectorFunctions,=mibBuilder.importSymbols('IPFIX-SELECTOR-MIB','ipfixSelectorFunctions')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
psampMIB=ModuleIdentity((1,3,6,1,2,1,212))
if mibBuilder.loadTexts:psampMIB.setRevisions(('2012-09-05 12:00',))
_PsampSampCountBased_ObjectIdentity=ObjectIdentity
psampSampCountBased=_PsampSampCountBased_ObjectIdentity((1,3,6,1,2,1,194,1,1,2))
_PsampSampCountBasedAvail_Type=TruthValue
_PsampSampCountBasedAvail_Object=MibScalar
psampSampCountBasedAvail=_PsampSampCountBasedAvail_Object((1,3,6,1,2,1,194,1,1,2,1),_PsampSampCountBasedAvail_Type())
psampSampCountBasedAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampCountBasedAvail.setStatus(_A)
_PsampSampCountBasedParamSetTable_Object=MibTable
psampSampCountBasedParamSetTable=_PsampSampCountBasedParamSetTable_Object((1,3,6,1,2,1,194,1,1,2,2))
if mibBuilder.loadTexts:psampSampCountBasedParamSetTable.setStatus(_A)
_PsampSampCountBasedParamSetEntry_Object=MibTableRow
psampSampCountBasedParamSetEntry=_PsampSampCountBasedParamSetEntry_Object((1,3,6,1,2,1,194,1,1,2,2,1))
psampSampCountBasedParamSetEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:psampSampCountBasedParamSetEntry.setStatus(_A)
class _PsampSampCountBasedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsampSampCountBasedIndex_Type.__name__=_D
_PsampSampCountBasedIndex_Object=MibTableColumn
psampSampCountBasedIndex=_PsampSampCountBasedIndex_Object((1,3,6,1,2,1,194,1,1,2,2,1,1),_PsampSampCountBasedIndex_Type())
psampSampCountBasedIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:psampSampCountBasedIndex.setStatus(_A)
_PsampSampCountBasedInterval_Type=Unsigned32
_PsampSampCountBasedInterval_Object=MibTableColumn
psampSampCountBasedInterval=_PsampSampCountBasedInterval_Object((1,3,6,1,2,1,194,1,1,2,2,1,2),_PsampSampCountBasedInterval_Type())
psampSampCountBasedInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampCountBasedInterval.setStatus(_A)
if mibBuilder.loadTexts:psampSampCountBasedInterval.setUnits(_F)
_PsampSampCountBasedSpace_Type=Unsigned32
_PsampSampCountBasedSpace_Object=MibTableColumn
psampSampCountBasedSpace=_PsampSampCountBasedSpace_Object((1,3,6,1,2,1,194,1,1,2,2,1,3),_PsampSampCountBasedSpace_Type())
psampSampCountBasedSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampCountBasedSpace.setStatus(_A)
if mibBuilder.loadTexts:psampSampCountBasedSpace.setUnits(_F)
_PsampSampTimeBased_ObjectIdentity=ObjectIdentity
psampSampTimeBased=_PsampSampTimeBased_ObjectIdentity((1,3,6,1,2,1,194,1,1,3))
_PsampSampTimeBasedAvail_Type=TruthValue
_PsampSampTimeBasedAvail_Object=MibScalar
psampSampTimeBasedAvail=_PsampSampTimeBasedAvail_Object((1,3,6,1,2,1,194,1,1,3,1),_PsampSampTimeBasedAvail_Type())
psampSampTimeBasedAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampTimeBasedAvail.setStatus(_A)
_PsampSampTimeBasedParamSetTable_Object=MibTable
psampSampTimeBasedParamSetTable=_PsampSampTimeBasedParamSetTable_Object((1,3,6,1,2,1,194,1,1,3,2))
if mibBuilder.loadTexts:psampSampTimeBasedParamSetTable.setStatus(_A)
_PsampSampTimeBasedParamSetEntry_Object=MibTableRow
psampSampTimeBasedParamSetEntry=_PsampSampTimeBasedParamSetEntry_Object((1,3,6,1,2,1,194,1,1,3,2,1))
psampSampTimeBasedParamSetEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:psampSampTimeBasedParamSetEntry.setStatus(_A)
class _PsampSampTimeBasedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsampSampTimeBasedIndex_Type.__name__=_D
_PsampSampTimeBasedIndex_Object=MibTableColumn
psampSampTimeBasedIndex=_PsampSampTimeBasedIndex_Object((1,3,6,1,2,1,194,1,1,3,2,1,1),_PsampSampTimeBasedIndex_Type())
psampSampTimeBasedIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:psampSampTimeBasedIndex.setStatus(_A)
_PsampSampTimeBasedInterval_Type=Unsigned32
_PsampSampTimeBasedInterval_Object=MibTableColumn
psampSampTimeBasedInterval=_PsampSampTimeBasedInterval_Object((1,3,6,1,2,1,194,1,1,3,2,1,2),_PsampSampTimeBasedInterval_Type())
psampSampTimeBasedInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampTimeBasedInterval.setStatus(_A)
if mibBuilder.loadTexts:psampSampTimeBasedInterval.setUnits(_I)
_PsampSampTimeBasedSpace_Type=Unsigned32
_PsampSampTimeBasedSpace_Object=MibTableColumn
psampSampTimeBasedSpace=_PsampSampTimeBasedSpace_Object((1,3,6,1,2,1,194,1,1,3,2,1,3),_PsampSampTimeBasedSpace_Type())
psampSampTimeBasedSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampTimeBasedSpace.setStatus(_A)
if mibBuilder.loadTexts:psampSampTimeBasedSpace.setUnits(_I)
_PsampSampRandOutOfN_ObjectIdentity=ObjectIdentity
psampSampRandOutOfN=_PsampSampRandOutOfN_ObjectIdentity((1,3,6,1,2,1,194,1,1,4))
_PsampSampRandOutOfNAvail_Type=TruthValue
_PsampSampRandOutOfNAvail_Object=MibScalar
psampSampRandOutOfNAvail=_PsampSampRandOutOfNAvail_Object((1,3,6,1,2,1,194,1,1,4,1),_PsampSampRandOutOfNAvail_Type())
psampSampRandOutOfNAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampRandOutOfNAvail.setStatus(_A)
_PsampSampRandOutOfNParamSetTable_Object=MibTable
psampSampRandOutOfNParamSetTable=_PsampSampRandOutOfNParamSetTable_Object((1,3,6,1,2,1,194,1,1,4,2))
if mibBuilder.loadTexts:psampSampRandOutOfNParamSetTable.setStatus(_A)
_PsampSampRandOutOfNParamSetEntry_Object=MibTableRow
psampSampRandOutOfNParamSetEntry=_PsampSampRandOutOfNParamSetEntry_Object((1,3,6,1,2,1,194,1,1,4,2,1))
psampSampRandOutOfNParamSetEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:psampSampRandOutOfNParamSetEntry.setStatus(_A)
class _PsampSampRandOutOfNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsampSampRandOutOfNIndex_Type.__name__=_D
_PsampSampRandOutOfNIndex_Object=MibTableColumn
psampSampRandOutOfNIndex=_PsampSampRandOutOfNIndex_Object((1,3,6,1,2,1,194,1,1,4,2,1,1),_PsampSampRandOutOfNIndex_Type())
psampSampRandOutOfNIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:psampSampRandOutOfNIndex.setStatus(_A)
_PsampSampRandOutOfNSize_Type=Unsigned32
_PsampSampRandOutOfNSize_Object=MibTableColumn
psampSampRandOutOfNSize=_PsampSampRandOutOfNSize_Object((1,3,6,1,2,1,194,1,1,4,2,1,2),_PsampSampRandOutOfNSize_Type())
psampSampRandOutOfNSize.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampRandOutOfNSize.setStatus(_A)
if mibBuilder.loadTexts:psampSampRandOutOfNSize.setUnits(_F)
_PsampSampRandOutOfNPopulation_Type=Unsigned32
_PsampSampRandOutOfNPopulation_Object=MibTableColumn
psampSampRandOutOfNPopulation=_PsampSampRandOutOfNPopulation_Object((1,3,6,1,2,1,194,1,1,4,2,1,3),_PsampSampRandOutOfNPopulation_Type())
psampSampRandOutOfNPopulation.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampRandOutOfNPopulation.setStatus(_A)
if mibBuilder.loadTexts:psampSampRandOutOfNPopulation.setUnits(_F)
_PsampSampUniProb_ObjectIdentity=ObjectIdentity
psampSampUniProb=_PsampSampUniProb_ObjectIdentity((1,3,6,1,2,1,194,1,1,5))
_PsampSampUniProbAvail_Type=TruthValue
_PsampSampUniProbAvail_Object=MibScalar
psampSampUniProbAvail=_PsampSampUniProbAvail_Object((1,3,6,1,2,1,194,1,1,5,1),_PsampSampUniProbAvail_Type())
psampSampUniProbAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampUniProbAvail.setStatus(_A)
_PsampSampUniProbParamSetTable_Object=MibTable
psampSampUniProbParamSetTable=_PsampSampUniProbParamSetTable_Object((1,3,6,1,2,1,194,1,1,5,2))
if mibBuilder.loadTexts:psampSampUniProbParamSetTable.setStatus(_A)
_PsampSampUniProbParamSetEntry_Object=MibTableRow
psampSampUniProbParamSetEntry=_PsampSampUniProbParamSetEntry_Object((1,3,6,1,2,1,194,1,1,5,2,1))
psampSampUniProbParamSetEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:psampSampUniProbParamSetEntry.setStatus(_A)
class _PsampSampUniProbIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsampSampUniProbIndex_Type.__name__=_D
_PsampSampUniProbIndex_Object=MibTableColumn
psampSampUniProbIndex=_PsampSampUniProbIndex_Object((1,3,6,1,2,1,194,1,1,5,2,1,1),_PsampSampUniProbIndex_Type())
psampSampUniProbIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:psampSampUniProbIndex.setStatus(_A)
_PsampSampUniProbProbability_Type=Float64TC
_PsampSampUniProbProbability_Object=MibTableColumn
psampSampUniProbProbability=_PsampSampUniProbProbability_Object((1,3,6,1,2,1,194,1,1,5,2,1,2),_PsampSampUniProbProbability_Type())
psampSampUniProbProbability.setMaxAccess(_C)
if mibBuilder.loadTexts:psampSampUniProbProbability.setStatus(_A)
_PsampFiltPropMatch_ObjectIdentity=ObjectIdentity
psampFiltPropMatch=_PsampFiltPropMatch_ObjectIdentity((1,3,6,1,2,1,194,1,1,6))
_PsampFiltPropMatchAvail_Type=TruthValue
_PsampFiltPropMatchAvail_Object=MibScalar
psampFiltPropMatchAvail=_PsampFiltPropMatchAvail_Object((1,3,6,1,2,1,194,1,1,6,1),_PsampFiltPropMatchAvail_Type())
psampFiltPropMatchAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltPropMatchAvail.setStatus(_A)
_PsampFiltHash_ObjectIdentity=ObjectIdentity
psampFiltHash=_PsampFiltHash_ObjectIdentity((1,3,6,1,2,1,194,1,1,7))
_PsampFiltHashAvail_Type=TruthValue
_PsampFiltHashAvail_Object=MibScalar
psampFiltHashAvail=_PsampFiltHashAvail_Object((1,3,6,1,2,1,194,1,1,7,1),_PsampFiltHashAvail_Type())
psampFiltHashAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashAvail.setStatus(_A)
_PsampFiltHashCapabilities_ObjectIdentity=ObjectIdentity
psampFiltHashCapabilities=_PsampFiltHashCapabilities_ObjectIdentity((1,3,6,1,2,1,194,1,1,7,2))
_PsampFiltHashParamSetTable_Object=MibTable
psampFiltHashParamSetTable=_PsampFiltHashParamSetTable_Object((1,3,6,1,2,1,194,1,1,7,3))
if mibBuilder.loadTexts:psampFiltHashParamSetTable.setStatus(_A)
_PsampFiltHashParamSetEntry_Object=MibTableRow
psampFiltHashParamSetEntry=_PsampFiltHashParamSetEntry_Object((1,3,6,1,2,1,194,1,1,7,3,1))
psampFiltHashParamSetEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:psampFiltHashParamSetEntry.setStatus(_A)
class _PsampFiltHashIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsampFiltHashIndex_Type.__name__=_D
_PsampFiltHashIndex_Object=MibTableColumn
psampFiltHashIndex=_PsampFiltHashIndex_Object((1,3,6,1,2,1,194,1,1,7,3,1,1),_PsampFiltHashIndex_Type())
psampFiltHashIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:psampFiltHashIndex.setStatus(_A)
class _PsampFiltHashFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('crc32',1),('ipsx',2),('bob',3)))
_PsampFiltHashFunction_Type.__name__=_D
_PsampFiltHashFunction_Object=MibTableColumn
psampFiltHashFunction=_PsampFiltHashFunction_Object((1,3,6,1,2,1,194,1,1,7,3,1,2),_PsampFiltHashFunction_Type())
psampFiltHashFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashFunction.setStatus(_A)
_PsampFiltHashInitializerValue_Type=Unsigned64TC
_PsampFiltHashInitializerValue_Object=MibTableColumn
psampFiltHashInitializerValue=_PsampFiltHashInitializerValue_Object((1,3,6,1,2,1,194,1,1,7,3,1,3),_PsampFiltHashInitializerValue_Type())
psampFiltHashInitializerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashInitializerValue.setStatus(_A)
_PsampFiltHashIpPayloadOffset_Type=Unsigned64TC
_PsampFiltHashIpPayloadOffset_Object=MibTableColumn
psampFiltHashIpPayloadOffset=_PsampFiltHashIpPayloadOffset_Object((1,3,6,1,2,1,194,1,1,7,3,1,4),_PsampFiltHashIpPayloadOffset_Type())
psampFiltHashIpPayloadOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashIpPayloadOffset.setStatus(_A)
_PsampFiltHashIpPayloadSize_Type=Unsigned64TC
_PsampFiltHashIpPayloadSize_Object=MibTableColumn
psampFiltHashIpPayloadSize=_PsampFiltHashIpPayloadSize_Object((1,3,6,1,2,1,194,1,1,7,3,1,5),_PsampFiltHashIpPayloadSize_Type())
psampFiltHashIpPayloadSize.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashIpPayloadSize.setStatus(_A)
_PsampFiltHashSelectedRangeMin_Type=Unsigned64TC
_PsampFiltHashSelectedRangeMin_Object=MibTableColumn
psampFiltHashSelectedRangeMin=_PsampFiltHashSelectedRangeMin_Object((1,3,6,1,2,1,194,1,1,7,3,1,6),_PsampFiltHashSelectedRangeMin_Type())
psampFiltHashSelectedRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashSelectedRangeMin.setStatus(_A)
_PsampFiltHashSelectedRangeMax_Type=Unsigned64TC
_PsampFiltHashSelectedRangeMax_Object=MibTableColumn
psampFiltHashSelectedRangeMax=_PsampFiltHashSelectedRangeMax_Object((1,3,6,1,2,1,194,1,1,7,3,1,7),_PsampFiltHashSelectedRangeMax_Type())
psampFiltHashSelectedRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashSelectedRangeMax.setStatus(_A)
_PsampFiltHashOutputRangeMin_Type=Unsigned64TC
_PsampFiltHashOutputRangeMin_Object=MibTableColumn
psampFiltHashOutputRangeMin=_PsampFiltHashOutputRangeMin_Object((1,3,6,1,2,1,194,1,1,7,3,1,8),_PsampFiltHashOutputRangeMin_Type())
psampFiltHashOutputRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashOutputRangeMin.setStatus(_A)
_PsampFiltHashOutputRangeMax_Type=Unsigned64TC
_PsampFiltHashOutputRangeMax_Object=MibTableColumn
psampFiltHashOutputRangeMax=_PsampFiltHashOutputRangeMax_Object((1,3,6,1,2,1,194,1,1,7,3,1,9),_PsampFiltHashOutputRangeMax_Type())
psampFiltHashOutputRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:psampFiltHashOutputRangeMax.setStatus(_A)
_PsampObjects_ObjectIdentity=ObjectIdentity
psampObjects=_PsampObjects_ObjectIdentity((1,3,6,1,2,1,212,1))
_PsampConformance_ObjectIdentity=ObjectIdentity
psampConformance=_PsampConformance_ObjectIdentity((1,3,6,1,2,1,212,2))
_PsampCompliances_ObjectIdentity=ObjectIdentity
psampCompliances=_PsampCompliances_ObjectIdentity((1,3,6,1,2,1,212,2,1))
_PsampGroups_ObjectIdentity=ObjectIdentity
psampGroups=_PsampGroups_ObjectIdentity((1,3,6,1,2,1,212,2,2))
psampGroupSampCountBased=ObjectGroup((1,3,6,1,2,1,212,2,2,1))
psampGroupSampCountBased.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:psampGroupSampCountBased.setStatus(_A)
psampGroupSampTimeBased=ObjectGroup((1,3,6,1,2,1,212,2,2,2))
psampGroupSampTimeBased.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:psampGroupSampTimeBased.setStatus(_A)
psampGroupSampRandOutOfN=ObjectGroup((1,3,6,1,2,1,212,2,2,3))
psampGroupSampRandOutOfN.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:psampGroupSampRandOutOfN.setStatus(_A)
psampGroupSampUniProb=ObjectGroup((1,3,6,1,2,1,212,2,2,4))
psampGroupSampUniProb.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:psampGroupSampUniProb.setStatus(_A)
psampGroupFiltPropMatch=ObjectGroup((1,3,6,1,2,1,212,2,2,5))
psampGroupFiltPropMatch.setObjects((_B,_X))
if mibBuilder.loadTexts:psampGroupFiltPropMatch.setStatus(_A)
psampGroupFiltHash=ObjectGroup((1,3,6,1,2,1,212,2,2,6))
psampGroupFiltHash.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:psampGroupFiltHash.setStatus(_A)
psampCompliance=ModuleCompliance((1,3,6,1,2,1,212,2,1,1))
psampCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:psampCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'psampSampCountBased':psampSampCountBased,_M:psampSampCountBasedAvail,'psampSampCountBasedParamSetTable':psampSampCountBasedParamSetTable,'psampSampCountBasedParamSetEntry':psampSampCountBasedParamSetEntry,_G:psampSampCountBasedIndex,_N:psampSampCountBasedInterval,_O:psampSampCountBasedSpace,'psampSampTimeBased':psampSampTimeBased,_P:psampSampTimeBasedAvail,'psampSampTimeBasedParamSetTable':psampSampTimeBasedParamSetTable,'psampSampTimeBasedParamSetEntry':psampSampTimeBasedParamSetEntry,_H:psampSampTimeBasedIndex,_Q:psampSampTimeBasedInterval,_R:psampSampTimeBasedSpace,'psampSampRandOutOfN':psampSampRandOutOfN,_S:psampSampRandOutOfNAvail,'psampSampRandOutOfNParamSetTable':psampSampRandOutOfNParamSetTable,'psampSampRandOutOfNParamSetEntry':psampSampRandOutOfNParamSetEntry,_J:psampSampRandOutOfNIndex,_T:psampSampRandOutOfNSize,_U:psampSampRandOutOfNPopulation,'psampSampUniProb':psampSampUniProb,_V:psampSampUniProbAvail,'psampSampUniProbParamSetTable':psampSampUniProbParamSetTable,'psampSampUniProbParamSetEntry':psampSampUniProbParamSetEntry,_K:psampSampUniProbIndex,_W:psampSampUniProbProbability,'psampFiltPropMatch':psampFiltPropMatch,_X:psampFiltPropMatchAvail,'psampFiltHash':psampFiltHash,_Y:psampFiltHashAvail,'psampFiltHashCapabilities':psampFiltHashCapabilities,'psampFiltHashParamSetTable':psampFiltHashParamSetTable,'psampFiltHashParamSetEntry':psampFiltHashParamSetEntry,_L:psampFiltHashIndex,_Z:psampFiltHashFunction,_a:psampFiltHashInitializerValue,_b:psampFiltHashIpPayloadOffset,_c:psampFiltHashIpPayloadSize,_d:psampFiltHashSelectedRangeMin,_e:psampFiltHashSelectedRangeMax,_f:psampFiltHashOutputRangeMin,_g:psampFiltHashOutputRangeMax,'psampMIB':psampMIB,'psampObjects':psampObjects,'psampConformance':psampConformance,'psampCompliances':psampCompliances,'psampCompliance':psampCompliance,'psampGroups':psampGroups,_h:psampGroupSampCountBased,_i:psampGroupSampTimeBased,_j:psampGroupSampRandOutOfN,_k:psampGroupSampUniProb,_l:psampGroupFiltPropMatch,_m:psampGroupFiltHash})