# SNMP MIB module (SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/SESSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:27 2025
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(FeatureStatus,
 RowStatus,
 TruthValue,
 rndErrorDesc,
 rndErrorSeverity,
 rsSESSION) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "FeatureStatus",
    "RowStatus",
    "TruthValue",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsSESSION")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSESSIONSessionTableStatus_Type = FeatureStatus
_RsSESSIONSessionTableStatus_Object = MibScalar
rsSESSIONSessionTableStatus = _RsSESSIONSessionTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 1),
    _RsSESSIONSessionTableStatus_Type()
)
rsSESSIONSessionTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableStatus.setStatus("mandatory")


class _RsSESSIONSessionTableLookupMode_Type(Integer32):
    """Custom type rsSESSIONSessionTableLookupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullLayer4", 1),
          ("fullLayer3", 2),
          ("destLayer4Port", 3))
    )


_RsSESSIONSessionTableLookupMode_Type.__name__ = "Integer32"
_RsSESSIONSessionTableLookupMode_Object = MibScalar
rsSESSIONSessionTableLookupMode = _RsSESSIONSessionTableLookupMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 2),
    _RsSESSIONSessionTableLookupMode_Type()
)
rsSESSIONSessionTableLookupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableLookupMode.setStatus("mandatory")
_RsSESSIONRemoveEntryAtSessionEnd_Type = FeatureStatus
_RsSESSIONRemoveEntryAtSessionEnd_Object = MibScalar
rsSESSIONRemoveEntryAtSessionEnd = _RsSESSIONRemoveEntryAtSessionEnd_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 3),
    _RsSESSIONRemoveEntryAtSessionEnd_Type()
)
rsSESSIONRemoveEntryAtSessionEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONRemoveEntryAtSessionEnd.setStatus("mandatory")


class _RsSESSIONSynProtectionStatus_Type(Integer32):
    """Custom type rsSESSIONSynProtectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("standby", 3))
    )


_RsSESSIONSynProtectionStatus_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionStatus_Object = MibScalar
rsSESSIONSynProtectionStatus = _RsSESSIONSynProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 4),
    _RsSESSIONSynProtectionStatus_Type()
)
rsSESSIONSynProtectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatus.setStatus("mandatory")


class _RsSESSIONSynProtectionTimeout_Type(Integer32):
    """Custom type rsSESSIONSynProtectionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsSESSIONSynProtectionTimeout_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionTimeout_Object = MibScalar
rsSESSIONSynProtectionTimeout = _RsSESSIONSynProtectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 5),
    _RsSESSIONSynProtectionTimeout_Type()
)
rsSESSIONSynProtectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionTimeout.setStatus("mandatory")


class _RsSESSIONSynProtectionActivationBound_Type(Integer32):
    """Custom type rsSESSIONSynProtectionActivationBound based on Integer32"""
    defaultValue = 30


_RsSESSIONSynProtectionActivationBound_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionActivationBound_Object = MibScalar
rsSESSIONSynProtectionActivationBound = _RsSESSIONSynProtectionActivationBound_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 6),
    _RsSESSIONSynProtectionActivationBound_Type()
)
rsSESSIONSynProtectionActivationBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionActivationBound.setStatus("mandatory")
_RsSESSIONSynProtectionDeactivationBound_Type = Integer32
_RsSESSIONSynProtectionDeactivationBound_Object = MibScalar
rsSESSIONSynProtectionDeactivationBound = _RsSESSIONSynProtectionDeactivationBound_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 7),
    _RsSESSIONSynProtectionDeactivationBound_Type()
)
rsSESSIONSynProtectionDeactivationBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionDeactivationBound.setStatus("mandatory")


class _RsSESSIONSynProtectionTrackingTime_Type(Integer32):
    """Custom type rsSESSIONSynProtectionTrackingTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsSESSIONSynProtectionTrackingTime_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionTrackingTime_Object = MibScalar
rsSESSIONSynProtectionTrackingTime = _RsSESSIONSynProtectionTrackingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 8),
    _RsSESSIONSynProtectionTrackingTime_Type()
)
rsSESSIONSynProtectionTrackingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionTrackingTime.setStatus("mandatory")
_RsSESSIONSynProtectionMinSynForTrigger_Type = Integer32
_RsSESSIONSynProtectionMinSynForTrigger_Object = MibScalar
rsSESSIONSynProtectionMinSynForTrigger = _RsSESSIONSynProtectionMinSynForTrigger_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 9),
    _RsSESSIONSynProtectionMinSynForTrigger_Type()
)
rsSESSIONSynProtectionMinSynForTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionMinSynForTrigger.setStatus("mandatory")
_RsSESSIONSynTriggerTable_Object = MibTable
rsSESSIONSynTriggerTable = _RsSESSIONSynTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10)
)
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerTable.setStatus("mandatory")
_RsSESSIONSynTriggerEntry_Object = MibTableRow
rsSESSIONSynTriggerEntry = _RsSESSIONSynTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1)
)
rsSESSIONSynTriggerEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSynTriggerIP"),
    (0, "SESSION-MIB", "rsSESSIONSynTriggerPort"),
    (0, "SESSION-MIB", "rsSESSIONSynTriggerRxport"),
)
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerEntry.setStatus("mandatory")
_RsSESSIONSynTriggerIP_Type = IpAddress
_RsSESSIONSynTriggerIP_Object = MibTableColumn
rsSESSIONSynTriggerIP = _RsSESSIONSynTriggerIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 1),
    _RsSESSIONSynTriggerIP_Type()
)
rsSESSIONSynTriggerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerIP.setStatus("mandatory")


class _RsSESSIONSynTriggerPort_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPort based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerPort_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPort_Object = MibTableColumn
rsSESSIONSynTriggerPort = _RsSESSIONSynTriggerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 2),
    _RsSESSIONSynTriggerPort_Type()
)
rsSESSIONSynTriggerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPort.setStatus("mandatory")


class _RsSESSIONSynTriggerRxport_Type(Integer32):
    """Custom type rsSESSIONSynTriggerRxport based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerRxport_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerRxport_Object = MibTableColumn
rsSESSIONSynTriggerRxport = _RsSESSIONSynTriggerRxport_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 3),
    _RsSESSIONSynTriggerRxport_Type()
)
rsSESSIONSynTriggerRxport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerRxport.setStatus("mandatory")


class _RsSESSIONSynTriggerTime_Type(Integer32):
    """Custom type rsSESSIONSynTriggerTime based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerTime_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerTime_Object = MibTableColumn
rsSESSIONSynTriggerTime = _RsSESSIONSynTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 4),
    _RsSESSIONSynTriggerTime_Type()
)
rsSESSIONSynTriggerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerTime.setStatus("mandatory")


class _RsSESSIONSynTriggerLastSecSYN_Type(Integer32):
    """Custom type rsSESSIONSynTriggerLastSecSYN based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerLastSecSYN_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerLastSecSYN_Object = MibTableColumn
rsSESSIONSynTriggerLastSecSYN = _RsSESSIONSynTriggerLastSecSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 5),
    _RsSESSIONSynTriggerLastSecSYN_Type()
)
rsSESSIONSynTriggerLastSecSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerLastSecSYN.setStatus("mandatory")


class _RsSESSIONSynTriggerLastSecRqst_Type(Integer32):
    """Custom type rsSESSIONSynTriggerLastSecRqst based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerLastSecRqst_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerLastSecRqst_Object = MibTableColumn
rsSESSIONSynTriggerLastSecRqst = _RsSESSIONSynTriggerLastSecRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 6),
    _RsSESSIONSynTriggerLastSecRqst_Type()
)
rsSESSIONSynTriggerLastSecRqst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerLastSecRqst.setStatus("mandatory")


