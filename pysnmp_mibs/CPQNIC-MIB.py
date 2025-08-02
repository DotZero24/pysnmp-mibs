_m='cpqNicFlexLomPhySlot'
_l='cpqNicIfVlanMapIndex'
_k='cpqNicPhyAdapBaseMemIndex'
_j='active'
_i='standby'
_h='cpqNicIfPhysAdapterIndex'
_g='cpqNicIfLogMapIndex'
_f='cpqNicOsCommonModuleIndex'
_e='NotificationType'
_d='none'
_c='other'
_b='degraded'
_a='cpqNicIfLogMapIPV6Address'
_Z='failed'
_Y='ok'
_X='OctetString'
_W='cpqNicIfLogMapAdapterOKCount'
_V='deprecated'
_U='unknown'
_T='cpqNicIfPhysAdapterStatus'
_S='ipAdEntAddr'
_R='IP-MIB'
_Q='cpqNicIfPhysAdapterPartNumber'
_P='cpqSePciSlotBoardName'
_O='CPQSTDEQ-MIB'
_N='cpqNicIfPhysAdapterPort'
_M='DisplayString'
_L='cpqSiServerSystemId'
_K='CPQSINFO-MIB'
_J='cpqNicIfPhysAdapterSlot'
_I='sysName'
_H='SNMPv2-MIB'
_G='cpqHoTrapFlags'
_F='CPQHOST-MIB'
_E='optional'
_D='Integer32'
_C='CPQNIC-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_F,'compaq',_G)
cpqSiServerSystemId,=mibBuilder.importSymbols(_K,_L)
cpqSePciSlotBoardName,=mibBuilder.importSymbols(_O,_P)
ipAdEntAddr,=mibBuilder.importSymbols(_R,_S)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_H,_I)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_e,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_e,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
_CpqNic_ObjectIdentity=ObjectIdentity
cpqNic=_CpqNic_ObjectIdentity((1,3,6,1,4,1,232,18))
_CpqNicMibRev_ObjectIdentity=ObjectIdentity
cpqNicMibRev=_CpqNicMibRev_ObjectIdentity((1,3,6,1,4,1,232,18,1))
class _CpqNicMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqNicMibRevMajor_Type.__name__=_D
_CpqNicMibRevMajor_Object=MibScalar
cpqNicMibRevMajor=_CpqNicMibRevMajor_Object((1,3,6,1,4,1,232,18,1,1),_CpqNicMibRevMajor_Type())
cpqNicMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicMibRevMajor.setStatus(_B)
class _CpqNicMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicMibRevMinor_Type.__name__=_D
_CpqNicMibRevMinor_Object=MibScalar
cpqNicMibRevMinor=_CpqNicMibRevMinor_Object((1,3,6,1,4,1,232,18,1,2),_CpqNicMibRevMinor_Type())
cpqNicMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicMibRevMinor.setStatus(_B)
class _CpqNicMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),(_b,3),(_Z,4)))
_CpqNicMibCondition_Type.__name__=_D
_CpqNicMibCondition_Object=MibScalar
cpqNicMibCondition=_CpqNicMibCondition_Object((1,3,6,1,4,1,232,18,1,3),_CpqNicMibCondition_Type())
cpqNicMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicMibCondition.setStatus(_B)
_CpqNicComponent_ObjectIdentity=ObjectIdentity
cpqNicComponent=_CpqNicComponent_ObjectIdentity((1,3,6,1,4,1,232,18,2))
_CpqNicInterface_ObjectIdentity=ObjectIdentity
cpqNicInterface=_CpqNicInterface_ObjectIdentity((1,3,6,1,4,1,232,18,2,1))
_CpqNicOsCommon_ObjectIdentity=ObjectIdentity
cpqNicOsCommon=_CpqNicOsCommon_ObjectIdentity((1,3,6,1,4,1,232,18,2,1,4))
class _CpqNicOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicOsCommonPollFreq_Type.__name__=_D
_CpqNicOsCommonPollFreq_Object=MibScalar
cpqNicOsCommonPollFreq=_CpqNicOsCommonPollFreq_Object((1,3,6,1,4,1,232,18,2,1,4,1),_CpqNicOsCommonPollFreq_Type())
cpqNicOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqNicOsCommonPollFreq.setStatus(_B)
_CpqNicOsCommonModuleTable_Object=MibTable
cpqNicOsCommonModuleTable=_CpqNicOsCommonModuleTable_Object((1,3,6,1,4,1,232,18,2,1,4,2))
if mibBuilder.loadTexts:cpqNicOsCommonModuleTable.setStatus(_V)
_CpqNicOsCommonModuleEntry_Object=MibTableRow
cpqNicOsCommonModuleEntry=_CpqNicOsCommonModuleEntry_Object((1,3,6,1,4,1,232,18,2,1,4,2,1))
cpqNicOsCommonModuleEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cpqNicOsCommonModuleEntry.setStatus(_V)
class _CpqNicOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqNicOsCommonModuleIndex_Type.__name__=_D
_CpqNicOsCommonModuleIndex_Object=MibTableColumn
cpqNicOsCommonModuleIndex=_CpqNicOsCommonModuleIndex_Object((1,3,6,1,4,1,232,18,2,1,4,2,1,1),_CpqNicOsCommonModuleIndex_Type())
cpqNicOsCommonModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicOsCommonModuleIndex.setStatus(_V)
class _CpqNicOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicOsCommonModuleName_Type.__name__=_M
_CpqNicOsCommonModuleName_Object=MibTableColumn
cpqNicOsCommonModuleName=_CpqNicOsCommonModuleName_Object((1,3,6,1,4,1,232,18,2,1,4,2,1,2),_CpqNicOsCommonModuleName_Type())
cpqNicOsCommonModuleName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicOsCommonModuleName.setStatus(_V)
class _CpqNicOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqNicOsCommonModuleVersion_Type.__name__=_M
_CpqNicOsCommonModuleVersion_Object=MibTableColumn
cpqNicOsCommonModuleVersion=_CpqNicOsCommonModuleVersion_Object((1,3,6,1,4,1,232,18,2,1,4,2,1,3),_CpqNicOsCommonModuleVersion_Type())
cpqNicOsCommonModuleVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicOsCommonModuleVersion.setStatus(_V)
class _CpqNicOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqNicOsCommonModuleDate_Type.__name__=_X
_CpqNicOsCommonModuleDate_Object=MibTableColumn
cpqNicOsCommonModuleDate=_CpqNicOsCommonModuleDate_Object((1,3,6,1,4,1,232,18,2,1,4,2,1,4),_CpqNicOsCommonModuleDate_Type())
cpqNicOsCommonModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicOsCommonModuleDate.setStatus(_V)
class _CpqNicOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicOsCommonModulePurpose_Type.__name__=_M
_CpqNicOsCommonModulePurpose_Object=MibTableColumn
cpqNicOsCommonModulePurpose=_CpqNicOsCommonModulePurpose_Object((1,3,6,1,4,1,232,18,2,1,4,2,1,5),_CpqNicOsCommonModulePurpose_Type())
cpqNicOsCommonModulePurpose.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicOsCommonModulePurpose.setStatus(_V)
_CpqNicIfLogMap_ObjectIdentity=ObjectIdentity
cpqNicIfLogMap=_CpqNicIfLogMap_ObjectIdentity((1,3,6,1,4,1,232,18,2,2))
_CpqNicIfLogMapTable_Object=MibTable
cpqNicIfLogMapTable=_CpqNicIfLogMapTable_Object((1,3,6,1,4,1,232,18,2,2,1))
if mibBuilder.loadTexts:cpqNicIfLogMapTable.setStatus(_B)
_CpqNicIfLogMapEntry_Object=MibTableRow
cpqNicIfLogMapEntry=_CpqNicIfLogMapEntry_Object((1,3,6,1,4,1,232,18,2,2,1,1))
cpqNicIfLogMapEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cpqNicIfLogMapEntry.setStatus(_B)
class _CpqNicIfLogMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicIfLogMapIndex_Type.__name__=_D
_CpqNicIfLogMapIndex_Object=MibTableColumn
cpqNicIfLogMapIndex=_CpqNicIfLogMapIndex_Object((1,3,6,1,4,1,232,18,2,2,1,1,1),_CpqNicIfLogMapIndex_Type())
cpqNicIfLogMapIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapIndex.setStatus(_B)
_CpqNicIfLogMapIfNumber_Type=OctetString
_CpqNicIfLogMapIfNumber_Object=MibTableColumn
cpqNicIfLogMapIfNumber=_CpqNicIfLogMapIfNumber_Object((1,3,6,1,4,1,232,18,2,2,1,1,2),_CpqNicIfLogMapIfNumber_Type())
cpqNicIfLogMapIfNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapIfNumber.setStatus(_B)
class _CpqNicIfLogMapDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfLogMapDescription_Type.__name__=_M
_CpqNicIfLogMapDescription_Object=MibTableColumn
cpqNicIfLogMapDescription=_CpqNicIfLogMapDescription_Object((1,3,6,1,4,1,232,18,2,2,1,1,3),_CpqNicIfLogMapDescription_Type())
cpqNicIfLogMapDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapDescription.setStatus(_B)
class _CpqNicIfLogMapGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_U,1),(_d,2),('redundantPair',3),('nft',4),('alb',5),('fec',6),('gec',7),('ad',8),('slb',9),('tlb',10),('redundancySet',11),('switchInd',12),('lacp',13),('team',14)))
_CpqNicIfLogMapGroupType_Type.__name__=_D
_CpqNicIfLogMapGroupType_Object=MibTableColumn
cpqNicIfLogMapGroupType=_CpqNicIfLogMapGroupType_Object((1,3,6,1,4,1,232,18,2,2,1,1,4),_CpqNicIfLogMapGroupType_Type())
cpqNicIfLogMapGroupType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapGroupType.setStatus(_B)
class _CpqNicIfLogMapAdapterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CpqNicIfLogMapAdapterCount_Type.__name__=_D
_CpqNicIfLogMapAdapterCount_Object=MibTableColumn
cpqNicIfLogMapAdapterCount=_CpqNicIfLogMapAdapterCount_Object((1,3,6,1,4,1,232,18,2,2,1,1,5),_CpqNicIfLogMapAdapterCount_Type())
cpqNicIfLogMapAdapterCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapAdapterCount.setStatus(_B)
class _CpqNicIfLogMapAdapterOKCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CpqNicIfLogMapAdapterOKCount_Type.__name__=_D
_CpqNicIfLogMapAdapterOKCount_Object=MibTableColumn
cpqNicIfLogMapAdapterOKCount=_CpqNicIfLogMapAdapterOKCount_Object((1,3,6,1,4,1,232,18,2,2,1,1,6),_CpqNicIfLogMapAdapterOKCount_Type())
cpqNicIfLogMapAdapterOKCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapAdapterOKCount.setStatus(_B)
class _CpqNicIfLogMapPhysicalAdapters_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqNicIfLogMapPhysicalAdapters_Type.__name__=_X
_CpqNicIfLogMapPhysicalAdapters_Object=MibTableColumn
cpqNicIfLogMapPhysicalAdapters=_CpqNicIfLogMapPhysicalAdapters_Object((1,3,6,1,4,1,232,18,2,2,1,1,7),_CpqNicIfLogMapPhysicalAdapters_Type())
cpqNicIfLogMapPhysicalAdapters.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapPhysicalAdapters.setStatus(_B)
class _CpqNicIfLogMapMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CpqNicIfLogMapMACAddress_Type.__name__=_X
_CpqNicIfLogMapMACAddress_Object=MibTableColumn
cpqNicIfLogMapMACAddress=_CpqNicIfLogMapMACAddress_Object((1,3,6,1,4,1,232,18,2,2,1,1,8),_CpqNicIfLogMapMACAddress_Type())
cpqNicIfLogMapMACAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapMACAddress.setStatus(_B)
class _CpqNicIfLogMapSwitchoverMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_U,1),(_d,2),('manual',3),('switchOnFail',4),('preferredPrimary',5),('auto',6),('preferenceOrder',7)))
_CpqNicIfLogMapSwitchoverMode_Type.__name__=_D
_CpqNicIfLogMapSwitchoverMode_Object=MibTableColumn
cpqNicIfLogMapSwitchoverMode=_CpqNicIfLogMapSwitchoverMode_Object((1,3,6,1,4,1,232,18,2,2,1,1,9),_CpqNicIfLogMapSwitchoverMode_Type())
cpqNicIfLogMapSwitchoverMode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapSwitchoverMode.setStatus(_B)
class _CpqNicIfLogMapCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_Y,2),(_b,3),(_Z,4)))
_CpqNicIfLogMapCondition_Type.__name__=_D
_CpqNicIfLogMapCondition_Object=MibTableColumn
cpqNicIfLogMapCondition=_CpqNicIfLogMapCondition_Object((1,3,6,1,4,1,232,18,2,2,1,1,10),_CpqNicIfLogMapCondition_Type())
cpqNicIfLogMapCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapCondition.setStatus(_B)
class _CpqNicIfLogMapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_U,1),(_Y,2),('primaryFailed',3),('standbyFailed',4),('groupFailed',5),('redundancyReduced',6),('redundancyLost',7)))
_CpqNicIfLogMapStatus_Type.__name__=_D
_CpqNicIfLogMapStatus_Object=MibTableColumn
cpqNicIfLogMapStatus=_CpqNicIfLogMapStatus_Object((1,3,6,1,4,1,232,18,2,2,1,1,11),_CpqNicIfLogMapStatus_Type())
cpqNicIfLogMapStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapStatus.setStatus(_B)
_CpqNicIfLogMapNumSwitchovers_Type=Counter32
_CpqNicIfLogMapNumSwitchovers_Object=MibTableColumn
cpqNicIfLogMapNumSwitchovers=_CpqNicIfLogMapNumSwitchovers_Object((1,3,6,1,4,1,232,18,2,2,1,1,12),_CpqNicIfLogMapNumSwitchovers_Type())
cpqNicIfLogMapNumSwitchovers.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapNumSwitchovers.setStatus(_B)
class _CpqNicIfLogMapHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfLogMapHwLocation_Type.__name__=_M
_CpqNicIfLogMapHwLocation_Object=MibTableColumn
cpqNicIfLogMapHwLocation=_CpqNicIfLogMapHwLocation_Object((1,3,6,1,4,1,232,18,2,2,1,1,13),_CpqNicIfLogMapHwLocation_Type())
cpqNicIfLogMapHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapHwLocation.setStatus(_E)
_CpqNicIfLogMapSpeed_Type=Gauge32
_CpqNicIfLogMapSpeed_Object=MibTableColumn
cpqNicIfLogMapSpeed=_CpqNicIfLogMapSpeed_Object((1,3,6,1,4,1,232,18,2,2,1,1,14),_CpqNicIfLogMapSpeed_Type())
cpqNicIfLogMapSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapSpeed.setStatus(_B)
class _CpqNicIfLogMapVlanCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CpqNicIfLogMapVlanCount_Type.__name__=_D
_CpqNicIfLogMapVlanCount_Object=MibTableColumn
cpqNicIfLogMapVlanCount=_CpqNicIfLogMapVlanCount_Object((1,3,6,1,4,1,232,18,2,2,1,1,15),_CpqNicIfLogMapVlanCount_Type())
cpqNicIfLogMapVlanCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapVlanCount.setStatus(_B)
class _CpqNicIfLogMapVlans_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqNicIfLogMapVlans_Type.__name__=_X
_CpqNicIfLogMapVlans_Object=MibTableColumn
cpqNicIfLogMapVlans=_CpqNicIfLogMapVlans_Object((1,3,6,1,4,1,232,18,2,2,1,1,16),_CpqNicIfLogMapVlans_Type())
cpqNicIfLogMapVlans.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapVlans.setStatus(_B)
_CpqNicIfLogMapLastChange_Type=TimeTicks
_CpqNicIfLogMapLastChange_Object=MibTableColumn
cpqNicIfLogMapLastChange=_CpqNicIfLogMapLastChange_Object((1,3,6,1,4,1,232,18,2,2,1,1,17),_CpqNicIfLogMapLastChange_Type())
cpqNicIfLogMapLastChange.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapLastChange.setStatus(_B)
_CpqNicIfLogMapAdvancedTeaming_Type=Integer32
_CpqNicIfLogMapAdvancedTeaming_Object=MibTableColumn
cpqNicIfLogMapAdvancedTeaming=_CpqNicIfLogMapAdvancedTeaming_Object((1,3,6,1,4,1,232,18,2,2,1,1,18),_CpqNicIfLogMapAdvancedTeaming_Type())
cpqNicIfLogMapAdvancedTeaming.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapAdvancedTeaming.setStatus(_B)
_CpqNicIfLogMapSpeedMbps_Type=Gauge32
_CpqNicIfLogMapSpeedMbps_Object=MibTableColumn
cpqNicIfLogMapSpeedMbps=_CpqNicIfLogMapSpeedMbps_Object((1,3,6,1,4,1,232,18,2,2,1,1,19),_CpqNicIfLogMapSpeedMbps_Type())
cpqNicIfLogMapSpeedMbps.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapSpeedMbps.setStatus(_E)
_CpqNicIfLogMapIPV6Address_Type=DisplayString
_CpqNicIfLogMapIPV6Address_Object=MibTableColumn
cpqNicIfLogMapIPV6Address=_CpqNicIfLogMapIPV6Address_Object((1,3,6,1,4,1,232,18,2,2,1,1,20),_CpqNicIfLogMapIPV6Address_Type())
cpqNicIfLogMapIPV6Address.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapIPV6Address.setStatus(_E)
_CpqNicIfLogMapLACNumber_Type=DisplayString
_CpqNicIfLogMapLACNumber_Object=MibTableColumn
cpqNicIfLogMapLACNumber=_CpqNicIfLogMapLACNumber_Object((1,3,6,1,4,1,232,18,2,2,1,1,21),_CpqNicIfLogMapLACNumber_Type())
cpqNicIfLogMapLACNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapLACNumber.setStatus(_E)
class _CpqNicIfLogMapDHCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CpqNicIfLogMapDHCP_Type.__name__=_D
_CpqNicIfLogMapDHCP_Object=MibTableColumn
cpqNicIfLogMapDHCP=_CpqNicIfLogMapDHCP_Object((1,3,6,1,4,1,232,18,2,2,1,1,22),_CpqNicIfLogMapDHCP_Type())
cpqNicIfLogMapDHCP.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapDHCP.setStatus(_B)
class _CpqNicIfLogMapPciLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfLogMapPciLocation_Type.__name__=_M
_CpqNicIfLogMapPciLocation_Object=MibTableColumn
cpqNicIfLogMapPciLocation=_CpqNicIfLogMapPciLocation_Object((1,3,6,1,4,1,232,18,2,2,1,1,23),_CpqNicIfLogMapPciLocation_Type())
cpqNicIfLogMapPciLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapPciLocation.setStatus(_E)
class _CpqNicIfLogMapOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_Y,2),(_b,3),(_Z,4)))
_CpqNicIfLogMapOverallCondition_Type.__name__=_D
_CpqNicIfLogMapOverallCondition_Object=MibScalar
cpqNicIfLogMapOverallCondition=_CpqNicIfLogMapOverallCondition_Object((1,3,6,1,4,1,232,18,2,2,2),_CpqNicIfLogMapOverallCondition_Type())
cpqNicIfLogMapOverallCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfLogMapOverallCondition.setStatus(_B)
_CpqNicIfPhysAdapter_ObjectIdentity=ObjectIdentity
cpqNicIfPhysAdapter=_CpqNicIfPhysAdapter_ObjectIdentity((1,3,6,1,4,1,232,18,2,3))
_CpqNicIfPhysAdapterTable_Object=MibTable
cpqNicIfPhysAdapterTable=_CpqNicIfPhysAdapterTable_Object((1,3,6,1,4,1,232,18,2,3,1))
if mibBuilder.loadTexts:cpqNicIfPhysAdapterTable.setStatus(_B)
_CpqNicIfPhysAdapterEntry_Object=MibTableRow
cpqNicIfPhysAdapterEntry=_CpqNicIfPhysAdapterEntry_Object((1,3,6,1,4,1,232,18,2,3,1,1))
cpqNicIfPhysAdapterEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cpqNicIfPhysAdapterEntry.setStatus(_B)
class _CpqNicIfPhysAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicIfPhysAdapterIndex_Type.__name__=_D
_CpqNicIfPhysAdapterIndex_Object=MibTableColumn
cpqNicIfPhysAdapterIndex=_CpqNicIfPhysAdapterIndex_Object((1,3,6,1,4,1,232,18,2,3,1,1,1),_CpqNicIfPhysAdapterIndex_Type())
cpqNicIfPhysAdapterIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterIndex.setStatus(_B)
_CpqNicIfPhysAdapterIfNumber_Type=OctetString
_CpqNicIfPhysAdapterIfNumber_Object=MibTableColumn
cpqNicIfPhysAdapterIfNumber=_CpqNicIfPhysAdapterIfNumber_Object((1,3,6,1,4,1,232,18,2,3,1,1,2),_CpqNicIfPhysAdapterIfNumber_Type())
cpqNicIfPhysAdapterIfNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterIfNumber.setStatus(_B)
class _CpqNicIfPhysAdapterRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*((_U,1),('primary',2),('secondary',3),('member',4),('txRx',5),('tx',6),(_i,7),(_d,8),(_j,9),('notApplicable',255)))
_CpqNicIfPhysAdapterRole_Type.__name__=_D
_CpqNicIfPhysAdapterRole_Object=MibTableColumn
cpqNicIfPhysAdapterRole=_CpqNicIfPhysAdapterRole_Object((1,3,6,1,4,1,232,18,2,3,1,1,3),_CpqNicIfPhysAdapterRole_Type())
cpqNicIfPhysAdapterRole.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterRole.setStatus(_B)
class _CpqNicIfPhysAdapterMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqNicIfPhysAdapterMACAddress_Type.__name__=_X
_CpqNicIfPhysAdapterMACAddress_Object=MibTableColumn
cpqNicIfPhysAdapterMACAddress=_CpqNicIfPhysAdapterMACAddress_Object((1,3,6,1,4,1,232,18,2,3,1,1,4),_CpqNicIfPhysAdapterMACAddress_Type())
cpqNicIfPhysAdapterMACAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterMACAddress.setStatus(_B)
_CpqNicIfPhysAdapterSlot_Type=Integer32
_CpqNicIfPhysAdapterSlot_Object=MibTableColumn
cpqNicIfPhysAdapterSlot=_CpqNicIfPhysAdapterSlot_Object((1,3,6,1,4,1,232,18,2,3,1,1,5),_CpqNicIfPhysAdapterSlot_Type())
cpqNicIfPhysAdapterSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterSlot.setStatus(_B)
_CpqNicIfPhysAdapterIoAddr_Type=Integer32
_CpqNicIfPhysAdapterIoAddr_Object=MibTableColumn
cpqNicIfPhysAdapterIoAddr=_CpqNicIfPhysAdapterIoAddr_Object((1,3,6,1,4,1,232,18,2,3,1,1,6),_CpqNicIfPhysAdapterIoAddr_Type())
cpqNicIfPhysAdapterIoAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterIoAddr.setStatus(_B)
class _CpqNicIfPhysAdapterIrq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqNicIfPhysAdapterIrq_Type.__name__=_D
_CpqNicIfPhysAdapterIrq_Object=MibTableColumn
cpqNicIfPhysAdapterIrq=_CpqNicIfPhysAdapterIrq_Object((1,3,6,1,4,1,232,18,2,3,1,1,7),_CpqNicIfPhysAdapterIrq_Type())
cpqNicIfPhysAdapterIrq.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterIrq.setStatus(_B)
_CpqNicIfPhysAdapterDma_Type=Integer32
_CpqNicIfPhysAdapterDma_Object=MibTableColumn
cpqNicIfPhysAdapterDma=_CpqNicIfPhysAdapterDma_Object((1,3,6,1,4,1,232,18,2,3,1,1,8),_CpqNicIfPhysAdapterDma_Type())
cpqNicIfPhysAdapterDma.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterDma.setStatus(_B)
_CpqNicIfPhysAdapterMemAddr_Type=Integer32
_CpqNicIfPhysAdapterMemAddr_Object=MibTableColumn
cpqNicIfPhysAdapterMemAddr=_CpqNicIfPhysAdapterMemAddr_Object((1,3,6,1,4,1,232,18,2,3,1,1,9),_CpqNicIfPhysAdapterMemAddr_Type())
cpqNicIfPhysAdapterMemAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterMemAddr.setStatus(_B)
_CpqNicIfPhysAdapterPort_Type=Integer32
_CpqNicIfPhysAdapterPort_Object=MibTableColumn
cpqNicIfPhysAdapterPort=_CpqNicIfPhysAdapterPort_Object((1,3,6,1,4,1,232,18,2,3,1,1,10),_CpqNicIfPhysAdapterPort_Type())
cpqNicIfPhysAdapterPort.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterPort.setStatus(_B)
class _CpqNicIfPhysAdapterDuplexState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('half',2),('full',3)))
_CpqNicIfPhysAdapterDuplexState_Type.__name__=_D
_CpqNicIfPhysAdapterDuplexState_Object=MibTableColumn
cpqNicIfPhysAdapterDuplexState=_CpqNicIfPhysAdapterDuplexState_Object((1,3,6,1,4,1,232,18,2,3,1,1,11),_CpqNicIfPhysAdapterDuplexState_Type())
cpqNicIfPhysAdapterDuplexState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterDuplexState.setStatus(_B)
class _CpqNicIfPhysAdapterCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_Y,2),(_b,3),(_Z,4)))
_CpqNicIfPhysAdapterCondition_Type.__name__=_D
_CpqNicIfPhysAdapterCondition_Object=MibTableColumn
cpqNicIfPhysAdapterCondition=_CpqNicIfPhysAdapterCondition_Object((1,3,6,1,4,1,232,18,2,3,1,1,12),_CpqNicIfPhysAdapterCondition_Type())
cpqNicIfPhysAdapterCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterCondition.setStatus(_B)
class _CpqNicIfPhysAdapterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_j,2),(_i,3),(_Z,4)))
_CpqNicIfPhysAdapterState_Type.__name__=_D
_CpqNicIfPhysAdapterState_Object=MibTableColumn
cpqNicIfPhysAdapterState=_CpqNicIfPhysAdapterState_Object((1,3,6,1,4,1,232,18,2,3,1,1,13),_CpqNicIfPhysAdapterState_Type())
cpqNicIfPhysAdapterState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterState.setStatus(_B)
class _CpqNicIfPhysAdapterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_Y,2),('generalFailure',3),('linkFailure',4)))
_CpqNicIfPhysAdapterStatus_Type.__name__=_D
_CpqNicIfPhysAdapterStatus_Object=MibTableColumn
cpqNicIfPhysAdapterStatus=_CpqNicIfPhysAdapterStatus_Object((1,3,6,1,4,1,232,18,2,3,1,1,14),_CpqNicIfPhysAdapterStatus_Type())
cpqNicIfPhysAdapterStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterStatus.setStatus(_B)
class _CpqNicIfPhysAdapterStatsValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CpqNicIfPhysAdapterStatsValid_Type.__name__=_D
_CpqNicIfPhysAdapterStatsValid_Object=MibTableColumn
cpqNicIfPhysAdapterStatsValid=_CpqNicIfPhysAdapterStatsValid_Object((1,3,6,1,4,1,232,18,2,3,1,1,15),_CpqNicIfPhysAdapterStatsValid_Type())
cpqNicIfPhysAdapterStatsValid.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterStatsValid.setStatus(_B)
_CpqNicIfPhysAdapterGoodTransmits_Type=Counter32
_CpqNicIfPhysAdapterGoodTransmits_Object=MibTableColumn
cpqNicIfPhysAdapterGoodTransmits=_CpqNicIfPhysAdapterGoodTransmits_Object((1,3,6,1,4,1,232,18,2,3,1,1,16),_CpqNicIfPhysAdapterGoodTransmits_Type())
cpqNicIfPhysAdapterGoodTransmits.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterGoodTransmits.setStatus(_B)
_CpqNicIfPhysAdapterGoodReceives_Type=Counter32
_CpqNicIfPhysAdapterGoodReceives_Object=MibTableColumn
cpqNicIfPhysAdapterGoodReceives=_CpqNicIfPhysAdapterGoodReceives_Object((1,3,6,1,4,1,232,18,2,3,1,1,17),_CpqNicIfPhysAdapterGoodReceives_Type())
cpqNicIfPhysAdapterGoodReceives.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterGoodReceives.setStatus(_B)
_CpqNicIfPhysAdapterBadTransmits_Type=Counter32
_CpqNicIfPhysAdapterBadTransmits_Object=MibTableColumn
cpqNicIfPhysAdapterBadTransmits=_CpqNicIfPhysAdapterBadTransmits_Object((1,3,6,1,4,1,232,18,2,3,1,1,18),_CpqNicIfPhysAdapterBadTransmits_Type())
cpqNicIfPhysAdapterBadTransmits.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterBadTransmits.setStatus(_B)
_CpqNicIfPhysAdapterBadReceives_Type=Counter32
_CpqNicIfPhysAdapterBadReceives_Object=MibTableColumn
cpqNicIfPhysAdapterBadReceives=_CpqNicIfPhysAdapterBadReceives_Object((1,3,6,1,4,1,232,18,2,3,1,1,19),_CpqNicIfPhysAdapterBadReceives_Type())
cpqNicIfPhysAdapterBadReceives.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterBadReceives.setStatus(_B)
_CpqNicIfPhysAdapterAlignmentErrors_Type=Counter32
_CpqNicIfPhysAdapterAlignmentErrors_Object=MibTableColumn
cpqNicIfPhysAdapterAlignmentErrors=_CpqNicIfPhysAdapterAlignmentErrors_Object((1,3,6,1,4,1,232,18,2,3,1,1,20),_CpqNicIfPhysAdapterAlignmentErrors_Type())
cpqNicIfPhysAdapterAlignmentErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterAlignmentErrors.setStatus(_B)
_CpqNicIfPhysAdapterFCSErrors_Type=Counter32
_CpqNicIfPhysAdapterFCSErrors_Object=MibTableColumn
cpqNicIfPhysAdapterFCSErrors=_CpqNicIfPhysAdapterFCSErrors_Object((1,3,6,1,4,1,232,18,2,3,1,1,21),_CpqNicIfPhysAdapterFCSErrors_Type())
cpqNicIfPhysAdapterFCSErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterFCSErrors.setStatus(_B)
_CpqNicIfPhysAdapterSingleCollisionFrames_Type=Counter32
_CpqNicIfPhysAdapterSingleCollisionFrames_Object=MibTableColumn
cpqNicIfPhysAdapterSingleCollisionFrames=_CpqNicIfPhysAdapterSingleCollisionFrames_Object((1,3,6,1,4,1,232,18,2,3,1,1,22),_CpqNicIfPhysAdapterSingleCollisionFrames_Type())
cpqNicIfPhysAdapterSingleCollisionFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterSingleCollisionFrames.setStatus(_B)
_CpqNicIfPhysAdapterMultipleCollisionFrames_Type=Counter32
_CpqNicIfPhysAdapterMultipleCollisionFrames_Object=MibTableColumn
cpqNicIfPhysAdapterMultipleCollisionFrames=_CpqNicIfPhysAdapterMultipleCollisionFrames_Object((1,3,6,1,4,1,232,18,2,3,1,1,23),_CpqNicIfPhysAdapterMultipleCollisionFrames_Type())
cpqNicIfPhysAdapterMultipleCollisionFrames.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterMultipleCollisionFrames.setStatus(_B)
_CpqNicIfPhysAdapterDeferredTransmissions_Type=Counter32
_CpqNicIfPhysAdapterDeferredTransmissions_Object=MibTableColumn
cpqNicIfPhysAdapterDeferredTransmissions=_CpqNicIfPhysAdapterDeferredTransmissions_Object((1,3,6,1,4,1,232,18,2,3,1,1,24),_CpqNicIfPhysAdapterDeferredTransmissions_Type())
cpqNicIfPhysAdapterDeferredTransmissions.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterDeferredTransmissions.setStatus(_B)
_CpqNicIfPhysAdapterLateCollisions_Type=Counter32
_CpqNicIfPhysAdapterLateCollisions_Object=MibTableColumn
cpqNicIfPhysAdapterLateCollisions=_CpqNicIfPhysAdapterLateCollisions_Object((1,3,6,1,4,1,232,18,2,3,1,1,25),_CpqNicIfPhysAdapterLateCollisions_Type())
cpqNicIfPhysAdapterLateCollisions.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterLateCollisions.setStatus(_B)
_CpqNicIfPhysAdapterExcessiveCollisions_Type=Counter32
_CpqNicIfPhysAdapterExcessiveCollisions_Object=MibTableColumn
cpqNicIfPhysAdapterExcessiveCollisions=_CpqNicIfPhysAdapterExcessiveCollisions_Object((1,3,6,1,4,1,232,18,2,3,1,1,26),_CpqNicIfPhysAdapterExcessiveCollisions_Type())
cpqNicIfPhysAdapterExcessiveCollisions.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterExcessiveCollisions.setStatus(_B)
_CpqNicIfPhysAdapterInternalMacTransmitErrors_Type=Counter32
_CpqNicIfPhysAdapterInternalMacTransmitErrors_Object=MibTableColumn
cpqNicIfPhysAdapterInternalMacTransmitErrors=_CpqNicIfPhysAdapterInternalMacTransmitErrors_Object((1,3,6,1,4,1,232,18,2,3,1,1,27),_CpqNicIfPhysAdapterInternalMacTransmitErrors_Type())
cpqNicIfPhysAdapterInternalMacTransmitErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterInternalMacTransmitErrors.setStatus(_B)
_CpqNicIfPhysAdapterCarrierSenseErrors_Type=Counter32
_CpqNicIfPhysAdapterCarrierSenseErrors_Object=MibTableColumn
cpqNicIfPhysAdapterCarrierSenseErrors=_CpqNicIfPhysAdapterCarrierSenseErrors_Object((1,3,6,1,4,1,232,18,2,3,1,1,28),_CpqNicIfPhysAdapterCarrierSenseErrors_Type())
cpqNicIfPhysAdapterCarrierSenseErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterCarrierSenseErrors.setStatus(_B)
_CpqNicIfPhysAdapterFrameTooLongs_Type=Counter32
_CpqNicIfPhysAdapterFrameTooLongs_Object=MibTableColumn
cpqNicIfPhysAdapterFrameTooLongs=_CpqNicIfPhysAdapterFrameTooLongs_Object((1,3,6,1,4,1,232,18,2,3,1,1,29),_CpqNicIfPhysAdapterFrameTooLongs_Type())
cpqNicIfPhysAdapterFrameTooLongs.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterFrameTooLongs.setStatus(_B)
_CpqNicIfPhysAdapterInternalMacReceiveErrors_Type=Counter32
_CpqNicIfPhysAdapterInternalMacReceiveErrors_Object=MibTableColumn
cpqNicIfPhysAdapterInternalMacReceiveErrors=_CpqNicIfPhysAdapterInternalMacReceiveErrors_Object((1,3,6,1,4,1,232,18,2,3,1,1,30),_CpqNicIfPhysAdapterInternalMacReceiveErrors_Type())
cpqNicIfPhysAdapterInternalMacReceiveErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterInternalMacReceiveErrors.setStatus(_B)
class _CpqNicIfPhysAdapterHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfPhysAdapterHwLocation_Type.__name__=_M
_CpqNicIfPhysAdapterHwLocation_Object=MibTableColumn
cpqNicIfPhysAdapterHwLocation=_CpqNicIfPhysAdapterHwLocation_Object((1,3,6,1,4,1,232,18,2,3,1,1,31),_CpqNicIfPhysAdapterHwLocation_Type())
cpqNicIfPhysAdapterHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterHwLocation.setStatus(_E)
class _CpqNicIfPhysAdapterPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfPhysAdapterPartNumber_Type.__name__=_M
_CpqNicIfPhysAdapterPartNumber_Object=MibTableColumn
cpqNicIfPhysAdapterPartNumber=_CpqNicIfPhysAdapterPartNumber_Object((1,3,6,1,4,1,232,18,2,3,1,1,32),_CpqNicIfPhysAdapterPartNumber_Type())
cpqNicIfPhysAdapterPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterPartNumber.setStatus(_B)
_CpqNicIfPhysAdapterSpeed_Type=Gauge32
_CpqNicIfPhysAdapterSpeed_Object=MibTableColumn
cpqNicIfPhysAdapterSpeed=_CpqNicIfPhysAdapterSpeed_Object((1,3,6,1,4,1,232,18,2,3,1,1,33),_CpqNicIfPhysAdapterSpeed_Type())
cpqNicIfPhysAdapterSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterSpeed.setStatus(_B)
class _CpqNicIfPhysAdapterConfSpeedDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_c,1),('autoAuto',2),('ethernetHalf',3),('ethernetFull',4),('fastEthernetHalf',5),('fastEthernetFull',6),('gigEthernetHalf',7),('gigEthernetFull',8),('gig10EthernetFull',9)))
_CpqNicIfPhysAdapterConfSpeedDuplex_Type.__name__=_D
_CpqNicIfPhysAdapterConfSpeedDuplex_Object=MibTableColumn
cpqNicIfPhysAdapterConfSpeedDuplex=_CpqNicIfPhysAdapterConfSpeedDuplex_Object((1,3,6,1,4,1,232,18,2,3,1,1,34),_CpqNicIfPhysAdapterConfSpeedDuplex_Type())
cpqNicIfPhysAdapterConfSpeedDuplex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterConfSpeedDuplex.setStatus(_B)
_CpqNicIfPhysAdapterAggregationGID_Type=Integer32
_CpqNicIfPhysAdapterAggregationGID_Object=MibTableColumn
cpqNicIfPhysAdapterAggregationGID=_CpqNicIfPhysAdapterAggregationGID_Object((1,3,6,1,4,1,232,18,2,3,1,1,35),_CpqNicIfPhysAdapterAggregationGID_Type())
cpqNicIfPhysAdapterAggregationGID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterAggregationGID.setStatus(_B)
_CpqNicIfPhysAdapterSpeedMbps_Type=Gauge32
_CpqNicIfPhysAdapterSpeedMbps_Object=MibTableColumn
cpqNicIfPhysAdapterSpeedMbps=_CpqNicIfPhysAdapterSpeedMbps_Object((1,3,6,1,4,1,232,18,2,3,1,1,36),_CpqNicIfPhysAdapterSpeedMbps_Type())
cpqNicIfPhysAdapterSpeedMbps.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterSpeedMbps.setStatus(_E)
_CpqNicIfPhysAdapterInOctets_Type=Counter32
_CpqNicIfPhysAdapterInOctets_Object=MibTableColumn
cpqNicIfPhysAdapterInOctets=_CpqNicIfPhysAdapterInOctets_Object((1,3,6,1,4,1,232,18,2,3,1,1,37),_CpqNicIfPhysAdapterInOctets_Type())
cpqNicIfPhysAdapterInOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterInOctets.setStatus(_E)
_CpqNicIfPhysAdapterOutOctets_Type=Counter32
_CpqNicIfPhysAdapterOutOctets_Object=MibTableColumn
cpqNicIfPhysAdapterOutOctets=_CpqNicIfPhysAdapterOutOctets_Object((1,3,6,1,4,1,232,18,2,3,1,1,38),_CpqNicIfPhysAdapterOutOctets_Type())
cpqNicIfPhysAdapterOutOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterOutOctets.setStatus(_E)
class _CpqNicIfPhysAdapterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfPhysAdapterName_Type.__name__=_M
_CpqNicIfPhysAdapterName_Object=MibTableColumn
cpqNicIfPhysAdapterName=_CpqNicIfPhysAdapterName_Object((1,3,6,1,4,1,232,18,2,3,1,1,39),_CpqNicIfPhysAdapterName_Type())
cpqNicIfPhysAdapterName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterName.setStatus(_E)
_CpqNicIfPhysAdapterIoBayNo_Type=Integer32
_CpqNicIfPhysAdapterIoBayNo_Object=MibTableColumn
cpqNicIfPhysAdapterIoBayNo=_CpqNicIfPhysAdapterIoBayNo_Object((1,3,6,1,4,1,232,18,2,3,1,1,40),_CpqNicIfPhysAdapterIoBayNo_Type())
cpqNicIfPhysAdapterIoBayNo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterIoBayNo.setStatus(_E)
class _CpqNicIfPhysAdapterFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfPhysAdapterFWVersion_Type.__name__=_M
_CpqNicIfPhysAdapterFWVersion_Object=MibTableColumn
cpqNicIfPhysAdapterFWVersion=_CpqNicIfPhysAdapterFWVersion_Object((1,3,6,1,4,1,232,18,2,3,1,1,41),_CpqNicIfPhysAdapterFWVersion_Type())
cpqNicIfPhysAdapterFWVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterFWVersion.setStatus(_E)
_CpqNicIfPhysAdapterVirtualPortNumber_Type=Integer32
_CpqNicIfPhysAdapterVirtualPortNumber_Object=MibTableColumn
cpqNicIfPhysAdapterVirtualPortNumber=_CpqNicIfPhysAdapterVirtualPortNumber_Object((1,3,6,1,4,1,232,18,2,3,1,1,42),_CpqNicIfPhysAdapterVirtualPortNumber_Type())
cpqNicIfPhysAdapterVirtualPortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterVirtualPortNumber.setStatus(_E)
class _CpqNicIfPhysAdapterPciLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqNicIfPhysAdapterPciLocation_Type.__name__=_M
_CpqNicIfPhysAdapterPciLocation_Object=MibTableColumn
cpqNicIfPhysAdapterPciLocation=_CpqNicIfPhysAdapterPciLocation_Object((1,3,6,1,4,1,232,18,2,3,1,1,43),_CpqNicIfPhysAdapterPciLocation_Type())
cpqNicIfPhysAdapterPciLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfPhysAdapterPciLocation.setStatus(_E)
_CpqNicPhyAdapBaseMemTable_Object=MibTable
cpqNicPhyAdapBaseMemTable=_CpqNicPhyAdapBaseMemTable_Object((1,3,6,1,4,1,232,18,2,3,2))
if mibBuilder.loadTexts:cpqNicPhyAdapBaseMemTable.setStatus(_E)
_CpqNicPhyAdapBaseMemEntry_Object=MibTableRow
cpqNicPhyAdapBaseMemEntry=_CpqNicPhyAdapBaseMemEntry_Object((1,3,6,1,4,1,232,18,2,3,2,1))
cpqNicPhyAdapBaseMemEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cpqNicPhyAdapBaseMemEntry.setStatus(_E)
class _CpqNicPhyAdapBaseMemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicPhyAdapBaseMemIndex_Type.__name__=_D
_CpqNicPhyAdapBaseMemIndex_Object=MibTableColumn
cpqNicPhyAdapBaseMemIndex=_CpqNicPhyAdapBaseMemIndex_Object((1,3,6,1,4,1,232,18,2,3,2,1,1),_CpqNicPhyAdapBaseMemIndex_Type())
cpqNicPhyAdapBaseMemIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicPhyAdapBaseMemIndex.setStatus(_E)
_CpqNicPhyAdapBaseMemIfIndex_Type=Integer32
_CpqNicPhyAdapBaseMemIfIndex_Object=MibTableColumn
cpqNicPhyAdapBaseMemIfIndex=_CpqNicPhyAdapBaseMemIfIndex_Object((1,3,6,1,4,1,232,18,2,3,2,1,2),_CpqNicPhyAdapBaseMemIfIndex_Type())
cpqNicPhyAdapBaseMemIfIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicPhyAdapBaseMemIfIndex.setStatus(_E)
_CpqNicPhyAdapBaseMemAddr_Type=Integer32
_CpqNicPhyAdapBaseMemAddr_Object=MibTableColumn
cpqNicPhyAdapBaseMemAddr=_CpqNicPhyAdapBaseMemAddr_Object((1,3,6,1,4,1,232,18,2,3,2,1,3),_CpqNicPhyAdapBaseMemAddr_Type())
cpqNicPhyAdapBaseMemAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicPhyAdapBaseMemAddr.setStatus(_E)
class _CpqNicFlexLomPhySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqNicFlexLomPhySlot_Type.__name__=_D
_CpqNicFlexLomPhySlot_Object=MibScalar
cpqNicFlexLomPhySlot=_CpqNicFlexLomPhySlot_Object((1,3,6,1,4,1,232,18,2,3,3),_CpqNicFlexLomPhySlot_Type())
cpqNicFlexLomPhySlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicFlexLomPhySlot.setStatus(_B)
_CpqNicIfVlanMap_ObjectIdentity=ObjectIdentity
cpqNicIfVlanMap=_CpqNicIfVlanMap_ObjectIdentity((1,3,6,1,4,1,232,18,2,4))
_CpqNicIfVlanMapTable_Object=MibTable
cpqNicIfVlanMapTable=_CpqNicIfVlanMapTable_Object((1,3,6,1,4,1,232,18,2,4,1))
if mibBuilder.loadTexts:cpqNicIfVlanMapTable.setStatus(_B)
_CpqNicIfVlanMapEntry_Object=MibTableRow
cpqNicIfVlanMapEntry=_CpqNicIfVlanMapEntry_Object((1,3,6,1,4,1,232,18,2,4,1,1))
cpqNicIfVlanMapEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cpqNicIfVlanMapEntry.setStatus(_B)
class _CpqNicIfVlanMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicIfVlanMapIndex_Type.__name__=_D
_CpqNicIfVlanMapIndex_Object=MibTableColumn
cpqNicIfVlanMapIndex=_CpqNicIfVlanMapIndex_Object((1,3,6,1,4,1,232,18,2,4,1,1,1),_CpqNicIfVlanMapIndex_Type())
cpqNicIfVlanMapIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapIndex.setStatus(_B)
class _CpqNicIfVlanMapLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqNicIfVlanMapLogIndex_Type.__name__=_D
_CpqNicIfVlanMapLogIndex_Object=MibTableColumn
cpqNicIfVlanMapLogIndex=_CpqNicIfVlanMapLogIndex_Object((1,3,6,1,4,1,232,18,2,4,1,1,2),_CpqNicIfVlanMapLogIndex_Type())
cpqNicIfVlanMapLogIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapLogIndex.setStatus(_B)
_CpqNicIfVlanMapIfIndex_Type=Integer32
_CpqNicIfVlanMapIfIndex_Object=MibTableColumn
cpqNicIfVlanMapIfIndex=_CpqNicIfVlanMapIfIndex_Object((1,3,6,1,4,1,232,18,2,4,1,1,3),_CpqNicIfVlanMapIfIndex_Type())
cpqNicIfVlanMapIfIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapIfIndex.setStatus(_B)
class _CpqNicIfVlanMapVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CpqNicIfVlanMapVlanId_Type.__name__=_D
_CpqNicIfVlanMapVlanId_Object=MibTableColumn
cpqNicIfVlanMapVlanId=_CpqNicIfVlanMapVlanId_Object((1,3,6,1,4,1,232,18,2,4,1,1,4),_CpqNicIfVlanMapVlanId_Type())
cpqNicIfVlanMapVlanId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapVlanId.setStatus(_B)
class _CpqNicIfVlanMapVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CpqNicIfVlanMapVlanName_Type.__name__=_M
_CpqNicIfVlanMapVlanName_Object=MibTableColumn
cpqNicIfVlanMapVlanName=_CpqNicIfVlanMapVlanName_Object((1,3,6,1,4,1,232,18,2,4,1,1,5),_CpqNicIfVlanMapVlanName_Type())
cpqNicIfVlanMapVlanName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapVlanName.setStatus(_B)
_CpqNicIfVlanMapVlanIPV6Address_Type=DisplayString
_CpqNicIfVlanMapVlanIPV6Address_Object=MibTableColumn
cpqNicIfVlanMapVlanIPV6Address=_CpqNicIfVlanMapVlanIPV6Address_Object((1,3,6,1,4,1,232,18,2,4,1,1,6),_CpqNicIfVlanMapVlanIPV6Address_Type())
cpqNicIfVlanMapVlanIPV6Address.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapVlanIPV6Address.setStatus(_E)
_CpqNicIfVlanMapVlanLACNumber_Type=DisplayString
_CpqNicIfVlanMapVlanLACNumber_Object=MibTableColumn
cpqNicIfVlanMapVlanLACNumber=_CpqNicIfVlanMapVlanLACNumber_Object((1,3,6,1,4,1,232,18,2,4,1,1,7),_CpqNicIfVlanMapVlanLACNumber_Type())
cpqNicIfVlanMapVlanLACNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicIfVlanMapVlanLACNumber.setStatus(_E)
_CpqNicVirusThrottle_ObjectIdentity=ObjectIdentity
cpqNicVirusThrottle=_CpqNicVirusThrottle_ObjectIdentity((1,3,6,1,4,1,232,18,2,5))
class _CpqNicVtInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notInstalled',1),('installed',2)))
_CpqNicVtInstalled_Type.__name__=_D
_CpqNicVtInstalled_Object=MibScalar
cpqNicVtInstalled=_CpqNicVtInstalled_Object((1,3,6,1,4,1,232,18,2,5,1),_CpqNicVtInstalled_Type())
cpqNicVtInstalled.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicVtInstalled.setStatus(_B)
class _CpqNicVtLicensed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notLicensed',1),('licensed',2)))
_CpqNicVtLicensed_Type.__name__=_D
_CpqNicVtLicensed_Object=MibScalar
cpqNicVtLicensed=_CpqNicVtLicensed_Object((1,3,6,1,4,1,232,18,2,5,2),_CpqNicVtLicensed_Type())
cpqNicVtLicensed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicVtLicensed.setStatus(_B)
class _CpqNicVtVirusActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notDetected',1),('detected',2)))
_CpqNicVtVirusActivity_Type.__name__=_D
_CpqNicVtVirusActivity_Object=MibScalar
cpqNicVtVirusActivity=_CpqNicVtVirusActivity_Object((1,3,6,1,4,1,232,18,2,5,3),_CpqNicVtVirusActivity_Type())
cpqNicVtVirusActivity.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqNicVtVirusActivity.setStatus(_B)
cpqNicConnectivityRestored=NotificationType((1,3,6,1,4,1,232,0,18001))
cpqNicConnectivityRestored.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N)))
if mibBuilder.loadTexts:cpqNicConnectivityRestored.setStatus('')
cpqNicConnectivityLost=NotificationType((1,3,6,1,4,1,232,0,18002))
cpqNicConnectivityLost.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N)))
if mibBuilder.loadTexts:cpqNicConnectivityLost.setStatus('')
cpqNicRedundancyIncreased=NotificationType((1,3,6,1,4,1,232,0,18003))
cpqNicRedundancyIncreased.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_C,_W)))
if mibBuilder.loadTexts:cpqNicRedundancyIncreased.setStatus('')
cpqNicRedundancyReduced=NotificationType((1,3,6,1,4,1,232,0,18004))
cpqNicRedundancyReduced.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_C,_W)))
if mibBuilder.loadTexts:cpqNicRedundancyReduced.setStatus('')
cpqNic2ConnectivityRestored=NotificationType((1,3,6,1,4,1,232,0,18005))
cpqNic2ConnectivityRestored.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S)))
if mibBuilder.loadTexts:cpqNic2ConnectivityRestored.setStatus('')
cpqNic2ConnectivityLost=NotificationType((1,3,6,1,4,1,232,0,18006))
cpqNic2ConnectivityLost.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S)))
if mibBuilder.loadTexts:cpqNic2ConnectivityLost.setStatus('')
cpqNic2RedundancyIncreased=NotificationType((1,3,6,1,4,1,232,0,18007))
cpqNic2RedundancyIncreased.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_W)))
if mibBuilder.loadTexts:cpqNic2RedundancyIncreased.setStatus('')
cpqNic2RedundancyReduced=NotificationType((1,3,6,1,4,1,232,0,18008))
cpqNic2RedundancyReduced.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_W)))
if mibBuilder.loadTexts:cpqNic2RedundancyReduced.setStatus('')
cpqNicVirusLikeActivityDetected=NotificationType((1,3,6,1,4,1,232,0,18009))
cpqNicVirusLikeActivityDetected.setObjects(*((_H,_I),(_F,_G),(_K,_L)))
if mibBuilder.loadTexts:cpqNicVirusLikeActivityDetected.setStatus('')
cpqNicVirusLikeActivityStopped=NotificationType((1,3,6,1,4,1,232,0,18010))
cpqNicVirusLikeActivityStopped.setObjects(*((_H,_I),(_F,_G),(_K,_L)))
if mibBuilder.loadTexts:cpqNicVirusLikeActivityStopped.setStatus('')
cpqNic3ConnectivityRestored=NotificationType((1,3,6,1,4,1,232,0,18011))
cpqNic3ConnectivityRestored.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_a)))
if mibBuilder.loadTexts:cpqNic3ConnectivityRestored.setStatus('')
cpqNic3ConnectivityLost=NotificationType((1,3,6,1,4,1,232,0,18012))
cpqNic3ConnectivityLost.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_a)))
if mibBuilder.loadTexts:cpqNic3ConnectivityLost.setStatus('')
cpqNic3RedundancyIncreased=NotificationType((1,3,6,1,4,1,232,0,18013))
cpqNic3RedundancyIncreased.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_a),(_C,_W)))
if mibBuilder.loadTexts:cpqNic3RedundancyIncreased.setStatus('')
cpqNic3RedundancyReduced=NotificationType((1,3,6,1,4,1,232,0,18014))
cpqNic3RedundancyReduced.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_C,_N),(_K,_L),(_C,_T),(_O,_P),(_C,_Q),(_R,_S),(_C,_a),(_C,_W)))
if mibBuilder.loadTexts:cpqNic3RedundancyReduced.setStatus('')
cpqNicAllLinksDown=NotificationType((1,3,6,1,4,1,232,0,18015))
cpqNicAllLinksDown.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_K,_L),(_O,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqNicAllLinksDown.setStatus('')
cpqNicAllLinksDownRepaired=NotificationType((1,3,6,1,4,1,232,0,18016))
cpqNicAllLinksDownRepaired.setObjects(*((_H,_I),(_F,_G),(_C,_J),(_K,_L),(_O,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqNicAllLinksDownRepaired.setStatus('')
cpqNicFlexLomTrainingFailed=NotificationType((1,3,6,1,4,1,232,0,18017))
cpqNicFlexLomTrainingFailed.setObjects(*((_H,_I),(_F,_G),(_C,_m)))
if mibBuilder.loadTexts:cpqNicFlexLomTrainingFailed.setStatus('')
mibBuilder.exportSymbols(_C,**{'cpqNicConnectivityRestored':cpqNicConnectivityRestored,'cpqNicConnectivityLost':cpqNicConnectivityLost,'cpqNicRedundancyIncreased':cpqNicRedundancyIncreased,'cpqNicRedundancyReduced':cpqNicRedundancyReduced,'cpqNic2ConnectivityRestored':cpqNic2ConnectivityRestored,'cpqNic2ConnectivityLost':cpqNic2ConnectivityLost,'cpqNic2RedundancyIncreased':cpqNic2RedundancyIncreased,'cpqNic2RedundancyReduced':cpqNic2RedundancyReduced,'cpqNicVirusLikeActivityDetected':cpqNicVirusLikeActivityDetected,'cpqNicVirusLikeActivityStopped':cpqNicVirusLikeActivityStopped,'cpqNic3ConnectivityRestored':cpqNic3ConnectivityRestored,'cpqNic3ConnectivityLost':cpqNic3ConnectivityLost,'cpqNic3RedundancyIncreased':cpqNic3RedundancyIncreased,'cpqNic3RedundancyReduced':cpqNic3RedundancyReduced,'cpqNicAllLinksDown':cpqNicAllLinksDown,'cpqNicAllLinksDownRepaired':cpqNicAllLinksDownRepaired,'cpqNicFlexLomTrainingFailed':cpqNicFlexLomTrainingFailed,'cpqNic':cpqNic,'cpqNicMibRev':cpqNicMibRev,'cpqNicMibRevMajor':cpqNicMibRevMajor,'cpqNicMibRevMinor':cpqNicMibRevMinor,'cpqNicMibCondition':cpqNicMibCondition,'cpqNicComponent':cpqNicComponent,'cpqNicInterface':cpqNicInterface,'cpqNicOsCommon':cpqNicOsCommon,'cpqNicOsCommonPollFreq':cpqNicOsCommonPollFreq,'cpqNicOsCommonModuleTable':cpqNicOsCommonModuleTable,'cpqNicOsCommonModuleEntry':cpqNicOsCommonModuleEntry,_f:cpqNicOsCommonModuleIndex,'cpqNicOsCommonModuleName':cpqNicOsCommonModuleName,'cpqNicOsCommonModuleVersion':cpqNicOsCommonModuleVersion,'cpqNicOsCommonModuleDate':cpqNicOsCommonModuleDate,'cpqNicOsCommonModulePurpose':cpqNicOsCommonModulePurpose,'cpqNicIfLogMap':cpqNicIfLogMap,'cpqNicIfLogMapTable':cpqNicIfLogMapTable,'cpqNicIfLogMapEntry':cpqNicIfLogMapEntry,_g:cpqNicIfLogMapIndex,'cpqNicIfLogMapIfNumber':cpqNicIfLogMapIfNumber,'cpqNicIfLogMapDescription':cpqNicIfLogMapDescription,'cpqNicIfLogMapGroupType':cpqNicIfLogMapGroupType,'cpqNicIfLogMapAdapterCount':cpqNicIfLogMapAdapterCount,_W:cpqNicIfLogMapAdapterOKCount,'cpqNicIfLogMapPhysicalAdapters':cpqNicIfLogMapPhysicalAdapters,'cpqNicIfLogMapMACAddress':cpqNicIfLogMapMACAddress,'cpqNicIfLogMapSwitchoverMode':cpqNicIfLogMapSwitchoverMode,'cpqNicIfLogMapCondition':cpqNicIfLogMapCondition,'cpqNicIfLogMapStatus':cpqNicIfLogMapStatus,'cpqNicIfLogMapNumSwitchovers':cpqNicIfLogMapNumSwitchovers,'cpqNicIfLogMapHwLocation':cpqNicIfLogMapHwLocation,'cpqNicIfLogMapSpeed':cpqNicIfLogMapSpeed,'cpqNicIfLogMapVlanCount':cpqNicIfLogMapVlanCount,'cpqNicIfLogMapVlans':cpqNicIfLogMapVlans,'cpqNicIfLogMapLastChange':cpqNicIfLogMapLastChange,'cpqNicIfLogMapAdvancedTeaming':cpqNicIfLogMapAdvancedTeaming,'cpqNicIfLogMapSpeedMbps':cpqNicIfLogMapSpeedMbps,_a:cpqNicIfLogMapIPV6Address,'cpqNicIfLogMapLACNumber':cpqNicIfLogMapLACNumber,'cpqNicIfLogMapDHCP':cpqNicIfLogMapDHCP,'cpqNicIfLogMapPciLocation':cpqNicIfLogMapPciLocation,'cpqNicIfLogMapOverallCondition':cpqNicIfLogMapOverallCondition,'cpqNicIfPhysAdapter':cpqNicIfPhysAdapter,'cpqNicIfPhysAdapterTable':cpqNicIfPhysAdapterTable,'cpqNicIfPhysAdapterEntry':cpqNicIfPhysAdapterEntry,_h:cpqNicIfPhysAdapterIndex,'cpqNicIfPhysAdapterIfNumber':cpqNicIfPhysAdapterIfNumber,'cpqNicIfPhysAdapterRole':cpqNicIfPhysAdapterRole,'cpqNicIfPhysAdapterMACAddress':cpqNicIfPhysAdapterMACAddress,_J:cpqNicIfPhysAdapterSlot,'cpqNicIfPhysAdapterIoAddr':cpqNicIfPhysAdapterIoAddr,'cpqNicIfPhysAdapterIrq':cpqNicIfPhysAdapterIrq,'cpqNicIfPhysAdapterDma':cpqNicIfPhysAdapterDma,'cpqNicIfPhysAdapterMemAddr':cpqNicIfPhysAdapterMemAddr,_N:cpqNicIfPhysAdapterPort,'cpqNicIfPhysAdapterDuplexState':cpqNicIfPhysAdapterDuplexState,'cpqNicIfPhysAdapterCondition':cpqNicIfPhysAdapterCondition,'cpqNicIfPhysAdapterState':cpqNicIfPhysAdapterState,_T:cpqNicIfPhysAdapterStatus,'cpqNicIfPhysAdapterStatsValid':cpqNicIfPhysAdapterStatsValid,'cpqNicIfPhysAdapterGoodTransmits':cpqNicIfPhysAdapterGoodTransmits,'cpqNicIfPhysAdapterGoodReceives':cpqNicIfPhysAdapterGoodReceives,'cpqNicIfPhysAdapterBadTransmits':cpqNicIfPhysAdapterBadTransmits,'cpqNicIfPhysAdapterBadReceives':cpqNicIfPhysAdapterBadReceives,'cpqNicIfPhysAdapterAlignmentErrors':cpqNicIfPhysAdapterAlignmentErrors,'cpqNicIfPhysAdapterFCSErrors':cpqNicIfPhysAdapterFCSErrors,'cpqNicIfPhysAdapterSingleCollisionFrames':cpqNicIfPhysAdapterSingleCollisionFrames,'cpqNicIfPhysAdapterMultipleCollisionFrames':cpqNicIfPhysAdapterMultipleCollisionFrames,'cpqNicIfPhysAdapterDeferredTransmissions':cpqNicIfPhysAdapterDeferredTransmissions,'cpqNicIfPhysAdapterLateCollisions':cpqNicIfPhysAdapterLateCollisions,'cpqNicIfPhysAdapterExcessiveCollisions':cpqNicIfPhysAdapterExcessiveCollisions,'cpqNicIfPhysAdapterInternalMacTransmitErrors':cpqNicIfPhysAdapterInternalMacTransmitErrors,'cpqNicIfPhysAdapterCarrierSenseErrors':cpqNicIfPhysAdapterCarrierSenseErrors,'cpqNicIfPhysAdapterFrameTooLongs':cpqNicIfPhysAdapterFrameTooLongs,'cpqNicIfPhysAdapterInternalMacReceiveErrors':cpqNicIfPhysAdapterInternalMacReceiveErrors,'cpqNicIfPhysAdapterHwLocation':cpqNicIfPhysAdapterHwLocation,_Q:cpqNicIfPhysAdapterPartNumber,'cpqNicIfPhysAdapterSpeed':cpqNicIfPhysAdapterSpeed,'cpqNicIfPhysAdapterConfSpeedDuplex':cpqNicIfPhysAdapterConfSpeedDuplex,'cpqNicIfPhysAdapterAggregationGID':cpqNicIfPhysAdapterAggregationGID,'cpqNicIfPhysAdapterSpeedMbps':cpqNicIfPhysAdapterSpeedMbps,'cpqNicIfPhysAdapterInOctets':cpqNicIfPhysAdapterInOctets,'cpqNicIfPhysAdapterOutOctets':cpqNicIfPhysAdapterOutOctets,'cpqNicIfPhysAdapterName':cpqNicIfPhysAdapterName,'cpqNicIfPhysAdapterIoBayNo':cpqNicIfPhysAdapterIoBayNo,'cpqNicIfPhysAdapterFWVersion':cpqNicIfPhysAdapterFWVersion,'cpqNicIfPhysAdapterVirtualPortNumber':cpqNicIfPhysAdapterVirtualPortNumber,'cpqNicIfPhysAdapterPciLocation':cpqNicIfPhysAdapterPciLocation,'cpqNicPhyAdapBaseMemTable':cpqNicPhyAdapBaseMemTable,'cpqNicPhyAdapBaseMemEntry':cpqNicPhyAdapBaseMemEntry,_k:cpqNicPhyAdapBaseMemIndex,'cpqNicPhyAdapBaseMemIfIndex':cpqNicPhyAdapBaseMemIfIndex,'cpqNicPhyAdapBaseMemAddr':cpqNicPhyAdapBaseMemAddr,_m:cpqNicFlexLomPhySlot,'cpqNicIfVlanMap':cpqNicIfVlanMap,'cpqNicIfVlanMapTable':cpqNicIfVlanMapTable,'cpqNicIfVlanMapEntry':cpqNicIfVlanMapEntry,_l:cpqNicIfVlanMapIndex,'cpqNicIfVlanMapLogIndex':cpqNicIfVlanMapLogIndex,'cpqNicIfVlanMapIfIndex':cpqNicIfVlanMapIfIndex,'cpqNicIfVlanMapVlanId':cpqNicIfVlanMapVlanId,'cpqNicIfVlanMapVlanName':cpqNicIfVlanMapVlanName,'cpqNicIfVlanMapVlanIPV6Address':cpqNicIfVlanMapVlanIPV6Address,'cpqNicIfVlanMapVlanLACNumber':cpqNicIfVlanMapVlanLACNumber,'cpqNicVirusThrottle':cpqNicVirusThrottle,'cpqNicVtInstalled':cpqNicVtInstalled,'cpqNicVtLicensed':cpqNicVtLicensed,'cpqNicVtVirusActivity':cpqNicVtVirusActivity})