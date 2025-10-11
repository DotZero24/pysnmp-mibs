# SNMP MIB module (MX-EPSERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-EPSERV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:13 2025
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

epServMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EpServMIBObjects_ObjectIdentity = ObjectIdentity
epServMIBObjects = _EpServMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1)
)
_CallGroup_ObjectIdentity = ObjectIdentity
callGroup = _CallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100)
)


class _DefaultCallHookFlashProcessing_Type(Integer32):
    """Custom type defaultCallHookFlashProcessing based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("processLocally", 100),
          ("transmitUsingSignalingProtocol", 200))
    )


_DefaultCallHookFlashProcessing_Type.__name__ = "Integer32"
_DefaultCallHookFlashProcessing_Object = MibScalar
defaultCallHookFlashProcessing = _DefaultCallHookFlashProcessing_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 200),
    _DefaultCallHookFlashProcessing_Type()
)
defaultCallHookFlashProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallHookFlashProcessing.setStatus("current")


class _DefaultCallAllowDirectIp_Type(MxEnableState):
    """Custom type defaultCallAllowDirectIp based on MxEnableState"""
    defaultValue = 0


_DefaultCallAllowDirectIp_Type.__name__ = "MxEnableState"
_DefaultCallAllowDirectIp_Object = MibScalar
defaultCallAllowDirectIp = _DefaultCallAllowDirectIp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 300),
    _DefaultCallAllowDirectIp_Type()
)
defaultCallAllowDirectIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallAllowDirectIp.setStatus("current")
_EpSpecificCallTable_Object = MibTable
epSpecificCallTable = _EpSpecificCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 400)
)
if mibBuilder.loadTexts:
    epSpecificCallTable.setStatus("current")
_EpSpecificCallEntry_Object = MibTableRow
epSpecificCallEntry = _EpSpecificCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 400, 1)
)
epSpecificCallEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificCallEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCallEntry.setStatus("current")
_EpSpecificCallEpId_Type = OctetString
_EpSpecificCallEpId_Object = MibTableColumn
epSpecificCallEpId = _EpSpecificCallEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 400, 1, 100),
    _EpSpecificCallEpId_Type()
)
epSpecificCallEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCallEpId.setStatus("current")


class _EpSpecificCallEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCallEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCallEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCallEnableConfig_Object = MibTableColumn
epSpecificCallEnableConfig = _EpSpecificCallEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 400, 1, 200),
    _EpSpecificCallEnableConfig_Type()
)
epSpecificCallEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallEnableConfig.setStatus("current")


class _EpSpecificCallHookFlashProcessing_Type(Integer32):
    """Custom type epSpecificCallHookFlashProcessing based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("processLocally", 100),
          ("transmitUsingSignalingProtocol", 200))
    )


_EpSpecificCallHookFlashProcessing_Type.__name__ = "Integer32"
_EpSpecificCallHookFlashProcessing_Object = MibTableColumn
epSpecificCallHookFlashProcessing = _EpSpecificCallHookFlashProcessing_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 400, 1, 400),
    _EpSpecificCallHookFlashProcessing_Type()
)
epSpecificCallHookFlashProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallHookFlashProcessing.setStatus("current")
_CallDtmfMapGroup_ObjectIdentity = ObjectIdentity
callDtmfMapGroup = _CallDtmfMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500)
)
_CallDtmfMapAllowedTable_Object = MibTable
callDtmfMapAllowedTable = _CallDtmfMapAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100)
)
if mibBuilder.loadTexts:
    callDtmfMapAllowedTable.setStatus("current")
_CallDtmfMapAllowedEntry_Object = MibTableRow
callDtmfMapAllowedEntry = _CallDtmfMapAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1)
)
callDtmfMapAllowedEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callDtmfMapAllowedIndex"),
)
if mibBuilder.loadTexts:
    callDtmfMapAllowedEntry.setStatus("current")


class _CallDtmfMapAllowedIndex_Type(Unsigned32):
    """Custom type callDtmfMapAllowedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CallDtmfMapAllowedIndex_Type.__name__ = "Unsigned32"
_CallDtmfMapAllowedIndex_Object = MibTableColumn
callDtmfMapAllowedIndex = _CallDtmfMapAllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 100),
    _CallDtmfMapAllowedIndex_Type()
)
callDtmfMapAllowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDtmfMapAllowedIndex.setStatus("current")


class _CallDtmfMapAllowedEnable_Type(MxEnableState):
    """Custom type callDtmfMapAllowedEnable based on MxEnableState"""
    defaultValue = 1


_CallDtmfMapAllowedEnable_Type.__name__ = "MxEnableState"
_CallDtmfMapAllowedEnable_Object = MibTableColumn
callDtmfMapAllowedEnable = _CallDtmfMapAllowedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 200),
    _CallDtmfMapAllowedEnable_Type()
)
callDtmfMapAllowedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedEnable.setStatus("current")


class _CallDtmfMapAllowedApplyTo_Type(Integer32):
    """Custom type callDtmfMapAllowedApplyTo based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unit", 100),
          ("endpoint", 200))
    )


_CallDtmfMapAllowedApplyTo_Type.__name__ = "Integer32"
_CallDtmfMapAllowedApplyTo_Object = MibTableColumn
callDtmfMapAllowedApplyTo = _CallDtmfMapAllowedApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 300),
    _CallDtmfMapAllowedApplyTo_Type()
)
callDtmfMapAllowedApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedApplyTo.setStatus("current")


class _CallDtmfMapAllowedEpId_Type(OctetString):
    """Custom type callDtmfMapAllowedEpId based on OctetString"""
    defaultValue = OctetString("")


_CallDtmfMapAllowedEpId_Type.__name__ = "OctetString"
_CallDtmfMapAllowedEpId_Object = MibTableColumn
callDtmfMapAllowedEpId = _CallDtmfMapAllowedEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 400),
    _CallDtmfMapAllowedEpId_Type()
)
callDtmfMapAllowedEpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedEpId.setStatus("current")


class _CallDtmfMapAllowedDtmfMap_Type(MxDigitMap):
    """Custom type callDtmfMapAllowedDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("x.T")


_CallDtmfMapAllowedDtmfMap_Type.__name__ = "MxDigitMap"
_CallDtmfMapAllowedDtmfMap_Object = MibTableColumn
callDtmfMapAllowedDtmfMap = _CallDtmfMapAllowedDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 500),
    _CallDtmfMapAllowedDtmfMap_Type()
)
callDtmfMapAllowedDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedDtmfMap.setStatus("current")


class _CallDtmfMapAllowedDtmfTransformation_Type(OctetString):
    """Custom type callDtmfMapAllowedDtmfTransformation based on OctetString"""
    defaultValue = OctetString("x")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CallDtmfMapAllowedDtmfTransformation_Type.__name__ = "OctetString"
_CallDtmfMapAllowedDtmfTransformation_Object = MibTableColumn
callDtmfMapAllowedDtmfTransformation = _CallDtmfMapAllowedDtmfTransformation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 600),
    _CallDtmfMapAllowedDtmfTransformation_Type()
)
callDtmfMapAllowedDtmfTransformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedDtmfTransformation.setStatus("current")


class _CallDtmfMapAllowedTargetHost_Type(MxIpHostNamePort):
    """Custom type callDtmfMapAllowedTargetHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_CallDtmfMapAllowedTargetHost_Type.__name__ = "MxIpHostNamePort"
_CallDtmfMapAllowedTargetHost_Object = MibTableColumn
callDtmfMapAllowedTargetHost = _CallDtmfMapAllowedTargetHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 700),
    _CallDtmfMapAllowedTargetHost_Type()
)
callDtmfMapAllowedTargetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedTargetHost.setStatus("current")


class _CallDtmfMapAllowedEmergency_Type(MxEnableState):
    """Custom type callDtmfMapAllowedEmergency based on MxEnableState"""
    defaultValue = 0


_CallDtmfMapAllowedEmergency_Type.__name__ = "MxEnableState"
_CallDtmfMapAllowedEmergency_Object = MibTableColumn
callDtmfMapAllowedEmergency = _CallDtmfMapAllowedEmergency_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 100, 1, 800),
    _CallDtmfMapAllowedEmergency_Type()
)
callDtmfMapAllowedEmergency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapAllowedEmergency.setStatus("current")
_CallDtmfMapRefuseTable_Object = MibTable
callDtmfMapRefuseTable = _CallDtmfMapRefuseTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200)
)
if mibBuilder.loadTexts:
    callDtmfMapRefuseTable.setStatus("current")
_CallDtmfMapRefuseEntry_Object = MibTableRow
callDtmfMapRefuseEntry = _CallDtmfMapRefuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1)
)
callDtmfMapRefuseEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callDtmfMapRefuseIndex"),
)
if mibBuilder.loadTexts:
    callDtmfMapRefuseEntry.setStatus("current")


class _CallDtmfMapRefuseIndex_Type(Unsigned32):
    """Custom type callDtmfMapRefuseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CallDtmfMapRefuseIndex_Type.__name__ = "Unsigned32"
_CallDtmfMapRefuseIndex_Object = MibTableColumn
callDtmfMapRefuseIndex = _CallDtmfMapRefuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1, 100),
    _CallDtmfMapRefuseIndex_Type()
)
callDtmfMapRefuseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDtmfMapRefuseIndex.setStatus("current")


class _CallDtmfMapRefuseEnable_Type(MxEnableState):
    """Custom type callDtmfMapRefuseEnable based on MxEnableState"""
    defaultValue = 0


_CallDtmfMapRefuseEnable_Type.__name__ = "MxEnableState"
_CallDtmfMapRefuseEnable_Object = MibTableColumn
callDtmfMapRefuseEnable = _CallDtmfMapRefuseEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1, 200),
    _CallDtmfMapRefuseEnable_Type()
)
callDtmfMapRefuseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapRefuseEnable.setStatus("current")


class _CallDtmfMapRefuseApplyTo_Type(Integer32):
    """Custom type callDtmfMapRefuseApplyTo based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unit", 100),
          ("endpoint", 200))
    )


_CallDtmfMapRefuseApplyTo_Type.__name__ = "Integer32"
_CallDtmfMapRefuseApplyTo_Object = MibTableColumn
callDtmfMapRefuseApplyTo = _CallDtmfMapRefuseApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1, 300),
    _CallDtmfMapRefuseApplyTo_Type()
)
callDtmfMapRefuseApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapRefuseApplyTo.setStatus("current")


class _CallDtmfMapRefuseEpId_Type(OctetString):
    """Custom type callDtmfMapRefuseEpId based on OctetString"""
    defaultValue = OctetString("")


_CallDtmfMapRefuseEpId_Type.__name__ = "OctetString"
_CallDtmfMapRefuseEpId_Object = MibTableColumn
callDtmfMapRefuseEpId = _CallDtmfMapRefuseEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1, 400),
    _CallDtmfMapRefuseEpId_Type()
)
callDtmfMapRefuseEpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapRefuseEpId.setStatus("current")


class _CallDtmfMapRefuseDtmfMap_Type(MxDigitMap):
    """Custom type callDtmfMapRefuseDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("")


_CallDtmfMapRefuseDtmfMap_Type.__name__ = "MxDigitMap"
_CallDtmfMapRefuseDtmfMap_Object = MibTableColumn
callDtmfMapRefuseDtmfMap = _CallDtmfMapRefuseDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 100, 500, 200, 1, 500),
    _CallDtmfMapRefuseDtmfMap_Type()
)
callDtmfMapRefuseDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callDtmfMapRefuseDtmfMap.setStatus("current")
_AutoCallGroup_ObjectIdentity = ObjectIdentity
autoCallGroup = _AutoCallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200)
)


class _DefaultAutoCallEnable_Type(MxEnableState):
    """Custom type defaultAutoCallEnable based on MxEnableState"""
    defaultValue = 0


_DefaultAutoCallEnable_Type.__name__ = "MxEnableState"
_DefaultAutoCallEnable_Object = MibScalar
defaultAutoCallEnable = _DefaultAutoCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 100),
    _DefaultAutoCallEnable_Type()
)
defaultAutoCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultAutoCallEnable.setStatus("current")


class _DefaultAutoCallTargetAddress_Type(OctetString):
    """Custom type defaultAutoCallTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DefaultAutoCallTargetAddress_Type.__name__ = "OctetString"
_DefaultAutoCallTargetAddress_Object = MibScalar
defaultAutoCallTargetAddress = _DefaultAutoCallTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 200),
    _DefaultAutoCallTargetAddress_Type()
)
defaultAutoCallTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultAutoCallTargetAddress.setStatus("current")
_EpSpecificAutoCallTable_Object = MibTable
epSpecificAutoCallTable = _EpSpecificAutoCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300)
)
if mibBuilder.loadTexts:
    epSpecificAutoCallTable.setStatus("current")
