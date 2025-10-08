#
# PySNMP MIB module TPT-VSA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-VSA-REG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_products, tpt_reg = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-products", "tpt-reg")
tpt_vsaMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 10)).setLabel("tpt-vsaMIBs")
tpt_vsaMIBs.setRevisions(('2016-05-25 18:54', '2014-11-11 19:37',))
if mibBuilder.loadTexts: tpt_vsaMIBs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_vsaMIBs.setOrganization('Trend Micro, Inc.')
tpt_vsa_family = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-vsa-family")
if mibBuilder.loadTexts: tpt_vsa_family.setStatus('current')
tpt_model_V10F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-V10F")
if mibBuilder.loadTexts: tpt_model_V10F.setStatus('current')
tpt_model_V1000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-V1000F")
if mibBuilder.loadTexts: tpt_model_V1000F.setStatus('current')
tpt_model_V2000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 3)).setLabel("tpt-model-V2000F")
if mibBuilder.loadTexts: tpt_model_V2000F.setStatus('current')
tpt_model_V5000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 4)).setLabel("tpt-model-V5000F")
if mibBuilder.loadTexts: tpt_model_V5000F.setStatus('current')
mibBuilder.exportSymbols("TPT-VSA-REG-MIB", tpt_vsaMIBs=tpt_vsaMIBs, tpt_model_V2000F=tpt_model_V2000F, tpt_model_V5000F=tpt_model_V5000F, tpt_model_V10F=tpt_model_V10F, tpt_model_V1000F=tpt_model_V1000F, tpt_vsa_family=tpt_vsa_family, PYSNMP_MODULE_ID=tpt_vsaMIBs)
