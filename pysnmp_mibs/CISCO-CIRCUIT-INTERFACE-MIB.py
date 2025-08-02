_I='ciscoCircuitInterfaceGroup'
_H='cciStatus'
_G='cciDescr'
_F='read-create'
_E='SnmpAdminString'
_D='ifIndex'
_C='IF-MIB'
_B='CISCO-CIRCUIT-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_C,_D)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoCircuitInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,160))
if mibBuilder.loadTexts:ciscoCircuitInterfaceMIB.setRevisions(('2000-05-09 00:00',))
_CiscoCircuitInterfaceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCircuitInterfaceMIBObjects=_CiscoCircuitInterfaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,160,1))
_CciDescription_ObjectIdentity=ObjectIdentity
cciDescription=_CciDescription_ObjectIdentity((1,3,6,1,4,1,9,9,160,1,1))
_CciDescriptionTable_Object=MibTable
cciDescriptionTable=_CciDescriptionTable_Object((1,3,6,1,4,1,9,9,160,1,1,1))
if mibBuilder.loadTexts:cciDescriptionTable.setStatus(_A)
_CciDescriptionEntry_Object=MibTableRow
cciDescriptionEntry=_CciDescriptionEntry_Object((1,3,6,1,4,1,9,9,160,1,1,1,1))
cciDescriptionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cciDescriptionEntry.setStatus(_A)
class _CciDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CciDescr_Type.__name__=_E
_CciDescr_Object=MibTableColumn
cciDescr=_CciDescr_Object((1,3,6,1,4,1,9,9,160,1,1,1,1,1),_CciDescr_Type())
cciDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:cciDescr.setStatus(_A)
_CciStatus_Type=RowStatus
_CciStatus_Object=MibTableColumn
cciStatus=_CciStatus_Object((1,3,6,1,4,1,9,9,160,1,1,1,1,2),_CciStatus_Type())
cciStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cciStatus.setStatus(_A)
_CiscoCircuitInterfaceMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCircuitInterfaceMIBConformance=_CiscoCircuitInterfaceMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,160,3))
_CiscoCircuitInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCircuitInterfaceMIBCompliances=_CiscoCircuitInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,160,3,1))
_CiscoCircuitInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCircuitInterfaceMIBGroups=_CiscoCircuitInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,160,3,2))
ciscoCircuitInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,160,3,2,1))
ciscoCircuitInterfaceGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:ciscoCircuitInterfaceGroup.setStatus(_A)
ciscoCircuitInterfaceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,160,3,1,1))
ciscoCircuitInterfaceMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoCircuitInterfaceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCircuitInterfaceMIB':ciscoCircuitInterfaceMIB,'ciscoCircuitInterfaceMIBObjects':ciscoCircuitInterfaceMIBObjects,'cciDescription':cciDescription,'cciDescriptionTable':cciDescriptionTable,'cciDescriptionEntry':cciDescriptionEntry,_G:cciDescr,_H:cciStatus,'ciscoCircuitInterfaceMIBConformance':ciscoCircuitInterfaceMIBConformance,'ciscoCircuitInterfaceMIBCompliances':ciscoCircuitInterfaceMIBCompliances,'ciscoCircuitInterfaceMIBCompliance':ciscoCircuitInterfaceMIBCompliance,'ciscoCircuitInterfaceMIBGroups':ciscoCircuitInterfaceMIBGroups,_I:ciscoCircuitInterfaceGroup})