#
# PySNMP MIB module INFINERA-TP-PASSIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PASSIVE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
commonTerminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonTerminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
passivePtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2))
passivePtpMIB.setRevisions(('2017-01-08 00:00',))
if mibBuilder.loadTexts: passivePtpMIB.setLastUpdated('201708010000Z')
if mibBuilder.loadTexts: passivePtpMIB.setOrganization('Infinera')
passivePtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1), )
if mibBuilder.loadTexts: passivePtpTable.setStatus('current')
passivePtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: passivePtpEntry.setStatus('current')
passiveMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: passiveMoId.setStatus('current')
passivePtpType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: passivePtpType.setStatus('current')
passivePtpProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: passivePtpProvNbrTP.setStatus('current')
passivePtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3))
passivePtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 1))
passivePtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 2))
passivePtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 1, 1)).setObjects(("INFINERA-TP-PASSIVE-MIB", "passivePtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    passivePtpCompliance = passivePtpCompliance.setStatus('current')
passivePtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 2, 1)).setObjects(("INFINERA-TP-PASSIVE-MIB", "passiveMoId"), ("INFINERA-TP-PASSIVE-MIB", "passivePtpType"), ("INFINERA-TP-PASSIVE-MIB", "passivePtpProvNbrTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    passivePtpGroup = passivePtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-PASSIVE-MIB", passiveMoId=passiveMoId, passivePtpConformance=passivePtpConformance, passivePtpTable=passivePtpTable, PYSNMP_MODULE_ID=passivePtpMIB, passivePtpMIB=passivePtpMIB, passivePtpCompliance=passivePtpCompliance, passivePtpCompliances=passivePtpCompliances, passivePtpGroups=passivePtpGroups, passivePtpType=passivePtpType, passivePtpGroup=passivePtpGroup, passivePtpEntry=passivePtpEntry, passivePtpProvNbrTP=passivePtpProvNbrTP)
