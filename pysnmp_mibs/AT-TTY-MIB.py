#
# PySNMP MIB module AT-TTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/AT-TTY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AT-TTY-MIB", loginFailureUser=loginFailureUser, loginFailureIPAddress=loginFailureIPAddress, loginFailureTrap=loginFailureTrap, PYSNMP_MODULE_ID=tty, ttyTraps=ttyTraps, tty=tty, loginFailureAttempts=loginFailureAttempts)
