#
# PySNMP MIB module OA-PROTOCOL-PARAMETERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OA-PROTOCOL-PARAMETERS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OA-PROTOCOL-PARAMETERS-MIB", EntryValidator=EntryValidator, oaPrtclConformance=oaPrtclConformance, oaPrtclMIBGroups=oaPrtclMIBGroups, oaSnmpSecurStrName=oaSnmpSecurStrName, oaPrtclMIBCompliances=oaPrtclMIBCompliances, PYSNMP_MODULE_ID=oaProtocolParams, oaManagement=oaManagement, oaSnmpSecurStrEntry=oaSnmpSecurStrEntry, oaSnmpPrtcl=oaSnmpPrtcl, oaSnmpSecurStrTable=oaSnmpSecurStrTable, oaSnmpSecurStrAdminStatus=oaSnmpSecurStrAdminStatus, oaPrtclMIBCompliance=oaPrtclMIBCompliance, oaSnmpSecurStrGroup=oaSnmpSecurStrGroup, oaSnmpSecurStrAccessPermission=oaSnmpSecurStrAccessPermission, oaProtocolParams=oaProtocolParams, oaccess=oaccess)
