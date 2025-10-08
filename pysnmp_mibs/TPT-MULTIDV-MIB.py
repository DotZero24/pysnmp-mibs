#
# PySNMP MIB module TPT-MULTIDV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-MULTIDV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
policyDVObjs, = mibBuilder.importSymbols("TPT-POLICY-MIB", "policyDVObjs")
tpt_multidv_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2)).setLabel("tpt-multidv-objs")
tpt_multidv_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_multidv_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_multidv_objs.setOrganization('Trend Micro, Inc.')
class DVIsActive(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

installedDVTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1), )
if mibBuilder.loadTexts: installedDVTable.setStatus('current')
installedDVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1), ).setIndexNames((0, "TPT-MULTIDV-MIB", "installedDVIndex"))
if mibBuilder.loadTexts: installedDVEntry.setStatus('current')
installedDVIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: installedDVIndex.setStatus('current')
installedDVVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedDVVersion.setStatus('current')
installedDVIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 3), DVIsActive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedDVIsActive.setStatus('current')
auxiliaryDVTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2), )
if mibBuilder.loadTexts: auxiliaryDVTable.setStatus('current')
auxiliaryDVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1), ).setIndexNames((0, "TPT-MULTIDV-MIB", "auxiliaryDVIndex"))
if mibBuilder.loadTexts: auxiliaryDVEntry.setStatus('current')
auxiliaryDVIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: auxiliaryDVIndex.setStatus('current')
auxiliaryDVType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVType.setStatus('current')
auxiliaryDVName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVName.setStatus('current')
auxiliaryDVVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVVersion.setStatus('current')
auxiliaryDVPackage = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVPackage.setStatus('current')
mibBuilder.exportSymbols("TPT-MULTIDV-MIB", installedDVTable=installedDVTable, auxiliaryDVName=auxiliaryDVName, tpt_multidv_objs=tpt_multidv_objs, DVIsActive=DVIsActive, installedDVIndex=installedDVIndex, auxiliaryDVVersion=auxiliaryDVVersion, installedDVIsActive=installedDVIsActive, auxiliaryDVPackage=auxiliaryDVPackage, PYSNMP_MODULE_ID=tpt_multidv_objs, auxiliaryDVTable=auxiliaryDVTable, auxiliaryDVEntry=auxiliaryDVEntry, auxiliaryDVIndex=auxiliaryDVIndex, installedDVEntry=installedDVEntry, installedDVVersion=installedDVVersion, auxiliaryDVType=auxiliaryDVType)
