_V='nsrpLinkInfoIndex'
_U='nsrpClusterTblIndex'
_T='nsrpTrackIpIndex'
_S='nsrpRtoCounterIdx'
_R='nsrpRtoUnitId'
_Q='nsrpRtoUnitGroupId'
_P='nsrpRtoGroupId'
_O='active'
_N='nsrpVsdIfIndex'
_M='undefined'
_L='nsrpVsdMemberUnitId'
_K='nsrpVsdMemberGroupId'
_J='nsrpVsdGroupID'
_I='enabled'
_H='disabled'
_G='DisplayString'
_F='enable'
_E='disable'
_D='NETSCREEN-NSRP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenNsrp,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenNsrp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
netscreenNsrpMibModule=ModuleIdentity((1,3,6,1,4,1,3224,6,0))
if mibBuilder.loadTexts:netscreenNsrpMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-14 00:00','2003-06-04 00:00','2001-01-08 00:00'))
_NetscreenNsrpGeneral_ObjectIdentity=ObjectIdentity
netscreenNsrpGeneral=_NetscreenNsrpGeneral_ObjectIdentity((1,3,6,1,4,1,3224,6,1))
_NsrpGeneralClusterId_Type=Integer32
_NsrpGeneralClusterId_Object=MibScalar
nsrpGeneralClusterId=_NsrpGeneralClusterId_Object((1,3,6,1,4,1,3224,6,1,1),_NsrpGeneralClusterId_Type())
nsrpGeneralClusterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralClusterId.setStatus(_A)
_NsrpGeneralLocalUnitId_Type=Integer32
_NsrpGeneralLocalUnitId_Object=MibScalar
nsrpGeneralLocalUnitId=_NsrpGeneralLocalUnitId_Object((1,3,6,1,4,1,3224,6,1,2),_NsrpGeneralLocalUnitId_Type())
nsrpGeneralLocalUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralLocalUnitId.setStatus(_A)
class _NsrpGeneralEncrypEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsrpGeneralEncrypEnable_Type.__name__=_C
_NsrpGeneralEncrypEnable_Object=MibScalar
nsrpGeneralEncrypEnable=_NsrpGeneralEncrypEnable_Object((1,3,6,1,4,1,3224,6,1,3),_NsrpGeneralEncrypEnable_Type())
nsrpGeneralEncrypEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralEncrypEnable.setStatus(_A)
class _NsrpGeneralAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsrpGeneralAuthEnable_Type.__name__=_C
_NsrpGeneralAuthEnable_Object=MibScalar
nsrpGeneralAuthEnable=_NsrpGeneralAuthEnable_Object((1,3,6,1,4,1,3224,6,1,4),_NsrpGeneralAuthEnable_Type())
nsrpGeneralAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralAuthEnable.setStatus(_A)
class _NsrpGeneralIfMonitor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsrpGeneralIfMonitor_Type.__name__=_G
_NsrpGeneralIfMonitor_Object=MibScalar
nsrpGeneralIfMonitor=_NsrpGeneralIfMonitor_Object((1,3,6,1,4,1,3224,6,1,5),_NsrpGeneralIfMonitor_Type())
nsrpGeneralIfMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralIfMonitor.setStatus(_A)
_NsrpGeneralGratArps_Type=Integer32
_NsrpGeneralGratArps_Object=MibScalar
nsrpGeneralGratArps=_NsrpGeneralGratArps_Object((1,3,6,1,4,1,3224,6,1,6),_NsrpGeneralGratArps_Type())
nsrpGeneralGratArps.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpGeneralGratArps.setStatus(_A)
_NetscreenNsrpVSD_ObjectIdentity=ObjectIdentity
netscreenNsrpVSD=_NetscreenNsrpVSD_ObjectIdentity((1,3,6,1,4,1,3224,6,2))
_NsrpVsdGroupTable_Object=MibTable
nsrpVsdGroupTable=_NsrpVsdGroupTable_Object((1,3,6,1,4,1,3224,6,2,1))
if mibBuilder.loadTexts:nsrpVsdGroupTable.setStatus(_A)
_NsrpVsdGroupEntry_Object=MibTableRow
nsrpVsdGroupEntry=_NsrpVsdGroupEntry_Object((1,3,6,1,4,1,3224,6,2,1,1))
nsrpVsdGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nsrpVsdGroupEntry.setStatus(_A)
class _NsrpVsdGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpVsdGroupID_Type.__name__=_C
_NsrpVsdGroupID_Object=MibTableColumn
nsrpVsdGroupID=_NsrpVsdGroupID_Object((1,3,6,1,4,1,3224,6,2,1,1,1),_NsrpVsdGroupID_Type())
nsrpVsdGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupID.setStatus(_A)
_NsrpVsdGroupPriority_Type=Integer32
_NsrpVsdGroupPriority_Object=MibTableColumn
nsrpVsdGroupPriority=_NsrpVsdGroupPriority_Object((1,3,6,1,4,1,3224,6,2,1,1,2),_NsrpVsdGroupPriority_Type())
nsrpVsdGroupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupPriority.setStatus(_A)
_NsrpVsdGroupPreempt_Type=Integer32
_NsrpVsdGroupPreempt_Object=MibTableColumn
nsrpVsdGroupPreempt=_NsrpVsdGroupPreempt_Object((1,3,6,1,4,1,3224,6,2,1,1,3),_NsrpVsdGroupPreempt_Type())
nsrpVsdGroupPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupPreempt.setStatus(_A)
_NsrpVsdGroupHoldDownTime_Type=Integer32
_NsrpVsdGroupHoldDownTime_Object=MibTableColumn
nsrpVsdGroupHoldDownTime=_NsrpVsdGroupHoldDownTime_Object((1,3,6,1,4,1,3224,6,2,1,1,4),_NsrpVsdGroupHoldDownTime_Type())
nsrpVsdGroupHoldDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupHoldDownTime.setStatus(_A)
_NsrpVsdGroupNumberOfUnit_Type=Integer32
_NsrpVsdGroupNumberOfUnit_Object=MibTableColumn
nsrpVsdGroupNumberOfUnit=_NsrpVsdGroupNumberOfUnit_Object((1,3,6,1,4,1,3224,6,2,1,1,5),_NsrpVsdGroupNumberOfUnit_Type())
nsrpVsdGroupNumberOfUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupNumberOfUnit.setStatus(_A)
_NsrpVsdGroupCntStateChange_Type=Integer32
_NsrpVsdGroupCntStateChange_Object=MibTableColumn
nsrpVsdGroupCntStateChange=_NsrpVsdGroupCntStateChange_Object((1,3,6,1,4,1,3224,6,2,1,1,6),_NsrpVsdGroupCntStateChange_Type())
nsrpVsdGroupCntStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntStateChange.setStatus(_A)
_NsrpVsdGroupCntToInit_Type=Integer32
_NsrpVsdGroupCntToInit_Object=MibTableColumn
nsrpVsdGroupCntToInit=_NsrpVsdGroupCntToInit_Object((1,3,6,1,4,1,3224,6,2,1,1,7),_NsrpVsdGroupCntToInit_Type())
nsrpVsdGroupCntToInit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToInit.setStatus(_A)
_NsrpVsdGroupCntToMaster_Type=Integer32
_NsrpVsdGroupCntToMaster_Object=MibTableColumn
nsrpVsdGroupCntToMaster=_NsrpVsdGroupCntToMaster_Object((1,3,6,1,4,1,3224,6,2,1,1,8),_NsrpVsdGroupCntToMaster_Type())
nsrpVsdGroupCntToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToMaster.setStatus(_A)
_NsrpVsdGroupCntToPBackup_Type=Integer32
_NsrpVsdGroupCntToPBackup_Object=MibTableColumn
nsrpVsdGroupCntToPBackup=_NsrpVsdGroupCntToPBackup_Object((1,3,6,1,4,1,3224,6,2,1,1,9),_NsrpVsdGroupCntToPBackup_Type())
nsrpVsdGroupCntToPBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToPBackup.setStatus(_A)
_NsrpVsdGroupCntToBackup_Type=Integer32
_NsrpVsdGroupCntToBackup_Object=MibTableColumn
nsrpVsdGroupCntToBackup=_NsrpVsdGroupCntToBackup_Object((1,3,6,1,4,1,3224,6,2,1,1,10),_NsrpVsdGroupCntToBackup_Type())
nsrpVsdGroupCntToBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToBackup.setStatus(_A)
_NsrpVsdGroupCntToIneligible_Type=Integer32
_NsrpVsdGroupCntToIneligible_Object=MibTableColumn
nsrpVsdGroupCntToIneligible=_NsrpVsdGroupCntToIneligible_Object((1,3,6,1,4,1,3224,6,2,1,1,11),_NsrpVsdGroupCntToIneligible_Type())
nsrpVsdGroupCntToIneligible.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToIneligible.setStatus(_A)
_NsrpVsdGroupCntToInoperable_Type=Integer32
_NsrpVsdGroupCntToInoperable_Object=MibTableColumn
nsrpVsdGroupCntToInoperable=_NsrpVsdGroupCntToInoperable_Object((1,3,6,1,4,1,3224,6,2,1,1,12),_NsrpVsdGroupCntToInoperable_Type())
nsrpVsdGroupCntToInoperable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntToInoperable.setStatus(_A)
_NsrpVsdGroupCntMasterConflict_Type=Integer32
_NsrpVsdGroupCntMasterConflict_Object=MibTableColumn
nsrpVsdGroupCntMasterConflict=_NsrpVsdGroupCntMasterConflict_Object((1,3,6,1,4,1,3224,6,2,1,1,13),_NsrpVsdGroupCntMasterConflict_Type())
nsrpVsdGroupCntMasterConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntMasterConflict.setStatus(_A)
_NsrpVsdGroupCntPbConfilict_Type=Integer32
_NsrpVsdGroupCntPbConfilict_Object=MibTableColumn
nsrpVsdGroupCntPbConfilict=_NsrpVsdGroupCntPbConfilict_Object((1,3,6,1,4,1,3224,6,2,1,1,14),_NsrpVsdGroupCntPbConfilict_Type())
nsrpVsdGroupCntPbConfilict.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntPbConfilict.setStatus(_A)
_NsrpVsdGroupCntHeartbeatTx_Type=Integer32
_NsrpVsdGroupCntHeartbeatTx_Object=MibTableColumn
nsrpVsdGroupCntHeartbeatTx=_NsrpVsdGroupCntHeartbeatTx_Object((1,3,6,1,4,1,3224,6,2,1,1,15),_NsrpVsdGroupCntHeartbeatTx_Type())
nsrpVsdGroupCntHeartbeatTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntHeartbeatTx.setStatus(_A)
_NsrpVsdGroupCntHeartbeatRx_Type=Integer32
_NsrpVsdGroupCntHeartbeatRx_Object=MibTableColumn
nsrpVsdGroupCntHeartbeatRx=_NsrpVsdGroupCntHeartbeatRx_Object((1,3,6,1,4,1,3224,6,2,1,1,16),_NsrpVsdGroupCntHeartbeatRx_Type())
nsrpVsdGroupCntHeartbeatRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGroupCntHeartbeatRx.setStatus(_A)
_NsrpVsdMemberTable_Object=MibTable
nsrpVsdMemberTable=_NsrpVsdMemberTable_Object((1,3,6,1,4,1,3224,6,2,2))
if mibBuilder.loadTexts:nsrpVsdMemberTable.setStatus(_A)
_NsrpVsdMemberEntry_Object=MibTableRow
nsrpVsdMemberEntry=_NsrpVsdMemberEntry_Object((1,3,6,1,4,1,3224,6,2,2,1))
nsrpVsdMemberEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:nsrpVsdMemberEntry.setStatus(_A)
class _NsrpVsdMemberGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpVsdMemberGroupId_Type.__name__=_C
_NsrpVsdMemberGroupId_Object=MibTableColumn
nsrpVsdMemberGroupId=_NsrpVsdMemberGroupId_Object((1,3,6,1,4,1,3224,6,2,2,1,1),_NsrpVsdMemberGroupId_Type())
nsrpVsdMemberGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdMemberGroupId.setStatus(_A)
class _NsrpVsdMemberUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpVsdMemberUnitId_Type.__name__=_C
_NsrpVsdMemberUnitId_Object=MibTableColumn
nsrpVsdMemberUnitId=_NsrpVsdMemberUnitId_Object((1,3,6,1,4,1,3224,6,2,2,1,2),_NsrpVsdMemberUnitId_Type())
nsrpVsdMemberUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdMemberUnitId.setStatus(_A)
class _NsrpVsdMemberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_M,0),('init',1),('master',2),('primary-backup',3),('backup',4),('ineligible',5),('inoperable',6)))
_NsrpVsdMemberStatus_Type.__name__=_C
_NsrpVsdMemberStatus_Object=MibTableColumn
nsrpVsdMemberStatus=_NsrpVsdMemberStatus_Object((1,3,6,1,4,1,3224,6,2,2,1,3),_NsrpVsdMemberStatus_Type())
nsrpVsdMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdMemberStatus.setStatus(_A)
_NsrpVsdMemberPriority_Type=Integer32
_NsrpVsdMemberPriority_Object=MibTableColumn
nsrpVsdMemberPriority=_NsrpVsdMemberPriority_Object((1,3,6,1,4,1,3224,6,2,2,1,4),_NsrpVsdMemberPriority_Type())
nsrpVsdMemberPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdMemberPriority.setStatus(_A)
_NsrpVsdMemberPreempt_Type=Integer32
_NsrpVsdMemberPreempt_Object=MibTableColumn
nsrpVsdMemberPreempt=_NsrpVsdMemberPreempt_Object((1,3,6,1,4,1,3224,6,2,2,1,5),_NsrpVsdMemberPreempt_Type())
nsrpVsdMemberPreempt.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdMemberPreempt.setStatus(_A)
_NsrpVsdInterfaceTable_Object=MibTable
nsrpVsdInterfaceTable=_NsrpVsdInterfaceTable_Object((1,3,6,1,4,1,3224,6,2,3))
if mibBuilder.loadTexts:nsrpVsdInterfaceTable.setStatus(_A)
_NsrpVsdInterfaceEntry_Object=MibTableRow
nsrpVsdInterfaceEntry=_NsrpVsdInterfaceEntry_Object((1,3,6,1,4,1,3224,6,2,3,1))
nsrpVsdInterfaceEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:nsrpVsdInterfaceEntry.setStatus(_A)
class _NsrpVsdIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpVsdIfIndex_Type.__name__=_C
_NsrpVsdIfIndex_Object=MibTableColumn
nsrpVsdIfIndex=_NsrpVsdIfIndex_Object((1,3,6,1,4,1,3224,6,2,3,1,1),_NsrpVsdIfIndex_Type())
nsrpVsdIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfIndex.setStatus(_A)
class _NsrpVsdIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),('inactive',1),(_O,2)))
_NsrpVsdIfStatus_Type.__name__=_C
_NsrpVsdIfStatus_Object=MibTableColumn
nsrpVsdIfStatus=_NsrpVsdIfStatus_Object((1,3,6,1,4,1,3224,6,2,3,1,2),_NsrpVsdIfStatus_Type())
nsrpVsdIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfStatus.setStatus(_A)
_NsrpVsdIfGroupId_Type=Integer32
_NsrpVsdIfGroupId_Object=MibTableColumn
nsrpVsdIfGroupId=_NsrpVsdIfGroupId_Object((1,3,6,1,4,1,3224,6,2,3,1,3),_NsrpVsdIfGroupId_Type())
nsrpVsdIfGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfGroupId.setStatus(_A)
_NsrpVsdIfIp_Type=IpAddress
_NsrpVsdIfIp_Object=MibTableColumn
nsrpVsdIfIp=_NsrpVsdIfIp_Object((1,3,6,1,4,1,3224,6,2,3,1,4),_NsrpVsdIfIp_Type())
nsrpVsdIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfIp.setStatus(_A)
_NsrpVsdIfNetmask_Type=IpAddress
_NsrpVsdIfNetmask_Object=MibTableColumn
nsrpVsdIfNetmask=_NsrpVsdIfNetmask_Object((1,3,6,1,4,1,3224,6,2,3,1,5),_NsrpVsdIfNetmask_Type())
nsrpVsdIfNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfNetmask.setStatus(_A)
_NsrpVsdIfGateway_Type=IpAddress
_NsrpVsdIfGateway_Object=MibTableColumn
nsrpVsdIfGateway=_NsrpVsdIfGateway_Object((1,3,6,1,4,1,3224,6,2,3,1,6),_NsrpVsdIfGateway_Type())
nsrpVsdIfGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfGateway.setStatus(_A)
class _NsrpVsdIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsrpVsdIfName_Type.__name__=_G
_NsrpVsdIfName_Object=MibTableColumn
nsrpVsdIfName=_NsrpVsdIfName_Object((1,3,6,1,4,1,3224,6,2,3,1,7),_NsrpVsdIfName_Type())
nsrpVsdIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfName.setStatus(_A)
_NsrpVsdIfVLAN_Type=Integer32
_NsrpVsdIfVLAN_Object=MibTableColumn
nsrpVsdIfVLAN=_NsrpVsdIfVLAN_Object((1,3,6,1,4,1,3224,6,2,3,1,8),_NsrpVsdIfVLAN_Type())
nsrpVsdIfVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfVLAN.setStatus(_A)
_NsrpVsdIfMAC_Type=PhysAddress
_NsrpVsdIfMAC_Object=MibTableColumn
nsrpVsdIfMAC=_NsrpVsdIfMAC_Object((1,3,6,1,4,1,3224,6,2,3,1,9),_NsrpVsdIfMAC_Type())
nsrpVsdIfMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMAC.setStatus(_A)
class _NsrpVsdIfVSys_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsrpVsdIfVSys_Type.__name__=_G
_NsrpVsdIfVSys_Object=MibTableColumn
nsrpVsdIfVSys=_NsrpVsdIfVSys_Object((1,3,6,1,4,1,3224,6,2,3,1,10),_NsrpVsdIfVSys_Type())
nsrpVsdIfVSys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfVSys.setStatus(_A)
class _NsrpVsdIfMngTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngTelnet_Type.__name__=_C
_NsrpVsdIfMngTelnet_Object=MibTableColumn
nsrpVsdIfMngTelnet=_NsrpVsdIfMngTelnet_Object((1,3,6,1,4,1,3224,6,2,3,1,11),_NsrpVsdIfMngTelnet_Type())
nsrpVsdIfMngTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngTelnet.setStatus(_A)
class _NsrpVsdIfMngSCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngSCS_Type.__name__=_C
_NsrpVsdIfMngSCS_Object=MibTableColumn
nsrpVsdIfMngSCS=_NsrpVsdIfMngSCS_Object((1,3,6,1,4,1,3224,6,2,3,1,12),_NsrpVsdIfMngSCS_Type())
nsrpVsdIfMngSCS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngSCS.setStatus(_A)
class _NsrpVsdIfMngWEB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngWEB_Type.__name__=_C
_NsrpVsdIfMngWEB_Object=MibTableColumn
nsrpVsdIfMngWEB=_NsrpVsdIfMngWEB_Object((1,3,6,1,4,1,3224,6,2,3,1,13),_NsrpVsdIfMngWEB_Type())
nsrpVsdIfMngWEB.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngWEB.setStatus(_A)
class _NsrpVsdIfMngSSL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngSSL_Type.__name__=_C
_NsrpVsdIfMngSSL_Object=MibTableColumn
nsrpVsdIfMngSSL=_NsrpVsdIfMngSSL_Object((1,3,6,1,4,1,3224,6,2,3,1,14),_NsrpVsdIfMngSSL_Type())
nsrpVsdIfMngSSL.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngSSL.setStatus(_A)
class _NsrpVsdIfMngSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngSNMP_Type.__name__=_C
_NsrpVsdIfMngSNMP_Object=MibTableColumn
nsrpVsdIfMngSNMP=_NsrpVsdIfMngSNMP_Object((1,3,6,1,4,1,3224,6,2,3,1,15),_NsrpVsdIfMngSNMP_Type())
nsrpVsdIfMngSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngSNMP.setStatus(_A)
class _NsrpVsdIfMngGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngGlobal_Type.__name__=_C
_NsrpVsdIfMngGlobal_Object=MibTableColumn
nsrpVsdIfMngGlobal=_NsrpVsdIfMngGlobal_Object((1,3,6,1,4,1,3224,6,2,3,1,16),_NsrpVsdIfMngGlobal_Type())
nsrpVsdIfMngGlobal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngGlobal.setStatus(_A)
class _NsrpVsdIfMngGlobalPro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngGlobalPro_Type.__name__=_C
_NsrpVsdIfMngGlobalPro_Object=MibTableColumn
nsrpVsdIfMngGlobalPro=_NsrpVsdIfMngGlobalPro_Object((1,3,6,1,4,1,3224,6,2,3,1,17),_NsrpVsdIfMngGlobalPro_Type())
nsrpVsdIfMngGlobalPro.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngGlobalPro.setStatus(_A)
class _NsrpVsdIfMngPing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngPing_Type.__name__=_C
_NsrpVsdIfMngPing_Object=MibTableColumn
nsrpVsdIfMngPing=_NsrpVsdIfMngPing_Object((1,3,6,1,4,1,3224,6,2,3,1,18),_NsrpVsdIfMngPing_Type())
nsrpVsdIfMngPing.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngPing.setStatus(_A)
class _NsrpVsdIfMngIdentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsrpVsdIfMngIdentReset_Type.__name__=_C
_NsrpVsdIfMngIdentReset_Object=MibTableColumn
nsrpVsdIfMngIdentReset=_NsrpVsdIfMngIdentReset_Object((1,3,6,1,4,1,3224,6,2,3,1,19),_NsrpVsdIfMngIdentReset_Type())
nsrpVsdIfMngIdentReset.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdIfMngIdentReset.setStatus(_A)
_NsrpVsdGeneral_ObjectIdentity=ObjectIdentity
nsrpVsdGeneral=_NsrpVsdGeneral_ObjectIdentity((1,3,6,1,4,1,3224,6,2,4))
_NsrpVsdGeneralInitHoldTime_Type=Counter32
_NsrpVsdGeneralInitHoldTime_Object=MibScalar
nsrpVsdGeneralInitHoldTime=_NsrpVsdGeneralInitHoldTime_Object((1,3,6,1,4,1,3224,6,2,4,1),_NsrpVsdGeneralInitHoldTime_Type())
nsrpVsdGeneralInitHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGeneralInitHoldTime.setStatus(_A)
_NsrpVsdGeneralHbInterval_Type=Counter32
_NsrpVsdGeneralHbInterval_Object=MibScalar
nsrpVsdGeneralHbInterval=_NsrpVsdGeneralHbInterval_Object((1,3,6,1,4,1,3224,6,2,4,2),_NsrpVsdGeneralHbInterval_Type())
nsrpVsdGeneralHbInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGeneralHbInterval.setStatus(_A)
_NsrpVsdGeneralHbLostThres_Type=Counter32
_NsrpVsdGeneralHbLostThres_Object=MibScalar
nsrpVsdGeneralHbLostThres=_NsrpVsdGeneralHbLostThres_Object((1,3,6,1,4,1,3224,6,2,4,3),_NsrpVsdGeneralHbLostThres_Type())
nsrpVsdGeneralHbLostThres.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpVsdGeneralHbLostThres.setStatus(_A)
_NetscreenNsrpRTO_ObjectIdentity=ObjectIdentity
netscreenNsrpRTO=_NetscreenNsrpRTO_ObjectIdentity((1,3,6,1,4,1,3224,6,3))
_NsrpRtoGroupTable_Object=MibTable
nsrpRtoGroupTable=_NsrpRtoGroupTable_Object((1,3,6,1,4,1,3224,6,3,1))
if mibBuilder.loadTexts:nsrpRtoGroupTable.setStatus(_A)
_NsrpRtoGroupEntry_Object=MibTableRow
nsrpRtoGroupEntry=_NsrpRtoGroupEntry_Object((1,3,6,1,4,1,3224,6,3,1,1))
nsrpRtoGroupEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:nsrpRtoGroupEntry.setStatus(_A)
class _NsrpRtoGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpRtoGroupId_Type.__name__=_C
_NsrpRtoGroupId_Object=MibTableColumn
nsrpRtoGroupId=_NsrpRtoGroupId_Object((1,3,6,1,4,1,3224,6,3,1,1,1),_NsrpRtoGroupId_Type())
nsrpRtoGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoGroupId.setStatus(_A)
_NsrpRtoNumOfUnit_Type=Integer32
_NsrpRtoNumOfUnit_Object=MibTableColumn
nsrpRtoNumOfUnit=_NsrpRtoNumOfUnit_Object((1,3,6,1,4,1,3224,6,3,1,1,2),_NsrpRtoNumOfUnit_Type())
nsrpRtoNumOfUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoNumOfUnit.setStatus(_A)
_NsrpRtoUnitTable_Object=MibTable
nsrpRtoUnitTable=_NsrpRtoUnitTable_Object((1,3,6,1,4,1,3224,6,3,2))
if mibBuilder.loadTexts:nsrpRtoUnitTable.setStatus(_A)
_NsrpRtoUnitEntry_Object=MibTableRow
nsrpRtoUnitEntry=_NsrpRtoUnitEntry_Object((1,3,6,1,4,1,3224,6,3,2,1))
nsrpRtoUnitEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:nsrpRtoUnitEntry.setStatus(_A)
class _NsrpRtoUnitGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpRtoUnitGroupId_Type.__name__=_C
_NsrpRtoUnitGroupId_Object=MibTableColumn
nsrpRtoUnitGroupId=_NsrpRtoUnitGroupId_Object((1,3,6,1,4,1,3224,6,3,2,1,1),_NsrpRtoUnitGroupId_Type())
nsrpRtoUnitGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitGroupId.setStatus(_A)
class _NsrpRtoUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpRtoUnitId_Type.__name__=_C
_NsrpRtoUnitId_Object=MibTableColumn
nsrpRtoUnitId=_NsrpRtoUnitId_Object((1,3,6,1,4,1,3224,6,3,2,1,2),_NsrpRtoUnitId_Type())
nsrpRtoUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitId.setStatus(_A)
class _NsrpRtoUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('set',1),(_O,2)))
_NsrpRtoUnitStatus_Type.__name__=_C
_NsrpRtoUnitStatus_Object=MibTableColumn
nsrpRtoUnitStatus=_NsrpRtoUnitStatus_Object((1,3,6,1,4,1,3224,6,3,2,1,3),_NsrpRtoUnitStatus_Type())
nsrpRtoUnitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitStatus.setStatus(_A)
class _NsrpRtoUnitDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('out',1),('in',2)))
_NsrpRtoUnitDirection_Type.__name__=_C
_NsrpRtoUnitDirection_Object=MibTableColumn
nsrpRtoUnitDirection=_NsrpRtoUnitDirection_Object((1,3,6,1,4,1,3224,6,3,2,1,4),_NsrpRtoUnitDirection_Type())
nsrpRtoUnitDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitDirection.setStatus(_A)
_NsrpRtoUnitLostHeartbeat_Type=Counter32
_NsrpRtoUnitLostHeartbeat_Object=MibTableColumn
nsrpRtoUnitLostHeartbeat=_NsrpRtoUnitLostHeartbeat_Object((1,3,6,1,4,1,3224,6,3,2,1,5),_NsrpRtoUnitLostHeartbeat_Type())
nsrpRtoUnitLostHeartbeat.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitLostHeartbeat.setStatus(_A)
_NsrpRtoUnitToActive_Type=Counter32
_NsrpRtoUnitToActive_Object=MibTableColumn
nsrpRtoUnitToActive=_NsrpRtoUnitToActive_Object((1,3,6,1,4,1,3224,6,3,2,1,6),_NsrpRtoUnitToActive_Type())
nsrpRtoUnitToActive.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitToActive.setStatus(_A)
_NsrpRtoUnitToSet_Type=Counter32
_NsrpRtoUnitToSet_Object=MibTableColumn
nsrpRtoUnitToSet=_NsrpRtoUnitToSet_Object((1,3,6,1,4,1,3224,6,3,2,1,7),_NsrpRtoUnitToSet_Type())
nsrpRtoUnitToSet.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitToSet.setStatus(_A)
_NsrpRtoUnitLostPeer_Type=Counter32
_NsrpRtoUnitLostPeer_Object=MibTableColumn
nsrpRtoUnitLostPeer=_NsrpRtoUnitLostPeer_Object((1,3,6,1,4,1,3224,6,3,2,1,8),_NsrpRtoUnitLostPeer_Type())
nsrpRtoUnitLostPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitLostPeer.setStatus(_A)
_NsrpRtoUnitGroupDetach_Type=Counter32
_NsrpRtoUnitGroupDetach_Object=MibTableColumn
nsrpRtoUnitGroupDetach=_NsrpRtoUnitGroupDetach_Object((1,3,6,1,4,1,3224,6,3,2,1,9),_NsrpRtoUnitGroupDetach_Type())
nsrpRtoUnitGroupDetach.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoUnitGroupDetach.setStatus(_A)
_NsrpRtoCounter_ObjectIdentity=ObjectIdentity
nsrpRtoCounter=_NsrpRtoCounter_ObjectIdentity((1,3,6,1,4,1,3224,6,3,3))
_NsrpRtoCounterPakForwarded_Type=Counter32
_NsrpRtoCounterPakForwarded_Object=MibScalar
nsrpRtoCounterPakForwarded=_NsrpRtoCounterPakForwarded_Object((1,3,6,1,4,1,3224,6,3,3,1),_NsrpRtoCounterPakForwarded_Type())
nsrpRtoCounterPakForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterPakForwarded.setStatus(_A)
_NsrpRtoCounterPakReceived_Type=Counter32
_NsrpRtoCounterPakReceived_Object=MibScalar
nsrpRtoCounterPakReceived=_NsrpRtoCounterPakReceived_Object((1,3,6,1,4,1,3224,6,3,3,2),_NsrpRtoCounterPakReceived_Type())
nsrpRtoCounterPakReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterPakReceived.setStatus(_A)
_NsrpRtoCounterTable_Object=MibTable
nsrpRtoCounterTable=_NsrpRtoCounterTable_Object((1,3,6,1,4,1,3224,6,3,3,3))
if mibBuilder.loadTexts:nsrpRtoCounterTable.setStatus(_A)
_NsrpRtoCounterEntry_Object=MibTableRow
nsrpRtoCounterEntry=_NsrpRtoCounterEntry_Object((1,3,6,1,4,1,3224,6,3,3,3,1))
nsrpRtoCounterEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:nsrpRtoCounterEntry.setStatus(_A)
class _NsrpRtoCounterIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpRtoCounterIdx_Type.__name__=_C
_NsrpRtoCounterIdx_Object=MibTableColumn
nsrpRtoCounterIdx=_NsrpRtoCounterIdx_Object((1,3,6,1,4,1,3224,6,3,3,3,1,1),_NsrpRtoCounterIdx_Type())
nsrpRtoCounterIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterIdx.setStatus(_A)
class _NsrpRtoCounterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsrpRtoCounterName_Type.__name__=_G
_NsrpRtoCounterName_Object=MibTableColumn
nsrpRtoCounterName=_NsrpRtoCounterName_Object((1,3,6,1,4,1,3224,6,3,3,3,1,2),_NsrpRtoCounterName_Type())
nsrpRtoCounterName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterName.setStatus(_A)
_NsrpRtoCounterSend_Type=Counter32
_NsrpRtoCounterSend_Object=MibTableColumn
nsrpRtoCounterSend=_NsrpRtoCounterSend_Object((1,3,6,1,4,1,3224,6,3,3,3,1,3),_NsrpRtoCounterSend_Type())
nsrpRtoCounterSend.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterSend.setStatus(_A)
_NsrpRtoCounterReceive_Type=Counter32
_NsrpRtoCounterReceive_Object=MibTableColumn
nsrpRtoCounterReceive=_NsrpRtoCounterReceive_Object((1,3,6,1,4,1,3224,6,3,3,3,1,4),_NsrpRtoCounterReceive_Type())
nsrpRtoCounterReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterReceive.setStatus(_A)
_NsrpRtoCounterDrop_Type=Counter32
_NsrpRtoCounterDrop_Object=MibTableColumn
nsrpRtoCounterDrop=_NsrpRtoCounterDrop_Object((1,3,6,1,4,1,3224,6,3,3,3,1,5),_NsrpRtoCounterDrop_Type())
nsrpRtoCounterDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoCounterDrop.setStatus(_A)
_NsrpRtoGeneral_ObjectIdentity=ObjectIdentity
nsrpRtoGeneral=_NsrpRtoGeneral_ObjectIdentity((1,3,6,1,4,1,3224,6,3,4))
_NsrpRtoGeneralHbInterval_Type=Counter32
_NsrpRtoGeneralHbInterval_Object=MibScalar
nsrpRtoGeneralHbInterval=_NsrpRtoGeneralHbInterval_Object((1,3,6,1,4,1,3224,6,3,4,1),_NsrpRtoGeneralHbInterval_Type())
nsrpRtoGeneralHbInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoGeneralHbInterval.setStatus(_A)
_NsrpRtoGeneralHbLostThres_Type=Counter32
_NsrpRtoGeneralHbLostThres_Object=MibScalar
nsrpRtoGeneralHbLostThres=_NsrpRtoGeneralHbLostThres_Object((1,3,6,1,4,1,3224,6,3,4,2),_NsrpRtoGeneralHbLostThres_Type())
nsrpRtoGeneralHbLostThres.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoGeneralHbLostThres.setStatus(_A)
class _NsrpRtoGeneralSessSyncEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsrpRtoGeneralSessSyncEnable_Type.__name__=_C
_NsrpRtoGeneralSessSyncEnable_Object=MibScalar
nsrpRtoGeneralSessSyncEnable=_NsrpRtoGeneralSessSyncEnable_Object((1,3,6,1,4,1,3224,6,3,4,3),_NsrpRtoGeneralSessSyncEnable_Type())
nsrpRtoGeneralSessSyncEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpRtoGeneralSessSyncEnable.setStatus(_A)
_NetscreenNsrpTrack_ObjectIdentity=ObjectIdentity
netscreenNsrpTrack=_NetscreenNsrpTrack_ObjectIdentity((1,3,6,1,4,1,3224,6,4))
_NsrpTrackEnable_Type=Integer32
_NsrpTrackEnable_Object=MibScalar
nsrpTrackEnable=_NsrpTrackEnable_Object((1,3,6,1,4,1,3224,6,4,1),_NsrpTrackEnable_Type())
nsrpTrackEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackEnable.setStatus(_A)
_NsrpTrackThreshold_Type=Integer32
_NsrpTrackThreshold_Object=MibScalar
nsrpTrackThreshold=_NsrpTrackThreshold_Object((1,3,6,1,4,1,3224,6,4,2),_NsrpTrackThreshold_Type())
nsrpTrackThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackThreshold.setStatus(_A)
_NsrpTrackFailoverEnalble_Type=Integer32
_NsrpTrackFailoverEnalble_Object=MibScalar
nsrpTrackFailoverEnalble=_NsrpTrackFailoverEnalble_Object((1,3,6,1,4,1,3224,6,4,3),_NsrpTrackFailoverEnalble_Type())
nsrpTrackFailoverEnalble.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackFailoverEnalble.setStatus(_A)
_NsrpTrackTable_Object=MibTable
nsrpTrackTable=_NsrpTrackTable_Object((1,3,6,1,4,1,3224,6,4,4))
if mibBuilder.loadTexts:nsrpTrackTable.setStatus(_A)
_NsrpTrackEntry_Object=MibTableRow
nsrpTrackEntry=_NsrpTrackEntry_Object((1,3,6,1,4,1,3224,6,4,4,1))
nsrpTrackEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:nsrpTrackEntry.setStatus(_A)
class _NsrpTrackIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpTrackIpIndex_Type.__name__=_C
_NsrpTrackIpIndex_Object=MibTableColumn
nsrpTrackIpIndex=_NsrpTrackIpIndex_Object((1,3,6,1,4,1,3224,6,4,4,1,1),_NsrpTrackIpIndex_Type())
nsrpTrackIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpIndex.setStatus(_A)
_NsrpTrackIpAddr_Type=IpAddress
_NsrpTrackIpAddr_Object=MibTableColumn
nsrpTrackIpAddr=_NsrpTrackIpAddr_Object((1,3,6,1,4,1,3224,6,4,4,1,2),_NsrpTrackIpAddr_Type())
nsrpTrackIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpAddr.setStatus(_A)
class _NsrpTrackIpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('success',0),('fail',1)))
_NsrpTrackIpStatus_Type.__name__=_C
_NsrpTrackIpStatus_Object=MibTableColumn
nsrpTrackIpStatus=_NsrpTrackIpStatus_Object((1,3,6,1,4,1,3224,6,4,4,1,3),_NsrpTrackIpStatus_Type())
nsrpTrackIpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpStatus.setStatus(_A)
_NsrpTrackIpTimestamp_Type=Integer32
_NsrpTrackIpTimestamp_Object=MibTableColumn
nsrpTrackIpTimestamp=_NsrpTrackIpTimestamp_Object((1,3,6,1,4,1,3224,6,4,4,1,4),_NsrpTrackIpTimestamp_Type())
nsrpTrackIpTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpTimestamp.setStatus(_A)
_NsrpTrackIpInterval_Type=Integer32
_NsrpTrackIpInterval_Object=MibTableColumn
nsrpTrackIpInterval=_NsrpTrackIpInterval_Object((1,3,6,1,4,1,3224,6,4,4,1,5),_NsrpTrackIpInterval_Type())
nsrpTrackIpInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpInterval.setStatus(_A)
_NsrpTrackIpThreshhold_Type=Integer32
_NsrpTrackIpThreshhold_Object=MibTableColumn
nsrpTrackIpThreshhold=_NsrpTrackIpThreshhold_Object((1,3,6,1,4,1,3224,6,4,4,1,6),_NsrpTrackIpThreshhold_Type())
nsrpTrackIpThreshhold.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpThreshhold.setStatus(_A)
class _NsrpTrackIpMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ping',0),('arp',1)))
_NsrpTrackIpMethod_Type.__name__=_C
_NsrpTrackIpMethod_Object=MibTableColumn
nsrpTrackIpMethod=_NsrpTrackIpMethod_Object((1,3,6,1,4,1,3224,6,4,4,1,7),_NsrpTrackIpMethod_Type())
nsrpTrackIpMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpMethod.setStatus(_A)
_NsrpTrackIpWeight_Type=Integer32
_NsrpTrackIpWeight_Object=MibTableColumn
nsrpTrackIpWeight=_NsrpTrackIpWeight_Object((1,3,6,1,4,1,3224,6,4,4,1,8),_NsrpTrackIpWeight_Type())
nsrpTrackIpWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpWeight.setStatus(_A)
class _NsrpTrackIpIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsrpTrackIpIfName_Type.__name__=_G
_NsrpTrackIpIfName_Object=MibTableColumn
nsrpTrackIpIfName=_NsrpTrackIpIfName_Object((1,3,6,1,4,1,3224,6,4,4,1,9),_NsrpTrackIpIfName_Type())
nsrpTrackIpIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpIfName.setStatus(_A)
_NsrpTrackIpTotalCheck_Type=Integer32
_NsrpTrackIpTotalCheck_Object=MibTableColumn
nsrpTrackIpTotalCheck=_NsrpTrackIpTotalCheck_Object((1,3,6,1,4,1,3224,6,4,4,1,10),_NsrpTrackIpTotalCheck_Type())
nsrpTrackIpTotalCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpTotalCheck.setStatus(_A)
_NsrpTrackIpTotalFailedCheck_Type=Integer32
_NsrpTrackIpTotalFailedCheck_Object=MibTableColumn
nsrpTrackIpTotalFailedCheck=_NsrpTrackIpTotalFailedCheck_Object((1,3,6,1,4,1,3224,6,4,4,1,11),_NsrpTrackIpTotalFailedCheck_Type())
nsrpTrackIpTotalFailedCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpTrackIpTotalFailedCheck.setStatus(_A)
_NetscreenNsrpCluster_ObjectIdentity=ObjectIdentity
netscreenNsrpCluster=_NetscreenNsrpCluster_ObjectIdentity((1,3,6,1,4,1,3224,6,5))
_NsrpClusterTable_Object=MibTable
nsrpClusterTable=_NsrpClusterTable_Object((1,3,6,1,4,1,3224,6,5,1))
if mibBuilder.loadTexts:nsrpClusterTable.setStatus(_A)
_NsrpClusterEntry_Object=MibTableRow
nsrpClusterEntry=_NsrpClusterEntry_Object((1,3,6,1,4,1,3224,6,5,1,1))
nsrpClusterEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:nsrpClusterEntry.setStatus(_A)
class _NsrpClusterTblIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpClusterTblIndex_Type.__name__=_C
_NsrpClusterTblIndex_Object=MibTableColumn
nsrpClusterTblIndex=_NsrpClusterTblIndex_Object((1,3,6,1,4,1,3224,6,5,1,1,1),_NsrpClusterTblIndex_Type())
nsrpClusterTblIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpClusterTblIndex.setStatus(_A)
_NsrpClusterUnitId_Type=Integer32
_NsrpClusterUnitId_Object=MibTableColumn
nsrpClusterUnitId=_NsrpClusterUnitId_Object((1,3,6,1,4,1,3224,6,5,1,1,2),_NsrpClusterUnitId_Type())
nsrpClusterUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpClusterUnitId.setStatus(_A)
_NsrpClusterUnitCtrlMac_Type=PhysAddress
_NsrpClusterUnitCtrlMac_Object=MibTableColumn
nsrpClusterUnitCtrlMac=_NsrpClusterUnitCtrlMac_Object((1,3,6,1,4,1,3224,6,5,1,1,3),_NsrpClusterUnitCtrlMac_Type())
nsrpClusterUnitCtrlMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpClusterUnitCtrlMac.setStatus(_A)
_NsrpClusterUnitDataMac_Type=PhysAddress
_NsrpClusterUnitDataMac_Object=MibTableColumn
nsrpClusterUnitDataMac=_NsrpClusterUnitDataMac_Object((1,3,6,1,4,1,3224,6,5,1,1,4),_NsrpClusterUnitDataMac_Type())
nsrpClusterUnitDataMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpClusterUnitDataMac.setStatus(_A)
_NetscreenNsrpLinkInfo_ObjectIdentity=ObjectIdentity
netscreenNsrpLinkInfo=_NetscreenNsrpLinkInfo_ObjectIdentity((1,3,6,1,4,1,3224,6,6))
_NsrpLinkInfoTable_Object=MibTable
nsrpLinkInfoTable=_NsrpLinkInfoTable_Object((1,3,6,1,4,1,3224,6,6,1))
if mibBuilder.loadTexts:nsrpLinkInfoTable.setStatus(_A)
_NsrpLinkInfoEntry_Object=MibTableRow
nsrpLinkInfoEntry=_NsrpLinkInfoEntry_Object((1,3,6,1,4,1,3224,6,6,1,1))
nsrpLinkInfoEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:nsrpLinkInfoEntry.setStatus(_A)
class _NsrpLinkInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsrpLinkInfoIndex_Type.__name__=_C
_NsrpLinkInfoIndex_Object=MibTableColumn
nsrpLinkInfoIndex=_NsrpLinkInfoIndex_Object((1,3,6,1,4,1,3224,6,6,1,1,1),_NsrpLinkInfoIndex_Type())
nsrpLinkInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpLinkInfoIndex.setStatus(_A)
class _NsrpLinkInfoLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('control',0),('data',1),('unused',2),('hapath2',3)))
_NsrpLinkInfoLinkType_Type.__name__=_C
_NsrpLinkInfoLinkType_Object=MibTableColumn
nsrpLinkInfoLinkType=_NsrpLinkInfoLinkType_Object((1,3,6,1,4,1,3224,6,6,1,1,2),_NsrpLinkInfoLinkType_Type())
nsrpLinkInfoLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpLinkInfoLinkType.setStatus(_A)
class _NsrpLinkInfoChannel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsrpLinkInfoChannel_Type.__name__=_G
_NsrpLinkInfoChannel_Object=MibTableColumn
nsrpLinkInfoChannel=_NsrpLinkInfoChannel_Object((1,3,6,1,4,1,3224,6,6,1,1,3),_NsrpLinkInfoChannel_Type())
nsrpLinkInfoChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpLinkInfoChannel.setStatus(_A)
_NsrpLinkInfoMac_Type=PhysAddress
_NsrpLinkInfoMac_Object=MibTableColumn
nsrpLinkInfoMac=_NsrpLinkInfoMac_Object((1,3,6,1,4,1,3224,6,6,1,1,4),_NsrpLinkInfoMac_Type())
nsrpLinkInfoMac.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpLinkInfoMac.setStatus(_A)
class _NsrpLinkInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_NsrpLinkInfoState_Type.__name__=_C
_NsrpLinkInfoState_Object=MibTableColumn
nsrpLinkInfoState=_NsrpLinkInfoState_Object((1,3,6,1,4,1,3224,6,6,1,1,5),_NsrpLinkInfoState_Type())
nsrpLinkInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsrpLinkInfoState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'netscreenNsrpMibModule':netscreenNsrpMibModule,'netscreenNsrpGeneral':netscreenNsrpGeneral,'nsrpGeneralClusterId':nsrpGeneralClusterId,'nsrpGeneralLocalUnitId':nsrpGeneralLocalUnitId,'nsrpGeneralEncrypEnable':nsrpGeneralEncrypEnable,'nsrpGeneralAuthEnable':nsrpGeneralAuthEnable,'nsrpGeneralIfMonitor':nsrpGeneralIfMonitor,'nsrpGeneralGratArps':nsrpGeneralGratArps,'netscreenNsrpVSD':netscreenNsrpVSD,'nsrpVsdGroupTable':nsrpVsdGroupTable,'nsrpVsdGroupEntry':nsrpVsdGroupEntry,_J:nsrpVsdGroupID,'nsrpVsdGroupPriority':nsrpVsdGroupPriority,'nsrpVsdGroupPreempt':nsrpVsdGroupPreempt,'nsrpVsdGroupHoldDownTime':nsrpVsdGroupHoldDownTime,'nsrpVsdGroupNumberOfUnit':nsrpVsdGroupNumberOfUnit,'nsrpVsdGroupCntStateChange':nsrpVsdGroupCntStateChange,'nsrpVsdGroupCntToInit':nsrpVsdGroupCntToInit,'nsrpVsdGroupCntToMaster':nsrpVsdGroupCntToMaster,'nsrpVsdGroupCntToPBackup':nsrpVsdGroupCntToPBackup,'nsrpVsdGroupCntToBackup':nsrpVsdGroupCntToBackup,'nsrpVsdGroupCntToIneligible':nsrpVsdGroupCntToIneligible,'nsrpVsdGroupCntToInoperable':nsrpVsdGroupCntToInoperable,'nsrpVsdGroupCntMasterConflict':nsrpVsdGroupCntMasterConflict,'nsrpVsdGroupCntPbConfilict':nsrpVsdGroupCntPbConfilict,'nsrpVsdGroupCntHeartbeatTx':nsrpVsdGroupCntHeartbeatTx,'nsrpVsdGroupCntHeartbeatRx':nsrpVsdGroupCntHeartbeatRx,'nsrpVsdMemberTable':nsrpVsdMemberTable,'nsrpVsdMemberEntry':nsrpVsdMemberEntry,_K:nsrpVsdMemberGroupId,_L:nsrpVsdMemberUnitId,'nsrpVsdMemberStatus':nsrpVsdMemberStatus,'nsrpVsdMemberPriority':nsrpVsdMemberPriority,'nsrpVsdMemberPreempt':nsrpVsdMemberPreempt,'nsrpVsdInterfaceTable':nsrpVsdInterfaceTable,'nsrpVsdInterfaceEntry':nsrpVsdInterfaceEntry,_N:nsrpVsdIfIndex,'nsrpVsdIfStatus':nsrpVsdIfStatus,'nsrpVsdIfGroupId':nsrpVsdIfGroupId,'nsrpVsdIfIp':nsrpVsdIfIp,'nsrpVsdIfNetmask':nsrpVsdIfNetmask,'nsrpVsdIfGateway':nsrpVsdIfGateway,'nsrpVsdIfName':nsrpVsdIfName,'nsrpVsdIfVLAN':nsrpVsdIfVLAN,'nsrpVsdIfMAC':nsrpVsdIfMAC,'nsrpVsdIfVSys':nsrpVsdIfVSys,'nsrpVsdIfMngTelnet':nsrpVsdIfMngTelnet,'nsrpVsdIfMngSCS':nsrpVsdIfMngSCS,'nsrpVsdIfMngWEB':nsrpVsdIfMngWEB,'nsrpVsdIfMngSSL':nsrpVsdIfMngSSL,'nsrpVsdIfMngSNMP':nsrpVsdIfMngSNMP,'nsrpVsdIfMngGlobal':nsrpVsdIfMngGlobal,'nsrpVsdIfMngGlobalPro':nsrpVsdIfMngGlobalPro,'nsrpVsdIfMngPing':nsrpVsdIfMngPing,'nsrpVsdIfMngIdentReset':nsrpVsdIfMngIdentReset,'nsrpVsdGeneral':nsrpVsdGeneral,'nsrpVsdGeneralInitHoldTime':nsrpVsdGeneralInitHoldTime,'nsrpVsdGeneralHbInterval':nsrpVsdGeneralHbInterval,'nsrpVsdGeneralHbLostThres':nsrpVsdGeneralHbLostThres,'netscreenNsrpRTO':netscreenNsrpRTO,'nsrpRtoGroupTable':nsrpRtoGroupTable,'nsrpRtoGroupEntry':nsrpRtoGroupEntry,_P:nsrpRtoGroupId,'nsrpRtoNumOfUnit':nsrpRtoNumOfUnit,'nsrpRtoUnitTable':nsrpRtoUnitTable,'nsrpRtoUnitEntry':nsrpRtoUnitEntry,_Q:nsrpRtoUnitGroupId,_R:nsrpRtoUnitId,'nsrpRtoUnitStatus':nsrpRtoUnitStatus,'nsrpRtoUnitDirection':nsrpRtoUnitDirection,'nsrpRtoUnitLostHeartbeat':nsrpRtoUnitLostHeartbeat,'nsrpRtoUnitToActive':nsrpRtoUnitToActive,'nsrpRtoUnitToSet':nsrpRtoUnitToSet,'nsrpRtoUnitLostPeer':nsrpRtoUnitLostPeer,'nsrpRtoUnitGroupDetach':nsrpRtoUnitGroupDetach,'nsrpRtoCounter':nsrpRtoCounter,'nsrpRtoCounterPakForwarded':nsrpRtoCounterPakForwarded,'nsrpRtoCounterPakReceived':nsrpRtoCounterPakReceived,'nsrpRtoCounterTable':nsrpRtoCounterTable,'nsrpRtoCounterEntry':nsrpRtoCounterEntry,_S:nsrpRtoCounterIdx,'nsrpRtoCounterName':nsrpRtoCounterName,'nsrpRtoCounterSend':nsrpRtoCounterSend,'nsrpRtoCounterReceive':nsrpRtoCounterReceive,'nsrpRtoCounterDrop':nsrpRtoCounterDrop,'nsrpRtoGeneral':nsrpRtoGeneral,'nsrpRtoGeneralHbInterval':nsrpRtoGeneralHbInterval,'nsrpRtoGeneralHbLostThres':nsrpRtoGeneralHbLostThres,'nsrpRtoGeneralSessSyncEnable':nsrpRtoGeneralSessSyncEnable,'netscreenNsrpTrack':netscreenNsrpTrack,'nsrpTrackEnable':nsrpTrackEnable,'nsrpTrackThreshold':nsrpTrackThreshold,'nsrpTrackFailoverEnalble':nsrpTrackFailoverEnalble,'nsrpTrackTable':nsrpTrackTable,'nsrpTrackEntry':nsrpTrackEntry,_T:nsrpTrackIpIndex,'nsrpTrackIpAddr':nsrpTrackIpAddr,'nsrpTrackIpStatus':nsrpTrackIpStatus,'nsrpTrackIpTimestamp':nsrpTrackIpTimestamp,'nsrpTrackIpInterval':nsrpTrackIpInterval,'nsrpTrackIpThreshhold':nsrpTrackIpThreshhold,'nsrpTrackIpMethod':nsrpTrackIpMethod,'nsrpTrackIpWeight':nsrpTrackIpWeight,'nsrpTrackIpIfName':nsrpTrackIpIfName,'nsrpTrackIpTotalCheck':nsrpTrackIpTotalCheck,'nsrpTrackIpTotalFailedCheck':nsrpTrackIpTotalFailedCheck,'netscreenNsrpCluster':netscreenNsrpCluster,'nsrpClusterTable':nsrpClusterTable,'nsrpClusterEntry':nsrpClusterEntry,_U:nsrpClusterTblIndex,'nsrpClusterUnitId':nsrpClusterUnitId,'nsrpClusterUnitCtrlMac':nsrpClusterUnitCtrlMac,'nsrpClusterUnitDataMac':nsrpClusterUnitDataMac,'netscreenNsrpLinkInfo':netscreenNsrpLinkInfo,'nsrpLinkInfoTable':nsrpLinkInfoTable,'nsrpLinkInfoEntry':nsrpLinkInfoEntry,_V:nsrpLinkInfoIndex,'nsrpLinkInfoLinkType':nsrpLinkInfoLinkType,'nsrpLinkInfoChannel':nsrpLinkInfoChannel,'nsrpLinkInfoMac':nsrpLinkInfoMac,'nsrpLinkInfoState':nsrpLinkInfoState})