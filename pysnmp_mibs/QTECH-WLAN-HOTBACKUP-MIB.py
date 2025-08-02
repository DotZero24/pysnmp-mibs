_S='qtechNotifyNewState'
_R='qtechNotifyOldState'
_Q='qtechNotifyCtxId'
_P='qtechNotifyPeerIp'
_O='qtechNotifyPeerIpType'
_N='qtechWlanHotbackupContextId'
_M='qtechWlanHotbackupCtxIpAddress'
_L='qtechWlanHotbackupIpAddress'
_K='pair-standby'
_J='pair-active'
_I='single-standby'
_H='single-active'
_G='unknown'
_F='disable'
_E='accessible-for-notify'
_D='read-only'
_C='Integer32'
_B='QTECH-WLAN-HOTBACKUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechWlanHotbackupMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,115))
if mibBuilder.loadTexts:qtechWlanHotbackupMIB.setRevisions(('2012-07-31 00:00',))
_QtechWlanHotbackupMIBObjects_ObjectIdentity=ObjectIdentity
qtechWlanHotbackupMIBObjects=_QtechWlanHotbackupMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,115,1))
_QtechWlanHotbackupPeerTable_Object=MibTable
qtechWlanHotbackupPeerTable=_QtechWlanHotbackupPeerTable_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,1))
if mibBuilder.loadTexts:qtechWlanHotbackupPeerTable.setStatus(_A)
_QtechWlanHotbackupPeerEntry_Object=MibTableRow
qtechWlanHotbackupPeerEntry=_QtechWlanHotbackupPeerEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,1,1))
qtechWlanHotbackupPeerEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechWlanHotbackupPeerEntry.setStatus(_A)
_QtechWlanHotbackupIpAddress_Type=IpAddress
_QtechWlanHotbackupIpAddress_Object=MibTableColumn
qtechWlanHotbackupIpAddress=_QtechWlanHotbackupIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,1,1,1),_QtechWlanHotbackupIpAddress_Type())
qtechWlanHotbackupIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechWlanHotbackupIpAddress.setStatus(_A)
class _QtechWlanHotbackupIsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('enable',1)))
_QtechWlanHotbackupIsEnabled_Type.__name__=_C
_QtechWlanHotbackupIsEnabled_Object=MibTableColumn
qtechWlanHotbackupIsEnabled=_QtechWlanHotbackupIsEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,1,1,2),_QtechWlanHotbackupIsEnabled_Type())
qtechWlanHotbackupIsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWlanHotbackupIsEnabled.setStatus(_A)
class _QtechWlanHotbackupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hb-disable',1),('probe',2),('hdsk',3),('tcp-connect',4),('sulking',5),('channel-up',6)))
_QtechWlanHotbackupState_Type.__name__=_C
_QtechWlanHotbackupState_Object=MibTableColumn
qtechWlanHotbackupState=_QtechWlanHotbackupState_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,1,1,3),_QtechWlanHotbackupState_Type())
qtechWlanHotbackupState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWlanHotbackupState.setStatus(_A)
_QtechWlanHotbackupContextTable_Object=MibTable
qtechWlanHotbackupContextTable=_QtechWlanHotbackupContextTable_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,2))
if mibBuilder.loadTexts:qtechWlanHotbackupContextTable.setStatus(_A)
_QtechWlanHotbackupContextEntry_Object=MibTableRow
qtechWlanHotbackupContextEntry=_QtechWlanHotbackupContextEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,2,1))
qtechWlanHotbackupContextEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:qtechWlanHotbackupContextEntry.setStatus(_A)
_QtechWlanHotbackupCtxIpAddress_Type=IpAddress
_QtechWlanHotbackupCtxIpAddress_Object=MibTableColumn
qtechWlanHotbackupCtxIpAddress=_QtechWlanHotbackupCtxIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,2,1,1),_QtechWlanHotbackupCtxIpAddress_Type())
qtechWlanHotbackupCtxIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWlanHotbackupCtxIpAddress.setStatus(_A)
_QtechWlanHotbackupContextId_Type=Integer32
_QtechWlanHotbackupContextId_Object=MibTableColumn
qtechWlanHotbackupContextId=_QtechWlanHotbackupContextId_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,2,1,2),_QtechWlanHotbackupContextId_Type())
qtechWlanHotbackupContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWlanHotbackupContextId.setStatus(_A)
class _QtechWlanHotbackupContextState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_QtechWlanHotbackupContextState_Type.__name__=_C
_QtechWlanHotbackupContextState_Object=MibTableColumn
qtechWlanHotbackupContextState=_QtechWlanHotbackupContextState_Object((1,3,6,1,4,1,27514,1,1,10,2,115,1,2,1,3),_QtechWlanHotbackupContextState_Type())
qtechWlanHotbackupContextState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWlanHotbackupContextState.setStatus(_A)
_QtechWlanHotbackupNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
qtechWlanHotbackupNotificationsMIBObjects=_QtechWlanHotbackupNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,115,2))
_QtechWlanHotbackupNtfObjects_ObjectIdentity=ObjectIdentity
qtechWlanHotbackupNtfObjects=_QtechWlanHotbackupNtfObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,115,2,1))
_QtechNotifyPeerIpType_Type=InetAddressType
_QtechNotifyPeerIpType_Object=MibScalar
qtechNotifyPeerIpType=_QtechNotifyPeerIpType_Object((1,3,6,1,4,1,27514,1,1,10,2,115,2,1,1),_QtechNotifyPeerIpType_Type())
qtechNotifyPeerIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNotifyPeerIpType.setStatus(_A)
_QtechNotifyPeerIp_Type=InetAddress
_QtechNotifyPeerIp_Object=MibScalar
qtechNotifyPeerIp=_QtechNotifyPeerIp_Object((1,3,6,1,4,1,27514,1,1,10,2,115,2,1,2),_QtechNotifyPeerIp_Type())
qtechNotifyPeerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNotifyPeerIp.setStatus(_A)
class _QtechNotifyCtxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechNotifyCtxId_Type.__name__=_C
_QtechNotifyCtxId_Object=MibScalar
qtechNotifyCtxId=_QtechNotifyCtxId_Object((1,3,6,1,4,1,27514,1,1,10,2,115,2,1,3),_QtechNotifyCtxId_Type())
qtechNotifyCtxId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNotifyCtxId.setStatus(_A)
class _QtechNotifyOldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_QtechNotifyOldState_Type.__name__=_C
_QtechNotifyOldState_Object=MibScalar
qtechNotifyOldState=_QtechNotifyOldState_Object((1,3,6,1,4,1,27514,1,1,10,2,115,2,1,4),_QtechNotifyOldState_Type())
qtechNotifyOldState.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNotifyOldState.setStatus(_A)
class _QtechNotifyNewState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5)))
_QtechNotifyNewState_Type.__name__=_C
_QtechNotifyNewState_Object=MibScalar
qtechNotifyNewState=_QtechNotifyNewState_Object((1,3,6,1,4,1,27514,1,1,10,2,115,2,1,5),_QtechNotifyNewState_Type())
qtechNotifyNewState.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechNotifyNewState.setStatus(_A)
_QtechWlanHotbackupNotifications_ObjectIdentity=ObjectIdentity
qtechWlanHotbackupNotifications=_QtechWlanHotbackupNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,115,2,2))
qtechNotifyWlanHBChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,115,2,2,1))
qtechNotifyWlanHBChange.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechNotifyWlanHBChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechWlanHotbackupMIB':qtechWlanHotbackupMIB,'qtechWlanHotbackupMIBObjects':qtechWlanHotbackupMIBObjects,'qtechWlanHotbackupPeerTable':qtechWlanHotbackupPeerTable,'qtechWlanHotbackupPeerEntry':qtechWlanHotbackupPeerEntry,_L:qtechWlanHotbackupIpAddress,'qtechWlanHotbackupIsEnabled':qtechWlanHotbackupIsEnabled,'qtechWlanHotbackupState':qtechWlanHotbackupState,'qtechWlanHotbackupContextTable':qtechWlanHotbackupContextTable,'qtechWlanHotbackupContextEntry':qtechWlanHotbackupContextEntry,_M:qtechWlanHotbackupCtxIpAddress,_N:qtechWlanHotbackupContextId,'qtechWlanHotbackupContextState':qtechWlanHotbackupContextState,'qtechWlanHotbackupNotificationsMIBObjects':qtechWlanHotbackupNotificationsMIBObjects,'qtechWlanHotbackupNtfObjects':qtechWlanHotbackupNtfObjects,_O:qtechNotifyPeerIpType,_P:qtechNotifyPeerIp,_Q:qtechNotifyCtxId,_R:qtechNotifyOldState,_S:qtechNotifyNewState,'qtechWlanHotbackupNotifications':qtechWlanHotbackupNotifications,'qtechNotifyWlanHBChange':qtechNotifyWlanHBChange})