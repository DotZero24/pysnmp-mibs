_r='vRtrMplsTpTunnelNextHopAddress'
_q='vRtrMplsTpTunnelNextHopAddrType'
_p='vRtrMplsTpTunnelID'
_o='vRtrMplsTpTunnelType'
_n='vRtrMplsTpTunnelPreference'
_m='vRtrMplsTpTunnelGlobalId'
_l='vRtrMplsTpTunnelNodeId'
_k='vRtrMplsTpLsrPathIdLspNumber'
_j='vRtrMplsTpLsrPathIdDestTunNum'
_i='vRtrMplsTpLsrPathIdDestNodeId'
_h='vRtrMplsTpLsrPathIdDestGlobalId'
_g='vRtrMplsTpLsrPathIdSrcTunNum'
_f='vRtrMplsTpLsrPathIdSrcNodeId'
_e='vRtrMplsTpLsrPathIdSrcGlobalId'
_d='vRtrMplsTpLsrPathName'
_c='unknown'
_b='vRtrMplsTpPtcTmplName'
_a='vRtrMplsTpOamTmplName'
_Z='vRtrMplsTpNodeId'
_Y='TmnxMplsTpNodeID'
_X='TmnxMplsTpGlobalID'
_W='seconds'
_V='centiseconds'
_U='TNamedItemOrEmpty'
_T='TruthValue'
_S='vRtrMplsTpLspPathIndex'
_R='Bits'
_Q='InetAddressType'
_P='InterfaceIndexOrZero'
_O='TmnxAdminState'
_N='vRtrMplsLspIndex'
_M='TN-MPLS-MIB'
_L='InetAddress'
_K='Integer32'
_J='tnSysSwitchId'
_I='TROPIC-SYSTEM-MIB'
_H='vRtrID'
_G='TN-VRTR-MIB'
_F='not-accessible'
_E='Unsigned32'
_D='TN-MPLS-TP-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_P)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp',_T)
vRtrMplsLspIndex,=mibBuilder.importSymbols(_M,_N)
TNamedItem,TNamedItemOrEmpty,TmnxAdminState,TmnxMplsTpGlobalID,TmnxMplsTpNodeID,TmnxMplsTpTunnelType,TmnxOperState,TmnxTunnelID=mibBuilder.importSymbols('TN-TC-MIB','TNamedItem',_U,_O,_X,_Y,'TmnxMplsTpTunnelType','TmnxOperState','TmnxTunnelID')
vRtrID,=mibBuilder.importSymbols(_G,_H)
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_I,_J)
tnMplsTpMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,83))
if mibBuilder.loadTexts:tnMplsTpMIBModule.setRevisions(('2015-09-30 00:00','2015-04-30 00:00','2012-06-01 00:00'))
class VRtrMplsTpLspPathMepPduType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_VRtrMplsTpObjs_ObjectIdentity=ObjectIdentity
vRtrMplsTpObjs=_VRtrMplsTpObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83))
_VRtrMplsTpConfigTimeStamps_ObjectIdentity=ObjectIdentity
vRtrMplsTpConfigTimeStamps=_VRtrMplsTpConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,1))
_VRtrMplsTpSystemTableLastChanged_Type=TimeStamp
_VRtrMplsTpSystemTableLastChanged_Object=MibScalar
vRtrMplsTpSystemTableLastChanged=_VRtrMplsTpSystemTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,83,1,1),_VRtrMplsTpSystemTableLastChanged_Type())
vRtrMplsTpSystemTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpSystemTableLastChanged.setStatus(_A)
_VRtrMplsTpOamTemplTblLastChanged_Type=TimeStamp
_VRtrMplsTpOamTemplTblLastChanged_Object=MibScalar
vRtrMplsTpOamTemplTblLastChanged=_VRtrMplsTpOamTemplTblLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,83,1,2),_VRtrMplsTpOamTemplTblLastChanged_Type())
vRtrMplsTpOamTemplTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpOamTemplTblLastChanged.setStatus(_A)
_VRtrMplsTpPtcTemplTblLastChanged_Type=TimeStamp
_VRtrMplsTpPtcTemplTblLastChanged_Object=MibScalar
vRtrMplsTpPtcTemplTblLastChanged=_VRtrMplsTpPtcTemplTblLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,83,1,3),_VRtrMplsTpPtcTemplTblLastChanged_Type())
vRtrMplsTpPtcTemplTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpPtcTemplTblLastChanged.setStatus(_A)
_VRtrMplsTpLspPathTblLastChanged_Type=TimeStamp
_VRtrMplsTpLspPathTblLastChanged_Object=MibScalar
vRtrMplsTpLspPathTblLastChanged=_VRtrMplsTpLspPathTblLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,83,1,5),_VRtrMplsTpLspPathTblLastChanged_Type())
vRtrMplsTpLspPathTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathTblLastChanged.setStatus(_A)
_VRtrMplsTpLspPathMepTblLastChg_Type=TimeStamp
_VRtrMplsTpLspPathMepTblLastChg_Object=MibScalar
vRtrMplsTpLspPathMepTblLastChg=_VRtrMplsTpLspPathMepTblLastChg_Object((1,3,6,1,4,1,7483,6,1,2,83,1,6),_VRtrMplsTpLspPathMepTblLastChg_Type())
vRtrMplsTpLspPathMepTblLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepTblLastChg.setStatus(_A)
_VRtrMplsTpLsrTblLastChanged_Type=TimeStamp
_VRtrMplsTpLsrTblLastChanged_Object=MibScalar
vRtrMplsTpLsrTblLastChanged=_VRtrMplsTpLsrTblLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,83,1,7),_VRtrMplsTpLsrTblLastChanged_Type())
vRtrMplsTpLsrTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLsrTblLastChanged.setStatus(_A)
_VRtrMplsTpLsrPathIdTblLastChg_Type=TimeStamp
_VRtrMplsTpLsrPathIdTblLastChg_Object=MibScalar
vRtrMplsTpLsrPathIdTblLastChg=_VRtrMplsTpLsrPathIdTblLastChg_Object((1,3,6,1,4,1,7483,6,1,2,83,1,8),_VRtrMplsTpLsrPathIdTblLastChg_Type())
vRtrMplsTpLsrPathIdTblLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdTblLastChg.setStatus(_A)
_VRtrMplsTpScalar1_Type=Unsigned32
_VRtrMplsTpScalar1_Object=MibScalar
vRtrMplsTpScalar1=_VRtrMplsTpScalar1_Object((1,3,6,1,4,1,7483,6,1,2,83,1,101),_VRtrMplsTpScalar1_Type())
vRtrMplsTpScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpScalar1.setStatus(_A)
_VRtrMplsTpScalar2_Type=Unsigned32
_VRtrMplsTpScalar2_Object=MibScalar
vRtrMplsTpScalar2=_VRtrMplsTpScalar2_Object((1,3,6,1,4,1,7483,6,1,2,83,1,102),_VRtrMplsTpScalar2_Type())
vRtrMplsTpScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpScalar2.setStatus(_A)
_VRtrMplsTpConfigurations_ObjectIdentity=ObjectIdentity
vRtrMplsTpConfigurations=_VRtrMplsTpConfigurations_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2))
_VRtrMplsTpSystemIdentifiers_ObjectIdentity=ObjectIdentity
vRtrMplsTpSystemIdentifiers=_VRtrMplsTpSystemIdentifiers_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2,1))
_VRtrMplsTpSystemTable_Object=MibTable
vRtrMplsTpSystemTable=_VRtrMplsTpSystemTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1))
if mibBuilder.loadTexts:vRtrMplsTpSystemTable.setStatus(_A)
_VRtrMplsTpSystemEntry_Object=MibTableRow
vRtrMplsTpSystemEntry=_VRtrMplsTpSystemEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1))
vRtrMplsTpSystemEntry.setIndexNames((0,_I,_J),(0,_G,_H))
if mibBuilder.loadTexts:vRtrMplsTpSystemEntry.setStatus(_A)
_VRtrMplsTpRowStatus_Type=RowStatus
_VRtrMplsTpRowStatus_Object=MibTableColumn
vRtrMplsTpRowStatus=_VRtrMplsTpRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,1),_VRtrMplsTpRowStatus_Type())
vRtrMplsTpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpRowStatus.setStatus(_A)
class _VRtrMplsTpGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_VRtrMplsTpGlobalId_Type.__name__=_X
_VRtrMplsTpGlobalId_Object=MibTableColumn
vRtrMplsTpGlobalId=_VRtrMplsTpGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,2),_VRtrMplsTpGlobalId_Type())
vRtrMplsTpGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpGlobalId.setStatus(_A)
class _VRtrMplsTpNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_VRtrMplsTpNodeId_Type.__name__=_Y
_VRtrMplsTpNodeId_Object=MibTableColumn
vRtrMplsTpNodeId=_VRtrMplsTpNodeId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,3),_VRtrMplsTpNodeId_Type())
vRtrMplsTpNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpNodeId.setStatus(_A)
class _VRtrMplsTpTunnelIdMin_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,61440))
_VRtrMplsTpTunnelIdMin_Type.__name__=_E
_VRtrMplsTpTunnelIdMin_Object=MibTableColumn
vRtrMplsTpTunnelIdMin=_VRtrMplsTpTunnelIdMin_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,4),_VRtrMplsTpTunnelIdMin_Type())
vRtrMplsTpTunnelIdMin.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpTunnelIdMin.setStatus(_A)
class _VRtrMplsTpTunnelIdMax_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,61440))
_VRtrMplsTpTunnelIdMax_Type.__name__=_E
_VRtrMplsTpTunnelIdMax_Object=MibTableColumn
vRtrMplsTpTunnelIdMax=_VRtrMplsTpTunnelIdMax_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,5),_VRtrMplsTpTunnelIdMax_Type())
vRtrMplsTpTunnelIdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpTunnelIdMax.setStatus(_A)
class _VRtrMplsTpAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsTpAdminState_Type.__name__=_O
_VRtrMplsTpAdminState_Object=MibTableColumn
vRtrMplsTpAdminState=_VRtrMplsTpAdminState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,6),_VRtrMplsTpAdminState_Type())
vRtrMplsTpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpAdminState.setStatus(_A)
class _VRtrMplsTpInheritance_Type(Bits):defaultBinValue='0';namedValues=NamedValues((_Z,0))
_VRtrMplsTpInheritance_Type.__name__=_R
_VRtrMplsTpInheritance_Object=MibTableColumn
vRtrMplsTpInheritance=_VRtrMplsTpInheritance_Object((1,3,6,1,4,1,7483,6,1,2,83,2,1,1,1,7),_VRtrMplsTpInheritance_Type())
vRtrMplsTpInheritance.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpInheritance.setStatus(_A)
_VRtrMplsTpTemplateObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpTemplateObjects=_VRtrMplsTpTemplateObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2,2))
_VRtrMplsTpOamTemplateCfgTable_Object=MibTable
vRtrMplsTpOamTemplateCfgTable=_VRtrMplsTpOamTemplateCfgTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1))
if mibBuilder.loadTexts:vRtrMplsTpOamTemplateCfgTable.setStatus(_A)
_VRtrMplsTpOamTemplateCfgEntry_Object=MibTableRow
vRtrMplsTpOamTemplateCfgEntry=_VRtrMplsTpOamTemplateCfgEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1))
vRtrMplsTpOamTemplateCfgEntry.setIndexNames((0,_I,_J),(0,_G,_H),(1,_D,_a))
if mibBuilder.loadTexts:vRtrMplsTpOamTemplateCfgEntry.setStatus(_A)
_VRtrMplsTpOamTmplName_Type=TNamedItem
_VRtrMplsTpOamTmplName_Object=MibTableColumn
vRtrMplsTpOamTmplName=_VRtrMplsTpOamTmplName_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,1),_VRtrMplsTpOamTmplName_Type())
vRtrMplsTpOamTmplName.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplName.setStatus(_A)
_VRtrMplsTpOamTmplRowStatus_Type=RowStatus
_VRtrMplsTpOamTmplRowStatus_Object=MibTableColumn
vRtrMplsTpOamTmplRowStatus=_VRtrMplsTpOamTmplRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,2),_VRtrMplsTpOamTmplRowStatus_Type())
vRtrMplsTpOamTmplRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplRowStatus.setStatus(_A)
_VRtrMplsTpOamTmplLastChangedTime_Type=TimeStamp
_VRtrMplsTpOamTmplLastChangedTime_Object=MibTableColumn
vRtrMplsTpOamTmplLastChangedTime=_VRtrMplsTpOamTmplLastChangedTime_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,3),_VRtrMplsTpOamTmplLastChangedTime_Type())
vRtrMplsTpOamTmplLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplLastChangedTime.setStatus(_A)
_VRtrMplsTpOamTmplBfdTemplateName_Type=TNamedItemOrEmpty
_VRtrMplsTpOamTmplBfdTemplateName_Object=MibTableColumn
vRtrMplsTpOamTmplBfdTemplateName=_VRtrMplsTpOamTmplBfdTemplateName_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,4),_VRtrMplsTpOamTmplBfdTemplateName_Type())
vRtrMplsTpOamTmplBfdTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplBfdTemplateName.setStatus(_A)
class _VRtrMplsTpOamTmplHoldTimeDown_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_VRtrMplsTpOamTmplHoldTimeDown_Type.__name__=_E
_VRtrMplsTpOamTmplHoldTimeDown_Object=MibTableColumn
vRtrMplsTpOamTmplHoldTimeDown=_VRtrMplsTpOamTmplHoldTimeDown_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,5),_VRtrMplsTpOamTmplHoldTimeDown_Type())
vRtrMplsTpOamTmplHoldTimeDown.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplHoldTimeDown.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplHoldTimeDown.setUnits(_V)
class _VRtrMplsTpOamTmplHoldTimeUp_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_VRtrMplsTpOamTmplHoldTimeUp_Type.__name__=_E
_VRtrMplsTpOamTmplHoldTimeUp_Object=MibTableColumn
vRtrMplsTpOamTmplHoldTimeUp=_VRtrMplsTpOamTmplHoldTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,1,1,6),_VRtrMplsTpOamTmplHoldTimeUp_Type())
vRtrMplsTpOamTmplHoldTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplHoldTimeUp.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpOamTmplHoldTimeUp.setUnits('deciseconds')
_VRtrMplsTpPtcTemplateCfgTable_Object=MibTable
vRtrMplsTpPtcTemplateCfgTable=_VRtrMplsTpPtcTemplateCfgTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2))
if mibBuilder.loadTexts:vRtrMplsTpPtcTemplateCfgTable.setStatus(_A)
_VRtrMplsTpPtcTemplateCfgEntry_Object=MibTableRow
vRtrMplsTpPtcTemplateCfgEntry=_VRtrMplsTpPtcTemplateCfgEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1))
vRtrMplsTpPtcTemplateCfgEntry.setIndexNames((0,_I,_J),(0,_G,_H),(1,_D,_b))
if mibBuilder.loadTexts:vRtrMplsTpPtcTemplateCfgEntry.setStatus(_A)
_VRtrMplsTpPtcTmplName_Type=TNamedItem
_VRtrMplsTpPtcTmplName_Object=MibTableColumn
vRtrMplsTpPtcTmplName=_VRtrMplsTpPtcTmplName_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,1),_VRtrMplsTpPtcTmplName_Type())
vRtrMplsTpPtcTmplName.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplName.setStatus(_A)
_VRtrMplsTpPtcTmplRowStatus_Type=RowStatus
_VRtrMplsTpPtcTmplRowStatus_Object=MibTableColumn
vRtrMplsTpPtcTmplRowStatus=_VRtrMplsTpPtcTmplRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,2),_VRtrMplsTpPtcTmplRowStatus_Type())
vRtrMplsTpPtcTmplRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplRowStatus.setStatus(_A)
_VRtrMplsTpPtcTmplLastChangedTime_Type=TimeStamp
_VRtrMplsTpPtcTmplLastChangedTime_Object=MibTableColumn
vRtrMplsTpPtcTmplLastChangedTime=_VRtrMplsTpPtcTmplLastChangedTime_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,3),_VRtrMplsTpPtcTmplLastChangedTime_Type())
vRtrMplsTpPtcTmplLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplLastChangedTime.setStatus(_A)
class _VRtrMplsTpPtcTmplProtectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('one2one',1))
_VRtrMplsTpPtcTmplProtectionMode_Type.__name__=_K
_VRtrMplsTpPtcTmplProtectionMode_Object=MibTableColumn
vRtrMplsTpPtcTmplProtectionMode=_VRtrMplsTpPtcTmplProtectionMode_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,4),_VRtrMplsTpPtcTmplProtectionMode_Type())
vRtrMplsTpPtcTmplProtectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplProtectionMode.setStatus(_A)
class _VRtrMplsTpPtcTmplProtectionDir_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('bidirectional',2))
_VRtrMplsTpPtcTmplProtectionDir_Type.__name__=_K
_VRtrMplsTpPtcTmplProtectionDir_Object=MibTableColumn
vRtrMplsTpPtcTmplProtectionDir=_VRtrMplsTpPtcTmplProtectionDir_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,5),_VRtrMplsTpPtcTmplProtectionDir_Type())
vRtrMplsTpPtcTmplProtectionDir.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplProtectionDir.setStatus(_A)
class _VRtrMplsTpPtcTmplRevertive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRevertive',1),('revertive',2)))
_VRtrMplsTpPtcTmplRevertive_Type.__name__=_K
_VRtrMplsTpPtcTmplRevertive_Object=MibTableColumn
vRtrMplsTpPtcTmplRevertive=_VRtrMplsTpPtcTmplRevertive_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,6),_VRtrMplsTpPtcTmplRevertive_Type())
vRtrMplsTpPtcTmplRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplRevertive.setStatus(_A)
class _VRtrMplsTpPtcTmplWaitToRestore_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_VRtrMplsTpPtcTmplWaitToRestore_Type.__name__=_E
_VRtrMplsTpPtcTmplWaitToRestore_Object=MibTableColumn
vRtrMplsTpPtcTmplWaitToRestore=_VRtrMplsTpPtcTmplWaitToRestore_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,7),_VRtrMplsTpPtcTmplWaitToRestore_Type())
vRtrMplsTpPtcTmplWaitToRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplWaitToRestore.setUnits(_W)
class _VRtrMplsTpPtcTmplRapidPscTimer_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,3),ValueRangeConstraint(10,10),ValueRangeConstraint(100,100),ValueRangeConstraint(1000,1000))
_VRtrMplsTpPtcTmplRapidPscTimer_Type.__name__=_E
_VRtrMplsTpPtcTmplRapidPscTimer_Object=MibTableColumn
vRtrMplsTpPtcTmplRapidPscTimer=_VRtrMplsTpPtcTmplRapidPscTimer_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,8),_VRtrMplsTpPtcTmplRapidPscTimer_Type())
vRtrMplsTpPtcTmplRapidPscTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplRapidPscTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplRapidPscTimer.setUnits('milliseconds')
class _VRtrMplsTpPtcTmplSlowPscTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_VRtrMplsTpPtcTmplSlowPscTimer_Type.__name__=_E
_VRtrMplsTpPtcTmplSlowPscTimer_Object=MibTableColumn
vRtrMplsTpPtcTmplSlowPscTimer=_VRtrMplsTpPtcTmplSlowPscTimer_Object((1,3,6,1,4,1,7483,6,1,2,83,2,2,2,1,9),_VRtrMplsTpPtcTmplSlowPscTimer_Type())
vRtrMplsTpPtcTmplSlowPscTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplSlowPscTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpPtcTmplSlowPscTimer.setUnits(_W)
_VRtrMplsTpLspObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpLspObjects=_VRtrMplsTpLspObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2,3))
_VRtrMplsTpLspPathTable_Object=MibTable
vRtrMplsTpLspPathTable=_VRtrMplsTpLspPathTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2))
if mibBuilder.loadTexts:vRtrMplsTpLspPathTable.setStatus(_A)
_VRtrMplsTpLspPathEntry_Object=MibTableRow
vRtrMplsTpLspPathEntry=_VRtrMplsTpLspPathEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1))
vRtrMplsTpLspPathEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_M,_N),(0,_D,_S))
if mibBuilder.loadTexts:vRtrMplsTpLspPathEntry.setStatus(_A)
class _VRtrMplsTpLspPathIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('working',1),('protecting',2)))
_VRtrMplsTpLspPathIndex_Type.__name__=_K
_VRtrMplsTpLspPathIndex_Object=MibTableColumn
vRtrMplsTpLspPathIndex=_VRtrMplsTpLspPathIndex_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,1),_VRtrMplsTpLspPathIndex_Type())
vRtrMplsTpLspPathIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLspPathIndex.setStatus(_A)
_VRtrMplsTpLspPathRowStatus_Type=RowStatus
_VRtrMplsTpLspPathRowStatus_Object=MibTableColumn
vRtrMplsTpLspPathRowStatus=_VRtrMplsTpLspPathRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,2),_VRtrMplsTpLspPathRowStatus_Type())
vRtrMplsTpLspPathRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathRowStatus.setStatus(_A)
_VRtrMplsTpLspPathLastChangedTime_Type=TimeStamp
_VRtrMplsTpLspPathLastChangedTime_Object=MibTableColumn
vRtrMplsTpLspPathLastChangedTime=_VRtrMplsTpLspPathLastChangedTime_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,3),_VRtrMplsTpLspPathLastChangedTime_Type())
vRtrMplsTpLspPathLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathLastChangedTime.setStatus(_A)
class _VRtrMplsTpLspPathAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsTpLspPathAdminState_Type.__name__=_O
_VRtrMplsTpLspPathAdminState_Object=MibTableColumn
vRtrMplsTpLspPathAdminState=_VRtrMplsTpLspPathAdminState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,4),_VRtrMplsTpLspPathAdminState_Type())
vRtrMplsTpLspPathAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathAdminState.setStatus(_A)
_VRtrMplsTpLspPathOperState_Type=TmnxOperState
_VRtrMplsTpLspPathOperState_Object=MibTableColumn
vRtrMplsTpLspPathOperState=_VRtrMplsTpLspPathOperState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,5),_VRtrMplsTpLspPathOperState_Type())
vRtrMplsTpLspPathOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathOperState.setStatus(_A)
class _VRtrMplsTpLspPathReasonDownFlags_Type(Bits):namedValues=NamedValues(*((_c,0),('ccFault',1),('cvFault',2),('ifDn',3),('portDn',4),('parentAdminDn',5),('mepAdminDn',6),('unsupportedPort',7),('ifNhAddrInconsistent',8),('ptcTmplMsng',9),('ccDnHold',10),('ccUpHold',11),('bfdNoRsrc',12)))
_VRtrMplsTpLspPathReasonDownFlags_Type.__name__=_R
_VRtrMplsTpLspPathReasonDownFlags_Object=MibTableColumn
vRtrMplsTpLspPathReasonDownFlags=_VRtrMplsTpLspPathReasonDownFlags_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,6),_VRtrMplsTpLspPathReasonDownFlags_Type())
vRtrMplsTpLspPathReasonDownFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathReasonDownFlags.setStatus(_A)
class _VRtrMplsTpLspPathLspNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VRtrMplsTpLspPathLspNumber_Type.__name__=_E
_VRtrMplsTpLspPathLspNumber_Object=MibTableColumn
vRtrMplsTpLspPathLspNumber=_VRtrMplsTpLspPathLspNumber_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,7),_VRtrMplsTpLspPathLspNumber_Type())
vRtrMplsTpLspPathLspNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathLspNumber.setStatus(_A)
class _VRtrMplsTpLspPathInLabel_Type(Unsigned32):defaultValue=0
_VRtrMplsTpLspPathInLabel_Type.__name__=_E
_VRtrMplsTpLspPathInLabel_Object=MibTableColumn
vRtrMplsTpLspPathInLabel=_VRtrMplsTpLspPathInLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,8),_VRtrMplsTpLspPathInLabel_Type())
vRtrMplsTpLspPathInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathInLabel.setStatus(_A)
class _VRtrMplsTpLspPathOutLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_VRtrMplsTpLspPathOutLabel_Type.__name__=_E
_VRtrMplsTpLspPathOutLabel_Object=MibTableColumn
vRtrMplsTpLspPathOutLabel=_VRtrMplsTpLspPathOutLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,9),_VRtrMplsTpLspPathOutLabel_Type())
vRtrMplsTpLspPathOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathOutLabel.setStatus(_A)
class _VRtrMplsTpLspPathOutLink_Type(InterfaceIndexOrZero):defaultValue=0
_VRtrMplsTpLspPathOutLink_Type.__name__=_P
_VRtrMplsTpLspPathOutLink_Object=MibTableColumn
vRtrMplsTpLspPathOutLink=_VRtrMplsTpLspPathOutLink_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,10),_VRtrMplsTpLspPathOutLink_Type())
vRtrMplsTpLspPathOutLink.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathOutLink.setStatus(_A)
class _VRtrMplsTpLspPathNextHopAddrType_Type(InetAddressType):defaultValue=0
_VRtrMplsTpLspPathNextHopAddrType_Type.__name__=_Q
_VRtrMplsTpLspPathNextHopAddrType_Object=MibTableColumn
vRtrMplsTpLspPathNextHopAddrType=_VRtrMplsTpLspPathNextHopAddrType_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,11),_VRtrMplsTpLspPathNextHopAddrType_Type())
vRtrMplsTpLspPathNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathNextHopAddrType.setStatus(_A)
class _VRtrMplsTpLspPathNextHopAddress_Type(InetAddress):defaultValue=OctetString('');subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrMplsTpLspPathNextHopAddress_Type.__name__=_L
_VRtrMplsTpLspPathNextHopAddress_Object=MibTableColumn
vRtrMplsTpLspPathNextHopAddress=_VRtrMplsTpLspPathNextHopAddress_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,12),_VRtrMplsTpLspPathNextHopAddress_Type())
vRtrMplsTpLspPathNextHopAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathNextHopAddress.setStatus(_A)
class _VRtrMplsTpLspPathState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('active',2),('inactive',3)))
_VRtrMplsTpLspPathState_Type.__name__=_K
_VRtrMplsTpLspPathState_Object=MibTableColumn
vRtrMplsTpLspPathState=_VRtrMplsTpLspPathState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,13),_VRtrMplsTpLspPathState_Type())
vRtrMplsTpLspPathState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathState.setStatus(_A)
_VRtrMplsTpLspPathTimeUp_Type=TimeInterval
_VRtrMplsTpLspPathTimeUp_Object=MibTableColumn
vRtrMplsTpLspPathTimeUp=_VRtrMplsTpLspPathTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,14),_VRtrMplsTpLspPathTimeUp_Type())
vRtrMplsTpLspPathTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathTimeUp.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpLspPathTimeUp.setUnits(_V)
_VRtrMplsTpLspPathTimeDown_Type=TimeInterval
_VRtrMplsTpLspPathTimeDown_Object=MibTableColumn
vRtrMplsTpLspPathTimeDown=_VRtrMplsTpLspPathTimeDown_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,15),_VRtrMplsTpLspPathTimeDown_Type())
vRtrMplsTpLspPathTimeDown.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathTimeDown.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpLspPathTimeDown.setUnits(_V)
_VRtrMplsTpLspPathActiveTimeUp_Type=TimeInterval
_VRtrMplsTpLspPathActiveTimeUp_Object=MibTableColumn
vRtrMplsTpLspPathActiveTimeUp=_VRtrMplsTpLspPathActiveTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,2,1,16),_VRtrMplsTpLspPathActiveTimeUp_Type())
vRtrMplsTpLspPathActiveTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathActiveTimeUp.setStatus(_A)
_VRtrMplsTpLspPathMepTable_Object=MibTable
vRtrMplsTpLspPathMepTable=_VRtrMplsTpLspPathMepTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3))
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepTable.setStatus(_A)
_VRtrMplsTpLspPathMepEntry_Object=MibTableRow
vRtrMplsTpLspPathMepEntry=_VRtrMplsTpLspPathMepEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1))
vRtrMplsTpLspPathMepEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_M,_N),(0,_D,_S))
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepEntry.setStatus(_A)
_VRtrMplsTpLspPathMepLastChgTime_Type=TimeStamp
_VRtrMplsTpLspPathMepLastChgTime_Object=MibTableColumn
vRtrMplsTpLspPathMepLastChgTime=_VRtrMplsTpLspPathMepLastChgTime_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,1),_VRtrMplsTpLspPathMepLastChgTime_Type())
vRtrMplsTpLspPathMepLastChgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepLastChgTime.setStatus(_A)
_VRtrMplsTpLspPathMepRowStatus_Type=RowStatus
_VRtrMplsTpLspPathMepRowStatus_Object=MibTableColumn
vRtrMplsTpLspPathMepRowStatus=_VRtrMplsTpLspPathMepRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,2),_VRtrMplsTpLspPathMepRowStatus_Type())
vRtrMplsTpLspPathMepRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepRowStatus.setStatus(_A)
class _VRtrMplsTpLspPathMepAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsTpLspPathMepAdminState_Type.__name__=_O
_VRtrMplsTpLspPathMepAdminState_Object=MibTableColumn
vRtrMplsTpLspPathMepAdminState=_VRtrMplsTpLspPathMepAdminState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,3),_VRtrMplsTpLspPathMepAdminState_Type())
vRtrMplsTpLspPathMepAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepAdminState.setStatus(_A)
class _VRtrMplsTpLspPathMepProtectTmpl_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_VRtrMplsTpLspPathMepProtectTmpl_Type.__name__=_U
_VRtrMplsTpLspPathMepProtectTmpl_Object=MibTableColumn
vRtrMplsTpLspPathMepProtectTmpl=_VRtrMplsTpLspPathMepProtectTmpl_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,4),_VRtrMplsTpLspPathMepProtectTmpl_Type())
vRtrMplsTpLspPathMepProtectTmpl.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepProtectTmpl.setStatus(_A)
class _VRtrMplsTpLspPathMepOamTmpl_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_VRtrMplsTpLspPathMepOamTmpl_Type.__name__=_U
_VRtrMplsTpLspPathMepOamTmpl_Object=MibTableColumn
vRtrMplsTpLspPathMepOamTmpl=_VRtrMplsTpLspPathMepOamTmpl_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,5),_VRtrMplsTpLspPathMepOamTmpl_Type())
vRtrMplsTpLspPathMepOamTmpl.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepOamTmpl.setStatus(_A)
class _VRtrMplsTpLspPathMepBfdEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('cc',1),('ccCv',2)))
_VRtrMplsTpLspPathMepBfdEnabled_Type.__name__=_K
_VRtrMplsTpLspPathMepBfdEnabled_Object=MibTableColumn
vRtrMplsTpLspPathMepBfdEnabled=_VRtrMplsTpLspPathMepBfdEnabled_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,6),_VRtrMplsTpLspPathMepBfdEnabled_Type())
vRtrMplsTpLspPathMepBfdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepBfdEnabled.setStatus(_A)
_VRtrMplsTpLspPathMepBfdOperState_Type=TmnxOperState
_VRtrMplsTpLspPathMepBfdOperState_Object=MibTableColumn
vRtrMplsTpLspPathMepBfdOperState=_VRtrMplsTpLspPathMepBfdOperState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,3,1,7),_VRtrMplsTpLspPathMepBfdOperState_Type())
vRtrMplsTpLspPathMepBfdOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPathMepBfdOperState.setStatus(_A)
_VRtrMplsTpLspPtPathMepStatTable_Object=MibTable
vRtrMplsTpLspPtPathMepStatTable=_VRtrMplsTpLspPtPathMepStatTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4))
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepStatTable.setStatus(_A)
_VRtrMplsTpLspPtPathMepStatEntry_Object=MibTableRow
vRtrMplsTpLspPtPathMepStatEntry=_VRtrMplsTpLspPtPathMepStatEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4,1))
vRtrMplsTpLspPtPathMepStatEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_M,_N),(0,_D,_S))
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepStatEntry.setStatus(_A)
_VRtrMplsTpLspPtPathMepRxPdu_Type=VRtrMplsTpLspPathMepPduType
_VRtrMplsTpLspPtPathMepRxPdu_Object=MibTableColumn
vRtrMplsTpLspPtPathMepRxPdu=_VRtrMplsTpLspPtPathMepRxPdu_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4,1,1),_VRtrMplsTpLspPtPathMepRxPdu_Type())
vRtrMplsTpLspPtPathMepRxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepRxPdu.setStatus(_A)
_VRtrMplsTpLspPtPathMepTxPdu_Type=VRtrMplsTpLspPathMepPduType
_VRtrMplsTpLspPtPathMepTxPdu_Object=MibTableColumn
vRtrMplsTpLspPtPathMepTxPdu=_VRtrMplsTpLspPtPathMepTxPdu_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4,1,2),_VRtrMplsTpLspPtPathMepTxPdu_Type())
vRtrMplsTpLspPtPathMepTxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepTxPdu.setStatus(_A)
class _VRtrMplsTpLspPtPathMepDefects_Type(Bits):namedValues=NamedValues(*(('protectionTypeMismatch',0),('revertModeMismatch',1)))
_VRtrMplsTpLspPtPathMepDefects_Type.__name__=_R
_VRtrMplsTpLspPtPathMepDefects_Object=MibTableColumn
vRtrMplsTpLspPtPathMepDefects=_VRtrMplsTpLspPtPathMepDefects_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4,1,3),_VRtrMplsTpLspPtPathMepDefects_Type())
vRtrMplsTpLspPtPathMepDefects.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepDefects.setStatus(_A)
_VRtrMplsTpLspPtPathMepWTRTimer_Type=Counter32
_VRtrMplsTpLspPtPathMepWTRTimer_Object=MibTableColumn
vRtrMplsTpLspPtPathMepWTRTimer=_VRtrMplsTpLspPtPathMepWTRTimer_Object((1,3,6,1,4,1,7483,6,1,2,83,2,3,4,1,4),_VRtrMplsTpLspPtPathMepWTRTimer_Type())
vRtrMplsTpLspPtPathMepWTRTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepWTRTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsTpLspPtPathMepWTRTimer.setUnits(_W)
_VRtrMplsTpCmdObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpCmdObjects=_VRtrMplsTpCmdObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2,4))
_VRtrMplsTpTunnelCommandTable_Object=MibTable
vRtrMplsTpTunnelCommandTable=_VRtrMplsTpTunnelCommandTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,4,1))
if mibBuilder.loadTexts:vRtrMplsTpTunnelCommandTable.setStatus(_A)
_VRtrMplsTpTunnelCommandEntry_Object=MibTableRow
vRtrMplsTpTunnelCommandEntry=_VRtrMplsTpTunnelCommandEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,4,1,1))
vRtrMplsTpTunnelCommandEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_M,_N))
if mibBuilder.loadTexts:vRtrMplsTpTunnelCommandEntry.setStatus(_A)
class _VRtrMplsTpTunnelCommandSwitch_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noCmd',0),('clear',1),('forceSwitch',2),('manualSwitch',3),('lockout',4)))
_VRtrMplsTpTunnelCommandSwitch_Type.__name__=_K
_VRtrMplsTpTunnelCommandSwitch_Object=MibTableColumn
vRtrMplsTpTunnelCommandSwitch=_VRtrMplsTpTunnelCommandSwitch_Object((1,3,6,1,4,1,7483,6,1,2,83,2,4,1,1,1),_VRtrMplsTpTunnelCommandSwitch_Type())
vRtrMplsTpTunnelCommandSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpTunnelCommandSwitch.setStatus(_A)
_VRtrMplsTpLsrObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpLsrObjects=_VRtrMplsTpLsrObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,2,5))
_VRtrMplsTpLsrCfgTable_Object=MibTable
vRtrMplsTpLsrCfgTable=_VRtrMplsTpLsrCfgTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1))
if mibBuilder.loadTexts:vRtrMplsTpLsrCfgTable.setStatus(_A)
_VRtrMplsTpLsrCfgEntry_Object=MibTableRow
vRtrMplsTpLsrCfgEntry=_VRtrMplsTpLsrCfgEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1))
vRtrMplsTpLsrCfgEntry.setIndexNames((0,_I,_J),(0,_G,_H),(1,_D,_d))
if mibBuilder.loadTexts:vRtrMplsTpLsrCfgEntry.setStatus(_A)
_VRtrMplsTpLsrPathName_Type=TNamedItem
_VRtrMplsTpLsrPathName_Object=MibTableColumn
vRtrMplsTpLsrPathName=_VRtrMplsTpLsrPathName_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,1),_VRtrMplsTpLsrPathName_Type())
vRtrMplsTpLsrPathName.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathName.setStatus(_A)
_VRtrMplsTpLsrRowStatus_Type=RowStatus
_VRtrMplsTpLsrRowStatus_Object=MibTableColumn
vRtrMplsTpLsrRowStatus=_VRtrMplsTpLsrRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,2),_VRtrMplsTpLsrRowStatus_Type())
vRtrMplsTpLsrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRowStatus.setStatus(_A)
_VRtrMplsTpLsrLastChangedTime_Type=TimeStamp
_VRtrMplsTpLsrLastChangedTime_Object=MibTableColumn
vRtrMplsTpLsrLastChangedTime=_VRtrMplsTpLsrLastChangedTime_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,3),_VRtrMplsTpLsrLastChangedTime_Type())
vRtrMplsTpLsrLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLsrLastChangedTime.setStatus(_A)
class _VRtrMplsTpLsrAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsTpLsrAdminState_Type.__name__=_O
_VRtrMplsTpLsrAdminState_Object=MibTableColumn
vRtrMplsTpLsrAdminState=_VRtrMplsTpLsrAdminState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,4),_VRtrMplsTpLsrAdminState_Type())
vRtrMplsTpLsrAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrAdminState.setStatus(_A)
_VRtrMplsTpLsrOperState_Type=TmnxOperState
_VRtrMplsTpLsrOperState_Object=MibTableColumn
vRtrMplsTpLsrOperState=_VRtrMplsTpLsrOperState_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,5),_VRtrMplsTpLsrOperState_Type())
vRtrMplsTpLsrOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpLsrOperState.setStatus(_A)
class _VRtrMplsTpLsrFPInLabel_Type(Unsigned32):defaultValue=0
_VRtrMplsTpLsrFPInLabel_Type.__name__=_E
_VRtrMplsTpLsrFPInLabel_Object=MibTableColumn
vRtrMplsTpLsrFPInLabel=_VRtrMplsTpLsrFPInLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,6),_VRtrMplsTpLsrFPInLabel_Type())
vRtrMplsTpLsrFPInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPInLabel.setStatus(_A)
class _VRtrMplsTpLsrFPOutLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_VRtrMplsTpLsrFPOutLabel_Type.__name__=_E
_VRtrMplsTpLsrFPOutLabel_Object=MibTableColumn
vRtrMplsTpLsrFPOutLabel=_VRtrMplsTpLsrFPOutLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,7),_VRtrMplsTpLsrFPOutLabel_Type())
vRtrMplsTpLsrFPOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPOutLabel.setStatus(_A)
class _VRtrMplsTpLsrFPOutLink_Type(InterfaceIndexOrZero):defaultValue=0
_VRtrMplsTpLsrFPOutLink_Type.__name__=_P
_VRtrMplsTpLsrFPOutLink_Object=MibTableColumn
vRtrMplsTpLsrFPOutLink=_VRtrMplsTpLsrFPOutLink_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,8),_VRtrMplsTpLsrFPOutLink_Type())
vRtrMplsTpLsrFPOutLink.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPOutLink.setStatus(_A)
class _VRtrMplsTpLsrFPNextHopAddrType_Type(InetAddressType):defaultValue=0
_VRtrMplsTpLsrFPNextHopAddrType_Type.__name__=_Q
_VRtrMplsTpLsrFPNextHopAddrType_Object=MibTableColumn
vRtrMplsTpLsrFPNextHopAddrType=_VRtrMplsTpLsrFPNextHopAddrType_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,9),_VRtrMplsTpLsrFPNextHopAddrType_Type())
vRtrMplsTpLsrFPNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPNextHopAddrType.setStatus(_A)
class _VRtrMplsTpLsrFPNextHopAddress_Type(InetAddress):defaultValue=OctetString('');subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrMplsTpLsrFPNextHopAddress_Type.__name__=_L
_VRtrMplsTpLsrFPNextHopAddress_Object=MibTableColumn
vRtrMplsTpLsrFPNextHopAddress=_VRtrMplsTpLsrFPNextHopAddress_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,10),_VRtrMplsTpLsrFPNextHopAddress_Type())
vRtrMplsTpLsrFPNextHopAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPNextHopAddress.setStatus(_A)
class _VRtrMplsTpLsrRPInLabel_Type(Unsigned32):defaultValue=0
_VRtrMplsTpLsrRPInLabel_Type.__name__=_E
_VRtrMplsTpLsrRPInLabel_Object=MibTableColumn
vRtrMplsTpLsrRPInLabel=_VRtrMplsTpLsrRPInLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,11),_VRtrMplsTpLsrRPInLabel_Type())
vRtrMplsTpLsrRPInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPInLabel.setStatus(_A)
class _VRtrMplsTpLsrRPOutLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_VRtrMplsTpLsrRPOutLabel_Type.__name__=_E
_VRtrMplsTpLsrRPOutLabel_Object=MibTableColumn
vRtrMplsTpLsrRPOutLabel=_VRtrMplsTpLsrRPOutLabel_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,12),_VRtrMplsTpLsrRPOutLabel_Type())
vRtrMplsTpLsrRPOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPOutLabel.setStatus(_A)
class _VRtrMplsTpLsrRPOutLink_Type(InterfaceIndexOrZero):defaultValue=0
_VRtrMplsTpLsrRPOutLink_Type.__name__=_P
_VRtrMplsTpLsrRPOutLink_Object=MibTableColumn
vRtrMplsTpLsrRPOutLink=_VRtrMplsTpLsrRPOutLink_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,13),_VRtrMplsTpLsrRPOutLink_Type())
vRtrMplsTpLsrRPOutLink.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPOutLink.setStatus(_A)
class _VRtrMplsTpLsrRPNextHopAddrType_Type(InetAddressType):defaultValue=0
_VRtrMplsTpLsrRPNextHopAddrType_Type.__name__=_Q
_VRtrMplsTpLsrRPNextHopAddrType_Object=MibTableColumn
vRtrMplsTpLsrRPNextHopAddrType=_VRtrMplsTpLsrRPNextHopAddrType_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,14),_VRtrMplsTpLsrRPNextHopAddrType_Type())
vRtrMplsTpLsrRPNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPNextHopAddrType.setStatus(_A)
class _VRtrMplsTpLsrRPNextHopAddress_Type(InetAddress):defaultValue=OctetString('');subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrMplsTpLsrRPNextHopAddress_Type.__name__=_L
_VRtrMplsTpLsrRPNextHopAddress_Object=MibTableColumn
vRtrMplsTpLsrRPNextHopAddress=_VRtrMplsTpLsrRPNextHopAddress_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,15),_VRtrMplsTpLsrRPNextHopAddress_Type())
vRtrMplsTpLsrRPNextHopAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPNextHopAddress.setStatus(_A)
class _VRtrMplsTpLsrFPEnabled_Type(TruthValue):defaultValue=2
_VRtrMplsTpLsrFPEnabled_Type.__name__=_T
_VRtrMplsTpLsrFPEnabled_Object=MibTableColumn
vRtrMplsTpLsrFPEnabled=_VRtrMplsTpLsrFPEnabled_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,16),_VRtrMplsTpLsrFPEnabled_Type())
vRtrMplsTpLsrFPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrFPEnabled.setStatus(_A)
class _VRtrMplsTpLsrRPEnabled_Type(TruthValue):defaultValue=2
_VRtrMplsTpLsrRPEnabled_Type.__name__=_T
_VRtrMplsTpLsrRPEnabled_Object=MibTableColumn
vRtrMplsTpLsrRPEnabled=_VRtrMplsTpLsrRPEnabled_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,1,1,17),_VRtrMplsTpLsrRPEnabled_Type())
vRtrMplsTpLsrRPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrRPEnabled.setStatus(_A)
_VRtrMplsTpLsrPathIdTable_Object=MibTable
vRtrMplsTpLsrPathIdTable=_VRtrMplsTpLsrPathIdTable_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3))
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdTable.setStatus(_A)
_VRtrMplsTpLsrPathIdEntry_Object=MibTableRow
vRtrMplsTpLsrPathIdEntry=_VRtrMplsTpLsrPathIdEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1))
vRtrMplsTpLsrPathIdEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdEntry.setStatus(_A)
_VRtrMplsTpLsrPathIdSrcGlobalId_Type=TmnxMplsTpGlobalID
_VRtrMplsTpLsrPathIdSrcGlobalId_Object=MibTableColumn
vRtrMplsTpLsrPathIdSrcGlobalId=_VRtrMplsTpLsrPathIdSrcGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,1),_VRtrMplsTpLsrPathIdSrcGlobalId_Type())
vRtrMplsTpLsrPathIdSrcGlobalId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdSrcGlobalId.setStatus(_A)
_VRtrMplsTpLsrPathIdSrcNodeId_Type=TmnxMplsTpNodeID
_VRtrMplsTpLsrPathIdSrcNodeId_Object=MibTableColumn
vRtrMplsTpLsrPathIdSrcNodeId=_VRtrMplsTpLsrPathIdSrcNodeId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,2),_VRtrMplsTpLsrPathIdSrcNodeId_Type())
vRtrMplsTpLsrPathIdSrcNodeId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdSrcNodeId.setStatus(_A)
class _VRtrMplsTpLsrPathIdSrcTunNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,61440))
_VRtrMplsTpLsrPathIdSrcTunNum_Type.__name__=_E
_VRtrMplsTpLsrPathIdSrcTunNum_Object=MibTableColumn
vRtrMplsTpLsrPathIdSrcTunNum=_VRtrMplsTpLsrPathIdSrcTunNum_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,3),_VRtrMplsTpLsrPathIdSrcTunNum_Type())
vRtrMplsTpLsrPathIdSrcTunNum.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdSrcTunNum.setStatus(_A)
_VRtrMplsTpLsrPathIdDestGlobalId_Type=TmnxMplsTpGlobalID
_VRtrMplsTpLsrPathIdDestGlobalId_Object=MibTableColumn
vRtrMplsTpLsrPathIdDestGlobalId=_VRtrMplsTpLsrPathIdDestGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,4),_VRtrMplsTpLsrPathIdDestGlobalId_Type())
vRtrMplsTpLsrPathIdDestGlobalId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdDestGlobalId.setStatus(_A)
_VRtrMplsTpLsrPathIdDestNodeId_Type=TmnxMplsTpNodeID
_VRtrMplsTpLsrPathIdDestNodeId_Object=MibTableColumn
vRtrMplsTpLsrPathIdDestNodeId=_VRtrMplsTpLsrPathIdDestNodeId_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,5),_VRtrMplsTpLsrPathIdDestNodeId_Type())
vRtrMplsTpLsrPathIdDestNodeId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdDestNodeId.setStatus(_A)
class _VRtrMplsTpLsrPathIdDestTunNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,61440))
_VRtrMplsTpLsrPathIdDestTunNum_Type.__name__=_E
_VRtrMplsTpLsrPathIdDestTunNum_Object=MibTableColumn
vRtrMplsTpLsrPathIdDestTunNum=_VRtrMplsTpLsrPathIdDestTunNum_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,6),_VRtrMplsTpLsrPathIdDestTunNum_Type())
vRtrMplsTpLsrPathIdDestTunNum.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdDestTunNum.setStatus(_A)
class _VRtrMplsTpLsrPathIdLspNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VRtrMplsTpLsrPathIdLspNumber_Type.__name__=_E
_VRtrMplsTpLsrPathIdLspNumber_Object=MibTableColumn
vRtrMplsTpLsrPathIdLspNumber=_VRtrMplsTpLsrPathIdLspNumber_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,7),_VRtrMplsTpLsrPathIdLspNumber_Type())
vRtrMplsTpLsrPathIdLspNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdLspNumber.setStatus(_A)
_VRtrMplsTpLsrPathIdRowStatus_Type=RowStatus
_VRtrMplsTpLsrPathIdRowStatus_Object=MibTableColumn
vRtrMplsTpLsrPathIdRowStatus=_VRtrMplsTpLsrPathIdRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,8),_VRtrMplsTpLsrPathIdRowStatus_Type())
vRtrMplsTpLsrPathIdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdRowStatus.setStatus(_A)
_VRtrMplsTpLsrPathIdPathName_Type=TNamedItem
_VRtrMplsTpLsrPathIdPathName_Object=MibTableColumn
vRtrMplsTpLsrPathIdPathName=_VRtrMplsTpLsrPathIdPathName_Object((1,3,6,1,4,1,7483,6,1,2,83,2,5,3,1,9),_VRtrMplsTpLsrPathIdPathName_Type())
vRtrMplsTpLsrPathIdPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsTpLsrPathIdPathName.setStatus(_A)
_VRtrMplsTpStatus_ObjectIdentity=ObjectIdentity
vRtrMplsTpStatus=_VRtrMplsTpStatus_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,3))
_VRtrMplsTpStatusObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpStatusObjects=_VRtrMplsTpStatusObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,3,1))
_VRtrMplsTpTunnelTable_Object=MibTable
vRtrMplsTpTunnelTable=_VRtrMplsTpTunnelTable_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1))
if mibBuilder.loadTexts:vRtrMplsTpTunnelTable.setStatus(_A)
_VRtrMplsTpTunnelEntry_Object=MibTableRow
vRtrMplsTpTunnelEntry=_VRtrMplsTpTunnelEntry_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1))
vRtrMplsTpTunnelEntry.setIndexNames((0,_I,_J),(0,_G,_H),(0,_D,_l),(0,_D,_m),(0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:vRtrMplsTpTunnelEntry.setStatus(_A)
_VRtrMplsTpTunnelNodeId_Type=TmnxMplsTpNodeID
_VRtrMplsTpTunnelNodeId_Object=MibTableColumn
vRtrMplsTpTunnelNodeId=_VRtrMplsTpTunnelNodeId_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,1),_VRtrMplsTpTunnelNodeId_Type())
vRtrMplsTpTunnelNodeId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelNodeId.setStatus(_A)
_VRtrMplsTpTunnelGlobalId_Type=TmnxMplsTpGlobalID
_VRtrMplsTpTunnelGlobalId_Object=MibTableColumn
vRtrMplsTpTunnelGlobalId=_VRtrMplsTpTunnelGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,2),_VRtrMplsTpTunnelGlobalId_Type())
vRtrMplsTpTunnelGlobalId.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelGlobalId.setStatus(_A)
class _VRtrMplsTpTunnelPreference_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VRtrMplsTpTunnelPreference_Type.__name__=_E
_VRtrMplsTpTunnelPreference_Object=MibTableColumn
vRtrMplsTpTunnelPreference=_VRtrMplsTpTunnelPreference_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,3),_VRtrMplsTpTunnelPreference_Type())
vRtrMplsTpTunnelPreference.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelPreference.setStatus(_A)
_VRtrMplsTpTunnelType_Type=TmnxMplsTpTunnelType
_VRtrMplsTpTunnelType_Object=MibTableColumn
vRtrMplsTpTunnelType=_VRtrMplsTpTunnelType_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,4),_VRtrMplsTpTunnelType_Type())
vRtrMplsTpTunnelType.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelType.setStatus(_A)
_VRtrMplsTpTunnelID_Type=TmnxTunnelID
_VRtrMplsTpTunnelID_Object=MibTableColumn
vRtrMplsTpTunnelID=_VRtrMplsTpTunnelID_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,5),_VRtrMplsTpTunnelID_Type())
vRtrMplsTpTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelID.setStatus(_A)
_VRtrMplsTpTunnelNextHopAddrType_Type=InetAddressType
_VRtrMplsTpTunnelNextHopAddrType_Object=MibTableColumn
vRtrMplsTpTunnelNextHopAddrType=_VRtrMplsTpTunnelNextHopAddrType_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,6),_VRtrMplsTpTunnelNextHopAddrType_Type())
vRtrMplsTpTunnelNextHopAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelNextHopAddrType.setStatus(_A)
class _VRtrMplsTpTunnelNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_VRtrMplsTpTunnelNextHopAddress_Type.__name__=_L
_VRtrMplsTpTunnelNextHopAddress_Object=MibTableColumn
vRtrMplsTpTunnelNextHopAddress=_VRtrMplsTpTunnelNextHopAddress_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,7),_VRtrMplsTpTunnelNextHopAddress_Type())
vRtrMplsTpTunnelNextHopAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:vRtrMplsTpTunnelNextHopAddress.setStatus(_A)
_VRtrMplsTpTunnelMetric_Type=Unsigned32
_VRtrMplsTpTunnelMetric_Object=MibTableColumn
vRtrMplsTpTunnelMetric=_VRtrMplsTpTunnelMetric_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,8),_VRtrMplsTpTunnelMetric_Type())
vRtrMplsTpTunnelMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpTunnelMetric.setStatus(_A)
_VRtrMplsTpTunnelAge_Type=Integer32
_VRtrMplsTpTunnelAge_Object=MibTableColumn
vRtrMplsTpTunnelAge=_VRtrMplsTpTunnelAge_Object((1,3,6,1,4,1,7483,6,1,2,83,3,1,1,1,9),_VRtrMplsTpTunnelAge_Type())
vRtrMplsTpTunnelAge.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsTpTunnelAge.setStatus(_A)
_VRtrMplsTpStatistics_ObjectIdentity=ObjectIdentity
vRtrMplsTpStatistics=_VRtrMplsTpStatistics_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,5))
_VRtrMplsTpActions_ObjectIdentity=ObjectIdentity
vRtrMplsTpActions=_VRtrMplsTpActions_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,6))
_VRtrMplsTpNotifyObjects_ObjectIdentity=ObjectIdentity
vRtrMplsTpNotifyObjects=_VRtrMplsTpNotifyObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,83,10))
mibBuilder.exportSymbols(_D,**{'VRtrMplsTpLspPathMepPduType':VRtrMplsTpLspPathMepPduType,'tnMplsTpMIBModule':tnMplsTpMIBModule,'vRtrMplsTpObjs':vRtrMplsTpObjs,'vRtrMplsTpConfigTimeStamps':vRtrMplsTpConfigTimeStamps,'vRtrMplsTpSystemTableLastChanged':vRtrMplsTpSystemTableLastChanged,'vRtrMplsTpOamTemplTblLastChanged':vRtrMplsTpOamTemplTblLastChanged,'vRtrMplsTpPtcTemplTblLastChanged':vRtrMplsTpPtcTemplTblLastChanged,'vRtrMplsTpLspPathTblLastChanged':vRtrMplsTpLspPathTblLastChanged,'vRtrMplsTpLspPathMepTblLastChg':vRtrMplsTpLspPathMepTblLastChg,'vRtrMplsTpLsrTblLastChanged':vRtrMplsTpLsrTblLastChanged,'vRtrMplsTpLsrPathIdTblLastChg':vRtrMplsTpLsrPathIdTblLastChg,'vRtrMplsTpScalar1':vRtrMplsTpScalar1,'vRtrMplsTpScalar2':vRtrMplsTpScalar2,'vRtrMplsTpConfigurations':vRtrMplsTpConfigurations,'vRtrMplsTpSystemIdentifiers':vRtrMplsTpSystemIdentifiers,'vRtrMplsTpSystemTable':vRtrMplsTpSystemTable,'vRtrMplsTpSystemEntry':vRtrMplsTpSystemEntry,'vRtrMplsTpRowStatus':vRtrMplsTpRowStatus,'vRtrMplsTpGlobalId':vRtrMplsTpGlobalId,_Z:vRtrMplsTpNodeId,'vRtrMplsTpTunnelIdMin':vRtrMplsTpTunnelIdMin,'vRtrMplsTpTunnelIdMax':vRtrMplsTpTunnelIdMax,'vRtrMplsTpAdminState':vRtrMplsTpAdminState,'vRtrMplsTpInheritance':vRtrMplsTpInheritance,'vRtrMplsTpTemplateObjects':vRtrMplsTpTemplateObjects,'vRtrMplsTpOamTemplateCfgTable':vRtrMplsTpOamTemplateCfgTable,'vRtrMplsTpOamTemplateCfgEntry':vRtrMplsTpOamTemplateCfgEntry,_a:vRtrMplsTpOamTmplName,'vRtrMplsTpOamTmplRowStatus':vRtrMplsTpOamTmplRowStatus,'vRtrMplsTpOamTmplLastChangedTime':vRtrMplsTpOamTmplLastChangedTime,'vRtrMplsTpOamTmplBfdTemplateName':vRtrMplsTpOamTmplBfdTemplateName,'vRtrMplsTpOamTmplHoldTimeDown':vRtrMplsTpOamTmplHoldTimeDown,'vRtrMplsTpOamTmplHoldTimeUp':vRtrMplsTpOamTmplHoldTimeUp,'vRtrMplsTpPtcTemplateCfgTable':vRtrMplsTpPtcTemplateCfgTable,'vRtrMplsTpPtcTemplateCfgEntry':vRtrMplsTpPtcTemplateCfgEntry,_b:vRtrMplsTpPtcTmplName,'vRtrMplsTpPtcTmplRowStatus':vRtrMplsTpPtcTmplRowStatus,'vRtrMplsTpPtcTmplLastChangedTime':vRtrMplsTpPtcTmplLastChangedTime,'vRtrMplsTpPtcTmplProtectionMode':vRtrMplsTpPtcTmplProtectionMode,'vRtrMplsTpPtcTmplProtectionDir':vRtrMplsTpPtcTmplProtectionDir,'vRtrMplsTpPtcTmplRevertive':vRtrMplsTpPtcTmplRevertive,'vRtrMplsTpPtcTmplWaitToRestore':vRtrMplsTpPtcTmplWaitToRestore,'vRtrMplsTpPtcTmplRapidPscTimer':vRtrMplsTpPtcTmplRapidPscTimer,'vRtrMplsTpPtcTmplSlowPscTimer':vRtrMplsTpPtcTmplSlowPscTimer,'vRtrMplsTpLspObjects':vRtrMplsTpLspObjects,'vRtrMplsTpLspPathTable':vRtrMplsTpLspPathTable,'vRtrMplsTpLspPathEntry':vRtrMplsTpLspPathEntry,_S:vRtrMplsTpLspPathIndex,'vRtrMplsTpLspPathRowStatus':vRtrMplsTpLspPathRowStatus,'vRtrMplsTpLspPathLastChangedTime':vRtrMplsTpLspPathLastChangedTime,'vRtrMplsTpLspPathAdminState':vRtrMplsTpLspPathAdminState,'vRtrMplsTpLspPathOperState':vRtrMplsTpLspPathOperState,'vRtrMplsTpLspPathReasonDownFlags':vRtrMplsTpLspPathReasonDownFlags,'vRtrMplsTpLspPathLspNumber':vRtrMplsTpLspPathLspNumber,'vRtrMplsTpLspPathInLabel':vRtrMplsTpLspPathInLabel,'vRtrMplsTpLspPathOutLabel':vRtrMplsTpLspPathOutLabel,'vRtrMplsTpLspPathOutLink':vRtrMplsTpLspPathOutLink,'vRtrMplsTpLspPathNextHopAddrType':vRtrMplsTpLspPathNextHopAddrType,'vRtrMplsTpLspPathNextHopAddress':vRtrMplsTpLspPathNextHopAddress,'vRtrMplsTpLspPathState':vRtrMplsTpLspPathState,'vRtrMplsTpLspPathTimeUp':vRtrMplsTpLspPathTimeUp,'vRtrMplsTpLspPathTimeDown':vRtrMplsTpLspPathTimeDown,'vRtrMplsTpLspPathActiveTimeUp':vRtrMplsTpLspPathActiveTimeUp,'vRtrMplsTpLspPathMepTable':vRtrMplsTpLspPathMepTable,'vRtrMplsTpLspPathMepEntry':vRtrMplsTpLspPathMepEntry,'vRtrMplsTpLspPathMepLastChgTime':vRtrMplsTpLspPathMepLastChgTime,'vRtrMplsTpLspPathMepRowStatus':vRtrMplsTpLspPathMepRowStatus,'vRtrMplsTpLspPathMepAdminState':vRtrMplsTpLspPathMepAdminState,'vRtrMplsTpLspPathMepProtectTmpl':vRtrMplsTpLspPathMepProtectTmpl,'vRtrMplsTpLspPathMepOamTmpl':vRtrMplsTpLspPathMepOamTmpl,'vRtrMplsTpLspPathMepBfdEnabled':vRtrMplsTpLspPathMepBfdEnabled,'vRtrMplsTpLspPathMepBfdOperState':vRtrMplsTpLspPathMepBfdOperState,'vRtrMplsTpLspPtPathMepStatTable':vRtrMplsTpLspPtPathMepStatTable,'vRtrMplsTpLspPtPathMepStatEntry':vRtrMplsTpLspPtPathMepStatEntry,'vRtrMplsTpLspPtPathMepRxPdu':vRtrMplsTpLspPtPathMepRxPdu,'vRtrMplsTpLspPtPathMepTxPdu':vRtrMplsTpLspPtPathMepTxPdu,'vRtrMplsTpLspPtPathMepDefects':vRtrMplsTpLspPtPathMepDefects,'vRtrMplsTpLspPtPathMepWTRTimer':vRtrMplsTpLspPtPathMepWTRTimer,'vRtrMplsTpCmdObjects':vRtrMplsTpCmdObjects,'vRtrMplsTpTunnelCommandTable':vRtrMplsTpTunnelCommandTable,'vRtrMplsTpTunnelCommandEntry':vRtrMplsTpTunnelCommandEntry,'vRtrMplsTpTunnelCommandSwitch':vRtrMplsTpTunnelCommandSwitch,'vRtrMplsTpLsrObjects':vRtrMplsTpLsrObjects,'vRtrMplsTpLsrCfgTable':vRtrMplsTpLsrCfgTable,'vRtrMplsTpLsrCfgEntry':vRtrMplsTpLsrCfgEntry,_d:vRtrMplsTpLsrPathName,'vRtrMplsTpLsrRowStatus':vRtrMplsTpLsrRowStatus,'vRtrMplsTpLsrLastChangedTime':vRtrMplsTpLsrLastChangedTime,'vRtrMplsTpLsrAdminState':vRtrMplsTpLsrAdminState,'vRtrMplsTpLsrOperState':vRtrMplsTpLsrOperState,'vRtrMplsTpLsrFPInLabel':vRtrMplsTpLsrFPInLabel,'vRtrMplsTpLsrFPOutLabel':vRtrMplsTpLsrFPOutLabel,'vRtrMplsTpLsrFPOutLink':vRtrMplsTpLsrFPOutLink,'vRtrMplsTpLsrFPNextHopAddrType':vRtrMplsTpLsrFPNextHopAddrType,'vRtrMplsTpLsrFPNextHopAddress':vRtrMplsTpLsrFPNextHopAddress,'vRtrMplsTpLsrRPInLabel':vRtrMplsTpLsrRPInLabel,'vRtrMplsTpLsrRPOutLabel':vRtrMplsTpLsrRPOutLabel,'vRtrMplsTpLsrRPOutLink':vRtrMplsTpLsrRPOutLink,'vRtrMplsTpLsrRPNextHopAddrType':vRtrMplsTpLsrRPNextHopAddrType,'vRtrMplsTpLsrRPNextHopAddress':vRtrMplsTpLsrRPNextHopAddress,'vRtrMplsTpLsrFPEnabled':vRtrMplsTpLsrFPEnabled,'vRtrMplsTpLsrRPEnabled':vRtrMplsTpLsrRPEnabled,'vRtrMplsTpLsrPathIdTable':vRtrMplsTpLsrPathIdTable,'vRtrMplsTpLsrPathIdEntry':vRtrMplsTpLsrPathIdEntry,_e:vRtrMplsTpLsrPathIdSrcGlobalId,_f:vRtrMplsTpLsrPathIdSrcNodeId,_g:vRtrMplsTpLsrPathIdSrcTunNum,_h:vRtrMplsTpLsrPathIdDestGlobalId,_i:vRtrMplsTpLsrPathIdDestNodeId,_j:vRtrMplsTpLsrPathIdDestTunNum,_k:vRtrMplsTpLsrPathIdLspNumber,'vRtrMplsTpLsrPathIdRowStatus':vRtrMplsTpLsrPathIdRowStatus,'vRtrMplsTpLsrPathIdPathName':vRtrMplsTpLsrPathIdPathName,'vRtrMplsTpStatus':vRtrMplsTpStatus,'vRtrMplsTpStatusObjects':vRtrMplsTpStatusObjects,'vRtrMplsTpTunnelTable':vRtrMplsTpTunnelTable,'vRtrMplsTpTunnelEntry':vRtrMplsTpTunnelEntry,_l:vRtrMplsTpTunnelNodeId,_m:vRtrMplsTpTunnelGlobalId,_n:vRtrMplsTpTunnelPreference,_o:vRtrMplsTpTunnelType,_p:vRtrMplsTpTunnelID,_q:vRtrMplsTpTunnelNextHopAddrType,_r:vRtrMplsTpTunnelNextHopAddress,'vRtrMplsTpTunnelMetric':vRtrMplsTpTunnelMetric,'vRtrMplsTpTunnelAge':vRtrMplsTpTunnelAge,'vRtrMplsTpStatistics':vRtrMplsTpStatistics,'vRtrMplsTpActions':vRtrMplsTpActions,'vRtrMplsTpNotifyObjects':vRtrMplsTpNotifyObjects})