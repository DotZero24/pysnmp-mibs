# SNMP MIB module (IEEE8023-DOT3-LLDP-EXT-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/IEEE8023-DOT3-LLDP-EXT-V2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:19:13 2025
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

(ifGeneralInformationGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifGeneralInformationGroup")

(lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(LldpV2PowerPortClass,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2PowerPortClass")

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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8023lldpV2Xdot3MIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8023lldpV2Xdot3MIB.setRevisions(
        ("2013-04-11 00:00",
         "2011-02-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpV2Xdot3Objects_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Objects = _LldpV2Xdot3Objects_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 1)
)
_LldpV2Xdot3Config_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Config = _LldpV2Xdot3Config_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 1)
)
_LldpV2Xdot3PortConfigTable_Object = MibTable
lldpV2Xdot3PortConfigTable = _LldpV2Xdot3PortConfigTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigTable.setStatus("current")
_LldpV2Xdot3PortConfigEntry_Object = MibTableRow
lldpV2Xdot3PortConfigEntry = _LldpV2Xdot3PortConfigEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigEntry.setStatus("current")


class _LldpV2Xdot3PortConfigTLVsTxEnable_Type(Bits):
    """Custom type lldpV2Xdot3PortConfigTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("macPhyConfigStatus", 0),
          ("powerViaMDI", 1),
          ("unused", 2),
          ("maxFrameSize", 3))
    )

_LldpV2Xdot3PortConfigTLVsTxEnable_Type.__name__ = "Bits"
_LldpV2Xdot3PortConfigTLVsTxEnable_Object = MibTableColumn
lldpV2Xdot3PortConfigTLVsTxEnable = _LldpV2Xdot3PortConfigTLVsTxEnable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 1, 1, 1, 1),
    _LldpV2Xdot3PortConfigTLVsTxEnable_Type()
)
lldpV2Xdot3PortConfigTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot3PortConfigTLVsTxEnable.setStatus("current")
_LldpV2Xdot3LocalData_ObjectIdentity = ObjectIdentity
lldpV2Xdot3LocalData = _LldpV2Xdot3LocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2)
)
_LldpV2Xdot3LocPortTable_Object = MibTable
lldpV2Xdot3LocPortTable = _LldpV2Xdot3LocPortTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortTable.setStatus("current")
_LldpV2Xdot3LocPortEntry_Object = MibTableRow
lldpV2Xdot3LocPortEntry = _LldpV2Xdot3LocPortEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1, 1)
)
lldpV2Xdot3LocPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortEntry.setStatus("current")
_LldpV2Xdot3LocPortAutoNegSupported_Type = TruthValue
_LldpV2Xdot3LocPortAutoNegSupported_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegSupported = _LldpV2Xdot3LocPortAutoNegSupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1, 1, 1),
    _LldpV2Xdot3LocPortAutoNegSupported_Type()
)
lldpV2Xdot3LocPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegSupported.setStatus("current")
_LldpV2Xdot3LocPortAutoNegEnabled_Type = TruthValue
_LldpV2Xdot3LocPortAutoNegEnabled_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegEnabled = _LldpV2Xdot3LocPortAutoNegEnabled_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1, 1, 2),
    _LldpV2Xdot3LocPortAutoNegEnabled_Type()
)
lldpV2Xdot3LocPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegEnabled.setStatus("current")


class _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpV2Xdot3LocPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpV2Xdot3LocPortAutoNegAdvertisedCap = _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1, 1, 3),
    _LldpV2Xdot3LocPortAutoNegAdvertisedCap_Type()
)
lldpV2Xdot3LocPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortAutoNegAdvertisedCap.setStatus("current")


class _LldpV2Xdot3LocPortOperMauType_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPortOperMauType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2Xdot3LocPortOperMauType_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPortOperMauType_Object = MibTableColumn
lldpV2Xdot3LocPortOperMauType = _LldpV2Xdot3LocPortOperMauType_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 1, 1, 4),
    _LldpV2Xdot3LocPortOperMauType_Type()
)
lldpV2Xdot3LocPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPortOperMauType.setStatus("current")
_LldpV2Xdot3LocPowerTable_Object = MibTable
lldpV2Xdot3LocPowerTable = _LldpV2Xdot3LocPowerTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerTable.setStatus("current")
_LldpV2Xdot3LocPowerEntry_Object = MibTableRow
lldpV2Xdot3LocPowerEntry = _LldpV2Xdot3LocPowerEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1)
)
lldpV2Xdot3LocPowerEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerEntry.setStatus("current")
_LldpV2Xdot3LocPowerPortClass_Type = LldpV2PowerPortClass
_LldpV2Xdot3LocPowerPortClass_Object = MibTableColumn
lldpV2Xdot3LocPowerPortClass = _LldpV2Xdot3LocPowerPortClass_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 1),
    _LldpV2Xdot3LocPowerPortClass_Type()
)
lldpV2Xdot3LocPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPortClass.setStatus("current")
_LldpV2Xdot3LocPowerMDISupported_Type = TruthValue
_LldpV2Xdot3LocPowerMDISupported_Object = MibTableColumn
lldpV2Xdot3LocPowerMDISupported = _LldpV2Xdot3LocPowerMDISupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 2),
    _LldpV2Xdot3LocPowerMDISupported_Type()
)
lldpV2Xdot3LocPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerMDISupported.setStatus("current")
_LldpV2Xdot3LocPowerMDIEnabled_Type = TruthValue
_LldpV2Xdot3LocPowerMDIEnabled_Object = MibTableColumn
lldpV2Xdot3LocPowerMDIEnabled = _LldpV2Xdot3LocPowerMDIEnabled_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 3),
    _LldpV2Xdot3LocPowerMDIEnabled_Type()
)
lldpV2Xdot3LocPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerMDIEnabled.setStatus("current")
_LldpV2Xdot3LocPowerPairControlable_Type = TruthValue
_LldpV2Xdot3LocPowerPairControlable_Object = MibTableColumn
lldpV2Xdot3LocPowerPairControlable = _LldpV2Xdot3LocPowerPairControlable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 4),
    _LldpV2Xdot3LocPowerPairControlable_Type()
)
lldpV2Xdot3LocPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPairControlable.setStatus("current")


class _LldpV2Xdot3LocPowerPairs_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPowerPairs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpV2Xdot3LocPowerPairs_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPowerPairs_Object = MibTableColumn
lldpV2Xdot3LocPowerPairs = _LldpV2Xdot3LocPowerPairs_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 5),
    _LldpV2Xdot3LocPowerPairs_Type()
)
lldpV2Xdot3LocPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPairs.setStatus("current")


class _LldpV2Xdot3LocPowerClass_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocPowerClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpV2Xdot3LocPowerClass_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocPowerClass_Object = MibTableColumn
lldpV2Xdot3LocPowerClass = _LldpV2Xdot3LocPowerClass_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 6),
    _LldpV2Xdot3LocPowerClass_Type()
)
lldpV2Xdot3LocPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerClass.setStatus("current")


class _LldpV2Xdot3LocPowerType_Type(Integer32):
    """Custom type lldpV2Xdot3LocPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("psetype1", 0),
          ("psetype2", 1),
          ("pdtype", 2),
          ("pdtype2", 3))
    )