_EpSpecificAutoCallEntry_Object = MibTableRow
epSpecificAutoCallEntry = _EpSpecificAutoCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300, 1)
)
epSpecificAutoCallEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificAutoCallEpId"),
)
if mibBuilder.loadTexts:
    epSpecificAutoCallEntry.setStatus("current")
_EpSpecificAutoCallEpId_Type = OctetString
_EpSpecificAutoCallEpId_Object = MibTableColumn
epSpecificAutoCallEpId = _EpSpecificAutoCallEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300, 1, 100),
    _EpSpecificAutoCallEpId_Type()
)
epSpecificAutoCallEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificAutoCallEpId.setStatus("current")


class _EpSpecificAutoCallEnableConfig_Type(MxEnableState):
    """Custom type epSpecificAutoCallEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificAutoCallEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificAutoCallEnableConfig_Object = MibTableColumn
epSpecificAutoCallEnableConfig = _EpSpecificAutoCallEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300, 1, 200),
    _EpSpecificAutoCallEnableConfig_Type()
)
epSpecificAutoCallEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificAutoCallEnableConfig.setStatus("current")


class _EpSpecificAutoCallEnable_Type(MxEnableState):
    """Custom type epSpecificAutoCallEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificAutoCallEnable_Type.__name__ = "MxEnableState"
_EpSpecificAutoCallEnable_Object = MibTableColumn
epSpecificAutoCallEnable = _EpSpecificAutoCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300, 1, 300),
    _EpSpecificAutoCallEnable_Type()
)
epSpecificAutoCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificAutoCallEnable.setStatus("current")


class _EpSpecificAutoCallTargetAddress_Type(OctetString):
    """Custom type epSpecificAutoCallTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EpSpecificAutoCallTargetAddress_Type.__name__ = "OctetString"
_EpSpecificAutoCallTargetAddress_Object = MibTableColumn
epSpecificAutoCallTargetAddress = _EpSpecificAutoCallTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 200, 300, 1, 400),
    _EpSpecificAutoCallTargetAddress_Type()
)
epSpecificAutoCallTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificAutoCallTargetAddress.setStatus("current")
_HoldGroup_ObjectIdentity = ObjectIdentity
holdGroup = _HoldGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300)
)


class _DefaultHoldEnable_Type(MxEnableState):
    """Custom type defaultHoldEnable based on MxEnableState"""
    defaultValue = 1


_DefaultHoldEnable_Type.__name__ = "MxEnableState"
_DefaultHoldEnable_Object = MibScalar
defaultHoldEnable = _DefaultHoldEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 100),
    _DefaultHoldEnable_Type()
)
defaultHoldEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultHoldEnable.setStatus("current")
_EpSpecificHoldTable_Object = MibTable
epSpecificHoldTable = _EpSpecificHoldTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 200)
)
if mibBuilder.loadTexts:
    epSpecificHoldTable.setStatus("current")
_EpSpecificHoldEntry_Object = MibTableRow
epSpecificHoldEntry = _EpSpecificHoldEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 200, 1)
)
epSpecificHoldEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificHoldEpId"),
)
if mibBuilder.loadTexts:
    epSpecificHoldEntry.setStatus("current")
_EpSpecificHoldEpId_Type = OctetString
_EpSpecificHoldEpId_Object = MibTableColumn
epSpecificHoldEpId = _EpSpecificHoldEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 200, 1, 100),
    _EpSpecificHoldEpId_Type()
)
epSpecificHoldEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificHoldEpId.setStatus("current")


class _EpSpecificHoldEnableConfig_Type(MxEnableState):
    """Custom type epSpecificHoldEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificHoldEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificHoldEnableConfig_Object = MibTableColumn
epSpecificHoldEnableConfig = _EpSpecificHoldEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 200, 1, 200),
    _EpSpecificHoldEnableConfig_Type()
)
epSpecificHoldEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificHoldEnableConfig.setStatus("current")


class _EpSpecificHoldEnable_Type(MxEnableState):
    """Custom type epSpecificHoldEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificHoldEnable_Type.__name__ = "MxEnableState"
_EpSpecificHoldEnable_Object = MibTableColumn
epSpecificHoldEnable = _EpSpecificHoldEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 200, 1, 300),
    _EpSpecificHoldEnable_Type()
)
epSpecificHoldEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificHoldEnable.setStatus("current")
_HoldStatusTable_Object = MibTable
holdStatusTable = _HoldStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 300)
)
if mibBuilder.loadTexts:
    holdStatusTable.setStatus("current")
_HoldStatusEntry_Object = MibTableRow
holdStatusEntry = _HoldStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 300, 1)
)
holdStatusEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "holdStatusEpId"),
)
if mibBuilder.loadTexts:
    holdStatusEntry.setStatus("current")
_HoldStatusEpId_Type = OctetString
_HoldStatusEpId_Object = MibTableColumn
holdStatusEpId = _HoldStatusEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 300, 1, 100),
    _HoldStatusEpId_Type()
)
holdStatusEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    holdStatusEpId.setStatus("current")
_HoldStatusState_Type = MxActivationState
_HoldStatusState_Object = MibTableColumn
holdStatusState = _HoldStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 300, 300, 1, 200),
    _HoldStatusState_Type()
)
holdStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    holdStatusState.setStatus("current")
_CallWaitingGroup_ObjectIdentity = ObjectIdentity
callWaitingGroup = _CallWaitingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400)
)


class _DefaultCallWaitingEnable_Type(MxEnableState):
    """Custom type defaultCallWaitingEnable based on MxEnableState"""
    defaultValue = 1


_DefaultCallWaitingEnable_Type.__name__ = "MxEnableState"
_DefaultCallWaitingEnable_Object = MibScalar
defaultCallWaitingEnable = _DefaultCallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 100),
    _DefaultCallWaitingEnable_Type()
)
defaultCallWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallWaitingEnable.setStatus("current")


class _DefaultCallWaitingCancelDtmfMap_Type(MxDigitMap):
    """Custom type defaultCallWaitingCancelDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallWaitingCancelDtmfMap_Type.__name__ = "MxDigitMap"
_DefaultCallWaitingCancelDtmfMap_Object = MibScalar
defaultCallWaitingCancelDtmfMap = _DefaultCallWaitingCancelDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 200),
    _DefaultCallWaitingCancelDtmfMap_Type()
)
defaultCallWaitingCancelDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallWaitingCancelDtmfMap.setStatus("current")


class _DefaultCallWaitingActivationDtmfMap_Type(MxDigitMap):
    """Custom type defaultCallWaitingActivationDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallWaitingActivationDtmfMap_Type.__name__ = "MxDigitMap"
_DefaultCallWaitingActivationDtmfMap_Object = MibScalar
defaultCallWaitingActivationDtmfMap = _DefaultCallWaitingActivationDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 210),
    _DefaultCallWaitingActivationDtmfMap_Type()
)
defaultCallWaitingActivationDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallWaitingActivationDtmfMap.setStatus("current")


class _DefaultCallWaitingDeactivationDtmfMap_Type(MxDigitMap):
    """Custom type defaultCallWaitingDeactivationDtmfMap based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallWaitingDeactivationDtmfMap_Type.__name__ = "MxDigitMap"
_DefaultCallWaitingDeactivationDtmfMap_Object = MibScalar
defaultCallWaitingDeactivationDtmfMap = _DefaultCallWaitingDeactivationDtmfMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 220),
    _DefaultCallWaitingDeactivationDtmfMap_Type()
)
defaultCallWaitingDeactivationDtmfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallWaitingDeactivationDtmfMap.setStatus("current")
_EpSpecificCallWaitingTable_Object = MibTable
epSpecificCallWaitingTable = _EpSpecificCallWaitingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 300)
)
if mibBuilder.loadTexts:
    epSpecificCallWaitingTable.setStatus("current")
_EpSpecificCallWaitingEntry_Object = MibTableRow
epSpecificCallWaitingEntry = _EpSpecificCallWaitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 300, 1)
)
epSpecificCallWaitingEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificCallWaitingEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCallWaitingEntry.setStatus("current")
_EpSpecificCallWaitingEpId_Type = OctetString
_EpSpecificCallWaitingEpId_Object = MibTableColumn
epSpecificCallWaitingEpId = _EpSpecificCallWaitingEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 300, 1, 100),
    _EpSpecificCallWaitingEpId_Type()
)
epSpecificCallWaitingEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCallWaitingEpId.setStatus("current")


class _EpSpecificCallWaitingEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCallWaitingEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCallWaitingEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCallWaitingEnableConfig_Object = MibTableColumn
epSpecificCallWaitingEnableConfig = _EpSpecificCallWaitingEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 300, 1, 200),
    _EpSpecificCallWaitingEnableConfig_Type()
)
epSpecificCallWaitingEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallWaitingEnableConfig.setStatus("current")


class _EpSpecificCallWaitingEnable_Type(MxEnableState):
    """Custom type epSpecificCallWaitingEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCallWaitingEnable_Type.__name__ = "MxEnableState"
_EpSpecificCallWaitingEnable_Object = MibTableColumn
epSpecificCallWaitingEnable = _EpSpecificCallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 300, 1, 300),
    _EpSpecificCallWaitingEnable_Type()
)
epSpecificCallWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallWaitingEnable.setStatus("current")
_CallWaitingStatusTable_Object = MibTable
callWaitingStatusTable = _CallWaitingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 400)
)
if mibBuilder.loadTexts:
    callWaitingStatusTable.setStatus("current")
_CallWaitingStatusEntry_Object = MibTableRow
callWaitingStatusEntry = _CallWaitingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 400, 1)
)
callWaitingStatusEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callWaitingStatusEpId"),
)
if mibBuilder.loadTexts:
    callWaitingStatusEntry.setStatus("current")
_CallWaitingStatusEpId_Type = OctetString
_CallWaitingStatusEpId_Object = MibTableColumn
callWaitingStatusEpId = _CallWaitingStatusEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 400, 1, 100),
    _CallWaitingStatusEpId_Type()
)
callWaitingStatusEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callWaitingStatusEpId.setStatus("current")
_CallWaitingStatusState_Type = MxActivationState
_CallWaitingStatusState_Object = MibTableColumn
callWaitingStatusState = _CallWaitingStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 400, 1, 200),
    _CallWaitingStatusState_Type()
)
callWaitingStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callWaitingStatusState.setStatus("current")
_CallWaitingUserConfigTable_Object = MibTable
callWaitingUserConfigTable = _CallWaitingUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 500)
)
if mibBuilder.loadTexts:
    callWaitingUserConfigTable.setStatus("current")
_CallWaitingUserConfigEntry_Object = MibTableRow
callWaitingUserConfigEntry = _CallWaitingUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 500, 1)
)
callWaitingUserConfigEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callWaitingUserConfigEpId"),
)
if mibBuilder.loadTexts:
    callWaitingUserConfigEntry.setStatus("current")
_CallWaitingUserConfigEpId_Type = OctetString
_CallWaitingUserConfigEpId_Object = MibTableColumn
callWaitingUserConfigEpId = _CallWaitingUserConfigEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 500, 1, 100),
    _CallWaitingUserConfigEpId_Type()
)
callWaitingUserConfigEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callWaitingUserConfigEpId.setStatus("current")


class _CallWaitingUserConfigState_Type(MxActivationState):
    """Custom type callWaitingUserConfigState based on MxActivationState"""
    defaultValue = 1


_CallWaitingUserConfigState_Type.__name__ = "MxActivationState"
_CallWaitingUserConfigState_Object = MibTableColumn
callWaitingUserConfigState = _CallWaitingUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 400, 500, 1, 200),
    _CallWaitingUserConfigState_Type()
)
callWaitingUserConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingUserConfigState.setStatus("current")
_SecondCallGroup_ObjectIdentity = ObjectIdentity
secondCallGroup = _SecondCallGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500)
)


class _DefaultSecondCallEnable_Type(MxEnableState):
    """Custom type defaultSecondCallEnable based on MxEnableState"""
    defaultValue = 1


_DefaultSecondCallEnable_Type.__name__ = "MxEnableState"
_DefaultSecondCallEnable_Object = MibScalar
defaultSecondCallEnable = _DefaultSecondCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 100),
    _DefaultSecondCallEnable_Type()
)
defaultSecondCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSecondCallEnable.setStatus("current")


class _DefaultSecondCallDisconnectAction_Type(Integer32):
    """Custom type defaultSecondCallDisconnectAction based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("wait", 100),
          ("autoSwitch", 200))
    )


