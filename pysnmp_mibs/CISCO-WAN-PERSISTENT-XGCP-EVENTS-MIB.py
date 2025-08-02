_I='persistentXgcpEventsMIBGroup'
_H='persistentXgcpEventRowStatus'
_G='persistentXgcpEventName'
_F='read-write'
_E='persistentXgcpEventNum'
_D='Integer32'
_C='SnmpAdminString'
_B='CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoWanPersistentXgcpEventsMIB=ModuleIdentity((1,3,6,1,4,1,351,150,18))
if mibBuilder.loadTexts:ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))
_CiscoWanPersistentXgcpEventsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanPersistentXgcpEventsMIBObjects=_CiscoWanPersistentXgcpEventsMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,18,1))
_PersistentXgcpEvents_ObjectIdentity=ObjectIdentity
persistentXgcpEvents=_PersistentXgcpEvents_ObjectIdentity((1,3,6,1,4,1,351,150,18,1,1))
_PersistentXgcpEventsTable_Object=MibTable
persistentXgcpEventsTable=_PersistentXgcpEventsTable_Object((1,3,6,1,4,1,351,150,18,1,1,1))
if mibBuilder.loadTexts:persistentXgcpEventsTable.setStatus(_A)
_PersistentXgcpEventsEntry_Object=MibTableRow
persistentXgcpEventsEntry=_PersistentXgcpEventsEntry_Object((1,3,6,1,4,1,351,150,18,1,1,1,1))
persistentXgcpEventsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:persistentXgcpEventsEntry.setStatus(_A)
class _PersistentXgcpEventNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PersistentXgcpEventNum_Type.__name__=_D
_PersistentXgcpEventNum_Object=MibTableColumn
persistentXgcpEventNum=_PersistentXgcpEventNum_Object((1,3,6,1,4,1,351,150,18,1,1,1,1,1),_PersistentXgcpEventNum_Type())
persistentXgcpEventNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:persistentXgcpEventNum.setStatus(_A)
class _PersistentXgcpEventName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PersistentXgcpEventName_Type.__name__=_C
_PersistentXgcpEventName_Object=MibTableColumn
persistentXgcpEventName=_PersistentXgcpEventName_Object((1,3,6,1,4,1,351,150,18,1,1,1,1,2),_PersistentXgcpEventName_Type())
persistentXgcpEventName.setMaxAccess(_F)
if mibBuilder.loadTexts:persistentXgcpEventName.setStatus(_A)
_PersistentXgcpEventRowStatus_Type=RowStatus
_PersistentXgcpEventRowStatus_Object=MibTableColumn
persistentXgcpEventRowStatus=_PersistentXgcpEventRowStatus_Object((1,3,6,1,4,1,351,150,18,1,1,1,1,3),_PersistentXgcpEventRowStatus_Type())
persistentXgcpEventRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:persistentXgcpEventRowStatus.setStatus(_A)
_PersistentXgcpEventsMIBConformance_ObjectIdentity=ObjectIdentity
persistentXgcpEventsMIBConformance=_PersistentXgcpEventsMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,18,2))
_PersistentXgcpEventsMIBCompliances_ObjectIdentity=ObjectIdentity
persistentXgcpEventsMIBCompliances=_PersistentXgcpEventsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,18,2,1))
_PersistentXgcpEventsMIBGroups_ObjectIdentity=ObjectIdentity
persistentXgcpEventsMIBGroups=_PersistentXgcpEventsMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,18,2,2))
persistentXgcpEventsMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,18,2,2,1))
persistentXgcpEventsMIBGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:persistentXgcpEventsMIBGroup.setStatus(_A)
persistentXgcpEventsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,18,2,1,1))
persistentXgcpEventsMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:persistentXgcpEventsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanPersistentXgcpEventsMIB':ciscoWanPersistentXgcpEventsMIB,'ciscoWanPersistentXgcpEventsMIBObjects':ciscoWanPersistentXgcpEventsMIBObjects,'persistentXgcpEvents':persistentXgcpEvents,'persistentXgcpEventsTable':persistentXgcpEventsTable,'persistentXgcpEventsEntry':persistentXgcpEventsEntry,_E:persistentXgcpEventNum,_G:persistentXgcpEventName,_H:persistentXgcpEventRowStatus,'persistentXgcpEventsMIBConformance':persistentXgcpEventsMIBConformance,'persistentXgcpEventsMIBCompliances':persistentXgcpEventsMIBCompliances,'persistentXgcpEventsMIBCompliance':persistentXgcpEventsMIBCompliance,'persistentXgcpEventsMIBGroups':persistentXgcpEventsMIBGroups,_I:persistentXgcpEventsMIBGroup})