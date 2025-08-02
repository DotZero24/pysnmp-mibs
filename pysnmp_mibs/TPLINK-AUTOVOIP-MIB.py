_I='read-only'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='enable'
_D='disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkAutoVoipMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,98))
if mibBuilder.loadTexts:tplinkAutoVoipMIB.setRevisions(('2012-12-13 16:30',))
_TplinkAutoVoipMIBObjects_ObjectIdentity=ObjectIdentity
tplinkAutoVoipMIBObjects=_TplinkAutoVoipMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,98,1))
_AutoVoipGlobalConfig_ObjectIdentity=ObjectIdentity
autoVoipGlobalConfig=_AutoVoipGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,98,1,1))
class _AutoVoipGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoVoipGlobalEnable_Type.__name__=_B
_AutoVoipGlobalEnable_Object=MibScalar
autoVoipGlobalEnable=_AutoVoipGlobalEnable_Object((1,3,6,1,4,1,11863,6,98,1,1,1),_AutoVoipGlobalEnable_Type())
autoVoipGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:autoVoipGlobalEnable.setStatus(_A)
_AutoVoipPortConfig_ObjectIdentity=ObjectIdentity
autoVoipPortConfig=_AutoVoipPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,98,1,2))
_AutoVoipPortTable_Object=MibTable
autoVoipPortTable=_AutoVoipPortTable_Object((1,3,6,1,4,1,11863,6,98,1,2,1))
if mibBuilder.loadTexts:autoVoipPortTable.setStatus(_A)
_AutoVoipPortEntry_Object=MibTableRow
autoVoipPortEntry=_AutoVoipPortEntry_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1))
autoVoipPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:autoVoipPortEntry.setStatus(_A)
class _AutoVoipPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AutoVoipPortNumber_Type.__name__=_F
_AutoVoipPortNumber_Object=MibTableColumn
autoVoipPortNumber=_AutoVoipPortNumber_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,1),_AutoVoipPortNumber_Type())
autoVoipPortNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:autoVoipPortNumber.setStatus(_A)
class _AutoVoipPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('vlan',1),('dot1p',2),('none',3),('untagged',4)))
_AutoVoipPortMode_Type.__name__=_B
_AutoVoipPortMode_Object=MibTableColumn
autoVoipPortMode=_AutoVoipPortMode_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,2),_AutoVoipPortMode_Type())
autoVoipPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:autoVoipPortMode.setStatus(_A)
class _AutoVoipPortValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AutoVoipPortValue_Type.__name__=_B
_AutoVoipPortValue_Object=MibTableColumn
autoVoipPortValue=_AutoVoipPortValue_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,3),_AutoVoipPortValue_Type())
autoVoipPortValue.setMaxAccess(_C)
if mibBuilder.loadTexts:autoVoipPortValue.setStatus(_A)
class _AutoVoipCosOverrideMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoVoipCosOverrideMode_Type.__name__=_B
_AutoVoipCosOverrideMode_Object=MibTableColumn
autoVoipCosOverrideMode=_AutoVoipCosOverrideMode_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,4),_AutoVoipCosOverrideMode_Type())
autoVoipCosOverrideMode.setMaxAccess(_C)
if mibBuilder.loadTexts:autoVoipCosOverrideMode.setStatus(_A)
class _AutoVoipOperaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AutoVoipOperaState_Type.__name__=_B
_AutoVoipOperaState_Object=MibTableColumn
autoVoipOperaState=_AutoVoipOperaState_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,5),_AutoVoipOperaState_Type())
autoVoipOperaState.setMaxAccess(_I)
if mibBuilder.loadTexts:autoVoipOperaState.setStatus(_A)
class _AutoVoipDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AutoVoipDscpValue_Type.__name__=_B
_AutoVoipDscpValue_Object=MibTableColumn
autoVoipDscpValue=_AutoVoipDscpValue_Object((1,3,6,1,4,1,11863,6,98,1,2,1,1,6),_AutoVoipDscpValue_Type())
autoVoipDscpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:autoVoipDscpValue.setStatus(_A)
_TplinkAutoVoipMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkAutoVoipMIBNotifications=_TplinkAutoVoipMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,98,2))
mibBuilder.exportSymbols('TPLINK-AUTOVOIP-MIB',**{'tplinkAutoVoipMIB':tplinkAutoVoipMIB,'tplinkAutoVoipMIBObjects':tplinkAutoVoipMIBObjects,'autoVoipGlobalConfig':autoVoipGlobalConfig,'autoVoipGlobalEnable':autoVoipGlobalEnable,'autoVoipPortConfig':autoVoipPortConfig,'autoVoipPortTable':autoVoipPortTable,'autoVoipPortEntry':autoVoipPortEntry,'autoVoipPortNumber':autoVoipPortNumber,'autoVoipPortMode':autoVoipPortMode,'autoVoipPortValue':autoVoipPortValue,'autoVoipCosOverrideMode':autoVoipCosOverrideMode,'autoVoipOperaState':autoVoipOperaState,'autoVoipDscpValue':autoVoipDscpValue,'tplinkAutoVoipMIBNotifications':tplinkAutoVoipMIBNotifications})