# SNMP MIB module (IPAD-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zhone/IPAD-ROUTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:15 2025
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

(ipad,) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipad")

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


# MODULE-IDENTITY

ipadRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadCircuitParms_ObjectIdentity = ObjectIdentity
ipadCircuitParms = _IpadCircuitParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1)
)
_IpadCircuitTable_Object = MibTable
ipadCircuitTable = _IpadCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ipadCircuitTable.setStatus("current")
_IpadCircuitTableEntry_Object = MibTableRow
ipadCircuitTableEntry = _IpadCircuitTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1)
)
ipadCircuitTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadCircuitIndex"),
)
if mibBuilder.loadTexts:
    ipadCircuitTableEntry.setStatus("current")
_IpadCircuitIndex_Type = Integer32
_IpadCircuitIndex_Object = MibTableColumn
ipadCircuitIndex = _IpadCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 1),
    _IpadCircuitIndex_Type()
)
ipadCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadCircuitIndex.setStatus("current")
_IpadCircuitEndpoint_Type = DisplayString
_IpadCircuitEndpoint_Object = MibTableColumn
ipadCircuitEndpoint = _IpadCircuitEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 2),
    _IpadCircuitEndpoint_Type()
)
ipadCircuitEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEndpoint.setStatus("current")
_IpadCircuitIpAddress_Type = IpAddress
_IpadCircuitIpAddress_Object = MibTableColumn
ipadCircuitIpAddress = _IpadCircuitIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 3),
    _IpadCircuitIpAddress_Type()
)
ipadCircuitIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitIpAddress.setStatus("current")
_IpadCircuitIpMask_Type = IpAddress
_IpadCircuitIpMask_Object = MibTableColumn
ipadCircuitIpMask = _IpadCircuitIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 4),
    _IpadCircuitIpMask_Type()
)
ipadCircuitIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitIpMask.setStatus("current")


class _IpadCircuitMaxTransmitUnit_Type(Integer32):
    """Custom type ipadCircuitMaxTransmitUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitMaxTransmitUnit_Type.__name__ = "Integer32"
_IpadCircuitMaxTransmitUnit_Object = MibTableColumn
ipadCircuitMaxTransmitUnit = _IpadCircuitMaxTransmitUnit_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 5),
    _IpadCircuitMaxTransmitUnit_Type()
)
ipadCircuitMaxTransmitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitMaxTransmitUnit.setStatus("current")


class _IpadCircuitCost_Type(Integer32):
    """Custom type ipadCircuitCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitCost_Type.__name__ = "Integer32"
_IpadCircuitCost_Object = MibTableColumn
ipadCircuitCost = _IpadCircuitCost_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 6),
    _IpadCircuitCost_Type()
)
ipadCircuitCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitCost.setStatus("current")


class _IpadCircuitEnableRIP_Type(Integer32):
    """Custom type ipadCircuitEnableRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3),
          ("talkOnly", 4),
          ("listenOnly", 5))
    )


_IpadCircuitEnableRIP_Type.__name__ = "Integer32"
_IpadCircuitEnableRIP_Object = MibTableColumn
ipadCircuitEnableRIP = _IpadCircuitEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 7),
    _IpadCircuitEnableRIP_Type()
)
ipadCircuitEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableRIP.setStatus("current")


class _IpadCircuitEnableOSPF_Type(Integer32):
    """Custom type ipadCircuitEnableOSPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadCircuitEnableOSPF_Type.__name__ = "Integer32"
_IpadCircuitEnableOSPF_Object = MibTableColumn
ipadCircuitEnableOSPF = _IpadCircuitEnableOSPF_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 8),
    _IpadCircuitEnableOSPF_Type()
)
ipadCircuitEnableOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableOSPF.setStatus("current")


class _IpadCircuitEnableMulticast_Type(Integer32):
    """Custom type ipadCircuitEnableMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadCircuitEnableMulticast_Type.__name__ = "Integer32"
_IpadCircuitEnableMulticast_Object = MibTableColumn
ipadCircuitEnableMulticast = _IpadCircuitEnableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 9),
    _IpadCircuitEnableMulticast_Type()
)
ipadCircuitEnableMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitEnableMulticast.setStatus("current")


class _IpadCircuitOSPFArea_Type(Integer32):
    """Custom type ipadCircuitOSPFArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpadCircuitOSPFArea_Type.__name__ = "Integer32"
