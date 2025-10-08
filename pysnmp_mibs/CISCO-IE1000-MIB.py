#
# PySNMP MIB module CISCO-IE1000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IE1000-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIE1000MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832))
ciscoIE1000MIB.setRevisions(('2016-05-18 00:00',))
if mibBuilder.loadTexts: ciscoIE1000MIB.setLastUpdated('201605180000Z')
if mibBuilder.loadTexts: ciscoIE1000MIB.setOrganization('Cisco Systems, Inc')
cie1000SwitchMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1))
if mibBuilder.loadTexts: cie1000SwitchMgmt.setStatus('current')
mibBuilder.exportSymbols("CISCO-IE1000-MIB", cie1000SwitchMgmt=cie1000SwitchMgmt, PYSNMP_MODULE_ID=ciscoIE1000MIB, ciscoIE1000MIB=ciscoIE1000MIB)
