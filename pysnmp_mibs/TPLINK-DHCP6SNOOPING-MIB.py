_K='dhcp6SnoopingVlanId'
_J='TPLINK-DHCP6SNOOPING-MIB'
_I='enable'
_H='disable'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-write'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkDhcp6SnoopingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,91))
if mibBuilder.loadTexts:tplinkDhcp6SnoopingMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcp6SnoopingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcp6SnoopingMIBObjects=_TplinkDhcp6SnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,91,1))
_Dhcp6SnoopingGlobalConfig_ObjectIdentity=ObjectIdentity
dhcp6SnoopingGlobalConfig=_Dhcp6SnoopingGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,91,1,1))
class _Dhcp6SnoopingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_Dhcp6SnoopingEnable_Type.__name__=_B
_Dhcp6SnoopingEnable_Object=MibScalar
dhcp6SnoopingEnable=_Dhcp6SnoopingEnable_Object((1,3,6,1,4,1,11863,6,91,1,1,1),_Dhcp6SnoopingEnable_Type())
dhcp6SnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcp6SnoopingEnable.setStatus(_A)
_Dhcp6SnoopingVlanConfigTable_Object=MibTable
dhcp6SnoopingVlanConfigTable=_Dhcp6SnoopingVlanConfigTable_Object((1,3,6,1,4,1,11863,6,91,1,1,2))
if mibBuilder.loadTexts:dhcp6SnoopingVlanConfigTable.setStatus(_A)
_Dhcp6SnoopingVlanConfigEntry_Object=MibTableRow
dhcp6SnoopingVlanConfigEntry=_Dhcp6SnoopingVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,91,1,1,2,1))
dhcp6SnoopingVlanConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:dhcp6SnoopingVlanConfigEntry.setStatus(_A)
class _Dhcp6SnoopingVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dhcp6SnoopingVlanId_Type.__name__=_B
_Dhcp6SnoopingVlanId_Object=MibTableColumn
dhcp6SnoopingVlanId=_Dhcp6SnoopingVlanId_Object((1,3,6,1,4,1,11863,6,91,1,1,2,1,1),_Dhcp6SnoopingVlanId_Type())
dhcp6SnoopingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6SnoopingVlanId.setStatus(_A)
class _Dhcp6SnoopingVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_Dhcp6SnoopingVlanStatus_Type.__name__=_B
_Dhcp6SnoopingVlanStatus_Object=MibTableColumn
dhcp6SnoopingVlanStatus=_Dhcp6SnoopingVlanStatus_Object((1,3,6,1,4,1,11863,6,91,1,1,2,1,2),_Dhcp6SnoopingVlanStatus_Type())
dhcp6SnoopingVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcp6SnoopingVlanStatus.setStatus(_A)
_Dhcp6SnoopingPortConfig_ObjectIdentity=ObjectIdentity
dhcp6SnoopingPortConfig=_Dhcp6SnoopingPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,91,1,3))
_Dhcp6SnoopingPortConfigTable_Object=MibTable
dhcp6SnoopingPortConfigTable=_Dhcp6SnoopingPortConfigTable_Object((1,3,6,1,4,1,11863,6,91,1,3,1))
if mibBuilder.loadTexts:dhcp6SnoopingPortConfigTable.setStatus(_A)
_Dhcp6SnoopingPortConfigEntry_Object=MibTableRow
dhcp6SnoopingPortConfigEntry=_Dhcp6SnoopingPortConfigEntry_Object((1,3,6,1,4,1,11863,6,91,1,3,1,1))
dhcp6SnoopingPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dhcp6SnoopingPortConfigEntry.setStatus(_A)
class _Dhcp6SnoopingPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dhcp6SnoopingPort_Type.__name__=_C
_Dhcp6SnoopingPort_Object=MibTableColumn
dhcp6SnoopingPort=_Dhcp6SnoopingPort_Object((1,3,6,1,4,1,11863,6,91,1,3,1,1,1),_Dhcp6SnoopingPort_Type())
dhcp6SnoopingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6SnoopingPort.setStatus(_A)
_Dhcp6SnoopingPortConfigMaxEntry_Type=Integer32
_Dhcp6SnoopingPortConfigMaxEntry_Object=MibTableColumn
dhcp6SnoopingPortConfigMaxEntry=_Dhcp6SnoopingPortConfigMaxEntry_Object((1,3,6,1,4,1,11863,6,91,1,3,1,1,2),_Dhcp6SnoopingPortConfigMaxEntry_Type())
dhcp6SnoopingPortConfigMaxEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcp6SnoopingPortConfigMaxEntry.setStatus(_A)
class _Dhcp6SnoopingPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Dhcp6SnoopingPortConfigPortLag_Type.__name__=_C
_Dhcp6SnoopingPortConfigPortLag_Object=MibTableColumn
dhcp6SnoopingPortConfigPortLag=_Dhcp6SnoopingPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,91,1,3,1,1,3),_Dhcp6SnoopingPortConfigPortLag_Type())
dhcp6SnoopingPortConfigPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcp6SnoopingPortConfigPortLag.setStatus(_A)
_TplinkDhcp6SnoopingNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcp6SnoopingNotifications=_TplinkDhcp6SnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,91,2))
mibBuilder.exportSymbols(_J,**{'tplinkDhcp6SnoopingMIB':tplinkDhcp6SnoopingMIB,'tplinkDhcp6SnoopingMIBObjects':tplinkDhcp6SnoopingMIBObjects,'dhcp6SnoopingGlobalConfig':dhcp6SnoopingGlobalConfig,'dhcp6SnoopingEnable':dhcp6SnoopingEnable,'dhcp6SnoopingVlanConfigTable':dhcp6SnoopingVlanConfigTable,'dhcp6SnoopingVlanConfigEntry':dhcp6SnoopingVlanConfigEntry,_K:dhcp6SnoopingVlanId,'dhcp6SnoopingVlanStatus':dhcp6SnoopingVlanStatus,'dhcp6SnoopingPortConfig':dhcp6SnoopingPortConfig,'dhcp6SnoopingPortConfigTable':dhcp6SnoopingPortConfigTable,'dhcp6SnoopingPortConfigEntry':dhcp6SnoopingPortConfigEntry,'dhcp6SnoopingPort':dhcp6SnoopingPort,'dhcp6SnoopingPortConfigMaxEntry':dhcp6SnoopingPortConfigMaxEntry,'dhcp6SnoopingPortConfigPortLag':dhcp6SnoopingPortConfigPortLag,'tplinkDhcp6SnoopingNotifications':tplinkDhcp6SnoopingNotifications})