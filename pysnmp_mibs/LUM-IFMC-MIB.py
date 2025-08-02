_n='ifMcPortGroupV5'
_m='ifMcPortGroupV4'
_l='ifMcPortGroupV3'
_k='ifMcPortGroupV2'
_j='ifMcPortGroupV1'
_i='ifMcPortMpoCableType'
_h='ifMcGeneralIfMcPortStateLastChangeTime'
_g='ifMcGeneralIfMcPortConfigLastChangeTime'
_f='ifMcGeneralIfMcPortTableSize'
_e='ifMcGeneralStateLastChangeTime'
_d='ifMcGeneralConfigLastChangeTime'
_c='IfMcMpoCableType'
_b='IfMcExpectedType'
_a='notApplicable'
_Z='Unsigned32'
_Y='Integer32'
_X='PortNumber'
_W='BoardOrInterfaceOperStatus'
_V='BoardOrInterfaceAdminStatus'
_U='ifMcPortReceivedPowerLow'
_T='DisplayString'
_S='ifMcPortTrxClass'
_R='ifMcPortOperStatus'
_Q='ifMcPortAdminStatus'
_P='read-write'
_O='ifMcPortLossOfSignal'
_N='ifMcGeneralGroupV1'
_M='ifMcPortIfNo'
_L='ifMcPortSlot'
_K='ifMcPortSubrack'
_J='ifMcPortIdx'
_I='ifMcPortExpectedType'
_H='ifMcPortDescr'
_G='ifMcPortName'
_F='read-create'
_E='ifMcPortIndex'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFMC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfMcMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfMcMIB','lumModules')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,FaultStatus,MgmtNameString,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_V,_W,'FaultStatus','MgmtNameString',_X,'SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Y,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_T,'PhysAddress','TextualConvention')
lumIfMcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,64))
if mibBuilder.loadTexts:lumIfMcMIBModule.setRevisions(('2018-07-09 00:00','2018-04-13 00:00','2017-09-01 00:00','2017-06-15 00:00','2015-03-15 00:00'))
class IfMcExpectedType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ethernet100gLanSR10',1),('ethernet12x10gLan',2),('frontplane12x10g',3),('frontplane100g',4),('filter10x10g',5),(_a,6)))
class IfMcMpoCableType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('straight',1),('completeFanout',2),('fanout2x5',3),(_a,4)))
_LumIfMcConfs_ObjectIdentity=ObjectIdentity
lumIfMcConfs=_LumIfMcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,64,1))
_LumIfMcGroups_ObjectIdentity=ObjectIdentity
lumIfMcGroups=_LumIfMcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,64,1,1))
_LumIfMcCompl_ObjectIdentity=ObjectIdentity
lumIfMcCompl=_LumIfMcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,64,1,2))
_LumIfMcMIBObjects_ObjectIdentity=ObjectIdentity
lumIfMcMIBObjects=_LumIfMcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,64,2))
_IfMcGeneral_ObjectIdentity=ObjectIdentity
ifMcGeneral=_IfMcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,64,2,1))
_IfMcGeneralConfigLastChangeTime_Type=DateAndTime
_IfMcGeneralConfigLastChangeTime_Object=MibScalar
ifMcGeneralConfigLastChangeTime=_IfMcGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,64,2,1,1),_IfMcGeneralConfigLastChangeTime_Type())
ifMcGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcGeneralConfigLastChangeTime.setStatus(_B)
_IfMcGeneralStateLastChangeTime_Type=DateAndTime
_IfMcGeneralStateLastChangeTime_Object=MibScalar
ifMcGeneralStateLastChangeTime=_IfMcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,64,2,1,2),_IfMcGeneralStateLastChangeTime_Type())
ifMcGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcGeneralStateLastChangeTime.setStatus(_B)
_IfMcGeneralIfMcPortTableSize_Type=Unsigned32
_IfMcGeneralIfMcPortTableSize_Object=MibScalar
ifMcGeneralIfMcPortTableSize=_IfMcGeneralIfMcPortTableSize_Object((1,3,6,1,4,1,8708,2,64,2,1,3),_IfMcGeneralIfMcPortTableSize_Type())
ifMcGeneralIfMcPortTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcGeneralIfMcPortTableSize.setStatus(_B)
_IfMcGeneralIfMcPortConfigLastChangeTime_Type=DateAndTime
_IfMcGeneralIfMcPortConfigLastChangeTime_Object=MibScalar
ifMcGeneralIfMcPortConfigLastChangeTime=_IfMcGeneralIfMcPortConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,64,2,1,4),_IfMcGeneralIfMcPortConfigLastChangeTime_Type())
ifMcGeneralIfMcPortConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcGeneralIfMcPortConfigLastChangeTime.setStatus(_B)
_IfMcGeneralIfMcPortStateLastChangeTime_Type=DateAndTime
_IfMcGeneralIfMcPortStateLastChangeTime_Object=MibScalar
ifMcGeneralIfMcPortStateLastChangeTime=_IfMcGeneralIfMcPortStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,64,2,1,5),_IfMcGeneralIfMcPortStateLastChangeTime_Type())
ifMcGeneralIfMcPortStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcGeneralIfMcPortStateLastChangeTime.setStatus(_B)
_IfMcPortList_ObjectIdentity=ObjectIdentity
ifMcPortList=_IfMcPortList_ObjectIdentity((1,3,6,1,4,1,8708,2,64,2,2))
_IfMcPortTable_Object=MibTable
ifMcPortTable=_IfMcPortTable_Object((1,3,6,1,4,1,8708,2,64,2,2,1))
if mibBuilder.loadTexts:ifMcPortTable.setStatus(_B)
_IfMcPortEntry_Object=MibTableRow
ifMcPortEntry=_IfMcPortEntry_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1))
ifMcPortEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ifMcPortEntry.setStatus(_B)
_IfMcPortName_Type=MgmtNameString
_IfMcPortName_Object=MibTableColumn
ifMcPortName=_IfMcPortName_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,1),_IfMcPortName_Type())
ifMcPortName.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortName.setStatus(_B)
class _IfMcPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfMcPortIndex_Type.__name__=_Z
_IfMcPortIndex_Object=MibTableColumn
ifMcPortIndex=_IfMcPortIndex_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,2),_IfMcPortIndex_Type())
ifMcPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortIndex.setStatus(_B)
class _IfMcPortDescr_Type(DisplayString):defaultValue=OctetString('')
_IfMcPortDescr_Type.__name__=_T
_IfMcPortDescr_Object=MibTableColumn
ifMcPortDescr=_IfMcPortDescr_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,3),_IfMcPortDescr_Type())
ifMcPortDescr.setMaxAccess(_P)
if mibBuilder.loadTexts:ifMcPortDescr.setStatus(_B)
class _IfMcPortExpectedType_Type(IfMcExpectedType):defaultValue=1
_IfMcPortExpectedType_Type.__name__=_b
_IfMcPortExpectedType_Object=MibTableColumn
ifMcPortExpectedType=_IfMcPortExpectedType_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,4),_IfMcPortExpectedType_Type())
ifMcPortExpectedType.setMaxAccess(_P)
if mibBuilder.loadTexts:ifMcPortExpectedType.setStatus(_B)
class _IfMcPortIdx_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_IfMcPortIdx_Type.__name__=_Y
_IfMcPortIdx_Object=MibTableColumn
ifMcPortIdx=_IfMcPortIdx_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,5),_IfMcPortIdx_Type())
ifMcPortIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortIdx.setStatus(_B)
_IfMcPortSubrack_Type=SubrackNumber
_IfMcPortSubrack_Object=MibTableColumn
ifMcPortSubrack=_IfMcPortSubrack_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,6),_IfMcPortSubrack_Type())
ifMcPortSubrack.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortSubrack.setStatus(_B)
_IfMcPortSlot_Type=SlotNumber
_IfMcPortSlot_Object=MibTableColumn
ifMcPortSlot=_IfMcPortSlot_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,7),_IfMcPortSlot_Type())
ifMcPortSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortSlot.setStatus(_B)
class _IfMcPortIfNo_Type(PortNumber):defaultValue=0
_IfMcPortIfNo_Type.__name__=_X
_IfMcPortIfNo_Object=MibTableColumn
ifMcPortIfNo=_IfMcPortIfNo_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,8),_IfMcPortIfNo_Type())
ifMcPortIfNo.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMcPortIfNo.setStatus(_B)
_IfMcPortLossOfSignal_Type=FaultStatus
_IfMcPortLossOfSignal_Object=MibTableColumn
ifMcPortLossOfSignal=_IfMcPortLossOfSignal_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,9),_IfMcPortLossOfSignal_Type())
ifMcPortLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcPortLossOfSignal.setStatus(_B)
class _IfMcPortAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_IfMcPortAdminStatus_Type.__name__=_V
_IfMcPortAdminStatus_Object=MibTableColumn
ifMcPortAdminStatus=_IfMcPortAdminStatus_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,10),_IfMcPortAdminStatus_Type())
ifMcPortAdminStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:ifMcPortAdminStatus.setStatus(_B)
class _IfMcPortOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_IfMcPortOperStatus_Type.__name__=_W
_IfMcPortOperStatus_Object=MibTableColumn
ifMcPortOperStatus=_IfMcPortOperStatus_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,11),_IfMcPortOperStatus_Type())
ifMcPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcPortOperStatus.setStatus(_B)
class _IfMcPortTrxClass_Type(DisplayString):defaultValue=OctetString('')
_IfMcPortTrxClass_Type.__name__=_T
_IfMcPortTrxClass_Object=MibTableColumn
ifMcPortTrxClass=_IfMcPortTrxClass_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,12),_IfMcPortTrxClass_Type())
ifMcPortTrxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcPortTrxClass.setStatus(_B)
_IfMcPortReceivedPowerLow_Type=FaultStatus
_IfMcPortReceivedPowerLow_Object=MibTableColumn
ifMcPortReceivedPowerLow=_IfMcPortReceivedPowerLow_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,13),_IfMcPortReceivedPowerLow_Type())
ifMcPortReceivedPowerLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMcPortReceivedPowerLow.setStatus(_B)
class _IfMcPortMpoCableType_Type(IfMcMpoCableType):defaultValue=4
_IfMcPortMpoCableType_Type.__name__=_c
_IfMcPortMpoCableType_Object=MibTableColumn
ifMcPortMpoCableType=_IfMcPortMpoCableType_Object((1,3,6,1,4,1,8708,2,64,2,2,1,1,14),_IfMcPortMpoCableType_Type())
ifMcPortMpoCableType.setMaxAccess(_P)
if mibBuilder.loadTexts:ifMcPortMpoCableType.setStatus(_B)
ifMcGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,1))
ifMcGeneralGroupV1.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ifMcGeneralGroupV1.setStatus(_B)
ifMcPortGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,2))
ifMcPortGroupV1.setObjects(*((_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ifMcPortGroupV1.setStatus(_D)
ifMcPortGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,3))
ifMcPortGroupV2.setObjects(*((_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:ifMcPortGroupV2.setStatus(_D)
ifMcPortGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,4))
ifMcPortGroupV3.setObjects(*((_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ifMcPortGroupV3.setStatus(_D)
ifMcPortGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,5))
ifMcPortGroupV4.setObjects(*((_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_Q),(_A,_R),(_A,_S),(_A,_U)))
if mibBuilder.loadTexts:ifMcPortGroupV4.setStatus(_D)
ifMcPortGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,64,1,1,6))
ifMcPortGroupV5.setObjects(*((_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_i)))
if mibBuilder.loadTexts:ifMcPortGroupV5.setStatus(_B)
lumIfMcComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,64,1,2,1))
lumIfMcComplV1.setObjects(*((_A,_N),(_A,_j)))
if mibBuilder.loadTexts:lumIfMcComplV1.setStatus(_D)
lumIfMcComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,64,1,2,2))
lumIfMcComplV2.setObjects(*((_A,_N),(_A,_k)))
if mibBuilder.loadTexts:lumIfMcComplV2.setStatus(_D)
lumIfMcComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,64,1,2,3))
lumIfMcComplV3.setObjects(*((_A,_N),(_A,_l)))
if mibBuilder.loadTexts:lumIfMcComplV3.setStatus(_D)
lumIfMcComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,64,1,2,4))
lumIfMcComplV4.setObjects(*((_A,_N),(_A,_m)))
if mibBuilder.loadTexts:lumIfMcComplV4.setStatus(_D)
lumIfMcComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,64,1,2,5))
lumIfMcComplV5.setObjects(*((_A,_N),(_A,_n)))
if mibBuilder.loadTexts:lumIfMcComplV5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_b:IfMcExpectedType,_c:IfMcMpoCableType,'lumIfMcMIBModule':lumIfMcMIBModule,'lumIfMcConfs':lumIfMcConfs,'lumIfMcGroups':lumIfMcGroups,_N:ifMcGeneralGroupV1,_j:ifMcPortGroupV1,_k:ifMcPortGroupV2,_l:ifMcPortGroupV3,_m:ifMcPortGroupV4,_n:ifMcPortGroupV5,'lumIfMcCompl':lumIfMcCompl,'lumIfMcComplV1':lumIfMcComplV1,'lumIfMcComplV2':lumIfMcComplV2,'lumIfMcComplV3':lumIfMcComplV3,'lumIfMcComplV4':lumIfMcComplV4,'lumIfMcComplV5':lumIfMcComplV5,'lumIfMcMIBObjects':lumIfMcMIBObjects,'ifMcGeneral':ifMcGeneral,_d:ifMcGeneralConfigLastChangeTime,_e:ifMcGeneralStateLastChangeTime,_f:ifMcGeneralIfMcPortTableSize,_g:ifMcGeneralIfMcPortConfigLastChangeTime,_h:ifMcGeneralIfMcPortStateLastChangeTime,'ifMcPortList':ifMcPortList,'ifMcPortTable':ifMcPortTable,'ifMcPortEntry':ifMcPortEntry,_G:ifMcPortName,_E:ifMcPortIndex,_H:ifMcPortDescr,_I:ifMcPortExpectedType,_J:ifMcPortIdx,_K:ifMcPortSubrack,_L:ifMcPortSlot,_M:ifMcPortIfNo,_O:ifMcPortLossOfSignal,_Q:ifMcPortAdminStatus,_R:ifMcPortOperStatus,_S:ifMcPortTrxClass,_U:ifMcPortReceivedPowerLow,_i:ifMcPortMpoCableType})