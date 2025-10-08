#
# PySNMP MIB module HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpnicfARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146))
hpnicfARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setOrganization('')
hpnicfARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1))
hpnicfARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1))
hpnicfARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionEnable.setStatus('current')
hpnicfARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionLimit.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB", hpnicfARPSourceSuppressionGlobal=hpnicfARPSourceSuppressionGlobal, PYSNMP_MODULE_ID=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionObjects=hpnicfARPSourceSuppressionObjects, hpnicfARPSourceSuppression=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionLimit=hpnicfARPSourceSuppressionLimit, hpnicfARPSourceSuppressionEnable=hpnicfARPSourceSuppressionEnable)
