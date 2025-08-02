_i='mepGroup'
_h='mepCSFDEI'
_g='mepCSFPriority'
_f='mepCSFInterval'
_e='mepCSFSupport'
_d='mepPmHistStatsEnable'
_c='mepAisDEI'
_b='mepAisPriority'
_a='mepAISInterval'
_Z='mepClientMDLevel'
_Y='mepAISCapability'
_X='mepSomeMACStatusDefectCFMaction'
_W='mepErrorCCMDefectCFMAction'
_V='mepXconnDefectCFMAction'
_U='mepSomeRMEPDefectCFMAction'
_T='mepInterfaceStatusTLV'
_S='mepPortStatusTLV'
_R='mepLowestPriorityDefect'
_Q='mepMacAddress'
_P='mepCcmDEI'
_O='mepCcmPriority'
_N='mepDirection'
_M='mepRMEPCrossCheck'
_L='mepInnerPrimaryVID'
_K='mepOuterPrimaryVID'
_J='mepMDLevel'
_I='mepCCIEnabled'
_H='mepRole'
_G='mepMaaId'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-PXMMEP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnAISInterval,InfnCFMAction,InfnCSFInterval,InfnEnableDisable,InfnEnableDisableType,InfnEqptType,InfnInterfaceStatusTLV,InfnIsEnabled,InfnLowestPriDef,InfnMepDirection,InfnMepRole,InfnPortStatusTLV=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnAISInterval','InfnCFMAction','InfnCSFInterval','InfnEnableDisable','InfnEnableDisableType','InfnEqptType','InfnInterfaceStatusTLV','InfnIsEnabled','InfnLowestPriDef','InfnMepDirection','InfnMepRole','InfnPortStatusTLV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mepMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,43))
_MepTable_Object=MibTable
mepTable=_MepTable_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1))
if mibBuilder.loadTexts:mepTable.setStatus(_A)
_MepEntry_Object=MibTableRow
mepEntry=_MepEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1))
mepEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mepEntry.setStatus(_A)
_MepMaaId_Type=DisplayString
_MepMaaId_Object=MibTableColumn
mepMaaId=_MepMaaId_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,1),_MepMaaId_Type())
mepMaaId.setMaxAccess(_D)
if mibBuilder.loadTexts:mepMaaId.setStatus(_A)
_MepRole_Type=InfnMepRole
_MepRole_Object=MibTableColumn
mepRole=_MepRole_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,2),_MepRole_Type())
mepRole.setMaxAccess(_D)
if mibBuilder.loadTexts:mepRole.setStatus(_A)
_MepCCIEnabled_Type=InfnIsEnabled
_MepCCIEnabled_Object=MibTableColumn
mepCCIEnabled=_MepCCIEnabled_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,3),_MepCCIEnabled_Type())
mepCCIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCCIEnabled.setStatus(_A)
_MepMDLevel_Type=Integer32
_MepMDLevel_Object=MibTableColumn
mepMDLevel=_MepMDLevel_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,4),_MepMDLevel_Type())
mepMDLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:mepMDLevel.setStatus(_A)
_MepOuterPrimaryVID_Type=Integer32
_MepOuterPrimaryVID_Object=MibTableColumn
mepOuterPrimaryVID=_MepOuterPrimaryVID_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,5),_MepOuterPrimaryVID_Type())
mepOuterPrimaryVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mepOuterPrimaryVID.setStatus(_A)
_MepInnerPrimaryVID_Type=Integer32
_MepInnerPrimaryVID_Object=MibTableColumn
mepInnerPrimaryVID=_MepInnerPrimaryVID_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,6),_MepInnerPrimaryVID_Type())
mepInnerPrimaryVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mepInnerPrimaryVID.setStatus(_A)
_MepId_Type=Integer32
_MepId_Object=MibTableColumn
mepId=_MepId_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,7),_MepId_Type())
mepId.setMaxAccess(_C)
if mibBuilder.loadTexts:mepId.setStatus(_A)
_MepRMEPCrossCheck_Type=InfnEnableDisable
_MepRMEPCrossCheck_Object=MibTableColumn
mepRMEPCrossCheck=_MepRMEPCrossCheck_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,8),_MepRMEPCrossCheck_Type())
mepRMEPCrossCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:mepRMEPCrossCheck.setStatus(_A)
_MepDirection_Type=InfnMepDirection
_MepDirection_Object=MibTableColumn
mepDirection=_MepDirection_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,9),_MepDirection_Type())
mepDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:mepDirection.setStatus(_A)
_MepCcmPriority_Type=Integer32
_MepCcmPriority_Object=MibTableColumn
mepCcmPriority=_MepCcmPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,10),_MepCcmPriority_Type())
mepCcmPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCcmPriority.setStatus(_A)
_MepCcmDEI_Type=InfnIsEnabled
_MepCcmDEI_Object=MibTableColumn
mepCcmDEI=_MepCcmDEI_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,11),_MepCcmDEI_Type())
mepCcmDEI.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCcmDEI.setStatus(_A)
_MepMacAddress_Type=DisplayString
_MepMacAddress_Object=MibTableColumn
mepMacAddress=_MepMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,12),_MepMacAddress_Type())
mepMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mepMacAddress.setStatus(_A)
_MepLowestPriorityDefect_Type=InfnLowestPriDef
_MepLowestPriorityDefect_Object=MibTableColumn
mepLowestPriorityDefect=_MepLowestPriorityDefect_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,13),_MepLowestPriorityDefect_Type())
mepLowestPriorityDefect.setMaxAccess(_C)
if mibBuilder.loadTexts:mepLowestPriorityDefect.setStatus(_A)
_MepPortStatusTLV_Type=InfnPortStatusTLV
_MepPortStatusTLV_Object=MibTableColumn
mepPortStatusTLV=_MepPortStatusTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,14),_MepPortStatusTLV_Type())
mepPortStatusTLV.setMaxAccess(_D)
if mibBuilder.loadTexts:mepPortStatusTLV.setStatus(_A)
_MepInterfaceStatusTLV_Type=InfnInterfaceStatusTLV
_MepInterfaceStatusTLV_Object=MibTableColumn
mepInterfaceStatusTLV=_MepInterfaceStatusTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,15),_MepInterfaceStatusTLV_Type())
mepInterfaceStatusTLV.setMaxAccess(_D)
if mibBuilder.loadTexts:mepInterfaceStatusTLV.setStatus(_A)
_MepSomeRMEPDefectCFMAction_Type=InfnCFMAction
_MepSomeRMEPDefectCFMAction_Object=MibTableColumn
mepSomeRMEPDefectCFMAction=_MepSomeRMEPDefectCFMAction_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,16),_MepSomeRMEPDefectCFMAction_Type())
mepSomeRMEPDefectCFMAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mepSomeRMEPDefectCFMAction.setStatus(_A)
_MepXconnDefectCFMAction_Type=InfnCFMAction
_MepXconnDefectCFMAction_Object=MibTableColumn
mepXconnDefectCFMAction=_MepXconnDefectCFMAction_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,17),_MepXconnDefectCFMAction_Type())
mepXconnDefectCFMAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mepXconnDefectCFMAction.setStatus(_A)
_MepErrorCCMDefectCFMAction_Type=InfnCFMAction
_MepErrorCCMDefectCFMAction_Object=MibTableColumn
mepErrorCCMDefectCFMAction=_MepErrorCCMDefectCFMAction_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,18),_MepErrorCCMDefectCFMAction_Type())
mepErrorCCMDefectCFMAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mepErrorCCMDefectCFMAction.setStatus(_A)
_MepSomeMACStatusDefectCFMaction_Type=InfnCFMAction
_MepSomeMACStatusDefectCFMaction_Object=MibTableColumn
mepSomeMACStatusDefectCFMaction=_MepSomeMACStatusDefectCFMaction_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,19),_MepSomeMACStatusDefectCFMaction_Type())
mepSomeMACStatusDefectCFMaction.setMaxAccess(_C)
if mibBuilder.loadTexts:mepSomeMACStatusDefectCFMaction.setStatus(_A)
_MepAISCapability_Type=InfnIsEnabled
_MepAISCapability_Object=MibTableColumn
mepAISCapability=_MepAISCapability_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,20),_MepAISCapability_Type())
mepAISCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:mepAISCapability.setStatus(_A)
_MepClientMDLevel_Type=Integer32
_MepClientMDLevel_Object=MibTableColumn
mepClientMDLevel=_MepClientMDLevel_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,21),_MepClientMDLevel_Type())
mepClientMDLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mepClientMDLevel.setStatus(_A)
_MepAISInterval_Type=InfnAISInterval
_MepAISInterval_Object=MibTableColumn
mepAISInterval=_MepAISInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,22),_MepAISInterval_Type())
mepAISInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mepAISInterval.setStatus(_A)
_MepAisPriority_Type=Integer32
_MepAisPriority_Object=MibTableColumn
mepAisPriority=_MepAisPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,23),_MepAisPriority_Type())
mepAisPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mepAisPriority.setStatus(_A)
_MepAisDEI_Type=InfnIsEnabled
_MepAisDEI_Object=MibTableColumn
mepAisDEI=_MepAisDEI_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,24),_MepAisDEI_Type())
mepAisDEI.setMaxAccess(_C)
if mibBuilder.loadTexts:mepAisDEI.setStatus(_A)
_MepPmHistStatsEnable_Type=InfnEnableDisable
_MepPmHistStatsEnable_Object=MibTableColumn
mepPmHistStatsEnable=_MepPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,25),_MepPmHistStatsEnable_Type())
mepPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mepPmHistStatsEnable.setStatus(_A)
_MepCSFSupport_Type=InfnEnableDisableType
_MepCSFSupport_Object=MibTableColumn
mepCSFSupport=_MepCSFSupport_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,26),_MepCSFSupport_Type())
mepCSFSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCSFSupport.setStatus(_A)
_MepCSFInterval_Type=InfnCSFInterval
_MepCSFInterval_Object=MibTableColumn
mepCSFInterval=_MepCSFInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,27),_MepCSFInterval_Type())
mepCSFInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCSFInterval.setStatus(_A)
_MepCSFPriority_Type=Integer32
_MepCSFPriority_Object=MibTableColumn
mepCSFPriority=_MepCSFPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,28),_MepCSFPriority_Type())
mepCSFPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCSFPriority.setStatus(_A)
_MepCSFDEI_Type=InfnIsEnabled
_MepCSFDEI_Object=MibTableColumn
mepCSFDEI=_MepCSFDEI_Object((1,3,6,1,4,1,21296,2,2,2,2,43,1,1,29),_MepCSFDEI_Type())
mepCSFDEI.setMaxAccess(_C)
if mibBuilder.loadTexts:mepCSFDEI.setStatus(_A)
_MepConformance_ObjectIdentity=ObjectIdentity
mepConformance=_MepConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,43,3))
_MepCompliances_ObjectIdentity=ObjectIdentity
mepCompliances=_MepCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,43,3,1))
_MepGroups_ObjectIdentity=ObjectIdentity
mepGroups=_MepGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,43,3,2))
mepGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,43,3,2,1))
mepGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,'mepId'),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:mepGroup.setStatus(_A)
mepCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,43,3,1,1))
mepCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:mepCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mepMIB':mepMIB,'mepTable':mepTable,'mepEntry':mepEntry,_G:mepMaaId,_H:mepRole,_I:mepCCIEnabled,_J:mepMDLevel,_K:mepOuterPrimaryVID,_L:mepInnerPrimaryVID,'mepId':mepId,_M:mepRMEPCrossCheck,_N:mepDirection,_O:mepCcmPriority,_P:mepCcmDEI,_Q:mepMacAddress,_R:mepLowestPriorityDefect,_S:mepPortStatusTLV,_T:mepInterfaceStatusTLV,_U:mepSomeRMEPDefectCFMAction,_V:mepXconnDefectCFMAction,_W:mepErrorCCMDefectCFMAction,_X:mepSomeMACStatusDefectCFMaction,_Y:mepAISCapability,_Z:mepClientMDLevel,_a:mepAISInterval,_b:mepAisPriority,_c:mepAisDEI,_d:mepPmHistStatsEnable,_e:mepCSFSupport,_f:mepCSFInterval,_g:mepCSFPriority,_h:mepCSFDEI,'mepConformance':mepConformance,'mepCompliances':mepCompliances,'mepCompliance':mepCompliance,'mepGroups':mepGroups,_i:mepGroup})