#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonStatus, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lhnNusCommonStatusModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 99))
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setLastUpdated('0106010000Z')
if mibBuilder.loadTexts: lhnNusCommonStatusModule.setOrganization('LeftHand Networks, Inc.')
status = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('current')
statusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusMessage.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB", lhnNusCommonStatusModule=lhnNusCommonStatusModule, PYSNMP_MODULE_ID=lhnNusCommonStatusModule, statusMessage=statusMessage, status=status)
