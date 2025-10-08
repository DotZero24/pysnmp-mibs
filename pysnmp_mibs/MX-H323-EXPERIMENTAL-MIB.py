#
# PySNMP MIB module MX-H323-EXPERIMENTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-H323-EXPERIMENTAL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
MxIpHostName, MxEnableState = mibBuilder.importSymbols("MX-TC", "MxIpHostName", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h323ExperimentalMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 60))
h323ExperimentalMIB.setRevisions(('2007-04-06 00:00', '2005-03-25 00:00', '2005-03-25 00:00', '2004-10-04 00:00', '2004-08-03 00:00', '2003-10-20 00:00', '2003-10-06 00:00',))
if mibBuilder.loadTexts: h323ExperimentalMIB.setLastUpdated('200704060000Z')
if mibBuilder.loadTexts: h323ExperimentalMIB.setOrganization('Mediatrix Telecom, Inc.')
h323ExperimentalMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1))
h323ExperimentalConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 60, 2))
h323Interop = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5))
h323RegAsGateway = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323RegAsGateway.setStatus('current')
h323AliasTypeRestriction = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 15), MxEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323AliasTypeRestriction.setStatus('current')
h323AcceleratedRequestedLogicalChannel = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 18), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323AcceleratedRequestedLogicalChannel.setStatus('current')
h323VoiceIfCodecTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20), )
if mibBuilder.loadTexts: h323VoiceIfCodecTable.setStatus('current')
h323VoiceIfCodecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20, 1), ).setIndexNames((0, "MX-H323-EXPERIMENTAL-MIB", "ifIndex"))
if mibBuilder.loadTexts: h323VoiceIfCodecEntry.setStatus('current')
h323VoiceIfCodecG729Enable = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 20, 1, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323VoiceIfCodecG729Enable.setStatus('current')
h323AddT38MediaControlChannel = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 50), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323AddT38MediaControlChannel.setStatus('current')
h323UseEvenT38Port = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 60, 1, 5, 100), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323UseEvenT38Port.setStatus('current')
h323ExperimentalCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 1))
h323ExperimentalBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 1, 5)).setObjects(("MX-H323-EXPERIMENTAL-MIB", "h323ExperimentalGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h323ExperimentalBasicComplVer1 = h323ExperimentalBasicComplVer1.setStatus('current')
h323ExperimentalGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 2))
h323ExperimentalGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 60, 2, 2, 5)).setObjects(("MX-H323-EXPERIMENTAL-MIB", "h323RegAsGateway"), ("MX-H323-EXPERIMENTAL-MIB", "h323AddT38MediaControlChannel"), ("MX-H323-EXPERIMENTAL-MIB", "h323UseEvenT38Port"), ("MX-H323-EXPERIMENTAL-MIB", "h323VoiceIfCodecG729Enable"), ("MX-H323-EXPERIMENTAL-MIB", "h323AliasTypeRestriction"), ("MX-H323-EXPERIMENTAL-MIB", "h323AcceleratedRequestedLogicalChannel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h323ExperimentalGroupVer1 = h323ExperimentalGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-H323-EXPERIMENTAL-MIB", h323RegAsGateway=h323RegAsGateway, h323ExperimentalCompliances=h323ExperimentalCompliances, h323AcceleratedRequestedLogicalChannel=h323AcceleratedRequestedLogicalChannel, h323VoiceIfCodecTable=h323VoiceIfCodecTable, h323VoiceIfCodecG729Enable=h323VoiceIfCodecG729Enable, h323UseEvenT38Port=h323UseEvenT38Port, h323ExperimentalBasicComplVer1=h323ExperimentalBasicComplVer1, PYSNMP_MODULE_ID=h323ExperimentalMIB, h323ExperimentalGroupVer1=h323ExperimentalGroupVer1, h323Interop=h323Interop, h323ExperimentalGroups=h323ExperimentalGroups, h323AliasTypeRestriction=h323AliasTypeRestriction, h323ExperimentalConformance=h323ExperimentalConformance, h323ExperimentalMIBObjects=h323ExperimentalMIBObjects, h323AddT38MediaControlChannel=h323AddT38MediaControlChannel, h323ExperimentalMIB=h323ExperimentalMIB, h323VoiceIfCodecEntry=h323VoiceIfCodecEntry)
