#
# PySNMP MIB module VM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/VM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAStorageMediaType, = mibBuilder.importSymbols("IANA-STORAGE-MEDIA-TYPE-MIB", "IANAStorageMediaType")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, mib_2, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "mib-2", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "PhysAddress")
UUIDorZero, = mibBuilder.importSymbols("UUID-TC-MIB", "UUIDorZero")
vmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 236))
vmMIB.setRevisions(('2015-10-12 00:00',))
if mibBuilder.loadTexts: vmMIB.setLastUpdated('201510120000Z')
if mibBuilder.loadTexts: vmMIB.setOrganization('IETF Operations and Management Area Working Group')
vmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 0))
vmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 1))
vmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 2))
class VirtualMachineIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VirtualMachineIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class VirtualMachineAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("running", 1), ("suspended", 2), ("paused", 3), ("shutdown", 4))

class VirtualMachineOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("preparing", 3), ("running", 4), ("suspending", 5), ("suspended", 6), ("resuming", 7), ("paused", 8), ("migrating", 9), ("shuttingdown", 10), ("shutdown", 11), ("crashed", 12))

class VirtualMachineAutoStart(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3))

class VirtualMachinePersistent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("persistent", 2), ("transient", 3))

class VirtualMachineCpuIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VirtualMachineStorageIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VirtualMachineStorageSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("block", 3), ("raw", 4), ("sparse", 5), ("network", 6))

class VirtualMachineStorageAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("readwrite", 2), ("readonly", 3))

class VirtualMachineNetworkIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class VirtualMachineList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'

