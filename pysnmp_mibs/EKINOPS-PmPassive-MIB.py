#
# PySNMP MIB module EKINOPS-PmPassive-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ekinops/EKINOPS-PmPassive-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:46:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ekinops, = mibBuilder.importSymbols("EKINOPS-MIB", "ekinops")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
modulePmPassive = ModuleIdentity((1, 3, 6, 1, 4, 1, 20044, 20))
modulePmPassive.setRevisions(('2007-01-05 00:00',))
if mibBuilder.loadTexts: modulePmPassive.setLastUpdated('200701050000Z')
if mibBuilder.loadTexts: modulePmPassive.setOrganization('Ekinops')
pmpassiveri = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 20, 1))
pmpassiveRinvHwPlatform = MibScalar((1, 3, 6, 1, 4, 1, 20044, 20, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmpassiveRinvHwPlatform.setStatus('current')
mibBuilder.exportSymbols("EKINOPS-PmPassive-MIB", modulePmPassive=modulePmPassive, PYSNMP_MODULE_ID=modulePmPassive, pmpassiveri=pmpassiveri, pmpassiveRinvHwPlatform=pmpassiveRinvHwPlatform)