_DefaultSecondCallDisconnectAction_Type.__name__ = "Integer32"
_DefaultSecondCallDisconnectAction_Object = MibScalar
defaultSecondCallDisconnectAction = _DefaultSecondCallDisconnectAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 150),
    _DefaultSecondCallDisconnectAction_Type()
)
defaultSecondCallDisconnectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSecondCallDisconnectAction.setStatus("current")
_EpSpecificSecondCallTable_Object = MibTable
epSpecificSecondCallTable = _EpSpecificSecondCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200)
)
if mibBuilder.loadTexts:
    epSpecificSecondCallTable.setStatus("current")
_EpSpecificSecondCallEntry_Object = MibTableRow
epSpecificSecondCallEntry = _EpSpecificSecondCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200, 1)
)
epSpecificSecondCallEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificSecondCallEpId"),
)
if mibBuilder.loadTexts:
    epSpecificSecondCallEntry.setStatus("current")
_EpSpecificSecondCallEpId_Type = OctetString
_EpSpecificSecondCallEpId_Object = MibTableColumn
epSpecificSecondCallEpId = _EpSpecificSecondCallEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200, 1, 100),
    _EpSpecificSecondCallEpId_Type()
)
epSpecificSecondCallEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificSecondCallEpId.setStatus("current")


class _EpSpecificSecondCallEnableConfig_Type(MxEnableState):
    """Custom type epSpecificSecondCallEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificSecondCallEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificSecondCallEnableConfig_Object = MibTableColumn
epSpecificSecondCallEnableConfig = _EpSpecificSecondCallEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200, 1, 200),
    _EpSpecificSecondCallEnableConfig_Type()
)
epSpecificSecondCallEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecondCallEnableConfig.setStatus("current")


class _EpSpecificSecondCallEnable_Type(MxEnableState):
    """Custom type epSpecificSecondCallEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificSecondCallEnable_Type.__name__ = "MxEnableState"
_EpSpecificSecondCallEnable_Object = MibTableColumn
epSpecificSecondCallEnable = _EpSpecificSecondCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200, 1, 300),
    _EpSpecificSecondCallEnable_Type()
)
epSpecificSecondCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecondCallEnable.setStatus("current")


class _EpSpecificSecondCallDisconnectAction_Type(Integer32):
    """Custom type epSpecificSecondCallDisconnectAction based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("wait", 100),
          ("autoSwitch", 200))
    )


_EpSpecificSecondCallDisconnectAction_Type.__name__ = "Integer32"
_EpSpecificSecondCallDisconnectAction_Object = MibTableColumn
epSpecificSecondCallDisconnectAction = _EpSpecificSecondCallDisconnectAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 200, 1, 400),
    _EpSpecificSecondCallDisconnectAction_Type()
)
epSpecificSecondCallDisconnectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificSecondCallDisconnectAction.setStatus("current")
_SecondCallStatusTable_Object = MibTable
secondCallStatusTable = _SecondCallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 300)
)
if mibBuilder.loadTexts:
    secondCallStatusTable.setStatus("current")
_SecondCallStatusEntry_Object = MibTableRow
secondCallStatusEntry = _SecondCallStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 300, 1)
)
secondCallStatusEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "secondCallStatusEpId"),
)
if mibBuilder.loadTexts:
    secondCallStatusEntry.setStatus("current")
_SecondCallStatusEpId_Type = OctetString
_SecondCallStatusEpId_Object = MibTableColumn
secondCallStatusEpId = _SecondCallStatusEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 300, 1, 100),
    _SecondCallStatusEpId_Type()
)
secondCallStatusEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondCallStatusEpId.setStatus("current")
_SecondCallStatusState_Type = MxActivationState
_SecondCallStatusState_Object = MibTableColumn
secondCallStatusState = _SecondCallStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 500, 300, 1, 200),
    _SecondCallStatusState_Type()
)
secondCallStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondCallStatusState.setStatus("current")
_TransferGroup_ObjectIdentity = ObjectIdentity
transferGroup = _TransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600)
)


class _DefaultTransferBlindEnable_Type(MxEnableState):
    """Custom type defaultTransferBlindEnable based on MxEnableState"""
    defaultValue = 1


_DefaultTransferBlindEnable_Type.__name__ = "MxEnableState"
_DefaultTransferBlindEnable_Object = MibScalar
defaultTransferBlindEnable = _DefaultTransferBlindEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 100),
    _DefaultTransferBlindEnable_Type()
)
defaultTransferBlindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultTransferBlindEnable.setStatus("current")


class _DefaultTransferAttendedEnable_Type(MxEnableState):
    """Custom type defaultTransferAttendedEnable based on MxEnableState"""
    defaultValue = 1


_DefaultTransferAttendedEnable_Type.__name__ = "MxEnableState"
_DefaultTransferAttendedEnable_Object = MibScalar
defaultTransferAttendedEnable = _DefaultTransferAttendedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 200),
    _DefaultTransferAttendedEnable_Type()
)
defaultTransferAttendedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultTransferAttendedEnable.setStatus("current")
_EpSpecificTransferTable_Object = MibTable
epSpecificTransferTable = _EpSpecificTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300)
)
if mibBuilder.loadTexts:
    epSpecificTransferTable.setStatus("current")
_EpSpecificTransferEntry_Object = MibTableRow
epSpecificTransferEntry = _EpSpecificTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300, 1)
)
epSpecificTransferEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificTransferEpId"),
)
if mibBuilder.loadTexts:
    epSpecificTransferEntry.setStatus("current")
_EpSpecificTransferEpId_Type = OctetString
_EpSpecificTransferEpId_Object = MibTableColumn
epSpecificTransferEpId = _EpSpecificTransferEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300, 1, 100),
    _EpSpecificTransferEpId_Type()
)
epSpecificTransferEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificTransferEpId.setStatus("current")


class _EpSpecificTransferEnableConfig_Type(MxEnableState):
    """Custom type epSpecificTransferEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificTransferEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificTransferEnableConfig_Object = MibTableColumn
epSpecificTransferEnableConfig = _EpSpecificTransferEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300, 1, 200),
    _EpSpecificTransferEnableConfig_Type()
)
epSpecificTransferEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificTransferEnableConfig.setStatus("current")


class _EpSpecificTransferBlindEnable_Type(MxEnableState):
    """Custom type epSpecificTransferBlindEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificTransferBlindEnable_Type.__name__ = "MxEnableState"
_EpSpecificTransferBlindEnable_Object = MibTableColumn
epSpecificTransferBlindEnable = _EpSpecificTransferBlindEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300, 1, 500),
    _EpSpecificTransferBlindEnable_Type()
)
epSpecificTransferBlindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificTransferBlindEnable.setStatus("current")


class _EpSpecificTransferAttendedEnable_Type(MxEnableState):
    """Custom type epSpecificTransferAttendedEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificTransferAttendedEnable_Type.__name__ = "MxEnableState"
_EpSpecificTransferAttendedEnable_Object = MibTableColumn
epSpecificTransferAttendedEnable = _EpSpecificTransferAttendedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 300, 1, 600),
    _EpSpecificTransferAttendedEnable_Type()
)
epSpecificTransferAttendedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificTransferAttendedEnable.setStatus("current")
_TransferStatusTable_Object = MibTable
transferStatusTable = _TransferStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 400)
)
if mibBuilder.loadTexts:
    transferStatusTable.setStatus("current")
_TransferStatusEntry_Object = MibTableRow
transferStatusEntry = _TransferStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 400, 1)
)
transferStatusEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "transferStatusEpId"),
)
if mibBuilder.loadTexts:
    transferStatusEntry.setStatus("current")
_TransferStatusEpId_Type = OctetString
_TransferStatusEpId_Object = MibTableColumn
transferStatusEpId = _TransferStatusEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 400, 1, 100),
    _TransferStatusEpId_Type()
)
transferStatusEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatusEpId.setStatus("current")
_TransferStatusBlindState_Type = MxActivationState
_TransferStatusBlindState_Object = MibTableColumn
transferStatusBlindState = _TransferStatusBlindState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 400, 1, 200),
    _TransferStatusBlindState_Type()
)
transferStatusBlindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatusBlindState.setStatus("current")
_TransferStatusAttendedState_Type = MxActivationState
_TransferStatusAttendedState_Object = MibTableColumn
transferStatusAttendedState = _TransferStatusAttendedState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 600, 400, 1, 300),
    _TransferStatusAttendedState_Type()
)
transferStatusAttendedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatusAttendedState.setStatus("current")
_ConferenceGroup_ObjectIdentity = ObjectIdentity
conferenceGroup = _ConferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700)
)


class _DefaultConferenceEnable_Type(MxEnableState):
    """Custom type defaultConferenceEnable based on MxEnableState"""
    defaultValue = 1


_DefaultConferenceEnable_Type.__name__ = "MxEnableState"
_DefaultConferenceEnable_Object = MibScalar
defaultConferenceEnable = _DefaultConferenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 100),
    _DefaultConferenceEnable_Type()
)
defaultConferenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultConferenceEnable.setStatus("current")


class _DefaultConferenceType_Type(Integer32):
    """Custom type defaultConferenceType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("local", 100),
          ("conferenceServer", 200))
    )


_DefaultConferenceType_Type.__name__ = "Integer32"
_DefaultConferenceType_Object = MibScalar
defaultConferenceType = _DefaultConferenceType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 150),
    _DefaultConferenceType_Type()
)
defaultConferenceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultConferenceType.setStatus("current")
_EpSpecificConferenceTable_Object = MibTable
epSpecificConferenceTable = _EpSpecificConferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200)
)
if mibBuilder.loadTexts:
    epSpecificConferenceTable.setStatus("current")
_EpSpecificConferenceEntry_Object = MibTableRow
epSpecificConferenceEntry = _EpSpecificConferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200, 1)
)
epSpecificConferenceEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificConferenceEpId"),
)
if mibBuilder.loadTexts:
    epSpecificConferenceEntry.setStatus("current")
_EpSpecificConferenceEpId_Type = OctetString
_EpSpecificConferenceEpId_Object = MibTableColumn
epSpecificConferenceEpId = _EpSpecificConferenceEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200, 1, 100),
    _EpSpecificConferenceEpId_Type()
)
epSpecificConferenceEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificConferenceEpId.setStatus("current")


class _EpSpecificConferenceEnableConfig_Type(MxEnableState):
    """Custom type epSpecificConferenceEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificConferenceEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificConferenceEnableConfig_Object = MibTableColumn
epSpecificConferenceEnableConfig = _EpSpecificConferenceEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200, 1, 200),
    _EpSpecificConferenceEnableConfig_Type()
)
epSpecificConferenceEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificConferenceEnableConfig.setStatus("current")


class _EpSpecificConferenceEnable_Type(MxEnableState):
    """Custom type epSpecificConferenceEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificConferenceEnable_Type.__name__ = "MxEnableState"
_EpSpecificConferenceEnable_Object = MibTableColumn
epSpecificConferenceEnable = _EpSpecificConferenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200, 1, 300),
    _EpSpecificConferenceEnable_Type()
)
epSpecificConferenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificConferenceEnable.setStatus("current")


class _EpSpecificConferenceType_Type(Integer32):
    """Custom type epSpecificConferenceType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("local", 100),
          ("conferenceServer", 200))
    )


_EpSpecificConferenceType_Type.__name__ = "Integer32"
_EpSpecificConferenceType_Object = MibTableColumn
epSpecificConferenceType = _EpSpecificConferenceType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 200, 1, 400),
    _EpSpecificConferenceType_Type()
)
epSpecificConferenceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificConferenceType.setStatus("current")
_ConferenceStatusTable_Object = MibTable
conferenceStatusTable = _ConferenceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 300)
)
if mibBuilder.loadTexts:
    conferenceStatusTable.setStatus("current")
_ConferenceStatusEntry_Object = MibTableRow
conferenceStatusEntry = _ConferenceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 300, 1)
)
conferenceStatusEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "conferenceStatusEpId"),
)
if mibBuilder.loadTexts:
    conferenceStatusEntry.setStatus("current")
_ConferenceStatusEpId_Type = OctetString
_ConferenceStatusEpId_Object = MibTableColumn
conferenceStatusEpId = _ConferenceStatusEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 300, 1, 100),
    _ConferenceStatusEpId_Type()
)
conferenceStatusEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conferenceStatusEpId.setStatus("current")
_ConferenceStatusState_Type = MxActivationState
_ConferenceStatusState_Object = MibTableColumn
conferenceStatusState = _ConferenceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 700, 300, 1, 200),
    _ConferenceStatusState_Type()
)
conferenceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conferenceStatusState.setStatus("current")
_ForwardGroup_ObjectIdentity = ObjectIdentity
forwardGroup = _ForwardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800)
)
_ForwardUnconditionalGroup_ObjectIdentity = ObjectIdentity
forwardUnconditionalGroup = _ForwardUnconditionalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100)
)


class _DefaultForwardUnconditionalEnable_Type(MxEnableState):
    """Custom type defaultForwardUnconditionalEnable based on MxEnableState"""
    defaultValue = 0


