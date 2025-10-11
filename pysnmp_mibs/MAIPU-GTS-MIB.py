# SNMP MIB module (MAIPU-GTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-GTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:04 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

maipuGtsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64(TextualConvention, Counter64):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Maipu_ObjectIdentity = ObjectIdentity
maipu = _Maipu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651)
)
_MpMgmt2_ObjectIdentity = ObjectIdentity
mpMgmt2 = _MpMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6)
)
_MpRouterTech_ObjectIdentity = ObjectIdentity
mpRouterTech = _MpRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2)
)
_MpRtQoSv2_ObjectIdentity = ObjectIdentity
mpRtQoSv2 = _MpRtQoSv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3)
)
_MaipuGtsMIBObjects_ObjectIdentity = ObjectIdentity
maipuGtsMIBObjects = _MaipuGtsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1)
)
_MpGtsConfigs_ObjectIdentity = ObjectIdentity
mpGtsConfigs = _MpGtsConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1)
)
_MpGtsInterfaceCfgTable_Object = MibTable
mpGtsInterfaceCfgTable = _MpGtsInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpGtsInterfaceCfgTable.setStatus("current")
_MpGtsInterfaceCfgEntry_Object = MibTableRow
mpGtsInterfaceCfgEntry = _MpGtsInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1)
)
mpGtsInterfaceCfgEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsIFCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsInterfaceCfgEntry.setStatus("current")


class _MpGtsIFCfgRowIndex_Type(Integer32):
    """Custom type mpGtsIFCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpGtsIFCfgRowIndex_Type.__name__ = "Integer32"
_MpGtsIFCfgRowIndex_Object = MibTableColumn
mpGtsIFCfgRowIndex = _MpGtsIFCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 1),
    _MpGtsIFCfgRowIndex_Type()
)
mpGtsIFCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsIFCfgRowIndex.setStatus("current")


class _MpGtsIFCfgType_Type(Integer32):
    """Custom type mpGtsIFCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpGtsIFCfgType_Type.__name__ = "Integer32"
_MpGtsIFCfgType_Object = MibTableColumn
mpGtsIFCfgType = _MpGtsIFCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 2),
    _MpGtsIFCfgType_Type()
)
mpGtsIFCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgType.setStatus("current")


class _MpGtsIFCfgAclName_Type(DisplayString):
    """Custom type mpGtsIFCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpGtsIFCfgAclName_Type.__name__ = "DisplayString"
_MpGtsIFCfgAclName_Object = MibTableColumn
mpGtsIFCfgAclName = _MpGtsIFCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 3),
    _MpGtsIFCfgAclName_Type()
)
mpGtsIFCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgAclName.setStatus("current")
_MpGtsIFCfgRate64_Type = Unsigned64
_MpGtsIFCfgRate64_Object = MibTableColumn
mpGtsIFCfgRate64 = _MpGtsIFCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 4),
    _MpGtsIFCfgRate64_Type()
)
mpGtsIFCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFCfgRate64.setUnits("bits/second")
_MpGtsIFCfgBurstSize_Type = Unsigned32
_MpGtsIFCfgBurstSize_Object = MibTableColumn
mpGtsIFCfgBurstSize = _MpGtsIFCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 5),
    _MpGtsIFCfgBurstSize_Type()
)
mpGtsIFCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFCfgBurstSize.setUnits("bits")
_MpGtsIFCfgExtBurstSize_Type = Unsigned32
_MpGtsIFCfgExtBurstSize_Object = MibTableColumn
mpGtsIFCfgExtBurstSize = _MpGtsIFCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 6),
    _MpGtsIFCfgExtBurstSize_Type()
)
mpGtsIFCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFCfgExtBurstSize.setUnits("bits")
_MpGtsIFCfgQueueLimit_Type = Unsigned32
_MpGtsIFCfgQueueLimit_Object = MibTableColumn
mpGtsIFCfgQueueLimit = _MpGtsIFCfgQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 1, 1, 7),
    _MpGtsIFCfgQueueLimit_Type()
)
mpGtsIFCfgQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFCfgQueueLimit.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFCfgQueueLimit.setUnits("packets")
_MpGtsFrameRelayVCCfgTable_Object = MibTable
mpGtsFrameRelayVCCfgTable = _MpGtsFrameRelayVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpGtsFrameRelayVCCfgTable.setStatus("current")
_MpGtsFrameRelayVCCfgEntry_Object = MibTableRow
mpGtsFrameRelayVCCfgEntry = _MpGtsFrameRelayVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1)
)
mpGtsFrameRelayVCCfgEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsFRCfgDLCI"),
    (0, "MAIPU-GTS-MIB", "mpGtsFRCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsFrameRelayVCCfgEntry.setStatus("current")


class _MpGtsFRCfgDLCI_Type(Unsigned32):
    """Custom type mpGtsFRCfgDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MpGtsFRCfgDLCI_Type.__name__ = "Unsigned32"
