_d='fdryVplsEntry'
_c='fdryVplsEndPoint2IfIndex'
_b='fdryVplsEndPoint2InnerTag'
_a='fdryVplsEndPoint2InnerTagType'
_Z='fdryVplsEndPoint2VlanId'
_Y='fdryVplsEndPointIfIndex'
_X='fdryVplsEndPointPortVlan'
_W='fdryVllEndPointServiceType'
_V='forwarding'
_U='blocking'
_T='disabled'
_S='PwVlanCfg'
_R='pwName'
_Q='pwIndex'
_P='fdryPwServiceType'
_O='pwEnetPwInstance'
_N='FOUNDRY-PW-ENET-STD-MIB'
_M='fdryVplsVcId'
_L='ClassOfService'
_K='vplsConfigName'
_J='vplsConfigIndex'
_I='Integer32'
_H='VPLS-GENERIC-DRAFT-01-MIB'
_G='FOUNDRY-PW-STD-MIB'
_F='not-accessible'
_E='deprecated'
_D='FDRY-MPLS-L2VPN-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pwEnetPwInstance,=mibBuilder.importSymbols(_N,_O)
fdryPwServiceType,pwID,pwIndex,pwName=mibBuilder.importSymbols(_G,_P,'pwID',_Q,_R)
PwOperStatusTC,PwVlanCfg=mibBuilder.importSymbols('FOUNDRY-PW-TC-STD-MIB','PwOperStatusTC',_S)
snMpls,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','snMpls')
VlanTagMode,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','VlanTagMode')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
vplsConfigEntry,vplsConfigIndex,vplsConfigName=mibBuilder.importSymbols(_H,'vplsConfigEntry',_J,_K)
fdryMplsL2VpnMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,2,15,2))
if mibBuilder.loadTexts:fdryMplsL2VpnMIB.setRevisions(('2008-02-07 00:00','2017-08-07 00:00'))
class MplsServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vll',1),('vllLocal',2),('vpls',3)))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
class ClassOfService(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
class Layer2StateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_T,1),(_U,2),('listening',3),('learning',4),('preforwarding',5),(_V,6)))
_FdryMplsVpnNotifications_ObjectIdentity=ObjectIdentity
fdryMplsVpnNotifications=_FdryMplsVpnNotifications_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,2,0))
_FdryMplsVllInfo_ObjectIdentity=ObjectIdentity
fdryMplsVllInfo=_FdryMplsVllInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,2,1))
_FdryVllEndPointTable_Object=MibTable
fdryVllEndPointTable=_FdryVllEndPointTable_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1))
if mibBuilder.loadTexts:fdryVllEndPointTable.setStatus(_A)
_FdryVllEndPointEntry_Object=MibTableRow
fdryVllEndPointEntry=_FdryVllEndPointEntry_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1))
fdryVllEndPointEntry.setIndexNames((0,_D,_W),(0,_G,_Q),(0,_N,_O))
if mibBuilder.loadTexts:fdryVllEndPointEntry.setStatus(_A)
_FdryVllEndPointServiceType_Type=MplsServiceType
_FdryVllEndPointServiceType_Object=MibTableColumn
fdryVllEndPointServiceType=_FdryVllEndPointServiceType_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,1),_FdryVllEndPointServiceType_Type())
fdryVllEndPointServiceType.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVllEndPointServiceType.setStatus(_A)
_FdryVllEndPointVlanTagMode_Type=VlanTagMode
_FdryVllEndPointVlanTagMode_Object=MibTableColumn
fdryVllEndPointVlanTagMode=_FdryVllEndPointVlanTagMode_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,2),_FdryVllEndPointVlanTagMode_Type())
fdryVllEndPointVlanTagMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVllEndPointVlanTagMode.setStatus(_A)
class _FdryVllEndPointClassOfService_Type(ClassOfService):defaultValue=0
_FdryVllEndPointClassOfService_Type.__name__=_L
_FdryVllEndPointClassOfService_Object=MibTableColumn
fdryVllEndPointClassOfService=_FdryVllEndPointClassOfService_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,3),_FdryVllEndPointClassOfService_Type())
fdryVllEndPointClassOfService.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVllEndPointClassOfService.setStatus(_A)
_FdryVllEndPointInHCPkts_Type=Counter64
_FdryVllEndPointInHCPkts_Object=MibTableColumn
fdryVllEndPointInHCPkts=_FdryVllEndPointInHCPkts_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,4),_FdryVllEndPointInHCPkts_Type())
fdryVllEndPointInHCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVllEndPointInHCPkts.setStatus(_A)
_FdryVllEndPointOutHCPkts_Type=Counter64
_FdryVllEndPointOutHCPkts_Object=MibTableColumn
fdryVllEndPointOutHCPkts=_FdryVllEndPointOutHCPkts_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,5),_FdryVllEndPointOutHCPkts_Type())
fdryVllEndPointOutHCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVllEndPointOutHCPkts.setStatus(_A)
_FdryVllEndPointAdminStatus_Type=AdminStatus
_FdryVllEndPointAdminStatus_Object=MibTableColumn
fdryVllEndPointAdminStatus=_FdryVllEndPointAdminStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,6),_FdryVllEndPointAdminStatus_Type())
fdryVllEndPointAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVllEndPointAdminStatus.setStatus(_A)
_FdryVllEndPointOperStatus_Type=PwOperStatusTC
_FdryVllEndPointOperStatus_Object=MibTableColumn
fdryVllEndPointOperStatus=_FdryVllEndPointOperStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,7),_FdryVllEndPointOperStatus_Type())
fdryVllEndPointOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVllEndPointOperStatus.setStatus(_A)
_FdryVllEndPointRowStatus_Type=RowStatus
_FdryVllEndPointRowStatus_Object=MibTableColumn
fdryVllEndPointRowStatus=_FdryVllEndPointRowStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,8),_FdryVllEndPointRowStatus_Type())
fdryVllEndPointRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVllEndPointRowStatus.setStatus(_A)
class _FdryVllEndPointInnerVlanId_Type(PwVlanCfg):defaultValue=0
_FdryVllEndPointInnerVlanId_Type.__name__=_S
_FdryVllEndPointInnerVlanId_Object=MibTableColumn
fdryVllEndPointInnerVlanId=_FdryVllEndPointInnerVlanId_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,9),_FdryVllEndPointInnerVlanId_Type())
fdryVllEndPointInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVllEndPointInnerVlanId.setStatus(_A)
_FdryVllEndPointInHCOctets_Type=Counter64
_FdryVllEndPointInHCOctets_Object=MibTableColumn
fdryVllEndPointInHCOctets=_FdryVllEndPointInHCOctets_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,10),_FdryVllEndPointInHCOctets_Type())
fdryVllEndPointInHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVllEndPointInHCOctets.setStatus(_A)
_FdryVllEndPointOutHCOctets_Type=Counter64
_FdryVllEndPointOutHCOctets_Object=MibTableColumn
fdryVllEndPointOutHCOctets=_FdryVllEndPointOutHCOctets_Object((1,3,6,1,4,1,1991,1,2,15,2,1,1,1,11),_FdryVllEndPointOutHCOctets_Type())
fdryVllEndPointOutHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVllEndPointOutHCOctets.setStatus(_A)
_FdryMplsVplsInfo_ObjectIdentity=ObjectIdentity
fdryMplsVplsInfo=_FdryMplsVplsInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,2,2))
_FdryVplsEndPointTable_Object=MibTable
fdryVplsEndPointTable=_FdryVplsEndPointTable_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1))
if mibBuilder.loadTexts:fdryVplsEndPointTable.setStatus(_E)
_FdryVplsEndPointEntry_Object=MibTableRow
fdryVplsEndPointEntry=_FdryVplsEndPointEntry_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1))
fdryVplsEndPointEntry.setIndexNames((0,_H,_J),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:fdryVplsEndPointEntry.setStatus(_E)
_FdryVplsEndPointPortVlan_Type=PwVlanCfg
_FdryVplsEndPointPortVlan_Object=MibTableColumn
fdryVplsEndPointPortVlan=_FdryVplsEndPointPortVlan_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,1),_FdryVplsEndPointPortVlan_Type())
fdryVplsEndPointPortVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPointPortVlan.setStatus(_E)
_FdryVplsEndPointIfIndex_Type=InterfaceIndex
_FdryVplsEndPointIfIndex_Object=MibTableColumn
fdryVplsEndPointIfIndex=_FdryVplsEndPointIfIndex_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,2),_FdryVplsEndPointIfIndex_Type())
fdryVplsEndPointIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPointIfIndex.setStatus(_E)
_FdryVplsEndPointVlanTagMode_Type=VlanTagMode
_FdryVplsEndPointVlanTagMode_Object=MibTableColumn
fdryVplsEndPointVlanTagMode=_FdryVplsEndPointVlanTagMode_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,3),_FdryVplsEndPointVlanTagMode_Type())
fdryVplsEndPointVlanTagMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsEndPointVlanTagMode.setStatus(_E)
_FdryVplsEndPointOutHCPkts_Type=Counter64
_FdryVplsEndPointOutHCPkts_Object=MibTableColumn
fdryVplsEndPointOutHCPkts=_FdryVplsEndPointOutHCPkts_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,4),_FdryVplsEndPointOutHCPkts_Type())
fdryVplsEndPointOutHCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPointOutHCPkts.setStatus(_E)
class _FdryVplsEndPointState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,5)))
_FdryVplsEndPointState_Type.__name__=_I
_FdryVplsEndPointState_Object=MibTableColumn
fdryVplsEndPointState=_FdryVplsEndPointState_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,5),_FdryVplsEndPointState_Type())
fdryVplsEndPointState.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPointState.setStatus(_E)
_FdryVplsEndPointAdminStatus_Type=AdminStatus
_FdryVplsEndPointAdminStatus_Object=MibTableColumn
fdryVplsEndPointAdminStatus=_FdryVplsEndPointAdminStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,6),_FdryVplsEndPointAdminStatus_Type())
fdryVplsEndPointAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsEndPointAdminStatus.setStatus(_E)
_FdryVplsEndPointOperStatus_Type=PwOperStatusTC
_FdryVplsEndPointOperStatus_Object=MibTableColumn
fdryVplsEndPointOperStatus=_FdryVplsEndPointOperStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,7),_FdryVplsEndPointOperStatus_Type())
fdryVplsEndPointOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPointOperStatus.setStatus(_E)
_FdryVplsEndPointRowStatus_Type=RowStatus
_FdryVplsEndPointRowStatus_Object=MibTableColumn
fdryVplsEndPointRowStatus=_FdryVplsEndPointRowStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,8),_FdryVplsEndPointRowStatus_Type())
fdryVplsEndPointRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsEndPointRowStatus.setStatus(_E)
_FdryVplsEndPointInHCOctets_Type=Counter64
_FdryVplsEndPointInHCOctets_Object=MibTableColumn
fdryVplsEndPointInHCOctets=_FdryVplsEndPointInHCOctets_Object((1,3,6,1,4,1,1991,1,2,15,2,2,1,1,9),_FdryVplsEndPointInHCOctets_Type())
fdryVplsEndPointInHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPointInHCOctets.setStatus(_E)
_FdryVplsTable_Object=MibTable
fdryVplsTable=_FdryVplsTable_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2))
if mibBuilder.loadTexts:fdryVplsTable.setStatus(_A)
_FdryVplsEntry_Object=MibTableRow
fdryVplsEntry=_FdryVplsEntry_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2,1))
if mibBuilder.loadTexts:fdryVplsEntry.setStatus(_A)
class _FdryVplsClassOfService_Type(ClassOfService):defaultValue=0
_FdryVplsClassOfService_Type.__name__=_L
_FdryVplsClassOfService_Object=MibTableColumn
fdryVplsClassOfService=_FdryVplsClassOfService_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2,1,1),_FdryVplsClassOfService_Type())
fdryVplsClassOfService.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsClassOfService.setStatus(_A)
_FdryVplsMaxMacLearned_Type=Unsigned32
_FdryVplsMaxMacLearned_Object=MibTableColumn
fdryVplsMaxMacLearned=_FdryVplsMaxMacLearned_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2,1,2),_FdryVplsMaxMacLearned_Type())
fdryVplsMaxMacLearned.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsMaxMacLearned.setStatus(_A)
_FdryVplsClearMac_Type=TruthValue
_FdryVplsClearMac_Object=MibTableColumn
fdryVplsClearMac=_FdryVplsClearMac_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2,1,3),_FdryVplsClearMac_Type())
fdryVplsClearMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsClearMac.setStatus(_A)
_FdryVplsVcId_Type=Unsigned32
_FdryVplsVcId_Object=MibTableColumn
fdryVplsVcId=_FdryVplsVcId_Object((1,3,6,1,4,1,1991,1,2,15,2,2,2,1,4),_FdryVplsVcId_Type())
fdryVplsVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsVcId.setStatus(_A)
_FdryVplsEndPoint2Table_Object=MibTable
fdryVplsEndPoint2Table=_FdryVplsEndPoint2Table_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3))
if mibBuilder.loadTexts:fdryVplsEndPoint2Table.setStatus(_A)
_FdryVplsEndPoint2Entry_Object=MibTableRow
fdryVplsEndPoint2Entry=_FdryVplsEndPoint2Entry_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1))
fdryVplsEndPoint2Entry.setIndexNames((0,_H,_J),(0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:fdryVplsEndPoint2Entry.setStatus(_A)
_FdryVplsEndPoint2VlanId_Type=PwVlanCfg
_FdryVplsEndPoint2VlanId_Object=MibTableColumn
fdryVplsEndPoint2VlanId=_FdryVplsEndPoint2VlanId_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,1),_FdryVplsEndPoint2VlanId_Type())
fdryVplsEndPoint2VlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPoint2VlanId.setStatus(_A)
class _FdryVplsEndPoint2InnerTagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('innerVlan',2),('isid',3)))
_FdryVplsEndPoint2InnerTagType_Type.__name__=_I
_FdryVplsEndPoint2InnerTagType_Object=MibTableColumn
fdryVplsEndPoint2InnerTagType=_FdryVplsEndPoint2InnerTagType_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,2),_FdryVplsEndPoint2InnerTagType_Type())
fdryVplsEndPoint2InnerTagType.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPoint2InnerTagType.setStatus(_A)
_FdryVplsEndPoint2InnerTag_Type=Unsigned32
_FdryVplsEndPoint2InnerTag_Object=MibTableColumn
fdryVplsEndPoint2InnerTag=_FdryVplsEndPoint2InnerTag_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,3),_FdryVplsEndPoint2InnerTag_Type())
fdryVplsEndPoint2InnerTag.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPoint2InnerTag.setStatus(_A)
_FdryVplsEndPoint2IfIndex_Type=InterfaceIndex
_FdryVplsEndPoint2IfIndex_Object=MibTableColumn
fdryVplsEndPoint2IfIndex=_FdryVplsEndPoint2IfIndex_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,4),_FdryVplsEndPoint2IfIndex_Type())
fdryVplsEndPoint2IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fdryVplsEndPoint2IfIndex.setStatus(_A)
_FdryVplsEndPoint2VlanTagMode_Type=VlanTagMode
_FdryVplsEndPoint2VlanTagMode_Object=MibTableColumn
fdryVplsEndPoint2VlanTagMode=_FdryVplsEndPoint2VlanTagMode_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,5),_FdryVplsEndPoint2VlanTagMode_Type())
fdryVplsEndPoint2VlanTagMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsEndPoint2VlanTagMode.setStatus(_A)
_FdryVplsEndPoint2InHCOctets_Type=Counter64
_FdryVplsEndPoint2InHCOctets_Object=MibTableColumn
fdryVplsEndPoint2InHCOctets=_FdryVplsEndPoint2InHCOctets_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,6),_FdryVplsEndPoint2InHCOctets_Type())
fdryVplsEndPoint2InHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPoint2InHCOctets.setStatus(_A)
_FdryVplsEndPoint2Layer2State_Type=Layer2StateTC
_FdryVplsEndPoint2Layer2State_Object=MibTableColumn
fdryVplsEndPoint2Layer2State=_FdryVplsEndPoint2Layer2State_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,7),_FdryVplsEndPoint2Layer2State_Type())
fdryVplsEndPoint2Layer2State.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPoint2Layer2State.setStatus(_A)
_FdryVplsEndPoint2OperStatus_Type=PwOperStatusTC
_FdryVplsEndPoint2OperStatus_Object=MibTableColumn
fdryVplsEndPoint2OperStatus=_FdryVplsEndPoint2OperStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,8),_FdryVplsEndPoint2OperStatus_Type())
fdryVplsEndPoint2OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryVplsEndPoint2OperStatus.setStatus(_A)
_FdryVplsEndPoint2RowStatus_Type=RowStatus
_FdryVplsEndPoint2RowStatus_Object=MibTableColumn
fdryVplsEndPoint2RowStatus=_FdryVplsEndPoint2RowStatus_Object((1,3,6,1,4,1,1991,1,2,15,2,2,3,1,9),_FdryVplsEndPoint2RowStatus_Type())
fdryVplsEndPoint2RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryVplsEndPoint2RowStatus.setStatus(_A)
vplsConfigEntry.registerAugmentions((_D,_d))
fdryVplsEntry.setIndexNames(*vplsConfigEntry.getIndexNames())
fdryVplsCreated=NotificationType((1,3,6,1,4,1,1991,1,2,15,2,0,1))
fdryVplsCreated.setObjects(*((_H,_K),(_D,_M)))
if mibBuilder.loadTexts:fdryVplsCreated.setStatus(_A)
fdryVplsDeleted=NotificationType((1,3,6,1,4,1,1991,1,2,15,2,0,2))
fdryVplsDeleted.setObjects(*((_H,_K),(_D,_M)))
if mibBuilder.loadTexts:fdryVplsDeleted.setStatus(_A)
fdryPwCreated=NotificationType((1,3,6,1,4,1,1991,1,2,15,2,0,3))
fdryPwCreated.setObjects(*((_G,_P),(_G,_R),(_G,'pwID')))
if mibBuilder.loadTexts:fdryPwCreated.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MplsServiceType':MplsServiceType,'AdminStatus':AdminStatus,_L:ClassOfService,'Layer2StateTC':Layer2StateTC,'fdryMplsL2VpnMIB':fdryMplsL2VpnMIB,'fdryMplsVpnNotifications':fdryMplsVpnNotifications,'fdryVplsCreated':fdryVplsCreated,'fdryVplsDeleted':fdryVplsDeleted,'fdryPwCreated':fdryPwCreated,'fdryMplsVllInfo':fdryMplsVllInfo,'fdryVllEndPointTable':fdryVllEndPointTable,'fdryVllEndPointEntry':fdryVllEndPointEntry,_W:fdryVllEndPointServiceType,'fdryVllEndPointVlanTagMode':fdryVllEndPointVlanTagMode,'fdryVllEndPointClassOfService':fdryVllEndPointClassOfService,'fdryVllEndPointInHCPkts':fdryVllEndPointInHCPkts,'fdryVllEndPointOutHCPkts':fdryVllEndPointOutHCPkts,'fdryVllEndPointAdminStatus':fdryVllEndPointAdminStatus,'fdryVllEndPointOperStatus':fdryVllEndPointOperStatus,'fdryVllEndPointRowStatus':fdryVllEndPointRowStatus,'fdryVllEndPointInnerVlanId':fdryVllEndPointInnerVlanId,'fdryVllEndPointInHCOctets':fdryVllEndPointInHCOctets,'fdryVllEndPointOutHCOctets':fdryVllEndPointOutHCOctets,'fdryMplsVplsInfo':fdryMplsVplsInfo,'fdryVplsEndPointTable':fdryVplsEndPointTable,'fdryVplsEndPointEntry':fdryVplsEndPointEntry,_X:fdryVplsEndPointPortVlan,_Y:fdryVplsEndPointIfIndex,'fdryVplsEndPointVlanTagMode':fdryVplsEndPointVlanTagMode,'fdryVplsEndPointOutHCPkts':fdryVplsEndPointOutHCPkts,'fdryVplsEndPointState':fdryVplsEndPointState,'fdryVplsEndPointAdminStatus':fdryVplsEndPointAdminStatus,'fdryVplsEndPointOperStatus':fdryVplsEndPointOperStatus,'fdryVplsEndPointRowStatus':fdryVplsEndPointRowStatus,'fdryVplsEndPointInHCOctets':fdryVplsEndPointInHCOctets,'fdryVplsTable':fdryVplsTable,_d:fdryVplsEntry,'fdryVplsClassOfService':fdryVplsClassOfService,'fdryVplsMaxMacLearned':fdryVplsMaxMacLearned,'fdryVplsClearMac':fdryVplsClearMac,_M:fdryVplsVcId,'fdryVplsEndPoint2Table':fdryVplsEndPoint2Table,'fdryVplsEndPoint2Entry':fdryVplsEndPoint2Entry,_Z:fdryVplsEndPoint2VlanId,_a:fdryVplsEndPoint2InnerTagType,_b:fdryVplsEndPoint2InnerTag,_c:fdryVplsEndPoint2IfIndex,'fdryVplsEndPoint2VlanTagMode':fdryVplsEndPoint2VlanTagMode,'fdryVplsEndPoint2InHCOctets':fdryVplsEndPoint2InHCOctets,'fdryVplsEndPoint2Layer2State':fdryVplsEndPoint2Layer2State,'fdryVplsEndPoint2OperStatus':fdryVplsEndPoint2OperStatus,'fdryVplsEndPoint2RowStatus':fdryVplsEndPoint2RowStatus})