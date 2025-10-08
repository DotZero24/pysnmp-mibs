#
# PySNMP MIB module TPT-VSA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-VSA-REG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_reg, tpt_products = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg", "tpt-products")
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
mibBuilder.exportSymbols("TPT-VSA-REG-MIB", tpt_model_V2000F=tpt_model_V2000F, tpt_model_V1000F=tpt_model_V1000F, tpt_model_V10F=tpt_model_V10F, tpt_model_V5000F=tpt_model_V5000F, PYSNMP_MODULE_ID=tpt_vsaMIBs, tpt_vsa_family=tpt_vsa_family, tpt_vsaMIBs=tpt_vsaMIBs)
