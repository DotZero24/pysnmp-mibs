# SNMP MIB module (MELLANOX-CONFIG-DB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-CONFIG-DB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:46 2025
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

(mellanoxConfigDB,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxConfigDB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mellanoxConfigDBMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1)
)
if mibBuilder.loadTexts:
    mellanoxConfigDBMib.setRevisions(
        ("2017-07-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxConfigDBMibObjects_ObjectIdentity = ObjectIdentity
mellanoxConfigDBMibObjects = _MellanoxConfigDBMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1)
)
_MellanoxConfigDBCmd_ObjectIdentity = ObjectIdentity
mellanoxConfigDBCmd = _MellanoxConfigDBCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2)
)
_MellanoxConfigDBCmdUri_Type = OctetString
_MellanoxConfigDBCmdUri_Object = MibScalar
mellanoxConfigDBCmdUri = _MellanoxConfigDBCmdUri_Object(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 1),
    _MellanoxConfigDBCmdUri_Type()
)
mellanoxConfigDBCmdUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxConfigDBCmdUri.setStatus("current")
_MellanoxConfigDBCmdFilename_Type = OctetString
_MellanoxConfigDBCmdFilename_Object = MibScalar
mellanoxConfigDBCmdFilename = _MellanoxConfigDBCmdFilename_Object(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 2),
    _MellanoxConfigDBCmdFilename_Type()
)
mellanoxConfigDBCmdFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxConfigDBCmdFilename.setStatus("current")


class _MellanoxConfigDBCmdExecute_Type(Integer32):
    """Custom type mellanoxConfigDBCmdExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mellanoxConfigDBCmdExecuteBinarySwitchTo", 1),
          ("mellanoxConfigDBCmdExecuteTextApply", 2),
          ("mellanoxConfigDBCmdExecuteTextApplyFailContinue", 3),
          ("mellanoxConfigDBCmdExecuteBinaryUpload", 4),
          ("mellanoxConfigDBCmdExecuteTextUpload", 5),
          ("mellanoxConfigDBCmdExecuteConfigWrite", 6),
          ("mellanoxConfigDBCmdExecuteBinaryDelete", 7),
          ("mellanoxConfigDBCmdExecuteTextDelete", 8))
    )


_MellanoxConfigDBCmdExecute_Type.__name__ = "Integer32"
_MellanoxConfigDBCmdExecute_Object = MibScalar
mellanoxConfigDBCmdExecute = _MellanoxConfigDBCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 3),
    _MellanoxConfigDBCmdExecute_Type()
)
mellanoxConfigDBCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxConfigDBCmdExecute.setStatus("current")
_MellanoxConfigDBCmdStatus_Type = Integer32
_MellanoxConfigDBCmdStatus_Object = MibScalar
mellanoxConfigDBCmdStatus = _MellanoxConfigDBCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 4),
    _MellanoxConfigDBCmdStatus_Type()
)
mellanoxConfigDBCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxConfigDBCmdStatus.setStatus("current")
_MellanoxConfigDBCmdStatusString_Type = OctetString
_MellanoxConfigDBCmdStatusString_Object = MibScalar
mellanoxConfigDBCmdStatusString = _MellanoxConfigDBCmdStatusString_Object(
    (1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 5),
    _MellanoxConfigDBCmdStatusString_Type()
)
mellanoxConfigDBCmdStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxConfigDBCmdStatusString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-CONFIG-DB-MIB",
    **{"mellanoxConfigDBMib": mellanoxConfigDBMib,
       "mellanoxConfigDBMibObjects": mellanoxConfigDBMibObjects,
       "mellanoxConfigDBCmd": mellanoxConfigDBCmd,
       "mellanoxConfigDBCmdUri": mellanoxConfigDBCmdUri,
       "mellanoxConfigDBCmdFilename": mellanoxConfigDBCmdFilename,
       "mellanoxConfigDBCmdExecute": mellanoxConfigDBCmdExecute,
       "mellanoxConfigDBCmdStatus": mellanoxConfigDBCmdStatus,
       "mellanoxConfigDBCmdStatusString": mellanoxConfigDBCmdStatusString}
)
