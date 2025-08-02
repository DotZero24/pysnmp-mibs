_P='wwpLeosNtpClientSyncState'
_O='wwpLeosNtpMulticastIndex'
_N='wwpLeosNtpAuthKeyId'
_M='disabled'
_L='enabled'
_K='wwpLeosNtpServerIndex'
_J='Md5Key'
_I='read-create'
_H='deprecated'
_G='not-accessible'
_F='Unsigned32'
_E='WWP-LEOS-NTP-CLIENT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosNtpClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,18))
if mibBuilder.loadTexts:wwpLeosNtpClientMIB.setRevisions(('2012-09-12 00:00','2012-05-31 00:00','2012-03-27 00:00','2011-07-05 00:00','2011-03-29 12:00','2008-05-20 00:00','2007-12-20 00:00','2007-07-15 10:00','2003-04-11 17:00'))
class Md5Key(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosNtpClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBObjects=_WwpLeosNtpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,1))
_WwpLeosNtpClient_ObjectIdentity=ObjectIdentity
wwpLeosNtpClient=_WwpLeosNtpClient_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,1,1))
class _WwpLeosNtpClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpLeosNtpClientState_Type.__name__=_B
_WwpLeosNtpClientState_Object=MibScalar
wwpLeosNtpClientState=_WwpLeosNtpClientState_Object((1,3,6,1,4,1,6141,2,60,18,1,1,1),_WwpLeosNtpClientState_Type())
wwpLeosNtpClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientState.setStatus(_A)
class _WwpLeosNtpClientMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('polling',1),('broadcast',2)))
_WwpLeosNtpClientMode_Type.__name__=_B
_WwpLeosNtpClientMode_Object=MibScalar
wwpLeosNtpClientMode=_WwpLeosNtpClientMode_Object((1,3,6,1,4,1,6141,2,60,18,1,1,2),_WwpLeosNtpClientMode_Type())
wwpLeosNtpClientMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientMode.setStatus(_A)
class _WwpLeosNtpClientPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_WwpLeosNtpClientPollFreq_Type.__name__=_B
_WwpLeosNtpClientPollFreq_Object=MibScalar
wwpLeosNtpClientPollFreq=_WwpLeosNtpClientPollFreq_Object((1,3,6,1,4,1,6141,2,60,18,1,1,3),_WwpLeosNtpClientPollFreq_Type())
wwpLeosNtpClientPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientPollFreq.setStatus(_A)
_WwpLeosNtpClientTable_Object=MibTable
wwpLeosNtpClientTable=_WwpLeosNtpClientTable_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4))
if mibBuilder.loadTexts:wwpLeosNtpClientTable.setStatus(_A)
_WwpLeosNtpClientEntry_Object=MibTableRow
wwpLeosNtpClientEntry=_WwpLeosNtpClientEntry_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1))
wwpLeosNtpClientEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:wwpLeosNtpClientEntry.setStatus(_A)
class _WwpLeosNtpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosNtpServerIndex_Type.__name__=_B
_WwpLeosNtpServerIndex_Object=MibTableColumn
wwpLeosNtpServerIndex=_WwpLeosNtpServerIndex_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,1),_WwpLeosNtpServerIndex_Type())
wwpLeosNtpServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosNtpServerIndex.setStatus(_A)
_WwpLeosNtpServerAddrType_Type=AddressFamilyNumbers
_WwpLeosNtpServerAddrType_Object=MibTableColumn
wwpLeosNtpServerAddrType=_WwpLeosNtpServerAddrType_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,2),_WwpLeosNtpServerAddrType_Type())
wwpLeosNtpServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpServerAddrType.setStatus(_A)
_WwpLeosNtpServerAddr_Type=DisplayString
_WwpLeosNtpServerAddr_Object=MibTableColumn
wwpLeosNtpServerAddr=_WwpLeosNtpServerAddr_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,3),_WwpLeosNtpServerAddr_Type())
wwpLeosNtpServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpServerAddr.setStatus(_A)
_WwpLeosNtpServerResolvedAddr_Type=IpAddress
_WwpLeosNtpServerResolvedAddr_Object=MibTableColumn
wwpLeosNtpServerResolvedAddr=_WwpLeosNtpServerResolvedAddr_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,4),_WwpLeosNtpServerResolvedAddr_Type())
wwpLeosNtpServerResolvedAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerResolvedAddr.setStatus(_A)
class _WwpLeosNtpServerUserPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosNtpServerUserPri_Type.__name__=_B
_WwpLeosNtpServerUserPri_Object=MibTableColumn
wwpLeosNtpServerUserPri=_WwpLeosNtpServerUserPri_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,5),_WwpLeosNtpServerUserPri_Type())
wwpLeosNtpServerUserPri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpServerUserPri.setStatus(_H)
class _WwpLeosNtpServerDhcpPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosNtpServerDhcpPri_Type.__name__=_B
_WwpLeosNtpServerDhcpPri_Object=MibTableColumn
wwpLeosNtpServerDhcpPri=_WwpLeosNtpServerDhcpPri_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,6),_WwpLeosNtpServerDhcpPri_Type())
wwpLeosNtpServerDhcpPri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerDhcpPri.setStatus(_H)
class _WwpLeosNtpServerUserAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosNtpServerUserAdminState_Type.__name__=_B
_WwpLeosNtpServerUserAdminState_Object=MibTableColumn
wwpLeosNtpServerUserAdminState=_WwpLeosNtpServerUserAdminState_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,7),_WwpLeosNtpServerUserAdminState_Type())
wwpLeosNtpServerUserAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpServerUserAdminState.setStatus(_A)
class _WwpLeosNtpServerScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('dhcp',2),('both',3)))
_WwpLeosNtpServerScope_Type.__name__=_B
_WwpLeosNtpServerScope_Object=MibTableColumn
wwpLeosNtpServerScope=_WwpLeosNtpServerScope_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,8),_WwpLeosNtpServerScope_Type())
wwpLeosNtpServerScope.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerScope.setStatus(_A)
class _WwpLeosNtpServerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('notConfigured',3)))
_WwpLeosNtpServerOperState_Type.__name__=_B
_WwpLeosNtpServerOperState_Object=MibTableColumn
wwpLeosNtpServerOperState=_WwpLeosNtpServerOperState_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,9),_WwpLeosNtpServerOperState_Type())
wwpLeosNtpServerOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerOperState.setStatus(_A)
_WwpLeosNtpServerStatus_Type=RowStatus
_WwpLeosNtpServerStatus_Object=MibTableColumn
wwpLeosNtpServerStatus=_WwpLeosNtpServerStatus_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,10),_WwpLeosNtpServerStatus_Type())
wwpLeosNtpServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosNtpServerStatus.setStatus(_A)
class _WwpLeosNtpServerKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwpLeosNtpServerKeyId_Type.__name__=_F
_WwpLeosNtpServerKeyId_Object=MibTableColumn
wwpLeosNtpServerKeyId=_WwpLeosNtpServerKeyId_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,11),_WwpLeosNtpServerKeyId_Type())
wwpLeosNtpServerKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpServerKeyId.setStatus(_A)
class _WwpLeosNtpServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255,256)));namedValues=NamedValues(*(('reject',1),('insane',2),('correct',3),('standby',4),('candidate',5),('selected',6),('syspeer',7),('ppspeer',8),('reaching',255),('error',256)))
_WwpLeosNtpServerState_Type.__name__=_B
_WwpLeosNtpServerState_Object=MibTableColumn
wwpLeosNtpServerState=_WwpLeosNtpServerState_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,12),_WwpLeosNtpServerState_Type())
wwpLeosNtpServerState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerState.setStatus(_A)
_WwpLeosNtpServerResolvedInetAddrType_Type=InetAddressType
_WwpLeosNtpServerResolvedInetAddrType_Object=MibTableColumn
wwpLeosNtpServerResolvedInetAddrType=_WwpLeosNtpServerResolvedInetAddrType_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,13),_WwpLeosNtpServerResolvedInetAddrType_Type())
wwpLeosNtpServerResolvedInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerResolvedInetAddrType.setStatus(_A)
_WwpLeosNtpServerResolvedInetAddr_Type=InetAddress
_WwpLeosNtpServerResolvedInetAddr_Object=MibTableColumn
wwpLeosNtpServerResolvedInetAddr=_WwpLeosNtpServerResolvedInetAddr_Object((1,3,6,1,4,1,6141,2,60,18,1,1,4,1,14),_WwpLeosNtpServerResolvedInetAddr_Type())
wwpLeosNtpServerResolvedInetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpServerResolvedInetAddr.setStatus(_A)
_WwpLeosNtpAuthTable_Object=MibTable
wwpLeosNtpAuthTable=_WwpLeosNtpAuthTable_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5))
if mibBuilder.loadTexts:wwpLeosNtpAuthTable.setStatus(_A)
_WwpLeosNtpAuthEntry_Object=MibTableRow
wwpLeosNtpAuthEntry=_WwpLeosNtpAuthEntry_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5,1))
wwpLeosNtpAuthEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:wwpLeosNtpAuthEntry.setStatus(_A)
class _WwpLeosNtpAuthKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwpLeosNtpAuthKeyId_Type.__name__=_F
_WwpLeosNtpAuthKeyId_Object=MibTableColumn
wwpLeosNtpAuthKeyId=_WwpLeosNtpAuthKeyId_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5,1,1),_WwpLeosNtpAuthKeyId_Type())
wwpLeosNtpAuthKeyId.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosNtpAuthKeyId.setStatus(_A)
class _WwpLeosNtpAuthMd5Key_Type(Md5Key):subtypeSpec=Md5Key.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosNtpAuthMd5Key_Type.__name__=_J
_WwpLeosNtpAuthMd5Key_Object=MibTableColumn
wwpLeosNtpAuthMd5Key=_WwpLeosNtpAuthMd5Key_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5,1,2),_WwpLeosNtpAuthMd5Key_Type())
wwpLeosNtpAuthMd5Key.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpAuthMd5Key.setStatus(_A)
_WwpLeosNtpAuthRowStatus_Type=RowStatus
_WwpLeosNtpAuthRowStatus_Object=MibTableColumn
wwpLeosNtpAuthRowStatus=_WwpLeosNtpAuthRowStatus_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5,1,3),_WwpLeosNtpAuthRowStatus_Type())
wwpLeosNtpAuthRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosNtpAuthRowStatus.setStatus(_A)
class _WwpLeosNtpAuthMD5KeyEnc_Type(Md5Key):subtypeSpec=Md5Key.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WwpLeosNtpAuthMD5KeyEnc_Type.__name__=_J
_WwpLeosNtpAuthMD5KeyEnc_Object=MibTableColumn
wwpLeosNtpAuthMD5KeyEnc=_WwpLeosNtpAuthMD5KeyEnc_Object((1,3,6,1,4,1,6141,2,60,18,1,1,5,1,4),_WwpLeosNtpAuthMD5KeyEnc_Type())
wwpLeosNtpAuthMD5KeyEnc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpAuthMD5KeyEnc.setStatus(_A)
_WwpLeosNtpClientMD5State_Type=TruthValue
_WwpLeosNtpClientMD5State_Object=MibScalar
wwpLeosNtpClientMD5State=_WwpLeosNtpClientMD5State_Object((1,3,6,1,4,1,6141,2,60,18,1,1,6),_WwpLeosNtpClientMD5State_Type())
wwpLeosNtpClientMD5State.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientMD5State.setStatus(_A)
_WwpLeosNtpClientDrift_Type=Integer32
_WwpLeosNtpClientDrift_Object=MibScalar
wwpLeosNtpClientDrift=_WwpLeosNtpClientDrift_Object((1,3,6,1,4,1,6141,2,60,18,1,1,7),_WwpLeosNtpClientDrift_Type())
wwpLeosNtpClientDrift.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientDrift.setStatus(_A)
_WwpLeosNtpClientFastOffset_Type=Integer32
_WwpLeosNtpClientFastOffset_Object=MibScalar
wwpLeosNtpClientFastOffset=_WwpLeosNtpClientFastOffset_Object((1,3,6,1,4,1,6141,2,60,18,1,1,9),_WwpLeosNtpClientFastOffset_Type())
wwpLeosNtpClientFastOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientFastOffset.setStatus(_A)
_WwpLeosNtpClientSlowOffset_Type=Integer32
_WwpLeosNtpClientSlowOffset_Object=MibScalar
wwpLeosNtpClientSlowOffset=_WwpLeosNtpClientSlowOffset_Object((1,3,6,1,4,1,6141,2,60,18,1,1,10),_WwpLeosNtpClientSlowOffset_Type())
wwpLeosNtpClientSlowOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientSlowOffset.setStatus(_A)
class _WwpLeosNtpClientMinPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_WwpLeosNtpClientMinPollFreq_Type.__name__=_B
_WwpLeosNtpClientMinPollFreq_Object=MibScalar
wwpLeosNtpClientMinPollFreq=_WwpLeosNtpClientMinPollFreq_Object((1,3,6,1,4,1,6141,2,60,18,1,1,11),_WwpLeosNtpClientMinPollFreq_Type())
wwpLeosNtpClientMinPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientMinPollFreq.setStatus(_A)
class _WwpLeosNtpClientMaxPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_WwpLeosNtpClientMaxPollFreq_Type.__name__=_B
_WwpLeosNtpClientMaxPollFreq_Object=MibScalar
wwpLeosNtpClientMaxPollFreq=_WwpLeosNtpClientMaxPollFreq_Object((1,3,6,1,4,1,6141,2,60,18,1,1,12),_WwpLeosNtpClientMaxPollFreq_Type())
wwpLeosNtpClientMaxPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientMaxPollFreq.setStatus(_A)
_WwpLeosNtpClientOffset_Type=Integer32
_WwpLeosNtpClientOffset_Object=MibScalar
wwpLeosNtpClientOffset=_WwpLeosNtpClientOffset_Object((1,3,6,1,4,1,6141,2,60,18,1,1,13),_WwpLeosNtpClientOffset_Type())
wwpLeosNtpClientOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientOffset.setStatus(_H)
_WwpLeosNtpClientDelay_Type=Integer32
_WwpLeosNtpClientDelay_Object=MibScalar
wwpLeosNtpClientDelay=_WwpLeosNtpClientDelay_Object((1,3,6,1,4,1,6141,2,60,18,1,1,14),_WwpLeosNtpClientDelay_Type())
wwpLeosNtpClientDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientDelay.setStatus(_A)
_WwpLeosNtpClientJitter_Type=Integer32
_WwpLeosNtpClientJitter_Object=MibScalar
wwpLeosNtpClientJitter=_WwpLeosNtpClientJitter_Object((1,3,6,1,4,1,6141,2,60,18,1,1,15),_WwpLeosNtpClientJitter_Type())
wwpLeosNtpClientJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientJitter.setStatus(_A)
_WwpLeosNtpClientNtpOffset_Type=Integer32
_WwpLeosNtpClientNtpOffset_Object=MibScalar
wwpLeosNtpClientNtpOffset=_WwpLeosNtpClientNtpOffset_Object((1,3,6,1,4,1,6141,2,60,18,1,1,16),_WwpLeosNtpClientNtpOffset_Type())
wwpLeosNtpClientNtpOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientNtpOffset.setStatus(_A)
class _WwpLeosNtpClientNtpFastStartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosNtpClientNtpFastStartMode_Type.__name__=_B
_WwpLeosNtpClientNtpFastStartMode_Object=MibScalar
wwpLeosNtpClientNtpFastStartMode=_WwpLeosNtpClientNtpFastStartMode_Object((1,3,6,1,4,1,6141,2,60,18,1,1,17),_WwpLeosNtpClientNtpFastStartMode_Type())
wwpLeosNtpClientNtpFastStartMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientNtpFastStartMode.setStatus(_A)
_WwpLeosNtpMulticastTable_Object=MibTable
wwpLeosNtpMulticastTable=_WwpLeosNtpMulticastTable_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18))
if mibBuilder.loadTexts:wwpLeosNtpMulticastTable.setStatus(_A)
_WwpLeosNtpMulticastEntry_Object=MibTableRow
wwpLeosNtpMulticastEntry=_WwpLeosNtpMulticastEntry_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18,1))
wwpLeosNtpMulticastEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wwpLeosNtpMulticastEntry.setStatus(_A)
class _WwpLeosNtpMulticastIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosNtpMulticastIndex_Type.__name__=_B
_WwpLeosNtpMulticastIndex_Object=MibTableColumn
wwpLeosNtpMulticastIndex=_WwpLeosNtpMulticastIndex_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18,1,1),_WwpLeosNtpMulticastIndex_Type())
wwpLeosNtpMulticastIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosNtpMulticastIndex.setStatus(_A)
_WwpLeosNtpMulticastInetAddrType_Type=InetAddressType
_WwpLeosNtpMulticastInetAddrType_Object=MibTableColumn
wwpLeosNtpMulticastInetAddrType=_WwpLeosNtpMulticastInetAddrType_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18,1,2),_WwpLeosNtpMulticastInetAddrType_Type())
wwpLeosNtpMulticastInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpMulticastInetAddrType.setStatus(_A)
_WwpLeosNtpMulticastInetAddr_Type=InetAddress
_WwpLeosNtpMulticastInetAddr_Object=MibTableColumn
wwpLeosNtpMulticastInetAddr=_WwpLeosNtpMulticastInetAddr_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18,1,3),_WwpLeosNtpMulticastInetAddr_Type())
wwpLeosNtpMulticastInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpMulticastInetAddr.setStatus(_A)
_WwpLeosNtpMulticastRowStatus_Type=RowStatus
_WwpLeosNtpMulticastRowStatus_Object=MibTableColumn
wwpLeosNtpMulticastRowStatus=_WwpLeosNtpMulticastRowStatus_Object((1,3,6,1,4,1,6141,2,60,18,1,1,18,1,4),_WwpLeosNtpMulticastRowStatus_Type())
wwpLeosNtpMulticastRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosNtpMulticastRowStatus.setStatus(_A)
class _WwpLeosNtpClientSyncChangeNotifAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosNtpClientSyncChangeNotifAdminState_Type.__name__=_B
_WwpLeosNtpClientSyncChangeNotifAdminState_Object=MibScalar
wwpLeosNtpClientSyncChangeNotifAdminState=_WwpLeosNtpClientSyncChangeNotifAdminState_Object((1,3,6,1,4,1,6141,2,60,18,1,1,19),_WwpLeosNtpClientSyncChangeNotifAdminState_Type())
wwpLeosNtpClientSyncChangeNotifAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNtpClientSyncChangeNotifAdminState.setStatus(_A)
_WwpLeosNtpClientNotifAttrs_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientNotifAttrs=_WwpLeosNtpClientNotifAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,1,2))
class _WwpLeosNtpClientSyncState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('synchronized',1),('not-synchronized',2)))
_WwpLeosNtpClientSyncState_Type.__name__=_B
_WwpLeosNtpClientSyncState_Object=MibScalar
wwpLeosNtpClientSyncState=_WwpLeosNtpClientSyncState_Object((1,3,6,1,4,1,6141,2,60,18,1,2,1),_WwpLeosNtpClientSyncState_Type())
wwpLeosNtpClientSyncState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNtpClientSyncState.setStatus(_A)
_WwpLeosNtpClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBNotificationPrefix=_WwpLeosNtpClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,2))
_WwpLeosNtpClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBNotifications=_WwpLeosNtpClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,2,0))
_WwpLeosNtpClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBConformance=_WwpLeosNtpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,3))
_WwpLeosNtpClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBCompliances=_WwpLeosNtpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,3,1))
_WwpLeosNtpClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosNtpClientMIBGroups=_WwpLeosNtpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,18,3,2))
wwpLeosNtpClientSyncStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,18,2,0,1))
wwpLeosNtpClientSyncStatusChangeNotification.setObjects((_E,_P))
if mibBuilder.loadTexts:wwpLeosNtpClientSyncStatusChangeNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_J:Md5Key,'wwpLeosNtpClientMIB':wwpLeosNtpClientMIB,'wwpLeosNtpClientMIBObjects':wwpLeosNtpClientMIBObjects,'wwpLeosNtpClient':wwpLeosNtpClient,'wwpLeosNtpClientState':wwpLeosNtpClientState,'wwpLeosNtpClientMode':wwpLeosNtpClientMode,'wwpLeosNtpClientPollFreq':wwpLeosNtpClientPollFreq,'wwpLeosNtpClientTable':wwpLeosNtpClientTable,'wwpLeosNtpClientEntry':wwpLeosNtpClientEntry,_K:wwpLeosNtpServerIndex,'wwpLeosNtpServerAddrType':wwpLeosNtpServerAddrType,'wwpLeosNtpServerAddr':wwpLeosNtpServerAddr,'wwpLeosNtpServerResolvedAddr':wwpLeosNtpServerResolvedAddr,'wwpLeosNtpServerUserPri':wwpLeosNtpServerUserPri,'wwpLeosNtpServerDhcpPri':wwpLeosNtpServerDhcpPri,'wwpLeosNtpServerUserAdminState':wwpLeosNtpServerUserAdminState,'wwpLeosNtpServerScope':wwpLeosNtpServerScope,'wwpLeosNtpServerOperState':wwpLeosNtpServerOperState,'wwpLeosNtpServerStatus':wwpLeosNtpServerStatus,'wwpLeosNtpServerKeyId':wwpLeosNtpServerKeyId,'wwpLeosNtpServerState':wwpLeosNtpServerState,'wwpLeosNtpServerResolvedInetAddrType':wwpLeosNtpServerResolvedInetAddrType,'wwpLeosNtpServerResolvedInetAddr':wwpLeosNtpServerResolvedInetAddr,'wwpLeosNtpAuthTable':wwpLeosNtpAuthTable,'wwpLeosNtpAuthEntry':wwpLeosNtpAuthEntry,_N:wwpLeosNtpAuthKeyId,'wwpLeosNtpAuthMd5Key':wwpLeosNtpAuthMd5Key,'wwpLeosNtpAuthRowStatus':wwpLeosNtpAuthRowStatus,'wwpLeosNtpAuthMD5KeyEnc':wwpLeosNtpAuthMD5KeyEnc,'wwpLeosNtpClientMD5State':wwpLeosNtpClientMD5State,'wwpLeosNtpClientDrift':wwpLeosNtpClientDrift,'wwpLeosNtpClientFastOffset':wwpLeosNtpClientFastOffset,'wwpLeosNtpClientSlowOffset':wwpLeosNtpClientSlowOffset,'wwpLeosNtpClientMinPollFreq':wwpLeosNtpClientMinPollFreq,'wwpLeosNtpClientMaxPollFreq':wwpLeosNtpClientMaxPollFreq,'wwpLeosNtpClientOffset':wwpLeosNtpClientOffset,'wwpLeosNtpClientDelay':wwpLeosNtpClientDelay,'wwpLeosNtpClientJitter':wwpLeosNtpClientJitter,'wwpLeosNtpClientNtpOffset':wwpLeosNtpClientNtpOffset,'wwpLeosNtpClientNtpFastStartMode':wwpLeosNtpClientNtpFastStartMode,'wwpLeosNtpMulticastTable':wwpLeosNtpMulticastTable,'wwpLeosNtpMulticastEntry':wwpLeosNtpMulticastEntry,_O:wwpLeosNtpMulticastIndex,'wwpLeosNtpMulticastInetAddrType':wwpLeosNtpMulticastInetAddrType,'wwpLeosNtpMulticastInetAddr':wwpLeosNtpMulticastInetAddr,'wwpLeosNtpMulticastRowStatus':wwpLeosNtpMulticastRowStatus,'wwpLeosNtpClientSyncChangeNotifAdminState':wwpLeosNtpClientSyncChangeNotifAdminState,'wwpLeosNtpClientNotifAttrs':wwpLeosNtpClientNotifAttrs,_P:wwpLeosNtpClientSyncState,'wwpLeosNtpClientMIBNotificationPrefix':wwpLeosNtpClientMIBNotificationPrefix,'wwpLeosNtpClientMIBNotifications':wwpLeosNtpClientMIBNotifications,'wwpLeosNtpClientSyncStatusChangeNotification':wwpLeosNtpClientSyncStatusChangeNotification,'wwpLeosNtpClientMIBConformance':wwpLeosNtpClientMIBConformance,'wwpLeosNtpClientMIBCompliances':wwpLeosNtpClientMIBCompliances,'wwpLeosNtpClientMIBGroups':wwpLeosNtpClientMIBGroups})