_LldpV2Xdot3LocPowerType_Type.__name__ = "Integer32"
_LldpV2Xdot3LocPowerType_Object = MibTableColumn
lldpV2Xdot3LocPowerType = _LldpV2Xdot3LocPowerType_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 7),
    _LldpV2Xdot3LocPowerType_Type()
)
lldpV2Xdot3LocPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerType.setStatus("current")


class _LldpV2Xdot3LocPowerSource_Type(Integer32):
    """Custom type lldpV2Xdot3LocPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("pseprimary", 0),
          ("psebackup", 1),
          ("pseunknown", 2),
          ("pdpseandlocal", 3),
          ("pdpseonly", 4),
          ("pdunknown", 5))
    )


_LldpV2Xdot3LocPowerSource_Type.__name__ = "Integer32"
_LldpV2Xdot3LocPowerSource_Object = MibTableColumn
lldpV2Xdot3LocPowerSource = _LldpV2Xdot3LocPowerSource_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 8),
    _LldpV2Xdot3LocPowerSource_Type()
)
lldpV2Xdot3LocPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerSource.setStatus("current")


class _LldpV2Xdot3LocPowerPriority_Type(Integer32):
    """Custom type lldpV2Xdot3LocPowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1),
          ("critical", 2),
          ("unknown", 3))
    )


