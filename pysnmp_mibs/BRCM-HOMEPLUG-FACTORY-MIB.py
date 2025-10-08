#
# PySNMP MIB module BRCM-HOMEPLUG-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-HOMEPLUG-FACTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString")
homeplugFactory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9))
homeplugFactory.setRevisions(('2004-12-21 00:00',))
if mibBuilder.loadTexts: homeplugFactory.setLastUpdated('200412210000Z')
if mibBuilder.loadTexts: homeplugFactory.setOrganization('Broadcom Corporation')
homeplugFactMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: homeplugFactMacAddress.setStatus('current')
homeplugFactDEKPassword = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: homeplugFactDEKPassword.setStatus('current')
homeplugFactNEKPassword = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: homeplugFactNEKPassword.setStatus('current')
mibBuilder.exportSymbols("BRCM-HOMEPLUG-FACTORY-MIB", PYSNMP_MODULE_ID=homeplugFactory, homeplugFactNEKPassword=homeplugFactNEKPassword, homeplugFactDEKPassword=homeplugFactDEKPassword, homeplugFactMacAddress=homeplugFactMacAddress, homeplugFactory=homeplugFactory)