_DefaultForwardUnconditionalEnable_Type.__name__ = "MxEnableState"
_DefaultForwardUnconditionalEnable_Object = MibScalar
defaultForwardUnconditionalEnable = _DefaultForwardUnconditionalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 100),
    _DefaultForwardUnconditionalEnable_Type()
)
defaultForwardUnconditionalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardUnconditionalEnable.setStatus("current")


class _DefaultForwardUnconditionalDtmfMapActivation_Type(MxDigitMap):
    """Custom type defaultForwardUnconditionalDtmfMapActivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardUnconditionalDtmfMapActivation_Type.__name__ = "MxDigitMap"
_DefaultForwardUnconditionalDtmfMapActivation_Object = MibScalar
defaultForwardUnconditionalDtmfMapActivation = _DefaultForwardUnconditionalDtmfMapActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 200),
    _DefaultForwardUnconditionalDtmfMapActivation_Type()
)
defaultForwardUnconditionalDtmfMapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardUnconditionalDtmfMapActivation.setStatus("current")


class _DefaultForwardUnconditionalDtmfMapDeactivation_Type(MxDigitMap):
    """Custom type defaultForwardUnconditionalDtmfMapDeactivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardUnconditionalDtmfMapDeactivation_Type.__name__ = "MxDigitMap"
_DefaultForwardUnconditionalDtmfMapDeactivation_Object = MibScalar
defaultForwardUnconditionalDtmfMapDeactivation = _DefaultForwardUnconditionalDtmfMapDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 300),
    _DefaultForwardUnconditionalDtmfMapDeactivation_Type()
)
defaultForwardUnconditionalDtmfMapDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardUnconditionalDtmfMapDeactivation.setStatus("current")
_EpSpecificForwardUnconditionalTable_Object = MibTable
epSpecificForwardUnconditionalTable = _EpSpecificForwardUnconditionalTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 400)
)
if mibBuilder.loadTexts:
    epSpecificForwardUnconditionalTable.setStatus("current")
_EpSpecificForwardUnconditionalEntry_Object = MibTableRow
epSpecificForwardUnconditionalEntry = _EpSpecificForwardUnconditionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 400, 1)
)
epSpecificForwardUnconditionalEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificForwardUnconditionalEpId"),
)
if mibBuilder.loadTexts:
    epSpecificForwardUnconditionalEntry.setStatus("current")
_EpSpecificForwardUnconditionalEpId_Type = OctetString
_EpSpecificForwardUnconditionalEpId_Object = MibTableColumn
epSpecificForwardUnconditionalEpId = _EpSpecificForwardUnconditionalEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 400, 1, 100),
    _EpSpecificForwardUnconditionalEpId_Type()
)
epSpecificForwardUnconditionalEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificForwardUnconditionalEpId.setStatus("current")


class _EpSpecificForwardUnconditionalEnableConfig_Type(MxEnableState):
    """Custom type epSpecificForwardUnconditionalEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardUnconditionalEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificForwardUnconditionalEnableConfig_Object = MibTableColumn
epSpecificForwardUnconditionalEnableConfig = _EpSpecificForwardUnconditionalEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 400, 1, 200),
    _EpSpecificForwardUnconditionalEnableConfig_Type()
)
epSpecificForwardUnconditionalEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardUnconditionalEnableConfig.setStatus("current")


class _EpSpecificForwardUnconditionalEnable_Type(MxEnableState):
    """Custom type epSpecificForwardUnconditionalEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardUnconditionalEnable_Type.__name__ = "MxEnableState"
_EpSpecificForwardUnconditionalEnable_Object = MibTableColumn
epSpecificForwardUnconditionalEnable = _EpSpecificForwardUnconditionalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 400, 1, 300),
    _EpSpecificForwardUnconditionalEnable_Type()
)
epSpecificForwardUnconditionalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardUnconditionalEnable.setStatus("current")
_ForwardUnconditionalConfigTable_Object = MibTable
forwardUnconditionalConfigTable = _ForwardUnconditionalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 500)
)
if mibBuilder.loadTexts:
    forwardUnconditionalConfigTable.setStatus("current")
_ForwardUnconditionalConfigEntry_Object = MibTableRow
forwardUnconditionalConfigEntry = _ForwardUnconditionalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 500, 1)
)
forwardUnconditionalConfigEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "forwardUnconditionalConfigEpId"),
)
if mibBuilder.loadTexts:
    forwardUnconditionalConfigEntry.setStatus("current")
_ForwardUnconditionalConfigEpId_Type = OctetString
_ForwardUnconditionalConfigEpId_Object = MibTableColumn
forwardUnconditionalConfigEpId = _ForwardUnconditionalConfigEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 500, 1, 100),
    _ForwardUnconditionalConfigEpId_Type()
)
forwardUnconditionalConfigEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardUnconditionalConfigEpId.setStatus("current")


class _ForwardUnconditionalConfigActivation_Type(MxActivationState):
    """Custom type forwardUnconditionalConfigActivation based on MxActivationState"""
    defaultValue = 0


_ForwardUnconditionalConfigActivation_Type.__name__ = "MxActivationState"
_ForwardUnconditionalConfigActivation_Object = MibTableColumn
forwardUnconditionalConfigActivation = _ForwardUnconditionalConfigActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 500, 1, 200),
    _ForwardUnconditionalConfigActivation_Type()
)
forwardUnconditionalConfigActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardUnconditionalConfigActivation.setStatus("current")


class _ForwardUnconditionalConfigForwardingAddress_Type(OctetString):
    """Custom type forwardUnconditionalConfigForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ForwardUnconditionalConfigForwardingAddress_Type.__name__ = "OctetString"
_ForwardUnconditionalConfigForwardingAddress_Object = MibTableColumn
forwardUnconditionalConfigForwardingAddress = _ForwardUnconditionalConfigForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 100, 500, 1, 300),
    _ForwardUnconditionalConfigForwardingAddress_Type()
)
forwardUnconditionalConfigForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardUnconditionalConfigForwardingAddress.setStatus("current")
_ForwardOnBusyGroup_ObjectIdentity = ObjectIdentity
forwardOnBusyGroup = _ForwardOnBusyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200)
)


class _DefaultForwardOnBusyEnable_Type(MxEnableState):
    """Custom type defaultForwardOnBusyEnable based on MxEnableState"""
    defaultValue = 0


_DefaultForwardOnBusyEnable_Type.__name__ = "MxEnableState"
_DefaultForwardOnBusyEnable_Object = MibScalar
defaultForwardOnBusyEnable = _DefaultForwardOnBusyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 100),
    _DefaultForwardOnBusyEnable_Type()
)
defaultForwardOnBusyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardOnBusyEnable.setStatus("current")


class _DefaultForwardOnBusyDtmfMapActivation_Type(MxDigitMap):
    """Custom type defaultForwardOnBusyDtmfMapActivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardOnBusyDtmfMapActivation_Type.__name__ = "MxDigitMap"
_DefaultForwardOnBusyDtmfMapActivation_Object = MibScalar
defaultForwardOnBusyDtmfMapActivation = _DefaultForwardOnBusyDtmfMapActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 300),
    _DefaultForwardOnBusyDtmfMapActivation_Type()
)
defaultForwardOnBusyDtmfMapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardOnBusyDtmfMapActivation.setStatus("current")


class _DefaultForwardOnBusyDtmfMapDeactivation_Type(MxDigitMap):
    """Custom type defaultForwardOnBusyDtmfMapDeactivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardOnBusyDtmfMapDeactivation_Type.__name__ = "MxDigitMap"
_DefaultForwardOnBusyDtmfMapDeactivation_Object = MibScalar
defaultForwardOnBusyDtmfMapDeactivation = _DefaultForwardOnBusyDtmfMapDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 400),
    _DefaultForwardOnBusyDtmfMapDeactivation_Type()
)
defaultForwardOnBusyDtmfMapDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardOnBusyDtmfMapDeactivation.setStatus("current")
_EpSpecificForwardOnBusyTable_Object = MibTable
epSpecificForwardOnBusyTable = _EpSpecificForwardOnBusyTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 500)
)
if mibBuilder.loadTexts:
    epSpecificForwardOnBusyTable.setStatus("current")
_EpSpecificForwardOnBusyEntry_Object = MibTableRow
epSpecificForwardOnBusyEntry = _EpSpecificForwardOnBusyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 500, 1)
)
epSpecificForwardOnBusyEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificForwardOnBusyEpId"),
)
if mibBuilder.loadTexts:
    epSpecificForwardOnBusyEntry.setStatus("current")
_EpSpecificForwardOnBusyEpId_Type = OctetString
_EpSpecificForwardOnBusyEpId_Object = MibTableColumn
epSpecificForwardOnBusyEpId = _EpSpecificForwardOnBusyEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 500, 1, 100),
    _EpSpecificForwardOnBusyEpId_Type()
)
epSpecificForwardOnBusyEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificForwardOnBusyEpId.setStatus("current")


class _EpSpecificForwardOnBusyEnableConfig_Type(MxEnableState):
    """Custom type epSpecificForwardOnBusyEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardOnBusyEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificForwardOnBusyEnableConfig_Object = MibTableColumn
epSpecificForwardOnBusyEnableConfig = _EpSpecificForwardOnBusyEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 500, 1, 200),
    _EpSpecificForwardOnBusyEnableConfig_Type()
)
epSpecificForwardOnBusyEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardOnBusyEnableConfig.setStatus("current")


class _EpSpecificForwardOnBusyEnable_Type(MxEnableState):
    """Custom type epSpecificForwardOnBusyEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardOnBusyEnable_Type.__name__ = "MxEnableState"
_EpSpecificForwardOnBusyEnable_Object = MibTableColumn
epSpecificForwardOnBusyEnable = _EpSpecificForwardOnBusyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 500, 1, 300),
    _EpSpecificForwardOnBusyEnable_Type()
)
epSpecificForwardOnBusyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardOnBusyEnable.setStatus("current")
_ForwardOnBusyConfigTable_Object = MibTable
forwardOnBusyConfigTable = _ForwardOnBusyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 600)
)
if mibBuilder.loadTexts:
    forwardOnBusyConfigTable.setStatus("current")
_ForwardOnBusyConfigEntry_Object = MibTableRow
forwardOnBusyConfigEntry = _ForwardOnBusyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 600, 1)
)
forwardOnBusyConfigEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "forwardOnBusyConfigEpId"),
)
if mibBuilder.loadTexts:
    forwardOnBusyConfigEntry.setStatus("current")
_ForwardOnBusyConfigEpId_Type = OctetString
_ForwardOnBusyConfigEpId_Object = MibTableColumn
forwardOnBusyConfigEpId = _ForwardOnBusyConfigEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 600, 1, 100),
    _ForwardOnBusyConfigEpId_Type()
)
forwardOnBusyConfigEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardOnBusyConfigEpId.setStatus("current")


class _ForwardOnBusyConfigActivation_Type(MxActivationState):
    """Custom type forwardOnBusyConfigActivation based on MxActivationState"""
    defaultValue = 0


_ForwardOnBusyConfigActivation_Type.__name__ = "MxActivationState"
_ForwardOnBusyConfigActivation_Object = MibTableColumn
forwardOnBusyConfigActivation = _ForwardOnBusyConfigActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 600, 1, 200),
    _ForwardOnBusyConfigActivation_Type()
)
forwardOnBusyConfigActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardOnBusyConfigActivation.setStatus("current")


class _ForwardOnBusyConfigForwardingAddress_Type(OctetString):
    """Custom type forwardOnBusyConfigForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ForwardOnBusyConfigForwardingAddress_Type.__name__ = "OctetString"
_ForwardOnBusyConfigForwardingAddress_Object = MibTableColumn
forwardOnBusyConfigForwardingAddress = _ForwardOnBusyConfigForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 200, 600, 1, 300),
    _ForwardOnBusyConfigForwardingAddress_Type()
)
forwardOnBusyConfigForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardOnBusyConfigForwardingAddress.setStatus("current")
_ForwardNoAnswerGroup_ObjectIdentity = ObjectIdentity
forwardNoAnswerGroup = _ForwardNoAnswerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300)
)


class _DefaultForwardNoAnswerEnable_Type(MxEnableState):
    """Custom type defaultForwardNoAnswerEnable based on MxEnableState"""
    defaultValue = 0


_DefaultForwardNoAnswerEnable_Type.__name__ = "MxEnableState"
_DefaultForwardNoAnswerEnable_Object = MibScalar
defaultForwardNoAnswerEnable = _DefaultForwardNoAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 100),
    _DefaultForwardNoAnswerEnable_Type()
)
defaultForwardNoAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardNoAnswerEnable.setStatus("current")


