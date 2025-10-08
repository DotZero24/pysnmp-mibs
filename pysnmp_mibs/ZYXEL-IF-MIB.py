#
# PySNMP MIB module ZYXEL-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-IF-MIB", zyIfRowStatus=zyIfRowStatus, zyIfMaxNumberOfLoopbackIfs=zyIfMaxNumberOfLoopbackIfs, zyIfMaxNumberOfVlanIfs=zyIfMaxNumberOfVlanIfs, zyxelIfSetup=zyxelIfSetup, zyxelIf=zyxelIf, zyIfType=zyIfType, zyxelIfTable=zyxelIfTable, zyxelIfEntry=zyxelIfEntry, zyIfId=zyIfId, PYSNMP_MODULE_ID=zyxelIf)
