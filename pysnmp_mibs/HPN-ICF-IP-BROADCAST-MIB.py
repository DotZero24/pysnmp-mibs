_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfIpBroadcast=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,33))
if mibBuilder.loadTexts:hpnicfIpBroadcast.setRevisions(('2004-12-13 19:36',))
_HpnicfIpBdstScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfIpBdstScalarGroup=_HpnicfIpBdstScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,33,1))
class _HpnicfIpBdstForwardBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('notForwarding',2)))
_HpnicfIpBdstForwardBroadcast_Type.__name__=_A
_HpnicfIpBdstForwardBroadcast_Object=MibScalar
hpnicfIpBdstForwardBroadcast=_HpnicfIpBdstForwardBroadcast_Object((1,3,6,1,4,1,11,2,14,11,15,2,33,1,1),_HpnicfIpBdstForwardBroadcast_Type())
hpnicfIpBdstForwardBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpBdstForwardBroadcast.setStatus(_C)
class _HpnicfIpReceiveBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receive',1),('notReceive',2)))
_HpnicfIpReceiveBroadcast_Type.__name__=_A
_HpnicfIpReceiveBroadcast_Object=MibScalar
hpnicfIpReceiveBroadcast=_HpnicfIpReceiveBroadcast_Object((1,3,6,1,4,1,11,2,14,11,15,2,33,1,2),_HpnicfIpReceiveBroadcast_Type())
hpnicfIpReceiveBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpReceiveBroadcast.setStatus(_C)
_HpnicfIpBdstGroup_ObjectIdentity=ObjectIdentity
hpnicfIpBdstGroup=_HpnicfIpBdstGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,33,2))
_HpnicfIpBdstTrap_ObjectIdentity=ObjectIdentity
hpnicfIpBdstTrap=_HpnicfIpBdstTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,33,3))
_HpnicfIpBdstTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfIpBdstTrapPrex=_HpnicfIpBdstTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,33,3,0))
mibBuilder.exportSymbols('HPN-ICF-IP-BROADCAST-MIB',**{'hpnicfIpBroadcast':hpnicfIpBroadcast,'hpnicfIpBdstScalarGroup':hpnicfIpBdstScalarGroup,'hpnicfIpBdstForwardBroadcast':hpnicfIpBdstForwardBroadcast,'hpnicfIpReceiveBroadcast':hpnicfIpReceiveBroadcast,'hpnicfIpBdstGroup':hpnicfIpBdstGroup,'hpnicfIpBdstTrap':hpnicfIpBdstTrap,'hpnicfIpBdstTrapPrex':hpnicfIpBdstTrapPrex})