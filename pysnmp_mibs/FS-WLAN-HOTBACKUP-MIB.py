_S='fsNotifyNewState'
_R='fsNotifyOldState'
_Q='fsNotifyCtxId'
_P='fsNotifyPeerIp'
_O='fsNotifyPeerIpType'
_N='fsWlanHotbackupContextId'
_M='fsWlanHotbackupCtxIpAddress'
_L='fsWlanHotbackupIpAddress'
_K='pair-standby'
_J='pair-active'
_I='single-standby'
_H='single-active'
_G='unknown'
_F='disable'
_E='accessible-for-notify'
_D='read-only'
_C='Integer32'
_B='FS-WLAN-HOTBACKUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsWlanHotbackupMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,115))
if mibBuilder.loadTexts:fsWlanHotbackupMIB.setRevisions(('2012-07-31 00:00',))
_FsWlanHotbackupMIBObjects_ObjectIdentity=ObjectIdentity
fsWlanHotbackupMIBObjects=_FsWlanHotbackupMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,115,1))
_FsWlanHotbackupPeerTable_Object=MibTable
fsWlanHotbackupPeerTable=_FsWlanHotbackupPeerTable_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,1))
if mibBuilder.loadTexts:fsWlanHotbackupPeerTable.setStatus(_A)
_FsWlanHotbackupPeerEntry_Object=MibTableRow
fsWlanHotbackupPeerEntry=_FsWlanHotbackupPeerEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,1,1))
fsWlanHotbackupPeerEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsWlanHotbackupPeerEntry.setStatus(_A)
_FsWlanHotbackupIpAddress_Type=IpAddress
_FsWlanHotbackupIpAddress_Object=MibTableColumn
fsWlanHotbackupIpAddress=_FsWlanHotbackupIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,1,1,1),_FsWlanHotbackupIpAddress_Type())
fsWlanHotbackupIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsWlanHotbackupIpAddress.setStatus(_A)
class _FsWlanHotbackupIsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('enable',1)))
_FsWlanHotbackupIsEnabled_Type.__name__=_C
_FsWlanHotbackupIsEnabled_Object=MibTableColumn
fsWlanHotbackupIsEnabled=_FsWlanHotbackupIsEnabled_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,1,1,2),_FsWlanHotbackupIsEnabled_Type())
fsWlanHotbackupIsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWlanHotbackupIsEnabled.setStatus(_A)
class _FsWlanHotbackupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hb-disable',1),('probe',2),('hdsk',3),('tcp-connect',4),('sulking',5),('channel-up',6)))
_FsWlanHotbackupState_Type.__name__=_C
_FsWlanHotbackupState_Object=MibTableColumn
fsWlanHotbackupState=_FsWlanHotbackupState_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,1,1,3),_FsWlanHotbackupState_Type())
fsWlanHotbackupState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWlanHotbackupState.setStatus(_A)
_FsWlanHotbackupContextTable_Object=MibTable
fsWlanHotbackupContextTable=_FsWlanHotbackupContextTable_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,2))
if mibBuilder.loadTexts:fsWlanHotbackupContextTable.setStatus(_A)
_FsWlanHotbackupContextEntry_Object=MibTableRow
fsWlanHotbackupContextEntry=_FsWlanHotbackupContextEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,2,1))
fsWlanHotbackupContextEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:fsWlanHotbackupContextEntry.setStatus(_A)
_FsWlanHotbackupCtxIpAddress_Type=IpAddress
_FsWlanHotbackupCtxIpAddress_Object=MibTableColumn
fsWlanHotbackupCtxIpAddress=_FsWlanHotbackupCtxIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,2,1,1),_FsWlanHotbackupCtxIpAddress_Type())
fsWlanHotbackupCtxIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWlanHotbackupCtxIpAddress.setStatus(_A)
_FsWlanHotbackupContextId_Type=Integer32
_FsWlanHotbackupContextId_Object=MibTableColumn
fsWlanHotbackupContextId=_FsWlanHotbackupContextId_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,2,1,2),_FsWlanHotbackupContextId_Type())
fsWlanHotbackupContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWlanHotbackupContextId.setStatus(_A)
class _FsWlanHotbackupContextState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_FsWlanHotbackupContextState_Type.__name__=_C
_FsWlanHotbackupContextState_Object=MibTableColumn
fsWlanHotbackupContextState=_FsWlanHotbackupContextState_Object((1,3,6,1,4,1,52642,1,1,10,2,115,1,2,1,3),_FsWlanHotbackupContextState_Type())
fsWlanHotbackupContextState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWlanHotbackupContextState.setStatus(_A)
_FsWlanHotbackupNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
fsWlanHotbackupNotificationsMIBObjects=_FsWlanHotbackupNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,115,2))
_FsWlanHotbackupNtfObjects_ObjectIdentity=ObjectIdentity
fsWlanHotbackupNtfObjects=_FsWlanHotbackupNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,115,2,1))
_FsNotifyPeerIpType_Type=InetAddressType
_FsNotifyPeerIpType_Object=MibScalar
fsNotifyPeerIpType=_FsNotifyPeerIpType_Object((1,3,6,1,4,1,52642,1,1,10,2,115,2,1,1),_FsNotifyPeerIpType_Type())
fsNotifyPeerIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNotifyPeerIpType.setStatus(_A)
_FsNotifyPeerIp_Type=InetAddress
_FsNotifyPeerIp_Object=MibScalar
fsNotifyPeerIp=_FsNotifyPeerIp_Object((1,3,6,1,4,1,52642,1,1,10,2,115,2,1,2),_FsNotifyPeerIp_Type())
fsNotifyPeerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNotifyPeerIp.setStatus(_A)
class _FsNotifyCtxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsNotifyCtxId_Type.__name__=_C
_FsNotifyCtxId_Object=MibScalar
fsNotifyCtxId=_FsNotifyCtxId_Object((1,3,6,1,4,1,52642,1,1,10,2,115,2,1,3),_FsNotifyCtxId_Type())
fsNotifyCtxId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNotifyCtxId.setStatus(_A)
class _FsNotifyOldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_FsNotifyOldState_Type.__name__=_C
_FsNotifyOldState_Object=MibScalar
fsNotifyOldState=_FsNotifyOldState_Object((1,3,6,1,4,1,52642,1,1,10,2,115,2,1,4),_FsNotifyOldState_Type())
fsNotifyOldState.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNotifyOldState.setStatus(_A)
class _FsNotifyNewState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_FsNotifyNewState_Type.__name__=_C
_FsNotifyNewState_Object=MibScalar
fsNotifyNewState=_FsNotifyNewState_Object((1,3,6,1,4,1,52642,1,1,10,2,115,2,1,5),_FsNotifyNewState_Type())
fsNotifyNewState.setMaxAccess(_E)
if mibBuilder.loadTexts:fsNotifyNewState.setStatus(_A)
_FsWlanHotbackupNotifications_ObjectIdentity=ObjectIdentity
fsWlanHotbackupNotifications=_FsWlanHotbackupNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,115,2,2))
fsNotifyWlanHBChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,115,2,2,1))
fsNotifyWlanHBChange.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:fsNotifyWlanHBChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsWlanHotbackupMIB':fsWlanHotbackupMIB,'fsWlanHotbackupMIBObjects':fsWlanHotbackupMIBObjects,'fsWlanHotbackupPeerTable':fsWlanHotbackupPeerTable,'fsWlanHotbackupPeerEntry':fsWlanHotbackupPeerEntry,_L:fsWlanHotbackupIpAddress,'fsWlanHotbackupIsEnabled':fsWlanHotbackupIsEnabled,'fsWlanHotbackupState':fsWlanHotbackupState,'fsWlanHotbackupContextTable':fsWlanHotbackupContextTable,'fsWlanHotbackupContextEntry':fsWlanHotbackupContextEntry,_M:fsWlanHotbackupCtxIpAddress,_N:fsWlanHotbackupContextId,'fsWlanHotbackupContextState':fsWlanHotbackupContextState,'fsWlanHotbackupNotificationsMIBObjects':fsWlanHotbackupNotificationsMIBObjects,'fsWlanHotbackupNtfObjects':fsWlanHotbackupNtfObjects,_O:fsNotifyPeerIpType,_P:fsNotifyPeerIp,_Q:fsNotifyCtxId,_R:fsNotifyOldState,_S:fsNotifyNewState,'fsWlanHotbackupNotifications':fsWlanHotbackupNotifications,'fsNotifyWlanHBChange':fsNotifyWlanHBChange})