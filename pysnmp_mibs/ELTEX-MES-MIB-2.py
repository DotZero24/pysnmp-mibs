#
# PySNMP MIB module ELTEX-MES-MIB-2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-MIB-2
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesMng, = mibBuilder.importSymbols("ELTEX-MES", "eltMesMng")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
elt_mes_mib_2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1)).setLabel("elt-mes-mib-2")
if mibBuilder.loadTexts: elt_mes_mib_2.setLastUpdated('202006110000Z')
if mibBuilder.loadTexts: elt_mes_mib_2.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesIfMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31))
eltMesSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 32))
eltSysDescr = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 32, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSysDescr.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-MIB-2", eltSysDescr=eltSysDescr, eltMesIfMIB=eltMesIfMIB, PYSNMP_MODULE_ID=elt_mes_mib_2, eltMesSystem=eltMesSystem, elt_mes_mib_2=elt_mes_mib_2)
