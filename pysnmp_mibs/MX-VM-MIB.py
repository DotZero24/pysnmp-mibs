# SNMP MIB module (MX-VM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-VM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:41 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmMIBObjects_ObjectIdentity = ObjectIdentity
vmMIBObjects = _VmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1)
)
_ConfigGroup_ObjectIdentity = ObjectIdentity
configGroup = _ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100)
)
_VmTable_Object = MibTable
vmTable = _VmTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100)
)
if mibBuilder.loadTexts:
    vmTable.setStatus("current")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1)
)
vmEntry.setIndexNames(
    (0, "MX-VM-MIB", "vmIdx"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("current")


class _VmIdx_Type(Unsigned32):
    """Custom type vmIdx based on Unsigned32"""
    defaultValue = 0


_VmIdx_Type.__name__ = "Unsigned32"
_VmIdx_Object = MibTableColumn
vmIdx = _VmIdx_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 100),
    _VmIdx_Type()
)
vmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIdx.setStatus("current")


class _VmName_Type(OctetString):
    """Custom type vmName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_VmName_Type.__name__ = "OctetString"
_VmName_Object = MibTableColumn
vmName = _VmName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 200),
    _VmName_Type()
)
vmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmName.setStatus("current")


class _VmVncDisplayId_Type(Integer32):
    """Custom type vmVncDisplayId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_VmVncDisplayId_Type.__name__ = "Integer32"
_VmVncDisplayId_Object = MibTableColumn
vmVncDisplayId = _VmVncDisplayId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 300),
    _VmVncDisplayId_Type()
)
vmVncDisplayId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmVncDisplayId.setStatus("current")


class _VmUsbPort_Type(Integer32):
    """Custom type vmUsbPort based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("all", 200))
    )


_VmUsbPort_Type.__name__ = "Integer32"
_VmUsbPort_Object = MibTableColumn
vmUsbPort = _VmUsbPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 400),
    _VmUsbPort_Type()
)
vmUsbPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmUsbPort.setStatus("current")


class _VmIsoName_Type(OctetString):
    """Custom type vmIsoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_VmIsoName_Type.__name__ = "OctetString"
_VmIsoName_Object = MibTableColumn
vmIsoName = _VmIsoName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 500),
    _VmIsoName_Type()
)
vmIsoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmIsoName.setStatus("current")


class _VmMacAddress_Type(OctetString):
    """Custom type vmMacAddress based on OctetString"""
    defaultValue = OctetString("")


_VmMacAddress_Type.__name__ = "OctetString"
_VmMacAddress_Object = MibTableColumn
vmMacAddress = _VmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 550),
    _VmMacAddress_Type()
)
vmMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMacAddress.setStatus("current")


class _VmNetworkAdapter_Type(Integer32):
    """Custom type vmNetworkAdapter based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("e1000", 100),
          ("virtio", 200))
    )


_VmNetworkAdapter_Type.__name__ = "Integer32"
_VmNetworkAdapter_Object = MibTableColumn
vmNetworkAdapter = _VmNetworkAdapter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 560),
    _VmNetworkAdapter_Type()
)
vmNetworkAdapter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmNetworkAdapter.setStatus("current")


class _VmStartupType_Type(Integer32):
    """Custom type vmStartupType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("manual", 100),
          ("auto", 200))
    )


_VmStartupType_Type.__name__ = "Integer32"
_VmStartupType_Object = MibTableColumn
vmStartupType = _VmStartupType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 600),
    _VmStartupType_Type()
)
vmStartupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmStartupType.setStatus("current")


class _VmShutdownTimeout_Type(Unsigned32):
    """Custom type vmShutdownTimeout based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_VmShutdownTimeout_Type.__name__ = "Unsigned32"
_VmShutdownTimeout_Object = MibTableColumn
vmShutdownTimeout = _VmShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 650),
    _VmShutdownTimeout_Type()
)
vmShutdownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmShutdownTimeout.setStatus("current")


class _VmConfigStatus_Type(Integer32):
    """Custom type vmConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("uSBNotAvailable", 200),
          ("missingVMConfig", 300),
          ("needRestartToApplyConfig", 400))
    )


_VmConfigStatus_Type.__name__ = "Integer32"
_VmConfigStatus_Object = MibTableColumn
vmConfigStatus = _VmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 700),
    _VmConfigStatus_Type()
)
vmConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConfigStatus.setStatus("current")


class _VmStart_Type(Integer32):
    """Custom type vmStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("start", 10))
    )


_VmStart_Type.__name__ = "Integer32"
_VmStart_Object = MibTableColumn
vmStart = _VmStart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 10000),
    _VmStart_Type()
)
vmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmStart.setStatus("current")


class _VmStop_Type(Integer32):
    """Custom type vmStop based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("stop", 10))
    )


_VmStop_Type.__name__ = "Integer32"
_VmStop_Object = MibTableColumn
vmStop = _VmStop_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 10010),
    _VmStop_Type()
)
vmStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmStop.setStatus("current")


