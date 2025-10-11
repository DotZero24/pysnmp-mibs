# SNMP MIB module (SUPERMICRO-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:10 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsdhcpsnp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3)
)
if mibBuilder.loadTexts:
    fsdhcpsnp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpSnpScalars_ObjectIdentity = ObjectIdentity
fsDhcpSnpScalars = _FsDhcpSnpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 1)
)


class _FsDhcpSnpSnoopingAdminStatus_Type(Integer32):
    """Custom type fsDhcpSnpSnoopingAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsDhcpSnpSnoopingAdminStatus_Type.__name__ = "Integer32"
_FsDhcpSnpSnoopingAdminStatus_Object = MibScalar
fsDhcpSnpSnoopingAdminStatus = _FsDhcpSnpSnoopingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 1, 1),
    _FsDhcpSnpSnoopingAdminStatus_Type()
)
fsDhcpSnpSnoopingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpSnpSnoopingAdminStatus.setStatus("current")


class _FsDhcpSnpMacVerifyStatus_Type(Integer32):
    """Custom type fsDhcpSnpMacVerifyStatus based on Integer32"""
    defaultValue = 1

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


_FsDhcpSnpMacVerifyStatus_Type.__name__ = "Integer32"
_FsDhcpSnpMacVerifyStatus_Object = MibScalar
fsDhcpSnpMacVerifyStatus = _FsDhcpSnpMacVerifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 1, 2),
    _FsDhcpSnpMacVerifyStatus_Type()
)
fsDhcpSnpMacVerifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpSnpMacVerifyStatus.setStatus("current")
_FsDhcpSnpInterface_ObjectIdentity = ObjectIdentity
fsDhcpSnpInterface = _FsDhcpSnpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2)
)
_FsDhcpSnpInterfaceTable_Object = MibTable
fsDhcpSnpInterfaceTable = _FsDhcpSnpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fsDhcpSnpInterfaceTable.setStatus("current")
_FsDhcpSnpInterfaceEntry_Object = MibTableRow
fsDhcpSnpInterfaceEntry = _FsDhcpSnpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1)
)
fsDhcpSnpInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-DHCP-SNOOPING-MIB", "fsDhcpSnpVlanId"),
)
if mibBuilder.loadTexts:
    fsDhcpSnpInterfaceEntry.setStatus("current")


class _FsDhcpSnpVlanId_Type(Integer32):
    """Custom type fsDhcpSnpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsDhcpSnpVlanId_Type.__name__ = "Integer32"
_FsDhcpSnpVlanId_Object = MibTableColumn
fsDhcpSnpVlanId = _FsDhcpSnpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 1),
    _FsDhcpSnpVlanId_Type()
)
fsDhcpSnpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpSnpVlanId.setStatus("current")


class _FsDhcpSnpVlanSnpStatus_Type(Integer32):
    """Custom type fsDhcpSnpVlanSnpStatus based on Integer32"""
    defaultValue = 2

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


