_I='bcsiUdldNotifGroup'
_H='bcsiUdldNotifLinkUp'
_G='bcsiUdldNotifLinkDown'
_F='SnmpAdminString'
_E='bcsiUdldNotifMessage'
_D='ifIndex'
_C='IF-MIB'
_B='current'
_A='BROCADE-UDLD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ifIndex,=mibBuilder.importSymbols(_C,_D)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brocadeUdldMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,9))
if mibBuilder.loadTexts:brocadeUdldMIB.setRevisions(('2018-07-26 21:00','2016-09-28 00:00'))
_BcsiUdldNotifications_ObjectIdentity=ObjectIdentity
bcsiUdldNotifications=_BcsiUdldNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,0))
_BcsiUdldObjects_ObjectIdentity=ObjectIdentity
bcsiUdldObjects=_BcsiUdldObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,1))
_BcsiUdldNotifObjects_ObjectIdentity=ObjectIdentity
bcsiUdldNotifObjects=_BcsiUdldNotifObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,1,1))
class _BcsiUdldNotifMessage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BcsiUdldNotifMessage_Type.__name__=_F
_BcsiUdldNotifMessage_Object=MibScalar
bcsiUdldNotifMessage=_BcsiUdldNotifMessage_Object((1,3,6,1,4,1,1588,3,1,9,1,1,1),_BcsiUdldNotifMessage_Type())
bcsiUdldNotifMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bcsiUdldNotifMessage.setStatus(_B)
_BcsiUdldConformance_ObjectIdentity=ObjectIdentity
bcsiUdldConformance=_BcsiUdldConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,2))
_BcsiUdldCompliances_ObjectIdentity=ObjectIdentity
bcsiUdldCompliances=_BcsiUdldCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,2,1))
_BcsiUdldGroups_ObjectIdentity=ObjectIdentity
bcsiUdldGroups=_BcsiUdldGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,9,2,2))
bcsiUdldNotifLinkDown=NotificationType((1,3,6,1,4,1,1588,3,1,9,0,1))
bcsiUdldNotifLinkDown.setObjects(*((_C,_D),(_A,_E)))
if mibBuilder.loadTexts:bcsiUdldNotifLinkDown.setStatus(_B)
bcsiUdldNotifLinkUp=NotificationType((1,3,6,1,4,1,1588,3,1,9,0,2))
bcsiUdldNotifLinkUp.setObjects(*((_C,_D),(_A,_E)))
if mibBuilder.loadTexts:bcsiUdldNotifLinkUp.setStatus(_B)
bcsiUdldNotifGroup=NotificationGroup((1,3,6,1,4,1,1588,3,1,9,2,2,1))
bcsiUdldNotifGroup.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:bcsiUdldNotifGroup.setStatus(_B)
bcsiUdldCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,9,2,1,1))
bcsiUdldCompliance.setObjects((_A,_I))
if mibBuilder.loadTexts:bcsiUdldCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'brocadeUdldMIB':brocadeUdldMIB,'bcsiUdldNotifications':bcsiUdldNotifications,_G:bcsiUdldNotifLinkDown,_H:bcsiUdldNotifLinkUp,'bcsiUdldObjects':bcsiUdldObjects,'bcsiUdldNotifObjects':bcsiUdldNotifObjects,_E:bcsiUdldNotifMessage,'bcsiUdldConformance':bcsiUdldConformance,'bcsiUdldCompliances':bcsiUdldCompliances,'bcsiUdldCompliance':bcsiUdldCompliance,'bcsiUdldGroups':bcsiUdldGroups,_I:bcsiUdldNotifGroup})