_LldpV2Xdot3LocPowerPriority_Type.__name__ = "Integer32"
_LldpV2Xdot3LocPowerPriority_Object = MibTableColumn
lldpV2Xdot3LocPowerPriority = _LldpV2Xdot3LocPowerPriority_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 9),
    _LldpV2Xdot3LocPowerPriority_Type()
)
lldpV2Xdot3LocPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPowerPriority.setStatus("current")
_LldpV2Xdot3LocPDRequestedPowerValue_Type = Integer32
_LldpV2Xdot3LocPDRequestedPowerValue_Object = MibTableColumn
lldpV2Xdot3LocPDRequestedPowerValue = _LldpV2Xdot3LocPDRequestedPowerValue_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 10),
    _LldpV2Xdot3LocPDRequestedPowerValue_Type()
)
lldpV2Xdot3LocPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPDRequestedPowerValue.setStatus("current")
_LldpV2Xdot3LocPSEAllocatedPowerValue_Type = Integer32
_LldpV2Xdot3LocPSEAllocatedPowerValue_Object = MibTableColumn
lldpV2Xdot3LocPSEAllocatedPowerValue = _LldpV2Xdot3LocPSEAllocatedPowerValue_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 11),
    _LldpV2Xdot3LocPSEAllocatedPowerValue_Type()
)
lldpV2Xdot3LocPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocPSEAllocatedPowerValue.setStatus("current")
_LldpV2Xdot3LocResponseTime_Type = Integer32
_LldpV2Xdot3LocResponseTime_Object = MibTableColumn
lldpV2Xdot3LocResponseTime = _LldpV2Xdot3LocResponseTime_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 12),
    _LldpV2Xdot3LocResponseTime_Type()
)
lldpV2Xdot3LocResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocResponseTime.setStatus("current")
_LldpV2Xdot3LocReady_Type = TruthValue
_LldpV2Xdot3LocReady_Object = MibTableColumn
lldpV2Xdot3LocReady = _LldpV2Xdot3LocReady_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 13),
    _LldpV2Xdot3LocReady_Type()
)
lldpV2Xdot3LocReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocReady.setStatus("current")
_LldpV2Xdot3LocReducedOperationPowerValue_Type = Integer32
_LldpV2Xdot3LocReducedOperationPowerValue_Object = MibTableColumn
lldpV2Xdot3LocReducedOperationPowerValue = _LldpV2Xdot3LocReducedOperationPowerValue_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 2, 1, 14),
    _LldpV2Xdot3LocReducedOperationPowerValue_Type()
)
lldpV2Xdot3LocReducedOperationPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocReducedOperationPowerValue.setStatus("current")
_LldpV2Xdot3LocMaxFrameSizeTable_Object = MibTable
lldpV2Xdot3LocMaxFrameSizeTable = _LldpV2Xdot3LocMaxFrameSizeTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSizeTable.setStatus("current")
_LldpV2Xdot3LocMaxFrameSizeEntry_Object = MibTableRow
lldpV2Xdot3LocMaxFrameSizeEntry = _LldpV2Xdot3LocMaxFrameSizeEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 3, 1)
)
lldpV2Xdot3LocMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSizeEntry.setStatus("current")


class _LldpV2Xdot3LocMaxFrameSize_Type(Unsigned32):
    """Custom type lldpV2Xdot3LocMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpV2Xdot3LocMaxFrameSize_Type.__name__ = "Unsigned32"
_LldpV2Xdot3LocMaxFrameSize_Object = MibTableColumn
lldpV2Xdot3LocMaxFrameSize = _LldpV2Xdot3LocMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 3, 1, 1),
    _LldpV2Xdot3LocMaxFrameSize_Type()
)
lldpV2Xdot3LocMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocMaxFrameSize.setStatus("current")
_LldpV2Xdot3LocEEETable_Object = MibTable
lldpV2Xdot3LocEEETable = _LldpV2Xdot3LocEEETable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocEEETable.setStatus("current")
_LldpV2Xdot3LocEEEEntry_Object = MibTableRow
lldpV2Xdot3LocEEEEntry = _LldpV2Xdot3LocEEEEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1)
)
lldpV2Xdot3LocEEEEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocEEEEntry.setStatus("current")
_LldpV2Xdot3LocTxTwSys_Type = Integer32
_LldpV2Xdot3LocTxTwSys_Object = MibTableColumn
lldpV2Xdot3LocTxTwSys = _LldpV2Xdot3LocTxTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 1),
    _LldpV2Xdot3LocTxTwSys_Type()
)
lldpV2Xdot3LocTxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocTxTwSys.setStatus("current")
_LldpV2Xdot3LocTxTwSysEcho_Type = Integer32
_LldpV2Xdot3LocTxTwSysEcho_Object = MibTableColumn
lldpV2Xdot3LocTxTwSysEcho = _LldpV2Xdot3LocTxTwSysEcho_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 2),
    _LldpV2Xdot3LocTxTwSysEcho_Type()
)
lldpV2Xdot3LocTxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocTxTwSysEcho.setStatus("current")
_LldpV2Xdot3LocRxTwSys_Type = Integer32
_LldpV2Xdot3LocRxTwSys_Object = MibTableColumn
lldpV2Xdot3LocRxTwSys = _LldpV2Xdot3LocRxTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 3),
    _LldpV2Xdot3LocRxTwSys_Type()
)
lldpV2Xdot3LocRxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocRxTwSys.setStatus("current")
_LldpV2Xdot3LocRxTwSysEcho_Type = Integer32
_LldpV2Xdot3LocRxTwSysEcho_Object = MibTableColumn
lldpV2Xdot3LocRxTwSysEcho = _LldpV2Xdot3LocRxTwSysEcho_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 4),
    _LldpV2Xdot3LocRxTwSysEcho_Type()
)
lldpV2Xdot3LocRxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocRxTwSysEcho.setStatus("current")
_LldpV2Xdot3LocFbTwSys_Type = Integer32
_LldpV2Xdot3LocFbTwSys_Object = MibTableColumn
lldpV2Xdot3LocFbTwSys = _LldpV2Xdot3LocFbTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 5),
    _LldpV2Xdot3LocFbTwSys_Type()
)
lldpV2Xdot3LocFbTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocFbTwSys.setStatus("current")
_LldpV2Xdot3TxDllReady_Type = TruthValue
_LldpV2Xdot3TxDllReady_Object = MibTableColumn
lldpV2Xdot3TxDllReady = _LldpV2Xdot3TxDllReady_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 6),
    _LldpV2Xdot3TxDllReady_Type()
)
lldpV2Xdot3TxDllReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3TxDllReady.setStatus("current")
_LldpV2Xdot3RxDllReady_Type = TruthValue
_LldpV2Xdot3RxDllReady_Object = MibTableColumn
lldpV2Xdot3RxDllReady = _LldpV2Xdot3RxDllReady_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 7),
    _LldpV2Xdot3RxDllReady_Type()
)
lldpV2Xdot3RxDllReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RxDllReady.setStatus("current")
_LldpV2Xdot3LocDllEnabled_Type = TruthValue
_LldpV2Xdot3LocDllEnabled_Object = MibTableColumn
lldpV2Xdot3LocDllEnabled = _LldpV2Xdot3LocDllEnabled_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 2, 4, 1, 8),
    _LldpV2Xdot3LocDllEnabled_Type()
)
lldpV2Xdot3LocDllEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3LocDllEnabled.setStatus("current")
_LldpV2Xdot3RemoteData_ObjectIdentity = ObjectIdentity
lldpV2Xdot3RemoteData = _LldpV2Xdot3RemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3)
)
_LldpV2Xdot3RemPortTable_Object = MibTable
lldpV2Xdot3RemPortTable = _LldpV2Xdot3RemPortTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortTable.setStatus("current")
_LldpV2Xdot3RemPortEntry_Object = MibTableRow
lldpV2Xdot3RemPortEntry = _LldpV2Xdot3RemPortEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1, 1)
)
lldpV2Xdot3RemPortEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortEntry.setStatus("current")
_LldpV2Xdot3RemPortAutoNegSupported_Type = TruthValue
_LldpV2Xdot3RemPortAutoNegSupported_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegSupported = _LldpV2Xdot3RemPortAutoNegSupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1, 1, 1),
    _LldpV2Xdot3RemPortAutoNegSupported_Type()
)
lldpV2Xdot3RemPortAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegSupported.setStatus("current")
_LldpV2Xdot3RemPortAutoNegEnabled_Type = TruthValue
_LldpV2Xdot3RemPortAutoNegEnabled_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegEnabled = _LldpV2Xdot3RemPortAutoNegEnabled_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1, 1, 2),
    _LldpV2Xdot3RemPortAutoNegEnabled_Type()
)
lldpV2Xdot3RemPortAutoNegEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegEnabled.setStatus("current")


class _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type(OctetString):
    """Custom type lldpV2Xdot3RemPortAutoNegAdvertisedCap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type.__name__ = "OctetString"
_LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object = MibTableColumn
lldpV2Xdot3RemPortAutoNegAdvertisedCap = _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1, 1, 3),
    _LldpV2Xdot3RemPortAutoNegAdvertisedCap_Type()
)
lldpV2Xdot3RemPortAutoNegAdvertisedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortAutoNegAdvertisedCap.setStatus("current")


class _LldpV2Xdot3RemPortOperMauType_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPortOperMauType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2Xdot3RemPortOperMauType_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPortOperMauType_Object = MibTableColumn
lldpV2Xdot3RemPortOperMauType = _LldpV2Xdot3RemPortOperMauType_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 1, 1, 4),
    _LldpV2Xdot3RemPortOperMauType_Type()
)
lldpV2Xdot3RemPortOperMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPortOperMauType.setStatus("current")
_LldpV2Xdot3RemPowerTable_Object = MibTable
lldpV2Xdot3RemPowerTable = _LldpV2Xdot3RemPowerTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerTable.setStatus("current")
_LldpV2Xdot3RemPowerEntry_Object = MibTableRow
lldpV2Xdot3RemPowerEntry = _LldpV2Xdot3RemPowerEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1)
)
lldpV2Xdot3RemPowerEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerEntry.setStatus("current")
_LldpV2Xdot3RemPowerPortClass_Type = LldpV2PowerPortClass
_LldpV2Xdot3RemPowerPortClass_Object = MibTableColumn
lldpV2Xdot3RemPowerPortClass = _LldpV2Xdot3RemPowerPortClass_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 1),
    _LldpV2Xdot3RemPowerPortClass_Type()
)
lldpV2Xdot3RemPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPortClass.setStatus("current")
_LldpV2Xdot3RemPowerMDISupported_Type = TruthValue
_LldpV2Xdot3RemPowerMDISupported_Object = MibTableColumn
lldpV2Xdot3RemPowerMDISupported = _LldpV2Xdot3RemPowerMDISupported_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 2),
    _LldpV2Xdot3RemPowerMDISupported_Type()
)
lldpV2Xdot3RemPowerMDISupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerMDISupported.setStatus("current")
_LldpV2Xdot3RemPowerMDIEnabled_Type = TruthValue
_LldpV2Xdot3RemPowerMDIEnabled_Object = MibTableColumn
lldpV2Xdot3RemPowerMDIEnabled = _LldpV2Xdot3RemPowerMDIEnabled_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 3),
    _LldpV2Xdot3RemPowerMDIEnabled_Type()
)
lldpV2Xdot3RemPowerMDIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerMDIEnabled.setStatus("current")
_LldpV2Xdot3RemPowerPairControlable_Type = TruthValue
_LldpV2Xdot3RemPowerPairControlable_Object = MibTableColumn
lldpV2Xdot3RemPowerPairControlable = _LldpV2Xdot3RemPowerPairControlable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 4),
    _LldpV2Xdot3RemPowerPairControlable_Type()
)
lldpV2Xdot3RemPowerPairControlable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPairControlable.setStatus("current")