class _DefaultForwardNoAnswerTimeout_Type(Unsigned32):
    """Custom type defaultForwardNoAnswerTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 120000),
    )


_DefaultForwardNoAnswerTimeout_Type.__name__ = "Unsigned32"
_DefaultForwardNoAnswerTimeout_Object = MibScalar
defaultForwardNoAnswerTimeout = _DefaultForwardNoAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 200),
    _DefaultForwardNoAnswerTimeout_Type()
)
defaultForwardNoAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardNoAnswerTimeout.setStatus("current")


class _DefaultForwardNoAnswerDtmfMapActivation_Type(MxDigitMap):
    """Custom type defaultForwardNoAnswerDtmfMapActivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardNoAnswerDtmfMapActivation_Type.__name__ = "MxDigitMap"
_DefaultForwardNoAnswerDtmfMapActivation_Object = MibScalar
defaultForwardNoAnswerDtmfMapActivation = _DefaultForwardNoAnswerDtmfMapActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 300),
    _DefaultForwardNoAnswerDtmfMapActivation_Type()
)
defaultForwardNoAnswerDtmfMapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardNoAnswerDtmfMapActivation.setStatus("current")


class _DefaultForwardNoAnswerDtmfMapDeactivation_Type(MxDigitMap):
    """Custom type defaultForwardNoAnswerDtmfMapDeactivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultForwardNoAnswerDtmfMapDeactivation_Type.__name__ = "MxDigitMap"
_DefaultForwardNoAnswerDtmfMapDeactivation_Object = MibScalar
defaultForwardNoAnswerDtmfMapDeactivation = _DefaultForwardNoAnswerDtmfMapDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 400),
    _DefaultForwardNoAnswerDtmfMapDeactivation_Type()
)
defaultForwardNoAnswerDtmfMapDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardNoAnswerDtmfMapDeactivation.setStatus("current")
_EpSpecificForwardNoAnswerTable_Object = MibTable
epSpecificForwardNoAnswerTable = _EpSpecificForwardNoAnswerTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500)
)
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerTable.setStatus("current")
_EpSpecificForwardNoAnswerEntry_Object = MibTableRow
epSpecificForwardNoAnswerEntry = _EpSpecificForwardNoAnswerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500, 1)
)
epSpecificForwardNoAnswerEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificForwardNoAnswerEpId"),
)
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerEntry.setStatus("current")
_EpSpecificForwardNoAnswerEpId_Type = OctetString
_EpSpecificForwardNoAnswerEpId_Object = MibTableColumn
epSpecificForwardNoAnswerEpId = _EpSpecificForwardNoAnswerEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500, 1, 100),
    _EpSpecificForwardNoAnswerEpId_Type()
)
epSpecificForwardNoAnswerEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerEpId.setStatus("current")


class _EpSpecificForwardNoAnswerEnableConfig_Type(MxEnableState):
    """Custom type epSpecificForwardNoAnswerEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardNoAnswerEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificForwardNoAnswerEnableConfig_Object = MibTableColumn
epSpecificForwardNoAnswerEnableConfig = _EpSpecificForwardNoAnswerEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500, 1, 200),
    _EpSpecificForwardNoAnswerEnableConfig_Type()
)
epSpecificForwardNoAnswerEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerEnableConfig.setStatus("current")


class _EpSpecificForwardNoAnswerEnable_Type(MxEnableState):
    """Custom type epSpecificForwardNoAnswerEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificForwardNoAnswerEnable_Type.__name__ = "MxEnableState"
_EpSpecificForwardNoAnswerEnable_Object = MibTableColumn
epSpecificForwardNoAnswerEnable = _EpSpecificForwardNoAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500, 1, 300),
    _EpSpecificForwardNoAnswerEnable_Type()
)
epSpecificForwardNoAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerEnable.setStatus("current")


class _EpSpecificForwardNoAnswerTimeout_Type(Unsigned32):
    """Custom type epSpecificForwardNoAnswerTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 120000),
    )


_EpSpecificForwardNoAnswerTimeout_Type.__name__ = "Unsigned32"
_EpSpecificForwardNoAnswerTimeout_Object = MibTableColumn
epSpecificForwardNoAnswerTimeout = _EpSpecificForwardNoAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 500, 1, 400),
    _EpSpecificForwardNoAnswerTimeout_Type()
)
epSpecificForwardNoAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificForwardNoAnswerTimeout.setStatus("current")
_ForwardNoAnswerConfigTable_Object = MibTable
forwardNoAnswerConfigTable = _ForwardNoAnswerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 600)
)
if mibBuilder.loadTexts:
    forwardNoAnswerConfigTable.setStatus("current")
_ForwardNoAnswerConfigEntry_Object = MibTableRow
forwardNoAnswerConfigEntry = _ForwardNoAnswerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 600, 1)
)
forwardNoAnswerConfigEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "forwardNoAnswerConfigEpId"),
)
if mibBuilder.loadTexts:
    forwardNoAnswerConfigEntry.setStatus("current")
_ForwardNoAnswerConfigEpId_Type = OctetString
_ForwardNoAnswerConfigEpId_Object = MibTableColumn
forwardNoAnswerConfigEpId = _ForwardNoAnswerConfigEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 600, 1, 100),
    _ForwardNoAnswerConfigEpId_Type()
)
forwardNoAnswerConfigEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardNoAnswerConfigEpId.setStatus("current")


class _ForwardNoAnswerConfigActivation_Type(MxActivationState):
    """Custom type forwardNoAnswerConfigActivation based on MxActivationState"""
    defaultValue = 0


_ForwardNoAnswerConfigActivation_Type.__name__ = "MxActivationState"
_ForwardNoAnswerConfigActivation_Object = MibTableColumn
forwardNoAnswerConfigActivation = _ForwardNoAnswerConfigActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 600, 1, 200),
    _ForwardNoAnswerConfigActivation_Type()
)
forwardNoAnswerConfigActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardNoAnswerConfigActivation.setStatus("current")


class _ForwardNoAnswerConfigForwardingAddress_Type(OctetString):
    """Custom type forwardNoAnswerConfigForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ForwardNoAnswerConfigForwardingAddress_Type.__name__ = "OctetString"
_ForwardNoAnswerConfigForwardingAddress_Object = MibTableColumn
forwardNoAnswerConfigForwardingAddress = _ForwardNoAnswerConfigForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 800, 300, 600, 1, 300),
    _ForwardNoAnswerConfigForwardingAddress_Type()
)
forwardNoAnswerConfigForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardNoAnswerConfigForwardingAddress.setStatus("current")
_CallCompletionGroup_ObjectIdentity = ObjectIdentity
callCompletionGroup = _CallCompletionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900)
)


class _DefaultCallCompletionBusySubscriberEnable_Type(MxEnableState):
    """Custom type defaultCallCompletionBusySubscriberEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCallCompletionBusySubscriberEnable_Type.__name__ = "MxEnableState"
_DefaultCallCompletionBusySubscriberEnable_Object = MibScalar
defaultCallCompletionBusySubscriberEnable = _DefaultCallCompletionBusySubscriberEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 100),
    _DefaultCallCompletionBusySubscriberEnable_Type()
)
defaultCallCompletionBusySubscriberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionBusySubscriberEnable.setStatus("current")


class _DefaultCallCompletionBusySubscriberDtmfMapActivation_Type(MxDigitMap):
    """Custom type defaultCallCompletionBusySubscriberDtmfMapActivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallCompletionBusySubscriberDtmfMapActivation_Type.__name__ = "MxDigitMap"
_DefaultCallCompletionBusySubscriberDtmfMapActivation_Object = MibScalar
defaultCallCompletionBusySubscriberDtmfMapActivation = _DefaultCallCompletionBusySubscriberDtmfMapActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 200),
    _DefaultCallCompletionBusySubscriberDtmfMapActivation_Type()
)
defaultCallCompletionBusySubscriberDtmfMapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionBusySubscriberDtmfMapActivation.setStatus("current")


class _DefaultCallCompletionNoReplyEnable_Type(MxEnableState):
    """Custom type defaultCallCompletionNoReplyEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCallCompletionNoReplyEnable_Type.__name__ = "MxEnableState"
_DefaultCallCompletionNoReplyEnable_Object = MibScalar
defaultCallCompletionNoReplyEnable = _DefaultCallCompletionNoReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 300),
    _DefaultCallCompletionNoReplyEnable_Type()
)
defaultCallCompletionNoReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionNoReplyEnable.setStatus("current")


class _DefaultCallCompletionNoReplyDtmfMapActivation_Type(MxDigitMap):
    """Custom type defaultCallCompletionNoReplyDtmfMapActivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallCompletionNoReplyDtmfMapActivation_Type.__name__ = "MxDigitMap"
_DefaultCallCompletionNoReplyDtmfMapActivation_Object = MibScalar
defaultCallCompletionNoReplyDtmfMapActivation = _DefaultCallCompletionNoReplyDtmfMapActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 400),
    _DefaultCallCompletionNoReplyDtmfMapActivation_Type()
)
defaultCallCompletionNoReplyDtmfMapActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionNoReplyDtmfMapActivation.setStatus("current")


class _DefaultCallCompletionDtmfMapDeactivation_Type(MxDigitMap):
    """Custom type defaultCallCompletionDtmfMapDeactivation based on MxDigitMap"""
    defaultValue = OctetString("")


_DefaultCallCompletionDtmfMapDeactivation_Type.__name__ = "MxDigitMap"
_DefaultCallCompletionDtmfMapDeactivation_Object = MibScalar
defaultCallCompletionDtmfMapDeactivation = _DefaultCallCompletionDtmfMapDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 500),
    _DefaultCallCompletionDtmfMapDeactivation_Type()
)
defaultCallCompletionDtmfMapDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionDtmfMapDeactivation.setStatus("current")


class _DefaultCallCompletionExpirationTimeout_Type(Unsigned32):
    """Custom type defaultCallCompletionExpirationTimeout based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_DefaultCallCompletionExpirationTimeout_Type.__name__ = "Unsigned32"
_DefaultCallCompletionExpirationTimeout_Object = MibScalar
defaultCallCompletionExpirationTimeout = _DefaultCallCompletionExpirationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 600),
    _DefaultCallCompletionExpirationTimeout_Type()
)
defaultCallCompletionExpirationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionExpirationTimeout.setStatus("current")


class _DefaultCallCompletionMethod_Type(Integer32):
    """Custom type defaultCallCompletionMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("monitoringOnly", 100),
          ("monitoringAndPolling", 200))
    )


_DefaultCallCompletionMethod_Type.__name__ = "Integer32"
_DefaultCallCompletionMethod_Object = MibScalar
defaultCallCompletionMethod = _DefaultCallCompletionMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 650),
    _DefaultCallCompletionMethod_Type()
)
defaultCallCompletionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionMethod.setStatus("current")


class _DefaultCallCompletionAutoReactivateEnable_Type(MxEnableState):
    """Custom type defaultCallCompletionAutoReactivateEnable based on MxEnableState"""
    defaultValue = 0


_DefaultCallCompletionAutoReactivateEnable_Type.__name__ = "MxEnableState"
_DefaultCallCompletionAutoReactivateEnable_Object = MibScalar
defaultCallCompletionAutoReactivateEnable = _DefaultCallCompletionAutoReactivateEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 700),
    _DefaultCallCompletionAutoReactivateEnable_Type()
)
defaultCallCompletionAutoReactivateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionAutoReactivateEnable.setStatus("current")


class _DefaultCallCompletionAutoReactivateDelay_Type(Unsigned32):
    """Custom type defaultCallCompletionAutoReactivateDelay based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_DefaultCallCompletionAutoReactivateDelay_Type.__name__ = "Unsigned32"
_DefaultCallCompletionAutoReactivateDelay_Object = MibScalar
defaultCallCompletionAutoReactivateDelay = _DefaultCallCompletionAutoReactivateDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 750),
    _DefaultCallCompletionAutoReactivateDelay_Type()
)
defaultCallCompletionAutoReactivateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionAutoReactivateDelay.setStatus("current")


