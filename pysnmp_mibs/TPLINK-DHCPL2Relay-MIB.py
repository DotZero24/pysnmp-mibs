_L='read-only'
_K='read-create'
_J='dhcpL2RelayVlanId'
_I='TPLINK-DHCPL2Relay-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='enable'
_E='disable'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkDhcpL2RelayMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,66))
if mibBuilder.loadTexts:tplinkDhcpL2RelayMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcpL2RelayMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpL2RelayMIBObjects=_TplinkDhcpL2RelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,66,1))
_DhcpL2RelayGlobalConfig_ObjectIdentity=ObjectIdentity
dhcpL2RelayGlobalConfig=_DhcpL2RelayGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,66,1,1))
class _DhcpL2RelayEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpL2RelayEnable_Type.__name__=_B
_DhcpL2RelayEnable_Object=MibScalar
dhcpL2RelayEnable=_DhcpL2RelayEnable_Object((1,3,6,1,4,1,11863,6,66,1,1,1),_DhcpL2RelayEnable_Type())
dhcpL2RelayEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayEnable.setStatus(_A)
_DhcpL2RelayVlanConfigTable_Object=MibTable
dhcpL2RelayVlanConfigTable=_DhcpL2RelayVlanConfigTable_Object((1,3,6,1,4,1,11863,6,66,1,1,2))
if mibBuilder.loadTexts:dhcpL2RelayVlanConfigTable.setStatus(_A)
_DhcpL2RelayVlanConfigEntry_Object=MibTableRow
dhcpL2RelayVlanConfigEntry=_DhcpL2RelayVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,66,1,1,2,1))
dhcpL2RelayVlanConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dhcpL2RelayVlanConfigEntry.setStatus(_A)
class _DhcpL2RelayVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_DhcpL2RelayVlanId_Type.__name__=_B
_DhcpL2RelayVlanId_Object=MibTableColumn
dhcpL2RelayVlanId=_DhcpL2RelayVlanId_Object((1,3,6,1,4,1,11863,6,66,1,1,2,1,1),_DhcpL2RelayVlanId_Type())
dhcpL2RelayVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpL2RelayVlanId.setStatus(_A)
class _DhcpL2RelayVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpL2RelayVlanStatus_Type.__name__=_B
_DhcpL2RelayVlanStatus_Object=MibTableColumn
dhcpL2RelayVlanStatus=_DhcpL2RelayVlanStatus_Object((1,3,6,1,4,1,11863,6,66,1,1,2,1,2),_DhcpL2RelayVlanStatus_Type())
dhcpL2RelayVlanStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpL2RelayVlanStatus.setStatus(_A)
_DhcpL2RelayOption82Config_ObjectIdentity=ObjectIdentity
dhcpL2RelayOption82Config=_DhcpL2RelayOption82Config_ObjectIdentity((1,3,6,1,4,1,11863,6,66,1,2))
_DhcpL2RelayOption82ConfigTable_Object=MibTable
dhcpL2RelayOption82ConfigTable=_DhcpL2RelayOption82ConfigTable_Object((1,3,6,1,4,1,11863,6,66,1,2,1))
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigTable.setStatus(_A)
_DhcpL2RelayOption82ConfigEntry_Object=MibTableRow
dhcpL2RelayOption82ConfigEntry=_DhcpL2RelayOption82ConfigEntry_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1))
dhcpL2RelayOption82ConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigEntry.setStatus(_A)
class _DhcpL2RelayOption82ConfigPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpL2RelayOption82ConfigPort_Type.__name__=_D
_DhcpL2RelayOption82ConfigPort_Object=MibTableColumn
dhcpL2RelayOption82ConfigPort=_DhcpL2RelayOption82ConfigPort_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,1),_DhcpL2RelayOption82ConfigPort_Type())
dhcpL2RelayOption82ConfigPort.setMaxAccess(_L)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigPort.setStatus(_A)
class _DhcpL2RelayOption82ConfigSupportStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpL2RelayOption82ConfigSupportStatus_Type.__name__=_B
_DhcpL2RelayOption82ConfigSupportStatus_Object=MibTableColumn
dhcpL2RelayOption82ConfigSupportStatus=_DhcpL2RelayOption82ConfigSupportStatus_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,2),_DhcpL2RelayOption82ConfigSupportStatus_Type())
dhcpL2RelayOption82ConfigSupportStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigSupportStatus.setStatus(_A)
class _DhcpL2RelayOption82ConfigOperationStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('keep',0),('replace',1),('drop',2)))
_DhcpL2RelayOption82ConfigOperationStrategy_Type.__name__=_B
_DhcpL2RelayOption82ConfigOperationStrategy_Object=MibTableColumn
dhcpL2RelayOption82ConfigOperationStrategy=_DhcpL2RelayOption82ConfigOperationStrategy_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,3),_DhcpL2RelayOption82ConfigOperationStrategy_Type())
dhcpL2RelayOption82ConfigOperationStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigOperationStrategy.setStatus(_A)
class _DhcpL2RelayOption82ConfigFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('private',1)))
_DhcpL2RelayOption82ConfigFormat_Type.__name__=_B
_DhcpL2RelayOption82ConfigFormat_Object=MibTableColumn
dhcpL2RelayOption82ConfigFormat=_DhcpL2RelayOption82ConfigFormat_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,4),_DhcpL2RelayOption82ConfigFormat_Type())
dhcpL2RelayOption82ConfigFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigFormat.setStatus(_A)
class _DhcpL2RelayOption82ConfigCircuitCustomization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpL2RelayOption82ConfigCircuitCustomization_Type.__name__=_B
_DhcpL2RelayOption82ConfigCircuitCustomization_Object=MibTableColumn
dhcpL2RelayOption82ConfigCircuitCustomization=_DhcpL2RelayOption82ConfigCircuitCustomization_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,5),_DhcpL2RelayOption82ConfigCircuitCustomization_Type())
dhcpL2RelayOption82ConfigCircuitCustomization.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigCircuitCustomization.setStatus(_A)
class _DhcpL2RelayOption82ConfigCircuitID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpL2RelayOption82ConfigCircuitID_Type.__name__=_D
_DhcpL2RelayOption82ConfigCircuitID_Object=MibTableColumn
dhcpL2RelayOption82ConfigCircuitID=_DhcpL2RelayOption82ConfigCircuitID_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,6),_DhcpL2RelayOption82ConfigCircuitID_Type())
dhcpL2RelayOption82ConfigCircuitID.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigCircuitID.setStatus(_A)
class _DhcpL2RelayOption82ConfigRemoteCustomization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpL2RelayOption82ConfigRemoteCustomization_Type.__name__=_B
_DhcpL2RelayOption82ConfigRemoteCustomization_Object=MibTableColumn
dhcpL2RelayOption82ConfigRemoteCustomization=_DhcpL2RelayOption82ConfigRemoteCustomization_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,7),_DhcpL2RelayOption82ConfigRemoteCustomization_Type())
dhcpL2RelayOption82ConfigRemoteCustomization.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigRemoteCustomization.setStatus(_A)
class _DhcpL2RelayOption82ConfigRemoteID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpL2RelayOption82ConfigRemoteID_Type.__name__=_D
_DhcpL2RelayOption82ConfigRemoteID_Object=MibTableColumn
dhcpL2RelayOption82ConfigRemoteID=_DhcpL2RelayOption82ConfigRemoteID_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,8),_DhcpL2RelayOption82ConfigRemoteID_Type())
dhcpL2RelayOption82ConfigRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigRemoteID.setStatus(_A)
class _DhcpL2RelayOption82ConfigLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpL2RelayOption82ConfigLag_Type.__name__=_D
_DhcpL2RelayOption82ConfigLag_Object=MibTableColumn
dhcpL2RelayOption82ConfigLag=_DhcpL2RelayOption82ConfigLag_Object((1,3,6,1,4,1,11863,6,66,1,2,1,1,9),_DhcpL2RelayOption82ConfigLag_Type())
dhcpL2RelayOption82ConfigLag.setMaxAccess(_L)
if mibBuilder.loadTexts:dhcpL2RelayOption82ConfigLag.setStatus(_A)
_TplinkDhcpL2RelayNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpL2RelayNotifications=_TplinkDhcpL2RelayNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,66,2))
mibBuilder.exportSymbols(_I,**{'tplinkDhcpL2RelayMIB':tplinkDhcpL2RelayMIB,'tplinkDhcpL2RelayMIBObjects':tplinkDhcpL2RelayMIBObjects,'dhcpL2RelayGlobalConfig':dhcpL2RelayGlobalConfig,'dhcpL2RelayEnable':dhcpL2RelayEnable,'dhcpL2RelayVlanConfigTable':dhcpL2RelayVlanConfigTable,'dhcpL2RelayVlanConfigEntry':dhcpL2RelayVlanConfigEntry,_J:dhcpL2RelayVlanId,'dhcpL2RelayVlanStatus':dhcpL2RelayVlanStatus,'dhcpL2RelayOption82Config':dhcpL2RelayOption82Config,'dhcpL2RelayOption82ConfigTable':dhcpL2RelayOption82ConfigTable,'dhcpL2RelayOption82ConfigEntry':dhcpL2RelayOption82ConfigEntry,'dhcpL2RelayOption82ConfigPort':dhcpL2RelayOption82ConfigPort,'dhcpL2RelayOption82ConfigSupportStatus':dhcpL2RelayOption82ConfigSupportStatus,'dhcpL2RelayOption82ConfigOperationStrategy':dhcpL2RelayOption82ConfigOperationStrategy,'dhcpL2RelayOption82ConfigFormat':dhcpL2RelayOption82ConfigFormat,'dhcpL2RelayOption82ConfigCircuitCustomization':dhcpL2RelayOption82ConfigCircuitCustomization,'dhcpL2RelayOption82ConfigCircuitID':dhcpL2RelayOption82ConfigCircuitID,'dhcpL2RelayOption82ConfigRemoteCustomization':dhcpL2RelayOption82ConfigRemoteCustomization,'dhcpL2RelayOption82ConfigRemoteID':dhcpL2RelayOption82ConfigRemoteID,'dhcpL2RelayOption82ConfigLag':dhcpL2RelayOption82ConfigLag,'tplinkDhcpL2RelayNotifications':tplinkDhcpL2RelayNotifications})