#
# PySNMP MIB module CISCO-CDSTV-INGEST-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCdstvIngestTuningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 750))
ciscoCdstvIngestTuningMIB.setRevisions(('2010-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvIngestTuningMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 0))
ciscoCdstvIngestTuningMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1))
ciscoCdstvIngestTuningMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2))
ciscoCdstvIngestTuningMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1))
cdstvTrickModeSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1), )
if mibBuilder.loadTexts: cdstvTrickModeSpeedTable.setStatus('current')
cdstvTrickModeSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeedIndex"))
if mibBuilder.loadTexts: cdstvTrickModeSpeedEntry.setStatus('current')
cdstvTrickModeSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdstvTrickModeSpeedIndex.setStatus('current')
cdstvTrickModeSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-127, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvTrickModeSpeed.setStatus('current')
cdstvServerIngestMPEGSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2))
cdstvServerPIDStandardization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerPIDStandardization.setStatus('current')
cdstvServerSequenceEndRemove = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSequenceEndRemove.setStatus('current')
cdstvServerRateStandardize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerRateStandardize.setStatus('current')
ciscoCdstvIngestTuningMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2))
ciscoCdstvIngestTuningMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "ciscoCdstvIngestTuningMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBCompliance = ciscoCdstvIngestTuningMIBCompliance.setStatus('current')
ciscoCdstvIngestTuningMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeed"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerPIDStandardization"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerSequenceEndRemove"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerRateStandardize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBMainObjectGroup = ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-INGEST-TUNING-MIB", ciscoCdstvIngestTuningMIBConform=ciscoCdstvIngestTuningMIBConform, cdstvServerSequenceEndRemove=cdstvServerSequenceEndRemove, cdstvServerPIDStandardization=cdstvServerPIDStandardization, cdstvServerRateStandardize=cdstvServerRateStandardize, cdstvTrickModeSpeedEntry=cdstvTrickModeSpeedEntry, ciscoCdstvIngestTuningMIB=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBCompliances=ciscoCdstvIngestTuningMIBCompliances, ciscoCdstvIngestTuningMIBObjects=ciscoCdstvIngestTuningMIBObjects, ciscoCdstvIngestTuningMIBGroups=ciscoCdstvIngestTuningMIBGroups, PYSNMP_MODULE_ID=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBCompliance=ciscoCdstvIngestTuningMIBCompliance, cdstvTrickModeSpeedIndex=cdstvTrickModeSpeedIndex, cdstvServerIngestMPEGSettings=cdstvServerIngestMPEGSettings, cdstvTrickModeSpeedTable=cdstvTrickModeSpeedTable, ciscoCdstvIngestTuningMIBNotifs=ciscoCdstvIngestTuningMIBNotifs, cdstvTrickModeSpeed=cdstvTrickModeSpeed, ciscoCdstvIngestTuningMIBMainObjectGroup=ciscoCdstvIngestTuningMIBMainObjectGroup)
