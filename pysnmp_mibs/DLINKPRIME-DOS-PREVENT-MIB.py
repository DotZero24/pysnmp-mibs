# SNMP MIB module (DLINKPRIME-DOS-PREVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-DOS-PREVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:34 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeDosPrevMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4)
)
if mibBuilder.loadTexts:
    dlinkPrimeDosPrevMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DosAttackType(TextualConvention, Integer32):
    status = "current"
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("landAttack", 1),
          ("blatAttack", 2),
          ("tcpNullScan", 3),
          ("tcpXmasScan", 4),
          ("tcpSynFin", 5),
          ("tcpSynSrcPortLess1024", 6),
          ("pingDeathAttack", 7),
          ("all", 99))
    )



# MIB Managed Objects in the order of their OIDs

_DpDosPrevMIBNotifications_ObjectIdentity = ObjectIdentity
dpDosPrevMIBNotifications = _DpDosPrevMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 0)
)
_DpDosPrevMIBObjects_ObjectIdentity = ObjectIdentity
dpDosPrevMIBObjects = _DpDosPrevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1)
)
_DpDosPrevCtrlTable_Object = MibTable
dpDosPrevCtrlTable = _DpDosPrevCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dpDosPrevCtrlTable.setStatus("current")
_DpDosPrevCtrlEntry_Object = MibTableRow
dpDosPrevCtrlEntry = _DpDosPrevCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1)
)
dpDosPrevCtrlEntry.setIndexNames(
    (0, "DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevCtrlAttackType"),
)
if mibBuilder.loadTexts:
    dpDosPrevCtrlEntry.setStatus("current")
_DpDosPrevCtrlAttackType_Type = DosAttackType
_DpDosPrevCtrlAttackType_Object = MibTableColumn
dpDosPrevCtrlAttackType = _DpDosPrevCtrlAttackType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 1),
    _DpDosPrevCtrlAttackType_Type()
)
dpDosPrevCtrlAttackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpDosPrevCtrlAttackType.setStatus("current")


class _DpDosPrevCtrlEnabled_Type(TruthValue):
    """Custom type dpDosPrevCtrlEnabled based on TruthValue"""
    defaultValue = 2


_DpDosPrevCtrlEnabled_Type.__name__ = "TruthValue"
_DpDosPrevCtrlEnabled_Object = MibTableColumn
dpDosPrevCtrlEnabled = _DpDosPrevCtrlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 2),
    _DpDosPrevCtrlEnabled_Type()
)
dpDosPrevCtrlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDosPrevCtrlEnabled.setStatus("current")


class _DpDosPrevCtrlActionType_Type(Integer32):
    """Custom type dpDosPrevCtrlActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("drop", 1)
    )


_DpDosPrevCtrlActionType_Type.__name__ = "Integer32"
_DpDosPrevCtrlActionType_Object = MibTableColumn
dpDosPrevCtrlActionType = _DpDosPrevCtrlActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 3),
    _DpDosPrevCtrlActionType_Type()
)
dpDosPrevCtrlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpDosPrevCtrlActionType.setStatus("current")
_DpDosPrevMIBConformance_ObjectIdentity = ObjectIdentity
dpDosPrevMIBConformance = _DpDosPrevMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 2)
)
_DpDosPrevMIBCompliances_ObjectIdentity = ObjectIdentity
dpDosPrevMIBCompliances = _DpDosPrevMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 1)
)
_DpDosPrevMIBGroups_ObjectIdentity = ObjectIdentity
dpDosPrevMIBGroups = _DpDosPrevMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 2)
)

# Managed Objects groups

dpDosPrevBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 2, 1)
)
dpDosPrevBasicGroup.setObjects(
    ("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevCtrlEnabled")
)
if mibBuilder.loadTexts:
    dpDosPrevBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpDosPrevMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 1, 1)
)
dpDosPrevMIBCompliance.setObjects(
      *(("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevBasicGroup"),
        ("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevActionRedirectCtrlGroup"))
)
if mibBuilder.loadTexts:
    dpDosPrevMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-DOS-PREVENT-MIB",
    **{"DosAttackType": DosAttackType,
       "dlinkPrimeDosPrevMIB": dlinkPrimeDosPrevMIB,
       "dpDosPrevMIBNotifications": dpDosPrevMIBNotifications,
       "dpDosPrevMIBObjects": dpDosPrevMIBObjects,
       "dpDosPrevCtrlTable": dpDosPrevCtrlTable,
       "dpDosPrevCtrlEntry": dpDosPrevCtrlEntry,
       "dpDosPrevCtrlAttackType": dpDosPrevCtrlAttackType,
       "dpDosPrevCtrlEnabled": dpDosPrevCtrlEnabled,
       "dpDosPrevCtrlActionType": dpDosPrevCtrlActionType,
       "dpDosPrevMIBConformance": dpDosPrevMIBConformance,
       "dpDosPrevMIBCompliances": dpDosPrevMIBCompliances,
       "dpDosPrevMIBCompliance": dpDosPrevMIBCompliance,
       "dpDosPrevMIBGroups": dpDosPrevMIBGroups,
       "dpDosPrevBasicGroup": dpDosPrevBasicGroup}
)
