#
# PySNMP MIB module INFINERA-TP-FMPSCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPSCGPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fmpScgPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53))
fmpScgPtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: fmpScgPtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: fmpScgPtpMIB.setOrganization('Infinera')
fmpScgPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1), )
if mibBuilder.loadTexts: fmpScgPtpTable.setStatus('current')
fmpScgPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fmpScgPtpEntry.setStatus('current')
fmpScgPtpProvisionedNeighborTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpScgPtpProvisionedNeighborTP.setStatus('current')
fmpScgPtpMPOAID = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpScgPtpMPOAID.setStatus('current')
fmpScgPtpProvisionedOpenWaveRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpScgPtpProvisionedOpenWaveRemoteTP.setStatus('current')
fmpScgPtpNeighborFPMPOID = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpScgPtpNeighborFPMPOID.setStatus('current')
fmpScgPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3))
fmpScgPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 1))
fmpScgPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 2))
fmpScgPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 1, 1)).setObjects(("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpScgPtpCompliance = fmpScgPtpCompliance.setStatus('current')
fmpScgPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 2, 1)).setObjects(("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpProvisionedNeighborTP"), ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpMPOAID"), ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpProvisionedOpenWaveRemoteTP"), ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpNeighborFPMPOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpScgPtpGroup = fmpScgPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-FMPSCGPTP-MIB", fmpScgPtpEntry=fmpScgPtpEntry, fmpScgPtpMPOAID=fmpScgPtpMPOAID, fmpScgPtpCompliances=fmpScgPtpCompliances, fmpScgPtpGroup=fmpScgPtpGroup, fmpScgPtpTable=fmpScgPtpTable, fmpScgPtpConformance=fmpScgPtpConformance, fmpScgPtpProvisionedNeighborTP=fmpScgPtpProvisionedNeighborTP, PYSNMP_MODULE_ID=fmpScgPtpMIB, fmpScgPtpNeighborFPMPOID=fmpScgPtpNeighborFPMPOID, fmpScgPtpProvisionedOpenWaveRemoteTP=fmpScgPtpProvisionedOpenWaveRemoteTP, fmpScgPtpCompliance=fmpScgPtpCompliance, fmpScgPtpGroups=fmpScgPtpGroups, fmpScgPtpMIB=fmpScgPtpMIB)
