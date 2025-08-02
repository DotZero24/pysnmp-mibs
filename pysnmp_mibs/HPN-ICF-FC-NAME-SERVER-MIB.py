_H='accessible-for-notify'
_G='read-write'
_F='hpnicfFcNsFloginPortWWN'
_E='hpnicfFcNsLocalSwitchWWN'
_D='hpnicfVsanIndex'
_C='HPN-ICF-VSAN-MIB'
_B='HPN-ICF-FC-NAME-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcNameId,=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcNameId')
hpnicfSan,hpnicfVsanIndex=mibBuilder.importSymbols(_C,'hpnicfSan',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfFcNameServer=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10))
if mibBuilder.loadTexts:hpnicfFcNameServer.setRevisions(('2014-03-03 10:18',))
_HpnicfFcNameServerMibObjects_ObjectIdentity=ObjectIdentity
hpnicfFcNameServerMibObjects=_HpnicfFcNameServerMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1))
_HpnicfFcNsNotification_ObjectIdentity=ObjectIdentity
hpnicfFcNsNotification=_HpnicfFcNsNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1))
_HpnicfFcNsNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfFcNsNotificationPrefix=_HpnicfFcNsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,0))
_HpnicfFcNsNotificationSwitch_ObjectIdentity=ObjectIdentity
hpnicfFcNsNotificationSwitch=_HpnicfFcNsNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,1))
_HpnicfFcNsPortLoginNotifyEnable_Type=TruthValue
_HpnicfFcNsPortLoginNotifyEnable_Object=MibScalar
hpnicfFcNsPortLoginNotifyEnable=_HpnicfFcNsPortLoginNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,1,1),_HpnicfFcNsPortLoginNotifyEnable_Type())
hpnicfFcNsPortLoginNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcNsPortLoginNotifyEnable.setStatus(_A)
_HpnicfFcNsPortLogoutNotifyEnable_Type=TruthValue
_HpnicfFcNsPortLogoutNotifyEnable_Object=MibScalar
hpnicfFcNsPortLogoutNotifyEnable=_HpnicfFcNsPortLogoutNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,1,2),_HpnicfFcNsPortLogoutNotifyEnable_Type())
hpnicfFcNsPortLogoutNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcNsPortLogoutNotifyEnable.setStatus(_A)
_HpnicfFcNsObjsForNotification_ObjectIdentity=ObjectIdentity
hpnicfFcNsObjsForNotification=_HpnicfFcNsObjsForNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,2))
_HpnicfFcNsLocalSwitchWWN_Type=HpnicfFcNameId
_HpnicfFcNsLocalSwitchWWN_Object=MibScalar
hpnicfFcNsLocalSwitchWWN=_HpnicfFcNsLocalSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,2,1),_HpnicfFcNsLocalSwitchWWN_Type())
hpnicfFcNsLocalSwitchWWN.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFcNsLocalSwitchWWN.setStatus(_A)
_HpnicfFcNsFloginPortWWN_Type=HpnicfFcNameId
_HpnicfFcNsFloginPortWWN_Object=MibScalar
hpnicfFcNsFloginPortWWN=_HpnicfFcNsFloginPortWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,2,2),_HpnicfFcNsFloginPortWWN_Type())
hpnicfFcNsFloginPortWWN.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfFcNsFloginPortWWN.setStatus(_A)
hpnicfFcNsPortLoginNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,0,1))
hpnicfFcNsPortLoginNotify.setObjects(*((_C,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hpnicfFcNsPortLoginNotify.setStatus(_A)
hpnicfFcNsPortLogoutNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,10,1,1,0,2))
hpnicfFcNsPortLogoutNotify.setObjects(*((_C,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hpnicfFcNsPortLogoutNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfFcNameServer':hpnicfFcNameServer,'hpnicfFcNameServerMibObjects':hpnicfFcNameServerMibObjects,'hpnicfFcNsNotification':hpnicfFcNsNotification,'hpnicfFcNsNotificationPrefix':hpnicfFcNsNotificationPrefix,'hpnicfFcNsPortLoginNotify':hpnicfFcNsPortLoginNotify,'hpnicfFcNsPortLogoutNotify':hpnicfFcNsPortLogoutNotify,'hpnicfFcNsNotificationSwitch':hpnicfFcNsNotificationSwitch,'hpnicfFcNsPortLoginNotifyEnable':hpnicfFcNsPortLoginNotifyEnable,'hpnicfFcNsPortLogoutNotifyEnable':hpnicfFcNsPortLogoutNotifyEnable,'hpnicfFcNsObjsForNotification':hpnicfFcNsObjsForNotification,_E:hpnicfFcNsLocalSwitchWWN,_F:hpnicfFcNsFloginPortWWN})