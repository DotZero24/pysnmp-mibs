# SNMP MIB module (ADTRAN-AOS-Y1731-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-AOS-Y1731-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:20 2025
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

(adGenAOS,
 adGenAOSConformance,
 adGenAOSMef) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOS",
    "adGenAOSConformance",
    "adGenAOSMef")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex")

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

adGenAosY1731Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenAosY1731Alarms(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bDefY1731CcmRxRDIAlarm", 0),
          ("bDefY1731CcmLossOfContinuityAlarm", 1),
          ("bDefY1731CcmUnexpectedMepAlarm", 2),
          ("bDefY1731CcmUnexpectedPeriodAlarm", 3),
          ("bDefY1731CcmMismergeAlarm", 4),
          ("bDefY1731CcmUnexpectedMegLevelAlarm", 5))
    )


# MIB Managed Objects in the order of their OIDs

_AdGenAosY1731_ObjectIdentity = ObjectIdentity
adGenAosY1731 = _AdGenAosY1731_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9)
)
_AdGenAosY1731LocalMepTable_Object = MibTable
adGenAosY1731LocalMepTable = _AdGenAosY1731LocalMepTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1)
)
if mibBuilder.loadTexts:
    adGenAosY1731LocalMepTable.setStatus("current")
_AdGenAosY1731LocalMepEntry_Object = MibTableRow
adGenAosY1731LocalMepEntry = _AdGenAosY1731LocalMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1)
)
adGenAosY1731LocalMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "ADTRAN-AOS-Y1731-MIB", "adGenAosY1731LocalMepId"),
)
if mibBuilder.loadTexts:
    adGenAosY1731LocalMepEntry.setStatus("current")


class _AdGenAosY1731LocalMepId_Type(Unsigned32):
    """Custom type adGenAosY1731LocalMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenAosY1731LocalMepId_Type.__name__ = "Unsigned32"
_AdGenAosY1731LocalMepId_Object = MibTableColumn
adGenAosY1731LocalMepId = _AdGenAosY1731LocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1, 1),
    _AdGenAosY1731LocalMepId_Type()
)
adGenAosY1731LocalMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAosY1731LocalMepId.setStatus("current")
_AdGenAosY1731Alarms_Type = AdGenAosY1731Alarms
_AdGenAosY1731Alarms_Object = MibTableColumn
adGenAosY1731Alarms = _AdGenAosY1731Alarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1, 2),
    _AdGenAosY1731Alarms_Type()
)
adGenAosY1731Alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAosY1731Alarms.setStatus("current")
_AdGenAosY1731Conformance_ObjectIdentity = ObjectIdentity
adGenAosY1731Conformance = _AdGenAosY1731Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34)
)
_AdGenAosY1731Groups_ObjectIdentity = ObjectIdentity
adGenAosY1731Groups = _AdGenAosY1731Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 1)
)
_AdGenAosY1731Compliances_ObjectIdentity = ObjectIdentity
adGenAosY1731Compliances = _AdGenAosY1731Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 2)
)

# Managed Objects groups

adGenAosY1731Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 1, 1)
)
adGenAosY1731Group.setObjects(
    ("ADTRAN-AOS-Y1731-MIB", "adGenAosY1731Alarms")
)
if mibBuilder.loadTexts:
    adGenAosY1731Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosY1731FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 2, 1)
)
adGenAosY1731FullCompliance.setObjects(
    ("ADTRAN-AOS-Y1731-MIB", "adGenAosY1731Group")
)
if mibBuilder.loadTexts:
    adGenAosY1731FullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-Y1731-MIB",
    **{"AdGenAosY1731Alarms": AdGenAosY1731Alarms,
       "adGenAosY1731": adGenAosY1731,
       "adGenAosY1731LocalMepTable": adGenAosY1731LocalMepTable,
       "adGenAosY1731LocalMepEntry": adGenAosY1731LocalMepEntry,
       "adGenAosY1731LocalMepId": adGenAosY1731LocalMepId,
       "adGenAosY1731Alarms": adGenAosY1731Alarms,
       "adGenAosY1731Conformance": adGenAosY1731Conformance,
       "adGenAosY1731Groups": adGenAosY1731Groups,
       "adGenAosY1731Group": adGenAosY1731Group,
       "adGenAosY1731Compliances": adGenAosY1731Compliances,
       "adGenAosY1731FullCompliance": adGenAosY1731FullCompliance,
       "adGenAosY1731Mib": adGenAosY1731Mib}
)
