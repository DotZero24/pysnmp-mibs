_X='fsVoiceVlanMIBGroup'
_W='fsVoiceVlanMacDescription'
_V='fsVoiceVlanPortMode'
_U='fsVoiceVlanDscp'
_T='fsVoiceVlanCos'
_S='fsVoiceVlanSecurityState'
_R='fsVoiceVlanAgingTime'
_Q='fsVoiceVlanPortStatus'
_P='fsVoiceVlanEnabledId'
_O='fsVoiceVlanOuiRowStatus'
_N='fsVoiceVlanOuiDescription'
_M='fsVoiceVlanOuiMask'
_L='fsVoiceVlanPortIfIndex'
_K='not-accessible'
_J='fsVoiceVlanPortEnableIfIndex'
_I='fsVoiceVlanMacIfIndex'
_H='fsVoiceVlanMacAddress'
_G='fsVoiceVlanOuiAddress'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='FS-VOICE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsVoiceVlanMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,52))
if mibBuilder.loadTexts:fsVoiceVlanMIB.setRevisions(('2009-06-18 00:00',))
_FsVoiceVlanMIBObjects_ObjectIdentity=ObjectIdentity
fsVoiceVlanMIBObjects=_FsVoiceVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,52,1))
_FsVoiceVlanOuiTable_Object=MibTable
fsVoiceVlanOuiTable=_FsVoiceVlanOuiTable_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1))
if mibBuilder.loadTexts:fsVoiceVlanOuiTable.setStatus(_A)
_FsVoiceVlanOuiEntry_Object=MibTableRow
fsVoiceVlanOuiEntry=_FsVoiceVlanOuiEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1,1))
fsVoiceVlanOuiEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsVoiceVlanOuiEntry.setStatus(_A)
_FsVoiceVlanOuiAddress_Type=MacAddress
_FsVoiceVlanOuiAddress_Object=MibTableColumn
fsVoiceVlanOuiAddress=_FsVoiceVlanOuiAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1,1,1),_FsVoiceVlanOuiAddress_Type())
fsVoiceVlanOuiAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVoiceVlanOuiAddress.setStatus(_A)
_FsVoiceVlanOuiMask_Type=MacAddress
_FsVoiceVlanOuiMask_Object=MibTableColumn
fsVoiceVlanOuiMask=_FsVoiceVlanOuiMask_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1,1,2),_FsVoiceVlanOuiMask_Type())
fsVoiceVlanOuiMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanOuiMask.setStatus(_A)
class _FsVoiceVlanOuiDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_FsVoiceVlanOuiDescription_Type.__name__=_F
_FsVoiceVlanOuiDescription_Object=MibTableColumn
fsVoiceVlanOuiDescription=_FsVoiceVlanOuiDescription_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1,1,3),_FsVoiceVlanOuiDescription_Type())
fsVoiceVlanOuiDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanOuiDescription.setStatus(_A)
_FsVoiceVlanOuiRowStatus_Type=RowStatus
_FsVoiceVlanOuiRowStatus_Object=MibTableColumn
fsVoiceVlanOuiRowStatus=_FsVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,1,1,4),_FsVoiceVlanOuiRowStatus_Type())
fsVoiceVlanOuiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanOuiRowStatus.setStatus(_A)
_FsVoiceVlanEnabledId_Type=Integer32
_FsVoiceVlanEnabledId_Object=MibScalar
fsVoiceVlanEnabledId=_FsVoiceVlanEnabledId_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,2),_FsVoiceVlanEnabledId_Type())
fsVoiceVlanEnabledId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanEnabledId.setStatus(_A)
_FsVoiceVlanPortEnableTable_Object=MibTable
fsVoiceVlanPortEnableTable=_FsVoiceVlanPortEnableTable_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,3))
if mibBuilder.loadTexts:fsVoiceVlanPortEnableTable.setStatus(_A)
_FsVoiceVlanPortEnableEntry_Object=MibTableRow
fsVoiceVlanPortEnableEntry=_FsVoiceVlanPortEnableEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,3,1))
fsVoiceVlanPortEnableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsVoiceVlanPortEnableEntry.setStatus(_A)
_FsVoiceVlanPortEnableIfIndex_Type=IfIndex
_FsVoiceVlanPortEnableIfIndex_Object=MibTableColumn
fsVoiceVlanPortEnableIfIndex=_FsVoiceVlanPortEnableIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,3,1,1),_FsVoiceVlanPortEnableIfIndex_Type())
fsVoiceVlanPortEnableIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsVoiceVlanPortEnableIfIndex.setStatus(_A)
_FsVoiceVlanPortStatus_Type=EnabledStatus
_FsVoiceVlanPortStatus_Object=MibTableColumn
fsVoiceVlanPortStatus=_FsVoiceVlanPortStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,3,1,2),_FsVoiceVlanPortStatus_Type())
fsVoiceVlanPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanPortStatus.setStatus(_A)
class _FsVoiceVlanAgingTime_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,10000))
_FsVoiceVlanAgingTime_Type.__name__=_D
_FsVoiceVlanAgingTime_Object=MibScalar
fsVoiceVlanAgingTime=_FsVoiceVlanAgingTime_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,4),_FsVoiceVlanAgingTime_Type())
fsVoiceVlanAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanAgingTime.setStatus(_A)
class _FsVoiceVlanSecurityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('security',1),('normal',2)))
_FsVoiceVlanSecurityState_Type.__name__=_D
_FsVoiceVlanSecurityState_Object=MibScalar
fsVoiceVlanSecurityState=_FsVoiceVlanSecurityState_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,5),_FsVoiceVlanSecurityState_Type())
fsVoiceVlanSecurityState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanSecurityState.setStatus(_A)
class _FsVoiceVlanCos_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsVoiceVlanCos_Type.__name__=_D
_FsVoiceVlanCos_Object=MibScalar
fsVoiceVlanCos=_FsVoiceVlanCos_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,6),_FsVoiceVlanCos_Type())
fsVoiceVlanCos.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanCos.setStatus(_A)
class _FsVoiceVlanDscp_Type(Integer32):defaultValue=46
_FsVoiceVlanDscp_Type.__name__=_D
_FsVoiceVlanDscp_Object=MibScalar
fsVoiceVlanDscp=_FsVoiceVlanDscp_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,7),_FsVoiceVlanDscp_Type())
fsVoiceVlanDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanDscp.setStatus(_A)
_FsVoiceVlanPortModeTable_Object=MibTable
fsVoiceVlanPortModeTable=_FsVoiceVlanPortModeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,8))
if mibBuilder.loadTexts:fsVoiceVlanPortModeTable.setStatus(_A)
_FsVoiceVlanPortModeEntry_Object=MibTableRow
fsVoiceVlanPortModeEntry=_FsVoiceVlanPortModeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,8,1))
fsVoiceVlanPortModeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsVoiceVlanPortModeEntry.setStatus(_A)
_FsVoiceVlanPortIfIndex_Type=IfIndex
_FsVoiceVlanPortIfIndex_Object=MibTableColumn
fsVoiceVlanPortIfIndex=_FsVoiceVlanPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,8,1,1),_FsVoiceVlanPortIfIndex_Type())
fsVoiceVlanPortIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsVoiceVlanPortIfIndex.setStatus(_A)
class _FsVoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_FsVoiceVlanPortMode_Type.__name__=_D
_FsVoiceVlanPortMode_Object=MibTableColumn
fsVoiceVlanPortMode=_FsVoiceVlanPortMode_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,8,1,2),_FsVoiceVlanPortMode_Type())
fsVoiceVlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVoiceVlanPortMode.setStatus(_A)
_FsVoiceVlanMacTable_Object=MibTable
fsVoiceVlanMacTable=_FsVoiceVlanMacTable_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,9))
if mibBuilder.loadTexts:fsVoiceVlanMacTable.setStatus(_A)
_FsVoiceVlanMacEntry_Object=MibTableRow
fsVoiceVlanMacEntry=_FsVoiceVlanMacEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,9,1))
fsVoiceVlanMacEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsVoiceVlanMacEntry.setStatus(_A)
_FsVoiceVlanMacAddress_Type=MacAddress
_FsVoiceVlanMacAddress_Object=MibTableColumn
fsVoiceVlanMacAddress=_FsVoiceVlanMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,9,1,1),_FsVoiceVlanMacAddress_Type())
fsVoiceVlanMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVoiceVlanMacAddress.setStatus(_A)
_FsVoiceVlanMacIfIndex_Type=IfIndex
_FsVoiceVlanMacIfIndex_Object=MibTableColumn
fsVoiceVlanMacIfIndex=_FsVoiceVlanMacIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,9,1,2),_FsVoiceVlanMacIfIndex_Type())
fsVoiceVlanMacIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVoiceVlanMacIfIndex.setStatus(_A)
class _FsVoiceVlanMacDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_FsVoiceVlanMacDescription_Type.__name__=_F
_FsVoiceVlanMacDescription_Object=MibTableColumn
fsVoiceVlanMacDescription=_FsVoiceVlanMacDescription_Object((1,3,6,1,4,1,52642,1,1,10,2,52,1,9,1,3),_FsVoiceVlanMacDescription_Type())
fsVoiceVlanMacDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVoiceVlanMacDescription.setStatus(_A)
_FsVoiceVlanMIBConformance_ObjectIdentity=ObjectIdentity
fsVoiceVlanMIBConformance=_FsVoiceVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,52,2))
_FsVoiceVlanMIBCompliances_ObjectIdentity=ObjectIdentity
fsVoiceVlanMIBCompliances=_FsVoiceVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,52,2,1))
_FsVoiceVlanMIBGroups_ObjectIdentity=ObjectIdentity
fsVoiceVlanMIBGroups=_FsVoiceVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,52,2,2))
fsVoiceVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,52,2,2,1))
fsVoiceVlanMIBGroup.setObjects(*((_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_H),(_B,_I),(_B,_W)))
if mibBuilder.loadTexts:fsVoiceVlanMIBGroup.setStatus(_A)
fsVoiceVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,52,2,1,1))
fsVoiceVlanMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:fsVoiceVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsVoiceVlanMIB':fsVoiceVlanMIB,'fsVoiceVlanMIBObjects':fsVoiceVlanMIBObjects,'fsVoiceVlanOuiTable':fsVoiceVlanOuiTable,'fsVoiceVlanOuiEntry':fsVoiceVlanOuiEntry,_G:fsVoiceVlanOuiAddress,_M:fsVoiceVlanOuiMask,_N:fsVoiceVlanOuiDescription,_O:fsVoiceVlanOuiRowStatus,_P:fsVoiceVlanEnabledId,'fsVoiceVlanPortEnableTable':fsVoiceVlanPortEnableTable,'fsVoiceVlanPortEnableEntry':fsVoiceVlanPortEnableEntry,_J:fsVoiceVlanPortEnableIfIndex,_Q:fsVoiceVlanPortStatus,_R:fsVoiceVlanAgingTime,_S:fsVoiceVlanSecurityState,_T:fsVoiceVlanCos,_U:fsVoiceVlanDscp,'fsVoiceVlanPortModeTable':fsVoiceVlanPortModeTable,'fsVoiceVlanPortModeEntry':fsVoiceVlanPortModeEntry,_L:fsVoiceVlanPortIfIndex,_V:fsVoiceVlanPortMode,'fsVoiceVlanMacTable':fsVoiceVlanMacTable,'fsVoiceVlanMacEntry':fsVoiceVlanMacEntry,_H:fsVoiceVlanMacAddress,_I:fsVoiceVlanMacIfIndex,_W:fsVoiceVlanMacDescription,'fsVoiceVlanMIBConformance':fsVoiceVlanMIBConformance,'fsVoiceVlanMIBCompliances':fsVoiceVlanMIBCompliances,'fsVoiceVlanMIBCompliance':fsVoiceVlanMIBCompliance,'fsVoiceVlanMIBGroups':fsVoiceVlanMIBGroups,_X:fsVoiceVlanMIBGroup})