#
# PySNMP MIB module RSPAN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/RSPAN-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RSPAN-MGMT-MIB", swRSPANRedirct=swRSPANRedirct, swRSPANRowStatus=swRSPANRowStatus, swRSPANCtrl=swRSPANCtrl, swRSPANCurrentNumEntries=swRSPANCurrentNumEntries, swRSPANVLANID=swRSPANVLANID, swRSPANSourceEgress=swRSPANSourceEgress, swRSPANMaxSupportedEntry=swRSPANMaxSupportedEntry, swRSPANInfo=swRSPANInfo, swRSPANSourceIngress=swRSPANSourceIngress, swRSPANMIB=swRSPANMIB, PortList=PortList, swRSPANMgmt=swRSPANMgmt, swRSPANState=swRSPANState, swRSPANTable=swRSPANTable, swRSPANSrcMirrGroupID=swRSPANSrcMirrGroupID, swRSPANEntry=swRSPANEntry, PYSNMP_MODULE_ID=swRSPANMIB, VlanId=VlanId)