class _VmReboot_Type(Integer32):
    """Custom type vmReboot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reboot", 10))
    )


_VmReboot_Type.__name__ = "Integer32"
_VmReboot_Object = MibTableColumn
vmReboot = _VmReboot_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 10020),
    _VmReboot_Type()
)
vmReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmReboot.setStatus("current")


class _VmStartFromIsoImage_Type(Integer32):
    """Custom type vmStartFromIsoImage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("startFromIsoImage", 10))
    )


_VmStartFromIsoImage_Type.__name__ = "Integer32"
_VmStartFromIsoImage_Object = MibTableColumn
vmStartFromIsoImage = _VmStartFromIsoImage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 10030),
    _VmStartFromIsoImage_Type()
)
vmStartFromIsoImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmStartFromIsoImage.setStatus("current")


class _VmDelete_Type(Integer32):
    """Custom type vmDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_VmDelete_Type.__name__ = "Integer32"
_VmDelete_Object = MibTableColumn
vmDelete = _VmDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 100, 1, 10040),
    _VmDelete_Type()
)
vmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDelete.setStatus("current")


class _InternalVirtualSwitchEnable_Type(MxEnableState):
    """Custom type internalVirtualSwitchEnable based on MxEnableState"""
    defaultValue = 0


_InternalVirtualSwitchEnable_Type.__name__ = "MxEnableState"
_InternalVirtualSwitchEnable_Object = MibScalar
internalVirtualSwitchEnable = _InternalVirtualSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 200),
    _InternalVirtualSwitchEnable_Type()
)
internalVirtualSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalVirtualSwitchEnable.setStatus("current")


class _InternalVirtualSwitchIpAddr_Type(MxIpAddrMask):
    """Custom type internalVirtualSwitchIpAddr based on MxIpAddrMask"""
    defaultValue = OctetString("169.254.10.1/24")


_InternalVirtualSwitchIpAddr_Type.__name__ = "MxIpAddrMask"
_InternalVirtualSwitchIpAddr_Object = MibScalar
internalVirtualSwitchIpAddr = _InternalVirtualSwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 100, 300),
    _InternalVirtualSwitchIpAddr_Type()
)
internalVirtualSwitchIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalVirtualSwitchIpAddr.setStatus("current")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200)
)
_VmStatusTable_Object = MibTable
vmStatusTable = _VmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200)
)
if mibBuilder.loadTexts:
    vmStatusTable.setStatus("current")
_VmStatusEntry_Object = MibTableRow
vmStatusEntry = _VmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1)
)
vmStatusEntry.setIndexNames(
    (0, "MX-VM-MIB", "vmStatusIdx"),
)
if mibBuilder.loadTexts:
    vmStatusEntry.setStatus("current")
_VmStatusIdx_Type = Unsigned32
_VmStatusIdx_Object = MibTableColumn
vmStatusIdx = _VmStatusIdx_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 100),
    _VmStatusIdx_Type()
)
vmStatusIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusIdx.setStatus("current")
_VmStatusName_Type = OctetString
_VmStatusName_Object = MibTableColumn
vmStatusName = _VmStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 200),
    _VmStatusName_Type()
)
vmStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusName.setStatus("current")
_VmStatusVncDisplayId_Type = Integer32
_VmStatusVncDisplayId_Object = MibTableColumn
vmStatusVncDisplayId = _VmStatusVncDisplayId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 300),
    _VmStatusVncDisplayId_Type()
)
vmStatusVncDisplayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusVncDisplayId.setStatus("current")


class _VmStatusUsbPort_Type(Integer32):
    """Custom type vmStatusUsbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("all", 200))
    )


_VmStatusUsbPort_Type.__name__ = "Integer32"
_VmStatusUsbPort_Object = MibTableColumn
vmStatusUsbPort = _VmStatusUsbPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 400),
    _VmStatusUsbPort_Type()
)
vmStatusUsbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusUsbPort.setStatus("current")
_VmStatusIsoName_Type = OctetString
_VmStatusIsoName_Object = MibTableColumn
vmStatusIsoName = _VmStatusIsoName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 500),
    _VmStatusIsoName_Type()
)
vmStatusIsoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusIsoName.setStatus("current")


class _VmStatusMacAddress_Type(OctetString):
    """Custom type vmStatusMacAddress based on OctetString"""
    defaultValue = OctetString("")


_VmStatusMacAddress_Type.__name__ = "OctetString"
_VmStatusMacAddress_Object = MibTableColumn
vmStatusMacAddress = _VmStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 550),
    _VmStatusMacAddress_Type()
)
vmStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusMacAddress.setStatus("current")


