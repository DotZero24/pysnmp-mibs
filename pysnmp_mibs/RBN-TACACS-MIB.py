_Q='rbnTacacsNotifyGroup'
_P='rbnTacacsNotifyObjectsGroup'
_O='rbnTacacsStateChange'
_N='rbnTacacsServerMsg'
_M='rbnTacacsUserName'
_L='rbnTacacsServerReason'
_K='rbnTacacsServerState'
_J='rbnTacacsServerPort'
_I='rbnTacacsServerAddress'
_H='rbnTacacsServerAddressType'
_G='rbnTacacsServerIndex'
_F='rbnTacacsContext'
_E='Unsigned32'
_D='SnmpAdminString'
_C='accessible-for-notify'
_B='current'
_A='RBN-TACACS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnTacacsMib=ModuleIdentity((1,3,6,1,4,1,2352,2,33))
if mibBuilder.loadTexts:rbnTacacsMib.setRevisions(('2004-03-01 18:00',))
class RbnTacacsState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('up',2),('down',3)))
class RbnTacacsReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('responding',1),('packetTimeout',2),('serverTimeout',3),('serverError',4)))
_RbnTacacsMIBNotifications_ObjectIdentity=ObjectIdentity
rbnTacacsMIBNotifications=_RbnTacacsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,33,0))
_RbnTacacsMIBObjects_ObjectIdentity=ObjectIdentity
rbnTacacsMIBObjects=_RbnTacacsMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,33,1))
_RbnTacacsObjects_ObjectIdentity=ObjectIdentity
rbnTacacsObjects=_RbnTacacsObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,33,1,1))
_RbnTacacsAcctObjects_ObjectIdentity=ObjectIdentity
rbnTacacsAcctObjects=_RbnTacacsAcctObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,33,1,2))
_RbnTacacsNotifyObjects_ObjectIdentity=ObjectIdentity
rbnTacacsNotifyObjects=_RbnTacacsNotifyObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,33,1,3))
class _RbnTacacsContext_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RbnTacacsContext_Type.__name__=_D
_RbnTacacsContext_Object=MibScalar
rbnTacacsContext=_RbnTacacsContext_Object((1,3,6,1,4,1,2352,2,33,1,3,1),_RbnTacacsContext_Type())
rbnTacacsContext.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsContext.setStatus(_B)
class _RbnTacacsServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnTacacsServerIndex_Type.__name__=_E
_RbnTacacsServerIndex_Object=MibScalar
rbnTacacsServerIndex=_RbnTacacsServerIndex_Object((1,3,6,1,4,1,2352,2,33,1,3,2),_RbnTacacsServerIndex_Type())
rbnTacacsServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerIndex.setStatus(_B)
_RbnTacacsServerAddressType_Type=InetAddressType
_RbnTacacsServerAddressType_Object=MibScalar
rbnTacacsServerAddressType=_RbnTacacsServerAddressType_Object((1,3,6,1,4,1,2352,2,33,1,3,3),_RbnTacacsServerAddressType_Type())
rbnTacacsServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerAddressType.setStatus(_B)
_RbnTacacsServerAddress_Type=InetAddress
_RbnTacacsServerAddress_Object=MibScalar
rbnTacacsServerAddress=_RbnTacacsServerAddress_Object((1,3,6,1,4,1,2352,2,33,1,3,4),_RbnTacacsServerAddress_Type())
rbnTacacsServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerAddress.setStatus(_B)
class _RbnTacacsServerPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnTacacsServerPort_Type.__name__=_E
_RbnTacacsServerPort_Object=MibScalar
rbnTacacsServerPort=_RbnTacacsServerPort_Object((1,3,6,1,4,1,2352,2,33,1,3,5),_RbnTacacsServerPort_Type())
rbnTacacsServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerPort.setStatus(_B)
_RbnTacacsServerState_Type=RbnTacacsState
_RbnTacacsServerState_Object=MibScalar
rbnTacacsServerState=_RbnTacacsServerState_Object((1,3,6,1,4,1,2352,2,33,1,3,6),_RbnTacacsServerState_Type())
rbnTacacsServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerState.setStatus(_B)
_RbnTacacsServerReason_Type=RbnTacacsReason
_RbnTacacsServerReason_Object=MibScalar
rbnTacacsServerReason=_RbnTacacsServerReason_Object((1,3,6,1,4,1,2352,2,33,1,3,7),_RbnTacacsServerReason_Type())
rbnTacacsServerReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerReason.setStatus(_B)
class _RbnTacacsUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RbnTacacsUserName_Type.__name__=_D
_RbnTacacsUserName_Object=MibScalar
rbnTacacsUserName=_RbnTacacsUserName_Object((1,3,6,1,4,1,2352,2,33,1,3,8),_RbnTacacsUserName_Type())
rbnTacacsUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsUserName.setStatus(_B)
class _RbnTacacsServerMsg_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RbnTacacsServerMsg_Type.__name__=_D
_RbnTacacsServerMsg_Object=MibScalar
rbnTacacsServerMsg=_RbnTacacsServerMsg_Object((1,3,6,1,4,1,2352,2,33,1,3,9),_RbnTacacsServerMsg_Type())
rbnTacacsServerMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnTacacsServerMsg.setStatus(_B)
_RbnTacacsMIBConformance_ObjectIdentity=ObjectIdentity
rbnTacacsMIBConformance=_RbnTacacsMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,33,2))
_RbnTacacsCompliances_ObjectIdentity=ObjectIdentity
rbnTacacsCompliances=_RbnTacacsCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,33,2,1))
_RbnTacacsGroups_ObjectIdentity=ObjectIdentity
rbnTacacsGroups=_RbnTacacsGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,33,2,2))
rbnTacacsNotifyObjectsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,33,2,2,2))
rbnTacacsNotifyObjectsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:rbnTacacsNotifyObjectsGroup.setStatus(_B)
rbnTacacsStateChange=NotificationType((1,3,6,1,4,1,2352,2,33,0,1))
rbnTacacsStateChange.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:rbnTacacsStateChange.setStatus(_B)
rbnTacacsNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,33,2,2,3))
rbnTacacsNotifyGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:rbnTacacsNotifyGroup.setStatus(_B)
rbnTacacsCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,33,2,1,1))
rbnTacacsCompliance.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:rbnTacacsCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbnTacacsState':RbnTacacsState,'RbnTacacsReason':RbnTacacsReason,'rbnTacacsMib':rbnTacacsMib,'rbnTacacsMIBNotifications':rbnTacacsMIBNotifications,_O:rbnTacacsStateChange,'rbnTacacsMIBObjects':rbnTacacsMIBObjects,'rbnTacacsObjects':rbnTacacsObjects,'rbnTacacsAcctObjects':rbnTacacsAcctObjects,'rbnTacacsNotifyObjects':rbnTacacsNotifyObjects,_F:rbnTacacsContext,_G:rbnTacacsServerIndex,_H:rbnTacacsServerAddressType,_I:rbnTacacsServerAddress,_J:rbnTacacsServerPort,_K:rbnTacacsServerState,_L:rbnTacacsServerReason,_M:rbnTacacsUserName,_N:rbnTacacsServerMsg,'rbnTacacsMIBConformance':rbnTacacsMIBConformance,'rbnTacacsCompliances':rbnTacacsCompliances,'rbnTacacsCompliance':rbnTacacsCompliance,'rbnTacacsGroups':rbnTacacsGroups,_P:rbnTacacsNotifyObjectsGroup,_Q:rbnTacacsNotifyGroup})