_J='forwarding'
_I='blocking'
_H='rcPortPeerBackupLocalPortStatus'
_G='rcPortPeerBackupPortIndex'
_F='OctetString'
_E='read-only'
_D='SWITCH-PORTPEERBACKUP-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
Vlanset,=mibBuilder.importSymbols('SWITCH-TC','Vlanset')
rcPortPeerBackup=ModuleIdentity((1,3,6,1,4,1,8886,6,1,80))
_RcPortPeerBackupObjects_ObjectIdentity=ObjectIdentity
rcPortPeerBackupObjects=_RcPortPeerBackupObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,80,1))
_RcPortPeerBackupCfgTable_Object=MibTable
rcPortPeerBackupCfgTable=_RcPortPeerBackupCfgTable_Object((1,3,6,1,4,1,8886,6,1,80,1,1))
if mibBuilder.loadTexts:rcPortPeerBackupCfgTable.setStatus(_A)
_RcPortPeerBackupCfgEntry_Object=MibTableRow
rcPortPeerBackupCfgEntry=_RcPortPeerBackupCfgEntry_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1))
rcPortPeerBackupCfgEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:rcPortPeerBackupCfgEntry.setStatus(_A)
_RcPortPeerBackupPortIndex_Type=Integer32
_RcPortPeerBackupPortIndex_Object=MibTableColumn
rcPortPeerBackupPortIndex=_RcPortPeerBackupPortIndex_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,1),_RcPortPeerBackupPortIndex_Type())
rcPortPeerBackupPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupPortIndex.setStatus(_A)
_RcPortPeerBackupVlanlist_Type=Vlanset
_RcPortPeerBackupVlanlist_Object=MibTableColumn
rcPortPeerBackupVlanlist=_RcPortPeerBackupVlanlist_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,2),_RcPortPeerBackupVlanlist_Type())
rcPortPeerBackupVlanlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupVlanlist.setStatus(_A)
class _RcPortPeerBackupMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcPortPeerBackupMdName_Type.__name__=_F
_RcPortPeerBackupMdName_Object=MibTableColumn
rcPortPeerBackupMdName=_RcPortPeerBackupMdName_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,3),_RcPortPeerBackupMdName_Type())
rcPortPeerBackupMdName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupMdName.setStatus(_A)
class _RcPortPeerBackupMdLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcPortPeerBackupMdLevel_Type.__name__=_C
_RcPortPeerBackupMdLevel_Object=MibTableColumn
rcPortPeerBackupMdLevel=_RcPortPeerBackupMdLevel_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,4),_RcPortPeerBackupMdLevel_Type())
rcPortPeerBackupMdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupMdLevel.setStatus(_A)
class _RcPortPeerBackupMaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_RcPortPeerBackupMaName_Type.__name__=_F
_RcPortPeerBackupMaName_Object=MibTableColumn
rcPortPeerBackupMaName=_RcPortPeerBackupMaName_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,5),_RcPortPeerBackupMaName_Type())
rcPortPeerBackupMaName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupMaName.setStatus(_A)
class _RcPortPeerBackupRemoteMep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_RcPortPeerBackupRemoteMep_Type.__name__=_C
_RcPortPeerBackupRemoteMep_Object=MibTableColumn
rcPortPeerBackupRemoteMep=_RcPortPeerBackupRemoteMep_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,6),_RcPortPeerBackupRemoteMep_Type())
rcPortPeerBackupRemoteMep.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupRemoteMep.setStatus(_A)
_RcPortPeerBackupRowStatus_Type=RowStatus
_RcPortPeerBackupRowStatus_Object=MibTableColumn
rcPortPeerBackupRowStatus=_RcPortPeerBackupRowStatus_Object((1,3,6,1,4,1,8886,6,1,80,1,1,1,7),_RcPortPeerBackupRowStatus_Type())
rcPortPeerBackupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortPeerBackupRowStatus.setStatus(_A)
_RcPortPeerBackupStatusTable_Object=MibTable
rcPortPeerBackupStatusTable=_RcPortPeerBackupStatusTable_Object((1,3,6,1,4,1,8886,6,1,80,1,2))
if mibBuilder.loadTexts:rcPortPeerBackupStatusTable.setStatus(_A)
_RcPortPeerBackupStatusEntry_Object=MibTableRow
rcPortPeerBackupStatusEntry=_RcPortPeerBackupStatusEntry_Object((1,3,6,1,4,1,8886,6,1,80,1,2,1))
rcPortPeerBackupStatusEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:rcPortPeerBackupStatusEntry.setStatus(_A)
class _RcPortPeerBackupLocalPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RcPortPeerBackupLocalPortStatus_Type.__name__=_C
_RcPortPeerBackupLocalPortStatus_Object=MibTableColumn
rcPortPeerBackupLocalPortStatus=_RcPortPeerBackupLocalPortStatus_Object((1,3,6,1,4,1,8886,6,1,80,1,2,1,1),_RcPortPeerBackupLocalPortStatus_Type())
rcPortPeerBackupLocalPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortPeerBackupLocalPortStatus.setStatus(_A)
class _RcPortPeerBackupRemotePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('unknown',3)))
_RcPortPeerBackupRemotePortStatus_Type.__name__=_C
_RcPortPeerBackupRemotePortStatus_Object=MibTableColumn
rcPortPeerBackupRemotePortStatus=_RcPortPeerBackupRemotePortStatus_Object((1,3,6,1,4,1,8886,6,1,80,1,2,1,2),_RcPortPeerBackupRemotePortStatus_Type())
rcPortPeerBackupRemotePortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortPeerBackupRemotePortStatus.setStatus(_A)
_RcPortPeerBackupStatusDuration_Type=Integer32
_RcPortPeerBackupStatusDuration_Object=MibTableColumn
rcPortPeerBackupStatusDuration=_RcPortPeerBackupStatusDuration_Object((1,3,6,1,4,1,8886,6,1,80,1,2,1,3),_RcPortPeerBackupStatusDuration_Type())
rcPortPeerBackupStatusDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortPeerBackupStatusDuration.setStatus(_A)
_RcPortPeerBackupSwitchCnt_Type=Integer32
_RcPortPeerBackupSwitchCnt_Object=MibTableColumn
rcPortPeerBackupSwitchCnt=_RcPortPeerBackupSwitchCnt_Object((1,3,6,1,4,1,8886,6,1,80,1,2,1,4),_RcPortPeerBackupSwitchCnt_Type())
rcPortPeerBackupSwitchCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortPeerBackupSwitchCnt.setStatus(_A)
_RcPortPeerBackupNotifications_ObjectIdentity=ObjectIdentity
rcPortPeerBackupNotifications=_RcPortPeerBackupNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,80,2))
rcPortPeerBackupLocalPortForward=NotificationType((1,3,6,1,4,1,8886,6,1,80,2,1))
rcPortPeerBackupLocalPortForward.setObjects((_D,_H))
if mibBuilder.loadTexts:rcPortPeerBackupLocalPortForward.setStatus(_A)
rcPortPeerBackupLocalPortBlock=NotificationType((1,3,6,1,4,1,8886,6,1,80,2,2))
rcPortPeerBackupLocalPortBlock.setObjects((_D,_H))
if mibBuilder.loadTexts:rcPortPeerBackupLocalPortBlock.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rcPortPeerBackup':rcPortPeerBackup,'rcPortPeerBackupObjects':rcPortPeerBackupObjects,'rcPortPeerBackupCfgTable':rcPortPeerBackupCfgTable,'rcPortPeerBackupCfgEntry':rcPortPeerBackupCfgEntry,_G:rcPortPeerBackupPortIndex,'rcPortPeerBackupVlanlist':rcPortPeerBackupVlanlist,'rcPortPeerBackupMdName':rcPortPeerBackupMdName,'rcPortPeerBackupMdLevel':rcPortPeerBackupMdLevel,'rcPortPeerBackupMaName':rcPortPeerBackupMaName,'rcPortPeerBackupRemoteMep':rcPortPeerBackupRemoteMep,'rcPortPeerBackupRowStatus':rcPortPeerBackupRowStatus,'rcPortPeerBackupStatusTable':rcPortPeerBackupStatusTable,'rcPortPeerBackupStatusEntry':rcPortPeerBackupStatusEntry,_H:rcPortPeerBackupLocalPortStatus,'rcPortPeerBackupRemotePortStatus':rcPortPeerBackupRemotePortStatus,'rcPortPeerBackupStatusDuration':rcPortPeerBackupStatusDuration,'rcPortPeerBackupSwitchCnt':rcPortPeerBackupSwitchCnt,'rcPortPeerBackupNotifications':rcPortPeerBackupNotifications,'rcPortPeerBackupLocalPortForward':rcPortPeerBackupLocalPortForward,'rcPortPeerBackupLocalPortBlock':rcPortPeerBackupLocalPortBlock})