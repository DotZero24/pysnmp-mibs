_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cIpBroadcast=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,33))
if mibBuilder.loadTexts:h3cIpBroadcast.setRevisions(('2004-12-13 19:36',))
_H3cIpBdstScalarGroup_ObjectIdentity=ObjectIdentity
h3cIpBdstScalarGroup=_H3cIpBdstScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,33,1))
class _H3cIpBdstForwardBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('notForwarding',2)))
_H3cIpBdstForwardBroadcast_Type.__name__=_A
_H3cIpBdstForwardBroadcast_Object=MibScalar
h3cIpBdstForwardBroadcast=_H3cIpBdstForwardBroadcast_Object((1,3,6,1,4,1,43,45,1,10,2,33,1,1),_H3cIpBdstForwardBroadcast_Type())
h3cIpBdstForwardBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpBdstForwardBroadcast.setStatus(_C)
class _H3cIpReceiveBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receive',1),('notReceive',2)))
_H3cIpReceiveBroadcast_Type.__name__=_A
_H3cIpReceiveBroadcast_Object=MibScalar
h3cIpReceiveBroadcast=_H3cIpReceiveBroadcast_Object((1,3,6,1,4,1,43,45,1,10,2,33,1,2),_H3cIpReceiveBroadcast_Type())
h3cIpReceiveBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpReceiveBroadcast.setStatus(_C)
_H3cIpBdstGroup_ObjectIdentity=ObjectIdentity
h3cIpBdstGroup=_H3cIpBdstGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,33,2))
_H3cIpBdstTrap_ObjectIdentity=ObjectIdentity
h3cIpBdstTrap=_H3cIpBdstTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,33,3))
_H3cIpBdstTrapPrex_ObjectIdentity=ObjectIdentity
h3cIpBdstTrapPrex=_H3cIpBdstTrapPrex_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,33,3,0))
mibBuilder.exportSymbols('A3COM-HUAWEI-IP-BROADCAST-MIB',**{'h3cIpBroadcast':h3cIpBroadcast,'h3cIpBdstScalarGroup':h3cIpBdstScalarGroup,'h3cIpBdstForwardBroadcast':h3cIpBdstForwardBroadcast,'h3cIpReceiveBroadcast':h3cIpReceiveBroadcast,'h3cIpBdstGroup':h3cIpBdstGroup,'h3cIpBdstTrap':h3cIpBdstTrap,'h3cIpBdstTrapPrex':h3cIpBdstTrapPrex})