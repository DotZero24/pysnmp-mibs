# SNMP MIB module (OS-ONE-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-ONE-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:05 2025
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

(EntityName,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "EntityName",
    "oaOptiSwitch")

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

osOneIpMng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43)
)
if mibBuilder.loadTexts:
    osOneIpMng.setRevisions(
        ("2014-10-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsOneIpMngNat_ObjectIdentity = ObjectIdentity
osOneIpMngNat = _OsOneIpMngNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1)
)
_OsOneIpMngNatGen_ObjectIdentity = ObjectIdentity
osOneIpMngNatGen = _OsOneIpMngNatGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1)
)
_OsOneIpMngDefaultTable_Object = MibTable
osOneIpMngDefaultTable = _OsOneIpMngDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2)
)
if mibBuilder.loadTexts:
    osOneIpMngDefaultTable.setStatus("current")
_OsOneIpMngDefaultEntry_Object = MibTableRow
osOneIpMngDefaultEntry = _OsOneIpMngDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1)
)
osOneIpMngDefaultEntry.setIndexNames(
    (0, "OS-ONE-IP-MIB", "osOneIpMngDefName"),
)
if mibBuilder.loadTexts:
    osOneIpMngDefaultEntry.setStatus("current")
_OsOneIpMngDefName_Type = EntityName
_OsOneIpMngDefName_Object = MibTableColumn
osOneIpMngDefName = _OsOneIpMngDefName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 1),
    _OsOneIpMngDefName_Type()
)
osOneIpMngDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osOneIpMngDefName.setStatus("current")


class _OsOneIpMngDefTransport_Type(Integer32):
    """Custom type osOneIpMngDefTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_OsOneIpMngDefTransport_Type.__name__ = "Integer32"
_OsOneIpMngDefTransport_Object = MibTableColumn
osOneIpMngDefTransport = _OsOneIpMngDefTransport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 2),
    _OsOneIpMngDefTransport_Type()
)
osOneIpMngDefTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefTransport.setStatus("current")


class _OsOneIpMngDefListType_Type(Integer32):
    """Custom type osOneIpMngDefListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("range", 2),
          ("pair", 3))
    )


_OsOneIpMngDefListType_Type.__name__ = "Integer32"
_OsOneIpMngDefListType_Object = MibTableColumn
osOneIpMngDefListType = _OsOneIpMngDefListType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 3),
    _OsOneIpMngDefListType_Type()
)
osOneIpMngDefListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefListType.setStatus("current")


class _OsOneIpMngDefStdFirstPort_Type(Unsigned32):
    """Custom type osOneIpMngDefStdFirstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsOneIpMngDefStdFirstPort_Type.__name__ = "Unsigned32"
_OsOneIpMngDefStdFirstPort_Object = MibTableColumn
osOneIpMngDefStdFirstPort = _OsOneIpMngDefStdFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 4),
    _OsOneIpMngDefStdFirstPort_Type()
)
osOneIpMngDefStdFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefStdFirstPort.setStatus("current")


class _OsOneIpMngDefStdLastPort_Type(Unsigned32):
    """Custom type osOneIpMngDefStdLastPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsOneIpMngDefStdLastPort_Type.__name__ = "Unsigned32"
_OsOneIpMngDefStdLastPort_Object = MibTableColumn
osOneIpMngDefStdLastPort = _OsOneIpMngDefStdLastPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 5),
    _OsOneIpMngDefStdLastPort_Type()
)
osOneIpMngDefStdLastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefStdLastPort.setStatus("current")


class _OsOneIpMngDefAltFirstPort_Type(Unsigned32):
    """Custom type osOneIpMngDefAltFirstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsOneIpMngDefAltFirstPort_Type.__name__ = "Unsigned32"
_OsOneIpMngDefAltFirstPort_Object = MibTableColumn
osOneIpMngDefAltFirstPort = _OsOneIpMngDefAltFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 6),
    _OsOneIpMngDefAltFirstPort_Type()
)
osOneIpMngDefAltFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefAltFirstPort.setStatus("current")


class _OsOneIpMngDefAltLastPort_Type(Unsigned32):
    """Custom type osOneIpMngDefAltLastPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsOneIpMngDefAltLastPort_Type.__name__ = "Unsigned32"
_OsOneIpMngDefAltLastPort_Object = MibTableColumn
osOneIpMngDefAltLastPort = _OsOneIpMngDefAltLastPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 7),
    _OsOneIpMngDefAltLastPort_Type()
)
osOneIpMngDefAltLastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefAltLastPort.setStatus("current")


