_x='fsVMMIBGroup'
_w='fsVMOuiInfoRowStatus'
_v='fsVMPortTrapCfgNotifyStatus'
_u='fsVMPortInfoReflectStatus'
_t='fsVMPortInfoStatus'
_s='fsVMLocInfoRowStatus'
_r='fsVMLocInfoType'
_q='fsVMProfileQosRxPolicyMap'
_p='fsVMProfileQosDefCos'
_o='fsVMProfileQosTrustMode'
_n='fsVMProfileRowStatus'
_m='fsVMProfileRxBurst'
_l='fsVMProfileRxRate'
_k='fsVMProfileTxBurst'
_j='fsVMProfileTxRate'
_i='fsVMProfileAclOut'
_h='fsVMProfileAclIn'
_g='fsVMGroupInfoRowStatus'
_f='fsVMGroupInfoProfileName'
_e='fsVMGroupInfoProfileCfg'
_d='fsVMInfoRowStatus'
_c='fsVMBurstMax'
_b='fsVMBurstMin'
_a='fsVMRateMax'
_Z='fsVMRateMin'
_Y='fsVMTrapCfgHistorySize'
_X='fsVMTrapCfgNotifyStatus'
_W='fsVMFuncVMSupport'
_V='fsVMInfoChgDate'
_U='fsVMInfoChgAction'
_T='fsVMInfoChgPort'
_S='fsVMOuiInfoOui'
_R='fsVMPortTrapCfgPort'
_Q='fsVMPortInfoPort'
_P='fsVMLocInfoPort'
_O='fsVMLocInfoVMMac'
_N='fsVMProfileName'
_M='fsVMGroupInfoGroupName'
_L='fsVMInfoVMGroup'
_K='fsVMInfoVMMac'
_J='Integer32'
_I='fsVMInfoChgVlan'
_H='fsVMInfoChgVMMac'
_G='accessible-for-notify'
_F='read-create'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='FS-VM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsVMMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,96))
if mibBuilder.loadTexts:fsVMMIB.setRevisions(('2012-08-22 00:00',))
_FsVMMIBObjects_ObjectIdentity=ObjectIdentity
fsVMMIBObjects=_FsVMMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,96,1))
_FsVMFuncVMSupport_Type=ConfigStatus
_FsVMFuncVMSupport_Object=MibScalar
fsVMFuncVMSupport=_FsVMFuncVMSupport_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,1),_FsVMFuncVMSupport_Type())
fsVMFuncVMSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMFuncVMSupport.setStatus(_A)
_FsVMTrapCfgNotifyStatus_Type=ConfigStatus
_FsVMTrapCfgNotifyStatus_Object=MibScalar
fsVMTrapCfgNotifyStatus=_FsVMTrapCfgNotifyStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,2),_FsVMTrapCfgNotifyStatus_Type())
fsVMTrapCfgNotifyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMTrapCfgNotifyStatus.setStatus(_A)
_FsVMTrapCfgHistorySize_Type=Unsigned32
_FsVMTrapCfgHistorySize_Object=MibScalar
fsVMTrapCfgHistorySize=_FsVMTrapCfgHistorySize_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,3),_FsVMTrapCfgHistorySize_Type())
fsVMTrapCfgHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMTrapCfgHistorySize.setStatus(_A)
_FsVMInfoTable_Object=MibTable
fsVMInfoTable=_FsVMInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,4))
if mibBuilder.loadTexts:fsVMInfoTable.setStatus(_A)
_FsVMInfoEntry_Object=MibTableRow
fsVMInfoEntry=_FsVMInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,4,1))
fsVMInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsVMInfoEntry.setStatus(_A)
_FsVMInfoVMMac_Type=MacAddress
_FsVMInfoVMMac_Object=MibTableColumn
fsVMInfoVMMac=_FsVMInfoVMMac_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,4,1,1),_FsVMInfoVMMac_Type())
fsVMInfoVMMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMInfoVMMac.setStatus(_A)
_FsVMInfoVMGroup_Type=Integer32
_FsVMInfoVMGroup_Object=MibTableColumn
fsVMInfoVMGroup=_FsVMInfoVMGroup_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,4,1,2),_FsVMInfoVMGroup_Type())
fsVMInfoVMGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMInfoVMGroup.setStatus(_A)
_FsVMInfoRowStatus_Type=RowStatus
_FsVMInfoRowStatus_Object=MibTableColumn
fsVMInfoRowStatus=_FsVMInfoRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,4,1,3),_FsVMInfoRowStatus_Type())
fsVMInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVMInfoRowStatus.setStatus(_A)
_FsVMGroupInfoTable_Object=MibTable
fsVMGroupInfoTable=_FsVMGroupInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5))
if mibBuilder.loadTexts:fsVMGroupInfoTable.setStatus(_A)
_FsVMGroupInfoEntry_Object=MibTableRow
fsVMGroupInfoEntry=_FsVMGroupInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5,1))
fsVMGroupInfoEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:fsVMGroupInfoEntry.setStatus(_A)
_FsVMGroupInfoGroupName_Type=Integer32
_FsVMGroupInfoGroupName_Object=MibTableColumn
fsVMGroupInfoGroupName=_FsVMGroupInfoGroupName_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5,1,1),_FsVMGroupInfoGroupName_Type())
fsVMGroupInfoGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMGroupInfoGroupName.setStatus(_A)
_FsVMGroupInfoProfileCfg_Type=ConfigStatus
_FsVMGroupInfoProfileCfg_Object=MibTableColumn
fsVMGroupInfoProfileCfg=_FsVMGroupInfoProfileCfg_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5,1,2),_FsVMGroupInfoProfileCfg_Type())
fsVMGroupInfoProfileCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMGroupInfoProfileCfg.setStatus(_A)
class _FsVMGroupInfoProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVMGroupInfoProfileName_Type.__name__=_E
_FsVMGroupInfoProfileName_Object=MibTableColumn
fsVMGroupInfoProfileName=_FsVMGroupInfoProfileName_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5,1,3),_FsVMGroupInfoProfileName_Type())
fsVMGroupInfoProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMGroupInfoProfileName.setStatus(_A)
_FsVMGroupInfoRowStatus_Type=RowStatus
_FsVMGroupInfoRowStatus_Object=MibTableColumn
fsVMGroupInfoRowStatus=_FsVMGroupInfoRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,5,1,4),_FsVMGroupInfoRowStatus_Type())
fsVMGroupInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVMGroupInfoRowStatus.setStatus(_A)
_FsVMProfileTable_Object=MibTable
fsVMProfileTable=_FsVMProfileTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6))
if mibBuilder.loadTexts:fsVMProfileTable.setStatus(_A)
_FsVMProfileEntry_Object=MibTableRow
fsVMProfileEntry=_FsVMProfileEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1))
fsVMProfileEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsVMProfileEntry.setStatus(_A)
class _FsVMProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVMProfileName_Type.__name__=_E
_FsVMProfileName_Object=MibTableColumn
fsVMProfileName=_FsVMProfileName_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,1),_FsVMProfileName_Type())
fsVMProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMProfileName.setStatus(_A)
class _FsVMProfileAclIn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_FsVMProfileAclIn_Type.__name__=_E
_FsVMProfileAclIn_Object=MibTableColumn
fsVMProfileAclIn=_FsVMProfileAclIn_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,2),_FsVMProfileAclIn_Type())
fsVMProfileAclIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileAclIn.setStatus(_A)
class _FsVMProfileAclOut_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_FsVMProfileAclOut_Type.__name__=_E
_FsVMProfileAclOut_Object=MibTableColumn
fsVMProfileAclOut=_FsVMProfileAclOut_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,3),_FsVMProfileAclOut_Type())
fsVMProfileAclOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileAclOut.setStatus(_A)
_FsVMProfileTxRate_Type=Unsigned32
_FsVMProfileTxRate_Object=MibTableColumn
fsVMProfileTxRate=_FsVMProfileTxRate_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,4),_FsVMProfileTxRate_Type())
fsVMProfileTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileTxRate.setStatus(_A)
_FsVMProfileTxBurst_Type=Integer32
_FsVMProfileTxBurst_Object=MibTableColumn
fsVMProfileTxBurst=_FsVMProfileTxBurst_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,5),_FsVMProfileTxBurst_Type())
fsVMProfileTxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileTxBurst.setStatus(_A)
_FsVMProfileRxRate_Type=Unsigned32
_FsVMProfileRxRate_Object=MibTableColumn
fsVMProfileRxRate=_FsVMProfileRxRate_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,6),_FsVMProfileRxRate_Type())
fsVMProfileRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileRxRate.setStatus(_A)
_FsVMProfileRxBurst_Type=Integer32
_FsVMProfileRxBurst_Object=MibTableColumn
fsVMProfileRxBurst=_FsVMProfileRxBurst_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,7),_FsVMProfileRxBurst_Type())
fsVMProfileRxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileRxBurst.setStatus(_A)
_FsVMProfileRowStatus_Type=RowStatus
_FsVMProfileRowStatus_Object=MibTableColumn
fsVMProfileRowStatus=_FsVMProfileRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,8),_FsVMProfileRowStatus_Type())
fsVMProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVMProfileRowStatus.setStatus(_A)
class _FsVMProfileQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('not-trust',0),('trust-cos',1),('trust-dscp',2),('trust-ip-precedence',3)))
_FsVMProfileQosTrustMode_Type.__name__=_J
_FsVMProfileQosTrustMode_Object=MibTableColumn
fsVMProfileQosTrustMode=_FsVMProfileQosTrustMode_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,9),_FsVMProfileQosTrustMode_Type())
fsVMProfileQosTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileQosTrustMode.setStatus(_A)
class _FsVMProfileQosDefCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('invalid',8))
_FsVMProfileQosDefCos_Type.__name__=_J
_FsVMProfileQosDefCos_Object=MibTableColumn
fsVMProfileQosDefCos=_FsVMProfileQosDefCos_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,10),_FsVMProfileQosDefCos_Type())
fsVMProfileQosDefCos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileQosDefCos.setStatus(_A)
class _FsVMProfileQosRxPolicyMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVMProfileQosRxPolicyMap_Type.__name__=_E
_FsVMProfileQosRxPolicyMap_Object=MibTableColumn
fsVMProfileQosRxPolicyMap=_FsVMProfileQosRxPolicyMap_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,6,1,11),_FsVMProfileQosRxPolicyMap_Type())
fsVMProfileQosRxPolicyMap.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMProfileQosRxPolicyMap.setStatus(_A)
_FsVMLocInfoTable_Object=MibTable
fsVMLocInfoTable=_FsVMLocInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7))
if mibBuilder.loadTexts:fsVMLocInfoTable.setStatus(_A)
_FsVMLocInfoEntry_Object=MibTableRow
fsVMLocInfoEntry=_FsVMLocInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7,1))
fsVMLocInfoEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsVMLocInfoEntry.setStatus(_A)
_FsVMLocInfoVMMac_Type=MacAddress
_FsVMLocInfoVMMac_Object=MibTableColumn
fsVMLocInfoVMMac=_FsVMLocInfoVMMac_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7,1,1),_FsVMLocInfoVMMac_Type())
fsVMLocInfoVMMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMLocInfoVMMac.setStatus(_A)
_FsVMLocInfoPort_Type=IfIndex
_FsVMLocInfoPort_Object=MibTableColumn
fsVMLocInfoPort=_FsVMLocInfoPort_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7,1,2),_FsVMLocInfoPort_Type())
fsVMLocInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMLocInfoPort.setStatus(_A)
_FsVMLocInfoType_Type=Unsigned32
_FsVMLocInfoType_Object=MibTableColumn
fsVMLocInfoType=_FsVMLocInfoType_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7,1,3),_FsVMLocInfoType_Type())
fsVMLocInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMLocInfoType.setStatus(_A)
_FsVMLocInfoRowStatus_Type=RowStatus
_FsVMLocInfoRowStatus_Object=MibTableColumn
fsVMLocInfoRowStatus=_FsVMLocInfoRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,7,1,4),_FsVMLocInfoRowStatus_Type())
fsVMLocInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVMLocInfoRowStatus.setStatus(_A)
_FsVMPortInfoTable_Object=MibTable
fsVMPortInfoTable=_FsVMPortInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,8))
if mibBuilder.loadTexts:fsVMPortInfoTable.setStatus(_A)
_FsVMPortInfoEntry_Object=MibTableRow
fsVMPortInfoEntry=_FsVMPortInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,8,1))
fsVMPortInfoEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:fsVMPortInfoEntry.setStatus(_A)
_FsVMPortInfoPort_Type=IfIndex
_FsVMPortInfoPort_Object=MibTableColumn
fsVMPortInfoPort=_FsVMPortInfoPort_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,8,1,1),_FsVMPortInfoPort_Type())
fsVMPortInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMPortInfoPort.setStatus(_A)
_FsVMPortInfoStatus_Type=ConfigStatus
_FsVMPortInfoStatus_Object=MibTableColumn
fsVMPortInfoStatus=_FsVMPortInfoStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,8,1,2),_FsVMPortInfoStatus_Type())
fsVMPortInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMPortInfoStatus.setStatus(_A)
_FsVMPortInfoReflectStatus_Type=ConfigStatus
_FsVMPortInfoReflectStatus_Object=MibTableColumn
fsVMPortInfoReflectStatus=_FsVMPortInfoReflectStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,8,1,3),_FsVMPortInfoReflectStatus_Type())
fsVMPortInfoReflectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMPortInfoReflectStatus.setStatus(_A)
_FsVMPortTrapCfgTable_Object=MibTable
fsVMPortTrapCfgTable=_FsVMPortTrapCfgTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,9))
if mibBuilder.loadTexts:fsVMPortTrapCfgTable.setStatus(_A)
_FsVMPortTrapCfgEntry_Object=MibTableRow
fsVMPortTrapCfgEntry=_FsVMPortTrapCfgEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,9,1))
fsVMPortTrapCfgEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:fsVMPortTrapCfgEntry.setStatus(_A)
_FsVMPortTrapCfgPort_Type=IfIndex
_FsVMPortTrapCfgPort_Object=MibTableColumn
fsVMPortTrapCfgPort=_FsVMPortTrapCfgPort_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,9,1,1),_FsVMPortTrapCfgPort_Type())
fsVMPortTrapCfgPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMPortTrapCfgPort.setStatus(_A)
_FsVMPortTrapCfgNotifyStatus_Type=ConfigStatus
_FsVMPortTrapCfgNotifyStatus_Object=MibTableColumn
fsVMPortTrapCfgNotifyStatus=_FsVMPortTrapCfgNotifyStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,9,1,2),_FsVMPortTrapCfgNotifyStatus_Type())
fsVMPortTrapCfgNotifyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVMPortTrapCfgNotifyStatus.setStatus(_A)
_FsVMInfoChgTable_Object=MibTable
fsVMInfoChgTable=_FsVMInfoChgTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10))
if mibBuilder.loadTexts:fsVMInfoChgTable.setStatus(_A)
_FsVMInfoChgEntry_Object=MibTableRow
fsVMInfoChgEntry=_FsVMInfoChgEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1))
fsVMInfoChgEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsVMInfoChgEntry.setStatus(_A)
_FsVMInfoChgVMMac_Type=MacAddress
_FsVMInfoChgVMMac_Object=MibTableColumn
fsVMInfoChgVMMac=_FsVMInfoChgVMMac_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1,1),_FsVMInfoChgVMMac_Type())
fsVMInfoChgVMMac.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVMInfoChgVMMac.setStatus(_A)
_FsVMInfoChgVlan_Type=VlanId
_FsVMInfoChgVlan_Object=MibTableColumn
fsVMInfoChgVlan=_FsVMInfoChgVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1,2),_FsVMInfoChgVlan_Type())
fsVMInfoChgVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVMInfoChgVlan.setStatus(_A)
_FsVMInfoChgPort_Type=IfIndex
_FsVMInfoChgPort_Object=MibTableColumn
fsVMInfoChgPort=_FsVMInfoChgPort_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1,3),_FsVMInfoChgPort_Type())
fsVMInfoChgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVMInfoChgPort.setStatus(_A)
class _FsVMInfoChgAction_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVMInfoChgAction_Type.__name__=_E
_FsVMInfoChgAction_Object=MibTableColumn
fsVMInfoChgAction=_FsVMInfoChgAction_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1,4),_FsVMInfoChgAction_Type())
fsVMInfoChgAction.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVMInfoChgAction.setStatus(_A)
_FsVMInfoChgDate_Type=DateAndTime
_FsVMInfoChgDate_Object=MibTableColumn
fsVMInfoChgDate=_FsVMInfoChgDate_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,10,1,5),_FsVMInfoChgDate_Type())
fsVMInfoChgDate.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVMInfoChgDate.setStatus(_A)
_FsVMOuiInfoTable_Object=MibTable
fsVMOuiInfoTable=_FsVMOuiInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,11))
if mibBuilder.loadTexts:fsVMOuiInfoTable.setStatus(_A)
_FsVMOuiInfoEntry_Object=MibTableRow
fsVMOuiInfoEntry=_FsVMOuiInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,11,1))
fsVMOuiInfoEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:fsVMOuiInfoEntry.setStatus(_A)
_FsVMOuiInfoOui_Type=MacAddress
_FsVMOuiInfoOui_Object=MibTableColumn
fsVMOuiInfoOui=_FsVMOuiInfoOui_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,11,1,1),_FsVMOuiInfoOui_Type())
fsVMOuiInfoOui.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMOuiInfoOui.setStatus(_A)
_FsVMOuiInfoRowStatus_Type=RowStatus
_FsVMOuiInfoRowStatus_Object=MibTableColumn
fsVMOuiInfoRowStatus=_FsVMOuiInfoRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,11,1,2),_FsVMOuiInfoRowStatus_Type())
fsVMOuiInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVMOuiInfoRowStatus.setStatus(_A)
_FsVMRateMin_Type=Unsigned32
_FsVMRateMin_Object=MibScalar
fsVMRateMin=_FsVMRateMin_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,12),_FsVMRateMin_Type())
fsVMRateMin.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMRateMin.setStatus(_A)
_FsVMRateMax_Type=Unsigned32
_FsVMRateMax_Object=MibScalar
fsVMRateMax=_FsVMRateMax_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,13),_FsVMRateMax_Type())
fsVMRateMax.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMRateMax.setStatus(_A)
_FsVMBurstMin_Type=Unsigned32
_FsVMBurstMin_Object=MibScalar
fsVMBurstMin=_FsVMBurstMin_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,14),_FsVMBurstMin_Type())
fsVMBurstMin.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMBurstMin.setStatus(_A)
_FsVMBurstMax_Type=Unsigned32
_FsVMBurstMax_Object=MibScalar
fsVMBurstMax=_FsVMBurstMax_Object((1,3,6,1,4,1,52642,1,1,10,2,96,1,15),_FsVMBurstMax_Type())
fsVMBurstMax.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVMBurstMax.setStatus(_A)
_FsVMMIBTraps_ObjectIdentity=ObjectIdentity
fsVMMIBTraps=_FsVMMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,96,2))
_FsVMMIBConformance_ObjectIdentity=ObjectIdentity
fsVMMIBConformance=_FsVMMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,96,3))
_FsVMMIBCompliances_ObjectIdentity=ObjectIdentity
fsVMMIBCompliances=_FsVMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,96,3,1))
_FsVMMIBGroups_ObjectIdentity=ObjectIdentity
fsVMMIBGroups=_FsVMMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,96,3,2))
fsVMMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,96,3,2,1))
fsVMMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_K),(_B,_L),(_B,_d),(_B,_M),(_B,_e),(_B,_f),(_B,_g),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_O),(_B,_P),(_B,_r),(_B,_s),(_B,_Q),(_B,_t),(_B,_u),(_B,_R),(_B,_v),(_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_S),(_B,_w)))
if mibBuilder.loadTexts:fsVMMIBGroup.setStatus(_A)
fsVMsupMIBTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,96,2,1))
fsVMsupMIBTrap.setObjects(*((_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsVMsupMIBTrap.setStatus(_A)
fsVMMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,96,3,1,1))
fsVMMIBCompliance.setObjects((_B,_x))
if mibBuilder.loadTexts:fsVMMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsVMMIB':fsVMMIB,'fsVMMIBObjects':fsVMMIBObjects,_W:fsVMFuncVMSupport,_X:fsVMTrapCfgNotifyStatus,_Y:fsVMTrapCfgHistorySize,'fsVMInfoTable':fsVMInfoTable,'fsVMInfoEntry':fsVMInfoEntry,_K:fsVMInfoVMMac,_L:fsVMInfoVMGroup,_d:fsVMInfoRowStatus,'fsVMGroupInfoTable':fsVMGroupInfoTable,'fsVMGroupInfoEntry':fsVMGroupInfoEntry,_M:fsVMGroupInfoGroupName,_e:fsVMGroupInfoProfileCfg,_f:fsVMGroupInfoProfileName,_g:fsVMGroupInfoRowStatus,'fsVMProfileTable':fsVMProfileTable,'fsVMProfileEntry':fsVMProfileEntry,_N:fsVMProfileName,_h:fsVMProfileAclIn,_i:fsVMProfileAclOut,_j:fsVMProfileTxRate,_k:fsVMProfileTxBurst,_l:fsVMProfileRxRate,_m:fsVMProfileRxBurst,_n:fsVMProfileRowStatus,_o:fsVMProfileQosTrustMode,_p:fsVMProfileQosDefCos,_q:fsVMProfileQosRxPolicyMap,'fsVMLocInfoTable':fsVMLocInfoTable,'fsVMLocInfoEntry':fsVMLocInfoEntry,_O:fsVMLocInfoVMMac,_P:fsVMLocInfoPort,_r:fsVMLocInfoType,_s:fsVMLocInfoRowStatus,'fsVMPortInfoTable':fsVMPortInfoTable,'fsVMPortInfoEntry':fsVMPortInfoEntry,_Q:fsVMPortInfoPort,_t:fsVMPortInfoStatus,_u:fsVMPortInfoReflectStatus,'fsVMPortTrapCfgTable':fsVMPortTrapCfgTable,'fsVMPortTrapCfgEntry':fsVMPortTrapCfgEntry,_R:fsVMPortTrapCfgPort,_v:fsVMPortTrapCfgNotifyStatus,'fsVMInfoChgTable':fsVMInfoChgTable,'fsVMInfoChgEntry':fsVMInfoChgEntry,_H:fsVMInfoChgVMMac,_I:fsVMInfoChgVlan,_T:fsVMInfoChgPort,_U:fsVMInfoChgAction,_V:fsVMInfoChgDate,'fsVMOuiInfoTable':fsVMOuiInfoTable,'fsVMOuiInfoEntry':fsVMOuiInfoEntry,_S:fsVMOuiInfoOui,_w:fsVMOuiInfoRowStatus,_Z:fsVMRateMin,_a:fsVMRateMax,_b:fsVMBurstMin,_c:fsVMBurstMax,'fsVMMIBTraps':fsVMMIBTraps,'fsVMsupMIBTrap':fsVMsupMIBTrap,'fsVMMIBConformance':fsVMMIBConformance,'fsVMMIBCompliances':fsVMMIBCompliances,'fsVMMIBCompliance':fsVMMIBCompliance,'fsVMMIBGroups':fsVMMIBGroups,_x:fsVMMIBGroup})