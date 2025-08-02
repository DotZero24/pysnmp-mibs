_d='dpsvDeviceInfoGroup'
_c='dpsvOUICfgGroup'
_b='dpsvBasicGroup'
_a='dpsvDeviceStatus'
_Z='dpsvDeviceStartTime'
_Y='dpsvDeviceDescr'
_X='dpsvDeviceCompType'
_W='dpsvOuiRowStatus'
_V='dpsvOuiDescription'
_U='dpsvOuiComponentType'
_T='dpsvDynamicPorts'
_S='dpsvMemberPorts'
_R='dpsvAgingTime'
_Q='dpsvQos'
_P='dpsvVlanId'
_O='dpsvEnabled'
_N='dpsvDeviceAddr'
_M='dpsvDevicePortIfIdx'
_L='dpsvOuiMask'
_K='dpsvOuiAddr'
_J='Integer32'
_I='VlanIdOrNone'
_H='read-create'
_G='Unsigned32'
_F='SnmpAdminString'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='DLINKPRIME-SURVEILLANCE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeSurveillanceVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,15,19))
if mibBuilder.loadTexts:dlinkPrimeSurveillanceVlanMIB.setRevisions(('2014-04-26 00:00',))
class OuiComponentType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('dlink',2),('vms',3),('vmsClient',4),('videoEncoder',5),('networkStorage',6)))
_DpsvMIBNotifications_ObjectIdentity=ObjectIdentity
dpsvMIBNotifications=_DpsvMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,19,0))
_DpsvMIBObjects_ObjectIdentity=ObjectIdentity
dpsvMIBObjects=_DpsvMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,19,1))
_DpsvGlobal_ObjectIdentity=ObjectIdentity
dpsvGlobal=_DpsvGlobal_ObjectIdentity((1,3,6,1,4,1,171,15,19,1,1))
_DpsvEnabled_Type=TruthValue
_DpsvEnabled_Object=MibScalar
dpsvEnabled=_DpsvEnabled_Object((1,3,6,1,4,1,171,15,19,1,1,1),_DpsvEnabled_Type())
dpsvEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsvEnabled.setStatus(_A)
class _DpsvVlanId_Type(VlanIdOrNone):defaultValue=0
_DpsvVlanId_Type.__name__=_I
_DpsvVlanId_Object=MibScalar
dpsvVlanId=_DpsvVlanId_Object((1,3,6,1,4,1,171,15,19,1,1,2),_DpsvVlanId_Type())
dpsvVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsvVlanId.setStatus(_A)
class _DpsvQos_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DpsvQos_Type.__name__=_G
_DpsvQos_Object=MibScalar
dpsvQos=_DpsvQos_Object((1,3,6,1,4,1,171,15,19,1,1,3),_DpsvQos_Type())
dpsvQos.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsvQos.setStatus(_A)
class _DpsvAgingTime_Type(Unsigned32):defaultValue=720;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DpsvAgingTime_Type.__name__=_G
_DpsvAgingTime_Object=MibScalar
dpsvAgingTime=_DpsvAgingTime_Object((1,3,6,1,4,1,171,15,19,1,1,4),_DpsvAgingTime_Type())
dpsvAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dpsvAgingTime.setStatus(_A)
if mibBuilder.loadTexts:dpsvAgingTime.setUnits('minutes')
_DpsvOuiTable_Object=MibTable
dpsvOuiTable=_DpsvOuiTable_Object((1,3,6,1,4,1,171,15,19,1,1,5))
if mibBuilder.loadTexts:dpsvOuiTable.setStatus(_A)
_DpsvOuiEntry_Object=MibTableRow
dpsvOuiEntry=_DpsvOuiEntry_Object((1,3,6,1,4,1,171,15,19,1,1,5,1))
dpsvOuiEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:dpsvOuiEntry.setStatus(_A)
_DpsvOuiAddr_Type=MacAddress
_DpsvOuiAddr_Object=MibTableColumn
dpsvOuiAddr=_DpsvOuiAddr_Object((1,3,6,1,4,1,171,15,19,1,1,5,1,1),_DpsvOuiAddr_Type())
dpsvOuiAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsvOuiAddr.setStatus(_A)
_DpsvOuiMask_Type=MacAddress
_DpsvOuiMask_Object=MibTableColumn
dpsvOuiMask=_DpsvOuiMask_Object((1,3,6,1,4,1,171,15,19,1,1,5,1,2),_DpsvOuiMask_Type())
dpsvOuiMask.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsvOuiMask.setStatus(_A)
_DpsvOuiComponentType_Type=OuiComponentType
_DpsvOuiComponentType_Object=MibTableColumn
dpsvOuiComponentType=_DpsvOuiComponentType_Object((1,3,6,1,4,1,171,15,19,1,1,5,1,3),_DpsvOuiComponentType_Type())
dpsvOuiComponentType.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsvOuiComponentType.setStatus(_A)
class _DpsvOuiDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpsvOuiDescription_Type.__name__=_F
_DpsvOuiDescription_Object=MibTableColumn
dpsvOuiDescription=_DpsvOuiDescription_Object((1,3,6,1,4,1,171,15,19,1,1,5,1,4),_DpsvOuiDescription_Type())
dpsvOuiDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsvOuiDescription.setStatus(_A)
_DpsvOuiRowStatus_Type=RowStatus
_DpsvOuiRowStatus_Object=MibTableColumn
dpsvOuiRowStatus=_DpsvOuiRowStatus_Object((1,3,6,1,4,1,171,15,19,1,1,5,1,5),_DpsvOuiRowStatus_Type())
dpsvOuiRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:dpsvOuiRowStatus.setStatus(_A)
_DpsvInfo_ObjectIdentity=ObjectIdentity
dpsvInfo=_DpsvInfo_ObjectIdentity((1,3,6,1,4,1,171,15,19,1,2))
_DpsvMemberPorts_Type=PortList
_DpsvMemberPorts_Object=MibScalar
dpsvMemberPorts=_DpsvMemberPorts_Object((1,3,6,1,4,1,171,15,19,1,2,1),_DpsvMemberPorts_Type())
dpsvMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvMemberPorts.setStatus(_A)
_DpsvDynamicPorts_Type=PortList
_DpsvDynamicPorts_Object=MibScalar
dpsvDynamicPorts=_DpsvDynamicPorts_Object((1,3,6,1,4,1,171,15,19,1,2,2),_DpsvDynamicPorts_Type())
dpsvDynamicPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvDynamicPorts.setStatus(_A)
_DpsvDeviceTable_Object=MibTable
dpsvDeviceTable=_DpsvDeviceTable_Object((1,3,6,1,4,1,171,15,19,1,2,3))
if mibBuilder.loadTexts:dpsvDeviceTable.setStatus(_A)
_DpsvDeviceEntry_Object=MibTableRow
dpsvDeviceEntry=_DpsvDeviceEntry_Object((1,3,6,1,4,1,171,15,19,1,2,3,1))
dpsvDeviceEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:dpsvDeviceEntry.setStatus(_A)
_DpsvDevicePortIfIdx_Type=InterfaceIndex
_DpsvDevicePortIfIdx_Object=MibTableColumn
dpsvDevicePortIfIdx=_DpsvDevicePortIfIdx_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,1),_DpsvDevicePortIfIdx_Type())
dpsvDevicePortIfIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsvDevicePortIfIdx.setStatus(_A)
_DpsvDeviceAddr_Type=MacAddress
_DpsvDeviceAddr_Object=MibTableColumn
dpsvDeviceAddr=_DpsvDeviceAddr_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,2),_DpsvDeviceAddr_Type())
dpsvDeviceAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dpsvDeviceAddr.setStatus(_A)
_DpsvDeviceCompType_Type=OuiComponentType
_DpsvDeviceCompType_Object=MibTableColumn
dpsvDeviceCompType=_DpsvDeviceCompType_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,3),_DpsvDeviceCompType_Type())
dpsvDeviceCompType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvDeviceCompType.setStatus(_A)
class _DpsvDeviceDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpsvDeviceDescr_Type.__name__=_F
_DpsvDeviceDescr_Object=MibTableColumn
dpsvDeviceDescr=_DpsvDeviceDescr_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,4),_DpsvDeviceDescr_Type())
dpsvDeviceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvDeviceDescr.setStatus(_A)
_DpsvDeviceStartTime_Type=DateAndTime
_DpsvDeviceStartTime_Object=MibTableColumn
dpsvDeviceStartTime=_DpsvDeviceStartTime_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,5),_DpsvDeviceStartTime_Type())
dpsvDeviceStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvDeviceStartTime.setStatus(_A)
class _DpsvDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('aging',2)))
_DpsvDeviceStatus_Type.__name__=_J
_DpsvDeviceStatus_Object=MibTableColumn
dpsvDeviceStatus=_DpsvDeviceStatus_Object((1,3,6,1,4,1,171,15,19,1,2,3,1,6),_DpsvDeviceStatus_Type())
dpsvDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dpsvDeviceStatus.setStatus(_A)
_DpsvMIBConformance_ObjectIdentity=ObjectIdentity
dpsvMIBConformance=_DpsvMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,19,2))
_DpsvMIBCompliances_ObjectIdentity=ObjectIdentity
dpsvMIBCompliances=_DpsvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,19,2,1))
_DpsvMIBGroups_ObjectIdentity=ObjectIdentity
dpsvMIBGroups=_DpsvMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,19,2,2))
dpsvBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,19,2,2,1))
dpsvBasicGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dpsvBasicGroup.setStatus(_A)
dpsvOUICfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,19,2,2,2))
dpsvOUICfgGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:dpsvOUICfgGroup.setStatus(_A)
dpsvDeviceInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,19,2,2,3))
dpsvDeviceInfoGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:dpsvDeviceInfoGroup.setStatus(_A)
dpsvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,19,2,1,1))
dpsvMIBCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:dpsvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OuiComponentType':OuiComponentType,'dlinkPrimeSurveillanceVlanMIB':dlinkPrimeSurveillanceVlanMIB,'dpsvMIBNotifications':dpsvMIBNotifications,'dpsvMIBObjects':dpsvMIBObjects,'dpsvGlobal':dpsvGlobal,_O:dpsvEnabled,_P:dpsvVlanId,_Q:dpsvQos,_R:dpsvAgingTime,'dpsvOuiTable':dpsvOuiTable,'dpsvOuiEntry':dpsvOuiEntry,_K:dpsvOuiAddr,_L:dpsvOuiMask,_U:dpsvOuiComponentType,_V:dpsvOuiDescription,_W:dpsvOuiRowStatus,'dpsvInfo':dpsvInfo,_S:dpsvMemberPorts,_T:dpsvDynamicPorts,'dpsvDeviceTable':dpsvDeviceTable,'dpsvDeviceEntry':dpsvDeviceEntry,_M:dpsvDevicePortIfIdx,_N:dpsvDeviceAddr,_X:dpsvDeviceCompType,_Y:dpsvDeviceDescr,_Z:dpsvDeviceStartTime,_a:dpsvDeviceStatus,'dpsvMIBConformance':dpsvMIBConformance,'dpsvMIBCompliances':dpsvMIBCompliances,'dpsvMIBCompliance':dpsvMIBCompliance,'dpsvMIBGroups':dpsvMIBGroups,_b:dpsvBasicGroup,_c:dpsvOUICfgGroup,_d:dpsvDeviceInfoGroup})