_FsDhcpSnpVlanSnpStatus_Type.__name__ = "Integer32"
_FsDhcpSnpVlanSnpStatus_Object = MibTableColumn
fsDhcpSnpVlanSnpStatus = _FsDhcpSnpVlanSnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 2),
    _FsDhcpSnpVlanSnpStatus_Type()
)
fsDhcpSnpVlanSnpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpSnpVlanSnpStatus.setStatus("current")
_FsDhcpSnpRxDiscovers_Type = Counter32
_FsDhcpSnpRxDiscovers_Object = MibTableColumn
fsDhcpSnpRxDiscovers = _FsDhcpSnpRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 3),
    _FsDhcpSnpRxDiscovers_Type()
)
fsDhcpSnpRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpRxDiscovers.setStatus("current")
_FsDhcpSnpRxRequests_Type = Counter32
_FsDhcpSnpRxRequests_Object = MibTableColumn
fsDhcpSnpRxRequests = _FsDhcpSnpRxRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 4),
    _FsDhcpSnpRxRequests_Type()
)
fsDhcpSnpRxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpRxRequests.setStatus("current")
_FsDhcpSnpRxReleases_Type = Counter32
_FsDhcpSnpRxReleases_Object = MibTableColumn
fsDhcpSnpRxReleases = _FsDhcpSnpRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 5),
    _FsDhcpSnpRxReleases_Type()
)
fsDhcpSnpRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpRxReleases.setStatus("current")
_FsDhcpSnpRxDeclines_Type = Counter32
_FsDhcpSnpRxDeclines_Object = MibTableColumn
fsDhcpSnpRxDeclines = _FsDhcpSnpRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 6),
    _FsDhcpSnpRxDeclines_Type()
)
fsDhcpSnpRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpRxDeclines.setStatus("current")
_FsDhcpSnpRxInforms_Type = Counter32
_FsDhcpSnpRxInforms_Object = MibTableColumn
fsDhcpSnpRxInforms = _FsDhcpSnpRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 7),
    _FsDhcpSnpRxInforms_Type()
)
fsDhcpSnpRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpRxInforms.setStatus("current")
_FsDhcpSnpTxOffers_Type = Counter32
_FsDhcpSnpTxOffers_Object = MibTableColumn
fsDhcpSnpTxOffers = _FsDhcpSnpTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 8),
    _FsDhcpSnpTxOffers_Type()
)
fsDhcpSnpTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpTxOffers.setStatus("current")
_FsDhcpSnpTxAcks_Type = Counter32
_FsDhcpSnpTxAcks_Object = MibTableColumn
fsDhcpSnpTxAcks = _FsDhcpSnpTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 9),
    _FsDhcpSnpTxAcks_Type()
)
fsDhcpSnpTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpTxAcks.setStatus("current")
_FsDhcpSnpTxNaks_Type = Counter32
_FsDhcpSnpTxNaks_Object = MibTableColumn
fsDhcpSnpTxNaks = _FsDhcpSnpTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 10),
    _FsDhcpSnpTxNaks_Type()
)
fsDhcpSnpTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpTxNaks.setStatus("current")
_FsDhcpSnpNoOfDiscards_Type = Counter32
_FsDhcpSnpNoOfDiscards_Object = MibTableColumn
fsDhcpSnpNoOfDiscards = _FsDhcpSnpNoOfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 11),
    _FsDhcpSnpNoOfDiscards_Type()
)
fsDhcpSnpNoOfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpNoOfDiscards.setStatus("current")
_FsDhcpSnpMacDiscards_Type = Counter32
_FsDhcpSnpMacDiscards_Object = MibTableColumn
fsDhcpSnpMacDiscards = _FsDhcpSnpMacDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 12),
    _FsDhcpSnpMacDiscards_Type()
)
fsDhcpSnpMacDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpMacDiscards.setStatus("current")
_FsDhcpSnpServerDiscards_Type = Counter32
_FsDhcpSnpServerDiscards_Object = MibTableColumn
fsDhcpSnpServerDiscards = _FsDhcpSnpServerDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 13),
    _FsDhcpSnpServerDiscards_Type()
)
fsDhcpSnpServerDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpServerDiscards.setStatus("current")
_FsDhcpSnpOptionDiscards_Type = Counter32
_FsDhcpSnpOptionDiscards_Object = MibTableColumn
fsDhcpSnpOptionDiscards = _FsDhcpSnpOptionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 14),
    _FsDhcpSnpOptionDiscards_Type()
)
fsDhcpSnpOptionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpOptionDiscards.setStatus("current")
_FsDhcpSnpInterfaceStatus_Type = RowStatus
_FsDhcpSnpInterfaceStatus_Object = MibTableColumn
fsDhcpSnpInterfaceStatus = _FsDhcpSnpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 3, 2, 1, 1, 15),
    _FsDhcpSnpInterfaceStatus_Type()
)
fsDhcpSnpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpSnpInterfaceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DHCP-SNOOPING-MIB",
    **{"fsdhcpsnp": fsdhcpsnp,
       "fsDhcpSnpScalars": fsDhcpSnpScalars,
       "fsDhcpSnpSnoopingAdminStatus": fsDhcpSnpSnoopingAdminStatus,
       "fsDhcpSnpMacVerifyStatus": fsDhcpSnpMacVerifyStatus,
       "fsDhcpSnpInterface": fsDhcpSnpInterface,
       "fsDhcpSnpInterfaceTable": fsDhcpSnpInterfaceTable,
       "fsDhcpSnpInterfaceEntry": fsDhcpSnpInterfaceEntry,
       "fsDhcpSnpVlanId": fsDhcpSnpVlanId,
       "fsDhcpSnpVlanSnpStatus": fsDhcpSnpVlanSnpStatus,
       "fsDhcpSnpRxDiscovers": fsDhcpSnpRxDiscovers,
       "fsDhcpSnpRxRequests": fsDhcpSnpRxRequests,
       "fsDhcpSnpRxReleases": fsDhcpSnpRxReleases,
       "fsDhcpSnpRxDeclines": fsDhcpSnpRxDeclines,
       "fsDhcpSnpRxInforms": fsDhcpSnpRxInforms,
       "fsDhcpSnpTxOffers": fsDhcpSnpTxOffers,
       "fsDhcpSnpTxAcks": fsDhcpSnpTxAcks,
       "fsDhcpSnpTxNaks": fsDhcpSnpTxNaks,
       "fsDhcpSnpNoOfDiscards": fsDhcpSnpNoOfDiscards,
       "fsDhcpSnpMacDiscards": fsDhcpSnpMacDiscards,
       "fsDhcpSnpServerDiscards": fsDhcpSnpServerDiscards,
       "fsDhcpSnpOptionDiscards": fsDhcpSnpOptionDiscards,
       "fsDhcpSnpInterfaceStatus": fsDhcpSnpInterfaceStatus}
)
