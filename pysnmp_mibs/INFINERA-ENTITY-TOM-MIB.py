_n='tomGroup'
_m='tomIs3rdPartyTom'
_l='tomRxCtleEqValue'
_k='tomRxCtleOverride'
_j='tomHighPowerEnable'
_i='tomRx34Amplitude'
_h='tomRx12Amplitude'
_g='tomRx34Emphasis'
_f='tomRx12Emphasis'
_e='tomTx34Eq'
_d='tomTx12Eq'
_c='tomTxEq'
_b='tomTxPost3'
_a='tomTxPoshDn'
_Z='tomTxPoshUp'
_Y='tomTxIPreDrv'
_X='tomTxIDrv'
_W='tomTxPre'
_V='tomTxPost2'
_U='tomTxPost1'
_T='tomTxVod'
_S='tomTxAmplitude'
_R='tomSerdesOverride'
_Q='tomPhyMode'
_P='tomInstalledWavelength'
_O='tomProvisionedWavelength'
_N='tomProvisionedFrequency'
_M='tomRxPowerThresholdPcentge'
_L='tomTxPowerThresholdPcentge'
_K='tomSFPState'
_J='tomProvEqptType'
_I='tomMoId'
_H='tomInstalledFrequency'
_G='Integer32'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-TOM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnPhyMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType','InfnPhyMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
tomMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,9))
_TomTable_Object=MibTable
tomTable=_TomTable_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1))
if mibBuilder.loadTexts:tomTable.setStatus(_A)
_TomEntry_Object=MibTableRow
tomEntry=_TomEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1))
tomEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tomEntry.setStatus(_A)
_TomMoId_Type=DisplayString
_TomMoId_Object=MibTableColumn
tomMoId=_TomMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,1),_TomMoId_Type())
tomMoId.setMaxAccess('read-create')
if mibBuilder.loadTexts:tomMoId.setStatus(_A)
_TomProvEqptType_Type=InfnEqptType
_TomProvEqptType_Object=MibTableColumn
tomProvEqptType=_TomProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,2),_TomProvEqptType_Type())
tomProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:tomProvEqptType.setStatus(_A)
class _TomSFPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('locked',1),('maintenance',2),('unlocked',3)))
_TomSFPState_Type.__name__=_G
_TomSFPState_Object=MibTableColumn
tomSFPState=_TomSFPState_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,3),_TomSFPState_Type())
tomSFPState.setMaxAccess(_D)
if mibBuilder.loadTexts:tomSFPState.setStatus(_A)
_TomTxPowerThresholdPcentge_Type=Unsigned32
_TomTxPowerThresholdPcentge_Object=MibTableColumn
tomTxPowerThresholdPcentge=_TomTxPowerThresholdPcentge_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,4),_TomTxPowerThresholdPcentge_Type())
tomTxPowerThresholdPcentge.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPowerThresholdPcentge.setStatus(_A)
_TomRxPowerThresholdPcentge_Type=Unsigned32
_TomRxPowerThresholdPcentge_Object=MibTableColumn
tomRxPowerThresholdPcentge=_TomRxPowerThresholdPcentge_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,5),_TomRxPowerThresholdPcentge_Type())
tomRxPowerThresholdPcentge.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRxPowerThresholdPcentge.setStatus(_A)
_TomProvisionedFrequency_Type=Unsigned32
_TomProvisionedFrequency_Object=MibTableColumn
tomProvisionedFrequency=_TomProvisionedFrequency_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,6),_TomProvisionedFrequency_Type())
tomProvisionedFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:tomProvisionedFrequency.setStatus(_A)
_TomInstalledFrequency_Type=Unsigned32
_TomInstalledFrequency_Object=MibTableColumn
tomInstalledFrequency=_TomInstalledFrequency_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,7),_TomInstalledFrequency_Type())
tomInstalledFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:tomInstalledFrequency.setStatus(_A)
_TomProvisionedWavelength_Type=Unsigned32
_TomProvisionedWavelength_Object=MibTableColumn
tomProvisionedWavelength=_TomProvisionedWavelength_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,8),_TomProvisionedWavelength_Type())
tomProvisionedWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:tomProvisionedWavelength.setStatus(_A)
_TomInstalledWavelength_Type=Unsigned32
_TomInstalledWavelength_Object=MibTableColumn
tomInstalledWavelength=_TomInstalledWavelength_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,9),_TomInstalledWavelength_Type())
tomInstalledWavelength.setMaxAccess(_D)
if mibBuilder.loadTexts:tomInstalledWavelength.setStatus(_A)
_TomPhyMode_Type=InfnPhyMode
_TomPhyMode_Object=MibTableColumn
tomPhyMode=_TomPhyMode_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,10),_TomPhyMode_Type())
tomPhyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tomPhyMode.setStatus(_A)
_TomSerdesOverride_Type=TruthValue
_TomSerdesOverride_Object=MibTableColumn
tomSerdesOverride=_TomSerdesOverride_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,11),_TomSerdesOverride_Type())
tomSerdesOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:tomSerdesOverride.setStatus(_A)
_TomTxAmplitude_Type=Integer32
_TomTxAmplitude_Object=MibTableColumn
tomTxAmplitude=_TomTxAmplitude_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,12),_TomTxAmplitude_Type())
tomTxAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxAmplitude.setStatus(_A)
_TomTxVod_Type=Integer32
_TomTxVod_Object=MibTableColumn
tomTxVod=_TomTxVod_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,13),_TomTxVod_Type())
tomTxVod.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxVod.setStatus(_A)
_TomTxPost1_Type=Integer32
_TomTxPost1_Object=MibTableColumn
tomTxPost1=_TomTxPost1_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,14),_TomTxPost1_Type())
tomTxPost1.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPost1.setStatus(_A)
_TomTxPost2_Type=Integer32
_TomTxPost2_Object=MibTableColumn
tomTxPost2=_TomTxPost2_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,15),_TomTxPost2_Type())
tomTxPost2.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPost2.setStatus(_A)
_TomTxPre_Type=Integer32
_TomTxPre_Object=MibTableColumn
tomTxPre=_TomTxPre_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,16),_TomTxPre_Type())
tomTxPre.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPre.setStatus(_A)
_TomTxIDrv_Type=Integer32
_TomTxIDrv_Object=MibTableColumn
tomTxIDrv=_TomTxIDrv_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,17),_TomTxIDrv_Type())
tomTxIDrv.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxIDrv.setStatus(_A)
_TomTxIPreDrv_Type=Integer32
_TomTxIPreDrv_Object=MibTableColumn
tomTxIPreDrv=_TomTxIPreDrv_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,18),_TomTxIPreDrv_Type())
tomTxIPreDrv.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxIPreDrv.setStatus(_A)
_TomTxPoshUp_Type=Integer32
_TomTxPoshUp_Object=MibTableColumn
tomTxPoshUp=_TomTxPoshUp_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,19),_TomTxPoshUp_Type())
tomTxPoshUp.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPoshUp.setStatus(_A)
_TomTxPoshDn_Type=Integer32
_TomTxPoshDn_Object=MibTableColumn
tomTxPoshDn=_TomTxPoshDn_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,20),_TomTxPoshDn_Type())
tomTxPoshDn.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPoshDn.setStatus(_A)
_TomTxPost3_Type=Integer32
_TomTxPost3_Object=MibTableColumn
tomTxPost3=_TomTxPost3_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,21),_TomTxPost3_Type())
tomTxPost3.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxPost3.setStatus(_A)
_TomTxEq_Type=Integer32
_TomTxEq_Object=MibTableColumn
tomTxEq=_TomTxEq_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,22),_TomTxEq_Type())
tomTxEq.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTxEq.setStatus(_A)
_TomTx12Eq_Type=Integer32
_TomTx12Eq_Object=MibTableColumn
tomTx12Eq=_TomTx12Eq_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,23),_TomTx12Eq_Type())
tomTx12Eq.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTx12Eq.setStatus(_A)
_TomTx34Eq_Type=Integer32
_TomTx34Eq_Object=MibTableColumn
tomTx34Eq=_TomTx34Eq_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,24),_TomTx34Eq_Type())
tomTx34Eq.setMaxAccess(_C)
if mibBuilder.loadTexts:tomTx34Eq.setStatus(_A)
_TomRx12Emphasis_Type=Integer32
_TomRx12Emphasis_Object=MibTableColumn
tomRx12Emphasis=_TomRx12Emphasis_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,25),_TomRx12Emphasis_Type())
tomRx12Emphasis.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRx12Emphasis.setStatus(_A)
_TomRx34Emphasis_Type=Integer32
_TomRx34Emphasis_Object=MibTableColumn
tomRx34Emphasis=_TomRx34Emphasis_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,26),_TomRx34Emphasis_Type())
tomRx34Emphasis.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRx34Emphasis.setStatus(_A)
_TomRx12Amplitude_Type=Integer32
_TomRx12Amplitude_Object=MibTableColumn
tomRx12Amplitude=_TomRx12Amplitude_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,27),_TomRx12Amplitude_Type())
tomRx12Amplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRx12Amplitude.setStatus(_A)
_TomRx34Amplitude_Type=Integer32
_TomRx34Amplitude_Object=MibTableColumn
tomRx34Amplitude=_TomRx34Amplitude_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,28),_TomRx34Amplitude_Type())
tomRx34Amplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRx34Amplitude.setStatus(_A)
_TomHighPowerEnable_Type=TruthValue
_TomHighPowerEnable_Object=MibTableColumn
tomHighPowerEnable=_TomHighPowerEnable_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,29),_TomHighPowerEnable_Type())
tomHighPowerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tomHighPowerEnable.setStatus(_A)
_TomRxCtleOverride_Type=TruthValue
_TomRxCtleOverride_Object=MibTableColumn
tomRxCtleOverride=_TomRxCtleOverride_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,30),_TomRxCtleOverride_Type())
tomRxCtleOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRxCtleOverride.setStatus(_A)
_TomRxCtleEqValue_Type=Integer32
_TomRxCtleEqValue_Object=MibTableColumn
tomRxCtleEqValue=_TomRxCtleEqValue_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,31),_TomRxCtleEqValue_Type())
tomRxCtleEqValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tomRxCtleEqValue.setStatus(_A)
_TomIs3rdPartyTom_Type=TruthValue
_TomIs3rdPartyTom_Object=MibTableColumn
tomIs3rdPartyTom=_TomIs3rdPartyTom_Object((1,3,6,1,4,1,21296,2,2,2,1,9,1,1,32),_TomIs3rdPartyTom_Type())
tomIs3rdPartyTom.setMaxAccess(_D)
if mibBuilder.loadTexts:tomIs3rdPartyTom.setStatus(_A)
_TomConformance_ObjectIdentity=ObjectIdentity
tomConformance=_TomConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,9,3))
_TomCompliances_ObjectIdentity=ObjectIdentity
tomCompliances=_TomCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,9,3,1))
_TomGroups_ObjectIdentity=ObjectIdentity
tomGroups=_TomGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,9,3,2))
tomGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,9,3,2,1))
tomGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tomGroup.setStatus(_A)
tomCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,9,3,1,1))
tomCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:tomCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tomMIB':tomMIB,'tomTable':tomTable,'tomEntry':tomEntry,_I:tomMoId,_J:tomProvEqptType,_K:tomSFPState,_L:tomTxPowerThresholdPcentge,_M:tomRxPowerThresholdPcentge,_N:tomProvisionedFrequency,_H:tomInstalledFrequency,_O:tomProvisionedWavelength,_P:tomInstalledWavelength,_Q:tomPhyMode,_R:tomSerdesOverride,_S:tomTxAmplitude,_T:tomTxVod,_U:tomTxPost1,_V:tomTxPost2,_W:tomTxPre,_X:tomTxIDrv,_Y:tomTxIPreDrv,_Z:tomTxPoshUp,_a:tomTxPoshDn,_b:tomTxPost3,_c:tomTxEq,_d:tomTx12Eq,_e:tomTx34Eq,_f:tomRx12Emphasis,_g:tomRx34Emphasis,_h:tomRx12Amplitude,_i:tomRx34Amplitude,_j:tomHighPowerEnable,_k:tomRxCtleOverride,_l:tomRxCtleEqValue,_m:tomIs3rdPartyTom,'tomConformance':tomConformance,'tomCompliances':tomCompliances,'tomCompliance':tomCompliance,'tomGroups':tomGroups,_n:tomGroup})