vmHypervisor = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 1, 1))
vmHvSoftware = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmHvSoftware.setStatus('current')
vmHvVersion = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmHvVersion.setStatus('current')
vmHvObjectID = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmHvObjectID.setStatus('current')
vmHvUpTime = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmHvUpTime.setStatus('current')
vmNumber = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmNumber.setStatus('current')
vmTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmTableLastChange.setStatus('current')
vmTable = MibTable((1, 3, 6, 1, 2, 1, 236, 1, 4), )
if mibBuilder.loadTexts: vmTable.setStatus('current')
vmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 236, 1, 4, 1), ).setIndexNames((0, "VM-MIB", "vmIndex"))
if mibBuilder.loadTexts: vmEntry.setStatus('current')
vmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 1), VirtualMachineIndex())
if mibBuilder.loadTexts: vmIndex.setStatus('current')
vmName = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmName.setStatus('current')
vmUUID = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 3), UUIDorZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmUUID.setStatus('current')
vmOSType = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmOSType.setStatus('current')
vmAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 5), VirtualMachineAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmAdminState.setStatus('current')
vmOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 6), VirtualMachineOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmOperState.setStatus('current')
vmAutoStart = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 7), VirtualMachineAutoStart()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmAutoStart.setStatus('current')
vmPersistent = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 8), VirtualMachinePersistent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmPersistent.setStatus('current')
vmCurCpuNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmCurCpuNumber.setStatus('current')
vmMinCpuNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMinCpuNumber.setStatus('current')
vmMaxCpuNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMaxCpuNumber.setStatus('current')
vmMemUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMemUnit.setStatus('current')
vmCurMem = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmCurMem.setStatus('current')
vmMinMem = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMinMem.setStatus('current')
vmMaxMem = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmMaxMem.setStatus('current')
vmUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmUpTime.setStatus('current')
vmCpuTime = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 4, 1, 17), Counter64()).setUnits('microsecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmCpuTime.setStatus('current')
vmCpuTable = MibTable((1, 3, 6, 1, 2, 1, 236, 1, 5), )
if mibBuilder.loadTexts: vmCpuTable.setStatus('current')
vmCpuEntry = MibTableRow((1, 3, 6, 1, 2, 1, 236, 1, 5, 1), ).setIndexNames((0, "VM-MIB", "vmIndex"), (0, "VM-MIB", "vmCpuIndex"))
if mibBuilder.loadTexts: vmCpuEntry.setStatus('current')
vmCpuIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 5, 1, 1), VirtualMachineCpuIndex())
if mibBuilder.loadTexts: vmCpuIndex.setStatus('current')
vmCpuCoreTime = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 5, 1, 2), Counter64()).setUnits('microsecond').setMaxAccess("readonly")
if mibBuilder.loadTexts: vmCpuCoreTime.setStatus('current')
vmCpuAffinityTable = MibTable((1, 3, 6, 1, 2, 1, 236, 1, 6), )
if mibBuilder.loadTexts: vmCpuAffinityTable.setStatus('current')
vmCpuAffinityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 236, 1, 6, 1), ).setIndexNames((0, "VM-MIB", "vmIndex"), (0, "VM-MIB", "vmCpuIndex"), (0, "VM-MIB", "vmCpuPhysIndex"))
if mibBuilder.loadTexts: vmCpuAffinityEntry.setStatus('current')
vmCpuPhysIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vmCpuPhysIndex.setStatus('current')
vmCpuAffinity = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmCpuAffinity.setStatus('current')
vmStorageTable = MibTable((1, 3, 6, 1, 2, 1, 236, 1, 7), )
if mibBuilder.loadTexts: vmStorageTable.setStatus('current')
vmStorageEntry = MibTableRow((1, 3, 6, 1, 2, 1, 236, 1, 7, 1), ).setIndexNames((0, "VM-MIB", "vmStorageVmIndex"), (0, "VM-MIB", "vmStorageIndex"))
if mibBuilder.loadTexts: vmStorageEntry.setStatus('current')
vmStorageVmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 1), VirtualMachineIndexOrZero())
if mibBuilder.loadTexts: vmStorageVmIndex.setStatus('current')
vmStorageIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 2), VirtualMachineStorageIndex())
if mibBuilder.loadTexts: vmStorageIndex.setStatus('current')
vmStorageParent = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageParent.setStatus('current')
vmStorageSourceType = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 4), VirtualMachineStorageSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageSourceType.setStatus('current')
vmStorageSourceTypeString = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageSourceTypeString.setStatus('current')
vmStorageResourceID = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageResourceID.setStatus('current')
vmStorageAccess = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 7), VirtualMachineStorageAccess()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageAccess.setStatus('current')
vmStorageMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 8), IANAStorageMediaType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageMediaType.setStatus('current')
vmStorageMediaTypeString = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageMediaTypeString.setStatus('current')
vmStorageSizeUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageSizeUnit.setStatus('current')
vmStorageDefinedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageDefinedSize.setStatus('current')
vmStorageAllocatedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageAllocatedSize.setStatus('current')
vmStorageReadIOs = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageReadIOs.setStatus('current')
vmStorageWriteIOs = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageWriteIOs.setStatus('current')
vmStorageReadOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageReadOctets.setStatus('current')
vmStorageWriteOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageWriteOctets.setStatus('current')
vmStorageReadLatency = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageReadLatency.setStatus('current')
vmStorageWriteLatency = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 7, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageWriteLatency.setStatus('current')
vmNetworkTable = MibTable((1, 3, 6, 1, 2, 1, 236, 1, 8), )
if mibBuilder.loadTexts: vmNetworkTable.setStatus('current')
vmNetworkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 236, 1, 8, 1), ).setIndexNames((0, "VM-MIB", "vmIndex"), (0, "VM-MIB", "vmNetworkIndex"))
if mibBuilder.loadTexts: vmNetworkEntry.setStatus('current')
vmNetworkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 1), VirtualMachineNetworkIndex())
if mibBuilder.loadTexts: vmNetworkIndex.setStatus('current')
vmNetworkIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmNetworkIfIndex.setStatus('current')
vmNetworkParent = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmNetworkParent.setStatus('current')
vmNetworkModel = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmNetworkModel.setStatus('current')
vmNetworkPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 236, 1, 8, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmNetworkPhysAddress.setStatus('current')
vmPerVMNotificationsEnabled = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmPerVMNotificationsEnabled.setStatus('current')
vmBulkNotificationsEnabled = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmBulkNotificationsEnabled.setStatus('current')
vmAffectedVMs = MibScalar((1, 3, 6, 1, 2, 1, 236, 1, 11), VirtualMachineList()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmAffectedVMs.setStatus('current')
vmRunning = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 1)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmRunning.setStatus('current')
vmShuttingdown = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 2)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmShuttingdown.setStatus('current')
vmShutdown = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 3)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmShutdown.setStatus('current')
vmPaused = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 4)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmPaused.setStatus('current')
vmSuspending = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 5)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmSuspending.setStatus('current')
vmSuspended = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 6)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmSuspended.setStatus('current')
vmResuming = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 7)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmResuming.setStatus('current')
vmMigrating = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 8)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmMigrating.setStatus('current')
vmCrashed = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 9)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"))
if mibBuilder.loadTexts: vmCrashed.setStatus('current')
vmDeleted = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 10)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOperState"), ("VM-MIB", "vmPersistent"))
if mibBuilder.loadTexts: vmDeleted.setStatus('current')
vmBulkRunning = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 11)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkRunning.setStatus('current')
vmBulkShuttingdown = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 12)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkShuttingdown.setStatus('current')
vmBulkShutdown = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 13)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkShutdown.setStatus('current')
vmBulkPaused = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 14)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkPaused.setStatus('current')
vmBulkSuspending = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 15)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkSuspending.setStatus('current')
vmBulkSuspended = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 16)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkSuspended.setStatus('current')
vmBulkResuming = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 17)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkResuming.setStatus('current')
vmBulkMigrating = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 18)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkMigrating.setStatus('current')
vmBulkCrashed = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 19)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkCrashed.setStatus('current')
vmBulkDeleted = NotificationType((1, 3, 6, 1, 2, 1, 236, 0, 20)).setObjects(("VM-MIB", "vmAffectedVMs"))
if mibBuilder.loadTexts: vmBulkDeleted.setStatus('current')
vmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 2, 1))
vmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 236, 2, 2))
vmFullCompliances = ModuleCompliance((1, 3, 6, 1, 2, 1, 236, 2, 1, 1)).setObjects(("VM-MIB", "vmHypervisorGroup"), ("VM-MIB", "vmVirtualMachineGroup"), ("VM-MIB", "vmCpuGroup"), ("VM-MIB", "vmCpuAffinityGroup"), ("VM-MIB", "vmStorageGroup"), ("VM-MIB", "vmNetworkGroup"), ("VM-MIB", "vmPerVMNotificationOptionalGroup"), ("VM-MIB", "vmBulkNotificationsVariablesGroup"), ("VM-MIB", "vmBulkNotificationOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmFullCompliances = vmFullCompliances.setStatus('current')
vmReadOnlyCompliances = ModuleCompliance((1, 3, 6, 1, 2, 1, 236, 2, 1, 2)).setObjects(("VM-MIB", "vmHypervisorGroup"), ("VM-MIB", "vmVirtualMachineGroup"), ("VM-MIB", "vmCpuGroup"), ("VM-MIB", "vmCpuAffinityGroup"), ("VM-MIB", "vmStorageGroup"), ("VM-MIB", "vmNetworkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmReadOnlyCompliances = vmReadOnlyCompliances.setStatus('current')
vmHypervisorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 1)).setObjects(("VM-MIB", "vmHvSoftware"), ("VM-MIB", "vmHvVersion"), ("VM-MIB", "vmHvObjectID"), ("VM-MIB", "vmHvUpTime"), ("VM-MIB", "vmNumber"), ("VM-MIB", "vmTableLastChange"), ("VM-MIB", "vmPerVMNotificationsEnabled"), ("VM-MIB", "vmBulkNotificationsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmHypervisorGroup = vmHypervisorGroup.setStatus('current')
vmVirtualMachineGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 2)).setObjects(("VM-MIB", "vmName"), ("VM-MIB", "vmUUID"), ("VM-MIB", "vmOSType"), ("VM-MIB", "vmAdminState"), ("VM-MIB", "vmOperState"), ("VM-MIB", "vmAutoStart"), ("VM-MIB", "vmPersistent"), ("VM-MIB", "vmCurCpuNumber"), ("VM-MIB", "vmMinCpuNumber"), ("VM-MIB", "vmMaxCpuNumber"), ("VM-MIB", "vmMemUnit"), ("VM-MIB", "vmCurMem"), ("VM-MIB", "vmMinMem"), ("VM-MIB", "vmMaxMem"), ("VM-MIB", "vmUpTime"), ("VM-MIB", "vmCpuTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmVirtualMachineGroup = vmVirtualMachineGroup.setStatus('current')
vmCpuGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 3)).setObjects(("VM-MIB", "vmCpuCoreTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmCpuGroup = vmCpuGroup.setStatus('current')
vmCpuAffinityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 4)).setObjects(("VM-MIB", "vmCpuAffinity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmCpuAffinityGroup = vmCpuAffinityGroup.setStatus('current')
vmStorageGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 5)).setObjects(("VM-MIB", "vmStorageParent"), ("VM-MIB", "vmStorageSourceType"), ("VM-MIB", "vmStorageSourceTypeString"), ("VM-MIB", "vmStorageResourceID"), ("VM-MIB", "vmStorageAccess"), ("VM-MIB", "vmStorageMediaType"), ("VM-MIB", "vmStorageMediaTypeString"), ("VM-MIB", "vmStorageSizeUnit"), ("VM-MIB", "vmStorageDefinedSize"), ("VM-MIB", "vmStorageAllocatedSize"), ("VM-MIB", "vmStorageReadIOs"), ("VM-MIB", "vmStorageWriteIOs"), ("VM-MIB", "vmStorageReadOctets"), ("VM-MIB", "vmStorageWriteOctets"), ("VM-MIB", "vmStorageReadLatency"), ("VM-MIB", "vmStorageWriteLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmStorageGroup = vmStorageGroup.setStatus('current')
vmNetworkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 6)).setObjects(("VM-MIB", "vmNetworkIfIndex"), ("VM-MIB", "vmNetworkParent"), ("VM-MIB", "vmNetworkModel"), ("VM-MIB", "vmNetworkPhysAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmNetworkGroup = vmNetworkGroup.setStatus('current')
vmPerVMNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 7)).setObjects(("VM-MIB", "vmRunning"), ("VM-MIB", "vmShuttingdown"), ("VM-MIB", "vmShutdown"), ("VM-MIB", "vmPaused"), ("VM-MIB", "vmSuspending"), ("VM-MIB", "vmSuspended"), ("VM-MIB", "vmResuming"), ("VM-MIB", "vmMigrating"), ("VM-MIB", "vmCrashed"), ("VM-MIB", "vmDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmPerVMNotificationOptionalGroup = vmPerVMNotificationOptionalGroup.setStatus('current')
vmBulkNotificationsVariablesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 8)).setObjects(("VM-MIB", "vmAffectedVMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmBulkNotificationsVariablesGroup = vmBulkNotificationsVariablesGroup.setStatus('current')
vmBulkNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 236, 2, 2, 9)).setObjects(("VM-MIB", "vmBulkRunning"), ("VM-MIB", "vmBulkShuttingdown"), ("VM-MIB", "vmBulkShutdown"), ("VM-MIB", "vmBulkPaused"), ("VM-MIB", "vmBulkSuspending"), ("VM-MIB", "vmBulkSuspended"), ("VM-MIB", "vmBulkResuming"), ("VM-MIB", "vmBulkMigrating"), ("VM-MIB", "vmBulkCrashed"), ("VM-MIB", "vmBulkDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmBulkNotificationOptionalGroup = vmBulkNotificationOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("VM-MIB", vmStorageSourceTypeString=vmStorageSourceTypeString, vmMIB=vmMIB, vmMaxCpuNumber=vmMaxCpuNumber, vmBulkNotificationsEnabled=vmBulkNotificationsEnabled, vmCompliances=vmCompliances, vmStorageWriteIOs=vmStorageWriteIOs, vmNetworkGroup=vmNetworkGroup, vmNetworkPhysAddress=vmNetworkPhysAddress, PYSNMP_MODULE_ID=vmMIB, VirtualMachineIndex=VirtualMachineIndex, vmAffectedVMs=vmAffectedVMs, vmTable=vmTable, vmMemUnit=vmMemUnit, vmPersistent=vmPersistent, vmStorageAllocatedSize=vmStorageAllocatedSize, vmCpuCoreTime=vmCpuCoreTime, vmName=vmName, vmHypervisorGroup=vmHypervisorGroup, vmCpuIndex=vmCpuIndex, VirtualMachineCpuIndex=VirtualMachineCpuIndex, vmStorageWriteOctets=vmStorageWriteOctets, vmMinMem=vmMinMem, vmStorageGroup=vmStorageGroup, vmCpuTime=vmCpuTime, vmCpuAffinityGroup=vmCpuAffinityGroup, VirtualMachineNetworkIndex=VirtualMachineNetworkIndex, vmCpuAffinityTable=vmCpuAffinityTable, vmStorageMediaType=vmStorageMediaType, vmAutoStart=vmAutoStart, vmStorageReadLatency=vmStorageReadLatency, vmOperState=vmOperState, vmRunning=vmRunning, vmStorageMediaTypeString=vmStorageMediaTypeString, vmStorageIndex=vmStorageIndex, vmBulkMigrating=vmBulkMigrating, VirtualMachinePersistent=VirtualMachinePersistent, vmCurCpuNumber=vmCurCpuNumber, vmStorageSizeUnit=vmStorageSizeUnit, VirtualMachineAdminState=VirtualMachineAdminState, vmBulkNotificationsVariablesGroup=vmBulkNotificationsVariablesGroup, vmStorageReadOctets=vmStorageReadOctets, vmHvObjectID=vmHvObjectID, vmHypervisor=vmHypervisor, vmCpuGroup=vmCpuGroup, vmResuming=vmResuming, vmNumber=vmNumber, vmBulkNotificationOptionalGroup=vmBulkNotificationOptionalGroup, vmMaxMem=vmMaxMem, vmBulkPaused=vmBulkPaused, vmNetworkModel=vmNetworkModel, vmBulkShutdown=vmBulkShutdown, vmBulkDeleted=vmBulkDeleted, vmPerVMNotificationOptionalGroup=vmPerVMNotificationOptionalGroup, vmStorageParent=vmStorageParent, VirtualMachineStorageIndex=VirtualMachineStorageIndex, vmNetworkParent=vmNetworkParent, vmBulkSuspended=vmBulkSuspended, vmIndex=vmIndex, vmSuspended=vmSuspended, vmStorageDefinedSize=vmStorageDefinedSize, vmPerVMNotificationsEnabled=vmPerVMNotificationsEnabled, vmShuttingdown=vmShuttingdown, vmNetworkIfIndex=vmNetworkIfIndex, vmShutdown=vmShutdown, vmObjects=vmObjects, vmBulkShuttingdown=vmBulkShuttingdown, vmStorageWriteLatency=vmStorageWriteLatency, vmSuspending=vmSuspending, vmDeleted=vmDeleted, vmConformance=vmConformance, vmCpuAffinityEntry=vmCpuAffinityEntry, vmBulkRunning=vmBulkRunning, vmNetworkIndex=vmNetworkIndex, VirtualMachineStorageAccess=VirtualMachineStorageAccess, VirtualMachineAutoStart=VirtualMachineAutoStart, vmBulkSuspending=vmBulkSuspending, vmReadOnlyCompliances=vmReadOnlyCompliances, vmCrashed=vmCrashed, vmEntry=vmEntry, vmCpuPhysIndex=vmCpuPhysIndex, vmHvVersion=vmHvVersion, vmCpuEntry=vmCpuEntry, vmHvUpTime=vmHvUpTime, vmNetworkEntry=vmNetworkEntry, vmMinCpuNumber=vmMinCpuNumber, vmStorageAccess=vmStorageAccess, VirtualMachineStorageSourceType=VirtualMachineStorageSourceType, vmStorageTable=vmStorageTable, vmUUID=vmUUID, vmStorageVmIndex=vmStorageVmIndex, vmCurMem=vmCurMem, vmNotifications=vmNotifications, vmTableLastChange=vmTableLastChange, vmNetworkTable=vmNetworkTable, vmBulkResuming=vmBulkResuming, VirtualMachineList=VirtualMachineList, vmCpuTable=vmCpuTable, vmGroups=vmGroups, VirtualMachineIndexOrZero=VirtualMachineIndexOrZero, VirtualMachineOperState=VirtualMachineOperState, vmBulkCrashed=vmBulkCrashed, vmStorageSourceType=vmStorageSourceType, vmMigrating=vmMigrating, vmCpuAffinity=vmCpuAffinity, vmPaused=vmPaused, vmVirtualMachineGroup=vmVirtualMachineGroup, vmFullCompliances=vmFullCompliances, vmStorageReadIOs=vmStorageReadIOs, vmUpTime=vmUpTime, vmAdminState=vmAdminState, vmOSType=vmOSType, vmHvSoftware=vmHvSoftware, vmStorageEntry=vmStorageEntry, vmStorageResourceID=vmStorageResourceID)