class _RsSESSIONSynTriggerAvrgSYN_Type(Integer32):
    """Custom type rsSESSIONSynTriggerAvrgSYN based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerAvrgSYN_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerAvrgSYN_Object = MibTableColumn
rsSESSIONSynTriggerAvrgSYN = _RsSESSIONSynTriggerAvrgSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 7),
    _RsSESSIONSynTriggerAvrgSYN_Type()
)
rsSESSIONSynTriggerAvrgSYN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerAvrgSYN.setStatus("mandatory")


class _RsSESSIONSynTriggerAvrgRqst_Type(Integer32):
    """Custom type rsSESSIONSynTriggerAvrgRqst based on Integer32"""
    defaultValue = 0


_RsSESSIONSynTriggerAvrgRqst_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerAvrgRqst_Object = MibTableColumn
rsSESSIONSynTriggerAvrgRqst = _RsSESSIONSynTriggerAvrgRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 10, 1, 8),
    _RsSESSIONSynTriggerAvrgRqst_Type()
)
rsSESSIONSynTriggerAvrgRqst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerAvrgRqst.setStatus("mandatory")
_RsSESSIONTuning_ObjectIdentity = ObjectIdentity
rsSESSIONTuning = _RsSESSIONTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11)
)
_RsSESSIONSynProtectionTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSynProtectionTuning = _RsSESSIONSynProtectionTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 1)
)
_RsSESSIONSynProtectionEntries_Type = Integer32
_RsSESSIONSynProtectionEntries_Object = MibScalar
rsSESSIONSynProtectionEntries = _RsSESSIONSynProtectionEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 1, 1),
    _RsSESSIONSynProtectionEntries_Type()
)
rsSESSIONSynProtectionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionEntries.setStatus("mandatory")
_RsSESSIONSynProtectionEntriesAfterReset_Type = Integer32
_RsSESSIONSynProtectionEntriesAfterReset_Object = MibScalar
rsSESSIONSynProtectionEntriesAfterReset = _RsSESSIONSynProtectionEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 1, 2),
    _RsSESSIONSynProtectionEntriesAfterReset_Type()
)
rsSESSIONSynProtectionEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSynProtectionRqstsTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSynProtectionRqstsTuning = _RsSESSIONSynProtectionRqstsTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 2)
)
_RsSESSIONSynProtectionRqstsEntries_Type = Integer32
_RsSESSIONSynProtectionRqstsEntries_Object = MibScalar
rsSESSIONSynProtectionRqstsEntries = _RsSESSIONSynProtectionRqstsEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 2, 1),
    _RsSESSIONSynProtectionRqstsEntries_Type()
)
rsSESSIONSynProtectionRqstsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionRqstsEntries.setStatus("mandatory")
_RsSESSIONSynProtectionRqstsEntriesAfterReset_Type = Integer32
_RsSESSIONSynProtectionRqstsEntriesAfterReset_Object = MibScalar
rsSESSIONSynProtectionRqstsEntriesAfterReset = _RsSESSIONSynProtectionRqstsEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 2, 2),
    _RsSESSIONSynProtectionRqstsEntriesAfterReset_Type()
)
rsSESSIONSynProtectionRqstsEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionRqstsEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSynProtectionTriggerTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSynProtectionTriggerTuning = _RsSESSIONSynProtectionTriggerTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 3)
)
_RsSESSIONSynProtectionTriggerEntries_Type = Integer32
_RsSESSIONSynProtectionTriggerEntries_Object = MibScalar
rsSESSIONSynProtectionTriggerEntries = _RsSESSIONSynProtectionTriggerEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 3, 1),
    _RsSESSIONSynProtectionTriggerEntries_Type()
)
rsSESSIONSynProtectionTriggerEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionTriggerEntries.setStatus("mandatory")
_RsSESSIONSynProtectionTriggerEntriesAfterReset_Type = Integer32
_RsSESSIONSynProtectionTriggerEntriesAfterReset_Object = MibScalar
rsSESSIONSynProtectionTriggerEntriesAfterReset = _RsSESSIONSynProtectionTriggerEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 3, 2),
    _RsSESSIONSynProtectionTriggerEntriesAfterReset_Type()
)
rsSESSIONSynProtectionTriggerEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionTriggerEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSynProtectionPolicyTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSynProtectionPolicyTuning = _RsSESSIONSynProtectionPolicyTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 4)
)
_RsSESSIONSynProtectionPolicyEntries_Type = Integer32
_RsSESSIONSynProtectionPolicyEntries_Object = MibScalar
rsSESSIONSynProtectionPolicyEntries = _RsSESSIONSynProtectionPolicyEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 4, 1),
    _RsSESSIONSynProtectionPolicyEntries_Type()
)
rsSESSIONSynProtectionPolicyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionPolicyEntries.setStatus("mandatory")
_RsSESSIONSynProtectionPolicyEntriesAfterReset_Type = Integer32
_RsSESSIONSynProtectionPolicyEntriesAfterReset_Object = MibScalar
rsSESSIONSynProtectionPolicyEntriesAfterReset = _RsSESSIONSynProtectionPolicyEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 4, 2),
    _RsSESSIONSynProtectionPolicyEntriesAfterReset_Type()
)
rsSESSIONSynProtectionPolicyEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionPolicyEntriesAfterReset.setStatus("mandatory")
_RsSESSIONPasvProtocolsTuning_ObjectIdentity = ObjectIdentity
rsSESSIONPasvProtocolsTuning = _RsSESSIONPasvProtocolsTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 5)
)
_RsSESSIONPasvProtocolsEntries_Type = Integer32
_RsSESSIONPasvProtocolsEntries_Object = MibScalar
rsSESSIONPasvProtocolsEntries = _RsSESSIONPasvProtocolsEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 5, 1),
    _RsSESSIONPasvProtocolsEntries_Type()
)
rsSESSIONPasvProtocolsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONPasvProtocolsEntries.setStatus("mandatory")
_RsSESSIONPasvProtocolsEntriesAfterReset_Type = Integer32
_RsSESSIONPasvProtocolsEntriesAfterReset_Object = MibScalar
rsSESSIONPasvProtocolsEntriesAfterReset = _RsSESSIONPasvProtocolsEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 5, 2),
    _RsSESSIONPasvProtocolsEntriesAfterReset_Type()
)
rsSESSIONPasvProtocolsEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONPasvProtocolsEntriesAfterReset.setStatus("mandatory")
_RsSESSIONL3SynFloodReportTuning_ObjectIdentity = ObjectIdentity
rsSESSIONL3SynFloodReportTuning = _RsSESSIONL3SynFloodReportTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 6)
)
_RsSESSIONL3SynFloodReportEntries_Type = Integer32
_RsSESSIONL3SynFloodReportEntries_Object = MibScalar
rsSESSIONL3SynFloodReportEntries = _RsSESSIONL3SynFloodReportEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 6, 1),
    _RsSESSIONL3SynFloodReportEntries_Type()
)
rsSESSIONL3SynFloodReportEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONL3SynFloodReportEntries.setStatus("mandatory")
_RsSESSIONL3SynFloodReportEntriesAfterReset_Type = Integer32
_RsSESSIONL3SynFloodReportEntriesAfterReset_Object = MibScalar
rsSESSIONL3SynFloodReportEntriesAfterReset = _RsSESSIONL3SynFloodReportEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 6, 2),
    _RsSESSIONL3SynFloodReportEntriesAfterReset_Type()
)
rsSESSIONL3SynFloodReportEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONL3SynFloodReportEntriesAfterReset.setStatus("mandatory")
_RsSESSIONTableSynFloodTriggersTuning_ObjectIdentity = ObjectIdentity
rsSESSIONTableSynFloodTriggersTuning = _RsSESSIONTableSynFloodTriggersTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 7)
)
_RsSESSIONTableSynFloodTriggersEntries_Type = Integer32
_RsSESSIONTableSynFloodTriggersEntries_Object = MibScalar
rsSESSIONTableSynFloodTriggersEntries = _RsSESSIONTableSynFloodTriggersEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 7, 1),
    _RsSESSIONTableSynFloodTriggersEntries_Type()
)
rsSESSIONTableSynFloodTriggersEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONTableSynFloodTriggersEntries.setStatus("mandatory")
_RsSESSIONTableSynFloodTriggersEntriesAfterReset_Type = Integer32
_RsSESSIONTableSynFloodTriggersEntriesAfterReset_Object = MibScalar
rsSESSIONTableSynFloodTriggersEntriesAfterReset = _RsSESSIONTableSynFloodTriggersEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 7, 2),
    _RsSESSIONTableSynFloodTriggersEntriesAfterReset_Type()
)
rsSESSIONTableSynFloodTriggersEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableSynFloodTriggersEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSessionTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSessionTuning = _RsSESSIONSessionTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 8)
)
_RsSESSIONSessionEntries_Type = Integer32
_RsSESSIONSessionEntries_Object = MibScalar
rsSESSIONSessionEntries = _RsSESSIONSessionEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 8, 1),
    _RsSESSIONSessionEntries_Type()
)
rsSESSIONSessionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSessionEntries.setStatus("mandatory")
_RsSESSIONSessionEntriesAfterReset_Type = Integer32
_RsSESSIONSessionEntriesAfterReset_Object = MibScalar
rsSESSIONSessionEntriesAfterReset = _RsSESSIONSessionEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 8, 2),
    _RsSESSIONSessionEntriesAfterReset_Type()
)
rsSESSIONSessionEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionEntriesAfterReset.setStatus("mandatory")
_RsSESSIONAckReflectionTableTuning_ObjectIdentity = ObjectIdentity
rsSESSIONAckReflectionTableTuning = _RsSESSIONAckReflectionTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 9)
)
_RsSESSIONAckReflectionTableEntries_Type = Integer32
_RsSESSIONAckReflectionTableEntries_Object = MibScalar
rsSESSIONAckReflectionTableEntries = _RsSESSIONAckReflectionTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 9, 1),
    _RsSESSIONAckReflectionTableEntries_Type()
)
rsSESSIONAckReflectionTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONAckReflectionTableEntries.setStatus("mandatory")
_RsSESSIONAckReflectionTableEntriesAfterReset_Type = Integer32
_RsSESSIONAckReflectionTableEntriesAfterReset_Object = MibScalar
rsSESSIONAckReflectionTableEntriesAfterReset = _RsSESSIONAckReflectionTableEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 9, 2),
    _RsSESSIONAckReflectionTableEntriesAfterReset_Type()
)
rsSESSIONAckReflectionTableEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONAckReflectionTableEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSynProtectionStatsTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSynProtectionStatsTuning = _RsSESSIONSynProtectionStatsTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 10)
)


class _RsSESSIONSynProtectionStatsEntries_Type(Integer32):
    """Custom type rsSESSIONSynProtectionStatsEntries based on Integer32"""
    defaultValue = 100


_RsSESSIONSynProtectionStatsEntries_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionStatsEntries_Object = MibScalar
rsSESSIONSynProtectionStatsEntries = _RsSESSIONSynProtectionStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 10, 1),
    _RsSESSIONSynProtectionStatsEntries_Type()
)
rsSESSIONSynProtectionStatsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatsEntries.setStatus("mandatory")


class _RsSESSIONSynProtectionStatsEntriesAfterReset_Type(Integer32):
    """Custom type rsSESSIONSynProtectionStatsEntriesAfterReset based on Integer32"""
    defaultValue = 100


_RsSESSIONSynProtectionStatsEntriesAfterReset_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionStatsEntriesAfterReset_Object = MibScalar
rsSESSIONSynProtectionStatsEntriesAfterReset = _RsSESSIONSynProtectionStatsEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 10, 2),
    _RsSESSIONSynProtectionStatsEntriesAfterReset_Type()
)
rsSESSIONSynProtectionStatsEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatsEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSessionResetsTableTuning_ObjectIdentity = ObjectIdentity
rsSESSIONSessionResetsTableTuning = _RsSESSIONSessionResetsTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 11)
)
_RsSESSIONSessionResetsEntries_Type = Integer32
_RsSESSIONSessionResetsEntries_Object = MibScalar
rsSESSIONSessionResetsEntries = _RsSESSIONSessionResetsEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 11, 1),
    _RsSESSIONSessionResetsEntries_Type()
)
rsSESSIONSessionResetsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSessionResetsEntries.setStatus("mandatory")
_RsSESSIONSessionResetsEntriesAfterReset_Type = Integer32
_RsSESSIONSessionResetsEntriesAfterReset_Object = MibScalar
rsSESSIONSessionResetsEntriesAfterReset = _RsSESSIONSessionResetsEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 11, 11, 2),
    _RsSESSIONSessionResetsEntriesAfterReset_Type()
)
rsSESSIONSessionResetsEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionResetsEntriesAfterReset.setStatus("mandatory")
_RsSESSIONSynProtectionPolicyTable_Object = MibTable
rsSESSIONSynProtectionPolicyTable = _RsSESSIONSynProtectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12)
)
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionPolicyTable.setStatus("mandatory")
_RsSESSIONSynProtectionPolicyEntry_Object = MibTableRow
rsSESSIONSynProtectionPolicyEntry = _RsSESSIONSynProtectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1)
)
rsSESSIONSynProtectionPolicyEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSynTriggerPolicyName"),
)
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionPolicyEntry.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyName_Type(DisplayString):
    """Custom type rsSESSIONSynTriggerPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONSynTriggerPolicyName_Type.__name__ = "DisplayString"
_RsSESSIONSynTriggerPolicyName_Object = MibTableColumn
rsSESSIONSynTriggerPolicyName = _RsSESSIONSynTriggerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 1),
    _RsSESSIONSynTriggerPolicyName_Type()
)
rsSESSIONSynTriggerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyName.setStatus("mandatory")
_RsSESSIONSynTriggerPolicyIndex_Type = Integer32
_RsSESSIONSynTriggerPolicyIndex_Object = MibTableColumn
rsSESSIONSynTriggerPolicyIndex = _RsSESSIONSynTriggerPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 2),
    _RsSESSIONSynTriggerPolicyIndex_Type()
)
rsSESSIONSynTriggerPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyIndex.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyDescription_Type(DisplayString):
    """Custom type rsSESSIONSynTriggerPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONSynTriggerPolicyDescription_Type.__name__ = "DisplayString"
_RsSESSIONSynTriggerPolicyDescription_Object = MibTableColumn
rsSESSIONSynTriggerPolicyDescription = _RsSESSIONSynTriggerPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 3),
    _RsSESSIONSynTriggerPolicyDescription_Type()
)
rsSESSIONSynTriggerPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyDescription.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyDestination_Type(DisplayString):
    """Custom type rsSESSIONSynTriggerPolicyDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsSESSIONSynTriggerPolicyDestination_Type.__name__ = "DisplayString"
_RsSESSIONSynTriggerPolicyDestination_Object = MibTableColumn
rsSESSIONSynTriggerPolicyDestination = _RsSESSIONSynTriggerPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 4),
    _RsSESSIONSynTriggerPolicyDestination_Type()
)
rsSESSIONSynTriggerPolicyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyDestination.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyPhysicalPortGroup_Type(DisplayString):
    """Custom type rsSESSIONSynTriggerPolicyPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsSESSIONSynTriggerPolicyPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsSESSIONSynTriggerPolicyPhysicalPortGroup_Object = MibTableColumn
rsSESSIONSynTriggerPolicyPhysicalPortGroup = _RsSESSIONSynTriggerPolicyPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 5),
    _RsSESSIONSynTriggerPolicyPhysicalPortGroup_Type()
)
rsSESSIONSynTriggerPolicyPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyPhysicalPortGroup.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyService_Type(DisplayString):
    """Custom type rsSESSIONSynTriggerPolicyService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsSESSIONSynTriggerPolicyService_Type.__name__ = "DisplayString"
_RsSESSIONSynTriggerPolicyService_Object = MibTableColumn
rsSESSIONSynTriggerPolicyService = _RsSESSIONSynTriggerPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 6),
    _RsSESSIONSynTriggerPolicyService_Type()
)
rsSESSIONSynTriggerPolicyService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyService.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyProtectionMode_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPolicyProtectionMode based on Integer32"""
    defaultValue = 2

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
          ("triggered", 2),
          ("disabled", 3))
    )


_RsSESSIONSynTriggerPolicyProtectionMode_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPolicyProtectionMode_Object = MibTableColumn
rsSESSIONSynTriggerPolicyProtectionMode = _RsSESSIONSynTriggerPolicyProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 7),
    _RsSESSIONSynTriggerPolicyProtectionMode_Type()
)
rsSESSIONSynTriggerPolicyProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyProtectionMode.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyOperationalStatus_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPolicyOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsSESSIONSynTriggerPolicyOperationalStatus_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPolicyOperationalStatus_Object = MibTableColumn
rsSESSIONSynTriggerPolicyOperationalStatus = _RsSESSIONSynTriggerPolicyOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 8),
    _RsSESSIONSynTriggerPolicyOperationalStatus_Type()
)
rsSESSIONSynTriggerPolicyOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyOperationalStatus.setStatus("mandatory")
_RsSESSIONSynTriggerPolicyStatus_Type = RowStatus
_RsSESSIONSynTriggerPolicyStatus_Object = MibTableColumn
rsSESSIONSynTriggerPolicyStatus = _RsSESSIONSynTriggerPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 9),
    _RsSESSIONSynTriggerPolicyStatus_Type()
)
rsSESSIONSynTriggerPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyStatus.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyVerificationType_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPolicyVerificationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("request", 2))
    )


_RsSESSIONSynTriggerPolicyVerificationType_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPolicyVerificationType_Object = MibTableColumn
rsSESSIONSynTriggerPolicyVerificationType = _RsSESSIONSynTriggerPolicyVerificationType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 10),
    _RsSESSIONSynTriggerPolicyVerificationType_Type()
)
rsSESSIONSynTriggerPolicyVerificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyVerificationType.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyActivationThreshold_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPolicyActivationThreshold based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsSESSIONSynTriggerPolicyActivationThreshold_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPolicyActivationThreshold_Object = MibTableColumn
rsSESSIONSynTriggerPolicyActivationThreshold = _RsSESSIONSynTriggerPolicyActivationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 11),
    _RsSESSIONSynTriggerPolicyActivationThreshold_Type()
)
rsSESSIONSynTriggerPolicyActivationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyActivationThreshold.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyDeactivationThreshold_Type(Integer32):
    """Custom type rsSESSIONSynTriggerPolicyDeactivationThreshold based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsSESSIONSynTriggerPolicyDeactivationThreshold_Type.__name__ = "Integer32"
_RsSESSIONSynTriggerPolicyDeactivationThreshold_Object = MibTableColumn
rsSESSIONSynTriggerPolicyDeactivationThreshold = _RsSESSIONSynTriggerPolicyDeactivationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 12),
    _RsSESSIONSynTriggerPolicyDeactivationThreshold_Type()
)
rsSESSIONSynTriggerPolicyDeactivationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyDeactivationThreshold.setStatus("mandatory")


class _RsSESSIONSynTriggerPolicyCountStatistics_Type(FeatureStatus):
    """Custom type rsSESSIONSynTriggerPolicyCountStatistics based on FeatureStatus"""
    defaultValue = 1


_RsSESSIONSynTriggerPolicyCountStatistics_Type.__name__ = "FeatureStatus"
_RsSESSIONSynTriggerPolicyCountStatistics_Object = MibTableColumn
rsSESSIONSynTriggerPolicyCountStatistics = _RsSESSIONSynTriggerPolicyCountStatistics_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 12, 1, 13),
    _RsSESSIONSynTriggerPolicyCountStatistics_Type()
)
rsSESSIONSynTriggerPolicyCountStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerPolicyCountStatistics.setStatus("mandatory")
_RsSESSIONSynProtectionPolicyDummy_Type = Integer32
_RsSESSIONSynProtectionPolicyDummy_Object = MibScalar
rsSESSIONSynProtectionPolicyDummy = _RsSESSIONSynProtectionPolicyDummy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 13),
    _RsSESSIONSynProtectionPolicyDummy_Type()
)
rsSESSIONSynProtectionPolicyDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionPolicyDummy.setStatus("mandatory")
_RsSESSIONSynProtectionAttackAgingTime_Type = Integer32
_RsSESSIONSynProtectionAttackAgingTime_Object = MibScalar
rsSESSIONSynProtectionAttackAgingTime = _RsSESSIONSynProtectionAttackAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 14),
    _RsSESSIONSynProtectionAttackAgingTime_Type()
)
rsSESSIONSynProtectionAttackAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionAttackAgingTime.setStatus("mandatory")
_RsSESSIONSendResetToServer_Type = FeatureStatus
_RsSESSIONSendResetToServer_Object = MibScalar
rsSESSIONSendResetToServer = _RsSESSIONSendResetToServer_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 15),
    _RsSESSIONSendResetToServer_Type()
)
rsSESSIONSendResetToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSendResetToServer.setStatus("mandatory")


