_l='alaCfmDelayResultGroup'
_k='alaCfmMepGroup'
_j='alaCfmBaseGroup'
_i='alaCfmDelayResultVariation'
_h='alaCfmDelayResultTestDelay'
_g='alaCfmDelayResultRMepIdentifier'
_f='alaCfmMepRFPEnabled'
_e='alaCfmMepTWDTPriority'
_d='alaCfmMepTWDTRMepIdentifier'
_c='alaCfmMepTWDTMacAddress'
_b='alaCfmMepOWDTPriority'
_a='alaCfmMepOWDTRMepIdentifier'
_Z='alaCfmMepOWDTMacAddress'
_Y='alaCfmMepClearStats'
_X='alaCfmGlobalTWDClear'
_W='alaCfmGlobalOWDClear'
_V='alaCfmGlobalClearStats'
_U='alaCfmMepEntry'
_T='microseconds'
_S='not-accessible'
_R='alaCfmDelayResultRMepMacAddress'
_Q='alaCfmDelayResultType'
_P='000000000000'
_O='dot1agCfmMepIdentifier'
_N='dot1agCfmMdIndex'
_M='dot1agCfmMaIndex'
_L='read-only'
_K='read-write'
_J='MacAddress'
_I='Unsigned32'
_H='reset'
_G='default'
_F='TruthValue'
_E='IEEE8021-CFM-MIB'
_D='Integer32'
_C='read-create'
_B='ALCATEL-IND1-ETHERNET-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1EthernetOam,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1EthernetOam')
Dot1agCfmMepId,Dot1agCfmMepIdOrZero,dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepEntry,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_E,'Dot1agCfmMepId','Dot1agCfmMepIdOrZero',_M,_N,'dot1agCfmMepEntry',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_J,'PhysAddress','TextualConvention',_F)
alcatelIND1EoamMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1))
if mibBuilder.loadTexts:alcatelIND1EoamMIB.setRevisions(('2009-09-08 00:00',))
_AlcatelIND1CfmMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1CfmMIBObjects=_AlcatelIND1CfmMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,1))
if mibBuilder.loadTexts:alcatelIND1CfmMIBObjects.setStatus(_A)
_AlaCfmBase_ObjectIdentity=ObjectIdentity
alaCfmBase=_AlaCfmBase_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,1))
class _AlaCfmGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaCfmGlobalClearStats_Type.__name__=_D
_AlaCfmGlobalClearStats_Object=MibScalar
alaCfmGlobalClearStats=_AlaCfmGlobalClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,1,1),_AlaCfmGlobalClearStats_Type())
alaCfmGlobalClearStats.setMaxAccess(_K)
if mibBuilder.loadTexts:alaCfmGlobalClearStats.setStatus(_A)
class _AlaCfmGlobalOWDClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaCfmGlobalOWDClear_Type.__name__=_D
_AlaCfmGlobalOWDClear_Object=MibScalar
alaCfmGlobalOWDClear=_AlaCfmGlobalOWDClear_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,1,2),_AlaCfmGlobalOWDClear_Type())
alaCfmGlobalOWDClear.setMaxAccess(_K)
if mibBuilder.loadTexts:alaCfmGlobalOWDClear.setStatus(_A)
class _AlaCfmGlobalTWDClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaCfmGlobalTWDClear_Type.__name__=_D
_AlaCfmGlobalTWDClear_Object=MibScalar
alaCfmGlobalTWDClear=_AlaCfmGlobalTWDClear_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,1,3),_AlaCfmGlobalTWDClear_Type())
alaCfmGlobalTWDClear.setMaxAccess(_K)
if mibBuilder.loadTexts:alaCfmGlobalTWDClear.setStatus(_A)
_AlaCfmMep_ObjectIdentity=ObjectIdentity
alaCfmMep=_AlaCfmMep_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2))
_AlaCfmMepTable_Object=MibTable
alaCfmMepTable=_AlaCfmMepTable_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1))
if mibBuilder.loadTexts:alaCfmMepTable.setStatus(_A)
_AlaCfmMepEntry_Object=MibTableRow
alaCfmMepEntry=_AlaCfmMepEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1))
if mibBuilder.loadTexts:alaCfmMepEntry.setStatus(_A)
class _AlaCfmMepClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaCfmMepClearStats_Type.__name__=_D
_AlaCfmMepClearStats_Object=MibTableColumn
alaCfmMepClearStats=_AlaCfmMepClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,1),_AlaCfmMepClearStats_Type())
alaCfmMepClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepClearStats.setStatus(_A)
class _AlaCfmMepOWDTMacAddress_Type(MacAddress):defaultHexValue=_P
_AlaCfmMepOWDTMacAddress_Type.__name__=_J
_AlaCfmMepOWDTMacAddress_Object=MibTableColumn
alaCfmMepOWDTMacAddress=_AlaCfmMepOWDTMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,2),_AlaCfmMepOWDTMacAddress_Type())
alaCfmMepOWDTMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepOWDTMacAddress.setStatus(_A)
_AlaCfmMepOWDTRMepIdentifier_Type=Dot1agCfmMepId
_AlaCfmMepOWDTRMepIdentifier_Object=MibTableColumn
alaCfmMepOWDTRMepIdentifier=_AlaCfmMepOWDTRMepIdentifier_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,3),_AlaCfmMepOWDTRMepIdentifier_Type())
alaCfmMepOWDTRMepIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepOWDTRMepIdentifier.setStatus(_A)
class _AlaCfmMepOWDTPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AlaCfmMepOWDTPriority_Type.__name__=_I
_AlaCfmMepOWDTPriority_Object=MibTableColumn
alaCfmMepOWDTPriority=_AlaCfmMepOWDTPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,4),_AlaCfmMepOWDTPriority_Type())
alaCfmMepOWDTPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepOWDTPriority.setStatus(_A)
class _AlaCfmMepTWDTMacAddress_Type(MacAddress):defaultHexValue=_P
_AlaCfmMepTWDTMacAddress_Type.__name__=_J
_AlaCfmMepTWDTMacAddress_Object=MibTableColumn
alaCfmMepTWDTMacAddress=_AlaCfmMepTWDTMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,5),_AlaCfmMepTWDTMacAddress_Type())
alaCfmMepTWDTMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepTWDTMacAddress.setStatus(_A)
_AlaCfmMepTWDTRMepIdentifier_Type=Dot1agCfmMepId
_AlaCfmMepTWDTRMepIdentifier_Object=MibTableColumn
alaCfmMepTWDTRMepIdentifier=_AlaCfmMepTWDTRMepIdentifier_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,6),_AlaCfmMepTWDTRMepIdentifier_Type())
alaCfmMepTWDTRMepIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepTWDTRMepIdentifier.setStatus(_A)
class _AlaCfmMepTWDTPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AlaCfmMepTWDTPriority_Type.__name__=_I
_AlaCfmMepTWDTPriority_Object=MibTableColumn
alaCfmMepTWDTPriority=_AlaCfmMepTWDTPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,7),_AlaCfmMepTWDTPriority_Type())
alaCfmMepTWDTPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepTWDTPriority.setStatus(_A)
class _AlaCfmMepRFPEnabled_Type(TruthValue):defaultValue=2
_AlaCfmMepRFPEnabled_Type.__name__=_F
_AlaCfmMepRFPEnabled_Object=MibTableColumn
alaCfmMepRFPEnabled=_AlaCfmMepRFPEnabled_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,8),_AlaCfmMepRFPEnabled_Type())
alaCfmMepRFPEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepRFPEnabled.setStatus(_A)
class _AlaCfmMepPortStatusTlv_Type(TruthValue):defaultValue=1
_AlaCfmMepPortStatusTlv_Type.__name__=_F
_AlaCfmMepPortStatusTlv_Object=MibTableColumn
alaCfmMepPortStatusTlv=_AlaCfmMepPortStatusTlv_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,9),_AlaCfmMepPortStatusTlv_Type())
alaCfmMepPortStatusTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepPortStatusTlv.setStatus(_A)
class _AlaCfmMepIfStatusTlv_Type(TruthValue):defaultValue=1
_AlaCfmMepIfStatusTlv_Type.__name__=_F
_AlaCfmMepIfStatusTlv_Object=MibTableColumn
alaCfmMepIfStatusTlv=_AlaCfmMepIfStatusTlv_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,2,1,1,10),_AlaCfmMepIfStatusTlv_Type())
alaCfmMepIfStatusTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCfmMepIfStatusTlv.setStatus(_A)
_AlaCfmDelayResult_ObjectIdentity=ObjectIdentity
alaCfmDelayResult=_AlaCfmDelayResult_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3))
_AlaCfmDelayResultTable_Object=MibTable
alaCfmDelayResultTable=_AlaCfmDelayResultTable_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1))
if mibBuilder.loadTexts:alaCfmDelayResultTable.setStatus(_A)
_AlaCfmDelayResultEntry_Object=MibTableRow
alaCfmDelayResultEntry=_AlaCfmDelayResultEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1))
alaCfmDelayResultEntry.setIndexNames((0,_E,_N),(0,_E,_M),(0,_E,_O),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:alaCfmDelayResultEntry.setStatus(_A)
class _AlaCfmDelayResultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneWayTest',1),('twoWayTest',2)))
_AlaCfmDelayResultType_Type.__name__=_D
_AlaCfmDelayResultType_Object=MibTableColumn
alaCfmDelayResultType=_AlaCfmDelayResultType_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1,1),_AlaCfmDelayResultType_Type())
alaCfmDelayResultType.setMaxAccess(_S)
if mibBuilder.loadTexts:alaCfmDelayResultType.setStatus(_A)
_AlaCfmDelayResultRMepMacAddress_Type=MacAddress
_AlaCfmDelayResultRMepMacAddress_Object=MibTableColumn
alaCfmDelayResultRMepMacAddress=_AlaCfmDelayResultRMepMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1,2),_AlaCfmDelayResultRMepMacAddress_Type())
alaCfmDelayResultRMepMacAddress.setMaxAccess(_S)
if mibBuilder.loadTexts:alaCfmDelayResultRMepMacAddress.setStatus(_A)
_AlaCfmDelayResultRMepIdentifier_Type=Dot1agCfmMepIdOrZero
_AlaCfmDelayResultRMepIdentifier_Object=MibTableColumn
alaCfmDelayResultRMepIdentifier=_AlaCfmDelayResultRMepIdentifier_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1,3),_AlaCfmDelayResultRMepIdentifier_Type())
alaCfmDelayResultRMepIdentifier.setMaxAccess(_L)
if mibBuilder.loadTexts:alaCfmDelayResultRMepIdentifier.setStatus(_A)
_AlaCfmDelayResultTestDelay_Type=Integer32
_AlaCfmDelayResultTestDelay_Object=MibTableColumn
alaCfmDelayResultTestDelay=_AlaCfmDelayResultTestDelay_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1,4),_AlaCfmDelayResultTestDelay_Type())
alaCfmDelayResultTestDelay.setMaxAccess(_L)
if mibBuilder.loadTexts:alaCfmDelayResultTestDelay.setStatus(_A)
if mibBuilder.loadTexts:alaCfmDelayResultTestDelay.setUnits(_T)
_AlaCfmDelayResultVariation_Type=Unsigned32
_AlaCfmDelayResultVariation_Object=MibTableColumn
alaCfmDelayResultVariation=_AlaCfmDelayResultVariation_Object((1,3,6,1,4,1,6486,800,1,2,1,40,1,1,3,1,1,5),_AlaCfmDelayResultVariation_Type())
alaCfmDelayResultVariation.setMaxAccess(_L)
if mibBuilder.loadTexts:alaCfmDelayResultVariation.setStatus(_A)
if mibBuilder.loadTexts:alaCfmDelayResultVariation.setUnits(_T)
_AlaCfmConformance_ObjectIdentity=ObjectIdentity
alaCfmConformance=_AlaCfmConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,2))
_AlaCfmGroups_ObjectIdentity=ObjectIdentity
alaCfmGroups=_AlaCfmGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,1))
_AlaCfmCompliances_ObjectIdentity=ObjectIdentity
alaCfmCompliances=_AlaCfmCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,2))
dot1agCfmMepEntry.registerAugmentions((_B,_U))
alaCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
alaCfmBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,1,1))
alaCfmBaseGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:alaCfmBaseGroup.setStatus(_A)
alaCfmMepGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,1,2))
alaCfmMepGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:alaCfmMepGroup.setStatus(_A)
alaCfmDelayResultGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,1,3))
alaCfmDelayResultGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:alaCfmDelayResultGroup.setStatus(_A)
alaCfmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,40,1,2,2,1))
alaCfmCompliance.setObjects(*((_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaCfmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1EoamMIB':alcatelIND1EoamMIB,'alcatelIND1CfmMIBObjects':alcatelIND1CfmMIBObjects,'alaCfmBase':alaCfmBase,_V:alaCfmGlobalClearStats,_W:alaCfmGlobalOWDClear,_X:alaCfmGlobalTWDClear,'alaCfmMep':alaCfmMep,'alaCfmMepTable':alaCfmMepTable,_U:alaCfmMepEntry,_Y:alaCfmMepClearStats,_Z:alaCfmMepOWDTMacAddress,_a:alaCfmMepOWDTRMepIdentifier,_b:alaCfmMepOWDTPriority,_c:alaCfmMepTWDTMacAddress,_d:alaCfmMepTWDTRMepIdentifier,_e:alaCfmMepTWDTPriority,_f:alaCfmMepRFPEnabled,'alaCfmMepPortStatusTlv':alaCfmMepPortStatusTlv,'alaCfmMepIfStatusTlv':alaCfmMepIfStatusTlv,'alaCfmDelayResult':alaCfmDelayResult,'alaCfmDelayResultTable':alaCfmDelayResultTable,'alaCfmDelayResultEntry':alaCfmDelayResultEntry,_Q:alaCfmDelayResultType,_R:alaCfmDelayResultRMepMacAddress,_g:alaCfmDelayResultRMepIdentifier,_h:alaCfmDelayResultTestDelay,_i:alaCfmDelayResultVariation,'alaCfmConformance':alaCfmConformance,'alaCfmGroups':alaCfmGroups,_j:alaCfmBaseGroup,_k:alaCfmMepGroup,_l:alaCfmDelayResultGroup,'alaCfmCompliances':alaCfmCompliances,'alaCfmCompliance':alaCfmCompliance})