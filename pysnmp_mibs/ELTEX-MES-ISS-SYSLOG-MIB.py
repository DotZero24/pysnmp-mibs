#
# PySNMP MIB module ELTEX-MES-ISS-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SYSLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-SYSLOG-MIB", eltMesIssSyslogNotifications=eltMesIssSyslogNotifications, eltMesIssSyslogGlobals=eltMesIssSyslogGlobals, eltMesIssSyslogVersionString=eltMesIssSyslogVersionString, eltMesIssSyslogMIB=eltMesIssSyslogMIB, eltMesIssSyslogHostnameMode=eltMesIssSyslogHostnameMode, eltMesIssSyslogObjects=eltMesIssSyslogObjects, eltMesIssSyslogVersionMode=eltMesIssSyslogVersionMode, eltMesIssSyslogHostnameString=eltMesIssSyslogHostnameString, eltMesIssSyslogTimestampMode=eltMesIssSyslogTimestampMode, PYSNMP_MODULE_ID=eltMesIssSyslogMIB)