class _LldpV2Xdot3RemPowerPairs_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPowerPairs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_LldpV2Xdot3RemPowerPairs_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPowerPairs_Object = MibTableColumn
lldpV2Xdot3RemPowerPairs = _LldpV2Xdot3RemPowerPairs_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 5),
    _LldpV2Xdot3RemPowerPairs_Type()
)
lldpV2Xdot3RemPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPairs.setStatus("current")


class _LldpV2Xdot3RemPowerClass_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemPowerClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_LldpV2Xdot3RemPowerClass_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemPowerClass_Object = MibTableColumn
lldpV2Xdot3RemPowerClass = _LldpV2Xdot3RemPowerClass_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 6),
    _LldpV2Xdot3RemPowerClass_Type()
)
lldpV2Xdot3RemPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerClass.setStatus("current")


class _LldpV2Xdot3RemPowerType_Type(Integer32):
    """Custom type lldpV2Xdot3RemPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("psetype1", 0),
          ("psetype2", 1),
          ("pdtype", 2),
          ("pdtype2", 3))
    )


_LldpV2Xdot3RemPowerType_Type.__name__ = "Integer32"
_LldpV2Xdot3RemPowerType_Object = MibTableColumn
lldpV2Xdot3RemPowerType = _LldpV2Xdot3RemPowerType_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 7),
    _LldpV2Xdot3RemPowerType_Type()
)
lldpV2Xdot3RemPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerType.setStatus("current")


class _LldpV2Xdot3RemPowerSource_Type(Integer32):
    """Custom type lldpV2Xdot3RemPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pseprimary", 0),
          ("psebackup", 1),
          ("pseunknown", 2),
          ("pdpseandlocal", 3),
          ("pdlocalonly", 4),
          ("pdpseonly", 5),
          ("pdunknown", 6))
    )


_LldpV2Xdot3RemPowerSource_Type.__name__ = "Integer32"
_LldpV2Xdot3RemPowerSource_Object = MibTableColumn
lldpV2Xdot3RemPowerSource = _LldpV2Xdot3RemPowerSource_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 8),
    _LldpV2Xdot3RemPowerSource_Type()
)
lldpV2Xdot3RemPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerSource.setStatus("current")


class _LldpV2Xdot3RemPowerPriority_Type(Integer32):
    """Custom type lldpV2Xdot3RemPowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1),
          ("critical", 2),
          ("unknown", 3))
    )


_LldpV2Xdot3RemPowerPriority_Type.__name__ = "Integer32"
_LldpV2Xdot3RemPowerPriority_Object = MibTableColumn
lldpV2Xdot3RemPowerPriority = _LldpV2Xdot3RemPowerPriority_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 9),
    _LldpV2Xdot3RemPowerPriority_Type()
)
lldpV2Xdot3RemPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPowerPriority.setStatus("current")
_LldpV2Xdot3RemPDRequestedPowerValue_Type = Integer32
_LldpV2Xdot3RemPDRequestedPowerValue_Object = MibTableColumn
lldpV2Xdot3RemPDRequestedPowerValue = _LldpV2Xdot3RemPDRequestedPowerValue_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 10),
    _LldpV2Xdot3RemPDRequestedPowerValue_Type()
)
lldpV2Xdot3RemPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPDRequestedPowerValue.setStatus("current")
_LldpV2Xdot3RemPSEAllocatedPowerValue_Type = Integer32
_LldpV2Xdot3RemPSEAllocatedPowerValue_Object = MibTableColumn
lldpV2Xdot3RemPSEAllocatedPowerValue = _LldpV2Xdot3RemPSEAllocatedPowerValue_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 2, 1, 11),
    _LldpV2Xdot3RemPSEAllocatedPowerValue_Type()
)
lldpV2Xdot3RemPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemPSEAllocatedPowerValue.setStatus("current")
_LldpV2Xdot3RemMaxFrameSizeTable_Object = MibTable
lldpV2Xdot3RemMaxFrameSizeTable = _LldpV2Xdot3RemMaxFrameSizeTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSizeTable.setStatus("current")
_LldpV2Xdot3RemMaxFrameSizeEntry_Object = MibTableRow
lldpV2Xdot3RemMaxFrameSizeEntry = _LldpV2Xdot3RemMaxFrameSizeEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 3, 1)
)
lldpV2Xdot3RemMaxFrameSizeEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSizeEntry.setStatus("current")


class _LldpV2Xdot3RemMaxFrameSize_Type(Unsigned32):
    """Custom type lldpV2Xdot3RemMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LldpV2Xdot3RemMaxFrameSize_Type.__name__ = "Unsigned32"
