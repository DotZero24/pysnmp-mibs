#
# PySNMP MIB module LUM-FPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-FPU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumFpuMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumFpuMIB")
MgmtNameString, = mibBuilder.importSymbols("LUM-TC", "MgmtNameString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
lumFpuMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 66))
lumFpuMIBModule.setRevisions(('2017-06-15 00:00', '2015-11-30 00:00',))
if mibBuilder.loadTexts: lumFpuMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumFpuMIBModule.setOrganization('Infinera Corporation')
lumFpuConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1))
lumFpuGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1))
lumFpuCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 2))
lumFpuMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2))
fpuGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1))
fpuApplicationList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2))
class FpuWavelengthBand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1310, 1550, 2147483647))
    namedValues = NamedValues(("cwdm1310", 1310), ("dwdm1550", 1550), ("notApplicable", 2147483647))

fpuGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuGeneralConfigLastChangeTime.setStatus('current')
fpuGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuGeneralStateLastChangeTime.setStatus('current')
fpuGeneralFpuApplicationTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuGeneralFpuApplicationTableSize.setStatus('current')
fpuGeneralFpuApplicationConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuGeneralFpuApplicationConfigLastChangeTime.setStatus('current')
fpuGeneralFpuApplicationStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuGeneralFpuApplicationStateLastChangeTime.setStatus('current')
fpuApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1), )
if mibBuilder.loadTexts: fpuApplicationTable.setStatus('current')
fpuApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1), ).setIndexNames((0, "LUM-FPU-MIB", "fpuApplicationIndex"))
if mibBuilder.loadTexts: fpuApplicationEntry.setStatus('current')
fpuApplicationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuApplicationIndex.setStatus('current')
fpuApplicationName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fpuApplicationName.setStatus('current')
fpuApplicationWavelengthBand = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 66, 2, 2, 1, 1, 3), FpuWavelengthBand().clone('dwdm1550')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuApplicationWavelengthBand.setStatus('current')
fpuGeneralGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1, 1)).setObjects(("LUM-FPU-MIB", "fpuGeneralConfigLastChangeTime"), ("LUM-FPU-MIB", "fpuGeneralStateLastChangeTime"), ("LUM-FPU-MIB", "fpuGeneralFpuApplicationTableSize"), ("LUM-FPU-MIB", "fpuGeneralFpuApplicationConfigLastChangeTime"), ("LUM-FPU-MIB", "fpuGeneralFpuApplicationStateLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fpuGeneralGroupV1 = fpuGeneralGroupV1.setStatus('current')
fpuApplicationGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 1, 2)).setObjects(("LUM-FPU-MIB", "fpuApplicationIndex"), ("LUM-FPU-MIB", "fpuApplicationName"), ("LUM-FPU-MIB", "fpuApplicationWavelengthBand"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fpuApplicationGroupV1 = fpuApplicationGroupV1.setStatus('current')
lumFpuComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 66, 1, 2, 1)).setObjects(("LUM-FPU-MIB", "fpuGeneralGroupV1"), ("LUM-FPU-MIB", "fpuApplicationGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumFpuComplV1 = lumFpuComplV1.setStatus('current')
mibBuilder.exportSymbols("LUM-FPU-MIB", fpuApplicationGroupV1=fpuApplicationGroupV1, lumFpuCompl=lumFpuCompl, lumFpuMIBModule=lumFpuMIBModule, fpuGeneralFpuApplicationConfigLastChangeTime=fpuGeneralFpuApplicationConfigLastChangeTime, lumFpuComplV1=lumFpuComplV1, fpuApplicationName=fpuApplicationName, PYSNMP_MODULE_ID=lumFpuMIBModule, fpuGeneralGroupV1=fpuGeneralGroupV1, fpuApplicationWavelengthBand=fpuApplicationWavelengthBand, fpuGeneralConfigLastChangeTime=fpuGeneralConfigLastChangeTime, fpuGeneral=fpuGeneral, lumFpuConfs=lumFpuConfs, fpuGeneralStateLastChangeTime=fpuGeneralStateLastChangeTime, fpuApplicationIndex=fpuApplicationIndex, fpuGeneralFpuApplicationTableSize=fpuGeneralFpuApplicationTableSize, fpuApplicationList=fpuApplicationList, fpuGeneralFpuApplicationStateLastChangeTime=fpuGeneralFpuApplicationStateLastChangeTime, fpuApplicationTable=fpuApplicationTable, FpuWavelengthBand=FpuWavelengthBand, lumFpuMIBObjects=lumFpuMIBObjects, fpuApplicationEntry=fpuApplicationEntry, lumFpuGroups=lumFpuGroups)
