_J='hm2MACNotifyInterfaceMACStatus'
_I='hm2MACNotifyInterfaceMACAddr'
_H='read-only'
_G='HM2-MAC-NOTIFICATION-MIB'
_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='HmEnabledStatus'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_B,'hm2ConfigurationMibs')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hm2MACNotificationMib=ModuleIdentity((1,3,6,1,4,1,248,11,35))
if mibBuilder.loadTexts:hm2MACNotificationMib.setRevisions(('2012-03-31 00:00',))
_Hm2MACNotifyMibNotifications_ObjectIdentity=ObjectIdentity
hm2MACNotifyMibNotifications=_Hm2MACNotifyMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,35,0))
_Hm2MACNotifyMibObjects_ObjectIdentity=ObjectIdentity
hm2MACNotifyMibObjects=_Hm2MACNotifyMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,35,1))
class _Hm2MACNotifyAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2MACNotifyAdminState_Type.__name__=_B
_Hm2MACNotifyAdminState_Object=MibScalar
hm2MACNotifyAdminState=_Hm2MACNotifyAdminState_Object((1,3,6,1,4,1,248,11,35,1,1),_Hm2MACNotifyAdminState_Type())
hm2MACNotifyAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2MACNotifyAdminState.setStatus(_A)
class _Hm2MACNotifyInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2MACNotifyInterval_Type.__name__=_E
_Hm2MACNotifyInterval_Object=MibScalar
hm2MACNotifyInterval=_Hm2MACNotifyInterval_Object((1,3,6,1,4,1,248,11,35,1,2),_Hm2MACNotifyInterval_Type())
hm2MACNotifyInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2MACNotifyInterval.setStatus(_A)
_Hm2MACNotifyInterfaceTable_Object=MibTable
hm2MACNotifyInterfaceTable=_Hm2MACNotifyInterfaceTable_Object((1,3,6,1,4,1,248,11,35,1,10))
if mibBuilder.loadTexts:hm2MACNotifyInterfaceTable.setStatus(_A)
_Hm2MACNotifyInterfaceEntry_Object=MibTableRow
hm2MACNotifyInterfaceEntry=_Hm2MACNotifyInterfaceEntry_Object((1,3,6,1,4,1,248,11,35,1,10,1))
hm2MACNotifyInterfaceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hm2MACNotifyInterfaceEntry.setStatus(_A)
class _Hm2MACNotifyInterfaceAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2MACNotifyInterfaceAdminState_Type.__name__=_B
_Hm2MACNotifyInterfaceAdminState_Object=MibTableColumn
hm2MACNotifyInterfaceAdminState=_Hm2MACNotifyInterfaceAdminState_Object((1,3,6,1,4,1,248,11,35,1,10,1,1),_Hm2MACNotifyInterfaceAdminState_Type())
hm2MACNotifyInterfaceAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2MACNotifyInterfaceAdminState.setStatus(_A)
_Hm2MACNotifyInterfaceMACAddr_Type=MacAddress
_Hm2MACNotifyInterfaceMACAddr_Object=MibTableColumn
hm2MACNotifyInterfaceMACAddr=_Hm2MACNotifyInterfaceMACAddr_Object((1,3,6,1,4,1,248,11,35,1,10,1,2),_Hm2MACNotifyInterfaceMACAddr_Type())
hm2MACNotifyInterfaceMACAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2MACNotifyInterfaceMACAddr.setStatus(_A)
class _Hm2MACNotifyInterfaceMACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('added',2),('removed',3)))
_Hm2MACNotifyInterfaceMACStatus_Type.__name__=_E
_Hm2MACNotifyInterfaceMACStatus_Object=MibTableColumn
hm2MACNotifyInterfaceMACStatus=_Hm2MACNotifyInterfaceMACStatus_Object((1,3,6,1,4,1,248,11,35,1,10,1,3),_Hm2MACNotifyInterfaceMACStatus_Type())
hm2MACNotifyInterfaceMACStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2MACNotifyInterfaceMACStatus.setStatus(_A)
hm2MACNotificationTrap=NotificationType((1,3,6,1,4,1,248,11,35,0,1))
hm2MACNotificationTrap.setObjects(*((_C,_D),(_G,_I),(_G,_J)))
if mibBuilder.loadTexts:hm2MACNotificationTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hm2MACNotificationMib':hm2MACNotificationMib,'hm2MACNotifyMibNotifications':hm2MACNotifyMibNotifications,'hm2MACNotificationTrap':hm2MACNotificationTrap,'hm2MACNotifyMibObjects':hm2MACNotifyMibObjects,'hm2MACNotifyAdminState':hm2MACNotifyAdminState,'hm2MACNotifyInterval':hm2MACNotifyInterval,'hm2MACNotifyInterfaceTable':hm2MACNotifyInterfaceTable,'hm2MACNotifyInterfaceEntry':hm2MACNotifyInterfaceEntry,'hm2MACNotifyInterfaceAdminState':hm2MACNotifyInterfaceAdminState,_I:hm2MACNotifyInterfaceMACAddr,_J:hm2MACNotifyInterfaceMACStatus})