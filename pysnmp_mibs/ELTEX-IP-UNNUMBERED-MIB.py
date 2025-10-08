#
# PySNMP MIB module ELTEX-IP-UNNUMBERED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-IP-UNNUMBERED-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eltexIpUnnumberedMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 42))
eltexIpUnnumberedMIB.setRevisions(('2017-10-16 00:00',))
if mibBuilder.loadTexts: eltexIpUnnumberedMIB.setLastUpdated('201710160000Z')
if mibBuilder.loadTexts: eltexIpUnnumberedMIB.setOrganization('Eltex Enterprise Co, Ltd.')
eltexIpUnnumberedMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 42, 1))
eltexIpUnnumberedInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 42, 1, 1), )
if mibBuilder.loadTexts: eltexIpUnnumberedInterfaceTable.setStatus('current')
eltexIpUnnumberedInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 42, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltexIpUnnumberedInterfaceEntry.setStatus('current')
eltexIpUnnumberedParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 42, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexIpUnnumberedParentIfIndex.setStatus('current')
eltexIpUnnumberedRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 42, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltexIpUnnumberedRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-IP-UNNUMBERED-MIB", eltexIpUnnumberedParentIfIndex=eltexIpUnnumberedParentIfIndex, eltexIpUnnumberedInterfaceEntry=eltexIpUnnumberedInterfaceEntry, eltexIpUnnumberedMIB=eltexIpUnnumberedMIB, eltexIpUnnumberedMIBObjects=eltexIpUnnumberedMIBObjects, PYSNMP_MODULE_ID=eltexIpUnnumberedMIB, eltexIpUnnumberedRowStatus=eltexIpUnnumberedRowStatus, eltexIpUnnumberedInterfaceTable=eltexIpUnnumberedInterfaceTable)
