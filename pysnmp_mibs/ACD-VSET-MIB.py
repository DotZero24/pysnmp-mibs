#
# PySNMP MIB module ACD-VSET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/accedian/ACD-VSET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
acdVSet = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 13))
acdVSet.setRevisions(('2015-05-05 01:00', '2013-04-04 01:00', '2013-02-13 01:00', '2012-01-11 01:00',))
if mibBuilder.loadTexts: acdVSet.setLastUpdated('201505050100Z')
if mibBuilder.loadTexts: acdVSet.setOrganization('Accedian Networks, Inc.')
acdVSetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 0))
acdVSetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1))
acdVSetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2))
acdVSetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1))
class AcdVsetVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2), ("tvlan", 3))

class AcdVsetOuterVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("cvlan", 1), ("svlan", 2), ("tvlan", 3))

acdVSetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: acdVSetConfigTable.setStatus('current')
acdVSetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "ACD-VSET-MIB", "acdVSetConfigPolicyListID"), (0, "ACD-VSET-MIB", "acdVSetConfigID"))
if mibBuilder.loadTexts: acdVSetConfigEntry.setStatus('current')
acdVSetConfigPolicyListID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdVSetConfigPolicyListID.setStatus('current')
acdVSetConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: acdVSetConfigID.setStatus('current')
acdVSetConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigRowStatus.setStatus('current')
acdVSetConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigName.setStatus('current')
acdVSetConfigVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 5), AcdVsetVlanType().clone('cvlan')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanType.setStatus('current')
acdVSetConfigVlanIDs0to1023 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs0to1023.setStatus('current')
acdVSetConfigVlanIDs1024to2047 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs1024to2047.setStatus('current')
acdVSetConfigVlanIDs2048to3071 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs2048to3071.setStatus('current')
acdVSetConfigVlanIDs3072to4095 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigVlanIDs3072to4095.setStatus('current')
acdVSetConfigOuterVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 10), AcdVsetOuterVlanType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigOuterVlanType.setStatus('current')
acdVSetConfigOuterVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 13, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdVSetConfigOuterVlanID.setStatus('current')
acdVSetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1))
acdVSetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2))
acdVSetConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 2, 1)).setObjects(("ACD-VSET-MIB", "acdVSetConfigRowStatus"), ("ACD-VSET-MIB", "acdVSetConfigName"), ("ACD-VSET-MIB", "acdVSetConfigVlanType"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs0to1023"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs1024to2047"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs2048to3071"), ("ACD-VSET-MIB", "acdVSetConfigVlanIDs3072to4095"), ("ACD-VSET-MIB", "acdVSetConfigOuterVlanType"), ("ACD-VSET-MIB", "acdVSetConfigOuterVlanID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdVSetConfigGroup = acdVSetConfigGroup.setStatus('current')
acdVSetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 13, 2, 1, 1)).setObjects(("ACD-VSET-MIB", "acdVSetConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdVSetCompliance = acdVSetCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-VSET-MIB", acdVSetConfigVlanIDs3072to4095=acdVSetConfigVlanIDs3072to4095, acdVSetConfigVlanType=acdVSetConfigVlanType, AcdVsetOuterVlanType=AcdVsetOuterVlanType, PYSNMP_MODULE_ID=acdVSet, acdVSetConformance=acdVSetConformance, acdVSetConfigGroup=acdVSetConfigGroup, acdVSetGroups=acdVSetGroups, acdVSetConfigOuterVlanID=acdVSetConfigOuterVlanID, acdVSetConfigVlanIDs2048to3071=acdVSetConfigVlanIDs2048to3071, acdVSetConfigPolicyListID=acdVSetConfigPolicyListID, acdVSet=acdVSet, acdVSetConfigEntry=acdVSetConfigEntry, acdVSetConfigRowStatus=acdVSetConfigRowStatus, acdVSetNotifications=acdVSetNotifications, acdVSetConfigVlanIDs1024to2047=acdVSetConfigVlanIDs1024to2047, acdVSetConfig=acdVSetConfig, acdVSetConfigName=acdVSetConfigName, acdVSetCompliance=acdVSetCompliance, acdVSetConfigID=acdVSetConfigID, acdVSetCompliances=acdVSetCompliances, AcdVsetVlanType=AcdVsetVlanType, acdVSetConfigOuterVlanType=acdVSetConfigOuterVlanType, acdVSetMIBObjects=acdVSetMIBObjects, acdVSetConfigTable=acdVSetConfigTable, acdVSetConfigVlanIDs0to1023=acdVSetConfigVlanIDs0to1023)
