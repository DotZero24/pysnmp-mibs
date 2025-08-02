_R='extremeAuthServerIndex'
_Q='extremeAuthServerEnableAccessType'
_P='extremeAuthServerEnableServerType'
_O='extremeDNSServerAddressIndex'
_N='extremeRemoteSyslogServerFacility'
_M='extremeRemoteSyslogServerPort'
_L='extremeRemoteSyslogServerAddress'
_K='extremeRemoteSyslogServerAddressType'
_J='TruthValue'
_I='InetAddressType'
_H='read-create'
_G='InetAddress'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='EXTREME-SERVICES-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
extremeServices=ModuleIdentity((1,3,6,1,4,1,1916,1,26))
class AuthServerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('radius',1),('radius-acct',2),('tacacs',3),('tacacs-acct',4)))
class AuthServerAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgmt-access',1),('netlogin',2)))
_ExtremeSyslog_ObjectIdentity=ObjectIdentity
extremeSyslog=_ExtremeSyslog_ObjectIdentity((1,3,6,1,4,1,1916,1,26,1))
_ExtremeRemoteSyslogServerTable_Object=MibTable
extremeRemoteSyslogServerTable=_ExtremeRemoteSyslogServerTable_Object((1,3,6,1,4,1,1916,1,26,1,1))
if mibBuilder.loadTexts:extremeRemoteSyslogServerTable.setStatus(_A)
_ExtremeRemoteSyslogServerEntry_Object=MibTableRow
extremeRemoteSyslogServerEntry=_ExtremeRemoteSyslogServerEntry_Object((1,3,6,1,4,1,1916,1,26,1,1,1))
extremeRemoteSyslogServerEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:extremeRemoteSyslogServerEntry.setStatus(_A)
class _ExtremeRemoteSyslogServerAddressType_Type(InetAddressType):defaultValue=1
_ExtremeRemoteSyslogServerAddressType_Type.__name__=_I
_ExtremeRemoteSyslogServerAddressType_Object=MibTableColumn
extremeRemoteSyslogServerAddressType=_ExtremeRemoteSyslogServerAddressType_Object((1,3,6,1,4,1,1916,1,26,1,1,1,1),_ExtremeRemoteSyslogServerAddressType_Type())
extremeRemoteSyslogServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRemoteSyslogServerAddressType.setStatus(_A)
class _ExtremeRemoteSyslogServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ExtremeRemoteSyslogServerAddress_Type.__name__=_G
_ExtremeRemoteSyslogServerAddress_Object=MibTableColumn
extremeRemoteSyslogServerAddress=_ExtremeRemoteSyslogServerAddress_Object((1,3,6,1,4,1,1916,1,26,1,1,1,2),_ExtremeRemoteSyslogServerAddress_Type())
extremeRemoteSyslogServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRemoteSyslogServerAddress.setStatus(_A)
class _ExtremeRemoteSyslogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeRemoteSyslogServerPort_Type.__name__=_E
_ExtremeRemoteSyslogServerPort_Object=MibTableColumn
extremeRemoteSyslogServerPort=_ExtremeRemoteSyslogServerPort_Object((1,3,6,1,4,1,1916,1,26,1,1,1,3),_ExtremeRemoteSyslogServerPort_Type())
extremeRemoteSyslogServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRemoteSyslogServerPort.setStatus(_A)
class _ExtremeRemoteSyslogServerFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('local0',1),('local1',2),('local2',3),('local3',4),('local4',5),('local5',6),('local6',7),('local7',8)))
_ExtremeRemoteSyslogServerFacility_Type.__name__=_E
_ExtremeRemoteSyslogServerFacility_Object=MibTableColumn
extremeRemoteSyslogServerFacility=_ExtremeRemoteSyslogServerFacility_Object((1,3,6,1,4,1,1916,1,26,1,1,1,4),_ExtremeRemoteSyslogServerFacility_Type())
extremeRemoteSyslogServerFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRemoteSyslogServerFacility.setStatus(_A)
class _ExtremeRemoteSyslogServerSeverity_Type(Bits):defaultBinValue='11111111';namedValues=NamedValues(*(('critical',0),('error',1),('warning',2),('notice',3),('info',4),('debugSummary',5),('debugVerbose',6),('debugData',7)))
_ExtremeRemoteSyslogServerSeverity_Type.__name__='Bits'
_ExtremeRemoteSyslogServerSeverity_Object=MibTableColumn
extremeRemoteSyslogServerSeverity=_ExtremeRemoteSyslogServerSeverity_Object((1,3,6,1,4,1,1916,1,26,1,1,1,5),_ExtremeRemoteSyslogServerSeverity_Type())
extremeRemoteSyslogServerSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeRemoteSyslogServerSeverity.setStatus(_A)
_ExtremeRemoteSyslogServerStatus_Type=RowStatus
_ExtremeRemoteSyslogServerStatus_Object=MibTableColumn
extremeRemoteSyslogServerStatus=_ExtremeRemoteSyslogServerStatus_Object((1,3,6,1,4,1,1916,1,26,1,1,1,6),_ExtremeRemoteSyslogServerStatus_Type())
extremeRemoteSyslogServerStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeRemoteSyslogServerStatus.setStatus(_A)
_ExtremeEnableRemoteSyslog_Type=TruthValue
_ExtremeEnableRemoteSyslog_Object=MibScalar
extremeEnableRemoteSyslog=_ExtremeEnableRemoteSyslog_Object((1,3,6,1,4,1,1916,1,26,1,2),_ExtremeEnableRemoteSyslog_Type())
extremeEnableRemoteSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEnableRemoteSyslog.setStatus(_A)
_ExtremeDNS_ObjectIdentity=ObjectIdentity
extremeDNS=_ExtremeDNS_ObjectIdentity((1,3,6,1,4,1,1916,1,26,3))
_ExtremeDNSServerTable_Object=MibTable
extremeDNSServerTable=_ExtremeDNSServerTable_Object((1,3,6,1,4,1,1916,1,26,3,1))
if mibBuilder.loadTexts:extremeDNSServerTable.setStatus(_A)
_ExtremeDNSServerEntry_Object=MibTableRow
extremeDNSServerEntry=_ExtremeDNSServerEntry_Object((1,3,6,1,4,1,1916,1,26,3,1,1))
extremeDNSServerEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:extremeDNSServerEntry.setStatus(_A)
class _ExtremeDNSServerAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ExtremeDNSServerAddressIndex_Type.__name__=_E
_ExtremeDNSServerAddressIndex_Object=MibTableColumn
extremeDNSServerAddressIndex=_ExtremeDNSServerAddressIndex_Object((1,3,6,1,4,1,1916,1,26,3,1,1,1),_ExtremeDNSServerAddressIndex_Type())
extremeDNSServerAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeDNSServerAddressIndex.setStatus(_A)
_ExtremeDNSServerAddressType_Type=InetAddressType
_ExtremeDNSServerAddressType_Object=MibTableColumn
extremeDNSServerAddressType=_ExtremeDNSServerAddressType_Object((1,3,6,1,4,1,1916,1,26,3,1,1,2),_ExtremeDNSServerAddressType_Type())
extremeDNSServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeDNSServerAddressType.setStatus(_A)
class _ExtremeDNSServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ExtremeDNSServerAddress_Type.__name__=_G
_ExtremeDNSServerAddress_Object=MibTableColumn
extremeDNSServerAddress=_ExtremeDNSServerAddress_Object((1,3,6,1,4,1,1916,1,26,3,1,1,3),_ExtremeDNSServerAddress_Type())
extremeDNSServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeDNSServerAddress.setStatus(_A)
_ExtremeAuthServer_ObjectIdentity=ObjectIdentity
extremeAuthServer=_ExtremeAuthServer_ObjectIdentity((1,3,6,1,4,1,1916,1,26,4))
_ExtremeAuthServerEnableTable_Object=MibTable
extremeAuthServerEnableTable=_ExtremeAuthServerEnableTable_Object((1,3,6,1,4,1,1916,1,26,4,1))
if mibBuilder.loadTexts:extremeAuthServerEnableTable.setStatus(_A)
_ExtremeAuthServerEnableEntry_Object=MibTableRow
extremeAuthServerEnableEntry=_ExtremeAuthServerEnableEntry_Object((1,3,6,1,4,1,1916,1,26,4,1,1))
extremeAuthServerEnableEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:extremeAuthServerEnableEntry.setStatus(_A)
_ExtremeAuthServerEnableServerType_Type=AuthServerType
_ExtremeAuthServerEnableServerType_Object=MibTableColumn
extremeAuthServerEnableServerType=_ExtremeAuthServerEnableServerType_Object((1,3,6,1,4,1,1916,1,26,4,1,1,1),_ExtremeAuthServerEnableServerType_Type())
extremeAuthServerEnableServerType.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeAuthServerEnableServerType.setStatus(_A)
_ExtremeAuthServerEnableAccessType_Type=AuthServerAccessType
_ExtremeAuthServerEnableAccessType_Object=MibTableColumn
extremeAuthServerEnableAccessType=_ExtremeAuthServerEnableAccessType_Object((1,3,6,1,4,1,1916,1,26,4,1,1,2),_ExtremeAuthServerEnableAccessType_Type())
extremeAuthServerEnableAccessType.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeAuthServerEnableAccessType.setStatus(_A)
class _ExtremeAuthServerEnable_Type(TruthValue):defaultValue=2
_ExtremeAuthServerEnable_Type.__name__=_J
_ExtremeAuthServerEnable_Object=MibTableColumn
extremeAuthServerEnable=_ExtremeAuthServerEnable_Object((1,3,6,1,4,1,1916,1,26,4,1,1,3),_ExtremeAuthServerEnable_Type())
extremeAuthServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerEnable.setStatus(_A)
_ExtremeAuthServerTable_Object=MibTable
extremeAuthServerTable=_ExtremeAuthServerTable_Object((1,3,6,1,4,1,1916,1,26,4,2))
if mibBuilder.loadTexts:extremeAuthServerTable.setStatus(_A)
_ExtremeAuthServerEntry_Object=MibTableRow
extremeAuthServerEntry=_ExtremeAuthServerEntry_Object((1,3,6,1,4,1,1916,1,26,4,2,1))
extremeAuthServerEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:extremeAuthServerEntry.setStatus(_A)
class _ExtremeAuthServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeAuthServerIndex_Type.__name__=_E
_ExtremeAuthServerIndex_Object=MibTableColumn
extremeAuthServerIndex=_ExtremeAuthServerIndex_Object((1,3,6,1,4,1,1916,1,26,4,2,1,1),_ExtremeAuthServerIndex_Type())
extremeAuthServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:extremeAuthServerIndex.setStatus(_A)
_ExtremeAuthServerAddressType_Type=InetAddressType
_ExtremeAuthServerAddressType_Object=MibTableColumn
extremeAuthServerAddressType=_ExtremeAuthServerAddressType_Object((1,3,6,1,4,1,1916,1,26,4,2,1,2),_ExtremeAuthServerAddressType_Type())
extremeAuthServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerAddressType.setStatus(_A)
_ExtremeAuthServerAddress_Type=InetAddress
_ExtremeAuthServerAddress_Object=MibTableColumn
extremeAuthServerAddress=_ExtremeAuthServerAddress_Object((1,3,6,1,4,1,1916,1,26,4,2,1,3),_ExtremeAuthServerAddress_Type())
extremeAuthServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerAddress.setStatus(_A)
_ExtremeAuthServerClientAddressType_Type=InetAddressType
_ExtremeAuthServerClientAddressType_Object=MibTableColumn
extremeAuthServerClientAddressType=_ExtremeAuthServerClientAddressType_Object((1,3,6,1,4,1,1916,1,26,4,2,1,4),_ExtremeAuthServerClientAddressType_Type())
extremeAuthServerClientAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerClientAddressType.setStatus(_A)
_ExtremeAuthServerClientAddress_Type=InetAddress
_ExtremeAuthServerClientAddress_Object=MibTableColumn
extremeAuthServerClientAddress=_ExtremeAuthServerClientAddress_Object((1,3,6,1,4,1,1916,1,26,4,2,1,5),_ExtremeAuthServerClientAddress_Type())
extremeAuthServerClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerClientAddress.setStatus(_A)
_ExtremeAuthServerPort_Type=Integer32
_ExtremeAuthServerPort_Object=MibTableColumn
extremeAuthServerPort=_ExtremeAuthServerPort_Object((1,3,6,1,4,1,1916,1,26,4,2,1,6),_ExtremeAuthServerPort_Type())
extremeAuthServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerPort.setStatus(_A)
_ExtremeAuthServerSecret_Type=OctetString
_ExtremeAuthServerSecret_Object=MibTableColumn
extremeAuthServerSecret=_ExtremeAuthServerSecret_Object((1,3,6,1,4,1,1916,1,26,4,2,1,7),_ExtremeAuthServerSecret_Type())
extremeAuthServerSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerSecret.setStatus(_A)
_ExtremeAuthServerReTransmit_Type=Integer32
_ExtremeAuthServerReTransmit_Object=MibTableColumn
extremeAuthServerReTransmit=_ExtremeAuthServerReTransmit_Object((1,3,6,1,4,1,1916,1,26,4,2,1,8),_ExtremeAuthServerReTransmit_Type())
extremeAuthServerReTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerReTransmit.setStatus(_A)
_ExtremeAuthServerType_Type=AuthServerType
_ExtremeAuthServerType_Object=MibTableColumn
extremeAuthServerType=_ExtremeAuthServerType_Object((1,3,6,1,4,1,1916,1,26,4,2,1,9),_ExtremeAuthServerType_Type())
extremeAuthServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerType.setStatus(_A)
_ExtremeAuthServerIsPrimary_Type=TruthValue
_ExtremeAuthServerIsPrimary_Object=MibTableColumn
extremeAuthServerIsPrimary=_ExtremeAuthServerIsPrimary_Object((1,3,6,1,4,1,1916,1,26,4,2,1,10),_ExtremeAuthServerIsPrimary_Type())
extremeAuthServerIsPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerIsPrimary.setStatus(_A)
_ExtremeAuthServerAccessType_Type=AuthServerAccessType
_ExtremeAuthServerAccessType_Object=MibTableColumn
extremeAuthServerAccessType=_ExtremeAuthServerAccessType_Object((1,3,6,1,4,1,1916,1,26,4,2,1,11),_ExtremeAuthServerAccessType_Type())
extremeAuthServerAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAuthServerAccessType.setStatus(_A)
_ExtremeAuthServerStatus_Type=RowStatus
_ExtremeAuthServerStatus_Object=MibTableColumn
extremeAuthServerStatus=_ExtremeAuthServerStatus_Object((1,3,6,1,4,1,1916,1,26,4,2,1,12),_ExtremeAuthServerStatus_Type())
extremeAuthServerStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeAuthServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AuthServerType':AuthServerType,'AuthServerAccessType':AuthServerAccessType,'extremeServices':extremeServices,'extremeSyslog':extremeSyslog,'extremeRemoteSyslogServerTable':extremeRemoteSyslogServerTable,'extremeRemoteSyslogServerEntry':extremeRemoteSyslogServerEntry,_K:extremeRemoteSyslogServerAddressType,_L:extremeRemoteSyslogServerAddress,_M:extremeRemoteSyslogServerPort,_N:extremeRemoteSyslogServerFacility,'extremeRemoteSyslogServerSeverity':extremeRemoteSyslogServerSeverity,'extremeRemoteSyslogServerStatus':extremeRemoteSyslogServerStatus,'extremeEnableRemoteSyslog':extremeEnableRemoteSyslog,'extremeDNS':extremeDNS,'extremeDNSServerTable':extremeDNSServerTable,'extremeDNSServerEntry':extremeDNSServerEntry,_O:extremeDNSServerAddressIndex,'extremeDNSServerAddressType':extremeDNSServerAddressType,'extremeDNSServerAddress':extremeDNSServerAddress,'extremeAuthServer':extremeAuthServer,'extremeAuthServerEnableTable':extremeAuthServerEnableTable,'extremeAuthServerEnableEntry':extremeAuthServerEnableEntry,_P:extremeAuthServerEnableServerType,_Q:extremeAuthServerEnableAccessType,'extremeAuthServerEnable':extremeAuthServerEnable,'extremeAuthServerTable':extremeAuthServerTable,'extremeAuthServerEntry':extremeAuthServerEntry,_R:extremeAuthServerIndex,'extremeAuthServerAddressType':extremeAuthServerAddressType,'extremeAuthServerAddress':extremeAuthServerAddress,'extremeAuthServerClientAddressType':extremeAuthServerClientAddressType,'extremeAuthServerClientAddress':extremeAuthServerClientAddress,'extremeAuthServerPort':extremeAuthServerPort,'extremeAuthServerSecret':extremeAuthServerSecret,'extremeAuthServerReTransmit':extremeAuthServerReTransmit,'extremeAuthServerType':extremeAuthServerType,'extremeAuthServerIsPrimary':extremeAuthServerIsPrimary,'extremeAuthServerAccessType':extremeAuthServerAccessType,'extremeAuthServerStatus':extremeAuthServerStatus})