class _RsSESSIONSynProtectionGlobalStatisticsStatus_Type(Integer32):
    """Custom type rsSESSIONSynProtectionGlobalStatisticsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsSESSIONSynProtectionGlobalStatisticsStatus_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionGlobalStatisticsStatus_Object = MibScalar
rsSESSIONSynProtectionGlobalStatisticsStatus = _RsSESSIONSynProtectionGlobalStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 16),
    _RsSESSIONSynProtectionGlobalStatisticsStatus_Type()
)
rsSESSIONSynProtectionGlobalStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionGlobalStatisticsStatus.setStatus("mandatory")


class _RsSESSIONSessionAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionAgingTime_Object = MibScalar
rsSESSIONSessionAgingTime = _RsSESSIONSessionAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 17),
    _RsSESSIONSessionAgingTime_Type()
)
rsSESSIONSessionAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionAgingTime.setStatus("mandatory")
_RsSESSIONSessionEntriesNum_Type = Integer32
_RsSESSIONSessionEntriesNum_Object = MibScalar
rsSESSIONSessionEntriesNum = _RsSESSIONSessionEntriesNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 18),
    _RsSESSIONSessionEntriesNum_Type()
)
rsSESSIONSessionEntriesNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionEntriesNum.setStatus("mandatory")


class _RsSESSIONSessionMaxDisplayEntries_Type(Integer32):
    """Custom type rsSESSIONSessionMaxDisplayEntries based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionMaxDisplayEntries_Type.__name__ = "Integer32"
_RsSESSIONSessionMaxDisplayEntries_Object = MibScalar
rsSESSIONSessionMaxDisplayEntries = _RsSESSIONSessionMaxDisplayEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 19),
    _RsSESSIONSessionMaxDisplayEntries_Type()
)
rsSESSIONSessionMaxDisplayEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionMaxDisplayEntries.setStatus("mandatory")
_RsSESSIONDisplayFiltersTable_Object = MibTable
rsSESSIONDisplayFiltersTable = _RsSESSIONDisplayFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20)
)
if mibBuilder.loadTexts:
    rsSESSIONDisplayFiltersTable.setStatus("mandatory")
_RsSESSIONDisplayFilterEntry_Object = MibTableRow
rsSESSIONDisplayFilterEntry = _RsSESSIONDisplayFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1)
)
rsSESSIONDisplayFilterEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONDisplayFilterName"),
)
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterEntry.setStatus("mandatory")


class _RsSESSIONDisplayFilterName_Type(DisplayString):
    """Custom type rsSESSIONDisplayFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONDisplayFilterName_Type.__name__ = "DisplayString"
_RsSESSIONDisplayFilterName_Object = MibTableColumn
rsSESSIONDisplayFilterName = _RsSESSIONDisplayFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 1),
    _RsSESSIONDisplayFilterName_Type()
)
rsSESSIONDisplayFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterName.setStatus("mandatory")
_RsSESSIONDisplayFilterSrcIP_Type = IpAddress
_RsSESSIONDisplayFilterSrcIP_Object = MibTableColumn
rsSESSIONDisplayFilterSrcIP = _RsSESSIONDisplayFilterSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 2),
    _RsSESSIONDisplayFilterSrcIP_Type()
)
rsSESSIONDisplayFilterSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterSrcIP.setStatus("mandatory")
_RsSESSIONDisplayFilterSrcIPMask_Type = IpAddress
_RsSESSIONDisplayFilterSrcIPMask_Object = MibTableColumn
rsSESSIONDisplayFilterSrcIPMask = _RsSESSIONDisplayFilterSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 3),
    _RsSESSIONDisplayFilterSrcIPMask_Type()
)
rsSESSIONDisplayFilterSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterSrcIPMask.setStatus("mandatory")
_RsSESSIONDisplayFilterDstIP_Type = IpAddress
_RsSESSIONDisplayFilterDstIP_Object = MibTableColumn
rsSESSIONDisplayFilterDstIP = _RsSESSIONDisplayFilterDstIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 4),
    _RsSESSIONDisplayFilterDstIP_Type()
)
rsSESSIONDisplayFilterDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterDstIP.setStatus("mandatory")
_RsSESSIONDisplayFilterDstIPMask_Type = IpAddress
_RsSESSIONDisplayFilterDstIPMask_Object = MibTableColumn
rsSESSIONDisplayFilterDstIPMask = _RsSESSIONDisplayFilterDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 5),
    _RsSESSIONDisplayFilterDstIPMask_Type()
)
rsSESSIONDisplayFilterDstIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterDstIPMask.setStatus("mandatory")


class _RsSESSIONDisplayFilterSrcPort_Type(Integer32):
    """Custom type rsSESSIONDisplayFilterSrcPort based on Integer32"""
    defaultValue = 0


_RsSESSIONDisplayFilterSrcPort_Type.__name__ = "Integer32"
_RsSESSIONDisplayFilterSrcPort_Object = MibTableColumn
rsSESSIONDisplayFilterSrcPort = _RsSESSIONDisplayFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 6),
    _RsSESSIONDisplayFilterSrcPort_Type()
)
rsSESSIONDisplayFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterSrcPort.setStatus("mandatory")


class _RsSESSIONDisplayFilterDstPort_Type(Integer32):
    """Custom type rsSESSIONDisplayFilterDstPort based on Integer32"""
    defaultValue = 0


_RsSESSIONDisplayFilterDstPort_Type.__name__ = "Integer32"
_RsSESSIONDisplayFilterDstPort_Object = MibTableColumn
rsSESSIONDisplayFilterDstPort = _RsSESSIONDisplayFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 7),
    _RsSESSIONDisplayFilterDstPort_Type()
)
rsSESSIONDisplayFilterDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterDstPort.setStatus("mandatory")


class _RsSESSIONDisplayFilterPhysicalPort_Type(Integer32):
    """Custom type rsSESSIONDisplayFilterPhysicalPort based on Integer32"""
    defaultValue = 65535


_RsSESSIONDisplayFilterPhysicalPort_Type.__name__ = "Integer32"
_RsSESSIONDisplayFilterPhysicalPort_Object = MibTableColumn
rsSESSIONDisplayFilterPhysicalPort = _RsSESSIONDisplayFilterPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 8),
    _RsSESSIONDisplayFilterPhysicalPort_Type()
)
rsSESSIONDisplayFilterPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterPhysicalPort.setStatus("mandatory")
_RsSESSIONDisplayFilterStatus_Type = RowStatus
_RsSESSIONDisplayFilterStatus_Object = MibTableColumn
rsSESSIONDisplayFilterStatus = _RsSESSIONDisplayFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 20, 1, 9),
    _RsSESSIONDisplayFilterStatus_Type()
)
rsSESSIONDisplayFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONDisplayFilterStatus.setStatus("mandatory")
_RsSESSIONSessionTableEntriesTable_Object = MibTable
rsSESSIONSessionTableEntriesTable = _RsSESSIONSessionTableEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21)
)
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntriesTable.setStatus("obsolete")
_RsSESSIONSessionTableEntry_Object = MibTableRow
rsSESSIONSessionTableEntry = _RsSESSIONSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1)
)
rsSESSIONSessionTableEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSessionTableEntryIndex"),
)
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntry.setStatus("obsolete")
_RsSESSIONSessionTableEntryIndex_Type = Integer32
_RsSESSIONSessionTableEntryIndex_Object = MibTableColumn
rsSESSIONSessionTableEntryIndex = _RsSESSIONSessionTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 1),
    _RsSESSIONSessionTableEntryIndex_Type()
)
rsSESSIONSessionTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryIndex.setStatus("mandatory")
_RsSESSIONSessionTableEntrySrcIP_Type = IpAddress
_RsSESSIONSessionTableEntrySrcIP_Object = MibTableColumn
rsSESSIONSessionTableEntrySrcIP = _RsSESSIONSessionTableEntrySrcIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 2),
    _RsSESSIONSessionTableEntrySrcIP_Type()
)
rsSESSIONSessionTableEntrySrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntrySrcIP.setStatus("mandatory")
_RsSESSIONSessionTableEntryDstIP_Type = IpAddress
_RsSESSIONSessionTableEntryDstIP_Object = MibTableColumn
rsSESSIONSessionTableEntryDstIP = _RsSESSIONSessionTableEntryDstIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 3),
    _RsSESSIONSessionTableEntryDstIP_Type()
)
rsSESSIONSessionTableEntryDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryDstIP.setStatus("mandatory")
_RsSESSIONSessionTableEntrySrcPort_Type = Integer32
_RsSESSIONSessionTableEntrySrcPort_Object = MibTableColumn
rsSESSIONSessionTableEntrySrcPort = _RsSESSIONSessionTableEntrySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 4),
    _RsSESSIONSessionTableEntrySrcPort_Type()
)
rsSESSIONSessionTableEntrySrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntrySrcPort.setStatus("mandatory")
_RsSESSIONSessionTableEntryDstPort_Type = Integer32
_RsSESSIONSessionTableEntryDstPort_Object = MibTableColumn
rsSESSIONSessionTableEntryDstPort = _RsSESSIONSessionTableEntryDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 5),
    _RsSESSIONSessionTableEntryDstPort_Type()
)
rsSESSIONSessionTableEntryDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryDstPort.setStatus("mandatory")
_RsSESSIONSessionTableEntryPhysicalPort_Type = Integer32
_RsSESSIONSessionTableEntryPhysicalPort_Object = MibTableColumn
rsSESSIONSessionTableEntryPhysicalPort = _RsSESSIONSessionTableEntryPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 6),
    _RsSESSIONSessionTableEntryPhysicalPort_Type()
)
rsSESSIONSessionTableEntryPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryPhysicalPort.setStatus("mandatory")
_RsSESSIONSessionTableEntryLifetime_Type = Integer32
_RsSESSIONSessionTableEntryLifetime_Object = MibTableColumn
rsSESSIONSessionTableEntryLifetime = _RsSESSIONSessionTableEntryLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 7),
    _RsSESSIONSessionTableEntryLifetime_Type()
)
rsSESSIONSessionTableEntryLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryLifetime.setStatus("mandatory")


class _RsSESSIONSessionTableEntryAgingType_Type(Integer32):
    """Custom type rsSESSIONSessionTableEntryAgingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("app", 2),
          ("syn", 3),
          ("end", 4),
          ("unknown", 5),
          ("delete", 6),
          ("short", 7))
    )


_RsSESSIONSessionTableEntryAgingType_Type.__name__ = "Integer32"
_RsSESSIONSessionTableEntryAgingType_Object = MibTableColumn
rsSESSIONSessionTableEntryAgingType = _RsSESSIONSessionTableEntryAgingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 8),
    _RsSESSIONSessionTableEntryAgingType_Type()
)
rsSESSIONSessionTableEntryAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryAgingType.setStatus("mandatory")


class _RsSESSIONSessionTableEntrySYNData_Type(DisplayString):
    """Custom type rsSESSIONSessionTableEntrySYNData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONSessionTableEntrySYNData_Type.__name__ = "DisplayString"
_RsSESSIONSessionTableEntrySYNData_Object = MibTableColumn
rsSESSIONSessionTableEntrySYNData = _RsSESSIONSessionTableEntrySYNData_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 9),
    _RsSESSIONSessionTableEntrySYNData_Type()
)
rsSESSIONSessionTableEntrySYNData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntrySYNData.setStatus("mandatory")
_RsSESSIONSessionTableEntryRplyPhysicalPort_Type = Integer32
_RsSESSIONSessionTableEntryRplyPhysicalPort_Object = MibTableColumn
rsSESSIONSessionTableEntryRplyPhysicalPort = _RsSESSIONSessionTableEntryRplyPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 10),
    _RsSESSIONSessionTableEntryRplyPhysicalPort_Type()
)
rsSESSIONSessionTableEntryRplyPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryRplyPhysicalPort.setStatus("mandatory")


class _RsSESSIONSessionTableEntryIPProtocol_Type(Integer32):
    """Custom type rsSESSIONSessionTableEntryIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("gre", 5),
          ("icmpv6", 6))
    )


_RsSESSIONSessionTableEntryIPProtocol_Type.__name__ = "Integer32"
_RsSESSIONSessionTableEntryIPProtocol_Object = MibTableColumn
rsSESSIONSessionTableEntryIPProtocol = _RsSESSIONSessionTableEntryIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 21, 1, 11),
    _RsSESSIONSessionTableEntryIPProtocol_Type()
)
rsSESSIONSessionTableEntryIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryIPProtocol.setStatus("mandatory")
_RsSESSIONSessionTableEntryDummy_Type = Integer32
_RsSESSIONSessionTableEntryDummy_Object = MibScalar
rsSESSIONSessionTableEntryDummy = _RsSESSIONSessionTableEntryDummy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 22),
    _RsSESSIONSessionTableEntryDummy_Type()
)
rsSESSIONSessionTableEntryDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSessionTableEntryDummy.setStatus("mandatory")


