#
# PySNMP MIB module RSPAN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/RSPAN-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swRSPANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 68))
if mibBuilder.loadTexts: swRSPANMIB.setLastUpdated('200903100000Z')
if mibBuilder.loadTexts: swRSPANMIB.setOrganization('D-Link Crop.')
swRSPANCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 1))
swRSPANInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 2))
swRSPANMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 3))
swRSPANState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRSPANState.setStatus('current')
swRSPANMaxSupportedEntry = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANMaxSupportedEntry.setStatus('current')
swRSPANCurrentNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANCurrentNumEntries.setStatus('current')
swRSPANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1), )
if mibBuilder.loadTexts: swRSPANTable.setStatus('current')
swRSPANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1), ).setIndexNames((0, "RSPAN-MGMT-MIB", "swRSPANVLANID"))
if mibBuilder.loadTexts: swRSPANEntry.setStatus('current')
swRSPANVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANVLANID.setStatus('current')
swRSPANSourceIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 2), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANSourceIngress.setStatus('current')
swRSPANSourceEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANSourceEgress.setStatus('current')
swRSPANRedirct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANRedirct.setStatus('current')
swRSPANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANRowStatus.setStatus('current')
swRSPANSrcMirrGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANSrcMirrGroupID.setStatus('current')
mibBuilder.exportSymbols("RSPAN-MGMT-MIB", swRSPANInfo=swRSPANInfo, swRSPANCurrentNumEntries=swRSPANCurrentNumEntries, swRSPANRedirct=swRSPANRedirct, swRSPANRowStatus=swRSPANRowStatus, swRSPANSourceIngress=swRSPANSourceIngress, swRSPANMIB=swRSPANMIB, swRSPANEntry=swRSPANEntry, swRSPANSourceEgress=swRSPANSourceEgress, swRSPANCtrl=swRSPANCtrl, swRSPANState=swRSPANState, PortList=PortList, swRSPANMgmt=swRSPANMgmt, PYSNMP_MODULE_ID=swRSPANMIB, VlanId=VlanId, swRSPANTable=swRSPANTable, swRSPANSrcMirrGroupID=swRSPANSrcMirrGroupID, swRSPANMaxSupportedEntry=swRSPANMaxSupportedEntry, swRSPANVLANID=swRSPANVLANID)
