# SNMP MIB module (HPNSATRAPMNGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPNSATRAPMNGR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:09 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaTrapMgr_ObjectIdentity = ObjectIdentity
hpnsaTrapMgr = _HpnsaTrapMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23)
)
_HpnsaTrapMgrRev_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrRev = _HpnsaTrapMgrRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 1)
)


class _HpnsaTrapMgrMibRevMajor_Type(Integer32):
    """Custom type hpnsaTrapMgrMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaTrapMgrMibRevMajor_Type.__name__ = "Integer32"
_HpnsaTrapMgrMibRevMajor_Object = MibScalar
hpnsaTrapMgrMibRevMajor = _HpnsaTrapMgrMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 1, 1),
    _HpnsaTrapMgrMibRevMajor_Type()
)
hpnsaTrapMgrMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrMibRevMajor.setStatus("mandatory")


class _HpnsaTrapMgrMibRevMinor_Type(Integer32):
    """Custom type hpnsaTrapMgrMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaTrapMgrMibRevMinor_Type.__name__ = "Integer32"
_HpnsaTrapMgrMibRevMinor_Object = MibScalar
hpnsaTrapMgrMibRevMinor = _HpnsaTrapMgrMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 1, 2),
    _HpnsaTrapMgrMibRevMinor_Type()
)
hpnsaTrapMgrMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrMibRevMinor.setStatus("mandatory")
_HpnsaTrapMgrAgentInfo_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrAgentInfo = _HpnsaTrapMgrAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2)
)
_HpnsaTrapMgrAgentTable_Object = MibTable
hpnsaTrapMgrAgentTable = _HpnsaTrapMgrAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentTable.setStatus("mandatory")
_HpnsaTrapMgrAgentEntry_Object = MibTableRow
hpnsaTrapMgrAgentEntry = _HpnsaTrapMgrAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1, 1)
)
hpnsaTrapMgrAgentEntry.setIndexNames(
    (0, "HPNSATRAPMNGR-MIB", "hpnsaTrapMgrAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentEntry.setStatus("mandatory")


class _HpnsaTrapMgrAgentIndex_Type(Integer32):
    """Custom type hpnsaTrapMgrAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaTrapMgrAgentIndex_Type.__name__ = "Integer32"
_HpnsaTrapMgrAgentIndex_Object = MibTableColumn
hpnsaTrapMgrAgentIndex = _HpnsaTrapMgrAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1, 1, 1),
    _HpnsaTrapMgrAgentIndex_Type()
)
hpnsaTrapMgrAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentIndex.setStatus("mandatory")


class _HpnsaTrapMgrAgentName_Type(DisplayString):
    """Custom type hpnsaTrapMgrAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaTrapMgrAgentName_Type.__name__ = "DisplayString"
_HpnsaTrapMgrAgentName_Object = MibTableColumn
hpnsaTrapMgrAgentName = _HpnsaTrapMgrAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1, 1, 2),
    _HpnsaTrapMgrAgentName_Type()
)
hpnsaTrapMgrAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentName.setStatus("mandatory")


class _HpnsaTrapMgrAgentVersion_Type(DisplayString):
    """Custom type hpnsaTrapMgrAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaTrapMgrAgentVersion_Type.__name__ = "DisplayString"
_HpnsaTrapMgrAgentVersion_Object = MibTableColumn
hpnsaTrapMgrAgentVersion = _HpnsaTrapMgrAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1, 1, 3),
    _HpnsaTrapMgrAgentVersion_Type()
)
hpnsaTrapMgrAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentVersion.setStatus("mandatory")


class _HpnsaTrapMgrAgentDate_Type(OctetString):
    """Custom type hpnsaTrapMgrAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_HpnsaTrapMgrAgentDate_Type.__name__ = "OctetString"
_HpnsaTrapMgrAgentDate_Object = MibTableColumn
hpnsaTrapMgrAgentDate = _HpnsaTrapMgrAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 2, 1, 1, 4),
    _HpnsaTrapMgrAgentDate_Type()
)
hpnsaTrapMgrAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrAgentDate.setStatus("mandatory")
_HpnsaTrapMgrStats_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrStats = _HpnsaTrapMgrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 3)
)