_MpGtsFRCfgDLCI_Object = MibTableColumn
mpGtsFRCfgDLCI = _MpGtsFRCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 1),
    _MpGtsFRCfgDLCI_Type()
)
mpGtsFRCfgDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsFRCfgDLCI.setStatus("current")


class _MpGtsFRCfgRowIndex_Type(Integer32):
    """Custom type mpGtsFRCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpGtsFRCfgRowIndex_Type.__name__ = "Integer32"
_MpGtsFRCfgRowIndex_Object = MibTableColumn
mpGtsFRCfgRowIndex = _MpGtsFRCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 2),
    _MpGtsFRCfgRowIndex_Type()
)
mpGtsFRCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsFRCfgRowIndex.setStatus("current")


class _MpGtsFRCfgType_Type(Integer32):
    """Custom type mpGtsFRCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpGtsFRCfgType_Type.__name__ = "Integer32"
_MpGtsFRCfgType_Object = MibTableColumn
mpGtsFRCfgType = _MpGtsFRCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 3),
    _MpGtsFRCfgType_Type()
)
mpGtsFRCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgType.setStatus("current")


class _MpGtsFRCfgAclName_Type(DisplayString):
    """Custom type mpGtsFRCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpGtsFRCfgAclName_Type.__name__ = "DisplayString"
_MpGtsFRCfgAclName_Object = MibTableColumn
mpGtsFRCfgAclName = _MpGtsFRCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 4),
    _MpGtsFRCfgAclName_Type()
)
mpGtsFRCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgAclName.setStatus("current")
_MpGtsFRCfgRate64_Type = Unsigned64
_MpGtsFRCfgRate64_Object = MibTableColumn
mpGtsFRCfgRate64 = _MpGtsFRCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 5),
    _MpGtsFRCfgRate64_Type()
)
mpGtsFRCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRCfgRate64.setUnits("bits/second")
_MpGtsFRCfgBurstSize_Type = Unsigned32
_MpGtsFRCfgBurstSize_Object = MibTableColumn
mpGtsFRCfgBurstSize = _MpGtsFRCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 6),
    _MpGtsFRCfgBurstSize_Type()
)
mpGtsFRCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRCfgBurstSize.setUnits("bits")
_MpGtsFRCfgExtBurstSize_Type = Unsigned32
_MpGtsFRCfgExtBurstSize_Object = MibTableColumn
mpGtsFRCfgExtBurstSize = _MpGtsFRCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 7),
    _MpGtsFRCfgExtBurstSize_Type()
)
mpGtsFRCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRCfgExtBurstSize.setUnits("bits")
_MpGtsFRCfgQueueLimit_Type = Unsigned32
_MpGtsFRCfgQueueLimit_Object = MibTableColumn
mpGtsFRCfgQueueLimit = _MpGtsFRCfgQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 2, 1, 8),
    _MpGtsFRCfgQueueLimit_Type()
)
mpGtsFRCfgQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRCfgQueueLimit.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRCfgQueueLimit.setUnits("packets")
_MpGtsATMPVCCfgTable_Object = MibTable
mpGtsATMPVCCfgTable = _MpGtsATMPVCCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mpGtsATMPVCCfgTable.setStatus("current")
_MpGtsATMPVCCfgEntry_Object = MibTableRow
mpGtsATMPVCCfgEntry = _MpGtsATMPVCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1)
)
mpGtsATMPVCCfgEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgVPI"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgVCI"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsATMPVCCfgEntry.setStatus("current")


class _MpGtsATMCfgVPI_Type(Unsigned32):
    """Custom type mpGtsATMCfgVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpGtsATMCfgVPI_Type.__name__ = "Unsigned32"
