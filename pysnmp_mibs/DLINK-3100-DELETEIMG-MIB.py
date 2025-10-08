#
# PySNMP MIB module DLINK-3100-DELETEIMG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINK-3100-DELETEIMG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINK-3100-DELETEIMG-MIB", rlDeleteImgName=rlDeleteImgName, rlDeleteImgUnit=rlDeleteImgUnit, rlDeleteImgKey=rlDeleteImgKey, DELETEIMGName=DELETEIMGName, rlDeleteImgEntry=rlDeleteImgEntry, PYSNMP_MODULE_ID=rlDeleteImg, rlDeleteImg=rlDeleteImg, rlDeleteImgTable=rlDeleteImgTable)
