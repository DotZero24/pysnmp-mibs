#
# PySNMP MIB module ELTEX-MES-ISS-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltMesIssSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22))
eltMesIssSyslogMIB.setRevisions(('2020-07-29 00:00',))
if mibBuilder.loadTexts: eltMesIssSyslogMIB.setLastUpdated('202007290000Z')
if mibBuilder.loadTexts: eltMesIssSyslogMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1))
eltMesIssSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 2))
eltMesIssSyslogGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1))
eltMesIssSyslogVersionMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("empty", 1), ("present", 2))).clone('empty')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSyslogVersionMode.setStatus('current')
eltMesIssSyslogVersionString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSyslogVersionString.setStatus('current')
eltMesIssSyslogTimestampMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("legacy", 1), ("rfc5424", 2))).clone('legacy')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSyslogTimestampMode.setStatus('current')
eltMesIssSyslogHostnameMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("empty", 1), ("string", 2), ("hostname", 3), ("ip", 4), ("ipv6", 5))).clone('empty')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSyslogHostnameMode.setStatus('current')
eltMesIssSyslogHostnameString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 22, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSyslogHostnameString.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SYSLOG-MIB", eltMesIssSyslogVersionMode=eltMesIssSyslogVersionMode, eltMesIssSyslogVersionString=eltMesIssSyslogVersionString, eltMesIssSyslogGlobals=eltMesIssSyslogGlobals, eltMesIssSyslogHostnameMode=eltMesIssSyslogHostnameMode, eltMesIssSyslogObjects=eltMesIssSyslogObjects, PYSNMP_MODULE_ID=eltMesIssSyslogMIB, eltMesIssSyslogHostnameString=eltMesIssSyslogHostnameString, eltMesIssSyslogTimestampMode=eltMesIssSyslogTimestampMode, eltMesIssSyslogNotifications=eltMesIssSyslogNotifications, eltMesIssSyslogMIB=eltMesIssSyslogMIB)
