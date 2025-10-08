#
# PySNMP MIB module ARICENT-DSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aricent/ARICENT-DSMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsdsmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 3, 4))
fsdsmon.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsdsmon.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsdsmon.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsDsmonTrace = MibScalar((1, 3, 6, 1, 4, 1, 29601, 3, 4, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDsmonTrace.setStatus('current')
fsDsmonAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 29601, 3, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDsmonAdminStatus.setStatus('current')
mibBuilder.exportSymbols("ARICENT-DSMON-MIB", fsdsmon=fsdsmon, PYSNMP_MODULE_ID=fsdsmon, fsDsmonTrace=fsDsmonTrace, fsDsmonAdminStatus=fsDsmonAdminStatus)
