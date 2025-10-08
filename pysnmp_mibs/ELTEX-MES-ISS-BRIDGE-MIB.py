#
# PySNMP MIB module ELTEX-MES-ISS-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-BRIDGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:10 2025
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
eltMesIssBridgeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 14))
eltMesIssBridgeMIB.setRevisions(('2019-05-21 00:00',))
if mibBuilder.loadTexts: eltMesIssBridgeMIB.setLastUpdated('201906030000Z')
if mibBuilder.loadTexts: eltMesIssBridgeMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1))
eltMesIssMstMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1))
mibBuilder.exportSymbols("ELTEX-MES-ISS-BRIDGE-MIB", eltMesIssMstMIB=eltMesIssMstMIB, PYSNMP_MODULE_ID=eltMesIssBridgeMIB, eltMesIssBridgeMIB=eltMesIssBridgeMIB, eltMesIssBridgeMIBObjects=eltMesIssBridgeMIBObjects)
