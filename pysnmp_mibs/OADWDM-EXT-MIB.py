# SNMP MIB module (OADWDM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OADWDM-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:21 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oaLambdaDriver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41)
)
if mibBuilder.loadTexts:
    oaLambdaDriver.setRevisions(
        ("2009-06-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaLdPortsCntr_ObjectIdentity = ObjectIdentity
oaLdPortsCntr = _OaLdPortsCntr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10)
)
_OaLdPortsCntrTable_Object = MibTable
oaLdPortsCntrTable = _OaLdPortsCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2)
)
if mibBuilder.loadTexts:
    oaLdPortsCntrTable.setStatus("current")
_OaLdPortsCntrEntry_Object = MibTableRow
oaLdPortsCntrEntry = _OaLdPortsCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1)
)
oaLdPortsCntrEntry.setIndexNames(
    (0, "OADWDM-EXT-MIB", "oaLdPortsCntrSlotNumber"),
    (0, "OADWDM-EXT-MIB", "oaLdPortsCntrPortNumber"),
)
if mibBuilder.loadTexts:
    oaLdPortsCntrEntry.setStatus("current")


class _OaLdPortsCntrSlotNumber_Type(Integer32):
    """Custom type oaLdPortsCntrSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_OaLdPortsCntrSlotNumber_Type.__name__ = "Integer32"
_OaLdPortsCntrSlotNumber_Object = MibTableColumn
oaLdPortsCntrSlotNumber = _OaLdPortsCntrSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 1),
    _OaLdPortsCntrSlotNumber_Type()
)
oaLdPortsCntrSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaLdPortsCntrSlotNumber.setStatus("current")


class _OaLdPortsCntrPortNumber_Type(Integer32):
    """Custom type oaLdPortsCntrPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_OaLdPortsCntrPortNumber_Type.__name__ = "Integer32"
_OaLdPortsCntrPortNumber_Object = MibTableColumn
oaLdPortsCntrPortNumber = _OaLdPortsCntrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 2),
    _OaLdPortsCntrPortNumber_Type()
)
oaLdPortsCntrPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaLdPortsCntrPortNumber.setStatus("current")
_OaLdPortsCntrSyncErrs_Type = Counter32
_OaLdPortsCntrSyncErrs_Object = MibTableColumn
oaLdPortsCntrSyncErrs = _OaLdPortsCntrSyncErrs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 3),
    _OaLdPortsCntrSyncErrs_Type()
)
oaLdPortsCntrSyncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrSyncErrs.setStatus("current")
_OaLdPortsCntrCrcErrs_Type = Counter32
_OaLdPortsCntrCrcErrs_Object = MibTableColumn
oaLdPortsCntrCrcErrs = _OaLdPortsCntrCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 4),
    _OaLdPortsCntrCrcErrs_Type()
)
oaLdPortsCntrCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrCrcErrs.setStatus("current")
_OaLdPortsCntrInRateBits_Type = Integer32
_OaLdPortsCntrInRateBits_Object = MibTableColumn
oaLdPortsCntrInRateBits = _OaLdPortsCntrInRateBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 5),
    _OaLdPortsCntrInRateBits_Type()
)
oaLdPortsCntrInRateBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrInRateBits.setStatus("current")
_OaLdPortsCntrOutRateBits_Type = Integer32
_OaLdPortsCntrOutRateBits_Object = MibTableColumn
oaLdPortsCntrOutRateBits = _OaLdPortsCntrOutRateBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 6),
    _OaLdPortsCntrOutRateBits_Type()
)
oaLdPortsCntrOutRateBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrOutRateBits.setStatus("current")
_OaLdPortsCntrCodeViols_Type = Counter32
_OaLdPortsCntrCodeViols_Object = MibTableColumn
oaLdPortsCntrCodeViols = _OaLdPortsCntrCodeViols_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 7),
    _OaLdPortsCntrCodeViols_Type()
)
oaLdPortsCntrCodeViols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrCodeViols.setStatus("current")
_OaLdPortsCntrInPkts_Type = Counter64
_OaLdPortsCntrInPkts_Object = MibTableColumn
oaLdPortsCntrInPkts = _OaLdPortsCntrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 8),
    _OaLdPortsCntrInPkts_Type()
)
oaLdPortsCntrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrInPkts.setStatus("current")
_OaLdPortsCntrOutPkts_Type = Counter64
_OaLdPortsCntrOutPkts_Object = MibTableColumn
oaLdPortsCntrOutPkts = _OaLdPortsCntrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 9),
    _OaLdPortsCntrOutPkts_Type()
)
oaLdPortsCntrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrOutPkts.setStatus("current")
_OaLdPortsCntrInOctets_Type = Counter64
_OaLdPortsCntrInOctets_Object = MibTableColumn
oaLdPortsCntrInOctets = _OaLdPortsCntrInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 10),
    _OaLdPortsCntrInOctets_Type()
)
oaLdPortsCntrInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrInOctets.setStatus("current")
_OaLdPortsCntrOutOctets_Type = Counter64
_OaLdPortsCntrOutOctets_Object = MibTableColumn
oaLdPortsCntrOutOctets = _OaLdPortsCntrOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 10, 2, 1, 11),
    _OaLdPortsCntrOutOctets_Type()
)
oaLdPortsCntrOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaLdPortsCntrOutOctets.setStatus("current")
_OaLdPortsCntrConformance_ObjectIdentity = ObjectIdentity
oaLdPortsCntrConformance = _OaLdPortsCntrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 100)
)
_OaLdPortsCntrGroups_ObjectIdentity = ObjectIdentity
oaLdPortsCntrGroups = _OaLdPortsCntrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 100, 1)
)
_OaLdPortsCntrCompliances_ObjectIdentity = ObjectIdentity
oaLdPortsCntrCompliances = _OaLdPortsCntrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 100, 2)
)