_MpGtsATMCfgVPI_Object = MibTableColumn
mpGtsATMCfgVPI = _MpGtsATMCfgVPI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 1),
    _MpGtsATMCfgVPI_Type()
)
mpGtsATMCfgVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsATMCfgVPI.setStatus("current")


class _MpGtsATMCfgVCI_Type(Unsigned32):
    """Custom type mpGtsATMCfgVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpGtsATMCfgVCI_Type.__name__ = "Unsigned32"
_MpGtsATMCfgVCI_Object = MibTableColumn
mpGtsATMCfgVCI = _MpGtsATMCfgVCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 2),
    _MpGtsATMCfgVCI_Type()
)
mpGtsATMCfgVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsATMCfgVCI.setStatus("current")


class _MpGtsATMCfgRowIndex_Type(Integer32):
    """Custom type mpGtsATMCfgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpGtsATMCfgRowIndex_Type.__name__ = "Integer32"
_MpGtsATMCfgRowIndex_Object = MibTableColumn
mpGtsATMCfgRowIndex = _MpGtsATMCfgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 3),
    _MpGtsATMCfgRowIndex_Type()
)
mpGtsATMCfgRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpGtsATMCfgRowIndex.setStatus("current")


class _MpGtsATMCfgType_Type(Integer32):
    """Custom type mpGtsATMCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("accessList", 2))
    )


_MpGtsATMCfgType_Type.__name__ = "Integer32"
_MpGtsATMCfgType_Object = MibTableColumn
mpGtsATMCfgType = _MpGtsATMCfgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 4),
    _MpGtsATMCfgType_Type()
)
mpGtsATMCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgType.setStatus("current")


class _MpGtsATMCfgAclName_Type(DisplayString):
    """Custom type mpGtsATMCfgAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpGtsATMCfgAclName_Type.__name__ = "DisplayString"
