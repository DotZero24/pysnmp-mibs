_AU='ciuUpgradeOpNewGroup'
_AT='ciuUpgradeJobStatusNotify'
_AS='ciuUpgradeOpCompletionNotify'
_AR='ciuUpgradeOpLastStatusReason'
_AQ='ciuUpgradeJobStatusNotifyOnCompletion'
_AP='ciuUpgradeMiscInfoDescr'
_AO='ciuUpgradeMiscInfoModule'
_AN='ciuUpgradeMiscAutoCopy'
_AM='ciuUpgradeImageVersionUpgReqd'
_AL='ciuUpgradeImageVersionNew'
_AK='ciuUpgradeImageVersionRunning'
_AJ='ciuUpgradeImageVersionVarName'
_AI='ciuVersionCompUpgradeReason'
_AH='ciuVersionCompUpgradeImpact'
_AG='ciuVersionCompUpgradeLoader'
_AF='ciuVersionCompUpgradeBootrom'
_AE='ciuVersionCompUpgradeBios'
_AD='ciuVersionCompUpgradeAction'
_AC='ciuVersionCompUpgradable'
_AB='ciuVersionCompImageSame'
_AA='ciuImageLocInputEntryStatus'
_A9='ciuImageLocInputURI'
_A8='ciuUpgradeTargetEntryStatus'
_A7='ciuUpgradeTargetAction'
_A6='ciuUpgradeOpAbort'
_A5='ciuUpgradeOpTimeStarted'
_A4='ciuUpgradeOpNotifyOnCompletion'
_A3='ciuImageURI'
_A2='ciuTotalImageVariables'
_A1='ciuUpgradeMiscInfoIndex'
_A0='ciuUpgradeOpStatusOperIndex'
_z='ciuUpgradeImageVersionIndex'
_y='notApplicable'
_x='fsUpgReset'
_w='successReset'
_v='abortFailed'
_u='abortSuccess'
_t='abortInProgress'
_s='failure'
_r='invalidOperation'
_q='install'
_p='ciuUpgradeNotificationGroupSup'
_o='ciuUpgradeOpLastStatus'
_n='ciuUpgradeOpLastCommand'
_m='ciuUpgradeOpStatusJobStatusReas'
_l='ciuUpgradeOpStatusPercentCompl'
_k='ciuUpgradeOpStatusJobStatus'
_j='ciuUpgradeOpStatusDestImageLoc'
_i='ciuUpgradeOpStatusSrcImageLoc'
_h='ciuUpgradeOpStatusModule'
_g='ciuUpgradeOpStatusOperation'
_f='ciuUpgradeOpStatusReason'
_e='ciuUpgradeOpTimeCompleted'
_d='ciuUpgradeOpCommand'
_c='not-accessible'
_b='success'
_a='inProgress'
_Z='ciuUpgradeMiscInfoGroup'
_Y='deprecated'
_X='ciuUpgradeOpStatus'
_W='other'
_V='read-create'
_U='TruthValue'
_T='SnmpAdminString'
_S='ciuUpgradeMiscGroup'
_R='none'
_Q='ciuImageVariableName'
_P='entPhysicalIndex'
_O='ENTITY-MIB'
_N='ciuUpgradeNotificationGroup'
_M='ciuUpgradeOpStatusGroup'
_L='ciuUpgradeImageVersionGroup'
_K='ciuVersionCompChkGroup'
_J='ciuImageLocInputGroup'
_I='ciuUpgradeOpGroup'
_H='ciuImageURIGroup'
_G='ciuImageVariableGroup'
_F='ciuImageUpgradeGroup'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-IMAGE-UPGRADE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
entPhysicalIndex,=mibBuilder.importSymbols(_O,_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_U)
ciscoImageUpgradeMIB=ModuleIdentity((1,3,6,1,4,1,9,9,360))
if mibBuilder.loadTexts:ciscoImageUpgradeMIB.setRevisions(('2011-03-28 00:00','2008-03-18 00:00','2007-07-18 00:00','2006-12-21 00:00','2004-01-20 00:00','2003-11-04 00:00','2003-10-28 00:00','2003-07-11 00:00','2003-07-08 00:00','2003-06-01 00:00'))
class CiuImageVariableTypeName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiscoImageUpgradeMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeMIBNotifs=_CiscoImageUpgradeMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,360,0))
_CiscoImageUpgradeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeMIBObjects=_CiscoImageUpgradeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,360,1))
_CiscoImageUpgradeConfig_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeConfig=_CiscoImageUpgradeConfig_ObjectIdentity((1,3,6,1,4,1,9,9,360,1,1))
_CiuTotalImageVariables_Type=Unsigned32
_CiuTotalImageVariables_Object=MibScalar
ciuTotalImageVariables=_CiuTotalImageVariables_Object((1,3,6,1,4,1,9,9,360,1,1,1),_CiuTotalImageVariables_Type())
ciuTotalImageVariables.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuTotalImageVariables.setStatus(_B)
_CiuImageVariableTable_Object=MibTable
ciuImageVariableTable=_CiuImageVariableTable_Object((1,3,6,1,4,1,9,9,360,1,1,2))
if mibBuilder.loadTexts:ciuImageVariableTable.setStatus(_B)
_CiuImageVariableEntry_Object=MibTableRow
ciuImageVariableEntry=_CiuImageVariableEntry_Object((1,3,6,1,4,1,9,9,360,1,1,2,1))
ciuImageVariableEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:ciuImageVariableEntry.setStatus(_B)
_CiuImageVariableName_Type=CiuImageVariableTypeName
_CiuImageVariableName_Object=MibTableColumn
ciuImageVariableName=_CiuImageVariableName_Object((1,3,6,1,4,1,9,9,360,1,1,2,1,1),_CiuImageVariableName_Type())
ciuImageVariableName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuImageVariableName.setStatus(_B)
_CiuImageURITable_Object=MibTable
ciuImageURITable=_CiuImageURITable_Object((1,3,6,1,4,1,9,9,360,1,1,3))
if mibBuilder.loadTexts:ciuImageURITable.setStatus(_B)
_CiuImageURIEntry_Object=MibTableRow
ciuImageURIEntry=_CiuImageURIEntry_Object((1,3,6,1,4,1,9,9,360,1,1,3,1))
ciuImageURIEntry.setIndexNames((0,_O,_P),(0,_A,_Q))
if mibBuilder.loadTexts:ciuImageURIEntry.setStatus(_B)
_CiuImageURI_Type=SnmpAdminString
_CiuImageURI_Object=MibTableColumn
ciuImageURI=_CiuImageURI_Object((1,3,6,1,4,1,9,9,360,1,1,3,1,1),_CiuImageURI_Type())
ciuImageURI.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuImageURI.setStatus(_B)
_CiscoImageUpgradeOp_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeOp=_CiscoImageUpgradeOp_ObjectIdentity((1,3,6,1,4,1,9,9,360,1,1,4))
class _CiuUpgradeOpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('done',2),(_q,3),('check',4)))
_CiuUpgradeOpCommand_Type.__name__=_D
_CiuUpgradeOpCommand_Object=MibScalar
ciuUpgradeOpCommand=_CiuUpgradeOpCommand_Object((1,3,6,1,4,1,9,9,360,1,1,4,1),_CiuUpgradeOpCommand_Type())
ciuUpgradeOpCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuUpgradeOpCommand.setStatus(_B)
class _CiuUpgradeOpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_R,1),(_r,2),(_s,3),(_a,4),(_b,5),(_t,6),(_u,7),(_v,8),(_w,9),(_x,10)))
_CiuUpgradeOpStatus_Type.__name__=_D
_CiuUpgradeOpStatus_Object=MibScalar
ciuUpgradeOpStatus=_CiuUpgradeOpStatus_Object((1,3,6,1,4,1,9,9,360,1,1,4,2),_CiuUpgradeOpStatus_Type())
ciuUpgradeOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatus.setStatus(_B)
class _CiuUpgradeOpNotifyOnCompletion_Type(TruthValue):defaultValue=2
_CiuUpgradeOpNotifyOnCompletion_Type.__name__=_U
_CiuUpgradeOpNotifyOnCompletion_Object=MibScalar
ciuUpgradeOpNotifyOnCompletion=_CiuUpgradeOpNotifyOnCompletion_Object((1,3,6,1,4,1,9,9,360,1,1,4,3),_CiuUpgradeOpNotifyOnCompletion_Type())
ciuUpgradeOpNotifyOnCompletion.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuUpgradeOpNotifyOnCompletion.setStatus(_B)
_CiuUpgradeOpTimeStarted_Type=TimeStamp
_CiuUpgradeOpTimeStarted_Object=MibScalar
ciuUpgradeOpTimeStarted=_CiuUpgradeOpTimeStarted_Object((1,3,6,1,4,1,9,9,360,1,1,4,4),_CiuUpgradeOpTimeStarted_Type())
ciuUpgradeOpTimeStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpTimeStarted.setStatus(_B)
_CiuUpgradeOpTimeCompleted_Type=TimeStamp
_CiuUpgradeOpTimeCompleted_Object=MibScalar
ciuUpgradeOpTimeCompleted=_CiuUpgradeOpTimeCompleted_Object((1,3,6,1,4,1,9,9,360,1,1,4,5),_CiuUpgradeOpTimeCompleted_Type())
ciuUpgradeOpTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpTimeCompleted.setStatus(_B)
class _CiuUpgradeOpAbort_Type(TruthValue):defaultValue=2
_CiuUpgradeOpAbort_Type.__name__=_U
_CiuUpgradeOpAbort_Object=MibScalar
ciuUpgradeOpAbort=_CiuUpgradeOpAbort_Object((1,3,6,1,4,1,9,9,360,1,1,4,6),_CiuUpgradeOpAbort_Type())
ciuUpgradeOpAbort.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuUpgradeOpAbort.setStatus(_B)
_CiuUpgradeOpStatusReason_Type=SnmpAdminString
_CiuUpgradeOpStatusReason_Object=MibScalar
ciuUpgradeOpStatusReason=_CiuUpgradeOpStatusReason_Object((1,3,6,1,4,1,9,9,360,1,1,4,7),_CiuUpgradeOpStatusReason_Type())
ciuUpgradeOpStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusReason.setStatus(_B)
class _CiuUpgradeOpLastCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('done',2),(_q,3),('check',4)))
_CiuUpgradeOpLastCommand_Type.__name__=_D
_CiuUpgradeOpLastCommand_Object=MibScalar
ciuUpgradeOpLastCommand=_CiuUpgradeOpLastCommand_Object((1,3,6,1,4,1,9,9,360,1,1,4,8),_CiuUpgradeOpLastCommand_Type())
ciuUpgradeOpLastCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpLastCommand.setStatus(_B)
class _CiuUpgradeOpLastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_R,1),(_r,2),(_s,3),(_a,4),(_b,5),(_t,6),(_u,7),(_v,8),(_w,9),(_x,10)))
_CiuUpgradeOpLastStatus_Type.__name__=_D
_CiuUpgradeOpLastStatus_Object=MibScalar
ciuUpgradeOpLastStatus=_CiuUpgradeOpLastStatus_Object((1,3,6,1,4,1,9,9,360,1,1,4,9),_CiuUpgradeOpLastStatus_Type())
ciuUpgradeOpLastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpLastStatus.setStatus(_B)
_CiuUpgradeOpLastStatusReason_Type=SnmpAdminString
_CiuUpgradeOpLastStatusReason_Object=MibScalar
ciuUpgradeOpLastStatusReason=_CiuUpgradeOpLastStatusReason_Object((1,3,6,1,4,1,9,9,360,1,1,4,10),_CiuUpgradeOpLastStatusReason_Type())
ciuUpgradeOpLastStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpLastStatusReason.setStatus(_B)
_CiuUpgradeJobStatusNotifyOnCompletion_Type=TruthValue
_CiuUpgradeJobStatusNotifyOnCompletion_Object=MibScalar
ciuUpgradeJobStatusNotifyOnCompletion=_CiuUpgradeJobStatusNotifyOnCompletion_Object((1,3,6,1,4,1,9,9,360,1,1,4,11),_CiuUpgradeJobStatusNotifyOnCompletion_Type())
ciuUpgradeJobStatusNotifyOnCompletion.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuUpgradeJobStatusNotifyOnCompletion.setStatus(_B)
_CiuUpgradeTargetTable_Object=MibTable
ciuUpgradeTargetTable=_CiuUpgradeTargetTable_Object((1,3,6,1,4,1,9,9,360,1,1,5))
if mibBuilder.loadTexts:ciuUpgradeTargetTable.setStatus(_B)
_CiuUpgradeTargetEntry_Object=MibTableRow
ciuUpgradeTargetEntry=_CiuUpgradeTargetEntry_Object((1,3,6,1,4,1,9,9,360,1,1,5,1))
ciuUpgradeTargetEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:ciuUpgradeTargetEntry.setStatus(_B)
class _CiuUpgradeTargetAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('image',1),('bios',2),('loader',3),('bootrom',4)))
_CiuUpgradeTargetAction_Type.__name__=_D
_CiuUpgradeTargetAction_Object=MibTableColumn
ciuUpgradeTargetAction=_CiuUpgradeTargetAction_Object((1,3,6,1,4,1,9,9,360,1,1,5,1,1),_CiuUpgradeTargetAction_Type())
ciuUpgradeTargetAction.setMaxAccess(_V)
if mibBuilder.loadTexts:ciuUpgradeTargetAction.setStatus(_B)
_CiuUpgradeTargetEntryStatus_Type=RowStatus
_CiuUpgradeTargetEntryStatus_Object=MibTableColumn
ciuUpgradeTargetEntryStatus=_CiuUpgradeTargetEntryStatus_Object((1,3,6,1,4,1,9,9,360,1,1,5,1,2),_CiuUpgradeTargetEntryStatus_Type())
ciuUpgradeTargetEntryStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:ciuUpgradeTargetEntryStatus.setStatus(_B)
_CiuImageLocInputTable_Object=MibTable
ciuImageLocInputTable=_CiuImageLocInputTable_Object((1,3,6,1,4,1,9,9,360,1,1,6))
if mibBuilder.loadTexts:ciuImageLocInputTable.setStatus(_B)
_CiuImageLocInputEntry_Object=MibTableRow
ciuImageLocInputEntry=_CiuImageLocInputEntry_Object((1,3,6,1,4,1,9,9,360,1,1,6,1))
ciuImageLocInputEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:ciuImageLocInputEntry.setStatus(_B)
class _CiuImageLocInputURI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiuImageLocInputURI_Type.__name__=_T
_CiuImageLocInputURI_Object=MibTableColumn
ciuImageLocInputURI=_CiuImageLocInputURI_Object((1,3,6,1,4,1,9,9,360,1,1,6,1,1),_CiuImageLocInputURI_Type())
ciuImageLocInputURI.setMaxAccess(_V)
if mibBuilder.loadTexts:ciuImageLocInputURI.setStatus(_B)
_CiuImageLocInputEntryStatus_Type=RowStatus
_CiuImageLocInputEntryStatus_Object=MibTableColumn
ciuImageLocInputEntryStatus=_CiuImageLocInputEntryStatus_Object((1,3,6,1,4,1,9,9,360,1,1,6,1,2),_CiuImageLocInputEntryStatus_Type())
ciuImageLocInputEntryStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:ciuImageLocInputEntryStatus.setStatus(_B)
_CiuVersionCompChkTable_Object=MibTable
ciuVersionCompChkTable=_CiuVersionCompChkTable_Object((1,3,6,1,4,1,9,9,360,1,1,7))
if mibBuilder.loadTexts:ciuVersionCompChkTable.setStatus(_B)
_CiuVersionCompChkEntry_Object=MibTableRow
ciuVersionCompChkEntry=_CiuVersionCompChkEntry_Object((1,3,6,1,4,1,9,9,360,1,1,7,1))
ciuVersionCompChkEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:ciuVersionCompChkEntry.setStatus(_B)
_CiuVersionCompImageSame_Type=TruthValue
_CiuVersionCompImageSame_Object=MibTableColumn
ciuVersionCompImageSame=_CiuVersionCompImageSame_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,1),_CiuVersionCompImageSame_Type())
ciuVersionCompImageSame.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompImageSame.setStatus(_B)
_CiuVersionCompUpgradable_Type=TruthValue
_CiuVersionCompUpgradable_Object=MibTableColumn
ciuVersionCompUpgradable=_CiuVersionCompUpgradable_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,2),_CiuVersionCompUpgradable_Type())
ciuVersionCompUpgradable.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradable.setStatus(_B)
class _CiuVersionCompUpgradeAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_W,2),('rollingUpgrade',3),('switchOverReset',4),('reset',5),('copy',6),(_y,7),('plugin',8)))
_CiuVersionCompUpgradeAction_Type.__name__=_D
_CiuVersionCompUpgradeAction_Object=MibTableColumn
ciuVersionCompUpgradeAction=_CiuVersionCompUpgradeAction_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,3),_CiuVersionCompUpgradeAction_Type())
ciuVersionCompUpgradeAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeAction.setStatus(_B)
_CiuVersionCompUpgradeBios_Type=TruthValue
_CiuVersionCompUpgradeBios_Object=MibTableColumn
ciuVersionCompUpgradeBios=_CiuVersionCompUpgradeBios_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,4),_CiuVersionCompUpgradeBios_Type())
ciuVersionCompUpgradeBios.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeBios.setStatus(_B)
_CiuVersionCompUpgradeBootrom_Type=TruthValue
_CiuVersionCompUpgradeBootrom_Object=MibTableColumn
ciuVersionCompUpgradeBootrom=_CiuVersionCompUpgradeBootrom_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,5),_CiuVersionCompUpgradeBootrom_Type())
ciuVersionCompUpgradeBootrom.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeBootrom.setStatus(_B)
_CiuVersionCompUpgradeLoader_Type=TruthValue
_CiuVersionCompUpgradeLoader_Object=MibTableColumn
ciuVersionCompUpgradeLoader=_CiuVersionCompUpgradeLoader_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,6),_CiuVersionCompUpgradeLoader_Type())
ciuVersionCompUpgradeLoader.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeLoader.setStatus(_B)
class _CiuVersionCompUpgradeImpact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('nonDisruptive',2),('disruptive',3),(_y,4)))
_CiuVersionCompUpgradeImpact_Type.__name__=_D
_CiuVersionCompUpgradeImpact_Object=MibTableColumn
ciuVersionCompUpgradeImpact=_CiuVersionCompUpgradeImpact_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,7),_CiuVersionCompUpgradeImpact_Type())
ciuVersionCompUpgradeImpact.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeImpact.setStatus(_B)
_CiuVersionCompUpgradeReason_Type=SnmpAdminString
_CiuVersionCompUpgradeReason_Object=MibTableColumn
ciuVersionCompUpgradeReason=_CiuVersionCompUpgradeReason_Object((1,3,6,1,4,1,9,9,360,1,1,7,1,8),_CiuVersionCompUpgradeReason_Type())
ciuVersionCompUpgradeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuVersionCompUpgradeReason.setStatus(_B)
_CiuUpgradeImageVersionTable_Object=MibTable
ciuUpgradeImageVersionTable=_CiuUpgradeImageVersionTable_Object((1,3,6,1,4,1,9,9,360,1,1,8))
if mibBuilder.loadTexts:ciuUpgradeImageVersionTable.setStatus(_B)
_CiuUpgradeImageVersionEntry_Object=MibTableRow
ciuUpgradeImageVersionEntry=_CiuUpgradeImageVersionEntry_Object((1,3,6,1,4,1,9,9,360,1,1,8,1))
ciuUpgradeImageVersionEntry.setIndexNames((0,_O,_P),(0,_A,_z))
if mibBuilder.loadTexts:ciuUpgradeImageVersionEntry.setStatus(_B)
_CiuUpgradeImageVersionIndex_Type=Unsigned32
_CiuUpgradeImageVersionIndex_Object=MibTableColumn
ciuUpgradeImageVersionIndex=_CiuUpgradeImageVersionIndex_Object((1,3,6,1,4,1,9,9,360,1,1,8,1,1),_CiuUpgradeImageVersionIndex_Type())
ciuUpgradeImageVersionIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:ciuUpgradeImageVersionIndex.setStatus(_B)
_CiuUpgradeImageVersionVarName_Type=CiuImageVariableTypeName
_CiuUpgradeImageVersionVarName_Object=MibTableColumn
ciuUpgradeImageVersionVarName=_CiuUpgradeImageVersionVarName_Object((1,3,6,1,4,1,9,9,360,1,1,8,1,2),_CiuUpgradeImageVersionVarName_Type())
ciuUpgradeImageVersionVarName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeImageVersionVarName.setStatus(_B)
class _CiuUpgradeImageVersionRunning_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiuUpgradeImageVersionRunning_Type.__name__=_T
_CiuUpgradeImageVersionRunning_Object=MibTableColumn
ciuUpgradeImageVersionRunning=_CiuUpgradeImageVersionRunning_Object((1,3,6,1,4,1,9,9,360,1,1,8,1,3),_CiuUpgradeImageVersionRunning_Type())
ciuUpgradeImageVersionRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeImageVersionRunning.setStatus(_B)
class _CiuUpgradeImageVersionNew_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiuUpgradeImageVersionNew_Type.__name__=_T
_CiuUpgradeImageVersionNew_Object=MibTableColumn
ciuUpgradeImageVersionNew=_CiuUpgradeImageVersionNew_Object((1,3,6,1,4,1,9,9,360,1,1,8,1,4),_CiuUpgradeImageVersionNew_Type())
ciuUpgradeImageVersionNew.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeImageVersionNew.setStatus(_B)
_CiuUpgradeImageVersionUpgReqd_Type=TruthValue
_CiuUpgradeImageVersionUpgReqd_Object=MibTableColumn
ciuUpgradeImageVersionUpgReqd=_CiuUpgradeImageVersionUpgReqd_Object((1,3,6,1,4,1,9,9,360,1,1,8,1,5),_CiuUpgradeImageVersionUpgReqd_Type())
ciuUpgradeImageVersionUpgReqd.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeImageVersionUpgReqd.setStatus(_B)
_CiuUpgradeOpStatusTable_Object=MibTable
ciuUpgradeOpStatusTable=_CiuUpgradeOpStatusTable_Object((1,3,6,1,4,1,9,9,360,1,1,9))
if mibBuilder.loadTexts:ciuUpgradeOpStatusTable.setStatus(_B)
_CiuUpgradeOpStatusEntry_Object=MibTableRow
ciuUpgradeOpStatusEntry=_CiuUpgradeOpStatusEntry_Object((1,3,6,1,4,1,9,9,360,1,1,9,1))
ciuUpgradeOpStatusEntry.setIndexNames((0,_A,_A0))
if mibBuilder.loadTexts:ciuUpgradeOpStatusEntry.setStatus(_B)
_CiuUpgradeOpStatusOperIndex_Type=Unsigned32
_CiuUpgradeOpStatusOperIndex_Object=MibTableColumn
ciuUpgradeOpStatusOperIndex=_CiuUpgradeOpStatusOperIndex_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,1),_CiuUpgradeOpStatusOperIndex_Type())
ciuUpgradeOpStatusOperIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:ciuUpgradeOpStatusOperIndex.setStatus(_B)
class _CiuUpgradeOpStatusOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*(('unknown',1),(_W,2),('copy',3),('verify',4),('versionExtraction',5),('imageSync',6),('configSync',7),('preUpgrade',8),('forceDownload',9),('moduleOnline',10),('hitlessLCUpgrade',11),('hitfulLCUpgrade',12),('unusedBootvar',13),('convertStartUp',14),('looseIncompatibility',15),('haSeqNumMismatch',16),('unknownModuleOnline',17),('recommendedAction',18),('recoveryAction',19),('remainingAction',20),('additionalInfo',21),('settingBootvars',22),('informLcmFsUpg',23),('sysmgrSaveRuntimeStateAndSuccessReset',24),('kexecLoadUpgImages',25),('fsUpgCleanup',26),('saveMtsState',27),('fsUpgBegin',28),('lcWarmBootStatus',29),('waitStateVerificationStatus',30),('informLcmFsUpgExternalLc',31),('externalLcWarmBootStatus',32),('total',33),('compactFlashTcamSanity',34),('systemPreupgradeBegin',35)))
_CiuUpgradeOpStatusOperation_Type.__name__=_D
_CiuUpgradeOpStatusOperation_Object=MibTableColumn
ciuUpgradeOpStatusOperation=_CiuUpgradeOpStatusOperation_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,2),_CiuUpgradeOpStatusOperation_Type())
ciuUpgradeOpStatusOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusOperation.setStatus(_B)
_CiuUpgradeOpStatusModule_Type=EntPhysicalIndexOrZero
_CiuUpgradeOpStatusModule_Object=MibTableColumn
ciuUpgradeOpStatusModule=_CiuUpgradeOpStatusModule_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,3),_CiuUpgradeOpStatusModule_Type())
ciuUpgradeOpStatusModule.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusModule.setStatus(_B)
_CiuUpgradeOpStatusSrcImageLoc_Type=SnmpAdminString
_CiuUpgradeOpStatusSrcImageLoc_Object=MibTableColumn
ciuUpgradeOpStatusSrcImageLoc=_CiuUpgradeOpStatusSrcImageLoc_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,4),_CiuUpgradeOpStatusSrcImageLoc_Type())
ciuUpgradeOpStatusSrcImageLoc.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusSrcImageLoc.setStatus(_B)
_CiuUpgradeOpStatusDestImageLoc_Type=SnmpAdminString
_CiuUpgradeOpStatusDestImageLoc_Object=MibTableColumn
ciuUpgradeOpStatusDestImageLoc=_CiuUpgradeOpStatusDestImageLoc_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,5),_CiuUpgradeOpStatusDestImageLoc_Type())
ciuUpgradeOpStatusDestImageLoc.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusDestImageLoc.setStatus(_B)
class _CiuUpgradeOpStatusJobStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),(_W,2),('failed',3),(_a,4),(_b,5),('planned',6)))
_CiuUpgradeOpStatusJobStatus_Type.__name__=_D
_CiuUpgradeOpStatusJobStatus_Object=MibTableColumn
ciuUpgradeOpStatusJobStatus=_CiuUpgradeOpStatusJobStatus_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,6),_CiuUpgradeOpStatusJobStatus_Type())
ciuUpgradeOpStatusJobStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusJobStatus.setStatus(_B)
_CiuUpgradeOpStatusPercentCompl_Type=Integer32
_CiuUpgradeOpStatusPercentCompl_Object=MibTableColumn
ciuUpgradeOpStatusPercentCompl=_CiuUpgradeOpStatusPercentCompl_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,7),_CiuUpgradeOpStatusPercentCompl_Type())
ciuUpgradeOpStatusPercentCompl.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusPercentCompl.setStatus(_B)
_CiuUpgradeOpStatusJobStatusReas_Type=SnmpAdminString
_CiuUpgradeOpStatusJobStatusReas_Object=MibTableColumn
ciuUpgradeOpStatusJobStatusReas=_CiuUpgradeOpStatusJobStatusReas_Object((1,3,6,1,4,1,9,9,360,1,1,9,1,8),_CiuUpgradeOpStatusJobStatusReas_Type())
ciuUpgradeOpStatusJobStatusReas.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeOpStatusJobStatusReas.setStatus(_B)
_CiscoImageUpgradeMisc_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeMisc=_CiscoImageUpgradeMisc_ObjectIdentity((1,3,6,1,4,1,9,9,360,1,1,10))
class _CiuUpgradeMiscAutoCopy_Type(TruthValue):defaultValue=2
_CiuUpgradeMiscAutoCopy_Type.__name__=_U
_CiuUpgradeMiscAutoCopy_Object=MibScalar
ciuUpgradeMiscAutoCopy=_CiuUpgradeMiscAutoCopy_Object((1,3,6,1,4,1,9,9,360,1,1,10,1),_CiuUpgradeMiscAutoCopy_Type())
ciuUpgradeMiscAutoCopy.setMaxAccess(_E)
if mibBuilder.loadTexts:ciuUpgradeMiscAutoCopy.setStatus(_B)
_CiuUpgradeMiscInfoTable_Object=MibTable
ciuUpgradeMiscInfoTable=_CiuUpgradeMiscInfoTable_Object((1,3,6,1,4,1,9,9,360,1,1,11))
if mibBuilder.loadTexts:ciuUpgradeMiscInfoTable.setStatus(_B)
_CiuUpgradeMiscInfoEntry_Object=MibTableRow
ciuUpgradeMiscInfoEntry=_CiuUpgradeMiscInfoEntry_Object((1,3,6,1,4,1,9,9,360,1,1,11,1))
ciuUpgradeMiscInfoEntry.setIndexNames((0,_A,_A1))
if mibBuilder.loadTexts:ciuUpgradeMiscInfoEntry.setStatus(_B)
_CiuUpgradeMiscInfoIndex_Type=Unsigned32
_CiuUpgradeMiscInfoIndex_Object=MibTableColumn
ciuUpgradeMiscInfoIndex=_CiuUpgradeMiscInfoIndex_Object((1,3,6,1,4,1,9,9,360,1,1,11,1,1),_CiuUpgradeMiscInfoIndex_Type())
ciuUpgradeMiscInfoIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:ciuUpgradeMiscInfoIndex.setStatus(_B)
_CiuUpgradeMiscInfoModule_Type=EntPhysicalIndexOrZero
_CiuUpgradeMiscInfoModule_Object=MibTableColumn
ciuUpgradeMiscInfoModule=_CiuUpgradeMiscInfoModule_Object((1,3,6,1,4,1,9,9,360,1,1,11,1,2),_CiuUpgradeMiscInfoModule_Type())
ciuUpgradeMiscInfoModule.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeMiscInfoModule.setStatus(_B)
_CiuUpgradeMiscInfoDescr_Type=SnmpAdminString
_CiuUpgradeMiscInfoDescr_Object=MibTableColumn
ciuUpgradeMiscInfoDescr=_CiuUpgradeMiscInfoDescr_Object((1,3,6,1,4,1,9,9,360,1,1,11,1,3),_CiuUpgradeMiscInfoDescr_Type())
ciuUpgradeMiscInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuUpgradeMiscInfoDescr.setStatus(_B)
_CiscoImageUpgradeMIBConform_ObjectIdentity=ObjectIdentity
ciscoImageUpgradeMIBConform=_CiscoImageUpgradeMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,360,2))
_CiuImageUpgradeCompliances_ObjectIdentity=ObjectIdentity
ciuImageUpgradeCompliances=_CiuImageUpgradeCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,360,2,1))
_CiuImageUpgradeGroups_ObjectIdentity=ObjectIdentity
ciuImageUpgradeGroups=_CiuImageUpgradeGroups_ObjectIdentity((1,3,6,1,4,1,9,9,360,2,2))
ciuImageUpgradeGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,1))
ciuImageUpgradeGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:ciuImageUpgradeGroup.setStatus(_B)
ciuImageVariableGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,2))
ciuImageVariableGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:ciuImageVariableGroup.setStatus(_B)
ciuImageURIGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,3))
ciuImageURIGroup.setObjects((_A,_A3))
if mibBuilder.loadTexts:ciuImageURIGroup.setStatus(_B)
ciuUpgradeOpGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,4))
ciuUpgradeOpGroup.setObjects(*((_A,_d),(_A,_X),(_A,_A4),(_A,_A5),(_A,_e),(_A,_A6),(_A,_f)))
if mibBuilder.loadTexts:ciuUpgradeOpGroup.setStatus(_B)
ciuUpgradeTargetGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,5))
ciuUpgradeTargetGroup.setObjects(*((_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciuUpgradeTargetGroup.setStatus(_B)
ciuImageLocInputGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,6))
ciuImageLocInputGroup.setObjects(*((_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciuImageLocInputGroup.setStatus(_B)
ciuVersionCompChkGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,7))
ciuVersionCompChkGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ciuVersionCompChkGroup.setStatus(_B)
ciuUpgradeImageVersionGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,8))
ciuUpgradeImageVersionGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:ciuUpgradeImageVersionGroup.setStatus(_B)
ciuUpgradeOpStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,9))
ciuUpgradeOpStatusGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciuUpgradeOpStatusGroup.setStatus(_B)
ciuUpgradeMiscGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,11))
ciuUpgradeMiscGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:ciuUpgradeMiscGroup.setStatus(_B)
ciuUpgradeMiscInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,12))
ciuUpgradeMiscInfoGroup.setObjects(*((_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:ciuUpgradeMiscInfoGroup.setStatus(_B)
ciuUpgradeOpNewGroup=ObjectGroup((1,3,6,1,4,1,9,9,360,2,2,14))
ciuUpgradeOpNewGroup.setObjects(*((_A,_AQ),(_A,_n),(_A,_o),(_A,_AR)))
if mibBuilder.loadTexts:ciuUpgradeOpNewGroup.setStatus(_B)
ciuUpgradeOpCompletionNotify=NotificationType((1,3,6,1,4,1,9,9,360,0,1))
ciuUpgradeOpCompletionNotify.setObjects(*((_A,_d),(_A,_X),(_A,_e),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciuUpgradeOpCompletionNotify.setStatus(_B)
ciuUpgradeJobStatusNotify=NotificationType((1,3,6,1,4,1,9,9,360,0,2))
ciuUpgradeJobStatusNotify.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_X),(_A,_f)))
if mibBuilder.loadTexts:ciuUpgradeJobStatusNotify.setStatus(_B)
ciuUpgradeNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,360,2,2,10))
ciuUpgradeNotificationGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:ciuUpgradeNotificationGroup.setStatus(_B)
ciuUpgradeNotificationGroupSup=NotificationGroup((1,3,6,1,4,1,9,9,360,2,2,13))
ciuUpgradeNotificationGroupSup.setObjects((_A,_AT))
if mibBuilder.loadTexts:ciuUpgradeNotificationGroupSup.setStatus(_B)
ciuImageUpgradeCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,360,2,1,1))
ciuImageUpgradeCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciuImageUpgradeCompliance.setStatus(_Y)
ciuImageUpgradeComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,360,2,1,2))
ciuImageUpgradeComplianceRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S)))
if mibBuilder.loadTexts:ciuImageUpgradeComplianceRev1.setStatus(_Y)
ciuImageUpgradeComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,360,2,1,3))
ciuImageUpgradeComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S),(_A,_Z)))
if mibBuilder.loadTexts:ciuImageUpgradeComplianceRev2.setStatus(_Y)
ciuImageUpgradeComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,360,2,1,4))
ciuImageUpgradeComplianceRev3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_p),(_A,_S),(_A,_Z)))
if mibBuilder.loadTexts:ciuImageUpgradeComplianceRev3.setStatus(_Y)
ciuImageUpgradeComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,360,2,1,5))
ciuImageUpgradeComplianceRev4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_p),(_A,_S),(_A,_Z),(_A,_AU)))
if mibBuilder.loadTexts:ciuImageUpgradeComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiuImageVariableTypeName':CiuImageVariableTypeName,'ciscoImageUpgradeMIB':ciscoImageUpgradeMIB,'ciscoImageUpgradeMIBNotifs':ciscoImageUpgradeMIBNotifs,_AS:ciuUpgradeOpCompletionNotify,_AT:ciuUpgradeJobStatusNotify,'ciscoImageUpgradeMIBObjects':ciscoImageUpgradeMIBObjects,'ciscoImageUpgradeConfig':ciscoImageUpgradeConfig,_A2:ciuTotalImageVariables,'ciuImageVariableTable':ciuImageVariableTable,'ciuImageVariableEntry':ciuImageVariableEntry,_Q:ciuImageVariableName,'ciuImageURITable':ciuImageURITable,'ciuImageURIEntry':ciuImageURIEntry,_A3:ciuImageURI,'ciscoImageUpgradeOp':ciscoImageUpgradeOp,_d:ciuUpgradeOpCommand,_X:ciuUpgradeOpStatus,_A4:ciuUpgradeOpNotifyOnCompletion,_A5:ciuUpgradeOpTimeStarted,_e:ciuUpgradeOpTimeCompleted,_A6:ciuUpgradeOpAbort,_f:ciuUpgradeOpStatusReason,_n:ciuUpgradeOpLastCommand,_o:ciuUpgradeOpLastStatus,_AR:ciuUpgradeOpLastStatusReason,_AQ:ciuUpgradeJobStatusNotifyOnCompletion,'ciuUpgradeTargetTable':ciuUpgradeTargetTable,'ciuUpgradeTargetEntry':ciuUpgradeTargetEntry,_A7:ciuUpgradeTargetAction,_A8:ciuUpgradeTargetEntryStatus,'ciuImageLocInputTable':ciuImageLocInputTable,'ciuImageLocInputEntry':ciuImageLocInputEntry,_A9:ciuImageLocInputURI,_AA:ciuImageLocInputEntryStatus,'ciuVersionCompChkTable':ciuVersionCompChkTable,'ciuVersionCompChkEntry':ciuVersionCompChkEntry,_AB:ciuVersionCompImageSame,_AC:ciuVersionCompUpgradable,_AD:ciuVersionCompUpgradeAction,_AE:ciuVersionCompUpgradeBios,_AF:ciuVersionCompUpgradeBootrom,_AG:ciuVersionCompUpgradeLoader,_AH:ciuVersionCompUpgradeImpact,_AI:ciuVersionCompUpgradeReason,'ciuUpgradeImageVersionTable':ciuUpgradeImageVersionTable,'ciuUpgradeImageVersionEntry':ciuUpgradeImageVersionEntry,_z:ciuUpgradeImageVersionIndex,_AJ:ciuUpgradeImageVersionVarName,_AK:ciuUpgradeImageVersionRunning,_AL:ciuUpgradeImageVersionNew,_AM:ciuUpgradeImageVersionUpgReqd,'ciuUpgradeOpStatusTable':ciuUpgradeOpStatusTable,'ciuUpgradeOpStatusEntry':ciuUpgradeOpStatusEntry,_A0:ciuUpgradeOpStatusOperIndex,_g:ciuUpgradeOpStatusOperation,_h:ciuUpgradeOpStatusModule,_i:ciuUpgradeOpStatusSrcImageLoc,_j:ciuUpgradeOpStatusDestImageLoc,_k:ciuUpgradeOpStatusJobStatus,_l:ciuUpgradeOpStatusPercentCompl,_m:ciuUpgradeOpStatusJobStatusReas,'ciscoImageUpgradeMisc':ciscoImageUpgradeMisc,_AN:ciuUpgradeMiscAutoCopy,'ciuUpgradeMiscInfoTable':ciuUpgradeMiscInfoTable,'ciuUpgradeMiscInfoEntry':ciuUpgradeMiscInfoEntry,_A1:ciuUpgradeMiscInfoIndex,_AO:ciuUpgradeMiscInfoModule,_AP:ciuUpgradeMiscInfoDescr,'ciscoImageUpgradeMIBConform':ciscoImageUpgradeMIBConform,'ciuImageUpgradeCompliances':ciuImageUpgradeCompliances,'ciuImageUpgradeCompliance':ciuImageUpgradeCompliance,'ciuImageUpgradeComplianceRev1':ciuImageUpgradeComplianceRev1,'ciuImageUpgradeComplianceRev2':ciuImageUpgradeComplianceRev2,'ciuImageUpgradeComplianceRev3':ciuImageUpgradeComplianceRev3,'ciuImageUpgradeComplianceRev4':ciuImageUpgradeComplianceRev4,'ciuImageUpgradeGroups':ciuImageUpgradeGroups,_F:ciuImageUpgradeGroup,_G:ciuImageVariableGroup,_H:ciuImageURIGroup,_I:ciuUpgradeOpGroup,'ciuUpgradeTargetGroup':ciuUpgradeTargetGroup,_J:ciuImageLocInputGroup,_K:ciuVersionCompChkGroup,_L:ciuUpgradeImageVersionGroup,_M:ciuUpgradeOpStatusGroup,_N:ciuUpgradeNotificationGroup,_S:ciuUpgradeMiscGroup,_Z:ciuUpgradeMiscInfoGroup,_p:ciuUpgradeNotificationGroupSup,_AU:ciuUpgradeOpNewGroup})