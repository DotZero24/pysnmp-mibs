# SNMP MIB module (SWITCH-MULTISYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-MULTISYS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:32 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

raisecomMultiSys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22)
)
if mibBuilder.loadTexts:
    raisecomMultiSys.setRevisions(
        ("2011-01-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomMultiSysMibObjects_ObjectIdentity = ObjectIdentity
raisecomMultiSysMibObjects = _RaisecomMultiSysMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1)
)
_RaisecomMultiSysGlobalGroup_ObjectIdentity = ObjectIdentity
raisecomMultiSysGlobalGroup = _RaisecomMultiSysGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 1)
)
_RaisecomMultiSysVerNum_Type = Unsigned32
_RaisecomMultiSysVerNum_Object = MibScalar
raisecomMultiSysVerNum = _RaisecomMultiSysVerNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 1, 1),
    _RaisecomMultiSysVerNum_Type()
)
raisecomMultiSysVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMultiSysVerNum.setStatus("current")
_RaisecomMultiSysOverWriteVer_Type = Unsigned32
_RaisecomMultiSysOverWriteVer_Object = MibScalar
raisecomMultiSysOverWriteVer = _RaisecomMultiSysOverWriteVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 1, 2),
    _RaisecomMultiSysOverWriteVer_Type()
)
raisecomMultiSysOverWriteVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMultiSysOverWriteVer.setStatus("current")
_RaisecomMultiSysUploadVer_Type = Unsigned32
_RaisecomMultiSysUploadVer_Object = MibScalar
raisecomMultiSysUploadVer = _RaisecomMultiSysUploadVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 1, 3),
    _RaisecomMultiSysUploadVer_Type()
)
raisecomMultiSysUploadVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMultiSysUploadVer.setStatus("current")
_RaisecomMultiSysNextBootVer_Type = Unsigned32
_RaisecomMultiSysNextBootVer_Object = MibScalar
raisecomMultiSysNextBootVer = _RaisecomMultiSysNextBootVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 1, 4),
    _RaisecomMultiSysNextBootVer_Type()
)
raisecomMultiSysNextBootVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomMultiSysNextBootVer.setStatus("current")
_RaisecomMultiSysVerTable_Object = MibTable
raisecomMultiSysVerTable = _RaisecomMultiSysVerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomMultiSysVerTable.setStatus("current")
_RaisecomMultiSysVerEntry_Object = MibTableRow
raisecomMultiSysVerEntry = _RaisecomMultiSysVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 2, 1)
)
raisecomMultiSysVerEntry.setIndexNames(
    (0, "SWITCH-MULTISYS-MIB", "raisecomMultiSysVerIndex"),
)
if mibBuilder.loadTexts:
    raisecomMultiSysVerEntry.setStatus("current")
_RaisecomMultiSysVerIndex_Type = Unsigned32
_RaisecomMultiSysVerIndex_Object = MibTableColumn
raisecomMultiSysVerIndex = _RaisecomMultiSysVerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 2, 1, 1),
    _RaisecomMultiSysVerIndex_Type()
)
raisecomMultiSysVerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomMultiSysVerIndex.setStatus("current")


class _RaisecomMultiSysVerName_Type(OctetString):
    """Custom type raisecomMultiSysVerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_RaisecomMultiSysVerName_Type.__name__ = "OctetString"
_RaisecomMultiSysVerName_Object = MibTableColumn
raisecomMultiSysVerName = _RaisecomMultiSysVerName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 2, 1, 2),
    _RaisecomMultiSysVerName_Type()
)
raisecomMultiSysVerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMultiSysVerName.setStatus("current")
_RaisecomMultiSysVerSize_Type = Unsigned32
_RaisecomMultiSysVerSize_Object = MibTableColumn
raisecomMultiSysVerSize = _RaisecomMultiSysVerSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 22, 1, 2, 1, 3),
    _RaisecomMultiSysVerSize_Type()
)
raisecomMultiSysVerSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMultiSysVerSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-MULTISYS-MIB",
    **{"raisecomMultiSys": raisecomMultiSys,
       "raisecomMultiSysMibObjects": raisecomMultiSysMibObjects,
       "raisecomMultiSysGlobalGroup": raisecomMultiSysGlobalGroup,
       "raisecomMultiSysVerNum": raisecomMultiSysVerNum,
       "raisecomMultiSysOverWriteVer": raisecomMultiSysOverWriteVer,
       "raisecomMultiSysUploadVer": raisecomMultiSysUploadVer,
       "raisecomMultiSysNextBootVer": raisecomMultiSysNextBootVer,
       "raisecomMultiSysVerTable": raisecomMultiSysVerTable,
       "raisecomMultiSysVerEntry": raisecomMultiSysVerEntry,
       "raisecomMultiSysVerIndex": raisecomMultiSysVerIndex,
       "raisecomMultiSysVerName": raisecomMultiSysVerName,
       "raisecomMultiSysVerSize": raisecomMultiSysVerSize}
)