class _HpnsaTrapMgrNumActive_Type(Integer32):
    """Custom type hpnsaTrapMgrNumActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaTrapMgrNumActive_Type.__name__ = "Integer32"
_HpnsaTrapMgrNumActive_Object = MibScalar
hpnsaTrapMgrNumActive = _HpnsaTrapMgrNumActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 3, 1),
    _HpnsaTrapMgrNumActive_Type()
)
hpnsaTrapMgrNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrNumActive.setStatus("mandatory")


class _HpnsaTrapMgrNumHistory_Type(Integer32):
    """Custom type hpnsaTrapMgrNumHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaTrapMgrNumHistory_Type.__name__ = "Integer32"
_HpnsaTrapMgrNumHistory_Object = MibScalar
hpnsaTrapMgrNumHistory = _HpnsaTrapMgrNumHistory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 3, 2),
    _HpnsaTrapMgrNumHistory_Type()
)
hpnsaTrapMgrNumHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrNumHistory.setStatus("mandatory")


class _HpnsaTrapMgrMaxHistory_Type(Integer32):
    """Custom type hpnsaTrapMgrMaxHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaTrapMgrMaxHistory_Type.__name__ = "Integer32"
_HpnsaTrapMgrMaxHistory_Object = MibScalar
hpnsaTrapMgrMaxHistory = _HpnsaTrapMgrMaxHistory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 3, 3),
    _HpnsaTrapMgrMaxHistory_Type()
)
hpnsaTrapMgrMaxHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrMaxHistory.setStatus("mandatory")


class _HpnsaTrapMgrEraseTraps_Type(Integer32):
    """Custom type hpnsaTrapMgrEraseTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1234
        )
    )
    namedValues = NamedValues(
        ("eraseLogNow", 1234)
    )


_HpnsaTrapMgrEraseTraps_Type.__name__ = "Integer32"
_HpnsaTrapMgrEraseTraps_Object = MibScalar
hpnsaTrapMgrEraseTraps = _HpnsaTrapMgrEraseTraps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 3, 4),
    _HpnsaTrapMgrEraseTraps_Type()
)
hpnsaTrapMgrEraseTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaTrapMgrEraseTraps.setStatus("mandatory")
_HpnsaTrapMgrActive_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrActive = _HpnsaTrapMgrActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4)
)
_HpnsaTrapMgrActiveTable_Object = MibTable
hpnsaTrapMgrActiveTable = _HpnsaTrapMgrActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveTable.setStatus("mandatory")
_HpnsaTrapMgrActiveTableEntry_Object = MibTableRow
hpnsaTrapMgrActiveTableEntry = _HpnsaTrapMgrActiveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1)
)
hpnsaTrapMgrActiveTableEntry.setIndexNames(
    (0, "HPNSATRAPMNGR-MIB", "hpnsaTrapMgrActiveTrapHandleIndex"),
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveTableEntry.setStatus("mandatory")


class _HpnsaTrapMgrActiveTrapHandleIndex_Type(Integer32):
    """Custom type hpnsaTrapMgrActiveTrapHandleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnsaTrapMgrActiveTrapHandleIndex_Type.__name__ = "Integer32"
_HpnsaTrapMgrActiveTrapHandleIndex_Object = MibTableColumn
hpnsaTrapMgrActiveTrapHandleIndex = _HpnsaTrapMgrActiveTrapHandleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 1),
    _HpnsaTrapMgrActiveTrapHandleIndex_Type()
)
hpnsaTrapMgrActiveTrapHandleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveTrapHandleIndex.setStatus("mandatory")


class _HpnsaTrapMgrActiveTrapID_Type(DisplayString):
    """Custom type hpnsaTrapMgrActiveTrapID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaTrapMgrActiveTrapID_Type.__name__ = "DisplayString"
_HpnsaTrapMgrActiveTrapID_Object = MibTableColumn
hpnsaTrapMgrActiveTrapID = _HpnsaTrapMgrActiveTrapID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 2),
    _HpnsaTrapMgrActiveTrapID_Type()
)
hpnsaTrapMgrActiveTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveTrapID.setStatus("mandatory")
_HpnsaTrapMgrActiveTimeStamp_Type = Integer32
_HpnsaTrapMgrActiveTimeStamp_Object = MibTableColumn
hpnsaTrapMgrActiveTimeStamp = _HpnsaTrapMgrActiveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 3),
    _HpnsaTrapMgrActiveTimeStamp_Type()
)
hpnsaTrapMgrActiveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveTimeStamp.setStatus("mandatory")


