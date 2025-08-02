_F='PingState'
_E='TruthValue'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpPingMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,21))
if mibBuilder.loadTexts:wwpPingMIB.setRevisions(('2001-07-03 12:57',))
class PingFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('unknownHost',1),('socketError',2),('bindError',3),('connectError',4),('missingHost',5),('asyncError',6),('nonBlockError',7),('mcastError',8),('ttlError',9),('mcastTtlError',10),('outputError',11),('unreachableError',12),('isAlive',13),('txRx',14),('commandCompleted',15),('noStatus',16),('sendRecvMismatch',17)))
class PingState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('pinging',2),('pingComplete',3),('failed',4)))
_WwpPingMIBObjects_ObjectIdentity=ObjectIdentity
wwpPingMIBObjects=_WwpPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,21,1))
class _WwpPingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpPingDelay_Type.__name__=_C
_WwpPingDelay_Object=MibScalar
wwpPingDelay=_WwpPingDelay_Object((1,3,6,1,4,1,6141,2,21,1,1),_WwpPingDelay_Type())
wwpPingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingDelay.setStatus(_A)
class _WwpPingPacketSize_Type(Integer32):defaultValue=56;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1464))
_WwpPingPacketSize_Type.__name__=_C
_WwpPingPacketSize_Object=MibScalar
wwpPingPacketSize=_WwpPingPacketSize_Object((1,3,6,1,4,1,6141,2,21,1,2),_WwpPingPacketSize_Type())
wwpPingPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingPacketSize.setStatus(_A)
_WwpPingActivate_Type=TruthValue
_WwpPingActivate_Object=MibScalar
wwpPingActivate=_WwpPingActivate_Object((1,3,6,1,4,1,6141,2,21,1,3),_WwpPingActivate_Type())
wwpPingActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingActivate.setStatus(_A)
_WwpPingAddress_Type=IpAddress
_WwpPingAddress_Object=MibScalar
wwpPingAddress=_WwpPingAddress_Object((1,3,6,1,4,1,6141,2,21,1,4),_WwpPingAddress_Type())
wwpPingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingAddress.setStatus(_A)
class _WwpPingPacketCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpPingPacketCount_Type.__name__=_C
_WwpPingPacketCount_Object=MibScalar
wwpPingPacketCount=_WwpPingPacketCount_Object((1,3,6,1,4,1,6141,2,21,1,5),_WwpPingPacketCount_Type())
wwpPingPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingPacketCount.setStatus(_A)
class _WwpPingPacketTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_WwpPingPacketTimeout_Type.__name__=_C
_WwpPingPacketTimeout_Object=MibScalar
wwpPingPacketTimeout=_WwpPingPacketTimeout_Object((1,3,6,1,4,1,6141,2,21,1,6),_WwpPingPacketTimeout_Type())
wwpPingPacketTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingPacketTimeout.setStatus(_A)
_WwpPingSentPackets_Type=Counter32
_WwpPingSentPackets_Object=MibScalar
wwpPingSentPackets=_WwpPingSentPackets_Object((1,3,6,1,4,1,6141,2,21,1,8),_WwpPingSentPackets_Type())
wwpPingSentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPingSentPackets.setStatus(_A)
_WwpPingReceivedPackets_Type=Counter32
_WwpPingReceivedPackets_Object=MibScalar
wwpPingReceivedPackets=_WwpPingReceivedPackets_Object((1,3,6,1,4,1,6141,2,21,1,9),_WwpPingReceivedPackets_Type())
wwpPingReceivedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPingReceivedPackets.setStatus(_A)
_WwpPingFailCause_Type=PingFailCause
_WwpPingFailCause_Object=MibScalar
wwpPingFailCause=_WwpPingFailCause_Object((1,3,6,1,4,1,6141,2,21,1,13),_WwpPingFailCause_Type())
wwpPingFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPingFailCause.setStatus(_A)
class _WwpPingState_Type(PingState):defaultValue=1
_WwpPingState_Type.__name__=_F
_WwpPingState_Object=MibScalar
wwpPingState=_WwpPingState_Object((1,3,6,1,4,1,6141,2,21,1,15),_WwpPingState_Type())
wwpPingState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPingState.setStatus(_A)
class _WwpPingUntilStopped_Type(TruthValue):defaultValue=2
_WwpPingUntilStopped_Type.__name__=_E
_WwpPingUntilStopped_Object=MibScalar
wwpPingUntilStopped=_WwpPingUntilStopped_Object((1,3,6,1,4,1,6141,2,21,1,16),_WwpPingUntilStopped_Type())
wwpPingUntilStopped.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPingUntilStopped.setStatus(_A)
mibBuilder.exportSymbols('WWP-PING-MIB',**{'PingFailCause':PingFailCause,_F:PingState,'wwpPingMIB':wwpPingMIB,'wwpPingMIBObjects':wwpPingMIBObjects,'wwpPingDelay':wwpPingDelay,'wwpPingPacketSize':wwpPingPacketSize,'wwpPingActivate':wwpPingActivate,'wwpPingAddress':wwpPingAddress,'wwpPingPacketCount':wwpPingPacketCount,'wwpPingPacketTimeout':wwpPingPacketTimeout,'wwpPingSentPackets':wwpPingSentPackets,'wwpPingReceivedPackets':wwpPingReceivedPackets,'wwpPingFailCause':wwpPingFailCause,'wwpPingState':wwpPingState,'wwpPingUntilStopped':wwpPingUntilStopped})