_K='apH323StackMaxCallThresholdClearTrap'
_J='apH323StackMaxCallThresholdTrap'
_I='accessible-for-notify'
_H='read-only'
_G='DisplayString'
_F='apH323StackMaxCallsThreshold'
_E='apH323StackMaxCalls'
_D='apH323StackCurrentCalls'
_C='apH323StackName'
_B='current'
_A='APH323-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetVersion','InetZoneIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
apH323Module=ModuleIdentity((1,3,6,1,4,1,9148,3,10))
if mibBuilder.loadTexts:apH323Module.setRevisions(('2012-07-16 00:00',))
_ApH323MIBObjects_ObjectIdentity=ObjectIdentity
apH323MIBObjects=_ApH323MIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,10,1))
_ApH323StackTable_Object=MibTable
apH323StackTable=_ApH323StackTable_Object((1,3,6,1,4,1,9148,3,10,1,1))
if mibBuilder.loadTexts:apH323StackTable.setStatus(_B)
_ApH323StackEntry_Object=MibTableRow
apH323StackEntry=_ApH323StackEntry_Object((1,3,6,1,4,1,9148,3,10,1,1,1))
apH323StackEntry.setIndexNames((1,_A,_C))
if mibBuilder.loadTexts:apH323StackEntry.setStatus(_B)
class _ApH323StackName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApH323StackName_Type.__name__=_G
_ApH323StackName_Object=MibTableColumn
apH323StackName=_ApH323StackName_Object((1,3,6,1,4,1,9148,3,10,1,1,1,1),_ApH323StackName_Type())
apH323StackName.setMaxAccess(_H)
if mibBuilder.loadTexts:apH323StackName.setStatus(_B)
_ApH323StackCurrentCalls_Type=Unsigned32
_ApH323StackCurrentCalls_Object=MibTableColumn
apH323StackCurrentCalls=_ApH323StackCurrentCalls_Object((1,3,6,1,4,1,9148,3,10,1,1,1,2),_ApH323StackCurrentCalls_Type())
apH323StackCurrentCalls.setMaxAccess(_H)
if mibBuilder.loadTexts:apH323StackCurrentCalls.setStatus(_B)
_ApH323NotificationObjects_ObjectIdentity=ObjectIdentity
apH323NotificationObjects=_ApH323NotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,10,2))
_ApH323StackMaxCalls_Type=Unsigned32
_ApH323StackMaxCalls_Object=MibScalar
apH323StackMaxCalls=_ApH323StackMaxCalls_Object((1,3,6,1,4,1,9148,3,10,2,1),_ApH323StackMaxCalls_Type())
apH323StackMaxCalls.setMaxAccess(_I)
if mibBuilder.loadTexts:apH323StackMaxCalls.setStatus(_B)
_ApH323StackMaxCallsThreshold_Type=Unsigned32
_ApH323StackMaxCallsThreshold_Object=MibScalar
apH323StackMaxCallsThreshold=_ApH323StackMaxCallsThreshold_Object((1,3,6,1,4,1,9148,3,10,2,2),_ApH323StackMaxCallsThreshold_Type())
apH323StackMaxCallsThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:apH323StackMaxCallsThreshold.setStatus(_B)
_ApH323NotificationPrefix_ObjectIdentity=ObjectIdentity
apH323NotificationPrefix=_ApH323NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,10,3))
_ApH323Notifications_ObjectIdentity=ObjectIdentity
apH323Notifications=_ApH323Notifications_ObjectIdentity((1,3,6,1,4,1,9148,3,10,3,0))
_ApH323Conformance_ObjectIdentity=ObjectIdentity
apH323Conformance=_ApH323Conformance_ObjectIdentity((1,3,6,1,4,1,9148,3,10,4))
_ApH323Groups_ObjectIdentity=ObjectIdentity
apH323Groups=_ApH323Groups_ObjectIdentity((1,3,6,1,4,1,9148,3,10,4,1))
_ApH323NotificationGroups_ObjectIdentity=ObjectIdentity
apH323NotificationGroups=_ApH323NotificationGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,10,4,2))
apH323StackObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,10,4,1,1))
apH323StackObjectsGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:apH323StackObjectsGroup.setStatus(_B)
apH323StackMaxCallThresholdTrap=NotificationType((1,3,6,1,4,1,9148,3,10,3,0,1))
apH323StackMaxCallThresholdTrap.setObjects(*((_A,_C),(_A,_E),(_A,_F),(_A,_D)))
if mibBuilder.loadTexts:apH323StackMaxCallThresholdTrap.setStatus(_B)
apH323StackMaxCallThresholdClearTrap=NotificationType((1,3,6,1,4,1,9148,3,10,3,0,2))
apH323StackMaxCallThresholdClearTrap.setObjects(*((_A,_C),(_A,_E),(_A,_F),(_A,_D)))
if mibBuilder.loadTexts:apH323StackMaxCallThresholdClearTrap.setStatus(_B)
apH323StackNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,10,4,2,1))
apH323StackNotificationsGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:apH323StackNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apH323Module':apH323Module,'apH323MIBObjects':apH323MIBObjects,'apH323StackTable':apH323StackTable,'apH323StackEntry':apH323StackEntry,_C:apH323StackName,_D:apH323StackCurrentCalls,'apH323NotificationObjects':apH323NotificationObjects,_E:apH323StackMaxCalls,_F:apH323StackMaxCallsThreshold,'apH323NotificationPrefix':apH323NotificationPrefix,'apH323Notifications':apH323Notifications,_J:apH323StackMaxCallThresholdTrap,_K:apH323StackMaxCallThresholdClearTrap,'apH323Conformance':apH323Conformance,'apH323Groups':apH323Groups,'apH323StackObjectsGroup':apH323StackObjectsGroup,'apH323NotificationGroups':apH323NotificationGroups,'apH323StackNotificationsGroup':apH323StackNotificationsGroup})