_O='read-write'
_N='qtechL2TPv2TunnelSrcIP'
_M='qtechL2TPv2SessionDstIP'
_L='qtechL2TPv2SessionLocalVrf'
_K='qtechL2TPv2SessionExistTime'
_J='qtechL2TPv2SessionSrcIP'
_I='qtechL2TPv2SessionAccessDeviceID'
_H='qtechL2TPv2SessionIMSI'
_G='qtechL2TPv2TunnelDstIP'
_F='Unsigned32'
_E='qtechL2TPv2SessionLocalID'
_D='qtechL2TPv2TunnelLocalID'
_C='read-only'
_B='QTECH-L2TPV2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechL2TPv2MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,117))
_QtechL2TPv2Objects_ObjectIdentity=ObjectIdentity
qtechL2TPv2Objects=_QtechL2TPv2Objects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,117,1))
_QtechL2TPv2TunnelTable_Object=MibTable
qtechL2TPv2TunnelTable=_QtechL2TPv2TunnelTable_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1))
if mibBuilder.loadTexts:qtechL2TPv2TunnelTable.setStatus(_A)
_QtechL2TPv2TunnelEntry_Object=MibTableRow
qtechL2TPv2TunnelEntry=_QtechL2TPv2TunnelEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1))
qtechL2TPv2TunnelEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:qtechL2TPv2TunnelEntry.setStatus(_A)
class _QtechL2TPv2TunnelLocalID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechL2TPv2TunnelLocalID_Type.__name__=_F
_QtechL2TPv2TunnelLocalID_Object=MibTableColumn
qtechL2TPv2TunnelLocalID=_QtechL2TPv2TunnelLocalID_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,1),_QtechL2TPv2TunnelLocalID_Type())
qtechL2TPv2TunnelLocalID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelLocalID.setStatus(_A)
_QtechL2TPv2TunnelRemoteID_Type=Unsigned32
_QtechL2TPv2TunnelRemoteID_Object=MibTableColumn
qtechL2TPv2TunnelRemoteID=_QtechL2TPv2TunnelRemoteID_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,2),_QtechL2TPv2TunnelRemoteID_Type())
qtechL2TPv2TunnelRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelRemoteID.setStatus(_A)
_QtechL2TPv2TunnelStatus_Type=Unsigned32
_QtechL2TPv2TunnelStatus_Object=MibTableColumn
qtechL2TPv2TunnelStatus=_QtechL2TPv2TunnelStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,3),_QtechL2TPv2TunnelStatus_Type())
qtechL2TPv2TunnelStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechL2TPv2TunnelStatus.setStatus(_A)
_QtechL2TPv2TunnelSrcIP_Type=IpAddress
_QtechL2TPv2TunnelSrcIP_Object=MibTableColumn
qtechL2TPv2TunnelSrcIP=_QtechL2TPv2TunnelSrcIP_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,4),_QtechL2TPv2TunnelSrcIP_Type())
qtechL2TPv2TunnelSrcIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelSrcIP.setStatus(_A)
_QtechL2TPv2TunnelDstIP_Type=IpAddress
_QtechL2TPv2TunnelDstIP_Object=MibTableColumn
qtechL2TPv2TunnelDstIP=_QtechL2TPv2TunnelDstIP_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,5),_QtechL2TPv2TunnelDstIP_Type())
qtechL2TPv2TunnelDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelDstIP.setStatus(_A)
_QtechL2TPv2TunnelLacHostname_Type=OctetString
_QtechL2TPv2TunnelLacHostname_Object=MibTableColumn
qtechL2TPv2TunnelLacHostname=_QtechL2TPv2TunnelLacHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,6),_QtechL2TPv2TunnelLacHostname_Type())
qtechL2TPv2TunnelLacHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelLacHostname.setStatus(_A)
_QtechL2TPv2TunnelLacVendor_Type=OctetString
_QtechL2TPv2TunnelLacVendor_Object=MibTableColumn
qtechL2TPv2TunnelLacVendor=_QtechL2TPv2TunnelLacVendor_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,1,1,7),_QtechL2TPv2TunnelLacVendor_Type())
qtechL2TPv2TunnelLacVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2TunnelLacVendor.setStatus(_A)
_QtechL2TPv2SessionTable_Object=MibTable
qtechL2TPv2SessionTable=_QtechL2TPv2SessionTable_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2))
if mibBuilder.loadTexts:qtechL2TPv2SessionTable.setStatus(_A)
_QtechL2TPv2SessionEntry_Object=MibTableRow
qtechL2TPv2SessionEntry=_QtechL2TPv2SessionEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1))
qtechL2TPv2SessionEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:qtechL2TPv2SessionEntry.setStatus(_A)
class _QtechL2TPv2SessionLocalID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechL2TPv2SessionLocalID_Type.__name__=_F
_QtechL2TPv2SessionLocalID_Object=MibTableColumn
qtechL2TPv2SessionLocalID=_QtechL2TPv2SessionLocalID_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,1),_QtechL2TPv2SessionLocalID_Type())
qtechL2TPv2SessionLocalID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionLocalID.setStatus(_A)
_QtechL2TPv2SessionRemoteID_Type=Unsigned32
_QtechL2TPv2SessionRemoteID_Object=MibTableColumn
qtechL2TPv2SessionRemoteID=_QtechL2TPv2SessionRemoteID_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,2),_QtechL2TPv2SessionRemoteID_Type())
qtechL2TPv2SessionRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionRemoteID.setStatus(_A)
_QtechL2TPv2SessionUserName_Type=OctetString
_QtechL2TPv2SessionUserName_Object=MibTableColumn
qtechL2TPv2SessionUserName=_QtechL2TPv2SessionUserName_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,3),_QtechL2TPv2SessionUserName_Type())
qtechL2TPv2SessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionUserName.setStatus(_A)
_QtechL2TPv2SessionStatus_Type=Unsigned32
_QtechL2TPv2SessionStatus_Object=MibTableColumn
qtechL2TPv2SessionStatus=_QtechL2TPv2SessionStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,4),_QtechL2TPv2SessionStatus_Type())
qtechL2TPv2SessionStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechL2TPv2SessionStatus.setStatus(_A)
_QtechL2TPv2SessionSrcIP_Type=IpAddress
_QtechL2TPv2SessionSrcIP_Object=MibTableColumn
qtechL2TPv2SessionSrcIP=_QtechL2TPv2SessionSrcIP_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,5),_QtechL2TPv2SessionSrcIP_Type())
qtechL2TPv2SessionSrcIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionSrcIP.setStatus(_A)
_QtechL2TPv2SessionDstIP_Type=IpAddress
_QtechL2TPv2SessionDstIP_Object=MibTableColumn
qtechL2TPv2SessionDstIP=_QtechL2TPv2SessionDstIP_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,6),_QtechL2TPv2SessionDstIP_Type())
qtechL2TPv2SessionDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionDstIP.setStatus(_A)
_QtechL2TPv2SessionLocalVrf_Type=Integer32
_QtechL2TPv2SessionLocalVrf_Object=MibTableColumn
qtechL2TPv2SessionLocalVrf=_QtechL2TPv2SessionLocalVrf_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,7),_QtechL2TPv2SessionLocalVrf_Type())
qtechL2TPv2SessionLocalVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionLocalVrf.setStatus(_A)
_QtechL2TPv2SessionExistTime_Type=Integer32
_QtechL2TPv2SessionExistTime_Object=MibTableColumn
qtechL2TPv2SessionExistTime=_QtechL2TPv2SessionExistTime_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,8),_QtechL2TPv2SessionExistTime_Type())
qtechL2TPv2SessionExistTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionExistTime.setStatus(_A)
_QtechL2TPv2SessionIMSI_Type=OctetString
_QtechL2TPv2SessionIMSI_Object=MibTableColumn
qtechL2TPv2SessionIMSI=_QtechL2TPv2SessionIMSI_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,9),_QtechL2TPv2SessionIMSI_Type())
qtechL2TPv2SessionIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionIMSI.setStatus(_A)
_QtechL2TPv2SessionAccessDeviceID_Type=OctetString
_QtechL2TPv2SessionAccessDeviceID_Object=MibTableColumn
qtechL2TPv2SessionAccessDeviceID=_QtechL2TPv2SessionAccessDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,2,1,10),_QtechL2TPv2SessionAccessDeviceID_Type())
qtechL2TPv2SessionAccessDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionAccessDeviceID.setStatus(_A)
_QtechL2TPv2SessionTrafficStatTable_Object=MibTable
qtechL2TPv2SessionTrafficStatTable=_QtechL2TPv2SessionTrafficStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3))
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatTable.setStatus(_A)
_QtechL2TPv2SessionTrafficStatEntry_Object=MibTableRow
qtechL2TPv2SessionTrafficStatEntry=_QtechL2TPv2SessionTrafficStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1))
qtechL2TPv2SessionTrafficStatEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatEntry.setStatus(_A)
_QtechL2TPv2SessionTrafficStatRxBytes_Type=Counter64
_QtechL2TPv2SessionTrafficStatRxBytes_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatRxBytes=_QtechL2TPv2SessionTrafficStatRxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,1),_QtechL2TPv2SessionTrafficStatRxBytes_Type())
qtechL2TPv2SessionTrafficStatRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatRxBytes.setStatus(_A)
_QtechL2TPv2SessionTrafficStatRxPkts_Type=Counter64
_QtechL2TPv2SessionTrafficStatRxPkts_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatRxPkts=_QtechL2TPv2SessionTrafficStatRxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,2),_QtechL2TPv2SessionTrafficStatRxPkts_Type())
qtechL2TPv2SessionTrafficStatRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatRxPkts.setStatus(_A)
_QtechL2TPv2SessionTrafficStatRxErrPkts_Type=Counter64
_QtechL2TPv2SessionTrafficStatRxErrPkts_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatRxErrPkts=_QtechL2TPv2SessionTrafficStatRxErrPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,3),_QtechL2TPv2SessionTrafficStatRxErrPkts_Type())
qtechL2TPv2SessionTrafficStatRxErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatRxErrPkts.setStatus(_A)
_QtechL2TPv2SessionTrafficStatRxSpeed_Type=Counter64
_QtechL2TPv2SessionTrafficStatRxSpeed_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatRxSpeed=_QtechL2TPv2SessionTrafficStatRxSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,4),_QtechL2TPv2SessionTrafficStatRxSpeed_Type())
qtechL2TPv2SessionTrafficStatRxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatRxSpeed.setStatus(_A)
_QtechL2TPv2SessionTrafficStatTxBytes_Type=Counter64
_QtechL2TPv2SessionTrafficStatTxBytes_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatTxBytes=_QtechL2TPv2SessionTrafficStatTxBytes_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,5),_QtechL2TPv2SessionTrafficStatTxBytes_Type())
qtechL2TPv2SessionTrafficStatTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatTxBytes.setStatus(_A)
_QtechL2TPv2SessionTrafficStatTxPkts_Type=Counter64
_QtechL2TPv2SessionTrafficStatTxPkts_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatTxPkts=_QtechL2TPv2SessionTrafficStatTxPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,6),_QtechL2TPv2SessionTrafficStatTxPkts_Type())
qtechL2TPv2SessionTrafficStatTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatTxPkts.setStatus(_A)
_QtechL2TPv2SessionTrafficStatTxSpeed_Type=Counter64
_QtechL2TPv2SessionTrafficStatTxSpeed_Object=MibTableColumn
qtechL2TPv2SessionTrafficStatTxSpeed=_QtechL2TPv2SessionTrafficStatTxSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,117,1,3,1,7),_QtechL2TPv2SessionTrafficStatTxSpeed_Type())
qtechL2TPv2SessionTrafficStatTxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPv2SessionTrafficStatTxSpeed.setStatus(_A)
_QtechL2TPv2Notifications_ObjectIdentity=ObjectIdentity
qtechL2TPv2Notifications=_QtechL2TPv2Notifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,117,2))
_QtechL2TPv2SessionNotifications_ObjectIdentity=ObjectIdentity
qtechL2TPv2SessionNotifications=_QtechL2TPv2SessionNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,117,2,1))
_QtechL2TPVersion_Type=OctetString
_QtechL2TPVersion_Object=MibScalar
qtechL2TPVersion=_QtechL2TPVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,117,3),_QtechL2TPVersion_Type())
qtechL2TPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechL2TPVersion.setStatus(_A)
qtechL2TPv2SessionStart=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,117,2,1,1))
qtechL2TPv2SessionStart.setObjects(*((_B,_G),(_B,_D),(_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechL2TPv2SessionStart.setStatus(_A)
qtechL2TPv2SessionStop=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,117,2,1,2))
qtechL2TPv2SessionStop.setObjects(*((_B,_D),(_B,_E),(_B,_N),(_B,_G),(_B,_J),(_B,_M),(_B,_L),(_B,_K),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechL2TPv2SessionStop.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechL2TPv2MIB':qtechL2TPv2MIB,'qtechL2TPv2Objects':qtechL2TPv2Objects,'qtechL2TPv2TunnelTable':qtechL2TPv2TunnelTable,'qtechL2TPv2TunnelEntry':qtechL2TPv2TunnelEntry,_D:qtechL2TPv2TunnelLocalID,'qtechL2TPv2TunnelRemoteID':qtechL2TPv2TunnelRemoteID,'qtechL2TPv2TunnelStatus':qtechL2TPv2TunnelStatus,_N:qtechL2TPv2TunnelSrcIP,_G:qtechL2TPv2TunnelDstIP,'qtechL2TPv2TunnelLacHostname':qtechL2TPv2TunnelLacHostname,'qtechL2TPv2TunnelLacVendor':qtechL2TPv2TunnelLacVendor,'qtechL2TPv2SessionTable':qtechL2TPv2SessionTable,'qtechL2TPv2SessionEntry':qtechL2TPv2SessionEntry,_E:qtechL2TPv2SessionLocalID,'qtechL2TPv2SessionRemoteID':qtechL2TPv2SessionRemoteID,'qtechL2TPv2SessionUserName':qtechL2TPv2SessionUserName,'qtechL2TPv2SessionStatus':qtechL2TPv2SessionStatus,_J:qtechL2TPv2SessionSrcIP,_M:qtechL2TPv2SessionDstIP,_L:qtechL2TPv2SessionLocalVrf,_K:qtechL2TPv2SessionExistTime,_H:qtechL2TPv2SessionIMSI,_I:qtechL2TPv2SessionAccessDeviceID,'qtechL2TPv2SessionTrafficStatTable':qtechL2TPv2SessionTrafficStatTable,'qtechL2TPv2SessionTrafficStatEntry':qtechL2TPv2SessionTrafficStatEntry,'qtechL2TPv2SessionTrafficStatRxBytes':qtechL2TPv2SessionTrafficStatRxBytes,'qtechL2TPv2SessionTrafficStatRxPkts':qtechL2TPv2SessionTrafficStatRxPkts,'qtechL2TPv2SessionTrafficStatRxErrPkts':qtechL2TPv2SessionTrafficStatRxErrPkts,'qtechL2TPv2SessionTrafficStatRxSpeed':qtechL2TPv2SessionTrafficStatRxSpeed,'qtechL2TPv2SessionTrafficStatTxBytes':qtechL2TPv2SessionTrafficStatTxBytes,'qtechL2TPv2SessionTrafficStatTxPkts':qtechL2TPv2SessionTrafficStatTxPkts,'qtechL2TPv2SessionTrafficStatTxSpeed':qtechL2TPv2SessionTrafficStatTxSpeed,'qtechL2TPv2Notifications':qtechL2TPv2Notifications,'qtechL2TPv2SessionNotifications':qtechL2TPv2SessionNotifications,'qtechL2TPv2SessionStart':qtechL2TPv2SessionStart,'qtechL2TPv2SessionStop':qtechL2TPv2SessionStop,'qtechL2TPVersion':qtechL2TPVersion})