class _VmStatusNetworkAdapter_Type(Integer32):
    """Custom type vmStatusNetworkAdapter based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("e1000", 100),
          ("virtio", 200))
    )


_VmStatusNetworkAdapter_Type.__name__ = "Integer32"
_VmStatusNetworkAdapter_Object = MibTableColumn
vmStatusNetworkAdapter = _VmStatusNetworkAdapter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 560),
    _VmStatusNetworkAdapter_Type()
)
vmStatusNetworkAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusNetworkAdapter.setStatus("current")
_VmStatusAllocatedRamMb_Type = Unsigned32
_VmStatusAllocatedRamMb_Object = MibTableColumn
vmStatusAllocatedRamMb = _VmStatusAllocatedRamMb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 600),
    _VmStatusAllocatedRamMb_Type()
)
vmStatusAllocatedRamMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusAllocatedRamMb.setStatus("current")
_VmStatusAllocatedStorageGb_Type = Unsigned32
_VmStatusAllocatedStorageGb_Object = MibTableColumn
vmStatusAllocatedStorageGb = _VmStatusAllocatedStorageGb_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 700),
    _VmStatusAllocatedStorageGb_Type()
)
vmStatusAllocatedStorageGb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusAllocatedStorageGb.setStatus("current")


class _VmStatusImageFormat_Type(Integer32):
    """Custom type vmStatusImageFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("qcow2", 100),
          ("raw", 200),
          ("unknown", 300))
    )


_VmStatusImageFormat_Type.__name__ = "Integer32"
_VmStatusImageFormat_Object = MibTableColumn
vmStatusImageFormat = _VmStatusImageFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 710),
    _VmStatusImageFormat_Type()
)
vmStatusImageFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusImageFormat.setStatus("current")
_VmStatusAllocatedNbCores_Type = Unsigned32
_VmStatusAllocatedNbCores_Object = MibTableColumn
vmStatusAllocatedNbCores = _VmStatusAllocatedNbCores_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 800),
    _VmStatusAllocatedNbCores_Type()
)
vmStatusAllocatedNbCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusAllocatedNbCores.setStatus("current")


class _VmStatusState_Type(Integer32):
    """Custom type vmStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 100),
          ("started", 200),
          ("starting", 300),
          ("stopping", 400),
          ("invalidConfig", 500))
    )


_VmStatusState_Type.__name__ = "Integer32"
_VmStatusState_Object = MibTableColumn
vmStatusState = _VmStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 200, 1, 900),
    _VmStatusState_Type()
)
vmStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmStatusState.setStatus("current")


class _ConvertVmImageResult_Type(Integer32):
    """Custom type convertVmImageResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("running", 200),
          ("success", 300),
          ("errorNotEnoughSpace", 400))
    )


_ConvertVmImageResult_Type.__name__ = "Integer32"
_ConvertVmImageResult_Object = MibScalar
convertVmImageResult = _ConvertVmImageResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 200, 300),
    _ConvertVmImageResult_Type()
)
convertVmImageResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convertVmImageResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4500, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-VM-MIB",
    **{"vmMIB": vmMIB,
       "vmMIBObjects": vmMIBObjects,
       "configGroup": configGroup,
       "vmTable": vmTable,
       "vmEntry": vmEntry,
       "vmIdx": vmIdx,
       "vmName": vmName,
       "vmVncDisplayId": vmVncDisplayId,
       "vmUsbPort": vmUsbPort,
       "vmIsoName": vmIsoName,
       "vmMacAddress": vmMacAddress,
       "vmNetworkAdapter": vmNetworkAdapter,
       "vmStartupType": vmStartupType,
       "vmShutdownTimeout": vmShutdownTimeout,
       "vmConfigStatus": vmConfigStatus,
       "vmStart": vmStart,
       "vmStop": vmStop,
       "vmReboot": vmReboot,
       "vmStartFromIsoImage": vmStartFromIsoImage,
       "vmDelete": vmDelete,
       "internalVirtualSwitchEnable": internalVirtualSwitchEnable,
       "internalVirtualSwitchIpAddr": internalVirtualSwitchIpAddr,
       "statusGroup": statusGroup,
       "vmStatusTable": vmStatusTable,
       "vmStatusEntry": vmStatusEntry,
       "vmStatusIdx": vmStatusIdx,
       "vmStatusName": vmStatusName,
       "vmStatusVncDisplayId": vmStatusVncDisplayId,
       "vmStatusUsbPort": vmStatusUsbPort,
       "vmStatusIsoName": vmStatusIsoName,
       "vmStatusMacAddress": vmStatusMacAddress,
       "vmStatusNetworkAdapter": vmStatusNetworkAdapter,
       "vmStatusAllocatedRamMb": vmStatusAllocatedRamMb,
       "vmStatusAllocatedStorageGb": vmStatusAllocatedStorageGb,
       "vmStatusImageFormat": vmStatusImageFormat,
       "vmStatusAllocatedNbCores": vmStatusAllocatedNbCores,
       "vmStatusState": vmStatusState,
       "convertVmImageResult": convertVmImageResult,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
