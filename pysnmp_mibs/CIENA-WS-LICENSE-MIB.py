#
# PySNMP MIB module CIENA-WS-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-LICENSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
StringMaxl64, StringMaxl16, StringMaxl32, StringMaxl128 = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "StringMaxl64", "StringMaxl16", "StringMaxl32", "StringMaxl128")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaWsLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25))
cienaWsLicenseMIB.setRevisions(('2017-07-07 00:00',))
if mibBuilder.loadTexts: cienaWsLicenseMIB.setLastUpdated('201707070000Z')
if mibBuilder.loadTexts: cienaWsLicenseMIB.setOrganization('Ciena Corporation')
class LicenseComplianceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notCompliant", 0), ("compliant", 1))

class LicenseSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preInstall", 0), ("local", 1))

class LicenseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("valid", 0), ("invalid", 1), ("expired", 2))

class LicenseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("trial", 0), ("served", 1))

cwsLicenseClientIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4), )
if mibBuilder.loadTexts: cwsLicenseClientIdTable.setStatus('current')
cwsLicenseClientIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1), ).setIndexNames((0, "CIENA-WS-LICENSE-MIB", "cwsLicenseClientIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsLicenseClientIdEntry.setStatus('current')
cwsLicenseClientIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsLicenseClientIdTableSnmpKey.setStatus('current')
cwsLicenseClientIdRegistrationId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1, 2), StringMaxl64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseClientIdRegistrationId.setStatus('current')
cwsLicenseClientStateTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5), )
if mibBuilder.loadTexts: cwsLicenseClientStateTable.setStatus('current')
cwsLicenseClientStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1), ).setIndexNames((0, "CIENA-WS-LICENSE-MIB", "cwsLicenseClientStateTableSnmpKey"))
if mibBuilder.loadTexts: cwsLicenseClientStateEntry.setStatus('current')
cwsLicenseClientStateTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsLicenseClientStateTableSnmpKey.setStatus('current')
cwsLicenseClientStateComplianceState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1, 2), LicenseComplianceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseClientStateComplianceState.setStatus('current')
cwsLicenseLicenseslistTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7), )
if mibBuilder.loadTexts: cwsLicenseLicenseslistTable.setStatus('current')
cwsLicenseLicenseslistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1), ).setIndexNames((0, "CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistLicenseIndex"))
if mibBuilder.loadTexts: cwsLicenseLicenseslistEntry.setStatus('current')
cwsLicenseLicenseslistLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsLicenseLicenseslistLicenseIndex.setStatus('current')
cwsLicenseLicenseslistName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 2), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistName.setStatus('current')
cwsLicenseLicenseslistDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 3), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistDescription.setStatus('current')
cwsLicenseLicenseslistVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 4), StringMaxl16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistVersion.setStatus('current')
cwsLicenseLicenseslistStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 5), LicenseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistStatus.setStatus('current')
cwsLicenseLicenseslistSource = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 6), LicenseSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistSource.setStatus('current')
cwsLicenseLicenseslistIssuerName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 7), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistIssuerName.setStatus('current')
cwsLicenseLicenseslistIssuedDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 8), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistIssuedDate.setStatus('current')
cwsLicenseLicenseslistType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 9), LicenseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistType.setStatus('current')
cwsLicenseLicenseslistHostId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 10), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistHostId.setStatus('current')
cwsLicenseLicenseslistCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 11), StringMaxl16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistCount.setStatus('current')
cwsLicenseLicenseslistCheckedOutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 12), StringMaxl16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistCheckedOutCount.setStatus('current')
cwsLicenseLicenseslistExpiryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 13), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistExpiryDate.setStatus('current')
cwsLicenseLicenseslistNotice = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 14), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseLicenseslistNotice.setStatus('current')
cwsLicenseServerTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8), )
if mibBuilder.loadTexts: cwsLicenseServerTable.setStatus('current')
cwsLicenseServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1), ).setIndexNames((0, "CIENA-WS-LICENSE-MIB", "cwsLicenseServerTableSnmpKey"))
if mibBuilder.loadTexts: cwsLicenseServerEntry.setStatus('current')
cwsLicenseServerTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsLicenseServerTableSnmpKey.setStatus('current')
cwsLicenseServerHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsLicenseServerHostAddress.setStatus('current')
cwsLicenseServerNumLicenseServers = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsLicenseServerNumLicenseServers.setStatus('current')
cienaWsLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 1))
cienaWsLicenseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2))
cienaWsLicenseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 1))
cienaWsLicenseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 1, 1)).setObjects(("CIENA-WS-LICENSE-MIB", "cwsLicenseClientIdRegistrationId"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseClientStateComplianceState"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistName"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistDescription"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistVersion"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistStatus"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistSource"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistIssuerName"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistIssuedDate"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistType"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistHostId"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistCount"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistCheckedOutCount"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistExpiryDate"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistNotice"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseServerHostAddress"), ("CIENA-WS-LICENSE-MIB", "cwsLicenseServerNumLicenseServers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsLicenseGroup = cienaWsLicenseGroup.setStatus('current')
cienaWsLicenseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 2))
cienaWsLicenseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 2, 1)).setObjects(("CIENA-WS-LICENSE-MIB", "cienaWsLicenseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsLicenseCompliance = cienaWsLicenseCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-LICENSE-MIB", cienaWsLicenseCompliances=cienaWsLicenseCompliances, LicenseType=LicenseType, cwsLicenseLicenseslistStatus=cwsLicenseLicenseslistStatus, cienaWsLicenseMIB=cienaWsLicenseMIB, cwsLicenseLicenseslistVersion=cwsLicenseLicenseslistVersion, cwsLicenseLicenseslistCount=cwsLicenseLicenseslistCount, cwsLicenseClientStateComplianceState=cwsLicenseClientStateComplianceState, LicenseSource=LicenseSource, cienaWsLicenseConformance=cienaWsLicenseConformance, cwsLicenseLicenseslistName=cwsLicenseLicenseslistName, cwsLicenseServerHostAddress=cwsLicenseServerHostAddress, cwsLicenseLicenseslistSource=cwsLicenseLicenseslistSource, cwsLicenseLicenseslistType=cwsLicenseLicenseslistType, cwsLicenseServerEntry=cwsLicenseServerEntry, LicenseComplianceState=LicenseComplianceState, cwsLicenseClientIdRegistrationId=cwsLicenseClientIdRegistrationId, cwsLicenseClientStateTableSnmpKey=cwsLicenseClientStateTableSnmpKey, LicenseStatus=LicenseStatus, cwsLicenseLicenseslistCheckedOutCount=cwsLicenseLicenseslistCheckedOutCount, cienaWsLicenseCompliance=cienaWsLicenseCompliance, cwsLicenseLicenseslistExpiryDate=cwsLicenseLicenseslistExpiryDate, cwsLicenseServerTable=cwsLicenseServerTable, cwsLicenseServerNumLicenseServers=cwsLicenseServerNumLicenseServers, cwsLicenseClientIdTableSnmpKey=cwsLicenseClientIdTableSnmpKey, cwsLicenseLicenseslistTable=cwsLicenseLicenseslistTable, cwsLicenseLicenseslistEntry=cwsLicenseLicenseslistEntry, cwsLicenseLicenseslistDescription=cwsLicenseLicenseslistDescription, cwsLicenseLicenseslistLicenseIndex=cwsLicenseLicenseslistLicenseIndex, cienaWsLicenseObjects=cienaWsLicenseObjects, cwsLicenseLicenseslistIssuerName=cwsLicenseLicenseslistIssuerName, cwsLicenseLicenseslistHostId=cwsLicenseLicenseslistHostId, PYSNMP_MODULE_ID=cienaWsLicenseMIB, cwsLicenseServerTableSnmpKey=cwsLicenseServerTableSnmpKey, cienaWsLicenseGroup=cienaWsLicenseGroup, cwsLicenseClientStateEntry=cwsLicenseClientStateEntry, cwsLicenseClientIdEntry=cwsLicenseClientIdEntry, cwsLicenseClientIdTable=cwsLicenseClientIdTable, cienaWsLicenseGroups=cienaWsLicenseGroups, cwsLicenseLicenseslistIssuedDate=cwsLicenseLicenseslistIssuedDate, cwsLicenseClientStateTable=cwsLicenseClientStateTable, cwsLicenseLicenseslistNotice=cwsLicenseLicenseslistNotice)
