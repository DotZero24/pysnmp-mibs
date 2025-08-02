_Ad='ciscoFabricC12kOc192XbarGroup'
_Ac='ciscoFabricC12kOc192ScaGroup'
_Ab='ciscoFabricC12kOc192LCGroup'
_Aa='ciscoFabricC12kOc192FiaGroup'
_AZ='ciscoFabricC12kPreOc192XbarGroup'
_AY='ciscoFabricC12kPreOc192ScaGroup'
_AX='ciscoFabricC12kNotifGroup'
_AW='ciscoFabricC12kNotifEnableGroup'
_AV='ciscoFabricC12kPreOc192FiaGroup'
_AU='ciscoFabricC12kXbarGroup'
_AT='ciscoFabricC12kScaGroup'
_AS='ciscoFabricC12kFiaGroup'
_AR='ciscoFabricC12kGlobalGroup'
_AQ='ciscoFabricC12kMIBFabMasterSchCh'
_AP='cfcNotifEnable'
_AO='cfcOc192XbarCtrlCRCErr'
_AN='cfcOc192XbarCtrlLOSStatus'
_AM='cfcOc192ScaDisableGrants'
_AL='cfcOc192ScaRotationPeriod'
_AK='cfcGenericScaOc192LCsPresent'
_AJ='cfcOc192FabFrFabStatMCLoPktDrops'
_AI='cfcOc192FabFrFabStatMCHiPktDrops'
_AH='cfcOc192FabFrFabStatUCLoPktDrops'
_AG='cfcOc192FabFrFabStatUCHiPktDrops'
_AF='cfcOc192FabFrFabSliCellDrops'
_AE='cfcOc192FabFrFabSliXorErrs'
_AD='cfcOc192FabFrFabSeqErrs'
_AC='cfcOc192FabFrFabFirstLastErrs'
_AB='cfcOc192FabFrFabExtSramOvFlws'
_AA='cfcOc192FabFrFabHdrFifoOvFlws'
_A9='cfcOc192FabFrFabTxCtrlPEs'
_A8='cfcOc192FabFrFabHdrSramPEs'
_A7='cfcOc192FabFrFabPktLenPEs'
_A6='cfcOc192FabFrFabExtRamPEs'
_A5='cfcOc192FabFrFabPktLenErrs'
_A4='cfcOc192FabToFabMccCmdSeqStrErrs'
_A3='cfcOc192FabToFabMccCmdSeqEndErrs'
_A2='cfcOc192FabToFabCellFifoUnFlws'
_A1='cfcOc192FabToFabCellFifoOvFlws'
_A0='cfcOc192FabToFabBackPressurePEs'
_z='cfcOc192FabToFabMccCmdPEs'
_y='cfcOc192FabToFabMccDataPEs'
_x='cfcPreOc192XbarParityChkStatus'
_w='cfcPreOc192XbarIntrStatus'
_v='cfcPreOc192ScaLOSLog'
_u='cfcPreOc192ScaReSyncDelay'
_t='cfcPreOc192FabFrFabCellDrops'
_s='cfcPreOc192FabFrFabRedFifoOvflws'
_r='cfcPreOc192FabFrFabRedFifoPEs'
_q='cfcPreOc192FabFrFabCellFifoPEs'
_p='cfcPreOc192FabToFabEmptyDestRqs'
_o='cfcPreOc192FabToFabMultiDstUCRqs'
_n='cfcPreOc192FabToFabUniDestMCRqs'
_m='cfcPreOc192FabToFabBmaHskErrs'
_l='cfcPreOc192FabToFabBmaPEs'
_k='cfcPreOc192FabToFabMCFifoErrs'
_j='cfcPreOc192FabToFabUCFifoUnFlws'
_i='cfcPreOc192FabToFabUCFifoOvFlws'
_h='cfcPreOc192FabToFabScaLosts'
_g='cfcGenericXbarIdentifier'
_f='cfcGenericScaPreOc192LCsPresent'
_e='cfcGenericScaForcedBackPressure'
_d='cfcGenericScaLCsEnabled'
_c='cfcGenericScaFifoOverflowLog'
_b='cfcGenericScaPELog'
_a='cfcGenericScaConfig'
_Z='cfcGenericScaIntrsEnabled'
_Y='cfcGenericScaIntrStatus'
_X='cfcGenericScaIdentifier'
_W='cfcGenericFabFrFabSliLOSState'
_V='cfcGenericFabFrFabSliCRCErrors'
_U='cfcGenericFabFrFabSliLOSErrors'
_T='cfcGenericFabFrFabState'
_S='cfcGenericFabToFabCellFifoPEs'
_R='cfcGenericFabToFabRequestPEs'
_Q='cfcGenericFabToFabGrantPEs'
_P='cfcGenericFabToFabState'
_O='cfcGenericGlobalFabConfigMode'
_N='cfcOc192FabFrFabStatLCIndex'
_M='cfcOc192FabFrFabSliSwitchIndex'
_L='cfcGenericFabFrFabSliFabIndex'
_K='TruthValue'
_J='Integer32'
_I='entPhysicalName'
_H='cfcGenericGlobalFabMasterSched'
_G='not-accessible'
_F='Bits'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-FABRIC-C12K-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
PhysicalIndex,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_D,'PhysicalIndex',_E,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoFabricC12kMIB=ModuleIdentity((1,3,6,1,4,1,9,9,281))
if mibBuilder.loadTexts:ciscoFabricC12kMIB.setRevisions(('2002-09-20 00:00',))
class CfcFabricConfigMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('invalidMode',1),('quarterBwNonRedundant',2),('quarterBwRedundant',3),('fullBwNonRedundant',4),('fullBwRedundant',5)))
class CfcFabricFiaState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('halted',2)))
class CfcScaInterrupts(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('lossOfSync',0),('parityError',1),('overflow',2)))
class CfcSlotMask(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoFabricC12kMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFabricC12kMIBNotifs=_CiscoFabricC12kMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,281,0))
_CiscoFabricC12kMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFabricC12kMIBObjects=_CiscoFabricC12kMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,281,1))
_CfcGeneric_ObjectIdentity=ObjectIdentity
cfcGeneric=_CfcGeneric_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,1))
_CfcGenericGlobal_ObjectIdentity=ObjectIdentity
cfcGenericGlobal=_CfcGenericGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,1,1))
_CfcGenericGlobalFabConfigMode_Type=CfcFabricConfigMode
_CfcGenericGlobalFabConfigMode_Object=MibScalar
cfcGenericGlobalFabConfigMode=_CfcGenericGlobalFabConfigMode_Object((1,3,6,1,4,1,9,9,281,1,1,1,1),_CfcGenericGlobalFabConfigMode_Type())
cfcGenericGlobalFabConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericGlobalFabConfigMode.setStatus(_A)
_CfcGenericGlobalFabMasterSched_Type=EntPhysicalIndexOrZero
_CfcGenericGlobalFabMasterSched_Object=MibScalar
cfcGenericGlobalFabMasterSched=_CfcGenericGlobalFabMasterSched_Object((1,3,6,1,4,1,9,9,281,1,1,1,2),_CfcGenericGlobalFabMasterSched_Type())
cfcGenericGlobalFabMasterSched.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericGlobalFabMasterSched.setStatus(_A)
_CfcGenericFab_ObjectIdentity=ObjectIdentity
cfcGenericFab=_CfcGenericFab_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,1,2))
_CfcGenericFabToFabTable_Object=MibTable
cfcGenericFabToFabTable=_CfcGenericFabToFabTable_Object((1,3,6,1,4,1,9,9,281,1,1,2,1))
if mibBuilder.loadTexts:cfcGenericFabToFabTable.setStatus(_A)
_CfcGenericFabToFabEntry_Object=MibTableRow
cfcGenericFabToFabEntry=_CfcGenericFabToFabEntry_Object((1,3,6,1,4,1,9,9,281,1,1,2,1,1))
cfcGenericFabToFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcGenericFabToFabEntry.setStatus(_A)
_CfcGenericFabToFabState_Type=CfcFabricFiaState
_CfcGenericFabToFabState_Object=MibTableColumn
cfcGenericFabToFabState=_CfcGenericFabToFabState_Object((1,3,6,1,4,1,9,9,281,1,1,2,1,1,1),_CfcGenericFabToFabState_Type())
cfcGenericFabToFabState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabToFabState.setStatus(_A)
_CfcGenericFabToFabGrantPEs_Type=Counter32
_CfcGenericFabToFabGrantPEs_Object=MibTableColumn
cfcGenericFabToFabGrantPEs=_CfcGenericFabToFabGrantPEs_Object((1,3,6,1,4,1,9,9,281,1,1,2,1,1,2),_CfcGenericFabToFabGrantPEs_Type())
cfcGenericFabToFabGrantPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabToFabGrantPEs.setStatus(_A)
_CfcGenericFabToFabRequestPEs_Type=Counter32
_CfcGenericFabToFabRequestPEs_Object=MibTableColumn
cfcGenericFabToFabRequestPEs=_CfcGenericFabToFabRequestPEs_Object((1,3,6,1,4,1,9,9,281,1,1,2,1,1,3),_CfcGenericFabToFabRequestPEs_Type())
cfcGenericFabToFabRequestPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabToFabRequestPEs.setStatus(_A)
_CfcGenericFabToFabCellFifoPEs_Type=Counter32
_CfcGenericFabToFabCellFifoPEs_Object=MibTableColumn
cfcGenericFabToFabCellFifoPEs=_CfcGenericFabToFabCellFifoPEs_Object((1,3,6,1,4,1,9,9,281,1,1,2,1,1,4),_CfcGenericFabToFabCellFifoPEs_Type())
cfcGenericFabToFabCellFifoPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabToFabCellFifoPEs.setStatus(_A)
_CfcGenericFabFrFabTable_Object=MibTable
cfcGenericFabFrFabTable=_CfcGenericFabFrFabTable_Object((1,3,6,1,4,1,9,9,281,1,1,2,2))
if mibBuilder.loadTexts:cfcGenericFabFrFabTable.setStatus(_A)
_CfcGenericFabFrFabEntry_Object=MibTableRow
cfcGenericFabFrFabEntry=_CfcGenericFabFrFabEntry_Object((1,3,6,1,4,1,9,9,281,1,1,2,2,1))
cfcGenericFabFrFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcGenericFabFrFabEntry.setStatus(_A)
_CfcGenericFabFrFabState_Type=CfcFabricFiaState
_CfcGenericFabFrFabState_Object=MibTableColumn
cfcGenericFabFrFabState=_CfcGenericFabFrFabState_Object((1,3,6,1,4,1,9,9,281,1,1,2,2,1,1),_CfcGenericFabFrFabState_Type())
cfcGenericFabFrFabState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabFrFabState.setStatus(_A)
_CfcGenericFabFrFabSliTable_Object=MibTable
cfcGenericFabFrFabSliTable=_CfcGenericFabFrFabSliTable_Object((1,3,6,1,4,1,9,9,281,1,1,2,3))
if mibBuilder.loadTexts:cfcGenericFabFrFabSliTable.setStatus(_A)
_CfcGenericFabFrFabSliEntry_Object=MibTableRow
cfcGenericFabFrFabSliEntry=_CfcGenericFabFrFabSliEntry_Object((1,3,6,1,4,1,9,9,281,1,1,2,3,1))
cfcGenericFabFrFabSliEntry.setIndexNames((0,_D,_E),(0,_B,_L))
if mibBuilder.loadTexts:cfcGenericFabFrFabSliEntry.setStatus(_A)
_CfcGenericFabFrFabSliFabIndex_Type=PhysicalIndex
_CfcGenericFabFrFabSliFabIndex_Object=MibTableColumn
cfcGenericFabFrFabSliFabIndex=_CfcGenericFabFrFabSliFabIndex_Object((1,3,6,1,4,1,9,9,281,1,1,2,3,1,1),_CfcGenericFabFrFabSliFabIndex_Type())
cfcGenericFabFrFabSliFabIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcGenericFabFrFabSliFabIndex.setStatus(_A)
_CfcGenericFabFrFabSliLOSErrors_Type=Counter32
_CfcGenericFabFrFabSliLOSErrors_Object=MibTableColumn
cfcGenericFabFrFabSliLOSErrors=_CfcGenericFabFrFabSliLOSErrors_Object((1,3,6,1,4,1,9,9,281,1,1,2,3,1,2),_CfcGenericFabFrFabSliLOSErrors_Type())
cfcGenericFabFrFabSliLOSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabFrFabSliLOSErrors.setStatus(_A)
_CfcGenericFabFrFabSliCRCErrors_Type=Counter32
_CfcGenericFabFrFabSliCRCErrors_Object=MibTableColumn
cfcGenericFabFrFabSliCRCErrors=_CfcGenericFabFrFabSliCRCErrors_Object((1,3,6,1,4,1,9,9,281,1,1,2,3,1,3),_CfcGenericFabFrFabSliCRCErrors_Type())
cfcGenericFabFrFabSliCRCErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabFrFabSliCRCErrors.setStatus(_A)
class _CfcGenericFabFrFabSliLOSState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('losOff',1),('losOn',2)))
_CfcGenericFabFrFabSliLOSState_Type.__name__=_J
_CfcGenericFabFrFabSliLOSState_Object=MibTableColumn
cfcGenericFabFrFabSliLOSState=_CfcGenericFabFrFabSliLOSState_Object((1,3,6,1,4,1,9,9,281,1,1,2,3,1,4),_CfcGenericFabFrFabSliLOSState_Type())
cfcGenericFabFrFabSliLOSState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericFabFrFabSliLOSState.setStatus(_A)
_CfcGenericSca_ObjectIdentity=ObjectIdentity
cfcGenericSca=_CfcGenericSca_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,1,3))
_CfcGenericScaTable_Object=MibTable
cfcGenericScaTable=_CfcGenericScaTable_Object((1,3,6,1,4,1,9,9,281,1,1,3,1))
if mibBuilder.loadTexts:cfcGenericScaTable.setStatus(_A)
_CfcGenericScaEntry_Object=MibTableRow
cfcGenericScaEntry=_CfcGenericScaEntry_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1))
cfcGenericScaEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcGenericScaEntry.setStatus(_A)
_CfcGenericScaIdentifier_Type=SnmpAdminString
_CfcGenericScaIdentifier_Object=MibTableColumn
cfcGenericScaIdentifier=_CfcGenericScaIdentifier_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,1),_CfcGenericScaIdentifier_Type())
cfcGenericScaIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaIdentifier.setStatus(_A)
_CfcGenericScaIntrStatus_Type=CfcScaInterrupts
_CfcGenericScaIntrStatus_Object=MibTableColumn
cfcGenericScaIntrStatus=_CfcGenericScaIntrStatus_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,2),_CfcGenericScaIntrStatus_Type())
cfcGenericScaIntrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaIntrStatus.setStatus(_A)
_CfcGenericScaIntrsEnabled_Type=CfcScaInterrupts
_CfcGenericScaIntrsEnabled_Object=MibTableColumn
cfcGenericScaIntrsEnabled=_CfcGenericScaIntrsEnabled_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,3),_CfcGenericScaIntrsEnabled_Type())
cfcGenericScaIntrsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaIntrsEnabled.setStatus(_A)
class _CfcGenericScaConfig_Type(Bits):namedValues=NamedValues(*(('quarterBandwidth',0),('halfBandwidth',1),('fullBandwidth',2),('enableParity',3),('priMcast',4),('priUnicast',5),('priAlternating',6),('earlyIntrOnLOS',7),('noEarlyIntrOnLOS',8),('forceXbarParityXer',9),('forceGrantParityXer',10),('unicastAcceptMode',11),('forceXbarCrcOnCtlLink0',12),('forceXbarCrcOnCtlLink1',13),('forceXbarCrcOnCtlLink2',14),('forceXbarCrcOnCtlLink3',15)))
_CfcGenericScaConfig_Type.__name__=_F
_CfcGenericScaConfig_Object=MibTableColumn
cfcGenericScaConfig=_CfcGenericScaConfig_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,4),_CfcGenericScaConfig_Type())
cfcGenericScaConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaConfig.setStatus(_A)
_CfcGenericScaPELog_Type=CfcSlotMask
_CfcGenericScaPELog_Object=MibTableColumn
cfcGenericScaPELog=_CfcGenericScaPELog_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,5),_CfcGenericScaPELog_Type())
cfcGenericScaPELog.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaPELog.setStatus(_A)
_CfcGenericScaFifoOverflowLog_Type=CfcSlotMask
_CfcGenericScaFifoOverflowLog_Object=MibTableColumn
cfcGenericScaFifoOverflowLog=_CfcGenericScaFifoOverflowLog_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,6),_CfcGenericScaFifoOverflowLog_Type())
cfcGenericScaFifoOverflowLog.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaFifoOverflowLog.setStatus(_A)
_CfcGenericScaLCsEnabled_Type=CfcSlotMask
_CfcGenericScaLCsEnabled_Object=MibTableColumn
cfcGenericScaLCsEnabled=_CfcGenericScaLCsEnabled_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,7),_CfcGenericScaLCsEnabled_Type())
cfcGenericScaLCsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaLCsEnabled.setStatus(_A)
_CfcGenericScaForcedBackPressure_Type=CfcSlotMask
_CfcGenericScaForcedBackPressure_Object=MibTableColumn
cfcGenericScaForcedBackPressure=_CfcGenericScaForcedBackPressure_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,8),_CfcGenericScaForcedBackPressure_Type())
cfcGenericScaForcedBackPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaForcedBackPressure.setStatus(_A)
_CfcGenericScaOc192LCsPresent_Type=CfcSlotMask
_CfcGenericScaOc192LCsPresent_Object=MibTableColumn
cfcGenericScaOc192LCsPresent=_CfcGenericScaOc192LCsPresent_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,9),_CfcGenericScaOc192LCsPresent_Type())
cfcGenericScaOc192LCsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaOc192LCsPresent.setStatus(_A)
_CfcGenericScaPreOc192LCsPresent_Type=CfcSlotMask
_CfcGenericScaPreOc192LCsPresent_Object=MibTableColumn
cfcGenericScaPreOc192LCsPresent=_CfcGenericScaPreOc192LCsPresent_Object((1,3,6,1,4,1,9,9,281,1,1,3,1,1,10),_CfcGenericScaPreOc192LCsPresent_Type())
cfcGenericScaPreOc192LCsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericScaPreOc192LCsPresent.setStatus(_A)
_CfcGenericXbar_ObjectIdentity=ObjectIdentity
cfcGenericXbar=_CfcGenericXbar_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,1,4))
_CfcGenericXbarTable_Object=MibTable
cfcGenericXbarTable=_CfcGenericXbarTable_Object((1,3,6,1,4,1,9,9,281,1,1,4,1))
if mibBuilder.loadTexts:cfcGenericXbarTable.setStatus(_A)
_CfcGenericXbarEntry_Object=MibTableRow
cfcGenericXbarEntry=_CfcGenericXbarEntry_Object((1,3,6,1,4,1,9,9,281,1,1,4,1,1))
cfcGenericXbarEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcGenericXbarEntry.setStatus(_A)
_CfcGenericXbarIdentifier_Type=SnmpAdminString
_CfcGenericXbarIdentifier_Object=MibTableColumn
cfcGenericXbarIdentifier=_CfcGenericXbarIdentifier_Object((1,3,6,1,4,1,9,9,281,1,1,4,1,1,1),_CfcGenericXbarIdentifier_Type())
cfcGenericXbarIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcGenericXbarIdentifier.setStatus(_A)
_CfcPreOc192_ObjectIdentity=ObjectIdentity
cfcPreOc192=_CfcPreOc192_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,2))
_CfcPreOc192Fab_ObjectIdentity=ObjectIdentity
cfcPreOc192Fab=_CfcPreOc192Fab_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,2,1))
_CfcPreOc192FabToFabTable_Object=MibTable
cfcPreOc192FabToFabTable=_CfcPreOc192FabToFabTable_Object((1,3,6,1,4,1,9,9,281,1,2,1,1))
if mibBuilder.loadTexts:cfcPreOc192FabToFabTable.setStatus(_A)
_CfcPreOc192FabToFabEntry_Object=MibTableRow
cfcPreOc192FabToFabEntry=_CfcPreOc192FabToFabEntry_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1))
cfcPreOc192FabToFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcPreOc192FabToFabEntry.setStatus(_A)
_CfcPreOc192FabToFabScaLosts_Type=Counter32
_CfcPreOc192FabToFabScaLosts_Object=MibTableColumn
cfcPreOc192FabToFabScaLosts=_CfcPreOc192FabToFabScaLosts_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,1),_CfcPreOc192FabToFabScaLosts_Type())
cfcPreOc192FabToFabScaLosts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabScaLosts.setStatus(_A)
_CfcPreOc192FabToFabUCFifoOvFlws_Type=Counter32
_CfcPreOc192FabToFabUCFifoOvFlws_Object=MibTableColumn
cfcPreOc192FabToFabUCFifoOvFlws=_CfcPreOc192FabToFabUCFifoOvFlws_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,2),_CfcPreOc192FabToFabUCFifoOvFlws_Type())
cfcPreOc192FabToFabUCFifoOvFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabUCFifoOvFlws.setStatus(_A)
_CfcPreOc192FabToFabUCFifoUnFlws_Type=Counter32
_CfcPreOc192FabToFabUCFifoUnFlws_Object=MibTableColumn
cfcPreOc192FabToFabUCFifoUnFlws=_CfcPreOc192FabToFabUCFifoUnFlws_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,3),_CfcPreOc192FabToFabUCFifoUnFlws_Type())
cfcPreOc192FabToFabUCFifoUnFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabUCFifoUnFlws.setStatus(_A)
_CfcPreOc192FabToFabMCFifoErrs_Type=Counter32
_CfcPreOc192FabToFabMCFifoErrs_Object=MibTableColumn
cfcPreOc192FabToFabMCFifoErrs=_CfcPreOc192FabToFabMCFifoErrs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,4),_CfcPreOc192FabToFabMCFifoErrs_Type())
cfcPreOc192FabToFabMCFifoErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabMCFifoErrs.setStatus(_A)
_CfcPreOc192FabToFabBmaPEs_Type=Counter32
_CfcPreOc192FabToFabBmaPEs_Object=MibTableColumn
cfcPreOc192FabToFabBmaPEs=_CfcPreOc192FabToFabBmaPEs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,5),_CfcPreOc192FabToFabBmaPEs_Type())
cfcPreOc192FabToFabBmaPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabBmaPEs.setStatus(_A)
_CfcPreOc192FabToFabBmaHskErrs_Type=Counter32
_CfcPreOc192FabToFabBmaHskErrs_Object=MibTableColumn
cfcPreOc192FabToFabBmaHskErrs=_CfcPreOc192FabToFabBmaHskErrs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,6),_CfcPreOc192FabToFabBmaHskErrs_Type())
cfcPreOc192FabToFabBmaHskErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabBmaHskErrs.setStatus(_A)
_CfcPreOc192FabToFabUniDestMCRqs_Type=Counter32
_CfcPreOc192FabToFabUniDestMCRqs_Object=MibTableColumn
cfcPreOc192FabToFabUniDestMCRqs=_CfcPreOc192FabToFabUniDestMCRqs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,7),_CfcPreOc192FabToFabUniDestMCRqs_Type())
cfcPreOc192FabToFabUniDestMCRqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabUniDestMCRqs.setStatus(_A)
_CfcPreOc192FabToFabMultiDstUCRqs_Type=Counter32
_CfcPreOc192FabToFabMultiDstUCRqs_Object=MibTableColumn
cfcPreOc192FabToFabMultiDstUCRqs=_CfcPreOc192FabToFabMultiDstUCRqs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,8),_CfcPreOc192FabToFabMultiDstUCRqs_Type())
cfcPreOc192FabToFabMultiDstUCRqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabMultiDstUCRqs.setStatus(_A)
_CfcPreOc192FabToFabEmptyDestRqs_Type=Counter32
_CfcPreOc192FabToFabEmptyDestRqs_Object=MibTableColumn
cfcPreOc192FabToFabEmptyDestRqs=_CfcPreOc192FabToFabEmptyDestRqs_Object((1,3,6,1,4,1,9,9,281,1,2,1,1,1,9),_CfcPreOc192FabToFabEmptyDestRqs_Type())
cfcPreOc192FabToFabEmptyDestRqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabToFabEmptyDestRqs.setStatus(_A)
_CfcPreOc192FabFrFabTable_Object=MibTable
cfcPreOc192FabFrFabTable=_CfcPreOc192FabFrFabTable_Object((1,3,6,1,4,1,9,9,281,1,2,1,2))
if mibBuilder.loadTexts:cfcPreOc192FabFrFabTable.setStatus(_A)
_CfcPreOc192FabFrFabEntry_Object=MibTableRow
cfcPreOc192FabFrFabEntry=_CfcPreOc192FabFrFabEntry_Object((1,3,6,1,4,1,9,9,281,1,2,1,2,1))
cfcPreOc192FabFrFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcPreOc192FabFrFabEntry.setStatus(_A)
_CfcPreOc192FabFrFabCellFifoPEs_Type=Counter32
_CfcPreOc192FabFrFabCellFifoPEs_Object=MibTableColumn
cfcPreOc192FabFrFabCellFifoPEs=_CfcPreOc192FabFrFabCellFifoPEs_Object((1,3,6,1,4,1,9,9,281,1,2,1,2,1,1),_CfcPreOc192FabFrFabCellFifoPEs_Type())
cfcPreOc192FabFrFabCellFifoPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabFrFabCellFifoPEs.setStatus(_A)
_CfcPreOc192FabFrFabRedFifoPEs_Type=Counter32
_CfcPreOc192FabFrFabRedFifoPEs_Object=MibTableColumn
cfcPreOc192FabFrFabRedFifoPEs=_CfcPreOc192FabFrFabRedFifoPEs_Object((1,3,6,1,4,1,9,9,281,1,2,1,2,1,2),_CfcPreOc192FabFrFabRedFifoPEs_Type())
cfcPreOc192FabFrFabRedFifoPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabFrFabRedFifoPEs.setStatus(_A)
_CfcPreOc192FabFrFabRedFifoOvflws_Type=Counter32
_CfcPreOc192FabFrFabRedFifoOvflws_Object=MibTableColumn
cfcPreOc192FabFrFabRedFifoOvflws=_CfcPreOc192FabFrFabRedFifoOvflws_Object((1,3,6,1,4,1,9,9,281,1,2,1,2,1,3),_CfcPreOc192FabFrFabRedFifoOvflws_Type())
cfcPreOc192FabFrFabRedFifoOvflws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabFrFabRedFifoOvflws.setStatus(_A)
_CfcPreOc192FabFrFabCellDrops_Type=Counter32
_CfcPreOc192FabFrFabCellDrops_Object=MibTableColumn
cfcPreOc192FabFrFabCellDrops=_CfcPreOc192FabFrFabCellDrops_Object((1,3,6,1,4,1,9,9,281,1,2,1,2,1,4),_CfcPreOc192FabFrFabCellDrops_Type())
cfcPreOc192FabFrFabCellDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192FabFrFabCellDrops.setStatus(_A)
_CfcPreOc192Sca_ObjectIdentity=ObjectIdentity
cfcPreOc192Sca=_CfcPreOc192Sca_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,2,2))
_CfcPreOc192ScaTable_Object=MibTable
cfcPreOc192ScaTable=_CfcPreOc192ScaTable_Object((1,3,6,1,4,1,9,9,281,1,2,2,1))
if mibBuilder.loadTexts:cfcPreOc192ScaTable.setStatus(_A)
_CfcPreOc192ScaEntry_Object=MibTableRow
cfcPreOc192ScaEntry=_CfcPreOc192ScaEntry_Object((1,3,6,1,4,1,9,9,281,1,2,2,1,1))
cfcPreOc192ScaEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcPreOc192ScaEntry.setStatus(_A)
_CfcPreOc192ScaReSyncDelay_Type=Unsigned32
_CfcPreOc192ScaReSyncDelay_Object=MibTableColumn
cfcPreOc192ScaReSyncDelay=_CfcPreOc192ScaReSyncDelay_Object((1,3,6,1,4,1,9,9,281,1,2,2,1,1,1),_CfcPreOc192ScaReSyncDelay_Type())
cfcPreOc192ScaReSyncDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192ScaReSyncDelay.setStatus(_A)
_CfcPreOc192ScaLOSLog_Type=CfcSlotMask
_CfcPreOc192ScaLOSLog_Object=MibTableColumn
cfcPreOc192ScaLOSLog=_CfcPreOc192ScaLOSLog_Object((1,3,6,1,4,1,9,9,281,1,2,2,1,1,2),_CfcPreOc192ScaLOSLog_Type())
cfcPreOc192ScaLOSLog.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192ScaLOSLog.setStatus(_A)
_CfcPreOc192Xbar_ObjectIdentity=ObjectIdentity
cfcPreOc192Xbar=_CfcPreOc192Xbar_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,2,3))
_CfcPreOc192XbarTable_Object=MibTable
cfcPreOc192XbarTable=_CfcPreOc192XbarTable_Object((1,3,6,1,4,1,9,9,281,1,2,3,1))
if mibBuilder.loadTexts:cfcPreOc192XbarTable.setStatus(_A)
_CfcPreOc192XbarEntry_Object=MibTableRow
cfcPreOc192XbarEntry=_CfcPreOc192XbarEntry_Object((1,3,6,1,4,1,9,9,281,1,2,3,1,1))
cfcPreOc192XbarEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcPreOc192XbarEntry.setStatus(_A)
class _CfcPreOc192XbarIntrStatus_Type(Bits):namedValues=NamedValues(*(('frameLossOfSync',0),('parityErrorFromSca',1)))
_CfcPreOc192XbarIntrStatus_Type.__name__=_F
_CfcPreOc192XbarIntrStatus_Object=MibTableColumn
cfcPreOc192XbarIntrStatus=_CfcPreOc192XbarIntrStatus_Object((1,3,6,1,4,1,9,9,281,1,2,3,1,1,1),_CfcPreOc192XbarIntrStatus_Type())
cfcPreOc192XbarIntrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192XbarIntrStatus.setStatus(_A)
_CfcPreOc192XbarParityChkStatus_Type=TruthValue
_CfcPreOc192XbarParityChkStatus_Object=MibTableColumn
cfcPreOc192XbarParityChkStatus=_CfcPreOc192XbarParityChkStatus_Object((1,3,6,1,4,1,9,9,281,1,2,3,1,1,2),_CfcPreOc192XbarParityChkStatus_Type())
cfcPreOc192XbarParityChkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcPreOc192XbarParityChkStatus.setStatus(_A)
_CfcOc192_ObjectIdentity=ObjectIdentity
cfcOc192=_CfcOc192_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,3))
_CfcOc192Fab_ObjectIdentity=ObjectIdentity
cfcOc192Fab=_CfcOc192Fab_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,3,1))
_CfcOc192FabToFabTable_Object=MibTable
cfcOc192FabToFabTable=_CfcOc192FabToFabTable_Object((1,3,6,1,4,1,9,9,281,1,3,1,1))
if mibBuilder.loadTexts:cfcOc192FabToFabTable.setStatus(_A)
_CfcOc192FabToFabEntry_Object=MibTableRow
cfcOc192FabToFabEntry=_CfcOc192FabToFabEntry_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1))
cfcOc192FabToFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcOc192FabToFabEntry.setStatus(_A)
_CfcOc192FabToFabMccDataPEs_Type=Counter32
_CfcOc192FabToFabMccDataPEs_Object=MibTableColumn
cfcOc192FabToFabMccDataPEs=_CfcOc192FabToFabMccDataPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,1),_CfcOc192FabToFabMccDataPEs_Type())
cfcOc192FabToFabMccDataPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabMccDataPEs.setStatus(_A)
_CfcOc192FabToFabMccCmdPEs_Type=Counter32
_CfcOc192FabToFabMccCmdPEs_Object=MibTableColumn
cfcOc192FabToFabMccCmdPEs=_CfcOc192FabToFabMccCmdPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,2),_CfcOc192FabToFabMccCmdPEs_Type())
cfcOc192FabToFabMccCmdPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabMccCmdPEs.setStatus(_A)
_CfcOc192FabToFabBackPressurePEs_Type=Counter32
_CfcOc192FabToFabBackPressurePEs_Object=MibTableColumn
cfcOc192FabToFabBackPressurePEs=_CfcOc192FabToFabBackPressurePEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,3),_CfcOc192FabToFabBackPressurePEs_Type())
cfcOc192FabToFabBackPressurePEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabBackPressurePEs.setStatus(_A)
_CfcOc192FabToFabCellFifoOvFlws_Type=Counter32
_CfcOc192FabToFabCellFifoOvFlws_Object=MibTableColumn
cfcOc192FabToFabCellFifoOvFlws=_CfcOc192FabToFabCellFifoOvFlws_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,4),_CfcOc192FabToFabCellFifoOvFlws_Type())
cfcOc192FabToFabCellFifoOvFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabCellFifoOvFlws.setStatus(_A)
_CfcOc192FabToFabCellFifoUnFlws_Type=Counter32
_CfcOc192FabToFabCellFifoUnFlws_Object=MibTableColumn
cfcOc192FabToFabCellFifoUnFlws=_CfcOc192FabToFabCellFifoUnFlws_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,5),_CfcOc192FabToFabCellFifoUnFlws_Type())
cfcOc192FabToFabCellFifoUnFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabCellFifoUnFlws.setStatus(_A)
_CfcOc192FabToFabMccCmdSeqEndErrs_Type=Counter32
_CfcOc192FabToFabMccCmdSeqEndErrs_Object=MibTableColumn
cfcOc192FabToFabMccCmdSeqEndErrs=_CfcOc192FabToFabMccCmdSeqEndErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,6),_CfcOc192FabToFabMccCmdSeqEndErrs_Type())
cfcOc192FabToFabMccCmdSeqEndErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabMccCmdSeqEndErrs.setStatus(_A)
_CfcOc192FabToFabMccCmdSeqStrErrs_Type=Counter32
_CfcOc192FabToFabMccCmdSeqStrErrs_Object=MibTableColumn
cfcOc192FabToFabMccCmdSeqStrErrs=_CfcOc192FabToFabMccCmdSeqStrErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,1,1,7),_CfcOc192FabToFabMccCmdSeqStrErrs_Type())
cfcOc192FabToFabMccCmdSeqStrErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabToFabMccCmdSeqStrErrs.setStatus(_A)
_CfcOc192FabFrFabTable_Object=MibTable
cfcOc192FabFrFabTable=_CfcOc192FabFrFabTable_Object((1,3,6,1,4,1,9,9,281,1,3,1,2))
if mibBuilder.loadTexts:cfcOc192FabFrFabTable.setStatus(_A)
_CfcOc192FabFrFabEntry_Object=MibTableRow
cfcOc192FabFrFabEntry=_CfcOc192FabFrFabEntry_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1))
cfcOc192FabFrFabEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcOc192FabFrFabEntry.setStatus(_A)
_CfcOc192FabFrFabPktLenErrs_Type=Counter32
_CfcOc192FabFrFabPktLenErrs_Object=MibTableColumn
cfcOc192FabFrFabPktLenErrs=_CfcOc192FabFrFabPktLenErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,1),_CfcOc192FabFrFabPktLenErrs_Type())
cfcOc192FabFrFabPktLenErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabPktLenErrs.setStatus(_A)
_CfcOc192FabFrFabExtRamPEs_Type=Counter32
_CfcOc192FabFrFabExtRamPEs_Object=MibTableColumn
cfcOc192FabFrFabExtRamPEs=_CfcOc192FabFrFabExtRamPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,2),_CfcOc192FabFrFabExtRamPEs_Type())
cfcOc192FabFrFabExtRamPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabExtRamPEs.setStatus(_A)
_CfcOc192FabFrFabPktLenPEs_Type=Counter32
_CfcOc192FabFrFabPktLenPEs_Object=MibTableColumn
cfcOc192FabFrFabPktLenPEs=_CfcOc192FabFrFabPktLenPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,3),_CfcOc192FabFrFabPktLenPEs_Type())
cfcOc192FabFrFabPktLenPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabPktLenPEs.setStatus(_A)
_CfcOc192FabFrFabHdrSramPEs_Type=Counter32
_CfcOc192FabFrFabHdrSramPEs_Object=MibTableColumn
cfcOc192FabFrFabHdrSramPEs=_CfcOc192FabFrFabHdrSramPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,4),_CfcOc192FabFrFabHdrSramPEs_Type())
cfcOc192FabFrFabHdrSramPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabHdrSramPEs.setStatus(_A)
_CfcOc192FabFrFabTxCtrlPEs_Type=Counter32
_CfcOc192FabFrFabTxCtrlPEs_Object=MibTableColumn
cfcOc192FabFrFabTxCtrlPEs=_CfcOc192FabFrFabTxCtrlPEs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,5),_CfcOc192FabFrFabTxCtrlPEs_Type())
cfcOc192FabFrFabTxCtrlPEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabTxCtrlPEs.setStatus(_A)
_CfcOc192FabFrFabHdrFifoOvFlws_Type=Counter32
_CfcOc192FabFrFabHdrFifoOvFlws_Object=MibTableColumn
cfcOc192FabFrFabHdrFifoOvFlws=_CfcOc192FabFrFabHdrFifoOvFlws_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,6),_CfcOc192FabFrFabHdrFifoOvFlws_Type())
cfcOc192FabFrFabHdrFifoOvFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabHdrFifoOvFlws.setStatus(_A)
_CfcOc192FabFrFabExtSramOvFlws_Type=Counter32
_CfcOc192FabFrFabExtSramOvFlws_Object=MibTableColumn
cfcOc192FabFrFabExtSramOvFlws=_CfcOc192FabFrFabExtSramOvFlws_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,7),_CfcOc192FabFrFabExtSramOvFlws_Type())
cfcOc192FabFrFabExtSramOvFlws.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabExtSramOvFlws.setStatus(_A)
_CfcOc192FabFrFabFirstLastErrs_Type=Counter32
_CfcOc192FabFrFabFirstLastErrs_Object=MibTableColumn
cfcOc192FabFrFabFirstLastErrs=_CfcOc192FabFrFabFirstLastErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,8),_CfcOc192FabFrFabFirstLastErrs_Type())
cfcOc192FabFrFabFirstLastErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabFirstLastErrs.setStatus(_A)
_CfcOc192FabFrFabSeqErrs_Type=Counter32
_CfcOc192FabFrFabSeqErrs_Object=MibTableColumn
cfcOc192FabFrFabSeqErrs=_CfcOc192FabFrFabSeqErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,2,1,9),_CfcOc192FabFrFabSeqErrs_Type())
cfcOc192FabFrFabSeqErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabSeqErrs.setStatus(_A)
_CfcOc192FabFrFabSliTable_Object=MibTable
cfcOc192FabFrFabSliTable=_CfcOc192FabFrFabSliTable_Object((1,3,6,1,4,1,9,9,281,1,3,1,3))
if mibBuilder.loadTexts:cfcOc192FabFrFabSliTable.setStatus(_A)
_CfcOc192FabFrFabSliEntry_Object=MibTableRow
cfcOc192FabFrFabSliEntry=_CfcOc192FabFrFabSliEntry_Object((1,3,6,1,4,1,9,9,281,1,3,1,3,1))
cfcOc192FabFrFabSliEntry.setIndexNames((0,_D,_E),(0,_B,_M))
if mibBuilder.loadTexts:cfcOc192FabFrFabSliEntry.setStatus(_A)
_CfcOc192FabFrFabSliSwitchIndex_Type=PhysicalIndex
_CfcOc192FabFrFabSliSwitchIndex_Object=MibTableColumn
cfcOc192FabFrFabSliSwitchIndex=_CfcOc192FabFrFabSliSwitchIndex_Object((1,3,6,1,4,1,9,9,281,1,3,1,3,1,1),_CfcOc192FabFrFabSliSwitchIndex_Type())
cfcOc192FabFrFabSliSwitchIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcOc192FabFrFabSliSwitchIndex.setStatus(_A)
_CfcOc192FabFrFabSliXorErrs_Type=Counter32
_CfcOc192FabFrFabSliXorErrs_Object=MibTableColumn
cfcOc192FabFrFabSliXorErrs=_CfcOc192FabFrFabSliXorErrs_Object((1,3,6,1,4,1,9,9,281,1,3,1,3,1,2),_CfcOc192FabFrFabSliXorErrs_Type())
cfcOc192FabFrFabSliXorErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabSliXorErrs.setStatus(_A)
_CfcOc192FabFrFabSliCellDrops_Type=Counter32
_CfcOc192FabFrFabSliCellDrops_Object=MibTableColumn
cfcOc192FabFrFabSliCellDrops=_CfcOc192FabFrFabSliCellDrops_Object((1,3,6,1,4,1,9,9,281,1,3,1,3,1,3),_CfcOc192FabFrFabSliCellDrops_Type())
cfcOc192FabFrFabSliCellDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabSliCellDrops.setStatus(_A)
_CfcOc192FabFrFabStatTable_Object=MibTable
cfcOc192FabFrFabStatTable=_CfcOc192FabFrFabStatTable_Object((1,3,6,1,4,1,9,9,281,1,3,1,4))
if mibBuilder.loadTexts:cfcOc192FabFrFabStatTable.setStatus(_A)
_CfcOc192FabFrFabStatEntry_Object=MibTableRow
cfcOc192FabFrFabStatEntry=_CfcOc192FabFrFabStatEntry_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1))
cfcOc192FabFrFabStatEntry.setIndexNames((0,_D,_E),(0,_B,_N))
if mibBuilder.loadTexts:cfcOc192FabFrFabStatEntry.setStatus(_A)
_CfcOc192FabFrFabStatLCIndex_Type=PhysicalIndex
_CfcOc192FabFrFabStatLCIndex_Object=MibTableColumn
cfcOc192FabFrFabStatLCIndex=_CfcOc192FabFrFabStatLCIndex_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1,1),_CfcOc192FabFrFabStatLCIndex_Type())
cfcOc192FabFrFabStatLCIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcOc192FabFrFabStatLCIndex.setStatus(_A)
_CfcOc192FabFrFabStatUCHiPktDrops_Type=Counter32
_CfcOc192FabFrFabStatUCHiPktDrops_Object=MibTableColumn
cfcOc192FabFrFabStatUCHiPktDrops=_CfcOc192FabFrFabStatUCHiPktDrops_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1,2),_CfcOc192FabFrFabStatUCHiPktDrops_Type())
cfcOc192FabFrFabStatUCHiPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabStatUCHiPktDrops.setStatus(_A)
_CfcOc192FabFrFabStatUCLoPktDrops_Type=Counter32
_CfcOc192FabFrFabStatUCLoPktDrops_Object=MibTableColumn
cfcOc192FabFrFabStatUCLoPktDrops=_CfcOc192FabFrFabStatUCLoPktDrops_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1,3),_CfcOc192FabFrFabStatUCLoPktDrops_Type())
cfcOc192FabFrFabStatUCLoPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabStatUCLoPktDrops.setStatus(_A)
_CfcOc192FabFrFabStatMCHiPktDrops_Type=Counter32
_CfcOc192FabFrFabStatMCHiPktDrops_Object=MibTableColumn
cfcOc192FabFrFabStatMCHiPktDrops=_CfcOc192FabFrFabStatMCHiPktDrops_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1,4),_CfcOc192FabFrFabStatMCHiPktDrops_Type())
cfcOc192FabFrFabStatMCHiPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabStatMCHiPktDrops.setStatus(_A)
_CfcOc192FabFrFabStatMCLoPktDrops_Type=Counter32
_CfcOc192FabFrFabStatMCLoPktDrops_Object=MibTableColumn
cfcOc192FabFrFabStatMCLoPktDrops=_CfcOc192FabFrFabStatMCLoPktDrops_Object((1,3,6,1,4,1,9,9,281,1,3,1,4,1,5),_CfcOc192FabFrFabStatMCLoPktDrops_Type())
cfcOc192FabFrFabStatMCLoPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192FabFrFabStatMCLoPktDrops.setStatus(_A)
_CfcOc192Sca_ObjectIdentity=ObjectIdentity
cfcOc192Sca=_CfcOc192Sca_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,3,2))
_CfcOc192ScaTable_Object=MibTable
cfcOc192ScaTable=_CfcOc192ScaTable_Object((1,3,6,1,4,1,9,9,281,1,3,2,1))
if mibBuilder.loadTexts:cfcOc192ScaTable.setStatus(_A)
_CfcOc192ScaEntry_Object=MibTableRow
cfcOc192ScaEntry=_CfcOc192ScaEntry_Object((1,3,6,1,4,1,9,9,281,1,3,2,1,1))
cfcOc192ScaEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcOc192ScaEntry.setStatus(_A)
_CfcOc192ScaRotationPeriod_Type=Unsigned32
_CfcOc192ScaRotationPeriod_Object=MibTableColumn
cfcOc192ScaRotationPeriod=_CfcOc192ScaRotationPeriod_Object((1,3,6,1,4,1,9,9,281,1,3,2,1,1,1),_CfcOc192ScaRotationPeriod_Type())
cfcOc192ScaRotationPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192ScaRotationPeriod.setStatus(_A)
_CfcOc192ScaDisableGrants_Type=CfcSlotMask
_CfcOc192ScaDisableGrants_Object=MibTableColumn
cfcOc192ScaDisableGrants=_CfcOc192ScaDisableGrants_Object((1,3,6,1,4,1,9,9,281,1,3,2,1,1,2),_CfcOc192ScaDisableGrants_Type())
cfcOc192ScaDisableGrants.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192ScaDisableGrants.setStatus(_A)
_CfcOc192Xbar_ObjectIdentity=ObjectIdentity
cfcOc192Xbar=_CfcOc192Xbar_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,3,3))
_CfcOc192XbarTable_Object=MibTable
cfcOc192XbarTable=_CfcOc192XbarTable_Object((1,3,6,1,4,1,9,9,281,1,3,3,1))
if mibBuilder.loadTexts:cfcOc192XbarTable.setStatus(_A)
_CfcOc192XbarEntry_Object=MibTableRow
cfcOc192XbarEntry=_CfcOc192XbarEntry_Object((1,3,6,1,4,1,9,9,281,1,3,3,1,1))
cfcOc192XbarEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcOc192XbarEntry.setStatus(_A)
class _CfcOc192XbarCtrlLOSStatus_Type(Bits):namedValues=NamedValues(*(('frameLosErr',0),('sliErrorOnControlLink0',1),('sliErrorOnControlLink1',2),('sliErrorOnControlLink2',3),('sliErrorOnControlLink3',4)))
_CfcOc192XbarCtrlLOSStatus_Type.__name__=_F
_CfcOc192XbarCtrlLOSStatus_Object=MibTableColumn
cfcOc192XbarCtrlLOSStatus=_CfcOc192XbarCtrlLOSStatus_Object((1,3,6,1,4,1,9,9,281,1,3,3,1,1,1),_CfcOc192XbarCtrlLOSStatus_Type())
cfcOc192XbarCtrlLOSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192XbarCtrlLOSStatus.setStatus(_A)
class _CfcOc192XbarCtrlCRCErr_Type(Bits):namedValues=NamedValues(*(('ctlCrcErrorLink0',0),('ctlCrcErrorLink1',1),('ctlCrcErrorLink2',2),('ctlCrcErrorLink3',3)))
_CfcOc192XbarCtrlCRCErr_Type.__name__=_F
_CfcOc192XbarCtrlCRCErr_Object=MibTableColumn
cfcOc192XbarCtrlCRCErr=_CfcOc192XbarCtrlCRCErr_Object((1,3,6,1,4,1,9,9,281,1,3,3,1,1,2),_CfcOc192XbarCtrlCRCErr_Type())
cfcOc192XbarCtrlCRCErr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcOc192XbarCtrlCRCErr.setStatus(_A)
_CfcNotif_ObjectIdentity=ObjectIdentity
cfcNotif=_CfcNotif_ObjectIdentity((1,3,6,1,4,1,9,9,281,1,4))
class _CfcNotifEnable_Type(TruthValue):defaultValue=2
_CfcNotifEnable_Type.__name__=_K
_CfcNotifEnable_Object=MibScalar
cfcNotifEnable=_CfcNotifEnable_Object((1,3,6,1,4,1,9,9,281,1,4,1),_CfcNotifEnable_Type())
cfcNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cfcNotifEnable.setStatus(_A)
_CiscoFabricC12kMIBConform_ObjectIdentity=ObjectIdentity
ciscoFabricC12kMIBConform=_CiscoFabricC12kMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,281,2))
_CiscoFabricC12kMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFabricC12kMIBCompliances=_CiscoFabricC12kMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,281,2,1))
_CiscoFabricC12kMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFabricC12kMIBGroups=_CiscoFabricC12kMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,281,2,2))
ciscoFabricC12kGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,1))
ciscoFabricC12kGlobalGroup.setObjects(*((_B,_O),(_B,_H)))
if mibBuilder.loadTexts:ciscoFabricC12kGlobalGroup.setStatus(_A)
ciscoFabricC12kFiaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,2))
ciscoFabricC12kFiaGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoFabricC12kFiaGroup.setStatus(_A)
ciscoFabricC12kScaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,3))
ciscoFabricC12kScaGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoFabricC12kScaGroup.setStatus(_A)
ciscoFabricC12kXbarGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,4))
ciscoFabricC12kXbarGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:ciscoFabricC12kXbarGroup.setStatus(_A)
ciscoFabricC12kPreOc192FiaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,5))
ciscoFabricC12kPreOc192FiaGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoFabricC12kPreOc192FiaGroup.setStatus(_A)
ciscoFabricC12kPreOc192ScaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,6))
ciscoFabricC12kPreOc192ScaGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoFabricC12kPreOc192ScaGroup.setStatus(_A)
ciscoFabricC12kPreOc192XbarGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,7))
ciscoFabricC12kPreOc192XbarGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoFabricC12kPreOc192XbarGroup.setStatus(_A)
ciscoFabricC12kOc192FiaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,8))
ciscoFabricC12kOc192FiaGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:ciscoFabricC12kOc192FiaGroup.setStatus(_A)
ciscoFabricC12kOc192LCGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,9))
ciscoFabricC12kOc192LCGroup.setObjects((_B,_AK))
if mibBuilder.loadTexts:ciscoFabricC12kOc192LCGroup.setStatus(_A)
ciscoFabricC12kOc192ScaGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,10))
ciscoFabricC12kOc192ScaGroup.setObjects(*((_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:ciscoFabricC12kOc192ScaGroup.setStatus(_A)
ciscoFabricC12kOc192XbarGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,11))
ciscoFabricC12kOc192XbarGroup.setObjects(*((_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:ciscoFabricC12kOc192XbarGroup.setStatus(_A)
ciscoFabricC12kNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,281,2,2,12))
ciscoFabricC12kNotifEnableGroup.setObjects((_B,_AP))
if mibBuilder.loadTexts:ciscoFabricC12kNotifEnableGroup.setStatus(_A)
ciscoFabricC12kMIBFabMasterSchCh=NotificationType((1,3,6,1,4,1,9,9,281,0,1))
ciscoFabricC12kMIBFabMasterSchCh.setObjects(*((_B,_H),(_D,_I)))
if mibBuilder.loadTexts:ciscoFabricC12kMIBFabMasterSchCh.setStatus(_A)
ciscoFabricC12kNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,281,2,2,13))
ciscoFabricC12kNotifGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:ciscoFabricC12kNotifGroup.setStatus(_A)
ciscoFabricC12kMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,281,2,1,1))
ciscoFabricC12kMIBCompliance.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:ciscoFabricC12kMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CfcFabricConfigMode':CfcFabricConfigMode,'CfcFabricFiaState':CfcFabricFiaState,'CfcScaInterrupts':CfcScaInterrupts,'CfcSlotMask':CfcSlotMask,'ciscoFabricC12kMIB':ciscoFabricC12kMIB,'ciscoFabricC12kMIBNotifs':ciscoFabricC12kMIBNotifs,_AQ:ciscoFabricC12kMIBFabMasterSchCh,'ciscoFabricC12kMIBObjects':ciscoFabricC12kMIBObjects,'cfcGeneric':cfcGeneric,'cfcGenericGlobal':cfcGenericGlobal,_O:cfcGenericGlobalFabConfigMode,_H:cfcGenericGlobalFabMasterSched,'cfcGenericFab':cfcGenericFab,'cfcGenericFabToFabTable':cfcGenericFabToFabTable,'cfcGenericFabToFabEntry':cfcGenericFabToFabEntry,_P:cfcGenericFabToFabState,_Q:cfcGenericFabToFabGrantPEs,_R:cfcGenericFabToFabRequestPEs,_S:cfcGenericFabToFabCellFifoPEs,'cfcGenericFabFrFabTable':cfcGenericFabFrFabTable,'cfcGenericFabFrFabEntry':cfcGenericFabFrFabEntry,_T:cfcGenericFabFrFabState,'cfcGenericFabFrFabSliTable':cfcGenericFabFrFabSliTable,'cfcGenericFabFrFabSliEntry':cfcGenericFabFrFabSliEntry,_L:cfcGenericFabFrFabSliFabIndex,_U:cfcGenericFabFrFabSliLOSErrors,_V:cfcGenericFabFrFabSliCRCErrors,_W:cfcGenericFabFrFabSliLOSState,'cfcGenericSca':cfcGenericSca,'cfcGenericScaTable':cfcGenericScaTable,'cfcGenericScaEntry':cfcGenericScaEntry,_X:cfcGenericScaIdentifier,_Y:cfcGenericScaIntrStatus,_Z:cfcGenericScaIntrsEnabled,_a:cfcGenericScaConfig,_b:cfcGenericScaPELog,_c:cfcGenericScaFifoOverflowLog,_d:cfcGenericScaLCsEnabled,_e:cfcGenericScaForcedBackPressure,_AK:cfcGenericScaOc192LCsPresent,_f:cfcGenericScaPreOc192LCsPresent,'cfcGenericXbar':cfcGenericXbar,'cfcGenericXbarTable':cfcGenericXbarTable,'cfcGenericXbarEntry':cfcGenericXbarEntry,_g:cfcGenericXbarIdentifier,'cfcPreOc192':cfcPreOc192,'cfcPreOc192Fab':cfcPreOc192Fab,'cfcPreOc192FabToFabTable':cfcPreOc192FabToFabTable,'cfcPreOc192FabToFabEntry':cfcPreOc192FabToFabEntry,_h:cfcPreOc192FabToFabScaLosts,_i:cfcPreOc192FabToFabUCFifoOvFlws,_j:cfcPreOc192FabToFabUCFifoUnFlws,_k:cfcPreOc192FabToFabMCFifoErrs,_l:cfcPreOc192FabToFabBmaPEs,_m:cfcPreOc192FabToFabBmaHskErrs,_n:cfcPreOc192FabToFabUniDestMCRqs,_o:cfcPreOc192FabToFabMultiDstUCRqs,_p:cfcPreOc192FabToFabEmptyDestRqs,'cfcPreOc192FabFrFabTable':cfcPreOc192FabFrFabTable,'cfcPreOc192FabFrFabEntry':cfcPreOc192FabFrFabEntry,_q:cfcPreOc192FabFrFabCellFifoPEs,_r:cfcPreOc192FabFrFabRedFifoPEs,_s:cfcPreOc192FabFrFabRedFifoOvflws,_t:cfcPreOc192FabFrFabCellDrops,'cfcPreOc192Sca':cfcPreOc192Sca,'cfcPreOc192ScaTable':cfcPreOc192ScaTable,'cfcPreOc192ScaEntry':cfcPreOc192ScaEntry,_u:cfcPreOc192ScaReSyncDelay,_v:cfcPreOc192ScaLOSLog,'cfcPreOc192Xbar':cfcPreOc192Xbar,'cfcPreOc192XbarTable':cfcPreOc192XbarTable,'cfcPreOc192XbarEntry':cfcPreOc192XbarEntry,_w:cfcPreOc192XbarIntrStatus,_x:cfcPreOc192XbarParityChkStatus,'cfcOc192':cfcOc192,'cfcOc192Fab':cfcOc192Fab,'cfcOc192FabToFabTable':cfcOc192FabToFabTable,'cfcOc192FabToFabEntry':cfcOc192FabToFabEntry,_y:cfcOc192FabToFabMccDataPEs,_z:cfcOc192FabToFabMccCmdPEs,_A0:cfcOc192FabToFabBackPressurePEs,_A1:cfcOc192FabToFabCellFifoOvFlws,_A2:cfcOc192FabToFabCellFifoUnFlws,_A3:cfcOc192FabToFabMccCmdSeqEndErrs,_A4:cfcOc192FabToFabMccCmdSeqStrErrs,'cfcOc192FabFrFabTable':cfcOc192FabFrFabTable,'cfcOc192FabFrFabEntry':cfcOc192FabFrFabEntry,_A5:cfcOc192FabFrFabPktLenErrs,_A6:cfcOc192FabFrFabExtRamPEs,_A7:cfcOc192FabFrFabPktLenPEs,_A8:cfcOc192FabFrFabHdrSramPEs,_A9:cfcOc192FabFrFabTxCtrlPEs,_AA:cfcOc192FabFrFabHdrFifoOvFlws,_AB:cfcOc192FabFrFabExtSramOvFlws,_AC:cfcOc192FabFrFabFirstLastErrs,_AD:cfcOc192FabFrFabSeqErrs,'cfcOc192FabFrFabSliTable':cfcOc192FabFrFabSliTable,'cfcOc192FabFrFabSliEntry':cfcOc192FabFrFabSliEntry,_M:cfcOc192FabFrFabSliSwitchIndex,_AE:cfcOc192FabFrFabSliXorErrs,_AF:cfcOc192FabFrFabSliCellDrops,'cfcOc192FabFrFabStatTable':cfcOc192FabFrFabStatTable,'cfcOc192FabFrFabStatEntry':cfcOc192FabFrFabStatEntry,_N:cfcOc192FabFrFabStatLCIndex,_AG:cfcOc192FabFrFabStatUCHiPktDrops,_AH:cfcOc192FabFrFabStatUCLoPktDrops,_AI:cfcOc192FabFrFabStatMCHiPktDrops,_AJ:cfcOc192FabFrFabStatMCLoPktDrops,'cfcOc192Sca':cfcOc192Sca,'cfcOc192ScaTable':cfcOc192ScaTable,'cfcOc192ScaEntry':cfcOc192ScaEntry,_AL:cfcOc192ScaRotationPeriod,_AM:cfcOc192ScaDisableGrants,'cfcOc192Xbar':cfcOc192Xbar,'cfcOc192XbarTable':cfcOc192XbarTable,'cfcOc192XbarEntry':cfcOc192XbarEntry,_AN:cfcOc192XbarCtrlLOSStatus,_AO:cfcOc192XbarCtrlCRCErr,'cfcNotif':cfcNotif,_AP:cfcNotifEnable,'ciscoFabricC12kMIBConform':ciscoFabricC12kMIBConform,'ciscoFabricC12kMIBCompliances':ciscoFabricC12kMIBCompliances,'ciscoFabricC12kMIBCompliance':ciscoFabricC12kMIBCompliance,'ciscoFabricC12kMIBGroups':ciscoFabricC12kMIBGroups,_AR:ciscoFabricC12kGlobalGroup,_AS:ciscoFabricC12kFiaGroup,_AT:ciscoFabricC12kScaGroup,_AU:ciscoFabricC12kXbarGroup,_AV:ciscoFabricC12kPreOc192FiaGroup,_AY:ciscoFabricC12kPreOc192ScaGroup,_AZ:ciscoFabricC12kPreOc192XbarGroup,_Aa:ciscoFabricC12kOc192FiaGroup,_Ab:ciscoFabricC12kOc192LCGroup,_Ac:ciscoFabricC12kOc192ScaGroup,_Ad:ciscoFabricC12kOc192XbarGroup,_AW:ciscoFabricC12kNotifEnableGroup,_AX:ciscoFabricC12kNotifGroup})