_IpadCircuitOSPFArea_Object = MibTableColumn
ipadCircuitOSPFArea = _IpadCircuitOSPFArea_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 10),
    _IpadCircuitOSPFArea_Type()
)
ipadCircuitOSPFArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFArea.setStatus("current")


class _IpadCircuitOSPFLSATimer_Type(Integer32):
    """Custom type ipadCircuitOSPFLSATimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpadCircuitOSPFLSATimer_Type.__name__ = "Integer32"
_IpadCircuitOSPFLSATimer_Object = MibTableColumn
ipadCircuitOSPFLSATimer = _IpadCircuitOSPFLSATimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 11),
    _IpadCircuitOSPFLSATimer_Type()
)
ipadCircuitOSPFLSATimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFLSATimer.setStatus("current")


class _IpadCircuitOSPFLSUDelay_Type(Integer32):
    """Custom type ipadCircuitOSPFLSUDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_IpadCircuitOSPFLSUDelay_Type.__name__ = "Integer32"
_IpadCircuitOSPFLSUDelay_Object = MibTableColumn
ipadCircuitOSPFLSUDelay = _IpadCircuitOSPFLSUDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 12),
    _IpadCircuitOSPFLSUDelay_Type()
)
ipadCircuitOSPFLSUDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFLSUDelay.setStatus("current")


class _IpadCircuitOSPFRouterPriority_Type(Integer32):
    """Custom type ipadCircuitOSPFRouterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpadCircuitOSPFRouterPriority_Type.__name__ = "Integer32"
_IpadCircuitOSPFRouterPriority_Object = MibTableColumn
ipadCircuitOSPFRouterPriority = _IpadCircuitOSPFRouterPriority_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 13),
    _IpadCircuitOSPFRouterPriority_Type()
)
ipadCircuitOSPFRouterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFRouterPriority.setStatus("current")


class _IpadCircuitOSPFHelloInterval_Type(Integer32):
    """Custom type ipadCircuitOSPFHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitOSPFHelloInterval_Type.__name__ = "Integer32"
_IpadCircuitOSPFHelloInterval_Object = MibTableColumn
ipadCircuitOSPFHelloInterval = _IpadCircuitOSPFHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 14),
    _IpadCircuitOSPFHelloInterval_Type()
)
ipadCircuitOSPFHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFHelloInterval.setStatus("current")


class _IpadCircuitOSPFDeadInterval_Type(Integer32):
    """Custom type ipadCircuitOSPFDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadCircuitOSPFDeadInterval_Type.__name__ = "Integer32"
_IpadCircuitOSPFDeadInterval_Object = MibTableColumn
ipadCircuitOSPFDeadInterval = _IpadCircuitOSPFDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 15),
    _IpadCircuitOSPFDeadInterval_Type()
)
ipadCircuitOSPFDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFDeadInterval.setStatus("current")
_IpadCircuitOSPFAuthKey_Type = DisplayString
_IpadCircuitOSPFAuthKey_Object = MibTableColumn
ipadCircuitOSPFAuthKey = _IpadCircuitOSPFAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 16),
    _IpadCircuitOSPFAuthKey_Type()
)
ipadCircuitOSPFAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitOSPFAuthKey.setStatus("current")


class _IpadCircuitAdd_Type(Integer32):
    """Custom type ipadCircuitAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("addnew", 2))
    )


_IpadCircuitAdd_Type.__name__ = "Integer32"
_IpadCircuitAdd_Object = MibScalar
ipadCircuitAdd = _IpadCircuitAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 2),
    _IpadCircuitAdd_Type()
)
ipadCircuitAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitAdd.setStatus("current")
_IpadCircuitDelete_Type = Integer32
_IpadCircuitDelete_Object = MibScalar
ipadCircuitDelete = _IpadCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 3),
    _IpadCircuitDelete_Type()
)
ipadCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadCircuitDelete.setStatus("current")
_IpadRIPParms_ObjectIdentity = ObjectIdentity
ipadRIPParms = _IpadRIPParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2)
)


class _IpadRIPEnable_Type(Integer32):
    """Custom type ipadRIPEnable based on Integer32"""
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
        *(("other", 1),
          ("disabled", 2),
          ("enabledRIP1", 3),
          ("enabledRIP2", 4))
    )


