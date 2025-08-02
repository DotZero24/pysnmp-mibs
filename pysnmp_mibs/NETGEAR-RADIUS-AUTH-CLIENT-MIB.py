_N='obsolete'
_M='agentRadiusServerIndex'
_L='not-accessible'
_K='agentRadiusAccountingServerIndex'
_J='NETGEAR-RADIUS-AUTH-CLIENT-MIB'
_I='disable'
_H='enable'
_G='DisplayString'
_F='read-create'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
fastPathRadius=ModuleIdentity((1,3,6,1,4,1,4526,10,8))
if mibBuilder.loadTexts:fastPathRadius.setRevisions(('2014-04-21 00:00','2011-12-14 00:00','2011-09-26 00:00','2011-01-26 00:00','2007-05-23 00:00','2003-11-21 00:00','2003-05-07 00:00'))
_AgentRadiusConfigGroup_ObjectIdentity=ObjectIdentity
agentRadiusConfigGroup=_AgentRadiusConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,8,1))
class _AgentRadiusMaxTransmit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AgentRadiusMaxTransmit_Type.__name__=_E
_AgentRadiusMaxTransmit_Object=MibScalar
agentRadiusMaxTransmit=_AgentRadiusMaxTransmit_Object((1,3,6,1,4,1,4526,10,8,1,1),_AgentRadiusMaxTransmit_Type())
agentRadiusMaxTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusMaxTransmit.setStatus(_A)
class _AgentRadiusTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusTimeout_Type.__name__=_E
_AgentRadiusTimeout_Object=MibScalar
agentRadiusTimeout=_AgentRadiusTimeout_Object((1,3,6,1,4,1,4526,10,8,1,2),_AgentRadiusTimeout_Type())
agentRadiusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusTimeout.setStatus(_A)
class _AgentRadiusAccountingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusAccountingMode_Type.__name__=_D
_AgentRadiusAccountingMode_Object=MibScalar
agentRadiusAccountingMode=_AgentRadiusAccountingMode_Object((1,3,6,1,4,1,4526,10,8,1,3),_AgentRadiusAccountingMode_Type())
agentRadiusAccountingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingMode.setStatus(_A)
class _AgentRadiusStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusStatsClear_Type.__name__=_D
_AgentRadiusStatsClear_Object=MibScalar
agentRadiusStatsClear=_AgentRadiusStatsClear_Object((1,3,6,1,4,1,4526,10,8,1,4),_AgentRadiusStatsClear_Type())
agentRadiusStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusStatsClear.setStatus(_A)
class _AgentRadiusAccountingIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingIndexNextValid_Type.__name__=_D
_AgentRadiusAccountingIndexNextValid_Object=MibScalar
agentRadiusAccountingIndexNextValid=_AgentRadiusAccountingIndexNextValid_Object((1,3,6,1,4,1,4526,10,8,1,5),_AgentRadiusAccountingIndexNextValid_Type())
agentRadiusAccountingIndexNextValid.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAccountingIndexNextValid.setStatus(_A)
_AgentRadiusAccountingConfigTable_Object=MibTable
agentRadiusAccountingConfigTable=_AgentRadiusAccountingConfigTable_Object((1,3,6,1,4,1,4526,10,8,1,6))
if mibBuilder.loadTexts:agentRadiusAccountingConfigTable.setStatus(_A)
_AgentRadiusAccountingConfigEntry_Object=MibTableRow
agentRadiusAccountingConfigEntry=_AgentRadiusAccountingConfigEntry_Object((1,3,6,1,4,1,4526,10,8,1,6,1))
agentRadiusAccountingConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:agentRadiusAccountingConfigEntry.setStatus(_A)
class _AgentRadiusAccountingServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingServerIndex_Type.__name__=_D
_AgentRadiusAccountingServerIndex_Object=MibTableColumn
agentRadiusAccountingServerIndex=_AgentRadiusAccountingServerIndex_Object((1,3,6,1,4,1,4526,10,8,1,6,1,1),_AgentRadiusAccountingServerIndex_Type())
agentRadiusAccountingServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:agentRadiusAccountingServerIndex.setStatus(_A)
_AgentRadiusAccountingServerAddress_Type=InetAddress
_AgentRadiusAccountingServerAddress_Object=MibTableColumn
agentRadiusAccountingServerAddress=_AgentRadiusAccountingServerAddress_Object((1,3,6,1,4,1,4526,10,8,1,6,1,2),_AgentRadiusAccountingServerAddress_Type())
agentRadiusAccountingServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddress.setStatus(_A)
_AgentRadiusAccountingServerAddressType_Type=InetAddressType
_AgentRadiusAccountingServerAddressType_Object=MibTableColumn
agentRadiusAccountingServerAddressType=_AgentRadiusAccountingServerAddressType_Object((1,3,6,1,4,1,4526,10,8,1,6,1,3),_AgentRadiusAccountingServerAddressType_Type())
agentRadiusAccountingServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddressType.setStatus(_A)
class _AgentRadiusAccountingPort_Type(Unsigned32):defaultValue=1813;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentRadiusAccountingPort_Type.__name__=_E
_AgentRadiusAccountingPort_Object=MibTableColumn
agentRadiusAccountingPort=_AgentRadiusAccountingPort_Object((1,3,6,1,4,1,4526,10,8,1,6,1,4),_AgentRadiusAccountingPort_Type())
agentRadiusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingPort.setStatus(_A)
class _AgentRadiusAccountingSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentRadiusAccountingSecret_Type.__name__=_G
_AgentRadiusAccountingSecret_Object=MibTableColumn
agentRadiusAccountingSecret=_AgentRadiusAccountingSecret_Object((1,3,6,1,4,1,4526,10,8,1,6,1,5),_AgentRadiusAccountingSecret_Type())
agentRadiusAccountingSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingSecret.setStatus(_A)
_AgentRadiusAccountingStatus_Type=RowStatus
_AgentRadiusAccountingStatus_Object=MibTableColumn
agentRadiusAccountingStatus=_AgentRadiusAccountingStatus_Object((1,3,6,1,4,1,4526,10,8,1,6,1,6),_AgentRadiusAccountingStatus_Type())
agentRadiusAccountingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingStatus.setStatus(_A)
class _AgentRadiusAccountingServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusAccountingServerName_Type.__name__=_G
_AgentRadiusAccountingServerName_Object=MibTableColumn
agentRadiusAccountingServerName=_AgentRadiusAccountingServerName_Object((1,3,6,1,4,1,4526,10,8,1,6,1,7),_AgentRadiusAccountingServerName_Type())
agentRadiusAccountingServerName.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingServerName.setStatus(_A)
class _AgentRadiusServerIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndexNextValid_Type.__name__=_D
_AgentRadiusServerIndexNextValid_Object=MibScalar
agentRadiusServerIndexNextValid=_AgentRadiusServerIndexNextValid_Object((1,3,6,1,4,1,4526,10,8,1,7),_AgentRadiusServerIndexNextValid_Type())
agentRadiusServerIndexNextValid.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerIndexNextValid.setStatus(_A)
_AgentRadiusServerConfigTable_Object=MibTable
agentRadiusServerConfigTable=_AgentRadiusServerConfigTable_Object((1,3,6,1,4,1,4526,10,8,1,8))
if mibBuilder.loadTexts:agentRadiusServerConfigTable.setStatus(_A)
_AgentRadiusServerConfigEntry_Object=MibTableRow
agentRadiusServerConfigEntry=_AgentRadiusServerConfigEntry_Object((1,3,6,1,4,1,4526,10,8,1,8,1))
agentRadiusServerConfigEntry.setIndexNames((0,_J,_M))
if mibBuilder.loadTexts:agentRadiusServerConfigEntry.setStatus(_A)
class _AgentRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndex_Type.__name__=_D
_AgentRadiusServerIndex_Object=MibTableColumn
agentRadiusServerIndex=_AgentRadiusServerIndex_Object((1,3,6,1,4,1,4526,10,8,1,8,1,1),_AgentRadiusServerIndex_Type())
agentRadiusServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:agentRadiusServerIndex.setStatus(_A)
_AgentRadiusServerAddress_Type=InetAddress
_AgentRadiusServerAddress_Object=MibTableColumn
agentRadiusServerAddress=_AgentRadiusServerAddress_Object((1,3,6,1,4,1,4526,10,8,1,8,1,2),_AgentRadiusServerAddress_Type())
agentRadiusServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerAddress.setStatus(_N)
_AgentRadiusServerAddressType_Type=InetAddressType
_AgentRadiusServerAddressType_Object=MibTableColumn
agentRadiusServerAddressType=_AgentRadiusServerAddressType_Object((1,3,6,1,4,1,4526,10,8,1,8,1,3),_AgentRadiusServerAddressType_Type())
agentRadiusServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerAddressType.setStatus(_A)
class _AgentRadiusServerPort_Type(Unsigned32):defaultValue=1812;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentRadiusServerPort_Type.__name__=_E
_AgentRadiusServerPort_Object=MibTableColumn
agentRadiusServerPort=_AgentRadiusServerPort_Object((1,3,6,1,4,1,4526,10,8,1,8,1,4),_AgentRadiusServerPort_Type())
agentRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPort.setStatus(_A)
class _AgentRadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentRadiusServerSecret_Type.__name__=_G
_AgentRadiusServerSecret_Object=MibTableColumn
agentRadiusServerSecret=_AgentRadiusServerSecret_Object((1,3,6,1,4,1,4526,10,8,1,8,1,5),_AgentRadiusServerSecret_Type())
agentRadiusServerSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSecret.setStatus(_A)
class _AgentRadiusServerPrimaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerPrimaryMode_Type.__name__=_D
_AgentRadiusServerPrimaryMode_Object=MibTableColumn
agentRadiusServerPrimaryMode=_AgentRadiusServerPrimaryMode_Object((1,3,6,1,4,1,4526,10,8,1,8,1,6),_AgentRadiusServerPrimaryMode_Type())
agentRadiusServerPrimaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPrimaryMode.setStatus(_A)
class _AgentRadiusServerCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AgentRadiusServerCurrentMode_Type.__name__=_D
_AgentRadiusServerCurrentMode_Object=MibTableColumn
agentRadiusServerCurrentMode=_AgentRadiusServerCurrentMode_Object((1,3,6,1,4,1,4526,10,8,1,8,1,7),_AgentRadiusServerCurrentMode_Type())
agentRadiusServerCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerCurrentMode.setStatus(_A)
class _AgentRadiusServerMsgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerMsgAuth_Type.__name__=_D
_AgentRadiusServerMsgAuth_Object=MibTableColumn
agentRadiusServerMsgAuth=_AgentRadiusServerMsgAuth_Object((1,3,6,1,4,1,4526,10,8,1,8,1,8),_AgentRadiusServerMsgAuth_Type())
agentRadiusServerMsgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerMsgAuth.setStatus(_A)
_AgentRadiusServerRowStatus_Type=RowStatus
_AgentRadiusServerRowStatus_Object=MibTableColumn
agentRadiusServerRowStatus=_AgentRadiusServerRowStatus_Object((1,3,6,1,4,1,4526,10,8,1,8,1,9),_AgentRadiusServerRowStatus_Type())
agentRadiusServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerRowStatus.setStatus(_A)
class _AgentRadiusServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusServerName_Type.__name__=_G
_AgentRadiusServerName_Object=MibTableColumn
agentRadiusServerName=_AgentRadiusServerName_Object((1,3,6,1,4,1,4526,10,8,1,8,1,10),_AgentRadiusServerName_Type())
agentRadiusServerName.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerName.setStatus(_A)
_AgentRadiusServerInetAddress_Type=InetAddress
_AgentRadiusServerInetAddress_Object=MibTableColumn
agentRadiusServerInetAddress=_AgentRadiusServerInetAddress_Object((1,3,6,1,4,1,4526,10,8,1,8,1,11),_AgentRadiusServerInetAddress_Type())
agentRadiusServerInetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerInetAddress.setStatus(_A)
class _AgentRadiusServerTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusServerTimeout_Type.__name__=_E
_AgentRadiusServerTimeout_Object=MibTableColumn
agentRadiusServerTimeout=_AgentRadiusServerTimeout_Object((1,3,6,1,4,1,4526,10,8,1,8,1,12),_AgentRadiusServerTimeout_Type())
agentRadiusServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerTimeout.setStatus(_A)
class _AgentRadiusServerRetransmit_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentRadiusServerRetransmit_Type.__name__=_E
_AgentRadiusServerRetransmit_Object=MibTableColumn
agentRadiusServerRetransmit=_AgentRadiusServerRetransmit_Object((1,3,6,1,4,1,4526,10,8,1,8,1,13),_AgentRadiusServerRetransmit_Type())
agentRadiusServerRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerRetransmit.setStatus(_A)
class _AgentRadiusServerDeadtime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusServerDeadtime_Type.__name__=_E
_AgentRadiusServerDeadtime_Object=MibTableColumn
agentRadiusServerDeadtime=_AgentRadiusServerDeadtime_Object((1,3,6,1,4,1,4526,10,8,1,8,1,14),_AgentRadiusServerDeadtime_Type())
agentRadiusServerDeadtime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerDeadtime.setStatus(_A)
_AgentRadiusServerSourceIPAddr_Type=IpAddress
_AgentRadiusServerSourceIPAddr_Object=MibTableColumn
agentRadiusServerSourceIPAddr=_AgentRadiusServerSourceIPAddr_Object((1,3,6,1,4,1,4526,10,8,1,8,1,15),_AgentRadiusServerSourceIPAddr_Type())
agentRadiusServerSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSourceIPAddr.setStatus(_A)
class _AgentRadiusServerPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusServerPriority_Type.__name__=_E
_AgentRadiusServerPriority_Object=MibTableColumn
agentRadiusServerPriority=_AgentRadiusServerPriority_Object((1,3,6,1,4,1,4526,10,8,1,8,1,16),_AgentRadiusServerPriority_Type())
agentRadiusServerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPriority.setStatus(_A)
class _AgentRadiusServerUsageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('login',2),('dot1x',3)))
_AgentRadiusServerUsageType_Type.__name__=_D
_AgentRadiusServerUsageType_Object=MibTableColumn
agentRadiusServerUsageType=_AgentRadiusServerUsageType_Object((1,3,6,1,4,1,4526,10,8,1,8,1,17),_AgentRadiusServerUsageType_Type())
agentRadiusServerUsageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerUsageType.setStatus(_A)
_AgentRadiusAuthenticationServers_Type=Unsigned32
_AgentRadiusAuthenticationServers_Object=MibScalar
agentRadiusAuthenticationServers=_AgentRadiusAuthenticationServers_Object((1,3,6,1,4,1,4526,10,8,1,9),_AgentRadiusAuthenticationServers_Type())
agentRadiusAuthenticationServers.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAuthenticationServers.setStatus(_A)
_AgentRadiusAccountingServers_Type=Unsigned32
_AgentRadiusAccountingServers_Object=MibScalar
agentRadiusAccountingServers=_AgentRadiusAccountingServers_Object((1,3,6,1,4,1,4526,10,8,1,10),_AgentRadiusAccountingServers_Type())
agentRadiusAccountingServers.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAccountingServers.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroups_Type=Unsigned32
_AgentRadiusNamedAuthenticationServerGroups_Object=MibScalar
agentRadiusNamedAuthenticationServerGroups=_AgentRadiusNamedAuthenticationServerGroups_Object((1,3,6,1,4,1,4526,10,8,1,11),_AgentRadiusNamedAuthenticationServerGroups_Type())
agentRadiusNamedAuthenticationServerGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroups.setStatus(_A)
_AgentRadiusNamedAccountingServerGroups_Type=Unsigned32
_AgentRadiusNamedAccountingServerGroups_Object=MibScalar
agentRadiusNamedAccountingServerGroups=_AgentRadiusNamedAccountingServerGroups_Object((1,3,6,1,4,1,4526,10,8,1,12),_AgentRadiusNamedAccountingServerGroups_Type())
agentRadiusNamedAccountingServerGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroups.setStatus(_A)
class _AgentRadiusDeadTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusDeadTime_Type.__name__=_E
_AgentRadiusDeadTime_Object=MibScalar
agentRadiusDeadTime=_AgentRadiusDeadTime_Object((1,3,6,1,4,1,4526,10,8,1,13),_AgentRadiusDeadTime_Type())
agentRadiusDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusDeadTime.setStatus(_A)
class _AgentRadiusServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentRadiusServerKey_Type.__name__=_G
_AgentRadiusServerKey_Object=MibScalar
agentRadiusServerKey=_AgentRadiusServerKey_Object((1,3,6,1,4,1,4526,10,8,1,14),_AgentRadiusServerKey_Type())
agentRadiusServerKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerKey.setStatus(_N)
_AgentRadiusSourceIPAddr_Type=IpAddress
_AgentRadiusSourceIPAddr_Object=MibScalar
agentRadiusSourceIPAddr=_AgentRadiusSourceIPAddr_Object((1,3,6,1,4,1,4526,10,8,1,15),_AgentRadiusSourceIPAddr_Type())
agentRadiusSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusSourceIPAddr.setStatus(_A)
_AgentRadiusNasIpAddress_Type=IpAddress
_AgentRadiusNasIpAddress_Object=MibScalar
agentRadiusNasIpAddress=_AgentRadiusNasIpAddress_Object((1,3,6,1,4,1,4526,10,8,1,16),_AgentRadiusNasIpAddress_Type())
agentRadiusNasIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNasIpAddress.setStatus(_A)
class _AgentAuthorizationNetworkRadiusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_AgentAuthorizationNetworkRadiusMode_Type.__name__=_D
_AgentAuthorizationNetworkRadiusMode_Object=MibScalar
agentAuthorizationNetworkRadiusMode=_AgentAuthorizationNetworkRadiusMode_Object((1,3,6,1,4,1,4526,10,8,1,17),_AgentAuthorizationNetworkRadiusMode_Type())
agentAuthorizationNetworkRadiusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthorizationNetworkRadiusMode.setStatus(_A)
_AgentRadiusSourceInterface_Type=InterfaceIndexOrZero
_AgentRadiusSourceInterface_Object=MibScalar
agentRadiusSourceInterface=_AgentRadiusSourceInterface_Object((1,3,6,1,4,1,4526,10,8,1,18),_AgentRadiusSourceInterface_Type())
agentRadiusSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusSourceInterface.setStatus(_A)
_AgentDasRequestsReceived_Type=Unsigned32
_AgentDasRequestsReceived_Object=MibScalar
agentDasRequestsReceived=_AgentDasRequestsReceived_Object((1,3,6,1,4,1,4526,10,8,1,19),_AgentDasRequestsReceived_Type())
agentDasRequestsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsReceived.setStatus(_A)
_AgentDasACKResponsesSent_Type=Unsigned32
_AgentDasACKResponsesSent_Object=MibScalar
agentDasACKResponsesSent=_AgentDasACKResponsesSent_Object((1,3,6,1,4,1,4526,10,8,1,20),_AgentDasACKResponsesSent_Type())
agentDasACKResponsesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasACKResponsesSent.setStatus(_A)
_AgentDasNAKResponsesSent_Type=Unsigned32
_AgentDasNAKResponsesSent_Object=MibScalar
agentDasNAKResponsesSent=_AgentDasNAKResponsesSent_Object((1,3,6,1,4,1,4526,10,8,1,21),_AgentDasNAKResponsesSent_Type())
agentDasNAKResponsesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasNAKResponsesSent.setStatus(_A)
_AgentDasRequestsIgnored_Type=Unsigned32
_AgentDasRequestsIgnored_Object=MibScalar
agentDasRequestsIgnored=_AgentDasRequestsIgnored_Object((1,3,6,1,4,1,4526,10,8,1,22),_AgentDasRequestsIgnored_Type())
agentDasRequestsIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsIgnored.setStatus(_A)
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Type=Unsigned32
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Object=MibScalar
agentDasRequestsWithMissingOrUnsupportedAttribute=_AgentDasRequestsWithMissingOrUnsupportedAttribute_Object((1,3,6,1,4,1,4526,10,8,1,23),_AgentDasRequestsWithMissingOrUnsupportedAttribute_Type())
agentDasRequestsWithMissingOrUnsupportedAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsWithMissingOrUnsupportedAttribute.setStatus(_A)
_AgentDasRequestsWithSessionContextNotFound_Type=Unsigned32
_AgentDasRequestsWithSessionContextNotFound_Object=MibScalar
agentDasRequestsWithSessionContextNotFound=_AgentDasRequestsWithSessionContextNotFound_Object((1,3,6,1,4,1,4526,10,8,1,24),_AgentDasRequestsWithSessionContextNotFound_Type())
agentDasRequestsWithSessionContextNotFound.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsWithSessionContextNotFound.setStatus(_A)
_AgentDasRequestsWithInvalidAttributeValue_Type=Unsigned32
_AgentDasRequestsWithInvalidAttributeValue_Object=MibScalar
agentDasRequestsWithInvalidAttributeValue=_AgentDasRequestsWithInvalidAttributeValue_Object((1,3,6,1,4,1,4526,10,8,1,25),_AgentDasRequestsWithInvalidAttributeValue_Type())
agentDasRequestsWithInvalidAttributeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsWithInvalidAttributeValue.setStatus(_A)
_AgentDasRequestsAdministrativelyProhibited_Type=Unsigned32
_AgentDasRequestsAdministrativelyProhibited_Object=MibScalar
agentDasRequestsAdministrativelyProhibited=_AgentDasRequestsAdministrativelyProhibited_Object((1,3,6,1,4,1,4526,10,8,1,26),_AgentDasRequestsAdministrativelyProhibited_Type())
agentDasRequestsAdministrativelyProhibited.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDasRequestsAdministrativelyProhibited.setStatus(_A)
class _AgentRadiusServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentRadiusServicePortSrcInterface_Type.__name__=_D
_AgentRadiusServicePortSrcInterface_Object=MibScalar
agentRadiusServicePortSrcInterface=_AgentRadiusServicePortSrcInterface_Object((1,3,6,1,4,1,4526,10,8,1,27),_AgentRadiusServicePortSrcInterface_Type())
agentRadiusServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServicePortSrcInterface.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'fastPathRadius':fastPathRadius,'agentRadiusConfigGroup':agentRadiusConfigGroup,'agentRadiusMaxTransmit':agentRadiusMaxTransmit,'agentRadiusTimeout':agentRadiusTimeout,'agentRadiusAccountingMode':agentRadiusAccountingMode,'agentRadiusStatsClear':agentRadiusStatsClear,'agentRadiusAccountingIndexNextValid':agentRadiusAccountingIndexNextValid,'agentRadiusAccountingConfigTable':agentRadiusAccountingConfigTable,'agentRadiusAccountingConfigEntry':agentRadiusAccountingConfigEntry,_K:agentRadiusAccountingServerIndex,'agentRadiusAccountingServerAddress':agentRadiusAccountingServerAddress,'agentRadiusAccountingServerAddressType':agentRadiusAccountingServerAddressType,'agentRadiusAccountingPort':agentRadiusAccountingPort,'agentRadiusAccountingSecret':agentRadiusAccountingSecret,'agentRadiusAccountingStatus':agentRadiusAccountingStatus,'agentRadiusAccountingServerName':agentRadiusAccountingServerName,'agentRadiusServerIndexNextValid':agentRadiusServerIndexNextValid,'agentRadiusServerConfigTable':agentRadiusServerConfigTable,'agentRadiusServerConfigEntry':agentRadiusServerConfigEntry,_M:agentRadiusServerIndex,'agentRadiusServerAddress':agentRadiusServerAddress,'agentRadiusServerAddressType':agentRadiusServerAddressType,'agentRadiusServerPort':agentRadiusServerPort,'agentRadiusServerSecret':agentRadiusServerSecret,'agentRadiusServerPrimaryMode':agentRadiusServerPrimaryMode,'agentRadiusServerCurrentMode':agentRadiusServerCurrentMode,'agentRadiusServerMsgAuth':agentRadiusServerMsgAuth,'agentRadiusServerRowStatus':agentRadiusServerRowStatus,'agentRadiusServerName':agentRadiusServerName,'agentRadiusServerInetAddress':agentRadiusServerInetAddress,'agentRadiusServerTimeout':agentRadiusServerTimeout,'agentRadiusServerRetransmit':agentRadiusServerRetransmit,'agentRadiusServerDeadtime':agentRadiusServerDeadtime,'agentRadiusServerSourceIPAddr':agentRadiusServerSourceIPAddr,'agentRadiusServerPriority':agentRadiusServerPriority,'agentRadiusServerUsageType':agentRadiusServerUsageType,'agentRadiusAuthenticationServers':agentRadiusAuthenticationServers,'agentRadiusAccountingServers':agentRadiusAccountingServers,'agentRadiusNamedAuthenticationServerGroups':agentRadiusNamedAuthenticationServerGroups,'agentRadiusNamedAccountingServerGroups':agentRadiusNamedAccountingServerGroups,'agentRadiusDeadTime':agentRadiusDeadTime,'agentRadiusServerKey':agentRadiusServerKey,'agentRadiusSourceIPAddr':agentRadiusSourceIPAddr,'agentRadiusNasIpAddress':agentRadiusNasIpAddress,'agentAuthorizationNetworkRadiusMode':agentAuthorizationNetworkRadiusMode,'agentRadiusSourceInterface':agentRadiusSourceInterface,'agentDasRequestsReceived':agentDasRequestsReceived,'agentDasACKResponsesSent':agentDasACKResponsesSent,'agentDasNAKResponsesSent':agentDasNAKResponsesSent,'agentDasRequestsIgnored':agentDasRequestsIgnored,'agentDasRequestsWithMissingOrUnsupportedAttribute':agentDasRequestsWithMissingOrUnsupportedAttribute,'agentDasRequestsWithSessionContextNotFound':agentDasRequestsWithSessionContextNotFound,'agentDasRequestsWithInvalidAttributeValue':agentDasRequestsWithInvalidAttributeValue,'agentDasRequestsAdministrativelyProhibited':agentDasRequestsAdministrativelyProhibited,'agentRadiusServicePortSrcInterface':agentRadiusServicePortSrcInterface})