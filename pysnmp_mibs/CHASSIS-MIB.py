# SNMP MIB module (CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:55:01 2025
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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

nnchassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nnchassisMib.setRevisions(
        ("1900-01-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NnchassisModel_Type(DisplayString):
    """Custom type nnchassisModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NnchassisModel_Type.__name__ = "DisplayString"
_NnchassisModel_Object = MibScalar
nnchassisModel = _NnchassisModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 1),
    _NnchassisModel_Type()
)
nnchassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisModel.setStatus("current")


class _NnchassisOperStatus_Type(Integer32):
    """Custom type nnchassisOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("operdown", 2),
          ("admindown", 3),
          ("hotswap", 4),
          ("boot", 5),
          ("other", 6))
    )


_NnchassisOperStatus_Type.__name__ = "Integer32"
_NnchassisOperStatus_Object = MibScalar
nnchassisOperStatus = _NnchassisOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 2),
    _NnchassisOperStatus_Type()
)
nnchassisOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisOperStatus.setStatus("current")


class _NnchassisSerialNumber_Type(DisplayString):
    """Custom type nnchassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisSerialNumber_Type.__name__ = "DisplayString"
_NnchassisSerialNumber_Object = MibScalar
nnchassisSerialNumber = _NnchassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 3),
    _NnchassisSerialNumber_Type()
)
nnchassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisSerialNumber.setStatus("current")
_NnchassisRev_Type = DisplayString
_NnchassisRev_Object = MibScalar
nnchassisRev = _NnchassisRev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 4),
    _NnchassisRev_Type()
)
nnchassisRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisRev.setStatus("current")
_NnchassisInfoTable_Object = MibTable
nnchassisInfoTable = _NnchassisInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    nnchassisInfoTable.setStatus("current")
_NnchassisInfoEntry_Object = MibTableRow
nnchassisInfoEntry = _NnchassisInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1)
)
nnchassisInfoEntry.setIndexNames(
    (0, "CHASSIS-MIB", "nnchassisInfoSlotSubSlotIndex"),
)
if mibBuilder.loadTexts:
    nnchassisInfoEntry.setStatus("current")
_NnchassisInfoSlotSubSlotIndex_Type = Integer32
_NnchassisInfoSlotSubSlotIndex_Object = MibTableColumn
nnchassisInfoSlotSubSlotIndex = _NnchassisInfoSlotSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 1),
    _NnchassisInfoSlotSubSlotIndex_Type()
)
nnchassisInfoSlotSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoSlotSubSlotIndex.setStatus("current")


class _NnchassisInfoSlotSubSlotString_Type(DisplayString):
    """Custom type nnchassisInfoSlotSubSlotString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisInfoSlotSubSlotString_Type.__name__ = "DisplayString"
_NnchassisInfoSlotSubSlotString_Object = MibTableColumn
nnchassisInfoSlotSubSlotString = _NnchassisInfoSlotSubSlotString_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 2),
    _NnchassisInfoSlotSubSlotString_Type()
)
nnchassisInfoSlotSubSlotString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoSlotSubSlotString.setStatus("current")


class _NnchassisInfoCardType_Type(DisplayString):
    """Custom type nnchassisInfoCardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisInfoCardType_Type.__name__ = "DisplayString"
_NnchassisInfoCardType_Object = MibTableColumn
nnchassisInfoCardType = _NnchassisInfoCardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 3),
    _NnchassisInfoCardType_Type()
)
nnchassisInfoCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoCardType.setStatus("current")


class _NnchassisInfoCardStatus_Type(Integer32):
    """Custom type nnchassisInfoCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("operdown", 2),
          ("admindown", 3),
          ("hotswap", 4),
          ("normal", 5),
          ("unknown", 6),
          ("other", 7))
    )


_NnchassisInfoCardStatus_Type.__name__ = "Integer32"
_NnchassisInfoCardStatus_Object = MibTableColumn
nnchassisInfoCardStatus = _NnchassisInfoCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 4),
    _NnchassisInfoCardStatus_Type()
)
nnchassisInfoCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoCardStatus.setStatus("current")


class _NnchassisInfoModelNumber_Type(DisplayString):
    """Custom type nnchassisInfoModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisInfoModelNumber_Type.__name__ = "DisplayString"
_NnchassisInfoModelNumber_Object = MibTableColumn
nnchassisInfoModelNumber = _NnchassisInfoModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 5),
    _NnchassisInfoModelNumber_Type()
)
nnchassisInfoModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoModelNumber.setStatus("current")


class _NnchassisInfoSerialNumber_Type(DisplayString):
    """Custom type nnchassisInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisInfoSerialNumber_Type.__name__ = "DisplayString"
