#
# PySNMP MIB module ELTEX-MES-ISS-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SSH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesIssSshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30))
eltMesIssSshMIB.setRevisions(('2022-04-19 00:00',))
if mibBuilder.loadTexts: eltMesIssSshMIB.setLastUpdated('202204190000Z')
if mibBuilder.loadTexts: eltMesIssSshMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssSshObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1))
eltMesIssSshGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1))
eltMesIssSshAuthTypes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1, 1), Bits().clone(namedValues=NamedValues(("password", 0), ("publickey", 1))).clone(hexValue="80")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSshAuthTypes.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SSH-MIB", PYSNMP_MODULE_ID=eltMesIssSshMIB, eltMesIssSshMIB=eltMesIssSshMIB, eltMesIssSshGlobals=eltMesIssSshGlobals, eltMesIssSshAuthTypes=eltMesIssSshAuthTypes, eltMesIssSshObjects=eltMesIssSshObjects)
