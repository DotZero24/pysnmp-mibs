#
# PySNMP MIB module BRCM-HOMEPLUG-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-HOMEPLUG-FACTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("BRCM-HOMEPLUG-FACTORY-MIB", homeplugFactDEKPassword=homeplugFactDEKPassword, homeplugFactory=homeplugFactory, PYSNMP_MODULE_ID=homeplugFactory, homeplugFactMacAddress=homeplugFactMacAddress, homeplugFactNEKPassword=homeplugFactNEKPassword)