_NnchassisInfoSerialNumber_Object = MibTableColumn
nnchassisInfoSerialNumber = _NnchassisInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 6),
    _NnchassisInfoSerialNumber_Type()
)
nnchassisInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoSerialNumber.setStatus("current")
_NnchassisInfoFPGARev_Type = DisplayString
_NnchassisInfoFPGARev_Object = MibTableColumn
nnchassisInfoFPGARev = _NnchassisInfoFPGARev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 7),
    _NnchassisInfoFPGARev_Type()
)
nnchassisInfoFPGARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoFPGARev.setStatus("current")
_NnchassisInfoFPGAEngRev_Type = DisplayString
_NnchassisInfoFPGAEngRev_Object = MibTableColumn
nnchassisInfoFPGAEngRev = _NnchassisInfoFPGAEngRev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 8),
    _NnchassisInfoFPGAEngRev_Type()
)
nnchassisInfoFPGAEngRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoFPGAEngRev.setStatus("current")
_NnchassisInfoCPLDRev_Type = DisplayString
_NnchassisInfoCPLDRev_Object = MibTableColumn
nnchassisInfoCPLDRev = _NnchassisInfoCPLDRev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 9),
    _NnchassisInfoCPLDRev_Type()
)
nnchassisInfoCPLDRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoCPLDRev.setStatus("current")
_NnchassisInfoCPLDEngRev_Type = DisplayString
_NnchassisInfoCPLDEngRev_Object = MibTableColumn
nnchassisInfoCPLDEngRev = _NnchassisInfoCPLDEngRev_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 5, 1, 10),
    _NnchassisInfoCPLDEngRev_Type()
)
nnchassisInfoCPLDEngRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisInfoCPLDEngRev.setStatus("current")
_NnSFPTraps_ObjectIdentity = ObjectIdentity
nnSFPTraps = _NnSFPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6)
)
_NnSFPNotifications_ObjectIdentity = ObjectIdentity
nnSFPNotifications = _NnSFPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6, 0)
)
_NnSFPTrapVariables_ObjectIdentity = ObjectIdentity
nnSFPTrapVariables = _NnSFPTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6, 1)
)


class _NnSFPStatusStr_Type(DisplayString):
    """Custom type nnSFPStatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnSFPStatusStr_Type.__name__ = "DisplayString"
_NnSFPStatusStr_Object = MibScalar
nnSFPStatusStr = _NnSFPStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6, 1, 1),
    _NnSFPStatusStr_Type()
)
nnSFPStatusStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnSFPStatusStr.setStatus("current")

# Managed Objects groups


# Notification objects

nnSFPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6, 0, 1)
)
nnSFPUpTrap.setObjects(
    ("CHASSIS-MIB", "nnSFPStatusStr")
)
if mibBuilder.loadTexts:
    nnSFPUpTrap.setStatus(
        "current"
    )

nnSFPDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 6, 0, 2)
)
nnSFPDownTrap.setObjects(
    ("CHASSIS-MIB", "nnSFPStatusStr")
)
if mibBuilder.loadTexts:
    nnSFPDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHASSIS-MIB",
    **{"nnchassisMib": nnchassisMib,
       "nnchassisModel": nnchassisModel,
       "nnchassisOperStatus": nnchassisOperStatus,
       "nnchassisSerialNumber": nnchassisSerialNumber,
       "nnchassisRev": nnchassisRev,
       "nnchassisInfoTable": nnchassisInfoTable,
       "nnchassisInfoEntry": nnchassisInfoEntry,
       "nnchassisInfoSlotSubSlotIndex": nnchassisInfoSlotSubSlotIndex,
       "nnchassisInfoSlotSubSlotString": nnchassisInfoSlotSubSlotString,
       "nnchassisInfoCardType": nnchassisInfoCardType,
       "nnchassisInfoCardStatus": nnchassisInfoCardStatus,
       "nnchassisInfoModelNumber": nnchassisInfoModelNumber,
       "nnchassisInfoSerialNumber": nnchassisInfoSerialNumber,
       "nnchassisInfoFPGARev": nnchassisInfoFPGARev,
       "nnchassisInfoFPGAEngRev": nnchassisInfoFPGAEngRev,
       "nnchassisInfoCPLDRev": nnchassisInfoCPLDRev,
       "nnchassisInfoCPLDEngRev": nnchassisInfoCPLDEngRev,
       "nnSFPTraps": nnSFPTraps,
       "nnSFPNotifications": nnSFPNotifications,
       "nnSFPUpTrap": nnSFPUpTrap,
       "nnSFPDownTrap": nnSFPDownTrap,
       "nnSFPTrapVariables": nnSFPTrapVariables,
       "nnSFPStatusStr": nnSFPStatusStr}
)
