_T='cefexBindingConformanceObjects'
_S='cefexConfigRowStatus'
_R='cefexConfigCreationTime'
_Q='cefexConfigPinningMaxLinks'
_P='cefexConfigPinningFailOverMode'
_O='cefexConfigSerialNum'
_N='cefexConfigSerialNumCheck'
_M='cefexConfigExtenderName'
_L='cefexBindingRowStatus'
_K='cefexBindingCreationTime'
_J='CiscoPortPinningMode'
_I='read-only'
_H='cefexBindingInterfaceOnCoreSwitch'
_G='TruthValue'
_F='cefexBindingExtenderIndex'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-create'
_B='CISCO-ETHERNET-FABRIC-EXTENDER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
ciscoEthernetFabricExtenderMIB=ModuleIdentity((1,3,6,1,4,1,9,9,691))
if mibBuilder.loadTexts:ciscoEthernetFabricExtenderMIB.setRevisions(('2009-02-23 00:00',))
class CiscoPortPinningMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('static',1))
_CiscoEthernetFabricExtenderMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEthernetFabricExtenderMIBNotifs=_CiscoEthernetFabricExtenderMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,691,0))
_CiscoEthernetFabricExtenderObjects_ObjectIdentity=ObjectIdentity
ciscoEthernetFabricExtenderObjects=_CiscoEthernetFabricExtenderObjects_ObjectIdentity((1,3,6,1,4,1,9,9,691,1))
_CefexConfig_ObjectIdentity=ObjectIdentity
cefexConfig=_CefexConfig_ObjectIdentity((1,3,6,1,4,1,9,9,691,1,1))
_CefexBindingTable_Object=MibTable
cefexBindingTable=_CefexBindingTable_Object((1,3,6,1,4,1,9,9,691,1,1,1))
if mibBuilder.loadTexts:cefexBindingTable.setStatus(_A)
_CefexBindingEntry_Object=MibTableRow
cefexBindingEntry=_CefexBindingEntry_Object((1,3,6,1,4,1,9,9,691,1,1,1,1))
cefexBindingEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cefexBindingEntry.setStatus(_A)
_CefexBindingInterfaceOnCoreSwitch_Type=InterfaceIndex
_CefexBindingInterfaceOnCoreSwitch_Object=MibTableColumn
cefexBindingInterfaceOnCoreSwitch=_CefexBindingInterfaceOnCoreSwitch_Object((1,3,6,1,4,1,9,9,691,1,1,1,1,1),_CefexBindingInterfaceOnCoreSwitch_Type())
cefexBindingInterfaceOnCoreSwitch.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cefexBindingInterfaceOnCoreSwitch.setStatus(_A)
class _CefexBindingExtenderIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,999))
_CefexBindingExtenderIndex_Type.__name__=_E
_CefexBindingExtenderIndex_Object=MibTableColumn
cefexBindingExtenderIndex=_CefexBindingExtenderIndex_Object((1,3,6,1,4,1,9,9,691,1,1,1,1,2),_CefexBindingExtenderIndex_Type())
cefexBindingExtenderIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexBindingExtenderIndex.setStatus(_A)
_CefexBindingCreationTime_Type=TimeStamp
_CefexBindingCreationTime_Object=MibTableColumn
cefexBindingCreationTime=_CefexBindingCreationTime_Object((1,3,6,1,4,1,9,9,691,1,1,1,1,3),_CefexBindingCreationTime_Type())
cefexBindingCreationTime.setMaxAccess(_I)
if mibBuilder.loadTexts:cefexBindingCreationTime.setStatus(_A)
_CefexBindingRowStatus_Type=RowStatus
_CefexBindingRowStatus_Object=MibTableColumn
cefexBindingRowStatus=_CefexBindingRowStatus_Object((1,3,6,1,4,1,9,9,691,1,1,1,1,4),_CefexBindingRowStatus_Type())
cefexBindingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexBindingRowStatus.setStatus(_A)
_CefexConfigTable_Object=MibTable
cefexConfigTable=_CefexConfigTable_Object((1,3,6,1,4,1,9,9,691,1,1,2))
if mibBuilder.loadTexts:cefexConfigTable.setStatus(_A)
_CefexConfigEntry_Object=MibTableRow
cefexConfigEntry=_CefexConfigEntry_Object((1,3,6,1,4,1,9,9,691,1,1,2,1))
cefexConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cefexConfigEntry.setStatus(_A)
class _CefexConfigExtenderName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CefexConfigExtenderName_Type.__name__=_D
_CefexConfigExtenderName_Object=MibTableColumn
cefexConfigExtenderName=_CefexConfigExtenderName_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,1),_CefexConfigExtenderName_Type())
cefexConfigExtenderName.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigExtenderName.setStatus(_A)
class _CefexConfigSerialNumCheck_Type(TruthValue):defaultValue=2
_CefexConfigSerialNumCheck_Type.__name__=_G
_CefexConfigSerialNumCheck_Object=MibTableColumn
cefexConfigSerialNumCheck=_CefexConfigSerialNumCheck_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,2),_CefexConfigSerialNumCheck_Type())
cefexConfigSerialNumCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigSerialNumCheck.setStatus(_A)
class _CefexConfigSerialNum_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CefexConfigSerialNum_Type.__name__=_D
_CefexConfigSerialNum_Object=MibTableColumn
cefexConfigSerialNum=_CefexConfigSerialNum_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,3),_CefexConfigSerialNum_Type())
cefexConfigSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigSerialNum.setStatus(_A)
class _CefexConfigPinningFailOverMode_Type(CiscoPortPinningMode):defaultValue=1
_CefexConfigPinningFailOverMode_Type.__name__=_J
_CefexConfigPinningFailOverMode_Object=MibTableColumn
cefexConfigPinningFailOverMode=_CefexConfigPinningFailOverMode_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,4),_CefexConfigPinningFailOverMode_Type())
cefexConfigPinningFailOverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigPinningFailOverMode.setStatus(_A)
class _CefexConfigPinningMaxLinks_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CefexConfigPinningMaxLinks_Type.__name__=_E
_CefexConfigPinningMaxLinks_Object=MibTableColumn
cefexConfigPinningMaxLinks=_CefexConfigPinningMaxLinks_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,5),_CefexConfigPinningMaxLinks_Type())
cefexConfigPinningMaxLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigPinningMaxLinks.setStatus(_A)
_CefexConfigCreationTime_Type=TimeStamp
_CefexConfigCreationTime_Object=MibTableColumn
cefexConfigCreationTime=_CefexConfigCreationTime_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,6),_CefexConfigCreationTime_Type())
cefexConfigCreationTime.setMaxAccess(_I)
if mibBuilder.loadTexts:cefexConfigCreationTime.setStatus(_A)
_CefexConfigRowStatus_Type=RowStatus
_CefexConfigRowStatus_Object=MibTableColumn
cefexConfigRowStatus=_CefexConfigRowStatus_Object((1,3,6,1,4,1,9,9,691,1,1,2,1,7),_CefexConfigRowStatus_Type())
cefexConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefexConfigRowStatus.setStatus(_A)
_CiscoEthernetFabricExtenderMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEthernetFabricExtenderMIBConformance=_CiscoEthernetFabricExtenderMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,691,2))
_CEthernetFabricExtenderMIBCompliances_ObjectIdentity=ObjectIdentity
cEthernetFabricExtenderMIBCompliances=_CEthernetFabricExtenderMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,691,2,1))
_CEthernetFabricExtenderMIBGroups_ObjectIdentity=ObjectIdentity
cEthernetFabricExtenderMIBGroups=_CEthernetFabricExtenderMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,691,2,2))
cefexBindingConformanceObjects=ObjectGroup((1,3,6,1,4,1,9,9,691,2,2,1))
cefexBindingConformanceObjects.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cefexBindingConformanceObjects.setStatus(_A)
cEthernetFabricExtenderMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,691,2,1,1))
cEthernetFabricExtenderMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:cEthernetFabricExtenderMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:CiscoPortPinningMode,'ciscoEthernetFabricExtenderMIB':ciscoEthernetFabricExtenderMIB,'ciscoEthernetFabricExtenderMIBNotifs':ciscoEthernetFabricExtenderMIBNotifs,'ciscoEthernetFabricExtenderObjects':ciscoEthernetFabricExtenderObjects,'cefexConfig':cefexConfig,'cefexBindingTable':cefexBindingTable,'cefexBindingEntry':cefexBindingEntry,_H:cefexBindingInterfaceOnCoreSwitch,_F:cefexBindingExtenderIndex,_K:cefexBindingCreationTime,_L:cefexBindingRowStatus,'cefexConfigTable':cefexConfigTable,'cefexConfigEntry':cefexConfigEntry,_M:cefexConfigExtenderName,_N:cefexConfigSerialNumCheck,_O:cefexConfigSerialNum,_P:cefexConfigPinningFailOverMode,_Q:cefexConfigPinningMaxLinks,_R:cefexConfigCreationTime,_S:cefexConfigRowStatus,'ciscoEthernetFabricExtenderMIBConformance':ciscoEthernetFabricExtenderMIBConformance,'cEthernetFabricExtenderMIBCompliances':cEthernetFabricExtenderMIBCompliances,'cEthernetFabricExtenderMIBCompliance':cEthernetFabricExtenderMIBCompliance,'cEthernetFabricExtenderMIBGroups':cEthernetFabricExtenderMIBGroups,_T:cefexBindingConformanceObjects})