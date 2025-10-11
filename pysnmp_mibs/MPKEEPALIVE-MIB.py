# SNMP MIB module (MPKEEPALIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPKEEPALIVE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:10 2025
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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
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

mpKeepaliveMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpKeepaliveTable_Object = MibTable
mpKeepaliveTable = _MpKeepaliveTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1)
)
if mibBuilder.loadTexts:
    mpKeepaliveTable.setStatus("current")
_MpKeepaliveEntry_Object = MibTableRow
mpKeepaliveEntry = _MpKeepaliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1)
)
mpKeepaliveEntry.setIndexNames(
    (0, "MPKEEPALIVE-MIB", "mpIfNmae"),
)
if mibBuilder.loadTexts:
    mpKeepaliveEntry.setStatus("current")
_MpKaIfNmae_Type = DisplayString
_MpKaIfNmae_Object = MibTableColumn
mpKaIfNmae = _MpKaIfNmae_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 1),
    _MpKaIfNmae_Type()
)
mpKaIfNmae.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpKaIfNmae.setStatus("current")


class _MpKaTimeout_Type(Integer32):
    """Custom type mpKaTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MpKaTimeout_Type.__name__ = "Integer32"
_MpKaTimeout_Object = MibTableColumn
mpKaTimeout = _MpKaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 2),
    _MpKaTimeout_Type()
)
mpKaTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpKaTimeout.setStatus("current")


class _MpKaRetry_Type(Integer32):
    """Custom type mpKaRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MpKaRetry_Type.__name__ = "Integer32"
_MpKaRetry_Object = MibTableColumn
mpKaRetry = _MpKaRetry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 3),
    _MpKaRetry_Type()
)
mpKaRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpKaRetry.setStatus("current")
_MpKaGateway_Type = IpAddress
_MpKaGateway_Object = MibTableColumn
mpKaGateway = _MpKaGateway_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 4),
    _MpKaGateway_Type()
)
mpKaGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpKaGateway.setStatus("current")
_MpKaRowstatus_Type = RowStatus
_MpKaRowstatus_Object = MibTableColumn
mpKaRowstatus = _MpKaRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 5),
    _MpKaRowstatus_Type()
)
mpKaRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpKaRowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPKEEPALIVE-MIB",
    **{"mpKeepaliveMib": mpKeepaliveMib,
       "mpKeepaliveTable": mpKeepaliveTable,
       "mpKeepaliveEntry": mpKeepaliveEntry,
       "mpKaIfNmae": mpKaIfNmae,
       "mpKaTimeout": mpKaTimeout,
       "mpKaRetry": mpKaRetry,
       "mpKaGateway": mpKaGateway,
       "mpKaRowstatus": mpKaRowstatus}
)
