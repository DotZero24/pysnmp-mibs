_L='voiceVlanOui'
_K='TPLINK-VOICEVLAN-MIB'
_J='enable'
_I='disable'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='read-only'
_D='read-write'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkVoiceVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,19))
if mibBuilder.loadTexts:tplinkVoiceVlanMIB.setRevisions(('2012-12-13 16:30',))
_TplinkVoiceVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkVoiceVlanMIBObjects=_TplinkVoiceVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,19,1))
_VoiceVlanGlobalConfig_ObjectIdentity=ObjectIdentity
voiceVlanGlobalConfig=_VoiceVlanGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,19,1,1))
class _VoiceVlanGlobalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_VoiceVlanGlobalEnable_Type.__name__=_B
_VoiceVlanGlobalEnable_Object=MibScalar
voiceVlanGlobalEnable=_VoiceVlanGlobalEnable_Object((1,3,6,1,4,1,11863,6,19,1,1,1),_VoiceVlanGlobalEnable_Type())
voiceVlanGlobalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceVlanGlobalEnable.setStatus(_A)
class _VoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_VoiceVlanId_Type.__name__=_B
_VoiceVlanId_Object=MibScalar
voiceVlanId=_VoiceVlanId_Object((1,3,6,1,4,1,11863,6,19,1,1,2),_VoiceVlanId_Type())
voiceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceVlanId.setStatus(_A)
class _VoiceVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cos0',0),('cos1',1),('cos2',2),('cos3',3),('cos4',4),('cos5',5),('cos6',6),('cos7',7)))
_VoiceVlanPriority_Type.__name__=_B
_VoiceVlanPriority_Object=MibScalar
voiceVlanPriority=_VoiceVlanPriority_Object((1,3,6,1,4,1,11863,6,19,1,1,3),_VoiceVlanPriority_Type())
voiceVlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceVlanPriority.setStatus(_A)
_VoiceVlanPortConfig_ObjectIdentity=ObjectIdentity
voiceVlanPortConfig=_VoiceVlanPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,19,1,2))
_VoiceVlanPortTable_Object=MibTable
voiceVlanPortTable=_VoiceVlanPortTable_Object((1,3,6,1,4,1,11863,6,19,1,2,1))
if mibBuilder.loadTexts:voiceVlanPortTable.setStatus(_A)
_VoiceVlanPortEntry_Object=MibTableRow
voiceVlanPortEntry=_VoiceVlanPortEntry_Object((1,3,6,1,4,1,11863,6,19,1,2,1,1))
voiceVlanPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:voiceVlanPortEntry.setStatus(_A)
class _VoiceVlanPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VoiceVlanPortNumber_Type.__name__=_C
_VoiceVlanPortNumber_Object=MibTableColumn
voiceVlanPortNumber=_VoiceVlanPortNumber_Object((1,3,6,1,4,1,11863,6,19,1,2,1,1,1),_VoiceVlanPortNumber_Type())
voiceVlanPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:voiceVlanPortNumber.setStatus(_A)
class _VoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_VoiceVlanPortMode_Type.__name__=_B
_VoiceVlanPortMode_Object=MibTableColumn
voiceVlanPortMode=_VoiceVlanPortMode_Object((1,3,6,1,4,1,11863,6,19,1,2,1,1,2),_VoiceVlanPortMode_Type())
voiceVlanPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceVlanPortMode.setStatus(_A)
class _VoiceVlanPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_VoiceVlanPortStatus_Type.__name__=_B
_VoiceVlanPortStatus_Object=MibTableColumn
voiceVlanPortStatus=_VoiceVlanPortStatus_Object((1,3,6,1,4,1,11863,6,19,1,2,1,1,3),_VoiceVlanPortStatus_Type())
voiceVlanPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:voiceVlanPortStatus.setStatus(_A)
class _VoiceVlanPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_VoiceVlanPortLag_Type.__name__=_C
_VoiceVlanPortLag_Object=MibTableColumn
voiceVlanPortLag=_VoiceVlanPortLag_Object((1,3,6,1,4,1,11863,6,19,1,2,1,1,4),_VoiceVlanPortLag_Type())
voiceVlanPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:voiceVlanPortLag.setStatus(_A)
_VoiceVlanOuiConfig_ObjectIdentity=ObjectIdentity
voiceVlanOuiConfig=_VoiceVlanOuiConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,19,1,3))
_VoiceVlanOuiConfigTable_Object=MibTable
voiceVlanOuiConfigTable=_VoiceVlanOuiConfigTable_Object((1,3,6,1,4,1,11863,6,19,1,3,1))
if mibBuilder.loadTexts:voiceVlanOuiConfigTable.setStatus(_A)
_VoiceVlanOuiConfigEntry_Object=MibTableRow
voiceVlanOuiConfigEntry=_VoiceVlanOuiConfigEntry_Object((1,3,6,1,4,1,11863,6,19,1,3,1,1))
voiceVlanOuiConfigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:voiceVlanOuiConfigEntry.setStatus(_A)
class _VoiceVlanOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoiceVlanOui_Type.__name__=_C
_VoiceVlanOui_Object=MibTableColumn
voiceVlanOui=_VoiceVlanOui_Object((1,3,6,1,4,1,11863,6,19,1,3,1,1,1),_VoiceVlanOui_Type())
voiceVlanOui.setMaxAccess(_F)
if mibBuilder.loadTexts:voiceVlanOui.setStatus(_A)
class _VoiceVlanDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VoiceVlanDescription_Type.__name__=_C
_VoiceVlanDescription_Object=MibTableColumn
voiceVlanDescription=_VoiceVlanDescription_Object((1,3,6,1,4,1,11863,6,19,1,3,1,1,2),_VoiceVlanDescription_Type())
voiceVlanDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:voiceVlanDescription.setStatus(_A)
_VoiceVlanRowStatus_Type=TPRowStatus
_VoiceVlanRowStatus_Object=MibTableColumn
voiceVlanRowStatus=_VoiceVlanRowStatus_Object((1,3,6,1,4,1,11863,6,19,1,3,1,1,3),_VoiceVlanRowStatus_Type())
voiceVlanRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:voiceVlanRowStatus.setStatus(_A)
_TplinkVoiceVlanMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkVoiceVlanMIBNotifications=_TplinkVoiceVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,19,2))
mibBuilder.exportSymbols(_K,**{'tplinkVoiceVlanMIB':tplinkVoiceVlanMIB,'tplinkVoiceVlanMIBObjects':tplinkVoiceVlanMIBObjects,'voiceVlanGlobalConfig':voiceVlanGlobalConfig,'voiceVlanGlobalEnable':voiceVlanGlobalEnable,'voiceVlanId':voiceVlanId,'voiceVlanPriority':voiceVlanPriority,'voiceVlanPortConfig':voiceVlanPortConfig,'voiceVlanPortTable':voiceVlanPortTable,'voiceVlanPortEntry':voiceVlanPortEntry,'voiceVlanPortNumber':voiceVlanPortNumber,'voiceVlanPortMode':voiceVlanPortMode,'voiceVlanPortStatus':voiceVlanPortStatus,'voiceVlanPortLag':voiceVlanPortLag,'voiceVlanOuiConfig':voiceVlanOuiConfig,'voiceVlanOuiConfigTable':voiceVlanOuiConfigTable,'voiceVlanOuiConfigEntry':voiceVlanOuiConfigEntry,_L:voiceVlanOui,'voiceVlanDescription':voiceVlanDescription,'voiceVlanRowStatus':voiceVlanRowStatus,'tplinkVoiceVlanMIBNotifications':tplinkVoiceVlanMIBNotifications})