_X='qtechVoiceVlanMIBGroup'
_W='qtechVoiceVlanMacDescription'
_V='qtechVoiceVlanPortMode'
_U='qtechVoiceVlanDscp'
_T='qtechVoiceVlanCos'
_S='qtechVoiceVlanSecurityState'
_R='qtechVoiceVlanAgingTime'
_Q='qtechVoiceVlanPortStatus'
_P='qtechVoiceVlanEnabledId'
_O='qtechVoiceVlanOuiRowStatus'
_N='qtechVoiceVlanOuiDescription'
_M='qtechVoiceVlanOuiMask'
_L='qtechVoiceVlanPortIfIndex'
_K='not-accessible'
_J='qtechVoiceVlanPortEnableIfIndex'
_I='qtechVoiceVlanMacIfIndex'
_H='qtechVoiceVlanMacAddress'
_G='qtechVoiceVlanOuiAddress'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='QTECH-VOICE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
qtechVoiceVlanMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,52))
if mibBuilder.loadTexts:qtechVoiceVlanMIB.setRevisions(('2009-06-18 00:00',))
_QtechVoiceVlanMIBObjects_ObjectIdentity=ObjectIdentity
qtechVoiceVlanMIBObjects=_QtechVoiceVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,52,1))
_QtechVoiceVlanOuiTable_Object=MibTable
qtechVoiceVlanOuiTable=_QtechVoiceVlanOuiTable_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1))
if mibBuilder.loadTexts:qtechVoiceVlanOuiTable.setStatus(_A)
_QtechVoiceVlanOuiEntry_Object=MibTableRow
qtechVoiceVlanOuiEntry=_QtechVoiceVlanOuiEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1,1))
qtechVoiceVlanOuiEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechVoiceVlanOuiEntry.setStatus(_A)
_QtechVoiceVlanOuiAddress_Type=MacAddress
_QtechVoiceVlanOuiAddress_Object=MibTableColumn
qtechVoiceVlanOuiAddress=_QtechVoiceVlanOuiAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1,1,1),_QtechVoiceVlanOuiAddress_Type())
qtechVoiceVlanOuiAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVoiceVlanOuiAddress.setStatus(_A)
_QtechVoiceVlanOuiMask_Type=MacAddress
_QtechVoiceVlanOuiMask_Object=MibTableColumn
qtechVoiceVlanOuiMask=_QtechVoiceVlanOuiMask_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1,1,2),_QtechVoiceVlanOuiMask_Type())
qtechVoiceVlanOuiMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanOuiMask.setStatus(_A)
class _QtechVoiceVlanOuiDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_QtechVoiceVlanOuiDescription_Type.__name__=_F
_QtechVoiceVlanOuiDescription_Object=MibTableColumn
qtechVoiceVlanOuiDescription=_QtechVoiceVlanOuiDescription_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1,1,3),_QtechVoiceVlanOuiDescription_Type())
qtechVoiceVlanOuiDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanOuiDescription.setStatus(_A)
_QtechVoiceVlanOuiRowStatus_Type=RowStatus
_QtechVoiceVlanOuiRowStatus_Object=MibTableColumn
qtechVoiceVlanOuiRowStatus=_QtechVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,1,1,4),_QtechVoiceVlanOuiRowStatus_Type())
qtechVoiceVlanOuiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanOuiRowStatus.setStatus(_A)
_QtechVoiceVlanEnabledId_Type=Integer32
_QtechVoiceVlanEnabledId_Object=MibScalar
qtechVoiceVlanEnabledId=_QtechVoiceVlanEnabledId_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,2),_QtechVoiceVlanEnabledId_Type())
qtechVoiceVlanEnabledId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanEnabledId.setStatus(_A)
_QtechVoiceVlanPortEnableTable_Object=MibTable
qtechVoiceVlanPortEnableTable=_QtechVoiceVlanPortEnableTable_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,3))
if mibBuilder.loadTexts:qtechVoiceVlanPortEnableTable.setStatus(_A)
_QtechVoiceVlanPortEnableEntry_Object=MibTableRow
qtechVoiceVlanPortEnableEntry=_QtechVoiceVlanPortEnableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,3,1))
qtechVoiceVlanPortEnableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechVoiceVlanPortEnableEntry.setStatus(_A)
_QtechVoiceVlanPortEnableIfIndex_Type=IfIndex
_QtechVoiceVlanPortEnableIfIndex_Object=MibTableColumn
qtechVoiceVlanPortEnableIfIndex=_QtechVoiceVlanPortEnableIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,3,1,1),_QtechVoiceVlanPortEnableIfIndex_Type())
qtechVoiceVlanPortEnableIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:qtechVoiceVlanPortEnableIfIndex.setStatus(_A)
_QtechVoiceVlanPortStatus_Type=EnabledStatus
_QtechVoiceVlanPortStatus_Object=MibTableColumn
qtechVoiceVlanPortStatus=_QtechVoiceVlanPortStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,3,1,2),_QtechVoiceVlanPortStatus_Type())
qtechVoiceVlanPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanPortStatus.setStatus(_A)
class _QtechVoiceVlanAgingTime_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,10000))
_QtechVoiceVlanAgingTime_Type.__name__=_D
_QtechVoiceVlanAgingTime_Object=MibScalar
qtechVoiceVlanAgingTime=_QtechVoiceVlanAgingTime_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,4),_QtechVoiceVlanAgingTime_Type())
qtechVoiceVlanAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanAgingTime.setStatus(_A)
class _QtechVoiceVlanSecurityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('security',1),('normal',2)))
_QtechVoiceVlanSecurityState_Type.__name__=_D
_QtechVoiceVlanSecurityState_Object=MibScalar
qtechVoiceVlanSecurityState=_QtechVoiceVlanSecurityState_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,5),_QtechVoiceVlanSecurityState_Type())
qtechVoiceVlanSecurityState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanSecurityState.setStatus(_A)
class _QtechVoiceVlanCos_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechVoiceVlanCos_Type.__name__=_D
_QtechVoiceVlanCos_Object=MibScalar
qtechVoiceVlanCos=_QtechVoiceVlanCos_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,6),_QtechVoiceVlanCos_Type())
qtechVoiceVlanCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanCos.setStatus(_A)
class _QtechVoiceVlanDscp_Type(Integer32):defaultValue=46
_QtechVoiceVlanDscp_Type.__name__=_D
_QtechVoiceVlanDscp_Object=MibScalar
qtechVoiceVlanDscp=_QtechVoiceVlanDscp_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,7),_QtechVoiceVlanDscp_Type())
qtechVoiceVlanDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanDscp.setStatus(_A)
_QtechVoiceVlanPortModeTable_Object=MibTable
qtechVoiceVlanPortModeTable=_QtechVoiceVlanPortModeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,8))
if mibBuilder.loadTexts:qtechVoiceVlanPortModeTable.setStatus(_A)
_QtechVoiceVlanPortModeEntry_Object=MibTableRow
qtechVoiceVlanPortModeEntry=_QtechVoiceVlanPortModeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,8,1))
qtechVoiceVlanPortModeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qtechVoiceVlanPortModeEntry.setStatus(_A)
_QtechVoiceVlanPortIfIndex_Type=IfIndex
_QtechVoiceVlanPortIfIndex_Object=MibTableColumn
qtechVoiceVlanPortIfIndex=_QtechVoiceVlanPortIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,8,1,1),_QtechVoiceVlanPortIfIndex_Type())
qtechVoiceVlanPortIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:qtechVoiceVlanPortIfIndex.setStatus(_A)
class _QtechVoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_QtechVoiceVlanPortMode_Type.__name__=_D
_QtechVoiceVlanPortMode_Object=MibTableColumn
qtechVoiceVlanPortMode=_QtechVoiceVlanPortMode_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,8,1,2),_QtechVoiceVlanPortMode_Type())
qtechVoiceVlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVoiceVlanPortMode.setStatus(_A)
_QtechVoiceVlanMacTable_Object=MibTable
qtechVoiceVlanMacTable=_QtechVoiceVlanMacTable_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,9))
if mibBuilder.loadTexts:qtechVoiceVlanMacTable.setStatus(_A)
_QtechVoiceVlanMacEntry_Object=MibTableRow
qtechVoiceVlanMacEntry=_QtechVoiceVlanMacEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,9,1))
qtechVoiceVlanMacEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechVoiceVlanMacEntry.setStatus(_A)
_QtechVoiceVlanMacAddress_Type=MacAddress
_QtechVoiceVlanMacAddress_Object=MibTableColumn
qtechVoiceVlanMacAddress=_QtechVoiceVlanMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,9,1,1),_QtechVoiceVlanMacAddress_Type())
qtechVoiceVlanMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVoiceVlanMacAddress.setStatus(_A)
_QtechVoiceVlanMacIfIndex_Type=IfIndex
_QtechVoiceVlanMacIfIndex_Object=MibTableColumn
qtechVoiceVlanMacIfIndex=_QtechVoiceVlanMacIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,9,1,2),_QtechVoiceVlanMacIfIndex_Type())
qtechVoiceVlanMacIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVoiceVlanMacIfIndex.setStatus(_A)
class _QtechVoiceVlanMacDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_QtechVoiceVlanMacDescription_Type.__name__=_F
_QtechVoiceVlanMacDescription_Object=MibTableColumn
qtechVoiceVlanMacDescription=_QtechVoiceVlanMacDescription_Object((1,3,6,1,4,1,27514,1,1,10,2,52,1,9,1,3),_QtechVoiceVlanMacDescription_Type())
qtechVoiceVlanMacDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVoiceVlanMacDescription.setStatus(_A)
_QtechVoiceVlanMIBConformance_ObjectIdentity=ObjectIdentity
qtechVoiceVlanMIBConformance=_QtechVoiceVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,52,2))
_QtechVoiceVlanMIBCompliances_ObjectIdentity=ObjectIdentity
qtechVoiceVlanMIBCompliances=_QtechVoiceVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,52,2,1))
_QtechVoiceVlanMIBGroups_ObjectIdentity=ObjectIdentity
qtechVoiceVlanMIBGroups=_QtechVoiceVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,52,2,2))
qtechVoiceVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,52,2,2,1))
qtechVoiceVlanMIBGroup.setObjects(*((_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_H),(_B,_I),(_B,_W)))
if mibBuilder.loadTexts:qtechVoiceVlanMIBGroup.setStatus(_A)
qtechVoiceVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,52,2,1,1))
qtechVoiceVlanMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:qtechVoiceVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechVoiceVlanMIB':qtechVoiceVlanMIB,'qtechVoiceVlanMIBObjects':qtechVoiceVlanMIBObjects,'qtechVoiceVlanOuiTable':qtechVoiceVlanOuiTable,'qtechVoiceVlanOuiEntry':qtechVoiceVlanOuiEntry,_G:qtechVoiceVlanOuiAddress,_M:qtechVoiceVlanOuiMask,_N:qtechVoiceVlanOuiDescription,_O:qtechVoiceVlanOuiRowStatus,_P:qtechVoiceVlanEnabledId,'qtechVoiceVlanPortEnableTable':qtechVoiceVlanPortEnableTable,'qtechVoiceVlanPortEnableEntry':qtechVoiceVlanPortEnableEntry,_J:qtechVoiceVlanPortEnableIfIndex,_Q:qtechVoiceVlanPortStatus,_R:qtechVoiceVlanAgingTime,_S:qtechVoiceVlanSecurityState,_T:qtechVoiceVlanCos,_U:qtechVoiceVlanDscp,'qtechVoiceVlanPortModeTable':qtechVoiceVlanPortModeTable,'qtechVoiceVlanPortModeEntry':qtechVoiceVlanPortModeEntry,_L:qtechVoiceVlanPortIfIndex,_V:qtechVoiceVlanPortMode,'qtechVoiceVlanMacTable':qtechVoiceVlanMacTable,'qtechVoiceVlanMacEntry':qtechVoiceVlanMacEntry,_H:qtechVoiceVlanMacAddress,_I:qtechVoiceVlanMacIfIndex,_W:qtechVoiceVlanMacDescription,'qtechVoiceVlanMIBConformance':qtechVoiceVlanMIBConformance,'qtechVoiceVlanMIBCompliances':qtechVoiceVlanMIBCompliances,'qtechVoiceVlanMIBCompliance':qtechVoiceVlanMIBCompliance,'qtechVoiceVlanMIBGroups':qtechVoiceVlanMIBGroups,_X:qtechVoiceVlanMIBGroup})