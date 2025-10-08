#
# PySNMP MIB module SUPERMICRO-IPV6-MLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-IPV6-MLD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
futuremld = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70))
futuremld.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: futuremld.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: futuremld.setOrganization('Super Micro Computer Inc.')
fsmldScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1))
fsmldNoOfCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldNoOfCacheEntries.setStatus('deprecated')
fsmldNoOfRoutingProtocols = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldNoOfRoutingProtocols.setStatus('deprecated')
fsmldTraceDebug = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldTraceDebug.setStatus('current')
fsmldMode = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mldrouter", 1), ("mldhost", 2), ("mldrouterhost", 3))).clone('mldrouter')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldMode.setStatus('current')
fsmldProtocolUpDown = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 70, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mldinit", 1), ("mldshutdown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldProtocolUpDown.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-IPV6-MLD-MIB", PYSNMP_MODULE_ID=futuremld, fsmldTraceDebug=fsmldTraceDebug, fsmldProtocolUpDown=fsmldProtocolUpDown, fsmldScalars=fsmldScalars, fsmldNoOfCacheEntries=fsmldNoOfCacheEntries, futuremld=futuremld, fsmldMode=fsmldMode, fsmldNoOfRoutingProtocols=fsmldNoOfRoutingProtocols)
