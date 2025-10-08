#
# PySNMP MIB module BSUVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/BSUVLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 11))
if mibBuilder.loadTexts: aniBsuVlan.setLastUpdated('0210251725Z')
if mibBuilder.loadTexts: aniBsuVlan.setOrganization('Aperto Networks')
aniBsuVlanConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1))
aniBsuVlanConfMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfMgmtVlanId.setStatus('current')
aniBsuVlanConfOuterTagId = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfOuterTagId.setStatus('current')
aniBsuVlanConfMgmtVlanIdPriority = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfMgmtVlanIdPriority.setStatus('current')
aniBsuVlanConfOuterTagPriority = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfOuterTagPriority.setStatus('current')
aniBsuVlanConfSUMgmtVlanIdList = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuVlanConfSUMgmtVlanIdList.setStatus('current')
mibBuilder.exportSymbols("BSUVLAN-MIB", aniBsuVlanConfOuterTagId=aniBsuVlanConfOuterTagId, PYSNMP_MODULE_ID=aniBsuVlan, aniBsuVlanConfMgmtVlanId=aniBsuVlanConfMgmtVlanId, aniBsuVlanConf=aniBsuVlanConf, aniBsuVlanConfMgmtVlanIdPriority=aniBsuVlanConfMgmtVlanIdPriority, aniBsuVlan=aniBsuVlan, aniBsuVlanConfOuterTagPriority=aniBsuVlanConfOuterTagPriority, aniBsuVlanConfSUMgmtVlanIdList=aniBsuVlanConfSUMgmtVlanIdList)
