# SNMP MIB module (HM2-TSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-TSN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:21 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(ieee8021STParametersEntry,) = mibBuilder.importSymbols(
    "IEEE8021-ST-MIB",
    "ieee8021STParametersEntry")

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

hm2TsnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51)
)
if mibBuilder.loadTexts:
    hm2TsnMib.setRevisions(
        ("2018-02-06 00:00",
         "2021-02-19 00:00",
         "2021-03-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2TsnBaseTime(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11



# MIB Managed Objects in the order of their OIDs

_Hm2TsnNotifications_ObjectIdentity = ObjectIdentity
hm2TsnNotifications = _Hm2TsnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 0)
)
_Hm2TsnMibObjects_ObjectIdentity = ObjectIdentity
hm2TsnMibObjects = _Hm2TsnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1)
)
_Hm2TsnGroup_ObjectIdentity = ObjectIdentity
hm2TsnGroup = _Hm2TsnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 1)
)


class _Hm2TsnAdminState_Type(HmEnabledStatus):
    """Custom type hm2TsnAdminState based on HmEnabledStatus"""
    defaultValue = 2


_Hm2TsnAdminState_Type.__name__ = "HmEnabledStatus"
_Hm2TsnAdminState_Object = MibScalar
hm2TsnAdminState = _Hm2TsnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 1, 1),
    _Hm2TsnAdminState_Type()
)
hm2TsnAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TsnAdminState.setStatus("current")
_Hm2STParametersTable_Object = MibTable
hm2STParametersTable = _Hm2STParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2)
)
if mibBuilder.loadTexts:
    hm2STParametersTable.setStatus("current")
_Hm2STParametersEntry_Object = MibTableRow
hm2STParametersEntry = _Hm2STParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2STParametersEntry.setStatus("current")
_Hm2STAdminBaseTime_Type = Hm2TsnBaseTime
_Hm2STAdminBaseTime_Object = MibTableColumn
hm2STAdminBaseTime = _Hm2STAdminBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2, 1, 1),
    _Hm2STAdminBaseTime_Type()
)
hm2STAdminBaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2STAdminBaseTime.setStatus("current")
_Hm2STOperBaseTime_Type = Hm2TsnBaseTime
_Hm2STOperBaseTime_Object = MibTableColumn
hm2STOperBaseTime = _Hm2STOperBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2, 1, 2),
    _Hm2STOperBaseTime_Type()
)
hm2STOperBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2STOperBaseTime.setStatus("current")
_Hm2STConfigChangeTime_Type = Hm2TsnBaseTime
_Hm2STConfigChangeTime_Object = MibTableColumn
hm2STConfigChangeTime = _Hm2STConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2, 1, 3),
    _Hm2STConfigChangeTime_Type()
)
hm2STConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2STConfigChangeTime.setStatus("current")


class _Hm2STPortStatus_Type(Integer32):
    """Custom type hm2STPortStatus based on Integer32"""
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
        *(("running", 1),
          ("waitForTimeSync", 2),
          ("pending", 3),
          ("disabled", 4),
          ("error", 5))
    )


_Hm2STPortStatus_Type.__name__ = "Integer32"
_Hm2STPortStatus_Object = MibTableColumn
hm2STPortStatus = _Hm2STPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 2, 1, 4),
    _Hm2STPortStatus_Type()
)
hm2STPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2STPortStatus.setStatus("current")
_Hm2TsnTemplateBasedGroup_ObjectIdentity = ObjectIdentity
hm2TsnTemplateBasedGroup = _Hm2TsnTemplateBasedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 3)
)
_Hm2TsnTemplateBasedParametersTable_Object = MibTable
hm2TsnTemplateBasedParametersTable = _Hm2TsnTemplateBasedParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2TsnTemplateBasedParametersTable.setStatus("current")
_Hm2TsnTemplateBasedParametersEntry_Object = MibTableRow
hm2TsnTemplateBasedParametersEntry = _Hm2TsnTemplateBasedParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2TsnTemplateBasedParametersEntry.setStatus("current")


class _Hm2TsnAdminTemplateGcl_Type(Integer32):
    """Custom type hm2TsnAdminTemplateGcl based on Integer32"""
    defaultValue = 1

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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("tc7Tc6to0Gb", 2),
          ("gbTc7Tc6to0", 3),
          ("tc6to0GbTc7", 4),
          ("gbTc7GbTc6Tc5to0", 5),
          ("tc5to0GbTc7GbTc6", 6),
          ("gbTc6GbTc7Tc5to0", 7),
          ("gbTc7Tc5to0GbTc6", 8),
          ("tc7GbTc6Tc5to0Gb", 9))
    )


