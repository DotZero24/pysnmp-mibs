_q='alaLbdTrapsGroup'
_p='alaLbdStateTrapForAutoRecoveryGroup'
_o='alaLbdStateTrapForClearViolationAllGroup'
_n='alaLbdStateTrapToShutdownGroup'
_m='alaLbdPortStatusGroup'
_l='alaLbdIntfConfigGroup'
_k='alaLbdGlobalConfigGroup'
_j='alaLbdStateChangeToShutdown'
_i='alaLbdStateChangeForClearViolationAll'
_h='alaLbdStateChangeForAutoRecovery'
_g='alaLbdPortStatsClear'
_f='alaLbdPortLbdSent'
_e='alaLbdPortNumLbdInvalidRcvd'
_d='alaLbdPortConfigLbdOperStatus'
_c='alaLbdPortConfigLbdAdminStatus'
_b='alaLbdGlobalConfigAutorecoveryTimer'
_a='alaLbdGlobalClearPortStat'
_Z='alaLbdGlobalConfigTransmissionTimer'
_Y='alaLbdGlobalConfigStatus'
_X='alaLbdPortStatsIfIndex'
_W='not-accessible'
_V='alaLbdPortConfigIfIndex'
_U='default'
_T='seconds'
_S='disable'
_R='enable'
_Q='inactive'
_P='alaLbdCurrentStateAutoRecovery'
_O='alaLbdPreviousStateAutoRecovery'
_N='alaLbdCurrentStateClearViolationAll'
_M='alaLbdPreviousStateClearViolationAll'
_L='alaLbdCurrentState'
_K='alaLbdPreviousState'
_J='read-only'
_I='normal'
_H='Unsigned32'
_G='alaLbdPortIfIndex'
_F='shutdown'
_E='read-write'
_D='accessible-for-notify'
_C='Integer32'
_B='ALCATEL-IND1-LBD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alaLbdTraps,softentIND1Lbd=mibBuilder.importSymbols('ALCATEL-IND1-BASE','alaLbdTraps','softentIND1Lbd')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1LBDMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIB.setRevisions(('2008-12-10 00:00',))
class AlaLbdPortConfigLbdOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_I,1),(_F,2)))
class AlaLbdCurrentStateCVAorAR(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_I,1)))
_AlcatelIND1LBDMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBObjects=_AlcatelIND1LBDMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIBObjects.setStatus(_A)
class _AlaLbdGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AlaLbdGlobalConfigStatus_Type.__name__=_C
_AlaLbdGlobalConfigStatus_Object=MibScalar
alaLbdGlobalConfigStatus=_AlaLbdGlobalConfigStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,1),_AlaLbdGlobalConfigStatus_Type())
alaLbdGlobalConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdGlobalConfigStatus.setStatus(_A)
class _AlaLbdGlobalConfigTransmissionTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_AlaLbdGlobalConfigTransmissionTimer_Type.__name__=_H
_AlaLbdGlobalConfigTransmissionTimer_Object=MibScalar
alaLbdGlobalConfigTransmissionTimer=_AlaLbdGlobalConfigTransmissionTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,2),_AlaLbdGlobalConfigTransmissionTimer_Type())
alaLbdGlobalConfigTransmissionTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdGlobalConfigTransmissionTimer.setStatus(_A)
if mibBuilder.loadTexts:alaLbdGlobalConfigTransmissionTimer.setUnits(_T)
class _AlaLbdGlobalClearPortStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),('reset',1)))
_AlaLbdGlobalClearPortStat_Type.__name__=_C
_AlaLbdGlobalClearPortStat_Object=MibScalar
alaLbdGlobalClearPortStat=_AlaLbdGlobalClearPortStat_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,3),_AlaLbdGlobalClearPortStat_Type())
alaLbdGlobalClearPortStat.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdGlobalClearPortStat.setStatus(_A)
class _AlaLbdGlobalConfigAutorecoveryTimer_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_AlaLbdGlobalConfigAutorecoveryTimer_Type.__name__=_H
_AlaLbdGlobalConfigAutorecoveryTimer_Object=MibScalar
alaLbdGlobalConfigAutorecoveryTimer=_AlaLbdGlobalConfigAutorecoveryTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,4),_AlaLbdGlobalConfigAutorecoveryTimer_Type())
alaLbdGlobalConfigAutorecoveryTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdGlobalConfigAutorecoveryTimer.setStatus(_A)
if mibBuilder.loadTexts:alaLbdGlobalConfigAutorecoveryTimer.setUnits(_T)
_AlaLbdPortConfig_ObjectIdentity=ObjectIdentity
alaLbdPortConfig=_AlaLbdPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5))
_AlaLbdPortConfigTable_Object=MibTable
alaLbdPortConfigTable=_AlaLbdPortConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5,1))
if mibBuilder.loadTexts:alaLbdPortConfigTable.setStatus(_A)
_AlaLbdPortConfigEntry_Object=MibTableRow
alaLbdPortConfigEntry=_AlaLbdPortConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5,1,1))
alaLbdPortConfigEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:alaLbdPortConfigEntry.setStatus(_A)
_AlaLbdPortConfigIfIndex_Type=InterfaceIndex
_AlaLbdPortConfigIfIndex_Object=MibTableColumn
alaLbdPortConfigIfIndex=_AlaLbdPortConfigIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5,1,1,1),_AlaLbdPortConfigIfIndex_Type())
alaLbdPortConfigIfIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:alaLbdPortConfigIfIndex.setStatus(_A)
class _AlaLbdPortConfigLbdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AlaLbdPortConfigLbdAdminStatus_Type.__name__=_C
_AlaLbdPortConfigLbdAdminStatus_Object=MibTableColumn
alaLbdPortConfigLbdAdminStatus=_AlaLbdPortConfigLbdAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5,1,1,2),_AlaLbdPortConfigLbdAdminStatus_Type())
alaLbdPortConfigLbdAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortConfigLbdAdminStatus.setStatus(_A)
_AlaLbdPortConfigLbdOperStatus_Type=AlaLbdPortConfigLbdOperStatus
_AlaLbdPortConfigLbdOperStatus_Object=MibTableColumn
alaLbdPortConfigLbdOperStatus=_AlaLbdPortConfigLbdOperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,5,1,1,3),_AlaLbdPortConfigLbdOperStatus_Type())
alaLbdPortConfigLbdOperStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:alaLbdPortConfigLbdOperStatus.setStatus(_A)
_AlaLbdPortStat_ObjectIdentity=ObjectIdentity
alaLbdPortStat=_AlaLbdPortStat_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6))
_AlaLbdPortStatsTable_Object=MibTable
alaLbdPortStatsTable=_AlaLbdPortStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1))
if mibBuilder.loadTexts:alaLbdPortStatsTable.setStatus(_A)
_AlaLbdPortStatsEntry_Object=MibTableRow
alaLbdPortStatsEntry=_AlaLbdPortStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1,1))
alaLbdPortStatsEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:alaLbdPortStatsEntry.setStatus(_A)
_AlaLbdPortStatsIfIndex_Type=InterfaceIndex
_AlaLbdPortStatsIfIndex_Object=MibTableColumn
alaLbdPortStatsIfIndex=_AlaLbdPortStatsIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1,1,1),_AlaLbdPortStatsIfIndex_Type())
alaLbdPortStatsIfIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:alaLbdPortStatsIfIndex.setStatus(_A)
_AlaLbdPortNumLbdInvalidRcvd_Type=Counter32
_AlaLbdPortNumLbdInvalidRcvd_Object=MibTableColumn
alaLbdPortNumLbdInvalidRcvd=_AlaLbdPortNumLbdInvalidRcvd_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1,1,2),_AlaLbdPortNumLbdInvalidRcvd_Type())
alaLbdPortNumLbdInvalidRcvd.setMaxAccess(_J)
if mibBuilder.loadTexts:alaLbdPortNumLbdInvalidRcvd.setStatus(_A)
_AlaLbdPortLbdSent_Type=Counter32
_AlaLbdPortLbdSent_Object=MibTableColumn
alaLbdPortLbdSent=_AlaLbdPortLbdSent_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1,1,3),_AlaLbdPortLbdSent_Type())
alaLbdPortLbdSent.setMaxAccess(_J)
if mibBuilder.loadTexts:alaLbdPortLbdSent.setStatus(_A)
class _AlaLbdPortStatsClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),('reset',1)))
_AlaLbdPortStatsClear_Type.__name__=_C
_AlaLbdPortStatsClear_Object=MibTableColumn
alaLbdPortStatsClear=_AlaLbdPortStatsClear_Object((1,3,6,1,4,1,6486,800,1,2,1,56,1,1,6,1,1,4),_AlaLbdPortStatsClear_Type())
alaLbdPortStatsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLbdPortStatsClear.setStatus(_A)
_AlcatelIND1LBDMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBConformance=_AlcatelIND1LBDMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,2))
if mibBuilder.loadTexts:alcatelIND1LBDMIBConformance.setStatus(_A)
_AlcatelIND1LBDMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBGroups=_AlcatelIND1LBDMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1))
if mibBuilder.loadTexts:alcatelIND1LBDMIBGroups.setStatus(_A)
_AlcatelIND1LBDMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1LBDMIBCompliances=_AlcatelIND1LBDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,2))
if mibBuilder.loadTexts:alcatelIND1LBDMIBCompliances.setStatus(_A)
_AlaLbdTrapsDesc_ObjectIdentity=ObjectIdentity
alaLbdTrapsDesc=_AlaLbdTrapsDesc_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,22,1))
_AlaLbdTrapsRoot_ObjectIdentity=ObjectIdentity
alaLbdTrapsRoot=_AlaLbdTrapsRoot_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,22,1,0))
_AlaLbdTrapsObj_ObjectIdentity=ObjectIdentity
alaLbdTrapsObj=_AlaLbdTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,22,2))
_AlaLbdPortIfIndex_Type=InterfaceIndex
_AlaLbdPortIfIndex_Object=MibScalar
alaLbdPortIfIndex=_AlaLbdPortIfIndex_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,1),_AlaLbdPortIfIndex_Type())
alaLbdPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPortIfIndex.setStatus(_A)
class _AlaLbdPreviousState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_AlaLbdPreviousState_Type.__name__=_C
_AlaLbdPreviousState_Object=MibScalar
alaLbdPreviousState=_AlaLbdPreviousState_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,2),_AlaLbdPreviousState_Type())
alaLbdPreviousState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPreviousState.setStatus(_A)
class _AlaLbdCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_AlaLbdCurrentState_Type.__name__=_C
_AlaLbdCurrentState_Object=MibScalar
alaLbdCurrentState=_AlaLbdCurrentState_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,3),_AlaLbdCurrentState_Type())
alaLbdCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdCurrentState.setStatus(_A)
class _AlaLbdPreviousStateClearViolationAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_AlaLbdPreviousStateClearViolationAll_Type.__name__=_C
_AlaLbdPreviousStateClearViolationAll_Object=MibScalar
alaLbdPreviousStateClearViolationAll=_AlaLbdPreviousStateClearViolationAll_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,4),_AlaLbdPreviousStateClearViolationAll_Type())
alaLbdPreviousStateClearViolationAll.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPreviousStateClearViolationAll.setStatus(_A)
_AlaLbdCurrentStateClearViolationAll_Type=AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateClearViolationAll_Object=MibScalar
alaLbdCurrentStateClearViolationAll=_AlaLbdCurrentStateClearViolationAll_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,5),_AlaLbdCurrentStateClearViolationAll_Type())
alaLbdCurrentStateClearViolationAll.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdCurrentStateClearViolationAll.setStatus(_A)
class _AlaLbdPreviousStateAutoRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_F,1))
_AlaLbdPreviousStateAutoRecovery_Type.__name__=_C
_AlaLbdPreviousStateAutoRecovery_Object=MibScalar
alaLbdPreviousStateAutoRecovery=_AlaLbdPreviousStateAutoRecovery_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,6),_AlaLbdPreviousStateAutoRecovery_Type())
alaLbdPreviousStateAutoRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdPreviousStateAutoRecovery.setStatus(_A)
_AlaLbdCurrentStateAutoRecovery_Type=AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateAutoRecovery_Object=MibScalar
alaLbdCurrentStateAutoRecovery=_AlaLbdCurrentStateAutoRecovery_Object((1,3,6,1,4,1,6486,800,1,3,2,22,2,7),_AlaLbdCurrentStateAutoRecovery_Type())
alaLbdCurrentStateAutoRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLbdCurrentStateAutoRecovery.setStatus(_A)
alaLbdGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,1))
alaLbdGlobalConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:alaLbdGlobalConfigGroup.setStatus(_A)
alaLbdIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,2))
alaLbdIntfConfigGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:alaLbdIntfConfigGroup.setStatus(_A)
alaLbdPortStatusGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,3))
alaLbdPortStatusGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:alaLbdPortStatusGroup.setStatus(_A)
alaLbdStateTrapToShutdownGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,4))
alaLbdStateTrapToShutdownGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaLbdStateTrapToShutdownGroup.setStatus(_A)
alaLbdStateTrapForClearViolationAllGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,5))
alaLbdStateTrapForClearViolationAllGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaLbdStateTrapForClearViolationAllGroup.setStatus(_A)
alaLbdStateTrapForAutoRecoveryGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,6))
alaLbdStateTrapForAutoRecoveryGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alaLbdStateTrapForAutoRecoveryGroup.setStatus(_A)
alaLbdStateChangeToShutdown=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,22,1,0,1))
alaLbdStateChangeToShutdown.setObjects(*((_B,_G),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaLbdStateChangeToShutdown.setStatus(_A)
alaLbdStateChangeForClearViolationAll=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,22,1,0,2))
alaLbdStateChangeForClearViolationAll.setObjects(*((_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaLbdStateChangeForClearViolationAll.setStatus(_A)
alaLbdStateChangeForAutoRecovery=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,22,1,0,3))
alaLbdStateChangeForAutoRecovery.setObjects(*((_B,_G),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alaLbdStateChangeForAutoRecovery.setStatus(_A)
alaLbdTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,1,7))
alaLbdTrapsGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:alaLbdTrapsGroup.setStatus(_A)
alcatelIND1LBDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,56,1,2,2,1))
alcatelIND1LBDMIBCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alcatelIND1LBDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaLbdPortConfigLbdOperStatus':AlaLbdPortConfigLbdOperStatus,'AlaLbdCurrentStateCVAorAR':AlaLbdCurrentStateCVAorAR,'alcatelIND1LBDMIB':alcatelIND1LBDMIB,'alcatelIND1LBDMIBObjects':alcatelIND1LBDMIBObjects,_Y:alaLbdGlobalConfigStatus,_Z:alaLbdGlobalConfigTransmissionTimer,_a:alaLbdGlobalClearPortStat,_b:alaLbdGlobalConfigAutorecoveryTimer,'alaLbdPortConfig':alaLbdPortConfig,'alaLbdPortConfigTable':alaLbdPortConfigTable,'alaLbdPortConfigEntry':alaLbdPortConfigEntry,_V:alaLbdPortConfigIfIndex,_c:alaLbdPortConfigLbdAdminStatus,_d:alaLbdPortConfigLbdOperStatus,'alaLbdPortStat':alaLbdPortStat,'alaLbdPortStatsTable':alaLbdPortStatsTable,'alaLbdPortStatsEntry':alaLbdPortStatsEntry,_X:alaLbdPortStatsIfIndex,_e:alaLbdPortNumLbdInvalidRcvd,_f:alaLbdPortLbdSent,_g:alaLbdPortStatsClear,'alcatelIND1LBDMIBConformance':alcatelIND1LBDMIBConformance,'alcatelIND1LBDMIBGroups':alcatelIND1LBDMIBGroups,_k:alaLbdGlobalConfigGroup,_l:alaLbdIntfConfigGroup,_m:alaLbdPortStatusGroup,_n:alaLbdStateTrapToShutdownGroup,_o:alaLbdStateTrapForClearViolationAllGroup,_p:alaLbdStateTrapForAutoRecoveryGroup,_q:alaLbdTrapsGroup,'alcatelIND1LBDMIBCompliances':alcatelIND1LBDMIBCompliances,'alcatelIND1LBDMIBCompliance':alcatelIND1LBDMIBCompliance,'alaLbdTrapsDesc':alaLbdTrapsDesc,'alaLbdTrapsRoot':alaLbdTrapsRoot,_j:alaLbdStateChangeToShutdown,_i:alaLbdStateChangeForClearViolationAll,_h:alaLbdStateChangeForAutoRecovery,'alaLbdTrapsObj':alaLbdTrapsObj,_G:alaLbdPortIfIndex,_K:alaLbdPreviousState,_L:alaLbdCurrentState,_M:alaLbdPreviousStateClearViolationAll,_N:alaLbdCurrentStateClearViolationAll,_O:alaLbdPreviousStateAutoRecovery,_P:alaLbdCurrentStateAutoRecovery})