# Managed Objects groups

oaLdPortsCntrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 100, 1, 1)
)
oaLdPortsCntrGroup.setObjects(
      *(("OADWDM-EXT-MIB", "oaLdPortsCntrSyncErrs"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrCrcErrs"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrInRateBits"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrOutRateBits"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrCodeViols"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrInPkts"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrOutPkts"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrInOctets"),
        ("OADWDM-EXT-MIB", "oaLdPortsCntrOutOctets"))
)
if mibBuilder.loadTexts:
    oaLdPortsCntrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaLdPortsCntrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 41, 100, 2, 1)
)
oaLdPortsCntrCompliance.setObjects(
    ("OADWDM-EXT-MIB", "oaLdPortsCntrGroup")
)
if mibBuilder.loadTexts:
    oaLdPortsCntrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OADWDM-EXT-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaLambdaDriver": oaLambdaDriver,
       "oaLdPortsCntr": oaLdPortsCntr,
       "oaLdPortsCntrTable": oaLdPortsCntrTable,
       "oaLdPortsCntrEntry": oaLdPortsCntrEntry,
       "oaLdPortsCntrSlotNumber": oaLdPortsCntrSlotNumber,
       "oaLdPortsCntrPortNumber": oaLdPortsCntrPortNumber,
       "oaLdPortsCntrSyncErrs": oaLdPortsCntrSyncErrs,
       "oaLdPortsCntrCrcErrs": oaLdPortsCntrCrcErrs,
       "oaLdPortsCntrInRateBits": oaLdPortsCntrInRateBits,
       "oaLdPortsCntrOutRateBits": oaLdPortsCntrOutRateBits,
       "oaLdPortsCntrCodeViols": oaLdPortsCntrCodeViols,
       "oaLdPortsCntrInPkts": oaLdPortsCntrInPkts,
       "oaLdPortsCntrOutPkts": oaLdPortsCntrOutPkts,
       "oaLdPortsCntrInOctets": oaLdPortsCntrInOctets,
       "oaLdPortsCntrOutOctets": oaLdPortsCntrOutOctets,
       "oaLdPortsCntrConformance": oaLdPortsCntrConformance,
       "oaLdPortsCntrGroups": oaLdPortsCntrGroups,
       "oaLdPortsCntrGroup": oaLdPortsCntrGroup,
       "oaLdPortsCntrCompliances": oaLdPortsCntrCompliances,
       "oaLdPortsCntrCompliance": oaLdPortsCntrCompliance}
)
