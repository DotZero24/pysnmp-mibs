_W='hpicfOobmGroups'
_V='hpicfOobmMemberGroup'
_U='hpicfOobmDefGatewayGroup'
_T='hpicfSnmpTargetAddrIsOobmGroup'
_S='hpicfOobmServersGroup'
_R='hpicfOobmScalarsGroup'
_Q='hpicfOobmMemberDefGatewayAddr'
_P='hpicfOobmDefGatewayAddr'
_O='hpicfSnmpTargetAddrIsOobm'
_N='hpicfOobmServerListenMode'
_M='hpicfOobmStatus'
_L='hpicfSnmpTargetAddrIsOobmEntry'
_K='hpicfOobmMemberDefGatewayType'
_J='hpicfOobmDefGatewayType'
_I='hpicfOobmServerType'
_H='TruthValue'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-write'
_B='HP-ICF-OOBM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
snmpTargetAddrEntry,=mibBuilder.importSymbols('SNMP-TARGET-MIB','snmpTargetAddrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
hpicfOobmMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58))
if mibBuilder.loadTexts:hpicfOobmMIB.setRevisions(('2010-03-26 00:00','2009-02-13 00:00'))
class HpicfOobmServerIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('telnet',1),('ssh',2),('tftp',3),('http',4),('snmp',5)))
class HpicfOobmServerState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oobm',1),('data',2),('both',3)))
_HpicfOobmNotifications_ObjectIdentity=ObjectIdentity
hpicfOobmNotifications=_HpicfOobmNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,0))
_HpicfOobmObjects_ObjectIdentity=ObjectIdentity
hpicfOobmObjects=_HpicfOobmObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1))
_HpicfOobmScalars_ObjectIdentity=ObjectIdentity
hpicfOobmScalars=_HpicfOobmScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1,1))
class _HpicfOobmStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfOobmStatus_Type.__name__=_G
_HpicfOobmStatus_Object=MibScalar
hpicfOobmStatus=_HpicfOobmStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,1,1),_HpicfOobmStatus_Type())
hpicfOobmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfOobmStatus.setStatus(_A)
_HpicfOobmServers_ObjectIdentity=ObjectIdentity
hpicfOobmServers=_HpicfOobmServers_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1,2))
_HpicfOobmServerTable_Object=MibTable
hpicfOobmServerTable=_HpicfOobmServerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,2,1))
if mibBuilder.loadTexts:hpicfOobmServerTable.setStatus(_A)
_HpicfOobmServerEntry_Object=MibTableRow
hpicfOobmServerEntry=_HpicfOobmServerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,2,1,1))
hpicfOobmServerEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hpicfOobmServerEntry.setStatus(_A)
_HpicfOobmServerType_Type=HpicfOobmServerIndex
_HpicfOobmServerType_Object=MibTableColumn
hpicfOobmServerType=_HpicfOobmServerType_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,2,1,1,1),_HpicfOobmServerType_Type())
hpicfOobmServerType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfOobmServerType.setStatus(_A)
_HpicfOobmServerListenMode_Type=HpicfOobmServerState
_HpicfOobmServerListenMode_Object=MibTableColumn
hpicfOobmServerListenMode=_HpicfOobmServerListenMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,2,1,1,2),_HpicfOobmServerListenMode_Type())
hpicfOobmServerListenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfOobmServerListenMode.setStatus(_A)
_HpicfOobmSnmpTargetAddrIsOobm_ObjectIdentity=ObjectIdentity
hpicfOobmSnmpTargetAddrIsOobm=_HpicfOobmSnmpTargetAddrIsOobm_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1,3))
_HpicfSnmpTargetAddrIsOobmTable_Object=MibTable
hpicfSnmpTargetAddrIsOobmTable=_HpicfSnmpTargetAddrIsOobmTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,3,1))
if mibBuilder.loadTexts:hpicfSnmpTargetAddrIsOobmTable.setStatus(_A)
_HpicfSnmpTargetAddrIsOobmEntry_Object=MibTableRow
hpicfSnmpTargetAddrIsOobmEntry=_HpicfSnmpTargetAddrIsOobmEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,3,1,1))
if mibBuilder.loadTexts:hpicfSnmpTargetAddrIsOobmEntry.setStatus(_A)
class _HpicfSnmpTargetAddrIsOobm_Type(TruthValue):defaultValue=2
_HpicfSnmpTargetAddrIsOobm_Type.__name__=_H
_HpicfSnmpTargetAddrIsOobm_Object=MibTableColumn
hpicfSnmpTargetAddrIsOobm=_HpicfSnmpTargetAddrIsOobm_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,3,1,1,1),_HpicfSnmpTargetAddrIsOobm_Type())
hpicfSnmpTargetAddrIsOobm.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfSnmpTargetAddrIsOobm.setStatus(_A)
_HpicfOobmDefGateway_ObjectIdentity=ObjectIdentity
hpicfOobmDefGateway=_HpicfOobmDefGateway_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1,4))
_HpicfOobmDefGatewayTable_Object=MibTable
hpicfOobmDefGatewayTable=_HpicfOobmDefGatewayTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,4,1))
if mibBuilder.loadTexts:hpicfOobmDefGatewayTable.setStatus(_A)
_HpicfOobmDefGatewayEntry_Object=MibTableRow
hpicfOobmDefGatewayEntry=_HpicfOobmDefGatewayEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,4,1,1))
hpicfOobmDefGatewayEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpicfOobmDefGatewayEntry.setStatus(_A)
_HpicfOobmDefGatewayType_Type=InetAddressType
_HpicfOobmDefGatewayType_Object=MibTableColumn
hpicfOobmDefGatewayType=_HpicfOobmDefGatewayType_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,4,1,1,1),_HpicfOobmDefGatewayType_Type())
hpicfOobmDefGatewayType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfOobmDefGatewayType.setStatus(_A)
_HpicfOobmDefGatewayAddr_Type=InetAddress
_HpicfOobmDefGatewayAddr_Object=MibTableColumn
hpicfOobmDefGatewayAddr=_HpicfOobmDefGatewayAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,4,1,1,2),_HpicfOobmDefGatewayAddr_Type())
hpicfOobmDefGatewayAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfOobmDefGatewayAddr.setStatus(_A)
_HpicfOobmStackMembers_ObjectIdentity=ObjectIdentity
hpicfOobmStackMembers=_HpicfOobmStackMembers_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,1,5))
_HpicfOobmMemberDefGatewayTable_Object=MibTable
hpicfOobmMemberDefGatewayTable=_HpicfOobmMemberDefGatewayTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,5,3))
if mibBuilder.loadTexts:hpicfOobmMemberDefGatewayTable.setStatus(_A)
_HpicfOobmMemberDefGatewayEntry_Object=MibTableRow
hpicfOobmMemberDefGatewayEntry=_HpicfOobmMemberDefGatewayEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,5,3,1))
hpicfOobmMemberDefGatewayEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:hpicfOobmMemberDefGatewayEntry.setStatus(_A)
_HpicfOobmMemberDefGatewayType_Type=InetAddressType
_HpicfOobmMemberDefGatewayType_Object=MibTableColumn
hpicfOobmMemberDefGatewayType=_HpicfOobmMemberDefGatewayType_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,5,3,1,1),_HpicfOobmMemberDefGatewayType_Type())
hpicfOobmMemberDefGatewayType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfOobmMemberDefGatewayType.setStatus(_A)
_HpicfOobmMemberDefGatewayAddr_Type=InetAddress
_HpicfOobmMemberDefGatewayAddr_Object=MibTableColumn
hpicfOobmMemberDefGatewayAddr=_HpicfOobmMemberDefGatewayAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,58,1,5,3,1,2),_HpicfOobmMemberDefGatewayAddr_Type())
hpicfOobmMemberDefGatewayAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfOobmMemberDefGatewayAddr.setStatus(_A)
_HpicfOobmConformance_ObjectIdentity=ObjectIdentity
hpicfOobmConformance=_HpicfOobmConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,3))
_HpicfOobmCompliance_ObjectIdentity=ObjectIdentity
hpicfOobmCompliance=_HpicfOobmCompliance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,3,1))
_HpicfOobmGroups_ObjectIdentity=ObjectIdentity
hpicfOobmGroups=_HpicfOobmGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2))
snmpTargetAddrEntry.registerAugmentions((_B,_L))
hpicfSnmpTargetAddrIsOobmEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
hpicfOobmScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2,1))
hpicfOobmScalarsGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:hpicfOobmScalarsGroup.setStatus(_A)
hpicfOobmServersGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2,2))
hpicfOobmServersGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:hpicfOobmServersGroup.setStatus(_A)
hpicfSnmpTargetAddrIsOobmGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2,3))
hpicfSnmpTargetAddrIsOobmGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:hpicfSnmpTargetAddrIsOobmGroup.setStatus(_A)
hpicfOobmDefGatewayGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2,4))
hpicfOobmDefGatewayGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:hpicfOobmDefGatewayGroup.setStatus(_A)
hpicfOobmMemberGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,58,3,2,5))
hpicfOobmMemberGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:hpicfOobmMemberGroup.setStatus(_A)
hpicfOobmMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,58,3,1,1))
hpicfOobmMibCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpicfOobmMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpicfOobmServerIndex':HpicfOobmServerIndex,'HpicfOobmServerState':HpicfOobmServerState,'hpicfOobmMIB':hpicfOobmMIB,'hpicfOobmNotifications':hpicfOobmNotifications,'hpicfOobmObjects':hpicfOobmObjects,'hpicfOobmScalars':hpicfOobmScalars,_M:hpicfOobmStatus,'hpicfOobmServers':hpicfOobmServers,'hpicfOobmServerTable':hpicfOobmServerTable,'hpicfOobmServerEntry':hpicfOobmServerEntry,_I:hpicfOobmServerType,_N:hpicfOobmServerListenMode,'hpicfOobmSnmpTargetAddrIsOobm':hpicfOobmSnmpTargetAddrIsOobm,'hpicfSnmpTargetAddrIsOobmTable':hpicfSnmpTargetAddrIsOobmTable,_L:hpicfSnmpTargetAddrIsOobmEntry,_O:hpicfSnmpTargetAddrIsOobm,'hpicfOobmDefGateway':hpicfOobmDefGateway,'hpicfOobmDefGatewayTable':hpicfOobmDefGatewayTable,'hpicfOobmDefGatewayEntry':hpicfOobmDefGatewayEntry,_J:hpicfOobmDefGatewayType,_P:hpicfOobmDefGatewayAddr,'hpicfOobmStackMembers':hpicfOobmStackMembers,'hpicfOobmMemberDefGatewayTable':hpicfOobmMemberDefGatewayTable,'hpicfOobmMemberDefGatewayEntry':hpicfOobmMemberDefGatewayEntry,_K:hpicfOobmMemberDefGatewayType,_Q:hpicfOobmMemberDefGatewayAddr,'hpicfOobmConformance':hpicfOobmConformance,'hpicfOobmCompliance':hpicfOobmCompliance,'hpicfOobmMibCompliance':hpicfOobmMibCompliance,_W:hpicfOobmGroups,_R:hpicfOobmScalarsGroup,_S:hpicfOobmServersGroup,_T:hpicfSnmpTargetAddrIsOobmGroup,_U:hpicfOobmDefGatewayGroup,_V:hpicfOobmMemberGroup})