class _DefaultCallCompletionEarlyMediaBehaviour_Type(Integer32):
    """Custom type defaultCallCompletionEarlyMediaBehaviour based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("ccbs", 200),
          ("ccnr", 300))
    )


_DefaultCallCompletionEarlyMediaBehaviour_Type.__name__ = "Integer32"
_DefaultCallCompletionEarlyMediaBehaviour_Object = MibScalar
defaultCallCompletionEarlyMediaBehaviour = _DefaultCallCompletionEarlyMediaBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 775),
    _DefaultCallCompletionEarlyMediaBehaviour_Type()
)
defaultCallCompletionEarlyMediaBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionEarlyMediaBehaviour.setStatus("current")
_EpSpecificCallCompletionTable_Object = MibTable
epSpecificCallCompletionTable = _EpSpecificCallCompletionTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800)
)
if mibBuilder.loadTexts:
    epSpecificCallCompletionTable.setStatus("current")
_EpSpecificCallCompletionEntry_Object = MibTableRow
epSpecificCallCompletionEntry = _EpSpecificCallCompletionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800, 1)
)
epSpecificCallCompletionEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificCallCompletionEpId"),
)
if mibBuilder.loadTexts:
    epSpecificCallCompletionEntry.setStatus("current")
_EpSpecificCallCompletionEpId_Type = OctetString
_EpSpecificCallCompletionEpId_Object = MibTableColumn
epSpecificCallCompletionEpId = _EpSpecificCallCompletionEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800, 1, 100),
    _EpSpecificCallCompletionEpId_Type()
)
epSpecificCallCompletionEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificCallCompletionEpId.setStatus("current")


class _EpSpecificCallCompletionEnableConfig_Type(MxEnableState):
    """Custom type epSpecificCallCompletionEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificCallCompletionEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificCallCompletionEnableConfig_Object = MibTableColumn
epSpecificCallCompletionEnableConfig = _EpSpecificCallCompletionEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800, 1, 200),
    _EpSpecificCallCompletionEnableConfig_Type()
)
epSpecificCallCompletionEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallCompletionEnableConfig.setStatus("current")


class _EpSpecificCallCompletionBusySubscriberEnable_Type(MxEnableState):
    """Custom type epSpecificCallCompletionBusySubscriberEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCallCompletionBusySubscriberEnable_Type.__name__ = "MxEnableState"
_EpSpecificCallCompletionBusySubscriberEnable_Object = MibTableColumn
epSpecificCallCompletionBusySubscriberEnable = _EpSpecificCallCompletionBusySubscriberEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800, 1, 300),
    _EpSpecificCallCompletionBusySubscriberEnable_Type()
)
epSpecificCallCompletionBusySubscriberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallCompletionBusySubscriberEnable.setStatus("current")


class _EpSpecificCallCompletionNoReplyEnable_Type(MxEnableState):
    """Custom type epSpecificCallCompletionNoReplyEnable based on MxEnableState"""
    defaultValue = 1


_EpSpecificCallCompletionNoReplyEnable_Type.__name__ = "MxEnableState"
_EpSpecificCallCompletionNoReplyEnable_Object = MibTableColumn
epSpecificCallCompletionNoReplyEnable = _EpSpecificCallCompletionNoReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 800, 1, 400),
    _EpSpecificCallCompletionNoReplyEnable_Type()
)
epSpecificCallCompletionNoReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificCallCompletionNoReplyEnable.setStatus("current")
_CallCompletionConfigTable_Object = MibTable
callCompletionConfigTable = _CallCompletionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900)
)
if mibBuilder.loadTexts:
    callCompletionConfigTable.setStatus("current")
_CallCompletionConfigEntry_Object = MibTableRow
callCompletionConfigEntry = _CallCompletionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1)
)
callCompletionConfigEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callCompletionConfigIndex"),
)
if mibBuilder.loadTexts:
    callCompletionConfigEntry.setStatus("current")
_CallCompletionConfigIndex_Type = Unsigned32
_CallCompletionConfigIndex_Object = MibTableColumn
callCompletionConfigIndex = _CallCompletionConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1, 100),
    _CallCompletionConfigIndex_Type()
)
callCompletionConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCompletionConfigIndex.setStatus("current")
_CallCompletionConfigEpId_Type = OctetString
_CallCompletionConfigEpId_Object = MibTableColumn
callCompletionConfigEpId = _CallCompletionConfigEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1, 200),
    _CallCompletionConfigEpId_Type()
)
callCompletionConfigEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCompletionConfigEpId.setStatus("current")


class _CallCompletionConfigType_Type(Integer32):
    """Custom type callCompletionConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ccbs", 100),
          ("ccnr", 200))
    )


_CallCompletionConfigType_Type.__name__ = "Integer32"
_CallCompletionConfigType_Object = MibTableColumn
callCompletionConfigType = _CallCompletionConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1, 300),
    _CallCompletionConfigType_Type()
)
callCompletionConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCompletionConfigType.setStatus("current")
_CallCompletionConfigTargetAddress_Type = OctetString
_CallCompletionConfigTargetAddress_Object = MibTableColumn
callCompletionConfigTargetAddress = _CallCompletionConfigTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1, 400),
    _CallCompletionConfigTargetAddress_Type()
)
callCompletionConfigTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCompletionConfigTargetAddress.setStatus("current")


class _CallCompletionConfigTargetState_Type(Integer32):
    """Custom type callCompletionConfigTargetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 100),
          ("idle", 200),
          ("busy", 300))
    )


_CallCompletionConfigTargetState_Type.__name__ = "Integer32"
_CallCompletionConfigTargetState_Object = MibTableColumn
callCompletionConfigTargetState = _CallCompletionConfigTargetState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 900, 1, 500),
    _CallCompletionConfigTargetState_Type()
)
callCompletionConfigTargetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCompletionConfigTargetState.setStatus("current")
_CallCompletionPollingGroup_ObjectIdentity = ObjectIdentity
callCompletionPollingGroup = _CallCompletionPollingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 10000)
)


class _DefaultCallCompletionPollingInterval_Type(Unsigned32):
    """Custom type defaultCallCompletionPollingInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_DefaultCallCompletionPollingInterval_Type.__name__ = "Unsigned32"
_DefaultCallCompletionPollingInterval_Object = MibScalar
defaultCallCompletionPollingInterval = _DefaultCallCompletionPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 900, 10000, 780),
    _DefaultCallCompletionPollingInterval_Type()
)
defaultCallCompletionPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCallCompletionPollingInterval.setStatus("current")
_DelayedHotlineGroup_ObjectIdentity = ObjectIdentity
delayedHotlineGroup = _DelayedHotlineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000)
)


class _DefaultDelayedHotlineEnable_Type(MxEnableState):
    """Custom type defaultDelayedHotlineEnable based on MxEnableState"""
    defaultValue = 0


_DefaultDelayedHotlineEnable_Type.__name__ = "MxEnableState"
_DefaultDelayedHotlineEnable_Object = MibScalar
defaultDelayedHotlineEnable = _DefaultDelayedHotlineEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 100),
    _DefaultDelayedHotlineEnable_Type()
)
defaultDelayedHotlineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDelayedHotlineEnable.setStatus("current")


class _DefaultDelayedHotlineCondition_Type(Integer32):
    """Custom type defaultDelayedHotlineCondition based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("firstDtmfTimeout", 100),
          ("interDtmfOrCompletionTimeout", 200),
          ("anyTimeout", 300))
    )


_DefaultDelayedHotlineCondition_Type.__name__ = "Integer32"
_DefaultDelayedHotlineCondition_Object = MibScalar
defaultDelayedHotlineCondition = _DefaultDelayedHotlineCondition_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 200),
    _DefaultDelayedHotlineCondition_Type()
)
defaultDelayedHotlineCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDelayedHotlineCondition.setStatus("current")


class _DefaultDelayedHotlineTargetAddress_Type(OctetString):
    """Custom type defaultDelayedHotlineTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DefaultDelayedHotlineTargetAddress_Type.__name__ = "OctetString"
_DefaultDelayedHotlineTargetAddress_Object = MibScalar
defaultDelayedHotlineTargetAddress = _DefaultDelayedHotlineTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 300),
    _DefaultDelayedHotlineTargetAddress_Type()
)
defaultDelayedHotlineTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDelayedHotlineTargetAddress.setStatus("current")
_EpSpecificDelayedHotlineTable_Object = MibTable
epSpecificDelayedHotlineTable = _EpSpecificDelayedHotlineTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000)
)
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineTable.setStatus("current")
_EpSpecificDelayedHotlineEntry_Object = MibTableRow
epSpecificDelayedHotlineEntry = _EpSpecificDelayedHotlineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1)
)
epSpecificDelayedHotlineEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificDelayedHotlineEpId"),
)
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineEntry.setStatus("current")
_EpSpecificDelayedHotlineEpId_Type = OctetString
_EpSpecificDelayedHotlineEpId_Object = MibTableColumn
epSpecificDelayedHotlineEpId = _EpSpecificDelayedHotlineEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1, 100),
    _EpSpecificDelayedHotlineEpId_Type()
)
epSpecificDelayedHotlineEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineEpId.setStatus("current")


class _EpSpecificDelayedHotlineEnableConfig_Type(MxEnableState):
    """Custom type epSpecificDelayedHotlineEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificDelayedHotlineEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificDelayedHotlineEnableConfig_Object = MibTableColumn
epSpecificDelayedHotlineEnableConfig = _EpSpecificDelayedHotlineEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1, 200),
    _EpSpecificDelayedHotlineEnableConfig_Type()
)
epSpecificDelayedHotlineEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineEnableConfig.setStatus("current")


class _EpSpecificDelayedHotlineEnable_Type(MxEnableState):
    """Custom type epSpecificDelayedHotlineEnable based on MxEnableState"""
    defaultValue = 0


_EpSpecificDelayedHotlineEnable_Type.__name__ = "MxEnableState"
_EpSpecificDelayedHotlineEnable_Object = MibTableColumn
epSpecificDelayedHotlineEnable = _EpSpecificDelayedHotlineEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1, 300),
    _EpSpecificDelayedHotlineEnable_Type()
)
epSpecificDelayedHotlineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineEnable.setStatus("current")


class _EpSpecificDelayedHotlineCondition_Type(Integer32):
    """Custom type epSpecificDelayedHotlineCondition based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("firstDtmfTimeout", 100),
          ("interDtmfOrCompletionTimeout", 200),
          ("anyTimeout", 300))
    )


_EpSpecificDelayedHotlineCondition_Type.__name__ = "Integer32"
_EpSpecificDelayedHotlineCondition_Object = MibTableColumn
epSpecificDelayedHotlineCondition = _EpSpecificDelayedHotlineCondition_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1, 400),
    _EpSpecificDelayedHotlineCondition_Type()
)
epSpecificDelayedHotlineCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineCondition.setStatus("current")


