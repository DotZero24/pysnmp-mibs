#
# PySNMP MIB module IBM-FEATURE-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/IBM-FEATURE-ACTIVATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
ibmFeatureActivationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2, 5, 31))
ibmFeatureActivationMIB.setRevisions(('2011-03-30 07:33', '2011-02-02 19:49', '2010-12-08 18:33',))
if mibBuilder.loadTexts: ibmFeatureActivationMIB.setLastUpdated('201103300733Z')
if mibBuilder.loadTexts: ibmFeatureActivationMIB.setOrganization('International Business Machines Corp.')
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmArchitecture = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5))
ibmFodNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 31, 0))
ibmFodObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 31, 1))
ibmFodConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 31, 2))
ibmFodAction = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("installActivationKey", 1), ("uninstallActivationKey", 2), ("exportActivationKey", 3), ("inventoryInstalledActivationKeys", 4))).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmFodAction.setStatus('current')
ibmFodIndex = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmFodIndex.setStatus('current')
ibmFodFileUri = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ibmFodFileUri.setStatus('current')
ibmFodStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("success", 1), ("rebootRequired", 2), ("versionMismatch", 3), ("corruptKeyFile", 4), ("invalideKeyFileTarget", 5), ("keyFileNotPresent", 6), ("communicationFailure", 7), ("keyStoreFull", 8), ("ftpServerFull", 9), ("userAuthenticationFailed", 10), ("invalidIndex", 11), ("protocolNotSupported", 12), ("preRequisiteKeyActionRequired", 13), ("actionIncompleteDeviceBusy", 14), ("fileAlreadyExists", 15), ("permissionProblem", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmFodStatus.setStatus('current')
ibmFodKeyChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ibmFodKeyChangeTime.setStatus('current')
ibmFodKeyOldStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noPreviousStatus", 1), ("keyValid", 2), ("keyInvalid", 3), ("keyValidElsewhere", 4), ("keyFeatureActive", 5), ("keyFeatureRequiresHostReboot", 6), ("keyFeatureRequiresBMCReboot", 7), ("keyExpired", 8), ("keyUseLimitExceeded", 9), ("keyInProcessOfValidation", 10)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ibmFodKeyOldStatus.setStatus('current')
ibmFodKeyNewStatus = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("keyRemoved", 1), ("keyValid", 2), ("keyInvalid", 3), ("keyValidElsewhere", 4), ("keyFeatureActive", 5), ("keyFeatureRequiresHostReboot", 6), ("keyFeatureRequiresBMCReboot", 7), ("keyExpired", 8), ("keyUseLimitExceeded", 9), ("keyInProcessOfValidation", 10), ("keyReplaced", 11)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ibmFodKeyNewStatus.setStatus('current')
ibmFodKeyUpdateData = MibScalar((1, 3, 6, 1, 4, 1, 2, 5, 31, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ibmFodKeyUpdateData.setStatus('current')
ibmFodActivationChangeAlert = NotificationType((1, 3, 6, 1, 4, 1, 2, 5, 31, 0, 1)).setObjects(("IBM-FEATURE-ACTIVATION-MIB", "ibmFodIndex"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyChangeTime"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyOldStatus"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyNewStatus"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyUpdateData"))
if mibBuilder.loadTexts: ibmFodActivationChangeAlert.setStatus('current')
ibmFeatureActivationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 1))
ibmFeatureActivationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2))
ibmFeatureActivationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 1, 1)).setObjects(("IBM-FEATURE-ACTIVATION-MIB", "ibmFeatureActivationBaseGroup"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFeatureActivationNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibmFeatureActivationCompliance = ibmFeatureActivationCompliance.setStatus('current')
ibmFeatureActivationBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2, 1)).setObjects(("IBM-FEATURE-ACTIVATION-MIB", "ibmFodAction"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodIndex"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodFileUri"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodStatus"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyChangeTime"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyOldStatus"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyNewStatus"), ("IBM-FEATURE-ACTIVATION-MIB", "ibmFodKeyUpdateData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibmFeatureActivationBaseGroup = ibmFeatureActivationBaseGroup.setStatus('current')
ibmFeatureActivationNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2, 5, 31, 2, 2, 2)).setObjects(("IBM-FEATURE-ACTIVATION-MIB", "ibmFodActivationChangeAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibmFeatureActivationNotifGroup = ibmFeatureActivationNotifGroup.setStatus('current')
mibBuilder.exportSymbols("IBM-FEATURE-ACTIVATION-MIB", ibmFeatureActivationCompliances=ibmFeatureActivationCompliances, ibmFeatureActivationNotifGroup=ibmFeatureActivationNotifGroup, ibmFodIndex=ibmFodIndex, ibmFodStatus=ibmFodStatus, ibmFodActivationChangeAlert=ibmFodActivationChangeAlert, ibmFeatureActivationBaseGroup=ibmFeatureActivationBaseGroup, ibmFodNotifications=ibmFodNotifications, ibmFodKeyNewStatus=ibmFodKeyNewStatus, ibmFeatureActivationGroups=ibmFeatureActivationGroups, ibm=ibm, ibmFodAction=ibmFodAction, ibmFodObjects=ibmFodObjects, ibmFodKeyChangeTime=ibmFodKeyChangeTime, ibmFeatureActivationCompliance=ibmFeatureActivationCompliance, ibmFodFileUri=ibmFodFileUri, PYSNMP_MODULE_ID=ibmFeatureActivationMIB, ibmFodKeyOldStatus=ibmFodKeyOldStatus, ibmFodKeyUpdateData=ibmFodKeyUpdateData, ibmFodConformance=ibmFodConformance, ibmFeatureActivationMIB=ibmFeatureActivationMIB, ibmArchitecture=ibmArchitecture)
