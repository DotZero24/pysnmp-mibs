_F='ciscoThrottleGroup'
_E='cniThrottleCount'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='CISCO-NETINT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoNetintMIB=ModuleIdentity((1,3,6,1,4,1,9,9,490))
if mibBuilder.loadTexts:ciscoNetintMIB.setRevisions(('2005-09-26 00:00',))
_CiscoNetintMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNetintMIBNotifs=_CiscoNetintMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,490,0))
_CiscoNetintMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNetintMIBObjects=_CiscoNetintMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,490,1))
_CniThrottle_ObjectIdentity=ObjectIdentity
cniThrottle=_CniThrottle_ObjectIdentity((1,3,6,1,4,1,9,9,490,1,1))
_CniThrottleTable_Object=MibTable
cniThrottleTable=_CniThrottleTable_Object((1,3,6,1,4,1,9,9,490,1,1,1))
if mibBuilder.loadTexts:cniThrottleTable.setStatus(_A)
_CniThrottleEntry_Object=MibTableRow
cniThrottleEntry=_CniThrottleEntry_Object((1,3,6,1,4,1,9,9,490,1,1,1,1))
cniThrottleEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cniThrottleEntry.setStatus(_A)
_CniThrottleCount_Type=Counter32
_CniThrottleCount_Object=MibTableColumn
cniThrottleCount=_CniThrottleCount_Object((1,3,6,1,4,1,9,9,490,1,1,1,1,1),_CniThrottleCount_Type())
cniThrottleCount.setMaxAccess('read-only')
if mibBuilder.loadTexts:cniThrottleCount.setStatus(_A)
_CiscoNetintMIBConformance_ObjectIdentity=ObjectIdentity
ciscoNetintMIBConformance=_CiscoNetintMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,490,2))
_CiscoNetintMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNetintMIBCompliances=_CiscoNetintMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,490,2,1))
_CiscoNetintMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNetintMIBGroups=_CiscoNetintMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,490,2,2))
ciscoThrottleGroup=ObjectGroup((1,3,6,1,4,1,9,9,490,2,2,1))
ciscoThrottleGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:ciscoThrottleGroup.setStatus(_A)
ciscoNetintMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,490,2,1,1))
ciscoNetintMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoNetintMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNetintMIB':ciscoNetintMIB,'ciscoNetintMIBNotifs':ciscoNetintMIBNotifs,'ciscoNetintMIBObjects':ciscoNetintMIBObjects,'cniThrottle':cniThrottle,'cniThrottleTable':cniThrottleTable,'cniThrottleEntry':cniThrottleEntry,_E:cniThrottleCount,'ciscoNetintMIBConformance':ciscoNetintMIBConformance,'ciscoNetintMIBCompliances':ciscoNetintMIBCompliances,'ciscoNetintMIBCompliance':ciscoNetintMIBCompliance,'ciscoNetintMIBGroups':ciscoNetintMIBGroups,_F:ciscoThrottleGroup})