class _RsSESSIONAckReflectionProtectionMode_Type(Integer32):
    """Custom type rsSESSIONAckReflectionProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("reportOnly", 2),
          ("disable", 3))
    )


_RsSESSIONAckReflectionProtectionMode_Type.__name__ = "Integer32"
_RsSESSIONAckReflectionProtectionMode_Object = MibScalar
rsSESSIONAckReflectionProtectionMode = _RsSESSIONAckReflectionProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 23),
    _RsSESSIONAckReflectionProtectionMode_Type()
)
rsSESSIONAckReflectionProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONAckReflectionProtectionMode.setStatus("mandatory")
_RsSESSIONAckReflectionSamplingPerSecond_Type = Integer32
_RsSESSIONAckReflectionSamplingPerSecond_Object = MibScalar
rsSESSIONAckReflectionSamplingPerSecond = _RsSESSIONAckReflectionSamplingPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 24),
    _RsSESSIONAckReflectionSamplingPerSecond_Type()
)
rsSESSIONAckReflectionSamplingPerSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONAckReflectionSamplingPerSecond.setStatus("mandatory")
_RsSESSIONAckReflectionDropThreshold_Type = Integer32
_RsSESSIONAckReflectionDropThreshold_Object = MibScalar
rsSESSIONAckReflectionDropThreshold = _RsSESSIONAckReflectionDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 25),
    _RsSESSIONAckReflectionDropThreshold_Type()
)
rsSESSIONAckReflectionDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONAckReflectionDropThreshold.setStatus("mandatory")
_RsSESSIONSynProtectionMaxTrapsPerTimeUnit_Type = Integer32
_RsSESSIONSynProtectionMaxTrapsPerTimeUnit_Object = MibScalar
rsSESSIONSynProtectionMaxTrapsPerTimeUnit = _RsSESSIONSynProtectionMaxTrapsPerTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 26),
    _RsSESSIONSynProtectionMaxTrapsPerTimeUnit_Type()
)
rsSESSIONSynProtectionMaxTrapsPerTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionMaxTrapsPerTimeUnit.setStatus("mandatory")
_RsSESSIONSynProtectionTrapsTimeUnit_Type = Integer32
_RsSESSIONSynProtectionTrapsTimeUnit_Object = MibScalar
rsSESSIONSynProtectionTrapsTimeUnit = _RsSESSIONSynProtectionTrapsTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 27),
    _RsSESSIONSynProtectionTrapsTimeUnit_Type()
)
rsSESSIONSynProtectionTrapsTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionTrapsTimeUnit.setStatus("mandatory")
_RsSESSIONNewSynTriggerTable_Object = MibTable
rsSESSIONNewSynTriggerTable = _RsSESSIONNewSynTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28)
)
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerTable.setStatus("mandatory")
_RsSESSIONNewSynTriggerEntry_Object = MibTableRow
rsSESSIONNewSynTriggerEntry = _RsSESSIONNewSynTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1)
)
rsSESSIONNewSynTriggerEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONNewSynTriggerType"),
    (0, "SESSION-MIB", "rsSESSIONNewSynTriggerIP"),
    (0, "SESSION-MIB", "rsSESSIONNewSynTriggerPort"),
    (0, "SESSION-MIB", "rsSESSIONNewSynTriggerRxport"),
)
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerEntry.setStatus("mandatory")


class _RsSESSIONNewSynTriggerType_Type(Integer32):
    """Custom type rsSESSIONNewSynTriggerType based on Integer32"""
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
        *(("synProtectionTrigger", 1),
          ("synProtectionEnable", 2),
          ("synProtectionTotal", 3),
          ("ackReflection", 4))
    )


_RsSESSIONNewSynTriggerType_Type.__name__ = "Integer32"
_RsSESSIONNewSynTriggerType_Object = MibTableColumn
rsSESSIONNewSynTriggerType = _RsSESSIONNewSynTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 1),
    _RsSESSIONNewSynTriggerType_Type()
)
rsSESSIONNewSynTriggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerType.setStatus("mandatory")
_RsSESSIONNewSynTriggerIP_Type = IpAddress
_RsSESSIONNewSynTriggerIP_Object = MibTableColumn
rsSESSIONNewSynTriggerIP = _RsSESSIONNewSynTriggerIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 2),
    _RsSESSIONNewSynTriggerIP_Type()
)
rsSESSIONNewSynTriggerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerIP.setStatus("mandatory")
_RsSESSIONNewSynTriggerPort_Type = Integer32
_RsSESSIONNewSynTriggerPort_Object = MibTableColumn
rsSESSIONNewSynTriggerPort = _RsSESSIONNewSynTriggerPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 3),
    _RsSESSIONNewSynTriggerPort_Type()
)
rsSESSIONNewSynTriggerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerPort.setStatus("mandatory")
_RsSESSIONNewSynTriggerRxport_Type = Integer32
_RsSESSIONNewSynTriggerRxport_Object = MibTableColumn
rsSESSIONNewSynTriggerRxport = _RsSESSIONNewSynTriggerRxport_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 4),
    _RsSESSIONNewSynTriggerRxport_Type()
)
rsSESSIONNewSynTriggerRxport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerRxport.setStatus("mandatory")
_RsSESSIONNewSynTriggerTime_Type = Integer32
_RsSESSIONNewSynTriggerTime_Object = MibTableColumn
rsSESSIONNewSynTriggerTime = _RsSESSIONNewSynTriggerTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 5),
    _RsSESSIONNewSynTriggerTime_Type()
)
rsSESSIONNewSynTriggerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerTime.setStatus("mandatory")
_RsSESSIONNewSynTriggerLastSecSYN_Type = Integer32
_RsSESSIONNewSynTriggerLastSecSYN_Object = MibTableColumn
rsSESSIONNewSynTriggerLastSecSYN = _RsSESSIONNewSynTriggerLastSecSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 6),
    _RsSESSIONNewSynTriggerLastSecSYN_Type()
)
rsSESSIONNewSynTriggerLastSecSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerLastSecSYN.setStatus("mandatory")
_RsSESSIONNewSynTriggerLastSecRqst_Type = Integer32
_RsSESSIONNewSynTriggerLastSecRqst_Object = MibTableColumn
rsSESSIONNewSynTriggerLastSecRqst = _RsSESSIONNewSynTriggerLastSecRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 7),
    _RsSESSIONNewSynTriggerLastSecRqst_Type()
)
rsSESSIONNewSynTriggerLastSecRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerLastSecRqst.setStatus("mandatory")
_RsSESSIONNewSynTriggerAvrgSYN_Type = Integer32
_RsSESSIONNewSynTriggerAvrgSYN_Object = MibTableColumn
rsSESSIONNewSynTriggerAvrgSYN = _RsSESSIONNewSynTriggerAvrgSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 8),
    _RsSESSIONNewSynTriggerAvrgSYN_Type()
)
rsSESSIONNewSynTriggerAvrgSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerAvrgSYN.setStatus("mandatory")
_RsSESSIONNewSynTriggerAvrgRqst_Type = Integer32
_RsSESSIONNewSynTriggerAvrgRqst_Object = MibTableColumn
rsSESSIONNewSynTriggerAvrgRqst = _RsSESSIONNewSynTriggerAvrgRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 9),
    _RsSESSIONNewSynTriggerAvrgRqst_Type()
)
rsSESSIONNewSynTriggerAvrgRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerAvrgRqst.setStatus("mandatory")
_RsSESSIONNewSynTriggerTotalSYN_Type = DisplayString
_RsSESSIONNewSynTriggerTotalSYN_Object = MibTableColumn
rsSESSIONNewSynTriggerTotalSYN = _RsSESSIONNewSynTriggerTotalSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 10),
    _RsSESSIONNewSynTriggerTotalSYN_Type()
)
rsSESSIONNewSynTriggerTotalSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerTotalSYN.setStatus("mandatory")
_RsSESSIONNewSynTriggerTotalDropped_Type = DisplayString
_RsSESSIONNewSynTriggerTotalDropped_Object = MibTableColumn
rsSESSIONNewSynTriggerTotalDropped = _RsSESSIONNewSynTriggerTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 28, 1, 11),
    _RsSESSIONNewSynTriggerTotalDropped_Type()
)
rsSESSIONNewSynTriggerTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONNewSynTriggerTotalDropped.setStatus("mandatory")


class _RsSESSIONSynStatsMaxDestPerPolicy_Type(Integer32):
    """Custom type rsSESSIONSynStatsMaxDestPerPolicy based on Integer32"""
    defaultValue = 5


_RsSESSIONSynStatsMaxDestPerPolicy_Type.__name__ = "Integer32"
_RsSESSIONSynStatsMaxDestPerPolicy_Object = MibScalar
rsSESSIONSynStatsMaxDestPerPolicy = _RsSESSIONSynStatsMaxDestPerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 29),
    _RsSESSIONSynStatsMaxDestPerPolicy_Type()
)
rsSESSIONSynStatsMaxDestPerPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynStatsMaxDestPerPolicy.setStatus("mandatory")


class _RsSESSIONSynStatsTimePeriod_Type(Integer32):
    """Custom type rsSESSIONSynStatsTimePeriod based on Integer32"""
    defaultValue = 60


_RsSESSIONSynStatsTimePeriod_Type.__name__ = "Integer32"
_RsSESSIONSynStatsTimePeriod_Object = MibScalar
rsSESSIONSynStatsTimePeriod = _RsSESSIONSynStatsTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 30),
    _RsSESSIONSynStatsTimePeriod_Type()
)
rsSESSIONSynStatsTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynStatsTimePeriod.setStatus("mandatory")
_RsSESSIONSynStatsDisplayPolicyName_Type = DisplayString
_RsSESSIONSynStatsDisplayPolicyName_Object = MibScalar
rsSESSIONSynStatsDisplayPolicyName = _RsSESSIONSynStatsDisplayPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 31),
    _RsSESSIONSynStatsDisplayPolicyName_Type()
)
rsSESSIONSynStatsDisplayPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynStatsDisplayPolicyName.setStatus("mandatory")
_RsSESSIONSynStatisticsTable_Object = MibTable
rsSESSIONSynStatisticsTable = _RsSESSIONSynStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32)
)
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsTable.setStatus("mandatory")
_RsSESSIONSynStatisticsEntry_Object = MibTableRow
rsSESSIONSynStatisticsEntry = _RsSESSIONSynStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1)
)
rsSESSIONSynStatisticsEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSynStatisticsPolicy"),
    (0, "SESSION-MIB", "rsSESSIONSynStatisticsIP"),
    (0, "SESSION-MIB", "rsSESSIONSynStatisticsPort"),
    (0, "SESSION-MIB", "rsSESSIONSynStatisticsRxPort"),
)
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsEntry.setStatus("mandatory")
_RsSESSIONSynStatisticsPolicy_Type = DisplayString
_RsSESSIONSynStatisticsPolicy_Object = MibTableColumn
rsSESSIONSynStatisticsPolicy = _RsSESSIONSynStatisticsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 1),
    _RsSESSIONSynStatisticsPolicy_Type()
)
rsSESSIONSynStatisticsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsPolicy.setStatus("mandatory")
_RsSESSIONSynStatisticsIP_Type = IpAddress
_RsSESSIONSynStatisticsIP_Object = MibTableColumn
rsSESSIONSynStatisticsIP = _RsSESSIONSynStatisticsIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 2),
    _RsSESSIONSynStatisticsIP_Type()
)
rsSESSIONSynStatisticsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsIP.setStatus("mandatory")
_RsSESSIONSynStatisticsPort_Type = Integer32
_RsSESSIONSynStatisticsPort_Object = MibTableColumn
rsSESSIONSynStatisticsPort = _RsSESSIONSynStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 3),
    _RsSESSIONSynStatisticsPort_Type()
)
rsSESSIONSynStatisticsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsPort.setStatus("mandatory")
_RsSESSIONSynStatisticsRxPort_Type = Integer32
_RsSESSIONSynStatisticsRxPort_Object = MibTableColumn
rsSESSIONSynStatisticsRxPort = _RsSESSIONSynStatisticsRxPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 4),
    _RsSESSIONSynStatisticsRxPort_Type()
)
rsSESSIONSynStatisticsRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsRxPort.setStatus("mandatory")


class _RsSESSIONSynStatisticsCurrentAttackStatus_Type(Integer32):
    """Custom type rsSESSIONSynStatisticsCurrentAttackStatus based on Integer32"""
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
        *(("protectedUnderAttack", 1),
          ("protectedNoAttack", 2),
          ("monitorNoAttack", 3),
          ("unprotected", 4))
    )


_RsSESSIONSynStatisticsCurrentAttackStatus_Type.__name__ = "Integer32"
_RsSESSIONSynStatisticsCurrentAttackStatus_Object = MibTableColumn
rsSESSIONSynStatisticsCurrentAttackStatus = _RsSESSIONSynStatisticsCurrentAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 5),
    _RsSESSIONSynStatisticsCurrentAttackStatus_Type()
)
rsSESSIONSynStatisticsCurrentAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsCurrentAttackStatus.setStatus("mandatory")
_RsSESSIONSynStatisticsLastSecSynCount_Type = Integer32
_RsSESSIONSynStatisticsLastSecSynCount_Object = MibTableColumn
rsSESSIONSynStatisticsLastSecSynCount = _RsSESSIONSynStatisticsLastSecSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 6),
    _RsSESSIONSynStatisticsLastSecSynCount_Type()
)
rsSESSIONSynStatisticsLastSecSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsLastSecSynCount.setStatus("mandatory")
_RsSESSIONSynStatisticsLastSecGoodCount_Type = Integer32
_RsSESSIONSynStatisticsLastSecGoodCount_Object = MibTableColumn
rsSESSIONSynStatisticsLastSecGoodCount = _RsSESSIONSynStatisticsLastSecGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 7),
    _RsSESSIONSynStatisticsLastSecGoodCount_Type()
)
rsSESSIONSynStatisticsLastSecGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsLastSecGoodCount.setStatus("mandatory")
_RsSESSIONSynStatisticsAverageSynCount_Type = Integer32
_RsSESSIONSynStatisticsAverageSynCount_Object = MibTableColumn
rsSESSIONSynStatisticsAverageSynCount = _RsSESSIONSynStatisticsAverageSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 8),
    _RsSESSIONSynStatisticsAverageSynCount_Type()
)
rsSESSIONSynStatisticsAverageSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsAverageSynCount.setStatus("mandatory")
_RsSESSIONSynStatisticsAverageGoodCount_Type = Integer32
_RsSESSIONSynStatisticsAverageGoodCount_Object = MibTableColumn
rsSESSIONSynStatisticsAverageGoodCount = _RsSESSIONSynStatisticsAverageGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 9),
    _RsSESSIONSynStatisticsAverageGoodCount_Type()
)
rsSESSIONSynStatisticsAverageGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsAverageGoodCount.setStatus("mandatory")
_RsSESSIONSynStatisticsPeakSynCount_Type = Integer32
_RsSESSIONSynStatisticsPeakSynCount_Object = MibTableColumn
rsSESSIONSynStatisticsPeakSynCount = _RsSESSIONSynStatisticsPeakSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 10),
    _RsSESSIONSynStatisticsPeakSynCount_Type()
)
rsSESSIONSynStatisticsPeakSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsPeakSynCount.setStatus("mandatory")
_RsSESSIONSynStatisticsPeakGoodCount_Type = Integer32
_RsSESSIONSynStatisticsPeakGoodCount_Object = MibTableColumn
rsSESSIONSynStatisticsPeakGoodCount = _RsSESSIONSynStatisticsPeakGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 11),
    _RsSESSIONSynStatisticsPeakGoodCount_Type()
)
rsSESSIONSynStatisticsPeakGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsPeakGoodCount.setStatus("mandatory")
_RsSESSIONSynStatisticsActivityTime_Type = Integer32
_RsSESSIONSynStatisticsActivityTime_Object = MibTableColumn
rsSESSIONSynStatisticsActivityTime = _RsSESSIONSynStatisticsActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 12),
    _RsSESSIONSynStatisticsActivityTime_Type()
)
rsSESSIONSynStatisticsActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsActivityTime.setStatus("mandatory")
_RsSESSIONSynStatisticsLastAttackStartTime_Type = DisplayString
_RsSESSIONSynStatisticsLastAttackStartTime_Object = MibTableColumn
rsSESSIONSynStatisticsLastAttackStartTime = _RsSESSIONSynStatisticsLastAttackStartTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 13),
    _RsSESSIONSynStatisticsLastAttackStartTime_Type()
)
rsSESSIONSynStatisticsLastAttackStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsLastAttackStartTime.setStatus("mandatory")
_RsSESSIONSynStatisticsLastAttackTermTime_Type = DisplayString
_RsSESSIONSynStatisticsLastAttackTermTime_Object = MibTableColumn
rsSESSIONSynStatisticsLastAttackTermTime = _RsSESSIONSynStatisticsLastAttackTermTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 32, 1, 14),
    _RsSESSIONSynStatisticsLastAttackTermTime_Type()
)
rsSESSIONSynStatisticsLastAttackTermTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsLastAttackTermTime.setStatus("mandatory")
_RsSESSIONSynStatisticsTableDummy_Type = Integer32
_RsSESSIONSynStatisticsTableDummy_Object = MibScalar
rsSESSIONSynStatisticsTableDummy = _RsSESSIONSynStatisticsTableDummy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 33),
    _RsSESSIONSynStatisticsTableDummy_Type()
)
rsSESSIONSynStatisticsTableDummy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsTableDummy.setStatus("mandatory")


class _RsSESSIONSynStatisticsReset_Type(Integer32):
    """Custom type rsSESSIONSynStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStatistics", 1)
    )


