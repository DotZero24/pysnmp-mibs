#
# PySNMP MIB module ELTEX-MES-APPLICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-APPLICATIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rsPingInetEntry, = mibBuilder.importSymbols("RADLAN-rndApplications", "rsPingInetEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltMesApplicationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96))
eltMesApplicationsMIB.setRevisions(('2018-06-26 00:00',))
if mibBuilder.loadTexts: eltMesApplicationsMIB.setLastUpdated('201806260000Z')
if mibBuilder.loadTexts: eltMesApplicationsMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesApplicationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96, 1))
eltMesApplicationsGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96, 1, 1))
eltPingInetTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96, 1, 1, 1), )
if mibBuilder.loadTexts: eltPingInetTable.setStatus('current')
eltPingInetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96, 1, 1, 1, 1), )
rsPingInetEntry.registerAugmentions(("ELTEX-MES-APPLICATIONS-MIB", "eltPingInetEntry"))
eltPingInetEntry.setIndexNames(*rsPingInetEntry.getIndexNames())
if mibBuilder.loadTexts: eltPingInetEntry.setStatus('current')
eltPingInetDontFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 96, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPingInetDontFragment.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-APPLICATIONS-MIB", eltPingInetEntry=eltPingInetEntry, eltPingInetDontFragment=eltPingInetDontFragment, eltMesApplicationsMIB=eltMesApplicationsMIB, PYSNMP_MODULE_ID=eltMesApplicationsMIB, eltPingInetTable=eltPingInetTable, eltMesApplicationsGlobals=eltMesApplicationsGlobals, eltMesApplicationsObjects=eltMesApplicationsObjects)
