#
# PySNMP MIB module TIPPINGPOINT-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TIPPINGPOINT-REG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tippingpoint = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734))
tippingpoint.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tippingpoint.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tippingpoint.setOrganization('Trend Micro, Inc.')
tpt_reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1)).setLabel("tpt-reg")
if mibBuilder.loadTexts: tpt_reg.setStatus('current')
tpt_generic = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 2)).setLabel("tpt-generic")
if mibBuilder.loadTexts: tpt_generic.setStatus('current')
tpt_products = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3)).setLabel("tpt-products")
if mibBuilder.loadTexts: tpt_products.setStatus('current')
tpt_caps = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 4)).setLabel("tpt-caps")
if mibBuilder.loadTexts: tpt_caps.setStatus('current')
tpt_reqs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 5)).setLabel("tpt-reqs")
if mibBuilder.loadTexts: tpt_reqs.setStatus('current')
tpt_expr = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 6)).setLabel("tpt-expr")
if mibBuilder.loadTexts: tpt_expr.setStatus('current')
mibBuilder.exportSymbols("TIPPINGPOINT-REG-MIB", tpt_products=tpt_products, tpt_expr=tpt_expr, PYSNMP_MODULE_ID=tippingpoint, tpt_caps=tpt_caps, tpt_reqs=tpt_reqs, tpt_reg=tpt_reg, tpt_generic=tpt_generic, tippingpoint=tippingpoint)
