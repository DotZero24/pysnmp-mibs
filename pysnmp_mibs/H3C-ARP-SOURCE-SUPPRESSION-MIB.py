#
# PySNMP MIB module H3C-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
h3cARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146))
h3cARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
if mibBuilder.loadTexts: h3cARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: h3cARPSourceSuppression.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1))
h3cARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1))
h3cARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cARPSourceSuppressionEnable.setStatus('current')
h3cARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cARPSourceSuppressionLimit.setStatus('current')
mibBuilder.exportSymbols("H3C-ARP-SOURCE-SUPPRESSION-MIB", h3cARPSourceSuppressionLimit=h3cARPSourceSuppressionLimit, h3cARPSourceSuppressionObjects=h3cARPSourceSuppressionObjects, h3cARPSourceSuppression=h3cARPSourceSuppression, PYSNMP_MODULE_ID=h3cARPSourceSuppression, h3cARPSourceSuppressionEnable=h3cARPSourceSuppressionEnable, h3cARPSourceSuppressionGlobal=h3cARPSourceSuppressionGlobal)
