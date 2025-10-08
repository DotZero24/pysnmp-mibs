#
# PySNMP MIB module ARICENT-IPV6-MLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aricent/ARICENT-IPV6-MLD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
futuremld = ModuleIdentity((1, 3, 6, 1, 4, 1, 2076, 70))
futuremld.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: futuremld.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: futuremld.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsmldScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 70, 1))
fsmldNoOfCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldNoOfCacheEntries.setStatus('deprecated')
fsmldNoOfRoutingProtocols = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldNoOfRoutingProtocols.setStatus('deprecated')
fsmldTraceDebug = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldTraceDebug.setStatus('current')
fsmldDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldDebugLevel.setStatus('current')
fsmldMode = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mldrouter", 1), ("mldhost", 2), ("mldrouterhost", 3))).clone('mldrouter')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldMode.setStatus('current')
fsmldProtocolUpDown = MibScalar((1, 3, 6, 1, 4, 1, 2076, 70, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mldinit", 1), ("mldshutdown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsmldProtocolUpDown.setStatus('current')
mibBuilder.exportSymbols("ARICENT-IPV6-MLD-MIB", fsmldScalars=fsmldScalars, PYSNMP_MODULE_ID=futuremld, fsmldMode=fsmldMode, futuremld=futuremld, fsmldProtocolUpDown=fsmldProtocolUpDown, fsmldNoOfCacheEntries=fsmldNoOfCacheEntries, fsmldDebugLevel=fsmldDebugLevel, fsmldTraceDebug=fsmldTraceDebug, fsmldNoOfRoutingProtocols=fsmldNoOfRoutingProtocols)
