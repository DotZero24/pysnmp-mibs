#
# PySNMP MIB module DEVSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVSERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniDevServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 5))
if mibBuilder.loadTexts: aniDevServer.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevServer.setOrganization('Aperto Networks')
aniDevTftpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevTftpServer.setStatus('current')
aniDevDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDhcpServer.setStatus('current')
aniDevDhcpLeaseExpiration = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDhcpLeaseExpiration.setStatus('current')
aniDevSuDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSuDhcpServer.setStatus('current')
aniDevTimeServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevTimeServer.setStatus('current')
aniDevSyslogServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSyslogServer.setStatus('current')
aniDevSmtpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevSmtpServer.setStatus('current')
mibBuilder.exportSymbols("DEVSERVER-MIB", aniDevDhcpServer=aniDevDhcpServer, aniDevTftpServer=aniDevTftpServer, PYSNMP_MODULE_ID=aniDevServer, aniDevSuDhcpServer=aniDevSuDhcpServer, aniDevServer=aniDevServer, aniDevSyslogServer=aniDevSyslogServer, aniDevSmtpServer=aniDevSmtpServer, aniDevDhcpLeaseExpiration=aniDevDhcpLeaseExpiration, aniDevTimeServer=aniDevTimeServer)