_Hm2TsnAdminTemplateGcl_Type.__name__ = "Integer32"
_Hm2TsnAdminTemplateGcl_Object = MibTableColumn
hm2TsnAdminTemplateGcl = _Hm2TsnAdminTemplateGcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 3, 1, 1, 1),
    _Hm2TsnAdminTemplateGcl_Type()
)
hm2TsnAdminTemplateGcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2TsnAdminTemplateGcl.setStatus("current")


class _Hm2TsnOperTemplateGcl_Type(Integer32):
    """Custom type hm2TsnOperTemplateGcl based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noTemplate", 1),
          ("tc7Tc6to0Gb", 2),
          ("gbTc7Tc6to0", 3),
          ("tc6to0GbTc7", 4),
          ("gbTc7GbTc6Tc5to0", 5),
          ("tc5to0GbTc7GbTc6", 6),
          ("gbTc6GbTc7Tc5to0", 7),
          ("gbTc7Tc5to0GbTc6", 8),
          ("tc7GbTc6Tc5to0Gb", 9))
    )


_Hm2TsnOperTemplateGcl_Type.__name__ = "Integer32"
_Hm2TsnOperTemplateGcl_Object = MibTableColumn
hm2TsnOperTemplateGcl = _Hm2TsnOperTemplateGcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 1, 3, 1, 1, 2),
    _Hm2TsnOperTemplateGcl_Type()
)
hm2TsnOperTemplateGcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2TsnOperTemplateGcl.setStatus("current")
_Hm2TsnMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2TsnMibSNMPExtensionGroup = _Hm2TsnMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 3)
)
_Hm2TsnConflictMibSESGroup_ObjectIdentity = ObjectIdentity
hm2TsnConflictMibSESGroup = _Hm2TsnConflictMibSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 3, 1)
)
_Hm2TsnGranulaityConflict_ObjectIdentity = ObjectIdentity
hm2TsnGranulaityConflict = _Hm2TsnGranulaityConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2TsnGranulaityConflict.setStatus("current")
_Hm2TsnGCLTimeIntervalConflit_ObjectIdentity = ObjectIdentity
hm2TsnGCLTimeIntervalConflit = _Hm2TsnGCLTimeIntervalConflit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hm2TsnGCLTimeIntervalConflit.setStatus("current")
_Hm2TsnGCLTemplateConflict_ObjectIdentity = ObjectIdentity
hm2TsnGCLTemplateConflict = _Hm2TsnGCLTemplateConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 51, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hm2TsnGCLTemplateConflict.setStatus("current")
ieee8021STParametersEntry.registerAugmentions(
    ("HM2-TSN-MIB",
     "hm2STParametersEntry")
)
hm2STParametersEntry.setIndexNames(*ieee8021STParametersEntry.getIndexNames())
ieee8021STParametersEntry.registerAugmentions(
    ("HM2-TSN-MIB",
     "hm2TsnTemplateBasedParametersEntry")
)
hm2TsnTemplateBasedParametersEntry.setIndexNames(*ieee8021STParametersEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-TSN-MIB",
    **{"Hm2TsnBaseTime": Hm2TsnBaseTime,
       "hm2TsnMib": hm2TsnMib,
       "hm2TsnNotifications": hm2TsnNotifications,
       "hm2TsnMibObjects": hm2TsnMibObjects,
       "hm2TsnGroup": hm2TsnGroup,
       "hm2TsnAdminState": hm2TsnAdminState,
       "hm2STParametersTable": hm2STParametersTable,
       "hm2STParametersEntry": hm2STParametersEntry,
       "hm2STAdminBaseTime": hm2STAdminBaseTime,
       "hm2STOperBaseTime": hm2STOperBaseTime,
       "hm2STConfigChangeTime": hm2STConfigChangeTime,
       "hm2STPortStatus": hm2STPortStatus,
       "hm2TsnTemplateBasedGroup": hm2TsnTemplateBasedGroup,
       "hm2TsnTemplateBasedParametersTable": hm2TsnTemplateBasedParametersTable,
       "hm2TsnTemplateBasedParametersEntry": hm2TsnTemplateBasedParametersEntry,
       "hm2TsnAdminTemplateGcl": hm2TsnAdminTemplateGcl,
       "hm2TsnOperTemplateGcl": hm2TsnOperTemplateGcl,
       "hm2TsnMibSNMPExtensionGroup": hm2TsnMibSNMPExtensionGroup,
       "hm2TsnConflictMibSESGroup": hm2TsnConflictMibSESGroup,
       "hm2TsnGranulaityConflict": hm2TsnGranulaityConflict,
       "hm2TsnGCLTimeIntervalConflit": hm2TsnGCLTimeIntervalConflit,
       "hm2TsnGCLTemplateConflict": hm2TsnGCLTemplateConflict}
)