_MpGtsATMCfgAclName_Object = MibTableColumn
mpGtsATMCfgAclName = _MpGtsATMCfgAclName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 5),
    _MpGtsATMCfgAclName_Type()
)
mpGtsATMCfgAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgAclName.setStatus("current")
_MpGtsATMCfgRate64_Type = Unsigned64
_MpGtsATMCfgRate64_Object = MibTableColumn
mpGtsATMCfgRate64 = _MpGtsATMCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 6),
    _MpGtsATMCfgRate64_Type()
)
mpGtsATMCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMCfgRate64.setUnits("bits/second")
_MpGtsATMCfgBurstSize_Type = Unsigned32
_MpGtsATMCfgBurstSize_Object = MibTableColumn
mpGtsATMCfgBurstSize = _MpGtsATMCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 7),
    _MpGtsATMCfgBurstSize_Type()
)
mpGtsATMCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMCfgBurstSize.setUnits("bits")
_MpGtsATMCfgExtBurstSize_Type = Unsigned32
_MpGtsATMCfgExtBurstSize_Object = MibTableColumn
mpGtsATMCfgExtBurstSize = _MpGtsATMCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 8),
    _MpGtsATMCfgExtBurstSize_Type()
)
mpGtsATMCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMCfgExtBurstSize.setUnits("bits")
_MpGtsATMCfgQueueLimit_Type = Unsigned32
_MpGtsATMCfgQueueLimit_Object = MibTableColumn
mpGtsATMCfgQueueLimit = _MpGtsATMCfgQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 1, 3, 1, 9),
    _MpGtsATMCfgQueueLimit_Type()
)
mpGtsATMCfgQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMCfgQueueLimit.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMCfgQueueLimit.setUnits("packets")
_MpGtsStats_ObjectIdentity = ObjectIdentity
mpGtsStats = _MpGtsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2)
)
_MpGtsInterfaceStatTable_Object = MibTable
mpGtsInterfaceStatTable = _MpGtsInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpGtsInterfaceStatTable.setStatus("current")
_MpGtsInterfaceStatEntry_Object = MibTableRow
mpGtsInterfaceStatEntry = _MpGtsInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1)
)
mpGtsInterfaceStatEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsIFCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsInterfaceStatEntry.setStatus("current")
_MpGtsIFStatSentByte64_Type = Counter64
_MpGtsIFStatSentByte64_Object = MibTableColumn
mpGtsIFStatSentByte64 = _MpGtsIFStatSentByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 1),
    _MpGtsIFStatSentByte64_Type()
)
mpGtsIFStatSentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatSentByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatSentByte64.setUnits("Octets")
_MpGtsIFStatSentPkt64_Type = Counter64
_MpGtsIFStatSentPkt64_Object = MibTableColumn
mpGtsIFStatSentPkt64 = _MpGtsIFStatSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 2),
    _MpGtsIFStatSentPkt64_Type()
)
mpGtsIFStatSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatSentPkt64.setUnits("Packets")
_MpGtsIFStatDelayedByte64_Type = Counter64
_MpGtsIFStatDelayedByte64_Object = MibTableColumn
mpGtsIFStatDelayedByte64 = _MpGtsIFStatDelayedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 3),
    _MpGtsIFStatDelayedByte64_Type()
)
mpGtsIFStatDelayedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatDelayedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatDelayedByte64.setUnits("Octets")
_MpGtsIFStatDelayedPkt64_Type = Counter64
_MpGtsIFStatDelayedPkt64_Object = MibTableColumn
mpGtsIFStatDelayedPkt64 = _MpGtsIFStatDelayedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 4),
    _MpGtsIFStatDelayedPkt64_Type()
)
mpGtsIFStatDelayedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatDelayedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatDelayedPkt64.setUnits("Packets")
_MpGtsIFStatDropByte64_Type = Counter64
_MpGtsIFStatDropByte64_Object = MibTableColumn
mpGtsIFStatDropByte64 = _MpGtsIFStatDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 5),
    _MpGtsIFStatDropByte64_Type()
)
mpGtsIFStatDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatDropByte64.setUnits("Octets")
_MpGtsIFStatDropPkt64_Type = Counter64
_MpGtsIFStatDropPkt64_Object = MibTableColumn
mpGtsIFStatDropPkt64 = _MpGtsIFStatDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 6),
    _MpGtsIFStatDropPkt64_Type()
)
mpGtsIFStatDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatDropPkt64.setUnits("Packets")
_MpGtsIFStatActive_Type = TruthValue
_MpGtsIFStatActive_Object = MibTableColumn
mpGtsIFStatActive = _MpGtsIFStatActive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 7),
    _MpGtsIFStatActive_Type()
)
mpGtsIFStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatActive.setStatus("current")
_MpGtsIFStatCurrentQSize_Type = Gauge32
_MpGtsIFStatCurrentQSize_Object = MibTableColumn
mpGtsIFStatCurrentQSize = _MpGtsIFStatCurrentQSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 1, 1, 8),
    _MpGtsIFStatCurrentQSize_Type()
)
mpGtsIFStatCurrentQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsIFStatCurrentQSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsIFStatCurrentQSize.setUnits("Packets")
_MpGtsFrameRelayVCStatTable_Object = MibTable
mpGtsFrameRelayVCStatTable = _MpGtsFrameRelayVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpGtsFrameRelayVCStatTable.setStatus("current")
_MpGtsFrameRelayVCStatEntry_Object = MibTableRow
mpGtsFrameRelayVCStatEntry = _MpGtsFrameRelayVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1)
)
mpGtsFrameRelayVCStatEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsFRCfgDLCI"),
    (0, "MAIPU-GTS-MIB", "mpGtsFRCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsFrameRelayVCStatEntry.setStatus("current")
_MpGtsFRStatSentByte64_Type = Counter64
_MpGtsFRStatSentByte64_Object = MibTableColumn
mpGtsFRStatSentByte64 = _MpGtsFRStatSentByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 1),
    _MpGtsFRStatSentByte64_Type()
)
mpGtsFRStatSentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatSentByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatSentByte64.setUnits("Octets")
_MpGtsFRStatSentPkt64_Type = Counter64
_MpGtsFRStatSentPkt64_Object = MibTableColumn
mpGtsFRStatSentPkt64 = _MpGtsFRStatSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 2),
    _MpGtsFRStatSentPkt64_Type()
)
mpGtsFRStatSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatSentPkt64.setUnits("Packets")
_MpGtsFRStatDelayedByte64_Type = Counter64
_MpGtsFRStatDelayedByte64_Object = MibTableColumn
mpGtsFRStatDelayedByte64 = _MpGtsFRStatDelayedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 3),
    _MpGtsFRStatDelayedByte64_Type()
)
mpGtsFRStatDelayedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatDelayedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatDelayedByte64.setUnits("Octets")
_MpGtsFRStatDelayedPkt64_Type = Counter64
_MpGtsFRStatDelayedPkt64_Object = MibTableColumn
mpGtsFRStatDelayedPkt64 = _MpGtsFRStatDelayedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 4),
    _MpGtsFRStatDelayedPkt64_Type()
)
mpGtsFRStatDelayedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatDelayedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatDelayedPkt64.setUnits("Packets")
_MpGtsFRStatDropByte64_Type = Counter64
_MpGtsFRStatDropByte64_Object = MibTableColumn
mpGtsFRStatDropByte64 = _MpGtsFRStatDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 5),
    _MpGtsFRStatDropByte64_Type()
)
mpGtsFRStatDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatDropByte64.setUnits("Octets")
_MpGtsFRStatDropPkt64_Type = Counter64
_MpGtsFRStatDropPkt64_Object = MibTableColumn
mpGtsFRStatDropPkt64 = _MpGtsFRStatDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 6),
    _MpGtsFRStatDropPkt64_Type()
)
mpGtsFRStatDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatDropPkt64.setUnits("Packets")
_MpGtsFRStatActive_Type = TruthValue
_MpGtsFRStatActive_Object = MibTableColumn
mpGtsFRStatActive = _MpGtsFRStatActive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 7),
    _MpGtsFRStatActive_Type()
)
mpGtsFRStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatActive.setStatus("current")
_MpGtsFRStatCurrentQSize_Type = Gauge32
_MpGtsFRStatCurrentQSize_Object = MibTableColumn
mpGtsFRStatCurrentQSize = _MpGtsFRStatCurrentQSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 2, 1, 8),
    _MpGtsFRStatCurrentQSize_Type()
)
mpGtsFRStatCurrentQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsFRStatCurrentQSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsFRStatCurrentQSize.setUnits("Packets")
_MpGtsATMPVCStatTable_Object = MibTable
mpGtsATMPVCStatTable = _MpGtsATMPVCStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpGtsATMPVCStatTable.setStatus("current")
_MpGtsATMPVCStatEntry_Object = MibTableRow
mpGtsATMPVCStatEntry = _MpGtsATMPVCStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1)
)
mpGtsATMPVCStatEntry.setIndexNames(
    (0, "MAIPU-GTS-MIB", "ifIndex"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgVPI"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgVCI"),
    (0, "MAIPU-GTS-MIB", "mpGtsATMCfgRowIndex"),
)
if mibBuilder.loadTexts:
    mpGtsATMPVCStatEntry.setStatus("current")