_LldpV2Xdot3RemMaxFrameSize_Object = MibTableColumn
lldpV2Xdot3RemMaxFrameSize = _LldpV2Xdot3RemMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 3, 1, 1),
    _LldpV2Xdot3RemMaxFrameSize_Type()
)
lldpV2Xdot3RemMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemMaxFrameSize.setStatus("current")
_LldpV2Xdot3RemEEETable_Object = MibTable
lldpV2Xdot3RemEEETable = _LldpV2Xdot3RemEEETable_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemEEETable.setStatus("current")
_LldpV2Xdot3RemEEEEntry_Object = MibTableRow
lldpV2Xdot3RemEEEEntry = _LldpV2Xdot3RemEEEEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1)
)
lldpV2Xdot3RemEEEEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemEEEEntry.setStatus("current")
_LldpV2Xdot3RemTxTwSys_Type = Integer32
_LldpV2Xdot3RemTxTwSys_Object = MibTableColumn
lldpV2Xdot3RemTxTwSys = _LldpV2Xdot3RemTxTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1, 1),
    _LldpV2Xdot3RemTxTwSys_Type()
)
lldpV2Xdot3RemTxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemTxTwSys.setStatus("current")
_LldpV2Xdot3RemTxTwSysEcho_Type = Integer32
_LldpV2Xdot3RemTxTwSysEcho_Object = MibTableColumn
lldpV2Xdot3RemTxTwSysEcho = _LldpV2Xdot3RemTxTwSysEcho_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1, 2),
    _LldpV2Xdot3RemTxTwSysEcho_Type()
)
lldpV2Xdot3RemTxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemTxTwSysEcho.setStatus("current")
_LldpV2Xdot3RemRxTwSys_Type = Integer32
_LldpV2Xdot3RemRxTwSys_Object = MibTableColumn
lldpV2Xdot3RemRxTwSys = _LldpV2Xdot3RemRxTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1, 3),
    _LldpV2Xdot3RemRxTwSys_Type()
)
lldpV2Xdot3RemRxTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemRxTwSys.setStatus("current")
_LldpV2Xdot3RemRxTwSysEcho_Type = Integer32
_LldpV2Xdot3RemRxTwSysEcho_Object = MibTableColumn
lldpV2Xdot3RemRxTwSysEcho = _LldpV2Xdot3RemRxTwSysEcho_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1, 4),
    _LldpV2Xdot3RemRxTwSysEcho_Type()
)
lldpV2Xdot3RemRxTwSysEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemRxTwSysEcho.setStatus("current")
_LldpV2Xdot3RemFbTwSys_Type = Integer32
_LldpV2Xdot3RemFbTwSys_Object = MibTableColumn
lldpV2Xdot3RemFbTwSys = _LldpV2Xdot3RemFbTwSys_Object(
    (1, 3, 111, 2, 802, 3, 1, 5, 1, 3, 4, 1, 5),
    _LldpV2Xdot3RemFbTwSys_Type()
)
lldpV2Xdot3RemFbTwSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2Xdot3RemFbTwSys.setStatus("current")
_LldpV2Xdot3Conformance_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Conformance = _LldpV2Xdot3Conformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 2)
)
_LldpV2Xdot3Compliances_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Compliances = _LldpV2Xdot3Compliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 1)
)
_LldpV2Xdot3Groups_ObjectIdentity = ObjectIdentity
lldpV2Xdot3Groups = _LldpV2Xdot3Groups_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("IEEE8023-DOT3-LLDP-EXT-V2-MIB",
     "lldpV2Xdot3PortConfigEntry")
)
lldpV2Xdot3PortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpV2Xdot3ConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 2, 1)
)
lldpV2Xdot3ConfigGroup.setObjects(
    ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3PortConfigTLVsTxEnable")
)
if mibBuilder.loadTexts:
    lldpV2Xdot3ConfigGroup.setStatus("current")

lldpV2Xdot3LocSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 2, 2)
)
lldpV2Xdot3LocSysGroup.setObjects(
      *(("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPortAutoNegSupported"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPortAutoNegEnabled"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPortAutoNegAdvertisedCap"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPortOperMauType"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerPortClass"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerMDISupported"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerMDIEnabled"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerPairControlable"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerPairs"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerClass"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocMaxFrameSize"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerType"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerSource"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPowerPriority"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPDRequestedPowerValue"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocPSEAllocatedPowerValue"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocResponseTime"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocReady"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocReducedOperationPowerValue"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocTxTwSys"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocTxTwSysEcho"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocRxTwSys"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocRxTwSysEcho"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocFbTwSys"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3TxDllReady"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RxDllReady"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocDllEnabled"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot3LocSysGroup.setStatus("current")

lldpV2Xdot3RemSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 2, 3)
)
lldpV2Xdot3RemSysGroup.setObjects(
      *(("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPortAutoNegSupported"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPortAutoNegEnabled"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPortAutoNegAdvertisedCap"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPortOperMauType"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerPortClass"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerMDISupported"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerMDIEnabled"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerPairControlable"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerPairs"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerClass"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemMaxFrameSize"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerType"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerSource"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPowerPriority"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPDRequestedPowerValue"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemPSEAllocatedPowerValue"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemTxTwSys"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemTxTwSysEcho"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemRxTwSys"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemRxTwSysEcho"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemFbTwSys"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RemSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpV2Xdot3TxRxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 1, 1)
)
lldpV2Xdot3TxRxCompliance.setObjects(
      *(("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3ConfigGroup"),
        ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "ifGeneralInformationGroup"))
)
if mibBuilder.loadTexts:
    lldpV2Xdot3TxRxCompliance.setStatus(
        "current"
    )

lldpV2Xdot3TxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 1, 2)
)
lldpV2Xdot3TxCompliance.setObjects(
    ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3LocSysGroup")
)
if mibBuilder.loadTexts:
    lldpV2Xdot3TxCompliance.setStatus(
        "current"
    )

