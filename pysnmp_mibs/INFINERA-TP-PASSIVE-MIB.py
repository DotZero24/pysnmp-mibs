#
# PySNMP MIB module INFINERA-TP-PASSIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PASSIVE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
commonTerminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonTerminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-PASSIVE-MIB", passivePtpCompliance=passivePtpCompliance, passivePtpTable=passivePtpTable, passivePtpEntry=passivePtpEntry, passivePtpCompliances=passivePtpCompliances, passivePtpConformance=passivePtpConformance, PYSNMP_MODULE_ID=passivePtpMIB, passiveMoId=passiveMoId, passivePtpType=passivePtpType, passivePtpGroups=passivePtpGroups, passivePtpGroup=passivePtpGroup, passivePtpMIB=passivePtpMIB, passivePtpProvNbrTP=passivePtpProvNbrTP)
