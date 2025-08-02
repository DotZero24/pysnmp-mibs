_H='accessible-for-notify'
_G='read-write'
_F='h3cFcNsFloginPortWWN'
_E='h3cFcNsLocalSwitchWWN'
_D='h3cVsanIndex'
_C='H3C-VSAN-MIB'
_B='H3C-FC-NAME-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcNameId,=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcNameId')
h3cSan,h3cVsanIndex=mibBuilder.importSymbols(_C,'h3cSan',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cFcNameServer=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,10))
if mibBuilder.loadTexts:h3cFcNameServer.setRevisions(('2014-03-03 10:18',))
_H3cFcNameServerMibObjects_ObjectIdentity=ObjectIdentity
h3cFcNameServerMibObjects=_H3cFcNameServerMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,10,1))
_H3cFcNsNotification_ObjectIdentity=ObjectIdentity
h3cFcNsNotification=_H3cFcNsNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,10,1,1))
_H3cFcNsNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cFcNsNotificationPrefix=_H3cFcNsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,10,1,1,0))
_H3cFcNsNotificationSwitch_ObjectIdentity=ObjectIdentity
h3cFcNsNotificationSwitch=_H3cFcNsNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,10,1,1,1))
_H3cFcNsPortLoginNotifyEnable_Type=TruthValue
_H3cFcNsPortLoginNotifyEnable_Object=MibScalar
h3cFcNsPortLoginNotifyEnable=_H3cFcNsPortLoginNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,127,10,1,1,1,1),_H3cFcNsPortLoginNotifyEnable_Type())
h3cFcNsPortLoginNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcNsPortLoginNotifyEnable.setStatus(_A)
_H3cFcNsPortLogoutNotifyEnable_Type=TruthValue
_H3cFcNsPortLogoutNotifyEnable_Object=MibScalar
h3cFcNsPortLogoutNotifyEnable=_H3cFcNsPortLogoutNotifyEnable_Object((1,3,6,1,4,1,2011,10,2,127,10,1,1,1,2),_H3cFcNsPortLogoutNotifyEnable_Type())
h3cFcNsPortLogoutNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcNsPortLogoutNotifyEnable.setStatus(_A)
_H3cFcNsObjsForNotification_ObjectIdentity=ObjectIdentity
h3cFcNsObjsForNotification=_H3cFcNsObjsForNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,10,1,1,2))
_H3cFcNsLocalSwitchWWN_Type=H3cFcNameId
_H3cFcNsLocalSwitchWWN_Object=MibScalar
h3cFcNsLocalSwitchWWN=_H3cFcNsLocalSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,10,1,1,2,1),_H3cFcNsLocalSwitchWWN_Type())
h3cFcNsLocalSwitchWWN.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFcNsLocalSwitchWWN.setStatus(_A)
_H3cFcNsFloginPortWWN_Type=H3cFcNameId
_H3cFcNsFloginPortWWN_Object=MibScalar
h3cFcNsFloginPortWWN=_H3cFcNsFloginPortWWN_Object((1,3,6,1,4,1,2011,10,2,127,10,1,1,2,2),_H3cFcNsFloginPortWWN_Type())
h3cFcNsFloginPortWWN.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cFcNsFloginPortWWN.setStatus(_A)
h3cFcNsPortLoginNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,10,1,1,0,1))
h3cFcNsPortLoginNotify.setObjects(*((_C,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:h3cFcNsPortLoginNotify.setStatus(_A)
h3cFcNsPortLogoutNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,10,1,1,0,2))
h3cFcNsPortLogoutNotify.setObjects(*((_C,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:h3cFcNsPortLogoutNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cFcNameServer':h3cFcNameServer,'h3cFcNameServerMibObjects':h3cFcNameServerMibObjects,'h3cFcNsNotification':h3cFcNsNotification,'h3cFcNsNotificationPrefix':h3cFcNsNotificationPrefix,'h3cFcNsPortLoginNotify':h3cFcNsPortLoginNotify,'h3cFcNsPortLogoutNotify':h3cFcNsPortLogoutNotify,'h3cFcNsNotificationSwitch':h3cFcNsNotificationSwitch,'h3cFcNsPortLoginNotifyEnable':h3cFcNsPortLoginNotifyEnable,'h3cFcNsPortLogoutNotifyEnable':h3cFcNsPortLogoutNotifyEnable,'h3cFcNsObjsForNotification':h3cFcNsObjsForNotification,_E:h3cFcNsLocalSwitchWWN,_F:h3cFcNsFloginPortWWN})