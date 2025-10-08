#
# PySNMP MIB module Papouch-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/papouch/Papouch-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
papouchProjekt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18248))
papouchProjekt.setRevisions(('2006-04-07 00:00',))
if mibBuilder.loadTexts: papouchProjekt.setLastUpdated('200604070000Z')
if mibBuilder.loadTexts: papouchProjekt.setOrganization('PaPouch s.r.o')
tme = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 1))
if mibBuilder.loadTexts: tme.setStatus('current')
quido = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 2))
if mibBuilder.loadTexts: quido.setStatus('current')
eccitace = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 3))
if mibBuilder.loadTexts: eccitace.setStatus('current')
e_monitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 18248, 4))
if mibBuilder.loadTexts: e_monitor.setStatus('current')
mibBuilder.exportSymbols("Papouch-SMI", quido=quido, papouchProjekt=papouchProjekt, eccitace=eccitace, e_monitor=e_monitor, PYSNMP_MODULE_ID=papouchProjekt, tme=tme)
