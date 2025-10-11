# SNMP MIB module (ADTRAN-GENIGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENIGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:43 2025
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

(adGenEthernetDslamFlowName,) = mibBuilder.importSymbols(
    "ADTRAN-ETHERNET-DSLAM-FLOW-MIB",
    "adGenEthernetDslamFlowName")

(adGenEVCName,) = mibBuilder.importSymbols(
    "ADTRAN-GENEVC-MIB",
    "adGenEVCName")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenIGMP,
 adGenIGMPID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenIGMP",
    "adGenIGMPID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenIGMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 16, 1)
)
if mibBuilder.loadTexts:
    adGenIGMPMIB.setRevisions(
        ("2013-05-02 00:00",
         "2013-02-20 00:00",
         "2013-02-04 00:00",
         "2010-06-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenIGMPProvisioning_ObjectIdentity = ObjectIdentity
adGenIGMPProvisioning = _AdGenIGMPProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1)
)
_AdGenIGMPEVCTable_Object = MibTable
adGenIGMPEVCTable = _AdGenIGMPEVCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 1)
)
if mibBuilder.loadTexts:
    adGenIGMPEVCTable.setStatus("current")
_AdGenIGMPEVCEntry_Object = MibTableRow
adGenIGMPEVCEntry = _AdGenIGMPEVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 1, 1)
)
adGenIGMPEVCEntry.setIndexNames(
    (1, "ADTRAN-GENEVC-MIB", "adGenEVCName"),
)
if mibBuilder.loadTexts:
    adGenIGMPEVCEntry.setStatus("current")


class _AdGenIGMPEVCPriority_Type(Integer32):
    """Custom type adGenIGMPEVCPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenIGMPEVCPriority_Type.__name__ = "Integer32"
_AdGenIGMPEVCPriority_Object = MibTableColumn
adGenIGMPEVCPriority = _AdGenIGMPEVCPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 1, 1, 1),
    _AdGenIGMPEVCPriority_Type()
)
adGenIGMPEVCPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCPriority.setStatus("current")


class _AdGenIGMPEVCVersion_Type(Integer32):
    """Custom type adGenIGMPEVCVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3lite", 3))
    )


_AdGenIGMPEVCVersion_Type.__name__ = "Integer32"
_AdGenIGMPEVCVersion_Object = MibTableColumn
adGenIGMPEVCVersion = _AdGenIGMPEVCVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 1, 1, 2),
    _AdGenIGMPEVCVersion_Type()
)
adGenIGMPEVCVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCVersion.setStatus("current")
_AdGenIGMPEVCSlotTable_Object = MibTable
adGenIGMPEVCSlotTable = _AdGenIGMPEVCSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2)
)
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotTable.setStatus("current")
_AdGenIGMPEVCSlotEntry_Object = MibTableRow
adGenIGMPEVCSlotEntry = _AdGenIGMPEVCSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1)
)
adGenIGMPEVCSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENEVC-MIB", "adGenEVCName"),
)
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotEntry.setStatus("current")
_AdGenIGMPEVCSlotHostIP_Type = IpAddress
_AdGenIGMPEVCSlotHostIP_Object = MibTableColumn
adGenIGMPEVCSlotHostIP = _AdGenIGMPEVCSlotHostIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 1),
    _AdGenIGMPEVCSlotHostIP_Type()
)
adGenIGMPEVCSlotHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotHostIP.setStatus("current")


class _AdGenIGMPEVCSlotLastMemberQueryInterval_Type(Integer32):
    """Custom type adGenIGMPEVCSlotLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_AdGenIGMPEVCSlotLastMemberQueryInterval_Type.__name__ = "Integer32"
_AdGenIGMPEVCSlotLastMemberQueryInterval_Object = MibTableColumn
adGenIGMPEVCSlotLastMemberQueryInterval = _AdGenIGMPEVCSlotLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 2),
    _AdGenIGMPEVCSlotLastMemberQueryInterval_Type()
)
adGenIGMPEVCSlotLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotLastMemberQueryInterval.setStatus("current")


class _AdGenIGMPEVCSlotLastMemberQueryCount_Type(Integer32):
    """Custom type adGenIGMPEVCSlotLastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenIGMPEVCSlotLastMemberQueryCount_Type.__name__ = "Integer32"
_AdGenIGMPEVCSlotLastMemberQueryCount_Object = MibTableColumn
adGenIGMPEVCSlotLastMemberQueryCount = _AdGenIGMPEVCSlotLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 3),
    _AdGenIGMPEVCSlotLastMemberQueryCount_Type()
)
adGenIGMPEVCSlotLastMemberQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotLastMemberQueryCount.setStatus("current")


