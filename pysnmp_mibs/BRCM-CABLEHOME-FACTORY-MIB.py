#
# PySNMP MIB module BRCM-CABLEHOME-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEHOME-FACTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cableHomeFactory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3))
cableHomeFactory.setRevisions(('2007-02-05 00:00', '2004-04-27 00:00', '2004-03-24 00:00', '2002-08-23 00:00',))
if mibBuilder.loadTexts: cableHomeFactory.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: cableHomeFactory.setOrganization('Broadcom Corporation')
chFactoryBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 1))
chFactorySecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2))
chSecPsCert = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSecPsCert.setStatus('current')
chSecPsPrivateKey = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSecPsPrivateKey.setStatus('current')
chSecManCaCert = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSecManCaCert.setStatus('current')
chSecSvcProviderRootCaCert = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSecSvcProviderRootCaCert.setStatus('current')
chSpsClabCvcRootCaCert = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSpsClabCvcRootCaCert.setStatus('current')
chSpsClabCvcCaCert = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chSpsClabCvcCaCert.setStatus('current')
mibBuilder.exportSymbols("BRCM-CABLEHOME-FACTORY-MIB", chSpsClabCvcRootCaCert=chSpsClabCvcRootCaCert, chFactorySecurity=chFactorySecurity, PYSNMP_MODULE_ID=cableHomeFactory, chFactoryBase=chFactoryBase, cableHomeFactory=cableHomeFactory, chSecPsPrivateKey=chSecPsPrivateKey, chSecPsCert=chSecPsCert, chSpsClabCvcCaCert=chSpsClabCvcCaCert, chSecSvcProviderRootCaCert=chSecSvcProviderRootCaCert, chSecManCaCert=chSecManCaCert)
