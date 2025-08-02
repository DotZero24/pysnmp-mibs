_g='ciscoFcSdvConfigGroup'
_f='cFcSdvVirtRealDevMapRowStatus'
_e='cFcSdvVirtRealDevMapStorageType'
_d='cFcSdvVirtRealDevMapType'
_c='cFcSdvVirtRealDeviceId'
_b='cFcSdvVirtRealDeviceIdType'
_a='cFcSdvVdRowStatus'
_Z='cFcSdvVdRealDevMapList'
_Y='cFcSdvVdStorageType'
_X='cFcSdvVdAssignedFcId'
_W='cFcSdvVdNwwn'
_V='cFcSdvVdPwwn'
_U='cFcSdvVdFcId'
_T='cFcSdvVdVirtDomain'
_S='cFcSdvVdName'
_R='CiscoFcSdvRealDevMapType'
_Q='CiscoFcSdvDevId'
_P='CiscoFcSdvDevIdType'
_O='cFcSdvVirtRealDevMapIndex'
_N='not-accessible'
_M='SnmpAdminString'
_L='FcList'
_K='FcAddressId'
_J='DomainIdOrZero'
_I='cFcSdvVdIndex'
_H='StorageType'
_G='Unsigned32'
_F='vsanIndex'
_E='CISCO-VSAN-MIB'
_D='read-only'
_C='read-create'
_B='CISCO-FC-SDV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DomainIdOrZero,FcAddressId,FcNameIdOrZero=mibBuilder.importSymbols('CISCO-ST-TC',_J,_K,'FcNameIdOrZero')
vsanIndex,=mibBuilder.importSymbols(_E,_F)
FcList,=mibBuilder.importSymbols('CISCO-ZS-MIB',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention')
ciscoFcSdvMIB=ModuleIdentity((1,3,6,1,4,1,9,9,593))
if mibBuilder.loadTexts:ciscoFcSdvMIB.setRevisions(('2006-09-26 00:00',))
class CiscoFcSdvDevIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleDevPWWN',1),('singleDevDevAlias',2)))
class CiscoFcSdvDevId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class CiscoFcSdvRealDevMapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryDevMap',1),('secondaryDevMap',2)))
_CiscoFcSdvMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFcSdvMIBNotifs=_CiscoFcSdvMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,593,0))
_CiscoFcSdvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcSdvMIBObjects=_CiscoFcSdvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,593,1))
_CFcSdvConfig_ObjectIdentity=ObjectIdentity
cFcSdvConfig=_CFcSdvConfig_ObjectIdentity((1,3,6,1,4,1,9,9,593,1,1))
_CFcSdvVirtDeviceTable_Object=MibTable
cFcSdvVirtDeviceTable=_CFcSdvVirtDeviceTable_Object((1,3,6,1,4,1,9,9,593,1,1,1))
if mibBuilder.loadTexts:cFcSdvVirtDeviceTable.setStatus(_A)
_CFcSdvVirtDeviceEntry_Object=MibTableRow
cFcSdvVirtDeviceEntry=_CFcSdvVirtDeviceEntry_Object((1,3,6,1,4,1,9,9,593,1,1,1,1))
cFcSdvVirtDeviceEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:cFcSdvVirtDeviceEntry.setStatus(_A)
class _CFcSdvVdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CFcSdvVdIndex_Type.__name__=_G
_CFcSdvVdIndex_Object=MibTableColumn
cFcSdvVdIndex=_CFcSdvVdIndex_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,1),_CFcSdvVdIndex_Type())
cFcSdvVdIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cFcSdvVdIndex.setStatus(_A)
class _CFcSdvVdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CFcSdvVdName_Type.__name__=_M
_CFcSdvVdName_Object=MibTableColumn
cFcSdvVdName=_CFcSdvVdName_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,2),_CFcSdvVdName_Type())
cFcSdvVdName.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVdName.setStatus(_A)
class _CFcSdvVdVirtDomain_Type(DomainIdOrZero):defaultValue=0
_CFcSdvVdVirtDomain_Type.__name__=_J
_CFcSdvVdVirtDomain_Object=MibTableColumn
cFcSdvVdVirtDomain=_CFcSdvVdVirtDomain_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,3),_CFcSdvVdVirtDomain_Type())
cFcSdvVdVirtDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVdVirtDomain.setStatus(_A)
class _CFcSdvVdFcId_Type(FcAddressId):defaultHexValue='000000'
_CFcSdvVdFcId_Type.__name__=_K
_CFcSdvVdFcId_Object=MibTableColumn
cFcSdvVdFcId=_CFcSdvVdFcId_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,4),_CFcSdvVdFcId_Type())
cFcSdvVdFcId.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVdFcId.setStatus(_A)
_CFcSdvVdPwwn_Type=FcNameIdOrZero
_CFcSdvVdPwwn_Object=MibTableColumn
cFcSdvVdPwwn=_CFcSdvVdPwwn_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,5),_CFcSdvVdPwwn_Type())
cFcSdvVdPwwn.setMaxAccess(_D)
if mibBuilder.loadTexts:cFcSdvVdPwwn.setStatus(_A)
_CFcSdvVdNwwn_Type=FcNameIdOrZero
_CFcSdvVdNwwn_Object=MibTableColumn
cFcSdvVdNwwn=_CFcSdvVdNwwn_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,6),_CFcSdvVdNwwn_Type())
cFcSdvVdNwwn.setMaxAccess(_D)
if mibBuilder.loadTexts:cFcSdvVdNwwn.setStatus(_A)
_CFcSdvVdAssignedFcId_Type=FcAddressId
_CFcSdvVdAssignedFcId_Object=MibTableColumn
cFcSdvVdAssignedFcId=_CFcSdvVdAssignedFcId_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,7),_CFcSdvVdAssignedFcId_Type())
cFcSdvVdAssignedFcId.setMaxAccess(_D)
if mibBuilder.loadTexts:cFcSdvVdAssignedFcId.setStatus(_A)
class _CFcSdvVdRealDevMapList_Type(FcList):defaultHexValue='';subtypeSpec=FcList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CFcSdvVdRealDevMapList_Type.__name__=_L
_CFcSdvVdRealDevMapList_Object=MibTableColumn
cFcSdvVdRealDevMapList=_CFcSdvVdRealDevMapList_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,8),_CFcSdvVdRealDevMapList_Type())
cFcSdvVdRealDevMapList.setMaxAccess(_D)
if mibBuilder.loadTexts:cFcSdvVdRealDevMapList.setStatus(_A)
class _CFcSdvVdStorageType_Type(StorageType):defaultValue=3
_CFcSdvVdStorageType_Type.__name__=_H
_CFcSdvVdStorageType_Object=MibTableColumn
cFcSdvVdStorageType=_CFcSdvVdStorageType_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,9),_CFcSdvVdStorageType_Type())
cFcSdvVdStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVdStorageType.setStatus(_A)
_CFcSdvVdRowStatus_Type=RowStatus
_CFcSdvVdRowStatus_Object=MibTableColumn
cFcSdvVdRowStatus=_CFcSdvVdRowStatus_Object((1,3,6,1,4,1,9,9,593,1,1,1,1,10),_CFcSdvVdRowStatus_Type())
cFcSdvVdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVdRowStatus.setStatus(_A)
_CFcSdvVirtRealDevMapTable_Object=MibTable
cFcSdvVirtRealDevMapTable=_CFcSdvVirtRealDevMapTable_Object((1,3,6,1,4,1,9,9,593,1,1,2))
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapTable.setStatus(_A)
_CFcSdvVirtRealDevMapEntry_Object=MibTableRow
cFcSdvVirtRealDevMapEntry=_CFcSdvVirtRealDevMapEntry_Object((1,3,6,1,4,1,9,9,593,1,1,2,1))
cFcSdvVirtRealDevMapEntry.setIndexNames((0,_E,_F),(0,_B,_I),(0,_B,_O))
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapEntry.setStatus(_A)
class _CFcSdvVirtRealDevMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CFcSdvVirtRealDevMapIndex_Type.__name__=_G
_CFcSdvVirtRealDevMapIndex_Object=MibTableColumn
cFcSdvVirtRealDevMapIndex=_CFcSdvVirtRealDevMapIndex_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,1),_CFcSdvVirtRealDevMapIndex_Type())
cFcSdvVirtRealDevMapIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapIndex.setStatus(_A)
class _CFcSdvVirtRealDeviceIdType_Type(CiscoFcSdvDevIdType):defaultValue=1
_CFcSdvVirtRealDeviceIdType_Type.__name__=_P
_CFcSdvVirtRealDeviceIdType_Object=MibTableColumn
cFcSdvVirtRealDeviceIdType=_CFcSdvVirtRealDeviceIdType_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,2),_CFcSdvVirtRealDeviceIdType_Type())
cFcSdvVirtRealDeviceIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVirtRealDeviceIdType.setStatus(_A)
class _CFcSdvVirtRealDeviceId_Type(CiscoFcSdvDevId):defaultHexValue='0000000000000000';subtypeSpec=CiscoFcSdvDevId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CFcSdvVirtRealDeviceId_Type.__name__=_Q
_CFcSdvVirtRealDeviceId_Object=MibTableColumn
cFcSdvVirtRealDeviceId=_CFcSdvVirtRealDeviceId_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,3),_CFcSdvVirtRealDeviceId_Type())
cFcSdvVirtRealDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVirtRealDeviceId.setStatus(_A)
class _CFcSdvVirtRealDevMapType_Type(CiscoFcSdvRealDevMapType):defaultValue=2
_CFcSdvVirtRealDevMapType_Type.__name__=_R
_CFcSdvVirtRealDevMapType_Object=MibTableColumn
cFcSdvVirtRealDevMapType=_CFcSdvVirtRealDevMapType_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,4),_CFcSdvVirtRealDevMapType_Type())
cFcSdvVirtRealDevMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapType.setStatus(_A)
class _CFcSdvVirtRealDevMapStorageType_Type(StorageType):defaultValue=3
_CFcSdvVirtRealDevMapStorageType_Type.__name__=_H
_CFcSdvVirtRealDevMapStorageType_Object=MibTableColumn
cFcSdvVirtRealDevMapStorageType=_CFcSdvVirtRealDevMapStorageType_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,5),_CFcSdvVirtRealDevMapStorageType_Type())
cFcSdvVirtRealDevMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapStorageType.setStatus(_A)
_CFcSdvVirtRealDevMapRowStatus_Type=RowStatus
_CFcSdvVirtRealDevMapRowStatus_Object=MibTableColumn
cFcSdvVirtRealDevMapRowStatus=_CFcSdvVirtRealDevMapRowStatus_Object((1,3,6,1,4,1,9,9,593,1,1,2,1,6),_CFcSdvVirtRealDevMapRowStatus_Type())
cFcSdvVirtRealDevMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cFcSdvVirtRealDevMapRowStatus.setStatus(_A)
_CiscoFcSdvMIBConform_ObjectIdentity=ObjectIdentity
ciscoFcSdvMIBConform=_CiscoFcSdvMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,593,2))
_CiscoFcSdvMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFcSdvMIBCompliances=_CiscoFcSdvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,593,2,1))
_CiscoFcSdvMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFcSdvMIBGroups=_CiscoFcSdvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,593,2,2))
ciscoFcSdvConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,593,2,2,1))
ciscoFcSdvConfigGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoFcSdvConfigGroup.setStatus(_A)
ciscoFcSdvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,593,2,1,1))
ciscoFcSdvMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:ciscoFcSdvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:CiscoFcSdvDevIdType,_Q:CiscoFcSdvDevId,_R:CiscoFcSdvRealDevMapType,'ciscoFcSdvMIB':ciscoFcSdvMIB,'ciscoFcSdvMIBNotifs':ciscoFcSdvMIBNotifs,'ciscoFcSdvMIBObjects':ciscoFcSdvMIBObjects,'cFcSdvConfig':cFcSdvConfig,'cFcSdvVirtDeviceTable':cFcSdvVirtDeviceTable,'cFcSdvVirtDeviceEntry':cFcSdvVirtDeviceEntry,_I:cFcSdvVdIndex,_S:cFcSdvVdName,_T:cFcSdvVdVirtDomain,_U:cFcSdvVdFcId,_V:cFcSdvVdPwwn,_W:cFcSdvVdNwwn,_X:cFcSdvVdAssignedFcId,_Z:cFcSdvVdRealDevMapList,_Y:cFcSdvVdStorageType,_a:cFcSdvVdRowStatus,'cFcSdvVirtRealDevMapTable':cFcSdvVirtRealDevMapTable,'cFcSdvVirtRealDevMapEntry':cFcSdvVirtRealDevMapEntry,_O:cFcSdvVirtRealDevMapIndex,_b:cFcSdvVirtRealDeviceIdType,_c:cFcSdvVirtRealDeviceId,_d:cFcSdvVirtRealDevMapType,_e:cFcSdvVirtRealDevMapStorageType,_f:cFcSdvVirtRealDevMapRowStatus,'ciscoFcSdvMIBConform':ciscoFcSdvMIBConform,'ciscoFcSdvMIBCompliances':ciscoFcSdvMIBCompliances,'ciscoFcSdvMIBCompliance':ciscoFcSdvMIBCompliance,'ciscoFcSdvMIBGroups':ciscoFcSdvMIBGroups,_g:ciscoFcSdvConfigGroup})