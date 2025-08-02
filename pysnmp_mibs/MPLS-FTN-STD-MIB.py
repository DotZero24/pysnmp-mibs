_t='mplsFTNPerfDiscontinuityTime'
_s='mplsFTNPerfMatchedOctets'
_r='mplsFTNPerfMatchedPackets'
_q='mplsFTNMapStorageType'
_p='mplsFTNMapRowStatus'
_o='mplsFTNMapTableLastChanged'
_n='mplsFTNStorageType'
_m='mplsFTNDscp'
_l='mplsFTNActionPointer'
_k='mplsFTNActionType'
_j='mplsFTNProtocol'
_i='mplsFTNDestPortMax'
_h='mplsFTNDestPortMin'
_g='mplsFTNSourcePortMax'
_f='mplsFTNSourcePortMin'
_e='mplsFTNDestAddrMax'
_d='mplsFTNDestAddrMin'
_c='mplsFTNSourceAddrMax'
_b='mplsFTNSourceAddrMin'
_a='mplsFTNAddrType'
_Z='mplsFTNMask'
_Y='mplsFTNDescr'
_X='mplsFTNRowStatus'
_W='mplsFTNTableLastChanged'
_V='mplsFTNIndexNext'
_U='mplsFTNPerfCurrIndex'
_T='mplsFTNPerfIndex'
_S='mplsFTNMapCurrIndex'
_R='mplsFTNMapPrevIndex'
_Q='mplsFTNMapIndex'
_P='mplsFTNIndex'
_O='RowStatus'
_N='mplsFTNPerfGroup'
_M='mplsFTNMapGroup'
_L='mplsFTNRuleGroup'
_K='StorageType'
_J='Integer32'
_I='ifGeneralInformationGroup'
_H='ifCounterDiscontinuityGroup'
_G='InetPortNumber'
_F='IF-MIB'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='MPLS-FTN-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
InterfaceIndexOrZero,ifCounterDiscontinuityGroup,ifGeneralInformationGroup=mibBuilder.importSymbols(_F,'InterfaceIndexOrZero',_H,_I)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_G)
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer',_O,_K,'TextualConvention','TimeStamp')
mplsFTNStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,8))
if mibBuilder.loadTexts:mplsFTNStdMIB.setRevisions(('2004-06-03 00:00',))
class MplsFTNEntryIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class MplsFTNEntryIndexOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MplsFTNNotifications_ObjectIdentity=ObjectIdentity
mplsFTNNotifications=_MplsFTNNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,8,0))
_MplsFTNObjects_ObjectIdentity=ObjectIdentity
mplsFTNObjects=_MplsFTNObjects_ObjectIdentity((1,3,6,1,2,1,10,166,8,1))
_MplsFTNIndexNext_Type=MplsFTNEntryIndexOrZero
_MplsFTNIndexNext_Object=MibScalar
mplsFTNIndexNext=_MplsFTNIndexNext_Object((1,3,6,1,2,1,10,166,8,1,1),_MplsFTNIndexNext_Type())
mplsFTNIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNIndexNext.setStatus(_A)
_MplsFTNTableLastChanged_Type=TimeStamp
_MplsFTNTableLastChanged_Object=MibScalar
mplsFTNTableLastChanged=_MplsFTNTableLastChanged_Object((1,3,6,1,2,1,10,166,8,1,2),_MplsFTNTableLastChanged_Type())
mplsFTNTableLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNTableLastChanged.setStatus(_A)
_MplsFTNTable_Object=MibTable
mplsFTNTable=_MplsFTNTable_Object((1,3,6,1,2,1,10,166,8,1,3))
if mibBuilder.loadTexts:mplsFTNTable.setStatus(_A)
_MplsFTNEntry_Object=MibTableRow
mplsFTNEntry=_MplsFTNEntry_Object((1,3,6,1,2,1,10,166,8,1,3,1))
mplsFTNEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:mplsFTNEntry.setStatus(_A)
_MplsFTNIndex_Type=MplsFTNEntryIndex
_MplsFTNIndex_Object=MibTableColumn
mplsFTNIndex=_MplsFTNIndex_Object((1,3,6,1,2,1,10,166,8,1,3,1,1),_MplsFTNIndex_Type())
mplsFTNIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNIndex.setStatus(_A)
_MplsFTNRowStatus_Type=RowStatus
_MplsFTNRowStatus_Object=MibTableColumn
mplsFTNRowStatus=_MplsFTNRowStatus_Object((1,3,6,1,2,1,10,166,8,1,3,1,2),_MplsFTNRowStatus_Type())
mplsFTNRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNRowStatus.setStatus(_A)
_MplsFTNDescr_Type=SnmpAdminString
_MplsFTNDescr_Object=MibTableColumn
mplsFTNDescr=_MplsFTNDescr_Object((1,3,6,1,2,1,10,166,8,1,3,1,3),_MplsFTNDescr_Type())
mplsFTNDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDescr.setStatus(_A)
class _MplsFTNMask_Type(Bits):namedValues=NamedValues(*(('sourceAddr',0),('destAddr',1),('sourcePort',2),('destPort',3),('protocol',4),('dscp',5)))
_MplsFTNMask_Type.__name__='Bits'
_MplsFTNMask_Object=MibTableColumn
mplsFTNMask=_MplsFTNMask_Object((1,3,6,1,2,1,10,166,8,1,3,1,4),_MplsFTNMask_Type())
mplsFTNMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNMask.setStatus(_A)
_MplsFTNAddrType_Type=InetAddressType
_MplsFTNAddrType_Object=MibTableColumn
mplsFTNAddrType=_MplsFTNAddrType_Object((1,3,6,1,2,1,10,166,8,1,3,1,5),_MplsFTNAddrType_Type())
mplsFTNAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNAddrType.setStatus(_A)
_MplsFTNSourceAddrMin_Type=InetAddress
_MplsFTNSourceAddrMin_Object=MibTableColumn
mplsFTNSourceAddrMin=_MplsFTNSourceAddrMin_Object((1,3,6,1,2,1,10,166,8,1,3,1,6),_MplsFTNSourceAddrMin_Type())
mplsFTNSourceAddrMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNSourceAddrMin.setStatus(_A)
_MplsFTNSourceAddrMax_Type=InetAddress
_MplsFTNSourceAddrMax_Object=MibTableColumn
mplsFTNSourceAddrMax=_MplsFTNSourceAddrMax_Object((1,3,6,1,2,1,10,166,8,1,3,1,7),_MplsFTNSourceAddrMax_Type())
mplsFTNSourceAddrMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNSourceAddrMax.setStatus(_A)
_MplsFTNDestAddrMin_Type=InetAddress
_MplsFTNDestAddrMin_Object=MibTableColumn
mplsFTNDestAddrMin=_MplsFTNDestAddrMin_Object((1,3,6,1,2,1,10,166,8,1,3,1,8),_MplsFTNDestAddrMin_Type())
mplsFTNDestAddrMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDestAddrMin.setStatus(_A)
_MplsFTNDestAddrMax_Type=InetAddress
_MplsFTNDestAddrMax_Object=MibTableColumn
mplsFTNDestAddrMax=_MplsFTNDestAddrMax_Object((1,3,6,1,2,1,10,166,8,1,3,1,9),_MplsFTNDestAddrMax_Type())
mplsFTNDestAddrMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDestAddrMax.setStatus(_A)
class _MplsFTNSourcePortMin_Type(InetPortNumber):defaultValue=0
_MplsFTNSourcePortMin_Type.__name__=_G
_MplsFTNSourcePortMin_Object=MibTableColumn
mplsFTNSourcePortMin=_MplsFTNSourcePortMin_Object((1,3,6,1,2,1,10,166,8,1,3,1,10),_MplsFTNSourcePortMin_Type())
mplsFTNSourcePortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNSourcePortMin.setStatus(_A)
class _MplsFTNSourcePortMax_Type(InetPortNumber):defaultValue=65535
_MplsFTNSourcePortMax_Type.__name__=_G
_MplsFTNSourcePortMax_Object=MibTableColumn
mplsFTNSourcePortMax=_MplsFTNSourcePortMax_Object((1,3,6,1,2,1,10,166,8,1,3,1,11),_MplsFTNSourcePortMax_Type())
mplsFTNSourcePortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNSourcePortMax.setStatus(_A)
class _MplsFTNDestPortMin_Type(InetPortNumber):defaultValue=0
_MplsFTNDestPortMin_Type.__name__=_G
_MplsFTNDestPortMin_Object=MibTableColumn
mplsFTNDestPortMin=_MplsFTNDestPortMin_Object((1,3,6,1,2,1,10,166,8,1,3,1,12),_MplsFTNDestPortMin_Type())
mplsFTNDestPortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDestPortMin.setStatus(_A)
class _MplsFTNDestPortMax_Type(InetPortNumber):defaultValue=65535
_MplsFTNDestPortMax_Type.__name__=_G
_MplsFTNDestPortMax_Object=MibTableColumn
mplsFTNDestPortMax=_MplsFTNDestPortMax_Object((1,3,6,1,2,1,10,166,8,1,3,1,13),_MplsFTNDestPortMax_Type())
mplsFTNDestPortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDestPortMax.setStatus(_A)
class _MplsFTNProtocol_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MplsFTNProtocol_Type.__name__=_J
_MplsFTNProtocol_Object=MibTableColumn
mplsFTNProtocol=_MplsFTNProtocol_Object((1,3,6,1,2,1,10,166,8,1,3,1,14),_MplsFTNProtocol_Type())
mplsFTNProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNProtocol.setStatus(_A)
_MplsFTNDscp_Type=Dscp
_MplsFTNDscp_Object=MibTableColumn
mplsFTNDscp=_MplsFTNDscp_Object((1,3,6,1,2,1,10,166,8,1,3,1,15),_MplsFTNDscp_Type())
mplsFTNDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNDscp.setStatus(_A)
class _MplsFTNActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redirectLsp',1),('redirectTunnel',2)))
_MplsFTNActionType_Type.__name__=_J
_MplsFTNActionType_Object=MibTableColumn
mplsFTNActionType=_MplsFTNActionType_Object((1,3,6,1,2,1,10,166,8,1,3,1,16),_MplsFTNActionType_Type())
mplsFTNActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNActionType.setStatus(_A)
_MplsFTNActionPointer_Type=RowPointer
_MplsFTNActionPointer_Object=MibTableColumn
mplsFTNActionPointer=_MplsFTNActionPointer_Object((1,3,6,1,2,1,10,166,8,1,3,1,17),_MplsFTNActionPointer_Type())
mplsFTNActionPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNActionPointer.setStatus(_A)
class _MplsFTNStorageType_Type(StorageType):defaultValue=3
_MplsFTNStorageType_Type.__name__=_K
_MplsFTNStorageType_Object=MibTableColumn
mplsFTNStorageType=_MplsFTNStorageType_Object((1,3,6,1,2,1,10,166,8,1,3,1,18),_MplsFTNStorageType_Type())
mplsFTNStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNStorageType.setStatus(_A)
_MplsFTNMapTableLastChanged_Type=TimeStamp
_MplsFTNMapTableLastChanged_Object=MibScalar
mplsFTNMapTableLastChanged=_MplsFTNMapTableLastChanged_Object((1,3,6,1,2,1,10,166,8,1,4),_MplsFTNMapTableLastChanged_Type())
mplsFTNMapTableLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNMapTableLastChanged.setStatus(_A)
_MplsFTNMapTable_Object=MibTable
mplsFTNMapTable=_MplsFTNMapTable_Object((1,3,6,1,2,1,10,166,8,1,5))
if mibBuilder.loadTexts:mplsFTNMapTable.setStatus(_A)
_MplsFTNMapEntry_Object=MibTableRow
mplsFTNMapEntry=_MplsFTNMapEntry_Object((1,3,6,1,2,1,10,166,8,1,5,1))
mplsFTNMapEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:mplsFTNMapEntry.setStatus(_A)
_MplsFTNMapIndex_Type=InterfaceIndexOrZero
_MplsFTNMapIndex_Object=MibTableColumn
mplsFTNMapIndex=_MplsFTNMapIndex_Object((1,3,6,1,2,1,10,166,8,1,5,1,1),_MplsFTNMapIndex_Type())
mplsFTNMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNMapIndex.setStatus(_A)
_MplsFTNMapPrevIndex_Type=MplsFTNEntryIndexOrZero
_MplsFTNMapPrevIndex_Object=MibTableColumn
mplsFTNMapPrevIndex=_MplsFTNMapPrevIndex_Object((1,3,6,1,2,1,10,166,8,1,5,1,2),_MplsFTNMapPrevIndex_Type())
mplsFTNMapPrevIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNMapPrevIndex.setStatus(_A)
_MplsFTNMapCurrIndex_Type=MplsFTNEntryIndex
_MplsFTNMapCurrIndex_Object=MibTableColumn
mplsFTNMapCurrIndex=_MplsFTNMapCurrIndex_Object((1,3,6,1,2,1,10,166,8,1,5,1,3),_MplsFTNMapCurrIndex_Type())
mplsFTNMapCurrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNMapCurrIndex.setStatus(_A)
class _MplsFTNMapRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*(('active',1),('createAndGo',4),('destroy',6)))
_MplsFTNMapRowStatus_Type.__name__=_O
_MplsFTNMapRowStatus_Object=MibTableColumn
mplsFTNMapRowStatus=_MplsFTNMapRowStatus_Object((1,3,6,1,2,1,10,166,8,1,5,1,4),_MplsFTNMapRowStatus_Type())
mplsFTNMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNMapRowStatus.setStatus(_A)
class _MplsFTNMapStorageType_Type(StorageType):defaultValue=3
_MplsFTNMapStorageType_Type.__name__=_K
_MplsFTNMapStorageType_Object=MibTableColumn
mplsFTNMapStorageType=_MplsFTNMapStorageType_Object((1,3,6,1,2,1,10,166,8,1,5,1,5),_MplsFTNMapStorageType_Type())
mplsFTNMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsFTNMapStorageType.setStatus(_A)
_MplsFTNPerfTable_Object=MibTable
mplsFTNPerfTable=_MplsFTNPerfTable_Object((1,3,6,1,2,1,10,166,8,1,6))
if mibBuilder.loadTexts:mplsFTNPerfTable.setStatus(_A)
_MplsFTNPerfEntry_Object=MibTableRow
mplsFTNPerfEntry=_MplsFTNPerfEntry_Object((1,3,6,1,2,1,10,166,8,1,6,1))
mplsFTNPerfEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:mplsFTNPerfEntry.setStatus(_A)
_MplsFTNPerfIndex_Type=InterfaceIndexOrZero
_MplsFTNPerfIndex_Object=MibTableColumn
mplsFTNPerfIndex=_MplsFTNPerfIndex_Object((1,3,6,1,2,1,10,166,8,1,6,1,1),_MplsFTNPerfIndex_Type())
mplsFTNPerfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNPerfIndex.setStatus(_A)
_MplsFTNPerfCurrIndex_Type=MplsFTNEntryIndex
_MplsFTNPerfCurrIndex_Object=MibTableColumn
mplsFTNPerfCurrIndex=_MplsFTNPerfCurrIndex_Object((1,3,6,1,2,1,10,166,8,1,6,1,2),_MplsFTNPerfCurrIndex_Type())
mplsFTNPerfCurrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mplsFTNPerfCurrIndex.setStatus(_A)
_MplsFTNPerfMatchedPackets_Type=Counter64
_MplsFTNPerfMatchedPackets_Object=MibTableColumn
mplsFTNPerfMatchedPackets=_MplsFTNPerfMatchedPackets_Object((1,3,6,1,2,1,10,166,8,1,6,1,3),_MplsFTNPerfMatchedPackets_Type())
mplsFTNPerfMatchedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNPerfMatchedPackets.setStatus(_A)
_MplsFTNPerfMatchedOctets_Type=Counter64
_MplsFTNPerfMatchedOctets_Object=MibTableColumn
mplsFTNPerfMatchedOctets=_MplsFTNPerfMatchedOctets_Object((1,3,6,1,2,1,10,166,8,1,6,1,4),_MplsFTNPerfMatchedOctets_Type())
mplsFTNPerfMatchedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNPerfMatchedOctets.setStatus(_A)
_MplsFTNPerfDiscontinuityTime_Type=TimeStamp
_MplsFTNPerfDiscontinuityTime_Object=MibTableColumn
mplsFTNPerfDiscontinuityTime=_MplsFTNPerfDiscontinuityTime_Object((1,3,6,1,2,1,10,166,8,1,6,1,5),_MplsFTNPerfDiscontinuityTime_Type())
mplsFTNPerfDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsFTNPerfDiscontinuityTime.setStatus(_A)
_MplsFTNConformance_ObjectIdentity=ObjectIdentity
mplsFTNConformance=_MplsFTNConformance_ObjectIdentity((1,3,6,1,2,1,10,166,8,2))
_MplsFTNGroups_ObjectIdentity=ObjectIdentity
mplsFTNGroups=_MplsFTNGroups_ObjectIdentity((1,3,6,1,2,1,10,166,8,2,1))
_MplsFTNCompliances_ObjectIdentity=ObjectIdentity
mplsFTNCompliances=_MplsFTNCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,8,2,2))
mplsFTNRuleGroup=ObjectGroup((1,3,6,1,2,1,10,166,8,2,1,1))
mplsFTNRuleGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:mplsFTNRuleGroup.setStatus(_A)
mplsFTNMapGroup=ObjectGroup((1,3,6,1,2,1,10,166,8,2,1,2))
mplsFTNMapGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:mplsFTNMapGroup.setStatus(_A)
mplsFTNPerfGroup=ObjectGroup((1,3,6,1,2,1,10,166,8,2,1,3))
mplsFTNPerfGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:mplsFTNPerfGroup.setStatus(_A)
mplsFTNModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,8,2,2,1))
mplsFTNModuleFullCompliance.setObjects(*((_F,_I),(_F,_H),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mplsFTNModuleFullCompliance.setStatus(_A)
mplsFTNModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,8,2,2,2))
mplsFTNModuleReadOnlyCompliance.setObjects(*((_F,_I),(_F,_H),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mplsFTNModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MplsFTNEntryIndex':MplsFTNEntryIndex,'MplsFTNEntryIndexOrZero':MplsFTNEntryIndexOrZero,'mplsFTNStdMIB':mplsFTNStdMIB,'mplsFTNNotifications':mplsFTNNotifications,'mplsFTNObjects':mplsFTNObjects,_V:mplsFTNIndexNext,_W:mplsFTNTableLastChanged,'mplsFTNTable':mplsFTNTable,'mplsFTNEntry':mplsFTNEntry,_P:mplsFTNIndex,_X:mplsFTNRowStatus,_Y:mplsFTNDescr,_Z:mplsFTNMask,_a:mplsFTNAddrType,_b:mplsFTNSourceAddrMin,_c:mplsFTNSourceAddrMax,_d:mplsFTNDestAddrMin,_e:mplsFTNDestAddrMax,_f:mplsFTNSourcePortMin,_g:mplsFTNSourcePortMax,_h:mplsFTNDestPortMin,_i:mplsFTNDestPortMax,_j:mplsFTNProtocol,_m:mplsFTNDscp,_k:mplsFTNActionType,_l:mplsFTNActionPointer,_n:mplsFTNStorageType,_o:mplsFTNMapTableLastChanged,'mplsFTNMapTable':mplsFTNMapTable,'mplsFTNMapEntry':mplsFTNMapEntry,_Q:mplsFTNMapIndex,_R:mplsFTNMapPrevIndex,_S:mplsFTNMapCurrIndex,_p:mplsFTNMapRowStatus,_q:mplsFTNMapStorageType,'mplsFTNPerfTable':mplsFTNPerfTable,'mplsFTNPerfEntry':mplsFTNPerfEntry,_T:mplsFTNPerfIndex,_U:mplsFTNPerfCurrIndex,_r:mplsFTNPerfMatchedPackets,_s:mplsFTNPerfMatchedOctets,_t:mplsFTNPerfDiscontinuityTime,'mplsFTNConformance':mplsFTNConformance,'mplsFTNGroups':mplsFTNGroups,_L:mplsFTNRuleGroup,_M:mplsFTNMapGroup,_N:mplsFTNPerfGroup,'mplsFTNCompliances':mplsFTNCompliances,'mplsFTNModuleFullCompliance':mplsFTNModuleFullCompliance,'mplsFTNModuleReadOnlyCompliance':mplsFTNModuleReadOnlyCompliance})