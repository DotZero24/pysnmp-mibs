# SNMP MIB module (MX-LQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-LQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:35 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

lQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LQosMIBObjects_ObjectIdentity = ObjectIdentity
lQosMIBObjects = _LQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1)
)


class _DefaultDiffServ_Type(Unsigned32):
    """Custom type defaultDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultDiffServ_Type.__name__ = "Unsigned32"
_DefaultDiffServ_Object = MibScalar
defaultDiffServ = _DefaultDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 100),
    _DefaultDiffServ_Type()
)
defaultDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDiffServ.setStatus("current")


class _DefaultTrafficClass_Type(Unsigned32):
    """Custom type defaultTrafficClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultTrafficClass_Type.__name__ = "Unsigned32"
_DefaultTrafficClass_Object = MibScalar
defaultTrafficClass = _DefaultTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 150),
    _DefaultTrafficClass_Type()
)
defaultTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultTrafficClass.setStatus("current")
_Ethernet8021QTaggingTable_Object = MibTable
ethernet8021QTaggingTable = _Ethernet8021QTaggingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 200)
)
if mibBuilder.loadTexts:
    ethernet8021QTaggingTable.setStatus("current")
_Ethernet8021QTaggingEntry_Object = MibTableRow
ethernet8021QTaggingEntry = _Ethernet8021QTaggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 200, 1)
)
ethernet8021QTaggingEntry.setIndexNames(
    (0, "MX-LQOS-MIB", "ethernet8021QTaggingInterfaceName"),
)
if mibBuilder.loadTexts:
    ethernet8021QTaggingEntry.setStatus("current")
_Ethernet8021QTaggingInterfaceName_Type = OctetString
_Ethernet8021QTaggingInterfaceName_Object = MibTableColumn
ethernet8021QTaggingInterfaceName = _Ethernet8021QTaggingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 200, 1, 100),
    _Ethernet8021QTaggingInterfaceName_Type()
)
ethernet8021QTaggingInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernet8021QTaggingInterfaceName.setStatus("current")


class _Ethernet8021QTaggingEnablePriorityTagging_Type(MxEnableState):
    """Custom type ethernet8021QTaggingEnablePriorityTagging based on MxEnableState"""
    defaultValue = 0


_Ethernet8021QTaggingEnablePriorityTagging_Type.__name__ = "MxEnableState"
_Ethernet8021QTaggingEnablePriorityTagging_Object = MibTableColumn
ethernet8021QTaggingEnablePriorityTagging = _Ethernet8021QTaggingEnablePriorityTagging_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 200, 1, 200),
    _Ethernet8021QTaggingEnablePriorityTagging_Type()
)
ethernet8021QTaggingEnablePriorityTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet8021QTaggingEnablePriorityTagging.setStatus("current")


class _Ethernet8021QTaggingDefaultUserPriority_Type(Unsigned32):
    """Custom type ethernet8021QTaggingDefaultUserPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ethernet8021QTaggingDefaultUserPriority_Type.__name__ = "Unsigned32"
_Ethernet8021QTaggingDefaultUserPriority_Object = MibTableColumn
ethernet8021QTaggingDefaultUserPriority = _Ethernet8021QTaggingDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 200, 1, 300),
    _Ethernet8021QTaggingDefaultUserPriority_Type()
)
ethernet8021QTaggingDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernet8021QTaggingDefaultUserPriority.setStatus("current")
_ServiceClassesTable_Object = MibTable
serviceClassesTable = _ServiceClassesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300)
)
if mibBuilder.loadTexts:
    serviceClassesTable.setStatus("current")
_ServiceClassesEntry_Object = MibTableRow
serviceClassesEntry = _ServiceClassesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1)
)
serviceClassesEntry.setIndexNames(
    (0, "MX-LQOS-MIB", "serviceClassesId"),
)
if mibBuilder.loadTexts:
    serviceClassesEntry.setStatus("current")
_ServiceClassesId_Type = Unsigned32
_ServiceClassesId_Object = MibTableColumn
serviceClassesId = _ServiceClassesId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1, 100),
    _ServiceClassesId_Type()
)
serviceClassesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceClassesId.setStatus("current")


class _ServiceClassesDescription_Type(OctetString):
    """Custom type serviceClassesDescription based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ServiceClassesDescription_Type.__name__ = "OctetString"
_ServiceClassesDescription_Object = MibTableColumn
serviceClassesDescription = _ServiceClassesDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1, 200),
    _ServiceClassesDescription_Type()
)
serviceClassesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceClassesDescription.setStatus("current")


class _ServiceClassesDiffServ_Type(Unsigned32):
    """Custom type serviceClassesDiffServ based on Unsigned32"""
    defaultValue = 184

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ServiceClassesDiffServ_Type.__name__ = "Unsigned32"
_ServiceClassesDiffServ_Object = MibTableColumn
serviceClassesDiffServ = _ServiceClassesDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1, 300),
    _ServiceClassesDiffServ_Type()
)
serviceClassesDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassesDiffServ.setStatus("current")


class _ServiceClassesTrafficClass_Type(Unsigned32):
    """Custom type serviceClassesTrafficClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ServiceClassesTrafficClass_Type.__name__ = "Unsigned32"
_ServiceClassesTrafficClass_Object = MibTableColumn
serviceClassesTrafficClass = _ServiceClassesTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1, 350),
    _ServiceClassesTrafficClass_Type()
)
serviceClassesTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassesTrafficClass.setStatus("current")


class _ServiceClassesUserPriority_Type(Unsigned32):
    """Custom type serviceClassesUserPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ServiceClassesUserPriority_Type.__name__ = "Unsigned32"
_ServiceClassesUserPriority_Object = MibTableColumn
serviceClassesUserPriority = _ServiceClassesUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 300, 1, 400),
    _ServiceClassesUserPriority_Type()
)
serviceClassesUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceClassesUserPriority.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2500, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-LQOS-MIB",
    **{"lQosMIB": lQosMIB,
       "lQosMIBObjects": lQosMIBObjects,
       "defaultDiffServ": defaultDiffServ,
       "defaultTrafficClass": defaultTrafficClass,
       "ethernet8021QTaggingTable": ethernet8021QTaggingTable,
       "ethernet8021QTaggingEntry": ethernet8021QTaggingEntry,
       "ethernet8021QTaggingInterfaceName": ethernet8021QTaggingInterfaceName,
       "ethernet8021QTaggingEnablePriorityTagging": ethernet8021QTaggingEnablePriorityTagging,
       "ethernet8021QTaggingDefaultUserPriority": ethernet8021QTaggingDefaultUserPriority,
       "serviceClassesTable": serviceClassesTable,
       "serviceClassesEntry": serviceClassesEntry,
       "serviceClassesId": serviceClassesId,
       "serviceClassesDescription": serviceClassesDescription,
       "serviceClassesDiffServ": serviceClassesDiffServ,
       "serviceClassesTrafficClass": serviceClassesTrafficClass,
       "serviceClassesUserPriority": serviceClassesUserPriority,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