class _AdGenIGMPEVCSlotMode_Type(Integer32):
    """Custom type adGenIGMPEVCSlotMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snooping", 1),
          ("proxy", 2),
          ("transparent", 3))
    )


_AdGenIGMPEVCSlotMode_Type.__name__ = "Integer32"
_AdGenIGMPEVCSlotMode_Object = MibTableColumn
adGenIGMPEVCSlotMode = _AdGenIGMPEVCSlotMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 4),
    _AdGenIGMPEVCSlotMode_Type()
)
adGenIGMPEVCSlotMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotMode.setStatus("current")
_AdGenIGMPEVCSlotRowStatus_Type = RowStatus
_AdGenIGMPEVCSlotRowStatus_Object = MibTableColumn
adGenIGMPEVCSlotRowStatus = _AdGenIGMPEVCSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 5),
    _AdGenIGMPEVCSlotRowStatus_Type()
)
adGenIGMPEVCSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotRowStatus.setStatus("current")
_AdGenIGMPEVCSlotStatus_Type = DisplayString
_AdGenIGMPEVCSlotStatus_Object = MibTableColumn
adGenIGMPEVCSlotStatus = _AdGenIGMPEVCSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 6),
    _AdGenIGMPEVCSlotStatus_Type()
)
adGenIGMPEVCSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotStatus.setStatus("current")
_AdGenIGMPEVCSlotLastError_Type = DisplayString
_AdGenIGMPEVCSlotLastError_Object = MibTableColumn
adGenIGMPEVCSlotLastError = _AdGenIGMPEVCSlotLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 2, 1, 7),
    _AdGenIGMPEVCSlotLastError_Type()
)
adGenIGMPEVCSlotLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIGMPEVCSlotLastError.setStatus("current")
_AdGenIGMPEVCMapTable_Object = MibTable
adGenIGMPEVCMapTable = _AdGenIGMPEVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3)
)
if mibBuilder.loadTexts:
    adGenIGMPEVCMapTable.setStatus("current")
_AdGenIGMPEVCMapEntry_Object = MibTableRow
adGenIGMPEVCMapEntry = _AdGenIGMPEVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1)
)
adGenIGMPEVCMapEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowName"),
)
if mibBuilder.loadTexts:
    adGenIGMPEVCMapEntry.setStatus("current")


class _AdGenIGMPEVCMapMode_Type(Integer32):
    """Custom type adGenIGMPEVCMapMode based on Integer32"""
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
        *(("processingEnabled", 1),
          ("block", 2),
          ("transparent", 3),
          ("forking", 4))
    )


_AdGenIGMPEVCMapMode_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapMode_Object = MibTableColumn
adGenIGMPEVCMapMode = _AdGenIGMPEVCMapMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 1),
    _AdGenIGMPEVCMapMode_Type()
)
adGenIGMPEVCMapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMode.setStatus("current")
_AdGenIGMPEVCMapMaxMulticastBandwidth_Type = Integer32
_AdGenIGMPEVCMapMaxMulticastBandwidth_Object = MibTableColumn
adGenIGMPEVCMapMaxMulticastBandwidth = _AdGenIGMPEVCMapMaxMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 2),
    _AdGenIGMPEVCMapMaxMulticastBandwidth_Type()
)
adGenIGMPEVCMapMaxMulticastBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMaxMulticastBandwidth.setStatus("current")


class _AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type(Integer32):
    """Custom type adGenIGMPEVCMapMaxMulticastBandwidthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Object = MibTableColumn
adGenIGMPEVCMapMaxMulticastBandwidthEnable = _AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 3),
    _AdGenIGMPEVCMapMaxMulticastBandwidthEnable_Type()
)
adGenIGMPEVCMapMaxMulticastBandwidthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMaxMulticastBandwidthEnable.setStatus("current")
_AdGenIGMPEVCMapMaxMulticastGroups_Type = Integer32
_AdGenIGMPEVCMapMaxMulticastGroups_Object = MibTableColumn
adGenIGMPEVCMapMaxMulticastGroups = _AdGenIGMPEVCMapMaxMulticastGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 4),
    _AdGenIGMPEVCMapMaxMulticastGroups_Type()
)
adGenIGMPEVCMapMaxMulticastGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMaxMulticastGroups.setStatus("current")


class _AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type(Integer32):
    """Custom type adGenIGMPEVCMapMaxMulticastGroupsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapMaxMulticastGroupsEnable_Object = MibTableColumn
adGenIGMPEVCMapMaxMulticastGroupsEnable = _AdGenIGMPEVCMapMaxMulticastGroupsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 5),
    _AdGenIGMPEVCMapMaxMulticastGroupsEnable_Type()
)
adGenIGMPEVCMapMaxMulticastGroupsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMaxMulticastGroupsEnable.setStatus("current")
_AdGenIGMPEVCMapRouterIP_Type = IpAddress
_AdGenIGMPEVCMapRouterIP_Object = MibTableColumn
adGenIGMPEVCMapRouterIP = _AdGenIGMPEVCMapRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 6),
    _AdGenIGMPEVCMapRouterIP_Type()
)
adGenIGMPEVCMapRouterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapRouterIP.setStatus("current")


class _AdGenIGMPEVCMapImmediateLeave_Type(Integer32):
    """Custom type adGenIGMPEVCMapImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenIGMPEVCMapImmediateLeave_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapImmediateLeave_Object = MibTableColumn
