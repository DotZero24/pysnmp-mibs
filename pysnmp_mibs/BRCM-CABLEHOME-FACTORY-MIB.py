#
# PySNMP MIB module BRCM-CABLEHOME-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEHOME-FACTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-CABLEHOME-FACTORY-MIB", chFactoryBase=chFactoryBase, chFactorySecurity=chFactorySecurity, chSpsClabCvcCaCert=chSpsClabCvcCaCert, chSecManCaCert=chSecManCaCert, PYSNMP_MODULE_ID=cableHomeFactory, chSecPsCert=chSecPsCert, cableHomeFactory=cableHomeFactory, chSecPsPrivateKey=chSecPsPrivateKey, chSpsClabCvcRootCaCert=chSpsClabCvcRootCaCert, chSecSvcProviderRootCaCert=chSecSvcProviderRootCaCert)
