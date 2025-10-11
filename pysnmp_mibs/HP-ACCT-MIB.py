# SNMP MIB module (HP-ACCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ACCT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:08 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpSwitchAccountingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17)
)
if mibBuilder.loadTexts:
    hpSwitchAccountingMIB.setRevisions(
        ("2019-09-26 00:00",
         "2017-11-22 00:00",
         "2014-08-04 00:00",
         "2011-03-05 00:00",
         "2009-07-14 00:00",
         "2008-07-11 00:00",
         "2001-08-22 02:38")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchAccountingConfig_ObjectIdentity = ObjectIdentity
hpSwitchAccountingConfig = _HpSwitchAccountingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1)
)


class _HpSwitchAcctUpdateInterval_Type(Integer32):
    """Custom type hpSwitchAcctUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_HpSwitchAcctUpdateInterval_Type.__name__ = "Integer32"
_HpSwitchAcctUpdateInterval_Object = MibScalar
hpSwitchAcctUpdateInterval = _HpSwitchAcctUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 1),
    _HpSwitchAcctUpdateInterval_Type()
)
hpSwitchAcctUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctUpdateInterval.setStatus("current")


class _HpSwitchAcctSuppressNullUserName_Type(Integer32):
    """Custom type hpSwitchAcctSuppressNullUserName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HpSwitchAcctSuppressNullUserName_Type.__name__ = "Integer32"
_HpSwitchAcctSuppressNullUserName_Object = MibScalar
hpSwitchAcctSuppressNullUserName = _HpSwitchAcctSuppressNullUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 2),
    _HpSwitchAcctSuppressNullUserName_Type()
)
hpSwitchAcctSuppressNullUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctSuppressNullUserName.setStatus("current")


class _HpSwitchAcctSessionIdentification_Type(Integer32):
    """Custom type hpSwitchAcctSessionIdentification based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unique", 1),
          ("common", 2))
    )


_HpSwitchAcctSessionIdentification_Type.__name__ = "Integer32"
_HpSwitchAcctSessionIdentification_Object = MibScalar
hpSwitchAcctSessionIdentification = _HpSwitchAcctSessionIdentification_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 3),
    _HpSwitchAcctSessionIdentification_Type()
)
hpSwitchAcctSessionIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctSessionIdentification.setStatus("current")


class _HpSwitchAcctSessIdIncSwitchIdentity_Type(Integer32):
    """Custom type hpSwitchAcctSessIdIncSwitchIdentity based on Integer32"""
    defaultValue = 2

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


_HpSwitchAcctSessIdIncSwitchIdentity_Type.__name__ = "Integer32"
_HpSwitchAcctSessIdIncSwitchIdentity_Object = MibScalar
hpSwitchAcctSessIdIncSwitchIdentity = _HpSwitchAcctSessIdIncSwitchIdentity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 4),
    _HpSwitchAcctSessIdIncSwitchIdentity_Type()
)
hpSwitchAcctSessIdIncSwitchIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctSessIdIncSwitchIdentity.setStatus("current")
_HpSwitchAcctServiceTable_Object = MibTable
hpSwitchAcctServiceTable = _HpSwitchAcctServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2)
)
if mibBuilder.loadTexts:
    hpSwitchAcctServiceTable.setStatus("current")
_HpSwitchAcctServiceEntry_Object = MibTableRow
hpSwitchAcctServiceEntry = _HpSwitchAcctServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1)
)
hpSwitchAcctServiceEntry.setIndexNames(
    (0, "HP-ACCT-MIB", "hpSwitchAcctServiceIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchAcctServiceEntry.setStatus("current")


class _HpSwitchAcctServiceIndex_Type(Integer32):
    """Custom type hpSwitchAcctServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("exec", 2),
          ("system", 3),
          ("commands", 4),
          ("restUri", 5))
    )


_HpSwitchAcctServiceIndex_Type.__name__ = "Integer32"
_HpSwitchAcctServiceIndex_Object = MibTableColumn
hpSwitchAcctServiceIndex = _HpSwitchAcctServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 1),
    _HpSwitchAcctServiceIndex_Type()
)
hpSwitchAcctServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAcctServiceIndex.setStatus("current")


class _HpSwitchAcctServiceMethod_Type(Integer32):
    """Custom type hpSwitchAcctServiceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("radius", 2),
          ("syslog", 3),
          ("tacacs", 4))
    )


_HpSwitchAcctServiceMethod_Type.__name__ = "Integer32"
_HpSwitchAcctServiceMethod_Object = MibTableColumn
hpSwitchAcctServiceMethod = _HpSwitchAcctServiceMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 2),
    _HpSwitchAcctServiceMethod_Type()
)
hpSwitchAcctServiceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctServiceMethod.setStatus("current")


class _HpSwitchAcctServiceMode_Type(Integer32):
    """Custom type hpSwitchAcctServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startStop", 2),
          ("stopOnly", 3),
          ("interimUpdate", 4))
    )


