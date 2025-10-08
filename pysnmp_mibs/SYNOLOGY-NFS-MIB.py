#
# PySNMP MIB module SYNOLOGY-NFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-NFS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNOLOGY-NFS-MIB", nfsReadOPS=nfsReadOPS, nfsEntry=nfsEntry, PYSNMP_MODULE_ID=nfs, nfsReadMaxLatency=nfsReadMaxLatency, nfsWriteMaxLatency=nfsWriteMaxLatency, nfsGroups=nfsGroups, nfsGroup=nfsGroup, synology=synology, nfsTotalMaxLatency=nfsTotalMaxLatency, nfsCompliances=nfsCompliances, nfs=nfs, nfsIndex=nfsIndex, nfsTable=nfsTable, nfsWriteOPS=nfsWriteOPS, nfsCompliance=nfsCompliance, nfsConformance=nfsConformance, nfsTotalOPS=nfsTotalOPS, nfsName=nfsName)
