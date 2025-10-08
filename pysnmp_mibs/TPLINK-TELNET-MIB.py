#
# PySNMP MIB module TPLINK-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-TELNET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TPLINK-TELNET-MIB", PYSNMP_MODULE_ID=tplinkTelnet, tplinkTelnet=tplinkTelnet, tplinkTelnetMIBObjects=tplinkTelnetMIBObjects, telnetConfig=telnetConfig, telnetPort=telnetPort, tplinkTelnetMIBNotifications=tplinkTelnetMIBNotifications)
