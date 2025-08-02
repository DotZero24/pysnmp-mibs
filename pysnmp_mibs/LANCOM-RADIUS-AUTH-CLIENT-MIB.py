_c='agentRadiusNamedAccountingServerGroupName'
_b='least-outstanding-request'
_a='agentRadiusNamedAuthenticationServerGroupName'
_Z='include'
_Y='doNotInclude'
_X='agentRadiusServerIndex'
_W='mortal'
_V='immortal'
_U='unknown'
_T='quarantined'
_S='inactive'
_R='agentRadiusAccountingServerIndex'
_Q='radiusFormatUnformatUpperCase'
_P='radiusFormatUnformatLowerCase'
_O='radiusFormatIetfUpperCase'
_N='radiusFormatIetfLowerrCase'
_M='radiusFormatLegacyUpperCase'
_L='radiusFormatLegacyLowerCase'
_K='not-accessible'
_J='LANCOM-RADIUS-AUTH-CLIENT-MIB'
_I='disable'
_H='enable'
_G='read-create'
_F='DisplayString'
_E='Unsigned32'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fastPathRadius=ModuleIdentity((1,3,6,1,4,1,2356,16,1,8))
if mibBuilder.loadTexts:fastPathRadius.setRevisions(('2018-03-10 00:00','2018-02-13 00:00','2017-03-30 00:00','2016-11-21 00:00','2016-09-29 00:00','2014-04-21 00:00','2011-12-14 00:00','2011-09-26 00:00','2011-01-26 00:00','2007-05-23 00:00','2003-11-21 00:00','2003-05-07 00:00'))
_AgentRadiusConfigGroup_ObjectIdentity=ObjectIdentity
agentRadiusConfigGroup=_AgentRadiusConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,8,1))
class _AgentRadiusMaxTransmit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AgentRadiusMaxTransmit_Type.__name__=_E
_AgentRadiusMaxTransmit_Object=MibScalar
agentRadiusMaxTransmit=_AgentRadiusMaxTransmit_Object((1,3,6,1,4,1,2356,16,1,8,1,1),_AgentRadiusMaxTransmit_Type())
agentRadiusMaxTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusMaxTransmit.setStatus(_A)
class _AgentRadiusTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusTimeout_Type.__name__=_E
_AgentRadiusTimeout_Object=MibScalar
agentRadiusTimeout=_AgentRadiusTimeout_Object((1,3,6,1,4,1,2356,16,1,8,1,2),_AgentRadiusTimeout_Type())
agentRadiusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusTimeout.setStatus(_A)
class _AgentRadiusAccountingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusAccountingMode_Type.__name__=_C
_AgentRadiusAccountingMode_Object=MibScalar
agentRadiusAccountingMode=_AgentRadiusAccountingMode_Object((1,3,6,1,4,1,2356,16,1,8,1,3),_AgentRadiusAccountingMode_Type())
agentRadiusAccountingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingMode.setStatus(_A)
class _AgentRadiusStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusStatsClear_Type.__name__=_C
_AgentRadiusStatsClear_Object=MibScalar
agentRadiusStatsClear=_AgentRadiusStatsClear_Object((1,3,6,1,4,1,2356,16,1,8,1,4),_AgentRadiusStatsClear_Type())
agentRadiusStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusStatsClear.setStatus(_A)
class _AgentRadiusAccountingIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingIndexNextValid_Type.__name__=_C
_AgentRadiusAccountingIndexNextValid_Object=MibScalar
agentRadiusAccountingIndexNextValid=_AgentRadiusAccountingIndexNextValid_Object((1,3,6,1,4,1,2356,16,1,8,1,5),_AgentRadiusAccountingIndexNextValid_Type())
agentRadiusAccountingIndexNextValid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAccountingIndexNextValid.setStatus(_A)
_AgentRadiusAccountingConfigTable_Object=MibTable
agentRadiusAccountingConfigTable=_AgentRadiusAccountingConfigTable_Object((1,3,6,1,4,1,2356,16,1,8,1,6))
if mibBuilder.loadTexts:agentRadiusAccountingConfigTable.setStatus(_A)
_AgentRadiusAccountingConfigEntry_Object=MibTableRow
agentRadiusAccountingConfigEntry=_AgentRadiusAccountingConfigEntry_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1))
agentRadiusAccountingConfigEntry.setIndexNames((0,_J,_R))
if mibBuilder.loadTexts:agentRadiusAccountingConfigEntry.setStatus(_A)
class _AgentRadiusAccountingServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingServerIndex_Type.__name__=_C
_AgentRadiusAccountingServerIndex_Object=MibTableColumn
agentRadiusAccountingServerIndex=_AgentRadiusAccountingServerIndex_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,1),_AgentRadiusAccountingServerIndex_Type())
agentRadiusAccountingServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentRadiusAccountingServerIndex.setStatus(_A)
_AgentRadiusAccountingServerAddress_Type=InetAddress
_AgentRadiusAccountingServerAddress_Object=MibTableColumn
agentRadiusAccountingServerAddress=_AgentRadiusAccountingServerAddress_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,2),_AgentRadiusAccountingServerAddress_Type())
agentRadiusAccountingServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddress.setStatus(_A)
_AgentRadiusAccountingServerAddressType_Type=InetAddressType
_AgentRadiusAccountingServerAddressType_Object=MibTableColumn
agentRadiusAccountingServerAddressType=_AgentRadiusAccountingServerAddressType_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,3),_AgentRadiusAccountingServerAddressType_Type())
agentRadiusAccountingServerAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddressType.setStatus(_A)
class _AgentRadiusAccountingPort_Type(Unsigned32):defaultValue=1813;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentRadiusAccountingPort_Type.__name__=_E
_AgentRadiusAccountingPort_Object=MibTableColumn
agentRadiusAccountingPort=_AgentRadiusAccountingPort_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,4),_AgentRadiusAccountingPort_Type())
agentRadiusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingPort.setStatus(_A)
class _AgentRadiusAccountingSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentRadiusAccountingSecret_Type.__name__=_F
_AgentRadiusAccountingSecret_Object=MibTableColumn
agentRadiusAccountingSecret=_AgentRadiusAccountingSecret_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,5),_AgentRadiusAccountingSecret_Type())
agentRadiusAccountingSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingSecret.setStatus(_A)
_AgentRadiusAccountingStatus_Type=RowStatus
_AgentRadiusAccountingStatus_Object=MibTableColumn
agentRadiusAccountingStatus=_AgentRadiusAccountingStatus_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,6),_AgentRadiusAccountingStatus_Type())
agentRadiusAccountingStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingStatus.setStatus(_A)
class _AgentRadiusAccountingServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusAccountingServerName_Type.__name__=_F
_AgentRadiusAccountingServerName_Object=MibTableColumn
agentRadiusAccountingServerName=_AgentRadiusAccountingServerName_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,7),_AgentRadiusAccountingServerName_Type())
agentRadiusAccountingServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingServerName.setStatus(_A)
_AgentRadiusAccountingLinkLocalIntf_Type=InterfaceIndexOrZero
_AgentRadiusAccountingLinkLocalIntf_Object=MibTableColumn
agentRadiusAccountingLinkLocalIntf=_AgentRadiusAccountingLinkLocalIntf_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,8),_AgentRadiusAccountingLinkLocalIntf_Type())
agentRadiusAccountingLinkLocalIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingLinkLocalIntf.setStatus(_A)
class _AgentRadiusAccountingServerTestUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusAccountingServerTestUserName_Type.__name__=_F
_AgentRadiusAccountingServerTestUserName_Object=MibTableColumn
agentRadiusAccountingServerTestUserName=_AgentRadiusAccountingServerTestUserName_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,9),_AgentRadiusAccountingServerTestUserName_Type())
agentRadiusAccountingServerTestUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingServerTestUserName.setStatus(_A)
class _AgentRadiusAccountingServerIdleTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35791))
_AgentRadiusAccountingServerIdleTime_Type.__name__=_E
_AgentRadiusAccountingServerIdleTime_Object=MibTableColumn
agentRadiusAccountingServerIdleTime=_AgentRadiusAccountingServerIdleTime_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,10),_AgentRadiusAccountingServerIdleTime_Type())
agentRadiusAccountingServerIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusAccountingServerIdleTime.setStatus(_A)
class _AgentRadiusAccountingServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),(_S,2),('dead',3),(_T,4),(_U,5)))
_AgentRadiusAccountingServerState_Type.__name__=_C
_AgentRadiusAccountingServerState_Object=MibTableColumn
agentRadiusAccountingServerState=_AgentRadiusAccountingServerState_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,11),_AgentRadiusAccountingServerState_Type())
agentRadiusAccountingServerState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAccountingServerState.setStatus(_A)
_AgentRadiusAccountingServerStateDuration_Type=Unsigned32
_AgentRadiusAccountingServerStateDuration_Object=MibTableColumn
agentRadiusAccountingServerStateDuration=_AgentRadiusAccountingServerStateDuration_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,12),_AgentRadiusAccountingServerStateDuration_Type())
agentRadiusAccountingServerStateDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAccountingServerStateDuration.setStatus(_A)
class _AgentRadiusAccountingServerImmortalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AgentRadiusAccountingServerImmortalState_Type.__name__=_C
_AgentRadiusAccountingServerImmortalState_Object=MibTableColumn
agentRadiusAccountingServerImmortalState=_AgentRadiusAccountingServerImmortalState_Object((1,3,6,1,4,1,2356,16,1,8,1,6,1,13),_AgentRadiusAccountingServerImmortalState_Type())
agentRadiusAccountingServerImmortalState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAccountingServerImmortalState.setStatus(_A)
class _AgentRadiusServerIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndexNextValid_Type.__name__=_C
_AgentRadiusServerIndexNextValid_Object=MibScalar
agentRadiusServerIndexNextValid=_AgentRadiusServerIndexNextValid_Object((1,3,6,1,4,1,2356,16,1,8,1,7),_AgentRadiusServerIndexNextValid_Type())
agentRadiusServerIndexNextValid.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusServerIndexNextValid.setStatus(_A)
_AgentRadiusServerConfigTable_Object=MibTable
agentRadiusServerConfigTable=_AgentRadiusServerConfigTable_Object((1,3,6,1,4,1,2356,16,1,8,1,8))
if mibBuilder.loadTexts:agentRadiusServerConfigTable.setStatus(_A)
_AgentRadiusServerConfigEntry_Object=MibTableRow
agentRadiusServerConfigEntry=_AgentRadiusServerConfigEntry_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1))
agentRadiusServerConfigEntry.setIndexNames((0,_J,_X))
if mibBuilder.loadTexts:agentRadiusServerConfigEntry.setStatus(_A)
class _AgentRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndex_Type.__name__=_C
_AgentRadiusServerIndex_Object=MibTableColumn
agentRadiusServerIndex=_AgentRadiusServerIndex_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,1),_AgentRadiusServerIndex_Type())
agentRadiusServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentRadiusServerIndex.setStatus(_A)
_AgentRadiusServerAddress_Type=InetAddress
_AgentRadiusServerAddress_Object=MibTableColumn
agentRadiusServerAddress=_AgentRadiusServerAddress_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,2),_AgentRadiusServerAddress_Type())
agentRadiusServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerAddress.setStatus('obsolete')
_AgentRadiusServerAddressType_Type=InetAddressType
_AgentRadiusServerAddressType_Object=MibTableColumn
agentRadiusServerAddressType=_AgentRadiusServerAddressType_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,3),_AgentRadiusServerAddressType_Type())
agentRadiusServerAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerAddressType.setStatus(_A)
class _AgentRadiusServerPort_Type(Unsigned32):defaultValue=1812;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentRadiusServerPort_Type.__name__=_E
_AgentRadiusServerPort_Object=MibTableColumn
agentRadiusServerPort=_AgentRadiusServerPort_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,4),_AgentRadiusServerPort_Type())
agentRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPort.setStatus(_A)
class _AgentRadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentRadiusServerSecret_Type.__name__=_F
_AgentRadiusServerSecret_Object=MibTableColumn
agentRadiusServerSecret=_AgentRadiusServerSecret_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,5),_AgentRadiusServerSecret_Type())
agentRadiusServerSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSecret.setStatus(_A)
class _AgentRadiusServerPrimaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerPrimaryMode_Type.__name__=_C
_AgentRadiusServerPrimaryMode_Object=MibTableColumn
agentRadiusServerPrimaryMode=_AgentRadiusServerPrimaryMode_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,6),_AgentRadiusServerPrimaryMode_Type())
agentRadiusServerPrimaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPrimaryMode.setStatus(_A)
class _AgentRadiusServerCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AgentRadiusServerCurrentMode_Type.__name__=_C
_AgentRadiusServerCurrentMode_Object=MibTableColumn
agentRadiusServerCurrentMode=_AgentRadiusServerCurrentMode_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,7),_AgentRadiusServerCurrentMode_Type())
agentRadiusServerCurrentMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusServerCurrentMode.setStatus(_A)
class _AgentRadiusServerMsgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerMsgAuth_Type.__name__=_C
_AgentRadiusServerMsgAuth_Object=MibTableColumn
agentRadiusServerMsgAuth=_AgentRadiusServerMsgAuth_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,8),_AgentRadiusServerMsgAuth_Type())
agentRadiusServerMsgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerMsgAuth.setStatus(_A)
_AgentRadiusServerRowStatus_Type=RowStatus
_AgentRadiusServerRowStatus_Object=MibTableColumn
agentRadiusServerRowStatus=_AgentRadiusServerRowStatus_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,9),_AgentRadiusServerRowStatus_Type())
agentRadiusServerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerRowStatus.setStatus(_A)
class _AgentRadiusServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusServerName_Type.__name__=_F
_AgentRadiusServerName_Object=MibTableColumn
agentRadiusServerName=_AgentRadiusServerName_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,10),_AgentRadiusServerName_Type())
agentRadiusServerName.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerName.setStatus(_A)
_AgentRadiusServerInetAddress_Type=InetAddress
_AgentRadiusServerInetAddress_Object=MibTableColumn
agentRadiusServerInetAddress=_AgentRadiusServerInetAddress_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,11),_AgentRadiusServerInetAddress_Type())
agentRadiusServerInetAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerInetAddress.setStatus(_A)
class _AgentRadiusServerTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusServerTimeout_Type.__name__=_E
_AgentRadiusServerTimeout_Object=MibTableColumn
agentRadiusServerTimeout=_AgentRadiusServerTimeout_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,12),_AgentRadiusServerTimeout_Type())
agentRadiusServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerTimeout.setStatus(_A)
class _AgentRadiusServerRetransmit_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentRadiusServerRetransmit_Type.__name__=_E
_AgentRadiusServerRetransmit_Object=MibTableColumn
agentRadiusServerRetransmit=_AgentRadiusServerRetransmit_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,13),_AgentRadiusServerRetransmit_Type())
agentRadiusServerRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerRetransmit.setStatus(_A)
class _AgentRadiusServerDeadtime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusServerDeadtime_Type.__name__=_E
_AgentRadiusServerDeadtime_Object=MibTableColumn
agentRadiusServerDeadtime=_AgentRadiusServerDeadtime_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,14),_AgentRadiusServerDeadtime_Type())
agentRadiusServerDeadtime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerDeadtime.setStatus(_A)
_AgentRadiusServerSourceIPAddr_Type=IpAddress
_AgentRadiusServerSourceIPAddr_Object=MibTableColumn
agentRadiusServerSourceIPAddr=_AgentRadiusServerSourceIPAddr_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,15),_AgentRadiusServerSourceIPAddr_Type())
agentRadiusServerSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSourceIPAddr.setStatus(_A)
class _AgentRadiusServerPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusServerPriority_Type.__name__=_E
_AgentRadiusServerPriority_Object=MibTableColumn
agentRadiusServerPriority=_AgentRadiusServerPriority_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,16),_AgentRadiusServerPriority_Type())
agentRadiusServerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerPriority.setStatus(_A)
class _AgentRadiusServerUsageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('login',2),('dot1x',3),('authmgr',4)))
_AgentRadiusServerUsageType_Type.__name__=_C
_AgentRadiusServerUsageType_Object=MibTableColumn
agentRadiusServerUsageType=_AgentRadiusServerUsageType_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,17),_AgentRadiusServerUsageType_Type())
agentRadiusServerUsageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerUsageType.setStatus(_A)
_AgentRadiusServerSourceIPv6Addr_Type=InetAddress
_AgentRadiusServerSourceIPv6Addr_Object=MibTableColumn
agentRadiusServerSourceIPv6Addr=_AgentRadiusServerSourceIPv6Addr_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,18),_AgentRadiusServerSourceIPv6Addr_Type())
agentRadiusServerSourceIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerSourceIPv6Addr.setStatus(_A)
class _AgentRadiusServerConfigAttr31MacFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_AgentRadiusServerConfigAttr31MacFormat_Type.__name__=_C
_AgentRadiusServerConfigAttr31MacFormat_Object=MibTableColumn
agentRadiusServerConfigAttr31MacFormat=_AgentRadiusServerConfigAttr31MacFormat_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,19),_AgentRadiusServerConfigAttr31MacFormat_Type())
agentRadiusServerConfigAttr31MacFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerConfigAttr31MacFormat.setStatus('deprecated')
_AgentRadiusServerLinkLocalIntf_Type=InterfaceIndexOrZero
_AgentRadiusServerLinkLocalIntf_Object=MibTableColumn
agentRadiusServerLinkLocalIntf=_AgentRadiusServerLinkLocalIntf_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,20),_AgentRadiusServerLinkLocalIntf_Type())
agentRadiusServerLinkLocalIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerLinkLocalIntf.setStatus(_A)
class _AgentRadiusServerTestUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusServerTestUserName_Type.__name__=_F
_AgentRadiusServerTestUserName_Object=MibTableColumn
agentRadiusServerTestUserName=_AgentRadiusServerTestUserName_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,21),_AgentRadiusServerTestUserName_Type())
agentRadiusServerTestUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerTestUserName.setStatus(_A)
class _AgentRadiusServerIdleTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35791))
_AgentRadiusServerIdleTime_Type.__name__=_E
_AgentRadiusServerIdleTime_Object=MibTableColumn
agentRadiusServerIdleTime=_AgentRadiusServerIdleTime_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,22),_AgentRadiusServerIdleTime_Type())
agentRadiusServerIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerIdleTime.setStatus(_A)
class _AgentRadiusServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),(_S,2),('dead',3),(_T,4),(_U,5)))
_AgentRadiusServerState_Type.__name__=_C
_AgentRadiusServerState_Object=MibTableColumn
agentRadiusServerState=_AgentRadiusServerState_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,23),_AgentRadiusServerState_Type())
agentRadiusServerState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusServerState.setStatus(_A)
_AgentRadiusServerStateDuration_Type=Unsigned32
_AgentRadiusServerStateDuration_Object=MibTableColumn
agentRadiusServerStateDuration=_AgentRadiusServerStateDuration_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,24),_AgentRadiusServerStateDuration_Type())
agentRadiusServerStateDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusServerStateDuration.setStatus(_A)
class _AgentRadiusServerImmortalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AgentRadiusServerImmortalState_Type.__name__=_C
_AgentRadiusServerImmortalState_Object=MibTableColumn
agentRadiusServerImmortalState=_AgentRadiusServerImmortalState_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,25),_AgentRadiusServerImmortalState_Type())
agentRadiusServerImmortalState.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusServerImmortalState.setStatus(_A)
class _AgentRadiusServerVSAAuth_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentRadiusServerVSAAuth_Type.__name__=_C
_AgentRadiusServerVSAAuth_Object=MibTableColumn
agentRadiusServerVSAAuth=_AgentRadiusServerVSAAuth_Object((1,3,6,1,4,1,2356,16,1,8,1,8,1,26),_AgentRadiusServerVSAAuth_Type())
agentRadiusServerVSAAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerVSAAuth.setStatus(_A)
_AgentRadiusAuthenticationServers_Type=Unsigned32
_AgentRadiusAuthenticationServers_Object=MibScalar
agentRadiusAuthenticationServers=_AgentRadiusAuthenticationServers_Object((1,3,6,1,4,1,2356,16,1,8,1,9),_AgentRadiusAuthenticationServers_Type())
agentRadiusAuthenticationServers.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAuthenticationServers.setStatus(_A)
_AgentRadiusAccountingServers_Type=Unsigned32
_AgentRadiusAccountingServers_Object=MibScalar
agentRadiusAccountingServers=_AgentRadiusAccountingServers_Object((1,3,6,1,4,1,2356,16,1,8,1,10),_AgentRadiusAccountingServers_Type())
agentRadiusAccountingServers.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusAccountingServers.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroups_Type=Unsigned32
_AgentRadiusNamedAuthenticationServerGroups_Object=MibScalar
agentRadiusNamedAuthenticationServerGroups=_AgentRadiusNamedAuthenticationServerGroups_Object((1,3,6,1,4,1,2356,16,1,8,1,11),_AgentRadiusNamedAuthenticationServerGroups_Type())
agentRadiusNamedAuthenticationServerGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroups.setStatus(_A)
_AgentRadiusNamedAccountingServerGroups_Type=Unsigned32
_AgentRadiusNamedAccountingServerGroups_Object=MibScalar
agentRadiusNamedAccountingServerGroups=_AgentRadiusNamedAccountingServerGroups_Object((1,3,6,1,4,1,2356,16,1,8,1,12),_AgentRadiusNamedAccountingServerGroups_Type())
agentRadiusNamedAccountingServerGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroups.setStatus(_A)
class _AgentRadiusDeadTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentRadiusDeadTime_Type.__name__=_E
_AgentRadiusDeadTime_Object=MibScalar
agentRadiusDeadTime=_AgentRadiusDeadTime_Object((1,3,6,1,4,1,2356,16,1,8,1,13),_AgentRadiusDeadTime_Type())
agentRadiusDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusDeadTime.setStatus(_A)
class _AgentRadiusServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentRadiusServerKey_Type.__name__=_F
_AgentRadiusServerKey_Object=MibScalar
agentRadiusServerKey=_AgentRadiusServerKey_Object((1,3,6,1,4,1,2356,16,1,8,1,14),_AgentRadiusServerKey_Type())
agentRadiusServerKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerKey.setStatus(_A)
_AgentRadiusSourceIPAddr_Type=IpAddress
_AgentRadiusSourceIPAddr_Object=MibScalar
agentRadiusSourceIPAddr=_AgentRadiusSourceIPAddr_Object((1,3,6,1,4,1,2356,16,1,8,1,15),_AgentRadiusSourceIPAddr_Type())
agentRadiusSourceIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusSourceIPAddr.setStatus(_A)
_AgentRadiusNasIpAddress_Type=IpAddress
_AgentRadiusNasIpAddress_Object=MibScalar
agentRadiusNasIpAddress=_AgentRadiusNasIpAddress_Object((1,3,6,1,4,1,2356,16,1,8,1,16),_AgentRadiusNasIpAddress_Type())
agentRadiusNasIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNasIpAddress.setStatus(_A)
class _AgentAuthorizationNetworkRadiusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_H,1)))
_AgentAuthorizationNetworkRadiusMode_Type.__name__=_C
_AgentAuthorizationNetworkRadiusMode_Object=MibScalar
agentAuthorizationNetworkRadiusMode=_AgentAuthorizationNetworkRadiusMode_Object((1,3,6,1,4,1,2356,16,1,8,1,17),_AgentAuthorizationNetworkRadiusMode_Type())
agentAuthorizationNetworkRadiusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthorizationNetworkRadiusMode.setStatus(_A)
_AgentRadiusSourceInterface_Type=InterfaceIndexOrZero
_AgentRadiusSourceInterface_Object=MibScalar
agentRadiusSourceInterface=_AgentRadiusSourceInterface_Object((1,3,6,1,4,1,2356,16,1,8,1,18),_AgentRadiusSourceInterface_Type())
agentRadiusSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusSourceInterface.setStatus(_A)
_AgentDasRequestsReceived_Type=Unsigned32
_AgentDasRequestsReceived_Object=MibScalar
agentDasRequestsReceived=_AgentDasRequestsReceived_Object((1,3,6,1,4,1,2356,16,1,8,1,19),_AgentDasRequestsReceived_Type())
agentDasRequestsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsReceived.setStatus(_A)
_AgentDasACKResponsesSent_Type=Unsigned32
_AgentDasACKResponsesSent_Object=MibScalar
agentDasACKResponsesSent=_AgentDasACKResponsesSent_Object((1,3,6,1,4,1,2356,16,1,8,1,20),_AgentDasACKResponsesSent_Type())
agentDasACKResponsesSent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasACKResponsesSent.setStatus(_A)
_AgentDasNAKResponsesSent_Type=Unsigned32
_AgentDasNAKResponsesSent_Object=MibScalar
agentDasNAKResponsesSent=_AgentDasNAKResponsesSent_Object((1,3,6,1,4,1,2356,16,1,8,1,21),_AgentDasNAKResponsesSent_Type())
agentDasNAKResponsesSent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasNAKResponsesSent.setStatus(_A)
_AgentDasRequestsIgnored_Type=Unsigned32
_AgentDasRequestsIgnored_Object=MibScalar
agentDasRequestsIgnored=_AgentDasRequestsIgnored_Object((1,3,6,1,4,1,2356,16,1,8,1,22),_AgentDasRequestsIgnored_Type())
agentDasRequestsIgnored.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsIgnored.setStatus(_A)
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Type=Unsigned32
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Object=MibScalar
agentDasRequestsWithMissingOrUnsupportedAttribute=_AgentDasRequestsWithMissingOrUnsupportedAttribute_Object((1,3,6,1,4,1,2356,16,1,8,1,23),_AgentDasRequestsWithMissingOrUnsupportedAttribute_Type())
agentDasRequestsWithMissingOrUnsupportedAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsWithMissingOrUnsupportedAttribute.setStatus(_A)
_AgentDasRequestsWithSessionContextNotFound_Type=Unsigned32
_AgentDasRequestsWithSessionContextNotFound_Object=MibScalar
agentDasRequestsWithSessionContextNotFound=_AgentDasRequestsWithSessionContextNotFound_Object((1,3,6,1,4,1,2356,16,1,8,1,24),_AgentDasRequestsWithSessionContextNotFound_Type())
agentDasRequestsWithSessionContextNotFound.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsWithSessionContextNotFound.setStatus(_A)
_AgentDasRequestsWithInvalidAttributeValue_Type=Unsigned32
_AgentDasRequestsWithInvalidAttributeValue_Object=MibScalar
agentDasRequestsWithInvalidAttributeValue=_AgentDasRequestsWithInvalidAttributeValue_Object((1,3,6,1,4,1,2356,16,1,8,1,25),_AgentDasRequestsWithInvalidAttributeValue_Type())
agentDasRequestsWithInvalidAttributeValue.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsWithInvalidAttributeValue.setStatus(_A)
_AgentDasRequestsAdministrativelyProhibited_Type=Unsigned32
_AgentDasRequestsAdministrativelyProhibited_Object=MibScalar
agentDasRequestsAdministrativelyProhibited=_AgentDasRequestsAdministrativelyProhibited_Object((1,3,6,1,4,1,2356,16,1,8,1,26),_AgentDasRequestsAdministrativelyProhibited_Type())
agentDasRequestsAdministrativelyProhibited.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDasRequestsAdministrativelyProhibited.setStatus(_A)
class _AgentRadiusServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentRadiusServicePortSrcInterface_Type.__name__=_C
_AgentRadiusServicePortSrcInterface_Object=MibScalar
agentRadiusServicePortSrcInterface=_AgentRadiusServicePortSrcInterface_Object((1,3,6,1,4,1,2356,16,1,8,1,27),_AgentRadiusServicePortSrcInterface_Type())
agentRadiusServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServicePortSrcInterface.setStatus(_A)
_AgentRadiusNasIpv6Address_Type=InetAddress
_AgentRadiusNasIpv6Address_Object=MibScalar
agentRadiusNasIpv6Address=_AgentRadiusNasIpv6Address_Object((1,3,6,1,4,1,2356,16,1,8,1,28),_AgentRadiusNasIpv6Address_Type())
agentRadiusNasIpv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNasIpv6Address.setStatus(_A)
class _AgentRadiusServerAttr31MacFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_AgentRadiusServerAttr31MacFormat_Type.__name__=_C
_AgentRadiusServerAttr31MacFormat_Object=MibScalar
agentRadiusServerAttr31MacFormat=_AgentRadiusServerAttr31MacFormat_Object((1,3,6,1,4,1,2356,16,1,8,1,29),_AgentRadiusServerAttr31MacFormat_Type())
agentRadiusServerAttr31MacFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerAttr31MacFormat.setStatus(_A)
class _AgentRadiusServerAttr30MacFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_AgentRadiusServerAttr30MacFormat_Type.__name__=_C
_AgentRadiusServerAttr30MacFormat_Object=MibScalar
agentRadiusServerAttr30MacFormat=_AgentRadiusServerAttr30MacFormat_Object((1,3,6,1,4,1,2356,16,1,8,1,30),_AgentRadiusServerAttr30MacFormat_Type())
agentRadiusServerAttr30MacFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerAttr30MacFormat.setStatus(_A)
class _AgentRadiusServerAttr32MacFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_AgentRadiusServerAttr32MacFormat_Type.__name__=_C
_AgentRadiusServerAttr32MacFormat_Object=MibScalar
agentRadiusServerAttr32MacFormat=_AgentRadiusServerAttr32MacFormat_Object((1,3,6,1,4,1,2356,16,1,8,1,31),_AgentRadiusServerAttr32MacFormat_Type())
agentRadiusServerAttr32MacFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerAttr32MacFormat.setStatus(_A)
class _AgentRadiusServerInclude32InAccessRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_AgentRadiusServerInclude32InAccessRequest_Type.__name__=_C
_AgentRadiusServerInclude32InAccessRequest_Object=MibScalar
agentRadiusServerInclude32InAccessRequest=_AgentRadiusServerInclude32InAccessRequest_Object((1,3,6,1,4,1,2356,16,1,8,1,32),_AgentRadiusServerInclude32InAccessRequest_Type())
agentRadiusServerInclude32InAccessRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerInclude32InAccessRequest.setStatus(_A)
class _AgentRadiusServerInclude32InAccessRequestFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,128))
_AgentRadiusServerInclude32InAccessRequestFormat_Type.__name__=_F
_AgentRadiusServerInclude32InAccessRequestFormat_Object=MibScalar
agentRadiusServerInclude32InAccessRequestFormat=_AgentRadiusServerInclude32InAccessRequestFormat_Object((1,3,6,1,4,1,2356,16,1,8,1,33),_AgentRadiusServerInclude32InAccessRequestFormat_Type())
agentRadiusServerInclude32InAccessRequestFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerInclude32InAccessRequestFormat.setStatus(_A)
class _AgentRadiusServerInclude44InAccessRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_AgentRadiusServerInclude44InAccessRequest_Type.__name__=_C
_AgentRadiusServerInclude44InAccessRequest_Object=MibScalar
agentRadiusServerInclude44InAccessRequest=_AgentRadiusServerInclude44InAccessRequest_Object((1,3,6,1,4,1,2356,16,1,8,1,34),_AgentRadiusServerInclude44InAccessRequest_Type())
agentRadiusServerInclude44InAccessRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerInclude44InAccessRequest.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroupConfigTable_Object=MibTable
agentRadiusNamedAuthenticationServerGroupConfigTable=_AgentRadiusNamedAuthenticationServerGroupConfigTable_Object((1,3,6,1,4,1,2356,16,1,8,1,35))
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupConfigTable.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroupConfigEntry_Object=MibTableRow
agentRadiusNamedAuthenticationServerGroupConfigEntry=_AgentRadiusNamedAuthenticationServerGroupConfigEntry_Object((1,3,6,1,4,1,2356,16,1,8,1,35,1))
agentRadiusNamedAuthenticationServerGroupConfigEntry.setIndexNames((0,_J,_a))
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupConfigEntry.setStatus(_A)
class _AgentRadiusNamedAuthenticationServerGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusNamedAuthenticationServerGroupName_Type.__name__=_F
_AgentRadiusNamedAuthenticationServerGroupName_Object=MibTableColumn
agentRadiusNamedAuthenticationServerGroupName=_AgentRadiusNamedAuthenticationServerGroupName_Object((1,3,6,1,4,1,2356,16,1,8,1,35,1,1),_AgentRadiusNamedAuthenticationServerGroupName_Type())
agentRadiusNamedAuthenticationServerGroupName.setMaxAccess(_K)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupName.setStatus(_A)
class _AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),(_b,2)))
_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type.__name__=_C
_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Object=MibTableColumn
agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod=_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Object((1,3,6,1,4,1,2356,16,1,8,1,35,1,2),_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type())
agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod.setStatus(_A)
class _AgentRadiusNamedAuthenticationServerGroupBatchSize_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusNamedAuthenticationServerGroupBatchSize_Type.__name__=_E
_AgentRadiusNamedAuthenticationServerGroupBatchSize_Object=MibTableColumn
agentRadiusNamedAuthenticationServerGroupBatchSize=_AgentRadiusNamedAuthenticationServerGroupBatchSize_Object((1,3,6,1,4,1,2356,16,1,8,1,35,1,3),_AgentRadiusNamedAuthenticationServerGroupBatchSize_Type())
agentRadiusNamedAuthenticationServerGroupBatchSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupBatchSize.setStatus(_A)
_AgentRadiusNamedAuthenticationServerGroupDeadCount_Type=Unsigned32
_AgentRadiusNamedAuthenticationServerGroupDeadCount_Object=MibTableColumn
agentRadiusNamedAuthenticationServerGroupDeadCount=_AgentRadiusNamedAuthenticationServerGroupDeadCount_Object((1,3,6,1,4,1,2356,16,1,8,1,35,1,4),_AgentRadiusNamedAuthenticationServerGroupDeadCount_Type())
agentRadiusNamedAuthenticationServerGroupDeadCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusNamedAuthenticationServerGroupDeadCount.setStatus(_A)
_AgentRadiusNamedAccountingServerGroupConfigTable_Object=MibTable
agentRadiusNamedAccountingServerGroupConfigTable=_AgentRadiusNamedAccountingServerGroupConfigTable_Object((1,3,6,1,4,1,2356,16,1,8,1,36))
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupConfigTable.setStatus(_A)
_AgentRadiusNamedAccountingServerGroupConfigEntry_Object=MibTableRow
agentRadiusNamedAccountingServerGroupConfigEntry=_AgentRadiusNamedAccountingServerGroupConfigEntry_Object((1,3,6,1,4,1,2356,16,1,8,1,36,1))
agentRadiusNamedAccountingServerGroupConfigEntry.setIndexNames((0,_J,_c))
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupConfigEntry.setStatus(_A)
class _AgentRadiusNamedAccountingServerGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentRadiusNamedAccountingServerGroupName_Type.__name__=_F
_AgentRadiusNamedAccountingServerGroupName_Object=MibTableColumn
agentRadiusNamedAccountingServerGroupName=_AgentRadiusNamedAccountingServerGroupName_Object((1,3,6,1,4,1,2356,16,1,8,1,36,1,1),_AgentRadiusNamedAccountingServerGroupName_Type())
agentRadiusNamedAccountingServerGroupName.setMaxAccess(_K)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupName.setStatus(_A)
class _AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),(_b,2)))
_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type.__name__=_C
_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Object=MibTableColumn
agentRadiusNamedAccountingServerGroupLoadBalanceMethod=_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Object((1,3,6,1,4,1,2356,16,1,8,1,36,1,2),_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type())
agentRadiusNamedAccountingServerGroupLoadBalanceMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupLoadBalanceMethod.setStatus(_A)
class _AgentRadiusNamedAccountingServerGroupBatchSize_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusNamedAccountingServerGroupBatchSize_Type.__name__=_E
_AgentRadiusNamedAccountingServerGroupBatchSize_Object=MibTableColumn
agentRadiusNamedAccountingServerGroupBatchSize=_AgentRadiusNamedAccountingServerGroupBatchSize_Object((1,3,6,1,4,1,2356,16,1,8,1,36,1,3),_AgentRadiusNamedAccountingServerGroupBatchSize_Type())
agentRadiusNamedAccountingServerGroupBatchSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupBatchSize.setStatus(_A)
_AgentRadiusNamedAccountingServerGroupDeadCount_Type=Unsigned32
_AgentRadiusNamedAccountingServerGroupDeadCount_Object=MibTableColumn
agentRadiusNamedAccountingServerGroupDeadCount=_AgentRadiusNamedAccountingServerGroupDeadCount_Object((1,3,6,1,4,1,2356,16,1,8,1,36,1,4),_AgentRadiusNamedAccountingServerGroupDeadCount_Type())
agentRadiusNamedAccountingServerGroupDeadCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRadiusNamedAccountingServerGroupDeadCount.setStatus(_A)
class _AgentRadiusServerDeadCriteriaTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_AgentRadiusServerDeadCriteriaTime_Type.__name__=_E
_AgentRadiusServerDeadCriteriaTime_Object=MibScalar
agentRadiusServerDeadCriteriaTime=_AgentRadiusServerDeadCriteriaTime_Object((1,3,6,1,4,1,2356,16,1,8,1,37),_AgentRadiusServerDeadCriteriaTime_Type())
agentRadiusServerDeadCriteriaTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerDeadCriteriaTime.setStatus(_A)
class _AgentRadiusServerDeadCriteriaTries_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AgentRadiusServerDeadCriteriaTries_Type.__name__=_E
_AgentRadiusServerDeadCriteriaTries_Object=MibScalar
agentRadiusServerDeadCriteriaTries=_AgentRadiusServerDeadCriteriaTries_Object((1,3,6,1,4,1,2356,16,1,8,1,38),_AgentRadiusServerDeadCriteriaTries_Type())
agentRadiusServerDeadCriteriaTries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRadiusServerDeadCriteriaTries.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'fastPathRadius':fastPathRadius,'agentRadiusConfigGroup':agentRadiusConfigGroup,'agentRadiusMaxTransmit':agentRadiusMaxTransmit,'agentRadiusTimeout':agentRadiusTimeout,'agentRadiusAccountingMode':agentRadiusAccountingMode,'agentRadiusStatsClear':agentRadiusStatsClear,'agentRadiusAccountingIndexNextValid':agentRadiusAccountingIndexNextValid,'agentRadiusAccountingConfigTable':agentRadiusAccountingConfigTable,'agentRadiusAccountingConfigEntry':agentRadiusAccountingConfigEntry,_R:agentRadiusAccountingServerIndex,'agentRadiusAccountingServerAddress':agentRadiusAccountingServerAddress,'agentRadiusAccountingServerAddressType':agentRadiusAccountingServerAddressType,'agentRadiusAccountingPort':agentRadiusAccountingPort,'agentRadiusAccountingSecret':agentRadiusAccountingSecret,'agentRadiusAccountingStatus':agentRadiusAccountingStatus,'agentRadiusAccountingServerName':agentRadiusAccountingServerName,'agentRadiusAccountingLinkLocalIntf':agentRadiusAccountingLinkLocalIntf,'agentRadiusAccountingServerTestUserName':agentRadiusAccountingServerTestUserName,'agentRadiusAccountingServerIdleTime':agentRadiusAccountingServerIdleTime,'agentRadiusAccountingServerState':agentRadiusAccountingServerState,'agentRadiusAccountingServerStateDuration':agentRadiusAccountingServerStateDuration,'agentRadiusAccountingServerImmortalState':agentRadiusAccountingServerImmortalState,'agentRadiusServerIndexNextValid':agentRadiusServerIndexNextValid,'agentRadiusServerConfigTable':agentRadiusServerConfigTable,'agentRadiusServerConfigEntry':agentRadiusServerConfigEntry,_X:agentRadiusServerIndex,'agentRadiusServerAddress':agentRadiusServerAddress,'agentRadiusServerAddressType':agentRadiusServerAddressType,'agentRadiusServerPort':agentRadiusServerPort,'agentRadiusServerSecret':agentRadiusServerSecret,'agentRadiusServerPrimaryMode':agentRadiusServerPrimaryMode,'agentRadiusServerCurrentMode':agentRadiusServerCurrentMode,'agentRadiusServerMsgAuth':agentRadiusServerMsgAuth,'agentRadiusServerRowStatus':agentRadiusServerRowStatus,'agentRadiusServerName':agentRadiusServerName,'agentRadiusServerInetAddress':agentRadiusServerInetAddress,'agentRadiusServerTimeout':agentRadiusServerTimeout,'agentRadiusServerRetransmit':agentRadiusServerRetransmit,'agentRadiusServerDeadtime':agentRadiusServerDeadtime,'agentRadiusServerSourceIPAddr':agentRadiusServerSourceIPAddr,'agentRadiusServerPriority':agentRadiusServerPriority,'agentRadiusServerUsageType':agentRadiusServerUsageType,'agentRadiusServerSourceIPv6Addr':agentRadiusServerSourceIPv6Addr,'agentRadiusServerConfigAttr31MacFormat':agentRadiusServerConfigAttr31MacFormat,'agentRadiusServerLinkLocalIntf':agentRadiusServerLinkLocalIntf,'agentRadiusServerTestUserName':agentRadiusServerTestUserName,'agentRadiusServerIdleTime':agentRadiusServerIdleTime,'agentRadiusServerState':agentRadiusServerState,'agentRadiusServerStateDuration':agentRadiusServerStateDuration,'agentRadiusServerImmortalState':agentRadiusServerImmortalState,'agentRadiusServerVSAAuth':agentRadiusServerVSAAuth,'agentRadiusAuthenticationServers':agentRadiusAuthenticationServers,'agentRadiusAccountingServers':agentRadiusAccountingServers,'agentRadiusNamedAuthenticationServerGroups':agentRadiusNamedAuthenticationServerGroups,'agentRadiusNamedAccountingServerGroups':agentRadiusNamedAccountingServerGroups,'agentRadiusDeadTime':agentRadiusDeadTime,'agentRadiusServerKey':agentRadiusServerKey,'agentRadiusSourceIPAddr':agentRadiusSourceIPAddr,'agentRadiusNasIpAddress':agentRadiusNasIpAddress,'agentAuthorizationNetworkRadiusMode':agentAuthorizationNetworkRadiusMode,'agentRadiusSourceInterface':agentRadiusSourceInterface,'agentDasRequestsReceived':agentDasRequestsReceived,'agentDasACKResponsesSent':agentDasACKResponsesSent,'agentDasNAKResponsesSent':agentDasNAKResponsesSent,'agentDasRequestsIgnored':agentDasRequestsIgnored,'agentDasRequestsWithMissingOrUnsupportedAttribute':agentDasRequestsWithMissingOrUnsupportedAttribute,'agentDasRequestsWithSessionContextNotFound':agentDasRequestsWithSessionContextNotFound,'agentDasRequestsWithInvalidAttributeValue':agentDasRequestsWithInvalidAttributeValue,'agentDasRequestsAdministrativelyProhibited':agentDasRequestsAdministrativelyProhibited,'agentRadiusServicePortSrcInterface':agentRadiusServicePortSrcInterface,'agentRadiusNasIpv6Address':agentRadiusNasIpv6Address,'agentRadiusServerAttr31MacFormat':agentRadiusServerAttr31MacFormat,'agentRadiusServerAttr30MacFormat':agentRadiusServerAttr30MacFormat,'agentRadiusServerAttr32MacFormat':agentRadiusServerAttr32MacFormat,'agentRadiusServerInclude32InAccessRequest':agentRadiusServerInclude32InAccessRequest,'agentRadiusServerInclude32InAccessRequestFormat':agentRadiusServerInclude32InAccessRequestFormat,'agentRadiusServerInclude44InAccessRequest':agentRadiusServerInclude44InAccessRequest,'agentRadiusNamedAuthenticationServerGroupConfigTable':agentRadiusNamedAuthenticationServerGroupConfigTable,'agentRadiusNamedAuthenticationServerGroupConfigEntry':agentRadiusNamedAuthenticationServerGroupConfigEntry,_a:agentRadiusNamedAuthenticationServerGroupName,'agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod':agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod,'agentRadiusNamedAuthenticationServerGroupBatchSize':agentRadiusNamedAuthenticationServerGroupBatchSize,'agentRadiusNamedAuthenticationServerGroupDeadCount':agentRadiusNamedAuthenticationServerGroupDeadCount,'agentRadiusNamedAccountingServerGroupConfigTable':agentRadiusNamedAccountingServerGroupConfigTable,'agentRadiusNamedAccountingServerGroupConfigEntry':agentRadiusNamedAccountingServerGroupConfigEntry,_c:agentRadiusNamedAccountingServerGroupName,'agentRadiusNamedAccountingServerGroupLoadBalanceMethod':agentRadiusNamedAccountingServerGroupLoadBalanceMethod,'agentRadiusNamedAccountingServerGroupBatchSize':agentRadiusNamedAccountingServerGroupBatchSize,'agentRadiusNamedAccountingServerGroupDeadCount':agentRadiusNamedAccountingServerGroupDeadCount,'agentRadiusServerDeadCriteriaTime':agentRadiusServerDeadCriteriaTime,'agentRadiusServerDeadCriteriaTries':agentRadiusServerDeadCriteriaTries})