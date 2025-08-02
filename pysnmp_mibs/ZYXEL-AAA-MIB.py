_O='zyAaaTrapAuthorizationMethod'
_N='zyAaaTrapAuthenticationMethod'
_M='telnet'
_L='console'
_K='notAvailable'
_J='zyAaaAccountingTypeName'
_I='tacacs'
_H='radius'
_G='zyAaaAuthorizationTypeName'
_F='zyAaaAuthenticationTypeName'
_E='not-accessible'
_D='ZYXEL-AAA-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelAaa=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,94))
_ZyxelAaaSetup_ObjectIdentity=ObjectIdentity
zyxelAaaSetup=_ZyxelAaaSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,1))
_ZyxelAaaAuthenticationSetup_ObjectIdentity=ObjectIdentity
zyxelAaaAuthenticationSetup=_ZyxelAaaAuthenticationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,1,1))
_ZyxelAaaAuthenticationTypeTable_Object=MibTable
zyxelAaaAuthenticationTypeTable=_ZyxelAaaAuthenticationTypeTable_Object((1,3,6,1,4,1,890,1,15,3,94,1,1,1))
if mibBuilder.loadTexts:zyxelAaaAuthenticationTypeTable.setStatus(_A)
_ZyxelAaaAuthenticationTypeEntry_Object=MibTableRow
zyxelAaaAuthenticationTypeEntry=_ZyxelAaaAuthenticationTypeEntry_Object((1,3,6,1,4,1,890,1,15,3,94,1,1,1,1))
zyxelAaaAuthenticationTypeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:zyxelAaaAuthenticationTypeEntry.setStatus(_A)
_ZyAaaAuthenticationTypeName_Type=DisplayString
_ZyAaaAuthenticationTypeName_Object=MibTableColumn
zyAaaAuthenticationTypeName=_ZyAaaAuthenticationTypeName_Object((1,3,6,1,4,1,890,1,15,3,94,1,1,1,1,1),_ZyAaaAuthenticationTypeName_Type())
zyAaaAuthenticationTypeName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAaaAuthenticationTypeName.setStatus(_A)
_ZyAaaAuthenticationTypeMethodList_Type=OctetString
_ZyAaaAuthenticationTypeMethodList_Object=MibTableColumn
zyAaaAuthenticationTypeMethodList=_ZyAaaAuthenticationTypeMethodList_Object((1,3,6,1,4,1,890,1,15,3,94,1,1,1,1,2),_ZyAaaAuthenticationTypeMethodList_Type())
zyAaaAuthenticationTypeMethodList.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAuthenticationTypeMethodList.setStatus(_A)
_ZyxelAaaAuthorizationSetup_ObjectIdentity=ObjectIdentity
zyxelAaaAuthorizationSetup=_ZyxelAaaAuthorizationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,1,2))
_ZyAaaAuthorizationConsoleState_Type=EnabledStatus
_ZyAaaAuthorizationConsoleState_Object=MibScalar
zyAaaAuthorizationConsoleState=_ZyAaaAuthorizationConsoleState_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,1),_ZyAaaAuthorizationConsoleState_Type())
zyAaaAuthorizationConsoleState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAuthorizationConsoleState.setStatus(_A)
_ZyxelAaaAuthorizationTypeTable_Object=MibTable
zyxelAaaAuthorizationTypeTable=_ZyxelAaaAuthorizationTypeTable_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,2))
if mibBuilder.loadTexts:zyxelAaaAuthorizationTypeTable.setStatus(_A)
_ZyxelAaaAuthorizationTypeEntry_Object=MibTableRow
zyxelAaaAuthorizationTypeEntry=_ZyxelAaaAuthorizationTypeEntry_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,2,1))
zyxelAaaAuthorizationTypeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:zyxelAaaAuthorizationTypeEntry.setStatus(_A)
_ZyAaaAuthorizationTypeName_Type=DisplayString
_ZyAaaAuthorizationTypeName_Object=MibTableColumn
zyAaaAuthorizationTypeName=_ZyAaaAuthorizationTypeName_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,2,1,1),_ZyAaaAuthorizationTypeName_Type())
zyAaaAuthorizationTypeName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAaaAuthorizationTypeName.setStatus(_A)
_ZyAaaAuthorizationTypeState_Type=EnabledStatus
_ZyAaaAuthorizationTypeState_Object=MibTableColumn
zyAaaAuthorizationTypeState=_ZyAaaAuthorizationTypeState_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,2,1,2),_ZyAaaAuthorizationTypeState_Type())
zyAaaAuthorizationTypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAuthorizationTypeState.setStatus(_A)
class _ZyAaaAuthorizationTypeMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZyAaaAuthorizationTypeMethod_Type.__name__=_C
_ZyAaaAuthorizationTypeMethod_Object=MibTableColumn
zyAaaAuthorizationTypeMethod=_ZyAaaAuthorizationTypeMethod_Object((1,3,6,1,4,1,890,1,15,3,94,1,2,2,1,3),_ZyAaaAuthorizationTypeMethod_Type())
zyAaaAuthorizationTypeMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAuthorizationTypeMethod.setStatus(_A)
_ZyxelAaaAccountingSetup_ObjectIdentity=ObjectIdentity
zyxelAaaAccountingSetup=_ZyxelAaaAccountingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,1,3))
_ZyAaaAccountingUpdatePeriod_Type=Integer32
_ZyAaaAccountingUpdatePeriod_Object=MibScalar
zyAaaAccountingUpdatePeriod=_ZyAaaAccountingUpdatePeriod_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,1),_ZyAaaAccountingUpdatePeriod_Type())
zyAaaAccountingUpdatePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingUpdatePeriod.setStatus(_A)
_ZyxelAaaAccountingTypeTable_Object=MibTable
zyxelAaaAccountingTypeTable=_ZyxelAaaAccountingTypeTable_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2))
if mibBuilder.loadTexts:zyxelAaaAccountingTypeTable.setStatus(_A)
_ZyxelAaaAccountingTypeEntry_Object=MibTableRow
zyxelAaaAccountingTypeEntry=_ZyxelAaaAccountingTypeEntry_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1))
zyxelAaaAccountingTypeEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:zyxelAaaAccountingTypeEntry.setStatus(_A)
_ZyAaaAccountingTypeName_Type=DisplayString
_ZyAaaAccountingTypeName_Object=MibTableColumn
zyAaaAccountingTypeName=_ZyAaaAccountingTypeName_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,1),_ZyAaaAccountingTypeName_Type())
zyAaaAccountingTypeName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAaaAccountingTypeName.setStatus(_A)
_ZyAaaAccountingTypeState_Type=EnabledStatus
_ZyAaaAccountingTypeState_Object=MibTableColumn
zyAaaAccountingTypeState=_ZyAaaAccountingTypeState_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,2),_ZyAaaAccountingTypeState_Type())
zyAaaAccountingTypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingTypeState.setStatus(_A)
_ZyAaaAccountingTypeBroadcastState_Type=EnabledStatus
_ZyAaaAccountingTypeBroadcastState_Object=MibTableColumn
zyAaaAccountingTypeBroadcastState=_ZyAaaAccountingTypeBroadcastState_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,3),_ZyAaaAccountingTypeBroadcastState_Type())
zyAaaAccountingTypeBroadcastState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingTypeBroadcastState.setStatus(_A)
class _ZyAaaAccountingTypeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('startStop',1),('stopOnly',2),(_K,255)))
_ZyAaaAccountingTypeMode_Type.__name__=_C
_ZyAaaAccountingTypeMode_Object=MibTableColumn
zyAaaAccountingTypeMode=_ZyAaaAccountingTypeMode_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,4),_ZyAaaAccountingTypeMode_Type())
zyAaaAccountingTypeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingTypeMode.setStatus(_A)
class _ZyAaaAccountingTypeMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZyAaaAccountingTypeMethod_Type.__name__=_C
_ZyAaaAccountingTypeMethod_Object=MibTableColumn
zyAaaAccountingTypeMethod=_ZyAaaAccountingTypeMethod_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,5),_ZyAaaAccountingTypeMethod_Type())
zyAaaAccountingTypeMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingTypeMethod.setStatus(_A)
class _ZyAaaAccountingTypePrivilege_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,255)));namedValues=NamedValues(*(('privilege0',0),('privilege1',1),('privilege2',2),('privilege3',3),('privilege4',4),('privilege5',5),('privilege6',6),('privilege7',7),('privilege8',8),('privilege9',9),('privilege10',10),('privilege11',11),('privilege12',12),('privilege13',13),('privilege14',14),(_K,255)))
_ZyAaaAccountingTypePrivilege_Type.__name__=_C
_ZyAaaAccountingTypePrivilege_Object=MibTableColumn
zyAaaAccountingTypePrivilege=_ZyAaaAccountingTypePrivilege_Object((1,3,6,1,4,1,890,1,15,3,94,1,3,2,1,6),_ZyAaaAccountingTypePrivilege_Type())
zyAaaAccountingTypePrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:zyAaaAccountingTypePrivilege.setStatus(_A)
_ZyxelAaaTrapInfoObjects_ObjectIdentity=ObjectIdentity
zyxelAaaTrapInfoObjects=_ZyxelAaaTrapInfoObjects_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,2))
class _ZyAaaTrapAuthenticationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('snmp',0),('ftp',1),(_L,2),('ssh',3),('https',4),('http',5),(_M,6)))
_ZyAaaTrapAuthenticationMethod_Type.__name__=_C
_ZyAaaTrapAuthenticationMethod_Object=MibScalar
zyAaaTrapAuthenticationMethod=_ZyAaaTrapAuthenticationMethod_Object((1,3,6,1,4,1,890,1,15,3,94,2,1),_ZyAaaTrapAuthenticationMethod_Type())
zyAaaTrapAuthenticationMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAaaTrapAuthenticationMethod.setStatus(_A)
class _ZyAaaTrapAuthorizationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('dot1x',0),('ssh',1),('http',2),(_M,3),('ftp',4),(_L,5)))
_ZyAaaTrapAuthorizationMethod_Type.__name__=_C
_ZyAaaTrapAuthorizationMethod_Object=MibScalar
zyAaaTrapAuthorizationMethod=_ZyAaaTrapAuthorizationMethod_Object((1,3,6,1,4,1,890,1,15,3,94,2,2),_ZyAaaTrapAuthorizationMethod_Type())
zyAaaTrapAuthorizationMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:zyAaaTrapAuthorizationMethod.setStatus(_A)
_ZyxelAaaNotifications_ObjectIdentity=ObjectIdentity
zyxelAaaNotifications=_ZyxelAaaNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,94,3))
zyAaaAuthenticationFailure=NotificationType((1,3,6,1,4,1,890,1,15,3,94,3,1))
zyAaaAuthenticationFailure.setObjects((_D,_N))
if mibBuilder.loadTexts:zyAaaAuthenticationFailure.setStatus(_A)
zyAaaAuthorizationFailure=NotificationType((1,3,6,1,4,1,890,1,15,3,94,3,2))
zyAaaAuthorizationFailure.setObjects((_D,_O))
if mibBuilder.loadTexts:zyAaaAuthorizationFailure.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelAaa':zyxelAaa,'zyxelAaaSetup':zyxelAaaSetup,'zyxelAaaAuthenticationSetup':zyxelAaaAuthenticationSetup,'zyxelAaaAuthenticationTypeTable':zyxelAaaAuthenticationTypeTable,'zyxelAaaAuthenticationTypeEntry':zyxelAaaAuthenticationTypeEntry,_F:zyAaaAuthenticationTypeName,'zyAaaAuthenticationTypeMethodList':zyAaaAuthenticationTypeMethodList,'zyxelAaaAuthorizationSetup':zyxelAaaAuthorizationSetup,'zyAaaAuthorizationConsoleState':zyAaaAuthorizationConsoleState,'zyxelAaaAuthorizationTypeTable':zyxelAaaAuthorizationTypeTable,'zyxelAaaAuthorizationTypeEntry':zyxelAaaAuthorizationTypeEntry,_G:zyAaaAuthorizationTypeName,'zyAaaAuthorizationTypeState':zyAaaAuthorizationTypeState,'zyAaaAuthorizationTypeMethod':zyAaaAuthorizationTypeMethod,'zyxelAaaAccountingSetup':zyxelAaaAccountingSetup,'zyAaaAccountingUpdatePeriod':zyAaaAccountingUpdatePeriod,'zyxelAaaAccountingTypeTable':zyxelAaaAccountingTypeTable,'zyxelAaaAccountingTypeEntry':zyxelAaaAccountingTypeEntry,_J:zyAaaAccountingTypeName,'zyAaaAccountingTypeState':zyAaaAccountingTypeState,'zyAaaAccountingTypeBroadcastState':zyAaaAccountingTypeBroadcastState,'zyAaaAccountingTypeMode':zyAaaAccountingTypeMode,'zyAaaAccountingTypeMethod':zyAaaAccountingTypeMethod,'zyAaaAccountingTypePrivilege':zyAaaAccountingTypePrivilege,'zyxelAaaTrapInfoObjects':zyxelAaaTrapInfoObjects,_N:zyAaaTrapAuthenticationMethod,_O:zyAaaTrapAuthorizationMethod,'zyxelAaaNotifications':zyxelAaaNotifications,'zyAaaAuthenticationFailure':zyAaaAuthenticationFailure,'zyAaaAuthorizationFailure':zyAaaAuthorizationFailure})