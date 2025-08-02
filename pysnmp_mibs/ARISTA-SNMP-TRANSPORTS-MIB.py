_F='aristaAuthFailTrapObjectsGroup'
_E='aristaAuthFailTrapSrcTAddress'
_D='aristaAuthFailTrapTDomain'
_C='read-only'
_B='ARISTA-SNMP-TRANSPORTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TAddress,TDomain,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TAddress','TDomain','TextualConvention')
aristaSnmpTransportMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,10))
if mibBuilder.loadTexts:aristaSnmpTransportMIB.setRevisions(('2014-08-15 00:00','2012-01-09 13:00','2012-01-05 18:30'))
class TransportAddressIPv4NS(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d.1d:2d@*1t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,255))
class TransportAddressIPv6NS(TextualConvention,OctetString):status=_A;displayHint='0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(19,255))
_AristaUDPNSDomain_ObjectIdentity=ObjectIdentity
aristaUDPNSDomain=_AristaUDPNSDomain_ObjectIdentity((1,3,6,1,4,1,30065,3,10,1))
if mibBuilder.loadTexts:aristaUDPNSDomain.setStatus(_A)
_AristaTCPNSDomain_ObjectIdentity=ObjectIdentity
aristaTCPNSDomain=_AristaTCPNSDomain_ObjectIdentity((1,3,6,1,4,1,30065,3,10,2))
if mibBuilder.loadTexts:aristaTCPNSDomain.setStatus(_A)
_AristaUDPNS6Domain_ObjectIdentity=ObjectIdentity
aristaUDPNS6Domain=_AristaUDPNS6Domain_ObjectIdentity((1,3,6,1,4,1,30065,3,10,3))
if mibBuilder.loadTexts:aristaUDPNS6Domain.setStatus(_A)
_AristaTCPNS6Domain_ObjectIdentity=ObjectIdentity
aristaTCPNS6Domain=_AristaTCPNS6Domain_ObjectIdentity((1,3,6,1,4,1,30065,3,10,4))
if mibBuilder.loadTexts:aristaTCPNS6Domain.setStatus(_A)
_AristaAuthFailTrapObjects_ObjectIdentity=ObjectIdentity
aristaAuthFailTrapObjects=_AristaAuthFailTrapObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,10,5))
_AristaAuthFailTrapTDomain_Type=TDomain
_AristaAuthFailTrapTDomain_Object=MibScalar
aristaAuthFailTrapTDomain=_AristaAuthFailTrapTDomain_Object((1,3,6,1,4,1,30065,3,10,5,1),_AristaAuthFailTrapTDomain_Type())
aristaAuthFailTrapTDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAuthFailTrapTDomain.setStatus(_A)
_AristaAuthFailTrapSrcTAddress_Type=TAddress
_AristaAuthFailTrapSrcTAddress_Object=MibScalar
aristaAuthFailTrapSrcTAddress=_AristaAuthFailTrapSrcTAddress_Object((1,3,6,1,4,1,30065,3,10,5,2),_AristaAuthFailTrapSrcTAddress_Type())
aristaAuthFailTrapSrcTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAuthFailTrapSrcTAddress.setStatus(_A)
_AristaTransportConformance_ObjectIdentity=ObjectIdentity
aristaTransportConformance=_AristaTransportConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,10,6))
_AristaAuthFailTrapGroups_ObjectIdentity=ObjectIdentity
aristaAuthFailTrapGroups=_AristaAuthFailTrapGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,10,6,1))
_AristaAuthFailCompliances_ObjectIdentity=ObjectIdentity
aristaAuthFailCompliances=_AristaAuthFailCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,10,6,2))
aristaAuthFailTrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,10,6,1,1))
aristaAuthFailTrapObjectsGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:aristaAuthFailTrapObjectsGroup.setStatus(_A)
aristaAuthFailCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,10,6,2,1))
aristaAuthFailCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:aristaAuthFailCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TransportAddressIPv4NS':TransportAddressIPv4NS,'TransportAddressIPv6NS':TransportAddressIPv6NS,'aristaSnmpTransportMIB':aristaSnmpTransportMIB,'aristaUDPNSDomain':aristaUDPNSDomain,'aristaTCPNSDomain':aristaTCPNSDomain,'aristaUDPNS6Domain':aristaUDPNS6Domain,'aristaTCPNS6Domain':aristaTCPNS6Domain,'aristaAuthFailTrapObjects':aristaAuthFailTrapObjects,_D:aristaAuthFailTrapTDomain,_E:aristaAuthFailTrapSrcTAddress,'aristaTransportConformance':aristaTransportConformance,'aristaAuthFailTrapGroups':aristaAuthFailTrapGroups,_F:aristaAuthFailTrapObjectsGroup,'aristaAuthFailCompliances':aristaAuthFailCompliances,'aristaAuthFailCompliance':aristaAuthFailCompliance})