#
# PySNMP MIB module INFINERA-TP-FMPSCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPSCGPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-FMPSCGPTP-MIB", fmpScgPtpProvisionedNeighborTP=fmpScgPtpProvisionedNeighborTP, fmpScgPtpEntry=fmpScgPtpEntry, fmpScgPtpMPOAID=fmpScgPtpMPOAID, fmpScgPtpCompliances=fmpScgPtpCompliances, fmpScgPtpGroups=fmpScgPtpGroups, fmpScgPtpNeighborFPMPOID=fmpScgPtpNeighborFPMPOID, fmpScgPtpCompliance=fmpScgPtpCompliance, fmpScgPtpGroup=fmpScgPtpGroup, fmpScgPtpProvisionedOpenWaveRemoteTP=fmpScgPtpProvisionedOpenWaveRemoteTP, PYSNMP_MODULE_ID=fmpScgPtpMIB, fmpScgPtpTable=fmpScgPtpTable, fmpScgPtpMIB=fmpScgPtpMIB, fmpScgPtpConformance=fmpScgPtpConformance)
