#
# PySNMP MIB module CRESTRON-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/crestron/CRESTRON-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
crestron, = mibBuilder.importSymbols("CRESTRON-ROOT-MIB", "crestron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
crestronProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 3212, 9))
if mibBuilder.loadTexts: crestronProducts.setLastUpdated('200505181925Z')
if mibBuilder.loadTexts: crestronProducts.setOrganization('Organization.')
crestronProductPRO2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 1))
if mibBuilder.loadTexts: crestronProductPRO2.setStatus('current')
crestronProductQMRMC = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 2))
if mibBuilder.loadTexts: crestronProductQMRMC.setStatus('current')
crestronProductQMRMCRX = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 3))
if mibBuilder.loadTexts: crestronProductQMRMCRX.setStatus('current')
crestronProductDVP4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 4))
if mibBuilder.loadTexts: crestronProductDVP4.setStatus('current')
crestronProductMP2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 5))
if mibBuilder.loadTexts: crestronProductMP2.setStatus('current')
crestronProductPollAcc = ObjectIdentity((1, 3, 6, 1, 4, 1, 3212, 9, 6))
if mibBuilder.loadTexts: crestronProductPollAcc.setStatus('current')
mibBuilder.exportSymbols("CRESTRON-PRODUCTS-MIB", crestronProductQMRMC=crestronProductQMRMC, crestronProductPRO2=crestronProductPRO2, crestronProductMP2=crestronProductMP2, crestronProductDVP4=crestronProductDVP4, crestronProducts=crestronProducts, crestronProductPollAcc=crestronProductPollAcc, PYSNMP_MODULE_ID=crestronProducts, crestronProductQMRMCRX=crestronProductQMRMCRX)
