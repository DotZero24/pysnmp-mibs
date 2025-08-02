_AC='pktcEUEDevPerDeviceGroup'
_AB='pktcEUEDevBSFGroup'
_AA='pktcEUEDevPCSCFGroup'
_A9='pktcEUEDevDnsGroup'
_A8='pktcEUEDevOpGroup'
_A7='pktcEUEDevProfileGroup'
_A6='pktcEUEDevSipPort'
_A5='pktcEUECBData'
_A4='pktcEUECBEnable'
_A3='pktcEUECBSupport'
_A2='pktcEUEDevBSFRowStatus'
_A1='pktcEUEDevBSFAddr'
_A0='pktcEUEDevBSFAddrType'
_z='pktcEUEDevPCSCFSubscribeRetry'
_y='pktcEUEDevPCSCFBaseTimeAllNotFailed'
_x='pktcEUEDevPCSCFBaseTimeAllFailed'
_w='pktcEUEDevPCSCFMaxTime'
_v='pktcEUEDevPCSCFInviteAttempts'
_u='pktcEUEDevPCSCFRowStatus'
_t='pktcEUEDevPCSCFTimerTD'
_s='pktcEUEDevPCSCFTimerT4'
_r='pktcEUEDevPCSCFTimerT2'
_q='pktcEUEDevPCSCFTimerT1'
_p='pktcEUEDevPCSCFUsedInetAddress'
_o='pktcEUEDevPCSCFUsedInetAddressType'
_n='pktcEUEDevPCSCFUsedProtocol'
_m='pktcEUEDevPCSCFSipPort'
_l='pktcEUEDevPCSCFAddr'
_k='pktcEUEDevPCSCFAddrType'
_j='pktcEUEDevDnsRowStatus'
_i='pktcEUEDevDnsAddr'
_h='pktcEUEDevDnsAddrType'
_g='pktcEUEDevOpRowStatus'
_f='pktcEUEDevOpSTUNRelayCreds'
_e='pktcEUEDevOpSTUNRelayCredsType'
_d='pktcEUEDevOpSTUNRelayAddrPort'
_c='pktcEUEDevOpSTUNRelayAddr'
_b='pktcEUEDevOpSTUNRelayAddrType'
_a='pktcEUEDevOpSTUNAddrPort'
_Z='pktcEUEDevOpSTUNAddr'
_Y='pktcEUEDevOpSTUNAddrType'
_X='pktcEUEDevOpDomain'
_W='pktcEUEDevProfileVersion'
_V='pktcEUEDevBSFIndex'
_U='pktcEUEDevBSFASType'
_T='pktcEUEDevPCSCFIndex'
_S='pktcEUEDevDnsIndex'
_R='TruthValue'
_Q='SnmpAdminString'
_P='PktcEUETCCredsType'
_O='PktcEUETCCreds'
_N='OctetString'
_M='read-write'
_L='seconds'
_K='milliseconds'
_J='not-accessible'
_I='pktcEUEDevOpIndex'
_H='InetPortNumber'
_G='InetAddressType'
_F='InetAddress'
_E='read-only'
_D='Unsigned32'
_C='read-create'
_B='CL-PKTC-EUE-DEV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PktcEUETCCreds,PktcEUETCCredsType=mibBuilder.importSymbols('CL-PKTC-EUE-TC-MIB',_O,_P)
pktcEUEMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcEUEMibs')
InetAddress,InetAddressDNS,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressDNS',_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_R)
pktcEUEDevMIB=ModuleIdentity((1,3,6,1,4,1,4491,2,2,10,3))
if mibBuilder.loadTexts:pktcEUEDevMIB.setRevisions(('2010-04-26 00:00','2008-07-10 00:00','2007-11-06 00:00'))
class PktcEUEDevSipProtID(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('udp',2),('tcp',3),('tls',4)))
_PktcEUEDevNotification_ObjectIdentity=ObjectIdentity
pktcEUEDevNotification=_PktcEUEDevNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,0))
_PktcEUEDevObjects_ObjectIdentity=ObjectIdentity
pktcEUEDevObjects=_PktcEUEDevObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,1))
_PktcEUEDevProfile_ObjectIdentity=ObjectIdentity
pktcEUEDevProfile=_PktcEUEDevProfile_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,1,1))
class _PktcEUEDevProfileVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_PktcEUEDevProfileVersion_Type.__name__=_Q
_PktcEUEDevProfileVersion_Object=MibScalar
pktcEUEDevProfileVersion=_PktcEUEDevProfileVersion_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,1),_PktcEUEDevProfileVersion_Type())
pktcEUEDevProfileVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevProfileVersion.setStatus(_A)
_PktcEUEDevOpTable_Object=MibTable
pktcEUEDevOpTable=_PktcEUEDevOpTable_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2))
if mibBuilder.loadTexts:pktcEUEDevOpTable.setStatus(_A)
_PktcEUEDevOpEntry_Object=MibTableRow
pktcEUEDevOpEntry=_PktcEUEDevOpEntry_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1))
pktcEUEDevOpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:pktcEUEDevOpEntry.setStatus(_A)
class _PktcEUEDevOpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PktcEUEDevOpIndex_Type.__name__=_D
_PktcEUEDevOpIndex_Object=MibTableColumn
pktcEUEDevOpIndex=_PktcEUEDevOpIndex_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,1),_PktcEUEDevOpIndex_Type())
pktcEUEDevOpIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcEUEDevOpIndex.setStatus(_A)
_PktcEUEDevOpDomain_Type=InetAddressDNS
_PktcEUEDevOpDomain_Object=MibTableColumn
pktcEUEDevOpDomain=_PktcEUEDevOpDomain_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,2),_PktcEUEDevOpDomain_Type())
pktcEUEDevOpDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpDomain.setStatus(_A)
class _PktcEUEDevOpSTUNAddrType_Type(InetAddressType):defaultValue=0
_PktcEUEDevOpSTUNAddrType_Type.__name__=_G
_PktcEUEDevOpSTUNAddrType_Object=MibTableColumn
pktcEUEDevOpSTUNAddrType=_PktcEUEDevOpSTUNAddrType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,3),_PktcEUEDevOpSTUNAddrType_Type())
pktcEUEDevOpSTUNAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNAddrType.setStatus(_A)
class _PktcEUEDevOpSTUNAddr_Type(InetAddress):defaultValue=OctetString('')
_PktcEUEDevOpSTUNAddr_Type.__name__=_F
_PktcEUEDevOpSTUNAddr_Object=MibTableColumn
pktcEUEDevOpSTUNAddr=_PktcEUEDevOpSTUNAddr_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,4),_PktcEUEDevOpSTUNAddr_Type())
pktcEUEDevOpSTUNAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNAddr.setStatus(_A)
class _PktcEUEDevOpSTUNAddrPort_Type(InetPortNumber):defaultValue=0
_PktcEUEDevOpSTUNAddrPort_Type.__name__=_H
_PktcEUEDevOpSTUNAddrPort_Object=MibTableColumn
pktcEUEDevOpSTUNAddrPort=_PktcEUEDevOpSTUNAddrPort_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,5),_PktcEUEDevOpSTUNAddrPort_Type())
pktcEUEDevOpSTUNAddrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNAddrPort.setStatus(_A)
class _PktcEUEDevOpSTUNRelayAddrType_Type(InetAddressType):defaultValue=0
_PktcEUEDevOpSTUNRelayAddrType_Type.__name__=_G
_PktcEUEDevOpSTUNRelayAddrType_Object=MibTableColumn
pktcEUEDevOpSTUNRelayAddrType=_PktcEUEDevOpSTUNRelayAddrType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,6),_PktcEUEDevOpSTUNRelayAddrType_Type())
pktcEUEDevOpSTUNRelayAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNRelayAddrType.setStatus(_A)
class _PktcEUEDevOpSTUNRelayAddr_Type(InetAddress):defaultValue=OctetString('')
_PktcEUEDevOpSTUNRelayAddr_Type.__name__=_F
_PktcEUEDevOpSTUNRelayAddr_Object=MibTableColumn
pktcEUEDevOpSTUNRelayAddr=_PktcEUEDevOpSTUNRelayAddr_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,7),_PktcEUEDevOpSTUNRelayAddr_Type())
pktcEUEDevOpSTUNRelayAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNRelayAddr.setStatus(_A)
class _PktcEUEDevOpSTUNRelayAddrPort_Type(InetPortNumber):defaultValue=0
_PktcEUEDevOpSTUNRelayAddrPort_Type.__name__=_H
_PktcEUEDevOpSTUNRelayAddrPort_Object=MibTableColumn
pktcEUEDevOpSTUNRelayAddrPort=_PktcEUEDevOpSTUNRelayAddrPort_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,8),_PktcEUEDevOpSTUNRelayAddrPort_Type())
pktcEUEDevOpSTUNRelayAddrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNRelayAddrPort.setStatus(_A)
class _PktcEUEDevOpSTUNRelayCredsType_Type(PktcEUETCCredsType):defaultValue=2
_PktcEUEDevOpSTUNRelayCredsType_Type.__name__=_P
_PktcEUEDevOpSTUNRelayCredsType_Object=MibTableColumn
pktcEUEDevOpSTUNRelayCredsType=_PktcEUEDevOpSTUNRelayCredsType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,9),_PktcEUEDevOpSTUNRelayCredsType_Type())
pktcEUEDevOpSTUNRelayCredsType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNRelayCredsType.setStatus(_A)
class _PktcEUEDevOpSTUNRelayCreds_Type(PktcEUETCCreds):defaultValue=OctetString('')
_PktcEUEDevOpSTUNRelayCreds_Type.__name__=_O
_PktcEUEDevOpSTUNRelayCreds_Object=MibTableColumn
pktcEUEDevOpSTUNRelayCreds=_PktcEUEDevOpSTUNRelayCreds_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,10),_PktcEUEDevOpSTUNRelayCreds_Type())
pktcEUEDevOpSTUNRelayCreds.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpSTUNRelayCreds.setStatus(_A)
_PktcEUEDevOpRowStatus_Type=RowStatus
_PktcEUEDevOpRowStatus_Object=MibTableColumn
pktcEUEDevOpRowStatus=_PktcEUEDevOpRowStatus_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,2,1,11),_PktcEUEDevOpRowStatus_Type())
pktcEUEDevOpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevOpRowStatus.setStatus(_A)
_PktcEUEDevDnsTable_Object=MibTable
pktcEUEDevDnsTable=_PktcEUEDevDnsTable_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3))
if mibBuilder.loadTexts:pktcEUEDevDnsTable.setStatus(_A)
_PktcEUEDevDnsEntry_Object=MibTableRow
pktcEUEDevDnsEntry=_PktcEUEDevDnsEntry_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3,1))
pktcEUEDevDnsEntry.setIndexNames((0,_B,_I),(0,_B,_S))
if mibBuilder.loadTexts:pktcEUEDevDnsEntry.setStatus(_A)
class _PktcEUEDevDnsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PktcEUEDevDnsIndex_Type.__name__=_D
_PktcEUEDevDnsIndex_Object=MibTableColumn
pktcEUEDevDnsIndex=_PktcEUEDevDnsIndex_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3,1,1),_PktcEUEDevDnsIndex_Type())
pktcEUEDevDnsIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcEUEDevDnsIndex.setStatus(_A)
class _PktcEUEDevDnsAddrType_Type(InetAddressType):defaultValue=0
_PktcEUEDevDnsAddrType_Type.__name__=_G
_PktcEUEDevDnsAddrType_Object=MibTableColumn
pktcEUEDevDnsAddrType=_PktcEUEDevDnsAddrType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3,1,2),_PktcEUEDevDnsAddrType_Type())
pktcEUEDevDnsAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevDnsAddrType.setStatus(_A)
class _PktcEUEDevDnsAddr_Type(InetAddress):defaultValue=OctetString('')
_PktcEUEDevDnsAddr_Type.__name__=_F
_PktcEUEDevDnsAddr_Object=MibTableColumn
pktcEUEDevDnsAddr=_PktcEUEDevDnsAddr_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3,1,3),_PktcEUEDevDnsAddr_Type())
pktcEUEDevDnsAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevDnsAddr.setStatus(_A)
_PktcEUEDevDnsRowStatus_Type=RowStatus
_PktcEUEDevDnsRowStatus_Object=MibTableColumn
pktcEUEDevDnsRowStatus=_PktcEUEDevDnsRowStatus_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,3,1,4),_PktcEUEDevDnsRowStatus_Type())
pktcEUEDevDnsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevDnsRowStatus.setStatus(_A)
_PktcEUEDevPCSCFTable_Object=MibTable
pktcEUEDevPCSCFTable=_PktcEUEDevPCSCFTable_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4))
if mibBuilder.loadTexts:pktcEUEDevPCSCFTable.setStatus(_A)
_PktcEUEDevPCSCFEntry_Object=MibTableRow
pktcEUEDevPCSCFEntry=_PktcEUEDevPCSCFEntry_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1))
pktcEUEDevPCSCFEntry.setIndexNames((0,_B,_I),(0,_B,_T))
if mibBuilder.loadTexts:pktcEUEDevPCSCFEntry.setStatus(_A)
class _PktcEUEDevPCSCFIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PktcEUEDevPCSCFIndex_Type.__name__=_D
_PktcEUEDevPCSCFIndex_Object=MibTableColumn
pktcEUEDevPCSCFIndex=_PktcEUEDevPCSCFIndex_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,1),_PktcEUEDevPCSCFIndex_Type())
pktcEUEDevPCSCFIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcEUEDevPCSCFIndex.setStatus(_A)
class _PktcEUEDevPCSCFAddrType_Type(InetAddressType):defaultValue=0
_PktcEUEDevPCSCFAddrType_Type.__name__=_G
_PktcEUEDevPCSCFAddrType_Object=MibTableColumn
pktcEUEDevPCSCFAddrType=_PktcEUEDevPCSCFAddrType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,2),_PktcEUEDevPCSCFAddrType_Type())
pktcEUEDevPCSCFAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFAddrType.setStatus(_A)
class _PktcEUEDevPCSCFAddr_Type(InetAddress):defaultValue=OctetString('')
_PktcEUEDevPCSCFAddr_Type.__name__=_F
_PktcEUEDevPCSCFAddr_Object=MibTableColumn
pktcEUEDevPCSCFAddr=_PktcEUEDevPCSCFAddr_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,3),_PktcEUEDevPCSCFAddr_Type())
pktcEUEDevPCSCFAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFAddr.setStatus(_A)
class _PktcEUEDevPCSCFSipPort_Type(InetPortNumber):defaultValue=5060
_PktcEUEDevPCSCFSipPort_Type.__name__=_H
_PktcEUEDevPCSCFSipPort_Object=MibTableColumn
pktcEUEDevPCSCFSipPort=_PktcEUEDevPCSCFSipPort_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,4),_PktcEUEDevPCSCFSipPort_Type())
pktcEUEDevPCSCFSipPort.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFSipPort.setStatus(_A)
_PktcEUEDevPCSCFUsedProtocol_Type=PktcEUEDevSipProtID
_PktcEUEDevPCSCFUsedProtocol_Object=MibTableColumn
pktcEUEDevPCSCFUsedProtocol=_PktcEUEDevPCSCFUsedProtocol_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,5),_PktcEUEDevPCSCFUsedProtocol_Type())
pktcEUEDevPCSCFUsedProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevPCSCFUsedProtocol.setStatus(_A)
_PktcEUEDevPCSCFUsedInetAddressType_Type=InetAddressType
_PktcEUEDevPCSCFUsedInetAddressType_Object=MibTableColumn
pktcEUEDevPCSCFUsedInetAddressType=_PktcEUEDevPCSCFUsedInetAddressType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,6),_PktcEUEDevPCSCFUsedInetAddressType_Type())
pktcEUEDevPCSCFUsedInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevPCSCFUsedInetAddressType.setStatus(_A)
_PktcEUEDevPCSCFUsedInetAddress_Type=InetAddress
_PktcEUEDevPCSCFUsedInetAddress_Object=MibTableColumn
pktcEUEDevPCSCFUsedInetAddress=_PktcEUEDevPCSCFUsedInetAddress_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,7),_PktcEUEDevPCSCFUsedInetAddress_Type())
pktcEUEDevPCSCFUsedInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevPCSCFUsedInetAddress.setStatus(_A)
class _PktcEUEDevPCSCFTimerT1_Type(Unsigned32):defaultValue=500
_PktcEUEDevPCSCFTimerT1_Type.__name__=_D
_PktcEUEDevPCSCFTimerT1_Object=MibTableColumn
pktcEUEDevPCSCFTimerT1=_PktcEUEDevPCSCFTimerT1_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,8),_PktcEUEDevPCSCFTimerT1_Type())
pktcEUEDevPCSCFTimerT1.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT1.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT1.setUnits(_K)
class _PktcEUEDevPCSCFTimerT2_Type(Unsigned32):defaultValue=4000
_PktcEUEDevPCSCFTimerT2_Type.__name__=_D
_PktcEUEDevPCSCFTimerT2_Object=MibTableColumn
pktcEUEDevPCSCFTimerT2=_PktcEUEDevPCSCFTimerT2_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,9),_PktcEUEDevPCSCFTimerT2_Type())
pktcEUEDevPCSCFTimerT2.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT2.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT2.setUnits(_K)
class _PktcEUEDevPCSCFTimerT4_Type(Unsigned32):defaultValue=5000
_PktcEUEDevPCSCFTimerT4_Type.__name__=_D
_PktcEUEDevPCSCFTimerT4_Object=MibTableColumn
pktcEUEDevPCSCFTimerT4=_PktcEUEDevPCSCFTimerT4_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,10),_PktcEUEDevPCSCFTimerT4_Type())
pktcEUEDevPCSCFTimerT4.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT4.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerT4.setUnits(_K)
class _PktcEUEDevPCSCFTimerTD_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(32000,4294967295))
_PktcEUEDevPCSCFTimerTD_Type.__name__=_D
_PktcEUEDevPCSCFTimerTD_Object=MibTableColumn
pktcEUEDevPCSCFTimerTD=_PktcEUEDevPCSCFTimerTD_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,11),_PktcEUEDevPCSCFTimerTD_Type())
pktcEUEDevPCSCFTimerTD.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerTD.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFTimerTD.setUnits(_K)
_PktcEUEDevPCSCFRowStatus_Type=RowStatus
_PktcEUEDevPCSCFRowStatus_Object=MibTableColumn
pktcEUEDevPCSCFRowStatus=_PktcEUEDevPCSCFRowStatus_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,12),_PktcEUEDevPCSCFRowStatus_Type())
pktcEUEDevPCSCFRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFRowStatus.setStatus(_A)
class _PktcEUEDevPCSCFInviteAttempts_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PktcEUEDevPCSCFInviteAttempts_Type.__name__=_D
_PktcEUEDevPCSCFInviteAttempts_Object=MibTableColumn
pktcEUEDevPCSCFInviteAttempts=_PktcEUEDevPCSCFInviteAttempts_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,13),_PktcEUEDevPCSCFInviteAttempts_Type())
pktcEUEDevPCSCFInviteAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFInviteAttempts.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFInviteAttempts.setUnits('attempts')
class _PktcEUEDevPCSCFMaxTime_Type(Unsigned32):defaultValue=1800
_PktcEUEDevPCSCFMaxTime_Type.__name__=_D
_PktcEUEDevPCSCFMaxTime_Object=MibTableColumn
pktcEUEDevPCSCFMaxTime=_PktcEUEDevPCSCFMaxTime_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,14),_PktcEUEDevPCSCFMaxTime_Type())
pktcEUEDevPCSCFMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFMaxTime.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFMaxTime.setUnits(_L)
class _PktcEUEDevPCSCFBaseTimeAllFailed_Type(Unsigned32):defaultValue=30
_PktcEUEDevPCSCFBaseTimeAllFailed_Type.__name__=_D
_PktcEUEDevPCSCFBaseTimeAllFailed_Object=MibTableColumn
pktcEUEDevPCSCFBaseTimeAllFailed=_PktcEUEDevPCSCFBaseTimeAllFailed_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,15),_PktcEUEDevPCSCFBaseTimeAllFailed_Type())
pktcEUEDevPCSCFBaseTimeAllFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFBaseTimeAllFailed.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFBaseTimeAllFailed.setUnits(_L)
class _PktcEUEDevPCSCFBaseTimeAllNotFailed_Type(Unsigned32):defaultValue=90
_PktcEUEDevPCSCFBaseTimeAllNotFailed_Type.__name__=_D
_PktcEUEDevPCSCFBaseTimeAllNotFailed_Object=MibTableColumn
pktcEUEDevPCSCFBaseTimeAllNotFailed=_PktcEUEDevPCSCFBaseTimeAllNotFailed_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,16),_PktcEUEDevPCSCFBaseTimeAllNotFailed_Type())
pktcEUEDevPCSCFBaseTimeAllNotFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFBaseTimeAllNotFailed.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFBaseTimeAllNotFailed.setUnits(_L)
class _PktcEUEDevPCSCFSubscribeRetry_Type(Unsigned32):defaultValue=900
_PktcEUEDevPCSCFSubscribeRetry_Type.__name__=_D
_PktcEUEDevPCSCFSubscribeRetry_Object=MibTableColumn
pktcEUEDevPCSCFSubscribeRetry=_PktcEUEDevPCSCFSubscribeRetry_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,4,1,17),_PktcEUEDevPCSCFSubscribeRetry_Type())
pktcEUEDevPCSCFSubscribeRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevPCSCFSubscribeRetry.setStatus(_A)
if mibBuilder.loadTexts:pktcEUEDevPCSCFSubscribeRetry.setUnits(_L)
_PktcEUEDevBSFTable_Object=MibTable
pktcEUEDevBSFTable=_PktcEUEDevBSFTable_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5))
if mibBuilder.loadTexts:pktcEUEDevBSFTable.setStatus(_A)
_PktcEUEDevBSFEntry_Object=MibTableRow
pktcEUEDevBSFEntry=_PktcEUEDevBSFEntry_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1))
pktcEUEDevBSFEntry.setIndexNames((0,_B,_I),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:pktcEUEDevBSFEntry.setStatus(_A)
_PktcEUEDevBSFASType_Type=SnmpAdminString
_PktcEUEDevBSFASType_Object=MibTableColumn
pktcEUEDevBSFASType=_PktcEUEDevBSFASType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1,1),_PktcEUEDevBSFASType_Type())
pktcEUEDevBSFASType.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcEUEDevBSFASType.setStatus(_A)
class _PktcEUEDevBSFIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PktcEUEDevBSFIndex_Type.__name__=_D
_PktcEUEDevBSFIndex_Object=MibTableColumn
pktcEUEDevBSFIndex=_PktcEUEDevBSFIndex_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1,2),_PktcEUEDevBSFIndex_Type())
pktcEUEDevBSFIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcEUEDevBSFIndex.setStatus(_A)
class _PktcEUEDevBSFAddrType_Type(InetAddressType):defaultValue=0
_PktcEUEDevBSFAddrType_Type.__name__=_G
_PktcEUEDevBSFAddrType_Object=MibTableColumn
pktcEUEDevBSFAddrType=_PktcEUEDevBSFAddrType_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1,3),_PktcEUEDevBSFAddrType_Type())
pktcEUEDevBSFAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevBSFAddrType.setStatus(_A)
class _PktcEUEDevBSFAddr_Type(InetAddress):defaultValue=OctetString('')
_PktcEUEDevBSFAddr_Type.__name__=_F
_PktcEUEDevBSFAddr_Object=MibTableColumn
pktcEUEDevBSFAddr=_PktcEUEDevBSFAddr_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1,4),_PktcEUEDevBSFAddr_Type())
pktcEUEDevBSFAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUEDevBSFAddr.setStatus(_A)
_PktcEUEDevBSFRowStatus_Type=RowStatus
_PktcEUEDevBSFRowStatus_Object=MibTableColumn
pktcEUEDevBSFRowStatus=_PktcEUEDevBSFRowStatus_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,5,1,5),_PktcEUEDevBSFRowStatus_Type())
pktcEUEDevBSFRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcEUEDevBSFRowStatus.setStatus(_A)
_PktcEUECBSupport_Type=TruthValue
_PktcEUECBSupport_Object=MibScalar
pktcEUECBSupport=_PktcEUECBSupport_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,6),_PktcEUECBSupport_Type())
pktcEUECBSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcEUECBSupport.setStatus(_A)
class _PktcEUECBEnable_Type(TruthValue):defaultValue=2
_PktcEUECBEnable_Type.__name__=_R
_PktcEUECBEnable_Object=MibScalar
pktcEUECBEnable=_PktcEUECBEnable_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,7),_PktcEUECBEnable_Type())
pktcEUECBEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcEUECBEnable.setStatus(_A)
class _PktcEUECBData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_PktcEUECBData_Type.__name__=_N
_PktcEUECBData_Object=MibScalar
pktcEUECBData=_PktcEUECBData_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,8),_PktcEUECBData_Type())
pktcEUECBData.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcEUECBData.setStatus(_A)
class _PktcEUEDevSipPort_Type(InetPortNumber):defaultValue=5060
_PktcEUEDevSipPort_Type.__name__=_H
_PktcEUEDevSipPort_Object=MibScalar
pktcEUEDevSipPort=_PktcEUEDevSipPort_Object((1,3,6,1,4,1,4491,2,2,10,3,1,1,9),_PktcEUEDevSipPort_Type())
pktcEUEDevSipPort.setMaxAccess(_M)
if mibBuilder.loadTexts:pktcEUEDevSipPort.setStatus(_A)
_PktcEUEDevConformance_ObjectIdentity=ObjectIdentity
pktcEUEDevConformance=_PktcEUEDevConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,2))
_PktcEUEDevCompliances_ObjectIdentity=ObjectIdentity
pktcEUEDevCompliances=_PktcEUEDevCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,2,1))
_PktcEUEDevGroups_ObjectIdentity=ObjectIdentity
pktcEUEDevGroups=_PktcEUEDevGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,3,2,2))
pktcEUEDevProfileGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,1))
pktcEUEDevProfileGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:pktcEUEDevProfileGroup.setStatus(_A)
pktcEUEDevOpGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,2))
pktcEUEDevOpGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:pktcEUEDevOpGroup.setStatus(_A)
pktcEUEDevDnsGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,3))
pktcEUEDevDnsGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:pktcEUEDevDnsGroup.setStatus(_A)
pktcEUEDevPCSCFGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,4))
pktcEUEDevPCSCFGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:pktcEUEDevPCSCFGroup.setStatus(_A)
pktcEUEDevBSFGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,5))
pktcEUEDevBSFGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:pktcEUEDevBSFGroup.setStatus(_A)
pktcEUEDevPerDeviceGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,3,2,2,6))
pktcEUEDevPerDeviceGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:pktcEUEDevPerDeviceGroup.setStatus(_A)
pktcEUEDevMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,10,3,2,1,1))
pktcEUEDevMIBCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:pktcEUEDevMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PktcEUEDevSipProtID':PktcEUEDevSipProtID,'pktcEUEDevMIB':pktcEUEDevMIB,'pktcEUEDevNotification':pktcEUEDevNotification,'pktcEUEDevObjects':pktcEUEDevObjects,'pktcEUEDevProfile':pktcEUEDevProfile,_W:pktcEUEDevProfileVersion,'pktcEUEDevOpTable':pktcEUEDevOpTable,'pktcEUEDevOpEntry':pktcEUEDevOpEntry,_I:pktcEUEDevOpIndex,_X:pktcEUEDevOpDomain,_Y:pktcEUEDevOpSTUNAddrType,_Z:pktcEUEDevOpSTUNAddr,_a:pktcEUEDevOpSTUNAddrPort,_b:pktcEUEDevOpSTUNRelayAddrType,_c:pktcEUEDevOpSTUNRelayAddr,_d:pktcEUEDevOpSTUNRelayAddrPort,_e:pktcEUEDevOpSTUNRelayCredsType,_f:pktcEUEDevOpSTUNRelayCreds,_g:pktcEUEDevOpRowStatus,'pktcEUEDevDnsTable':pktcEUEDevDnsTable,'pktcEUEDevDnsEntry':pktcEUEDevDnsEntry,_S:pktcEUEDevDnsIndex,_h:pktcEUEDevDnsAddrType,_i:pktcEUEDevDnsAddr,_j:pktcEUEDevDnsRowStatus,'pktcEUEDevPCSCFTable':pktcEUEDevPCSCFTable,'pktcEUEDevPCSCFEntry':pktcEUEDevPCSCFEntry,_T:pktcEUEDevPCSCFIndex,_k:pktcEUEDevPCSCFAddrType,_l:pktcEUEDevPCSCFAddr,_m:pktcEUEDevPCSCFSipPort,_n:pktcEUEDevPCSCFUsedProtocol,_o:pktcEUEDevPCSCFUsedInetAddressType,_p:pktcEUEDevPCSCFUsedInetAddress,_q:pktcEUEDevPCSCFTimerT1,_r:pktcEUEDevPCSCFTimerT2,_s:pktcEUEDevPCSCFTimerT4,_t:pktcEUEDevPCSCFTimerTD,_u:pktcEUEDevPCSCFRowStatus,_v:pktcEUEDevPCSCFInviteAttempts,_w:pktcEUEDevPCSCFMaxTime,_x:pktcEUEDevPCSCFBaseTimeAllFailed,_y:pktcEUEDevPCSCFBaseTimeAllNotFailed,_z:pktcEUEDevPCSCFSubscribeRetry,'pktcEUEDevBSFTable':pktcEUEDevBSFTable,'pktcEUEDevBSFEntry':pktcEUEDevBSFEntry,_U:pktcEUEDevBSFASType,_V:pktcEUEDevBSFIndex,_A0:pktcEUEDevBSFAddrType,_A1:pktcEUEDevBSFAddr,_A2:pktcEUEDevBSFRowStatus,_A3:pktcEUECBSupport,_A4:pktcEUECBEnable,_A5:pktcEUECBData,_A6:pktcEUEDevSipPort,'pktcEUEDevConformance':pktcEUEDevConformance,'pktcEUEDevCompliances':pktcEUEDevCompliances,'pktcEUEDevMIBCompliance':pktcEUEDevMIBCompliance,'pktcEUEDevGroups':pktcEUEDevGroups,_A7:pktcEUEDevProfileGroup,_A8:pktcEUEDevOpGroup,_A9:pktcEUEDevDnsGroup,_AA:pktcEUEDevPCSCFGroup,_AB:pktcEUEDevBSFGroup,_AC:pktcEUEDevPerDeviceGroup})