class _EpSpecificDelayedHotlineTargetAddress_Type(OctetString):
    """Custom type epSpecificDelayedHotlineTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EpSpecificDelayedHotlineTargetAddress_Type.__name__ = "OctetString"
_EpSpecificDelayedHotlineTargetAddress_Object = MibTableColumn
epSpecificDelayedHotlineTargetAddress = _EpSpecificDelayedHotlineTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1000, 1000, 1, 500),
    _EpSpecificDelayedHotlineTargetAddress_Type()
)
epSpecificDelayedHotlineTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDelayedHotlineTargetAddress.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200)
)
_CallStatisticsTable_Object = MibTable
callStatisticsTable = _CallStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100)
)
if mibBuilder.loadTexts:
    callStatisticsTable.setStatus("current")
_CallStatisticsEntry_Object = MibTableRow
callStatisticsEntry = _CallStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1)
)
callStatisticsEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "callStatisticsEpId"),
)
if mibBuilder.loadTexts:
    callStatisticsEntry.setStatus("current")
_CallStatisticsEpId_Type = OctetString
_CallStatisticsEpId_Object = MibTableColumn
callStatisticsEpId = _CallStatisticsEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 100),
    _CallStatisticsEpId_Type()
)
callStatisticsEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsEpId.setStatus("current")
_CallStatisticsIncomingCallsReceived_Type = Unsigned32
_CallStatisticsIncomingCallsReceived_Object = MibTableColumn
callStatisticsIncomingCallsReceived = _CallStatisticsIncomingCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 200),
    _CallStatisticsIncomingCallsReceived_Type()
)
callStatisticsIncomingCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsIncomingCallsReceived.setStatus("current")
_CallStatisticsIncomingCallsAnswered_Type = Unsigned32
_CallStatisticsIncomingCallsAnswered_Object = MibTableColumn
callStatisticsIncomingCallsAnswered = _CallStatisticsIncomingCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 300),
    _CallStatisticsIncomingCallsAnswered_Type()
)
callStatisticsIncomingCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsIncomingCallsAnswered.setStatus("current")
_CallStatisticsIncomingCallsConnected_Type = Unsigned32
_CallStatisticsIncomingCallsConnected_Object = MibTableColumn
callStatisticsIncomingCallsConnected = _CallStatisticsIncomingCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 400),
    _CallStatisticsIncomingCallsConnected_Type()
)
callStatisticsIncomingCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsIncomingCallsConnected.setStatus("current")
_CallStatisticsIncomingCallsFailed_Type = Unsigned32
_CallStatisticsIncomingCallsFailed_Object = MibTableColumn
callStatisticsIncomingCallsFailed = _CallStatisticsIncomingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 500),
    _CallStatisticsIncomingCallsFailed_Type()
)
callStatisticsIncomingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsIncomingCallsFailed.setStatus("current")
_CallStatisticsOutgoingCallsAttempted_Type = Unsigned32
_CallStatisticsOutgoingCallsAttempted_Object = MibTableColumn
callStatisticsOutgoingCallsAttempted = _CallStatisticsOutgoingCallsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 600),
    _CallStatisticsOutgoingCallsAttempted_Type()
)
callStatisticsOutgoingCallsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsOutgoingCallsAttempted.setStatus("current")
_CallStatisticsOutgoingCallsAnswered_Type = Unsigned32
_CallStatisticsOutgoingCallsAnswered_Object = MibTableColumn
callStatisticsOutgoingCallsAnswered = _CallStatisticsOutgoingCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 700),
    _CallStatisticsOutgoingCallsAnswered_Type()
)
callStatisticsOutgoingCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsOutgoingCallsAnswered.setStatus("current")
_CallStatisticsOutgoingCallsConnected_Type = Unsigned32
_CallStatisticsOutgoingCallsConnected_Object = MibTableColumn
callStatisticsOutgoingCallsConnected = _CallStatisticsOutgoingCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 800),
    _CallStatisticsOutgoingCallsConnected_Type()
)
callStatisticsOutgoingCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsOutgoingCallsConnected.setStatus("current")
_CallStatisticsOutgoingCallsFailed_Type = Unsigned32
_CallStatisticsOutgoingCallsFailed_Object = MibTableColumn
callStatisticsOutgoingCallsFailed = _CallStatisticsOutgoingCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 900),
    _CallStatisticsOutgoingCallsFailed_Type()
)
callStatisticsOutgoingCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsOutgoingCallsFailed.setStatus("current")
_CallStatisticsCallsDropped_Type = Unsigned32
_CallStatisticsCallsDropped_Object = MibTableColumn
callStatisticsCallsDropped = _CallStatisticsCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 1000),
    _CallStatisticsCallsDropped_Type()
)
callStatisticsCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsCallsDropped.setStatus("current")
_CallStatisticsTotalCallTime_Type = Unsigned32
_CallStatisticsTotalCallTime_Object = MibTableColumn
callStatisticsTotalCallTime = _CallStatisticsTotalCallTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 1100),
    _CallStatisticsTotalCallTime_Type()
)
callStatisticsTotalCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatisticsTotalCallTime.setStatus("current")


class _CallStatisticsReset_Type(Integer32):
    """Custom type callStatisticsReset based on Integer32"""
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
          ("reset", 10))
    )


_CallStatisticsReset_Type.__name__ = "Integer32"
_CallStatisticsReset_Object = MibTableColumn
callStatisticsReset = _CallStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 1200, 100, 1, 1200),
    _CallStatisticsReset_Type()
)
callStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callStatisticsReset.setStatus("current")
_DtmfMapGroup_ObjectIdentity = ObjectIdentity
dtmfMapGroup = _DtmfMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000)
)


class _DtmfMapTimeoutCompletion_Type(Unsigned32):
    """Custom type dtmfMapTimeoutCompletion based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_DtmfMapTimeoutCompletion_Type.__name__ = "Unsigned32"
_DtmfMapTimeoutCompletion_Object = MibScalar
dtmfMapTimeoutCompletion = _DtmfMapTimeoutCompletion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 100),
    _DtmfMapTimeoutCompletion_Type()
)
dtmfMapTimeoutCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmfMapTimeoutCompletion.setStatus("current")


class _DtmfMapTimeoutFirstDtmf_Type(Unsigned32):
    """Custom type dtmfMapTimeoutFirstDtmf based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_DtmfMapTimeoutFirstDtmf_Type.__name__ = "Unsigned32"
_DtmfMapTimeoutFirstDtmf_Object = MibScalar
dtmfMapTimeoutFirstDtmf = _DtmfMapTimeoutFirstDtmf_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 200),
    _DtmfMapTimeoutFirstDtmf_Type()
)
dtmfMapTimeoutFirstDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmfMapTimeoutFirstDtmf.setStatus("current")


class _DtmfMapTimeoutInterDtmf_Type(Unsigned32):
    """Custom type dtmfMapTimeoutInterDtmf based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_DtmfMapTimeoutInterDtmf_Type.__name__ = "Unsigned32"
_DtmfMapTimeoutInterDtmf_Object = MibScalar
dtmfMapTimeoutInterDtmf = _DtmfMapTimeoutInterDtmf_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 300),
    _DtmfMapTimeoutInterDtmf_Type()
)
dtmfMapTimeoutInterDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmfMapTimeoutInterDtmf.setStatus("current")
_EpSpecificDtmfMapTimeoutTable_Object = MibTable
epSpecificDtmfMapTimeoutTable = _EpSpecificDtmfMapTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000)
)
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutTable.setStatus("current")
_EpSpecificDtmfMapTimeoutEntry_Object = MibTableRow
epSpecificDtmfMapTimeoutEntry = _EpSpecificDtmfMapTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1)
)
epSpecificDtmfMapTimeoutEntry.setIndexNames(
    (0, "MX-EPSERV-MIB", "epSpecificDtmfMapTimeoutEpId"),
)
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutEntry.setStatus("current")
_EpSpecificDtmfMapTimeoutEpId_Type = OctetString
_EpSpecificDtmfMapTimeoutEpId_Object = MibTableColumn
epSpecificDtmfMapTimeoutEpId = _EpSpecificDtmfMapTimeoutEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1, 100),
    _EpSpecificDtmfMapTimeoutEpId_Type()
)
epSpecificDtmfMapTimeoutEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutEpId.setStatus("current")


class _EpSpecificDtmfMapTimeoutEnableConfig_Type(MxEnableState):
    """Custom type epSpecificDtmfMapTimeoutEnableConfig based on MxEnableState"""
    defaultValue = 0


_EpSpecificDtmfMapTimeoutEnableConfig_Type.__name__ = "MxEnableState"
_EpSpecificDtmfMapTimeoutEnableConfig_Object = MibTableColumn
epSpecificDtmfMapTimeoutEnableConfig = _EpSpecificDtmfMapTimeoutEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1, 200),
    _EpSpecificDtmfMapTimeoutEnableConfig_Type()
)
epSpecificDtmfMapTimeoutEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutEnableConfig.setStatus("current")


class _EpSpecificDtmfMapTimeoutCompletion_Type(Unsigned32):
    """Custom type epSpecificDtmfMapTimeoutCompletion based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_EpSpecificDtmfMapTimeoutCompletion_Type.__name__ = "Unsigned32"
_EpSpecificDtmfMapTimeoutCompletion_Object = MibTableColumn
epSpecificDtmfMapTimeoutCompletion = _EpSpecificDtmfMapTimeoutCompletion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1, 300),
    _EpSpecificDtmfMapTimeoutCompletion_Type()
)
epSpecificDtmfMapTimeoutCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutCompletion.setStatus("current")


class _EpSpecificDtmfMapTimeoutFirstDtmf_Type(Unsigned32):
    """Custom type epSpecificDtmfMapTimeoutFirstDtmf based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_EpSpecificDtmfMapTimeoutFirstDtmf_Type.__name__ = "Unsigned32"
_EpSpecificDtmfMapTimeoutFirstDtmf_Object = MibTableColumn
epSpecificDtmfMapTimeoutFirstDtmf = _EpSpecificDtmfMapTimeoutFirstDtmf_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1, 400),
    _EpSpecificDtmfMapTimeoutFirstDtmf_Type()
)
epSpecificDtmfMapTimeoutFirstDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutFirstDtmf.setStatus("current")


