#
# PySNMP MIB module Juniper-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-HDLC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniHdlcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9))
juniHdlcMIB.setRevisions(('2003-10-03 19:25', '2002-09-16 21:44', '2001-11-28 13:43', '2001-03-22 14:30', '2000-01-26 00:00', '1999-07-28 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: juniHdlcMIB.setLastUpdated('200310031925Z')
if mibBuilder.loadTexts: juniHdlcMIB.setOrganization('Juniper Networks, Inc.')
juniHdlcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1))
juniHdlcNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniHdlcNextIfIndex.setStatus('current')
juniHdlcIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2), )
if mibBuilder.loadTexts: juniHdlcIfTable.setStatus('current')
juniHdlcIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1), ).setIndexNames((0, "Juniper-HDLC-MIB", "juniHdlcIfIndex"))
if mibBuilder.loadTexts: juniHdlcIfEntry.setStatus('current')
juniHdlcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniHdlcIfIndex.setStatus('current')
juniHdlcIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfRowStatus.setStatus('current')
juniHdlcIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfLowerIfIndex.setStatus('current')
juniHdlcIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32763))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfMtu.setStatus('current')
juniHdlcIfMru = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32763))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfMru.setStatus('current')
juniHdlcIfCrcSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("crc16", 1), ("crc32", 2))).clone('crc16')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfCrcSize.setStatus('current')
juniHdlcIfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfDataPolarity.setStatus('current')
juniHdlcIfClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("hdlcClockUnsupported", 0), ("hdlcClockInternal", 1), ("hdlcClockLine", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfClockMode.setStatus('current')
juniHdlcIfClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("hdlcClockRateUnsupported", 0), ("hdlcClockRate34At368Mhz", 1), ("hdlcClockRate44At736Mhz", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfClockRate.setStatus('current')
juniHdlcIfForceDteAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forceDteAckUnsupported", 0), ("forceDteAckNormal", 1), ("forceDteAckForced", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfForceDteAck.setStatus('current')
juniHdlcIfIdleCharacter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idleCharacterFlags", 0), ("idleCharacterMarks", 1))).clone('idleCharacterFlags')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHdlcIfIdleCharacter.setStatus('current')
juniHdlcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4))
juniHdlcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1))
juniHdlcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2))
juniHdlcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 1)).setObjects(("Juniper-HDLC-MIB", "juniHdlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcCompliance = juniHdlcCompliance.setStatus('obsolete')
juniHdlcCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 2)).setObjects(("Juniper-HDLC-MIB", "juniHdlcGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcCompliance2 = juniHdlcCompliance2.setStatus('obsolete')
juniHdlcCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 3)).setObjects(("Juniper-HDLC-MIB", "juniHdlcGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcCompliance3 = juniHdlcCompliance3.setStatus('obsolete')
juniHdlcCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 4)).setObjects(("Juniper-HDLC-MIB", "juniHdlcGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcCompliance4 = juniHdlcCompliance4.setStatus('current')
juniHdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 1)).setObjects(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"), ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfMtu"), ("Juniper-HDLC-MIB", "juniHdlcIfMru"), ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcGroup = juniHdlcGroup.setStatus('obsolete')
juniHdlcGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 2)).setObjects(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"), ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfMtu"), ("Juniper-HDLC-MIB", "juniHdlcIfMru"), ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"), ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcGroup2 = juniHdlcGroup2.setStatus('obsolete')
juniHdlcGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 3)).setObjects(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"), ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfMtu"), ("Juniper-HDLC-MIB", "juniHdlcIfMru"), ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"), ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"), ("Juniper-HDLC-MIB", "juniHdlcIfClockMode"), ("Juniper-HDLC-MIB", "juniHdlcIfClockRate"), ("Juniper-HDLC-MIB", "juniHdlcIfForceDteAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcGroup3 = juniHdlcGroup3.setStatus('obsolete')
juniHdlcGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 4)).setObjects(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"), ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"), ("Juniper-HDLC-MIB", "juniHdlcIfMtu"), ("Juniper-HDLC-MIB", "juniHdlcIfMru"), ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"), ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"), ("Juniper-HDLC-MIB", "juniHdlcIfClockMode"), ("Juniper-HDLC-MIB", "juniHdlcIfClockRate"), ("Juniper-HDLC-MIB", "juniHdlcIfForceDteAck"), ("Juniper-HDLC-MIB", "juniHdlcIfIdleCharacter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHdlcGroup4 = juniHdlcGroup4.setStatus('current')
mibBuilder.exportSymbols("Juniper-HDLC-MIB", juniHdlcIfIdleCharacter=juniHdlcIfIdleCharacter, juniHdlcIfClockRate=juniHdlcIfClockRate, PYSNMP_MODULE_ID=juniHdlcMIB, juniHdlcIfForceDteAck=juniHdlcIfForceDteAck, juniHdlcGroup2=juniHdlcGroup2, juniHdlcIfMru=juniHdlcIfMru, juniHdlcCompliance=juniHdlcCompliance, juniHdlcIfEntry=juniHdlcIfEntry, juniHdlcNextIfIndex=juniHdlcNextIfIndex, juniHdlcIfDataPolarity=juniHdlcIfDataPolarity, juniHdlcCompliance2=juniHdlcCompliance2, juniHdlcIfCrcSize=juniHdlcIfCrcSize, juniHdlcIfClockMode=juniHdlcIfClockMode, juniHdlcCompliance3=juniHdlcCompliance3, juniHdlcMIB=juniHdlcMIB, juniHdlcIfMtu=juniHdlcIfMtu, juniHdlcIfLowerIfIndex=juniHdlcIfLowerIfIndex, juniHdlcIfIndex=juniHdlcIfIndex, juniHdlcIfRowStatus=juniHdlcIfRowStatus, juniHdlcGroups=juniHdlcGroups, juniHdlcGroup=juniHdlcGroup, juniHdlcCompliances=juniHdlcCompliances, juniHdlcIfTable=juniHdlcIfTable, juniHdlcObjects=juniHdlcObjects, juniHdlcCompliance4=juniHdlcCompliance4, juniHdlcConformance=juniHdlcConformance, juniHdlcGroup4=juniHdlcGroup4, juniHdlcGroup3=juniHdlcGroup3)
