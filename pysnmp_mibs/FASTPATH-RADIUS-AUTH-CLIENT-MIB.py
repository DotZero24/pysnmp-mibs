_N='agentRadiusAccountingServerIndex'
_M='not-accessible'
_L='agentRadiusServerIndex'
_K='obsolete'
_J='FASTPATH-RADIUS-AUTH-CLIENT-MIB'
_I='disable'
_H='enable'
_G='DisplayString'
_F='read-only'
_E='read-create'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
fastPathRadius=ModuleIdentity((1,3,6,1,4,1,4413,1,1,8))
if mibBuilder.loadTexts:fastPathRadius.setRevisions(('2007-05-23 00:00','2003-11-21 00:00','2003-05-07 00:00'))
_AgentRadiusConfigGroup_ObjectIdentity=ObjectIdentity
agentRadiusConfigGroup=_AgentRadiusConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,8,1))
class _AgentRadiusRetransmit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AgentRadiusRetransmit_Type.__name__=_D
_AgentRadiusRetransmit_Object=MibScalar
agentRadiusRetransmit=_AgentRadiusRetransmit_Object((1,3,6,1,4,1,4413,1,1,8,1,1),_AgentRadiusRetransmit_Type())
agentRadiusRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusRetransmit.setStatus(_A)
class _AgentRadiusTimeout_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusTimeout_Type.__name__=_D
_AgentRadiusTimeout_Object=MibScalar
agentRadiusTimeout=_AgentRadiusTimeout_Object((1,3,6,1,4,1,4413,1,1,8,1,2),_AgentRadiusTimeout_Type())
agentRadiusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusTimeout.setStatus(_A)
class _AgentRadiusDeadTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusDeadTime_Type.__name__=_D
_AgentRadiusDeadTime_Object=MibScalar
agentRadiusDeadTime=_AgentRadiusDeadTime_Object((1,3,6,1,4,1,4413,1,1,8,1,3),_AgentRadiusDeadTime_Type())
agentRadiusDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusDeadTime.setStatus(_A)
class _AgentRadiusServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentRadiusServerKey_Type.__name__=_G
_AgentRadiusServerKey_Object=MibScalar
agentRadiusServerKey=_AgentRadiusServerKey_Object((1,3,6,1,4,1,4413,1,1,8,1,4),_AgentRadiusServerKey_Type())
agentRadiusServerKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerKey.setStatus(_K)
_AgentRadiusSourceIPAddr_Type=IpAddress
_AgentRadiusSourceIPAddr_Object=MibScalar
agentRadiusSourceIPAddr=_AgentRadiusSourceIPAddr_Object((1,3,6,1,4,1,4413,1,1,8,1,5),_AgentRadiusSourceIPAddr_Type())
agentRadiusSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusSourceIPAddr.setStatus(_A)
class _AgentRadiusServerIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndexNextValid_Type.__name__=_C
_AgentRadiusServerIndexNextValid_Object=MibScalar
agentRadiusServerIndexNextValid=_AgentRadiusServerIndexNextValid_Object((1,3,6,1,4,1,4413,1,1,8,1,6),_AgentRadiusServerIndexNextValid_Type())
agentRadiusServerIndexNextValid.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerIndexNextValid.setStatus(_A)
_AgentRadiusServerConfigTable_Object=MibTable
agentRadiusServerConfigTable=_AgentRadiusServerConfigTable_Object((1,3,6,1,4,1,4413,1,1,8,1,7))
if mibBuilder.loadTexts:agentRadiusServerConfigTable.setStatus(_A)
_AgentRadiusServerConfigEntry_Object=MibTableRow
agentRadiusServerConfigEntry=_AgentRadiusServerConfigEntry_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1))
agentRadiusServerConfigEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:agentRadiusServerConfigEntry.setStatus(_A)
class _AgentRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndex_Type.__name__=_C
_AgentRadiusServerIndex_Object=MibTableColumn
agentRadiusServerIndex=_AgentRadiusServerIndex_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,1),_AgentRadiusServerIndex_Type())
agentRadiusServerIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentRadiusServerIndex.setStatus(_A)
_AgentRadiusServerAddress_Type=InetAddress
_AgentRadiusServerAddress_Object=MibTableColumn
agentRadiusServerAddress=_AgentRadiusServerAddress_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,2),_AgentRadiusServerAddress_Type())
agentRadiusServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusServerAddress.setStatus(_K)
class _AgentRadiusServerPort_Type(Unsigned32):defaultValue=1812;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusServerPort_Type.__name__=_D
_AgentRadiusServerPort_Object=MibTableColumn
agentRadiusServerPort=_AgentRadiusServerPort_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,3),_AgentRadiusServerPort_Type())
agentRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPort.setStatus(_A)
class _AgentRadiusServerTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusServerTimeout_Type.__name__=_D
_AgentRadiusServerTimeout_Object=MibTableColumn
agentRadiusServerTimeout=_AgentRadiusServerTimeout_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,4),_AgentRadiusServerTimeout_Type())
agentRadiusServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerTimeout.setStatus(_A)
class _AgentRadiusServerRetransmit_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentRadiusServerRetransmit_Type.__name__=_D
_AgentRadiusServerRetransmit_Object=MibTableColumn
agentRadiusServerRetransmit=_AgentRadiusServerRetransmit_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,5),_AgentRadiusServerRetransmit_Type())
agentRadiusServerRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerRetransmit.setStatus(_A)
class _AgentRadiusServerDeadtime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusServerDeadtime_Type.__name__=_D
_AgentRadiusServerDeadtime_Object=MibTableColumn
agentRadiusServerDeadtime=_AgentRadiusServerDeadtime_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,6),_AgentRadiusServerDeadtime_Type())
agentRadiusServerDeadtime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerDeadtime.setStatus(_A)
_AgentRadiusServerSourceIPAddr_Type=IpAddress
_AgentRadiusServerSourceIPAddr_Object=MibTableColumn
agentRadiusServerSourceIPAddr=_AgentRadiusServerSourceIPAddr_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,7),_AgentRadiusServerSourceIPAddr_Type())
agentRadiusServerSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSourceIPAddr.setStatus(_A)
class _AgentRadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AgentRadiusServerSecret_Type.__name__=_G
_AgentRadiusServerSecret_Object=MibTableColumn
agentRadiusServerSecret=_AgentRadiusServerSecret_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,8),_AgentRadiusServerSecret_Type())
agentRadiusServerSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSecret.setStatus(_A)
class _AgentRadiusServerPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusServerPriority_Type.__name__=_D
_AgentRadiusServerPriority_Object=MibTableColumn
agentRadiusServerPriority=_AgentRadiusServerPriority_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,9),_AgentRadiusServerPriority_Type())
agentRadiusServerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPriority.setStatus(_A)
class _AgentRadiusServerUsageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('login',2),('dot1x',3)))
_AgentRadiusServerUsageType_Type.__name__=_C
_AgentRadiusServerUsageType_Object=MibTableColumn
agentRadiusServerUsageType=_AgentRadiusServerUsageType_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,10),_AgentRadiusServerUsageType_Type())
agentRadiusServerUsageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerUsageType.setStatus(_A)
_AgentRadiusServerAddressRowStatus_Type=RowStatus
_AgentRadiusServerAddressRowStatus_Object=MibTableColumn
agentRadiusServerAddressRowStatus=_AgentRadiusServerAddressRowStatus_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,11),_AgentRadiusServerAddressRowStatus_Type())
agentRadiusServerAddressRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusServerAddressRowStatus.setStatus(_A)
class _AgentRadiusServerPrimaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerPrimaryMode_Type.__name__=_C
_AgentRadiusServerPrimaryMode_Object=MibTableColumn
agentRadiusServerPrimaryMode=_AgentRadiusServerPrimaryMode_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,12),_AgentRadiusServerPrimaryMode_Type())
agentRadiusServerPrimaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPrimaryMode.setStatus(_A)
class _AgentRadiusServerCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AgentRadiusServerCurrentMode_Type.__name__=_C
_AgentRadiusServerCurrentMode_Object=MibTableColumn
agentRadiusServerCurrentMode=_AgentRadiusServerCurrentMode_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,13),_AgentRadiusServerCurrentMode_Type())
agentRadiusServerCurrentMode.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusServerCurrentMode.setStatus(_A)
class _AgentRadiusServerMsgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerMsgAuth_Type.__name__=_C
_AgentRadiusServerMsgAuth_Object=MibTableColumn
agentRadiusServerMsgAuth=_AgentRadiusServerMsgAuth_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,14),_AgentRadiusServerMsgAuth_Type())
agentRadiusServerMsgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerMsgAuth.setStatus(_A)
class _AgentRadiusServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusServerName_Type.__name__=_G
_AgentRadiusServerName_Object=MibTableColumn
agentRadiusServerName=_AgentRadiusServerName_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,15),_AgentRadiusServerName_Type())
agentRadiusServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusServerName.setStatus(_A)
_AgentRadiusServerInetAddress_Type=InetAddress
_AgentRadiusServerInetAddress_Object=MibTableColumn
agentRadiusServerInetAddress=_AgentRadiusServerInetAddress_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,16),_AgentRadiusServerInetAddress_Type())
agentRadiusServerInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusServerInetAddress.setStatus(_A)
_AgentRadiusServerAddressType_Type=InetAddressType
_AgentRadiusServerAddressType_Object=MibTableColumn
agentRadiusServerAddressType=_AgentRadiusServerAddressType_Object((1,3,6,1,4,1,4413,1,1,8,1,7,1,17),_AgentRadiusServerAddressType_Type())
agentRadiusServerAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusServerAddressType.setStatus(_A)
_AgentRadiusNasIpAddress_Type=IpAddress
_AgentRadiusNasIpAddress_Object=MibScalar
agentRadiusNasIpAddress=_AgentRadiusNasIpAddress_Object((1,3,6,1,4,1,4413,1,1,8,1,8),_AgentRadiusNasIpAddress_Type())
agentRadiusNasIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNasIpAddress.setStatus(_A)
class _AgentAuthorizationNetworkRadiusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_AgentAuthorizationNetworkRadiusMode_Type.__name__=_C
_AgentAuthorizationNetworkRadiusMode_Object=MibScalar
agentAuthorizationNetworkRadiusMode=_AgentAuthorizationNetworkRadiusMode_Object((1,3,6,1,4,1,4413,1,1,8,1,9),_AgentAuthorizationNetworkRadiusMode_Type())
agentAuthorizationNetworkRadiusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthorizationNetworkRadiusMode.setStatus(_A)
class _AgentRadiusAccountingIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingIndexNextValid_Type.__name__=_C
_AgentRadiusAccountingIndexNextValid_Object=MibScalar
agentRadiusAccountingIndexNextValid=_AgentRadiusAccountingIndexNextValid_Object((1,3,6,1,4,1,4413,1,1,8,1,10),_AgentRadiusAccountingIndexNextValid_Type())
agentRadiusAccountingIndexNextValid.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingIndexNextValid.setStatus(_A)
_AgentRadiusAccountingConfigTable_Object=MibTable
agentRadiusAccountingConfigTable=_AgentRadiusAccountingConfigTable_Object((1,3,6,1,4,1,4413,1,1,8,1,11))
if mibBuilder.loadTexts:agentRadiusAccountingConfigTable.setStatus(_A)
_AgentRadiusAccountingConfigEntry_Object=MibTableRow
agentRadiusAccountingConfigEntry=_AgentRadiusAccountingConfigEntry_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1))
agentRadiusAccountingConfigEntry.setIndexNames((0,_J,_N))
if mibBuilder.loadTexts:agentRadiusAccountingConfigEntry.setStatus(_A)
class _AgentRadiusAccountingServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingServerIndex_Type.__name__=_C
_AgentRadiusAccountingServerIndex_Object=MibTableColumn
agentRadiusAccountingServerIndex=_AgentRadiusAccountingServerIndex_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,1),_AgentRadiusAccountingServerIndex_Type())
agentRadiusAccountingServerIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentRadiusAccountingServerIndex.setStatus(_A)
_AgentRadiusAccountingServerAddress_Type=InetAddress
_AgentRadiusAccountingServerAddress_Object=MibTableColumn
agentRadiusAccountingServerAddress=_AgentRadiusAccountingServerAddress_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,2),_AgentRadiusAccountingServerAddress_Type())
agentRadiusAccountingServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddress.setStatus(_A)
_AgentRadiusAccountingServerAddressType_Type=InetAddressType
_AgentRadiusAccountingServerAddressType_Object=MibTableColumn
agentRadiusAccountingServerAddressType=_AgentRadiusAccountingServerAddressType_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,3),_AgentRadiusAccountingServerAddressType_Type())
agentRadiusAccountingServerAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddressType.setStatus(_A)
class _AgentRadiusAccountingPort_Type(Unsigned32):defaultValue=1813;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusAccountingPort_Type.__name__=_D
_AgentRadiusAccountingPort_Object=MibTableColumn
agentRadiusAccountingPort=_AgentRadiusAccountingPort_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,4),_AgentRadiusAccountingPort_Type())
agentRadiusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingPort.setStatus(_A)
class _AgentRadiusAccountingSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AgentRadiusAccountingSecret_Type.__name__=_G
_AgentRadiusAccountingSecret_Object=MibTableColumn
agentRadiusAccountingSecret=_AgentRadiusAccountingSecret_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,5),_AgentRadiusAccountingSecret_Type())
agentRadiusAccountingSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingSecret.setStatus(_A)
_AgentRadiusAccountingStatus_Type=RowStatus
_AgentRadiusAccountingStatus_Object=MibTableColumn
agentRadiusAccountingStatus=_AgentRadiusAccountingStatus_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,6),_AgentRadiusAccountingStatus_Type())
agentRadiusAccountingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusAccountingStatus.setStatus(_A)
class _AgentRadiusAccountingServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusAccountingServerName_Type.__name__=_G
_AgentRadiusAccountingServerName_Object=MibTableColumn
agentRadiusAccountingServerName=_AgentRadiusAccountingServerName_Object((1,3,6,1,4,1,4413,1,1,8,1,11,1,7),_AgentRadiusAccountingServerName_Type())
agentRadiusAccountingServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRadiusAccountingServerName.setStatus(_A)
class _AgentRadiusAccountingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusAccountingMode_Type.__name__=_C
_AgentRadiusAccountingMode_Object=MibScalar
agentRadiusAccountingMode=_AgentRadiusAccountingMode_Object((1,3,6,1,4,1,4413,1,1,8,1,12),_AgentRadiusAccountingMode_Type())
agentRadiusAccountingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingMode.setStatus(_A)
class _AgentRadiusStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusStatsClear_Type.__name__=_C
_AgentRadiusStatsClear_Object=MibScalar
agentRadiusStatsClear=_AgentRadiusStatsClear_Object((1,3,6,1,4,1,4413,1,1,8,1,13),_AgentRadiusStatsClear_Type())
agentRadiusStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusStatsClear.setStatus(_A)
_AgentRadiusAuthenticationServers_Type=Unsigned32
_AgentRadiusAuthenticationServers_Object=MibScalar
agentRadiusAuthenticationServers=_AgentRadiusAuthenticationServers_Object((1,3,6,1,4,1,4413,1,1,8,1,14),_AgentRadiusAuthenticationServers_Type())
agentRadiusAuthenticationServers.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAuthenticationServers.setStatus(_A)
_AgentRadiusAccountingServers_Type=Unsigned32
_AgentRadiusAccountingServers_Object=MibScalar
agentRadiusAccountingServers=_AgentRadiusAccountingServers_Object((1,3,6,1,4,1,4413,1,1,8,1,15),_AgentRadiusAccountingServers_Type())
agentRadiusAccountingServers.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusAccountingServers.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroups_Type=Unsigned32
_AgentRadiusNamedAuthenticationServerGroups_Object=MibScalar
agentRadiusNamedAuthenticationServerGroups=_AgentRadiusNamedAuthenticationServerGroups_Object((1,3,6,1,4,1,4413,1,1,8,1,16),_AgentRadiusNamedAuthenticationServerGroups_Type())
agentRadiusNamedAuthenticationServerGroups.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroups.setStatus(_A)
_AgentRadiusNamedAccountingServerGroups_Type=Unsigned32
_AgentRadiusNamedAccountingServerGroups_Object=MibScalar
agentRadiusNamedAccountingServerGroups=_AgentRadiusNamedAccountingServerGroups_Object((1,3,6,1,4,1,4413,1,1,8,1,17),_AgentRadiusNamedAccountingServerGroups_Type())
agentRadiusNamedAccountingServerGroups.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroups.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'fastPathRadius':fastPathRadius,'agentRadiusConfigGroup':agentRadiusConfigGroup,'agentRadiusRetransmit':agentRadiusRetransmit,'agentRadiusTimeout':agentRadiusTimeout,'agentRadiusDeadTime':agentRadiusDeadTime,'agentRadiusServerKey':agentRadiusServerKey,'agentRadiusSourceIPAddr':agentRadiusSourceIPAddr,'agentRadiusServerIndexNextValid':agentRadiusServerIndexNextValid,'agentRadiusServerConfigTable':agentRadiusServerConfigTable,'agentRadiusServerConfigEntry':agentRadiusServerConfigEntry,_L:agentRadiusServerIndex,'agentRadiusServerAddress':agentRadiusServerAddress,'agentRadiusServerPort':agentRadiusServerPort,'agentRadiusServerTimeout':agentRadiusServerTimeout,'agentRadiusServerRetransmit':agentRadiusServerRetransmit,'agentRadiusServerDeadtime':agentRadiusServerDeadtime,'agentRadiusServerSourceIPAddr':agentRadiusServerSourceIPAddr,'agentRadiusServerSecret':agentRadiusServerSecret,'agentRadiusServerPriority':agentRadiusServerPriority,'agentRadiusServerUsageType':agentRadiusServerUsageType,'agentRadiusServerAddressRowStatus':agentRadiusServerAddressRowStatus,'agentRadiusServerPrimaryMode':agentRadiusServerPrimaryMode,'agentRadiusServerCurrentMode':agentRadiusServerCurrentMode,'agentRadiusServerMsgAuth':agentRadiusServerMsgAuth,'agentRadiusServerName':agentRadiusServerName,'agentRadiusServerInetAddress':agentRadiusServerInetAddress,'agentRadiusServerAddressType':agentRadiusServerAddressType,'agentRadiusNasIpAddress':agentRadiusNasIpAddress,'agentAuthorizationNetworkRadiusMode':agentAuthorizationNetworkRadiusMode,'agentRadiusAccountingIndexNextValid':agentRadiusAccountingIndexNextValid,'agentRadiusAccountingConfigTable':agentRadiusAccountingConfigTable,'agentRadiusAccountingConfigEntry':agentRadiusAccountingConfigEntry,_N:agentRadiusAccountingServerIndex,'agentRadiusAccountingServerAddress':agentRadiusAccountingServerAddress,'agentRadiusAccountingServerAddressType':agentRadiusAccountingServerAddressType,'agentRadiusAccountingPort':agentRadiusAccountingPort,'agentRadiusAccountingSecret':agentRadiusAccountingSecret,'agentRadiusAccountingStatus':agentRadiusAccountingStatus,'agentRadiusAccountingServerName':agentRadiusAccountingServerName,'agentRadiusAccountingMode':agentRadiusAccountingMode,'agentRadiusStatsClear':agentRadiusStatsClear,'agentRadiusAuthenticationServers':agentRadiusAuthenticationServers,'agentRadiusAccountingServers':agentRadiusAccountingServers,'agentRadiusNamedAuthenticationServerGroups':agentRadiusNamedAuthenticationServerGroups,'agentRadiusNamedAccountingServerGroups':agentRadiusNamedAccountingServerGroups})