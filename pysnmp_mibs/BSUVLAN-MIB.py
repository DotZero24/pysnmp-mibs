#
# PySNMP MIB module BSUVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/BSUVLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BSUVLAN-MIB", aniBsuVlanConfOuterTagId=aniBsuVlanConfOuterTagId, aniBsuVlanConfMgmtVlanId=aniBsuVlanConfMgmtVlanId, PYSNMP_MODULE_ID=aniBsuVlan, aniBsuVlan=aniBsuVlan, aniBsuVlanConf=aniBsuVlanConf, aniBsuVlanConfOuterTagPriority=aniBsuVlanConfOuterTagPriority, aniBsuVlanConfSUMgmtVlanIdList=aniBsuVlanConfSUMgmtVlanIdList, aniBsuVlanConfMgmtVlanIdPriority=aniBsuVlanConfMgmtVlanIdPriority)
