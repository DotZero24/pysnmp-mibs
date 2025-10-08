#
# PySNMP MIB module SYNOLOGY-NFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-NFS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nfs = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 107))
nfs.setRevisions(('2018-08-10 00:00',))
if mibBuilder.loadTexts: nfs.setLastUpdated('201808100000Z')
if mibBuilder.loadTexts: nfs.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
nfsTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 107, 1), )
if mibBuilder.loadTexts: nfsTable.setStatus('current')
nfsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1), ).setIndexNames((0, "SYNOLOGY-NFS-MIB", "nfsIndex"))
if mibBuilder.loadTexts: nfsEntry.setStatus('current')
nfsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: nfsIndex.setStatus('current')
nfsName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsName.setStatus('current')
nfsTotalMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsTotalMaxLatency.setStatus('current')
nfsReadMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReadMaxLatency.setStatus('current')
nfsWriteMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsWriteMaxLatency.setStatus('current')
nfsTotalOPS = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsTotalOPS.setStatus('current')
nfsReadOPS = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReadOPS.setStatus('current')
nfsWriteOPS = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsWriteOPS.setStatus('current')
nfsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 107, 2))
nfsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 107, 2, 1))
nfsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 107, 2, 2))
nfsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 107, 2, 1, 1)).setObjects(("SYNOLOGY-NFS-MIB", "nfsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfsCompliance = nfsCompliance.setStatus('current')
nfsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 107, 2, 2, 1)).setObjects(("SYNOLOGY-NFS-MIB", "nfsName"), ("SYNOLOGY-NFS-MIB", "nfsTotalMaxLatency"), ("SYNOLOGY-NFS-MIB", "nfsReadMaxLatency"), ("SYNOLOGY-NFS-MIB", "nfsWriteMaxLatency"), ("SYNOLOGY-NFS-MIB", "nfsTotalOPS"), ("SYNOLOGY-NFS-MIB", "nfsReadOPS"), ("SYNOLOGY-NFS-MIB", "nfsWriteOPS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfsGroup = nfsGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-NFS-MIB", nfsName=nfsName, nfsGroup=nfsGroup, nfsConformance=nfsConformance, nfsReadMaxLatency=nfsReadMaxLatency, nfsCompliances=nfsCompliances, PYSNMP_MODULE_ID=nfs, nfsTable=nfsTable, nfsReadOPS=nfsReadOPS, nfsTotalMaxLatency=nfsTotalMaxLatency, nfs=nfs, nfsWriteOPS=nfsWriteOPS, nfsGroups=nfsGroups, nfsCompliance=nfsCompliance, nfsIndex=nfsIndex, synology=synology, nfsWriteMaxLatency=nfsWriteMaxLatency, nfsTotalOPS=nfsTotalOPS, nfsEntry=nfsEntry)
