_A3='ieee8021CfmConfigErrorListErrorType'
_A2='ieee8021CfmVlanRowStatus'
_A1='ieee8021CfmVlanPrimarySelector'
_A0='ieee8021CfmDefaultMdIdPermission'
_z='ieee8021CfmDefaultMdMhfCreation'
_y='ieee8021CfmDefaultMdLevel'
_x='ieee8021CfmDefaultMdStatus'
_w='ieee8021CfmMaCompNumberOfVids'
_v='ieee8021CfmMaCompRowStatus'
_u='ieee8021CfmMaCompIdPermission'
_t='ieee8021CfmMaCompMhfCreation'
_s='ieee8021CfmMaCompPrimarySelectorOrNone'
_r='ieee8021CfmMaCompPrimarySelectorType'
_q='ieee8021CfmStackMacAddress'
_p='ieee8021CfmStackMepId'
_o='ieee8021CfmStackMaIndex'
_n='ieee8021CfmStackMdIndex'
_m='ieee8021CfmMaComponentId'
_l='ieee8021CfmConfigErrorListIfIndex'
_k='ieee8021CfmConfigErrorListSelector'
_j='ieee8021CfmConfigErrorListSelectorType'
_i='ieee8021CfmVlanSelector'
_h='ieee8021CfmVlanComponentId'
_g='ieee8021CfmDefaultMdPrimarySelector'
_f='ieee8021CfmDefaultMdPrimarySelectorType'
_e='ieee8021CfmDefaultMdComponentId'
_d='ieee8021CfmStackDirection'
_c='ieee8021CfmStackMdLevel'
_b='ieee8021CfmStackServiceSelectorOrNone'
_a='ieee8021CfmStackServiceSelectorType'
_Z='ieee8021CfmStackifIndex'
_Y='ieee8021CfmPbbTeTrafficBitGroup'
_X='ieee8021CfmPbbTeExtensionGroup'
_W='dot1agCfmMdIndex'
_V='dot1agCfmMaIndex'
_U='Dot1agCfmMDLevelOrNone'
_T='ieee8021CfmVlanIdGroup'
_S='ieee8021CfmConfigErrorListGroup'
_R='ieee8021CfmDefaultMdGroup'
_Q='ieee8021CfmMaGroup'
_P='ieee8021CfmStackGroup'
_O='read-write'
_N='ieee8021CfmMaNetGroup'
_M='ieee8021CfmDefaultMdDefGroup'
_L='dot1agCfmNotificationsGroup'
_K='dot1agCfmMepGroup'
_J='dot1agCfmMepDbGroup'
_I='dot1agCfmMdGroup'
_H='Dot1agCfmMhfCreation'
_G='Dot1agCfmIdPermission'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='IEEE8021-CFM-MIB'
_B='IEEE8021-CFM-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmConfigErrors,Dot1agCfmIdPermission,Dot1agCfmMDLevel,Dot1agCfmMDLevelOrNone,Dot1agCfmMepIdOrZero,Dot1agCfmMhfCreation,Dot1agCfmMpDirection,dot1agCfmCompliances,dot1agCfmConfigErrorList,dot1agCfmDefaultMd,dot1agCfmGroups,dot1agCfmMa,dot1agCfmMaIndex,dot1agCfmMaMepListRowStatus,dot1agCfmMaNetRowStatus,dot1agCfmMdGroup,dot1agCfmMdIndex,dot1agCfmMdRowStatus,dot1agCfmMepDbGroup,dot1agCfmMepGroup,dot1agCfmMepLbrBadMsdu,dot1agCfmMepRowStatus,dot1agCfmNotificationsGroup,dot1agCfmStack,dot1agCfmVlan,ieee8021CfmDefaultMdDefGroup,ieee8021CfmMaNetGroup,ieee8021CfmPbbTeExtensionGroup,ieee8021CfmPbbTeTrafficBitGroup=mibBuilder.importSymbols(_C,'Dot1agCfmConfigErrors',_G,'Dot1agCfmMDLevel',_U,'Dot1agCfmMepIdOrZero',_H,'Dot1agCfmMpDirection','dot1agCfmCompliances','dot1agCfmConfigErrorList','dot1agCfmDefaultMd','dot1agCfmGroups','dot1agCfmMa',_V,'dot1agCfmMaMepListRowStatus','dot1agCfmMaNetRowStatus',_I,_W,'dot1agCfmMdRowStatus',_J,_K,'dot1agCfmMepLbrBadMsdu','dot1agCfmMepRowStatus',_L,'dot1agCfmStack','dot1agCfmVlan',_M,_N,_X,_Y)
IEEE8021PbbComponentIdentifier,IEEE8021ServiceSelectorType,IEEE8021ServiceSelectorValue,IEEE8021ServiceSelectorValueOrNone,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier','IEEE8021ServiceSelectorType','IEEE8021ServiceSelectorValue','IEEE8021ServiceSelectorValueOrNone','ieee802dot1mibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ieee8021CfmV2Mib=ModuleIdentity((1,3,111,2,802,1,1,7))
if mibBuilder.loadTexts:ieee8021CfmV2Mib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-02-27 00:00','2008-11-18 00:00','2008-10-15 00:00'))
_Ieee8021CfmStackTable_Object=MibTable
ieee8021CfmStackTable=_Ieee8021CfmStackTable_Object((1,3,111,2,802,1,1,8,1,1,2))
if mibBuilder.loadTexts:ieee8021CfmStackTable.setStatus(_A)
_Ieee8021CfmStackEntry_Object=MibTableRow
ieee8021CfmStackEntry=_Ieee8021CfmStackEntry_Object((1,3,111,2,802,1,1,8,1,1,2,1))
ieee8021CfmStackEntry.setIndexNames((0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:ieee8021CfmStackEntry.setStatus(_A)
_Ieee8021CfmStackifIndex_Type=InterfaceIndex
_Ieee8021CfmStackifIndex_Object=MibTableColumn
ieee8021CfmStackifIndex=_Ieee8021CfmStackifIndex_Object((1,3,111,2,802,1,1,8,1,1,2,1,1),_Ieee8021CfmStackifIndex_Type())
ieee8021CfmStackifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmStackifIndex.setStatus(_A)
_Ieee8021CfmStackServiceSelectorType_Type=IEEE8021ServiceSelectorType
_Ieee8021CfmStackServiceSelectorType_Object=MibTableColumn
ieee8021CfmStackServiceSelectorType=_Ieee8021CfmStackServiceSelectorType_Object((1,3,111,2,802,1,1,8,1,1,2,1,2),_Ieee8021CfmStackServiceSelectorType_Type())
ieee8021CfmStackServiceSelectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmStackServiceSelectorType.setStatus(_A)
_Ieee8021CfmStackServiceSelectorOrNone_Type=IEEE8021ServiceSelectorValueOrNone
_Ieee8021CfmStackServiceSelectorOrNone_Object=MibTableColumn
ieee8021CfmStackServiceSelectorOrNone=_Ieee8021CfmStackServiceSelectorOrNone_Object((1,3,111,2,802,1,1,8,1,1,2,1,3),_Ieee8021CfmStackServiceSelectorOrNone_Type())
ieee8021CfmStackServiceSelectorOrNone.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmStackServiceSelectorOrNone.setStatus(_A)
_Ieee8021CfmStackMdLevel_Type=Dot1agCfmMDLevel
_Ieee8021CfmStackMdLevel_Object=MibTableColumn
ieee8021CfmStackMdLevel=_Ieee8021CfmStackMdLevel_Object((1,3,111,2,802,1,1,8,1,1,2,1,4),_Ieee8021CfmStackMdLevel_Type())
ieee8021CfmStackMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmStackMdLevel.setStatus(_A)
_Ieee8021CfmStackDirection_Type=Dot1agCfmMpDirection
_Ieee8021CfmStackDirection_Object=MibTableColumn
ieee8021CfmStackDirection=_Ieee8021CfmStackDirection_Object((1,3,111,2,802,1,1,8,1,1,2,1,5),_Ieee8021CfmStackDirection_Type())
ieee8021CfmStackDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmStackDirection.setStatus(_A)
_Ieee8021CfmStackMdIndex_Type=Unsigned32
_Ieee8021CfmStackMdIndex_Object=MibTableColumn
ieee8021CfmStackMdIndex=_Ieee8021CfmStackMdIndex_Object((1,3,111,2,802,1,1,8,1,1,2,1,6),_Ieee8021CfmStackMdIndex_Type())
ieee8021CfmStackMdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmStackMdIndex.setStatus(_A)
_Ieee8021CfmStackMaIndex_Type=Unsigned32
_Ieee8021CfmStackMaIndex_Object=MibTableColumn
ieee8021CfmStackMaIndex=_Ieee8021CfmStackMaIndex_Object((1,3,111,2,802,1,1,8,1,1,2,1,7),_Ieee8021CfmStackMaIndex_Type())
ieee8021CfmStackMaIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmStackMaIndex.setStatus(_A)
_Ieee8021CfmStackMepId_Type=Dot1agCfmMepIdOrZero
_Ieee8021CfmStackMepId_Object=MibTableColumn
ieee8021CfmStackMepId=_Ieee8021CfmStackMepId_Object((1,3,111,2,802,1,1,8,1,1,2,1,8),_Ieee8021CfmStackMepId_Type())
ieee8021CfmStackMepId.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmStackMepId.setStatus(_A)
_Ieee8021CfmStackMacAddress_Type=MacAddress
_Ieee8021CfmStackMacAddress_Object=MibTableColumn
ieee8021CfmStackMacAddress=_Ieee8021CfmStackMacAddress_Object((1,3,111,2,802,1,1,8,1,1,2,1,9),_Ieee8021CfmStackMacAddress_Type())
ieee8021CfmStackMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmStackMacAddress.setStatus(_A)
_Ieee8021CfmDefaultMdTable_Object=MibTable
ieee8021CfmDefaultMdTable=_Ieee8021CfmDefaultMdTable_Object((1,3,111,2,802,1,1,8,1,2,5))
if mibBuilder.loadTexts:ieee8021CfmDefaultMdTable.setStatus(_A)
_Ieee8021CfmDefaultMdEntry_Object=MibTableRow
ieee8021CfmDefaultMdEntry=_Ieee8021CfmDefaultMdEntry_Object((1,3,111,2,802,1,1,8,1,2,5,1))
ieee8021CfmDefaultMdEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:ieee8021CfmDefaultMdEntry.setStatus(_A)
_Ieee8021CfmDefaultMdComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CfmDefaultMdComponentId_Object=MibTableColumn
ieee8021CfmDefaultMdComponentId=_Ieee8021CfmDefaultMdComponentId_Object((1,3,111,2,802,1,1,8,1,2,5,1,1),_Ieee8021CfmDefaultMdComponentId_Type())
ieee8021CfmDefaultMdComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdComponentId.setStatus(_A)
_Ieee8021CfmDefaultMdPrimarySelectorType_Type=IEEE8021ServiceSelectorType
_Ieee8021CfmDefaultMdPrimarySelectorType_Object=MibTableColumn
ieee8021CfmDefaultMdPrimarySelectorType=_Ieee8021CfmDefaultMdPrimarySelectorType_Object((1,3,111,2,802,1,1,8,1,2,5,1,2),_Ieee8021CfmDefaultMdPrimarySelectorType_Type())
ieee8021CfmDefaultMdPrimarySelectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdPrimarySelectorType.setStatus(_A)
_Ieee8021CfmDefaultMdPrimarySelector_Type=IEEE8021ServiceSelectorValue
_Ieee8021CfmDefaultMdPrimarySelector_Object=MibTableColumn
ieee8021CfmDefaultMdPrimarySelector=_Ieee8021CfmDefaultMdPrimarySelector_Object((1,3,111,2,802,1,1,8,1,2,5,1,3),_Ieee8021CfmDefaultMdPrimarySelector_Type())
ieee8021CfmDefaultMdPrimarySelector.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdPrimarySelector.setStatus(_A)
_Ieee8021CfmDefaultMdStatus_Type=TruthValue
_Ieee8021CfmDefaultMdStatus_Object=MibTableColumn
ieee8021CfmDefaultMdStatus=_Ieee8021CfmDefaultMdStatus_Object((1,3,111,2,802,1,1,8,1,2,5,1,4),_Ieee8021CfmDefaultMdStatus_Type())
ieee8021CfmDefaultMdStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdStatus.setStatus(_A)
class _Ieee8021CfmDefaultMdLevel_Type(Dot1agCfmMDLevelOrNone):defaultValue=-1
_Ieee8021CfmDefaultMdLevel_Type.__name__=_U
_Ieee8021CfmDefaultMdLevel_Object=MibTableColumn
ieee8021CfmDefaultMdLevel=_Ieee8021CfmDefaultMdLevel_Object((1,3,111,2,802,1,1,8,1,2,5,1,5),_Ieee8021CfmDefaultMdLevel_Type())
ieee8021CfmDefaultMdLevel.setMaxAccess(_O)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdLevel.setStatus(_A)
class _Ieee8021CfmDefaultMdMhfCreation_Type(Dot1agCfmMhfCreation):defaultValue=4
_Ieee8021CfmDefaultMdMhfCreation_Type.__name__=_H
_Ieee8021CfmDefaultMdMhfCreation_Object=MibTableColumn
ieee8021CfmDefaultMdMhfCreation=_Ieee8021CfmDefaultMdMhfCreation_Object((1,3,111,2,802,1,1,8,1,2,5,1,6),_Ieee8021CfmDefaultMdMhfCreation_Type())
ieee8021CfmDefaultMdMhfCreation.setMaxAccess(_O)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdMhfCreation.setStatus(_A)
class _Ieee8021CfmDefaultMdIdPermission_Type(Dot1agCfmIdPermission):defaultValue=5
_Ieee8021CfmDefaultMdIdPermission_Type.__name__=_G
_Ieee8021CfmDefaultMdIdPermission_Object=MibTableColumn
ieee8021CfmDefaultMdIdPermission=_Ieee8021CfmDefaultMdIdPermission_Object((1,3,111,2,802,1,1,8,1,2,5,1,7),_Ieee8021CfmDefaultMdIdPermission_Type())
ieee8021CfmDefaultMdIdPermission.setMaxAccess(_O)
if mibBuilder.loadTexts:ieee8021CfmDefaultMdIdPermission.setStatus(_A)
_Ieee8021CfmVlanTable_Object=MibTable
ieee8021CfmVlanTable=_Ieee8021CfmVlanTable_Object((1,3,111,2,802,1,1,8,1,3,2))
if mibBuilder.loadTexts:ieee8021CfmVlanTable.setStatus(_A)
_Ieee8021CfmVlanEntry_Object=MibTableRow
ieee8021CfmVlanEntry=_Ieee8021CfmVlanEntry_Object((1,3,111,2,802,1,1,8,1,3,2,1))
ieee8021CfmVlanEntry.setIndexNames((0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:ieee8021CfmVlanEntry.setStatus(_A)
_Ieee8021CfmVlanComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CfmVlanComponentId_Object=MibTableColumn
ieee8021CfmVlanComponentId=_Ieee8021CfmVlanComponentId_Object((1,3,111,2,802,1,1,8,1,3,2,1,1),_Ieee8021CfmVlanComponentId_Type())
ieee8021CfmVlanComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmVlanComponentId.setStatus(_A)
_Ieee8021CfmVlanSelector_Type=IEEE8021ServiceSelectorValue
_Ieee8021CfmVlanSelector_Object=MibTableColumn
ieee8021CfmVlanSelector=_Ieee8021CfmVlanSelector_Object((1,3,111,2,802,1,1,8,1,3,2,1,3),_Ieee8021CfmVlanSelector_Type())
ieee8021CfmVlanSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmVlanSelector.setStatus(_A)
_Ieee8021CfmVlanPrimarySelector_Type=IEEE8021ServiceSelectorValue
_Ieee8021CfmVlanPrimarySelector_Object=MibTableColumn
ieee8021CfmVlanPrimarySelector=_Ieee8021CfmVlanPrimarySelector_Object((1,3,111,2,802,1,1,8,1,3,2,1,5),_Ieee8021CfmVlanPrimarySelector_Type())
ieee8021CfmVlanPrimarySelector.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmVlanPrimarySelector.setStatus(_A)
_Ieee8021CfmVlanRowStatus_Type=RowStatus
_Ieee8021CfmVlanRowStatus_Object=MibTableColumn
ieee8021CfmVlanRowStatus=_Ieee8021CfmVlanRowStatus_Object((1,3,111,2,802,1,1,8,1,3,2,1,6),_Ieee8021CfmVlanRowStatus_Type())
ieee8021CfmVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmVlanRowStatus.setStatus(_A)
_Ieee8021CfmConfigErrorListTable_Object=MibTable
ieee8021CfmConfigErrorListTable=_Ieee8021CfmConfigErrorListTable_Object((1,3,111,2,802,1,1,8,1,4,2))
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListTable.setStatus(_A)
_Ieee8021CfmConfigErrorListEntry_Object=MibTableRow
ieee8021CfmConfigErrorListEntry=_Ieee8021CfmConfigErrorListEntry_Object((1,3,111,2,802,1,1,8,1,4,2,1))
ieee8021CfmConfigErrorListEntry.setIndexNames((0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListEntry.setStatus(_A)
_Ieee8021CfmConfigErrorListSelectorType_Type=IEEE8021ServiceSelectorType
_Ieee8021CfmConfigErrorListSelectorType_Object=MibTableColumn
ieee8021CfmConfigErrorListSelectorType=_Ieee8021CfmConfigErrorListSelectorType_Object((1,3,111,2,802,1,1,8,1,4,2,1,1),_Ieee8021CfmConfigErrorListSelectorType_Type())
ieee8021CfmConfigErrorListSelectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListSelectorType.setStatus(_A)
_Ieee8021CfmConfigErrorListSelector_Type=IEEE8021ServiceSelectorValue
_Ieee8021CfmConfigErrorListSelector_Object=MibTableColumn
ieee8021CfmConfigErrorListSelector=_Ieee8021CfmConfigErrorListSelector_Object((1,3,111,2,802,1,1,8,1,4,2,1,2),_Ieee8021CfmConfigErrorListSelector_Type())
ieee8021CfmConfigErrorListSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListSelector.setStatus(_A)
_Ieee8021CfmConfigErrorListIfIndex_Type=InterfaceIndex
_Ieee8021CfmConfigErrorListIfIndex_Object=MibTableColumn
ieee8021CfmConfigErrorListIfIndex=_Ieee8021CfmConfigErrorListIfIndex_Object((1,3,111,2,802,1,1,8,1,4,2,1,3),_Ieee8021CfmConfigErrorListIfIndex_Type())
ieee8021CfmConfigErrorListIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListIfIndex.setStatus(_A)
_Ieee8021CfmConfigErrorListErrorType_Type=Dot1agCfmConfigErrors
_Ieee8021CfmConfigErrorListErrorType_Object=MibTableColumn
ieee8021CfmConfigErrorListErrorType=_Ieee8021CfmConfigErrorListErrorType_Object((1,3,111,2,802,1,1,8,1,4,2,1,4),_Ieee8021CfmConfigErrorListErrorType_Type())
ieee8021CfmConfigErrorListErrorType.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListErrorType.setStatus(_A)
_Ieee8021CfmMaCompTable_Object=MibTable
ieee8021CfmMaCompTable=_Ieee8021CfmMaCompTable_Object((1,3,111,2,802,1,1,8,1,6,4))
if mibBuilder.loadTexts:ieee8021CfmMaCompTable.setStatus(_A)
_Ieee8021CfmMaCompEntry_Object=MibTableRow
ieee8021CfmMaCompEntry=_Ieee8021CfmMaCompEntry_Object((1,3,111,2,802,1,1,8,1,6,4,1))
ieee8021CfmMaCompEntry.setIndexNames((0,_B,_m),(0,_C,_W),(0,_C,_V))
if mibBuilder.loadTexts:ieee8021CfmMaCompEntry.setStatus(_A)
_Ieee8021CfmMaComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021CfmMaComponentId_Object=MibTableColumn
ieee8021CfmMaComponentId=_Ieee8021CfmMaComponentId_Object((1,3,111,2,802,1,1,8,1,6,4,1,1),_Ieee8021CfmMaComponentId_Type())
ieee8021CfmMaComponentId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021CfmMaComponentId.setStatus(_A)
_Ieee8021CfmMaCompPrimarySelectorType_Type=IEEE8021ServiceSelectorType
_Ieee8021CfmMaCompPrimarySelectorType_Object=MibTableColumn
ieee8021CfmMaCompPrimarySelectorType=_Ieee8021CfmMaCompPrimarySelectorType_Object((1,3,111,2,802,1,1,8,1,6,4,1,2),_Ieee8021CfmMaCompPrimarySelectorType_Type())
ieee8021CfmMaCompPrimarySelectorType.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompPrimarySelectorType.setStatus(_A)
_Ieee8021CfmMaCompPrimarySelectorOrNone_Type=IEEE8021ServiceSelectorValueOrNone
_Ieee8021CfmMaCompPrimarySelectorOrNone_Object=MibTableColumn
ieee8021CfmMaCompPrimarySelectorOrNone=_Ieee8021CfmMaCompPrimarySelectorOrNone_Object((1,3,111,2,802,1,1,8,1,6,4,1,3),_Ieee8021CfmMaCompPrimarySelectorOrNone_Type())
ieee8021CfmMaCompPrimarySelectorOrNone.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompPrimarySelectorOrNone.setStatus(_A)
class _Ieee8021CfmMaCompMhfCreation_Type(Dot1agCfmMhfCreation):defaultValue=4
_Ieee8021CfmMaCompMhfCreation_Type.__name__=_H
_Ieee8021CfmMaCompMhfCreation_Object=MibTableColumn
ieee8021CfmMaCompMhfCreation=_Ieee8021CfmMaCompMhfCreation_Object((1,3,111,2,802,1,1,8,1,6,4,1,4),_Ieee8021CfmMaCompMhfCreation_Type())
ieee8021CfmMaCompMhfCreation.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompMhfCreation.setStatus(_A)
class _Ieee8021CfmMaCompIdPermission_Type(Dot1agCfmIdPermission):defaultValue=5
_Ieee8021CfmMaCompIdPermission_Type.__name__=_G
_Ieee8021CfmMaCompIdPermission_Object=MibTableColumn
ieee8021CfmMaCompIdPermission=_Ieee8021CfmMaCompIdPermission_Object((1,3,111,2,802,1,1,8,1,6,4,1,5),_Ieee8021CfmMaCompIdPermission_Type())
ieee8021CfmMaCompIdPermission.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompIdPermission.setStatus(_A)
_Ieee8021CfmMaCompNumberOfVids_Type=Unsigned32
_Ieee8021CfmMaCompNumberOfVids_Object=MibTableColumn
ieee8021CfmMaCompNumberOfVids=_Ieee8021CfmMaCompNumberOfVids_Object((1,3,111,2,802,1,1,8,1,6,4,1,6),_Ieee8021CfmMaCompNumberOfVids_Type())
ieee8021CfmMaCompNumberOfVids.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompNumberOfVids.setStatus(_A)
_Ieee8021CfmMaCompRowStatus_Type=RowStatus
_Ieee8021CfmMaCompRowStatus_Object=MibTableColumn
ieee8021CfmMaCompRowStatus=_Ieee8021CfmMaCompRowStatus_Object((1,3,111,2,802,1,1,8,1,6,4,1,7),_Ieee8021CfmMaCompRowStatus_Type())
ieee8021CfmMaCompRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021CfmMaCompRowStatus.setStatus(_A)
ieee8021CfmStackGroup=ObjectGroup((1,3,111,2,802,1,1,8,2,2,12))
ieee8021CfmStackGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ieee8021CfmStackGroup.setStatus(_A)
ieee8021CfmMaGroup=ObjectGroup((1,3,111,2,802,1,1,8,2,2,13))
ieee8021CfmMaGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ieee8021CfmMaGroup.setStatus(_A)
ieee8021CfmDefaultMdGroup=ObjectGroup((1,3,111,2,802,1,1,8,2,2,14))
ieee8021CfmDefaultMdGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ieee8021CfmDefaultMdGroup.setStatus(_A)
ieee8021CfmVlanIdGroup=ObjectGroup((1,3,111,2,802,1,1,8,2,2,15))
ieee8021CfmVlanIdGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ieee8021CfmVlanIdGroup.setStatus(_A)
ieee8021CfmConfigErrorListGroup=ObjectGroup((1,3,111,2,802,1,1,8,2,2,16))
ieee8021CfmConfigErrorListGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:ieee8021CfmConfigErrorListGroup.setStatus(_A)
ieee8021CfmComplianceV2=ModuleCompliance((1,3,111,2,802,1,1,8,2,1,2))
ieee8021CfmComplianceV2.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_C,_I),(_C,_K),(_C,_J),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:ieee8021CfmComplianceV2.setStatus(_A)
dot1agCfmWithPbbTeCompliance=ModuleCompliance((1,3,111,2,802,1,1,8,2,1,3))
dot1agCfmWithPbbTeCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_C,_I),(_C,_K),(_C,_J),(_C,_L),(_C,_M),(_C,_N),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:dot1agCfmWithPbbTeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021CfmV2Mib':ieee8021CfmV2Mib,'ieee8021CfmStackTable':ieee8021CfmStackTable,'ieee8021CfmStackEntry':ieee8021CfmStackEntry,_Z:ieee8021CfmStackifIndex,_a:ieee8021CfmStackServiceSelectorType,_b:ieee8021CfmStackServiceSelectorOrNone,_c:ieee8021CfmStackMdLevel,_d:ieee8021CfmStackDirection,_n:ieee8021CfmStackMdIndex,_o:ieee8021CfmStackMaIndex,_p:ieee8021CfmStackMepId,_q:ieee8021CfmStackMacAddress,'ieee8021CfmDefaultMdTable':ieee8021CfmDefaultMdTable,'ieee8021CfmDefaultMdEntry':ieee8021CfmDefaultMdEntry,_e:ieee8021CfmDefaultMdComponentId,_f:ieee8021CfmDefaultMdPrimarySelectorType,_g:ieee8021CfmDefaultMdPrimarySelector,_x:ieee8021CfmDefaultMdStatus,_y:ieee8021CfmDefaultMdLevel,_z:ieee8021CfmDefaultMdMhfCreation,_A0:ieee8021CfmDefaultMdIdPermission,'ieee8021CfmVlanTable':ieee8021CfmVlanTable,'ieee8021CfmVlanEntry':ieee8021CfmVlanEntry,_h:ieee8021CfmVlanComponentId,_i:ieee8021CfmVlanSelector,_A1:ieee8021CfmVlanPrimarySelector,_A2:ieee8021CfmVlanRowStatus,'ieee8021CfmConfigErrorListTable':ieee8021CfmConfigErrorListTable,'ieee8021CfmConfigErrorListEntry':ieee8021CfmConfigErrorListEntry,_j:ieee8021CfmConfigErrorListSelectorType,_k:ieee8021CfmConfigErrorListSelector,_l:ieee8021CfmConfigErrorListIfIndex,_A3:ieee8021CfmConfigErrorListErrorType,'ieee8021CfmMaCompTable':ieee8021CfmMaCompTable,'ieee8021CfmMaCompEntry':ieee8021CfmMaCompEntry,_m:ieee8021CfmMaComponentId,_r:ieee8021CfmMaCompPrimarySelectorType,_s:ieee8021CfmMaCompPrimarySelectorOrNone,_t:ieee8021CfmMaCompMhfCreation,_u:ieee8021CfmMaCompIdPermission,_w:ieee8021CfmMaCompNumberOfVids,_v:ieee8021CfmMaCompRowStatus,'ieee8021CfmComplianceV2':ieee8021CfmComplianceV2,'dot1agCfmWithPbbTeCompliance':dot1agCfmWithPbbTeCompliance,_P:ieee8021CfmStackGroup,_Q:ieee8021CfmMaGroup,_R:ieee8021CfmDefaultMdGroup,_T:ieee8021CfmVlanIdGroup,_S:ieee8021CfmConfigErrorListGroup})