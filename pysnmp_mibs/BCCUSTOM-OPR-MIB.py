#
# PySNMP MIB module BCCUSTOM-OPR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BCCUSTOM-OPR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fcSwitch, = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BCCUSTOM-OPR-MIB", hwinfospsaveSet=hwinfospsaveSet, hwUpdateFile=hwUpdateFile, hwinfospsaveGet=hwinfospsaveGet, hwUpdateFilecmd=hwUpdateFilecmd, hwUpdateFileInfo=hwUpdateFileInfo, bcCustomOperation=bcCustomOperation, hwSoftwareVersion=hwSoftwareVersion, PYSNMP_MODULE_ID=bcCustomOperation, hwinfospsaveCmd=hwinfospsaveCmd)
