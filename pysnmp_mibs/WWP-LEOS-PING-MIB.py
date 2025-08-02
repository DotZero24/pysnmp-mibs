_F='PingState'
_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosPingMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,19))
if mibBuilder.loadTexts:wwpLeosPingMIB.setRevisions(('2012-04-02 00:00','2001-07-03 12:57'))
class PingFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('unknownHost',1),('socketError',2),('bindError',3),('connectError',4),('missingHost',5),('asyncError',6),('nonBlockError',7),('mcastError',8),('ttlError',9),('mcastTtlError',10),('outputError',11),('unreachableError',12),('isAlive',13),('txRx',14),('commandCompleted',15),('noStatus',16),('sendRecvMismatch',17)))
class PingState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('pinging',2),('pingComplete',3),('failed',4)))
_WwpLeosPingMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosPingMIBObjects=_WwpLeosPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,19,1))
class _WwpLeosPingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpLeosPingDelay_Type.__name__=_D
_WwpLeosPingDelay_Object=MibScalar
wwpLeosPingDelay=_WwpLeosPingDelay_Object((1,3,6,1,4,1,6141,2,60,19,1,1),_WwpLeosPingDelay_Type())
wwpLeosPingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingDelay.setStatus(_A)
class _WwpLeosPingPacketSize_Type(Integer32):defaultValue=56;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1464))
_WwpLeosPingPacketSize_Type.__name__=_D
_WwpLeosPingPacketSize_Object=MibScalar
wwpLeosPingPacketSize=_WwpLeosPingPacketSize_Object((1,3,6,1,4,1,6141,2,60,19,1,2),_WwpLeosPingPacketSize_Type())
wwpLeosPingPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingPacketSize.setStatus(_A)
_WwpLeosPingActivate_Type=TruthValue
_WwpLeosPingActivate_Object=MibScalar
wwpLeosPingActivate=_WwpLeosPingActivate_Object((1,3,6,1,4,1,6141,2,60,19,1,3),_WwpLeosPingActivate_Type())
wwpLeosPingActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingActivate.setStatus(_A)
_WwpLeosPingAddrType_Type=AddressFamilyNumbers
_WwpLeosPingAddrType_Object=MibScalar
wwpLeosPingAddrType=_WwpLeosPingAddrType_Object((1,3,6,1,4,1,6141,2,60,19,1,4),_WwpLeosPingAddrType_Type())
wwpLeosPingAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingAddrType.setStatus(_A)
_WwpLeosPingAddr_Type=DisplayString
_WwpLeosPingAddr_Object=MibScalar
wwpLeosPingAddr=_WwpLeosPingAddr_Object((1,3,6,1,4,1,6141,2,60,19,1,5),_WwpLeosPingAddr_Type())
wwpLeosPingAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingAddr.setStatus(_A)
class _WwpLeosPingPacketCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpLeosPingPacketCount_Type.__name__=_D
_WwpLeosPingPacketCount_Object=MibScalar
wwpLeosPingPacketCount=_WwpLeosPingPacketCount_Object((1,3,6,1,4,1,6141,2,60,19,1,6),_WwpLeosPingPacketCount_Type())
wwpLeosPingPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingPacketCount.setStatus(_A)
class _WwpLeosPingPacketTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpLeosPingPacketTimeout_Type.__name__=_D
_WwpLeosPingPacketTimeout_Object=MibScalar
wwpLeosPingPacketTimeout=_WwpLeosPingPacketTimeout_Object((1,3,6,1,4,1,6141,2,60,19,1,7),_WwpLeosPingPacketTimeout_Type())
wwpLeosPingPacketTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingPacketTimeout.setStatus(_A)
_WwpLeosPingSentPackets_Type=Counter32
_WwpLeosPingSentPackets_Object=MibScalar
wwpLeosPingSentPackets=_WwpLeosPingSentPackets_Object((1,3,6,1,4,1,6141,2,60,19,1,8),_WwpLeosPingSentPackets_Type())
wwpLeosPingSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingSentPackets.setStatus(_A)
_WwpLeosPingReceivedPackets_Type=Counter32
_WwpLeosPingReceivedPackets_Object=MibScalar
wwpLeosPingReceivedPackets=_WwpLeosPingReceivedPackets_Object((1,3,6,1,4,1,6141,2,60,19,1,9),_WwpLeosPingReceivedPackets_Type())
wwpLeosPingReceivedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingReceivedPackets.setStatus(_A)
_WwpLeosPingFailCause_Type=PingFailCause
_WwpLeosPingFailCause_Object=MibScalar
wwpLeosPingFailCause=_WwpLeosPingFailCause_Object((1,3,6,1,4,1,6141,2,60,19,1,10),_WwpLeosPingFailCause_Type())
wwpLeosPingFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingFailCause.setStatus(_A)
class _WwpLeosPingState_Type(PingState):defaultValue=1
_WwpLeosPingState_Type.__name__=_F
_WwpLeosPingState_Object=MibScalar
wwpLeosPingState=_WwpLeosPingState_Object((1,3,6,1,4,1,6141,2,60,19,1,11),_WwpLeosPingState_Type())
wwpLeosPingState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingState.setStatus(_A)
class _WwpLeosPingUntilStopped_Type(TruthValue):defaultValue=2
_WwpLeosPingUntilStopped_Type.__name__=_E
_WwpLeosPingUntilStopped_Object=MibScalar
wwpLeosPingUntilStopped=_WwpLeosPingUntilStopped_Object((1,3,6,1,4,1,6141,2,60,19,1,12),_WwpLeosPingUntilStopped_Type())
wwpLeosPingUntilStopped.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPingUntilStopped.setStatus(_A)
_WwpLeosPingInetAddrType_Type=InetAddressType
_WwpLeosPingInetAddrType_Object=MibScalar
wwpLeosPingInetAddrType=_WwpLeosPingInetAddrType_Object((1,3,6,1,4,1,6141,2,60,19,1,13),_WwpLeosPingInetAddrType_Type())
wwpLeosPingInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosPingInetAddrType.setStatus(_A)
mibBuilder.exportSymbols('WWP-LEOS-PING-MIB',**{'PingFailCause':PingFailCause,_F:PingState,'wwpLeosPingMIB':wwpLeosPingMIB,'wwpLeosPingMIBObjects':wwpLeosPingMIBObjects,'wwpLeosPingDelay':wwpLeosPingDelay,'wwpLeosPingPacketSize':wwpLeosPingPacketSize,'wwpLeosPingActivate':wwpLeosPingActivate,'wwpLeosPingAddrType':wwpLeosPingAddrType,'wwpLeosPingAddr':wwpLeosPingAddr,'wwpLeosPingPacketCount':wwpLeosPingPacketCount,'wwpLeosPingPacketTimeout':wwpLeosPingPacketTimeout,'wwpLeosPingSentPackets':wwpLeosPingSentPackets,'wwpLeosPingReceivedPackets':wwpLeosPingReceivedPackets,'wwpLeosPingFailCause':wwpLeosPingFailCause,'wwpLeosPingState':wwpLeosPingState,'wwpLeosPingUntilStopped':wwpLeosPingUntilStopped,'wwpLeosPingInetAddrType':wwpLeosPingInetAddrType})