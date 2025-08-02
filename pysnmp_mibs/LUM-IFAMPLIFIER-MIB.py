_At='ifAmplifierAmplifierGroupV4'
_As='ifAmplifierAmplifierGroupV3'
_Ar='ifAmplifierEdfaGroupV2'
_Aq='ifAmplifierAmplifierGroupV2'
_Ap='ifAmplifierEdfaGroupV1'
_Ao='ifAmplifierAmplifierGroupV1'
_An='ifAmplifierAmplifierDescr'
_Am='ifAmplifierEdfaActualGain'
_Al='ifAmplifierRamanActualGain'
_Ak='ifAmplifierEdfaSaturation'
_Aj='ifAmplifierModuleSlot'
_Ai='ifAmplifierModuleSubrack'
_Ah='ifAmplifierModuleColdRestart'
_Ag='ifAmplifierModuleCommunicationFailure'
_Af='ifAmplifierModuleHighPumpTemperature'
_Ae='ifAmplifierModuleHighPumpCurrent'
_Ad='ifAmplifierModuleHighModuleTemperature'
_Ac='ifAmplifierModuleInfo'
_Ab='ifAmplifierModuleTemperature'
_Aa='ifAmplifierModuleUId'
_AZ='ifAmplifierModuleName'
_AY='ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime'
_AX='ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime'
_AW='ifAmplifierGeneralIfAmplifierEdfaTableSize'
_AV='ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime'
_AU='ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime'
_AT='ifAmplifierGeneralIfAmplifierRamanTableSize'
_AS='ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime'
_AR='ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime'
_AQ='ifAmplifierGeneralIfAmplifierModuleTableSize'
_AP='ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime'
_AO='ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime'
_AN='ifAmplifierGeneralIfAmplifierAmplifierTableSize'
_AM='ifAmplifierGeneralStateLastChangeTime'
_AL='ifAmplifierGeneralConfigLastChangeTime'
_AK='DisplayString'
_AJ='OperStatusWithNA'
_AI='AdminStatusWithNA'
_AH='ifAmplifierEdfaGroupV3'
_AG='ifAmplifierRamanGroupV2'
_AF='ifAmplifierRamanGroupV1'
_AE='ifAmplifierAmplifierFunctionalType'
_AD='ifAmplifierEdfaPumpCurrent'
_AC='ifAmplifierEdfaPumpPower'
_AB='ifAmplifierRamanSlot'
_AA='ifAmplifierRamanSubrack'
_A9='ifAmplifierRamanRelatedAmplifierIndex'
_A8='ifAmplifierRamanHighPointInsertionLoss'
_A7='ifAmplifierRamanPointInsertionLossThld'
_A6='ifAmplifierRamanPointInsertionLoss'
_A5='ifAmplifierRamanHighBackReflectionThld'
_A4='ifAmplifierRamanHighBackReflection'
_A3='ifAmplifierRamanBackReflectionPowerRatio'
_A2='ifAmplifierRamanBackReflectionPower'
_A1='ifAmplifierRamanTotalPumpPower'
_A0='ifAmplifierRamanPump2Status'
_z='ifAmplifierRamanPump2Power'
_y='ifAmplifierRamanPump1Status'
_x='ifAmplifierRamanPump1Power'
_w='ifAmplifierRamanReceivedPowerLevel'
_v='ifAmplifierRamanWantedGainTilt'
_u='ifAmplifierRamanLineFiberType'
_t='ifAmplifierRamanUId'
_s='ifAmplifierRamanName'
_r='notAvailable'
_q='off'
_p='notApplicable'
_o='ifAmplifierModuleIndex'
_n='ifAmplifierAmplifierSaturation'
_m='ifAmplifierAmplifierOutputPowerFail'
_l='ifAmplifierEdfaSlot'
_k='ifAmplifierEdfaSubrack'
_j='ifAmplifierEdfaRelatedAmplifierIndex'
_i='ifAmplifierEdfaMonitorPortLoss'
_h='ifAmplifierEdfaHighBackReflectionThld'
_g='ifAmplifierEdfaHighBackReflection'
_f='ifAmplifierEdfaBackReflectionPowerRatio'
_e='ifAmplifierEdfaBackReflectionPower'
_d='ifAmplifierEdfaPumpStatus'
_c='ifAmplifierEdfaTxPowerLimit'
_b='ifAmplifierEdfaWantedGainTilt'
_a='ifAmplifierEdfaUId'
_Z='ifAmplifierEdfaName'
_Y='ifAmplifierRamanIndex'
_X='ifAmplifierModuleGroupV1'
_W='ifAmplifierGeneralGroupV1'
_V='ifAmplifierAmplifierSlot'
_U='ifAmplifierAmplifierSubrack'
_T='ifAmplifierAmplifierRxIfIndex'
_S='ifAmplifierAmplifierTxIfIndex'
_R='ifAmplifierAmplifierMidStageLoss'
_Q='ifAmplifierAmplifierOperStatus'
_P='ifAmplifierAmplifierAdminStatus'
_O='ifAmplifierAmplifierActualGain'
_N='ifAmplifierAmplifierWantedGain'
_M='ifAmplifierAmplifierTxPower'
_L='ifAmplifierAmplifierRxPower'
_K='ifAmplifierAmplifierUId'
_J='ifAmplifierAmplifierName'
_I='ifAmplifierEdfaIndex'
_H='ifAmplifierAmplifierIndex'
_G='Signed32WithNA'
_F='Integer32'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='LUM-IFAMPLIFIER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfAmplifierMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfAmplifierMIB','lumModules')
AdminStatusWithNA,FaultStatusWithNA,Integer32WithNA,MgmtNameString,OperStatusWithNA,Signed32WithNA=mibBuilder.importSymbols('LUM-TC',_AI,'FaultStatusWithNA','Integer32WithNA','MgmtNameString',_AJ,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_AK,'PhysAddress','TextualConvention')
lumIfAmplifierMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,65))
if mibBuilder.loadTexts:lumIfAmplifierMIBModule.setRevisions(('2018-09-28 00:00','2017-12-15 00:00','2017-06-15 00:00','2016-05-30 00:00','2015-11-30 00:00'))
_LumIfAmplifierConfs_ObjectIdentity=ObjectIdentity
lumIfAmplifierConfs=_LumIfAmplifierConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,65,1))
_LumIfAmplifierGroups_ObjectIdentity=ObjectIdentity
lumIfAmplifierGroups=_LumIfAmplifierGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,65,1,1))
_LumIfAmplifierCompl_ObjectIdentity=ObjectIdentity
lumIfAmplifierCompl=_LumIfAmplifierCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,65,1,2))
_LumIfAmplifierMIBObjects_ObjectIdentity=ObjectIdentity
lumIfAmplifierMIBObjects=_LumIfAmplifierMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2))
_IfAmplifierGeneral_ObjectIdentity=ObjectIdentity
ifAmplifierGeneral=_IfAmplifierGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2,1))
_IfAmplifierGeneralConfigLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralConfigLastChangeTime_Object=MibScalar
ifAmplifierGeneralConfigLastChangeTime=_IfAmplifierGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,1),_IfAmplifierGeneralConfigLastChangeTime_Type())
ifAmplifierGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralConfigLastChangeTime.setStatus(_B)
_IfAmplifierGeneralStateLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralStateLastChangeTime_Object=MibScalar
ifAmplifierGeneralStateLastChangeTime=_IfAmplifierGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,2),_IfAmplifierGeneralStateLastChangeTime_Type())
ifAmplifierGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralStateLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Type=Unsigned32
_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Object=MibScalar
ifAmplifierGeneralIfAmplifierAmplifierTableSize=_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Object((1,3,6,1,4,1,8708,2,65,2,1,3),_IfAmplifierGeneralIfAmplifierAmplifierTableSize_Type())
ifAmplifierGeneralIfAmplifierAmplifierTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierAmplifierTableSize.setStatus(_B)
_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime=_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,4),_IfAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime=_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,5),_IfAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierModuleTableSize_Type=Unsigned32
_IfAmplifierGeneralIfAmplifierModuleTableSize_Object=MibScalar
ifAmplifierGeneralIfAmplifierModuleTableSize=_IfAmplifierGeneralIfAmplifierModuleTableSize_Object((1,3,6,1,4,1,8708,2,65,2,1,6),_IfAmplifierGeneralIfAmplifierModuleTableSize_Type())
ifAmplifierGeneralIfAmplifierModuleTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierModuleTableSize.setStatus(_B)
_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime=_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,7),_IfAmplifierGeneralIfAmplifierModuleConfigLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime=_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,8),_IfAmplifierGeneralIfAmplifierModuleStateLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierRamanTableSize_Type=Unsigned32
_IfAmplifierGeneralIfAmplifierRamanTableSize_Object=MibScalar
ifAmplifierGeneralIfAmplifierRamanTableSize=_IfAmplifierGeneralIfAmplifierRamanTableSize_Object((1,3,6,1,4,1,8708,2,65,2,1,9),_IfAmplifierGeneralIfAmplifierRamanTableSize_Type())
ifAmplifierGeneralIfAmplifierRamanTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierRamanTableSize.setStatus(_B)
_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime=_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,10),_IfAmplifierGeneralIfAmplifierRamanConfigLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime=_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,11),_IfAmplifierGeneralIfAmplifierRamanStateLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierEdfaTableSize_Type=Unsigned32
_IfAmplifierGeneralIfAmplifierEdfaTableSize_Object=MibScalar
ifAmplifierGeneralIfAmplifierEdfaTableSize=_IfAmplifierGeneralIfAmplifierEdfaTableSize_Object((1,3,6,1,4,1,8708,2,65,2,1,12),_IfAmplifierGeneralIfAmplifierEdfaTableSize_Type())
ifAmplifierGeneralIfAmplifierEdfaTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierEdfaTableSize.setStatus(_B)
_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime=_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,13),_IfAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime.setStatus(_B)
_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Type=DateAndTime
_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Object=MibScalar
ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime=_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,65,2,1,14),_IfAmplifierGeneralIfAmplifierEdfaStateLastChangeTime_Type())
ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime.setStatus(_B)
_IfAmplifierAmplifierList_ObjectIdentity=ObjectIdentity
ifAmplifierAmplifierList=_IfAmplifierAmplifierList_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2,2))
_IfAmplifierAmplifierTable_Object=MibTable
ifAmplifierAmplifierTable=_IfAmplifierAmplifierTable_Object((1,3,6,1,4,1,8708,2,65,2,2,1))
if mibBuilder.loadTexts:ifAmplifierAmplifierTable.setStatus(_B)
_IfAmplifierAmplifierEntry_Object=MibTableRow
ifAmplifierAmplifierEntry=_IfAmplifierAmplifierEntry_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1))
ifAmplifierAmplifierEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:ifAmplifierAmplifierEntry.setStatus(_B)
_IfAmplifierAmplifierIndex_Type=Unsigned32
_IfAmplifierAmplifierIndex_Object=MibTableColumn
ifAmplifierAmplifierIndex=_IfAmplifierAmplifierIndex_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,1),_IfAmplifierAmplifierIndex_Type())
ifAmplifierAmplifierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierIndex.setStatus(_B)
_IfAmplifierAmplifierName_Type=MgmtNameString
_IfAmplifierAmplifierName_Object=MibTableColumn
ifAmplifierAmplifierName=_IfAmplifierAmplifierName_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,2),_IfAmplifierAmplifierName_Type())
ifAmplifierAmplifierName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierName.setStatus(_B)
_IfAmplifierAmplifierUId_Type=Unsigned32
_IfAmplifierAmplifierUId_Object=MibTableColumn
ifAmplifierAmplifierUId=_IfAmplifierAmplifierUId_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,3),_IfAmplifierAmplifierUId_Type())
ifAmplifierAmplifierUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierUId.setStatus(_B)
_IfAmplifierAmplifierRxPower_Type=Signed32WithNA
_IfAmplifierAmplifierRxPower_Object=MibTableColumn
ifAmplifierAmplifierRxPower=_IfAmplifierAmplifierRxPower_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,4),_IfAmplifierAmplifierRxPower_Type())
ifAmplifierAmplifierRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierRxPower.setStatus(_B)
_IfAmplifierAmplifierTxPower_Type=Signed32WithNA
_IfAmplifierAmplifierTxPower_Object=MibTableColumn
ifAmplifierAmplifierTxPower=_IfAmplifierAmplifierTxPower_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,5),_IfAmplifierAmplifierTxPower_Type())
ifAmplifierAmplifierTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierTxPower.setStatus(_B)
_IfAmplifierAmplifierWantedGain_Type=Signed32WithNA
_IfAmplifierAmplifierWantedGain_Object=MibTableColumn
ifAmplifierAmplifierWantedGain=_IfAmplifierAmplifierWantedGain_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,6),_IfAmplifierAmplifierWantedGain_Type())
ifAmplifierAmplifierWantedGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierAmplifierWantedGain.setStatus(_B)
_IfAmplifierAmplifierActualGain_Type=Signed32WithNA
_IfAmplifierAmplifierActualGain_Object=MibTableColumn
ifAmplifierAmplifierActualGain=_IfAmplifierAmplifierActualGain_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,7),_IfAmplifierAmplifierActualGain_Type())
ifAmplifierAmplifierActualGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierActualGain.setStatus(_B)
class _IfAmplifierAmplifierAdminStatus_Type(AdminStatusWithNA):defaultValue=1
_IfAmplifierAmplifierAdminStatus_Type.__name__=_AI
_IfAmplifierAmplifierAdminStatus_Object=MibTableColumn
ifAmplifierAmplifierAdminStatus=_IfAmplifierAmplifierAdminStatus_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,8),_IfAmplifierAmplifierAdminStatus_Type())
ifAmplifierAmplifierAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierAmplifierAdminStatus.setStatus(_B)
class _IfAmplifierAmplifierOperStatus_Type(OperStatusWithNA):defaultValue=1
_IfAmplifierAmplifierOperStatus_Type.__name__=_AJ
_IfAmplifierAmplifierOperStatus_Object=MibTableColumn
ifAmplifierAmplifierOperStatus=_IfAmplifierAmplifierOperStatus_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,9),_IfAmplifierAmplifierOperStatus_Type())
ifAmplifierAmplifierOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierOperStatus.setStatus(_B)
_IfAmplifierAmplifierMidStageLoss_Type=Signed32WithNA
_IfAmplifierAmplifierMidStageLoss_Object=MibTableColumn
ifAmplifierAmplifierMidStageLoss=_IfAmplifierAmplifierMidStageLoss_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,10),_IfAmplifierAmplifierMidStageLoss_Type())
ifAmplifierAmplifierMidStageLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierMidStageLoss.setStatus(_B)
_IfAmplifierAmplifierTxIfIndex_Type=Unsigned32
_IfAmplifierAmplifierTxIfIndex_Object=MibTableColumn
ifAmplifierAmplifierTxIfIndex=_IfAmplifierAmplifierTxIfIndex_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,11),_IfAmplifierAmplifierTxIfIndex_Type())
ifAmplifierAmplifierTxIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierTxIfIndex.setStatus(_B)
_IfAmplifierAmplifierRxIfIndex_Type=Unsigned32
_IfAmplifierAmplifierRxIfIndex_Object=MibTableColumn
ifAmplifierAmplifierRxIfIndex=_IfAmplifierAmplifierRxIfIndex_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,12),_IfAmplifierAmplifierRxIfIndex_Type())
ifAmplifierAmplifierRxIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierRxIfIndex.setStatus(_B)
_IfAmplifierAmplifierSubrack_Type=Unsigned32
_IfAmplifierAmplifierSubrack_Object=MibTableColumn
ifAmplifierAmplifierSubrack=_IfAmplifierAmplifierSubrack_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,13),_IfAmplifierAmplifierSubrack_Type())
ifAmplifierAmplifierSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierSubrack.setStatus(_B)
_IfAmplifierAmplifierSlot_Type=Unsigned32
_IfAmplifierAmplifierSlot_Object=MibTableColumn
ifAmplifierAmplifierSlot=_IfAmplifierAmplifierSlot_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,14),_IfAmplifierAmplifierSlot_Type())
ifAmplifierAmplifierSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierSlot.setStatus(_B)
_IfAmplifierAmplifierOutputPowerFail_Type=FaultStatusWithNA
_IfAmplifierAmplifierOutputPowerFail_Object=MibTableColumn
ifAmplifierAmplifierOutputPowerFail=_IfAmplifierAmplifierOutputPowerFail_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,15),_IfAmplifierAmplifierOutputPowerFail_Type())
ifAmplifierAmplifierOutputPowerFail.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierOutputPowerFail.setStatus(_B)
_IfAmplifierAmplifierSaturation_Type=FaultStatusWithNA
_IfAmplifierAmplifierSaturation_Object=MibTableColumn
ifAmplifierAmplifierSaturation=_IfAmplifierAmplifierSaturation_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,16),_IfAmplifierAmplifierSaturation_Type())
ifAmplifierAmplifierSaturation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierAmplifierSaturation.setStatus(_B)
class _IfAmplifierAmplifierFunctionalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('undefined',1),('preAmp',2),('offLinePreAmp',3),('lineAmp',4),('booster',5)))
_IfAmplifierAmplifierFunctionalType_Type.__name__=_F
_IfAmplifierAmplifierFunctionalType_Object=MibTableColumn
ifAmplifierAmplifierFunctionalType=_IfAmplifierAmplifierFunctionalType_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,17),_IfAmplifierAmplifierFunctionalType_Type())
ifAmplifierAmplifierFunctionalType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierAmplifierFunctionalType.setStatus(_B)
class _IfAmplifierAmplifierDescr_Type(DisplayString):defaultValue=OctetString('')
_IfAmplifierAmplifierDescr_Type.__name__=_AK
_IfAmplifierAmplifierDescr_Object=MibTableColumn
ifAmplifierAmplifierDescr=_IfAmplifierAmplifierDescr_Object((1,3,6,1,4,1,8708,2,65,2,2,1,1,18),_IfAmplifierAmplifierDescr_Type())
ifAmplifierAmplifierDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierAmplifierDescr.setStatus(_B)
_IfAmplifierModuleList_ObjectIdentity=ObjectIdentity
ifAmplifierModuleList=_IfAmplifierModuleList_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2,3))
_IfAmplifierModuleTable_Object=MibTable
ifAmplifierModuleTable=_IfAmplifierModuleTable_Object((1,3,6,1,4,1,8708,2,65,2,3,1))
if mibBuilder.loadTexts:ifAmplifierModuleTable.setStatus(_B)
_IfAmplifierModuleEntry_Object=MibTableRow
ifAmplifierModuleEntry=_IfAmplifierModuleEntry_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1))
ifAmplifierModuleEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:ifAmplifierModuleEntry.setStatus(_B)
_IfAmplifierModuleIndex_Type=Unsigned32
_IfAmplifierModuleIndex_Object=MibTableColumn
ifAmplifierModuleIndex=_IfAmplifierModuleIndex_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,1),_IfAmplifierModuleIndex_Type())
ifAmplifierModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleIndex.setStatus(_B)
_IfAmplifierModuleName_Type=MgmtNameString
_IfAmplifierModuleName_Object=MibTableColumn
ifAmplifierModuleName=_IfAmplifierModuleName_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,2),_IfAmplifierModuleName_Type())
ifAmplifierModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleName.setStatus(_B)
_IfAmplifierModuleUId_Type=Unsigned32
_IfAmplifierModuleUId_Object=MibTableColumn
ifAmplifierModuleUId=_IfAmplifierModuleUId_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,3),_IfAmplifierModuleUId_Type())
ifAmplifierModuleUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleUId.setStatus(_B)
_IfAmplifierModuleTemperature_Type=Integer32WithNA
_IfAmplifierModuleTemperature_Object=MibTableColumn
ifAmplifierModuleTemperature=_IfAmplifierModuleTemperature_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,4),_IfAmplifierModuleTemperature_Type())
ifAmplifierModuleTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleTemperature.setStatus(_B)
_IfAmplifierModuleInfo_Type=DisplayString
_IfAmplifierModuleInfo_Object=MibTableColumn
ifAmplifierModuleInfo=_IfAmplifierModuleInfo_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,5),_IfAmplifierModuleInfo_Type())
ifAmplifierModuleInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleInfo.setStatus(_B)
_IfAmplifierModuleHighModuleTemperature_Type=FaultStatusWithNA
_IfAmplifierModuleHighModuleTemperature_Object=MibTableColumn
ifAmplifierModuleHighModuleTemperature=_IfAmplifierModuleHighModuleTemperature_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,6),_IfAmplifierModuleHighModuleTemperature_Type())
ifAmplifierModuleHighModuleTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleHighModuleTemperature.setStatus(_B)
_IfAmplifierModuleHighPumpCurrent_Type=FaultStatusWithNA
_IfAmplifierModuleHighPumpCurrent_Object=MibTableColumn
ifAmplifierModuleHighPumpCurrent=_IfAmplifierModuleHighPumpCurrent_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,7),_IfAmplifierModuleHighPumpCurrent_Type())
ifAmplifierModuleHighPumpCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleHighPumpCurrent.setStatus(_B)
_IfAmplifierModuleHighPumpTemperature_Type=FaultStatusWithNA
_IfAmplifierModuleHighPumpTemperature_Object=MibTableColumn
ifAmplifierModuleHighPumpTemperature=_IfAmplifierModuleHighPumpTemperature_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,8),_IfAmplifierModuleHighPumpTemperature_Type())
ifAmplifierModuleHighPumpTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleHighPumpTemperature.setStatus(_B)
_IfAmplifierModuleCommunicationFailure_Type=FaultStatusWithNA
_IfAmplifierModuleCommunicationFailure_Object=MibTableColumn
ifAmplifierModuleCommunicationFailure=_IfAmplifierModuleCommunicationFailure_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,9),_IfAmplifierModuleCommunicationFailure_Type())
ifAmplifierModuleCommunicationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleCommunicationFailure.setStatus(_B)
class _IfAmplifierModuleColdRestart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doSoftwareColdRestart',1),('doNotSoftwareColdRestart',2)))
_IfAmplifierModuleColdRestart_Type.__name__=_F
_IfAmplifierModuleColdRestart_Object=MibTableColumn
ifAmplifierModuleColdRestart=_IfAmplifierModuleColdRestart_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,10),_IfAmplifierModuleColdRestart_Type())
ifAmplifierModuleColdRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierModuleColdRestart.setStatus(_B)
_IfAmplifierModuleSubrack_Type=Unsigned32
_IfAmplifierModuleSubrack_Object=MibTableColumn
ifAmplifierModuleSubrack=_IfAmplifierModuleSubrack_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,11),_IfAmplifierModuleSubrack_Type())
ifAmplifierModuleSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleSubrack.setStatus(_B)
_IfAmplifierModuleSlot_Type=Unsigned32
_IfAmplifierModuleSlot_Object=MibTableColumn
ifAmplifierModuleSlot=_IfAmplifierModuleSlot_Object((1,3,6,1,4,1,8708,2,65,2,3,1,1,12),_IfAmplifierModuleSlot_Type())
ifAmplifierModuleSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierModuleSlot.setStatus(_B)
_IfAmplifierRamanList_ObjectIdentity=ObjectIdentity
ifAmplifierRamanList=_IfAmplifierRamanList_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2,4))
_IfAmplifierRamanTable_Object=MibTable
ifAmplifierRamanTable=_IfAmplifierRamanTable_Object((1,3,6,1,4,1,8708,2,65,2,4,1))
if mibBuilder.loadTexts:ifAmplifierRamanTable.setStatus(_B)
_IfAmplifierRamanEntry_Object=MibTableRow
ifAmplifierRamanEntry=_IfAmplifierRamanEntry_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1))
ifAmplifierRamanEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:ifAmplifierRamanEntry.setStatus(_B)
_IfAmplifierRamanIndex_Type=Unsigned32
_IfAmplifierRamanIndex_Object=MibTableColumn
ifAmplifierRamanIndex=_IfAmplifierRamanIndex_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,1),_IfAmplifierRamanIndex_Type())
ifAmplifierRamanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanIndex.setStatus(_B)
_IfAmplifierRamanName_Type=MgmtNameString
_IfAmplifierRamanName_Object=MibTableColumn
ifAmplifierRamanName=_IfAmplifierRamanName_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,2),_IfAmplifierRamanName_Type())
ifAmplifierRamanName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanName.setStatus(_B)
_IfAmplifierRamanUId_Type=Unsigned32
_IfAmplifierRamanUId_Object=MibTableColumn
ifAmplifierRamanUId=_IfAmplifierRamanUId_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,3),_IfAmplifierRamanUId_Type())
ifAmplifierRamanUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanUId.setStatus(_B)
class _IfAmplifierRamanLineFiberType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ftG652',1),('ftG655',2),(_p,2147483647)))
_IfAmplifierRamanLineFiberType_Type.__name__=_F
_IfAmplifierRamanLineFiberType_Object=MibTableColumn
ifAmplifierRamanLineFiberType=_IfAmplifierRamanLineFiberType_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,4),_IfAmplifierRamanLineFiberType_Type())
ifAmplifierRamanLineFiberType.setMaxAccess('read-create')
if mibBuilder.loadTexts:ifAmplifierRamanLineFiberType.setStatus(_B)
class _IfAmplifierRamanWantedGainTilt_Type(Signed32WithNA):defaultValue=0;subtypeSpec=Signed32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-15,5),ValueRangeConstraint(2147483647,2147483647))
_IfAmplifierRamanWantedGainTilt_Type.__name__=_G
_IfAmplifierRamanWantedGainTilt_Object=MibTableColumn
ifAmplifierRamanWantedGainTilt=_IfAmplifierRamanWantedGainTilt_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,5),_IfAmplifierRamanWantedGainTilt_Type())
ifAmplifierRamanWantedGainTilt.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierRamanWantedGainTilt.setStatus(_B)
_IfAmplifierRamanReceivedPowerLevel_Type=Signed32WithNA
_IfAmplifierRamanReceivedPowerLevel_Object=MibTableColumn
ifAmplifierRamanReceivedPowerLevel=_IfAmplifierRamanReceivedPowerLevel_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,6),_IfAmplifierRamanReceivedPowerLevel_Type())
ifAmplifierRamanReceivedPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanReceivedPowerLevel.setStatus(_B)
_IfAmplifierRamanPump1Power_Type=Signed32WithNA
_IfAmplifierRamanPump1Power_Object=MibTableColumn
ifAmplifierRamanPump1Power=_IfAmplifierRamanPump1Power_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,7),_IfAmplifierRamanPump1Power_Type())
ifAmplifierRamanPump1Power.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanPump1Power.setStatus(_B)
class _IfAmplifierRamanPump1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2147483646,2147483647)));namedValues=NamedValues(*((_q,0),('on',1),(_r,2147483646),(_p,2147483647)))
_IfAmplifierRamanPump1Status_Type.__name__=_F
_IfAmplifierRamanPump1Status_Object=MibTableColumn
ifAmplifierRamanPump1Status=_IfAmplifierRamanPump1Status_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,8),_IfAmplifierRamanPump1Status_Type())
ifAmplifierRamanPump1Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanPump1Status.setStatus(_B)
_IfAmplifierRamanPump2Power_Type=Signed32WithNA
_IfAmplifierRamanPump2Power_Object=MibTableColumn
ifAmplifierRamanPump2Power=_IfAmplifierRamanPump2Power_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,9),_IfAmplifierRamanPump2Power_Type())
ifAmplifierRamanPump2Power.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanPump2Power.setStatus(_B)
class _IfAmplifierRamanPump2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2147483646,2147483647)));namedValues=NamedValues(*((_q,0),('on',1),(_r,2147483646),(_p,2147483647)))
_IfAmplifierRamanPump2Status_Type.__name__=_F
_IfAmplifierRamanPump2Status_Object=MibTableColumn
ifAmplifierRamanPump2Status=_IfAmplifierRamanPump2Status_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,10),_IfAmplifierRamanPump2Status_Type())
ifAmplifierRamanPump2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanPump2Status.setStatus(_B)
_IfAmplifierRamanTotalPumpPower_Type=Signed32WithNA
_IfAmplifierRamanTotalPumpPower_Object=MibTableColumn
ifAmplifierRamanTotalPumpPower=_IfAmplifierRamanTotalPumpPower_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,11),_IfAmplifierRamanTotalPumpPower_Type())
ifAmplifierRamanTotalPumpPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanTotalPumpPower.setStatus(_B)
_IfAmplifierRamanBackReflectionPower_Type=Signed32WithNA
_IfAmplifierRamanBackReflectionPower_Object=MibTableColumn
ifAmplifierRamanBackReflectionPower=_IfAmplifierRamanBackReflectionPower_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,12),_IfAmplifierRamanBackReflectionPower_Type())
ifAmplifierRamanBackReflectionPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanBackReflectionPower.setStatus(_B)
_IfAmplifierRamanBackReflectionPowerRatio_Type=Signed32WithNA
_IfAmplifierRamanBackReflectionPowerRatio_Object=MibTableColumn
ifAmplifierRamanBackReflectionPowerRatio=_IfAmplifierRamanBackReflectionPowerRatio_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,13),_IfAmplifierRamanBackReflectionPowerRatio_Type())
ifAmplifierRamanBackReflectionPowerRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanBackReflectionPowerRatio.setStatus(_B)
_IfAmplifierRamanHighBackReflection_Type=FaultStatusWithNA
_IfAmplifierRamanHighBackReflection_Object=MibTableColumn
ifAmplifierRamanHighBackReflection=_IfAmplifierRamanHighBackReflection_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,14),_IfAmplifierRamanHighBackReflection_Type())
ifAmplifierRamanHighBackReflection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanHighBackReflection.setStatus(_B)
class _IfAmplifierRamanHighBackReflectionThld_Type(Signed32WithNA):defaultValue=260;subtypeSpec=Signed32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,280),ValueRangeConstraint(2147483647,2147483647))
_IfAmplifierRamanHighBackReflectionThld_Type.__name__=_G
_IfAmplifierRamanHighBackReflectionThld_Object=MibTableColumn
ifAmplifierRamanHighBackReflectionThld=_IfAmplifierRamanHighBackReflectionThld_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,15),_IfAmplifierRamanHighBackReflectionThld_Type())
ifAmplifierRamanHighBackReflectionThld.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierRamanHighBackReflectionThld.setStatus(_B)
_IfAmplifierRamanPointInsertionLoss_Type=Signed32WithNA
_IfAmplifierRamanPointInsertionLoss_Object=MibTableColumn
ifAmplifierRamanPointInsertionLoss=_IfAmplifierRamanPointInsertionLoss_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,16),_IfAmplifierRamanPointInsertionLoss_Type())
ifAmplifierRamanPointInsertionLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanPointInsertionLoss.setStatus(_B)
class _IfAmplifierRamanPointInsertionLossThld_Type(Signed32WithNA):defaultValue=-10
_IfAmplifierRamanPointInsertionLossThld_Type.__name__=_G
_IfAmplifierRamanPointInsertionLossThld_Object=MibTableColumn
ifAmplifierRamanPointInsertionLossThld=_IfAmplifierRamanPointInsertionLossThld_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,17),_IfAmplifierRamanPointInsertionLossThld_Type())
ifAmplifierRamanPointInsertionLossThld.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierRamanPointInsertionLossThld.setStatus(_B)
_IfAmplifierRamanHighPointInsertionLoss_Type=FaultStatusWithNA
_IfAmplifierRamanHighPointInsertionLoss_Object=MibTableColumn
ifAmplifierRamanHighPointInsertionLoss=_IfAmplifierRamanHighPointInsertionLoss_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,18),_IfAmplifierRamanHighPointInsertionLoss_Type())
ifAmplifierRamanHighPointInsertionLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanHighPointInsertionLoss.setStatus(_B)
_IfAmplifierRamanRelatedAmplifierIndex_Type=Unsigned32
_IfAmplifierRamanRelatedAmplifierIndex_Object=MibTableColumn
ifAmplifierRamanRelatedAmplifierIndex=_IfAmplifierRamanRelatedAmplifierIndex_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,19),_IfAmplifierRamanRelatedAmplifierIndex_Type())
ifAmplifierRamanRelatedAmplifierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanRelatedAmplifierIndex.setStatus(_B)
_IfAmplifierRamanSubrack_Type=Unsigned32
_IfAmplifierRamanSubrack_Object=MibTableColumn
ifAmplifierRamanSubrack=_IfAmplifierRamanSubrack_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,20),_IfAmplifierRamanSubrack_Type())
ifAmplifierRamanSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanSubrack.setStatus(_B)
_IfAmplifierRamanSlot_Type=Unsigned32
_IfAmplifierRamanSlot_Object=MibTableColumn
ifAmplifierRamanSlot=_IfAmplifierRamanSlot_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,21),_IfAmplifierRamanSlot_Type())
ifAmplifierRamanSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanSlot.setStatus(_B)
_IfAmplifierRamanActualGain_Type=Signed32WithNA
_IfAmplifierRamanActualGain_Object=MibTableColumn
ifAmplifierRamanActualGain=_IfAmplifierRamanActualGain_Object((1,3,6,1,4,1,8708,2,65,2,4,1,1,22),_IfAmplifierRamanActualGain_Type())
ifAmplifierRamanActualGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierRamanActualGain.setStatus(_B)
_IfAmplifierEdfaList_ObjectIdentity=ObjectIdentity
ifAmplifierEdfaList=_IfAmplifierEdfaList_ObjectIdentity((1,3,6,1,4,1,8708,2,65,2,5))
_IfAmplifierEdfaTable_Object=MibTable
ifAmplifierEdfaTable=_IfAmplifierEdfaTable_Object((1,3,6,1,4,1,8708,2,65,2,5,1))
if mibBuilder.loadTexts:ifAmplifierEdfaTable.setStatus(_B)
_IfAmplifierEdfaEntry_Object=MibTableRow
ifAmplifierEdfaEntry=_IfAmplifierEdfaEntry_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1))
ifAmplifierEdfaEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ifAmplifierEdfaEntry.setStatus(_B)
_IfAmplifierEdfaIndex_Type=Unsigned32
_IfAmplifierEdfaIndex_Object=MibTableColumn
ifAmplifierEdfaIndex=_IfAmplifierEdfaIndex_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,1),_IfAmplifierEdfaIndex_Type())
ifAmplifierEdfaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaIndex.setStatus(_B)
_IfAmplifierEdfaName_Type=MgmtNameString
_IfAmplifierEdfaName_Object=MibTableColumn
ifAmplifierEdfaName=_IfAmplifierEdfaName_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,2),_IfAmplifierEdfaName_Type())
ifAmplifierEdfaName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaName.setStatus(_B)
_IfAmplifierEdfaUId_Type=Unsigned32
_IfAmplifierEdfaUId_Object=MibTableColumn
ifAmplifierEdfaUId=_IfAmplifierEdfaUId_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,3),_IfAmplifierEdfaUId_Type())
ifAmplifierEdfaUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaUId.setStatus(_B)
class _IfAmplifierEdfaWantedGainTilt_Type(Signed32WithNA):defaultValue=-10;subtypeSpec=Signed32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,0),ValueRangeConstraint(2147483647,2147483647))
_IfAmplifierEdfaWantedGainTilt_Type.__name__=_G
_IfAmplifierEdfaWantedGainTilt_Object=MibTableColumn
ifAmplifierEdfaWantedGainTilt=_IfAmplifierEdfaWantedGainTilt_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,4),_IfAmplifierEdfaWantedGainTilt_Type())
ifAmplifierEdfaWantedGainTilt.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierEdfaWantedGainTilt.setStatus(_B)
_IfAmplifierEdfaTxPowerLimit_Type=Signed32WithNA
_IfAmplifierEdfaTxPowerLimit_Object=MibTableColumn
ifAmplifierEdfaTxPowerLimit=_IfAmplifierEdfaTxPowerLimit_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,5),_IfAmplifierEdfaTxPowerLimit_Type())
ifAmplifierEdfaTxPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierEdfaTxPowerLimit.setStatus(_B)
class _IfAmplifierEdfaPumpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2147483646)));namedValues=NamedValues(*((_q,0),('on',1),(_r,2147483646)))
_IfAmplifierEdfaPumpStatus_Type.__name__=_F
_IfAmplifierEdfaPumpStatus_Object=MibTableColumn
ifAmplifierEdfaPumpStatus=_IfAmplifierEdfaPumpStatus_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,6),_IfAmplifierEdfaPumpStatus_Type())
ifAmplifierEdfaPumpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaPumpStatus.setStatus(_B)
_IfAmplifierEdfaBackReflectionPower_Type=Signed32WithNA
_IfAmplifierEdfaBackReflectionPower_Object=MibTableColumn
ifAmplifierEdfaBackReflectionPower=_IfAmplifierEdfaBackReflectionPower_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,7),_IfAmplifierEdfaBackReflectionPower_Type())
ifAmplifierEdfaBackReflectionPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaBackReflectionPower.setStatus(_B)
_IfAmplifierEdfaBackReflectionPowerRatio_Type=Signed32WithNA
_IfAmplifierEdfaBackReflectionPowerRatio_Object=MibTableColumn
ifAmplifierEdfaBackReflectionPowerRatio=_IfAmplifierEdfaBackReflectionPowerRatio_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,8),_IfAmplifierEdfaBackReflectionPowerRatio_Type())
ifAmplifierEdfaBackReflectionPowerRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaBackReflectionPowerRatio.setStatus(_B)
_IfAmplifierEdfaHighBackReflection_Type=FaultStatusWithNA
_IfAmplifierEdfaHighBackReflection_Object=MibTableColumn
ifAmplifierEdfaHighBackReflection=_IfAmplifierEdfaHighBackReflection_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,9),_IfAmplifierEdfaHighBackReflection_Type())
ifAmplifierEdfaHighBackReflection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaHighBackReflection.setStatus(_B)
class _IfAmplifierEdfaHighBackReflectionThld_Type(Signed32WithNA):defaultValue=260;subtypeSpec=Signed32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,280),ValueRangeConstraint(2147483647,2147483647))
_IfAmplifierEdfaHighBackReflectionThld_Type.__name__=_G
_IfAmplifierEdfaHighBackReflectionThld_Object=MibTableColumn
ifAmplifierEdfaHighBackReflectionThld=_IfAmplifierEdfaHighBackReflectionThld_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,10),_IfAmplifierEdfaHighBackReflectionThld_Type())
ifAmplifierEdfaHighBackReflectionThld.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAmplifierEdfaHighBackReflectionThld.setStatus(_B)
_IfAmplifierEdfaSaturation_Type=FaultStatusWithNA
_IfAmplifierEdfaSaturation_Object=MibTableColumn
ifAmplifierEdfaSaturation=_IfAmplifierEdfaSaturation_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,11),_IfAmplifierEdfaSaturation_Type())
ifAmplifierEdfaSaturation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaSaturation.setStatus(_E)
_IfAmplifierEdfaMonitorPortLoss_Type=Signed32WithNA
_IfAmplifierEdfaMonitorPortLoss_Object=MibTableColumn
ifAmplifierEdfaMonitorPortLoss=_IfAmplifierEdfaMonitorPortLoss_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,12),_IfAmplifierEdfaMonitorPortLoss_Type())
ifAmplifierEdfaMonitorPortLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaMonitorPortLoss.setStatus(_B)
_IfAmplifierEdfaRelatedAmplifierIndex_Type=Unsigned32
_IfAmplifierEdfaRelatedAmplifierIndex_Object=MibTableColumn
ifAmplifierEdfaRelatedAmplifierIndex=_IfAmplifierEdfaRelatedAmplifierIndex_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,13),_IfAmplifierEdfaRelatedAmplifierIndex_Type())
ifAmplifierEdfaRelatedAmplifierIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaRelatedAmplifierIndex.setStatus(_B)
_IfAmplifierEdfaSubrack_Type=Unsigned32
_IfAmplifierEdfaSubrack_Object=MibTableColumn
ifAmplifierEdfaSubrack=_IfAmplifierEdfaSubrack_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,14),_IfAmplifierEdfaSubrack_Type())
ifAmplifierEdfaSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaSubrack.setStatus(_B)
_IfAmplifierEdfaSlot_Type=Unsigned32
_IfAmplifierEdfaSlot_Object=MibTableColumn
ifAmplifierEdfaSlot=_IfAmplifierEdfaSlot_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,15),_IfAmplifierEdfaSlot_Type())
ifAmplifierEdfaSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaSlot.setStatus(_B)
_IfAmplifierEdfaPumpPower_Type=Signed32WithNA
_IfAmplifierEdfaPumpPower_Object=MibTableColumn
ifAmplifierEdfaPumpPower=_IfAmplifierEdfaPumpPower_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,16),_IfAmplifierEdfaPumpPower_Type())
ifAmplifierEdfaPumpPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaPumpPower.setStatus(_B)
_IfAmplifierEdfaPumpCurrent_Type=Signed32WithNA
_IfAmplifierEdfaPumpCurrent_Object=MibTableColumn
ifAmplifierEdfaPumpCurrent=_IfAmplifierEdfaPumpCurrent_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,17),_IfAmplifierEdfaPumpCurrent_Type())
ifAmplifierEdfaPumpCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaPumpCurrent.setStatus(_B)
_IfAmplifierEdfaActualGain_Type=Signed32WithNA
_IfAmplifierEdfaActualGain_Object=MibTableColumn
ifAmplifierEdfaActualGain=_IfAmplifierEdfaActualGain_Object((1,3,6,1,4,1,8708,2,65,2,5,1,1,18),_IfAmplifierEdfaActualGain_Type())
ifAmplifierEdfaActualGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAmplifierEdfaActualGain.setStatus(_B)
ifAmplifierGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,1))
ifAmplifierGeneralGroupV1.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:ifAmplifierGeneralGroupV1.setStatus(_B)
ifAmplifierAmplifierGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,2))
ifAmplifierAmplifierGroupV1.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ifAmplifierAmplifierGroupV1.setStatus(_E)
ifAmplifierModuleGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,3))
ifAmplifierModuleGroupV1.setObjects(*((_A,_o),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:ifAmplifierModuleGroupV1.setStatus(_B)
ifAmplifierRamanGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,4))
ifAmplifierRamanGroupV1.setObjects(*((_A,_Y),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ifAmplifierRamanGroupV1.setStatus(_E)
ifAmplifierEdfaGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,5))
ifAmplifierEdfaGroupV1.setObjects(*((_A,_I),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_Ak),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ifAmplifierEdfaGroupV1.setStatus(_E)
ifAmplifierAmplifierGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,6))
ifAmplifierAmplifierGroupV2.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ifAmplifierAmplifierGroupV2.setStatus(_E)
ifAmplifierEdfaGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,7))
ifAmplifierEdfaGroupV2.setObjects(*((_A,_I),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ifAmplifierEdfaGroupV2.setStatus(_E)
ifAmplifierRamanGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,8))
ifAmplifierRamanGroupV2.setObjects(*((_A,_Y),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_Al)))
if mibBuilder.loadTexts:ifAmplifierRamanGroupV2.setStatus(_B)
ifAmplifierEdfaGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,9))
ifAmplifierEdfaGroupV3.setObjects(*((_A,_I),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_AC),(_A,_AD),(_A,_Am)))
if mibBuilder.loadTexts:ifAmplifierEdfaGroupV3.setStatus(_B)
ifAmplifierAmplifierGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,10))
ifAmplifierAmplifierGroupV3.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_m),(_A,_n),(_A,_AE)))
if mibBuilder.loadTexts:ifAmplifierAmplifierGroupV3.setStatus(_E)
ifAmplifierAmplifierGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,65,1,1,11))
ifAmplifierAmplifierGroupV4.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_m),(_A,_n),(_A,_AE),(_A,_An)))
if mibBuilder.loadTexts:ifAmplifierAmplifierGroupV4.setStatus(_B)
lumIfAmplifierComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,65,1,2,1))
lumIfAmplifierComplV1.setObjects(*((_A,_W),(_A,_Ao),(_A,_X),(_A,_AF),(_A,_Ap)))
if mibBuilder.loadTexts:lumIfAmplifierComplV1.setStatus(_E)
lumIfAmplifierComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,65,1,2,2))
lumIfAmplifierComplV2.setObjects(*((_A,_W),(_A,_Aq),(_A,_X),(_A,_AF),(_A,_Ar)))
if mibBuilder.loadTexts:lumIfAmplifierComplV2.setStatus(_E)
lumIfAmplifierComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,65,1,2,3))
lumIfAmplifierComplV3.setObjects(*((_A,_W),(_A,_As),(_A,_X),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:lumIfAmplifierComplV3.setStatus(_E)
lumIfAmplifierComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,65,1,2,4))
lumIfAmplifierComplV4.setObjects(*((_A,_W),(_A,_At),(_A,_X),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:lumIfAmplifierComplV4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfAmplifierMIBModule':lumIfAmplifierMIBModule,'lumIfAmplifierConfs':lumIfAmplifierConfs,'lumIfAmplifierGroups':lumIfAmplifierGroups,_W:ifAmplifierGeneralGroupV1,_Ao:ifAmplifierAmplifierGroupV1,_X:ifAmplifierModuleGroupV1,_AF:ifAmplifierRamanGroupV1,_Ap:ifAmplifierEdfaGroupV1,_Aq:ifAmplifierAmplifierGroupV2,_Ar:ifAmplifierEdfaGroupV2,_AG:ifAmplifierRamanGroupV2,_AH:ifAmplifierEdfaGroupV3,_As:ifAmplifierAmplifierGroupV3,_At:ifAmplifierAmplifierGroupV4,'lumIfAmplifierCompl':lumIfAmplifierCompl,'lumIfAmplifierComplV1':lumIfAmplifierComplV1,'lumIfAmplifierComplV2':lumIfAmplifierComplV2,'lumIfAmplifierComplV3':lumIfAmplifierComplV3,'lumIfAmplifierComplV4':lumIfAmplifierComplV4,'lumIfAmplifierMIBObjects':lumIfAmplifierMIBObjects,'ifAmplifierGeneral':ifAmplifierGeneral,_AL:ifAmplifierGeneralConfigLastChangeTime,_AM:ifAmplifierGeneralStateLastChangeTime,_AN:ifAmplifierGeneralIfAmplifierAmplifierTableSize,_AO:ifAmplifierGeneralIfAmplifierAmplifierConfigLastChangeTime,_AP:ifAmplifierGeneralIfAmplifierAmplifierStateLastChangeTime,_AQ:ifAmplifierGeneralIfAmplifierModuleTableSize,_AR:ifAmplifierGeneralIfAmplifierModuleConfigLastChangeTime,_AS:ifAmplifierGeneralIfAmplifierModuleStateLastChangeTime,_AT:ifAmplifierGeneralIfAmplifierRamanTableSize,_AU:ifAmplifierGeneralIfAmplifierRamanConfigLastChangeTime,_AV:ifAmplifierGeneralIfAmplifierRamanStateLastChangeTime,_AW:ifAmplifierGeneralIfAmplifierEdfaTableSize,_AX:ifAmplifierGeneralIfAmplifierEdfaConfigLastChangeTime,_AY:ifAmplifierGeneralIfAmplifierEdfaStateLastChangeTime,'ifAmplifierAmplifierList':ifAmplifierAmplifierList,'ifAmplifierAmplifierTable':ifAmplifierAmplifierTable,'ifAmplifierAmplifierEntry':ifAmplifierAmplifierEntry,_H:ifAmplifierAmplifierIndex,_J:ifAmplifierAmplifierName,_K:ifAmplifierAmplifierUId,_L:ifAmplifierAmplifierRxPower,_M:ifAmplifierAmplifierTxPower,_N:ifAmplifierAmplifierWantedGain,_O:ifAmplifierAmplifierActualGain,_P:ifAmplifierAmplifierAdminStatus,_Q:ifAmplifierAmplifierOperStatus,_R:ifAmplifierAmplifierMidStageLoss,_S:ifAmplifierAmplifierTxIfIndex,_T:ifAmplifierAmplifierRxIfIndex,_U:ifAmplifierAmplifierSubrack,_V:ifAmplifierAmplifierSlot,_m:ifAmplifierAmplifierOutputPowerFail,_n:ifAmplifierAmplifierSaturation,_AE:ifAmplifierAmplifierFunctionalType,_An:ifAmplifierAmplifierDescr,'ifAmplifierModuleList':ifAmplifierModuleList,'ifAmplifierModuleTable':ifAmplifierModuleTable,'ifAmplifierModuleEntry':ifAmplifierModuleEntry,_o:ifAmplifierModuleIndex,_AZ:ifAmplifierModuleName,_Aa:ifAmplifierModuleUId,_Ab:ifAmplifierModuleTemperature,_Ac:ifAmplifierModuleInfo,_Ad:ifAmplifierModuleHighModuleTemperature,_Ae:ifAmplifierModuleHighPumpCurrent,_Af:ifAmplifierModuleHighPumpTemperature,_Ag:ifAmplifierModuleCommunicationFailure,_Ah:ifAmplifierModuleColdRestart,_Ai:ifAmplifierModuleSubrack,_Aj:ifAmplifierModuleSlot,'ifAmplifierRamanList':ifAmplifierRamanList,'ifAmplifierRamanTable':ifAmplifierRamanTable,'ifAmplifierRamanEntry':ifAmplifierRamanEntry,_Y:ifAmplifierRamanIndex,_s:ifAmplifierRamanName,_t:ifAmplifierRamanUId,_u:ifAmplifierRamanLineFiberType,_v:ifAmplifierRamanWantedGainTilt,_w:ifAmplifierRamanReceivedPowerLevel,_x:ifAmplifierRamanPump1Power,_y:ifAmplifierRamanPump1Status,_z:ifAmplifierRamanPump2Power,_A0:ifAmplifierRamanPump2Status,_A1:ifAmplifierRamanTotalPumpPower,_A2:ifAmplifierRamanBackReflectionPower,_A3:ifAmplifierRamanBackReflectionPowerRatio,_A4:ifAmplifierRamanHighBackReflection,_A5:ifAmplifierRamanHighBackReflectionThld,_A6:ifAmplifierRamanPointInsertionLoss,_A7:ifAmplifierRamanPointInsertionLossThld,_A8:ifAmplifierRamanHighPointInsertionLoss,_A9:ifAmplifierRamanRelatedAmplifierIndex,_AA:ifAmplifierRamanSubrack,_AB:ifAmplifierRamanSlot,_Al:ifAmplifierRamanActualGain,'ifAmplifierEdfaList':ifAmplifierEdfaList,'ifAmplifierEdfaTable':ifAmplifierEdfaTable,'ifAmplifierEdfaEntry':ifAmplifierEdfaEntry,_I:ifAmplifierEdfaIndex,_Z:ifAmplifierEdfaName,_a:ifAmplifierEdfaUId,_b:ifAmplifierEdfaWantedGainTilt,_c:ifAmplifierEdfaTxPowerLimit,_d:ifAmplifierEdfaPumpStatus,_e:ifAmplifierEdfaBackReflectionPower,_f:ifAmplifierEdfaBackReflectionPowerRatio,_g:ifAmplifierEdfaHighBackReflection,_h:ifAmplifierEdfaHighBackReflectionThld,_Ak:ifAmplifierEdfaSaturation,_i:ifAmplifierEdfaMonitorPortLoss,_j:ifAmplifierEdfaRelatedAmplifierIndex,_k:ifAmplifierEdfaSubrack,_l:ifAmplifierEdfaSlot,_AC:ifAmplifierEdfaPumpPower,_AD:ifAmplifierEdfaPumpCurrent,_Am:ifAmplifierEdfaActualGain})