_IpadRIPEnable_Type.__name__ = "Integer32"
_IpadRIPEnable_Object = MibScalar
ipadRIPEnable = _IpadRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 1),
    _IpadRIPEnable_Type()
)
ipadRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPEnable.setStatus("current")


class _IpadRIPTrustNeighbors_Type(Integer32):
    """Custom type ipadRIPTrustNeighbors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadRIPTrustNeighbors_Type.__name__ = "Integer32"
_IpadRIPTrustNeighbors_Object = MibScalar
ipadRIPTrustNeighbors = _IpadRIPTrustNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 2),
    _IpadRIPTrustNeighbors_Type()
)
ipadRIPTrustNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPTrustNeighbors.setStatus("current")


class _IpadRIPInterval_Type(Integer32):
    """Custom type ipadRIPInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPInterval_Type.__name__ = "Integer32"
_IpadRIPInterval_Object = MibScalar
ipadRIPInterval = _IpadRIPInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 3),
    _IpadRIPInterval_Type()
)
ipadRIPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPInterval.setStatus("current")


class _IpadRIPDomain_Type(Integer32):
    """Custom type ipadRIPDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPDomain_Type.__name__ = "Integer32"
_IpadRIPDomain_Object = MibScalar
ipadRIPDomain = _IpadRIPDomain_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 4),
    _IpadRIPDomain_Type()
)
ipadRIPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPDomain.setStatus("current")
_IpadRIPStaticARPTable_Object = MibTable
ipadRIPStaticARPTable = _IpadRIPStaticARPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5)
)
if mibBuilder.loadTexts:
    ipadRIPStaticARPTable.setStatus("current")
_IpadRIPStaticARPTableEntry_Object = MibTableRow
ipadRIPStaticARPTableEntry = _IpadRIPStaticARPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1)
)
ipadRIPStaticARPTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPStaticARPIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPStaticARPTableEntry.setStatus("current")
_IpadRIPStaticARPIndex_Type = Integer32
_IpadRIPStaticARPIndex_Object = MibTableColumn
ipadRIPStaticARPIndex = _IpadRIPStaticARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 1),
    _IpadRIPStaticARPIndex_Type()
)
ipadRIPStaticARPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPStaticARPIndex.setStatus("current")
_IpadRIPStaticARPEndpoint_Type = DisplayString
_IpadRIPStaticARPEndpoint_Object = MibTableColumn
ipadRIPStaticARPEndpoint = _IpadRIPStaticARPEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 2),
    _IpadRIPStaticARPEndpoint_Type()
)
ipadRIPStaticARPEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPEndpoint.setStatus("current")
_IpadRIPStaticARPIpAddress_Type = IpAddress
_IpadRIPStaticARPIpAddress_Object = MibTableColumn
ipadRIPStaticARPIpAddress = _IpadRIPStaticARPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 3),
    _IpadRIPStaticARPIpAddress_Type()
)
ipadRIPStaticARPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPIpAddress.setStatus("current")
_IpadRIPStaticARPMacAddress_Type = DisplayString
_IpadRIPStaticARPMacAddress_Object = MibTableColumn
ipadRIPStaticARPMacAddress = _IpadRIPStaticARPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 4),
    _IpadRIPStaticARPMacAddress_Type()
)
ipadRIPStaticARPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPMacAddress.setStatus("current")
_IpadRIPStaticARPDLCIAddress_Type = Integer32
_IpadRIPStaticARPDLCIAddress_Object = MibTableColumn
ipadRIPStaticARPDLCIAddress = _IpadRIPStaticARPDLCIAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 5),
    _IpadRIPStaticARPDLCIAddress_Type()
)
ipadRIPStaticARPDLCIAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPDLCIAddress.setStatus("current")


class _IpadRIPStaticARPEnableARP_Type(Integer32):
    """Custom type ipadRIPStaticARPEnableARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadRIPStaticARPEnableARP_Type.__name__ = "Integer32"
_IpadRIPStaticARPEnableARP_Object = MibTableColumn
ipadRIPStaticARPEnableARP = _IpadRIPStaticARPEnableARP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 6),
    _IpadRIPStaticARPEnableARP_Type()
)
ipadRIPStaticARPEnableARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPEnableARP.setStatus("current")


