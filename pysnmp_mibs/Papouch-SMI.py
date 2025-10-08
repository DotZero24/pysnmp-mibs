#
# PySNMP MIB module Papouch-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/papouch/Papouch-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("Papouch-SMI", eccitace=eccitace, e_monitor=e_monitor, tme=tme, PYSNMP_MODULE_ID=papouchProjekt, papouchProjekt=papouchProjekt, quido=quido)
