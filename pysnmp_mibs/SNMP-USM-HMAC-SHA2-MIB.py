_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snmpAuthProtocols,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','snmpAuthProtocols')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpUsmHmacSha2MIB=ModuleIdentity((1,3,6,1,2,1,235))
if mibBuilder.loadTexts:snmpUsmHmacSha2MIB.setRevisions(('2016-04-18 00:00','2015-10-14 00:00'))
_UsmHMAC128SHA224AuthProtocol_ObjectIdentity=ObjectIdentity
usmHMAC128SHA224AuthProtocol=_UsmHMAC128SHA224AuthProtocol_ObjectIdentity((1,3,6,1,6,3,10,1,1,4))
if mibBuilder.loadTexts:usmHMAC128SHA224AuthProtocol.setStatus(_A)
_UsmHMAC192SHA256AuthProtocol_ObjectIdentity=ObjectIdentity
usmHMAC192SHA256AuthProtocol=_UsmHMAC192SHA256AuthProtocol_ObjectIdentity((1,3,6,1,6,3,10,1,1,5))
if mibBuilder.loadTexts:usmHMAC192SHA256AuthProtocol.setStatus(_A)
_UsmHMAC256SHA384AuthProtocol_ObjectIdentity=ObjectIdentity
usmHMAC256SHA384AuthProtocol=_UsmHMAC256SHA384AuthProtocol_ObjectIdentity((1,3,6,1,6,3,10,1,1,6))
if mibBuilder.loadTexts:usmHMAC256SHA384AuthProtocol.setStatus(_A)
_UsmHMAC384SHA512AuthProtocol_ObjectIdentity=ObjectIdentity
usmHMAC384SHA512AuthProtocol=_UsmHMAC384SHA512AuthProtocol_ObjectIdentity((1,3,6,1,6,3,10,1,1,7))
if mibBuilder.loadTexts:usmHMAC384SHA512AuthProtocol.setStatus(_A)
mibBuilder.exportSymbols('SNMP-USM-HMAC-SHA2-MIB',**{'snmpUsmHmacSha2MIB':snmpUsmHmacSha2MIB,'usmHMAC128SHA224AuthProtocol':usmHMAC128SHA224AuthProtocol,'usmHMAC192SHA256AuthProtocol':usmHMAC192SHA256AuthProtocol,'usmHMAC256SHA384AuthProtocol':usmHMAC256SHA384AuthProtocol,'usmHMAC384SHA512AuthProtocol':usmHMAC384SHA512AuthProtocol})