class _OsOneIpMngDefOperStatus_Type(Integer32):
    """Custom type osOneIpMngDefOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("original", 1),
          ("modified", 2),
          ("removed", 3))
    )


_OsOneIpMngDefOperStatus_Type.__name__ = "Integer32"
_OsOneIpMngDefOperStatus_Object = MibTableColumn
osOneIpMngDefOperStatus = _OsOneIpMngDefOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 2, 1, 98),
    _OsOneIpMngDefOperStatus_Type()
)
osOneIpMngDefOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngDefOperStatus.setStatus("current")
_OsOneIpMngProtoTable_Object = MibTable
osOneIpMngProtoTable = _OsOneIpMngProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3)
)
if mibBuilder.loadTexts:
    osOneIpMngProtoTable.setStatus("current")
_OsOneIpMngProtoEntry_Object = MibTableRow
osOneIpMngProtoEntry = _OsOneIpMngProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1)
)
osOneIpMngProtoEntry.setIndexNames(
    (0, "OS-ONE-IP-MIB", "osOneIpMngCfgName"),
)
if mibBuilder.loadTexts:
    osOneIpMngProtoEntry.setStatus("current")
_OsOneIpMngCfgName_Type = EntityName
_OsOneIpMngCfgName_Object = MibTableColumn
osOneIpMngCfgName = _OsOneIpMngCfgName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 1),
    _OsOneIpMngCfgName_Type()
)
osOneIpMngCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osOneIpMngCfgName.setStatus("current")


class _OsOneIpMngCfgTransport_Type(Integer32):
    """Custom type osOneIpMngCfgTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_OsOneIpMngCfgTransport_Type.__name__ = "Integer32"
_OsOneIpMngCfgTransport_Object = MibTableColumn
osOneIpMngCfgTransport = _OsOneIpMngCfgTransport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 2),
    _OsOneIpMngCfgTransport_Type()
)
osOneIpMngCfgTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgTransport.setStatus("current")


class _OsOneIpMngCfgListType_Type(Integer32):
    """Custom type osOneIpMngCfgListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("range", 2),
          ("pair", 3))
    )


_OsOneIpMngCfgListType_Type.__name__ = "Integer32"
_OsOneIpMngCfgListType_Object = MibTableColumn
osOneIpMngCfgListType = _OsOneIpMngCfgListType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 3),
    _OsOneIpMngCfgListType_Type()
)
osOneIpMngCfgListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgListType.setStatus("current")


class _OsOneIpMngCfgStdFirstPort_Type(Unsigned32):
    """Custom type osOneIpMngCfgStdFirstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsOneIpMngCfgStdFirstPort_Type.__name__ = "Unsigned32"
_OsOneIpMngCfgStdFirstPort_Object = MibTableColumn
osOneIpMngCfgStdFirstPort = _OsOneIpMngCfgStdFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 4),
    _OsOneIpMngCfgStdFirstPort_Type()
)
osOneIpMngCfgStdFirstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgStdFirstPort.setStatus("current")


class _OsOneIpMngCfgStdLastPort_Type(Unsigned32):
    """Custom type osOneIpMngCfgStdLastPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsOneIpMngCfgStdLastPort_Type.__name__ = "Unsigned32"
_OsOneIpMngCfgStdLastPort_Object = MibTableColumn
osOneIpMngCfgStdLastPort = _OsOneIpMngCfgStdLastPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 5),
    _OsOneIpMngCfgStdLastPort_Type()
)
osOneIpMngCfgStdLastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgStdLastPort.setStatus("current")


class _OsOneIpMngCfgAltFirstPort_Type(Unsigned32):
    """Custom type osOneIpMngCfgAltFirstPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsOneIpMngCfgAltFirstPort_Type.__name__ = "Unsigned32"
_OsOneIpMngCfgAltFirstPort_Object = MibTableColumn
osOneIpMngCfgAltFirstPort = _OsOneIpMngCfgAltFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 6),
    _OsOneIpMngCfgAltFirstPort_Type()
)
osOneIpMngCfgAltFirstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgAltFirstPort.setStatus("current")


class _OsOneIpMngCfgAltLastPort_Type(Unsigned32):
    """Custom type osOneIpMngCfgAltLastPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsOneIpMngCfgAltLastPort_Type.__name__ = "Unsigned32"
_OsOneIpMngCfgAltLastPort_Object = MibTableColumn
osOneIpMngCfgAltLastPort = _OsOneIpMngCfgAltLastPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 7),
    _OsOneIpMngCfgAltLastPort_Type()
)
osOneIpMngCfgAltLastPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgAltLastPort.setStatus("current")


class _OsOneIpMngCfgOperStatus_Type(Integer32):
    """Custom type osOneIpMngCfgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultOriginal", 1),
          ("defaultModified", 2),
          ("hotDefault", 3))
    )


_OsOneIpMngCfgOperStatus_Type.__name__ = "Integer32"
_OsOneIpMngCfgOperStatus_Object = MibTableColumn
osOneIpMngCfgOperStatus = _OsOneIpMngCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 98),
    _OsOneIpMngCfgOperStatus_Type()
)
osOneIpMngCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOneIpMngCfgOperStatus.setStatus("current")


