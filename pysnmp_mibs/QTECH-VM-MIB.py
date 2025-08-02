_x='qtechVMMIBGroup'
_w='qtechVMOuiInfoRowStatus'
_v='qtechVMPortTrapCfgNotifyStatus'
_u='qtechVMPortInfoReflectStatus'
_t='qtechVMPortInfoStatus'
_s='qtechVMLocInfoRowStatus'
_r='qtechVMLocInfoType'
_q='qtechVMProfileQosRxPolicyMap'
_p='qtechVMProfileQosDefCos'
_o='qtechVMProfileQosTrustMode'
_n='qtechVMProfileRowStatus'
_m='qtechVMProfileRxBurst'
_l='qtechVMProfileRxRate'
_k='qtechVMProfileTxBurst'
_j='qtechVMProfileTxRate'
_i='qtechVMProfileAclOut'
_h='qtechVMProfileAclIn'
_g='qtechVMGroupInfoRowStatus'
_f='qtechVMGroupInfoProfileName'
_e='qtechVMGroupInfoProfileCfg'
_d='qtechVMInfoRowStatus'
_c='qtechVMBurstMax'
_b='qtechVMBurstMin'
_a='qtechVMRateMax'
_Z='qtechVMRateMin'
_Y='qtechVMTrapCfgHistorySize'
_X='qtechVMTrapCfgNotifyStatus'
_W='qtechVMFuncVMSupport'
_V='qtechVMInfoChgDate'
_U='qtechVMInfoChgAction'
_T='qtechVMInfoChgPort'
_S='qtechVMOuiInfoOui'
_R='qtechVMPortTrapCfgPort'
_Q='qtechVMPortInfoPort'
_P='qtechVMLocInfoPort'
_O='qtechVMLocInfoVMMac'
_N='qtechVMProfileName'
_M='qtechVMGroupInfoGroupName'
_L='qtechVMInfoVMGroup'
_K='qtechVMInfoVMMac'
_J='Integer32'
_I='qtechVMInfoChgVlan'
_H='qtechVMInfoChgVMMac'
_G='accessible-for-notify'
_F='read-create'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='QTECH-VM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechVMMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,96))
if mibBuilder.loadTexts:qtechVMMIB.setRevisions(('2012-08-22 00:00',))
_QtechVMMIBObjects_ObjectIdentity=ObjectIdentity
qtechVMMIBObjects=_QtechVMMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,96,1))
_QtechVMFuncVMSupport_Type=ConfigStatus
_QtechVMFuncVMSupport_Object=MibScalar
qtechVMFuncVMSupport=_QtechVMFuncVMSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,1),_QtechVMFuncVMSupport_Type())
qtechVMFuncVMSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMFuncVMSupport.setStatus(_A)
_QtechVMTrapCfgNotifyStatus_Type=ConfigStatus
_QtechVMTrapCfgNotifyStatus_Object=MibScalar
qtechVMTrapCfgNotifyStatus=_QtechVMTrapCfgNotifyStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,2),_QtechVMTrapCfgNotifyStatus_Type())
qtechVMTrapCfgNotifyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMTrapCfgNotifyStatus.setStatus(_A)
_QtechVMTrapCfgHistorySize_Type=Unsigned32
_QtechVMTrapCfgHistorySize_Object=MibScalar
qtechVMTrapCfgHistorySize=_QtechVMTrapCfgHistorySize_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,3),_QtechVMTrapCfgHistorySize_Type())
qtechVMTrapCfgHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMTrapCfgHistorySize.setStatus(_A)
_QtechVMInfoTable_Object=MibTable
qtechVMInfoTable=_QtechVMInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,4))
if mibBuilder.loadTexts:qtechVMInfoTable.setStatus(_A)
_QtechVMInfoEntry_Object=MibTableRow
qtechVMInfoEntry=_QtechVMInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,4,1))
qtechVMInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:qtechVMInfoEntry.setStatus(_A)
_QtechVMInfoVMMac_Type=MacAddress
_QtechVMInfoVMMac_Object=MibTableColumn
qtechVMInfoVMMac=_QtechVMInfoVMMac_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,4,1,1),_QtechVMInfoVMMac_Type())
qtechVMInfoVMMac.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMInfoVMMac.setStatus(_A)
_QtechVMInfoVMGroup_Type=Integer32
_QtechVMInfoVMGroup_Object=MibTableColumn
qtechVMInfoVMGroup=_QtechVMInfoVMGroup_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,4,1,2),_QtechVMInfoVMGroup_Type())
qtechVMInfoVMGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMInfoVMGroup.setStatus(_A)
_QtechVMInfoRowStatus_Type=RowStatus
_QtechVMInfoRowStatus_Object=MibTableColumn
qtechVMInfoRowStatus=_QtechVMInfoRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,4,1,3),_QtechVMInfoRowStatus_Type())
qtechVMInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechVMInfoRowStatus.setStatus(_A)
_QtechVMGroupInfoTable_Object=MibTable
qtechVMGroupInfoTable=_QtechVMGroupInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5))
if mibBuilder.loadTexts:qtechVMGroupInfoTable.setStatus(_A)
_QtechVMGroupInfoEntry_Object=MibTableRow
qtechVMGroupInfoEntry=_QtechVMGroupInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5,1))
qtechVMGroupInfoEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechVMGroupInfoEntry.setStatus(_A)
_QtechVMGroupInfoGroupName_Type=Integer32
_QtechVMGroupInfoGroupName_Object=MibTableColumn
qtechVMGroupInfoGroupName=_QtechVMGroupInfoGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5,1,1),_QtechVMGroupInfoGroupName_Type())
qtechVMGroupInfoGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMGroupInfoGroupName.setStatus(_A)
_QtechVMGroupInfoProfileCfg_Type=ConfigStatus
_QtechVMGroupInfoProfileCfg_Object=MibTableColumn
qtechVMGroupInfoProfileCfg=_QtechVMGroupInfoProfileCfg_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5,1,2),_QtechVMGroupInfoProfileCfg_Type())
qtechVMGroupInfoProfileCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMGroupInfoProfileCfg.setStatus(_A)
class _QtechVMGroupInfoProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVMGroupInfoProfileName_Type.__name__=_E
_QtechVMGroupInfoProfileName_Object=MibTableColumn
qtechVMGroupInfoProfileName=_QtechVMGroupInfoProfileName_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5,1,3),_QtechVMGroupInfoProfileName_Type())
qtechVMGroupInfoProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMGroupInfoProfileName.setStatus(_A)
_QtechVMGroupInfoRowStatus_Type=RowStatus
_QtechVMGroupInfoRowStatus_Object=MibTableColumn
qtechVMGroupInfoRowStatus=_QtechVMGroupInfoRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,5,1,4),_QtechVMGroupInfoRowStatus_Type())
qtechVMGroupInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechVMGroupInfoRowStatus.setStatus(_A)
_QtechVMProfileTable_Object=MibTable
qtechVMProfileTable=_QtechVMProfileTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6))
if mibBuilder.loadTexts:qtechVMProfileTable.setStatus(_A)
_QtechVMProfileEntry_Object=MibTableRow
qtechVMProfileEntry=_QtechVMProfileEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1))
qtechVMProfileEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qtechVMProfileEntry.setStatus(_A)
class _QtechVMProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVMProfileName_Type.__name__=_E
_QtechVMProfileName_Object=MibTableColumn
qtechVMProfileName=_QtechVMProfileName_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,1),_QtechVMProfileName_Type())
qtechVMProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMProfileName.setStatus(_A)
class _QtechVMProfileAclIn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_QtechVMProfileAclIn_Type.__name__=_E
_QtechVMProfileAclIn_Object=MibTableColumn
qtechVMProfileAclIn=_QtechVMProfileAclIn_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,2),_QtechVMProfileAclIn_Type())
qtechVMProfileAclIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileAclIn.setStatus(_A)
class _QtechVMProfileAclOut_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_QtechVMProfileAclOut_Type.__name__=_E
_QtechVMProfileAclOut_Object=MibTableColumn
qtechVMProfileAclOut=_QtechVMProfileAclOut_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,3),_QtechVMProfileAclOut_Type())
qtechVMProfileAclOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileAclOut.setStatus(_A)
_QtechVMProfileTxRate_Type=Unsigned32
_QtechVMProfileTxRate_Object=MibTableColumn
qtechVMProfileTxRate=_QtechVMProfileTxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,4),_QtechVMProfileTxRate_Type())
qtechVMProfileTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileTxRate.setStatus(_A)
_QtechVMProfileTxBurst_Type=Integer32
_QtechVMProfileTxBurst_Object=MibTableColumn
qtechVMProfileTxBurst=_QtechVMProfileTxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,5),_QtechVMProfileTxBurst_Type())
qtechVMProfileTxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileTxBurst.setStatus(_A)
_QtechVMProfileRxRate_Type=Unsigned32
_QtechVMProfileRxRate_Object=MibTableColumn
qtechVMProfileRxRate=_QtechVMProfileRxRate_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,6),_QtechVMProfileRxRate_Type())
qtechVMProfileRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileRxRate.setStatus(_A)
_QtechVMProfileRxBurst_Type=Integer32
_QtechVMProfileRxBurst_Object=MibTableColumn
qtechVMProfileRxBurst=_QtechVMProfileRxBurst_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,7),_QtechVMProfileRxBurst_Type())
qtechVMProfileRxBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileRxBurst.setStatus(_A)
_QtechVMProfileRowStatus_Type=RowStatus
_QtechVMProfileRowStatus_Object=MibTableColumn
qtechVMProfileRowStatus=_QtechVMProfileRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,8),_QtechVMProfileRowStatus_Type())
qtechVMProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechVMProfileRowStatus.setStatus(_A)
class _QtechVMProfileQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('not-trust',0),('trust-cos',1),('trust-dscp',2),('trust-ip-precedence',3)))
_QtechVMProfileQosTrustMode_Type.__name__=_J
_QtechVMProfileQosTrustMode_Object=MibTableColumn
qtechVMProfileQosTrustMode=_QtechVMProfileQosTrustMode_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,9),_QtechVMProfileQosTrustMode_Type())
qtechVMProfileQosTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileQosTrustMode.setStatus(_A)
class _QtechVMProfileQosDefCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('invalid',8))
_QtechVMProfileQosDefCos_Type.__name__=_J
_QtechVMProfileQosDefCos_Object=MibTableColumn
qtechVMProfileQosDefCos=_QtechVMProfileQosDefCos_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,10),_QtechVMProfileQosDefCos_Type())
qtechVMProfileQosDefCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileQosDefCos.setStatus(_A)
class _QtechVMProfileQosRxPolicyMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechVMProfileQosRxPolicyMap_Type.__name__=_E
_QtechVMProfileQosRxPolicyMap_Object=MibTableColumn
qtechVMProfileQosRxPolicyMap=_QtechVMProfileQosRxPolicyMap_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,6,1,11),_QtechVMProfileQosRxPolicyMap_Type())
qtechVMProfileQosRxPolicyMap.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMProfileQosRxPolicyMap.setStatus(_A)
_QtechVMLocInfoTable_Object=MibTable
qtechVMLocInfoTable=_QtechVMLocInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7))
if mibBuilder.loadTexts:qtechVMLocInfoTable.setStatus(_A)
_QtechVMLocInfoEntry_Object=MibTableRow
qtechVMLocInfoEntry=_QtechVMLocInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7,1))
qtechVMLocInfoEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:qtechVMLocInfoEntry.setStatus(_A)
_QtechVMLocInfoVMMac_Type=MacAddress
_QtechVMLocInfoVMMac_Object=MibTableColumn
qtechVMLocInfoVMMac=_QtechVMLocInfoVMMac_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7,1,1),_QtechVMLocInfoVMMac_Type())
qtechVMLocInfoVMMac.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMLocInfoVMMac.setStatus(_A)
_QtechVMLocInfoPort_Type=IfIndex
_QtechVMLocInfoPort_Object=MibTableColumn
qtechVMLocInfoPort=_QtechVMLocInfoPort_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7,1,2),_QtechVMLocInfoPort_Type())
qtechVMLocInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMLocInfoPort.setStatus(_A)
_QtechVMLocInfoType_Type=Unsigned32
_QtechVMLocInfoType_Object=MibTableColumn
qtechVMLocInfoType=_QtechVMLocInfoType_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7,1,3),_QtechVMLocInfoType_Type())
qtechVMLocInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMLocInfoType.setStatus(_A)
_QtechVMLocInfoRowStatus_Type=RowStatus
_QtechVMLocInfoRowStatus_Object=MibTableColumn
qtechVMLocInfoRowStatus=_QtechVMLocInfoRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,7,1,4),_QtechVMLocInfoRowStatus_Type())
qtechVMLocInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechVMLocInfoRowStatus.setStatus(_A)
_QtechVMPortInfoTable_Object=MibTable
qtechVMPortInfoTable=_QtechVMPortInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,8))
if mibBuilder.loadTexts:qtechVMPortInfoTable.setStatus(_A)
_QtechVMPortInfoEntry_Object=MibTableRow
qtechVMPortInfoEntry=_QtechVMPortInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,8,1))
qtechVMPortInfoEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qtechVMPortInfoEntry.setStatus(_A)
_QtechVMPortInfoPort_Type=IfIndex
_QtechVMPortInfoPort_Object=MibTableColumn
qtechVMPortInfoPort=_QtechVMPortInfoPort_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,8,1,1),_QtechVMPortInfoPort_Type())
qtechVMPortInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMPortInfoPort.setStatus(_A)
_QtechVMPortInfoStatus_Type=ConfigStatus
_QtechVMPortInfoStatus_Object=MibTableColumn
qtechVMPortInfoStatus=_QtechVMPortInfoStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,8,1,2),_QtechVMPortInfoStatus_Type())
qtechVMPortInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMPortInfoStatus.setStatus(_A)
_QtechVMPortInfoReflectStatus_Type=ConfigStatus
_QtechVMPortInfoReflectStatus_Object=MibTableColumn
qtechVMPortInfoReflectStatus=_QtechVMPortInfoReflectStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,8,1,3),_QtechVMPortInfoReflectStatus_Type())
qtechVMPortInfoReflectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMPortInfoReflectStatus.setStatus(_A)
_QtechVMPortTrapCfgTable_Object=MibTable
qtechVMPortTrapCfgTable=_QtechVMPortTrapCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,9))
if mibBuilder.loadTexts:qtechVMPortTrapCfgTable.setStatus(_A)
_QtechVMPortTrapCfgEntry_Object=MibTableRow
qtechVMPortTrapCfgEntry=_QtechVMPortTrapCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,9,1))
qtechVMPortTrapCfgEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:qtechVMPortTrapCfgEntry.setStatus(_A)
_QtechVMPortTrapCfgPort_Type=IfIndex
_QtechVMPortTrapCfgPort_Object=MibTableColumn
qtechVMPortTrapCfgPort=_QtechVMPortTrapCfgPort_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,9,1,1),_QtechVMPortTrapCfgPort_Type())
qtechVMPortTrapCfgPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMPortTrapCfgPort.setStatus(_A)
_QtechVMPortTrapCfgNotifyStatus_Type=ConfigStatus
_QtechVMPortTrapCfgNotifyStatus_Object=MibTableColumn
qtechVMPortTrapCfgNotifyStatus=_QtechVMPortTrapCfgNotifyStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,9,1,2),_QtechVMPortTrapCfgNotifyStatus_Type())
qtechVMPortTrapCfgNotifyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVMPortTrapCfgNotifyStatus.setStatus(_A)
_QtechVMInfoChgTable_Object=MibTable
qtechVMInfoChgTable=_QtechVMInfoChgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10))
if mibBuilder.loadTexts:qtechVMInfoChgTable.setStatus(_A)
_QtechVMInfoChgEntry_Object=MibTableRow
qtechVMInfoChgEntry=_QtechVMInfoChgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1))
qtechVMInfoChgEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechVMInfoChgEntry.setStatus(_A)
_QtechVMInfoChgVMMac_Type=MacAddress
_QtechVMInfoChgVMMac_Object=MibTableColumn
qtechVMInfoChgVMMac=_QtechVMInfoChgVMMac_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1,1),_QtechVMInfoChgVMMac_Type())
qtechVMInfoChgVMMac.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechVMInfoChgVMMac.setStatus(_A)
_QtechVMInfoChgVlan_Type=VlanId
_QtechVMInfoChgVlan_Object=MibTableColumn
qtechVMInfoChgVlan=_QtechVMInfoChgVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1,2),_QtechVMInfoChgVlan_Type())
qtechVMInfoChgVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechVMInfoChgVlan.setStatus(_A)
_QtechVMInfoChgPort_Type=IfIndex
_QtechVMInfoChgPort_Object=MibTableColumn
qtechVMInfoChgPort=_QtechVMInfoChgPort_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1,3),_QtechVMInfoChgPort_Type())
qtechVMInfoChgPort.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechVMInfoChgPort.setStatus(_A)
class _QtechVMInfoChgAction_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVMInfoChgAction_Type.__name__=_E
_QtechVMInfoChgAction_Object=MibTableColumn
qtechVMInfoChgAction=_QtechVMInfoChgAction_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1,4),_QtechVMInfoChgAction_Type())
qtechVMInfoChgAction.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechVMInfoChgAction.setStatus(_A)
_QtechVMInfoChgDate_Type=DateAndTime
_QtechVMInfoChgDate_Object=MibTableColumn
qtechVMInfoChgDate=_QtechVMInfoChgDate_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,10,1,5),_QtechVMInfoChgDate_Type())
qtechVMInfoChgDate.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechVMInfoChgDate.setStatus(_A)
_QtechVMOuiInfoTable_Object=MibTable
qtechVMOuiInfoTable=_QtechVMOuiInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,11))
if mibBuilder.loadTexts:qtechVMOuiInfoTable.setStatus(_A)
_QtechVMOuiInfoEntry_Object=MibTableRow
qtechVMOuiInfoEntry=_QtechVMOuiInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,11,1))
qtechVMOuiInfoEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:qtechVMOuiInfoEntry.setStatus(_A)
_QtechVMOuiInfoOui_Type=MacAddress
_QtechVMOuiInfoOui_Object=MibTableColumn
qtechVMOuiInfoOui=_QtechVMOuiInfoOui_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,11,1,1),_QtechVMOuiInfoOui_Type())
qtechVMOuiInfoOui.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMOuiInfoOui.setStatus(_A)
_QtechVMOuiInfoRowStatus_Type=RowStatus
_QtechVMOuiInfoRowStatus_Object=MibTableColumn
qtechVMOuiInfoRowStatus=_QtechVMOuiInfoRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,11,1,2),_QtechVMOuiInfoRowStatus_Type())
qtechVMOuiInfoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechVMOuiInfoRowStatus.setStatus(_A)
_QtechVMRateMin_Type=Unsigned32
_QtechVMRateMin_Object=MibScalar
qtechVMRateMin=_QtechVMRateMin_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,12),_QtechVMRateMin_Type())
qtechVMRateMin.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMRateMin.setStatus(_A)
_QtechVMRateMax_Type=Unsigned32
_QtechVMRateMax_Object=MibScalar
qtechVMRateMax=_QtechVMRateMax_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,13),_QtechVMRateMax_Type())
qtechVMRateMax.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMRateMax.setStatus(_A)
_QtechVMBurstMin_Type=Unsigned32
_QtechVMBurstMin_Object=MibScalar
qtechVMBurstMin=_QtechVMBurstMin_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,14),_QtechVMBurstMin_Type())
qtechVMBurstMin.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMBurstMin.setStatus(_A)
_QtechVMBurstMax_Type=Unsigned32
_QtechVMBurstMax_Object=MibScalar
qtechVMBurstMax=_QtechVMBurstMax_Object((1,3,6,1,4,1,27514,1,1,10,2,96,1,15),_QtechVMBurstMax_Type())
qtechVMBurstMax.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVMBurstMax.setStatus(_A)
_QtechVMMIBTraps_ObjectIdentity=ObjectIdentity
qtechVMMIBTraps=_QtechVMMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,96,2))
_QtechVMMIBConformance_ObjectIdentity=ObjectIdentity
qtechVMMIBConformance=_QtechVMMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,96,3))
_QtechVMMIBCompliances_ObjectIdentity=ObjectIdentity
qtechVMMIBCompliances=_QtechVMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,96,3,1))
_QtechVMMIBGroups_ObjectIdentity=ObjectIdentity
qtechVMMIBGroups=_QtechVMMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,96,3,2))
qtechVMMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,96,3,2,1))
qtechVMMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_K),(_B,_L),(_B,_d),(_B,_M),(_B,_e),(_B,_f),(_B,_g),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_O),(_B,_P),(_B,_r),(_B,_s),(_B,_Q),(_B,_t),(_B,_u),(_B,_R),(_B,_v),(_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_S),(_B,_w)))
if mibBuilder.loadTexts:qtechVMMIBGroup.setStatus(_A)
qtechVMsupMIBTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,96,2,1))
qtechVMsupMIBTrap.setObjects(*((_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechVMsupMIBTrap.setStatus(_A)
qtechVMMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,96,3,1,1))
qtechVMMIBCompliance.setObjects((_B,_x))
if mibBuilder.loadTexts:qtechVMMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechVMMIB':qtechVMMIB,'qtechVMMIBObjects':qtechVMMIBObjects,_W:qtechVMFuncVMSupport,_X:qtechVMTrapCfgNotifyStatus,_Y:qtechVMTrapCfgHistorySize,'qtechVMInfoTable':qtechVMInfoTable,'qtechVMInfoEntry':qtechVMInfoEntry,_K:qtechVMInfoVMMac,_L:qtechVMInfoVMGroup,_d:qtechVMInfoRowStatus,'qtechVMGroupInfoTable':qtechVMGroupInfoTable,'qtechVMGroupInfoEntry':qtechVMGroupInfoEntry,_M:qtechVMGroupInfoGroupName,_e:qtechVMGroupInfoProfileCfg,_f:qtechVMGroupInfoProfileName,_g:qtechVMGroupInfoRowStatus,'qtechVMProfileTable':qtechVMProfileTable,'qtechVMProfileEntry':qtechVMProfileEntry,_N:qtechVMProfileName,_h:qtechVMProfileAclIn,_i:qtechVMProfileAclOut,_j:qtechVMProfileTxRate,_k:qtechVMProfileTxBurst,_l:qtechVMProfileRxRate,_m:qtechVMProfileRxBurst,_n:qtechVMProfileRowStatus,_o:qtechVMProfileQosTrustMode,_p:qtechVMProfileQosDefCos,_q:qtechVMProfileQosRxPolicyMap,'qtechVMLocInfoTable':qtechVMLocInfoTable,'qtechVMLocInfoEntry':qtechVMLocInfoEntry,_O:qtechVMLocInfoVMMac,_P:qtechVMLocInfoPort,_r:qtechVMLocInfoType,_s:qtechVMLocInfoRowStatus,'qtechVMPortInfoTable':qtechVMPortInfoTable,'qtechVMPortInfoEntry':qtechVMPortInfoEntry,_Q:qtechVMPortInfoPort,_t:qtechVMPortInfoStatus,_u:qtechVMPortInfoReflectStatus,'qtechVMPortTrapCfgTable':qtechVMPortTrapCfgTable,'qtechVMPortTrapCfgEntry':qtechVMPortTrapCfgEntry,_R:qtechVMPortTrapCfgPort,_v:qtechVMPortTrapCfgNotifyStatus,'qtechVMInfoChgTable':qtechVMInfoChgTable,'qtechVMInfoChgEntry':qtechVMInfoChgEntry,_H:qtechVMInfoChgVMMac,_I:qtechVMInfoChgVlan,_T:qtechVMInfoChgPort,_U:qtechVMInfoChgAction,_V:qtechVMInfoChgDate,'qtechVMOuiInfoTable':qtechVMOuiInfoTable,'qtechVMOuiInfoEntry':qtechVMOuiInfoEntry,_S:qtechVMOuiInfoOui,_w:qtechVMOuiInfoRowStatus,_Z:qtechVMRateMin,_a:qtechVMRateMax,_b:qtechVMBurstMin,_c:qtechVMBurstMax,'qtechVMMIBTraps':qtechVMMIBTraps,'qtechVMsupMIBTrap':qtechVMsupMIBTrap,'qtechVMMIBConformance':qtechVMMIBConformance,'qtechVMMIBCompliances':qtechVMMIBCompliances,'qtechVMMIBCompliance':qtechVMMIBCompliance,'qtechVMMIBGroups':qtechVMMIBGroups,_x:qtechVMMIBGroup})