class _IpadRIPStaticARPAdd_Type(Integer32):
    """Custom type ipadRIPStaticARPAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("addnew", 2))
    )


_IpadRIPStaticARPAdd_Type.__name__ = "Integer32"
_IpadRIPStaticARPAdd_Object = MibScalar
ipadRIPStaticARPAdd = _IpadRIPStaticARPAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 6),
    _IpadRIPStaticARPAdd_Type()
)
ipadRIPStaticARPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPAdd.setStatus("current")
_IpadRIPStaticARPDelete_Type = Integer32
_IpadRIPStaticARPDelete_Object = MibScalar
ipadRIPStaticARPDelete = _IpadRIPStaticARPDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 7),
    _IpadRIPStaticARPDelete_Type()
)
ipadRIPStaticARPDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticARPDelete.setStatus("current")
_IpadRIPStaticRouteTable_Object = MibTable
ipadRIPStaticRouteTable = _IpadRIPStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8)
)
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTable.setStatus("current")
_IpadRIPStaticRouteTableEntry_Object = MibTableRow
ipadRIPStaticRouteTableEntry = _IpadRIPStaticRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1)
)
ipadRIPStaticRouteTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTableEntry.setStatus("current")
_IpadRIPStaticRouteIndex_Type = Integer32
_IpadRIPStaticRouteIndex_Object = MibTableColumn
ipadRIPStaticRouteIndex = _IpadRIPStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 1),
    _IpadRIPStaticRouteIndex_Type()
)
ipadRIPStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteIndex.setStatus("current")
_IpadRIPStaticRouteEndpoint_Type = DisplayString
_IpadRIPStaticRouteEndpoint_Object = MibTableColumn
ipadRIPStaticRouteEndpoint = _IpadRIPStaticRouteEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 2),
    _IpadRIPStaticRouteEndpoint_Type()
)
ipadRIPStaticRouteEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteEndpoint.setStatus("current")
_IpadRIPStaticRouteTargetIpAddress_Type = IpAddress
_IpadRIPStaticRouteTargetIpAddress_Object = MibTableColumn
ipadRIPStaticRouteTargetIpAddress = _IpadRIPStaticRouteTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 3),
    _IpadRIPStaticRouteTargetIpAddress_Type()
)
ipadRIPStaticRouteTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTargetIpAddress.setStatus("current")
_IpadRIPStaticRouteTargetIpMask_Type = IpAddress
_IpadRIPStaticRouteTargetIpMask_Object = MibTableColumn
ipadRIPStaticRouteTargetIpMask = _IpadRIPStaticRouteTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 4),
    _IpadRIPStaticRouteTargetIpMask_Type()
)
ipadRIPStaticRouteTargetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteTargetIpMask.setStatus("current")
_IpadRIPStaticRouteNextHopIpAddress_Type = IpAddress
_IpadRIPStaticRouteNextHopIpAddress_Object = MibTableColumn
ipadRIPStaticRouteNextHopIpAddress = _IpadRIPStaticRouteNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 5),
    _IpadRIPStaticRouteNextHopIpAddress_Type()
)
ipadRIPStaticRouteNextHopIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteNextHopIpAddress.setStatus("current")


class _IpadRIPStaticRouteCost_Type(Integer32):
    """Custom type ipadRIPStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpadRIPStaticRouteCost_Type.__name__ = "Integer32"
_IpadRIPStaticRouteCost_Object = MibTableColumn
ipadRIPStaticRouteCost = _IpadRIPStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 6),
    _IpadRIPStaticRouteCost_Type()
)
ipadRIPStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteCost.setStatus("current")


class _IpadRIPStaticRouteEnableRouter_Type(Integer32):
    """Custom type ipadRIPStaticRouteEnableRouter based on Integer32"""
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
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("enableAndAdvertize", 4))
    )


_IpadRIPStaticRouteEnableRouter_Type.__name__ = "Integer32"
_IpadRIPStaticRouteEnableRouter_Object = MibTableColumn
ipadRIPStaticRouteEnableRouter = _IpadRIPStaticRouteEnableRouter_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 7),
    _IpadRIPStaticRouteEnableRouter_Type()
)
ipadRIPStaticRouteEnableRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteEnableRouter.setStatus("current")


