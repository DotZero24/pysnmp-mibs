_O='read-write'
_N='fsL2TPv2TunnelSrcIP'
_M='fsL2TPv2SessionDstIP'
_L='fsL2TPv2SessionLocalVrf'
_K='fsL2TPv2SessionExistTime'
_J='fsL2TPv2SessionSrcIP'
_I='fsL2TPv2SessionAccessDeviceID'
_H='fsL2TPv2SessionIMSI'
_G='fsL2TPv2TunnelDstIP'
_F='Unsigned32'
_E='fsL2TPv2SessionLocalID'
_D='fsL2TPv2TunnelLocalID'
_C='read-only'
_B='FS-L2TPV2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsL2TPv2MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,117))
_FsL2TPv2Objects_ObjectIdentity=ObjectIdentity
fsL2TPv2Objects=_FsL2TPv2Objects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,117,1))
_FsL2TPv2TunnelTable_Object=MibTable
fsL2TPv2TunnelTable=_FsL2TPv2TunnelTable_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1))
if mibBuilder.loadTexts:fsL2TPv2TunnelTable.setStatus(_A)
_FsL2TPv2TunnelEntry_Object=MibTableRow
fsL2TPv2TunnelEntry=_FsL2TPv2TunnelEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1))
fsL2TPv2TunnelEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsL2TPv2TunnelEntry.setStatus(_A)
class _FsL2TPv2TunnelLocalID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsL2TPv2TunnelLocalID_Type.__name__=_F
_FsL2TPv2TunnelLocalID_Object=MibTableColumn
fsL2TPv2TunnelLocalID=_FsL2TPv2TunnelLocalID_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,1),_FsL2TPv2TunnelLocalID_Type())
fsL2TPv2TunnelLocalID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelLocalID.setStatus(_A)
_FsL2TPv2TunnelRemoteID_Type=Unsigned32
_FsL2TPv2TunnelRemoteID_Object=MibTableColumn
fsL2TPv2TunnelRemoteID=_FsL2TPv2TunnelRemoteID_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,2),_FsL2TPv2TunnelRemoteID_Type())
fsL2TPv2TunnelRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelRemoteID.setStatus(_A)
_FsL2TPv2TunnelStatus_Type=Unsigned32
_FsL2TPv2TunnelStatus_Object=MibTableColumn
fsL2TPv2TunnelStatus=_FsL2TPv2TunnelStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,3),_FsL2TPv2TunnelStatus_Type())
fsL2TPv2TunnelStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsL2TPv2TunnelStatus.setStatus(_A)
_FsL2TPv2TunnelSrcIP_Type=IpAddress
_FsL2TPv2TunnelSrcIP_Object=MibTableColumn
fsL2TPv2TunnelSrcIP=_FsL2TPv2TunnelSrcIP_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,4),_FsL2TPv2TunnelSrcIP_Type())
fsL2TPv2TunnelSrcIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelSrcIP.setStatus(_A)
_FsL2TPv2TunnelDstIP_Type=IpAddress
_FsL2TPv2TunnelDstIP_Object=MibTableColumn
fsL2TPv2TunnelDstIP=_FsL2TPv2TunnelDstIP_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,5),_FsL2TPv2TunnelDstIP_Type())
fsL2TPv2TunnelDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelDstIP.setStatus(_A)
_FsL2TPv2TunnelLacHostname_Type=OctetString
_FsL2TPv2TunnelLacHostname_Object=MibTableColumn
fsL2TPv2TunnelLacHostname=_FsL2TPv2TunnelLacHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,6),_FsL2TPv2TunnelLacHostname_Type())
fsL2TPv2TunnelLacHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelLacHostname.setStatus(_A)
_FsL2TPv2TunnelLacVendor_Type=OctetString
_FsL2TPv2TunnelLacVendor_Object=MibTableColumn
fsL2TPv2TunnelLacVendor=_FsL2TPv2TunnelLacVendor_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,1,1,7),_FsL2TPv2TunnelLacVendor_Type())
fsL2TPv2TunnelLacVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2TunnelLacVendor.setStatus(_A)
_FsL2TPv2SessionTable_Object=MibTable
fsL2TPv2SessionTable=_FsL2TPv2SessionTable_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2))
if mibBuilder.loadTexts:fsL2TPv2SessionTable.setStatus(_A)
_FsL2TPv2SessionEntry_Object=MibTableRow
fsL2TPv2SessionEntry=_FsL2TPv2SessionEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1))
fsL2TPv2SessionEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsL2TPv2SessionEntry.setStatus(_A)
class _FsL2TPv2SessionLocalID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsL2TPv2SessionLocalID_Type.__name__=_F
_FsL2TPv2SessionLocalID_Object=MibTableColumn
fsL2TPv2SessionLocalID=_FsL2TPv2SessionLocalID_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,1),_FsL2TPv2SessionLocalID_Type())
fsL2TPv2SessionLocalID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionLocalID.setStatus(_A)
_FsL2TPv2SessionRemoteID_Type=Unsigned32
_FsL2TPv2SessionRemoteID_Object=MibTableColumn
fsL2TPv2SessionRemoteID=_FsL2TPv2SessionRemoteID_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,2),_FsL2TPv2SessionRemoteID_Type())
fsL2TPv2SessionRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionRemoteID.setStatus(_A)
_FsL2TPv2SessionUserName_Type=OctetString
_FsL2TPv2SessionUserName_Object=MibTableColumn
fsL2TPv2SessionUserName=_FsL2TPv2SessionUserName_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,3),_FsL2TPv2SessionUserName_Type())
fsL2TPv2SessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionUserName.setStatus(_A)
_FsL2TPv2SessionStatus_Type=Unsigned32
_FsL2TPv2SessionStatus_Object=MibTableColumn
fsL2TPv2SessionStatus=_FsL2TPv2SessionStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,4),_FsL2TPv2SessionStatus_Type())
fsL2TPv2SessionStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsL2TPv2SessionStatus.setStatus(_A)
_FsL2TPv2SessionSrcIP_Type=IpAddress
_FsL2TPv2SessionSrcIP_Object=MibTableColumn
fsL2TPv2SessionSrcIP=_FsL2TPv2SessionSrcIP_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,5),_FsL2TPv2SessionSrcIP_Type())
fsL2TPv2SessionSrcIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionSrcIP.setStatus(_A)
_FsL2TPv2SessionDstIP_Type=IpAddress
_FsL2TPv2SessionDstIP_Object=MibTableColumn
fsL2TPv2SessionDstIP=_FsL2TPv2SessionDstIP_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,6),_FsL2TPv2SessionDstIP_Type())
fsL2TPv2SessionDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionDstIP.setStatus(_A)
_FsL2TPv2SessionLocalVrf_Type=Integer32
_FsL2TPv2SessionLocalVrf_Object=MibTableColumn
fsL2TPv2SessionLocalVrf=_FsL2TPv2SessionLocalVrf_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,7),_FsL2TPv2SessionLocalVrf_Type())
fsL2TPv2SessionLocalVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionLocalVrf.setStatus(_A)
_FsL2TPv2SessionExistTime_Type=Integer32
_FsL2TPv2SessionExistTime_Object=MibTableColumn
fsL2TPv2SessionExistTime=_FsL2TPv2SessionExistTime_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,8),_FsL2TPv2SessionExistTime_Type())
fsL2TPv2SessionExistTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionExistTime.setStatus(_A)
_FsL2TPv2SessionIMSI_Type=OctetString
_FsL2TPv2SessionIMSI_Object=MibTableColumn
fsL2TPv2SessionIMSI=_FsL2TPv2SessionIMSI_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,9),_FsL2TPv2SessionIMSI_Type())
fsL2TPv2SessionIMSI.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionIMSI.setStatus(_A)
_FsL2TPv2SessionAccessDeviceID_Type=OctetString
_FsL2TPv2SessionAccessDeviceID_Object=MibTableColumn
fsL2TPv2SessionAccessDeviceID=_FsL2TPv2SessionAccessDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,2,1,10),_FsL2TPv2SessionAccessDeviceID_Type())
fsL2TPv2SessionAccessDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionAccessDeviceID.setStatus(_A)
_FsL2TPv2SessionTrafficStatTable_Object=MibTable
fsL2TPv2SessionTrafficStatTable=_FsL2TPv2SessionTrafficStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3))
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatTable.setStatus(_A)
_FsL2TPv2SessionTrafficStatEntry_Object=MibTableRow
fsL2TPv2SessionTrafficStatEntry=_FsL2TPv2SessionTrafficStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1))
fsL2TPv2SessionTrafficStatEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatEntry.setStatus(_A)
_FsL2TPv2SessionTrafficStatRxBytes_Type=Counter64
_FsL2TPv2SessionTrafficStatRxBytes_Object=MibTableColumn
fsL2TPv2SessionTrafficStatRxBytes=_FsL2TPv2SessionTrafficStatRxBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,1),_FsL2TPv2SessionTrafficStatRxBytes_Type())
fsL2TPv2SessionTrafficStatRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatRxBytes.setStatus(_A)
_FsL2TPv2SessionTrafficStatRxPkts_Type=Counter64
_FsL2TPv2SessionTrafficStatRxPkts_Object=MibTableColumn
fsL2TPv2SessionTrafficStatRxPkts=_FsL2TPv2SessionTrafficStatRxPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,2),_FsL2TPv2SessionTrafficStatRxPkts_Type())
fsL2TPv2SessionTrafficStatRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatRxPkts.setStatus(_A)
_FsL2TPv2SessionTrafficStatRxErrPkts_Type=Counter64
_FsL2TPv2SessionTrafficStatRxErrPkts_Object=MibTableColumn
fsL2TPv2SessionTrafficStatRxErrPkts=_FsL2TPv2SessionTrafficStatRxErrPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,3),_FsL2TPv2SessionTrafficStatRxErrPkts_Type())
fsL2TPv2SessionTrafficStatRxErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatRxErrPkts.setStatus(_A)
_FsL2TPv2SessionTrafficStatRxSpeed_Type=Counter64
_FsL2TPv2SessionTrafficStatRxSpeed_Object=MibTableColumn
fsL2TPv2SessionTrafficStatRxSpeed=_FsL2TPv2SessionTrafficStatRxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,4),_FsL2TPv2SessionTrafficStatRxSpeed_Type())
fsL2TPv2SessionTrafficStatRxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatRxSpeed.setStatus(_A)
_FsL2TPv2SessionTrafficStatTxBytes_Type=Counter64
_FsL2TPv2SessionTrafficStatTxBytes_Object=MibTableColumn
fsL2TPv2SessionTrafficStatTxBytes=_FsL2TPv2SessionTrafficStatTxBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,5),_FsL2TPv2SessionTrafficStatTxBytes_Type())
fsL2TPv2SessionTrafficStatTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatTxBytes.setStatus(_A)
_FsL2TPv2SessionTrafficStatTxPkts_Type=Counter64
_FsL2TPv2SessionTrafficStatTxPkts_Object=MibTableColumn
fsL2TPv2SessionTrafficStatTxPkts=_FsL2TPv2SessionTrafficStatTxPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,6),_FsL2TPv2SessionTrafficStatTxPkts_Type())
fsL2TPv2SessionTrafficStatTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatTxPkts.setStatus(_A)
_FsL2TPv2SessionTrafficStatTxSpeed_Type=Counter64
_FsL2TPv2SessionTrafficStatTxSpeed_Object=MibTableColumn
fsL2TPv2SessionTrafficStatTxSpeed=_FsL2TPv2SessionTrafficStatTxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,117,1,3,1,7),_FsL2TPv2SessionTrafficStatTxSpeed_Type())
fsL2TPv2SessionTrafficStatTxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPv2SessionTrafficStatTxSpeed.setStatus(_A)
_FsL2TPv2Notifications_ObjectIdentity=ObjectIdentity
fsL2TPv2Notifications=_FsL2TPv2Notifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,117,2))
_FsL2TPv2SessionNotifications_ObjectIdentity=ObjectIdentity
fsL2TPv2SessionNotifications=_FsL2TPv2SessionNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,117,2,1))
_FsL2TPVersion_Type=OctetString
_FsL2TPVersion_Object=MibScalar
fsL2TPVersion=_FsL2TPVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,117,3),_FsL2TPVersion_Type())
fsL2TPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsL2TPVersion.setStatus(_A)
fsL2TPv2SessionStart=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,117,2,1,1))
fsL2TPv2SessionStart.setObjects(*((_B,_G),(_B,_D),(_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsL2TPv2SessionStart.setStatus(_A)
fsL2TPv2SessionStop=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,117,2,1,2))
fsL2TPv2SessionStop.setObjects(*((_B,_D),(_B,_E),(_B,_N),(_B,_G),(_B,_J),(_B,_M),(_B,_L),(_B,_K),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsL2TPv2SessionStop.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsL2TPv2MIB':fsL2TPv2MIB,'fsL2TPv2Objects':fsL2TPv2Objects,'fsL2TPv2TunnelTable':fsL2TPv2TunnelTable,'fsL2TPv2TunnelEntry':fsL2TPv2TunnelEntry,_D:fsL2TPv2TunnelLocalID,'fsL2TPv2TunnelRemoteID':fsL2TPv2TunnelRemoteID,'fsL2TPv2TunnelStatus':fsL2TPv2TunnelStatus,_N:fsL2TPv2TunnelSrcIP,_G:fsL2TPv2TunnelDstIP,'fsL2TPv2TunnelLacHostname':fsL2TPv2TunnelLacHostname,'fsL2TPv2TunnelLacVendor':fsL2TPv2TunnelLacVendor,'fsL2TPv2SessionTable':fsL2TPv2SessionTable,'fsL2TPv2SessionEntry':fsL2TPv2SessionEntry,_E:fsL2TPv2SessionLocalID,'fsL2TPv2SessionRemoteID':fsL2TPv2SessionRemoteID,'fsL2TPv2SessionUserName':fsL2TPv2SessionUserName,'fsL2TPv2SessionStatus':fsL2TPv2SessionStatus,_J:fsL2TPv2SessionSrcIP,_M:fsL2TPv2SessionDstIP,_L:fsL2TPv2SessionLocalVrf,_K:fsL2TPv2SessionExistTime,_H:fsL2TPv2SessionIMSI,_I:fsL2TPv2SessionAccessDeviceID,'fsL2TPv2SessionTrafficStatTable':fsL2TPv2SessionTrafficStatTable,'fsL2TPv2SessionTrafficStatEntry':fsL2TPv2SessionTrafficStatEntry,'fsL2TPv2SessionTrafficStatRxBytes':fsL2TPv2SessionTrafficStatRxBytes,'fsL2TPv2SessionTrafficStatRxPkts':fsL2TPv2SessionTrafficStatRxPkts,'fsL2TPv2SessionTrafficStatRxErrPkts':fsL2TPv2SessionTrafficStatRxErrPkts,'fsL2TPv2SessionTrafficStatRxSpeed':fsL2TPv2SessionTrafficStatRxSpeed,'fsL2TPv2SessionTrafficStatTxBytes':fsL2TPv2SessionTrafficStatTxBytes,'fsL2TPv2SessionTrafficStatTxPkts':fsL2TPv2SessionTrafficStatTxPkts,'fsL2TPv2SessionTrafficStatTxSpeed':fsL2TPv2SessionTrafficStatTxSpeed,'fsL2TPv2Notifications':fsL2TPv2Notifications,'fsL2TPv2SessionNotifications':fsL2TPv2SessionNotifications,'fsL2TPv2SessionStart':fsL2TPv2SessionStart,'fsL2TPv2SessionStop':fsL2TPv2SessionStop,'fsL2TPVersion':fsL2TPVersion})