_a='bsDhcpSnoopingBindingInterface'
_Z='bsDhcpSnoopingNotificationMsgType'
_Y='bsDhcpSnoopingNotificationSourcePort'
_X='seconds'
_W='bsDhcpSnoopingBindingMacAddress'
_V='bsDhcpSnoopingVlanId'
_U='DisplayString'
_T='InetPortNumber'
_S='bsDhcpSnoopingIfTrusted'
_R='bsDhcpSnoopingNotificationSourceMACAddr'
_Q='bsDhcpSnoopingNotificationClientMACAddr'
_P='bsDhcpSnoopingBindingVlanId'
_O='bsDhcpSnoopingIfIndex'
_N='not-accessible'
_M='Integer32'
_L='bsDhcpSnoopingExtSaveSftpServerAddress'
_K='bsDhcpSnoopingExtSaveSftpServerAddressType'
_J='bsDhcpSnoopingExtSaveTftpServerAddress'
_I='bsDhcpSnoopingExtSaveTftpServerAddressType'
_H='bsDhcpSnoopingExtSaveUsbTargetUnit'
_G='accessible-for-notify'
_F='read-create'
_E='read-only'
_D='bsDhcpSnoopingNotificationsBindingMacAddress'
_C='read-write'
_B='BAY-STACK-DHCP-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_T)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_U,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackDhcpSnoopingMib=ModuleIdentity((1,3,6,1,4,1,45,5,17))
if mibBuilder.loadTexts:bayStackDhcpSnoopingMib.setRevisions(('2020-11-12 00:00','2020-11-02 00:00','2014-03-20 00:00','2013-10-11 00:00','2013-07-25 00:00','2013-07-09 00:00','2013-04-18 00:00','2013-03-21 00:00','2012-05-28 00:00','2010-11-18 00:00','2010-10-05 00:00','2009-09-23 00:00','2009-04-01 00:00','2009-03-30 00:00','2009-03-26 00:00','2008-10-30 00:00','2008-06-02 00:00','2006-06-23 00:00'))
_BsDhcpSnoopingNotifications_ObjectIdentity=ObjectIdentity
bsDhcpSnoopingNotifications=_BsDhcpSnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,17,0))
_BsDhcpSnoopingObjects_ObjectIdentity=ObjectIdentity
bsDhcpSnoopingObjects=_BsDhcpSnoopingObjects_ObjectIdentity((1,3,6,1,4,1,45,5,17,1))
_BsDhcpSnoopingScalars_ObjectIdentity=ObjectIdentity
bsDhcpSnoopingScalars=_BsDhcpSnoopingScalars_ObjectIdentity((1,3,6,1,4,1,45,5,17,1,1))
_BsDhcpSnoopingEnabled_Type=TruthValue
_BsDhcpSnoopingEnabled_Object=MibScalar
bsDhcpSnoopingEnabled=_BsDhcpSnoopingEnabled_Object((1,3,6,1,4,1,45,5,17,1,1,1),_BsDhcpSnoopingEnabled_Type())
bsDhcpSnoopingEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingEnabled.setStatus(_A)
_BsDhcpSnoopingOption82Enabled_Type=TruthValue
_BsDhcpSnoopingOption82Enabled_Object=MibScalar
bsDhcpSnoopingOption82Enabled=_BsDhcpSnoopingOption82Enabled_Object((1,3,6,1,4,1,45,5,17,1,1,2),_BsDhcpSnoopingOption82Enabled_Type())
bsDhcpSnoopingOption82Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingOption82Enabled.setStatus(_A)
_BsDhcpSnoopingVlanTable_Object=MibTable
bsDhcpSnoopingVlanTable=_BsDhcpSnoopingVlanTable_Object((1,3,6,1,4,1,45,5,17,1,2))
if mibBuilder.loadTexts:bsDhcpSnoopingVlanTable.setStatus(_A)
_BsDhcpSnoopingVlanEntry_Object=MibTableRow
bsDhcpSnoopingVlanEntry=_BsDhcpSnoopingVlanEntry_Object((1,3,6,1,4,1,45,5,17,1,2,1))
bsDhcpSnoopingVlanEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:bsDhcpSnoopingVlanEntry.setStatus(_A)
_BsDhcpSnoopingVlanId_Type=VlanIndex
_BsDhcpSnoopingVlanId_Object=MibTableColumn
bsDhcpSnoopingVlanId=_BsDhcpSnoopingVlanId_Object((1,3,6,1,4,1,45,5,17,1,2,1,1),_BsDhcpSnoopingVlanId_Type())
bsDhcpSnoopingVlanId.setMaxAccess(_N)
if mibBuilder.loadTexts:bsDhcpSnoopingVlanId.setStatus(_A)
_BsDhcpSnoopingVlanEnabled_Type=TruthValue
_BsDhcpSnoopingVlanEnabled_Object=MibTableColumn
bsDhcpSnoopingVlanEnabled=_BsDhcpSnoopingVlanEnabled_Object((1,3,6,1,4,1,45,5,17,1,2,1,2),_BsDhcpSnoopingVlanEnabled_Type())
bsDhcpSnoopingVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingVlanEnabled.setStatus(_A)
_BsDhcpSnoopingVlanOption82Enabled_Type=TruthValue
_BsDhcpSnoopingVlanOption82Enabled_Object=MibTableColumn
bsDhcpSnoopingVlanOption82Enabled=_BsDhcpSnoopingVlanOption82Enabled_Object((1,3,6,1,4,1,45,5,17,1,2,1,3),_BsDhcpSnoopingVlanOption82Enabled_Type())
bsDhcpSnoopingVlanOption82Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingVlanOption82Enabled.setStatus(_A)
class _BsDhcpSnoopingOrigin_Type(Bits):namedValues=NamedValues(*(('config',0),('radius',1)))
_BsDhcpSnoopingOrigin_Type.__name__='Bits'
_BsDhcpSnoopingOrigin_Object=MibTableColumn
bsDhcpSnoopingOrigin=_BsDhcpSnoopingOrigin_Object((1,3,6,1,4,1,45,5,17,1,2,1,4),_BsDhcpSnoopingOrigin_Type())
bsDhcpSnoopingOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:bsDhcpSnoopingOrigin.setStatus(_A)
_BsDhcpSnoopingIfTable_Object=MibTable
bsDhcpSnoopingIfTable=_BsDhcpSnoopingIfTable_Object((1,3,6,1,4,1,45,5,17,1,3))
if mibBuilder.loadTexts:bsDhcpSnoopingIfTable.setStatus(_A)
_BsDhcpSnoopingIfEntry_Object=MibTableRow
bsDhcpSnoopingIfEntry=_BsDhcpSnoopingIfEntry_Object((1,3,6,1,4,1,45,5,17,1,3,1))
bsDhcpSnoopingIfEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:bsDhcpSnoopingIfEntry.setStatus(_A)
_BsDhcpSnoopingIfIndex_Type=InterfaceIndex
_BsDhcpSnoopingIfIndex_Object=MibTableColumn
bsDhcpSnoopingIfIndex=_BsDhcpSnoopingIfIndex_Object((1,3,6,1,4,1,45,5,17,1,3,1,1),_BsDhcpSnoopingIfIndex_Type())
bsDhcpSnoopingIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:bsDhcpSnoopingIfIndex.setStatus(_A)
_BsDhcpSnoopingIfTrusted_Type=TruthValue
_BsDhcpSnoopingIfTrusted_Object=MibTableColumn
bsDhcpSnoopingIfTrusted=_BsDhcpSnoopingIfTrusted_Object((1,3,6,1,4,1,45,5,17,1,3,1,2),_BsDhcpSnoopingIfTrusted_Type())
bsDhcpSnoopingIfTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingIfTrusted.setStatus(_A)
_BsDhcpSnoopingIfOption82SubscriberId_Type=DisplayString
_BsDhcpSnoopingIfOption82SubscriberId_Object=MibTableColumn
bsDhcpSnoopingIfOption82SubscriberId=_BsDhcpSnoopingIfOption82SubscriberId_Object((1,3,6,1,4,1,45,5,17,1,3,1,3),_BsDhcpSnoopingIfOption82SubscriberId_Type())
bsDhcpSnoopingIfOption82SubscriberId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingIfOption82SubscriberId.setStatus(_A)
_BsDhcpSnoopingBindingTable_Object=MibTable
bsDhcpSnoopingBindingTable=_BsDhcpSnoopingBindingTable_Object((1,3,6,1,4,1,45,5,17,1,4))
if mibBuilder.loadTexts:bsDhcpSnoopingBindingTable.setStatus(_A)
_BsDhcpSnoopingBindingEntry_Object=MibTableRow
bsDhcpSnoopingBindingEntry=_BsDhcpSnoopingBindingEntry_Object((1,3,6,1,4,1,45,5,17,1,4,1))
bsDhcpSnoopingBindingEntry.setIndexNames((0,_B,_P),(0,_B,_W))
if mibBuilder.loadTexts:bsDhcpSnoopingBindingEntry.setStatus(_A)
_BsDhcpSnoopingBindingVlanId_Type=VlanIndex
_BsDhcpSnoopingBindingVlanId_Object=MibTableColumn
bsDhcpSnoopingBindingVlanId=_BsDhcpSnoopingBindingVlanId_Object((1,3,6,1,4,1,45,5,17,1,4,1,1),_BsDhcpSnoopingBindingVlanId_Type())
bsDhcpSnoopingBindingVlanId.setMaxAccess(_N)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingVlanId.setStatus(_A)
_BsDhcpSnoopingBindingMacAddress_Type=MacAddress
_BsDhcpSnoopingBindingMacAddress_Object=MibTableColumn
bsDhcpSnoopingBindingMacAddress=_BsDhcpSnoopingBindingMacAddress_Object((1,3,6,1,4,1,45,5,17,1,4,1,2),_BsDhcpSnoopingBindingMacAddress_Type())
bsDhcpSnoopingBindingMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingMacAddress.setStatus(_A)
_BsDhcpSnoopingBindingAddressType_Type=InetAddressType
_BsDhcpSnoopingBindingAddressType_Object=MibTableColumn
bsDhcpSnoopingBindingAddressType=_BsDhcpSnoopingBindingAddressType_Object((1,3,6,1,4,1,45,5,17,1,4,1,3),_BsDhcpSnoopingBindingAddressType_Type())
bsDhcpSnoopingBindingAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingAddressType.setStatus(_A)
_BsDhcpSnoopingBindingAddress_Type=InetAddress
_BsDhcpSnoopingBindingAddress_Object=MibTableColumn
bsDhcpSnoopingBindingAddress=_BsDhcpSnoopingBindingAddress_Object((1,3,6,1,4,1,45,5,17,1,4,1,4),_BsDhcpSnoopingBindingAddress_Type())
bsDhcpSnoopingBindingAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingAddress.setStatus(_A)
_BsDhcpSnoopingBindingInterface_Type=InterfaceIndex
_BsDhcpSnoopingBindingInterface_Object=MibTableColumn
bsDhcpSnoopingBindingInterface=_BsDhcpSnoopingBindingInterface_Object((1,3,6,1,4,1,45,5,17,1,4,1,5),_BsDhcpSnoopingBindingInterface_Type())
bsDhcpSnoopingBindingInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingInterface.setStatus(_A)
_BsDhcpSnoopingBindingLeaseTime_Type=Unsigned32
_BsDhcpSnoopingBindingLeaseTime_Object=MibTableColumn
bsDhcpSnoopingBindingLeaseTime=_BsDhcpSnoopingBindingLeaseTime_Object((1,3,6,1,4,1,45,5,17,1,4,1,6),_BsDhcpSnoopingBindingLeaseTime_Type())
bsDhcpSnoopingBindingLeaseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingLeaseTime.setUnits(_X)
_BsDhcpSnoopingBindingRowStatus_Type=RowStatus
_BsDhcpSnoopingBindingRowStatus_Object=MibTableColumn
bsDhcpSnoopingBindingRowStatus=_BsDhcpSnoopingBindingRowStatus_Object((1,3,6,1,4,1,45,5,17,1,4,1,7),_BsDhcpSnoopingBindingRowStatus_Type())
bsDhcpSnoopingBindingRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingRowStatus.setStatus(_A)
_BsDhcpSnoopingBindingTimeToExpiry_Type=Unsigned32
_BsDhcpSnoopingBindingTimeToExpiry_Object=MibTableColumn
bsDhcpSnoopingBindingTimeToExpiry=_BsDhcpSnoopingBindingTimeToExpiry_Object((1,3,6,1,4,1,45,5,17,1,4,1,8),_BsDhcpSnoopingBindingTimeToExpiry_Type())
bsDhcpSnoopingBindingTimeToExpiry.setMaxAccess(_E)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingTimeToExpiry.setStatus(_A)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingTimeToExpiry.setUnits(_X)
class _BsDhcpSnoopingBindingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('learned',1),('static',2)))
_BsDhcpSnoopingBindingSource_Type.__name__=_M
_BsDhcpSnoopingBindingSource_Object=MibTableColumn
bsDhcpSnoopingBindingSource=_BsDhcpSnoopingBindingSource_Object((1,3,6,1,4,1,45,5,17,1,4,1,9),_BsDhcpSnoopingBindingSource_Type())
bsDhcpSnoopingBindingSource.setMaxAccess(_E)
if mibBuilder.loadTexts:bsDhcpSnoopingBindingSource.setStatus(_A)
_BsDhcpSnoopingNotificationObjects_ObjectIdentity=ObjectIdentity
bsDhcpSnoopingNotificationObjects=_BsDhcpSnoopingNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,17,1,5))
class _BsDhcpSnoopingNotificationSourcePort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BsDhcpSnoopingNotificationSourcePort_Type.__name__=_T
_BsDhcpSnoopingNotificationSourcePort_Object=MibScalar
bsDhcpSnoopingNotificationSourcePort=_BsDhcpSnoopingNotificationSourcePort_Object((1,3,6,1,4,1,45,5,17,1,5,1),_BsDhcpSnoopingNotificationSourcePort_Type())
bsDhcpSnoopingNotificationSourcePort.setMaxAccess(_G)
if mibBuilder.loadTexts:bsDhcpSnoopingNotificationSourcePort.setStatus(_A)
class _BsDhcpSnoopingNotificationMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('dhcpDiscover',1),('dhcpOffer',2),('dhcpRequest',3),('dhcpDecline',4),('dhcpAck',5),('dhcpNak',6),('dhcpRelease',7),('dhcpInform',8),('dhcpForceRenew',9),('dhcpLeaseQuery',10),('dhcpLeaseUnassigned',11),('dhcpLeaseUnknown',12),('dhcpLeaseActive',13)))
_BsDhcpSnoopingNotificationMsgType_Type.__name__=_M
_BsDhcpSnoopingNotificationMsgType_Object=MibScalar
bsDhcpSnoopingNotificationMsgType=_BsDhcpSnoopingNotificationMsgType_Object((1,3,6,1,4,1,45,5,17,1,5,2),_BsDhcpSnoopingNotificationMsgType_Type())
bsDhcpSnoopingNotificationMsgType.setMaxAccess(_G)
if mibBuilder.loadTexts:bsDhcpSnoopingNotificationMsgType.setStatus(_A)
_BsDhcpSnoopingNotificationSourceMACAddr_Type=MacAddress
_BsDhcpSnoopingNotificationSourceMACAddr_Object=MibScalar
bsDhcpSnoopingNotificationSourceMACAddr=_BsDhcpSnoopingNotificationSourceMACAddr_Object((1,3,6,1,4,1,45,5,17,1,5,3),_BsDhcpSnoopingNotificationSourceMACAddr_Type())
bsDhcpSnoopingNotificationSourceMACAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:bsDhcpSnoopingNotificationSourceMACAddr.setStatus(_A)
_BsDhcpSnoopingNotificationClientMACAddr_Type=MacAddress
_BsDhcpSnoopingNotificationClientMACAddr_Object=MibScalar
bsDhcpSnoopingNotificationClientMACAddr=_BsDhcpSnoopingNotificationClientMACAddr_Object((1,3,6,1,4,1,45,5,17,1,5,4),_BsDhcpSnoopingNotificationClientMACAddr_Type())
bsDhcpSnoopingNotificationClientMACAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:bsDhcpSnoopingNotificationClientMACAddr.setStatus(_A)
_BsDhcpSnoopingNotificationsBindingMacAddress_Type=MacAddress
_BsDhcpSnoopingNotificationsBindingMacAddress_Object=MibScalar
bsDhcpSnoopingNotificationsBindingMacAddress=_BsDhcpSnoopingNotificationsBindingMacAddress_Object((1,3,6,1,4,1,45,5,17,1,5,5),_BsDhcpSnoopingNotificationsBindingMacAddress_Type())
bsDhcpSnoopingNotificationsBindingMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:bsDhcpSnoopingNotificationsBindingMacAddress.setStatus(_A)
_BsDhcpSnoopingExtSave_ObjectIdentity=ObjectIdentity
bsDhcpSnoopingExtSave=_BsDhcpSnoopingExtSave_ObjectIdentity((1,3,6,1,4,1,45,5,17,1,6))
_BsDhcpSnoopingExtSaveEnabled_Type=TruthValue
_BsDhcpSnoopingExtSaveEnabled_Object=MibScalar
bsDhcpSnoopingExtSaveEnabled=_BsDhcpSnoopingExtSaveEnabled_Object((1,3,6,1,4,1,45,5,17,1,6,1),_BsDhcpSnoopingExtSaveEnabled_Type())
bsDhcpSnoopingExtSaveEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEnabled.setStatus(_A)
_BsDhcpSnoopingExtSaveLastSyncTime_Type=DateAndTime
_BsDhcpSnoopingExtSaveLastSyncTime_Object=MibScalar
bsDhcpSnoopingExtSaveLastSyncTime=_BsDhcpSnoopingExtSaveLastSyncTime_Object((1,3,6,1,4,1,45,5,17,1,6,2),_BsDhcpSnoopingExtSaveLastSyncTime_Type())
bsDhcpSnoopingExtSaveLastSyncTime.setMaxAccess(_E)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveLastSyncTime.setStatus(_A)
_BsDhcpSnoopingExtSaveSyncFlag_Type=TruthValue
_BsDhcpSnoopingExtSaveSyncFlag_Object=MibScalar
bsDhcpSnoopingExtSaveSyncFlag=_BsDhcpSnoopingExtSaveSyncFlag_Object((1,3,6,1,4,1,45,5,17,1,6,3),_BsDhcpSnoopingExtSaveSyncFlag_Type())
bsDhcpSnoopingExtSaveSyncFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSyncFlag.setStatus(_A)
class _BsDhcpSnoopingExtSaveFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BsDhcpSnoopingExtSaveFilename_Type.__name__=_U
_BsDhcpSnoopingExtSaveFilename_Object=MibScalar
bsDhcpSnoopingExtSaveFilename=_BsDhcpSnoopingExtSaveFilename_Object((1,3,6,1,4,1,45,5,17,1,6,4),_BsDhcpSnoopingExtSaveFilename_Type())
bsDhcpSnoopingExtSaveFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveFilename.setStatus(_A)
_BsDhcpSnoopingExtSaveTftpServerAddressType_Type=InetAddressType
_BsDhcpSnoopingExtSaveTftpServerAddressType_Object=MibScalar
bsDhcpSnoopingExtSaveTftpServerAddressType=_BsDhcpSnoopingExtSaveTftpServerAddressType_Object((1,3,6,1,4,1,45,5,17,1,6,5),_BsDhcpSnoopingExtSaveTftpServerAddressType_Type())
bsDhcpSnoopingExtSaveTftpServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTftpServerAddressType.setStatus(_A)
_BsDhcpSnoopingExtSaveTftpServerAddress_Type=InetAddress
_BsDhcpSnoopingExtSaveTftpServerAddress_Object=MibScalar
bsDhcpSnoopingExtSaveTftpServerAddress=_BsDhcpSnoopingExtSaveTftpServerAddress_Object((1,3,6,1,4,1,45,5,17,1,6,6),_BsDhcpSnoopingExtSaveTftpServerAddress_Type())
bsDhcpSnoopingExtSaveTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTftpServerAddress.setStatus(_A)
class _BsDhcpSnoopingExtSaveUsbTargetUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_BsDhcpSnoopingExtSaveUsbTargetUnit_Type.__name__=_M
_BsDhcpSnoopingExtSaveUsbTargetUnit_Object=MibScalar
bsDhcpSnoopingExtSaveUsbTargetUnit=_BsDhcpSnoopingExtSaveUsbTargetUnit_Object((1,3,6,1,4,1,45,5,17,1,6,7),_BsDhcpSnoopingExtSaveUsbTargetUnit_Type())
bsDhcpSnoopingExtSaveUsbTargetUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveUsbTargetUnit.setStatus(_A)
_BsDhcpSnoopingExtSaveForceRestore_Type=Integer32
_BsDhcpSnoopingExtSaveForceRestore_Object=MibScalar
bsDhcpSnoopingExtSaveForceRestore=_BsDhcpSnoopingExtSaveForceRestore_Object((1,3,6,1,4,1,45,5,17,1,6,8),_BsDhcpSnoopingExtSaveForceRestore_Type())
bsDhcpSnoopingExtSaveForceRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveForceRestore.setStatus(_A)
_BsDhcpSnoopingExtSaveSftpServerAddressType_Type=InetAddressType
_BsDhcpSnoopingExtSaveSftpServerAddressType_Object=MibScalar
bsDhcpSnoopingExtSaveSftpServerAddressType=_BsDhcpSnoopingExtSaveSftpServerAddressType_Object((1,3,6,1,4,1,45,5,17,1,6,9),_BsDhcpSnoopingExtSaveSftpServerAddressType_Type())
bsDhcpSnoopingExtSaveSftpServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSftpServerAddressType.setStatus(_A)
_BsDhcpSnoopingExtSaveSftpServerAddress_Type=InetAddress
_BsDhcpSnoopingExtSaveSftpServerAddress_Object=MibScalar
bsDhcpSnoopingExtSaveSftpServerAddress=_BsDhcpSnoopingExtSaveSftpServerAddress_Object((1,3,6,1,4,1,45,5,17,1,6,10),_BsDhcpSnoopingExtSaveSftpServerAddress_Type())
bsDhcpSnoopingExtSaveSftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSftpServerAddress.setStatus(_A)
bsDhcpSnoopingBindingTableFull=NotificationType((1,3,6,1,4,1,45,5,17,0,1))
bsDhcpSnoopingBindingTableFull.setObjects((_B,_Q))
if mibBuilder.loadTexts:bsDhcpSnoopingBindingTableFull.setStatus(_A)
bsDhcpSnoopingTrap=NotificationType((1,3,6,1,4,1,45,5,17,0,2))
bsDhcpSnoopingTrap.setObjects(*((_B,_Y),(_B,_Z),(_B,_R),(_B,_Q),(_B,_S)))
if mibBuilder.loadTexts:bsDhcpSnoopingTrap.setStatus(_A)
bsDhcpOption82MaxLengthExceeded=NotificationType((1,3,6,1,4,1,45,5,17,0,3))
if mibBuilder.loadTexts:bsDhcpOption82MaxLengthExceeded.setStatus(_A)
bsDhcpSnoopingExtSaveEntryMACConflict=NotificationType((1,3,6,1,4,1,45,5,17,0,4))
bsDhcpSnoopingExtSaveEntryMACConflict.setObjects((_B,_D))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryMACConflict.setStatus(_A)
bsDhcpSnoopingExtSaveEntryInvalidInterface=NotificationType((1,3,6,1,4,1,45,5,17,0,5))
bsDhcpSnoopingExtSaveEntryInvalidInterface.setObjects(*((_B,_D),(_B,_a)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryInvalidInterface.setStatus(_A)
bsDhcpSnoopingExtSaveEntryLeaseExpired=NotificationType((1,3,6,1,4,1,45,5,17,0,6))
bsDhcpSnoopingExtSaveEntryLeaseExpired.setObjects((_B,_D))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryLeaseExpired.setStatus(_A)
bsDhcpSnoopingExtSaveEntryParsingFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,7))
bsDhcpSnoopingExtSaveEntryParsingFailure.setObjects((_B,_D))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryParsingFailure.setStatus(_A)
bsDhcpSnoopingExtSaveNTP=NotificationType((1,3,6,1,4,1,45,5,17,0,8))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveNTP.setStatus(_A)
bsDhcpSnoopingExtSaveUSBSyncSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,9))
bsDhcpSnoopingExtSaveUSBSyncSuccess.setObjects((_B,_H))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveUSBSyncSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveTFTPSyncSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,10))
bsDhcpSnoopingExtSaveTFTPSyncSuccess.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTFTPSyncSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveUSBSyncFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,11))
bsDhcpSnoopingExtSaveUSBSyncFailure.setObjects((_B,_H))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveUSBSyncFailure.setStatus(_A)
bsDhcpSnoopingExtSaveTFTPSyncFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,12))
bsDhcpSnoopingExtSaveTFTPSyncFailure.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTFTPSyncFailure.setStatus(_A)
bsDhcpSnoopingExtSaveUSBRestoreSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,13))
bsDhcpSnoopingExtSaveUSBRestoreSuccess.setObjects((_B,_H))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveUSBRestoreSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveTFTPRestoreSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,14))
bsDhcpSnoopingExtSaveTFTPRestoreSuccess.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTFTPRestoreSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveUSBRestoreFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,15))
bsDhcpSnoopingExtSaveUSBRestoreFailure.setObjects((_B,_H))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveUSBRestoreFailure.setStatus(_A)
bsDhcpSnoopingExtSaveTFTPRestoreFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,16))
bsDhcpSnoopingExtSaveTFTPRestoreFailure.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveTFTPRestoreFailure.setStatus(_A)
bsDhcpSnoopingExtSaveEntryInvalidVlan=NotificationType((1,3,6,1,4,1,45,5,17,0,17))
bsDhcpSnoopingExtSaveEntryInvalidVlan.setObjects(*((_B,_D),(_B,_P)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryInvalidVlan.setStatus(_A)
bsDhcpSnoopingExtSaveSFTPSyncSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,18))
bsDhcpSnoopingExtSaveSFTPSyncSuccess.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSFTPSyncSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveSFTPSyncFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,19))
bsDhcpSnoopingExtSaveSFTPSyncFailure.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSFTPSyncFailure.setStatus(_A)
bsDhcpSnoopingExtSaveSFTPRestoreSuccess=NotificationType((1,3,6,1,4,1,45,5,17,0,20))
bsDhcpSnoopingExtSaveSFTPRestoreSuccess.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSFTPRestoreSuccess.setStatus(_A)
bsDhcpSnoopingExtSaveSFTPRestoreFailure=NotificationType((1,3,6,1,4,1,45,5,17,0,21))
bsDhcpSnoopingExtSaveSFTPRestoreFailure.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveSFTPRestoreFailure.setStatus(_A)
bsDhcpSnoopingExtSaveEntryIfTrustedConflict=NotificationType((1,3,6,1,4,1,45,5,17,0,22))
bsDhcpSnoopingExtSaveEntryIfTrustedConflict.setObjects(*((_B,_D),(_B,_S)))
if mibBuilder.loadTexts:bsDhcpSnoopingExtSaveEntryIfTrustedConflict.setStatus(_A)
bsDhcpSnoopingStaticEntryMACConflict=NotificationType((1,3,6,1,4,1,45,5,17,0,23))
bsDhcpSnoopingStaticEntryMACConflict.setObjects(*((_B,_R),(_B,_O)))
if mibBuilder.loadTexts:bsDhcpSnoopingStaticEntryMACConflict.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackDhcpSnoopingMib':bayStackDhcpSnoopingMib,'bsDhcpSnoopingNotifications':bsDhcpSnoopingNotifications,'bsDhcpSnoopingBindingTableFull':bsDhcpSnoopingBindingTableFull,'bsDhcpSnoopingTrap':bsDhcpSnoopingTrap,'bsDhcpOption82MaxLengthExceeded':bsDhcpOption82MaxLengthExceeded,'bsDhcpSnoopingExtSaveEntryMACConflict':bsDhcpSnoopingExtSaveEntryMACConflict,'bsDhcpSnoopingExtSaveEntryInvalidInterface':bsDhcpSnoopingExtSaveEntryInvalidInterface,'bsDhcpSnoopingExtSaveEntryLeaseExpired':bsDhcpSnoopingExtSaveEntryLeaseExpired,'bsDhcpSnoopingExtSaveEntryParsingFailure':bsDhcpSnoopingExtSaveEntryParsingFailure,'bsDhcpSnoopingExtSaveNTP':bsDhcpSnoopingExtSaveNTP,'bsDhcpSnoopingExtSaveUSBSyncSuccess':bsDhcpSnoopingExtSaveUSBSyncSuccess,'bsDhcpSnoopingExtSaveTFTPSyncSuccess':bsDhcpSnoopingExtSaveTFTPSyncSuccess,'bsDhcpSnoopingExtSaveUSBSyncFailure':bsDhcpSnoopingExtSaveUSBSyncFailure,'bsDhcpSnoopingExtSaveTFTPSyncFailure':bsDhcpSnoopingExtSaveTFTPSyncFailure,'bsDhcpSnoopingExtSaveUSBRestoreSuccess':bsDhcpSnoopingExtSaveUSBRestoreSuccess,'bsDhcpSnoopingExtSaveTFTPRestoreSuccess':bsDhcpSnoopingExtSaveTFTPRestoreSuccess,'bsDhcpSnoopingExtSaveUSBRestoreFailure':bsDhcpSnoopingExtSaveUSBRestoreFailure,'bsDhcpSnoopingExtSaveTFTPRestoreFailure':bsDhcpSnoopingExtSaveTFTPRestoreFailure,'bsDhcpSnoopingExtSaveEntryInvalidVlan':bsDhcpSnoopingExtSaveEntryInvalidVlan,'bsDhcpSnoopingExtSaveSFTPSyncSuccess':bsDhcpSnoopingExtSaveSFTPSyncSuccess,'bsDhcpSnoopingExtSaveSFTPSyncFailure':bsDhcpSnoopingExtSaveSFTPSyncFailure,'bsDhcpSnoopingExtSaveSFTPRestoreSuccess':bsDhcpSnoopingExtSaveSFTPRestoreSuccess,'bsDhcpSnoopingExtSaveSFTPRestoreFailure':bsDhcpSnoopingExtSaveSFTPRestoreFailure,'bsDhcpSnoopingExtSaveEntryIfTrustedConflict':bsDhcpSnoopingExtSaveEntryIfTrustedConflict,'bsDhcpSnoopingStaticEntryMACConflict':bsDhcpSnoopingStaticEntryMACConflict,'bsDhcpSnoopingObjects':bsDhcpSnoopingObjects,'bsDhcpSnoopingScalars':bsDhcpSnoopingScalars,'bsDhcpSnoopingEnabled':bsDhcpSnoopingEnabled,'bsDhcpSnoopingOption82Enabled':bsDhcpSnoopingOption82Enabled,'bsDhcpSnoopingVlanTable':bsDhcpSnoopingVlanTable,'bsDhcpSnoopingVlanEntry':bsDhcpSnoopingVlanEntry,_V:bsDhcpSnoopingVlanId,'bsDhcpSnoopingVlanEnabled':bsDhcpSnoopingVlanEnabled,'bsDhcpSnoopingVlanOption82Enabled':bsDhcpSnoopingVlanOption82Enabled,'bsDhcpSnoopingOrigin':bsDhcpSnoopingOrigin,'bsDhcpSnoopingIfTable':bsDhcpSnoopingIfTable,'bsDhcpSnoopingIfEntry':bsDhcpSnoopingIfEntry,_O:bsDhcpSnoopingIfIndex,_S:bsDhcpSnoopingIfTrusted,'bsDhcpSnoopingIfOption82SubscriberId':bsDhcpSnoopingIfOption82SubscriberId,'bsDhcpSnoopingBindingTable':bsDhcpSnoopingBindingTable,'bsDhcpSnoopingBindingEntry':bsDhcpSnoopingBindingEntry,_P:bsDhcpSnoopingBindingVlanId,_W:bsDhcpSnoopingBindingMacAddress,'bsDhcpSnoopingBindingAddressType':bsDhcpSnoopingBindingAddressType,'bsDhcpSnoopingBindingAddress':bsDhcpSnoopingBindingAddress,_a:bsDhcpSnoopingBindingInterface,'bsDhcpSnoopingBindingLeaseTime':bsDhcpSnoopingBindingLeaseTime,'bsDhcpSnoopingBindingRowStatus':bsDhcpSnoopingBindingRowStatus,'bsDhcpSnoopingBindingTimeToExpiry':bsDhcpSnoopingBindingTimeToExpiry,'bsDhcpSnoopingBindingSource':bsDhcpSnoopingBindingSource,'bsDhcpSnoopingNotificationObjects':bsDhcpSnoopingNotificationObjects,_Y:bsDhcpSnoopingNotificationSourcePort,_Z:bsDhcpSnoopingNotificationMsgType,_R:bsDhcpSnoopingNotificationSourceMACAddr,_Q:bsDhcpSnoopingNotificationClientMACAddr,_D:bsDhcpSnoopingNotificationsBindingMacAddress,'bsDhcpSnoopingExtSave':bsDhcpSnoopingExtSave,'bsDhcpSnoopingExtSaveEnabled':bsDhcpSnoopingExtSaveEnabled,'bsDhcpSnoopingExtSaveLastSyncTime':bsDhcpSnoopingExtSaveLastSyncTime,'bsDhcpSnoopingExtSaveSyncFlag':bsDhcpSnoopingExtSaveSyncFlag,'bsDhcpSnoopingExtSaveFilename':bsDhcpSnoopingExtSaveFilename,_I:bsDhcpSnoopingExtSaveTftpServerAddressType,_J:bsDhcpSnoopingExtSaveTftpServerAddress,_H:bsDhcpSnoopingExtSaveUsbTargetUnit,'bsDhcpSnoopingExtSaveForceRestore':bsDhcpSnoopingExtSaveForceRestore,_K:bsDhcpSnoopingExtSaveSftpServerAddressType,_L:bsDhcpSnoopingExtSaveSftpServerAddress})