class _IpadRIPStaticRouteAdd_Type(Integer32):
    """Custom type ipadRIPStaticRouteAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("addnew", 2))
    )


_IpadRIPStaticRouteAdd_Type.__name__ = "Integer32"
_IpadRIPStaticRouteAdd_Object = MibScalar
ipadRIPStaticRouteAdd = _IpadRIPStaticRouteAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 9),
    _IpadRIPStaticRouteAdd_Type()
)
ipadRIPStaticRouteAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteAdd.setStatus("current")
_IpadRIPStaticRouteDelete_Type = Integer32
_IpadRIPStaticRouteDelete_Object = MibScalar
ipadRIPStaticRouteDelete = _IpadRIPStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 10),
    _IpadRIPStaticRouteDelete_Type()
)
ipadRIPStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPStaticRouteDelete.setStatus("current")
_IpadRIPNeighborTable_Object = MibTable
ipadRIPNeighborTable = _IpadRIPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11)
)
if mibBuilder.loadTexts:
    ipadRIPNeighborTable.setStatus("current")
_IpadRIPNeighborTableEntry_Object = MibTableRow
ipadRIPNeighborTableEntry = _IpadRIPNeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1)
)
ipadRIPNeighborTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadRIPNeighborIndex"),
)
if mibBuilder.loadTexts:
    ipadRIPNeighborTableEntry.setStatus("current")
_IpadRIPNeighborIndex_Type = Integer32
_IpadRIPNeighborIndex_Object = MibTableColumn
ipadRIPNeighborIndex = _IpadRIPNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 1),
    _IpadRIPNeighborIndex_Type()
)
ipadRIPNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPNeighborIndex.setStatus("current")
_IpadRIPNeighborAddress_Type = IpAddress
_IpadRIPNeighborAddress_Object = MibTableColumn
ipadRIPNeighborAddress = _IpadRIPNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 2),
    _IpadRIPNeighborAddress_Type()
)
ipadRIPNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadRIPNeighborAddress.setStatus("current")
_IpadRIPNeighborAdd_Type = IpAddress
_IpadRIPNeighborAdd_Object = MibScalar
ipadRIPNeighborAdd = _IpadRIPNeighborAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 12),
    _IpadRIPNeighborAdd_Type()
)
ipadRIPNeighborAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPNeighborAdd.setStatus("current")
_IpadRIPNeighborDelete_Type = IpAddress
_IpadRIPNeighborDelete_Object = MibScalar
ipadRIPNeighborDelete = _IpadRIPNeighborDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 13),
    _IpadRIPNeighborDelete_Type()
)
ipadRIPNeighborDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadRIPNeighborDelete.setStatus("current")
_IpadOSPFParms_ObjectIdentity = ObjectIdentity
ipadOSPFParms = _IpadOSPFParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3)
)


class _IpadOSPFEnable_Type(Integer32):
    """Custom type ipadOSPFEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadOSPFEnable_Type.__name__ = "Integer32"
_IpadOSPFEnable_Object = MibScalar
ipadOSPFEnable = _IpadOSPFEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 1),
    _IpadOSPFEnable_Type()
)
ipadOSPFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFEnable.setStatus("current")
_IpadOSPFRouterID_Type = IpAddress
_IpadOSPFRouterID_Object = MibScalar
ipadOSPFRouterID = _IpadOSPFRouterID_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 2),
    _IpadOSPFRouterID_Type()
)
ipadOSPFRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFRouterID.setStatus("current")
_IpadOSPFAreaTable_Object = MibTable
ipadOSPFAreaTable = _IpadOSPFAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3)
)
if mibBuilder.loadTexts:
    ipadOSPFAreaTable.setStatus("current")
_IpadOSPFAreaTableEntry_Object = MibTableRow
ipadOSPFAreaTableEntry = _IpadOSPFAreaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1)
)
ipadOSPFAreaTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadOSPFAreaIndex"),
)
if mibBuilder.loadTexts:
    ipadOSPFAreaTableEntry.setStatus("current")
_IpadOSPFAreaIndex_Type = Integer32
_IpadOSPFAreaIndex_Object = MibTableColumn
ipadOSPFAreaIndex = _IpadOSPFAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 1),
    _IpadOSPFAreaIndex_Type()
)
ipadOSPFAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOSPFAreaIndex.setStatus("current")
_IpadOSPFAreaID_Type = IpAddress
_IpadOSPFAreaID_Object = MibTableColumn
ipadOSPFAreaID = _IpadOSPFAreaID_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 2),
    _IpadOSPFAreaID_Type()
)
ipadOSPFAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaID.setStatus("current")