_HpSwitchAcctServiceMode_Type.__name__ = "Integer32"
_HpSwitchAcctServiceMode_Object = MibTableColumn
hpSwitchAcctServiceMode = _HpSwitchAcctServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 3),
    _HpSwitchAcctServiceMode_Type()
)
hpSwitchAcctServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctServiceMode.setStatus("current")


class _HpSwitchAcctServiceServerGroupName_Type(DisplayString):
    """Custom type hpSwitchAcctServiceServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAcctServiceServerGroupName_Type.__name__ = "DisplayString"
_HpSwitchAcctServiceServerGroupName_Object = MibTableColumn
hpSwitchAcctServiceServerGroupName = _HpSwitchAcctServiceServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 4),
    _HpSwitchAcctServiceServerGroupName_Type()
)
hpSwitchAcctServiceServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAcctServiceServerGroupName.setStatus("current")
_HpSwitchAccountingMIBConformance_ObjectIdentity = ObjectIdentity
hpSwitchAccountingMIBConformance = _HpSwitchAccountingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3)
)
_HpSwitchAccountingMIBCompliances_ObjectIdentity = ObjectIdentity
hpSwitchAccountingMIBCompliances = _HpSwitchAccountingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1)
)
_HpSwitchAccountingMIBGroups_ObjectIdentity = ObjectIdentity
hpSwitchAccountingMIBGroups = _HpSwitchAccountingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2)
)

# Managed Objects groups

hpSwitchAccountingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2, 1)
)
hpSwitchAccountingConfigGroup.setObjects(
      *(("HP-ACCT-MIB", "hpSwitchAcctUpdateInterval"),
        ("HP-ACCT-MIB", "hpSwitchAcctSuppressNullUserName"),
        ("HP-ACCT-MIB", "hpSwitchAcctSessionIdentification"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceMethod"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceMode"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceServerGroupName"))
)
if mibBuilder.loadTexts:
    hpSwitchAccountingConfigGroup.setStatus("deprecated")

hpSwitchAccountingConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2, 2)
)
hpSwitchAccountingConfigGroup1.setObjects(
      *(("HP-ACCT-MIB", "hpSwitchAcctUpdateInterval"),
        ("HP-ACCT-MIB", "hpSwitchAcctSuppressNullUserName"),
        ("HP-ACCT-MIB", "hpSwitchAcctSessionIdentification"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceMethod"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceMode"),
        ("HP-ACCT-MIB", "hpSwitchAcctServiceServerGroupName"),
        ("HP-ACCT-MIB", "hpSwitchAcctSessIdIncSwitchIdentity"))
)
if mibBuilder.loadTexts:
    hpSwitchAccountingConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchAccountingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1, 1)
)
hpSwitchAccountingMIBCompliance.setObjects(
    ("HP-ACCT-MIB", "hpSwitchAccountingConfigGroup")
)
if mibBuilder.loadTexts:
    hpSwitchAccountingMIBCompliance.setStatus(
        "deprecated"
    )

hpSwitchAccountingMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1, 2)
)
hpSwitchAccountingMIBCompliance1.setObjects(
    ("HP-ACCT-MIB", "hpSwitchAccountingConfigGroup1")
)
if mibBuilder.loadTexts:
    hpSwitchAccountingMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ACCT-MIB",
    **{"hpSwitchAccountingMIB": hpSwitchAccountingMIB,
       "hpSwitchAccountingConfig": hpSwitchAccountingConfig,
       "hpSwitchAcctUpdateInterval": hpSwitchAcctUpdateInterval,
       "hpSwitchAcctSuppressNullUserName": hpSwitchAcctSuppressNullUserName,
       "hpSwitchAcctSessionIdentification": hpSwitchAcctSessionIdentification,
       "hpSwitchAcctSessIdIncSwitchIdentity": hpSwitchAcctSessIdIncSwitchIdentity,
       "hpSwitchAcctServiceTable": hpSwitchAcctServiceTable,
       "hpSwitchAcctServiceEntry": hpSwitchAcctServiceEntry,
       "hpSwitchAcctServiceIndex": hpSwitchAcctServiceIndex,
       "hpSwitchAcctServiceMethod": hpSwitchAcctServiceMethod,
       "hpSwitchAcctServiceMode": hpSwitchAcctServiceMode,
       "hpSwitchAcctServiceServerGroupName": hpSwitchAcctServiceServerGroupName,
       "hpSwitchAccountingMIBConformance": hpSwitchAccountingMIBConformance,
       "hpSwitchAccountingMIBCompliances": hpSwitchAccountingMIBCompliances,
       "hpSwitchAccountingMIBCompliance": hpSwitchAccountingMIBCompliance,
       "hpSwitchAccountingMIBCompliance1": hpSwitchAccountingMIBCompliance1,
       "hpSwitchAccountingMIBGroups": hpSwitchAccountingMIBGroups,
       "hpSwitchAccountingConfigGroup": hpSwitchAccountingConfigGroup,
       "hpSwitchAccountingConfigGroup1": hpSwitchAccountingConfigGroup1}
)
