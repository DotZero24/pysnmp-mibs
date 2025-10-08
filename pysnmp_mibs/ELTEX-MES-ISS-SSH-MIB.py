#
# PySNMP MIB module ELTEX-MES-ISS-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:55 2025
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
eltMesIssSshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30))
eltMesIssSshMIB.setRevisions(('2022-04-19 00:00',))
if mibBuilder.loadTexts: eltMesIssSshMIB.setLastUpdated('202204190000Z')
if mibBuilder.loadTexts: eltMesIssSshMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssSshObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1))
eltMesIssSshGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1))
eltMesIssSshAuthTypes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1, 1), Bits().clone(namedValues=NamedValues(("password", 0), ("publickey", 1))).clone(hexValue="80")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSshAuthTypes.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SSH-MIB", eltMesIssSshObjects=eltMesIssSshObjects, eltMesIssSshGlobals=eltMesIssSshGlobals, PYSNMP_MODULE_ID=eltMesIssSshMIB, eltMesIssSshAuthTypes=eltMesIssSshAuthTypes, eltMesIssSshMIB=eltMesIssSshMIB)