class _IpadOSPFAreaEnable_Type(Integer32):
    """Custom type ipadOSPFAreaEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadOSPFAreaEnable_Type.__name__ = "Integer32"
_IpadOSPFAreaEnable_Object = MibTableColumn
ipadOSPFAreaEnable = _IpadOSPFAreaEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 3),
    _IpadOSPFAreaEnable_Type()
)
ipadOSPFAreaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaEnable.setStatus("current")


class _IpadOSPFAreaAuthType_Type(Integer32):
    """Custom type ipadOSPFAreaAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2))
    )


_IpadOSPFAreaAuthType_Type.__name__ = "Integer32"
_IpadOSPFAreaAuthType_Object = MibTableColumn
ipadOSPFAreaAuthType = _IpadOSPFAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 4),
    _IpadOSPFAreaAuthType_Type()
)
ipadOSPFAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaAuthType.setStatus("current")


class _IpadOSPFAreaStub_Type(Integer32):
    """Custom type ipadOSPFAreaStub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("no", 2),
          ("yes", 3))
    )


_IpadOSPFAreaStub_Type.__name__ = "Integer32"
_IpadOSPFAreaStub_Object = MibTableColumn
ipadOSPFAreaStub = _IpadOSPFAreaStub_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 5),
    _IpadOSPFAreaStub_Type()
)
ipadOSPFAreaStub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaStub.setStatus("current")
_IpadOSPFAreaAddrSummary_Type = IpAddress
_IpadOSPFAreaAddrSummary_Object = MibTableColumn
ipadOSPFAreaAddrSummary = _IpadOSPFAreaAddrSummary_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 6),
    _IpadOSPFAreaAddrSummary_Type()
)
ipadOSPFAreaAddrSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaAddrSummary.setStatus("current")
_IpadOSPFAreaMaskSummary_Type = IpAddress
_IpadOSPFAreaMaskSummary_Object = MibTableColumn
ipadOSPFAreaMaskSummary = _IpadOSPFAreaMaskSummary_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 7),
    _IpadOSPFAreaMaskSummary_Type()
)
ipadOSPFAreaMaskSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaMaskSummary.setStatus("current")


class _IpadOSPFAreaAdvertise_Type(Integer32):
    """Custom type ipadOSPFAreaAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadOSPFAreaAdvertise_Type.__name__ = "Integer32"
_IpadOSPFAreaAdvertise_Object = MibTableColumn
ipadOSPFAreaAdvertise = _IpadOSPFAreaAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 3, 1, 8),
    _IpadOSPFAreaAdvertise_Type()
)
ipadOSPFAreaAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaAdvertise.setStatus("current")


class _IpadOSPFAreaAdd_Type(Integer32):
    """Custom type ipadOSPFAreaAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("addnew", 2))
    )


_IpadOSPFAreaAdd_Type.__name__ = "Integer32"
_IpadOSPFAreaAdd_Object = MibScalar
ipadOSPFAreaAdd = _IpadOSPFAreaAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 4),
    _IpadOSPFAreaAdd_Type()
)
ipadOSPFAreaAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaAdd.setStatus("current")
_IpadOSPFAreaDelete_Type = Integer32
_IpadOSPFAreaDelete_Object = MibScalar
ipadOSPFAreaDelete = _IpadOSPFAreaDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 5),
    _IpadOSPFAreaDelete_Type()
)
ipadOSPFAreaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFAreaDelete.setStatus("current")
_IpadOSPFVlinkTable_Object = MibTable
ipadOSPFVlinkTable = _IpadOSPFVlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6)
)
if mibBuilder.loadTexts:
    ipadOSPFVlinkTable.setStatus("current")
_IpadOSPFVlinkTableEntry_Object = MibTableRow
ipadOSPFVlinkTableEntry = _IpadOSPFVlinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6, 1)
)
ipadOSPFVlinkTableEntry.setIndexNames(
    (0, "IPAD-ROUTER-MIB", "ipadOSPFVlinkIndex"),
)
if mibBuilder.loadTexts:
    ipadOSPFVlinkTableEntry.setStatus("current")
_IpadOSPFVlinkIndex_Type = Integer32
_IpadOSPFVlinkIndex_Object = MibTableColumn
ipadOSPFVlinkIndex = _IpadOSPFVlinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6, 1, 1),
    _IpadOSPFVlinkIndex_Type()
)
ipadOSPFVlinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOSPFVlinkIndex.setStatus("current")


class _IpadOSPFVlinkEnable_Type(Integer32):
    """Custom type ipadOSPFVlinkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_IpadOSPFVlinkEnable_Type.__name__ = "Integer32"