_RsSESSIONSynStatisticsReset_Type.__name__ = "Integer32"
_RsSESSIONSynStatisticsReset_Object = MibScalar
rsSESSIONSynStatisticsReset = _RsSESSIONSynStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 34),
    _RsSESSIONSynStatisticsReset_Type()
)
rsSESSIONSynStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSynStatisticsReset.setStatus("mandatory")


class _RsSESSIONH225AgingTime_Type(Integer32):
    """Custom type rsSESSIONH225AgingTime based on Integer32"""
    defaultValue = 20000


_RsSESSIONH225AgingTime_Type.__name__ = "Integer32"
_RsSESSIONH225AgingTime_Object = MibScalar
rsSESSIONH225AgingTime = _RsSESSIONH225AgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 35),
    _RsSESSIONH225AgingTime_Type()
)
rsSESSIONH225AgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONH225AgingTime.setStatus("mandatory")
_RsSESSIONNoAgingMode_Type = FeatureStatus
_RsSESSIONNoAgingMode_Object = MibScalar
rsSESSIONNoAgingMode = _RsSESSIONNoAgingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 36),
    _RsSESSIONNoAgingMode_Type()
)
rsSESSIONNoAgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONNoAgingMode.setStatus("mandatory")
_RsSESSIONProtectionMode_Type = FeatureStatus
_RsSESSIONProtectionMode_Object = MibScalar
rsSESSIONProtectionMode = _RsSESSIONProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 37),
    _RsSESSIONProtectionMode_Type()
)
rsSESSIONProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONProtectionMode.setStatus("mandatory")


class _RsSESSIONProtectionShortLifetime_Type(Integer32):
    """Custom type rsSESSIONProtectionShortLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsSESSIONProtectionShortLifetime_Type.__name__ = "Integer32"
_RsSESSIONProtectionShortLifetime_Object = MibScalar
rsSESSIONProtectionShortLifetime = _RsSESSIONProtectionShortLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 38),
    _RsSESSIONProtectionShortLifetime_Type()
)
rsSESSIONProtectionShortLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONProtectionShortLifetime.setStatus("mandatory")
_RsSESSIONProtectionMaxSessions_Type = Integer32
_RsSESSIONProtectionMaxSessions_Object = MibScalar
rsSESSIONProtectionMaxSessions = _RsSESSIONProtectionMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 39),
    _RsSESSIONProtectionMaxSessions_Type()
)
rsSESSIONProtectionMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONProtectionMaxSessions.setStatus("mandatory")
_RsSESSIONFiltersTable_Object = MibTable
rsSESSIONFiltersTable = _RsSESSIONFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40)
)
if mibBuilder.loadTexts:
    rsSESSIONFiltersTable.setStatus("mandatory")
_RsSESSIONFilterEntry_Object = MibTableRow
rsSESSIONFilterEntry = _RsSESSIONFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1)
)
rsSESSIONFilterEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONFilterName"),
)
if mibBuilder.loadTexts:
    rsSESSIONFilterEntry.setStatus("mandatory")


class _RsSESSIONFilterName_Type(DisplayString):
    """Custom type rsSESSIONFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONFilterName_Type.__name__ = "DisplayString"
_RsSESSIONFilterName_Object = MibTableColumn
rsSESSIONFilterName = _RsSESSIONFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 1),
    _RsSESSIONFilterName_Type()
)
rsSESSIONFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterName.setStatus("mandatory")
_RsSESSIONFilterSrcIP_Type = Ipv6Address
_RsSESSIONFilterSrcIP_Object = MibTableColumn
rsSESSIONFilterSrcIP = _RsSESSIONFilterSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 2),
    _RsSESSIONFilterSrcIP_Type()
)
rsSESSIONFilterSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterSrcIP.setStatus("mandatory")
_RsSESSIONFilterSrcIPMask_Type = Ipv6Address
_RsSESSIONFilterSrcIPMask_Object = MibTableColumn
rsSESSIONFilterSrcIPMask = _RsSESSIONFilterSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 3),
    _RsSESSIONFilterSrcIPMask_Type()
)
rsSESSIONFilterSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterSrcIPMask.setStatus("mandatory")
_RsSESSIONFilterDstIP_Type = Ipv6Address
_RsSESSIONFilterDstIP_Object = MibTableColumn
rsSESSIONFilterDstIP = _RsSESSIONFilterDstIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 4),
    _RsSESSIONFilterDstIP_Type()
)
rsSESSIONFilterDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterDstIP.setStatus("mandatory")
_RsSESSIONFilterDstIPMask_Type = Ipv6Address
_RsSESSIONFilterDstIPMask_Object = MibTableColumn
rsSESSIONFilterDstIPMask = _RsSESSIONFilterDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 5),
    _RsSESSIONFilterDstIPMask_Type()
)
rsSESSIONFilterDstIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterDstIPMask.setStatus("mandatory")


class _RsSESSIONFilterSrcPort_Type(Integer32):
    """Custom type rsSESSIONFilterSrcPort based on Integer32"""
    defaultValue = 0


_RsSESSIONFilterSrcPort_Type.__name__ = "Integer32"
_RsSESSIONFilterSrcPort_Object = MibTableColumn
rsSESSIONFilterSrcPort = _RsSESSIONFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 6),
    _RsSESSIONFilterSrcPort_Type()
)
rsSESSIONFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterSrcPort.setStatus("mandatory")


class _RsSESSIONFilterDstPort_Type(Integer32):
    """Custom type rsSESSIONFilterDstPort based on Integer32"""
    defaultValue = 0


_RsSESSIONFilterDstPort_Type.__name__ = "Integer32"
_RsSESSIONFilterDstPort_Object = MibTableColumn
rsSESSIONFilterDstPort = _RsSESSIONFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 7),
    _RsSESSIONFilterDstPort_Type()
)
rsSESSIONFilterDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterDstPort.setStatus("mandatory")


class _RsSESSIONFilterPhysicalPort_Type(Integer32):
    """Custom type rsSESSIONFilterPhysicalPort based on Integer32"""
    defaultValue = 65535


_RsSESSIONFilterPhysicalPort_Type.__name__ = "Integer32"
_RsSESSIONFilterPhysicalPort_Object = MibTableColumn
rsSESSIONFilterPhysicalPort = _RsSESSIONFilterPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 8),
    _RsSESSIONFilterPhysicalPort_Type()
)
rsSESSIONFilterPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterPhysicalPort.setStatus("mandatory")
_RsSESSIONFilterStatus_Type = RowStatus
_RsSESSIONFilterStatus_Object = MibTableColumn
rsSESSIONFilterStatus = _RsSESSIONFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 40, 1, 9),
    _RsSESSIONFilterStatus_Type()
)
rsSESSIONFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONFilterStatus.setStatus("mandatory")
_RsSESSIONTableEntriesTable_Object = MibTable
rsSESSIONTableEntriesTable = _RsSESSIONTableEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41)
)
if mibBuilder.loadTexts:
    rsSESSIONTableEntriesTable.setStatus("mandatory")
_RsSESSIONTableEntry_Object = MibTableRow
rsSESSIONTableEntry = _RsSESSIONTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1)
)
rsSESSIONTableEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONTableEntryCoreIndex"),
    (0, "SESSION-MIB", "rsSESSIONTableEntryIndex"),
)
if mibBuilder.loadTexts:
    rsSESSIONTableEntry.setStatus("mandatory")
_RsSESSIONTableEntryIndex_Type = Integer32
_RsSESSIONTableEntryIndex_Object = MibTableColumn
rsSESSIONTableEntryIndex = _RsSESSIONTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 1),
    _RsSESSIONTableEntryIndex_Type()
)
rsSESSIONTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryIndex.setStatus("mandatory")
_RsSESSIONTableEntrySrcIP_Type = Ipv6Address
_RsSESSIONTableEntrySrcIP_Object = MibTableColumn
rsSESSIONTableEntrySrcIP = _RsSESSIONTableEntrySrcIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 2),
    _RsSESSIONTableEntrySrcIP_Type()
)
rsSESSIONTableEntrySrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntrySrcIP.setStatus("mandatory")
_RsSESSIONTableEntryDstIP_Type = Ipv6Address
_RsSESSIONTableEntryDstIP_Object = MibTableColumn
rsSESSIONTableEntryDstIP = _RsSESSIONTableEntryDstIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 3),
    _RsSESSIONTableEntryDstIP_Type()
)
rsSESSIONTableEntryDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryDstIP.setStatus("mandatory")
_RsSESSIONTableEntrySrcPort_Type = Integer32
_RsSESSIONTableEntrySrcPort_Object = MibTableColumn
rsSESSIONTableEntrySrcPort = _RsSESSIONTableEntrySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 4),
    _RsSESSIONTableEntrySrcPort_Type()
)
rsSESSIONTableEntrySrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntrySrcPort.setStatus("mandatory")
_RsSESSIONTableEntryDstPort_Type = Integer32
_RsSESSIONTableEntryDstPort_Object = MibTableColumn
rsSESSIONTableEntryDstPort = _RsSESSIONTableEntryDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 5),
    _RsSESSIONTableEntryDstPort_Type()
)
rsSESSIONTableEntryDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryDstPort.setStatus("mandatory")
_RsSESSIONTableEntryPhysicalPort_Type = Integer32
_RsSESSIONTableEntryPhysicalPort_Object = MibTableColumn
rsSESSIONTableEntryPhysicalPort = _RsSESSIONTableEntryPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 6),
    _RsSESSIONTableEntryPhysicalPort_Type()
)
rsSESSIONTableEntryPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryPhysicalPort.setStatus("mandatory")
_RsSESSIONTableEntryLifetime_Type = Integer32
_RsSESSIONTableEntryLifetime_Object = MibTableColumn
rsSESSIONTableEntryLifetime = _RsSESSIONTableEntryLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 7),
    _RsSESSIONTableEntryLifetime_Type()
)
rsSESSIONTableEntryLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryLifetime.setStatus("mandatory")


class _RsSESSIONTableEntryAgingType_Type(Integer32):
    """Custom type rsSESSIONTableEntryAgingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("app", 2),
          ("syn", 3),
          ("end", 4),
          ("unknown", 5),
          ("delete", 6),
          ("short", 7))
    )


_RsSESSIONTableEntryAgingType_Type.__name__ = "Integer32"
_RsSESSIONTableEntryAgingType_Object = MibTableColumn
rsSESSIONTableEntryAgingType = _RsSESSIONTableEntryAgingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 8),
    _RsSESSIONTableEntryAgingType_Type()
)
rsSESSIONTableEntryAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryAgingType.setStatus("mandatory")


class _RsSESSIONTableEntrySYNData_Type(DisplayString):
    """Custom type rsSESSIONTableEntrySYNData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsSESSIONTableEntrySYNData_Type.__name__ = "DisplayString"
_RsSESSIONTableEntrySYNData_Object = MibTableColumn
rsSESSIONTableEntrySYNData = _RsSESSIONTableEntrySYNData_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 9),
    _RsSESSIONTableEntrySYNData_Type()
)
rsSESSIONTableEntrySYNData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntrySYNData.setStatus("mandatory")
_RsSESSIONTableEntryRplyPhysicalPort_Type = Integer32
_RsSESSIONTableEntryRplyPhysicalPort_Object = MibTableColumn
rsSESSIONTableEntryRplyPhysicalPort = _RsSESSIONTableEntryRplyPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 10),
    _RsSESSIONTableEntryRplyPhysicalPort_Type()
)
rsSESSIONTableEntryRplyPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryRplyPhysicalPort.setStatus("mandatory")


