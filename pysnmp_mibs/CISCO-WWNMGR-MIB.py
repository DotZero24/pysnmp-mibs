_b='cwmWwnmVsanWwnGroup'
_a='wwnmTypeOtherWwnAvailableNotify'
_Z='wwnmTypeOtherWwnShortageNotify'
_Y='wwnmType1WwnAvailableNotify'
_X='wwnmType1WwnShortageNotify'
_W='wwnmVsanWwnRowStatus'
_V='wwnmVsanWwnStorageType'
_U='wwnmVsanWwn'
_T='wwnmTypeOtherReservedWwns'
_S='wwnmType1ReservedWwns'
_R='wwnmTypeOtherMaxWwns'
_Q='wwnmType1MaxWwns'
_P='wwnmSecondaryMacAddressRange'
_O='wwnmSecondaryBaseMacAddress'
_N='read-create'
_M='read-write'
_L='StorageType'
_K='MacAddress'
_J='vsanIndex'
_I='CISCO-VSAN-MIB'
_H='cwmWwnmNotificationGroup'
_G='cwmWwnmConfigurationGroup'
_F='wwnmTypeOtherAvailableWwns'
_E='wwnmType1AvailableWwns'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-WWNMGR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId')
vsanIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_K,'PhysAddress','RowStatus',_L,'TextualConvention')
ciscoWwnmgrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,286))
if mibBuilder.loadTexts:ciscoWwnmgrMIB.setRevisions(('2006-02-06 00:00','2002-10-01 00:00'))
_CiscoWwnmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWwnmMIBObjects=_CiscoWwnmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,286,1))
_WwnmConfigurationGroup_ObjectIdentity=ObjectIdentity
wwnmConfigurationGroup=_WwnmConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,9,9,286,1,1))
class _WwnmSecondaryBaseMacAddress_Type(MacAddress):defaultHexValue='000000000000'
_WwnmSecondaryBaseMacAddress_Type.__name__=_K
_WwnmSecondaryBaseMacAddress_Object=MibScalar
wwnmSecondaryBaseMacAddress=_WwnmSecondaryBaseMacAddress_Object((1,3,6,1,4,1,9,9,286,1,1,1),_WwnmSecondaryBaseMacAddress_Type())
wwnmSecondaryBaseMacAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:wwnmSecondaryBaseMacAddress.setStatus(_B)
class _WwnmSecondaryMacAddressRange_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwnmSecondaryMacAddressRange_Type.__name__=_D
_WwnmSecondaryMacAddressRange_Object=MibScalar
wwnmSecondaryMacAddressRange=_WwnmSecondaryMacAddressRange_Object((1,3,6,1,4,1,9,9,286,1,1,2),_WwnmSecondaryMacAddressRange_Type())
wwnmSecondaryMacAddressRange.setMaxAccess(_M)
if mibBuilder.loadTexts:wwnmSecondaryMacAddressRange.setStatus(_B)
class _WwnmType1MaxWwns_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwnmType1MaxWwns_Type.__name__=_D
_WwnmType1MaxWwns_Object=MibScalar
wwnmType1MaxWwns=_WwnmType1MaxWwns_Object((1,3,6,1,4,1,9,9,286,1,1,3),_WwnmType1MaxWwns_Type())
wwnmType1MaxWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmType1MaxWwns.setStatus(_B)
_WwnmType1AvailableWwns_Type=Gauge32
_WwnmType1AvailableWwns_Object=MibScalar
wwnmType1AvailableWwns=_WwnmType1AvailableWwns_Object((1,3,6,1,4,1,9,9,286,1,1,4),_WwnmType1AvailableWwns_Type())
wwnmType1AvailableWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmType1AvailableWwns.setStatus(_B)
class _WwnmTypeOtherMaxWwns_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwnmTypeOtherMaxWwns_Type.__name__=_D
_WwnmTypeOtherMaxWwns_Object=MibScalar
wwnmTypeOtherMaxWwns=_WwnmTypeOtherMaxWwns_Object((1,3,6,1,4,1,9,9,286,1,1,5),_WwnmTypeOtherMaxWwns_Type())
wwnmTypeOtherMaxWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmTypeOtherMaxWwns.setStatus(_B)
_WwnmTypeOtherAvailableWwns_Type=Gauge32
_WwnmTypeOtherAvailableWwns_Object=MibScalar
wwnmTypeOtherAvailableWwns=_WwnmTypeOtherAvailableWwns_Object((1,3,6,1,4,1,9,9,286,1,1,6),_WwnmTypeOtherAvailableWwns_Type())
wwnmTypeOtherAvailableWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmTypeOtherAvailableWwns.setStatus(_B)
class _WwnmType1ReservedWwns_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwnmType1ReservedWwns_Type.__name__=_D
_WwnmType1ReservedWwns_Object=MibScalar
wwnmType1ReservedWwns=_WwnmType1ReservedWwns_Object((1,3,6,1,4,1,9,9,286,1,1,7),_WwnmType1ReservedWwns_Type())
wwnmType1ReservedWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmType1ReservedWwns.setStatus(_B)
class _WwnmTypeOtherReservedWwns_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_WwnmTypeOtherReservedWwns_Type.__name__=_D
_WwnmTypeOtherReservedWwns_Object=MibScalar
wwnmTypeOtherReservedWwns=_WwnmTypeOtherReservedWwns_Object((1,3,6,1,4,1,9,9,286,1,1,8),_WwnmTypeOtherReservedWwns_Type())
wwnmTypeOtherReservedWwns.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmTypeOtherReservedWwns.setStatus(_B)
_WwnmVsanWwnTable_Object=MibTable
wwnmVsanWwnTable=_WwnmVsanWwnTable_Object((1,3,6,1,4,1,9,9,286,1,1,9))
if mibBuilder.loadTexts:wwnmVsanWwnTable.setStatus(_B)
_WwnmVsanWwnEntry_Object=MibTableRow
wwnmVsanWwnEntry=_WwnmVsanWwnEntry_Object((1,3,6,1,4,1,9,9,286,1,1,9,1))
wwnmVsanWwnEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:wwnmVsanWwnEntry.setStatus(_B)
_WwnmVsanWwn_Type=FcNameId
_WwnmVsanWwn_Object=MibTableColumn
wwnmVsanWwn=_WwnmVsanWwn_Object((1,3,6,1,4,1,9,9,286,1,1,9,1,1),_WwnmVsanWwn_Type())
wwnmVsanWwn.setMaxAccess(_N)
if mibBuilder.loadTexts:wwnmVsanWwn.setStatus(_B)
class _WwnmVsanWwnStorageType_Type(StorageType):defaultValue=3
_WwnmVsanWwnStorageType_Type.__name__=_L
_WwnmVsanWwnStorageType_Object=MibTableColumn
wwnmVsanWwnStorageType=_WwnmVsanWwnStorageType_Object((1,3,6,1,4,1,9,9,286,1,1,9,1,2),_WwnmVsanWwnStorageType_Type())
wwnmVsanWwnStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwnmVsanWwnStorageType.setStatus(_B)
_WwnmVsanWwnRowStatus_Type=RowStatus
_WwnmVsanWwnRowStatus_Object=MibTableColumn
wwnmVsanWwnRowStatus=_WwnmVsanWwnRowStatus_Object((1,3,6,1,4,1,9,9,286,1,1,9,1,3),_WwnmVsanWwnRowStatus_Type())
wwnmVsanWwnRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:wwnmVsanWwnRowStatus.setStatus(_B)
_WwnmNotificationGroup_ObjectIdentity=ObjectIdentity
wwnmNotificationGroup=_WwnmNotificationGroup_ObjectIdentity((1,3,6,1,4,1,9,9,286,1,2))
_WwnmNotification_ObjectIdentity=ObjectIdentity
wwnmNotification=_WwnmNotification_ObjectIdentity((1,3,6,1,4,1,9,9,286,1,2,1))
_WwnmNotificationPrefix_ObjectIdentity=ObjectIdentity
wwnmNotificationPrefix=_WwnmNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,286,1,2,1,0))
_CiscoWwnmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWwnmMIBConformance=_CiscoWwnmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,286,2))
_CiscoWwnmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWwnmMIBCompliances=_CiscoWwnmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,286,2,1))
_CiscoWwnmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWwnmMIBGroups=_CiscoWwnmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,286,2,2))
cwmWwnmConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,286,2,2,6))
cwmWwnmConfigurationGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_E),(_A,_R),(_A,_F),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cwmWwnmConfigurationGroup.setStatus(_B)
cwmWwnmVsanWwnGroup=ObjectGroup((1,3,6,1,4,1,9,9,286,2,2,9))
cwmWwnmVsanWwnGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cwmWwnmVsanWwnGroup.setStatus(_B)
wwnmType1WwnShortageNotify=NotificationType((1,3,6,1,4,1,9,9,286,1,2,1,0,1))
wwnmType1WwnShortageNotify.setObjects((_A,_E))
if mibBuilder.loadTexts:wwnmType1WwnShortageNotify.setStatus(_B)
wwnmType1WwnAvailableNotify=NotificationType((1,3,6,1,4,1,9,9,286,1,2,1,0,2))
wwnmType1WwnAvailableNotify.setObjects((_A,_E))
if mibBuilder.loadTexts:wwnmType1WwnAvailableNotify.setStatus(_B)
wwnmTypeOtherWwnShortageNotify=NotificationType((1,3,6,1,4,1,9,9,286,1,2,1,0,3))
wwnmTypeOtherWwnShortageNotify.setObjects((_A,_F))
if mibBuilder.loadTexts:wwnmTypeOtherWwnShortageNotify.setStatus(_B)
wwnmTypeOtherWwnAvailableNotify=NotificationType((1,3,6,1,4,1,9,9,286,1,2,1,0,4))
wwnmTypeOtherWwnAvailableNotify.setObjects((_A,_F))
if mibBuilder.loadTexts:wwnmTypeOtherWwnAvailableNotify.setStatus(_B)
cwmWwnmNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,286,2,2,8))
cwmWwnmNotificationGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cwmWwnmNotificationGroup.setStatus(_B)
ciscoWwnmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,286,2,1,1))
ciscoWwnmMIBCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ciscoWwnmMIBCompliance.setStatus('deprecated')
ciscoWwnmMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,286,2,1,2))
ciscoWwnmMIBCompliance1.setObjects(*((_A,_G),(_A,_b),(_A,_H)))
if mibBuilder.loadTexts:ciscoWwnmMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWwnmgrMIB':ciscoWwnmgrMIB,'ciscoWwnmMIBObjects':ciscoWwnmMIBObjects,'wwnmConfigurationGroup':wwnmConfigurationGroup,_O:wwnmSecondaryBaseMacAddress,_P:wwnmSecondaryMacAddressRange,_Q:wwnmType1MaxWwns,_E:wwnmType1AvailableWwns,_R:wwnmTypeOtherMaxWwns,_F:wwnmTypeOtherAvailableWwns,_S:wwnmType1ReservedWwns,_T:wwnmTypeOtherReservedWwns,'wwnmVsanWwnTable':wwnmVsanWwnTable,'wwnmVsanWwnEntry':wwnmVsanWwnEntry,_U:wwnmVsanWwn,_V:wwnmVsanWwnStorageType,_W:wwnmVsanWwnRowStatus,'wwnmNotificationGroup':wwnmNotificationGroup,'wwnmNotification':wwnmNotification,'wwnmNotificationPrefix':wwnmNotificationPrefix,_X:wwnmType1WwnShortageNotify,_Y:wwnmType1WwnAvailableNotify,_Z:wwnmTypeOtherWwnShortageNotify,_a:wwnmTypeOtherWwnAvailableNotify,'ciscoWwnmMIBConformance':ciscoWwnmMIBConformance,'ciscoWwnmMIBCompliances':ciscoWwnmMIBCompliances,'ciscoWwnmMIBCompliance':ciscoWwnmMIBCompliance,'ciscoWwnmMIBCompliance1':ciscoWwnmMIBCompliance1,'ciscoWwnmMIBGroups':ciscoWwnmMIBGroups,_G:cwmWwnmConfigurationGroup,_H:cwmWwnmNotificationGroup,_b:cwmWwnmVsanWwnGroup})