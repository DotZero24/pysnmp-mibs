#
# PySNMP MIB module EAP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/EAP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eap, = mibBuilder.importSymbols("TPLINK-MIB", "eap")
clientStatis = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1))
clientStatis.setRevisions(('2016-10-17 00:00',))
if mibBuilder.loadTexts: clientStatis.setLastUpdated('201610170000z')
if mibBuilder.loadTexts: clientStatis.setOrganization('TPLINK')
clientCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clientCount.setStatus('current')
clientTable = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 2))
mibBuilder.exportSymbols("EAP-CLIENT-MIB", clientStatis=clientStatis, clientTable=clientTable, PYSNMP_MODULE_ID=clientStatis, clientCount=clientCount)
