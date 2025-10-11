# SNMP MIB module (MITEL-MN3100-CALL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mitel/MITEL-MN3100-CALL-CONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:35 2025
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

mitelCallControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9)
)
if mibBuilder.loadTexts:
    mitelCallControl.setRevisions(
        ("2003-03-24 11:43",
         "2002-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsIpera1000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera1000 = _MitelIdCsIpera1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelCallCtrlFaultTable_Object = MibTable
mitelCallCtrlFaultTable = _MitelCallCtrlFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1)
)
if mibBuilder.loadTexts:
    mitelCallCtrlFaultTable.setStatus("current")
_MitelCallCtrlFaultEntry_Object = MibTableRow
mitelCallCtrlFaultEntry = _MitelCallCtrlFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1)
)
mitelCallCtrlFaultEntry.setIndexNames(
    (0, "MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFaultTblIndex"),
)
if mibBuilder.loadTexts:
    mitelCallCtrlFaultEntry.setStatus("current")
_MitelCallCtrlFaultTblIndex_Type = Integer32
_MitelCallCtrlFaultTblIndex_Object = MibTableColumn
mitelCallCtrlFaultTblIndex = _MitelCallCtrlFaultTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1),
    _MitelCallCtrlFaultTblIndex_Type()
)
mitelCallCtrlFaultTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelCallCtrlFaultTblIndex.setStatus("current")


class _MitelCallCtrlFaultId_Type(Integer32):
    """Custom type mitelCallCtrlFaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mitelCallCtrlFailedSeizeLine", 1),
          ("mitelCallCtrlDdiMappingError", 2))
    )


_MitelCallCtrlFaultId_Type.__name__ = "Integer32"
_MitelCallCtrlFaultId_Object = MibTableColumn
mitelCallCtrlFaultId = _MitelCallCtrlFaultId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2),
    _MitelCallCtrlFaultId_Type()
)
mitelCallCtrlFaultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelCallCtrlFaultId.setStatus("current")


class _MitelCallCtrlFaultStatus_Type(Integer32):
    """Custom type mitelCallCtrlFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("clear", 2),
          ("message", 3))
    )


_MitelCallCtrlFaultStatus_Type.__name__ = "Integer32"
_MitelCallCtrlFaultStatus_Object = MibTableColumn
mitelCallCtrlFaultStatus = _MitelCallCtrlFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 3),
    _MitelCallCtrlFaultStatus_Type()
)
mitelCallCtrlFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelCallCtrlFaultStatus.setStatus("current")
_MitelCallCtrlFaultOccur_Type = Counter32
_MitelCallCtrlFaultOccur_Object = MibTableColumn
mitelCallCtrlFaultOccur = _MitelCallCtrlFaultOccur_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 4),
    _MitelCallCtrlFaultOccur_Type()
)
mitelCallCtrlFaultOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelCallCtrlFaultOccur.setStatus("current")

# Managed Objects groups


# Notification objects

mitelCallCtrlFailedSeizeLineNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 406)
)
mitelCallCtrlFailedSeizeLineNotif.setObjects(
      *(("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFaultStatus"),
        ("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFaultOccur"))
)
if mibBuilder.loadTexts:
    mitelCallCtrlFailedSeizeLineNotif.setStatus(
        "current"
    )

mitelCallCtrlDdiMappingErrorNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 407)
)
mitelCallCtrlDdiMappingErrorNotif.setObjects(
      *(("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFaultStatus"),
        ("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFaultOccur"))
)
if mibBuilder.loadTexts:
    mitelCallCtrlDdiMappingErrorNotif.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
      *(("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlFailedSeizeLineNotif"),
        ("MITEL-MN3100-CALL-CONTROL-MIB", "mitelCallCtrlDdiMappingErrorNotif"))
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-MN3100-CALL-CONTROL-MIB",
    **{"mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelCallCtrlFailedSeizeLineNotif": mitelCallCtrlFailedSeizeLineNotif,
       "mitelCallCtrlDdiMappingErrorNotif": mitelCallCtrlDdiMappingErrorNotif,
       "mitelProprietary": mitelProprietary,
       "mitelCallControl": mitelCallControl,
       "mitelCallCtrlFaultTable": mitelCallCtrlFaultTable,
       "mitelCallCtrlFaultEntry": mitelCallCtrlFaultEntry,
       "mitelCallCtrlFaultTblIndex": mitelCallCtrlFaultTblIndex,
       "mitelCallCtrlFaultId": mitelCallCtrlFaultId,
       "mitelCallCtrlFaultStatus": mitelCallCtrlFaultStatus,
       "mitelCallCtrlFaultOccur": mitelCallCtrlFaultOccur}
)
