#
# PySNMP MIB module ARICENT-RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aricent/ARICENT-RMON2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsrmon2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 2, 19))
fsrmon2.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsrmon2.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsrmon2.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsRmon2Trace = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 19, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsRmon2Trace.setStatus('current')
fsRmon2AdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29601, 2, 19, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsRmon2AdminStatus.setStatus('current')
mibBuilder.exportSymbols("ARICENT-RMON2-MIB", fsrmon2=fsrmon2, PYSNMP_MODULE_ID=fsrmon2, fsRmon2AdminStatus=fsRmon2AdminStatus, fsRmon2Trace=fsRmon2Trace)
