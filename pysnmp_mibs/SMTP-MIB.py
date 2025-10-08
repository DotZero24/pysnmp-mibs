#
# PySNMP MIB module SMTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SMTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:37 2025
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
swSMTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 29))
if mibBuilder.loadTexts: swSMTPMIB.setLastUpdated('0810220000Z')
if mibBuilder.loadTexts: swSMTPMIB.setOrganization('D-Link Corp.')
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

swSMTPCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 1))
swSMTPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 2))
swSMTPMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 3))
smtpStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpStatus.setStatus('current')
smtpSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSrvAddr.setStatus('current')
smtpSrvPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSrvPort.setStatus('current')
smtpSelfMailAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSelfMailAddr.setStatus('current')
smtpTestMsgSubject = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpTestMsgSubject.setStatus('current')
smtpTestMsgContent = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpTestMsgContent.setStatus('current')
smtpSendTestMsg = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send", 1), ("noAction", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSendTestMsg.setStatus('current')
smtpSendTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failed", 2), ("in-processing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtpSendTestStatus.setStatus('current')
smtpMailReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1), )
if mibBuilder.loadTexts: smtpMailReceiverTable.setStatus('current')
smtpReceiverAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1), ).setIndexNames((0, "SMTP-MIB", "smtpMailReceiverAddrIndex"))
if mibBuilder.loadTexts: smtpReceiverAddrEntry.setStatus('current')
smtpMailReceiverAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtpMailReceiverAddrIndex.setStatus('current')
smtpMailReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smtpMailReceiverAddr.setStatus('current')
smtpMailReceiverAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smtpMailReceiverAddrState.setStatus('current')
mibBuilder.exportSymbols("SMTP-MIB", smtpMailReceiverAddrState=smtpMailReceiverAddrState, smtpSendTestStatus=smtpSendTestStatus, smtpMailReceiverTable=smtpMailReceiverTable, smtpSrvAddr=smtpSrvAddr, smtpTestMsgSubject=smtpTestMsgSubject, swSMTPInfo=swSMTPInfo, swSMTPMIB=swSMTPMIB, swSMTPMgmt=swSMTPMgmt, smtpSrvPort=smtpSrvPort, smtpTestMsgContent=smtpTestMsgContent, smtpMailReceiverAddrIndex=smtpMailReceiverAddrIndex, smtpSelfMailAddr=smtpSelfMailAddr, smtpStatus=smtpStatus, MacAddress=MacAddress, PYSNMP_MODULE_ID=swSMTPMIB, swSMTPCtrl=swSMTPCtrl, smtpMailReceiverAddr=smtpMailReceiverAddr, smtpReceiverAddrEntry=smtpReceiverAddrEntry, PortList=PortList, VlanId=VlanId, smtpSendTestMsg=smtpSendTestMsg)