adGenIGMPEVCMapImmediateLeave = _AdGenIGMPEVCMapImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 7),
    _AdGenIGMPEVCMapImmediateLeave_Type()
)
adGenIGMPEVCMapImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapImmediateLeave.setStatus("current")


class _AdGenIGMPEVCMapMulticastACLMode_Type(Integer32):
    """Custom type adGenIGMPEVCMapMulticastACLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("disabled", 3))
    )


_AdGenIGMPEVCMapMulticastACLMode_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapMulticastACLMode_Object = MibTableColumn
adGenIGMPEVCMapMulticastACLMode = _AdGenIGMPEVCMapMulticastACLMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 8),
    _AdGenIGMPEVCMapMulticastACLMode_Type()
)
adGenIGMPEVCMapMulticastACLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMulticastACLMode.setStatus("current")


class _AdGenIGMPEVCMapMulticastACLName_Type(DisplayString):
    """Custom type adGenIGMPEVCMapMulticastACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenIGMPEVCMapMulticastACLName_Type.__name__ = "DisplayString"
_AdGenIGMPEVCMapMulticastACLName_Object = MibTableColumn
adGenIGMPEVCMapMulticastACLName = _AdGenIGMPEVCMapMulticastACLName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 9),
    _AdGenIGMPEVCMapMulticastACLName_Type()
)
adGenIGMPEVCMapMulticastACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapMulticastACLName.setStatus("current")


class _AdGenIGMPEVCMapAuthentication_Type(Integer32):
    """Custom type adGenIGMPEVCMapAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenIGMPEVCMapAuthentication_Type.__name__ = "Integer32"
_AdGenIGMPEVCMapAuthentication_Object = MibTableColumn
adGenIGMPEVCMapAuthentication = _AdGenIGMPEVCMapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 16, 1, 3, 1, 10),
    _AdGenIGMPEVCMapAuthentication_Type()
)
adGenIGMPEVCMapAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIGMPEVCMapAuthentication.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENIGMP-MIB",
    **{"adGenIGMPProvisioning": adGenIGMPProvisioning,
       "adGenIGMPEVCTable": adGenIGMPEVCTable,
       "adGenIGMPEVCEntry": adGenIGMPEVCEntry,
       "adGenIGMPEVCPriority": adGenIGMPEVCPriority,
       "adGenIGMPEVCVersion": adGenIGMPEVCVersion,
       "adGenIGMPEVCSlotTable": adGenIGMPEVCSlotTable,
       "adGenIGMPEVCSlotEntry": adGenIGMPEVCSlotEntry,
       "adGenIGMPEVCSlotHostIP": adGenIGMPEVCSlotHostIP,
       "adGenIGMPEVCSlotLastMemberQueryInterval": adGenIGMPEVCSlotLastMemberQueryInterval,
       "adGenIGMPEVCSlotLastMemberQueryCount": adGenIGMPEVCSlotLastMemberQueryCount,
       "adGenIGMPEVCSlotMode": adGenIGMPEVCSlotMode,
       "adGenIGMPEVCSlotRowStatus": adGenIGMPEVCSlotRowStatus,
       "adGenIGMPEVCSlotStatus": adGenIGMPEVCSlotStatus,
       "adGenIGMPEVCSlotLastError": adGenIGMPEVCSlotLastError,
       "adGenIGMPEVCMapTable": adGenIGMPEVCMapTable,
       "adGenIGMPEVCMapEntry": adGenIGMPEVCMapEntry,
       "adGenIGMPEVCMapMode": adGenIGMPEVCMapMode,
       "adGenIGMPEVCMapMaxMulticastBandwidth": adGenIGMPEVCMapMaxMulticastBandwidth,
       "adGenIGMPEVCMapMaxMulticastBandwidthEnable": adGenIGMPEVCMapMaxMulticastBandwidthEnable,
       "adGenIGMPEVCMapMaxMulticastGroups": adGenIGMPEVCMapMaxMulticastGroups,
       "adGenIGMPEVCMapMaxMulticastGroupsEnable": adGenIGMPEVCMapMaxMulticastGroupsEnable,
       "adGenIGMPEVCMapRouterIP": adGenIGMPEVCMapRouterIP,
       "adGenIGMPEVCMapImmediateLeave": adGenIGMPEVCMapImmediateLeave,
       "adGenIGMPEVCMapMulticastACLMode": adGenIGMPEVCMapMulticastACLMode,
       "adGenIGMPEVCMapMulticastACLName": adGenIGMPEVCMapMulticastACLName,
       "adGenIGMPEVCMapAuthentication": adGenIGMPEVCMapAuthentication,
       "adGenIGMPMIB": adGenIGMPMIB}
)