_MpGtsATMStatSentByte64_Type = Counter64
_MpGtsATMStatSentByte64_Object = MibTableColumn
mpGtsATMStatSentByte64 = _MpGtsATMStatSentByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 1),
    _MpGtsATMStatSentByte64_Type()
)
mpGtsATMStatSentByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatSentByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatSentByte64.setUnits("Octets")
_MpGtsATMStatSentPkt64_Type = Counter64
_MpGtsATMStatSentPkt64_Object = MibTableColumn
mpGtsATMStatSentPkt64 = _MpGtsATMStatSentPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 2),
    _MpGtsATMStatSentPkt64_Type()
)
mpGtsATMStatSentPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatSentPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatSentPkt64.setUnits("Packets")
_MpGtsATMStatDelayedByte64_Type = Counter64
_MpGtsATMStatDelayedByte64_Object = MibTableColumn
mpGtsATMStatDelayedByte64 = _MpGtsATMStatDelayedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 3),
    _MpGtsATMStatDelayedByte64_Type()
)
mpGtsATMStatDelayedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatDelayedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatDelayedByte64.setUnits("Octets")
_MpGtsATMStatDelayedPkt64_Type = Counter64
_MpGtsATMStatDelayedPkt64_Object = MibTableColumn
mpGtsATMStatDelayedPkt64 = _MpGtsATMStatDelayedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 4),
    _MpGtsATMStatDelayedPkt64_Type()
)
mpGtsATMStatDelayedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatDelayedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatDelayedPkt64.setUnits("Packets")
_MpGtsATMStatDropByte64_Type = Counter64
_MpGtsATMStatDropByte64_Object = MibTableColumn
mpGtsATMStatDropByte64 = _MpGtsATMStatDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 5),
    _MpGtsATMStatDropByte64_Type()
)
mpGtsATMStatDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatDropByte64.setUnits("Octets")
_MpGtsATMStatDropPkt64_Type = Counter64
_MpGtsATMStatDropPkt64_Object = MibTableColumn
mpGtsATMStatDropPkt64 = _MpGtsATMStatDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 6),
    _MpGtsATMStatDropPkt64_Type()
)
mpGtsATMStatDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatDropPkt64.setUnits("Packets")
_MpGtsATMStatActive_Type = TruthValue
_MpGtsATMStatActive_Object = MibTableColumn
mpGtsATMStatActive = _MpGtsATMStatActive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 7),
    _MpGtsATMStatActive_Type()
)
mpGtsATMStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatActive.setStatus("current")
_MpGtsATMStatCurrentQSize_Type = Gauge32
_MpGtsATMStatCurrentQSize_Object = MibTableColumn
mpGtsATMStatCurrentQSize = _MpGtsATMStatCurrentQSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 5, 1, 2, 3, 1, 8),
    _MpGtsATMStatCurrentQSize_Type()
)
mpGtsATMStatCurrentQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpGtsATMStatCurrentQSize.setStatus("current")
if mibBuilder.loadTexts:
    mpGtsATMStatCurrentQSize.setUnits("Packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-GTS-MIB",
    **{"Unsigned64": Unsigned64,
       "maipu": maipu,
       "mpMgmt2": mpMgmt2,
       "mpRouterTech": mpRouterTech,
       "mpRtQoSv2": mpRtQoSv2,
       "maipuGtsMIB": maipuGtsMIB,
       "maipuGtsMIBObjects": maipuGtsMIBObjects,
       "mpGtsConfigs": mpGtsConfigs,
       "mpGtsInterfaceCfgTable": mpGtsInterfaceCfgTable,
       "mpGtsInterfaceCfgEntry": mpGtsInterfaceCfgEntry,
       "mpGtsIFCfgRowIndex": mpGtsIFCfgRowIndex,
       "mpGtsIFCfgType": mpGtsIFCfgType,
       "mpGtsIFCfgAclName": mpGtsIFCfgAclName,
       "mpGtsIFCfgRate64": mpGtsIFCfgRate64,
       "mpGtsIFCfgBurstSize": mpGtsIFCfgBurstSize,
       "mpGtsIFCfgExtBurstSize": mpGtsIFCfgExtBurstSize,
       "mpGtsIFCfgQueueLimit": mpGtsIFCfgQueueLimit,
       "mpGtsFrameRelayVCCfgTable": mpGtsFrameRelayVCCfgTable,
       "mpGtsFrameRelayVCCfgEntry": mpGtsFrameRelayVCCfgEntry,
       "mpGtsFRCfgDLCI": mpGtsFRCfgDLCI,
       "mpGtsFRCfgRowIndex": mpGtsFRCfgRowIndex,
       "mpGtsFRCfgType": mpGtsFRCfgType,
       "mpGtsFRCfgAclName": mpGtsFRCfgAclName,
       "mpGtsFRCfgRate64": mpGtsFRCfgRate64,
       "mpGtsFRCfgBurstSize": mpGtsFRCfgBurstSize,
       "mpGtsFRCfgExtBurstSize": mpGtsFRCfgExtBurstSize,
       "mpGtsFRCfgQueueLimit": mpGtsFRCfgQueueLimit,
       "mpGtsATMPVCCfgTable": mpGtsATMPVCCfgTable,
       "mpGtsATMPVCCfgEntry": mpGtsATMPVCCfgEntry,
       "mpGtsATMCfgVPI": mpGtsATMCfgVPI,
       "mpGtsATMCfgVCI": mpGtsATMCfgVCI,
       "mpGtsATMCfgRowIndex": mpGtsATMCfgRowIndex,
       "mpGtsATMCfgType": mpGtsATMCfgType,
       "mpGtsATMCfgAclName": mpGtsATMCfgAclName,
       "mpGtsATMCfgRate64": mpGtsATMCfgRate64,
       "mpGtsATMCfgBurstSize": mpGtsATMCfgBurstSize,
       "mpGtsATMCfgExtBurstSize": mpGtsATMCfgExtBurstSize,
       "mpGtsATMCfgQueueLimit": mpGtsATMCfgQueueLimit,
       "mpGtsStats": mpGtsStats,
       "mpGtsInterfaceStatTable": mpGtsInterfaceStatTable,
       "mpGtsInterfaceStatEntry": mpGtsInterfaceStatEntry,
       "mpGtsIFStatSentByte64": mpGtsIFStatSentByte64,
       "mpGtsIFStatSentPkt64": mpGtsIFStatSentPkt64,
       "mpGtsIFStatDelayedByte64": mpGtsIFStatDelayedByte64,
       "mpGtsIFStatDelayedPkt64": mpGtsIFStatDelayedPkt64,
       "mpGtsIFStatDropByte64": mpGtsIFStatDropByte64,
       "mpGtsIFStatDropPkt64": mpGtsIFStatDropPkt64,
       "mpGtsIFStatActive": mpGtsIFStatActive,
       "mpGtsIFStatCurrentQSize": mpGtsIFStatCurrentQSize,
       "mpGtsFrameRelayVCStatTable": mpGtsFrameRelayVCStatTable,
       "mpGtsFrameRelayVCStatEntry": mpGtsFrameRelayVCStatEntry,
       "mpGtsFRStatSentByte64": mpGtsFRStatSentByte64,
       "mpGtsFRStatSentPkt64": mpGtsFRStatSentPkt64,
       "mpGtsFRStatDelayedByte64": mpGtsFRStatDelayedByte64,
       "mpGtsFRStatDelayedPkt64": mpGtsFRStatDelayedPkt64,
       "mpGtsFRStatDropByte64": mpGtsFRStatDropByte64,
       "mpGtsFRStatDropPkt64": mpGtsFRStatDropPkt64,
       "mpGtsFRStatActive": mpGtsFRStatActive,
       "mpGtsFRStatCurrentQSize": mpGtsFRStatCurrentQSize,
       "mpGtsATMPVCStatTable": mpGtsATMPVCStatTable,
       "mpGtsATMPVCStatEntry": mpGtsATMPVCStatEntry,
       "mpGtsATMStatSentByte64": mpGtsATMStatSentByte64,
       "mpGtsATMStatSentPkt64": mpGtsATMStatSentPkt64,
       "mpGtsATMStatDelayedByte64": mpGtsATMStatDelayedByte64,
       "mpGtsATMStatDelayedPkt64": mpGtsATMStatDelayedPkt64,
       "mpGtsATMStatDropByte64": mpGtsATMStatDropByte64,
       "mpGtsATMStatDropPkt64": mpGtsATMStatDropPkt64,
       "mpGtsATMStatActive": mpGtsATMStatActive,
       "mpGtsATMStatCurrentQSize": mpGtsATMStatCurrentQSize}
)
