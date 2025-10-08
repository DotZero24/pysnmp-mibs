#
# PySNMP MIB module GBNL2PppoePlus-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/gcom/GBNL2PppoePlus-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
gbnL2PppoePlus = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6))
gbnL2PppoePlus.setRevisions(('1907-11-22 00:00',))
if mibBuilder.loadTexts: gbnL2PppoePlus.setLastUpdated('0711220000Z')
if mibBuilder.loadTexts: gbnL2PppoePlus.setOrganization('Greentech')
pppoeplusOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusOnOff.setStatus('current')
pppoeplusType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("standard", 0), ("huawei", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusType.setStatus('current')
mibBuilder.exportSymbols("GBNL2PppoePlus-MIB", gbnL2PppoePlus=gbnL2PppoePlus, PYSNMP_MODULE_ID=gbnL2PppoePlus, pppoeplusOnOff=pppoeplusOnOff, pppoeplusType=pppoeplusType)
