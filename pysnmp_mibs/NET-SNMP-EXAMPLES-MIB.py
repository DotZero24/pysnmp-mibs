_M='netSnmpExampleHeartbeatRate'
_L='netSnmpHostName'
_K='not-accessible'
_J='nsIETFWGName'
_I='StorageType'
_H='SnmpAdminString'
_G='accessible-for-notify'
_F='read-write'
_E='Integer32'
_D='OctetString'
_C='NET-SNMP-EXAMPLES-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
netSnmp,=mibBuilder.importSymbols('NET-SNMP-MIB','netSnmp')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention')
netSnmpExamples=ModuleIdentity((1,3,6,1,4,1,8072,2))
if mibBuilder.loadTexts:netSnmpExamples.setRevisions(('2004-06-15 00:00','2002-02-06 00:00'))
_NetSnmpExampleScalars_ObjectIdentity=ObjectIdentity
netSnmpExampleScalars=_NetSnmpExampleScalars_ObjectIdentity((1,3,6,1,4,1,8072,2,1))
class _NetSnmpExampleInteger_Type(Integer32):defaultValue=42
_NetSnmpExampleInteger_Type.__name__=_E
_NetSnmpExampleInteger_Object=MibScalar
netSnmpExampleInteger=_NetSnmpExampleInteger_Object((1,3,6,1,4,1,8072,2,1,1),_NetSnmpExampleInteger_Type())
netSnmpExampleInteger.setMaxAccess(_F)
if mibBuilder.loadTexts:netSnmpExampleInteger.setStatus(_A)
class _NetSnmpExampleSleeper_Type(Integer32):defaultValue=1
_NetSnmpExampleSleeper_Type.__name__=_E
_NetSnmpExampleSleeper_Object=MibScalar
netSnmpExampleSleeper=_NetSnmpExampleSleeper_Object((1,3,6,1,4,1,8072,2,1,2),_NetSnmpExampleSleeper_Type())
netSnmpExampleSleeper.setMaxAccess(_F)
if mibBuilder.loadTexts:netSnmpExampleSleeper.setStatus(_A)
class _NetSnmpExampleString_Type(SnmpAdminString):defaultValue=OctetString('So long, and thanks for all the fish!')
_NetSnmpExampleString_Type.__name__=_H
_NetSnmpExampleString_Object=MibScalar
netSnmpExampleString=_NetSnmpExampleString_Object((1,3,6,1,4,1,8072,2,1,3),_NetSnmpExampleString_Type())
netSnmpExampleString.setMaxAccess(_F)
if mibBuilder.loadTexts:netSnmpExampleString.setStatus(_A)
_NetSnmpExampleTables_ObjectIdentity=ObjectIdentity
netSnmpExampleTables=_NetSnmpExampleTables_ObjectIdentity((1,3,6,1,4,1,8072,2,2))
_NetSnmpIETFWGTable_Object=MibTable
netSnmpIETFWGTable=_NetSnmpIETFWGTable_Object((1,3,6,1,4,1,8072,2,2,1))
if mibBuilder.loadTexts:netSnmpIETFWGTable.setStatus(_A)
_NetSnmpIETFWGEntry_Object=MibTableRow
netSnmpIETFWGEntry=_NetSnmpIETFWGEntry_Object((1,3,6,1,4,1,8072,2,2,1,1))
netSnmpIETFWGEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:netSnmpIETFWGEntry.setStatus(_A)
class _NsIETFWGName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NsIETFWGName_Type.__name__=_D
_NsIETFWGName_Object=MibTableColumn
nsIETFWGName=_NsIETFWGName_Object((1,3,6,1,4,1,8072,2,2,1,1,1),_NsIETFWGName_Type())
nsIETFWGName.setMaxAccess(_K)
if mibBuilder.loadTexts:nsIETFWGName.setStatus(_A)
_NsIETFWGChair1_Type=OctetString
_NsIETFWGChair1_Object=MibTableColumn
nsIETFWGChair1=_NsIETFWGChair1_Object((1,3,6,1,4,1,8072,2,2,1,1,2),_NsIETFWGChair1_Type())
nsIETFWGChair1.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIETFWGChair1.setStatus(_A)
_NsIETFWGChair2_Type=OctetString
_NsIETFWGChair2_Object=MibTableColumn
nsIETFWGChair2=_NsIETFWGChair2_Object((1,3,6,1,4,1,8072,2,2,1,1,3),_NsIETFWGChair2_Type())
nsIETFWGChair2.setMaxAccess(_B)
if mibBuilder.loadTexts:nsIETFWGChair2.setStatus(_A)
_NetSnmpHostsTable_Object=MibTable
netSnmpHostsTable=_NetSnmpHostsTable_Object((1,3,6,1,4,1,8072,2,2,2))
if mibBuilder.loadTexts:netSnmpHostsTable.setStatus(_A)
_NetSnmpHostsEntry_Object=MibTableRow
netSnmpHostsEntry=_NetSnmpHostsEntry_Object((1,3,6,1,4,1,8072,2,2,2,1))
netSnmpHostsEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:netSnmpHostsEntry.setStatus(_A)
class _NetSnmpHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NetSnmpHostName_Type.__name__=_D
_NetSnmpHostName_Object=MibTableColumn
netSnmpHostName=_NetSnmpHostName_Object((1,3,6,1,4,1,8072,2,2,2,1,1),_NetSnmpHostName_Type())
netSnmpHostName.setMaxAccess(_K)
if mibBuilder.loadTexts:netSnmpHostName.setStatus(_A)
_NetSnmpHostAddressType_Type=InetAddressType
_NetSnmpHostAddressType_Object=MibTableColumn
netSnmpHostAddressType=_NetSnmpHostAddressType_Object((1,3,6,1,4,1,8072,2,2,2,1,2),_NetSnmpHostAddressType_Type())
netSnmpHostAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpHostAddressType.setStatus(_A)
_NetSnmpHostAddress_Type=InetAddress
_NetSnmpHostAddress_Object=MibTableColumn
netSnmpHostAddress=_NetSnmpHostAddress_Object((1,3,6,1,4,1,8072,2,2,2,1,3),_NetSnmpHostAddress_Type())
netSnmpHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpHostAddress.setStatus(_A)
class _NetSnmpHostStorage_Type(StorageType):defaultValue=3
_NetSnmpHostStorage_Type.__name__=_I
_NetSnmpHostStorage_Object=MibTableColumn
netSnmpHostStorage=_NetSnmpHostStorage_Object((1,3,6,1,4,1,8072,2,2,2,1,4),_NetSnmpHostStorage_Type())
netSnmpHostStorage.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpHostStorage.setStatus(_A)
_NetSnmpHostRowStatus_Type=RowStatus
_NetSnmpHostRowStatus_Object=MibTableColumn
netSnmpHostRowStatus=_NetSnmpHostRowStatus_Object((1,3,6,1,4,1,8072,2,2,2,1,5),_NetSnmpHostRowStatus_Type())
netSnmpHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:netSnmpHostRowStatus.setStatus(_A)
_NetSnmpExampleNotifications_ObjectIdentity=ObjectIdentity
netSnmpExampleNotifications=_NetSnmpExampleNotifications_ObjectIdentity((1,3,6,1,4,1,8072,2,3))
_NetSnmpExampleNotificationPrefix_ObjectIdentity=ObjectIdentity
netSnmpExampleNotificationPrefix=_NetSnmpExampleNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8072,2,3,0))
_NetSnmpExampleNotification_Type=SnmpAdminString
_NetSnmpExampleNotification_Object=MibScalar
netSnmpExampleNotification=_NetSnmpExampleNotification_Object((1,3,6,1,4,1,8072,2,3,1),_NetSnmpExampleNotification_Type())
netSnmpExampleNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:netSnmpExampleNotification.setStatus('obsolete')
_NetSnmpExampleNotificationObjects_ObjectIdentity=ObjectIdentity
netSnmpExampleNotificationObjects=_NetSnmpExampleNotificationObjects_ObjectIdentity((1,3,6,1,4,1,8072,2,3,2))
_NetSnmpExampleHeartbeatRate_Type=Integer32
_NetSnmpExampleHeartbeatRate_Object=MibScalar
netSnmpExampleHeartbeatRate=_NetSnmpExampleHeartbeatRate_Object((1,3,6,1,4,1,8072,2,3,2,1),_NetSnmpExampleHeartbeatRate_Type())
netSnmpExampleHeartbeatRate.setMaxAccess(_G)
if mibBuilder.loadTexts:netSnmpExampleHeartbeatRate.setStatus(_A)
_NetSnmpExampleHeartbeatName_Type=SnmpAdminString
_NetSnmpExampleHeartbeatName_Object=MibScalar
netSnmpExampleHeartbeatName=_NetSnmpExampleHeartbeatName_Object((1,3,6,1,4,1,8072,2,3,2,2),_NetSnmpExampleHeartbeatName_Type())
netSnmpExampleHeartbeatName.setMaxAccess(_G)
if mibBuilder.loadTexts:netSnmpExampleHeartbeatName.setStatus(_A)
netSnmpExampleHeartbeatNotification=NotificationType((1,3,6,1,4,1,8072,2,3,0,1))
netSnmpExampleHeartbeatNotification.setObjects((_C,_M))
if mibBuilder.loadTexts:netSnmpExampleHeartbeatNotification.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'netSnmpExamples':netSnmpExamples,'netSnmpExampleScalars':netSnmpExampleScalars,'netSnmpExampleInteger':netSnmpExampleInteger,'netSnmpExampleSleeper':netSnmpExampleSleeper,'netSnmpExampleString':netSnmpExampleString,'netSnmpExampleTables':netSnmpExampleTables,'netSnmpIETFWGTable':netSnmpIETFWGTable,'netSnmpIETFWGEntry':netSnmpIETFWGEntry,_J:nsIETFWGName,'nsIETFWGChair1':nsIETFWGChair1,'nsIETFWGChair2':nsIETFWGChair2,'netSnmpHostsTable':netSnmpHostsTable,'netSnmpHostsEntry':netSnmpHostsEntry,_L:netSnmpHostName,'netSnmpHostAddressType':netSnmpHostAddressType,'netSnmpHostAddress':netSnmpHostAddress,'netSnmpHostStorage':netSnmpHostStorage,'netSnmpHostRowStatus':netSnmpHostRowStatus,'netSnmpExampleNotifications':netSnmpExampleNotifications,'netSnmpExampleNotificationPrefix':netSnmpExampleNotificationPrefix,'netSnmpExampleHeartbeatNotification':netSnmpExampleHeartbeatNotification,'netSnmpExampleNotification':netSnmpExampleNotification,'netSnmpExampleNotificationObjects':netSnmpExampleNotificationObjects,_M:netSnmpExampleHeartbeatRate,'netSnmpExampleHeartbeatName':netSnmpExampleHeartbeatName})