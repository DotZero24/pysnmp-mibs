# SNMP MIB module (CONVERTOR-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/CONVERTOR-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:56 2025
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

(iscomMediaConvertor,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomMediaConvertor")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

rcmcVlanConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcmcVlanCoreTagType_Type(Integer32):
    """Custom type rcmcVlanCoreTagType based on Integer32"""
    defaultValue = 37120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcmcVlanCoreTagType_Type.__name__ = "Integer32"
_RcmcVlanCoreTagType_Object = MibScalar
rcmcVlanCoreTagType = _RcmcVlanCoreTagType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 1),
    _RcmcVlanCoreTagType_Type()
)
rcmcVlanCoreTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanCoreTagType.setStatus("current")


class _RcmcVlanSwitchMode_Type(Integer32):
    """Custom type rcmcVlanSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("dot1q-vlan", 2),
          ("double-tagged-vlan", 3))
    )


_RcmcVlanSwitchMode_Type.__name__ = "Integer32"
_RcmcVlanSwitchMode_Object = MibScalar
rcmcVlanSwitchMode = _RcmcVlanSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 2),
    _RcmcVlanSwitchMode_Type()
)
rcmcVlanSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanSwitchMode.setStatus("current")
_RcmcVlanPortConfigTable_Object = MibTable
rcmcVlanPortConfigTable = _RcmcVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rcmcVlanPortConfigTable.setStatus("current")
_RcmcVlanPortConfigEntry_Object = MibTableRow
rcmcVlanPortConfigEntry = _RcmcVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1)
)
rcmcVlanPortConfigEntry.setIndexNames(
    (0, "CONVERTOR-VLAN-MIB", "rcmcVlanPortIndex"),
)
if mibBuilder.loadTexts:
    rcmcVlanPortConfigEntry.setStatus("current")
_RcmcVlanPortIndex_Type = Integer32
_RcmcVlanPortIndex_Object = MibTableColumn
rcmcVlanPortIndex = _RcmcVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 1),
    _RcmcVlanPortIndex_Type()
)
rcmcVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcmcVlanPortIndex.setStatus("current")


class _RcmcVlanNative_Type(Integer32):
    """Custom type rcmcVlanNative based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcmcVlanNative_Type.__name__ = "Integer32"
_RcmcVlanNative_Object = MibTableColumn
rcmcVlanNative = _RcmcVlanNative_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 2),
    _RcmcVlanNative_Type()
)
rcmcVlanNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanNative.setStatus("current")


class _RcmcVlanNativeOverride_Type(EnableVar):
    """Custom type rcmcVlanNativeOverride based on EnableVar"""
    defaultValue = 2


_RcmcVlanNativeOverride_Type.__name__ = "EnableVar"
_RcmcVlanNativeOverride_Object = MibTableColumn
rcmcVlanNativeOverride = _RcmcVlanNativeOverride_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 3),
    _RcmcVlanNativeOverride_Type()
)
rcmcVlanNativeOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanNativeOverride.setStatus("current")


class _RcmcVlanDoubleTagEnable_Type(EnableVar):
    """Custom type rcmcVlanDoubleTagEnable based on EnableVar"""
    defaultValue = 2


_RcmcVlanDoubleTagEnable_Type.__name__ = "EnableVar"
_RcmcVlanDoubleTagEnable_Object = MibTableColumn
rcmcVlanDoubleTagEnable = _RcmcVlanDoubleTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 4),
    _RcmcVlanDoubleTagEnable_Type()
)
rcmcVlanDoubleTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanDoubleTagEnable.setStatus("current")


class _RcmcVlanIngressFilter_Type(Integer32):
    """Custom type rcmcVlanIngressFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("notmember", 2),
          ("unkown", 3))
    )


_RcmcVlanIngressFilter_Type.__name__ = "Integer32"
_RcmcVlanIngressFilter_Object = MibTableColumn
rcmcVlanIngressFilter = _RcmcVlanIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 5),
    _RcmcVlanIngressFilter_Type()
)
rcmcVlanIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanIngressFilter.setStatus("current")


class _RcmcVlanAcceptFrameType_Type(Integer32):
    """Custom type rcmcVlanAcceptFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tag", 2),
          ("untag", 3))
    )


_RcmcVlanAcceptFrameType_Type.__name__ = "Integer32"
_RcmcVlanAcceptFrameType_Object = MibTableColumn
rcmcVlanAcceptFrameType = _RcmcVlanAcceptFrameType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 6),
    _RcmcVlanAcceptFrameType_Type()
)
rcmcVlanAcceptFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanAcceptFrameType.setStatus("current")


class _RcmcVlanEgressDefault_Type(Integer32):
    """Custom type rcmcVlanEgressDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unmodify", 1),
          ("tag", 2),
          ("untag", 3),
          ("disable", 4))
    )


_RcmcVlanEgressDefault_Type.__name__ = "Integer32"
_RcmcVlanEgressDefault_Object = MibTableColumn
rcmcVlanEgressDefault = _RcmcVlanEgressDefault_Object(
    (1, 3, 6, 1, 4, 1, 8886, 16, 1, 2, 3, 1, 7),
    _RcmcVlanEgressDefault_Type()
)
rcmcVlanEgressDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmcVlanEgressDefault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONVERTOR-VLAN-MIB",
    **{"rcmcVlanConfig": rcmcVlanConfig,
       "rcmcVlanCoreTagType": rcmcVlanCoreTagType,
       "rcmcVlanSwitchMode": rcmcVlanSwitchMode,
       "rcmcVlanPortConfigTable": rcmcVlanPortConfigTable,
       "rcmcVlanPortConfigEntry": rcmcVlanPortConfigEntry,
       "rcmcVlanPortIndex": rcmcVlanPortIndex,
       "rcmcVlanNative": rcmcVlanNative,
       "rcmcVlanNativeOverride": rcmcVlanNativeOverride,
       "rcmcVlanDoubleTagEnable": rcmcVlanDoubleTagEnable,
       "rcmcVlanIngressFilter": rcmcVlanIngressFilter,
       "rcmcVlanAcceptFrameType": rcmcVlanAcceptFrameType,
       "rcmcVlanEgressDefault": rcmcVlanEgressDefault}
)
