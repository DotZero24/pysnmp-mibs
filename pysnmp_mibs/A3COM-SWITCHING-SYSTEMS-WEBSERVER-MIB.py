#
# PySNMP MIB module A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB", switchingSystemsMibs=switchingSystemsMibs, a3ComWebConfigHelpServer=a3ComWebConfigHelpServer, a3Com=a3Com, a3ComWebConfigEmailServerAddress=a3ComWebConfigEmailServerAddress, a3ComWebConfigEmailAddresses=a3ComWebConfigEmailAddresses, a3ComWebConfig=a3ComWebConfig, a3ComSwitchingSystemsMib=a3ComSwitchingSystemsMib)
