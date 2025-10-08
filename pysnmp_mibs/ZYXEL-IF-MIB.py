#
# PySNMP MIB module ZYXEL-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27))
if mibBuilder.loadTexts: zyxelIf.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIf.setOrganization('Enterprise Solution ZyXEL')
zyxelIfSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1))
zyIfMaxNumberOfVlanIfs = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIfMaxNumberOfVlanIfs.setStatus('current')
zyIfMaxNumberOfLoopbackIfs = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIfMaxNumberOfLoopbackIfs.setStatus('current')
zyxelIfTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3), )
if mibBuilder.loadTexts: zyxelIfTable.setStatus('current')
zyxelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1), ).setIndexNames((0, "ZYXEL-IF-MIB", "zyIfType"), (0, "ZYXEL-IF-MIB", "zyIfId"))
if mibBuilder.loadTexts: zyxelIfEntry.setStatus('current')
zyIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("loopback", 2))))
if mibBuilder.loadTexts: zyIfType.setStatus('current')
zyIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: zyIfId.setStatus('current')
zyIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyIfRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IF-MIB", zyIfId=zyIfId, zyIfRowStatus=zyIfRowStatus, zyxelIfSetup=zyxelIfSetup, zyxelIf=zyxelIf, zyIfMaxNumberOfLoopbackIfs=zyIfMaxNumberOfLoopbackIfs, PYSNMP_MODULE_ID=zyxelIf, zyIfType=zyIfType, zyIfMaxNumberOfVlanIfs=zyIfMaxNumberOfVlanIfs, zyxelIfTable=zyxelIfTable, zyxelIfEntry=zyxelIfEntry)
