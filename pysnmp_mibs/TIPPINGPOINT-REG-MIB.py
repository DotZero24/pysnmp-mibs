#
# PySNMP MIB module TIPPINGPOINT-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TIPPINGPOINT-REG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TIPPINGPOINT-REG-MIB", tpt_products=tpt_products, tpt_reqs=tpt_reqs, tpt_expr=tpt_expr, PYSNMP_MODULE_ID=tippingpoint, tpt_caps=tpt_caps, tpt_generic=tpt_generic, tippingpoint=tippingpoint, tpt_reg=tpt_reg)