lldpV2Xdot3RxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 5, 2, 1, 3)
)
lldpV2Xdot3RxCompliance.setObjects(
    ("IEEE8023-DOT3-LLDP-EXT-V2-MIB", "lldpV2Xdot3RemSysGroup")
)
if mibBuilder.loadTexts:
    lldpV2Xdot3RxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8023-DOT3-LLDP-EXT-V2-MIB",
    **{"ieee8023lldpV2Xdot3MIB": ieee8023lldpV2Xdot3MIB,
       "lldpV2Xdot3Objects": lldpV2Xdot3Objects,
       "lldpV2Xdot3Config": lldpV2Xdot3Config,
       "lldpV2Xdot3PortConfigTable": lldpV2Xdot3PortConfigTable,
       "lldpV2Xdot3PortConfigEntry": lldpV2Xdot3PortConfigEntry,
       "lldpV2Xdot3PortConfigTLVsTxEnable": lldpV2Xdot3PortConfigTLVsTxEnable,
       "lldpV2Xdot3LocalData": lldpV2Xdot3LocalData,
       "lldpV2Xdot3LocPortTable": lldpV2Xdot3LocPortTable,
       "lldpV2Xdot3LocPortEntry": lldpV2Xdot3LocPortEntry,
       "lldpV2Xdot3LocPortAutoNegSupported": lldpV2Xdot3LocPortAutoNegSupported,
       "lldpV2Xdot3LocPortAutoNegEnabled": lldpV2Xdot3LocPortAutoNegEnabled,
       "lldpV2Xdot3LocPortAutoNegAdvertisedCap": lldpV2Xdot3LocPortAutoNegAdvertisedCap,
       "lldpV2Xdot3LocPortOperMauType": lldpV2Xdot3LocPortOperMauType,
       "lldpV2Xdot3LocPowerTable": lldpV2Xdot3LocPowerTable,
       "lldpV2Xdot3LocPowerEntry": lldpV2Xdot3LocPowerEntry,
       "lldpV2Xdot3LocPowerPortClass": lldpV2Xdot3LocPowerPortClass,
       "lldpV2Xdot3LocPowerMDISupported": lldpV2Xdot3LocPowerMDISupported,
       "lldpV2Xdot3LocPowerMDIEnabled": lldpV2Xdot3LocPowerMDIEnabled,
       "lldpV2Xdot3LocPowerPairControlable": lldpV2Xdot3LocPowerPairControlable,
       "lldpV2Xdot3LocPowerPairs": lldpV2Xdot3LocPowerPairs,
       "lldpV2Xdot3LocPowerClass": lldpV2Xdot3LocPowerClass,
       "lldpV2Xdot3LocPowerType": lldpV2Xdot3LocPowerType,
       "lldpV2Xdot3LocPowerSource": lldpV2Xdot3LocPowerSource,
       "lldpV2Xdot3LocPowerPriority": lldpV2Xdot3LocPowerPriority,
       "lldpV2Xdot3LocPDRequestedPowerValue": lldpV2Xdot3LocPDRequestedPowerValue,
       "lldpV2Xdot3LocPSEAllocatedPowerValue": lldpV2Xdot3LocPSEAllocatedPowerValue,
       "lldpV2Xdot3LocResponseTime": lldpV2Xdot3LocResponseTime,
       "lldpV2Xdot3LocReady": lldpV2Xdot3LocReady,
       "lldpV2Xdot3LocReducedOperationPowerValue": lldpV2Xdot3LocReducedOperationPowerValue,
       "lldpV2Xdot3LocMaxFrameSizeTable": lldpV2Xdot3LocMaxFrameSizeTable,
       "lldpV2Xdot3LocMaxFrameSizeEntry": lldpV2Xdot3LocMaxFrameSizeEntry,
       "lldpV2Xdot3LocMaxFrameSize": lldpV2Xdot3LocMaxFrameSize,
       "lldpV2Xdot3LocEEETable": lldpV2Xdot3LocEEETable,
       "lldpV2Xdot3LocEEEEntry": lldpV2Xdot3LocEEEEntry,
       "lldpV2Xdot3LocTxTwSys": lldpV2Xdot3LocTxTwSys,
       "lldpV2Xdot3LocTxTwSysEcho": lldpV2Xdot3LocTxTwSysEcho,
       "lldpV2Xdot3LocRxTwSys": lldpV2Xdot3LocRxTwSys,
       "lldpV2Xdot3LocRxTwSysEcho": lldpV2Xdot3LocRxTwSysEcho,
       "lldpV2Xdot3LocFbTwSys": lldpV2Xdot3LocFbTwSys,
       "lldpV2Xdot3TxDllReady": lldpV2Xdot3TxDllReady,
       "lldpV2Xdot3RxDllReady": lldpV2Xdot3RxDllReady,
       "lldpV2Xdot3LocDllEnabled": lldpV2Xdot3LocDllEnabled,
       "lldpV2Xdot3RemoteData": lldpV2Xdot3RemoteData,
       "lldpV2Xdot3RemPortTable": lldpV2Xdot3RemPortTable,
       "lldpV2Xdot3RemPortEntry": lldpV2Xdot3RemPortEntry,
       "lldpV2Xdot3RemPortAutoNegSupported": lldpV2Xdot3RemPortAutoNegSupported,
       "lldpV2Xdot3RemPortAutoNegEnabled": lldpV2Xdot3RemPortAutoNegEnabled,
       "lldpV2Xdot3RemPortAutoNegAdvertisedCap": lldpV2Xdot3RemPortAutoNegAdvertisedCap,
       "lldpV2Xdot3RemPortOperMauType": lldpV2Xdot3RemPortOperMauType,
       "lldpV2Xdot3RemPowerTable": lldpV2Xdot3RemPowerTable,
       "lldpV2Xdot3RemPowerEntry": lldpV2Xdot3RemPowerEntry,
       "lldpV2Xdot3RemPowerPortClass": lldpV2Xdot3RemPowerPortClass,
       "lldpV2Xdot3RemPowerMDISupported": lldpV2Xdot3RemPowerMDISupported,
       "lldpV2Xdot3RemPowerMDIEnabled": lldpV2Xdot3RemPowerMDIEnabled,
       "lldpV2Xdot3RemPowerPairControlable": lldpV2Xdot3RemPowerPairControlable,
       "lldpV2Xdot3RemPowerPairs": lldpV2Xdot3RemPowerPairs,
       "lldpV2Xdot3RemPowerClass": lldpV2Xdot3RemPowerClass,
       "lldpV2Xdot3RemPowerType": lldpV2Xdot3RemPowerType,
       "lldpV2Xdot3RemPowerSource": lldpV2Xdot3RemPowerSource,
       "lldpV2Xdot3RemPowerPriority": lldpV2Xdot3RemPowerPriority,
       "lldpV2Xdot3RemPDRequestedPowerValue": lldpV2Xdot3RemPDRequestedPowerValue,
       "lldpV2Xdot3RemPSEAllocatedPowerValue": lldpV2Xdot3RemPSEAllocatedPowerValue,
       "lldpV2Xdot3RemMaxFrameSizeTable": lldpV2Xdot3RemMaxFrameSizeTable,
       "lldpV2Xdot3RemMaxFrameSizeEntry": lldpV2Xdot3RemMaxFrameSizeEntry,
       "lldpV2Xdot3RemMaxFrameSize": lldpV2Xdot3RemMaxFrameSize,
       "lldpV2Xdot3RemEEETable": lldpV2Xdot3RemEEETable,
       "lldpV2Xdot3RemEEEEntry": lldpV2Xdot3RemEEEEntry,
       "lldpV2Xdot3RemTxTwSys": lldpV2Xdot3RemTxTwSys,
       "lldpV2Xdot3RemTxTwSysEcho": lldpV2Xdot3RemTxTwSysEcho,
       "lldpV2Xdot3RemRxTwSys": lldpV2Xdot3RemRxTwSys,
       "lldpV2Xdot3RemRxTwSysEcho": lldpV2Xdot3RemRxTwSysEcho,
       "lldpV2Xdot3RemFbTwSys": lldpV2Xdot3RemFbTwSys,
       "lldpV2Xdot3Conformance": lldpV2Xdot3Conformance,
       "lldpV2Xdot3Compliances": lldpV2Xdot3Compliances,
       "lldpV2Xdot3TxRxCompliance": lldpV2Xdot3TxRxCompliance,
       "lldpV2Xdot3TxCompliance": lldpV2Xdot3TxCompliance,
       "lldpV2Xdot3RxCompliance": lldpV2Xdot3RxCompliance,
       "lldpV2Xdot3Groups": lldpV2Xdot3Groups,
       "lldpV2Xdot3ConfigGroup": lldpV2Xdot3ConfigGroup,
       "lldpV2Xdot3LocSysGroup": lldpV2Xdot3LocSysGroup,
       "lldpV2Xdot3RemSysGroup": lldpV2Xdot3RemSysGroup}
)
