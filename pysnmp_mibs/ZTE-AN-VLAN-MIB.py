_A0='zxAnVlanBasedForwardCVid'
_z='zxAnVlanBasedForwardSVid'
_y='zxAnVlanIfCosMapCos'
_x='zxAnVlanRuledTransCVid'
_w='zxAnVlanRuledTransSVid'
_v='zxAnVlanTagSlot'
_u='zxAnVlanTagShelf'
_t='zxAnVlanCtag'
_s='zxAnVlanStag'
_r='zxAnMVlanGlobalTransMVid'
_q='zxAnIeee1588Vlan'
_p='zxAnVlanTpidCVlanId'
_o='zxAnVlanTpidSVlanId'
_n='zxAnVlanExQinQOnuGroupId'
_m='zxAnVlanExQinQPonPortIndex'
_l='zxAnInternalVlanServiceType'
_k='zxAnProtocolVlanPortIfIndex'
_j='zxAnPortMvlanTranslateCvlan'
_i='zxAnPortMvlanTranslateMvlan'
_h='zxAnPortMvlanTranslateIfIndex'
_g='zxAnVlanInterfaceVlanId'
_f='zxAnIpRouteVlan'
_e='zxAnOnuMngVlan'
_d='0x8100'
_c='zxAnXconnectLocationIndex'
_b='zxAnXconnectPortIndex'
_a='zxAnEtherProtocolType'
_Z='zxAnProtocolVlanPortIndex'
_Y='zxAnVlanExTranslatePortIndex'
_X='zxAnVlanExQinQPortIndex'
_W='zxAnVlanVoipVlanId'
_V='zxAnVlanExQinQSessionNo'
_U='zxAnVlanGlobalTransSessionNo'
_T='zxAnSlotIndex'
_S='zxAnShelfIndex'
_R='zxAnVlanIndex'
_Q='zxAnVlanIfTransUserVid'
_P='zxAnVlanTranslatePortId'
_O='hybrid'
_N='TruthValue'
_M='Bits'
_L='zxAnVlanId'
_K='zxAnVlanPortIndex'
_J='DisplayString'
_I='disable'
_H='enable'
_G='read-only'
_F='read-write'
_E='not-accessible'
_D='ZTE-AN-VLAN-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention',_N)
VlanId,ZxAnIfindex,ZxAnPortList,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId','ZxAnIfindex','ZxAnPortList','zxAn')
zxAnVlanMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,20))
if mibBuilder.loadTexts:zxAnVlanMib.setRevisions(('1911-06-15 00:00',))
_ZxAnVlanNum_Type=Integer32
_ZxAnVlanNum_Object=MibScalar
zxAnVlanNum=_ZxAnVlanNum_Object((1,3,6,1,4,1,3902,1015,20,1),_ZxAnVlanNum_Type())
zxAnVlanNum.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanNum.setStatus(_A)
_ZxAnVlanTable_Object=MibTable
zxAnVlanTable=_ZxAnVlanTable_Object((1,3,6,1,4,1,3902,1015,20,2))
if mibBuilder.loadTexts:zxAnVlanTable.setStatus(_A)
_ZxAnVlanEntry_Object=MibTableRow
zxAnVlanEntry=_ZxAnVlanEntry_Object((1,3,6,1,4,1,3902,1015,20,2,1))
zxAnVlanEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:zxAnVlanEntry.setStatus(_A)
_ZxAnVlanId_Type=VlanId
_ZxAnVlanId_Object=MibTableColumn
zxAnVlanId=_ZxAnVlanId_Object((1,3,6,1,4,1,3902,1015,20,2,1,1),_ZxAnVlanId_Type())
zxAnVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanId.setStatus(_A)
class _ZxAnVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnVlanName_Type.__name__=_J
_ZxAnVlanName_Object=MibTableColumn
zxAnVlanName=_ZxAnVlanName_Object((1,3,6,1,4,1,3902,1015,20,2,1,2),_ZxAnVlanName_Type())
zxAnVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanName.setStatus(_A)
class _ZxAnVlanTransparent_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanTransparent_Type.__name__=_C
_ZxAnVlanTransparent_Object=MibTableColumn
zxAnVlanTransparent=_ZxAnVlanTransparent_Object((1,3,6,1,4,1,3902,1015,20,2,1,3),_ZxAnVlanTransparent_Type())
zxAnVlanTransparent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTransparent.setStatus(_A)
_ZxAnVlanRowStatus_Type=RowStatus
_ZxAnVlanRowStatus_Object=MibTableColumn
zxAnVlanRowStatus=_ZxAnVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,20,2,1,4),_ZxAnVlanRowStatus_Type())
zxAnVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRowStatus.setStatus(_A)
class _ZxAnVlanXconnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanXconnect_Type.__name__=_C
_ZxAnVlanXconnect_Object=MibTableColumn
zxAnVlanXconnect=_ZxAnVlanXconnect_Object((1,3,6,1,4,1,3902,1015,20,2,1,5),_ZxAnVlanXconnect_Type())
zxAnVlanXconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanXconnect.setStatus(_A)
class _ZxAnVlanDesc_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnVlanDesc_Type.__name__=_J
_ZxAnVlanDesc_Object=MibTableColumn
zxAnVlanDesc=_ZxAnVlanDesc_Object((1,3,6,1,4,1,3902,1015,20,2,1,6),_ZxAnVlanDesc_Type())
zxAnVlanDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanDesc.setStatus(_A)
_ZxAnVlanPortTable_Object=MibTable
zxAnVlanPortTable=_ZxAnVlanPortTable_Object((1,3,6,1,4,1,3902,1015,20,3))
if mibBuilder.loadTexts:zxAnVlanPortTable.setStatus(_A)
_ZxAnVlanPortEntry_Object=MibTableRow
zxAnVlanPortEntry=_ZxAnVlanPortEntry_Object((1,3,6,1,4,1,3902,1015,20,3,1))
zxAnVlanPortEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:zxAnVlanPortEntry.setStatus(_A)
_ZxAnVlanPortIndex_Type=ZxAnIfindex
_ZxAnVlanPortIndex_Object=MibTableColumn
zxAnVlanPortIndex=_ZxAnVlanPortIndex_Object((1,3,6,1,4,1,3902,1015,20,3,1,1),_ZxAnVlanPortIndex_Type())
zxAnVlanPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanPortIndex.setStatus(_A)
class _ZxAnVlanIfConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('access',1),('trunk',2),(_O,3),('transparent',4)))
_ZxAnVlanIfConfMode_Type.__name__=_C
_ZxAnVlanIfConfMode_Object=MibTableColumn
zxAnVlanIfConfMode=_ZxAnVlanIfConfMode_Object((1,3,6,1,4,1,3902,1015,20,3,1,2),_ZxAnVlanIfConfMode_Type())
zxAnVlanIfConfMode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfMode.setStatus(_A)
class _ZxAnVlanIfConfTlsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanIfConfTlsEnable_Type.__name__=_C
_ZxAnVlanIfConfTlsEnable_Object=MibTableColumn
zxAnVlanIfConfTlsEnable=_ZxAnVlanIfConfTlsEnable_Object((1,3,6,1,4,1,3902,1015,20,3,1,3),_ZxAnVlanIfConfTlsEnable_Type())
zxAnVlanIfConfTlsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfTlsEnable.setStatus(_A)
class _ZxAnVlanIfConfTlsSVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanIfConfTlsSVid_Type.__name__=_C
_ZxAnVlanIfConfTlsSVid_Object=MibTableColumn
zxAnVlanIfConfTlsSVid=_ZxAnVlanIfConfTlsSVid_Object((1,3,6,1,4,1,3902,1015,20,3,1,4),_ZxAnVlanIfConfTlsSVid_Type())
zxAnVlanIfConfTlsSVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfTlsSVid.setStatus(_A)
_ZxAnVlanIfConfDefaultVid_Type=VlanId
_ZxAnVlanIfConfDefaultVid_Object=MibTableColumn
zxAnVlanIfConfDefaultVid=_ZxAnVlanIfConfDefaultVid_Object((1,3,6,1,4,1,3902,1015,20,3,1,5),_ZxAnVlanIfConfDefaultVid_Type())
zxAnVlanIfConfDefaultVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfDefaultVid.setStatus(_A)
class _ZxAnVlanIfConfDefaultCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanIfConfDefaultCVid_Type.__name__=_C
_ZxAnVlanIfConfDefaultCVid_Object=MibTableColumn
zxAnVlanIfConfDefaultCVid=_ZxAnVlanIfConfDefaultCVid_Object((1,3,6,1,4,1,3902,1015,20,3,1,6),_ZxAnVlanIfConfDefaultCVid_Type())
zxAnVlanIfConfDefaultCVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfDefaultCVid.setStatus(_A)
_ZxAnVlanIfConfUntaggedVlanList_Type=DisplayString
_ZxAnVlanIfConfUntaggedVlanList_Object=MibTableColumn
zxAnVlanIfConfUntaggedVlanList=_ZxAnVlanIfConfUntaggedVlanList_Object((1,3,6,1,4,1,3902,1015,20,3,1,7),_ZxAnVlanIfConfUntaggedVlanList_Type())
zxAnVlanIfConfUntaggedVlanList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanIfConfUntaggedVlanList.setStatus(_A)
_ZxAnVlanIfConfTaggedVlanList_Type=DisplayString
_ZxAnVlanIfConfTaggedVlanList_Object=MibTableColumn
zxAnVlanIfConfTaggedVlanList=_ZxAnVlanIfConfTaggedVlanList_Object((1,3,6,1,4,1,3902,1015,20,3,1,8),_ZxAnVlanIfConfTaggedVlanList_Type())
zxAnVlanIfConfTaggedVlanList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanIfConfTaggedVlanList.setStatus(_A)
class _ZxAnVlanIfConfTpid_Type(Integer32):defaultValue=33024
_ZxAnVlanIfConfTpid_Type.__name__=_C
_ZxAnVlanIfConfTpid_Object=MibTableColumn
zxAnVlanIfConfTpid=_ZxAnVlanIfConfTpid_Object((1,3,6,1,4,1,3902,1015,20,3,1,9),_ZxAnVlanIfConfTpid_Type())
zxAnVlanIfConfTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfTpid.setStatus(_A)
class _ZxAnVlanIfIngressFilterEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanIfIngressFilterEnable_Type.__name__=_C
_ZxAnVlanIfIngressFilterEnable_Object=MibTableColumn
zxAnVlanIfIngressFilterEnable=_ZxAnVlanIfIngressFilterEnable_Object((1,3,6,1,4,1,3902,1015,20,3,1,10),_ZxAnVlanIfIngressFilterEnable_Type())
zxAnVlanIfIngressFilterEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfIngressFilterEnable.setStatus(_A)
class _ZxAnVlanIfAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2),('admitOnlyVlanUntagged',3),('admitOnlyVlanSingleTagged',4),('admitOnlyVlanMaxDoubleTagged',5),('admitOnlyVlanMaxSingleTagged',6),('admitOnlyVlanDoubleTagged',7)))
_ZxAnVlanIfAcceptableFrameTypes_Type.__name__=_C
_ZxAnVlanIfAcceptableFrameTypes_Object=MibTableColumn
zxAnVlanIfAcceptableFrameTypes=_ZxAnVlanIfAcceptableFrameTypes_Object((1,3,6,1,4,1,3902,1015,20,3,1,11),_ZxAnVlanIfAcceptableFrameTypes_Type())
zxAnVlanIfAcceptableFrameTypes.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfAcceptableFrameTypes.setStatus(_A)
class _ZxAnVlanIfConfTpidEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanIfConfTpidEnable_Type.__name__=_C
_ZxAnVlanIfConfTpidEnable_Object=MibTableColumn
zxAnVlanIfConfTpidEnable=_ZxAnVlanIfConfTpidEnable_Object((1,3,6,1,4,1,3902,1015,20,3,1,12),_ZxAnVlanIfConfTpidEnable_Type())
zxAnVlanIfConfTpidEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfTpidEnable.setStatus(_A)
_ZxAnVlanIfConfVlanCmdTable_Object=MibTable
zxAnVlanIfConfVlanCmdTable=_ZxAnVlanIfConfVlanCmdTable_Object((1,3,6,1,4,1,3902,1015,20,4))
if mibBuilder.loadTexts:zxAnVlanIfConfVlanCmdTable.setStatus(_A)
_ZxAnVlanIfConfVlanCmdEntry_Object=MibTableRow
zxAnVlanIfConfVlanCmdEntry=_ZxAnVlanIfConfVlanCmdEntry_Object((1,3,6,1,4,1,3902,1015,20,4,1))
zxAnVlanIfConfVlanCmdEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:zxAnVlanIfConfVlanCmdEntry.setStatus(_A)
class _ZxAnVlanIfConfVlanCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('addTaggedVlan',1),('delTaggedVlan',2),('addUntaggedVlan',3),('delUntaggedVlan',4),('addDefaultVlan',5),('delDefaultVlan',6)))
_ZxAnVlanIfConfVlanCmd_Type.__name__=_C
_ZxAnVlanIfConfVlanCmd_Object=MibTableColumn
zxAnVlanIfConfVlanCmd=_ZxAnVlanIfConfVlanCmd_Object((1,3,6,1,4,1,3902,1015,20,4,1,1),_ZxAnVlanIfConfVlanCmd_Type())
zxAnVlanIfConfVlanCmd.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfVlanCmd.setStatus(_A)
_ZxAnVlanIfConfVlanList_Type=VlanId
_ZxAnVlanIfConfVlanList_Object=MibTableColumn
zxAnVlanIfConfVlanList=_ZxAnVlanIfConfVlanList_Object((1,3,6,1,4,1,3902,1015,20,4,1,2),_ZxAnVlanIfConfVlanList_Type())
zxAnVlanIfConfVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfConfVlanList.setStatus(_A)
_ZxAnVlanIfTransTable_Object=MibTable
zxAnVlanIfTransTable=_ZxAnVlanIfTransTable_Object((1,3,6,1,4,1,3902,1015,20,5))
if mibBuilder.loadTexts:zxAnVlanIfTransTable.setStatus(_A)
_ZxAnVlanIfTransEntry_Object=MibTableRow
zxAnVlanIfTransEntry=_ZxAnVlanIfTransEntry_Object((1,3,6,1,4,1,3902,1015,20,5,1))
zxAnVlanIfTransEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:zxAnVlanIfTransEntry.setStatus(_A)
_ZxAnVlanTranslatePortId_Type=Integer32
_ZxAnVlanTranslatePortId_Object=MibTableColumn
zxAnVlanTranslatePortId=_ZxAnVlanTranslatePortId_Object((1,3,6,1,4,1,3902,1015,20,5,1,1),_ZxAnVlanTranslatePortId_Type())
zxAnVlanTranslatePortId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanTranslatePortId.setStatus(_A)
_ZxAnVlanIfTransUserVid_Type=VlanId
_ZxAnVlanIfTransUserVid_Object=MibTableColumn
zxAnVlanIfTransUserVid=_ZxAnVlanIfTransUserVid_Object((1,3,6,1,4,1,3902,1015,20,5,1,2),_ZxAnVlanIfTransUserVid_Type())
zxAnVlanIfTransUserVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanIfTransUserVid.setStatus(_A)
class _ZxAnVlanIfTransCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanIfTransCVid_Type.__name__=_C
_ZxAnVlanIfTransCVid_Object=MibTableColumn
zxAnVlanIfTransCVid=_ZxAnVlanIfTransCVid_Object((1,3,6,1,4,1,3902,1015,20,5,1,3),_ZxAnVlanIfTransCVid_Type())
zxAnVlanIfTransCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfTransCVid.setStatus(_A)
_ZxAnVlanIfTransSVid_Type=VlanId
_ZxAnVlanIfTransSVid_Object=MibTableColumn
zxAnVlanIfTransSVid=_ZxAnVlanIfTransSVid_Object((1,3,6,1,4,1,3902,1015,20,5,1,4),_ZxAnVlanIfTransSVid_Type())
zxAnVlanIfTransSVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfTransSVid.setStatus(_A)
_ZxAnVlanIfTransRowStatus_Type=RowStatus
_ZxAnVlanIfTransRowStatus_Object=MibTableColumn
zxAnVlanIfTransRowStatus=_ZxAnVlanIfTransRowStatus_Object((1,3,6,1,4,1,3902,1015,20,5,1,5),_ZxAnVlanIfTransRowStatus_Type())
zxAnVlanIfTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfTransRowStatus.setStatus(_A)
class _ZxAnVlanIfTransVlanMerge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanIfTransVlanMerge_Type.__name__=_C
_ZxAnVlanIfTransVlanMerge_Object=MibTableColumn
zxAnVlanIfTransVlanMerge=_ZxAnVlanIfTransVlanMerge_Object((1,3,6,1,4,1,3902,1015,20,5,1,6),_ZxAnVlanIfTransVlanMerge_Type())
zxAnVlanIfTransVlanMerge.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfTransVlanMerge.setStatus(_A)
_ZxAnVlanPortListTable_Object=MibTable
zxAnVlanPortListTable=_ZxAnVlanPortListTable_Object((1,3,6,1,4,1,3902,1015,20,6))
if mibBuilder.loadTexts:zxAnVlanPortListTable.setStatus(_A)
_ZxAnVlanPortListEntry_Object=MibTableRow
zxAnVlanPortListEntry=_ZxAnVlanPortListEntry_Object((1,3,6,1,4,1,3902,1015,20,6,1))
zxAnVlanPortListEntry.setIndexNames((0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:zxAnVlanPortListEntry.setStatus(_A)
_ZxAnVlanIndex_Type=VlanId
_ZxAnVlanIndex_Object=MibTableColumn
zxAnVlanIndex=_ZxAnVlanIndex_Object((1,3,6,1,4,1,3902,1015,20,6,1,1),_ZxAnVlanIndex_Type())
zxAnVlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanIndex.setStatus(_A)
_ZxAnShelfIndex_Type=Integer32
_ZxAnShelfIndex_Object=MibTableColumn
zxAnShelfIndex=_ZxAnShelfIndex_Object((1,3,6,1,4,1,3902,1015,20,6,1,2),_ZxAnShelfIndex_Type())
zxAnShelfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnShelfIndex.setStatus(_A)
_ZxAnSlotIndex_Type=Integer32
_ZxAnSlotIndex_Object=MibTableColumn
zxAnSlotIndex=_ZxAnSlotIndex_Object((1,3,6,1,4,1,3902,1015,20,6,1,3),_ZxAnSlotIndex_Type())
zxAnSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSlotIndex.setStatus(_A)
_ZxAnVlanPortListSlotIfType_Type=Integer32
_ZxAnVlanPortListSlotIfType_Object=MibTableColumn
zxAnVlanPortListSlotIfType=_ZxAnVlanPortListSlotIfType_Object((1,3,6,1,4,1,3902,1015,20,6,1,4),_ZxAnVlanPortListSlotIfType_Type())
zxAnVlanPortListSlotIfType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanPortListSlotIfType.setStatus(_A)
_ZxAnVlanPortUntaggedPortList_Type=ZxAnPortList
_ZxAnVlanPortUntaggedPortList_Object=MibTableColumn
zxAnVlanPortUntaggedPortList=_ZxAnVlanPortUntaggedPortList_Object((1,3,6,1,4,1,3902,1015,20,6,1,5),_ZxAnVlanPortUntaggedPortList_Type())
zxAnVlanPortUntaggedPortList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanPortUntaggedPortList.setStatus(_A)
_ZxAnVlanPortTaggedPortList_Type=ZxAnPortList
_ZxAnVlanPortTaggedPortList_Object=MibTableColumn
zxAnVlanPortTaggedPortList=_ZxAnVlanPortTaggedPortList_Object((1,3,6,1,4,1,3902,1015,20,6,1,6),_ZxAnVlanPortTaggedPortList_Type())
zxAnVlanPortTaggedPortList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanPortTaggedPortList.setStatus(_A)
_ZxAnVlanGlobalTransTable_Object=MibTable
zxAnVlanGlobalTransTable=_ZxAnVlanGlobalTransTable_Object((1,3,6,1,4,1,3902,1015,20,7))
if mibBuilder.loadTexts:zxAnVlanGlobalTransTable.setStatus(_A)
_ZxAnVlanGlobalTransEntry_Object=MibTableRow
zxAnVlanGlobalTransEntry=_ZxAnVlanGlobalTransEntry_Object((1,3,6,1,4,1,3902,1015,20,7,1))
zxAnVlanGlobalTransEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:zxAnVlanGlobalTransEntry.setStatus(_A)
class _ZxAnVlanGlobalTransSessionNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ZxAnVlanGlobalTransSessionNo_Type.__name__=_C
_ZxAnVlanGlobalTransSessionNo_Object=MibTableColumn
zxAnVlanGlobalTransSessionNo=_ZxAnVlanGlobalTransSessionNo_Object((1,3,6,1,4,1,3902,1015,20,7,1,1),_ZxAnVlanGlobalTransSessionNo_Type())
zxAnVlanGlobalTransSessionNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanGlobalTransSessionNo.setStatus(_A)
_ZxAnVlanMpTranslatePortId_Type=Integer32
_ZxAnVlanMpTranslatePortId_Object=MibTableColumn
zxAnVlanMpTranslatePortId=_ZxAnVlanMpTranslatePortId_Object((1,3,6,1,4,1,3902,1015,20,7,1,2),_ZxAnVlanMpTranslatePortId_Type())
zxAnVlanMpTranslatePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanMpTranslatePortId.setStatus(_A)
_ZxAnVlanGlobalTransVid_Type=VlanId
_ZxAnVlanGlobalTransVid_Object=MibTableColumn
zxAnVlanGlobalTransVid=_ZxAnVlanGlobalTransVid_Object((1,3,6,1,4,1,3902,1015,20,7,1,3),_ZxAnVlanGlobalTransVid_Type())
zxAnVlanGlobalTransVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanGlobalTransVid.setStatus(_A)
class _ZxAnVlanGlobalTransCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnVlanGlobalTransCVid_Type.__name__=_C
_ZxAnVlanGlobalTransCVid_Object=MibTableColumn
zxAnVlanGlobalTransCVid=_ZxAnVlanGlobalTransCVid_Object((1,3,6,1,4,1,3902,1015,20,7,1,4),_ZxAnVlanGlobalTransCVid_Type())
zxAnVlanGlobalTransCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanGlobalTransCVid.setStatus(_A)
class _ZxAnVlanGlobalTransSVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanGlobalTransSVid_Type.__name__=_C
_ZxAnVlanGlobalTransSVid_Object=MibTableColumn
zxAnVlanGlobalTransSVid=_ZxAnVlanGlobalTransSVid_Object((1,3,6,1,4,1,3902,1015,20,7,1,5),_ZxAnVlanGlobalTransSVid_Type())
zxAnVlanGlobalTransSVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanGlobalTransSVid.setStatus(_A)
class _ZxAnVlanMpTranslateDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upStream',1),('downStream',2)))
_ZxAnVlanMpTranslateDirection_Type.__name__=_C
_ZxAnVlanMpTranslateDirection_Object=MibTableColumn
zxAnVlanMpTranslateDirection=_ZxAnVlanMpTranslateDirection_Object((1,3,6,1,4,1,3902,1015,20,7,1,6),_ZxAnVlanMpTranslateDirection_Type())
zxAnVlanMpTranslateDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanMpTranslateDirection.setStatus(_A)
_ZxAnVlanGlobalTransRowStatus_Type=RowStatus
_ZxAnVlanGlobalTransRowStatus_Object=MibTableColumn
zxAnVlanGlobalTransRowStatus=_ZxAnVlanGlobalTransRowStatus_Object((1,3,6,1,4,1,3902,1015,20,7,1,7),_ZxAnVlanGlobalTransRowStatus_Type())
zxAnVlanGlobalTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanGlobalTransRowStatus.setStatus(_A)
class _ZxAnVlanGlobalTransVlanMerge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanGlobalTransVlanMerge_Type.__name__=_C
_ZxAnVlanGlobalTransVlanMerge_Object=MibTableColumn
zxAnVlanGlobalTransVlanMerge=_ZxAnVlanGlobalTransVlanMerge_Object((1,3,6,1,4,1,3902,1015,20,7,1,8),_ZxAnVlanGlobalTransVlanMerge_Type())
zxAnVlanGlobalTransVlanMerge.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanGlobalTransVlanMerge.setStatus(_A)
_ZxAnVlanMpExQinQTable_Object=MibTable
zxAnVlanMpExQinQTable=_ZxAnVlanMpExQinQTable_Object((1,3,6,1,4,1,3902,1015,20,8))
if mibBuilder.loadTexts:zxAnVlanMpExQinQTable.setStatus(_A)
_ZxAnVlanMpExQinQEntry_Object=MibTableRow
zxAnVlanMpExQinQEntry=_ZxAnVlanMpExQinQEntry_Object((1,3,6,1,4,1,3902,1015,20,8,1))
zxAnVlanMpExQinQEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:zxAnVlanMpExQinQEntry.setStatus(_A)
_ZxAnVlanExQinQSessionNo_Type=Integer32
_ZxAnVlanExQinQSessionNo_Object=MibTableColumn
zxAnVlanExQinQSessionNo=_ZxAnVlanExQinQSessionNo_Object((1,3,6,1,4,1,3902,1015,20,8,1,1),_ZxAnVlanExQinQSessionNo_Type())
zxAnVlanExQinQSessionNo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanExQinQSessionNo.setStatus(_A)
_ZxAnVlanSmartQinQIfIndex_Type=Integer32
_ZxAnVlanSmartQinQIfIndex_Object=MibTableColumn
zxAnVlanSmartQinQIfIndex=_ZxAnVlanSmartQinQIfIndex_Object((1,3,6,1,4,1,3902,1015,20,8,1,2),_ZxAnVlanSmartQinQIfIndex_Type())
zxAnVlanSmartQinQIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQIfIndex.setStatus(_A)
_ZxAnVlanSmartQinQUserVid_Type=Integer32
_ZxAnVlanSmartQinQUserVid_Object=MibTableColumn
zxAnVlanSmartQinQUserVid=_ZxAnVlanSmartQinQUserVid_Object((1,3,6,1,4,1,3902,1015,20,8,1,3),_ZxAnVlanSmartQinQUserVid_Type())
zxAnVlanSmartQinQUserVid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanSmartQinQUserVid.setStatus(_A)
class _ZxAnVlanSmartQinQSelectiveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cvlanscope',1),('ethertype',2),('cos',3),('cvlancos',4),('cvlanethertype',5),('cvlantransparent',6)))
_ZxAnVlanSmartQinQSelectiveType_Type.__name__=_C
_ZxAnVlanSmartQinQSelectiveType_Object=MibTableColumn
zxAnVlanSmartQinQSelectiveType=_ZxAnVlanSmartQinQSelectiveType_Object((1,3,6,1,4,1,3902,1015,20,8,1,4),_ZxAnVlanSmartQinQSelectiveType_Type())
zxAnVlanSmartQinQSelectiveType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQSelectiveType.setStatus(_A)
_ZxAnVlanSmartQinQStartUserVid_Type=Integer32
_ZxAnVlanSmartQinQStartUserVid_Object=MibTableColumn
zxAnVlanSmartQinQStartUserVid=_ZxAnVlanSmartQinQStartUserVid_Object((1,3,6,1,4,1,3902,1015,20,8,1,5),_ZxAnVlanSmartQinQStartUserVid_Type())
zxAnVlanSmartQinQStartUserVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQStartUserVid.setStatus(_A)
_ZxAnVlanSmartQinQEndUserVid_Type=Integer32
_ZxAnVlanSmartQinQEndUserVid_Object=MibTableColumn
zxAnVlanSmartQinQEndUserVid=_ZxAnVlanSmartQinQEndUserVid_Object((1,3,6,1,4,1,3902,1015,20,8,1,6),_ZxAnVlanSmartQinQEndUserVid_Type())
zxAnVlanSmartQinQEndUserVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQEndUserVid.setStatus(_A)
_ZxAnVlanExQinQInCVlanMask_Type=Integer32
_ZxAnVlanExQinQInCVlanMask_Object=MibTableColumn
zxAnVlanExQinQInCVlanMask=_ZxAnVlanExQinQInCVlanMask_Object((1,3,6,1,4,1,3902,1015,20,8,1,7),_ZxAnVlanExQinQInCVlanMask_Type())
zxAnVlanExQinQInCVlanMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanExQinQInCVlanMask.setStatus(_A)
_ZxAnVlanSmartQinQEtherType_Type=Integer32
_ZxAnVlanSmartQinQEtherType_Object=MibTableColumn
zxAnVlanSmartQinQEtherType=_ZxAnVlanSmartQinQEtherType_Object((1,3,6,1,4,1,3902,1015,20,8,1,8),_ZxAnVlanSmartQinQEtherType_Type())
zxAnVlanSmartQinQEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQEtherType.setStatus(_A)
class _ZxAnVlanSmartQinQUserCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_ZxAnVlanSmartQinQUserCos_Type.__name__=_C
_ZxAnVlanSmartQinQUserCos_Object=MibTableColumn
zxAnVlanSmartQinQUserCos=_ZxAnVlanSmartQinQUserCos_Object((1,3,6,1,4,1,3902,1015,20,8,1,9),_ZxAnVlanSmartQinQUserCos_Type())
zxAnVlanSmartQinQUserCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQUserCos.setStatus(_A)
_ZxAnVlanSmartQinQSVid_Type=VlanId
_ZxAnVlanSmartQinQSVid_Object=MibTableColumn
zxAnVlanSmartQinQSVid=_ZxAnVlanSmartQinQSVid_Object((1,3,6,1,4,1,3902,1015,20,8,1,10),_ZxAnVlanSmartQinQSVid_Type())
zxAnVlanSmartQinQSVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQSVid.setStatus(_A)
class _ZxAnVlanSmartQinQStagCos_Type(Integer32):defaultValue=255
_ZxAnVlanSmartQinQStagCos_Type.__name__=_C
_ZxAnVlanSmartQinQStagCos_Object=MibTableColumn
zxAnVlanSmartQinQStagCos=_ZxAnVlanSmartQinQStagCos_Object((1,3,6,1,4,1,3902,1015,20,8,1,11),_ZxAnVlanSmartQinQStagCos_Type())
zxAnVlanSmartQinQStagCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQStagCos.setStatus(_A)
class _ZxAnVlanExQinQRefOnuGroupId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxAnVlanExQinQRefOnuGroupId_Type.__name__=_C
_ZxAnVlanExQinQRefOnuGroupId_Object=MibTableColumn
zxAnVlanExQinQRefOnuGroupId=_ZxAnVlanExQinQRefOnuGroupId_Object((1,3,6,1,4,1,3902,1015,20,8,1,12),_ZxAnVlanExQinQRefOnuGroupId_Type())
zxAnVlanExQinQRefOnuGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanExQinQRefOnuGroupId.setStatus(_A)
_ZxAnVlanSmartQinQRowStatus_Type=RowStatus
_ZxAnVlanSmartQinQRowStatus_Object=MibTableColumn
zxAnVlanSmartQinQRowStatus=_ZxAnVlanSmartQinQRowStatus_Object((1,3,6,1,4,1,3902,1015,20,8,1,50),_ZxAnVlanSmartQinQRowStatus_Type())
zxAnVlanSmartQinQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanSmartQinQRowStatus.setStatus(_A)
_ZxAnVlanVoipConfTable_Object=MibTable
zxAnVlanVoipConfTable=_ZxAnVlanVoipConfTable_Object((1,3,6,1,4,1,3902,1015,20,9))
if mibBuilder.loadTexts:zxAnVlanVoipConfTable.setStatus(_A)
_ZxAnVlanVoipConfEntry_Object=MibTableRow
zxAnVlanVoipConfEntry=_ZxAnVlanVoipConfEntry_Object((1,3,6,1,4,1,3902,1015,20,9,1))
zxAnVlanVoipConfEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:zxAnVlanVoipConfEntry.setStatus(_A)
_ZxAnVlanVoipVlanId_Type=VlanId
_ZxAnVlanVoipVlanId_Object=MibTableColumn
zxAnVlanVoipVlanId=_ZxAnVlanVoipVlanId_Object((1,3,6,1,4,1,3902,1015,20,9,1,1),_ZxAnVlanVoipVlanId_Type())
zxAnVlanVoipVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanVoipVlanId.setStatus(_A)
class _ZxAnVoipVlanUsages_Type(Bits):namedValues=NamedValues(*(('media',0),('signal',1)))
_ZxAnVoipVlanUsages_Type.__name__=_M
_ZxAnVoipVlanUsages_Object=MibTableColumn
zxAnVoipVlanUsages=_ZxAnVoipVlanUsages_Object((1,3,6,1,4,1,3902,1015,20,9,1,2),_ZxAnVoipVlanUsages_Type())
zxAnVoipVlanUsages.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVoipVlanUsages.setStatus(_A)
_ZxAnVlanVoipRowStatus_Type=RowStatus
_ZxAnVlanVoipRowStatus_Object=MibTableColumn
zxAnVlanVoipRowStatus=_ZxAnVlanVoipRowStatus_Object((1,3,6,1,4,1,3902,1015,20,9,1,50),_ZxAnVlanVoipRowStatus_Type())
zxAnVlanVoipRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanVoipRowStatus.setStatus(_A)
class _ZxAnVlanSmartQinQEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('enableGlobal',1),('disablGlobal',2),('enableEIGMP',3),('disablEIGMP',4),('enableV2',5),('disableV2',6),('enableV3',7),('disableV3',8)))
_ZxAnVlanSmartQinQEnable_Type.__name__=_C
_ZxAnVlanSmartQinQEnable_Object=MibScalar
zxAnVlanSmartQinQEnable=_ZxAnVlanSmartQinQEnable_Object((1,3,6,1,4,1,3902,1015,20,10),_ZxAnVlanSmartQinQEnable_Type())
zxAnVlanSmartQinQEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanSmartQinQEnable.setStatus(_A)
_ZxAnReservedVlan_Type=DisplayString
_ZxAnReservedVlan_Object=MibScalar
zxAnReservedVlan=_ZxAnReservedVlan_Object((1,3,6,1,4,1,3902,1015,20,11),_ZxAnReservedVlan_Type())
zxAnReservedVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnReservedVlan.setStatus(_A)
_ZxAnVlanMpExQinQPortTable_Object=MibTable
zxAnVlanMpExQinQPortTable=_ZxAnVlanMpExQinQPortTable_Object((1,3,6,1,4,1,3902,1015,20,12))
if mibBuilder.loadTexts:zxAnVlanMpExQinQPortTable.setStatus(_A)
_ZxAnVlanMpExQinQPortEntry_Object=MibTableRow
zxAnVlanMpExQinQPortEntry=_ZxAnVlanMpExQinQPortEntry_Object((1,3,6,1,4,1,3902,1015,20,12,1))
zxAnVlanMpExQinQPortEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:zxAnVlanMpExQinQPortEntry.setStatus(_A)
_ZxAnVlanExQinQPortIndex_Type=ZxAnIfindex
_ZxAnVlanExQinQPortIndex_Object=MibTableColumn
zxAnVlanExQinQPortIndex=_ZxAnVlanExQinQPortIndex_Object((1,3,6,1,4,1,3902,1015,20,12,1,1),_ZxAnVlanExQinQPortIndex_Type())
zxAnVlanExQinQPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanExQinQPortIndex.setStatus(_A)
class _ZxAnVlanSmartQinQIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanSmartQinQIfEnable_Type.__name__=_C
_ZxAnVlanSmartQinQIfEnable_Object=MibTableColumn
zxAnVlanSmartQinQIfEnable=_ZxAnVlanSmartQinQIfEnable_Object((1,3,6,1,4,1,3902,1015,20,12,1,2),_ZxAnVlanSmartQinQIfEnable_Type())
zxAnVlanSmartQinQIfEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanSmartQinQIfEnable.setStatus(_A)
class _ZxAnVlanExQinQOnuMapGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ZxAnVlanExQinQOnuMapGroupId_Type.__name__=_C
_ZxAnVlanExQinQOnuMapGroupId_Object=MibTableColumn
zxAnVlanExQinQOnuMapGroupId=_ZxAnVlanExQinQOnuMapGroupId_Object((1,3,6,1,4,1,3902,1015,20,12,1,3),_ZxAnVlanExQinQOnuMapGroupId_Type())
zxAnVlanExQinQOnuMapGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanExQinQOnuMapGroupId.setStatus(_A)
class _ZxAnVlanExQinQPortResVlan_Type(Integer32):defaultValue=4094;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4055,4094))
_ZxAnVlanExQinQPortResVlan_Type.__name__=_C
_ZxAnVlanExQinQPortResVlan_Object=MibTableColumn
zxAnVlanExQinQPortResVlan=_ZxAnVlanExQinQPortResVlan_Object((1,3,6,1,4,1,3902,1015,20,12,1,4),_ZxAnVlanExQinQPortResVlan_Type())
zxAnVlanExQinQPortResVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanExQinQPortResVlan.setStatus(_A)
_ZxAnVlanMpExTranslatePortTable_Object=MibTable
zxAnVlanMpExTranslatePortTable=_ZxAnVlanMpExTranslatePortTable_Object((1,3,6,1,4,1,3902,1015,20,13))
if mibBuilder.loadTexts:zxAnVlanMpExTranslatePortTable.setStatus(_A)
_ZxAnVlanMpExTranslatePortEntry_Object=MibTableRow
zxAnVlanMpExTranslatePortEntry=_ZxAnVlanMpExTranslatePortEntry_Object((1,3,6,1,4,1,3902,1015,20,13,1))
zxAnVlanMpExTranslatePortEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:zxAnVlanMpExTranslatePortEntry.setStatus(_A)
_ZxAnVlanExTranslatePortIndex_Type=ZxAnIfindex
_ZxAnVlanExTranslatePortIndex_Object=MibTableColumn
zxAnVlanExTranslatePortIndex=_ZxAnVlanExTranslatePortIndex_Object((1,3,6,1,4,1,3902,1015,20,13,1,1),_ZxAnVlanExTranslatePortIndex_Type())
zxAnVlanExTranslatePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanExTranslatePortIndex.setStatus(_A)
class _ZxAnVlanExTranslatePortEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnVlanExTranslatePortEnabled_Type.__name__=_C
_ZxAnVlanExTranslatePortEnabled_Object=MibTableColumn
zxAnVlanExTranslatePortEnabled=_ZxAnVlanExTranslatePortEnabled_Object((1,3,6,1,4,1,3902,1015,20,13,1,2),_ZxAnVlanExTranslatePortEnabled_Type())
zxAnVlanExTranslatePortEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanExTranslatePortEnabled.setStatus(_A)
class _ZxAnVlanTranslateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ntoone',1),(_O,2)))
_ZxAnVlanTranslateMode_Type.__name__=_C
_ZxAnVlanTranslateMode_Object=MibScalar
zxAnVlanTranslateMode=_ZxAnVlanTranslateMode_Object((1,3,6,1,4,1,3902,1015,20,14),_ZxAnVlanTranslateMode_Type())
zxAnVlanTranslateMode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanTranslateMode.setStatus(_A)
_ZxAnProtocolVlanMapTable_Object=MibTable
zxAnProtocolVlanMapTable=_ZxAnProtocolVlanMapTable_Object((1,3,6,1,4,1,3902,1015,20,16))
if mibBuilder.loadTexts:zxAnProtocolVlanMapTable.setStatus(_A)
_ZxAnProtocolVlanMapEntry_Object=MibTableRow
zxAnProtocolVlanMapEntry=_ZxAnProtocolVlanMapEntry_Object((1,3,6,1,4,1,3902,1015,20,16,1))
zxAnProtocolVlanMapEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:zxAnProtocolVlanMapEntry.setStatus(_A)
_ZxAnProtocolVlanPortIndex_Type=ZxAnIfindex
_ZxAnProtocolVlanPortIndex_Object=MibTableColumn
zxAnProtocolVlanPortIndex=_ZxAnProtocolVlanPortIndex_Object((1,3,6,1,4,1,3902,1015,20,16,1,1),_ZxAnProtocolVlanPortIndex_Type())
zxAnProtocolVlanPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnProtocolVlanPortIndex.setStatus(_A)
_ZxAnEtherProtocolType_Type=Integer32
_ZxAnEtherProtocolType_Object=MibTableColumn
zxAnEtherProtocolType=_ZxAnEtherProtocolType_Object((1,3,6,1,4,1,3902,1015,20,16,1,2),_ZxAnEtherProtocolType_Type())
zxAnEtherProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnEtherProtocolType.setStatus(_A)
_ZxAnVlanIfProtoMapVid_Type=VlanId
_ZxAnVlanIfProtoMapVid_Object=MibTableColumn
zxAnVlanIfProtoMapVid=_ZxAnVlanIfProtoMapVid_Object((1,3,6,1,4,1,3902,1015,20,16,1,3),_ZxAnVlanIfProtoMapVid_Type())
zxAnVlanIfProtoMapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapVid.setStatus(_A)
class _ZxAnVlanIfProtoMapCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnVlanIfProtoMapCos_Type.__name__=_C
_ZxAnVlanIfProtoMapCos_Object=MibTableColumn
zxAnVlanIfProtoMapCos=_ZxAnVlanIfProtoMapCos_Object((1,3,6,1,4,1,3902,1015,20,16,1,4),_ZxAnVlanIfProtoMapCos_Type())
zxAnVlanIfProtoMapCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapCos.setStatus(_A)
class _ZxAnVlanIfProtoMapCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanIfProtoMapCVid_Type.__name__=_C
_ZxAnVlanIfProtoMapCVid_Object=MibTableColumn
zxAnVlanIfProtoMapCVid=_ZxAnVlanIfProtoMapCVid_Object((1,3,6,1,4,1,3902,1015,20,16,1,5),_ZxAnVlanIfProtoMapCVid_Type())
zxAnVlanIfProtoMapCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapCVid.setStatus(_A)
class _ZxAnVlanIfProtoMapCtagCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnVlanIfProtoMapCtagCos_Type.__name__=_C
_ZxAnVlanIfProtoMapCtagCos_Object=MibTableColumn
zxAnVlanIfProtoMapCtagCos=_ZxAnVlanIfProtoMapCtagCos_Object((1,3,6,1,4,1,3902,1015,20,16,1,6),_ZxAnVlanIfProtoMapCtagCos_Type())
zxAnVlanIfProtoMapCtagCos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapCtagCos.setStatus(_A)
_ZxAnVlanIfProtoMapRowStatus_Type=RowStatus
_ZxAnVlanIfProtoMapRowStatus_Object=MibTableColumn
zxAnVlanIfProtoMapRowStatus=_ZxAnVlanIfProtoMapRowStatus_Object((1,3,6,1,4,1,3902,1015,20,16,1,100),_ZxAnVlanIfProtoMapRowStatus_Type())
zxAnVlanIfProtoMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapRowStatus.setStatus(_A)
_ZxAnBatchVLANObjects_ObjectIdentity=ObjectIdentity
zxAnBatchVLANObjects=_ZxAnBatchVLANObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,17))
_ZxAnVlanBatchConfVlanList_Type=DisplayString
_ZxAnVlanBatchConfVlanList_Object=MibScalar
zxAnVlanBatchConfVlanList=_ZxAnVlanBatchConfVlanList_Object((1,3,6,1,4,1,3902,1015,20,17,1),_ZxAnVlanBatchConfVlanList_Type())
zxAnVlanBatchConfVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanBatchConfVlanList.setStatus(_A)
class _ZxAnVlanBatchConfPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnVlanBatchConfPrefixName_Type.__name__=_J
_ZxAnVlanBatchConfPrefixName_Object=MibScalar
zxAnVlanBatchConfPrefixName=_ZxAnVlanBatchConfPrefixName_Object((1,3,6,1,4,1,3902,1015,20,17,2),_ZxAnVlanBatchConfPrefixName_Type())
zxAnVlanBatchConfPrefixName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanBatchConfPrefixName.setStatus(_A)
class _ZxAnBatchVlanTransparent_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnBatchVlanTransparent_Type.__name__=_C
_ZxAnBatchVlanTransparent_Object=MibScalar
zxAnBatchVlanTransparent=_ZxAnBatchVlanTransparent_Object((1,3,6,1,4,1,3902,1015,20,17,3),_ZxAnBatchVlanTransparent_Type())
zxAnBatchVlanTransparent.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnBatchVlanTransparent.setStatus(_A)
class _ZxAnVlanBatchConfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('create',1),('delete',2)))
_ZxAnVlanBatchConfType_Type.__name__=_C
_ZxAnVlanBatchConfType_Object=MibScalar
zxAnVlanBatchConfType=_ZxAnVlanBatchConfType_Object((1,3,6,1,4,1,3902,1015,20,17,4),_ZxAnVlanBatchConfType_Type())
zxAnVlanBatchConfType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanBatchConfType.setStatus(_A)
class _ZxAnVlanBatchConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notstarted',1),('inprogress',2),('success',3),('failed',4)))
_ZxAnVlanBatchConfStatus_Type.__name__=_C
_ZxAnVlanBatchConfStatus_Object=MibScalar
zxAnVlanBatchConfStatus=_ZxAnVlanBatchConfStatus_Object((1,3,6,1,4,1,3902,1015,20,17,5),_ZxAnVlanBatchConfStatus_Type())
zxAnVlanBatchConfStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanBatchConfStatus.setStatus(_A)
_ZxAnVlanBatchConfFailedVlanList_Type=DisplayString
_ZxAnVlanBatchConfFailedVlanList_Object=MibScalar
zxAnVlanBatchConfFailedVlanList=_ZxAnVlanBatchConfFailedVlanList_Object((1,3,6,1,4,1,3902,1015,20,17,6),_ZxAnVlanBatchConfFailedVlanList_Type())
zxAnVlanBatchConfFailedVlanList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanBatchConfFailedVlanList.setStatus(_A)
_ZxAnVlanBatchConfCurrVlanList_Type=DisplayString
_ZxAnVlanBatchConfCurrVlanList_Object=MibScalar
zxAnVlanBatchConfCurrVlanList=_ZxAnVlanBatchConfCurrVlanList_Object((1,3,6,1,4,1,3902,1015,20,17,7),_ZxAnVlanBatchConfCurrVlanList_Type())
zxAnVlanBatchConfCurrVlanList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanBatchConfCurrVlanList.setStatus(_A)
_ZxAnXconnectTable_Object=MibTable
zxAnXconnectTable=_ZxAnXconnectTable_Object((1,3,6,1,4,1,3902,1015,20,18))
if mibBuilder.loadTexts:zxAnXconnectTable.setStatus(_A)
_ZxAnXconnectEntry_Object=MibTableRow
zxAnXconnectEntry=_ZxAnXconnectEntry_Object((1,3,6,1,4,1,3902,1015,20,18,1))
zxAnXconnectEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:zxAnXconnectEntry.setStatus(_A)
_ZxAnXconnectPortIndex_Type=ZxAnIfindex
_ZxAnXconnectPortIndex_Object=MibTableColumn
zxAnXconnectPortIndex=_ZxAnXconnectPortIndex_Object((1,3,6,1,4,1,3902,1015,20,18,1,1),_ZxAnXconnectPortIndex_Type())
zxAnXconnectPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnXconnectPortIndex.setStatus(_A)
_ZxAnXconnectLocationIndex_Type=Integer32
_ZxAnXconnectLocationIndex_Object=MibTableColumn
zxAnXconnectLocationIndex=_ZxAnXconnectLocationIndex_Object((1,3,6,1,4,1,3902,1015,20,18,1,2),_ZxAnXconnectLocationIndex_Type())
zxAnXconnectLocationIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnXconnectLocationIndex.setStatus(_A)
class _ZxAnXconnectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tlsvlan',1),('cvlan',2),('svlan',3)))
_ZxAnXconnectMode_Type.__name__=_C
_ZxAnXconnectMode_Object=MibTableColumn
zxAnXconnectMode=_ZxAnXconnectMode_Object((1,3,6,1,4,1,3902,1015,20,18,1,3),_ZxAnXconnectMode_Type())
zxAnXconnectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnXconnectMode.setStatus(_A)
_ZxAnVlanBasedFwdSVid_Type=VlanId
_ZxAnVlanBasedFwdSVid_Object=MibTableColumn
zxAnVlanBasedFwdSVid=_ZxAnVlanBasedFwdSVid_Object((1,3,6,1,4,1,3902,1015,20,18,1,4),_ZxAnVlanBasedFwdSVid_Type())
zxAnVlanBasedFwdSVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanBasedFwdSVid.setStatus(_A)
_ZxAnVlanBasedFwdCVid_Type=VlanId
_ZxAnVlanBasedFwdCVid_Object=MibTableColumn
zxAnVlanBasedFwdCVid=_ZxAnVlanBasedFwdCVid_Object((1,3,6,1,4,1,3902,1015,20,18,1,5),_ZxAnVlanBasedFwdCVid_Type())
zxAnVlanBasedFwdCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanBasedFwdCVid.setStatus(_A)
_ZxAnXconnectNewCvlanId_Type=VlanId
_ZxAnXconnectNewCvlanId_Object=MibTableColumn
zxAnXconnectNewCvlanId=_ZxAnXconnectNewCvlanId_Object((1,3,6,1,4,1,3902,1015,20,18,1,6),_ZxAnXconnectNewCvlanId_Type())
zxAnXconnectNewCvlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnXconnectNewCvlanId.setStatus(_A)
_ZxAnXconnectNewSvlanId_Type=VlanId
_ZxAnXconnectNewSvlanId_Object=MibTableColumn
zxAnXconnectNewSvlanId=_ZxAnXconnectNewSvlanId_Object((1,3,6,1,4,1,3902,1015,20,18,1,7),_ZxAnXconnectNewSvlanId_Type())
zxAnXconnectNewSvlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnXconnectNewSvlanId.setStatus(_A)
_ZxAnVlanBasedFwdUplinkPort_Type=ZxAnIfindex
_ZxAnVlanBasedFwdUplinkPort_Object=MibTableColumn
zxAnVlanBasedFwdUplinkPort=_ZxAnVlanBasedFwdUplinkPort_Object((1,3,6,1,4,1,3902,1015,20,18,1,8),_ZxAnVlanBasedFwdUplinkPort_Type())
zxAnVlanBasedFwdUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanBasedFwdUplinkPort.setStatus(_A)
_ZxAnVlanBasedFwdRowStatus_Type=RowStatus
_ZxAnVlanBasedFwdRowStatus_Object=MibTableColumn
zxAnVlanBasedFwdRowStatus=_ZxAnVlanBasedFwdRowStatus_Object((1,3,6,1,4,1,3902,1015,20,18,1,100),_ZxAnVlanBasedFwdRowStatus_Type())
zxAnVlanBasedFwdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanBasedFwdRowStatus.setStatus(_A)
_ZxAnVlanExQinQSupportEIGMP_Type=TruthValue
_ZxAnVlanExQinQSupportEIGMP_Object=MibScalar
zxAnVlanExQinQSupportEIGMP=_ZxAnVlanExQinQSupportEIGMP_Object((1,3,6,1,4,1,3902,1015,20,22),_ZxAnVlanExQinQSupportEIGMP_Type())
zxAnVlanExQinQSupportEIGMP.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanExQinQSupportEIGMP.setStatus(_A)
class _ZxAnVlanGlobalCtagTpid_Type(DisplayString):defaultValue=OctetString(_d)
_ZxAnVlanGlobalCtagTpid_Type.__name__=_J
_ZxAnVlanGlobalCtagTpid_Object=MibScalar
zxAnVlanGlobalCtagTpid=_ZxAnVlanGlobalCtagTpid_Object((1,3,6,1,4,1,3902,1015,20,23),_ZxAnVlanGlobalCtagTpid_Type())
zxAnVlanGlobalCtagTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanGlobalCtagTpid.setStatus(_A)
class _ZxAnVlanGlobalTpid_Type(DisplayString):defaultValue=OctetString(_d)
_ZxAnVlanGlobalTpid_Type.__name__=_J
_ZxAnVlanGlobalTpid_Object=MibScalar
zxAnVlanGlobalTpid=_ZxAnVlanGlobalTpid_Object((1,3,6,1,4,1,3902,1015,20,24),_ZxAnVlanGlobalTpid_Type())
zxAnVlanGlobalTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanGlobalTpid.setStatus(_A)
_ZxAnOnuMngVlanTable_Object=MibTable
zxAnOnuMngVlanTable=_ZxAnOnuMngVlanTable_Object((1,3,6,1,4,1,3902,1015,20,25))
if mibBuilder.loadTexts:zxAnOnuMngVlanTable.setStatus(_A)
_ZxAnOnuMngVlanEntry_Object=MibTableRow
zxAnOnuMngVlanEntry=_ZxAnOnuMngVlanEntry_Object((1,3,6,1,4,1,3902,1015,20,25,1))
zxAnOnuMngVlanEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:zxAnOnuMngVlanEntry.setStatus(_A)
_ZxAnOnuMngVlan_Type=VlanId
_ZxAnOnuMngVlan_Object=MibTableColumn
zxAnOnuMngVlan=_ZxAnOnuMngVlan_Object((1,3,6,1,4,1,3902,1015,20,25,1,1),_ZxAnOnuMngVlan_Type())
zxAnOnuMngVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnOnuMngVlan.setStatus(_A)
_ZxAnOnuMngVlanRowStatus_Type=RowStatus
_ZxAnOnuMngVlanRowStatus_Object=MibTableColumn
zxAnOnuMngVlanRowStatus=_ZxAnOnuMngVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,20,25,1,20),_ZxAnOnuMngVlanRowStatus_Type())
zxAnOnuMngVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnOnuMngVlanRowStatus.setStatus(_A)
_ZxAnIpRouteVlanTable_Object=MibTable
zxAnIpRouteVlanTable=_ZxAnIpRouteVlanTable_Object((1,3,6,1,4,1,3902,1015,20,26))
if mibBuilder.loadTexts:zxAnIpRouteVlanTable.setStatus(_A)
_ZxAnIpRouteVlanEntry_Object=MibTableRow
zxAnIpRouteVlanEntry=_ZxAnIpRouteVlanEntry_Object((1,3,6,1,4,1,3902,1015,20,26,1))
zxAnIpRouteVlanEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:zxAnIpRouteVlanEntry.setStatus(_A)
_ZxAnIpRouteVlan_Type=VlanId
_ZxAnIpRouteVlan_Object=MibTableColumn
zxAnIpRouteVlan=_ZxAnIpRouteVlan_Object((1,3,6,1,4,1,3902,1015,20,26,1,1),_ZxAnIpRouteVlan_Type())
zxAnIpRouteVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIpRouteVlan.setStatus(_A)
_ZxAnIpRouteVlanRowStatus_Type=RowStatus
_ZxAnIpRouteVlanRowStatus_Object=MibTableColumn
zxAnIpRouteVlanRowStatus=_ZxAnIpRouteVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,20,26,1,20),_ZxAnIpRouteVlanRowStatus_Type())
zxAnIpRouteVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIpRouteVlanRowStatus.setStatus(_A)
_ZxAnVlanInterfaceTable_Object=MibTable
zxAnVlanInterfaceTable=_ZxAnVlanInterfaceTable_Object((1,3,6,1,4,1,3902,1015,20,27))
if mibBuilder.loadTexts:zxAnVlanInterfaceTable.setStatus(_A)
_ZxAnVlanInterfaceEntry_Object=MibTableRow
zxAnVlanInterfaceEntry=_ZxAnVlanInterfaceEntry_Object((1,3,6,1,4,1,3902,1015,20,27,1))
zxAnVlanInterfaceEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:zxAnVlanInterfaceEntry.setStatus(_A)
_ZxAnVlanInterfaceVlanId_Type=VlanId
_ZxAnVlanInterfaceVlanId_Object=MibTableColumn
zxAnVlanInterfaceVlanId=_ZxAnVlanInterfaceVlanId_Object((1,3,6,1,4,1,3902,1015,20,27,1,1),_ZxAnVlanInterfaceVlanId_Type())
zxAnVlanInterfaceVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanInterfaceVlanId.setStatus(_A)
_ZxAnVlanBroadcastRateLimit_Type=Integer32
_ZxAnVlanBroadcastRateLimit_Object=MibTableColumn
zxAnVlanBroadcastRateLimit=_ZxAnVlanBroadcastRateLimit_Object((1,3,6,1,4,1,3902,1015,20,27,1,5),_ZxAnVlanBroadcastRateLimit_Type())
zxAnVlanBroadcastRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanBroadcastRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnVlanBroadcastRateLimit.setUnits('kbps')
_ZxAnPortMvlanTranslateTable_Object=MibTable
zxAnPortMvlanTranslateTable=_ZxAnPortMvlanTranslateTable_Object((1,3,6,1,4,1,3902,1015,20,28))
if mibBuilder.loadTexts:zxAnPortMvlanTranslateTable.setStatus(_A)
_ZxAnPortMvlanTranslateEntry_Object=MibTableRow
zxAnPortMvlanTranslateEntry=_ZxAnPortMvlanTranslateEntry_Object((1,3,6,1,4,1,3902,1015,20,28,1))
zxAnPortMvlanTranslateEntry.setIndexNames((0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:zxAnPortMvlanTranslateEntry.setStatus(_A)
_ZxAnPortMvlanTranslateIfIndex_Type=ZxAnIfindex
_ZxAnPortMvlanTranslateIfIndex_Object=MibTableColumn
zxAnPortMvlanTranslateIfIndex=_ZxAnPortMvlanTranslateIfIndex_Object((1,3,6,1,4,1,3902,1015,20,28,1,1),_ZxAnPortMvlanTranslateIfIndex_Type())
zxAnPortMvlanTranslateIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPortMvlanTranslateIfIndex.setStatus(_A)
_ZxAnPortMvlanTranslateMvlan_Type=VlanId
_ZxAnPortMvlanTranslateMvlan_Object=MibTableColumn
zxAnPortMvlanTranslateMvlan=_ZxAnPortMvlanTranslateMvlan_Object((1,3,6,1,4,1,3902,1015,20,28,1,2),_ZxAnPortMvlanTranslateMvlan_Type())
zxAnPortMvlanTranslateMvlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPortMvlanTranslateMvlan.setStatus(_A)
class _ZxAnPortMvlanTranslateCvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnPortMvlanTranslateCvlan_Type.__name__=_C
_ZxAnPortMvlanTranslateCvlan_Object=MibTableColumn
zxAnPortMvlanTranslateCvlan=_ZxAnPortMvlanTranslateCvlan_Object((1,3,6,1,4,1,3902,1015,20,28,1,3),_ZxAnPortMvlanTranslateCvlan_Type())
zxAnPortMvlanTranslateCvlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPortMvlanTranslateCvlan.setStatus(_A)
_ZxAnMVlanIfTransRowStatus_Type=RowStatus
_ZxAnMVlanIfTransRowStatus_Object=MibTableColumn
zxAnMVlanIfTransRowStatus=_ZxAnMVlanIfTransRowStatus_Object((1,3,6,1,4,1,3902,1015,20,28,1,10),_ZxAnMVlanIfTransRowStatus_Type())
zxAnMVlanIfTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMVlanIfTransRowStatus.setStatus(_A)
_ZxAnVlanIfProtoMapEnableTable_Object=MibTable
zxAnVlanIfProtoMapEnableTable=_ZxAnVlanIfProtoMapEnableTable_Object((1,3,6,1,4,1,3902,1015,20,29))
if mibBuilder.loadTexts:zxAnVlanIfProtoMapEnableTable.setStatus(_A)
_ZxAnVlanIfProtoMapEnableEntry_Object=MibTableRow
zxAnVlanIfProtoMapEnableEntry=_ZxAnVlanIfProtoMapEnableEntry_Object((1,3,6,1,4,1,3902,1015,20,29,1))
zxAnVlanIfProtoMapEnableEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:zxAnVlanIfProtoMapEnableEntry.setStatus(_A)
_ZxAnProtocolVlanPortIfIndex_Type=ZxAnIfindex
_ZxAnProtocolVlanPortIfIndex_Object=MibTableColumn
zxAnProtocolVlanPortIfIndex=_ZxAnProtocolVlanPortIfIndex_Object((1,3,6,1,4,1,3902,1015,20,29,1,1),_ZxAnProtocolVlanPortIfIndex_Type())
zxAnProtocolVlanPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnProtocolVlanPortIfIndex.setStatus(_A)
class _ZxAnVlanIfProtoMapEnable_Type(TruthValue):defaultValue=2
_ZxAnVlanIfProtoMapEnable_Type.__name__=_N
_ZxAnVlanIfProtoMapEnable_Object=MibTableColumn
zxAnVlanIfProtoMapEnable=_ZxAnVlanIfProtoMapEnable_Object((1,3,6,1,4,1,3902,1015,20,29,1,2),_ZxAnVlanIfProtoMapEnable_Type())
zxAnVlanIfProtoMapEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfProtoMapEnable.setStatus(_A)
_ZxAnInternalVlanTable_Object=MibTable
zxAnInternalVlanTable=_ZxAnInternalVlanTable_Object((1,3,6,1,4,1,3902,1015,20,30))
if mibBuilder.loadTexts:zxAnInternalVlanTable.setStatus(_A)
_ZxAnInternalVlanEntry_Object=MibTableRow
zxAnInternalVlanEntry=_ZxAnInternalVlanEntry_Object((1,3,6,1,4,1,3902,1015,20,30,1))
zxAnInternalVlanEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:zxAnInternalVlanEntry.setStatus(_A)
class _ZxAnInternalVlanServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vpn',1),('voipUpstream',2),('voipDownstream',3),('ieee1588',4),('gpon',5)))
_ZxAnInternalVlanServiceType_Type.__name__=_C
_ZxAnInternalVlanServiceType_Object=MibTableColumn
zxAnInternalVlanServiceType=_ZxAnInternalVlanServiceType_Object((1,3,6,1,4,1,3902,1015,20,30,1,1),_ZxAnInternalVlanServiceType_Type())
zxAnInternalVlanServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnInternalVlanServiceType.setStatus(_A)
_ZxAnInternalVlanList_Type=DisplayString
_ZxAnInternalVlanList_Object=MibTableColumn
zxAnInternalVlanList=_ZxAnInternalVlanList_Object((1,3,6,1,4,1,3902,1015,20,30,1,2),_ZxAnInternalVlanList_Type())
zxAnInternalVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnInternalVlanList.setStatus(_A)
_ZxAnInternalVlanRowStatus_Type=RowStatus
_ZxAnInternalVlanRowStatus_Object=MibTableColumn
zxAnInternalVlanRowStatus=_ZxAnInternalVlanRowStatus_Object((1,3,6,1,4,1,3902,1015,20,30,1,20),_ZxAnInternalVlanRowStatus_Type())
zxAnInternalVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnInternalVlanRowStatus.setStatus(_A)
_ZxAnVlanExQinQOnuGroupTable_Object=MibTable
zxAnVlanExQinQOnuGroupTable=_ZxAnVlanExQinQOnuGroupTable_Object((1,3,6,1,4,1,3902,1015,20,31))
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupTable.setStatus(_A)
_ZxAnVlanExQinQOnuGroupEntry_Object=MibTableRow
zxAnVlanExQinQOnuGroupEntry=_ZxAnVlanExQinQOnuGroupEntry_Object((1,3,6,1,4,1,3902,1015,20,31,1))
zxAnVlanExQinQOnuGroupEntry.setIndexNames((0,_D,_m),(0,_D,_n))
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupEntry.setStatus(_A)
_ZxAnVlanExQinQPonPortIndex_Type=ZxAnIfindex
_ZxAnVlanExQinQPonPortIndex_Object=MibTableColumn
zxAnVlanExQinQPonPortIndex=_ZxAnVlanExQinQPonPortIndex_Object((1,3,6,1,4,1,3902,1015,20,31,1,1),_ZxAnVlanExQinQPonPortIndex_Type())
zxAnVlanExQinQPonPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanExQinQPonPortIndex.setStatus(_A)
class _ZxAnVlanExQinQOnuGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ZxAnVlanExQinQOnuGroupId_Type.__name__=_C
_ZxAnVlanExQinQOnuGroupId_Object=MibTableColumn
zxAnVlanExQinQOnuGroupId=_ZxAnVlanExQinQOnuGroupId_Object((1,3,6,1,4,1,3902,1015,20,31,1,2),_ZxAnVlanExQinQOnuGroupId_Type())
zxAnVlanExQinQOnuGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupId.setStatus(_A)
class _ZxAnVlanExQinQOnuGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnVlanExQinQOnuGroupName_Type.__name__=_J
_ZxAnVlanExQinQOnuGroupName_Object=MibTableColumn
zxAnVlanExQinQOnuGroupName=_ZxAnVlanExQinQOnuGroupName_Object((1,3,6,1,4,1,3902,1015,20,31,1,3),_ZxAnVlanExQinQOnuGroupName_Type())
zxAnVlanExQinQOnuGroupName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupName.setStatus(_A)
_ZxAnVlanExQinQOnuGroupResVlan_Type=Integer32
_ZxAnVlanExQinQOnuGroupResVlan_Object=MibTableColumn
zxAnVlanExQinQOnuGroupResVlan=_ZxAnVlanExQinQOnuGroupResVlan_Object((1,3,6,1,4,1,3902,1015,20,31,1,4),_ZxAnVlanExQinQOnuGroupResVlan_Type())
zxAnVlanExQinQOnuGroupResVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupResVlan.setStatus(_A)
_ZxAnVlanExQinQOnuGroupMembers_Type=DisplayString
_ZxAnVlanExQinQOnuGroupMembers_Object=MibTableColumn
zxAnVlanExQinQOnuGroupMembers=_ZxAnVlanExQinQOnuGroupMembers_Object((1,3,6,1,4,1,3902,1015,20,31,1,5),_ZxAnVlanExQinQOnuGroupMembers_Type())
zxAnVlanExQinQOnuGroupMembers.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanExQinQOnuGroupMembers.setStatus(_A)
_ZxAnVlanTpidObjects_ObjectIdentity=ObjectIdentity
zxAnVlanTpidObjects=_ZxAnVlanTpidObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,32))
_ZxAnVlanTpidTable_Object=MibTable
zxAnVlanTpidTable=_ZxAnVlanTpidTable_Object((1,3,6,1,4,1,3902,1015,20,32,2))
if mibBuilder.loadTexts:zxAnVlanTpidTable.setStatus('deprecated')
_ZxAnVlanTpidEntry_Object=MibTableRow
zxAnVlanTpidEntry=_ZxAnVlanTpidEntry_Object((1,3,6,1,4,1,3902,1015,20,32,2,1))
zxAnVlanTpidEntry.setIndexNames((0,_D,_K),(0,_D,_o),(0,_D,_p))
if mibBuilder.loadTexts:zxAnVlanTpidEntry.setStatus(_A)
class _ZxAnVlanTpidSVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnVlanTpidSVlanId_Type.__name__=_C
_ZxAnVlanTpidSVlanId_Object=MibTableColumn
zxAnVlanTpidSVlanId=_ZxAnVlanTpidSVlanId_Object((1,3,6,1,4,1,3902,1015,20,32,2,1,1),_ZxAnVlanTpidSVlanId_Type())
zxAnVlanTpidSVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanTpidSVlanId.setStatus(_A)
class _ZxAnVlanTpidCVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanTpidCVlanId_Type.__name__=_C
_ZxAnVlanTpidCVlanId_Object=MibTableColumn
zxAnVlanTpidCVlanId=_ZxAnVlanTpidCVlanId_Object((1,3,6,1,4,1,3902,1015,20,32,2,1,2),_ZxAnVlanTpidCVlanId_Type())
zxAnVlanTpidCVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanTpidCVlanId.setStatus(_A)
class _ZxAnVlanTpid_Type(Integer32):defaultValue=33024
_ZxAnVlanTpid_Type.__name__=_C
_ZxAnVlanTpid_Object=MibTableColumn
zxAnVlanTpid=_ZxAnVlanTpid_Object((1,3,6,1,4,1,3902,1015,20,32,2,1,3),_ZxAnVlanTpid_Type())
zxAnVlanTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTpid.setStatus(_A)
_ZxAnVlanTpidRowStatus_Type=RowStatus
_ZxAnVlanTpidRowStatus_Object=MibTableColumn
zxAnVlanTpidRowStatus=_ZxAnVlanTpidRowStatus_Object((1,3,6,1,4,1,3902,1015,20,32,2,1,50),_ZxAnVlanTpidRowStatus_Type())
zxAnVlanTpidRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTpidRowStatus.setStatus(_A)
_ZxAnIeee1588VlanTable_Object=MibTable
zxAnIeee1588VlanTable=_ZxAnIeee1588VlanTable_Object((1,3,6,1,4,1,3902,1015,20,33))
if mibBuilder.loadTexts:zxAnIeee1588VlanTable.setStatus(_A)
_ZxAnIeee1588VlanEntry_Object=MibTableRow
zxAnIeee1588VlanEntry=_ZxAnIeee1588VlanEntry_Object((1,3,6,1,4,1,3902,1015,20,33,1))
zxAnIeee1588VlanEntry.setIndexNames((0,_D,_q))
if mibBuilder.loadTexts:zxAnIeee1588VlanEntry.setStatus(_A)
_ZxAnIeee1588Vlan_Type=VlanId
_ZxAnIeee1588Vlan_Object=MibTableColumn
zxAnIeee1588Vlan=_ZxAnIeee1588Vlan_Object((1,3,6,1,4,1,3902,1015,20,33,1,1),_ZxAnIeee1588Vlan_Type())
zxAnIeee1588Vlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnIeee1588Vlan.setStatus(_A)
_ZxAnIeee1588VlanRowStatus_Type=RowStatus
_ZxAnIeee1588VlanRowStatus_Object=MibTableColumn
zxAnIeee1588VlanRowStatus=_ZxAnIeee1588VlanRowStatus_Object((1,3,6,1,4,1,3902,1015,20,33,1,50),_ZxAnIeee1588VlanRowStatus_Type())
zxAnIeee1588VlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnIeee1588VlanRowStatus.setStatus(_A)
_ZxAnMVlanGlobalTransTable_Object=MibTable
zxAnMVlanGlobalTransTable=_ZxAnMVlanGlobalTransTable_Object((1,3,6,1,4,1,3902,1015,20,34))
if mibBuilder.loadTexts:zxAnMVlanGlobalTransTable.setStatus(_A)
_ZxAnMVlanGlobalTransEntry_Object=MibTableRow
zxAnMVlanGlobalTransEntry=_ZxAnMVlanGlobalTransEntry_Object((1,3,6,1,4,1,3902,1015,20,34,1))
zxAnMVlanGlobalTransEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:zxAnMVlanGlobalTransEntry.setStatus(_A)
_ZxAnMVlanGlobalTransMVid_Type=VlanId
_ZxAnMVlanGlobalTransMVid_Object=MibTableColumn
zxAnMVlanGlobalTransMVid=_ZxAnMVlanGlobalTransMVid_Object((1,3,6,1,4,1,3902,1015,20,34,1,1),_ZxAnMVlanGlobalTransMVid_Type())
zxAnMVlanGlobalTransMVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMVlanGlobalTransMVid.setStatus(_A)
class _ZxAnMVlanGlobalTransCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnMVlanGlobalTransCVid_Type.__name__=_C
_ZxAnMVlanGlobalTransCVid_Object=MibTableColumn
zxAnMVlanGlobalTransCVid=_ZxAnMVlanGlobalTransCVid_Object((1,3,6,1,4,1,3902,1015,20,34,1,2),_ZxAnMVlanGlobalTransCVid_Type())
zxAnMVlanGlobalTransCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMVlanGlobalTransCVid.setStatus(_A)
_ZxAnMVlanGlobalTransRowStatus_Type=RowStatus
_ZxAnMVlanGlobalTransRowStatus_Object=MibTableColumn
zxAnMVlanGlobalTransRowStatus=_ZxAnMVlanGlobalTransRowStatus_Object((1,3,6,1,4,1,3902,1015,20,34,1,20),_ZxAnMVlanGlobalTransRowStatus_Type())
zxAnMVlanGlobalTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnMVlanGlobalTransRowStatus.setStatus(_A)
_ZxAnVlanStormCtrlTable_Object=MibTable
zxAnVlanStormCtrlTable=_ZxAnVlanStormCtrlTable_Object((1,3,6,1,4,1,3902,1015,20,35))
if mibBuilder.loadTexts:zxAnVlanStormCtrlTable.setStatus(_A)
_ZxAnVlanStormCtrlEntry_Object=MibTableRow
zxAnVlanStormCtrlEntry=_ZxAnVlanStormCtrlEntry_Object((1,3,6,1,4,1,3902,1015,20,35,1))
zxAnVlanStormCtrlEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:zxAnVlanStormCtrlEntry.setStatus(_A)
class _ZxAnVlanMulticastFloodCtrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('floodUnknown',1),('dropUnknown',2),('floodAll',3)))
_ZxAnVlanMulticastFloodCtrl_Type.__name__=_C
_ZxAnVlanMulticastFloodCtrl_Object=MibTableColumn
zxAnVlanMulticastFloodCtrl=_ZxAnVlanMulticastFloodCtrl_Object((1,3,6,1,4,1,3902,1015,20,35,1,1),_ZxAnVlanMulticastFloodCtrl_Type())
zxAnVlanMulticastFloodCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanMulticastFloodCtrl.setStatus(_A)
_ZxAnVlanTagPortListTable_Object=MibTable
zxAnVlanTagPortListTable=_ZxAnVlanTagPortListTable_Object((1,3,6,1,4,1,3902,1015,20,36))
if mibBuilder.loadTexts:zxAnVlanTagPortListTable.setStatus(_A)
_ZxAnVlanTagPortListEntry_Object=MibTableRow
zxAnVlanTagPortListEntry=_ZxAnVlanTagPortListEntry_Object((1,3,6,1,4,1,3902,1015,20,36,1))
zxAnVlanTagPortListEntry.setIndexNames((0,_D,_s),(0,_D,_t),(0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:zxAnVlanTagPortListEntry.setStatus(_A)
class _ZxAnVlanStag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanStag_Type.__name__=_C
_ZxAnVlanStag_Object=MibTableColumn
zxAnVlanStag=_ZxAnVlanStag_Object((1,3,6,1,4,1,3902,1015,20,36,1,1),_ZxAnVlanStag_Type())
zxAnVlanStag.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanStag.setStatus(_A)
class _ZxAnVlanCtag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanCtag_Type.__name__=_C
_ZxAnVlanCtag_Object=MibTableColumn
zxAnVlanCtag=_ZxAnVlanCtag_Object((1,3,6,1,4,1,3902,1015,20,36,1,2),_ZxAnVlanCtag_Type())
zxAnVlanCtag.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanCtag.setStatus(_A)
_ZxAnVlanTagShelf_Type=Integer32
_ZxAnVlanTagShelf_Object=MibTableColumn
zxAnVlanTagShelf=_ZxAnVlanTagShelf_Object((1,3,6,1,4,1,3902,1015,20,36,1,3),_ZxAnVlanTagShelf_Type())
zxAnVlanTagShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanTagShelf.setStatus(_A)
_ZxAnVlanTagSlot_Type=Integer32
_ZxAnVlanTagSlot_Object=MibTableColumn
zxAnVlanTagSlot=_ZxAnVlanTagSlot_Object((1,3,6,1,4,1,3902,1015,20,36,1,4),_ZxAnVlanTagSlot_Type())
zxAnVlanTagSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanTagSlot.setStatus(_A)
_ZxAnVlanTagPortList_Type=ZxAnPortList
_ZxAnVlanTagPortList_Object=MibTableColumn
zxAnVlanTagPortList=_ZxAnVlanTagPortList_Object((1,3,6,1,4,1,3902,1015,20,36,1,5),_ZxAnVlanTagPortList_Type())
zxAnVlanTagPortList.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanTagPortList.setStatus(_A)
_ZxAnVlanConfTpidTable_Object=MibTable
zxAnVlanConfTpidTable=_ZxAnVlanConfTpidTable_Object((1,3,6,1,4,1,3902,1015,20,37))
if mibBuilder.loadTexts:zxAnVlanConfTpidTable.setStatus(_A)
_ZxAnVlanConfTpidEntry_Object=MibTableRow
zxAnVlanConfTpidEntry=_ZxAnVlanConfTpidEntry_Object((1,3,6,1,4,1,3902,1015,20,37,1))
zxAnVlanConfTpidEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:zxAnVlanConfTpidEntry.setStatus(_A)
_ZxAnVlanTpidConfTpid_Type=Integer32
_ZxAnVlanTpidConfTpid_Object=MibTableColumn
zxAnVlanTpidConfTpid=_ZxAnVlanTpidConfTpid_Object((1,3,6,1,4,1,3902,1015,20,37,1,1),_ZxAnVlanTpidConfTpid_Type())
zxAnVlanTpidConfTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTpidConfTpid.setStatus(_A)
_ZxAnVlanTpidConfRowStatus_Type=RowStatus
_ZxAnVlanTpidConfRowStatus_Object=MibTableColumn
zxAnVlanTpidConfRowStatus=_ZxAnVlanTpidConfRowStatus_Object((1,3,6,1,4,1,3902,1015,20,37,1,50),_ZxAnVlanTpidConfRowStatus_Type())
zxAnVlanTpidConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanTpidConfRowStatus.setStatus(_A)
_ZxAnVlanRuledTransGroup_ObjectIdentity=ObjectIdentity
zxAnVlanRuledTransGroup=_ZxAnVlanRuledTransGroup_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,38))
_ZxAnVlanRuledTransTable_Object=MibTable
zxAnVlanRuledTransTable=_ZxAnVlanRuledTransTable_Object((1,3,6,1,4,1,3902,1015,20,38,2))
if mibBuilder.loadTexts:zxAnVlanRuledTransTable.setStatus(_A)
_ZxAnVlanRuledTransEntry_Object=MibTableRow
zxAnVlanRuledTransEntry=_ZxAnVlanRuledTransEntry_Object((1,3,6,1,4,1,3902,1015,20,38,2,1))
zxAnVlanRuledTransEntry.setIndexNames((0,_D,_K),(0,_D,_w),(0,_D,_x))
if mibBuilder.loadTexts:zxAnVlanRuledTransEntry.setStatus(_A)
class _ZxAnVlanRuledTransSVid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanRuledTransSVid_Type.__name__=_C
_ZxAnVlanRuledTransSVid_Object=MibTableColumn
zxAnVlanRuledTransSVid=_ZxAnVlanRuledTransSVid_Object((1,3,6,1,4,1,3902,1015,20,38,2,1,1),_ZxAnVlanRuledTransSVid_Type())
zxAnVlanRuledTransSVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanRuledTransSVid.setStatus(_A)
class _ZxAnVlanRuledTransCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanRuledTransCVid_Type.__name__=_C
_ZxAnVlanRuledTransCVid_Object=MibTableColumn
zxAnVlanRuledTransCVid=_ZxAnVlanRuledTransCVid_Object((1,3,6,1,4,1,3902,1015,20,38,2,1,2),_ZxAnVlanRuledTransCVid_Type())
zxAnVlanRuledTransCVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanRuledTransCVid.setStatus(_A)
class _ZxAnVlanRuledTransUserVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanRuledTransUserVid_Type.__name__=_C
_ZxAnVlanRuledTransUserVid_Object=MibTableColumn
zxAnVlanRuledTransUserVid=_ZxAnVlanRuledTransUserVid_Object((1,3,6,1,4,1,3902,1015,20,38,2,1,3),_ZxAnVlanRuledTransUserVid_Type())
zxAnVlanRuledTransUserVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRuledTransUserVid.setStatus(_A)
_ZxAnVlanRuledTransRowStatus_Type=RowStatus
_ZxAnVlanRuledTransRowStatus_Object=MibTableColumn
zxAnVlanRuledTransRowStatus=_ZxAnVlanRuledTransRowStatus_Object((1,3,6,1,4,1,3902,1015,20,38,2,1,50),_ZxAnVlanRuledTransRowStatus_Type())
zxAnVlanRuledTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanRuledTransRowStatus.setStatus(_A)
_ZxAnVlanIfCosMapObjects_ObjectIdentity=ObjectIdentity
zxAnVlanIfCosMapObjects=_ZxAnVlanIfCosMapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,39))
_ZxAnVlanIfCosMapEnableTable_Object=MibTable
zxAnVlanIfCosMapEnableTable=_ZxAnVlanIfCosMapEnableTable_Object((1,3,6,1,4,1,3902,1015,20,39,2))
if mibBuilder.loadTexts:zxAnVlanIfCosMapEnableTable.setStatus(_A)
_ZxAnVlanIfCosMapEnableEntry_Object=MibTableRow
zxAnVlanIfCosMapEnableEntry=_ZxAnVlanIfCosMapEnableEntry_Object((1,3,6,1,4,1,3902,1015,20,39,2,1))
zxAnVlanIfCosMapEnableEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:zxAnVlanIfCosMapEnableEntry.setStatus(_A)
class _ZxAnVlanIfCosMapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnVlanIfCosMapEnable_Type.__name__=_C
_ZxAnVlanIfCosMapEnable_Object=MibTableColumn
zxAnVlanIfCosMapEnable=_ZxAnVlanIfCosMapEnable_Object((1,3,6,1,4,1,3902,1015,20,39,2,1,1),_ZxAnVlanIfCosMapEnable_Type())
zxAnVlanIfCosMapEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVlanIfCosMapEnable.setStatus(_A)
_ZxAnVlanIfCosMapTable_Object=MibTable
zxAnVlanIfCosMapTable=_ZxAnVlanIfCosMapTable_Object((1,3,6,1,4,1,3902,1015,20,39,3))
if mibBuilder.loadTexts:zxAnVlanIfCosMapTable.setStatus(_A)
_ZxAnVlanIfCosMapEntry_Object=MibTableRow
zxAnVlanIfCosMapEntry=_ZxAnVlanIfCosMapEntry_Object((1,3,6,1,4,1,3902,1015,20,39,3,1))
zxAnVlanIfCosMapEntry.setIndexNames((0,_D,_K),(0,_D,_y))
if mibBuilder.loadTexts:zxAnVlanIfCosMapEntry.setStatus(_A)
class _ZxAnVlanIfCosMapCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnVlanIfCosMapCos_Type.__name__=_C
_ZxAnVlanIfCosMapCos_Object=MibTableColumn
zxAnVlanIfCosMapCos=_ZxAnVlanIfCosMapCos_Object((1,3,6,1,4,1,3902,1015,20,39,3,1,1),_ZxAnVlanIfCosMapCos_Type())
zxAnVlanIfCosMapCos.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanIfCosMapCos.setStatus(_A)
class _ZxAnVlanIfCosMapSVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnVlanIfCosMapSVid_Type.__name__=_C
_ZxAnVlanIfCosMapSVid_Object=MibTableColumn
zxAnVlanIfCosMapSVid=_ZxAnVlanIfCosMapSVid_Object((1,3,6,1,4,1,3902,1015,20,39,3,1,2),_ZxAnVlanIfCosMapSVid_Type())
zxAnVlanIfCosMapSVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfCosMapSVid.setStatus(_A)
class _ZxAnVlanIfCosMapCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanIfCosMapCVid_Type.__name__=_C
_ZxAnVlanIfCosMapCVid_Object=MibTableColumn
zxAnVlanIfCosMapCVid=_ZxAnVlanIfCosMapCVid_Object((1,3,6,1,4,1,3902,1015,20,39,3,1,3),_ZxAnVlanIfCosMapCVid_Type())
zxAnVlanIfCosMapCVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfCosMapCVid.setStatus(_A)
_ZxAnVlanIfCosMapRowStatus_Type=RowStatus
_ZxAnVlanIfCosMapRowStatus_Object=MibTableColumn
zxAnVlanIfCosMapRowStatus=_ZxAnVlanIfCosMapRowStatus_Object((1,3,6,1,4,1,3902,1015,20,39,3,1,50),_ZxAnVlanIfCosMapRowStatus_Type())
zxAnVlanIfCosMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanIfCosMapRowStatus.setStatus(_A)
_ZxAnVlanBasedForwardObjects_ObjectIdentity=ObjectIdentity
zxAnVlanBasedForwardObjects=_ZxAnVlanBasedForwardObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,40))
_ZxAnVlanBasedForwardTable_Object=MibTable
zxAnVlanBasedForwardTable=_ZxAnVlanBasedForwardTable_Object((1,3,6,1,4,1,3902,1015,20,40,2))
if mibBuilder.loadTexts:zxAnVlanBasedForwardTable.setStatus(_A)
_ZxAnVlanBasedForwardEntry_Object=MibTableRow
zxAnVlanBasedForwardEntry=_ZxAnVlanBasedForwardEntry_Object((1,3,6,1,4,1,3902,1015,20,40,2,1))
zxAnVlanBasedForwardEntry.setIndexNames((0,_D,_z),(0,_D,_A0))
if mibBuilder.loadTexts:zxAnVlanBasedForwardEntry.setStatus(_A)
_ZxAnVlanBasedForwardSVid_Type=VlanId
_ZxAnVlanBasedForwardSVid_Object=MibTableColumn
zxAnVlanBasedForwardSVid=_ZxAnVlanBasedForwardSVid_Object((1,3,6,1,4,1,3902,1015,20,40,2,1,1),_ZxAnVlanBasedForwardSVid_Type())
zxAnVlanBasedForwardSVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanBasedForwardSVid.setStatus(_A)
class _ZxAnVlanBasedForwardCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxAnVlanBasedForwardCVid_Type.__name__=_C
_ZxAnVlanBasedForwardCVid_Object=MibTableColumn
zxAnVlanBasedForwardCVid=_ZxAnVlanBasedForwardCVid_Object((1,3,6,1,4,1,3902,1015,20,40,2,1,2),_ZxAnVlanBasedForwardCVid_Type())
zxAnVlanBasedForwardCVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVlanBasedForwardCVid.setStatus(_A)
_ZxAnVlanBasedForwardIfIndex_Type=ZxAnIfindex
_ZxAnVlanBasedForwardIfIndex_Object=MibTableColumn
zxAnVlanBasedForwardIfIndex=_ZxAnVlanBasedForwardIfIndex_Object((1,3,6,1,4,1,3902,1015,20,40,2,1,3),_ZxAnVlanBasedForwardIfIndex_Type())
zxAnVlanBasedForwardIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanBasedForwardIfIndex.setStatus(_A)
_ZxAnVlanBasedForwardUplinkPort_Type=ZxAnIfindex
_ZxAnVlanBasedForwardUplinkPort_Object=MibTableColumn
zxAnVlanBasedForwardUplinkPort=_ZxAnVlanBasedForwardUplinkPort_Object((1,3,6,1,4,1,3902,1015,20,40,2,1,4),_ZxAnVlanBasedForwardUplinkPort_Type())
zxAnVlanBasedForwardUplinkPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanBasedForwardUplinkPort.setStatus(_A)
_ZxAnVlanBasedForwardRowStatus_Type=RowStatus
_ZxAnVlanBasedForwardRowStatus_Object=MibTableColumn
zxAnVlanBasedForwardRowStatus=_ZxAnVlanBasedForwardRowStatus_Object((1,3,6,1,4,1,3902,1015,20,40,2,1,50),_ZxAnVlanBasedForwardRowStatus_Type())
zxAnVlanBasedForwardRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnVlanBasedForwardRowStatus.setStatus(_A)
_ZxAnVlanGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVlanGlobalObjects=_ZxAnVlanGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,20,99))
class _ZxAnVlanCapabilities_Type(Bits):namedValues=NamedValues(('supportBasedForwardObjects',0))
_ZxAnVlanCapabilities_Type.__name__=_M
_ZxAnVlanCapabilities_Object=MibScalar
zxAnVlanCapabilities=_ZxAnVlanCapabilities_Object((1,3,6,1,4,1,3902,1015,20,99,1),_ZxAnVlanCapabilities_Type())
zxAnVlanCapabilities.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanCapabilities.setStatus(_A)
_ZxAnVlanMibEnd_Type=Integer32
_ZxAnVlanMibEnd_Object=MibScalar
zxAnVlanMibEnd=_ZxAnVlanMibEnd_Object((1,3,6,1,4,1,3902,1015,20,100),_ZxAnVlanMibEnd_Type())
zxAnVlanMibEnd.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVlanMibEnd.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnVlanMib':zxAnVlanMib,'zxAnVlanNum':zxAnVlanNum,'zxAnVlanTable':zxAnVlanTable,'zxAnVlanEntry':zxAnVlanEntry,_L:zxAnVlanId,'zxAnVlanName':zxAnVlanName,'zxAnVlanTransparent':zxAnVlanTransparent,'zxAnVlanRowStatus':zxAnVlanRowStatus,'zxAnVlanXconnect':zxAnVlanXconnect,'zxAnVlanDesc':zxAnVlanDesc,'zxAnVlanPortTable':zxAnVlanPortTable,'zxAnVlanPortEntry':zxAnVlanPortEntry,_K:zxAnVlanPortIndex,'zxAnVlanIfConfMode':zxAnVlanIfConfMode,'zxAnVlanIfConfTlsEnable':zxAnVlanIfConfTlsEnable,'zxAnVlanIfConfTlsSVid':zxAnVlanIfConfTlsSVid,'zxAnVlanIfConfDefaultVid':zxAnVlanIfConfDefaultVid,'zxAnVlanIfConfDefaultCVid':zxAnVlanIfConfDefaultCVid,'zxAnVlanIfConfUntaggedVlanList':zxAnVlanIfConfUntaggedVlanList,'zxAnVlanIfConfTaggedVlanList':zxAnVlanIfConfTaggedVlanList,'zxAnVlanIfConfTpid':zxAnVlanIfConfTpid,'zxAnVlanIfIngressFilterEnable':zxAnVlanIfIngressFilterEnable,'zxAnVlanIfAcceptableFrameTypes':zxAnVlanIfAcceptableFrameTypes,'zxAnVlanIfConfTpidEnable':zxAnVlanIfConfTpidEnable,'zxAnVlanIfConfVlanCmdTable':zxAnVlanIfConfVlanCmdTable,'zxAnVlanIfConfVlanCmdEntry':zxAnVlanIfConfVlanCmdEntry,'zxAnVlanIfConfVlanCmd':zxAnVlanIfConfVlanCmd,'zxAnVlanIfConfVlanList':zxAnVlanIfConfVlanList,'zxAnVlanIfTransTable':zxAnVlanIfTransTable,'zxAnVlanIfTransEntry':zxAnVlanIfTransEntry,_P:zxAnVlanTranslatePortId,_Q:zxAnVlanIfTransUserVid,'zxAnVlanIfTransCVid':zxAnVlanIfTransCVid,'zxAnVlanIfTransSVid':zxAnVlanIfTransSVid,'zxAnVlanIfTransRowStatus':zxAnVlanIfTransRowStatus,'zxAnVlanIfTransVlanMerge':zxAnVlanIfTransVlanMerge,'zxAnVlanPortListTable':zxAnVlanPortListTable,'zxAnVlanPortListEntry':zxAnVlanPortListEntry,_R:zxAnVlanIndex,_S:zxAnShelfIndex,_T:zxAnSlotIndex,'zxAnVlanPortListSlotIfType':zxAnVlanPortListSlotIfType,'zxAnVlanPortUntaggedPortList':zxAnVlanPortUntaggedPortList,'zxAnVlanPortTaggedPortList':zxAnVlanPortTaggedPortList,'zxAnVlanGlobalTransTable':zxAnVlanGlobalTransTable,'zxAnVlanGlobalTransEntry':zxAnVlanGlobalTransEntry,_U:zxAnVlanGlobalTransSessionNo,'zxAnVlanMpTranslatePortId':zxAnVlanMpTranslatePortId,'zxAnVlanGlobalTransVid':zxAnVlanGlobalTransVid,'zxAnVlanGlobalTransCVid':zxAnVlanGlobalTransCVid,'zxAnVlanGlobalTransSVid':zxAnVlanGlobalTransSVid,'zxAnVlanMpTranslateDirection':zxAnVlanMpTranslateDirection,'zxAnVlanGlobalTransRowStatus':zxAnVlanGlobalTransRowStatus,'zxAnVlanGlobalTransVlanMerge':zxAnVlanGlobalTransVlanMerge,'zxAnVlanMpExQinQTable':zxAnVlanMpExQinQTable,'zxAnVlanMpExQinQEntry':zxAnVlanMpExQinQEntry,_V:zxAnVlanExQinQSessionNo,'zxAnVlanSmartQinQIfIndex':zxAnVlanSmartQinQIfIndex,'zxAnVlanSmartQinQUserVid':zxAnVlanSmartQinQUserVid,'zxAnVlanSmartQinQSelectiveType':zxAnVlanSmartQinQSelectiveType,'zxAnVlanSmartQinQStartUserVid':zxAnVlanSmartQinQStartUserVid,'zxAnVlanSmartQinQEndUserVid':zxAnVlanSmartQinQEndUserVid,'zxAnVlanExQinQInCVlanMask':zxAnVlanExQinQInCVlanMask,'zxAnVlanSmartQinQEtherType':zxAnVlanSmartQinQEtherType,'zxAnVlanSmartQinQUserCos':zxAnVlanSmartQinQUserCos,'zxAnVlanSmartQinQSVid':zxAnVlanSmartQinQSVid,'zxAnVlanSmartQinQStagCos':zxAnVlanSmartQinQStagCos,'zxAnVlanExQinQRefOnuGroupId':zxAnVlanExQinQRefOnuGroupId,'zxAnVlanSmartQinQRowStatus':zxAnVlanSmartQinQRowStatus,'zxAnVlanVoipConfTable':zxAnVlanVoipConfTable,'zxAnVlanVoipConfEntry':zxAnVlanVoipConfEntry,_W:zxAnVlanVoipVlanId,'zxAnVoipVlanUsages':zxAnVoipVlanUsages,'zxAnVlanVoipRowStatus':zxAnVlanVoipRowStatus,'zxAnVlanSmartQinQEnable':zxAnVlanSmartQinQEnable,'zxAnReservedVlan':zxAnReservedVlan,'zxAnVlanMpExQinQPortTable':zxAnVlanMpExQinQPortTable,'zxAnVlanMpExQinQPortEntry':zxAnVlanMpExQinQPortEntry,_X:zxAnVlanExQinQPortIndex,'zxAnVlanSmartQinQIfEnable':zxAnVlanSmartQinQIfEnable,'zxAnVlanExQinQOnuMapGroupId':zxAnVlanExQinQOnuMapGroupId,'zxAnVlanExQinQPortResVlan':zxAnVlanExQinQPortResVlan,'zxAnVlanMpExTranslatePortTable':zxAnVlanMpExTranslatePortTable,'zxAnVlanMpExTranslatePortEntry':zxAnVlanMpExTranslatePortEntry,_Y:zxAnVlanExTranslatePortIndex,'zxAnVlanExTranslatePortEnabled':zxAnVlanExTranslatePortEnabled,'zxAnVlanTranslateMode':zxAnVlanTranslateMode,'zxAnProtocolVlanMapTable':zxAnProtocolVlanMapTable,'zxAnProtocolVlanMapEntry':zxAnProtocolVlanMapEntry,_Z:zxAnProtocolVlanPortIndex,_a:zxAnEtherProtocolType,'zxAnVlanIfProtoMapVid':zxAnVlanIfProtoMapVid,'zxAnVlanIfProtoMapCos':zxAnVlanIfProtoMapCos,'zxAnVlanIfProtoMapCVid':zxAnVlanIfProtoMapCVid,'zxAnVlanIfProtoMapCtagCos':zxAnVlanIfProtoMapCtagCos,'zxAnVlanIfProtoMapRowStatus':zxAnVlanIfProtoMapRowStatus,'zxAnBatchVLANObjects':zxAnBatchVLANObjects,'zxAnVlanBatchConfVlanList':zxAnVlanBatchConfVlanList,'zxAnVlanBatchConfPrefixName':zxAnVlanBatchConfPrefixName,'zxAnBatchVlanTransparent':zxAnBatchVlanTransparent,'zxAnVlanBatchConfType':zxAnVlanBatchConfType,'zxAnVlanBatchConfStatus':zxAnVlanBatchConfStatus,'zxAnVlanBatchConfFailedVlanList':zxAnVlanBatchConfFailedVlanList,'zxAnVlanBatchConfCurrVlanList':zxAnVlanBatchConfCurrVlanList,'zxAnXconnectTable':zxAnXconnectTable,'zxAnXconnectEntry':zxAnXconnectEntry,_b:zxAnXconnectPortIndex,_c:zxAnXconnectLocationIndex,'zxAnXconnectMode':zxAnXconnectMode,'zxAnVlanBasedFwdSVid':zxAnVlanBasedFwdSVid,'zxAnVlanBasedFwdCVid':zxAnVlanBasedFwdCVid,'zxAnXconnectNewCvlanId':zxAnXconnectNewCvlanId,'zxAnXconnectNewSvlanId':zxAnXconnectNewSvlanId,'zxAnVlanBasedFwdUplinkPort':zxAnVlanBasedFwdUplinkPort,'zxAnVlanBasedFwdRowStatus':zxAnVlanBasedFwdRowStatus,'zxAnVlanExQinQSupportEIGMP':zxAnVlanExQinQSupportEIGMP,'zxAnVlanGlobalCtagTpid':zxAnVlanGlobalCtagTpid,'zxAnVlanGlobalTpid':zxAnVlanGlobalTpid,'zxAnOnuMngVlanTable':zxAnOnuMngVlanTable,'zxAnOnuMngVlanEntry':zxAnOnuMngVlanEntry,_e:zxAnOnuMngVlan,'zxAnOnuMngVlanRowStatus':zxAnOnuMngVlanRowStatus,'zxAnIpRouteVlanTable':zxAnIpRouteVlanTable,'zxAnIpRouteVlanEntry':zxAnIpRouteVlanEntry,_f:zxAnIpRouteVlan,'zxAnIpRouteVlanRowStatus':zxAnIpRouteVlanRowStatus,'zxAnVlanInterfaceTable':zxAnVlanInterfaceTable,'zxAnVlanInterfaceEntry':zxAnVlanInterfaceEntry,_g:zxAnVlanInterfaceVlanId,'zxAnVlanBroadcastRateLimit':zxAnVlanBroadcastRateLimit,'zxAnPortMvlanTranslateTable':zxAnPortMvlanTranslateTable,'zxAnPortMvlanTranslateEntry':zxAnPortMvlanTranslateEntry,_h:zxAnPortMvlanTranslateIfIndex,_i:zxAnPortMvlanTranslateMvlan,_j:zxAnPortMvlanTranslateCvlan,'zxAnMVlanIfTransRowStatus':zxAnMVlanIfTransRowStatus,'zxAnVlanIfProtoMapEnableTable':zxAnVlanIfProtoMapEnableTable,'zxAnVlanIfProtoMapEnableEntry':zxAnVlanIfProtoMapEnableEntry,_k:zxAnProtocolVlanPortIfIndex,'zxAnVlanIfProtoMapEnable':zxAnVlanIfProtoMapEnable,'zxAnInternalVlanTable':zxAnInternalVlanTable,'zxAnInternalVlanEntry':zxAnInternalVlanEntry,_l:zxAnInternalVlanServiceType,'zxAnInternalVlanList':zxAnInternalVlanList,'zxAnInternalVlanRowStatus':zxAnInternalVlanRowStatus,'zxAnVlanExQinQOnuGroupTable':zxAnVlanExQinQOnuGroupTable,'zxAnVlanExQinQOnuGroupEntry':zxAnVlanExQinQOnuGroupEntry,_m:zxAnVlanExQinQPonPortIndex,_n:zxAnVlanExQinQOnuGroupId,'zxAnVlanExQinQOnuGroupName':zxAnVlanExQinQOnuGroupName,'zxAnVlanExQinQOnuGroupResVlan':zxAnVlanExQinQOnuGroupResVlan,'zxAnVlanExQinQOnuGroupMembers':zxAnVlanExQinQOnuGroupMembers,'zxAnVlanTpidObjects':zxAnVlanTpidObjects,'zxAnVlanTpidTable':zxAnVlanTpidTable,'zxAnVlanTpidEntry':zxAnVlanTpidEntry,_o:zxAnVlanTpidSVlanId,_p:zxAnVlanTpidCVlanId,'zxAnVlanTpid':zxAnVlanTpid,'zxAnVlanTpidRowStatus':zxAnVlanTpidRowStatus,'zxAnIeee1588VlanTable':zxAnIeee1588VlanTable,'zxAnIeee1588VlanEntry':zxAnIeee1588VlanEntry,_q:zxAnIeee1588Vlan,'zxAnIeee1588VlanRowStatus':zxAnIeee1588VlanRowStatus,'zxAnMVlanGlobalTransTable':zxAnMVlanGlobalTransTable,'zxAnMVlanGlobalTransEntry':zxAnMVlanGlobalTransEntry,_r:zxAnMVlanGlobalTransMVid,'zxAnMVlanGlobalTransCVid':zxAnMVlanGlobalTransCVid,'zxAnMVlanGlobalTransRowStatus':zxAnMVlanGlobalTransRowStatus,'zxAnVlanStormCtrlTable':zxAnVlanStormCtrlTable,'zxAnVlanStormCtrlEntry':zxAnVlanStormCtrlEntry,'zxAnVlanMulticastFloodCtrl':zxAnVlanMulticastFloodCtrl,'zxAnVlanTagPortListTable':zxAnVlanTagPortListTable,'zxAnVlanTagPortListEntry':zxAnVlanTagPortListEntry,_s:zxAnVlanStag,_t:zxAnVlanCtag,_u:zxAnVlanTagShelf,_v:zxAnVlanTagSlot,'zxAnVlanTagPortList':zxAnVlanTagPortList,'zxAnVlanConfTpidTable':zxAnVlanConfTpidTable,'zxAnVlanConfTpidEntry':zxAnVlanConfTpidEntry,'zxAnVlanTpidConfTpid':zxAnVlanTpidConfTpid,'zxAnVlanTpidConfRowStatus':zxAnVlanTpidConfRowStatus,'zxAnVlanRuledTransGroup':zxAnVlanRuledTransGroup,'zxAnVlanRuledTransTable':zxAnVlanRuledTransTable,'zxAnVlanRuledTransEntry':zxAnVlanRuledTransEntry,_w:zxAnVlanRuledTransSVid,_x:zxAnVlanRuledTransCVid,'zxAnVlanRuledTransUserVid':zxAnVlanRuledTransUserVid,'zxAnVlanRuledTransRowStatus':zxAnVlanRuledTransRowStatus,'zxAnVlanIfCosMapObjects':zxAnVlanIfCosMapObjects,'zxAnVlanIfCosMapEnableTable':zxAnVlanIfCosMapEnableTable,'zxAnVlanIfCosMapEnableEntry':zxAnVlanIfCosMapEnableEntry,'zxAnVlanIfCosMapEnable':zxAnVlanIfCosMapEnable,'zxAnVlanIfCosMapTable':zxAnVlanIfCosMapTable,'zxAnVlanIfCosMapEntry':zxAnVlanIfCosMapEntry,_y:zxAnVlanIfCosMapCos,'zxAnVlanIfCosMapSVid':zxAnVlanIfCosMapSVid,'zxAnVlanIfCosMapCVid':zxAnVlanIfCosMapCVid,'zxAnVlanIfCosMapRowStatus':zxAnVlanIfCosMapRowStatus,'zxAnVlanBasedForwardObjects':zxAnVlanBasedForwardObjects,'zxAnVlanBasedForwardTable':zxAnVlanBasedForwardTable,'zxAnVlanBasedForwardEntry':zxAnVlanBasedForwardEntry,_z:zxAnVlanBasedForwardSVid,_A0:zxAnVlanBasedForwardCVid,'zxAnVlanBasedForwardIfIndex':zxAnVlanBasedForwardIfIndex,'zxAnVlanBasedForwardUplinkPort':zxAnVlanBasedForwardUplinkPort,'zxAnVlanBasedForwardRowStatus':zxAnVlanBasedForwardRowStatus,'zxAnVlanGlobalObjects':zxAnVlanGlobalObjects,'zxAnVlanCapabilities':zxAnVlanCapabilities,'zxAnVlanMibEnd':zxAnVlanMibEnd})