class _EpSpecificDtmfMapTimeoutInterDtmf_Type(Unsigned32):
    """Custom type epSpecificDtmfMapTimeoutInterDtmf based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_EpSpecificDtmfMapTimeoutInterDtmf_Type.__name__ = "Unsigned32"
_EpSpecificDtmfMapTimeoutInterDtmf_Object = MibTableColumn
epSpecificDtmfMapTimeoutInterDtmf = _EpSpecificDtmfMapTimeoutInterDtmf_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 20000, 1000, 1, 500),
    _EpSpecificDtmfMapTimeoutInterDtmf_Type()
)
epSpecificDtmfMapTimeoutInterDtmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epSpecificDtmfMapTimeoutInterDtmf.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1700, 1, 60020, 100),
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
    "MX-EPSERV-MIB",
    **{"epServMIB": epServMIB,
       "epServMIBObjects": epServMIBObjects,
       "callGroup": callGroup,
       "defaultCallHookFlashProcessing": defaultCallHookFlashProcessing,
       "defaultCallAllowDirectIp": defaultCallAllowDirectIp,
       "epSpecificCallTable": epSpecificCallTable,
       "epSpecificCallEntry": epSpecificCallEntry,
       "epSpecificCallEpId": epSpecificCallEpId,
       "epSpecificCallEnableConfig": epSpecificCallEnableConfig,
       "epSpecificCallHookFlashProcessing": epSpecificCallHookFlashProcessing,
       "callDtmfMapGroup": callDtmfMapGroup,
       "callDtmfMapAllowedTable": callDtmfMapAllowedTable,
       "callDtmfMapAllowedEntry": callDtmfMapAllowedEntry,
       "callDtmfMapAllowedIndex": callDtmfMapAllowedIndex,
       "callDtmfMapAllowedEnable": callDtmfMapAllowedEnable,
       "callDtmfMapAllowedApplyTo": callDtmfMapAllowedApplyTo,
       "callDtmfMapAllowedEpId": callDtmfMapAllowedEpId,
       "callDtmfMapAllowedDtmfMap": callDtmfMapAllowedDtmfMap,
       "callDtmfMapAllowedDtmfTransformation": callDtmfMapAllowedDtmfTransformation,
       "callDtmfMapAllowedTargetHost": callDtmfMapAllowedTargetHost,
       "callDtmfMapAllowedEmergency": callDtmfMapAllowedEmergency,
       "callDtmfMapRefuseTable": callDtmfMapRefuseTable,
       "callDtmfMapRefuseEntry": callDtmfMapRefuseEntry,
       "callDtmfMapRefuseIndex": callDtmfMapRefuseIndex,
       "callDtmfMapRefuseEnable": callDtmfMapRefuseEnable,
       "callDtmfMapRefuseApplyTo": callDtmfMapRefuseApplyTo,
       "callDtmfMapRefuseEpId": callDtmfMapRefuseEpId,
       "callDtmfMapRefuseDtmfMap": callDtmfMapRefuseDtmfMap,
       "autoCallGroup": autoCallGroup,
       "defaultAutoCallEnable": defaultAutoCallEnable,
       "defaultAutoCallTargetAddress": defaultAutoCallTargetAddress,
       "epSpecificAutoCallTable": epSpecificAutoCallTable,
       "epSpecificAutoCallEntry": epSpecificAutoCallEntry,
       "epSpecificAutoCallEpId": epSpecificAutoCallEpId,
       "epSpecificAutoCallEnableConfig": epSpecificAutoCallEnableConfig,
       "epSpecificAutoCallEnable": epSpecificAutoCallEnable,
       "epSpecificAutoCallTargetAddress": epSpecificAutoCallTargetAddress,
       "holdGroup": holdGroup,
       "defaultHoldEnable": defaultHoldEnable,
       "epSpecificHoldTable": epSpecificHoldTable,
       "epSpecificHoldEntry": epSpecificHoldEntry,
       "epSpecificHoldEpId": epSpecificHoldEpId,
       "epSpecificHoldEnableConfig": epSpecificHoldEnableConfig,
       "epSpecificHoldEnable": epSpecificHoldEnable,
       "holdStatusTable": holdStatusTable,
       "holdStatusEntry": holdStatusEntry,
       "holdStatusEpId": holdStatusEpId,
       "holdStatusState": holdStatusState,
       "callWaitingGroup": callWaitingGroup,
       "defaultCallWaitingEnable": defaultCallWaitingEnable,
       "defaultCallWaitingCancelDtmfMap": defaultCallWaitingCancelDtmfMap,
       "defaultCallWaitingActivationDtmfMap": defaultCallWaitingActivationDtmfMap,
       "defaultCallWaitingDeactivationDtmfMap": defaultCallWaitingDeactivationDtmfMap,
       "epSpecificCallWaitingTable": epSpecificCallWaitingTable,
       "epSpecificCallWaitingEntry": epSpecificCallWaitingEntry,
       "epSpecificCallWaitingEpId": epSpecificCallWaitingEpId,
       "epSpecificCallWaitingEnableConfig": epSpecificCallWaitingEnableConfig,
       "epSpecificCallWaitingEnable": epSpecificCallWaitingEnable,
       "callWaitingStatusTable": callWaitingStatusTable,
       "callWaitingStatusEntry": callWaitingStatusEntry,
       "callWaitingStatusEpId": callWaitingStatusEpId,
       "callWaitingStatusState": callWaitingStatusState,
       "callWaitingUserConfigTable": callWaitingUserConfigTable,
       "callWaitingUserConfigEntry": callWaitingUserConfigEntry,
       "callWaitingUserConfigEpId": callWaitingUserConfigEpId,
       "callWaitingUserConfigState": callWaitingUserConfigState,
       "secondCallGroup": secondCallGroup,
       "defaultSecondCallEnable": defaultSecondCallEnable,
       "defaultSecondCallDisconnectAction": defaultSecondCallDisconnectAction,
       "epSpecificSecondCallTable": epSpecificSecondCallTable,
       "epSpecificSecondCallEntry": epSpecificSecondCallEntry,
       "epSpecificSecondCallEpId": epSpecificSecondCallEpId,
       "epSpecificSecondCallEnableConfig": epSpecificSecondCallEnableConfig,
       "epSpecificSecondCallEnable": epSpecificSecondCallEnable,
       "epSpecificSecondCallDisconnectAction": epSpecificSecondCallDisconnectAction,
       "secondCallStatusTable": secondCallStatusTable,
       "secondCallStatusEntry": secondCallStatusEntry,
       "secondCallStatusEpId": secondCallStatusEpId,
       "secondCallStatusState": secondCallStatusState,
       "transferGroup": transferGroup,
       "defaultTransferBlindEnable": defaultTransferBlindEnable,
       "defaultTransferAttendedEnable": defaultTransferAttendedEnable,
       "epSpecificTransferTable": epSpecificTransferTable,
       "epSpecificTransferEntry": epSpecificTransferEntry,
       "epSpecificTransferEpId": epSpecificTransferEpId,
       "epSpecificTransferEnableConfig": epSpecificTransferEnableConfig,
       "epSpecificTransferBlindEnable": epSpecificTransferBlindEnable,
       "epSpecificTransferAttendedEnable": epSpecificTransferAttendedEnable,
       "transferStatusTable": transferStatusTable,
       "transferStatusEntry": transferStatusEntry,
       "transferStatusEpId": transferStatusEpId,
       "transferStatusBlindState": transferStatusBlindState,
       "transferStatusAttendedState": transferStatusAttendedState,
       "conferenceGroup": conferenceGroup,
       "defaultConferenceEnable": defaultConferenceEnable,
       "defaultConferenceType": defaultConferenceType,
       "epSpecificConferenceTable": epSpecificConferenceTable,
       "epSpecificConferenceEntry": epSpecificConferenceEntry,
       "epSpecificConferenceEpId": epSpecificConferenceEpId,
       "epSpecificConferenceEnableConfig": epSpecificConferenceEnableConfig,
       "epSpecificConferenceEnable": epSpecificConferenceEnable,
       "epSpecificConferenceType": epSpecificConferenceType,
       "conferenceStatusTable": conferenceStatusTable,
       "conferenceStatusEntry": conferenceStatusEntry,
       "conferenceStatusEpId": conferenceStatusEpId,
       "conferenceStatusState": conferenceStatusState,
       "forwardGroup": forwardGroup,
       "forwardUnconditionalGroup": forwardUnconditionalGroup,
       "defaultForwardUnconditionalEnable": defaultForwardUnconditionalEnable,
       "defaultForwardUnconditionalDtmfMapActivation": defaultForwardUnconditionalDtmfMapActivation,
       "defaultForwardUnconditionalDtmfMapDeactivation": defaultForwardUnconditionalDtmfMapDeactivation,
       "epSpecificForwardUnconditionalTable": epSpecificForwardUnconditionalTable,
       "epSpecificForwardUnconditionalEntry": epSpecificForwardUnconditionalEntry,
       "epSpecificForwardUnconditionalEpId": epSpecificForwardUnconditionalEpId,
       "epSpecificForwardUnconditionalEnableConfig": epSpecificForwardUnconditionalEnableConfig,
       "epSpecificForwardUnconditionalEnable": epSpecificForwardUnconditionalEnable,
       "forwardUnconditionalConfigTable": forwardUnconditionalConfigTable,
       "forwardUnconditionalConfigEntry": forwardUnconditionalConfigEntry,
       "forwardUnconditionalConfigEpId": forwardUnconditionalConfigEpId,
       "forwardUnconditionalConfigActivation": forwardUnconditionalConfigActivation,
       "forwardUnconditionalConfigForwardingAddress": forwardUnconditionalConfigForwardingAddress,
       "forwardOnBusyGroup": forwardOnBusyGroup,
       "defaultForwardOnBusyEnable": defaultForwardOnBusyEnable,
       "defaultForwardOnBusyDtmfMapActivation": defaultForwardOnBusyDtmfMapActivation,
       "defaultForwardOnBusyDtmfMapDeactivation": defaultForwardOnBusyDtmfMapDeactivation,
       "epSpecificForwardOnBusyTable": epSpecificForwardOnBusyTable,
       "epSpecificForwardOnBusyEntry": epSpecificForwardOnBusyEntry,
       "epSpecificForwardOnBusyEpId": epSpecificForwardOnBusyEpId,
       "epSpecificForwardOnBusyEnableConfig": epSpecificForwardOnBusyEnableConfig,
       "epSpecificForwardOnBusyEnable": epSpecificForwardOnBusyEnable,
       "forwardOnBusyConfigTable": forwardOnBusyConfigTable,
       "forwardOnBusyConfigEntry": forwardOnBusyConfigEntry,
       "forwardOnBusyConfigEpId": forwardOnBusyConfigEpId,
       "forwardOnBusyConfigActivation": forwardOnBusyConfigActivation,
       "forwardOnBusyConfigForwardingAddress": forwardOnBusyConfigForwardingAddress,
       "forwardNoAnswerGroup": forwardNoAnswerGroup,
       "defaultForwardNoAnswerEnable": defaultForwardNoAnswerEnable,
       "defaultForwardNoAnswerTimeout": defaultForwardNoAnswerTimeout,
       "defaultForwardNoAnswerDtmfMapActivation": defaultForwardNoAnswerDtmfMapActivation,
       "defaultForwardNoAnswerDtmfMapDeactivation": defaultForwardNoAnswerDtmfMapDeactivation,
       "epSpecificForwardNoAnswerTable": epSpecificForwardNoAnswerTable,
       "epSpecificForwardNoAnswerEntry": epSpecificForwardNoAnswerEntry,
       "epSpecificForwardNoAnswerEpId": epSpecificForwardNoAnswerEpId,
       "epSpecificForwardNoAnswerEnableConfig": epSpecificForwardNoAnswerEnableConfig,
       "epSpecificForwardNoAnswerEnable": epSpecificForwardNoAnswerEnable,
       "epSpecificForwardNoAnswerTimeout": epSpecificForwardNoAnswerTimeout,
       "forwardNoAnswerConfigTable": forwardNoAnswerConfigTable,
       "forwardNoAnswerConfigEntry": forwardNoAnswerConfigEntry,
       "forwardNoAnswerConfigEpId": forwardNoAnswerConfigEpId,
       "forwardNoAnswerConfigActivation": forwardNoAnswerConfigActivation,
       "forwardNoAnswerConfigForwardingAddress": forwardNoAnswerConfigForwardingAddress,
       "callCompletionGroup": callCompletionGroup,
       "defaultCallCompletionBusySubscriberEnable": defaultCallCompletionBusySubscriberEnable,
       "defaultCallCompletionBusySubscriberDtmfMapActivation": defaultCallCompletionBusySubscriberDtmfMapActivation,
       "defaultCallCompletionNoReplyEnable": defaultCallCompletionNoReplyEnable,
       "defaultCallCompletionNoReplyDtmfMapActivation": defaultCallCompletionNoReplyDtmfMapActivation,
       "defaultCallCompletionDtmfMapDeactivation": defaultCallCompletionDtmfMapDeactivation,
       "defaultCallCompletionExpirationTimeout": defaultCallCompletionExpirationTimeout,
       "defaultCallCompletionMethod": defaultCallCompletionMethod,
       "defaultCallCompletionAutoReactivateEnable": defaultCallCompletionAutoReactivateEnable,
       "defaultCallCompletionAutoReactivateDelay": defaultCallCompletionAutoReactivateDelay,
       "defaultCallCompletionEarlyMediaBehaviour": defaultCallCompletionEarlyMediaBehaviour,
       "epSpecificCallCompletionTable": epSpecificCallCompletionTable,
       "epSpecificCallCompletionEntry": epSpecificCallCompletionEntry,
       "epSpecificCallCompletionEpId": epSpecificCallCompletionEpId,
       "epSpecificCallCompletionEnableConfig": epSpecificCallCompletionEnableConfig,
       "epSpecificCallCompletionBusySubscriberEnable": epSpecificCallCompletionBusySubscriberEnable,
       "epSpecificCallCompletionNoReplyEnable": epSpecificCallCompletionNoReplyEnable,
       "callCompletionConfigTable": callCompletionConfigTable,
       "callCompletionConfigEntry": callCompletionConfigEntry,
       "callCompletionConfigIndex": callCompletionConfigIndex,
       "callCompletionConfigEpId": callCompletionConfigEpId,
       "callCompletionConfigType": callCompletionConfigType,
       "callCompletionConfigTargetAddress": callCompletionConfigTargetAddress,
       "callCompletionConfigTargetState": callCompletionConfigTargetState,
       "callCompletionPollingGroup": callCompletionPollingGroup,
       "defaultCallCompletionPollingInterval": defaultCallCompletionPollingInterval,
       "delayedHotlineGroup": delayedHotlineGroup,
       "defaultDelayedHotlineEnable": defaultDelayedHotlineEnable,
       "defaultDelayedHotlineCondition": defaultDelayedHotlineCondition,
       "defaultDelayedHotlineTargetAddress": defaultDelayedHotlineTargetAddress,
       "epSpecificDelayedHotlineTable": epSpecificDelayedHotlineTable,
       "epSpecificDelayedHotlineEntry": epSpecificDelayedHotlineEntry,
       "epSpecificDelayedHotlineEpId": epSpecificDelayedHotlineEpId,
       "epSpecificDelayedHotlineEnableConfig": epSpecificDelayedHotlineEnableConfig,
       "epSpecificDelayedHotlineEnable": epSpecificDelayedHotlineEnable,
       "epSpecificDelayedHotlineCondition": epSpecificDelayedHotlineCondition,
       "epSpecificDelayedHotlineTargetAddress": epSpecificDelayedHotlineTargetAddress,
       "statisticsGroup": statisticsGroup,
       "callStatisticsTable": callStatisticsTable,
       "callStatisticsEntry": callStatisticsEntry,
       "callStatisticsEpId": callStatisticsEpId,
       "callStatisticsIncomingCallsReceived": callStatisticsIncomingCallsReceived,
       "callStatisticsIncomingCallsAnswered": callStatisticsIncomingCallsAnswered,
       "callStatisticsIncomingCallsConnected": callStatisticsIncomingCallsConnected,
       "callStatisticsIncomingCallsFailed": callStatisticsIncomingCallsFailed,
       "callStatisticsOutgoingCallsAttempted": callStatisticsOutgoingCallsAttempted,
       "callStatisticsOutgoingCallsAnswered": callStatisticsOutgoingCallsAnswered,
       "callStatisticsOutgoingCallsConnected": callStatisticsOutgoingCallsConnected,
       "callStatisticsOutgoingCallsFailed": callStatisticsOutgoingCallsFailed,
       "callStatisticsCallsDropped": callStatisticsCallsDropped,
       "callStatisticsTotalCallTime": callStatisticsTotalCallTime,
       "callStatisticsReset": callStatisticsReset,
       "dtmfMapGroup": dtmfMapGroup,
       "dtmfMapTimeoutCompletion": dtmfMapTimeoutCompletion,
       "dtmfMapTimeoutFirstDtmf": dtmfMapTimeoutFirstDtmf,
       "dtmfMapTimeoutInterDtmf": dtmfMapTimeoutInterDtmf,
       "epSpecificDtmfMapTimeoutTable": epSpecificDtmfMapTimeoutTable,
       "epSpecificDtmfMapTimeoutEntry": epSpecificDtmfMapTimeoutEntry,
       "epSpecificDtmfMapTimeoutEpId": epSpecificDtmfMapTimeoutEpId,
       "epSpecificDtmfMapTimeoutEnableConfig": epSpecificDtmfMapTimeoutEnableConfig,
       "epSpecificDtmfMapTimeoutCompletion": epSpecificDtmfMapTimeoutCompletion,
       "epSpecificDtmfMapTimeoutFirstDtmf": epSpecificDtmfMapTimeoutFirstDtmf,
       "epSpecificDtmfMapTimeoutInterDtmf": epSpecificDtmfMapTimeoutInterDtmf,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