class _RsSESSIONTableEntryIPProtocol_Type(Integer32):
    """Custom type rsSESSIONTableEntryIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("gre", 5),
          ("icmpv6", 6))
    )


_RsSESSIONTableEntryIPProtocol_Type.__name__ = "Integer32"
_RsSESSIONTableEntryIPProtocol_Object = MibTableColumn
rsSESSIONTableEntryIPProtocol = _RsSESSIONTableEntryIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 11),
    _RsSESSIONTableEntryIPProtocol_Type()
)
rsSESSIONTableEntryIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryIPProtocol.setStatus("mandatory")


class _RsSESSIONTableEntryPolicyName_Type(DisplayString):
    """Custom type rsSESSIONTableEntryPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsSESSIONTableEntryPolicyName_Type.__name__ = "DisplayString"
_RsSESSIONTableEntryPolicyName_Object = MibTableColumn
rsSESSIONTableEntryPolicyName = _RsSESSIONTableEntryPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 12),
    _RsSESSIONTableEntryPolicyName_Type()
)
rsSESSIONTableEntryPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryPolicyName.setStatus("mandatory")
_RsSESSIONTableEntryCoreIndex_Type = Integer32
_RsSESSIONTableEntryCoreIndex_Object = MibTableColumn
rsSESSIONTableEntryCoreIndex = _RsSESSIONTableEntryCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 41, 1, 13),
    _RsSESSIONTableEntryCoreIndex_Type()
)
rsSESSIONTableEntryCoreIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableEntryCoreIndex.setStatus("mandatory")
_RsSESSIONSynActivationTable_Object = MibTable
rsSESSIONSynActivationTable = _RsSESSIONSynActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42)
)
if mibBuilder.loadTexts:
    rsSESSIONSynActivationTable.setStatus("mandatory")
_RsSESSIONSynActivationEntry_Object = MibTableRow
rsSESSIONSynActivationEntry = _RsSESSIONSynActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1)
)
rsSESSIONSynActivationEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSynActivationType"),
    (0, "SESSION-MIB", "rsSESSIONSynActivationIP"),
    (0, "SESSION-MIB", "rsSESSIONSynActivationPort"),
    (0, "SESSION-MIB", "rsSESSIONSynActivationRxport"),
)
if mibBuilder.loadTexts:
    rsSESSIONSynActivationEntry.setStatus("mandatory")


class _RsSESSIONSynActivationType_Type(Integer32):
    """Custom type rsSESSIONSynActivationType based on Integer32"""
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
        *(("synProtectionTrigger", 1),
          ("synProtectionEnable", 2),
          ("synProtectionTotal", 3),
          ("ackReflection", 4))
    )


_RsSESSIONSynActivationType_Type.__name__ = "Integer32"
_RsSESSIONSynActivationType_Object = MibTableColumn
rsSESSIONSynActivationType = _RsSESSIONSynActivationType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 1),
    _RsSESSIONSynActivationType_Type()
)
rsSESSIONSynActivationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationType.setStatus("mandatory")
_RsSESSIONSynActivationIP_Type = Ipv6Address
_RsSESSIONSynActivationIP_Object = MibTableColumn
rsSESSIONSynActivationIP = _RsSESSIONSynActivationIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 2),
    _RsSESSIONSynActivationIP_Type()
)
rsSESSIONSynActivationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationIP.setStatus("mandatory")
_RsSESSIONSynActivationPort_Type = Integer32
_RsSESSIONSynActivationPort_Object = MibTableColumn
rsSESSIONSynActivationPort = _RsSESSIONSynActivationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 3),
    _RsSESSIONSynActivationPort_Type()
)
rsSESSIONSynActivationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationPort.setStatus("mandatory")
_RsSESSIONSynActivationRxport_Type = Integer32
_RsSESSIONSynActivationRxport_Object = MibTableColumn
rsSESSIONSynActivationRxport = _RsSESSIONSynActivationRxport_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 4),
    _RsSESSIONSynActivationRxport_Type()
)
rsSESSIONSynActivationRxport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationRxport.setStatus("mandatory")
_RsSESSIONSynActivationTime_Type = Integer32
_RsSESSIONSynActivationTime_Object = MibTableColumn
rsSESSIONSynActivationTime = _RsSESSIONSynActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 5),
    _RsSESSIONSynActivationTime_Type()
)
rsSESSIONSynActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationTime.setStatus("mandatory")
_RsSESSIONSynActivationLastSecSYN_Type = Integer32
_RsSESSIONSynActivationLastSecSYN_Object = MibTableColumn
rsSESSIONSynActivationLastSecSYN = _RsSESSIONSynActivationLastSecSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 6),
    _RsSESSIONSynActivationLastSecSYN_Type()
)
rsSESSIONSynActivationLastSecSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationLastSecSYN.setStatus("mandatory")
_RsSESSIONSynActivationLastSecRqst_Type = Integer32
_RsSESSIONSynActivationLastSecRqst_Object = MibTableColumn
rsSESSIONSynActivationLastSecRqst = _RsSESSIONSynActivationLastSecRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 7),
    _RsSESSIONSynActivationLastSecRqst_Type()
)
rsSESSIONSynActivationLastSecRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationLastSecRqst.setStatus("mandatory")
_RsSESSIONSynActivationAvrgSYN_Type = Integer32
_RsSESSIONSynActivationAvrgSYN_Object = MibTableColumn
rsSESSIONSynActivationAvrgSYN = _RsSESSIONSynActivationAvrgSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 8),
    _RsSESSIONSynActivationAvrgSYN_Type()
)
rsSESSIONSynActivationAvrgSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationAvrgSYN.setStatus("mandatory")
_RsSESSIONSynActivationAvrgRqst_Type = Integer32
_RsSESSIONSynActivationAvrgRqst_Object = MibTableColumn
rsSESSIONSynActivationAvrgRqst = _RsSESSIONSynActivationAvrgRqst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 9),
    _RsSESSIONSynActivationAvrgRqst_Type()
)
rsSESSIONSynActivationAvrgRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationAvrgRqst.setStatus("mandatory")
_RsSESSIONSynActivationTotalSYN_Type = DisplayString
_RsSESSIONSynActivationTotalSYN_Object = MibTableColumn
rsSESSIONSynActivationTotalSYN = _RsSESSIONSynActivationTotalSYN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 10),
    _RsSESSIONSynActivationTotalSYN_Type()
)
rsSESSIONSynActivationTotalSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationTotalSYN.setStatus("mandatory")
_RsSESSIONSynActivationTotalDropped_Type = DisplayString
_RsSESSIONSynActivationTotalDropped_Object = MibTableColumn
rsSESSIONSynActivationTotalDropped = _RsSESSIONSynActivationTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 42, 1, 11),
    _RsSESSIONSynActivationTotalDropped_Type()
)
rsSESSIONSynActivationTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynActivationTotalDropped.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsTable_Object = MibTable
rsSESSIONSynProtectionStatisticsTable = _RsSESSIONSynProtectionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43)
)
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsTable.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsEntry_Object = MibTableRow
rsSESSIONSynProtectionStatisticsEntry = _RsSESSIONSynProtectionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1)
)
rsSESSIONSynProtectionStatisticsEntry.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONSynProtectionStatisticsPolicy"),
    (0, "SESSION-MIB", "rsSESSIONSynProtectionStatisticsIP"),
    (0, "SESSION-MIB", "rsSESSIONSynProtectionStatisticsPort"),
    (0, "SESSION-MIB", "rsSESSIONSynProtectionStatisticsRxPort"),
)
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsEntry.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsPolicy_Type = DisplayString
_RsSESSIONSynProtectionStatisticsPolicy_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsPolicy = _RsSESSIONSynProtectionStatisticsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 1),
    _RsSESSIONSynProtectionStatisticsPolicy_Type()
)
rsSESSIONSynProtectionStatisticsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsPolicy.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsIP_Type = Ipv6Address
_RsSESSIONSynProtectionStatisticsIP_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsIP = _RsSESSIONSynProtectionStatisticsIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 2),
    _RsSESSIONSynProtectionStatisticsIP_Type()
)
rsSESSIONSynProtectionStatisticsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsIP.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsPort_Type = Integer32
_RsSESSIONSynProtectionStatisticsPort_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsPort = _RsSESSIONSynProtectionStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 3),
    _RsSESSIONSynProtectionStatisticsPort_Type()
)
rsSESSIONSynProtectionStatisticsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsPort.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsRxPort_Type = Integer32
_RsSESSIONSynProtectionStatisticsRxPort_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsRxPort = _RsSESSIONSynProtectionStatisticsRxPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 4),
    _RsSESSIONSynProtectionStatisticsRxPort_Type()
)
rsSESSIONSynProtectionStatisticsRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsRxPort.setStatus("mandatory")


class _RsSESSIONSynProtectionStatisticsCurrentAttackStatus_Type(Integer32):
    """Custom type rsSESSIONSynProtectionStatisticsCurrentAttackStatus based on Integer32"""
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
        *(("protectedUnderAttack", 1),
          ("protectedNoAttack", 2),
          ("monitorNoAttack", 3),
          ("unprotected", 4))
    )


_RsSESSIONSynProtectionStatisticsCurrentAttackStatus_Type.__name__ = "Integer32"
_RsSESSIONSynProtectionStatisticsCurrentAttackStatus_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsCurrentAttackStatus = _RsSESSIONSynProtectionStatisticsCurrentAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 5),
    _RsSESSIONSynProtectionStatisticsCurrentAttackStatus_Type()
)
rsSESSIONSynProtectionStatisticsCurrentAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsCurrentAttackStatus.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsLastSecSynCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsLastSecSynCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsLastSecSynCount = _RsSESSIONSynProtectionStatisticsLastSecSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 6),
    _RsSESSIONSynProtectionStatisticsLastSecSynCount_Type()
)
rsSESSIONSynProtectionStatisticsLastSecSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsLastSecSynCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsLastSecGoodCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsLastSecGoodCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsLastSecGoodCount = _RsSESSIONSynProtectionStatisticsLastSecGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 7),
    _RsSESSIONSynProtectionStatisticsLastSecGoodCount_Type()
)
rsSESSIONSynProtectionStatisticsLastSecGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsLastSecGoodCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsAverageSynCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsAverageSynCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsAverageSynCount = _RsSESSIONSynProtectionStatisticsAverageSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 8),
    _RsSESSIONSynProtectionStatisticsAverageSynCount_Type()
)
rsSESSIONSynProtectionStatisticsAverageSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsAverageSynCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsAverageGoodCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsAverageGoodCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsAverageGoodCount = _RsSESSIONSynProtectionStatisticsAverageGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 9),
    _RsSESSIONSynProtectionStatisticsAverageGoodCount_Type()
)
rsSESSIONSynProtectionStatisticsAverageGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsAverageGoodCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsPeakSynCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsPeakSynCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsPeakSynCount = _RsSESSIONSynProtectionStatisticsPeakSynCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 10),
    _RsSESSIONSynProtectionStatisticsPeakSynCount_Type()
)
rsSESSIONSynProtectionStatisticsPeakSynCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsPeakSynCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsPeakGoodCount_Type = Integer32
_RsSESSIONSynProtectionStatisticsPeakGoodCount_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsPeakGoodCount = _RsSESSIONSynProtectionStatisticsPeakGoodCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 11),
    _RsSESSIONSynProtectionStatisticsPeakGoodCount_Type()
)
rsSESSIONSynProtectionStatisticsPeakGoodCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsPeakGoodCount.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsActivityTime_Type = Integer32
_RsSESSIONSynProtectionStatisticsActivityTime_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsActivityTime = _RsSESSIONSynProtectionStatisticsActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 12),
    _RsSESSIONSynProtectionStatisticsActivityTime_Type()
)
rsSESSIONSynProtectionStatisticsActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsActivityTime.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsLastAttackStartTime_Type = DisplayString
_RsSESSIONSynProtectionStatisticsLastAttackStartTime_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsLastAttackStartTime = _RsSESSIONSynProtectionStatisticsLastAttackStartTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 13),
    _RsSESSIONSynProtectionStatisticsLastAttackStartTime_Type()
)
rsSESSIONSynProtectionStatisticsLastAttackStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsLastAttackStartTime.setStatus("mandatory")
_RsSESSIONSynProtectionStatisticsLastAttackTermTime_Type = DisplayString
_RsSESSIONSynProtectionStatisticsLastAttackTermTime_Object = MibTableColumn
rsSESSIONSynProtectionStatisticsLastAttackTermTime = _RsSESSIONSynProtectionStatisticsLastAttackTermTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 43, 1, 14),
    _RsSESSIONSynProtectionStatisticsLastAttackTermTime_Type()
)
rsSESSIONSynProtectionStatisticsLastAttackTermTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONSynProtectionStatisticsLastAttackTermTime.setStatus("mandatory")


