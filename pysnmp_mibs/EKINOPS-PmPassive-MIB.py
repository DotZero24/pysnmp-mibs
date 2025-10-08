#
# PySNMP MIB module EKINOPS-PmPassive-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ekinops/EKINOPS-PmPassive-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ekinops, = mibBuilder.importSymbols("EKINOPS-MIB", "ekinops")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
modulePmPassive = ModuleIdentity((1, 3, 6, 1, 4, 1, 20044, 20))
modulePmPassive.setRevisions(('2007-01-05 00:00',))
if mibBuilder.loadTexts: modulePmPassive.setLastUpdated('200701050000Z')
if mibBuilder.loadTexts: modulePmPassive.setOrganization('Ekinops')
pmpassiveri = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 20, 1))
pmpassiveRinvHwPlatform = MibScalar((1, 3, 6, 1, 4, 1, 20044, 20, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmpassiveRinvHwPlatform.setStatus('current')
mibBuilder.exportSymbols("EKINOPS-PmPassive-MIB", pmpassiveRinvHwPlatform=pmpassiveRinvHwPlatform, modulePmPassive=modulePmPassive, pmpassiveri=pmpassiveri, PYSNMP_MODULE_ID=modulePmPassive)
