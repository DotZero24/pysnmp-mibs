#
# PySNMP MIB module TPLINK-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-TELNET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkTelnet = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 52))
tplinkTelnet.setRevisions(('2016-02-26 11:10',))
if mibBuilder.loadTexts: tplinkTelnet.setLastUpdated('201602261110Z')
if mibBuilder.loadTexts: tplinkTelnet.setOrganization('TPLINK')
tplinkTelnetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1))
tplinkTelnetMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 2))
telnetConfig = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetConfig.setStatus('current')
telnetPort = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetPort.setStatus('current')
mibBuilder.exportSymbols("TPLINK-TELNET-MIB", tplinkTelnetMIBNotifications=tplinkTelnetMIBNotifications, tplinkTelnetMIBObjects=tplinkTelnetMIBObjects, PYSNMP_MODULE_ID=tplinkTelnet, telnetPort=telnetPort, tplinkTelnet=tplinkTelnet, telnetConfig=telnetConfig)
