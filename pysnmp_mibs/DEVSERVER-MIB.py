#
# PySNMP MIB module DEVSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVSERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DEVSERVER-MIB", PYSNMP_MODULE_ID=aniDevServer, aniDevSyslogServer=aniDevSyslogServer, aniDevSuDhcpServer=aniDevSuDhcpServer, aniDevTftpServer=aniDevTftpServer, aniDevTimeServer=aniDevTimeServer, aniDevDhcpLeaseExpiration=aniDevDhcpLeaseExpiration, aniDevSmtpServer=aniDevSmtpServer, aniDevServer=aniDevServer, aniDevDhcpServer=aniDevDhcpServer)
