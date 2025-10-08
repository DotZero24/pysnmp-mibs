#
# PySNMP MIB module DLINK-3100-DELETEIMG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINK-3100-DELETEIMG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DELETEIMGName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("image1", 1), ("image2", 2))

rlDeleteImg = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142))
rlDeleteImg.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlDeleteImg.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlDeleteImg.setOrganization('Dlink, Inc.')
rlDeleteImgTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1), )
if mibBuilder.loadTexts: rlDeleteImgTable.setStatus('current')
rlDeleteImgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1), ).setIndexNames((0, "DLINK-3100-DELETEIMG-MIB", "rlDeleteImgKey"))
if mibBuilder.loadTexts: rlDeleteImgEntry.setStatus('current')
rlDeleteImgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: rlDeleteImgKey.setStatus('current')
rlDeleteImgUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgUnit.setStatus('current')
rlDeleteImgName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 3), DELETEIMGName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgName.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-DELETEIMG-MIB", rlDeleteImgUnit=rlDeleteImgUnit, rlDeleteImgName=rlDeleteImgName, DELETEIMGName=DELETEIMGName, rlDeleteImgEntry=rlDeleteImgEntry, PYSNMP_MODULE_ID=rlDeleteImg, rlDeleteImgKey=rlDeleteImgKey, rlDeleteImgTable=rlDeleteImgTable, rlDeleteImg=rlDeleteImg)
