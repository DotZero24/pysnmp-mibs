#
# PySNMP MIB module GBNL2PppoePlus-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/gcom/GBNL2PppoePlus-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
gbnL2PppoePlus = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6))
gbnL2PppoePlus.setRevisions(('1907-11-22 00:00',))
if mibBuilder.loadTexts: gbnL2PppoePlus.setLastUpdated('0711220000Z')
if mibBuilder.loadTexts: gbnL2PppoePlus.setOrganization('Greentech')
pppoeplusOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusOnOff.setStatus('current')
pppoeplusType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("standard", 0), ("huawei", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusType.setStatus('current')
mibBuilder.exportSymbols("GBNL2PppoePlus-MIB", PYSNMP_MODULE_ID=gbnL2PppoePlus, pppoeplusType=pppoeplusType, gbnL2PppoePlus=gbnL2PppoePlus, pppoeplusOnOff=pppoeplusOnOff)
