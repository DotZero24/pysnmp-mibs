# SNMP MIB module (HPN-ICF-EPON-FB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-EPON-FB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:53 2025
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

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

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

hpnicfEponFBMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEponFBMIB_ObjectIdentity = ObjectIdentity
hpnicfEponFBMIB = _HpnicfEponFBMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1)
)
_HpnicfEponFBMIBTable_Object = MibTable
hpnicfEponFBMIBTable = _HpnicfEponFBMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponFBMIBTable.setStatus("current")
_HpnicfEponFBMIBEntry_Object = MibTableRow
hpnicfEponFBMIBEntry = _HpnicfEponFBMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1)
)
hpnicfEponFBMIBEntry.setIndexNames(
    (0, "HPN-ICF-EPON-FB-MIB", "hpnicfEponFBGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponFBMIBEntry.setStatus("current")
_HpnicfEponFBGroupIndex_Type = Integer32
_HpnicfEponFBGroupIndex_Object = MibTableColumn
hpnicfEponFBGroupIndex = _HpnicfEponFBGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 1),
    _HpnicfEponFBGroupIndex_Type()
)
hpnicfEponFBGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponFBGroupIndex.setStatus("current")
_HpnicfEponFBGroupRowStatus_Type = RowStatus
_HpnicfEponFBGroupRowStatus_Object = MibTableColumn
hpnicfEponFBGroupRowStatus = _HpnicfEponFBGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 2),
    _HpnicfEponFBGroupRowStatus_Type()
)
hpnicfEponFBGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponFBGroupRowStatus.setStatus("current")
_HpnicfEponFBMasterPort_Type = Integer32
_HpnicfEponFBMasterPort_Object = MibTableColumn
hpnicfEponFBMasterPort = _HpnicfEponFBMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 3),
    _HpnicfEponFBMasterPort_Type()
)
hpnicfEponFBMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponFBMasterPort.setStatus("current")
_HpnicfEponFBSlavePort_Type = Integer32
_HpnicfEponFBSlavePort_Object = MibTableColumn
hpnicfEponFBSlavePort = _HpnicfEponFBSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 4),
    _HpnicfEponFBSlavePort_Type()
)
hpnicfEponFBSlavePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponFBSlavePort.setStatus("current")


class _HpnicfEponFBMasterPortStatus_Type(Integer32):
    """Custom type hpnicfEponFBMasterPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_HpnicfEponFBMasterPortStatus_Type.__name__ = "Integer32"
_HpnicfEponFBMasterPortStatus_Object = MibTableColumn
hpnicfEponFBMasterPortStatus = _HpnicfEponFBMasterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 5),
    _HpnicfEponFBMasterPortStatus_Type()
)
hpnicfEponFBMasterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponFBMasterPortStatus.setStatus("current")


class _HpnicfEponFBSlavePortStatus_Type(Integer32):
    """Custom type hpnicfEponFBSlavePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("down", 2))
    )


_HpnicfEponFBSlavePortStatus_Type.__name__ = "Integer32"
_HpnicfEponFBSlavePortStatus_Object = MibTableColumn
hpnicfEponFBSlavePortStatus = _HpnicfEponFBSlavePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 6),
    _HpnicfEponFBSlavePortStatus_Type()
)
hpnicfEponFBSlavePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponFBSlavePortStatus.setStatus("current")


class _HpnicfEponFBSwitchover_Type(Integer32):
    """Custom type hpnicfEponFBSwitchover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_HpnicfEponFBSwitchover_Type.__name__ = "Integer32"
_HpnicfEponFBSwitchover_Object = MibTableColumn
hpnicfEponFBSwitchover = _HpnicfEponFBSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 7),
    _HpnicfEponFBSwitchover_Type()
)
hpnicfEponFBSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponFBSwitchover.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EPON-FB-MIB",
    **{"hpnicfEponFBMibObjects": hpnicfEponFBMibObjects,
       "hpnicfEponFBMIB": hpnicfEponFBMIB,
       "hpnicfEponFBMIBTable": hpnicfEponFBMIBTable,
       "hpnicfEponFBMIBEntry": hpnicfEponFBMIBEntry,
       "hpnicfEponFBGroupIndex": hpnicfEponFBGroupIndex,
       "hpnicfEponFBGroupRowStatus": hpnicfEponFBGroupRowStatus,
       "hpnicfEponFBMasterPort": hpnicfEponFBMasterPort,
       "hpnicfEponFBSlavePort": hpnicfEponFBSlavePort,
       "hpnicfEponFBMasterPortStatus": hpnicfEponFBMasterPortStatus,
       "hpnicfEponFBSlavePortStatus": hpnicfEponFBSlavePortStatus,
       "hpnicfEponFBSwitchover": hpnicfEponFBSwitchover}
)
