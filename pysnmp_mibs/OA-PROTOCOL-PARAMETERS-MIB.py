#
# PySNMP MIB module OA-PROTOCOL-PARAMETERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OA-PROTOCOL-PARAMETERS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oaProtocolParams = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 1, 42))
oaProtocolParams.setRevisions(('2008-11-24 00:00',))
if mibBuilder.loadTexts: oaProtocolParams.setLastUpdated('200811240000Z')
if mibBuilder.loadTexts: oaProtocolParams.setOrganization('MRV Communications, Inc.')
oaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6926))
oaManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1))
oaSnmpPrtcl = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2))
oaPrtclConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 42, 101))
class EntryValidator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("nothing", 2), ("delete", 3), ("create", 4), ("enable", 5), ("disable", 6))

oaSnmpSecurStrTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2), )
if mibBuilder.loadTexts: oaSnmpSecurStrTable.setStatus('current')
oaSnmpSecurStrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1), ).setIndexNames((0, "OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrName"))
if mibBuilder.loadTexts: oaSnmpSecurStrEntry.setStatus('current')
oaSnmpSecurStrName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 33)))
if mibBuilder.loadTexts: oaSnmpSecurStrName.setStatus('current')
oaSnmpSecurStrAccessPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaSnmpSecurStrAccessPermission.setStatus('current')
oaSnmpSecurStrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 1, 42, 2, 2, 1, 11), EntryValidator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oaSnmpSecurStrAdminStatus.setStatus('current')
oaPrtclMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 1))
oaPrtclMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 2))
oaPrtclMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 1, 1)).setObjects(("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaPrtclMIBCompliance = oaPrtclMIBCompliance.setStatus('current')
oaSnmpSecurStrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 1, 42, 101, 2, 1)).setObjects(("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrAccessPermission"), ("OA-PROTOCOL-PARAMETERS-MIB", "oaSnmpSecurStrAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaSnmpSecurStrGroup = oaSnmpSecurStrGroup.setStatus('current')
mibBuilder.exportSymbols("OA-PROTOCOL-PARAMETERS-MIB", oaSnmpSecurStrTable=oaSnmpSecurStrTable, oaPrtclMIBGroups=oaPrtclMIBGroups, oaManagement=oaManagement, oaPrtclMIBCompliances=oaPrtclMIBCompliances, oaSnmpSecurStrGroup=oaSnmpSecurStrGroup, oaccess=oaccess, oaSnmpSecurStrAdminStatus=oaSnmpSecurStrAdminStatus, oaProtocolParams=oaProtocolParams, oaSnmpSecurStrEntry=oaSnmpSecurStrEntry, oaPrtclConformance=oaPrtclConformance, oaSnmpSecurStrName=oaSnmpSecurStrName, oaSnmpSecurStrAccessPermission=oaSnmpSecurStrAccessPermission, EntryValidator=EntryValidator, oaSnmpPrtcl=oaSnmpPrtcl, oaPrtclMIBCompliance=oaPrtclMIBCompliance, PYSNMP_MODULE_ID=oaProtocolParams)
