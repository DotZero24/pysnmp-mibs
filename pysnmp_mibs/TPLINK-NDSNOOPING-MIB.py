_K='ndSnoopingVlanId'
_J='TPLINK-NDSNOOPING-MIB'
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
tplinkNdSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,92))
if mibBuilder.loadTexts:tplinkNdSnoopingMIB.setRevisions(('2012-12-17 10:14',))
_TplinkNdSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkNdSnoopingMIBObjects=_TplinkNdSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,92,1))
_NdSnoopingGlobalConfig_ObjectIdentity=ObjectIdentity
ndSnoopingGlobalConfig=_NdSnoopingGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,92,1,1))
class _NdSnoopingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NdSnoopingEnable_Type.__name__=_B
_NdSnoopingEnable_Object=MibScalar
ndSnoopingEnable=_NdSnoopingEnable_Object((1,3,6,1,4,1,11863,6,92,1,1,1),_NdSnoopingEnable_Type())
ndSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ndSnoopingEnable.setStatus(_A)
_NdSnoopingVlanConfigTable_Object=MibTable
ndSnoopingVlanConfigTable=_NdSnoopingVlanConfigTable_Object((1,3,6,1,4,1,11863,6,92,1,1,2))
if mibBuilder.loadTexts:ndSnoopingVlanConfigTable.setStatus(_A)
_NdSnoopingVlanConfigEntry_Object=MibTableRow
ndSnoopingVlanConfigEntry=_NdSnoopingVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,92,1,1,2,1))
ndSnoopingVlanConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:ndSnoopingVlanConfigEntry.setStatus(_A)
class _NdSnoopingVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_NdSnoopingVlanId_Type.__name__=_B
_NdSnoopingVlanId_Object=MibTableColumn
ndSnoopingVlanId=_NdSnoopingVlanId_Object((1,3,6,1,4,1,11863,6,92,1,1,2,1,1),_NdSnoopingVlanId_Type())
ndSnoopingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ndSnoopingVlanId.setStatus(_A)
class _NdSnoopingVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NdSnoopingVlanStatus_Type.__name__=_B
_NdSnoopingVlanStatus_Object=MibTableColumn
ndSnoopingVlanStatus=_NdSnoopingVlanStatus_Object((1,3,6,1,4,1,11863,6,92,1,1,2,1,2),_NdSnoopingVlanStatus_Type())
ndSnoopingVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ndSnoopingVlanStatus.setStatus(_A)
_NdSnoopingPortConfig_ObjectIdentity=ObjectIdentity
ndSnoopingPortConfig=_NdSnoopingPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,92,1,3))
_NdSnoopingPortConfigTable_Object=MibTable
ndSnoopingPortConfigTable=_NdSnoopingPortConfigTable_Object((1,3,6,1,4,1,11863,6,92,1,3,1))
if mibBuilder.loadTexts:ndSnoopingPortConfigTable.setStatus(_A)
_NdSnoopingPortConfigEntry_Object=MibTableRow
ndSnoopingPortConfigEntry=_NdSnoopingPortConfigEntry_Object((1,3,6,1,4,1,11863,6,92,1,3,1,1))
ndSnoopingPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ndSnoopingPortConfigEntry.setStatus(_A)
class _NdSnoopingPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NdSnoopingPort_Type.__name__=_C
_NdSnoopingPort_Object=MibTableColumn
ndSnoopingPort=_NdSnoopingPort_Object((1,3,6,1,4,1,11863,6,92,1,3,1,1,1),_NdSnoopingPort_Type())
ndSnoopingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ndSnoopingPort.setStatus(_A)
class _NdSnoopingPortConfigMaxEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1024))
_NdSnoopingPortConfigMaxEntry_Type.__name__=_B
_NdSnoopingPortConfigMaxEntry_Object=MibTableColumn
ndSnoopingPortConfigMaxEntry=_NdSnoopingPortConfigMaxEntry_Object((1,3,6,1,4,1,11863,6,92,1,3,1,1,2),_NdSnoopingPortConfigMaxEntry_Type())
ndSnoopingPortConfigMaxEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:ndSnoopingPortConfigMaxEntry.setStatus(_A)
class _NdSnoopingPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NdSnoopingPortConfigPortLag_Type.__name__=_C
_NdSnoopingPortConfigPortLag_Object=MibTableColumn
ndSnoopingPortConfigPortLag=_NdSnoopingPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,92,1,3,1,1,3),_NdSnoopingPortConfigPortLag_Type())
ndSnoopingPortConfigPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:ndSnoopingPortConfigPortLag.setStatus(_A)
_TplinkNdSnoopingNotifications_ObjectIdentity=ObjectIdentity
tplinkNdSnoopingNotifications=_TplinkNdSnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,92,2))
mibBuilder.exportSymbols(_J,**{'tplinkNdSnoopingMIB':tplinkNdSnoopingMIB,'tplinkNdSnoopingMIBObjects':tplinkNdSnoopingMIBObjects,'ndSnoopingGlobalConfig':ndSnoopingGlobalConfig,'ndSnoopingEnable':ndSnoopingEnable,'ndSnoopingVlanConfigTable':ndSnoopingVlanConfigTable,'ndSnoopingVlanConfigEntry':ndSnoopingVlanConfigEntry,_K:ndSnoopingVlanId,'ndSnoopingVlanStatus':ndSnoopingVlanStatus,'ndSnoopingPortConfig':ndSnoopingPortConfig,'ndSnoopingPortConfigTable':ndSnoopingPortConfigTable,'ndSnoopingPortConfigEntry':ndSnoopingPortConfigEntry,'ndSnoopingPort':ndSnoopingPort,'ndSnoopingPortConfigMaxEntry':ndSnoopingPortConfigMaxEntry,'ndSnoopingPortConfigPortLag':ndSnoopingPortConfigPortLag,'tplinkNdSnoopingNotifications':tplinkNdSnoopingNotifications})