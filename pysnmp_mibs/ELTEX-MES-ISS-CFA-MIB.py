#
# PySNMP MIB module ELTEX-MES-ISS-CFA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-CFA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesIssCfaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20))
eltMesIssCfaMIB.setRevisions(('2020-05-25 00:00',))
if mibBuilder.loadTexts: eltMesIssCfaMIB.setLastUpdated('202005250000Z')
if mibBuilder.loadTexts: eltMesIssCfaMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssCfaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1))
eltMesIssCfaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 2))
eltMesIssCfaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1))
eltMesIssCfaGlobalMtu = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 12288))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssCfaGlobalMtu.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-CFA-MIB", eltMesIssCfaObjects=eltMesIssCfaObjects, PYSNMP_MODULE_ID=eltMesIssCfaMIB, eltMesIssCfaMIB=eltMesIssCfaMIB, eltMesIssCfaGlobals=eltMesIssCfaGlobals, eltMesIssCfaGlobalMtu=eltMesIssCfaGlobalMtu, eltMesIssCfaNotifications=eltMesIssCfaNotifications)
