#
# PySNMP MIB module HP-SWITCH-ERROR-MSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-SWITCH-ERROR-MSG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
hpSwitchErrorMsgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68))
hpSwitchErrorMsgMIB.setRevisions(('2009-04-06 00:00',))
if mibBuilder.loadTexts: hpSwitchErrorMsgMIB.setLastUpdated('200904060000Z')
if mibBuilder.loadTexts: hpSwitchErrorMsgMIB.setOrganization('HP Networking')
hpSwitchErrorMsgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1))
hpSwitchErrorMsgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1), )
if mibBuilder.loadTexts: hpSwitchErrorMsgTable.setStatus('current')
hpSwitchErrorMsgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1), ).setIndexNames((0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityType"), (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityHandle"), (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorSnmpSeqCode"))
if mibBuilder.loadTexts: hpSwitchErrorMsgEntry.setStatus('current')
hpSwitchErrorEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("others", 1), ("cliSession", 2), ("webSession", 3), ("ipV4Address", 4), ("ipV6Address", 5), ("oaApplication", 6))))
if mibBuilder.loadTexts: hpSwitchErrorEntityType.setStatus('current')
hpSwitchErrorEntityHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)))
if mibBuilder.loadTexts: hpSwitchErrorEntityHandle.setStatus('current')
hpSwitchErrorSnmpSeqCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpSwitchErrorSnmpSeqCode.setStatus('current')
hpSwitchErrorTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchErrorTime.setStatus('current')
hpSwitchErrorFailedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchErrorFailedOID.setStatus('current')
hpSwitchEntityErrorMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchEntityErrorMsg.setStatus('current')
hpSwitchSnmpErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchSnmpErrorCode.setStatus('current')
hpSwitchErrorMsgMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2))
hpSwitchErrorMsgMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1))
hpSwitchErrorMsgMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2))
hpSwitchErrorMsgMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1, 1)).setObjects(("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorMsgMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchErrorMsgMIBCompliance = hpSwitchErrorMsgMIBCompliance.setStatus('current')
hpSwitchErrorMsgMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2, 1)).setObjects(("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorTime"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorFailedOID"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchEntityErrorMsg"), ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchSnmpErrorCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchErrorMsgMIBGroup = hpSwitchErrorMsgMIBGroup.setStatus('current')
mibBuilder.exportSymbols("HP-SWITCH-ERROR-MSG-MIB", hpSwitchErrorMsgTable=hpSwitchErrorMsgTable, hpSwitchSnmpErrorCode=hpSwitchSnmpErrorCode, hpSwitchEntityErrorMsg=hpSwitchEntityErrorMsg, hpSwitchErrorMsgMIBGroup=hpSwitchErrorMsgMIBGroup, hpSwitchErrorMsgMIBConformance=hpSwitchErrorMsgMIBConformance, hpSwitchErrorMsgMIBCompliances=hpSwitchErrorMsgMIBCompliances, hpSwitchErrorMsgObjects=hpSwitchErrorMsgObjects, hpSwitchErrorEntityType=hpSwitchErrorEntityType, PYSNMP_MODULE_ID=hpSwitchErrorMsgMIB, hpSwitchErrorEntityHandle=hpSwitchErrorEntityHandle, hpSwitchErrorSnmpSeqCode=hpSwitchErrorSnmpSeqCode, hpSwitchErrorTime=hpSwitchErrorTime, hpSwitchErrorMsgEntry=hpSwitchErrorMsgEntry, hpSwitchErrorMsgMIBCompliance=hpSwitchErrorMsgMIBCompliance, hpSwitchErrorFailedOID=hpSwitchErrorFailedOID, hpSwitchErrorMsgMIB=hpSwitchErrorMsgMIB, hpSwitchErrorMsgMIBGroups=hpSwitchErrorMsgMIBGroups)