class _OsOneIpMngCfgAdminStatus_Type(Integer32):
    """Custom type osOneIpMngCfgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_OsOneIpMngCfgAdminStatus_Type.__name__ = "Integer32"
_OsOneIpMngCfgAdminStatus_Object = MibTableColumn
osOneIpMngCfgAdminStatus = _OsOneIpMngCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 1, 3, 1, 99),
    _OsOneIpMngCfgAdminStatus_Type()
)
osOneIpMngCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpMngCfgAdminStatus.setStatus("current")
_OsOneIpMngNatGlb_ObjectIdentity = ObjectIdentity
osOneIpMngNatGlb = _OsOneIpMngNatGlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 2)
)


class _OsOneIpManagFeatOpStatus_Type(Integer32):
    """Custom type osOneIpManagFeatOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_OsOneIpManagFeatOpStatus_Type.__name__ = "Integer32"
_OsOneIpManagFeatOpStatus_Object = MibScalar
osOneIpManagFeatOpStatus = _OsOneIpManagFeatOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 1, 2, 1),
    _OsOneIpManagFeatOpStatus_Type()
)
osOneIpManagFeatOpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osOneIpManagFeatOpStatus.setStatus("current")
_OsOneIpMngNatConformance_ObjectIdentity = ObjectIdentity
osOneIpMngNatConformance = _OsOneIpMngNatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 101)
)
_OsOneIpMngNatMIBCompliances_ObjectIdentity = ObjectIdentity
osOneIpMngNatMIBCompliances = _OsOneIpMngNatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 101, 1)
)
_OsOneIpMngNatMIBGroups_ObjectIdentity = ObjectIdentity
osOneIpMngNatMIBGroups = _OsOneIpMngNatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 101, 2)
)

# Managed Objects groups

osOneIpMngNatMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 101, 2, 1)
)
osOneIpMngNatMandatoryGroup.setObjects(
      *(("OS-ONE-IP-MIB", "osOneIpManagFeatOpStatus"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefTransport"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefListType"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefStdFirstPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefStdLastPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefAltFirstPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefAltLastPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngDefOperStatus"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgTransport"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgListType"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgStdFirstPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgStdLastPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgAltFirstPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgAltLastPort"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgOperStatus"),
        ("OS-ONE-IP-MIB", "osOneIpMngCfgAdminStatus"))
)
if mibBuilder.loadTexts:
    osOneIpMngNatMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osOneIpMngNatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 43, 101, 1, 1)
)
osOneIpMngNatMIBCompliance.setObjects(
    ("OS-ONE-IP-MIB", "osOneIpMngNatMandatoryGroup")
)
if mibBuilder.loadTexts:
    osOneIpMngNatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-ONE-IP-MIB",
    **{"osOneIpMng": osOneIpMng,
       "osOneIpMngNat": osOneIpMngNat,
       "osOneIpMngNatGen": osOneIpMngNatGen,
       "osOneIpMngDefaultTable": osOneIpMngDefaultTable,
       "osOneIpMngDefaultEntry": osOneIpMngDefaultEntry,
       "osOneIpMngDefName": osOneIpMngDefName,
       "osOneIpMngDefTransport": osOneIpMngDefTransport,
       "osOneIpMngDefListType": osOneIpMngDefListType,
       "osOneIpMngDefStdFirstPort": osOneIpMngDefStdFirstPort,
       "osOneIpMngDefStdLastPort": osOneIpMngDefStdLastPort,
       "osOneIpMngDefAltFirstPort": osOneIpMngDefAltFirstPort,
       "osOneIpMngDefAltLastPort": osOneIpMngDefAltLastPort,
       "osOneIpMngDefOperStatus": osOneIpMngDefOperStatus,
       "osOneIpMngProtoTable": osOneIpMngProtoTable,
       "osOneIpMngProtoEntry": osOneIpMngProtoEntry,
       "osOneIpMngCfgName": osOneIpMngCfgName,
       "osOneIpMngCfgTransport": osOneIpMngCfgTransport,
       "osOneIpMngCfgListType": osOneIpMngCfgListType,
       "osOneIpMngCfgStdFirstPort": osOneIpMngCfgStdFirstPort,
       "osOneIpMngCfgStdLastPort": osOneIpMngCfgStdLastPort,
       "osOneIpMngCfgAltFirstPort": osOneIpMngCfgAltFirstPort,
       "osOneIpMngCfgAltLastPort": osOneIpMngCfgAltLastPort,
       "osOneIpMngCfgOperStatus": osOneIpMngCfgOperStatus,
       "osOneIpMngCfgAdminStatus": osOneIpMngCfgAdminStatus,
       "osOneIpMngNatGlb": osOneIpMngNatGlb,
       "osOneIpManagFeatOpStatus": osOneIpManagFeatOpStatus,
       "osOneIpMngNatConformance": osOneIpMngNatConformance,
       "osOneIpMngNatMIBCompliances": osOneIpMngNatMIBCompliances,
       "osOneIpMngNatMIBCompliance": osOneIpMngNatMIBCompliance,
       "osOneIpMngNatMIBGroups": osOneIpMngNatMIBGroups,
       "osOneIpMngNatMandatoryGroup": osOneIpMngNatMandatoryGroup}
)
