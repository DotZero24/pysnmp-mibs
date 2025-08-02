_b='dpVoiceVlanDeviceInfoGroup'
_a='dpVoiceVlanOUICfgGroup'
_Z='dpVoiceVlanBasicGroup'
_Y='dpVoiceVlanDeviceStatus'
_X='dpVoiceVlanDeviceStartTime'
_W='dpVoiceVlanOuiRowStatus'
_V='dpVoiceVlanOuiDes'
_U='dpVoiceVlanDynamicMemberPorts'
_T='dpVoiceVlanMemberPorts'
_S='dpVoiceVlanAgingTime'
_R='dpVoiceVlanQos'
_Q='dpVoiceVlanVlanId'
_P='dpVoiceVlanEnabled'
_O='dpVoiceVlanDeviceAddr'
_N='dpVoiceVlanDevicePortIfindex'
_M='dpVoiceVlanIfIndex'
_L='read-create'
_K='dpVoiceVlanOuiMask'
_J='dpVoiceVlanOuiAddr'
_I='SnmpAdminString'
_H='VlanIdOrNone'
_G='Unsigned32'
_F='Integer32'
_E='read-only'
_D='not-accessible'
_C='read-write'
_B='DLINKPRIME-VOICE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeVoiceVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,15,27))
if mibBuilder.loadTexts:dlinkPrimeVoiceVlanMIB.setRevisions(('2014-04-26 00:00',))
_DpVoiceVlanMIBNotifications_ObjectIdentity=ObjectIdentity
dpVoiceVlanMIBNotifications=_DpVoiceVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,27,0))
_DpVoiceVlanMIBObjects_ObjectIdentity=ObjectIdentity
dpVoiceVlanMIBObjects=_DpVoiceVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,27,1))
_DpVoiceVlanGlobal_ObjectIdentity=ObjectIdentity
dpVoiceVlanGlobal=_DpVoiceVlanGlobal_ObjectIdentity((1,3,6,1,4,1,171,15,27,1,1))
_DpVoiceVlanEnabled_Type=TruthValue
_DpVoiceVlanEnabled_Object=MibScalar
dpVoiceVlanEnabled=_DpVoiceVlanEnabled_Object((1,3,6,1,4,1,171,15,27,1,1,1),_DpVoiceVlanEnabled_Type())
dpVoiceVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanEnabled.setStatus(_A)
class _DpVoiceVlanVlanId_Type(VlanIdOrNone):defaultValue=0
_DpVoiceVlanVlanId_Type.__name__=_H
_DpVoiceVlanVlanId_Object=MibScalar
dpVoiceVlanVlanId=_DpVoiceVlanVlanId_Object((1,3,6,1,4,1,171,15,27,1,1,2),_DpVoiceVlanVlanId_Type())
dpVoiceVlanVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanVlanId.setStatus(_A)
class _DpVoiceVlanQos_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DpVoiceVlanQos_Type.__name__=_G
_DpVoiceVlanQos_Object=MibScalar
dpVoiceVlanQos=_DpVoiceVlanQos_Object((1,3,6,1,4,1,171,15,27,1,1,3),_DpVoiceVlanQos_Type())
dpVoiceVlanQos.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanQos.setStatus(_A)
class _DpVoiceVlanAgingTime_Type(Unsigned32):defaultValue=720;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DpVoiceVlanAgingTime_Type.__name__=_G
_DpVoiceVlanAgingTime_Object=MibScalar
dpVoiceVlanAgingTime=_DpVoiceVlanAgingTime_Object((1,3,6,1,4,1,171,15,27,1,1,4),_DpVoiceVlanAgingTime_Type())
dpVoiceVlanAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanAgingTime.setStatus(_A)
if mibBuilder.loadTexts:dpVoiceVlanAgingTime.setUnits('minutes')
_DpVoiceVlanOuiTable_Object=MibTable
dpVoiceVlanOuiTable=_DpVoiceVlanOuiTable_Object((1,3,6,1,4,1,171,15,27,1,1,5))
if mibBuilder.loadTexts:dpVoiceVlanOuiTable.setStatus(_A)
_DpVoiceVlanOuiEntry_Object=MibTableRow
dpVoiceVlanOuiEntry=_DpVoiceVlanOuiEntry_Object((1,3,6,1,4,1,171,15,27,1,1,5,1))
dpVoiceVlanOuiEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:dpVoiceVlanOuiEntry.setStatus(_A)
_DpVoiceVlanOuiAddr_Type=MacAddress
_DpVoiceVlanOuiAddr_Object=MibTableColumn
dpVoiceVlanOuiAddr=_DpVoiceVlanOuiAddr_Object((1,3,6,1,4,1,171,15,27,1,1,5,1,1),_DpVoiceVlanOuiAddr_Type())
dpVoiceVlanOuiAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dpVoiceVlanOuiAddr.setStatus(_A)
_DpVoiceVlanOuiMask_Type=MacAddress
_DpVoiceVlanOuiMask_Object=MibTableColumn
dpVoiceVlanOuiMask=_DpVoiceVlanOuiMask_Object((1,3,6,1,4,1,171,15,27,1,1,5,1,2),_DpVoiceVlanOuiMask_Type())
dpVoiceVlanOuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dpVoiceVlanOuiMask.setStatus(_A)
class _DpVoiceVlanOuiDes_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DpVoiceVlanOuiDes_Type.__name__=_I
_DpVoiceVlanOuiDes_Object=MibTableColumn
dpVoiceVlanOuiDes=_DpVoiceVlanOuiDes_Object((1,3,6,1,4,1,171,15,27,1,1,5,1,3),_DpVoiceVlanOuiDes_Type())
dpVoiceVlanOuiDes.setMaxAccess(_L)
if mibBuilder.loadTexts:dpVoiceVlanOuiDes.setStatus(_A)
_DpVoiceVlanOuiRowStatus_Type=RowStatus
_DpVoiceVlanOuiRowStatus_Object=MibTableColumn
dpVoiceVlanOuiRowStatus=_DpVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,171,15,27,1,1,5,1,4),_DpVoiceVlanOuiRowStatus_Type())
dpVoiceVlanOuiRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:dpVoiceVlanOuiRowStatus.setStatus(_A)
_DpVoiceVlanInterface_ObjectIdentity=ObjectIdentity
dpVoiceVlanInterface=_DpVoiceVlanInterface_ObjectIdentity((1,3,6,1,4,1,171,15,27,1,2))
_DpVoiceVlanInterfaceTable_Object=MibTable
dpVoiceVlanInterfaceTable=_DpVoiceVlanInterfaceTable_Object((1,3,6,1,4,1,171,15,27,1,2,1))
if mibBuilder.loadTexts:dpVoiceVlanInterfaceTable.setStatus(_A)
_DpVoiceVlanInterfaceEntry_Object=MibTableRow
dpVoiceVlanInterfaceEntry=_DpVoiceVlanInterfaceEntry_Object((1,3,6,1,4,1,171,15,27,1,2,1,1))
dpVoiceVlanInterfaceEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:dpVoiceVlanInterfaceEntry.setStatus(_A)
_DpVoiceVlanIfIndex_Type=InterfaceIndex
_DpVoiceVlanIfIndex_Object=MibTableColumn
dpVoiceVlanIfIndex=_DpVoiceVlanIfIndex_Object((1,3,6,1,4,1,171,15,27,1,2,1,1,1),_DpVoiceVlanIfIndex_Type())
dpVoiceVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dpVoiceVlanIfIndex.setStatus(_A)
_DpVoiceVlanIfEnabled_Type=TruthValue
_DpVoiceVlanIfEnabled_Object=MibTableColumn
dpVoiceVlanIfEnabled=_DpVoiceVlanIfEnabled_Object((1,3,6,1,4,1,171,15,27,1,2,1,1,2),_DpVoiceVlanIfEnabled_Type())
dpVoiceVlanIfEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanIfEnabled.setStatus(_A)
class _DpVoiceVlanIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('autoUntagged',1),('autoTagged',2),('manual',3)))
_DpVoiceVlanIfMode_Type.__name__=_F
_DpVoiceVlanIfMode_Object=MibTableColumn
dpVoiceVlanIfMode=_DpVoiceVlanIfMode_Object((1,3,6,1,4,1,171,15,27,1,2,1,1,3),_DpVoiceVlanIfMode_Type())
dpVoiceVlanIfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVoiceVlanIfMode.setStatus(_A)
_DpVoiceVlanInfo_ObjectIdentity=ObjectIdentity
dpVoiceVlanInfo=_DpVoiceVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,15,27,1,3))
_DpVoiceVlanMemberPorts_Type=PortList
_DpVoiceVlanMemberPorts_Object=MibScalar
dpVoiceVlanMemberPorts=_DpVoiceVlanMemberPorts_Object((1,3,6,1,4,1,171,15,27,1,3,1),_DpVoiceVlanMemberPorts_Type())
dpVoiceVlanMemberPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dpVoiceVlanMemberPorts.setStatus(_A)
_DpVoiceVlanDynamicMemberPorts_Type=PortList
_DpVoiceVlanDynamicMemberPorts_Object=MibScalar
dpVoiceVlanDynamicMemberPorts=_DpVoiceVlanDynamicMemberPorts_Object((1,3,6,1,4,1,171,15,27,1,3,2),_DpVoiceVlanDynamicMemberPorts_Type())
dpVoiceVlanDynamicMemberPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dpVoiceVlanDynamicMemberPorts.setStatus(_A)
_DpVoiceVlanDeviceTable_Object=MibTable
dpVoiceVlanDeviceTable=_DpVoiceVlanDeviceTable_Object((1,3,6,1,4,1,171,15,27,1,3,3))
if mibBuilder.loadTexts:dpVoiceVlanDeviceTable.setStatus(_A)
_DpVoiceVlanDeviceEntry_Object=MibTableRow
dpVoiceVlanDeviceEntry=_DpVoiceVlanDeviceEntry_Object((1,3,6,1,4,1,171,15,27,1,3,3,1))
dpVoiceVlanDeviceEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:dpVoiceVlanDeviceEntry.setStatus(_A)
_DpVoiceVlanDevicePortIfindex_Type=InterfaceIndex
_DpVoiceVlanDevicePortIfindex_Object=MibTableColumn
dpVoiceVlanDevicePortIfindex=_DpVoiceVlanDevicePortIfindex_Object((1,3,6,1,4,1,171,15,27,1,3,3,1,1),_DpVoiceVlanDevicePortIfindex_Type())
dpVoiceVlanDevicePortIfindex.setMaxAccess(_D)
if mibBuilder.loadTexts:dpVoiceVlanDevicePortIfindex.setStatus(_A)
_DpVoiceVlanDeviceAddr_Type=MacAddress
_DpVoiceVlanDeviceAddr_Object=MibTableColumn
dpVoiceVlanDeviceAddr=_DpVoiceVlanDeviceAddr_Object((1,3,6,1,4,1,171,15,27,1,3,3,1,2),_DpVoiceVlanDeviceAddr_Type())
dpVoiceVlanDeviceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dpVoiceVlanDeviceAddr.setStatus(_A)
_DpVoiceVlanDeviceStartTime_Type=DateAndTime
_DpVoiceVlanDeviceStartTime_Object=MibTableColumn
dpVoiceVlanDeviceStartTime=_DpVoiceVlanDeviceStartTime_Object((1,3,6,1,4,1,171,15,27,1,3,3,1,3),_DpVoiceVlanDeviceStartTime_Type())
dpVoiceVlanDeviceStartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:dpVoiceVlanDeviceStartTime.setStatus(_A)
class _DpVoiceVlanDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('aging',2)))
_DpVoiceVlanDeviceStatus_Type.__name__=_F
_DpVoiceVlanDeviceStatus_Object=MibTableColumn
dpVoiceVlanDeviceStatus=_DpVoiceVlanDeviceStatus_Object((1,3,6,1,4,1,171,15,27,1,3,3,1,4),_DpVoiceVlanDeviceStatus_Type())
dpVoiceVlanDeviceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpVoiceVlanDeviceStatus.setStatus(_A)
_DpVoiceVlanMIBConformance_ObjectIdentity=ObjectIdentity
dpVoiceVlanMIBConformance=_DpVoiceVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,27,2))
_DpVoiceVlanMIBCompliances_ObjectIdentity=ObjectIdentity
dpVoiceVlanMIBCompliances=_DpVoiceVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,27,2,1))
_DpVoiceVlanMIBGroups_ObjectIdentity=ObjectIdentity
dpVoiceVlanMIBGroups=_DpVoiceVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,27,2,2))
dpVoiceVlanBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,27,2,2,1))
dpVoiceVlanBasicGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:dpVoiceVlanBasicGroup.setStatus(_A)
dpVoiceVlanOUICfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,27,2,2,2))
dpVoiceVlanOUICfgGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:dpVoiceVlanOUICfgGroup.setStatus(_A)
dpVoiceVlanDeviceInfoGroup=ObjectGroup((1,3,6,1,4,1,171,15,27,2,2,3))
dpVoiceVlanDeviceInfoGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:dpVoiceVlanDeviceInfoGroup.setStatus(_A)
dpVoiceVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,27,2,1,1))
dpVoiceVlanMIBCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:dpVoiceVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeVoiceVlanMIB':dlinkPrimeVoiceVlanMIB,'dpVoiceVlanMIBNotifications':dpVoiceVlanMIBNotifications,'dpVoiceVlanMIBObjects':dpVoiceVlanMIBObjects,'dpVoiceVlanGlobal':dpVoiceVlanGlobal,_P:dpVoiceVlanEnabled,_Q:dpVoiceVlanVlanId,_R:dpVoiceVlanQos,_S:dpVoiceVlanAgingTime,'dpVoiceVlanOuiTable':dpVoiceVlanOuiTable,'dpVoiceVlanOuiEntry':dpVoiceVlanOuiEntry,_J:dpVoiceVlanOuiAddr,_K:dpVoiceVlanOuiMask,_V:dpVoiceVlanOuiDes,_W:dpVoiceVlanOuiRowStatus,'dpVoiceVlanInterface':dpVoiceVlanInterface,'dpVoiceVlanInterfaceTable':dpVoiceVlanInterfaceTable,'dpVoiceVlanInterfaceEntry':dpVoiceVlanInterfaceEntry,_M:dpVoiceVlanIfIndex,'dpVoiceVlanIfEnabled':dpVoiceVlanIfEnabled,'dpVoiceVlanIfMode':dpVoiceVlanIfMode,'dpVoiceVlanInfo':dpVoiceVlanInfo,_T:dpVoiceVlanMemberPorts,_U:dpVoiceVlanDynamicMemberPorts,'dpVoiceVlanDeviceTable':dpVoiceVlanDeviceTable,'dpVoiceVlanDeviceEntry':dpVoiceVlanDeviceEntry,_N:dpVoiceVlanDevicePortIfindex,_O:dpVoiceVlanDeviceAddr,_X:dpVoiceVlanDeviceStartTime,_Y:dpVoiceVlanDeviceStatus,'dpVoiceVlanMIBConformance':dpVoiceVlanMIBConformance,'dpVoiceVlanMIBCompliances':dpVoiceVlanMIBCompliances,'dpVoiceVlanMIBCompliance':dpVoiceVlanMIBCompliance,'dpVoiceVlanMIBGroups':dpVoiceVlanMIBGroups,_Z:dpVoiceVlanBasicGroup,_a:dpVoiceVlanOUICfgGroup,_b:dpVoiceVlanDeviceInfoGroup})