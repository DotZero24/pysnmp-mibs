_K='wwpLeosDnsServerEntryIpv6Group'
_J='wwpLeosDnsServerInetAddr'
_I='wwpLeosDnsServerInetAddrType'
_H='wwpLeosDnsServerIndex'
_G='disabled'
_F='enabled'
_E='WWP-LEOS-DNS-CLIENT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosDnsClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,16))
if mibBuilder.loadTexts:wwpLeosDnsClientMIB.setRevisions(('2012-03-20 07:00','2003-03-19 10:12'))
_WwpLeosDnsClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBObjects=_WwpLeosDnsClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,1))
_WwpLeosDnsClient_ObjectIdentity=ObjectIdentity
wwpLeosDnsClient=_WwpLeosDnsClient_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,1,1))
class _WwpLeosDnsClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_WwpLeosDnsClientStatus_Type.__name__=_B
_WwpLeosDnsClientStatus_Object=MibScalar
wwpLeosDnsClientStatus=_WwpLeosDnsClientStatus_Object((1,3,6,1,4,1,6141,2,60,16,1,1,1),_WwpLeosDnsClientStatus_Type())
wwpLeosDnsClientStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsClientStatus.setStatus(_A)
_WwpLeosDnsClientDhcpDomainName_Type=DisplayString
_WwpLeosDnsClientDhcpDomainName_Object=MibScalar
wwpLeosDnsClientDhcpDomainName=_WwpLeosDnsClientDhcpDomainName_Object((1,3,6,1,4,1,6141,2,60,16,1,1,2),_WwpLeosDnsClientDhcpDomainName_Type())
wwpLeosDnsClientDhcpDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsClientDhcpDomainName.setStatus(_A)
class _WwpLeosDnsClientDhcpDomainNameState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_WwpLeosDnsClientDhcpDomainNameState_Type.__name__=_B
_WwpLeosDnsClientDhcpDomainNameState_Object=MibScalar
wwpLeosDnsClientDhcpDomainNameState=_WwpLeosDnsClientDhcpDomainNameState_Object((1,3,6,1,4,1,6141,2,60,16,1,1,3),_WwpLeosDnsClientDhcpDomainNameState_Type())
wwpLeosDnsClientDhcpDomainNameState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsClientDhcpDomainNameState.setStatus(_A)
_WwpLeosDnsClientUserDomainName_Type=DisplayString
_WwpLeosDnsClientUserDomainName_Object=MibScalar
wwpLeosDnsClientUserDomainName=_WwpLeosDnsClientUserDomainName_Object((1,3,6,1,4,1,6141,2,60,16,1,1,4),_WwpLeosDnsClientUserDomainName_Type())
wwpLeosDnsClientUserDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsClientUserDomainName.setStatus(_A)
class _WwpLeosDnsClientUserDomainNameState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_WwpLeosDnsClientUserDomainNameState_Type.__name__=_B
_WwpLeosDnsClientUserDomainNameState_Object=MibScalar
wwpLeosDnsClientUserDomainNameState=_WwpLeosDnsClientUserDomainNameState_Object((1,3,6,1,4,1,6141,2,60,16,1,1,5),_WwpLeosDnsClientUserDomainNameState_Type())
wwpLeosDnsClientUserDomainNameState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsClientUserDomainNameState.setStatus(_A)
_WwpLeosDnsServerTable_Object=MibTable
wwpLeosDnsServerTable=_WwpLeosDnsServerTable_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6))
if mibBuilder.loadTexts:wwpLeosDnsServerTable.setStatus(_A)
_WwpLeosDnsServerEntry_Object=MibTableRow
wwpLeosDnsServerEntry=_WwpLeosDnsServerEntry_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1))
wwpLeosDnsServerEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosDnsServerEntry.setStatus(_A)
class _WwpLeosDnsServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosDnsServerIndex_Type.__name__=_B
_WwpLeosDnsServerIndex_Object=MibTableColumn
wwpLeosDnsServerIndex=_WwpLeosDnsServerIndex_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,1),_WwpLeosDnsServerIndex_Type())
wwpLeosDnsServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wwpLeosDnsServerIndex.setStatus(_A)
_WwpLeosDnsServerAddr_Type=IpAddress
_WwpLeosDnsServerAddr_Object=MibTableColumn
wwpLeosDnsServerAddr=_WwpLeosDnsServerAddr_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,2),_WwpLeosDnsServerAddr_Type())
wwpLeosDnsServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsServerAddr.setStatus(_A)
class _WwpLeosDnsServerUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosDnsServerUserPriority_Type.__name__=_B
_WwpLeosDnsServerUserPriority_Object=MibTableColumn
wwpLeosDnsServerUserPriority=_WwpLeosDnsServerUserPriority_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,3),_WwpLeosDnsServerUserPriority_Type())
wwpLeosDnsServerUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsServerUserPriority.setStatus(_A)
class _WwpLeosDnsServerDhcpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosDnsServerDhcpPriority_Type.__name__=_B
_WwpLeosDnsServerDhcpPriority_Object=MibTableColumn
wwpLeosDnsServerDhcpPriority=_WwpLeosDnsServerDhcpPriority_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,4),_WwpLeosDnsServerDhcpPriority_Type())
wwpLeosDnsServerDhcpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsServerDhcpPriority.setStatus(_A)
class _WwpLeosDnsServerScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('dhcp',2),('both',3)))
_WwpLeosDnsServerScope_Type.__name__=_B
_WwpLeosDnsServerScope_Object=MibTableColumn
wwpLeosDnsServerScope=_WwpLeosDnsServerScope_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,5),_WwpLeosDnsServerScope_Type())
wwpLeosDnsServerScope.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsServerScope.setStatus(_A)
_WwpLeosDnsServerStatus_Type=RowStatus
_WwpLeosDnsServerStatus_Object=MibTableColumn
wwpLeosDnsServerStatus=_WwpLeosDnsServerStatus_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,6),_WwpLeosDnsServerStatus_Type())
wwpLeosDnsServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpLeosDnsServerStatus.setStatus(_A)
_WwpLeosDnsServerInetAddrType_Type=InetAddressType
_WwpLeosDnsServerInetAddrType_Object=MibTableColumn
wwpLeosDnsServerInetAddrType=_WwpLeosDnsServerInetAddrType_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,7),_WwpLeosDnsServerInetAddrType_Type())
wwpLeosDnsServerInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsServerInetAddrType.setStatus(_A)
_WwpLeosDnsServerInetAddr_Type=InetAddress
_WwpLeosDnsServerInetAddr_Object=MibTableColumn
wwpLeosDnsServerInetAddr=_WwpLeosDnsServerInetAddr_Object((1,3,6,1,4,1,6141,2,60,16,1,1,6,1,8),_WwpLeosDnsServerInetAddr_Type())
wwpLeosDnsServerInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsServerInetAddr.setStatus(_A)
_WwpLeosDnsServerExtTable_Object=MibTable
wwpLeosDnsServerExtTable=_WwpLeosDnsServerExtTable_Object((1,3,6,1,4,1,6141,2,60,16,1,1,7))
if mibBuilder.loadTexts:wwpLeosDnsServerExtTable.setStatus(_A)
_WwpLeosDnsServerExtEntry_Object=MibTableRow
wwpLeosDnsServerExtEntry=_WwpLeosDnsServerExtEntry_Object((1,3,6,1,4,1,6141,2,60,16,1,1,7,1))
wwpLeosDnsServerExtEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosDnsServerExtEntry.setStatus(_A)
class _WwpLeosDnsServerAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_WwpLeosDnsServerAdminState_Type.__name__=_B
_WwpLeosDnsServerAdminState_Object=MibTableColumn
wwpLeosDnsServerAdminState=_WwpLeosDnsServerAdminState_Object((1,3,6,1,4,1,6141,2,60,16,1,1,7,1,1),_WwpLeosDnsServerAdminState_Type())
wwpLeosDnsServerAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDnsServerAdminState.setStatus(_A)
class _WwpLeosDnsServerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_WwpLeosDnsServerOperState_Type.__name__=_B
_WwpLeosDnsServerOperState_Object=MibTableColumn
wwpLeosDnsServerOperState=_WwpLeosDnsServerOperState_Object((1,3,6,1,4,1,6141,2,60,16,1,1,7,1,2),_WwpLeosDnsServerOperState_Type())
wwpLeosDnsServerOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDnsServerOperState.setStatus(_A)
_WwpLeosDnsClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBNotificationPrefix=_WwpLeosDnsClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,2))
_WwpLeosDnsClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBNotifications=_WwpLeosDnsClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,2,0))
_WwpLeosDnsClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBConformance=_WwpLeosDnsClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,3))
_WwpLeosDnsClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBCompliances=_WwpLeosDnsClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,3,1))
_WwpLeosDnsClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosDnsClientMIBGroups=_WwpLeosDnsClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,16,3,2))
wwpLeosDnsServerEntryIpv6Group=ObjectGroup((1,3,6,1,4,1,6141,2,60,16,3,2,1))
wwpLeosDnsServerEntryIpv6Group.setObjects(*((_E,_I),(_E,_J)))
if mibBuilder.loadTexts:wwpLeosDnsServerEntryIpv6Group.setStatus(_A)
wwpLeosDnsServerEntryCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,16,3,1,1))
wwpLeosDnsServerEntryCompliance.setObjects((_E,_K))
if mibBuilder.loadTexts:wwpLeosDnsServerEntryCompliance.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wwpLeosDnsClientMIB':wwpLeosDnsClientMIB,'wwpLeosDnsClientMIBObjects':wwpLeosDnsClientMIBObjects,'wwpLeosDnsClient':wwpLeosDnsClient,'wwpLeosDnsClientStatus':wwpLeosDnsClientStatus,'wwpLeosDnsClientDhcpDomainName':wwpLeosDnsClientDhcpDomainName,'wwpLeosDnsClientDhcpDomainNameState':wwpLeosDnsClientDhcpDomainNameState,'wwpLeosDnsClientUserDomainName':wwpLeosDnsClientUserDomainName,'wwpLeosDnsClientUserDomainNameState':wwpLeosDnsClientUserDomainNameState,'wwpLeosDnsServerTable':wwpLeosDnsServerTable,'wwpLeosDnsServerEntry':wwpLeosDnsServerEntry,_H:wwpLeosDnsServerIndex,'wwpLeosDnsServerAddr':wwpLeosDnsServerAddr,'wwpLeosDnsServerUserPriority':wwpLeosDnsServerUserPriority,'wwpLeosDnsServerDhcpPriority':wwpLeosDnsServerDhcpPriority,'wwpLeosDnsServerScope':wwpLeosDnsServerScope,'wwpLeosDnsServerStatus':wwpLeosDnsServerStatus,_I:wwpLeosDnsServerInetAddrType,_J:wwpLeosDnsServerInetAddr,'wwpLeosDnsServerExtTable':wwpLeosDnsServerExtTable,'wwpLeosDnsServerExtEntry':wwpLeosDnsServerExtEntry,'wwpLeosDnsServerAdminState':wwpLeosDnsServerAdminState,'wwpLeosDnsServerOperState':wwpLeosDnsServerOperState,'wwpLeosDnsClientMIBNotificationPrefix':wwpLeosDnsClientMIBNotificationPrefix,'wwpLeosDnsClientMIBNotifications':wwpLeosDnsClientMIBNotifications,'wwpLeosDnsClientMIBConformance':wwpLeosDnsClientMIBConformance,'wwpLeosDnsClientMIBCompliances':wwpLeosDnsClientMIBCompliances,'wwpLeosDnsServerEntryCompliance':wwpLeosDnsServerEntryCompliance,'wwpLeosDnsClientMIBGroups':wwpLeosDnsClientMIBGroups,_K:wwpLeosDnsServerEntryIpv6Group})