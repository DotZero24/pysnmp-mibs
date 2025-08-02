_U='tpl2BridgeManageDynPort'
_T='tpl2BridgeManagePortIndex'
_S='VlanSecEntryStatus'
_R='tpFdbVlanSecurityVid'
_Q='tpl2BridgeManageFilterMac'
_P='tpl2BridgeManageDynVlanId'
_O='tpl2BridgeManageDynMac'
_N='tpl2BridgeManageStaticVlanId'
_M='tpl2BridgeManageStaticMac'
_L='destroy'
_K='DisplayString'
_J='tpl2BridgeManageFilterVlanId'
_I='tpl2BridgeManageStaticPort'
_H='enable'
_G='read-create'
_F='disable'
_E='read-write'
_D='read-only'
_C='TPLINK-L2BRIDGE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkl2BridgeMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,10))
if mibBuilder.loadTexts:tplinkl2BridgeMIB.setRevisions(('2012-12-13 00:00',))
class VlanSecEntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),('drop',1),('forward',2),('createRequest',3),(_L,4)))
_Tplinkl2BridgeMIBObjects_ObjectIdentity=ObjectIdentity
tplinkl2BridgeMIBObjects=_Tplinkl2BridgeMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1))
_Tpl2BridgeManageStaticAddrCtrl_ObjectIdentity=ObjectIdentity
tpl2BridgeManageStaticAddrCtrl=_Tpl2BridgeManageStaticAddrCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1,1))
_Tpl2BridgeManageStaticAddrCtrlTable_Object=MibTable
tpl2BridgeManageStaticAddrCtrlTable=_Tpl2BridgeManageStaticAddrCtrlTable_Object((1,3,6,1,4,1,11863,6,10,1,1,1))
if mibBuilder.loadTexts:tpl2BridgeManageStaticAddrCtrlTable.setStatus(_A)
_Tpl2BridgeManageStaticAddrCtrlEntry_Object=MibTableRow
tpl2BridgeManageStaticAddrCtrlEntry=_Tpl2BridgeManageStaticAddrCtrlEntry_Object((1,3,6,1,4,1,11863,6,10,1,1,1,1))
tpl2BridgeManageStaticAddrCtrlEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:tpl2BridgeManageStaticAddrCtrlEntry.setStatus(_A)
_Tpl2BridgeManageStaticMac_Type=OctetString
_Tpl2BridgeManageStaticMac_Object=MibTableColumn
tpl2BridgeManageStaticMac=_Tpl2BridgeManageStaticMac_Object((1,3,6,1,4,1,11863,6,10,1,1,1,1,1),_Tpl2BridgeManageStaticMac_Type())
tpl2BridgeManageStaticMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageStaticMac.setStatus(_A)
class _Tpl2BridgeManageStaticVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Tpl2BridgeManageStaticVlanId_Type.__name__=_B
_Tpl2BridgeManageStaticVlanId_Object=MibTableColumn
tpl2BridgeManageStaticVlanId=_Tpl2BridgeManageStaticVlanId_Object((1,3,6,1,4,1,11863,6,10,1,1,1,1,2),_Tpl2BridgeManageStaticVlanId_Type())
tpl2BridgeManageStaticVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageStaticVlanId.setStatus(_A)
_Tpl2BridgeManageStaticPort_Type=OctetString
_Tpl2BridgeManageStaticPort_Object=MibTableColumn
tpl2BridgeManageStaticPort=_Tpl2BridgeManageStaticPort_Object((1,3,6,1,4,1,11863,6,10,1,1,1,1,3),_Tpl2BridgeManageStaticPort_Type())
tpl2BridgeManageStaticPort.setMaxAccess(_G)
if mibBuilder.loadTexts:tpl2BridgeManageStaticPort.setStatus(_A)
_Tpl2BridgeManageStaticStatus_Type=TPRowStatus
_Tpl2BridgeManageStaticStatus_Object=MibTableColumn
tpl2BridgeManageStaticStatus=_Tpl2BridgeManageStaticStatus_Object((1,3,6,1,4,1,11863,6,10,1,1,1,1,4),_Tpl2BridgeManageStaticStatus_Type())
tpl2BridgeManageStaticStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tpl2BridgeManageStaticStatus.setStatus(_A)
_Tpl2BridgeManageDynAddrCtrl_ObjectIdentity=ObjectIdentity
tpl2BridgeManageDynAddrCtrl=_Tpl2BridgeManageDynAddrCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1,2))
class _Tpl2BridgeManageDynAddrCtrlAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,630))
_Tpl2BridgeManageDynAddrCtrlAgingTime_Type.__name__=_B
_Tpl2BridgeManageDynAddrCtrlAgingTime_Object=MibScalar
tpl2BridgeManageDynAddrCtrlAgingTime=_Tpl2BridgeManageDynAddrCtrlAgingTime_Object((1,3,6,1,4,1,11863,6,10,1,2,1),_Tpl2BridgeManageDynAddrCtrlAgingTime_Type())
tpl2BridgeManageDynAddrCtrlAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageDynAddrCtrlAgingTime.setStatus(_A)
_Tpl2BridgeManageDynAddrCtrlTable_Object=MibTable
tpl2BridgeManageDynAddrCtrlTable=_Tpl2BridgeManageDynAddrCtrlTable_Object((1,3,6,1,4,1,11863,6,10,1,2,2))
if mibBuilder.loadTexts:tpl2BridgeManageDynAddrCtrlTable.setStatus(_A)
_Tpl2BridgeManageDynAddrCtrlEntry_Object=MibTableRow
tpl2BridgeManageDynAddrCtrlEntry=_Tpl2BridgeManageDynAddrCtrlEntry_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1))
tpl2BridgeManageDynAddrCtrlEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:tpl2BridgeManageDynAddrCtrlEntry.setStatus(_A)
_Tpl2BridgeManageDynMac_Type=OctetString
_Tpl2BridgeManageDynMac_Object=MibTableColumn
tpl2BridgeManageDynMac=_Tpl2BridgeManageDynMac_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1,1),_Tpl2BridgeManageDynMac_Type())
tpl2BridgeManageDynMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageDynMac.setStatus(_A)
class _Tpl2BridgeManageDynVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Tpl2BridgeManageDynVlanId_Type.__name__=_B
_Tpl2BridgeManageDynVlanId_Object=MibTableColumn
tpl2BridgeManageDynVlanId=_Tpl2BridgeManageDynVlanId_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1,2),_Tpl2BridgeManageDynVlanId_Type())
tpl2BridgeManageDynVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageDynVlanId.setStatus(_A)
_Tpl2BridgeManageDynPort_Type=OctetString
_Tpl2BridgeManageDynPort_Object=MibTableColumn
tpl2BridgeManageDynPort=_Tpl2BridgeManageDynPort_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1,3),_Tpl2BridgeManageDynPort_Type())
tpl2BridgeManageDynPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageDynPort.setStatus(_A)
class _Tpl2BridgeManageDynAgeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAging',0),('aging',1)))
_Tpl2BridgeManageDynAgeStatus_Type.__name__=_B
_Tpl2BridgeManageDynAgeStatus_Object=MibTableColumn
tpl2BridgeManageDynAgeStatus=_Tpl2BridgeManageDynAgeStatus_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1,4),_Tpl2BridgeManageDynAgeStatus_Type())
tpl2BridgeManageDynAgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageDynAgeStatus.setStatus(_A)
class _Tpl2BridgeManageDynStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*(('active',1),('bind',4),(_L,6)))
_Tpl2BridgeManageDynStatus_Type.__name__=_B
_Tpl2BridgeManageDynStatus_Object=MibTableColumn
tpl2BridgeManageDynStatus=_Tpl2BridgeManageDynStatus_Object((1,3,6,1,4,1,11863,6,10,1,2,2,1,5),_Tpl2BridgeManageDynStatus_Type())
tpl2BridgeManageDynStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageDynStatus.setStatus(_A)
_Tpl2BridgeManageFilterAddrCtrl_ObjectIdentity=ObjectIdentity
tpl2BridgeManageFilterAddrCtrl=_Tpl2BridgeManageFilterAddrCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1,3))
_Tpl2BridgeManageFilterCtrlTable_Object=MibTable
tpl2BridgeManageFilterCtrlTable=_Tpl2BridgeManageFilterCtrlTable_Object((1,3,6,1,4,1,11863,6,10,1,3,1))
if mibBuilder.loadTexts:tpl2BridgeManageFilterCtrlTable.setStatus(_A)
_Tpl2BridgeManageFilterCtrlEntry_Object=MibTableRow
tpl2BridgeManageFilterCtrlEntry=_Tpl2BridgeManageFilterCtrlEntry_Object((1,3,6,1,4,1,11863,6,10,1,3,1,1))
tpl2BridgeManageFilterCtrlEntry.setIndexNames((0,_C,_Q),(0,_C,_J))
if mibBuilder.loadTexts:tpl2BridgeManageFilterCtrlEntry.setStatus(_A)
_Tpl2BridgeManageFilterMac_Type=OctetString
_Tpl2BridgeManageFilterMac_Object=MibTableColumn
tpl2BridgeManageFilterMac=_Tpl2BridgeManageFilterMac_Object((1,3,6,1,4,1,11863,6,10,1,3,1,1,1),_Tpl2BridgeManageFilterMac_Type())
tpl2BridgeManageFilterMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageFilterMac.setStatus(_A)
class _Tpl2BridgeManageFilterVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Tpl2BridgeManageFilterVlanId_Type.__name__=_B
_Tpl2BridgeManageFilterVlanId_Object=MibTableColumn
tpl2BridgeManageFilterVlanId=_Tpl2BridgeManageFilterVlanId_Object((1,3,6,1,4,1,11863,6,10,1,3,1,1,2),_Tpl2BridgeManageFilterVlanId_Type())
tpl2BridgeManageFilterVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManageFilterVlanId.setStatus(_A)
_Tpl2BridgeManageFilterStatus_Type=TPRowStatus
_Tpl2BridgeManageFilterStatus_Object=MibTableColumn
tpl2BridgeManageFilterStatus=_Tpl2BridgeManageFilterStatus_Object((1,3,6,1,4,1,11863,6,10,1,3,1,1,3),_Tpl2BridgeManageFilterStatus_Type())
tpl2BridgeManageFilterStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tpl2BridgeManageFilterStatus.setStatus(_A)
_Tpl2BridgeManageVlanSecurityCtrl_ObjectIdentity=ObjectIdentity
tpl2BridgeManageVlanSecurityCtrl=_Tpl2BridgeManageVlanSecurityCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1,4))
_Tpl2BridgeManagevlanSecurityTable_Object=MibTable
tpl2BridgeManagevlanSecurityTable=_Tpl2BridgeManagevlanSecurityTable_Object((1,3,6,1,4,1,11863,6,10,1,4,1))
if mibBuilder.loadTexts:tpl2BridgeManagevlanSecurityTable.setStatus(_A)
_Tpl2BridgeManagevlanSecEntry_Object=MibTableRow
tpl2BridgeManagevlanSecEntry=_Tpl2BridgeManagevlanSecEntry_Object((1,3,6,1,4,1,11863,6,10,1,4,1,1))
tpl2BridgeManagevlanSecEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:tpl2BridgeManagevlanSecEntry.setStatus(_A)
class _TpFdbVlanSecurityVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TpFdbVlanSecurityVid_Type.__name__=_B
_TpFdbVlanSecurityVid_Object=MibTableColumn
tpFdbVlanSecurityVid=_TpFdbVlanSecurityVid_Object((1,3,6,1,4,1,11863,6,10,1,4,1,1,1),_TpFdbVlanSecurityVid_Type())
tpFdbVlanSecurityVid.setMaxAccess(_D)
if mibBuilder.loadTexts:tpFdbVlanSecurityVid.setStatus(_A)
class _TpFdbVlanSecurityMaxLearned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_TpFdbVlanSecurityMaxLearned_Type.__name__=_B
_TpFdbVlanSecurityMaxLearned_Object=MibTableColumn
tpFdbVlanSecurityMaxLearned=_TpFdbVlanSecurityMaxLearned_Object((1,3,6,1,4,1,11863,6,10,1,4,1,1,2),_TpFdbVlanSecurityMaxLearned_Type())
tpFdbVlanSecurityMaxLearned.setMaxAccess(_G)
if mibBuilder.loadTexts:tpFdbVlanSecurityMaxLearned.setStatus(_A)
class _TpFdbVlanSecurityRowStatus_Type(VlanSecEntryStatus):defaultValue=2
_TpFdbVlanSecurityRowStatus_Type.__name__=_S
_TpFdbVlanSecurityRowStatus_Object=MibTableColumn
tpFdbVlanSecurityRowStatus=_TpFdbVlanSecurityRowStatus_Object((1,3,6,1,4,1,11863,6,10,1,4,1,1,3),_TpFdbVlanSecurityRowStatus_Type())
tpFdbVlanSecurityRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tpFdbVlanSecurityRowStatus.setStatus(_A)
_Tpl2BridgeManageNotificationCtrl_ObjectIdentity=ObjectIdentity
tpl2BridgeManageNotificationCtrl=_Tpl2BridgeManageNotificationCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,10,1,5))
class _Tpl2BridgeManageNotificationGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_Tpl2BridgeManageNotificationGlobalStatus_Type.__name__=_B
_Tpl2BridgeManageNotificationGlobalStatus_Object=MibScalar
tpl2BridgeManageNotificationGlobalStatus=_Tpl2BridgeManageNotificationGlobalStatus_Object((1,3,6,1,4,1,11863,6,10,1,5,1),_Tpl2BridgeManageNotificationGlobalStatus_Type())
tpl2BridgeManageNotificationGlobalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageNotificationGlobalStatus.setStatus(_A)
class _Tpl2BridgeManageNotificationTableFullStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_Tpl2BridgeManageNotificationTableFullStatus_Type.__name__=_B
_Tpl2BridgeManageNotificationTableFullStatus_Object=MibScalar
tpl2BridgeManageNotificationTableFullStatus=_Tpl2BridgeManageNotificationTableFullStatus_Object((1,3,6,1,4,1,11863,6,10,1,5,2),_Tpl2BridgeManageNotificationTableFullStatus_Type())
tpl2BridgeManageNotificationTableFullStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageNotificationTableFullStatus.setStatus(_A)
class _Tpl2BridgeManageNotificationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Tpl2BridgeManageNotificationInterval_Type.__name__=_B
_Tpl2BridgeManageNotificationInterval_Object=MibScalar
tpl2BridgeManageNotificationInterval=_Tpl2BridgeManageNotificationInterval_Object((1,3,6,1,4,1,11863,6,10,1,5,3),_Tpl2BridgeManageNotificationInterval_Type())
tpl2BridgeManageNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageNotificationInterval.setStatus(_A)
_Tpl2BridgeManageNotificationTable_Object=MibTable
tpl2BridgeManageNotificationTable=_Tpl2BridgeManageNotificationTable_Object((1,3,6,1,4,1,11863,6,10,1,5,4))
if mibBuilder.loadTexts:tpl2BridgeManageNotificationTable.setStatus(_A)
_Tpl2BridgeManageNotificationCtrlEntry_Object=MibTableRow
tpl2BridgeManageNotificationCtrlEntry=_Tpl2BridgeManageNotificationCtrlEntry_Object((1,3,6,1,4,1,11863,6,10,1,5,4,1))
tpl2BridgeManageNotificationCtrlEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:tpl2BridgeManageNotificationCtrlEntry.setStatus(_A)
class _Tpl2BridgeManagePortIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Tpl2BridgeManagePortIndex_Type.__name__=_K
_Tpl2BridgeManagePortIndex_Object=MibTableColumn
tpl2BridgeManagePortIndex=_Tpl2BridgeManagePortIndex_Object((1,3,6,1,4,1,11863,6,10,1,5,4,1,1),_Tpl2BridgeManagePortIndex_Type())
tpl2BridgeManagePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpl2BridgeManagePortIndex.setStatus(_A)
class _Tpl2BridgeManageLrnModeChg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_Tpl2BridgeManageLrnModeChg_Type.__name__=_B
_Tpl2BridgeManageLrnModeChg_Object=MibTableColumn
tpl2BridgeManageLrnModeChg=_Tpl2BridgeManageLrnModeChg_Object((1,3,6,1,4,1,11863,6,10,1,5,4,1,2),_Tpl2BridgeManageLrnModeChg_Type())
tpl2BridgeManageLrnModeChg.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageLrnModeChg.setStatus(_A)
class _Tpl2BridgeManageExceedMaxLrn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_Tpl2BridgeManageExceedMaxLrn_Type.__name__=_B
_Tpl2BridgeManageExceedMaxLrn_Object=MibTableColumn
tpl2BridgeManageExceedMaxLrn=_Tpl2BridgeManageExceedMaxLrn_Object((1,3,6,1,4,1,11863,6,10,1,5,4,1,3),_Tpl2BridgeManageExceedMaxLrn_Type())
tpl2BridgeManageExceedMaxLrn.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageExceedMaxLrn.setStatus(_A)
class _Tpl2BridgeManageNewMacLrn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_H,1)))
_Tpl2BridgeManageNewMacLrn_Type.__name__=_B
_Tpl2BridgeManageNewMacLrn_Object=MibTableColumn
tpl2BridgeManageNewMacLrn=_Tpl2BridgeManageNewMacLrn_Object((1,3,6,1,4,1,11863,6,10,1,5,4,1,4),_Tpl2BridgeManageNewMacLrn_Type())
tpl2BridgeManageNewMacLrn.setMaxAccess(_E)
if mibBuilder.loadTexts:tpl2BridgeManageNewMacLrn.setStatus(_A)
_Tplinkl2BridgeNotifications_ObjectIdentity=ObjectIdentity
tplinkl2BridgeNotifications=_Tplinkl2BridgeNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,10,2))
fdbDynMacNew=NotificationType((1,3,6,1,4,1,11863,6,10,2,1))
fdbDynMacNew.setObjects((_C,_U))
if mibBuilder.loadTexts:fdbDynMacNew.setStatus(_A)
fdbStaticMacNew=NotificationType((1,3,6,1,4,1,11863,6,10,2,2))
fdbStaticMacNew.setObjects((_C,_I))
if mibBuilder.loadTexts:fdbStaticMacNew.setStatus(_A)
fdbFilterMacNew=NotificationType((1,3,6,1,4,1,11863,6,10,2,3))
fdbFilterMacNew.setObjects((_C,_J))
if mibBuilder.loadTexts:fdbFilterMacNew.setStatus(_A)
fdbMacTableFull=NotificationType((1,3,6,1,4,1,11863,6,10,2,4))
fdbMacTableFull.setObjects((_C,_I))
if mibBuilder.loadTexts:fdbMacTableFull.setStatus(_A)
fdbMacMaxLearnedNumExceed=NotificationType((1,3,6,1,4,1,11863,6,10,2,5))
fdbMacMaxLearnedNumExceed.setObjects((_C,_I))
if mibBuilder.loadTexts:fdbMacMaxLearnedNumExceed.setStatus(_A)
fdbMacLearnModeChange=NotificationType((1,3,6,1,4,1,11863,6,10,2,6))
fdbMacLearnModeChange.setObjects((_C,_I))
if mibBuilder.loadTexts:fdbMacLearnModeChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_S:VlanSecEntryStatus,'tplinkl2BridgeMIB':tplinkl2BridgeMIB,'tplinkl2BridgeMIBObjects':tplinkl2BridgeMIBObjects,'tpl2BridgeManageStaticAddrCtrl':tpl2BridgeManageStaticAddrCtrl,'tpl2BridgeManageStaticAddrCtrlTable':tpl2BridgeManageStaticAddrCtrlTable,'tpl2BridgeManageStaticAddrCtrlEntry':tpl2BridgeManageStaticAddrCtrlEntry,_M:tpl2BridgeManageStaticMac,_N:tpl2BridgeManageStaticVlanId,_I:tpl2BridgeManageStaticPort,'tpl2BridgeManageStaticStatus':tpl2BridgeManageStaticStatus,'tpl2BridgeManageDynAddrCtrl':tpl2BridgeManageDynAddrCtrl,'tpl2BridgeManageDynAddrCtrlAgingTime':tpl2BridgeManageDynAddrCtrlAgingTime,'tpl2BridgeManageDynAddrCtrlTable':tpl2BridgeManageDynAddrCtrlTable,'tpl2BridgeManageDynAddrCtrlEntry':tpl2BridgeManageDynAddrCtrlEntry,_O:tpl2BridgeManageDynMac,_P:tpl2BridgeManageDynVlanId,_U:tpl2BridgeManageDynPort,'tpl2BridgeManageDynAgeStatus':tpl2BridgeManageDynAgeStatus,'tpl2BridgeManageDynStatus':tpl2BridgeManageDynStatus,'tpl2BridgeManageFilterAddrCtrl':tpl2BridgeManageFilterAddrCtrl,'tpl2BridgeManageFilterCtrlTable':tpl2BridgeManageFilterCtrlTable,'tpl2BridgeManageFilterCtrlEntry':tpl2BridgeManageFilterCtrlEntry,_Q:tpl2BridgeManageFilterMac,_J:tpl2BridgeManageFilterVlanId,'tpl2BridgeManageFilterStatus':tpl2BridgeManageFilterStatus,'tpl2BridgeManageVlanSecurityCtrl':tpl2BridgeManageVlanSecurityCtrl,'tpl2BridgeManagevlanSecurityTable':tpl2BridgeManagevlanSecurityTable,'tpl2BridgeManagevlanSecEntry':tpl2BridgeManagevlanSecEntry,_R:tpFdbVlanSecurityVid,'tpFdbVlanSecurityMaxLearned':tpFdbVlanSecurityMaxLearned,'tpFdbVlanSecurityRowStatus':tpFdbVlanSecurityRowStatus,'tpl2BridgeManageNotificationCtrl':tpl2BridgeManageNotificationCtrl,'tpl2BridgeManageNotificationGlobalStatus':tpl2BridgeManageNotificationGlobalStatus,'tpl2BridgeManageNotificationTableFullStatus':tpl2BridgeManageNotificationTableFullStatus,'tpl2BridgeManageNotificationInterval':tpl2BridgeManageNotificationInterval,'tpl2BridgeManageNotificationTable':tpl2BridgeManageNotificationTable,'tpl2BridgeManageNotificationCtrlEntry':tpl2BridgeManageNotificationCtrlEntry,_T:tpl2BridgeManagePortIndex,'tpl2BridgeManageLrnModeChg':tpl2BridgeManageLrnModeChg,'tpl2BridgeManageExceedMaxLrn':tpl2BridgeManageExceedMaxLrn,'tpl2BridgeManageNewMacLrn':tpl2BridgeManageNewMacLrn,'tplinkl2BridgeNotifications':tplinkl2BridgeNotifications,'fdbDynMacNew':fdbDynMacNew,'fdbStaticMacNew':fdbStaticMacNew,'fdbFilterMacNew':fdbFilterMacNew,'fdbMacTableFull':fdbMacTableFull,'fdbMacMaxLearnedNumExceed':fdbMacMaxLearnedNumExceed,'fdbMacLearnModeChange':fdbMacLearnModeChange})