class _HpnsaTrapMgrActiveSeverity_Type(Integer32):
    """Custom type hpnsaTrapMgrActiveSeverity based on Integer32"""
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
        *(("Unknown", 1),
          ("Informational", 2),
          ("Normal", 3),
          ("Warning", 4),
          ("Critical", 5))
    )


_HpnsaTrapMgrActiveSeverity_Type.__name__ = "Integer32"
_HpnsaTrapMgrActiveSeverity_Object = MibTableColumn
hpnsaTrapMgrActiveSeverity = _HpnsaTrapMgrActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 4),
    _HpnsaTrapMgrActiveSeverity_Type()
)
hpnsaTrapMgrActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveSeverity.setStatus("mandatory")


class _HpnsaTrapMgrActiveCustomString_Type(DisplayString):
    """Custom type hpnsaTrapMgrActiveCustomString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnsaTrapMgrActiveCustomString_Type.__name__ = "DisplayString"
_HpnsaTrapMgrActiveCustomString_Object = MibTableColumn
hpnsaTrapMgrActiveCustomString = _HpnsaTrapMgrActiveCustomString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 5),
    _HpnsaTrapMgrActiveCustomString_Type()
)
hpnsaTrapMgrActiveCustomString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveCustomString.setStatus("mandatory")


class _HpnsaTrapMgrActiveEnterpriseID_Type(DisplayString):
    """Custom type hpnsaTrapMgrActiveEnterpriseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaTrapMgrActiveEnterpriseID_Type.__name__ = "DisplayString"
_HpnsaTrapMgrActiveEnterpriseID_Object = MibTableColumn
hpnsaTrapMgrActiveEnterpriseID = _HpnsaTrapMgrActiveEnterpriseID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 6),
    _HpnsaTrapMgrActiveEnterpriseID_Type()
)
hpnsaTrapMgrActiveEnterpriseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveEnterpriseID.setStatus("mandatory")


class _HpnsaTrapMgrActiveSpecificID_Type(Integer32):
    """Custom type hpnsaTrapMgrActiveSpecificID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaTrapMgrActiveSpecificID_Type.__name__ = "Integer32"
_HpnsaTrapMgrActiveSpecificID_Object = MibTableColumn
hpnsaTrapMgrActiveSpecificID = _HpnsaTrapMgrActiveSpecificID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 4, 1, 1, 7),
    _HpnsaTrapMgrActiveSpecificID_Type()
)
hpnsaTrapMgrActiveSpecificID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrActiveSpecificID.setStatus("mandatory")
_HpnsaTrapMgrAck_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrAck = _HpnsaTrapMgrAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 5)
)


class _HpnsaTrapMgrTrapHandleAck_Type(Integer32):
    """Custom type hpnsaTrapMgrTrapHandleAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnsaTrapMgrTrapHandleAck_Type.__name__ = "Integer32"
_HpnsaTrapMgrTrapHandleAck_Object = MibScalar
hpnsaTrapMgrTrapHandleAck = _HpnsaTrapMgrTrapHandleAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 5, 1),
    _HpnsaTrapMgrTrapHandleAck_Type()
)
hpnsaTrapMgrTrapHandleAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaTrapMgrTrapHandleAck.setStatus("mandatory")
_HpnsaTrapMgrHist_ObjectIdentity = ObjectIdentity
hpnsaTrapMgrHist = _HpnsaTrapMgrHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6)
)
_HpnsaTrapMgrHistTable_Object = MibTable
hpnsaTrapMgrHistTable = _HpnsaTrapMgrHistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1)
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistTable.setStatus("mandatory")
_HpnsaTrapMgrHistTableEntry_Object = MibTableRow
hpnsaTrapMgrHistTableEntry = _HpnsaTrapMgrHistTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1)
)
hpnsaTrapMgrHistTableEntry.setIndexNames(
    (0, "HPNSATRAPMNGR-MIB", "hpnsaTrapMgrHistTrapHandleIndex"),
)
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistTableEntry.setStatus("mandatory")