class _RsSESSIONTableFullAction_Type(Integer32):
    """Custom type rsSESSIONTableFullAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_RsSESSIONTableFullAction_Type.__name__ = "Integer32"
_RsSESSIONTableFullAction_Object = MibScalar
rsSESSIONTableFullAction = _RsSESSIONTableFullAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 44),
    _RsSESSIONTableFullAction_Type()
)
rsSESSIONTableFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableFullAction.setStatus("mandatory")


class _RsSESSIONTableFullActiveThreshold_Type(Integer32):
    """Custom type rsSESSIONTableFullActiveThreshold based on Integer32"""
    defaultValue = 95


_RsSESSIONTableFullActiveThreshold_Type.__name__ = "Integer32"
_RsSESSIONTableFullActiveThreshold_Object = MibScalar
rsSESSIONTableFullActiveThreshold = _RsSESSIONTableFullActiveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 45),
    _RsSESSIONTableFullActiveThreshold_Type()
)
rsSESSIONTableFullActiveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableFullActiveThreshold.setStatus("mandatory")


class _RsSESSIONTableFullDeactiveThreshold_Type(Integer32):
    """Custom type rsSESSIONTableFullDeactiveThreshold based on Integer32"""
    defaultValue = 90


_RsSESSIONTableFullDeactiveThreshold_Type.__name__ = "Integer32"
_RsSESSIONTableFullDeactiveThreshold_Object = MibScalar
rsSESSIONTableFullDeactiveThreshold = _RsSESSIONTableFullDeactiveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 46),
    _RsSESSIONTableFullDeactiveThreshold_Type()
)
rsSESSIONTableFullDeactiveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONTableFullDeactiveThreshold.setStatus("mandatory")


class _RsSESSIONSessionTCPAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionTCPAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionTCPAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionTCPAgingTime_Object = MibScalar
rsSESSIONSessionTCPAgingTime = _RsSESSIONSessionTCPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 47),
    _RsSESSIONSessionTCPAgingTime_Type()
)
rsSESSIONSessionTCPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionTCPAgingTime.setStatus("mandatory")


class _RsSESSIONSessionUDPAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionUDPAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionUDPAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionUDPAgingTime_Object = MibScalar
rsSESSIONSessionUDPAgingTime = _RsSESSIONSessionUDPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 48),
    _RsSESSIONSessionUDPAgingTime_Type()
)
rsSESSIONSessionUDPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionUDPAgingTime.setStatus("mandatory")


class _RsSESSIONSessionSCTPAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionSCTPAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionSCTPAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionSCTPAgingTime_Object = MibScalar
rsSESSIONSessionSCTPAgingTime = _RsSESSIONSessionSCTPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 49),
    _RsSESSIONSessionSCTPAgingTime_Type()
)
rsSESSIONSessionSCTPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionSCTPAgingTime.setStatus("mandatory")


class _RsSESSIONSessionICMPAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionICMPAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionICMPAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionICMPAgingTime_Object = MibScalar
rsSESSIONSessionICMPAgingTime = _RsSESSIONSessionICMPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 50),
    _RsSESSIONSessionICMPAgingTime_Type()
)
rsSESSIONSessionICMPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionICMPAgingTime.setStatus("mandatory")


class _RsSESSIONSessionGREAgingTime_Type(Integer32):
    """Custom type rsSESSIONSessionGREAgingTime based on Integer32"""
    defaultValue = 100


_RsSESSIONSessionGREAgingTime_Type.__name__ = "Integer32"
_RsSESSIONSessionGREAgingTime_Object = MibScalar
rsSESSIONSessionGREAgingTime = _RsSESSIONSessionGREAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 51),
    _RsSESSIONSessionGREAgingTime_Type()
)
rsSESSIONSessionGREAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONSessionGREAgingTime.setStatus("mandatory")


class _RsSESSIONRemoveEntryAtSessionEndTimeout_Type(Integer32):
    """Custom type rsSESSIONRemoveEntryAtSessionEndTimeout based on Integer32"""
    defaultValue = 5


_RsSESSIONRemoveEntryAtSessionEndTimeout_Type.__name__ = "Integer32"
_RsSESSIONRemoveEntryAtSessionEndTimeout_Object = MibScalar
rsSESSIONRemoveEntryAtSessionEndTimeout = _RsSESSIONRemoveEntryAtSessionEndTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 52),
    _RsSESSIONRemoveEntryAtSessionEndTimeout_Type()
)
rsSESSIONRemoveEntryAtSessionEndTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSESSIONRemoveEntryAtSessionEndTimeout.setStatus("mandatory")
_RsSESSIONTotalUsed_Type = Integer32
_RsSESSIONTotalUsed_Object = MibScalar
rsSESSIONTotalUsed = _RsSESSIONTotalUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 53),
    _RsSESSIONTotalUsed_Type()
)
rsSESSIONTotalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONTotalUsed.setStatus("mandatory")
_RsSESSIONUsedEntriesTable_Object = MibTable
rsSESSIONUsedEntriesTable = _RsSESSIONUsedEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 54)
)
if mibBuilder.loadTexts:
    rsSESSIONUsedEntriesTable.setStatus("mandatory")
_RsSESSIONUsedEntries_Object = MibTableRow
rsSESSIONUsedEntries = _RsSESSIONUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 54, 1)
)
rsSESSIONUsedEntries.setIndexNames(
    (0, "SESSION-MIB", "rsSESSIONEngineID"),
)
if mibBuilder.loadTexts:
    rsSESSIONUsedEntries.setStatus("mandatory")
_RsSESSIONEngineID_Type = Integer32
_RsSESSIONEngineID_Object = MibTableColumn
rsSESSIONEngineID = _RsSESSIONEngineID_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 54, 1, 1),
    _RsSESSIONEngineID_Type()
)
rsSESSIONEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONEngineID.setStatus("mandatory")
_RsSESSIONUsedPerEngine_Type = Integer32
_RsSESSIONUsedPerEngine_Object = MibTableColumn
rsSESSIONUsedPerEngine = _RsSESSIONUsedPerEngine_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 54, 1, 2),
    _RsSESSIONUsedPerEngine_Type()
)
rsSESSIONUsedPerEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSESSIONUsedPerEngine.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsSESSIONTablesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 0, 1)
)
rsSESSIONTablesFull.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSESSIONTablesFull.setStatus(
        ""
    )

rsSESSIONSynTriggerUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 0, 2)
)
rsSESSIONSynTriggerUpdate.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSESSIONSynTriggerUpdate.setStatus(
        ""
    )

rsSESSIONTablesNotFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 104, 0, 3)
)
rsSESSIONTablesNotFull.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSESSIONTablesNotFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SESSION-MIB",
    **{"NetNumber": NetNumber,
       "rsSESSIONTablesFull": rsSESSIONTablesFull,
       "rsSESSIONSynTriggerUpdate": rsSESSIONSynTriggerUpdate,
       "rsSESSIONTablesNotFull": rsSESSIONTablesNotFull,
       "rsSESSIONSessionTableStatus": rsSESSIONSessionTableStatus,
       "rsSESSIONSessionTableLookupMode": rsSESSIONSessionTableLookupMode,
       "rsSESSIONRemoveEntryAtSessionEnd": rsSESSIONRemoveEntryAtSessionEnd,
       "rsSESSIONSynProtectionStatus": rsSESSIONSynProtectionStatus,
       "rsSESSIONSynProtectionTimeout": rsSESSIONSynProtectionTimeout,
       "rsSESSIONSynProtectionActivationBound": rsSESSIONSynProtectionActivationBound,
       "rsSESSIONSynProtectionDeactivationBound": rsSESSIONSynProtectionDeactivationBound,
       "rsSESSIONSynProtectionTrackingTime": rsSESSIONSynProtectionTrackingTime,
       "rsSESSIONSynProtectionMinSynForTrigger": rsSESSIONSynProtectionMinSynForTrigger,
       "rsSESSIONSynTriggerTable": rsSESSIONSynTriggerTable,
       "rsSESSIONSynTriggerEntry": rsSESSIONSynTriggerEntry,
       "rsSESSIONSynTriggerIP": rsSESSIONSynTriggerIP,
       "rsSESSIONSynTriggerPort": rsSESSIONSynTriggerPort,
       "rsSESSIONSynTriggerRxport": rsSESSIONSynTriggerRxport,
       "rsSESSIONSynTriggerTime": rsSESSIONSynTriggerTime,
       "rsSESSIONSynTriggerLastSecSYN": rsSESSIONSynTriggerLastSecSYN,
       "rsSESSIONSynTriggerLastSecRqst": rsSESSIONSynTriggerLastSecRqst,
       "rsSESSIONSynTriggerAvrgSYN": rsSESSIONSynTriggerAvrgSYN,
       "rsSESSIONSynTriggerAvrgRqst": rsSESSIONSynTriggerAvrgRqst,
       "rsSESSIONTuning": rsSESSIONTuning,
       "rsSESSIONSynProtectionTuning": rsSESSIONSynProtectionTuning,
       "rsSESSIONSynProtectionEntries": rsSESSIONSynProtectionEntries,
       "rsSESSIONSynProtectionEntriesAfterReset": rsSESSIONSynProtectionEntriesAfterReset,
       "rsSESSIONSynProtectionRqstsTuning": rsSESSIONSynProtectionRqstsTuning,
       "rsSESSIONSynProtectionRqstsEntries": rsSESSIONSynProtectionRqstsEntries,
       "rsSESSIONSynProtectionRqstsEntriesAfterReset": rsSESSIONSynProtectionRqstsEntriesAfterReset,
       "rsSESSIONSynProtectionTriggerTuning": rsSESSIONSynProtectionTriggerTuning,
       "rsSESSIONSynProtectionTriggerEntries": rsSESSIONSynProtectionTriggerEntries,
       "rsSESSIONSynProtectionTriggerEntriesAfterReset": rsSESSIONSynProtectionTriggerEntriesAfterReset,
       "rsSESSIONSynProtectionPolicyTuning": rsSESSIONSynProtectionPolicyTuning,
       "rsSESSIONSynProtectionPolicyEntries": rsSESSIONSynProtectionPolicyEntries,
       "rsSESSIONSynProtectionPolicyEntriesAfterReset": rsSESSIONSynProtectionPolicyEntriesAfterReset,
       "rsSESSIONPasvProtocolsTuning": rsSESSIONPasvProtocolsTuning,
       "rsSESSIONPasvProtocolsEntries": rsSESSIONPasvProtocolsEntries,
       "rsSESSIONPasvProtocolsEntriesAfterReset": rsSESSIONPasvProtocolsEntriesAfterReset,
       "rsSESSIONL3SynFloodReportTuning": rsSESSIONL3SynFloodReportTuning,
       "rsSESSIONL3SynFloodReportEntries": rsSESSIONL3SynFloodReportEntries,
       "rsSESSIONL3SynFloodReportEntriesAfterReset": rsSESSIONL3SynFloodReportEntriesAfterReset,
       "rsSESSIONTableSynFloodTriggersTuning": rsSESSIONTableSynFloodTriggersTuning,
       "rsSESSIONTableSynFloodTriggersEntries": rsSESSIONTableSynFloodTriggersEntries,
       "rsSESSIONTableSynFloodTriggersEntriesAfterReset": rsSESSIONTableSynFloodTriggersEntriesAfterReset,
       "rsSESSIONSessionTuning": rsSESSIONSessionTuning,
       "rsSESSIONSessionEntries": rsSESSIONSessionEntries,
       "rsSESSIONSessionEntriesAfterReset": rsSESSIONSessionEntriesAfterReset,
       "rsSESSIONAckReflectionTableTuning": rsSESSIONAckReflectionTableTuning,
       "rsSESSIONAckReflectionTableEntries": rsSESSIONAckReflectionTableEntries,
       "rsSESSIONAckReflectionTableEntriesAfterReset": rsSESSIONAckReflectionTableEntriesAfterReset,
       "rsSESSIONSynProtectionStatsTuning": rsSESSIONSynProtectionStatsTuning,
       "rsSESSIONSynProtectionStatsEntries": rsSESSIONSynProtectionStatsEntries,
       "rsSESSIONSynProtectionStatsEntriesAfterReset": rsSESSIONSynProtectionStatsEntriesAfterReset,
       "rsSESSIONSessionResetsTableTuning": rsSESSIONSessionResetsTableTuning,
       "rsSESSIONSessionResetsEntries": rsSESSIONSessionResetsEntries,
       "rsSESSIONSessionResetsEntriesAfterReset": rsSESSIONSessionResetsEntriesAfterReset,
       "rsSESSIONSynProtectionPolicyTable": rsSESSIONSynProtectionPolicyTable,
       "rsSESSIONSynProtectionPolicyEntry": rsSESSIONSynProtectionPolicyEntry,
       "rsSESSIONSynTriggerPolicyName": rsSESSIONSynTriggerPolicyName,
       "rsSESSIONSynTriggerPolicyIndex": rsSESSIONSynTriggerPolicyIndex,
       "rsSESSIONSynTriggerPolicyDescription": rsSESSIONSynTriggerPolicyDescription,
       "rsSESSIONSynTriggerPolicyDestination": rsSESSIONSynTriggerPolicyDestination,
       "rsSESSIONSynTriggerPolicyPhysicalPortGroup": rsSESSIONSynTriggerPolicyPhysicalPortGroup,
       "rsSESSIONSynTriggerPolicyService": rsSESSIONSynTriggerPolicyService,
       "rsSESSIONSynTriggerPolicyProtectionMode": rsSESSIONSynTriggerPolicyProtectionMode,
       "rsSESSIONSynTriggerPolicyOperationalStatus": rsSESSIONSynTriggerPolicyOperationalStatus,
       "rsSESSIONSynTriggerPolicyStatus": rsSESSIONSynTriggerPolicyStatus,
       "rsSESSIONSynTriggerPolicyVerificationType": rsSESSIONSynTriggerPolicyVerificationType,
       "rsSESSIONSynTriggerPolicyActivationThreshold": rsSESSIONSynTriggerPolicyActivationThreshold,
       "rsSESSIONSynTriggerPolicyDeactivationThreshold": rsSESSIONSynTriggerPolicyDeactivationThreshold,
       "rsSESSIONSynTriggerPolicyCountStatistics": rsSESSIONSynTriggerPolicyCountStatistics,
       "rsSESSIONSynProtectionPolicyDummy": rsSESSIONSynProtectionPolicyDummy,
       "rsSESSIONSynProtectionAttackAgingTime": rsSESSIONSynProtectionAttackAgingTime,
       "rsSESSIONSendResetToServer": rsSESSIONSendResetToServer,
       "rsSESSIONSynProtectionGlobalStatisticsStatus": rsSESSIONSynProtectionGlobalStatisticsStatus,
       "rsSESSIONSessionAgingTime": rsSESSIONSessionAgingTime,
       "rsSESSIONSessionEntriesNum": rsSESSIONSessionEntriesNum,
       "rsSESSIONSessionMaxDisplayEntries": rsSESSIONSessionMaxDisplayEntries,
       "rsSESSIONDisplayFiltersTable": rsSESSIONDisplayFiltersTable,
       "rsSESSIONDisplayFilterEntry": rsSESSIONDisplayFilterEntry,
       "rsSESSIONDisplayFilterName": rsSESSIONDisplayFilterName,
       "rsSESSIONDisplayFilterSrcIP": rsSESSIONDisplayFilterSrcIP,
       "rsSESSIONDisplayFilterSrcIPMask": rsSESSIONDisplayFilterSrcIPMask,
       "rsSESSIONDisplayFilterDstIP": rsSESSIONDisplayFilterDstIP,
       "rsSESSIONDisplayFilterDstIPMask": rsSESSIONDisplayFilterDstIPMask,
       "rsSESSIONDisplayFilterSrcPort": rsSESSIONDisplayFilterSrcPort,
       "rsSESSIONDisplayFilterDstPort": rsSESSIONDisplayFilterDstPort,
       "rsSESSIONDisplayFilterPhysicalPort": rsSESSIONDisplayFilterPhysicalPort,
       "rsSESSIONDisplayFilterStatus": rsSESSIONDisplayFilterStatus,
       "rsSESSIONSessionTableEntriesTable": rsSESSIONSessionTableEntriesTable,
       "rsSESSIONSessionTableEntry": rsSESSIONSessionTableEntry,
       "rsSESSIONSessionTableEntryIndex": rsSESSIONSessionTableEntryIndex,
       "rsSESSIONSessionTableEntrySrcIP": rsSESSIONSessionTableEntrySrcIP,
       "rsSESSIONSessionTableEntryDstIP": rsSESSIONSessionTableEntryDstIP,
       "rsSESSIONSessionTableEntrySrcPort": rsSESSIONSessionTableEntrySrcPort,
       "rsSESSIONSessionTableEntryDstPort": rsSESSIONSessionTableEntryDstPort,
       "rsSESSIONSessionTableEntryPhysicalPort": rsSESSIONSessionTableEntryPhysicalPort,
       "rsSESSIONSessionTableEntryLifetime": rsSESSIONSessionTableEntryLifetime,
       "rsSESSIONSessionTableEntryAgingType": rsSESSIONSessionTableEntryAgingType,
       "rsSESSIONSessionTableEntrySYNData": rsSESSIONSessionTableEntrySYNData,
       "rsSESSIONSessionTableEntryRplyPhysicalPort": rsSESSIONSessionTableEntryRplyPhysicalPort,
       "rsSESSIONSessionTableEntryIPProtocol": rsSESSIONSessionTableEntryIPProtocol,
       "rsSESSIONSessionTableEntryDummy": rsSESSIONSessionTableEntryDummy,
       "rsSESSIONAckReflectionProtectionMode": rsSESSIONAckReflectionProtectionMode,
       "rsSESSIONAckReflectionSamplingPerSecond": rsSESSIONAckReflectionSamplingPerSecond,
       "rsSESSIONAckReflectionDropThreshold": rsSESSIONAckReflectionDropThreshold,
       "rsSESSIONSynProtectionMaxTrapsPerTimeUnit": rsSESSIONSynProtectionMaxTrapsPerTimeUnit,
       "rsSESSIONSynProtectionTrapsTimeUnit": rsSESSIONSynProtectionTrapsTimeUnit,
       "rsSESSIONNewSynTriggerTable": rsSESSIONNewSynTriggerTable,
       "rsSESSIONNewSynTriggerEntry": rsSESSIONNewSynTriggerEntry,
       "rsSESSIONNewSynTriggerType": rsSESSIONNewSynTriggerType,
       "rsSESSIONNewSynTriggerIP": rsSESSIONNewSynTriggerIP,
       "rsSESSIONNewSynTriggerPort": rsSESSIONNewSynTriggerPort,
       "rsSESSIONNewSynTriggerRxport": rsSESSIONNewSynTriggerRxport,
       "rsSESSIONNewSynTriggerTime": rsSESSIONNewSynTriggerTime,
       "rsSESSIONNewSynTriggerLastSecSYN": rsSESSIONNewSynTriggerLastSecSYN,
       "rsSESSIONNewSynTriggerLastSecRqst": rsSESSIONNewSynTriggerLastSecRqst,
       "rsSESSIONNewSynTriggerAvrgSYN": rsSESSIONNewSynTriggerAvrgSYN,
       "rsSESSIONNewSynTriggerAvrgRqst": rsSESSIONNewSynTriggerAvrgRqst,
       "rsSESSIONNewSynTriggerTotalSYN": rsSESSIONNewSynTriggerTotalSYN,
       "rsSESSIONNewSynTriggerTotalDropped": rsSESSIONNewSynTriggerTotalDropped,
       "rsSESSIONSynStatsMaxDestPerPolicy": rsSESSIONSynStatsMaxDestPerPolicy,
       "rsSESSIONSynStatsTimePeriod": rsSESSIONSynStatsTimePeriod,
       "rsSESSIONSynStatsDisplayPolicyName": rsSESSIONSynStatsDisplayPolicyName,
       "rsSESSIONSynStatisticsTable": rsSESSIONSynStatisticsTable,
       "rsSESSIONSynStatisticsEntry": rsSESSIONSynStatisticsEntry,
       "rsSESSIONSynStatisticsPolicy": rsSESSIONSynStatisticsPolicy,
       "rsSESSIONSynStatisticsIP": rsSESSIONSynStatisticsIP,
       "rsSESSIONSynStatisticsPort": rsSESSIONSynStatisticsPort,
       "rsSESSIONSynStatisticsRxPort": rsSESSIONSynStatisticsRxPort,
       "rsSESSIONSynStatisticsCurrentAttackStatus": rsSESSIONSynStatisticsCurrentAttackStatus,
       "rsSESSIONSynStatisticsLastSecSynCount": rsSESSIONSynStatisticsLastSecSynCount,
       "rsSESSIONSynStatisticsLastSecGoodCount": rsSESSIONSynStatisticsLastSecGoodCount,
       "rsSESSIONSynStatisticsAverageSynCount": rsSESSIONSynStatisticsAverageSynCount,
       "rsSESSIONSynStatisticsAverageGoodCount": rsSESSIONSynStatisticsAverageGoodCount,
       "rsSESSIONSynStatisticsPeakSynCount": rsSESSIONSynStatisticsPeakSynCount,
       "rsSESSIONSynStatisticsPeakGoodCount": rsSESSIONSynStatisticsPeakGoodCount,
       "rsSESSIONSynStatisticsActivityTime": rsSESSIONSynStatisticsActivityTime,
       "rsSESSIONSynStatisticsLastAttackStartTime": rsSESSIONSynStatisticsLastAttackStartTime,
       "rsSESSIONSynStatisticsLastAttackTermTime": rsSESSIONSynStatisticsLastAttackTermTime,
       "rsSESSIONSynStatisticsTableDummy": rsSESSIONSynStatisticsTableDummy,
       "rsSESSIONSynStatisticsReset": rsSESSIONSynStatisticsReset,
       "rsSESSIONH225AgingTime": rsSESSIONH225AgingTime,
       "rsSESSIONNoAgingMode": rsSESSIONNoAgingMode,
       "rsSESSIONProtectionMode": rsSESSIONProtectionMode,
       "rsSESSIONProtectionShortLifetime": rsSESSIONProtectionShortLifetime,
       "rsSESSIONProtectionMaxSessions": rsSESSIONProtectionMaxSessions,
       "rsSESSIONFiltersTable": rsSESSIONFiltersTable,
       "rsSESSIONFilterEntry": rsSESSIONFilterEntry,
       "rsSESSIONFilterName": rsSESSIONFilterName,
       "rsSESSIONFilterSrcIP": rsSESSIONFilterSrcIP,
       "rsSESSIONFilterSrcIPMask": rsSESSIONFilterSrcIPMask,
       "rsSESSIONFilterDstIP": rsSESSIONFilterDstIP,
       "rsSESSIONFilterDstIPMask": rsSESSIONFilterDstIPMask,
       "rsSESSIONFilterSrcPort": rsSESSIONFilterSrcPort,
       "rsSESSIONFilterDstPort": rsSESSIONFilterDstPort,
       "rsSESSIONFilterPhysicalPort": rsSESSIONFilterPhysicalPort,
       "rsSESSIONFilterStatus": rsSESSIONFilterStatus,
       "rsSESSIONTableEntriesTable": rsSESSIONTableEntriesTable,
       "rsSESSIONTableEntry": rsSESSIONTableEntry,
       "rsSESSIONTableEntryIndex": rsSESSIONTableEntryIndex,
       "rsSESSIONTableEntrySrcIP": rsSESSIONTableEntrySrcIP,
       "rsSESSIONTableEntryDstIP": rsSESSIONTableEntryDstIP,
       "rsSESSIONTableEntrySrcPort": rsSESSIONTableEntrySrcPort,
       "rsSESSIONTableEntryDstPort": rsSESSIONTableEntryDstPort,
       "rsSESSIONTableEntryPhysicalPort": rsSESSIONTableEntryPhysicalPort,
       "rsSESSIONTableEntryLifetime": rsSESSIONTableEntryLifetime,
       "rsSESSIONTableEntryAgingType": rsSESSIONTableEntryAgingType,
       "rsSESSIONTableEntrySYNData": rsSESSIONTableEntrySYNData,
       "rsSESSIONTableEntryRplyPhysicalPort": rsSESSIONTableEntryRplyPhysicalPort,
       "rsSESSIONTableEntryIPProtocol": rsSESSIONTableEntryIPProtocol,
       "rsSESSIONTableEntryPolicyName": rsSESSIONTableEntryPolicyName,
       "rsSESSIONTableEntryCoreIndex": rsSESSIONTableEntryCoreIndex,
       "rsSESSIONSynActivationTable": rsSESSIONSynActivationTable,
       "rsSESSIONSynActivationEntry": rsSESSIONSynActivationEntry,
       "rsSESSIONSynActivationType": rsSESSIONSynActivationType,
       "rsSESSIONSynActivationIP": rsSESSIONSynActivationIP,
       "rsSESSIONSynActivationPort": rsSESSIONSynActivationPort,
       "rsSESSIONSynActivationRxport": rsSESSIONSynActivationRxport,
       "rsSESSIONSynActivationTime": rsSESSIONSynActivationTime,
       "rsSESSIONSynActivationLastSecSYN": rsSESSIONSynActivationLastSecSYN,
       "rsSESSIONSynActivationLastSecRqst": rsSESSIONSynActivationLastSecRqst,
       "rsSESSIONSynActivationAvrgSYN": rsSESSIONSynActivationAvrgSYN,
       "rsSESSIONSynActivationAvrgRqst": rsSESSIONSynActivationAvrgRqst,
       "rsSESSIONSynActivationTotalSYN": rsSESSIONSynActivationTotalSYN,
       "rsSESSIONSynActivationTotalDropped": rsSESSIONSynActivationTotalDropped,
       "rsSESSIONSynProtectionStatisticsTable": rsSESSIONSynProtectionStatisticsTable,
       "rsSESSIONSynProtectionStatisticsEntry": rsSESSIONSynProtectionStatisticsEntry,
       "rsSESSIONSynProtectionStatisticsPolicy": rsSESSIONSynProtectionStatisticsPolicy,
       "rsSESSIONSynProtectionStatisticsIP": rsSESSIONSynProtectionStatisticsIP,
       "rsSESSIONSynProtectionStatisticsPort": rsSESSIONSynProtectionStatisticsPort,
       "rsSESSIONSynProtectionStatisticsRxPort": rsSESSIONSynProtectionStatisticsRxPort,
       "rsSESSIONSynProtectionStatisticsCurrentAttackStatus": rsSESSIONSynProtectionStatisticsCurrentAttackStatus,
       "rsSESSIONSynProtectionStatisticsLastSecSynCount": rsSESSIONSynProtectionStatisticsLastSecSynCount,
       "rsSESSIONSynProtectionStatisticsLastSecGoodCount": rsSESSIONSynProtectionStatisticsLastSecGoodCount,
       "rsSESSIONSynProtectionStatisticsAverageSynCount": rsSESSIONSynProtectionStatisticsAverageSynCount,
       "rsSESSIONSynProtectionStatisticsAverageGoodCount": rsSESSIONSynProtectionStatisticsAverageGoodCount,
       "rsSESSIONSynProtectionStatisticsPeakSynCount": rsSESSIONSynProtectionStatisticsPeakSynCount,
       "rsSESSIONSynProtectionStatisticsPeakGoodCount": rsSESSIONSynProtectionStatisticsPeakGoodCount,
       "rsSESSIONSynProtectionStatisticsActivityTime": rsSESSIONSynProtectionStatisticsActivityTime,
       "rsSESSIONSynProtectionStatisticsLastAttackStartTime": rsSESSIONSynProtectionStatisticsLastAttackStartTime,
       "rsSESSIONSynProtectionStatisticsLastAttackTermTime": rsSESSIONSynProtectionStatisticsLastAttackTermTime,
       "rsSESSIONTableFullAction": rsSESSIONTableFullAction,
       "rsSESSIONTableFullActiveThreshold": rsSESSIONTableFullActiveThreshold,
       "rsSESSIONTableFullDeactiveThreshold": rsSESSIONTableFullDeactiveThreshold,
       "rsSESSIONSessionTCPAgingTime": rsSESSIONSessionTCPAgingTime,
       "rsSESSIONSessionUDPAgingTime": rsSESSIONSessionUDPAgingTime,
       "rsSESSIONSessionSCTPAgingTime": rsSESSIONSessionSCTPAgingTime,
       "rsSESSIONSessionICMPAgingTime": rsSESSIONSessionICMPAgingTime,
       "rsSESSIONSessionGREAgingTime": rsSESSIONSessionGREAgingTime,
       "rsSESSIONRemoveEntryAtSessionEndTimeout": rsSESSIONRemoveEntryAtSessionEndTimeout,
       "rsSESSIONTotalUsed": rsSESSIONTotalUsed,
       "rsSESSIONUsedEntriesTable": rsSESSIONUsedEntriesTable,
       "rsSESSIONUsedEntries": rsSESSIONUsedEntries,
       "rsSESSIONEngineID": rsSESSIONEngineID,
       "rsSESSIONUsedPerEngine": rsSESSIONUsedPerEngine}
)
