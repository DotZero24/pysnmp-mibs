#
# PySNMP MIB module SUPERMICRO-RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-RMON2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsrmon2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 19))
fsrmon2.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsrmon2.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsrmon2.setOrganization('Super Micro Computer Inc.')
fsRmon2Trace = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 19, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsRmon2Trace.setStatus('current')
fsRmon2AdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 19, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsRmon2AdminStatus.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-RMON2-MIB", fsrmon2=fsrmon2, PYSNMP_MODULE_ID=fsrmon2, fsRmon2Trace=fsRmon2Trace, fsRmon2AdminStatus=fsRmon2AdminStatus)
