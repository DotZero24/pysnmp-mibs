if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoModules,=mibBuilder.importSymbols('CISCO-SMI','ciscoModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSnmpUsmOidsMIB=ModuleIdentity((1,3,6,1,4,1,9,12,6))
if mibBuilder.loadTexts:ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))
_CiscoSnmpPrivProtocols_ObjectIdentity=ObjectIdentity
ciscoSnmpPrivProtocols=_CiscoSnmpPrivProtocols_ObjectIdentity((1,3,6,1,4,1,9,12,6,1))
_CusmAESCfb192PrivProtocol_ObjectIdentity=ObjectIdentity
cusmAESCfb192PrivProtocol=_CusmAESCfb192PrivProtocol_ObjectIdentity((1,3,6,1,4,1,9,12,6,1,1))
_CusmAESCfb256PrivProtocol_ObjectIdentity=ObjectIdentity
cusmAESCfb256PrivProtocol=_CusmAESCfb256PrivProtocol_ObjectIdentity((1,3,6,1,4,1,9,12,6,1,2))
_Cusm3DES168PrivProtocol_ObjectIdentity=ObjectIdentity
cusm3DES168PrivProtocol=_Cusm3DES168PrivProtocol_ObjectIdentity((1,3,6,1,4,1,9,12,6,1,3))
mibBuilder.exportSymbols('CISCO-SNMP-USM-OIDS-MIB',**{'ciscoSnmpUsmOidsMIB':ciscoSnmpUsmOidsMIB,'ciscoSnmpPrivProtocols':ciscoSnmpPrivProtocols,'cusmAESCfb192PrivProtocol':cusmAESCfb192PrivProtocol,'cusmAESCfb256PrivProtocol':cusmAESCfb256PrivProtocol,'cusm3DES168PrivProtocol':cusm3DES168PrivProtocol})