_P='zySecuredClientIndex'
_O='console'
_N='zyAccessControlService'
_M='https'
_L='http'
_K='ftp'
_J='ssh'
_I='telnet'
_H='Integer32'
_G='zyAccessControlLoginIpAddress'
_F='zyAccessControlLoginUsername'
_E='zyAccessControlLoginService'
_D='not-accessible'
_C='read-write'
_B='ZYXEL-ACCESS-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelAccessControl=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,9))
_ZyxelAccessControlSetup_ObjectIdentity=ObjectIdentity
zyxelAccessControlSetup=_ZyxelAccessControlSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,9,1))
_ZyxelAccessControlTable_Object=MibTable
zyxelAccessControlTable=_ZyxelAccessControlTable_Object((1,3,6,1,4,1,890,1,15,3,9,1,1))
if mibBuilder.loadTexts:zyxelAccessControlTable.setStatus(_A)
_ZyxelAccessControlEntry_Object=MibTableRow
zyxelAccessControlEntry=_ZyxelAccessControlEntry_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1))
zyxelAccessControlEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:zyxelAccessControlEntry.setStatus(_A)
class _ZyAccessControlService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),('icmp',6),('snmp',7),(_O,8)))
_ZyAccessControlService_Type.__name__=_H
_ZyAccessControlService_Object=MibTableColumn
zyAccessControlService=_ZyAccessControlService_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1,1),_ZyAccessControlService_Type())
zyAccessControlService.setMaxAccess(_D)
if mibBuilder.loadTexts:zyAccessControlService.setStatus(_A)
_ZyAccessControlState_Type=EnabledStatus
_ZyAccessControlState_Object=MibTableColumn
zyAccessControlState=_ZyAccessControlState_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1,2),_ZyAccessControlState_Type())
zyAccessControlState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyAccessControlState.setStatus(_A)
_ZyAccessControlServicePort_Type=Integer32
_ZyAccessControlServicePort_Object=MibTableColumn
zyAccessControlServicePort=_ZyAccessControlServicePort_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1,3),_ZyAccessControlServicePort_Type())
zyAccessControlServicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:zyAccessControlServicePort.setStatus(_A)
_ZyAccessControlTimeout_Type=Integer32
_ZyAccessControlTimeout_Object=MibTableColumn
zyAccessControlTimeout=_ZyAccessControlTimeout_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1,4),_ZyAccessControlTimeout_Type())
zyAccessControlTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:zyAccessControlTimeout.setStatus(_A)
_ZyAccessControlLoginTimeout_Type=Integer32
_ZyAccessControlLoginTimeout_Object=MibTableColumn
zyAccessControlLoginTimeout=_ZyAccessControlLoginTimeout_Object((1,3,6,1,4,1,890,1,15,3,9,1,1,1,5),_ZyAccessControlLoginTimeout_Type())
zyAccessControlLoginTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:zyAccessControlLoginTimeout.setStatus(_A)
_ZyxelSecuredClientTable_Object=MibTable
zyxelSecuredClientTable=_ZyxelSecuredClientTable_Object((1,3,6,1,4,1,890,1,15,3,9,1,2))
if mibBuilder.loadTexts:zyxelSecuredClientTable.setStatus(_A)
_ZyxelSecuredClientEntry_Object=MibTableRow
zyxelSecuredClientEntry=_ZyxelSecuredClientEntry_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1))
zyxelSecuredClientEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:zyxelSecuredClientEntry.setStatus(_A)
_ZySecuredClientIndex_Type=Integer32
_ZySecuredClientIndex_Object=MibTableColumn
zySecuredClientIndex=_ZySecuredClientIndex_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1,1),_ZySecuredClientIndex_Type())
zySecuredClientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zySecuredClientIndex.setStatus(_A)
_ZySecuredClientState_Type=EnabledStatus
_ZySecuredClientState_Object=MibTableColumn
zySecuredClientState=_ZySecuredClientState_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1,2),_ZySecuredClientState_Type())
zySecuredClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:zySecuredClientState.setStatus(_A)
_ZySecuredClientStartIpAddress_Type=IpAddress
_ZySecuredClientStartIpAddress_Object=MibTableColumn
zySecuredClientStartIpAddress=_ZySecuredClientStartIpAddress_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1,3),_ZySecuredClientStartIpAddress_Type())
zySecuredClientStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zySecuredClientStartIpAddress.setStatus(_A)
_ZySecuredClientEndIpAddress_Type=IpAddress
_ZySecuredClientEndIpAddress_Object=MibTableColumn
zySecuredClientEndIpAddress=_ZySecuredClientEndIpAddress_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1,4),_ZySecuredClientEndIpAddress_Type())
zySecuredClientEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zySecuredClientEndIpAddress.setStatus(_A)
class _ZySecuredClientService_Type(Bits):namedValues=NamedValues(*((_I,0),(_K,1),(_L,2),('icmp',3),('snmp',4),(_J,5),(_M,6)))
_ZySecuredClientService_Type.__name__='Bits'
_ZySecuredClientService_Object=MibTableColumn
zySecuredClientService=_ZySecuredClientService_Object((1,3,6,1,4,1,890,1,15,3,9,1,2,1,5),_ZySecuredClientService_Type())
zySecuredClientService.setMaxAccess(_C)
if mibBuilder.loadTexts:zySecuredClientService.setStatus(_A)
_ZyxelAccessControlTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelAccessControlTrapInfoObject=_ZyxelAccessControlTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,9,3))
class _ZyAccessControlLoginService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_ZyAccessControlLoginService_Type.__name__=_H
_ZyAccessControlLoginService_Object=MibScalar
zyAccessControlLoginService=_ZyAccessControlLoginService_Object((1,3,6,1,4,1,890,1,15,3,9,3,1),_ZyAccessControlLoginService_Type())
zyAccessControlLoginService.setMaxAccess(_D)
if mibBuilder.loadTexts:zyAccessControlLoginService.setStatus(_A)
_ZyAccessControlLoginUsername_Type=DisplayString
_ZyAccessControlLoginUsername_Object=MibScalar
zyAccessControlLoginUsername=_ZyAccessControlLoginUsername_Object((1,3,6,1,4,1,890,1,15,3,9,3,2),_ZyAccessControlLoginUsername_Type())
zyAccessControlLoginUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:zyAccessControlLoginUsername.setStatus(_A)
_ZyAccessControlLoginIpAddress_Type=DisplayString
_ZyAccessControlLoginIpAddress_Object=MibScalar
zyAccessControlLoginIpAddress=_ZyAccessControlLoginIpAddress_Object((1,3,6,1,4,1,890,1,15,3,9,3,3),_ZyAccessControlLoginIpAddress_Type())
zyAccessControlLoginIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyAccessControlLoginIpAddress.setStatus(_A)
_ZyxelAccessControlNotifications_ObjectIdentity=ObjectIdentity
zyxelAccessControlNotifications=_ZyxelAccessControlNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,9,4))
zyAccessControlLoginRecord=NotificationType((1,3,6,1,4,1,890,1,15,3,9,4,1))
zyAccessControlLoginRecord.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:zyAccessControlLoginRecord.setStatus(_A)
zyAccessControlLogoutRecord=NotificationType((1,3,6,1,4,1,890,1,15,3,9,4,2))
zyAccessControlLogoutRecord.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:zyAccessControlLogoutRecord.setStatus(_A)
zyAccessControlLoginFail=NotificationType((1,3,6,1,4,1,890,1,15,3,9,4,3))
zyAccessControlLoginFail.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:zyAccessControlLoginFail.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelAccessControl':zyxelAccessControl,'zyxelAccessControlSetup':zyxelAccessControlSetup,'zyxelAccessControlTable':zyxelAccessControlTable,'zyxelAccessControlEntry':zyxelAccessControlEntry,_N:zyAccessControlService,'zyAccessControlState':zyAccessControlState,'zyAccessControlServicePort':zyAccessControlServicePort,'zyAccessControlTimeout':zyAccessControlTimeout,'zyAccessControlLoginTimeout':zyAccessControlLoginTimeout,'zyxelSecuredClientTable':zyxelSecuredClientTable,'zyxelSecuredClientEntry':zyxelSecuredClientEntry,_P:zySecuredClientIndex,'zySecuredClientState':zySecuredClientState,'zySecuredClientStartIpAddress':zySecuredClientStartIpAddress,'zySecuredClientEndIpAddress':zySecuredClientEndIpAddress,'zySecuredClientService':zySecuredClientService,'zyxelAccessControlTrapInfoObject':zyxelAccessControlTrapInfoObject,_E:zyAccessControlLoginService,_F:zyAccessControlLoginUsername,_G:zyAccessControlLoginIpAddress,'zyxelAccessControlNotifications':zyxelAccessControlNotifications,'zyAccessControlLoginRecord':zyAccessControlLoginRecord,'zyAccessControlLogoutRecord':zyAccessControlLogoutRecord,'zyAccessControlLoginFail':zyAccessControlLoginFail})