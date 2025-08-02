_N='oghostNotificationsGroup'
_M='ogHostMibGroup'
_L='oghostEventOccurred'
_K='oghostEventIndex'
_J='Integer32'
_I='oghostEventPort'
_H='oghostEventProtocol'
_G='oghostEventDescription'
_F='oghostEventAddress'
_E='oghostEventType'
_D='oghostEventUsername'
_C='read-only'
_B='current'
_A='OG-HOST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogHostMib=ModuleIdentity((1,3,6,1,4,1,25049,10,14))
if mibBuilder.loadTexts:ogHostMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgHostMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogHostMibNotificationPrefix=_OgHostMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,14,2))
_OghostMibNotifications_ObjectIdentity=ObjectIdentity
oghostMibNotifications=_OghostMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,14,2,0))
_OgHostMibConformance_ObjectIdentity=ObjectIdentity
ogHostMibConformance=_OgHostMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,14,3))
_OgHostMibCompliances_ObjectIdentity=ObjectIdentity
ogHostMibCompliances=_OgHostMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,14,3,1))
_OgHostMibGroups_ObjectIdentity=ObjectIdentity
ogHostMibGroups=_OgHostMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,14,3,2))
_OgHostMibObjects_ObjectIdentity=ObjectIdentity
ogHostMibObjects=_OgHostMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,14,10))
_OghostEvent_ObjectIdentity=ObjectIdentity
oghostEvent=_OghostEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,14,10,1))
_OghostEventTable_Object=MibTable
oghostEventTable=_OghostEventTable_Object((1,3,6,1,4,1,25049,10,14,10,1,1))
if mibBuilder.loadTexts:oghostEventTable.setStatus(_B)
_OghostEventEntry_Object=MibTableRow
oghostEventEntry=_OghostEventEntry_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1))
oghostEventEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:oghostEventEntry.setStatus(_B)
class _OghostEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OghostEventIndex_Type.__name__=_J
_OghostEventIndex_Object=MibTableColumn
oghostEventIndex=_OghostEventIndex_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,1),_OghostEventIndex_Type())
oghostEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oghostEventIndex.setStatus(_B)
_OghostEventUsername_Type=DisplayString
_OghostEventUsername_Object=MibTableColumn
oghostEventUsername=_OghostEventUsername_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,10),_OghostEventUsername_Type())
oghostEventUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventUsername.setStatus(_B)
_OghostEventType_Type=DisplayString
_OghostEventType_Object=MibTableColumn
oghostEventType=_OghostEventType_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,11),_OghostEventType_Type())
oghostEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventType.setStatus(_B)
_OghostEventAddress_Type=DisplayString
_OghostEventAddress_Object=MibTableColumn
oghostEventAddress=_OghostEventAddress_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,12),_OghostEventAddress_Type())
oghostEventAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventAddress.setStatus(_B)
_OghostEventDescription_Type=DisplayString
_OghostEventDescription_Object=MibTableColumn
oghostEventDescription=_OghostEventDescription_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,13),_OghostEventDescription_Type())
oghostEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventDescription.setStatus(_B)
_OghostEventProtocol_Type=DisplayString
_OghostEventProtocol_Object=MibTableColumn
oghostEventProtocol=_OghostEventProtocol_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,14),_OghostEventProtocol_Type())
oghostEventProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventProtocol.setStatus(_B)
_OghostEventPort_Type=Integer32
_OghostEventPort_Object=MibTableColumn
oghostEventPort=_OghostEventPort_Object((1,3,6,1,4,1,25049,10,14,10,1,1,1,15),_OghostEventPort_Type())
oghostEventPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oghostEventPort.setStatus(_B)
ogHostMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,14,3,2,1))
ogHostMibGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ogHostMibGroup.setStatus(_B)
oghostEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,14,2,0,200))
oghostEventOccurred.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:oghostEventOccurred.setStatus(_B)
oghostNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,14,3,2,2))
oghostNotificationsGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:oghostNotificationsGroup.setStatus(_B)
ogHostMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,14,3,1,1))
ogHostMibCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ogHostMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogHostMib':ogHostMib,'ogHostMibNotificationPrefix':ogHostMibNotificationPrefix,'oghostMibNotifications':oghostMibNotifications,_L:oghostEventOccurred,'ogHostMibConformance':ogHostMibConformance,'ogHostMibCompliances':ogHostMibCompliances,'ogHostMibCompliance':ogHostMibCompliance,'ogHostMibGroups':ogHostMibGroups,_M:ogHostMibGroup,_N:oghostNotificationsGroup,'ogHostMibObjects':ogHostMibObjects,'oghostEvent':oghostEvent,'oghostEventTable':oghostEventTable,'oghostEventEntry':oghostEventEntry,_K:oghostEventIndex,_D:oghostEventUsername,_E:oghostEventType,_F:oghostEventAddress,_G:oghostEventDescription,_H:oghostEventProtocol,_I:oghostEventPort})