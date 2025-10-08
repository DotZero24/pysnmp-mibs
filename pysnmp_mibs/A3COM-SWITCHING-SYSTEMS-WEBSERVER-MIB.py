#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
switchingSystemsMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29))
a3ComSwitchingSystemsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4))
a3ComWebConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 29, 4, 24))
a3ComWebConfigHelpServer = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigHelpServer.setStatus('mandatory')
a3ComWebConfigEmailServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 85))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailServerAddress.setStatus('mandatory')
a3ComWebConfigEmailAddresses = MibScalar((1, 3, 6, 1, 4, 1, 43, 29, 4, 24, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComWebConfigEmailAddresses.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB", a3ComWebConfigEmailServerAddress=a3ComWebConfigEmailServerAddress, a3ComWebConfigEmailAddresses=a3ComWebConfigEmailAddresses, a3ComWebConfigHelpServer=a3ComWebConfigHelpServer, a3ComSwitchingSystemsMib=a3ComSwitchingSystemsMib, switchingSystemsMibs=switchingSystemsMibs, a3ComWebConfig=a3ComWebConfig, a3Com=a3Com)