_IpadOSPFVlinkEnable_Object = MibTableColumn
ipadOSPFVlinkEnable = _IpadOSPFVlinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6, 1, 2),
    _IpadOSPFVlinkEnable_Type()
)
ipadOSPFVlinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFVlinkEnable.setStatus("current")
_IpadOSPFVlinkTransitAreaID_Type = IpAddress
_IpadOSPFVlinkTransitAreaID_Object = MibTableColumn
ipadOSPFVlinkTransitAreaID = _IpadOSPFVlinkTransitAreaID_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6, 1, 3),
    _IpadOSPFVlinkTransitAreaID_Type()
)
ipadOSPFVlinkTransitAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFVlinkTransitAreaID.setStatus("current")
_IpadOSPFVlinkAreaBorderRouterID_Type = IpAddress
_IpadOSPFVlinkAreaBorderRouterID_Object = MibTableColumn
ipadOSPFVlinkAreaBorderRouterID = _IpadOSPFVlinkAreaBorderRouterID_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 6, 1, 4),
    _IpadOSPFVlinkAreaBorderRouterID_Type()
)
ipadOSPFVlinkAreaBorderRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFVlinkAreaBorderRouterID.setStatus("current")


class _IpadOSPFVlinkAdd_Type(Integer32):
    """Custom type ipadOSPFVlinkAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("addnew", 2))
    )


_IpadOSPFVlinkAdd_Type.__name__ = "Integer32"
_IpadOSPFVlinkAdd_Object = MibScalar
ipadOSPFVlinkAdd = _IpadOSPFVlinkAdd_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 7),
    _IpadOSPFVlinkAdd_Type()
)
ipadOSPFVlinkAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFVlinkAdd.setStatus("current")
_IpadOSPFVlinkDelete_Type = Integer32
_IpadOSPFVlinkDelete_Object = MibScalar
ipadOSPFVlinkDelete = _IpadOSPFVlinkDelete_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 3, 8),
    _IpadOSPFVlinkDelete_Type()
)
ipadOSPFVlinkDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOSPFVlinkDelete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-ROUTER-MIB",
    **{"ipadRouter": ipadRouter,
       "ipadCircuitParms": ipadCircuitParms,
       "ipadCircuitTable": ipadCircuitTable,
       "ipadCircuitTableEntry": ipadCircuitTableEntry,
       "ipadCircuitIndex": ipadCircuitIndex,
       "ipadCircuitEndpoint": ipadCircuitEndpoint,
       "ipadCircuitIpAddress": ipadCircuitIpAddress,
       "ipadCircuitIpMask": ipadCircuitIpMask,
       "ipadCircuitMaxTransmitUnit": ipadCircuitMaxTransmitUnit,
       "ipadCircuitCost": ipadCircuitCost,
       "ipadCircuitEnableRIP": ipadCircuitEnableRIP,
       "ipadCircuitEnableOSPF": ipadCircuitEnableOSPF,
       "ipadCircuitEnableMulticast": ipadCircuitEnableMulticast,
       "ipadCircuitOSPFArea": ipadCircuitOSPFArea,
       "ipadCircuitOSPFLSATimer": ipadCircuitOSPFLSATimer,
       "ipadCircuitOSPFLSUDelay": ipadCircuitOSPFLSUDelay,
       "ipadCircuitOSPFRouterPriority": ipadCircuitOSPFRouterPriority,
       "ipadCircuitOSPFHelloInterval": ipadCircuitOSPFHelloInterval,
       "ipadCircuitOSPFDeadInterval": ipadCircuitOSPFDeadInterval,
       "ipadCircuitOSPFAuthKey": ipadCircuitOSPFAuthKey,
       "ipadCircuitAdd": ipadCircuitAdd,
       "ipadCircuitDelete": ipadCircuitDelete,
       "ipadRIPParms": ipadRIPParms,
       "ipadRIPEnable": ipadRIPEnable,
       "ipadRIPTrustNeighbors": ipadRIPTrustNeighbors,
       "ipadRIPInterval": ipadRIPInterval,
       "ipadRIPDomain": ipadRIPDomain,
       "ipadRIPStaticARPTable": ipadRIPStaticARPTable,
       "ipadRIPStaticARPTableEntry": ipadRIPStaticARPTableEntry,
       "ipadRIPStaticARPIndex": ipadRIPStaticARPIndex,
       "ipadRIPStaticARPEndpoint": ipadRIPStaticARPEndpoint,
       "ipadRIPStaticARPIpAddress": ipadRIPStaticARPIpAddress,
       "ipadRIPStaticARPMacAddress": ipadRIPStaticARPMacAddress,
       "ipadRIPStaticARPDLCIAddress": ipadRIPStaticARPDLCIAddress,
       "ipadRIPStaticARPEnableARP": ipadRIPStaticARPEnableARP,
       "ipadRIPStaticARPAdd": ipadRIPStaticARPAdd,
       "ipadRIPStaticARPDelete": ipadRIPStaticARPDelete,
       "ipadRIPStaticRouteTable": ipadRIPStaticRouteTable,
       "ipadRIPStaticRouteTableEntry": ipadRIPStaticRouteTableEntry,
       "ipadRIPStaticRouteIndex": ipadRIPStaticRouteIndex,
       "ipadRIPStaticRouteEndpoint": ipadRIPStaticRouteEndpoint,
       "ipadRIPStaticRouteTargetIpAddress": ipadRIPStaticRouteTargetIpAddress,
       "ipadRIPStaticRouteTargetIpMask": ipadRIPStaticRouteTargetIpMask,
       "ipadRIPStaticRouteNextHopIpAddress": ipadRIPStaticRouteNextHopIpAddress,
       "ipadRIPStaticRouteCost": ipadRIPStaticRouteCost,
       "ipadRIPStaticRouteEnableRouter": ipadRIPStaticRouteEnableRouter,
       "ipadRIPStaticRouteAdd": ipadRIPStaticRouteAdd,
       "ipadRIPStaticRouteDelete": ipadRIPStaticRouteDelete,
       "ipadRIPNeighborTable": ipadRIPNeighborTable,
       "ipadRIPNeighborTableEntry": ipadRIPNeighborTableEntry,
       "ipadRIPNeighborIndex": ipadRIPNeighborIndex,
       "ipadRIPNeighborAddress": ipadRIPNeighborAddress,
       "ipadRIPNeighborAdd": ipadRIPNeighborAdd,
       "ipadRIPNeighborDelete": ipadRIPNeighborDelete,
       "ipadOSPFParms": ipadOSPFParms,
       "ipadOSPFEnable": ipadOSPFEnable,
       "ipadOSPFRouterID": ipadOSPFRouterID,
       "ipadOSPFAreaTable": ipadOSPFAreaTable,
       "ipadOSPFAreaTableEntry": ipadOSPFAreaTableEntry,
       "ipadOSPFAreaIndex": ipadOSPFAreaIndex,
       "ipadOSPFAreaID": ipadOSPFAreaID,
       "ipadOSPFAreaEnable": ipadOSPFAreaEnable,
       "ipadOSPFAreaAuthType": ipadOSPFAreaAuthType,
       "ipadOSPFAreaStub": ipadOSPFAreaStub,
       "ipadOSPFAreaAddrSummary": ipadOSPFAreaAddrSummary,
       "ipadOSPFAreaMaskSummary": ipadOSPFAreaMaskSummary,
       "ipadOSPFAreaAdvertise": ipadOSPFAreaAdvertise,
       "ipadOSPFAreaAdd": ipadOSPFAreaAdd,
       "ipadOSPFAreaDelete": ipadOSPFAreaDelete,
       "ipadOSPFVlinkTable": ipadOSPFVlinkTable,
       "ipadOSPFVlinkTableEntry": ipadOSPFVlinkTableEntry,
       "ipadOSPFVlinkIndex": ipadOSPFVlinkIndex,
       "ipadOSPFVlinkEnable": ipadOSPFVlinkEnable,
       "ipadOSPFVlinkTransitAreaID": ipadOSPFVlinkTransitAreaID,
       "ipadOSPFVlinkAreaBorderRouterID": ipadOSPFVlinkAreaBorderRouterID,
       "ipadOSPFVlinkAdd": ipadOSPFVlinkAdd,
       "ipadOSPFVlinkDelete": ipadOSPFVlinkDelete}
)
