#
# PySNMP MIB module AT-TTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/AT-TTY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tty = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36))
tty.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: tty.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: tty.setOrganization('Allied Telesis, Inc')
ttyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100))
loginFailureUser = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 1), DisplayString())
if mibBuilder.loadTexts: loginFailureUser.setStatus('current')
loginFailureIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 2), IpAddress())
if mibBuilder.loadTexts: loginFailureIPAddress.setStatus('current')
loginFailureAttempts = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 3), Integer32())
if mibBuilder.loadTexts: loginFailureAttempts.setStatus('current')
loginFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 11)).setObjects(("AT-TTY-MIB", "loginFailureUser"), ("AT-TTY-MIB", "loginFailureIPAddress"), ("AT-TTY-MIB", "loginFailureAttempts"))
if mibBuilder.loadTexts: loginFailureTrap.setStatus('current')
mibBuilder.exportSymbols("AT-TTY-MIB", tty=tty, loginFailureUser=loginFailureUser, loginFailureAttempts=loginFailureAttempts, loginFailureIPAddress=loginFailureIPAddress, PYSNMP_MODULE_ID=tty, ttyTraps=ttyTraps, loginFailureTrap=loginFailureTrap)
