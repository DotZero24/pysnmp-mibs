#
# PySNMP MIB module PCUBE-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/PCUBE-CONFIG-COPY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pcubeMgmt, = mibBuilder.importSymbols("PCUBE-SMI", "pcubeMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
pcubeConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 3, 1))
pcubeConfigCopyMIB.setRevisions(('2006-04-06 20:00', '2002-01-14 20:00',))
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setLastUpdated('200604062000Z')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setOrganization('Cisco Systems, Inc.')
class ConfigFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("startupConfig", 1), ("runningConfig", 2))

pcubeConfigCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1))
pcubeConfigCopyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2))
pcubeConfigCopyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1))
pcubeConfigCopyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2))
pcubeCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1))
pcubeCopyTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: pcubeCopyTable.setStatus('current')
pcubeCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1), ).setIndexNames((0, "PCUBE-CONFIG-COPY-MIB", "pcubeCopyIndex"))
if mibBuilder.loadTexts: pcubeCopyEntry.setStatus('current')
pcubeCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pcubeCopyIndex.setStatus('current')
pcubeCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyEntryRowStatus.setStatus('current')
pcubeCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopySourceFileType.setStatus('current')
pcubeCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyDestFileType.setStatus('current')
pcubeConfigCopyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeConfigCopyMIBCompliance = pcubeConfigCopyMIBCompliance.setStatus('current')
pcubeCopyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyEntryRowStatus"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopySourceFileType"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopyDestFileType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeCopyGroup = pcubeCopyGroup.setStatus('current')
mibBuilder.exportSymbols("PCUBE-CONFIG-COPY-MIB", pcubeConfigCopyMIBGroups=pcubeConfigCopyMIBGroups, PYSNMP_MODULE_ID=pcubeConfigCopyMIB, pcubeConfigCopyMIBCompliance=pcubeConfigCopyMIBCompliance, pcubeCopyIndex=pcubeCopyIndex, pcubeCopy=pcubeCopy, pcubeConfigCopyMIB=pcubeConfigCopyMIB, pcubeCopySourceFileType=pcubeCopySourceFileType, pcubeConfigCopyMIBObjects=pcubeConfigCopyMIBObjects, pcubeCopyEntryRowStatus=pcubeCopyEntryRowStatus, pcubeConfigCopyMIBCompliances=pcubeConfigCopyMIBCompliances, pcubeCopyTable=pcubeCopyTable, pcubeCopyEntry=pcubeCopyEntry, pcubeConfigCopyMIBConformance=pcubeConfigCopyMIBConformance, pcubeCopyDestFileType=pcubeCopyDestFileType, pcubeCopyGroup=pcubeCopyGroup, ConfigFileType=ConfigFileType)