class _HpnsaTrapMgrHistTrapHandleIndex_Type(Integer32):
    """Custom type hpnsaTrapMgrHistTrapHandleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnsaTrapMgrHistTrapHandleIndex_Type.__name__ = "Integer32"
_HpnsaTrapMgrHistTrapHandleIndex_Object = MibTableColumn
hpnsaTrapMgrHistTrapHandleIndex = _HpnsaTrapMgrHistTrapHandleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 1),
    _HpnsaTrapMgrHistTrapHandleIndex_Type()
)
hpnsaTrapMgrHistTrapHandleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistTrapHandleIndex.setStatus("mandatory")


class _HpnsaTrapMgrHistTrapID_Type(DisplayString):
    """Custom type hpnsaTrapMgrHistTrapID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaTrapMgrHistTrapID_Type.__name__ = "DisplayString"
_HpnsaTrapMgrHistTrapID_Object = MibTableColumn
hpnsaTrapMgrHistTrapID = _HpnsaTrapMgrHistTrapID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 2),
    _HpnsaTrapMgrHistTrapID_Type()
)
hpnsaTrapMgrHistTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistTrapID.setStatus("mandatory")
_HpnsaTrapMgrHistTimeStamp_Type = Integer32
_HpnsaTrapMgrHistTimeStamp_Object = MibTableColumn
hpnsaTrapMgrHistTimeStamp = _HpnsaTrapMgrHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 3),
    _HpnsaTrapMgrHistTimeStamp_Type()
)
hpnsaTrapMgrHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistTimeStamp.setStatus("mandatory")


class _HpnsaTrapMgrHistSeverity_Type(Integer32):
    """Custom type hpnsaTrapMgrHistSeverity based on Integer32"""
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
        *(("Unknown", 1),
          ("Informational", 2),
          ("Normal", 3),
          ("Warning", 4),
          ("Critical", 5))
    )


_HpnsaTrapMgrHistSeverity_Type.__name__ = "Integer32"
_HpnsaTrapMgrHistSeverity_Object = MibTableColumn
hpnsaTrapMgrHistSeverity = _HpnsaTrapMgrHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 4),
    _HpnsaTrapMgrHistSeverity_Type()
)
hpnsaTrapMgrHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistSeverity.setStatus("mandatory")


class _HpnsaTrapMgrHistCustomString_Type(DisplayString):
    """Custom type hpnsaTrapMgrHistCustomString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnsaTrapMgrHistCustomString_Type.__name__ = "DisplayString"
_HpnsaTrapMgrHistCustomString_Object = MibTableColumn
hpnsaTrapMgrHistCustomString = _HpnsaTrapMgrHistCustomString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 5),
    _HpnsaTrapMgrHistCustomString_Type()
)
hpnsaTrapMgrHistCustomString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistCustomString.setStatus("mandatory")


class _HpnsaTrapMgrHistEnterpriseID_Type(DisplayString):
    """Custom type hpnsaTrapMgrHistEnterpriseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnsaTrapMgrHistEnterpriseID_Type.__name__ = "DisplayString"
_HpnsaTrapMgrHistEnterpriseID_Object = MibTableColumn
hpnsaTrapMgrHistEnterpriseID = _HpnsaTrapMgrHistEnterpriseID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 6),
    _HpnsaTrapMgrHistEnterpriseID_Type()
)
hpnsaTrapMgrHistEnterpriseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistEnterpriseID.setStatus("mandatory")


class _HpnsaTrapMgrHistSpecificID_Type(Integer32):
    """Custom type hpnsaTrapMgrHistSpecificID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaTrapMgrHistSpecificID_Type.__name__ = "Integer32"
_HpnsaTrapMgrHistSpecificID_Object = MibTableColumn
hpnsaTrapMgrHistSpecificID = _HpnsaTrapMgrHistSpecificID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 7),
    _HpnsaTrapMgrHistSpecificID_Type()
)
hpnsaTrapMgrHistSpecificID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistSpecificID.setStatus("mandatory")


class _HpnsaTrapMgrHistAck_Type(Integer32):
    """Custom type hpnsaTrapMgrHistAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ACTIVE", 0),
          ("ACKNOWLEDGED", 1))
    )


