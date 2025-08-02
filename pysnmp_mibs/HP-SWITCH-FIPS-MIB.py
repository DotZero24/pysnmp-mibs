_j='hpSwitchFipsStatisticsGroup'
_i='hpSwitchFipsSessionGroup'
_h='hpSwitchFipsConfigGroup'
_g='hpSwitchFipsStatsSessFcoePermitPkts'
_f='hpSwitchFipsStatsSessFcfMacAddress'
_e='hpSwitchFipsFcoeDropPkts'
_d='hpSwitchFipsFipDropPkts'
_c='hpSwitchFipsSessFcfNameId'
_b='hpSwitchFipsSessVlanId'
_a='hpSwitchFipsSessFcMap'
_Z='hpSwitchFipsSessFcfMacAddress'
_Y='hpSwitchFipsSessEnodeNportIdType'
_X='hpSwitchFipsSessEnodeNportId'
_W='hpSwitchFipsSessEnodeMacAddress'
_V='hpSwitchFipsFcfMacTableRowStatus'
_U='hpSwitchFipsFabricName'
_T='hpSwitchFipsFcfNameId'
_S='hpSwitchFipsFcfEnodeLoginCount'
_R='hpSwitchFipsFcfFcMap'
_Q='hpSwitchFipsFcoeVlanId'
_P='hpSwitchFipsFcMap'
_O='hpSwitchFipsAdminStatus'
_N='hpSwitchFipsStatsSessFPMAMacAddress'
_M='hpSwitchFipsStatsSessEnodeIfIndex'
_L='hpSwitchFipsSessEnodeFPMAMacAddress'
_K='hpSwitchFipsSessEnodeInterfaceIndex'
_J='hpSwitchFipsFcfMacAddress'
_I='hpSwitchFipsVirtualFabricInterfaceIndex'
_H='hpSwitchFipsFcMapIndex'
_G='read-write'
_F='Integer32'
_E='not-accessible'
_D='OctetString'
_C='read-only'
_B='HP-SWITCH-FIPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpSwitchFipSnoopingMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78))
if mibBuilder.loadTexts:hpSwitchFipSnoopingMib.setRevisions(('2010-06-03 15:39',))
_HpSwitchFipsConfigObjects_ObjectIdentity=ObjectIdentity
hpSwitchFipsConfigObjects=_HpSwitchFipsConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,1))
_HpSwitchFipsScalars_ObjectIdentity=ObjectIdentity
hpSwitchFipsScalars=_HpSwitchFipsScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,1,1))
class _HpSwitchFipsAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpSwitchFipsAdminStatus_Type.__name__=_F
_HpSwitchFipsAdminStatus_Object=MibScalar
hpSwitchFipsAdminStatus=_HpSwitchFipsAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,1,1),_HpSwitchFipsAdminStatus_Type())
hpSwitchFipsAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchFipsAdminStatus.setStatus(_A)
_HpSwitchFipsTables_ObjectIdentity=ObjectIdentity
hpSwitchFipsTables=_HpSwitchFipsTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2))
_HpSwitchFipsFcMapTable_Object=MibTable
hpSwitchFipsFcMapTable=_HpSwitchFipsFcMapTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,1))
if mibBuilder.loadTexts:hpSwitchFipsFcMapTable.setStatus(_A)
_HpSwitchFipsFcMapEntry_Object=MibTableRow
hpSwitchFipsFcMapEntry=_HpSwitchFipsFcMapEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,1,1))
hpSwitchFipsFcMapEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpSwitchFipsFcMapEntry.setStatus(_A)
class _HpSwitchFipsFcMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpSwitchFipsFcMapIndex_Type.__name__=_F
_HpSwitchFipsFcMapIndex_Object=MibTableColumn
hpSwitchFipsFcMapIndex=_HpSwitchFipsFcMapIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,1,1,1),_HpSwitchFipsFcMapIndex_Type())
hpSwitchFipsFcMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsFcMapIndex.setStatus(_A)
class _HpSwitchFipsFcMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpSwitchFipsFcMap_Type.__name__=_D
_HpSwitchFipsFcMap_Object=MibTableColumn
hpSwitchFipsFcMap=_HpSwitchFipsFcMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,1,1,2),_HpSwitchFipsFcMap_Type())
hpSwitchFipsFcMap.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchFipsFcMap.setStatus(_A)
_HpSwitchFipsFcfMacAddressTable_Object=MibTable
hpSwitchFipsFcfMacAddressTable=_HpSwitchFipsFcfMacAddressTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2))
if mibBuilder.loadTexts:hpSwitchFipsFcfMacAddressTable.setStatus(_A)
_HpSwitchFipsFcfMacAddressEntry_Object=MibTableRow
hpSwitchFipsFcfMacAddressEntry=_HpSwitchFipsFcfMacAddressEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1))
hpSwitchFipsFcfMacAddressEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hpSwitchFipsFcfMacAddressEntry.setStatus(_A)
_HpSwitchFipsVirtualFabricInterfaceIndex_Type=InterfaceIndex
_HpSwitchFipsVirtualFabricInterfaceIndex_Object=MibTableColumn
hpSwitchFipsVirtualFabricInterfaceIndex=_HpSwitchFipsVirtualFabricInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,1),_HpSwitchFipsVirtualFabricInterfaceIndex_Type())
hpSwitchFipsVirtualFabricInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsVirtualFabricInterfaceIndex.setStatus(_A)
_HpSwitchFipsFcfMacAddress_Type=MacAddress
_HpSwitchFipsFcfMacAddress_Object=MibTableColumn
hpSwitchFipsFcfMacAddress=_HpSwitchFipsFcfMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,2),_HpSwitchFipsFcfMacAddress_Type())
hpSwitchFipsFcfMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsFcfMacAddress.setStatus(_A)
_HpSwitchFipsFcoeVlanId_Type=Integer32
_HpSwitchFipsFcoeVlanId_Object=MibTableColumn
hpSwitchFipsFcoeVlanId=_HpSwitchFipsFcoeVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,3),_HpSwitchFipsFcoeVlanId_Type())
hpSwitchFipsFcoeVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFcoeVlanId.setStatus(_A)
class _HpSwitchFipsFcfFcMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpSwitchFipsFcfFcMap_Type.__name__=_D
_HpSwitchFipsFcfFcMap_Object=MibTableColumn
hpSwitchFipsFcfFcMap=_HpSwitchFipsFcfFcMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,4),_HpSwitchFipsFcfFcMap_Type())
hpSwitchFipsFcfFcMap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFcfFcMap.setStatus(_A)
_HpSwitchFipsFcfEnodeLoginCount_Type=Integer32
_HpSwitchFipsFcfEnodeLoginCount_Object=MibTableColumn
hpSwitchFipsFcfEnodeLoginCount=_HpSwitchFipsFcfEnodeLoginCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,5),_HpSwitchFipsFcfEnodeLoginCount_Type())
hpSwitchFipsFcfEnodeLoginCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFcfEnodeLoginCount.setStatus(_A)
class _HpSwitchFipsFcfNameId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpSwitchFipsFcfNameId_Type.__name__=_D
_HpSwitchFipsFcfNameId_Object=MibTableColumn
hpSwitchFipsFcfNameId=_HpSwitchFipsFcfNameId_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,6),_HpSwitchFipsFcfNameId_Type())
hpSwitchFipsFcfNameId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFcfNameId.setStatus(_A)
class _HpSwitchFipsFabricName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpSwitchFipsFabricName_Type.__name__=_D
_HpSwitchFipsFabricName_Object=MibTableColumn
hpSwitchFipsFabricName=_HpSwitchFipsFabricName_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,7),_HpSwitchFipsFabricName_Type())
hpSwitchFipsFabricName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFabricName.setStatus(_A)
_HpSwitchFipsFcfMacTableRowStatus_Type=RowStatus
_HpSwitchFipsFcfMacTableRowStatus_Object=MibTableColumn
hpSwitchFipsFcfMacTableRowStatus=_HpSwitchFipsFcfMacTableRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,2,1,8),_HpSwitchFipsFcfMacTableRowStatus_Type())
hpSwitchFipsFcfMacTableRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpSwitchFipsFcfMacTableRowStatus.setStatus(_A)
_HpSwitchFipsSessionTable_Object=MibTable
hpSwitchFipsSessionTable=_HpSwitchFipsSessionTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3))
if mibBuilder.loadTexts:hpSwitchFipsSessionTable.setStatus(_A)
_HpSwitchFipsSessionEntry_Object=MibTableRow
hpSwitchFipsSessionEntry=_HpSwitchFipsSessionEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1))
hpSwitchFipsSessionEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpSwitchFipsSessionEntry.setStatus(_A)
_HpSwitchFipsSessEnodeInterfaceIndex_Type=InterfaceIndex
_HpSwitchFipsSessEnodeInterfaceIndex_Object=MibTableColumn
hpSwitchFipsSessEnodeInterfaceIndex=_HpSwitchFipsSessEnodeInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,1),_HpSwitchFipsSessEnodeInterfaceIndex_Type())
hpSwitchFipsSessEnodeInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsSessEnodeInterfaceIndex.setStatus(_A)
_HpSwitchFipsSessEnodeFPMAMacAddress_Type=MacAddress
_HpSwitchFipsSessEnodeFPMAMacAddress_Object=MibTableColumn
hpSwitchFipsSessEnodeFPMAMacAddress=_HpSwitchFipsSessEnodeFPMAMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,2),_HpSwitchFipsSessEnodeFPMAMacAddress_Type())
hpSwitchFipsSessEnodeFPMAMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsSessEnodeFPMAMacAddress.setStatus(_A)
_HpSwitchFipsSessEnodeMacAddress_Type=MacAddress
_HpSwitchFipsSessEnodeMacAddress_Object=MibTableColumn
hpSwitchFipsSessEnodeMacAddress=_HpSwitchFipsSessEnodeMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,3),_HpSwitchFipsSessEnodeMacAddress_Type())
hpSwitchFipsSessEnodeMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessEnodeMacAddress.setStatus(_A)
class _HpSwitchFipsSessEnodeNportId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpSwitchFipsSessEnodeNportId_Type.__name__=_D
_HpSwitchFipsSessEnodeNportId_Object=MibTableColumn
hpSwitchFipsSessEnodeNportId=_HpSwitchFipsSessEnodeNportId_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,4),_HpSwitchFipsSessEnodeNportId_Type())
hpSwitchFipsSessEnodeNportId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessEnodeNportId.setStatus(_A)
class _HpSwitchFipsSessEnodeNportIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flogi',1),('npivfdisc',2)))
_HpSwitchFipsSessEnodeNportIdType_Type.__name__=_F
_HpSwitchFipsSessEnodeNportIdType_Object=MibTableColumn
hpSwitchFipsSessEnodeNportIdType=_HpSwitchFipsSessEnodeNportIdType_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,5),_HpSwitchFipsSessEnodeNportIdType_Type())
hpSwitchFipsSessEnodeNportIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessEnodeNportIdType.setStatus(_A)
_HpSwitchFipsSessFcfMacAddress_Type=MacAddress
_HpSwitchFipsSessFcfMacAddress_Object=MibTableColumn
hpSwitchFipsSessFcfMacAddress=_HpSwitchFipsSessFcfMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,6),_HpSwitchFipsSessFcfMacAddress_Type())
hpSwitchFipsSessFcfMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessFcfMacAddress.setStatus(_A)
class _HpSwitchFipsSessFcMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpSwitchFipsSessFcMap_Type.__name__=_D
_HpSwitchFipsSessFcMap_Object=MibTableColumn
hpSwitchFipsSessFcMap=_HpSwitchFipsSessFcMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,7),_HpSwitchFipsSessFcMap_Type())
hpSwitchFipsSessFcMap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessFcMap.setStatus(_A)
_HpSwitchFipsSessVlanId_Type=Integer32
_HpSwitchFipsSessVlanId_Object=MibTableColumn
hpSwitchFipsSessVlanId=_HpSwitchFipsSessVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,8),_HpSwitchFipsSessVlanId_Type())
hpSwitchFipsSessVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessVlanId.setStatus(_A)
class _HpSwitchFipsSessFcfNameId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpSwitchFipsSessFcfNameId_Type.__name__=_D
_HpSwitchFipsSessFcfNameId_Object=MibTableColumn
hpSwitchFipsSessFcfNameId=_HpSwitchFipsSessFcfNameId_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,1,2,3,1,9),_HpSwitchFipsSessFcfNameId_Type())
hpSwitchFipsSessFcfNameId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsSessFcfNameId.setStatus(_A)
_HpSwitchFipsStatistics_ObjectIdentity=ObjectIdentity
hpSwitchFipsStatistics=_HpSwitchFipsStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,2))
_HpSwitchFipsGlobalStats_ObjectIdentity=ObjectIdentity
hpSwitchFipsGlobalStats=_HpSwitchFipsGlobalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,2,1))
_HpSwitchFipsFipDropPkts_Type=Counter64
_HpSwitchFipsFipDropPkts_Object=MibScalar
hpSwitchFipsFipDropPkts=_HpSwitchFipsFipDropPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,1,1),_HpSwitchFipsFipDropPkts_Type())
hpSwitchFipsFipDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFipDropPkts.setStatus(_A)
_HpSwitchFipsFcoeDropPkts_Type=Counter64
_HpSwitchFipsFcoeDropPkts_Object=MibScalar
hpSwitchFipsFcoeDropPkts=_HpSwitchFipsFcoeDropPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,1,2),_HpSwitchFipsFcoeDropPkts_Type())
hpSwitchFipsFcoeDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsFcoeDropPkts.setStatus(_A)
_HpSwitchFipsSessStats_ObjectIdentity=ObjectIdentity
hpSwitchFipsSessStats=_HpSwitchFipsSessStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2))
_HpSwitchFipsSessStatsTable_Object=MibTable
hpSwitchFipsSessStatsTable=_HpSwitchFipsSessStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1))
if mibBuilder.loadTexts:hpSwitchFipsSessStatsTable.setStatus(_A)
_HpSwitchFipsSessStatsEntry_Object=MibTableRow
hpSwitchFipsSessStatsEntry=_HpSwitchFipsSessStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1,1))
hpSwitchFipsSessStatsEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hpSwitchFipsSessStatsEntry.setStatus(_A)
_HpSwitchFipsStatsSessEnodeIfIndex_Type=InterfaceIndex
_HpSwitchFipsStatsSessEnodeIfIndex_Object=MibTableColumn
hpSwitchFipsStatsSessEnodeIfIndex=_HpSwitchFipsStatsSessEnodeIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1,1,1),_HpSwitchFipsStatsSessEnodeIfIndex_Type())
hpSwitchFipsStatsSessEnodeIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsStatsSessEnodeIfIndex.setStatus(_A)
_HpSwitchFipsStatsSessFPMAMacAddress_Type=MacAddress
_HpSwitchFipsStatsSessFPMAMacAddress_Object=MibTableColumn
hpSwitchFipsStatsSessFPMAMacAddress=_HpSwitchFipsStatsSessFPMAMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1,1,2),_HpSwitchFipsStatsSessFPMAMacAddress_Type())
hpSwitchFipsStatsSessFPMAMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpSwitchFipsStatsSessFPMAMacAddress.setStatus(_A)
_HpSwitchFipsStatsSessFcfMacAddress_Type=MacAddress
_HpSwitchFipsStatsSessFcfMacAddress_Object=MibTableColumn
hpSwitchFipsStatsSessFcfMacAddress=_HpSwitchFipsStatsSessFcfMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1,1,3),_HpSwitchFipsStatsSessFcfMacAddress_Type())
hpSwitchFipsStatsSessFcfMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsStatsSessFcfMacAddress.setStatus(_A)
_HpSwitchFipsStatsSessFcoePermitPkts_Type=Counter64
_HpSwitchFipsStatsSessFcoePermitPkts_Object=MibTableColumn
hpSwitchFipsStatsSessFcoePermitPkts=_HpSwitchFipsStatsSessFcoePermitPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,78,2,2,1,1,4),_HpSwitchFipsStatsSessFcoePermitPkts_Type())
hpSwitchFipsStatsSessFcoePermitPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFipsStatsSessFcoePermitPkts.setStatus(_A)
_HpSwitchFipsConformance_ObjectIdentity=ObjectIdentity
hpSwitchFipsConformance=_HpSwitchFipsConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,3))
_HpSwitchFipsCompliances_ObjectIdentity=ObjectIdentity
hpSwitchFipsCompliances=_HpSwitchFipsCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,3,1))
_HpSwitchFipsGroups_ObjectIdentity=ObjectIdentity
hpSwitchFipsGroups=_HpSwitchFipsGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,78,3,2))
hpSwitchFipsConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,78,3,2,1))
hpSwitchFipsConfigGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:hpSwitchFipsConfigGroup.setStatus(_A)
hpSwitchFipsSessionGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,78,3,2,2))
hpSwitchFipsSessionGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:hpSwitchFipsSessionGroup.setStatus(_A)
hpSwitchFipsStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,78,3,2,3))
hpSwitchFipsStatisticsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:hpSwitchFipsStatisticsGroup.setStatus(_A)
hpSwitchFipsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,78,3,1,1))
hpSwitchFipsCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:hpSwitchFipsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpSwitchFipSnoopingMib':hpSwitchFipSnoopingMib,'hpSwitchFipsConfigObjects':hpSwitchFipsConfigObjects,'hpSwitchFipsScalars':hpSwitchFipsScalars,_O:hpSwitchFipsAdminStatus,'hpSwitchFipsTables':hpSwitchFipsTables,'hpSwitchFipsFcMapTable':hpSwitchFipsFcMapTable,'hpSwitchFipsFcMapEntry':hpSwitchFipsFcMapEntry,_H:hpSwitchFipsFcMapIndex,_P:hpSwitchFipsFcMap,'hpSwitchFipsFcfMacAddressTable':hpSwitchFipsFcfMacAddressTable,'hpSwitchFipsFcfMacAddressEntry':hpSwitchFipsFcfMacAddressEntry,_I:hpSwitchFipsVirtualFabricInterfaceIndex,_J:hpSwitchFipsFcfMacAddress,_Q:hpSwitchFipsFcoeVlanId,_R:hpSwitchFipsFcfFcMap,_S:hpSwitchFipsFcfEnodeLoginCount,_T:hpSwitchFipsFcfNameId,_U:hpSwitchFipsFabricName,_V:hpSwitchFipsFcfMacTableRowStatus,'hpSwitchFipsSessionTable':hpSwitchFipsSessionTable,'hpSwitchFipsSessionEntry':hpSwitchFipsSessionEntry,_K:hpSwitchFipsSessEnodeInterfaceIndex,_L:hpSwitchFipsSessEnodeFPMAMacAddress,_W:hpSwitchFipsSessEnodeMacAddress,_X:hpSwitchFipsSessEnodeNportId,_Y:hpSwitchFipsSessEnodeNportIdType,_Z:hpSwitchFipsSessFcfMacAddress,_a:hpSwitchFipsSessFcMap,_b:hpSwitchFipsSessVlanId,_c:hpSwitchFipsSessFcfNameId,'hpSwitchFipsStatistics':hpSwitchFipsStatistics,'hpSwitchFipsGlobalStats':hpSwitchFipsGlobalStats,_d:hpSwitchFipsFipDropPkts,_e:hpSwitchFipsFcoeDropPkts,'hpSwitchFipsSessStats':hpSwitchFipsSessStats,'hpSwitchFipsSessStatsTable':hpSwitchFipsSessStatsTable,'hpSwitchFipsSessStatsEntry':hpSwitchFipsSessStatsEntry,_M:hpSwitchFipsStatsSessEnodeIfIndex,_N:hpSwitchFipsStatsSessFPMAMacAddress,_f:hpSwitchFipsStatsSessFcfMacAddress,_g:hpSwitchFipsStatsSessFcoePermitPkts,'hpSwitchFipsConformance':hpSwitchFipsConformance,'hpSwitchFipsCompliances':hpSwitchFipsCompliances,'hpSwitchFipsCompliance':hpSwitchFipsCompliance,'hpSwitchFipsGroups':hpSwitchFipsGroups,_h:hpSwitchFipsConfigGroup,_i:hpSwitchFipsSessionGroup,_j:hpSwitchFipsStatisticsGroup})