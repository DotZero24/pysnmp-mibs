# SNMP MIB module (OCNOS-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/OCNOS-VRF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:19 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

(vrVrId,) = mibBuilder.importSymbols(
    "OCNOS-VR-MIB",
    "vrVrId")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

vrf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 3)
)
if mibBuilder.loadTexts:
    vrf.setRevisions(
        ("2018-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrfVrfTable_Object = MibTable
vrfVrfTable = _VrfVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1)
)
if mibBuilder.loadTexts:
    vrfVrfTable.setStatus("current")
_VrfVrfEntry_Object = MibTableRow
vrfVrfEntry = _VrfVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1)
)
vrfVrfEntry.setIndexNames(
    (0, "OCNOS-VR-MIB", "vrVrId"),
    (0, "OCNOS-VRF-MIB", "vrfVrfName"),
)
if mibBuilder.loadTexts:
    vrfVrfEntry.setStatus("current")
_VrfVrfName_Type = OctetString
_VrfVrfName_Object = MibTableColumn
vrfVrfName = _VrfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 1),
    _VrfVrfName_Type()
)
vrfVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrfVrfName.setStatus("current")


class _VrfMacVrf_Type(Integer32):
    """Custom type vrfMacVrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_VrfMacVrf_Type.__name__ = "Integer32"
_VrfMacVrf_Object = MibTableColumn
vrfMacVrf = _VrfMacVrf_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 2),
    _VrfMacVrf_Type()
)
vrfMacVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrfMacVrf.setStatus("current")
_VrfVrfId_Type = Unsigned32
_VrfVrfId_Object = MibTableColumn
vrfVrfId = _VrfVrfId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 3),
    _VrfVrfId_Type()
)
vrfVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrfVrfId.setStatus("current")
_VrfFibId_Type = Unsigned32
_VrfFibId_Object = MibTableColumn
vrfFibId = _VrfFibId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 4),
    _VrfFibId_Type()
)
vrfFibId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrfFibId.setStatus("current")
_VrfDescription_Type = OctetString
_VrfDescription_Object = MibTableColumn
vrfDescription = _VrfDescription_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 5),
    _VrfDescription_Type()
)
vrfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrfDescription.setStatus("current")
_VrfRouterId_Type = IpAddress
_VrfRouterId_Object = MibTableColumn
vrfRouterId = _VrfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 3, 1, 1, 6),
    _VrfRouterId_Type()
)
vrfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrfRouterId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCNOS-VRF-MIB",
    **{"vrf": vrf,
       "vrfVrfTable": vrfVrfTable,
       "vrfVrfEntry": vrfVrfEntry,
       "vrfVrfName": vrfVrfName,
       "vrfMacVrf": vrfMacVrf,
       "vrfVrfId": vrfVrfId,
       "vrfFibId": vrfFibId,
       "vrfDescription": vrfDescription,
       "vrfRouterId": vrfRouterId}
)
