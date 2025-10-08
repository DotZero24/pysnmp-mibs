#
# PySNMP MIB module ELTEX-MES-ISS-CFA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-CFA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesIssCfaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20))
eltMesIssCfaMIB.setRevisions(('2020-05-25 00:00',))
if mibBuilder.loadTexts: eltMesIssCfaMIB.setLastUpdated('202005250000Z')
if mibBuilder.loadTexts: eltMesIssCfaMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssCfaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1))
eltMesIssCfaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 2))
eltMesIssCfaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1))
eltMesIssCfaGlobalMtu = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 12288))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssCfaGlobalMtu.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-CFA-MIB", eltMesIssCfaGlobalMtu=eltMesIssCfaGlobalMtu, eltMesIssCfaObjects=eltMesIssCfaObjects, eltMesIssCfaNotifications=eltMesIssCfaNotifications, eltMesIssCfaMIB=eltMesIssCfaMIB, PYSNMP_MODULE_ID=eltMesIssCfaMIB, eltMesIssCfaGlobals=eltMesIssCfaGlobals)
