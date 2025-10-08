#
# PySNMP MIB module CISCOSMB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSMB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2010-10-31 00:00',))
if mibBuilder.loadTexts: cisco.setLastUpdated('201010310000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6))
ciscosb = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1))
switch001 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
rndMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
mibBuilder.exportSymbols("CISCOSMB-MIB", cisco=cisco, PYSNMP_MODULE_ID=cisco, rndMib=rndMib, ciscosb=ciscosb, otherEnterprises=otherEnterprises, switch001=switch001)
