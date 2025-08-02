_J='read-create'
_I='DisplayString'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkPPPoEConfigMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,57))
if mibBuilder.loadTexts:tplinkPPPoEConfigMIB.setRevisions(('2012-12-17 10:50',))
_TplinkPPPoEConfigMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPPPoEConfigMIBObjects=_TplinkPPPoEConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,57,1))
_TpPppoeIdInsertionGlobalConfig_ObjectIdentity=ObjectIdentity
tpPppoeIdInsertionGlobalConfig=_TpPppoeIdInsertionGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,57,1,1))
class _TpPppoeIdInsertionGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TpPppoeIdInsertionGlobalEnable_Type.__name__=_B
_TpPppoeIdInsertionGlobalEnable_Object=MibScalar
tpPppoeIdInsertionGlobalEnable=_TpPppoeIdInsertionGlobalEnable_Object((1,3,6,1,4,1,11863,6,57,1,1,1),_TpPppoeIdInsertionGlobalEnable_Type())
tpPppoeIdInsertionGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPppoeIdInsertionGlobalEnable.setStatus(_A)
_TpPppoeIdInsertionPortConfig_ObjectIdentity=ObjectIdentity
tpPppoeIdInsertionPortConfig=_TpPppoeIdInsertionPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,57,1,2))
_TpPppoeIdInsertionPortConfigTable_Object=MibTable
tpPppoeIdInsertionPortConfigTable=_TpPppoeIdInsertionPortConfigTable_Object((1,3,6,1,4,1,11863,6,57,1,2,1))
if mibBuilder.loadTexts:tpPppoeIdInsertionPortConfigTable.setStatus(_A)
_TpPppoeIdInsertionPortConfigEntry_Object=MibTableRow
tpPppoeIdInsertionPortConfigEntry=_TpPppoeIdInsertionPortConfigEntry_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1))
tpPppoeIdInsertionPortConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpPppoeIdInsertionPortConfigEntry.setStatus(_A)
class _TpPppoeIdInsertionPortIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpPppoeIdInsertionPortIndex_Type.__name__=_I
_TpPppoeIdInsertionPortIndex_Object=MibTableColumn
tpPppoeIdInsertionPortIndex=_TpPppoeIdInsertionPortIndex_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,1),_TpPppoeIdInsertionPortIndex_Type())
tpPppoeIdInsertionPortIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpPppoeIdInsertionPortIndex.setStatus(_A)
class _TpPppoeCircuitIdPortConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TpPppoeCircuitIdPortConfigEnable_Type.__name__=_B
_TpPppoeCircuitIdPortConfigEnable_Object=MibTableColumn
tpPppoeCircuitIdPortConfigEnable=_TpPppoeCircuitIdPortConfigEnable_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,2),_TpPppoeCircuitIdPortConfigEnable_Type())
tpPppoeCircuitIdPortConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPppoeCircuitIdPortConfigEnable.setStatus(_A)
class _TpPppoeCircuitIdPortConfigIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('switchIp',0),('switchMac',1),('switchUdf',2),('switchUdfOnly',3)))
_TpPppoeCircuitIdPortConfigIdType_Type.__name__=_B
_TpPppoeCircuitIdPortConfigIdType_Object=MibTableColumn
tpPppoeCircuitIdPortConfigIdType=_TpPppoeCircuitIdPortConfigIdType_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,3),_TpPppoeCircuitIdPortConfigIdType_Type())
tpPppoeCircuitIdPortConfigIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPppoeCircuitIdPortConfigIdType.setStatus(_A)
class _TpPppoeCircuitIdPortConfigUdfValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TpPppoeCircuitIdPortConfigUdfValue_Type.__name__=_D
_TpPppoeCircuitIdPortConfigUdfValue_Object=MibTableColumn
tpPppoeCircuitIdPortConfigUdfValue=_TpPppoeCircuitIdPortConfigUdfValue_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,4),_TpPppoeCircuitIdPortConfigUdfValue_Type())
tpPppoeCircuitIdPortConfigUdfValue.setMaxAccess(_J)
if mibBuilder.loadTexts:tpPppoeCircuitIdPortConfigUdfValue.setStatus(_A)
class _TpPppoeRemoteIdPortConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TpPppoeRemoteIdPortConfigEnable_Type.__name__=_B
_TpPppoeRemoteIdPortConfigEnable_Object=MibTableColumn
tpPppoeRemoteIdPortConfigEnable=_TpPppoeRemoteIdPortConfigEnable_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,5),_TpPppoeRemoteIdPortConfigEnable_Type())
tpPppoeRemoteIdPortConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpPppoeRemoteIdPortConfigEnable.setStatus(_A)
class _TpPppoeRemoteIdPortConfigValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TpPppoeRemoteIdPortConfigValue_Type.__name__=_D
_TpPppoeRemoteIdPortConfigValue_Object=MibTableColumn
tpPppoeRemoteIdPortConfigValue=_TpPppoeRemoteIdPortConfigValue_Object((1,3,6,1,4,1,11863,6,57,1,2,1,1,6),_TpPppoeRemoteIdPortConfigValue_Type())
tpPppoeRemoteIdPortConfigValue.setMaxAccess(_J)
if mibBuilder.loadTexts:tpPppoeRemoteIdPortConfigValue.setStatus(_A)
_TplinkPPPoEConfigNotifications_ObjectIdentity=ObjectIdentity
tplinkPPPoEConfigNotifications=_TplinkPPPoEConfigNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,57,2))
mibBuilder.exportSymbols('TPLINK-pppoeConfig-MIB',**{'tplinkPPPoEConfigMIB':tplinkPPPoEConfigMIB,'tplinkPPPoEConfigMIBObjects':tplinkPPPoEConfigMIBObjects,'tpPppoeIdInsertionGlobalConfig':tpPppoeIdInsertionGlobalConfig,'tpPppoeIdInsertionGlobalEnable':tpPppoeIdInsertionGlobalEnable,'tpPppoeIdInsertionPortConfig':tpPppoeIdInsertionPortConfig,'tpPppoeIdInsertionPortConfigTable':tpPppoeIdInsertionPortConfigTable,'tpPppoeIdInsertionPortConfigEntry':tpPppoeIdInsertionPortConfigEntry,'tpPppoeIdInsertionPortIndex':tpPppoeIdInsertionPortIndex,'tpPppoeCircuitIdPortConfigEnable':tpPppoeCircuitIdPortConfigEnable,'tpPppoeCircuitIdPortConfigIdType':tpPppoeCircuitIdPortConfigIdType,'tpPppoeCircuitIdPortConfigUdfValue':tpPppoeCircuitIdPortConfigUdfValue,'tpPppoeRemoteIdPortConfigEnable':tpPppoeRemoteIdPortConfigEnable,'tpPppoeRemoteIdPortConfigValue':tpPppoeRemoteIdPortConfigValue,'tplinkPPPoEConfigNotifications':tplinkPPPoEConfigNotifications})