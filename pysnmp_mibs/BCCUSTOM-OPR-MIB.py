#
# PySNMP MIB module BCCUSTOM-OPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BCCUSTOM-OPR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fcSwitch, = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcCustomOperation = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52))
bcCustomOperation.setRevisions(('2011-12-19 10:30',))
if mibBuilder.loadTexts: bcCustomOperation.setLastUpdated('200807291830Z')
if mibBuilder.loadTexts: bcCustomOperation.setOrganization('Brocade Communications Systems, Inc.')
hwinfospsaveCmd = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1))
if mibBuilder.loadTexts: hwinfospsaveCmd.setStatus('current')
hwinfospsaveSet = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwinfospsaveSet.setStatus('current')
hwinfospsaveGet = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("success", 0), ("ftperror", 1), ("progressing", 2), ("systemerror", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwinfospsaveGet.setStatus('current')
hwUpdateFilecmd = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2))
if mibBuilder.loadTexts: hwUpdateFilecmd.setStatus('current')
hwUpdateFile = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUpdateFile.setStatus('current')
hwUpdateFileInfo = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUpdateFileInfo.setStatus('current')
hwSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSoftwareVersion.setStatus('current')
mibBuilder.exportSymbols("BCCUSTOM-OPR-MIB", hwinfospsaveGet=hwinfospsaveGet, hwSoftwareVersion=hwSoftwareVersion, hwUpdateFilecmd=hwUpdateFilecmd, hwinfospsaveSet=hwinfospsaveSet, hwinfospsaveCmd=hwinfospsaveCmd, bcCustomOperation=bcCustomOperation, hwUpdateFile=hwUpdateFile, hwUpdateFileInfo=hwUpdateFileInfo, PYSNMP_MODULE_ID=bcCustomOperation)