_HpnsaTrapMgrHistAck_Type.__name__ = "Integer32"
_HpnsaTrapMgrHistAck_Object = MibTableColumn
hpnsaTrapMgrHistAck = _HpnsaTrapMgrHistAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 23, 6, 1, 1, 8),
    _HpnsaTrapMgrHistAck_Type()
)
hpnsaTrapMgrHistAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaTrapMgrHistAck.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSATRAPMNGR-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaTrapMgr": hpnsaTrapMgr,
       "hpnsaTrapMgrRev": hpnsaTrapMgrRev,
       "hpnsaTrapMgrMibRevMajor": hpnsaTrapMgrMibRevMajor,
       "hpnsaTrapMgrMibRevMinor": hpnsaTrapMgrMibRevMinor,
       "hpnsaTrapMgrAgentInfo": hpnsaTrapMgrAgentInfo,
       "hpnsaTrapMgrAgentTable": hpnsaTrapMgrAgentTable,
       "hpnsaTrapMgrAgentEntry": hpnsaTrapMgrAgentEntry,
       "hpnsaTrapMgrAgentIndex": hpnsaTrapMgrAgentIndex,
       "hpnsaTrapMgrAgentName": hpnsaTrapMgrAgentName,
       "hpnsaTrapMgrAgentVersion": hpnsaTrapMgrAgentVersion,
       "hpnsaTrapMgrAgentDate": hpnsaTrapMgrAgentDate,
       "hpnsaTrapMgrStats": hpnsaTrapMgrStats,
       "hpnsaTrapMgrNumActive": hpnsaTrapMgrNumActive,
       "hpnsaTrapMgrNumHistory": hpnsaTrapMgrNumHistory,
       "hpnsaTrapMgrMaxHistory": hpnsaTrapMgrMaxHistory,
       "hpnsaTrapMgrEraseTraps": hpnsaTrapMgrEraseTraps,
       "hpnsaTrapMgrActive": hpnsaTrapMgrActive,
       "hpnsaTrapMgrActiveTable": hpnsaTrapMgrActiveTable,
       "hpnsaTrapMgrActiveTableEntry": hpnsaTrapMgrActiveTableEntry,
       "hpnsaTrapMgrActiveTrapHandleIndex": hpnsaTrapMgrActiveTrapHandleIndex,
       "hpnsaTrapMgrActiveTrapID": hpnsaTrapMgrActiveTrapID,
       "hpnsaTrapMgrActiveTimeStamp": hpnsaTrapMgrActiveTimeStamp,
       "hpnsaTrapMgrActiveSeverity": hpnsaTrapMgrActiveSeverity,
       "hpnsaTrapMgrActiveCustomString": hpnsaTrapMgrActiveCustomString,
       "hpnsaTrapMgrActiveEnterpriseID": hpnsaTrapMgrActiveEnterpriseID,
       "hpnsaTrapMgrActiveSpecificID": hpnsaTrapMgrActiveSpecificID,
       "hpnsaTrapMgrAck": hpnsaTrapMgrAck,
       "hpnsaTrapMgrTrapHandleAck": hpnsaTrapMgrTrapHandleAck,
       "hpnsaTrapMgrHist": hpnsaTrapMgrHist,
       "hpnsaTrapMgrHistTable": hpnsaTrapMgrHistTable,
       "hpnsaTrapMgrHistTableEntry": hpnsaTrapMgrHistTableEntry,
       "hpnsaTrapMgrHistTrapHandleIndex": hpnsaTrapMgrHistTrapHandleIndex,
       "hpnsaTrapMgrHistTrapID": hpnsaTrapMgrHistTrapID,
       "hpnsaTrapMgrHistTimeStamp": hpnsaTrapMgrHistTimeStamp,
       "hpnsaTrapMgrHistSeverity": hpnsaTrapMgrHistSeverity,
       "hpnsaTrapMgrHistCustomString": hpnsaTrapMgrHistCustomString,
       "hpnsaTrapMgrHistEnterpriseID": hpnsaTrapMgrHistEnterpriseID,
       "hpnsaTrapMgrHistSpecificID": hpnsaTrapMgrHistSpecificID,
       "hpnsaTrapMgrHistAck": hpnsaTrapMgrHistAck}
)
