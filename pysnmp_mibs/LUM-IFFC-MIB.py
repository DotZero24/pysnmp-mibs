_Z='ifFcPhysicalGroupV3'
_Y='ifFcPhysicalGroupV2'
_X='ifFcPhysicalGroupV1'
_W='ifFcPhysicalTxLocalLinkFault'
_V='ifFcPhysicalRxLocalLinkFault'
_U='ifFcPhysicalRxHighBitErrorRate'
_T='ifFcGeneralIfFcPhysicalStateLastChangeTime'
_S='ifFcGeneralIfFcPhysicalConfigLastChangeTime'
_R='ifFcGeneralIfFcPhysicalTableSize'
_Q='ifFcGeneralStateLastChangeTime'
_P='ifFcGeneralConfigLastChangeTime'
_O='ifFcPhysicalTxPcsLossOfSync'
_N='ifFcGeneralGroupV1'
_M='deprecated'
_L='ifFcPhysicalPcsLossOfSync'
_K='ifFcPhysicalLinkDown'
_J='ifFcPhysicalLocalLinkFault'
_I='ifFcPhysicalRemoteLinkFault'
_H='ifFcPhysicalRxSignalStatus'
_G='ifFcPhysicalTxSignalStatus'
_F='ifFcPhysicalConnIfBasicIfIndex'
_E='ifFcPhysicalName'
_D='ifFcPhysicalIndex'
_C='read-only'
_B='current'
_A='LUM-IFFC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfFcMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfFcMIB','lumModules')
FaultStatusWithNA,MgmtNameString,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','FaultStatusWithNA','MgmtNameString','SignalStatusWithNA','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfFcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,59))
if mibBuilder.loadTexts:lumIfFcMIBModule.setRevisions(('2018-08-01 00:00','2017-06-15 00:00','2015-09-30 00:00','2013-11-20 00:00'))
_LumIfFcConfs_ObjectIdentity=ObjectIdentity
lumIfFcConfs=_LumIfFcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,59,1))
_LumIfFcGroups_ObjectIdentity=ObjectIdentity
lumIfFcGroups=_LumIfFcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,59,1,1))
_LumIfFcCompl_ObjectIdentity=ObjectIdentity
lumIfFcCompl=_LumIfFcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,59,1,2))
_LumIfFcMIBObjects_ObjectIdentity=ObjectIdentity
lumIfFcMIBObjects=_LumIfFcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,59,2))
_IfFcGeneral_ObjectIdentity=ObjectIdentity
ifFcGeneral=_IfFcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,59,2,1))
_IfFcGeneralConfigLastChangeTime_Type=DateAndTime
_IfFcGeneralConfigLastChangeTime_Object=MibScalar
ifFcGeneralConfigLastChangeTime=_IfFcGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,59,2,1,1),_IfFcGeneralConfigLastChangeTime_Type())
ifFcGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcGeneralConfigLastChangeTime.setStatus(_B)
_IfFcGeneralStateLastChangeTime_Type=DateAndTime
_IfFcGeneralStateLastChangeTime_Object=MibScalar
ifFcGeneralStateLastChangeTime=_IfFcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,59,2,1,2),_IfFcGeneralStateLastChangeTime_Type())
ifFcGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcGeneralStateLastChangeTime.setStatus(_B)
_IfFcGeneralIfFcPhysicalTableSize_Type=Unsigned32
_IfFcGeneralIfFcPhysicalTableSize_Object=MibScalar
ifFcGeneralIfFcPhysicalTableSize=_IfFcGeneralIfFcPhysicalTableSize_Object((1,3,6,1,4,1,8708,2,59,2,1,3),_IfFcGeneralIfFcPhysicalTableSize_Type())
ifFcGeneralIfFcPhysicalTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcGeneralIfFcPhysicalTableSize.setStatus(_B)
_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Type=DateAndTime
_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Object=MibScalar
ifFcGeneralIfFcPhysicalConfigLastChangeTime=_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,59,2,1,4),_IfFcGeneralIfFcPhysicalConfigLastChangeTime_Type())
ifFcGeneralIfFcPhysicalConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcGeneralIfFcPhysicalConfigLastChangeTime.setStatus(_B)
_IfFcGeneralIfFcPhysicalStateLastChangeTime_Type=DateAndTime
_IfFcGeneralIfFcPhysicalStateLastChangeTime_Object=MibScalar
ifFcGeneralIfFcPhysicalStateLastChangeTime=_IfFcGeneralIfFcPhysicalStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,59,2,1,5),_IfFcGeneralIfFcPhysicalStateLastChangeTime_Type())
ifFcGeneralIfFcPhysicalStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcGeneralIfFcPhysicalStateLastChangeTime.setStatus(_B)
_IfFcPhysicalList_ObjectIdentity=ObjectIdentity
ifFcPhysicalList=_IfFcPhysicalList_ObjectIdentity((1,3,6,1,4,1,8708,2,59,2,2))
_IfFcPhysicalTable_Object=MibTable
ifFcPhysicalTable=_IfFcPhysicalTable_Object((1,3,6,1,4,1,8708,2,59,2,2,1))
if mibBuilder.loadTexts:ifFcPhysicalTable.setStatus(_B)
_IfFcPhysicalEntry_Object=MibTableRow
ifFcPhysicalEntry=_IfFcPhysicalEntry_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1))
ifFcPhysicalEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:ifFcPhysicalEntry.setStatus(_B)
_IfFcPhysicalIndex_Type=Unsigned32
_IfFcPhysicalIndex_Object=MibTableColumn
ifFcPhysicalIndex=_IfFcPhysicalIndex_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,1),_IfFcPhysicalIndex_Type())
ifFcPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalIndex.setStatus(_B)
_IfFcPhysicalName_Type=MgmtNameString
_IfFcPhysicalName_Object=MibTableColumn
ifFcPhysicalName=_IfFcPhysicalName_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,2),_IfFcPhysicalName_Type())
ifFcPhysicalName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalName.setStatus(_B)
_IfFcPhysicalConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfFcPhysicalConnIfBasicIfIndex_Object=MibTableColumn
ifFcPhysicalConnIfBasicIfIndex=_IfFcPhysicalConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,3),_IfFcPhysicalConnIfBasicIfIndex_Type())
ifFcPhysicalConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalConnIfBasicIfIndex.setStatus(_B)
_IfFcPhysicalTxSignalStatus_Type=SignalStatusWithNA
_IfFcPhysicalTxSignalStatus_Object=MibTableColumn
ifFcPhysicalTxSignalStatus=_IfFcPhysicalTxSignalStatus_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,4),_IfFcPhysicalTxSignalStatus_Type())
ifFcPhysicalTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalTxSignalStatus.setStatus(_B)
_IfFcPhysicalRxSignalStatus_Type=SignalStatusWithNA
_IfFcPhysicalRxSignalStatus_Object=MibTableColumn
ifFcPhysicalRxSignalStatus=_IfFcPhysicalRxSignalStatus_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,5),_IfFcPhysicalRxSignalStatus_Type())
ifFcPhysicalRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalRxSignalStatus.setStatus(_B)
_IfFcPhysicalRemoteLinkFault_Type=FaultStatusWithNA
_IfFcPhysicalRemoteLinkFault_Object=MibTableColumn
ifFcPhysicalRemoteLinkFault=_IfFcPhysicalRemoteLinkFault_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,6),_IfFcPhysicalRemoteLinkFault_Type())
ifFcPhysicalRemoteLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalRemoteLinkFault.setStatus(_B)
_IfFcPhysicalLocalLinkFault_Type=FaultStatusWithNA
_IfFcPhysicalLocalLinkFault_Object=MibTableColumn
ifFcPhysicalLocalLinkFault=_IfFcPhysicalLocalLinkFault_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,7),_IfFcPhysicalLocalLinkFault_Type())
ifFcPhysicalLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalLocalLinkFault.setStatus(_B)
_IfFcPhysicalLinkDown_Type=FaultStatusWithNA
_IfFcPhysicalLinkDown_Object=MibTableColumn
ifFcPhysicalLinkDown=_IfFcPhysicalLinkDown_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,8),_IfFcPhysicalLinkDown_Type())
ifFcPhysicalLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalLinkDown.setStatus(_B)
_IfFcPhysicalPcsLossOfSync_Type=FaultStatusWithNA
_IfFcPhysicalPcsLossOfSync_Object=MibTableColumn
ifFcPhysicalPcsLossOfSync=_IfFcPhysicalPcsLossOfSync_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,9),_IfFcPhysicalPcsLossOfSync_Type())
ifFcPhysicalPcsLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalPcsLossOfSync.setStatus(_B)
_IfFcPhysicalTxPcsLossOfSync_Type=FaultStatusWithNA
_IfFcPhysicalTxPcsLossOfSync_Object=MibTableColumn
ifFcPhysicalTxPcsLossOfSync=_IfFcPhysicalTxPcsLossOfSync_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,10),_IfFcPhysicalTxPcsLossOfSync_Type())
ifFcPhysicalTxPcsLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalTxPcsLossOfSync.setStatus(_B)
_IfFcPhysicalRxHighBitErrorRate_Type=FaultStatusWithNA
_IfFcPhysicalRxHighBitErrorRate_Object=MibTableColumn
ifFcPhysicalRxHighBitErrorRate=_IfFcPhysicalRxHighBitErrorRate_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,11),_IfFcPhysicalRxHighBitErrorRate_Type())
ifFcPhysicalRxHighBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalRxHighBitErrorRate.setStatus(_B)
_IfFcPhysicalRxLocalLinkFault_Type=FaultStatusWithNA
_IfFcPhysicalRxLocalLinkFault_Object=MibTableColumn
ifFcPhysicalRxLocalLinkFault=_IfFcPhysicalRxLocalLinkFault_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,12),_IfFcPhysicalRxLocalLinkFault_Type())
ifFcPhysicalRxLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalRxLocalLinkFault.setStatus(_B)
_IfFcPhysicalTxLocalLinkFault_Type=FaultStatusWithNA
_IfFcPhysicalTxLocalLinkFault_Object=MibTableColumn
ifFcPhysicalTxLocalLinkFault=_IfFcPhysicalTxLocalLinkFault_Object((1,3,6,1,4,1,8708,2,59,2,2,1,1,13),_IfFcPhysicalTxLocalLinkFault_Type())
ifFcPhysicalTxLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifFcPhysicalTxLocalLinkFault.setStatus(_B)
ifFcGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,59,1,1,1))
ifFcGeneralGroupV1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ifFcGeneralGroupV1.setStatus(_B)
ifFcPhysicalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,59,1,1,2))
ifFcPhysicalGroupV1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ifFcPhysicalGroupV1.setStatus(_M)
ifFcPhysicalGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,59,1,1,3))
ifFcPhysicalGroupV2.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O)))
if mibBuilder.loadTexts:ifFcPhysicalGroupV2.setStatus(_M)
ifFcPhysicalGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,59,1,1,4))
ifFcPhysicalGroupV3.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ifFcPhysicalGroupV3.setStatus(_B)
lumIfFcComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,59,1,2,1))
lumIfFcComplV1.setObjects(*((_A,_N),(_A,_X)))
if mibBuilder.loadTexts:lumIfFcComplV1.setStatus(_M)
lumIfFcComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,59,1,2,2))
lumIfFcComplV2.setObjects(*((_A,_N),(_A,_Y)))
if mibBuilder.loadTexts:lumIfFcComplV2.setStatus(_M)
lumIfFcComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,59,1,2,3))
lumIfFcComplV3.setObjects(*((_A,_N),(_A,_Z)))
if mibBuilder.loadTexts:lumIfFcComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfFcMIBModule':lumIfFcMIBModule,'lumIfFcConfs':lumIfFcConfs,'lumIfFcGroups':lumIfFcGroups,_N:ifFcGeneralGroupV1,_X:ifFcPhysicalGroupV1,_Y:ifFcPhysicalGroupV2,_Z:ifFcPhysicalGroupV3,'lumIfFcCompl':lumIfFcCompl,'lumIfFcComplV1':lumIfFcComplV1,'lumIfFcComplV2':lumIfFcComplV2,'lumIfFcComplV3':lumIfFcComplV3,'lumIfFcMIBObjects':lumIfFcMIBObjects,'ifFcGeneral':ifFcGeneral,_P:ifFcGeneralConfigLastChangeTime,_Q:ifFcGeneralStateLastChangeTime,_R:ifFcGeneralIfFcPhysicalTableSize,_S:ifFcGeneralIfFcPhysicalConfigLastChangeTime,_T:ifFcGeneralIfFcPhysicalStateLastChangeTime,'ifFcPhysicalList':ifFcPhysicalList,'ifFcPhysicalTable':ifFcPhysicalTable,'ifFcPhysicalEntry':ifFcPhysicalEntry,_D:ifFcPhysicalIndex,_E:ifFcPhysicalName,_F:ifFcPhysicalConnIfBasicIfIndex,_G:ifFcPhysicalTxSignalStatus,_H:ifFcPhysicalRxSignalStatus,_I:ifFcPhysicalRemoteLinkFault,_J:ifFcPhysicalLocalLinkFault,_K:ifFcPhysicalLinkDown,_L:ifFcPhysicalPcsLossOfSync,_O:ifFcPhysicalTxPcsLossOfSync,_U:ifFcPhysicalRxHighBitErrorRate,_V:ifFcPhysicalRxLocalLinkFault,_W:ifFcPhysicalTxLocalLinkFault})